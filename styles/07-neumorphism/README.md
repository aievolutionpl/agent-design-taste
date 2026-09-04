# 07 · Neumorphism (Soft UI)

**Overview:** Surfaces extruded from a single background color. Depth comes from a matched pair of soft shadows — one light (top-left) and one dark (bottom-right) — on elements that share the background's hue. Tactile, quiet, almost physical. It is also the style with the **worst accessibility record in modern UI** — read the a11y section before using it.

**Visual principles:** single-hue surfaces · dual soft shadows (light + dark) · extruded "pushable" components · inset pressed states · minimal color, shape does the work · rounded, plush geometry.

## ⚠️ Contrast & accessibility — the defining problem
Neumorphism's signature look **requires** low contrast between surface and background (typically ΔL ≤ 10%). That breaks the WCAG floor in three compounding ways:
1. **Component boundaries fail 1.4.11 Non-text Contrast (3:1):** a `#E0E0E0` card on `#ECF0F3` bg is ~1.2:1. Shadows are the only edge cue — they disappear on cheap/low-gamma screens and in bright light.
2. **Icon-only and ghost controls become invisible:** no border, no fill — just a soft bump. Users with low vision, older screens, or sunlight cannot find them at all.
3. **Disabled-looking enabled states:** everything soft and low-contrast reads as "off". Button affordance studies (e.g. Norman-group commentary, 2020 wave of neumorphic UI critiques) consistently found lower discoverability and higher misclick rates.
**Mitigation if you must use it:** keep ≥ 3:1 contrast for all interactive boundaries (add a visible 1px border or darker fill on hover/focus), never rely on shadow alone to signal interactivity, always show visible focus rings (`:focus-visible`, 3px accent ring), and put text in #111-on-light / #F5F5F5-on-dark with ≥ 4.5:1.

## When NOT to use
- **Never:** banking, healthcare, government, accessibility-first products, dense data tools, dashboards with many controls, anything WCAG-compliance-audited.
- **Avoid:** dark-mode-heavy products (soft shadows fail harder on dark), low-end display audiences, enterprise procurement checklists.
- **OK only for:** decorative marketing surfaces, smart-home/ IoT companion apps, weather/ambience widgets, landing heroes — i.e. content that can fall back to plain flat panels without loss. If a control must be found and used by everyone, neumorphism is the wrong tool; use it as garnish over an accessible base, not as the base.

## Typography
- **Recommended families (Google Fonts):** Rounded-friendly sans: Nunito Sans, Jakarta Sans, Manrope. Accent: Poppins (600–700).
- **Pairing:** Manrope (H1–H3, 700–800) + Nunito Sans (body) — friendly geometry matches the plush surfaces.
- **Scale:** H1 48/1.1 · H2 36/1.2 · H3 24/1.3 · body 16/1.65 · small 14/1.5. Soft style tolerates slightly looser leading.
- **Body:** 16px, letter-spacing 0, max 60ch.
- **Uppercase:** small pill labels only, 11–12px +0.06em.
- **CSS:**
```css
h1 { font: 800 48px/1.1 'Manrope', sans-serif; letter-spacing: -0.015em; }
body { font: 400 16px/1.65 'Nunito Sans', sans-serif; }
.pill { font: 600 11px/1 'Nunito Sans'; letter-spacing: 0.06em; text-transform: uppercase; }
```
- **Typical mistakes:** gray-on-gray text below 4.5:1; ultra-thin weights (200–300) blending into surfaces; sharp condensed fonts (wrong personality).

## Layout & Frames
- **Grid:** 12-col, max 1100px, generous gutters (32px). Neumorphism works best with fewer, larger cards.
- **Spacing:** airy — sections 96px+, padding inside cards 32px+ so shadows have room to read.
- **Hero:** centered or split hero with one extruded device/widget mockup; the widget is the star.
- **Frame patterns:** centered hero with extruded widget, card trios, stat tiles, large pill CTA band.
- **Responsive:** cards stack; keep 24px+ page margins so shadows don't clip at the viewport edge.

