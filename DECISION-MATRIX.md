# Product → Style Decision Engine

A style is a **consequence**, not a preference. It falls out of who uses the
product, how much information is on screen, and what the user must feel in the
first three seconds. Never choose a style because it looks cool.

```
Product type → Audience → Personality → Density → Trust → Emotion
    → veto gates → weighted score → dominant style (+ optional supporting)
```

Two paths. Take the **fast path** when the brief is unambiguous; take the
**scored path** when two styles are plausible, when a stakeholder will ask
"why," or when the brief pulls in different directions.

---

## Part 1 — The brief (answer before scoring)

Eleven signals. Answer them from `SKILL.md` step 1. Anything you cannot answer
is a question for the user, not a blank to fill with a guess.

| # | Signal | Values |
|---|---|---|
| S1 | **Content density** | low · medium · high |
| S2 | **Audience** | technical · professional · consumer · creative · child/family · mixed-public |
| S3 | **Brand personality** | precise · bold · warm · premium · playful · nostalgic · futuristic · literary |
| S4 | **Trust requirement** | low · medium · **critical** (money, health, legal, identity) |
| S5 | **Accessibility sensitivity** | standard · **elevated** (public sector, health, wide age range, regulated) |
| S6 | **Conversion priority** | browse · consider · convert-now |
| S7 | **Information complexity** | simple · layered · dense-relational (tables, graphs, hierarchies) |
| S8 | **Device context** | desktop-first · mobile-first · mixed |
| S9 | **Session duration** | glance (<1 min) · task (1–10 min) · dwell (daily use, long-form) |
| S10 | **Emotional target** | trust · competence · calm · excitement · status · safety · curiosity |
| S11 | **Existing brand system** | none (greenfield) · partial · complete |

**S11 = complete or partial short-circuits everything below.** Go to
`docs/PRECEDENCE.md` and run ANALYZE → MAP → ADAPT. You are choosing a style to
*accommodate* an existing system, not to replace it.

---

## Part 2 — Veto gates (run first, they are absolute)

A veto removes a style from consideration no matter how well it scores.
This is where most bad AI style choices die.

| Condition | Vetoed styles | Why |
|---|---|---|
| S4 = **critical** (money/health/legal) | Y2K (13) · Maximalism (12) · Neumorphism (07) · Anti-Grid (06) | Visual instability reads as institutional instability |
| S5 = **elevated** | Neumorphism (07) · Glassmorphism (02) as dominant · Maximalism (12) | Soft-shadow and translucent surfaces cannot reliably hold 3:1 non-text contrast |
| S1 = **high** or S7 = **dense-relational** | Neumorphism (07) · Claymorphism (08) · Anti-Grid (06) · Kinetic Type (15) | Each pays a legibility tax per element; density multiplies it |
| S2 = **child/family** | Neo-Brutalism (05) · Anti-Grid (06) · Skeuomorphism (09) | Aggressive or complex surfaces, wrong affordances for the audience |
| S8 = **mobile-first** | 3D/Spatial (14) as dominant · Anti-Grid (06) | Both depend on viewport area and pointer precision |
| S9 = **dwell** (hours per day) | Maximalism (12) · Y2K (13) · Kinetic Type (15) | High-stimulus surfaces exhaust on repeat exposure |

If vetoes eliminate everything, the brief is contradictory. Say so, name the
contradiction, and propose the trade-off — do not silently pick a survivor.

---

## Part 3 — Scoring cards

Score every surviving style. Add the modifiers whose condition the brief meets.
Highest total wins; ties go to Part 5.

**01 · Minimalism** — *the neutral default*
`+3` trust:critical · `+3` personality:premium · `+2` audience:professional
`+2` emotion:calm · `+2` S5 elevated · `+1` density:medium · `+1` mobile-first
`−2` emotion:excitement · `−2` personality:playful · `−3` audience:child/family

**02 · Glassmorphism**
`+3` personality:futuristic · `+2` audience:technical · `+2` device:desktop-first
`+1` density:medium · `+1` emotion:curiosity
`−2` S5 elevated · `−3` trust:critical · `−3` density:high

