# Preamble TODO

## Execution priorities

Build the remaining general scheme-theory toolkit from the current `src/dzack_research/preamble/` tree.
Complete shared mathematical dependencies before extending their consumers.
Geometry has priority over independent arithmetic applications; an arithmetic computation moves earlier only when a named geometric construction needs its result.

Among ready nodes, take the groups below in this order (owner, 2026-09-25): wrong answers; the foundations that block many consumers; the test-suite nodes; the remaining runtime triage catalogue; then the forms, categorical-authority and public-interaction nodes that feed `architecture-remediation`. Geometry-before-arithmetic breaks ties within a group. Priority orders ready nodes; it is never an edge.

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

The queue is the scheduling surface. Completed prerequisite rows and their edge references are removed together, so the ready frontier is precisely the rows with `Needs: none`.
Recompute the ready frontier from the current rows before selecting work; do not preserve dated frontier counts or a private list of what was ready in an earlier turn:

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
   Derive that family from the original requirement and source declarations before comparing it with the delivered routes. Read called helpers and overrides; a changed-file list or a set of search matches is not the family.
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

The rows group obligations; only unchecked nodes schedule work. Complexity follows [COMPLEXITY.md](COMPLEXITY.md), measures the assigned responsibility, and is reassessed when a leaf's inputs are settled.

| Work | Shared output and closure boundary | Complexity and reason |
| --- | --- | --- |
| Constructor/admission foundations | One datum and admission authority; framing, tensor, scalar and algebra laws survive all routes | 90: recursive construction and shared mathematical identity |
| Diagrams/rings/geometry | Universal maps, varying-ring descent and projectivization through existing owners | 85: variance, base changes and general-versus-specialized constructions |
| Forms/actions/arithmetic | Exact forms, duals, group actions and owned arithmetic witnesses | 85: weak hypotheses, infinite objects and completeness of algorithms |
| Common categorical authority | Single functor/adjunction/provenance authority, inherited operations and recursive ownership | 90: contracts span multiple consumer families |
| Maintained computation | Complete engine result/maps and exact computational frontiers | 80: upstream capability and representation contracts |
| Public interaction | Mathematical vocabulary, coordinate boundary, codomains and research narrative | 65: coherent migration of all consumers |
| Terminal proof and convergence | Executed distinguishing evidence, then finite whole-repo review and justified typing repair | 15 for execution; score newly observed repairs at their actual owners |

Among ready items, close a shared constructor/admission prerequisite before its dependent API polish. Geometry precedes independent arithmetic. An already-integrated route is preserved and reviewed against its remaining obligation, not rewritten from its historical complaint. Carry one node to its full source acceptance before selecting another (`DEV-60`). No workstream gets a separate claim/status ledger.

### Invariants required to close any source node

The node's own contract and `DEV-67` are conjunctive. Review the complete affected entry and consumer family, not only its first specimen. Every source delivery must establish:

- **Defining datum:** the exact owned objects, maps, base and hypotheses are fixed by one constructor; structure is the defining morphism, and checks and structure tables are computed only when asked for (`CON-16`, `OWN-22`, `OWN-23`).
- **Inherited structure:** the immediate general construction supplies its actual operations; stronger structure adds only its own data. Retained input, free-functor source and underlying object are not conflated (`OWN-14`--`20`).
- **Mathematical maps:** domains, codomains, equations, universal factorizations and transport agree. Dimension/rank/cardinality agreement is insufficient.
- **Ownership and computation:** every reachable result is owned; protected access stays at its declared owner; a maintained semantic computation is actually reused (`OWN-04`--`08`).
- **Required generality:** preserve represented infinite objects, nonfree modules, nontrivial coefficients and exact hypotheses. `Unknown` is not true, a finite window is not the object, and an abstract placeholder is not a delivered concrete operation.
- **Proof transfer:** bank a positive and a separating nearby invalid/different specimen, and preserve execution under T. Specimens falsify particular substitutes; source coverage must separately discharge every clause and required regime. Naming a child or removing an API transfers no burden by itself. Aggregate closure requires all required descendants closed.

Writing or revising this DAG records work; it does not execute or close the nodes. During subsequent source implementation, `DEV-58` defers Sage, tests, QC, notebook execution and live megadoc generation until T; inspect current source alongside the existing generated reference. Specimens stated below describe mathematics and do not invent callable APIs.

### Delivery and regression boundaries

The unit of source delivery is the repaired owner together with the actual consumers of its changed contract. At selection, identify that family from declarations, construction routes and callers, and compare it with the original requirement. At closure, account for every required route and regime in the delivery commit. Keep only concrete unfinished obligations in the node. No additional registry or compliance artifact is required.

| Boundary being changed | What must hold before its consumer proceeds |
| --- | --- |
| Admission or a defining equation | The owner distinguishes decided laws, construction-derived laws and unresolved hypotheses on the actual datum. A dependent conclusion carries those hypotheses; a category label or caller assurance cannot turn them into established laws. |
| Mutually recursive constructors | The common repair supplies a well-founded construction on fixed data and a real consuming map. Neither half closes on the promise that the other will later remove the recursion. |
| A producer with private access, placement or inherited-operation defects | Repair those defects on the affected route in this delivery. Later boundary, membership and inheritance sweeps own independently untouched routes only. |
| A later edit to a delivered contract | Preserve its previous equations, generality and separating specimens. Inspect the changed owner and affected callers against the preceding delivery; before T bank the additional evidence, and during T re-execute it. |
| A counterexample to a shared repair method | Inspect its other applications and restore the affected prerequisite before consuming it. Reopen that concrete obligation with its original burden; independently established work stays closed. |
| A whole-family claim | Reconcile the source-derived family with the requirement clause by clause, including helpers, alternate constructors and inherited paths. Passing a specimen or exhausting the first search cannot close an uninspected route. |

For example, an equalizer factorizer delivered by admission cannot retain an unchecked flag or open another object's engine on the ground that `private-owner-boundaries` comes later. Conversely, an unrelated untouched geometric adapter does not become a prerequisite of this module repair. The residue sweeps below reconcile that remainder across the full named scope.

### Bounded closure

This queue preserves the full required scope while avoiding repeated whole-tree reconstruction. Select the earliest ready shared repair with its consumer; then prefer ready geometric work. Independent arithmetic remains required but does not block a geometric route that does not consume it.

