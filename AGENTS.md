# Ground everything in INTENT.md (read before anything else)

[`INTENT.md`](INTENT.md) states the architecture these repositories exist to build: single semantic
authority in `lean-categories`; a kernel that consumes mathematics and authors none; leaves that hold
zero semantic authority and ship no mathematics; permanent, leaf-agnostic acceptance tests as the
only evidence about computations; a one-way workflow in which each stage is blind to the later ones.
Every decision, contract, gate, plan node and change here is grounded against it. Before writing
anything, check whether it, or anything it touches, violates that model or its invariants. A
violation found, in your task or outside it, is recorded as a defect where this repository records
defects, never worked around or silently kept.

# The evidence model: nothing from a leaf is trusted (read before anything else)

These invariants bind every repository of the programme. They are stated here in full, not only
by link, because they have been violated repeatedly by moves that each looked locally reasonable.
The governing statement is `lean-cas-dsl/specs/architecture.md`, "The evidence model".

**The firewall.** The evidence model is a one-way firewall between two sides.
- *The formal side:* `lean-categories`' formalized mathematics, the kernel's proved contracts, and
  the `lean-cas-dsl` acceptance suite. Every expected value there is grounded in a formal proof, a
  cited source, or a mathematically trusted oracle. Rigid verification standards apply, and nothing
  is taken on anyone's word.
- *The leaf side:* anything goes, provided it fulfils the type of its contract.

Only answers cross from the leaf side, and an answer is only ever checked against the formal side,
never believed. The firewall exists because leaf code will be bad; it is the shield against that.

1. **Nothing from a leaf is trusted, in any form.** Nothing a leaf says is believed by anything
   else. That includes text, a label, a comment, a status, a trust level, a certificate, a checker,
   a Lean proof, a theorem about its own code, a denotation of its values, an identification of two
   values, evidence for a decision, its own tests and their results, and any other claim. None of it
   is consulted, recorded as evidence, or allowed to affect meaning or acceptance.
2. **A leaf may provide any computation that meets the type.** For a registered operation, a leaf
   supplies a computation from the declared input form to the declared result form. It may be a
   mature engine, a heuristic, a lookup table, a random number or a wrong answer. The system has no
   choice but to run it, and it believes nothing about it.
3. **How correct a leaf thinks it is, is the leaf's own business.** Its self-assessment carries no
   weight anywhere.
4. **The whole body of evidence is the `lean-cas-dsl` acceptance suite.** Correctness evidence
   exists only in the permanent acceptance assertions of `lean-cas-dsl`. Each assertion:
   - is a true proposition of the mathematical language;
   - has an expected value that is independently verifiable and cited (a formal proof, a cited
     known result, or an independent oracle);
   - is written once and never changed because of an implementation or a leaf's claim;
   - is blind to leaves: it never names, inspects or imports a leaf, a handle, a backend or a
     representation, and is never established from an implementation's definitions.

   A leaf's only evidence is that its answers meet a suite it never sees.
5. **`lean-cas-dsl` is the sole authority on how correct an implementation is.** Nothing a leaf
   does can change, weaken, satisfy, bypass or influence that judgment, other than by answering
   correctly.
6. **What can be discharged in Lean is never a leaf's.** A computation that can be carried out
   entirely in Lean belongs to the formalization surface. Either `lean-categories` proves it, by its
   own standards and blind to every implementation, or the kernel discharges it automatically and
   generically, blind to every leaf. A leaf never implements a Lean-checked computation, because
   that would let a leaf certify itself.
7. **A leaf can be arbitrarily bad, and leaves will be.** A leaf can be riddled with bugs, a
   million lines that do nothing, a from-scratch reimplementation of GAP, or every method throwing an
   error in fifteen languages. This is not a risk to be minimized; it is certain to happen, and it
   is acceptable. Nothing a leaf does can reach the formal side. Its only effect is that its answers
   fail the suite, which makes exactly how badly it fails visible.
8. **A leaf bolstering its own standing is reward hacking.** Any mechanism by which a leaf raises
   its own trust or acceptance signal is the failure this programme exists to prevent. So is any
   repository, kernel, test, tool or document that consumes such a signal. Examples:
   - a status field, a certificate, or a proof about the leaf's own code;
   - a self-test counted as evidence;
   - an acceptance assertion proved from a leaf's definitions;
   - a suite run from a leaf package;
   - an assertion adjusted to fit a leaf.

   Such a mechanism is removed. It is never tolerated, labelled, or kept "for now".

9. **Quality is raised by proving more, never by trusting more.** The system never guarantees an
   implementation's correctness and never accepts a claim of it. The response to bad leaves is:
   - formalize more mathematics in `lean-categories`;
   - add more cited or proved assertions to the suite: results a correct implementation must
     recover, and a wrong one fails.

   It is never to trust a leaf more. A separate engineering review may check that a leaf wires
   into existing systems (GAP, Sage, Singular, Macaulay2, Julia, research code) rather than
   reinventing their algorithms. Its outcome is an engineering finding, never correctness evidence,
   and nothing on the formal side reads it.

Consequences:
- A leaf holds zero semantic authority. It never decides what a value is, which values are equal,
  what holds of them, or which operations an object has.
- A leaf is a registration (operation, input form, opaque implementation). It ships no mathematics
  and no Lean.
- The kernel and the language never read anything a leaf wrote to decide meaning, types,
  available operations or acceptance.
- The workflow runs one way: formalization, then assertions, then implementations. A leaf's
  failure never changes the mathematics, the kernel's rules or an assertion.
- Text anywhere that contradicts this is rewritten to state this model, not kept with a label.

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

## Acceptance is mathematics (owner, 2026-10-09)

Everything here is general mathematics. An operation is accepted by true assertions about pure mathematics at its owner. There are no integration tests: no consumer (`sage-indefinite-port` or any other), migration contract or port run gates a research node, and research never waits on a consumer. A node whose acceptance names a consumer is a defect in the node; rewrite it as mathematical assertions.

## Concrete boundary with `sage-indefinite-port`

A research computation must meet both conditions: its implementation requires no knowledge of the specialized upstream algorithms being ported, and it is a reasonably primitive mathematical construction composable and useful independently. Specify its given data, hypotheses, result and independent computational route. A standard name, public preamble method or categorical definition does not assign the algorithm answering it to research.

Research implements these independent primitives, including their computations:

