# Archive Port Outstanding Work

**Testing is deferred until every item in these queues is done.** Run no tests,
no QC gates, no Sage and no notebooks against this work. A port is an
architecture edit: read the archived notion, reconcile it against the live
owner, write the construction and the test that would falsify it, and commit
unverified. Red is the expected state until the last unit lands.
[TODO-PRIORITIES.md](TODO-PRIORITIES.md#testing-is-deferred-until-every-other-item-is-done-always-on)
owns the rule and its two narrow exceptions.

Mathematical requirements for the preamble, including work originating in `archives/preamble/`.
An unchecked row can include an implemented case whose extension remains open.
Inspect the current source before selecting its missing mathematical output.
Original section numbers are retained for source references.

[TODO-PRIORITIES.md](TODO-PRIORITIES.md#current-objective-and-order) owns execution order and the boundary for local category work.
General scheme theory is the active mathematical program, developed alongside `sage-categories`.
Its foundation is a coherent algebraic subtree with reusable module, ring, algebra, and functor constructions.

## Geometry delivery sequence

- [ ] Close the quotient/localization/module dependencies in §8.4 using the family `xy=t`, its reducible special fiber, and its local rings.
  Extend the existing distinguished-open construction with restriction maps on functions and modules.
- [ ] Complete affine `Spec` on ring morphisms, closed immersions, and fiber products through the algebra constructions in §§8.4–10.
- [ ] Supply structure sheaves, localized modules, projective affine charts, and gluing from §§8.4 and 9.4, with their restriction and transition maps.
- [ ] Build general group actions from §13.1 and reuse them for sets, modules, schemes, and induced actions on invariants.
- [ ] Connect the toric character and cocharacter constructions in §16 to the preamble's module and lattice operations.
- [ ] Build the divisor, line-bundle, cycle, and cohomology constructions in §11 with their comparison maps and computational hypotheses.
- [ ] Construct relative cyclic covers, fixed subschemes, and supported quotients through the sheaf and action constructions in §13.
- [ ] Extend the local theory in §12 and the families and higher direct images in §15 through the same algebraic and sheaf owners.
- [ ] Make each general construction available through the notebook session with its defining maps and supported algorithms.

The sequence selects complete constructions along their mathematical dependencies.
Develop the algebraic foundation before its dependent geometric operation, while allowing independent constructions to proceed together.
Affine charts and stalks expose objects in that foundation, where categories supply the applicable algorithms.
The scheme layer assembles local results through restriction and gluing maps.
State computational regimes explicitly and extend them through established engines while retaining general mathematical ownership.

## Existing mathematical implementations to extend

These source locations establish implementation scope, not current execution results:

| Construction | Current owner under `src/dzack_research/preamble/` | Extension boundary |
| --- | --- | --- |
| Algebra structure and underlying module | `categories/algebras/algebras.py`, `categories/functors/algebra_modules.py` | Complete constructor threading and inherited module operations for each geometric algebra. |
| Isotropic subobjects, flags, orbit representatives, transporters, and stabilizers | `categories/isotropic_orbits.py`, `categories/lattice_morphisms.py` | Compose the existing operations into the required incidence and research calculations. |
| Arithmetic-subgroup orbit splitting | `categories/orthogonal_quotients.py`, `categories/group/predicate_subgroups.py` | Extend the represented character-subgroup cases to the subgroup required by the application. |
| Centralizer image on the discriminant form | `categories/lattice_morphisms.py::centralizer_discriminant_image`, `categories/lattice_engines.py` | The full arithmetic centralizer and equivariant orbit calculations are distinct outputs. |
| Embeddings and isometries | `categories/lattice_morphisms.py`, `categories/lattices.py` | Extend supported target and witness regimes; distinguish existence, a morphism, and orbit classification. |
| Rooted Coxeter diagrams and elliptic/parabolic subdiagrams | `categories/coxeter_diagrams.py` | Extend to required chamber, reflection, and subdiagram-orbit constructions. |

Retain the existing definite-lattice, finite-form, gluing, module, and algebra algorithms when categories become framework leaves.
Their defining data and exact engine calculations remain useful across the transfer.

## 0. Owned-category and backend-neutral architecture

Apply these obligations to the active construction and its shared dependencies under the local Cat work criteria in `TODO-PRIORITIES.md`.
Reuse the existing implementations; earlier completion notes are retained there.
General automatic interpretation of declared functors and constructor inheritance is developed in `sage-categories`.
Local repairs provide coherent reuse until the corresponding framework consumer is ready.

- [ ] Complete the graph-purity migration: every mathematical `super_categories()` edge in the live preamble must run only between owned categories. Sage category nodes (`sage.categories.*`) may be queried privately to recognize capabilities of a concrete engine object, but must never be semantic supercategories, public theorem hypotheses, or part of the owned category graph.
- [ ] Replace remaining subclasses/usages of Sage parameterized category bases whose constructors impose Sage mathematical-category membership. In particular, categories parameterized by a ring/module/group/etc. must store the owned base object directly; the owned base need not itself lie in Sage's corresponding category graph.
- [ ] Audit all category constructors with custom `__classcall__`/`__classcall_private__` logic after the parameterized-category migration. Normalize parameters through owned constructors (`own_ring`, owned groups, etc.) and do not use Sage category membership as the criterion that the parameter is mathematically valid.
- [ ] Complete the owned Hom/End/Aut packet architecture at foundational levels. `Hom_C(A,B)`, `End_C(A)`, and `Aut_C(A)` are owned category constructions; runtime inheritance from Sage Homsets may be used only where Python's `Morphism` machinery requires it, never to define the mathematical Hom notion.
- [ ] Complete and consistently use the existing `RingHomset` and `RingMorphism` in `categories/rings/ring_foundation.py`.
  Extend their kernel, factorization, and algebra-map connections as specified in §8.4.
  Quotient, localization, residue, completion, and structure maps must retain the owned Hom and their mathematical endpoints.
- [ ] Remove public uses of `Hom(..., SageRings())`, `Hom(..., SageSets())`, `Hom(..., SageGroups())`, Sage `Modules(R)`, Sage `Algebras(R)`, and analogous constructions whenever the intended arrow is a mathematical arrow in an owned category. Replace them by the corresponding owned Hom object; retain Sage Hom calls only at explicit private engine boundaries.
- [ ] Remove Sage mathematical categories from foundational owned categories: `Sets`, finite/infinite/countable set refinements, magma/semigroup/monoid/additive variants, groups/abelian/finite groups, semirings/rngs/rings/commutative rings/domains/division rings/fields/finite fields, modules/vector spaces, associative/unital/commutative algebras, graded variants, and any descendants whose semantic inheritance still reaches a Sage category node.
- [ ] Do the same purity audit in the less central branches after the foundation is stable: graded modules/algebras, profinite groups, G-sets, forms/value modules, connections, function spaces, enumerated/ordered sets, divisors, lattices, Coxeter structures, schemes, and other category families. Backend predicates can witness owned placement; they cannot be inherited semantic structure.
- [ ] Separate object identity from computational realization uniformly. There is one owned mathematical object such as `R/I`, `S^{-1}R`, `S^{-1}M`, `Spec(R)`, `O(L)`, etc.; Sage/Singular/GAP/OSCAR/Hecke/Maxima/Macaulay2/`py_polyhedral` implementations are interchangeable private engines or algorithms. Never expose a "native" versus "fallback" mathematical class distinction merely because different computations are available.
- [ ] Where a mathematically canonical owned carrier is useful (literal quotient cosets, localization fractions, arbitrary set/action modules, categorical subobjects, etc.), retain it independently of backend availability. Attach cached engine realizations/conversions opportunistically rather than replacing the public parent with the engine parent.
- [ ] Conversely, do not require every object to be copied into a bespoke Python carrier when an existing parent is an efficient storage realization. A Sage parent or Julia handle may back the owned object, but its engine category/class must remain private metadata and may be swapped without changing the mathematical API.
- [ ] Introduce a small capability/realization registry on owned objects or private backend adapters: ask for operations such as Groebner basis, syzygy, Smith form, primary decomposition, normalization, group stabilizer, lattice isometry, etc.; select Sage/Singular/GAP/OSCAR/etc. internally; cross results back to owned objects/morphisms/subobjects.
- [ ] Remove wording and APIs that describe mathematically equivalent carriers as "fallback" objects. Use terms such as owned carrier, represented carrier, engine realization, or backend adapter only when the distinction is genuinely computational.
- [ ] Eliminate reliance on Sage generic coercion discovery for constructors whose semantics the preamble owns. Owned parents (tensor modules, general/localized modules, quotient/localization rings, Hom parents, lattices, etc.) should construct known input forms directly instead of asking Sage to synthesize conversion maps through its category graph.
- [ ] Audit `Parent.__call__` paths for dict/tuple/callable/generator-image constructors. In owned Hom parents and other structured parents, route these inputs directly to the owned `_element_constructor_`/explicit constructor so Python input types do not trigger Sage's generic `Hom(..., SetsWithPartialMaps())` machinery.
- [ ] Restore any elementary operations that were accidentally inherited only from Sage category mixins (`zero`, `one`, additive/scalar actions, identities, etc.) as explicit owned-category/object methods. Removing Sage supercategory edges must expose missing owned mathematics rather than be repaired by reattaching the Sage edge.
- [ ] Audit all uses of `candidate in SageSets()/SageRings()/SageGroups()/...`: distinguish private engine recognition from public mathematical membership. Public `Sets()/Rings()/Groups()/...` membership must work for owned carriers even when they are not Sage objects of the analogous category.
- [ ] Make owned set membership broad enough to contain every owned mathematical parent through the owned graph. Set-valued Hom objects, subobjects, spectra, lattices, modules, schemes, etc. must not need parallel Sage-set classification merely to be legitimate objects of `Sets()`.
- [ ] Keep size/enumerability/commutativity/domain/field/etc. engine predicates as placement witnesses only. Once witnessed, refine into owned property categories; callers should then ask owned predicates/categories rather than Sage categories.
- [ ] Add graph-purity regressions that recursively inspect the foundational owned category graph and fail if a Sage mathematical category appears in `super_categories()`. Permit Sage runtime classes only in explicit implementation fields/engine adapters, not semantic edges.
- [ ] Add backend-independence regressions for representative objects: construct or realize the same quotient/localization/module/group/lattice computation through two available engines/carriers where practical and verify the public owned category, structure maps, and mathematical operations agree without engine-specific branches in user code.
- [ ] Audit `engine_ring`/analogous helpers so they mean "selected computation realization" rather than "the true underlying object". Generalize the pattern to other domains where multiple engines are useful; avoid APIs that assume Sage is privileged as the unique backend.
- [ ] Keep the current dirty-tree migration safe while doing the graph-purity pass: repair exposed missing owned operations incrementally and run broad foundational regressions after each cluster; do not restore Sage supercategory edges merely to make an old constructor pass.

## 8. Remaining module-level algorithms

### 8.2 Presented modules over more general bases

- [ ] Extend Smith/Hermite/presentation operations beyond `ZZ`/fields only where theorem/backend support exists.
- [ ] Extend the now-live general module carrier (arbitrary represented set with explicit additive structure and scalar action, stored as `rho:R -> End(M)`) through the rest of the owned module graph: make the additive-group structure itself a first-class owned construction where useful, remove remaining dependence of `Modules(R)` on Sage's native module category as mathematical structure, and preserve Sage modules only as optimized computational realizations.
- [ ] Extend linearity verification dispatch for elementwise module morphisms: generator-defined framed/FP maps remain linear by construction with relation checks; finite represented carriers/rings are exhaustively checked; add exact engine/symbolic/PID-specific checks where they genuinely prove the callable agrees with a linear map, and keep DEBUG-only diagnostics for declared callables outside decidable regimes.
- [ ] Extend the now-live rank distinction beyond represented finite modules: `rank_at(p)=dim_{kappa(p)}(M tensor_R kappa(p))`, finite-projective local rank, and generic/Matsumura rank over domains are separate APIs and must remain so. Add rank-function objects/stratifications on `Spec(R)` and locally constant rank for finite projectives; support infinite-cardinal generic rank only when the module/cardinal infrastructure genuinely represents it.
- [ ] Extend the existing fraction-module localization and its transported presentations through exact relation computations over local rings; §8.4 owns the source-grounded scope.
  Preserve the existing module fibers, residue modules, minimal generating sets, and Nakayama surjectivity operations.
- [ ] Extend the existing Fitting/support/fiber-dimension operations to local-freeness loci with their trivializations and comparison maps.
  Extend annihilators beyond their Smith and cyclic-presentation cases at the scalar-action kernel owner.
- [ ] Generalize torsion/torsion-free predicates without guessed booleans.
- [ ] Generalize cardinality using the cardinal of the base and actual decomposition.
- [ ] Generalize exponent/annihilator vocabulary only where meaningful; a nonzero free abelian group does not have exponent `1`.

### 8.3 Module automorphism groups/action homsets

- [ ] Audit archived `ModuleAutomorphism`, `ModuleAutomorphismGroup`, `AutomorphismSubgroup`, `SubFramingMorphism` against live generic machinery.
- [ ] Port only missing mathematical operations: actual automorphism groups, subgroup inclusions, sections/retractions/one-sided inverses, and action homsets.

### 8.4 Commutative-algebra foundation required by scheme theory

The following assessment traces the requested geometry through the working source inspected on 2026-09-05, including uncommitted implementations.
It establishes source-level construction paths and explicit restrictions; it does not establish fresh Sage execution results.
The named owners below were read at their constructors and dependent operations.
A definition search across `src/dzack_research/preamble/` supplied the surrounding scope; archive implementations and external engine coverage remain separate investigations.

The existing foundation is substantial: polynomial presentations, quotient maps, ideal submodules, module kernels, scalar change, differentials, and affine constructions.
The immediate problem is closure under the operations geometry applies to them.
A polynomial quotient can supply a differential module while its prime localization is rejected.
A localization can retain a module presentation while its fraction equality cannot use that presentation.
Closing these paths supplies several geometric constructions from the same algebraic work.

#### Equations, affine maps, and fibers

[`free_algebras.py`](src/dzack_research/preamble/categories/algebras/free_algebras.py) constructs polynomial and Laurent algebras, selected polynomial quotients, coefficient base change, coproducts, and pushouts.
`_quotient_by_algebra_elements_backend` already combines new equations with an existing presentation's relations.
[`schemes.py`](src/dzack_research/preamble/categories/schemes/schemes.py) contains affine spaces, equation-defined embeddings, distinguished-open immersions, and affine fiber products using these operations.
[`AffineSpecFunctor`](src/dzack_research/preamble/categories/schemes/affine_spec.py) already acts on objects and morphisms of commutative algebras over a fixed ring.
`Schemes` also supplies slice objects over `Spec(R)` through the shared `SliceOver` construction.

The boundaries occur at the maps and presentations.
`AffineSchemes.closed_subscheme` calls `FinitelyPresentedAlgebra` directly on its coordinate algebra, whose constructor requires a symmetric algebra.
Thus a second closed embedding into a presented quotient needs the existing quotient-of-presentation operation.
The pushout backend accepts concrete `AlgebraMorphism` instances; presented and ring morphisms have separate implementations.
`Spec` and `affine_spec_morphism` require Sage realizations, and the latter requires a common represented algebra base.
[`RingMorphism.kernel`](src/dzack_research/preamble/categories/rings/ring_foundation.py) currently delegates only to a selected module-annihilator provider.

- [ ] Consolidate successive quotients, ring and algebra quotient presentations, and their maps while preserving the chosen scalar ring.
  The same presentation must serve subschemes, fibers, module coefficients, and differentials.
- [ ] Make the existing coproduct, pushout, and affine-Spec paths accept the required owned ring/algebra maps through their mathematical Hom owners.
  Supply quotient factorization, localization factorization, kernels, images, and ideal extension/contraction in supported presentation regimes.
- [ ] Represent a chosen parameter map as an algebra structure with a usable relative presentation.
  `own_algebra(structure_map)` currently makes an unframed algebra, while algebra scalar extension requires a chosen finite polynomial presentation.
  Thread the presentation through parameter changes so explicit families retain computable fibers and relative differentials.
  Extend the existing slice construction to the required general scheme bases and commuting family morphisms.

#### Localizations, stalks, and exact modules

[`CommutativeIdeal`](src/dzack_research/preamble/categories/rings/commutative_ideals.py) already constructs ideals as submodules of the regular module.
It uses engine syzygies, or a principal-domain case, to obtain their presentations.
Its methods include sum, product, intersection, powers, radical, colon, saturation, primary decomposition, and associated primes when the engine supplies them.
This is broader than integer and number-order ideals.
Localization extension is implemented; contraction uses a remembered source ideal and a finitely generated denominator monoid.

[`commutative_algebra.py`](src/dzack_research/preamble/categories/rings/commutative_algebra.py) contains prime spectra, specialization, `V(I)`, `D(f)`, quotients, and localizations.
`PrimeLocalization` explicitly requires an integral domain and selects its fraction field as engine.
`quotient_localization_comparison` supplies maps in both directions for finitely generated denominator monoids.
General prime complements fall outside that comparison.

[`finitely_presented_modules.py`](src/dzack_research/preamble/categories/modules/framed/finitely_generated/finitely_presented_modules.py) supplies presented kernels over PIDs and polynomial quotients over fields through Singular syzygies.
It lifts coefficient-ring relations into the free-module presentation for quotient-coefficient equality.
[`ModuleLocalizationFunctor`](src/dzack_research/preamble/categories/functors/module_localization.py) transports objects, morphisms, inclusions, and kernel/cokernel comparisons.
[`LocalizedModule`](src/dzack_research/preamble/categories/modules/localizations.py) transports selected presentations too.
Its fraction-equality implementation uses source equality, a torsion-free case, and finite-set enumeration; it does not consume the transported relation presentation for general torsion modules.

- [ ] Extend prime localization and its ideal/module operations to represented reducible and nonreduced polynomial quotients.
  The local ring of `QQ[x,y]/(xy)` at `(x,y)` is a first required case for singular fibers.
  Preserve residue maps and the comparison between quotient-then-localize and localize-then-quotient.
- [ ] Correct local unit and ideal semantics in the shared ring implementation.
  `LocalizationRings` asks its engine about units; `PrimeLocalizations` selects a fraction field, where every nonzero element is a unit.
  Unit testing in `QQ[x]_(x)` must instead reflect its maximal ideal.
  `OwnedRings.Commutative.ideal` also selects `LocalizedMaximalIdeal` views for prime-localized ideals; connect these to the same ideal-submodule operations.
- [ ] Compute equality, vanishing, and relation membership of localized finitely presented modules using supported saturation/local-algebra algorithms.
  Localizing `QQ[x]/(x)` at `x` must produce the zero module through those algorithms.
  Its infinite underlying set is irrelevant to that computation.
- [ ] Extend exact module calculations to maps constructed directly over localized coefficient rings, alongside the existing transport of known source kernels.
  Reuse this path for overlap compatibility, sheaf kernels, conormal modules, and finite algebra calculations.
- [ ] Preserve represented spectrum points, residue fields, and scalar maps across these constructions.
  Extend local homomorphisms and maximal-ideal compatibility through that same path.

#### Differentials, singular loci, and flatness

[`KahlerDifferentials`](src/dzack_research/preamble/categories/algebras/kahler_differentials.py) already constructs the differential module from the derivatives of polynomial relations.
It retains the universal derivation and factorization to a target module.
Its presentation reader in [`derivations.py`](src/dzack_research/preamble/categories/algebras/derivations.py) accepts symmetric algebras and chosen finite polynomial presentations.
The presented-module owner already computes Fitting ideals, support, and fiber-dimension loci.
`Modules` supplies residue modules and fibers; the presented owner selects minimal module generating sets by residue linear algebra.
`ModuleMorphism.is_surjective_by_nakayama` already uses the residue morphism.
Annihilators currently have Smith and cyclic-presentation implementations.

- [ ] Connect differential modules to localization, scalar change, the conormal sequence, and change of relative base.
  Route cotangent spaces and tangent maps through the existing module fiber and Hom operations.
- [ ] Construct smooth and singular loci from the differential/Fitting calculations with the correct relative hypotheses and scheme structures.
  Supply local dimension, regularity, and component data where the criterion needs more than the differential presentation.
- [ ] Extend annihilators beyond Smith and cyclic presentations, using the existing scalar-action kernel owner.
  Use the resulting ideals for support and local-freeness calculations.
- [ ] Establish finite projectivity, local freeness, and flatness in the supported presentation regimes.
  `ProjectiveModules` currently records placement and computes rank through fibers; it does not decide projectivity from a presentation.
  Supply actual local trivializations and comparison maps for invertible modules and finite locally free algebras.
- [ ] For families over a DVR, connect supported torsion and module calculations to the applicable flatness criterion.
  A chosen morphism to the base alone supplies neither flatness nor its locus.

#### Affine covers, invertible sheaves, and cyclic covers

[`StructureSheaf`](src/dzack_research/preamble/categories/schemes/ringed_spaces.py) delegates global sections, distinguished-open sections, and affine stalks to scheme methods.
The affine methods return the existing algebra, its localizations, and prime local rings.
This supplies local values; §9.4 still needs the restriction morphisms and compatible overlap/gluing constructions.
The sections method accepts a distinguished-open inclusion in the prime spectrum, while `AffineSchemes.distinguished_open` returns a scheme with its inclusion.
Connect these representations so the same geometric open determines its sections and restriction maps.
`ProjectiveSpace` currently adopts the Sage space; its standard charts must connect to the same algebraic theory through graded localization and degree-zero parts.

[`algebra_from_multiplication`](src/dzack_research/preamble/categories/algebras/algebras.py) already builds an algebra from a module multiplication map.
The presented-algebra constructor also selects finite-free module data for supported one-variable quotients.
[`AlgebraUnderlyingModuleFunctor`](src/dzack_research/preamble/categories/functors/algebra_modules.py) transports free tensor/symmetric algebras through graded module sums and otherwise returns the existing algebra object.
These are useful beginnings for finite cover algebras; usable inherited module data and the affine-Spec realization must agree.

- [ ] Supply restriction maps between localizations and their composition, cover refinements, and gluing of objects and morphisms through §9.4.
  Localize the same module presentation for sheaf restrictions and stalks.
- [ ] Build graded localization, degree-zero chart algebras, and overlap maps for `Proj` through the existing graded algebra owners.
- [ ] Glue rank-one locally free modules with their transition units, tensor powers, and section maps.
  Use these for Cartier divisors, line bundles, and the cyclic cover algebra in §13.2.
- [ ] Make the cyclic algebra's multiplication, underlying finite module, local equation presentation, and scalar changes share one construction.
  Relative `Spec` then glues its affine spectra and structure maps.
  Ramification calculations use the differential and Fitting operations above.

#### Divisors, cycles, and completed local geometry

The constructors in [`divisors/`](src/dzack_research/preamble/categories/divisors/) equip supplied modules with divisor, class-group, or Picard roles.
`PicardGroup(module)` requires a supplied framed module; it does not compute a scheme's invertible sheaves or their quotient by isomorphism.
The finite module and formed-module structures can receive the geometric results once those are constructed.

`AdicCompletion` in `commutative_algebra.py` accepts a principal ideal and calls the selected engine's completion operation.
`PowerSeriesRing` and `DualNumbers` provide additional local examples.
Their local-base constructors currently store only the new variable in the maximal ideal; extension of the base maximal ideal needs repair.
A multigenerator maximal-adic completion of a singular affine algebra is outside the completion constructor's explicit input regime.

- [ ] Supply total quotient rings where needed, regular-element predicates, height-one localizations, orders of vanishing, and finite local lengths.
  Use these for Cartier/Weil comparison, principal divisors, fundamental-cycle multiplicities, and local intersections.
- [ ] Extend finite/integral algebra theory with normalization, integral closure, conductor ideals, and the maps needed for curve normalization and divisor classes.
  Retain dimension, prime-height, minimal-prime, Artinian-factor, and support computations at their algebraic owners.
- [ ] Implement the supported normality, regularity, and local-factoriality criteria required by the comparisons in §11.
  Construct Picard and class groups from their geometric relations before equipping the results with module or form structure.
- [ ] Extend completion to local polynomial quotients, multigenerator ideals, and finite modules, with quotient/localization comparison maps.
  Retain adic inverse systems and the Noetherian hypotheses for exactness, separatedness, and flatness.
  Keep finite precision attached to the engine realization.
- [ ] Correct local-base power-series and dual-number maximal ideals, including the image of the base maximal ideal.
  Reuse the resulting DVR, residue-field, valuation, and completion maps in formal families and singularity calculations.

#### Group actions, toric geometry, and global cohomology

[`GSets`](src/dzack_research/preamble/categories/group/g_sets.py) has a finite enumerated permutation realization with equivariant maps, orbits, and fixed-point sets.
[`GroupModule`](src/dzack_research/preamble/categories/modules/group_modules/group_modules.py) uses a selected finite module presentation and supplies module invariants and coinvariants.
The action constructors are specialized to these objects; §13.1 must supply their common categorical construction and its scheme specialization.
For an affine quotient, a module of invariants must additionally obtain its algebra multiplication and a computable algebra presentation.
Finite-point fixed-set enumeration cannot supply a scheme-theoretic fixed ideal.

[`polytopes.py`](src/dzack_research/preamble/categories/schemes/polytopes.py) already uses a preamble free integer module and a private normal-fan engine.
The required continuation is characters/cocharacters, semigroup algebras of cones, and their localization maps and gluing in §16.
These depend on the same presented-algebra and cover machinery above.

[`Cohomology`](src/dzack_research/preamble/categories/modules/cochain_complexes.py) computes a kernel/image quotient of a supplied complex.
[`CohomologyAlgebra`](src/dzack_research/preamble/categories/algebras/cohomology_algebras.py) obtains products from a supplied DGA.
[`DeRhamAlgebra`](src/dzack_research/preamble/categories/algebras/de_rham_algebras.py) reuses differential modules and exterior powers for affine algebraic de Rham theory.
`modules/hodge.py` constructs exterior-algebra duality and Hodge-star operations on finite free modules with extra data.
These operations do not construct the singular cochains or Hodge structure of a scheme.
The selected presented-module `free_resolution` builds a length-one PID resolution; higher local homological computations need a wider resolution regime.

- [ ] Build the common action construction through the existing Hom and functor owners, then add scheme equalizers and supported invariant-algebra quotients.
- [ ] Extend the toric algebra and gluing constructions in §16 using the existing integer modules and polytope computations.
- [ ] Supply supported longer resolutions and `Tor`/`Ext` calculations for the local intersection and sheaf computations that need them.
  Reuse existing tensor, internal-Hom, kernel, cokernel, and cohomology operations.
- [ ] Construct the geometric complexes and comparison maps required for coherent cohomology, integral singular cohomology, and higher direct images.
  Covers and local algebra supply inputs; topology, cup products, cycle classes, and monodromy require their own justified constructions.
  Connect their output modules to the existing formed-module and lattice theory.

#### Existing engine integration obligations

- [ ] Backend routing policy: keep mathematical objects, inclusions, structure maps, universal properties, and functorial laws in the preamble, but delegate algorithmic engine work to established CAS backends wherever available. Backend-specific matrices/ideals/handles/process protocols remain private and every public result must be crossed back into live owned objects/morphisms/subobjects.
- [ ] Use Sage's native commutative-algebra interfaces, and hence Singular where Sage routes there, for Groebner bases, syzygies, elimination, ideal membership/reduction, saturation/colon computations, dimensions/Hilbert data, polynomial quotient calculations, resolutions, and primary-decomposition/associated-prime computations in the regimes those backends actually support. Do not reimplement these algorithms in Python.
- [ ] Audit Sage's Singular bridge before adding any owned algorithmic code for polynomial/local singularity computations; use direct Singular only when Sage does not expose the needed exact operation cleanly, and keep the direct interface behind one private adapter.
- [ ] Use `libgap`/Sage's GAP-backed parents for finite/combinatorial group calculations, automorphism groups, stabilizers, orbit calculations, and group homomorphism algorithms rather than duplicating GAP algorithms in the preamble.
- [ ] Restore `sage-julia-bridge` as the canonical persistent Julia/OSCAR/Hecke boundary. Instantiate/provision the bridge's Julia project so its declared `JSON` dependency is available, initialize `using Oscar` through the bridge, and make bridge availability a normal backend capability rather than bypassing it.
- [ ] Replace the current raw `julia` subprocess + temporary-matrix-file + stdout-parsing code in `categories/lattice_engines.py` with `sage-julia-bridge` calls/handles and structured Sage<->Julia conversions; preserve the owned row/column/tensor convention checks at the private crossing only.
- [ ] Reuse the bridge's structured integer/rational/vector/matrix codec and opaque `JuliaHandle` support; add conversion registrations to `sage-julia-bridge` when a reusable mathematical Sage<->OSCAR conversion is missing instead of building one-off text protocols in the preamble.
- [ ] Prefer OSCAR/Hecke through `sage-julia-bridge` for lattice/quadratic-form, number-field/order, normalization, and exact algebra computations when it is materially stronger than Sage's native backend; verify returned data at the owned mathematical boundary rather than duplicating the engine algorithm.
- [ ] Treat Macaulay2 as an optional advanced commutative-algebra backend: Sage's M2 interface is present but no `M2`/`Macaulay2` executable is currently provisioned. Once available, use it where it materially improves free resolutions, Betti data, local/cohomological algebra, or primary decomposition instead of recreating those algorithms.
- [ ] Use Maxima only for symbolic-calculus operations it actually owns; do not route exact algebraic ideal/module computations through Maxima merely because the executable is present.
- [ ] Maintain a small backend-capability layer selecting among Sage/Singular, `libgap`, OSCAR via `sage-julia-bridge`, optional Macaulay2, Maxima, and specialized wrappers such as `py_polyhedral`; mathematical code should ask for an operation/capability rather than shelling out to a particular executable itself.

## 9. Scheme and algebraic-geometry foundation

### 9.1 Ringed spaces and schemes

- [ ] Affine and projective spaces over `Spec(R)` with their structure morphisms, affine or homogeneous coordinate algebras, and standard charts.
- [ ] Construct closed subschemes from equations in those algebras, with homogeneity required in the projective case; retain the ideal sheaf and embedding.
- [ ] Complete `Spec` as a contravariant functor on the owned ring-Hom construction.
  Make affine pullback intrinsic data of the scheme Hom, using shared Hom and functor machinery for endpoints and construction reuse.
- [ ] Extend the now-live affine stalks `O_{Spec R,p}=R_p` beyond the current domain/prime-localization regime and integrate them with general ringed-space/local-intersection constructions.
- [ ] Populate exact generic membership/refinement for quasi-affine, quasi-projective, integral, separated, finite-type, normal, and smooth scheme properties beyond the currently placed base/affine/projective spaces.

### 9.2 Subschemes

- [ ] Integrate closed-subscheme inclusions with the generic `SubobjectCategory`; native equation-defined closed embeddings already land as live scheme morphisms.
- [ ] Extend the existing distinguished-open immersions to general represented open subschemes and their gluing.
- [ ] Complete function and module restriction maps on principal opens, reusing their existing localization maps.
- [ ] Scheme-theoretic intersections.
- [ ] Intersection multiplicity from correct local/stalk/Tor definitions with hypotheses visible.

### 9.3 Varieties, curves, surfaces

- [ ] `Varieties(S)` with finite-type/separated/integral hypotheses explicit.
- [ ] `Curves(S)` and `Surfaces(S)` as dimension subcategories.
- [ ] Toric varieties through the toric-scheme layer.
- [ ] Arithmetic and geometric genus as distinct invariants.
- [ ] Curve normalization data and relation to delta invariants.

### 9.4 Affine covers, gluing, and sheaves

- [ ] Represent affine covers by open immersions, with overlap opens, transition isomorphisms, and their restriction maps.
  Refine overlaps by affine covers when needed; retain the refinements and comparison maps.
- [ ] Glue schemes and scheme morphisms from compatible local data.
  Check inverse and cocycle conditions on represented overlaps through the underlying algebra morphisms where equality is decidable.
  Use the mapping properties in [Stacks, gluing schemes](https://stacks.math.columbia.edu/tag/01JA).
- [ ] Construct sheaves of `O_X`-modules and `O_X`-algebras from modules and algebras on affine opens and compatible overlap identifications.
  Reuse localization and scalar extension for restrictions; glue morphisms as well as objects.
- [ ] Compute sections on supported covers from compatible local sections, with their restriction maps.
  Compute stalks through the existing local-ring and module-localization constructions.
- [ ] Supply sheaf kernels, cokernels, tensor products, and local presentations through their algebraic owners.
  State the sheaf category and hypotheses required for each operation.
- [ ] Implement inverse image, direct image, and pullback of modules along a scheme morphism with their correct source and target categories.
  Distinguish inverse image of a sheaf from scalar extension defining module pullback.
- [ ] Construct relative `Spec_X(A)` for a quasi-coherent `O_X`-algebra from affine spectra and their gluing maps.
  Retain its structure morphism and compatibility with base change.

## 10. Categorical scheme operations and products

- [ ] Products of schemes as categorical products over the stated base.
- [ ] Extend the now-live products of projective spaces and finitely presented affine schemes to the remaining general affine/projective cases while preserving actual categorical projections.
- [ ] Mixed affine/projective/base-change products without backend strings as API.
- [ ] Extend the now-live affine fiber products/pullback squares `Spec(B tensor_A C)` to non-affine/mixed cases and verify gluing/base-change compatibility.
- [ ] Inverse images of closed subschemes.
- [ ] Diagonals as morphisms/subobjects.
- [ ] Graph morphisms/subschemes.
- [ ] Equalizers and fixed subschemes.
- [ ] Scheme-theoretic image.
- [ ] Base change of schemes with identity/composition laws.
- [ ] Slice and coslice categories using the shared categorical constructions, with their objects and commuting morphisms.
  Schemes over `S` and families `X -> S` use `Sch/S`; pointed constructions use the appropriate coslice.
- [ ] Base change on objects, morphisms, and automorphisms over a base, with the induced commuting squares.
- [ ] Composition along a base morphism and its relation to pullback in slice categories.
  Lift or descend automorphisms only with the required compatibility and descent data.
- [ ] Parameter spaces of sections and relative `Spec` through the sheaf constructions in §9.4 and families in §15.

## 11. Picard groups, line bundles, intersections, cohomology, and sections

### 11.1 Picard and divisor groups

- [ ] Attach live `PicardGroup`, `ClassGroup`, `CartierDivisorGroup`, `WeilDivisorGroup` functorially to schemes where defined.
- [ ] Natural Cartier/Picard to Weil/class comparisons under correct hypotheses.
- [ ] Compute Cartier divisors by local equations with their associated invertible sheaves; compute Weil multiplicities and principal divisors at their divisor owners.
- [ ] Supply exact supported predicates for normality, regularity, and local factoriality, and use them to establish the applicable comparison isomorphisms.
  For locally Noetherian integral schemes, use [the Picard-to-class-group comparison](https://stacks.math.columbia.edu/tag/02SI).
- [ ] Distinguished `O(1)` on projective space.
- [ ] Field cases `Pic(A^n)=0`, `Cl(A^n)=0`, `Pic(P^n)=Z`, `Cl(P^n)=Z` through the general objects.
- [ ] General-base projective-space Picard group including the base contribution; do not hard-code field formulas.
- [ ] `Pic(P^1 x P^1) ~= Z^2` and standard generators.
- [ ] Picard lattice/intersection pairing on surfaces such as `P^1 x P^1`.
- [ ] Keep `Pic(X)` as an abelian group or `ZZ`-module; equip it with the intersection form where defined.
  Expose the Néron–Severi group and numerical divisor classes with their quotient maps when those are the computed objects.
  Specialize to preamble lattices when the chosen group is finite free and satisfies the required form hypotheses.
  Record the polarization when a higher-dimensional intersection pairing requires one.

### 11.2 Line bundles/intersections

- [ ] `O(d_1,...,d_r)` on products of projective spaces.
- [ ] Tensor product/addition, dual/inverse, powers.
- [ ] Pullback and base change.
- [ ] Canonical and anticanonical bundles.
- [ ] Ampleness predicates where exact.
- [ ] Intersection pairings and top self-intersections.
- [ ] Complete-intersection adjunction through the actual canonical bundle.

### 11.3 Cohomology/sections

- [ ] `H^i(X,L)` as actual modules/vector spaces.
- [ ] Exact cohomology dimensions on supported projective spaces/products.
- [ ] Pullback/restriction maps on global sections as actual linear morphisms with kernels/cokernels.
- [ ] Sections <-> homogeneous polynomials.
- [ ] Section rings as graded algebras.
- [ ] Cox rings with Picard/multigrading.
- [ ] Homogeneous-degree lookup in the Cox ring.

### 11.4 Linear systems

- [ ] Complete linear systems `|L|`.
- [ ] Associated projective morphism.
- [ ] Base loci and basepoint-freeness.
- [ ] Restriction/evaluation maps to closed subschemes.
- [ ] Jets and imposed-singularity conditions.
- [ ] Parameter spaces of sections.
- [ ] Bertini-family interfaces only with correct genericity statements.

### 11.5 Algebraic cycles and cycle classes

- [ ] Construct the codimension-graded cycle groups `Z^r(X)` in supported dimension regimes.
  Send a closed subscheme to its fundamental cycle, using local lengths for component multiplicities.
- [ ] Form Chow groups `CH^r(X)` by rational equivalence, with cycle representatives and quotient maps where computable.
  Relate codimension-one cycles, Weil divisor classes, and `Pic(X)` through the comparisons in §11.1.
- [ ] Supply proper pushforward, flat pullback, and supported intersection products with their hypotheses and degree shifts.
- [ ] Construct cycle class maps to the supported cohomology or homology theory, with coefficients and grading explicit.
  Relate divisor classes to first Chern classes and intersection products to cup products where the comparison applies.

### 11.6 Topological invariants and cohomology forms

- [ ] For schemes with a specified complex realization, compute supported singular cohomology groups `H^i(X; ZZ)` and their graded ring structure.
  Preserve integral torsion and induced maps; keep coherent-sheaf cohomology in §11.3 distinct.
- [ ] Realize cup-product pairings as preamble formed modules in the regimes where evaluation gives the required value module.
  For smooth projective surfaces, construct the middle-cohomology lattice on `H^2(X; ZZ)` modulo torsion.
  Support the torsion-free K3 case directly, with divisor cycle classes as actual module morphisms.
- [ ] Extend these constructions to specified mild singularities using the appropriate ordinary, intersection, or resolution cohomology.
  State comparison maps and the hypotheses for nondegeneracy or duality for the selected theory.
- [ ] Compute supported fundamental groups with a base point and induced homomorphisms when the pointed morphism is available.
- [ ] Compute supported Hodge numbers; state purity or mixed-Hodge grading and connect to the relevant cohomology objects.
- [ ] Use established topological and geometric algorithms for global invariants.
  Reuse affine-local algebra for their local inputs and module algorithms for the resulting groups, maps, and pairings.

## 12. Singularities of curves and schemes

- [ ] Local regularity/singularity testing through `O_{X,x}`, its maximal ideal, residue field, and completion.
  Retain the localization, residue, and completion maps and their supported computational presentations.
- [ ] Construct the smooth locus of a morphism as an open subscheme in supported finite-presentation settings.
  Construct the singular or nonsmooth closed subscheme using a stated ideal-sheaf convention and hypotheses.
  Distinguish regularity of local rings from smoothness over the specified base.
- [ ] Zariski tangent spaces.
- [ ] Jacobian criterion in supported finite-type settings.
- [ ] Milnor algebras/numbers for isolated hypersurface singularities.
- [ ] Tjurina algebras/numbers.
- [ ] ADE normal-form/type recognition with explicit scope/hypotheses.
- [ ] Classify supported pointed singularities using their local or completed local algebras and established algorithms.
  Return the equivalence notion and any constructed coordinate change with the classification.
- [ ] Archived `A_n` and `D_n` plane-curve families.
- [ ] Delta invariants and relation to normalization/geometric genus.

## 16. Toric schemes and varieties

- [ ] `ToricSchemes(S)` as schemes with torus/fan structure, not hard-coded fan recognition.
- [ ] Represent the character and cocharacter lattices `M` and `N` of a split torus through existing preamble free `ZZ`-modules and their module duality.
  Elements represent actual characters and cocharacters, with the perfect evaluation pairing `M x N -> ZZ`.
  A chosen frame gives the standard `ZZ^n` presentation and permits reuse of `I_{n,0}` operations through its underlying module.
  Keep the chosen positive form distinct from the character–cocharacter pairing.
- [ ] Construct affine toric charts from cone semigroup algebras and glue along face-localization maps through §§8.4 and 9.4.
- [ ] Use lattice homomorphisms compatible with fans to construct toric morphisms and the induced algebra maps.
- [ ] Compute supported toric divisor, class, Picard, and cohomology data through the general objects in §11.
- [ ] Construction from rational fans.
- [ ] Construction from lattice polytopes via normal fans.
- [ ] Preserve polarizing-polytope relation.
- [ ] Native Sage toric varieties only as backend realizations.
- [ ] Toric closed subschemes as ordinary closed subschemes; general hypersurfaces are not toric automatically.
- [ ] Standard identifications (`P^n`, `P^1 x P^1`, weighted projective spaces, Hirzebruch surfaces, etc.) only as proven isomorphisms or exact derived display metadata.

## 13. Cyclic covers, involutions, fixed loci, and quotients

### 13.1 Group actions in a category

- [ ] Construct objects with a `G`-action from a group morphism `G -> Aut_C(X)`, using the existing group, Hom, and functor machinery.
  Define morphisms by equivariance in `C`, with the forgetful functor to `C` explicit on objects and morphisms.
- [ ] Develop `G`-sets and equivariant maps at that generic owner.
  Relate linear actions on `R`-modules to `R[G]`-modules, including `ZZ[G]`, through the module and algebra constructions.
- [ ] Specialize the same construction to `C = Sch/S` and reuse it for induced actions on sheaves, sections, divisors, and cohomology.
  Record variance and any preserved form on the induced action.
- [ ] Support restriction along a group homomorphism and transport through functors when the required functorial action is defined.
- [ ] Distinguish abstract-group actions from group-scheme actions over a general base; use each with its actual morphisms and hypotheses.

### 13.2 Relative cyclic covers and deck groups

- [ ] Cyclic-cover data `(L,s,n)` with branch section in `H^0(X,L^n)`.
- [ ] Cover algebra `oplus_{i=0}^{n-1} L^{-i}` with multiplication from the branch section.
- [ ] Construct the cover by relative `Spec` of that `O_X`-algebra, using its module operations and affine gluing.
- [ ] Finite cover morphism as an object of `Sch/X`, with its base changes and morphisms over `X`.
- [ ] Branch and ramification subschemes.
- [ ] Canonical-bundle formula under correct hypotheses.
- [ ] Smoothness criteria in supported cases.
- [ ] Deck group as the automorphism group of the cover object over its base, with its action on the covering scheme.
  Determine when the cyclic construction supplies a `mu_n`-action and when it identifies with the intended constant cyclic group.
  Retain characteristic, roots-of-unity, and separability hypotheses in ramification and quotient computations.
- [ ] Lifts of base automorphisms preserving/scaling the branch section; two lifts for double covers when they exist.
- [ ] Action on holomorphic top forms when cohomology is present.
- [ ] `(4,4)` K3 double-cover family and two lifts of the diagonal sign involution.

### 13.3 Fixed subschemes and quotients

- [ ] Fixed subschemes of automorphisms as equalizers, and common fixed subschemes for represented group actions.
  Compute fixed ideals on affine charts through the ring-morphism and ideal algorithms, then glue.
- [ ] Decide emptiness of supported fixed subschemes and expose the resulting fixed-point-free predicate.
  Distinguish absence of common fixed points from freeness of the whole group action.
- [ ] Fixed-point evaluation and equivariant section-space actions.
- [ ] Fixed-locus/representation/Lefschetz compatibility under the applicable geometric and topological hypotheses.
- [ ] Construct quotients for supported cyclic groups and involutions, with the quotient morphism and universal property.
  Compute affine invariant rings through established algebra algorithms and glue when the quotient hypotheses permit it.
- [ ] Descend equivariant morphisms and compatible automorphisms through those quotients.
  State the hypotheses for compatibility with base change, including for families.
- [ ] Enriques quotient only after fixed-point-free and compatibility conditions are actual predicates/morphisms.

## 14. Complete intersections, del Pezzo geometry, and blowups

- [ ] Complete-intersection detection and defining degrees.
- [ ] Mathematical complete-intersection datum/object rather than generic certificate records.
- [ ] Normality and Gorenstein predicates where exactly decidable.
- [ ] Canonical/anticanonical bundles by adjunction.
- [ ] Del Pezzo degree and predicate via ampleness of `-K`.
- [ ] Blowups of the projective plane and supported smooth surfaces.
- [ ] Exceptional divisors and Picard/intersection changes.
- [ ] Strict transforms of curves/divisors.
- [ ] Archived del Pezzo blowup benchmarks.

## 15. Families, local bases, and higher direct images

- [ ] Represent families as morphisms `f: X -> S` in the slice category, with fibers and base changes through §10.
  Record flatness, properness, and smoothness as additional properties of the morphism when established.
- [ ] Construct a family from polynomial equations by specifying the parameter algebra and its map into the coordinate algebra.
  Selecting `z` as parameter in equations in `x,y,z` gives a morphism to the `z`-line.
  Compute fibers using the corresponding residue-field base change and determine flatness in supported regimes.
- [ ] Support bases given by DVRs and their spectra, generic and special fibers, and base change to completions.
  Reuse the valuation, localization, residue-field, and completion constructions in §8.4.
- [ ] Support complex-disc families in the analytic category, with explicit comparison to algebraic or formal models when available.
  State which topology each sheaf and cohomology operation uses.
- [ ] Construct supported higher direct images of the constant integral sheaf and their stalks.
  Supply the comparison with fiber cohomology when the hypotheses of [proper base change in topology](https://stacks.math.columbia.edu/tag/09V4) apply.
- [ ] On suitable smooth strata, represent the resulting local systems and monodromy as actual group actions on cohomology modules.
  Retain specialization and comparison maps when supported, using the same module, sheaf, and action owners.
- [ ] Build relative cyclic covers and compatible quotient families by applying §13 over the specified base.

## 7. Representation theory of `R[G]`-modules and group lattices

- [ ] Restricted automorphism actions on invariant/isotypic pieces.
- [ ] `(4,4)` involution example with `13+12` section-space decomposition after geometry lands.

## 3. Integral Lattices, Elements, Reductions, and Arithmetic Groups (Semantic API Contracts)

### 3.1 Lattices (`L`)

- [ ] `B = L.gram_tensor()`: actual symmetric $(0,2)$-tensor.
- [ ] `M = L.gram_matrix(basis=None)`: coordinate presentation of $B$.
- [ ] `L.b(v, w)`: bilinear pairing $b_L(v,w)$.
- [ ] `L.q(v)`: quadratic evaluation $b_L(v,v)$ without $1/2$ factor.
- [ ] `L.metric_map()`: canonical map $L \to L.\operatorname{linear\_dual}()$.
- [ ] `L.linear_dual()`: exact module dual $\operatorname{Hom}_{\mathbb{Z}}(L, \mathbb{Z})$.
- [ ] `L.dual_lattice()`: dual lattice $L^\vee$ inside $L \otimes \mathbb{Q}$.
- [ ] `L.discriminant_module()`: finite formed module $A_L = L^\vee/L$ with quadratic form $q(x + L) \in \mathbb{Q}/2\mathbb{Z}$ (even) or bilinear form (odd).
- [ ] Invariant predicates: `L.signature()`, `L.radical()`, `L.is_even()`, `L.is_nondegenerate()`.
- [ ] `L.sublattice_from(vectors, saturate=False)`: returns a subobject pair $(S, \iota: S \hookrightarrow L)$ with inclusion morphism, never an unattached Gram matrix.
- [ ] `L.primitive_sublattice_from(vectors)`: saturated subobject via Smith normal form of the quotient.
- [ ] `L.orthogonal_complement(I)` / `L.perp(I)`: orthogonal subobject pair $(I^\perp, \iota: I^\perp \hookrightarrow L)$.
- [ ] `L.O()`: full finitely generated arithmetic group $O(L)$.
- [ ] `L.O_plus()`: stable orthogonal group $\widetilde{O}(L) = \ker(O(L) \to O(A_L))$.
- [ ] `L.O_component()`: positive cone component group $O^\Omega(L)$, when a component is specified.
- [ ] `L.isometry_to(M)`: returns an actual `LatticeIsometry` morphism $f: L \to M$ or `None`.
- [ ] `L.is_isometric_to(M)`: verified boolean predicate.
- [ ] Locus objects: `L.vector_locus(norm=m, primitive=False)`, `L.isotropic_sublattice_locus(rank=k)`, `L.isotropic_flag_locus(ranks=(d1, ..., dr))`.

### 3.2 Lattice Elements (`v`)

- [ ] `v.parent()`: lattice $L$.
- [ ] `v.to_vector(basis=None)`: coordinate row vector.
- [ ] `v.to_covector()`: dual evaluation $\beta_L(v) \in L.\operatorname{linear\_dual}()$.
- [ ] `v.is_primitive()`: primitivity test in $L$.
- [ ] `v.divisor()`: positive generator of the ideal $b(v, L) \subset \mathbb{Z}$.
- [ ] `v.discriminant_class()`: associated class $[v / \operatorname{div}(v)] \in A_L$ for primitive $v$.
- [ ] `v.is_isotropic()`: test $L.q(v) == 0$.
- [ ] `v.sublattice()`: rank-1 subobject $\mathbb{Z}v \hookrightarrow L$ with inclusion morphism.
- [ ] `v.orthogonal_complement()` / `v.perp()`: orthogonal complement $(v^\perp, \iota: v^\perp \hookrightarrow L)$.
- [ ] `v.isotropic_reduction()`: rank-1 isotropic reduction object.

### 3.3 Sublattices and Isotropic Reductions (`I`, `R`)

- [ ] `I.ambient_lattice()`: derived codomain of inclusion morphism $\iota.\operatorname{codomain}()$.
- [ ] `I.inclusion()`: embedding morphism $\iota: I \hookrightarrow L$.
- [ ] `I.basis()`: basis elements of $I$.
- [ ] `I.rank()`: rank of $I$.
- [ ] `I.saturation()`: saturated closure $I_{\text{sat}} \hookrightarrow L$.
- [ ] `I.is_primitive()`: saturation test via Smith invariants of $L/I$.
- [ ] `I.is_totally_isotropic()`: test $b(x,y) = 0$ for all $x,y \in I$.
- [ ] `I.perp()`: orthogonal complement $(I^\perp, I^\perp \hookrightarrow L)$.
- [ ] `R = I.isotropic_reduction()`: structured reduction object for $K_I := I^\perp / I$ (torsion-free, non-degenerate of signature $(p-k, q-k)$ for $\operatorname{rk}(I)=k$ and $\operatorname{sig}(L)=(p,q)$):
  - `R.isotropic_sublattice()`: original subobject $I$.
  - `R.orthogonal_complement()`: $I^\perp$.
  - `R.quotient_lattice()`: non-degenerate formed quotient lattice $K_I = I^\perp / I$.
  - `R.inclusion()`: inclusion morphism $I \hookrightarrow I^\perp$.
  - `R.projection()`: canonical projection morphism $I^\perp \twoheadrightarrow K_I$.
  - `R.levi_action()`.
  - `R.unipotent_kernel()`.
  - `R.lift_isometry(...)`.

### 3.4 Orthogonal and Arithmetic Groups (`G = L.O()`) and Subgroup Constructors

- [ ] `G.ambient_lattice()`: underlying lattice $L$.
- [ ] `G.gens()`, `G.one()`, `G.element(matrix)`, `G.contains(g)`.
- [ ] `G.discriminant_representation()`: reduction homomorphism $\rho_A: G \to O(A_L)$.
- [ ] `G.component_character()`: character $\chi_\Omega$, when defined.
- [ ] `G.kernel(phi)`: kernel subgroup for homomorphisms $\phi$.
- [ ] `G.preimage(phi, H)`: preimage subgroup.
- [ ] `G.stable_subgroup()`: kernel of $\rho_A$ on discriminant form.
- [ ] `G.component_subgroup()`.
- [ ] `G.centralizer(f)`: centralizer $Z_G(f)$.
- [ ] `G.stabilizer(v)`: point stabilizer of vector $v$.
- [ ] `G.stabilizer(I, action="setwise")` and `G.stabilizer(I, action="pointwise")`: setwise and pointwise stabilizers of sublattice $I$.
- [ ] `G.intersection(H1, ..., Hr)`: intersection of subgroups.
- [ ] `G.transporter(x, y)`: element $g \in G$ mapping $x \mapsto y$.
- [ ] `G.orbit_decomposition(X)`: orbit representatives, stabilizers, and transporters on locus $X$.
- [ ] Structured subgroup parents retaining construction provenance:
  - `GeneratedSubgroup(generators)`
  - `KernelSubgroup(phi)`
  - `PreimageSubgroup(phi, H)`
  - `StabilizerSubgroup(G, object, action)`
  - `CentralizerSubgroup(G, f)`
  - `IntersectionSubgroup(G1, ..., Gr)`
- [ ] Finite-quotient double coset splitting for $\Gamma = \rho^{-1}(H) \leq O(L)$: $P_x \backslash G / \Gamma \cong \rho(P_x) \backslash \rho(G) / H$ computed via libGAP.

### 3.5 Rational Matrix Groups and Integral Lattice Stabilizers

- [ ] `integral_stabilizer(G_Q, L)`: computes $G \cap \operatorname{GL}(L) = \rho^{-1}(\operatorname{Stab}_{\rho(G)}(S_L))$ for rational matrix group $G = \langle g_1, \dots, g_r \rangle \leq \operatorname{GL}(V_{\mathbb{Q}})$ and commensurable lattice $dM \subseteq L \subseteq M$.
- [ ] `integral_transporter(G_Q, L1, L2)`: computes rational element making $g L_1 = L_2$ integral.
- [ ] `integral_right_cosets(G_Q, L)`: computes right-coset transversals of $G_L$ in $G$.
- [ ] `integral_double_cosets(V_Q, G_Q, L)`: computes $V \backslash G / G_L$ on finite quotient module $F_M = M/dM$ via libGAP.

### 3.6 Centralizers $O(L,f)$ and Equivariant Lattices

- [ ] Involution centralizer algorithm for $f^2 = 1$: eigenspaces $V_\pm = \ker(f \mp 1)$, sublattices $L_\pm = L \cap V_\pm$, gluing subgroup $H_L = L/(L_+ \oplus L_-) \subset A_{L_+} \oplus A_{L_-}$, and $O(L,f) \cong \{(g_+, g_-) \in O(L_+) \times O(L_-) : (g_+, g_-)(H_L) = H_L\}$.
- [ ] Cyclotomic decomposition for finite-order $f$: $\bigoplus_{d \mid \operatorname{ord}(f)} V_{\Phi_d}$, sublattices $L_d = L \cap V_{\Phi_d}$, and equivariant gluing stabilizer.
- [ ] Semantic decorated lattice types: `Lf = L.with_isometry(f)`, `Lf.centralizer_group()`, `Lf.equivariant_sublattice(...)`, `Lf.equivariant_isometry_to(Mg)`.
- [ ] Equivariant orbit enumeration on decorated objects $(L,f)$ preserving $b_L$ and $f$ at every stage.

### 3.7 Finite Configuration, Graph Labeling, and Polyhedral Primitives

- [ ] **Pairing configuration graphs**: Encoding vector/facet pairings into colored graphs with vertex/edge invariants.
- [ ] **Graph canonization interface**: Interface to Sage's Bliss/Nauty backend for canonical graph labeling and automorphism groups.
- [ ] **Permutation lifting**: Lifting graph automorphism permutations to integral lattice isometries via `libgap`.
- [ ] **Exact rational polyhedral cones**: Facet enumeration, extreme rays, incidence, and face stabilizers delegating to Normaliz, cddlib, or PPL.

### 3.8 Reduction Complex, Transporters, and Lorentzian Base Case

- [ ] **Reduction cell and transporter interfaces**: Structured `ReductionCell` and `AdjacentCell` records.
- [ ] **Lorentzian perfect-domain engine**: Signature $(1,n)$ component group $O^\Omega(L)$ and full group $O(L) = O^\Omega(L) \times \langle -I \rangle$.
- [ ] **Marked-vector cell extension**: Traversal of perfect domains carrying marked nonzero-norm vector sets for general Lorentzian vector orbits.

## 5. Indefinite Recursion, Parabolic Induction, and Milestones

### 5.1 Higher-Witt-Index $2U$-Eichler Approximate Models and Recursion

- [ ] **$2U$-Eichler model**: For $L = U \oplus U \oplus K$, generate $A(L) = \langle SL_2(\mathbb{Z})_{\text{left}}, SL_2(\mathbb{Z})_{\text{right}}, E_{f,x}, \operatorname{Aut}_K(A_L) \rangle$ where $E_{f,x}(y) = y + b(y,x)f - \frac{q(x)}{2}b(y,f)f - b(y,f)x$.
- [ ] **Covering representatives**: Compute finite covering list $C(L, \beta)$ from discriminant classes $[v/\operatorname{div}(v)] \in A_L$ and square divisors.
- [ ] **Full orthogonal group generation**: Compute $O(L) = \langle A(L), P_v, t_1, \dots, t_s \rangle$ from approximate subgroup $A(L)$, recursive stabilizer $P_v = \operatorname{Stab}_{O(L)}(v)$, and transporters $t_i$.
- [ ] **Recursive lattice equivalence**: Splitting vector selection, covering list enumeration, and recursive vector transporters.

### 5.2 Primitive Isotropic Vectors & Cusp Orbits

- [ ] Priority API: `L.primitive_isotropic_vectors()` returning the domain/enumeration of primitive isotropic vectors $v \in L$ ($b_L(v,v)=0$, $\operatorname{div}(v)=1$ in $\mathbb{Z}v$).
- [ ] Priority API: `O.orbit_decomposition(X)` for primitive isotropic vectors returning exact cusp orbit representatives, stabilizers $\Gamma_v$, and transporter isometries.
- [ ] Exact cusp invariants: divisibility $\operatorname{div}(v) = \gcd(b_L(v, L))$ and associated discriminant class $[v/\operatorname{div}(v)] \in A_L = L^\vee/L$.

### 5.3 Primitive Isotropic Sublattices & Flags via Exact Gluing Parabolics

- [ ] Priority API: `L.primitive_isotropic_sublattices(rank=k)` returning saturated isotropic submodules $(I, \iota: I \hookrightarrow L)$ satisfying $I^\perp \cap I = I$ (primitivity certified by Smith invariants of $L/I$, never raw basis matrices).
- [ ] Semantic separation: Vector $v$ vs. rank-1 sublattice $\mathbb{Z}v$ vs. rational $k$-plane $W \subset L \otimes \mathbb{Q}$ vs. integral saturated sublattice $L \cap W$.
- [ ] Exact gluing-based parabolic stabilizer replacing the "helping lattice" heuristic: rational Witt decomposition $L_{\mathbb{Q}} \cong I_{\mathbb{Q}} \oplus K_{\mathbb{Q}} \oplus I'_{\mathbb{Q}}$ with exact SES $1 \to U_I(\mathbb{Z}) \to P_I \to M_I \to 1$ where $M_I \leq \operatorname{GL}(I) \times O(K_I)$ preserves the gluing subgroup $H_L = L/(I \oplus K \oplus I')$.
- [ ] Inductive orbit step via double cosets $Q_u \backslash O(K_I) / H_I$ where $Q_u = \operatorname{Stab}_{O(K_I)}(u)$ and $H_I = \pi_I(P_I) \leq O(K_I)$.

### 5.4 Mathematical Verification Milestones

- [ ] Milestone 1 ($h=1$): $L = U \oplus E_8(-1)$ — full Lorentzian $O(L)$, $O^\Omega(L)$, primitive isotropic vector orbit, cusp stabilizer $\twoheadrightarrow O(E_8)$, unipotent radical, and transporters.
- [ ] Milestone 2 ($h=2$): $N = U \oplus U(2) \oplus E_8(-2)$ — full $O(N)$, stable $O^+(N)$, line and plane orbits, stabilizers, Tits-building incidence, and $\Gamma$-orbit splitting for finite-index $\Gamma = \rho_A^{-1}(H)$.
- [ ] Milestone 3 (Equivariant): K3 lattice $\Lambda_{K3} = 3U \oplus 2E_8(-1)$ with Enriques involution $\iota$ — invariant/anti-invariant decomposition $S_{\text{En}} \oplus T_{\text{En}}$, $O(\Lambda_{K3}, \iota)$ via gluing stabilizer, intersection with polarization stabilizer, and anti-invariant isotropic orbits.

## 6. Coxeter diagrams, reflection groups, and Vinberg theory

### 6.1 Coxeter diagrams

- [ ] Preserve root realizations/root-to-diagram morphisms, not only graphs.
- [ ] Associated Coxeter/finitely-presented Coxeter groups.
- [ ] Elliptic and parabolic subdiagram orbit posets.
- [ ] Maximal elliptic and parabolic subdiagram posets.
- [ ] Root-intersection graphs.
- [ ] Restore mathematically valid finite/affine/noncrystallographic literature regressions from `coxeter_tdd_specs`.

### 6.2 Vinberg invariant matrices and weighted graphs

- [ ] Exact reflection-cosine values.
- [ ] Vinberg invariant matrix from Gram/root data.
- [ ] Combinatorial Vinberg invariant matrices.
- [ ] Projective weighted graphs/digraphs and symmetric variants as mathematical objects.
- [ ] Conversion to/from Coxeter matrices where valid.
- [ ] Exact edge/vertex weights and projectivization.
- [ ] Crystallographic, simply-laced, compact-hyperbolic, and paracompact-hyperbolic predicates with exact hypotheses.
- [ ] Schlaeflian/determinant invariants and literature examples.

### 6.3 Hyperbolic reflection algorithms

- [ ] Dominant cone/fundamental chamber.
- [ ] Vinberg's algorithm over integral hyperbolic lattices.
- [ ] Number-field-root-row backend where mathematically valid.
- [ ] Root-length bounds and local-obstruction cases from archived tests.
- [ ] Reflectivity testing when the algorithm actually proves the result.
- [ ] Cocompactness from chamber/diagram data.
- [ ] Weyl/reflection groups as actual subgroups of `O(L)`.
- [ ] Isotropic vectors below a Vinberg height bound.
- [ ] Chamber-complex data.
- [ ] Lorentz/Allcock edge-walk fundamental-domain backend.
- [ ] Bogachev--Kolpakov exact regression examples.

## 17. ADE and toric log-pair geometry

- [ ] `LogPairs` as equipped `(X,Delta)` objects.
- [ ] Toric log pairs `(V,Delta_toric)`.
- [ ] ADE log pairs.
- [ ] Exact ADE type/variant range, including affine families where intended.
- [ ] Integral ADE polygons `Q` and distinguished point `p*`.
- [ ] Side decorations as exact combinatorial classification data.
- [ ] Toric base `Y=V_Q`.
- [ ] Boundary/blue divisor `C` and complementary divisor `C'`.
- [ ] Branch polynomial/section with Newton polygon `Q` and branch divisor `B`.
- [ ] Pyramidal 3-polytope `P` and toric threefold `V_P`.
- [ ] Double cover `X=V(z^2+f(x,y))->Y` through the general cyclic-cover construction.
- [ ] Del Pezzo involution as deck involution.
- [ ] Boundary divisor `D=pi^*C`.
- [ ] ADE base/cover surfaces as equipped geometric objects, not duplicate records.
- [ ] Polarizing-polytope invariants from the general polytope layer.
- [ ] Dynkin/ADE diagrams through the Coxeter/root-system layer.
- [ ] Alexeev--Thompson regression examples.

## 20. Archived framework specifications without complete source implementations

- [ ] Relative-Spec primitive and affine parameter spaces of sections.
- [ ] Jets and imposed-singularity linear systems.
- [ ] Bertini-family machinery.
- [ ] Linearizations of line bundles/group actions.
- [ ] Equivariant evaluation at fixed points.
- [ ] Holomorphic Lefschetz examples.
- [ ] Invariant divisors versus eigensections.
- [ ] Singular orbits and parity-forced odd `A_n` cases.
- [ ] General complete-intersection families.
- [ ] Local-global singularity compatibility cycles.
- [ ] Quotient compatibility cycles.
- [ ] Gluing-independence cycles.
- [ ] External database adapters/examples (LMFDB, curve/field databases, OEIS, GRDB) only if useful to live research API.
- [ ] Kreuzer--Skarke reflexive-polytope probes after lattice-polytopes land.
- [ ] Fanography/classified Fano-family probes after the toric layer lands.
- [ ] Late backend cleanup: wire a leaner adaptation of the required `polyhedral_common` binaries through the `py_polyhedral` bridge, preserving the wrapper boundary and PATH-based executable resolution.

## 19. Visualization and display helpers (non-blocking)

- [ ] 2D polygon SVG generation if still useful.
- [ ] 3D polytope HTML/Three.js generation if still useful.
- [ ] Coxeter/ADE TikZ only after diagram objects exist live.
- [ ] Custom rich representations only as views of live mathematical objects.
- [ ] Reassess implicit display-hook installation separately from mathematical ports.

## 24. Port-completion audit

- [ ] Compare public mathematical nouns/operations in every archived `categories/**/*.sage`/`.py` file against live API.
- [ ] Re-run every mathematically valid archived `test_known_mathematics.sage` assertion through live public constructions.
- [ ] Re-run valid `coxeter_tdd_specs` literature examples through live Coxeter/Vinberg surface.
- [ ] Rebuild valid framework scenarios against live scheme/geometry surface.
- [ ] Confirm every intentionally unported archived construction is recorded above as superseded, rejected, or spec-only.
