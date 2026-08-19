# Binary Targets

Every entry maps a `.cpp` source file to the binary it compiles into.
All binaries are produced by the root `CMakeLists.txt` via the `add_polyhedral_binary()` function and placed in `${CMAKE_BINARY_DIR}/bin`, unless noted as **Makefile-only**.

## src_copos

| Binary | Source |
|---|---|
| `CP_CopositiveMin` | `src_copos/CP_CopositiveMin.cpp` |
| `CP_CopositiveListCone` | `src_copos/CP_CopositiveListCone.cpp` |
| `CP_TestCompletePositivity` | `src_copos/CP_TestCompletePositivity.cpp` |
| `CP_CopositiveKernelMin` | `src_copos/CP_CopositiveKernelMin.cpp` |
| `CP_CopositiveMaxNorm` | `src_copos/CP_CopositiveMaxNorm.cpp` |
| `CP_TestCopositivity` | `src_copos/CP_TestCopositivity.cpp` |
| `CP_TestStrictCopositivity` | `src_copos/CP_TestStrictCopositivity.cpp` |

## src_ctype

| Binary | Source |
|---|---|
| `CTYP_PrepareInitialFile` | `src_ctype/CTYP_PrepareInitialFile.cpp` |
| `CTYP_MPI_Enumeration_c` | `src_ctype/CTYP_MPI_Enumeration_c.cpp` |
| `CTYP_ComputeInvariant` | `src_ctype/CTYP_ComputeInvariant.cpp` |
| `CTYP_PrepareAdjacencyFile` | `src_ctype/CTYP_PrepareAdjacencyFile.cpp` |
| `CTYP_MPI_EnumerationAdjacencies` | `src_ctype/CTYP_MPI_EnumerationAdjacencies.cpp` |
| `CTYP_CheckAdjacency` | `src_ctype/CTYP_CheckAdjacency.cpp` |
| `CTYP_SearchMatrix` | `src_ctype/CTYP_SearchMatrix.cpp` |
| `CTYP_LookForNoFreeVector` | `src_ctype/CTYP_LookForNoFreeVector.cpp` |
| `CTYP_MPI_AdjScheme` | `src_ctype/CTYP_MPI_AdjScheme.cpp` |
| `CTYP_ComputeHashStat` | `src_ctype/CTYP_ComputeHashStat.cpp` |
| `CTYP_ComputeInvariant_B` | `src_ctype/CTYP_ComputeInvariant_B.cpp` |
| `NC_ComputeAverage` | `src_ctype/NC_ComputeAverage.cpp` |

## src_delaunay

| Binary | Source |
|---|---|
| `LATT_FindOneVertex` | `src_delaunay/LATT_FindOneVertex.cpp` |
| `LATT_MPI_Lattice_IsoDelaunayDomain` | `src_delaunay/LATT_MPI_Lattice_IsoDelaunayDomain.cpp` |
| `LATT_SerialLattice_IsoDelaunayDomain` | `src_delaunay/LATT_SerialLattice_IsoDelaunayDomain.cpp` |
| `LATT_MPI_ComputeDelaunay` | `src_delaunay/LATT_MPI_ComputeDelaunay.cpp` |
| `LATT_SerialComputeDelaunay` | `src_delaunay/LATT_SerialComputeDelaunay.cpp` |

## src_dualdesc

