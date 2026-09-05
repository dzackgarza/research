# Preamble execution priorities

This file orders the outstanding preamble work across `TODO.md`, `TODO-ORGANIZATION.md`, `PORT_TODO.md`, the archived preamble TODOs, and the repository architecture policies.
It is an execution order, not a duplicate inventory: the detailed mathematical requirements remain in their owning TODO files.

The governing rule is **delete/consolidate before refactoring survivors**. Do not spend time cleaning representation, imports, file layout, or collection handling inside an implementation that a higher-priority step is expected to remove or merge into another mathematical owner.

Before editing `src/dzack_research/preamble/**`, follow `AGENTS.md`: read all current root `*TODO*.md` files and the generated `docs/preamble-megadoc.md`; regenerate the megadoc first when it is stale relative to the live tree.
Preserve the dirty authoritative tree and unrelated work throughout.

## Priority 0 — Re-ground and identify deletion boundaries

Before a structural edit in a subsystem:

1. Identify the mathematical owner that should survive.

2. Check `TODO-ORGANIZATION.md` for a known duplicate/obsolete implementation.

3. Check `PORT_TODO.md` for a more foundational construction that the subsystem is expected to use later.

4. If two implementations express the same mathematics, consolidate them before improving either one's internals.

5. Do not split files or reorganize packages until ownership and dependencies have stabilized enough that the split reflects mathematics rather than current implementation accidents.

In particular, **pause the broad per-file `tuple/list` cleanup** whenever the file is scheduled for deletion/consolidation below.
The collection spine already landed should be used by surviving abstractions; it should not motivate polishing code that will disappear.

Judge progress by `CONTRIBUTING.md` `DEV-36`.  The goal is source a mathematician can read against a definition; every count is a weak proxy for that.
A measure is usable only as a differential signal beside its upstream Sage comparator, and only when it makes someone open a file and read it.
Sage itself would fail several measures that look like defects here — its category package runs 154 of 229 modules in one dependency cycle — so an uncalibrated number is not evidence.

## Priority 0.5 — Standing repairs, before the phase order resumes

These are open defects in code that has already landed, plus two mathematical
questions that must be answered before more code assumes an answer.
They run ahead of Priorities 1–10 because each one makes the work below it
unsound: a broken session import blocks every specimen, a sampled invariant
proves nothing about the objects it does not name, and a duplicated Hom object
is the defect the Mor conversion exists to remove.

Order within this phase is 0.5.1, then 0.5.2, then 0.5.3, then 0.5.4.
0.5.5 is answered before anything touches the code it governs, and 0.5.6 gates
all of it.

### 0.5.1 Four Hom objects claim to be the ambient Mor

`ConnectionSpace` and `ConnectionHomset` (`categories/modules/connections.py`),
`DerivationSpace` and `GradedDerivationSpace`
(`categories/algebras/derivations.py`), and `AbsoluteGaloisGroup`
(`categories/group/profinite/absolute_galois_group.py`) left `OwnedHomset` by
declaring `HomCategoryConstruction(<ambient category>)` and passing their own
endpoints.

`Modules(R).Mor(E, E ⊗ Ω)` and `OwnedFields().Mor(K̄, K̄)` already exist and are
reached through `HomCategory().Of(...)`.
So each of these is a second object for one category and one pair of endpoints
— the split `tests/categories/test_mor_is_one_category.py` was written to
forbid, and the same defect the formed-module Homsets had.
`ConnectionSpace` and `DerivationSpace` show it in their own bodies: each
stores an `_ambient_hom` built from `Modules(base).Mor(...)` beside the
`CategoricalHomset` it declares itself to be.

None of them is a Hom object in its own right.
Each is a subcategory of its ambient Mor carved by a predicate — Leibniz for
derivations and connections, fixing the structure map for the absolute Galois
group — which is the shape `Monos`, `Epis`, `Isos` and `Auts` already have.
`FixedRestrictedHomCategory` and the `Mono`/`Epi`/`Iso`/`Aut` constructions
express it; construct these through that machinery rather than declaring a new
Hom.
This is the mathematical half of Priority 3 step 10, left undone when the
mechanical half landed.

**Status: complete.**

### 0.5.2 Make the `Mor` invariant exhaustive rather than sampled

