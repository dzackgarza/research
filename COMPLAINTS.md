# Foundational Gaps and Papercuts

Record unresolved issues observed anywhere in research or contribution work.
The primary subject is general mathematical machinery that should be available
but is missing, incomplete, or bypassed in the owned language. Concrete workflow
papercuts also belong here. This is neither a retrospective work log nor a list
of hypothetical defects.

Use the [mathematical tracing method](CONTRIBUTING.md#mathematical-dependency-tracing)
and the capture/lifecycle rule
[`DEV-59`](CONTRIBUTING.md#dev-59-record-observed-foundational-gaps-and-papercuts).
State the mathematics before its implementation symptoms. Extend an existing
entry when another consumer exposes the same foundation. Link execution details
in [TODO.md](TODO.md); keep implementation ordering and active reservations there.
Remove resolved entries with evidence in the commit, retaining only unfinished
needs and any required terminal verification. Durable definitions and decisions
belong at their mathematical declarations or in CONTRIBUTING, not solely here.

## Foundational Mathematics

### Localization must define its fraction-field specialization

**Mathematical need.** For a commutative ring `R` and a multiplicative submonoid
`S` of its multiplicative monoid, localization supplies `S^(-1)R`, the ring map
from `R`, and the universal factorization of ring maps that invert `S`. The
fraction field of an integral domain is the case of its nonzero elements. Prime
localization and inversion of selected elements are other specializations, not
independent definitions of fractions. See the
[localization examples](https://stacks.math.columbia.edu/tag/02C5) and the
[required construction factorizations](CONTRIBUTING.md#required-construction-factorizations).

**Dependency trace.** Fraction field -> localization at the specified submonoid
-> commutative rings and ring morphisms, multiplicative monoids and submonoid
inclusions -> sets, operations, maps and their laws; universal factorization
uses the ring category and its Homs. Module use adds modules and scalar change
along that particular ring map. The unmet requirement is threading the special
case through this general construction, not inventing fraction arithmetic.

- **Searched:** `OwnedRings.ParentMethods.fraction_field` and
  `OwnedIntegralDomains.ParentMethods.fraction_field_map` in
  [ring_foundation.py](src/dzack_research/preamble/categories/rings/ring_foundation.py),
  and the complete element/submonoid dispatch functions in
  [commutative_algebra.py](src/dzack_research/preamble/categories/rings/commutative_algebra.py).
- **Found:** the general fraction-field method returns an owned version of
  `engine.fraction_field()`; the source map is constructed separately. Element
  and prime routes already enter `_localization_at_submonoid`.
- **Conclusion:** source evidence supports a missing common construction path
  for this fraction-field specialization. It does not support a claim that
  localization or fraction-field computation is absent from the repository.
- **Confidence:** high for the inspected construction path.
- **Gaps:** no runtime execution; not every specialized ring override or
  fraction-field consumer has been inspected. Re-read live source before repair.

**Consequences and resolution.** Scalar extension and localization consumers
need the submonoid, source map and comparison to belong to the same construction.
Use the maintained fraction-field computation privately while supplying that
datum at the general localization owner. Do not mutate a shared field to store
one caller's source, and do not infer locality for every localization. The
[localization work item](TODO.md#localization-specializations-through-one-construction)
owns the implementation, affected consumers and distinguishing specimens.

### Completion must be a limit rather than one quotient

**Mathematical need.** Completion with respect to an ideal `I` is the inverse
limit of the rings `R/I^n`, with their transition maps. Module completion uses
the corresponding quotients `M/I^n M`. A finite stage and the completed object
have different mathematical roles. The canonical source maps, projections,
and induced maps on completions belong to the construction. See
[Stacks, Completion](https://stacks.math.columbia.edu/tag/00M9).

**Dependency trace.** Completion -> inverse system and its limit -> ideal
powers, quotient rings/modules and quotient morphisms -> ring/module structure,
subobjects and the relevant categories -> sets, functions and algebraic laws.
The index category, functor describing the system, cones, and projections use
the common categorical foundations. The required product/equalizer realization
and restrictions of systems belong to that general theory, as specified in the
[limit/colimit contract](CONTRIBUTING.md#limits-colimits-and-structured-specialization).
A computational series realization specializes the same owned construction by
inheritance or composition (`OWN-14`); a comparison of answers from parallel
implementations is not sufficient. It does not replace the definition by one stage.

- **Searched:** the complete `AdicCompletion` factory in
  [commutative_algebra.py](src/dzack_research/preamble/categories/rings/commutative_algebra.py),
  together with its existing TODO contract and the definition of completion.
- **Found:** the multigenerator presented-algebra branch adds the selected ideal
  power to the defining relations and passes that finite quotient as the engine
  realization. The principal and p-adic branches call maintained completion
  operations. Common diagram and inverse-system declarations also exist in
  [products.py](src/dzack_research/preamble/categories/abstract_categories/products.py).
- **Conclusion:** the inspected branch needs a realization of the actual limit
  connected to the general construction. Renaming its quotient or adding
  projection accessors does not supply that realization. This is not a claim
  that the repository lacks all diagrams or all completion computations.
- **Confidence:** high for the finite-quotient construction observed in source.
- **Gaps:** no runtime execution or exhaustive element-arithmetic review; the
  supported realizations of general presented-algebra completions still need
  capability research. Source declarations alone do not establish a working
  general inverse-limit construction.

**Consequences and resolution.** Module completion, continuous morphisms,
formal neighborhoods and completed families need the same completed object,
not independent truncation conventions. Use the existing quotient and diagram
owners and maintained completion/series implementations, preserving the actual
scope of exactness and comparison theorems. General diagram restriction must
remain usable through the specialized completion, with the actual source and
projection maps. Retain the full system and finite restrictions separately;
the ideal-power indexing gives stage access its precision interpretation.
The [shared construction work](TODO.md#shared-diagrams-and-universal-constructions)
owns this integration with the general mathematical foundation. This requirement
does not assert that every general diagram operation is currently absent: the
source coverage and unresolved questions above remain the evidence boundary. The
[completion work items](TODO.md#completion-objects-and-finite-approximations)
own realization selection, precision semantics and integration; their downstream
module and family work must consume that construction.

### Cohomology needs a common complex contract in boundary degrees

**Mathematical need.** In a complex, degree-`n` cohomology uses both the outgoing
differential and the image of the incoming differential. A complex concentrated
in nonnegative degrees still has a zero incoming map at degree zero. Equipping
that complex with DGA structure must preserve the same component and differential
contract. The existing
[cohomology construction](src/dzack_research/preamble/categories/modules/cochain_complexes.py)
states the cycle-quotient definition.

**Dependency trace.** DGA cohomology -> the underlying complex and compatible
graded multiplication -> graded modules, differentials, kernels, images and
quotients -> modules and module morphisms, scalar rings and actions -> additive
groups, sets and maps. Boundary components use the zero object and zero
morphisms of the same module category. Adding multiplication does not create
another definition of the incoming differential or of the cycle quotient.

- **Searched:** `Cycles`, `Boundaries`, `Cohomology`, and the component methods
  of `CochainComplexObject` in
  [cochain_complexes.py](src/dzack_research/preamble/categories/modules/cochain_complexes.py),
  and `DifferentialGradedAlgebras.ParentMethods.differential_component` in
  [differential_graded_algebras.py](src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py).
- **Found:** `Boundaries` requests the component in degree `n-1`. The represented
  nonnegative cochain-complex route supplies a zero incoming map, while the DGA
  method rejects a negative component request. The DGA category names the
  cochain-complex category among its supercategories.
- **Conclusion:** these inspected contracts disagree at the degree-zero boundary;
  the inherited complex structure needs reconciliation. This is a source-level
  mismatch, not a claim that a particular runtime session has been reproduced
  failing or that a general cohomology algorithm must be written.
- **Confidence:** high for the conflicting source contracts; runtime dispatch
  remains unverified.
- **Gaps:** the complete generated method-resolution behavior and every DGA
  specialization were not executed or exhaustively inspected.

**Consequences and resolution.** Ordinary complexes and DGAs must supply the
same zero-component and differential data to the shared cohomology functor.
Repair that common contract rather than special-casing the degree-zero quotient
or omitting it. The [shared complex and DGA work](TODO.md#shared-complex-and-dga-integration)
owns the boundary specimens, inherited structures and maintained computation
selection. Its broader grading and coefficient obligations remain intact.

## Workflow Papercuts

Add concrete observed workflow friction here under a descriptive heading, with
the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution. Foundational mathematical gaps belong
above even when first noticed as an inconvenient method or notebook interaction.