For each subtree or repository sweep, establish its finite source population and obligation family at entry from the live tree, the original requirement and the implicated declarations. Cover each route once under that sweep's stated questions. Reuse earlier source evidence only after checking that neither the route nor its dependencies changed. Record the inspected boundary in delivery commits; keep concrete findings in the existing open node or an actual repair prerequisite. Search counts are navigation aids, never the progress measure.

A repair triggers review of its diff, its consumer impact and the relevant proof, not another unrelated whole-tree pass. A newly discovered dependent defect extends that repair's obligations; a newly discovered independent required defect gets its own owner and edge. Neither creates a new general audit round. The terminating condition is complete stated coverage, no unresolved required finding, and preserved evidence for every changed route on the closing tree. It is not a claim that arbitrary future scrutiny could never find another defect.

Every source-backed defect within a sweep's stated obligations is required work. Severity labels, a new owner or a later audit cannot remove that burden. Source review must establish a causal reduction: the repaired owner supplies the needed datum, its real consumer uses it, and the former bypass is no longer needed there. More policies, lower scan counts or a passing specimen alone do not establish that change.

Repeated failure of the same equation or recurrence of the same bypass stops leaf patching: repair the shared cause and review the sibling routes that used it. If the necessary maintained operation or authority cannot be obtained, leave the exact obligation open, report its missing input and continue independent ready work. Do not claim convergence, reduce the domain or invent a local replacement to force closure. New functionality unrelated to these obligations remains outside this convergence pass.

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

Select a node with no remaining prerequisites, subject to the existing geometry priority. Apply `DEV-61` to foreign edits or reservations; do not create a claim layer.
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

Before committing a queue change, check that every checkbox has exactly one ID and one Needs list, IDs are unique, all references resolve, and there is no self-edge or cycle. Required pre-T implementation nodes must feed `architecture-remediation` and the terminal chain that verifies them. Once T begins, newly exposed repairs feed the still-open terminal or post-T node that found them, whose acceptance includes re-execution of affected proof. Do not resurrect closed phase nodes or restart the source-phase execution suspension.
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

A wrong answer outranks every failure that raises: a false value is trusted, a raised error is not. Paths below are relative to `src/dzack_research/preamble/` unless a different root is given.

## Foundations blocking many consumers

Each of these fails a whole population of constructions or tests; closing one unblocks many.

- [ ] **`framed-axiom-retired`**. **Needs:** none.
  **Owner and delta:** the global `Framed` axiom (`objects.py`, registered in `all_axioms`) and its consumers, per `CAT-29`. The population is read by `rg '\.Framed\(\)|FramedModules|FramedAlgebras|FramedFreeModules|_with_axiom\("Framed"\)|class Framed\(' src/dzack_research/preamble` (52 files, 246 lines on 2026-09-25). Chosen generating sets and presentations become chosen truncations in the shared resolution category; the per-owner framing registry (`_selected_framing_registry`, `_fix_selected_framing`) becomes the store of those chosen truncations; `is_framed_algebra()` and every read of `_algebra_framing_owner` ask the resolution category instead of an attribute; `ModulesWithChosenFinitePresentation`, `GroupsWithChosenFinitePresentation` and `AlgebrasWithChosenFinitePresentation` become fibres of the truncation-1 resolutions. `FramedFreeModules(R)` (free modules with a chosen basis) is the length-0 case and stays, as the framed modules. No category declares `Framed` afterwards.
  **Closure:** the `rg` above matches only `FramedFreeModules` and its consumers; `Algebras(R).Associative().Unital().Framed()` no longer exists; the selected-framing consumers (algebra generators, presentation display, module generators, matrix units of `End_R(F)`) run through the resolution category.

- [ ] **`integers-coerce-into-rationals-and-reals`**. **Needs:** `framed-axiom-retired`.
  **Owner and delta:** coercion of the session integers into `QQ` and the owned reals `RR`. Sage builds the coercion Hom in the meet of the two categories, and with a global `Framed` axiom that meet contains framed categories that one side is not placed in: on `main` and rack's head `72650e04f`, `RR.coerce_map_from(ZZ)` raises `ValueError: Integer Ring is not in Join of ... associative unital framed algebras ...`. Giving `ZZ` its empty algebra framing moves the failure to `QQ.coerce_map_from(ZZ)` (the meet then puts `Framed` on `Modules(ZZ)`). A meet computed as the intersection of declared supercategories gives the right categories but types the Hom as the owned ring Mor, whose `homset_category()` is Sage's `Sets()`, and Sage rebuilds a weakened coercion map's parent there; owned objects are not in Sage's `Sets()` (owned `Sets` declares `Objects()` only, contrary to the `owned_category.py` module docstring).
  **Closure:** `RR.coerce_map_from(ZZ)` and `QQ.coerce_map_from(ZZ)` exist; `4 / pi**2` evaluates in a session; `tests/functions/test_young_convolution.sage` collects; `tests/lattices/test_d4_metric_invariants.sage::test_d4_successive_minima_hermite_invariant_and_gaussian_heuristic` and the three `tests/functions` Lebesgue tests pass.

- [ ] **`forms-are-covariant-tensors`**. **Needs:** none.
  **Owner and delta:** `categories/forms/forms.py` (the evaluation at line 331) and `tensors/tensor.py`. A bilinear form `b: M x M -> W` is a covariant 2-tensor on `M`, type `(0, 2)`, so it takes two vectors. The form evaluation builds or receives a type-`(2, 0)` tensor and then applies it to two vectors, which raises `TypeError: a type-(2, 0) tensor has only 0 covariant slots, got 2 arguments`. The same error is raised whether or not the owned categories over `ZZ` are pre-created at import.
  **Closure:** `Lattices(ZZ)("A2").discriminant_group()` is the cyclic group of order 3 with `q = 2/3 mod 2`; the discriminant-group rows in `tests/constructions/test_lattices_construct.sage` and `tests/modules/test_invariant_factor_framing.sage` run past form evaluation.

