---
trackerStatus:
  type: plan
title: 'Phase 4 lattice meets duals and discriminant descent'
status: approved
planId: PLN-LAT-040
planType: implementation-phase
priority: high
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
parentPlan: PLN-LAT-000
tasks:
  - TASK-LAT-PHASE4-RATIONAL-LATTICE-MEET
  - TASK-LAT-PHASE4-DUAL-LATTICE-OBJECTS
  - TASK-LAT-PHASE4-DISCRIMINANT-OBJECTS
  - TASK-LAT-PHASE4-LATTICE-CONSTRUCTORS
  - TASK-LAT-PHASE4-DISCRIMINANT-VALIDATION
tags:
  - category-specs
  - plan
  - lattices
  - theme-modules-tensors
---

Migrated source: this plan contains the full content formerly stored at `plans/PHASE_4_DISCRIMINANT_DESCENT.md`. The old `plans/` copy was removed so this tracked plan is the active planning document.

# Phase 4: Lattice Meets, Duals, and Discriminant Descent

## Source-Grounded Contract

Source anchors:
`.agents/skills/lattice-redesign/references/category-abc-spec.md`,
`.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`,
`theory/foundations/bilinear-forms-duals-morphisms.md`,
`category_specs/forms/docs/MAPPING.md`,
`category_specs/lattices/docs/MAPPING.md`, and `theory/references/index.md`.

- `Lattices(R)` is the integral meet
  `ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()`.
  `RationalLattices(R)` is the rational meet
  `ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()`, with codomain
  `K = Frac(R)`.
- The algebraic dual `Hom_R(L, R)` and the sharp/rational dual
  `L^# = {x in L_K : b_K(x, L) <= R}` are distinct notions. Phase 4 implements the
  rational-dual object inside `L_K`, with basis-dependent matrices used only as
  representations of the adjoint morphism `ad_b: L -> L^*`, `v |-> b(v,-)`.
- The discriminant object is the actual cokernel
  `A_L = coker(L -> L^*) = L^*/L`, not an invariant package. Its descended bilinear
  form is quotient-valued: `bar_b([x],[y]) = b(x,y) mod R` in `K/R`; the quadratic
  refinement uses the quotient-valued codomain required by the discriminant-form path
  (`K/2R`, and `QQ/2ZZ` when `R = ZZ`).
- `discriminant_class` is the quotient map from dual-lattice elements to `A_L`;
  ordinary elements of `L` map to the zero class after inclusion. `lift()` returns an
  element of the dual-lattice object, not a raw coordinate vector.
- Divisibility is the pairing-image submodule
  `<b(v, w) : w in M>` of the form codomain. In scalar-valued integral cases this is an
  ideal; coordinate gcds are only representations under extra hypotheses.
- Presented-object equality remains distinct from isometry. Basis change, lift, dual,
  and discriminant construction return new objects and explicit morphisms; they do not
  mutate a hidden ambient presentation.

## Admitted Definitions

Phase 4 child work may use these definitions:

- `Lattices(R)` is
  `ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()`. For `R = ZZ`,
  `Lattice` is the integral lattice endpoint. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- `RationalLattices(R)` is
  `ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()` with codomain
  `K = Frac(R)`. An integral lattice is also a rational lattice by codomain extension.
  Source: `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- The adjoint map is `ad_b: L -> L^*`, `v |-> b(v,-)`. Matrices represent this map only
  after bases are fixed; the invariant content is the morphism. Source:
  `theory/foundations/bilinear-forms-duals-morphisms.md`.
- Dual lattice elements are functionals or dual-lattice elements, not bare vectors.
  Backend interop that needs coordinates must expose that separately from semantic
  lifting. Sources: `theory/foundations/bilinear-forms-duals-morphisms.md` and
  `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`.
- The discriminant group/object is `A_L = coker(L -> L^*) = L^*/L` with quotient-valued
  bilinear form `bar b([x],[y]) = b(x,y) mod R` when the dual/discriminant hypotheses
  hold. Source: `theory/foundations/bilinear-forms-duals-morphisms.md`.
- `discriminant_class` is the quotient map from dual objects to `L^*/L`; ordinary
  elements of `L` map to the zero class after inclusion. Source:
  `category_specs/lattices/docs/MAPPING.md`.

Build the downstream meet-based categories on top of `ModulesWithForms(R)`:

- `Lattices(R) = ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()`
- `RationalLattices(R) = ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()`
- quotient-valued torsion refinements for discriminant objects, including
  the quadratic refinement layer used for discriminant forms.

This phase implements the complete discriminant descent pipeline:
named lattice constructors, dual lattices whose elements are functionals,
the cokernel path `L -> L* -> A_L`, quotient-valued discriminant data,
lift, and `discriminant_class`.

**Depends on:** Phase 3 (concrete morphism wrappers and the cokernel
machine). The discriminant group is literally `iota.cokernel()` where
`iota: L -> L*` is the inclusion morphism. Phase 3 provides the quotient
machinery; Phase 4 provides the named lattice/discriminant meets and the
additional quotient-valued form semantics.

**Supersedes:** PHASE_1 Steps 9, 10, and 11.

**Style guide:** `plans/LATTICE_STYLE_GUIDE.md`.
Core style constraints for this phase: dual elements are functionals (not
vectors), discriminant_class returns group elements (not coordinates), lift
returns dual lattice elements (not raw vectors), equality means canonical
isomorphism, explicit morphisms for all embeddings.


## Files

```
src/lattices/
    categories/
        rational_lattices.py      # meet-based rational lattice category facade
        lattices.py               # meet-based lattice category facade
        discriminant_quadratic_forms.py  # torsion quadratic quotient-valued meet
    core/
        rational.py               # RationalLattice, DualLattice
        discriminant.py           # DiscriminantGroup, DiscriminantForm
    morphisms/
        discriminant.py           # DiscriminantGroupMorphism (if needed)
    lattices.py                   # Lattice class + all named constructors
    validation/
        presentations.py          # (extend) LatticeFromGramModel,
                                  #   DiscriminantGroupFromCokernelModel
```


## Implementation Steps


### Step 4.1: Rational Lattice Meet

**File:** `core/rational.py`

**Existing code:** 126-line `RationalLattice(FreeBilinearModule)`.

A concrete carrier realizing the meet
`ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()`.
The bilinear form takes values in `K = Frac(R)` (for `R = ZZ`, values in
`QQ`). This is the natural home for `L*` and for scalar multiples like
`(1/2)*L`.

```python
class RationalLattice(FreeBilinearModule):
    """Free bilinear module with K-valued form, K = Frac(R)."""

    @classmethod
    def from_free_module_and_gram(cls, module, gram_matrix):
        codomain = FormCodomain.rational(module.base_ring())
        ...
```

**Key property:** `RationalLattice` elements can have non-integral
bilinear products. For example, in `(1/2)*U`, the form evaluates to
`QQ(1/4)` on pairs of generators.

**Scalar multiples.** `(1/n) * L` constructs a `RationalLattice` whose
underlying module is `(1/n) * L.underlying_module()` and whose Gram matrix
is `(1/n^2) * L.gram_matrix()`. Elements are `(1/n) * v` for `v in L`.
This is NOT the same as `L.twist(1/n^2)` -- twist scales the form, scalar
multiplication scales the elements.


### Step 4.2: Dual Lattice Objects

**File:** `core/rational.py`

**Existing code:** Part of the 126-line file.

`DualLattice` is a rational-lattice object with:
- A reference to the source lattice `L`
- An `inclusion_morphism()` returning `iota_L: L -> L*` with matrix `G`
- Gram matrix `G^{-1}` (the inverse Gram in the dual basis)

```python
class DualLattice(RationalLattice):
    """L* = Hom(L, ZZ) with form beta*(f, g) = beta(f_vec, g_vec).

    Elements are functionals: e_star(v) evaluates the functional
    on a lattice element.
    """

    @classmethod
    def from_lattice(cls, L):
        dual_gram = L.gram_matrix().inverse()
        return cls(dual_gram, FormCodomain.rational(L.base_ring()),
                   source_lattice=L)

    def inclusion_morphism(self):
        """iota_L: L -> L*, v -> beta(v, -).

        Matrix representation is G (the Gram matrix of L).
        """
        H = self._source_lattice.Hom(self)
        return H.from_matrix(self._source_lattice.gram_matrix())

    def source_lattice(self):
        return self._source_lattice
