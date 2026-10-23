"""Create a self-contained, uniquely scoped SVG scaffold; never overwrite a file."""

import argparse
from html import escape
import json
import math
from pathlib import Path
from string import Template
import uuid


SKILL = Path(__file__).resolve().parents[1]


def make_svg(title, description, width=1600, height=900, *, display_width, body_px):
    if not title.strip() or not description.strip():
        raise ValueError("Title and description must be nonempty")
    if not all(math.isfinite(v) and v > 0 for v in (width, height, display_width, body_px)):
        raise ValueError("Dimensions and body size must be positive and finite")
    palette = json.loads((SKILL / "assets/palette.json").read_text())
    prefix = "rg-" + uuid.uuid4().hex[:12]
    scope = "#" + prefix
    ordinary = body_px * width / display_width
    css = [
        f"{scope} text {{ font-family: Georgia, serif; font-weight:400; "
        f"font-size:{ordinary:.6f}px; fill:var(--rg-ink,{palette['neutral_ink']}); }}",
        f"{scope} .rg-title {{ font-size:{ordinary * 1.3:.6f}px; }}",
        f"{scope} .rg-support {{ font-size:{ordinary * .9:.6f}px; "
        f"fill:var(--rg-support,{palette['secondary_ink']}); }}",
        f"{scope} .rg-shape {{ fill:var(--rg-fill); stroke:var(--rg-stroke); "
        f"stroke-width:{3.5 * width / 1600:.6f}; }}",
    ]
    for role, values in palette["roles"].items():
        css.append(
            f'{scope} [data-rg-role="{role}"] {{ --rg-fill:{values["fill"]}; '
            f'--rg-stroke:{values["stroke"]}; --rg-ink:{values["ink"]}; '
            f'--rg-support:{values["supporting"]}; }}'
        )
    return Template((SKILL / "templates/canvas.svg").read_text()).substitute(
        prefix=prefix, width=width, height=height, center=width / 2,
        title_y=height / 9, title=escape(title), description=escape(description),
        css="\n" + "\n".join(css) + "\n",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--width", type=int, default=1600)
    parser.add_argument("--height", type=int, default=900)
    parser.add_argument("--display-width", type=int, required=True,
                        help="Intended rendered SVG width in CSS pixels")
    parser.add_argument("--body-px", type=float, required=True,
                        help="Target ordinary-label size in CSS pixels at that width")
    args = parser.parse_args()
    try:
        svg = make_svg(args.title, args.description, args.width, args.height,
                       display_width=args.display_width, body_px=args.body_px)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as output:
            output.write(svg)
    except (ValueError, FileExistsError) as error:
        parser.error(str(error))
    print(f"Created scaffold: {args.output}; add content before validation/delivery.")


if __name__ == "__main__":
    main()
