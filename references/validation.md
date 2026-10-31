# Validation and delivery

Validation has four independent acceptance gates. Record each as passed,
failed or unverified; never report one as proof of another.

| Gate | Evidence | Does not prove |
|---|---|---|
| Semantic correctness | Article/blueprint comparison; independently checked facts and arithmetic | Legibility or visual effectiveness |
| Reference / visual fit | Opened render at reading width; comparison against Reference contract | Correct facts or correct served version |
| Technical validity | Source, geometry, font and applicable regression checks | Clear explanation or user acceptance |
| Host / version agreement | Actual page image URL, loaded asset and fresh host capture | All environments behave identically |

## 1. Content review

Against the approved blueprint and article:

- Does the diagram answer its stated question with one clear conclusion?
- Is the chosen structure appropriate, with no invented hierarchy or causal edge?
- Are every condition, equality boundary, unit and label correct?
- Do omitted details remain available in the caption/prose?
- Are colors consistent across related images and still understandable in grayscale?
- Are explanations beside the relevant objects, rather than a disconnected summary?
- Recompute numbers, coordinate mappings and bar ratios independently.

The generic validator cannot establish any of these from arbitrary SVG.
For plots and bars, add data-specific tests beside the generator.

## 2. Reference and visual fit

When a reference or visual complaint exists, follow
[reference and revision](reference-and-revision.md). Write observable acceptance
criteria and inspect a representative render before batch production. A helper
named `bezier_arrow`, an SVG containing `C`, or a passing validator is not visual
proof. If the requested shape is present but communicates poorly, revise it.

## 3. Source and browser checks

From this skill directory:

```sh
python3 scripts/validate_svg.py path/to/figure.svg
python3 scripts/render_svg.py path/to/figure.svg --output-dir path/to/previews --widths 800 600 --min-text-px 12 --min-support-px 11
```

Source checking uses Python's standard library. Rendering requires Python
Playwright plus an installed Chrome, or Playwright's Chromium with
`--browser chromium`. Missing dependencies must produce an honest failure,
not an automatic global installation.

Choose `--widths` explicitly for the intended embedding contexts. The example
widths are not a fixed host requirement. Ordinary/supporting reading floors
are configurable with `--min-text-px` / `--min-support-px`; both must be
positive finite CSS-pixel values. The report records the thresholds used.

The renderer creates PNGs and a JSON report. Open the PNGs and inspect them.
It measures text bounds, overlap, title centering, rendered text sizes and
reports actual fonts. It checks standalone SVG at specified widths, not
the real article DOM. Host integration must also be tested separately.

The source checker checks unique IDs, references, accessible descriptions,
title anchor and known unsafe content, plus shape-only filter placement
and semantic connector markers. It is a contract check, not a security
sandbox for arbitrary untrusted SVG.

Use librsvg's `rsvg-convert` as an additional renderer if installed. Chrome
is the supported default here. State which renderer actually ran.
Do not claim success from an unrun or substituted check.

## 4. Visual iteration and host agreement

Look at rendered output:

1. What does the reader notice in five seconds?
2. Does the visual path follow the intended relation?
3. Are arrowheads visible, with no unintended crossings or disconnected branches?
4. Is every title centered on its whole canvas and every label within bounds?
5. Can labels be read at the actual embedded size without enlargement?
6. Are numbers and visual proportions mutually consistent?
7. Did the latest fix introduce a new issue elsewhere?

Fix failures and rerender. A pass from automatic geometry checks does not
replace this review. Do not spawn review agents without the user's required
delegation authorization; direct inspection remains necessary.

After visual iteration, reopen the actual article and check the image URL,
loaded asset and rendering. For visual changes, show a fresh host capture where
possible; a standalone render is not host evidence. If the user sees a different
version, compare the served resource to the intended artifact before diagnosing
the cause. If the host cannot be reached, state that limitation and show the
standalone render instead.

## Acceptance artifacts

Deliver the approved blueprint, final selectable SVG, generator if used,
data-specific tests and verification evidence. PNG previews are helpful but
not a substitute for SVG. Keep filenames stable only when replacement was
authorized. Never publish a comparison page without being asked.

Report what changed, what each image explains, checks actually run and
unverified dependencies. Do not call the result publication-ready solely
because it compiles.
