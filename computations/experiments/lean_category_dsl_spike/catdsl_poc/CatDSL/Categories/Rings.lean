import CatDSL.Categories.Sets

/-!
# Commutative rings and the finite subcategory

The category of commutative rings IS Mathlib's `CommRingCat`; nothing
local is declared for it.  Finite commutative rings are the full
subcategory on the property `Finite` — no new noun.
-/

namespace CatDSL.Categories

open CategoryTheory CatDSL

/-- The category of finite commutative rings: the full subcategory of
`CommRingCat` on `Finite`. -/
abbrev FinCommRing :=
  ObjectProperty.FullSubcategory (fun R : CommRingCat => Finite R.carrier)

/-- The inclusion into commutative rings. -/
def FinCommRing.ι : FinCommRing ⥤ CommRingCat :=
  ObjectProperty.ι _

/--
The restriction of the forgetful functor to the finite fragment: a finite
ring's underlying set is finite, so `forget` lifts through the `Finite`
property.  This is a restriction square of standard functors, not a new
arrow.
-/
def FinCommRing.toFinSet : FinCommRing ⥤ FinSet :=
  ObjectProperty.lift _
    (ObjectProperty.ι _ ⋙ CategoryTheory.forget CommRingCat)
    fun R => R.property

/-- The worked-example base ring: `𝔽₂ = ℤ/2` as a finite commutative ring.
An example-local object built from identified pieces, not vocabulary. -/
noncomputable abbrev 𝔽₂ : FinCommRing :=
  ⟨CommRingCat.of (ZMod 2), inferInstanceAs (Finite (ZMod 2))⟩

end CatDSL.Categories
