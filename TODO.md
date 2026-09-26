# Preamble TODO

## Execution priorities

Build the remaining general scheme-theory toolkit from the current `src/dzack_research/preamble/` tree.
Complete shared mathematical dependencies before extending their consumers.
Geometry has priority over independent arithmetic applications; an arithmetic computation moves earlier only when a named geometric construction needs its result.

Among ready nodes, take the groups below in this order (owner, 2026-09-25): wrong answers; the foundations that block many consumers; the test-suite nodes; the remaining runtime triage catalogue; then the forms, categorical-authority and public-interaction nodes that feed `architecture-remediation`. Geometry-before-arithmetic breaks ties within a group.
Priority orders ready nodes; it is never an edge.

This is an executable work list, not a record of past work.
Remove an item when its stated work is delivered; retain only its unfinished obligations if delivery is partial.
Completion evidence belongs in the implementation commit and its mathematical specimens.
Do not append completed rows, release histories, audit transcripts, or an overall-progress table.

The requirements below specify new deltas from existing constructions.
A source path identifies where to extend or repair, not an instruction to recreate that subsystem.
Inspect the live constructor and its consumers before editing.
Uncertainty explicitly assigned to a source review is not a claim of a runtime failure.
The pending terminal verification applies to the entire implementation, including constructions no longer listed as implementation work.

