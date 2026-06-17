# design-portfolio-plugin

A Claude Code **plugin** that ships the `design-portfolio-pdf` skill — a premium,
multi-page **A4 PDF portfolio** generator in the house style (warm off-white +
terracotta + Inter), reusable for construction, architecture, interior, BIM,
landscape, or any project-specific portfolio.

This repo is also a **plugin marketplace** (`.claude-plugin/marketplace.json`), so
you can install the skill into **all** your projects from here.

## Install across all your projects

### Local Claude Code (desktop / CLI / IDE) — persistent everywhere

Run once; it stays available in every project and future session on that machine:

```
/plugin marketplace add dblackone/job-portfolio
/plugin install design-portfolio-plugin@job-portfolio-plugins
```

(Installs at user scope by default. CLI equivalent:
`claude plugin marketplace add dblackone/job-portfolio` then
`claude plugin install design-portfolio-plugin@job-portfolio-plugins`.)

### Claude Code on the web — re-add per session (ephemeral container)

The web environment is reset each session, so personal installs don't persist.
Add a **SessionStart hook** to the repo you're working in
(`.claude/settings.json`) so the plugin auto-installs at the start of every web
session:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          { "type": "command", "command": "claude plugin marketplace add dblackone/job-portfolio 2>/dev/null || true" },
          { "type": "command", "command": "claude plugin install design-portfolio-plugin@job-portfolio-plugins 2>/dev/null || true" }
        ]
      }
    ]
  }
}
```

Alternatively, for a single repo you can just copy the skill folder into that
repo's `.claude/skills/design-portfolio-pdf/` (project-scoped, no install step).

## Use it

Once installed, just describe the task — e.g. *"make me a construction portfolio"*
— and the skill triggers. The fully-qualified name is
`design-portfolio-plugin:design-portfolio-pdf`.

Then edit the `CONFIG` in `skills/design-portfolio-pdf/build_portfolio.py`
(or pass your own dict to `build()`), drop your images, and run:

```bash
pip install weasyprint pillow
python3 build_portfolio.py        # -> CONFIG["output"]
```

See `skills/design-portfolio-pdf/SKILL.md` for the full method, design system,
image-size specs, and QA workflow.
