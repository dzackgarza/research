/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.StructuralMap
import NormalizedCategoryGraph.Registry.Entry

/-!
# Viability specimen — symbolic specification

Exercises: foundations, magma tower, two-operation rings, parameterized modules,
remote Finite, implicit Rings.Graded.Finite, opaque host, alias CRings.
-/

namespace NormalizedCategoryGraph.Specimen

open NormalizedCategoryGraph

/-! ## Classifier hosts -/

def specimenHosts : ClassifierHostTable where
  hostOf
    | ⟨"clf.sets.finite"⟩ | ⟨"clf.sets.graded"⟩ | ⟨"clf.sets.binary_operation"⟩ =>
        some CategoryId.sets
    | ⟨"clf.magmas.associative"⟩ | ⟨"clf.magmas.commutative"⟩
    | ⟨"clf.magmas.unital"⟩ | ⟨"clf.magmas.inverse"⟩
    | ⟨"clf.magmas.additive"⟩ | ⟨"clf.magmas.multiplicative"⟩ =>
        some CategoryId.magmas
    | ⟨"clf.magmaswithtwooperations.distributive"⟩ =>
        some CategoryId.magmasWithTwoOperations
    | ⟨"clf.rings.division"⟩ =>
        some CategoryId.rings
    | ⟨"clf.modules_r.free"⟩ | ⟨"clf.modules_r.finitely_generated"⟩
    | ⟨"clf.modules_r.finite_rank"⟩ =>
        some CategoryId.modulesR
    | _ => none

def specimenAliases : AliasTable where
  canonicalOf
    | ⟨"cat.crings"⟩ => some CategoryId.commutativeRings
    | _ => none

/-! ## Named expressions (canonical bodies) -/

def exprSets : CategoryExpr := .atom CategoryId.sets
def exprMagmas : CategoryExpr := .classifierTotal ClassifierId.setsBinaryOperation
def exprSemigroups : CategoryExpr :=
  .refine exprMagmas ClassifierId.magmasAssociative none
def exprMonoids : CategoryExpr :=
  .refine exprSemigroups ClassifierId.magmasUnital none
def exprGroups : CategoryExpr :=
  .refine exprMonoids ClassifierId.magmasInverse none
/-- Magmas.Additive (one-tower role). -/
def exprAdditiveMagmas : CategoryExpr :=
  .refine exprMagmas ClassifierId.magmasAdditive none
def exprAdditiveSemigroups : CategoryExpr :=
  .refine exprAdditiveMagmas ClassifierId.magmasAssociative (some RouteId.additive)
def exprAdditiveMonoids : CategoryExpr :=
  .refine exprAdditiveSemigroups ClassifierId.magmasUnital (some RouteId.additive)
def exprAdditiveGroups : CategoryExpr :=
  .refine exprAdditiveMonoids ClassifierId.magmasInverse (some RouteId.additive)
def exprMagmasWithTwoOperations : CategoryExpr :=
  .opaque CategoryId.magmasWithTwoOperations
/-- Rings as the refined two-operation tower (not the unrefined host). -/
def exprRings : CategoryExpr :=
  let m2o := exprMagmasWithTwoOperations
  let addAssoc := .refine m2o ClassifierId.magmasAssociative (some RouteId.additive)
  let addComm := .refine addAssoc ClassifierId.magmasCommutative (some RouteId.additive)
  let addUnital := .refine addComm ClassifierId.magmasUnital (some RouteId.additive)
  let addInv := .refine addUnital ClassifierId.magmasInverse (some RouteId.additive)
  let mulAssoc := .refine addInv ClassifierId.magmasAssociative (some RouteId.multiplicative)
  let dist := .refine mulAssoc ClassifierId.m2oDistributive none
  .refine dist ClassifierId.magmasUnital (some RouteId.multiplicative)
def exprCommRings : CategoryExpr :=
  .refine (.atom CategoryId.rings) ClassifierId.magmasCommutative (some RouteId.multiplicative)
/-- DivisionRings := Rings.Division (not Magmas.Inverse). -/
def exprDivisionRings : CategoryExpr :=
  .refine (.atom CategoryId.rings) ClassifierId.ringsDivision none
def exprModules : CategoryExpr := .atom CategoryId.modulesR
def exprFreeModules : CategoryExpr :=
  .refine exprModules ClassifierId.modulesFree none
def exprFinitelyGeneratedModules : CategoryExpr :=
  .refine exprModules ClassifierId.modulesFinitelyGenerated none
