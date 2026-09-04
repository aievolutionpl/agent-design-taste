# Component Patterns

**Anatomy is fixed. Style changes the skin.** A button is a label, a hit area,
and six states in every design language ever made. What changes between Swiss
and Claymorphism is radius, shadow, weight and motion — never whether focus is
visible.

This file defines anatomy and states. The style DNA defines appearance.

---

## The state matrix

Every interactive component owes eight states. A component shipped with only
`default` is unfinished, not minimal.

| State | Required when | Rule |
|---|---|---|
| `default` | always | The resting appearance |
| `hover` | pointer devices | 150–250ms, color or transform — never layout |
| `focus-visible` | always | **Non-negotiable.** Visible ring ≥2px, ≥3:1 against both the component and the page |
| `active` / pressed | always | Immediate (≤100ms). Confirms the tap landed |
| `disabled` | when the action can be unavailable | Reduced contrast **plus** `aria-disabled`; explain *why* nearby |
| `loading` | any async action | In place, preserving width — never a layout jump |
| `error` | any input or async action | Color **plus** icon **plus** text. Never color alone |
| `success` | destructive or slow actions | Brief, then return to rest |

Plus three content states for anything that renders data:
**empty** (with a next action), **partial** (skeleton, not a spinner), and
**overflow** (long strings, 40 items, one item).

---

## 1 · Navigation

**Anatomy** logo · destinations (≤6) · optional utility cluster · one CTA
**States** scrolled (elevation or border appears) · active destination · focus
**Mobile** overlay or drawer (≤7 items) or bottom tab bar (≤5 items). The
primary CTA stays reachable without opening the menu.
**a11y** `<nav>` landmark · skip link to `<main>` · `aria-current="page"` ·
focus trap while an overlay is open, ESC closes, focus returns to the trigger.
**Style shifts** Swiss: hairline border, no shadow, 0 radius · Clay: puffy pill
nav, chunky spacing · Editorial: serif wordmark, links as underlined text ·
Brutalist: 3px black border, hard offset shadow.

## 2 · Hero

**Anatomy** eyebrow (optional) · H1 · sub (≤2 lines) · primary CTA · optional
secondary · supporting visual
**Rules** exactly one H1 · one primary action · the sub explains, it does not
repeat the headline
**Mobile** the visual is *re-cropped*, not scaled. H1 drops ~30–40%.
**a11y** decorative hero art is `alt=""`; if the image carries the message, the
message must also be in text.

## 3 · Buttons

**Anatomy** label ± icon · hit area ≥44×44px including padding · radius from tokens
**Hierarchy** one primary per view · secondary is outline or ghost · tertiary is
a link. Three visually equal buttons means no primary.
**Labels** verb + noun. "Delete project", never "OK". "Start free trial", never
"Submit".
**Loading** replace the label with a spinner *at the same width*; keep the
accessible name.
**a11y** a real `<button>` (or `<a>` for navigation) · icon-only needs
`aria-label` · never remove the focus ring without replacing it.
**Style shifts** Minimalism: solid, 8–12px radius, no shadow · Neo-Brutalism:
0 radius, 3px border, 4px hard offset shadow that collapses on press ·
Clay: 24px radius, inset bottom shadow, spring press · Swiss: sharp, 0 radius,
uppercase label at 12px.

## 4 · Forms and inputs

**Anatomy** label *above* the field · field · helper text slot · error slot
**Rules** placeholder is never the label · required marked in text, not only
with `*` · validate on blur, not on every keystroke · never disable submit
without saying what is missing
**Errors** icon + text + color. The message says how to fix it, not that
something is wrong.
**Mobile** correct `type` and `autocomplete` (drives the right keyboard) ·
fields ≥44px tall · font-size ≥16px or iOS zooms on focus
**a11y** `<label for>` · `aria-describedby` linking helper and error ·
`aria-invalid` on failure · errors announced, not only rendered.

## 5 · Cards

**Anatomy** container · optional media · body · optional actions
**Rules** a card groups *comparable* objects. If the page has one card, it is a
section — remove the container. Elevation is semantic: same level, same shadow.
**Whole-card links** wrap in a single link or use a pseudo-element overlay;
never nest interactive elements inside an interactive card.
**Mobile** full-bleed or edge-padded, never a 320px card inside a 390px viewport
with 35px of dead margin.
**a11y** hover-only affordances must also appear on focus.

## 6 · Pricing

**Anatomy** plan name · price + period · one-line positioning · feature list ·
CTA · optional annual toggle
**Rules** the recommended plan is anchored by **size, border or elevation** —
not only by a badge. Test it in grayscale: if the recommendation disappears, it
was never anchored.
**Mobile** recommended plan **first**, then the rest.
**a11y** the toggle is a real control with a label; announce the price change.

## 7 · Tables

