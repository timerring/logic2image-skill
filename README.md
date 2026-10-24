<h1 align="center">logic2image</h1>

<p align="center"><strong>English</strong> | <a href="README.zh-CN.md">简体中文</a></p>

<p align="center">From logic to image.</p>

## Examples

Example diagrams generated with logic2image. Click a preview to view the full SVG.

<table>
  <tr>
    <th width="50%">Contract counterparties</th>
    <th width="50%">Option payoff</th>
  </tr>
  <tr>
    <td align="center" valign="top"><a href="examples/contract-counterparties.svg"><img src="examples/contract-counterparties.svg" alt="Rights, obligations and premium flow" width="360"></a></td>
    <td align="center" valign="top"><a href="examples/option-payoff.svg"><img src="examples/option-payoff.svg" alt="Exercise value versus net profit" width="360"></a></td>
  </tr>
  <tr>
    <td align="center">Buyer rights, seller obligations<br>and premium flow.</td>
    <td align="center">Illustrative gold call, one troy ounce.<br>Strike 4,150 USD; premium 50 USD.<br>Costs excluded.</td>
  </tr>
</table>

## What it does

- Reads an article, identifies its key relationships and suggests where diagrams help.
- Selects flows, comparisons, matrices or quantitative charts to match the content.
- Drafts figure titles, labels, connections and data before drawing.
- Creates editable SVGs and renders PNG previews.
- Checks SVG structure, text overlap and readability, then refines the figures.

## Use

Place this folder at `.agents/skills/logic2image/` in your project.
Invoke `/logic2image` in a compatible agent, or ask it to read [SKILL.md](SKILL.md).

> Use logic2image to illustrate this article. First propose the figure locations,
> the question each figure answers, and a content blueprint. Wait for my approval
> before drawing.

To proceed without another approval round, explicitly authorize the agent to
plan and draw. Existing images are replaced only when requested.

## Workflow

**Understand → Select → Blueprint → Draw → Validate → Refine**

One message per figure. No forced hierarchy, invented data or mandatory image
count. If prose or a table is clearer, no extra diagram is needed.

## Tools

From this folder, after the agent has completed a figure:

```sh
python3 scripts/validate_svg.py figure.svg
python3 scripts/render_svg.py figure.svg --output-dir previews --widths 800 600
```

Python 3 is required for the tools. Rendering additionally needs Playwright and
Chrome; Georgia must be available for exact typography. Nothing is installed
automatically. No image-generation API is required.

The included scaffold creates an **empty starting point**, not a finished
diagram. See the [validation guide](references/validation.md).
Source checks do not replace content review or real article-page checks.
Choose display width and text size explicitly when creating a scaffold;
render widths are also required. Reading floors are configurable with
`--min-text-px` and `--min-support-px` (defaults: 12px and 11px).

## Files

| Path | Purpose |
|---|---|
| `SKILL.md` | Agent entry point |
| `references/` | Content, layout, drawing and typography rules |
| `assets/` | Complete semantic palette |
| `templates/` | Content blueprint and SVG scaffold |
| `scripts/` | Scaffold, source checks and browser rendering |
| `examples/` | SVG examples |

## Acknowledgements

- Parts of the article comprehension workflow were informed by [chingswy/Skill-Research-Figure](https://github.com/chingswy/Skill-Research-Figure).
- SVG color schemes were adapted from [canmi21/lib](https://github.com/canmi21/lib).
