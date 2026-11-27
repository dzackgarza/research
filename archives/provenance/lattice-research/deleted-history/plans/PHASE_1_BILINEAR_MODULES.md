# Phase 1: ModulesWithForms Foundation Crosswalk

> **Superseded as a monolithic build sheet.** The old Phase 1 combined
> categories, forms, carriers, morphisms, lattices, discriminant objects,
> and orthogonal groups into one document. That architecture is no longer
> correct. The authoritative implementation plans are now:
>
> - `PHASE_2_CORE_OBJECTS.md`
> - `PHASE_3_MORPHISMS.md`
> - `PHASE_4_DISCRIMINANT_DESCENT.md`
> - `PHASE_5_ORTHOGONAL_GROUPS.md`

Build the `ModulesWithForms(R)` foundation over an arbitrary PID `R`
(primarily `R = ZZ`) with one uniform categorical base for:

- free bilinear modules,
- torsion bilinear modules,
- quadratic refinements,
- lattices,
- rational lattices,
- dual objects,
- discriminant bilinear modules,
- discriminant quadratic forms.

The central correction is that there is no longer a split between
"categories" and "core objects." The category `ModulesWithForms(R)`
defines almost all generic parent, element, morphism, homset, tensor,
Cartesian-product, and dual-object behavior. Concrete files carry state and
backend handles, but not a second architecture.

**Depends on:** Phase 0 (Sage patches), especially working quotient-valued
codomains such as `K/R` and `K/2R`, together with enriched finitely
generated-module primitives.

**Canonical sources:**
- `plans/CATEGORY_ABC_SPEC.md`
- `plans/LATTICE_STYLE_GUIDE.md`
- `plans/lattice_redesign_corrections_spec.md`
- `tests/lattice_spec/interface_semantics.sage`
- `tests/lattice_spec/interface_extensions.sage`
- `tests/lattice_spec/more_specs.sage`
- `tests/sage_spec/lattice_methods.sage`


## Corrected Target Structure

```text
src/lattices/
    __init__.py
    lattices.py                          # Lattice carrier + named constructors
    categories/
        __init__.py
        modules_with_forms.py            # top-level category + generic mixins
        bilinear_forms.py                # thin facade for the bilinear form stratum
        quadratic_forms.py               # thin facade for the quadratic form stratum
        bilinear_modules.py              # ModulesWithForms(R).Bilinear()
        quadratic_modules.py             # ModulesWithForms(R).Quadratic()
        free_bilinear_modules.py         # Bilinear().Free()
        torsion_bilinear_modules.py      # Bilinear().Torsion()
        lattices.py                      # Bilinear().Free().NonDegenerate().Integral()
        rational_lattices.py             # Bilinear().Free().NonDegenerate().Rational()
        discriminant_quadratic_forms.py  # Torsion().Quadratic().NonDegenerate() with quotient-valued codomain
    core/
        __init__.py
        codomains.py                     # FormCodomain and codomain predicates
        forms.py                         # BilinearForm and QuadraticForm helpers
        abstract.py                      # thin concrete parent carriers
        elements.py                      # thin concrete element wrappers
        free.py                          # concrete free carriers
        torsion.py                       # concrete torsion carriers
        rational.py                      # rational-lattice and dual carriers
        discriminant.py                  # discriminant carriers
    morphisms/
        __init__.py
        homspaces.py                     # concrete hom-space wrappers
        bilinear.py                      # concrete morphism wrappers
        discriminant.py                  # discriminant-specific wrappers if needed
    groups/
        __init__.py
        orthogonal.py                    # orthogonal, Weyl, Eichler, Coxeter layer
    validation/
        __init__.py
        presentations.py                 # constructor validation
```

The category-owning design is the non-negotiable point:

- `ModulesWithForms(R)` is the top-level category of pairs `(M, f)`.
- `Bilinear()`, `Quadratic()`, `Free()`, `Torsion()`,
  `NonDegenerate()`, `Integral()`, and `Rational()` are meetable axioms.
- named categories such as `BilinearModules`, `QuadraticModules`,
  `FreeBilinearModules`, `TorsionBilinearModules`, `Lattices`,
  `RationalLattices`, and `DiscriminantQuadraticForms` are thin facades or
  aliases for those meets.
- `BilinearForms` and `QuadraticForms` are subordinate form strata, not
  rival top-level architectures.


## Phase 1 Crosswalk

Phase 1 is now a dependency map showing where the old monolithic work went.


### Category and Subcategory Layer

This is implemented in `PHASE_2_CORE_OBJECTS.md`, especially Step 2.1.

Required outcomes:

- `ModulesWithForms(R)` owns:
  - `SubcategoryMethods`
  - `ParentMethods`
  - `ElementMethods`
  - `MorphismMethods`
  - `Homsets.ParentMethods`
  - `TensorProducts`
  - `CartesianProducts`
  - `DualObjects`