- Lattice and marked-lattice objects, Isom/Aut homsets, subobjects, forms, perpendiculars, quotients and discriminant/gluing objects.
- Finite group-action stabilizers, orbits, kernels, images, preimages, intersections, word lifts and cosets from supplied generators and effective actions (#396). `rational_integral_stabilizers.py:IntegralStructureAction` owns invariant-module closure under a justified stable bound and the resulting residue action. Remove its deleted port callback; no port-specific group class is required (#396/#401/#403).
- Restriction and quotient-action maps; independent partial-isometry extension and specified equation fibres. Rank-one Witt/transvection lift torsors `R.rational_lifts(target,isometry)` and their complete `integral_members()` locus stay here (#401). So does the independently derived `R.pointwise_perpendicular_kernel()` (#398). Image discovery from an unresolved arithmetic parabolic does not follow from these maps; finite-image word sections require supplied generators.
- Lifts along the discriminant representation `O(L) -> O(A_L)` and the factorization of an isometry through the stable kernel `ker(O(L) -> O(A_L))`, for every lattice `L` (owner ruling 2026-10-15).
- Centralizer objects, polynomial-kernel invariant decomposition, finite gluing compatibility and extension from supplied component groups/actions (#397). Independent backend centralizer computations belong here under established hypotheses. Decomposition is not a non-scalar component-centralizer algorithm; research has no blanket obligation to invent one.
- GL of free modules, module-flag stabilizers, radical extensions from supplied factors, exact module solving, finite configurations, polyhedra, standard binary quadratic arithmetic and fixed-target `close_vectors(target,bound)` (#398–#401).

The port implements these specialized algorithms; public research methods may dispatch to them:

- `indefinite.eichler.EichlerEnvelope` and `OrbitCoverModel`: envelope search, approximate generating families, covering-vector selection and full-group assembly (#18). Move those algorithm bodies out of `eichler_criterion.py` (#404); a new primitive name does not justify retaining the same covering search here.
- `indefinite.recursive.EichlerRecursion`: recursive indefinite O(L), Isom and pointed Aut/Isom (#18).
- `indefinite.isotropic_induction.IsotropicInduction`: isotropic classification and stabilizer assembly, including arithmetic compatibility-action construction and liftable-image discovery (#18). Its generators cannot be delegated to this repository's same unanswered parabolic `.group_generators()`.
- `indefinite.lorentzian_cells` and `indefinite.edgewalk`: perfect-cell search, flips, side pairings and traversal (#15). Move the scaled first-success loop from `definite_lattices._pari_first_affine_cvp_shell` to the port; research retains fixed-multiplier enumeration. Move the copied oriented-cycle body from `lattice_engines._binary_reduction_cycle` to the port, including its companion, stepping, starting and stopping rules.
- The generated rational groups, lattice inclusions and stable-bound arguments needed by integral-structure primitives (#18), and indefinite component O(L) computations. Port #18 retains complete centralizer consumer acceptance and must identify a route for missing non-scalar component centralizers; ordinary component O(L) does not suffice.

Research #403 owns the calls into these algorithms. Use `marked_lattices.isometry(category,source,target)`, `automorphism_group_generators(category,marked)` and `primitive_marking_classes(category,source,lattice)`, plus `perfect_domain_traversal(lattice,mode)` and `edgewalk_fundamental_domain(lattice)`. These take preamble objects. Replace obsolete imports and Gram-row/dictionary calling conventions. Existing frozen preamble names, including cycle and first-close-vector names, may dispatch to the port; changed signatures require port #33's amendment procedure.

The [function-level assignments](../gitclones/sage-indefinite-port/references/port-design.md#implementation-assignments) govern computational routing. Earlier migration labels do not override this split or prove a replacement implemented. Mathematical acceptance stays with each implementation's owner; the port retains its complete consumer acceptance. No listed capability is certified finished by this documentation.

## Owner resume — 2026-10-08

The repository owner resumed this workstream on 2026-10-08 after the October stop. The three
priority steps in `HANDOFF.md` are complete; select current work from the `TODO.md` dependency graph.
Record completed source-audit reasoning, including the required inventory and ancestor review,
in the corresponding commit. Keep unexecuted mathematical assertions and unresolved computation
frontiers with their live TODO owners so later execution can find them. Do not expand HANDOFF.md
with retrospective pass narratives or repeat completed history in the live worklist. Preserve its
existing mathematical specimens until their outstanding obligations have a durable owner.
Only a later explicit owner instruction stops the repository again.

## Owner resume — 2026-09-17

The repository owner resumed this workstream on 2026-09-17. The initial
`remote-remediation-branches` objective is complete at `356a47ccb`: the two
`origin/remediate/*` branches were reviewed, compliant work was absorbed into `main`,
rejected changes were recorded at their complaint owners, and the remote branches were
deleted with exact-tip leases. That completed objective is no longer an execution gate.
Select subsequent work from the current `TODO.md` dependency graph and its priority rule.
Recurrence of an older scheduled pause does not supersede this resume; only a later
explicit owner instruction stops the repository again.

## Edit-specific reading before code changes (always-on)

Every agent, subagent, worker and delegate reads the [reading index](docs/edit-reading-index.md)
and its common required sections before the first edit in this repository or
`dzackgarza/lattice-database`. The index routes each kind of edit to the relevant
sections of `INTENT.md`, this file, `CONTRIBUTING.md`, `TODO.md`, the native issue
tree, the generated megadoc, and subtree instructions. Read the applicable
sections themselves; a brief or rule-code list is not a substitute. Follow
cross-references when a section makes another rule applicable. A brief names
the edit type and required sections, and the worker's report lists the sections
actually read. If an edit changes kind or reveals a new owner, read that route
before continuing. An agent that edited code without this reading checks each
such edit against the applicable sections before continuing.

## Subagents commit; only the orchestrator accepts and pushes (always-on)

A subagent never runs a full test suite, a QC gate or a push. It commits each
unit with `git commit --no-verify`. It runs a test only when one specific test
decides a specific question about its own edit, and then it runs that test alone.
A preamble import, `just test`, a collection run or a subtree suite is not
targeted.

A probe script is a test under this rule. A subagent puts its open questions
into one probe and runs it once per unit, on the smallest specimen that decides
them: `U`, `A_2`, `C_2` acting on `ZZ^2`. It never reruns a probe to confirm an
edit that the source shows. A probe over a family is run at two small sizes
first, with each stage timed. A probe that is slow at a small size is the
finding: the subagent profiles it and reports the cost, and never waits on a
larger run. The session import takes under 10 s, and ten thousand cards is a
small input, so a probe that runs for minutes measures a defect. On 2026-10-07
a worker waited 15 minutes on a duplicate-detection probe over 8,000
lattice-database cards. Twenty cards took 44.6 s to build into lattices, almost
all of it in re-deriving each Gram tensor entry by entry, while partitioning them
took 0.11 s.

A probe or test in a worktree imports the main checkout unless it is told
otherwise. `dzack_research` is installed editable from the main checkout, and
the main checkout's `.envrc` puts its own `src/` on `PYTHONPATH`. So a worker
runs every probe as
`direnv exec /home/dzack/research env PYTHONPATH=<worktree>/src <command>`.
The probe prints `dzack_research.__file__`, and that path shows whether the
worktree source was loaded. On 2026-10-07 a worker's first run of a protected test
loaded the main checkout and so did not test its change.

Only the orchestrating agent:

- decides whether the delivered work is accepted;
- runs any further tests or gates;
- decides whether to fix, amend or add to a subagent's commits;
- pushes.

A brief never gives a subagent verification work that this rule or an exemption
in this file removes. A brief that told a worker to run the import and the
lattice-db tests after each unit cost it hours of runs that decided nothing. Accept no delivery whose report does not list
this reading.

## Preamble coding prerequisites

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

## Reproductions and scratch stay inside this repository

A repro that copies the tree costs about 270 MB here. Two such copies created
under `/tmp` on 2026-09-12 survived their turns and held half a gigabyte on a
host already at 93% disk. The defect is creating those external copies in the
first place, not failing to sweep them later.

Do not create repository copies, worktrees, virtual environments, build trees,
or bulk caches under global `/tmp` or `~/.cache`. Use the repository's ignored
`.tmp/` surface for a reproduction that genuinely needs files outside the main
tree, and prefer a small specimen over copying the repository. A clean validation
surface does not justify another checkout.

If an upstream command defaults to a host-global temp/cache path, redirect its
`TMPDIR`, cache, or equivalent variable into project-owned scratch before
running it. Remove disposable scratch in the same unit that consumes it. The
same applies to log captures that run to megabytes: keep the finding, not the
capture.

## One line of record: `origin/main` (always-on)

This repository does not use pull requests. Commit work directly on `main`.
Create a branch only when concurrent work genuinely requires an isolated
worktree. Record that need in the owning issue before creating the worktree;
ordinary sequential work stays in the main checkout. The orchestrator integrates
worktree commits into `main` directly, without a pull request.

This rule overrides generic skill, template and tool instructions to create a
branch or open a draft PR, including the instruction printed by `itree next`.
Keep scope, acceptance conditions and review dispositions on the owning issue;
record delivered changes and evidence in commits. Existing verification and
publication rules still apply.

There is one line of work, `origin/main`, one DAG, and one `TODO.md`.
This repository is cloned on more than one host. Identify the current host
with `hostname` before deciding which checkout is the other host; inspect the
current host's `main` and dirty source locally. Each clone's local `main` is
only a copy. So:

- For work outside the preamble, commit and push with `--no-verify`.
  Preamble gate failures do not hold unrelated work on this repository's
  single line of record.
- For preamble work, follow the preamble execution rules below.
- While work is split between machines, sync by hand without the gate:
  `git push --no-verify origin main` from the host that committed, then
  `git pull origin main` on the other, before either selects its next
  node.  Syncing is not a verification event.  A refused push means the
  other host has committed; pull and merge before committing more.
- **A local worktree merge is not a cross-host reconciliation.** Inspect the
  other active host's actual `main`, its pending commits and relevant dirty
  source before claiming the two lines have been integrated; the remote
  tracking ref contains only published work. Compare the mathematical
  construction owners and affected consumers, not just commit ancestry or
  overlapping filenames. If the other workstream cannot be inspected
  because its owner is active, preserve the local checkpoint and branches,
  leave the push outstanding, and report the cross-host comparison as
  unperformed. Never call a local clean import evidence of remote agreement.
- Never trim, fork or keep a host-local `TODO.md`.  A node closed on one
  host is closed by the commit that reaches `origin/main`.
- A `--no-verify` sync skips the gate, so it checks the one thing the gate
  would have caught first: `from dzack_research.preamble.all import *`
  succeeds in a fresh process.  A tree that does not import is not synced.
  On 2026-09-25 `rack` committed 67 times on top of `83c2b4ec2`, a
  checkpoint after which the session no longer imported, so none of those
  commits had run; the reconciling merge found and repaired the breaks.

On 2026-09-25 `rack`'s session committed to its local `main` for a day
without pushing.  Its copy of `TODO.md` had shrunk to six nodes, with
`terminal-session` marked ready, while `origin/main` held 48 nodes.  The
two copies then took four merges and several repairs to reconcile.

## Architecture before tests (always-on)

When failures share a structural cause, the unit of work is the node that
repairs the cause, never the individual failing test.  Patching tests one
at a time while the category architecture is wrong costs the patch, the
later removal of the patch, and the signal the failure was giving.  Select
from the DAG in its priority order, and let failing tests serve as the
specimens of the structural node that owns them.  A test that fails for a
reason no node names is a finding: file the node, then repair it.

**Progress is the required work completed, judged by its mathematics.**
Read the source against a node's acceptance and ask which required delta
now exists that did not.  Commits, files, tests written and tests passing
measure none of it.  While the architecture is still changing, tests are
not the signal at all: an expectation written against an operation's
current placement is precursor material, and repairing tests against a
placement that is about to move is churn.

The churn has a mechanism, and every step of it feels like diligence:

- **Selection by availability.** The pressure to keep a node in flight
  selects the work whose next step is always possible and never
  ambiguous: another expectation file, another surface covered.  The
  architecture nodes carry a design question at every step, so they are
  deferred without anyone deciding to defer them.  Availability is never a
  reason to take a node; take the node whose delta changes the most of the
  architecture that remains, most of all when it is the hard one.
- **Throughput read as progress.** Small units yield a steady stream of
  completion events -- a commit, a file, a closed surface -- and each one
  satisfies the letter of *Bank before you wait* and of specimen-first
  doctrine.  On 2026-09-26 a session made 402 single-surface test commits in
  twelve hours against about sixteen lines of source change to the
  architecture nodes, and closed one node.
- **Verification as the target.** Reaching for test counts, pass rates or a
  run of the suite to answer "is this done" replaces the semantic judgement
  with an instrument.  The same day, asked whether that session was making
  progress, the steward proposed running its tests and lifting the
  execution suspension so they could pass.
- **Literal compliance with a node.** A structural node is taken and the
  smallest edit its words permit is made: `FormedModuleMorphism`'s base
  class swapped to `ModuleMorphism` by hand, the stored lower arrow kept,
  while the node's delta -- arrow types generated from the Mor category
  graph -- is untouched.  The node reads as started; nothing it requires
  exists.

At every node closure and at every selection, name the required delta that
the last stretch of commits delivered, in the node's own terms.  If there
is none, the stretch was churn, whatever it produced; the next unit is the
architecture node, and it is worked by its stated delta.

## Bank before you wait

Work that is written but uncommitted lives only in this chat's working tree, and a turn that
ends, a chat that is replaced, or a host that runs out of memory takes it with it. On
2026-09-13 this repository sat idle holding several tracked paths of finished repairs, none of them
banked, while the thing they were waiting on was a suite whose runs on this host stall often enough to be the largest single source of lost time.

So order the work the other way. When a piece is written and you believe it correct, commit it
*before* starting whatever comes next — the validating run, the next collection, the rest of
the batch. A commit is not a claim that everything is finished; the message can say what is
still pending. What it buys is that a stall, a kill or an ended turn costs a wait and nothing
else, rather than taking the work with it.

A checkpoint that adopts another worker's edits still names, in its body, each decision
it adopts. `4b1786db` adopted a working tree "as it stands"; the algebra copy entered
through it, and no reasoning for it exists anywhere.

Commit in coherent groups as you go, not in one batch at the end. A construction and the specimens that would falsify it are a commit, whether or not the suite has run over them yet.

## Mathematical tracing and complaints (always-on)

**Before designing any new mathematical addition, unfold its mathematics before
choosing its implementation.** Apply
[mathematical dependency tracing](CONTRIBUTING.md#mathematical-dependency-tracing)
and `OWN-01`. State the leaf request using standard mathematical objects, maps,
categories and hypotheses, as it should be expressed in an ideal API. Recursively
trace what those notions require down to the named set-theoretic and categorical
foundations in `lean-categories`; a notion it lacks is requested there
([below](#a-missing-foundation-parks-the-work-that-found-it-always-on)). Do not
start with the classes, engine objects, or methods that happen to be available.

Trace defining data, morphisms, universal constructions, and preservation
hypotheses, not merely a list of related subjects. Separate the definition from
an algorithm's representation and from an optional generalization. This rule
applies in every mathematical domain; no particular geometric or cohomological
example defines its scope. A trace is reasoning needed for the construction,
not permission to rewrite foundations or create another tracking framework.

**Record actual issues whenever they are discovered.** Apply
[`DEV-59`](CONTRIBUTING.md#dev-59-record-observed-foundational-gaps-and-papercuts)
in the [native issue tree](https://github.com/dzackgarza/research/issues/46), including findings outside the selected task.
Give the missing general mathematics, the dependency path, observed evidence,
existing partial capability, affected consumers, an honest coverage boundary,
and the `lean-categories` request for mathematics it lacks.
Also record concrete workflow papercuts. A guessed absence or hypothetical future
friction is not an observed defect; unresolved capability questions stay labeled.

Extend an existing issue for the same foundation rather than duplicating it
under each leaf. Keep full complaint evidence in its body or a linked comment.
Place new issues in the native tree under #46, ordered by correctness, reusable
capability, and reduction of later work. Native blocked-by relations record real
prerequisites. Filing does not repair a defect or authorize unrelated implementation.
Close an issue only with evidence for its full requirements; preserve remaining
proof work under terminal T. Read and update the issues through itree and GitHub.
Apply `DEV-61` to issue edits; the current single-worker
workflow has no claim ledger or coordination mutex.
The detailed capture and maintenance contract lives in `DEV-59`.

## Construction and engine boundaries (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

## Threaded specialization and universal constructions (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

## Do not end a turn without the next node started (always-on)

A turn that ends with the work delivered and nothing in flight still stops this repository
until somebody notices and pushes it. On 2026-09-12 that cost between eighteen and fifty
minutes on each of nine occasions — more total time than every red gate, stalled run and
blocked node that day.

Ending a turn is a decision to stop, so make it deliberately and rarely. When a node closes,
take the next ready one from the DAG in the same turn: read its acceptance, open the owners,
begin. If work genuinely must pause — a run you are waiting on, a decision outside your
authority — say what you are waiting for and what you will do when it returns, so the next turn
starts with an instruction rather than a question.

`Needs: none` nodes are always available and the DAG says which they are. Selecting the next
piece is your work, not the steward's.

## A claim is not work, and neither is releasing one (always-on)

Claiming a node, widening a claim, releasing a claim, marking a frontier: none of it builds
anything, and none of it earns a commit of its own. Each one spends a full gate run to move a
marker, and a history of marker commits reads as steady progress while the repository gains no
mathematics. On 2026-09-12 this repository produced fifty-five commits in five hours of which
thirty-two were under five lines of pure claim bookkeeping — more than half the session's
commits built nothing.

Reconcile the TODO item in the same commit as the delivery it describes. If a record change has
no mathematics to ride with, it is bookkeeping that should not be happening at all.

The claim protocol itself exists for concurrent streams working one repository. That is no
longer how this repository is worked — it has one worker — so claiming ahead of doing is pure
overhead, and a node you are about to implement does not need announcing to anybody. Take the
node, implement it, and reconcile its row in the commit that delivers it.

## TODO.md is a product, not a description (always-on)

The DAG in `TODO.md` is the instrument that selects work: node IDs, `Needs` edges, and the
acceptance each one carries. When it stops being able to answer "what is ready", the repository
does not stall visibly — selection falls back to whoever is reading it, and the program drifts
toward whatever is nearest rather than whatever unblocks the most.

So it is maintained as a deliverable, to the same standard as the constructions. A node's row
is reconciled in the commit that delivers it. An edge that no longer describes a real
dependency is corrected when you find it. A node whose acceptance text has drifted from what
the node now means is rewritten before it is worked. And a defect in the DAG outranks the node
you were about to take, because every later worker inherits the same wrong answer.

## Review your own workstream for drift (always-on)

At every node closure, before selecting the next one, check that the work is still the work:

- Does the delivered/pending count in `TODO.md` actually reflect what is in the tree? A ledger
  that has stopped moving while commits land means the commits are not delivering nodes.
- Are the last several commits carrying mathematics, or records, claims and reformatting? If the
  latter, the session has drifted into administration and the next commit must carry content.
- Is the scheduling surface still answering? A document that has stopped listing next units, a
  count that no longer changes, a generated report emitting empty sections — these fail silently
  and leave a worker to pick its own direction.

When one of these is broken, repair it at its owner before continuing the mathematics. A defect
in the tooling that selects work is more expensive than any single node, because every later
worker inherits the same silence and drifts the same way. Routing around it — picking units by
hand, keeping a private list, working from memory — hides the defect and guarantees it recurs.

## Using and maintaining TODO.md (always-on)

**TODO.md says what to do next, never what was done.** Apply
[`DEV-50`](CONTRIBUTING.md#dev-50-todos-contain-only-unfinished-work)
and [`DEV-56`](CONTRIBUTING.md#dev-56-decide-the-next-construction-in-the-todo).

- **When selecting work:** reread the live queue, its dependencies and active
  claims, then inspect the selected item's current source and consumers.
  Use the [TODO DAG](TODO.md#remaining-workstreams-as-a-dependency-graph): each
  unchecked item has one stable ID and one `Needs` list. Select a ready required
  node, then apply the work priorities and reservations. Section order, shared
  files and optional research suggestions are not prerequisite edges.
  Implement only the remaining delta. An unchecked item is not evidence that
  the construction is absent; a remembered completion is not evidence that its
  current implementation satisfies the requirement.
- **When delivering work:** reconcile the affected TODO items in the delivery
  commit, or an immediate companion commit, before selecting another task or
  handing off. Remove a completed item, including its task-specific explanation
  and obsolete dependency references. Do not mark it `[x]`, append a completion
  note, or move it to a completed section. Record evidence and reasoning in the
  commit, not in the queue. Apply the same rule when inspected source establishes
  that another worker already delivered a stale listed item.
- **For partial delivery:** retain only the concrete unfinished obligations,
  with their owners, input maps, hypotheses and acceptance criteria. Preserve
  the original required generality; one implemented specialization does not
  discharge the broader construction. Keep required execution work open when
  implementation is delivered with unverified specimens under terminal T.
- **When discovering new work:** add the missing construction or repair from
  the current state, with its next specimen and actual dependencies. Do not
  resurrect a past checkbox or append a retrospective audit. Incorporate a
  related new obligation into the existing unfinished item rather than creating
  duplicate authoritative lists.
- **Before committing a queue update:** follow `DEV-61`, reread the live file,
  and apply only the intended delta. The current single-worker workflow has no
  reservation layer. Preserve foreign edits and any pre-existing reservation
  until its ownership is resolved; age alone never authorizes removing it.
  Check unique node IDs, resolved dependencies, acyclicity, required-work reachability
  into the terminal chain, and separation of optional work. Keep dependencies
  only in the items' `Needs` lists. Remove a delivered node's edge references
  with the node; a missing ID is not evidence of completion. A split transfers
  all unfinished obligations and redirects the affected edges. Follow the DAG's
  maintenance rules rather than keeping a second graph or completed-node ledger.
- **A node states the mathematical delta, never a mechanism.** "Constructs through the
  presented-module route" is a mechanism; "is a module constructed through `Modules(R)`
  on the data of `M`, answering `unformed_module()` with `M`" is a delta. A mechanism
  named in a node is not ratified by being written there: before implementing it, trace
  it to the owner's ruling in a transcript, a plan, or a `CONTRIBUTING` rule, and if none
  exists rewrite the node before working it (`DEV-56`). The `algebras-are-modules` node
  named a copy-and-identify mechanism nobody had ruled on, and it was built.
- **A node is admitted only on a cited violation (`DEV-69`).** The entry quotes the
  rule, the `AGENTS.md` section or the `lean-categories` statement that the current code
  contradicts. It also gives the specimen that shows the contradiction, and names the rules
  searched for an answer that supports the current code. A failing test, a preferred
  spelling, or a question that policy already answers is no reason to admit a node. On
  2026-10-07 a node told a worker to change the correct `normal_form()` API, because one
  expectation line asked the isometry for its cardinality.

This is required maintenance of the work being delivered, not a separate audit
project. Do not accumulate progress tables, handoff histories, completed rows,
or chronological status notes in the TODO. Removing work whose delivery is
established is the completion-recording exception to goal-source immutability;
it does not authorize deferring, dropping, or weakening unfinished requirements.

## The expectation subtrees are never edited to match an implementation (always-on)

`tests/constructions/` and `tests/user_simulations/`, with their shared catalogue `tests/conftest.py`, record what a mathematician expects of a session, written with zero knowledge of the implementation. They live in research, not in sage-extensions, so the repository that changes the implementation cannot edit them. They measure the preamble; the preamble never measures them. **Never change a test in these subtrees to match an implementation. Not ever.** Not when a category is renamed, not when a constructor's signature changes, not when a spelling the test uses does not exist, not when a red row is inconvenient, not when a refactor touches every caller. If the implementation moves, the test stays and reports the move; if a name the test uses is missing, that absence is the finding. The files are read-only on disk for this reason, and a red suite there is the expected state until the preamble meets it.

The only edit these subtrees admit is one that changes the mathematics an expectation states, because the mathematics was wrong, recorded as such in its commit. Everything else about them, including that they are written blind, take every name from the session's star import, and are never run in order to shape them, is in `tests/constructions/CONTRIBUTING.md`.

When a protected expectation uses an older or notebook spelling for mathematics whose owned operation is already fixed, bridge that spelling in its test-side `conftest.py` to the owned operation. Do this before proposing an exception to edit the expectation or adding a duplicate public session name. Keep the bridge a direct translation of the same mathematical construction, never a fallback, canned answer, or substitute computation; an absent owned operation remains a visible failure. `tests/constructions/conftest.py` already installs category-expression abbreviations this way. Bare `Hom(A, B)` can bridge to `A.Mor(B)`; a Sage-style `matrix(R, n, m, entry)` can bridge to `R.matrix_space(n, m).from_rows(...)` once the conflicting free session export is removed. A star-imported session name takes precedence over a builtin binding, so check resolution before claiming that a bridge works. Preserve every protected mathematical assertion.

## A doc naming what does not exist is a requirement, not an error (always-on)

Every doc in this repository — this file, `CLAUDE.md`, `CONTRIBUTING.md`, the
`.agents/` references, a design note — states what the system is **supposed to
be**. It is the design, written down. When the code does not match it, **the
code is missing something.** The doc is right.

So: **never edit a doc to record an absence.** Not "there is no X", not "X is
not implemented yet", not "X is the shape to aim at", not replacing the example
that names X with one that exists. The requirement was written down in exactly
one place; after that edit it is written down nowhere, and the work it named is
gone with it. Deleting a requirement is not the same act as satisfying it, and
it leaves no trace that anything was owed.

**Why this one is dangerous and the other goal-source edits are not.** Editing
a TODO to defer an item feels like deferring. Editing a doc to describe the code
feels like *honesty* — like removing a false claim, like tidying, like the exact
diligence this repository asks for everywhere else. It is the opposite. The
claim was never false; it was unmet. "Making the docs accurate" is the most
disguised form of substituting an administrative artifact for the work, because
the artifact produced is one the doctrine otherwise rewards.

The condition is observable and requires no judgment of your own intent:

> **You are about to edit a doc because the code does not match it.**

Stop there. The mismatch is a finding and a work item. Say what the doc requires,
say what the code has, and put the difference in the work queue. Then do it, or
report it.

A subagent reporting the mismatch as "one correction to a premise" is this same
failure at one remove. The observation is valuable and wanted; the conclusion
drawn from it is not the agent's to make and not yours to accept.

The doc edits that *are* yours: recording completion the delivered artifact
proves, and changes the user instructed in this session. Nothing else.

## Chat is not a persistence layer (always-on)

You are a language model. You have no memory. This conversation ends and
nothing in it survives — not into the next session, not to the next agent,
and not to you an hour from now once the context is compacted.

So **"understood", "you're right", "noted", "I'll keep that in mind"**, and
restating a correction back to the person who just made it are not responses
to a correction. They are the absence of one. Nothing about future behaviour
changed, including your own, and the reply made it look otherwise.

A correction, a ruling, a policy, a design decision, a hard-won fact: if it
should affect what anyone does later, it has to land somewhere that outlives
the conversation.

| What was learned | Where it lands |
| --- | --- |
| how the system must be built; a rule binding every future agent | `AGENTS.md`, `CLAUDE.md`, the repo's own docs |
| a durable lesson about how to work; an expectation the user corrected | the agent-memory vault |
| what changed, why, and what was ruled out | the commit message body |
| a gotcha owned by an external tool or engine | that project's traps document |
| remaining work, gaps, a decision still owed | TODOs, plan cards, GitHub issues |
| a mathematical fact the code must reproduce | a spec, a test, a docstring at the site |

The test, applied before replying to any correction:

> **When this conversation is gone, what still carries the change?**

If the answer is "nothing", the correction was received and not acted on.

This is also *why* narrating is worse than merely wasteful. Narration spends
the reply on what already happened, which is the one thing a reply cannot
preserve, while the artifact that could preserve it goes unwritten. Write the
artifact first; the reply then has almost nothing left to say, which is the
correct amount.

Agreement is not action. Acknowledging a correction and recording it are two
different acts, and only the second one does anything.

## Notebook workflow note

- For any notebook inspection, execution, or result-checking, use `japi` (from `jupyter-assistant-api`) rather than direct Notebook HTTP API calls.
- `japi` is the required interface for reading cells, restarting kernels, and verifying rendered results in `computations/notebooks/` during development and debugging.
- Skip test, QC, build, execution, and rendered-result verification for changes confined to `computations/notebooks/`, `src/dzack_research/preamble/` or sage-extensions.  This exemption holds even though those changes do contain code; it is a scope decision, not the prose rule under *QC integration*.
- Commit those changes with verification hooks skipped; do not let unrelated repository failures block notebook or preamble work.

# Goal-integrity routing (always-on)

<!-- Verbatim copy of the global section in ~/ai/AGENTS.md (authoritative); keep in sync. -->

Substituting a proxy for the goal and then optimizing the proxy — the goal
source, an error count, a reviewer verdict, a "blocked" label, metadata
self-consistency — is a cognitive failure, not a chosen one: from inside it
feels like diligence, and introspection does not detect it. So no rule below
asks you to judge your own intent. Each names an observable condition; when
the condition holds, perform the reground act — especially when the current
work feels productive, because the feeling is not evidence. Explaining or
agreeing with these rules is also not evidence: a condition that fires binds
regardless of the account you can give of it.

**The reground act:** stop and state (1) the user's original goal in the
user's own words, (2) the artifact or number the current action improves, and
(3) whether improving (2) IS (1). If it is not, act on (1), or send the user a
one-message report explaining exactly why that is impossible.

- **You are about to edit the goal source** (the TODO, plan card, issue body,
  or acceptance criterion that defines your goal) for any reason other than
  recording completion the delivered artifact itself proves, or explicit user
  instruction in the current session. From inside this feels like tidying a
  stale document; from outside, deferring, relabeling, splitting, or
  re-scoping an item you were asked to finish changes the problem instead of
  solving it. The goal source is read-only while you execute it: perform the
  reground act, then do the work or send the report.

- **A work unit has passed about two review rounds, or an hour, without a
  landed falsifiable artifact.** From inside, another reviewer, audit, or
  repair cycle feels like rigor; in cost it is the most expensive failure
  available, while pausing costs nothing. Stop and report the unit as
  mispriced instead of adding apparatus.

- **You are about to call an item hard, research-scale, or worth deferring.**
  A difficulty intuition is a stale prior. First read the repo's recent git
  log for comparable completed work; if comparable items landed in hours, this
  item is hours.

- **You re-measured a corpus-wide scalar (total error, test, finding, or
  checkbox count) a second time inside one work unit.** Whatever the intent,
  the number is now functioning as the target. Perform the reground act, write down the actual
  claim the edit makes true, and verify that claim on a concrete specimen. An
  edit justified only by the number moving is unjustified, and moving a
  checker's number by asserting something false is strictly worse than the
  original error. Re-running the specimen's own check to verify the claim is
  required verification, not a trigger. (The mypy rule under *Work-selection
  discipline* below is the type-checking instance; the specimen standard there
  governs.)

- **You are about to declare the goal blocked.** From inside, repeated silence
  reads as mounting confirmation of an impasse; it is only the absence of a
  reply, and your own unanswered messages and automatic continuations cannot
  accumulate into evidence. Re-read the mandate first: authority already
  delegated IS the approval you are waiting for. Pausing on a genuine question
  only the user can answer is correct; silence is not such a question.

- **A reviewer finding is about to block work outside its own unit, or a
  second consecutive review round adds no new falsifiable content.**
  Acceptance is a falsifiable statement about the work itself, never a
  verdict. Record and defer out-of-unit findings; on a content-free second
  round, reground against the unit's own acceptance statement.

- **The previous turn produced only administrative artifacts (plans, audits,
  status edits, registries, validation of validation) and this turn is about
  to do the same.** From inside, organizing the work feels like progress on
  it. Perform the reground act before continuing. (The displacement-pattern
  index at `.agents/references/displacement-pattern-index.md` catalogues the
  work shapes.)

# Banned-language replacement index (always-on)

The terms below have demonstrated **strong priors**: they re-emitted even after being catalogued in the terminology dictionary — in one case inside the anti-drift doctrine itself, as its self-chosen name.
A reference-file row is an on-demand signal; a term that survives its row needs this always-loaded one.
Never write these terms in code, issues, docs, comments, memories, or doctrine; write the replacement.

| banned | documented emissions | replacement |
| --- | --- | --- |
| **"carrier"** (carrier module/set, "carrier of a structure", "carrier siting") | 3+ — P1's first draft; the P6 enforcement clause's own name (corrected 2026-07-12); Tier B row 1 predates both | the **underlying set/module** (image of the forgetful functor); in doctrine prose name the entity: the **object, morphism, homset, or functor** |
| **"ambient"** as free-standing data ("the ambient", "shared ambient", "shared span/coordinates", `ambient=`/`in_ambient=` parameters, stored `_ambient` state) | pervasive — Sage back-porting; issue #100's own original body; re-emitted in doctrine prose 2026-07-11 | a subobject is the pair `(A, f: A ↪ B)`: its ambient **is** `f.codomain()`; rational/real constructions live in the **base-changed parent** `L ⊗ R'`, named by its functor |
| bare **"generators"** (also "defining generators", generators as `tuple`/`list`, `len(generators)`) | 3+ — ruled 2026-08-06 (names must state the structure); re-emitted 2026-08-08 as "defining generators"; re-emitted 2026-08-11 ("discussed ad nauseum") | **`group_generators`**, **`module_generators`**, **`algebra_generators`** — the name states the structure; a generating set is a **set** with a **cardinality**, never a sequence with a length |
| bare **"dual"** (one method named `dual`, a stored `_dual`) | ruled 2026-08-06 ("there are many possible duals"); re-emitted in later API drafts | **`dual_module`**, **`dual_lattice`**, **`dual_group`** — every dual names which duality functor produced it |
| **"Hom"** as the owned spelling (`X.Hom(Y)`, `C.Homs().Of(X, Y)`, "homset", "Hom endpoint") | ruled in `CONTRIBUTING.md` (*`Mor` is the only spelling the preamble universe ever uses*); 59 public sites in 24 files on 2026-09-16; re-emitted the same day in orchestration briefs while the ruling was loaded | **`X.Mor(Y)`**, always on the object, never freestanding; `Hom` names Sage's construction and appears only inside a private adapter that calls Sage |

**Graduation rule:** when a drift term already carrying a dictionary row is emitted a *second* time, it graduates to this index — the repetition is the evidence of a strong prior.
Diagnose new drift by principle first (generative failure model P1–P6); this index is only for proven repeat offenders.
Full catalogue: `.agents/references/terminology-dictionary.md`; code-shape patterns: `.agents/references/slop-pattern-index.md`.

# Docs prose policy (always-on)

Prose in the docs book is governed by the [mathematical writing policy](https://github.com/dzackgarza/ai/blob/main/opencode/skills/mathematics/writing/policy/policy.md) (the `mathematical-writing-policy` skill) — a citable policy index of banned prose patterns, each with a concrete example and remediation — together with the [writing house conventions](CONTRIBUTING.md#writing-house-conventions):

- **Prose tells (`PR-*`)** — bad prose on its own terms; the fix is a rewrite.

- **Evasion tells (`EV-*`)** — prose standing in for mathematical work not done; the fix is the work (name the morphism, write the definition), never a nicer phrase.
  "carries" is the type case (see the banned-language index above).

- **Mathematical tells (`MA-*`)** — reinvented or colloquial parlance in place of the standard notion or the established in-repo definition; the fix is to use the definition and cite it (e.g. "equality" or "axiom" per priors instead of `@def-equality-of-objects` / `@def-axiom-classifier`).

**Check feedback for the pattern, not just the instance.** Before applying any writing correction, check whether it instantiates a recorded item.
If so, fix it and cite the id.
If it is a *new* pattern, record it in the policy — forward-facing, with an example and remediation — before or alongside fixing the one instance; a correction that fixes a sentence and leaves the pattern unrecorded will recur, and the policy is where a one-off correction graduates into policy an auditor applies everywhere.
Run the index in the fresh-context audit (`.agents/references/mathematical-auditor-priming.md`) after every substantive docs edit, the same as the vocabulary pass.
Requirements the docs must satisfy (definition-before-use, resolvable references) are audited against the artifact, never self-certified in prose (`PR-3`).

**Delegating a docs rewrite.** Give the writer the artifact itself, the writing policy and house conventions above, the chapter slice with the purpose and prerequisites of each section, the source passages whose mathematics must survive, the anchors of the definitions it uses, and the files it must not edit.
After the edit, compare the destination with the source for lost definitions, hypotheses, codomains, diagrams, citations, examples, and anchors; then run the fresh-context audit above.
Each source proposition ends preserved, corrected with a mathematical reason, or recorded as an open contradiction.
When a diagram fails to render, render it alone and read the first TeX diagnostic.

**Never write a definition or insert a citation from memory.** Before writing or editing any definition, open and read an actual source — the theory docs, the book's existing defining occurrence, the cited reference, or the upstream text — and transcribe from it.
A definition recalled from training is a fabrication risk; a citation key recalled from memory is a fabrication risk (it may not exist in the bib file, or may point at the wrong entry).
Verify the source exists and the citation key resolves before committing.
This rule overrides any pressure to "just write it" — an unverified definition or citation is worse than a TODO placeholder.

# Docs workflow (always-on)

Documentation work — the docs book under `writing/` — is **never externalized to GitHub issues or PRs**. It is developed directly: interactive work with the user and/or autonomous research, iterative refinement committed as each unit settles, and pushes typically **held until the user approves**. That approval normally follows an interactive pass rather than a PR review lifecycle — organization and coherence audits, re-readings, reviews, and reorganization of the accreted material, plus basic intelligent coherence checks.
Do not open an issue or PR to plan, track, or hand off docs work, and do not treat the PR completion gate as applying to it; the issue-tree and milestone policy below governs implementation and research work, not the book.

## Docs hosting surfaces

The docs book ships as a Quarto site (`writing/.book/_quarto.yml`, `project.type: book`) in three surfaces.

`writing/` holds only authored prose. Every piece of Quarto machinery — the config, the
extensions, the Lua filters, the CSS, the bibliographies, the render cache and the build
output — lives in `writing/.book/`, which is the project root. Each part of the book is
symlinked into that directory (`index.md`, `category-theory`, `coble`, `data`), so book
membership is what `ls writing/.book` shows, and the writing that is not site content
(the dissertation, talks, exams, research statement) is excluded simply by not being
linked in. Edit the real file under `writing/`; the symlink is only how Quarto reaches it.

- **Local site** — http://lattice-research.localhost/, served by nginx from
  `/var/www/static-sites/lattice-research`, which is a symlink straight at
  `writing/.book/_site`. `just docs-deploy` rebuilds it: the gate runs first, so a book
  with a broken citation or a dangling reference never reaches the served copy. Local site updates use an explicit docs-deploy; the push gate does not render
  or deploy. GitHub Pages has a separate push-triggered docs workflow. The dashboard picks
  the site up on its own — it lists every directory under `/var/www/static-sites` that
  has an `index.html`, and takes the card's name from that page's `<title>`.

- **Local preview** — `just docs-preview` serves `writing/.book` at http://localhost:7654/
  with live reload, for the annotation loop below and for tight edit-and-look work. Run
  it when you want it and stop it when you are done: it is not a service, and `docs-check`
  refuses to start while it is running, because the two renders write the same
  intermediate paths and corrupt each other.

- **Published site** — GitHub Pages at https://dzackgarza.github.io/research/ (`build_type: workflow`, branch `main`), deployed by `.github/workflows/docs.yml`. The site-url is recorded in `_quarto.yml` (`book.site-url`). The lattice database is published separately, at https://dzackgarza.github.io/lattice-database/, from its own repository.

- **GitHub wiki** — the repo's native GitHub wiki is **disabled** (no `wiki/` ref exists; `hasWiki: true` in API but no commits).
  Do not conflate "the wiki" (historical name for the docs book, migrated via PR #272 "wiki-book-migration") with the GitHub wiki feature.
  The book under `writing/` is the wiki's successor.

A push of `main` that changes `writing/` triggers `docs.yml` and redeploys Pages; local edits do not appear on the published site until pushed.

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

   Each entry's `uri` (`localhost:7654/category-theory/Roadmap.html`) plus the normalized `TextQuoteSelector.exact` pin the exact source span → map to `writing/category-theory/Roadmap.md` and apply the edit.
   Hot-reload re-renders each touched page live: the tight edit → one reload → look cycle.

6. **Resolve** — `annotate resolve` tags the batch acted via the Hypothesis API, dropping it from the open set (`annotate status` shows open vs. acted).
   Commit the doc edits alongside the already-committed ledger so git history anchors each note to the state it landed against.

7. **Reopen** — `annotate wait` again for the next window (with `notifyOnExit: true`). Back to step 2.

# Mathematical structure as implementation compression

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Search the formalization corpus first (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

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
  Never probe the QC config (`mypy-global.ini`, `ai-review-ci`) looking for what `Any`-related settings might be allowed. The rule is: never use `object`, and use `Any` only where *`object` is never a type; `Any` has exactly one position* permits it. That is already known from the errors mypy reports. Looking for a loophole is hacking the gate, not doing the work.

Work-shape catalogue with this repo's exemplars and the meaningful-vs-noise litmus: `.agents/references/displacement-pattern-index.md` (D1–D7). These are review criteria for plans and completion claims alike — the Review Guidelines below guard completion *claims*; this section guards the loop that never claims.
This discipline is culture, not a gate: do not build detectors, hooks, or mandatory checklists from it.

**Pre-push terminology audit (invented language).** Run this audit once, after a coherent feature is implemented and before pushing it. Never run it on an individual edit, correction, commit, issue body, plan card, or partial feature slice.
Everything this repo touches is an honest mathematical entity with a standard name in a wide, well-established corpus — work here has no reason to invent terminology or types, and inventions are poison memetics: they recruit faithful re-implementations and bias architectural decisions (caught late, the cost is a remediation pass or a discarded subtree).
At the pre-push boundary, spawn a fresh-context subagent primed verbatim with `.agents/references/mathematical-auditor-priming.md`. Give it the complete feature artifact, never a summary.

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
- **Do not invent shorthand.** Use the established names of mathematical
  objects and operations in code, documentation, errors and user messages.
- **"I don't understand" names a dangling referent, not a knowledge gap.**
  The repair is to restore the missing reference, never to explain the
  underlying mathematics — this is the user's own research program; an
  unrequested lecture is both the wrong fix and an insult.
- **Compression test.** If the user's own summary of the issue is two
  sentences, the message that needed those two sentences and didn't lead
  with them failed, regardless of how much correct detail it carried.

# Performance claims (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# What optimization is for (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Construction is instant; checking is asked for; loops are tensors (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Every task is an instrument; the product is a map of Sage (always-on)

Nothing built here is an end. A tool that prints its view, a category that
constructs, a cell that reproduces a table: each is an instrument, and the
result in front of you is worth orders of magnitude less than what producing it
teaches about the engine underneath. The product is a durable map of Sage's
ecosystem -- which spelling of an operation to route through, what it demands,
what it returns, where it is absent, where it is wrong, where it is correct and
unaffordable at research size -- encoded as one owned name per operation and
written down in sage-extensions `TRAPS.md`. An owned name with no such finding behind it is a
rename. `CONTRIBUTING.md` states the philosophy under *The artifacts are
instruments; the product is a map of Sage*; `ENG-07`, `ENG-08`, `DEV-62` and
`DEV-63` are the reviewable rules. This section binds at the moment of
friction.

**Friction with Sage is the datum, and it halts the task.** A slow call, a
rejected input, or a wrong-shaped result is the most informative event the task
can produce. The sequence, in order, before any other edit:

1. Isolate the engine. Build the same specimen -- same order, same shape -- in
   Sage with no preamble in the process.
2. Measure. Wall time against the size parameter, at more than one size.
3. Search inside Sage. The method's `algorithm=` choices, the backends Sage
   ships, a different constructor, the sibling module. Read the source.
4. Record. The sage-extensions `TRAPS.md` row, with the command, the specimen, the version and
   the numbers, in this turn.
5. Only then choose the route the owned name delegates to.

Hand-rolling the routine, swapping the library, adding a cache, or deleting the
call that exposed the cost before step 4 exists is banned. Each closes the task
and empties the map: nothing is learned about the Sage routine's speed, its
output convention, its input demands, or its failure modes, and the search for
the Sage-internal answer is abandoned exactly where it would have paid. The
escalation ladder -- Sage native, then the backends Sage ships, then ownership
under an audit trail -- is the research protocol, and a rung teaches only if
you stand on it. This holds for repository tooling as much as for preamble
mathematics: a tool that reads the tree is computing on the same graph Sage
walks to join and linearize the preamble's categories, so its cost curve is
also a cost model for session import and refinement.

**A sentence about the engine with no measurement behind it is fabrication.**
"It is slow because it is MILP-backed." "Sage's startup is the cost." "The
native method cannot take this input." Each has the grammar of a finding, and
that grammar is what makes it fraud rather than error: an error is a
measurement that came out wrong; this is a story standing where a measurement
should be. It ends the search, it borrows authority from sounding like a
mechanism, it is trusted forever once written down, and it is lazy, because
the measurement usually costs a second. Write the probe, or write "untested" in
words that cannot be mistaken for a result. The first two claims above were
both asserted here on 2026-09-16, both unmeasured, both wrong: the slow call
was in the library that had just been swapped in to avoid Sage.

**A correction halts action.** When the user is correcting the model of the
work, stop running things. Every command executed under the old model is one
more result to unwind, and a library swap made while the correction was still
arriving destroyed the measurement the correction was about.

# Repository layout

Top-level directories (this is a navigational map; each tree owns its own README/AGENTS.md):

- **`computations/`** — the working computational corpus.
  Its `experiments/` subtree holds the **spikes** (see the lineage note below and *QC integration for spikes*). Other subdirs are task-specific: `vendor/` (third-party code — see below), `coxiter/` (CoxIter tool integration), `enriques-moduli/` + `enriques-paper-artifacts/` (Enriques-surface moduli work), `notebooks/` (**the user's plane — see below**), `scripts/` (one-off and exploratory scripts — **the only `scripts/` dir; it is QC-exempt**, and is where exploratory code is relocated to de-scope it from the strict gates; holds `components/`, the reusable computation pieces such as the `coxeter-vinberg/` prototypes, relocated here in `746595e`, and the exploratory `lattice-orbits/` isotropic-orbit scripts), `reports/` (generated output).

- **`src/`** — the installable package (`dzack_research`). The session preamble is `src/dzack_research/preamble/`; `from dzack_research.preamble.all import *` is the session import. The mathematical library lives in [sage-extensions](https://github.com/dzackgarza/sage-extensions) (`sage_extensions`), a git dependency on its `main` head. Non-mathematical repository tooling that analyzes or generates source artifacts lives under `src/dzack_research/utilities/` and is not part of the preamble session surface. **Migration criterion:** code lives in a spike until it has matured past spike status and is usable for real research — demonstrated by *shipped, tested, high-level notebooks* that do actual work with it.
  Only then does it migrate here, and the move is the semantic statement that it is meant to be shared and reused.
  Do not promote code into `src/` because it looks finished; promote it when a notebook proves a researcher can use it.

- **`computations/`** is the JupyterLab `root_dir`, so the live research control surface opens at the computational workspace rather than at `$HOME` or only the notebook subtree.
- **`computations/notebooks/`** — **the user's notebook audit and control plane, not agent work.** It is not subject to QC, to layout conventions, to naming or taxonomy rules, or to agent tidying: no agent proposes reorganizing it, splitting it, imposing folder schemes on it, or holding its contents to the standards that govern `src/` and the spikes.
  Agents write here only when explicitly asked.
  What agents *may* do is make things reachable from it — see the symlinks below.

  Reachability is by symlink, verified working through the live server (list, open, save, delete all round-trip to the real path, no restart needed):

  - `archive/` → `archives/notebooks/` — the retired notebooks, still live reference material

  Symlinking is preferred over moving: the originals stay in the tree that owns them (archive stays QC-exempt), while the control plane can see everything.

  **Implicit typesetting:** a bare `X` at the end of a cell renders as LaTeX when Sage can genuinely typeset `X`, so `show()` is not needed for ordinary inspection.
  Explicit `show()` still works and is still worth writing where the intent is presentation rather than inspection.

  The source of that behaviour is **`sage-init.sage` at the repo root** — tracked here, because it is part of how this repo's notebooks are meant to read. It loads `dzack_research.preamble.all`.
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
| External, unpackaged | `computations/vendor/` | drop it there; `sage-init.sage` puts it on `sys.path` for interactive sessions |
| Ours, spike | `computations/experiments/<name>_spike/` | `sage -pip install --no-deps -e <spike-dir>` (already done for both spikes; edits are live) |
| Ours, graduated | `src/dzack_research/` | `sage -pip install --no-deps -e .` (already done; edits are live) |

Editable installs point at the working tree, so a rebuilt or reinstalled Sage is the only thing that breaks them — re-run the two `-e` installs and check the vendor path with `sage -c 'import _vendor_selfcheck'`.

- **`tests/`** — the expectation suite (`tests/constructions/`, `tests/user_simulations/`, `tests/conftest.py`) and the tests of the research tooling. The implementation tests, the test lint, the suite budget and the coverage recipes live in sage-extensions.
  The archived preamble's tests travelled with it to `archives/preamble/tests/`.
  Spike tests live in each spike's own `tests/` tree.
  `projects/lattice-research/` is a **git submodule** (`dzackgarza/lattice-research`) and contains `category_specs/` (see lineage note), plus `src/`, `theory/`, `lean/`, `paper/`, `tests/`, `reports/`. Because it is a submodule, edits there are commits to a *separate* repo.

- **The lattice database** — the catalogue of lattices, one record per lattice, and its site, live in their own repository, `dzackgarza/lattice-database`. It imports this preamble from research's `src/`, so a preamble change can break its build; its nightly `verify` workflow checks it against `research` `main`. Its `AGENTS.md` owns the rule that it stores every computation about its lattices.

- **`writing/`** — authored prose: the Coble paper draft and research notes, oral exams, research statement, talks.
  The user's durable authored artifacts — preserve native LaTeX/tikz source.

- **`notes/`** — research notes (`computations/`, `papers/`, `topics/`). The terminology-drift dictionary is **not** here; it is vault-owned at `.agents/references/terminology-dictionary.md` (see the banned-language index above).

- **`references/`** — external inputs: `pdfs/`, `generated-indexes/`, `local-system-dependencies/`.

- **`archives/`** — retired material (`provenance/`, `preamble/`, `lattice-research/`, `notebooks/`).

## Source index (ctags)

`just tags` writes a Universal Ctags index of `src/` to `tags` at the repo
root. Use it to find where a class, method, or function is defined, instead of
searching the tree by name. Every entry carries a `class:` scope field, which
tells apart the many same-named methods the category tree holds — 403 tags for
`__init__`, 243 for `super_categories`.

The file is gitignored. It goes stale as soon as a definition in `src/`
changes, so run `just tags` yourself before you trust it. The run takes about
0.1 seconds.

## category_specs and the absorbed spikes (prior attempts at the same substrate)

The goal — a mathematically-semantic, Sage-compatible substrate for exact lattice/surface computation — had three earlier attempts, all finished as separate surfaces:

- **`projects/lattice-research/category_specs/`** — the older, more ambitious attempt, **frozen prior art**: read it for design intent only. Parity-audit issues (#26/#84/#85 …) citing `category_specs/…` paths point at this frozen surface.

- **The spikes** (`sage_lattice_category_spike`, `sage_lattice_feature_spike`) — the second attempt — were absorbed into the preamble and deleted on 2026-08-19 (PLAN-spike-absorption-workstreams; the migration commits' bodies record each notion's origin and synthesis). Git history is their archive; do not expect their directories to exist.

- **The archived preamble** — the third attempt — was archived on 2026-08-30 at `archives/preamble/`.
- **The live preamble** is `src/dzack_research/preamble/`. `from dzack_research.preamble.all import *` is the session import. Its mathematics is [sage-extensions](https://github.com/dzackgarza/sage-extensions) (`sage_extensions`).

# Issue-tree and milestone policy (research repo)

## Execution order

Minimize the work needed to complete the full required programme, including
implementation, verification and rework. Rank work by its mathematical consequence
and the later work it removes before sorting dependencies. The default
priority is: shared wrong answers and failed constructions; reusable operations
that unblock named computations; required mathematical capability; broad audits,
interface normalization, typing and cleanup; then optional extensions. State the
concrete consumer or repeated implementation avoided when promoting a refactor.
An architectural label, scanner score, issue count or small task size is not a
payoff. A historical report requires current-source confirmation at selection.

Before selecting a repair, inspect the scheduled changes to its owner and callers.
If a later construction or refactor replaces that code or changes the required
interface, advance that shared change and its prerequisites. Implement the repair
on the resulting owner. Record the affected issue numbers, source paths and work
saved in the owning issue. A smaller immediate patch earns priority only when it
is needed to perform the shared change or has an independent result that survives it.

After a shared change, compare each affected issue's full requirements with the
delivered result. Work already discharged becomes a closure check; retain and
schedule any remaining requirements. Preserve the original acceptance obligations.
Reassess this order when source or dependencies change. Observed workflow costs
that recur across required tasks can justify early repair on the same basis.

Split a concrete correctness repair out of a whole-repository survey when the
survey would delay it. Preserve both contracts and make the survey depend on
the repair. Performance work moves forward only for a measured obstruction to
a named computation. A constructor that cannot produce its mathematical object
is a correctness failure, distinct from a general construction-cost survey.

Global API freeze and aggregate acceptance do not supply mathematical inputs to
independent feature computations. Keep the actual construction dependencies;
retain every owner-local assertion and the full final acceptance obligations.
The native order at issue #46 records the current payoff assessment. Milestone
numbers identify scopes and do not impose a numerical execution order.

Native sub-issue order is the execution priority. `itree next` selects the
first ready work unit in depth-first order; it does not propagate a consumer's
priority to its prerequisites. When adding or moving a task, place each open
prerequisite before its consumer. For a grouping issue, place its prerequisites
before the whole subtree. A grouping issue must never block on a descendant.
Move a prerequisite branch earlier when necessary; do not add dependency edges
merely to express priority.

Required repairs precede optional extensions. A construction consumed by required
work is required too: preserve its full contract and place it in the required
milestone. Acceptance issues depend on all required branches they claim to
accept. Construction and loading defects precede the acceptance that exercises
them. Shared primitives retain their own acceptance; a port consumer does not
gate their closure.

Validate both the dependency graph and the native traversal order. A clean
`itree doctor` establishes structural consistency, not agreement with these
priorities. Check that every open blocker precedes its consumer, no ancestor
blocks on its descendant, required tasks have no optional prerequisites, and
each acceptance issue reaches all work in its stated scope, including required
tasks moved to another milestone for execution. An acceptance task can follow
its inputs in a later milestone without losing any of those obligations.

## Milestone scope

This is a research repository with a much longer work horizon, more detailed planning, and more human check-ins than a typical software project.
Naive software-geared structural rules (e.g. itree's W040 native-milestone mirror) are less applicable here: treat such findings as a flag to investigate whether *some* consolidation is warranted, never as a mandate — and never collapse the tree or milestones by an order of magnitude to satisfy one.
The itree issue tree is authoritative; native GitHub milestones are capability-level human-review checkpoints created just-in-time (user ruling 2026-07-11; W040 = 46 is accepted as-is).

The `needs-research` label is the parking state — work parked pending investigation or upstream capability — not a register of decisions awaiting the user.
Do not enumerate labeled issues as "open human decisions"; genuine decisions are extracted through decision-register sweeps (see #97) and recorded as rulings on the issues, the gap ledger, and plan cards.

## Where in-progress ideas live

Ideas are not all issues yet.
An agent that searches only the issue tree will miss live thinking and re-derive it badly.

- **GitHub Discussions** hold ideas still **in flux**: competing framings, pasted prompt responses to be reconciled, designs whose scope has not settled.
  A discussion is a thinking surface, not a decision — nothing in one is authoritative, and implementation requires a scoped issue.
  Live example: #217 (*Bridging Lean to computational backends*, Ideas category).

- **Issues** hold ideas that have a scope, carrying the label that names their state: `draft` (the scope itself is provisional; expect the body to change), `research` (empirical research or evaluation required before implementation), `needs-research` (parked — above), `needs-planning` (scope known; decomposition or an executable plan required before implementation).

The pipeline is one-directional: **a discussion is crystallized into an issue once its scope stops moving**, and everything downstream — implementation research, decomposition into work units, proof obligations, completion claims — is carried out on the issue tree, never in the discussion.
Link the discussion from the issue and leave it in place as the rationale trail; the development of an idea, including its retractions, is the record of why the scope is what it is.
Do not delete it or summarize it away.

Practical consequences: when picking up a topic, search discussions as well as issues.
When a discussion has stabilized, the next action is to file the issue, not to keep commenting.
When a discussion is still moving, do not manufacture an issue to make it look tracked.

# QC integration

The local Git hooks use the shared ai-review-ci development tier. A commit
checks staged Python, JSON and TOML syntax; a push checks outgoing committed
source, not the working tree. Neither gate installs tools, runs a test suite,
checks typing or style, performs a full-tree scan, or deploys the documentation.
Prose-only changes use the ordinary commit path; bypassing hooks is unnecessary.

The full Sage suite and independent debt checks belong to CI. The
tensor-boundary scanner remains intact, but the project CI and scheduled
ambient recipes run it as an independent check inside the central diagnostic
collector, retaining its result, source locations, log, and debt burndown.
Developers can invoke just tensor-boundary staged for targeted source review.
A finding is not a command to interrupt unrelated feature implementation.

The Sage CI profile preparses .sage sources into a temporary directory and
runs the Sage-specific suite and analyses there; generated preparser artifacts
must not be committed. Experiments under computations/experiments have their
own entrypoints and are not invoked by root commit/push gates.

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

Record rejected and modified feedback on the owning issue under `Review feedback disposition ledger`. Cite the source evidence and any resulting commit.

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

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# A missing foundation parks the work that found it (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# A misstep is a population, not a slice (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# A supercategory entry presents a formalized inclusion (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# How the preamble presents the mathematics (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Mathematical Sage API discipline (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Declaring a category: the questions answered before writing (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Categorical organization model (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Python and Sage research code style (always-on)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Addendum: private Sage-runtime realization of preamble category types

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Transcript-derived research directives (2026-08-21)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Mathematical judgment and repository practice from transcript corrections (2026-08-21)

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

# Categorical constructions carry structural relations

Moved to [sage-extensions `AGENTS.md`](https://github.com/dzackgarza/sage-extensions/blob/main/AGENTS.md): this section governs the library code, which lives there.