| Binary | Source |
|---|---|
| `POLY_CheckCanonicalGAP` | `src_dualdesc/POLY_CheckCanonicalGAP.cpp` |
| `POLY_SerialDualDesc` | `src_dualdesc/POLY_SerialDualDesc.cpp` |
| `POLY_MPI_DualDesc` | `src_dualdesc/POLY_MPI_DualDesc.cpp` |
| `POLY_RunTheBank` | `src_dualdesc/POLY_RunTheBank.cpp` |
| `POLY_DatabaseRestructuration` | `src_dualdesc/POLY_DatabaseRestructuration.cpp` |
| `POLY_FindNeededBalinski` | `src_dualdesc/POLY_FindNeededBalinski.cpp` |
| `POLY_EvaluateDualDesc` | `src_dualdesc/POLY_EvaluateDualDesc.cpp` |
| `POLY_ReadPartialEnum` | `src_dualdesc/POLY_ReadPartialEnum.cpp` |
| `Read_MPI_sizes` | `src_dualdesc/Read_MPI_sizes.cpp` |
| `POLY_UpgradeDatabase` | `src_dualdesc/POLY_UpgradeDatabase.cpp` |
| `POLY_EvaluateBalinski` | `src_dualdesc/POLY_EvaluateBalinski.cpp` |
| `POLY_sampling_facets` | `src_dualdesc/POLY_sampling_facets.cpp` |
| `POLY_DirectSerialDualDesc` | `src_dualdesc/POLY_DirectSerialDualDesc.cpp` |

## src_group

| Binary | Source |
|---|---|
| `TEST_WeightMatrixLimited` | `src_group/TEST_WeightMatrixLimited.cpp` |
| `GRP_OrbitSplitting` | `src_group/GRP_OrbitSplitting.cpp` |
| `GRP_VectorSplitting` | `src_group/GRP_VectorSplitting.cpp` |
| `GRP_LinearSpace_Equivalence` | `src_group/GRP_LinearSpace_Equivalence.cpp` |
| `GRP_LinearSpace_Stabilizer` | `src_group/GRP_LinearSpace_Stabilizer.cpp` |
| `GRP_LinearSpace_Stabilizer_RightCoset` | `src_group/GRP_LinearSpace_Stabilizer_RightCoset.cpp` |
| `GRP_ListMat_Vdiag_EXT_Automorphism` | `src_group/GRP_ListMat_Vdiag_EXT_Automorphism.cpp` |
| `GRP_ListMat_Vdiag_EXT_Isomorphism` | `src_group/GRP_ListMat_Vdiag_EXT_Isomorphism.cpp` |
| `GRP_ListMat_Vdiag_EXT_Invariant` | `src_group/GRP_ListMat_Vdiag_EXT_Invariant.cpp` |
| `GRP_LinPolytope_Automorphism` | `src_group/GRP_LinPolytope_Automorphism.cpp` |
| `GRP_LinPolytope_Isomorphism` | `src_group/GRP_LinPolytope_Isomorphism.cpp` |
| `GRP_LinPolytopeIntegral_Isomorphism` | `src_group/GRP_LinPolytopeIntegral_Isomorphism.cpp` |
| `GRP_LinPolytopeIntegral_Automorphism` | `src_group/GRP_LinPolytopeIntegral_Automorphism.cpp` |
| `GRP_LinPolytopeIntegral_Automorphism_RightCoset` | `src_group/GRP_LinPolytopeIntegral_Automorphism_RightCoset.cpp` |
| `GRP_LinPolytope_Canonic` | `src_group/GRP_LinPolytope_Canonic.cpp` |
| `GRP_LinPolytope_Invariant` | `src_group/GRP_LinPolytope_Invariant.cpp` |
| `GRP_RuntimeOrbitSplitting` | `src_group/GRP_RuntimeOrbitSplitting.cpp` |
| `GRP_OrbitSplittingPerfect` | `src_group/GRP_OrbitSplittingPerfect.cpp` |
| `GRP_MatrixGroupPermSimplification` | `src_group/GRP_MatrixGroupPermSimplification.cpp` |
| `GRP_LinPolytope_Automorphism_GramMat` | `src_group/GRP_LinPolytope_Automorphism_GramMat.cpp` |
| `GRP_LinPolytope_Isomorphism_GramMat` | `src_group/GRP_LinPolytope_Isomorphism_GramMat.cpp` |
| `GRP_IsomorphismReduction` | `src_group/GRP_IsomorphismReduction.cpp` |
| `GRP_GroupAverage_Matrix` | `src_group/GRP_GroupAverage_Matrix.cpp` |
| `GRP_GroupAverage_Vector` | `src_group/GRP_GroupAverage_Vector.cpp` |
| `GRP_LinearSpace_Stabilizer_DoubleCoset` | `src_group/GRP_LinearSpace_Stabilizer_DoubleCoset.cpp` |
| `GRP_LinPolytopeIntegral_Automorphism_DoubleCoset` | `src_group/GRP_LinPolytopeIntegral_Automorphism_DoubleCoset.cpp` |
| `GRP_LinPolytopeIntegral_Automorphism_DoubleCosetStabilizer` | `src_group/GRP_LinPolytopeIntegral_Automorphism_DoubleCosetStabilizer.cpp` |
| `GRP_MatrixGroupSimplification` | `src_group/GRP_MatrixGroupSimplification.cpp` |
| `GRP_MatrixGroupSimplificationOnline` | `src_group/GRP_MatrixGroupSimplificationOnline.cpp` |
| `GRP_MatrixGroupSimplificationOnlineOpt` | `src_group/GRP_MatrixGroupSimplificationOnlineOpt.cpp` |
| `GRP_TestFinitenessSimp` | `src_group/GRP_TestFinitenessSimp.cpp` | **Makefile-only** |

