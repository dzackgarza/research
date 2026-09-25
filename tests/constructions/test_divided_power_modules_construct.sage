r"""Divided powers of a module retain their ambient divided-power algebra.

For a free module ``M``, ``Gamma^2(M)`` is the homogeneous degree-two part of
``Gamma(M)``.  Its distinguished divided powers are elements of that module and
the module remembers the ambient graded algebra containing them.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_second_divided_power_remembers_the_ambient_power_algebra() -> None:
    module = ZZ.free_module(2)
    divided = module.divided_power_module(2)
    algebra = module.divided_power_algebra()
    square = module.divided_power_element(2, module.module_generator(0))

    assert divided in Modules(ZZ)
    assert divided.ambient_power_algebra() is algebra
    assert square in divided
    assert isinstance(square, divided.ElementType)


def test_divided_power_module_morphisms_have_identity() -> None:
    divided = ZZ.free_module(2).divided_power_module(2)
    identity = divided.Mor(divided).identity()

    assert identity(divided.zero()) == divided.zero()
    assert identity * identity == identity
