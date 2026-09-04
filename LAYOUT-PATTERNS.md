# Layout Pattern Library — a decision library, not a menu

43 ways to compose a page. The #1 AI layout failure is not color — it is
generating **centered hero → three cards → CTA → footer** every single time.

Each pattern carries the information needed to *choose* it: when it works, the
density it wants, which styles it fits, how it recomposes on mobile, where the
CTA goes, and the mistake agents keep making with it.

**Legend** · `D` density fit · `✓` fits these styles · `✗` fights these styles
· `📱` mobile recomposition · `→` CTA + hierarchy · `⚠` common AI mistake

Sections are separable — load `§ Hero` and `§ Feature` for a landing page; you
do not need all 43 in context.

---

## § Hero patterns

### 1 · Split Hero
Text one side, visual the other (50/50 or 60/40).
**Use when** a real screenshot or photograph carries meaning and the value
proposition fits two lines. `D` medium
`✓` Swiss, Minimalism, Bento, Glassmorphism  `✗` Anti-Grid, Kinetic Type
`📱` Decide which half leads: if the image *explains*, image first; if it
decorates, text first. Never squeeze 50/50 into two thin columns.
`→` CTA under the sub-headline, left-aligned to the text column. H1 → sub → CTA.
`⚠` A floating browser mockup at 40% scale where no UI text is readable.

### 2 · Centered Hero
Headline, sub, CTA stacked centre.
**Use when** the visual comes *below* the fold, not beside it — and the message
is short enough to centre without a ragged block. `D` low
`✓` Minimalism, Claymorphism, Y2K  `✗` Editorial, Swiss (as a whole page)
`📱` Already vertical; reduce H1 by ~35% and tighten the CTA gap.
`→` One CTA, optionally one ghost secondary. Never three equal buttons.
`⚠` Used by default. If you did not consider a split or editorial hero first,
this is not a choice.

### 3 · Editorial Hero
Oversized headline across the full width, magazine dek, image below.
**Use when** the words are the product: manifestos, campaigns, publications.
`D` low  `✓` Editorial, Brutalist, Kinetic, Maximalism  `✗` Dashboards, Bento
`📱` Headline stays oversized (that is the point); the dek drops to 2 lines.
`→` CTA is often a link, not a button. Hierarchy: headline dominates absolutely.
`⚠` Setting the huge headline in the body font at 700 weight and calling it
editorial.

### 4 · Product Screenshot Hero
Real UI, large, above or behind a short headline.
**Use when** the interface *is* the argument — dev tools, SaaS, design software.
`D` medium  `✓` Swiss, Minimalism, Bento, Glass  `✗` Claymorphism, Y2K
`📱` Crop to the single most meaningful region at 2× scale. Never shrink the
whole screenshot until nothing is legible.
`→` CTA above the screenshot; the image is proof, not the action.
`⚠` A mocked-up dashboard with invented numbers. That is a 🔴 anti-slop blocker.

### 5 · Dashboard Hero
The product's dashboard is the hero, slightly tilted or in a browser frame.
**Use when** density itself is the selling point (analytics, observability).
`D` high  `✓` Swiss, Bento, Glass  `✗` Editorial, Clay
`📱` Replace the full dashboard with one widget, real size, real data.
`→` CTA above; a caption naming what the user is looking at.
`⚠` 3D perspective tilt so aggressive the UI becomes texture.

### 6 · Full-bleed Visual Hero
Image or video fills the viewport, text overlaid bottom-left.
**Use when** atmosphere sells: hospitality, travel, fashion, food. `D` low
`✓` Editorial, Maximalism, Minimalism  `✗` Dev tools, dense SaaS
`📱` Change the crop, not the scale — a 16:9 landscape becomes a 4:5 portrait
focused on the subject.
`→` CTA in the text block. Overlay must be a scrim, not opacity on the text.
`⚠` White text straight onto a bright photo: a contrast blocker every time.
Use a gradient scrim and measure the actual ratio.

### 7 · Terminal Hero
A live-looking terminal or REPL types the product's value.
**Use when** the audience lives in a terminal. `D` medium
`✓` Swiss, Brutalist, Minimalism  `✗` Clay, Liquid Glass
`📱` Reduce to 4–6 lines, monospace at 13–14px minimum, horizontal scroll inside
the terminal frame only — never the page.
`→` CTA is the install command, copyable, with a real copy button.
`⚠` Fake command output that would not actually be produced by that command.

