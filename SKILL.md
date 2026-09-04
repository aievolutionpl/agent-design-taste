---
name: agent-design-taste
description: Use when generating, redesigning or reviewing any UI — landing page, dashboard, app screen, component, or design system. Teaches the agent to analyze product and audience first, choose one design style deliberately, build from real tokens, render it, and audit it — instead of producing generic "modern premium AI SaaS" output.
license: MIT
version: 2.0.0
metadata:
  repository: https://github.com/aievolutionpl/agent-design-taste
  styles: 15
  entrypoint: AGENT-BOOTSTRAP.md
  manifest: design-taste.manifest.json
---

# Agent Design Taste — Design Intelligence Layer

This skill makes an agent design like a designer, not like a preset machine.
It is a **process**, not a style catalog. The process is the product.

```
UNDERSTAND → CHOOSE STYLE → TYPOGRAPHY → LAYOUT → TOKENS
    → BUILD → RENDER → AUDIT → REMOVE SLOP → POLISH
```

---

## Before step 1: route

Two decisions come before any design thinking.

**Profile** — how much of this repository to load.
LIGHT (a component) · STANDARD (a page) · FULL (a product).
→ `docs/CONTEXT-PROFILES.md`. **Never load all 15 styles.**

**Mode** — what the user actually asked for, taken from their verb.
Shape · Implement · Review · Copy · Harden.
→ `evaluation/MODE-ROUTING.md`. Do not audit when asked to implement.

---

## ⛔ The workflow

```
1.  UNDERSTAND        product, audience, brand personality, density, action, emotion
2.  CHOOSE STYLE      DECISION-MATRIX.md — 1 dominant + max 1 supporting, with scores
3.  CHOOSE TYPOGRAPHY from the style DNA, and say WHY in one sentence
4.  CHOOSE LAYOUT     LAYOUT-PATTERNS.md — not the same hero every time
5.  DEFINE TOKENS     resolve against docs/PRECEDENCE.md, write DESIGN.md
6.  BUILD             constraint-first: tokens, grid, type scale, component specs
7.  RENDER            real browser: 1440 → 768 → 390. Screenshot, don't assume
8.  AUDIT             evaluation/DESIGN-TASTE-SCORE.md — below 75, fix and re-score
9.  REMOVE AI SLOP    ANTI-SLOP.md line by line — every BLOCKER must be zero
10. POLISH            spacing rhythm, focus states, reduced-motion, meta
```

Delivering a design without steps 1, 2, 7 and 9 is a **failure**, even when the
result looks good. Looking good is not the same as being designed.

---

## Step 1 — Understand

Write these down in your response before touching any pixel:

- **Audience** — who uses this? (developers ≠ doctors ≠ teenagers ≠ CFOs)
- **Product type** — SaaS / fintech / AI / ecommerce / luxury / portfolio /
  agency / dev tool / education / media / local business
- **Brand personality** — 2–4 adjectives (technical, fast, precise · warm,
  human, forgiving)
- **Content density** — low / medium / high. How much information per screen?
- **Primary action** — what should the user do first?
- **Emotion to evoke** — trust, competence, calm, excitement, status, safety

```
Audience: developers evaluating a tool in under 90 seconds
Product: AI coding platform · Personality: technical / fast / precise
Density: medium-high · Action: start free trial · Emotion: competence + speed
```

If a project already has a design system, run **ANALYZE → MAP → ADAPT** from
`docs/PRECEDENCE.md` *now*, before choosing anything.

## Step 2 — Choose style

Score candidates in `DECISION-MATRIX.md`. Output the reasoning, not just the
answer:

```
Chosen: Swiss / International (10) — score 14
Runner-up: Minimalism (01) — 11. Rejected: reads calm, the brand needs precision.
Rejected: Claymorphism (08) — −6. Friendly tone contradicts a technical audience.
Supporting: Brutalism (06), owning display type only.
```

