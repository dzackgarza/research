import CatDSL.Categories.Modules
import CatDSL.ForMathlib.LinearAlgebra.Dual

/-!
# Lattices, and the unimodular full subcategory

Object types + Mathlib `Category` instances, bundled with `Cat.of`; functors
between object types, never between bundles (see `Categories/Rings.lean`).

`LatticeObj` is the *general* notion: a finite free module with a
**nondegenerate** symmetric bilinear form.  Unimodularity is a property, and
the unimodular lattices form a full subcategory (`ObjectProperty`
machinery), with its inclusion as the preferred realization functor.
-/

namespace CatDSL.Categories

open CategoryTheory CatDSL

/--
An `R`-lattice: a finite free `R`-module with a **nondegenerate** symmetric
bilinear form.

`form` is `b̃ : M →ₗ M^∨`, `x ↦ b(x,-)`:

  * `b̃` injective            = `b` is **nondegenerate** — this structure's field;
  * `b̃` an isomorphism       = `b` is **perfect**, i.e. `M` is **unimodular** —
    the property `IsUnimodular` below, carving out the full subcategory.

The cokernel of `b̃` is the *discriminant group*
`L^∨/L = Module.Dual R.set M ⧸ LinearMap.range form` — expressible from this
definition (that is the point of not requiring an isomorphism), deliberately
not developed here; the general theory is upstream-destined.

**Finite-ring coincidence.**  Over the finite rings this PoC instantiates,
an injective endomap of a finite module is bijective, so nondegenerate and
unimodular coincide *extensionally* on every current instance.  The
distinction here is definitional siting.  The genuine separation — e.g. the
root lattice `A₂` over `ℤ`, with discriminant group `ℤ/3` — needs infinite
base rings outside the `FiniteRingObj` frame; no in-frame witness exists,
and none is faked.
-/
structure LatticeObj (R : FiniteRingObj) where
  module : FreeFinModuleObj R
  form :
    module.module.set →ₗ[R.set] Module.Dual R.set module.module.set
  nondegenerate : Function.Injective form
  symmetric : ∀ x y, form x y = form y x

instance (R : FiniteRingObj) : CoeSort (LatticeObj R) Type where
  coe L := L.module.module.set

/-- Morphisms of lattices are isometries: they preserve the form. -/
structure LatticeHom {R : FiniteRingObj} (L M : LatticeObj R) where
  hom :
    L.module.module.set →ₗ[R.set] M.module.module.set
  isometry :
    ∀ x y, M.form (hom x) (hom y) = L.form x y

namespace LatticeHom

@[ext]
theorem ext {R : FiniteRingObj} {L M : LatticeObj R}
    {f g : LatticeHom L M}
    (h : f.hom = g.hom) :
    f = g := by
  cases f
  cases g
  cases h
  rfl

end LatticeHom

instance (R : FiniteRingObj) : Category (LatticeObj R) where
  Hom L M := LatticeHom L M
  id L := { hom := LinearMap.id, isometry := by intro x y; rfl }
  comp {L M N} f g :=
    { hom := g.hom.comp f.hom
      isometry := by
        intro x y
        simp only [LinearMap.comp_apply]
        rw [g.isometry, f.isometry] }
  id_comp _ := by apply LatticeHom.ext; rfl
  comp_id _ := by apply LatticeHom.ext; rfl
  assoc _ _ _ := by apply LatticeHom.ext; rfl

abbrev Lattices (R : FiniteRingObj) : LargeCat := Cat.of (LatticeObj R)

/--
A lattice is **unimodular** when its form is perfect: `b̃` is an isomorphism,
not merely injective.  Equivalently, the discriminant group `coker b̃` is
trivial.
-/
def LatticeObj.IsUnimodular {R : FiniteRingObj} (L : LatticeObj R) : Prop :=
  Function.Bijective L.form

/--
The full subcategory of unimodular lattices.  An axiomatic subcategory is a
`Prop`-valued property + Mathlib's `ObjectProperty.FullSubcategory`; the
inclusion functor below is its preferred realization.  This is the reference
shape for every axiom-gated subcategory.
-/
abbrev UnimodularLatticeObj (R : FiniteRingObj) :=
  ObjectProperty.FullSubcategory (LatticeObj.IsUnimodular (R := R))

abbrev UnimodularLattices (R : FiniteRingObj) : LargeCat :=
  Cat.of (UnimodularLatticeObj R)

/-- The inclusion of the unimodular full subcategory: forgets the witness. -/
def Unimodular.toLattice (R : FiniteRingObj) :
    UnimodularLatticeObj R ⥤ LatticeObj R :=
  ObjectProperty.ι _

namespace LatticeObj

/--
The standard lattice on `R²`: the form with identity Gram matrix.

This is what `(R², id)` denotes in DSL source -- `id` is the *form*, not an
automorphism.  For the standard basis, `Basis.toDual` is precisely the
identity-Gram form `b(x,y) = Σᵢ xᵢ yᵢ`; nondegeneracy is
`Basis.toDual_injective`.

`noncomputable` because the basis machinery rests on `Classical.choice`.
That costs nothing here, and is quietly a demonstration of the
architecture's own point: `π_R` forgets the form, so `|L|` reduces through
`L.module` and never touches `form` at all.
-/
noncomputable def standard (R : FiniteRingObj) : LatticeObj R where
  module := FreeFinModuleObj.rankTwo R
  form := (Pi.basisFun R.set (Fin 2)).toDual
  nondegenerate := (Pi.basisFun R.set (Fin 2)).toDual_injective
  symmetric := fun x y => Module.Basis.toDual_comm _ x y

/--
The standard lattice is unimodular: for a basis, `b̃ = Basis.toDual` is
injective with full range, hence an isomorphism.  A real proof term — the
membership of the example in the subcategory is proved, not aliased.
-/
theorem standard_isUnimodular (R : FiniteRingObj) :
    (standard R).IsUnimodular :=
  ⟨(Pi.basisFun R.set (Fin 2)).toDual_injective,
   LinearMap.range_eq_top.mp (Pi.basisFun R.set (Fin 2)).toDual_range⟩

/-- The standard lattice as an object of the unimodular full subcategory. -/
noncomputable def standardUnimodular (R : FiniteRingObj) :
    UnimodularLatticeObj R :=
  ⟨standard R, standard_isUnimodular R⟩

end LatticeObj

/-- The `FreeFinMod(R)`-realization of a lattice: `(L,b) ↦ L`. -/
def Lattice.toFreeFinModule (R : FiniteRingObj) :
    LatticeObj R ⥤ FreeFinModuleObj R where
  obj L := L.module
  map f := f.hom

end CatDSL.Categories
