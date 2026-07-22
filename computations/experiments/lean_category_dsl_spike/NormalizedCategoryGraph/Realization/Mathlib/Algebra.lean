/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Algebra.Category.Semigrp.Basic
import Mathlib.Algebra.Group.Defs
import Mathlib.CategoryTheory.Category.Cat
import Mathlib.CategoryTheory.ConcreteCategory.Basic
import Mathlib.CategoryTheory.ObjectProperty.FullSubcategory
import NormalizedCategoryGraph.Realization.Mathlib.Foundation

/-!
# Mathlib algebra atoms on Magmas

* Associative — `Semigrp → MagmaCat`
* Commutative — full subcategory of commutative magmas (property)
* Unital — magmas with a designated unit and **unit-preserving** morphisms
  (structure: faithful, not full)
* Inverse — unital magmas with an inverse operation satisfying both inverse laws,
  with inverse- and unit-preserving morphisms.
-/

namespace NormalizedCategoryGraph.Realization.Mathlib

open CategoryTheory
open NormalizedCategoryGraph

universe u

set_option linter.checkUnivs false

/-- Commutative magmas as a full subcategory of `MagmaCat`. -/
abbrev CommMagmaCat : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := MagmaCat.{u}) (fun M : MagmaCat.{u} => Nonempty (CommMagma M))

/-- Magma with a designated two-sided unit. -/
structure UnitalMagma where
  underlyingSet : Type u
  mul : Mul underlyingSet
  one : One underlyingSet
  one_mul : ∀ a : underlyingSet, (1 : underlyingSet) * a = a
  mul_one : ∀ a : underlyingSet, a * (1 : underlyingSet) = a

attribute [instance] UnitalMagma.mul UnitalMagma.one

namespace UnitalMagma

/-- Morphisms preserve multiplication and the unit. -/
@[ext]
structure Hom (A B : UnitalMagma.{u}) where
  toFun : A.underlyingSet → B.underlyingSet
  map_mul : ∀ x y, toFun (x * y) = toFun x * toFun y
  map_one : toFun (1 : A.underlyingSet) = (1 : B.underlyingSet)

instance : Category UnitalMagma.{u} where
  Hom := Hom
  id A :=
    { toFun := id
      map_mul := by intro x y; rfl
      map_one := rfl }
  comp {A B C} f g :=
    { toFun := g.toFun ∘ f.toFun
      map_mul := by
        intro x y
        simp [f.map_mul, g.map_mul]
      map_one := by simp [f.map_one, g.map_one] }