```

**DualLatticeElement:** Each element of `L*` is a functional `L -> ZZ`.
This means `e_star(v)` is meaningful for `v in L` -- it evaluates the
linear functional.

```python
class DualLatticeElement(RationalLatticeElement):
    def __call__(self, lattice_element):
        """Evaluate the functional on a lattice element."""
        assert lattice_element in self.parent().source_lattice()
        ...

    def discriminant_class(self):
        """Project to A_L = L*/L."""
        A_L = self.parent().source_lattice().discriminant_group()
        pi = A_L.projection()
        return pi(self)
```

**Dual basis semantics.** For `L = U` with generators `e, f` and Gram
matrix `[[0,1],[1,0]]`:
- `L* = DualLattice.from_lattice(L)` with Gram `[[0,1],[1,0]]^{-1}`
- `e_star, f_star = L*.gens()`
- `e_star(e) == 1`, `e_star(f) == 0` (dual basis evaluation)
- `iota(e) == f_star` because `beta(e, -) = f_star` (since `beta(e,e)=0, beta(e,f)=1`)
- `iota(f) == e_star` because `beta(f, -) = e_star`

For `U(2)` with Gram `[[0,2],[2,0]]`:
- `U2_dual.gens()` are `ep/2, fp/2` (half the original generators)
- `ep_dual.discriminant_class() == g1` (nontrivial in `A_{U(2)}`)


### Step 4.3: Discriminant Objects

**File:** `core/discriminant.py`

**Existing code:** a mixed old hierarchy centered on
`DiscriminantGroup(TorsionBilinearModule, QuadraticModule)`.

The corrected architecture is:

- the underlying quotient object first lands in the torsion bilinear meet,
- any quadratic refinement is additional structure on the same quotient,
- named discriminant categories are meet-based facades rather than a second
  independent architecture.

In particular, the named quadratic facade should be treated as

```text
DiscriminantQuadraticForms(R)
    := ModulesWithForms(R).Quadratic().Torsion().NonDegenerate()
       with quotient-valued codomain, typically K/R or K/2R
```

and not as a separate base class tower.

At minimum, Phase 4 must support the standard discriminant descent cases:

- bilinear values in `K/R` (for `R = ZZ`, `QQ/ZZ`),
- quadratic refinement in the quotient-valued codomain used by the even
  discriminant form path.

**Construction via cokernel (the critical path):**
```python
# This is what L.discriminant_group() calls internally:
iota = L.dual().inclusion_morphism()   # iota: L -> L*
A_L = iota.cokernel()                  # coker(L -> L*) = L*/L
```

Phase 3's cokernel machine handles the FGP quotient and generic form
descent. Phase 4 adds the promotion logic so the result lands in the
appropriate named discriminant meet when the source data identifies the
standard `L -> L* -> A_L` path.

**Direct construction (for testing):**
```python
@classmethod
def from_invariants_and_gram(cls, invariants, gram):
    """Direct construction without source lattice.

    Useful for comparison and testing. gram entries in QQ,
    interpreted modulo ZZ for bilinear and modulo 2ZZ for quadratic.
    """
    ...
```

**Methods:**
- `gens()`, `zero()` -- inherited from `TorsionBilinearModule`
- `b(x, y)` -- bilinear form, values in `QQ/ZZ`
- `q(x)` -- quadratic form, values in `QQ/2ZZ`
- `bilinear_form()`, `quadratic_form()` -- form objects
- `invariants()` -- Smith normal form invariants
- `cardinality()` -- `prod(invariants)`
- `isotropic_elements()` -- `{x in A_L : q(x) == 0}`
- `elements_of_norm(n)` -- `{x in A_L : q(x) == n}`
- `value_map()` -- `{n: elements_of_norm(n) for n in range}`
- `is_p_elementary(p)` -- all invariants are `p`
- `p_rank(p)` -- number of invariants equal to `p`
- `is_isometric_to(other)` -- compare quadratic form isometry classes
- `isomorphic_as_groups(other)` -- compare underlying abelian group structure

**DiscriminantGroupElement:**
- `additive_order()` -- order in the group
- `lift()` -- returns element of `DualLattice`, NOT a raw vector.
  `g.lift() in L.dual()` must hold.
- `discriminant_class()` is identity on discriminant group elements

**Discriminant quadratic forms** are the torsion quadratic, quotient-valued
refinement layer. They should be treated as the meet-based quadratic
subcategory on top of the same quotient object, not as a separate base
architecture.


### Step 4.4: The Lattice Meet and Concrete Carrier

**File:** `lattices.py`

**Existing code:** 344-line `Lattice(RationalLattice)` with named
constructors and backend delegation.

`Lattice` is the primary user-facing concrete carrier for the meet
`ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()`. It may
internally reuse the free/rational concrete carriers, but its public
semantics come from category membership rather than from the old inheritance
story.

**Dual backends.** Every `Lattice` stores both a Sage and a Julia
representation. The Julia backend (via `~/sage-julia-bridge`) handles
algorithms where Sage is weak: indefinite isometry, genus computations,
automorphism groups. Both are internal implementation details; callers
use our public API.

```python
class Lattice(RationalLattice):
    # Internal backends -- never exposed publicly
    _sage_lattice: IntegralLattice       # Sage backend (always present)
    _julia_lattice: object | None = None  # Lazily initialized on first use

    def _julia_repr(self):
        """Lazily construct the Julia lattice from our Gram matrix."""
        if self._julia_lattice is None:
            from sage_julia_bridge import julia
            julia.eval("using Hecke")
            julia.set("G", self.gram_matrix())
            self._julia_lattice = julia.eval("integer_lattice(G)")
        return self._julia_lattice
