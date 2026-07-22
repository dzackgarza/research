/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.CategoricalPullback
import NormalizedCategoryGraph.Core.Expr
import NormalizedCategoryGraph.Model.Atomic

/-!
# Interpretation — evaluate category expressions in an atomic model

Refinements are interpreted by `Classifier.reindex` (categorical pullback).
Magmas-hosted towers compose forgetfuls to `Magmas`; two-operation refinements
use the additive/multiplicative ports.
-/

namespace NormalizedCategoryGraph

open Normalized CategoryTheory

universe uObj uHom

/-- An interpreted functor between two concrete category objects. -/
structure EvaluatedFunctor (M : AtomicModel.{uObj, uHom}) where
  source : ObjCat.{uObj, uHom}
  target : ObjCat.{uObj, uHom}
  functor : source ⟶ target

/-- The two structural projections of an interpreted refinement. -/
structure EvaluatedRefinement (M : AtomicModel.{uObj, uHom}) where
  refined : ObjCat.{uObj, uHom}
  base : ObjCat.{uObj, uHom}
  classifierTotal : ObjCat.{uObj, uHom}
  baseProjection : refined ⟶ base
  classifierProjection : refined ⟶ classifierTotal

/--
Semantic bindings for declaration-backed structural maps.

The registry keeps stable IDs and elaborated declarations; an atomic model supplies
their actual functors.  This is deliberately a semantic boundary: a `Lean.Name`
cannot be reflected into a value of an arbitrary functor type at run time.
-/
structure FunctorSemantics (M : AtomicModel.{uObj, uHom}) where
  named : FunctorId → Option (EvaluatedFunctor M)
  refinement : RefinementId → Option (EvaluatedRefinement M)
  opaquePort : OpaquePortId → Option (EvaluatedFunctor M)
  theoremInclusion : StructuralTheoremId → Option (EvaluatedFunctor M)
  finiteLimitLift : ConeCertificateId → Option (EvaluatedFunctor M)
  constructorMap : ConstructorId → Option (EvaluatedFunctor M)

/-- The empty semantic environment evaluates only functors generated internally. -/
def FunctorSemantics.empty (M : AtomicModel.{uObj, uHom}) : FunctorSemantics M where
  named _ := none
  refinement _ := none
  opaquePort _ := none
  theoremInclusion _ := none
  finiteLimitLift _ := none
  constructorMap _ := none

/-- Form the category-level pullback when both functors have the chosen codomain. -/
noncomputable def EvaluatedFunctor.pullbackCategory (left right : EvaluatedFunctor M)
    (over : ObjCat.{uObj, uHom}) : Option (ObjCat.{uObj, uHom}) := by
  classical
  rcases left with ⟨leftSource, leftTarget, leftFunctor⟩
  rcases right with ⟨rightSource, rightTarget, rightFunctor⟩
  by_cases leftOver : leftTarget = over
  · subst over
    by_cases rightOver : rightTarget = leftTarget
    · subst rightTarget
      exact
        some
          (Cat.of
            (CategoryTheory.Limits.CategoricalPullback
              leftFunctor.toFunctor rightFunctor.toFunctor))
    · exact none
  · exact none

/-- Compose interpreted functors only after their concrete middle categories agree. -/
noncomputable def EvaluatedFunctor.compose (left right : EvaluatedFunctor M) :
    Option (EvaluatedFunctor M) := by
  classical
  rcases left with ⟨leftSource, leftTarget, leftFunctor⟩
  rcases right with ⟨rightSource, rightTarget, rightFunctor⟩
  by_cases middle : leftTarget = rightSource
  · subst rightSource
    exact some ⟨leftSource, rightTarget, leftFunctor ≫ rightFunctor⟩
  · exact none

/-- Interpret a named atom using the realization-authored table. -/
noncomputable def evalAtom (M : AtomicModel.{uObj, uHom}) (id : CategoryId) :
    Option (ObjCat.{uObj, uHom}) :=
  M.namedCategory id

/-- Magmas-hosted classifiers. -/
noncomputable def magmasClassifier (M : AtomicModel.{uObj, uHom}) (id : ClassifierId) :
    Option (Classifier (Magmas M)) :=
  if id == ClassifierId.magmasAssociative then some M.algebra.associative
  else if id == ClassifierId.magmasCommutative then some M.algebra.commutative
  else if id == ClassifierId.magmasUnital then some M.algebra.unital
  else if id == ClassifierId.magmasInverse then some M.algebra.inverse
  else if id == ClassifierId.magmasAdditive then some M.algebra.additive
  else if id == ClassifierId.magmasMultiplicative then some M.algebra.multiplicative
  else none