- meet-based subcategories exist for:
  - bilinear structure,
  - quadratic structure,
  - free carriers,
  - torsion carriers,
  - nondegeneracy,
  - integral codomains,
  - rational codomains.
- thin facade names exist for:
  - `BilinearForms`
  - `QuadraticForms`
  - `BilinearModules`
  - `QuadraticModules`
  - `FreeBilinearModules`
  - `TorsionBilinearModules`
  - `Lattices`
  - `RationalLattices`
  - `DiscriminantQuadraticForms`


### Codomain Descriptors and Form Helpers

This is implemented in `PHASE_2_CORE_OBJECTS.md`, Steps 2.2 and 2.3.

Required outcomes:

- codomain descriptors distinguish subring codomains from quotient
  codomains,
- the first supported quotient-valued strata are `K/R` and `K/2R`,
- bilinear and quadratic helper objects are lightweight semantics carriers,
- the generic element API may use `v.q() := v.parent().b(v, v)` everywhere
  until a genuine quadratic specialization is needed.


### Thin Concrete Carriers and Element Wrappers

This is implemented in `PHASE_2_CORE_OBJECTS.md`, Steps 2.4 through 2.6.

Required outcomes:

- concrete parent files are thin stateful carriers, not the semantic base,
- free and torsion bilinear carriers exist without assuming
  nondegeneracy,
- element wrappers are thin and inherit their generic behavior from the
  category,
- promotion lands in the richest correct meet instead of hard-coded old
  class trees.


### Concrete Homsets, Morphisms, and Real Cokernels

This is implemented in `PHASE_3_MORPHISMS.md`.

Required outcomes:

- generic homset and morphism behavior already comes from
  `ModulesWithForms`,
- concrete wrappers store data and expose Sage plumbing,
- kernels, images, and cokernels are real categorical objects,
- cokernels are constructed as actual quotients even when SNF invariants are
  the internal algorithm.


### Named Lattice, Dual, and Discriminant Meets

This is implemented in `PHASE_4_DISCRIMINANT_DESCENT.md`.

Required outcomes:

- `Lattices(R)` is the meet
  `ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()`,
- `RationalLattices(R)` is the meet
  `ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()`,
- `DiscriminantQuadraticForms(R)` is the torsion quadratic nondegenerate
  quotient-valued meet on the same quotient object,
- `L`, `L*`, and `A_L` are produced by one framework and one cokernel
  machine,
- the critical descent case is the cokernel of
  `iota: L -> L*` when `beta_{L*}(v, iota(L)) \subseteq R`, yielding the
  descended quotient-valued form.


### Orthogonal, Root, Weyl, Eichler, and Coxeter Layer

This is implemented in `PHASE_5_ORTHOGONAL_GROUPS.md`.

Required outcomes:

- orthogonal group elements are endomorphisms coming from the homset layer,
- subgroup predicates are centralized,
- root and reflection behavior is built on lattice elements and morphisms,
- no separate matrix-only group architecture is introduced.


## Non-Negotiable Consistency Rules

- Do not reintroduce a split between category semantics and core-object
  semantics.
- Do not treat discriminant objects as a separate object system detached
  from `ModulesWithForms`.
- Do not assume free or torsion implies nondegenerate.
- Do not put generic element, morphism, or homset behavior into concrete
  carriers when the category can own it.
- Do not special-case `L`, `L*`, and `A_L` as unrelated foundations.
- Do not replace real cokernels by invariant packages in the public
  semantics.


## Verification Crosswalk

- Phase 2 checkpoint proves the category, subcategories, codomain
  descriptors, form helpers, and thin free/torsion carriers.
- Phase 3 checkpoint proves the concrete hom-space wrappers, morphism
  wrappers, kernels, images, and cokernels.
- Phase 4 checkpoint proves duals, discriminant descent, rational lattices,
  lattices, and named quotient-valued discriminant structures.
- Phase 5 checkpoint proves orthogonal groups, roots, Weyl machinery,
  Eichler transvections, and Coxeter constructions.

The full plan is consistent only if the following spec surfaces become
simultaneously expressible in the same framework:

- `tests/lattice_spec/interface_semantics.sage`
- `tests/lattice_spec/interface_extensions.sage`
- `tests/lattice_spec/more_specs.sage`
- `tests/sage_spec/lattice_methods.sage`


## Exit Condition

Phase 1 is satisfied when the later phase documents collectively describe a
single `ModulesWithForms` architecture in which:

- the generic semantics live in the category,
- the named downstream categories are meets,
- the concrete files are thin carriers and wrappers,
- the discriminant descent `L -> L* -> A_L` is categorical and uniform,
- the same base can express lattices, dual lattices, and discriminant
  forms without switching foundations.
