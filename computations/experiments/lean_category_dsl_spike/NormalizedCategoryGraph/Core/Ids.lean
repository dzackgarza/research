/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Stable identity types

Stable IDs are normalized mathematical identity (matching the Python semantic seed /
authored ledger). They never embed Lean universe metavariables.
-/

namespace NormalizedCategoryGraph

/-- Stable category id, e.g. `cat.sets`, `cat.commutative_rings`. -/
structure CategoryId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable classifier id, e.g. `clf.magmas.commutative`. -/
structure ClassifierId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable category-family id (parameterized constructors), e.g. `fam.modules`. -/
structure CategoryFamilyId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable identity of a ring parameter variable in a category-family expression. -/
structure RingParameterId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable constructor id, e.g. `ctor.hom_categories`. -/
structure ConstructorId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable functor id. -/
structure FunctorId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable structural port id, e.g. `port.multiplicative`. -/
structure PortId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable alias id, e.g. `alias.crings`. -/
structure AliasId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable route selector for multi-port refinements. -/
structure RouteId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable refinement occurrence id (for projection certificates). -/
structure RefinementId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable structural theorem id. -/
structure StructuralTheoremId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable opaque structural port id. -/
structure OpaquePortId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable cone / finite-limit certificate id. -/
structure ConeCertificateId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable coherence-witness id. -/
structure CoherenceId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable presentation-overlay id. -/
structure PresentationId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable cluster id for presentation overlay only. -/
structure ClusterId where
  raw : String
  deriving DecidableEq, Repr, Hashable

namespace CategoryId
def sets : CategoryId := ⟨"cat.sets"⟩
instance : Inhabited CategoryId := ⟨sets⟩
def magmas : CategoryId := ⟨"cat.magmas"⟩
/-- Semantic host for inverse laws; not a separately audited Sage public target. -/
def unitalMagmas : CategoryId := ⟨"cat.unital_magmas"⟩
def rings : CategoryId := ⟨"cat.rings"⟩
def commutativeRings : CategoryId := ⟨"cat.commutative_rings"⟩
def groups : CategoryId := ⟨"cat.groups"⟩
def semigroups : CategoryId := ⟨"cat.semigroups"⟩
def monoids : CategoryId := ⟨"cat.monoids"⟩
def modulesR : CategoryId := ⟨"cat.modules_r"⟩
def finitelyGeneratedModules : CategoryId := ⟨"cat.finitelygeneratedmodules"⟩
def finiteRankModules : CategoryId := ⟨"cat.finiterankmodules"⟩
def freeModules : CategoryId := ⟨"cat.freemodules"⟩
def magmasWithTwoOperations : CategoryId := ⟨"cat.magmaswithtwooperations"⟩
def crystals : CategoryId := ⟨"cat.crystals"⟩
/-- DivisionRings := Rings.Division. -/
def divisionRings : CategoryId := ⟨"cat.division_rings"⟩
end CategoryId

namespace ClassifierId
def setsFinite : ClassifierId := ⟨"clf.sets.finite"⟩
instance : Inhabited ClassifierId := ⟨setsFinite⟩
def setsGraded : ClassifierId := ⟨"clf.sets.graded"⟩
def setsBinaryOperation : ClassifierId := ⟨"clf.sets.binary_operation"⟩
def magmasAssociative : ClassifierId := ⟨"clf.magmas.associative"⟩
def magmasCommutative : ClassifierId := ⟨"clf.magmas.commutative"⟩
def magmasUnital : ClassifierId := ⟨"clf.magmas.unital"⟩
def magmasInverse : ClassifierId := ⟨"clf.magmas.inverse"⟩
/-- Magmas.Additive — operation role/presentation on Magmas (one-tower). -/
def magmasAdditive : ClassifierId := ⟨"clf.magmas.additive"⟩
/-- Magmas.Multiplicative — dual role when both ops are in play. -/
def magmasMultiplicative : ClassifierId := ⟨"clf.magmas.multiplicative"⟩
def modulesFree : ClassifierId := ⟨"clf.modules_free"⟩
def modulesFinitelyGenerated : ClassifierId := ⟨"clf.modules_finitelygenerated"⟩
/-- Finite rank — distinct from finitely generated. -/
def modulesFiniteRank : ClassifierId := ⟨"clf.modules_finiterank"⟩
def m2oDistributive : ClassifierId := ⟨"clf.magmaswithtwooperations.distributive"⟩
/-- Nonzero multiplicative invertibility on Rings — not Magmas.Inverse. -/
def ringsDivision : ClassifierId := ⟨"clf.division"⟩
end ClassifierId

namespace CategoryId
def additiveMagmas : CategoryId := ⟨"cat.additive_magmas"⟩
def additiveSemigroups : CategoryId := ⟨"cat.additive_semigroups"⟩
def additiveMonoids : CategoryId := ⟨"cat.additive_monoids"⟩
def additiveGroups : CategoryId := ⟨"cat.additive_groups"⟩
end CategoryId

namespace CategoryFamilyId
def modules : CategoryFamilyId := ⟨"fam.modules"⟩
instance : Inhabited CategoryFamilyId := ⟨modules⟩
end CategoryFamilyId

namespace RingParameterId
def r : RingParameterId := ⟨"R"⟩
instance : Inhabited RingParameterId := ⟨r⟩
end RingParameterId

namespace PortId
def additive : PortId := ⟨"port.additive"⟩
instance : Inhabited PortId := ⟨additive⟩
def multiplicative : PortId := ⟨"port.multiplicative"⟩
def underlyingSet : PortId := ⟨"port.underlying_set"⟩
end PortId

namespace RouteId
def multiplicative : RouteId := ⟨"route.multiplicative"⟩
instance : Inhabited RouteId := ⟨multiplicative⟩
def additive : RouteId := ⟨"route.additive"⟩
end RouteId

namespace AliasId
def crings : AliasId := ⟨"alias.crings"⟩
instance : Inhabited AliasId := ⟨crings⟩
end AliasId

namespace OpaquePortId
instance : Inhabited OpaquePortId := ⟨⟨""⟩⟩
end OpaquePortId

end NormalizedCategoryGraph
