# MAPPING.md — Lattices Subtree

Records the mathematical justification for how every Sage surface maps to our hierarchy.
For each Sage type: what Sage provides, the correct mathematical concept, placement
decision, and consequence for refinement and regression tests.

---

## Hierarchy Overview

```
FormedModules(R) = Modules(R, dispatch=False).WithForms()  [owned in forms/]
└── .Bilinear()                                            [owned in forms/]
    └── .Symmetric()                                       [owned in forms/]
        └── .Nondegenerate()                               [owned in forms/]
            └── .Integral()                                [owned in forms/]
                └── .Lattice()                             [named endpoint in lattices/]

forms/subcategories/
├── with_forms.py          _WithForms
├── bilinear.py            _BilinearModules
├── quadratic.py           _QuadraticModules
├── symmetric.py           _SymmetricBilinearModules
├── nondegenerate.py       _NondegenerateBilinearModules
├── indefinite.py          _IndefiniteBilinearModules
├── definite.py            _DefiniteBilinearModules
├── integral.py            _IntegralBilinearModules
├── rational.py            _RationalBilinearModules
└── free_bilinear.py       _FreeBilinearModules     (Free + Bilinear)

lattices/subcategories/
├── over_dedekind.py       _LatticesOverDedekindDomain
├── over_pid.py            _LatticesOverPID
├── over_integers.py       _LatticesOverIntegers    (= Lattices(ZZ))
├── even.py                _EvenLattices
├── unimodular.py          _UnimodularLattices
└── constructions/
    ├── dual_objects.py    _DualObjects      (= Lattices(R).DualObjects())
    ├── dual_lattices.py   compatibility alias for DualObjects()
    ├── overlattices.py
    ├── orthogonal_direct_sums.py
    └── discriminant_groups.py
```

---

## Method Placement Table

The table answers: at what tier is each method first universally well-defined?

