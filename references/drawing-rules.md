# Draw the SVG

Use native selectable SVG. Do not replace diagrams with screenshots or
outline the text. English labels and accessible descriptions are the default.
Use unique root IDs and prefix every marker, filter, pattern, title and
description ID; multiple inline images must not collide.

## Shapes and layers

For workflows, use:

| Meaning | Useful shape |
|---|---|
| Actor or role | Ellipse |
| Processing step | Rounded rectangle |
| Shared phase or ownership | Larger grouping boundary |
| Decision | Diamond, only when it clarifies a real decision |
| Data / output | Parallelogram when useful |
| Optional system boundary | Dashed boundary |

These are choices, not obligations for plots or matrices. Draw backgrounds
first, connectors next, and foreground shapes/text last as appropriate.
Never let a background overlay wash out text.

Use the local palette JSON and readable palette table. The supplied scaffold
embeds all CSS in the SVG, scoped to one root ID. Copy the asset values, not
colors remembered from another style. Keep named roles stable across images.

## Subtle sketch treatment

The scaffold provides a shape-only filter:

```xml
<filter id="unique-sketch" x="-3%" y="-3%" width="106%" height="106%">
  <feTurbulence type="turbulence" baseFrequency="0.03"
    numOctaves="4" seed="2" result="noise"/>
  <feDisplacementMap in="SourceGraphic" in2="noise" scale="2.5"
    xChannelSelector="R" yChannelSelector="G"/>
</filter>
```

Apply it directly to decorative shape outlines, not to a group containing
other elements. Never filter text, connectors, axes, quantitative bars,
data points, numeric curves, or an ancestor of those elements.

For optional diagonal hatching, use an 8–10-unit pattern rotated -45 degrees
at the 1600-unit scale, with stroke around 1.5 and opacity .3–.5.
Use the role's stroke color. Put the hatch on top of the opaque role fill;
do not lighten or replace the original palette with a new translucent color.
Remove texture where it hurts readability. Data geometry stays exact even
when a surrounding decorative container is sketchy.

## Connections

Make a checklist of every semantic connection in the blueprint.

1. Every directed connector has a visible arrowhead; guides and dividers do not.
2. Use an approximately 3-unit or thicker stroke at a 1600-unit working width,
   then verify actual screen visibility. Scale stroke and marker together.
3. Marker ink matches its connector. The scaffold uses `context-stroke`.
4. Route process connectors horizontally/vertically around unrelated shapes.
5. Land at the intended target anchor. For a top-entry arrow, align its final
   segment to the target center x; for side entry, align to the center y.
6. Leave about 5–10 working units of edge clearance so tips remain visible.
7. Place connector labels beside the line, not on top of it. A 15–20-unit
   offset is a starting point; verify rendered text bounds.
8. For branching, use a continuous shared trunk and deliberate branches;
   do not overlay shortened arrows that leave unintended gaps.
9. No filters, including inherited filters, on any connector.

In generated files, mark shapes `data-rg-kind="shape"`, directed edges
`data-rg-kind="connector"`, guides `data-rg-kind="guide"` and quantitative
marks `data-rg-kind="data"`. These annotations enable structural checks;
they do not prove that the semantics or arithmetic are correct.

## Quantitative correctness

Declare the source data or formula in the blueprint. Compute coordinates
from one common scale. For linear mapping:

```text
x = x_left + (value - domain_min) / (domain_max - domain_min) * plot_width
y = y_bottom - (value - range_min) / (range_max - range_min) * plot_height
```

Recompute representative points independently. Include thresholds and exact
breakpoints; do not smooth a piecewise function. Round display labels only,
not the geometry calculation.
Magnitude bars normally share a zero baseline. Label any justified alternative
scale explicitly. A visible difference must be proportional to the numbers.
Shading needs a stated meaning; never imply probability, forecasts or confidence
intervals without evidence. Units and equality conditions belong in the image
or its immediately adjacent caption.
Label the meaning of dashed numeric references, such as a zero baseline,
threshold or comparison reference; do not make readers guess whether they
are data or guides.

## Output safety

Use a meaningful viewBox, accessible title and description, and a unique root
class/ID. Embed needed styles and definitions. No scripts, event handlers,
external images, web fonts, linked stylesheets or foreignObject.
Default background is white. Dark-mode behavior is not automatic; only claim
it after separately implementing and testing it.
Version exploratory files. Replace existing article assets only when authorized.