`tests/categories/test_mor_is_one_category.py` asserts that `A.Mor(B)` is one
interned category on seven hand-picked specimens: a finite ordinal, `ZZ`, a
free module, `U`, a discriminant form, an affine plane, a polynomial algebra.
"Every owned object" is unverified, and cannot be verified by adding specimens
one at a time.

The instrument that would make it exhaustive is the constructor-obligations
sweep, which does not exist in the live tree:
`test_constructors_meet_their_obligations.sage` is in
`archives/preamble/tests/` only.
`AGENTS.md` states as standing policy that every new constructor adds a row to
its `_constructions()` table, so that policy is currently unmeetable.

Restore the sweep on the live tree first.
Then the `Mor` invariant is checked over construction paths instead of seven
objects, and one table carries both audits.

**Status: complete.**

### 0.5.3 One cardinal sweep for `rank` and `cardinality`

"A rank is a cardinal" and "cardinality is total on `Sets`, valued in
cardinals" are one statement, and it is applied in one place.

`rank` is a cardinal in `categories/modules/framed/framed_free_modules.py`.
Elsewhere it is not:

- `categories/modules/framed/finitely_generated/finitely_presented_modules.py`
  returns `sum(1 for ...)`, a Python `int`;

- `categories/isotropic_orbits.py` returns `lattice().base_ring()(len(...))`,
  an owned ring element counted with `len`;

- `categories/rings/number_fields.py` returns an owned `ZZ` element;

- `categories/lattices.py` returns whatever the module it stores returns.

`categories/modules/pure/modules.py` `rank()` is the rank of a matrix
morphism.  That is a different notion and stays where it is; give it a name
that says so.

`cardinality` has 35 implementations.  `FiniteOrdinalSet.cardinality()`
(`categories/sets/set_categories.py`) returns the stored Python size, and
`_FormalSymbols.cardinality()` (`categories/_lattice.py`) returns Sage's
`Infinity`.  Call sites were normalized with `cardinal(...)` while passing
through; the sources were not.  Repair the sources and delete the call-site
normalization.

Two more members of the same sweep:

- `categories/rings/number_fields.py` `signature()` returns a bare pair
  \((r_1, r_2)\) — the defect `signature_pair` already removed elsewhere.

- `tensors/tensor.py` `tensor_order()` returns `len(...)` as a Python `int`,
  where the number of index slots is a cardinal.  `upper_ranks` and
  `lower_ranks` are still public names returning tuples; they were documented
  as private plumbing and not renamed.

**Status: complete.**

### 0.5.4 One owned crossing for numerals entering Sage constructors

`_engine_scalar` (`categories/rings/number_fields.py`), `_engine_dimension`
(`categories/schemes/schemes.py`) and `_states_a_rank`
(`categories/modules/framed/framed_free_modules.py`) are three near-identical
helpers, each written at the point where the defect was met.

They are one operation: an owned numeral crossing into a private Sage
constructor that cannot read it.  The operation has no owned home, which is
why it has three implementations.  `_states_a_rank`'s
`isinstance(labels, (int, Integer))` is that absence showing through as a type
probe.

Give the crossing one owner and delete the three helpers.

**Status: complete.**

### 0.5.5 Two questions to answer before more code assumes an answer

- **Equality of indexed families.**  `categories/sets/indexed_families.py`
  defines no `__eq__`, so sites compare two shapes, two factor families, or
  two invariant-factor families entrywise by hand.  Equality is decidable for
  finite index sets and undecidable in general, so the answer is the
  three-valued one, and nobody has made it.  Decide it before another site
  hand-rolls its own comparison.

- **Injectivity of a form embedding.**  `FormEmbedding.is_injective()`
  (`categories/modules/framed/formed/form_modules.py`) returns `True`
  unconditionally: a monomorphism by fiat.  The repo owns
  `MonoCategoryConstruction`.  A form embedding should be an element of the
  `Mono` subcategory carved out of `FormModules(R).Mor(...)`, where membership
  states injectivity instead of a method asserting it.  This is the same shape
  as the `is_form_morphism` question, which was answered.

**Status: complete.**

### 0.5.6 The live tree import gate

**Status: complete.**

The recorded `from dzack_research.preamble.all import *` failure while
`catalogue.py` built `NamedLattices.LK3.Aut()(...)` was an import-hoist name
collision: `tensors/tensor.py` imported the module-Hom `_engine_matrix` and then
overwrote that binding with its own tensor backend helper.  The module-Hom
helper is now bound as `_engine_module_matrix`; the session import passes and
the defining-module graph remains acyclic with no deferred project imports.

