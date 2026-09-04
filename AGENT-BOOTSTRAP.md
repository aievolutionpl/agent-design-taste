# AGENT BOOTSTRAP

> The shortest possible entry point. If you are an AI agent and you read only
> one file in this repository, read this one, then read `SKILL.md`.

**You are about to build or change a user interface. Do not write UI code yet.**

---

## The 10 steps

```
1.  READ        SKILL.md (the full workflow + hard rules)
2.  MODE        pick LIGHT / STANDARD / FULL   → docs/CONTEXT-PROFILES.md
3.  UNDERSTAND  product · audience · personality · density · action · emotion
4.  CHOOSE      1 dominant style (+ max 1 supporting) → DECISION-MATRIX.md
5.  LOAD        only styles/<chosen>/README.md + tokens.css   (never all 15)
6.  TOKENS      resolve conflicts via PRECEDENCE  → docs/PRECEDENCE.md
7.  BUILD       constraint-first: tokens, grid, type scale, component specs
8.  RENDER      real browser at 1440 / 768 / 390 → evaluation/RENDERED-VERIFICATION.md
9.  AUDIT       score + anti-slop → evaluation/DESIGN-TASTE-SCORE.md · ANTI-SLOP.md
10. FIX         repair the two weakest areas, render again, then deliver
```

Steps 3, 4, 8 and 9 are not optional. A design delivered without them is a
failure even when it looks good.

---

## What NOT to load

| Do not load | Why |
|---|---|
| All 15 style folders | ~60k tokens of context for a decision you make once |
| Every `example.html` | They are reference output, not input. Open one, at most |
| `styles/*/prompts.md` | Only when you are *writing a prompt for another tool* |
| `evaluation/TASTE-LOOP.md` | Only for multi-session projects that keep a `taste/` folder |
| `docs/INTEGRATIONS.md` | Only when installing the skill, never when designing |
| `README.pl.md` | Polish translation of the README — same content |

Loading more than one style's DNA is the single most common context mistake.
The decision matrix exists so you *don't* have to read them all.

---

## Reading order by task

| Task | Read, in order |
|---|---|
| "make this button/section better" | `ANTI-SLOP.md` → the project's own tokens |
| "build a landing page" | `SKILL.md` → `DECISION-MATRIX.md` → 1 style → `LAYOUT-PATTERNS.md` |
| "redesign the whole product" | Everything in FULL profile — see `docs/CONTEXT-PROFILES.md` |
| "review this UI" | `evaluation/DESIGN-TASTE-SCORE.md` → `ANTI-SLOP.md` → style Do/Don't |
| "the project already has a design system" | `docs/PRECEDENCE.md` first, before anything else |

---

## Three rules that override your instincts

1. **Analyze before you choose.** A style is a consequence of audience and
   content density, never of what looks good in isolation.
2. **The existing brand wins.** Style tokens are *defaults for greenfield work*,
   not permission to repaint someone's product. See `docs/PRECEDENCE.md`.
3. **Code review is not visual review.** You have not verified anything until
   you have looked at a rendered screenshot.
   `node scripts/screenshot.mjs <url-or-file>` renders all four viewports and
   fails on mobile overflow — then open the images and actually look.

---

## Machine-readable index

Routing without reading prose: `design-taste.manifest.json` (repo + skill
version, file map, context profiles) and `styles/index.json` (all 15 styles
with ids, aliases, paths, scoring weights, incompatibilities).

Next file: **[`SKILL.md`](SKILL.md)**.