**Anatomy** header row · body rows · optional footer/summary
**Rules** zebra striping **or** row lines, never both · numeric columns
right-aligned in a tabular-figure face · sortable headers show direction ·
sticky header on long tables
**Mobile** the hardest component. Choose one: (a) one card per row, (b) sticky
first column with horizontal scroll *inside the table container*, (c) fewer
columns with a detail view. Never a shrunken desktop table.
**States** empty (say what would appear here), loading (skeleton rows),
error, and a single-row case.
**a11y** real `<table>` · `<th scope>` · `<caption>` · scroll container gets
`tabindex="0"` and an accessible name so keyboard users can scroll it.

## 8 · Modals and dialogs

**Anatomy** scrim · panel · title · body · actions · close
**Rules** ESC closes · click-outside closes (unless data would be lost) ·
focus moves in on open and returns to the trigger on close · body scroll locked
**Mobile** bottom sheet ≥ centered modal. Respect safe-area insets.
**a11y** `<dialog>` or `role="dialog"` + `aria-modal="true"` + `aria-labelledby`
· focus trap while open · the close control has an accessible name.

## 9 · Sidebars

**Anatomy** brand · primary nav · optional secondary group · account/footer
**Rules** ≤7 primary items · collapsed state keeps icons *and* tooltips ·
active item marked by more than color
**Mobile** drawer or bottom tabs. Never a persistent sidebar under 768px.
**a11y** `<nav>` with an accessible name · `aria-current` on the active item.

## 10 · Dashboards and widgets

**Anatomy** title · value · delta · optional sparkline · optional timeframe
**Rules** the delta needs a direction *and* a comparison period · one metric per
widget · a number without a unit or a period is decoration
**States** loading skeleton (not a spinner), empty ("no data for this period"),
error (with retry), stale (last-updated timestamp)
**Mobile** priority order, not grid order. The top three metrics, then the rest.
**a11y** never encode change by color alone: `↑ 12%` beats a green number.

## 11 · Tabs

**Anatomy** tablist · tabs · panels · visible active indicator
**Rules** ≤6 tabs · never nest tab sets · content must not shift height wildly
between tabs
**Mobile** horizontal scroller with a peeking edge, or a `<select>`.
**a11y** `role="tablist"` / `tab` / `tabpanel` · arrow-key navigation ·
`aria-selected` · panel labelled by its tab.

## 12 · Tooltips

**Rules** 300ms show delay, instant hide · ≤2 lines · never the only source of
information · never contains interactive content (use a popover)
**Touch** there is no hover. On touch, tooltip content must be reachable another
way — tap-toggle, or inline helper text.
**a11y** `aria-describedby` on the trigger · dismissible with ESC · must remain
visible while the pointer travels to it.

## 13 · Badges and status

**Rules** semantic colors (info / success / warning / error) from tokens ·
readable in both themes · **never color alone** — pair with a label or icon
**Sizing** the badge never dictates row height.

## 14 · Empty states

The most neglected component and often the first thing a new user sees.

**Anatomy** short heading · one sentence explaining what would appear here ·
one primary action · optional illustration
**Rules** never a lone spinner or a shrug emoji · the action is the *next real
step*, not "Refresh" · differentiate "nothing yet" from "nothing matched your
filter" — they need different actions.

## 15 · Command palette

**Anatomy** trigger (⌘K + a visible button) · input · grouped results ·
keyboard hints · empty state
**Rules** results grouped and ranked · recent items first when the query is
empty · every action reachable another way — a palette is an accelerator, not
the only path
**a11y** combobox pattern: `aria-expanded`, `aria-activedescendant`, results in
a listbox, ESC closes and returns focus.

## 16 · Onboarding

**Rules** show progress and total steps · every step skippable or reversible ·
never more than 3–4 steps before first value · save partial progress
**a11y** focus moves to the new step's heading on advance; progress announced.

## 17 · Search

**Anatomy** input · optional scope selector · results · empty state · clear button
**Rules** debounce ~200–300ms · show what is being searched · zero-results
suggests corrections or a broader scope · preserve the query on back-navigation
**a11y** `role="search"` landmark · result count announced via `aria-live="polite"`.

## 18 · Filters

**Rules** show applied filters as removable chips · always offer "clear all" ·
show the result count before and after · never lose scroll position on apply
**Mobile** bottom sheet with an applied-count badge on the trigger.
**a11y** announce the new result count; group related filters with `<fieldset>`
and `<legend>`.

## 19 · Mobile navigation

**Bottom tabs** ≤5 items · icon **and** label · active state beyond color ·
respect the safe-area inset
**Drawer** ≤7 items · swipe *and* button dismiss · focus trap while open
**Rules** the primary action does not hide behind a hamburger. Thumb reach
matters: destructive actions do not belong in the easiest zone.

---

## Rules that apply to every component

1. Anatomy is fixed; the style changes the skin only.
2. Every interactive element has a visible `:focus-visible` style.
3. Error states never rely on color alone — icon plus text, always.
4. Icon + label beats icon-only. Icon-only requires `aria-label`.
5. Radius, spacing, shadow and duration come from tokens. A hard-coded `13px`
   means either the token is missing or the value is wrong.
6. Hover-only information is invisible on touch. It must also appear on focus.
7. The same component looks the same everywhere on the site. Two button styles
   for the same action is a consistency failure, not a variant.