## src_indefinite

| Binary | Source |
|---|---|
| `INDEF_FORM_GetOrbit_IsotropicKplane` | `src_indefinite/INDEF_FORM_GetOrbit_IsotropicKplane.cpp` |
| `INDEF_ApproximateOrbitRepresentative` | `src_indefinite/INDEF_ApproximateOrbitRepresentative.cpp` |
| `INDEF_FORM_GetOrbitRepresentative` | `src_indefinite/INDEF_FORM_GetOrbitRepresentative.cpp` |
| `INDEF_FORM_TestEquivalence` | `src_indefinite/INDEF_FORM_TestEquivalence.cpp` |
| `INDEF_FORM_AutomorphismGroup` | `src_indefinite/INDEF_FORM_AutomorphismGroup.cpp` |
| `INDEF_FORM_TestEquivalenceVector` | `src_indefinite/INDEF_FORM_TestEquivalenceVector.cpp` |
| `INDEF_FORM_ApproxCanonicalForm` | `src_indefinite/INDEF_FORM_ApproxCanonicalForm.cpp` |
| `INDEF_FORM_InvariantIsotropicPlane` | `src_indefinite/INDEF_FORM_InvariantIsotropicPlane.cpp` |
| `INDEF_FORM_StabilizerIsotropicPlane` | `src_indefinite/INDEF_FORM_StabilizerIsotropicPlane.cpp` |

## src_isotropy

| Binary | Source |
|---|---|
| `LATT_IndefiniteLLL` | `src_isotropy/LATT_IndefiniteLLL.cpp` |
| `LATT_IndefiniteReduction` | `src_isotropy/LATT_IndefiniteReduction.cpp` |
| `LATT_LLLreduceBasis` | `src_isotropy/LATT_LLLreduceBasis.cpp` |
| `LATT_DetMinimization` | `src_isotropy/LATT_DetMinimization.cpp` |
| `LATT_FindIsotropic` | `src_isotropy/LATT_FindIsotropic.cpp` |
| `LATT_TestIsotropic` | `src_isotropy/LATT_TestIsotropic.cpp` |
| `LATT_FindPositiveVector` | `src_isotropy/LATT_FindPositiveVector.cpp` |
| `LATT_lll` | `src_isotropy/LATT_lll.cpp` |
| `CheckPositiveSemiDefinite` | `src_isotropy/CheckPositiveSemiDefinite.cpp` |
| `LATT_DiophantApprox` | `src_isotropy/LATT_DiophantApprox.cpp` |
| `VectFamily_Reduction` | `src_isotropy/VectFamily_Reduction.cpp` |

## src_latt