- [ ] **`triage-session-integer-identity`**. **Needs:** none.
  **Site:** raw Sage integers and rationals returned where owned ones belong, and session integers handed to Sage unlowered.  The session's integers are owned; Sage neither contains nor converts them (TRAPS.md), and the owned rings refuse Sage's.  Observed leaks: `n_vertices()` of a polygon returns a raw Sage integer, so `cell.n_vertices() == 4` is False; the nested-literal Gram route passes a raw Sage `1` into the owned ring; `schlaflian()`, the `*_inertia_index()` methods, `exceptional_self_intersection()` and `del_pezzo_degree()` return engine numbers; `GF(7)(3).multiplicative_order()` and `Groups.Heisenberg(1, 3)` fail on owned integers.  Repair each at its crossing: lower with `_engine_element`, raise with `_owned_engine_element`.
  **Example:** `tests/lattices/test_rational_polyhedral_cells.sage::test_square_voronoi_cell_retains_facets_incidence_and_stabilizers`; `tests/rings/test_elementary_arithmetic_of_owned_rings.sage::test_three_is_a_primitive_root_modulo_seven`.

- [ ] **`triage-mor-sets-and-groups-are-sets`**. **Needs:** none.
  **Site:** `categories/sets/set_categories.py`, `SetMorCategory`: `Sets().Mor(X, Y)` is placed in Sage's "endsets of sets" category, not in the owned `Sets()`, so it has no cardinality and is refused wherever a set is required ("a map of sets needs a set as domain"; `group/g_objects.py`, `action_functor`).  ARC-07 makes `Mor(X, Y)` a category and a set the discrete one, so `Mor_Set(X, Y)` is the set `Y^X`; the tree also owns `Y^X` as `FunctionSets`, whose `mor()` returns this homset.  There is exactly one such category, the essential image of `Mor: Set^op x Set -> Set`; two classes realizing it is an architectural incoherence (owner ruling 2026-09-25), so they are unified into one, whose objects are the `Mor_Set(X, Y)` and which is a subcategory of `Sets()`.  Blocks every `FiniteGSets(G)(points, action)`, every `AffineGSchemes` action, descent equalizers and naturality squares.
  **Example:** `tests/schemes/test_glued_invariant_quotients_of_glued_lines.sage::test_negation_is_an_involution_of_the_line`.

- [ ] **`mor-construction-computes-no-presentation`**. **Needs:** none.
  **Site:** `categories/modules/module_morphisms/module_morphisms.py`, `_initialize_module_mor_parent`: a Mor between presented modules computes its presented internal-Hom model and fixes its framing and presentation when it is constructed.  `OWN-22` (owner ruling 2026-09-25): constructing `Mor_C(X, Y)` fixes its endpoints and composition and computes no presentation; the model is realized when a module operation asks for it (`OWN-23`).  After the End algebra stopped building its multiplication eagerly, `End(Z/2 + Z^2)` costs 0.34 s, all of it this model.

- [ ] **`ordinals-form-a-category`**. **Needs:** none.
  **Site:** `categories/sets/cardinals.py`, `Ordinals()`, and `categories/sets/set_categories.py`, `FiniteOrdinalSets`.  Cardinals are objects of a thin category (`Cardinalities`); ordinals are only elements of one semiring object `Ordinals()`, so there is no category of ordinals, and `order_type()` on `[n]` is a method returning such an element, not a functor.  `FiniteOrdinalSets` holds the standard finite linear orders `[n]`, whose category with order-preserving maps is the (augmented) simplex category, a skeleton of the finite linear orders (Mathlib `SimplexCategory`, a skeleton of `NonemptyFinLinOrd`); it is not a category of ordinals.  Prior art defines an ordinal as the order-isomorphism class of a well-ordered set (Mathlib `Ordinal := Quotient Ordinal.isEquivalent` on `WellOrder`; nLab, *ordinal number*), and the class of ordinals as well ordered by initial-segment embedding.  Owed: `Ord`, the thin category of ordinals, whose semiring operations are operations on its objects as `Cardinalities`' are; the order type as a functor from well-ordered sets and their isomorphisms to `Ord`; `[n]` named for what it is.  The design is an owner decision (raised 2026-09-25).