Every specimen below depends on the session import, so this gate stays first.
The working tree is dirty across roughly 126 files.  Commits `a7de990b`,
`1af9bafb` and the checkpoint commit after them carry another agent's
in-flight work under unrelated commit messages; the work is in history and
nothing is lost.

## Priority 1 — High-confidence deletion and consolidation

Do the large, already-identified reductions first.
These remove code that would otherwise be refactored multiple times.

### 1.1 Make generic categorical constructions actually categorical

**Status: complete.**

Target the switchboards in `categories/abstract_categories/constructions.py` and related construction-functor code.

- `Product`, `Coproduct`, `Biproduct`, `TensorProduct`, `Kernel`, `Cokernel`, `Pushout`, `FiberProduct`, etc. should delegate to the relevant owned category, Hom construction, or universal construction.

- The abstract layer must not contain a growing list of concrete theories such as modules, algebras, sets, and schemes.

- Repair the semantic owner when a construction is missing rather than adding a new concrete branch.

This comes before downstream refactors because many finite-coordinate and scheme-specific workarounds should disappear once the generic construction is usable.

### 1.2 Delete matrix-as-tensor duplication

**Status: complete.**

`categories/modules/pure/modules.py` now owns the mathematical identification

`M_{m x n}(R) = Hom_R(F_R([n]), F_R([m]))`

through the `MatrixSpaces` category.
(This lived in a `categories/matrices.py` that the Priority 3 purity pass folded into the module owner; the standalone file no longer exists.)

Before auditing `tensors/tensor.py` for collection/style issues, remove the legacy second linear-map system from type-(1,1) tensors where the operation is actually a matrix/Hom operation:

- linear solve;

- kernels/left kernels;

- matrix stack/block operations;

- matrix inverse;

- row/column API;

- determinant/trace/rank/transpose where duplicated by matrix Homs.

Tensor code should retain tensor mathematics.
Finite backend matrix arrays may remain private implementation details of matrix/Hom operations.

### 1.3 Collapse represented forms onto universal Hom objects

**Status: complete.**

Do not further elaborate the parallel finite represented Hom hierarchy in `categories/forms/forms.py` before this consolidation.

- Represented bilinear pairings should be literal elements of `Hom_R(M tensor_R N, W)` where the tensor product is represented.

- Represented bilinear forms use the diagonal specialization of the same object.

- Quadratic maps should route through the live `DividedSquare` / `Gamma^2` universal construction where appropriate.

- Keep a general callable/indexed form surface only where the relevant universal object is genuinely not represented yet.

- Delete duplicate Hom spaces, equality, pullback, cache, and coordinate machinery once the universal owners subsume them.

### 1.4 Collapse `PowerAlgebra` onto the graded direct-sum implementation

**Status: complete.**

`PowerAlgebra` and `GradedDirectSumModule` duplicate finite-support graded-sum storage and arithmetic.

- Make the power algebra use the existing graded direct sum as its underlying module/additive object.

- Add only the multiplication/unit/free-algebra structure specific to the power algebra.

- Delete the duplicate element normalization, homogeneous component, degree, addition, negation, scalar multiplication, equality, and display machinery.

Do this before further collection cleanup inside either duplicate implementation.

### 1.5 Make `Adjunction` derive redundant data

**Status: complete.**

Twenty-one adjunctions currently repeat equivalent mathematical data.
Choose the canonical representation and derive the rest.

Preferred direction:

- subclasses provide the functors plus unit and counit;

- the generic `Adjunction` derives `hom_set_isomorphism_forward` and `hom_set_isomorphism_inverse`;

- triangle/naturality laws are checked as mathematical specimens, not maintained by duplicate implementations.

Delete the independent transpose implementations after each adjunction is routed through the generic formulas.

### 1.6 Collapse variance/arity functors onto ordinary `Functor`

**Status: complete.**

- `ContravariantFunctor` should be a thin view of a functor from an opposite category.

- `Bifunctor` should be a thin view of a functor from a product category.

- Keep convenience calling syntax; remove duplicate object caches, endpoint validation, and morphism dispatch.

### 1.7 Deduplicate Homset/category infrastructure and caches

**Status: complete.**

After the preceding owners are stable:

- remove copied `ModuleHomset` method assignments from graded/group Homsets;

