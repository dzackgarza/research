'Modules equipped with bilinear or quadratic forms.'

from importlib import import_module as _import_module

_EXPORTS = {'DiscriminantBilinearModules': ('dzack_research.preamble.categories.modules.framed.formed.discriminant_modules',
                                 'DiscriminantBilinearModules'),
 'DiscriminantModules': ('dzack_research.preamble.categories.modules.framed.formed.discriminant_modules',
                         'DiscriminantModules'),
 'DiscriminantQuadraticModules': ('dzack_research.preamble.categories.modules.framed.formed.discriminant_modules',
                                  'DiscriminantQuadraticModules'),
 'BilinearFormModules': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                         'BilinearFormModules'),
 'FiberedFormedModuleMor': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                               'FiberedFormedModuleMor'),
 'FiberedFormedModuleMorphism': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                                 'FiberedFormedModuleMorphism'),
 'FormedModuleMor': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                        'FormedModuleMor'),
 'FormedModuleMorphism': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                          'FormedModuleMorphism'),
 'FormEmbedding': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                   'FormEmbedding'),
 'FormModules': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                 'FormModules'),
 'FreeFormModules': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                     'FreeFormModules'),
 'PairedModules': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                   'PairedModules'),
 'QuadraticFormModules': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                          'QuadraticFormModules'),
 'SymmetricBilinearFormModules': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                                  'SymmetricBilinearFormModules'),
 'TorsionBilinearFormModules': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                                'TorsionBilinearFormModules'),
 'TorsionFormIsometry': ('dzack_research.preamble.categories.modules.framed.formed.torsion_form_modules',
                         'TorsionFormIsometry'),
 'TorsionQuadraticFormModules': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                                 'TorsionQuadraticFormModules')}

__all__ = [
 'BilinearFormModules',
 'DiscriminantBilinearModules',
 'DiscriminantModules',
 'DiscriminantQuadraticModules',
 'FormEmbedding',
 'FormedModuleMor',
 'FormedModuleMorphism',
 'FiberedFormedModuleMor',
 'FiberedFormedModuleMorphism',
 'FormModules',
 'FreeFormModules',
 'PairedModules',
 'QuadraticFormModules',
 'SymmetricBilinearFormModules',
 'TorsionBilinearFormModules',
 'TorsionFormIsometry',
 'TorsionQuadraticFormModules']

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
