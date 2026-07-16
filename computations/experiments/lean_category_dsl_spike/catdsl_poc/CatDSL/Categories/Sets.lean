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

/--
Tether witness: our category of sets IS Mathlib's category of types, as an
equivalence of categories.  `SetObj` is a transparent bundling of `Type`;
this witness is the kernel-checked form of that claim.
-/
def SetObj.equivTypes : SetObj ≌ Type where
  functor :=
    { obj := fun X => X.set
      -- this Mathlib wraps `Type`'s morphisms (`TypeCat.Hom`); wrap/unwrap
      -- explicitly
      map := fun {X Y} (f : X.set → Y.set) => TypeCat.ofHom f }
  inverse :=
    { obj := fun T => ⟨T⟩
      map := fun {T U} f => (f.hom : T → U) }
  unitIso := NatIso.ofComponents fun X => Iso.refl _
  counitIso := NatIso.ofComponents fun T => Iso.refl _

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

/-- Tether witness: `cardinality` IS `Cardinal.mk`, definitionally. -/
theorem cardinality_eq_mk (X : SetObj) :
    X.cardinality = Cardinal.mk X.set :=
  rfl

end SetObj

/-- `ℤ` as a set object: infinite sets are first-class citizens of `Sets`,
and the cardinality invariant is total on them. -/
def integers : SetObj := ⟨ℤ⟩

/-- `|ℤ| = ℵ₀`, obviously. -/
theorem cardinality_integers : integers.cardinality = Cardinal.aleph0 :=
  Cardinal.mk_int

/-- Tether witness: `integers` carries Mathlib's `ℤ`, definitionally. -/
def integers.equivInt : integers.set ≃ ℤ :=
  Equiv.refl ℤ

/--
A set carrying an actual countability implementation.

`number` is injective because `nth (number x) = some x`.  Morphisms are all
functions between the `Set`-realizations; they need not preserve the chosen
implementation.

**Mathlib identity.**  Field for field this is Mathlib's `Encodable`
(`encode` / `decode` / `encodek`) in bundled-object form; the manifest
aligns the concept to `Encodable`.

Convention divergence: bundled object structure vs Mathlib's typeclass form
(`Encodable`).  Reason: the spike wanted objects carrying chosen data as
first-class category objects.  Adjudication: local change queued — the
#217-ratified consolidation replaces this structure with a thin bundling of
the class; until then any new field must mirror the class exactly so the
consolidation stays mechanical.
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

/-- Tether witness: the fields of a countable set object ARE an `Encodable`
instance — the tie to Mathlib as a construction, not prose. -/
@[reducible]
def CountableSetObj.encodable (X : CountableSetObj) : Encodable X.set :=
  ⟨X.number, X.nth, X.nth_number⟩

/--
A finite set with a chosen enumeration.  The enumeration is data, not a
proposition asserting finiteness.

**Mathlib identity.**  This is Mathlib's `FinEnum` (`card` + `α ≃ Fin card`)
in bundled-object form; the manifest aligns the concept to `FinEnum`.

Convention divergence: bundled object structure vs Mathlib's typeclass form
(`FinEnum`).  Same status as `CountableSetObj` above: local change queued
per the #217-ratified consolidation; new fields must mirror the class.
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

/-- Tether witness: the fields of a finite set object ARE a `FinEnum`
instance (`decEq` transported along the chosen enumeration). -/
@[reducible]
def finEnum (X : FiniteSetObj) : FinEnum X.set where
  card := X.size
  equiv := X.enumerate
  decEq := X.enumerate.decidableEq

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

/-- Tether witness: the finite evaluation IS Mathlib's `FinEnum.card`. -/
theorem cardinality_eq_finEnumCard (X : FiniteSetObj) :
    cardinality X = @FinEnum.card X.set X.finEnum :=
  rfl

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

/-- Tether witness: `two` carries Mathlib's `ZMod 2`, definitionally. -/
def two.equivZMod : (two).set ≃ ZMod 2 :=
  Equiv.refl _

end CatDSL.Categories