/-- Sets-hosted classifiers. -/
noncomputable def setsClassifier (M : AtomicModel.{uObj, uHom}) (id : ClassifierId) :
    Option (Classifier (Sets M)) :=
  if id == ClassifierId.setsFinite then some M.foundations.finite
  else if id == ClassifierId.setsGraded then some M.foundations.graded
  else if id == ClassifierId.setsBinaryOperation then some M.foundations.binaryOperation
  else none

/-- Modules-hosted classifiers. -/
noncomputable def modulesClassifier (M : AtomicModel.{uObj, uHom})
    (R : M.modules.RingObjects) (id : ClassifierId) : Option (Classifier (Modules M R)) :=
  if id == ClassifierId.modulesFree then some (M.modules.free R)
  else if id == ClassifierId.modulesFinitelyGenerated then some (M.modules.finitelyGenerated R)
  else if id == ClassifierId.modulesFiniteRank then some (M.modules.finiteRank R)
  else none

/-- M2O-hosted classifiers. -/
noncomputable def m2oClassifier (M : AtomicModel.{uObj, uHom}) (id : ClassifierId) :
    Option (Classifier (MagmasWithTwoOperations M)) :=
  if id == ClassifierId.m2oDistributive then some M.exceptional.distributive
  else if id == ClassifierId.ringsDivision then some M.exceptional.division
  else none

/-- A forgetful functor into `Magmas`, with its domain. -/
structure ForgetfulToMagmas (M : AtomicModel.{uObj, uHom}) where
  domain : ObjCat.{uObj, uHom}
  forget : domain ⟶ Magmas M

/-- A forgetful functor into `Modules`, with its domain. -/
structure ForgetfulToModules (M : AtomicModel.{uObj, uHom}) where
  ring : M.modules.RingObjects
  domain : ObjCat.{uObj, uHom}
  forget : domain ⟶ Modules M ring

/-- Forgetful for named Magmas-tower atoms. -/
noncomputable def forgetfulToMagmasAtom (M : AtomicModel.{uObj, uHom}) (id : CategoryId) :
    Option (ForgetfulToMagmas M) :=
  if id == CategoryId.magmas then
    some ⟨Magmas M, CategoryTheory.CategoryStruct.id (Magmas M)⟩
  else if id == CategoryId.additiveMagmas then
    some ⟨AdditiveMagmas M, additiveMagmasToMagmas M⟩
  else if id == CategoryId.semigroups then
    some ⟨Semigroups M, semigroupsToMagmas M⟩
  else if id == CategoryId.monoids then
    some
      ⟨Monoids M,
        (Classifier.reindex (semigroupsToMagmas M) M.algebra.unital).baseProjection ≫
          semigroupsToMagmas M⟩
  else if id == CategoryId.groups then
    let monoidsToMagmas :=
      (Classifier.reindex (semigroupsToMagmas M) M.algebra.unital).baseProjection ≫
        semigroupsToMagmas M
    some
      ⟨Groups M,
        (Classifier.reindex monoidsToMagmas M.algebra.inverse).baseProjection ≫
          monoidsToMagmas⟩
  else
    none

/-- Composite forgetful from a Magmas-hosted expression down to `Magmas`. -/
noncomputable def forgetfulToMagmas (M : AtomicModel.{uObj, uHom}) :
    CategoryExpr → Option (ForgetfulToMagmas M)
  | .atom id => forgetfulToMagmasAtom M id
  | .classifierTotal id =>
      if id == ClassifierId.setsBinaryOperation then
        some ⟨Magmas M, CategoryTheory.CategoryStruct.id (Magmas M)⟩
      else
        none
  | .reference id => forgetfulToMagmasAtom M id
  | .refine base clf _ =>
      match magmasClassifier M clf, forgetfulToMagmas M base with
      | some A, some Fbase =>
          let R := Classifier.reindex Fbase.forget A
          some ⟨R.total, R.baseProjection ≫ Fbase.forget⟩
      | _, _ => none
  | _ => none

