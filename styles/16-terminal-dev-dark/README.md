# 16 · Terminal / Dev Dark

**Signal on black.**

## 01 · Overview

The interface borrows the terminal's grammar: monospaced display type, a near-black canvas, one phosphor accent, and real commands where other sites put marketing copy. It reads as *built by people who use the thing*, which is the only credibility a developer audience extends on first contact.

## 02 · Design philosophy

Developers trust what they can run. This style puts the product's actual surface — the install command, a real session, a changelog — at the centre of the page and strips everything that would not survive in a terminal: gradients, illustrations, decorative motion. It is not "dark mode applied to a SaaS template"; the command line is the information architecture.

**Design decisions explained — why, not just what**

- **Why these fonts:** a monospace display face (JetBrains Mono) signals "this is a tool you operate", and it keeps code, commands and headlines on one optical grid; a humanist sans (IBM Plex Sans) carries body text because long mono paragraphs tire the eye
- **Why this radius:** 4–8px — the radius of a terminal window and a key cap; 0 reads brutalist, 16+ reads consumer app
- **Why this density:** medium-high — developers scan; a real session, a table and a changelog say more per pixel than three feature cards

## 03 · Visual principles

dark-native canvas · monospace display, sans body · one phosphor accent for actions and success · real commands as content · hairline structure, no shadows · status-bar and changelog grammar · nothing decorative that cannot be copied.

## 04 · Typography

- **Recommended families (Google Fonts):** Display + code: JetBrains Mono, IBM Plex Mono, Geist Mono. Text: IBM Plex Sans, Inter. Never more than one mono family per page.
- **Pairing:** JetBrains Mono 700 (H1–H2, tight tracking) + JetBrains Mono 400/500 (labels, commands, tables of values) + IBM Plex Sans 400/600 (paragraphs, H3).
- **Scale:** H1 56/60 (−0.03em) · H2 36/42 · H3 22/28 (sans) · H4 18/24 · body 16/1.6 · small 14/1.5 · label 12/1 mono uppercase.
- **Body:** 16px sans, line-height 1.6, measure 56–70ch. Code blocks 13–14px mono, line-height 1.7.
- **Uppercase:** mono labels and table headers only (+0.06em). Commands and code keep their real case — never uppercase a command a user will type.
- **CSS:**
```css
h1 { font: 700 56px/1.08 'JetBrains Mono', monospace; letter-spacing: -0.03em; }
body { font: 400 16px/1.6 'IBM Plex Sans', system-ui, sans-serif; }
.label { font: 500 12px/1 'JetBrains Mono', monospace; letter-spacing: .06em; text-transform: uppercase; }
```
- **Typical mistakes:** mono for every paragraph (exhausting); a "hacker" display face with glitch effects; green-on-black body text; mixing two mono families; fake terminal text that is not a real command.

## 05 · Layout & grid

- **Grid:** 12-col, max-width 1200px, 24px gutters; split heads (label + H2 left, explainer right) at 5/7.
- **Spacing:** 8px base; sections 96px apart, separated by a full-width 1px rule rather than background changes.
- **Hero:** Product Screenshot Hero — headline + install command left, a real terminal session or product UI right. The command line is the primary CTA.
- **Frame patterns:** Product Screenshot Hero, Numbered Feature List as joined step cells, Comparison Table, changelog list, status-bar footer.

## 06 · Visual hierarchy

First: the H1 in mono. Second: the install command with its accent-green copy button. Third: the session window, where the eye reads the ✓/▲/✗ column top to bottom. Colour does the ranking — only actions and results are green; everything else is grey on black.

## 07 · Color system

- **Light:** bg #F6F6F3 · surface #ECECE7 · text #0C0E0F · secondary #50575E · border #D3D5D0 · primary #0C0E0F · accent #0B6B33.
- **Dark (native):** bg #0B0D0E · surface #131618 · code #0F1213 · text #E7E9E6 · secondary #949CA3 · border #262B2F · accent #5BE08F · warning #F2B84B · error #FF7A70.
- Accent is reserved for primary actions, success marks and the active state. Warning/error only for real states. Avoid: pure #000 backgrounds, neon gradients, a second accent "for variety", green body text.

## 08 · Components

Buttons: 6px radius, accent fill with near-black label for the primary; outline hairline for secondary; labels in mono lowercase. Command blocks: code-bg panel, `$` prompt in accent, copy button inside. Cards: joined cells sharing hairline borders, not floating tiles. Navbar: 64px, mono links in secondary grey, `kbd` search hint. Inputs: 1px border, mono placeholder, accent focus ring. Tables: hairline rows, mono values, sans labels. Badges: 1px outline mono tags (`new`, `fix`). Modals: surface panel, 8px radius, no shadow — a 1px border separates it. Footer: a status-bar line.

Anatomy and the required state matrix (default / hover / focus-visible / active / disabled / loading / error / success) are universal — see `component-patterns/COMPONENT-PATTERNS.md`. This section defines the *skin*, not the behaviour.

## 09 · Shape language

Radius 4/6/8px. 1px hairlines carry all structure; depth is never expressed with shadows — a surface step (bg → surface → code) is the only elevation. Window chrome is minimal: three outline dots and a title, no glossy traffic lights.

## 10 · Imagery & visual direction

Fits: real terminal sessions, real product UI, diffs, architecture diagrams in line art, logs. Breaks cohesion: stock photography, 3D renders, glowing orbs, "matrix rain", illustrated mascots.

