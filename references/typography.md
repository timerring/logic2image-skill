# Typography and integration

English text uses `Georgia, serif` consistently. Do not import Comic Sans,
Ma Shan Zheng, or any web font. Fonts are not bundled: verify the actual
rendered font, and disclose a fallback rather than claiming exact Georgia.

## Match the host's body text

Use the surrounding text and the space the figure occupies to choose the
target label size. For a slide, account for viewing distance. The 17px
column below illustrates the scaffold's starting proportions.
Recommended ratios at the intended reading width:

| Role | Body-size multiple | At 17px body |
|---|---|---|
| Ordinary label | 1.0 | 17px |
| Supporting text | 0.9 | 15.3px |
| Whole-figure title | 1.3 | 22.1px |

Apply `rg-support` to an auxiliary `text` or `tspan`, not its containing
group. It uses the current color role's supporting ink, or neutral
`#696c77` outside a role. Ordinary text and titles use that role's main ink,
or neutral `#383a42`. Nested role groups reset both ink variables together.
Do not mark an essential conclusion or result as supporting text merely
to make it fit. Prefer one or two supporting lines per node; move longer
qualifications into the caption instead of shrinking the image.
If supporting ink lacks contrast at the intended reading size, use the
role's darker main ink explicitly and record the accessibility reason.
Do not silently replace all supporting colors with one generic gray.

Adjust hierarchy only with a concrete reason. Long titles wrap or become
shorter; do not shrink everything to fit.

For uniform scaling:

```text
rendered_font_px = svg_font_units * rendered_svg_width / viewBox_width
svg_font_units = target_font_px * viewBox_width / intended_rendered_width
```

Inspect actual transforms if the diagram has nested scaling. SVG font-size
attributes are user units; a value of 48 does not mean 48 screen pixels.

The scaffold requires intended display width and target ordinary-text size
as explicit inputs (`--display-width`, `--body-px`). Its working canvas
dimensions are configurable; the 1600×900 defaults do not prescribe a host
layout. Choose display widths and any scrolling policy from the actual
embedding context.

## Center the whole-figure title

For `viewBox="x0 y0 W H"`:

```xml
<text data-rg-title="true" x="x0 + W/2" text-anchor="middle">Title</text>
```

Write the actual numeric x value, not the expression. For multiple lines,
use tspans sharing the same center x. Verify that the rendered bounding-box
midpoint agrees with the whole canvas midpoint.
Centering the SVG element in HTML does not center internal text.
Do not center the title on an asymmetric plot or one panel.
Axis titles, row headers, value labels and annotations keep their own
meaningful alignment; they are not whole-figure titles.

## Readability on narrow screens

For responsive screen content, check the intended display width and the
narrowest supported container. When its minimum width is unknown, use a
**360 CSS px content width** for the narrow preview and record that assumption
in the blueprint. Check that the rendered SVG fits inside the container and
that the text meets the chosen reading floors. If either check fails, revise
the layout and recheck both widths.

For fixed-size output, use the figure's actual placement. Inspect a slide at
its intended presentation size and viewing distance, or a printed figure at
its final physical size. If the same figure also has a responsive web version,
check that version at its supported widths.

Prefer layout adaptation, stacking, shorter labels or split figures before
shrinking. If the task requires a larger reading surface, explicitly agree
on horizontal scrolling or an enlarged view. A clipped screenshot is not
a mobile-readability pass.

Check the actual host at its intended reading widths. The renderer requires
explicit `--widths`; its screen-oriented reading floors default to 12px
for ordinary text and 11px for supporting text. Configure them using
`--min-text-px` and `--min-support-px` for the actual reading context.
These are floors, not desired sizes. Printed output or projection still
requires review at its physical size or viewing distance, not just pixel checks.
Check wrapping, title centering, node padding and line/label collisions again
after changing font family or display width.
