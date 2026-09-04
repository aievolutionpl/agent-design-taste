# Design Taste Score — 0-100 self-audit

Score your design BEFORE delivering. Below 75 → fix the two weakest criteria
and re-score. Be honest; inflate nothing.

## Criteria (10 × 10 points)

| # | Criterion | Question | 9-10 looks like | 0-4 looks like |
|---|---|---|---|---|
| 1 | **Hierarchy** | Is there an obvious #1 thing to see? | One dominant element per screen, clear scan path | Everything same size, eye wanders |
| 2 | **Typography** | Real pairing + correct scale? | 2-3 families max, H1-H6 scale used, ≥3 type roles visible | One font, one size, default weight |
| 3 | **Spacing** | One consistent rhythm? | Single spacing scale, generous section spacing | Random gaps, cramped or scattered |
| 4 | **Consistency** | Same component = same look everywhere? | Component family unified across page | 3 different button styles |
| 5 | **Contrast & a11y** | Text ≥4.5:1, focus visible, touch ≥44px? | Passes WCAG AA basics | Gray-on-gray, invisible focus |
| 6 | **Visual quality** | Imagery/icons/3D coherent and purposeful? | One visual language, quality assets | Mixed icon families, stock-ish images |
| 7 | **Usability** | Can a first-time user find primary action in 3s? | Primary CTA unmissable, nav obvious | Hunting for the CTA |
| 8 | **Originality** | Does this look like THIS brand, not generic AI? | Recognizable identity, at least one distinctive choice | Could belong to any startup |
| 9 | **Brand fit** | Style matches product/audience (per DECISION-MATRIX)? | Style serves the audience | Style fights the content |
| 10 | **Responsiveness** | 1440/768/375 all correct? | All breakpoints designed, not just squeezed | Mobile horizontal scroll, broken hero |

## Penalties (subtract from total)

- Any ANTI-SLOP.md hit on fake stats/testimonials/lorem ipsum: **-15 each**
- Any other anti-slop hit: **-5 each**
- Missing `prefers-reduced-motion` handling with animated page: **-5**
- Horizontal scroll on mobile: **-10**

## Pass thresholds

- **85-100** — ship it.
- **75-84** — ship after fixing flagged items.
- **60-74** — redesign the two weakest criteria, re-score.
- **< 60** — return to SKILL.md step 1. The concept, not the pixels, is wrong.

## Audit output format (agent should print this)

```
DESIGN TASTE AUDIT
hierarchy 8 | typography 7 | spacing 8 | consistency 9 | contrast 8
visual 6 | usability 9 | originality 5 | brand-fit 8 | responsive 9
TOTAL: 77/100 → ship after fixing: originality (add one distinctive brand
element), visual (replace mismatched icons with one family)
```