### 8 · Typographic Hero
Type *is* the visual: oversized, variable, kinetic.
**Use when** the brand is expressive and the page is short. `D` low
`✓` Kinetic Type, Brutalist, Maximalism, Editorial  `✗` Fintech, health, enterprise
`📱` Reflow the line breaks deliberately at each breakpoint — never let a
display headline wrap by accident.
`→` CTA must survive the type: a plain, high-contrast button.
`⚠` Animated headline carrying information that exists nowhere else on the page.

### 9 · 3D Object Hero
A hero object centre stage, orbiting or scroll-reactive.
**Use when** the product is physical, spatial, or genuinely three-dimensional.
`D` low  `✓` 3D/Spatial, Glass, Y2K  `✗` Editorial, Swiss, dense products
`📱` Ship a static high-quality render. A 3D canvas on mobile costs battery and
usually drops frames.
`→` CTA below the object, never overlapping it.
`⚠` An abstract 3D blob that represents nothing. 🟠 anti-slop.

### 10 · Video Background Hero
Muted looped video, high-contrast text overlay.
**Use when** motion communicates something a still cannot. `D` low
`✓` Editorial, Maximalism, 3D  `✗` Anything data-heavy
`📱` Replace with a poster image. Do not autoplay video on cellular.
`→` Same as full-bleed: scrim behind the text block.
`⚠` No `prefers-reduced-motion` fallback. 🔴 blocker.

### 11 · Split Diagonal Hero
A diagonal divides text and visual.
**Use when** you want energy without disorder. `D` medium
`✓` Neo-Brutalism, Y2K, Maximalism  `✗` Swiss, Minimalism, Editorial
`📱` The diagonal becomes a horizontal band; a diagonal at 390px just clips text.
`→` CTA inside the text field, well clear of the diagonal edge.
`⚠` Text placed under the diagonal so the first and last words are cut off.

### 12 · Card Stack Hero
Overlapping stacked cards fan out on scroll.
**Use when** you have 3–5 parallel value props of equal weight. `D` medium
`✓` Bento, Glass, Liquid Glass  `✗` Editorial, Swiss
`📱` Become a vertical list, not a tiny stack. Fanning needs width.
`→` CTA after the stack resolves.
`⚠` Scroll-driven animation with no reduced-motion static state. 🔴 blocker.

---

## § Feature and content patterns

### 13 · Bento Feature Grid
Asymmetric modular tiles, one hero tile.
**Use when** the product has one headline capability and several supporting
ones. `D` high  `✓` Bento, Glass, Swiss, Neo-Brutalism  `✗` Editorial, Anti-Grid
`📱` Ordered stack, **hero tile first**. Never let CSS grid auto-flow decide the
narrative order.
`→` CTA in the hero tile or after the grid, not repeated per tile.
`⚠` Twelve equal tiles. Equal tiles are a table, not a bento.
**a11y** Reading order must match visual order; check DOM order after any
`grid-area` reordering.

### 14 · Alternating Feature Sections
Text/image zig-zag down the page.
**Use when** there are 3–5 features each needing a sentence and a picture.
`D` medium  `✓` Minimalism, Swiss, Editorial, Clay  `✗` Anti-Grid
`📱` All become text-then-image. Do **not** preserve the alternation — on mobile
it just looks like inconsistent ordering.
`→` One CTA at the end, not one per section.
`⚠` Six alternating sections. After the third, the rhythm is a lullaby.

### 15 · Numbered Feature List
01 / 02 / 03 vertical list with large numerals.
**Use when** the features are sequential, or one clearly matters most.
`D` medium-high  `✓` Swiss, Brutalist, Editorial, Minimalism  `✗` Clay, Y2K
`📱` Numerals shrink but stay dominant; the list stays a list.
`→` CTA after the last item. Hierarchy: numeral → title → description.
`⚠` Numbers styled as decoration with no ordinal meaning.
**a11y** Use `<ol>`. Do not fake numbering with pseudo-elements on a `<div>`.

