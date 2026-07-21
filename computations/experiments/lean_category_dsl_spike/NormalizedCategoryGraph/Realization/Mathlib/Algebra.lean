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
* Inverse — magmas with an involutive inverse operation and inverse-preserving
  morphisms (structure: faithful, not full). Does **not** force associativity
  or a unit (so it is not `GrpCat → MagmaCat`).
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
  carrier : Type u
  mul : Mul carrier
  one : One carrier
  one_mul : ∀ a : carrier, (1 : carrier) * a = a
  mul_one : ∀ a : carrier, a * (1 : carrier) = a

attribute [instance] UnitalMagma.mul UnitalMagma.one

namespace UnitalMagma

/-- Morphisms preserve multiplication and the unit. -/
@[ext]
structure Hom (A B : UnitalMagma.{u}) where
  toFun : A.carrier → B.carrier
  map_mul : ∀ x y, toFun (x * y) = toFun x * toFun y
  map_one : toFun (1 : A.carrier) = (1 : B.carrier)

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
  obj A := MagmaCat.of A.carrier
  map {A B} f := MagmaCat.ofHom
    { toFun := f.toFun
      map_mul' := f.map_mul }

end UnitalMagma

/-- Magma with an involutive inverse operation (no unit/associativity required). -/
structure MagmaWithInv where
  toMagma : MagmaCat.{u}
  inv : toMagma → toMagma
  inv_inv : ∀ x : toMagma, inv (inv x) = x

namespace MagmaWithInv

/-- Morphisms are magma morphisms that commute with `inv`. -/
@[ext]
structure Hom (A B : MagmaWithInv.{u}) where
  toHom : A.toMagma ⟶ B.toMagma
  map_inv : ∀ x : A.toMagma, (ConcreteCategory.hom toHom) (A.inv x) = B.inv ((ConcreteCategory.hom toHom) x)

instance : Category MagmaWithInv.{u} where
  Hom := Hom
  id A :=
    { toHom := 𝟙 A.toMagma
      map_inv := by intro x; simp }
  comp {A B C} f g :=
    { toHom := f.toHom ≫ g.toHom
      map_inv := by
        intro x
        simp [f.map_inv, g.map_inv] }

/-- Forgetful to `MagmaCat`. -/
def toMagmaCatFunctor : MagmaWithInv.{u} ⥤ MagmaCat.{u} where
  obj A := A.toMagma
  map {A B} f := f.toHom

end MagmaWithInv

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

/-- Inverse classifier: involutive inverse, not `GrpCat`. -/
noncomputable def inverse : Classifier Magmas where
  total := Cat.of MagmaWithInv.{u}
  forget := MagmaWithInv.toMagmaCatFunctor.toCatHom

/-- Algebra atoms over the Mathlib foundations. -/
noncomputable def algebraAtoms : AlgebraAtoms foundationAtoms where
  associative := associative
  commutative := commutative
  unital := unital
  inverse := inverse

end NormalizedCategoryGraph.Realization.Mathlib