| Method | Minimal tier | Justification |
|--------|-------------|---------------|
| `form()` | `WithForms` | definitional; every object in this category carries a form |
| form evaluation | inherited from `Modules().WithForms()` | not lattice-owned; lattices inherit module-with-form evaluation rather than defining a lattice-specific `evaluate` method |
| `form_degree() -> (p,q)` | `WithForms` | (1,1) for bilinear, (1,0) for linear, etc. |
| `b(v, w)` | `Bilinear` | bilinear evaluation; only defined once the form is bilinear |
| `self_product(v)` | `Bilinear` | `b(v,v)`; defined for any bilinear form |
| `is_isotropic(v)` | `Bilinear` | `b(v,v) = 0`; defined for any bilinear form |
| `perp(v)` (element) | `Bilinear` | `{w ∈ M : b(v,w)=0}` is a submodule for any bilinear form |
| `orthogonal_submodule_to(S)` | `Bilinear` | `S^⊥ = {w : b(s,w)=0 ∀s∈S}`; always a submodule |
| `q(v)` | `Quadratic` | quadratic form evaluation |
| `is_symmetric()` | `Symmetric` | witness predicate |
| `is_alternating()` | `Alternating` | witness predicate |
| `is_nondegenerate()` | `Nondegenerate` | witness predicate |
| `is_indefinite()` | `Indefinite` | witness predicate |
| `is_definite()` | `Definite` | witness predicate |
| `gram_matrix()` | `Free + Bilinear` | requires a basis; entries `b(e_i,e_j)` lie in R; see note (1) |
| `inner_product_matrix()` | `Free + Bilinear` | synonym / alternative presentation |
| `rank()` | `Free` | rank of free module; undefined for general modules |
| `determinant()` | `Free + Bilinear` | `det(gram_matrix)`; requires basis |
| `discriminant()` | `Free + Bilinear` | `(-1)^r * det`; requires basis |
| `is_positive_definite()` | `Free + Symmetric` | eigenvalue criterion needs free + symmetric |
| `is_negative_definite()` | `Free + Symmetric` | same |
| `signature_pair()` | `Free + Symmetric + OverIntegralDomain` | eigenvalues over Frac(R)⊗R; see note (2) |
| `signature()` | `Free + Symmetric + OverIntegralDomain` | derived: `p - q` |
| `dual_lattice()` | `Bilinear.Integral + OverIntegralDomain` | `L^*={v∈L_K:β(v,L)⊆R}` requires K=ff(R) and R-valued form; see note (3) |
| `discriminant_group()` | `Bilinear.Integral + OverIntegralDomain` | `L^*/L`; follows from dual_lattice; see note (3) |
| `inclusion_morphism()` | `Bilinear.Integral + OverIntegralDomain` | `ι: L → L^*`; same tier |
| `is_even()` | `Bilinear.Integral` | `b(e_i,e_i) ∈ 2R`; requires integrality but NOT freeness |
| `is_unimodular()` | `Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` | `L=L^*`, i.e. `|det|=1` |
| `orthogonal_complement(S)` (parent) | `Bilinear.Symmetric` | `S^⊥` is a submodule for ANY symmetric bilinear module; see note (4) |
| `is_primitive(M)` | `Free + OverIntegralDomain` | quotient L/M is torsion-free |
| `direct_sum(other)` | `Free + Bilinear` | orthogonal direct sum with block-diagonal gram matrix |
| `tensor_product(other)` | `Free + Bilinear` | Kronecker product of gram matrices |
| `sublattice(basis)` | `Free + Bilinear + OverPID` | sublattice on a basis requires PID structure |
| `overlattice(gens)` | `Free + Symmetric + Nondegenerate + OverIntegralDomain` | L + span(gens) ∩ dual; requires dual |
| `maximal_overlattice(p)` | `OverZZ` | algorithm uses ZZ-specific arithmetic |
| `twist(s)` | `WithForms` | scale form by scalar; defined for any module with form |
| `genus()` | `OverZZ` | local-global genus theory; requires ZZ (or at least Dedekind) |
| `orthogonal_group()` | `Modules(R).WithForms().AutCategory()` | `O(M,b) = Aut(M,b)` in the category of modules with forms; see note (5) |
| `special_orthogonal_group()` | `Lattices(R).AutCategory()` parent-method refinement | determinant-one subgroup of the lattice orthogonal group, defined once the aut surface has a determinant realization |
| `stable_orthogonal_group()` | `Lattices(R).AutCategory()` parent-method refinement | orientation or positive-cone refinement of the lattice orthogonal group, not a method on lattice objects |
| `nikulin_invariants()` | `OverZZ + Free + Symmetric + Nondegenerate` | discriminant group invariants (l, δ) |
| `is_isometric_to(other)` | `OverZZ + Free + Symmetric + Nondegenerate` | lattice isometry test |
| `minimum()` | `OverZZ + Free + Symmetric` | shortest vector (requires ZZ for finiteness) |
| `maximum()` | `OverZZ + Free + Symmetric` | longest nonzero vector in compact regions |
| `LLL()` | `OverZZ + Free + Symmetric` | LLL reduction; ZZ-specific |
| `short_vectors(n)` | `OverZZ + Free + Symmetric` | ZZ-specific enumeration |
| `short_vectors(n, up_to_sign_flag=True)` | `short_vectors_up_to_sign(n)` at the same tier | Sage forwards `**kwargs` to `QuadraticForm.short_vector_list_up_to_length`; the installed source exposes the single meaningful keyword `up_to_sign_flag`. The project splits that finite case into a named method instead of exposing a keyword bag. |
| `quadratic_form()` | `Free + Symmetric` | convert to `QuadraticForm` object |
| `rational_span()` | `Free + OverIntegralDomain` | `L ⊗_R Frac(R)` |
| `base_change_to(ring)` | `Free + Bilinear` | change coefficient ring |
| `gram_matrix_bilinear()` | `Torsion + Bilinear` | Gram matrix in Q/mZ; see note (6) |
| `gram_matrix_quadratic()` | `Torsion + Quadratic` | quadratic Gram matrix |
| `brown_invariant()` | `Torsion + Bilinear + Symmetric` | global torsion QF invariant |
| `normal_form()` | `Torsion + Bilinear + Symmetric` | canonical form |
| `primary_part(m)` | `Torsion` | m-primary part |
| `value_module()` | `Torsion + Bilinear` | Q/mZ containing form values |
| `value_module_qf()` | `Torsion + Quadratic` | Q/nZ containing QF values |
| `additive_order(v)` | `Torsion` (element) | order in torsion group |
| `lift(v)` | `Torsion` (element) | lift to dual lattice |
| `divisibility(v)` | `Free` (element) | gcd{a ∈ R : v = a·w for w ∈ L} |
| `is_primitive(v)` | `Free` (element) | divisibility is a unit |
| `discriminant_class(x)` | `Lattices(R).DualObjects()` (element) | quotient map `L^* -> L^*/L`; ordinary `v in L` maps to the zero class via `L -> L^*`; see note (8) |
| `reflection(v)` | `Free + Symmetric + Nondegenerate` (element) | s_v(w) = w - 2b(v,w)/b(v,v) · v |
| `is_root(v)` | `Free + Symmetric + Integral` (element) | b(v,v) ∈ {-2, 2} |
| `norm(v)` | `Bilinear` (element) — see note (7) | b(v,v); defined for any bilinear form |

---

## Notes