### 16 · Sticky Storytelling
Left column sticky, right column scrolls through steps.
**Use when** explaining a process where the visual updates per step.
`D` medium  `✓` Swiss, Minimalism, Glass, 3D  `✗` Editorial long-form
`📱` Collapse to a linear sequence: visual, then step, repeated. Sticky
positioning at 390px steals the whole viewport.
`→` CTA after the last step.
`⚠` Sticky element taller than the viewport, so it can never fully show.
**a11y** Ensure scroll position is not the *only* way to reach later content.

### 17 · Horizontal Showcase
Horizontally scrolling gallery.
**Use when** items are peers and the set is browsable, not readable. `D` medium
`✓` Editorial, Maximalism, Bento, Y2K  `✗` Swiss (as a primary section)
`📱` Native touch scroll with visible affordance (a peeking next card).
`→` No CTA inside cards; one after the rail.
`⚠` Horizontal scroll with no visual hint that more exists.
**a11y** Keyboard-reachable: arrow keys or focusable items that scroll into view.

### 18 · Comparison Table
You vs alternatives, honest and specific.
**Use when** the audience is actively comparing. `D` high
`✓` Swiss, Minimalism, Bento  `✗` Maximalism, Kinetic
`📱` Do **not** shrink the table. Transform: one card per competitor, or a
sticky first column with horizontal scroll inside the table container.
`→` CTA in your own column, once.
`⚠` Every competitor row marked ✗ and yours ✓. Nobody believes it.
**a11y** Real `<table>` with `<th scope>`; a caption; never a grid of divs.

### 19 · Tabbed Use-Cases
Switch between personas or industries.
**Use when** one product genuinely serves distinct audiences. `D` medium
`✓` Swiss, Bento, Minimalism  `✗` Editorial
`📱` Tabs become a horizontal scroller or a select; content stacks below.
`→` A CTA per tab is legitimate — each persona converts differently.
`⚠` Four tabs whose content differs only in the noun.
**a11y** Full tab pattern: `role="tablist"`, arrow-key navigation, `aria-selected`.

### 20 · Metrics Strip
One band of 3–4 real KPIs.
**Use when** the numbers are real, sourced, and impressive. `D` low
`✓` Swiss, Minimalism, Bento, Editorial  `✗` —
`📱` 2×2 grid, not a single row of tiny numbers.
`→` No CTA. This is proof, not action.
`⚠` Invented numbers. 🔴 blocker. If you do not have real figures, delete
the section — an honest page beats a decorated lie.

### 21 · Logo Wall
Customer logos, usually grayscale.
**Use when** you have permission and the names mean something to the audience.
`D` low  `✓` most styles  `✗` Anti-Grid
`📱` Two columns, or a paused marquee. Never eight logos at 40px wide.
`→` None.
`⚠` Logos of companies that never agreed. 🔴 blocker.
**a11y** Real `alt` text with the company name; not `alt="logo"`.

### 22 · Case Study Grid
2–3 deep cards, image + result.
**Use when** the work is the argument. `D` medium
`✓` Editorial, Swiss, Minimalism, Anti-Grid  `✗` Clay
`📱` One per row, full-bleed image, result metric prominent.
`→` CTA per card ("Read the case"), plus one section CTA.
`⚠` Three cards with identical crops and identical made-up percentages.

### 23 · Magazine Grid
Mixed-size article cards, newspaper-front-page logic.
**Use when** content volume is real and items have genuinely different weight.
`D` high  `✓` Editorial, Swiss, Maximalism  `✗` Clay, Neumorphism
`📱` Priority-ordered single column. The lead story stays the lead.
`→` None; the cards are the actions.
`⚠` A magazine grid where every item has the same importance — that is a list.

### 24 · Annotated Screenshot
Product UI with callout lines.
**Use when** the UI needs interpretation. `D` medium
`✓` Swiss, Minimalism, Bento  `✗` Maximalism
`📱` Callouts become a numbered list beneath a croppable image. Lines and dots
at 390px are unreadable.
`→` CTA after.
`⚠` Nine callouts. Three to five, maximum.
**a11y** Callout text must exist in the DOM, not only inside the image.

