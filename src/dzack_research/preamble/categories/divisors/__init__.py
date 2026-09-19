'Lazy public aggregation for divisors.'

from importlib import import_module as _import_module

_EXPORTS = {'AlgebraicCycleGroups': ('dzack_research.preamble.categories.divisors.chow_groups', 'AlgebraicCycleGroups'),
 'CartierDivisorGroups': ('dzack_research.preamble.categories.divisors.cartier_divisor_groups',
                          'CartierDivisorGroups'),
 'ClassGroups': ('dzack_research.preamble.categories.divisors.class_groups', 'ClassGroups'),
 'LineBundleCohomologySpaces': ('dzack_research.preamble.categories.divisors.cohomology',
                                'LineBundleCohomologySpaces'),
 'ChowGroups': ('dzack_research.preamble.categories.divisors.chow_groups', 'ChowGroups'),
 'TorusInvariantCycleGroups': ('dzack_research.preamble.categories.divisors.chow_groups',
                               'TorusInvariantCycleGroups'),
 'CompleteLinearSystems': ('dzack_research.preamble.categories.divisors.linear_systems',
                           'CompleteLinearSystems'),
 'CoxRings': ('dzack_research.preamble.categories.divisors.cox_rings', 'CoxRings'),
 'DivisorGroups': ('dzack_research.preamble.categories.divisors.divisor_groups', 'DivisorGroups'),
 'FormalDivisorGroups': ('dzack_research.preamble.categories.divisors.divisor_groups',
                         'FormalDivisorGroups'),
 'FiniteAtlasInvertibleSheaf': ('dzack_research.preamble.categories.divisors.invertible_sheaves',
                                'FiniteAtlasInvertibleSheaf'),
 'InvertibleSheaf': ('dzack_research.preamble.categories.divisors.invertible_sheaves',
                     'InvertibleSheaf'),
 'HomogeneousPolynomialSectionSpaces': ('dzack_research.preamble.categories.divisors.linear_systems',
                                        'HomogeneousPolynomialSectionSpaces'),
 'ImposedMultiplicityLinearSystems': ('dzack_research.preamble.categories.divisors.linear_systems',
                                      'ImposedMultiplicityLinearSystems'),
 'PicardGroups': ('dzack_research.preamble.categories.divisors.picard_groups', 'PicardGroups'),
 'ProductProjectiveSubschemeLineBundle': ('dzack_research.preamble.categories.divisors.invertible_sheaves', 'ProductProjectiveSubschemeLineBundle'),
 'ProjectiveSubschemeLineBundle': ('dzack_research.preamble.categories.divisors.invertible_sheaves', 'ProjectiveSubschemeLineBundle'),
 'ProjectiveLinearSystems': ('dzack_research.preamble.categories.divisors.linear_systems',
                             'ProjectiveLinearSystems'),
 'ProjectiveJetSpaces': ('dzack_research.preamble.categories.divisors.linear_systems',
                        'ProjectiveJetSpaces'),
 'SectionRings': ('dzack_research.preamble.categories.divisors.section_rings', 'SectionRings'),
 'WeilDivisorGroups': ('dzack_research.preamble.categories.divisors.weil_divisor_groups',
                       'WeilDivisorGroups')}

__all__ = [
    'AlgebraicCycleGroups',
    'CartierDivisorGroups',
    'ChowGroups',
    'ClassGroups',
    'CompleteLinearSystems',
    'CoxRings',
    'DivisorGroups',
    'FiniteAtlasInvertibleSheaf',
    'FormalDivisorGroups',
    'HomogeneousPolynomialSectionSpaces',
    'ImposedMultiplicityLinearSystems',
    'InvertibleSheaf',
    'LineBundleCohomologySpaces',
    'PicardGroups',
    'ProjectiveJetSpaces',
    'ProductProjectiveSubschemeLineBundle',
    'ProjectiveSubschemeLineBundle',
    'ProjectiveLinearSystems',
    'SectionRings',
    'TorusInvariantCycleGroups',
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