**(1) `gram_matrix()` placement**: Sage places this at `FreeQuadraticModule_generic`
(free over commutative ring). We confirm: entries `b(e_i, e_j)` live in R only when the
form is R-valued and M is free (so the `e_i` are a basis). For a torsion module over a
PID, the analogous concept is `gram_matrix_bilinear()` in Q/mZ. These are distinct
methods at distinct tiers; do NOT merge them.

**(2) `signature_pair()` placement**: Sage places this at
`FreeQuadraticModule_integer_symmetric` (= ZZ). Mathematically it is meaningful for any
free symmetric bilinear module over an ordered integral domain via base-change to the
fraction field and then to ℝ. We place it at `Free + Symmetric + OverIntegralDomain`;
the `OverIntegers` tier provides the concrete algorithm. The abstract stub lives at the
Dedekind domain level.

**(3) `dual_lattice()` placement**: `L^* = {v ∈ L_K : β(v,L) ⊆ R}` where
`L_K = L ⊗_R K` and `K = ff(R)`. The definition makes almost no assumptions on `R`:
we only need a fraction field (OverIntegralDomain) and an R-valued form (Integral).
Nondegeneracy is NOT required by the definition — `L^*` is always a well-defined
sub-K-module of `L_K` containing `L`. Freeness is NOT required — the definition is
purely set-theoretic inside `L_K`. We therefore place the abstract stub at
`Bilinear.Integral + OverIntegralDomain`; Sage's ZZ-specific implementation is just
one concrete algorithm.

**(4) `orthogonal_complement(S)` placement**: `S^⊥ = {v ∈ M : b(v,s) = 0 ∀s ∈ S}`.
This is always a submodule. No assumptions needed beyond having a bilinear form.
For symmetric forms, left and right orthogonal complements coincide, so the symmetric
axiom is needed only to guarantee `(S^⊥)^⊥ = S`. Abstract stub belongs at
`Bilinear.Symmetric`. Computability (as a free module of explicit rank) requires
nondegeneracy + free; that is an algorithm concern, not a placement concern.

**(5) `orthogonal_group()` placement**: `O(M,b) = Aut(M,b)` in the category of
modules with forms. Equivalently, its elements are module automorphisms `f` such that
`b(fv, fw) = b(v, w)`, or the corresponding form-preservation diagram commutes. This
definition does not require freeness, nondegeneracy, or integrality, so it covers
degenerate formed modules such as `e^perp` in `U`, rational formed modules, integral
lattices, and finite discriminant forms. Freeness and nondegeneracy are only needed for
particular realizations such as matrix groups inside `GL_n(R)`. The `OverZZ` definite
lattice computation uses Plesken-Souvignier; that is an algorithm detail, not the
mathematical owner.

**(6) Torsion `gram_matrix_bilinear()`**: For `TorsionQuadraticModule = V/W`, the form
takes values in `Q/mZ = (V^*/W^*) / (V/W)^*`. This is a *different type* from the
integral Gram matrix. Both are "gram matrices" but they live at different tiers with
different codomains. The torsion version is named `gram_matrix_bilinear()` (following
Sage) to avoid ambiguity with `gram_matrix()` at the free level.

**(7) `norm(v)` vs `self_product(v)`**: Both are `b(v,v)`. The name `norm` is Sage
lattice convention (appears in `Lattices.ElementMethods`). The name `self_product`
appears in our `BilinearModules.ElementMethods`. Both belong at `Bilinear` (element).
In the spec we use `self_product` at the generic bilinear level and provide `norm` as an
alias at the `Lattices(ZZ)` level (where "norm" is standard terminology).

**(8) `discriminant_class(x)` ownership**: The nontrivial map is the quotient
`L^* -> L^*/L`, so the method belongs to elements of
`Lattices(R).DualObjects()`. The former ordinary lattice-element reading is recovered
by first applying the inclusion `L -> L^*`; its discriminant class is necessarily the
zero element of `L.discriminant_group()`, so it is not a separate element obligation on
`L`.

---

## Construction-Category Vocabulary

The canonical dual construction name is `Lattices(R).DualObjects()`, matching the
standard Sage/project construction category `DualObjectsCategory`. The old
`Lattices(R).DualLattices()` spelling is a compatibility alias only; new specs and
mappings should use `DualObjects()`.

Other lattice construction names audited in this pass are not duplicate spellings of
standard construction categories:

| Lattice surface | Relationship to standard construction vocabulary | Decision |
| --- | --- | --- |
| `DualObjects()` | Standard dual-object construction; objects are dual lattices `L^*`. | Canonical surface. |
| `DualLattices()` | Old lattice-specific spelling of the same `DualObjectsCategory`. | Compatibility alias. |
| `Overlattices()` | Objects under a fixed lattice with finite-index, same-rational-span, inherited-form conditions. | Keep as lattice-specific refinement, not a replacement for `ObjectsUnder(base)`. |
| `OrthogonalDirectSums()` | Cartesian-product construction plus the orthogonal block-sum form and summand access. | Keep as refinement below `CartesianProducts()`. |
| `DiscriminantGroups()` | Finite torsion formed modules `L^*/L` with discriminant-form data. | Keep as lattice-specific quotient/form construction, not generic `Quotients()`. |

