---
trackerStatus:
  type: plan
title: 'Phase 2 ModulesWithForms core category and carrier integration'
status: approved
planId: PLN-LAT-020
planType: implementation-phase
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
parentPlan: PLN-LAT-000
tasks:
  - TASK-LAT-PHASE2-MODULES-WITH-FORMS-CATEGORY
  - TASK-LAT-PHASE2-FORM-CODOMAIN
  - TASK-LAT-PHASE2-FORM-HELPER-OBJECTS
  - TASK-LAT-PHASE2-THIN-CARRIERS-PROMOTION
  - TASK-LAT-PHASE2-ELEMENT-WRAPPERS
  - TASK-LAT-PHASE2-FREE-TORSION-CARRIERS
  - TASK-LAT-PHASE2-PYDANTIC-VALIDATION
tags:
  - category-specs
  - plan
  - lattices
  - theme-modules-tensors
---

Migrated source: this plan contains the full content formerly stored at `plans/PHASE_2_CORE_OBJECTS.md`. The old `plans/` copy was removed so this tracked plan is the active planning document.

# Phase 2: ModulesWithForms Integration Layer

## Grounded Implementation Contract

Phase-2 is executable as written against the following concrete object-model:

- `ModulesWithForms(R)` owns pairs `(M, f)` where `M` is finitely presented, `f` is a form object on tensor data
  of `M`, and both parent/element/morphism semantics are category-owned.
- `FormCodomain` carries the codomain parent `S` and requires first-class branch families:
  `R`, `Frac(R)`, `Frac(R)/R`, `Frac(R)/2R`, with `QQ/ZZ`, `QQ/2ZZ` as `R=ZZ` instances.
- Object identity is presented-object-sensitive (`M`+generators+`f`); isometric objects may be distinct.
- Morphisms are form-preserving maps at the chosen base ring; over base change, the morphism is realized by
  semilinear triples in `theory/foundations/bilinear-forms-duals-morphisms.md`.
- Elements are symbolic parent elements; membership is parent check and coordinates require semantic conversion
  (`element_from`), not automatic coercion.
- Thin concrete carriers (`core/*`) are wrappers/state holders; public behavior lives in category mixins and
  pydantic-gated constructors.

Method targets by step:

- Step 2.1 (`ModulesWithForms`): category mixins and subcategory lattice, including
  `Hom`, `Homsets`, `SubcategoryMethods`, `form`, `Hom`, `Hom` spaces, and promotion-aware
  containment checks.
- Step 2.2 (`FormCodomain`): codomain constructors + coercion checks for the four explicit branches.
- Step 2.3 (`Form helper objects`): `BilinearForm` and `QuadraticForm` evaluation surfaces and quadratic polar
  conversion.
- Step 2.4 (`thin carriers`): `from_gram`, `from_module_and_form_data`, promotion, direct sum, scalar-submodule
  operations, membership.
- Step 2.5 (`element wrappers`): `ElementWrapper` thin adapters + symbol-space operations.
- Step 2.6 (`free/torsion carriers`): `span/perp/orthogonal_complement`, free/torsion invariants, torsion
  element semantics.
- Step 2.8 (`pydantic validation`): constructor validation models with branch-specific constraints.

## Admitted Definitions

Phase 2 child work may use the following exact definitions:

- `ModulesWithForms(R)` object: `(M, f)` where `M` is a finitely presented `R`-module
  and `f` is form data on a tensor-degree source or quotient of the tensor algebra of
  `M`, with an actual `R`-module codomain `S`. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- Bilinear branch: degree `2`, scalar action endomorphism `sigma = id_R`, source
  `M tensor_R M` or a descended symmetric quotient such as `Sym_R^2(M)`. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- Quadratic branch: degree `1` with current lattice workflow twist `sigma(r)=r^2`,
  sharing the same module, morphism, homset, tensor, Cartesian, and dual machinery when
  the mathematics allows it. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- Form codomain `S` is a genuine `R`-module parent. The first codomain strata are
  `S = R`, `S = Frac(R)`, `S = Frac(R)/R`, `S = Frac(R)/2R`, and for `R = ZZ`,
  `QQ/ZZ` and `QQ/2ZZ`. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- Elements are real parent elements with symbolic generator coordinates; membership is
  parent membership. Coordinate vectors define elements only through semantic
  conversion such as `L.element_from(v)`. Source:
  `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`.
