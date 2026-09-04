'Mapping spaces \\(C^k(X,Y)\\), Lebesgue spaces \\(L^p\\), and sequence spaces \\(\\ell^p\\).'

from importlib import import_module as _import_module

_EXPORTS = {'C': ('dzack_research.preamble.categories.functions.real_functions', 'C'),
 'Lp': ('dzack_research.preamble.categories.functions.real_functions', 'Lp'),
 'ell': ('dzack_research.preamble.categories.functions.real_functions', 'ell'),
 'GradedLebesgueModule': ('dzack_research.preamble.categories.functions.lebesgue_graded',
                          'GradedLebesgueModule'),
 'GradedTensorProductModules': ('dzack_research.preamble.categories.functions.lebesgue_graded',
                                'GradedTensorProductModules'),
 'GradedTensorSquare': ('dzack_research.preamble.categories.functions.lebesgue_graded',
                        'GradedTensorSquare'),
 'LebesgueGradedModules': ('dzack_research.preamble.categories.functions.lebesgue_graded',
                           'LebesgueGradedModules'),
 'graded_lebesgue_algebra': ('dzack_research.preamble.categories.functions.lebesgue_graded',
                             'graded_lebesgue_algebra'),
 'lebesgue_convolution_algebra': ('dzack_research.preamble.categories.functions.lebesgue_graded',
                                  'lebesgue_convolution_algebra')}

__all__ = ['C',
 'GradedLebesgueModule',
 'GradedTensorProductModules',
 'GradedTensorSquare',
 'LebesgueGradedModules',
 'Lp',
 'ell',
 'graded_lebesgue_algebra',
 'lebesgue_convolution_algebra']

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
