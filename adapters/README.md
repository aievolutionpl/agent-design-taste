# Adapters

Copy-paste-ready instruction files that point your coding agent at this
repository. Each targets a convention documented by the tool that reads it —
see [`../docs/INTEGRATIONS.md`](../docs/INTEGRATIONS.md) for the details and
the sources.

| File | Copy to | Read by |
|---|---|---|
| `AGENTS.md` | `./AGENTS.md` (or `~/.codex/AGENTS.md`) | Codex, Copilot coding agent, Cursor, Windsurf and other agents that read the open `AGENTS.md` format |
| `CLAUDE.md` | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Claude Code |
| `GEMINI.md` | `./GEMINI.md` or `~/.gemini/GEMINI.md` | Gemini CLI |
| `cursor/agent-design-taste.mdc` | `.cursor/rules/` | Cursor (glob-scoped) |
| `windsurf/agent-design-taste.md` | `.windsurf/rules/` | Windsurf |
| `copilot/copilot-instructions.md` | `.github/copilot-instructions.md` | GitHub Copilot |

Install them automatically from inside your project:

```bash
bash agent-design-taste/scripts/install.sh --agent claude
bash agent-design-taste/scripts/install.sh --agent all --dry-run
```

Every adapter assumes the repository sits at `./agent-design-taste/` relative
to your project root. If you cloned it elsewhere, edit the path in the adapter —
it appears in the first line of each file.

**These files point; they do not duplicate.** They stay short on purpose: the
knowledge lives in the repository, and the adapter's only job is to make the
agent open the right file first.