- `divisibility(v)` for a symmetric bilinear element is already admitted in
  `category_specs/forms/docs/MAPPING.md` as `<b(v,M)> <= S`; Phase 2 must not create a
  coordinate-gcd free-module method with that name.

Build the `ModulesWithForms(R)` integration layer, form codomain
abstraction, and the thin concrete carriers that realize the category
mixins. The architectural correction for this phase is:

- `ModulesWithForms(R)` is the single top-level category,
- bilinear/quadratic, free/torsion, nondegenerate, integral/rational, and
  similar notions are subcategory axioms,
- much of the generic parent, element, morphism, and homset behavior lives
  directly in the category definitions as `ParentMethods`,
  `ElementMethods`, `MorphismMethods`, and `Homsets.ParentMethods`,
- the concrete files under `core/` and `morphisms/` are thin stateful
  carriers, wrappers, and promotion points, not a competing conceptual
  hierarchy.

At the end of this phase, one can construct modules with forms, create
symbolic elements, evaluate forms, perform direct sums, use category meets
such as `ModulesWithForms(ZZ).Bilinear().Free()`, and rely on generic
homset and morphism scaffolding supplied by the category layer.

**Depends on:** Phase 0 (Sage patches), especially `QQ/ZZ` and `QQ/2ZZ`
as working codomains, enriched FGP module operations, and `+` = direct sum.

**Supersedes:** PHASE_1 Steps 1-7.

**Style guide:** `plans/LATTICE_STYLE_GUIDE.md`.
**Category contract:** `plans/CATEGORY_ABC_SPEC.md`.
Every object built here must satisfy: elements are symbolic (not numerical),
containment over equations, categories over classes, operators overloaded,
validation at construction, exact arithmetic only.


## Files

```
src/lattices/
    categories/
        modules_with_forms.py     # top-level category + most generic mixins
        bilinear_forms.py         # thin facade for the bilinear form stratum
        quadratic_forms.py        # thin facade for the quadratic form stratum
        bilinear_modules.py       # Bilinear() convenience facade / alias layer
        quadratic_modules.py      # Quadratic() convenience facade / alias layer
        free_bilinear_modules.py  # Bilinear().Free()
        torsion_bilinear_modules.py  # Bilinear().Torsion()
        lattices.py               # Bilinear().Free().NonDegenerate().Integral()
        rational_lattices.py      # Bilinear().Free().NonDegenerate().Rational()
        discriminant_quadratic_forms.py  # quotient-valued torsion quadratic meet
    core/
        codomains.py              # FormCodomain
        forms.py                  # BilinearForm, QuadraticForm
        abstract.py               # thin concrete parent carriers only
        elements.py               # thin ElementWrapper classes only
        free.py                   # concrete free carriers
        torsion.py                # concrete torsion carriers
    validation/
        presentations.py          # Pydantic validators for all Phase 2 constructors
```


## Implementation Steps


### Step 2.1: `ModulesWithForms(R)` Category

**Files:** `categories/modules_with_forms.py`, thin alias files in
`categories/`

**Existing code:** fragmented category files centered on the legacy
`BilinearModules(R)` nomenclature.

Model the top-level category on `sage.categories.modules.Modules`. This is
the foundation everything else hooks into via Sage's category/parent
machinery.

The major correction is that the category definition now owns much of the
generic behavior. In particular, Phase 2 should implement or stub in
category mixins for:

- `ParentMethods`
- `ElementMethods`
- `MorphismMethods`
- `Homsets.ParentMethods`
- `SubcategoryMethods`

Those mixins define the generic semantics for modules with forms and are
reused by all downstream meets.

