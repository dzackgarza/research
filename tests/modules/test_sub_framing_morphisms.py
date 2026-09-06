r"""The inclusion of a free module on part of another module's framing.

The free module functor turns an injection of framing sets into a split
monomorphism, and both the question of lying in its image and the lift are
then decided on labels: an element of the larger module comes from the
smaller one exactly when it is supported on the smaller framing, with the
same coefficients.  Nothing is solved and no matrix is formed, which is what
makes the construction available when the smaller framing is infinite.
"""

from dzack_research.preamble.all import (
    BasedFreeModule,
    ZZ,
    sub_framing_morphism,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _inclusion():
    r"""Return the inclusion of the free module on ``a, c`` into the one on ``a, b, c``."""
    small = BasedFreeModule(ZZ, finite_ordered_set(("a", "c")))
    large = BasedFreeModule(ZZ, finite_ordered_set(("a", "b", "c")))
    return small, large, sub_framing_morphism(small, large)


def test_the_inclusion_carries_each_generator_to_its_namesake() -> None:
    small, large, inclusion = _inclusion()

    assert inclusion(small.module_generator("a")) == large.module_generator("a")
    assert inclusion(small.module_generator("c")) == large.module_generator("c")
    assert inclusion.is_injective()


def test_an_element_supported_on_the_smaller_framing_lifts_back() -> None:
    small, large, inclusion = _inclusion()
    element = 2 * large.module_generator("a") + 3 * large.module_generator("c")

    assert inclusion.is_in_image(element)
    assert inclusion(inclusion.lift(element)) == element
    assert inclusion.lift(element) == 2 * small.module_generator(
        "a"
    ) + 3 * small.module_generator("c")


def test_a_generator_outside_the_smaller_framing_is_not_in_the_image() -> None:
    _, large, inclusion = _inclusion()

    assert not inclusion.is_in_image(large.module_generator("b"))
