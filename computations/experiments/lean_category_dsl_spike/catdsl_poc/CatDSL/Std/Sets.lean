import CatDSL.Foundation

/-!
# Sets, countable sets, finite sets

Each layer is an object *type* carrying a Mathlib `Category` instance,
bundled with `Cat.of` into a first-class category object.  This is the
reference shape for every category module.
-/

namespace CatDSL.Std

open CategoryTheory CatDSL

/-- A small set. -/
structure SetObj where
  set : Type

instance : CoeSort SetObj Type where
  coe X := X.set

instance : Category SetObj where
  Hom X Y := X.set → Y.set
  id _ := fun x => x
  comp f g := fun x => g (f x)

/-- The category of small sets, as a first-class category object. -/
abbrev Sets : LargeCat := Cat.of SetObj

/--
A set carrying an actual countability implementation.

`number` is injective because `nth (number x) = some x`.  Morphisms are all
functions between the `Set`-realizations; they need not preserve the chosen
implementation.
-/
structure CountableSetObj where
  set : Type
  number : set → Nat
  nth : Nat → Option set
  nth_number : ∀ x, nth (number x) = some x

instance : CoeSort CountableSetObj Type where
  coe X := X.set

instance : Category CountableSetObj where
  Hom X Y := X.set → Y.set
  id _ := fun x => x
  comp f g := fun x => g (f x)

abbrev CountableSets : LargeCat := Cat.of CountableSetObj

/-- The `Set`-realization of a countable set. -/
def CountableSet.forget : CountableSetObj ⥤ SetObj where
  obj X := ⟨X.set⟩
  map f := f

/--
A finite set with a chosen enumeration.  The enumeration is data, not a
proposition asserting finiteness.
-/
structure FiniteSetObj where
  set : Type
  size : Nat
  enumerate : set ≃ Fin size

instance : CoeSort FiniteSetObj Type where
  coe X := X.set

instance : Category FiniteSetObj where
  Hom X Y := X.set → Y.set
  id _ := fun x => x
  comp f g := fun x => g (f x)

abbrev FiniteSets : LargeCat := Cat.of FiniteSetObj

namespace FiniteSetObj

def number (X : FiniteSetObj) : X.set → Nat :=
  fun x => (X.enumerate x).val

def nth (X : FiniteSetObj) : Nat → Option X.set :=
  fun n =>
    if h : n < X.size then
      some (X.enumerate.symm ⟨n, h⟩)
    else
      none

theorem nth_number (X : FiniteSetObj) :
    ∀ x, X.nth (X.number x) = some x := by
  intro x
  simp [nth, number]

/-- The countability implementation induced by a chosen enumeration. -/
def toCountable (X : FiniteSetObj) : CountableSetObj where
  set := X.set
  number := X.number
  nth := X.nth
  nth_number := X.nth_number

/--
The product of finite sets, enumerated by the standard mixed-radix
equivalence `Fin m × Fin n ≃ Fin (m*n)`.

`finProdFinEquiv` is top-level with `{m n}` implicit; it is not
`Fin.finProdFinEquiv`, and takes no explicit size arguments.
-/
def prod (X Y : FiniteSetObj) : FiniteSetObj where
  set := X.set × Y.set
  size := X.size * Y.size
  enumerate :=
    (Equiv.prodCongr X.enumerate Y.enumerate).trans finProdFinEquiv

@[simp]
theorem prod_size (X Y : FiniteSetObj) :
    (prod X Y).size = X.size * Y.size :=
  rfl

end FiniteSetObj

/-- The `Set`-realization of a finite set. -/
def FiniteSet.forget : FiniteSetObj ⥤ SetObj where
  obj X := ⟨X.set⟩
  map f := f

/-- Every finite set is countable, via its chosen enumeration. -/
def FiniteSet.toCountable : FiniteSetObj ⥤ CountableSetObj where
  obj := FiniteSetObj.toCountable
  map f := f

/-- The finite cardinality implementation used by the elaborator. -/
def cardinality (X : FiniteSetObj) : Nat :=
  X.size

end CatDSL.Std