```python
class ModulesWithForms(Category_module):
    """Category of finitely generated R-modules equipped with a form."""

    def super_categories(self):
        return [Modules(self.base_ring()).FinitelyPresented()]

    def additional_structure(self):
        return self

    class SubcategoryMethods:
        def Bilinear(self): ...
        def Quadratic(self): ...
        def Free(self): ...
        def Torsion(self): ...
        def NonDegenerate(self): ...
        def Integral(self): ...
        def Rational(self): ...
        def TensorProducts(self): ...
        def CartesianProducts(self): ...
        def DualObjects(self): ...

    class ParentMethods(ABC):
        def form(self) -> Form: ...
        def gens(self) -> tuple[ModuleWithFormElement, ...]: ...
        def zero(self) -> ModuleWithFormElement: ...
        def base_ring(self) -> Ring: ...
        def free_part(self) -> ModuleWithForm: ...
        def torsion_part(self) -> ModuleWithForm: ...
        def Hom(self, other: ModuleWithForm) -> ModuleWithFormHomSpace: ...
        def dual(self) -> ModuleWithForm: ...
        def span(self, elements) -> ModuleWithForm: ...

    class ElementMethods(ABC):
        def parent(self) -> ModuleWithForm: ...
        def __add__(self, other) -> ModuleWithFormElement: ...
        def __neg__(self) -> ModuleWithFormElement: ...
        def __rmul__(self, scalar) -> ModuleWithFormElement: ...
        def to_vector(self) -> Vector: ...

    class MorphismMethods(ABC):
        def domain(self) -> ModuleWithForm: ...
        def codomain(self) -> ModuleWithForm: ...
        def __call__(self, v) -> ModuleWithFormElement: ...
        def to_matrix(self) -> Matrix: ...
        def kernel(self) -> ModuleWithForm: ...
        def image(self) -> ModuleWithForm: ...
        def cokernel(self) -> ModuleWithForm: ...

    class Homsets(HomsetsCategory):
        def extra_super_categories(self):
            return [Modules(self.base_category().base_ring())]
```

**Downstream categories are mostly meets, not fresh architectures.**
Required examples:

- `ModulesWithForms(R).Bilinear()`
- `ModulesWithForms(R).Quadratic()`
- `ModulesWithForms(R).Bilinear().Free()`
- `ModulesWithForms(R).Bilinear().Torsion()`
- `ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()`
- `ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()`

Thin compatibility facades such as `BilinearModules`, `QuadraticModules`,
`FreeBilinearModules`, `TorsionBilinearModules`, `Lattices`,
`RationalLattices`, and `DiscriminantQuadraticForms`, together with
subordinate form-stratum names such as `BilinearForms` and
`QuadraticForms`, may remain as names, but they should be trivial wrappers
or aliases for those meets and should inherit the Sage mixins from the
category machinery rather than redefining them.

**Key decisions:**
- `rank` is not on the generic top-level category.
- `_Hom_` is internal Sage plumbing; the public contract is `Hom`.
- `TensorProducts`, `CartesianProducts`, and `DualObjects` come from the
  same category layer, not from a later ad hoc hierarchy.
- Generic element, morphism, and homset behavior should not be restated in
  concrete carrier files.


### Step 2.2: FormCodomain

**File:** `core/codomains.py`

Lightweight Pydantic-validated descriptor for the codomain of a form. This
determines where form values land and which meet predicates (`Integral`,
`Rational`, quotient-valued torsion cases) hold.

```python
class FormCodomain(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    base_ring: Parent   # R
    codomain: Parent    # C (the Sage object accepting form values)

    @classmethod
    def integral(cls, R) -> FormCodomain:
        """R-valued forms: beta: M x M -> R"""
        return cls(base_ring=R, codomain=R)

    @classmethod
    def rational(cls, R) -> FormCodomain:
        """K-valued forms: beta: M x M -> K = Frac(R)"""
        return cls(base_ring=R, codomain=R.fraction_field())

    @classmethod
    def torsion_bilinear(cls, R) -> FormCodomain:
        """K/R-valued forms for discriminant bilinear forms"""
        K = R.fraction_field()
        return cls(base_ring=R, codomain=K / R)

    @classmethod
    def torsion_quadratic(cls, R) -> FormCodomain:
        """K/2R-valued forms for discriminant quadratic forms"""
        K = R.fraction_field()
        return cls(base_ring=R, codomain=K / (2*R))
```

