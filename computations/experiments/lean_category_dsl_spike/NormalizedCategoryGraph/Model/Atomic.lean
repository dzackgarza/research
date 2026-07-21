/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.CategoricalPullback
import NormalizedCategoryGraph.Core.Expr
import NormalizedCategoryGraph.Core.Ids

/-!
# Atomic model (model-parametric semantics)

Semantic definitions typecheck for every `M : AtomicModel`. The Mathlib
instance is `Realization.Mathlib.atomicModel`.

`MagmasWithTwoOperations` is the shared-carrier two-operation host (pullback over
Sets). `Rings` is obtained by refining that host along additive group laws,
multiplicative monoid laws, and distributivity — it is never definitionally the
unrefined host.
-/

namespace NormalizedCategoryGraph

open CategoryTheory

universe uObj uHom

set_option linter.checkUnivs false

/-- Irreducible foundation atoms. -/
structure FoundationAtoms where
  Sets : ObjCat.{uObj, uHom}
  finite : Classifier Sets
  graded : Classifier Sets
  binaryOperation : Classifier Sets

/-- Algebra classifiers whose least host is Magmas. -/
structure AlgebraAtoms (F : FoundationAtoms.{uObj, uHom}) where
  associative : Classifier F.binaryOperation.total
  commutative : Classifier F.binaryOperation.total
  unital : Classifier F.binaryOperation.total
  inverse : Classifier F.binaryOperation.total
  /-- Operation-role Magmas.Additive (one-tower; not a second law family). -/
  additive : Classifier F.binaryOperation.total
  /-- Operation-role Magmas.Multiplicative. -/
  multiplicative : Classifier F.binaryOperation.total

/-- Module atoms: the genuinely parameterized family `R ↦ Modules(R)` and
classifiers on every fibre. -/
structure ModuleAtoms (F : FoundationAtoms.{uObj, uHom}) (_A : AlgebraAtoms F) where
  /-- Parameter category for the module family. -/
  RingObjects : ObjCat.{uObj, uHom}
  /-- The category `Modules(R)` for a base-ring object `R`. -/
  modules : RingObjects → ObjCat.{uObj, uHom}
  /-- Opposite-ring substitution for right-module families. -/
  oppositeRing : RingObjects → RingObjects
  free : (R : RingObjects) → Classifier (modules R)
  /-- Finitely generated modules — not finite rank. -/
  finitelyGenerated : (R : RingObjects) → Classifier (modules R)
  /-- Finite free rank (admits a finite basis). Distinct from finitely generated. -/
  finiteRank : (R : RingObjects) → Classifier (modules R)
  modulesToSets : (R : RingObjects) → modules R ⟶ F.Sets

/-- Exceptional hosts with typed ports. -/
structure ExceptionalAtoms (F : FoundationAtoms.{uObj, uHom}) where
  MagmasWithTwoOperations : ObjCat.{uObj, uHom}
  additivePort : MagmasWithTwoOperations ⟶ F.binaryOperation.total
  multiplicativePort : MagmasWithTwoOperations ⟶ F.binaryOperation.total
  /-- Distributivity of the multiplicative magma over the additive magma. -/
  distributive : Classifier MagmasWithTwoOperations
  /-- Division on the two-operation host (reindexed onto Rings). Not Magmas.Inverse. -/
  division : Classifier MagmasWithTwoOperations
  Crystals : ObjCat.{uObj, uHom}
  crystalsToSets : Crystals ⟶ F.Sets

/-- Full atomic model. -/
structure AtomicModel where
  foundations : FoundationAtoms.{uObj, uHom}
  algebra : AlgebraAtoms foundations
  modules : ModuleAtoms foundations algebra
  exceptional : ExceptionalAtoms foundations

namespace Normalized

variable (M : AtomicModel.{uObj, uHom})

def Sets : ObjCat.{uObj, uHom} := M.foundations.Sets

def Magmas : ObjCat.{uObj, uHom} := M.foundations.binaryOperation.total

def magmasToSets : Magmas M ⟶ Sets M :=
  M.foundations.binaryOperation.forget

/-- Semigroups := Magmas.Associative. -/
def Semigroups : ObjCat := M.algebra.associative.total

def semigroupsToMagmas : Semigroups M ⟶ Magmas M :=
  M.algebra.associative.forget

/-- Magmas.Additive — one-tower additive presentation (role classifier). -/
def AdditiveMagmas : ObjCat := M.algebra.additive.total

def additiveMagmasToMagmas : AdditiveMagmas M ⟶ Magmas M :=
  M.algebra.additive.forget