def exprFiniteRankModules : CategoryExpr :=
  .refine exprModules ClassifierId.modulesFiniteRank none
def exprFiniteFreeModules : CategoryExpr :=
  .refine exprFreeModules ClassifierId.setsFinite none
/-- Family application `Modules(R)` (args symbolic until interpreted). -/
def exprModulesFamily : CategoryExpr :=
  .familyApp CategoryFamilyId.modules #[]
/-- Implicit unnamed target: constructible, not a named registry node. -/
def exprRingsGradedFinite : CategoryExpr :=
  .refine
    (.refine (.atom CategoryId.rings) ClassifierId.setsGraded none)
    ClassifierId.setsFinite none

def specimenNamed : NamedExpressionTable where
  bodyOf
    | ⟨"cat.sets"⟩ => some exprSets
    | ⟨"cat.magmas"⟩ => some exprMagmas
    | ⟨"cat.semigroups"⟩ => some exprSemigroups
    | ⟨"cat.monoids"⟩ => some exprMonoids
    | ⟨"cat.groups"⟩ => some exprGroups
    | ⟨"cat.additive_magmas"⟩ => some exprAdditiveMagmas
    | ⟨"cat.additive_semigroups"⟩ => some exprAdditiveSemigroups
    | ⟨"cat.additive_monoids"⟩ => some exprAdditiveMonoids
    | ⟨"cat.additive_groups"⟩ => some exprAdditiveGroups
    | ⟨"cat.rings"⟩ => some exprRings
    | ⟨"cat.commutative_rings"⟩ => some exprCommRings
    | ⟨"cat.division_rings"⟩ => some exprDivisionRings
    | ⟨"cat.modules_r"⟩ => some exprModules
    | ⟨"cat.free_modules_r"⟩ => some exprFreeModules
    | ⟨"cat.finitely_generated_modules_r"⟩ => some exprFinitelyGeneratedModules
    | ⟨"cat.finite_rank_modules_r"⟩ => some exprFiniteRankModules
    | ⟨"cat.finite_free_modules_r"⟩ => some exprFiniteFreeModules
    | ⟨"cat.magmaswithtwooperations"⟩ => some exprMagmasWithTwoOperations
    | ⟨"cat.crystals"⟩ => some (.opaque CategoryId.crystals)
    | _ => none

def specimenOpaquePorts : OpaquePortTable where
  port
    | ⟨"cat.magmaswithtwooperations"⟩, ⟨"cat.magmas"⟩, .port ⟨"port.multiplicative"⟩ =>
        some ⟨"oport.m2o.multiplicative"⟩
    | ⟨"cat.magmaswithtwooperations"⟩, ⟨"cat.magmas"⟩, .port ⟨"port.additive"⟩ =>
        some ⟨"oport.m2o.additive"⟩
    | ⟨"cat.magmaswithtwooperations"⟩, ⟨"cat.magmas"⟩, .route ⟨"route.multiplicative"⟩ =>
        some ⟨"oport.m2o.multiplicative"⟩
    | ⟨"cat.magmaswithtwooperations"⟩, ⟨"cat.magmas"⟩, .route ⟨"route.additive"⟩ =>
        some ⟨"oport.m2o.additive"⟩
    | ⟨"cat.modules_r"⟩, ⟨"cat.sets"⟩, _ =>
        some ⟨"oport.modules.sets"⟩
    | ⟨"cat.crystals"⟩, ⟨"cat.sets"⟩, _ =>
        some ⟨"oport.crystals.sets"⟩
    | _, _, _ => none

def specimenCtx : ProjectionContext where
  hosts := specimenHosts
  aliases := specimenAliases
  named := specimenNamed
  opaquePorts := specimenOpaquePorts
  refinementId := fun base clf route =>
    let r := match route with
      | some rid => rid.raw
      | none => "default"
    ⟨s!"ref.{toString (repr base)}.{clf.raw}.{r}"⟩

/-! ## Normalization / alias checks (`partial` ⇒ `native_decide`) -/

example :
    specimenAliases.canonicalize ⟨"cat.crings"⟩ = CategoryId.commutativeRings := by
  native_decide

example :
    isIdentityEdge ⟨"cat.crings"⟩ CategoryId.commutativeRings specimenAliases = true := by
  native_decide

example :
    isIdentityEdge CategoryId.commutativeRings CategoryId.commutativeRings specimenAliases =
      true := by
  native_decide

/-! ## Projection checks -/