/-- Forgetful from a Modules-family expression to its selected fibre. -/
noncomputable def forgetfulToModules (M : AtomicModel.{uObj, uHom})
    (resolveRing : RingParameterId → Option M.modules.RingObjects) :
    CategoryExpr → Option (ForgetfulToModules M)
  | .familyApp family args =>
      if family == CategoryFamilyId.modules && args.size == 1 then
        match args[0]? with
        | some parameter =>
            match moduleParameter M resolveRing parameter with
            | some R => some ⟨R, Modules M R, CategoryTheory.CategoryStruct.id (Modules M R)⟩
            | none => none
        | none => none
      else none
  | .refine base clf _ =>
      match forgetfulToModules M resolveRing base with
      | some Fbase =>
          match modulesClassifier M Fbase.ring clf with
          | some A =>
              let R := Classifier.reindex Fbase.forget A
              some ⟨Fbase.ring, R.total, R.baseProjection ≫ Fbase.forget⟩
          | none => none
      | none => none
  | _ => none

/-- A classifier together with the actual category and forgetful functor it denotes. -/
structure EvaluatedClassifier (M : AtomicModel.{uObj, uHom}) where
  host : ObjCat.{uObj, uHom}
  total : ObjCat.{uObj, uHom}
  forget : total ⟶ host

/--
Evaluate a classifier identifier to its categorical classifier object.

The host expression determines the ring fibre for module classifiers.  The remaining
classifier namespaces have a unique host in an atomic model.
-/
noncomputable def evalClassifier (M : AtomicModel.{uObj, uHom})
    (resolveRing : RingParameterId → Option M.modules.RingObjects)
    (host : CategoryExpr) (id : ClassifierId) : Option (EvaluatedClassifier M) :=
  if id == ClassifierId.ringsDivision then
    if host.syntacticEq (.atom CategoryId.rings) then
      let classifier := divisionOnRings M
      some ⟨Rings M, classifier.total, classifier.forget⟩
    else none
  else
    match magmasClassifier M id with
    | some classifier => some ⟨Magmas M, classifier.total, classifier.forget⟩
    | none =>
        match setsClassifier M id with
        | some classifier => some ⟨Sets M, classifier.total, classifier.forget⟩
        | none =>
            match m2oClassifier M id with
            | some classifier =>
                some ⟨MagmasWithTwoOperations M, classifier.total, classifier.forget⟩
            | none =>
                match forgetfulToModules M resolveRing host with
                | some evaluatedHost =>
                    match modulesClassifier M evaluatedHost.ring id with
                    | some classifier =>
                        some ⟨Modules M evaluatedHost.ring, classifier.total, classifier.forget⟩
                    | none => none
                | none => none

