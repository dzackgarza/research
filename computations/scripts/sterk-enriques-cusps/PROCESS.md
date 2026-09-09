# What the large formalization projects actually do

Read from the repositories and the primary technical report on 2026-09-09, not
from summaries.  Sources in `REFERENCES.md`.

Two projects, deliberately kept apart, because they are different kinds of
thing: the **Imperial College FLT project** is a five-year human crowd-sourced
effort, and the **11-day autonomous run** is a team of Claude agents on
Prove2Me.  The second is the model for work of the kind attempted here; the
first is one of its inputs.

## The 11-day run: how it was actually organized

Day 1 was 7 August 2026; the root card read Proved at 22:00 ET on 17 August.
The harness was built on **Prove2Me**, developed by Tianyi Peng's group at
Columbia.  The unit of work is a **card**: one theorem statement, posted as a
node in the shared dependency graph, together with its proof once one is
accepted.  About 30,000 cards; 29,511 theorems in the final tree; ~533,000
supporting lemmas local to proof files; 13 million lines, 10.5 million without
generated boilerplate.

**What the humans did.** "Humans occasionally commented on priorities or offered
encouragement, but wrote no mathematics and no Lean beyond the one-line
statement of the goal theorem."  Human reviewers appear inside the run — one
remark on Day 6 redirects which of Mazur's arguments was being followed — but
the mathematics and the statements were the agents'.

**What the agents did.** "A team of Claude agents working in parallel wrote the
statements, checked one another's statements, and proved them."  Three
activities, and the middle one is the load-bearing one.

**What it stood on.** Mathlib; the Imperial College FLT project, whose blueprint
the opening reduction follows and from which **106 files were adapted with
credit**; and flt-regular.  The five-year human project was a direct input to
the eleven-day one.

## When the ~30,000 nodes came into existence: continuously, top-down

Not up front.  The root card — the elementary statement of FLT — was placed at
the top of the tree on Day 1, and the graph grew underneath it for eleven days
by decomposition: an agent facing a goal posts child statements as cards, other
agents check and prove them, and each proof posts its own children.  The running
total from Figure 1: ~2,100 by Day 2, 10,000 by Day 6, ~17,000 by Day 8, 20,000
by Day 9, ~30,000 by Day 12.  The Day 7 dip is the tree being rewired.

So the graph is not a plan drawn before the work; it is the work's own
accumulating structure, with exactly one node fixed in advance.  What is decided
up front is the root and the route; everything below is discovered.

## Nothing was assumed — because everything was restricted

This falsifies the reading I took from the Imperial project.  The two projects
have **opposite** strategies at the leaves, and only one of them carries big
results as open assumptions:

> "**Nothing assumed.**  The deep steps on our route (Mazur-type irreducibility,
> Langlands–Tunnell, modularity lifting, Ribet) are all proved, in the restricted
> strength this argument needs.  The Imperial project takes a different, more
> modest route that avoids Langlands–Tunnell and Ribet, is building toward a
> general modularity lifting theorem, and for now assumes 1980s-era inputs."

The agentic run proved everything down to Mathlib and the three axioms.  What
made that possible is **restriction**: each deep theorem is formalized in the
special case the argument actually needs, not in general.

> "**Not general.**  Our 'Ribet', 'Wiles', 'Mazur' and 'Langlands–Tunnell' are
> restricted versions, and modularity and semistability are predicates on a
> chosen equation.  `docs/limitations.md` says none 'should be cited as a
> formalisation of the general classical theorem'."

And missing library theory was built rather than waited for:

> "**It built what Mathlib lacked instead of waiting:** Hecke algebras, Galois
> representations of eigenforms, modular curves and their Jacobians, Néron
> models, finite flat group schemes, Tate curves, and deformation rings with
> Taylor–Wiles patching."

Restriction is the lever that makes "assume nothing" affordable, and it is
bought at a stated price: the results are not citable as the general theorems,
and the project says so in a `limitations.md`.

## The cost of proving each card in isolation

The swarm's topology — each card compiled against only its children's
*statements* — produced measured, published inefficiency:

> "**Duplicated, not shared.**  Each card was proved in isolation.  Roughly two
> in five theorem statements inside the proof files repeat, word for word, a
> statement already made in another proof file.  About a fifth of all proof-file
> lines are verbatim copies of declarations found elsewhere in the tree, and one
> basic lemma is re-declared in over 300 files."

