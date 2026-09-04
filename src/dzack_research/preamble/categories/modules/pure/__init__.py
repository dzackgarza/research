'Lazy public aggregation for pure.'

from importlib import import_module as _import_module

_EXPORTS = {'Modules': ('dzack_research.preamble.categories.modules.pure.modules', 'Modules'),
 'VectorSpaces': ('dzack_research.preamble.categories.modules.pure.modules', 'VectorSpaces'),
 'FreeModules': ('dzack_research.preamble.categories.modules.pure.modules', 'FreeModules'),
 'ProjectiveModules': ('dzack_research.preamble.categories.modules.pure.modules',
                       'ProjectiveModules'),
 'TorsionModules': ('dzack_research.preamble.categories.modules.pure.torsion_modules',
                    'TorsionModules')}

__all__ = ['FreeModules', 'Modules', 'ProjectiveModules', 'TorsionModules', 'VectorSpaces']

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
