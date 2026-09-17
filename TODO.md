# Preamble TODO

## Execution priorities

Build the remaining general scheme-theory toolkit from the current `src/dzack_research/preamble/` tree.
Complete shared mathematical dependencies before extending their consumers.
Geometry has priority over independent arithmetic applications; an arithmetic computation moves earlier only when a named geometric construction needs its result.

This is an executable work list, not a record of past work.
Remove an item when its stated work is delivered; retain only its unfinished obligations if delivery is partial.
Completion evidence belongs in the implementation commit and its mathematical specimens.
Do not append completed rows, release histories, audit transcripts, or an overall-progress table.

The requirements below specify new deltas from existing constructions.
A source path identifies where to extend or repair, not an instruction to recreate that subsystem.
Inspect the live constructor and its consumers before editing.
Uncertainty explicitly assigned to a source review is not a claim of a runtime failure.
The pending terminal verification applies to the entire implementation, including constructions no longer listed as implementation work.

Follow [CONTRIBUTING.md](CONTRIBUTING.md), especially `DEV-50` through `DEV-59`. Begin new additions with its [mathematical dependency trace](CONTRIBUTING.md#mathematical-dependency-tracing), before selecting an implementation.
Record observed missing foundations and papercuts in [COMPLAINTS.md](COMPLAINTS.md), including independent discoveries.
That file owns the observed need and evidence; this queue owns the selected remaining repair and its acceptance.
Link them instead of copying status.
The [design philosophy](CONTRIBUTING.md#preamble-design-philosophy) and [architecture specification](CONTRIBUTING.md#preamble-architecture-specification) govern how every item is implemented, including already-existing dependencies.
The intended result is one recursively owned mathematical language composed from shared constructions and maintained computations, not a larger local CAS. Read the generated `docs/preamble-megadoc.md` before preamble implementation under the governing `AGENTS.md` prerequisites.
This queue does not authorize running preamble tests, QC, Sage, or notebooks before terminal T.

### Select from the live dependency graph

The queue is the scheduling surface.
Recompute the ready frontier from the current rows before selecting work; do not preserve dated frontier counts or a private list of what was ready in an earlier turn:

```sh
grep -nE '^- \[[ x]\] \*\*`[a-z0-9-]+`\*\*\. \*\*Needs:\*\*' TODO.md
```

Take the ready frontier in dependency order and carry each selected node through delivery before moving on.
A node that closes unblocks its dependents; a node that merely grows does not.
This repository has one worker, so selection has no claim or reservation layer.

### Contents

- [Execution decisions](#execution-decisions-for-every-item)

- [Workstreams](#workstreams) and [dependencies](#remaining-workstreams-as-a-dependency-graph)

- [Completion and local algebra](#completion-and-local-algebra)

- [Construction contracts](#architecture-before-dependent-implementation)

- [Covering families and sheaves](#covering-families-and-sheaves)

- [Divisors and relative geometry](#divisors-and-relative-geometry)

- [Cohomology and equivariance](#cohomology-and-equivariance)

- [Families and singularities](#families-and-singularities)

- [Geometric research applications](#geometric-research-applications)

- [Arithmetic and reflection geometry](#arithmetic-and-reflection-geometry)

- [Framework transfer and organization](#framework-transfer-and-organization)

- [Complaint-driven architecture remediation](#complaint-driven-architecture-remediation)

- [Final verification](#final-verification)

- [Optional research consumers](#optional-research-consumers)

### Execution decisions for every item

Apply these decisions inside the selected unfinished item, not in a separate audit, readiness registry, or new planning system.
Their durable authority is `OWN-01` through `OWN-14` and `DEV-50` through `DEV-59` in CONTRIBUTING.

1. **Select a remaining mathematical delta.** First express the requested addition in standard mathematics and recursively unfold its dependencies through the source-backed set-theoretic and categorical foundations.
   Separate defining mathematics from computational choices and related extensions.
   Then read the live owner, its immediate structure, the complete relevant methods, and its callers before changing it.
   Record actual gaps under `DEV-59`, linking the complaint to the relevant repair rather than using a missing method name as the mathematical specification.
   Preserve supplied capabilities.
   A source-review task below is a question to settle, not an assertion that the whole subsystem is broken.
   If the current source already meets it, remove the stale task with source evidence in the commit; retain terminal-T execution where still owed (`DEV-50`, `OWN-12`).

2. **Decide the route before adding computation.** Name the sanctioned entrypoint, defining objects and maps, reusable owned operations, and private computation owner in the selected item's contract.
   Use the existing declaration for the durable result (`OWN-02`, `OWN-13`). An owner path in this queue is a place to inspect, not permission to call every importable factory or private method.
   For a specialization, name the actual general construction it inherits or contains and the operations delegated to it (`OWN-14`). A shared name or an isomorphic result does not establish that implementation relationship.

3. **Resolve the actual upstream capability question.** Read the applicable maintained operation's input and result contract, including representatives, maps, hypotheses, and precision.
   Record the selected operation and remaining integration in the item while it is open, then at the adapter declaration.
   Where this queue names candidates, selection is unresolved work, not license to implement the computation from scratch (`OWN-08`, `ENG-06`).

4. **Repair one prerequisite with its real consumer.** Missing inherited data, constructor recursion, inaccessible maps, or awkward engine output belong at the owner that should provide them.
   Complete that repair and route the selected consumer through it; do not create a consumer-specific substitute or prebuild unrelated foundations.
   The first release includes an actual mathematical construction, not just an abstract interface (`OWN-03`, `OWN-07`, `OWN-11`).

5. **Preserve the full public object.** Retain coefficients, component modules, indexing objects, actions, maps, representatives, and results of subsequent arithmetic as owned mathematics.
   Transport through the existing functors with their preservation hypotheses.
   A new wrapper, accessor, category label, or private helper does not discharge these obligations (`OWN-04` through `OWN-09`).

6. **Close against construction and computation together.** Read the complete selected route and affected alternative routes, including inherited methods, notation, catalogue construction, and raising.
   Deliver distinguishing mathematical specimens and the required consumer changes.
   Commit specimens unexecuted until T. Neither matching dimensions nor replacing a local loop with a lower-level library call establishes architectural completion (`OWN-12`).

When work changes direction, use the relevant decision below immediately:

| Observable choice in the current task | Decision already made; next action |
| --- | --- |
| A missing method looks like new mathematics | Unfold the requested mathematics first; then search the owned category, structural functors, and maintained implementations. Separate missing exposure, missing transport, and missing computation; record the observed gap and repair its mathematical owner (`OWN-01`, `OWN-08`, `DEV-59`). |
| A foundational gap or papercut appears outside the selected item | Record the observed need and dependency path in COMPLAINTS, with inspected scope and existing partial capability. Link any existing repair item; do not suppress the finding or silently expand the current task (`DEV-59`). |
| A package does not implement the Python class model | Evaluate its concrete computation separately. Generic compilation belongs to `sage-categories`; inability to compile classes does not reject CAP, Sage, or Julia mathematics (`OWN-01`). |
| An engine supplies invariants but the task needs maps | Inspect its representative/presentation operations and established compositions. Keep the map obligation open; do not replace it with a freely chosen space of the same dimension (`OWN-07`). |
| Lowering and raising call each other recursively | Separate computed defining data from the request to compute it at the common owner. Preserve one constructor contract; do not introduce a trusted or unchecked route (`OWN-02`, `OWN-07`). |
| A bridge or dependency is unavailable | Identify the existing bridge or package owner and exact missing capability. Repair that boundary within scope or report it. No new direct engine-to-engine connection or local replacement algorithm is implied (`OWN-08`, `OWN-11`). |
| A generic helper still contains the old bespoke algorithm | Compare the semantic operation with maintained upstream operations. Moving code between files, languages, or repositories is not computational delegation (`OWN-08`). |
| A finite window or a specialized theorem gives the expected answer | Preserve the original object, range, coefficient domain, and comparison hypotheses. Completion is not a quotient; a resolution prefix is not a resolution; a rational answer does not contain integral torsion (`OWN-09`, `OWN-10`). |
| A specialized object has its own general maps or diagram operations | Locate its inherited or composed general construction and delegate those operations. Remove duplicated authority as part of the affected repair; attaching metadata or comparing answers does not establish threading (`OWN-14`). |
| Equality, zero, or membership is not decidable by the selected representation | Preserve the mathematical object and use the declared computational frontier. No guessed boolean, infinite equality loop, or weakened codomain (`DEV-51`, `DEV-52`, `OWN-10`). |
| A review finds the same bypass in another consumer | Repair the shared owner and all consumers depending on that changed contract in the unit; add only independently remaining repairs to their existing items. Renaming the bypass is not resolution (`OWN-11`). |
| An item appears finished because code, a report, or a passing invariant exists | Compare its full construction, maps, recursive ownership, and maintained computation against the source. Remove only delivered obligations; preserve unexecuted proof work under T (`DEV-50`, `OWN-12`). |

These routes address the integration errors discussed in the [sage-categories complaints](https://github.com/dzackgarza/sage-categories/blob/main/COMPLAINTS.md) without importing their historical findings as current preamble defects.
Read the relevant upstream contract at selection; a package catalogue is a discovery lead, not evidence that every coefficient regime or map is implemented.

### Workstreams

Select a concrete unchecked construction below, not an entire row.
Scores follow [COMPLEXITY.md](COMPLEXITY.md); they measure the responsibility for the named boundary, not its line count or duration.
Reassess a bounded implementation once its input contracts are settled.

| Work | Required input | Next mathematical output | Complexity and reason |
| --- | --- | --- | --- |
| Completion and local algebra | Existing ring, ideal, localization, presentation, diagram, and scalar-change owners | One localization construction for its special cases; completion with maintained series realization and distinct finite stages | 90: exactness and representation decisions propagate into formal geometry |
| Construction contracts | Existing category/Hom/construction framework | Sanctioned entrypoints, recursive ownership, and construction-order independence across affected constructors | 90: shared runtime and mathematical identity |
| Covering families and sheaves | Existing affine charts, localization maps, and finite scheme gluing | Descent across distinct chart rings, refinement comparisons, and sheaf operations | 85: common descent contract for all non-affine consumers |
| Divisors and relative geometry | Sheaf descent and supported local algebra | Non-toric and relative divisor/section/intersection constructions | 65: several geometric theories share maps and hypotheses |
| Cohomology and equivariance | Existing complexes, derived module operations, geometry and actions | Shared complex/DGA computation routes and toric boundary repair, then geometric functors and equivariant comparisons | 75: topology, variance, and comparison hypotheses |
| Families and singularities | Completion for formal tasks; sheaves and local criteria for other tasks | DVR families, formal models, relative invariants, and local systems | 75: compatibility and distinct algebraic/formal/analytic meanings |
| Geometric research applications | Specific cover, divisor, cohomology, and lattice inputs | ADE log pairs and the K3/Enriques workflows below | 65: source-defined applications of shared constructions |
| Arithmetic and reflection geometry | Existing lattice, group-action, discriminant, and exact engine owners | Remaining transporters, higher-order centralizers, parabolics and reduction complexes | 85: completeness and witness construction in infinite groups |
| Framework transfer and organization | Each subsystem's complete upstream dependency | One surviving mathematical owner with usable inherited operations | 90: shared ownership and cross-framework transfer |
| Complaint-driven architecture remediation | Current owned preamble plus the unresolved source-level findings in `COMPLAINTS.md` | Converged construction data, owner API, categorical representations, computation boundaries, public types, notebook/session vocabulary, and proof-sensitive tests | 95: cross-cutting source repair whose ordering matters because later API/test/notebook work must consume the corrected owners rather than compatibility residue |
| T | All required implementation, integration, source consolidation, and complaint-driven architecture remediation below | Executed mathematical evidence and repairs of the failures it exposes | 15 for execution; score each resulting repair at its actual owner |

### Remaining workstreams as a dependency graph

The executable DAG is defined by the unchecked items below, not by the workstream table or section order.
Each item begins with a unique stable mathematical ID and a **Needs** list of immediate unfinished prerequisites.
`A` in `B`'s Needs means the edge `A -> B`: deliver A's required output before completing B. `none` means no unfinished queue prerequisite, not no mathematical foundations.
Existing constructions and external input contracts remain in the item's body; inspect them at selection.
All listed prerequisites are conjunctive.

Keep this one edge source.
Do not maintain another hand-written graph, status table or dependency registry.
A visualization, if needed, is generated from the items.
Cross-references explain requirements; they do not create extra edges.
If prose requires an unfinished output, reflect it in Needs or explicitly place the mutually dependent obligations in one coherent node.
Do not conceal cycles behind words such as "with", "later", or "integration".

Select a node with no remaining prerequisites, subject to the existing geometry priority and active file reservations.
Priority is a preference among ready nodes, not an edge.
File conflicts, shared owners, and related mathematical subjects are not dependency edges either.
Completion does not block ordinary geometry that does not use it; an unrelated arithmetic gap does not block geometry.
Repair a newly discovered prerequisite at its owner and record the actual dependency before extending its consumer.

An edge names the output described by its prerequisite's acceptance contract.
When only an independently deliverable part is needed, split that concrete output into its own node, transfer its obligations intact, and redirect only the affected edges.
Do not force a consumer to await an entire broad workstream.
Do not remove an edge because its prerequisite is inconvenient, deferred, or merely represented by a class.
The generic universal-construction node delivers real module constructions first; completion then owns integrating that contract with its ideal-power system and maintained series realization.
The general construction does not wait for completion's implementation.

Before committing a queue change, check that every checkbox has exactly one ID and one Needs list, IDs are unique, all references resolve, and there is no self-edge or cycle. Required pre-T implementation nodes must feed the terminal chain that verifies them. Complaint-driven remediation opened after the first terminal pass must feed `architecture-remediation`, then `terminal-session`, so the repaired source is re-exercised before post-remediation audits. During terminal execution, newly exposed repairs must reach the still-open terminal node whose acceptance requires them.
The terminal nodes form their own final chain.
No required or terminal node may depend on an optional node.
Optional work must name its concrete consumer and dependencies before implementation; a required engine repair belongs in the required consumer's dependency path, never in the optional branch.

Remove a delivered node and its incoming/outgoing edge references in the same queue transaction, after inspecting the delivered output.
Preserve unfinished residue under its ID, or split it without dropping any obligation.
An absent ID is never an implicit completion record: dangling references are errors to reconcile against source and git evidence.
Keep completed history in commits.
Repairs and re-execution within terminal verification do not create a back-edge to an earlier terminal node.
New failure-specific work becomes a prerequisite of the still-open terminal repair or final-verification node, with the required re-execution in its acceptance.
Preserve the phase-T execution rules.

## Completion and local algebra

Paths in this section are relative to `src/dzack_research/preamble/categories/`.

### Localization specializations through one construction

### Completion objects and finite approximations

### Local algebra extensions

## Architecture before dependent implementation

These are targeted remaining contracts and preservation obligations, not a restart of the module/algebra/action constructions.

### Shared diagrams and universal constructions

### Constructor and ownership convergence

## Covering families and sheaves

**Integration route for this workstream:** the covering-family owner constructs the geometric descent datum; local kernels, cokernels, tensor products, restriction, and scalar change use the existing module/algebra owners.
At the first unsupported local computation, determine whether its established Sage/Singular module operation or the applicable CAP module-presentation operation supplies the needed maps.
Repair that adapter once.
Research a sheaf-level package for the specified geometric category when it can supply a larger operation; do not assume a finite-category presheaf package computes arbitrary scheme sheaves.
Keep the exact missing comparison or descent datum with the item that requires it (`OWN-08`, `OWN-09`, `DEV-56`).

## Divisors and relative geometry

**Integration decisions:** products and intersections enter the existing diagram, algebra pushout, quotient, and gluing constructions.
Divisor and line-bundle operations enter their owned groups and sheaf functors, not a scheme-specific matrix layer.
For each selected non-toric regime, inspect the applicable maintained Singular/Macaulay2/OSCAR operation for class relations, sections, Rees algebras, saturation, or intersection data, with its hypotheses and returned maps.
The unanswered question is which full operation supplies the chosen specimen, not whether these theories should be reimplemented here.
Retain existing fan/subdivision and toric-divisor engines for the toric cases.
Do not make an engine's affine or toric specialization the public definition of the more general construction (`OWN-01`, `OWN-08`, `OWN-09`).

## Cohomology and equivariance

### Shared complex and DGA integration

### Toric integration before geometric extensions

### Geometric and equivariant extensions

## Families and singularities

**Integration route:** construct a family through the scheme slice; its fibers and coefficient changes use the existing pullback and scalar-change functors.
Formal consumers use the completed object and its inverse system, never their own precision parameter as a defining equation.
Local classification uses the existing singularity/normalization adapters.
Before implementing a new local recognition rule, identify the maintained algorithm for the specified equivalence relation and whether it returns coordinate maps.
For analytic comparisons, monodromy and nearby/vanishing cycles, identify the precise source construction and available implementation first; names shared with algebraic operations do not establish a comparison or authorize a substitute (`OWN-08`, `OWN-09`).

## Geometric research applications

**Release boundary:** these are research consumers of the preceding shared constructions.
Their local contribution is the source-specified geometric data and composition of existing functors/maps.
Any missing section, quotient, cohomology, or lattice operation returns to its named dependency owner; the application must not introduce a private copy.
Before each application release, trace its nonidentity maps back through those owners.
An expected lattice, signature, dimension, or classification label is a comparison specimen, not the definition of the computed geometric result (`OWN-01`, `OWN-09`, `OWN-12`).

## Arithmetic and reflection geometry

Arithmetic work follows geometry except for an explicitly named geometric dependency.
Reuse the current orthogonal groups, subgroup constructions, finite-quotient splitting, involution centralizers, lattice loci, configuration lifting, and height-bounded enumeration; extend only the missing regimes specified below.

**Computation decision for each selected arithmetic item:** inspect the current private lattice/group adapters and the relevant `sage-indefinite-port`, OSCAR/Hecke, GAP, or polyhedral operation for the exact requested witnesses and completeness regime.
State whether it supplies existence, a transporter, an orbit representative, or a complete classification; keep those outputs distinct.
Assemble subgroup, action, quotient and gluing data through their existing owned constructors.
Do not rebuild a lattice/group algorithm because its output needs an owned morphism, and do not move a bespoke algorithm to an external-language script and call it delegated.
If an actual algorithmic gap remains, name it and apply `ENG-06` before implementation.
Bridge repairs and codec additions belong at the existing bridge owner, not in an arithmetic consumer (`OWN-07`, `OWN-08`).

## Framework transfer and organization

### Organization findings

## Final verification

### Testing is deferred until every other item is done (always-on)

The terminal-T rule is defined by `DEV-58` in [CONTRIBUTING.md](CONTRIBUTING.md).
Write falsifying mathematical specimens with implementation and commit them unverified.
Do not execute them during the preceding workstreams.
Optional research consumers below do not delay T.

The source-conformance and integration obligations above are required work, not optional engine improvements.
A feature's numerical implementation can already exist while its construction or encapsulation still needs repair.
Deliver and review those source changes before T; T executes the mathematical evidence and repairs what it exposes.
It is not a reason to postpone source-level ownership review until every downstream consumer has copied the same bypass.

### Terminal T was entered; complaint remediation has reopened required source work

The repository already entered terminal T; `terminal-reference`, `terminal-execution` and `terminal-repairs` are delivered, and the evidence they established is in their delivery commits.  The later source audit in `COMPLAINTS.md`, however, found mandatory architectural violations that were not represented in the old DAG.  Those findings are now promoted into the required [complaint-driven architecture remediation](#complaint-driven-architecture-remediation) workstream below.

The phase rule therefore applies again while `architecture-remediation` is open: do not use Sage/tests/QC/notebooks to drive source authoring in that workstream.  Bank the corrected constructions and the specimens that will falsify them, then return to terminal execution.  The prior terminal evidence is not discarded, but it cannot certify source that changed afterward.

`terminal-session` is the re-entry boundary.  It depends on the delivered `terminal-repairs` work and on the `architecture-remediation` convergence node.  Once both hold, regenerate the live reference/graph as needed, execute the final public session/notebook surface, and run the prescribed final QC against the repaired architecture.

This keeps the two roles distinct: source-level architecture remediation is driven by the observed construction contract, while terminal execution decides whether the repaired public mathematics actually works.  Do not use a previously green terminal run to waive a newly observed source defect, and do not use an architectural audit finding as if it were already a runtime failure.

### The sage-categories pin is unresolvable, and the cause is in that repository

`pyproject.toml` pins `sage-categories @ git+https://github.com/dzackgarza/sage-categories.git@66efc15bf5050a527f1bb4ff3bff8542e3d83203`. That revision exists locally and is an ancestor of the producer's active `codex/functorial-core-kernel` branch, but it is not on any published `origin/*` ref.
Reverified 2026-09-14: local `main` and `origin/main` are both `10e14a53`; the active producer branch is `5660e01a`, **1577 commits ahead of `origin/main`**, and no remote branch contains the required `66efc15b` revision.
So the resolution failure `terminal-execution` recorded is not a defect in this repository and cannot be repaired from here by choosing another local producer revision; the required producer history has not been published to the GitHub route this dependency declares.

Do not work around it by switching to a filesystem path dependency.
That hides a publication gap that affects every consumer, and the declared route between these projects is GitHub.
Treat the pin as blocked, record it that way against the affected items in the observed failure set, and carry on with the 36 collection errors, which are this repository's own and are repairable here.

- [ ] **`terminal-session`**. **Needs:** `architecture-remediation`, `research-sage-runtime`. Verify the required session/rendered examples and final contribution contracts after mathematical integration and complaint-driven architecture convergence.
  **Goal:** Exercise the repaired preamble as a coherent live Sage mathematical session: import the public category/lattice language, regenerate its derived views, inspect research examples, and run final QC.
  **Fresh-session invariant:** before this node can close, a fresh live Sage process on the repository's active environment must execute `from dzack_research.preamble.all import *` successfully and expose at least the core `Cat` and `Lattices` entry points.
  Regenerate the preamble megadoc/graph from that same tree and require the JSON/megadoc inventory to agree with the live session; graph node counts are an inventory, not acceptance by themselves.
  Treat a preamble-owned import warning or an import-order-dependent result as a terminal repair, not as harmless startup noise.
  Re-run this smoke after terminal repairs that touch category/bootstrap, exports, or session initialization so a previously green import cannot silently regress.
  **Deliver:** actual inspected notebook/rendering results where relevant, source-backed terminology review at the required push boundary, and the repository's prescribed final QC. **Acceptance:** the public star import and live graph/session invariant above hold; the displayed mathematical objects and maps are correct; no output is certified solely by a generated file, a graph count, or a server starting.
  Respect the user's push approval and active-task scope.

## Complaint-driven architecture remediation

The 2026-09-15 audit in [COMPLAINTS.md](COMPLAINTS.md) found twenty systematic violations of the normative architecture plus two concrete workflow/environment papercuts.  Those observations are evidence, not an execution plan; this section is the one scheduling surface for repairing them.  The foundational nodes below are required source work; the workflow nodes repair prerequisites of that work or its terminal execution.  When a node is delivered, remove the corresponding resolved complaint evidence in the same commit rather than appending a status line to the complaint.

The audit counts are discovery measurements, not acceptance thresholds.  A node closes when the mathematical owner and affected consumers are correct, not when a grep count reaches zero.  Conversely, a broad node must inspect the complete occurrence family named by its complaint before closure; fixing only the representative example is not enough.

### Workflow and execution prerequisites

- [ ] **`research-sage-runtime`**. **Needs:** `architecture-remediation`.
  **Goal:** Restore the repository’s stable Sage execution environment so the final mathematical session and `.sage` consumers run against the intended Sage installation rather than a stub or temporary runtime.
  Restore the tracked Sage runtime before terminal execution resumes.
  **Observed gap:** `.envrc` names a source-checkout launcher that resolves into a stub-source tree and cannot import Sage; source inspection alone therefore cannot close the environment complaint.
  **Owner:** the tracked `.envrc` runtime contract and the supported static Sage installation for this repository.
  **Deliver:** select the actual supported Sage executable in `.envrc` (or repair the intended installation at its stable path) without creating another temporary Sage distribution; preserve the repository's intended dependency/runtime semantics rather than treating any Python with a `sage` module as interchangeable.
  **Acceptance:** after source remediation has closed and terminal execution is authorized, the tracked environment launches Sage, preparses the repository's `.sage` inputs through the normal project route, and a fresh process reaches the `terminal-session` star-import invariant.  This node does not authorize running Sage while `architecture-remediation` remains open.

### Categorical placement foundations

A `super_categories()` return states that every object of the category is an object of those.
Thirty categories declare `Sets()`; `just category-graph by-supercategory` lists the group.
Some members are sets with structure and belong there.
Others are not sets at all, and declare `Sets()` because the category their objects belong to is not in the tree.
These nodes build the missing categories rather than leaving the false declarations standing.

- [ ] **`algebra-structure-morphism-constructor`**. **Needs:** none.
  **Goal:** The root `Algebras(R)` owns the one constructor of an \(R\)-algebra, \((A, m)\mapsto A\): \(A\) an \(R\)-module and \(m\colon A\otimes_R A\to A\) an \(R\)-bilinear multiplication.  Over commutative \(R\) an \(R\)-algebra is determined by its structure morphism \(\rho\colon R\to Z(A)\), and the constructor produces \(\rho\) from \(m\): the scalar action \(r\mapsto(a\mapsto r\cdot a)\) lies in the centroid because \(m\) is bilinear, and for unital associative \(A\) it is the ring map \(r\mapsto r\cdot 1\), computed once at the root.  For \(R\) over itself, \(A=R\) as the free rank-one \(R\)-module and \(m\) its multiplication, so \(\rho=\mathrm{id}_R\).  No unit, associativity or commutativity is assumed at the root; those are axioms above it, and a Lie bracket is the multiplication of its algebra.  Every other route computes \((A, m)\) and calls this constructor (`CON-16`).
  **Remaining:** Finish native module-and-product construction in `_OwnedRingParent`, `_OwnedAlgebraParent`, predicate subrings, exact real scalars, and localizations. `_initialize_engine_algebra` still reaches `_install_multiplication`, which sets `unformed_module` to the object itself and records a native binary rule instead of constructing its module and feeding that module with its tensor classifier to the one entry. The integer/self-scalar bootstrap must retain the exact scalar object and identity morphism without becoming an exemption. Explicit central ring maps and the pointwise Lebesgue algebra now use the module and tensor owners; preserve those routes. The original one-entry acceptance below remains in force.
  **Owners:** `Algebras(R)` as the root; its `Associative`, `Unital`, `Commutative`, `Lie` axioms; the algebra Hom classes; `Modules(R)` for the underlying module.
  **Deliver:** the root constructor `Algebras(R)(A, m)` with \(A\) placed, storing \(m\) and producing \(\rho\) from it; `algebra_structure_morphism` a root method returning \(\rho\), its ring-map form on the unital associative refinement computed once; every engine ring constructed through it with its own multiplication (over itself, \(A\) the free rank-one module and \(\rho=\mathrm{id}\)); `OwnedAlgebras`, `AlgebraStructureConstruction`, the thirteen leaf restatements, the copy-and-identify machinery and its names deleted; the Hom admitting a linear map by the equation \(f\,m_A=m_B\,(f\otimes f)\) asked of the module Hom, which decides on finitary data and answers `Unknown`, recorded as the hypothesis, otherwise.
  **Acceptance:** `Algebras(R)(A, m)` is \(A\) placed in `Algebras(R)`, not a copy, and its `algebra_structure_morphism()` is the \(\rho\) produced from \(m\); \(R\) as an algebra over itself answers \(\mathrm{id}_R\); `algebra_structure_morphism` is defined once, at the root; `R[G]`, centres, quotients, the commutator Lie algebra, and every unital associative algebra, every engine ring included, reach `Algebras(R)` through the one constructor; `Lie` and nonunital algebras take the same constructor as unital associative ones; no category in the tree is named for carrying the root's datum.

- [ ] **`engine-algebras-through-the-structure-constructor`**. **Needs:** `algebra-structure-morphism-constructor`.
  **Goal:** Every algebra adopted from the engine -- polynomial rings, free and symmetric algebras, chosen-presentation quotients, matrix algebras, and the free algebra on a non-free module (`algebras/sparse_free_algebras.py`, an engine realization) -- is constructed through the structure-morphism constructor, so that its underlying \(R\)-module is constructed and the forgetful functor \(\mathbf{Alg}_R\to\mathbf{Mod}_R\) has something to send it to.  A free algebra is the image of the free functor, and its underlying module is the free module on words or monomials, the same \(R^{(I)}\) the free module functor gives.  Every ring \(R\) is placed as the free rank-one \(R\)-algebra and the free rank-one \(R\)-module over itself, alongside its other structures.
  **Observed gap:** `Algebras(R)` declares `Modules(R)`, so `_OwnedAlgebraParent` (`algebras/algebras.py`) and the engine free-algebra realization are placed in `Modules(R)` by declaration while neither constructs its module; the realization hand-writes `module_generating_set`, `module_generator`, `linear_combination`, `zero` and `scalar_multiple` (`sparse_free_algebras.py:182-212`, `:332-369`, `:537-566`), and `FramedAlgebras.ParentMethods.cardinality` restates a set-level operation on the algebra.  Before commit `83c80ce4` the forgetful functor answered these with a separate graded module; the history of `functors/algebra_modules.py` before that commit records how words and monomials index the homogeneous pieces.
  **Owners:** the structure-morphism constructor; `_OwnedAlgebraParent`; the free functor \(\mathbf{Set}\to\mathbf{Alg}_R\) and its module-level factor; `FramedAlgebras`.
  **Transferred from the delivered structured-module node:** the free-algebra inputs named `free_source_module` remain in `free_algebras.py`, `sparse_free_algebras.py` and `power_algebras.py`, with the scalar-change consumer in `functors/algebra_scalar_change.py`. They name the module generating a free algebra, not its full underlying module, so replacing their spelling by `unformed_module` would conflate different objects. Supply the correct free-functor/underlying-module data at their owners. The algebra root now implements the element-crossing pair and retains its exact `unformed_module`; native free-algebra realizations still need to construct that module rather than hand-writing its operations.
  **Deliver:** each engine-backed algebra route computing \((A, \rho)\) and feeding the constructor; the hand-written module operations and the algebra-level `cardinality` deleted; the free and power algebras answer the module they are built on through `unformed_module()`; the algebra level implements the element-crossing pair.
  **Acceptance:** `Modules(R).symmetric_algebra()(M)` and `R.polynomial_ring(names)` answer `module_generating_set`, `module_generator` and `scalar_multiple` by inheritance from the module the constructor built; no operation `Modules(R)` provides is defined in the algebra subtree; `rg -n 'def \w*_source_module\b' src` is empty; for `A = Algebras(R)(M, m)`, `A.unformed_module() is M` and `M(a)` reads an element of `A` in `M`.

- [ ] **`arrow-category-is-the-functor-category`**. **Needs:** none.
  **Goal:** `C.ArrowCategory()` is `Cat().Mor(FiniteOrdinalCategory(2), C)`, and arrow objects are built by that functor category's entry. Endomorphism, isomorphism, automorphism, monomorphism and epimorphism arrow categories are its full subcategories. Slices and coslices restrict one endpoint map to the identity, so are not full arrow subcategories; represented subobjects form the monomorphism subcategory of the slice.
  **Remaining:** `SubobjectCategory` still declares the underlying object category rather than constructing its chosen inclusion as a slice object; its admission probes for `inclusion` and its Hom detects failed factorization by exceptions. Thread the subobject constructors and their consumers through the slice owner, retaining each exact chosen inclusion and the correct fixed-edge Homs. The walking-arrow identity, natural-transformation squares and slice/coslice fixed-edge Homs are now implemented at the single functor-category owner; do not recreate a second arrow category.
  **Owners:** the slice/subobject construction in `abstract_categories/arrow_categories.py`; the set, module, group and lattice subobject constructors.
  **Acceptance:** every represented subobject retains its exact inclusion through the slice construction, and subobject Homs have the commuting-triangle semantics. `C.ArrowCategory()` remains literally `Cat().Mor(FiniteOrdinalCategory(2), C)`, with no second `_ArrowCategory` or per-arrow wrapper registry.

- [ ] **`functor-category-placement`**. **Needs:** none.
  **Goal:** \([A, B]\), \(C^{op}\), \(C \times D\), \(\mathrm{Disc}(S)\), \(\mathrm{Im}(F)\) and \(BG\) are each declared into the category their definition names, and a category is an object of `Cat` by construction.
  **Remaining:** the constructed categories now record their `Cat` placement, and `Cat` reads that placement rather than a general class predicate. Complete the distinct question of the categories containing their objects: a functor category contains functors and natural transformations, an opposite category contains opposite objects, and a product category contains pairs of objects. Their own membership in `Cat` does not make those objects categories. The remaining root `Objects()` declarations and `ClassifyingCategory` must be resolved by their actual definitions, with the native Sage category/Hom endpoint boundary kept private. Do not replace an object-level declaration by `Cat()` merely because the category is an object of `Cat`.
  **Owners:** `Cat`, the functor, opposite, product, discrete and image constructions, and the classifying-category owner.
  **Deliver:** for each construction, its genuine object/morphism category relationship, separately from its placement as a category object; no false graph edge or public host wrapper introduced to conflate the two.
  **Acceptance:** the categorical object placement and every changed object-level declaration have the stated mathematical meaning, with inherited Hom theories preserved. Execute the graph checks only in the authorized terminal phase.

- [ ] **`glued-sheaves-through-the-sheaf-entry`**. **Needs:** none.
  **Goal:** every sheaf on a scheme is an object of `Sheaves(coverage, D)` constructed by `Sheaves.object(presheaf, descent_data)`, the `X`-indexed sheaf categories are subcategories of it, and `DistinguishedAffineCover.glue_modules` returns that object.
  **Remaining:** The distinguished-cover module/algebra descent sheaves already call Sheaves.object, but cover.glue_modules still returns the datum rather than its sheaf. StructureSheaf and finite-atlas sheaf realizations still bypass the shared construction; scheme-indexed sheaf, cover and descent categories still need correct placement. Construct actual module-valued restrictions and descent before changing those entries: an affine-only presheaf on all Sch/X, singleton-only gluing, or refine after allocation does not complete the requirement.
  **Owners:** `Sheaves`, `DescentDataOnCover`, `CoveringFamilies` (`presheaves.py`); `SheafObjects`, `ModuleSheaves`, `DistinguishedAffineCover`, `StructureSheaf` (`ringed_spaces.py`).
  **Deliver:** `SheafObjects(X)` declared into `Sheaves` for the Zariski coverage on `X` with the module category as value category; `StructureSheaf` built through `Sheaves.object` with its `DescentData`; `glue_modules` returning the sheaf; `DescentDataOnCover` and `CoveringFamilies` declared into the categories their definitions name.
  **Acceptance:** `rg -n 'category=Cat\(\)\.meet' src/dzack_research/preamble/categories/schemes` is empty; `cover.glue_modules(M, t) in cover.cech_coverage().sheaves(Modules(A))` holds by construction; `just category-graph by-supercategory` lists `SheafObjects` under a `Sheaves` heading and none of the four categories above under `Objects`.

- [ ] **`objects-through-categories-scheme-gluing`**. **Needs:** `objects-through-categories-schemes`, `objects-through-categories-functions-sets-tensors`, `finite-affine-atlases`, `modules-over-varying-rings`, `sheaves-of-modules-over-a-sheaf-of-rings`, `limits-of-modules-created-by-underlying-sets`, `tensor-products-of-unframed-modules`.
  **Goal:** Every object of this subtree is an object of its category, constructed through that category's one entry (`CON-16`) and threaded through its immediate supercategory, so that the runtime root alone realizes `Parent`/`Element`; the side attributes, probes and exception branches those hand-assembled parents needed become construction data, placement questions and `case`/`match` on placement or asserted frontiers (`POLICY.NO_EXCEPTION_CONTROL_FLOW`).
  **Remaining:** The glued scheme now uses Schemes(R) with a private realization and the shared Hom/structure-map entry. Remaining are finite atlases/refinements, semilinear maps, descent data and their morphisms, inverse images and pullbacks. GlobalSectionModules, GlobalSectionAlgebras and QuasiCoherentSheavesWithChosenDescentDatum still require their genuine module/algebra/sheaf entries. Retain the descent interpretation needed to validate cyclic-cover branch sections, not just component arithmetic. Algebras must use Algebras(R)(M,m), sheaves must use Sheaves.object, and literal ingress belongs to the indexed-family owner.
  **Owners:** the `Schemes(R)` glued-scheme entry; the category of finite affine atlases of `X`; the module Hom over a ring map; sheaves of modules over a sheaf of rings; the `Modules(R)` limit and tensor constructions.
  **Deliver:** the glued scheme built by its `Schemes(R)` entry on the gluing datum; atlases, finite-atlas descent data (declaring `DescentDataOnCover`) and their morphisms built by their categories; semilinear maps as arrows of the module Hom over a ring map; \(f^{-1}F\) in its module-sheaf category; the categories `GluedSchemes`, `GlobalSectionModules`, `GlobalSectionAlgebras` and `QuasiCoherentSheavesWithChosenDescentDatum` removed, with their engines kept and their objects placed in `Schemes(R)`, `Modules(O(X))`, the algebra category over \(\mathcal{O}(X)\) and `QuasiCoherentSheaves(X)`.
  **Acceptance:** `schemes/gluing.py` holds no non-root host `__init__`, no `x._preamble_* = `, and no `isinstance` outside `_element_constructor_`, `__contains__` and `__eq__`; its engine classes are kept and their objects are placed in `Schemes(R)`, `Modules(O(X))` and `QuasiCoherentSheaves(X)` by those entries; it declares no category for glued schemes, modules of global sections or presented sheaves.

- [ ] **`objects-through-categories-schemes`**. **Needs:** none.
  **Goal:** Every object of this subtree is an object of its category, constructed through that category's one entry (`CON-16`) and threaded through its immediate supercategory, so that the runtime root alone realizes `Parent`/`Element`; the side attributes, probes and exception branches those hand-assembled parents needed become construction data, placement questions and `case`/`match` on placement or asserted frontiers (`POLICY.NO_EXCEPTION_CONTROL_FLOW`).
  **Remaining:** The affine/projective, closed/open, product/pullback, toric and relative-family schemes now use root construction and fixed-endpoint Hom owners. Remaining are ringed-space/sheaf realizations, formal and analytic family/local-system records, AT21 engines, covering/refinement and comparison records, geometric and log-pair placements, and their complete constructor/probe/exception occurrence families. Resolve the schemes-package cold-import cycle through invertible sheaves and K3/cyclic-cover families before replacing its lazy table. Renamed records and categories minted for engine outputs do not discharge these obligations.
  **Owners:** `Schemes(R)` and its affine, quasi-affine and toric refinements; `RingedSpaces`; the cohomology and family constructions; the owned root runtime.
  **Deliver:** Per file, each engine class on `Parent`/`SageObject`/`_OwnedRingParent` is kept and threaded: the objects it realizes are placed in the category they already belong to, by that category's entry, and no category is minted for the class of objects an engine or construction produces (CONTRIBUTING, *Contributing a category*, step 2); each non-root `Parent.__init__` becomes cooperative `super().__init__`; each `x._preamble_* = ` assignment becomes a constructor datum or is deleted as derivable; each `try:` becomes a `case`/`match` on categorical containment or an asserted frontier; each `isinstance`/`getattr`/`hasattr`/`__dict__` probe outside `_element_constructor_`, `__contains__`, `__eq__` and a declared engine adapter (`OWN-06`) becomes a placement question.
  **Acceptance:** for `schemes/`, the non-root `Parent.__init__`, side-attribute, probe and `try:` counts in the gap statement are zero outside sanctioned sites; every engine class there is kept and realizes objects placed by their existing category's entry; no category class is added without a literature definition of its objects and morphisms and the `CAT-22` search in the commit body; `just category-graph audit` reports no hand-assembled parent in it.

- [ ] **`objects-through-categories-groups`**. **Needs:** none.
  **Goal:** Every object of this subtree is an object of its category, constructed through that category's one entry (`CON-16`) and threaded through its immediate supercategory, so that the runtime root alone realizes `Parent`/`Element`; the side attributes, probes and exception branches those hand-assembled parents needed become construction data, placement questions and `case`/`match` on placement or asserted frontiers (`POLICY.NO_EXCEPTION_CONTROL_FLOW`).
  **Remaining:** ordinary native groups and transported subgroups now allocate through the group/subgroup entries, submonoids through `Monoids().Subobjects(M)`, and finite field-automorphism groups through `OwnedGroups().Finite()` with private engines. The absolute Galois restricted-Hom construction, prime prolongations, decomposition/inertia towers, conjugacy-class and lift-coset records still need their complete category entries. The group Hom realization, remaining predicate/data interfaces and exception/placeholder sites retain their original full obligations; the remote integration is not their completion. No constructor may replace a maintained catalogue engine by an assertion that its construction datum is missing.
  **Owners:** `OwnedGroups`, the profinite and Galois categories, `Monoids`, `GObjects`; the owned root runtime.
  **Deliver:** Per file, each engine class on `Parent`/`SageObject`/`_OwnedRingParent` is kept and threaded: the objects it realizes are placed in the category they already belong to, by that category's entry, and no category is minted for the class of objects an engine or construction produces (CONTRIBUTING, *Contributing a category*, step 2); each non-root `Parent.__init__` becomes cooperative `super().__init__`; each `x._preamble_* = ` assignment becomes a constructor datum or is deleted as derivable; each `try:` becomes a `case`/`match` on categorical containment or an asserted frontier; each `isinstance`/`getattr`/`hasattr`/`__dict__` probe outside `_element_constructor_`, `__contains__`, `__eq__` and a declared engine adapter (`OWN-06`) becomes a placement question.
  **Acceptance:** for `group/`, the non-root `Parent.__init__`, side-attribute, probe and `try:` counts in the gap statement are zero outside sanctioned sites; every engine class there is kept and realizes objects placed by their existing category's entry; no category class is added without a literature definition of its objects and morphisms and the `CAT-22` search in the commit body; `just category-graph audit` reports no hand-assembled parent in it.

- [ ] **`objects-through-categories-divisors`**. **Needs:** `glued-sheaves-through-the-sheaf-entry`, `objects-through-categories-schemes`, `invertible-sheaf-axiom`, `quasi-coherent-sheaf-morphisms-on-non-affine-schemes`, `sheaves-of-modules-over-a-sheaf-of-rings`, `cartier-divisors-as-sections`.
  **Goal:** Every object of this subtree is an object of its category, constructed through that category's one entry (`CON-16`) and threaded through its immediate supercategory, so that the runtime root alone realizes `Parent`/`Element`; the side attributes, probes and exception branches those hand-assembled parents needed become construction data, placement questions and `case`/`match` on placement or asserted frontiers (`POLICY.NO_EXCEPTION_CONTROL_FLOW`).
  **Remaining:** The section is its compatible chart family, and scalar change pulls it back without a remembered homogeneous source. The three linear systems now use the shared projective-space entry with their section, subobject/base-locus or jet-kernel data. Remaining are invertible-sheaf and isomorphism realizations, FiniteAtlasCartierDivisor, linearization classes, their genuine sheaf/group/Hom entries, the divisor package import order and all inherited non-root Parent, probe and exception sites. Their full acceptance below is unchanged.
  **Owners:** the sheaf categories and their invertible axiom; `Sheaves.object`; the projectivization functor or projective-space entry; the divisor package's import order.
  **Deliver:** invertible sheaves as objects of `QuasiCoherentSheaves(X).Invertible()` with a chosen trivialization, built by the sheaf entry, their comparisons as sheaf `Mor` elements and their restrictions as pullback images; the finite-atlas Cartier divisor as an element of the owned \(\mathrm{CDiv}(X)\); the three linear-system packages dissolved into data threaded by the projective-space entry; `linearizations.py`'s classes built by their categories; `__init__.py` importing its submodules eagerly.
  **Acceptance:** `divisors/` holds no non-root `Parent.__init__`, no `x._preamble_* = `, no `try:`, and no `isinstance`/`getattr` outside sanctioned sites; its engine classes are kept and their objects are placed by their existing categories' entries.

- [ ] **`finite-affine-atlases`**. **Needs:** `objects-through-categories-abstract-categories`.
  **Goal:** A finite affine atlas of a scheme \(X\) is a finite covering family of \(X\) by affine open immersions in the Zariski coverage of \(\mathbf{Sch}_R/X\), an object of a constructing `CoveringFamilies` level; its refinements, and the descent data on it (objects of `DescentDataOnCover`), are built by their categories.
  **Observed gap:** `CoveringFamilies` now constructs its objects, and distinguished affine covers thread their defining elements through that entry, deriving charts and indices from the root family. Remaining are the finite-atlas, refinement and descent-data classes in `schemes/gluing.py` and the geometric `CoverRefinement` record in `schemes/ringed_spaces.py`; they must construct through the covering/descent owners rather than allocating host records.
  **Owners:** `CoveringFamilies`, `DescentDataOnCover` (`presheaves.py`); the Zariski coverage on `Sch_R/X`.
  **Deliver:** `CoveringFamilies` with a constructor entry; the atlas, refinement and finite-atlas descent-data categories declared into it and into `DescentDataOnCover`; the gluing classes built through them.
  **Acceptance:** the listed `gluing.py` classes are objects of those categories built by their entries.

- [ ] **`modules-over-varying-rings`**. **Needs:** none.
  **Goal:** The Grothendieck construction of the functor \(R \mapsto \mathbf{Mod}_R\) on commutative rings: objects are pairs \((R, M)\), and a morphism \((R, M) \to (S, N)\) is a ring map \(\sigma\colon R \to S\) with an \(S\)-linear map \(S \otimes_R M \to N\), equivalently a \(\sigma\)-semilinear map \(M \to N\).
  **Observed gap:** semilinear maps and the transitions of finite-atlas gluing (`schemes/gluing.py` near 1529, 1653, 1820, 1866) are `SageObject`s because no category has these morphisms.  `FiberedFormedModuleMorphism` is the in-tree precedent for the fibered construction.
  **Owners:** the module category construction over `Rings`; the scalar-extension functor.
  **Deliver:** the fibered category with its projection to commutative rings; semilinear maps as its arrows, composed through scalar extension.
  **Acceptance:** the gluing semilinear maps and transitions are arrows of this category; composition of \((\sigma, f)\) and \((\tau, g)\) is \((\tau\sigma, g \circ (T \otimes_S f))\) up to the canonical isomorphism.

- [ ] **`sheaves-of-modules-over-a-sheaf-of-rings`**. **Needs:** `glued-sheaves-through-the-sheaf-entry`.
  **Goal:** For a ringed space \((X, \mathcal{O}_X)\), the category \(\mathbf{Mod}(\mathcal{O}_X)\) of sheaves of \(\mathcal{O}_X\)-modules; for \(f\colon Y \to X\), the inverse image \(f^{-1}\) of sheaves and the pullback \(f^{*}F = \mathcal{O}_Y \otimes_{f^{-1}\mathcal{O}_X} f^{-1}F\) as functors.
  **Observed gap:** the inverse image \(f^{-1}F\), its morphism and the pullback functor (`schemes/gluing.py` near 4409, 4456, 4498) are hand-built, `FiniteAtlasInverseImageModuleSheaf` is hand-placed in `SheafObjects`, and `Functor` accepts only `Map` morphisms.  The divisors node's projective-subscheme line bundles need the pullback along a closed immersion \(i\colon Z \to \mathbb{P}\).
  **Owners:** the sheaf categories; `ModuleSheaves`; `Functor`.
  **Deliver:** \(\mathbf{Mod}(\mathcal{O}_X)\) under the sheaf categories; \(f^{-1}\) and \(f^{*}\) as owned functors.
  **Acceptance:** `gluing.py`'s inverse-image classes are images of \(f^{-1}\); `ProjectiveSubschemeLineBundle` restricts by \(i^{*}\).

- [ ] **`limits-of-modules-created-by-underlying-sets`**. **Needs:** none.
  **Goal:** Products and equalizers of arbitrary \(R\)-modules at `Modules(R)`, created by the forgetful functor \(U\colon \mathbf{Mod}_R \to \mathbf{Set}\), with the diagram and the universal cone retained (the limits and colimits contract in CONTRIBUTING).
  **Observed gap:** `Modules(R)` has products only for framed or presented factors (`modules/pure/modules.py:507-529`), so the gluing merge (`d83d43c2`) builds \(\Gamma(X, F)\) as the Čech equalizer on underlying sets in two local categories, `GlobalSectionModules(R)` and `GlobalSectionAlgebras(R)`.
  **Owners:** `Modules(R)`; the categorical limit owner.
  **Deliver:** the general product and equalizer of modules; the engine realizing \(\Gamma(X, F)\) placing its object in `Modules(O(X))` through them.
  **Acceptance:** \(\Gamma(X, F)\) is the equalizer of \(\prod_i F(U_i) \rightrightarrows \prod_{i,j} F(U_{ij})\) constructed at `Modules(R)`, with its cone.

- [ ] **`tensor-products-of-unframed-modules`**. **Needs:** `limits-of-modules-created-by-underlying-sets`.
  **Goal:** The tensor product \(M \otimes_R N\) of \(R\)-modules without a chosen framing, with its universal bilinear map, at `Modules(R)`.
  **Observed gap:** The general tensor quotient and binary classifier are represented at `Modules(R)` without a framing. The global-section algebra in `schemes/gluing.py` still bypasses `Algebras(R)(M,m)`; integrate its chartwise product and unit with that classifier after its exact section module is built by the module-limit owner. Keep its descent interpretation and cyclic-cover consumers intact, and retain undecided quotient equalities as `Unknown` rather than confusing representatives with quotient classes.
  **Owners:** `Modules(R)`.
  **Deliver:** the tensor product of arbitrary modules with its universal bilinear map; the global-section algebra built through `Algebras(R)(M, m)`.
  **Acceptance:** `Algebras(R)(Γ(X, A), m)` constructs for a glued algebra sheaf; its multiplication is a morphism from the owned tensor square.

- [ ] **`invertible-sheaf-axiom`**. **Needs:** `glued-sheaves-through-the-sheaf-entry`.
  **Goal:** `QuasiCoherentSheaves(X).Invertible()`, the property of being locally free of rank one, as an axiom (`CAT-17`); an invertible sheaf with a chosen trivializing cover is its data subcategory.
  **Observed gap:** `divisors/invertible_sheaves.py` builds its five line-bundle classes by hand because no category states invertibility.
  **Owners:** `QuasiCoherentSheaves(X)`.
  **Deliver:** the axiom and its data subcategory; the invertible-sheaf classes built by the sheaf entry into them.
  **Acceptance:** an invertible sheaf is an object of `QuasiCoherentSheaves(X).Invertible()` by construction.

- [ ] **`quasi-coherent-sheaf-morphisms-on-non-affine-schemes`**. **Needs:** `glued-sheaves-through-the-sheaf-entry`.
  **Goal:** `Mor` in `QuasiCoherentSheaves(X)` for non-affine \(X\): a morphism of quasi-coherent sheaves is a family of module maps on the charts of a cover compatible with the transitions.
  **Observed gap:** the owned Hom of quasi-coherent sheaves is affine only; the comparison isomorphisms of \(\mathcal{O}_X(d)\) in `divisors/invertible_sheaves.py` are hand-built.
  **Owners:** `QuasiCoherentSheaves(X)`; the sheaf Hom.
  **Deliver:** the Hom on a cover, gluing module maps through the descent data.
  **Acceptance:** the \(\mathcal{O}_X(d)\) comparisons are elements of `X`'s quasi-coherent sheaf `Mor`.

- [ ] **`cartier-divisors-as-sections`**. **Needs:** `glued-sheaves-through-the-sheaf-entry`, `finite-affine-atlases`.
  **Goal:** The group \(\mathrm{CDiv}(X) = \Gamma(X, \mathcal{K}_X^{*}/\mathcal{O}_X^{*})\) of Cartier divisors, with an element on a finite atlas represented by local equations \((U_i, f_i)\) with \(f_i/f_j \in \mathcal{O}_X^{*}(U_i \cap U_j)\).
  **Observed gap:** `FiniteAtlasCartierDivisor` (`divisors/general_divisors.py:116`) is a `SageObject`; no owned group has these elements.
  **Owners:** the Cartier divisor group category; the quotient sheaf \(\mathcal{K}^{*}/\mathcal{O}^{*}\).
  **Deliver:** \(\mathrm{CDiv}(X)\) as that group of global sections; `FiniteAtlasCartierDivisor` retired into its elements.
  **Acceptance:** a finite-atlas Cartier divisor is an element of the owned \(\mathrm{CDiv}(X)\).

- [ ] **`objects-through-categories-abstract-categories`**. **Needs:** none.
  **Goal:** Every object of this subtree is an object of its category, constructed through that category's one entry (`CON-16`) and threaded through its immediate supercategory, so that the runtime root alone realizes `Parent`/`Element`; the side attributes, probes and exception branches those hand-assembled parents needed become construction data, placement questions and `case`/`match` on placement or asserted frontiers (`POLICY.NO_EXCEPTION_CONTROL_FLOW`).
  **Observed gap:** subobject factorization and the generic mono/epi families still use exception-based decisions; biproduct/tensor occurrence admission still probes for structure rather than following construction placement. The fixed Hom/native category-endpoint boundary and the construction of descent comparison data still require owner-level review. Replacing probes by class patterns, or catching the same owned exceptions in a helper named an engine adapter, is not remediation. Functor, arrow, covering-family and sheaf objects now use the owner entries, and fixed Hom categories reuse the arrow objects. Keep the selected-limit and selected-colimit engine records: they retain already-owned cone objects and their factorization rules, and are not grounds for inventing categories of engine outputs. Inspect the remaining constructor/membership occurrence family, including inherited declarations, before closing the node.
  **Owners:** `Cat`, the functor, arrow, product and presheaf categories; the owned root runtime.
  **Deliver:** Per file, each engine class on `Parent`/`SageObject`/`_OwnedRingParent` is kept and threaded: the objects it realizes are placed in the category they already belong to, by that category's entry, and no category is minted for the class of objects an engine or construction produces (CONTRIBUTING, *Contributing a category*, step 2); each non-root `Parent.__init__` becomes cooperative `super().__init__`; each `x._preamble_* = ` assignment becomes a constructor datum or is deleted as derivable; each `try:` becomes a `case`/`match` on categorical containment or an asserted frontier; each `isinstance`/`getattr`/`hasattr`/`__dict__` probe outside `_element_constructor_`, `__contains__`, `__eq__` and a declared engine adapter (`OWN-06`) becomes a placement question.
  **Acceptance:** for `abstract_categories/`, the non-root `Parent.__init__`, side-attribute, probe and `try:` counts in the gap statement are zero outside sanctioned sites; every engine class there is kept and realizes objects placed by their existing category's entry; no category class is added without a literature definition of its objects and morphisms and the `CAT-22` search in the commit body; `just category-graph audit` reports no hand-assembled parent in it.

- [ ] **`objects-through-categories-rings`**. **Needs:** none.
  **Goal:** Every object of this subtree is an object of its category, constructed through that category's one entry (`CON-16`) and threaded through its immediate supercategory, so that the runtime root alone realizes `Parent`/`Element`; the side attributes, probes and exception branches those hand-assembled parents needed become construction data, placement questions and `case`/`match` on placement or asserted frontiers (`POLICY.NO_EXCEPTION_CONTROL_FLOW`).
  **Observed gap:** 9 classes on `Parent`/`_OwnedRingParent` (`rings/commutative_algebra.py` 6, `ring_foundation.py` 3) plus `nonnegative_reals.py`, `unit_interval.py`; 6 non-root `Parent.__init__`; 32 side attributes (`ring_foundation.py` 14, `rings/__init__.py` 10); 109 `try:` blocks, the densest in the tree (`ring_foundation.py` 41, `commutative_algebra.py` 37, `commutative_ideals.py` 13); 56 `isinstance`, 60 `getattr`; 2 `__contains__` deciding by `isinstance`.
  **Owners:** `OwnedRings` and its axioms, the ideal, localization, completion and number-field categories; the engine adapters under `OWN-06`.
  **Deliver:** Per file, each engine class on `Parent`/`SageObject`/`_OwnedRingParent` is kept and threaded: the objects it realizes are placed in the category they already belong to, by that category's entry, and no category is minted for the class of objects an engine or construction produces (CONTRIBUTING, *Contributing a category*, step 2); each non-root `Parent.__init__` becomes cooperative `super().__init__`; each `x._preamble_* = ` assignment becomes a constructor datum or is deleted as derivable; each `try:` becomes a `case`/`match` on categorical containment or an asserted frontier; each `isinstance`/`getattr`/`hasattr`/`__dict__` probe outside `_element_constructor_`, `__contains__`, `__eq__` and a declared engine adapter (`OWN-06`) becomes a placement question.
  **Acceptance:** for `rings/`, the non-root `Parent.__init__`, side-attribute, probe and `try:` counts in the gap statement are zero outside sanctioned sites; every engine class there is kept and realizes objects placed by their existing category's entry; no category class is added without a literature definition of its objects and morphisms and the `CAT-22` search in the commit body; `just category-graph audit` reports no hand-assembled parent in it.

- [ ] **`objects-through-categories-modules`**. **Needs:** none.
  **Goal:** Every object of this subtree is an object of its category, constructed through that category's one entry (`CON-16`) and threaded through its immediate supercategory, so that the runtime root alone realizes `Parent`/`Element`; the side attributes, probes and exception branches those hand-assembled parents needed become construction data, placement questions and `case`/`match` on placement or asserted frontiers (`POLICY.NO_EXCEPTION_CONTROL_FLOW`).
  **Remaining:** the general, restricted-scalar, sparse free and selected-quotient constructors and the public finite-cokernel entry now carry their data at their owners. Finish the remaining constructor/refinement cycle in framed modules and presented internal Homs: `_install_framing` and `_install_presentation` are called during construction to resolve endpoint dependencies, but they still need to converge with the root construction contract rather than serve as a later independent refinement entry. Group lattices now thread their form and linearized action through their constructors without two levels consuming the same retained-module datum; coefficient-presentation methods are private to the linearized-module realization. The adic-completion and form/action consumers use the retained module and the source-owned scalar-change maps. `graded_direct_sums.py`, `connections.py`, `cochain_complexes.py` and formed-module records still need their own construction/membership review; the local Singular kernel orchestration remains the separately listed engine-delegation complaint. Generic mono/epi admission and stronger-Hom inheritance are not certified by merely moving native decisions into a helper. The lattice host constructor is owned by the lattice-files node, not this one.
  **Owners:** `Modules(R)` and its framed, presented, formed, graded and group-module refinements; the module Hom categories.
  **Deliver:** Per file, each engine class on `Parent`/`SageObject`/`_OwnedRingParent` is kept and threaded: the objects it realizes are placed in the category they already belong to, by that category's entry, and no category is minted for the class of objects an engine or construction produces (CONTRIBUTING, *Contributing a category*, step 2); each non-root `Parent.__init__` becomes cooperative `super().__init__`; each `x._preamble_* = ` assignment becomes a constructor datum or is deleted as derivable; each `try:` becomes a `case`/`match` on categorical containment or an asserted frontier; each `isinstance`/`getattr`/`hasattr`/`__dict__` probe outside `_element_constructor_`, `__contains__`, `__eq__` and a declared engine adapter (`OWN-06`) becomes a placement question.
  **Acceptance:** for `modules/`, the non-root `Parent.__init__`, side-attribute, probe and `try:` counts in the gap statement are zero outside sanctioned sites; every engine class there is kept and realizes objects placed by their existing category's entry; no category class is added without a literature definition of its objects and morphisms and the `CAT-22` search in the commit body; `just category-graph audit` reports no hand-assembled parent in it.

- [ ] **`objects-through-categories-algebras`**. **Needs:** `algebra-structure-morphism-constructor`, `engine-algebras-through-the-structure-constructor`.
  **Goal:** Every object of this subtree is an object of its category, constructed through that category's one entry (`CON-16`) and threaded through its immediate supercategory, so that the runtime root alone realizes `Parent`/`Element`; the side attributes, probes and exception branches those hand-assembled parents needed become construction data, placement questions and `case`/`match` on placement or asserted frontiers (`POLICY.NO_EXCEPTION_CONTROL_FLOW`).
  **Observed gap:** after the two algebra constructor nodes: 4 classes on `Parent`/`_OwnedRingParent` (`sparse_free_algebras.py` 2, `algebras.py` 1, `cyclic_cover_algebras.py` 1), 8 non-root `Parent.__init__`, 39 side attributes (`algebras.py` 12, `free_algebras.py` 11, `derivations.py` 5), 10 `refine(` sites in `algebras.py`, 82 `isinstance`, 33 `getattr`, 37 `try:`, 10 sites routing on a `WithChosen` category.
  **Owners:** `Algebras(R)` and its axioms, the free, graded, augmented and presented algebra categories, derivations.
  **Deliver:** Per file, each engine class on `Parent`/`SageObject`/`_OwnedRingParent` is kept and threaded: the objects it realizes are placed in the category they already belong to, by that category's entry, and no category is minted for the class of objects an engine or construction produces (CONTRIBUTING, *Contributing a category*, step 2); each non-root `Parent.__init__` becomes cooperative `super().__init__`; each `x._preamble_* = ` assignment becomes a constructor datum or is deleted as derivable; each `try:` becomes a `case`/`match` on categorical containment or an asserted frontier; each `isinstance`/`getattr`/`hasattr`/`__dict__` probe outside `_element_constructor_`, `__contains__`, `__eq__` and a declared engine adapter (`OWN-06`) becomes a placement question.
  **Acceptance:** for `algebras/`, the non-root `Parent.__init__`, side-attribute, probe and `try:` counts in the gap statement are zero outside sanctioned sites; every engine class there is kept and realizes objects placed by their existing category's entry; no category class is added without a literature definition of its objects and morphisms and the `CAT-22` search in the commit body; `just category-graph audit` reports no hand-assembled parent in it.

- [ ] **`objects-through-categories-lattice-files`**. **Needs:** none.
  **Goal:** Every object of this subtree is an object of its category, constructed through that category's one entry (`CON-16`) and threaded through its immediate supercategory, so that the runtime root alone realizes `Parent`/`Element`; the side attributes, probes and exception branches those hand-assembled parents needed become construction data, placement questions and `case`/`match` on placement or asserted frontiers (`POLICY.NO_EXCEPTION_CONTROL_FLOW`).
  **Remaining:** the lattice construction now equips the exact selected free module through the form/module owners; manifold points, analytic opens and discs use their existing mathematical owners, without new categories of those presentations. Voronoi cells/facets and reduction cells are ordinary owned polytopes/cones; Allcock vertices and ideal endpoints are actual rays. Finish the remaining isotropic-locus, orbit-decomposition, centralizer and reduction-adjacency host records and their functor/arrow constructions; do not reintroduce their missing orbit algorithms as unconditional failure stubs. General infinite forms still require their true functional/inverse data: finite-stage sampling cannot decide a colimit signature or all generator pairings. Nondegeneracy uses the declared ring, and infinite unimodularity means an isomorphism with the full algebraic dual, not the finite-support dual. These are mathematical requirements, not source-count or naming targets.
  **Owners:** `Lattices(R)` and the orbit, centralizer, reduction-complex and hyperbolic categories; `Modules(R)` underneath.
  **Deliver:** Per file, each engine class on `Parent`/`SageObject`/`_OwnedRingParent` is kept and threaded: the objects it realizes are placed in the category they already belong to, by that category's entry, and no category is minted for the class of objects an engine or construction produces (CONTRIBUTING, *Contributing a category*, step 2); each non-root `Parent.__init__` becomes cooperative `super().__init__`; each `x._preamble_* = ` assignment becomes a constructor datum or is deleted as derivable; each `try:` becomes a `case`/`match` on categorical containment or an asserted frontier; each `isinstance`/`getattr`/`hasattr`/`__dict__` probe outside `_element_constructor_`, `__contains__`, `__eq__` and a declared engine adapter (`OWN-06`) becomes a placement question.
  **Acceptance:** for `the lattice files under categories/`, the non-root `Parent.__init__`, side-attribute, probe and `try:` counts in the gap statement are zero outside sanctioned sites; every engine class there is kept and realizes objects placed by their existing category's entry; no category class is added without a literature definition of its objects and morphisms and the `CAT-22` search in the commit body; `just category-graph audit` reports no hand-assembled parent in it.

- [ ] **`objects-through-categories-functions-sets-tensors`**. **Needs:** none.
  **Goal:** Every object of this subtree is an object of its category, constructed through that category's one entry (`CON-16`) and threaded through its immediate supercategory, so that the runtime root alone realizes `Parent`/`Element`; the side attributes, probes and exception branches those hand-assembled parents needed become construction data, placement questions and `case`/`match` on placement or asserted frontiers (`POLICY.NO_EXCEPTION_CONTROL_FLOW`).
  **Observed gap:**  Arbitrary functor and natural-transformation objects, `module_localization.py`'s kernel/cokernel comparisons, `logic.py`'s propositions and `forms/gram_matrices.py`'s weighted graphs still need category construction.  `IndexedFamily` remains a raw `SageObject`: tensor index-slot families currently use `FiniteOrderedSets.from_indexed` even when different slots carry equal values, so they are not injective enumerations; replacing them with an unplaced `IndexedFamily` would not make them objects of the declared `Set x Set`.  The family and product-category owners must resolve this without identifying repeated slots.  Source-level probes, exception flow, element host initializations and restated set/module operations outside the repaired constructions still require the per-owner pass; the earlier aggregate counts are not current completion evidence.
  **Owners:** `Sets()` and its enumerated refinements, the function-space and Lebesgue categories, `Functor`, the form and tensor categories.
  **Deliver:** Per file, each engine class on `Parent`/`SageObject`/`_OwnedRingParent` is kept and threaded: the objects it realizes are placed in the category they already belong to, by that category's entry, and no category is minted for the class of objects an engine or construction produces (CONTRIBUTING, *Contributing a category*, step 2); each non-root `Parent.__init__` becomes cooperative `super().__init__`; each `x._preamble_* = ` assignment becomes a constructor datum or is deleted as derivable; each `try:` becomes a `case`/`match` on categorical containment or an asserted frontier; each `isinstance`/`getattr`/`hasattr`/`__dict__` probe outside `_element_constructor_`, `__contains__`, `__eq__` and a declared engine adapter (`OWN-06`) becomes a placement question.
  **Acceptance:** for `functions/, functors/, sets/, forms/, tensors/ and logic.py`, the non-root `Parent.__init__`, side-attribute, probe and `try:` counts in the gap statement are zero outside sanctioned sites; every engine class there is kept and realizes objects placed by their existing category's entry; no category class is added without a literature definition of its objects and morphisms and the `CAT-22` search in the commit body; `just category-graph audit` reports no hand-assembled parent in it.

- [ ] **`probe-and-exception-residue`**. **Needs:** `objects-through-categories-scheme-gluing`, `objects-through-categories-schemes`, `objects-through-categories-groups`, `objects-through-categories-divisors`, `objects-through-categories-abstract-categories`, `objects-through-categories-rings`, `objects-through-categories-modules`, `objects-through-categories-algebras`, `objects-through-categories-lattice-files`, `objects-through-categories-functions-sets-tensors`.
  **Goal:** No dynamic probe and no exception branch remains in mathematical code: `isinstance`, `getattr`, `hasattr` and `__dict__` reads exist only in `_element_constructor_`, `__contains__`, `__eq__` and declared engine adapters (`OWN-06`); `try:` exists only in a declared boundary renderer.
  **Observed gap:** at `HEAD` 869 `isinstance` (120 files), 317 `getattr` (91), 41 `hasattr` (23), 74 `__dict__.get` (19) and 500 `try:` (111).  The subtree nodes remove the ones their hand-assembled parents needed; this node is the sweep of what remains, classified site by site against the sanctioned list, never by a global count.
  **Owners:** every category whose code holds a probe; the engine adapters.
  **Deliver:** each remaining site either sits in a sanctioned method, is rewritten as `case`/`match` on placement or an asserted frontier, or is deleted with the placement that made it unnecessary named in the commit.
  **Acceptance:** the four probe counts and the `try:` count outside sanctioned sites are zero, measured by the survey commands in the commit body.

- [ ] **`inherited-operations-not-restated`**. **Needs:** `objects-through-categories-scheme-gluing`, `objects-through-categories-schemes`, `objects-through-categories-groups`, `objects-through-categories-divisors`, `objects-through-categories-abstract-categories`, `objects-through-categories-rings`, `objects-through-categories-modules`, `objects-through-categories-algebras`, `objects-through-categories-lattice-files`, `objects-through-categories-functions-sets-tensors`.
  **Goal:** An operation a supercategory provides is defined once, at its owner; no enriched object restates a set or module operation.
  **Observed gap:** 54 `cardinality` definitions in 30 files (`sets/set_categories.py` 10), 38 `zero` in 27, 16 `scalar_multiple` in 10, 9 `module_generator` in 8, 8 `module_generating_set` in 7.  Most sit on parents the subtree nodes rebuild; the remainder are restatements on constructed objects (the algebra-level `cardinality` on `FramedAlgebras`).
  **Owners:** `Sets()`, `Modules(R)`, `FramedModules(R)`; each restating leaf.
  **Deliver:** each definition outside its owning category deleted, with the object then answering by inheritance; a specialization that keeps a faster implementation states the theorem it uses.
  **Acceptance:** each of the five names is defined once per owning category and in no leaf; the objects the deleted definitions served answer the same operation through their construction.

- [ ] **`construction-datum-classification`**. **Needs:** none.
  **Goal:** Every private `_*Construction`/`_*Datum` class is either a functor-image provenance object `CON-05` names or is dissolved into its constructor's datum; none is a package of constructor arguments (`LEX-01`).
  **Observed gap:** 57 such classes in 35 files (`group/predicate_subgroups.py` 6, `divisors/linear_systems.py` 6, `schemes/geometric_cohomology.py` 5).  First specimens on each side: `_ChosenAlgebraMultiplicationDatum` (a package around `(M, m)`, deleted by `algebra-structure-morphism-constructor`) and `_GroupModuleConstruction`/`_FormModuleConstruction` (retained inputs behind identification maps, deleted 2026-09-17).
  **Owners:** the constructor of each class's product; `CON-05` for genuine provenance.
  **Deliver:** per class, the classification and the action: kept as the named provenance object with its consumer, or dissolved.
  **Acceptance:** no private class in the tree exists only to carry constructor arguments; each surviving one is the selected-image datum of a named functor with a consumer that reads it.

- [ ] **`banned-language-residue`**. **Needs:** none.
  **Goal:** No banned term of the replacement index appears in source.
  **Observed gap:** `carrier` at 30 sites in 8 files (`abstract_categories/arrow_categories.py` 17); 2 public `.Hom(` spellings outside engine adapters; the `*_source_module` accessors are handled by `engine-algebras-through-the-structure-constructor`.
  **Owners:** the file that holds each occurrence; the terminology dictionary for the replacement.
  **Deliver:** each occurrence replaced by the object it names (the underlying set or module, the target object of an arrow, `Mor`).
  **Acceptance:** `rg -w carrier src/dzack_research/preamble` and the `.Hom(` search are empty outside engine adapters.

- [ ] **`geometric-space-placement`**. **Needs:** none.
  **Goal:** The spaces, pairs and convex bodies in the `Sets()` group declare the categories their own definitions name.
  **Observed gap:** the enumerated table in [COMPLAINTS.md](COMPLAINTS.md) lists each with its docstring and the category it should be declared into.  `TopologicalManifolds` needs a category of topological spaces, which is absent.  `LogPairs` is a scheme with a divisor.  `HyperbolicSpaces`, `HyperbolicPolyhedra` and `PositiveConeComponents` are subspaces and projectivizations of \(L \otimes \mathbf{R}\).  `ConvexPolytopes` and `RationalPolyhedralCones` are convex bodies and cones in \(L \otimes \mathbf{Q}\).
  **Deliver:** per member, the correct declaration, or the missing category built, or `super_categories()` left abstract so the category refuses to construct.  Decide each against the definition it states, not by a rule applied across the group.
  **Acceptance:** none of these categories declares a supercategory its own definition contradicts.

- [ ] **`combinatorial-object-placement`**. **Needs:** none.
  **Goal:** The combinatorial members of the `Sets()` group declare the categories their own definitions name.
  **Observed gap:** `RegularPolytopes` are "abstract polytopes", which are graded posets, and `PartiallyOrderedSets` already exists.  `CoxeterDiagrams` ("a symmetric matrix of vertex angles") and `ProjectiveWeightedGraphs` ("finite graphs or digraphs with weights") need a category of graphs, which is absent.  `WeylChamberComplexes` ("locally finite chamber systems") needs chamber systems.  `VinbergInvariantMatrices` ("symmetric matrices") belongs to a matrix space over its coefficient ring.
  **Undecided:** `CharacterSets` calls itself a category of sets while \(\mathrm{Char}(G)\) carries a ring structure.  Whether the category is of the sets or of the rings is a decision this node surfaces rather than settles.
  **Acceptance:** none of these categories declares a supercategory its own definition contradicts, and the one undecided member is recorded as a decision rather than left as a false declaration.

- [ ] **`group-objects-construction`**. **Needs:** none.
  **Goal:** Own group objects in a category with finite products, \(\mathrm{Grp}(C)\), as a construction parameterized by \(C\) and declaring \(C\) (`CAT-20`), so that affine group schemes are `Grp(Schemes(R).Affine())` and their actions are objects of the category of \(G\)-objects for a group object \(G\).
  **Observed gap:** `AffineGroupSchemes` and `AffineGroupSchemeActions` (schemes/group_schemes.py:55, :249) declare `AffineSchemes(R)` directly, the true but non-immediate parent, because `GObjects(G, C)` takes an owned abstract group (group/g_objects.py:174), not a group object of \(C\).
  **Owners:** the owned product construction on `Cat` objects; `GObjects`, which should be the case of a discrete group object.
  **Acceptance:** an affine group scheme is placed through the group-object construction; the two scheme categories declare it and nothing two levels up; `GObjects(G, C)` is its restriction to constant group objects.

- [ ] **`membership-by-placement`**. **Needs:** `objects-through-categories-scheme-gluing`, `objects-through-categories-schemes`, `objects-through-categories-groups`, `objects-through-categories-divisors`, `objects-through-categories-abstract-categories`, `objects-through-categories-rings`, `objects-through-categories-modules`, `objects-through-categories-algebras`, `objects-through-categories-lattice-files`, `objects-through-categories-functions-sets-tensors`.
  **Goal:** No `__contains__` decides membership by a predicate (`CAT-23`).
  **Observed gap:** checked on 2026-09-16 by an empty-bodied commit (`1a3a5ba1`) while 26 `__contains__` bodies contain `isinstance` at `2ec862c6` (`hom_categories.py` 3, `arrow_categories.py` 2, `functors.py` 2, `products.py` 2, `cat.py` 2, `schemes/gluing.py` 2, one each in thirteen more files; bodies deciding through a helper such as `_IsoArrowCategory._accepts_arrow` are not in that count).  The original base-tower case: `Schemes.__contains__` answers lower-base membership by walking the candidate ring's base tower (schemes/schemes.py), so `X in Schemes(ZZ)` is true for a QQ-scheme that inherits nothing from it; `Sets.Countable.Infinite` decides membership by cardinality (a6078850); `QuasiCoherentSheaves.__contains__` duck-types (owned by `sheaf-object-placement`).
  **Acceptance:** each such membership is answered by placement at construction or through the functor of `CAT-16`; the predicates are gone.

- [ ] **`mor-spelling-convergence`**. **Needs:** none.
  **Goal:** `X.Mor(Y)` is the only spelling of a category of morphisms in the preamble universe (CONTRIBUTING, *`Mor` is the only spelling the preamble universe ever uses*; AGENTS.md banned-language index). `Hom` names Sage's construction and occurs only inside a private adapter that calls Sage.
  **Observed gap:** 59 public `Hom`/`Homs()` spellings in 24 files under `src/dzack_research/preamble/` on 2026-09-16, beside 1014 `Mor` spellings; 373 definitions whose names contain `hom` (`HomCategories`, `_hom_endpoint`, `module_homset`, ...), which realize the owned `Mor` constructions under Sage's name. The conversion was started once and interrupted (CONTRIBUTING `DEV-48`).
  **Owners:** the owned `Mor` construction on each category and the Hom-category types it generates; the private Sage boundary that constructs Sage's `Hom` for computation.
  **Deliver:** every public spelling becomes `X.Mor(Y)`; every owned definition named for Sage's construction is renamed for the owned construction it realizes, or moved behind the adapter if it is the Sage call; the conversion is carried through the whole tree before any run (`DEV-48`).
  **Acceptance:** `rg '\.Hom\(|\bHoms\(\)' src/dzack_research/preamble` finds only adapter sites that call Sage; the expectation subtrees' `Mor` spellings resolve.

### Owner API and construction data

- [ ] **`owned-provenance-data`**. **Needs:** `objects-through-categories-scheme-gluing`, `objects-through-categories-schemes`, `objects-through-categories-groups`, `objects-through-categories-divisors`, `objects-through-categories-abstract-categories`, `objects-through-categories-rings`, `objects-through-categories-modules`, `objects-through-categories-algebras`, `objects-through-categories-lattice-files`, `objects-through-categories-functions-sets-tensors`.
  **Goal:** Represent chosen source maps, presentations, base changes, completions, and comparison morphisms as first-class construction data instead of hidden `_preamble_*` provenance attributes.
  Replace hidden `_preamble_*source*`, functor-preimage, coordinate-morphism, and provenance side channels with first-class construction data (`CON-05`, `STY-07`, `OWN-03`--`05`).
  **Observed gap:** checked on 2026-09-16 by an empty-bodied commit (`0d458d7e`) with 327 `x._preamble_* = ` assignments before and after it; 329 at `2ec862c6` in 62 files (`schemes/schemes.py` 35, `module_morphisms.py` 23, `schemes/gluing.py` 20, `pure/modules.py` 16, `ring_foundation.py` 14, `algebras.py` 12).  The subtree nodes convert the ones their hand-assembled parents carry; this node is the sweep of the remainder to zero, site by site.
  **Owners:** the functor image, chosen presentation, comparison morphism, base-change datum, completion datum, or other mathematical construction whose later operations require the source.
  **Deliver:** identify which source/preimage is genuine selected mathematics and store it in the construction object or represented morphism that defines the result.  Derivable debug provenance is not public construction data and should disappear instead of moving to another dictionary.
  **Acceptance:** affected downstream operations recover required source objects/maps from their defining construction, not ad-hoc attributes on an otherwise ordinary result; deleting a private source attribute cannot change the mathematics because no such authority remains.

- [ ] **`refinement-convergence`**. **Needs:** `owned-provenance-data`.
  **Goal:** Construct objects with all structure implied or selected by their defining data, reserving later refinement for genuinely new mathematical facts proved after construction.
  Eliminate runtime refinement as a second ordinary construction mechanism under `ARC-13`, `STY-08`, and `OWN-02`--`03`.
  **Observed gap:** 49 `refine(...)` call sites remain; ring and scheme constructors still install standard structure or `_preamble_scheme_*` state after object allocation.  Added 2026-09-16 (d0bc6903): `OwnedOrders` is now the join of `Algebras(ZZ)`'s finite-generation axiom with the Noetherian domains, and because the integers are themselves an order while `Algebras(ZZ)` needs them, `_owned_integers` refines the constructed integers into `OwnedOrders` after construction and `OwnedOrders.super_categories` reads an engine view of ZZ to avoid re-entering that refinement (`CAT-24`).  The initial ring's placement in the algebras over itself is a construction-time fact to state once, not a post-construction refinement.
  **Deliver:** standard structure that follows from defining data is present when the object is constructed; selected structure is passed explicitly through its constructor/functor; later `refine` remains only for a genuinely new mathematical fact proved after construction.  Remove call-history/import-order dependence from inherited operations.
  **Acceptance:** representative ring, scheme, module and functor-image constructions have identical mathematical category/operations regardless of which accessor is called first or import order; every surviving runtime refinement names the later theorem/chosen datum that justifies it rather than repairing incomplete initialization.

### Public vocabulary, representations, and codomains

- [ ] **`mathematical-return-types`**. **Needs:** `refinement-convergence`.
  **Goal:** State public API codomains in mathematical terms—sets, categories, refinements, morphism spaces—rather than framework-universal `Parent`, `Element`, or ad hoc `Any`.
  Replace framework-universal public return annotations (`Parent`, `Element`, `CategoryObject`, and ad hoc `Any`) with mathematical codomains under `LEX-12`--`15`.
  **Observed gap:** the audit counted 261 framework-universal return annotations, including functor images, cardinalities and scheme operations.
  **Deliver:** after the affected public APIs have stabilized, annotate each operation by the mathematical set/category/refinement its values inhabit.  When Python cannot yet express that codomain directly, introduce or reuse one central mathematically named alias/refinement rather than a local implementation wrapper.
  **Non-goal:** this is not checker paydown; do not distort source to satisfy mypy or replace an honest mathematical union by a narrower convenient implementation type.
  **Acceptance:** representative operations in every audited family state falsifiable mathematical codomains; a source audit finds no remaining universal annotation unless its declaration has an explicit documented mathematical alias/union whose precision is genuinely not expressible more directly.

### Computational boundaries and duplicate algorithms

- [ ] **`assertion-frontiers`**. **Needs:** none.
  **Goal:** Keep public operations at their full mathematical domain while making the exact unsupported computational remainder fail explicitly at the representation/hypothesis frontier.
  Replace public mathematical `NotImplementedError` control flow with the exact computational frontier required by `CAT-01`, `DEF-06`, `STY-48`, and `DEV-11`.
  **Observed gap:** 449 direct raises remain, in 212 public callables, with major concentrations in schemes, algebras, commutative algebra, modules, lattices and groups.
  **Deliver:** for each public mathematical operation, keep it at the domain where the notion is defined, route every supported exact case through its maintained owner, and assertion-gate only the precise unsupported computational remainder with the missing hypothesis/representation stated.  Remove methods with no successful mathematical case or make genuine abstract contracts abstract.
  **Acceptance:** no public mathematical API uses `NotImplementedError` as its ordinary unsupported-case semantics; representative unsupported inputs fail at an informative assertion frontier without returning a false mathematical value or narrowing the method's codomain.

- [ ] **`placeholder-stubs`**. **Needs:** `assertion-frontiers`.
  **Goal:** Remove unconditional `assert False`, `pass`, and similar placeholders from public mathematical promises by implementing the operation, making it genuinely abstract, or deleting the misplaced API.
  Remove unconditional visible mathematical placeholders (`STY-48`, `STY-160`).
  **Observed gap:** tensor `_index_ranks()`/`tensor_valence()` use unconditional `assert False`; an optional abstract profinite-group method uses `pass` rather than the required Sage abstract contract.
  **Deliver:** implement the operation at its proper owner when mathematics is available; otherwise make the genuine abstract contract explicit or delete/move a method that is not defined at that layer.  Use `...` in Sage abstract bodies as required by policy.
  **Acceptance:** each audited method has a successful mathematical implementation path or is an honest abstract declaration; no unconditional failure/pass body remains behind a public mathematical promise.

- [ ] **`singular-kernel-delegation`**. **Needs:** `assertion-frontiers`.
  **Goal:** Delegate finitely presented module kernel/syzygy computation to a maintained Sage/Singular operation through one adapter, then raise the result to the owned kernel object, inclusion, and presentation.
  Replace `_singular_presentation_kernel`'s long Python orchestration with a maintained Singular/Sage operation behind one owned adapter crossing (`ENG-01`--`03`, `STY-57`--`59`, `OWN-08`).
  **Observed gap:** current code manually builds matrices, lifts coefficients, invokes Singular `modulo`, reconstructs relations and recovers lifts across roughly 170 lines.
  **Deliver:** identify the exact maintained kernel/syzygy/presentation operation that returns enough data to reconstruct the owned kernel inclusion and selected presentation.  Keep representation conversion at the adapter boundary; do not reproduce the standard algorithm in Python around lower-level Singular calls.
  **Acceptance:** a nontrivial finitely presented module morphism obtains its kernel object, inclusion and presentation through one maintained-engine computation and raises every constituent to owned mathematics; unsupported coefficient regimes stop at the declared frontier rather than falling back to the old orchestration.

- [ ] **`imperative-algorithm-cleanup`**. **Needs:** `singular-kernel-delegation`.
  **Goal:** Replace generic local traversal, grouping, multiplication, and accumulation code with standard mathematical operations or mature dependency owners, retaining loops only when they are genuinely theory-specific algorithms.
  Remove the remaining guide-catalogued imperative algorithms only after their larger duplicated owners have converged.
  **Observed gap:** examples include bilinear nested accumulation, duplicate free-algebra target multiplication loops, divided-power coefficient loops, absolute-Galois append/filter construction, `setdefault(...).append(...)` grouping, and bespoke `frontier`/`seen` traversals in lattice/action code.
  **Deliver:** for each audited site, identify the standard mathematical operation or mature dependency owner and replace the local algorithm with that operation.  When an explicit loop is genuinely the theory-specific algorithm, retain it and document the mathematical reason rather than rewriting it cosmetically.
  **Acceptance:** every occurrence family named by the complaint has been adjudicated; removed sites delegate to a real owner, and retained loops are demonstrably special mathematics rather than generic grouping/traversal/multiplication infrastructure.

### Public interaction and proof surfaces

- [ ] **`coordinate-firewall`**. **Needs:** none.
  **Goal:** Confine coordinates and raw matrices/vectors to explicitly chosen finite framings or presentations; ordinary lattice/module/morphism interaction should remain semantic.
  Close ordinary public coordinate/storage escape hatches that bypass semantic owners (`ARC-18`, `API-02`, `DEV-40`).
  **Observed gap:** lattice elements expose `to_list`/`to_tuple`/`to_vector`, tensor elements expose raw `components()`/`list()`, and module morphisms expose matrix storage as ordinary public interaction; the canonical notebook teaches these routes.
  **Deliver:** keep explicit coordinate views only on the selected finite framing/presentation object where coordinates are mathematically part of that chosen datum.  Ordinary element/morphism APIs route through owned operations, Homs and universal constructions; downstream research code migrates before the old hatches are removed.
  **Acceptance:** a user cannot bypass the semantic object merely by calling an equally public raw-storage method; the retained finite-coordinate boundary names the framing/presentation that makes the coordinates meaningful and distinguishes it from unframed/infinite cases.

- [ ] **`canonical-notebook-contract`**. **Needs:** `coordinate-firewall`.
  **Goal:** Turn the canonical notebook into an executable research narrative organized by mathematical questions and witnesses, using the same final public API expected from ordinary users.
  Repair the canonical notebook to satisfy `NB-01`--`05`, `ARC-07`, `LEX-10`, and `DEV-40` after the public APIs it teaches have converged.
  **Observed gap:** 30/51 code cells are unexecuted, committed failure output remains, several mathematical claims occur only in prose, section headings are implementation tours, and examples use old globals/ambiguous generator APIs/raw constructors and coordinate paths.
  **Deliver:** organize sections by mathematical questions; express claims as computations/assertions/witness displays; use the same owner-method/Hom/functor/session syntax expected from ordinary researchers; remove stale output and compatibility-layer examples.  Preserve useful research content rather than turning the notebook into a policy demonstration.
  **Acceptance:** every substantive claim in the audited notebook is executable or visibly witnessed, no committed traceback remains, and no example depends on an API prohibited by the upstream remediation nodes.  Actual execution is deferred to `terminal-session`.

- [ ] **`architecture-remediation`**. **Needs:** `finite-affine-atlases`, `modules-over-varying-rings`, `sheaves-of-modules-over-a-sheaf-of-rings`, `limits-of-modules-created-by-underlying-sets`, `tensor-products-of-unframed-modules`, `invertible-sheaf-axiom`, `quasi-coherent-sheaf-morphisms-on-non-affine-schemes`, `cartier-divisors-as-sections`, `mor-spelling-convergence`, `group-objects-construction`, `membership-by-placement`, `algebra-structure-morphism-constructor`, `engine-algebras-through-the-structure-constructor`, `arrow-category-is-the-functor-category`, `functor-category-placement`, `glued-sheaves-through-the-sheaf-entry`, `objects-through-categories-scheme-gluing`, `objects-through-categories-schemes`, `objects-through-categories-groups`, `objects-through-categories-divisors`, `objects-through-categories-abstract-categories`, `objects-through-categories-rings`, `objects-through-categories-modules`, `objects-through-categories-algebras`, `objects-through-categories-lattice-files`, `objects-through-categories-functions-sets-tensors`, `probe-and-exception-residue`, `inherited-operations-not-restated`, `construction-datum-classification`, `banned-language-residue`, `geometric-space-placement`, `combinatorial-object-placement`, `owned-provenance-data`, `refinement-convergence`, `assertion-frontiers`, `placeholder-stubs`, `singular-kernel-delegation`, `imperative-algorithm-cleanup`, `mathematical-return-types`, `coordinate-firewall`, `canonical-notebook-contract`.
  **Goal:** Converge the twenty complaint-derived architecture repairs into one coherent mathematical API before any final runtime/session claim is accepted.
  This is the convergence/scheduling node for the complaint-derived workstream, not another implementation pass.
  **Acceptance:** each of the twenty audit findings has either been repaired at its mathematical owner and removed from `COMPLAINTS.md`, or has exposed a genuinely independent residual obligation that exists as its own DAG child with explicit acceptance and is therefore added to this node's `Needs`.  No finding is closed by changing a count, hiding a name, adding a wrapper, or weakening a public mathematical claim.  All source-level specimens needed to falsify the repaired contracts are banked for terminal execution.

### Post-remediation convergence

- [ ] **`refactor-audit`**. **Needs:** `terminal-session`.
  **Goal:** After the repaired mathematics runs end-to-end, audit the repository for duplicated authority, poor organization, and maintainability defects that survived the architecture work.
  Audit the whole repository for messy, disorganized or duplicated code after the complaint-derived architecture has been exercised through the final public session.
  The public mathematical API need not change and should not change incidentally; this pass is about internal sources of truth, ownership and maintainability that survive the mandatory architecture repairs.

  Repair a bounded finding at its owner during the audit.  If a finding is genuinely too large or crosses independent owners, give the concrete repair its own DAG row with source-backed acceptance and make this node depend on that repair before it can close.  Do not create rows whose deliverable is only a report, inventory, approval, or proof that the audit ran.

  **Acceptance:** the whole-repository pass is complete; every defensible finding has either been repaired at its owner or is represented by a concrete repair row that has itself closed; and a final read finds no remaining source-of-truth, ownership, or duplication defect in this scope.  A clean pass requires no receipt commit.

- [ ] **`type-paydown`**. **Needs:** `refactor-audit`.
  **Goal:** Improve static type information only where it clarifies the mathematics and makes correctness easier to reason about; do not contort code merely to lower an error count.
  Pay down type errors where doing so is reasonable, and not one step further.
  Every typing decision must improve the legibility of the code, the ability to understand what it does, and the ability to reason statically about whether it is correct.  That is the standard the change is judged against, not the error count.

  Golfing the code into oblivion -- distortions that exist only to silence a checker -- is the failure mode.  Where a contortion is genuinely warranted, it must be judged as significantly serving the goal above, and the argument for it recorded explicitly in the commit message.  A type annotation nobody can read has made the code worse even when the checker is quieter.

- [ ] **`bloat-audit-loop`**. **Needs:** `type-paydown`.
  The legacy identifier is retained for stable references, but this is a finite terminal convergence pass, not a permanently open audit loop.
  Before each pass reread `AGENTS.md`, `CONTRIBUTING.md`, this DAG, and the relevant audit skills under `~/ai/opencode/skills/`: `addressing-shallow-work`, `policy-index`, `anti-slop`, `fixing-slop`, `bespoke-software-policy`, `code-patterns`, `thermo-nuclear-code-quality-review`, `brooks-audit`, `brooks-debt`, `test-guidelines`, `test-writing`, `known-solution-first`, `epistemic-integrity`, `reality-grounded-debugging`, `reviewing-llm-code`, `quality-control`, and `general-cleanup`.  These are interpretive lenses, not a checklist and not permission to rewrite mathematical expectations.

  Cover categorical/math owner placement; duplicate or derivable retained state; public type/API design; tests as behavioral proofs rather than implementation mirrors; dead compatibility bridges and validation-evasion fallbacks; dependency offload to Sage, GAP/CAP, OSCAR, SymPy, Python or another mature owner; import/lazy-import and module-cycle structure; notebook/session usability; generated/static projection boundaries; and AI-slop or locally tidy code that violates the architectural contract.
  Search the dependency or upstream owner before improving a local mechanism that may not need to exist.

  Repair a small, well-supported finding in the same pass and commit the behavioral regression or mathematical consumer that proves it.  If a finding spans several owners or is too large to repair coherently in one pass, add a concrete repair row with the necessary dependency edges; this node cannot close until that repair closes.  Never create a node merely to say that an audit ran, and never leave a finding in `COMPLAINTS.md` as a substitute for repair.

  **Acceptance:** all lenses above have been applied to the post-`type-paydown` tree; every resulting finding has been repaired at its owner or through a closed concrete repair row; and one final whole-repository pass finds no additional defensible bloat, duplicate owner, avoidable bespoke mechanism, or architectural violation.  A clean final pass makes no receipt commit.  Later regressions are new owner-local defects and do not retroactively turn this completed convergence pass into a perpetual queue.

## Optional research consumers

These are not prerequisites for the required mathematics, complaint remediation, terminal verification, or convergence audits.

- [ ] **`optional-database`**. **Needs:** `terminal-session`. Add a database/classification example when it supplies data needed by research: LMFDB, curve/field databases, OEIS, GRDB, Kreuzer--Skarke or Fanography.
  **Goal:** Add a research database adapter only for a concrete mathematical query whose data materially benefits a live research workflow.
  Select a concrete mathematical query before provisioning an adapter.

- [ ] **`optional-engine`**. **Needs:** `terminal-session`. Extend private engine integrations when a named construction benefits: Sage/Singular for local and polynomial algebra, libGAP for group actions, persistent `sage-julia-bridge` for OSCAR/Hecke, optional Macaulay2 for its exact algebra strengths, and `py_polyhedral` for required polyhedral binaries.
  **Goal:** Extend private CAS/engine integrations only for a named mathematical construction that benefits from that engine, returning owned objects and maps at the public boundary.
  Maxima stays within its symbolic-calculus domain.
  **Decision:** search existing interfaces first; provision only the needed dependency; put reusable codecs and bridge defects at their actual owner.
  Mathematical outputs always return as owned objects and maps.
  An integration required by an item above is part of that required item, not this optional list.
  Only additional research capabilities with no required consumer belong here; moving a dependency here does not unblock or complete its consumer.
