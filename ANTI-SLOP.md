# Anti AI-Slop Rules

Universal rules that kill generic AI-generated UI. Run this before delivery,
every time.

## Severity

| Level | Meaning | Action |
|---|---|---|
| 🔴 **BLOCKER** | Breaks trust, accessibility, or honesty. Not a taste issue. | **Must be zero.** Fix before delivering. No exceptions, no justification. |
| 🟠 **STRONG SMELL** | The recognizable fingerprint of unconsidered AI output. | Fix, or justify in one line naming the design reason. |
| 🟡 **MINOR SMELL** | Sloppiness that accumulates. | Fix if cheap; note it if not. |

Three or more STRONG hits means the interface was generated, not designed.
Return to `SKILL.md` step 1.

---

## 🔴 BLOCKERS

Every one of these is a hard fail. They are not opinions.

- [ ] **Fake statistics.** "99.9% uptime", "10× faster", "Trusted by 50,000+
      teams" with no real number behind it. Fabricated precision is the fastest
      way to destroy credibility — and it is a lie you put in someone's product.
- [ ] **Fake testimonials.** "Sarah J., CEO" with no company, no person, no
      permission. Same for invented case-study results.
- [ ] **Fake logo walls.** Real companies' marks on a page they never agreed to.
- [ ] **Lorem ipsum or placeholder copy shipped as final.** Every heading must
      be real, specific and benefit-led.
- [ ] **Body text below 4.5:1 contrast.** Gray-on-gray is not "subtle."
- [ ] **Horizontal scroll on mobile at 390px.** The layout is broken, not tight.
- [ ] **Missing or invisible `:focus-visible` on interactive elements.**
      Keyboard users cannot use the interface at all.
- [ ] **Animation with no `prefers-reduced-motion` fallback.** A vestibular
      accessibility failure, not a polish item.
- [ ] **Touch targets below 44×44px** on a mobile-reachable control.
- [ ] **Information conveyed by color alone** (error states, chart series,
      status dots without labels or icons).
- [ ] **Inconsistent design tokens** — the same semantic role rendered with
      three different hex values or radii across the page.
- [ ] **Screenshots of a product that does not exist**, presented as real UI.
      Mock UI must be labeled as mock.

---

## 🟠 STRONG SMELLS

### Color & gradient
- [ ] **Purple gradient by default.** Purple-to-blue mesh behind a hero because
      it "looks AI-premium." A gradient must encode something: state, depth,
      brand. Decoration is not a reason.
- [ ] **Default neon violet (`#8B5CF6` family) as primary brand color.** The most
      statistically over-used color in AI output. If purple is genuinely on-brand,
      choose a specific shade — not the framework default.
- [ ] **Gradient text on headings** with no semantic purpose.
- [ ] **More than 2 accent colors** on one screen.

### Cards & surfaces
- [ ] **Uniform 24px radius on everything.** One radius for every element, from
      a badge to a full-width section, is a fingerprint. Radius should follow
      hierarchy — or be consistently sharp.
- [ ] **Every section wrapped in a card.** When everything is elevated, nothing
      is. Sections are sections; cards are for grouped, comparable objects.
- [ ] **More than 2 glass/translucent surfaces per view.** Glassmorphism is not
      thirty frosted panels.
- [ ] **Floating cards with large soft shadows for no reason.** Shadow encodes
      elevation, not "premium."
- [ ] **Three identical feature cards in a row.** Vary composition: bento,
      alternating, editorial split, numbered list.
- [ ] **Meaningless metric cards** — a dashboard-style KPI grid on a marketing
      page where the numbers are decorative.
- [ ] **Excessive pills.** Every label, tag, badge and button as a 999px pill.

### Layout & composition
- [ ] **Everything centered.** Universal centering is a default, not a decision.
      Left-aligned text with a strong ragged right is a choice.
- [ ] **The same hero every time.** Rotate patterns — `LAYOUT-PATTERNS.md`.
- [ ] **Desktop layout merely stacked for mobile.** Responsive means
      recomposition: different hierarchy, different crop, different nav.
- [ ] **No content hierarchy** — no obvious first thing to look at.
- [ ] **Random spacing.** 18px here, 37px there. One scale, everywhere.
- [ ] **Five-column "app store" footer** on a product with five links total.

### Typography
- [ ] **Inter/Roboto as an unconsidered default.** A grotesk can be right — but
      it must come from the style DNA, not from muscle memory.
- [ ] **One size for all body text.** Hierarchy needs ≥3 distinct type roles.
- [ ] **ALL-CAPS paragraphs.** Uppercase is for labels and eyebrows only.
- [ ] **Generic marketing copy**: "Built for modern teams", "Transform your
      workflow", "Supercharge your productivity", "The future of X". If the
      sentence works for any product, it works for none.

### Icons & imagery
- [ ] **Generic icon grid** — twelve outline icons in a 4×3 grid, each one
      loosely related to its label, none of them necessary.
- [ ] **Mismatched icon families** (filled + outlined + 3D on one screen).
- [ ] **Random emoji as feature icons** in a professional context.
- [ ] **Abstract 3D blobs floating in the hero** when the style is not 3D/Spatial.
- [ ] **Stock photography of people pointing at laptops.**

### Motion
- [ ] **900ms hover transitions.** Reads as lag, not luxury. Hover: 150–250ms.
- [ ] **Everything floats or pulses infinitely.**
- [ ] **Parallax on dense content.** Motion belongs to heroes and storytelling.
- [ ] **Scroll-jacking.** The scrollbar belongs to the reader.

---

## 🟡 MINOR SMELLS

- [ ] Section padding that never varies (every section exactly 96px).
- [ ] A "most popular" pricing badge with no visual anchoring behind it.
- [ ] Decorative dividers between every section.
- [ ] Marquees of logos or words that pause for nobody.
- [ ] Icon-only buttons without `aria-label`.
- [ ] Fake letter-spacing on serif display faces.
- [ ] `border-radius` on images that are already inside a rounded card.
- [ ] A dark-mode toggle that only inverts the background.

---

## The two questions that catch what checklists miss

1. **"Could this exact page belong to a different product?"** If yes, you built
   a template, not an interface. Find the one element only *this* product could
   have shown.
2. **"What did I remove?"** A design with nothing removed was not edited. Name
   one element you deleted and why the page is better without it.

---

## Output format

```
ANTI-SLOP AUDIT
BLOCKERS       0
STRONG         2 — uniform 20px radius on all surfaces · centered every section
MINOR          1 — icon-only share button missing aria-label
FIXED          radius now 4/8/16 by hierarchy · features left-aligned, hero centered
JUSTIFIED      none
VERDICT        clear to deliver
```

Any BLOCKER, or any unjustified STRONG hit, means **not clear to deliver**.
