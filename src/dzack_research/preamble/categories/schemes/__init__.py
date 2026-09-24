"""Lazy public aggregation for owned algebraic-geometry categories."""

from importlib import import_module as _import_module


_EXPORTS = {
    'HesseBertiniFamily': ('dzack_research.preamble.categories.schemes.bertini_families', 'HesseBertiniFamily'),
    'HorikawaEnriquesSurface': ('dzack_research.preamble.categories.schemes.enriques_families', 'HorikawaEnriquesSurface'),
    'ADELogPairs': ('dzack_research.preamble.categories.schemes.ade_surfaces', 'ADELogPairs'),
    'SideDecoration': ('dzack_research.preamble.categories.schemes.ade_surfaces', 'SideDecoration'),
    'AlgebraSheaves': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'AlgebraSheaves'),
    'AnalyticDiscFamily': ('dzack_research.preamble.categories.schemes.analytic_families', 'AnalyticDiscFamily'),
    'CyclicCoverBaseChangeComparison': ('dzack_research.preamble.categories.schemes.cyclic_covers', 'CyclicCoverBaseChangeComparison'),
    'RelativeCyclicCoverLift': ('dzack_research.preamble.categories.schemes.cyclic_covers', 'RelativeCyclicCoverLift'),
    'RelativeProjectivizations': ('dzack_research.preamble.categories.schemes.relative_proj', 'RelativeProjectivizations'),
    'HorikawaK3Family': ('dzack_research.preamble.categories.schemes.k3_families', 'HorikawaK3Family'),
    'LegendreMonodromyFamily': ('dzack_research.preamble.categories.schemes.monodromy', 'LegendreMonodromyFamily'),
    'PointedAnalyticFundamentalGroup': ('dzack_research.preamble.categories.schemes.monodromy', 'PointedAnalyticFundamentalGroup'),
    'AffineInvariantQuotientBaseChangeComparison': ('dzack_research.preamble.categories.schemes.quotients', 'AffineInvariantQuotientBaseChangeComparison'),
    'AffineSchemes': ('dzack_research.preamble.categories.schemes.schemes', 'AffineSchemes'),
    'AffineGSchemes': ('dzack_research.preamble.categories.schemes.schemes', 'AffineGSchemes'),
    'AffineGroupSchemes': ('dzack_research.preamble.categories.schemes.group_schemes', 'AffineGroupSchemes'),
    'AffineGroupSchemeActions': ('dzack_research.preamble.categories.schemes.group_schemes', 'AffineGroupSchemeActions'),
    'AffineSpaces': ('dzack_research.preamble.categories.schemes.schemes', 'AffineSpaces'),
    'ClosedEmbeddings': ('dzack_research.preamble.categories.schemes.schemes', 'ClosedEmbeddings'),
    'ClosedSubschemes': ('dzack_research.preamble.categories.schemes.schemes', 'ClosedSubschemes'),
    'ConvexPolygons': ('dzack_research.preamble.categories.schemes.polytopes', 'ConvexPolygons'),
    'ConvexPolytopes': ('dzack_research.preamble.categories.schemes.polytopes', 'ConvexPolytopes'),
    'DistinguishedAffineCoverRefinement': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'DistinguishedAffineCoverRefinement'),
    'DistinguishedAffineCovers': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'DistinguishedAffineCovers'),
    'distinguished_affine_coverage': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'distinguished_affine_coverage'),
    'Curves': ('dzack_research.preamble.categories.schemes.varieties', 'Curves'),
    'CurveLocalDeltaContribution': ('dzack_research.preamble.categories.schemes.curve_genus', 'CurveLocalDeltaContribution'),
    'rational_quintic_with_nonrational_node_normalization': ('dzack_research.preamble.categories.schemes.curve_genus', 'rational_quintic_with_nonrational_node_normalization'),
    'rational_quintic_with_two_nodes_normalization': ('dzack_research.preamble.categories.schemes.curve_genus', 'rational_quintic_with_two_nodes_normalization'),
    'SchemeMonomorphisms': ('dzack_research.preamble.categories.schemes.schemes', 'SchemeMonomorphisms'),
    'FiberProductSchemes': ('dzack_research.preamble.categories.schemes.schemes', 'FiberProductSchemes'),
    'IntegralSchemes': ('dzack_research.preamble.categories.schemes.schemes', 'IntegralSchemes'),
    'IsolatedHypersurfaceSingularity': ('dzack_research.preamble.categories.schemes.singularities', 'IsolatedHypersurfaceSingularity'),
    'LatticePolygons': ('dzack_research.preamble.categories.schemes.polytopes', 'LatticePolygons'),
    'LatticePolytopes': ('dzack_research.preamble.categories.schemes.polytopes', 'LatticePolytopes'),
    'RegularPolytopes': ('dzack_research.preamble.categories.schemes.polytopes', 'RegularPolytopes'),
    'LocallyRingedSpaces': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'LocallyRingedSpaces'),
    'ModuleSheaves': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'ModuleSheaves'),
    'LogPairs': ('dzack_research.preamble.categories.schemes.log_pairs', 'LogPairs'),
    'NormalSchemes': ('dzack_research.preamble.categories.schemes.schemes', 'NormalSchemes'),
    'OpenImmersions': ('dzack_research.preamble.categories.schemes.schemes', 'OpenImmersions'),
    'ProjectivePointBlowups': ('dzack_research.preamble.categories.schemes.blowups', 'ProjectivePointBlowups'),
    'ProjectiveCompleteIntersections': ('dzack_research.preamble.categories.schemes.complete_intersections', 'ProjectiveCompleteIntersections'),
    'ProjectiveSchemes': ('dzack_research.preamble.categories.schemes.schemes', 'ProjectiveSchemes'),
    'ProjectiveSpaces': ('dzack_research.preamble.categories.schemes.schemes', 'ProjectiveSpaces'),
    'ProductProjectiveSpaces': ('dzack_research.preamble.categories.schemes.schemes', 'ProductProjectiveSpaces'),
    'ProductSchemes': ('dzack_research.preamble.categories.schemes.schemes', 'ProductSchemes'),
    'QuasiCoherentSheaves': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'QuasiCoherentSheaves'),
    'RationalPolyhedralFans': ('dzack_research.preamble.categories.schemes.toric.fans', 'RationalPolyhedralFans'),
    'RingedSpaces': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'RingedSpaces'),
    'SheafObjects': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'SheafObjects'),
    'SheafedSpaces': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'SheafedSpaces'),
    'ZariskiCoveringFamilies': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'ZariskiCoveringFamilies'),
    'zariski_coverage': ('dzack_research.preamble.categories.schemes.ringed_spaces', 'zariski_coverage'),
    'SchemeMorphism': ('dzack_research.preamble.categories.schemes.schemes', 'SchemeMorphism'),
    'Schemes': ('dzack_research.preamble.categories.schemes.schemes', 'Schemes'),
    'SmoothSchemes': ('dzack_research.preamble.categories.schemes.schemes', 'SmoothSchemes'),
    'Surfaces': ('dzack_research.preamble.categories.schemes.varieties', 'Surfaces'),
    'ToricLogPairs': ('dzack_research.preamble.categories.schemes.log_pairs', 'ToricLogPairs'),
    'ToricFixedPointBlowups': ('dzack_research.preamble.categories.schemes.toric.blowups', 'ToricFixedPointBlowups'),
    'ToricSchemes': ('dzack_research.preamble.categories.schemes.toric.toric_schemes', 'ToricSchemes'),
    'ToricGeometricLineBundleCohomologySpaces': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'ToricGeometricLineBundleCohomologySpaces'),
    'GeometricFundamentalGroups': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'GeometricFundamentalGroups'),
    'IntegralTopologicalCohomologyGroups': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'IntegralTopologicalCohomologyGroups'),
    'ResolutionIntegralCohomologyGroups': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'ResolutionIntegralCohomologyGroups'),
    'NodalCubic': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'NodalCubic'),
    'NodalCubicNormalization': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'NodalCubicNormalization'),
    'NodalCubicIntegralTopology': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'NodalCubicIntegralTopology'),
    'IntegralSingularCohomologyGroups': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'IntegralSingularCohomologyGroups'),
    'PGL2IntegralTopology': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'PGL2IntegralTopology'),
    'ProjectiveGeneralLinearGroup2': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'ProjectiveGeneralLinearGroup2'),
    'ToricIntegralSingularCohomologyGroups': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'ToricIntegralSingularCohomologyGroups'),
    'ToricFundamentalGroups': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'ToricFundamentalGroups'),
    'ToricWeightCohomologyComplexes': ('dzack_research.preamble.categories.schemes.geometric_cohomology', 'ToricWeightCohomologyComplexes'),
    'Varieties': ('dzack_research.preamble.categories.schemes.varieties', 'Varieties'),
    'FiniteGluedInvariantQuotient': ('dzack_research.preamble.categories.schemes.invariant_quotient_gluing', 'FiniteGluedInvariantQuotient'),
}