For R = ZZ: integral -> ZZ, rational -> QQ, torsion_bilinear -> QQ/ZZ,
torsion_quadratic -> QQ/2ZZ.

The `codomain` field is a real Sage parent (Phase 0 makes QQ/ZZ work).
Form evaluation coerces into this parent via `codomain(value)`.


### Step 2.3: Form Helper Objects

**File:** `core/forms.py`

Data objects (NOT Sage Parents) storing domain, codomain, and Gram matrix.
The critical design: form evaluation coerces the raw scalar product into
the codomain, so the same code handles integral, rational, and torsion
forms.

```python
class BilinearForm:
    def __init__(self, domain, codomain: FormCodomain, gram_matrix: Matrix):
        ...

    def evaluate(self, left, right):
        """Compute beta(left, right) in C."""
        raw = left.to_vector() * self._gram * right.to_vector().column()
        return self._codomain.codomain(raw[0])
```

QuadraticForm stores a gram matrix and evaluates `q(v) = v^T G v` with
coercion into the quadratic codomain. Its `polar_form()` returns the
associated BilinearForm.

These are helper objects, not an alternative category layer.


### Step 2.4: Thin Concrete Parent Carriers and Promotion

**File:** `core/abstract.py`

**Existing code:** 298-line `BilinearModule(Parent)` -- migrate and
correct per corrections spec.

Concrete parent classes are now thin carriers for state, backend handles,
and promotion hooks. They should not duplicate generic semantics already
owned by `ModulesWithForms(...).ParentMethods`.

**Constructor surface:**
- `ModuleWithForm.from_gram(R, gram_matrix)` -- primary for free modules
- `ModuleWithForm.from_module_and_form_data(module, gram_matrix, codomain)`
  -- for torsion/mixed
- `ModuleWithForm.from_cokernel(morphism)` -- Phase 3 fills this in

Automatic promotion lands objects in the richest correct meet:

- bilinear vs quadratic,
- free vs torsion,
- nondegenerate vs degenerate,
- integral vs rational vs quotient-valued.

The concrete constructors should therefore decide category membership by
mathematical predicates, then let Sage's category machinery supply the
appropriate mixins.

**What to migrate from existing code:**
- `Parent.__init__` with correct category
- `_element_constructor_` / `__call__`
- `_wrap_element` for rewrapping Sage elements
- Direct sum via `__add__` (block diagonal Gram)
- `__pow__` for n-fold direct sum

**What to remove:**
- `_sage_like()` from public API (keep as `_internal_module`)
- `_ambient`, `_ambient_generators`, `_ambient_submodule`
- `rescale` (banned)
- `getattr`-based `_element_cls` resolution

**Operators required:**
- `__add__` = direct sum
- `__pow__` = n-fold direct sum (`L^3 == L + L + L`)
- `__mul__` / `__rmul__` = scalar submodule: `n * L` returns the submodule `{n*v : v in L}`, with Gram matrix `n^2 * G`. This is a SUBMODULE of `L` of index `n^{rank(L)}`, **not** a twist. It is isometric to `L.twist(n^2)` but is a different object. For `L = ZZ`, `n * ZZ = nZZ` is the ideal `(n)` in ZZ.
- `__truediv__` = quotient (stub; Phase 3 fills in via cokernel)
- `__eq__` = canonical isomorphism (identity-matrix isometry for lattices)
- `__contains__` = parent check (never automatic coercion)
- `__iter__` = lazy enumeration of elements


### Step 2.5: Thin Element Wrappers Backed by Category Mixins

**File:** `core/elements.py`

**Existing code:** 150-line file with `FreeBilinearModuleElement(ElementWrapper)`.

