r"""The callable frontier for genuinely unframed infinite modules.

Two Python callables can define the same linear map without carrying a finite
presentation on which equality can be decided.  The Hom owner must retain that
boundary: construction is permitted as a declared elementwise linear map, but
equality is refused rather than guessed from callable identity or a finite
sample.
"""

from sage.misc.unknown import Unknown

from dzack_research.preamble.all import ZZ, GeneralModules, Set


def _unframed_integer_module():
    return GeneralModules(ZZ).from_operations(
        Set(ZZ),
        addition=lambda left, right: left + right,
        zero=ZZ.zero(),
        negation=lambda value: -value,
        scalar_action=lambda scalar, value: scalar * value,
    )


def test_extensionally_equal_callable_maps_do_not_acquire_a_false_equality_decision() -> None:
    module = _unframed_integer_module()
    homset = module.module_category().Mor(module, module)
    first = homset.elementwise(lambda element: element, verify_linearity=False)
    second = homset.elementwise(
        lambda element: module(element.underlying_element()),
        verify_linearity=False,
    )

    assert first(module(ZZ(7))) == second(module(ZZ(7)))
    assert (first == second) is Unknown
