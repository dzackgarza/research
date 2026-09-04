'Lazy public aggregation for divisors.'

from importlib import import_module as _import_module

_EXPORTS = {'CartierDivisorGroup': ('dzack_research.preamble.categories.divisors.cartier_divisor_groups',
                         'CartierDivisorGroup'),
 'CartierDivisorGroups': ('dzack_research.preamble.categories.divisors.cartier_divisor_groups',
                          'CartierDivisorGroups'),
 'ClassGroup': ('dzack_research.preamble.categories.divisors.class_groups', 'ClassGroup'),
 'ClassGroups': ('dzack_research.preamble.categories.divisors.class_groups', 'ClassGroups'),
 'DivisorGroup': ('dzack_research.preamble.categories.divisors.divisor_groups', 'DivisorGroup'),
 'DivisorGroups': ('dzack_research.preamble.categories.divisors.divisor_groups', 'DivisorGroups'),
 'FormalDivisor': ('dzack_research.preamble.categories.divisors.divisor_groups', 'FormalDivisor'),
 'FormalDivisorGroup': ('dzack_research.preamble.categories.divisors.divisor_groups',
                        'FormalDivisorGroup'),
 'FormalDivisorGroups': ('dzack_research.preamble.categories.divisors.divisor_groups',
                         'FormalDivisorGroups'),
 'PicardGroup': ('dzack_research.preamble.categories.divisors.picard_groups', 'PicardGroup'),
 'PicardGroups': ('dzack_research.preamble.categories.divisors.picard_groups', 'PicardGroups'),
 'WeilDivisorGroup': ('dzack_research.preamble.categories.divisors.weil_divisor_groups',
                      'WeilDivisorGroup'),
 'WeilDivisorGroups': ('dzack_research.preamble.categories.divisors.weil_divisor_groups',
                       'WeilDivisorGroups')}

__all__ = ['CartierDivisorGroup',
 'CartierDivisorGroups',
 'ClassGroup',
 'ClassGroups',
 'DivisorGroup',
 'DivisorGroups',
 'FormalDivisor',
 'FormalDivisorGroup',
 'FormalDivisorGroups',
 'PicardGroup',
 'PicardGroups',
 'WeilDivisorGroup',
 'WeilDivisorGroups']

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
