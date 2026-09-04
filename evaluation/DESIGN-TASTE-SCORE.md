# Design Taste Score v2 — weighted 0–100 audit

Score the design **after rendering it**, before delivering it. Be honest;
inflate nothing. A score you argued yourself into is worthless.

---

## Step 0 — Hard blockers (checked first, they override the score)

If any of these is true, the design **fails** — a 94 with a blocker is still a
fail. There is no partial credit here.

| # | Blocker | Test |
|---|---|---|
| B1 | Body text below 4.5:1 contrast | Sample the three most common text/background pairs |
| B2 | Horizontal overflow at 390px | Render at 390 and scroll sideways. Any movement = fail |
| B3 | Fake statistics, testimonials, or logos presented as real | Every number and name traces to something real |
| B4 | Missing or invisible `:focus-visible` on any interactive element | Tab through the whole page |
| B5 | Unreadable typography | Body < 15px, measure > 90ch, or line-height < 1.4 on paragraphs |
| B6 | Inconsistent design tokens | The same semantic role rendered with different values |
| B7 | Animation without `prefers-reduced-motion` handling | Emulate reduce; page must stay usable |
| B8 | Touch target below 44×44px on a mobile control | Measure the smallest tappable element |

These eight are `ANTI-SLOP.md`'s 🔴 BLOCKER list, consolidated — that file
lists twelve because it separates the fabrication cases (invented statistics,
testimonials, logo walls, mock screenshots) that B3 groups together, and adds
two that this list covers through categories rather than gates: placeholder
copy (category 12) and information conveyed by color alone (category 6).

Same content, two jobs: that file tells you to remove them, this one refuses to
score around them. **Anything red there fails here.**

---

## Step 1 — Score 13 categories

Each category scores **0–5**. Multiply by its weight, divide by 5, sum.

| # | Category | Weight | 5 = | 0–1 = |
|---|---|---|---|---|
| 1 | **Hierarchy** | 10 | One dominant element per screen; the scan path is obvious in 2 seconds | Everything the same weight; the eye wanders |
| 2 | **Typography** | 9 | 2–3 families with assigned roles, real scale, ≥3 type roles visible, justified choice | One family, one size, default weight |
| 3 | **Spacing & rhythm** | 7 | One scale end to end; section spacing varies with meaning | Random gaps; uniform padding regardless of content |
| 4 | **Composition** | 8 | A named layout pattern, deliberately chosen; sections differ in rhythm | Centered hero → 3 cards → CTA → footer |
| 5 | **Consistency** | 7 | Same component = same look everywhere; one radius logic | Three button styles; four radii; two greys for one role |
| 6 | **Accessibility & contrast** | 12 | AA everywhere, visible focus, semantic HTML, keyboard-complete, color never alone | Passes nothing; a11y was not considered |
| 7 | **Component quality** | 7 | Every interactive component has default/hover/focus/active/disabled + empty, loading, error where relevant | Default state only; states invented at runtime |
| 8 | **Visual direction** | 6 | One photography treatment, one icon family, one illustration system, purposeful | Mixed icon fills, stock photos, decorative 3D blobs |
| 9 | **Brand fit** | 8 | The style serves *this* audience, and you can say why the runner-up loses | Style fights the content; chosen on vibes |
| 10 | **Originality** | 7 | At least one choice only this product could have made | Could belong to any startup founded this year |
| 11 | **Responsive quality** | 10 | 1440/768/390 each *composed*, not squeezed; nav, crop and hierarchy transform | Desktop layout stacked vertically |
| 12 | **Content honesty** | 5 | Every claim, number and name is real or clearly marked as sample | Invented proof, filler copy, generic promises |
| 13 | **Interaction quality** | 4 | Motion within budget, feedback under 250ms, no jank, states legible | 900ms hovers, infinite float, no feedback at all |
| | **Total** | **100** | | |

### Worked calculation

```
hierarchy       4/5 × 10 =  8.0
typography      3/5 ×  9 =  5.4
spacing         4/5 ×  7 =  5.6
composition     3/5 ×  8 =  4.8
consistency     5/5 ×  7 =  7.0
accessibility   4/5 × 12 =  9.6
components      3/5 ×  7 =  4.2
visual          2/5 ×  6 =  2.4
brand fit       4/5 ×  8 =  6.4
originality     2/5 ×  7 =  2.8
responsive      4/5 × 10 =  8.0
honesty         5/5 ×  5 =  5.0
interaction     4/5 ×  4 =  3.2
                          ------
                    TOTAL  72.4
```

---

## Step 2 — Thresholds

| Score | Verdict |
|---|---|
| **85–100** | Ship it. |
| **75–84** | Ship after fixing the two lowest-weighted-loss categories. |
| **60–74** | Redesign the two weakest categories and re-score. Do not ship. |
| **< 60** | The concept is wrong, not the pixels. Return to `SKILL.md` step 1. |

"Weighted loss" is `(5 − score) × weight ÷ 5`. Fix by weighted loss, not by raw
score — a 3/5 on accessibility (loss 4.8) costs more than a 2/5 on interaction
quality (loss 2.4).

---

## Step 3 — Output format

Print this. It is the audit trail.

```
DESIGN TASTE SCORE v2

BLOCKERS  none

hierarchy 4 · typography 3 · spacing 4 · composition 3 · consistency 5
a11y 4 · components 3 · visual 2 · brand-fit 4 · originality 2
responsive 4 · honesty 5 · interaction 4

TOTAL 72.4 / 100  →  redesign required

Largest weighted losses
  visual direction   3.6   mixed icon families + one stock photo
  originality        4.2   nothing here is specific to this product
  composition        4.0   centered hero, the default pattern

Fixes applied
  → single icon family (Lucide outline, 1.5px), stock photo replaced with
    a real product screenshot in a browser frame
  → hero switched to Product Screenshot Hero; the terminal is the identity
  → re-render, re-score

RE-SCORE  81.6 / 100  →  ship after fixing spacing rhythm in the pricing block
```

---

## Score inflation warning

Past roughly 85, iterating on the number optimizes the metric rather than the
page. Use the score to **find** faults, not to certify quality.

**The decision to ship is made after looking at the screenshot**, never after
reading a total. If the score says 88 and the render looks wrong, the render is
right.
