'Enumerated sets of functions, as generating sets of free modules.'

from importlib import import_module as _import_module

_EXPORTS = {'EnumeratedSets': ('dzack_research.preamble.categories.sets.enumerated.enumerated_sets',
                    'EnumeratedSets'),
 'InfiniteEnumeratedSets': ('dzack_research.preamble.categories.sets.enumerated.enumerated_sets',
                            'InfiniteEnumeratedSets'),
 'FourierCharacters': ('dzack_research.preamble.categories.sets.enumerated.fourier_characters',
                       'FourierCharacters'),
 'EnumeratedByIntegers': ('dzack_research.preamble.categories.sets.enumerated.function_sets',
                          'EnumeratedByIntegers'),
 'EnumeratedByNaturals': ('dzack_research.preamble.categories.sets.enumerated.function_sets',
                          'EnumeratedByNaturals'),
 'FunctionEnumeratedSets': ('dzack_research.preamble.categories.sets.enumerated.function_sets',
                            'FunctionEnumeratedSets'),
 'HermitePolynomials': ('dzack_research.preamble.categories.sets.enumerated.hermite_polynomials',
                        'HermitePolynomials'),
 'LaurentMonomials': ('dzack_research.preamble.categories.sets.enumerated.laurent_monomials',
                      'LaurentMonomials'),
 'SincTranslates': ('dzack_research.preamble.categories.sets.enumerated.sinc_translates',
                    'SincTranslates')}

__all__ = ['EnumeratedByIntegers',
 'EnumeratedByNaturals',
 'EnumeratedSets',
 'FourierCharacters',
 'FunctionEnumeratedSets',
 'HermitePolynomials',
 'InfiniteEnumeratedSets',
 'LaurentMonomials',
 'SincTranslates']

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