- [ ] **`natural-numbers-meet-integers`**. **Needs:** none.
  **Site:** `categories/sets/set_categories.py`, `NaturalNumberSets`: it declares `AdditiveMonoids()`, `Sets().Infinite()` and `EnumeratedSets()`, yet `NN.category()` is not a subcategory of `NN.category()._meet_(ZZ.category())`, "infinite countable additive monoids", so no coercion `NN -> ZZ` can be built (Sage's homset asserts both endpoints lie in the meet). The canonical semiring map from the initial semiring `N` into every unital ring is therefore absent, and an `NN` element compares with an owned integer only through `NN`'s own element methods.
  **Example:** `NN(2) + ZZ(3)` in a session.

- [ ] **`triage-parent-init-keywords`**. **Needs:** none.
  **Site:** `sage/structure/parent.pyx:238`: construction data reaching `Parent.__init__` unconsumed: `power_source` (195) and `concentrated_degree` (83); the level that declares each datum is not in the constructed object's chain.
  **Example:** `tests/schemes/test_scheme_category_archive.sage::test_projective_plane_has_picard_and_class_group_z_generated_by_a_line`.

- [ ] **`triage-augmentation-retained`**. **Needs:** none.
  **Site:** `categories/algebras/augmented_algebras.py:84`: "an augmented algebra retains its selected augmentation morphism" (136).
  **Example:** `tests/algebras/test_group_algebra_functor_archive.sage::test_underlying_module_of_group_algebra_is_the_literal_functor_composite`.

## Test suite: specimens, speed and coverage

The suite is the instrument that finds the rest; these make it fast and complete.

- [ ] **`small-specimen-tests`**. **Needs:** none.
  **Owner and delta:** tests exercise every path nontrivially on the smallest specimen that separates the claim; a large lattice or scheme appears only when the claim is about that object, and then through an invariant that does not enumerate it (owner, 2026-09-25).  Measured on the 2026-09-24 coverage run: `tests/lattices/test_lattice_catalogue_constructors_archive.sage::test_leech_lattice_uses_the_rootless_even_unimodular_archive_contract` 225 s, `tests/objects/test_k3_lattice.sage::test_an_embedded_hyperbolic_plane_splits_off` 152 s, `tests/lattices/test_k3_even_unimodular_uniqueness_archive.sage::test_k3_lattice_is_the_even_unimodular_signature_3_19_model` 112 s, `tests/lattices/test_nikulin_classification.sage::test_each_hyperbolic_type_is_realised[r18-a0-d0]` 60 s, `tests/schemes/test_toric_blowups.sage::test_archived_three_step_projective_plane_blowup_chain_has_del_pezzo_degrees_8_7_6` 50 s.
  **Closure:** each such claim is either restated on a small specimen (`U`, `A_2`, `U + U`, `P^2`) or, when it is about the large object, checked by an invariant such as the minimum or the discriminant form; no test over its per-test limit.

- [ ] **`suite-within-time-gates`**. **Needs:** `mor-construction-computes-no-presentation`, `small-specimen-tests`.
  **Owner and delta:** the suite passes its gates in `dzack_research.utilities.suite_budget`: star import 2 s after `sage.all`, collection 30 s, execution 100 ms per selected test, no test over its per-test limit.
  **Observed:** the catalogue executed in about 6.5 minutes, 24 ms per test; with tracebacks on, formatting failure reports dominates because owned `_repr_` methods compute (a ring's repr computes its cardinality). 16 tests exceeded 1 s.  Measured 2026-09-25: each process that reaches the Julia bridge pays about 20 s to start Julia and load Oscar (compile cache warm), and `test_centralizer_discriminant_image_of_the_swap_on_a1_plus_a1` spends 72 s in one call; the tests on large lattices are `small-specimen-tests`. pytest-timeout's `SIGALRM` inside Cython code is caught by cysignals as `AlarmInterrupt`, which stops the run.
  **Observed after the rack reconciliation (2026-09-25, single process, --timeout=600):** the enumerating lattice specimens slowed. Pre-merge `1e1a69be2` against merged `d14a3878f`: `test_equivariant_vector_orbits.sage::test_representatives_are_the_same_live_orbit_package` 113 s → 145 s; `test_centralizer_gluing.sage::test_the_a2_centralizer_splits_the_single_root_orbit_in_two` 79 s → 99 s; `::test_the_a2_centralizer_separates_two_roots_that_o_a2_identifies` 29 s → 58 s; `test_cyclotomic_centralizer.sage::test_the_centralizer_of_minus_one_on_Z3_is_the_signed_permutation_group_of_order_48` 55 s → 58 s. Each builds one isometry per group element through module Mor membership tests; the cyclotomic profile had category `__contains__` at 57 of 120 profiled seconds before `d14a3878f`.
  **Closure:** the default suite run is green on all four gates, with no gate raised.

- [ ] **`session-star-import-lint`**. **Needs:** none.
  **Site:** `src/dzack_research/utilities/test_lint.py`.  Its standard is that every name comes from `from dzack_research.preamble.all import *`, but it accepts an explicit import from that module, under which a `.sage` file's literals are Sage's raw integers.  Add the rule once dzackgarza/tree-sitter-sage#8 stops the research preparser from rewriting `X = Y[name]` for star-imported names; then convert `tests/sets/test_cardinality_construction_comparisons.sage` and `tests/sets/test_power_set_archive_known_math.sage`.  Three locked files keep explicit imports until an owner unlocks them: `tests/constructions/test_direct_sum_objects_archive.sage`, `test_slice_coslice_archive.sage`, `test_products_archive_reconciliation.sage`.

- [ ] **`category-method-coverage-sweep`**. **Needs:** `triage-session-integer-identity`, `triage-mor-sets-and-groups-are-sets`, `mor-construction-computes-no-presentation`, `triage-parent-init-keywords`, `triage-augmentation-retained`.
  **Owner and delta:** for every category in the live session, construct its objects on small specimens and call every public method of the object, its elements and its morphisms, asserting the mathematical value (owner, 2026-09-24).  The categories and operations come from a regenerated `just preamble-megadoc` survey; one test file per category, written to `tests/constructions/CONTRIBUTING.md`'s session standard.
  **Closure:** every category of the survey has its file, and `just coverage-report` shows no public method of the preamble that no passing test calls, other than those whose failure is a recorded node.

## Runtime triage catalogue

The first full execution of the suite since the tree stopped importing (2026-09-07), run once as a triage catalogue on 2026-09-23 with `--no-time-gates --timeout=1 -o timeout_func_only=true` (16,311 tests collected): 11,874 failed, 4,335 passed. Failures are grouped here by the site that raises them; paths are relative to `src/dzack_research/preamble/` unless a different root is given. A node's cause is the defect behind its site, which the node establishes; the site and example are where to start. Each node closes when its example passes and a re-run of the catalogue shows no failure raised at its site. Regenerate the catalogue with the same command; the time gates are on by default.

- [ ] **`triage-native-module-additive-group`**. **Needs:** none.
  **Site:** `categories/modules/native_modules.py:102` and `:103`, `_RingModulePresentation.construct`: "the action is on the supplied owned additive group" (1,924) and "native scalar structure cannot overwrite another chosen base" (185).
  **Example:** `tests/algebras/test_module_structure.sage::test_forgetful_functor_sends_an_algebra_to_its_underlying_module`; `tests/rings/test_local_base_maximal_ideals.sage::test_dual_numbers_over_a_field_are_local_at_the_nilpotent_alone`.

- [ ] **`triage-framing-source-base-ring`**. **Needs:** none.
  **Site:** `categories/modules/pure/modules.py:3051`, `_fix_selected_module_framing`: "the selected framing source is a free module over this module's base ring" (1,571).
  **Example:** `tests/divisors/test_divisor_node_specimens.sage::test_normal_singular_surface_has_a_noncartier_weil_class`.

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
  **Site:** `categories/rings/ring_foundation.py:2163`, `OwnedRings.ParentMethods.cardinality`: the exact computation covers only finite, countably infinite and uncountable placements (348).
  **Example:** `tests/algebras/test_affine_semigroup_algebras.sage::test_affine_semigroup_algebra_retains_its_selected_binomial_presentation`.

- [ ] **`triage-module-mor-endpoints`**. **Needs:** none.
  **Site:** `categories/modules/pure/modules.py:904`, `Modules.Mor`: "an R-module Mor requires two R-modules" (338).
  **Example:** `tests/algebras/test_de_rham.sage::test_relative_conormal_and_tangent_comparison_for_xy_equals_t`.

- [ ] **`triage-subring-base`**. **Needs:** none.
  **Site:** `sage/categories/rings.py:1705`: "base must be a subring of this ring" (177), raised by Sage when an owned construction passes a base that Sage does not recognize as a subring.
  **Example:** `tests/sets/test_standard_cardinals_archive.sage::test_matrix_ring_cardinality_tracks_the_coefficient_ring`.

- [ ] **`triage-an-element`**. **Needs:** none.
  **Site:** `sage/structure/parent.pyx:2847`: `please implement _an_element_` for join-category, product and coproduct parents (158 + 37 + 23).
  **Example:** `tests/functions/test_lebesgue_quotient.sage::test_quotient_keeps_a_nonzero_function_and_does_not_sample_callable_equality`.

- [ ] **`triage-category-c3-keys`**. **Needs:** none.
  **Site:** `sage/misc/c3_controlled.pyx:945`: `KeyError` on a category sort key while Sage linearizes super categories (143 + 49); a category is joined whose comparison key is not registered.
  **Example:** `tests/algebras/test_cartan_calculus.sage::test_vector_fields_are_derivations_and_have_the_expected_lie_bracket`.

- [ ] **`triage-construction-contract`**. **Needs:** none.
  **Site:** `owned_category.py:802`, the construction-contract check: invertible-sheaf categories on join-category schemes (138).
  **Example:** none current: the cited test was removed in b9b95babe, and `O(d)` on `P^n` no longer raises here (88d2dc923).  Find an invertible sheaf on a join-category scheme that still raises at this site before working the node, or remove the node with that evidence.

- [ ] **`triage-selected-framing-at-construction`**. **Needs:** none.
  **Site:** `categories/abstract_categories/objects.py:264`: polynomial rings "constructed without" their selected framing (126).
  **Example:** `tests/algebras/test_relative_presentations.sage::test_zero_relation_presentation_lifts_through_the_identity_engine`.

- [ ] **`triage-indexed-cardinal-finiteness`**. **Needs:** none.
  **Site:** `categories/sets/cardinals.py:478`: "finiteness is not selected for an arbitrary indexed cardinal family" (108).
  **Example:** `tests/algebras/test_center_corestriction_archive.sage::test_exterior_algebra_center_is_the_archived_predicate_subring`.

- [ ] **`triage-discriminant-over-general-rings`**. **Needs:** none.
  **Site:** `categories/lattices.py:2222`: "discriminant_group is the ZZ specialization; use discriminant_module" (106), reached by `DiscriminantBilinearModules` over rings other than `ZZ`.
  **Example:** `tests/constructions/test_categories_inhabited.sage::test_a_category_over_a_ring_is_inhabited_over_every_ring[AA-DiscriminantBilinearModules]`.

- [ ] **`triage-toric-charts-over-fields`**. **Needs:** none.
  **Site:** `categories/schemes/toric/toric_schemes.py:1907`: "the semigroup algebras of the charts are algebras over a field" (100), reached by toric categories over non-fields.
  **Example:** `tests/constructions/test_categories_inhabited.sage::test_a_category_over_a_ring_is_inhabited_over_every_ring[GF(5)[t]-ADELogPairs]`.

- [ ] **`triage-missing-owned-operations`**. **Needs:** none.
  **Site:** `sage/cpython/getattr.pyx:357`/`:362`: `AttributeError` for operations the owned objects do not have: on module Mor elements (99 + 37), sparse free module object types (83), `DistinguishedAffineCovers.subcategory_class` (92), and the `mor`, `point_mor`, `nilradical`, `free_bilinear_form_adjunction` and `cardinality` names that the specifications call.
  **Example:** `tests/algebras/test_algebra_base_change_archive.sage::test_scalar_restriction_retains_the_selected_ring_map_identity`.

- [ ] **`triage-signature-over-ordered-fields`**. **Needs:** none.
  **Site:** `categories/_lattice.py:1296`: the signature pair asserted for quadratic spaces whose base is not a subfield of the reals (78).
  **Example:** `tests/constructions/test_categories_inhabited.sage::test_a_category_over_a_ring_is_inhabited_over_every_ring[AA-HyperbolicLattices]`.

- [ ] **`triage-kahler-backend`**. **Needs:** none.
  **Site:** `categories/algebras/derivations.py:61`: "the represented Kähler-calculus backend requires a symmetric algebra or a chosen finite commutative presentation" (74).
  **Example:** `tests/constructions/test_algebras_construct.sage::test_kahler_differentials_of_a_ring_over_itself_vanish[AA]`.

- [ ] **`closed-immersion-citation`**. **Needs:** none.
  **Site:** `categories/schemes/schemes.py`, `is_closed_immersion`, cites Stacks Tag 01HV, which is Lemma 26.5.4 (sections of `M~` on `Spec R`). Cite the Stacks result that a morphism of affine schemes is a closed immersion exactly when its ring map is surjective, after opening it.

- [ ] **`triage-long-tail`**. **Needs:** none.
  **Site:** the remaining 699 sites of the catalogue, together about 2,200 failures, among them `categories/rings/commutative_ideals.py:946` (59), `categories/group/g_sets.py:167` (54), `categories/modules/pure/modules.py:4681` (53), `categories/modules/framed/fraction_field_quotients.py:123` (50), `sage/matrix/matrix_gfpn_dense.pyx:429` (`GF(27)` in MeatAxe, 36), and 27 specification tests calling `Hom`, which the session does not export under `Mor` as its only spelling.
  Also: deciding whether an endomorphism of a free module lies in the image of the zero module's Mor (`module_morphisms.py:1139`, "cannot decide whether ... is in the image"), reached by the centre of a unital associative algebra (`tests/algebras/test_algebra_preservation.sage`).
  **Closure:** a re-run of the catalogue with no failure at these sites; split any site whose cause is shared by others into its own node first.

## Forms, actions and arithmetic realizations

- [ ] **`dual-lattice-through-the-discriminant-sequence`**. **Needs:** none.
  **Owner and delta:** for an `R`-lattice `L` with form `b` valued in `K = Frac(R)` and an `R`-submodule `S <= K`, `L^# = {x in V : b(x, L) <= O}` for `V = L_K = L tensor_R K`, and `L` is `A`-modular for a fractional ideal `A` when `A L^# = L`, unimodular when `A = O` (Kirschmer, *Definite quadratic and hermitian forms with small class number*, Def. 2.3.3; arXiv:1904.04518, Def. 2.1). For invertible `A`, `A L^# = {x in V : b(x, L) <= A}`, so `A`-modularity says this `A`-dual of `L` is `L`. Kirschmer's `L^A = {x in L : b(x, L) <= A}` (same Def., item 8) is the sub-bilinear module of `L` cut out by the same condition. The maps are `L -> L^#` when `b(L, L) <= O`, with cokernel `A_L`, and `L^# -> L^* = Hom_R(L, R)`, `x |-> b(x, -)`. The form on `L^*` is transported along that map. `Lattices.dual_lattice` (`categories/lattices.py`) instead equips the dual module with a `QQ`-valued form and refines it into `FormModules(ZZ).Nondegenerate()`, whose predicate asks for a correlation `M -> Hom_R(M, R)` (`categories/modules/hodge.py`, `_algebraic_correlation_morphism`) defined only for `W = R`.
  **Invariants:** the left and right radicals are the kernels of the two curried maps `L -> Hom_R(L, W)`, `x |-> b(x, -)` and `y |-> b(-, y)`, from `b: L tensor_R L -> W` by tensor-hom adjunction, for every value module `W`; nondegeneracy is that both radicals are zero. The `W = R` case is recovered, not special-cased.
  **Closure specimens:** `NamedLattices.TdP.dual_lattice()` returns `L^*` with its transported form and the map `L -> L^*`; `A_1` has `A_L = ZZ/2`; the form with Gram matrix `[[1,1],[1,1]]` on `ZZ^2` has a radical of rank one.

## Common categorical authority and public boundaries

- [ ] **`group-categories-defined-by-data`**. **Needs:** none.
  **Owner and delta:** `categories/group/groups.py`. The groups whose category is fixed by mathematical data, per `CAT-28`: `SymmetricGroups()(Omega)` for a set `Omega`, `GeneralLinearGroups()(R, n)`, `FreeGroupQuotients()(F, R)` (a free group and a set of relators), `CoxeterGroups()(M)` for a Coxeter matrix, and an `Arithmetic` axiom on `OwnedGroups`. Each is built from main's current `groups.py`, with its morphisms and its `CAT-22` owner search. `remediate/groups` (`bbce862e3`, deleted 2026-09-25) drafted these, and complaint 10 in `COMPLAINTS.md` records why that draft was rejected: it replaced working catalogue entries with assertions, and it gave a number field the automorphism group of the original field as its Galois group.
  **Closure:** `SymmetricGroups()(Sets.Delta[2])` has order 6; `GeneralLinearGroups()(GF(2), 2)` has order 6 and is isomorphic to it; `FreeGroupQuotients()(F_2, {a^2, b^3, (ab)^2})` has order 6; `CoxeterGroups()` of the `A_2` matrix is that same group; the arithmetic axiom holds for `SL_2(ZZ)`.

- [ ] **`engine-wiring-audit`**. **Needs:** none.
  **Owner and delta:** every owned construction that computes, itself, behaviour a maintained engine provides, starting with the set layer (`categories/sets/`): membership, position and order of finite sets, images, products, coproducts, power sets and function sets, as tabulated in [COMPLAINTS.md](COMPLAINTS.md#set-theoretic-behaviour-is-re-implemented-instead-of-wired-to-a-set-engine), then the whole preamble.
  **Invariants:** public mathematics stays owned; the computation behind it is the engine's, reached privately at its owner (`OWN-06`). A membership decision follows the set's definition -- predicate, identity of listed points, inverse of an image -- and never searches an enumeration. An enumeration is a chosen bijection from an ordinal, separate from membership. No owned code re-implements what Sage, GAP, SymPy, PARI or the Python standard library computes, unless the engine lacks it, which is then recorded in `TRAPS.md` with the measurement.
  **Coverage:** survey the preamble once for owned code whose body is a general algorithm -- loops that search, compare element by element, enumerate to decide, or rebuild an object to read one value -- and map each to the engine routine that computes it or to the recorded reason there is none. The profiled sites of 2026-09-23 are the first evidence, not the population.
  **Closure specimens:** membership of a point in a finite set of SR symbols, an image, a product and a power set answered without comparing against every point; a rank-16 diagonal lattice built in time linear in its Gram entries; each audited family's route read from its public entry to the engine call.
## Public mathematical interaction

## Source convergence and terminal proof

- [ ] **`architecture-remediation`**. **Needs:** `engine-wiring-audit`, `dual-lattice-through-the-discriminant-sequence`.
  **Owner and delta:** the integrated source route from public category entry through complete defining data, private computation and every owned result and consumer, against all unresolved complaints.
  **Invariants:** every required source descendant closes before this node; introducing a residual child keeps this node open. Each complaint's entire burden is discharged or retained in a required prerequisite. All alternative construction routes affected by a repair are inspected. No numerical answer, renamed field, new wrapper, source count or administrative record substitutes for delivery (`DEV-67`, `DEV-68`).
  **Closure comparison:** reconcile the original complaint/requirement clauses with the delivered owner and consumer routes, including the generality beyond their first specimens. Review later changes to each shared contract against its delivery evidence. In particular, an "assumed linear" rename, a framing proof depending on its own Mor placement, or a private access deferred from a delivered producer fails this comparison and reopens that exact repair. Existing evidence for unaffected routes remains usable.
  **Closure evidence:** bank falsifying specimens for every repaired obligation, including inherited operations, wrong nearby inputs and relevant infinite/nonfree/base-change cases. Commits record source coverage and unexecuted proof. Review composed consumers after their prerequisites, without rerunning an unrelated whole-tree inventory after every leaf. Source closure authorizes T; it does not claim runtime success.

- [ ] **`function-spaces-are-subobjects-of-mor`**. **Needs:** `triage-mor-sets-and-groups-are-sets`.
  **Owner and delta:** the owned function spaces (`categories/functions/real_functions.py`), under `CON-17`. Each space is a family of functors in both arguments, and its constructor takes both: `C(n, A, B)`, `Lp(p, A, B)`, `ell(p, A, B)`; the tests now construct `C(Infinity, RR, RR)`, `Lp(2, RR, RR)` and `ell(2, NN, RR)`. Coordinates are owned by the domain: `RR.coordinate()` is the coordinate of ℝ (for ℝ² it is the pair (x = (x_0, x_1))), and a map is built from it, `C(Infinity, RR, RR)(x^2 + 1)`. `Lp(p)` (maps ℝ → ℝ) is built with `indeterminate=SR.var("x")` and `ell(p)` (maps ℕ → ℝ) with `SR.var("n")`; each stores the variable, hands it out as `indeterminate()`, and reads `space(expr)` as the map t ↦ expr. The delta: each space is the subobject of `Sets().Mor(X, Y)` cut out by its condition (integrability, summability, smoothness, boundedness), with its module structure; element construction is `Mor(X, Y)`'s element constructor (callables, formulas binding their own variable, finitary data), and the space admits the element by its condition; `indeterminate()` and the stored variable are removed, together with their consumers: `convolution.py` and `lebesgue_quotients.py` substitute into `parent().indeterminate()`, and `modules/pure/function_modules.py:378` defaults a formula's variable to `x`. Each works on the map it is given.
  **Observed:** the formulas are Sage symbolic expressions in the stored variable, and owned numbers never enter Sage's symbolic ring (`AGENTS.md`, ruled 2026-09-23), so `x**2`, `2 ** (-n)` and `1 / (1 + x**2)` raise `TypeError` in `tests/functions/test_function_modules_archive.sage`, `test_real_functions.sage` and `test_young_convolution.sage`. Those tests use `indeterminate()` and are rewritten with the delivery to define their maps (`f(t) = exp(-t^2)`).
  **Closure:** the maps t ↦ t², t ↦ 1/(1 + t²), t ↦ exp(−t²) and k ↦ 2⁻ᵏ, each defined with its own variable, are constructed in `Mor(X, Y)` and admitted by their spaces; no space supplies a point of its domain, and `X.coordinate()` of a function space, where it exists, is a general element of that space.

- [ ] **`terminal-session`**. **Needs:** `architecture-remediation`, `forms-are-covariant-tensors`, `group-categories-defined-by-data`, `branches-absorbed-into-main`, `integers-coerce-into-rationals-and-reals`, `triage-native-module-additive-group`, `triage-framing-source-base-ring`, `triage-subobject-base-placement`, `triage-an-object-contracts`, `triage-owned-ring-custom-name`, `triage-ring-cardinality-frontier`, `triage-module-mor-endpoints`, `triage-parent-init-keywords`, `triage-subring-base`, `triage-an-element`, `triage-category-c3-keys`, `triage-construction-contract`, `triage-augmentation-retained`, `triage-selected-framing-at-construction`, `triage-indexed-cardinal-finiteness`, `triage-discriminant-over-general-rings`, `triage-toric-charts-over-fields`, `triage-missing-owned-operations`, `triage-signature-over-ordered-fields`, `triage-kahler-backend`, `triage-session-integer-identity`, `session-star-import-lint`, `natural-numbers-meet-integers`, `triage-mor-sets-and-groups-are-sets`, `mor-construction-computes-no-presentation`, `ordinals-form-a-category`, `closed-immersion-citation`, `triage-long-tail`, `suite-within-time-gates`, `small-specimen-tests`, `category-method-coverage-sweep`, `function-spaces-are-subobjects-of-mor`.
  **Owner and delta:** execute the integrated mathematical proof burden on the final owned session and research notebook; `DEV-58` governs this transition.
  **Invariants:** a fresh process imports `from dzack_research.preamble.all import *` and exposes Cat and Lattices. This is a prerequisite, not mathematical acceptance. Regenerate `docs/preamble-megadoc.md` and the graph through `just preamble-megadoc`; inspect their agreement with live categories, operations, domains and codomains. Preamble warnings and order-dependent imports require repair.
  **Closure evidence:** execute all required banked construction specimens and the protected expectation/user-simulation obligations through the prescribed project recipes, classify actual failures at their owners and repair them without weakening expectations. Cover direct, convenience, functor, catalogue and engine-raised routes; free/nonfree, finite/infinite and changed-base regimes where claimed. A previous run certifies only the source it exercised.
  Use japi for notebook execution and inspect actual rendered mathematical outputs; source, saved files and successful imports do not prove rendering or mathematical claims. Run the prescribed final QC at its applicable boundary, retaining explicit evidence for any remaining failures. A required failure keeps this node open; fixes and focused re-execution stay within T rather than restarting the architecture suspension. Respect push authorization.

## Post-remediation convergence

- [ ] **`branches-absorbed-into-main`**. **Needs:** none.
  **Owner and delta:** every local branch on this workstation and on `rack` that `main` does not contain: 17 here (`git branch --no-merged main`; newest the `remediate/*` branches of 2026-09-17, whose worktrees sit under a scratch directory) and 8 on `rack` (newest `steward/preamble-rescue-2026-09-09`). Each is read once. Work that `main` lacks is merged or re-expressed on `main`, and rejected work is recorded at its complaint owner. Then the branch and its worktree are deleted, as the `remote-remediation-branches` objective did for the `origin/remediate/*` branches.
  **Closure:** `git branch --no-merged main` is empty on both hosts, and no worktree outside the main checkout remains.

- [ ] **`refactor-audit`**. **Needs:** `terminal-session`.
  **Goal:** After the repaired mathematics runs end-to-end, audit the repository for duplicated authority, poor organization, and maintainability defects that survived the architecture work.
  Audit the whole repository for messy, disorganized or duplicated code after the complaint-derived architecture has been exercised through the final public session.
  The public mathematical API need not change and should not change incidentally; this pass is about internal sources of truth, ownership and maintainability that survive the mandatory architecture repairs.

  Fix the whole-repository source population at entry and cover it once for organization, sources of truth, ownership and duplication. Inspect the authored owners of generated projections and any participating local changes; preserve unrelated foreign work. Review concrete declarations and consumers, not only search matches. Apply the bounded-closure rule above: a repair revisits its changed route and affected uses, without restarting the repository survey.

  Repair a bounded finding at its owner. If it crosses independent owners, give its concrete repair a DAG row with source-backed acceptance and make this node depend on it. Re-execute affected proof in the active terminal phase. Newly observed required findings are repaired by the same rule; they do not initiate another general audit. Do not create rows whose deliverable is only a report, inventory, approval or proof that the audit ran.

  **Acceptance:** the stated whole-repository coverage is complete, every resulting required finding is repaired, and the changed routes and their consumers have been reviewed and re-exercised on the closing tree. Unchanged, unaffected coverage carries forward; no second whole-repository discovery pass is required. Record the inspected coverage and residual uncertainty without claiming that no future defect can exist. A clean pass requires no receipt commit.

- [ ] **`type-paydown`**. **Needs:** `refactor-audit`.
  **Goal:** Improve static type information only where it clarifies the mathematics and makes correctness easier to reason about; do not contort code merely to lower an error count.
  Pay down type errors where doing so is reasonable, and not one step further.
  **Acceptance:** inspect the diagnostics from the prescribed typing boundary once, resolve their shared causes at the mathematical or typing owner, and give every retained diagnostic an evidence-backed disposition there. Check changed declarations and affected uses after each coherent repair; broaden only for a demonstrated new effect. No required behavior or proof is bypassed. Re-execute affected mathematical specimens after behavioral changes under the already-active terminal phase. Every typing decision must improve the legibility of the code, the ability to understand what it does, and the ability to reason statically about whether it is correct. That is the standard the change is judged against, not the error count. A retained false positive needs source-backed justification; a missing mathematical contract remains required work.

  Golfing the code into oblivion -- distortions that exist only to silence a checker -- is the failure mode.  Where a contortion is genuinely warranted, it must be judged as significantly serving the goal above, and the argument for it recorded explicitly in the commit message.  A type annotation nobody can read has made the code worse even when the checker is quieter.

- [ ] **`bloat-audit-loop`**. **Needs:** `type-paydown`.
  The legacy identifier is retained for stable references, but this is a finite terminal convergence pass, not a permanently open audit loop.
  Read the governing `AGENTS.md`, `CONTRIBUTING.md` and this DAG at entry. Use `policy-index` to select the review skill for the actual boundary, and load narrower skills only for findings that need them. Loading another skill supplies a method for the stated obligations; it does not create another workstream, proof requirement or repository-wide round.

  Fix the source population at the post-typing tree. Cover categorical/math owner placement; duplicate or derivable retained state; public type/API design; tests as behavioral proofs rather than implementation mirrors; dead compatibility bridges and validation-evasion fallbacks; dependency offload to Sage, GAP/CAP, OSCAR, SymPy, Python or another mature owner; import/lazy-import and module-cycle structure; notebook/session usability; generated/static projection boundaries; and AI-slop or locally tidy code that violates the architectural contract. Reuse the preceding audit's coverage for overlapping questions only where the route and its dependencies remain unchanged; complete the other questions across the whole repository once. Protected mathematical expectations retain their own correction rule.
  Search the dependency or upstream owner before improving a local mechanism that may not need to exist.

  Repair a small, well-supported finding and commit the behavioral regression or mathematical consumer that proves it. If a finding spans several owners, add a concrete repair row with the necessary edges; this node cannot close until that repair closes. Revisit the repaired route, affected callers and evidence. A repeated finding with the same cause requires shared-owner repair and review of its sibling uses, not another whole-tree search. Never create a node merely to say that an audit ran, and never leave a required finding in COMPLAINTS as a substitute for repair.

  **Acceptance:** every stated question has complete coverage, every resulting required finding has been repaired, and each subsequent change has its affected source and proof revalidated on the closing tree. Re-execute affected mathematical proof after repairs and confirm the final public session after bootstrap/export changes. Stop at that condition; there is no repeat-until-empty whole-repository discovery step. A clean pass makes no receipt commit. Later regressions are new owner-local defects and do not retroactively turn this completed convergence pass into a perpetual queue.

## Optional research consumers

These are not prerequisites for the required mathematics, complaint remediation, terminal verification, or convergence audits.

- [ ] **`optional-framed-manifolds`**. **Needs:** `terminal-session`, `optional-manifold-tangent-bundles`.
  **Goal:** the framed manifolds of `CAT-29`: a smooth manifold with a length-0 resolution of its tangent bundle by trivial bundles, i.e. a trivialization of `TX` (nLab *framed manifold*; the `G = {e}` G-structure), with stable framings as trivializations of `TX + R^k` and `n`-framings as trivializations of `TX + R^(n - dim X)`. Specimens: `S^1` and a Lie group framed by left-invariant vector fields; `S^2` not framable and stably framable.

- [ ] **`optional-manifold-tangent-bundles`**. **Needs:** `terminal-session`.
  **Goal:** the tangent bundle of an object of `SmoothManifolds` (`categories/manifolds.py`) as an owned vector bundle, with its module of sections `Der(C^oo(M))`, realized through SageManifolds' tangent bundle privately. Specimen: `TS^1` trivial of rank 1.

- [ ] **`optional-random-lattices-of-given-invariants`**. **Needs:** `terminal-session`.
  **Goal:** random lattices in `Lattices(ZZ)` with a prescribed signature, determinant or rank, built as a random `SL(n, ZZ)` congruence `A^T G A` of a diagonal Gram matrix with Sage's randomness scoped by `seed()`, returning owned lattices, not matrices; and a random isotropic subgroup of a discriminant module (`categories/modules/framed/formed/discriminant_modules.py`, next to `isotropic_subgroups`), feeding `overlattice`. Prior art and its tests: `archives/random-lattice-constructors/`. State the limit: congruence of a diagonal form reaches only odd unimodular lattices, so a random lattice within a genus needs a different construction.

- [ ] **`optional-moduli-of-stable-curves`**. **Needs:** `terminal-session`.
  **Goal:** the moduli of stable pointed curves over the owned scheme categories. The category of stable graphs of type `(g, n)` with contractions and automorphisms, the stratification of `Mbar_{g,n}` by dual graphs, and charts for `M_{0,n}`, `Mbar_{0,n}`, `M_{1,n}`, `M_{2,n}`. The cited values (Harris-Morrison, Arbarello-Cornalba, Chan) become rows of `tests/test_known_mathematics.sage` with their citations. Prior art: `archives/dm-moduli-spike/`.

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
