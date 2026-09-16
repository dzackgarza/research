from sage.categories.homset import Homset

import pytest

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.modules import (
    DifferentialGradedModules,
    Modules,
    ModulesWithFlatConnection,
    ModulesWithConnection,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.static_types import (
    coefficient_form_view,
    covariant_d,
    flat_connection_view,
)


def test_connection_extends_by_leibniz_and_curvature_detects_nonflatness() -> None:
    algebra = QQ.free_module(("x", "y")).symmetric_algebra()
    x = algebra.algebra_generator("x")
    module = algebra.free_module(finite_ordered_set(("e",)))
    space = module.connections()
    assert space is module.connections()
    omega = space.one_forms()
    e = module.module_generator("e")
    dx = omega.differential_generator("x")

    trivial = space({"e": space.target_module().zero()})
    module_morphisms = Modules(QQ).Mor(
        space.restricted_source_module(), space.restricted_target_module()
    )
    assert not isinstance(space, Homset)
    assert space.arrow_set() is module_morphisms
    assert module_morphisms in space.super_categories()
    assert trivial.as_morphism().parent() is module_morphisms
    assert trivial.as_morphism() in space
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
    algebra = QQ.free_module(("x",)).symmetric_algebra()
    module = algebra.free_module(finite_ordered_set(("e",)))
    zero_space = module.connections()
    zero_connection = zero_space({"e": zero_space.target_module().zero()})
    structured = ModulesWithConnection(algebra)(zero_connection)

    assert structured is not module
    assert structured in ModulesWithConnection(algebra)
    assert structured.connection_construction().source_connection() is zero_connection
    underlying_connection = zero_connection.underlying_linear_morphism()
    assert underlying_connection.connection() is zero_connection
    assert zero_space(underlying_connection) is zero_connection
    assert structured.connection().parent() is structured.connections()
    assert structured in ModulesWithFlatConnection(algebra)
    assert structured.connection().is_flat()
    horizontal_maps = structured.Mor(structured)
    module_morphisms = Modules(algebra).Mor(structured, structured)
    identity = horizontal_maps.identity()
    assert not isinstance(horizontal_maps, Homset)
    assert horizontal_maps.arrow_set() is module_morphisms
    assert module_morphisms in horizontal_maps.super_categories()
    assert identity.as_morphism().parent() is module_morphisms
    assert identity.as_morphism().connection_morphism() is identity
    assert horizontal_maps(identity.as_morphism()) is identity
    assert identity.as_morphism() in horizontal_maps
    assert identity(structured.module_generator("e")) == structured.module_generator("e")

    nonzero_source = algebra.free_module(finite_ordered_set(("e",)))
    nonzero_space = nonzero_source.connections()
    dx = nonzero_space.one_forms().differential_generator("x")
    nonzero = nonzero_space(
        {
            "e": nonzero_space.target_module().pure_tensor(
                nonzero_source.module_generator("e"),
                dx,
            )
        }
    )
    other = ModulesWithConnection(algebra)(nonzero)
    with pytest.raises(ValueError, match="not horizontal"):
        structured.Mor(other)(
            {"e": other.module_generator("e")}
        )


def test_flat_connection_builds_the_de_rham_dg_module() -> None:
    algebra = QQ.free_module(("x",)).symmetric_algebra()
    x = algebra.algebra_generator("x")
    module = algebra.free_module(finite_ordered_set(("e",)))
    space = module.connections()
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
    from dzack_research.preamble.categories.sets import NN

    algebra = QQ.free_module(("t",)).symmetric_algebra()
    module = algebra.free_module(NN)
    connection_space = module.connections()
    connection = connection_space(
        lambda _label: connection_space.target_module().zero()
    )

    e1000 = module.module_generator(NN(1000))
    assert connection.generator_image(NN(1000)) == connection_space.target_module().zero()
    assert connection(e1000) == connection_space.target_module().zero()
    with pytest.raises(AssertionError, match="finite framing"):
        connection.is_flat()
