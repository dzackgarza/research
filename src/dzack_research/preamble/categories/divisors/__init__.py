'Lazy public aggregation for divisors.'

from importlib import import_module as _import_module

_EXPORTS = {'AffineCodimensionOneChowComparison': ('dzack_research.preamble.categories.divisors.chow_groups', 'AffineCodimensionOneChowComparison'),
 'AlgebraicCycleGroups': ('dzack_research.preamble.categories.divisors.chow_groups', 'AlgebraicCycleGroups'),
 'CartierDivisorGroup': ('dzack_research.preamble.categories.divisors.cartier_divisor_groups',
                         'CartierDivisorGroup'),
 'CartierDivisorGroups': ('dzack_research.preamble.categories.divisors.cartier_divisor_groups',
                          'CartierDivisorGroups'),
 'ClassGroup': ('dzack_research.preamble.categories.divisors.class_groups', 'ClassGroup'),
 'ClassGroups': ('dzack_research.preamble.categories.divisors.class_groups', 'ClassGroups'),
 'LineBundleCohomologySpaces': ('dzack_research.preamble.categories.divisors.cohomology',
                                'LineBundleCohomologySpaces'),
 'ChowGroup': ('dzack_research.preamble.categories.divisors.chow_groups', 'ChowGroup'),
 'ChowGroups': ('dzack_research.preamble.categories.divisors.chow_groups', 'ChowGroups'),
 'TorusInvariantCycleGroups': ('dzack_research.preamble.categories.divisors.chow_groups',
                               'TorusInvariantCycleGroups'),
 'CompleteLinearSystems': ('dzack_research.preamble.categories.divisors.linear_systems',
                           'CompleteLinearSystems'),
 'CoxRings': ('dzack_research.preamble.categories.divisors.cox_rings', 'CoxRings'),
 'DivisorGroup': ('dzack_research.preamble.categories.divisors.divisor_groups', 'DivisorGroup'),
 'DivisorGroups': ('dzack_research.preamble.categories.divisors.divisor_groups', 'DivisorGroups'),
 'FormalDivisor': ('dzack_research.preamble.categories.divisors.divisor_groups', 'FormalDivisor'),
 'FormalDivisorGroup': ('dzack_research.preamble.categories.divisors.divisor_groups',
                        'FormalDivisorGroup'),
 'FormalDivisorGroups': ('dzack_research.preamble.categories.divisors.divisor_groups',
                         'FormalDivisorGroups'),
 'DivisorClassComparison': ('dzack_research.preamble.categories.divisors.general_divisors',
                           'DivisorClassComparison'),
 'FiniteAtlasCartierDivisor': ('dzack_research.preamble.categories.divisors.general_divisors',
                              'FiniteAtlasCartierDivisor'),
 'FiniteAtlasInvertibleSheaf': ('dzack_research.preamble.categories.divisors.invertible_sheaves',
                                'FiniteAtlasInvertibleSheaf'),
 'InvertibleSheaf': ('dzack_research.preamble.categories.divisors.invertible_sheaves',
                     'InvertibleSheaf'),
 'HomogeneousPolynomialSectionSpaces': ('dzack_research.preamble.categories.divisors.linear_systems',
                                        'HomogeneousPolynomialSectionSpaces'),
 'ImposedMultiplicityLinearSystems': ('dzack_research.preamble.categories.divisors.linear_systems',
                                      'ImposedMultiplicityLinearSystems'),
 'PicardGroup': ('dzack_research.preamble.categories.divisors.picard_groups', 'PicardGroup'),
 'PicardGroups': ('dzack_research.preamble.categories.divisors.picard_groups', 'PicardGroups'),
 'ProductProjectiveSubschemeLineBundle': ('dzack_research.preamble.categories.divisors.invertible_sheaves', 'ProductProjectiveSubschemeLineBundle'),
 'ProjectiveSubschemeLineBundle': ('dzack_research.preamble.categories.divisors.invertible_sheaves', 'ProjectiveSubschemeLineBundle'),
 'ProjectiveLinearSystems': ('dzack_research.preamble.categories.divisors.linear_systems',
                             'ProjectiveLinearSystems'),
 'ProjectiveJetSpaces': ('dzack_research.preamble.categories.divisors.linear_systems',
                        'ProjectiveJetSpaces'),
 'SerreIntersectionData': ('dzack_research.preamble.categories.divisors.chow_groups', 'SerreIntersectionData'),
 'SectionRings': ('dzack_research.preamble.categories.divisors.section_rings', 'SectionRings'),
 'WeilDivisorGroup': ('dzack_research.preamble.categories.divisors.weil_divisor_groups',
                      'WeilDivisorGroup'),
 'WeilDivisorGroups': ('dzack_research.preamble.categories.divisors.weil_divisor_groups',
                       'WeilDivisorGroups')}

__all__ = [
    'AffineCodimensionOneChowComparison',
    'AlgebraicCycleGroups',
    'CartierDivisorGroup',
    'CartierDivisorGroups',
    'ChowGroup',
    'ChowGroups',
    'ClassGroup',
    'ClassGroups',
    'CompleteLinearSystems',
    'CoxRings',
    'DivisorGroup',
    'DivisorGroups',
    'DivisorClassComparison',
    'FiniteAtlasCartierDivisor',
    'FiniteAtlasInvertibleSheaf',
    'FormalDivisor',
    'FormalDivisorGroup',
    'FormalDivisorGroups',
    'HomogeneousPolynomialSectionSpaces',
    'ImposedMultiplicityLinearSystems',
    'InvertibleSheaf',
    'LineBundleCohomologySpaces',
    'PicardGroup',
    'PicardGroups',
    'ProjectiveJetSpaces',
    'ProductProjectiveSubschemeLineBundle',
    'ProjectiveSubschemeLineBundle',
    'ProjectiveLinearSystems',
    'SerreIntersectionData',
    'SectionRings',
    'TorusInvariantCycleGroups',
    'WeilDivisorGroup',
    'WeilDivisorGroups',
]

def __getattr__(name):
    try:
        module_name, attribute = _EXPORTS[name]
    except KeyError as error:
        raise AttributeError(name) from error
    value = getattr(_import_module(module_name), attribute)
    globals()[name] = value
    return value

def __dir__():
    return sorted((*globals(), *__all__))