- remove duplicate `_element_constructor_` definitions;

- introduce the shared parameterized-category abstraction needed by the several `(base_ring, group)` category families;

- centralize identity-sensitive memoization instead of maintaining many local `id(...)` cache dictionaries;

- do not create another cache abstraction if an existing Sage cache or functor image cache already expresses the required identity semantics.

### 1.8 Collapse the four enumerated symbolic-function parents

**Status: complete.**

`TODO-ORGANIZATION.md` §16.  `FourierCharacters`, `HermitePolynomials`, `LaurentMonomials`, and `SincTranslates` under `categories/sets/enumerated/` are four copies of one `UniqueRepresentation, Parent` implementation: infinite cardinality, `rank`/`unrank`, membership by attempting `rank`, unbounded enumeration, and symbolic indexed element construction.

`function_sets.py` already owns `EnumeratedByNaturals`, `EnumeratedByIntegers`, and the index-conversion helpers; the abstraction stops one layer short of the shared indexed-symbol-set parent.
Introduce that parent and delete the four duplicates.

This has no foundational dependency and may be taken at any point in Priority 1.

## Priority 2 — Expose the true dependency DAG (`ARC-11`)

**Status: complete.**

Only after the large deletion/consolidation pass should dependency cleanup begin in earnest.

`TODO-ORGANIZATION.md` identifies package-aggregator imports and local/deferred imports as the principal organization problem.
Make `ARC-11` true on the surviving code:

1. Replace internal imports through package `__init__.py` aggregators with imports from defining modules.

2. Remove local imports whose only purpose is to break import cycles.

3. Use the resulting failures to identify real mathematical dependency inversions.

4. Move ownership/dependencies, not just import statements, until the defining module graph is a credible DAG.

5. Keep public aggregators as dependency leaves only.

Do **not** reorganize large files into new directories merely to change the graph shape.
First expose and repair the semantic graph; package boundaries come later.

## Priority 3 — Foundational owned-category graph and Hom architecture

Execute `PORT_TODO.md §0` breadth-first on the surviving DAG.

Order within this phase:

1. Remove Sage mathematical categories from foundational owned supercategory edges.

2. Replace Sage parameterized category bases that impose Sage membership on owned parameters.

3. Normalize category `__classcall__` logic through owned constructors after the parameterized-base migration.

4. Complete the owned `Hom_C / End_C / Aut_C` packet architecture.

5. Complete the generic owned ring-morphism Hom object and route quotient, localization, residue, structure, completion, and affine-Spec maps through it.

6. Remove public mathematical `Hom(..., SageSets/SageRings/SageGroups/...)` constructions; keep Sage Hom calls only at private engine boundaries.

7. Restore elementary methods that disappear when Sage supercategory edges are removed at their correct owned category owners.

8. Add graph-purity specimens for the foundational graph.

9. Make Hom categories own morphism equality, then delete the capability probes that currently stand in for the owned graph.

10. Convert the remaining 28 `OwnedHomset` subclasses into Mor categories, and carve the predicate-defined ones as subcategories.

Only after the foundational graph is stable should the same purity audit proceed through graded theories, forms, G-sets, divisors, lattices, Coxeter structures, schemes, and profinite groups.

Step 9 owns `TODO-ORGANIZATION.md` §9 and §12, which are one repair.
That repair has landed in the foundational scope: morphism equality is owned by the
relevant morphism/Hom theory, including presented-algebra maps; the old root
`_morphisms_agree` dispatcher is gone; foundational public mathematical methods no
longer use capability probing as a second type system.  Remaining probes in this
phase are constructor ingress, arbitrary-candidate dunders/membership, or private
engine adapters, as required by `DEV-36` and `DEV-32`.

Step 10 is also closed.  The earlier predicate-defined cases were repaired by
Priority 0.5.1/0.5.2 as restricted Hom/Mono/Aut subcategories over their existing
ambient `Mor` parents.  The live tree has exactly two `OwnedHomset` subclasses:
`CategoricalHomset`, the Sage-runtime carrier used by owned Hom categories, and
`UnderlyingSetHomset`, the private underlying-set adapter.  No mathematical
concrete Hom theory remains outside the owned Mor tree.

Step 9 must follow step 7: a probe cannot be deleted until the operation it gropes for exists at its owned owner.
Do not set a target count for it — `DEV-36` and `DEV-32` govern.

