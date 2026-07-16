import CatDSL.Categories.Modules
import CatDSL.ForMathlib.LinearAlgebra.Dual

/-!
# Lattices

Object types + Mathlib `Category` instances, bundled with `Cat.of`; functors
between object types, never between bundles (see `Categories/Rings.lean`).
-/

namespace CatDSL.Categories

open CategoryTheory CatDSL

/--
A **unimodular** `R`-lattice: a finite free `R`-module with a *perfect*
symmetric bilinear form.

`form` is `b̃ : M → M^∨`, `x ↦ b(x,-)`.  Note what requiring it to be a
`LinearEquiv` actually says:

  * `b̃` injective            = `b` is **nondegenerate**
  * `b̃` an isomorphism       = `b` is **perfect**, i.e. `M` is **unimodular**

These coincide for finite-dimensional `M` over a field -- which is why the
`𝔽₂` example is unaffected -- but not over a general commutative ring.  The
cokernel of `b̃ : L ↪ L^∨` is precisely the *discriminant group* `L^∨/L`,
which is trivial exactly when `L` is unimodular.

So this structure is NOT "lattices"; it is the unimodular ones, and it
defines the discriminant form out of existence.  A general lattice layer
would weaken `form` to a `LinearMap` with a separate nondegeneracy field and
recover the unimodular case as the specialisation where `b̃` is an iso.  That
is deliberately not done here: the PoC only needs `𝔽₂`, where the notions
agree, and doing it properly is a real design task, not a rename.

-/
structure LatticeObj (R : FiniteRingObj) where
  module : FreeFinModuleObj R
  form :
    module.module.set ≃ₗ[R.set] Module.Dual R.set module.module.set
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

namespace LatticeObj

/--
The standard lattice on `R²`: the form with identity Gram matrix.

This is what `(R², id)` denotes in DSL source -- `id` is the *form*, not an
automorphism.  For the standard basis, `toDualEquiv` is precisely the
identity-Gram form `b(x,y) = Σᵢ xᵢ yᵢ`.

`noncomputable` because `toDualEquiv` is built with `LinearEquiv.ofBijective`
and so rests on `Classical.choice`.  That costs nothing here, and is quietly
a demonstration of the architecture's own point: `π_R` forgets the form, so
`|L|` reduces through `L.module` and never touches `form` at all.
-/
noncomputable def standard (R : FiniteRingObj) : LatticeObj R where
  module := FreeFinModuleObj.rankTwo R
  form := (Pi.basisFun R.set (Fin 2)).toDualEquiv
  symmetric := fun x y => Module.Basis.toDual_comm _ x y

end LatticeObj

/-- The `FreeFinMod(R)`-realization of a lattice: `(L,b) ↦ L`. -/
def Lattice.toFreeFinModule (R : FiniteRingObj) :
    LatticeObj R ⥤ FreeFinModuleObj R where
  obj L := L.module
  map f := f.hom

end CatDSL.Categories
