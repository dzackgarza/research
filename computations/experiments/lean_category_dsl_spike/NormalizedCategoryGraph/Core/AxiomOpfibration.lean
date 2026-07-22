/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.CategoricalPullback
import NormalizedCategoryGraph.Core.Ids
import Mathlib.CategoryTheory.Equivalence

/-!
# Axiomatic opfibration (meta-level)

Orientation: with forgetful arrows `E → C`, reindexing is contravariant
(a **fibration** over the forgetful graph). The project-facing name
`AxiomOpfibration` is retained.

Mathlib `CatCommSq T L R B` means `T ⋙ R ≅ L ⋙ B`. For a classifier square

```
E --totalMap--> E'
|forget_A        |forget_B
C --baseMap-->  C'
```

we need `totalMap ⋙ forget_B ≅ forget_A ⋙ baseMap`, i.e.
`CatCommSq totalMap forget_A forget_B baseMap`.
-/

namespace NormalizedCategoryGraph

open CategoryTheory

universe uObj uHom

set_option linter.checkUnivs false

/-- An object of the total classifier construction: `(C, ι_A : E → C)`. -/
structure ClassifiedCategory where
  host : ObjCat.{uObj, uHom}
  classifier : Classifier host

/-- A 2-commuting square of classified categories. -/
@[ext] structure ClassifierSquare (A B : ClassifiedCategory.{uObj, uHom}) where
  baseMap : A.host ⟶ B.host
  totalMap : A.classifier.total ⟶ B.classifier.total
  /-- Existence, rather than a chosen 2-cell, makes the square category strict. -/
  square : Nonempty <|
    CatCommSq
      totalMap.toFunctor
      A.classifier.forget.toFunctor
      B.classifier.forget.toFunctor
      baseMap.toFunctor

namespace AxiomOpfibration

private theorem composeSquare {A B C : ClassifiedCategory.{uObj, uHom}}
    (first : ClassifierSquare A B) (second : ClassifierSquare B C) :
    Nonempty <| CatCommSq
      (first.totalMap ≫ second.totalMap).toFunctor
      A.classifier.forget.toFunctor
      C.classifier.forget.toFunctor
      (first.baseMap ≫ second.baseMap).toFunctor :=
  first.square.elim fun firstSquare =>
    second.square.elim fun secondSquare =>
      ⟨CatCommSq.hComp' firstSquare secondSquare⟩

/-- Classified categories and classifier squares form a category. -/
instance : Category ClassifiedCategory where
  Hom A B := ClassifierSquare A B
  id A :=
    { baseMap := 𝟙 A.host
      totalMap := 𝟙 A.classifier.total
      square := ⟨CatCommSq.hId A.classifier.forget.toFunctor⟩ }
  comp f g :=
    { baseMap := f.baseMap ≫ g.baseMap
      totalMap := f.totalMap ≫ g.totalMap
      square := composeSquare f g }
  id_comp := by
    intro A B square
    ext <;> simp
  comp_id := by
    intro A B square
    ext <;> simp
  assoc := by
    intro W X Y Z first second third
    ext <;> simp

/-- The forgetful functor from classified categories to their hosts. -/
def projection : ClassifiedCategory.{uObj, uHom} ⥤ Cat.{uHom, max uObj uHom} where
  obj A := A.host
  map square := square.baseMap

/-- The classified object obtained by pulling a classifier back along a host functor. -/
noncomputable def reindexObject {C D : ObjCat.{uObj, uHom}} (F : D ⟶ C) (A : Classifier C) :
    ClassifiedCategory.{uObj, uHom} where
  host := D
  classifier := (Classifier.reindex F A).asClassifier

/-- The chosen reindexing arrow lies over the functor along which it was formed. -/
noncomputable def reindexLift {C D : ObjCat.{uObj, uHom}} (F : D ⟶ C) (A : Classifier C) :
    reindexObject F A ⟶ ⟨C, A⟩ :=
  let R := Classifier.reindex F A
  { baseMap := F
    totalMap := R.axiomProjection
    square := ⟨{ iso := R.square.iso.symm }⟩ }

@[simp]
theorem projection_reindexLift {C D : ObjCat.{uObj, uHom}} (F : D ⟶ C) (A : Classifier C) :
    projection.map (reindexLift F A) = F :=
  rfl

/-- Reindex a classified category along a base map into its host. -/
noncomputable def reindex {C D : ObjCat.{uObj, uHom}} (F : D ⟶ C) (A : Classifier C) :
    Reindexed F A :=
  Classifier.reindex F A

/-- Projection to the host category. -/
def baseProjection {C D : ObjCat.{uObj, uHom}} {F : D ⟶ C} {A : Classifier C}
    (R : Reindexed F A) : R.total ⟶ D :=
  R.baseProjection

/-- Projection to the classifier total. -/
def classifierProjection {C D : ObjCat.{uObj, uHom}} {F : D ⟶ C} {A : Classifier C}
    (R : Reindexed F A) : R.total ⟶ A.total :=
  R.axiomProjection

/-- The canonical square of a reindexing. -/
@[reducible] def square {C D : ObjCat.{uObj, uHom}} {F : D ⟶ C} {A : Classifier C}
    (R : Reindexed F A) :=
  R.square

/-- Identity reindex coherence (Equivalence of underlying categories). -/
structure ReindexIdIso {C : ObjCat.{uObj, uHom}} (A : Classifier C) where
  equiv : (Classifier.reindex (𝟙 C) A).total ≌ A.total

/-- Composition reindex coherence (Equivalence of underlying categories). -/
structure ReindexCompIso {B C D : ObjCat.{uObj, uHom}} (G : D ⟶ C) (F : C ⟶ B)
    (A : Classifier B) where
  equiv :
    (Classifier.reindex (G ≫ F) A).total ≌
      (Classifier.reindex G (Classifier.reindex F A).asClassifier).total

end AxiomOpfibration

end NormalizedCategoryGraph
