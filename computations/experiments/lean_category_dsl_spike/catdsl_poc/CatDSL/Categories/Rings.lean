import CatDSL.Categories.Sets

/-!
# Rings and finite rings

Each layer is an object type + a Mathlib `Category` instance, bundled into a
first-class category object with `Cat.of`.

**Functors are declared between the object types** (`RingObj ⥤ SetObj`), not
between the bundled objects (`Rings ⥤ Sets`).  Routing them through the
bundles would resolve `Cat.str Rings` rather than the `Category RingObj`
instance -- a diamond -- and leaves `⇑f` unable to find its coercion.  The
bundles exist for the category graph; the functors are stated where the
elaborator sees through them.  This is also what Mathlib does.
-/

namespace CatDSL.Categories

open CategoryTheory CatDSL

/-- A small commutative ring. -/
structure RingObj where
  set : Type
  commRing : CommRing set

attribute [instance] RingObj.commRing

instance : CoeSort RingObj Type where
  coe R := R.set

instance : Category RingObj where
  Hom R S := R.set →+* S.set
  id R := RingHom.id R.set
  comp f g := g.comp f

abbrev Rings : LargeCat := Cat.of RingObj

/--
Tether witness: our category of rings IS Mathlib's `CommRingCat`, as an
equivalence of categories — the #217 consolidation claim kernel-checked
*before* any structure retirement.  Structure eta makes both round trips
definitional, so the unit and counit are identities.
-/
def RingObj.equivCommRingCat : RingObj ≌ CommRingCat where
  functor :=
    { obj := fun R => CommRingCat.of R.set
      map := fun {R S} (f : R.set →+* S.set) => CommRingCat.ofHom f }
  inverse :=
    { obj := fun X => ⟨X.carrier, inferInstance⟩
      map := fun f => f.hom }
  unitIso := NatIso.ofComponents fun R => Iso.refl _
  counitIso := NatIso.ofComponents fun X => Iso.refl _

/-- The `Set`-realization of a ring. -/
def Ring.forget : RingObj ⥤ SetObj where
  obj R := ⟨R.set⟩
  -- The binder's explicit type forces `R ⟶ S =?= R.set →+* S.set` at default
  -- transparency; `⇑f` then has a `RingHom` to coerce.
  map {R S} (f : R.set →+* S.set) := ⇑f

/--
A commutative ring structure on an object already owned by `FiniteSets`.
The finite set is not reconstructed or duplicated by the ring layer.
-/
structure FiniteRingObj where
  finiteSet : FiniteSetObj
  commRing : CommRing finiteSet.set

attribute [instance] FiniteRingObj.commRing

namespace FiniteRingObj

/--
`abbrev`, not `def`: instance search only unfolds reducible definitions, so
`CommRing R.set` would not be found from the `CommRing R.finiteSet.set`
instance despite the two being definitionally equal.
-/
abbrev set (R : FiniteRingObj) : Type :=
  R.finiteSet.set

instance : CoeSort FiniteRingObj Type where
  coe R := R.set

abbrev size (R : FiniteRingObj) : Nat :=
  R.finiteSet.size

abbrev enumerate (R : FiniteRingObj) :
    R.set ≃ Fin R.size :=
  R.finiteSet.enumerate

abbrev toRing (R : FiniteRingObj) : RingObj where
  set := R.set
  commRing := R.commRing

abbrev toFiniteSet (R : FiniteRingObj) : FiniteSetObj :=
  R.finiteSet

def prod (R S : FiniteRingObj) : FiniteRingObj where
  finiteSet := FiniteSetObj.prod R.finiteSet S.finiteSet
  commRing := by
    -- `FiniteSetObj.prod` is a `def`, so the goal's `.set` will not reduce
    -- for instance search; `show` reduces it at default transparency.
    show CommRing (R.set × S.set)
    infer_instance

end FiniteRingObj

instance : Category FiniteRingObj where
  Hom R S := R.set →+* S.set
  id R := RingHom.id R.set
  comp f g := g.comp f

abbrev FiniteRings : LargeCat := Cat.of FiniteRingObj

def FiniteRing.toRing : FiniteRingObj ⥤ RingObj where
  obj := FiniteRingObj.toRing
  map f := f

/-- The `FiniteSet`-realization of a finite ring. -/
def FiniteRing.toFiniteSet : FiniteRingObj ⥤ FiniteSetObj where
  obj := FiniteRingObj.toFiniteSet
  map {R S} (f : R.set →+* S.set) := ⇑f

/-- The field `𝔽₂`: the commutative-ring structure on `𝟚`. -/
def 𝔽₂ : FiniteRingObj where
  finiteSet := 𝟚
  commRing := inferInstance

end CatDSL.Categories
