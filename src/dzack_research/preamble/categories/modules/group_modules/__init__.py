'Modules equipped with group actions.'

from importlib import import_module as _import_module

_EXPORTS = {'FinitelyGeneratedFreeGroupModules': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                                       'FinitelyGeneratedFreeGroupModules'),
 'FinitelyPresentedGroupModules': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                                   'FinitelyPresentedGroupModules'),
 'GroupModule': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                 'GroupModule'),
 'GroupModuleHomset': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                       'GroupModuleHomset'),
 'GroupModuleMorphism': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                         'GroupModuleMorphism'),
 'GroupModules': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                  'GroupModules'),
 'group_module_homset': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                         'group_module_homset'),
 'trivial_group_action': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                          'trivial_group_action'),
 'GroupLattice': ('dzack_research.preamble.categories.modules.group_modules.group_lattices',
                  'GroupLattice'),
 'GroupLattices': ('dzack_research.preamble.categories.modules.group_modules.group_lattices',
                   'GroupLattices')}

__all__ = ['FinitelyGeneratedFreeGroupModules',
 'FinitelyPresentedGroupModules',
 'GroupModule',
 'GroupModuleHomset',
 'GroupModuleMorphism',
 'GroupModules',
 'GroupLattice',
 'GroupLattices',
 'group_module_homset',
 'trivial_group_action']

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
