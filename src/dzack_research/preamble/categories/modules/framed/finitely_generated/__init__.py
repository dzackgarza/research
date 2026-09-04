'Lazy public aggregation for finitely_generated.'

from importlib import import_module as _import_module

_EXPORTS = {'FinitelyGeneratedFreeModules': ('dzack_research.preamble.categories.modules.pure.modules',
                                  'FinitelyGeneratedFreeModules'),
 'BasedFreeModule': ('dzack_research.preamble.categories.modules.framed.framed_free_modules',
                     'BasedFreeModule'),
 'ring_as_module': ('dzack_research.preamble.categories.modules.framed.framed_free_modules',
                    'ring_as_module'),
 'FinitelyPresentedModules': ('dzack_research.preamble.categories.modules.pure.modules',
                              'FinitelyPresentedModules'),
 'ModulesWithChosenFinitePresentation': ('dzack_research.preamble.categories.modules.pure.modules',
                                         'ModulesWithChosenFinitePresentation'),
 'FinitelyPresentedModule': ('dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules',
                             'FinitelyPresentedModule'),
 'FinitelyPresentedTorsionModules': ('dzack_research.preamble.categories.modules.pure.torsion_modules',
                                     'FinitelyPresentedTorsionModules'),
 'TorsionModule': ('dzack_research.preamble.categories.modules.pure.torsion_modules',
                   'TorsionModule')}

__all__ = ['BasedFreeModule',
 'FinitelyGeneratedFreeModules',
 'FinitelyPresentedModule',
 'FinitelyPresentedModules',
 'FinitelyPresentedTorsionModules',
 'ModulesWithChosenFinitePresentation',
 'TorsionModule',
 'ring_as_module']

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
