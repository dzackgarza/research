from sage.categories.homset import Homset


from dzack_research.preamble.all import QQ, ZZ
from dzack_research.preamble.categories.modules import (
    CochainComplexes,
    DifferentialGradedModules,
    Modules,
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
    assert dg_module in CochainComplexes(QQ)
    assert dg_module.connection() is connection
    assert dg_module.degree_index_set() is ZZ
    assert dg_module.d(dg_module.d(e)) == dg_module.zero()
    assert dg_module.d(dg_module.act(e, X)) == (
        dg_module.act(dg_module.d(e), X)
        + dg_module.act(e, dga.d(X))
    )

    viewed_connection = flat_connection_view(connection)
    viewed_coefficient = coefficient_form_view(e)
    assert covariant_d(viewed_connection, viewed_coefficient) == dg_module.d(e)


