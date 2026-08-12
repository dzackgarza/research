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

## Notebook workflow note

- For any notebook inspection, execution, or result-checking, use `japi` (from `jupyter-assistant-api`) rather than direct Notebook HTTP API calls.
- `japi` is the required interface for reading cells, restarting kernels, and verifying rendered results in `computations/notebooks/` during development and debugging.
- Skip test, QC, build, execution, and rendered-result verification for changes confined to `computations/notebooks/` or `src/dzack_research/preamble/`.
- Commit those changes with verification hooks skipped; do not let unrelated repository failures block notebook or preamble work.

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

**Never write a definition or insert a citation from memory.** Before writing or editing any definition, open and read an actual source — the theory docs, the book's existing defining occurrence, the cited reference, or the upstream text — and transcribe from it.
A definition recalled from training is a fabrication risk; a citation key recalled from memory is a fabrication risk (it may not exist in the bib file, or may point at the wrong entry).
Verify the source exists and the citation key resolves before committing.
This rule overrides any pressure to "just write it" — an unverified definition or citation is worse than a TODO placeholder.

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
   **Discuss before editing.** An annotation identifies a concern; it is not an implementation instruction.
   Before changing any artifact, discuss the intended update with the user and obtain explicit approval.
   For mathematical feedback, establish the correct theory and the source that states it before proposing prose.
   Do not make a reflexive local correction from the quoted span or from memory: confirm that the proposed change fits the document's global mathematical story.

   Each entry's `uri` (`localhost:7654/Roadmap.html`) plus the normalized `TextQuoteSelector.exact` pin the exact source span → map to `docs/Roadmap.md` and apply the edit.
   Hot-reload re-renders each touched page live: the tight edit → one reload → look cycle.

6. **Resolve** — `annotate resolve` tags the batch acted via the Hypothesis API, dropping it from the open set (`annotate status` shows open vs. acted).
   Commit the doc edits alongside the already-committed ledger so git history anchors each note to the state it landed against.

7. **Reopen** — `annotate wait` again for the next window (with `notifyOnExit: true`). Back to step 2.

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

- **Undecidability audit (always-on).** Before writing code, reflect explicitly on whether the requested operation or equality check relies on or attempts to resolve an **undecidable problem** (e.g. morphism equality in presented modules/groups, the Word Problem, general equivalence of infinite algebraic structures). Never invent hand-rolled or ground-up boolean checks (`==`, `is_zero()`, `is_isomorphic()`) for undecidable problems; state the exact decidability boundary, rely only on battle-tested decision algorithms where they exist, and keep axiomatic invariants as paper-proven category theory rather than pseudo-computable runtime booleans.

- **A correction that removes machinery halts artifact production.** The rebuild's first act is the specimen, not the re-filed card; two machinery-removals on one proposal invalidate the frame (vault: `global/advice/corrections-update-the-model-not-the-artifact`).

- **Turn audit.** What statement could now be falsified that could not before this turn?
  If none, the turn was preparation — apply the deletion test (vault: `global/traps/hard-problem-artifact-drift`). Meaningful work can be embarrassing; process noise cannot.

- **mypy is a discovery tool, not a gate.** A type error is a signal about the actual code: a wrong return type, a missing method on a real class, a type hierarchy that doesn't match the mathematics. The correct response is to understand what the code's types actually are and fix them — never to silence the checker with `object`, `Any`, `type`, deleted annotations, `# type: ignore`, or config loopholes. Those carry zero type information; a function annotated `-> object` passes on literally anything, which means it asserts nothing.
  When a type is genuinely unnameable because the object is load-injected from a `.sage` file mypy cannot import, the fix is to make it importable (move to `.py`, add a stub, or restructure the import boundary) — not to annotate around the absence.
  Never probe the QC config (`mypy-global.ini`, `ai-review-ci`) looking for what `Any`-related settings might be allowed. The rule is: never use `object` or `Any`. That is already known from the errors mypy reports. Looking for a loophole is hacking the gate, not doing the work.

Work-shape catalogue with this repo's exemplars and the meaningful-vs-noise litmus: `.agents/references/displacement-pattern-index.md` (D1–D6). These are review criteria for plans and completion claims alike — the Review Guidelines below guard completion *claims*; this section guards the loop that never claims.
This discipline is culture, not a gate: do not build detectors, hooks, or mandatory checklists from it.

**Self-audit checkpoint (invented language).** Everything this repo touches is an honest mathematical entity with a standard name in a wide, well-established corpus — work here has no reason to invent terminology or types, and inventions are poison memetics: they recruit faithful re-implementations and bias architectural decisions (caught late, the cost is a remediation pass or a discarded subtree).
The emitting context reliably cannot see its own inventions — re-emission risk peaks *while processing a correction* ("cardinal-equipped" was emitted in the very sentence describing the previous fix, 2026-07-17) — so the audit must be fresh-context: spawn a subagent primed verbatim with `.agents/references/mathematical-auditor-priming.md` and hand it the artifact itself, never a summary.
Checkpoint after any correction, before issue bodies or plan cards ship, and before committing lexicon/manifest/typing surfaces.

# Relay and referent discipline (always-on)

