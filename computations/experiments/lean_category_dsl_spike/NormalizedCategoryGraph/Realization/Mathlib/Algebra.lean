/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Algebra.Category.Grp.Basic
import Mathlib.Algebra.Category.MonCat.Adjunctions
import Mathlib.Algebra.Category.Semigrp.Basic
import Mathlib.Algebra.Group.Defs
import Mathlib.CategoryTheory.Category.Cat
import Mathlib.CategoryTheory.ConcreteCategory.Basic
import Mathlib.CategoryTheory.ObjectProperty.FullSubcategory
import NormalizedCategoryGraph.Realization.Mathlib.Foundation

/-!
# Mathlib algebra atoms on Magmas

Classifiers whose least host is Magmas:

* Associative — `Semigrp → MagmaCat`
* Commutative — full subcategory of commutative magmas
* Unital — full subcategory of `MulOneClass` magmas
* Inverse — `GrpCat → MagmaCat` (composite of forget₂)
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

/-- Magmas with a two-sided unit (`MulOneClass`) as a full subcategory of `MagmaCat`. -/
abbrev UnitalMagmaCat : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := MagmaCat.{u}) (fun M : MagmaCat.{u} => Nonempty (MulOneClass M))

/-- Associative classifier. -/
noncomputable def associative : Classifier Magmas where
  total := Cat.of Semigrp.{u}
  forget := (forget₂ Semigrp MagmaCat).toCatHom

/-- Commutative classifier. -/
noncomputable def commutative : Classifier Magmas where
  total := Cat.of CommMagmaCat.{u}
  forget := (ObjectProperty.ι
      (C := MagmaCat.{u}) (fun M : MagmaCat.{u} => Nonempty (CommMagma M))).toCatHom

/-- Unital classifier (unit laws; not necessarily associative). -/
noncomputable def unital : Classifier Magmas where
  total := Cat.of UnitalMagmaCat.{u}
  forget := (ObjectProperty.ι
      (C := MagmaCat.{u}) (fun M : MagmaCat.{u} => Nonempty (MulOneClass M))).toCatHom

/-- Forgetful `GrpCat → MagmaCat` via MonCat and Semigrp. -/
noncomputable def grpToMagma : GrpCat.{u} ⥤ MagmaCat.{u} :=
  forget₂ GrpCat MonCat ⋙ forget₂ MonCat Semigrp ⋙ forget₂ Semigrp MagmaCat

/-- Inverse classifier (groups as magmas with inverse). -/
noncomputable def inverse : Classifier Magmas where
  total := Cat.of GrpCat.{u}
  forget := grpToMagma.toCatHom

/-- Algebra atoms over the Mathlib foundations. -/
noncomputable def algebraAtoms : AlgebraAtoms foundationAtoms where
  associative := associative
  commutative := commutative
  unital := unital
  inverse := inverse

end NormalizedCategoryGraph.Realization.Mathlib
