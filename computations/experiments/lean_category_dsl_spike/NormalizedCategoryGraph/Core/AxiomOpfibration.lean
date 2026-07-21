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
structure ClassifierSquare (A B : ClassifiedCategory.{uObj, uHom}) where
  baseMap : A.host ⟶ B.host
  totalMap : A.classifier.total ⟶ B.classifier.total
  square :
    CatCommSq
      totalMap.toFunctor
      A.classifier.forget.toFunctor
      B.classifier.forget.toFunctor
      baseMap.toFunctor

namespace AxiomOpfibration

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