| Binary | Source |
|---|---|
| `LATT_Canonicalize` | `src_latt/LATT_Canonicalize.cpp` |
| `LATT_CanonicalizeMultiple` | `src_latt/LATT_CanonicalizeMultiple.cpp` |
| `LATT_CanonicalizeSymplectic` | `src_latt/LATT_CanonicalizeSymplectic.cpp` |
| `LATT_Automorphism` | `src_latt/LATT_Automorphism.cpp` |
| `LATT_Isomorphism` | `src_latt/LATT_Isomorphism.cpp` |
| `LATT_near` | `src_latt/LATT_near.cpp` |
| `LATT_GenerateCharacteristicVectorSet` | `src_latt/LATT_GenerateCharacteristicVectorSet.cpp` |
| `TSPACE_FileFormatConversion` | `src_latt/TSPACE_FileFormatConversion.cpp` |
| `TSPACE_Stabilizer` | `src_latt/TSPACE_Stabilizer.cpp` |
| `TSPACE_Equivalence` | `src_latt/TSPACE_Equivalence.cpp` |
| `TEST_EquiStabFamily` | `src_latt/TEST_EquiStabFamily.cpp` |
| `LATT_ComputeShortestOrbits` | `src_latt/LATT_ComputeShortestOrbits.cpp` |
| `GRP_TestFiniteness` | `src_latt/GRP_TestFiniteness.cpp` |
| `LATT_ResolveModAction` | `src_latt/LATT_ResolveModAction.cpp` |
| `LATT_ComputeGroupModAction` | `src_latt/LATT_ComputeGroupModAction.cpp` |
| `TSPACE_IntegralSaturation` | `src_latt/TSPACE_IntegralSaturation.cpp` | **Makefile-only** |

## src_lorentzian

| Binary | Source |
|---|---|
| `LORENTZ_FundDomain_AllcockEdgewalk` | `src_lorentzian/LORENTZ_FundDomain_AllcockEdgewalk.cpp` |
| `LORENTZ_FundDomain_AllcockEdgewalk_Isomorphism` | `src_lorentzian/LORENTZ_FundDomain_AllcockEdgewalk_Isomorphism.cpp` |
| `LORENTZ_FundDomain_Vinberg` | `src_lorentzian/LORENTZ_FundDomain_Vinberg.cpp` |
| `LORENTZ_TwoDimAnisotropic_Allcock` | `src_lorentzian/LORENTZ_TwoDimAnisotropic_Allcock.cpp` |
| `COXDYN_FindExtensions` | `src_lorentzian/COXDYN_FindExtensions.cpp` |
| `COXDYN_ComputeSymbol` | `src_lorentzian/COXDYN_ComputeSymbol.cpp` |
| `COXDYN_GetFacetOneDomain` | `src_lorentzian/COXDYN_GetFacetOneDomain.cpp` |
| `LORENTZ_ComputeStabilizer_Vertex` | `src_lorentzian/LORENTZ_ComputeStabilizer_Vertex.cpp` |
| `COXDYN_FindExtensionsCoxMat` | `src_lorentzian/COXDYN_FindExtensionsCoxMat.cpp` |
| `LATT_GetIntegralMatricesPossibleOrders` | `src_lorentzian/LATT_GetIntegralMatricesPossibleOrders.cpp` |
| `LORENTZ_PERF_Automorphism` | `src_lorentzian/LORENTZ_PERF_Automorphism.cpp` |
| `LORENTZ_PERF_Isomorphism` | `src_lorentzian/LORENTZ_PERF_Isomorphism.cpp` |
| `LORENTZ_MPI_PerfectLorentzian` | `src_lorentzian/LORENTZ_MPI_PerfectLorentzian.cpp` |
| `LORENTZ_ReflectiveEdgewalk` | `src_lorentzian/LORENTZ_ReflectiveEdgewalk.cpp` |

## src_perfect