The user reads only the orchestrator's own messages — subagent reports, tool
output, and session shorthand are private context. Communicating from that
private context as if it were shared is a theory-of-mind failure with
recurring shapes (memory: `relay-translation-not-forwarding`, 2026-08-09):

- **Relay = translation, not forwarding.** State the decision-relevant claim
  first, in repo-grounded terms (this repo's files, spec rows, standard
  mathematical names), a few sentences; detail on request. An agent's
  journey — what it ran, what it tried, how it got there — is not content.
- **Coinages are not shared language.** Session-local shorthand (input→output
  arrows like "A1^8 -> E8", row nicknames, bare count fractions) means
  nothing outside the context that minted it. Re-ground every reference
  before it crosses to the user.
- **"I don't understand" names a dangling referent, not a knowledge gap.**
  The repair is to restore the missing reference, never to explain the
  underlying mathematics — this is the user's own research program; an
  unrequested lecture is both the wrong fix and an insult.
- **Compression test.** If the user's own summary of the issue is two
  sentences, the message that needed those two sentences and didn't lead
  with them failed, regardless of how much correct detail it carried.

# Performance claims (always-on)

**Never report a call count as an efficiency metric.** Not "2,502 constructions",
not "~3 million calls to `coordinate_ring`", not "it runs 484 times". A count is
not a cost: a million cheap calls can be free and four hundred expensive ones can
be the whole run, so the number carries no information about what to fix and
invites optimising the wrong thing.

Report **wall time as a function of \(n\)** — how the cost grows with rank,
order, number of generators, size of the input — or report nothing. A single wall
time for one specimen is a data point, not a claim about efficiency; it becomes
one only when a second size shows the shape. Where a profile is the evidence,
quote its *time* columns, never its `ncalls`.

Call counts remain legitimate as **diagnosis**: they locate a recursion, name the
function that repeats, and prove a cascade exists. Use them to say what is
happening, never to say how expensive it is.

# What optimization is for (always-on)

The dominating concerns are legibility, auditability by a mathematician,
elegance, cohesion with the preamble's style, and doing the mathematically
principled thing rather than raw numerics. If that costs performance, so be it.

Never take apart code that reads as the correct mathematical sequence of steps in
order to make it faster. A method whose body a mathematician can check against the
definition is worth more than a fast one they cannot.

Optimize **waste**, which is a different thing entirely:

- needless recomputation — the same value derived again because nothing carried it;
- needless enumeration — ranging over an object where generators, a presentation,
  or a matrix identity answers (see the enumeration rule);
- needless verification — re-deriving a theorem, a definition, or a fact the
  caller already established;
- a general algorithm applied where the object's own structure has a better one —
  the fix there is to give the structure its own category and let placement pick
  the algorithm, never to special-case inside a general method.

Removing waste usually makes the code *more* legible, because what remains is the
mathematics. That is the tell that it was waste.

Genuine hot paths may later need `case`/`match` dispatch or caching. That is a
design change: propose it and discuss it explicitly first. Reaching for a cache,
or for a literature constant in place of a computation, before finding out *why*
something is slow, is not optimization — it is hiding the defect.

**Test specimens are small by default.** A proof of correctness for invariants,
coinvariants, or \(O(L)\) does not need \(E_8\), a K3 lattice, or an Enriques
lattice. \(U\) has the swap involution; powers of \(U\) already give interesting
combinations; their orthogonal groups are finite and their invariants and
coinvariants are quick. Reach for a large specimen only when the claim is about
that specimen.

# Repository layout

Top-level directories (this is a navigational map; each tree owns its own README/AGENTS.md):