Per-style image direction table: `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md` § 10.

## 11 · Motion

80–240ms, linear-ish ease. Allowed: a blinking block caret (once per page), hover colour shifts, a copy-button state change. Forbidden: typing animations that delay content, scanlines, glitch effects. `prefers-reduced-motion`: caret stops, everything else is already static.

## 12 · Responsive behaviour

Verify at **1440 · 768 · 390** (canonical mobile) and once at **360** (narrow floor). Responsive means recomposition, not stacking — `responsive/RESPONSIVE-FOUNDATIONS.md`.

- **Adaptation:** hero splits stack with the command above the session window; step cells become a vertical list; tables scroll inside their own frame; changelog rows collapse to date-over-text.
- **Non-negotiable for this style:** the install command must stay one tap from the top on mobile, and long code must scroll inside its block — never widen the page.

## 13 · Accessibility

- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every pair in this style's palette.
- Focus states: a 2px accent ring is highly visible on near-black — never remove it for "clean" aesthetics, and make `kbd` hints real shortcuts or drop them.
- Motion: this style is tempted toward typewriter reveals and blinking everything — one caret, and it stops under reduced motion.
- Common a11y failure in this style: mid-grey secondary text (#6B7280-ish) on near-black falling to ~3.5:1; and fake terminal output rendered as an image. Keep secondary ≥ #949CA3 on #0B0D0E, and render sessions as real text with an `aria-label` on the frame.

The universal floor — contrast, focus, keyboard, semantics, motion, touch targets, zoom — is in `accessibility/ACCESSIBILITY.md`. This section covers what *this style specifically* gets wrong.

## 14 · When to use

CLIs, SDKs, APIs, infrastructure and observability tools, AI-agent tooling, developer platforms, open-source project sites, changelogs and status pages. The audience lives in a terminal and evaluates by trying.

## 15 · When NOT to use

Consumer, family or wellness products — it reads cold and exclusionary. Anything where the buyer is not the user (procurement-led enterprise sales) — lead with Minimalism (01) or Swiss (10). Long-form reading. And any product without a real command or real UI to show: the style only works when the content is genuine; without it, it is a costume.

## 16 · Do

- Make the install or run command the primary CTA, copyable
- Show a real session, diff or product screen in the hero
- Use mono for display and data, sans for prose
- Keep one accent, reserved for actions and success
- Separate sections with hairlines, not background bands
- Write labels the way a CLI would (`01 / how it works`)
- Put a changelog or version on the page

## 17 · Don't

- Green-on-black body text
- Glitch, scanline or matrix-rain effects
- Typing animations that hide content
- Fake commands that do not run
- Pure #000 backgrounds with pure #FFF text
- Glossy macOS traffic lights as decoration
- Gradient "AI" orbs behind the terminal

## 18 · Anti-slop — Terminal edition

Slop here is the "hacker aesthetic" costume: neon green on #000, a typewriter that animates `Hello, World!`, a glowing purple orb behind a fake terminal that prints `Deploying AI...`, and three feature cards saying "Fast. Secure. Scalable." The fix is honesty: a real command, a real output, a real changelog date.

**Good vs bad**

- **Good:** a CLI landing page whose hero is the actual install command and a captured session with exit codes — the reader can verify every line.
- **Bad:** a dark template with a fake terminal typing marketing slogans — terminal grammar used as decoration over nothing.

Universal severity levels (BLOCKER / STRONG / MINOR): `ANTI-SLOP.md`.

## 19 · Style combinations

One dominant + at most one supporting style. The supporting style owns exactly one layer — typography, one section type, or micro-motion — never structure.

- **Works with:** Swiss (10) — Swiss owns the grid discipline of docs pages · Bento (04) — one bento section for a feature overview, built from joined hairline cells · Minimalism (01) — restraint on the marketing pages around the docs
- **Avoid pairing with:** Claymorphism (08) — puffy softness contradicts the precision promise · Y2K (13) — chrome nostalgia turns the terminal into a costume · Liquid Glass (03) — refraction over code destroys legibility

Full rules: `STYLE-COMBINATIONS.md`.

## 20 · Signature move

**The command line as the hero CTA** — a single code-bg panel with an accent `$` prompt, the real install command, a blinking block caret and a copy button. It replaces the "Get started" button; the command may return once at the end as the closing CTA.

Use it **once per page**, deliberately. A signature move repeated on every element is no longer a signature.

## 21 · When to break the rules

One human sentence: a single manifesto line set large in the proportional sans, no mono, no code — the moment the page stops sounding like a tool and says why it exists. Everything around it stays strict.

## 22 · Example prompts

Ready-to-paste prompts for Codex, Claude, Lovable and v0: [`prompts.md`](prompts.md)

## 23 · Design tokens

- [`tokens.css`](tokens.css) — **canonical.** If this file and the prose above disagree, the token wins.
- [`tokens.json`](tokens.json) — generated, for design tools and JS
- [`tokens.tailwind.css`](tokens.tailwind.css) — generated, Tailwind v4 `@theme`

Regenerate the two derived files with `python3 scripts/gen_tokens.py` after editing `tokens.css`.

## 24 · Example implementation

[`example.html`](example.html) — a single-file, zero-dependency page built strictly from this style's DNA and tokens. Open it in a browser.

It is **one valid interpretation, not a spec.** Copying it wholesale is how every page ends up identical — read it, then compose something else.
