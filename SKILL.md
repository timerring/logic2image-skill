---
name: logic2image
description: Plan and create English blog SVG illustrations using article comprehension, explicit diagram blueprints, drawing checks, a semantic palette and Georgia typography. Use for article illustration, flows, matrices, comparisons and quantitative explanations, including requests to choose what to draw before drawing.
---

# logic2image

A self-contained article-to-SVG workflow. All required rules, palette values,
templates and tools are physically included here. Do not load another skill,
fetch an upstream guide or read a personal directory to execute this workflow.
Attributions appear in the README acknowledgements. Retained copyright
notices are preserved separately.

## Scope

Create accurate, readable article illustrations, not a mandatory learning
report or a fixed bundle of diagrams. Content and chart choice come before
styling. Keep old skills and existing article assets unchanged unless asked.
Default output is English native SVG with selectable Georgia text.

## Workflow and required local files

1. **Understand the article.** Read `references/article-understanding.md`.
   Extract thesis, concepts, prerequisites, relations and evidence; then
   identify useful illustration locations. Do not start with coordinates.
2. **Plan the images.** Read `references/diagram-planning.md`, and fill
   `templates/diagram-plan.md`. State what goes in each image, why that
   chart type fits, and what remains in prose. Seek content approval for a
   new multi-image plan unless already authorized to proceed.
3. **Design and draw.** Read `references/drawing-rules.md`,
   `references/palette.md` and `references/typography.md`. Use the complete
   local palette in `assets/palette.json`, not a substitute color scheme.
   Draft SVG from the scaffold or write native SVG following the same contract.
4. **Validate and render.** Read `references/validation.md`. Run source checks,
   recompute quantitative data, render and inspect images at actual reading
   widths, and then verify the real article integration.
5. **Iterate and deliver.** Fix semantic and visual failures before delivery.
   Report actual checks, fonts, output files and remaining limitations.

## Non-negotiable decisions

- Understand actors, phases, steps and connections where they exist; do not
  force a workflow, tree or common root onto unrelated content.
- Distinguish conditions, matrices, comparisons and numeric functions.
- One clear message per image; a figure is optional if prose/table is enough.
- Analyze the current content to assign semantic color roles from the palette.
  Preserve established mappings within a related series. Use direct labels
  as well as color; do not reduce the palette to one accent without asking.
- English uses `Georgia, serif`; ordinary text aims at the host body size.
- Center each whole-figure title on the full viewBox, not on one panel.
- Filter decorative shapes only; never filter text or quantitative geometry.
- Validate data, units and equality boundaries independently of layout.
- No automatic subagent delegation, network generation API, publication or
  destructive asset replacement. Respect the user's authorization boundaries.

## Included tools

Run from this skill directory; paths can be absolute when invoked elsewhere:

```sh
python3 scripts/new_diagram.py /path/to/output.svg \
  --title "A precise conclusion" --description "What the figure explains" \
  --width 1600 --height 900 --display-width 800 --body-px 18
python3 scripts/validate_svg.py /path/to/output.svg
python3 scripts/render_svg.py /path/to/output.svg \
  --output-dir /path/to/previews --widths 800 600 \
  --min-text-px 12 --min-support-px 11
```

`new_diagram.py` creates an intentionally empty drawing scaffold, not an
automatic layout or finished illustration. Add the blueprint's content
inside its marked content group. Do not deliver the scaffold as a figure.
The source checker rejects an empty drawing.

Display width and target ordinary-text size must be specified explicitly;
choose them from the actual destination rather than assuming a blog layout.
Rendering also requires explicit check widths. The example dimensions above
are illustrative. Reading floors default to 12px/11px for screen inspection
and can be changed with `--min-text-px` and `--min-support-px`.

The source checker and scaffold need only Python 3. Rendering additionally
requires Playwright and Chrome/Chromium. They are not bundled or installed
automatically. SVG font appearance depends on Georgia availability.
No TeX, Blender or external image-generation service is needed for this SVG
workflow; unrelated upstream tools are not included as unused dependencies.

## Integration boundary

This skill does not depend on a host project's specialized generator or
assume a particular article domain. Analyze each task's actual content and
embedding context. Replacing existing assets requires authorization.
