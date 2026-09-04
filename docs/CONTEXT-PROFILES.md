# Context Profiles — load the smallest thing that works

This repository is roughly **100,000 tokens** of design knowledge. Loading it all
for "make this button nicer" is not thoroughness, it is waste — and a context
window full of styles you rejected makes the output *worse*, not better.

**The agent never loads all 15 styles.** Route first, load second.

---

## Pick a profile

| Signal | Profile |
|---|---|
| One component, one section, a copy fix, a spacing pass | **LIGHT** |
| A page: landing, pricing, marketing site, a feature area | **STANDARD** |
| A whole product or site: new identity, full redesign, design system | **FULL** |

When in doubt, start LIGHT and escalate. Escalating costs one extra file read.
Starting FULL costs the whole budget and cannot be undone.

---

## LIGHT — ~3k tokens

*Small, local improvements inside an interface that already exists.*

```
ANTI-SLOP.md                       (the severity table only)
docs/PRECEDENCE.md                 (if the project has its own design system)
the project's own tokens/config    (theirs, not ours)
component-patterns/COMPONENT-PATTERNS.md   (only the component you are touching)
```

Do **not** choose a style in LIGHT mode. The project already has one — your job
is to stop violating it, not to introduce a new one.

**Exit gate:** no anti-slop BLOCKER, no new token invented, contrast holds.

---

## STANDARD — ~8k tokens

*A page or a coherent feature area. This is the default profile.*

```
SKILL.md                           the workflow + hard rules
DECISION-MATRIX.md                 choose the style, with reasons
styles/<chosen>/README.md          exactly one style DNA
styles/<chosen>/tokens.css         its tokens
ANTI-SLOP.md                       the quality gate
LAYOUT-PATTERNS.md                 §Hero + §Feature only, not all 43
```

**Exit gate:** rendered at 1440/768/390, Design Taste Score ≥ 75, anti-slop clear.

---

## FULL — ~25k tokens

*A complete product, a new visual identity, or a design system build.*

```
Everything in STANDARD, plus:
STYLE-COMBINATIONS.md              if a supporting style is in play
styles/<supporting>/README.md      the supporting style DNA (max one)
LAYOUT-PATTERNS.md                 all of it — you are composing many pages
typography/TYPOGRAPHY-FOUNDATIONS.md
visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md
motion/MOTION-FOUNDATIONS.md
component-patterns/COMPONENT-PATTERNS.md
responsive/RESPONSIVE-FOUNDATIONS.md
accessibility/ACCESSIBILITY.md
design-tokens/TOKENS-GUIDE.md
evaluation/DESIGN-TASTE-SCORE.md
prompts/DESIGN-CONTRACT.md         write DESIGN.md before any UI
```

**Exit gate:** every STANDARD gate, plus a written `DESIGN.md` contract and a
per-surface render pass.

---

## Approximate cost of every file

Measured at roughly 4 characters per token. Use it to budget deliberately.

| File | ~tokens | Load when |
|---|---|---|
| `AGENT-BOOTSTRAP.md` | 0.8k | always, first |
| `SKILL.md` | 2.8k | STANDARD and up |
| `DECISION-MATRIX.md` | 2.9k | a style is not yet chosen |
| `ANTI-SLOP.md` | 1.7k | always, before delivery |
| `LAYOUT-PATTERNS.md` | 4.9k | composing a page (sections are separable) |
| `styles/<one>/README.md` | ~2.7k | the chosen style, one only |
| `styles/<one>/tokens.css` | ~0.6k | the chosen style, one only |
| `styles/<one>/example.html` | ~2.3k | rarely — reference output, not input |
| `styles/<one>/prompts.md` | ~0.9k | only when prompting another tool |
| foundations (each) | 0.6–2.7k | FULL, or when the task is about that layer |
| `evaluation/DESIGN-TASTE-SCORE.md` | 1.4k | before delivery in STANDARD and up |
| **all 15 style READMEs** | **~41k** | **never** |

Regenerate these numbers any time: `python3 scripts/validate.py --budget`.

---

## Escalation rules

1. **Escalate on evidence, not on nerves.** Move LIGHT → STANDARD when the task
   turns out to need a style decision, not because the page felt important.
2. **One style at a time.** If a second style DNA enters context, you are either
   in FULL with a declared supporting style, or you have made a mistake.
3. **Discard after deciding.** Once the style is chosen, the decision matrix has
   done its job — do not keep re-reading it while building.
4. **Never re-read a file you already summarized** into `DESIGN.md`. The contract
   is the compressed form; that is what it is for.

---

## Why this matters more than adding knowledge

A style DNA in this library already specifies fonts, type scale, layout, color
system, components, motion, accessibility and per-style anti-slop rules. One
style is a complete design brief. Fifteen styles is noise with a brief buried
in it.

**Routing knowledge beats accumulating knowledge.** That is the product.
