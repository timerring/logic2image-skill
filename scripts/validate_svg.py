"""Check the logic2image SVG contract, not semantics or arbitrary SVG security."""

import argparse
import json
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET


SKILL = Path(__file__).resolve().parents[1]
NS = "{http://www.w3.org/2000/svg}"


def validate(source):
    errors = []
    if "<!DOCTYPE" in source.upper() or "<!ENTITY" in source.upper():
        return ["DOCTYPE and entity declarations are not allowed"]
    try:
        root = ET.fromstring(source)
    except ET.ParseError as error:
        return [f"Invalid XML: {error}"]
    if root.tag != NS + "svg":
        return ["Root must be SVG in the SVG namespace"]
    try:
        x, y, w, h = map(float, root.get("viewBox", "").split())
        if not all(math.isfinite(v) for v in (x, y, w, h)) or min(w, h) <= 0:
            raise ValueError
    except ValueError:
        return ["viewBox must contain four finite numbers with positive width/height"]
    if root.get("role") != "img":
        errors.append("Root must have role=img")
    ids = [e.get("id") for e in root.iter() if e.get("id")]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate IDs")
    for attr in ("aria-labelledby", "aria-describedby"):
        targets = root.get(attr, "").split()
        if not targets or any(t not in ids for t in targets):
            errors.append(f"Missing or unresolved {attr}")
    for name in ("title", "desc"):
        element = root.find(NS + name)
        if element is None or not "".join(element.itertext()).strip():
            errors.append(f"Missing accessible {name}")
    titles = [e for e in root.iter(NS + "text") if e.get("data-rg-title") == "true"]
    if len(titles) != 1:
        errors.append("Exactly one whole-figure title is required")
    else:
        title = titles[0]
        try:
            centered = abs(float(title.get("x", "")) - (x + w / 2)) < .01
        except ValueError:
            centered = False
        if not centered or title.get("text-anchor") != "middle":
            errors.append("Whole-figure title must be centered on the full viewBox")
        for span in title.iter(NS + "tspan"):
            if span.get("x") is not None and span.get("x") != title.get("x"):
                errors.append("Title tspans must share the title center")
    contents = [e for e in root.iter() if e.get("data-rg-content") == "true"]
    if not contents or not any(list(e) for e in contents):
        errors.append("Drawing is an empty scaffold")
    roles = json.loads((SKILL / "assets/palette.json").read_text())["roles"]
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1]
        if tag in {"script", "foreignObject", "image", "use", "a", "animate", "set"}:
            errors.append(f"Unsupported element: {tag}")
        for attr in element.attrib:
            local = attr.rsplit("}", 1)[-1].lower()
            if local.startswith("on") or local in {"href", "src"}:
                errors.append(f"Unsupported attribute: {local}")
        role = element.get("data-rg-role")
        if role and role not in roles:
            errors.append(f"Unknown palette role: {role}")
        if "filter" in element.attrib or "filter:" in element.get("style", "").replace(" ", ""):
            if tag not in {"rect", "ellipse", "circle", "path", "polygon"} or element.get("data-rg-kind") != "shape":
                errors.append("Filter must be directly on a decorative shape, never an ancestor/text/data/connector")
        if element.get("data-rg-kind") == "connector":
            if tag not in {"line", "path", "polyline"} or "marker-end" not in element.attrib:
                errors.append("Directed connector needs a line/path and marker-end")
            try:
                if float(element.get("stroke-width", "0")) < 3 * w / 1600:
                    errors.append("Connector stroke is too thin")
            except ValueError:
                errors.append("Connector stroke must be numeric")
    for style in root.iter(NS + "style"):
        css = style.text or ""
        if "@import" in css or "@font-face" in css:
            errors.append("External/imported fonts and styles are not allowed")
        # Keep shape filter use explicit and inspectable in attributes.
        if re.search(r"\bfilter\s*:", css):
            errors.append("CSS filters are not allowed; annotate filtered shapes directly")
        if not re.search(r"font-family\s*:\s*['\"]?Georgia", css):
            errors.append("Embedded style must declare Georgia")
        selectors = re.findall(r"(?:^|})\s*([^{}]+)\{", css)
        if not root.get("id") or any(
            not part.strip().startswith("#" + root.get("id", "") + " ")
            for selector in selectors for part in selector.split(",")
        ):
            errors.append("Style selectors must be scoped to the root ID")
    if root.find(".//" + NS + "style") is None:
        errors.append("A self-contained embedded stylesheet is required")
    for target in re.findall(r"url\(\s*['\"]?([^)'\"\s]+)", source):
        if not target.startswith("#") or target[1:] not in ids:
            errors.append(f"External or unresolved reference: {target}")
    return sorted(set(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("svg", type=Path)
    args = parser.parse_args()
    errors = validate(args.svg.read_text(encoding="utf-8"))
    print(json.dumps({"file": str(args.svg), "errors": errors}, indent=2))
    raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
