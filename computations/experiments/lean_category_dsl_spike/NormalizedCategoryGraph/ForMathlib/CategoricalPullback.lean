/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.CategoryTheory.Equivalence
import Mathlib.CategoryTheory.Limits.Shapes.Pullback.Categorical.Basic
import NormalizedCategoryGraph.Core.AxiomOpfibration
import NormalizedCategoryGraph.Core.CategoricalPullback

/-!
# Categorical pullback coherences

Proves the reindexing equivalences:

* `(𝟙)^* A ≌ A`
* `(G ≫ F)^* A ≌ G^*(F^* A)`
-/

namespace NormalizedCategoryGraph.ForMathlib

open CategoryTheory CategoryTheory.Limits NormalizedCategoryGraph

universe v u uObj uHom

set_option linter.checkUnivs false
set_option maxHeartbeats 800000

/-- Section of `π₂` along the identity cospan. -/
@[simps!]
noncomputable def pullbackIdSection {A : Type u} {B : Type u} [Category.{v} A] [Category.{v} B]
    (G : B ⥤ A) : B ⥤ CategoricalPullback (𝟭 A) G where
  obj b := ⟨G.obj b, b, Iso.refl _⟩
  map f := ⟨G.map f, f, by cat_disch⟩

/-- Unit isomorphism for identity reindexing. -/
noncomputable def pullbackIdUnit {A : Type u} {B : Type u} [Category.{v} A] [Category.{v} B]
    (G : B ⥤ A) :
    𝟭 (CategoricalPullback (𝟭 A) G) ≅
      CategoricalPullback.π₂ (𝟭 A) G ⋙ pullbackIdSection G :=
  NatIso.ofComponents
    (fun P => CategoricalPullback.mkIso P.iso (Iso.refl _) (by
      change P.iso.hom ≫ 𝟙 _ = P.iso.hom ≫ G.map (𝟙 _)
      simp))
    (fun {P Q} f => by
      refine CategoricalPullback.hom_ext ?_ ?_
      · change f.fst ≫ Q.iso.hom = P.iso.hom ≫ G.map f.snd
        exact f.w
      · change f.snd ≫ 𝟙 _ = 𝟙 _ ≫ f.snd
        simp)

/-- Pullback along the identity ≃ domain of the second leg. -/
noncomputable def pullbackIdEquiv {A : Type u} {B : Type u} [Category.{v} A] [Category.{v} B]
    (G : B ⥤ A) : CategoricalPullback (𝟭 A) G ≌ B :=
  CategoryTheory.Equivalence.mk
    (CategoricalPullback.π₂ (𝟭 A) G)
    (pullbackIdSection G)
    (pullbackIdUnit G)
    (Iso.refl (𝟭 B))

/-- Forward pasting functor. -/
@[simps!]
noncomputable def pullbackCompFwd {A B C E : Type u}
    [Category.{v} A] [Category.{v} B] [Category.{v} C] [Category.{v} E]
    (F : B ⥤ A) (G : C ⥤ B) (H : E ⥤ A) :
    CategoricalPullback (G ⋙ F) H ⥤ CategoricalPullback G (CategoricalPullback.π₁ F H) where
  obj P := ⟨P.fst, ⟨G.obj P.fst, P.snd, P.iso⟩, Iso.refl _⟩
  map f := ⟨f.fst, ⟨G.map f.fst, f.snd, f.w⟩, by
    change G.map f.fst ≫ 𝟙 _ = 𝟙 _ ≫ G.map f.fst
    simp⟩

/-- Compatibility of backward pasting on morphisms. -/
theorem pullbackCompBwd_w {A B C E : Type u}
    [Category.{v} A] [Category.{v} B] [Category.{v} C] [Category.{v} E]
    (F : B ⥤ A) (G : C ⥤ B) (H : E ⥤ A)
    {X Y : CategoricalPullback G (CategoricalPullback.π₁ F H)} (f : X ⟶ Y) :
    (G ⋙ F).map f.fst ≫ (F.mapIso Y.iso ≪≫ Y.snd.iso).hom =
      (F.mapIso X.iso ≪≫ X.snd.iso).hom ≫ H.map f.snd.snd := by
  have w₁F : (G ⋙ F).map f.fst ≫ F.map Y.iso.hom =
      F.map X.iso.hom ≫ F.map ((CategoricalPullback.π₁ F H).map f.snd) := by
    have := congrArg F.map f.w
    simp only [Functor.map_comp, Functor.comp_map] at this ⊢
    exact this
  have w₂ := f.snd.w
  calc
    (G ⋙ F).map f.fst ≫ (F.mapIso Y.iso ≪≫ Y.snd.iso).hom
        = (G ⋙ F).map f.fst ≫ F.map Y.iso.hom ≫ Y.snd.iso.hom := rfl
    _ = ((G ⋙ F).map f.fst ≫ F.map Y.iso.hom) ≫ Y.snd.iso.hom := (Category.assoc _ _ _).symm
    _ = (F.map X.iso.hom ≫ F.map ((CategoricalPullback.π₁ F H).map f.snd)) ≫ Y.snd.iso.hom :=
          congrArg (· ≫ Y.snd.iso.hom) w₁F
    _ = F.map X.iso.hom ≫ F.map ((CategoricalPullback.π₁ F H).map f.snd) ≫ Y.snd.iso.hom :=
          Category.assoc _ _ _
    _ = F.map X.iso.hom ≫ X.snd.iso.hom ≫ H.map f.snd.snd :=
          congrArg (F.map X.iso.hom ≫ ·) w₂
    _ = (F.map X.iso.hom ≫ X.snd.iso.hom) ≫ H.map f.snd.snd := (Category.assoc _ _ _).symm
    _ = (F.mapIso X.iso ≪≫ X.snd.iso).hom ≫ H.map f.snd.snd := rfl

