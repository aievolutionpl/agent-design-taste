# Prompt Library (cross-style)

Universal prompt patterns. Style-specific prompts live in
`styles/<style>/prompts.md`.

## Structure of a good UI prompt (constraint-first)

```
[ROLE] You are a senior product designer + front-end engineer.
[PRODUCT] What it is, for whom, primary action.
[STYLE] Dominant style + supporting style + WHY (audience fit).
[TYPOGRAPHY] Exact fonts + scale.
[COLOR] Exact palette with hex + contrast requirement.
[LAYOUT] Named pattern from LAYOUT-PATTERNS.md.
[TOKENS] Use this tokens.css (paste).
[ANTI-SLOP] Specific things NOT to do.
[DELIVERABLE] Single-file HTML / component / tokens JSON.
[AUDIT] Before answering, score with DESIGN-TASTE-SCORE.md; fix below 75.
```

## Universal anti-slop prompt block (paste into any UI prompt)

```
Do NOT:
- use purple-blue gradient blobs, glassmorphism on more than 2 elements,
  uniform 24px radius on all cards, or 3 identical feature cards in a row
- use fake statistics (99.9%, 10x), fake testimonials, or lorem ipsum
- center everything; vary layout rhythm; left-align body text
- mix icon families; use neon purple as default accent
- animate without prefers-reduced-motion fallback
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
Score this design 0-100 on: hierarchy, typography, spacing, consistency,
contrast, visual quality, usability, originality, brand fit, responsiveness.
Run the anti-slop checklist. List every hit with a concrete fix, apply the
fixes, and output the improved version with the final score.
```

## Tool notes

- **Codex/Claude**: full prompt works; paste tokens.css for best fidelity.
- **Lovable**: lead with STYLE + TYPOGRAPHY + COLOR; keep anti-slop block;
  iterate per section rather than whole page at once.
- **v0**: it defaults to shadcn/Tailwind — paste `tokens.tailwind.css` into
  the prompt and explicitly override radius/shadow defaults.