- **`computations/`** — the working computational corpus.
  Its `experiments/` subtree holds the **spikes** (see the lineage note below and *QC integration for spikes*). Other subdirs are task-specific: `vendor/` (third-party code — see below), `coxiter/` (CoxIter tool integration), `lattice-orbits/`, `enriques-moduli/` + `enriques-paper-artifacts/` (Enriques-surface moduli work), `notebooks/` (**the user's plane — see below**), `scripts/` (one-off and exploratory scripts — **the only `scripts/` dir; it is QC-exempt**, and is where exploratory code is relocated to de-scope it from the strict gates; holds `components/`, the reusable computation pieces such as the `coxeter-vinberg/` prototypes, relocated here in `746595e`), `reports/` (generated output).

- **`src/`** — the installable package (`dzack_research`). Deliberately thin: right now it is the public Sage import surface re-exporting the maintained spikes (`lattice`, `feature`), covered by `tests/`. **Migration criterion:** code lives in a spike until it has matured past spike status and is usable for real research — demonstrated by *shipped, tested, high-level notebooks* that do actual work with it.
  Only then does it migrate here, and the move is the semantic statement that it is meant to be shared and reused.
  Do not promote code into `src/` because it looks finished; promote it when a notebook proves a researcher can use it.

- **`computations/notebooks/`** — **the user's audit and control plane, not agent work.** It is the JupyterLab `root_dir`. It is not subject to QC, to layout conventions, to naming or taxonomy rules, or to agent tidying: no agent proposes reorganizing it, splitting it, imposing folder schemes on it, or holding its contents to the standards that govern `src/` and the spikes.
  Agents write here only when explicitly asked.
  What agents *may* do is make things reachable from it — see the symlinks below.

  Reachability is by symlink, verified working through the live server (list, open, save, delete all round-trip to the real path, no restart needed):

  - `archive/` → `archives/notebooks/` — the retired notebooks, still live reference material

  - `spike-demos/` → `computations/experiments/sage_lattice_category_spike/notebooks/`

  Symlinking is preferred over moving: the originals stay in the tree that owns them (archive stays QC-exempt, spike demos stay beside the spike whose test suite runs them), while the control plane can see everything.

  **Implicit typesetting:** a bare `X` at the end of a cell renders as LaTeX when Sage can genuinely typeset `X`, so `show()` is not needed for ordinary inspection.
  Explicit `show()` still works and is still worth writing where the intent is presentation rather than inspection.

  The source of that behaviour is **`sage-init.sage` at the repo root** — tracked here, because it is part of how this repo's notebooks are meant to read.
  It becomes active only by being linked to Sage's startup file:

  ```
  just sage-init-install   # links ${DOT_SAGE:-~/.sage}/init.sage -> sage-init.sage
  just sage-init-check     # proves in a real kernel that Sage objects typeset and plain text does not
  ```

  `sage-init-install` is idempotent and refuses to replace anything it did not create, including a symlink pointing elsewhere — a pre-existing `init.sage` is never clobbered.
  Sage reads that one file for the terminal REPL *and* every Jupyter kernel, so installing it once covers both with nothing to remember per notebook.

  It is deliberately *not* `%display latex`, which also typesets strings, numpy arrays and opaque objects into unreadable character-by-character fallbacks; the file's own header comment records the measurements behind that choice.
  Being a tracked `.sage` file it is in Sage QC scope: it passes `_sage-syntax` (the commit tier) and draws no vulture findings.

- **`computations/vendor/`** — **third-party code you did not write.** Clone or drop external scripts here and they are importable from every Sage process (CLI, `sage -python`, every Jupyter kernel) with no restart and no registration; see its README. Contents are gitignored, and `vendor` is already a globally QC-excluded directory name, so external code never enters the gates.
  Nothing authored here ever graduates — write your own code in a spike.

**How code becomes importable in a Sage notebook.** One rule per kind, no bespoke path plumbing:

| Kind | Home | Made importable by |
| --- | --- | --- |
| External, published | — | `sage -pip install <pkg>` (or `sage -pip install "<name> @ git+<url>"` when it has no PyPI wheel, as `ore_algebra` does) |
| External, unpackaged | `computations/vendor/` | drop it there; `dzack_research.preamble.vendor` puts it on the path, called from `sage-init.sage` (interactive sessions; non-interactive callers call `vendor.activate()`) |
| Ours, spike | `computations/experiments/<name>_spike/` | `sage -pip install --no-deps -e <spike-dir>` (already done for both spikes; edits are live) |
| Ours, graduated | `src/dzack_research/` | `sage -pip install --no-deps -e .` (already done; edits are live) |

Editable installs point at the working tree, so a rebuilt or reinstalled Sage is the only thing that breaks them — re-run the two `-e` installs and check the vendor path with `sage -c 'import _vendor_selfcheck'`.

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

3. **Package importability** — the spike directory is a package (`__init__.py`). For shells and tests the repo `.envrc` puts `computations/experiments` on `PYTHONPATH`. **Notebook kernels do not inherit that** — the systemd unit runs `direnv exec /home/dzack`, which loads `~/.envrc`, not the repo's. Kernels get the spikes from `sage -pip install --no-deps -e <spike-dir>`, which is the durable mechanism; see the importability table under *Repository layout*. A new spike needs that one install, once.

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

# The preamble is a universe over Sage (always-on)

The preamble is a layer over Sage, not a collection of helpers.
Once a session loads it, the mathematician stops receiving raw Sage objects: everything reached from the preamble is an owned object, which may or may not use a Sage object underneath.
The stated purpose is *owned uniformization*.

What it exists to fix is Sage's non-uniformity, not Sage's algorithms.
Sage carries more than ten distinct notions of *group*, and an operation as elementary as $\operatorname{Aut}(G)$ is, depending on which one you hold: absent; present under a different name; known and simple but unwired (it is a call into GAP); or genuinely uncomputable.
A session cannot hold that variation, so the preamble presents one name for one mathematical operation, and either answers or asserts.

This governs the rules below:

- Sage objects are an implementation detail. The crossing happens inside owned code, at the point of computing, never in what a session receives.
- Where Sage spells one mathematical operation several ways, the preamble picks one spelling and the others do not exist in the session.
- Where Sage has no algorithm, the preamble still owns the name. A missing capability is a stated gap on the owned interface, never a second spelling and never a silent absence.

# Mathematical Sage API discipline (always-on)

These rules govern preamble, spike, and any Sage-facing API in this repo.
They are the generative constraints behind repeated corrections (override-refine, catalogue namespaces, Hom/Aut construction, session ergonomics).
A design that violates them is wrong even when it “works.”

**In one line:** write Sage as if the category and the catalogue *are* the theory — idiomatic constructions, one ontological home, no second layer between the mathematician and the object — and delete anything whose only job is to mediate, rename, wrap, or reassure.

## 1. The category is the only extension point

Methods belong on refined categories (`ParentMethods` / `ElementMethods` / `MorphismMethods`).
This repo’s override-refine puts the new subcategory’s methods first in the MRO so owned methods win over concrete class methods; that is what makes monkey-patches, module `__getattr__`, and “hack around Cython/Hom” unnecessary.

If Sage’s interface is wrong or incomplete, **own it in the category and replace it**.
Workarounds (`without_element_wrap`, ad-hoc `L.isometry(matrix)`, freestanding patch modules) mean ownership was refused.

The mechanism is boring and total: one general refine helper, plus post-init hooks on **classes** (not constructor wrappers) so new categories install themselves.
New capability = new category content, not a new installation strategy.
Element Cython types get a thin façade so `ElementMethods` (including dunders) can override; do not escalate that into a parallel object model.

See the addendum below for the refine pattern; prefer override-refine from `dzack_research.preamble.refine` over raw `_refine_category_` when owned methods must precede concrete class methods.

## 2. API shape is dictated by the mathematics

Reject APIs that are software-coherent but mathematically incoherent.

- Named literature objects (e.g. a K3 involution) are **catalogue data**, not methods of every lattice of that type.
- Operations of an object under structure (e.g. invariant and coinvariant lattices under a group action) live on that object’s category methods — or as thin sugar on the morphism — not in a freestanding feature file.
- An isometry is a **Hom/Aut element**. Construct it the way morphisms are constructed (generator images `{g: image}`); the matrix is a derived view (`to_matrix`), not the definition.
- Algebraic operations use native protocols (`L + M`, `sum([...])`, `L ** n` for n-fold sum). Do not invent `_oplus` or force chains of `.direct_sum` when `+` is the monoidal operation.

If the call site would not be written at a Sage prompt while doing the math, the API is wrong.

## 3. Ontological placement — one home

Every entity has exactly one kind of home:

| Kind | Home |
| --- | --- |
| Behavior of a class of objects | category methods on the refined category |
| Named specimens / literature tables | one catalogue namespace (e.g. `Lattices`) |
| Session defaults (implicit multiplication, traceback colour, …) | import-time effect of loading the init/ergonomics module |

Freestanding files, string registries, factory functions, module `__getattr__`, and dual module-level aliases of the same object are symptoms of placement by accident of authorship, not by what the entity is.

Named lookup is by attribute (`Lattices.U`).
Keys that are mathematics stay typed (`Lattices.TwoElementary[8, 8, 0]` for Nikulin $(r,a,\delta)$), never stringified tuples.
Put such tables on the namespace that owns the specimens.

Prefer **one clean export** for a catalogue surface: import `Lattices`, use `Lattices.…`. Do not re-export every attribute at module level.

## 4. One source of truth, stated once, inline

Construction **is** the definition.
Define values inline in the namespace class body (or a helper called from that body while dependencies are in scope).
Do not spread a definition across “empty container → later assignment → `globals().update` → string lookup → re-export.”
Do not construct after the class and patch attributes on afterward — that means the class body was not the definition.

An alias is object identity (`SEn is E10_2`), not a gram-matrix equality check in production code.
If identity matters, assert `is` in a test.

## 5. Hostility to non-semantic indirection

Delete anything that can be removed without changing what a mathematician can say or compute:

- wrap-then-call (`enable_X` → `install()` → `enable_X` → real call)
- catch-and-rethrow the same exception kind with a different message
- dict façades that reimplement `.items()` / `.keys()`
- re-exports of the same object under a second name
- import-time asserts that restate what construction already entails
- tests of “conflict scenarios” instead of tests of the intended dispatch or mathematical claim
- catalogue factories that re-verify primitives on every lookup (`is_involution` belongs on the morphism)

Ceremony is a bug: it creates a second, softer API that agents will use instead of the real one.
This is the same discipline as work-selection (above): an artifact that cannot fail carries no information.

## 6. Generality over local cleverness

When blocked, do not add a special case for this object.
Strengthen the general interface (element façade, Aut constructor, `+` / `sum`, override-refine) so the special case disappears.
Ask “why does this freestanding file/function exist?” — if it has no mathematical referent, delete it and place the content in the category or catalogue.

## 7. Tests certify the intended contract

Tests falsify the mathematical or dispatch claim: refined methods win over class methods; this alias is the same parent; this Aut is an involution; this table entry is that named lattice.
They do not exercise scaffolding, reassure about naming conflicts, or re-encode construction as gram-matrix comparisons.

Predicates that are part of the theory (`is_involution`, invariant and coinvariant lattices, isotypic components, …) are methods on the owned category interfaces, not side conditions in catalogue loaders.

**Adding to `tests/test_known_mathematics.sage`.** That file is the owner's specification of mathematics the preamble must reproduce, so agents do not extend it freely — but an addition is allowed whenever an independent source citation is attached to the new row: the Stacks Project, Kerodon, an item in the owner's Zotero library, a published paper, or an arXiv preprint. The citation is the admission ticket, and it names the source of the *asserted fact*, not of the implementation. Cite by the source's own identifier (Zotero `citationkey`, Stacks tag, arXiv id), verified against the source rather than recalled.

A row whose assertion would hold with the functionality removed certifies nothing. Assert the content: a maximal overlattice is reached by an inclusion, so the arrow's index is the assertion, not the codomain's existence.

## 8. Block Hom spelling, invariant and coinvariant lattices, and catalogue hygiene

Rules distilled from preamble work on direct-sum coordinates, embeddings, and coinvariant lattices (2026-07).

**Block Hom spelling.** A Hom/Aut between orthogonal direct sums is a block matrix: the $j$-th block column is the image of the $j$-th domain summand. Prefer block dicts via `L.summands()` — `{a1: b1, a2: b2 + b3}` — over flat generator-image lists when the mathematics is blockwise. Equal-rank block sums (`b2 + b3`) are gen-wise placement into multiple target blocks (the diagonal $N(2)\hookrightarrow N\oplus N$, not $N\to N\oplus N$). Name morphisms by their true domain; ergonomic sugar must not invent the wrong morphism type.

**Invariant and coinvariant lattices, and inclusions, are computed on the lattice.** There is no "eigenlattice": the notions are the invariant lattice, the coinvariant lattice, and the isotypic components. Invariant/coinvariant lattices and primitive inclusions (`invariant_lattice`, `coinvariant_lattice`, `coinvariant_inclusion`) are category methods on `IntegralLattices`; the coinvariant is $(L^G)^{\perp L}$. Catalogue must not ship helpers that take a named lattice plus an involution and assert kernel rank or Gram agreement — that certifies a guess, it does not construct. Named literature embeddings *use* the generic interface; they do not reimplement it.

**Catalogue is specimens plus nested namespaces, not ceremony.** Call `categories.install()` before building catalogue lattices; no manual `refine_one_lattice`. No `_with_names`, `_involutions`, `_embeddings`, or similar factories around one-liners or class bodies. Nested `Involutions` / `Embeddings` belong in the `Lattices` class body (populate empty nested classes in that body when Python scoping requires it); no post-hoc `__qualname__` patching or `Lattices.X = …` assignment after the class is built. Once the principled block or coinvariant API exists, catalogue entries use it everywhere — flat lists or kernel-basis shortcuts left “because they still work” are drift.

# Categorical organization model (always-on)

How the preamble's category tree is organized, and where new content goes.
For precise, formalized definitions of the notions below, defer to
`~/gitclones/lean-categories` (FOUNDATIONS.md and `LeanCategories/`): framed
generators and bases are §13.5, chosen presentations as structure are §75,
partial resolutions and the $FP_n$ hierarchy are §76, resolution classifiers
are §77. When a preamble docstring and that document disagree, the document
wins.

## Property subcategories vs data subcategories

Two kinds of subcategory, and the distinction decides method placement.

- A *property* subcategory states a fact about its members: finitely
  generated, finitely presented, finite, abelian. Membership is the
  statement, so its methods are predicates answered by placement
  (`is_finite` returns `True` because membership states it) and theorems the
  property entails.
- A *data* subcategory states that members carry a chosen datum: a framing
  (a chosen generating epimorphism $F(S)\twoheadrightarrow X$ from a free
  object), a chosen presentation (a framing plus chosen free relations), a
  chosen basis. Its methods consume the datum.

A property is the propositional truncation of the corresponding data
category: finitely generated = "some finite 1-framing exists"; finitely
presented = "some finite 2-framing exists"; $FP_n$ continues through chosen
syzygies, and each extension of a framing to the next level is itself a
choice. So a method that consumes a choice lives on the data subcategory and
never on the property one. A group can be provably finitely presented
(arithmeticity) while no practical presentation algorithm exists; asking it
for a presenting free group must be an absence, not a computation.

Producing a choice is one explicit crossing: a single named method computes
the datum once, stores it, refines the object into the data subcategory, and
returns it. Downstream code then asks the data category's words. A property
category never silently computes presentation data on demand.

The basic form of such a datum is a collection of morphisms (the chosen
tower). Where the surrounding category supports it, prefer the principled
package — an augmented chain complex for additive data, a DGA only when the
resolution must carry multiplication — over loose tuples of maps.

## Axioms live as high up as possible

An axiomatic subcategory is declared once, at the highest category that can
state it, and reached by `with_axiom` (the axiom name registered in
`sage.categories.category_with_axiom.all_axioms`). `Framed` is the model
case: one global axiom whose category owns everything derivable from the
framing datum — generating set, generators, counts, presentation display —
so that groups, modules, and algebras share one contract instead of three
restatements.

Duplication is the diagnostic: if two parallel categories restate the same
contract or the same derived method, the axiom was attached too low. Never
re-declare in a subcategory what a supercategory already provides, and never
restate category methods on a concrete class.

## Contracts are abstract_methods

A data subcategory states its contractual requirement as `abstract_method`s
on its `ParentMethods` (the pattern of
`categories/modules/pure/modules.sage`, where being a module *is* the ring
morphism $\rho: R \to \operatorname{End}(M)$ and the category requires it).
The obligation cannot be a construction gate — `_refine_category_` admits
anything and runs no hook — but it can be *visible*: an unmet obligation
resolves to the abstract declaration on the object, and the sweep below
reports it.

## Every constructor registers in the obligations sweep (for now)

`tests/test_constructors_meet_their_obligations.sage` runs every way the
preamble makes an object and asks each result whether any name its
categories require still resolves to an abstract declaration. That sweep is
the enforcement of the contract above, so every new constructor or
construction path must add a specimen row to its `_constructions()` table.
An object that can enter a category without the category's defining datum is
exactly the failure class this catches (modules with no ring action, form
modules with no form). "For now": the sweep is the current gate; a stronger
mechanism may replace it, but absence from the sweep is never acceptable.

## Classes only tie constructions into the tree

Almost everything lives at the categorical level. Concrete `Parent` classes
enter only to tie a specific construction into the tree for a specific
subcategory — `BasedFreeModule`, framed groups intake, the framed free
algebras — and constructions are uniformized as high up as possible: one
free functor per concrete category in
`categories/functors/free_forgetful_adjunction.sage`, one framing contract,
per-category classes only where the construction itself is specific. A new
capability is new category content plus, at most, one construction class;
it is never a parallel class hierarchy.

# Python and Sage research code style (always-on)

These rules govern Python, Sage, spikes, the preamble, the installed package, tests, and notebooks.
Use the detailed mathematical and repository rules above when they give a narrower instruction.

## Mathematical model before representation

- Work in the order mathematical object → representation → implementation.
- Start with the mathematical object, its data, its laws, and its hypotheses.
- Identify the relevant category, objects, morphisms, functors, and universal properties before choosing classes or methods.
- Map that representation into Sage only after its objects, morphisms, hypotheses, and constructions are specified.
- Implement only the operations that remain after native Sage structure is used.
- Do not derive an API from the methods, classes, or data layouts that happen to exist.
- Do not duplicate the data of a chosen morphism in fields on its domain or codomain.
- Represent a chosen representative of a subobject of $B$ by a monomorphism $f:A\hookrightarrow B$.
- Obtain its target from `f.codomain()` and use $f$ as the chosen monomorphism.
- Keep an element of $A$ distinct from its image in $B$.
- Do not use coercion to erase the distinction between an element and its image.
- Preserve distinctions between objects, presentations, morphisms, images, theorems, and decision procedures.
- A presentation is not the object that it presents, a registry label is not a category, and runtime validation is not a theorem.
- Never replace an undecidable equality problem with a new Boolean method.

## Goal substitution and agent hubris

Treat the user's technical discussion as a precise specification.
Do not read it as loose guidance because it arrives in prose.
Every mathematical noun, qualifier, example, caveat, and request to think can constrain the result.
If code and the stated model differ, surface the difference.
Never silently choose the code's weaker model.

This repository contains research code that is intentionally outside common software patterns.
The agent will tend to replace unusual mathematics with conventional code from its training distribution.
This default can change the object, hypotheses, codomain, or required construction.
Conventional code is not a useful default when the task is to implement new mathematics.

Assume that the user knows this repository, Sage, and the mathematical program better than the agent.
This is an operational limit on the agent's authority.
It does not make every user claim true.
It means that an apparent contradiction must become a discussion, not a silent correction.

Agent hubris occurs when the agent treats its current framing as the only possible framing.
An apparent implementation barrier proves only that the present approach has a barrier.
It does not prove that the mathematical requirement must be weakened.
The agent is often too close to its first design to see a better formulation.
User input can resolve the barrier by changing the representation, category, functor, or direction of construction.

Never make a theoretical compromise on the user's behalf.
This includes replacing a general object with a special case, a construction with a predicate, or a theorem with a runtime guess.
It also includes adding a fallback, an exception branch, or a weaker public operation to make the code run.

When the exact implementation appears impossible, stop before writing compromise code.
Report these facts:

- The exact requested object or statement.
- The precise obstruction in the current approach.
- The hypothesis or property that a proposed compromise would weaken.
- The mathematically distinct alternatives that remain visible.
- The smallest question that needs the user's judgment.

Recommend a compromise when useful, but do not select it without approval.
The user can often remove the obstruction without any compromise.
A short expert reframe can prevent generic code, false abstractions, and a later refactor.

For example, let $R$ be a commutative ring.
Let $M$ and $W$ be $R$-modules, and let $b:M\times M\to W$ be $R$-bilinear.
A user can request the submodule $\langle b(x,y)\mid x,y\in M\rangle_R\le W$.
Replacing it with a $\mathbb Z$-lattice's scale ideal changes the codomain and requested object.
The user already made that distinction.
The agent must preserve it, not teach it back or erase it.

Likewise, let $f:M\to N$ be an $R$-module homomorphism.
A request to construct $\ker(f)\le M$ is not a request to decide whether $\ker(f)=0$.
If current code decides only the latter in a special case, surface the mismatch before changing the construction.

A passing test can hide the substitution when the test encodes only the weaker claim.
The loop is self-confirming:

1. Replace the requested object with a familiar proxy.
2. Test the proxy.
3. Use the passing test as evidence for the original requirement.

Such evidence says nothing about the omitted requirement.
It makes later work inherit a mathematically false interface.

No instruction file can contain all of the user's mathematical knowledge.
Exact listening is therefore a required research method.
Implement what the user specified.
If that cannot be done exactly, surface the nuance and defer the mathematical decision.

## Native Sage model and direct code

- Use Sage's `Parent`, `Element`, `Category`, `Morphism`, and `Hom` structures.
- Model a functor as a functor and a morphism as a morphism.
- Let subcategory relations and Sage categories with axioms determine available methods, hypotheses, codomains, and algorithms.
- Put mathematical operations, constructions, and predicates in category methods, as specified above.
- Use a narrow subclass for one representation-specific defect that Sage categories cannot express.
- Override only the incorrect operation and retain the established implementation.
- Keep each method in the same order as the mathematical definition.
- A mathematician must be able to compare the method body directly with that definition.
- Do not hide the defining steps behind chains of non-mathematical helper functions.
- Return results in their correct parent and category.
- Make public operations and valid constructions explicit after every refactor.
- Compare valid constructions, methods, category membership, result parents, and notebook behavior.
- Compare semantics, not filenames, class counts, method counts, or structural similarity.

## Types

- Give each value the type that names its mathematical role.
- Use `Parent` for an object of a Sage category, not `Any` or `object`.
- Distinguish parents, elements, morphisms, coefficient rings, modules, matrices, domains, and codomains.
- Treat each mypy error as evidence about the model or import boundary.
- Fix the model, method owner, return contract, import path, or missing stub.
- Never weaken an annotation to silence the checker.
- Make stable `.sage` definitions importable when their real types cannot otherwise be named.

## Simplicity and prior art

- Choose the smallest implementation that satisfies the complete mathematical requirement.
- Add no unused parameter, speculative extension point, or interface with one caller.
- Add an abstraction only when a second real use requires it.
- Use the project's dependencies before adding code or packages.
- Use native Sage before adding a parallel implementation.
- Use a maintained package or mature reference implementation before new local code.
- Keep unavoidable local code small and cite its mature reference implementation.
- Remove obsolete constructors, aliases, fallbacks, bridges, and compatibility paths.
- Keep one current implementation for each operation or construction.

## Names and ownership

- Use established mathematical or Sage terminology.
- Name each entity by its mathematical role, not its storage or implementation.
- Treat a wrong name as possible evidence of a wrong abstraction.
- Check the definition, type, owner, operations, and category before a semantic rename.
- Give each mathematical entity one authoritative module and one public export.
- Place public exports at a clear package boundary.
- Keep category methods, catalogues of examples, session defaults, and computation code in their stated homes.
- Keep definitions, terminology, category declarations, exports, and decisions in one authoritative source.
- Do not create mirrored registries or synchronized copies.

## Repository placement

- Keep the installed package thin and stable.
- Move code from a spike into `src/` only after a high-level research notebook uses it.
- Do not promote code because it looks complete.
- Develop new mathematics in the active spikes by generalizing from verified examples.
- Use the frozen category specifications only as prior art.
- Install published dependencies normally.
- Put unpackaged external code in `computations/vendor/`.
- Code in `computations/vendor/` never graduates into the maintained package.
- Keep project-authored experimental code in a spike.
- Treat `computations/notebooks/` as the researcher's control surface.
- Do not reorganize, classify, or tidy that notebook tree unless the user asks.
- Use editable installs and repository symlinks instead of notebook path manipulation.
- Keep notebook setup cells minimal and make editable-install changes available without copying code.
- Use high-level notebooks for real mathematical work, not only API demonstrations.
- Keep the preamble small, cohesive, native to Sage, and usable without notebook setup.

## Proof and tests

- Test mathematical behavior and method resolution through Sage categories, not scaffolding or correction history.
- Assert the correct parent, category, domain, codomain, images of elements where defined, composition, or mathematical equality.
- Test high-level notebook operations when notebook usability is the claimed behavior.
- Use the smallest test case that distinguishes correct behavior from a plausible failure.
- Use a large named example only when the claim concerns that example.
- Verify the surface named by the requirement.
- Use a real Sage process for Sage behavior and a live kernel for notebook behavior.
- Inspect rendered output when the requirement concerns rendering.
- Treat a nearby green check as evidence only for the proposition it executes.

## Performance and search

- Measure wall time and its growth with input size.
- Use call counts only to locate repeated work.
- Remove repeated derivation, needless enumeration, repeated verification, and overly general algorithms.
- Preserve code that shows the correct mathematical sequence, even when a faster form is less clear.
- Start filesystem discovery at the requested path with a shallow query.
- Expand the search only when the evidence requires it.

## Completion and durability

- Complete the original mathematical operation or construction, not only a local type, test, registry, or plan task.
- Continue when the next in-scope step is clear and safe.
- Defer work only for a real dependency or a required user decision.
- Context limits and a successful local subtask do not justify deferral.
- End each substantive unit in a focused commit.
- Preserve unknown files until their ownership is known.
- After ownership is known, commit required files and use recoverable deletion for disposable files.
- Keep important work in version control, not only in a working tree or notebook session.

# Addendum: installing methods on Sage objects via category refinement

This addendum is the **mechanism** for §1 above (category as extension point).
For preamble and owned APIs, use override-refine (`dzack_research.preamble.refine.refine`) and post-init hooks on classes; do not introduce monkey-patches or constructor-only installation paths for new work.

Sage objects (parents, elements, morphisms) carry methods through their **category's dynamic MRO**.
A category defines `ParentMethods`, `ElementMethods`, and `SubcategoryMethods` inner classes;
any parent whose category (or join of categories) includes that category gains those methods automatically.

**The correct way to install new methods on existing Sage objects** — in exploratory notebooks,
preamble files, or a spike's initialization — is:

1. **Define a category** that declares `ParentMethods`, `ElementMethods`, or both.
2. **Route objects into that category** by post-init hooks on the relevant **classes** (preferred), calling override-refine so owned methods precede concrete class methods.

This is **not monkey-patching**. You are not replacing methods on a class;
you are telling Sage that certain instances belong to a more refined category,
and Sage's own dynamic dispatch makes the methods available.

## Canonical pattern

```python
from sage.categories.category_with_axiom import CategoryWithAxiom_singleton

class _MyCustomCategory(CategoryWithAxiom):
    """A custom category whose methods apply to refined objects."""

    def super_categories(self):
        return [SomeBaseCategory()]

    class ParentMethods:
        """Methods available on every parent refined into this category."""

        def my_method(self):
            return ...

    class ElementMethods:
        """Methods available on elements of parents refined into this category."""

        def my_element_method(self):
            return ...


# Post-init: refine specific objects into the category
def install():
    cat = _MyCustomCategory()
    for obj in target_objects:
        obj._refine_category_(cat)
```

## Codebase examples

| File | Category | Target objects | Entry point |
| --- | --- | --- | --- |
| `archives/lattice-research/src/sage_patches/ring_base_category.py` | `_ModuleBaseRings` (custom) | `ZZ`, `QQ`, `RR`, `CC`, `QQbar`, `Zp(p)`, `GF(p)` | `_install_module_base_rings()` — iterates well-known singletons |
| `archives/lattice-research/src/sage_patches/ideal_submodule.py` | `Modules(ring)` (existing Sage category) | Ideals produced by `Ring.ideal()` | `_module_aware_ideal()` — intercepts the constructor and refines each result |
| `archives/lattice-research/src/sage_patches/fraction_quotients.py` | `Modules(ZZ)` (existing) | `QQ / ZZ`, `QQ / (n*ZZ)` | `__truediv__` patch on `RationalField` + direct refinement of two specific instances |
| `archives/lattice-research/src/sage_patches/module_enrichment.py` | `Modules(R)` (existing) | Direct sums, quotients of free modules | `_ensure_module_refinement()` — called inside patched `direct_sum` and `quotient` |

## Variants

### A. Define a custom category + batch post-init (preferred)

Used in `ring_base_category.py`. Best when you know the target objects at import time:
they are singletons (like `ZZ`) or produced by a small set of constructors.

```python
class _MyMethods(CategoryWithAxiom):
    class ParentMethods:
        def utility(self): ...

def install():
    for obj in [ring1, ring2, ...]:
        obj._refine_category_(_MyMethods())
```

### B. Constructor interceptor (archive / last resort)

Used historically in `ideal_submodule.py` and `fraction_quotients.py`.
Prefer class post-init hooks (§1) for new work.
Only intercept a constructor when objects cannot be caught after `__init__` and a class hook is impossible.

```python
def _intercept_constructor(self, *args):
    result = _native_constructor(self, *args)
    refine(result, MyCategory())  # override-refine when owned methods must win
    return result
```

### C. Mid-construction refinement

Used in `module_enrichment.py`. The refinement happens *inside* a method that already
creates the object, so no interception is needed — just add `_refine_category_` before returning.

## Rules of thumb

- **Category owns the methods.** The method implementation lives in `ParentMethods` or
  `ElementMethods`, not inline in the post-init code. The post-init only routes the object in.

- **Override-refine when owning an interface.** Use `refine` from the preamble so the new
  subcategory precedes the concrete class in the MRO; bare `_refine_category_` alone leaves
  class methods ahead of category methods (Sage’s default), which is wrong for overrides.

- **Hook classes, not constructors**, for new installations. Post-init on the Sage class is
  the default; constructor interception is archive/last-resort (Variant B).

- **Use existing Sage categories when possible.** If you just need an object to be recognized
  as an `R`-module, refine into `Modules(R)` rather than defining a new category.
  Define a new category only when you have method implementations that no existing category provides.

- **Do not monkey-patch class methods.** If you find yourself writing
  `SomeSageClass.my_method = lambda ...`, stop and write a category instead.
  Monkey-patching breaks for subclasses, is non-composable, and bypasses Sage's MRO.

- **Do not store method implementations on the parent class itself.**
  The parent class (`IntegerRing_class`, `MatrixSpace`, etc.) is Sage's compiled code;
  the category's `ParentMethods` is where new methods belong.

- **`_refine_category_` joins.** It calls `self._init_category_(self.category().join(Cat))`, so
  the object keeps all its existing category memberships and gains the new one.
  Calling it multiple times is safe. Override-refine still performs that join, then rebuilds
  `__class__` so owned methods win.

- **`@final` guards override.** If a method in `ParentMethods` should not be overridden by
  a more specific category in the join, mark it `@final`.

## What this is not

This pattern is specifically for **retroactive method installation** — adding capabilities to
objects that already exist at import time or are created by Sage's existing constructors.
It is not a replacement for defining a proper category hierarchy from scratch;
it is the bridge between Sage's compiled algebra and this repo's semantic needs during
exploratory and spike work.
