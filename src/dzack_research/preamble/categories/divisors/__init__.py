'Lazy public aggregation for divisors.'

from importlib import import_module as _import_module

_EXPORTS = {'CartierDivisorGroup': ('dzack_research.preamble.categories.divisors.cartier_divisor_groups',
                         'CartierDivisorGroup'),
 'CartierDivisorGroups': ('dzack_research.preamble.categories.divisors.cartier_divisor_groups',
                          'CartierDivisorGroups'),
 'ClassGroup': ('dzack_research.preamble.categories.divisors.class_groups', 'ClassGroup'),
 'ClassGroups': ('dzack_research.preamble.categories.divisors.class_groups', 'ClassGroups'),
 'LineBundleCohomologySpace': ('dzack_research.preamble.categories.divisors.cohomology',
                               'LineBundleCohomologySpace'),
 'LineBundleCohomologySpaces': ('dzack_research.preamble.categories.divisors.cohomology',
                                'LineBundleCohomologySpaces'),
 'ChowGroup': ('dzack_research.preamble.categories.divisors.chow_groups', 'ChowGroup'),
 'ChowGroups': ('dzack_research.preamble.categories.divisors.chow_groups', 'ChowGroups'),
 'CompleteLinearSystem': ('dzack_research.preamble.categories.divisors.linear_systems',
                          'CompleteLinearSystem'),
 'CompleteLinearSystems': ('dzack_research.preamble.categories.divisors.linear_systems',
                           'CompleteLinearSystems'),
 'CoxRing': ('dzack_research.preamble.categories.divisors.cox_rings', 'CoxRing'),
 'CoxRings': ('dzack_research.preamble.categories.divisors.cox_rings', 'CoxRings'),
 'DivisorGroup': ('dzack_research.preamble.categories.divisors.divisor_groups', 'DivisorGroup'),
 'DivisorGroups': ('dzack_research.preamble.categories.divisors.divisor_groups', 'DivisorGroups'),
 'FormalDivisor': ('dzack_research.preamble.categories.divisors.divisor_groups', 'FormalDivisor'),
 'FormalDivisorGroup': ('dzack_research.preamble.categories.divisors.divisor_groups',
                        'FormalDivisorGroup'),
 'FormalDivisorGroups': ('dzack_research.preamble.categories.divisors.divisor_groups',
                         'FormalDivisorGroups'),
 'FiniteAtlasInvertibleSheaf': ('dzack_research.preamble.categories.divisors.invertible_sheaves',
                                'FiniteAtlasInvertibleSheaf'),
 'InvertibleSheaf': ('dzack_research.preamble.categories.divisors.invertible_sheaves',
                     'InvertibleSheaf'),
 'PicardGroup': ('dzack_research.preamble.categories.divisors.picard_groups', 'PicardGroup'),
 'PicardGroups': ('dzack_research.preamble.categories.divisors.picard_groups', 'PicardGroups'),
 'SectionRing': ('dzack_research.preamble.categories.divisors.section_rings', 'SectionRing'),
 'SectionRings': ('dzack_research.preamble.categories.divisors.section_rings', 'SectionRings'),
 'TrivialInvertibleSheaf': ('dzack_research.preamble.categories.divisors.invertible_sheaves',
                            'TrivialInvertibleSheaf'),
 'WeilDivisorGroup': ('dzack_research.preamble.categories.divisors.weil_divisor_groups',
                      'WeilDivisorGroup'),
 'WeilDivisorGroups': ('dzack_research.preamble.categories.divisors.weil_divisor_groups',
                       'WeilDivisorGroups')}

__all__ = [
    'CartierDivisorGroup',
    'CartierDivisorGroups',
    'ChowGroup',
    'ChowGroups',
    'ClassGroup',
    'ClassGroups',
    'CompleteLinearSystem',
    'CompleteLinearSystems',
    'CoxRing',
    'CoxRings',
    'DivisorGroup',
    'DivisorGroups',
    'FiniteAtlasInvertibleSheaf',
    'FormalDivisor',
    'FormalDivisorGroup',
    'FormalDivisorGroups',
    'InvertibleSheaf',
    'LineBundleCohomologySpace',
    'LineBundleCohomologySpaces',
    'PicardGroup',
    'PicardGroups',
    'SectionRing',
    'SectionRings',
    'TrivialInvertibleSheaf',
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
