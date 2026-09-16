'Lazy public aggregation for finitely_generated.'

from importlib import import_module as _import_module

_EXPORTS = {'FinitelyGeneratedFreeModules': ('dzack_research.preamble.categories.modules.pure.modules',
                                  'FinitelyGeneratedFreeModules'),
 'FinitelyPresentedModules': ('dzack_research.preamble.categories.modules.pure.modules',
                              'FinitelyPresentedModules'),
 'ModulesWithChosenFinitePresentation': ('dzack_research.preamble.categories.modules.pure.modules',
                                         'ModulesWithChosenFinitePresentation'),
 'FinitelyPresentedTorsionModules': ('dzack_research.preamble.categories.modules.pure.modules',
                                     'FinitelyPresentedTorsionModules'),
}

__all__ = ['FinitelyGeneratedFreeModules',
 'FinitelyPresentedModules',
 'FinitelyPresentedTorsionModules',
 'ModulesWithChosenFinitePresentation',
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