/-- Forgetful to `MagmaCat`. -/
def toMagmaCatFunctor : UnitalMagma.{u} ⥤ MagmaCat.{u} where
  obj A := MagmaCat.of A.underlyingSet
  map {A B} f := MagmaCat.ofHom
    { toFun := f.toFun
      map_mul' := f.map_mul }

end UnitalMagma

/-- A unital magma with two-sided inverse equations. -/
structure UnitalMagmaWithInv where
  toUnitalMagma : UnitalMagma.{u}
  inv : toUnitalMagma.underlyingSet → toUnitalMagma.underlyingSet
  mul_inv : ∀ x : toUnitalMagma.underlyingSet, x * inv x = 1
  inv_mul : ∀ x : toUnitalMagma.underlyingSet, inv x * x = 1

namespace UnitalMagmaWithInv

/-- Morphisms preserve multiplication, the chosen unit, and inverse. -/
@[ext]
structure Hom (A B : UnitalMagmaWithInv.{u}) where
  toHom : A.toUnitalMagma ⟶ B.toUnitalMagma
  map_inv : ∀ x : A.toUnitalMagma.underlyingSet,
    toHom.toFun (A.inv x) = B.inv (toHom.toFun x)

instance : Category UnitalMagmaWithInv.{u} where
  Hom := Hom
  id A :=
    { toHom := 𝟙 A.toUnitalMagma
      map_inv := by intro x; rfl }
  comp {A B C} f g :=
    { toHom := f.toHom ≫ g.toHom
      map_inv := by
        intro x
        change g.toHom.toFun (f.toHom.toFun (A.inv x)) = _
        rw [f.map_inv, g.map_inv]
        rfl }

 /-- Forgetful to the selected unital-magma host. -/
def toUnitalMagmaFunctor : UnitalMagmaWithInv.{u} ⥤ UnitalMagma.{u} where
  obj A := A.toUnitalMagma
  map {A B} f := f.toHom

end UnitalMagmaWithInv

/-- Operation-role wrapper for the additive presentation of a magma. -/
structure AdditiveMagma where
  toMagma : MagmaCat.{u}

namespace AdditiveMagma

abbrev Hom (A B : AdditiveMagma.{u}) := A.toMagma ⟶ B.toMagma

instance : Category AdditiveMagma.{u} where
  Hom := Hom
  id A := 𝟙 A.toMagma
  comp f g := f ≫ g

def toMagmaCatFunctor : AdditiveMagma.{u} ⥤ MagmaCat.{u} where
  obj A := A.toMagma
  map f := f

end AdditiveMagma

/-- Operation-role wrapper for the multiplicative presentation of a magma. -/
structure MultiplicativeMagma where
  toMagma : MagmaCat.{u}

namespace MultiplicativeMagma

abbrev Hom (A B : MultiplicativeMagma.{u}) := A.toMagma ⟶ B.toMagma

instance : Category MultiplicativeMagma.{u} where
  Hom := Hom
  id A := 𝟙 A.toMagma
  comp f g := f ≫ g

def toMagmaCatFunctor : MultiplicativeMagma.{u} ⥤ MagmaCat.{u} where
  obj A := A.toMagma
  map f := f

end MultiplicativeMagma

/-- Associative classifier. -/
noncomputable def associative : Classifier Magmas where
  total := Cat.of Semigrp.{u}
  forget := (forget₂ Semigrp MagmaCat).toCatHom

/-- Commutative classifier (property: full subcategory). -/
noncomputable def commutative : Classifier Magmas where
  total := Cat.of CommMagmaCat.{u}
  forget := (ObjectProperty.ι
      (C := MagmaCat.{u}) (fun M : MagmaCat.{u} => Nonempty (CommMagma M))).toCatHom

/-- Unital classifier: unit-preserving morphisms (structure, not full). -/
noncomputable def unital : Classifier Magmas where
  total := Cat.of UnitalMagma.{u}
  forget := UnitalMagma.toMagmaCatFunctor.toCatHom

/-- The named host category for inverse laws. -/
noncomputable def UnitalMagmas : ObjCat := unital.total

/-- Inverse classifier on unital magmas, with both group inverse equations. -/
noncomputable def inverse : Classifier unital.total where
  total := Cat.of UnitalMagmaWithInv.{u}
  forget := UnitalMagmaWithInv.toUnitalMagmaFunctor.toCatHom

/-- Magmas.Additive retains the operation role in its categorical objects. -/
noncomputable def additive : Classifier Magmas where
  total := Cat.of AdditiveMagma.{u}
  forget := AdditiveMagma.toMagmaCatFunctor.toCatHom

/-- Magmas.Multiplicative retains the operation role in its categorical objects. -/
noncomputable def multiplicative : Classifier Magmas where
  total := Cat.of MultiplicativeMagma.{u}
  forget := MultiplicativeMagma.toMagmaCatFunctor.toCatHom

/-- Algebra atoms over the Mathlib foundations. -/
noncomputable def algebraAtoms : AlgebraAtoms foundationAtoms where
  associative := associative
  commutative := commutative
  unital := unital
  inverse := inverse
  additive := additive
  multiplicative := multiplicative

end NormalizedCategoryGraph.Realization.Mathlib
