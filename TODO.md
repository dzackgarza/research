# Preamble TODO

## Execution priorities

Make the existing preamble reliable for daily mathematics, stabilize its construction language, and prove the frozen API before expanding its required capabilities.
Complete shared mathematical dependencies before extending their consumers.
Within a milestone, geometry has priority over independent arithmetic applications; an arithmetic computation moves earlier only when a named geometric construction needs its result.

Select from the earliest unfinished milestone. Within its ready frontier, fix wrong mathematical answers first, then shared architectural causes, then the remaining owner repairs and exercises. Preserve the placement and extensibility contract while doing so. Later capability growth consumes the accepted architecture through explicit gate edges below.
Priority orders ready nodes; it is never an edge. Milestone acceptance is an actual required output and therefore has a node and dependency edges.

This is an executable work list, not a record of past work.
Remove an item when its stated work is delivered; retain only its unfinished obligations if delivery is partial.
Completion evidence belongs in the implementation commit and its mathematical specimens.
Do not append completed rows, release histories, audit transcripts, or an overall-progress table.

The requirements below specify new deltas from existing constructions.
A source path identifies where to extend or repair, not an instruction to recreate that subsystem.
Inspect the live constructor and its consumers before editing.
Uncertainty explicitly assigned to a source review is not a claim of a runtime failure.
The pending acceptance sessions cover the entire required implementation, including banked proof for constructions no longer listed as source work. M1 proves the selected daily core, M3 proves the frozen existing API, and M4 proves the required additions.