```

Isometry methods (`is_isometric_to`, `is_locally_isometric_to`,
`is_in_same_genus_as`) delegate to the Julia backend internally and
convert the result back to Sage types. See the Julia Backend section in
`plans/LATTICE_STYLE_GUIDE.md` for the usage pattern and the table of
which methods go to which backend.

**Named constructors:**
```python
class Lattice(RationalLattice):
    @classmethod
    def Z(cls) -> Lattice:
        """The rank-1 lattice ZZ with form (1)."""
        return cls.from_gram(matrix(ZZ, [[1]]))

    @classmethod
    def U(cls) -> Lattice:
        """The hyperbolic plane with form [[0,1],[1,0]]."""
        return cls.from_gram(matrix(ZZ, [[0,1],[1,0]]))

    @classmethod
    def A(cls, n: int) -> Lattice:
        """The A_n root lattice."""
        ...

    @classmethod
    def D(cls, n: int) -> Lattice:
        """The D_n root lattice."""
        ...

    @classmethod
    def E(cls, n: int) -> Lattice:
        """E_6, E_7, or E_8."""
        assert n in {6, 7, 8}
        ...

    @classmethod
    def I(cls, p: int, q: int) -> Lattice:
        """The odd unimodular lattice I_{p,q}."""
        ...

    @classmethod
    def II(cls, p: int, q: int) -> Lattice:
        """The even unimodular lattice II_{p,q}."""
        ...

    @classmethod
    def k3(cls) -> Lattice:
        """The K3 lattice II_{3,19} = U^3 + E_8(-1)^2."""
        return cls.II(3, 19)

    @classmethod
    def coble_picard(cls) -> Lattice:
        """The Coble-Picard lattice Z(2) + Z(-2)^{10}."""
        return cls.Z().twist(2) + cls.Z().twist(-2) ** 10

    @classmethod
    def root_lattice(cls, name: str) -> Lattice:
        """Root lattice by Cartan type string (e.g. 'A4', 'E8')."""
        ...

    @classmethod
    def from_gram(cls, G: Matrix) -> Lattice:
        """Construct from Gram matrix."""
        ...

    @classmethod
    def from_string(cls, s: str) -> Lattice:
        """Parse lattice notation like 'U(2) + A_1 + E_8'."""
        ...
