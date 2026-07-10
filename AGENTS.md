<!-- agent-memory:start -->
# Agent memory

This repository uses the central agent memory vault at `/home/dzack/.agent-memory-vault`.

Project memory key: `projects/github.com__dzackgarza__research/index`.

Repository `.agents` and `.hermes` paths are symlinks to the same vault-owned project directory.

Before changing architecture, search both project and global memory:

```bash
agent-memory search --scope both "<task or subsystem>"
```

Record durable repo-specific lessons with:

```bash
agent-memory add --scope project --type decision --title <title> --content <content>
agent-memory add --scope project --type trap --title <title> --content <content>
agent-memory add --scope project --type advice --title <title> --content <content>
agent-memory add --scope project --type context --title <title> --content <content>
agent-memory add --scope project --type reference --title <title> --content <content>
```

Plan work is card-backed. Create and update plan cards with `agent-memory plan add` and `agent-memory plan update`, not `agent-memory add --type plan`.

Use `agent-memory retrieve <key>`, `agent-memory update <key>`, and `agent-memory delete <key>` for memory CRUD.

The vault should be committed at all times. Treat staged or unstaged vault changes as an ephemeral error state. Before normal memory work resumes, load the bundled vault-maintenance skill with `agent-memory maintain skill vault-maintenance` and follow its referenced check, repair, and commit workflows.

Move reusable lessons during maintenance with:

```bash
agent-memory maintain move <key> --to global/advice
```
<!-- agent-memory:end -->

# QC integration for spikes

This repo delegates all test/QC to the global QC in `~/ai-review-ci`
(`dzackgarza/ai-review-ci`). The pre-commit hook runs the root `just test`;
pre-push runs `just test-ci`. The root recipes run umbrella hygiene, then every
`computations/experiments/*/justfile` — a spike with a justfile is on QC rails
automatically; adding one never requires editing the root justfile.

## Adding a new spike

Create `computations/experiments/<spike_name>/` with:

1. **`justfile`** delegating to the global Sage QC (this is the whole file):

   ```justfile
   export PYTHONDONTWRITEBYTECODE := "1"

   test:
       @just -f ~/ai-review-ci/justfiles/sage.just -d . test

   test-ci:
       @just -f ~/ai-review-ci/justfiles/sage.just -d . test-ci
   ```

   Pure-Python spikes delegate to `python.just` instead. Run
   `just -f ~/ai-review-ci/justfiles/sage.just setup` for the full wiring
   contract; the QC preflight prints the exact fix for anything missing.

2. **`pyproject.toml`** — minimal `[project]` with `name`, `version`, and
   `requires-python = ">=3.14"` (QC installs the spike editable for mypy).

3. **Package importability** — the spike directory is a package
   (`__init__.py`); the repo `.envrc` already puts `computations/experiments`
   on `PYTHONPATH`, so `import <spike_name>` works in Sage, tests, and
   notebooks with no per-spike setup.

4. **Tests as `.sage` files** (`tests/**/test_*.sage`) so the Sage preparser
   converts integer literals to `Integer`/`Rational` before pytest collects
   them. Never commit generated `*.sage.py` preparse artifacts — they are
   gitignored; QC preparses into a tempdir itself.

5. **Environment** — `SAGE_BIN` is exported by the repo `.envrc`; nothing
   per-spike. Tests execute under Sage's own Python (which has pytest), not a
   uvx CPython.

Code in spikes is held to the global strict gates (ruff, strict mypy, pytest
at commit; vulture/coverage/slop stack at push). QC tool configs are owned
centrally in `~/ai-review-ci` — never add local ruff/mypy/coverage config to a
spike.
