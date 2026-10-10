'Modules over group algebras and lattices with a group action.'

from importlib import import_module as _import_module

_EXPORTS = {'GroupModuleMor': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                       'GroupModuleMor'),
 'FiniteFreeGroupRepresentations': ('dzack_research.preamble.categories.modules.group_modules.group_modules', 'FiniteFreeGroupRepresentations'),
 'OrdinaryCharacterRepresentations': ('dzack_research.preamble.categories.modules.group_modules.group_modules', 'OrdinaryCharacterRepresentations'),
 'BrauerCharacterRepresentations': ('dzack_research.preamble.categories.modules.group_modules.group_modules', 'BrauerCharacterRepresentations'),
 'GroupModuleMorphism': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                         'GroupModuleMorphism'),
 'ModulesOverGroupAlgebra': ('dzack_research.preamble.categories.modules.group_modules.group_modules',
                             'ModulesOverGroupAlgebra'),
 'LatticesOverGroupAlgebra': ('dzack_research.preamble.categories.modules.group_modules.group_lattices',
                             'LatticesOverGroupAlgebra')}

__all__ = ['GroupModuleMor',
 'FiniteFreeGroupRepresentations',
 'OrdinaryCharacterRepresentations',
 'BrauerCharacterRepresentations',
 'GroupModuleMorphism',
 'ModulesOverGroupAlgebra',
 'LatticesOverGroupAlgebra',
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
