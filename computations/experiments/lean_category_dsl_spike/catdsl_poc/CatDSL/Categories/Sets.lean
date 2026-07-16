import CatDSL.Foundation

/-!
# Sets, countable sets, finite sets

Each layer is an object *type* carrying a Mathlib `Category` instance,
bundled with `Cat.of` into a first-class category object.  This is the
reference shape for every category module.
-/

namespace CatDSL.Categories

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

namespace SetObj

/--
The **cardinality** of a set — total on `Sets`, valued in cardinals.  Every
set has one; `ℤ` has one.

This is the concept; its home is `Sets`, all of it.  It is not a functor out
of the whole category into the discrete category of cardinals (a functor
into a discrete category would force `|X| = |Y|` whenever any map `X → Y`
exists); it is a functor on the **core groupoid** — an isomorphism invariant
of objects, transported along bijections and nothing else.

The enumeration-equipped subcategories (`FiniteSetObj`, `CountableSetObj`)
are *presentations* that evaluate this invariant (`cardinality_eval` below),
never its home.
-/
def cardinality (X : SetObj) : Cardinal :=
  Cardinal.mk X.set

end SetObj

/-- `ℤ` as a set object: infinite sets are first-class citizens of `Sets`,
and the cardinality invariant is total on them. -/
def integers : SetObj := ⟨ℤ⟩

/-- `|ℤ| = ℵ₀`, obviously. -/
theorem cardinality_integers : integers.cardinality = Cardinal.aleph0 :=
  Cardinal.mk_int

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

/--
Evaluation of the cardinality invariant on an enumeration-equipped
presentation: `|X|` read off the chosen `X ≃ Fin size`.

This is the finite fragment's *computation witness*, not the concept — the
concept is `SetObj.cardinality`, total on `Sets` (its home).
`cardinality_eval` is the proof that this evaluation computes the invariant.
-/
def cardinality (X : FiniteSetObj) : Nat :=
  X.size

/-- The presentation evaluates the invariant: for an enumeration-equipped
finite set, the total cardinality on `Sets` is exactly `size`. -/
theorem cardinality_eval (X : FiniteSetObj) :
    (FiniteSet.forget.obj X).cardinality = (cardinality X : Cardinal) :=
  (Cardinal.mk_congr X.enumerate).trans (Cardinal.mk_fin X.size)

/-- The concrete two-element set `{0,1}`, owned by `FiniteSets`. -/
abbrev two : FiniteSetObj where
  set := ZMod 2
  size := 2
  enumerate := Equiv.refl (Fin 2)

/--
Paper-like notation for `two`.

`𝟚` is U+1D7DA, a mathematical double-struck *digit*.  Lean's identifier
lexer accepts double-struck *letters* (`𝔽` is fine) but rejects digits, so
`def 𝟚` cannot be written.  Notation may use any token, so the surface
spelling lives here over a declaration whose name Lean can lex.
-/
notation "𝟚" => two

end CatDSL.Categories