`Lattices(R).ObjectsOver(L)` and `Lattices(R).ObjectsUnder(L)` keep the
lattice-specific `structure_lattice()` and lattice morphism `structure_map()`.
Their former local `structure_domain()` and `structure_codomain()` implementations now
map to the Cat-owned universal structure-morphism methods through
`structure_morphism().domain()` and `structure_morphism().codomain()`.

---

## Sage Type → Spec Category Mapping

| Sage Type | Spec Category | Justification |
|-----------|--------------|---------------|
| `FreeQuadraticModule_generic` | `FormedModules(R).Bilinear()` plus free finite-rank module refinements | free quadratic module over commutative ring |
| `FreeQuadraticModule_generic_pid` | `FormedModules(R).Bilinear()` plus free finite-rank `OverPID()` refinements | adds span/span_of_basis with PID structure |
| `FreeQuadraticModule_generic_field` | `FormedModules(K).Bilinear()` plus free finite-rank `OverField()` refinements | over a field (= vector space with form) |
| `FreeQuadraticModule_submodule_*_pid` | forms-owned bilinear subobjects over PID | submodule of free quadratic over PID |
| `FGP_Module_class` | `Modules(R).FinitelyPresented().OverPID()` | V/W presentation; no form |
| `TorsionQuadraticModule` | `forms.subcategories.torsion_quadratic_modules._TorsionQuadraticModules` | V/W with Q/mZ-valued bilinear form |
| `FreeQuadraticModule_integer_symmetric` | forms-owned finite-rank free symmetric nondegenerate integral bilinear chain, then `Lattices(ZZ)` | the canonical integral lattice |
| `QuadraticForm` | forms-owned finite-rank free symmetric nondegenerate integral bilinear chain, then `Lattices(ZZ)` | same category; different presentation (upper-triangular coefficients) |

**Note on `QuadraticForm` vs `FreeQuadraticModule_integer_symmetric`**: Both represent
the same mathematical object (an integral lattice). Sage keeps them as separate classes
for historical reasons. Our spec treats them as objects in the same category; the
constructor `Lattices(ZZ).Constructors().from_quadratic_form(qf)` converts between them.

---

## What Lives in `forms/` vs What Lives in `lattices/`

### Lives in `forms/`

The forms subtree owns the formed-module hierarchy:

- `_WithForms`
- `_BilinearModules`
- `_QuadraticModules`
- `_SymmetricBilinearModules`
- `_AlternatingBilinearModules`
- `_NondegenerateBilinearModules`
- `_DefiniteBilinearModules`
- `_IndefiniteBilinearModules`
- `_IntegralBilinearModules`
- `_RationalBilinearModules`
- `_FreeBilinearModules`
- `_TorsionQuadraticModules`

### Lives in `lattices/subcategories/`

Only lattice-specific axiom classes live here:

- `over_dedekind.py` — `_LatticesOverDedekindDomain`
- `over_pid.py` — `_LatticesOverPID`
- `over_integers.py` — `_LatticesOverIntegers` (canonical `Lattices(ZZ)`)
- `even.py` — `_EvenLattices`
- `unimodular.py` — `_UnimodularLattices`

The former lattice files for generic formed-module axioms are compatibility shims that
import the forms-owned classes.

### Discriminant groups live in `lattices/subcategories/constructions/discriminant_groups.py`

`DiscriminantGroups(ZZ)` = finite torsion formed modules with discriminant form data.
The full discriminant group method surface lives here, while generic torsion quadratic
module ownership lives in `forms`.

---

## Compatibility Paths

`modules/subcategories/with_forms.py`, `modules/subcategories/bilinear.py`,
`modules/subcategories/quadratic.py`, `modules/subcategories/torsion_quadratic_modules.py`,
and the old generic formed-module files in `lattices/subcategories/` re-export the
forms-owned classes. They exist only to preserve old import paths.

Former ordinary lattice-element calls to `v.discriminant_class()` are represented as
`L.inclusion_morphism()(v).discriminant_class()` or, equivalently, the zero element of
`L.discriminant_group()`.

Former lattice-object calls to `L.special_orthogonal_group()` and
`L.stable_orthogonal_group()` are represented by first taking the lattice aut object:
`L.orthogonal_group().special_orthogonal_group()` and
`L.orthogonal_group().stable_orthogonal_group()`. The subgroup constructors live on
`Lattices(R).AutCategory().ParentMethods`; `special_subgroup()` and
`stable_subgroup()` are the primitive subgroup selectors there.
