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

- [x] **`localization`**. **Needs:** none.
  Route fraction fields and their maps through the existing localization owner, and close the affected specialization paths.
  **Owners:** `rings/ring_foundation.py::OwnedRings.ParentMethods.fraction_field`, `OwnedIntegralDomains.ParentMethods.fraction_field_map`, `rings/commutative_algebra.py::_localization_at_submonoid`, and the existing submonoid, ring Hom, and module-localization owners.
  **Observed gap:** see the [localization complaint](COMPLAINTS.md#localization-must-define-its-fraction-field-specialization) for the inspected specialization bypass and mathematical dependency trace.
  Preserve the existing general localization and element/prime routes.
  **Decision:** the domain's nonzero-element submonoid defines this specialization.
  The private Sage fraction-field operation remains a computational realization, but raising must establish that localization datum, its source map, and its universal factorization.
  Selecting the fraction-field realization must not call the public fraction-field method again during construction.
  **Integration:** extend the existing submonoid dispatch with this represented case, not a second localization class or a finite enumeration of nonzero elements.
  Review field inputs, prime complements, element-generated submonoids, and the number-field specialization against the same declaration.
  Preserve canonical field identities while retaining the map from each original source; do not attach source-dependent state to a shared field singleton.
  **Required consumer:** module scalar extension along the resulting fraction map uses the existing module-localization/scalar-change functor.
  Inspect every caller of the changed fraction-field and localization-map contracts and adjust dependent callers in this unit, without rebuilding unaffected local algebra.
  **First specimen:** the fraction field of `ZZ` and its source morphism, with numerator/denominator interpretation and the induced map of a module.
  **Separating specimens:** `ZZ[1/2]` and `ZZ_(3)` retain different unit behavior from `QQ`; a ring with zero divisors requires its total quotient-ring operation, not the fraction-field operation.
  Locality is justified for prime localization, not for all submonoids.
  **Acceptance:** direct owned construction, the fraction-field method, and scalar-change consumption establish the same semantic contract and comparison maps.
  Source review confirms the retained maintained arithmetic and absence of a bypass; specimens exercise owned elements, submonoids, and morphism endpoints.
  Follow the [construction factorizations](CONTRIBUTING.md#required-construction-factorizations), `OWN-02`, `OWN-07`, and `OWN-10`; do not infer constructor convergence from equality of printed rings or impose a general submonoid-equality algorithm.

### Completion objects and finite approximations

- [x] **`module-completion`**. **Needs:** none.
  Make finite-module completion consume the corrected ring completion and construct its functorial maps.
  **Owner:** `modules/framed/finitely_generated/finitely_presented_modules.py`, module scalar change, and the existing ring completion owner.
  **Reuse:** use the existing scalar-change functor on the supplied module presentation and its morphisms.
  Resolve any missing coefficient transport at that owner.
  Module completion must not implement another tensor product, relation reducer, or precision convention independent of the ring completion.
  **Decision:** use `M tensor_R R_hat` as completion for finite modules over a Noetherian ring, with the canonical comparison to the inverse limit and exactness justified by [Stacks 00MA](https://stacks.math.columbia.edu/tag/00MA). Keep the general completion definition separate from that theorem; finite presentation alone does not authorize every Noetherian exactness claim.
  **Deliver:** the completed module, canonical map into its scalar restriction, completed nonidentity morphisms, and `M_hat -> M/I^n M` with transitions.
  Preserve the selected presentation and transport maps without treating its framing as a basis.
  **First specimen:** multiplication by `x` on the free rank-one module over `QQ[x]` remains injective after `(x)`-adic completion.
  Multiplication by `x` on `QQ[x]/(x^N)` has a nonzero kernel.
  **Acceptance:** the implementation distinguishes those maps and realizes the completed exact sequence with cokernel `QQ`. Repeat the free-module construction over `QQ[x,y]` completed at `(x,y)`, so the multivariable route cannot escape the same obligation.
  Also use a free-plus-torsion module; an already annihilated torsion example alone cannot test completion.

- [x] **`quotient-completion`**. **Needs:** `module-completion`. Implement quotient/completion comparisons with hypotheses and actual maps.
  **Owner:** ring quotient, module quotient, and completion functors.
  **Decision:** in the Noetherian finite regime, construct the comparison between completing a quotient and quotienting the completion by the extended ideal/submodule.
  Derive it through completed maps and cokernels.
  Retain closure requirements outside that regime; do not identify a quotient by an arbitrary nonclosed submodule with a completed quotient.
  **Specimen:** complete `QQ[x,y]/(xy)` at `(x,y)` by both supported routes.
  Match the images of `x,y`, their product, projections to several orders, and the maps from the original algebra.
  **Acceptance:** an explicit comparison isomorphism, not matching dimensions or a pair of parents with similar printed equations.

- [x] **`completion-comparisons`**. **Needs:** `quotient-completion`, `local-module-maps`. Define the supported localization/completion and base-change comparisons before formal-family consumers use them.
  **Decision:** there is no unrestricted rule that completion commutes with localization or arbitrary scalar extension.
  State the source and target of each proposed comparison and the theorem making it an isomorphism.
  For a Noetherian algebra at a chosen maximal ideal, use the appropriate maximal-adic local comparison.
  For other localizations retain only the maps actually supplied by the topology.
  **Separating example:** `QQ[[t]][1/t]` is nonzero, whereas completing `QQ[t,1/t]` with respect to the extended ideal `(t)=(1)` gives zero.
  **Acceptance:** no general localization functor or family method silently identifies these constructions; a formal generic fiber is not obtained by relabeling a finite truncation.

### Local algebra extensions

- [x] **`normalization`**. **Needs:** none.
  Extend normalization and local-length operations beyond the represented integral affine and selected plane-curve regimes needed below.
  **Owners:** `rings/commutative_algebra.py`, `rings/commutative_ideals.py`, their normalization adapter, and `schemes/singularities.py`. **Deliver:** total quotient rings for supported reduced rings, regular-element tests, normalization maps componentwise when required, conductor ideals, height-one valuations, and finite local lengths with residue-field degree accounted for.
  Preserve minimal primes, components, and support.
  **Decision:** normalization is a ring/scheme map, not a selected polynomial normal form; a list of normalized components is not yet the glued normalization.
  Local invariants name a point; global delta cannot be substituted for delta at that point.
  **Acceptance:** a reducible reduced curve, a singular integral curve, and a nonrational closed point exercise the required maps and local lengths.
  Reuse the existing integral normalization and local `deltaLoc` operations.
  **Capability question:** which operation in the existing Singular normalization adapter supplies the reduced/componentwise case, conductor, and comparison maps?
  Inspect the corresponding OSCAR/Macaulay2 operations only for obligations the current adapter cannot discharge.
  Retain that choice at the adapter; extend its raising of ideals, components, and maps rather than implementing local normalization, factorization, or length algorithms in the scheme consumer.

- [x] **`local-module-maps`**. **Needs:** none.
  Extend local homomorphisms and local-module operations only at their shared owners when these consumers require a new supported coefficient regime.
  **Owners:** ring Hom, prime localization, localized ideals and module presentations.
  **Preserve:** `QQ[x]_(x)` has nonunit `x` and unit `1+x`; `QQ[x,y]/(xy)` localized at `(x,y)` retains zero divisors; localizing `QQ[x]/(x)` by `x` yields the zero module.
  **Deliver:** ideal extension/contraction, residue maps, maximal-ideal compatibility, and direct-map kernels through the existing exact algorithms, including nonreduced coefficients where supported.
  **Acceptance:** transported maps and directly constructed local maps agree through their comparison morphisms.
  A fraction-field computation cannot supply a local-ring unit, kernel, or vanishing claim without the required faithful comparison.

## Architecture before dependent implementation

These are targeted remaining contracts and preservation obligations, not a restart of the module/algebra/action constructions.

### Shared diagrams and universal constructions

### Constructor and ownership convergence

- [x] **`constructor-data`**. **Needs:** none.
  Complete constructor-contract discovery and close the remaining variadic/opaque defining-data boundaries.
  **Owners:** the common `object_of` construction path, generated category contracts, typed parameterized categories, and surviving functors.
  **Deliver:** named mathematical parameter domains and required data for ordinary construction, adopted runtime realizations, Hom construction and property refinement.
  Specializations fulfill inherited accessors before returning their objects.
  **Boundary decision:** a private runtime realization still receives complete owned defining data through the common constructor; adoption is not a public raw-engine input form.
  Inspect inherited zero/one, empty families, component access, and scalar actions as well as the newly declared accessor.
  Keep presentation changes explicit through maps, not mutations of retained data.
  **Decision:** retain the exact supplied module when equipping distinct algebra structures; chosen multiplication/action/presentation is new structure, not a property mutation.
  Refinement cannot overwrite another structure.
  **Acceptance:** source-backed public signatures and constructor examples cover an algebra and a module over the same object, a noncommutative regular module action into additive endomorphisms, and two multiplications on one supplied module.
  Generic owners do not import their new descendants.
  Keep general class/functor compilation at `sage-categories`, not here.

- [x] **`general-modules`**. **Needs:** none.
  Extend general module contracts outside the current finite presentation algorithms without weakening their mathematical domains.
  **Owners:** `categories/modules/general_modules.py`, module Homs, rank functions, framings, and scalar-change functors.
  **Deliver:** additive-group ownership for general supplied modules; source-backed linearity algorithms where decidable; broader PID/Smith/ Hermite support when an engine theorem applies; and infinite-cardinal rank where represented.
  **Decision:** fiber rank, locally constant finite-projective rank, and generic rank over a domain are separate notions.
  A finitely generated or finitely presented property supplies no chosen framing by itself.
  **Acceptance:** a nonfree module, a nonconstant rank function, an infinite indexing set, and an unsupported callable equality problem retain their correct interfaces and computational frontier.

## Covering families and sheaves

**Integration route for this workstream:** the covering-family owner constructs the geometric descent datum; local kernels, cokernels, tensor products, restriction, and scalar change use the existing module/algebra owners.
At the first unsupported local computation, determine whether its established Sage/Singular module operation or the applicable CAP module-presentation operation supplies the needed maps.
Repair that adapter once.
Research a sheaf-level package for the specified geometric category when it can supply a larger operation; do not assume a finite-category presheaf package computes arbitrary scheme sheaves.
Keep the exact missing comparison or descent datum with the item that requires it (`OWN-08`, `OWN-09`, `DEV-56`).

- [x] **`affine-descent`**. **Needs:** none.
  Extend module and algebra descent from one distinguished affine cover to covering families with distinct overlap rings.
  **Owners:** `categories/schemes/gluing.py`, `categories/schemes/affine_covers.py`, and `categories/divisors/invertible_sheaves.py`. **Current boundary:** `ModuleGluingDatum` obtains both transition endpoints through one cover's `restricted_module`/intersection path.
  **Decision:** use the two overlap open immersions and their isomorphism.
  Transport the module on the other chart along that isomorphism's ring pullback before comparing or composing local maps.
  Reuse the finite scheme gluing's triple-overlap transport.
  **First specimen:** a nontrivial invertible sheaf on the standard two-chart cover of `P^1`, then its refinement to three charts.
  **Acceptance:** actual inverse and triple-cocycle equations in the correct Homs, glued nonidentity morphisms, and explicit refinement comparisons.
  Isomorphic overlap rings are not silently identical parents.
  [Stacks 01JA](https://stacks.math.columbia.edu/tag/01JA) supplies the scheme gluing maps and compatibility requirements.

- [x] **`general-descent`**. **Needs:** `affine-descent`. Extend the same covering-family owner to non-affine overlaps and to the corresponding locally ringed-space and manifold atlases.
  The locally ringed-space part retains non-affine overlaps, both embeddings, and affine-refinement comparison maps; manifold atlas owners retain topological, finite-`C^k`, and smooth coordinate changes.
  **Deliver:** an affine refinement of a represented non-affine overlap, comparison maps between refinements, and local-to-global gluing independent of the chosen refinement.
  Include smooth, topological, and `C^k` atlas maps at their respective owners.
  **Decision:** a covering family is not necessarily a distinguished cover of one affine scheme.
  It must not acquire a fictitious global coordinate ring.
  **Acceptance:** the punctured-plane/overlap construction and refinement diagrams retain chart labels and both embeddings; non-affine global sections do not replace the whole space by their spectrum.

- [x] **`sheaf-operations`**. **Needs:** `general-descent`. Implement sheaf kernels, cokernels, tensor products, local presentations and stalk comparisons through the existing module operations.
  **Owner:** module sheaves and their descent morphisms.
  **Deliver:** restrictions of each construction, comparison to chartwise constructions, and the induced maps at stalks.
  **Decision:** use the sheaf category in which the construction exists.
  Taking a cokernel of global sections is not in general the global sections of the sheaf cokernel; taking an inverse limit of sections is not automatically an exact sheaf construction.
  **Acceptance:** a nonzero map of sheaves with nontrivial kernel/cokernel and a refinement comparison; equality tests live at the responsible module/Hom owner rather than in a new sheaf-level coordinate algorithm.

- [x] **`sheaf-functors`**. **Needs:** `sheaf-operations`. Construct inverse image, direct image and module pullback along represented scheme morphisms with their correct categories and variance.
  **Decision:** inverse image of a sheaf and tensoring by the target structure sheaf are distinct steps of module pullback.
  Preserve the structural ring map and canonical comparison morphisms.
  **Deliver:** functor actions on nonidentity maps, identities, composition, and the applicable adjunction unit/counit.
  **Acceptance:** a nontrivial base change of an invertible sheaf agrees via a constructed comparison with pulling back its transition data.

## Divisors and relative geometry

**Integration decisions:** products and intersections enter the existing diagram, algebra pushout, quotient, and gluing constructions.
Divisor and line-bundle operations enter their owned groups and sheaf functors, not a scheme-specific matrix layer.
For each selected non-toric regime, inspect the applicable maintained Singular/Macaulay2/OSCAR operation for class relations, sections, Rees algebras, saturation, or intersection data, with its hypotheses and returned maps.
The unanswered question is which full operation supplies the chosen specimen, not whether these theories should be reimplemented here.
Retain existing fan/subdivision and toric-divisor engines for the toric cases.
Do not make an engine's affine or toric specialization the public definition of the more general construction (`OWN-01`, `OWN-08`, `OWN-09`).

## Cohomology and equivariance

### Shared complex and DGA integration

- [x] **`complexes`**. **Needs:** none.
  Complete the remaining coefficient-ring computation boundary without replacing the owned cycle/boundary quotient by an abstract homology group.
  **Owners:** module kernels/images/cokernels and the common cochain/cohomology owners.
  The represented complex itself now supports integer degrees, finite support with known zero outside it, and lazy indexed families over all `ZZ`. **Current maintained boundary:** finite free kernels use Sage matrix `right_kernel`; PID presentation normalization uses the backend `smith_form`; polynomial-presentation kernels over a field use Singular `modulo` and `lift`. `Cycles`, `Boundaries`, and `Cohomology` compose those operations while retaining the inclusion, boundary-in-cycles map, quotient projection, representatives, coefficients and induced functor maps.
  Sage `ChainComplex.homology` was inspected: it supplies abstract groups and optional cycle generators, but not those full owned comparison maps, so a second whole-complex computation is not selected.
  **Remaining capability:** complexes of finitely presented modules over rings outside the existing PID and polynomial-over-a-field adapters.
  CAP/homalg's ModulePresentationsForCAP, FreydCategoriesForCAP, and ComplexesAndFilteredObjectsForCAP are listed only as computation references and are not provisioned in this repository.
  Provision and inspect the maintained operation before adding any local reduction (`ENG-06`). **First remaining specimen:** over `R=ZZ[x]`, represent the two-term map `R^2 -> R`, `(a,b) |-> 2a+xb`, and retain both the syzygy inclusion generated by `(-x,2)` and the quotient projection onto `R/(2,x)`, together with a nonidentity induced map.
  This ring deliberately lies outside the currently represented PID/Singular-field regimes.
  **Construction decisions:** homological resolutions keep their augmentation and degree convention explicitly; cochain complexes use degree `+1`. A finite computational window, if introduced by a provider, must contain both incoming and outgoing maps required by a requested degree and must never declare the uncomputed complement to be zero.
  **Acceptance:** the remaining coefficient regime returns owned presentations, cycle/boundary inclusions, quotient maps, representatives and induced maps via a maintained provider; no new local chain-reduction algorithm is introduced.

- [x] **`dga-cohomology`**. **Needs:** `complexes`. Make the existing DGA/cohomology-algebra routes consume that same complex contract and preserve only the algebraic refinements the source justifies.
  **Owners:** `categories/algebras/differential_graded_algebras.py`, `categories/algebras/cohomology_algebras.py`, graded algebras and derivations, and `categories/functors/cohomology.py`. **Preserve:** the existing descended multiplication through cycle representatives and `class_of_cycle`, and the induced map from a DGA morphism.
  Review `CohomologyAlgebras.super_categories`, which currently declares strict graded commutativity, against every admitted source DGA. Place the result in the general graded algebra category and add only justified refinements; characteristic and parity hypotheses must not disappear during raising.
  **Computation selection:** inspect Sage's [commutative DGA operations](https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/commutative_dga.html) for cocycles, coboundaries, cohomology, representatives, and products in the represented degree range.
  Use them for the supported commutative case; inspect the applicable maintained algebra/module operations for other DGAs rather than relabeling them commutative.
  Decide the exact basis/presentation correspondence at the adapter.
  Do not build a second cohomology solver or multiply chosen normal forms without the quotient comparison.
  **Deliver:** inherited underlying module, grading, differential, self-module action, unit when required, multiplication, and nonidentity DGA morphisms through their immediate owners.
  Zero boundary degrees and lazy homogeneous pieces follow the same component contract as ordinary complexes.
  **Specimens:** degree-zero cohomology of a nonnegative unital DGA; a nonzero boundary representing the zero class; multiplication after changing a cycle representative by a boundary; and a source-backed noncommutative DGA that must not acquire graded commutativity.
  Retain the applicable characteristic-two distinction between sign conventions and additional square-zero relations.
  **Acceptance:** forgetting multiplication gives the same complex construction and cohomology modules, with comparison maps if a representation changed.
  Products and induced maps compose through those owned modules.
  Source review establishes inherited data and computational reuse; numerical agreement alone cannot remove this item (`OWN-03`, `OWN-07`, `OWN-09`, `OWN-12`).

### Toric integration before geometric extensions

- [x] **`toric-cohomology`**. **Needs:** `complexes`. Consolidate toric cohomology's existing maintained computations inside declared private adapters and complete raising through the shared constructors.
  **Owners:** `categories/schemes/geometric_cohomology.py`'s `ToricWeightCohomologyComplex` and `ToricLineBundleCohomology`, the existing toric-divisor/fan adapters, and the common complex/module owners above.
  **Starting point:** these functions already use Sage's `_sheaf_complex`, `_sheaf_cohomology_support`, and simplicial chain-complex construction.
  Keep that algorithmic reuse.
  They also call another object's engine accessor and attach geometric data after constructing a complex/module; those paths must satisfy `OWN-03`, `OWN-05`, `OWN-06`, and `OWN-07`. **Capability decision:** first compare the documented public [toric-divisor cohomology operation](https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/divisor.html) with the required weight complex, cycle quotient and induced maps.
  Its returned vector spaces are not sufficient evidence of these correspondences.
  Use the public computation where adequate; any necessary upstream private helper is confined to the declared toric adapter with its source-backed contract.
  Check [Klyachko bundle/sheaf complexes](https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/sheaf/klyachko.html) for the equivariant generalization's actual inputs and outputs, not by name.
  **Deliver:** owned weight/index objects, augmented and shifted differential data, cycle and boundary maps, and the total cohomology construction with its summand inclusions/projections.
  Construct the scheme/divisor/weight datum through the category initializer before exposure.
  An empty support and a zero group retain the same defining data and scalar action as a nonzero result.
  **Missing-map question:** which upstream geometric maps or established complexes supply the requested nonidentity sheaf/restriction/refinement map?
  Obtain and raise that map, then let the shared cohomology functor act.
  Equal weights or dimensions do not define it.
  Preserve explicit completeness, coefficient, and Cartier/Weil hypotheses at their relevant operations.
  **First specimen:** take a divisor with nonzero higher cohomology from the cited Sage toric-divisor examples, retaining the stated fan, coefficients and weight.
  Construct an owned weight class with its representative, inclusion and quotient image, then its inclusion into total cohomology.
  The first induced map is multiplication by `2` on that line bundle over `QQ`, transported through its complex; it must act as multiplication by `2` on the nonzero class.
  Add zero-support and boundary-degree cases.
  Non-scalar geometric and refinement comparisons remain with the extension items; this scalar specimen does not discharge them.
  Acceptance compares actual maps, not only a Betti-number list.
  **Acceptance:** geometry consumes owned complexes and cohomology; the adapter retains existing maintained toric computations; all returned constituents and later arithmetic remain owned.
  Source review covers every affected constructor and private call, with the missing integration recorded at its owner.
  Do not recreate toric cohomology or declare its whole implementation absent.

### Geometric and equivariant extensions

- [x] **`geometric-cohomology`**. **Needs:** `toric-cohomology`, `sheaf-functors`. Extend geometric cohomology from the current toric weight complexes to the required non-toric schemes and sheaves.
  **Owners:** `categories/schemes/geometric_cohomology.py`, sheaf descent, and existing cochain complexes.
  **Dependency and reuse:** consume the common complex/cohomology route above.
  The new geometric work is the justified complex, augmentation and functorial comparison.
  Inspect the appropriate maintained sheaf-cohomology operation for the chosen non-toric presentation before assembling a complex locally; retain an existing resolution or Cech construction when it supplies the full datum.
  The unresolved capability is the non-toric complex and maps, not another kernel, syzygy, chain-reduction, or cohomology implementation.
  **Deliver:** a geometrically justified complex with its augmentation/ comparison, induced nonidentity maps, and actual cohomology modules.
  State which cover computes the theory and why it is acyclic or otherwise sufficient.
  **Decision:** a complex merely having the expected dimensions is not a geometric cohomology construction.
  Refining a cover produces a comparison on complexes and cohomology, not an assertion that two output ranks agree.
  **Acceptance:** a non-toric coherent-cohomology computation and a refinement comparison preserve maps and functoriality.

- [x] **`tor-ext`**. **Needs:** `dga-cohomology`. Extend the existing Tor/Ext functoriality to both arguments and the resolutions needed by geometric consumers.
  **Owners:** module resolutions, chain maps, derived functors, and DGA multiplication at the algebra owner.
  **Computation decision:** inspect the current resolution/derived-module adapter and the applicable Singular, Macaulay2, OSCAR or homalg operations for lifts and resolution comparisons as well as modules.
  The owned functor provides variance and composition; the private adapter supplies maintained resolution computations.
  Repair missing lift transport at that owner, not in each Ext, Tor, intersection, and geometric consumer independently.
  **Deliver:** the unresolved argument's induced maps, correct covariance/ contravariance, comparisons between chosen resolutions, and cohomology independence through the appropriate chain-homotopy argument.
  **Decision:** no unsupported bound may turn a prefix of a resolution into a complete resolution.
  Do not require equal chain lifts when only their induced cohomology maps are canonical.
  **Acceptance:** nonidentity maps in each argument and two chosen lifts; products use a multiplication compatible with the differential and descend to cycles modulo boundaries.

## Families and singularities

**Integration route:** construct a family through the scheme slice; its fibers and coefficient changes use the existing pullback and scalar-change functors.
Formal consumers use the completed object and its inverse system, never their own precision parameter as a defining equation.
Local classification uses the existing singularity/normalization adapters.
Before implementing a new local recognition rule, identify the maintained algorithm for the specified equivalence relation and whether it returns coordinate maps.
For analytic comparisons, monodromy and nearby/vanishing cycles, identify the precise source construction and available implementation first; names shared with algebraic operations do not establish a comparison or authorize a substitute (`OWN-08`, `OWN-09`).

- [x] **`dvr-families`**. **Needs:** `localization`, `completion-comparisons`. Extend `categories/schemes/families.py` to DVR bases through the existing scheme slice and scalar-change constructions.
  **Dependencies:** local algebra; corrected completion only for the completed base-change portion.
  **Deliver:** spectra of DVRs, generic and special fibers via fraction and residue maps, the completed-base family, and maps comparing the two routes to its special fiber.
  **Decision:** the family is its morphism `X -> S`. Flatness, properness and smoothness are additional properties, not consequences of naming it a family.
  Use torsion-freeness for the relevant module over a DVR only with the theorem's actual hypotheses; do not transplant it to arbitrary bases.
  **First specimen:** `xy=t` over `QQ[t]_(t)`, its generic fiber and nodal special fiber, followed by base change to `QQ[[t]]`. **Acceptance:** the same parameter map controls equations, differentials, fibers and flatness; a scalar-killed comparison detects nonflatness.
  Completion precision is absent from exact flatness and fiber claims.

- [x] **`formal-families`**. **Needs:** `completion-comparisons`, `sheaf-functors`. Construct formal neighborhoods and formal families as formal objects, retaining their algebraic comparisons.
  **Dependencies:** corrected ring/module completion and continuous maps.
  **Decision:** distinguish `Spec(A_hat)`, the formal spectrum, and the system of infinitesimal thickenings.
  Their point sets and categories are not interchangeable.
  An infinitesimal thickening is one finite stage.
  **Deliver:** the selected ideal of definition, compatible thickenings, formal restrictions, and morphisms justified by the topology.
  **Acceptance:** changing the finite computational order refines information without changing the formal object; compatible truncation data is connected to the completed algebra by actual maps.

- [x] **`singularity-classification`**. **Needs:** `normalization`, `local-module-maps`. Extend local singularity classification beyond selected coordinate normal-form recognition.
  **Owners:** `categories/schemes/singularities.py`, pointed local rings, completions, and established singularity algorithms.
  **Decision:** regularity and smoothness over a base differ; name which is decided.
  A normal-form label requires the appropriate equivalence and, when constructed, its coordinate-change morphism.
  Matching Milnor/Tjurina numbers alone is not a classification theorem.
  **Deliver:** supported coordinate changes, the correct equivalence notion, Jacobian/Fitting ideals under their hypotheses, and smooth/nonsmooth loci with the selected scheme structure.
  **Acceptance:** the same singularity in non-normal-form coordinates, a nearby non-equivalent example where invariants do not suffice, and a nonperfect-base case that separates regularity from smoothness.

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

- [x] **`transporters`**. **Needs:** none.
  Finish rational-integral transporters and cosets through the required external arithmetic operations.
  **Owners:** rational matrix groups, lattice stabilizers, `categories/orthogonal_quotients.py`, and `sage-indefinite-port`. **Deliver:** integral transporter between commensurable lattices and the remaining external arithmetic lifting theorem.
  Finite-character right-coset transversals and stabilizer double cosets now return live orthogonal-group lifts with explicit coset orientation.
  **Decision:** finite reduction computes the stated arithmetic object only after proving the invariant-lattice/denominator and lifting hypotheses.
  An arbitrary rational matrix group need not admit the required finite reduction.
  Specify the cases, rather than silently bounding denominators.
  **Acceptance:** lift each representative/transporter to an actual rational or integral morphism, verify its action on the lattice, and retain exact stabilizer inclusions and coset orientation.

- [x] **`centralizers`**. **Needs:** `transporters`. Extend centralizers from involutions to higher finite-order isometries and their equivariant orbits.
  **Deliver:** cyclotomic primary subspaces, their integral intersections, gluing subgroup, compatible isometry groups, and lifts to the full lattice.
  Account for the extra algebra/hermitian structure required on a cyclotomic component.
  **Decision:** the finite discriminant image is not the full arithmetic centralizer; independent isometries of the components need not preserve the gluing.
  Keep the commuting square with the distinguished isometry.
  **Acceptance:** a finite-order example with a nontrivial cyclotomic component and nontrivial gluing, plus decorated sublattice/flag orbit representatives and transporter morphisms.

- [x] **`reduction-complexes`**. **Needs:** `transporters`. Complete exact rational polyhedral and reduction-complex constructions.
  **Owners:** existing polytope/cone, pairing-configuration, and lattice-action owners; Normaliz, cddlib, PPL or the existing bridge computes polyhedra.
  **Deliver:** facets, extreme rays, incidences and face stabilizers; reduction cells and adjacent-cell morphisms; Lorentzian perfect-domain traversal and marked nonzero-norm vector transport.
  **Decision:** use the retained pairing and exact rational inequalities, not a floating-point picture or only a canonized incidence graph.
  **Acceptance:** adjacent cells share the actual face, their transporter sends one cell to the other, and the group-generation/completeness argument distinguishes a full domain from a finite exploration prefix.

- [x] **`witt-recursion`**. **Needs:** `parabolic-gluing`. Implement higher-Witt-index recursion and the `2U` Eichler construction through the existing isometry, discriminant and transporter owners.
  **Deliver:** complete the source-defined subgroup beyond the represented two `SL_2(ZZ)` actions, Eichler transformations, canonical `O(K)` lifts and finite covering representatives: supply the remaining discriminant lifts, recursive stabilizers, transporter completion to the full orthogonal group, and recursive lattice equivalence.
  **Decision:** state evenness/integrality conditions for every transformation.
  A subgroup generated so far is not the full orthogonal group until the generation theorem applies.
  A covering family is not automatically a set of distinct orbit representatives.
  **Acceptance:** explicit action morphisms and a completeness argument, with each recursive step decreasing the parameter its termination proof uses.

- [x] **`parabolic-gluing`**. **Needs:** `transporters`. Replace heuristic parabolic constructions by exact integral gluing.
  **Owners:** isotropic reductions, group actions and arithmetic groups.
  **Deliver:** the rational Witt decomposition with integral sublattices, unipotent kernel, gluing-preserving Levi image, lift obstructions and supported lifts, and the corresponding exact sequence.
  Construct the inductive flag-orbit double cosets in the actual image of the parabolic, not automatically in the whole orthogonal group of the reduction.
  **Decision:** primitive means the quotient by the submodule is torsion-free; a primitive vector can have pairing divisibility greater than one.
  Distinguish vectors, their rank-one sublattices, rational planes, and saturated integral sublattices throughout.
  **Acceptance:** a non-unimodular example where gluing restricts the Levi action, plus line/plane incidence with actual embeddings and transporters.

- [x] **`chambers`**. **Needs:** none.
  Finish the remaining Coxeter-poset and number-field Vinberg operations.
  **Owners:** `categories/coxeter_diagrams.py`, Vinberg invariants and the reflection-engine adapter.
  **Deliver:** maximal elliptic/parabolic subdiagram posets and the number-field root computation in its valid arithmetic regimes.
  The exact root-half-space chamber, dominant cone, positive-cone projectivization, Weyl group and lazy chamber complex are already delivered at their owners.
  **Decision:** retain root-to-diagram maps and exact edge/vertex weights; bounded search is not a nonreflectivity proof.
  Reuse projectively weighted graph objects and the current Vinberg/edge-walk implementations.
  The number-field operation remains a provider obligation rather than an integer algorithm with coerced coefficients.
  **Acceptance:** sourced finite, affine, noncrystallographic and hyperbolic literature examples distinguish the asserted regimes, and a supported totally-real number-field example returns roots over its actual integer ring.

- [x] **`arithmetic-applications`**. **Needs:** `witt-recursion`, `centralizers`, `reduction-complexes`. Assemble the three arithmetic research constructions with their maps.
  **Lorentzian:** `U + E8(-1)`, its orthogonal/component groups, cusp orbit, cusp stabilizer, unipotent radical and map onto the definite reduction group.
  **Higher Witt index:** `U + U(2) + E8(-2)`, with its represented line/plane orbits, stabilizers, full-orthogonal Tits-building incidence, and generic character-defined subgroup cusp/flag splitting with actual subgroup transporters, obtained by left-adjusting a full-orthogonal witness by the target stabilizer inside the finite character quotient; instantiate the intended `H <= O(A_L)` and retain the resulting application maps.
  **Equivariant:** the K3 lattice with an Enriques involution, its integral invariant/anti-invariant decomposition and gluing, full centralizer, polarization stabilizer intersection, and anti-invariant isotropic orbits.
  **Acceptance:** actual inclusions, projections, group maps and transporters, not a table of expected invariants.
  Their execution belongs to T.

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

The repository already entered terminal T and the checked `terminal-reference`, `terminal-execution`, and `terminal-repairs` nodes retain the evidence they established at their recorded revisions.  The later source audit in `COMPLAINTS.md`, however, found mandatory architectural violations that were not represented in the old DAG.  Those findings are now promoted into the required [complaint-driven architecture remediation](#complaint-driven-architecture-remediation) workstream below.

The phase rule therefore applies again while `architecture-remediation` is open: do not use Sage/tests/QC/notebooks to drive source authoring in that workstream.  Bank the corrected constructions and the specimens that will falsify them, then return to terminal execution.  The prior terminal evidence is not discarded, but it cannot certify source that changed afterward.

`terminal-session` is the re-entry boundary.  It depends on both the already-completed `terminal-repairs` work and the new `architecture-remediation` convergence node.  Once both hold, regenerate the live reference/graph as needed, execute the final public session/notebook surface, and run the prescribed final QC against the repaired architecture.

This keeps the two roles distinct: source-level architecture remediation is driven by the observed construction contract, while terminal execution decides whether the repaired public mathematics actually works.  Do not use a previously green terminal run to waive a newly observed source defect, and do not use an architectural audit finding as if it were already a runtime failure.

- [x] **`terminal-reference`**. **Needs:** none.
  *Required implementation and transfer are finished.* They mean the twenty-eight implementation nodes checked off in this file — `toric-cohomology`, `tor-ext`, `witt-recursion`, `arithmetic-applications` and the rest — and every one is closed.
  `optional-database` and `optional-engine` are optional by name and gate nothing.
  A repair you discover from here does not reopen that condition; if it did, the condition could never be met, because there is always one more repair to find.
  Generate the preamble reference and category/functor graph from the integrated source, then read them against the intended objects, maps and inherited operations.
  **Acceptance:** documentation describes that source and exposes the mathematical contracts.
  Generation success alone is not a correctness claim.
  Compare the integrated constructor, adapter, export and consumer contracts with `OWN-01` through `OWN-14`, including source-reviewed work no longer in this queue.
  Use the completed units' commits to locate evidence, then inspect the affected live routes after integration.
  Missing mandatory architecture is new concrete repair work at its owner, not a documentation rewrite declaring the weaker implementation acceptable.
  Do not turn this comparison into a source-policing test or a count of engine imports.

- [x] **`terminal-execution`**. **Needs:** `terminal-reference`. Execute the prescribed public-construction and mathematical suites in the terminal verification phase through the existing project recipes.
  **Scope:** expectation subtrees, ring/module/algebra/action contracts, completion versus truncation, geometric constructions and comparisons, transferred framework consumers, and the valid archive/literature specimens.
  Include the permitted construction-order/session tests on the integrated tree and notebook checks through `japi`. **Acceptance:** each claimed behavior is exercised through the actual public path.
  An unverified assertion, suite count, or backend-only test is not proof of the corresponding construction.
  Include the new localization/fraction-field route, genuine completion and its projections, shared complex and DGA boundary degrees, integral torsion, representative-independent products, toric weight-to-total maps, lazy owned constituents, and the nonidentity maps recorded with each integration unit.
  Reuse existing proof surfaces and preserve independent mathematical expected results.
  Engine call counts, mocked delegation, and checks of private helper spellings do not prove these obligations.

### The sage-categories pin is unresolvable, and the cause is in that repository

`pyproject.toml` pins `sage-categories @ git+https://github.com/dzackgarza/sage-categories.git@66efc15bf5050a527f1bb4ff3bff8542e3d83203`. That revision exists locally and is an ancestor of the producer's active `codex/functorial-core-kernel` branch, but it is not on any published `origin/*` ref.
Reverified 2026-09-14: local `main` and `origin/main` are both `10e14a53`; the active producer branch is `5660e01a`, **1577 commits ahead of `origin/main`**, and no remote branch contains the required `66efc15b` revision.
So the resolution failure `terminal-execution` recorded is not a defect in this repository and cannot be repaired from here by choosing another local producer revision; the required producer history has not been published to the GitHub route this dependency declares.

Do not work around it by switching to a filesystem path dependency.
That hides a publication gap that affects every consumer, and the declared route between these projects is GitHub.
Treat the pin as blocked, record it that way against the affected items in the observed failure set, and carry on with the 36 collection errors, which are this repository's own and are repairable here.

- [x] **`terminal-repairs`**. **Needs:** `terminal-execution`. Repair the mathematical owners exposed by terminal verification and establish the originally required behavior.
  **Observed terminal failure set (2026-09-13):** `terminal-reference` now generates `docs/preamble-megadoc.md` and the 327-category/94-functor preamble graph from a live Sage session.
  The declared `just graph` route is reproducible from committed `scripts/build_graph.py`. The 36 collection errors caused by missing public `preamble.all` construction names are also repaired and pinned by a direct public-import regression; collection now passes those former failures and reaches the independently blocked `sage-categories` import.
  `just test-push` cannot resolve the declared `sage-categories` revision `66efc15bf5050a527f1bb4ff3bff8542e3d83203`. A direct Sage 3.12 collection against the current local upstream checkout now collects 19,702 tests and reaches one upstream-only syntax error in `sage_categories/cat/category.py`. The archived Nikulin genus specimen no longer imports the retired `integrallattice` package path: it imports `Genus` from the live lattice owner.
  Remaining observed collection repairs are duplicate test-module basenames, group-algebra commutativity reaching an `OwnedArrowCategory` parent, and the missing `OwnedCategoryOverBaseRing` session export.
  A fresh category-suite execution then exposed a distinct group-Hom admission defect: an automorphism in `Aut(G)` was rejected as a morphism of `Grp` while checking abelianization-unit naturality.
  The group Hom owner now corestricts same-endpoint structured group homomorphisms through their retained GAP map; the abelianization naturality regression passes.
  The next category-suite failure was an obsolete assertion that `Modules(R[G])` is literally a subcategory of `Modules(R)`. The retained architecture correctly makes restriction along `R -> R[G]` a functor; the specimen now exercises that object/morphism restriction and keeps genuine form/lattice subcategory inclusions separate.
  Continuing the category suite exposed Hom admission rebuilding stronger structured arrows in a weaker Hom category; fixed Hom objects now accept same-endpoint arrows along the declared subcategory edge instead of re-verifying their presentation.
  This subsumes the earlier group-automorphism special case and lets the free-algebra functor reach its next independent arithmetic assertion.
  The archived wide-subcategory specimen also now uses the represented fixed-Hom object's explicit arrow object rather than incorrectly identifying that object with its underlying map; corestriction from a more specific core similarly retains the same forward and inverse arrows while changing the represented Hom parent.
  The construction-order session regression no longer reads Sage's private `_cmp_key` representation (a method on current join categories); it now compares the existing structural category-graph signature that the owned ordering itself is defined from.
  A toric construction then exposed join categories inheriting both an ordinary Hom and its stricter subobject Hom; fixed-Hom selection now removes inherited super-Homs and keeps the unique minimal arrow theory, while still rejecting genuinely incomparable Hom constructions.
  Generic `G`-objects then exposed two representation-boundary defects: Hom inheritance attempted to reuse a supercategory Hom whose endpoints that supercategory did not admit, and functor admission bypassed `GObjects.Mor` for represented action functors.
  Hom selection now inherits only from endpoint-admitting supercategories, the generic functor check uses each category's public `Mor` selector, and a `BG -> Set` action is wrapped as the represented functor-category object; the nontrivial `C2` swap action and its equivariant endomorphism pass.
  A concrete acted object is now forgotten before forming `Mor_C`: in particular an `R[G]`-module contributes its retained coefficient module to `Mod_R` rather than being incorrectly used as an `R`-module endpoint itself.
  The sign-module equivariant doubling map and its naturality square pass.
  Predicate subgroup specializations now thread the inherited `Subgroups(G)` datum as `supergroup=G` through the construction contract instead of hiding it behind a duplicate `containing_group` name; regular-action point stabilizers again construct with their actual ambient group.
  Finite `G`-set orbit and fixed-point functors are cached by the source category, so repeated `X.orbits()` calls retain one quotient object and orbit-indexed stabilizer families keep that exact index set.
  Character inner products now use the identity `conjugate(chi(g)) = chi(g^{-1})` inside the character/group owners instead of requiring a nonexistent generic complex-conjugation method on owned cyclotomic scalars; direct-sum irreducible constituents are recovered again.
  The default absolute Galois realization is now canonical per owned base field: repeated `AbsoluteGaloisGroup(K)` and `K.absolute_galois_group()` calls retain the same chosen closure/embedding object, while explicitly supplied realization data still construct their stated choice.
  Finite automorphism groups now enumerate through their retained GAP automorphism group and compose inside the same `Aut(G)` parent; `Aut(C8)` consequently exhibits all four involutions and `Aut(V4)` retains its noncommutative order-six multiplication.
  Kernels of finite represented group morphisms now take their order from GAP's exact kernel, and GAP subgroups of `Aut(G)` return through the automorphism-group subgroup constructor rather than a nonexistent Sage-group crossing; the conjugation maps for `S3` and `S6` recover the expected inner images.
  A fresh 2026-09-14 `just test-universe` run reports 485 proof-surface diagnostics.
  Per `DEV-34` and `DEV-49`, that aggregate is a review input, not the `terminal-repairs` denominator or scheduling queue: this node advances only from concrete failed propositions exposed by the prescribed terminal public/session executions.
  The two recorded session/notebook failures are no longer active.
  The preamble startup-display item was already cleared by a live `just sage-init-check`; on 2026-09-14 the main `H0_O_P1xP1_4_4.ipynb` setup cell was then executed in a fresh Sage kernel from the integrated tree and passed the projective framework's idempotent-installation regression with 209 registered patches and `unregistered external methods = {}`. Keep rechecking session failures against the live tree before treating a historical record as current.
  Preserve these propositions and repair their owners; do not edit expectations merely to reduce this list.
  **Decision:** do not weaken expectations to match an implementation, filter required failures, infer false from missing algorithms, or turn the failure list into unrelated architectural work.
  A mathematically incorrect expectation may change only under the exception in `AGENTS.md`, with the correction justified in its commit.
  **Acceptance:** the actual failed proposition is established and the affected downstream construction remains coherent.

- [ ] **`terminal-session`**. **Needs:** `terminal-repairs`, `architecture-remediation`, `research-sage-runtime`. Verify the required session/rendered examples and final contribution contracts after mathematical integration and complaint-driven architecture convergence.
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

- [ ] **`sheaf-descent-subcategory`**. **Needs:** `arrow-category-placement`, `cat-valued-placement`.
  **Goal:** Own a coverage on a category and the sheaf condition it defines, so that sheaves on \(C\) are the full subcategory of \(\mathrm{Presh}(C, D)\) cut out by descent.
  **Observed gap:** the descent condition exists in exactly one situation and as gluing data rather than as a definition: `DistinguishedAffineCover.glue_modules` assembles a module sheaf from charts and transition isomorphisms.  Nothing states the condition a presheaf must satisfy.
  **Owners:** the coverage on \(C\), the descent diagram it produces for a covering family, and the full subcategory of the presheaf category.
  A full subcategory of the presheaf category places its objects through the presheaf category's own construction, and today `_FunctorCategory` builds its objects as objects of `Arr(Cat)` (cat.py, `_object_on`), so nothing can be placed under it until the functor category owns its objects; that is the edge to the two placement nodes.
  **Deliver:** the sheaf condition as an equalizer over a covering family, the resulting full subcategory, and the existing affine gluing re-expressed as an instance of it rather than a parallel implementation.
  The gluing-data categories are placed by that instance: `DistinguishedAffineCovers` (schemes/ringed_spaces.py) is the category of covering families of an affine scheme under the coverage, and `ModuleGluingData(cover)` and `AlgebraGluingData(cover)` (schemes/gluing.py) are the descent-data categories of that covering family; all three declare `Objects()` today and decide membership by `isinstance`.
  **Separating cases:** a presheaf that fails descent on a two-element cover, and the same presheaf on the trivial coverage where it passes.  Keep the coverage a parameter: the reason for stating it this way is that stacks change the value category, not the condition.
  **Acceptance:** a presheaf and a sheaf on the same site are distinguished by the construction rather than by the caller's assertion; the affine module-gluing route returns an object of the sheaf category.

- [ ] **`sheaf-object-placement`**. **Needs:** `sheaf-descent-subcategory`.
  **Goal:** Place every sheaf in the tree as an object of the sheaf category, and declare the sheaf-bearing categories into the categories their own definitions name.
  **Observed gap:** `QuasiCoherentSheaves` (`schemes/ringed_spaces.py:541`) and `RingedSpaces` (`:642`) both declare `Sets()`.  A quasi-coherent sheaf is an \(\mathcal{O}_X\)-module and a ringed space is \((X, \mathcal{O}_X)\); neither is a set.  `StructureSheaf`, `AffineModuleSheaf`, `GluedModuleSheaf`, `GluedAlgebraSheaf`, `FiniteAtlasInverseImageModuleSheaf`, `InvertibleSheaf` and `HigherDirectImageSheaf` are plain `SageObject`s, so none inherits the abelian or monoidal structure `QuasiCoherentSheaves` documents, and `__contains__` has to duck-type its argument for want of a placement.
  **Owners:** the sheaf category from `sheaf-descent-subcategory`; the ringed space as a space together with its sheaf of rings; the affine equivalence with \(\mathbf{Mod}_A\) already implemented as `module_category`/`associated_sheaf`/`global_sections`.
  **Deliver:** the sheaves become objects with placements; the two categories declare their real supercategories; `QuasiCoherentSheaves.__contains__` asks for a placement instead of probing for an attribute.  Retain the affine equivalence and the Stacks Tag 01I8 statement it cites --- this node changes where the objects live, not what they are.
  **Acceptance:** the abelian and monoidal operations `QuasiCoherentSheaves` documents are reached through its declared supercategories rather than restated on it; no sheaf in the tree is outside the category graph.

- [ ] **`algebras-are-modules`**. **Needs:** none.
  **Goal:** An algebra built by `Algebras(R)(module, multiplication)` is a module object constructed through `Modules(R)`, so it answers its module operations by inheritance.
  **Observed gap:** `Algebras(R)` declares `Modules(R)`, but `Algebras._call_` (`algebras/algebras.py`) returns an object of the arrow category \(\mathrm{Arr}(\mathbf{Mod}_R)\) whose module is its `target_object()`, so `Algebras.ParentMethods` forwards `zero`, `module_generating_set`, `module_generator`, `module_rank`, `scalar_multiple`, `_selected_module_coefficients`, `__contains__` and `_element_constructor_` through `underlying_module()` behind an exact-module guard, and `AlgebrasWithChosenMultiplication.ElementMethods` wraps one module element.  The threaded route exists for associative multiplications only: `_algebra_from_multiplication` rebuilds the module through `_module_presented_by_multiplication` with the multiplication as construction data, received by `AssociativeAlgebrasWithChosenMultiplication.ParentMethods.__init__`.
  **Owners:** `Algebras(R)._call_`; `AlgebrasWithChosenMultiplication`, which takes the threaded `__init__` and the multiplication transport from its associative refinement; `_equip_unit`, which transports the unit along the equipping map; the algebra Hom classes selected by `GeneralAlgebraHomCategoryConstruction`.
  **Deliver:** `Algebras(R)(module, m)` constructs through the presented-module route for every bilinear `m`, associative or not; the forwarding block, the wrapper element class, the exact-module guard and the arrow-object branches of the algebra Hom classes are deleted with it; `underlying_module()` remains the functor \(\mathbf{Alg}_R\to\mathbf{Mod}_R\) obtained from its category.
  **Acceptance:** an algebra answers its module operations through `Modules(R)`; no operation `Modules(R)` provides is defined a second time in the algebra subtree.

- [ ] **`arrow-category-placement`**. **Needs:** none.
  **Goal:** `_ArrowCategory` is an object of `Cat`, which is what its own definition \(\mathrm{Arr}(C) = \mathrm{Fun}([1], C)\) says it is.
  **Observed gap:** `abstract_categories/arrow_categories.py:156` states the functor-category definition in its docstring and declares `Objects()`, the root, so an arrow object inherits nothing from the functor category its definition names.  The functor category's own objects are built as objects of `Arr(Cat)` (`cat.py`, `_FunctorCategory._object_on`), so the two constructions currently define each other; one must become primary before `Arr(C)` can be declared into `[1] \to C`.
  **Owners:** `Cat`, and the owned functor category.
  **Acceptance:** the arrow category is reached as the functor category \([1] \to C\) rather than declared alongside it; its placement is in `Cat`.

- [ ] **`geometric-space-placement`**. **Needs:** `sheaf-object-placement`.
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

- [ ] **`cat-valued-placement`**. **Needs:** `arrow-category-placement`.
  **Goal:** Every category-of-categories construction is an object of `Cat`: `_FunctorCategory`, `_OppositeCategory`, `_ProductCategory`, `ClassifyingCategory`, `DiscreteCategory`, `ImageOfFunctor`, alongside `HomCategories` (done, 61bd8c65) and `_ArrowCategory`.
  **Observed gap:** each declares `Objects()`; the sets sweep left them because their `super_categories` describe their objects rather than the category, the same circularity `arrow-category-placement` records (`[1] -> C` builds its objects as objects of `Arr(Cat)`).
  **Acceptance:** one construction is primary, and every one of these categories is placed in `Cat` by it.

- [ ] **`membership-by-placement`**. **Needs:** none.
  **Goal:** No `__contains__` decides membership by a predicate (`CAT-23`).
  **Observed gap:** `Schemes.__contains__` answers lower-base membership by walking the candidate ring's base tower (schemes/schemes.py), so `X in Schemes(ZZ)` is true for a QQ-scheme that inherits nothing from it; `Sets.Countable.Infinite` decides membership by cardinality (a6078850); `QuasiCoherentSheaves.__contains__` duck-types (owned by `sheaf-object-placement`).
  **Acceptance:** each such membership is answered by placement at construction or through the functor of `CAT-16`; the predicates are gone.

- [ ] **`mor-spelling-convergence`**. **Needs:** none.
  **Goal:** `X.Mor(Y)` is the only spelling of a category of morphisms in the preamble universe (CONTRIBUTING, *`Mor` is the only spelling the preamble universe ever uses*; AGENTS.md banned-language index). `Hom` names Sage's construction and occurs only inside a private adapter that calls Sage.
  **Observed gap:** 59 public `Hom`/`Homs()` spellings in 24 files under `src/dzack_research/preamble/` on 2026-09-16, beside 1014 `Mor` spellings; 373 definitions whose names contain `hom` (`HomCategories`, `_hom_endpoint`, `module_homset`, ...), which realize the owned `Mor` constructions under Sage's name. The conversion was started once and interrupted (CONTRIBUTING `DEV-48`).
  **Owners:** the owned `Mor` construction on each category and the Hom-category types it generates; the private Sage boundary that constructs Sage's `Hom` for computation.
  **Deliver:** every public spelling becomes `X.Mor(Y)`; every owned definition named for Sage's construction is renamed for the owned construction it realizes, or moved behind the adapter if it is the Sage call; the conversion is carried through the whole tree before any run (`DEV-48`).
  **Acceptance:** `rg '\.Hom\(|\bHoms\(\)' src/dzack_research/preamble` finds only adapter sites that call Sage; the expectation subtrees' `Mor` spellings resolve.

### Owner API and construction data

- [x] **`owner-api-convergence`**. **Needs:** none.
  Remove the public/global operation language forbidden by `ARC-12`, `API-07`, `STY-01`--`04`, and `OWN-02`.
  **Observed gap:** `preamble.all` still exports construction verbs such as products, coproducts, tensor products, kernels/cokernels, pushouts, localizations, completions, and quotients as free functions; the audit also found 261 exported owner-in-argument functions across 107 files.
  **Owners:** the actual category/object/morphism/Hom/functor that determines each operation; `preamble.all` is only the session aggregator and must not become a second operation registry.
  **Deliver:** migrate every ordinary source/notebook/test consumer of each removed global to the mathematical owner spelling; retain notation only when it delegates to that owner.  Delete compatibility exports rather than preserving aliases whose only purpose is the old route.
  **Non-goal:** do not mechanically turn every module-level function into a method.  A genuine constructor whose inputs do not already contain its mathematical owner may remain a constructor; decide by the operation's mathematics, not syntax.
  **Acceptance:** a source/export audit finds no free-standing public operation whose owner is already supplied as an argument; `from dzack_research.preamble.all import *` exposes mathematical objects/categories and deliberate session vocabulary but not a duplicate operation catalogue; the negative test surface needed by `ownership-test-contract` can distinguish the removed route.


- [x] **`framing-primary-epi`**. **Needs:** none.
  Rebuild framed-module construction around the selected epimorphism `Free_R(S) -> M` as the defining datum required by `CON-11`, `OWN-03`, `ARC-20`, and `STY-152`.
  **Observed gap:** generic framing currently stores a generating set/function and reconstructs `Free_R(S)` and the generator map later when `framing_morphism()` is queried.
  **Owners:** generic framed modules, the free-module functor/unit, and the represented module morphism/Hom owner.
  **Deliver:** construction receives or canonically constructs the actual owned source `Free_R(S)` and selected epi before the framed module is exposed; the indexing set is the free source's defining set, and `module_generator(s)` is the image of its free generator.  `framing_source()`, `module_generating_set()`, `module_generator()`, and `framing_morphism()` are projections of that one datum.
  **Separating cases:** a framed quotient whose selected generators satisfy relations, a framed free module where the epi is an isomorphism, and a framing with labels that are not positional integers.  Do not silently strengthen every framing to a basis or ordered enumeration.
  **Acceptance:** generic framed modules plus the first framed-free and presented-module consumers retain one actual framing object; no public framing accessor allocates a new free module or reconstructs a morphism from stored label metadata.

- [x] **`framing-specialization-convergence`**. **Needs:** `framing-primary-epi`.
  Remove duplicated framing/generator implementations from lattice, fractional-ideal, presented-module, framed-free, group-module, restricted-scalar, matrix-module, and number-field specializations (`OWN-14`, `STY-154`).
  **Observed gap:** the audit found nine independent `module_generators()` implementations and several descendant-specific framing reconstructions.
  **Deliver:** each specialization inherits or composes the general framing datum and introduces only genuinely stronger mathematics.  A lattice may provide lattice-specific structure on its generators only when that returned object actually has extra lattice semantics; otherwise its module generators are the same module-theoretic image inherited from the underlying free module.
  **Acceptance:** one framing authority supplies source, selected epi, generator set and generator evaluation across the audited descendants; specialization methods that remain have a documented stronger codomain/operation and are not renamings of the generic result.

- [x] **`owned-provenance-data`**. **Needs:** none.
  **Goal:** Represent chosen source maps, presentations, base changes, completions, and comparison morphisms as first-class construction data instead of hidden `_preamble_*` provenance attributes.
  Replace hidden `_preamble_*source*`, functor-preimage, coordinate-morphism, and provenance side channels with first-class construction data (`CON-05`, `STY-07`, `OWN-03`--`05`).
  **Observed gap:** the audit found 108 attachment/provenance sites across 32 files, including functor-image preimages, de Rham/Kahler/cohomology source attributes, coordinate-algebra morphisms, completion sources and base-change sources.
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

- [x] **`generator-lexicon`**. **Needs:** `framing-specialization-convergence`.
  Remove implementation-role display language such as `"Module-generator family"`, `"Free-module generator family"`, `"Presented-module generator family"`, and `"Lattice-generator family"` (`LEX-01`, `LEX-04`).
  **Observed gap:** public displays currently describe an `IndexedFamily`/refinement role instead of the mathematical set or its image.
  **Deliver:** display the actual selected generator set/image, a bounded mathematically meaningful view for infinite sets, and any truly distinguishing chosen structure.  The object returned by `module_generators()` must look like module generators, not like the Python/category mechanism used to store them.
  **Acceptance:** finite free/lattice examples show their generator image (for example `{e_0, e_1}` or an equally informative owned-set rendering); infinite examples preserve laziness and expose the indexing mathematics without implementation taxonomy; no audited generator display is merely a renamed type.

- [x] **`ambiguous-generator-names`**. **Needs:** `framing-specialization-convergence`.
  **Goal:** Replace bare `gens`, `basis`, `dual`, and similar names with structure-qualified operations whose mathematical codomain is clear from the name itself.
  Remove public bare `gens`, `generators`, `basis`, `dual`, and `ngens` spellings where `LEX-02`, `LEX-10`, and `STY-127` require the structure-qualified referent.
  **Observed gap:** current examples include fractional-ideal/lattice `gens`, lattice/isotropic `basis`, and six divisor/sheaf `dual()` methods.
  **Deliver:** choose names such as `module_generators`, `group_generators`, `ideal_generators`, `lattice_basis`, `dual_module`, `dual_lattice`, `dual_sheaf`, etc. according to the actual codomain; remove aliases that preserve the ambiguous spelling and migrate every ordinary consumer in the same unit.
  **Acceptance:** each audited public name identifies what is generated/dualized/based without knowing the receiver's implementation class, and no banned bare alias remains on the public surface.

- [x] **`categorical-representation-convergence`**. **Needs:** none.
  Collapse parallel representations of equivalent categorical/universal data into one authoritative representation (`ARC-14`, `STY-51`, `STY-54`).
  **Observed gap:** contravariant functors are independently modelled instead of ordinary functors from an opposite category; bifunctors duplicate product-domain functor machinery; adjunctions independently require unit, counit, and both Hom transposes.
  **Owners:** `Functor(C^op,D)`, functors out of product categories, natural transformations, adjunction/unit-counit data, and the common Hom/universal-construction calculus.
  **Deliver:** choose the standard categorical datum at each site and mechanically derive equivalent views.  Compatibility accessors may expose a mathematically distinct view only when computed from the authoritative datum; subclasses must not prove mutually determining data twice.
  **Acceptance:** constructing one representation determines the others, round-trips agree by construction, and no audited categorical object can be made internally inconsistent by supplying incompatible equivalent data.

- [x] **`owned-product-codomains`**. **Needs:** `categorical-representation-convergence`.
  Replace public bare tuple/list products with elements of the appropriate owned product (`CON-15`, `SET-01`, `CAT-08`).
  **Observed gap:** commutative-square components, naturality-square morphisms, and tensor index-module/index pairs currently return Python tuples.
  **Deliver:** identify the index set and factor family for each operation, construct or reuse the corresponding owned product, and return its element.  Preserve named projections/components so callers do not unpack storage positions to recover mathematics.
  **Acceptance:** the audited public signatures contain no bare Python tuple/list return for mathematical product data; component access factors through the owned product/projections and works for the stated index object rather than only a hard-coded pair.

- [ ] **`mathematical-return-types`**. **Needs:** `owner-api-convergence`, `framing-specialization-convergence`, `refinement-convergence`, `categorical-representation-convergence`, `owned-product-codomains`.
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

- [x] **`group-module-scalar-change-convergence`**. **Needs:** `categorical-representation-convergence`.
  Make group-module scalar extension/restriction one construction whose object and morphism actions are owned once (`STY-54`, `OWN-09`, `OWN-14`).
  **Observed gap:** object-level `base_change` transports the action while `GroupModuleScalarExtensionFunctor` separately owns morphism transport and construction knowledge.
  **Deliver:** select the mathematical owner (normally the scalar-change functor/construction); make the convenience object method delegate to it or vice versa, with one retained source/target ring map, group action and induced morphism law.
  **Acceptance:** object and morphism transport are two actions of the same retained functor/construction, not parallel algorithms, and a nonidentity group-module map commutes with scalar change through that one owner.

- [x] **`memoization-convergence`**. **Needs:** `owned-provenance-data`.
  **Goal:** Give constructions such as de Rham algebras, Kähler differentials, cohomology, and absolute Galois groups one shared identity/caching mechanism keyed by their defining mathematical data.
  Replace theory-local identity caches for de Rham algebras, Kahler differentials, cohomology, cohomology algebras, and absolute Galois groups with the common identity/lifetime mechanism (`STY-55`, `DEV-12`, `OWN-10`).
  **Observed gap:** five independent dictionaries encode construction identity and lifetime.
  **Deliver:** after chosen provenance is first-class, use the appropriate shared unique-representation/cached-function/cached-method owner keyed by the defining mathematical data.  Do not cache by display strings or backend handles and do not use a cache to invent identity between different chosen presentations.
  **Acceptance:** repeated construction with identical defining data retains the documented identity; genuinely different choices remain distinct; no audited theory keeps a parallel identity dictionary.

- [ ] **`singular-kernel-delegation`**. **Needs:** `framing-primary-epi`, `assertion-frontiers`.
  **Goal:** Delegate finitely presented module kernel/syzygy computation to a maintained Sage/Singular operation through one adapter, then raise the result to the owned kernel object, inclusion, and presentation.
  Replace `_singular_presentation_kernel`'s long Python orchestration with a maintained Singular/Sage operation behind one owned adapter crossing (`ENG-01`--`03`, `STY-57`--`59`, `OWN-08`).
  **Observed gap:** current code manually builds matrices, lifts coefficients, invokes Singular `modulo`, reconstructs relations and recovers lifts across roughly 170 lines.
  **Deliver:** identify the exact maintained kernel/syzygy/presentation operation that returns enough data to reconstruct the owned kernel inclusion and selected presentation.  Keep representation conversion at the adapter boundary; do not reproduce the standard algorithm in Python around lower-level Singular calls.
  **Acceptance:** a nontrivial finitely presented module morphism obtains its kernel object, inclusion and presentation through one maintained-engine computation and raises every constituent to owned mathematics; unsupported coefficient regimes stop at the declared frontier rather than falling back to the old orchestration.

- [x] **`torsion-action-delegation`**. **Needs:** none.
  Route torsion-form orbit/stabilizer computation through the general owned action/G-set infrastructure, with GAP private beneath that owner (`ENG-01`, `STY-40`--`42`, `BND-01`--`02`).
  **Observed gap:** torsion-form modules contain both a hand-written orbit traversal and direct `libgap.Orbit`/`Stabilizer` calls.
  **Deliver:** represent the relevant finite action once, expose orbit/stabilizer through the action/G-set owner, and let that owner select GAP where appropriate.  The torsion-form layer supplies the mathematical set/action and consumes owned orbit/stabilizer objects; it does not own traversal or GAP calls.
  **Acceptance:** representative torsion-form subobject orbits/stabilizers agree with the retained action, return through the general owned action API, and the torsion-form subtree contains no independent orbit engine.

- [ ] **`imperative-algorithm-cleanup`**. **Needs:** `group-module-scalar-change-convergence`, `singular-kernel-delegation`, `torsion-action-delegation`.
  **Goal:** Replace generic local traversal, grouping, multiplication, and accumulation code with standard mathematical operations or mature dependency owners, retaining loops only when they are genuinely theory-specific algorithms.
  Remove the remaining guide-catalogued imperative algorithms only after their larger duplicated owners have converged.
  **Observed gap:** examples include bilinear nested accumulation, duplicate free-algebra target multiplication loops, divided-power coefficient loops, absolute-Galois append/filter construction, `setdefault(...).append(...)` grouping, and bespoke `frontier`/`seen` traversals in lattice/action code.
  **Deliver:** for each audited site, identify the standard mathematical operation or mature dependency owner and replace the local algorithm with that operation.  When an explicit loop is genuinely the theory-specific algorithm, retain it and document the mathematical reason rather than rewriting it cosmetically.
  **Acceptance:** every occurrence family named by the complaint has been adjudicated; removed sites delegate to a real owner, and retained loops are demonstrably special mathematics rather than generic grouping/traversal/multiplication infrastructure.

### Public interaction and proof surfaces

- [ ] **`coordinate-firewall`**. **Needs:** `framing-specialization-convergence`.
  **Goal:** Confine coordinates and raw matrices/vectors to explicitly chosen finite framings or presentations; ordinary lattice/module/morphism interaction should remain semantic.
  Close ordinary public coordinate/storage escape hatches that bypass semantic owners (`ARC-18`, `API-02`, `DEV-40`).
  **Observed gap:** lattice elements expose `to_list`/`to_tuple`/`to_vector`, tensor elements expose raw `components()`/`list()`, and module morphisms expose matrix storage as ordinary public interaction; the canonical notebook teaches these routes.
  **Deliver:** keep explicit coordinate views only on the selected finite framing/presentation object where coordinates are mathematically part of that chosen datum.  Ordinary element/morphism APIs route through owned operations, Homs and universal constructions; downstream research code migrates before the old hatches are removed.
  **Acceptance:** a user cannot bypass the semantic object merely by calling an equally public raw-storage method; the retained finite-coordinate boundary names the framing/presentation that makes the coordinates meaningful and distinguishes it from unframed/infinite cases.

- [x] **`ownership-test-contract`**. **Needs:** `owner-api-convergence`.
  Replace the compatibility behavior in `tests/conftest.py` and old-global test consumers with behavioral proof of the owner API (`DEV-06`, `DEV-37`, `DEV-43`, `STY-118`, `STY-125`).
  **Observed gap:** the harness claims global operations are absent but uses `setdefault` injections that leave existing forbidden exports untouched; 135 old-global call sites and 51 star-importing test files mean a green suite can coexist with the violation.
  **Deliver:** remove the compatibility injection, migrate tests to the owner spelling, add a negative public-surface assertion that fails when a forbidden owner-in-argument global is exported, and keep mathematical expectations independent of implementation helper names.
  **Acceptance:** the old global route makes the relevant test fail, while the owner route exercises the same mathematical construction; no test harness mutation silently supplies or preserves the API being removed.

- [ ] **`canonical-notebook-contract`**. **Needs:** `owner-api-convergence`, `generator-lexicon`, `ambiguous-generator-names`, `categorical-representation-convergence`, `coordinate-firewall`.
  **Goal:** Turn the canonical notebook into an executable research narrative organized by mathematical questions and witnesses, using the same final public API expected from ordinary users.
  Repair the canonical notebook to satisfy `NB-01`--`05`, `ARC-07`, `LEX-10`, and `DEV-40` after the public APIs it teaches have converged.
  **Observed gap:** 30/51 code cells are unexecuted, committed failure output remains, several mathematical claims occur only in prose, section headings are implementation tours, and examples use old globals/ambiguous generator APIs/raw constructors and coordinate paths.
  **Deliver:** organize sections by mathematical questions; express claims as computations/assertions/witness displays; use the same owner-method/Hom/functor/session syntax expected from ordinary researchers; remove stale output and compatibility-layer examples.  Preserve useful research content rather than turning the notebook into a policy demonstration.
  **Acceptance:** every substantive claim in the audited notebook is executable or visibly witnessed, no committed traceback remains, and no example depends on an API prohibited by the upstream remediation nodes.  Actual execution is deferred to `terminal-session`.

- [ ] **`architecture-remediation`**. **Needs:** `mor-spelling-convergence`, `group-objects-construction`, `cat-valued-placement`, `membership-by-placement`, `sheaf-descent-subcategory`, `sheaf-object-placement`, `algebras-are-modules`, `arrow-category-placement`, `geometric-space-placement`, `combinatorial-object-placement`, `owner-api-convergence`, `framing-primary-epi`, `framing-specialization-convergence`, `generator-lexicon`, `ambiguous-generator-names`, `owned-provenance-data`, `refinement-convergence`, `assertion-frontiers`, `placeholder-stubs`, `categorical-representation-convergence`, `group-module-scalar-change-convergence`, `memoization-convergence`, `singular-kernel-delegation`, `torsion-action-delegation`, `imperative-algorithm-cleanup`, `owned-product-codomains`, `mathematical-return-types`, `coordinate-firewall`, `canonical-notebook-contract`, `ownership-test-contract`.
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

- [x] **`optional-display`**. **Needs:** none.
  Add further notebook/rich-display examples only for a named research question using live objects.
  Use existing polygon, Three.js, and diagram rendering owners; do not install implicit global display hooks.

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