**03 · Liquid Glass**
`+3` audience:consumer · `+3` personality:futuristic · `+2` emotion:excitement
`+2` mobile-first · `+1` session:glance
`−2` density:high · `−3` S7 dense-relational · `−2` trust:critical

**04 · Bento Grid**
`+3` density:high · `+3` S7 layered · `+2` conversion:consider
`+2` audience:consumer · `+2` personality:precise · `+1` mixed device
`−2` personality:literary · `−2` session:dwell (as a whole-app layout)

**05 · Neo-Brutalism**
`+3` personality:bold · `+3` emotion:excitement · `+2` audience:creative
`+2` conversion:convert-now · `+1` session:glance
`−2` trust:critical · `−3` audience:child/family · `−2` S5 elevated

**06 · Brutalist / Anti-Grid**
`+3` audience:creative · `+3` personality:bold · `+2` emotion:curiosity
`+2` density:low · `+1` desktop-first
`−3` density:high · `−3` trust:critical · `−3` S5 elevated · `−2` mobile-first

**07 · Neumorphism** — *use sparingly, never for critical controls*
`+2` personality:calm/premium · `+1` density:low · `+1` audience:consumer
`−3` S5 elevated · `−3` density:high · `−3` trust:critical · `−2` mobile-first

**08 · Claymorphism**
`+3` audience:child/family · `+3` personality:playful · `+3` emotion:safety
`+2` audience:consumer · `+1` conversion:browse
`−3` density:high · `−3` audience:technical · `−2` trust:critical

**09 · Skeuomorphism / Tactile**
`+3` S7 dense-relational *in instrument UI* · `+2` personality:premium
`+2` emotion:competence · `+2` desktop-first · `+1` session:dwell
`−2` mobile-first · `−2` audience:child/family · `−1` conversion:convert-now

**10 · Swiss / International**
`+3` density:high · `+3` personality:precise · `+3` S7 dense-relational
`+2` audience:technical · `+2` trust:critical · `+2` emotion:competence
`+1` session:dwell
`−2` personality:playful · `−2` emotion:excitement · `−2` audience:child/family

**11 · Editorial / Magazine**
`+3` personality:literary · `+3` session:dwell · `+3` S7 layered
`+2` personality:premium · `+2` emotion:trust · `+1` conversion:browse
`−2` S7 dense-relational · `−2` conversion:convert-now · `−1` audience:technical

**12 · Maximalism**
`+3` personality:bold · `+3` emotion:excitement · `+2` audience:creative
`+2` session:glance · `+1` conversion:browse
`−3` trust:critical · `−3` S5 elevated · `−3` session:dwell · `−2` density:high

**13 · Y2K / Retrofuturism**
`+3` personality:nostalgic · `+3` emotion:excitement · `+2` audience:consumer
`+2` session:glance · `+1` conversion:convert-now
`−3` trust:critical · `−3` audience:professional · `−2` S5 elevated

**14 · 3D / Spatial UI**
`+3` personality:futuristic · `+3` emotion:curiosity · `+2` audience:creative
`+2` desktop-first · `+1` session:glance
`−3` mobile-first · `−3` density:high · `−2` S5 elevated

**15 · Expressive / Kinetic Typography**
`+3` audience:creative · `+3` personality:bold · `+2` emotion:curiosity
`+2` density:low · `+2` session:glance
`−3` S7 dense-relational · `−3` S5 elevated · `−2` session:dwell

---

## Part 4 — Fast path (unambiguous briefs)

Skip scoring when the brief lands cleanly in a row here. This table is a
shortcut through Part 3, not a replacement for the veto gates.