"Why not the others" is half the deliverable. A style you cannot argue against
is a style you did not choose.

**One dominant + at most one supporting.** See `STYLE-COMBINATIONS.md` for safe
pairs and the dangerous ones. Then load exactly that style's
`README.md` + `tokens.css` — nothing else.

## Step 3 — Typography

Take families, scale, metrics and casing rules from the style DNA. Then justify
the choice in one sentence naming the *audience emotion*:

> "Fraunces, because anxious freelancers need warmth before authority — a
> grotesk here would read like the tax office they are afraid of."

If you cannot write that sentence, you did not choose the font; the default did.
→ `typography/TYPOGRAPHY-FOUNDATIONS.md`

## Step 4 — Layout

Pick a named pattern from `LAYOUT-PATTERNS.md` and name it in your output. The
#1 AI layout failure is not color — it is generating *centered hero → three
cards → CTA → footer* every single time. Rotate: split hero, editorial hero,
product screenshot hero, terminal hero, bento, sticky storytelling, numbered
feature list.

## Step 5 — Tokens

Copy `styles/<style>/tokens.css` (or `.json` / `.tailwind.css`) into the project,
**after** resolving it against the precedence chain. Then write `DESIGN.md` at
the project root — the binding visual contract that survives context loss.
→ `prompts/DESIGN-CONTRACT.md`

## Step 6 — Build

Constraint-first. Every color, space, radius, shadow and duration resolves to a
token. Component anatomy from `component-patterns/`, motion budgets from
`motion/`, imagery direction from `visual-language/`.

## Step 7 — Render

**Code review is not visual review.** Load the real page in a real browser and
look at it, at the canonical viewports below. An agent claiming "looks great"
without a rendered screenshot has verified nothing.
→ `evaluation/RENDERED-VERIFICATION.md`

## Step 8 — Audit

Score 0–100 in `evaluation/DESIGN-TASTE-SCORE.md`. Below 75, fix the two lowest
categories and re-score. Any hard blocker fails the design regardless of score.

## Step 9 — Remove AI slop

`ANTI-SLOP.md`, top to bottom. **BLOCKER** hits must be zero.
**STRONG SMELL** hits must be fixed or explicitly justified in one line.

## Step 10 — Polish

One spacing scale end to end · visible `:focus-visible` on every interactive
element · `prefers-reduced-motion` honored · title, description and favicon
present · empty, loading and error states exist.

**After delivery:** record the decision in `evaluation/TASTE-LOOP.md` — what won,
what lost, and the reusable principle. That is how the skill compounds.

---

## Canonical viewports

One ladder. Do not invent others; do not skip mobile.

| Width | Name | Role |
|---|---|---|
| **1440** | Desktop | Primary composition. Where the design is *authored*. |
| **768** | Tablet | Adaptation. Where two-column layouts have to decide. |
| **390** | **Mobile — canonical** | **The primary verification viewport.** Check it *first*. |
| 360 | Narrow floor | Regression only: horizontal overflow, text clipping. |

390 × 844 is the canonical mobile check (the modern iPhone/Android class width).
360 is the narrow floor: if the layout holds at 360 it holds at every width
above it. Earlier versions of this repository said 375px in some places and 390
in others — 390 is now the single canonical number.

**Responsive is recomposition, not stacking.** → `responsive/RESPONSIVE-FOUNDATIONS.md`

---

## Precedence — what wins when sources disagree

```
P1 Brand & legal  ▸  P2 Accessibility floor  ▸  P3 Product needs
   ▸  P4 Style DNA  ▸  P5 Repository tokens  ▸  P6 Agent preference
```

Style tokens are **defaults for greenfield work**, never permission to repaint
an existing brand. When a brand color fails contrast, you keep the brand and
derive an accessible variant inside the same hue family — you do not swap the
brand out, and you do not ship failing text.

