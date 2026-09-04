<div align="center">

<img src="assets/banner.png" alt="Agent Design Taste" width="100%">

# Agent Design Taste

### Inteligencja projektowa dla agentów AI

**Naucz swojego agenta *jak projektować* — nie tylko jak kodować.**

[![Licencja: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Skill v2.0.0](https://img.shields.io/badge/skill-v2.0.0-black.svg)](SKILL.md)
[![15 stylów](https://img.shields.io/badge/style-15-black.svg)](#15-stylów)
[![validate](https://github.com/aievolutionpl/agent-design-taste/actions/workflows/validate.yml/badge.svg)](https://github.com/aievolutionpl/agent-design-taste/actions/workflows/validate.yml)

[English](README.md) · **Polski**

[Instalacja](#instalacja) · [Dla agentów AI](#dla-agentów-ai) · [Workflow](#workflow) · [15 stylów](#15-stylów) · [Integracje](docs/INTEGRATIONS.md)

</div>

> **Uwaga:** dokumentacja techniczna repozytorium (`SKILL.md`, `DECISION-MATRIX.md`,
> style, oceny) jest w języku angielskim — to język, w którym agenci pracują
> najpewniej. Ten plik to pełne wprowadzenie po polsku.

---

## Po co to istnieje

Agenci AI budują działające aplikacje w kilka minut. I każda wygląda tak samo:

> fioletowy gradient · szklane karty · wszędzie ten sam promień 24px · Inter w
> każdym rozmiarze · trzy identyczne karty funkcji · pływająca bryła 3D ·
> „Trusted by 50,000+ teams" · wszystko wycentrowane · widok mobilny to po
> prostu desktop poskładany w pionie

To nie jest problem umiejętności. To **problem wiedzy**: nikt nie dał agentowi
systemu projektowego ani sposobu podejmowania decyzji. Sięga więc po
statystycznie najczęstszy wzorzec — i dokładnie dlatego wynik wygląda na
wygenerowany.

To repozytorium daje agentowi jedno i drugie: prawdziwy system projektowy oraz
proces wybierania wewnątrz niego.

**Procesem jest produkt:**

```
Produkt → Odbiorca → Styl → Layout → Tokeny → Render → Krytyka → Poprawa
```

Piętnaście bibliotek stylów to łatwiejsza połowa. Ta, która naprawdę się liczy,
to nauczenie agenta, żeby *obserwował, decydował i potrafił obronić decyzję*.

<div align="center">

⭐ **Jeśli to poprawia UI twojego agenta — zostaw gwiazdkę**, żeby trafiło do
większej liczby osób.

</div>

---

## Instalacja

Sklonuj repozytorium, potem dodaj jeden plik, żeby agent znajdował je w każdej sesji.

```bash
git clone https://github.com/aievolutionpl/agent-design-taste.git
```

<table>
<tr><th width="33%">Jednorazowo</th><th width="33%">W projekcie</th><th width="33%">Globalnie</th></tr>
<tr valign="top">
<td>Chcesz spróbować raz. Nic nie instalujesz — wklejasz prompt.</td>
<td>Jeden projekt. Leży obok kodu, commitowane razem z nim.</td>
<td>Każdy projekt na twojej maszynie.</td>
</tr>
</table>

### A · Jednorazowo — wklej ten prompt

Bez instalacji. Działa w Claude Code, Codex, Cursor, ChatGPT — wszędzie.

```text
Użyj systemu Agent Design Taste: https://github.com/aievolutionpl/agent-design-taste

Przeczytaj najpierw AGENT-BOOTSTRAP.md, potem SKILL.md. Zanim napiszesz jakikolwiek UI:

1. Wypisz odbiorcę, typ produktu, osobowość marki, gęstość treści,
   główną akcję i emocję docelową — na piśmie.
2. Użyj DECISION-MATRIX.md, żeby wybrać JEDEN styl dominujący (plus maksymalnie
   jeden wspierający), i powiedz, dlaczego drugi w kolejności przegrywa.
3. Wczytaj TYLKO README.md i tokens.css tego stylu. Nie ładuj wszystkich 15.
4. Jeśli projekt ma już system projektowy, zastosuj docs/PRECEDENCE.md:
   przeanalizuj go, zmapuj się do niego, zaadaptuj — nigdy nie przemalowuj.
5. Buduj z tokenów. Każdy kolor, odstęp, promień i czas trwania to token.
6. Wyrenderuj w 1440 / 768 / 390 i spójrz na to. Przegląd kodu to nie
   przegląd wizualny.
7. Zrób audyt: ANTI-SLOP.md (zero BLOCKERÓW) i evaluation/DESIGN-TASTE-SCORE.md
   (wynik 75+), popraw dwa najsłabsze obszary, wyrenderuj ponownie, dopiero
   wtedy oddaj.
```

### B · Instalacja w projekcie

```bash
cd twoj-projekt
git clone --depth 1 https://github.com/aievolutionpl/agent-design-taste.git
bash agent-design-taste/scripts/install.sh --agent claude   # albo codex, cursor,
                                                            # windsurf, copilot,
                                                            # gemini, agents, all
```

```
twoj-projekt/
├── agent-design-taste/     ← system
├── CLAUDE.md               ← pisze instalator: kieruje agenta do systemu
├── DESIGN.md               ← pisze agent: kontrakt wizualny twojego projektu
└── src/
```

Instalator nigdy nie nadpisuje bez `--force`, a `--dry-run` pokazuje plan.

### C · Instalacja globalna

Jeden klon, używany wszędzie.

```bash
git clone https://github.com/aievolutionpl/agent-design-taste.git ~/design/agent-design-taste

# Claude Code — katalog skilla może być dowiązaniem; ładuje się tylko gdy trzeba
ln -s ~/design/agent-design-taste ~/.claude/skills/agent-design-taste

# Codex — obowiązuje w każdym otwieranym projekcie
cp ~/design/agent-design-taste/adapters/AGENTS.md ~/.codex/AGENTS.md

# Gemini CLI
cp ~/design/agent-design-taste/adapters/GEMINI.md ~/.gemini/GEMINI.md
```

`git pull` aktualizuje wszystkie projekty naraz.

> **Konfiguracja per narzędzie — Claude Code, Codex, Cursor, Windsurf, GitHub
> Copilot, Gemini CLI, Lovable, v0 — z dokładnymi ścieżkami, które każde z nich
> dokumentuje: [`docs/INTEGRATIONS.md`](docs/INTEGRATIONS.md)**

**Sprawdź, czy działa.** Zapytaj agenta, bez żadnego innego kontekstu: *„Jaki
plik czytasz jako pierwszy przed zmianą UI w tym projekcie i jakie są
kanoniczne viewporty?"* Poprawna odpowiedź: `AGENT-BOOTSTRAP.md` oraz
**1440 / 768 / 390**.

---

## Dla agentów AI

**Jeśli jesteś agentem AI czytającym to repozytorium — ta sekcja jest dla ciebie.**

1. **Nie generuj jeszcze UI.**
2. Przeczytaj [`AGENT-BOOTSTRAP.md`](AGENT-BOOTSTRAP.md) — 75 linii, potem
   [`SKILL.md`](SKILL.md).
3. Ustal **tryb** (projektowanie / budowa / przegląd / dopracowanie) i **profil
   kontekstu** (LIGHT / STANDARD / FULL) →
   [`docs/CONTEXT-PROFILES.md`](docs/CONTEXT-PROFILES.md).
4. Przeanalizuj istniejący projekt, zanim cokolwiek zmienisz. Jeśli ma system
   projektowy, wykonaj ANALYZE → MAP → ADAPT →
   [`docs/PRECEDENCE.md`](docs/PRECEDENCE.md).
5. **Zachowaj ograniczenia marki.** Tokeny stylów to domyślne wartości dla
   nowych projektów, a nie zgoda na przemalowanie cudzego produktu.
6. Wybierz **jeden** styl dominujący przez
   [`DECISION-MATRIX.md`](DECISION-MATRIX.md). Powiedz, dlaczego drugi w
   kolejności przegrywa.
7. **Ładuj tylko to, czego potrzebujesz.** Jedno DNA stylu to ~2,7 tys. tokenów.
   Wszystkie piętnaście to ~41 tys. — a czternaście odrzuconych stylów w
   kontekście *pogarsza* twój wynik.
8. Buduj z tokenów. Każda wartość jest tokenem.
9. **Renderuj** w 1440 / 768 / 390 i patrz na wynik —
   `node scripts/screenshot.mjs <url-lub-plik>` robi wszystkie cztery viewporty
   i kończy błędem przy przewijaniu poziomym na mobile.
10. **Oceń** przez [`evaluation/DESIGN-TASTE-SCORE.md`](evaluation/DESIGN-TASTE-SCORE.md).
11. **Usuń slop** przez [`ANTI-SLOP.md`](ANTI-SLOP.md). Zero 🔴 BLOCKERÓW.
12. **Iteruj**, dopiero potem oddaj.

Routing maszynowy, bez parsowania prozy:
[`design-taste.manifest.json`](design-taste.manifest.json) ·
[`styles/index.json`](styles/index.json)

---

## Workflow

```
        ZROZUM              odbiorca · produkt · osobowość · gęstość · emocja
             │
       WYBIERZ STYL         punktacja ważona, bramki weta, i dlaczego nie inne
             │
        TYPOGRAFIA          role przed krojami — uzasadnione jednym zdaniem
             │
          LAYOUT            nazwany wzorzec, nie znowu to samo hero
             │
          TOKENY            rozstrzygnięte przez precedencję, zapisane w DESIGN.md
             │
          BUDUJ             najpierw ograniczenia: każda wartość to token
             │
        RENDERUJ            1440 · 768 · 390 — w prawdziwej przeglądarce, oczami
             │
          AUDYT             13 ważonych kategorii, 8 twardych blokerów
             │
      USUŃ AI SLOP          BLOCKER · STRONG SMELL · MINOR SMELL
             │
        DOPRACUJ            rytm · stany focus · reduced motion · prawdziwe treści
```

Pominięcie ZROZUM, WYBIERZ, RENDERUJ albo USUŃ SLOP to porażka — nawet jeśli
wynik wygląda dobrze. **„Wygląda dobrze" i „jest zaprojektowane" to dwie różne
rzeczy.**

Zobacz cały proces na jednym briefie:
[`docs/EXAMPLE-WORKFLOW.md`](docs/EXAMPLE-WORKFLOW.md)

---

## 15 stylów

<img src="assets/styles-overview.png" alt="15 stylów projektowych w tej bibliotece" width="100%">

| # | Styl | Tożsamość | Najlepszy do | Gęstość |
|---|---|---|---|---|
| 01 | [Minimalism](styles/01-minimalism/) | Mniej, ale lepiej | B2B SaaS, fintech, premium | niska–śr. |
| 02 | [Glassmorphism](styles/02-glassmorphism/) | Przezroczyste. Warstwowe. | Narzędzia dev, dashboardy | niska–śr. |
| 03 | [Liquid Glass](styles/03-liquid-glass/) | Płynne światło i ruch | Aplikacje konsumenckie i kreatywne | niska–śr. |
| 04 | [Bento Grid](styles/04-bento-grid/) | Modularne, uporządkowane bloki | Produkty bogate w funkcje | śr.–wys. |
| 05 | [Neo-Brutalism](styles/05-neo-brutalism/) | Odważny, surowy, nieoczywisty | Marki młodzieżowe, narzędzia twórców | niska–śr. |
| 06 | [Brutalist / Anti-Grid](styles/06-brutalist-anti-grid/) | Łam siatkę celowo | Portfolia, agencje, sztuka | niska |
| 07 | [Neumorphism](styles/07-neumorphism/) | Miękkie wytłoczone powierzchnie | Tylko powierzchnie dekoracyjne ⚠️ | niska |
| 08 | [Claymorphism](styles/08-claymorphism/) | Radosne, puszyste 3D | Dzieci, edukacja, wellness | niska–śr. |
| 09 | [Skeuomorphism](styles/09-skeuomorphism-tactile/) | Wygląda jak rzecz prawdziwa | Audio, instrumenty, finanse | śr.–wys. |
| 10 | [Swiss / International](styles/10-swiss-international/) | Siatka, typografia, porządek | Narzędzia dev, dane, korporacje | śr.–wys. |
| 11 | [Editorial / Magazine](styles/11-editorial-magazine/) | Czyta się jak magazyn | Media, długie formy, luksus | śr.–wys. |
| 12 | [Maximalism](styles/12-maximalism/) | Więcej znaczy więcej | Moda, wydarzenia, kultura | wysoka |
| 13 | [Y2K / Retrofuturism](styles/13-y2k-retrofuturism/) | Chrom, bańka, optymizm | Muzyka, streetwear, gaming | śr.–wys. |
| 14 | [3D / Spatial UI](styles/14-3d-spatial-ui/) | Głębia, przez którą się przechodzi | Web3, premiery, immersja | niska–śr. |
| 15 | [Kinetic Typography](styles/15-expressive-kinetic-typography/) | Typografia jako interfejs | Portfolia, kampanie | niska |

[**Galeria podglądów wszystkich 15 stron przykładowych**](docs/index.html) — otwórz
lokalnie albo opublikuj, włączając GitHub Pages dla tego repozytorium
(*Settings → Pages → main / `docs`*), co udostępni ją pod adresem
`https://aievolutionpl.github.io/agent-design-taste/`.

### Co jest w każdym folderze stylu

Nie moodboard. Kompletny, samowystarczalny brief projektowy:

```
styles/10-swiss-international/
├── README.md              Design DNA w 24 sekcjach — filozofia, typografia,
│                          siatka, kolor, komponenty, motion, RWD, dostępność,
│                          kiedy NIE używać, do/don't, anti-slop, ruch firmowy
├── tokens.css             kanoniczne design tokens (jasny + ciemny)
├── tokens.json            te same tokeny dla narzędzi projektowych i JS
├── tokens.tailwind.css    te same tokeny jako blok @theme w Tailwind v4
├── prompts.md             gotowe prompty dla Codex / Claude / Lovable / v0
└── example.html           działająca strona, jeden plik, zero zależności
```

`tokens.css` to źródło prawdy; pozostałe dwa są z niego generowane i sprawdzane
w CI. **Jeśli tekst i token się nie zgadzają — wygrywa token.**

---

## Czym to się różni od biblioteki promptów

<table>
<tr><th width="50%">Biblioteka promptów daje ci</th><th width="50%">To daje twojemu agentowi</th></tr>
<tr valign="top"><td>

Tekst do wklejenia

</td><td>

**Proces decyzyjny** z bramkami weta i punktacją ważoną

</td></tr>
<tr valign="top"><td>

Styl — o ile już wiesz, którego chcesz

</td><td>

**Powód** wyboru stylu — i argument przeciw drugiemu w kolejności

</td></tr>
<tr valign="top"><td>

Wszystko, za każdym razem

</td><td>

**Routing kontekstu** — LIGHT / STANDARD / FULL, jedno DNA naraz

</td></tr>
<tr valign="top"><td>

Wynik

</td><td>

Wynik **wyrenderowany, oceniony, oczyszczony ze slopu i poprawiony**

</td></tr>
<tr valign="top"><td>

To, co model ma domyślnie

</td><td>

Jawny **łańcuch precedencji**, który chroni istniejącą markę

</td></tr>
</table>

### Precedencja — reguła, która chroni twoją markę

```
marka i prawo ▸ dostępność ▸ potrzeby produktu ▸ DNA stylu ▸ tokeny repo ▸ gust agenta
```

Tokeny stylów to **domyślne wartości dla nowych projektów**. Gdy projekt ma już
system projektowy, agent go analizuje, mapuje się do niego i adaptuje — nie
przemalowuje go. A gdy kolor marki nie spełnia kontrastu, odpowiedzią jest
zachowanie marki i wyprowadzenie dostępnego wariantu z tej samej rodziny
odcieni — nie podmiana marki i nie wysłanie tekstu, którego nie da się
przeczytać.

→ [`docs/PRECEDENCE.md`](docs/PRECEDENCE.md)

---

## Mapa repozytorium

<details>
<summary><b>Wszystko i kiedy to ładować</b></summary>

```
AGENT-BOOTSTRAP.md         punkt wejścia — 10 kroków i czego NIE ładować
SKILL.md                   workflow, twarde reguły, priorytet wiedzy
DECISION-MATRIX.md         11 sygnałów → bramki weta → punktacja ważona
STYLE-COMBINATIONS.md      bezpieczne i niebezpieczne połączenia stylów
LAYOUT-PATTERNS.md         43 wzorce jako biblioteka decyzyjna
ANTI-SLOP.md               BLOCKER / STRONG SMELL / MINOR SMELL

docs/
  PRECEDENCE.md            rozstrzyganie konfliktów · ANALYZE → MAP → ADAPT
  CONTEXT-PROFILES.md      LIGHT / STANDARD / FULL, ze zmierzonym kosztem
  INTEGRATIONS.md          instalacja per agent, zweryfikowana z dokumentacją
  EXAMPLE-WORKFLOW.md      jeden brief, przeprowadzony od początku do końca
  STYLE-TEMPLATE.md        wymagana struktura dla stylu #16

styles/
  NN-nazwa/                15 samowystarczalnych Design DNA
  index.json               routing maszynowy: id, aliasy, punktacja, weta

accessibility/             podłoga dostępności + błędy typowe dla każdego stylu
responsive/                drabina viewportów; rekompozycja, nie układanie w stos
typography/                role, sygnały, metryki, wsparcie językowe, wydajność
visual-language/           fotografia, 3D, ikony, tekstura, kierunek artystyczny
motion/                    budżety czasu, easing, reduced-motion
component-patterns/        19 komponentów × 8 stanów interakcji
layout-patterns/           siatki, skala odstępów, anatomia sekcji
design-tokens/             kategorie tokenów, nazewnictwo, formaty

evaluation/
  DESIGN-TASTE-SCORE.md    13 ważonych kategorii + 8 twardych blokerów
  RENDERED-VERIFICATION.md przegląd kodu to nie przegląd wizualny
  MODE-ROUTING.md          czasownik → tryb → wycinek wiedzy
  TASTE-LOOP.md            uczenie preferencji między sesjami

prompts/
  DESIGN-CONTRACT.md       wzorzec DESIGN.md
  PROMPT-LIBRARY.md        szkielety promptów oparte na ograniczeniach

adapters/                  pliki do skopiowania dla każdego agenta
scripts/                   gen_tokens · gen_manifest · validate · install
design-taste.manifest.json manifest repozytorium czytelny maszynowo
```

</details>

<details>
<summary><b>Koszt kontekstu — dlaczego agent nie może ładować wszystkiego</b></summary>

| Ładujesz | ~tokenów |
|---|---|
| `AGENT-BOOTSTRAP.md` | 0,8 tys. |
| Profil LIGHT — poprawka komponentu | ~3 tys. |
| Profil STANDARD — landing page | ~8 tys. |
| Profil FULL — cały produkt | ~25 tys. |
| Jedno DNA stylu | ~2,7 tys. |
| **Wszystkie 15 DNA stylów** | **~41 tys.** ← nigdy |
| Całe repozytorium | ~101 tys. |

Zmierz sam: `python3 scripts/validate.py --budget`

DNA stylu określa już kroje, skalę, layout, kolor, komponenty, motion,
dostępność i reguły anti-slop. **Jeden styl to kompletny brief. Piętnaście to
szum z briefem gdzieś w środku.**

</details>

<details>
<summary><b>Współpraca i walidacja</b></summary>

```bash
python3 scripts/validate.py          # pełna kontrola strukturalna — to samo co CI
python3 scripts/validate.py --budget # zmierzony koszt kontekstu per plik
python3 scripts/gen_tokens.py        # regeneruje tokens.json + tokens.tailwind.css
python3 scripts/gen_manifest.py      # regeneruje styles/index.json + manifest
node    scripts/screenshot.mjs 10    # renderuje styl w 1440/768/390/360
```

CI sprawdza, czy każdy folder stylu jest kompletny, czy istnieją wszystkie
wymagane kategorie tokenów (w tym `--shadow-focus`), czy każdy link wewnętrzny
działa, czy każdy `example.html` się parsuje, czy wszystkie 15 DNA ma tę samą
24-sekcyjną strukturę i czy pliki generowane są zgodne ze źródłem.

Dodajesz styl #16? [`CONTRIBUTING.md`](CONTRIBUTING.md) i
[`docs/STYLE-TEMPLATE.md`](docs/STYLE-TEMPLATE.md) mają pełną listę kontrolną.
Sekcja, którą recenzenci czytają pierwszą, to **„When NOT to use"** — styl bez
uczciwie opisanego trybu porażki nie został przemyślany.

</details>

---

## Zasady

- Każdy folder stylu musi odpowiadać na pytanie **kiedy NIE używać tego stylu**.
- **Tokeny są kanoniczne.** Jeśli `README.md` i `tokens.css` się nie zgadzają,
  wygrywa token, a README jest błędem do zgłoszenia.
- Strony przykładowe to pojedyncze pliki HTML, zero zależności, otwierasz w
  przeglądarce.
- Prompty to sprawdzone wzorce, nie życzenia — zwięzłe, oparte na ograniczeniach.
- Żadnych niepopartych twierdzeń: bez zmyślonych cytowań, bez niezweryfikowanych
  integracji, bez statystyk bez źródła. Ta reguła dotyczy również tego repozytorium.

---

<div align="center">

## Zbudowane przez AI Evolution Polska + AI Evolution Labs

**[AI Evolution Polska](https://www.aievolutionpolska.pl/)** — praktyczna
edukacja AI, workflow, agenci i automatyzacja.
**AI Evolution Labs** — produkty AI, automatyzacja i technologia kreatywna.

[![GitHub](https://img.shields.io/badge/GitHub-@aievolutionpl-black?logo=github)](https://github.com/aievolutionpl)

---

Jeśli Agent Design Taste pomógł twojemu agentowi budować lepsze interfejsy:

⭐ **Zostaw gwiazdkę** &nbsp;·&nbsp; 🤝 **[Wkład mile widziany](CONTRIBUTING.md)** &nbsp;·&nbsp; 🐛 **[Zgłoś issue](https://github.com/aievolutionpl/agent-design-taste/issues)**

<sub>MIT © AI Evolution Polska / AI Evolution Labs · Baner i grafika przeglądowa
stylów powyżej zostały wygenerowane przez naszego agenta AI — zaprojektowane
przez agenta, dla agentów.</sub>

</div>
