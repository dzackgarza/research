/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Specimen.Viability
import NormalizedCategoryGraph.Registry.Extension

/-!
# Register the viability specimen into the Lean environment

Each command is the authored registry declaration.  There is no parallel snapshot to
replay: importing this module elaborates, validates, and inserts each declaration into
`registryExt` once.
-/

open NormalizedCategoryGraph
open NormalizedCategoryGraph.Specimen

normalized_registry .category
  { id := CategoryId.sets, canonicalName := "Sets"
    declaration := `NormalizedCategoryGraph.Normalized.Sets
    expression := exprSets
    realization := some `NormalizedCategoryGraph.Specimen.specimenSetsRealization
    origin := .root, visibility := .present }

normalized_registry .category
  { id := CategoryId.magmas, canonicalName := "Magmas"
    declaration := `NormalizedCategoryGraph.Normalized.Magmas
    expression := exprMagmas
    realization := some `NormalizedCategoryGraph.Specimen.specimenMagmasRealization
    origin := .atomicClassifierTotal, visibility := .present }

normalized_registry .category
  { id := CategoryId.semigroups, canonicalName := "Semigroups"
    declaration := `NormalizedCategoryGraph.Normalized.Semigroups
    expression := exprSemigroups
    realization := some `NormalizedCategoryGraph.Specimen.specimenSemigroupsRealization
    origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.monoids, canonicalName := "Monoids"
    declaration := `NormalizedCategoryGraph.Normalized.Monoids
    expression := exprMonoids, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.groups, canonicalName := "Groups"
    declaration := `NormalizedCategoryGraph.Normalized.Groups
    expression := exprGroups, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.additiveMagmas, canonicalName := "AdditiveMagmas"
    declaration := `NormalizedCategoryGraph.Normalized.AdditiveMagmas
    expression := exprAdditiveMagmas, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.additiveSemigroups, canonicalName := "AdditiveSemigroups"
    declaration := `NormalizedCategoryGraph.Normalized.AdditiveSemigroups
    expression := exprAdditiveSemigroups, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.additiveMonoids, canonicalName := "AdditiveMonoids"
    declaration := `NormalizedCategoryGraph.Normalized.AdditiveMonoids
    expression := exprAdditiveMonoids, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.additiveGroups, canonicalName := "AdditiveGroups"
    declaration := `NormalizedCategoryGraph.Normalized.AdditiveGroups
    expression := exprAdditiveGroups, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.rings, canonicalName := "Rings"
    declaration := `NormalizedCategoryGraph.Normalized.Rings
    expression := exprRings, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.commutativeRings, canonicalName := "CommutativeRings"
    declaration := `NormalizedCategoryGraph.Normalized.CommutativeRings
    expression := exprCommRings, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.divisionRings, canonicalName := "DivisionRings"
    declaration := `NormalizedCategoryGraph.Normalized.DivisionRings
    expression := exprDivisionRings, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.modulesR, canonicalName := "Modules(R)"
    declaration := `NormalizedCategoryGraph.Normalized.Modules
    expression := exprModules, origin := .root, visibility := .present }

