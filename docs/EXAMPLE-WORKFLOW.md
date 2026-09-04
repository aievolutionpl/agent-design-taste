# Example workflow — the system running end to end

One request, followed all the way through. This is what "the process is the
product" means in practice: the same brief, given to an agent with and without
this repository, produces two different *kinds* of answer — not two colour
schemes.

---

## The request

> **User:** "Build a landing page for an AI coding platform."

An agent without a design system starts writing JSX here. An agent with one
does not.

---

## Step 0 — Route

```
PROFILE   STANDARD — one page, style not yet chosen         (docs/CONTEXT-PROFILES.md)
MODE      Implement — the verb is "build"                   (evaluation/MODE-ROUTING.md)
LOAD      SKILL.md · DECISION-MATRIX.md · ANTI-SLOP.md
          + one style DNA once chosen. Not all 15.
```

---

## Step 1 — Understand

```
Audience              developers evaluating a tool in under 90 seconds
Product type          dev tool / AI platform
Brand personality     technical · fast · precise
Content density       medium-high (S1) · dense-relational (S7)
Primary action        start free trial
Emotion to evoke      competence + speed
Trust requirement     medium        Accessibility sensitivity   standard
Device context        desktop-first (developers evaluate on a laptop)
Session duration      glance → task  Existing brand system      none (greenfield)
```

Note what is *not* here: no adjective like "modern" or "premium". Those are
not design inputs, they are decoration on a brief.

---

## Step 2 — Choose style

**Veto gates** — none triggered. Trust is medium, accessibility standard,
audience is not child/family, device is desktop-first.

**Scores** (`DECISION-MATRIX.md` Part 3):

| Style | Modifiers met | Total |
|---|---|---|
| **Swiss / International (10)** | +3 density:high · +3 personality:precise · +3 complexity:dense-relational · +2 audience:technical · +2 emotion:competence | **13** |
| Bento Grid (04) | +3 density:high · +2 personality:precise | 5 |
| Glassmorphism (02) | +2 audience:technical · +2 desktop-first · −3 density:high | 1 |
| Minimalism (01) | +1 density:medium | 1 |
| Claymorphism (08) | −3 audience:technical · −3 density:high | −6 |

**Dominant:** Swiss / International (10)
**Supporting:** Neo-Brutalism (05) — owning display type weight only

**Why not Bento.** Modular tiles imply feature parity. This product has one
headline capability and a long tail; a numbered list expresses that hierarchy,
a grid of equal tiles flattens it.

**Why not Claymorphism.** Friendly softness contradicts an audience that buys
on precision. Clay says "we will look after you"; this audience wants "this
will not waste your time".

**Why not Minimalism.** It is the right *temperature* but the wrong *density* —
minimalism would ask us to remove the technical detail that is the argument.

---

## Step 3 — Typography

From the Swiss DNA: neo-grotesk display + neutral text + mono for code.

```
Display   Archivo        H1–H2, 600
Text/UI   Inter          H3–body, 400/500
Mono      JetBrains Mono code blocks, labels, numeric columns
```

**Why:** grotesk + mono is the native vernacular of this audience — deviating
from it reads as unfamiliarity with the domain. A display serif here would
signal "marketing wrote this page", which is exactly the wrong signal for a
developer deciding whether the team can be trusted with their build.

---

## Step 4 — Layout

From `LAYOUT-PATTERNS.md`:

```
Hero        #4  Product Screenshot Hero    — the interface is the argument
Features    #15 Numbered Feature List      — one capability dominates, the rest support
Proof       #18 Comparison Table           — this audience actively compares
Deep dive   #24 Annotated Screenshot       — the UI needs interpretation
Close       #35 Final Split CTA
Structure   #40 Top-Bar Marketing Layout
```

Deliberately **not** used: Centered Hero (the default), three identical
feature cards, a logo wall we have no permission for, a metrics strip with no
real numbers.

---

## Step 5 — Tokens

No existing brand system, so the style tokens are the greenfield default:
`styles/10-swiss-international/tokens.css`, copied unchanged.

Then `DESIGN.md` at the project root (`prompts/DESIGN-CONTRACT.md`):

```markdown
# DESIGN.md — <product>
## Style
Dominant: Swiss / International (10) + Supporting: Neo-Brutalism (05), display type only.
Why: developers buy on precision; the grid IS the credibility signal.
## Constraints
- Radius 0 everywhere. Borders, never shadows.
- One accent, used once per screen, on the primary action.
- Type: Archivo / Inter / JetBrains Mono. H1 clamp(2.5rem, 1.6rem + 4vw, 4.5rem)/600.
- Spacing scale: 4 8 12 16 24 32 48 64 96
## Anti-references
- Not like generic AI SaaS: purple gradient, glass cards, 24px radius on everything
- Not like a design-agency site: no oversized serif, no full-bleed photography
```

---

## Step 6 — Build

Constraint-first. Every value from a token. Real copy, not filler. The hero
screenshot is a real screenshot — and if one does not exist yet, the honest
options are a terminal recording, a diagram, or typography. Not a mockup with
invented metrics.

---

## Step 7 — Render

```
1440 × 900   composition holds; the numbered list carries the page
768 × 1024   12→8 columns; comparison table gets a sticky first column
390 × 844    ✗ the comparison table overflows horizontally  ← 🔴 BLOCKER
360          ✗ same
```

Found by looking, in one second. Invisible in the CSS for an hour.

**Fix:** at 390 the comparison table becomes one card per competitor. Re-render.
Clean.

---

## Step 8 — Audit

```
hierarchy 4 · typography 4 · spacing 4 · composition 4 · consistency 5
a11y 4 · components 3 · visual 3 · brand-fit 5 · originality 3
responsive 4 · honesty 5 · interaction 4          TOTAL 80.4 / 100

Largest weighted losses
  components   5.6   pricing cards have no loading or error state
  originality  5.6   nothing here is specific to THIS product yet
  visual       2.4   two icon weights in the feature list
```

---

## Step 9 — Remove slop

```
BLOCKERS   0
STRONG     1 — every section is 96px apart; no rhythm
MINOR      1 — icon-only GitHub link missing aria-label
FIXED      section spacing now 64 / 96 / 128 by weight · aria-label added
```

---

## Step 10 — Polish, then deliver

Originality was the largest remaining loss, so it gets the fix: the hero shows
a **real terminal session** running the product against a real repository —
something only this product could show. That is the element that stops the page
being a template.

```
RE-SCORE 86.2 / 100 → ship
```

---

## Files this run actually loaded

```
AGENT-BOOTSTRAP.md                            0.8k tokens
SKILL.md                                      2.8k
DECISION-MATRIX.md                            2.9k
styles/10-swiss-international/README.md       2.7k
styles/10-swiss-international/tokens.css      0.5k
LAYOUT-PATTERNS.md  (§ Hero + § Feature)      3.0k
ANTI-SLOP.md                                  1.7k
evaluation/DESIGN-TASTE-SCORE.md              1.4k
                                             ─────
                                             ~15k tokens
```

Loading all 15 style folders would have cost **~41k tokens** on its own, and
would have made the answer worse — fourteen rejected styles sitting in context
while the model tries to be consistent with one.

**That is the whole argument for routing knowledge instead of dumping it.**
