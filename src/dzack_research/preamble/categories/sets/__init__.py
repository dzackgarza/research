"""Lazy public aggregation for owned Set-side constructions.

The defining modules must remain independently importable. Python executes a
package ``__init__`` before any submodule, so eager re-exports here create
defining-module cycles: ``abstract_categories.mor_categories`` imports
``sets.indexed_families`` at module level, which runs this file first, and
every set module imports ``mor_categories`` back while it is only partly
initialized.  Public names are resolved lazily until that module-level edge is
removed at its owner.
"""

from importlib import import_module as _import_module

_EXPORTS = {'CountableSets': ('dzack_research.preamble.categories.sets.set_categories', 'CountableSets'),
 'CountablyInfiniteSets': ('dzack_research.preamble.categories.sets.set_categories',
                           'CountablyInfiniteSets'),
 'FiniteSets': ('dzack_research.preamble.categories.sets.set_categories', 'FiniteSets'),
 'FinitelySupportedFunctionSets': ('dzack_research.preamble.categories.sets.set_categories',
                                   'FinitelySupportedFunctionSets'),
 'InfiniteSets': ('dzack_research.preamble.categories.sets.set_categories', 'InfiniteSets'),
 'NN': ('dzack_research.preamble.categories.sets.set_categories', 'NN'),
 'PartiallyOrderedSets': ('dzack_research.preamble.categories.sets.set_categories',
                          'PartiallyOrderedSets'),
 'Sets': ('dzack_research.preamble.categories.sets.set_categories', 'Sets'),
 'TotallyOrderedSets': ('dzack_research.preamble.categories.sets.set_categories',
                        'TotallyOrderedSets'),
 'UncountableSets': ('dzack_research.preamble.categories.sets.set_categories', 'UncountableSets'),
 'register_set_axioms': ('dzack_research.preamble.categories.sets.set_categories',
                         'register_set_axioms'),
 'PowerSets': ('dzack_research.preamble.categories.sets.set_categories', 'PowerSets'),
 'ObjectSetsOfDiscreteCategories': ('dzack_research.preamble.categories.sets.set_categories',
                                    'ObjectSetsOfDiscreteCategories'),
 'FinitePowerSets': ('dzack_research.preamble.categories.sets.set_categories', 'FinitePowerSets'),
 'DisjointUnionsOfSets': ('dzack_research.preamble.categories.sets.set_categories',
                          'DisjointUnionsOfSets'),
 'CoproductsOfSets': ('dzack_research.preamble.categories.sets.set_categories', 'CoproductsOfSets'),
 'CartesianProductsOfSets': ('dzack_research.preamble.categories.sets.set_categories',
                             'CartesianProductsOfSets'),
 'Set': ('dzack_research.preamble.categories.sets.set_categories', 'Set'),
 'SetInclusion': ('dzack_research.preamble.categories.sets.set_categories', 'SetInclusion'),
 'SetInjection': ('dzack_research.preamble.categories.sets.set_categories', 'SetInjection'),
 'SetSurjection': ('dzack_research.preamble.categories.sets.set_categories', 'SetSurjection'),
 'CardinalComparison': ('dzack_research.preamble.categories.sets.cardinals', 'CardinalComparison'),
 'Cardinalities': ('dzack_research.preamble.categories.sets.cardinals', 'Cardinalities'),
 'OrdinalSemirings': ('dzack_research.preamble.categories.sets.cardinals', 'OrdinalSemirings'),
 'Ordinals': ('dzack_research.preamble.categories.sets.cardinals', 'Ordinals'),
 'aleph': ('dzack_research.preamble.categories.sets.cardinals', 'aleph'),
 'aleph0': ('dzack_research.preamble.categories.sets.cardinals', 'aleph0'),
 'cardinal': ('dzack_research.preamble.categories.sets.cardinals', 'cardinal'),
 'continuum': ('dzack_research.preamble.categories.sets.cardinals', 'continuum'),
 'omega': ('dzack_research.preamble.categories.sets.cardinals', 'omega'),
 'omega0': ('dzack_research.preamble.categories.sets.cardinals', 'omega0'),
 'ordinal': ('dzack_research.preamble.categories.sets.cardinals', 'ordinal'),
 'EnumeratedByIntegers': ('dzack_research.preamble.categories.sets.enumerated',
                          'EnumeratedByIntegers'),
 'EnumeratedByNaturals': ('dzack_research.preamble.categories.sets.enumerated',
                          'EnumeratedByNaturals'),
 'EnumeratedSets': ('dzack_research.preamble.categories.sets.enumerated', 'EnumeratedSets'),
 'FourierCharacters': ('dzack_research.preamble.categories.sets.enumerated', 'FourierCharacters'),
 'FunctionEnumeratedSets': ('dzack_research.preamble.categories.sets.enumerated',
                            'FunctionEnumeratedSets'),
 'HermitePolynomials': ('dzack_research.preamble.categories.sets.enumerated', 'HermitePolynomials'),
 'LaurentMonomials': ('dzack_research.preamble.categories.sets.enumerated', 'LaurentMonomials'),
 'SincTranslates': ('dzack_research.preamble.categories.sets.enumerated', 'SincTranslates'),
 'FixedSizeSelectionElement': ('dzack_research.preamble.categories.sets.fixed_size_selections',
                               'FixedSizeSelectionElement'),
 'FixedSizeSelections': ('dzack_research.preamble.categories.sets.fixed_size_selections',
                         'FixedSizeSelections'),
 'IndexedFamily': ('dzack_research.preamble.categories.sets.indexed_families', 'IndexedFamily'),
 'finite_indexed_family': ('dzack_research.preamble.categories.sets.indexed_families',
                           'finite_indexed_family'),
 'indexed_family': ('dzack_research.preamble.categories.sets.indexed_families', 'indexed_family'),
 'FiniteOrderedSets': ('dzack_research.preamble.categories.sets.finite_ordered_sets',
                       'FiniteOrderedSets'),
 'OrderedEnumeratedSets': ('dzack_research.preamble.categories.sets.finite_ordered_sets',
                           'OrderedEnumeratedSets'),
 'finite_ordered_set': ('dzack_research.preamble.categories.sets.finite_ordered_sets',
                        'finite_ordered_set')}