| Binary | Source |
|---|---|
| `PERF_MPI_EnumeratePerfectCones` | `src_perfect/PERF_MPI_EnumeratePerfectCones.cpp` |
| `IsEutactic` | `src_perfect/IsEutactic.cpp` |
| `PERF_SerialPerfectComputation` | `src_perfect/PERF_SerialPerfectComputation.cpp` |
| `PERF_IsBoundedFace` | `src_perfect/PERF_IsBoundedFace.cpp` |

## src_poincare_polyhedron

| Binary | Source |
|---|---|
| `POINCARE_Initial_Computation` | `src_poincare_polyhedron/POINCARE_Initial_Computation.cpp` |

## src_poly

| Binary | Source |
|---|---|
| `POLY_CreateAffineBasis` | `src_poly/POLY_CreateAffineBasis.cpp` |
| `POLY_cdd_skeletons` | `src_poly/POLY_cdd_skeletons.cpp` |
| `POLY_SolutionMatNonnegativeComplete` | `src_poly/POLY_SolutionMatNonnegativeComplete.cpp` |
| `POLY_redundancy` | `src_poly/POLY_redundancy.cpp` |
| `POLY_redundancyGroup` | `src_poly/POLY_redundancyGroup.cpp` |
| `POLY_IntegralPoints` | `src_poly/POLY_IntegralPoints.cpp` |
| `POLY_SkelettonClarkson` | `src_poly/POLY_SkelettonClarkson.cpp` |
| `POLY_redundancyClarksonCddlib` | `src_poly/POLY_redundancyClarksonCddlib.cpp` | **Makefile-only** |
| `POLY_GapFindHyperplaneRegions` | `src_poly/POLY_GapFindHyperplaneRegions.cpp` | **Makefile-only** |
| `POLY_FaceLatticeGen` | `src_poly/POLY_FaceLatticeGen.cpp` |
| `VectFamily_ColumnReduction` | `src_poly/VectFamily_ColumnReduction.cpp` |
| `POLY_lrs` | `src_poly/POLY_lrs.cpp` |
| `POLY_SmallPolytope` | `src_poly/POLY_SmallPolytope.cpp` |
| `POLY_LinearDetermineByInequalities` | `src_poly/POLY_LinearDetermineByInequalities.cpp` |
| `POLY_IsPointedCone` | `src_poly/POLY_IsPointedCone.cpp` |
| `POLY_DirectFaceLattice` | `src_poly/POLY_DirectFaceLattice.cpp` |
| `POLY_SolutionMatNonnegative` | `src_poly/POLY_SolutionMatNonnegative.cpp` |
| `POLY_cdd_LinearProgramming` | `src_poly/POLY_cdd_LinearProgramming.cpp` |
| `POLY_dual_description` | `src_poly/POLY_dual_description.cpp` |
| `POLY_dual_description_group` | `src_poly/POLY_dual_description_group.cpp` |
| `POLY_GetFullRankFacetSet` | `src_poly/POLY_GetFullRankFacetSet.cpp` |
| `POLY_GeometricallyUniqueInteriorPoint` | `src_poly/POLY_GeometricallyUniqueInteriorPoint.cpp` |
| `POLY_lrs_volume` | `src_poly/POLY_lrs_volume.cpp` |
| `POLY_lrs_triangulation` | `src_poly/POLY_lrs_triangulation.cpp` |
| `POLY_TwoLaminations` | `src_poly/POLY_TwoLaminations.cpp` |
| `POLY_lrs_triang_facets` | `src_poly/POLY_lrs_triang_facets.cpp` |

## src_polydecomp

| Binary | Source |
|---|---|
| `DEC_ComputeDecomposition` | `src_polydecomp/DEC_ComputeDecomposition.cpp` |
| `DEC_TestUnionCones` | `src_polydecomp/DEC_TestUnionCones.cpp` |
| `DEC_TestIntersectionMethods` | `src_polydecomp/DEC_TestIntersectionMethods.cpp` |

## src_polygen

| Binary | Source |
|---|---|
| `PolyGen_Difference` | `src_polygen/PolyGen_Difference.cpp` |

## src_rankin