**Status: complete.**  The regenerated megadoc/category graph contains zero
reachable `sage.categories.*` mathematical nodes; the foundational architecture,
abstract-category, Hom, ring/algebra, group/module, and Priority 0.5.5 regression
gate passes 130/130.

## Priority 4 — Finish common collection/finiteness architecture on survivors

The collection spine is already partly implemented.
Complete the remaining **foundational** items from `TODO.md` before theory-specific collection cleanup.
Priority 0.5.3 is the cardinal-valued half of this phase and runs ahead of it: `rank` and `cardinality` answer with cardinals before anything below builds on their answers.

### 4.1 Free framings

- Finish the owned-`NN` positional framing route.

- Keep module/algebra framing index sets as owned ordered/enumerated sets.

- Keep framing images as indexed families.

- Remove duplicate positional tables/caches when `rank/unrank` already provides the operation.

- Bounded convenience methods must state their finite hypothesis explicitly.

**Status: complete.**  Module and algebra generator maps retain lazy
`IndexedFamily` data, including countably infinite framings; dict/sequence and
other bounded conveniences require finiteness explicitly, and positional lookup
uses the owned framing's `rank/unrank` interface rather than duplicate tables.
The focused framing/presentation/algebra gate passes 25/25.

### 4.2 Biproduct/tensor/InternalHom

- Biproduct framings are coproducts of framing sets.

- Tensor framings are Cartesian products of framing sets.

- Finite presentation matrix algorithms dispatch from `ModulesWithChosenFinitePresentation`, not merely from the existence property `FinitelyPresentedModules`.

- Apply the same chosen-data routing to `InternalHom` and the tensor/Hom adjunction.

- General Hom objects remain constructible without exhausting either framing.

**Status: complete.**  Biproduct/tensor framings use owned coproduct/Cartesian
index objects; finite matrix realization is gated by the chosen-presentation
category; `InternalHom` leaves general infinite-framing Hom carriers unmaterialized;
and tensor/Hom unit, counit, and induced Hom maps use callable/indexed-family
data rather than eager generator tables.  The focused biproduct/tensor/Hom gate
passes 13/13.

### 4.3 Abstract factor/index families

- Migrate `DiscreteCategory.objects`, direct-sum decompositions, abstract products/coproducts, and similar factor collections to owned indexed families.

- A finite theorem may refine cardinality; it does not justify replacing the collection by a Python sequence.

**Status: complete.**  Discrete object collections, selected direct-sum
decompositions, and abstract product/coproduct/tensor factor collections retain
their owned index sets and `IndexedFamily` representations.  The focused
abstract-collection gate passes 9/9, including infinite discrete objects and
direct retention of a supplied summand family.

### 4.4 Stop at deletion boundaries

Do not yet perform the final `tuple/list` sweep in:

- tensor code scheduled for matrix-API deletion;

- forms code scheduled for Hom/DividedSquare consolidation;

- power-algebra code scheduled for graded-direct-sum consolidation;

- scheme wrapper code scheduled for Spec/Hom normalization;

- duplicated group-Hom/category code scheduled for consolidation.

Migrate only the surviving abstraction after its owner is settled.

**Status: complete through the stated stop boundary.**

## Priority 5 — Repair semantic APIs before downstream numerical consumers

Follow `ARC-16`, `ARC-17`, `DEV-13`, and `STY-104`–`STY-111`. Mathematical consumers should compose semantic constructions; finite coordinate algorithms belong behind those constructions.

High-priority conversions:

1. `FreeResolution.is_exact()` should state exactness via image/kernel subobjects, not compare backend row modules.

   **Status: complete.**  Exactness now checks injectivity/surjectivity and the
   two inclusions `im(d_1) <= ker(epsilon)` and `ker(epsilon) <= im(d_1)` in
   the represented subobject category.  `FreeResolution` no longer carries a
   relation-matrix side channel for this predicate.  The live replacement gate
   is `tests/modules/test_free_resolutions.py` through the central Sage pytest
   runner, and passes 3/3.

