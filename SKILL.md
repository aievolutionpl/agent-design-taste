---
name: agent-design-taste
description: Use when generating any UI, landing page, dashboard, or app interface. Teaches the agent to analyze product and audience first, choose the right design style, then build with real design constraints — instead of generic "modern premium AI UI".
version: 1.0.0
license: MIT
---

# Agent Design Taste — Design Intelligence Layer

This skill makes an agent design like a designer, not like a preset-machine.
It is a **workflow**, not a style catalog. Never skip steps.

## ⛔ Mandatory workflow (in order)

```
1. UNDERSTAND        — analyze product, audience, brand personality
2. CHOOSE STYLE      — via DECISION-MATRIX.md (1 dominant + max 1 supporting)
3. CHOOSE TYPOGRAPHY — from the style's Design DNA (with reasoning, see below)
4. CHOOSE LAYOUT     — from LAYOUT-PATTERNS.md (not the same hero every time)
5. DEFINE TOKENS     — copy styles/<style>/tokens.css + write DESIGN.md contract
6. BUILD             — apply ANTI-SLOP.md rules during generation
7. VISUAL AUDIT      — score 0-100 with evaluation/DESIGN-TASTE-SCORE.md; redo if < 75
8. RESPONSIVE AUDIT  — check 1440 / 768 / **390px first**; render, don't inspect
9. REMOVE AI SLOP    — run the anti-slop checklist line by line
10. FINAL POLISH     — spacing rhythm, contrast, motion fallbacks
```

**Before step 1:** resolve the MODE from the user's verb (design / build /
review / copy / polish) — load only that slice, see `evaluation/MODE-ROUTING.md`.

**Typography reasoning (step 3):** never pick a font "because the style says
so". State WHY in one line: "Fraunces because the audience (anxious freelancers)
needs warmth/trust; a grotesk would read cold." If you can't articulate why a
family fits the audience's emotion, you haven't chosen it — the default has.

**Rendered verification (steps 7-8):** a design fault is visible in a
screenshot in one second and invisible in code review for an hour. Load the
real page in a browser before claiming done — see
`evaluation/RENDERED-VERIFICATION.md`. Never claim visual verification from
code alone.

**After step 10:** record the decision in the taste loop
(`evaluation/TASTE-LOOP.md`) — what was chosen, what was rejected, and the
reusable principle. This is how the skill compounds value over time.

Outputting a design without steps 1, 2, 7 and 9 is a **failure**, even if the
design looks good.

---

## Step 1 — Understand (before any pixel)

Answer these explicitly (write them down in your response):

- **Audience:** who uses this? (developers ≠ doctors ≠ teenagers)
- **Product type:** SaaS / fintech / AI / ecommerce / luxury / portfolio / agency / dev tool / education / startup / media
- **Brand personality:** 2-4 adjectives (e.g. technical, fast, precise OR warm, human, friendly)
- **Content density:** low / medium / high (how much information per screen?)
- **Primary action:** what should the user do first? (sign up / buy / read / explore)
- **Emotion to evoke:** trust, excitement, calm, curiosity, status...

Example — "AI coding platform for developers":
```
Audience: developers
Brand personality: technical / fast / precise
Content density: medium-high
Primary action: start free trial
Emotion: competence + speed
```

## Step 2 — Choose style

Open **DECISION-MATRIX.md**. Match product type + personality + density to a
style. Rule: **1 dominant style + maximum 1 supporting style** (see
STYLE-COMBINATIONS.md for safe pairings).

Load the chosen style's full Design DNA:
`styles/<style-name>/README.md` + `tokens.css`.

## Step 3 — Typography

Take fonts, H1-H6 scale, body metrics, letter-spacing and uppercase rules
directly from the style's README. Never default to Inter "because it's safe"
unless the style calls for it.

## Step 4 — Layout

Pick a frame pattern from **LAYOUT-PATTERNS.md** (40+ patterns). Do NOT
repeatedly generate the same centered-hero-then-3-cards layout. Vary:
split hero, editorial hero, dashboard hero, bento grid, sticky storytelling...

## Step 5 — Tokens

Copy `styles/<style>/tokens.css` (or tokens.json / tokens.tailwind.css) into
the project. All colors, spacing, radius, shadows, motion come from tokens —
no ad-hoc values.

## Step 6 — Build

Generate the UI. Constraint-first: tokens, grid, type scale, component specs
from the style DNA.

## Step 7 — Visual audit

Score with **evaluation/DESIGN-TASTE-SCORE.md** (10 criteria, 0-100).
Below 75 → identify the two weakest criteria, fix, re-score.

## Step 8 — Responsive audit

Verify 1440px, 768px, 375px. No horizontal scroll, no collapsed type hierarchy,
touch targets ≥ 44px on mobile.

## Step 9 — Remove AI slop

Run **ANTI-SLOP.md** checklist. Any hit → fix before delivering.

## Step 10 — Final polish

Spacing rhythm consistent (single spacing scale), all text ≥ 4.5:1 contrast,
prefers-reduced-motion handled, favicon/meta present.

---

## File map

| File | Purpose |
|---|---|
| `SKILL.md` | this workflow |
| `DECISION-MATRIX.md` | product/audience → style decision engine |
| `LAYOUT-PATTERNS.md` | 40+ composition patterns |
| `STYLE-COMBINATIONS.md` | safe style pairings |
| `ANTI-SLOP.md` | universal anti-AI-slop rules |
| `evaluation/DESIGN-TASTE-SCORE.md` | 0-100 scoring system |
| `styles/<style>/README.md` | full Design DNA per style |
| `styles/<style>/tokens.css` | design tokens (CSS variables) |
| `styles/<style>/tokens.json` | tokens as JSON |
| `styles/<style>/tokens.tailwind.css` | tokens as Tailwind v4 @theme |
| `styles/<style>/prompts.md` | ready prompts for Codex/Claude/Lovable/v0 |
| `styles/<style>/example.html` | working single-file example |
| `typography/`, `layout-patterns/`, `visual-language/`, `motion/`, `design-tokens/` | design foundations |

## Hard rules

1. Never start generating before Step 1 is answered.
2. Never use more than 1 dominant + 1 supporting style.
3. Never invent colors/fonts outside the chosen tokens.
4. Never deliver without scoring ≥ 75 and clearing the anti-slop checklist.
5. If the product genuinely fits no style, choose Minimalism (the neutral
   default) and say why.
