# Integrations — how to install this into your agent

Every mechanism below is documented by the tool that provides it, and was
checked against that tool's own documentation before being written down here.
Where a convention is a tool's *setting* rather than a fixed filename, that is
stated. **Nothing here is invented.** If your tool is not listed, use the
[Universal](#universal--any-coding-agent) section — it works everywhere.

**Three questions this page answers**

1. Where do I put the repository?
2. Which file do I add so my agent finds it every session?
3. What exactly do I paste?

---

## Step 0 — Get the repository

```bash
git clone https://github.com/aievolutionpl/agent-design-taste.git
```

Three placements, in increasing order of permanence:

| Mode | Where | Best for |
|---|---|---|
| **One-shot** | Nowhere — you paste a prompt with the URL | Trying it once |
| **Project** | `./agent-design-taste/` inside your project | One project, committed with the code |
| **Global** | `~/design/agent-design-taste/` (any stable path) | Every project on your machine |

For **Project** mode, either commit it or add it as a submodule:

```bash
# inside your project
git clone --depth 1 https://github.com/aievolutionpl/agent-design-taste.git
echo "agent-design-taste/" >> .gitignore        # or commit it — your call

# or, to track a pinned version
git submodule add https://github.com/aievolutionpl/agent-design-taste.git
```

Then add the adapter file for your agent (below), and you are done.

---

## Automatic install

From inside your project:

```bash
bash agent-design-taste/scripts/install.sh --agent claude
```

`--agent` accepts `claude`, `codex`, `cursor`, `windsurf`, `copilot`, `gemini`,
`agents` (the universal `AGENTS.md`), or `all`. It copies the matching adapter
into the right location, never overwrites without `--force`, and prints exactly
what it did. `--dry-run` shows the plan without touching anything.

---

## Universal — any coding agent

The single most portable move: put an `AGENTS.md` at your project root.

`AGENTS.md` is an open, vendor-neutral Markdown format — plain Markdown, no
required fields — read by a broad set of coding agents including OpenAI Codex,
GitHub Copilot's coding agent, Cursor, and Windsurf. See <https://agents.md>.

```bash
cp agent-design-taste/adapters/AGENTS.md ./AGENTS.md
```

That file tells any agent where the repository is, which file to read first,
and what not to load. If your project already has an `AGENTS.md`, append the
`## Design` section from the adapter instead of replacing the file.

---

## Claude Code

Claude Code has two mechanisms, and they do different jobs. Use both.

### 1. As a skill (recommended — loads only when relevant)

Claude Code skills live in a folder containing a `SKILL.md` with YAML
frontmatter. Claude sees only the name and description until a task matches,
then loads the body — so a large skill costs almost nothing until it is used.

| Scope | Location |
|---|---|
| Personal (all your projects) | `~/.claude/skills/<name>/SKILL.md` |
| Project (this repo, shared with the team) | `.claude/skills/<name>/SKILL.md` |

This repository's root `SKILL.md` is already a valid Agent Skill. A skill
directory may be a **symlink** to a directory elsewhere on disk — Claude Code
follows it and reads `SKILL.md` from the target — so you can point at your
clone without copying anything:

```bash
# personal: available in every project, always current with `git pull`
ln -s ~/design/agent-design-taste ~/.claude/skills/agent-design-taste

# project: committed with the code, shared with the team
mkdir -p .claude/skills
ln -s ../../agent-design-taste .claude/skills/agent-design-taste
```

Then invoke it directly with `/agent-design-taste`, or let Claude load it
automatically when a UI task matches the description. Claude Code watches skill
directories, so edits are picked up without a restart.

> Committing a symlink works only if everyone's clone sits at the same relative
> path. For a team, prefer a git submodule at `.claude/skills/agent-design-taste`,
> or copy the folder.

### 2. As memory (always in context)

`CLAUDE.md` loads at the start of every session. Keep it small — Anthropic's
guidance is under 200 lines — and use it to point at the skill rather than to
restate it:

```bash
cp agent-design-taste/adapters/CLAUDE.md ./CLAUDE.md
```

CLAUDE.md supports `@path/to/file` imports (recursive, up to four hops), and
Claude Code reads `CLAUDE.md`, **not** `AGENTS.md`. If your project already has
an `AGENTS.md`, the documented bridge is a one-line import:

```markdown
@AGENTS.md

## Claude Code
Design work: read `agent-design-taste/AGENT-BOOTSTRAP.md` before writing UI.
```

### 3. Path-scoped rules (optional)

For a rule that should only load when Claude touches UI files, use
`.claude/rules/` with `paths:` frontmatter:

```markdown
---
paths:
  - "src/**/*.{tsx,jsx,vue,svelte}"
  - "**/*.css"
---
Before changing any UI: read `agent-design-taste/AGENT-BOOTSTRAP.md`.
Never introduce a color, radius or spacing value that is not a token.
```

**Load first:** `AGENT-BOOTSTRAP.md` → `SKILL.md` → one style DNA.

---

## OpenAI Codex

Codex reads `AGENTS.md`. It resolves them from the broadest scope inward —
your Codex home directory (`~/.codex/`), then the git root, then each directory
between the root and your working directory — and concatenates them from the
root down. An `AGENTS.override.md` at any level *replaces* the instructions
above it rather than extending them.

```bash
# project-level
cp agent-design-taste/adapters/AGENTS.md ./AGENTS.md

# global: applies to every project you open with Codex
mkdir -p ~/.codex && cp agent-design-taste/adapters/AGENTS.md ~/.codex/AGENTS.md
```

Note that Codex caps the combined size of these files (32 KiB by default, via
`project_doc_max_bytes`). The adapter is deliberately short for this reason —
it points at the repository rather than inlining it.

**Load first:** `AGENT-BOOTSTRAP.md` → `DECISION-MATRIX.md` → one style DNA.

---

## Cursor

Cursor project rules live in `.cursor/rules/` as `.mdc` files: YAML frontmatter
(`description`, `globs`, `alwaysApply`) followed by Markdown. A plain `.md` file
in that directory is ignored — the extension must be `.mdc`. The older
single-file `.cursorrules` is legacy: still read, but it receives no new
features.

```bash
mkdir -p .cursor/rules
cp agent-design-taste/adapters/cursor/agent-design-taste.mdc .cursor/rules/
```

The adapter is scoped with `globs` so it activates on UI files rather than
loading on every prompt. Cursor also reads `AGENTS.md`, so the universal
adapter works too — the `.mdc` version just gives you glob scoping.

**Load first:** `AGENT-BOOTSTRAP.md` → one style DNA + its `tokens.css`.

---

## Windsurf

Windsurf rules are Markdown files in `.windsurf/rules/` in the project, with a
per-rule activation mode set in the editor. Global rules live in a
`global_rules.md` reachable from the editor's memories panel ("Edit global
rules"). Where both exist, project rules take precedence.

```bash
mkdir -p .windsurf/rules
cp agent-design-taste/adapters/windsurf/agent-design-taste.md .windsurf/rules/
```

Set the rule's activation mode to **Glob** on `*.tsx, *.jsx, *.vue, *.svelte,
*.css` for UI-only loading, or **Always On** if the project is UI-heavy.

**Load first:** `AGENT-BOOTSTRAP.md` → `ANTI-SLOP.md` → one style DNA.

---

## GitHub Copilot

Copilot's coding agent supports several instruction formats at once:
`.github/copilot-instructions.md` for repository-wide instructions,
`.github/instructions/**/*.instructions.md` for path-specific ones, and
`AGENTS.md`, `CLAUDE.md` or `GEMINI.md` agent-instruction files.

```bash
mkdir -p .github
cp agent-design-taste/adapters/copilot/copilot-instructions.md .github/
```

For UI-only scoping, use a path-specific file instead —
`.github/instructions/ui.instructions.md` with an `applyTo` glob in its
frontmatter. If you already keep an `AGENTS.md`, Copilot reads that and you do
not need a second file.

**Load first:** `AGENT-BOOTSTRAP.md` → `ANTI-SLOP.md`.

---

## Gemini CLI

Gemini CLI loads context files hierarchically: a global `~/.gemini/GEMINI.md`,
then `GEMINI.md` files found walking up from your working directory, then
component-level files in subdirectories. All of them are concatenated into the
prompt.

```bash
cp agent-design-taste/adapters/GEMINI.md ./GEMINI.md
# or globally
mkdir -p ~/.gemini && cp agent-design-taste/adapters/GEMINI.md ~/.gemini/GEMINI.md
```

The filename is configurable: set `context.fileName` in `.gemini/settings.json`
to `"AGENTS.md"` (or a list of accepted names) and Gemini CLI loads those files
through the same hierarchy — useful if you would rather keep one `AGENTS.md`:

```json
{ "context": { "fileName": ["AGENTS.md", "GEMINI.md"] } }
```

Use `/memory show` to confirm what was loaded.

**Load first:** `AGENT-BOOTSTRAP.md` → `DECISION-MATRIX.md`.

---

## Lovable

Lovable is a browser builder with no filesystem, so there is nothing to clone.
It has a **Knowledge** field in project settings that is prepended to every
prompt — that is where the design contract goes.

1. **Project settings → Knowledge.** Paste your `DESIGN.md` contract there
   (`prompts/DESIGN-CONTRACT.md` has the template). The field holds up to
   10,000 characters, so paste the *contract*, not the repository.
2. In chat, iterate **per section**, not whole pages at once.
3. Keep the anti-slop block in every substantial prompt —
   `prompts/PROMPT-LIBRARY.md § Universal anti-slop prompt block`.

Style-specific prompts written for Lovable are in each
`styles/<style>/prompts.md`.

---

## v0

v0 generates React with Tailwind and shadcn/ui by default, which means its
defaults will fight your tokens unless you override them explicitly.

1. Paste `styles/<style>/tokens.tailwind.css` into your prompt or project so
   the theme variables exist.
2. **Explicitly override the shadcn defaults** for radius, shadow and font —
   they are the strongest source of "every v0 app looks the same".
3. v0 supports custom instructions in its settings and can import a design
   system; put the durable constraints there rather than repeating them.
4. Use the v0 entry in `styles/<style>/prompts.md` as the starting prompt.

---

## Other agents (Aider, Devin, Zed, Warp, Amp, Jules, Factory…)

Use `AGENTS.md`. It is the format these tools converged on precisely so this
question has one answer.

```bash
cp agent-design-taste/adapters/AGENTS.md ./AGENTS.md
```

---

## Updating

```bash
cd agent-design-taste && git pull
```

- **Symlinked Claude Code skill** — picked up automatically.
- **Submodule** — `git submodule update --remote`.
- **Copied adapter files** — re-run `scripts/install.sh --force`, or diff the
  adapter against your copy.
- Breaking changes are listed in [`CHANGELOG.md`](../CHANGELOG.md). The skill
  follows semantic versioning; the current version is in `SKILL.md` frontmatter
  and in `design-taste.manifest.json`.

---

## Verifying it worked

Ask your agent, without any other context:

> "What is the first file you read before changing UI in this project, and what
> are the canonical viewports?"

A correct answer names `AGENT-BOOTSTRAP.md` (or `SKILL.md`) and
**1440 / 768 / 390**, with 390 as the primary mobile check. If it does not,
the instruction file is not loading — check the tool's own diagnostic
(`/context` in Claude Code, `/memory show` in Gemini CLI, the rules panel in
Cursor or Windsurf).
