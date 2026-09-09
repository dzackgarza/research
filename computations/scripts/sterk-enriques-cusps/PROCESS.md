# What the large formalization projects actually do

Read from the repositories themselves on 2026-09-09, not from summaries.  Every
claim below is sourced in `REFERENCES.md`.

## FLT: build from both ends, state before proving

The instruction that most contradicts the instinct to build foundations first,
from the project's own `GENERAL.md`:

> "This project will start everywhere at once.  We're going to build from both
> ends.  The project will have achieved its initial goal if it successfully
> reduces Fermat's Last Theorem (initially proved in the 1990s) to a collection
> of several far more complex mathematical claims, all of which were known by
> the end of the 1980s. […] We'll also work up from the basics, PRing stuff to
> Lean's mathematics library `mathlib` as we go, and eventually we'll meet in
> the middle.  A preliminary early goal will be to *state* all of the major
> claims which we shall initially be assuming."

Four things follow.

**Leaves may be large and unproved, provided they are stated and cited.** The
whole first phase of FLT is a reduction to claims it does not prove.  Carrying
Baily–Borel or Torelli as stated, cited, open nodes is therefore the ordinary
structure of such a project, not a compromise and not one option among several.

**Statements are the primary artifact; proofs come later and from other people.**
Buzzard states results he does not know how to prove — explicitly including
Langlands' cyclic base change and Jacquet–Langlands, of which he says he has "the
most superficial understanding" — and hands them on.  The formal statement is the
interface that makes the division of labour possible.

**Missing library theory is contributed upstream while the top-down work
proceeds.**  Not a phase, a parallel track.

**The route is designed by a domain expert.**  FLT's path "was essentially
completely designed by Richard Taylor after discussions with Kevin Buzzard".
The DAG's shape is a research decision, not a mechanical derivation from the
source text.

## FLT: the orchestration is lightweight and state-bearing

From `CONTRIBUTING.md` and the repository metadata: 69 contributors, open since
2023-11-19, still active, with monthly commit counts between 4 and 249 —
sustained low-intensity work, not a sprint.

- A GitHub **project dashboard** with explicit columns: `Unclaimed`, `Claimed`,
  `In Progress`, `In Review`, `Completed`.
- Tasks are **issues**; work is claimed by commenting the single word `claim`,
  released with `disclaim`, linked to a PR with `propose #N`, withdrawn with
  `withdraw #N`, and moved to review by commenting `awaiting-review`.
- Labels `awaiting-review` / `awaiting-author` carry the review ping-pong.
- The blueprint graph colours nodes by status, including nodes marked as
  suitable for a small project — task granularity is a first-class design
  concern, and newcomer-sized work is identified in the graph itself.
- Pre-push hooks and a `run_before_push.sh` exist to keep CI green.

The coordination vocabulary is five words on issues.  The state lives in the
dashboard and the blueprint, not in conversations.

## FLT: what actually went backwards

Scanning ~1,400 commit messages for `revert`, `redefine`, `wrong`, `mistake`,
`deprecat`: the hits are almost entirely infrastructure — Ruby gem bumps in the
docs build reverted four times (#879, #927, #951, #1041), Mathlib deprecations
propagating downstream, CI actions.  Mathematical rework barely appears.

That is a structural result, not luck.  When statements are fixed in a blueprint
before proofs are attempted, the expensive class of rework — discovering that
what you proved was not what you meant — mostly does not happen.  The churn
migrates to dependencies and tooling, which is cheap.

## Navier–Stokes: what a finished AI formalization ships with

`openai/NavierStokesAndEuler`, published 2026-09-08, is small (two entry files,
three directories) and carries three things worth copying.

**A machine-readable manifest.**  `formalization.yaml`, following the
`mathlib-initiative/formalization.yaml` schema v0.4, records at repository root:
the sources being formalized with their `location` and an explicit
`relationship: formalizes`; `related_formalizations` with `relationship:
builds-on`; MSC2020 and arXiv classification; and a `status` block giving

```yaml
  sorry_count: 0
  sorry_in_definitions: 0
  main_results:
    - declaration: "NavierStokes.Comparator.navier_stokes_breakdown_R3"
      file: "NavierStokes/ComparatorSolution.lean"
      sorry_count: 0
      axioms: ["propext", "Classical.choice", "Quot.sound"]
```

`sorry_in_definitions` is a tracked field of its own, and the axioms actually
used by each main result are enumerated.  Both are exactly the surface where
this repository's failures would have been visible.

**Statements sourced from an independent party.**  The Comparator reference
statements are adapted from DeepMind's Formal Conjectures formalization of the
Clay problem, not written by the authors of the proof.  Separating who states
the theorem from who proves it is a structural defence against semantic
hallucination: you cannot quietly prove a weaker statement if you did not write
the statement.

**Independent kernel re-checking.**  `lake exe comparator` runs the
formalization against `leanprover/comparator` with `lean4export` and an external
checker (`nanoda_bin`) under a sandbox (`landrun`), rather than trusting the
build that produced it.

## The convergence conditions, and their opposites

What made these projects converge:

- statements fixed and cited before proofs are attempted;
- a dependency graph as the durable store of project state;
- statement authorship separated from proof authorship, and from review;
- big known results carried as stated, cited, open leaves;
- foundations contributed upstream in parallel with top-down work;
- per-node status, sorry counts, and axiom lists as tracked data;
- an independent checker run over the finished artifact.

What sent work sideways or backwards:

- **loss of project state** — the recorded cause of the failed FLT attempts,
  where agents lost track of what was done and what remained;
- dependency and tooling churn, which is the cheap kind and shows up as
  repeated reverts in the commit log;
- semantic hallucination, the expensive kind, which the statement-first
  discipline is designed to prevent rather than to detect.