| Binary | Source |
|---|---|
| `RANKIN_Compute_k_min` | `src_rankin/RANKIN_Compute_k_min.cpp` |

## src__covering

| Binary | Source |
|---|---|
| `_RandomEstimation` | `src_robust_covering/Robust_RandomEstimation.cpp` |
| `_InitialVoronoiData` | `src_robust_covering/Robust_InitialVoronoiData.cpp` |
| `_ExactRobustCoveringDensity` | `src_robust_covering/Robust_ExactRobustCoveringDensity.cpp` |
| `_RandomVertexEstimation` | `src_robust_covering/Robust_RandomVertexEstimation.cpp` | **Makefile-only** |

## src_short

| Binary | Source |
|---|---|
| `SHORT_EnumerateCyclicCases` | `src_short/SHORT_EnumerateCyclicCases.cpp` |
| `SHORT_GetShortestVector` | `src_short/SHORT_GetShortestVector.cpp` |
| `SHORT_CheckPrimeRealizability` | `src_short/SHORT_CheckPrimeRealizability.cpp` |
| `SHORT_TestRealizability` | `src_short/SHORT_TestRealizability.cpp` |
| `SHORT_ReduceVectorFamilyGAP` | `src_short/SHORT_ReduceVectorFamilyGAP.cpp` |
| `SHORT_AutomorphismGroup` | `src_short/SHORT_AutomorphismGroup.cpp` |
| `SHORT_SplitVectorFamily` | `src_short/SHORT_SplitVectorFamily.cpp` |

## src_sparse_solver

| Binary | Source |
|---|---|
| `StandaloneSparseSolver` | `src_sparse_solver/StandaloneSparseSolver.cpp` |
| `StandaloneSparseSolver_NNZ` | `src_sparse_solver/StandaloneSparseSolver_NNZ.cpp` |

## src_export_oscar

Alternate builds of same-named binaries from other directories, via symlinks into the source dirs.
Built with Oscar-specific flags. All `.cpp` files here are symlinks to the originals.

| Binary | Source (symlink) |
|---|---|
| `CP_TestCompletePositivity` | `src_export_oscar/CP_TestCompletePositivity.cpp` → `src_copos/` |
| `CP_TestCopositivity` | `src_export_oscar/CP_TestCopositivity.cpp` → `src_copos/` |
| `GRP_ListMat_Vdiag_EXT_Automorphism` | `src_export_oscar/GRP_ListMat_Vdiag_EXT_Automorphism.cpp` → `src_group/` |
| `GRP_ListMat_Vdiag_EXT_Invariant` | `src_export_oscar/GRP_ListMat_Vdiag_EXT_Invariant.cpp` → `src_group/` |
| `GRP_ListMat_Vdiag_EXT_Isomorphism` | `src_export_oscar/GRP_ListMat_Vdiag_EXT_Isomorphism.cpp` → `src_group/` |
| `LATT_Automorphism` | `src_export_oscar/LATT_Automorphism.cpp` → `src_latt/` |
| `LATT_IndefiniteReduction` | `src_export_oscar/LATT_IndefiniteReduction.cpp` → `src_isotropy/` |
| `LATT_Isomorphism` | `src_export_oscar/LATT_Isomorphism.cpp` → `src_latt/` |
| `LATT_near` | `src_export_oscar/LATT_near.cpp` → `src_latt/` |
| `LORENTZ_FundDomain_AllcockEdgewalk` | `src_export_oscar/LORENTZ_FundDomain_AllcockEdgewalk.cpp` → `src_lorentzian/` |
| `POLY_cdd_LinearProgramming` | `src_export_oscar/POLY_cdd_LinearProgramming.cpp` → `src_poly/` |
| `POLY_dual_description_group` | `src_export_oscar/POLY_dual_description_group.cpp` → `src_poly/` |
| `POLY_redundancyGroup` | `src_export_oscar/POLY_redundancyGroup.cpp` → `src_poly/` |
| `SHORT_TestRealizability` | `src_export_oscar/SHORT_TestRealizability.cpp` → `src_short/` |