/-- Magmas.Multiplicative — dual role classifier. -/
def MultiplicativeMagmas : ObjCat := M.algebra.multiplicative.total

/-- Monoids := Semigroups.Unital via reindex of Unital along Semigroups → Magmas. -/
noncomputable def Monoids : ObjCat :=
  (Classifier.reindex (semigroupsToMagmas M) M.algebra.unital).total

noncomputable def monoidsToSemigroups : Monoids M ⟶ Semigroups M :=
  (Classifier.reindex (semigroupsToMagmas M) M.algebra.unital).baseProjection

/-- Groups := Monoids.Inverse. -/
noncomputable def Groups : ObjCat :=
  let monoidsToMagmas :=
    (Classifier.reindex (semigroupsToMagmas M) M.algebra.unital).baseProjection ≫
      semigroupsToMagmas M
  (Classifier.reindex monoidsToMagmas M.algebra.inverse).total

/-- Two-operation host (pullback Magmas ×_Sets Magmas). -/
def MagmasWithTwoOperations : ObjCat := M.exceptional.MagmasWithTwoOperations

def m2oToMagmasMul : MagmasWithTwoOperations M ⟶ Magmas M :=
  M.exceptional.multiplicativePort

def m2oToMagmasAdd : MagmasWithTwoOperations M ⟶ Magmas M :=
  M.exceptional.additivePort

/-! ### Rings tower

Schematically:

```
Rngs := MagmasWithTwoOperations
  .AdditiveAssociative.AdditiveCommutative.AdditiveUnital.AdditiveInverse
  .MultiplicativeAssociative.Distributive
Rings := Rngs.MultiplicativeUnital
```

each refinement a `Classifier.reindex` along the appropriate port.
-/

/-- Additive-associative two-operation objects. -/
noncomputable def M2O.AdditiveAssociative : ObjCat :=
  (Classifier.reindex (m2oToMagmasAdd M) M.algebra.associative).total

noncomputable def m2oAddAssocToM2O :
    M2O.AdditiveAssociative M ⟶ MagmasWithTwoOperations M :=
  (Classifier.reindex (m2oToMagmasAdd M) M.algebra.associative).baseProjection

/-- Then additive-commutative. -/
noncomputable def M2O.AdditiveCommutative : ObjCat :=
  let toMagmas := m2oAddAssocToM2O M ≫ m2oToMagmasAdd M
  (Classifier.reindex toMagmas M.algebra.commutative).total

noncomputable def m2oAddCommToAddAssoc :
    M2O.AdditiveCommutative M ⟶ M2O.AdditiveAssociative M :=
  let toMagmas := m2oAddAssocToM2O M ≫ m2oToMagmasAdd M
  (Classifier.reindex toMagmas M.algebra.commutative).baseProjection

/-- Then additive-unital. -/
noncomputable def M2O.AdditiveUnital : ObjCat :=
  let toMagmas :=
    m2oAddCommToAddAssoc M ≫ m2oAddAssocToM2O M ≫ m2oToMagmasAdd M
  (Classifier.reindex toMagmas M.algebra.unital).total

noncomputable def m2oAddUnitalToAddComm :
    M2O.AdditiveUnital M ⟶ M2O.AdditiveCommutative M :=
  let toMagmas :=
    m2oAddCommToAddAssoc M ≫ m2oAddAssocToM2O M ≫ m2oToMagmasAdd M
  (Classifier.reindex toMagmas M.algebra.unital).baseProjection

/-- Then additive-inverse (additive groups with a second magma). -/
noncomputable def M2O.AdditiveInverse : ObjCat :=
  let toMagmas :=
    m2oAddUnitalToAddComm M ≫
      m2oAddCommToAddAssoc M ≫ m2oAddAssocToM2O M ≫ m2oToMagmasAdd M
  (Classifier.reindex toMagmas M.algebra.inverse).total

noncomputable def m2oAddInvToAddUnital :
    M2O.AdditiveInverse M ⟶ M2O.AdditiveUnital M :=
  let toMagmas :=
    m2oAddUnitalToAddComm M ≫
      m2oAddCommToAddAssoc M ≫ m2oAddAssocToM2O M ≫ m2oToMagmasAdd M
  (Classifier.reindex toMagmas M.algebra.inverse).baseProjection

/-- Forget the additive tower back to M2O. -/
noncomputable def m2oAddInvToM2O :
    M2O.AdditiveInverse M ⟶ MagmasWithTwoOperations M :=
  m2oAddInvToAddUnital M ≫
    m2oAddUnitalToAddComm M ≫
      m2oAddCommToAddAssoc M ≫ m2oAddAssocToM2O M

