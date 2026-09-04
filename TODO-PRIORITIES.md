# Preamble execution priorities

This file orders the outstanding preamble work across `TODO.md`,
`TODO-ORGANIZATION.md`, `PORT_TODO.md`, the archived preamble TODOs, and the
repository architecture policies. It is an execution order, not a duplicate
inventory: the detailed mathematical requirements remain in their owning TODO
files.

The governing rule is **delete/consolidate before refactoring survivors**.
Do not spend time cleaning representation, imports, file layout, or collection
handling inside an implementation that a higher-priority step is expected to
remove or merge into another mathematical owner.

Before editing `src/dzack_research/preamble/**`, follow `AGENTS.md`: read all
current root `*TODO*.md` files and the generated `docs/preamble-megadoc.md`;
regenerate the megadoc first when it is stale relative to the live tree.
Preserve the dirty authoritative tree and unrelated work throughout.

## Priority 0 — Re-ground and identify deletion boundaries

Before a structural edit in a subsystem:

1. Identify the mathematical owner that should survive.
2. Check `TODO-ORGANIZATION.md` for a known duplicate/obsolete implementation.
3. Check `PORT_TODO.md` for a more foundational construction that the subsystem
   is expected to use later.
4. If two implementations express the same mathematics, consolidate them before
   improving either one's internals.
5. Do not split files or reorganize packages until ownership and dependencies
   have stabilized enough that the split reflects mathematics rather than current
   implementation accidents.

In particular, **pause the broad per-file `tuple/list` cleanup** whenever the
file is scheduled for deletion/consolidation below. The collection spine already
landed should be used by surviving abstractions; it should not motivate polishing
code that will disappear.

## Priority 1 — High-confidence deletion and consolidation

Do the large, already-identified reductions first. These remove code that would
otherwise be refactored multiple times.

### 1.1 Make generic categorical constructions actually categorical

**Status: complete.**

Target the switchboards in `categories/abstract_categories/constructions.py`
and related construction-functor code.

- `Product`, `Coproduct`, `Biproduct`, `TensorProduct`, `Kernel`, `Cokernel`,
  `Pushout`, `FiberProduct`, etc. should delegate to the relevant owned category,
  Hom construction, or universal construction.
- The abstract layer must not contain a growing list of concrete theories such
  as modules, algebras, sets, and schemes.
- Repair the semantic owner when a construction is missing rather than adding a
  new concrete branch.

This comes before downstream refactors because many finite-coordinate and
scheme-specific workarounds should disappear once the generic construction is
usable.

### 1.2 Delete matrix-as-tensor duplication

**Status: complete.**

`categories/matrices.py` now owns the mathematical identification

`M_{m x n}(R) = Hom_R(F_R([n]), F_R([m]))`.

Before auditing `tensors/tensor.py` for collection/style issues, remove the
legacy second linear-map system from type-(1,1) tensors where the operation is
actually a matrix/Hom operation:

- linear solve;
- kernels/left kernels;
- matrix stack/block operations;
- matrix inverse;
- row/column API;
- determinant/trace/rank/transpose where duplicated by matrix Homs.

Tensor code should retain tensor mathematics. Finite backend matrix arrays may
remain private implementation details of matrix/Hom operations.

### 1.3 Collapse represented forms onto universal Hom objects

**Status: complete.**

Do not further elaborate the parallel finite represented Hom hierarchy in
`categories/forms/forms.py` before this consolidation.

- Represented bilinear pairings should be literal elements of
  `Hom_R(M tensor_R N, W)` where the tensor product is represented.
- Represented bilinear forms use the diagonal specialization of the same object.
- Quadratic maps should route through the live `DividedSquare` / `Gamma^2`
  universal construction where appropriate.
- Keep a general callable/indexed form surface only where the relevant universal
  object is genuinely not represented yet.
- Delete duplicate Hom spaces, equality, pullback, cache, and coordinate
  machinery once the universal owners subsume them.

### 1.4 Collapse `PowerAlgebra` onto the graded direct-sum implementation

**Status: complete.**

`PowerAlgebra` and `GradedDirectSumModule` duplicate finite-support graded-sum
storage and arithmetic.