Follow [CONTRIBUTING.md](CONTRIBUTING.md), especially `DEV-50` through `DEV-68`. Begin new additions with its [mathematical dependency trace](CONTRIBUTING.md#mathematical-dependency-tracing), before selecting an implementation.
Record observed missing foundations and papercuts in [COMPLAINTS.md](COMPLAINTS.md), including independent discoveries.
That file owns the observed need and evidence; this queue owns the selected remaining repair and its acceptance.
Link them instead of copying status.
The [design philosophy](CONTRIBUTING.md#preamble-design-philosophy) and [architecture specification](CONTRIBUTING.md#preamble-architecture-specification) govern how every item is implemented, including already-existing dependencies.
The intended result is one recursively owned mathematical language composed from shared constructions and maintained computations, not a larger local CAS. Read the generated `docs/preamble-megadoc.md` before preamble implementation under the governing `AGENTS.md` prerequisites.
Under DEV-58, only M1 source closure precedes the execution phase. The daily-core session starts that phase; M2 audits, M3 full acceptance and M4 additions then retain execution of affected proof.

### Select from the live dependency graph

The queue is the scheduling surface.
Completed prerequisite rows and their edge references are removed together, so the ready frontier is precisely the rows with `Needs: none`. Recompute the ready frontier from the current rows before selecting work; do not preserve dated frontier counts or a private list of what was ready in an earlier turn:

```sh
rg -n '^- \[ \] \*\*`[a-z0-9-]+`\*\*\. \*\*Needs:\*\* none\.$' TODO.md
```

Take the ready frontier in dependency order and carry each selected node through delivery before moving on.
A node that closes unblocks its dependents; a node that merely grows does not.
This repository has one worker, so selection has no claim or reservation layer.

## Milestones

| Milestone | Delivered result | Acceptance boundary |
| --- | --- | --- |
| M1 — Daily mathematical work | A broad core of ordinary research workflows works through owned objects, maps and category methods; algorithms can gain cases without narrowing the API | Source repairs and the daily exercises feed `core-usability-session`; the core passes in fresh and composed sessions with usable display and response time |
| M2 — Auditable minimal API | One documented generating construction language, a coherent category graph, highest valid method owners and discoverable constructors | `minimal-api-freeze` closes after the finite source audits and constructor audit; existing capability is preserved |
| M3 — Compact mathematical test suite | The frozen API has substantive exercises, a consolidated suite and explicit meaningful-method coverage | `terminal-session` requires 100 percent pass rate for the retained required suite and greater than 90 percent meaningful method coverage, with performance gates intact |
| M4 — Required mathematical expansion | The pending group, lattice, geometric and automorphic constructions extend stable owners and computational cases | `extended-mathematics-session` proves the required additions together with the retained core |
| M5 — Optional research extensions | Additional named research consumers use the accepted architecture | Each optional node supplies its own mathematics and proof; it never becomes a hidden prerequisite of required work |

A milestone is an acceptance boundary, not a claim that the mathematics outside it is absent.
M1's broad core is chosen from actual mathematical work before its tests run. Its failures are repaired at their owners. Failures elsewhere stay visible for M3; they do not justify reducing the core or requiring the entire current suite to pass before ordinary work becomes usable.
M2 freezes independent contracts and their derivations, not today's implementation classes or a reduced feature set.
M3 audits and consolidates the existing suite before making whole-suite success the gate.
M4 retains every required feature obligation and engine decision below. A feature whose foundation is broken repairs that prerequisite before extending the consumer.
M5 remains optional. A substantial category-kernel replacement is an explicit architectural revision with renewed affected freeze and proof obligations.

The node sections below are the milestone assignments. Only their Needs lists define edges; the overview is not a second graph or completion ledger.
Remove completed nodes and their references under DEV-50. Retain a milestone's acceptance node until its evidence is delivered.

### Contents

- [Execution decisions](#execution-decisions-for-every-item), [workstreams](#workstreams), and [DAG rules](#remaining-workstreams-as-a-dependency-graph)
- [M1: Daily mathematical work](#m1--daily-mathematical-work)
- [M2: Auditable minimal API](#m2--auditable-minimal-api)
- [M3: Compact mathematical test suite](#m3--compact-mathematical-test-suite)
- [M4: Required mathematical expansion](#m4--required-mathematical-expansion)
- [M5: Optional research extensions](#m5--optional-research-extensions)

### Execution decisions for every item

Apply these decisions inside the selected unfinished item, not in a separate audit, readiness registry, or new planning system.
Their durable authority is `OWN-01` through `OWN-23` and `DEV-50` through `DEV-68` in CONTRIBUTING.

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
   Derive that family from the original requirement and source declarations before comparing it with the delivered routes.
   Read called helpers and overrides; a changed-file list or a set of search matches is not the family.
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

The rows group obligations; only unchecked nodes schedule work.
Complexity follows [COMPLEXITY.md](COMPLEXITY.md), measures the assigned responsibility, and is reassessed when a leaf's inputs are settled.

| Work | Shared output and closure boundary | Complexity and reason |
| --- | --- | --- |
| Constructor/admission foundations | One datum and admission authority; framing, tensor, scalar and algebra laws survive all routes | 90: recursive construction and shared mathematical identity |
| Diagrams/rings/geometry | Universal maps, varying-ring descent and projectivization through existing owners | 85: variance, base changes and general-versus-specialized constructions |
| Forms/actions/arithmetic | Exact forms, duals, group actions and owned arithmetic witnesses | 85: weak hypotheses, infinite objects and completeness of algorithms |
| Common categorical authority | Single functor/adjunction/provenance authority, inherited operations and recursive ownership | 90: contracts span multiple consumer families |
| Maintained computation | Complete engine result/maps and exact computational frontiers | 80: upstream capability and representation contracts |
| Public interaction | Mathematical vocabulary, coordinate boundary, codomains and research narrative | 65: coherent migration of all consumers |
| Terminal proof and convergence | Executed distinguishing evidence, then finite whole-repo review and justified typing repair | 15 for execution; score newly observed repairs at their actual owners |

Among ready items, close a shared constructor/admission prerequisite before its dependent API polish.
Within the selected milestone, geometry precedes independent arithmetic.
An already-integrated route is preserved and reviewed against its remaining obligation, not rewritten from its historical complaint.
Carry one node to its full source acceptance before selecting another (`DEV-60`). No workstream gets a separate claim/status ledger.

### Invariants required to close any source node

The node's own contract and `DEV-67` are conjunctive.
Review the complete affected entry and consumer family, not only its first specimen.
Every source delivery must establish:

- **Defining datum:** the exact owned objects, maps, base and hypotheses are fixed by one constructor; structure is the defining morphism, and checks and structure tables are computed only when asked for (`CON-16`, `OWN-22`, `OWN-23`).

- **Inherited structure:** the immediate general construction supplies its actual operations; stronger structure adds only its own data.
  Retained input, free-functor source and underlying object are not conflated (`OWN-14`--`20`).

- **Mathematical maps:** domains, codomains, equations, universal factorizations and transport agree.
  Dimension/rank/cardinality agreement is insufficient.

- **Ownership and computation:** every reachable result is owned; protected access stays at its declared owner; a maintained semantic computation is actually reused (`OWN-04`--`08`).

- **Required generality:** preserve represented infinite objects, nonfree modules, nontrivial coefficients and exact hypotheses.
  `Unknown` is not true, a finite window is not the object, and an abstract placeholder is not a delivered concrete operation.

- **Proof transfer:** bank a positive and a separating nearby invalid/different specimen, and preserve execution under T. Specimens falsify particular substitutes; source coverage must separately discharge every clause and required regime.
  Naming a child or removing an API transfers no burden by itself.
  Aggregate closure requires all required descendants closed.

Writing or revising this DAG records work; it does not execute or close the nodes.
During M1 source implementation, `DEV-58` defers Sage, tests, QC, notebook execution and live megadoc generation until the daily-core session starts T; inspect current source alongside the existing generated reference. Later milestone repairs keep focused execution active.
Specimens stated below describe mathematics and do not invent callable APIs.

### Delivery and regression boundaries

The unit of source delivery is the repaired owner together with the actual consumers of its changed contract.
At selection, identify that family from declarations, construction routes and callers, and compare it with the original requirement.
At closure, account for every required route and regime in the delivery commit.
Keep only concrete unfinished obligations in the node.
No additional registry or compliance artifact is required.

| Boundary being changed | What must hold before its consumer proceeds |
| --- | --- |
| Admission or a defining equation | The owner distinguishes decided laws, construction-derived laws and unresolved hypotheses on the actual datum. A dependent conclusion carries those hypotheses; a category label or caller assurance cannot turn them into established laws. |
| Mutually recursive constructors | The common repair supplies a well-founded construction on fixed data and a real consuming map. Neither half closes on the promise that the other will later remove the recursion. |
| A producer with private access, placement or inherited-operation defects | Repair those defects on the affected route in this delivery. Later boundary, membership and inheritance sweeps own independently untouched routes only. |
| A later edit to a delivered contract | Preserve its previous equations, generality and separating specimens. Inspect the changed owner and affected callers against the preceding delivery; before T bank the additional evidence, and during T re-execute it. |
| A counterexample to a shared repair method | Inspect its other applications and restore the affected prerequisite before consuming it. Reopen that concrete obligation with its original burden; independently established work stays closed. |
| A whole-family claim | Reconcile the source-derived family with the requirement clause by clause, including helpers, alternate constructors and inherited paths. Passing a specimen or exhausting the first search cannot close an uninspected route. |

For example, an equalizer factorizer delivered by admission cannot retain an unchecked flag or open another object's engine on the ground that `private-owner-boundaries` comes later.
Conversely, an unrelated untouched geometric adapter does not become a prerequisite of this module repair.
The residue sweeps below reconcile that remainder across the full named scope.

### Bounded closure

This queue preserves the full required scope while avoiding repeated whole-tree reconstruction.
Select the earliest ready shared repair with its consumer; then prefer ready geometric work.
Independent arithmetic remains required but does not block a geometric route that does not consume it.

For each subtree or repository sweep, establish its finite source population and obligation family at entry from the live tree, the original requirement and the implicated declarations.
Cover each route once under that sweep's stated questions.
Reuse earlier source evidence only after checking that neither the route nor its dependencies changed.
Record the inspected boundary in delivery commits; keep concrete findings in the existing open node or an actual repair prerequisite.
Search counts are navigation aids, never the progress measure.

A repair triggers review of its diff, its consumer impact and the relevant proof, not another unrelated whole-tree pass.
A newly discovered dependent defect extends that repair's obligations; a newly discovered independent required defect gets its own owner and edge.
Neither creates a new general audit round.
The terminating condition is complete stated coverage, no unresolved required finding, and preserved evidence for every changed route on the closing tree.
It is not a claim that arbitrary future scrutiny could never find another defect.

Every source-backed defect within a sweep's stated obligations is required work.
Severity labels, a new owner or a later audit cannot remove that burden.
Source review must establish a causal reduction: the repaired owner supplies the needed datum, its real consumer uses it, and the former bypass is no longer needed there.
More policies, lower scan counts or a passing specimen alone do not establish that change.

Repeated failure of the same equation or recurrence of the same bypass stops leaf patching: repair the shared cause and review the sibling routes that used it.
If the necessary maintained operation or authority cannot be obtained, leave the exact obligation open, report its missing input and continue independent ready work.
Do not claim convergence, reduce the domain or invent a local replacement to force closure.
New functionality unrelated to these obligations remains outside this convergence pass.

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

Select a node with no remaining prerequisites in the earliest unfinished milestone, subject to the existing geometry priority.
Apply `DEV-61` to foreign edits or reservations; do not create a claim layer.
Priority is a preference among ready nodes, not an edge.
File conflicts, shared owners, and related mathematical subjects are not dependency edges either.
Completion does not block ordinary geometry that does not use it; an unrelated arithmetic gap does not block geometry.
Repair a newly discovered prerequisite at its owner and record the actual dependency before extending its consumer.

An edge names the output described by its prerequisite's acceptance contract.
When only an independently deliverable part is needed, split that concrete output into its own node, transfer its obligations intact, and redirect only the affected edges.
Do not force a consumer to await an entire broad workstream.
Do not remove an edge because its prerequisite is inconvenient, deferred, or merely represented by a class.
General module products and equalizers are shared inputs; diagram specialization and completion consume those constructions with their own defining maps.
The general construction does not wait for completion's implementation.

Before committing a queue change, check that every checkbox has exactly one ID and one Needs list, IDs are unique, all references resolve, and there is no self-edge or cycle.
M1 source nodes must feed `architecture-remediation` and its usability session. Every later required node must reach its milestone acceptance node. The explicit milestone gate edges keep feature growth after frozen-API acceptance.
Once the daily-core execution phase begins, newly exposed repairs feed the still-open acceptance or audit node that found them, whose acceptance includes re-execution of affected proof.
Do not resurrect closed phase nodes or restart the source-phase execution suspension.
The milestone acceptance nodes form the required delivery chain.
No required or terminal node may depend on an optional node.
Optional work must name its concrete consumer and dependencies before implementation; a required engine repair belongs in the required consumer's dependency path, never in the optional branch.

Remove a delivered node and its incoming/outgoing edge references in the same queue transaction, after inspecting the delivered output.
Preserve unfinished residue under its ID, or split it without dropping any obligation.
An absent ID is never an implicit completion record: dangling references are errors to reconcile against source and git evidence.
Keep completed history in commits.
Repairs and re-execution within terminal verification do not create a back-edge to an earlier terminal node.
New failure-specific work becomes a prerequisite of the still-open terminal repair or final-verification node, with the required re-execution in its acceptance.
Preserve the phase-T execution rules.

## M1 — Daily mathematical work

Repair the existing public construction routes and inherited methods before proving the daily core. Placement and engine audits cover the existing preamble; the exercise core tests mathematically useful composed pathways.

- [ ] **`placement-audit`**. **Needs:** none.
  **Inspection surface:** use the opt-in [architecture inspection recipes](docs/architecture-inspection.md) to choose source and live slices, constructor/call evidence, repeated introductions and private-access candidates. These tools support mathematical review; their output is not an acceptance gate or a substitute for the category definitions and construction trace.
  **Owner and delta:** every public object and element operation introduced on each owned category, judged by the `CAT-05` placement test: an operation introduced on `C` is misplaced when it is well-defined on a supercategory of `C`, and moves to `max W_f` over the up-set `U_C = {D > C}`. Include arrow operations and inspect the delivered Mor-category inheritance: an arrow operation can move only to an arrow type that the arrow types below inherit.
  At its home an operation decides computability in one `case`/`match` on categorical containment: each case with a known algorithm routes to it, and the final `case _` asserts, naming the missing algorithm (`CAT-01`; AGENTS.md, *Abstract contracts are distinct from partial algorithms*). An operation placed low because only there can it be computed is the commonest misplacement: `conjugacy_classes`, `conjugacy_class`, `conjugation_g_set`, `left_cosets` and `right_cosets` sit on `Groups().Finite()` (`categories/group/groups.py`) though they are defined for every group, and they move to `Groups()` with the finite case as a route.
  Instrument: `just preamble-megadoc`, then `just placement [CATEGORY ...]`, forms the slice: for each category it prints the introduced object, element and arrow operations and the up-set `U_C` with each member's definition.
  It decides nothing about placement; `W_f` and its maximum come only from the investigation in the loop body.
  It also prints three mechanical findings: a name introduced on `C` and again in `U_C`; the lowest categories of `U_C` whose arrow type the arrow type of `C` does not inherit, and every Mor class that declares no arrow type; and each name introduced on pairwise incomparable categories, with their minimal common upper bounds in `P`. Loop body: one category `C`, with all of its introduced object and element operations handled together in the one pass.
  State the definitions of the categories in `U_C`. For every operation `f` introduced on `C`, state its mathematical definition with the data and hypotheses it uses, read from a source, never from its method body, which may use only what `C` happens to compute.
  Then decide, for all of them at once, which members `D` of `U_C` supply that data and satisfy those hypotheses for every object of `D`. Those members form `W_f`, and `max W_f` is the home of `f`. Move every operation whose home is above `C`, and route its computation.
  The categories are independent.
  A move that cannot be made in the loop body becomes its own node, named by the mathematics it needs, and this node `Needs` it: several maximal elements of `W_f`, or a maximum absent from `P`, is a missing category, axiom or property, or a defect in the declared graph; a consumer that breaks because it reached the operation through the old placement is repaired in the same loop body.
  `category-method-coverage-sweep` calls every method where it currently sits, so it certifies the current placement and cannot detect a misplacement; this node supplies that check.
  Each move is witnessed by an expectation that calls the operation on a specimen of the supercategory that is not in `C`. **Closure specimens:** `conjugacy_classes` asked of an infinite group reaches its own assertion, not an `AttributeError`; every owned category in the survey has had its pass, and each operation it moved answers on a specimen of its new home that is not in `C`.
  **Extension contract:** place the mathematical operation at the weakest sufficient structure; keep its signature, defining maps and existing computable cases usable as new cases arrive. Use category-aware `match`/`case`, specialization, or an owner-local algorithm registry with explicit applicability and precedence. Registration must not make a general category import or enumerate its descendants. Overlapping cases must select a mathematically compatible implementation. A new backend or case adds capability through this extension point; it must not narrow the old domain or replace inherited semantics. A substantial refactor carries an explicit contract change and the affected mathematical proof.

- [ ] **`engine-wiring-audit`**. **Needs:** none.
  **Owner and delta:** every owned construction that computes, itself, behaviour a maintained engine provides, starting with the set layer (`categories/sets/`): membership, position and order of finite sets, images, products, coproducts, power sets and function sets, as tabulated in [COMPLAINTS.md](COMPLAINTS.md#set-theoretic-behaviour-is-re-implemented-instead-of-wired-to-a-set-engine), then the whole preamble.
  **Invariants:** public mathematics stays owned; the computation behind it is the engine's, reached privately at its owner (`OWN-06`). A membership decision follows the set's definition -- predicate, identity of listed points, inverse of an image -- and never searches an enumeration.
  An enumeration is a chosen bijection from an ordinal, separate from membership.
  No owned code re-implements what Sage, GAP, SymPy, PARI or the Python standard library computes, unless the engine lacks it, which is then recorded in `TRAPS.md` with the measurement.
  **Coverage:** survey the preamble once for owned code whose body is a general algorithm -- loops that search, compare element by element, enumerate to decide, or rebuild an object to read one value -- and map each to the engine routine that computes it or to the recorded reason there is none.
  The profiled sites of 2026-09-23 are the first evidence, not the population.
  **Closure specimens:** membership of a point in a finite set of SR symbols, an image, a product and a power set answered without comparing against every point; a rank-16 diagonal lattice built in time linear in its Gram entries; each audited family's route read from its public entry to the engine call.
- [ ] **`framing-labels-are-owned`**. **Needs:** none.
  **Owner and delta:** `Lattices(R)._call_` (`categories/lattices.py`, docstring at line 841) and the framed free module it builds. When no `module_generators=` is given, the free module of rank `n` is the free module on the ordinal `{0, ..., n-1}`, an owned finite ordered set of natural numbers, and `module_generator(i)` takes `i` in it. Today the default generating set is `{e_0, ..., e_{n-1}}` with each `e_i` an element of Sage's Symbolic Ring: the label reaches the session as a raw Sage `Expression` (`OWN-01`), and `M.module_generator(0)` raises `ValueError` because `0` is not a label. Observed 2026-10-07 on `Lattices(ZZ)([[2, 0], [0, 2]]).unformed_module()`. The names `e_i` stay a printing convention of the element, never the label.
  **Consumers:** `tests/constructions/test_geometry_and_analysis_construct.sage` (`test_a_gram_tensor_and_its_pullback`) and the `tests/modules/` files that call `module_generator(0)`; the performance half is `engine-wiring-audit`.
  **Closure:** `Lattices(ZZ)([[2, 1], [1, 2]]).unformed_module().module_generator(0)` is the first basis vector, and the generating set of that module is a set of natural numbers of cardinality 2 with no Symbolic Ring element in it.

- [ ] **`group-categories-defined-by-data`**. **Needs:** none.
  **Owner and delta:** `categories/group/groups.py`. The groups whose category is fixed by mathematical data, per `CAT-28`: `SymmetricGroups()(Omega)` for a set `Omega`, `GeneralLinearGroups()(R, n)`, `FreeGroupQuotients()(F, R)` (a free group and a set of relators), `CoxeterGroups()(M)` for a Coxeter matrix, and an `Arithmetic` axiom on `OwnedGroups`. Each is built from main's current `groups.py`, with its morphisms and its `CAT-22` owner search.
  `remediate/groups` (`bbce862e3`, deleted 2026-09-25) drafted these, and complaint 10 in `COMPLAINTS.md` records why that draft was rejected: it replaced working catalogue entries with assertions, and it gave a number field the automorphism group of the original field as its Galois group.
  **Closure:** `SymmetricGroups()(Sets.Delta[2])` has order 6; `GeneralLinearGroups()(GF(2), 2)` has order 6 and is isomorphic to it; `FreeGroupQuotients()(F_2, {a^2, b^3, (ab)^2})` has order 6; `CoxeterGroups()` of the `A_2` matrix is that same group; the arithmetic axiom holds for `SL_2(ZZ)`.

- [ ] **`function-spaces-are-subobjects-of-mor`**. **Needs:** none.
  **Owner and delta:** the owned function spaces (`categories/functions/real_functions.py`), under `CON-17`. Each space is a family of functors in both arguments, and its constructor takes both: `C(n, A, B)`, `Lp(p, A, B)`, `ell(p, A, B)`; the tests now construct `C(Infinity, RR, RR)`, `Lp(2, RR, RR)` and `ell(2, NN, RR)`. Coordinates are owned by the domain: `RR.coordinate()` is the coordinate of ℝ (for ℝ² it is the pair (x = (x_0, x_1))), and a map is built from it, `C(Infinity, RR, RR)(x^2 + 1)`. `Lp(p)` (maps ℝ → ℝ) is built with `indeterminate=SR.var("x")` and `ell(p)` (maps ℕ → ℝ) with `SR.var("n")`; each stores the variable, hands it out as `indeterminate()`, and reads `space(expr)` as the map t ↦ expr.
  The delta: each space is the subobject of `Sets().Mor(X, Y)` cut out by its condition (integrability, summability, smoothness, boundedness), with its module structure; element construction is `Mor(X, Y)`'s element constructor (callables, formulas binding their own variable, finitary data), and the space admits the element by its condition; `indeterminate()` and the stored variable are removed, together with their consumers: `convolution.py` and `lebesgue_quotients.py` substitute into `parent().indeterminate()`, and `modules/pure/function_modules.py:378` defaults a formula's variable to `x`. Each works on the map it is given.
  **Observed:** the formulas are Sage symbolic expressions in the stored variable, and owned numbers never enter Sage's symbolic ring (`AGENTS.md`, ruled 2026-09-23), so `x**2`, `2 ** (-n)` and `1 / (1 + x**2)` raise `TypeError` in `tests/functions/test_function_modules_archive.sage`, `test_real_functions.sage` and `test_young_convolution.sage`. Those tests use `indeterminate()` and are rewritten with the delivery to define their maps (`f(t) = exp(-t^2)`). **Closure:** the maps t ↦ t², t ↦ 1/(1 + t²), t ↦ exp(−t²) and k ↦ 2⁻ᵏ, each defined with its own variable, are constructed in `Mor(X, Y)` and admitted by their spaces; no space supplies a point of its domain, and `X.coordinate()` of a function space, where it exists, is a general element of that space.

- [ ] **`scalar-extension-is-order-independent`**. **Needs:** none.
  **Site:** `categories/algebras/`, algebra scalar extension along `ZZ -> QQ`. `tests/algebras/test_algebra_base_change_archive.sage::test_archived_algebra_base_change_is_the_live_scalar_extension_functor` passes when its file runs alone and fails when `tests/modules`, `tests/sets`, `tests/rings`, `tests/forms` and `tests/tensors` ran first in the same process, with `TypeError: cannot apply Algebra scalar extension along ZZ -> QQ ... to Generic endomorphism of Ring over Integer Ring: it is not a morphism ... of Category of algebras` (observed 2026-09-26, before and after the coordinate sweep).
  A construction whose answer depends on what the session built earlier reads shared state that some earlier construction changed; the node finds that state and makes scalar extension read only its own data.
  **Closure:** the test passes in the batched run.

- [ ] **`genera-are-finite-sets-of-isometry-classes`**. **Needs:** none.
  **Owner and delta:** `Genus` in `categories/lattices.py` (line 371) is a plain Python class holding a signature and a discriminant quadratic form.
  A genus of integral lattices is the finite set of isometry classes of lattices with that signature and discriminant form, so it is an object of a category of genera that forgets to finite sets.
  Its cardinality is the class number, and parity (even or odd) is an axiom on it, the same for every member.
  It is constructed through its owner, not as a bare class, per `CAT-28`. `representatives()` and `class_number()` become that set's enumeration and cardinality.
  The spike built this and it reached main's history as PR #59 (`d2891a225`) and `5766b97d1`, then was lost when the spike was absorbed; do not port that code.
  The genus exists for odd lattices too, and genera have an equality: `Lattices(ZZ).isometry_classes` then groups a family by the owned genus instead of by Sage's local symbols in private (`COMPLAINTS.md`, *The genus of an odd integral lattice has no owned object*).
  **Closure:** the genus of `E8` has cardinality 1; the genus of `E8 + E8` has cardinality 2 (`E8 + E8` and `D16^+`); the genus of `A2` is even; the genus of `I_1 + I_1` is odd; `representatives()` enumerates that finite set.

- [ ] **`construction-is-instant`**. **Needs:** none.
  **Owner and delta:** every constructor in `src/dzack_research/preamble/`, under `OWN-22` and `OWN-24`. The global strict-checking flag exists at one owner, off by default; every well-definedness check is a validator method that construction calls after the object exists and that returns at once while the flag is off; every datum beyond the defining one is computed on first request and cached; every loop over pairings is the tensor equation it states.
  **Population tells (rerun per subtree):** `rg -n 'def __init__|def _element_constructor_' -A40` followed by a check, `assert`, `.inverse()`, `is_injective()` or a generator computation; `rg -n 'check: bool = True'`; `rg -n 'for .* in .*:' ` whose body pairs two elements; a method computing an object's datum without `cached_method`. The first specimens are `lattice_morphisms.py` (eager linearity, injectivity, surjectivity and inverse in `LatticeMorphism`, the embedding and isometry constructors, and eager group generators in `LatticeIsometryMor`) and `form_modules.py` (`_form_square_commutes`, and `b()` at 60 ms a call), and `group/groups.py`, where `_own_group` decides commutativity through `engine.is_abelian()` while it places the group, so that `Groups.Coxeter(["A", 2])` raises `NotImplementedError` from Sage's `CoxeterMatrixGroup`. `LatticeIsometryMethods.__init__` (`lattice_morphisms.py`) routes on a class pattern, `case CategoricalIsomorphism():`, which is `isinstance` under another syntax: an isometry built from a module isomorphism is a construction of the isometry Mor category on that datum, chosen by its category membership, not by the class of the argument.
  In `group/g_sets.py`, `_permutation_from_point_map` asserts at construction that a point map is a bijection by counting the preimages of every point, quadratic in the number of points; the check belongs in a validator of the permutation.
  Engine answers checked at construction: `lattice_engines.py:589-599` checks the shape, symmetry, unimodularity and evenness of the Leech Gram matrix OSCAR returns; `lattices.py:3014` and `lattice_morphisms.py:1255` check that an embedding OSCAR returns is primitive; `lattices.py:3075` asserts primitivity of each glue summand on every call. Each is a validator of the constructed lattice or embedding. `GradedModuleMor._element_constructor_` (`modules/graded_modules.py`) routes on `isinstance(images, ModuleMorphismMethods)` and `GradedModuleMorphismMethods`, not on Mor membership.
  **Measured specimen (2026-10-07), the lattice-db card build:** `ZZ.free_module(r).equip_bilinear_form(QQ, G)`, then `.twist(m).gram_tensor()`, then `Lattices(ZZ)(gram)`; the isometry partition of 20 definite cards of rank at most 6 takes 0.11 s. The last step, `Lattices(ZZ)(gram)`, costs 2.5 ms at rank 2 and 8.3 ms at rank 6. Cumulative over those 20 cards, the bilinear-forms space that `twist` constructs costs 0.54 s and `Mor ... Of` 0.74 s. `support()` of a free-module element (`framed_free_modules.py`) costs 1.4 ms at ranks 3 and 6, part of it constructing `Mor_Set(A, X)` (0.19 ms at `|A|` 3 and 6) for the inclusion of the new finite subset in `_from_finite_members`: the subset's defining datum is that inclusion. `NN**2` returns its interned product but costs 3.2 ms for 20 calls, against 0.22 ms for 20 calls of the `cached_function` `_bidegrees()` (`tensors/tensor.py`) that caches it a second time: each call of `Sets.ObjectType.__pow__` builds the constant family over `Δ[n-1]`, passes it through `_finite_factor_family` and the factor membership checks, and forms the key before the lookup; which of these steps holds the cost is unmeasured. Closure for this specimen: `X**n` for one set `X` and one `n` reaches its interned product at the cost of a lookup, `_bidegrees` is deleted, and its call sites write `NN**2`. `_MorCategoryOf.Of` (`abstract_categories/mor_categories.py`) builds a fixed Mor category for every supercategory that admits both endpoints and discards all but one: 100 requests of `Sets().Mor(A, X)` built 122 (2026-10-07). It constructs the one Mor category of the requested placement. Closure for this specimen: the card build is dominated by reading the card, measured at two ranks.
  **Placement validators need placement-independent statements:** `CategoricalMor.validate_placement` asks each certifying statement of the placement after construction. `Modules(R).Projective()` states `projectivity_decision`, which reads the module's data. `Modules(R).Torsion()` states `is_torsion` (`modules/pure/modules.py`), which answers `True` by placement, so a validator over that placement cannot fail; `FormModules(R).Nondegenerate()` states `is_nondegenerate` (`framed/formed/form_modules.py:1263`), which does the same. Closure: each certifying statement in `modules.py`, `form_modules.py` and `rings/number_fields.py` decides its property from the object's data, so `strict_checking()` falsifies a wrong placement.
  **Closure:** constructing an isometry of `E8` from its matrix runs no check and no inversion while the flag is off and runs its validator, `codomain.gram_tensor().pullback(f)` compared with `domain.gram_tensor()`, when it is on; `O(E6).cardinality()` is 103680 and the group is built in time dominated by the engine's group computation, measured at `A2`, `D4` and `E6` with the curve recorded.

- [ ] **`isometry-is-decided-without-a-witness`**. **Needs:** none.
  **Owner and delta:** `LatticeIsometryMor._isometry_decision` in `categories/lattice_morphisms.py` answers `Isom(L, M).is_empty()` by constructing an isometry: `is_globally_equivalent_to(..., return_matrix=True)` for a definite pair and `sage_indefinite_port`'s `isometry` for an indefinite pair of rank at least 3, so `L.is_isometric(M)` builds a morphism to answer a yes-or-no question.
  `Lattices(ZZ).isometry_classes` decides the same relation without a witness (PARI `qfisom` against a stored `qfisominit`; Hecke `is_isometric` through `_OscarLatticeAdapter.integer_lattices_are_isometric`), so the tree holds two decisions of one relation, with two indefinite engines.
  The decision that `M` is isometric to `L` is one operation; `is_empty()` and `isometry_classes` both ask it, and `an_element()` alone constructs the isometry.
  **Closure:** `A2.is_isometric(A2')` for `A2'` the form `[[2, 1], [1, 2]]` constructs no element of `Isom(A2, A2')`; `diag(2, 7, -64)` and `[[2, 0, 0], [0, -4, 2], [0, 2, 111]]` (one genus, two spinor genera) are not isometric through `is_isometric` and through `isometry_classes`, by one decision.

- [ ] **`daily-core-exercises`**. **Needs:** `placement-audit`.
  **Owner and delta:** a broad, bounded mathematical exercise core under the existing object and session test conventions. Select from the live public API and the research notebook before executing; keep its collection explicit in the existing test configuration, with the exercised mathematical contracts in the test files. Include rings and their ideals, quotients and localizations; free and nonfree modules, linear maps, kernels, images, cokernels and base change; groups, actions and quotients; forms and lattices; affine and projective schemes, morphisms and basic geometric constructions. Use small examples over integers, rationals, finite fields and polynomial or quotient rings, and finite/infinite and degenerate/nondegenerate cases where the operation claims them.
  Construct each selected object through its sanctioned entrypoints and exercise all of its mathematically applicable public object, element and morphism methods. Assert independently known values, equations, universal maps and compatibility with change of base. Follow the test guidelines and `tests/constructions/CONTRIBUTING.md`; existence, category membership and agreement between two calls alone do not establish a mathematical result. Parameterization must vary mathematical cases, not multiply identical witness checks.
  **Acceptance:** the core covers composed day-to-day pathways, including localization followed by module scalar extension, a presentation followed by a quotient and its induced map, a group action followed by an orbit or stabilizer, and a scheme construction followed by its maps. Include notebook display and session-order specimens. Record genuine unsupported algorithms explicitly; an assertion from an unsupported branch is boundary evidence, not a successful computation. A missing operation needed by a selected workflow is an owner repair prerequisite, not grounds to shrink the core. Bank these specimens for execution by the usability session; preserve the broader suite for its later audit.

- [ ] **`vinberg-invariants-are-points-of-the-projective-line`**. **Needs:** none.
  **Owner and delta:** `VinbergInvariantMatrices.vinberg_invariant` (`categories/vinberg_invariants.py`) returns the invariant `[4 b(r,s)^2 : q(r) q(s)]` as an `R`-point of the owned `P^1_R`, that is, a morphism `Spec R -> P^1_R`; for normals of positive square it dehomogenizes to `4 g^2` for the entry `g` of the Gram matrix of the unit normals (Vinberg 1985, section 1). The owned `ProjectiveSpaces(R)(1)` has no constructor from homogeneous coordinates, so every label of an invariant matrix and its `weighted_graph()` fail today. Over a principal ideal domain the point is that of the primitive pair, since `P^1(R) = P^1(K)`; the construction states this hypothesis and asserts outside it. Complaint: [A Vinberg invariant is not yet a point of the projective line](COMPLAINTS.md#a-vinberg-invariant-is-not-yet-a-point-of-the-projective-line).
  **Closure specimens:** for the `A_2` invariant matrix over `ZZ`, the off-diagonal invariant is the point `[1 : 1]` and the diagonal invariant is `[4 : 1]`; `weighted_graph()` is an object of `LabelledGraphs()` with two vertices, one edge, and those labels.

- [ ] **`coxeter-diagrams-construct-from-their-data`**. **Needs:** none.
  **Owner and delta:** `CoxeterDiagrams` (`categories/coxeter_diagrams.py`) is the constructor of its objects: the category applied to a Coxeter diagram's defining data, a Coxeter matrix `m: V x V -> Card` or a finite family of roots of a lattice, constructs the diagram, and equals `from_coxeter_matrix(m)` or `from_roots(roots)` on the same data. Today the category has no element constructor, and `CoxeterDiagrams()(datum)` raises `NotImplementedError`. A Cartan type is the third datum the tests apply the category to; it enters as a Sage `CartanType`, which `coxeter-diagram-orders-are-owned-posets` already names as engine input. Complaint: [A Coxeter diagram is not constructed by its category](COMPLAINTS.md#a-coxeter-diagram-is-not-constructed-by-its-category).
  **Closure specimens:** `CoxeterDiagrams()(Lattices(ZZ)([[-2, 2], [2, -2]]).module_generators())` equals `CoxeterDiagrams().from_roots(...)` on the same roots; `CoxeterDiagrams()([[1, 3, 3], [3, 1, 3], [3, 3, 1]])` is the affine `A_2` triangle; `tests/lattices/test_coxeter.sage`, `test_coxeter_subdiagrams.sage` and `test_vinberg_invariants.sage` no longer fail on the category call.

- [ ] **`the-session-matrix-takes-its-ring`**. **Needs:** none.
  **Owner and delta:** the session's `matrix` (`preamble/language_runtime.py`) constructs the matrix over a named ring `R`: `matrix(R, rows)` and `matrix(R, m, n, f)` with entries `f(i, j)` in `R`, as well as `matrix(rows)` with the ring read from the entries. Today it takes one positional argument, so `matrix(ZZ, [[4, 1, 1], [1, 4, 1], [1, 1, 4]])` raises `TypeError`. Complaint: [The session matrix does not take its ring](COMPLAINTS.md#the-session-matrix-does-not-take-its-ring).
  **Closure specimens:** `matrix(ZZ, [[4, 1, 1], [1, 4, 1], [1, 1, 4]])` is a matrix over the session's `ZZ`; `matrix(ZZ, 3, 3, lambda i, j: (i + 1) * (j + 1) + (1 if i == j else 0))` (`tests/user_simulations/test_newcomer_session.sage`) has determinant 15.

- [ ] **`a-finite-cardinal-is-a-natural-number`**. **Needs:** none.
  **Owner and delta:** the integers' element constructor (`categories/rings/ring_foundation.py`) accepts a finite cardinal as the natural number it is, the image of the cardinal under `NN -> ZZ`. A cardinal is an object of `Cardinalities` (a parent), so `element_parent` returns its class, and `ZZ(c)` raises `TypeError: category() needs an argument` from `Modules(ZZ).__contains__`. `RegularPolytopes.dimension()` (`categories/schemes/polytopes.py`) converts `schlafli_symbol().cardinality() + 1` into `_own_ring(SageZZ)` and so fails for every polytope. Complaint: [A finite cardinal does not convert into the integers](COMPLAINTS.md#a-finite-cardinal-does-not-convert-into-the-integers).
  **Closure specimens:** `ZZ(finite_ordered_set((4, 3)).cardinality()) == 2`; the cube `RegularPolytopes().from_schlafli_symbol("{4,3}")` has dimension 3.

- [ ] **`coxeter-diagram-orders-are-owned-posets`**. **Needs:** none.
  **Owner and delta:** `PartiallyOrderedSets()` (`categories/sets/set_categories.py`) constructs a finite poset from its underlying finite set and its order relation; `CoxeterDiagrams` (`categories/coxeter_diagrams.py`) answers the subdiagram order (inclusion of vertex sets) and the order that inclusion induces on `Aut`-orbits of subdiagrams as such objects, in `subdiagram_poset`, `elliptic_subdiagram_poset`, `parabolic_subdiagram_poset`, `subdiagram_orbit_poset`, `elliptic_subdiagram_orbit_poset` and `parabolic_subdiagram_orbit_poset`, which return Sage `Poset` today (`OWN-03`). `plot()` returns a Sage `Graphics`. `from_coxeter_matrix` (a Sage `CoxeterMatrix`), `from_cartan_type` (a Sage `CartanType`) and `Groups.Coxeter` (any Sage datum) admit engine input (`OWN-04`). Complaint: [Coxeter diagrams answer subdiagram orders and drawings as Sage objects](COMPLAINTS.md#coxeter-diagrams-answer-subdiagram-orders-and-drawings-as-sage-objects).
  **Closure specimens:** the `A_2` diagram's `subdiagram_poset()` is an object of `PartiallyOrderedSets()` of cardinality 4 whose maximum is the diagram and whose minimum is the subdiagram on no vertices; no public method of `CoxeterDiagrams` returns or accepts a `sage.*` object.

- [ ] **`modules-over-a-group-algebra-keep-the-module-axioms`**. **Needs:** none.
  **Owner and delta:** `Modules(R[G])` is the category of modules over the ring `R[G]` (AGENTS.md, *Group modules are `Modules(R[G])`*), so `Modules(R[G]).Free()`, `.FinitelyGenerated()` and every other axiom of `Modules` exist on it. `Modules.__classcall__` (`modules/pure/modules.py`) constructs `ModulesOverGroupAlgebra` (`modules/group_modules/group_modules.py:90`), a Python subclass of `Modules`, when the base is a group algebra. Sage's `CategoryWithAxiom.__classget__` (category_with_axiom.py) asserts that a nested axiom class is read from its own base class (`TRAPS.md`, *A Python subclass of a category class loses its axiom classes*), so `Modules(ZZ[C2]).Free()` raises `AssertionError: base category class for Modules.Free mismatch`. `_equip_action` (`group_modules.py`, `group_algebra.free_module(labels)`) reaches it, so `Modules(R[G])(M, rho)` fails for every `M`, and with it `Modules(ZZ).trivial_action(G)`.
  **Ruling owed (`DEV-65`):** the owner chooses the route. (i) `Modules(R[G])` is `Modules(R[G])` itself, and the group-algebra functors (induction, restriction, invariants, coinvariants) are methods of `Modules` that match on the base being a group algebra; this is the route the AGENTS.md ruling states. (ii) The subclass declares its own axiom classes, each a `CategoryWithAxiom` over `ModulesOverGroupAlgebra`. (iii) `ModulesOverGroupAlgebra` is a category with its own class that declares `Modules(R[G])` in `super_categories`, which the AGENTS.md ruling forbids.
  **Closure:** `Modules(ZZ).trivial_action(Groups.C(2))(Modules(ZZ).free_module(("n",)))` constructs; `Modules(ZZ[C2])(ZZ^2, rho)` constructs for the swap action `rho`; `tests/constructions/test_group_module_mor_construct.sage` and `tests/categories/test_adjunctions.sage` run alone with no `AssertionError` from the axiom classes.

- [ ] **`tensor-algebras-are-not-commutative`**. **Needs:** none.
  **Owner and delta:** the construction chain of a native free algebra, `_NativeFreeAlgebraParent` (`algebras/free_algebras.py`), `_OwnedAlgebraParent` (`algebras/algebras.py`) and `_OwnedRingParent` (`rings/ring_foundation.py`). `T(QQ^2) = QQ.free_module(("a", "b")).tensor_algebra()` lies in `Algebras(QQ).Associative().Unital().Commutative()`: its category has the commutative algebras as a supercategory, and `is_commutative()` answers True. Observed 2026-10-07: the engine's `is_commutative()` is False, and none of `FreeAlgebras(QQ)`, `GradedFreeAlgebras(QQ)`, `TensorAlgebras(QQ)` and `GradedAlgebras(QQ)` is a subcategory of the commutative algebras, so the commutative placement enters the join on another route of that chain, not yet located.
  **Closure:** `tests/objects/test_tensor_algebra_of_qq2.sage::test_the_categories_of_the_tensor_algebra` passes alone; the tensor algebra on one generator stays commutative.

- [ ] **`centres-of-algebras-on-infinitely-generated-modules`**. **Needs:** `tensor-algebras-are-not-commutative`.
  **Owner and delta:** `center()` on `Algebras(R)` (`algebras/algebras.py`) asserts that the underlying module has finitely many module generators. The centre `Z(A) = {z : za = az for all a in A}` of an algebra with a set `S` of algebra generators is the kernel of the `R`-linear map `A -> A^S`, `z -> (za - az)_(a in S)`, so a finitely generated algebra whose underlying module is infinitely generated, such as `T(QQ^2)` with its countable word basis, has a centre defined by finite data. A graded algebra with homogeneous generators has a graded centre, computed degree by degree on finite pieces.
  **Closure:** `tests/objects/test_tensor_algebra_of_qq2.sage::test_the_centre_of_the_tensor_algebra` passes alone.

- [ ] **`arrows-compare-through-richcmp`**. **Needs:** none.
  **Owner and delta:** every element and arrow type in `src/dzack_research/preamble/` decides equality in `_richcmp_` with a compatible `__hash__` (`STY-167`). The root host `OwnedSetMorphism` (`sets/set_categories.py`) routes `==` and `!=` to `_richcmp_`, so an `__eq__` on an arrow type below it shadows that protocol and makes equality depend on which class realizes the left operand.
  **Population tell:** `rg -n "    def __eq__" src/dzack_research/preamble` lists 88 sites on 2026-10-07, on parents and on elements; each site on an element or arrow type moves to `_richcmp_`. First specimens: `EquivariantMorphismMethods.__eq__` (`group/g_objects.py`) and `RingMorphism.__eq__` (`rings/ring_foundation.py`), which the root routing makes redundant.
  **Closure:** the tell lists no `__eq__` on an element or arrow type; an equivariant map `f` of finite `C2`-sets answers True to `f == f * id` and to `id * f == f`.

- [ ] **`one-mor-one-arrow-type`**. **Needs:** none.
  **Owner and delta:** an arrow of `C.Mor(A, B)` is an element of that Mor, realized by the arrow type the Mor category graph generates. `module_morphisms.py` constructs `_ScalarIdentityModuleMorphism` (for `scalar * identity`) and `_ZeroModuleMorphism` (for the zero map) directly, so one Mor holds arrows on two hosts, and every comparison or composition on that Mor must accept both. The scalar multiple of the identity and the zero map are the Mor's element constructor applied to their defining data. The arrows of `Sets().Mor(A, B)` and `FiniteSets().Mor(A, B)` are `OwnedSetMorphism` (`sets/set_categories.py`), outside the root of the generated arrow types, `CategoricalMor.ElementMethods` (`abstract_categories/mor_categories.py`). So they lack the protocol `_transport_initialization_to_mor`, by which a Mor with more structure threads its arrow through the arrow it is in the underlying category. A morphism of finite `G`-sets is a set map that commutes with the actions, and its construction fails there: `acted = FiniteGSets(Groups.S(3))((1, 2, 3), lambda g, p: g(p))`, then `acted.Mor(acted).identity()`, raises `AttributeError` in `EquivariantMorphismMethods.__init__` (`group/g_objects.py`). A composite of two `CategoricalIsomorphism` arrows (`abstract_categories/mor_categories.py`, `__mul__`) is parented by `_category_mor_parent(...)`, which returns the function-map substrate `arrow_set()` of the selected Mor (an `UnderlyingSetMor`, or Sage's `Hom` for a native category), not the Iso Mor. That parent has no `mor_category()`, so composing the composite again fails at `self.parent().mor_category().Core()`.
  **Population tell:** `rg -n "^class _.*Morphism\((ModuleMorphism|.*Morphism)\)" src/dzack_research/preamble` for a class instantiated with a Mor parent instead of through `parent(datum)`; `rg -n "class .*\((Sage)?SetMorphism\)" src/dzack_research/preamble` for an arrow host outside the generated root.
  **Closure:** `M.Mor(M)(0)` and `2 * M.Mor(M).identity()` are instances of `M.Mor(M).element_class`; `acted.Mor(acted).identity()` above constructs, and `tests/constructions/test_g_set_mor_construct.sage` passes.

- [ ] **`algebra-arrows-are-ring-arrows`**. **Needs:** none.
  **Owner and delta:** a unital associative `R`-algebra is a ring, and the forgetful functor `Alg^ua_R -> Rings` sends an algebra map to a ring map. The arrow type of `Algebras(R).Associative().Unital().Mor` does not inherit the arrow type of `OwnedRings().Mor`, so `is_group_algebra_augmentation` and `is_group_algebra_subgroup_inclusion` are stated twice: on `RingMorphism` (`rings/ring_foundation.py`) and on `UnitalMultiplicativeAlgebraMorphism` (`algebras/algebras.py`), where the restriction and induction functors of `Modules(ZZ[G])` read them from the augmentation `ZZ[G] -> ZZ`.
  **Closure:** the two predicates are stated once, on the ring arrow type, and the augmentation of `ZZ[C2]` answers both through inheritance.

- [ ] **`power-algebra-identity`**. **Needs:** none.
  **Owner and delta:** `Mor(A, A).identity()` of a power algebra (`algebras/power_algebras.py`, `identity`) builds the identity from the identity of the generating module and fails, because the power algebra has no chosen module resolution; observed on the exterior algebra on 2026-10-07. The identity of `A` is an arrow of the algebra Mor that needs no chosen resolution.
  **Closure:** `E.Mor(E).identity()` of the exterior algebra of `QQ^2` constructs and composes with itself to itself.

- [ ] **`modules-call-on-a-set-is-the-free-module`**. **Needs:** none.
  **Owner and delta:** `Modules(R)(S)` for an object `S` of `Sets()` is the free `R`-module on `S`, the value of the free functor, the same object as `Modules(R).free_module(S)`. `Modules._call_` (`modules/pure/modules.py`) reads its one argument as a scalar action and fails on a set with `AttributeError: codomain`. The routing is a `match` on `datum in Sets()` against a scalar action.
  **Closure:** `tests/groups/test_g_objects.sage::test_the_averaging_operator_of_s3_squares_to_six_times_itself_and_kills_augmentation` passes alone.

- [ ] **`unital-algebras-supply-their-unit`**. **Needs:** none.
  **Owner and delta:** a unital algebra's unit is part of its defining data, established at construction. `Monoids.ParentMethods.one` (`group/magmas.py`) is an abstract contract that the matrix algebra `QQ.matrix_space(2)` and the de Rham algebra (`algebras/restricted_graded_algebras.py:195`) leave unfulfilled, so `_center_algebra` (`algebras/algebras.py`) and `de_rham_algebra` raise `NotImplementedError: abstract method one`.
  **Closure:** `tests/algebras/test_algebra_preservation.sage::test_center_of_the_two_by_two_matrix_algebra_is_the_scalars` passes alone, and `de_rham_algebra` constructs.

- [ ] **`derivation-spaces-read-declared-data`**. **Needs:** none.
  **Owner and delta:** `DerivationSpace` (`algebras/derivations.py`) reads `_selected_module_presentation`, which no level declares (`modules/finitely_presented_modules.py`); it asks the module for its selected presentation through the public resolution accessor. The graded derivation `_element_constructor_` (`algebras/derivations.py`) constructs a derivation from a dict of generator images, as every other Mor of the tree does.
  **Closure:** a derivation space of a finitely presented algebra constructs, and a graded derivation is constructed from `{generator: image}`.

- [ ] **`group-resolution-augmentation-terminates`**. **Needs:** none.
  **Owner and delta:** the augmentation of the selected resolution of a group is a morphism of `Modules(ZZ[G])` from its degree-0 term to `ZZ`. `Groups.C(2).selected_group_resolution().augmentation()` raises `RecursionError` in the cardinality of a `FiniteOrderedSet`.
  **Closure:** that call returns the augmentation, whose image is `ZZ`.

- [ ] **`preimages-through-a-torsion-image`**. **Needs:** none.
  **Owner and delta:** a preimage under `f: F -> M` with `F` finite free and `M` torsion is a preimage through the image factorization `F ->> im f >-> M`. `ModuleMorphism.preimage` (`module_morphisms.py:1129`) lifts through `image.inclusion()`, whose `_preimage_or_none` (`:1263`) asserts a finite free domain, so it rejects every torsion image. The lift of an element along a monomorphism of presented modules is the module-level preimage through the codomain's presentation, never a search of the domain's elements (`:1117`).
  **Closure:** `tests/modules/test_tor_and_ext_of_finite_cyclic_groups.sage::test_multiplication_by_two_induces_zero_on_tor_one_of_z2_and_z2` passes.

- [ ] **`resolution-truncations-in-the-session`**. **Needs:** none.
  **Owner and delta:** a chosen resolution is truncated at an index in `ℕ ∪ {∞}`, where `∞` is a cofibrant replacement (`CAT-29`). `Resolutions` takes `Infinity` (`abstract_categories/resolutions.py:25`), but the session star import binds neither `Infinity` nor `oo`. So `tests/categories/test_resolution_categories.sage:9` imports it from `sage.rings.infinity` (TL01). The session presents the truncation index.
  The same file passes `FramedFreeModules(ZZ)` as the level category of a resolution and asserts `level(0) in FramedFreeModules(ZZ)`, at lines 61, 82, 91 and 130. TL08 (`utilities/test_lint.py:24`) bans naming a `Framed…` category anywhere in a test. `CAT-29` makes framed free modules the levels of a chosen free resolution. **Owner ruling owed:** whether a test may name a chosen-datum category as a parameter or a membership target, or whether `Resolutions` takes the level class some other way.
  **Closure:** `tests/categories/test_resolution_categories.sage` passes the test lint.

- [ ] **`restricted-scalars-modules-are-modules`**. **Needs:** none.
  **Owner and delta:** `RestrictedScalarsModules` (`modules/pure/modules.py`) constructs `Res_f(M)` along `f: R -> S`, and two module operations stop there.
  `is_torsion` and `is_torsion_free` answer `Unknown` for `Res_f(QQ^2)` along `ZZ -> QQ`. When `S` is a field and `f` is injective, every nonzero `f(r)` is a unit, so `Res_f(M)` is torsion-free, and it is torsion only when `M = 0`. A ring morphism out of `ZZ` is injective exactly when its codomain has characteristic `0`, because `ZZ` is initial.
  `base_change` is abstract on restricted-scalars modules, so the counit `QQ ⊗ Res(QQ^2) -> QQ^2` of `Modules(ZZ).base_change_adjunction` raises `NotImplementedError` (`functors/scalar_change.py:138`).
  `GF(2)["x"]` is a native free algebra with no `gen()`. The preamble spelling of its variable is `algebra_generator(label)`, and `tests/modules/test_restriction_of_scalars_on_morphisms.sage:63` calls `R.gen()`. The owner rules which spelling the session presents for the variable of a polynomial ring.
  **Closure:** `tests/modules/test_scalar_change_between_z_and_q.sage` passes, and so does `test_restricting_f2_x_mod_x2_to_f2_gives_a_plane_of_four_elements_on_which_x_squares_to_zero`.

- [ ] **`presented-modules-are-presented-by-their-relation-morphism`**. **Needs:** none.
  **Owner and delta:** a finitely presented module is the cokernel of its relation morphism `r: F(relations) -> F(module_generators)`, which it stores (`finitely_presented_modules.py`). `_torsion_module_presented_by_matrix` (`modules/pure/modules.py:5287`) and `from_relations_and_gram` (`framed/formed/form_modules.py:1735`, `:2107`) still take a family of relation coordinate rows; each takes `r` as its datum, and their callers in `modules.py`, `lattices.py`, `fraction_field_quotients.py` and `torsion_form_modules.py` build `r`.
  `Modules(ZZ).biproduct((M, M))` and `M + M` for the presented `M = ZZ/2 + ZZ/3` raise `TypeError`: the presented module is not hashable and has no `_cache_key()`, so the biproduct's unique-representation key fails.
  A 2-adic Jordan generator of the hyperbolic form on `ZZ/2 + ZZ/2` prints as `32*[0] + [1]`: the engine's representative of `0` modulo the `p`-adic precision is raised as the integer `32`, not reduced to its class in `ZZ/2`.
  **Closure:** the three constructors take a relation morphism; `M + M` constructs and has cardinality 36; the Jordan generators of the hyperbolic form on `ZZ/2 + ZZ/2` have coefficients in `{0, 1}`.

- [ ] **`finite-galois-stages-answer-as-their-fields`**. **Needs:** none.
  **Violated statement:** `OWN-15`: "construct the weaker object first and retain that exact object as part of the stronger object's defining data"; `AGENTS.md`, *Added structure enriches an object; it never wraps one*: "every set-theoretic answer -- cardinality, finiteness, ... -- is *inherited through the construction*".
  **Evidence:** over `F_q` the degree-`d` stage of `G_{F_q}` is the field `F_{q^d}` with its maps `F_q -> F_{q^d} -> Fbar_q`, an object of the slice `(F_q / Fields) / e` (`group/profinite/galois_quotient.py`, `FiniteGaloisExtension`). `AbsoluteGaloisGroup(GF(5)).finite_extension(3).cardinality()` fails: the stage object (`SliceCategory.parent_class[_FiniteGaloisExtensionEngine].ObjectType`) has no `cardinality`, so the operations of `F_125` do not reach it.
  **Policy search:** `CON-16`/`OWN-15` (chosen enrichment) make the stage its own object constructed on `F_{q^d}`, which is what the code builds; neither permits the stage to lose the operations of the field it is built on. `CAT-15`/`CAT-16` place the slice over `Fields` by its projection, which carries no rule that hides the field's operations.
  **Owner and delta:** the stage retains `F_{q^d}` as defining data, and the operations of that field reach the stage through the construction chain of the slice.
  **Closure:** `tests/constructions/test_galois_construct.sage::test_the_absolute_galois_group_of_a_finite_field` passes.

- [ ] **`continuity-is-membership-in-top-mor`**. **Needs:** none.
  **Owner and delta:** the forgetful functor `Top -> Sets` is faithful, so `TopologicalSpaces().Mor(X, Y)` is the subset of `Sets().Mor(UX, UY)` of the maps whose preimages of opens are open, and a set map lies in it exactly when it is continuous. `identity in TopologicalSpaces().Mor(sierpinski, indiscrete)` answers `False` for the identity of `{0, 1}`, which is continuous (`categories/topological_spaces.py`, `TopologicalSpaceMor`). Membership decides continuity on the preimages of the codomain's opens.
  **Closure:** `tests/topology/test_topological_spaces.sage` passes.

- [ ] **`architecture-remediation`**. **Needs:** `placement-audit`, `engine-wiring-audit`, `coxeter-diagram-orders-are-owned-posets`, `coxeter-diagrams-construct-from-their-data`, `the-session-matrix-takes-its-ring`, `a-finite-cardinal-is-a-natural-number`, `group-categories-defined-by-data`, `function-spaces-are-subobjects-of-mor`, `scalar-extension-is-order-independent`, `genera-are-finite-sets-of-isometry-classes`, `isometry-is-decided-without-a-witness`, `construction-is-instant`, `vinberg-invariants-are-points-of-the-projective-line`, `daily-core-exercises`, `modules-over-a-group-algebra-keep-the-module-axioms`, `tensor-algebras-are-not-commutative`, `centres-of-algebras-on-infinitely-generated-modules`, `arrows-compare-through-richcmp`, `one-mor-one-arrow-type`, `algebra-arrows-are-ring-arrows`, `power-algebra-identity`, `modules-call-on-a-set-is-the-free-module`, `unital-algebras-supply-their-unit`, `derivation-spaces-read-declared-data`, `group-resolution-augmentation-terminates`, `preimages-through-a-torsion-image`, `resolution-truncations-in-the-session`, `restricted-scalars-modules-are-modules`, `presented-modules-are-presented-by-their-relation-morphism`, `finite-galois-stages-answer-as-their-fields`, `continuity-is-membership-in-top-mor`. **Owner and delta:** the integrated source route from public category entry through complete defining data, private computation and every owned result and consumer, against the unresolved complaints affecting the existing public API and the daily core. Required capability additions retain their full contracts in M4; they are not prerequisites merely because they are unfinished. If a daily-core route actually consumes one of their outputs, split that prerequisite intact and put its edge here.
  **Invariants:** every M1 source descendant closes before this node; introducing a residual child keeps this node open.
  Each complaint's entire burden is discharged or retained in a required prerequisite.
  All alternative construction routes affected by a repair are inspected.
  No numerical answer, renamed field, new wrapper, source count or administrative record substitutes for delivery (`DEV-67`, `DEV-68`). **Closure comparison:** reconcile the original complaint/requirement clauses with the delivered owner and consumer routes, including the generality beyond their first specimens.
  Review later changes to each shared contract against its delivery evidence.
  In particular, an "assumed linear" rename, a framing proof depending on its own Mor placement, or a private access deferred from a delivered producer fails this comparison and reopens that exact repair.
  Existing evidence for unaffected routes remains usable.
  **Closure evidence:** bank falsifying specimens for every repaired obligation, including inherited operations, wrong nearby inputs and relevant infinite/nonfree/base-change cases.
  Commits record source coverage and unexecuted proof.
  Review composed consumers after their prerequisites, without rerunning an unrelated whole-tree inventory after every leaf.
  Source closure authorizes T; it does not claim runtime success.

- [ ] **`core-usability-session`**. **Needs:** `architecture-remediation`.
  **Pending tool execution:** regenerate the live survey with its source fingerprint and method source locations; exercise the Sage topology report on a triangle boundary versus its filled flag/order complex and on an isolated vertex (`tests/engineering/test_category_inspection_topology.sage`). Source-only queries and saved-snapshot queries have separate plain-Python CLI specimens. Keep these opt-in inspection utilities outside automated architecture gates.
  **Owner and delta:** start the execution phase defined by `DEV-58` and establish a preamble usable for ordinary mathematical work. Run the daily core in a fresh process and in composed sessions; use japi to execute the research notebook and inspect its rendered mathematics. Confirm startup, object display, tab/help discovery, maps and results through the owned interface. Regenerate the megadoc and category graph at this point and reconcile them with the live API.
  **Acceptance:** the selected workflows and their mathematical assertions pass, standard small constructions and displays respond within the applicable existing budgets, and session order does not change results. Diagnose failures by shared mathematical owner and repair the affected routes. Preserve every failure outside the core under `triage-long-tail` or its concrete repair node. Broad-suite failures do not prevent this milestone if they neither invalidate the core's mathematics nor expose an unresolved shared defect on its routes. This is executed usability evidence, not a claim that the whole suite passes. Runtime repairs and focused re-execution remain active after this node closes.

## M2 — Auditable minimal API

Use the executed core to settle the construction language and finite source audits. Carry forward unchanged placement evidence; repair each new finding at its owner.

- [ ] **`refactor-audit`**. **Needs:** `core-usability-session`. **Goal:** After the repaired mathematics runs end-to-end, audit the repository for duplicated authority, poor organization, and maintainability defects that survived the architecture work.
  Audit the whole repository for messy, disorganized or duplicated code after the complaint-derived architecture has been exercised through the daily public session.
  The public mathematical API need not change and should not change incidentally; this pass is about internal sources of truth, ownership and maintainability that survive the mandatory architecture repairs.

  Fix the whole-repository source population at entry and cover it once for organization, sources of truth, ownership and duplication.
  Inspect the authored owners of generated projections and any participating local changes; preserve unrelated foreign work.
  Review concrete declarations and consumers, not only search matches.
  Apply the bounded-closure rule above: a repair revisits its changed route and affected uses, without restarting the repository survey.

  Repair a bounded finding at its owner.
  If it crosses independent owners, give its concrete repair a DAG row with source-backed acceptance and make this node depend on it.
  Re-execute affected proof in the active terminal phase.
  Newly observed required findings are repaired by the same rule; they do not initiate another general audit.
  Do not create rows whose deliverable is only a report, inventory, approval or proof that the audit ran.

  **Acceptance:** the stated whole-repository coverage is complete, every resulting required finding is repaired, and the changed routes and their consumers have been reviewed and re-exercised on the closing tree.
  Unchanged, unaffected coverage carries forward; no second whole-repository discovery pass is required.
  Record the inspected coverage and residual uncertainty without claiming that no future defect can exist.
  A clean pass requires no receipt commit.

- [ ] **`type-paydown`**. **Needs:** `refactor-audit`. **Goal:** Improve static type information only where it clarifies the mathematics and makes correctness easier to reason about; do not contort code merely to lower an error count.
  Pay down type errors where doing so is reasonable, and not one step further.
  **Acceptance:** inspect the diagnostics from the prescribed typing boundary once, resolve their shared causes at the mathematical or typing owner, and give every retained diagnostic an evidence-backed disposition there.
  Check changed declarations and affected uses after each coherent repair; broaden only for a demonstrated new effect.
  No required behavior or proof is bypassed.
  Re-execute affected mathematical specimens after behavioral changes under the already-active terminal phase.
  Every typing decision must improve the legibility of the code, the ability to understand what it does, and the ability to reason statically about whether it is correct.
  That is the standard the change is judged against, not the error count.
  A retained false positive needs source-backed justification; a missing mathematical contract remains required work.

  Golfing the code into oblivion -- distortions that exist only to silence a checker -- is the failure mode.
  Where a contortion is genuinely warranted, it must be judged as significantly serving the goal above, and the argument for it recorded explicitly in the commit message.
  A type annotation nobody can read has made the code worse even when the checker is quieter.

- [ ] **`bloat-audit-loop`**. **Needs:** `type-paydown`. The legacy identifier is retained for stable references, but this is a finite terminal convergence pass, not a permanently open audit loop.
  Read the governing `AGENTS.md`, `CONTRIBUTING.md` and this DAG at entry.
  Use `policy-index` to select the review skill for the actual boundary, and load narrower skills only for findings that need them.
  Loading another skill supplies a method for the stated obligations; it does not create another workstream, proof requirement or repository-wide round.

  Fix the source population at the post-typing tree.
  Cover categorical/math owner placement; duplicate or derivable retained state; public type/API design; tests as behavioral proofs rather than implementation mirrors; dead compatibility bridges and validation-evasion fallbacks; dependency offload to Sage, GAP/CAP, OSCAR, SymPy, Python or another mature owner; import/lazy-import and module-cycle structure; notebook/session usability; generated/static projection boundaries; and AI-slop or locally tidy code that violates the architectural contract.
  Reuse the preceding audit's coverage for overlapping questions only where the route and its dependencies remain unchanged; complete the other questions across the whole repository once.
  Protected mathematical expectations retain their own correction rule.
  Search the dependency or upstream owner before improving a local mechanism that may not need to exist.

  Repair a small, well-supported finding and commit the behavioral regression or mathematical consumer that proves it.
  If a finding spans several owners, add a concrete repair row with the necessary edges; this node cannot close until that repair closes.
  Revisit the repaired route, affected callers and evidence.
  A repeated finding with the same cause requires shared-owner repair and review of its sibling uses, not another whole-tree search.
  Never create a node merely to say that an audit ran, and never leave a required finding in COMPLAINTS as a substitute for repair.

  **Acceptance:** every stated question has complete coverage, every resulting required finding has been repaired, and each subsequent change has its affected source and proof revalidated on the closing tree.
  Re-execute affected mathematical proof after repairs and confirm the final public session after bootstrap/export changes.
  Stop at that condition; there is no repeat-until-empty whole-repository discovery step.
  A clean pass makes no receipt commit.
  Later regressions are new owner-local defects and do not retroactively turn this completed convergence pass into a perpetual queue.

- [ ] **`constructor-discovery`**. **Needs:** `core-usability-session`.
  **Owner and delta:** audit the existing public construction families and give each one a single discoverable mathematical owner, defining datum and map contract. Direct construction, object methods, functor images, catalogue examples and raised results use that owner. Help, signatures and the generated reference lead a user from the category or object to the constructor; private implementation classes and global factory aliases are not competing entrypoints.
  **Core integration boundary:** use the [sage-categories constructor design](docs/constructor-architecture.md) to map module, formed-module and subgroup routes to the backing core before freezing a shared constructor mechanism. Constructor inheritance and implementation registration belong to its `construction_owner()`, selected `structure_functors()` and `Cat().implement(...)` interfaces. Missing generic introspection or binding belongs at that core owner; the preamble supplies mathematical leaves and private computation adapters. Report both current constructor/provider evidence and the target functor declarations through the existing opt-in tools. Full runtime replacement remains separately scheduled; this design constraint applies now.
  Compare ordinary method introspection, declaration decorators and owner-local implementation registries using the [constructor discovery assessment](docs/architecture-inspection.md#constructor-discovery-decorators-and-registries). Cover sets, rings, algebras, modules, formed modules and lattices. Select a mechanism from concrete routes in at least two families; distinguish collecting public constructor declarations from dispatching computational cases. Derive the catalogue from authoritative declarations, preserve category parameters and exact signatures, and expose source locations, inherited availability and any dispatch ambiguity through the existing opt-in tools. Establish reproducible provider loading without making general categories import their descendants. Record the selected architecture in CONTRIBUTING before changing runtime construction.
  **Acceptance:** for each family in the freeze scope, inspect the full route and exercise representative consumers. In particular a commutative ring owns `localization(S)` for its multiplicative submonoid, with the structure map and universal factorization; inversion, prime localization and fraction fields specialize it under their hypotheses. The owner is the commutative-ring category (or its equivalent refinement in the declared graph), not an arbitrary noncommutative ring with an unsupported generic promise. Constructor centralization retains current mathematical generality and maps.

- [ ] **`mor-hom-expectation-ruling`**. **Needs:** `core-usability-session`.
  **Owner and delta:** resolve the direct conflict between the protected-expectation rule in `AGENTS.md` and `ARC-07`. The protected `tests/constructions/` and `tests/user_simulations/` files currently contain global `Hom(...)` expectations and may not be edited merely to match an implementation; `ARC-07` simultaneously states that `Mor` is the only owned spelling and `Hom` names Sage's private construction and may appear nowhere in the public preamble universe. The long-tail catalogue records these missing `Hom` calls as failures. Per `AGENTS.md`, *if two rules conflict, the conflict is recorded for the owner to rule on*; no implementation choice is authorized until that ruling determines which prescription is corrected.
  **Acceptance:** one owner ruling makes the prescriptions consistent and names the required source delta: either the protected mathematical expectation is explicitly corrected under its sole allowed exception, or `ARC-07` is explicitly revised to require a public owned `Hom` spelling with the Sage-boundary consequences repaired. Apply that ruling across the whole named population, not only the three currently visible calls, then return the resulting source obligation to `triage-long-tail` for terminal verification.

- [ ] **`minimal-api-freeze`**. **Needs:** `bloat-audit-loop`, `constructor-discovery`, `mor-hom-expectation-ruling`.
  **Owner and delta:** publish an auditable minimal generating API and category graph in the existing architecture specification and generated reference. For every public construction and operation record its mathematical owner, defining data, hypotheses, domain/codomain, induced maps and computational cases. Distinguish primitive construction contracts from methods derived through them; minimality concerns independent authorities, not removal of useful capabilities.
  **Acceptance:** the graph expresses inheritance and structural forgetful maps; every operation is at the highest mathematically valid owner under `CAT-05`; constructors have one discoverable authority; derived conveniences compose that authority. Resolve duplicate meanings, incomparable-owner collisions and hidden representation requirements. Reuse M1 placement evidence on unchanged routes and inspect subsequent changes instead of restarting an unrelated sweep.
  The freeze captures the complete existing public surface and its minimal generating contracts, including supported and explicitly unsupported computational regimes. It supplies the denominator for the method audit in M3. Adding an algorithm case preserves these contracts. A substantial architectural revision explicitly revises the freeze and reopens only the affected acceptance and proof. The daily core remains usable throughout.

## M3 — Compact mathematical test suite

Consolidate the suite around the frozen API, retaining distinct mathematical obligations. The historical runtime catalogue is evidence to refresh here, not a current count of defects.

- [ ] **`suite-compactification`**. **Needs:** `minimal-api-freeze`.
  **Owner and delta:** audit the whole existing suite against the frozen mathematical contracts and the test guidelines. Consolidate repeated setup and duplicate mathematical cases, replace vacuous checks with distinguishing results, use small specimens with the same mathematical force, and organize exercises by object/category and composed workflow. Preserve each distinct mathematical obligation and its generality when consolidating files or parameter families.
  Protected expectation files retain their mathematical correction rule: consolidation preserves the statements and hypotheses; a changed expectation needs a mathematical justification, never agreement with the implementation. Unresolved specification conflicts are settled at their owner before editing those statements.
  **Acceptance:** every existing obligation has a retained exercise or a source-backed disposition in the delivery commit. Separate exercises of the frozen API from specifications of genuinely new M4 capabilities by their mathematical contracts, before execution. Retain the latter with their required feature nodes and expose their collection separately; a failure of an existing frozen contract cannot be moved there. The default frozen-API suite collects every retained test of that API. Real product failures remain required repairs; no skip, expected failure, changed oracle or reduced parameter domain obtains a green result. Coverage follows meaningful assertions about results and maps, not incidental execution, introspection or counts of inhabited categories.

- [ ] **`category-method-coverage-sweep`**. **Needs:** `suite-compactification`. Write and audit the exercises against the frozen API and category graph, retaining valid daily-core and existing mathematical specimens.
  **Owner and delta:** for every category in the live session, construct its objects on small specimens and call every public method of the object, its elements and its morphisms, asserting the mathematical value (owner, 2026-09-24). The categories and operations come from a regenerated `just preamble-megadoc` survey; one test file per category, written to `tests/constructions/CONTRIBUTING.md`'s session standard.
  Loop body: one category, its whole public surface in one pass: every operation of its objects, elements and morphisms, from the survey's listing of what the category introduces, written into that category's one file and banked in one commit.
  A file or commit per method or per surface is not the unit; the category is.
  **Closure:** every category of the survey has its file, and `just coverage-report` shows no public method of the preamble that no passing test calls, other than those whose failure is a recorded node.
  **Measurement:** reconcile the frozen public object, element and morphism methods with actual mathematical assertions. Count each semantic method contract once at its declaring owner; inherited copies, aliases, private helpers and generated accessors do not inflate the denominator or numerator. Account separately for distinct coefficient, representation and hypothesis regimes. A method is meaningfully covered only when a passing exercise establishes an independently justified result or map property; mere execution or an unsupported-case assertion is insufficient. Publish numerator, denominator, uncovered methods and the inspected regimes with the existing coverage report. The acceptance threshold is strictly greater than 90 percent meaningful method coverage, with all core contracts covered; retain the stronger survey obligation to exercise every available public method and disposition every gap. Line/branch coverage is supplementary evidence.

- [ ] **`triage-long-tail`**. **Needs:** `minimal-api-freeze`.
  **Catalogue origin:** the suite run recorded on 2026-09-23 used `--no-time-gates --timeout=1 -o timeout_func_only=true` to locate failure sites. Refresh that diagnostic catalogue once after grouping and repairing shared causes; acceptance runs retain the default time gates. Inspect the owning cause, not only the historical line number.
  **Site:** the remaining 699 sites of the catalogue, together about 2,200 failures, among them `categories/rings/commutative_ideals.py:946` (59), `categories/group/g_sets.py:167` (54), `categories/modules/pure/modules.py:4681` (53), `categories/modules/framed/fraction_field_quotients.py:123` (50), `sage/matrix/matrix_gfpn_dense.pyx:429` (`GF(27)` in MeatAxe, 36), and 27 specification tests calling `Hom`, which the session does not export under `Mor` as its only spelling.
  Also: deciding whether an endomorphism of a free module lies in the image of the zero module's Mor (`module_morphisms.py:1139`, "cannot decide whether ... is in the image"), reached by the centre of a unital associative algebra (`tests/algebras/test_algebra_preservation.sage`). **Closure:** a re-run of the catalogue with no failure at these sites; split any site whose cause is shared by others into its own node first.
  **Source narrowing (2026-09-26):** several named clusters predate later owner repairs. Ideal construction no longer has the `syzygy_rows is None` fallback/assertion: exact syzygy routes now cover the represented number-field-order, quotient-ring and polynomial cases. `FractionFieldQuotients(R)` now has a general `Frac(R)/aR` realization, retaining `QmodnZ` only for `ZZ`. Module-subobject inclusions now certify their selected lifts as exact construction data, so `None` means genuine nonmembership rather than the former undecidable-image error. These repairs all postdate the catalogue commit `3aede5875`.
  The former module-presentation-width failure was the comparison `labels.cardinality() != width`; commit `280023972` postdates the catalogue and compares with `cardinal(width)` instead, which the current constructor retains. The finite-G-set preservation site remained live because its private permutation application returned an engine point; it now lowers the owned input point and raises the permutation image before the action re-enters the represented point set. The protected expectation subtrees still contain three global `Hom(...)` calls, but `ARC-07` reserves `Hom` for Sage and requires owned `A.Mor(B)`; neither adding a public `Hom` alias nor rewriting those protected expectations is permitted without resolving that specification conflict at its governing owner.
  **Execution scope:** refresh the historical catalogue on the frozen API. Group failures by cause, preserve independently justified mathematical expectations, and repair the required cases. Old site counts are leads, not the acceptance population. All unresolved required failures feed terminal acceptance.

- [ ] **`suite-within-time-gates`**. **Needs:** `suite-compactification`.
  **Owner and delta:** the suite passes its gates in `dzack_research.utilities.suite_budget`: star import 2 s after `sage.all`, collection 30 s, execution 100 ms per selected test, no test over its per-test limit.
  **Observed:** the catalogue executed in about 6.5 minutes, 24 ms per test; with tracebacks on, formatting failure reports dominates because owned `_repr_` methods compute (a ring's repr computes its cardinality).
  16 tests exceeded 1 s. Measured 2026-09-25: each process that reaches the Julia bridge pays about 20 s to start Julia and load Oscar (compile cache warm), and `test_centralizer_discriminant_image_of_the_swap_on_a1_plus_a1` spends 72 s in one call; the tests on large lattices are `small-specimen-tests`. pytest-timeout's `SIGALRM` inside Cython code is caught by cysignals as `AlarmInterrupt`, which stops the run.
  **Observed after the rack reconciliation (2026-09-25, single process, --timeout=600):** the enumerating lattice specimens slowed.
  Pre-merge `1e1a69be2` against merged `d14a3878f`: `test_equivariant_vector_orbits.sage::test_representatives_are_the_same_live_orbit_package` 113 s → 145 s; `test_centralizer_gluing.sage::test_the_a2_centralizer_splits_the_single_root_orbit_in_two` 79 s → 99 s; `::test_the_a2_centralizer_separates_two_roots_that_o_a2_identifies` 29 s → 58 s; `test_cyclotomic_centralizer.sage::test_the_centralizer_of_minus_one_on_Z3_is_the_signed_permutation_group_of_order_48` 55 s → 58 s. Each builds one isometry per group element through module Mor membership tests; the cyclotomic profile had category `__contains__` at 57 of 120 profiled seconds before `d14a3878f`. **Observed (2026-09-25):** the expectation subtrees collect 13,154 cases, and `tests/constructions/test_categories_inhabited.sage` (3.6 KB) is 8,500 of them, one per session category and witness check.
  A run of the two subtrees on three workers does not finish in 10 minutes.
  **Observed (2026-09-25):** `tests/constructions/test_schemes_construct.sage` does not finish: run alone it passed 42% of its cases in the first minutes, then sat for 40 minutes inside one case despite `--timeout=60`, so the blocking call does not return to Python.
  `test_rings_construct.sage` exceeds 300 s run alone.
  **Observed (2026-09-26):** the smallest `ADELogPairs` witness, type `A_1`, costs 0.7 s per base ring and `P^2` from its fan 0.9 s, nearly all of it in the fan's chart changes.
  **Closure:** the default suite run is green on all four gates, with no gate raised.

- [ ] **`terminal-session`**. **Needs:** `category-method-coverage-sweep`, `triage-long-tail`, `suite-within-time-gates`.

  **Owner and delta:** execute the integrated mathematical proof burden against the frozen API on the final owned session and research notebook. This is full acceptance within the already-active execution phase.
  **Invariants:** a fresh process imports `from dzack_research.preamble.all import *` and exposes Cat and Lattices.
  This is a prerequisite, not mathematical acceptance.
  Regenerate `docs/preamble-megadoc.md` and the graph through `just preamble-megadoc`; inspect their agreement with live categories, operations, domains and codomains.
  Preamble warnings and order-dependent imports require repair.
  **Closure evidence:** execute all required banked construction specimens and the protected expectation/user-simulation obligations through the prescribed project recipes, classify actual failures at their owners and repair them without weakening expectations.
  Cover direct, convenience, functor, catalogue and engine-raised routes; free/nonfree, finite/infinite and changed-base regimes where claimed.
  A previous run certifies only the source it exercised.
  Use japi for notebook execution and inspect actual rendered mathematical outputs; source, saved files and successful imports do not prove rendering or mathematical claims.
  Run the prescribed final QC at its applicable boundary, retaining explicit evidence for any remaining failures.
  A required failure keeps this node open; fixes and focused re-execution stay within T rather than restarting the architecture suspension.
  Respect push authorization.
  **Frozen-suite acceptance:** every retained test of the frozen API passes in its complete default suite, with 100 percent pass rate and strictly greater than 90 percent meaningful public-method coverage as defined by the coverage sweep. No failure of that API is waived to reach the threshold. Audit the residual uncovered contracts, execute its banked obligations on the integrated tree, and retain the existing performance gates. The frozen scope and test population cannot shrink to obtain the result. Preserved specifications of new M4 capabilities belong to their feature acceptance; they neither count as passing frozen-API tests nor disappear from the required programme.

## M4 — Required mathematical expansion

These remain required constructions with their original generality, maps, specimens and unresolved engine decisions. Their roots wait for the accepted frozen API. Split a genuine prerequisite needed earlier into the consuming milestone, retaining the rest here.

- [ ] **`lattice-represents-an-integer`**. **Needs:** `higher-rank-integral-lattice-representation`.
  **Owner and delta:** `Lattices(R)` answers the existential question whether `L` represents `n`, i.e. whether the hypersurface `V(q - n)` has an `R`-point.
  It also answers `representation_vector(n)`, a witness as an element of `L`. The elementwise `represents` on form-module elements (`categories/modules/framed/formed/form_modules.py`, ~line 1260) is a different statement and stays.
  Routing is `case` on categorical membership.
  Definite: short-vector enumeration (PARI `qfminim`), with the theta series when many `n` are asked.
  Indefinite rank 2: binary-form reduction (PARI `qfbsolve`). Indefinite rank >= 4: the real place and `L_p` for `p | 2 n det(L)` (Kneser; strong approximation for the spin group).
  Indefinite rank 3: the local test, then the finitely many spinor-exceptional square classes (Schulze-Pillot; Earnest--Hsia), decided by a witness search.
  `n = 0` is isotropy (Hasse--Minkowski; Meyer for rank >= 5). Every theorem is cited from its source, and every engine call is private.
  **Closure specimens:** `E_8` represents 2 and not 1. `U` represents every integer.
  `A_1(-1) + A_1(-1) + A_1(-1)`, the form `-(x^2 + y^2 + z^2)`, does not represent `-7`, the Legendre obstruction at 2. `U + U` represents 0 with a nonzero witness.

- [ ] **`higher-rank-integral-lattice-representation`**. **Needs:** `higher-rank-representation-engine-ruling`.
  **Owner and delta:** the indefinite integral rank-at-least-three branches of `Lattices(ZZ).representation_vector(n)`. Do not use `QuadraticForm.solve`, which solves over `QQ`, as an integral witness. Rank at least four uses the real place plus the exact local tests at primes dividing `2 n det(L)` and the strong-approximation/Kneser route to construct an integral witness when the local conditions hold. Rank three uses the same local test followed by the finitely many spinor-exceptional square classes (Schulze-Pillot; Earnest--Hsia), with an exact witness construction in the positive cases. `n=0` is integral isotropy and requires a nonzero integral witness. Research maintained Sage/PARI/OSCAR algorithms before implementing; if none exposes the complete witness route, add the private engine adapter rather than substituting rational solvability or an unbounded search.
  **Closure specimens:** `U + U` represents `0` by a nonzero vector; `-(x^2+y^2+z^2)` does not represent `-7`; one indefinite rank-four locally soluble positive example returns an exact integral witness.

- [ ] **`higher-rank-representation-engine-ruling`**. **Needs:** `terminal-session`.
  **Owner decision required by `ENG-06`:** source audit found exact maintained routes for definite integral forms (`PARI qfminim`, already wrapped by `vectors_of_square`) and binary integral forms (`Sage BinaryQF.solve_integer`, delegating to `PARI qfbsolve`). Installed Sage, Hecke and OSCAR expose rational-space representation/isotropy machinery but no complete exact integral rank-at-least-three witness operation; Hecke's `represents` is an isometry-class/subspace statement over the fraction field, not an integral lattice-point solver. No maintained rank-at-least-three integral witness route was found in the current engine population.
  Under `ENG-06`, implementing the Kneser/strong-approximation and ternary spinor-exception algorithms locally materially expands the repository's correctness burden and therefore needs an explicit project/owner decision. The ruling must choose either (a) deliberately own that algorithm here, with cited source-grounded contracts and a private engine boundary, or (b) designate a maintained external exact solver and authorize the adapter. Rational solvability, local solvability alone, or an unbounded witness search are not acceptable substitutes.

- [ ] **`lattice-reflection-groups`**. **Needs:** `higher-signature-reflection-group-search`, `hyperbolic-restricted-norm-reflection-groups`.
  **Owner and delta:** every lattice `L` owns *the* reflection group `W(L) = <s_v : v in L_K, s_v in O(L)>` and `W_S(L) = <s_v in W(L) : v^2 in S>` for `S <= ZZ`, as `L.reflection_group(S)`. Its default `S` is the finite set `{n : n | 2 e(A_L)}` of admissible norms, so the call with no argument is `W(L)`. It is a subgroup of `O(L)`. When `L` is definite (finite root system) or hyperbolic (`W(L) cap O^+(L)`, the reflections in vectors of negative norm), it is also an object of a category of Coxeter groups, carrying the Coxeter system of a chamber: simple roots and Coxeter matrix, of possibly infinite rank.
  The hyperbolic Vinberg route (`categories/hyperbolic_lattices.py`, `reflection_group`) becomes the hyperbolic specialization of this construction.
  A search that did not complete yields a stated subgroup of `W(L)`. The second name `weyl_group` is removed and its callers are moved.
  The theory, still to be checked against its sources, is in `docs/theory/lattice-reflection-groups.md`. **Closure specimens:** `W(E_8)` is the finite Coxeter group of type `E_8` (order 696729600). For an even 2-elementary lattice, `W(L) = W_{-2,-4}(L)`. `U + <-6>` has a reflection in a norm `-6` vector, so `W(L) != W_{-2,-4}(L)`. `II_{1,9}` has Coxeter diagram `E_10`.

- [ ] **`higher-signature-reflection-group-search`**. **Needs:** `higher-signature-reflection-engine-ruling`.
  **Owner and delta:** construct `W(L)` for indefinite integral lattices with both inertia indices at least two. The defining group is generated by all integral reflections, and the admissible primitive root norms are still bounded by divisors of twice the discriminant exponent, but unlike the definite case the set of roots of one admissible norm need not be finite and unlike signature `(1,n)` there is no Vinberg chamber search. Research a maintained exact arithmetic-group/reflection-subgroup algorithm before adding local enumeration. A finite or interrupted search may return only the subgroup generated by the reflections it actually found, with that incompleteness stated in the returned construction; it must not be named `W(L)` without a completeness certificate.

- [ ] **`higher-signature-reflection-engine-ruling`**. **Needs:** `terminal-session`.
  **Owner decision required by `ENG-06`:** Sage/OSCAR/Hecke and current project backends expose orthogonal groups, individual reflections and the hyperbolic Vinberg case, but no exact construction of the subgroup generated by all integral reflections of a lattice with both inertia indices at least two. Magma's documented reflection-group facilities start from a supplied reflection representation/root datum or supplied roots; they do not construct this arithmetic reflection subgroup from an arbitrary integral lattice. Decide whether the project deliberately owns the missing arithmetic search/certification algorithm, or designate and authorize a maintained exact backend that supplies it. A bounded vector search without a completeness theorem is not `W(L)`.

- [ ] **`hyperbolic-restricted-norm-reflection-groups`**. **Needs:** `hyperbolic-restricted-reflection-engine-ruling`.
  **Owner and delta:** construct `W_S(L)` for hyperbolic lattices and a proper selected norm set `S`. Vinberg's simple roots generate the full reflection group `W(L)`, but merely discarding simple roots whose norms are not in `S` need not generate the subgroup generated by *all* reflections with norms in `S`; conjugation by reflections of other norms can produce further `S`-roots. Research the correct chamber/orbit construction or a maintained implementation. The full-group call with the default admissible norm set continues to use the existing Vinberg wall enumeration.

- [ ] **`hyperbolic-restricted-reflection-engine-ruling`**. **Needs:** `terminal-session`.
  **Owner decision required by `ENG-06`:** no maintained exact operation was found that takes a hyperbolic integral lattice and a norm predicate and returns the reflection subgroup generated by every root satisfying it. Coxeter-system packages can form a reflection subgroup from a supplied finite family of roots, but that does not solve the infinite root-family construction here. Decide whether to own the required reflection-subgroup/chamber algorithm or authorize a maintained exact backend that computes this norm-defined subgroup with a completeness certificate.

- [ ] **`group-exact-sequences-and-homology`**. **Needs:** `terminal-session`.
  **Owner and delta:** one owned construction for a short exact sequence of groups `1 -> N -> G -> Q -> 1`: the normal subobject `N -> G`, the quotient `G -> Q`, and exactness.
  `RankOneParabolicLeviExactSequence` (`categories/lattices.py`) and the discriminant reduction sequence are instances of it, not separate classes.
  Exactness only as pointed sets, when the image is not normal, uses the finite image-coset construction in `categories/group/g_sets.py`. The first group-exact instance is the commutator sequence `1 -> [G,G] -> G -> G^ab -> 1`, whose quotient map is the unit of `(-)^ab -| i` (`functors/abelianization.py`). Group homology `H_n(G; M)` and cohomology `H^n(G; M)` for a `ZZ[G]`-module `M`, as derived functors of coinvariants and invariants: through the resolution categories of `categories-of-resolutions`, computed privately by GAP's HAP or Sage.
  With them come the identifications `H_1(G; ZZ) = G^ab` (from `I_G/I_G^2 = G^ab` for the augmentation ideal `I_G`), `H^1(G; ZZ) = Hom(G, ZZ) = Hom(G^ab, ZZ)`, which sees only the free part, and `H^2(G; ZZ) = Hom(G, QQ/ZZ)` for finite `G`, the Pontryagin dual of `G^ab` (Brown, *Cohomology of Groups*, II.3 and III.1; cite from the source).
  Computation routes: finite `G` through GAP. Finitely presented `G` computes `G^ab` from its chosen presentation, by the Smith normal form of the abelianized relation matrix, including for infinite `G`. A Coxeter group `W` has `W^ab = (ZZ/2)^c`, with `c` the number of classes of Coxeter generators joined by paths of odd labels (read from the Coxeter matrix; `lattice-reflection-groups`). `O(L)`, for `L` containing enough hyperbolic planes, has its abelianization detected by the determinant, the spinor norms and the discriminant reduction (the classical theory of the stable orthogonal group; find and cite the precise theorem and its hypotheses before using it).
  Predicate-defined subgroups of `O(L)` go through the kernel route that `cokernel` already uses.
  **Closure specimens:** `S_3^ab = ZZ/2` with `[S_3, S_3] = A_3`. The free group `F_2` has abelianization `ZZ^2`, computed from its presentation.
  `SL_2(ZZ)^ab = ZZ/12`. `H_1(ZZ/n; ZZ) = ZZ/n`, `H^1(ZZ/n; ZZ) = 0`, `H^2(ZZ/n; ZZ) = ZZ/n`. `W(E_8)^ab = ZZ/2`.

- [ ] **`pullbacks-in-every-category`**. **Needs:** `terminal-session`.
  **Owner and delta:** the fibre product `A x_C B` of a cospan is constructed once, at the general owner (`Cat.fiber_product` in `abstract_categories/cat.py`, from `product` and `equalizer`), and it is reachable in sets, groups, modules, algebras, schemes and every category with products and equalizers.
  The result is the limit cone: the apex, both projections and the universal map, never a bare object.
  Leaf categories only place structure and properties on the apex so that it lives in the correct category: a subgroup of `A x B`, a submodule, a subalgebra.
  Schemes are the case where the fibre product is not the fibre product of underlying sets.
  Where a leaf has a better construction, it supplies one that realizes the same universal property.
  Leads: `docs/theory/glue-stabilizers.md`, *Pullbacks*. **Closure specimens:** the pullback of `ZZ -> ZZ/2 <- ZZ` in groups is the index-2 subgroup of `ZZ^2` with its two projections.
  The fibre product of two points over a point is a point in both sets and schemes.
  `Spec QQ(i) x_{Spec QQ} Spec QQ(i)` has two points.

- [ ] **`images-of-subgroups-and-predicate-subsets`**. **Needs:** `terminal-session`.
  **Owner and delta:** research, then construction.
  The image of a subgroup with generators under a group morphism is the subgroup generated by the images, as an owned subobject of the codomain.
  The image of a subset given only by a predicate is an existential projection, `{f(x) : P(x)}`, and is not computable in general.
  Survey what is known before choosing a representation: SymPy `ImageSet` and `ConditionSet`, quantifier elimination (Tarski–Seidenberg; Presburger), Chevalley's theorem for constructible images with elimination, and the finite-index Schreier route that turns a predicate subgroup into one with generators.
  Record the decidability boundary and which route each represented case uses.
  Leads: `docs/theory/glue-stabilizers.md`. **Closure specimens:** the image of `O(A_2)` under `rho` is computed from generators.
  The image of a predicate subgroup of finite index in `O(L)` is computed through its Schreier generators.
  A predicate subset with no route reaches an assertion that names the missing algorithm.

- [ ] **`finite-index-subgroup-generators`**. **Needs:** `terminal-session`.
  **Owner and delta:** a subgroup `H <= G` given by a membership test, known to have finite index (for example a preimage of a subgroup of a finite quotient), with `G` given by generators, answers generators of `H` by Schreier's lemma.
  It uses the action of `G` on the coset space and a transversal from `finite_image_lifts`. When `G` has a chosen presentation, it answers a presentation of `H` by Reidemeister–Schreier.
  This becomes a `case` of the group-level generator routing.
  Leads: `docs/theory/glue-stabilizers.md`, *Generators of finite-index subgroups*. **Closure specimens:** the kernel of `SL_2(ZZ) -> SL_2(ZZ/2)` has index 6, and its generators generate a subgroup of index 6. `\tilde O(L)` for an indefinite `L` with a generating set of `O(L)` answers generators, and each lies in the kernel of `rho`.

- [ ] **`lattice-glue-stabilizers`**. **Needs:** `pullbacks-in-every-category`, `finite-index-subgroup-generators`, `images-of-subgroups-and-predicate-subsets`. **Owner and delta:** for a primitive extension `S + T -> L` with glue `gamma: H_S -> H_T` (`Lattices.glue_map`), the preamble constructs:

  - the restriction morphisms `Stab_{O(L)}(S) -> O(S)` and `-> O(T)`, and `rho-bar_S: O(S)_{H_S} -> O(H_S)`;

  - `Stab_{O(L)}(S)` as the owned pullback `O(S)_{H_S} x_{O(H)} O(T)_{H_T}`, with its projections and the gluing map back into `O(L)`;

  - `Gamma_{h,T} = rho-bar_T^{-1}(gamma rho-bar_S(O(S,h)) gamma^{-1})` as a subgroup of `O(T)` with its inclusion.
    With generators of `O(S,h)` and `O(T)` (and relations, if any), it answers generators (and a presentation) of `Gamma_{h,T}`. The theory and its leads (Peters–Sterk 15.1; Nikulin 1979) are in `docs/theory/glue-stabilizers.md`. **Closure specimens:** for `L = U + U` with `S = U` and `T = U`, the stabilizer of `S` is `O(U) x O(U)`. For `L` unimodular, `Gamma_{h,T} = rho_T^{-1}(gamma rho_S(O(S,h)) gamma^{-1})`. For a rank-one `S = <h>` with `h^2 = 2` in `II_{1,9}`, the pullback description reconstructs the stabilizer of `h`.

- [ ] **`coxeter-group-structure`**. **Needs:** `lattice-reflection-groups`. **Owner and delta:** the category of Coxeter systems `(W, S)` owns:

  - word length and reduced words;

  - simple systems, positive roots and the fundamental chamber;

  - for finite `W`, the longest element `w_0` and the degrees `d_i`;

  - the ring of invariants `k[V]^W`, with its Molien series, toward GIT quotients `V // W`;

  - the Poincaré series `W(t)` as a rational function in general (Steinberg's formula from the finite parabolic subgroups; the product formula and Solomon's identity for finite `W`; Bott's formula for affine `W`);

  - `chi(W) = 1/W(1)`;

  - the growth rate of infinite `W`, as a Perron or Salem number.
    These two classes of real algebraic integers are owned if not already present.
    Crystallographic groups are constructed as stabilizers `GL(V)_L` of lattices `L <= V`. The existing chamber code (`categories/chamber_complexes.py`) and the Vinberg route thread into this owner.
    Theory and leads: `docs/theory/coxeter-groups-complexes-and-cell-structures.md`. **Closure specimens:** `W(E_8)` has degrees 2, 8, 12, 14, 18, 20, 24, 30 and `W(1) = 696729600`. `W(A_2)(t) = 1 + 2t + 2t^2 + t^3`. The affine `A_1` group has `W(t) = (1 + t)/(1 - t)`. The `(2,3,7)` triangle group has a Salem growth rate (Lehmer's number; check it against the source).

- [ ] **`simplicial-and-cw-foundations`**. **Needs:** `pullbacks-in-every-category`. **Owner and delta:**

  - Owned categories of simplicial complexes, Δ-complexes and simplicial sets, each with its face poset.
    The nerve of a poset (the order complex), and the nerve of the category of simplices of a simplicial set (the barycentric subdivision).

  - CW complexes built by attaching cells along maps `S^{n-1} -> X^{n-1}`, whose homotopy classes lie in the known range of the homotopy groups of spheres.
    Beyond that range, cells attach along explicitly given continuous or simplicial maps.

  - Predicates for regular, simplicial and Δ-complex structures.

  - Regularization, by induction up the skeleta, replacing each attaching map that is not an embedding with its mapping cylinder.

  - Deciding homotopy of maps and weak equivalence through simplicial approximation and effective homology (Kenzo, which Sage interfaces), assertion-gated where no algorithm applies.
    Sage's `SimplicialComplex`, `DeltaComplex` and `SimplicialSet` are private engines.
    Theory and leads: `docs/theory/coxeter-groups-complexes-and-cell-structures.md`. **Closure specimens:** the boundary of the 3-simplex realizes `S^2`, and the Δ-complex with one vertex and one edge realizes `S^1`. The CW structure on `RP^2` with one cell in each dimension is not regular, and its regularization is.
    The order complex of the face poset of a simplicial complex is its barycentric subdivision.

- [ ] **`coxeter-complexes-and-buildings`**. **Needs:** `coxeter-group-structure`, `simplicial-and-cw-foundations`. **Owner and delta:**

  - The poset of parabolic subgroups `W_J`.

  - The Coxeter complex `Sigma(W, S)`, as an honest simplicial complex whose face poset is the poset of cosets `wW_J` (`J` proper), with its chamber set `W` as a `W`-set.

  - The Tits cone.

  - Buildings as chamber complexes with apartment systems of Coxeter complexes, including those from BN-pairs.

  - The Tits complex: the spherical building of a BN-pair (owner, 2026-09-26).

  - The Iwahori–Hecke algebra `H(W, S)` over `ZZ[q^{±1/2}]`, with its standard basis `T_w`, the quadratic relations `(T_s − q)(T_s + 1) = 0` and the braid relations; its Kazhdan–Lusztig basis and polynomials; its specialization at `q = 1` to `ZZ[W]`; and, for a BN-pair over `F_q`, the isomorphism with the convolution algebra of `B`-bi-invariant functions on `G`, the endomorphism algebra of the permutation module on the chambers of the building.

  - The Davis complex of `W 𝒮^f`. Each is a construction on its owner, with the maps that relate them: chambers to group elements, apartments into buildings, and the Coxeter complex into the Tits cone.
    Theory and leads: `docs/theory/coxeter-groups-complexes-and-cell-structures.md`. **Closure specimens:** `Sigma(A_2)` is a hexagon, a triangulated `S^1` with 6 chambers.
    `Sigma` of the affine `A_1` group is a triangulated line.
    The Davis complex of the infinite dihedral group is a line.
    The building of `SL_3(F_2)` has 21 chambers and apartments that are hexagons.

- [ ] **`modular-forms-and-hecke-algebras`**. **Needs:** `finite-index-subgroup-generators`. **Owner and delta:**

  - Congruence subgroups of `SL_n(ZZ)` (`Γ(N)`, and `Γ_0(N)` and `Γ_1(N)` for `n = 2`) as subobjects with their inclusions and generators.

  - The modular curves `Y_0(N)`, `X_0(N)`, `Y_1(N)`, `X_1(N)` and `X(N)`, with cusps, genus, and their moduli interpretation.

  - Modular and cusp forms `M_k(Γ)` and `S_k(Γ)`, with Fourier (q-)expansions, inside the general setting of automorphic forms.

  - The Hecke operators `T_n` and the Hecke algebra they generate, with its eigenforms.

  - L-functions `L(s) = Σ a_n n^{-s}` with their Euler factorizations.
    Point counts of varieties over `ZZ` enter them: for an elliptic curve, `a_p = p + 1 − #E(F_p)`.

  - The modularity correspondences: an elliptic curve `E/QQ` of conductor `N` with a newform in `S_2(Γ_0(N))`, a parametrization `X_0(N) → E`, and `E` as an isogeny factor of `J_0(N)`; and abelian varieties `A_f` by Eichler–Shimura.

  - Isogenies and isogeny classes.

  - Torsion points `E[n] = (1/n)Λ/Λ` of complex tori `ℂ^g/Λ`, found as the lattice points of `(1/n)Λ` in a fundamental domain.
    Sage, PARI and LMFDB are private engines and specimen sources.
    Theory and leads: `docs/theory/modular-forms-and-hecke-operators.md`. **Closure specimens:** `[SL_2(ZZ) : Γ_0(11)] = 12`, and `X_0(11)` has genus 1. `S_2(Γ_0(11))` is spanned by `q ∏ (1 − q^n)^2 (1 − q^{11n})^2`, whose `a_p` agree with `p + 1 − #E(F_p)` for `E = 11a1` at good primes.
    `T_2` acts on that form by `a_2 = −2`. `E[2]` of `ℂ/(ZZ + ZZi)` has 4 points.

- [ ] **`satake-diagrams-present-real-forms`**. **Needs:** `terminal-session`.
  **Owner and delta:** `SatakeDiagrams` (`categories/satake_diagrams.py`) gains the functor to real forms: an admissible Satake diagram `(D, X, tau)` of a complex semisimple Lie algebra `g` presents a real form `g_0` of `g` up to isomorphism (Araki 1962; Kolb, *Quantum symmetric Kac-Moody pairs*, 2014, section 2.4).
  The codomain is the category of real forms of `g`, a real Lie algebra with an isomorphism of its complexification to `g`; `lean-categories` formalizes neither Satake diagrams nor real forms, so the request there runs beside this node.
  **Closure specimens:** each lattice-db Satake card maps to the real form its card names, with the identification cited from Araki's table (Araki 1962, pp. 32-33), beginning with `a2-su21-satake`: `A_2`, no black node, `tau` the swap. The functor is defined only on admissible diagrams, so `A_3` with black nodes `{1}` and `tau = id` (Kolb 2014, Example 2.4) has no image.

- [ ] **`complex-realization-is-a-functor`**. **Needs:** `terminal-session`.
  **Owner and delta:** for a field `k` of characteristic 0 and an embedding `sigma: k -> CC`, complex realization `X -> X(CC)_sigma` is a functor from schemes of finite type over `k` to `TopologicalSpaces`, and analytification is a functor to complex analytic spaces, defined on every scheme of finite type. Today `Schemes(k).FiniteType.complex_realization` (`categories/schemes/schemes.py`) acts on objects only, and `AffineSpaces(k).analytification` (`schemes.py`, `analytic_families.py`) is the only analytification, defined on affine spaces and polynomial maps. The realization computes `H^k(X(CC); ZZ)` only for projective space, smooth complete toric varieties and smooth projective complete intersections, and `_etale_comparison_embedding` constructs `sigma` only for `k = QQ`. Required: the action on morphisms, with `H^k(f(CC); ZZ)` the induced map; analytification of every finite-type scheme; the embeddings `sigma` of a number field, chosen by the caller; and a realization route for the branched double covers of the Horikawa families (`tests/schemes/test_horikawa_k3_family.sage`, `test_horikawa_enriques_family.sage`), whose topology is not toric and not a complete intersection.
  **Closure specimens:** the degree-2 map `P^1 -> P^1`, `[x:y] -> [x^2:y^2]`, induces multiplication by 2 on `H^2(P^1(CC); ZZ)`; the Horikawa K3 double cover has `chi = 24` and `b_2 = 22`; `QQ(i)` has two embeddings into `CC`, and both give the same Betti numbers of `P^2`.

- [ ] **`complete-intersection-hodge-sources`**. **Needs:** none.
  **Owner and delta:** the Zotero library holds an openable extraction of the source that states the Hodge numbers of a smooth complete intersection of any multidegree: SGA 7 II, Exposé XI (Deligne), or Hirzebruch, *Topological Methods in Algebraic Geometry*, §22. Today the item labelled SGA 7 II (`CMV4MC6A`, LNM 340) holds an extraction of SGA 7 I; the item labelled SGA 4, volume 305 (`ZXUPYTKS`) holds tome 1, Exposés I to IV; the SGA 4½ item (`HRUVM374`) holds only a table of contents; Hirzebruch's book is absent. Dimca, *Singularities and Topology of Hypersurfaces* [Dim92], (B34) covers quasismooth weighted hypersurfaces only.
  **Closure:** the generating function of the Hodge numbers of a smooth complete intersection, with its hypotheses, is read from an opened page, with the citation key verified against `references.bib`.

- [ ] **`complete-intersection-hodge-structure`**. **Needs:** `complete-intersection-hodge-sources`, `terminal-session`.
  **Owner and delta:** `ProjectiveCompleteIntersections(k).Smooth()` answers `hodge_structure()` and `hodge_number(p, q)` for every multidegree, from the generating function in `complete-intersection-hodge-sources`. Today `hodge_structure()` (`categories/schemes/complete_intersections.py`) builds `_QuarticK3HodgeData` only, and `Schemes(k).Proper().Smooth().hodge_number` routes complete intersections to it. The cohomology outside the middle degree is that of projective space (Lefschetz hyperplane theorem); only the middle degree depends on the multidegree.
  **Closure specimens:** the quartic surface in `P^3` answers the values `_QuarticK3HodgeData` holds today; the cubic surface in `P^3`, the quintic threefold in `P^4` and the intersection of two quadrics in `P^5` answer the Hodge numbers transcribed from the opened source, with its locator.

- [ ] **`geometric-cards-store-betti-numbers`**. **Needs:** none.
  **Owner and delta:** every card in `lattice-database/geometric-objects/` stores `betti_numbers` and `euler_characteristic`, each transcribed from a cited source or computed by the preamble for the constructed object, under the lattice-database rule that no computed invariant is discarded. Today 36 of the 37 cards store no Betti numbers; `k3-surface.md` stores them. `kummer-2.md` and `k3-hilbert-2.md` link an `H^2` lattice and store a Hodge series, which determines `b_k = sum_{p+q=k} h^{p,q}` for a compact Kähler manifold; the symmetric spaces and the Euclidean and hyperbolic spaces store neither.
  **Closure:** each card states `b_k` and `chi` with a citation or a preamble route.

- [ ] **`extended-mathematics-session`**. **Needs:** `lattice-represents-an-integer`, `lattice-glue-stabilizers`, `group-exact-sequences-and-homology`, `coxeter-complexes-and-buildings`, `modular-forms-and-hecke-algebras`, `complex-realization-is-a-functor`, `complete-intersection-hodge-structure`, `geometric-cards-store-betti-numbers`, `satake-diagrams-present-real-forms`.
  **Owner and delta:** exercise every required M4 construction and its maps together with the frozen core, through the public session and applicable research notebook. Extend the API reference and meaningful-method denominator with the new contracts. Run the distinguishing specimens retained in each feature node, including its full hypotheses and computational regimes.
  **Acceptance:** required feature specimens and the retained suite pass, meaningful-method coverage remains above 90 percent, and ordinary workflows preserve their previous capability. Repair shared owners before extending dependent consumers. An unresolved engine-ownership ruling keeps its required construction and this node open; it does not reopen the earlier usable-core milestone.

## M5 — Optional research extensions

These consumers follow required acceptance and never block it. Each extension retains the frozen contracts or explicitly revises and re-proves the affected architectural boundary.

- [ ] **`optional-framed-manifolds`**. **Needs:** `extended-mathematics-session`, `optional-manifold-tangent-bundles`. **Goal:** the framed manifolds of `CAT-29`: a smooth manifold with a length-0 resolution of its tangent bundle by trivial bundles, i.e. a trivialization of `TX` (nLab *framed manifold*; the `G = {e}` G-structure), with stable framings as trivializations of `TX + R^k` and `n`-framings as trivializations of `TX + R^(n - dim X)`. Specimens: `S^1` and a Lie group framed by left-invariant vector fields; `S^2` not framable and stably framable.

- [ ] **`optional-brauer-manin-obstructions`**. **Needs:** `extended-mathematics-session`. **Goal:** the Brauer--Manin pairing `X(A_k) x Br(X) -> Q/Z` and the obstruction sets for rational and integral points of varieties over a number field `k`, with the cases where the obstruction is computable or is the only one.
  Tori and their torsors (Sansuc).
  Homogeneous spaces of connected linear groups with connected or abelian stabilizers (Borovoi).
  Integral points on spin-group homogeneous spaces, including the rank-3 spinor exceptions of `lattice-represents-an-integer` (Colliot-Thelene--Xu; Borovoi--Demarche).
  Supersolvable finite stabilizers (Harpaz--Wittenberg).
  Abelian varieties, where the obstruction agrees with Sha (Manin).
  Cite each theorem from its source.
  **Construction rule:** nothing here is implemented ad hoc.
  Every notion used to state or compute these results is an owned construction in the preamble, and this node is exploded into its prerequisite DAG before any leaf is built (`DEV-56`, *A missing foundation parks the work that found it*). The expected prerequisites, to be confirmed by that trace: `G_K`-modules and Galois representations; étale cohomology specializing to Galois and group cohomology; categories of algebraic groups and their theory, with connectedness, commutativity, reductivity and simple connectedness decided or theorem-backed; tori with their character and cocharacter lattices as Galois lattices; torsors and principal `G`-bundles; homogeneous spaces and stabilizers in general; Tate--Shafarevich groups; symmetric spaces and basic Shimura-variety machinery; abelian varieties with elliptic curves as a specialization, their cohomology with its structures, torsion subgroups and Tate modules; the Brauer group of a scheme.
  **Specimens:** the Iskovskikh conic bundle, or the Cassels--Guy cubic, failing the Hasse principle through a Brauer class; an integral spinor-exceptional example taken from Colliot-Thelene--Xu, which has local points everywhere and fails only through the integral Brauer--Manin obstruction.

- [ ] **`optional-manifold-tangent-bundles`**. **Needs:** `extended-mathematics-session`. **Goal:** the tangent bundle of an object of `SmoothManifolds` (`categories/manifolds.py`) as an owned vector bundle, with its module of sections `Der(C^oo(M))`, realized through SageManifolds' tangent bundle privately.
  Specimen: `TS^1` trivial of rank 1.

- [ ] **`optional-random-lattices-of-given-invariants`**. **Needs:** `extended-mathematics-session`. **Goal:** random lattices in `Lattices(ZZ)` with a prescribed signature, determinant or rank, built as a random `SL(n, ZZ)` congruence `A^T G A` of a diagonal Gram matrix with Sage's randomness scoped by `seed()`, returning owned lattices, not matrices; and a random isotropic subgroup of a discriminant module (`categories/modules/framed/formed/discriminant_modules.py`, next to `isotropic_subgroups`), feeding `overlattice`. Prior art and its tests: `archives/random-lattice-constructors/`. State the limit: congruence of a diagonal form reaches only odd unimodular lattices, so a random lattice within a genus needs a different construction.

- [ ] **`optional-moduli-of-stable-curves`**. **Needs:** `extended-mathematics-session`. **Goal:** the moduli of stable pointed curves over the owned scheme categories.
  The category of stable graphs of type `(g, n)` with contractions and automorphisms, the stratification of `Mbar_{g,n}` by dual graphs, and charts for `M_{0,n}`, `Mbar_{0,n}`, `M_{1,n}`, `M_{2,n}`. The cited values (Harris-Morrison, Arbarello-Cornalba, Chan) become rows of `tests/test_known_mathematics.sage` with their citations.
  Prior art: `archives/dm-moduli-spike/`.

- [ ] **`optional-sage-categories-property-layer`**. **Needs:** `extended-mathematics-session`. **Goal:** rebuild the preamble's category machinery on the kernel and `Cat` core of `sage-categories` (github.com/dzackgarza/sage-categories), starting with its property layer.
  Use the [constructor integration boundary](docs/constructor-architecture.md) and inspect the chosen core revision's live public contracts before rewriting leaves. The earlier snapshot below is historical context. The rack inspection at `5867543f` includes `03f6a1fd`'s constructor-owner repair through nested property narrowings, selected-functor initialization and identity-functor implementation registration; consume those mechanisms rather than recreating them in research. Select a published full SHA under the core repository's consumer policy before changing the dependency. Retain generic binding, initialization, collision handling and shared constructor discovery in the core, with downstream mathematical specimens exercising the preserved data and maps.
  The core abstracts the Python and Sage class machinery so that leaves are mathematics and backend CAS wiring; mathematics it lacks (resolutions, chain complexes, lattices, forms, number fields) is leaves to write on it.
  State of its code at `21041b20` (2026-09-25):

  - leaves are isolated from the kernel: none of its 54 leaf files under `algebra/`, `geometry/`, `sets/`, `order/` (13,512 lines) imports `kernel` or `cat_kernel`, and one refers to Sage's category machinery; they import `cat` (221 imports, of which 28 name private helpers, mostly `_firewall`);

  - leaf code states constructions by their universal properties: `algebra/free_modules.py` builds the biproduct of modules from the limit and colimit of a discrete diagram in abelian groups and the module action as the lift of a cone;

  - axioms require a membership predicate, intersections are pullbacks (`cat/properties.py`, `cat_kernel/axioms.py`), hom objects are owned categories, and a public name defined by two incomparable owners raises `SemanticCollisionError` (`kernel/compiler.py`), so the preamble's failures from Sage joins, meets, `Sets()` hom categories and shadowed methods do not arise;

  - coercion is explicit: elements of two different objects never combine (`_combine` in `cat/structured_objects.py` asserts one owner), and no map is applied implicitly.
    This is a design choice, not a gap: combining elements of different objects needs a morphism, which is data except where it is unique (`ZZ -> R`, `ZZ` being initial), and writing `QQ(1) + QQ(1/2)` states it.
    Scalar actions (`2 * x` for an element of an abelian group or module) are structure, not coercion.
    The delta is the failure: it says only that the points belong to different objects, where it should name the morphisms available between them.
    The replaced preamble machinery is `owned_category.py`, `owned_category_bases.py`, `refine.py` and `categories/abstract_categories/` (about 12,800 of 156,500 lines); every mathematical category is re-declared through `structure_functors`, `ObjectType` and `Axiom`. **First specimen:** `ZZ` and `QQ` as objects of `Modules(ZZ)`, `QQ` refused by `Modules(ZZ).FinitelyGenerated()`, `QQ(1) + QQ(1/2) == QQ(3/2)`, and `ZZ(1) + QQ(1/2)` refused with an error naming the ring morphism `ZZ -> QQ`.

- [ ] **`optional-database`**. **Needs:** `extended-mathematics-session`. Add a database/classification example when it supplies data needed by research: LMFDB, curve/field databases, OEIS, GRDB, Kreuzer--Skarke or Fanography.
  **Goal:** Add a research database adapter only for a concrete mathematical query whose data materially benefits a live research workflow.
  Select a concrete mathematical query before provisioning an adapter.

- [ ] **`optional-engine`**. **Needs:** `extended-mathematics-session`. Extend private engine integrations when a named construction benefits: Sage/Singular for local and polynomial algebra, libGAP for group actions, persistent `sage-julia-bridge` for OSCAR/Hecke, optional Macaulay2 for its exact algebra strengths, and `sage-indefinite-port` for the indefinite and Lorentzian lattice algorithms.
  **Goal:** Extend private CAS/engine integrations only for a named mathematical construction that benefits from that engine, returning owned objects and maps at the public boundary.
  Maxima stays within its symbolic-calculus domain.
  **Decision:** search existing interfaces first; provision only the needed dependency; put reusable codecs and bridge defects at their actual owner.
  Mathematical outputs always return as owned objects and maps.
  An integration required by an item above is part of that required item, not this optional list.
  Only additional research capabilities with no required consumer belong here; moving a dependency here does not unblock or complete its consumer.