All elements MUST be genuine Sage `ElementWrapper` instances wrapping the
underlying FGP module element. Non-negotiable for `Map.__call__` to work.
Most element behavior should live in `ModulesWithForms(...).ElementMethods`
or its meets; the concrete classes in `core/elements.py` should be thin.

**Hierarchy:**
```
BilinearModuleElement(ElementWrapper)
+-- FreeBilinearModuleElement
|   +-- RationalLatticeElement     (Phase 4)
|   |   +-- LatticeElement         (Phase 4)
|   |   +-- DualLatticeElement     (Phase 4)
+-- TorsionBilinearModuleElement
|   +-- DiscriminantGroupElement   (Phase 4)
+-- QuadraticModuleElement
    +-- FreeQuadraticModuleElement
    +-- TorsionQuadraticModuleElement
        +-- DiscriminantFormElement (Phase 4)
```

Phase 2 implements `BilinearModuleElement`, `FreeBilinearModuleElement`,
`TorsionBilinearModuleElement`, and the Quadratic variants. Phase 4
subclasses are stubbed.

**Bilinear element behavior should primarily come from the category mixins:**
- `__mul__(other)` -- bilinear product when other is an element; delegates
  to parent's BilinearForm
- `q()` / `norm()` -- `self * self`
- `is_isotropic()` -- `self.q() == 0`
- `to_vector()` -- extract coordinate vector (explicit basis-dependent
  extraction)
- `to_coordinates()` -- alias
- `span()` -- `self.parent().span([self])`
- `perp()` -- `self.span().perp()`

**FreeBilinearModuleElement additions:**
- `inclusion()` -- morphism `self.span() -> parent` (stub until Phase 3)

**TorsionBilinearModuleElement additions:**
- `additive_order()` -- delegated to underlying FGP element
- `lift()` -- stub until Phase 4 (needs DualLattice)

**Critical style constraint:** `e + f` is a formal symbol in the parent,
not the vector `[1, 1]`. `[1, 0] not in L` must hold.


### Step 2.6: Concrete Free and Torsion Carriers

**Files:** `core/free.py`, `core/torsion.py`, and the thin downstream
concrete carriers introduced by later phases.

The concrete free and torsion classes carry presentation data and backend
handles. Their category membership should come from meets such as
`ModulesWithForms(R).Bilinear().Free()` and
`ModulesWithForms(R).Bilinear().Torsion()`.

**Key methods:**
- `span(elements)` -- sub-bilinear-module within `self` generated by given
  elements. Computes restricted Gram matrix. Returns `FreeBilinearModule`
  (or degenerate `BilinearModule` if the span is degenerate).
- `perp(submodule)` / `orthogonal_complement(elements)` -- orthogonal
  complement within `self`.
- `is_degenerate()`, `is_nondegenerate()`
- `is_even()`, `is_odd()` (when R = ZZ)
- `determinant()` -- `det(gram_matrix)`
- `signature_pair()` -- `(p, q)` for real forms (exact, via Sylvester)

**Span semantics:** `L.span([e, f])` computes the Gram matrix of the
sub-module generated by `e, f` within `L`. This is the INTERNAL span,
inheriting `L`'s bilinear form. It is NOT the external direct sum `+`.

**Generator assignment:** `L.<e, f> = FreeBilinearModule(...)` works via
Sage's preparser calling `_first_ngens(2)`. Verify this works natively
on the `FGP_Module` wrapper; patch if needed.


At this stage, the required concrete carriers are:

- free bilinear, not assumed nondegenerate,
- torsion bilinear, not assumed nondegenerate,
- enough quadratic/torsion scaffolding to support later discriminant
  refinement without introducing a second architecture.


### Step 2.8: Pydantic Validation

**File:** `validation/presentations.py`

**Existing code:** 209-line file with Pydantic models.

Phase 2 validators:
- `FormCodomainModel` -- validates base_ring is a PID, codomain is a ring
- `BilinearModulePresentationModel` -- validates Gram is symmetric, correct
  size, entries in correct ring