/-- Backward pasting functor. -/
@[simps!]
noncomputable def pullbackCompBwd {A B C E : Type u}
    [Category.{v} A] [Category.{v} B] [Category.{v} C] [Category.{v} E]
    (F : B ⥤ A) (G : C ⥤ B) (H : E ⥤ A) :
    CategoricalPullback G (CategoricalPullback.π₁ F H) ⥤ CategoricalPullback (G ⋙ F) H where
  obj Q := ⟨Q.fst, Q.snd.snd, F.mapIso Q.iso ≪≫ Q.snd.iso⟩
  map f := ⟨f.fst, f.snd.snd, pullbackCompBwd_w F G H f⟩

/-- Unit for pasting equivalence. -/
noncomputable def pullbackCompUnit {A B C E : Type u}
    [Category.{v} A] [Category.{v} B] [Category.{v} C] [Category.{v} E]
    (F : B ⥤ A) (G : C ⥤ B) (H : E ⥤ A) :
    𝟭 (CategoricalPullback (G ⋙ F) H) ≅
      pullbackCompFwd F G H ⋙ pullbackCompBwd F G H :=
  NatIso.ofComponents
    (fun P => CategoricalPullback.mkIso (Iso.refl _) (Iso.refl _) (by
      change F.map (G.map (𝟙 P.fst)) ≫ F.map (𝟙 (G.obj P.fst)) ≫ P.iso.hom =
        P.iso.hom ≫ H.map (𝟙 P.snd)
      simp only [Functor.map_id, Category.id_comp, Category.comp_id]))
    (fun {P Q} f => by
      refine CategoricalPullback.hom_ext ?_ ?_
      · change f.fst ≫ 𝟙 _ = 𝟙 _ ≫ f.fst; simp
      · change f.snd ≫ 𝟙 _ = 𝟙 _ ≫ f.snd; simp)

/-- Counit for pasting equivalence. -/
noncomputable def pullbackCompCounit {A B C E : Type u}
    [Category.{v} A] [Category.{v} B] [Category.{v} C] [Category.{v} E]
    (F : B ⥤ A) (G : C ⥤ B) (H : E ⥤ A) :
    pullbackCompBwd F G H ⋙ pullbackCompFwd F G H ≅
      𝟭 (CategoricalPullback G (CategoricalPullback.π₁ F H)) :=
  NatIso.ofComponents
    (fun Q =>
      CategoricalPullback.mkIso (Iso.refl _)
        (CategoricalPullback.mkIso Q.iso (Iso.refl _) (by
          change F.map Q.iso.hom ≫ Q.snd.iso.hom =
            (F.map Q.iso.hom ≫ Q.snd.iso.hom) ≫ H.map (𝟙 _)
          simp))
        (by
          change G.map (𝟙 _) ≫ Q.iso.hom = 𝟙 _ ≫ Q.iso.hom
          simp))
    (fun {Q Q'} f => by
      refine CategoricalPullback.hom_ext ?_ ?_
      · change f.fst ≫ 𝟙 _ = 𝟙 _ ≫ f.fst; simp
      · refine CategoricalPullback.hom_ext ?_ ?_
        · change G.map f.fst ≫ Q'.iso.hom = Q.iso.hom ≫ f.snd.fst
          exact f.w
        · change f.snd.snd ≫ 𝟙 _ = 𝟙 _ ≫ f.snd.snd; simp)

/-- Pasting equivalence for composite base maps. -/
noncomputable def pullbackCompEquiv {A B C E : Type u}
    [Category.{v} A] [Category.{v} B] [Category.{v} C] [Category.{v} E]
    (F : B ⥤ A) (G : C ⥤ B) (H : E ⥤ A) :
    CategoricalPullback (G ⋙ F) H ≌
      CategoricalPullback G (CategoricalPullback.π₁ F H) :=
  CategoryTheory.Equivalence.mk
    (pullbackCompFwd F G H) (pullbackCompBwd F G H)
    (pullbackCompUnit F G H) (pullbackCompCounit F G H)

/-- Identity reindex: `(𝟙)^* A ≌ A`. -/
noncomputable def reindexIdIso {C : ObjCat.{uObj, uHom}} (A : Classifier C) :
    AxiomOpfibration.ReindexIdIso A where
  equiv := pullbackIdEquiv A.forget.toFunctor

/-- Composition reindex: `(G ≫ F)^* A ≌ G^*(F^* A)`. -/
noncomputable def reindexCompIso {B C D : ObjCat.{uObj, uHom}} (G : D ⟶ C) (F : C ⟶ B)
    (A : Classifier B) : AxiomOpfibration.ReindexCompIso G F A where
  equiv := pullbackCompEquiv F.toFunctor G.toFunctor A.forget.toFunctor

end NormalizedCategoryGraph.ForMathlib
