# Semantic color palette

Use these fixed light-theme values.
The complete machine-readable palette is included in `../assets/palette.json`.
The palette's permission notice is included alongside it in `../assets/LICENSE`.
Names identify colors, not business meanings: `teal` is visibly blue-cyan and
`coral` is orange-brown. Use the hex values rather than guessing from names.

| Role token | Shape fill | Shape / connector stroke | Main text | Supporting text |
|---|---|---|---|---|
| purple | `#faecf9` | `#a626a4` | `#771977` | `#a626a4` |
| teal | `#e1f3fa` | `#0184bc` | `#015f88` | `#0184bc` |
| coral | `#fbeee2` | `#ca6f1e` | `#925113` | `#ca6f1e` |
| pink | `#fce8ee` | `#b83260` | `#852344` | `#b83260` |
| gray | `#f0f0f1` | `#5c5e66` | `#383a42` | `#5c5e66` |
| blue | `#e6efff` | `#4078f2` | `#1a52cf` | `#4078f2` |
| green | `#e8f3e2` | `#50a14f` | `#3a7639` | `#50a14f` |
| amber | `#fbeed8` | `#c18401` | `#8c6001` | `#c18401` |
| red | `#fde8e6` | `#e45649` | `#a83329` | `#e45649` |

Neutral main ink: `#383a42`; secondary ink: `#696c77`.
Use dark main ink for small important labels if supporting ink lacks contrast
at the actual reading size.

The scaffold defines both `--rg-ink` and `--rg-support` on every role group.
Ordinary text uses main ink; `text.rg-support` and `tspan.rg-support` use
supporting ink. Outside a role, supporting text uses the neutral secondary
ink above. Main and supporting inks remain distinct within each role.

## Semantic allocation

Assign distinct colors to distinct roles; repeat the same color whenever
the same role reappears. Multiple semantic colors are intentional, not
visual noise. Keep direct labels so grayscale readers can understand it.
Do not add extra hues for every box or enforce a universal red/green meaning.

Derive the mapping from the current article rather than a previous task:

1. Identify meaningful entities, categories, states and comparisons.
2. Decide what readers need to distinguish or follow across the image.
3. Assign palette colors to those semantic roles and record the mapping
   in the blueprint. Color names alone do not prescribe meaning.
4. Reuse each mapping across related figures. In an overview, distinct
   concept clusters may use distinct colors; carry each cluster's color
   into its detail diagrams so readers can follow the same theme. This
   does not require creating an overview. A repeated word is not enough:
   preserve color when the underlying role or meaning is the same, and
   reassess the mapping if that meaning changes.
5. Check the focal contrast and retain explicit labels so meaning does not
   depend on color alone.

Choose the mapping independently from the supplied content. Do not permanently
bind a color to a particular industry, product, actor or metric. Red and green,
for example, do not automatically mean failure and success.
Use multiple colors where they distinguish meaningful roles, not to give
every individual item an arbitrary unique hue.

Respect a user-specified mapping or an established convention in an existing
series. Ask before changing that convention; ask about ambiguous semantics
rather than guessing. Do not silently recolor unrelated existing figures.

## Integration

Use a uniquely scoped root ID and role groups or attributes. Explicitly
apply each role's fill, stroke and text colors; ensure nested group and
selector behavior is correct. Keep styles scoped to the current SVG and
avoid competing stylesheets that override its role variables or typography.
Do not inherit untested dark behavior.
