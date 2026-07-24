/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Classifier
import Mathlib.CategoryTheory.Limits.Shapes.Pullback.Categorical.Basic
import Mathlib.CategoryTheory.CatCommSq

/-!
# Categorical pullback coercions for `Cat`

Category files must never see `Cat.Hom` ↔ functor coercions. All reindexing
goes through `Classifier.reindex` here.

Mathlib path: `CategoryTheory.Limits.CategoricalPullback`.
-/

namespace NormalizedCategoryGraph

open CategoryTheory CategoryTheory.Limits

universe uObj uHom

/-- Generated data of reindexing a classifier along `F : D ⟶ C`. -/
structure Reindexed {C D : ObjCat.{uObj, uHom}} (F : D ⟶ C) (A : Classifier C) where
  total : ObjCat.{uObj, uHom}
  baseProjection : total ⟶ D
  axiomProjection : total ⟶ A.total
  /-- Underlying 2-commutative square on functors. -/
  square :
    CatCommSq
      baseProjection.toFunctor
      axiomProjection.toFunctor
      F.toFunctor
      A.forget.toFunctor

/-- View a reindexing as a classifier on the domain. -/
def Reindexed.asClassifier {C D : ObjCat.{uObj, uHom}} {F : D ⟶ C} {A : Classifier C}
    (R : Reindexed F A) : Classifier D :=
  ⟨R.total, R.baseProjection⟩

/-- Uniform reindex: `F^* A := D ×_C C.A → D`, via Mathlib's categorical pullback. -/
noncomputable def Classifier.reindex {C D : ObjCat.{uObj, uHom}} (F : D ⟶ C)
    (A : Classifier C) : Reindexed F A :=
  let P := CategoricalPullback F.toFunctor A.forget.toFunctor
  { total := Cat.of P
    baseProjection := (CategoricalPullback.π₁ F.toFunctor A.forget.toFunctor).toCatHom
    axiomProjection := (CategoricalPullback.π₂ F.toFunctor A.forget.toFunctor).toCatHom
    square := CategoricalPullback.catCommSq F.toFunctor A.forget.toFunctor }

end NormalizedCategoryGraph
