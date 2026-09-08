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

Follow [CONTRIBUTING.md](CONTRIBUTING.md), especially `DEV-50` through `DEV-58`.
Read the generated `docs/preamble-megadoc.md` before preamble implementation
under the governing `AGENTS.md` prerequisites. This queue does not authorize
running preamble tests, QC, Sage, or notebooks before terminal T.

### Contents

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
- [Work coordination](#work-coordination)

### Workstreams

Select a concrete unchecked construction below, not an entire row. Scores follow
[COMPLEXITY.md](COMPLEXITY.md); they measure the responsibility for the named
boundary, not its line count or duration. Reassess a bounded implementation once
its input contracts are settled.

| Work | Required input | Next mathematical output | Complexity and reason |
| --- | --- | --- | --- |
| Completion and local algebra | Existing ring, ideal, localization, presentation, and scalar-change owners | Completion distinguished from every finite quotient, then module and local comparison maps | 90: exactness and representation decisions propagate into formal geometry |
| Construction contracts | Existing category/Hom/construction framework | Construction-order independence and preservation of supplied structure across affected constructors | 90: shared runtime and mathematical identity |
| Covering families and sheaves | Existing affine charts, localization maps, and finite scheme gluing | Descent across distinct chart rings, refinement comparisons, and sheaf operations | 85: common descent contract for all non-affine consumers |
| Divisors and relative geometry | Sheaf descent and supported local algebra | Non-toric and relative divisor/section/intersection constructions | 65: several geometric theories share maps and hypotheses |
| Cohomology and equivariance | Existing complexes, derived module operations, geometry and actions | Geometric functors, integral comparisons, and linearized actions | 75: topology, variance, and comparison hypotheses |
| Families and singularities | Completion for formal tasks; sheaves and local criteria for other tasks | DVR families, formal models, relative invariants, and local systems | 75: compatibility and distinct algebraic/formal/analytic meanings |
| Geometric research applications | Specific cover, divisor, cohomology, and lattice inputs | ADE log pairs and the K3/Enriques workflows below | 65: source-defined applications of shared constructions |
| Arithmetic and reflection geometry | Existing lattice, group-action, discriminant, and exact engine owners | Remaining transporters, higher-order centralizers, parabolics and reduction complexes | 85: completeness and witness construction in infinite groups |
| Framework transfer and organization | Each subsystem's complete upstream dependency | One surviving mathematical owner with usable inherited operations | 90: shared ownership and cross-framework transfer |
| T | All required implementation, integration, and source consolidation below | Executed mathematical evidence and repairs of the failures it exposes | 15 for execution; score each resulting repair at its actual owner |

### Remaining workstreams as a dependency graph

Dependencies are on particular mathematical outputs, not on an entire workstream
being declared complete.

- Repair completion before module-completion consumers, completion base change,
  formal neighborhoods, or arguments using completion flatness.
- Repair the construction contract used by the selected consumer before adding
  another constructor around its missing inherited state.
- Extend covering-family descent before non-affine sheaf operations and the
  divisor, relative-Spec, or quotient constructions that need those operations.
- Supply actual section-space functors before transporting actions to sections;
  supply geometric complexes and comparison maps before topological or Hodge
  claims.
- Supply the particular branch, linearization, fixed-locus, and cohomological
  inputs before the K3/Enriques application.
- Supply exact gluing and the required external arithmetic operation before its
  parabolic or recursive arithmetic consumer.
- Transfer each mathematical subsystem when upstream supports its whole
  constructor/morphism/inherited-operation path. Finish the remaining transfers
  and organization before T.
- A blocked completion task does not block ordinary algebraic geometry that
  does not use completion. An arithmetic engine gap does not block geometry.
  An active file reservation blocks conflicting writes, not read-only reuse.

## Completion and local algebra

Paths in this section are relative to
`src/dzack_research/preamble/categories/`.

### Completion objects and finite approximations

- [ ] Replace the finite-quotient implementation of multigenerator adic
  completion with a realization of the actual completion.
  **Owner:** `rings/commutative_algebra.py::AdicCompletion` and its parent/
  element implementation; private exact-algebra adapters supply computations.
  **Boundary:** the current polynomial-presentation branch forms the quotient
  by the defining relations plus `I^precision`. Its inherited exact quotient
  arithmetic must not define arithmetic in the completion.
  **Decision:** the completion and its finite quotients are distinct owned
  objects. A computational precision selects available information, not a new
  exact defining relation. Keep `A -> A_hat`, `A_hat -> A/I^n`, and
  `A/I^m -> A/I^n` for `m >= n` as actual maps with their own endpoints.
  Use the inverse-limit definition in
  [Stacks 00M9](https://stacks.math.columbia.edu/tag/00M9).
  **First specimen:** for `A=QQ[x,y]`, `I=(x,y)`, the image of `x^4`
  is nonzero in `A_hat`; its projection to `A/I^4` is zero and to
  `A/I^5` is nonzero. Write this at the ring-completion proof surface.
  **Acceptance:** ring operations, source map, projections and transition
  composition express those three different statements. Replacing the finite
  quotient by a renamed wrapper or adding inverse-system accessors alone does
  not deliver the completion.

- [ ] Establish precision-aware element arithmetic at the shared completion
  boundary, including principal/p-adic and multivariable routes.
  **Decision:** exact elements retain exact defining data or a supported exact
  expression/algorithm. Finite approximations retain their modulus of
  agreement. Equality modulo `I^n` is a statement in the finite quotient,
  not equality of completed elements.
  A difference detected at finite precision proves inequality; agreement at
  one precision alone never proves exact equality.
  Use the repository's assertion-gated computational frontier when an exact
  equality question cannot be decided; do not return a guessed boolean or
  silently replace the exact codomain with a soft knowledge value.
  **Deliver:** compatible addition/multiplication, precision propagation,
  refinement where the underlying data permits it, and exact zero/unit/
  inversion behavior in the supported cases. A finite residue alone cannot
  manufacture higher-precision coefficients.
  **Specimens:** a series agreeing with zero to the initial precision but
  having a later nonzero coefficient; an actual zero; a polynomial image;
  an inverse of `1-x` whose product is exactly one; and a genuine nilpotent
  in the completion of `QQ[x,y]/(x^2)`.
  **Acceptance:** genuine nilpotence survives, truncation artifacts do not.
  Element comparison, truthiness, hashing where defined, and ideal membership
  use compatible equality semantics. Mutable precision must not corrupt caches.

- [ ] Put completion maps and ideals on the correct rings.
  **Owner:** completion parent, ring Hom, and ideal-submodule operations.
  **Decision:** distinguish the source ideal `I <= A`, its extension in
  `A_hat`, and its images in finite quotients; retain their extension maps.
  The completion source map is not automatically injective, and a completion
  along an arbitrary ideal is not automatically a local ring.
  Establish Noetherian, local, complete, separated, and flat properties only
  with the hypotheses supplying each claim.
  **Deliver:** continuous maps induced by compatible ring maps, quotient
  projections, identity/composition, residue comparisons, and the supported
  complete-local maximal ideal through the existing ring/Hom owners.
  **Acceptance:** nonmaximal-adic and maximal-adic examples remain distinct;
  `I=0`, a nilpotent ideal, and a non-separated source are handled by their
  mathematics, not by one blanket parent refinement.
  A method naming every `A/I^n` an Artin quotient must require the
  finite-length hypothesis rather than infer it from the word truncation.

### Module completion and comparisons

- [ ] Make finite-module completion consume the corrected ring completion and
  construct its functorial maps.
  **Owner:** `modules/framed/finitely_generated/finitely_presented_modules.py`,
  module scalar change, and the existing ring completion owner.
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

- [ ] Implement quotient/completion comparisons with hypotheses and actual maps.
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

- [ ] Define the supported localization/completion and base-change comparisons
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

- [ ] Extend normalization and local-length operations beyond the represented
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

- [ ] Extend local homomorphisms and local-module operations only at their shared
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

- [ ] Integrate a construction-order-independent owned category ordering across
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

- [ ] Complete the remaining owned category, Hom, and constructor boundaries.
  **Owners:** the common owned-category runtime, parameterized category bases,
  `rings/ring_foundation.py`, and each surviving mathematical category.
  **Current starting points:** `AdicCompletions`, `RingedSpaces`, and
  `LocallyRingedSpaces` directly use Sage's runtime `Category` base; inspect
  their complete method-packet and ordering paths when integrating them.
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
  **Acceptance:** the full surviving graph has the required ownership, and
  representative quotient, localization, module, group and lattice objects
  expose their promised operations and maps. The terminal graph inspection
  is paired with positive public constructions, never accepted on edge
  removal alone. Include comparisons across available realizations where
  the same mathematical construction has more than one engine.

- [ ] Complete constructor-contract discovery and close the remaining
  variadic/opaque defining-data boundaries.
  **Owners:** the common `object_of` construction path, generated category
  contracts, typed parameterized categories, and surviving functors.
  **Deliver:** named mathematical parameter domains and required data for
  ordinary construction, adopted runtime realizations, Hom construction and
  property refinement. Specializations fulfill inherited accessors before
  returning their objects.
  **Decision:** retain the exact supplied module when equipping distinct algebra
  structures; chosen multiplication/action/presentation is new structure, not
  a property mutation. Refinement cannot overwrite another structure.
  **Acceptance:** source-backed public signatures and constructor examples
  cover an algebra and a module over the same object, a noncommutative regular
  module action into additive endomorphisms, and two multiplications on one
  supplied module. Generic owners do not import their new descendants.
  Keep general class/functor compilation at `sage-categories`, not here.

- [ ] Add preservation specimens around shared algebra edits at the existing
  mathematical proof surfaces.
  **Owner:** `categories/algebras/algebras.py` and its tests.
  **Decision:** a shared-file edit is accepted against both the newly added
  operation and the neighboring mathematical contracts it can disturb.
  **Specimens:** the center of a finite-dimensional associative algebra as a
  subalgebra with its inclusion and multiplication; non-associative central
  submodule behavior; the unital center's unit when the category requires it;
  and the Lie cokernel of the Cartan inclusion in `sl_2(QQ)`.
  Contrast that Lie cokernel with the underlying-module cokernel.
  **Acceptance:** all assertions exercise the public mathematical operations;
  source review covers entire affected methods and class blocks, including
  return paths and indentation. Do not schedule reconstruction of the already
  present center or Lie ideal-quotient algorithms merely to add these controls.

- [ ] Extend general module contracts outside the current finite presentation
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

- [ ] Complete the remaining construction-specific witness and grading
  contracts against their live owners.
  **Deliver:** meaningful parameter types and owned `an_object()` examples;
  general graded-commutativity from a specified parity homomorphism rather
  than an identity check against `ZZ`; inherited self-module structures for
  graded and differential graded algebras; correct formed-module/vector-space
  placements and readable names for the form functors.
  **Decision:** inspect each current implementation before changing it.
  Existing membership and constructor repairs are inputs, not new work.
  **Acceptance:** examples use the stated category's constructors and inherited
  operations. Public exports contain mathematical categories, not abstract
  runtime bases. Finite and infinite signatures retain the same mathematical
  codomain.

## Covering families and sheaves

- [ ] Extend module and algebra descent from one distinguished affine cover to
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

- [ ] Extend the same covering-family owner to non-affine overlaps and to the
  corresponding locally ringed-space and manifold atlases.
  **Deliver:** an affine refinement of a represented non-affine overlap,
  comparison maps between refinements, and local-to-global gluing independent
  of the chosen refinement. Include smooth, topological, and `C^k`
  atlas maps at their respective owners.
  **Decision:** a covering family is not necessarily a distinguished cover of
  one affine scheme. It must not acquire a fictitious global coordinate ring.
  **Acceptance:** the punctured-plane/overlap construction and refinement
  diagrams retain chart labels and both embeddings; non-affine global
  sections do not replace the whole space by their spectrum.

- [ ] Implement sheaf kernels, cokernels, tensor products, local presentations
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

- [ ] Construct inverse image, direct image and module pullback along represented
  scheme morphisms with their correct categories and variance.
  **Decision:** inverse image of a sheaf and tensoring by the target structure
  sheaf are distinct steps of module pullback. Preserve the structural ring
  map and canonical comparison morphisms.
  **Deliver:** functor actions on nonidentity maps, identities, composition,
  and the applicable adjunction unit/counit.
  **Acceptance:** a nontrivial base change of an invertible sheaf agrees via a
  constructed comparison with pulling back its transition data.

- [ ] Extend relative Spec beyond the existing finite cyclic-cover construction.
  **Owners:** algebra sheaves, their affine spectra, and scheme gluing.
  **Deliver:** `Spec_X(A)` for the supported quasi-coherent algebra
  presentations, its map to `X`, nonidentity algebra-map contravariance,
  affine mapping property, and base-change comparison.
  **Decision:** a finite cover algebra is one case, not the definition of
  relative Spec. Retain the algebra's actual underlying module and its
  multiplication under restriction.
  **Acceptance:** a non-cyclic algebra example and a chart-refinement
  comparison use the same owner as cyclic covers.

## Divisors and relative geometry

- [ ] Extend scheme products, fiber products and closed/open subobjects beyond
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

- [ ] Extend divisor and class-group computations from toric presentations to
  the required general and relative schemes.
  **Owners:** `categories/divisors/`, scheme sheaves and local algebra.
  **Deliver:** Cartier local equations and units, Weil prime-divisor
  multiplicities, principal divisors, associated invertible sheaves, and
  Cartier/Picard/Weil/class comparison maps under their stated hypotheses.
  **Decision:** keep the full group of divisors distinct from the torus-invariant
  presentation used by a toric algorithm. Keep `Pic`, the Neron-Severi group,
  and numerical classes distinct, with quotient maps.
  **Specimens:** projective space over a field and over a base contributing
  nontrivial Picard data; a singular normal example where Cartier and Weil
  divisors are not automatically interchangeable.
  **Acceptance:** do not infer `Pic(P^n_S)=ZZ` over arbitrary `S`;
  do not infer singular local factoriality from failure of the regularity
  criterion. Compute geometric relations before equipping the resulting
  group with module or form structure.

- [ ] Complete line-bundle functors and section maps outside the current toric
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

- [ ] Extend linear-system restrictions and jets to general represented closed
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

- [ ] Construct non-toric cycles, rational equivalence and intersection operations
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

- [ ] Turn complete-intersection adjunction data into actual canonical-bundle
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

- [ ] Extend geometric cohomology from the current toric weight complexes to the
  required non-toric schemes and sheaves.
  **Owners:** `categories/schemes/geometric_cohomology.py`, sheaf descent,
  and existing cochain complexes.
  **Deliver:** a geometrically justified complex with its augmentation/
  comparison, induced nonidentity maps, and actual cohomology modules.
  State which cover computes the theory and why it is acyclic or otherwise
  sufficient.
  **Decision:** a complex merely having the expected dimensions is not a
  geometric cohomology construction. Refining a cover produces a comparison
  on complexes and cohomology, not an assertion that two output ranks agree.
  **Acceptance:** a non-toric coherent-cohomology computation and a refinement
  comparison preserve maps and functoriality.

- [ ] Extend the existing Tor/Ext functoriality to both arguments and the
  resolutions needed by geometric consumers.
  **Owners:** module resolutions, chain maps, derived functors, and DGA
  multiplication at the algebra owner.
  **Deliver:** the unresolved argument's induced maps, correct covariance/
  contravariance, comparisons between chosen resolutions, and cohomology
  independence through the appropriate chain-homotopy argument.
  **Decision:** no unsupported bound may turn a prefix of a resolution into
  a complete resolution. Do not require equal chain lifts when only their
  induced cohomology maps are canonical.
  **Acceptance:** nonidentity maps in each argument and two chosen lifts;
  products use a multiplication compatible with the differential and descend
  to cycles modulo boundaries.

- [ ] Extend integral topology, cycle classes and cup-product comparisons beyond
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

- [ ] Extend pointed fundamental groups and Hodge structures to the selected
  geometric realizations.
  **Deliver:** a base point, induced maps for pointed morphisms, and supported
  pure or mixed Hodge data attached to the relevant cohomology.
  **Decision:** a toric trivial-fundamental-group result or diagonal Hodge
  pattern cannot classify a general scheme. Hodge-star operators on formed
  modules are not the Hodge structure of a variety.
  **Acceptance:** a sourced nontrivial fundamental-group or off-diagonal
  Hodge example forces the new geometric computation to do real work.

- [ ] Construct line-bundle linearizations and induced section/cohomology
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

- [ ] Extend fixed loci, quotients and descended maps to the remaining
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

- [ ] Extend `categories/schemes/families.py` to DVR bases through the existing
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

- [ ] Construct formal neighborhoods and formal families as formal objects,
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

- [ ] Add analytic-disc families and their specified comparison with algebraic
  or formal models.
  **Decision:** use the analytic category and its topology. A formal power
  series need not converge; completion does not construct an analytic disc.
  **Deliver:** the analytic family morphism, the supported comparison functor
  and maps, and explicit hypotheses for transporting sheaf/cohomology results.
  **Acceptance:** the selected analytic example has a source-backed comparison;
  do not fabricate a comparison for arbitrary formal input.

- [ ] Construct higher direct images, local systems and monodromy for the
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

- [ ] Extend local singularity classification beyond selected coordinate
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

- [ ] Connect local delta, normalization, and geometric genus globally.
  **Dependencies:** normalization maps, local lengths, and projective gluing.
  **Deliver:** projective curve normalization and the comparison between
  arithmetic and geometric genus, with local contributions at every singular
  point and the applicable connectedness/geometric-integrality hypotheses.
  **Decision:** do not sum a global affine delta once per singular point.
  Base extension can split points and components; retain residue degrees.
  **Acceptance:** a curve with more than one singular point and a curve with a
  nonrational singular point, using an independently sourced genus relation.

## Geometric research applications

- [ ] Construct the `(4,4)` double-cover K3 family over `P^1 x P^1` and
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

- [ ] Construct the Enriques quotient and its lattice comparisons from the
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

- [ ] Implement source-defined ADE and toric log pairs through the existing
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

- [ ] Supply Bertini and general complete-intersection family applications.
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

- [ ] Extend indefinite lattice embeddings and resolve the remaining exact
  isometry algorithm regimes.
  **Owners:** `categories/lattice_morphisms.py`,
  `categories/lattices.py`, and private lattice engines.
  **Deliver:** existence and enumeration for the required indefinite
  codomains, including those not even unimodular; supported indefinite binary
  isometries and the genus/spinor-genus separation cases.
  **Decision:** existence, an explicit embedding/isometry, and a complete
  orbit classification are different outputs. Missing backend support is
  not a negative mathematical answer.
  **Acceptance:** an actual integral form-preserving map, its inverse when
  appropriate, primitivity through its cokernel, and orbit completeness under
  a stated theorem. Equal discriminants or genera alone do not supply a map.

- [ ] Finish rational-integral transporters and cosets through the required
  external arithmetic operations.
  **Owners:** rational matrix groups, lattice stabilizers,
  `categories/orthogonal_quotients.py`, and `sage-indefinite-port`.
  **Deliver:** integral transporter between commensurable lattices,
  right-coset transversals, and double cosets with the precise group actions
  on the finite quotient module.
  **Decision:** finite reduction computes the stated arithmetic object only
  after proving the invariant-lattice/denominator and lifting hypotheses.
  An arbitrary rational matrix group need not admit the required finite
  reduction. Specify the cases, rather than silently bounding denominators.
  **Acceptance:** lift each representative/transporter to an actual rational
  or integral morphism, verify its action on the lattice, and retain exact
  stabilizer inclusions and coset orientation.

- [ ] Extend centralizers from involutions to higher finite-order isometries
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

- [ ] Complete exact rational polyhedral and reduction-complex constructions.
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

- [ ] Implement higher-Witt-index recursion and the `2U` Eichler construction
  through the existing isometry, discriminant and transporter owners.
  **Deliver:** the source-defined subgroup from the two `SL_2(ZZ)`
  actions, Eichler transformations and the required discriminant action;
  finite covering representatives; recursive stabilizers; transporter
  completion to the full orthogonal group; and recursive lattice equivalence.
  **Decision:** state evenness/integrality conditions for every transformation.
  A subgroup generated so far is not the full orthogonal group until the
  generation theorem applies. A covering family is not automatically a set
  of distinct orbit representatives.
  **Acceptance:** explicit action morphisms and a completeness argument,
  with each recursive step decreasing the parameter its termination proof uses.

- [ ] Replace heuristic parabolic constructions by exact integral gluing.
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

- [ ] Complete the remaining chamber and Coxeter operations.
  **Owners:** `categories/coxeter_diagrams.py`, Vinberg invariants,
  hyperbolic lattices and the existing reflection engines.
  **Deliver:** maximal elliptic/parabolic subdiagram posets, dominant cone/
  fundamental chamber and chamber-complex maps, and the number-field root
  computation in its valid arithmetic regimes.
  **Decision:** retain root-to-diagram maps and exact edge/vertex weights;
  bounded search is not a nonreflectivity proof. Reuse projectively weighted
  graph objects and the current Vinberg/edge-walk implementations.
  **Acceptance:** sourced finite, affine, noncrystallographic and hyperbolic
  literature examples distinguish the asserted regimes.

- [ ] Assemble the three arithmetic research constructions with their maps.
  **Lorentzian:** `U + E8(-1)`, its orthogonal/component groups, cusp orbit,
  cusp stabilizer, unipotent radical and map onto the definite reduction group.
  **Higher Witt index:** `U + U(2) + E8(-2)`, line and plane orbits,
  stabilizers, Tits-building incidence and subgroup splitting under the
  discriminant representation.
  **Equivariant:** the K3 lattice with an Enriques involution, its integral
  invariant/anti-invariant decomposition and gluing, full centralizer,
  polarization stabilizer intersection, and anti-invariant isotropic orbits.
  **Acceptance:** actual inclusions, projections, group maps and transporters,
  not a table of expected invariants. Their execution belongs to T.

## Framework transfer and organization

### Organization findings

- [ ] Transfer each remaining subsystem to `sage-categories` only with its
  complete mathematical dependency path.
  **Inputs:** read the upstream `specs/system.md`, `specs/leaves.md`,
  `specs/functor.md`, and `specs/leaf-scaffolding.md` at that transfer.
  **Deliver:** leaf constructors, structural functors on objects and morphisms,
  inherited data/operations, and the real downstream algorithm; retire the
  covered local runtime responsibility in the same unit.
  **Decision:** arbitrary abelian-group/bimodule realization and the remaining
  generic monoidal/class/static-projection work belong upstream. A matching
  category name or a specification is not an implemented dependency.
  Explicit functor reuse may keep a preamble consumer coherent before full
  automatic inheritance; it must not duplicate the underlying algorithm.
  **Acceptance:** a nonidentity morphism and inherited operation work through
  the transferred construction without a second mathematical object system.

- [ ] Finish collection ownership and typing on the surviving interfaces.
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
  **Acceptance:** infinite/repeated-label specimens and nontrivial consumers
  retain their mathematics. A list/tuple count or annotation count alone
  cannot remove this item.

- [ ] Finish ownership-directed package, export and import consolidation after
  the affected interfaces settle.
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

- [ ] Complete the archive-to-live reconciliation without recreating supplied
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
  **Acceptance:** source-backed reconciliation for every required notion.
  Record completed dispositions in commits, not a historical table here.

## Final verification

### Testing is deferred until every other item is done (always-on)

The terminal-T rule is defined by `DEV-58` in
[CONTRIBUTING.md](CONTRIBUTING.md). Write falsifying mathematical specimens
with implementation and commit them unverified. Do not execute them during
the preceding workstreams. Optional research consumers below do not delay T.

- [ ] After required implementation and transfer are finished, generate the
  preamble reference and category/functor graph from the integrated source,
  then read them against the intended objects, maps and inherited operations.
  **Acceptance:** documentation describes that source and exposes the
  mathematical contracts. Generation success alone is not a correctness claim.

- [ ] Execute the prescribed public-construction and mathematical suites in the
  terminal verification phase through the existing project recipes.
  **Scope:** expectation subtrees, ring/module/algebra/action contracts,
  completion versus truncation, geometric constructions and comparisons,
  transferred framework consumers, and the valid archive/literature specimens.
  Include the permitted construction-order/session tests on the integrated
  tree and notebook checks through `japi`.
  **Acceptance:** each claimed behavior is exercised through the actual
  public path. An unverified assertion, suite count, or backend-only test is
  not proof of the corresponding construction.

- [ ] Repair the mathematical owners exposed by terminal verification and
  establish the originally required behavior.
  **Decision:** do not weaken expectations to match an implementation, filter
  required failures, infer false from missing algorithms, or turn the failure
  list into unrelated architectural work. A mathematically incorrect
  expectation may change only under the exception in `AGENTS.md`, with
  the correction justified in its commit.
  **Acceptance:** the actual failed proposition is established and the
  affected downstream construction remains coherent.

- [ ] Verify the required session/rendered examples and final contribution
  contracts after mathematical integration.
  **Deliver:** actual inspected notebook/rendering results where relevant,
  source-backed terminology review at the required push boundary, and the
  repository's prescribed final QC.
  **Acceptance:** the displayed mathematical objects and maps are correct;
  no output is certified solely by a generated file or a server starting.
  Respect the user's push approval and active-task scope.

## Optional research consumers

These are not prerequisites for the required mathematics or terminal T.

- [ ] Add further notebook/rich-display examples only for a named research
  question using live objects. Use existing polygon, Three.js, and diagram
  rendering owners; do not install implicit global display hooks.
- [ ] Add a database/classification example when it supplies data needed by
  research: LMFDB, curve/field databases, OEIS, GRDB, Kreuzer--Skarke or
  Fanography. Select a concrete mathematical query before provisioning an
  adapter.
- [ ] Extend private engine integrations when a named construction benefits:
  Sage/Singular for local and polynomial algebra, libGAP for group actions,
  persistent `sage-julia-bridge` for OSCAR/Hecke, optional Macaulay2 for
  its exact algebra strengths, and `py_polyhedral` for required polyhedral
  binaries. Maxima stays within its symbolic-calculus domain.
  **Decision:** search existing interfaces first; provision only the needed
  dependency; put reusable codecs and bridge defects at their actual owner.
  Mathematical outputs always return as owned objects and maps.

## Work coordination

### Claim and release

Use the existing shared-checkout transaction mutex before editing this queue
or staging/committing in a shared index:

```sh
flock -n -E 75 /home/dzack/research/.git/preamble-coordination.lock bash --noprofile --norc
```

Keep that shell alive through the transaction, then exit it to release the OS
lock. Exit 75 means the transaction is occupied; it is not a mathematical
blocker. Under the mutex, reread this queue and inspect `git status --short`,
`git diff --cached --name-only`, `git rev-parse HEAD`, and
`git worktree list`. Do not stage another writer's changes.

Reserve exact files or directory paths ending in `/`, with write/read mode,
owner, checkout, dependency revision and UTC update. Overlapping reads can
coexist; an overlapping write conflicts. Reserve both paths for a rename.
Acquire a claim's resources together or none. Include export and generated
files only when the work will edit them. A live kernel is a separate resource.

Claims are active coordination, not completed work. A timestamp is not a lease
expiry. Do not remove a reservation without release/handoff by its owner or
an explicit ownership decision. A claim does not grant permission to overwrite
uncommitted work. Preserve dirty paths with unidentified owners.

When waiting on a dependency, release resources no longer being edited.
Coordinate shared-contract changes with affected consumers; a path lock alone
does not keep their input interface stable. Readers in separate worktrees use
their pinned dependency; shared-checkout readers wait for the relevant
contract edit, not for unrelated workstreams.

At delivery, commit the construction and its unverified specimens, remove the
delivered TODO item or only its delivered obligations, and remove the released
claim under the mutex. Put evidence and reasoning in the commit.
Do not add a completed row or release-history section. If a new regression is
found later, write a new task from the then-current source and its desired
behavior.

### Active claims

| Claim | Stream / concrete release | Owner task/session and checkout | Reserved resources and mode | Base / checkpoint | Updated UTC |
| --- | --- | --- | --- | --- | --- |
| `A1-actual-group-algebra-parent-20260907-1700` | A1 / actual `R[G]` module parent and retained scalar restriction | Chat continuation 2026-09-07 Asia/Taipei; `/home/dzack/research` | `src/dzack_research/preamble/categories/modules/group_modules/group_modules.py; src/dzack_research/preamble/categories/functors/group_actions.py; src/dzack_research/preamble/categories/functors/group_scalar_change.py; tests/groups/test_actual_group_algebra_modules.py; src/dzack_research/preamble/categories/modules/group_modules/isotypic.py; src/dzack_research/preamble/categories/functors/group_induction.py; tests/groups/test_g_objects.py; tests/groups/test_restricted_actions.py` (write) | `152301b80e4ac18fa0684998c454bf54e34183ae` | 2026-09-07T07:57:50Z |
| `LATTICE-parabolic-gluing-20260908-0832` | arithmetic / exact parabolic Levi image | Chat continuation 2026-09-08; `/home/dzack/research` | `src/dzack_research/preamble/categories/lattices.py; tests/lattices/test_parabolic_gluing.py` (write) | `9f36bcb0` | 2026-09-08T08:32:00Z |