2. Cohomology should be constructed as `ker(d_n) / im(d_{n-1})` through owned kernel/image/quotient operations, not by rebuilding relation matrices in the cohomology layer.

   **Status: complete.**  `Cohomology` now constructs `Cycles` and `Boundaries`
   through the differentials' owned `kernel()` and `image()` methods, factors
   the boundary inclusion through the cycle inclusion, and takes that factor
   map's owned cokernel.  The cohomology layer contains no presentation/matrix
   reconstruction.  The finite-PID presentation calculation needed by this
   semantic path now lives behind `ModuleMorphism.kernel()`: for
   `M=R^n/P -> N=R^m/Q` it computes the free preimage
   `S={x : F(x) in Q}` and returns the owned kernel `S/P` with its inclusion and
   exact lift.  Presented-module `subobject_on()` also accepts finite indexed
   families directly, so `image()` does not materialize them as Python data.
   The live semantic kernel/cohomology gate passes 5/5, including
   `Z/4 -> Z/2`, the polynomial-presentation syzygy backend, and cochain-map
   functoriality.

3. Subobject inverse image/intersection should be pullback/kernel constructions; finite-free matrix stacking belongs in the relevant Hom/subobject backend.

   **Status: complete.**  Inverse image is the right adjoint on fixed-ambient
   subobjects and is constructed as the source projection of
   `ker(f,-i)`; module-subobject intersection is the image of the left
   projection from `ker(i,-j)`.  Neither consumer stacks coordinate matrices.
   The finite free span/lift backend now restricts itself to the finite union
   of observed supports without requiring a ranking map for the ambient
   framing, so the semantic constructions also work inside `FreeModuleOn(ZZ,
   NN)`.  The live subobject-image/intersection gate passes 3/3.

4. `module_invariants` and `module_coinvariants` should be equalizer/coequalizer constructions of the action; finite group-generation is an algorithmic specialization.

   **Status: complete.**  The abstract construction vocabulary now owns
   `Equalizer`, `Coequalizer`, and their nonempty-family variants.  In
   `R-Mod`, the binary constructions are realized as `ker(f-g)` and
   `coker(f-g)`; finite wide equalizers use kernel/intersection and finite wide
   coequalizers use image/sum/cokernel.  `module_invariants()` and
   `module_coinvariants()` now only request the wide equalizer/coequalizer of
   the action with the identity.  Choosing a finite group generating family is
   confined to the `FinitelyPresentedGroupModules` backend.  The live action
   gate passes 5/5, including both adjunctions and a two-generator Klein-four
   action whose invariants are zero and coinvariants are `(Z/2)^2`.

5. `GroupLattice` form preservation should be expressed by an action into the appropriate formed-module automorphism Hom rather than exhaustive basis-pair checking in the constructor.

   **Status: complete.**  A `GroupLattice` now stores its selected action as a
   map `G -> Aut(L)`, where `Aut(L)` is the owned lattice-isometry Hom.  The
   constructor forces the chosen group-generator images through that Hom;
   Gram-tensor pullback and invertibility are therefore checked by the common
   lattice-morphism backend rather than by a local basis-pair sweep.
   `action_of(g)` is literally the resulting element of `Aut(L)`.  The live
   form-action gate passes 2/2, including rejection of a non-isometric action.

6. `Ann_R(M)` should be the kernel/ideal attached to the scalar action, with exhaustive finite enumeration only as a backend case.

   **Status: complete.**  The common module surface now defines
   `annihilator()` as `scalar_action().kernel()`, where the scalar action is the
   owned ring morphism `R -> End_R(M)`.  `RingMorphism.kernel()` delegates to a
   represented kernel-ideal backend attached to that action.  Smith/presentation
   calculations for finitely presented modules and exhaustive scalar/carrier
   enumeration for finite general modules now live only behind that backend;
   framed free modules provide the faithful free/zero-module kernel directly.
   The live annihilator gate passes 3/3 and explicitly checks equality with
   `scalar_action().kernel()` in the represented polynomial, PID, finite-carrier,
   free, and zero-module regimes.

7. Fiber dimension and minimal-generator/Nakayama operations should construct the semantic fiber/residue module first and ask that object for dimension; matrix rank belongs in the represented vector-space implementation.

   **Status: complete.**  `fiber_dimension(p)` is now literally
   `fiber(p).dimension()`, and a local module's minimal generator count is
   `residue_module().dimension()`.  The residue module is explicitly refined as
   a vector space over the residue field.  Minimal-generator selection asks that
   vector space for a basis subfamily of its selected generators and lifts the
   corresponding original generators.  Coordinate rank/echelon calculations
   now occur only in the selected finite-presentation vector-space backend;
   finite free vector spaces answer dimension/basis from their framing.
   Nakayama surjectivity already reduces the morphism and asks the residue
   morphism for surjectivity.  The live fiber/Nakayama gate passes 3/3 with
   direct assertions against `fiber().dimension()` and
   `residue_module().dimension()`.