- Make the power algebra use the existing graded direct sum as its underlying
  module/additive object.
- Add only the multiplication/unit/free-algebra structure specific to the power
  algebra.
- Delete the duplicate element normalization, homogeneous component, degree,
  addition, negation, scalar multiplication, equality, and display machinery.

Do this before further collection cleanup inside either duplicate implementation.

### 1.5 Make `Adjunction` derive redundant data

**Status: complete.**

Twenty-one adjunctions currently repeat equivalent mathematical data.
Choose the canonical representation and derive the rest.

Preferred direction:

- subclasses provide the functors plus unit and counit;
- the generic `Adjunction` derives
  `hom_set_isomorphism_forward` and `hom_set_isomorphism_inverse`;
- triangle/naturality laws are checked as mathematical specimens, not maintained
  by duplicate implementations.

Delete the independent transpose implementations after each adjunction is routed
through the generic formulas.

### 1.6 Collapse variance/arity functors onto ordinary `Functor`

**Status: complete.**

- `ContravariantFunctor` should be a thin view of a functor from an opposite
  category.
- `Bifunctor` should be a thin view of a functor from a product category.
- Keep convenience calling syntax; remove duplicate object caches, endpoint
  validation, and morphism dispatch.

### 1.7 Deduplicate Homset/category infrastructure and caches

**Status: complete.**

After the preceding owners are stable:

- remove copied `ModuleHomset` method assignments from graded/group Homsets;
- remove duplicate `_element_constructor_` definitions;
- introduce the shared parameterized-category abstraction needed by the several
  `(base_ring, group)` category families;
- centralize identity-sensitive memoization instead of maintaining many local
  `id(...)` cache dictionaries;
- do not create another cache abstraction if an existing Sage cache or functor
  image cache already expresses the required identity semantics.

## Priority 2 — Expose the true dependency DAG (`ARC-11`)

Only after the large deletion/consolidation pass should dependency cleanup begin
in earnest.

`TODO-ORGANIZATION.md` identifies package-aggregator imports and local/deferred
imports as the principal organization problem. Make `ARC-11` true on the
surviving code:

1. Replace internal imports through package `__init__.py` aggregators with imports
   from defining modules.
2. Remove local imports whose only purpose is to break import cycles.
3. Use the resulting failures to identify real mathematical dependency inversions.
4. Move ownership/dependencies, not just import statements, until the defining
   module graph is a credible DAG.
5. Keep public aggregators as dependency leaves only.

Do **not** reorganize large files into new directories merely to change the graph
shape. First expose and repair the semantic graph; package boundaries come later.

## Priority 3 — Foundational owned-category graph and Hom architecture

Execute `PORT_TODO.md §0` breadth-first on the surviving DAG.

Order within this phase:

1. Remove Sage mathematical categories from foundational owned supercategory
   edges.
2. Replace Sage parameterized category bases that impose Sage membership on
   owned parameters.
3. Normalize category `__classcall__` logic through owned constructors after the
   parameterized-base migration.
4. Complete the owned `Hom_C / End_C / Aut_C` packet architecture.
5. Complete the generic owned ring-morphism Hom object and route quotient,
   localization, residue, structure, completion, and affine-Spec maps through it.
6. Remove public mathematical `Hom(..., SageSets/SageRings/SageGroups/...)`
   constructions; keep Sage Hom calls only at private engine boundaries.
7. Restore elementary methods that disappear when Sage supercategory edges are
   removed at their correct owned category owners.
8. Add graph-purity specimens for the foundational graph.

Only after the foundational graph is stable should the same purity audit proceed
through graded theories, forms, G-sets, divisors, lattices, Coxeter structures,
schemes, and profinite groups.

## Priority 4 — Finish common collection/finiteness architecture on survivors

The collection spine is already partly implemented. Complete the remaining
**foundational** items from `TODO.md` before theory-specific collection cleanup.

### 4.1 Free framings

- Finish the owned-`NN` positional framing route.
- Keep module/algebra framing index sets as owned ordered/enumerated sets.
- Keep framing images as indexed families.
- Remove duplicate positional tables/caches when `rank/unrank` already provides
  the operation.
