r"""The machinery does not assume a module is finitely generated.

Finiteness is an axiom, not a fact about modules, and most of what a module
is asked works without it.  These construct modules on a countable framing and
check that the general operations answer -- so that an optimization written
for the finite case shows up here rather than years later.

What is deliberately *not* asked: a rank, a Gram matrix, a finite generating
set.  Those belong to the finitely generated node, and a module that has not
got them should not be expected to answer.
"""

# Sage's namespace first, and the preamble's over it: these tests name
# ``MatrixSpace``, ``RR`` and their fellows, which the preamble does not
# export and a lowered module is not given.
from sage.all import *  # noqa: F401,F403

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import OrderedSet


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from dzack_research.preamble.install import install_preamble

    install_preamble(globals())
    Lattices.install(globals())


def _countable_framing() -> "OrderedSet":
    r"""Return $\Delta[\aleph_0]$, the countable set of generator labels."""
    _ensure_preamble()
    labels: "OrderedSet" = Sets.Δ[Sets.ℵ[0]]
    return labels


def test_a_countably_framed_free_module_is_constructible() -> None:
    r"""$\ZZ^{\infty}$ and $\RR^{\infty}$ are modules like any other."""
    labels = _countable_framing()

    assert labels not in Sets().Finite(), "the framing is the infinite one"
    for ring in (ZZ, RR):
        module = FreeModuleOn(ring, labels)
        assert module.base_ring() is ring
        assert module.module_generating_set() is labels


def test_its_generators_are_a_set_that_need_not_be_counted() -> None:
    r"""Asking for the generators must not require counting them.

    Sage decides an image set's injectivity by asking the codomain for a
    cardinality, which an infinite module has no reason to answer.  A free
    module's framing is injective by construction, so the question is settled
    without counting.
    """
    module = FreeModuleOn(ZZ, _countable_framing())

    module_generators = module.module_generators()
    assert module_generators is not None
    assert module.module_generator(0) in module
    assert module.module_generator(7) in module


def test_elements_add_and_scale_without_a_finite_basis() -> None:
    r"""The module operations are the module's, not the finite basis's."""
    module = FreeModuleOn(ZZ, _countable_framing())
    x = module.module_generator(0)
    y = module.module_generator(5)

    assert x + y == y + x
    assert x + module.zero() == x
    assert (x + y) - y == x
    assert 2 * x == x + x


def test_finiteness_is_an_axiom_the_module_does_not_claim() -> None:
    r"""$\ZZ^{\infty}$ is not finitely generated, and says so by placement."""
    infinite = FreeModuleOn(ZZ, _countable_framing())
    finite = FreeModuleOn(ZZ, Sets.Δ[2])

    assert finite.module_generating_set() in Sets().Finite()
    assert infinite.module_generating_set() not in Sets().Finite()
