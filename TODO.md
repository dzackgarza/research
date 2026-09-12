# Preamble TODO

## Execution priorities

Build the remaining general scheme-theory toolkit from the current
`src/dzack_research/preamble/` tree. Complete shared mathematical dependencies
before extending their consumers. Geometry has priority over independent
arithmetic applications; an arithmetic computation moves earlier only when a
named geometric construction needs its result.

This is an executable work list, not a record of past work. Remove an item when
its stated work is delivered; retain only its unfinished obligations if delivery
is partial. Completion evidence belongs in the implementation commit and its
mathematical specimens. Do not append completed rows, release histories, audit
transcripts, or an overall-progress table.

The requirements below specify new deltas from existing constructions. A source
path identifies where to extend or repair, not an instruction to recreate that
subsystem. Inspect the live constructor and its consumers before editing.
Uncertainty explicitly assigned to a source review is not a claim of a runtime
failure. The pending terminal verification applies to the entire implementation,
including constructions no longer listed as implementation work.

Follow [CONTRIBUTING.md](CONTRIBUTING.md), especially `DEV-50` through `DEV-59`.
Begin new additions with its
[mathematical dependency trace](CONTRIBUTING.md#mathematical-dependency-tracing),
before selecting an implementation. Record observed missing foundations and
papercuts in [COMPLAINTS.md](COMPLAINTS.md), including independent discoveries.
That file owns the observed need and evidence; this queue owns the selected
remaining repair and its acceptance. Link them instead of copying status.
The [design philosophy](CONTRIBUTING.md#preamble-design-philosophy) and
[architecture specification](CONTRIBUTING.md#preamble-architecture-specification)
govern how every item is implemented, including already-existing dependencies.
The intended result is one recursively owned mathematical language composed
from shared constructions and maintained computations, not a larger local CAS.
Read the generated `docs/preamble-megadoc.md` before preamble implementation
under the governing `AGENTS.md` prerequisites. This queue does not authorize
running preamble tests, QC, Sage, or notebooks before terminal T.

### Select from the live dependency graph

The queue is the scheduling surface. Recompute the ready frontier from the current rows
before selecting work; do not preserve dated frontier counts or a private list of what was
ready in an earlier turn:

```sh
grep -nE '^- \[[ x]\] \*\*`[a-z0-9-]+`\*\*\. \*\*Needs:\*\*' TODO.md
```

Take the ready frontier in dependency order and carry each selected node through delivery
before moving on. A node that closes unblocks its dependents; a node that merely grows does
not. This repository has one worker, so selection has no claim or reservation layer.

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
- [Final verification](#final-verification)
- [Optional research consumers](#optional-research-consumers)

### Execution decisions for every item

Apply these decisions inside the selected unfinished item, not in a separate
audit, readiness registry, or new planning system. Their durable authority is
`OWN-01` through `OWN-14` and `DEV-50` through `DEV-59` in CONTRIBUTING.

1. **Select a remaining mathematical delta.** First express the requested
   addition in standard mathematics and recursively unfold its dependencies
   through the source-backed set-theoretic and categorical foundations. Separate
   defining mathematics from computational choices and related extensions.
   Then read the live owner, its immediate structure, the complete relevant
   methods, and its callers before changing it. Record actual gaps under
   `DEV-59`, linking the complaint to the relevant repair rather than using a
   missing method name as the mathematical specification.
   Preserve supplied capabilities. A source-review task below is a question to
   settle, not an assertion that the whole subsystem is broken. If the current
   source already meets it, remove the stale task with source evidence in the
   commit; retain terminal-T execution where still owed (`DEV-50`, `OWN-12`).
2. **Decide the route before adding computation.** Name the sanctioned entrypoint,
   defining objects and maps, reusable owned operations, and private computation
   owner in the selected item's contract. Use the existing declaration for the
   durable result (`OWN-02`, `OWN-13`). An owner path in this queue is a place to
   inspect, not permission to call every importable factory or private method.
   For a specialization, name the actual general construction it inherits or
   contains and the operations delegated to it (`OWN-14`). A shared name or an
   isomorphic result does not establish that implementation relationship.
3. **Resolve the actual upstream capability question.** Read the applicable
   maintained operation's input and result contract, including representatives,
   maps, hypotheses, and precision. Record the selected operation and remaining
   integration in the item while it is open, then at the adapter declaration.
   Where this queue names candidates, selection is unresolved work, not license
   to implement the computation from scratch (`OWN-08`, `ENG-06`).
4. **Repair one prerequisite with its real consumer.** Missing inherited data,
   constructor recursion, inaccessible maps, or awkward engine output belong at
   the owner that should provide them. Complete that repair and route the selected
   consumer through it; do not create a consumer-specific substitute or prebuild
   unrelated foundations. The first release includes an actual mathematical
   construction, not just an abstract interface (`OWN-03`, `OWN-07`, `OWN-11`).
5. **Preserve the full public object.** Retain coefficients, component modules,
   indexing objects, actions, maps, representatives, and results of subsequent
   arithmetic as owned mathematics. Transport through the existing functors with
   their preservation hypotheses. A new wrapper, accessor, category label, or
   private helper does not discharge these obligations (`OWN-04` through `OWN-09`).
6. **Close against construction and computation together.** Read the complete
   selected route and affected alternative routes, including inherited methods,
   notation, catalogue construction, and raising. Deliver distinguishing
   mathematical specimens and the required consumer changes. Commit specimens
   unexecuted until T. Neither matching dimensions nor replacing a local loop
   with a lower-level library call establishes architectural completion (`OWN-12`).

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

These routes address the integration errors discussed in the
[sage-categories complaints](https://github.com/dzackgarza/sage-categories/blob/main/COMPLAINTS.md)
without importing their historical findings as current preamble defects. Read
the relevant upstream contract at selection; a package catalogue is a discovery
lead, not evidence that every coefficient regime or map is implemented.

### Workstreams

Select a concrete unchecked construction below, not an entire row. Scores follow
[COMPLEXITY.md](COMPLEXITY.md); they measure the responsibility for the named
boundary, not its line count or duration. Reassess a bounded implementation once
its input contracts are settled.

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
| T | All required implementation, integration, and source consolidation below | Executed mathematical evidence and repairs of the failures it exposes | 15 for execution; score each resulting repair at its actual owner |

### Remaining workstreams as a dependency graph

The executable DAG is defined by the unchecked items below, not by the
workstream table or section order. Each item begins with a unique stable
mathematical ID and a **Needs** list of immediate unfinished prerequisites.
`A` in `B`'s Needs means the edge `A -> B`: deliver A's required output before
completing B. `none` means no unfinished queue prerequisite, not no mathematical
foundations. Existing constructions and external input contracts remain in the
item's body; inspect them at selection. All listed prerequisites are conjunctive.

Keep this one edge source. Do not maintain another hand-written graph, status
table or dependency registry. A visualization, if needed, is generated from the
items. Cross-references explain requirements; they do not create extra edges.
If prose requires an unfinished output, reflect it in Needs or explicitly place
the mutually dependent obligations in one coherent node. Do not conceal cycles
behind words such as "with", "later", or "integration".

Select a node with no remaining prerequisites, subject to the existing geometry
priority and active file reservations. Priority is a preference among ready
nodes, not an edge. File conflicts, shared owners, and related mathematical
subjects are not dependency edges either. Completion does not block ordinary
geometry that does not use it; an unrelated arithmetic gap does not block
geometry. Repair a newly discovered prerequisite at its owner and record the
actual dependency before extending its consumer.

An edge names the output described by its prerequisite's acceptance contract.
When only an independently deliverable part is needed, split that concrete
output into its own node, transfer its obligations intact, and redirect only
the affected edges. Do not force a consumer to await an entire broad workstream.
Do not remove an edge because its prerequisite is inconvenient, deferred, or
merely represented by a class. The generic universal-construction node delivers
real module constructions first; completion then owns integrating that contract
with its ideal-power system and maintained series realization. The general
construction does not wait for completion's implementation.

Before committing a queue change, check that every checkbox has exactly one ID
and one Needs list, IDs are unique, all references resolve, no self-edge or cycle
exists, and every required implementation node reaches `terminal-reference`
before T. During T, newly exposed repairs must reach the still-open terminal
node whose acceptance requires them. The terminal nodes form their own final
chain. No required or terminal node may depend on an optional node. Optional
work must name its concrete consumer and
dependencies before implementation; a required engine repair belongs in the
required consumer's dependency path, never in the optional branch.

Remove a delivered node and its incoming/outgoing edge references in the same
queue transaction, after inspecting the delivered output. Preserve unfinished
residue under its ID, or split it without dropping any obligation. An absent ID
is never an implicit completion record: dangling references are errors to
reconcile against source and git evidence. Keep completed history in commits.
Repairs and re-execution within terminal verification do not create a back-edge
to an earlier terminal node. New failure-specific work becomes a prerequisite
of the still-open terminal repair or final-verification node, with the required
re-execution in its acceptance. Preserve the phase-T execution rules.

## Completion and local algebra

Paths in this section are relative to
`src/dzack_research/preamble/categories/`.

### Localization specializations through one construction

- [x] **`localization`**. **Needs:** none.
  Route fraction fields and their maps through the existing localization
  owner, and close the affected specialization paths.
  **Owners:** `rings/ring_foundation.py::OwnedRings.ParentMethods.fraction_field`,
  `OwnedIntegralDomains.ParentMethods.fraction_field_map`,
  `rings/commutative_algebra.py::_localization_at_submonoid`, and the existing
  submonoid, ring Hom, and module-localization owners.
  **Observed gap:** see the
  [localization complaint](COMPLAINTS.md#localization-must-define-its-fraction-field-specialization)
  for the inspected specialization bypass and mathematical dependency trace.
  Preserve the existing general localization and element/prime routes.
  **Decision:** the domain's nonzero-element submonoid defines this specialization.
  The private Sage fraction-field operation remains a computational realization,
  but raising must establish that localization datum, its source map, and its
  universal factorization. Selecting the fraction-field realization must not
  call the public fraction-field method again during construction.
  **Integration:** extend the existing submonoid dispatch with this represented
  case, not a second localization class or a finite enumeration of nonzero
  elements. Review field inputs, prime complements, element-generated submonoids,
  and the number-field specialization against the same declaration. Preserve
  canonical field identities while retaining the map from each original source;
  do not attach source-dependent state to a shared field singleton.
  **Required consumer:** module scalar extension along the resulting fraction
  map uses the existing module-localization/scalar-change functor. Inspect every
  caller of the changed fraction-field and localization-map contracts and adjust
  dependent callers in this unit, without rebuilding unaffected local algebra.
  **First specimen:** the fraction field of `ZZ` and its source morphism, with
  numerator/denominator interpretation and the induced map of a module.
  **Separating specimens:** `ZZ[1/2]` and `ZZ_(3)` retain different unit behavior
  from `QQ`; a ring with zero divisors requires its total quotient-ring operation,
  not the fraction-field operation. Locality is justified for prime localization,
  not for all submonoids.
  **Acceptance:** direct owned construction, the fraction-field method, and
  scalar-change consumption establish the same semantic contract and comparison
  maps. Source review confirms the retained maintained arithmetic and absence of
  a bypass; specimens exercise owned elements, submonoids, and morphism endpoints.
  Follow the [construction factorizations](CONTRIBUTING.md#required-construction-factorizations),
  `OWN-02`, `OWN-07`, and `OWN-10`; do not infer constructor convergence from
  equality of printed rings or impose a general submonoid-equality algorithm.

### Completion objects and finite approximations

- [x] **`module-completion`**. **Needs:** none.
  Make finite-module completion consume the corrected ring completion and
  construct its functorial maps.
  **Owner:** `modules/framed/finitely_generated/finitely_presented_modules.py`,
  module scalar change, and the existing ring completion owner.
  **Reuse:** use the existing scalar-change functor on the supplied module
  presentation and its morphisms. Resolve any missing coefficient transport at
  that owner. Module completion must not implement another tensor product,
  relation reducer, or precision convention independent of the ring completion.
  **Decision:** use `M tensor_R R_hat` as completion for finite modules over
  a Noetherian ring, with the canonical comparison to the inverse limit and
  exactness justified by [Stacks 00MA](https://stacks.math.columbia.edu/tag/00MA).
  Keep the general completion definition separate from that theorem; finite
  presentation alone does not authorize every Noetherian exactness claim.
  **Deliver:** the completed module, canonical map into its scalar restriction,
  completed nonidentity morphisms, and `M_hat -> M/I^n M` with transitions.
  Preserve the selected presentation and transport maps without treating its
  framing as a basis.
  **First specimen:** multiplication by `x` on the free rank-one module over
  `QQ[x]` remains injective after `(x)`-adic completion. Multiplication
  by `x` on `QQ[x]/(x^N)` has a nonzero kernel.
  **Acceptance:** the implementation distinguishes those maps and realizes the
  completed exact sequence with cokernel `QQ`. Repeat the free-module
  construction over `QQ[x,y]` completed at `(x,y)`, so the multivariable
  route cannot escape the same obligation. Also use a free-plus-torsion
  module; an already annihilated torsion example alone cannot test completion.

- [x] **`quotient-completion`**. **Needs:** `module-completion`.
  Implement quotient/completion comparisons with hypotheses and actual maps.
  **Owner:** ring quotient, module quotient, and completion functors.
  **Decision:** in the Noetherian finite regime, construct the comparison
  between completing a quotient and quotienting the completion by the extended
  ideal/submodule. Derive it through completed maps and cokernels.
  Retain closure requirements outside that regime; do not identify a quotient
  by an arbitrary nonclosed submodule with a completed quotient.
  **Specimen:** complete `QQ[x,y]/(xy)` at `(x,y)` by both supported
  routes. Match the images of `x,y`, their product, projections to several
  orders, and the maps from the original algebra.
  **Acceptance:** an explicit comparison isomorphism, not matching dimensions
  or a pair of parents with similar printed equations.

- [x] **`completion-comparisons`**. **Needs:** `quotient-completion`, `local-module-maps`.
  Define the supported localization/completion and base-change comparisons
  before formal-family consumers use them.
  **Decision:** there is no unrestricted rule that completion commutes with
  localization or arbitrary scalar extension. State the source and target of
  each proposed comparison and the theorem making it an isomorphism.
  For a Noetherian algebra at a chosen maximal ideal, use the appropriate
  maximal-adic local comparison. For other localizations retain only the maps
  actually supplied by the topology.
  **Separating example:** `QQ[[t]][1/t]` is nonzero, whereas completing
  `QQ[t,1/t]` with respect to the extended ideal `(t)=(1)` gives zero.
  **Acceptance:** no general localization functor or family method silently
  identifies these constructions; a formal generic fiber is not obtained by
  relabeling a finite truncation.

### Local algebra extensions

- [x] **`normalization`**. **Needs:** none.
  Extend normalization and local-length operations beyond the represented
  integral affine and selected plane-curve regimes needed below.
  **Owners:** `rings/commutative_algebra.py`, `rings/commutative_ideals.py`,
  their normalization adapter, and `schemes/singularities.py`.
  **Deliver:** total quotient rings for supported reduced rings, regular-element
  tests, normalization maps componentwise when required, conductor ideals,
  height-one valuations, and finite local lengths with residue-field degree
  accounted for. Preserve minimal primes, components, and support.
  **Decision:** normalization is a ring/scheme map, not a selected polynomial
  normal form; a list of normalized components is not yet the glued
  normalization. Local invariants name a point; global delta cannot be
  substituted for delta at that point.
  **Acceptance:** a reducible reduced curve, a singular integral curve, and
  a nonrational closed point exercise the required maps and local lengths.
  Reuse the existing integral normalization and local `deltaLoc` operations.
  **Capability question:** which operation in the existing Singular normalization
  adapter supplies the reduced/componentwise case, conductor, and comparison
  maps? Inspect the corresponding OSCAR/Macaulay2 operations only for obligations
  the current adapter cannot discharge. Retain that choice at the adapter; extend
  its raising of ideals, components, and maps rather than implementing local
  normalization, factorization, or length algorithms in the scheme consumer.

- [x] **`local-module-maps`**. **Needs:** none.
  Extend local homomorphisms and local-module operations only at their shared
  owners when these consumers require a new supported coefficient regime.
  **Owners:** ring Hom, prime localization, localized ideals and module
  presentations.
  **Preserve:** `QQ[x]_(x)` has nonunit `x` and unit `1+x`;
  `QQ[x,y]/(xy)` localized at `(x,y)` retains zero divisors;
  localizing `QQ[x]/(x)` by `x` yields the zero module.
  **Deliver:** ideal extension/contraction, residue maps, maximal-ideal
  compatibility, and direct-map kernels through the existing exact algorithms,
  including nonreduced coefficients where supported.
  **Acceptance:** transported maps and directly constructed local maps agree
  through their comparison morphisms. A fraction-field computation cannot
  supply a local-ring unit, kernel, or vanishing claim without the required
  faithful comparison.

## Architecture before dependent implementation

These are targeted remaining contracts and preservation obligations, not a
restart of the module/algebra/action constructions.

### Shared diagrams and universal constructions

### Constructor and ownership convergence

- [ ] **`constructor-convergence`**. **Needs:** none.
  Close the surviving alternate-constructor and private-access paths, one
  mathematical construction family with its consumers per release.
  **Owners:** declaration-side contracts at `owned_category.py::object_of`,
  the responsible category/object methods, `Mor`, and existing private adapters;
  session exports in `all.py`, notation in `lexicon/`, and catalogue entrypoints.
  **Scope:** every surviving public construction family, including those whose
  feature implementation no longer appears in this queue. Continue with lattice and
  collection consumers. This is a source-conformance task, not a claim that every
  family currently violates the contract.
  **Decision:** the constructor's defining datum and maps are authoritative.
  Document its allowed mathematical input forms at the existing declaration
  (`OWN-13`), including the actual inherited or composed general construction
  for each specialization (`OWN-14`). Direct construction, notation, a catalogue
  example, a functor image, element reconstruction, and an engine result must
  establish that same datum.
  Concrete runtime classes, global implementation factories, raw adoption and
  conversion helpers are private; importability does not grant calling authority.
  **Deliver:** inspect all routes in the selected family, repair established
  bypasses, and update their ordinary consumers to the owned operation. Preserve
  deliberate user notation through its sanctioned construction, not through a
  retained compatibility factory. Respect the fixed expectation subtrees.
  **Private-access disposition:** for each cross-owner engine/storage access
  encountered, either replace it with the responsible owned operation or establish
  that it implements the already-declared protected framework contract in
  `OWN-05`. A call-site comment, same-file placement, new public raw accessor, or
  helper extraction cannot create an exception. Move raw computation only into
  its designated adapter and keep its raising inside that boundary.
  **First remaining specimen:** a selected lattice constructed through
  `Lattices(R)(data)` and the structured refinements that retain its form and
  framing. Reuse the existing lattice constructor specimens rather than
  commissioning another suite of implementation-shaped checks.
  **Acceptance:** the family's source routes converge and its public objects
  retain the required data before inherited operations run. The accompanying
  source review covers the actual computation and raising, not only exports or
  underscores. Remove only the covered family from this remaining scope; keep
  others named until inspected and repaired where needed. Record completed
  dispositions in commits, never in a second status table in this queue.

- [x] **`category-order`**. **Needs:** none.
  Integrate a construction-order-independent owned category ordering across
  the actual session graph.
  **Owners:** `owned_category.py`, `owned_category_bases.py`,
  `refine.py`, `categories/lattices.py::RootLattices`,
  `categories/schemes/ringed_spaces.py`, and `all.py`.
  **Current boundary:** `all.py` still realizes exported categories over
  `ZZ` in a fixed order; that mechanism does not cover every parameterized,
  unexported, Hom, End, Aut, join, or axiom category.
  **Decision:** establish the class-ordering contract at the common owner and
  cover every category participating in it. Reuse a still-applicable
  implementation from repository history only after reconciling it with the
  current tree; do not merge a historical branch wholesale.
  **Specimens:** construct affine opens, matrix Homs, lattice ranks, the
  discriminant group of `A2`, and an isotropic overlattice in different
  orders over the relevant bases.
  **Acceptance:** the construction protocol explains the same category and
  Hom behavior without enumerating a growing list of startup examples.
  Source integration comes before the terminal-T construction-order executions.

- [ ] **`category-boundaries`**. **Needs:** `category-order`.
  Complete the remaining owned category, Hom, and constructor boundaries.
  **Owners:** the common owned-category runtime, parameterized category bases,
  `rings/ring_foundation.py`, and each surviving mathematical category.
  **Current starting point:** `AdicCompletions` still directly uses Sage's
  runtime `Category` base. `RingedSpaces`, `LocallyRingedSpaces`, and the
  profinite/absolute-Galois hierarchy already use the owned category graph;
  continue the surviving direct-Sage category scan from the remaining owners.
  Runtime inheritance alone does not establish a forbidden mathematical edge.
  **Deliver:** owned semantic supercategories, owned parameter normalization,
  and owned `Hom`, `End`, `Aut`, joins and property refinements throughout
  the surviving graph. Keep Sage mathematical membership tests private to
  engine recognition; public membership and theorem hypotheses use the owned
  graph. Constructor inputs go through the responsible owned construction,
  without asking Sage coercion discovery to invent a mathematical map.
  **Decision:** one object may have several private computational realizations;
  selecting an engine must not change its mathematical identity or interface.
  Preserve zero, one, actions, identity morphisms, and inherited operations
  when removing a semantic engine dependency. Reuse existing realization and
  functor-image owners instead of introducing another registry.
  **Reuse decision:** compare the current shared runtime with the actual released
  `sage-categories` constructor and inheritance interfaces. Keep general compiler
  fixes at that owner; carry only the necessary current integration here. Sage
  host primitives are not a reason to adopt Sage mathematical parents or expose
  their inherited API. Conversely, a different runtime class model is not a
  reason to replace Sage's maintained arithmetic (`OWN-01`, `OWN-04`, `OWN-06`).
  **Acceptance:** the full surviving graph has the required ownership, and
  representative quotient, localization, module, group and lattice objects
  expose their promised operations and maps. The terminal graph inspection
  is paired with positive public constructions, never accepted on edge
  removal alone. Include comparisons across available realizations where
  the same mathematical construction has more than one engine.

- [x] **`constructor-data`**. **Needs:** none.
  Complete constructor-contract discovery and close the remaining
  variadic/opaque defining-data boundaries.
  **Owners:** the common `object_of` construction path, generated category
  contracts, typed parameterized categories, and surviving functors.
  **Deliver:** named mathematical parameter domains and required data for
  ordinary construction, adopted runtime realizations, Hom construction and
  property refinement. Specializations fulfill inherited accessors before
  returning their objects.
  **Boundary decision:** a private runtime realization still receives complete
  owned defining data through the common constructor; adoption is not a public
  raw-engine input form. Inspect inherited zero/one, empty families, component
  access, and scalar actions as well as the newly declared accessor. Keep
  presentation changes explicit through maps, not mutations of retained data.
  **Decision:** retain the exact supplied module when equipping distinct algebra
  structures; chosen multiplication/action/presentation is new structure, not
  a property mutation. Refinement cannot overwrite another structure.
  **Acceptance:** source-backed public signatures and constructor examples
  cover an algebra and a module over the same object, a noncommutative regular
  module action into additive endomorphisms, and two multiplications on one
  supplied module. Generic owners do not import their new descendants.
  Keep general class/functor compilation at `sage-categories`, not here.

- [x] **`general-modules`**. **Needs:** none.
  Extend general module contracts outside the current finite presentation
  algorithms without weakening their mathematical domains.
  **Owners:** `categories/modules/general_modules.py`, module Homs,
  rank functions, framings, and scalar-change functors.
  **Deliver:** additive-group ownership for general supplied modules;
  source-backed linearity algorithms where decidable; broader PID/Smith/
  Hermite support when an engine theorem applies; and infinite-cardinal rank
  where represented.
  **Decision:** fiber rank, locally constant finite-projective rank, and generic
  rank over a domain are separate notions. A finitely generated or finitely
  presented property supplies no chosen framing by itself.
  **Acceptance:** a nonfree module, a nonconstant rank function, an infinite
  indexing set, and an unsupported callable equality problem retain their
  correct interfaces and computational frontier.

## Covering families and sheaves

**Integration route for this workstream:** the covering-family owner constructs
the geometric descent datum; local kernels, cokernels, tensor products,
restriction, and scalar change use the existing module/algebra owners. At the
first unsupported local computation, determine whether its established
Sage/Singular module operation or the applicable CAP module-presentation
operation supplies the needed maps. Repair that adapter once. Research a
sheaf-level package for the specified geometric category when it can supply a
larger operation; do not assume a finite-category presheaf package computes
arbitrary scheme sheaves. Keep the exact missing comparison or descent datum
with the item that requires it (`OWN-08`, `OWN-09`, `DEV-56`).

- [x] **`affine-descent`**. **Needs:** none.
  Extend module and algebra descent from one distinguished affine cover to
  covering families with distinct overlap rings.
  **Owners:** `categories/schemes/gluing.py`,
  `categories/schemes/affine_covers.py`, and
  `categories/divisors/invertible_sheaves.py`.
  **Current boundary:** `ModuleGluingDatum` obtains both transition endpoints
  through one cover's `restricted_module`/intersection path.
  **Decision:** use the two overlap open immersions and their isomorphism.
  Transport the module on the other chart along that isomorphism's ring
  pullback before comparing or composing local maps. Reuse the finite scheme
  gluing's triple-overlap transport.
  **First specimen:** a nontrivial invertible sheaf on the standard two-chart
  cover of `P^1`, then its refinement to three charts.
  **Acceptance:** actual inverse and triple-cocycle equations in the correct
  Homs, glued nonidentity morphisms, and explicit refinement comparisons.
  Isomorphic overlap rings are not silently identical parents.
  [Stacks 01JA](https://stacks.math.columbia.edu/tag/01JA) supplies the scheme
  gluing maps and compatibility requirements.

- [x] **`general-descent`**. **Needs:** `affine-descent`.
  Extend the same covering-family owner to non-affine overlaps and to the
  corresponding locally ringed-space and manifold atlases. The locally
  ringed-space part retains non-affine overlaps, both embeddings, and
  affine-refinement comparison maps; manifold atlas owners retain topological,
  finite-`C^k`, and smooth coordinate changes.
  **Deliver:** an affine refinement of a represented non-affine overlap,
  comparison maps between refinements, and local-to-global gluing independent
  of the chosen refinement. Include smooth, topological, and `C^k`
  atlas maps at their respective owners.
  **Decision:** a covering family is not necessarily a distinguished cover of
  one affine scheme. It must not acquire a fictitious global coordinate ring.
  **Acceptance:** the punctured-plane/overlap construction and refinement
  diagrams retain chart labels and both embeddings; non-affine global
  sections do not replace the whole space by their spectrum.

- [x] **`sheaf-operations`**. **Needs:** `general-descent`.
  Implement sheaf kernels, cokernels, tensor products, local presentations
  and stalk comparisons through the existing module operations.
  **Owner:** module sheaves and their descent morphisms.
  **Deliver:** restrictions of each construction, comparison to chartwise
  constructions, and the induced maps at stalks.
  **Decision:** use the sheaf category in which the construction exists.
  Taking a cokernel of global sections is not in general the global sections
  of the sheaf cokernel; taking an inverse limit of sections is not automatically
  an exact sheaf construction.
  **Acceptance:** a nonzero map of sheaves with nontrivial kernel/cokernel and
  a refinement comparison; equality tests live at the responsible module/Hom
  owner rather than in a new sheaf-level coordinate algorithm.

- [x] **`sheaf-functors`**. **Needs:** `sheaf-operations`.
  Construct inverse image, direct image and module pullback along represented
  scheme morphisms with their correct categories and variance.
  **Decision:** inverse image of a sheaf and tensoring by the target structure
  sheaf are distinct steps of module pullback. Preserve the structural ring
  map and canonical comparison morphisms.
  **Deliver:** functor actions on nonidentity maps, identities, composition,
  and the applicable adjunction unit/counit.
  **Acceptance:** a nontrivial base change of an invertible sheaf agrees via a
  constructed comparison with pulling back its transition data.


## Divisors and relative geometry

**Integration decisions:** products and intersections enter the existing
diagram, algebra pushout, quotient, and gluing constructions. Divisor and
line-bundle operations enter their owned groups and sheaf functors, not a
scheme-specific matrix layer. For each selected non-toric regime, inspect the
applicable maintained Singular/Macaulay2/OSCAR operation for class relations,
sections, Rees algebras, saturation, or intersection data, with its hypotheses
and returned maps. The unanswered question is which full operation supplies
the chosen specimen, not whether these theories should be reimplemented here.
Retain existing fan/subdivision and toric-divisor engines for the toric cases.
Do not make an engine's affine or toric specialization the public definition
of the more general construction (`OWN-01`, `OWN-08`, `OWN-09`).

- [ ] **`scheme-products`**. **Needs:** `universal-constructions`, `general-descent`.
  Extend scheme products, fiber products and closed/open subobjects beyond
  the represented affine and projective-product cases.
  **Owners:** `categories/schemes/schemes.py`, affine Spec, gluing,
  algebra pushouts, and generic diagram constructions.
  **Deliver:** mixed/non-affine products with projections; successive and
  projective closed embeddings with ideal sheaves and homogeneous relations;
  inverse images, graphs, diagonals and equalizers through the shared
  constructions wherever the extended regime permits them.
  **Decision:** products consume an indexed family; general pullbacks/pushouts
  consume their diagrams. Preserve factor roles even for repeated isomorphic
  factors. Scheme-theoretic image uses its defining factorization, not only
  a point-set image.
  **Acceptance:** a repeated `P^1` product, a non-affine base change, and
  successive equations over `ZZ` retain their maps and scalar bases.
  Extend exact property placement with these constructors: separated,
  finite-type, integral, normal, smooth, quasi-affine and quasi-projective
  hypotheses must survive the relevant construction before its consumer uses
  them. Preserve the existing variety, curve and surface categories; a chosen
  dimension or an affine chart alone does not establish their other hypotheses.

- [ ] **`line-bundles`**. **Needs:** `divisors`, `sheaf-functors`.
  Complete line-bundle functors and section maps outside the current toric
  computations.
  **Deliver:** `O(d_1,...,d_r)`, tensor products, inverse line bundles,
  powers, pullback/base change, canonical and anticanonical bundles,
  exact ampleness in supported regimes, graded section rings, and their
  homogeneous-component maps.
  **Decision:** section-ring and Cox gradings retain the actual grading group;
  homogeneous pieces are not just dimension values. A choice of coordinates
  or linearization must remain explicit.
  **Acceptance:** a nonidentity pullback/restriction and a nontrivial graded
  multiplication use the actual section modules and compose with the
  homogeneous-polynomial comparison.

- [ ] **`jets`**. **Needs:** `line-bundles`, `scheme-products`.
  Extend linear-system restrictions and jets to general represented closed
  subschemes and points.
  **Owners:** line bundles, section modules, local ideals and their powers.
  **Deliver:** evaluation and restriction maps, kernels for imposed
  multiplicities, base loci, basepoint-freeness, and parameter spaces.
  **Decision:** use the stalk/residue field and the quotient by the appropriate
  power of the point ideal. Selected toric monomial coordinates are a
  computation, not a definition of arbitrary jets.
  The associated projective map is a morphism only where the sections have
  no common zero; otherwise retain its actual domain of definition.
  **Acceptance:** non-coordinate points, nonreduced imposed conditions,
  and a linear system with a nonempty base locus distinguish these cases.

- [ ] **`cycles`**. **Needs:** `divisors`, `tor-ext`, `scheme-products`.
  Construct non-toric cycles, rational equivalence and intersection operations
  through their local multiplicities and morphisms.
  **Deliver:** fundamental cycles of supported closed subschemes,
  codimension-graded cycle and Chow groups, proper pushforward, flat pullback,
  and the applicable intersection products.
  **Decision:** finite-support cycles need not have a finite set of possible
  prime components. Preserve residue degrees, dimension shifts and hypotheses.
  The local-colength formula for proper surface hypersurface intersections
  does not replace Serre's Tor-length definition in other regimes.
  **Acceptance:** an embedded/nonreduced component contributes its actual
  multiplicity; a supported Tor intersection and the divisor/Chow comparison
  use the same local and homological owners.

- [ ] **`adjunction-blowups`**. **Needs:** `line-bundles`, `scheme-products`, `relative-spec`.
  Turn complete-intersection adjunction data into actual canonical-bundle
  maps, and extend blowups beyond torus-fixed surface centers.
  **Owners:** complete intersections, invertible sheaves, blowups, and local
  presentations.
  **Deliver:** adjunction isomorphisms, exceptional divisors, total and strict
  transforms, Picard pullback and intersection comparisons for the selected
  non-toric center; general complete-intersection family data.
  **Decision:** a stored adjunction twist is not the line bundle or its
  comparison map. Strict transform, total transform, and inverse image are
  distinct. Use the blowup/Rees-algebra construction at its general owner
  before a non-toric consumer; reuse existing fan subdivision in the toric case.
  **Acceptance:** a curve through the center with nontrivial multiplicity,
  the exceptional contribution, and canonical-bundle comparison; del Pezzo
  claims require the applicable smoothness and anticanonical ampleness facts,
  not positive degree alone.

## Cohomology and equivariance

### Shared complex and DGA integration

- [x] **`complexes`**. **Needs:** none.
  Complete the remaining coefficient-ring computation boundary without replacing
  the owned cycle/boundary quotient by an abstract homology group.
  **Owners:** module kernels/images/cokernels and the common cochain/cohomology
  owners. The represented complex itself now supports integer degrees, finite
  support with known zero outside it, and lazy indexed families over all `ZZ`.
  **Current maintained boundary:** finite free kernels use Sage matrix
  `right_kernel`; PID presentation normalization uses the backend `smith_form`;
  polynomial-presentation kernels over a field use Singular `modulo` and `lift`.
  `Cycles`, `Boundaries`, and `Cohomology` compose those operations while retaining
  the inclusion, boundary-in-cycles map, quotient projection, representatives,
  coefficients and induced functor maps. Sage `ChainComplex.homology` was inspected:
  it supplies abstract groups and optional cycle generators, but not those full
  owned comparison maps, so a second whole-complex computation is not selected.
  **Remaining capability:** complexes of finitely presented modules over rings
  outside the existing PID and polynomial-over-a-field adapters. CAP/homalg's
  ModulePresentationsForCAP, FreydCategoriesForCAP, and
  ComplexesAndFilteredObjectsForCAP are listed only as computation references and
  are not provisioned in this repository. Provision and inspect the maintained
  operation before adding any local reduction (`ENG-06`).
  **First remaining specimen:** over `R=ZZ[x]`, represent the two-term map
  `R^2 -> R`, `(a,b) |-> 2a+xb`, and retain both the syzygy inclusion generated
  by `(-x,2)` and the quotient projection onto `R/(2,x)`, together with a
  nonidentity induced map. This ring deliberately lies outside the currently
  represented PID/Singular-field regimes.
  **Construction decisions:** homological resolutions keep their augmentation
  and degree convention explicitly; cochain complexes use degree `+1`. A finite
  computational window, if introduced by a provider, must contain both incoming
  and outgoing maps required by a requested degree and must never declare the
  uncomputed complement to be zero.
  **Acceptance:** the remaining coefficient regime returns owned presentations,
  cycle/boundary inclusions, quotient maps, representatives and induced maps via
  a maintained provider; no new local chain-reduction algorithm is introduced.

- [x] **`dga-cohomology`**. **Needs:** `complexes`.
  Make the existing DGA/cohomology-algebra routes consume that same complex
  contract and preserve only the algebraic refinements the source justifies.
  **Owners:** `categories/algebras/differential_graded_algebras.py`,
  `categories/algebras/cohomology_algebras.py`, graded algebras and derivations,
  and `categories/functors/cohomology.py`.
  **Preserve:** the existing descended multiplication through cycle
  representatives and `class_of_cycle`, and the induced map from a DGA morphism.
  Review `CohomologyAlgebras.super_categories`, which currently declares strict
  graded commutativity, against every admitted source DGA. Place the result in
  the general graded algebra category and add only justified refinements;
  characteristic and parity hypotheses must not disappear during raising.
  **Computation selection:** inspect Sage's
  [commutative DGA operations](https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/commutative_dga.html)
  for cocycles, coboundaries, cohomology, representatives, and products in the
  represented degree range. Use them for the supported commutative case; inspect
  the applicable maintained algebra/module operations for other DGAs rather than
  relabeling them commutative. Decide the exact basis/presentation correspondence
  at the adapter. Do not build a second cohomology solver or multiply chosen
  normal forms without the quotient comparison.
  **Deliver:** inherited underlying module, grading, differential, self-module
  action, unit when required, multiplication, and nonidentity DGA morphisms
  through their immediate owners. Zero boundary degrees and lazy homogeneous
  pieces follow the same component contract as ordinary complexes.
  **Specimens:** degree-zero cohomology of a nonnegative unital DGA; a nonzero
  boundary representing the zero class; multiplication after changing a cycle
  representative by a boundary; and a source-backed noncommutative DGA that
  must not acquire graded commutativity. Retain the applicable characteristic-two
  distinction between sign conventions and additional square-zero relations.
  **Acceptance:** forgetting multiplication gives the same complex construction
  and cohomology modules, with comparison maps if a representation changed.
  Products and induced maps compose through those owned modules. Source review
  establishes inherited data and computational reuse; numerical agreement alone
  cannot remove this item (`OWN-03`, `OWN-07`, `OWN-09`, `OWN-12`).

### Toric integration before geometric extensions

- [x] **`toric-cohomology`**. **Needs:** `complexes`.
  Consolidate toric cohomology's existing maintained computations inside
  declared private adapters and complete raising through the shared constructors.
  **Owners:** `categories/schemes/geometric_cohomology.py`'s
  `ToricWeightCohomologyComplex` and `ToricLineBundleCohomology`, the existing
  toric-divisor/fan adapters, and the common complex/module owners above.
  **Starting point:** these functions already use Sage's `_sheaf_complex`,
  `_sheaf_cohomology_support`, and simplicial chain-complex construction. Keep
  that algorithmic reuse. They also call another object's engine accessor and
  attach geometric data after constructing a complex/module; those paths must
  satisfy `OWN-03`, `OWN-05`, `OWN-06`, and `OWN-07`.
  **Capability decision:** first compare the documented public
  [toric-divisor cohomology operation](https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/divisor.html)
  with the required weight complex, cycle quotient and induced maps. Its returned
  vector spaces are not sufficient evidence of these correspondences. Use the
  public computation where adequate; any necessary upstream private helper is
  confined to the declared toric adapter with its source-backed contract. Check
  [Klyachko bundle/sheaf complexes](https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/sheaf/klyachko.html)
  for the equivariant generalization's actual inputs and outputs, not by name.
  **Deliver:** owned weight/index objects, augmented and shifted differential
  data, cycle and boundary maps, and the total cohomology construction with its
  summand inclusions/projections. Construct the scheme/divisor/weight datum through
  the category initializer before exposure. An empty support and a zero group
  retain the same defining data and scalar action as a nonzero result.
  **Missing-map question:** which upstream geometric maps or established
  complexes supply the requested nonidentity sheaf/restriction/refinement map?
  Obtain and raise that map, then let the shared cohomology functor act. Equal
  weights or dimensions do not define it. Preserve explicit completeness,
  coefficient, and Cartier/Weil hypotheses at their relevant operations.
  **First specimen:** take a divisor with nonzero higher cohomology from the
  cited Sage toric-divisor examples, retaining the stated fan, coefficients and
  weight. Construct an owned weight class with its representative, inclusion and
  quotient image, then its inclusion into total cohomology. The first induced
  map is multiplication by `2` on that line bundle over `QQ`, transported through
  its complex; it must act as multiplication by `2` on the nonzero class.
  Add zero-support and boundary-degree cases. Non-scalar geometric and refinement
  comparisons remain with the extension items; this scalar specimen does not
  discharge them. Acceptance compares actual maps, not only a Betti-number list.
  **Acceptance:** geometry consumes owned complexes and cohomology; the adapter
  retains existing maintained toric computations; all returned constituents and
  later arithmetic remain owned. Source review covers every affected constructor
  and private call, with the missing integration recorded at its owner. Do not
  recreate toric cohomology or declare its whole implementation absent.

### Geometric and equivariant extensions

- [x] **`geometric-cohomology`**. **Needs:** `toric-cohomology`, `sheaf-functors`.
  Extend geometric cohomology from the current toric weight complexes to the
  required non-toric schemes and sheaves.
  **Owners:** `categories/schemes/geometric_cohomology.py`, sheaf descent,
  and existing cochain complexes.
  **Dependency and reuse:** consume the common complex/cohomology route above.
  The new geometric work is the justified complex, augmentation and functorial
  comparison. Inspect the appropriate maintained sheaf-cohomology operation for
  the chosen non-toric presentation before assembling a complex locally; retain
  an existing resolution or Cech construction when it supplies the full datum.
  The unresolved capability is the non-toric complex and maps, not another
  kernel, syzygy, chain-reduction, or cohomology implementation.
  **Deliver:** a geometrically justified complex with its augmentation/
  comparison, induced nonidentity maps, and actual cohomology modules.
  State which cover computes the theory and why it is acyclic or otherwise
  sufficient.
  **Decision:** a complex merely having the expected dimensions is not a
  geometric cohomology construction. Refining a cover produces a comparison
  on complexes and cohomology, not an assertion that two output ranks agree.
  **Acceptance:** a non-toric coherent-cohomology computation and a refinement
  comparison preserve maps and functoriality.

- [x] **`tor-ext`**. **Needs:** `dga-cohomology`.
  Extend the existing Tor/Ext functoriality to both arguments and the
  resolutions needed by geometric consumers.
  **Owners:** module resolutions, chain maps, derived functors, and DGA
  multiplication at the algebra owner.
  **Computation decision:** inspect the current resolution/derived-module adapter
  and the applicable Singular, Macaulay2, OSCAR or homalg operations for lifts
  and resolution comparisons as well as modules. The owned functor provides
  variance and composition; the private adapter supplies maintained resolution
  computations. Repair missing lift transport at that owner, not in each Ext,
  Tor, intersection, and geometric consumer independently.
  **Deliver:** the unresolved argument's induced maps, correct covariance/
  contravariance, comparisons between chosen resolutions, and cohomology
  independence through the appropriate chain-homotopy argument.
  **Decision:** no unsupported bound may turn a prefix of a resolution into
  a complete resolution. Do not require equal chain lifts when only their
  induced cohomology maps are canonical.
  **Acceptance:** nonidentity maps in each argument and two chosen lifts;
  products use a multiplication compatible with the differential and descend
  to cycles modulo boundaries.

- [ ] **`integral-topology`**. **Needs:** `cycles`.
  Extend integral topology, cycle classes and cup-product comparisons beyond
  smooth complete toric examples.
  **Deliver:** specified complex realizations, integral cohomology with
  torsion, graded cup products and induced maps, divisor first Chern classes,
  and the middle-cohomology pairing on the torsion-free quotient where defined.
  **Decision:** coherent cohomology is not singular cohomology; rational
  cohomology does not recover integral torsion. A Chow-to-cohomology
  isomorphism valid for a toric regime is not a universal comparison theorem.
  Specify ordinary, intersection, or resolution cohomology at singular spaces.
  **Acceptance:** actual comparison morphisms and a specimen separating the
  chosen theories; K3 middle cohomology retains its form and divisor inclusion.

- [ ] **`fundamental-hodge`**. **Needs:** `integral-topology`.
  Extend pointed fundamental groups and Hodge structures to the selected
  geometric realizations.
  **Deliver:** a base point, induced maps for pointed morphisms, and supported
  pure or mixed Hodge data attached to the relevant cohomology.
  **Decision:** a toric trivial-fundamental-group result or diagonal Hodge
  pattern cannot classify a general scheme. Hodge-star operators on formed
  modules are not the Hodge structure of a variety.
  **Acceptance:** a sourced nontrivial fundamental-group or off-diagonal
  Hodge example forces the new geometric computation to do real work.

- [ ] **`linearizations`**. **Needs:** `line-bundles`, `geometric-cohomology`.
  Construct line-bundle linearizations and induced section/cohomology
  actions before equivariant geometric applications.
  **Owners:** invertible sheaves, their pullback functors, section/cohomology
  functors, and `GObjects` transport.
  **Decision:** preserving a line-bundle isomorphism class is not choosing a
  compatible linearization. Keep the cocycle datum, the group action, and
  contravariance explicit; use inverse pullback for a left action on sections.
  **Deliver:** fixed-point fiber evaluation as an equivariant map, eigenspace/
  isotypic subobjects, invariant divisor versus eigensection comparisons,
  and action-preserving maps on geometric cohomology.
  **Acceptance:** a nontrivial linearization and two character twists give
  different section actions while the underlying line bundle is unchanged.
  Reuse the group-module scalar-change and restricted-action owners.

- [ ] **`geometric-quotients`**. **Needs:** `scheme-products`.
  Extend fixed loci, quotients and descended maps to the remaining
  non-affine and family cases.
  **Owners:** scheme action/equalizer, invariant algebra, and gluing owners.
  **Decision:** absence of points fixed by the whole group is not freeness;
  examine nonidentity stabilizers or the appropriate action morphism.
  In residue characteristic dividing the group order, abstract constant-group
  reasoning cannot replace group-scheme geometry.
  **Deliver:** scheme-theoretic fixed ideals, supported emptiness/freeness,
  universal quotient maps, descended nonidentity morphisms, and precisely
  qualified base-change comparisons.
  **Acceptance:** nonreduced fixed data and a group with no common fixed point
  but a nontrivial point stabilizer distinguish these predicates. Apply
  Lefschetz formulas only after their geometric/cohomological hypotheses and
  actions have been established.

## Families and singularities

**Integration route:** construct a family through the scheme slice; its fibers
and coefficient changes use the existing pullback and scalar-change functors.
Formal consumers use the completed object and its inverse system, never their
own precision parameter as a defining equation. Local classification uses the
existing singularity/normalization adapters. Before implementing a new local
recognition rule, identify the maintained algorithm for the specified equivalence
relation and whether it returns coordinate maps. For analytic comparisons,
monodromy and nearby/vanishing cycles, identify the precise source construction
and available implementation first; names shared with algebraic operations do
not establish a comparison or authorize a substitute (`OWN-08`, `OWN-09`).

- [x] **`dvr-families`**. **Needs:** `localization`, `completion-comparisons`, `scheme-products`.
  Extend `categories/schemes/families.py` to DVR bases through the existing
  scheme slice and scalar-change constructions.
  **Dependencies:** local algebra; corrected completion only for the completed
  base-change portion.
  **Deliver:** spectra of DVRs, generic and special fibers via fraction and
  residue maps, the completed-base family, and maps comparing the two routes
  to its special fiber.
  **Decision:** the family is its morphism `X -> S`. Flatness, properness and
  smoothness are additional properties, not consequences of naming it a family.
  Use torsion-freeness for the relevant module over a DVR only with the theorem's
  actual hypotheses; do not transplant it to arbitrary bases.
  **First specimen:** `xy=t` over `QQ[t]_(t)`, its generic fiber and nodal
  special fiber, followed by base change to `QQ[[t]]`.
  **Acceptance:** the same parameter map controls equations, differentials,
  fibers and flatness; a scalar-killed comparison detects nonflatness.
  Completion precision is absent from exact flatness and fiber claims.

- [x] **`formal-families`**. **Needs:** `completion-comparisons`, `sheaf-functors`.
  Construct formal neighborhoods and formal families as formal objects,
  retaining their algebraic comparisons.
  **Dependencies:** corrected ring/module completion and continuous maps.
  **Decision:** distinguish `Spec(A_hat)`, the formal spectrum, and the
  system of infinitesimal thickenings. Their point sets and categories are not
  interchangeable. An infinitesimal thickening is one finite stage.
  **Deliver:** the selected ideal of definition, compatible thickenings,
  formal restrictions, and morphisms justified by the topology.
  **Acceptance:** changing the finite computational order refines information
  without changing the formal object; compatible truncation data is connected
  to the completed algebra by actual maps.

- [ ] **`analytic-families`**. **Needs:** `scheme-products`.
  Add analytic-disc families and their specified comparison with algebraic
  or formal models.
  **Decision:** use the analytic category and its topology. A formal power
  series need not converge; completion does not construct an analytic disc.
  **Deliver:** the analytic family morphism, the supported comparison functor
  and maps, and explicit hypotheses for transporting sheaf/cohomology results.
  **Acceptance:** the selected analytic example has a source-backed comparison;
  do not fabricate a comparison for arbitrary formal input.
  **Dependency choice:** use an algebraic comparison for the first example.
  A separately required formal comparison must add `formal-families` to Needs
  before work begins; it cannot silently consume an unfinished formal model.

- [ ] **`monodromy`**. **Needs:** `analytic-families`, `fundamental-hodge`, `geometric-cohomology`.
  Construct higher direct images, local systems and monodromy for the
  required family strata.
  **Dependencies:** the selected topology, sheaves and geometric cohomology.
  **Deliver:** the relevant higher direct-image sheaf, stalk-to-fiber
  comparison, local system on the smooth stratum, and a representation of its
  pointed fundamental group on the actual cohomology module.
  **Decision:** a fiber cohomology module alone is not a higher direct image
  and repeated fiber dimensions do not prove local constancy.
  Use [topological proper base change](https://stacks.math.columbia.edu/tag/09V4)
  only in its stated setting. Singular-fiber specialization and nearby/vanishing
  cycles require their own comparison, not that same theorem by analogy.
  **Acceptance:** a sourced family with nonidentity monodromy and a singular
  fiber; maps preserve the applicable pairing and action.

- [x] **`singularity-classification`**. **Needs:** `normalization`, `local-module-maps`.
  Extend local singularity classification beyond selected coordinate
  normal-form recognition.
  **Owners:** `categories/schemes/singularities.py`, pointed local rings,
  completions, and established singularity algorithms.
  **Decision:** regularity and smoothness over a base differ; name which is
  decided. A normal-form label requires the appropriate equivalence and,
  when constructed, its coordinate-change morphism. Matching Milnor/Tjurina
  numbers alone is not a classification theorem.
  **Deliver:** supported coordinate changes, the correct equivalence notion,
  Jacobian/Fitting ideals under their hypotheses, and smooth/nonsmooth loci
  with the selected scheme structure.
  **Acceptance:** the same singularity in non-normal-form coordinates, a
  nearby non-equivalent example where invariants do not suffice, and a
  nonperfect-base case that separates regularity from smoothness.

- [ ] **`curve-genus`**. **Needs:** `normalization`, `general-descent`.
  Connect local delta, normalization, and geometric genus globally.
  **Dependencies:** normalization maps, local lengths, and projective gluing.
  **Deliver:** projective curve normalization and the comparison between
  arithmetic and geometric genus, with local contributions at every singular
  point and the applicable connectedness/geometric-integrality hypotheses.
  **Decision:** do not sum a global affine delta once per singular point.
  Base extension can split points and components; retain residue degrees.
  **Acceptance:** a curve with more than one singular point and a curve with a
  nonrational singular point, using an independently sourced genus relation.

## Geometric research applications

**Release boundary:** these are research consumers of the preceding shared
constructions. Their local contribution is the source-specified geometric data
and composition of existing functors/maps. Any missing section, quotient,
cohomology, or lattice operation returns to its named dependency owner; the
application must not introduce a private copy. Before each application release,
trace its nonidentity maps back through those owners. An expected lattice,
signature, dimension, or classification label is a comparison specimen, not the
definition of the computed geometric result (`OWN-01`, `OWN-09`, `OWN-12`).

- [ ] **`k3-family`**. **Needs:** `linearizations`, `geometric-quotients`, `jets`, `adjunction-blowups`.
  Construct the `(4,4)` double-cover K3 family over `P^1 x P^1` and
  the two lifts of the diagonal sign involution.
  **Inputs:** branch sections, a selected linearization, the existing cyclic
  cover algebra/relative Spec, smoothness criteria, and section actions.
  **Decisions:** a lift needs a compatible isomorphism on the line bundle
  and branch section, not just an invariant divisor class. Keep `mu_2`
  and a chosen constant-group identification distinct when base hypotheses
  matter. Determine the lift's order and action on top forms from its maps.
  **Deliver:** invariant/eigenspace decomposition of the section space,
  including the source-specified `13+12` decomposition, the cover morphism,
  both lifts, fixed subschemes and top-form action.
  **Acceptance:** compute the decomposition through the action rather than
  hard-code its dimensions. The cover, involutions and base changes commute.

- [ ] **`enriques-family`**. **Needs:** `k3-family`, `integral-topology`.
  Construct the Enriques quotient and its lattice comparisons from the
  preceding K3 action.
  **Inputs:** an actually fixed-point-free involution, the required field/
  characteristic hypotheses, quotient descent, integral cohomology and forms.
  **Deliver:** the quotient morphism and invariant factorization, induced
  cohomology maps, invariant/anti-invariant sublattices, discriminant gluing,
  and compatible family quotients.
  **Decision:** the name Enriques follows the proved geometric hypotheses,
  not a chosen fixture label or a lattice signature.
  **Acceptance:** compare fixed loci, representations and the applicable
  Lefschetz calculation; retain the integral embeddings and gluing maps, not
  only ranks.

- [ ] **`ade-pairs`**. **Needs:** `divisors`, `relative-spec`, `singularity-classification`, `chambers`.
  Implement source-defined ADE and toric log pairs through the existing
  toric, divisor, cyclic-cover and Coxeter owners.
  **Owner:** `categories/schemes/ade_surfaces.py` and those shared inputs.
  **Deliver:** equipped pairs `(X,Delta)`; the exact finite/affine ADE type
  and variant range; decorated integral polygons with distinguished point;
  toric base and boundary/complementary divisors; branch section/Newton
  polygon; pyramidal three-polytope and toric threefold; double cover and deck
  involution; pulled-back boundary; polarizing and Dynkin data.
  **Decision:** preserve side decorations and parity constraints as actual
  classification data. ADE base and cover surfaces are equipped geometric
  objects, not parallel records duplicating a scheme.
  **Acceptance:** Alexeev--Thompson source examples, singular-orbit and
  parity-forced cases, and local/global singularity comparisons.
  Read and cite the source for each classification rule before implementing it.

- [ ] **`bertini-family`**. **Needs:** `jets`, `adjunction-blowups`, `singularity-classification`.
  Supply Bertini and general complete-intersection family applications.
  **Inputs:** parameter spaces, evaluation/jet maps, and local smoothness.
  **Decision:** generic smoothness or a nonempty open good-parameter locus does
  not make every member smooth. Keep basepoint and characteristic hypotheses.
  **Deliver:** the parameter family and the actual condition/locus asserted
  by the selected theorem, together with base-change and restriction maps.
  **Acceptance:** a valid general member and an explicit exceptional singular
  member coexist in the same parameter construction.

## Arithmetic and reflection geometry

Arithmetic work follows geometry except for an explicitly named geometric
dependency. Reuse the current orthogonal groups, subgroup constructions,
finite-quotient splitting, involution centralizers, lattice loci, configuration
lifting, and height-bounded enumeration; extend only the missing regimes specified below.

**Computation decision for each selected arithmetic item:** inspect the current
private lattice/group adapters and the relevant `sage-indefinite-port`,
OSCAR/Hecke, GAP, or polyhedral operation for the exact requested witnesses and
completeness regime. State whether it supplies existence, a transporter, an
orbit representative, or a complete classification; keep those outputs distinct.
Assemble subgroup, action, quotient and gluing data through their existing owned
constructors. Do not rebuild a lattice/group algorithm because its output needs
an owned morphism, and do not move a bespoke algorithm to an external-language
script and call it delegated. If an actual algorithmic gap remains, name it and
apply `ENG-06` before implementation. Bridge repairs and codec additions belong
at the existing bridge owner, not in an arithmetic consumer (`OWN-07`, `OWN-08`).

- [x] **`transporters`**. **Needs:** none.
  Finish rational-integral transporters and cosets through the required
  external arithmetic operations.
  **Owners:** rational matrix groups, lattice stabilizers,
  `categories/orthogonal_quotients.py`, and `sage-indefinite-port`.
  **Deliver:** integral transporter between commensurable lattices and the
  remaining external arithmetic lifting theorem. Finite-character right-coset
  transversals and stabilizer double cosets now return live orthogonal-group
  lifts with explicit coset orientation.
  **Decision:** finite reduction computes the stated arithmetic object only
  after proving the invariant-lattice/denominator and lifting hypotheses.
  An arbitrary rational matrix group need not admit the required finite
  reduction. Specify the cases, rather than silently bounding denominators.
  **Acceptance:** lift each representative/transporter to an actual rational
  or integral morphism, verify its action on the lattice, and retain exact
  stabilizer inclusions and coset orientation.

- [x] **`centralizers`**. **Needs:** `transporters`.
  Extend centralizers from involutions to higher finite-order isometries
  and their equivariant orbits.
  **Deliver:** cyclotomic primary subspaces, their integral intersections,
  gluing subgroup, compatible isometry groups, and lifts to the full lattice.
  Account for the extra algebra/hermitian structure required on a cyclotomic
  component.
  **Decision:** the finite discriminant image is not the full arithmetic
  centralizer; independent isometries of the components need not preserve
  the gluing. Keep the commuting square with the distinguished isometry.
  **Acceptance:** a finite-order example with a nontrivial cyclotomic component
  and nontrivial gluing, plus decorated sublattice/flag orbit representatives
  and transporter morphisms.

- [x] **`reduction-complexes`**. **Needs:** `transporters`.
  Complete exact rational polyhedral and reduction-complex constructions.
  **Owners:** existing polytope/cone, pairing-configuration, and lattice-action
  owners; Normaliz, cddlib, PPL or the existing bridge computes polyhedra.
  **Deliver:** facets, extreme rays, incidences and face stabilizers; reduction
  cells and adjacent-cell morphisms; Lorentzian perfect-domain traversal and
  marked nonzero-norm vector transport.
  **Decision:** use the retained pairing and exact rational inequalities,
  not a floating-point picture or only a canonized incidence graph.
  **Acceptance:** adjacent cells share the actual face, their transporter
  sends one cell to the other, and the group-generation/completeness argument
  distinguishes a full domain from a finite exploration prefix.

- [x] **`witt-recursion`**. **Needs:** `lattice-embeddings`, `parabolic-gluing`.
  Implement higher-Witt-index recursion and the `2U` Eichler construction
  through the existing isometry, discriminant and transporter owners.
  **Deliver:** complete the source-defined subgroup beyond the represented
  two `SL_2(ZZ)` actions, Eichler transformations, canonical `O(K)` lifts and
  finite covering representatives: supply the remaining discriminant lifts,
  recursive stabilizers, transporter completion to the full orthogonal group,
  and recursive lattice equivalence.
  **Decision:** state evenness/integrality conditions for every transformation.
  A subgroup generated so far is not the full orthogonal group until the
  generation theorem applies. A covering family is not automatically a set
  of distinct orbit representatives.
  **Acceptance:** explicit action morphisms and a completeness argument,
  with each recursive step decreasing the parameter its termination proof uses.

- [x] **`parabolic-gluing`**. **Needs:** `transporters`.
  Replace heuristic parabolic constructions by exact integral gluing.
  **Owners:** isotropic reductions, group actions and arithmetic groups.
  **Deliver:** the rational Witt decomposition with integral sublattices,
  unipotent kernel, gluing-preserving Levi image, lift obstructions and
  supported lifts, and the corresponding exact sequence.
  Construct the inductive flag-orbit double cosets in the actual image of
  the parabolic, not automatically in the whole orthogonal group of the
  reduction.
  **Decision:** primitive means the quotient by the submodule is torsion-free;
  a primitive vector can have pairing divisibility greater than one.
  Distinguish vectors, their rank-one sublattices, rational planes, and
  saturated integral sublattices throughout.
  **Acceptance:** a non-unimodular example where gluing restricts the Levi
  action, plus line/plane incidence with actual embeddings and transporters.

- [x] **`chambers`**. **Needs:** none.
  Finish the remaining Coxeter-poset and number-field Vinberg operations.
  **Owners:** `categories/coxeter_diagrams.py`, Vinberg invariants and the
  reflection-engine adapter.
  **Deliver:** maximal elliptic/parabolic subdiagram posets and the number-field
  root computation in its valid arithmetic regimes. The exact root-half-space
  chamber, dominant cone, positive-cone projectivization, Weyl group and lazy
  chamber complex are already delivered at their owners.
  **Decision:** retain root-to-diagram maps and exact edge/vertex weights;
  bounded search is not a nonreflectivity proof. Reuse projectively weighted
  graph objects and the current Vinberg/edge-walk implementations. The
  number-field operation remains a provider obligation rather than an integer
  algorithm with coerced coefficients.
  **Acceptance:** sourced finite, affine, noncrystallographic and hyperbolic
  literature examples distinguish the asserted regimes, and a supported
  totally-real number-field example returns roots over its actual integer ring.

- [x] **`arithmetic-applications`**. **Needs:** `witt-recursion`, `centralizers`, `reduction-complexes`.
  Assemble the three arithmetic research constructions with their maps.
  **Lorentzian:** `U + E8(-1)`, its orthogonal/component groups, cusp orbit,
  cusp stabilizer, unipotent radical and map onto the definite reduction group.
  **Higher Witt index:** `U + U(2) + E8(-2)`, with its represented line/plane
  orbits, stabilizers, full-orthogonal Tits-building incidence, and generic
  character-defined subgroup cusp/flag splitting with actual subgroup
  transporters, obtained by left-adjusting a full-orthogonal witness by the
  target stabilizer inside the finite character quotient; instantiate the
  intended `H <= O(A_L)` and retain the resulting
  application maps.
  **Equivariant:** the K3 lattice with an Enriques involution, its integral
  invariant/anti-invariant decomposition and gluing, full centralizer,
  polarization stabilizer intersection, and anti-invariant isotropic orbits.
  **Acceptance:** actual inclusions, projections, group maps and transporters,
  not a table of expected invariants. Their execution belongs to T.

## Framework transfer and organization

### Organization findings

- [ ] **`framework-transfer`**. **Needs:** none.
  Transfer each remaining subsystem to `sage-categories` only with its
  complete mathematical dependency path.
  **Inputs:** read the upstream `specs/system.md`, `specs/leaves.md`,
  `specs/functor.md`, and `specs/leaf-scaffolding.md` at that transfer.
  **Deliver:** leaf constructors, structural functors on objects and morphisms,
  inherited data/operations, and the real downstream algorithm; retire the
  covered local runtime responsibility in the same unit.
  **Decision:** arbitrary abelian-group/bimodule realization and the remaining
  generic monoidal/class/static-projection work belong upstream. A matching
  category name or a specification is not an implemented dependency.
  **Computational decision:** distinguish the upstream class compiler from its
  mathematical computation owners. For finite diagrams, presented categories,
  module categories, and structural operations, inspect the applicable CAP and
  Catlab/GATlab implementations through upstream's existing bridges. Identify
  the exact output, maps, and supported regime at the consuming declaration.
  A finite-diagram engine is not an algorithm for arbitrary infinite limits;
  an equational engine does not decide every presented morphism equality.
  **Remaining source review:** inspect the complete transferred dependency path
  for local algorithms duplicating those maintained operations. Replace an
  established duplication at its computation owner and connect the preamble
  consumer to the released interface. Copying the same algorithm into
  `sage-categories` does not satisfy this obligation. Use its README, COMPLAINTS,
  and specs as requirements and discovery leads, then inspect the implementation.
  Do not repair all unrelated upstream findings as a precondition for this unit.
  Explicit functor reuse may keep a preamble consumer coherent before full
  automatic inheritance; it must not duplicate the underlying algorithm.
  **Acceptance:** a nonidentity morphism and inherited operation work through
  the transferred construction without a second mathematical object system.
  The downstream dependency is declared through the repository's supported
  release route, not a sibling-checkout import. The old local implementation
  remains a removal obligation until all its required callers use the surviving
  owner; changing imports or shipping an unused upstream implementation is not
  completion. Coordinate the interface revision before consumers change.

- [ ] **`collection-ownership`**. **Needs:** `toric-cohomology`.
  Finish collection ownership and typing on the surviving interfaces.
  **Targets:** group and coset/orbit collections, discriminant objects,
  lattice roots, Coxeter/configuration data, tensors and index shapes,
  scheme/fan/polytope families, and profinite/Galois stages and embeddings.
  **Decision:** owned sets/indexed families retain labels, multiplicity,
  cardinality and laziness. Finite support does not imply finite index set.
  A Python sequence survives only at syntactic ingress immediately parsed
  into owned data or private finite engine serialization.
  **Deliver:** mathematical parameter/result types and readable forms of
  functors, with unknown static expressibility localized according to the
  typing policy rather than broad annotations at each consumer.
  **Recursive boundary:** inspect each targeted public operation's constituents,
  not merely the outer collection type. Include lazy evaluation, iteration,
  indexing, coefficients, base rings, framing data, representatives, inclusions,
  projections, morphism endpoints, scalar arithmetic, equality and reconstruction.
  Extend this inspection to every surviving public family under the constructor
  scope above; the target list supplies traversal starting points, not exceptions
  for unlisted mathematics (`OWN-04`).
  **First concrete repair boundary:** inspect the geometric cohomology outputs
  and `ToricHodgeData.degree_hodge_numbers` alongside the toric item. That method
  currently constructs tuple-valued degree data with Python integer values.
  Express the mathematical indexing and values through the existing owned
  family/scalar owners; preserve its actual grading and source cohomology.
  Also follow a cohomology representative through inclusion and arithmetic, and
  a localized module element through its scalar action. Correctness of an outer
  module or family does not establish ownership of these evaluated results.
  **Integration decision:** raising belongs inside the selected adapter and
  passes through the same semantic constructor as ordinary input. Add the
  missing owned scalar/family/map operation at its owner rather than publishing
  raw storage or copying a conversion loop into each theory. Fix the actual type
  contract; `Any`, `object`, casts, and suppressed diagnostics do not supply it.
  **Acceptance:** infinite/repeated-label specimens and nontrivial consumers
  retain their mathematics. A list/tuple count or annotation count alone
  cannot remove this item.
  Retain only uninspected or unrepaired families after a delivery; evidence for
  completed families belongs in their commits. Source inspection establishes
  recursive ownership, and public specimens remain unexecuted until T.

- [ ] **`package-organization`**. **Needs:** `framework-transfer`, `collection-ownership`, `constructor-convergence`, `category-boundaries`, `general-modules`, `archive-reconciliation`, `dvr-families`, `formal-families`, `monodromy`, `curve-genus`, `enriques-family`, `ade-pairs`, `bertini-family`, `arithmetic-applications`.
  Finish ownership-directed package, export and import consolidation after
  the affected interfaces settle.
  **Dependency scope:** this is final cross-family consolidation. Each feature
  still repairs and consolidates its own changed owners in its delivery unit;
  these final prerequisites do not defer constructor or ownership correctness.
  **Targets:** surviving category/Hom infrastructure, module/algebra scalar
  changes, scheme descent, lattice ecosystem and private engine routines.
  **Deliver:** one owner for each repeated mathematical responsibility,
  defining-module imports with public aggregators as leaves, focused
  dependency boundaries, and package splits that reflect mathematical
  independence.
  **Decision:** do not resplit a file solely by size or reintroduce deferred
  imports to mask a mathematical dependency inversion. Preserve deliberate
  notebook/REPL vocabulary even when it has no internal callers.
  **Acceptance:** trace a public constructor, nonidentity functor image and
  downstream operation through the surviving owners; remove only superseded
  implementations whose required behavior has been transferred.
  Include their old construction routes, imports, session bindings, and ordinary
  consumers in that transfer. Preserve mathematical expectations and public
  vocabulary at the sanctioned entrypoint. A new private module containing the
  same duplicated mathematics, an unused replacement adapter, or a compatibility
  route left for an inconvenient caller leaves this item open (`OWN-08`, `OWN-13`).

- [ ] **`archive-reconciliation`**. **Needs:** none.
  Complete the archive-to-live reconciliation without recreating supplied
  mathematics.
  **Scope:** every archived `categories/**/*.sage` and `.py` public
  mathematical notion, valid known-mathematics assertions,
  `coxeter_tdd_specs`, and framework geometric scenarios.
  **Deliver:** genuinely missing operations at their live owners and migrated
  independent mathematical facts at the appropriate proof surfaces.
  **Decision:** compare semantic constructions, not foreign signatures or
  directories. Every required unresolved operation remains concrete work;
  omission, renaming, or a rejected implementation does not remove its
  mathematical burden. Preserve the author's expectation subtrees.
  **Reuse decision:** archive code supplies mathematical requirements and
  specimens, not sanctioned constructor or engine-access precedents. For each
  missing operation, first compare the live shared owner and maintained upstream
  operation, then add only its missing integration. Carry the original required
  maps and hypotheses into that task; do not port a historical bespoke algorithm
  merely because it is already written (`OWN-01`, `OWN-08`, `DEV-56`).
  **Acceptance:** source-backed reconciliation for every required notion.
  Record completed dispositions in commits, not a historical table here.
  The regenerable denominator is
  `computations/reports/archive_reconciliation_inventory.tsv`, generated by
  `computations/scripts/archive_reconciliation_inventory.py`. Reconcile its notions
  by archived module; record the established live owner and disposition as each notion
  is settled, and remove reconciled work from the remaining queue. Modules are
  independent; the single-worker repository needs no additional coordination record.

## Final verification

### Testing is deferred until every other item is done (always-on)

The terminal-T rule is defined by `DEV-58` in
[CONTRIBUTING.md](CONTRIBUTING.md). Write falsifying mathematical specimens
with implementation and commit them unverified. Do not execute them during
the preceding workstreams. Optional research consumers below do not delay T.

The source-conformance and integration obligations above are required work, not
optional engine improvements. A feature's numerical implementation can already
exist while its construction or encapsulation still needs repair. Deliver and
review those source changes before T; T executes the mathematical evidence and
repairs what it exposes. It is not a reason to postpone source-level ownership
review until every downstream consumer has copied the same bypass.

- [ ] **`terminal-reference`**. **Needs:** `package-organization`.
  After required implementation and transfer are finished, generate the
  preamble reference and category/functor graph from the integrated source,
  then read them against the intended objects, maps and inherited operations.
  **Acceptance:** documentation describes that source and exposes the
  mathematical contracts. Generation success alone is not a correctness claim.
  Compare the integrated constructor, adapter, export and consumer contracts
  with `OWN-01` through `OWN-14`, including source-reviewed work no longer in
  this queue. Use the completed units' commits to locate evidence, then inspect
  the affected live routes after integration. Missing mandatory architecture is
  new concrete repair work at its owner, not a documentation rewrite declaring
  the weaker implementation acceptable. Do not turn this comparison into a
  source-policing test or a count of engine imports.

- [ ] **`terminal-execution`**. **Needs:** `terminal-reference`.
  Execute the prescribed public-construction and mathematical suites in the
  terminal verification phase through the existing project recipes.
  **Scope:** expectation subtrees, ring/module/algebra/action contracts,
  completion versus truncation, geometric constructions and comparisons,
  transferred framework consumers, and the valid archive/literature specimens.
  Include the permitted construction-order/session tests on the integrated
  tree and notebook checks through `japi`.
  **Acceptance:** each claimed behavior is exercised through the actual
  public path. An unverified assertion, suite count, or backend-only test is
  not proof of the corresponding construction.
  Include the new localization/fraction-field route, genuine completion and its
  projections, shared complex and DGA boundary degrees, integral torsion,
  representative-independent products, toric weight-to-total maps, lazy owned
  constituents, and the nonidentity maps recorded with each integration unit.
  Reuse existing proof surfaces and preserve independent mathematical expected
  results. Engine call counts, mocked delegation, and checks of private helper
  spellings do not prove these obligations.

- [ ] **`terminal-repairs`**. **Needs:** `terminal-execution`.
  Repair the mathematical owners exposed by terminal verification and
  establish the originally required behavior.
  **Decision:** do not weaken expectations to match an implementation, filter
  required failures, infer false from missing algorithms, or turn the failure
  list into unrelated architectural work. A mathematically incorrect
  expectation may change only under the exception in `AGENTS.md`, with
  the correction justified in its commit.
  **Acceptance:** the actual failed proposition is established and the
  affected downstream construction remains coherent.

- [ ] **`terminal-session`**. **Needs:** `terminal-repairs`.
  Verify the required session/rendered examples and final contribution
  contracts after mathematical integration.
  **Deliver:** actual inspected notebook/rendering results where relevant,
  source-backed terminology review at the required push boundary, and the
  repository's prescribed final QC.
  **Acceptance:** the displayed mathematical objects and maps are correct;
  no output is certified solely by a generated file or a server starting.
  Respect the user's push approval and active-task scope.



## Optional research consumers

These are not prerequisites for the required mathematics or terminal T.

- [x] **`optional-display`**. **Needs:** none.
  Add further notebook/rich-display examples only for a named research
  question using live objects. Use existing polygon, Three.js, and diagram
  rendering owners; do not install implicit global display hooks.
- [ ] **`refactor-audit`**. **Needs:** `terminal-session`.

  Audit the whole repository for messy, disorganized or duplicated code and carry out the
  refactorings that consolidate sources of truth and restore proper encapsulation. The public
  mathematical API need not change and should not change incidentally; this is about the
  inside.

  **This node explodes.** Every refactor the audit identifies becomes its own node in this DAG,
  with its own `Needs` edges, and every one of them terminates back into this node. Do not
  carry a list of intended refactorings in prose or in your head — a refactoring that is not a
  node is one nobody will do. Recurse: a refactor that turns out to contain several
  independent ones explodes in turn.

  **Acceptance:** the audit is complete and every finding it produced exists as a node. At
  that point this node is done — it is a scheduling node, not a work node, and it may be
  marked skippable once the plan is fully exploded.

- [ ] **`type-paydown`**. **Needs:** `refactor-audit`.

  Pay down type errors where doing so is reasonable, and not one step further. Every typing
  decision must improve the legibility of the code, the ability to understand what it does, and
  the ability to reason statically about whether it is correct. That is the standard the change
  is judged against, not the error count.

  Golfing the code into oblivion — distortions that exist only to silence a checker — is the
  failure mode. Where a contortion is genuinely warranted, it must be judged as significantly
  serving the goal above, and the argument for it recorded explicitly in the commit message,
  not in a comment and not left implicit. A type annotation nobody can read has made the code
  worse even when the checker is quieter.

- [ ] **`bloat-audit-loop`**. **Needs:** `type-paydown`.

  The terminal node, and it loops rather than closing. Continually audit the codebase for
  unnecessary bloat, bad style and non-idiomatic constructions, opportunities to reduce lines
  of code, and anything hand-rolled that could be offloaded to a dependency — Python or
  otherwise, inside Sage or outside it. Append every finding to `COMPLAINTS.md` as it is found.

  Findings accumulate there; they do not have to be fixed in the same pass, and the audit is
  never declared finished. When there are no findings in a pass, record nothing and run it
  again later.

- [ ] **`optional-database`**. **Needs:** none.
  Add a database/classification example when it supplies data needed by
  research: LMFDB, curve/field databases, OEIS, GRDB, Kreuzer--Skarke or
  Fanography. Select a concrete mathematical query before provisioning an
  adapter.
- [ ] **`optional-engine`**. **Needs:** none.
  Extend private engine integrations when a named construction benefits:
  Sage/Singular for local and polynomial algebra, libGAP for group actions,
  persistent `sage-julia-bridge` for OSCAR/Hecke, optional Macaulay2 for
  its exact algebra strengths, and `py_polyhedral` for required polyhedral
  binaries. Maxima stays within its symbolic-calculus domain.
  **Decision:** search existing interfaces first; provision only the needed
  dependency; put reusable codecs and bridge defects at their actual owner.
  Mathematical outputs always return as owned objects and maps.
  An integration required by an item above is part of that required item, not
  this optional list. Only additional research capabilities with no required
  consumer belong here; moving a dependency here does not unblock or complete
  its consumer.