8. Primitive/saturation/exactness/cohomology/lattice consumers should call the common semantic methods even when repairing those methods is part of the current feature task.

   **Status: complete.**  The downstream consumer audit found and removed the
   remaining local semantic bypasses in the specialized lattice/orbit layer.
   `VectorPrimitiveExtension` now constructs the rank-one subobject and asks
   its common `is_primitive()` predicate instead of recomputing primitivity as
   a coordinate gcd.  Isotropic transport and backend-witness verification now
   take direct images as `(g * i).image()` instead of mapping a chosen
   generating family and rebuilding the subobject locally.  The final census
   finds no consumer-side matrix/row criterion for exactness or cohomology and
   no primitive/saturation coordinate criterion; the primitive-embedding
   engine output is immediately reified as an embedding and validated by the
   common `embedding.is_primitive()` predicate.  Through the central Sage
   pytest runner, the live Priority-5 semantic gate passes 15/15 and the
   specialized primitive/saturation/isotropic-image gate passes 3/3.

This phase deliberately precedes specialized lattice/orbit work so those theories do not acquire another generation of local matrix workarounds.

## Priority 6 — Centralize provenance, realization, and runtime construction

After duplicate functor/adjunction infrastructure has been removed:

### 6.1 Functor provenance

Collapse the three competing mechanisms:

- functor object-image caches;

- `ImageOfFunctor` / `FunctorImageObject`;

- ad hoc `_preamble_*_source_*` fields.

Use one chosen-preimage/provenance mechanism.
Then remove bespoke `source_set()`, `source_algebra()`, `original_group_module()`, etc. where they only recover hidden source attributes.

**Status:** Complete. `Functor` now owns one identity-based provenance store for both object and morphism images; `chosen_preimage()` derives reverse lookup from that same store, including ambiguity detection. The separate `ImageOfFunctor`/`FunctorImageObject` runtime category and `ImageInclusionFunctor` are removed, concrete functors no longer override `chosen_preimage()` by reverse-engineering output structure, and the listed bespoke source accessors/hidden provenance fields are removed. Module-localization kernel transport recovers its source morphism through the localization functor provenance; the explicit fraction model retains only its constructor-owned source module as representation state. Regenerated megadoc/graph contain no runtime functor-image wrapper symbols. Focused Sage gate: 20/20 across functor provenance, inverse/adjunction laws, algebra scalar change, group induction/coinduction, and module localization.

### 6.2 Engine capability/realization boundary

Implement the `PORT_TODO.md` capability-routing direction:

- mathematical objects remain owned;

- CAS engines are private realizations/algorithms;

- multi-stage Singular/GAP/OSCAR/etc.
  computations move behind dedicated private adapters rather than being orchestrated across many Python crossings;

- repair `sage-julia-bridge` before adding more raw Julia subprocess machinery.

**Status: complete.**  Backend selection now has one ordered capability
registry with explicit availability and loud failure when no realization is
present.  The lattice OSCAR backend is a private adapter registered by
operation; the former raw Julia subprocess, temporary matrix files, and
stdout protocol are gone.  It uses the persistent `sage-julia-bridge`, its
structured codec and retained `JuliaHandle`s, and all returned engine data are
crossed back into owned lattices, morphisms, and finite groups before leaving
the adapter.  A production-tree census finds no raw process-management calls
under `src/dzack_research/preamble`; the existing Singular and libGAP crossings
are already concentrated private realizations rather than public mathematical
objects.  The bridge runtime negotiates protocol 1 and passes retained-handle
call/release invalidation; the focused capability/crossing gate passes 3/3.
The separate even-unimodular embedding specimen is currently blocked before
its mocked engine seam by the pre-existing owned-cardinal arithmetic defect,
so it is not counted in that gate.

### 6.3 `refine()` audit

Only after construction/provenance simplification, execute `archives/preamble/src-TODO.md`:

- constructors provide construction data;

- cooperative construction follows immediate supercategory structure;

- `refine()` adds constructor-computed properties/axioms only;

- remove history-dependent refinement used as delayed construction;

- eliminate import-order-dependent ring/module/algebra structure installation.