Full rules, including ANALYZE → MAP → ADAPT: **`docs/PRECEDENCE.md`**.

---

## Knowledge priority — what wins when *files* disagree

```
1. The project's existing brand / design system
2. Explicit user requirements in this conversation
3. accessibility/ACCESSIBILITY.md          (the floor, never negotiable downward)
4. docs/PRECEDENCE.md                      (the tie-breaker itself)
5. SKILL.md                                (this workflow)
6. styles/<chosen>/tokens.css              (canonical values for that style)
7. styles/<chosen>/README.md               (the style's prose)
8. Cross-style foundations (typography/, layout-patterns/, motion/, …)
9. styles/<chosen>/example.html            (illustration, never authority)
```

Two consequences worth stating plainly:

- **Tokens beat prose.** If a style README says 12px radius and its `tokens.css`
  says 8px, the token wins — and the README is a bug to report.
- **Examples beat nothing.** `example.html` shows one valid interpretation. It is
  never a spec, and copying it wholesale is how every page ends up identical.

---

## Hard rules

1. Never generate UI before step 1 is answered in writing.
2. Never load more than one dominant style DNA into context.
3. Never use more than 1 dominant + 1 supporting style.
4. **Every value resolves to a token.** Tokens come from the precedence chain —
   brand first, style DNA as the greenfield default. A value that exists in
   neither is a bug: either it becomes a token, or it does not ship.
5. Never claim visual verification without a rendered screenshot.
6. Never deliver with an anti-slop BLOCKER or a Design Taste Score below 75.
7. Never invent policy from silence — a gap in the existing system is flagged,
   not filled by pattern-matching.
8. If the product genuinely fits no style, use Minimalism (the neutral default)
   and say why.

---

## File map

| File | Purpose | Load in |
|---|---|---|
| `AGENT-BOOTSTRAP.md` | 10-step entry point | always |
| `SKILL.md` | this workflow | STANDARD+ |
| `docs/PRECEDENCE.md` | conflict resolution, brand adaptation | always when a system exists |
| `docs/CONTEXT-PROFILES.md` | what to load, what not to | always |
| `DECISION-MATRIX.md` | weighted product → style scoring | when style unchosen |
| `STYLE-COMBINATIONS.md` | safe and dangerous pairings | when pairing |
| `LAYOUT-PATTERNS.md` | 43 composition patterns as a decision library | page work |
| `ANTI-SLOP.md` | BLOCKER / STRONG / MINOR quality gate | always |
| `accessibility/ACCESSIBILITY.md` | the a11y floor and its gates | always |
| `responsive/RESPONSIVE-FOUNDATIONS.md` | recomposition across the viewport ladder | page work |
| `typography/`, `visual-language/`, `motion/`, `component-patterns/`, `layout-patterns/`, `design-tokens/` | cross-style foundations | FULL |
| `evaluation/DESIGN-TASTE-SCORE.md` | weighted 0–100 audit + hard blockers | before delivery |
| `evaluation/RENDERED-VERIFICATION.md` | render-before-claiming protocol | before delivery |
| `evaluation/MODE-ROUTING.md` | verb → mode → slice | always |
| `evaluation/TASTE-LOOP.md` | preference learning across sessions | multi-session projects |
| `prompts/DESIGN-CONTRACT.md` | the DESIGN.md pattern | project start |
| `prompts/PROMPT-LIBRARY.md` | prompt scaffolds for other tools | when prompting a tool |
| `styles/<style>/README.md` | full Design DNA (24 sections) | the chosen style only |
| `styles/<style>/tokens.{css,json,tailwind.css}` | canonical values | the chosen style only |
| `styles/<style>/prompts.md` | ready prompts for Codex / Claude / Lovable / v0 | when prompting a tool |
| `styles/<style>/example.html` | one working interpretation | reference only |
| `design-taste.manifest.json`, `styles/index.json` | machine-readable routing | tooling |
