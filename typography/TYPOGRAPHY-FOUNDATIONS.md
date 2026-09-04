# Typography Foundations

Typography is not a font list. It is the fastest signal a product sends about
what kind of thing it is. Readers decide "serious / friendly / cheap / precise"
from letterforms before they read a word.

Cross-style baseline. Each style DNA overrides where it differs.

---

## 1. Roles before families

Assign roles first, then pick families to fill them. A project has 2–3 families
covering 3–5 roles — never five families covering five roles.

| Role | Job | Typical families |
|---|---|---|
| **Display** | Personality. H1–H2, hero statements | Fraunces, Playfair, Space Grotesk, Archivo Black, Unbounded, Instrument Serif |
| **Text** | Long-form reading, paragraphs | Inter, Instrument Sans, Source Serif, Newsreader, IBM Plex Sans |
| **UI** | Labels, buttons, nav, tables, form fields | Inter, Archivo, Jakarta Sans, IBM Plex Sans |
| **Mono** | Code, data, numeric columns, technical labels | JetBrains Mono, IBM Plex Mono, Space Mono |
| **Accent** | One deliberate exception (eyebrow, pull-quote, price) | anything, used ≤3 times per page |

Text and UI can be the same family. Display and Text should usually not be.

---

## 2. What a typeface signals

The agent's job is to match a signal to the audience emotion from `SKILL.md`
step 1 — not to pick a font it likes.

| Signal | Comes from | Reads as | Fits |
|---|---|---|---|
| **Trust / institutional** | Moderate contrast serif, generous x-height, restrained terminals | Established, careful | Fintech, health, legal, education |
| **Precision / technical** | Neo-grotesk, tight apertures, uniform stroke, tabular numerals | Engineered, exact | Dev tools, data, infrastructure |
| **Warmth / human** | Humanist sans or soft serif, open apertures, slight calligraphic axis | Approachable, honest | Wellness, community, local business |
| **Premium / editorial** | High-contrast display serif, tight display tracking, wide margins | Considered, expensive | Luxury, fashion, publishing |
| **Playful / safe** | Rounded terminals, high x-height, geometric bowls | Friendly, non-threatening | Kids, education, consumer onboarding |
| **Nostalgic / retro** | Era-specific letterforms (techno, bubble, slab) | Referential, fun | Music, events, games, drops |
| **Neutral / invisible** | System stack or plain grotesk | Gets out of the way | Documentation, internal tools, dashboards |

### The metrics that produce those signals

- **x-height** — tall x-height reads as modern, confident, legible at small
  sizes (Inter, Archivo). Small x-height reads as classical and elegant, and
  needs larger sizes to stay readable (Playfair, EB Garamond).
- **Width** — condensed faces increase density and urgency; extended faces
  read as luxurious or technological and eat horizontal space fast.
- **Contrast** (thick-to-thin stroke variation) — high contrast reads as
  editorial and refined, and collapses at small sizes and on low-DPI screens.
  Low contrast survives everywhere.
- **Aperture** — open apertures (the gap in `c`, `s`, `a`) increase legibility
  at distance and small size; closed apertures read as tight and technical.
- **Optical size** — real display cuts have tighter spacing and finer detail.
  Using a text cut at 96px looks loose; a display cut at 14px looks fragile.
  If a family ships optical-size variants, use them.

---

## 3. Scale

**Modular scale.** Pick one ratio and stay on it:

| Ratio | Name | Use for |
|---|---|---|
| 1.200 | Minor third | Dense dashboards, data UI |
| 1.250 | Major third | Product UI, app screens |
| 1.333 | Perfect fourth | Marketing pages, standard landing |
| 1.500 | Perfect fifth | Editorial, expressive, low-density |

At 1.333 from 16px: `12 · 16 · 21 · 28 · 38 · 50 · 67`.

**Fluid type with `clamp()`.** Never scale type with `vw` alone — it produces
unreadable text at 320px and absurd text at 2560px. Always min / preferred / max:

```css
/* clamp(min, fluid, max) — the fluid term needs a rem component
   so the text still responds to the user's browser font-size setting */
h1  { font-size: clamp(2.25rem, 1.5rem + 3.5vw, 4.5rem);  line-height: 1.05; }
h2  { font-size: clamp(1.75rem, 1.2rem + 2.2vw, 3rem);    line-height: 1.15; }
p   { font-size: clamp(1rem,    0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }
```

**Line-height tightens as size grows**: H1 1.02–1.15 · H2–H3 1.15–1.3 ·
body 1.5–1.7 · UI labels 1.2–1.4.

**Measure**: 60–75 characters for body, 45–60 for wide-set serif editorial,
30–40 for captions. Over 90 characters, scanning fails.

---

## 4. Weight strategy

- Choose a family with **≥4 weights**; ship **3** (e.g. 400 / 500 / 700).
- Hierarchy comes from **size + weight + color**, never weight alone.
- Light weights (200–300) only above 32px, and never on dark backgrounds where
  they thin out further.