- `FreeModulePresentationModel` -- validates gram over R, rank consistency
- `TorsionModulePresentationModel` -- validates invariants are positive
  integers, gram entries in K/R

Each model uses a single `model_validator(mode="after")` that asserts
nontrivial mathematical properties. No per-field validation.


## Explicitly Out of Scope for Phase 2

- **Concrete homset and morphism wrapper classes** -- Phase 3
- **Cokernel, kernel, image** -- Phase 3
- **Dual lattices, discriminant groups** -- Phase 4
- **Lattice named constructors** (`Lattice.U()`, etc.) -- Phase 4
- **Orthogonal groups** -- Phase 5
- **Tor/Ext functors** -- deferred indefinitely
- **Heavy quotient algorithms** -- Phase 3

Note: generic morphism and homset semantics are NOT out of scope anymore.
They belong in the category mixins delivered here, even if their concrete
wrapper classes and quotient algorithms are finished in Phase 3.


## Functional Checkpoint

Run in a Sage session after completing Phase 2:

```python
import src.sage_patches

from src.lattices.categories.modules_with_forms import ModulesWithForms
from src.lattices.core.free import FreeBilinearModule
from src.lattices.core.torsion import TorsionBilinearModule
from src.lattices.core.codomains import FormCodomain

# Category exists and is genuine
assert ModulesWithForms(ZZ) in Categories
assert ModulesWithForms(ZZ).Bilinear() in Categories

# Free bilinear module construction + category containment
L = FreeBilinearModule(ZZ, matrix(ZZ, [[0,1],[1,0]]))
assert L in ModulesWithForms(ZZ).Bilinear()
assert L in ModulesWithForms(ZZ).Bilinear().Free()
assert L in Modules(ZZ)
assert L.gram_matrix() == matrix(ZZ, [[0,1],[1,0]])

# Elements are symbolic, not numerical
L.<e, f> = FreeBilinearModule(ZZ, matrix(ZZ, [[0,1],[1,0]]))
assert e in L and f in L
assert [1, 0] not in L
assert e * f == 1
assert e * e == 0 and f * f == 0
assert e.is_isotropic()
assert e.to_vector() == vector(ZZ, [1, 0])

# FormCodomain machinery
assert L.bilinear_form().codomain() == FormCodomain.integral(ZZ)

# Direct sum via +
M = L + L
assert M.rank() == 4
assert M in ModulesWithForms(ZZ).Bilinear()
assert M.gram_matrix() == block_diagonal_matrix(
    L.gram_matrix(), L.gram_matrix()
)

# Power via ^
assert (L^3).rank() == 6

# Twist
L2 = L.twist(2)
assert L2.gram_matrix() == 2 * L.gram_matrix()

# Span and perp
S = L.span([e])
assert S in ModulesWithForms(ZZ).Bilinear()
assert S.is_degenerate()
assert S.perp() == S

# Torsion bilinear modules
T = TorsionBilinearModule.from_invariants_and_gram(
    [2, 2], matrix(QQ, [[0, QQ(1,2)], [QQ(1,2), 0]])
)
assert T in ModulesWithForms(ZZ).Bilinear()
assert T in ModulesWithForms(ZZ).Bilinear().Torsion()
assert T.bilinear_form().codomain() == FormCodomain.torsion_bilinear(ZZ)
g1, g2 = T.gens()
assert T.b(g1, g2) == QQ(1,2)
assert g1.additive_order() == 2

# Iteration exists (lazy)
first_few = list(itertools.islice(L, 5))
assert L.zero() in first_few
```


## Risks

| Risk | Mitigation |
|------|-----------|
| Element `__mul__` conflicts with Sage's coercion model | Only override on our ElementWrapper subclass; Sage elements use different dispatch |
| `_first_ngens` may not work on wrapped FGP modules | Test early; patch if needed |
| Category caching may interfere with meet-based containment checks | Use `__contains__` override, not cached category membership |
| Torsion form evaluation depends on Phase 0 QQ/ZZ arithmetic | Verify Phase 0 is complete before starting torsion modules |
