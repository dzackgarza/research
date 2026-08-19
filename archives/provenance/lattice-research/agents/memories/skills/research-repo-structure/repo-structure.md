# Research Repo Structure Reference

## Environment and sacred files

The Sage path is `/home/dzack/miniforge3/envs/sage/bin/sage`. Use `uv venv` for dependencies, never system packages. All computation, validation, and paper builds run through the `justfile`.

`GOAL.md` is the read-only research specification. `theory/references/index.md` is the append-only literature spine.

## Directory organization

Subdirectories of durable content roots are automatically allowed. The baseline durable roots are `src/`, `tests/`, `notes/`, `theory/`, `theory/references/literature/`, `paper/`, `reports/`, `lean/`, `tasks/`, `.agents/`, and `scratch/`.

Root-level additions are allowed only when they create a clearly valuable durable category of research material, tooling, or shared documentation that does not fit cleanly inside an existing root. Process-sprawl directories are forbidden.

## Where code goes

`src/` is finalized, permanent, reusable backend and tool code. It is the trusted first-party computation core. Code here uses canonical constructors and shared mathematical vocabulary. Vendored/external code goes in `src/external/`.

`tests/` contains verified mathematical tests run via pytest. Every test must use canonical constructors from `src/`. Tests verify real mathematics against known literature results and fixtures. Tests must not invent ad hoc lattice constructors, bypass the foundation API, or use raw `QuadraticForm()` or `diagonal_matrix()` calls when a canonical constructor exists. If the canonical API is insufficient for a test, surface that as a need to extend `src/`.

New executable task specs live as `.agents` cards. Legacy `tasks/T-XXXX/` artifacts, if present, are historical and should be migrated or linked from cards before reuse.

`scratch/` is gitignored. Agents do exploratory, experimental, or draft work there. Nothing in scratch is ever committed. Promote scratch work only after audit: move verification to `tests/` or reusable infrastructure to `src/`.

Lean formalizations go in `lean/`. There is exactly one Lean project. Do not create duplicate Lean scaffolds.

## Directory proliferation gate

Agents create directories to categorize process. This creates debris. Create folders inside established durable roots freely. New root-level directories require justification and must represent durable content, not a workflow stage.

Use this routing:

- Verified mathematical computation goes in `tests/`.
- Reusable computation code or infrastructure goes in `src/`.
- Exploratory draft work goes in gitignored `scratch/`.
- Mathematical observations go in `notes/`.
- Proof sketches go in `notes/proofs/`.
- Lean formalizations go in `lean/`.
- The living LaTeX working paper goes in `paper/`.
- Reviewed workstream reports and attachments go in `reports/workstreams/`.
- Papers go in `theory/references/literature/`.
- State-machine task artifacts go in `tasks/`.
- Durable shared theory/reference/tooling documentation goes in `theory/` or another coherent shared root.
- Operational context goes in agent memory.
- Change rationale goes in git commit messages.

There is no `computations/` directory. Exploratory work goes in `scratch/`, verified work goes in `tests/`, and reusable code goes in `src/`.

There is no `scripts/` root. `src/` is the trusted shared code surface, `tests/` is the verified computation surface, and task-linked computation artifacts should live in their natural durable roots and be linked from the `.agents` card; legacy `tasks/T-XXXX/computations/` paths are not the model for new work.

Git history and agent memories are not enough for mathematically informative failure.
If an approach failed in a way that constrains future research, preserve the
mathematical lesson in the relevant card, workstream report, or living paper. Do not
preserve broken code, dead scripts, or raw failed artifacts.

## Automatic pruning

At session startup, delete `.orig` files, `.sage.py` Sage preparse artifacts, and empty directories. Root-level process-debris directories require classification first.

Before deleting a root-level directory, classify it as durable repo root, process debris or duplicate scaffold, or mixed. For mixed directories, move durable contents to the correct location before deleting debris.

Before deleting a directory, check whether it contains uncommitted work that traces to a `GOAL.md` task. If so, move relevant files to their correct location first.

## Broken work policy

Broken computations get fixed or deleted. Never document and preserve them.

If a script fails, fix it in the same worktree or delete the broken code and start
over. Do not merge broken code with a companion status or issue document. Do not
archive broken code for reference. Preserve only the mathematical information learned
from the failure, such as a false conjecture, exact proof gap, exhausted search range,
or missing-source result.

## Spec and durable artifact preservation

Spec files, review files, theory notes, TODO files, and other durable design artifacts are source material. Autonomous agents must never modify spec files. The only exception is an interactive session where the user has given a specific spec edit or rewrite to implement.

A spec that disagrees with code is not stale implementation debris. It may define the migration target. It is evidence about intended semantics, required nouns and verbs, missing infrastructure, and preserved mathematical facts.

Do not rewrite a spec because it mentions an old API, rejected method name, or broader semantic surface than current implementation. If a spec/code mismatch matters, document it as follow-up and continue around it, or ask for an interactive pass.

An untracked durable file is not disposable. If it is a spec, review, note, theorem sketch, or substantive user work, treat it as high-value material immediately.

## Debris handling

Do not delete or remove any file unless you can directly prove it was created by a subagent, or the user explicitly authorizes the deletion. Inference from git messages, timing, style, or directory location is not proof.

Markdown requires special care. Markdown outside the explicitly allowed top-level set can be user-requested documentation or agent-generated debris. Read and classify before touching it.

Before cleanup that touches multiple files or removes a directory, list what will be removed, explain why each item qualifies as debris, and wait for user confirmation. The only pre-authorized exception is automatic pruning of `.orig`, `.sage.py`, and empty directories.

## Runtime caches and local generated artifacts

All repo workflows run through `just`. Do not run computation, tests, builds, publishing, or QC manually when a `just` recipe exists.

Expensive deterministic backend computations may use the repo cache configured by `.envrc` through `COBLE_RESEARCH_CACHE_DIR`. Treat that cache as local generated state, not source. Do not manage it in code or by hand except to invalidate stale deterministic outputs by deleting `.cache/` or specific cache-key files.

Test timing data configured through `COBLE_RESEARCH_TEST_TIMING_DIR` is local generated state. It may be deleted to reset local timing history and must not become durable repo documentation.

Global QC artifacts such as coverage data, coverage XML, CodeQL databases, SARIF, slop-classifier models, and tool caches belong under the global QC/cache system, not in this repo root.