### 25 · Before / After Slider
Draggable comparison.
**Use when** the change is visual and obvious. `D` low
`✓` most styles  `✗` Swiss (rarely earns it)
`📱` Works well; ensure the handle is ≥44px and drag does not fight page scroll.
`→` CTA after.
`⚠` Drag-only with no keyboard control.
**a11y** Back the handle with an `<input type="range">` so it is keyboard-operable.

### 26 · FAQ Accordion (two-column)
Sticky heading left, accordion right.
**Use when** there are ≥5 real questions people actually ask. `D` medium
`✓` Minimalism, Swiss, Editorial  `✗` Maximalism
`📱` Single column, heading above.
`→` A support link, not a purchase CTA.
`⚠` Marketing copy disguised as questions ("Why is X so great?").
**a11y** `<button>` triggers with `aria-expanded`; content reachable when open.

### 27 · Integration Marquee
Infinite scrolling logo strip.
**Use when** the integration count is genuinely a feature. `D` low
`✓` Bento, Glass, Y2K, Maximalism  `✗` Editorial, Minimalism
`📱` Slower, or static grid.
`→` None.
`⚠` No pause on hover and no reduced-motion stop. 🔴 blocker.

### 28 · Testimonial Masonry
Varied-size quote cards.
**Use when** you have real quotes of genuinely different lengths. `D` medium
`✓` Bento, Editorial, Maximalism  `✗` Swiss
`📱` Single column, longest quote first.
`→` None.
`⚠` Nine identical cards with stock avatars. 🔴 blocker if the people are fake.

### 29 · Video Testimonial Feature
One strong talking-head clip.
**Use when** you have one genuinely good clip. `D` low
`✓` Editorial, Minimalism, Swiss  `✗` Brutalist
`📱` Poster image + play; never autoplay with sound.
`→` CTA after.
`⚠` A wall of thumbnails nobody will watch.
**a11y** Captions are mandatory; a transcript is better.

### 30 · Interactive Demo Embed
The real product, sandboxed, on the page.
**Use when** the product demos itself in under 30 seconds. `D` high
`✓` Swiss, Bento, Glass, Minimalism  `✗` Editorial
`📱` Offer a guided video instead if the real UI needs a pointer.
`→` "Try it with your own data" after the demo.
`⚠` An "interactive" demo that is a looping GIF.
**a11y** Keyboard-operable, or offer an equivalent path.

### 31 · Timeline Section
Journey or how-it-works, horizontal or vertical.
**Use when** chronology or sequence carries meaning. `D` medium
`✓` Editorial, Swiss, Minimalism  `✗` Bento
`📱` Always vertical, with the connector line preserved.
`→` CTA at "today" or at the end.
`⚠` A timeline of company milestones nobody outside the company cares about.

### 32 · Pricing Toggle Cards
Monthly/annual toggle, plans side by side.
**Use when** there are 2–4 plans with real differences. `D` medium
`✓` Minimalism, Swiss, Bento, Clay  `✗` Anti-Grid, Kinetic
`📱` Recommended plan **first**, then the rest. Never the desktop left-to-right
order shrunk down.
`→` One CTA per card; the recommended one is visually anchored by size,
elevation or border — not only by a badge.
`⚠` "Most popular" badge as the only differentiation. Check it in grayscale.
**a11y** The toggle is a real control with a label; price changes announced.

### 33 · Pricing Comparison Slider
Drag between tiers; the feature list updates.
**Use when** pricing is usage-based and continuous. `D` medium
`✓` Swiss, Bento, Glass  `✗` Editorial
`📱` Slider plus a numeric input — dragging a fine slider on a phone is painful.
`→` CTA updates with the tier.
`⚠` A slider whose steps do not correspond to real pricing breakpoints.
**a11y** `<input type="range">` with `aria-valuetext` reading the price.

---

## § Conversion patterns

### 34 · CTA Banner
Full-width band, one message, one button.
**Use when** the page has earned the ask. `D` low  `✓` all  `✗` —
`📱` Full width, generous vertical padding, button ≥44px tall.
`→` Exactly one action.
`⚠` Three CTA banners on one page. The ask stops meaning anything.

### 35 · Final Split CTA
Recap left, big CTA right.
**Use when** the decision needs one last summary. `D` low
`✓` Swiss, Minimalism, Bento  `✗` Anti-Grid
`📱` Recap above, CTA below.
`→` Primary plus one low-commitment alternative ("talk to us").
`⚠` A recap that repeats the hero headline verbatim.

