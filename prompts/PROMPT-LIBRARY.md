# Prompt Library (cross-style)

Universal prompt patterns. Style-specific prompts live in
`styles/<style>/prompts.md`.

## Structure of a good UI prompt (constraint-first)

```
[ROLE]        You are a senior product designer + front-end engineer.
[PRODUCT]     What it is, for whom, the primary action.
[BRAND]       Existing colors/fonts to preserve — or "greenfield".
[STYLE]       Dominant style + supporting style + WHY (audience fit).
[TYPOGRAPHY]  Exact families + scale + the one-sentence justification.
[COLOR]       Exact palette with hex + contrast requirement.
[LAYOUT]      Named pattern from LAYOUT-PATTERNS.md.
[TOKENS]      Use this tokens.css (paste it).
[RESPONSIVE]  Must hold at 1440 / 768 / 390. Recompose, do not stack.
[ANTI-SLOP]   Specific things NOT to do (see the block below).
[DELIVERABLE] Single-file HTML / component / tokens JSON.
[AUDIT]       Before answering, run the anti-slop checklist and score with
              DESIGN-TASTE-SCORE.md. Fix anything below 75 and every BLOCKER.
```

## Universal anti-slop prompt block (paste into any UI prompt)

```
NEVER (these are blockers, not preferences):
- invent statistics, testimonials, customer logos, or case-study results
- ship body text below 4.5:1 contrast, or remove focus rings
- allow horizontal scroll at 390px, or touch targets under 44x44px
- animate without a prefers-reduced-motion fallback
- present a mockup of a product that does not exist as a real screenshot

DO NOT (fix or justify each one):
- purple-to-blue gradient blobs, or neon violet as the default accent
- glassmorphism on more than 2 surfaces, or a uniform 24px radius on everything
- three identical feature cards in a row, or every section wrapped in a card
- a 4x3 grid of generic outline icons; mixed icon families
- center-align everything; vary the rhythm, left-align body text
- generic copy: "Built for modern teams", "Transform your workflow"
- a desktop layout merely stacked vertically for mobile
```

## Style-selection prompt (when style isn't chosen yet)

```
Before designing, determine:
1. Audience + product type + brand personality (2-4 adjectives)
2. Content density (low/medium/high)
3. Consult the decision matrix: pick 1 dominant + max 1 supporting style
4. State the brief: style, fonts, palette, layout pattern, visual direction,
   and 3 things to avoid
Then generate the UI. Print the brief first.
```

## Audit-and-fix prompt (after generation)

```
Score this design with evaluation/DESIGN-TASTE-SCORE.md:

1. Check the 8 hard blockers first. Any hit fails the design regardless of score.
2. Score all 13 categories 0-5 and compute the weighted total out of 100.
3. Run the ANTI-SLOP.md checklist and report BLOCKER / STRONG / MINOR counts.
4. List the three largest weighted losses with a concrete fix for each.
5. Apply the fixes, re-render, re-score, and output the improved version.

Do not claim visual verification without a rendered screenshot.
```

## Tool notes

- **Codex/Claude**: full prompt works; paste tokens.css for best fidelity.
- **Lovable**: lead with STYLE + TYPOGRAPHY + COLOR; keep anti-slop block;
  iterate per section rather than whole page at once.
- **v0**: it defaults to shadcn/Tailwind — paste `tokens.tailwind.css` into
  the prompt and explicitly override radius/shadow defaults.