Follow [CONTRIBUTING.md](CONTRIBUTING.md), especially `DEV-50` through `DEV-68`. Begin new additions with its [mathematical dependency trace](CONTRIBUTING.md#mathematical-dependency-tracing), before selecting an implementation.
Record observed missing foundations and papercuts in [COMPLAINTS.md](COMPLAINTS.md), including independent discoveries.
That file owns the observed need and evidence; this queue owns the selected remaining repair and its acceptance.
Link them instead of copying status.
The [design philosophy](CONTRIBUTING.md#preamble-design-philosophy) and [architecture specification](CONTRIBUTING.md#preamble-architecture-specification) govern how every item is implemented, including already-existing dependencies.
The intended result is one recursively owned mathematical language composed from shared constructions and maintained computations, not a larger local CAS. Read the generated `docs/preamble-megadoc.md` before preamble implementation under the governing `AGENTS.md` prerequisites.
This queue does not authorize running preamble tests, QC, Sage, or notebooks before terminal T.

### Select from the live dependency graph

The queue is the scheduling surface.
Completed prerequisite rows and their edge references are removed together, so the ready frontier is precisely the rows with `Needs: none`. Recompute the ready frontier from the current rows before selecting work; do not preserve dated frontier counts or a private list of what was ready in an earlier turn:

```sh
rg -n '^- \[ \] \*\*`[a-z0-9-]+`\*\*\. \*\*Needs:\*\* none\.$' TODO.md
```

Take the ready frontier in dependency order and carry each selected node through delivery before moving on.
A node that closes unblocks its dependents; a node that merely grows does not.
This repository has one worker, so selection has no claim or reservation layer.

### Contents

- [Execution decisions](#execution-decisions-for-every-item), [workstreams](#workstreams), and [DAG rules](#remaining-workstreams-as-a-dependency-graph)

- [Delivery and regression boundaries](#delivery-and-regression-boundaries), [bounded closure](#bounded-closure)

- [Wrong answers](#wrong-answers)

- [Foundations blocking many consumers](#foundations-blocking-many-consumers)

- [Test suite: specimens, speed and coverage](#test-suite-specimens-speed-and-coverage)

- [Runtime triage catalogue](#runtime-triage-catalogue)

- [Forms, actions and arithmetic realizations](#forms-actions-and-arithmetic-realizations)

- [Common categorical authority and public boundaries](#common-categorical-authority-and-public-boundaries)

- [Public mathematical interaction](#public-mathematical-interaction)

- [Source convergence and terminal proof](#source-convergence-and-terminal-proof)

- [Post-remediation convergence](#post-remediation-convergence)

- [Optional research consumers](#optional-research-consumers)

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
Geometry precedes independent arithmetic.
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
During subsequent source implementation, `DEV-58` defers Sage, tests, QC, notebook execution and live megadoc generation until T; inspect current source alongside the existing generated reference.
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

Select a node with no remaining prerequisites, subject to the existing geometry priority.
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
Required pre-T implementation nodes must feed `architecture-remediation` and the terminal chain that verifies them.
Once T begins, newly exposed repairs feed the still-open terminal or post-T node that found them, whose acceptance includes re-execution of affected proof.
Do not resurrect closed phase nodes or restart the source-phase execution suspension.
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

## Wrong answers

A wrong answer outranks every failure that raises: a false value is trusted, a raised error is not.
Paths below are relative to `src/dzack_research/preamble/` unless a different root is given.

## Foundations that block many consumers

An operation, arrow or construction placed at the wrong category is inherited wrongly by every category below it, so these precede the test-suite and triage nodes.

- [ ] **`arrows-thread-through-the-mor-category-graph`**. **Needs:** none.
  **Owner and delta:** the arrow types of the owned Mor categories (`owned_category.py`, `categories/abstract_categories/mor_categories.py`). The arrow type of `Mor_D(A, B)` is the `ElementType` of that Mor category, generated from its supercategories the way `ObjectType` already is.
  For a structure `U : D -> C` it inherits the arrow type of `Mor_C(UA, UB)` and adds only what `D` introduces: the form square and value map for `FormModules(R)`, multiplicativity for `Algebras(R)`, equivariance for `G`-objects (`CAT-05`, `CAT-10`, `OWN-14`, `CON-16`). An operation defined on arrows of `C` is written once there and reached from every `D` above it.
  Two defect shapes contradict this: a stored lower arrow with forwarding (`FormedModuleMorphism._module_morphism`), and an operation carried only by a private construction-route subclass (`_TransportedLatticeEmbedding.isotropic_reduction`; `is_open_immersion` on private scheme-morphism subclasses).
  Population and census method: [COMPLAINTS.md](COMPLAINTS.md#arrows-of-a-structured-category-do-not-inherit-the-arrow-operations-of-the-category-below-it).
  Repair the whole population: the chain `Modules(R) -> FormModules(R) -> Lattices(R)` with its embeddings first, then algebras over modules, groups over monoids, fields over rings, holomorphic over continuous maps, and schemes.
  With the arrow types threaded, place each arrow operation by the `CAT-05` test with the `just placement` worksheet, as `placement-audit` does for object and element operations.
  Read the object-side mechanism in `owned_category.py` and `PLAN-threading-set-behaviour` first; the arrow side uses that mechanism and adds no second one.
  **Closure specimens:** for a primitive isotropic `v` in `U + E_8(-1)`, `v.isotropic_reduction()` returns `K_v = v^perp / ZZ v`, even unimodular of signature `(0, 8)`, with its parabolic data.
  A form embedding `L -> L + M` answers `is_primitive()`, `kernel()` and `cokernel()` from the module-arrow owner, with none of them written on a form-arrow class.
  A `LatticeEmbedding` built from images and one built from a module embedding answer the same operations.

- [ ] **`placement-audit`**. **Needs:** none.
  **Owner and delta:** every public object and element operation introduced on each owned category, judged by the `CAT-05` placement test: an operation introduced on `C` is misplaced when it is well-defined on a supercategory of `C`, and moves to `max W_f` over the up-set `U_C = {D > C}`.
  Arrow operations are placed by `arrows-thread-through-the-mor-category-graph`, since an arrow operation can move only to an arrow type that the arrow types below inherit.
  At its home an operation decides computability in one `case`/`match` on categorical containment: each case with a known algorithm routes to it, and the final `case _` asserts, naming the missing algorithm (`CAT-01`; AGENTS.md, *Abstract contracts are distinct from partial algorithms*).
  An operation placed low because only there can it be computed is the commonest misplacement: `conjugacy_classes`, `conjugacy_class`, `conjugation_g_set`, `left_cosets` and `right_cosets` sit on `Groups().Finite()` (`categories/group/groups.py`) though they are defined for every group, and they move to `Groups()` with the finite case as a route.
  Instrument: `just preamble-megadoc`, then `just placement [CATEGORY ...]`, forms the slice: for each category it prints the introduced object, element and arrow operations and the up-set `U_C` with each member's definition. It decides nothing about placement; `W_f` and its maximum come only from the investigation in the loop body.
  It also prints three mechanical findings: a name introduced on `C` and again in `U_C`; the lowest categories of `U_C` whose arrow type the arrow type of `C` does not inherit, and every Mor class that declares no arrow type; and each name introduced on pairwise incomparable categories, with their minimal common upper bounds in `P`.
  Loop body: one category `C`, with all of its introduced object and element operations handled together in the one pass. State the definitions of the categories in `U_C`. For every operation `f` introduced on `C`, state its mathematical definition with the data and hypotheses it uses, read from a source, never from its method body, which may use only what `C` happens to compute. Then decide, for all of them at once, which members `D` of `U_C` supply that data and satisfy those hypotheses for every object of `D`. Those members form `W_f`, and `max W_f` is the home of `f`. Move every operation whose home is above `C`, and route its computation.
  The categories are independent.
  A move that cannot be made in the loop body becomes its own node, named by the mathematics it needs, and this node `Needs` it: several maximal elements of `W_f`, or a maximum absent from `P`, is a missing category, axiom or property, or a defect in the declared graph (`degree` and `is_homogeneous` sit on `GradedAlgebras` and `GradedModules` with no common upper bound, so graded algebras are not declared graded modules); a consumer that breaks because it reached the operation through the old placement is repaired in the same loop body.
  `category-method-coverage-sweep` calls every method where it currently sits, so it certifies the current placement and cannot detect a misplacement; this node supplies that check.
  Each move is witnessed by an expectation that calls the operation on a specimen of the supercategory that is not in `C`.
  **Closure specimens:** `conjugacy_classes` asked of an infinite group reaches its own assertion, not an `AttributeError`; every owned category in the survey has had its pass, and each operation it moved answers on a specimen of its new home that is not in `C`.

- [ ] **`operations-sited-where-defined`**. **Needs:** none.
  **Owner and delta:** an operation at its general owner whose body calls one engine unconditionally, with no routing, contradicts the `case`/`match` rule that `placement-audit` applies at every home (`CAT-01`).
  The abelianization functor (`functors/abelianization.py`, `_apply_object`) calls `_gap_model` for every group, and `commutator_subgroup` guards with a bare finiteness assert, not a `case` whose last branch names the missing algorithm.
  Repair the population, not only these specimens.
  The tell, per subtree: `_gap_model(`, `_engine_ring(` or any other engine crossing at the top of an operation on a general category, outside a `case`.
  Before editing, record the commits that introduced these sites and the belief behind them: that an operation's home is where it is computable.
  **Closure specimens:** `Groups().abelianization()` applied to an infinite finitely presented group reaches the assertion, which names the missing presentation route, until `group-exact-sequences-and-homology` adds that case.

## Test suite: specimens, speed and coverage

The suite is the instrument that finds the rest; these make it fast and complete.

- [ ] **`category-method-coverage-sweep`**. **Needs:** none.
  **Owner and delta:** for every category in the live session, construct its objects on small specimens and call every public method of the object, its elements and its morphisms, asserting the mathematical value (owner, 2026-09-24). The categories and operations come from a regenerated `just preamble-megadoc` survey; one test file per category, written to `tests/constructions/CONTRIBUTING.md`'s session standard.
  Loop body: one category, its whole public surface in one pass: every operation of its objects, elements and morphisms, from the survey's listing of what the category introduces, written into that category's one file and banked in one commit. A file or commit per method or per surface is not the unit; the category is.
  **Closure:** every category of the survey has its file, and `just coverage-report` shows no public method of the preamble that no passing test calls, other than those whose failure is a recorded node.

## Runtime triage catalogue

The first full execution of the suite since the tree stopped importing (2026-09-07), run once as a triage catalogue on 2026-09-23 with `--no-time-gates --timeout=1 -o timeout_func_only=true` (16,311 tests collected): 11,874 failed, 4,335 passed.
Failures are grouped here by the site that raises them; paths are relative to `src/dzack_research/preamble/` unless a different root is given.
A node's cause is the defect behind its site, which the node establishes; the site and example are where to start.
Work the catalogue in one pass, not one site at a time: read every site below, group the sites whose failures share a cause, repair each cause at its owner, then re-run the catalogue once. A site that still raises keeps its node, and every node whose example passes and whose site no longer raises closes in that pass (AGENTS.md, *Architecture before tests*).
Regenerate the catalogue with the same command; the time gates are on by default.

- [ ] **`triage-native-module-additive-group`**. **Needs:** none.
  **Site:** `categories/modules/native_modules.py:102` and `:103`, `_RingModulePresentation.construct`: "the action is on the supplied owned additive group" (1,924) and "native scalar structure cannot overwrite another chosen base" (185). **Example:** `tests/algebras/test_module_structure.sage::test_forgetful_functor_sends_an_algebra_to_its_underlying_module`; `tests/rings/test_local_base_maximal_ideals.sage::test_dual_numbers_over_a_field_are_local_at_the_nilpotent_alone`.

- [ ] **`triage-framing-source-base-ring`**. **Needs:** none.
  **Site:** `categories/modules/pure/modules.py:3051`, `_fix_selected_module_framing`: "the selected framing source is a free module over this module's base ring" (1,571). **Example:** `tests/divisors/test_divisor_node_specimens.sage::test_normal_singular_surface_has_a_noncartier_weil_class`.

- [ ] **`triage-subobject-base-placement`**. **Needs:** none.
  **Site:** `categories/abstract_categories/arrow_categories.py:1087`, `SubobjectCategory.__init__`: "the subobject base must lie in its base category" (1,538). Reached from `_commutative_ideal` (`categories/rings/commutative_ideals.py:966`) through `Modules(R).Subobjects(R.regular_module())`; for `QQ['x,y']` the regular module is placed in `Modules(R)`, so the failing rings are the ones the Kähler-differential and cohomology constructions build.
  **Example:** `tests/algebras/test_cohomology.sage::test_dga_cohomology_is_a_graded_algebra_with_descended_product`.

- [ ] **`triage-an-object-contracts`**. **Needs:** none.
  **Site:** `sage/misc/abstract_method.py:218`: `NotImplementedError: <abstract method an_object>` (850): categories reached by the inhabitation specifications that do not exhibit an object.
  **Example:** `tests/algebras/test_native_free_algebra_module_factor.sage::test_free_algebra_on_the_zero_module_has_only_the_empty_word`.

- [ ] **`triage-owned-ring-custom-name`**. **Needs:** none.
  **Site:** `sage/cpython/getattr.pyx:362`: `'_OwnedRingParent_with_category' object has no attribute '_SageObject__custom_name'` (584): an owned ring reaches Sage's `rename`/repr machinery without `SageObject` initialization of that field.
  **Example:** `tests/algebras/test_center_corestriction_archive.sage::test_central_algebra_map_corestricts_through_the_actual_center`.

- [ ] **`triage-ring-cardinality-frontier`**. **Needs:** none.
  **Site:** `categories/rings/ring_foundation.py:2163`, `OwnedRings.ParentMethods.cardinality`: the exact computation covers only finite, countably infinite and uncountable placements (348). **Example:** `tests/algebras/test_affine_semigroup_algebras.sage::test_affine_semigroup_algebra_retains_its_selected_binomial_presentation`.

- [ ] **`triage-module-mor-endpoints`**. **Needs:** none.
  **Site:** `categories/modules/pure/modules.py:904`, `Modules.Mor`: "an R-module Mor requires two R-modules" (338). **Example:** `tests/algebras/test_de_rham.sage::test_relative_conormal_and_tangent_comparison_for_xy_equals_t`.

- [ ] **`triage-subring-base`**. **Needs:** none.
  **Site:** `sage/categories/rings.py:1705`: "base must be a subring of this ring" (177), raised by Sage when an owned construction passes a base that Sage does not recognize as a subring.
  **Example:** `tests/sets/test_standard_cardinals_archive.sage::test_matrix_ring_cardinality_tracks_the_coefficient_ring`.

- [ ] **`triage-an-element`**. **Needs:** none.
  **Site:** `sage/structure/parent.pyx:2847`: `please implement _an_element_` for join-category, product and coproduct parents (158 + 37 + 23). **Example:** `tests/functions/test_lebesgue_quotient.sage::test_quotient_keeps_a_nonzero_function_and_does_not_sample_callable_equality`.

- [ ] **`triage-category-c3-keys`**. **Needs:** none.
  **Site:** `sage/misc/c3_controlled.pyx:945`: `KeyError` on a category sort key while Sage linearizes super categories (143 + 49); a category is joined whose comparison key is not registered.
  **Example:** `tests/algebras/test_cartan_calculus.sage::test_vector_fields_are_derivations_and_have_the_expected_lie_bracket`.

- [ ] **`triage-construction-contract`**. **Needs:** none.
  **Site:** `owned_category.py:802`, the construction-contract check: invertible-sheaf categories on join-category schemes (138). **Example:** none current: the cited test was removed in b9b95babe, and `O(d)` on `P^n` no longer raises here (88d2dc923). Find an invertible sheaf on a join-category scheme that still raises at this site before working the node, or remove the node with that evidence.

- [ ] **`triage-selected-framing-at-construction`**. **Needs:** none.
  **Site:** `categories/abstract_categories/objects.py:264`: polynomial rings "constructed without" their selected framing (126). **Example:** `tests/algebras/test_relative_presentations.sage::test_zero_relation_presentation_lifts_through_the_identity_engine`.

- [ ] **`triage-indexed-cardinal-finiteness`**. **Needs:** none.
  **Site:** `categories/sets/cardinals.py:478`: "finiteness is not selected for an arbitrary indexed cardinal family" (108). **Example:** `tests/algebras/test_center_corestriction_archive.sage::test_exterior_algebra_center_is_the_archived_predicate_subring`.

- [ ] **`triage-discriminant-over-general-rings`**. **Needs:** none.
  **Site:** `categories/lattices.py:2222`: "discriminant_group is the ZZ specialization; use discriminant_module" (106), reached by `DiscriminantBilinearModules` over rings other than `ZZ`. **Example:** `tests/constructions/test_categories_inhabited.sage::test_a_category_over_a_ring_is_inhabited_over_every_ring[AA-DiscriminantBilinearModules]`.

- [ ] **`triage-toric-charts-over-fields`**. **Needs:** none.
  **Site:** `categories/schemes/toric/toric_schemes.py:1907`: "the semigroup algebras of the charts are algebras over a field" (100), reached by toric categories over non-fields.
  **Example:** `tests/constructions/test_categories_inhabited.sage::test_a_category_over_a_ring_is_inhabited_over_every_ring[GF(5)[t]-ADELogPairs]`.

- [ ] **`triage-missing-owned-operations`**. **Needs:** none.
  **Site:** `sage/cpython/getattr.pyx:357`/`:362`: `AttributeError` for operations the owned objects do not have: on module Mor elements (99 + 37), sparse free module object types (83), `DistinguishedAffineCovers.subcategory_class` (92), and the `mor`, `point_mor`, `nilradical`, `free_bilinear_form_adjunction` and `cardinality` names that the specifications call.
  **Example:** `tests/algebras/test_algebra_base_change_archive.sage::test_scalar_restriction_retains_the_selected_ring_map_identity`.

- [ ] **`triage-signature-over-ordered-fields`**. **Needs:** none.
  **Site:** `categories/_lattice.py:1296`: the signature pair asserted for quadratic spaces whose base is not a subfield of the reals (78). **Example:** `tests/constructions/test_categories_inhabited.sage::test_a_category_over_a_ring_is_inhabited_over_every_ring[AA-HyperbolicLattices]`.

- [ ] **`triage-kahler-backend`**. **Needs:** none.
  **Site:** `categories/algebras/derivations.py:61`: "the represented Kähler-calculus backend requires a symmetric algebra or a chosen finite commutative presentation" (74). **Example:** `tests/constructions/test_algebras_construct.sage::test_kahler_differentials_of_a_ring_over_itself_vanish[AA]`.

- [ ] **`closed-immersion-citation`**. **Needs:** none.
  **Site:** `categories/schemes/schemes.py`, `is_closed_immersion`, cites Stacks Tag 01HV, which is Lemma 26.5.4 (sections of `M~` on `Spec R`). Cite the Stacks result that a morphism of affine schemes is a closed immersion exactly when its ring map is surjective, after opening it.

- [ ] **`triage-long-tail`**. **Needs:** none.
  **Site:** the remaining 699 sites of the catalogue, together about 2,200 failures, among them `categories/rings/commutative_ideals.py:946` (59), `categories/group/g_sets.py:167` (54), `categories/modules/pure/modules.py:4681` (53), `categories/modules/framed/fraction_field_quotients.py:123` (50), `sage/matrix/matrix_gfpn_dense.pyx:429` (`GF(27)` in MeatAxe, 36), and 27 specification tests calling `Hom`, which the session does not export under `Mor` as its only spelling.
  Also: deciding whether an endomorphism of a free module lies in the image of the zero module's Mor (`module_morphisms.py:1139`, "cannot decide whether ... is in the image"), reached by the centre of a unital associative algebra (`tests/algebras/test_algebra_preservation.sage`). **Closure:** a re-run of the catalogue with no failure at these sites; split any site whose cause is shared by others into its own node first.

## Forms, actions and arithmetic realizations

- [ ] **`dual-lattice-through-the-discriminant-sequence`**. **Needs:** none.
  **Owner and delta:** for an `R`-lattice `L` with form `b` valued in `K = Frac(R)` and an `R`-submodule `S <= K`, `L^# = {x in V : b(x, L) <= O}` for `V = L_K = L tensor_R K`, and `L` is `A`-modular for a fractional ideal `A` when `A L^# = L`, unimodular when `A = O` (Kirschmer, *Definite quadratic and hermitian forms with small class number*, Def.
  2.3.3; arXiv:1904.04518, Def.
  2.1). For invertible `A`, `A L^# = {x in V : b(x, L) <= A}`, so `A`-modularity says this `A`-dual of `L` is `L`. Kirschmer's `L^A = {x in L : b(x, L) <= A}` (same Def., item 8) is the sub-bilinear module of `L` cut out by the same condition.
  The maps are `L -> L^#` when `b(L, L) <= O`, with cokernel `A_L`, and `L^# -> L^* = Hom_R(L, R)`, `x |-> b(x, -)`. The form on `L^*` is transported along that map.
  `Lattices.dual_lattice` (`categories/lattices.py`) instead equips the dual module with a `QQ`-valued form and refines it into `FormModules(ZZ).Nondegenerate()`, whose predicate asks for a correlation `M -> Hom_R(M, R)` (`categories/modules/hodge.py`, `_algebraic_correlation_morphism`) defined only for `W = R`. **Invariants:** the left and right radicals are the kernels of the two curried maps `L -> Hom_R(L, W)`, `x |-> b(x, -)` and `y |-> b(-, y)`, from `b: L tensor_R L -> W` by tensor-hom adjunction, for every value module `W`; nondegeneracy is that both radicals are zero.
  The `W = R` case is recovered, not special-cased.
  **Closure specimens:** `NamedLattices.TdP.dual_lattice()` returns `L^*` with its transported form and the map `L -> L^*`; `A_1` has `A_L = ZZ/2`; the form with Gram matrix `[[1,1],[1,1]]` on `ZZ^2` has a radical of rank one.

- [ ] **`orthogonal-reduction-sequences`**. **Needs:** `coset-spaces-of-finite-groups`, `spinor-norm-images`. **Owner and delta:** `Lattices.discriminant_reduction_sequence`, `spinor_norm`, `spinor_norm_sequence` and `witt_index` (`categories/lattices.py`), with the sequences `DiscriminantReductionSequence` and `SpinorNormSequence` there, the square-class group (`categories/rings/square_classes.py`) and the OSCAR adapters (`categories/lattice_engines.py`). Three obligations remain for a nondegenerate lattice `L` over `R`, `K = Frac(R)`, `L_K = L tensor_R K`. (1) The discriminant reduction cokernel `C_L = O(A_L)/f(O(L))` when `f(O(L))` is not normal in `O(A_L)`: the coset `O(A_L)`-set with its projection, the sequence then exact as pointed sets; `cokernel_projection` now asserts normality.
  \(2) The `K`-spinor norm cokernel `C_{sn_K}` for anisotropic `L_K` of dimension 1 or 2; the theorem-backed cases, isotropic `L_K` (O'Meara 55:2a) and dimension at least 3 (O'Meara 101:8), are answered.
  \(3) `sn_K` and the Witt index when `K` is a number field; they are computed for `K = QQ`, through OSCAR's `rational_spinor_norm` and Hecke's isometry classes of rational spaces ([COMPLAINTS.md](COMPLAINTS.md#the-spinor-norm-and-witt-index-are-computed-only-over-the-rationals)). **Closure specimens:** `tests/lattices/test_orthogonal_reduction_sequences.sage`, executed at T. For `A_2` the discriminant reduction cokernel is trivial and `\tilde O(A_2)` has index 2 in `O(A_2)`; for `A_1`, `O(A_{A_1})` is trivial, so `\tilde O(A_1) = O(A_1)`. For `U + A_1(-1)` (signature `(2,1)` in the `(2,n)` convention), `sn_QQ` of the reflection in a vector `v` with `(v,v) = -2` is the class of `1`, its `sn_RR` is `+1`, and it lies in `O^+`; the reflection in a vector of square `2` lies in neither kernel.
  `SO_{sn_QQ}(L)` is contained in `SO(L)` for this lattice, properly.
  On `<6>`, `sn_QQ(-1) = [-3]`. The `QQ`-spinor norm cokernel of `E_8` has order 2 with the multiplier `-1/2` and order 1 with `1/2`. `U + U` has Witt index 2 over `QQ`, `U + A_1(-1)` has Witt index 1, and `E_8` has Witt index 0.

- [ ] **`coset-spaces-of-finite-groups`**. **Needs:** none.
  **Owner and delta:** `categories/group/g_sets.py` and `categories/group/groups.py`. For a finite group `G` and a subgroup `H`, the left cosets `G/H` as an object of `FiniteGSets(G)` pointed at `H`, with the equivariant projection `G -> G/H`; when `H` is normal it is the quotient group of `SubgroupInclusion.cokernel()`, and the two agree.
  For a morphism `f: G -> G'` of finite groups, `G'/f(G)` makes `1 -> ker f -> G -> G' -> G'/f(G) -> *` exact as pointed sets; `DiscriminantReductionSequence.cokernel_projection` uses it for a non-normal image ([COMPLAINTS.md](COMPLAINTS.md#the-quotient-of-a-group-by-a-non-normal-subgroup-has-no-owned-coset-construction)). **Closure specimens:** `S_3/C_2` has three points, permuted transitively by `S_3`; for `L = A_2 + A_2 + E_6`, the image of `O(L)` in `O(A_L)` (order 48) has order 16, is not normal, and `C_L` has three points.

- [ ] **`spinor-norm-images`**. **Needs:** none.
  **Owner and delta:** the image `sn_K(O(V))` in `QQ.square_class_group()` of the spinor norm of an anisotropic quadratic space `V` over `QQ` of dimension 1 or 2, and the quotient of the square-class group by it with its projection, for `SpinorNormSequence.cokernel_projection` (`categories/lattices.py`). In dimension 1, `O(V) = {±1}` and the image is `{[1], [c(v,v)]}`; in dimension 2 it is generated by the reflection classes `[c(v,v)]` and the products of two values of `V` (O'Meara 55:2), with membership decided through the values of `V` (Hecke's `represents`). It needs an owned quotient of an abelian group by a subgroup with a membership decision ([COMPLAINTS.md](COMPLAINTS.md#the-image-of-the-spinor-norm-of-an-anisotropic-binary-or-unary-space-is-not-computed)). **Closure specimens:** for `<6>` the image is `{[1], [-3]}`, so the projection sends `[-3]` to the identity and `[-1]` elsewhere.

- [ ] **`infinite-rank-lattice-base-change`**. **Needs:** none.
  **Owner and delta:** `Lattices.base_change` (`categories/lattices.py`) builds `L tensor_R S` in `Lattices(S)` from the Gram matrix, so only in finite rank.
  In infinite rank the Gram presentation is a pairing rule (`_PairingGram`, `categories/_lattice.py`), and `L tensor_R S` is the lattice in `Lattices(S)` on that rule carried along `R -> S` ([COMPLAINTS.md](COMPLAINTS.md#scalar-extension-of-an-infinite-rank-lattice-is-not-a-lattice)). **Closure specimens:** the base change of `Lattices(ZZ)(ZZ^NN)` along `ZZ -> QQ` is in `Lattices(QQ)`, of infinite rank, with `e_0^2 = 1` and `e_0 . e_1 = 0`.

- [ ] **`lattice-represents-an-integer`**. **Needs:** none.
  **Owner and delta:** `Lattices(R)` answers the existential question whether `L` represents `n`, i.e. whether the hypersurface `V(q - n)` has an `R`-point.
  It also answers `representation_vector(n)`, a witness as an element of `L`. The elementwise `represents` on form-module elements (`categories/modules/framed/formed/form_modules.py`, ~line 1260) is a different statement and stays.
  Routing is `case` on categorical membership.
  Definite: short-vector enumeration (PARI `qfminim`), with the theta series when many `n` are asked.
  Indefinite rank 2: binary-form reduction (PARI `qfbsolve`). Indefinite rank >= 4: the real place and `L_p` for `p | 2 n det(L)` (Kneser; strong approximation for the spin group).
  Indefinite rank 3: the local test, then the finitely many spinor-exceptional square classes (Schulze-Pillot; Earnest--Hsia), decided by a witness search.
  `n = 0` is isotropy (Hasse--Minkowski; Meyer for rank >= 5). Every theorem is cited from its source, and every engine call is private.
  **Closure specimens:** `E_8` represents 2 and not 1. `U` represents every integer.
  `A_1(-1) + A_1(-1) + A_1(-1)`, the form `-(x^2 + y^2 + z^2)`, does not represent `-7`, the Legendre obstruction at 2. `U + U` represents 0 with a nonzero witness.

- [ ] **`lattice-reflection-groups`**. **Needs:** none.
  **Owner and delta:** every lattice `L` owns *the* reflection group `W(L) = <s_v : v in L_K, s_v in O(L)>` and `W_S(L) = <s_v in W(L) : v^2 in S>` for `S <= ZZ`, as `L.reflection_group(S)`. Its default `S` is the finite set `{n : n | 2 e(A_L)}` of admissible norms, so the call with no argument is `W(L)`. It is a subgroup of `O(L)`. When `L` is definite (finite root system) or hyperbolic (`W(L) cap O^+(L)`, the reflections in vectors of negative norm), it is also an object of a category of Coxeter groups, carrying the Coxeter system of a chamber: simple roots and Coxeter matrix, of possibly infinite rank.
  The hyperbolic Vinberg route (`categories/hyperbolic_lattices.py`, `reflection_group`) becomes the hyperbolic specialization of this construction.
  A search that did not complete yields a stated subgroup of `W(L)`. The second name `weyl_group` is removed and its callers are moved.
  The theory, still to be checked against its sources, is in `docs/theory/lattice-reflection-groups.md`. **Closure specimens:** `W(E_8)` is the finite Coxeter group of type `E_8` (order 696729600). For an even 2-elementary lattice, `W(L) = W_{-2,-4}(L)`. `U + <-6>` has a reflection in a norm `-6` vector, so `W(L) != W_{-2,-4}(L)`. `II_{1,9}` has Coxeter diagram `E_10`.

- [ ] **`group-exact-sequences-and-homology`**. **Needs:** `operations-sited-where-defined`. **Owner and delta:** one owned construction for a short exact sequence of groups `1 -> N -> G -> Q -> 1`: the normal subobject `N -> G`, the quotient `G -> Q`, and exactness.
  `RankOneParabolicLeviExactSequence` (`categories/lattices.py`) and the discriminant reduction sequence are instances of it, not separate classes.
  Exactness only as pointed sets, when the image is not normal, is the case of `coset-spaces-of-finite-groups`. The first instance is the commutator sequence `1 -> [G,G] -> G -> G^ab -> 1`, whose quotient map is the unit of `(-)^ab -| i` (`functors/abelianization.py`). Group homology `H_n(G; M)` and cohomology `H^n(G; M)` for a `ZZ[G]`-module `M`, as derived functors of coinvariants and invariants: through the resolution categories of `categories-of-resolutions`, computed privately by GAP's HAP or Sage.
  With them come the identifications `H_1(G; ZZ) = G^ab` (from `I_G/I_G^2 = G^ab` for the augmentation ideal `I_G`), `H^1(G; ZZ) = Hom(G, ZZ) = Hom(G^ab, ZZ)`, which sees only the free part, and `H^2(G; ZZ) = Hom(G, QQ/ZZ)` for finite `G`, the Pontryagin dual of `G^ab` (Brown, *Cohomology of Groups*, II.3 and III.1; cite from the source).
  Computation routes: finite `G` through GAP. Finitely presented `G` computes `G^ab` from its chosen presentation, by the Smith normal form of the abelianized relation matrix, including for infinite `G`. A Coxeter group `W` has `W^ab = (ZZ/2)^c`, with `c` the number of classes of Coxeter generators joined by paths of odd labels (read from the Coxeter matrix; `lattice-reflection-groups`). `O(L)`, for `L` containing enough hyperbolic planes, has its abelianization detected by the determinant, the spinor norms and the discriminant reduction (the classical theory of the stable orthogonal group; find and cite the precise theorem and its hypotheses before using it).
  Predicate-defined subgroups of `O(L)` go through the kernel route that `cokernel` already uses.
  **Closure specimens:** `S_3^ab = ZZ/2` with `[S_3, S_3] = A_3`. The free group `F_2` has abelianization `ZZ^2`, computed from its presentation.
  `SL_2(ZZ)^ab = ZZ/12`. `H_1(ZZ/n; ZZ) = ZZ/n`, `H^1(ZZ/n; ZZ) = 0`, `H^2(ZZ/n; ZZ) = ZZ/n`. `W(E_8)^ab = ZZ/2`.

- [ ] **`subobjects-retain-their-inclusions`**. **Needs:** none.
  **Owner and delta:** anything that is a subobject mathematically is returned through the subobject categories and APIs and keeps its monomorphism into its ambient object.
  It is never an independent object with no morphism: subgroups, stabilizers, centralizers, kernels, images, intersections, sublattices, submodules, subschemes and pullback apexes alike.
  A group that lands in a finitely generated or finitely presented category always answers its group generators and, where chosen, its presentation.
  The routing happens once at the group level, by `case` on membership, with a subtree of case-specific algorithms (GAP for finite groups, Schreier generators for finite index, reflection generators for Coxeter groups, and so on).
  The last case asserts which algorithm is missing (`CAT-01`, `operations-sited-where-defined`). Survey the population by these tells: a subgroup or submodule constructor returning a parent with no `inclusion()`; `_own_group(` or `_subgroup_from_gap(` results whose ambient is not recoverable; `FinitelyGenerated` or `FinitelyPresented` placements with no `group_generators` route.
  Before editing, record how the population entered and the belief behind it.
  **Closure specimens:** `O(L).centralizer(g).inclusion()` has codomain `O(L)`. `SL_2(ZZ).commutator_subgroup()` answers group generators through the finite-index route.
  A kernel of a group morphism answers its inclusion into the domain.

- [ ] **`pullbacks-in-every-category`**. **Needs:** none.
  **Owner and delta:** the fibre product `A x_C B` of a cospan is constructed once, at the general owner (`Cat.fiber_product` in `abstract_categories/cat.py`, from `product` and `equalizer`), and it is reachable in sets, groups, modules, algebras, schemes and every category with products and equalizers.
  The result is the limit cone: the apex, both projections and the universal map, never a bare object.
  Leaf categories only place structure and properties on the apex so that it lives in the correct category: a subgroup of `A x B`, a submodule, a subalgebra.
  Schemes are the case where the fibre product is not the fibre product of underlying sets.
  Where a leaf has a better construction, it supplies one that realizes the same universal property.
  Leads: `docs/theory/glue-stabilizers.md`, *Pullbacks*. **Closure specimens:** the pullback of `ZZ -> ZZ/2 <- ZZ` in groups is the index-2 subgroup of `ZZ^2` with its two projections.
  The fibre product of two points over a point is a point in both sets and schemes.
  `Spec QQ(i) x_{Spec QQ} Spec QQ(i)` has two points.

- [ ] **`images-of-subgroups-and-predicate-subsets`**. **Needs:** none.
  **Owner and delta:** research, then construction.
  The image of a subgroup with generators under a group morphism is the subgroup generated by the images, as an owned subobject of the codomain.
  The image of a subset given only by a predicate is an existential projection, `{f(x) : P(x)}`, and is not computable in general.
  Survey what is known before choosing a representation: SymPy `ImageSet` and `ConditionSet`, quantifier elimination (Tarski–Seidenberg; Presburger), Chevalley's theorem for constructible images with elimination, and the finite-index Schreier route that turns a predicate subgroup into one with generators.
  Record the decidability boundary and which route each represented case uses.
  Leads: `docs/theory/glue-stabilizers.md`. **Closure specimens:** the image of `O(A_2)` under `rho` is computed from generators.
  The image of a predicate subgroup of finite index in `O(L)` is computed through its Schreier generators.
  A predicate subset with no route reaches an assertion that names the missing algorithm.

- [ ] **`finite-index-subgroup-generators`**. **Needs:** `coset-spaces-of-finite-groups`, `subobjects-retain-their-inclusions`. **Owner and delta:** a subgroup `H <= G` given by a membership test, known to have finite index (for example a preimage of a subgroup of a finite quotient), with `G` given by generators, answers generators of `H` by Schreier's lemma.
  It uses the action of `G` on the coset space and a transversal from `finite_image_lifts`. When `G` has a chosen presentation, it answers a presentation of `H` by Reidemeister–Schreier.
  This becomes a `case` of the group-level generator routing.
  Leads: `docs/theory/glue-stabilizers.md`, *Generators of finite-index subgroups*. **Closure specimens:** the kernel of `SL_2(ZZ) -> SL_2(ZZ/2)` has index 6, and its generators generate a subgroup of index 6. `\tilde O(L)` for an indefinite `L` with a generating set of `O(L)` answers generators, and each lies in the kernel of `rho`.

- [ ] **`lattice-glue-stabilizers`**. **Needs:** `pullbacks-in-every-category`, `finite-index-subgroup-generators`, `images-of-subgroups-and-predicate-subsets`, `operations-sited-where-defined`. **Owner and delta:** for a primitive extension `S + T -> L` with glue `gamma: H_S -> H_T` (`Lattices.glue_map`), the preamble constructs:

  - the restriction morphisms `Stab_{O(L)}(S) -> O(S)` and `-> O(T)`, and `rho-bar_S: O(S)_{H_S} -> O(H_S)`;

  - `Stab_{O(L)}(S)` as the owned pullback `O(S)_{H_S} x_{O(H)} O(T)_{H_T}`, with its projections and the gluing map back into `O(L)`;

  - `Gamma_{h,T} = rho-bar_T^{-1}(gamma rho-bar_S(O(S,h)) gamma^{-1})` as a subgroup of `O(T)` with its inclusion.
    With generators of `O(S,h)` and `O(T)` (and relations, if any), it answers generators (and a presentation) of `Gamma_{h,T}`. The theory and its leads (Peters–Sterk 15.1; Nikulin 1979) are in `docs/theory/glue-stabilizers.md`. **Closure specimens:** for `L = U + U` with `S = U` and `T = U`, the stabilizer of `S` is `O(U) x O(U)`. For `L` unimodular, `Gamma_{h,T} = rho_T^{-1}(gamma rho_S(O(S,h)) gamma^{-1})`. For a rank-one `S = <h>` with `h^2 = 2` in `II_{1,9}`, the pullback description reconstructs the stabilizer of `h`.

- [ ] **`coxeter-group-structure`**. **Needs:** `lattice-reflection-groups`, `operations-sited-where-defined`. **Owner and delta:** the category of Coxeter systems `(W, S)` owns:

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

- [ ] **`modular-forms-and-hecke-algebras`**. **Needs:** `finite-index-subgroup-generators`, `operations-sited-where-defined`. **Owner and delta:**

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

## Common categorical authority and public boundaries

- [ ] **`genera-are-finite-sets-of-isometry-classes`**. **Needs:** none.
  **Owner and delta:** `Genus` in `categories/lattices.py` (line 371) is a plain Python class holding a signature and a discriminant quadratic form.
  A genus of integral lattices is the finite set of isometry classes of lattices with that signature and discriminant form, so it is an object of a category of genera that forgets to finite sets.
  Its cardinality is the class number, and parity (even or odd) is an axiom on it, the same for every member.
  It is constructed through its owner, not as a bare class, per `CAT-28`. `representatives()` and `class_number()` become that set's enumeration and cardinality.
  The spike built this and it reached main's history as PR #59 (`d2891a225`) and `5766b97d1`, then was lost when the spike was absorbed; do not port that code.
  **Closure:** the genus of `E8` has cardinality 1; the genus of `E8 + E8` has cardinality 2 (`E8 + E8` and `D16^+`); the genus of `A2` is even; the genus of `I_1 + I_1` is odd; `representatives()` enumerates that finite set.

- [ ] **`group-categories-defined-by-data`**. **Needs:** none.
  **Owner and delta:** `categories/group/groups.py`. The groups whose category is fixed by mathematical data, per `CAT-28`: `SymmetricGroups()(Omega)` for a set `Omega`, `GeneralLinearGroups()(R, n)`, `FreeGroupQuotients()(F, R)` (a free group and a set of relators), `CoxeterGroups()(M)` for a Coxeter matrix, and an `Arithmetic` axiom on `OwnedGroups`. Each is built from main's current `groups.py`, with its morphisms and its `CAT-22` owner search.
  `remediate/groups` (`bbce862e3`, deleted 2026-09-25) drafted these, and complaint 10 in `COMPLAINTS.md` records why that draft was rejected: it replaced working catalogue entries with assertions, and it gave a number field the automorphism group of the original field as its Galois group.
  **Closure:** `SymmetricGroups()(Sets.Delta[2])` has order 6; `GeneralLinearGroups()(GF(2), 2)` has order 6 and is isomorphic to it; `FreeGroupQuotients()(F_2, {a^2, b^3, (ab)^2})` has order 6; `CoxeterGroups()` of the `A_2` matrix is that same group; the arithmetic axiom holds for `SL_2(ZZ)`.

- [ ] **`engine-wiring-audit`**. **Needs:** none.
  **Owner and delta:** every owned construction that computes, itself, behaviour a maintained engine provides, starting with the set layer (`categories/sets/`): membership, position and order of finite sets, images, products, coproducts, power sets and function sets, as tabulated in [COMPLAINTS.md](COMPLAINTS.md#set-theoretic-behaviour-is-re-implemented-instead-of-wired-to-a-set-engine), then the whole preamble.
  **Invariants:** public mathematics stays owned; the computation behind it is the engine's, reached privately at its owner (`OWN-06`). A membership decision follows the set's definition -- predicate, identity of listed points, inverse of an image -- and never searches an enumeration.
  An enumeration is a chosen bijection from an ordinal, separate from membership.
  No owned code re-implements what Sage, GAP, SymPy, PARI or the Python standard library computes, unless the engine lacks it, which is then recorded in `TRAPS.md` with the measurement.
  **Coverage:** survey the preamble once for owned code whose body is a general algorithm -- loops that search, compare element by element, enumerate to decide, or rebuild an object to read one value -- and map each to the engine routine that computes it or to the recorded reason there is none.
  The profiled sites of 2026-09-23 are the first evidence, not the population.
  **Closure specimens:** membership of a point in a finite set of SR symbols, an image, a product and a power set answered without comparing against every point; a rank-16 diagonal lattice built in time linear in its Gram entries; each audited family's route read from its public entry to the engine call.
## Public mathematical interaction

## Source convergence and terminal proof

- [ ] **`architecture-remediation`**. **Needs:** `engine-wiring-audit`, `dual-lattice-through-the-discriminant-sequence`, `orthogonal-reduction-sequences`, `infinite-rank-lattice-base-change`. **Owner and delta:** the integrated source route from public category entry through complete defining data, private computation and every owned result and consumer, against all unresolved complaints.
  **Invariants:** every required source descendant closes before this node; introducing a residual child keeps this node open.
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

- [ ] **`function-spaces-are-subobjects-of-mor`**. **Needs:** none.
  **Owner and delta:** the owned function spaces (`categories/functions/real_functions.py`), under `CON-17`. Each space is a family of functors in both arguments, and its constructor takes both: `C(n, A, B)`, `Lp(p, A, B)`, `ell(p, A, B)`; the tests now construct `C(Infinity, RR, RR)`, `Lp(2, RR, RR)` and `ell(2, NN, RR)`. Coordinates are owned by the domain: `RR.coordinate()` is the coordinate of ℝ (for ℝ² it is the pair (x = (x_0, x_1))), and a map is built from it, `C(Infinity, RR, RR)(x^2 + 1)`. `Lp(p)` (maps ℝ → ℝ) is built with `indeterminate=SR.var("x")` and `ell(p)` (maps ℕ → ℝ) with `SR.var("n")`; each stores the variable, hands it out as `indeterminate()`, and reads `space(expr)` as the map t ↦ expr.
  The delta: each space is the subobject of `Sets().Mor(X, Y)` cut out by its condition (integrability, summability, smoothness, boundedness), with its module structure; element construction is `Mor(X, Y)`'s element constructor (callables, formulas binding their own variable, finitary data), and the space admits the element by its condition; `indeterminate()` and the stored variable are removed, together with their consumers: `convolution.py` and `lebesgue_quotients.py` substitute into `parent().indeterminate()`, and `modules/pure/function_modules.py:378` defaults a formula's variable to `x`. Each works on the map it is given.
  **Observed:** the formulas are Sage symbolic expressions in the stored variable, and owned numbers never enter Sage's symbolic ring (`AGENTS.md`, ruled 2026-09-23), so `x**2`, `2 ** (-n)` and `1 / (1 + x**2)` raise `TypeError` in `tests/functions/test_function_modules_archive.sage`, `test_real_functions.sage` and `test_young_convolution.sage`. Those tests use `indeterminate()` and are rewritten with the delivery to define their maps (`f(t) = exp(-t^2)`). **Closure:** the maps t ↦ t², t ↦ 1/(1 + t²), t ↦ exp(−t²) and k ↦ 2⁻ᵏ, each defined with its own variable, are constructed in `Mor(X, Y)` and admitted by their spaces; no space supplies a point of its domain, and `X.coordinate()` of a function space, where it exists, is a general element of that space.

- [ ] **`suite-within-time-gates`**. **Needs:** none.
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

- [ ] **`terminal-session`**. **Needs:** `architecture-remediation`, `group-categories-defined-by-data`, `triage-native-module-additive-group`, `triage-framing-source-base-ring`, `triage-subobject-base-placement`, `triage-an-object-contracts`, `triage-owned-ring-custom-name`, `triage-ring-cardinality-frontier`, `triage-module-mor-endpoints`, `triage-subring-base`, `triage-an-element`, `triage-category-c3-keys`, `triage-construction-contract`, `triage-selected-framing-at-construction`, `triage-indexed-cardinal-finiteness`, `triage-discriminant-over-general-rings`, `triage-toric-charts-over-fields`, `triage-missing-owned-operations`, `triage-signature-over-ordered-fields`, `triage-kahler-backend`, `closed-immersion-citation`, `triage-long-tail`, `category-method-coverage-sweep`, `function-spaces-are-subobjects-of-mor`, `suite-within-time-gates`, `scalar-extension-is-order-independent`, `genera-are-finite-sets-of-isometry-classes`, `arrows-thread-through-the-mor-category-graph`, `placement-audit`.

- [ ] **`scalar-extension-is-order-independent`**. **Needs:** none.
  **Site:** `categories/algebras/`, algebra scalar extension along `ZZ -> QQ`. `tests/algebras/test_algebra_base_change_archive.sage::test_archived_algebra_base_change_is_the_live_scalar_extension_functor` passes when its file runs alone and fails when `tests/modules`, `tests/sets`, `tests/rings`, `tests/forms` and `tests/tensors` ran first in the same process, with `TypeError: cannot apply Algebra scalar extension along ZZ -> QQ ... to Generic endomorphism of Ring over Integer Ring: it is not a morphism ... of Category of algebras` (observed 2026-09-26, before and after the coordinate sweep).
  A construction whose answer depends on what the session built earlier reads shared state that some earlier construction changed; the node finds that state and makes scalar extension read only its own data.
  **Closure:** the test passes in the batched run.

  **Owner and delta:** execute the integrated mathematical proof burden on the final owned session and research notebook; `DEV-58` governs this transition.
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

## Post-remediation convergence

- [ ] **`refactor-audit`**. **Needs:** `terminal-session`. **Goal:** After the repaired mathematics runs end-to-end, audit the repository for duplicated authority, poor organization, and maintainability defects that survived the architecture work.
  Audit the whole repository for messy, disorganized or duplicated code after the complaint-derived architecture has been exercised through the final public session.
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

## Optional research consumers

These are not prerequisites for the required mathematics, complaint remediation, terminal verification, or convergence audits.

- [ ] **`optional-framed-manifolds`**. **Needs:** `terminal-session`, `optional-manifold-tangent-bundles`. **Goal:** the framed manifolds of `CAT-29`: a smooth manifold with a length-0 resolution of its tangent bundle by trivial bundles, i.e. a trivialization of `TX` (nLab *framed manifold*; the `G = {e}` G-structure), with stable framings as trivializations of `TX + R^k` and `n`-framings as trivializations of `TX + R^(n - dim X)`. Specimens: `S^1` and a Lie group framed by left-invariant vector fields; `S^2` not framable and stably framable.

- [ ] **`optional-brauer-manin-obstructions`**. **Needs:** `terminal-session`. **Goal:** the Brauer--Manin pairing `X(A_k) x Br(X) -> Q/Z` and the obstruction sets for rational and integral points of varieties over a number field `k`, with the cases where the obstruction is computable or is the only one.
  Tori and their torsors (Sansuc).
  Homogeneous spaces of connected linear groups with connected or abelian stabilizers (Borovoi).
  Integral points on spin-group homogeneous spaces, including the rank-3 spinor exceptions of `lattice-represents-an-integer` (Colliot-Thelene--Xu; Borovoi--Demarche).
  Supersolvable finite stabilizers (Harpaz--Wittenberg).
  Abelian varieties, where the obstruction agrees with Sha (Manin).
  Cite each theorem from its source.
  **Construction rule:** nothing here is implemented ad hoc.
  Every notion used to state or compute these results is an owned construction in the preamble, and this node is exploded into its prerequisite DAG before any leaf is built (`DEV-56`, *A missing foundation parks the work that found it*). The expected prerequisites, to be confirmed by that trace: `G_K`-modules and Galois representations; étale cohomology specializing to Galois and group cohomology; categories of algebraic groups and their theory, with connectedness, commutativity, reductivity and simple connectedness decided or theorem-backed; tori with their character and cocharacter lattices as Galois lattices; torsors and principal `G`-bundles; homogeneous spaces and stabilizers in general; Tate--Shafarevich groups; symmetric spaces and basic Shimura-variety machinery; abelian varieties with elliptic curves as a specialization, their cohomology with its structures, torsion subgroups and Tate modules; the Brauer group of a scheme.
  **Specimens:** the Iskovskikh conic bundle, or the Cassels--Guy cubic, failing the Hasse principle through a Brauer class; an integral spinor-exceptional example taken from Colliot-Thelene--Xu, which has local points everywhere and fails only through the integral Brauer--Manin obstruction.

- [ ] **`optional-manifold-tangent-bundles`**. **Needs:** `terminal-session`. **Goal:** the tangent bundle of an object of `SmoothManifolds` (`categories/manifolds.py`) as an owned vector bundle, with its module of sections `Der(C^oo(M))`, realized through SageManifolds' tangent bundle privately.
  Specimen: `TS^1` trivial of rank 1.

- [ ] **`optional-random-lattices-of-given-invariants`**. **Needs:** `terminal-session`. **Goal:** random lattices in `Lattices(ZZ)` with a prescribed signature, determinant or rank, built as a random `SL(n, ZZ)` congruence `A^T G A` of a diagonal Gram matrix with Sage's randomness scoped by `seed()`, returning owned lattices, not matrices; and a random isotropic subgroup of a discriminant module (`categories/modules/framed/formed/discriminant_modules.py`, next to `isotropic_subgroups`), feeding `overlattice`. Prior art and its tests: `archives/random-lattice-constructors/`. State the limit: congruence of a diagonal form reaches only odd unimodular lattices, so a random lattice within a genus needs a different construction.

- [ ] **`optional-moduli-of-stable-curves`**. **Needs:** `terminal-session`. **Goal:** the moduli of stable pointed curves over the owned scheme categories.
  The category of stable graphs of type `(g, n)` with contractions and automorphisms, the stratification of `Mbar_{g,n}` by dual graphs, and charts for `M_{0,n}`, `Mbar_{0,n}`, `M_{1,n}`, `M_{2,n}`. The cited values (Harris-Morrison, Arbarello-Cornalba, Chan) become rows of `tests/test_known_mathematics.sage` with their citations.
  Prior art: `archives/dm-moduli-spike/`.

- [ ] **`optional-sage-categories-property-layer`**. **Needs:** `terminal-session`. **Goal:** rebuild the preamble's category machinery on the kernel and `Cat` core of `sage-categories` (github.com/dzackgarza/sage-categories), starting with its property layer.
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
