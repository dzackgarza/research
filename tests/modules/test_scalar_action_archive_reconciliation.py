r"""Archive reconciliation for modules constructed from a chosen scalar action.

The archived ``module_over_ring(rho)`` wrapper represented the mathematical
construction of an ``R``-module from a ring morphism
``rho : R -> End_Ab(M)``.  The sanctioned live constructor is
``Modules(R)(M, rho)`` (or ``Modules(R)(rho)``): it recovers the acted-on
additive object from the endomorphism ring and retains ``rho`` as the module's
actual scalar action.
"""

from dzack_research.preamble.all import ZZ, FreeModule, Modules
from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/pure/scalar_actions.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/pure/modules.py",
    "disposition": "reconciled-live-owner",
}


def test_module_constructor_recovers_the_underlying_object_from_the_action() -> None:
    line = FreeModule(ZZ, 1)
    endomorphisms = Modules(ZZ).End(line)
    generator = line.module_generator(0)

    def multiplication_by(scalar):
        scalar = ZZ(scalar)
        return endomorphisms({0: line.scalar_multiple(scalar, generator)})

    action = ring_morphism(ZZ, endomorphisms, multiplication_by)
    explicit = Modules(ZZ)(line, action)
    inferred = Modules(ZZ)(action)

    assert explicit in Modules(ZZ)
    assert inferred in Modules(ZZ)
    assert explicit.scalar_action() is action
    assert inferred.scalar_action() is action
    assert action.codomain().domain() is line


def test_scalar_multiplication_is_evaluation_of_the_chosen_action() -> None:
    line = FreeModule(ZZ, 1)
    endomorphisms = Modules(ZZ).End(line)
    generator = line.module_generator(0)

    action = ring_morphism(
        ZZ,
        endomorphisms,
        lambda scalar: endomorphisms(
            {0: line.scalar_multiple(ZZ(scalar), generator)}
        ),
    )
    acted = Modules(ZZ)(line, action)
    element = acted(line.scalar_multiple(ZZ(3), generator))

    assert acted.scalar_multiple(ZZ(-2), element) == acted(
        action(ZZ(-2))(line.scalar_multiple(ZZ(3), generator))
    )
    assert acted.scalar_action()(ZZ(5))(line.scalar_multiple(ZZ(3), generator)) == (
        line.scalar_multiple(ZZ(15), generator)
    )