normalized_registry .category
  { id := CategoryId.finitelyGeneratedModules, canonicalName := "FinitelyGeneratedModules(R)"
    declaration := `NormalizedCategoryGraph.Normalized.FinitelyGeneratedModules
    expression := exprFinitelyGeneratedModules, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.finiteRankModules, canonicalName := "FiniteRankModules(R)"
    declaration := `NormalizedCategoryGraph.Normalized.FiniteRankModules
    expression := exprFiniteRankModules, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.freeModules, canonicalName := "FreeModules(R)"
    declaration := `NormalizedCategoryGraph.Normalized.FreeModules
    expression := exprFreeModules, origin := .derivedNamed, visibility := .present }

normalized_registry .category
  { id := CategoryId.magmasWithTwoOperations, canonicalName := "MagmasWithTwoOperations"
    declaration := `NormalizedCategoryGraph.Normalized.MagmasWithTwoOperations
    expression := exprMagmasWithTwoOperations
    realization := some `NormalizedCategoryGraph.Specimen.specimenMagmasWithTwoOperationsRealization
    origin := .opaqueCategory, visibility := .semanticOnly }

normalized_registry .category
  { id := CategoryId.crystals, canonicalName := "Crystals"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.Crystals
    expression := .opaque CategoryId.crystals
    origin := .opaqueCategory, visibility := .semanticOnly }

normalized_registry .categoryFamily
  { id := CategoryFamilyId.modules
    canonicalName := "Modules(R)"
    declaration := `NormalizedCategoryGraph.Normalized.Modules
    parameter := { name := "R", kind := .ringObject }
    fibreDeclaration := `NormalizedCategoryGraph.Normalized.Modules
    variance := .restrictionOfScalarsContravariant }

normalized_registry .classifier
  { id := ClassifierId.setsFinite, canonicalName := "Finite"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.finite
    hostId := CategoryId.sets, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.setsGraded, canonicalName := "Graded"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.graded
    hostId := CategoryId.sets, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.setsBinaryOperation, canonicalName := "BinaryOperation"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.binaryOperation
    hostId := CategoryId.sets, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.magmasAssociative, canonicalName := "Associative"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.associative
    hostId := CategoryId.magmas, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.magmasCommutative, canonicalName := "Commutative"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.commutative
    hostId := CategoryId.magmas, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.magmasUnital, canonicalName := "Unital"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.unital
    hostId := CategoryId.magmas, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.magmasInverse, canonicalName := "Inverse"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.inverse
    hostId := CategoryId.magmas, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.magmasAdditive, canonicalName := "Additive"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.additive
    hostId := CategoryId.magmas, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.magmasMultiplicative, canonicalName := "Multiplicative"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.multiplicative
    hostId := CategoryId.magmas, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.modulesFree, canonicalName := "Free"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.free
    hostId := CategoryId.modulesR, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.modulesFinitelyGenerated, canonicalName := "FinitelyGenerated"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.finitelyGenerated
    hostId := CategoryId.modulesR, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.modulesFiniteRank, canonicalName := "FiniteRank"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.finiteRank
    hostId := CategoryId.modulesR, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.m2oDistributive, canonicalName := "Distributive"
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.distributive
    hostId := CategoryId.magmasWithTwoOperations, visibility := .present }

normalized_registry .classifier
  { id := ClassifierId.ringsDivision, canonicalName := "Division"
    declaration := `NormalizedCategoryGraph.Normalized.divisionOnRings
    hostId := CategoryId.rings, visibility := .present }

normalized_registry .functor
  { id := ⟨"fun.sets.identity"⟩
    canonicalName := "id_Sets"
    source := exprSets
    target := exprSets
    declaration := `NormalizedCategoryGraph.Specimen.specimenSetsIdentity
    expression := exprSetsIdentity
    role := .generatedStructural
    admissibility := .generated
    port := none
    origin := "identity"
    coherenceClass := none
    preferredPresentation := false }

normalized_registry .alias
  { id := AliasId.crings, spelling := "CRings"
    aliasOf := CategoryId.commutativeRings
    declaration := `NormalizedCategoryGraph.Specimen.CRings }

normalized_registry .opaque
  { id := CategoryId.magmasWithTwoOperations
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.MagmasWithTwoOperations
    ports := #[
      { id := ⟨"oport.m2o.multiplicative"⟩
        source := CategoryId.magmasWithTwoOperations
        target := CategoryId.magmas
        role := PortId.multiplicative
        declaration := `NormalizedCategoryGraph.Realization.Mathlib.multiplicativePort
        provenance := "authored opaque interface" },
      { id := ⟨"oport.m2o.additive"⟩
        source := CategoryId.magmasWithTwoOperations
        target := CategoryId.magmas
        role := PortId.additive
        declaration := `NormalizedCategoryGraph.Realization.Mathlib.additivePort
        provenance := "authored opaque interface" }
    ]
    reason := "two-operation host; distributivity is a separate classifier"
    visibility := .semanticOnly }

normalized_registry .opaque
  { id := CategoryId.crystals
    declaration := `NormalizedCategoryGraph.Realization.Mathlib.Crystals
    ports := #[
      { id := ⟨"oport.crystals.sets"⟩
        source := CategoryId.crystals
        target := CategoryId.sets
        role := PortId.underlyingSet
        declaration := `NormalizedCategoryGraph.Realization.Mathlib.crystalsToSets
        provenance := "authored opaque interface" }
    ]
    reason := "exceptional combinatorial host"
    visibility := .semanticOnly }

/--
error: registry declaration NormalizedCategoryGraph.Specimen.exprSets must return ObjCat,
but returns CategoryExpr
-/
#guard_msgs in
normalized_registry .category
  { id := ⟨"cat.invalid.ast"⟩
    canonicalName := "InvalidAST"
    declaration := `NormalizedCategoryGraph.Specimen.exprSets
    expression := exprSets
    origin := .root
    visibility := .semanticOnly }