- **Variable fonts**: one file, all weights, and an axis you can animate. Prefer
  them where the family offers one — but subset, or you ship every axis you
  never use.

---

## 5. Heading rhythm

A page has one H1. Below it, headings alternate density — a large section head
followed by tight subheads reads as structure; five equal headings reads as a
list of nothing.

- Space **above** a heading > space below it (the heading belongs to what
  follows). Typical: `margin-top: 2em; margin-bottom: 0.5em`.
- Eyebrow labels (11–12px, +0.08–0.1em tracking, uppercase) belong to the
  heading below them: 8px gap, not 24px.
- Never skip levels for size reasons. If H3 needs to look bigger, change the
  scale — not the tag.

---

## 6. Letter-spacing and case

| Context | Tracking |
|---|---|
| Display ≥ 48px | −0.02em to −0.04em (large type looks loose at default) |
| Headings 24–48px | −0.01em to −0.02em |
| Body | `normal`. Never touch it. |
| Uppercase labels ≤ 12px | +0.06em to +0.1em |
| All-caps display | +0.02em, and only if the style calls for it |

Uppercase is for eyebrows, labels and short buttons. Never for paragraphs,
never for headings above ~24px unless the style DNA explicitly demands it.

---

## 7. Language support — check before you commit

A font that lacks your characters is not a style choice, it is a bug.

- **Polish** needs `ą ć ę ł ń ó ś ź ż Ą Ć Ę Ł Ń Ó Ś Ź Ż` — verify `ł` and `ż`
  specifically; they are the first to be missing or badly drawn in display
  faces. On Google Fonts, filter by the **Latin Extended** subset.
- **Czech / Slovak / Hungarian** need long-double acutes and carons; **Turkish**
  needs dotless `ı` and `İ`; **Romanian** needs comma-below `ș ț`, not cedilla.
- **Greek / Cyrillic / CJK** — most display faces do not cover these. Plan a
  separate family per script and match x-height, not name.
- Test with a real string, not "Lorem ipsum":
  `Zażółć gęślą jaźń · Příliš žluťoučký kůň · İstanbul'da`

---

## 8. Performance — the cost of the choice

| Decision | Cost | Do this instead |
|---|---|---|
| 4 families × 4 weights, all loaded | 8–12 files, layout shift, slow LCP | 2 families, 3 weights, `woff2` only |
| Static weights for a variable family | 5× the bytes | One variable file, subset to the axes used |
| No `font-display` | Invisible text (FOIT) on slow connections | `font-display: swap` (or `optional` for decorative) |
| No fallback stack | Layout jumps when the webfont lands | Metric-similar fallback + `size-adjust` |
| Fonts fetched from a third-party CDN | Extra connection, privacy exposure | Self-host, `<link rel="preload">` the critical face |

```css
@font-face {
  font-family: "Archivo";
  src: url("/fonts/archivo-var.woff2") format("woff2-variations");
  font-weight: 400 700;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0100-017F; /* Latin + Latin Extended-A */
}
:root {
  --font-display: "Archivo", "Helvetica Neue", Arial, sans-serif;
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
}
```

Every family in the stack after the first is a real fallback that will be seen
by someone. Choose ones with similar metrics.

---

## 9. Decision examples

Each is one sentence of justification — the standard the agent must meet.

| Product | Stack | Why |
|---|---|---|
| **Fintech dashboard** | Inter (UI + text) · JetBrains Mono (figures) | Neutral precision plus tabular numerals; money columns must align, and personality here reads as risk |
| **Creative agency** | Instrument Serif (display) · Inter (text) | A character-led display face carries the portfolio; the body stays neutral so the work is the loudest thing on the page |
| **Developer tool** | Archivo (display) · Inter (UI) · JetBrains Mono (code) | Grotesk + mono is the vernacular of the audience; deviating from it reads as unfamiliarity with the domain |
| **Editorial / long-form** | Newsreader (reading face) · Inter (UI chrome) | A real reading serif for 2,000-word sessions; a neutral sans keeps navigation from competing with the article |
| **Kids' education** | Baloo 2 (display) · Nunito (text) | Rounded terminals and a tall x-height read as safe and are legible to early readers |
| **Luxury fashion** | Playfair Display (display) · Jost (text) | High stroke contrast signals craft; the geometric sans keeps commerce chrome quiet |

**The rule:** the agent must be able to write one sentence naming the *audience
emotion* the family serves. "Because the style says so" is not that sentence.

---

## 10. The AI typography fingerprint

- Inter at every size and weight — zero personality, and usually not a decision.
- `letter-spacing: normal` on a 64px display headline: characters collide.
- All-caps H1 with positive tracking on a serif: reads as shouting.
- Body at 14px "because it fits": it does not fit, the layout is wrong.
- Two sans-serifs that look identical, presented as a "pairing."
- Line length above 90 characters in a full-width container.
- Numbers in a table set in a proportional face, so columns never align.

---

Full per-style specs live in each `styles/<style>/README.md` § Typography.
This file is the shared baseline; the style DNA wins where they differ.
