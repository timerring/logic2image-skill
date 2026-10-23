# Plan before drawing

Create a Markdown blueprint before SVG code. Use the complete form in
`../templates/diagram-plan.md`. For a new multi-image article, show the
blueprints to the user and wait for approval. An already approved plan or
an explicit instruction to proceed is sufficient; do not ask repeatedly
for font-only or alignment-only revisions.

## Choose the relationship, then the shape

| Content | Natural diagram | Required evidence |
|---|---|---|
| Ordered transformations | Pipeline / timeline | Order and transition meaning |
| Condition selects an outcome | Branching decision | Complete conditions, including equality |
| A process returns to a prior state | Feedback / loop | Actual return edge and destination |
| Genuine parent-child concepts | Tree / nested boundaries | Actual hierarchy or ownership |
| Independent modules at the same level | Parallel columns / aligned lanes | Comparable criteria |
| Two independent dimensions | Labeled matrix | Both row and column meanings |
| Before/after or old/new | Aligned comparison | What changed and what is held constant |
| Magnitude or change | Shared-scale bars / bridge | Values, units and baseline |
| Numeric output varies with input | Function plot | Formula or data and meaningful domain |

Do not force a common root on unrelated concepts. Do not draw arrows
between simultaneous alternatives. A tree is not a universal knowledge map.
One diagram normally has one message and at most 7–9 peer elements; split
larger structures into focused diagrams, usually no more than two hierarchy
levels per image.

## Choose a series only when necessary

- An overview maps 3–6 major concept clusters when the whole article benefits.
  Its title identifies the article, not a generic "Overview".
- Detail diagrams explain mechanisms or comparisons, each with a specific title.
- Keep an entity's role color consistent between overview and detail views.
- Do not automatically add a learning path, gap analysis or decorative summary.

## Blueprint contents

Record exact visible text, node identities, relations, arrow labels, units,
formula/data source, color roles, diagram filename and insertion location.
List absent connections explicitly when their absence matters.
For plots, replace a node list with axes, domain, formula, reference lines
and annotation coordinates. For matrices, list dimensions and cell meanings.

Explanations should sit beside the feature they explain: a threshold label
near the crossing, a conversion rate near the conversion, a distinction
near the compared entities. Avoid a disconnected "key insights" box.
Include enough wording that labels make sense without requiring a full
reread of the article; use short meaningful phrases, not cryptic keywords.
Show shared assumptions once, outside repeated nodes. Keep long derivations,
repeated caveats and excess decimal places in the caption or adjacent prose.
Do not use paragraphs inside boxes or add a default three-card summary when
a boundary, axis or direct comparison would communicate the relationship.
Conversely, do not invent numerical axes for purely categorical information.

## Spatial plan

Honor a requested aspect ratio. When unspecified, start with 16:9 for a
presentation-oriented task. For a blog, measure the real embedding column
before choosing the final canvas; recommend a different ratio if it helps.
Do not silently impose 1600×900 on every structure.

Wide canvases favor horizontal flow; tall ones favor vertical flow; squares
can suit balanced matrices or genuine radial relationships. Reserve the
whole-figure title area, drawing area and caption space.

At a 1600-unit working width, roughly 60-unit gaps and 40-unit internal
padding are starting budgets. Fit content and arrowheads, then scale the
budget if the working width changes. Avoid both cramped nodes and large
empty areas with no explanatory purpose.

## Approval boundary

Content approval is distinct from aesthetic approval. Report changes to
facts, conditions, grouping or chart type before treating a revised picture
as equivalent. For an unchanged approved blueprint, iterate layout without
asking the user to reapprove the same content.
