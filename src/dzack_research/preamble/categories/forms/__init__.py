'Forms and their coordinate presentations.'

from importlib import import_module as _import_module

_EXPORTS = {'BilinearFormHomset': ('dzack_research.preamble.categories.forms.forms', 'BilinearFormHomset'),
 'BilinearFormMorphism': ('dzack_research.preamble.categories.forms.forms', 'BilinearFormMorphism'),
 'PairingMorphism': ('dzack_research.preamble.categories.forms.forms', 'PairingMorphism'),
 'QuadraticFormHomset': ('dzack_research.preamble.categories.forms.forms', 'QuadraticFormHomset'),
 'QuadraticMapMorphism': ('dzack_research.preamble.categories.forms.forms', 'QuadraticMapMorphism'),
 'QuadraticFormMorphism': ('dzack_research.preamble.categories.forms.forms',
                           'QuadraticFormMorphism'),
 'classifying_morphism': ('dzack_research.preamble.categories.forms.forms', 'classifying_morphism'),
 'GramTensorGraph': ('dzack_research.preamble.categories.forms.gram_matrices',
                     'GramTensorGraph'),
}

__all__ = ['BilinearFormMorphism',
 'BilinearFormHomset',
 'PairingMorphism',
 'QuadraticFormHomset',
 'QuadraticMapMorphism',
 'QuadraticFormMorphism',
 'GramTensorGraph',
 'classifying_morphism',
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