/-- Evaluate a category expression to an actual `ObjCat`. -/
noncomputable def evalCategory (M : AtomicModel.{uObj, uHom})
    (resolveRing : RingParameterId → Option M.modules.RingObjects)
    (semantics : FunctorSemantics M) :
    CategoryExpr → Option (ObjCat.{uObj, uHom})
  | .atom id => evalAtom M id
  | .opaque id => evalAtom M id
  | .reference id => evalAtom M id
  | .classifierTotal id =>
      if id == ClassifierId.ringsDivision then some (divisionOnRings M).total
      else
        match magmasClassifier M id with
        | some A => some A.total
        | none =>
            match setsClassifier M id with
            | some A => some A.total
            | none =>
                match m2oClassifier M id with
                | some A => some A.total
                | none => none
  | .refine base clf route =>
      match magmasClassifier M clf with
      | some A =>
          match forgetfulToMagmas M base with
          | some F => some (Classifier.reindex F.forget A).total
          | none =>
              match base with
              | .atom bid =>
                  if bid == CategoryId.magmasWithTwoOperations ∧
                      (route == some RouteId.additive ∨ route == none) then
                    some (Classifier.reindex (m2oToMagmasAdd M) A).total
                  else if bid == CategoryId.magmasWithTwoOperations ∧
                      route == some RouteId.multiplicative then
                    some (Classifier.reindex (m2oToMagmasMul M) A).total
                  else if bid == CategoryId.rings ∧
                      route == some RouteId.multiplicative then
                    some (Classifier.reindex (ringsToMagmasMul M) A).total
                  else if bid == CategoryId.rings ∧
                      route == some RouteId.additive then
                    some (Classifier.reindex (ringsToMagmasAdd M) A).total
                  else
                    none
              | _ => none
      | none =>
          match forgetfulToModules M resolveRing base with
          | some F =>
              match modulesClassifier M F.ring clf with
              | some A =>
                  some (Classifier.reindex F.forget A).total
              | none => none
          | none =>
              match setsClassifier M clf with
              | some A =>
                  match forgetfulToModules M resolveRing base with
                  | some Fm =>
                      some
                        (Classifier.reindex (Fm.forget ≫ M.modules.modulesToSets Fm.ring) A).total
                  | none =>
                      match base with
                      | .atom bid =>
                          if bid == CategoryId.magmas then
                            some (Classifier.reindex (magmasToSets M) A).total
                          else if bid == CategoryId.sets then
                            some
                              (Classifier.reindex
                                (CategoryTheory.CategoryStruct.id (Sets M)) A).total
                          else
                            none
                      | .classifierTotal cid =>
                          if cid == ClassifierId.setsBinaryOperation then
                            some (Classifier.reindex (magmasToSets M) A).total
                          else
                            none
                      | .refine .. =>
                          match forgetfulToMagmas M base with
                          | some Fmag =>
                              some
                                (Classifier.reindex (Fmag.forget ≫ magmasToSets M) A).total
                          | none => none
                      | _ => none
              | none =>
                  match m2oClassifier M clf with
                  | some A =>
                      match base with
                      | .atom bid =>
                          if bid == CategoryId.magmasWithTwoOperations then
                            some
                              (Classifier.reindex
                                (CategoryTheory.CategoryStruct.id
                                  (MagmasWithTwoOperations M))
                                A).total
                          else if bid == CategoryId.rings then
                            let ringsToM2O :=
                              ringsToRngs M ≫
                                rngsToMulAssoc M ≫
                                  m2oMulAssocToAddInv M ≫ m2oAddInvToM2O M
                            some (Classifier.reindex ringsToM2O A).total
                          else
                            none
                      | _ => none
                  | none => none
  | .familyApp family args =>
      match forgetfulToModules M resolveRing (.familyApp family args) with
      | some F => some F.domain
      | none => none
  | .pullback leftId rightId over =>
      match semantics.named leftId, semantics.named rightId,
          evalCategory M resolveRing semantics over with
      | some left, some right, some evaluatedOver => left.pullbackCategory right evaluatedOver
      | _, _, _ => none
  | .constructor _ _ => none

/-- Evaluate an expression that contains no declaration-backed functor references. -/
noncomputable def evalCategoryWithoutFunctors (M : AtomicModel.{uObj, uHom})
    (resolveRing : RingParameterId → Option M.modules.RingObjects) :
    CategoryExpr → Option (ObjCat.{uObj, uHom}) :=
  evalCategory M resolveRing (.empty M)

/-- Retain a semantic functor only when its concrete endpoints realize the indexed expressions. -/
noncomputable def validateFunctor (M : AtomicModel.{uObj, uHom})
    (resolveRing : RingParameterId → Option M.modules.RingObjects)
    (semantics : FunctorSemantics M) (source target : CategoryExpr)
    (candidate : Option (EvaluatedFunctor M)) : Option (EvaluatedFunctor M) := by
  classical
  rcases candidate with (_ | ⟨actualSource, actualTarget, map⟩)
  · exact none
  match evalCategory M resolveRing semantics source, evalCategory M resolveRing semantics target with
  | some expectedSource, some expectedTarget =>
      by_cases sourceMatch : actualSource = expectedSource
      · subst actualSource
        by_cases targetMatch : actualTarget = expectedTarget
        · subst actualTarget
          exact some ⟨expectedSource, expectedTarget, map⟩
        · exact none
      · exact none
  | _, _ => exact none