| Product type | Audience | Personality | Density | Dominant | Supporting | Avoid |
|---|---|---|---|---|---|---|
| B2B SaaS | managers, teams | trustworthy, clear | medium | Minimalism (01) | Swiss (10) | Maximalism, Y2K |
| Dev tool / AI platform | developers | technical, fast, precise | medium-high | Swiss (10) | subtle Brutalism (06) | Claymorphism, pastel gradients |
| Fintech / banking | professionals | secure, precise | medium-high | Minimalism (01) | Swiss (10) | Neo-Brutalism, Y2K |
| E-commerce (mass) | everyone | friendly, clear | high | Bento Grid (04) | Minimalism (01) | Anti-Grid, Skeuomorphism |
| Luxury / fashion | high-income | exclusive, refined | low | Editorial (11) | Minimalism (01) | Neon anything, gradients |
| Agency / studio | creative clients | bold, original | low-medium | Anti-Grid (06) | Kinetic Type (15) | Neumorphism, Bento |
| Portfolio (designer) | art directors | expressive, memorable | low | Kinetic Type (15) | Anti-Grid (06) | Dashboard layouts |
| Media / magazine | readers | intelligent, literary | high | Editorial (11) | Swiss (10) | Glassmorphism overload |
| Consumer app | 18–35 | modern, fluid | medium | Liquid Glass (03) | Bento (04) | Heavy skeuomorphism |
| Kids / education | children, parents | playful, safe | medium | Claymorphism (08) | Maximalism (12) | Brutalism, dark modes |
| Web3 / immersive | early adopters | futuristic | medium | 3D/Spatial (14) | Glassmorphism (02) | Editorial serif |
| Music / events / gaming | fans | loud, nostalgic | high | Y2K (13) | Maximalism (12) | Minimalism |
| Health / wellness | broad public | calm, human | low-medium | Minimalism (01) | Claymorphism (08) | Neon, harsh contrast |
| Restaurant / local biz | locals | appetizing, warm | medium | Editorial (11) | Neo-Brutalism (05) | 3D spatial, dark SaaS |
| Corporate / enterprise | executives | serious, stable | high | Swiss (10) | Minimalism (01) | Y2K, Maximalism |
| Developer docs | developers | clear, scannable | high | Swiss (10) | Minimalism (01) | Glass, 3D, Kinetic |
| Data / analytics product | analysts | precise, dense | high | Swiss (10) | Bento (04) | Clay, Neumorphism, Y2K |

---

## Part 5 — Tie-breakers, in order

1. **Accessibility.** The style that clears WCAG AA with less effort wins.
2. **Density durability.** The style that survives the product's *next* screen —
   the settings page, the empty state, the 40-row table — wins.
3. **Brand accommodation.** If a brand system exists, the style that adopts its
   colors and fonts without distortion wins (`docs/PRECEDENCE.md`).
4. **Mobile survivability.** If mobile is >50% of traffic, the style that
   recomposes rather than stacks wins.
5. **Still tied → Minimalism (01).** The neutral default. Say that you defaulted
   and why nothing else earned it.

---

## Part 6 — Required output

Choosing a style produces a **brief**, not a stylesheet. Print it:

```
DESIGN BRIEF
Audience        developers evaluating a tool in under 90 seconds
Product         AI coding platform · dev tool
Personality     technical / fast / precise
Density         medium-high (S1) · dense-relational (S7)
Trust           medium · A11y: standard · Device: desktop-first · Session: task

Vetoes applied  none triggered

Scores          Swiss (10)        +3 density-high +3 precise +3 dense-relational
                                  +2 technical +2 competence          = 13
                Minimalism (01)   +2 professional +1 medium-density   =  3
                Bento (04)        +3 density-high +2 precise          =  5
                Claymorphism (08) −3 technical −3 density-high        = −6

Dominant        Swiss / International (10)
Supporting      Neo-Brutalism (05) — owns display type weight only
Why not Bento   modular tiles imply feature parity; this product has one hero
                capability and a long tail, which a numbered list expresses better
Why not Clay    friendly softness contradicts an audience that buys on precision

Typography      Archivo (display) + Inter (UI) + JetBrains Mono (code, labels)
Layout          Product Screenshot Hero → Numbered Feature List → Comparison Table
Visual          real product UI, terminal frames, technical diagrams
Avoid           pastel gradients, clay characters, excessive glass, fake stats
```

A brief you cannot defend against its runner-up is a brief you did not write.