### 36 · Sticky Mini-CTA
Slim bar appears after ~50% scroll.
**Use when** the page is long and the action is simple. `D` low
`✓` most  `✗` Editorial long-form reading
`📱` Bottom bar, dismissible, respecting safe-area insets.
`→` One button; keep the bar under 64px.
`⚠` Appearing instantly, covering content, with no dismiss.
**a11y** Must not trap focus; must be dismissible by keyboard.

### 37 · Inline CTA in Editorial Flow
CTA styled as part of the text flow.
**Use when** the reader is mid-argument and convinced. `D` low
`✓` Editorial, Minimalism  `✗` Bento, dashboards
`📱` Full-width block inside the measure.
`→` A link or a modest button — not a billboard mid-paragraph.
`⚠` Breaking the reading rhythm with a full-color card.

### 38 · Email Capture with Value Promise
Input + button + one specific benefit line.
**Use when** you can name what arrives and how often. `D` low
`✓` all  `✗` —
`📱` Stacked; input ≥44px; correct `type="email"` and `autocomplete`.
`→` One field. Every extra field costs conversions.
`⚠` "Subscribe to our newsletter" with no promise of content or cadence.
**a11y** A real `<label>`; placeholder is never a label.

---

## § Structural patterns

### 39 · Sidebar App Layout
Persistent nav + content area.
**Use when** the product has ≥6 destinations used repeatedly. `D` high
`✓` Swiss, Minimalism, Bento, Glass  `✗` Editorial, Maximalism
`📱` Bottom tab bar (≤5 items) or a drawer. Not a squeezed sidebar.
`→` No marketing CTA. Primary action lives in the content area.
`⚠` Marketing patterns leaking into app UI.
**a11y** `<nav>` with a skip link to main content; current page marked
`aria-current="page"`.

### 40 · Top-Bar Marketing Layout
Slim sticky navbar, full-width sections.
**Use when** it is a marketing site. `D` medium  `✓` all  `✗` —
`📱` Burger or overlay; the primary CTA stays visible in the bar.
`→` One CTA in the bar, matching the hero CTA.
`⚠` Nine nav links. Six is the practical ceiling.
**a11y** Sticky headers must not cover the focused element on tab.

### 41 · Overlay Navigation
Fullscreen or panel menu behind a trigger.
**Use when** the navigation is an experience, or there are few destinations.
`D` low  `✓` Editorial, Anti-Grid, Kinetic, Maximalism  `✗` Dashboards
`📱` Natural fit.
`→` The CTA can live in the overlay if it is also elsewhere.
`⚠` A hamburger on desktop hiding four links that would have fit.
**a11y** Focus trap while open, ESC closes, focus returns to the trigger.

### 42 · Footer as Sitemap Grid
Organized columns plus one human element.
**Use when** the site is large enough to need a sitemap. `D` medium
`✓` all  `✗` —
`📱` Accordion sections, or two columns.
`→` Newsletter capture or contact — one, not both.
`⚠` A five-column footer on a five-link site. Scale the footer to the site.

### 43 · Breadcrumb + Filter Bar
Above a listing grid.
**Use when** the catalogue needs narrowing. `D` high
`✓` Swiss, Bento, Minimalism  `✗` Editorial
`📱` Filters in a bottom sheet with an applied-count badge; breadcrumb
truncates from the middle.
`→` None; the results are the action.
`⚠` Filters that reload the page and lose scroll position.
**a11y** Announce the result count on change (`aria-live="polite"`).

---

## Selection rules

1. **Vary rhythm between adjacent sections.** Never stack two grid-heavy
   patterns back to back. Grid → prose → grid reads; grid → grid → grid does not.
2. **One or two "wow" patterns per page.** The rest should be quiet. A page of
   highlights has no highlights.
3. **Name the mobile variant before you build the desktop one.** Patterns 13,
   17, 18, 19, 23 and 32 fail hardest when left to "just stack".
4. **Rotate across projects.** If your last page was Split Hero + Alternating
   Sections, this one is not. Keep a note of what you used last.
5. **Match density to the style.** A pattern marked `D high` inside a low-density
   style (Clay, Neumorphism, Kinetic) is a conflict — change one of them.
