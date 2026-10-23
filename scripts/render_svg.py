"""Validate and render standalone SVGs in Chrome; emit geometry and font evidence."""

import argparse
import json
import math
from pathlib import Path

from validate_svg import validate


GEOMETRY = r"""(svg, limits) => {
  const frame = svg.getBoundingClientRect(), errors = [], sizes = [];
  const text = [...svg.querySelectorAll('text')];
  const titles = text.filter(t => t.hasAttribute('data-rg-title'));
  for (const t of text) {
    const r = t.getBoundingClientRect(), m = t.getScreenCTM();
    const size = parseFloat(getComputedStyle(t).fontSize) * Math.hypot(m.a, m.b);
    sizes.push(size);
    if (r.left < frame.left - 1 || r.right > frame.right + 1 ||
        r.top < frame.top - 1 || r.bottom > frame.bottom + 1)
      errors.push('Text outside canvas: ' + t.textContent);
    const supporting = t.classList.contains('rg-support');
    if (size < (supporting ? limits.supporting : limits.ordinary))
      errors.push('Text below reading floor: ' + t.textContent);
    const g = t.closest('g[data-rg-node]');
    if (g) {
      const shape = g.querySelector('.rg-shape');
      if (shape) {
        const b = shape.getBoundingClientRect();
        if (r.left < b.left || r.right > b.right || r.top < b.top || r.bottom > b.bottom)
          errors.push('Text outside node: ' + t.textContent);
      }
    }
  }
  for (const t of titles) {
    const b = t.getBoundingClientRect();
    if (Math.abs((b.left+b.right)/2 - (frame.left+frame.right)/2) > 1)
      errors.push('Title not centered on canvas');
  }
  for (let i=0;i<text.length;i++) for (let j=i+1;j<text.length;j++) {
    const a=text[i].getBoundingClientRect(), b=text[j].getBoundingClientRect();
    if (Math.min(a.right,b.right)-Math.max(a.left,b.left)>1 &&
        Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>1)
      errors.push('Text overlap: '+text[i].textContent+' / '+text[j].textContent);
  }
  return {errors, width:frame.width, height:frame.height,
          minimumTextPx:Math.min(...sizes), maximumTextPx:Math.max(...sizes),
          declaredFont:getComputedStyle(text[0]).fontFamily};
}"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("svg", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--widths", type=int, nargs="+", required=True,
                        help="Explicit viewport widths for the intended reading contexts")
    parser.add_argument("--min-text-px", type=float, default=12,
                        help="Minimum rendered ordinary-text size (default: 12 CSS px)")
    parser.add_argument("--min-support-px", type=float, default=11,
                        help="Minimum rendered supporting-text size (default: 11 CSS px)")
    parser.add_argument("--browser", choices=("chrome", "chromium"), default="chrome")
    args = parser.parse_args()
    if not all(math.isfinite(v) and v > 0 for v in (args.min_text_px, args.min_support_px)):
        parser.error("Minimum text sizes must be positive and finite")
    source = args.svg.read_text(encoding="utf-8")
    errors = validate(source)
    if errors:
        parser.error("Source check failed: " + "; ".join(errors))
    if any(w <= 0 for w in args.widths) or len(args.widths) != len(set(args.widths)):
        parser.error("Widths must be positive and distinct")
    outputs = [args.output_dir / f"{args.svg.stem}-{w}.png" for w in args.widths]
    report_path = args.output_dir / f"{args.svg.stem}-report.json"
    if any(p.exists() for p in outputs + [report_path]):
        parser.error("Preview output exists; choose a fresh directory")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        parser.error("Rendering requires Python Playwright and Chrome/Chromium")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    reports = []
    with sync_playwright() as playwright:
        options = {"channel": "chrome"} if args.browser == "chrome" else {}
        browser = playwright.chromium.launch(headless=True, **options)
        try:
            for width, output in zip(args.widths, outputs):
                page = browser.new_page(viewport={"width": width, "height": 1200})
                try:
                    page.set_content('<!doctype html><html><head><style>'
                                     'body{margin:0}svg{display:block}</style></head>'
                                     '<body>' + source + '</body></html>')
                    page.evaluate("document.fonts.ready")
                    svg = page.locator("svg.logic2image")
                    limits = {"ordinary": args.min_text_px, "supporting": args.min_support_px}
                    report = svg.evaluate(GEOMETRY, limits)
                    report["readingFloorsPx"] = limits
                    session = page.context.new_cdp_session(page)
                    session.send("DOM.enable")
                    session.send("CSS.enable")
                    doc = session.send("DOM.getDocument")
                    node = session.send("DOM.querySelector", {
                        "nodeId": doc["root"]["nodeId"], "selector": "svg.logic2image"})
                    report["actualFonts"] = session.send(
                        "CSS.getPlatformFontsForNode", {"nodeId": node["nodeId"]})["fonts"]
                    report["renderer"] = args.browser
                    report["requestedWidth"] = width
                    svg.screenshot(path=str(output))
                    reports.append(report)
                finally:
                    page.close()
        finally:
            browser.close()
    report_path.write_text(json.dumps(reports, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(reports, indent=2))
    raise SystemExit(any(r["errors"] for r in reports))


if __name__ == "__main__":
    main()