/-- Then multiplicative-associative. -/
noncomputable def M2O.MultiplicativeAssociative : ObjCat :=
  let toMagmas := m2oAddInvToM2O M ≫ m2oToMagmasMul M
  (Classifier.reindex toMagmas M.algebra.associative).total

noncomputable def m2oMulAssocToAddInv :
    M2O.MultiplicativeAssociative M ⟶ M2O.AdditiveInverse M :=
  let toMagmas := m2oAddInvToM2O M ≫ m2oToMagmasMul M
  (Classifier.reindex toMagmas M.algebra.associative).baseProjection

/-- Then distributivity on the two-operation host (reindexed along the tower). -/
noncomputable def Rngs : ObjCat :=
  let toM2O := m2oMulAssocToAddInv M ≫ m2oAddInvToM2O M
  (Classifier.reindex toM2O M.exceptional.distributive).total

noncomputable def rngsToMulAssoc : Rngs M ⟶ M2O.MultiplicativeAssociative M :=
  let toM2O := m2oMulAssocToAddInv M ≫ m2oAddInvToM2O M
  (Classifier.reindex toM2O M.exceptional.distributive).baseProjection

/-- Rings := Rngs.MultiplicativeUnital. -/
noncomputable def Rings : ObjCat :=
  let toMagmas :=
    rngsToMulAssoc M ≫ m2oMulAssocToAddInv M ≫ m2oAddInvToM2O M ≫ m2oToMagmasMul M
  (Classifier.reindex toMagmas M.algebra.unital).total

noncomputable def ringsToRngs : Rings M ⟶ Rngs M :=
  let toMagmas :=
    rngsToMulAssoc M ≫ m2oMulAssocToAddInv M ≫ m2oAddInvToM2O M ≫ m2oToMagmasMul M
  (Classifier.reindex toMagmas M.algebra.unital).baseProjection

/-- Port Rings → Magmas along the multiplicative structure. -/
noncomputable def ringsToMagmasMul : Rings M ⟶ Magmas M :=
  ringsToRngs M ≫
    rngsToMulAssoc M ≫
      m2oMulAssocToAddInv M ≫ m2oAddInvToM2O M ≫ m2oToMagmasMul M

/-- Port Rings → Magmas along the additive structure. -/
noncomputable def ringsToMagmasAdd : Rings M ⟶ Magmas M :=
  ringsToRngs M ≫
    rngsToMulAssoc M ≫
      m2oMulAssocToAddInv M ≫ m2oAddInvToM2O M ≫ m2oToMagmasAdd M

/-- CommutativeRings := Rings.Commutative[via := multiplicative]. -/
noncomputable def CommutativeRings : ObjCat :=
  (Classifier.reindex (ringsToMagmasMul M) M.algebra.commutative).total

/-- DivisionRings := Rings.Division — reindex the division classifier along
Rings → MagmasWithTwoOperations. Not Magmas.Inverse. -/
noncomputable def DivisionRings : ObjCat :=
  let ringsToM2O := ringsToRngs M ≫ rngsToMulAssoc M ≫ m2oMulAssocToAddInv M ≫ m2oAddInvToM2O M
  (Classifier.reindex ringsToM2O M.exceptional.division).total

/-- The parameter category for `R ↦ Modules(R)`. -/
def ModuleRingObjects : ObjCat := M.modules.RingObjects

/-- The fibre `Modules(R)`. -/
def Modules (R : M.modules.RingObjects) : ObjCat := M.modules.modules R

/-- Interpret a typed parameter expression in an explicit variable environment. -/
def moduleParameter (resolve : RingParameterId → Option M.modules.RingObjects)
    (parameter : ParameterExpr) : Option M.modules.RingObjects :=
  match parameter with
  | .ringVariable id => resolve id
  | .opposite parameter => M.modules.oppositeRing <$> moduleParameter resolve parameter

def FreeModules (R : M.modules.RingObjects) : ObjCat := (M.modules.free R).total

/-- Finitely generated modules (not finite-rank). -/
def FinitelyGeneratedModules (R : M.modules.RingObjects) : ObjCat :=
  (M.modules.finitelyGenerated R).total

/-- Finite free rank modules (admits a finite basis). -/
def FiniteRankModules (R : M.modules.RingObjects) : ObjCat := (M.modules.finiteRank R).total

/-- Finite free modules: free modules with a finite basis index. -/
def FiniteFreeModules (R : M.modules.RingObjects) : ObjCat :=
  FiniteRankModules M R

end Normalized

end NormalizedCategoryGraph