## src_polarization

| Binary | Source |
|---|---|
| `polarization_gaussian` | `src_polarization/polarization_gaussian.cpp` | **Makefile-only** |
| `test_hessian_quadratic` | `src_polarization/test_hessian_quadratic.cpp` | **Makefile-only** |
| `test_lambda` | `src_polarization/test_lambda.cpp` | **Makefile-only** |

---

## Summary

| Source Directory | # Binaries (CMake) | # Binaries (Makefile-only) |
|---|---|---|
| `src_copos` | 7 | — |
| `src_ctype` | 12 | — |
| `src_delaunay` | 5 | — |
| `src_dualdesc` | 13 | — |
| `src_export_oscar` | — | — |
| `src_group` | 30 | 1 |
| `src_indefinite` | 9 | — |
| `src_isotropy` | 11 | — |
| `src_latt` | 15 | 1 |
| `src_lorentzian` | 14 | — |
| `src_perfect` | 4 | — |
| `src_poincare_polyhedron` | 1 | — |
| `src_polarization` | — | 3 |
| `src_poly` | 24 | 2 |
| `src_polydecomp` | 3 | — |
| `src_polygen` | 1 | — |
| `src_rankin` | 1 | — |
| `src__covering` | 3 | 1 |
| `src_short` | 7 | — |
| `src_sparse_solver` | 2 | — |
| **Total** | **162** | **8** |

**Grand total: 170 distinct binaries.**

All CMake binaries are built into `${CMAKE_BINARY_DIR}/bin/`.
Makefile-only binaries must be built via per-directory `make` commands or the legacy `compile.sh` script.

### Stale Makefile entries (no `.cpp` source found)

These appear in Makefile `PROGRAM` variables but have no corresponding `.cpp` file — likely renamed or deleted:
- `IndefiniteReduction` (listed in `src_isotropy/Makefile_indefinite`)
- `test_hot` (listed in `src_polarization/Makefile`)
- `test_hot_param` (listed in `src_polarization/Makefile`)
- `POLY_redundancyClarkson` (listed in `src_poly/Makefile_cdd`)

### Orphan binaries (`.cpp` with `main()` not wired into any build)

These files contain `main()` but are **not** referenced in any Makefile or CMakeLists.txt.
They can be compiled manually with `g++ -std=c++20 ...` but are not part of the official build:

| Source |
|---|
| `src_ctype/CTYP_CheckCanonical.cpp` |
| `src_ctype/CTYP_ComputeMaxCoefficients.cpp` |
| `src_ctype/CTYP_ComputeStatistics.cpp` |
| `src_ctype/CTYP_TimingRandomAccess.cpp` |
| `src_dualdesc/POLY_gather_vectface.cpp` |
| `src_indefinite/TEST_PermutationSignCanonic.cpp` |
| `src_isotropy/LATT_AutomorphyReduction.cpp` |
| `src_isotropy/LATT_SublatticeBasisReduction.cpp` |
| `src_latt/LATT_ZeroOneSolutions.cpp` |
| `src_lorentzian/LORENTZ_ComputeRoots_Vertex.cpp` |
| `src_lorentzian/LORENTZ_SingleEdgewalk.cpp` |
| `src_perfect/ComputePerfect.cpp` |
| `src_polarization/test_hessian.cpp` |

### Shared link targets (no `main()`)

These `.cpp` files are compiled as object files and linked into other binaries via `SRCFILES` in Makefiles or as CMake sources.
They do not produce standalone binaries:

| Source | Used in |
|---|---|
| `src_ctype/POLY_c_cddlib_mpq.cpp` | multiple Makefiles (SRCFILES) |
| `src_dualdesc/POLY_c_cddlib_mpq.cpp` | multiple Makefiles (SRCFILES) |
| `src_lorentzian/POLY_c_cddlib_mpq.cpp` | multiple Makefiles (SRCFILES) |
| `src_perfect/POLY_c_cddlib_mpq.cpp` | multiple Makefiles (SRCFILES) |
| `src_poincare_polyhedron/POLY_c_cddlib_mpq.cpp` | multiple Makefiles (SRCFILES) |
| `src_poly/POLY_c_cddlib_mpq.cpp` | multiple Makefiles (SRCFILES) |
| `src_polydecomp/POLY_c_cddlib_mpq.cpp` | multiple Makefiles (SRCFILES) |

