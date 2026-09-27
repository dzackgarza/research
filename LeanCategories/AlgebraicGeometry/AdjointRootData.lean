/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
module

public import LeanCategories.AlgebraicGeometry.DiagonalizableWeightData

/-!
# Roots from adjoint weight data

Definition-level realization of the definitional part of Humphreys
FC16-C06-U027.  The roots relative to a diagonalizable subgroup are the
nonzero weights of the restricted adjoint representation.  Coordinate data
for that restricted representation are supplied by the preceding
adjoint-representation layer; its rationality is result content.

The identification of the zero-weight space with the fixed Lie algebra and
the inclusion of the subgroup Lie algebra are also result content.
-/

@[expose] public noncomputable section

namespace LeanCategories.AlgebraicGeometry

universe u v

/-- The root space attached to a character, represented by the corresponding
weight space of supplied coordinate data for the restricted adjoint action. -/
noncomputable def adjointRootSpaceData
    {K : Type u} [Field K] [IsAlgClosed K]
    (D : AffineAlgebraicGroup K) (L : Type v)
    [AddCommGroup L] [Module K L]
    (adjointRestriction : RationalRepresentationCoordinateData D L)
    (a : GroupLike K (AffineAlgebraicGroup.coordinateHopfAlgebra D)) :
    Submodule K L :=
  characterWeightSpaceData D L adjointRestriction a

/-- The zero-weight space of the supplied restricted adjoint representation. -/
noncomputable def adjointZeroWeightSpaceData
    {K : Type u} [Field K] [IsAlgClosed K]
    (D : AffineAlgebraicGroup K) (L : Type v)
    [AddCommGroup L] [Module K L]
    (adjointRestriction : RationalRepresentationCoordinateData D L) :
    Submodule K L :=
  characterZeroWeightSpaceData D L adjointRestriction

/-- Humphreys' roots relative to a diagonalizable subgroup: the nontrivial
characters with nonzero restricted-adjoint weight space. -/
noncomputable def rootsRelativeToDiagonalizableSubgroupData
    {K : Type u} [Field K] [IsAlgClosed K]
    (D : AffineAlgebraicGroup K)
    (_isDiagonalizable : IsDiagonalizableGroupData D)
    (L : Type v) [AddCommGroup L] [Module K L]
    (adjointRestriction : RationalRepresentationCoordinateData D L) :
    Set (GroupLike K (AffineAlgebraicGroup.coordinateHopfAlgebra D)) :=
  characterWeightsData D L adjointRestriction

end LeanCategories.AlgebraicGeometry
