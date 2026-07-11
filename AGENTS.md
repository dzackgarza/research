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

# Repository layout

Top-level directories (this is a navigational map; each tree owns its own README/AGENTS.md):

- **`computations/`** — the working computational corpus. Its `experiments/` subtree holds the **spikes** (see the lineage note below and *QC integration for spikes*). Other subdirs are task-specific: `components/` (reusable computation pieces, e.g. the `coxeter-vinberg/` prototypes), `coxiter/` (CoxIter tool integration), `lattice-orbits/`, `enriques-moduli/` + `enriques-paper-artifacts/` (Enriques-surface moduli work), `notebooks/` (Jupyter), `scripts/` (one-off scripts), `reports/` (generated output).
- **`projects/`** — long-horizon subprojects. `projects/lattice-research/` is a **git submodule** (`dzackgarza/lattice-research`) and contains `category_specs/` (see lineage note), plus `src/`, `theory/`, `lean/`, `paper/`, `tests/`, `reports/`. Because it is a submodule, edits there are commits to a *separate* repo.
- **`writing/`** — authored prose: the Coble paper draft and research notes, oral exams, research statement, talks. The user's durable authored artifacts — preserve native LaTeX/tikz source.
- **`notes/`** — research notes (`computations/`, `papers/`, `topics/`), including the terminology-drift dictionary.
- **`references/`** — external inputs: `pdfs/`, `generated-indexes/`, `local-system-dependencies/`.
- **`archives/`** — retired material (`provenance/`).

## category_specs vs. the spikes (two attempts at the same substrate)

Both implement the same goal — a mathematically-semantic, Sage-compatible substrate for exact lattice/surface computation (`projects/lattice-research/GOAL.md`) — but are **two distinct attempts**, and it matters which one a given task targets:

- **`projects/lattice-research/category_specs/`** — the **older, more ambitious attempt**, now **stalled and frozen / on the backburner**. It aimed at the full category/refinement language up front (its `src.bak/`, `tests.bak/` are relics of that). Treat it as **frozen prior art**: read it for design intent, but it is not where active generalization happens. Parity-audit issues (#26/#84/#85 …) that cite `category_specs/…` paths are pointing at this frozen surface.
- **`computations/experiments/*` (the spikes)** — the **current, active attempt**: the same work **broken up and made modular**, deliberately **starting from provably-working lattices and generalizing outward** rather than specifying the whole category tree first.
  - **`sage_lattice_category_spike/`** — the **maintained base spike**: Sage parity, normalization, literature-backed behavior with a known reference surface. The lexicon (`lexicon/` + `typings/`) is its single type surface. This is where the root-datum, form, morphism, and category interfaces actually live — a repo-wide grep that skips `computations/experiments/` will falsely conclude "no repo surface exists."
  - **`sage_lattice_feature_spike/`** — the **fork** carrying genuinely new mathematics with no Sage analogue, gap-ledger gated; it *imports* the base spike.

When a task says "the repo owns X" or "X is a gap," resolve it against the **active spikes**, not the frozen `category_specs`.

# Issue-tree and milestone policy (research repo)

This is a research repository with a much longer work horizon, more detailed planning, and more human check-ins than a typical software project. Naive software-geared structural rules (e.g. itree's W040 native-milestone mirror) are less applicable here: treat such findings as a flag to investigate whether *some* consolidation is warranted, never as a mandate — and never collapse the tree or milestones by an order of magnitude to satisfy one. The itree issue tree is authoritative; native GitHub milestones are capability-level human-review checkpoints created just-in-time (user ruling 2026-07-11; W040 = 46 is accepted as-is).

The `needs-research` label is the parking state — work parked pending investigation or upstream capability — not a register of decisions awaiting the user. Do not enumerate labeled issues as "open human decisions"; genuine decisions are extracted through decision-register sweeps (see #97) and recorded as rulings on the issues, the gap ledger, and plan cards.

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


# Review Guidelines

These are additional requirements for reviewing agent work.
They do not replace the reviewer’s normal role, repo-specific standards, or technical
judgment. They provide the failure model that should shape the review.

The task is not merely to review a PR. The task is to decide whether a completion claim
is true under the original objective.
The standard is full, correct, provable completion against the original requirements and
repo guidelines. Anything less is incomplete work that must not be treated as a win.

## Failure Model

Agents systematically produce impressive non-completion.
Common patterns are: polished summaries that imply finished work, caveats that quietly
narrow the goal, reclassification without proof, delegated discovery presented as
resolution, process language that substitutes for evidence, merged PRs treated as
completion, passing checks treated as semantic proof, and artifacts that look
substantial while leaving required work unowned.

Treat the agent’s summary, PR description, closing comment, issue closure, “goal
completed” statement, and self-reported validations as untrusted.
They may be diagnostic pointers, but they are not evidence that the work is complete.
The evidence is the original issue or task, the code diff, tests, source/runtime facts,
review comments, and produced artifacts.

## Decisive Invariants

Preserve the original success condition.
Read the original issue or task before accepting any restatement of it.
Keep its quantifiers intact: “all,” “complete,” "full subset," “zero remaining,” and
similar terms cannot be quietly narrowed to examples, partial coverage, known blockers,
or whatever the PR happened to touch.

Nothing required may disappear silently.
A required work family must be implemented, explicitly falsified, or validly
reclassified with evidence that satisfies the issue’s own standard.
Partial implementation is not completion.
Future work is not completion.
Count reduction is not completion.
Resolved review threads are not completion.
Passing checks are not completion.
Substantial-looking work is not completion.
“Better than before” is not completion.

Goal substitution is the main thing to detect.
Ask whether the submitted work solves the original problem or merely produces a narrower
artifact: cleaner metadata, a partial subset, a better explanation, a new issue, a
renamed scope, a local workaround, or proof that someone should investigate later.

Technically correct administrative artifacts can be goal substitution.
A well-written issue, comment, audit note, scope statement, or enumeration of remaining
work may be required, but it does not complete implementation, testing, proof, or
downstream cleanup. If the original task requires execution, the artifact is only useful
insofar as it drives that execution; it must not become the stopping point.

Treat self-scoped remaining-work lists as a severe completion-laundering pattern.
When an agent is asked to enumerate remaining work, the domain is the original full
completion requirement, not the agent’s intended subset, the PR’s current shape, a
closeability criterion, or the work left after deferral and reclassification.
A valid enumeration subtracts only artifact-proven completed work from the original
contract. Deferrals, routed follow-ups, owner changes, and truthful incompletion notes
remain unresolved work unless the original task explicitly made that administrative
routing the whole deliverable.

If an agent repeats a narrowed enumeration after being corrected, treat that as a hard
misalignment signal, not as an innocent wording issue.
The reviewer should identify the original full requirement, the scope the agent
substituted, and the required work hidden by that substitution.

Silent reclassification is not resolution.
If the PR says remaining work is out-of-scope, research-owned, stub-owned, plugin-owned,
downstream-owned, or future-owned, require evidence from the relevant source/runtime
behavior, repo boundary, or original acceptance criteria.
A sentence in the PR description is not enough.

Ownership boundaries matter.
The submitting repo must prove its own claimed behavior and do the blocker forensics
required by its own issue.
Do not require a receiving or downstream repo to classify another project’s internal
uncertainty unless the original issue explicitly made that part of acceptance.
When an external issue is created, it should be written for that receiving repo, not for
a reader who already knows the submitting repo’s context.

## Evidence Expectations

Review tests as evidence, not as decoration.
Valid tests exercise the real production path or semantic requirement.
Be skeptical of helper-only tests, tautologies, assertions of the implementation’s own
output, bypasses around the runtime/plugin/stub path, example-only coverage where the
issue required full coverage, weakened assertions, and missing invalid-nearby cases
where the fix could overgeneralize.

For plugin work, the evidence should usually distinguish valid generic behavior from
invalid nearby ordinary Python and should not hard-code a downstream consumer.
For stubs work, the evidence should be source-backed: the upstream surface exists, the
stub matches public behavior, no fake API is added, no Any/object opacity escape is
introduced, and inherited-method inflation is not used unless source exposes that
surface.

Watch for code-level laundering: hard-coded consumer names, support for local research
abstractions as if they were external API, fake stubs, broad Any/object escapes, line
suppressions, diagnostic filtering, deletion of required data, broad type widening, and
any move that makes checks pass by weakening the problem instead of solving it.

## When Acting on Review Feedback

A positive disposition requires a commit.

Do not resolve an accepted review comment until the code/proof remediation is committed and the reply cites the commit.

Never reply “accepted,” “aligned,” “fixed,” “addressed,” or “will address” to a review thread unless the remediation is already committed. A thread cannot be resolved on intent or future work.

Rejected and modified feedback must be collected in a top-level PR comment titled `Review feedback disposition ledger` so resolved threads do not hide the audit trail.

Review comments are not implementation specs. The worker must translate accepted feedback into first-principles remediation requirements before assigning implementation.

For each comment:
- Identify the concern.
- Identify the proposed fix.
- Decide whether the concern is true under global + repo policy.
- Decide whether the proposed fix preserves those policies.
- If the concern is true but the fix is wrong, apply a policy-compatible remediation.

## Writing the Review

Write nuanced feedback for an intelligent reader.
Do not force a machine-readable template, a mandatory table, or a simplistic pass/fail
label when prose communicates the situation better.
Do make the completion judgment clear: whether the original task can be considered
complete, what evidence supports that judgment, and which unresolved requirements block
completion if any remain.

Do not foreground effort, progress, good intentions, volume of work, or “substantial”
partial implementation when required work remains.
Mention completed pieces only when they are necessary to identify the exact remaining
blockers or to prevent redoing already-correct work.
Do not compare incomplete work to “no work done” or “completely fake work”; compare it
to the expected standard: the task done correctly, completely, and provably.

When required work remains, lead with the incompleteness and the concrete blockers.
Do not make the reader excavate the missing work from beneath praise, context-setting,
or a narrative of what did get done.

Nuance belongs in the evidence and blocker analysis, not in softening the completion
standard. The review should make it easy to finish the work, not easy to feel satisfied
with less than the original contract required.