### Archived code (`OLD/` subdirectories)

These files are in `OLD/` subdirectories and are not wired into any build system.
Preserved for reference only:

| Source |
|---|
| `src_ctype/OLD/CTYP_debug.cpp` |
| `src_ctype/OLD/CTYP_MakeInitialFile.cpp` |
| `src_ctype/OLD/CTYP_MergeLogs.cpp` |
| `src_ctype/OLD/CTYP_MPI_Enumeration.cpp` |
| `src_ctype/OLD/CTYP_MPI_Enumeration_debug.cpp` |
| `src_dualdesc/OLD/ConvertNC_to_NC_FB_FF.cpp` |
| `src_dualdesc/OLD/DD_ConvertGAP_to_NC.cpp` |
| `src_dualdesc/OLD/POLY_NetcdfToGAP.cpp` |
| `src_lorentzian/OLD/LORENTZ_FindSpecificDistance.cpp` |

### Alternate build configs (`src_export_oscar/`)

The 14 `.cpp` files in `src_export_oscar/` are **symlinks** to originals in other `src_*` directories.
They produce binaries with the same name but different link flags (Oscar export build config).
They do not add distinct binary names.

| Source (symlink) | Same-name binary |
|---|---|
| `src_export_oscar/CP_TestCompletePositivity.cpp` | `CP_TestCompletePositivity` (also `src_copos/`) |
| `src_export_oscar/CP_TestCopositivity.cpp` | `CP_TestCopositivity` (also `src_copos/`) |
| `src_export_oscar/GRP_ListMat_Vdiag_EXT_Automorphism.cpp` | `GRP_ListMat_Vdiag_EXT_Automorphism` (also `src_group/`) |
| `src_export_oscar/GRP_ListMat_Vdiag_EXT_Invariant.cpp` | `GRP_ListMat_Vdiag_EXT_Invariant` (also `src_group/`) |
| `src_export_oscar/GRP_ListMat_Vdiag_EXT_Isomorphism.cpp` | `GRP_ListMat_Vdiag_EXT_Isomorphism` (also `src_group/`) |
| `src_export_oscar/LATT_Automorphism.cpp` | `LATT_Automorphism` (also `src_latt/`) |
| `src_export_oscar/LATT_IndefiniteReduction.cpp` | `LATT_IndefiniteReduction` (also `src_isotropy/`) |
| `src_export_oscar/LATT_Isomorphism.cpp` | `LATT_Isomorphism` (also `src_latt/`) |
| `src_export_oscar/LATT_near.cpp` | `LATT_near` (also `src_latt/`) |
| `src_export_oscar/LORENTZ_FundDomain_AllcockEdgewalk.cpp` | `LORENTZ_FundDomain_AllcockEdgewalk` (also `src_lorentzian/`) |
| `src_export_oscar/POLY_cdd_LinearProgramming.cpp` | `POLY_cdd_LinearProgramming` (also `src_poly/`) |
| `src_export_oscar/POLY_dual_description_group.cpp` | `POLY_dual_description_group` (also `src_poly/`) |
| `src_export_oscar/POLY_redundancyGroup.cpp` | `POLY_redundancyGroup` (also `src_poly/`) |
| `src_export_oscar/SHORT_TestRealizability.cpp` | `SHORT_TestRealizability` (also `src_short/`) |

Note: `src_export_oscar/LATT_canonicalize.cpp` is a **broken symlink** (target `../src_latt/LATT_canonicalize.cpp` does not exist; the real file is `LATT_Canonicalize.cpp` with uppercase `C`). It cannot compile.