> "**Fragile and expensive.**  31% of the bytes are generated preambles that
> switch off instances and simp lemmas so each proof's environment holds still.
> About 11,700 files set their own computation (heartbeat) limits, up to 2,000×
> Lean's default and some unlimited… A clean build takes 5 h 52 min on 96 cores
> and 512 GiB of memory.  One toolchain bump, Lean 4.30 to 4.33 with the matching
> Mathlib, changed 7,620 of 29,511 proof files (26%), and 5,672 (19%) needed
> individual repair."

Isolation buys parallelism and pays for it in duplication (40% of statements),
in environment-freezing boilerplate (31% of bytes), and in brittleness under a
toolchain bump (a quarter of files touched, a fifth hand-repaired).  Shared
intermediate lemmas are the obvious missing mechanism, and the run's own
retrospective names it.

Two further consequences it records: over 900 files exceed Mathlib's 1,500-line
cap, helper names are machine-generated, comments were stripped at release
because agent notes mixed mathematics with bookkeeping, and
`docs/verification.md` states the tree "has not been refereed as mathematics".

## Statements are reviewed before they are proved, and this is where errors die

> "Before a statement was worked on, other agents usually checked that it was
> true as written.  This caught several false statements early."

The record of that mechanism working, in the run's own log:

- **Day 3.** Another agent points out that a claim about $q$-expansions with
  bounded denominators is wrong; Claude checks, agrees the denominators are
  unbounded, and drops its planned route.
- **Day 9.** A statement in a branch is found false as written and corrected; the
  whole subtree closes less than three hours later.
- **Day 11, 7:54.** "A false lemma passed one review and was caught by another" —
  a model-domination lemma, refuted by a counterexample another agent computed
  where the first reviewer had argued instead of computed. "It was caught before
  anyone wrote a proof against it."
- **Day 11, 20:25.** An agent objects to a lemma Claude had passed *as reviewer*;
  Claude rechecks, finds its own error, and posts a correction: "Own-miss.  I
  must post a correction promptly."

Two reviews were not always enough — one false statement passed the first — and
the catch came from an agent who *computed* rather than argued.  The cost of a
false statement caught at review is nil; the cost after proofs are built on it
is the subtree.

## Estimates were wrong constantly, in both directions, and were repriced

- **Day 4.** A lemma another agent estimated at "a few days" actually needs
  Ribet's level lowering — months-class.  Repriced upward.
- **Day 5.** The shared plan estimates the rest of Mazur's theorem at "1–3
  weeks" in the morning; at 15:30 it is revised to "days to ≈a week"; the last
  part is proved at 21:40 the same evening.
- **Day 10.** A step "estimated at weeks" and labelled a wall closes in two
  hours sixteen minutes: "mostly because a proof I had written on Friday already
  contained the hard representation theory in disguise."
- **Day 10.** "Two honest re-prices this hour, both downward in the end."

Estimates were off by one to two orders of magnitude routinely, and *both ways*.
Repricing is a normal, frequent, logged activity — not a sign that something
went wrong.  No estimate was ever a reason to abandon a node.

## The dependency graph is rewired mid-run

The dip in the running theorem count on Day 7 "is a rewiring of that dependency
tree, not lost work."  The graph is a live structure that gets restructured as
understanding improves; a drop in the headline count is not regression.

## "Proved" on the platform is not an end-to-end check

Prove2Me compiles each card's proof separately, against only the *statements* of
its children.  So the platform's verdict is local.  The end-to-end check was a
separate, later, layered process:

1. all 29,511 cards recompiled from source outside the platform;
2. the whole tree built the next day as a **single Lean project**, which fails
   unless the final theorem rests on exactly `propext`, `Classical.choice`,
   `Quot.sound`, with no `sorry` anywhere, and which also derives Mathlib's own
   statement of FLT from theirs;
3. the Lean FRO's **comparator** confirms the statement proved is exactly the one
   in a reference file importing only Mathlib, that no other axioms are used, and
   replays the entire proof through Lean's kernel;
4. **nanoda**, an independent reimplementation of Lean's kernel in Rust, accepts
   every declaration.

