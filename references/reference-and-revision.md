# Reference-first drawing and feedback repair

This is a workflow correction, not a requirement to add curves everywhere.
Use it whenever a user supplies a reference, disputes the visible result, or
asks why the current visual does not explain the intended mechanism.

## 1. Reference contract

Inspect the actual supplied screenshot/SVG/figure, not only its caption. Record:

- **Semantic invariants:** actors, relations, conditions, order, units and facts.
- **Explanatory geometry:** for example a return arc beneath a forward sequence,
  separated critical/background paths, a common-scale comparison, visible queue
  occupancy, or a threshold crossing. State why it helps comprehension.
- **Visual hierarchy:** what the reader notices first, grouping and reading order.
- **Style constraints:** typography, palette, density and aspect ratio. Separate
  explicit requests from incidental styling in the screenshot.
- **Allowed differences:** source numbers, translations, established series
  colors, accessibility or factual corrections that must not be copied blindly.
- **Observable failures:** the few specific outcomes that would miss the request,
  such as an absent return arc, a floating connector, or flattening a time relation.

Do not treat every pixel as mandatory. Do not silently discard the distinguishing
geometry either. If a reference conflicts with factual accuracy or an explicit
project constraint, identify the conflict and propose the narrowest adjustment.
Do not import sample numbers or semantic claims merely to resemble the picture.

## 2. Representative proof

For a new or disputed visual approach, choose the smallest figure that exercises
the important feature. Draw it, render it, open it at its actual reading width,
and compare the result with the Reference contract **before** duplicating the
design across a series.

Questions to answer from the image, not the source code:

1. Is the requested relation actually visible and immediately recognizable?
2. Is the curve/shape doing explanatory work, rather than merely existing?
3. Are source, trunk, branches, arrow tips and target visibly continuous?
4. Is the intended distinction clear without a paragraph explaining the layout?
5. Is the result legible in the destination, not just at enlarged canvas size?

A function called `bezier_arrow`, an SVG containing `C`, or a passing validator
is not Representative proof. A screenshot with the requested curve visibly
rendered is evidence of that feature; it still does not prove semantic correctness.

If the user already authorized execution, continue after self-review; do not
force an extra approval round. If style/content approval is still required,
present this representative result rather than an unrendered promise.

## 3. Visual-feedback fast path

When the user points to a visual problem:

1. Acknowledge the specific visible defect and identify the artifact/version.
2. Translate it into a narrow, observable correction.
3. Change one representative figure and render the correction.
4. Show the fresh result; then apply the validated approach where appropriate.
5. Only afterward generalize helpers, guidelines and regression checks if useful.

Do not spend the turn primarily defending capability, enumerating passing tests,
redesigning the framework or expanding documentation while the visible defect
remains. Build infrastructure first only if a demonstrated blocker prevents the
representative repair; explain that blocker plainly.

## 4. Resolve “we are seeing different images”

If the user's screenshot differs from the intended output:

- Compare its title/layout with the on-disk asset and the live served asset.
- Inspect the actual article's image URL and loaded result; source file checks
  alone do not show what the reader received.
- Do not assert a cache cause without evidence. Check page/asset versions first.
- If necessary, use a new descriptive asset filename and update the real article.
- Reopen the article, verify the new resource loaded, and capture it there.
- Mark host verification unverified if the reader's environment is inaccessible.

## 5. Delivery evidence

Deliver the repaired visual, not just a statement that it was repaired:

- Prefer an actual-host screenshot for article revisions; if only a standalone
  render was possible, label that limitation explicitly.
- State which visible criteria changed, and provide the exact current page/asset.
- Report technical checks separately and briefly.
- Do not claim reference matching or user acceptance based on file existence,
  path commands, test results or self-declared completion.
- Do not add mandatory charts, curves, approval rounds, quizzes or reports to
  unrelated tasks. Carry the reasoning method forward, not this incident's layout.