/-- Evaluate a typed functor expression using its actual semantic bindings. -/
noncomputable def evalFunctor (M : AtomicModel.{uObj, uHom})
    (resolveRing : RingParameterId → Option M.modules.RingObjects)
    (semantics : FunctorSemantics M) {source target : CategoryExpr} :
    FunctorExpr source target → Option (EvaluatedFunctor M)
  | .identity category =>
      match evalCategory M resolveRing semantics category with
      | some evaluated => some ⟨evaluated, evaluated, CategoryTheory.CategoryStruct.id evaluated⟩
      | none => none
  | .named id => validateFunctor M resolveRing semantics source target (semantics.named id)
  | .baseProjection (.mk refinementId _ _ _) =>
      validateFunctor M resolveRing semantics source target <|
        (semantics.refinement refinementId).map fun value =>
          ⟨value.refined, value.base, value.baseProjection⟩
  | .classifierProjection (.mk refinementId _ _ _) =>
      validateFunctor M resolveRing semantics source target <|
        (semantics.refinement refinementId).map fun value =>
          ⟨value.refined, value.classifierTotal, value.classifierProjection⟩
  | .opaquePort port => validateFunctor M resolveRing semantics source target (semantics.opaquePort port)
  | .theoremInclusion theoremId =>
      validateFunctor M resolveRing semantics source target (semantics.theoremInclusion theoremId)
  | .finiteLimitLift cone =>
      validateFunctor M resolveRing semantics source target (semantics.finiteLimitLift cone)
  | .constructorMap constructor =>
      validateFunctor M resolveRing semantics source target (semantics.constructorMap constructor)
  | .compose first second =>
      match evalFunctor M resolveRing semantics first, evalFunctor M resolveRing semantics second with
      | some evaluatedFirst, some evaluatedSecond =>
          validateFunctor M resolveRing semantics source target (evaluatedFirst.compose evaluatedSecond)
      | _, _ => none

/-- Evaluate a legacy structural-map expression through the same semantic bindings. -/
noncomputable def evalStructuralMap (M : AtomicModel.{uObj, uHom})
    (resolveRing : RingParameterId → Option M.modules.RingObjects)
    (semantics : FunctorSemantics M) : StructuralMapExpr → Option (EvaluatedFunctor M)
  | .identity category =>
      match evalCategory M resolveRing semantics category with
      | some evaluated => some ⟨evaluated, evaluated, CategoryTheory.CategoryStruct.id evaluated⟩
      | none => none
  | .baseProjection refinementId =>
      (semantics.refinement refinementId).map fun value =>
        ⟨value.refined, value.base, value.baseProjection⟩
  | .classifierProjection refinementId =>
      (semantics.refinement refinementId).map fun value =>
        ⟨value.refined, value.classifierTotal, value.classifierProjection⟩
  | .opaquePort port => semantics.opaquePort port
  | .thmInclusion theoremId => semantics.theoremInclusion theoremId
  | .finiteLimitLift cone => semantics.finiteLimitLift cone
  | .compose first second =>
      match evalStructuralMap M resolveRing semantics first,
          evalStructuralMap M resolveRing semantics second with
      | some evaluatedFirst, some evaluatedSecond => evaluatedFirst.compose evaluatedSecond
      | _, _ => none

/--
An elaborated category declaration together with an evaluated expression and their
categorical equivalence in a fixed semantic model.

Registry rows will cite declarations of this type rather than independently asserting
that a `Lean.Name` and a `CategoryExpr` describe the same category.
-/
structure CategoryRealization (M : AtomicModel.{uObj, uHom})
    (resolveRing : RingParameterId → Option M.modules.RingObjects)
    (semantics : FunctorSemantics M) (expression : CategoryExpr)
    (category : ObjCat.{uObj, uHom}) where
  evaluated : ObjCat.{uObj, uHom}
  evaluates : evalCategory M resolveRing semantics expression = some evaluated
  equivalence : evaluated ≌ category

/--
An elaborated classifier declaration together with its evaluated host, total category,
and forgetful functor.  The indexed expression rules out host metadata detached from the
actual classifier.
-/
structure ClassifierRealization (M : AtomicModel.{uObj, uHom})
    (resolveRing : RingParameterId → Option M.modules.RingObjects)
    (host : CategoryExpr) (identifier : ClassifierId)
    (classifier : EvaluatedClassifier M) : Prop where
  realizes : evalClassifier M resolveRing host identifier = some classifier

/--
An elaborated functor declaration whose concrete endpoints and map realize its typed
symbolic expression.
-/
structure FunctorRealization (M : AtomicModel.{uObj, uHom})
    (resolveRing : RingParameterId → Option M.modules.RingObjects)
    (semantics : FunctorSemantics M) {source target : CategoryExpr}
    (expression : FunctorExpr source target) (functor : EvaluatedFunctor M) : Prop where
  realizes : evalFunctor M resolveRing semantics expression = some functor

end NormalizedCategoryGraph