```

**Key methods:**
- `dual()` -- returns `DualLattice.from_lattice(self)`
- `discriminant_group()` -- **must use the cokernel path:**
  `self.dual().inclusion_morphism().cokernel()`. NOT a direct bypass.
- `is_even()`, `is_odd()` -- parity of the lattice
- `determinant()` -- `det(gram_matrix)`
- `signature_pair()` -- `(p, q)` computed exactly (Sylvester, no floats)
- `nikulin_invariants()` -- `(rank, p_rank(2), delta)` for even 2-elementary
- `is_isometric_to(other, witness=False)` -- isometry comparison; optionally
  returns witness morphism
- `is_rationally_isometric_to(other)` -- rational equivalence
- `is_locally_isometric_to(other, p)` -- p-adic equivalence
- `is_in_same_genus_as(other)` -- genus equivalence
- `twist(n)` -- scale the form by `n`
- `span(elements)`, `perp()` -- inherited from `FreeBilinearModule`

**LatticeElement additions** (beyond `FreeBilinearModuleElement`):
- `inner_product(other)` -- alias for bilinear product, ZZ-valued
- `divisibility()` -- gcd of coordinates in the lattice basis
- `is_primitive()` -- `self.divisibility() == 1`
- `discriminant_class()` -- projection to `A_L`; always zero for integral
  lattice elements

**Twist vs multiplication distinction** (from `more_specs.sage`):
- `L.twist(n)` scales the FORM: `G_{twist} = n * G`. Returns a new bilinear
  module with the same generators but scaled form.
- `n * L` = `{n*v | v in L}` is a SUBMODULE of `L` of index `n^{rank(L)}`.
  Its generators are `{n*e_i}`, so its Gram matrix is `n^2 * G_L` (each
  bilinear product scales by `n^2`). It is isometric to `L.twist(n^2)`.
- These are NOT the same: `not (2*U).is_isometric_to(U.twist(2))`.
  `2*U` has Gram `4*G_U`; `U.twist(2)` has Gram `2*G_U`.
- For `L = ZZ` as a ZZ-module: `n * ZZ` is the ideal `(n)` -- simultaneously
  a submodule of `ZZ` and an ideal.

**Direct sum structure.** `L1 + L2` returns a lattice with:
- `summands` attribute: `(L1_copy, L2_copy)`
- `embeddings` attribute: `(iota_1, iota_2)` -- inclusion morphisms
- `iota_1.image().perp() == iota_2.image()` -- summands are orthogonal
- `iota_1.is_primitive()` -- primitive embeddings


### Step 4.5: Isometry Comparison Hierarchy

The spec asserts a careful hierarchy of equivalence relations on lattices,
from weakest to strongest:

```
is_rationally_isometric_to  (same signature and determinant mod squares)
    |
is_locally_isometric_to(p)  (isometric over ZZ_p for each prime p)
    |
is_in_same_genus_as         (locally isometric at all primes + rationally)
    |
is_isometric_to             (isometric over ZZ)
```

**Witness pattern.** `is_isometric_to` can optionally return a witness:
```python
is_isom, witness = L1.is_isometric_to(L2, witness=True)
# When is_isom is True:
assert witness in L1.Hom(L2)
assert witness.is_isometry()
```

Backend delegation: these computations are nontrivial and delegate to
Sage's `IntegralLattice` methods. We are glue, not math.


### Step 4.6: Lattice-Level Validation

**File:** `validation/presentations.py` (extend)

```python
class LatticeFromGramModel(BaseModel):
    """Validates Lattice constructed from Gram matrix."""
    gram_matrix: Matrix

    @model_validator(mode="after")
    def validate_lattice(self):
        G = self.gram_matrix
        assert G.is_symmetric(), "Gram matrix must be symmetric"
        assert G.base_ring() == ZZ, "Lattice Gram must have integer entries"
        assert G.det() != 0, "Lattice must be nondegenerate"
        return self

class DiscriminantGroupFromCokernelModel(BaseModel):
    """Validates DiscriminantGroup from cokernel data."""
    module: ...
    gram_matrix: Matrix
    source_lattice: ...

    @model_validator(mode="after")
    def validate_discriminant(self):
        # Cardinality must equal |det(G_L)|
        assert self.module.cardinality() == abs(
            self.source_lattice.gram_matrix().det()
        )
        # Form values must be well-defined in QQ/ZZ
        ...
        return self
```


## Explicitly Out of Scope for Phase 4

- **Orthogonal groups** -- Phase 5
- **Roots, reflections, Weyl groups** -- Phase 5
- **Eichler transvections** -- Phase 5
- **Coxeter diagrams** -- Phase 5
- **Involution eigenlattices** (`invariant_sublattice`,
  `coinvariant_sublattice`) -- Phase 5
- **Isotropic orbit enumeration** -- Phase 5
- **Coble geometry pipeline** (surface -> Picard -> K3 cover -> pullback) --
  deferred; `coble_picard()` is just a named constructor
- **Overlattices, maximal even overlattice, glue construction** -- deferred


## Functional Checkpoint

Run in a Sage session after completing Phase 4:

```python
import src.sage_patches
from src.lattices.lattices import Lattice
from src.lattices.categories.modules_with_forms import ModulesWithForms
from src.lattices.categories.lattices import Lattices
from src.lattices.core.codomains import FormCodomain

