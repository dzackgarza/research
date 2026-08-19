# Lattice Documentation (Indefinite-First)

## Purpose

This docs set exists to provide practical, accurate references for free/open lattice software with a **primary focus on indefinite lattices**.

The goal is to support workflows such as:

- indefinite quadratic form classification,
- local/global/rational isometry checks,
- discriminant-form and genus computations,
- hyperbolic/reflection-lattice methods (e.g. Vinberg-style workflows),
- lattice-with-isometry constructions used in arithmetic/algebraic geometry contexts.

## Priorities

1. Indefinite-lattice methods first.
2. Explicit method-level documentation (not vague package summaries).
3. Clear definiteness constraints and caveats.
4. Source-backed claims (official docs/source when possible).
5. Coverage across major free systems and packages.

## Non-Goals

- Proprietary CAS workflows (e.g. Magma, Wolfram).
- Polytope-counting-first documentation unless directly relevant to indefinite lattice work.
- Credit-by-alias or hidden coverage shortcuts.

## Practical Rule

When deciding what to add or refine, prefer content that improves indefinite workflows before expanding Euclidean-only reduction material.

## Setup

### 1. Install Miniforge (conda)

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash "Miniforge3-$(uname)-$(uname -m).sh" -b -p ~/miniforge3
~/miniforge3/bin/conda init bash
```

Open a new shell (or `source ~/.bashrc`) so that `conda` is on your PATH.

### 2. Create the SageMath environment

```bash
conda create -n sage sage -y
```

This downloads and installs SageMath (~1 GB, takes several minutes).

### 3. Install project Python dependencies

```bash
conda run -n sage python -m pip install pytest juliacall juliapkg pydantic pyright black
```

### 4. Verify

```bash
conda run -n sage sage -c "print('Hello from SageMath', version())"
```

### Shortcut

Steps 1–3 are wrapped in a single `just` recipe (run from the repo root):

```bash
just install-sage
```

### Running tests

```bash
just test       # standard suite
just test-full  # includes in-progress wrapper-contract tests
```

## Agents

Agents live under `agents/`, one directory per task. Each task has a shared `task.log` (the running record of all work done on that task, appended by every agent run) and per-agent debug subdirectories for individual run output.

### `agents/doc_coverage/` — documentation coverage

- prompt: `agents/doc_coverage/prompt.md`
- playbook: `agents/doc_coverage/playbook.md`
- runners:
  - `run_codex_docs_agent.sh` — OpenAI Codex
  - `run_claude_docs_agent.sh` — Claude (Sonnet, extended thinking)
  - `run_amp_docs_agent.sh` — Amp (smart mode)
  - `run_ollama_docs_agent.sh` — Ollama launching Claude integration (non-interactive)

### `agents/test_coverage/` — test coverage

- prompt: `agents/test_coverage/prompt.md`
- playbook: `agents/test_coverage/playbook.md`
- runners:
  - `run_codex_test_coverage_agent.sh` — OpenAI Codex
  - `run_claude_test_coverage_agent.sh` — Claude (Sonnet, extended thinking)
  - `run_amp_test_coverage_agent.sh` — Amp (smart mode)
  - `run_ollama_test_coverage_agent.sh` — Ollama launching Claude integration (non-interactive)

Runners can be invoked directly or scheduled via system cron.
