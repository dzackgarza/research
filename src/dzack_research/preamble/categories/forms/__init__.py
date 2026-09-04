'Forms and their coordinate presentations.'

from importlib import import_module as _import_module

_EXPORTS = {'BilinearFormHomset': ('dzack_research.preamble.categories.forms.forms', 'BilinearFormHomset'),
 'BilinearFormMorphism': ('dzack_research.preamble.categories.forms.forms', 'BilinearFormMorphism'),
 'BilinearForms': ('dzack_research.preamble.categories.forms.forms', 'BilinearForms'),
 'PairingMorphism': ('dzack_research.preamble.categories.forms.forms', 'PairingMorphism'),
 'Pairings': ('dzack_research.preamble.categories.forms.forms', 'Pairings'),
 'QuadraticFormHomset': ('dzack_research.preamble.categories.forms.forms', 'QuadraticFormHomset'),
 'QuadraticMap': ('dzack_research.preamble.categories.forms.forms', 'QuadraticMap'),
 'QuadraticMapMorphism': ('dzack_research.preamble.categories.forms.forms', 'QuadraticMapMorphism'),
 'QuadraticFormMorphism': ('dzack_research.preamble.categories.forms.forms',
                           'QuadraticFormMorphism'),
 'QuadraticForms': ('dzack_research.preamble.categories.forms.forms', 'QuadraticForms'),
 'classifying_morphism': ('dzack_research.preamble.categories.forms.forms', 'classifying_morphism'),
 'is_bilinear_form': ('dzack_research.preamble.categories.forms.forms', 'is_bilinear_form'),
 'is_quadratic_form': ('dzack_research.preamble.categories.forms.forms', 'is_quadratic_form'),
 'quadratic_map_from_morphism': ('dzack_research.preamble.categories.forms.forms',
                                 'quadratic_map_from_morphism'),
 'BilinearForm': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                  'BilinearForm'),
 'QuadraticForm': ('dzack_research.preamble.categories.modules.framed.formed.form_modules',
                   'QuadraticForm'),
 'gram_tensor_from_graph': ('dzack_research.preamble.categories.forms.gram_matrices',
                            'gram_tensor_from_graph'),
 'gram_tensor_graph': ('dzack_research.preamble.categories.forms.gram_matrices',
                       'gram_tensor_graph'),
 'tensor_connected_component_cuts': ('dzack_research.preamble.categories.forms.gram_matrices',
                                     'tensor_connected_component_cuts')}

__all__ = ['BilinearFormMorphism',
 'BilinearFormHomset',
 'BilinearForm',
 'BilinearForms',
 'PairingMorphism',
 'Pairings',
 'QuadraticForm',
 'QuadraticFormHomset',
 'QuadraticMap',
 'QuadraticMapMorphism',
 'QuadraticFormMorphism',
 'QuadraticForms',
 'classifying_morphism',
 'is_bilinear_form',
 'is_quadratic_form',
 'quadratic_map_from_morphism',
 'gram_tensor_from_graph',
 'gram_tensor_graph',
 'tensor_connected_component_cuts']

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