example :
    (project specimenCtx exprGroups exprMagmas .none).isSome = true := by
  native_decide

example :
    (project specimenCtx exprFiniteFreeModules exprSets .none).isSome = true := by
  native_decide

/-- Opaque two-operation host → Magmas along the multiplicative port.
Target is the named atom `cat.magmas` (not the classifier-total body). -/
example :
    (project specimenCtx exprMagmasWithTwoOperations (.atom CategoryId.magmas)
      (.route RouteId.multiplicative)).isSome = true := by
  native_decide

example :
    (project specimenCtx exprRingsGradedFinite (.atom CategoryId.rings) .none).isSome =
      true := by
  native_decide

/-! ## Registry snapshot (canonical CommRings; no CRings node) -/

def specimenSnapshot : RegistrySnapshot where
  schemaVersion := "0.1.0-specimen"
  categories := #[
    { id := CategoryId.sets, canonicalName := "Sets"
      declaration := "NormalizedCategoryGraph.Specimen.exprSets"
      expression := exprSets, origin := .root, visibility := .present },
    { id := CategoryId.magmas, canonicalName := "Magmas"
      declaration := "NormalizedCategoryGraph.Specimen.exprMagmas"
      expression := exprMagmas, origin := .atomicClassifierTotal, visibility := .present },
    { id := CategoryId.semigroups, canonicalName := "Semigroups"
      declaration := "NormalizedCategoryGraph.Specimen.exprSemigroups"
      expression := exprSemigroups, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.monoids, canonicalName := "Monoids"
      declaration := "NormalizedCategoryGraph.Specimen.exprMonoids"
      expression := exprMonoids, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.groups, canonicalName := "Groups"
      declaration := "NormalizedCategoryGraph.Specimen.exprGroups"
      expression := exprGroups, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.additiveMagmas, canonicalName := "AdditiveMagmas"
      declaration := "NormalizedCategoryGraph.Specimen.exprAdditiveMagmas"
      expression := exprAdditiveMagmas, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.additiveSemigroups, canonicalName := "AdditiveSemigroups"
      declaration := "NormalizedCategoryGraph.Specimen.exprAdditiveSemigroups"
      expression := exprAdditiveSemigroups, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.additiveMonoids, canonicalName := "AdditiveMonoids"
      declaration := "NormalizedCategoryGraph.Specimen.exprAdditiveMonoids"
      expression := exprAdditiveMonoids, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.additiveGroups, canonicalName := "AdditiveGroups"
      declaration := "NormalizedCategoryGraph.Specimen.exprAdditiveGroups"
      expression := exprAdditiveGroups, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.rings, canonicalName := "Rings"
      declaration := "NormalizedCategoryGraph.Specimen.exprRings"
      expression := exprRings, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.commutativeRings, canonicalName := "CommutativeRings"
      declaration := "NormalizedCategoryGraph.Specimen.exprCommRings"
      expression := exprCommRings, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.divisionRings, canonicalName := "DivisionRings"
      declaration := "NormalizedCategoryGraph.Specimen.exprDivisionRings"
      expression := exprDivisionRings, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.modulesR, canonicalName := "Modules(R)"
      declaration := "NormalizedCategoryGraph.Specimen.exprModules"
      expression := exprModules, origin := .root, visibility := .present },
    { id := ⟨"cat.finitely_generated_modules_r"⟩, canonicalName := "FinitelyGeneratedModules(R)"
      declaration := "NormalizedCategoryGraph.Specimen.exprFinitelyGeneratedModules"
      expression := exprFinitelyGeneratedModules, origin := .derivedNamed, visibility := .present },
    { id := ⟨"cat.finite_rank_modules_r"⟩, canonicalName := "FiniteRankModules(R)"
      declaration := "NormalizedCategoryGraph.Specimen.exprFiniteRankModules"
      expression := exprFiniteRankModules, origin := .derivedNamed, visibility := .present },
    { id := ⟨"cat.finite_free_modules_r"⟩, canonicalName := "FiniteFreeModules(R)"
      declaration := "NormalizedCategoryGraph.Specimen.exprFiniteFreeModules"
      expression := exprFiniteFreeModules, origin := .derivedNamed, visibility := .present },
    { id := CategoryId.magmasWithTwoOperations, canonicalName := "MagmasWithTwoOperations"
      declaration := "NormalizedCategoryGraph.Specimen.exprMagmasWithTwoOperations"
      expression := exprMagmasWithTwoOperations
      origin := .opaqueCategory, visibility := .semanticOnly },
    { id := CategoryId.crystals, canonicalName := "Crystals"
      declaration := "NormalizedCategoryGraph.Specimen.Crystals"
      expression := .opaque CategoryId.crystals
      origin := .opaqueCategory, visibility := .semanticOnly }
  ]
  classifiers := #[
    { id := ClassifierId.setsFinite, canonicalName := "Finite"
      declaration := "", hostId := CategoryId.sets, visibility := .present },
    { id := ClassifierId.setsGraded, canonicalName := "Graded"
      declaration := "", hostId := CategoryId.sets, visibility := .present },
    { id := ClassifierId.setsBinaryOperation, canonicalName := "BinaryOperation"
      declaration := "", hostId := CategoryId.sets, visibility := .present },
    { id := ClassifierId.magmasAssociative, canonicalName := "Associative"
      declaration := "", hostId := CategoryId.magmas, visibility := .present },
    { id := ClassifierId.magmasCommutative, canonicalName := "Commutative"
      declaration := "", hostId := CategoryId.magmas, visibility := .present },
    { id := ClassifierId.magmasUnital, canonicalName := "Unital"
      declaration := "", hostId := CategoryId.magmas, visibility := .present },
    { id := ClassifierId.magmasInverse, canonicalName := "Inverse"
      declaration := "", hostId := CategoryId.magmas, visibility := .present },
    { id := ClassifierId.magmasAdditive, canonicalName := "Additive"
      declaration := "", hostId := CategoryId.magmas, visibility := .present },
    { id := ClassifierId.magmasMultiplicative, canonicalName := "Multiplicative"
      declaration := "", hostId := CategoryId.magmas, visibility := .present },
    { id := ClassifierId.modulesFree, canonicalName := "Free"
      declaration := "", hostId := CategoryId.modulesR, visibility := .present },
    { id := ClassifierId.modulesFinitelyGenerated, canonicalName := "FinitelyGenerated"
      declaration := "", hostId := CategoryId.modulesR, visibility := .present },
    { id := ClassifierId.modulesFiniteRank, canonicalName := "FiniteRank"
      declaration := "", hostId := CategoryId.modulesR, visibility := .present },
    { id := ClassifierId.m2oDistributive, canonicalName := "Distributive"
      declaration := "", hostId := CategoryId.magmasWithTwoOperations, visibility := .present },
    { id := ClassifierId.ringsDivision, canonicalName := "Division"
      declaration := "", hostId := CategoryId.rings, visibility := .present }
  ]
  aliases := #[
    { id := AliasId.crings, spelling := "CRings"
      aliasOf := CategoryId.commutativeRings
      declaration := "NormalizedCategoryGraph.Specimen.CRings" }
  ]
  opaqueCategories := #[
    { id := CategoryId.magmasWithTwoOperations
      declaration := ""
      ports := #[
        { id := ⟨"oport.m2o.multiplicative"⟩
          source := CategoryId.magmasWithTwoOperations
          target := CategoryId.magmas
          role := PortId.multiplicative
          declaration := ""
          provenance := "authored ledger opaque interface" },
        { id := ⟨"oport.m2o.additive"⟩
          source := CategoryId.magmasWithTwoOperations
          target := CategoryId.magmas
          role := PortId.additive
          declaration := ""
          provenance := "authored ledger opaque interface" }
      ]
      reason := "two-operation host (MagmasWithTwoOperations); distributivity is a separate classifier"
      visibility := .semanticOnly },
    { id := CategoryId.crystals
      declaration := ""
      ports := #[
        { id := ⟨"oport.crystals.sets"⟩
          source := CategoryId.crystals
          target := CategoryId.sets
          role := PortId.underlyingSet
          declaration := ""
          provenance := "authored ledger opaque interface" }
      ]
      reason := "exceptional combinatorial host (Crystal with Kashiwara operators)"
      visibility := .semanticOnly }
  ]
  equivalences := #[]

/-- Spelling convenience; registry records aliasOf, not a second category. -/
abbrev CRings := CategoryId.commutativeRings

example :
    (specimenSnapshot.categories.filter (·.id == CategoryId.commutativeRings)).size = 1 := by
  native_decide

example :
    (specimenSnapshot.categories.filter (·.canonicalName == "CRings")).size = 0 := by
  native_decide

example :
    (specimenSnapshot.categories.filter (·.visibility == .semanticOnly)).size = 2 := by
  native_decide

end NormalizedCategoryGraph.Specimen
