import CatDSL.Foundation

/-!
# Sets and its property subcategories

**Convention (category vs objects).**  Following Mathlib (`CommRingCat`,
`ModuleCat` are *types* whose terms are the objects), a category is
presented as its object type together with its `Category` instance.  There
are no local object wrappers: the category of sets IS `Type`; finite and
countable sets are the full subcategories of `Type` cut out by the
PROPERTIES `Finite` and `Countable`.  Chosen computational data
(`Fintype`, `Encodable`, `FinEnum`) are witnesses used at evaluation
seams — typeclass instances on the underlying types — never object
structure and never categories.
-/

namespace CatDSL.Categories

open CategoryTheory CatDSL

/-- The category of sets, bundled for the preferred-functor graph.  The
category itself is Mathlib's `Type` with its `types` instance; there is
nothing local to declare. -/
abbrev Sets : LargeCat := Cat.of Type

/-- The category of countable sets: the full subcategory of `Type` on the
property `Countable`. -/
abbrev CountSet :=
  ObjectProperty.FullSubcategory (fun X : Type => Countable X)

/-- The category of finite sets: the full subcategory of `Type` on the
property `Finite`. -/
abbrev FinSet :=
  ObjectProperty.FullSubcategory (fun X : Type => Finite X)

/-- The inclusion of countable sets into sets: Mathlib's `ObjectProperty.ι`,
named so the preferred-functor graph can register this edge. -/
def CountSet.ι : CountSet ⥤ Type :=
  ObjectProperty.ι _

/-- The inclusion of finite sets into sets. -/
def FinSet.ι : FinSet ⥤ Type :=
  ObjectProperty.ι _

/-- Finite sets include into countable sets: the functor induced by the
property implication `Finite → Countable` (Mathlib's `ιOfLE`). -/
def FinSet.toCountSet : FinSet ⥤ CountSet :=
  ObjectProperty.ιOfLE fun X h => @Finite.to_countable X h

end CatDSL.Categories