# ------------------------------------------------------------------
# Named constructors
# ------------------------------------------------------------------

Z = Lattice.Z()
U = Lattice.U()
assert Z.rank() == 1 and Z.gram_matrix() == matrix(ZZ, [[1]])
assert U.gram_matrix() == matrix(ZZ, [[0,1],[1,0]])
assert Z.twist(2).gram_matrix() == matrix(ZZ, [[2]])

assert Lattice.II(0, 8).is_isometric_to(Lattice.E(8))
assert Lattice.II(3, 19).is_isometric_to(Lattice.k3())
assert Lattice.I(1, 10).signature_pair() == (1, 10)
assert Lattice.from_string("U(2) + A_1").is_isometric_to(
    Lattice.U().twist(2) + Lattice.A(1)
)

# ------------------------------------------------------------------
# Lattice is a BilinearModule in the right categories
# ------------------------------------------------------------------

assert U in ModulesWithForms(ZZ).Bilinear()
assert U in Lattices(ZZ)
assert U in Modules(ZZ)

# ------------------------------------------------------------------
# Element semantics
# ------------------------------------------------------------------

e, f = tuple(U.gens())
assert e.is_isotropic() and f.is_isotropic()
assert e * f == 1
assert e.divisibility() == 1
assert e.is_primitive()
assert e.discriminant_class().is_zero()

# ------------------------------------------------------------------
# Dual lattice: elements are functionals
# ------------------------------------------------------------------

U_dual = U.dual()
e_star, f_star = tuple(U_dual.gens())
assert e_star(e) == 1 and e_star(f) == 0
assert f_star(e) == 0 and f_star(f) == 1

# ------------------------------------------------------------------
# Inclusion morphism iota_L: L -> L*
# ------------------------------------------------------------------

iota = U_dual.inclusion_morphism()
assert iota in U.Hom(U_dual)
assert iota.to_matrix() == U.gram_matrix()
# iota(v) = beta(v, -): for U, iota(e) = f_star, iota(f) = e_star
assert iota(e) == f_star
assert iota(f) == e_star

# ------------------------------------------------------------------
# Unimodular: U is isometric to U* (but not equal)
# ------------------------------------------------------------------

assert U_dual.is_isometric_to(U)
assert U_dual != U  # Isometry swaps basis, not identity

# ------------------------------------------------------------------
# Discriminant group via cokernel (the critical path)
# ------------------------------------------------------------------

U2 = Lattice.U().twist(2)
ep, fp = tuple(U2.gens())
A_U2 = U2.discriminant_group()
assert A_U2 == U2.dual() / U2  # Canonical equality

g1, g2 = tuple(A_U2.gens())
assert A_U2.cardinality() == 4
assert g1.additive_order() == 2 and g2.additive_order() == 2

# Bilinear form in QQ/ZZ
assert A_U2.b(g1, g1) == 0 and A_U2.b(g2, g2) == 0
assert A_U2.b(g1, g2) == QQ(1, 2)

# Quadratic form in QQ/2ZZ
assert A_U2.q(g1) == 0 and A_U2.q(g2) == 0
assert A_U2.q(g1 + g2) == 1

# Isotropic elements
assert set(A_U2) == {A_U2.zero(), g1, g2, g1 + g2}
assert A_U2.isotropic_elements() == {A_U2.zero(), g1, g2}
assert A_U2.elements_of_norm(1) == {g1 + g2}

# ------------------------------------------------------------------
# Lift returns dual lattice element, not a vector
# ------------------------------------------------------------------

U2_dual = U2.dual()
ep_dual, fp_dual = tuple(U2_dual.gens())
assert ep_dual == ep / 2 and fp_dual == fp / 2
assert g1.lift() in U2.dual()
assert g1.lift() == ep_dual
assert g2.lift() == fp_dual

# Discriminant class of dual lattice elements
assert ep_dual.discriminant_class() == g1
assert fp_dual.discriminant_class() == g2

# Discriminant class of lattice elements is always zero
assert ep.discriminant_class() == A_U2.zero()
assert fp.discriminant_class() == A_U2.zero()