__all__ = [ 'PowerSets',
 'ObjectSetsOfDiscreteCategories',
 'FinitePowerSets',
 'DisjointUnionsOfSets',
 'CoproductsOfSets',
 'CartesianProductsOfSets',
 'register_set_axioms',
 'UncountableSets',
 'TotallyOrderedSets',
 'PartiallyOrderedSets',
 'InfiniteSets',
 'NN',
 'FinitelySupportedFunctionSets',
 'FiniteSets',
 'FixedSizeSelectionElement',
 'FixedSizeSelections',
 'CountablyInfiniteSets',
 'CountableSets',
 'Sets',
 'Set',
 'SetInclusion',
 'SetInjection',
 'SetSurjection',
 'CardinalComparison',
 'Cardinalities',
 'OrdinalSemirings',
 'Ordinals',
 'aleph',
 'aleph0',
 'cardinal',
 'continuum',
 'omega',
 'omega0',
 'ordinal',
 'EnumeratedByIntegers',
 'EnumeratedByNaturals',
 'EnumeratedSets',
 'FiniteOrderedSets',
 'OrderedEnumeratedSets',
 'FourierCharacters',
 'FunctionEnumeratedSets',
 'HermitePolynomials',
 'IndexedFamily',
 'LaurentMonomials',
 'SincTranslates',
 'finite_indexed_family',
 'finite_ordered_set',
 'indexed_family']

def __getattr__(name):
    if name not in _EXPORTS:
        raise AttributeError(name)
    module_name, attribute = _EXPORTS[name]
    value = getattr(_import_module(module_name), attribute)
    globals()[name] = value
    return value

def __dir__():
    return sorted((*globals(), *__all__))
