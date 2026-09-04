import pytest

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras import SymmetricAlgebraOn
from dzack_research.preamble.categories.modules import (
    BasedFreeModule,
    Connections,
    DifferentialGradedModules,
    ModuleWithConnection,
    ModulesWithFlatConnection,
    ModulesWithConnection,
    connection_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.static_types import (
    coefficient_form_view,
    covariant_d,
    flat_connection_view,
)


def test_connection_extends_by_leibniz_and_curvature_detects_nonflatness() -> None:
    algebra = SymmetricAlgebraOn(QQ, ("x", "y"))
    x = algebra.algebra_generator("x")
    module = BasedFreeModule(algebra, finite_ordered_set(("e",)))
    space = Connections(module)
    omega = space.one_forms()
    e = module.module_generator("e")
    dx = omega.differential_generator("x")

    trivial = space({"e": space.target_module().zero()})
    assert trivial(module.scalar_multiple(x, e)) == space.target_module().pure_tensor(e, dx)
    assert trivial.is_flat()

    dy = omega.differential_generator("y")
    nonflat = space(
        {
            "e": space.target_module().pure_tensor(
                e,
                omega.scalar_multiple(x, dy),
            )
        }
    )
    assert not nonflat.is_flat()
    assert nonflat.curvature_on_generator("e") != nonflat.curvature_target().zero()


def test_connection_modules_are_distinct_structured_objects_with_horizontal_homs() -> None:
    algebra = SymmetricAlgebraOn(QQ, ("x",))
    module = BasedFreeModule(algebra, finite_ordered_set(("e",)))
    zero_space = Connections(module)
    zero_connection = zero_space({"e": zero_space.target_module().zero()})
    structured = ModuleWithConnection(zero_connection)

    assert structured is not module
    assert structured in ModulesWithConnection(algebra)
    assert structured in ModulesWithFlatConnection(algebra)
    assert structured.connection().is_flat()
    identity = connection_homset(structured, structured).identity()
    assert identity(structured.module_generator("e")) == structured.module_generator("e")

    nonzero_source = BasedFreeModule(algebra, finite_ordered_set(("e",)))
    nonzero_space = Connections(nonzero_source)
    dx = nonzero_space.one_forms().differential_generator("x")
    nonzero = nonzero_space(
        {
            "e": nonzero_space.target_module().pure_tensor(
                nonzero_source.module_generator("e"),
                dx,
            )
        }
    )
    other = ModuleWithConnection(nonzero)
    with pytest.raises(ValueError, match="not horizontal"):
        connection_homset(structured, other)(
            {"e": other.module_generator("e")}
        )


def test_flat_connection_builds_the_de_rham_dg_module() -> None:
    algebra = SymmetricAlgebraOn(QQ, ("x",))
    x = algebra.algebra_generator("x")
    module = BasedFreeModule(algebra, finite_ordered_set(("e",)))
    space = Connections(module)
    dx = space.one_forms().differential_generator("x")
    connection = space(
        {
            "e": space.target_module().pure_tensor(
                module.module_generator("e"),
                dx,
            )
        }
    )
    assert connection.is_flat()

    dg_module = connection.de_rham_module()
    dga = dg_module.dga()
    e = dg_module.from_coefficient(module.module_generator("e"))
    X = dga.from_degree_zero(x)

    assert dg_module in DifferentialGradedModules(dga)
    assert dg_module.d(dg_module.d(e)) == dg_module.zero()
    assert dg_module.d(dg_module.act(e, X)) == (
        dg_module.act(dg_module.d(e), X)
        + dg_module.act(e, dga.d(X))
    )

    viewed_connection = flat_connection_view(connection)
    viewed_coefficient = coefficient_form_view(e)
    assert covariant_d(viewed_connection, viewed_coefficient) == dg_module.d(e)


def test_connection_on_countable_free_module_keeps_callable_generator_family_lazy() -> None:
    from dzack_research.preamble.categories.modules import FreeModuleOn
    from dzack_research.preamble.categories.sets import NN

    algebra = SymmetricAlgebraOn(QQ, ("t",))
    module = FreeModuleOn(algebra, NN)
    connection_space = Connections(module)
    connection = connection_space(
        lambda _label: connection_space.target_module().zero()
    )

    e1000 = module.module_generator(NN(1000))
    assert connection.generator_image(NN(1000)) == connection_space.target_module().zero()
    assert connection(e1000) == connection_space.target_module().zero()
    with pytest.raises(NotImplementedError, match="finite framing"):
        connection.is_flat()
