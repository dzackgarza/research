'Lazy public aggregation for framed.'

from importlib import import_module as _import_module

_EXPORTS = {'FramedModules': ('dzack_research.preamble.categories.modules.pure.modules', 'FramedModules'),
 'FractionFieldQuotient': ('dzack_research.preamble.categories.modules.framed.fraction_field_quotients',
                           'FractionFieldQuotient'),
 'FractionFieldQuotients': ('dzack_research.preamble.categories.modules.framed.fraction_field_quotients',
                            'FractionFieldQuotients'),
 'FramedFreeModules': ('dzack_research.preamble.categories.modules.framed.framed_free_modules',
                       'FramedFreeModules'),
 'FreeModule': ('dzack_research.preamble.categories.modules.framed.framed_free_modules',
                'FreeModule'),
 'FreeModuleOn': ('dzack_research.preamble.categories.modules.framed.framed_free_modules',
                  'FreeModuleOn')}

__all__ = ['FractionFieldQuotient',
 'FractionFieldQuotients',
 'FramedFreeModules',
 'FramedModules',
 'FreeModule',
 'FreeModuleOn']

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
