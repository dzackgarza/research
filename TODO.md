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
- [Constructor and admission foundations](#constructor-and-admission-foundations)
- [Diagrams, rings and geometric consumers](#diagrams-rings-and-geometric-consumers)
- [Forms, actions and arithmetic realizations](#forms-actions-and-arithmetic-realizations)
- [Common categorical authority and public boundaries](#common-categorical-authority-and-public-boundaries)
- [Maintained computation and honest frontiers](#maintained-computation-and-honest-frontiers)
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

- **Defining datum:** the exact owned objects, maps, base and hypotheses are fixed at admission, with one constructor and no disabling flag (`CON-16`, `OWN-22`, `OWN-23`).
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

## Constructor and admission foundations

Paths below are relative to `src/dzack_research/preamble/categories/` unless a different root is given. These nodes repair existing constructions. A requested source review is an unresolved obligation, not a claim that every named path is broken.

## Diagrams, rings and geometric consumers

## Forms, actions and arithmetic realizations

- [ ] **`lattice-action-results`**. **Needs:** none.
  **Owner and delta:** isotropic loci, orbit decompositions, centralizers, reduction adjacency and their functors/arrows; use the shared action/G-set and existing private arithmetic engines.
  **Invariants:** a locus is its owned mathematical set, an orbit comes from the actual action, a centralizer comes with its subgroup inclusion, and adjacency belongs to its represented complex. Preserve transporter/representative/completeness distinctions and defining equations. Existing torsion-form delegation through the G-set owner is a dependency to preserve, not work to recreate.
  **Closure specimens:** a finite action with multiple orbits gives orbit maps and stabilizers satisfying orbit-stabilizer; an isometry centralizer retains commuting witnesses. A bounded indefinite-lattice search is not a complete orbit classification. Review remaining isotropic, centralizer and reduction host records and their consumers; do not replace missing algorithms by unconditional stubs.

- [ ] **`objects-through-categories-lattice-files`**. **Needs:** `lattice-action-results`.
  **Owner and delta:** lattice, hyperbolic, orthogonal-quotient and reduction files under categories: finish placement and inherited-construction review across their remaining host records and maps.
  **Coverage boundary:** enumerate the construction routes and retained mathematical records in these files, including the arithmetic application callers. Earlier formed-module, primitive-extension and action deliveries already own defects on their changed paths; reconcile only independently remaining cases here while preserving their acceptance.
  **Invariants:** Lattices(R) constructs through its formed module on the exact selected module. Polytopes/cones/rays, manifold points and analytic opens stay at their existing mathematical owners. Category declarations state immediate sufficient structure rather than defaulting to Sets because an owner is inconvenient.
  **Closure specimens:** lattice arithmetic and induced forms, an isotropic locus, a centralizer inclusion and a nontrivial reduction adjacency answer through those owners. Review the complete named family, preserving currently integrated Voronoi and Allcock realizations and their maps. No deletion or class-label rewrite alone satisfies this node.

## Common categorical authority and public boundaries

- [ ] **`owned-product-results`**. **Needs:** none.
  **Owner and delta:** `CommutativeSquare.components()`, `NaturalTransformation.naturality_square()` and the complete public tuple-result family under `CON-15`.
  **Invariants:** genuinely mathematical products and indexed families have owned parents, projections and component codomains. Use existing product/family constructions; do not introduce a record class for each pair. Private adapter tuples remain representation data at their boundary.
  **Closure specimens:** project each square component into its actual morphism space and recover the naturality equation on a nonidentity arrow. Tensor shape/valence and invariant-factor families retain their mathematical indexing rather than a Python positional convention.

- [ ] **`owned-provenance-data`**. **Needs:** `objects-through-categories-lattice-files`, `sheaf-descent-threading`.
  **Owner and delta:** all remaining source/preimage, coordinate-morphism, presentation, comparison, completion and base-change side channels throughout the preamble, including schemes.
  **Coverage boundary:** reconcile residual declaration/assignment/read families against earlier construction deliveries. A producer cannot defer defining data used by its own consumers to this sweep; distinct untouched constructions remain this node's work.
  **Invariants:** each selected source or map is declared construction data at its mathematical owner. Derived/debug metadata carries no mathematical authority. A shared result object never receives caller-specific presentation state. A genuine chosen preimage of a functor remains a choice, not a reconstructed equal object (`CON-05`, `OWN-19`).
  **Closure specimens:** two constructions sharing an underlying result but choosing different presentations keep both choices without contaminating each other; base-change and completion consumers recover their exact maps from the defining datum. Review every residual assignment and read, not only `_preamble_*` names. Renaming or moving fields to a dictionary cannot close this node.

- [ ] **`construction-datum-classification`**. **Needs:** `owned-provenance-data`.
  **Owner and delta:** every private Construction/Datum record across the preamble, including predicate subgroups, linear systems and geometric cohomology.
  **Invariants:** a retained record denotes genuine selected mathematical data with a real consumer, such as a functor preimage; a package that only forwards constructor arguments dissolves into its owning constructor. Preserve general defining data and genuine choices without proliferating record classes.
  **Closure specimens:** follow an actual selected preimage through its downstream map and distinguish two valid choices; compare an ordinary multiplication constructor whose `(M,m)` needs no extra category or argument bundle. Classify the complete occurrence family and transfer every consumed datum before removing a record.

- [ ] **`private-owner-boundaries`**. **Needs:** `owned-provenance-data`.
  **Owner and delta:** the independently remaining cross-object engine/storage accesses across the preamble under `OWN-05`--`07`. Reconcile the full declaration/caller population with the constructor and provenance deliveries; accesses used by those repairs were closure-blocking there and cannot be parked here.
  **Invariants:** ordinary mathematics calls owned operations. Protected access has a declaration-side contract naming exact permitted caller roles. A helper, underscore, importable factory or comment at the caller grants no authority. Lowering/raising lives at the single adapter for that representation. Generic construction owners do not import their specialized consumers to select a route; specialization data enter through the shared contract. Generic framework repairs belong to `sage-categories`, with owned preamble mathematics and its integration kept here, rather than another local framework.
  **Closure specimens:** a geometric section operation and a lattice/group operation traverse the owned owner and retain their maps and coefficients; no consumer opens another object's backend to finish the calculation. Inspect the call chain across the boundary, including lazy results. A private extraction of the same access is not remediation.

- [ ] **`recursive-owned-results`**. **Needs:** `private-owner-boundaries`, `owned-product-results`.
  **Owner and delta:** public results throughout the affected algebraic, geometric and arithmetic owners, including maps, coefficients, base rings, representatives and lazy family values.
  **Coverage boundary:** follow return paths and subsequent public operations across the full named family, preserving recursive ownership already delivered with each producer and repairing independently remaining escapes. A producer's owned top level never authorizes deferring its raw children to this sweep.
  **Invariants:** raising reaches every publicly reachable mathematical constituent and subsequent arithmetic, through its canonical constructor. An owned parent containing raw engine children does not satisfy `OWN-04`. Arbitrary raw-engine ingress is not an alternative public API.
  **Closure specimens:** project a returned morphism component, evaluate a delayed family stage, extract a coefficient and perform arithmetic on it; each result has the correct owned parent and expected equation. Use both a geometric sheaf result and an arithmetic orbit/presentation result so a top-level wrapper cannot certify the boundary.

- [ ] **`membership-by-placement`**. **Needs:** `objects-through-categories-lattice-files`, `sheaf-descent-threading`.
  **Owner and delta:** category containment throughout the preamble, including abstract functor, arrow, product, morphism and sheaf categories and predicates hidden in helpers.
  **Coverage boundary:** enumerate category declarations and follow their inherited/overridden containment and helper calls, then compare every route with the original "each category" requirement. Distinguish genuine element membership at set owners explicitly. A scan of `__contains__` bodies or the original scheme complaint alone is incomplete. Earlier producer repairs must already establish their placements; this node reconciles the untouched remainder.
  **Invariants:** category membership follows construction placement or the specified functor, not engine class, duck typing, cardinality, or an implicit walk up a base-ring tower. Distinguish category membership from genuine element membership in a mathematical set; the latter may require an exact predicate at its owner.
  **Closure specimens:** a correctly placed object is accepted, a similarly represented object with the wrong structure is not. A QQ-scheme is not silently treated as a ZZ-scheme without the specified base passage. Check discrete categories and arrow helpers as well as the original scheme example; inspect every category containment body before closure.

- [ ] **`inherited-operations-not-restated`**. **Needs:** `objects-through-categories-lattice-files`.
  **Owner and delta:** `cardinality`, `zero`, `scalar_multiple`, `module_generator`, `module_generating_set` and the broader general-operation family implicated by these repairs.
  **Coverage boundary:** compare the declarations, overrides and actual inherited data across this family. Earlier constructor nodes already owe usable inherited operations on their delivered routes; reconcile independently remaining restatements and genuine specializations here.
  **Invariants:** the weakest sufficient category owns the operation; descendants inherit it from real construction data. A theorem-backed specialized algorithm may remain if it adds genuine computation and agrees with the general operation. Multiple definitions are not automatically duplication, and a forwarding copy is not inheritance.
  **Closure specimens:** free, presented, formed and algebra objects answer these operations through their construction before special accessors run. Compare a specialization against the general operation on a separating nonzero element; inspect all definitions in the named family, including stronger morphism spaces.

- [ ] **`refinement-convergence`**. **Needs:** `owned-provenance-data`.
  **Owner and delta:** every remaining `refine`/placement mutation in ring, scheme, module and functor-image construction after the bootstrap repair.
  **Invariants:** defining or selected structure exists at construction; later refinement only records a genuinely newly established mathematical fact. No accessor, engine query, import order or first arithmetic operation completes initialization retroactively.
  **Closure specimens:** request categories and inherited operations in different orders for ring, scheme, module and functor-image objects and obtain the same mathematical data. Each surviving refinement identifies the later theorem and its evidence. Moving mutation behind a helper or converting it into a category flag cannot close the node.

- [ ] **`probe-and-exception-residue`**. **Needs:** `private-owner-boundaries`, `membership-by-placement`, `refinement-convergence`.
  **Owner and delta:** all remaining `isinstance`, `getattr`, `hasattr`, `__dict__` probes and exception branches across preamble mathematics.
  **Invariants:** owned operations use the category's declared contract. Any sanctioned ingress/equality/containment or adapter probe is reviewed against its declaration; the method name alone grants no exemption from `CAT-23` or `OWN-05`. Runtime exceptions do not select an alternative mathematical algorithm; declared boundary rendering preserves the real failure.
  **Closure specimens:** supported input takes its owned route; a nearby unsupported representation fails at the stated frontier; an engine defect is not converted into a false value or another algorithm. Inspect each residual site and called helper. Search completeness is coverage evidence; replacing syntax without repairing data flow fails `DEV-68`.

## Maintained computation and honest frontiers

- [ ] **`singular-kernel-delegation`**. **Needs:** none.
  **Owner and delta:** `_singular_presentation_kernel` in `modules/framed/finitely_generated/finitely_presented_modules.py`: replace locally reconstructed kernel/presentation computation with the suitable maintained operation and owned integration.
  **Invariants:** inspect the installed Sage/Singular contract for input relations, coefficient rings, output presentation, inclusion and lifting/factorization. `homolog.lib::hom_kernel` and `modules.lib::kerHom` are discovery candidates, not interchangeable promises. Representation conversion remains private; two low-level `modulo` calls inside the old Python algorithm do not count as delegation. Preserve exact unsupported coefficient frontiers.
  **Closure specimens:** over A=Q[x,y]/(xy), the kernel of multiplication by x is the ideal (y), with its nonfree presentation, inclusion and factorization. Recover the relation x*y=0 inside that kernel presentation; a free rank-one substitute fails. Source review establishes maintained computation and all owned maps, not merely agreement of dimensions.

- [ ] **`imperative-algorithm-cleanup`**. **Needs:** `lattice-action-results`.
  **Owner and delta:** the complete catalogue of bilinear accumulation, duplicate free-algebra target multiplication, divided-power coefficients, absolute-Galois filtering, grouping and frontier/seen traversal in actions/lattices.
  **Invariants:** delegate the semantic operation to its weakest sufficient owned or maintained computation owner. Keep only representation adaptation or source-justified theory-specific algorithms; a list comprehension or a private helper containing the old loop is not a repair. Preserve already-correct torsion-form action delegation.
  **Closure specimens:** a noncommutative word preserves order under a universal extension; a divided-power product has its actual coefficient; a finite action with several orbits preserves representatives and stabilizers. Review every catalogue family, documenting the theorem for retained specialized loops and the actual dependency operation for replaced algorithms.

- [ ] **`assertion-frontiers`**. **Needs:** `singular-kernel-delegation`, `imperative-algorithm-cleanup`, `objects-through-categories-lattice-files`.
  **Owner and delta:** all public mathematical operations using `NotImplementedError` or equivalent runtime dispatch failures across schemes, algebras, rings, modules, lattices and groups.
  **Invariants:** keep the full mathematical domain. Supported exact cases use their maintained owner; only the precise unsupported computational remainder fails at the declared hypothesis/representation frontier. Existence, representation and computability are distinct. An undecidable assertion is not a false theorem, and making a required concrete operation abstract does not deliver it.
  **Closure specimens:** each operation family has a positive supported case and a nearby unsupported case distinguished by its actual hypothesis. Retain integral torsion, infinite objects and nonfree presentations where required. Review complete control flow, not only exception spellings; no blanket replacement with `assert False` or an unconditional message closes the family.

- [ ] **`placeholder-stubs`**. **Needs:** `assertion-frontiers`.
  **Owner and delta:** remaining public unconditional failure/pass bodies, including the profinite abstract contract; recheck old tensor examples against current source before changing them.
  **Invariants:** every concrete promise has a successful mathematical path; a genuine abstract contract is explicitly abstract, with its concrete obligations still assigned. Removal is permitted only for a misplaced duplicate after its behavior and consumers reach the correct owner. No required API disappears to improve a scan.
  **Closure specimens:** tensor rank/valence and the surviving profinite interfaces expose their promised data or genuine abstract contract. Every removed concrete placeholder has an implemented owner and a consumer specimen; otherwise its implementation obligation remains open here.

## Public mathematical interaction

- [ ] **`mor-spelling-convergence`**. **Needs:** none.
  **Owner and delta:** all owned morphism-category definitions, exports, imports and consumers: the public spelling is `X.Mor(Y)`. Sage `Hom` remains only at a private adapter calling the actual Sage operation.
  **Invariants:** rename the entire owned definition/reference family coherently without compatibility aliases or fake upstream stubs. Endpoint categories and inherited operations are preserved. Protected expectation subtrees are never rewritten to make the new implementation pass.
  **Closure specimens:** direct session construction and composition in module, algebra and scheme morphism spaces use Mor and exercise nonidentity maps. Source review covers owned definitions and dynamic exports as well as call sites. A spelling-only search cannot certify that the resulting morphism belongs to the right category.

- [ ] **`coordinate-firewall`**. **Needs:** none.
  **Owner and delta:** ordinary lattice, module, tensor and morphism coordinate/storage accessors and all research consumers of them.
  **Invariants:** coordinate views belong to a specified finite framing/presentation; a coordinate matrix of a linear map requires the chosen free endpoint framings (`CON-04`). Nonfree generators are not a basis. Ordinary operations use owned morphisms, tensors and universal constructions, without extracting raw engine storage.
  **Closure specimens:** express the same map in two selected bases and preserve its semantic action; a relationful module cannot acquire a free-module matrix by listing generators. Include an unframed/infinite object. Migrate actual consumers before removing to_list/to_tuple/to_vector/components/list escapes; their mathematical needs remain required.

- [ ] **`mathematical-return-types`**. **Needs:** `refinement-convergence`, `recursive-owned-results`.
  **Owner and delta:** the full public return-annotation family using Parent, Element, CategoryObject or ad hoc Any, including functor images, cardinalities and scheme operations.
  **Invariants:** annotations name the actual mathematical codomain, refinement or honest union. A central mathematically named alias may express a limitation of Python syntax; a universal type with a new name may not hide it. This node does not optimize checker counts.
  **Closure specimens:** follow a functor image, a cardinality, a scheme map and a composite's components into operations their claimed codomain supports. Review every occurrence family and required central alias; no narrowing to the currently convenient engine realization or broad Any escape.

- [ ] **`mathematical-display`**. **Needs:** `owned-product-results`, `inherited-operations-not-restated`.
  **Owner and delta:** generator/family displays, maps and other public results exposing implementation labels under complaint 4 and `OWN-21`.
  **Invariants:** display gives cheap positive information about the particular mathematical object at the requested abstraction level. No engine repr delegation, object address, private class/refinement label or expensive enumeration. A bounded display of an infinite object is marked as such and does not change its meaning.
  **Closure specimens:** free-module generators display their mathematical data; an enriched lattice does not rename the same generic generator result after the leaf class. A nonidentity map exposes its mathematical endpoints, and an infinite family has a useful bounded display. Rendering is inspected at T, not inferred from source.

- [ ] **`banned-language-residue`**. **Needs:** `mor-spelling-convergence`, `mathematical-display`.
  **Owner and delta:** the terminology replacement index across the remaining preamble public source and examples, including carrier and opaque implementation vocabulary.
  **Invariants:** replace each term with the actual object it denotes, such as an underlying set, module or arrow target. Preserve different mathematical notions even when old names resemble each other. No opaque synonym or new alias evades the dictionary.
  **Closure specimens:** read complete declarations and their callers for each remaining family, checking that terminology exposes correct domains/codomains. Search for prohibited terms verifies coverage, while the mathematical reading establishes acceptance. Private Sage calls retain Sage's exact API names.

- [ ] **`canonical-notebook-contract`**. **Needs:** `coordinate-firewall`, `mathematical-return-types`, `banned-language-residue`.
  **Owner and delta:** `computations/notebooks/preamble.ipynb`, through japi, organized around research questions and their mathematical witnesses (`NB-01`--`05`).
  **Invariants:** all substantive claims are executable assertions or displayed witnesses using the final owned session API. Preserve the existing useful research content; replace raw constructors, global Hom, ambiguous generators and coordinate workarounds with their mathematical owners. Clear stale failure output without representing unexecuted replacements as passed.
  **Closure specimens:** actual algebra substitutions, a nonidentity morphism, group/lattice constructions and the notebook's geometric claims have falsifiable expected results. Source authoring closes here; clean-kernel execution and visual inspection of every relevant rendered output remain required in `terminal-session`.

## Source convergence and terminal proof

- [ ] **`architecture-remediation`**. **Needs:** `construction-datum-classification`, `probe-and-exception-residue`, `placeholder-stubs`, `canonical-notebook-contract`.
  **Owner and delta:** the integrated source route from public category entry through complete defining data, private computation and every owned result and consumer, against all unresolved complaints.
  **Invariants:** every required source descendant closes before this node; introducing a residual child keeps this node open. Each complaint's entire burden is discharged or retained in a required prerequisite. All alternative construction routes affected by a repair are inspected. No numerical answer, renamed field, new wrapper, source count or administrative record substitutes for delivery (`DEV-67`, `DEV-68`).
  **Closure comparison:** reconcile the original complaint/requirement clauses with the delivered owner and consumer routes, including the generality beyond their first specimens. Review later changes to each shared contract against its delivery evidence. In particular, an "assumed linear" rename, a framing proof depending on its own Mor placement, or a private access deferred from a delivered producer fails this comparison and reopens that exact repair. Existing evidence for unaffected routes remains usable.
  **Closure evidence:** bank falsifying specimens for every repaired obligation, including inherited operations, wrong nearby inputs and relevant infinite/nonfree/base-change cases. Commits record source coverage and unexecuted proof. Review composed consumers after their prerequisites, without rerunning an unrelated whole-tree inventory after every leaf. Source closure authorizes T; it does not claim runtime success.

- [ ] **`research-sage-runtime`**. **Needs:** `architecture-remediation`.
  **Owner and delta:** the tracked `.envrc` and intended stable research-Sage installation, verified through the existing just recipes once source remediation closes.
  **Invariants:** establish the currently selected executable, interpreter, version and declared dependencies before diagnosing an environment failure. The old failed source-checkout launcher is not evidence that the current `.venv/bin/sage` fails. Repair a reproduced defect at the intended installation; no temporary Sage distribution or filesystem dependency replacement.
  **Closure evidence:** the tracked environment launches the intended Sage, preparses the repository's `.sage` inputs by the normal route and reaches the fresh star import. If it already does so, no environment edit is required. Keep mathematical failures distinct from launcher/provisioning failures.

- [ ] **`terminal-session`**. **Needs:** `research-sage-runtime`.
  **Owner and delta:** execute the integrated mathematical proof burden on the final owned session and research notebook; `DEV-58` governs this transition.
  **Invariants:** a fresh process imports `from dzack_research.preamble.all import *` and exposes Cat and Lattices. This is a prerequisite, not mathematical acceptance. Regenerate `docs/preamble-megadoc.md` and the graph through `just preamble-megadoc`; inspect their agreement with live categories, operations, domains and codomains. Preamble warnings and order-dependent imports require repair.
  **Closure evidence:** execute all required banked construction specimens and the protected expectation/user-simulation obligations through the prescribed project recipes, classify actual failures at their owners and repair them without weakening expectations. Cover direct, convenience, functor, catalogue and engine-raised routes; free/nonfree, finite/infinite and changed-base regimes where claimed. A previous run certifies only the source it exercised.
  Use japi for notebook execution and inspect actual rendered mathematical outputs; source, saved files and successful imports do not prove rendering or mathematical claims. Run the prescribed final QC at its applicable boundary, retaining explicit evidence for any remaining failures. A required failure keeps this node open; fixes and focused re-execution stay within T rather than restarting the architecture suspension. Respect push authorization.

## Post-remediation convergence

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