## Visual hierarchy
- First seen: extruded hero widget, then the filled (accent) CTA, then heading. Hierarchy must come from **size and position** — elevation is too subtle to carry it alone.

## Color system
- **Light:** bg #ECF0F3 · surface same as bg (#ECF0F3 — that's the point) · text #111827 · secondary #4B5563 · shadow-dark #C8D0E0 · shadow-light #FFFFFF · accent #4F6AF0 (interactive fill only).
- **Dark:** bg #23272E · surface same · text #E5E7EB · secondary #9CA3AF · shadow-dark #14161B · shadow-light #3B424D · accent same.
- Near-monochrome + one accent. Avoid: saturated section backgrounds, gradients (they kill the matched-shadow illusion), second accent.

## Components
Buttons: raised = surface + dual shadow (`6px 6px 12px dark, −6px −6px 12px light`); pressed = **inset** (`inset 4px 4px 8px dark, inset −4px −4px 8px light`). Primary CTA: filled accent with soft matching shadow — the ONLY high-contrast control. Cards: raised panels, radius 20–24px. Inputs: **inset** wells, radius 12–16px. Toggles: inset track + raised knob. Icon buttons: raised circles/squircles, must include a visible border or label for a11y. Tabs: raised active pill on an inset track. Sliders: inset track, raised thumb. Never: sharp corners (radius < 8px breaks the softness), heavy borders, hard shadows.

## Shape language
Radius 12–28px, generous. No visible borders — boundary = shadow pair. Depth = soft blur (8–20px) with matched angles (light source top-left). Two elevation levels only: raised and inset. Focus rings: 3px solid accent offset 2px — always visible.

## Visual direction
Fits: soft 3D-feel product renders, pastel gradients *inside* accent elements only, rounded line icons (2px), frosted overlays. Breaks cohesion: brutal black borders, neon, hard shadows, dense photography (photo edges clash with extruded surfaces).

## Motion & Interaction
Soft and springy: 200ms ease-out on press (raise→inset swap is the signature interaction); cards lift 2px on hover. `prefers-reduced-motion`: disable lift, keep instant inset state change. Focus states must never be shadow-only — use the accent ring.

## When to use
Smart-home controls, ambient/wellness apps, gadget companion apps, decorative hero widgets, concept showcases. Audience: consumer, relaxed, tactile.

## When NOT to use (recap — non-negotiable)
Fintech/banking, healthcare, government, enterprise dashboards, data-dense tools, or any product with an accessibility requirement. The style's core mechanism (surface≈background) is structurally incompatible with WCAG 1.4.11. Use flat cards with clear borders instead.

## Do
- Match surface and background hue (that's the aesthetic)
- Always pair shadows: light top-left + dark bottom-right
- Use inset for pressed/active and input wells
- One filled accent CTA — your guaranteed-contrast control
- Add a visible focus ring and a fallback border on interactive elements
- Keep card count low; shadows need whitespace
- Test on a cheap display and in sunlight

## Don't
- Rely on shadow alone to mark a button
- Put gray text below 4.5:1 contrast
- Use it in dark-heavy data UIs or compliance contexts
- Hard shadows, sharp corners, heavy borders
- Stack neumorphic cards on neumorphic cards (mush)
- Gradient backgrounds behind neumorphic surfaces (shadows stop matching)

## Anti AI-slop (neumorphism edition)
Everything soft but nothing clickable, white-on-white text, gray ghost buttons everywhere, neumorphic tables (never), random pastel gradients behind the soft panels — slop here = softness applied to a context that needs legibility. If you can't screenshot it and still point at the primary CTA in one second, it failed.

## Good vs Bad examples
- **Good:** smart-home dashboard concept — 6 large extruded tiles, inset temperature well, one accent-filled "away mode" button, all labels ≥ 4.5:1.
- **Bad:** neumorphic settings page — ghost icon-buttons, gray labels at 1.6:1, five levels of soft elevation, no visible focus anywhere. It looks like a screensaver and behaves like one.