__all__ = ['HesseBertiniFamily', 'HorikawaEnriquesSurface', 'ADELogPairs', 'SideDecoration', 'AlgebraSheaves', 'AnalyticDiscFamily', 'CyclicCoverBaseChangeComparison', 'RelativeCyclicCoverLift', 'RelativeProjectivizations', 'HorikawaK3Family', 'LegendreMonodromyFamily', 'PointedAnalyticFundamentalGroup', 'AffineInvariantQuotientBaseChangeComparison', 'AffineSchemes', 'AffineGSchemes', 'AffineGroupSchemes', 'AffineGroupSchemeActions', 'AffineSpaces', 'ClosedEmbeddings', 'ClosedSubschemes', 'ConvexPolygons', 'ConvexPolytopes', 'DistinguishedAffineCoverRefinement', 'DistinguishedAffineCovers', 'distinguished_affine_coverage', 'Curves', 'CurveLocalDeltaContribution', 'rational_quintic_with_nonrational_node_normalization', 'rational_quintic_with_two_nodes_normalization', 'SchemeMonomorphisms', 'FiberProductSchemes', 'IntegralSchemes', 'IsolatedHypersurfaceSingularity', 'LatticePolygons', 'LatticePolytopes', 'RegularPolytopes', 'LocallyRingedSpaces', 'ModuleSheaves', 'LogPairs', 'NormalSchemes', 'OpenImmersions', 'ProjectivePointBlowups', 'ProjectiveCompleteIntersections', 'ProjectiveSchemes', 'ProjectiveSpaces', 'ProductProjectiveSpaces', 'ProductSchemes', 'QuasiCoherentSheaves', 'RationalPolyhedralFans', 'RingedSpaces', 'SheafObjects', 'SheafedSpaces', 'ZariskiCoveringFamilies', 'zariski_coverage', 'SchemeMorphism', 'Schemes', 'SmoothSchemes', 'Surfaces', 'ToricLogPairs', 'ToricFixedPointBlowups', 'ToricSchemes', 'ToricGeometricLineBundleCohomologySpaces', 'GeometricFundamentalGroups', 'IntegralTopologicalCohomologyGroups', 'ResolutionIntegralCohomologyGroups', 'NodalCubic', 'NodalCubicNormalization', 'NodalCubicIntegralTopology', 'IntegralSingularCohomologyGroups', 'PGL2IntegralTopology', 'ProjectiveGeneralLinearGroup2', 'ToricIntegralSingularCohomologyGroups', 'ToricFundamentalGroups', 'ToricWeightCohomologyComplexes', 'Varieties', 'FiniteGluedInvariantQuotient']


def __getattr__(name):
    if name not in _EXPORTS:
        raise AttributeError(name)
    module_name, attribute = _EXPORTS[name]
    value = getattr(_import_module(module_name), attribute)
    globals()[name] = value
    return value


def __dir__():
    return sorted((*globals(), *__all__))