Auditing `refine()` earlier would waste effort on objects and source/provenance machinery expected to disappear in Priorities 1 and 6.1.

## Priority 7 — Normalize affine algebra/scheme architecture

Do this only after ring Hom, generic categorical constructions, provenance, and runtime construction are stable.

Order:

1. Complete the commutative-algebra semantic spine required by affine geometry: owned ideals, quotient/localization maps, spectra, residue/local rings, kernels/images and exact module operations.

2. Make `Spec` an actual contravariant functor on the owned ring/algebra Hom construction.

3. Make affine scheme morphism pullback intrinsic Hom data rather than side-channel metadata on a Sage wrapper.

4. Derive affine closed subschemes from quotient algebras and generic subobjects.

5. Derive affine products/fiber products through categorical tensor/pushout constructions.

6. Remove scheme-specific caches/endpoint overrides that the normalized Hom/functor layer makes unnecessary.

7. Then complete remaining scheme/polytope collection ownership, facets/fans, and general affine/projective cases.

Only after the affine/local algebra prerequisites land should work proceed to regularity, smoothness, local intersection multiplicity, `Proj`, sheaves, line bundles, cyclic covers, blowups, etc., as already ordered in `PORT_TODO.md`.

## Priority 8 — Specialized group, lattice, orbit, Coxeter, and profinite work

`PORT_TODO.md` explicitly orders work breadth-first: these branches come after the common foundations above.

Within this phase:

1. Deduplicate group-module category/Hom/action infrastructure first.

2. Route orbit/stabilizer computations through the common G-set/action layer, with GAP/libGAP private.

3. Finish group/discriminant/torsion-form collection ownership on the surviving APIs.

4. Finish lattice morphism/subobject/dual/discriminant semantics using common module/form/Hom constructions.

5. Only then clean finite Hodge/lattice/orbit/Coxeter collections and application catalogue data into owned sets/families.

6. Implement arithmetic-group, isotropic-orbit, centralizer, Vinberg/reduction, and higher-Witt-index algorithms only after their subobject, action, Hom, discriminant, and backend foundations are stable.

7. Profinite/Galois stage/embedding/conjugacy collection cleanup belongs here unless a needed fix is foundational for general groups/ring Homs.

The remaining archive-derived lattice gaps in `archives/preamble/TODO.md` are late specialized work, not prerequisites for foundational cleanup.

## Priority 9 — Filesystem/package decomposition

Only after Priorities 1–8 have exposed stable mathematical ownership and a real module DAG:

- split domain monoliths where the split corresponds to independent mathematical owners;

- consider a `categories/lattices/` subtree for the surviving lattice ecosystem;

- split large `ParentMethods` classes only along mathematical/category boundaries;

- update aggregators after the defining-module layout is stable.

Do not use LOC thresholds by themselves as split criteria.

## Priority 10 — Final collection and Python cleanup

This is deliberately last.

1. Run the final mechanical audit of every `tuple(...)` / `list(...)` occurrence under `src/dzack_research/preamble`.

2. Every survivor must be one of:

   - finite syntactic ingress immediately parsed into an owned object; or

   - transient private serialization immediately consumed by a backend requiring a concrete finite array.

3. Replace mathematically finite tuple/list return values—roots, orbit representatives, connected components, finite stages, divisor terms, etc.—by owned finite sets/ordered sets/indexed families on the surviving APIs.

4. Run Ruff/simple Python cleanup and remove dead imports/helpers created by the preceding deletions.

5. Do final package/export cleanup only after all deletions and moves are complete.

Mechanical cleanup earlier in the process is explicitly lower value because it would polish code scheduled for deletion or alter import/layout details that the semantic refactors will rewrite anyway.

## Dependency summary

The intended dependency chain is:

```text
known deletion/consolidation
    -> real defining-module DAG
        -> owned category/Hom graph
            -> common collection/finiteness foundations
                -> semantic kernel/image/quotient/action/etc. APIs
                    -> provenance/backend/refinement cleanup
                        -> affine algebra + scheme normalization
                            -> specialized lattice/group/orbit/geometry work
                                -> package splits
                                    -> mechanical collection/Python cleanup
```

A downstream task may move earlier only when it is needed to make an upstream semantic abstraction correct.
In that case, implement the minimum mathematical foundation at the upstream owner; do not bypass it with a local coordinate or engine workaround.
