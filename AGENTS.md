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

Plan work is card-backed.
Create and update plan cards with `agent-memory plan add` and `agent-memory plan update`, not `agent-memory add --type plan`.

Use `agent-memory retrieve <key>`, `agent-memory update <key>`, and `agent-memory delete <key>` for memory CRUD.

The vault should be committed at all times.
Treat staged or unstaged vault changes as an ephemeral error state.
Before normal memory work resumes, load the bundled vault-maintenance skill with `agent-memory maintain skill vault-maintenance` and follow its referenced check, repair, and commit workflows.

Move reusable lessons during maintenance with:

```bash
agent-memory maintain move <key> --to global/advice
```
<!-- agent-memory:end -->

# Banned-language replacement index (always-on)

The terms below have demonstrated **strong priors**: they re-emitted even after being catalogued in the terminology dictionary — in one case inside the anti-drift doctrine itself, as its self-chosen name.
A reference-file row is an on-demand signal; a term that survives its row needs this always-loaded one.
Never write these terms in code, issues, docs, comments, memories, or doctrine; write the replacement.

| banned | documented emissions | replacement |
| --- | --- | --- |
| **"carrier"** (carrier module/set, "carrier of a structure", "carrier siting") | 3+ — P1's first draft; the P6 enforcement clause's own name (corrected 2026-07-12); Tier B row 1 predates both | the **underlying set/module** (image of the forgetful functor); in doctrine prose name the entity: the **object, morphism, homset, or functor** |
| **"ambient"** as free-standing data ("the ambient", "shared ambient", "shared span/coordinates", `ambient=`/`in_ambient=` parameters, stored `_ambient` state) | pervasive — Sage back-porting; issue #100's own original body; re-emitted in doctrine prose 2026-07-11 | a subobject is the pair `(A, f: A ↪ B)`: its ambient **is** `f.codomain()`; rational/real constructions live in the **base-changed parent** `L ⊗ R'`, named by its functor |

**Graduation rule:** when a drift term already carrying a dictionary row is emitted a *second* time, it graduates to this index — the repetition is the evidence of a strong prior.
Diagnose new drift by principle first (generative failure model P1–P6); this index is only for proven repeat offenders.
Full catalogue: `.agents/references/terminology-dictionary.md`; code-shape patterns: `.agents/references/slop-pattern-index.md`.

# Docs prose policy (always-on)

Prose in the docs book is governed by the writing guide, `docs/_writing-guide.md` — a non-rendered (leading `_`, so Quarto ignores it), citable policy index of banned prose patterns in three kinds, each with a concrete example and remediation for one-shot learning:

- **Prose tells (`PR-*`)** — bad prose on its own terms; the fix is a rewrite.

- **Evasion tells (`EV-*`)** — prose standing in for mathematical work not done; the fix is the work (name the morphism, write the definition), never a nicer phrase.
  "carries" is the type case (see the banned-language index above).

- **Mathematical tells (`MA-*`)** — reinvented or colloquial parlance in place of the standard notion or the established in-repo definition; the fix is to use the definition and cite it (e.g. "equality" or "axiom" per priors instead of `@def-equality-of-objects` / `@def-axiom-classifier`).

**Check feedback for the pattern, not just the instance.** Before applying any writing correction, check whether it instantiates a recorded item.
If so, fix it and cite the id.
If it is a *new* pattern, record it in the guide — forward-facing, with an example and remediation — before or alongside fixing the one instance; a correction that fixes a sentence and leaves the pattern unrecorded will recur, and the guide is where a one-off correction graduates into policy an auditor applies everywhere.
Run the index in the fresh-context audit (`.agents/references/mathematical-auditor-priming.md`) after every substantive docs edit, the same as the vocabulary pass.
Requirements the docs must satisfy (definition-before-use, resolvable references) are *recorded* in the guide's Requirements section and audited against the artifact, never self-certified in prose (`PR-3`).

# Docs workflow (always-on)

Documentation work — the docs book under `docs/` — is **never externalized to GitHub issues or PRs**. It is developed directly: interactive work with the user and/or autonomous research, iterative refinement committed as each unit settles, and pushes typically **held until the user approves**. That approval normally follows an interactive pass rather than a PR review lifecycle — organization and coherence audits, re-readings, reviews, and reorganization of the accreted material, plus basic intelligent coherence checks.
Do not open an issue or PR to plan, track, or hand off docs work, and do not treat the PR completion gate as applying to it; the issue-tree and milestone policy below governs implementation and research work, not the book.