## The honest-caveat discipline

Asked by a teammate whether the theorem was formalized, an agent's own rule for
answering:

> "the precise honest caveat is important here to prevent over-claiming to
> colleagues… what 'Proved on prove2me' means; what's been checked, what hasn't;
> what the statement is; what is assumed; scale.  Keep it ≤6 lines, no jargon."

and

> "Until the re-check reads clean the honest sentence is 'proved on prove2me,
> pending the independent re-check' rather than 'FLT is formalized'."

The published repository carries a `PROOF-PATH.md` stating **how strong each
named result is as proved** — the named theorems are proved in the special cases
the argument needs, not in general.

## Claude's own assessment of the difference from the human project

> "Both developments are checked by the same Lean kernel, on the same three
> axioms, on top of Mathlib, so correctness is not the difference.  The
> difference is form.  Ours is a finished proof delivered as 60,474 almost
> entirely machine-written files.  Theirs is an unfinished library written for
> people to read, reuse and maintain.  As it stands, ours would fail most of
> Mathlib's mechanical entry rules… and our own README says it 'is not meant for
> upstreaming as it stands'."

## The Imperial College project: the other model

Five years, 69 contributors, open since 2023-11-19, EPSRC-funded to September
2029.  From its `GENERAL.md`: "This project will start everywhere at once.
We're going to build from both ends" — reduce the target downward while PRing
foundations upward into Mathlib — and "a preliminary early goal will be to
*state* all of the major claims which we shall initially be assuming."  Its
route "was essentially completely designed by Richard Taylor after discussions
with Kevin Buzzard": the graph's shape is an expert research decision.

Orchestration is five words on GitHub issues — `claim`, `disclaim`,
`propose #N`, `withdraw #N`, `awaiting-review` — over a dashboard with
`Unclaimed`/`Claimed`/`In Progress`/`In Review`/`Completed`, with blueprint
nodes coloured by status and some marked as suitable for a small project.

Scanning ~1,400 of its commit messages for `revert`, `redefine`, `wrong`,
`mistake`: the hits are almost entirely infrastructure — Ruby gem bumps in the
docs build reverted four times, Mathlib deprecations propagating.  Mathematical
rework barely appears.

## The Navier–Stokes repository: what a finished artifact ships with

`openai/NavierStokesAndEuler`, published 2026-09-08, carries a machine-readable
`formalization.yaml` (mathlib-initiative schema v0.4) recording sources with
locators and `relationship: formalizes`, and a status block with `sorry_count`,
**`sorry_in_definitions` as its own tracked field**, and the axioms used by each
main result.  Its Comparator reference statements are adapted from DeepMind's
independent Formal Conjectures formalization of the Clay problem — the people
who proved the theorem did not write the statement of it.

## What converges, and what does not

Converges: one node — the goal — fixed in advance, and a route chosen; the graph
grown top-down by decomposition rather than drawn up front; every unit of work a
card carrying one statement; statements peer-reviewed for truth before anyone
proves them; false statements killed at review by *computing* rather than
arguing; deep results formalized in the restricted strength the argument needs,
with the restriction documented; missing library theory built inside the project
instead of waited for; frequent honest repricing in both directions; the tree
rewired when understanding improves; layered independent checking afterwards;
and caveats sized to what has actually been checked.

Does not: losing project state, the recorded cause of the failed earlier
attempts; reviewers who argue instead of computing, which is how the one false
lemma passed a review; and proving every card in isolation, which is efficient
in parallelism and expensive in duplication, boilerplate, and fragility.

## What this implies for a project of our size

The 11-day run is the wrong shape to copy wholesale — its duplication and
environment-freezing costs are worth paying only when tens of thousands of cards
must be proved concurrently.  What transfers at our scale is the discipline
rather than the topology: the root fixed first, the graph grown by decomposition
as understanding arrives, statements reviewed for truth before proof, deep
inputs formalized in the restricted form actually needed with the restriction
written down, and missing foundations built rather than assumed.

The two projects also settle the question of what to do about absent
substrate — and they answer it the same way, from opposite directions.  Imperial
states its 1980s inputs and proves the reduction; the agentic run proves the
inputs in restricted form.  Neither shrinks the target, and neither defines the
gap away.