- Bounded convenience methods must state their finite hypothesis explicitly.

### 4.2 Biproduct/tensor/InternalHom

- Biproduct framings are coproducts of framing sets.
- Tensor framings are Cartesian products of framing sets.
- Finite presentation matrix algorithms dispatch from
  `ModulesWithChosenFinitePresentation`, not merely from the existence property
  `FinitelyPresentedModules`.
- Apply the same chosen-data routing to `InternalHom` and the tensor/Hom
  adjunction.
- General Hom objects remain constructible without exhausting either framing.

### 4.3 Abstract factor/index families

- Migrate `DiscreteCategory.objects`, direct-sum decompositions, abstract
  products/coproducts, and similar factor collections to owned indexed families.
- A finite theorem may refine cardinality; it does not justify replacing the
  collection by a Python sequence.

### 4.4 Stop at deletion boundaries

Do not yet perform the final `tuple/list` sweep in:

- tensor code scheduled for matrix-API deletion;
- forms code scheduled for Hom/DividedSquare consolidation;
- power-algebra code scheduled for graded-direct-sum consolidation;
- scheme wrapper code scheduled for Spec/Hom normalization;
- duplicated group-Hom/category code scheduled for consolidation.

Migrate only the surviving abstraction after its owner is settled.

## Priority 5 — Repair semantic APIs before downstream numerical consumers

Follow `ARC-16`, `ARC-17`, `DEV-13`, and `STY-104`–`STY-111`.
Mathematical consumers should compose semantic constructions; finite coordinate
algorithms belong behind those constructions.

High-priority conversions:

1. `FreeResolution.is_exact()` should state exactness via image/kernel subobjects,
   not compare backend row modules.
2. Cohomology should be constructed as `ker(d_n) / im(d_{n-1})` through owned
   kernel/image/quotient operations, not by rebuilding relation matrices in the
   cohomology layer.
3. Subobject inverse image/intersection should be pullback/kernel constructions;
   finite-free matrix stacking belongs in the relevant Hom/subobject backend.
4. `module_invariants` and `module_coinvariants` should be equalizer/coequalizer
   constructions of the action; finite group-generation is an algorithmic
   specialization.
5. `GroupLattice` form preservation should be expressed by an action into the
   appropriate formed-module automorphism Hom rather than exhaustive basis-pair
   checking in the constructor.
6. `Ann_R(M)` should be the kernel/ideal attached to the scalar action, with
   exhaustive finite enumeration only as a backend case.
7. Fiber dimension and minimal-generator/Nakayama operations should construct the
   semantic fiber/residue module first and ask that object for dimension; matrix
   rank belongs in the represented vector-space implementation.
8. Primitive/saturation/exactness/cohomology/lattice consumers should call the
   common semantic methods even when repairing those methods is part of the
   current feature task.

This phase deliberately precedes specialized lattice/orbit work so those theories
do not acquire another generation of local matrix workarounds.

## Priority 6 — Centralize provenance, realization, and runtime construction

After duplicate functor/adjunction infrastructure has been removed:

### 6.1 Functor provenance

Collapse the three competing mechanisms:

- functor object-image caches;
- `ImageOfFunctor` / `FunctorImageObject`;
- ad hoc `_preamble_*_source_*` fields.

Use one chosen-preimage/provenance mechanism. Then remove bespoke
`source_set()`, `source_algebra()`, `original_group_module()`, etc. where they
only recover hidden source attributes.

### 6.2 Engine capability/realization boundary

Implement the `PORT_TODO.md` capability-routing direction:

- mathematical objects remain owned;
- CAS engines are private realizations/algorithms;
- multi-stage Singular/GAP/OSCAR/etc. computations move behind dedicated private
  adapters rather than being orchestrated across many Python crossings;
- repair `sage-julia-bridge` before adding more raw Julia subprocess machinery.

### 6.3 `refine()` audit

Only after construction/provenance simplification, execute
`archives/preamble/src-TODO.md`:

- constructors provide construction data;
- cooperative construction follows immediate supercategory structure;
- `refine()` adds constructor-computed properties/axioms only;
- remove history-dependent refinement used as delayed construction;
- eliminate import-order-dependent ring/module/algebra structure installation.