## Docs hosting surfaces

The docs book ships as a Quarto site (`docs/_quarto.yml`, `project.type: book`) in three surfaces:

- **Local preview** — `just docs-preview` serves `docs/` at http://localhost:7654/ via `uvx --from quarto-cli quarto preview` (live reload; quarto-cli provisioned on demand, not installed system-wide).
  A stale render also lives at `docs/_site/` from prior builds; it is not kept fresh with the working tree.

- **Published site** — GitHub Pages at https://dzackgarza.github.io/research/ (`build_type: workflow`, branch `main`), deployed by `.github/workflows/docs.yml`. The site-url is recorded in `_quarto.yml` (`book.site-url`).

- **GitHub wiki** — the repo's native GitHub wiki is **disabled** (no `wiki/` ref exists; `hasWiki: true` in API but no commits).
  Do not conflate "the wiki" (historical name for the docs book, migrated via PR #272 "wiki-book-migration") with the GitHub wiki feature.
  The book under `docs/` is the wiki's successor.

A push of `main` that changes `docs/` triggers `docs.yml` and redeploys Pages; local edits do not appear on the published site until pushed.

## Annotation feedback loop

The user delivers docs feedback by annotating the rendered pages in the browser; the `annotate` CLI turns those annotations into a committed batch the agent acts on.
The CLI is not installed on `PATH` (`/bin/annotate` is an unrelated tool) — it is the `uvx`-installable console script from the Hypothesis fork at `~/gitclones/hypothesis-fork-project/hypothesis-review`, always invoked as:

```bash
uvx --from ~/gitclones/hypothesis-fork-project/hypothesis-review annotate <subcommand>   # run from ~/research
```

`<subcommand>` is `wait` / `pull` / `slice` / `record` / `resolve` / `status` / `doctor`; the steps below name it bare for readability.
One cycle:

1. **Serve** — `just docs-preview` runs in the background on `:7654`.

2. **Open a session** — from `~/research`, `annotate doctor` first confirms readiness (inside a git repo, `h` API + Postgres reachable), then `annotate wait` records the open timestamp locally and blocks, serving the loopback session-close endpoint on `127.0.0.1:8902`, waiting for the browser.
   A *session* is a time window.
   Run it as a background job so the agent can keep working while the window is open.
   **Spawn `annotate wait` with `notifyOnExit: true`** (or the equivalent exit-notification flag on your PTY/spawn tool) so that when the user hits **Send to agent** and `wait` exits, the agent receives the completion signal automatically instead of having to poll.
   Do not poll with `pty_read` + sleep loops to detect completion; wait for the exit notification.

3. **Annotate** — over the `:7654` pages, the user highlights spans and writes comments via the Hypothesis client, then hits **Send to agent**. That closes the window and unblocks `wait`.

4. **Record + deliver** — `wait` collects every annotation created during the window, appends them to `feedback/ledger.jsonl`, commits (`feedback: record N annotation(s) …`), *then* drains them from `h`, and prints the batch JSON. **Record-before-drain is the safety property**: feedback cannot reach the agent unrecorded, and a failed write leaves the notes in the sidebar rather than deleting the only copy.
   (`pull` does the same for an already-open session; `slice`+`record` capture ad-hoc notes made outside a session.)

5. **Act (agent)** — read the batch / ledger.
   Each entry's `uri` (`localhost:7654/Roadmap.html`) plus the normalized `TextQuoteSelector.exact` pin the exact source span → map to `docs/Roadmap.md` and apply the edit.
   Hot-reload re-renders each touched page live: the tight edit → one reload → look cycle.

6. **Resolve** — `annotate resolve` tags the batch acted via the Hypothesis API, dropping it from the open set (`annotate status` shows open vs. acted).
   Commit the doc edits alongside the already-committed ledger so git history anchors each note to the state it landed against.

7. **Reopen** — `annotate wait` again for the next window (with `notifyOnExit: true`).
   Back to step 2.

# Work-selection discipline (always-on)

An output that cannot fail carries no information.
Plans, schemas, id systems, plan cards, ledgers, status rows, memories, and readiness reports always "succeed" — producing them reduces no mathematical uncertainty, so they are exhaust around the work, never the work.
The unit of progress at every scale is a **falsifiable specimen**: something a mathematician could find *wrong* — a category defined natively, an operation placed with its hypotheses and codomain, a surfaced spike-vs-doctrine mismatch, a notebook cell reproducing a source.
This is the fourth graduation of one lesson (tests assert accomplishment, not declaration; negative tests assert a positive count first; real declarations are the schema); the work-selection instance graduated after recurring (#217's BFS registry; the 2026-07-16 #251 planning session, three corrections deep).

- **Specimen-first.** The first deliverable of any work unit is the specimen.
  A plan is approvable only if it names its first specimen; preparation is justified only by a named uncertainty and stops when the specimen can begin.
  Coordination machinery is justified only by friction observed while producing specimens, never by anticipated scale.

- **Mathematical questions get mathematical answers** — stated before any plan card, schema, or memory is touched.
  Artifact updates are exhaust around the answer, never the answer.

- **A correction that removes machinery halts artifact production.** The rebuild's first act is the specimen, not the re-filed card; two machinery-removals on one proposal invalidate the frame (vault: `global/advice/corrections-update-the-model-not-the-artifact`).

- **Turn audit.** What statement could now be falsified that could not before this turn?
  If none, the turn was preparation — apply the deletion test (vault: `global/traps/hard-problem-artifact-drift`). Meaningful work can be embarrassing; process noise cannot.

Work-shape catalogue with this repo's exemplars and the meaningful-vs-noise litmus: `.agents/references/displacement-pattern-index.md` (D1–D6). These are review criteria for plans and completion claims alike — the Review Guidelines below guard completion *claims*; this section guards the loop that never claims.
This discipline is culture, not a gate: do not build detectors, hooks, or mandatory checklists from it.

**Self-audit checkpoint (invented language).** Everything this repo touches is an honest mathematical entity with a standard name in a wide, well-established corpus — work here has no reason to invent terminology or types, and inventions are poison memetics: they recruit faithful re-implementations and bias architectural decisions (caught late, the cost is a remediation pass or a discarded subtree).
The emitting context reliably cannot see its own inventions — re-emission risk peaks *while processing a correction* ("cardinal-equipped" was emitted in the very sentence describing the previous fix, 2026-07-17) — so the audit must be fresh-context: spawn a subagent primed verbatim with `.agents/references/mathematical-auditor-priming.md` and hand it the artifact itself, never a summary.
Checkpoint after any correction, before issue bodies or plan cards ship, and before committing lexicon/manifest/typing surfaces.

# Repository layout

Top-level directories (this is a navigational map; each tree owns its own README/AGENTS.md):

- **`computations/`** — the working computational corpus.
  Its `experiments/` subtree holds the **spikes** (see the lineage note below and *QC integration for spikes*). Other subdirs are task-specific: `components/` (reusable computation pieces, e.g. the `coxeter-vinberg/` prototypes), `coxiter/` (CoxIter tool integration), `lattice-orbits/`, `enriques-moduli/` + `enriques-paper-artifacts/` (Enriques-surface moduli work), `notebooks/` (Jupyter), `scripts/` (one-off and exploratory scripts — **the only `scripts/` dir; it is QC-exempt**, and is where exploratory code is relocated to de-scope it from the strict gates), `reports/` (generated output).

- **`src/`** — the installable package (`dzack_research`). Deliberately thin: right now it is the public Sage import surface re-exporting the maintained spikes (`lattice`, `feature`), covered by `tests/`. **Migration criterion:** code lives in a spike until it has matured past spike status and is usable for real research — demonstrated by *shipped, tested, high-level notebooks* that do actual work with it.
  Only then does it migrate here, and the move is the semantic statement that it is meant to be shared and reused.
  Do not promote code into `src/` because it looks finished; promote it when a notebook proves a researcher can use it.

- **`tests/`** — tests for the `src/` package surface only.
  Spike tests live in each spike's own `tests/` tree.
  `projects/lattice-research/` is a **git submodule** (`dzackgarza/lattice-research`) and contains `category_specs/` (see lineage note), plus `src/`, `theory/`, `lean/`, `paper/`, `tests/`, `reports/`. Because it is a submodule, edits there are commits to a *separate* repo.

- **`review-calibration/`** — **git submodule** (`dzackgarza/research-review-calibration`) holding a frozen lattice-spike simulacrum for **LLM review calibration**. Planted violations live in `GROUND_TRUTH.md` (never in the review packet).
  Experiment issues and advisory review runs target the submodule repo, not this monorepo.
  Hill-climb prompt/context/permissions there before changing production `review-packet.tar` here.

- **`writing/`** — authored prose: the Coble paper draft and research notes, oral exams, research statement, talks.
  The user's durable authored artifacts — preserve native LaTeX/tikz source.

- **`notes/`** — research notes (`computations/`, `papers/`, `topics/`). The terminology-drift dictionary is **not** here; it is vault-owned at `.agents/references/terminology-dictionary.md` (see the banned-language index above).

- **`references/`** — external inputs: `pdfs/`, `generated-indexes/`, `local-system-dependencies/`.

- **`archives/`** — retired material (`provenance/`).

## category_specs vs. the spikes (two attempts at the same substrate)

Both implement the same goal — a mathematically-semantic, Sage-compatible substrate for exact lattice/surface computation (`projects/lattice-research/GOAL.md`) — but are **two distinct attempts**, and it matters which one a given task targets:

- **`projects/lattice-research/category_specs/`** — the **older, more ambitious attempt**, now **stalled and frozen / on the backburner**. It aimed at the full category/refinement language up front (its `src.bak/`, `tests.bak/` are relics of that).
  Treat it as **frozen prior art**: read it for design intent, but it is not where active generalization happens.
  Parity-audit issues (#26/#84/#85 …) that cite `category_specs/…` paths are pointing at this frozen surface.

- **`computations/experiments/*` (the spikes)** — the **current, active attempt**: the same work **broken up and made modular**, deliberately **starting from provably-working lattices and generalizing outward** rather than specifying the whole category tree first.

  - **`sage_lattice_category_spike/`** — the **maintained base spike**: Sage parity, normalization, literature-backed behavior with a known reference surface.
    The lexicon (`lexicon/` + `typings/`) is its single type surface.
    This is where the root-datum, form, morphism, and category interfaces actually live — a repo-wide grep that skips `computations/experiments/` will falsely conclude "no repo surface exists."

  - **`sage_lattice_feature_spike/`** — the **fork** carrying genuinely new mathematics with no Sage analogue, gap-ledger gated; it *imports* the base spike.

When a task says "the repo owns X" or "X is a gap," resolve it against the **active spikes**, not the frozen `category_specs`.

# Issue-tree and milestone policy (research repo)

This is a research repository with a much longer work horizon, more detailed planning, and more human check-ins than a typical software project.
Naive software-geared structural rules (e.g. itree's W040 native-milestone mirror) are less applicable here: treat such findings as a flag to investigate whether *some* consolidation is warranted, never as a mandate — and never collapse the tree or milestones by an order of magnitude to satisfy one.
The itree issue tree is authoritative; native GitHub milestones are capability-level human-review checkpoints created just-in-time (user ruling 2026-07-11; W040 = 46 is accepted as-is).

The `needs-research` label is the parking state — work parked pending investigation or upstream capability — not a register of decisions awaiting the user.
Do not enumerate labeled issues as "open human decisions"; genuine decisions are extracted through decision-register sweeps (see #97) and recorded as rulings on the issues, the gap ledger, and plan cards.

## Where in-progress ideas live

Ideas are not all issues yet.
An agent that searches only the issue tree will miss live thinking and re-derive it badly.

- **GitHub Discussions** hold ideas still **in flux**: competing framings, pasted prompt responses to be reconciled, designs whose scope has not settled.
  A discussion is a thinking surface, not a decision — nothing in one is authoritative, and no PR may claim work from a discussion alone.
  Live example: #217 (*Bridging Lean to computational backends*, Ideas category).

- **Issues** hold ideas that have a scope, carrying the label that names their state: `draft` (the scope itself is provisional; expect the body to change), `research` (empirical research or evaluation required before implementation), `needs-research` (parked — above), `needs-planning` (scope known; decomposition or an executable plan required before any PR claim).

The pipeline is one-directional: **a discussion is crystallized into an issue once its scope stops moving**, and everything downstream — implementation research, decomposition into work units, proof obligations, PR claims — is carried out on the issue tree, never in the discussion.
Link the discussion from the issue and leave it in place as the rationale trail; the development of an idea, including its retractions, is the record of why the scope is what it is.
Do not delete it or summarize it away.

Practical consequences: when picking up a topic, search discussions as well as issues.
When a discussion has stabilized, the next action is to file the issue, not to keep commenting.
When a discussion is still moving, do not manufacture an issue to make it look tracked.

# QC integration for spikes

This repo delegates all test/QC to the global QC in `~/ai-review-ci` (`dzackgarza/ai-review-ci`). The pre-commit hook runs the root `just test`; pre-push runs `just test-ci`. The root recipes run umbrella hygiene, then every `computations/experiments/*/justfile` — a spike with a justfile is on QC rails automatically; adding one never requires editing the root justfile.

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

   Pure-Python spikes delegate to `python.just` instead.
   Run `just -f ~/ai-review-ci/justfiles/sage.just setup` for the full wiring contract; the QC preflight prints the exact fix for anything missing.

2. **`pyproject.toml`** — minimal `[project]` with `name`, `version`, and `requires-python = ">=3.14"` (QC installs the spike editable for mypy).

3. **Package importability** — the spike directory is a package (`__init__.py`); the repo `.envrc` already puts `computations/experiments` on `PYTHONPATH`, so `import <spike_name>` works in Sage, tests, and notebooks with no per-spike setup.

4. **Tests as `.sage` files** (`tests/**/test_*.sage`) so the Sage preparser converts integer literals to `Integer`/`Rational` before pytest collects them.
   Never commit generated `*.sage.py` preparse artifacts — they are gitignored; QC preparses into a tempdir itself.

5. **Environment** — `SAGE_BIN` is exported by the repo `.envrc`; nothing per-spike.
   Tests execute under Sage's own Python (which has pytest), not a uvx CPython.

Code in spikes is held to the global strict gates (ruff, strict mypy, pytest at commit; vulture/coverage/slop stack at push).
QC tool configs are owned centrally in `~/ai-review-ci` — never add local ruff/mypy/coverage config to a spike.

# Review Guidelines

These are additional requirements for reviewing agent work.
They do not replace the reviewer’s normal role, repo-specific standards, or technical judgment.
They provide the failure model that should shape the review.

The task is not merely to review a PR. The task is to decide whether a completion claim is true under the original objective.
The standard is full, correct, provable completion against the original requirements and repo guidelines.
Anything less is incomplete work that must not be treated as a win.

## Failure Model

Agents systematically produce impressive non-completion.
Common patterns are: polished summaries that imply finished work, caveats that quietly narrow the goal, reclassification without proof, delegated discovery presented as resolution, process language that substitutes for evidence, merged PRs treated as completion, passing checks treated as semantic proof, and artifacts that look substantial while leaving required work unowned.

Treat the agent’s summary, PR description, closing comment, issue closure, “goal completed” statement, and self-reported validations as untrusted.
They may be diagnostic pointers, but they are not evidence that the work is complete.
The evidence is the original issue or task, the code diff, tests, source/runtime facts, review comments, and produced artifacts.

## Decisive Invariants

Preserve the original success condition.
Read the original issue or task before accepting any restatement of it.
Keep its quantifiers intact: “all,” “complete,” "full subset," “zero remaining,” and similar terms cannot be quietly narrowed to examples, partial coverage, known blockers, or whatever the PR happened to touch.

Nothing required may disappear silently.
A required work family must be implemented, explicitly falsified, or validly reclassified with evidence that satisfies the issue’s own standard.
Partial implementation is not completion.
Future work is not completion.
Count reduction is not completion.
Resolved review threads are not completion.
Passing checks are not completion.
Substantial-looking work is not completion.
“Better than before” is not completion.

Goal substitution is the main thing to detect.
Ask whether the submitted work solves the original problem or merely produces a narrower artifact: cleaner metadata, a partial subset, a better explanation, a new issue, a renamed scope, a local workaround, or proof that someone should investigate later.

Technically correct administrative artifacts can be goal substitution.
A well-written issue, comment, audit note, scope statement, or enumeration of remaining work may be required, but it does not complete implementation, testing, proof, or downstream cleanup.
If the original task requires execution, the artifact is only useful insofar as it drives that execution; it must not become the stopping point.

Treat self-scoped remaining-work lists as a severe completion-laundering pattern.
When an agent is asked to enumerate remaining work, the domain is the original full completion requirement, not the agent’s intended subset, the PR’s current shape, a closeability criterion, or the work left after deferral and reclassification.
A valid enumeration subtracts only artifact-proven completed work from the original contract.
Deferrals, routed follow-ups, owner changes, and truthful incompletion notes remain unresolved work unless the original task explicitly made that administrative routing the whole deliverable.

If an agent repeats a narrowed enumeration after being corrected, treat that as a hard misalignment signal, not as an innocent wording issue.
The reviewer should identify the original full requirement, the scope the agent substituted, and the required work hidden by that substitution.

Silent reclassification is not resolution.
If the PR says remaining work is out-of-scope, research-owned, stub-owned, plugin-owned, downstream-owned, or future-owned, require evidence from the relevant source/runtime behavior, repo boundary, or original acceptance criteria.
A sentence in the PR description is not enough.

Ownership boundaries matter.
The submitting repo must prove its own claimed behavior and do the blocker forensics required by its own issue.
Do not require a receiving or downstream repo to classify another project’s internal uncertainty unless the original issue explicitly made that part of acceptance.
When an external issue is created, it should be written for that receiving repo, not for a reader who already knows the submitting repo’s context.

## Evidence Expectations

Review tests as evidence, not as decoration.
Valid tests exercise the real production path or semantic requirement.
Be skeptical of helper-only tests, tautologies, assertions of the implementation’s own output, bypasses around the runtime/plugin/stub path, example-only coverage where the issue required full coverage, weakened assertions, and missing invalid-nearby cases where the fix could overgeneralize.

For plugin work, the evidence should usually distinguish valid generic behavior from invalid nearby ordinary Python and should not hard-code a downstream consumer.
For stubs work, the evidence should be source-backed: the upstream surface exists, the stub matches public behavior, no fake API is added, no Any/object opacity escape is introduced, and inherited-method inflation is not used unless source exposes that surface.

Watch for code-level laundering: hard-coded consumer names, support for local research abstractions as if they were external API, fake stubs, broad Any/object escapes, line suppressions, diagnostic filtering, deletion of required data, broad type widening, and any move that makes checks pass by weakening the problem instead of solving it.

## When Acting on Review Feedback

A positive disposition requires a commit.

Do not resolve an accepted review comment until the code/proof remediation is committed and the reply cites the commit.

Never reply “accepted,” “aligned,” “fixed,” “addressed,” or “will address” to a review thread unless the remediation is already committed.
A thread cannot be resolved on intent or future work.

Rejected and modified feedback must be collected in a top-level PR comment titled `Review feedback disposition ledger` so resolved threads do not hide the audit trail.

Review comments are not implementation specs.
The worker must translate accepted feedback into first-principles remediation requirements before assigning implementation.

For each comment:

- Identify the concern.

- Identify the proposed fix.

- Decide whether the concern is true under global + repo policy.

- Decide whether the proposed fix preserves those policies.

- If the concern is true but the fix is wrong, apply a policy-compatible remediation.

## Writing the Review

Write nuanced feedback for an intelligent reader.
Do not force a machine-readable template, a mandatory table, or a simplistic pass/fail label when prose communicates the situation better.
Do make the completion judgment clear: whether the original task can be considered complete, what evidence supports that judgment, and which unresolved requirements block completion if any remain.

Do not foreground effort, progress, good intentions, volume of work, or “substantial” partial implementation when required work remains.
Mention completed pieces only when they are necessary to identify the exact remaining blockers or to prevent redoing already-correct work.
Do not compare incomplete work to “no work done” or “completely fake work”; compare it to the expected standard: the task done correctly, completely, and provably.

When required work remains, lead with the incompleteness and the concrete blockers.
Do not make the reader excavate the missing work from beneath praise, context-setting, or a narrative of what did get done.

Nuance belongs in the evidence and blocker analysis, not in softening the completion standard.
The review should make it easy to finish the work, not easy to feel satisfied with less than the original contract required.