# ------------------------------------------------------------------
# Explicit morphism semantics: subobject generators != ambient elements
# ------------------------------------------------------------------

S = ep.span()
sp = S.gens()[0]
assert sp in S
assert sp not in U2  # Different parent!
iota_S = S.inclusion()
assert iota_S(sp) == ep  # Image under inclusion IS in U2
assert iota_S(sp) in U2

# ------------------------------------------------------------------
# Nikulin invariants
# ------------------------------------------------------------------

assert U2.is_even()
assert U2.discriminant_group().is_p_elementary(2)
assert U2.discriminant_group().p_rank(2) == 2
assert U2.nikulin_invariants() == (2, 2, 0)

# ------------------------------------------------------------------
# Isometry comparison hierarchy
# ------------------------------------------------------------------

U2_split = Lattice.from_gram(diagonal_matrix(ZZ, [2, -2]))
assert U2.is_rationally_isometric_to(U2_split)
assert not U2.is_locally_isometric_to(U2_split, 2)
assert U2.is_locally_isometric_to(U2_split, 3)
assert not U2.is_in_same_genus_as(U2_split)
assert not U2.is_isometric_to(U2_split)

# Discriminant groups: isomorphic as groups but NOT isometric
assert U2.discriminant_group().isomorphic_as_groups(
    U2_split.discriminant_group()
)
assert not U2.discriminant_group().is_isometric_to(
    U2_split.discriminant_group()
)

# ------------------------------------------------------------------
# Witness pattern
# ------------------------------------------------------------------

U2_changed = Lattice.from_gram(matrix(ZZ, [[2,2],[2,4]]))
is_isom, witness = U2.is_isometric_to(U2_changed, witness=True)
assert is_isom
assert witness in U2.Hom(U2_changed)
assert witness.is_isometry()

# ------------------------------------------------------------------
# Twist vs multiplication distinction
# ------------------------------------------------------------------

assert U.twist(2).gram_matrix() == 2 * U.gram_matrix()
assert not (2*U).is_isometric_to(U.twist(2))
# 2*U has form 4*G, while U.twist(2) has form 2*G

# ------------------------------------------------------------------
# Direct sum structure
# ------------------------------------------------------------------

L1 = U + U2
iota_U, iota_U2 = L1.embeddings
assert iota_U.image().perp() == iota_U2.image()
assert iota_U2.image().perp() == iota_U.image()
assert iota_U.is_primitive()
assert iota_U2.is_primitive()

# ------------------------------------------------------------------
# K3 lattice
# ------------------------------------------------------------------

K3 = Lattice.k3()
assert K3.is_even()
assert K3.signature_pair() == (3, 19)
assert K3.discriminant_group().cardinality() == 1  # Unimodular

# ------------------------------------------------------------------
# Coble-Picard lattice
# ------------------------------------------------------------------

coble = Lattice.coble_picard()
assert coble.signature_pair() == (1, 10)
assert coble.discriminant_group().is_p_elementary(2)
assert coble.nikulin_invariants() == (11, 11, 1)

# ------------------------------------------------------------------
# E8 duality
# ------------------------------------------------------------------

E8 = Lattice.E(8)
E8_2 = E8.twist(2)
assert E8.dual() == E8  # E8 is unimodular
assert E8_2.discriminant_group() == E8_2.dual() / E8_2
```


## Risks

| Risk | Mitigation |
|------|-----------|
| `DualLatticeElement.__call__` may conflict with Sage's element `__call__` | Implement as explicit `evaluate(v)` method with `__call__` as thin wrapper; test early |
| `discriminant_group()` via cokernel may differ numerically from direct construction | Both paths must produce the same invariants; test on all standard lattices |
| Gram matrix inversion for dual lattice requires nondegenerate form | Assert nondegeneracy at `DualLattice.from_lattice`; degenerate lattices do not have classical duals |
| `from_string` parser is nontrivial | Use a simple recursive descent or regex; support `U(n)`, `A_n`, `E_n`, `D_n`, `+`, `^{n}` |
| Lattice isometry backends in Sage may not handle all indefinite cases | Delegate to `pari` or `magma` for hard cases; document which methods require definite input |
| `n * L` (scalar multiplication of elements) vs `L.twist(n)` semantic confusion | Clear docstrings; test both paths explicitly; `__mul__` and `__rmul__` dispatch based on argument type |