Auditing `refine()` earlier would waste effort on objects and source/provenance
machinery expected to disappear in Priorities 1 and 6.1.

## Priority 7 — Normalize affine algebra/scheme architecture

Do this only after ring Hom, generic categorical constructions, provenance, and
runtime construction are stable.

Order:

1. Complete the commutative-algebra semantic spine required by affine geometry:
   owned ideals, quotient/localization maps, spectra, residue/local rings,
   kernels/images and exact module operations.
2. Make `Spec` an actual contravariant functor on the owned ring/algebra Hom
   construction.
3. Make affine scheme morphism pullback intrinsic Hom data rather than side-channel
   metadata on a Sage wrapper.
4. Derive affine closed subschemes from quotient algebras and generic subobjects.
5. Derive affine products/fiber products through categorical tensor/pushout
   constructions.
6. Remove scheme-specific caches/endpoint overrides that the normalized Hom/functor
   layer makes unnecessary.
7. Then complete remaining scheme/polytope collection ownership, facets/fans, and
   general affine/projective cases.

Only after the affine/local algebra prerequisites land should work proceed to
regularity, smoothness, local intersection multiplicity, `Proj`, sheaves,
line bundles, cyclic covers, blowups, etc., as already ordered in `PORT_TODO.md`.

## Priority 8 — Specialized group, lattice, orbit, Coxeter, and profinite work

`PORT_TODO.md` explicitly orders work breadth-first: these branches come after the
common foundations above.

Within this phase:

1. Deduplicate group-module category/Hom/action infrastructure first.
2. Route orbit/stabilizer computations through the common G-set/action layer,
   with GAP/libGAP private.
3. Finish group/discriminant/torsion-form collection ownership on the surviving
   APIs.
4. Finish lattice morphism/subobject/dual/discriminant semantics using common
   module/form/Hom constructions.
5. Only then clean finite Hodge/lattice/orbit/Coxeter collections and application
   catalogue data into owned sets/families.
6. Implement arithmetic-group, isotropic-orbit, centralizer, Vinberg/reduction,
   and higher-Witt-index algorithms only after their subobject, action, Hom,
   discriminant, and backend foundations are stable.
7. Profinite/Galois stage/embedding/conjugacy collection cleanup belongs here
   unless a needed fix is foundational for general groups/ring Homs.

The remaining archive-derived lattice gaps in `archives/preamble/TODO.md` are
late specialized work, not prerequisites for foundational cleanup.

## Priority 9 — Filesystem/package decomposition

Only after Priorities 1–8 have exposed stable mathematical ownership and a real
module DAG:

- split domain monoliths where the split corresponds to independent mathematical
  owners;
- consider a `categories/lattices/` subtree for the surviving lattice ecosystem;
- split large `ParentMethods` classes only along mathematical/category boundaries;
- update aggregators after the defining-module layout is stable.

Do not use LOC thresholds by themselves as split criteria.

## Priority 10 — Final collection and Python cleanup

This is deliberately last.

1. Run the final mechanical audit of every `tuple(...)` / `list(...)` occurrence
   under `src/dzack_research/preamble`.
2. Every survivor must be one of:
   - finite syntactic ingress immediately parsed into an owned object; or
   - transient private serialization immediately consumed by a backend requiring
     a concrete finite array.
3. Replace mathematically finite tuple/list return values—roots, orbit
   representatives, connected components, finite stages, divisor terms, etc.—by
   owned finite sets/ordered sets/indexed families on the surviving APIs.
4. Run Ruff/simple Python cleanup and remove dead imports/helpers created by the
   preceding deletions.
5. Do final package/export cleanup only after all deletions and moves are complete.

Mechanical cleanup earlier in the process is explicitly lower value because it
would polish code scheduled for deletion or alter import/layout details that the
semantic refactors will rewrite anyway.

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

A downstream task may move earlier only when it is needed to make an upstream
semantic abstraction correct. In that case, implement the minimum mathematical
foundation at the upstream owner; do not bypass it with a local coordinate or
engine workaround.
