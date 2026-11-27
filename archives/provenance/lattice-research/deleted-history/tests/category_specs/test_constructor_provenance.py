"""Constructor discovery and provenance route checks.

This test suite verifies that constructor discovery through ``Cat().Constructors()``
keeps an owner route for the ``Rings`` entry points, not just plain method names.
"""

from __future__ import annotations

import importlib

importlib.import_module("sage.all")
importlib.import_module("category_specs")

from sage.all import QQ, ZZ  # noqa: E402

from category_specs.algebras import Algebras  # noqa: E402
from category_specs.cat import Cat  # noqa: E402
from category_specs.lattices import Lattices  # noqa: E402
from category_specs.modules import Modules  # noqa: E402
from category_specs.posets import Posets  # noqa: E402
from category_specs.rings import Rings  # noqa: E402
from category_specs.sets import Sets  # noqa: E402
from category_specs.spec_core import ConstructorRegistry  # noqa: E402
from category_specs.tensor_algebra_components import (  # noqa: E402
    TensorAlgebraComponents,
)
from category_specs.topological_spaces import TopologicalSpaces  # noqa: E402

_CONSTRUCTOR_METADATA_NAMES = frozenset(
    {"base_ring", "category", "names", "provenance"}
)


def _constructor_names(collector_type: type) -> list[str]:
    return sorted(
        name
        for name in dir(collector_type)
        if not name.startswith("_")
        and callable(getattr(collector_type, name, None))
        and name[0].isupper()
    )


def _public_constructor_methods(collector_type: type) -> tuple[str, ...]:
    return tuple(
        name
        for name, value in collector_type.__dict__.items()
        if not name.startswith("_")
        and name not in _CONSTRUCTOR_METADATA_NAMES
        and name.isidentifier()
        and callable(value)
        and not getattr(value, "_cat_constructor_generated_forwarder", False)
    )


def test_cat_constructor_forwarders_expose_rings_owner_route() -> None:
    cat_constructors = Cat().Constructors()
    ring_constructors = Rings().Constructors()

    ring_constructor_methods = _constructor_names(type(ring_constructors))
    cat_rings_methods = [
        name
        for name in dir(type(cat_constructors))
        if name.startswith("rings_") and not name.startswith("rings__")
        and callable(getattr(type(cat_constructors), name, None))
    ]

    # Use a focused set so this test stays anchored to a stable surface.
    for constructor_name in ("ZZ", "QQ", "IntegerModRing"):
        expected = f"rings_{constructor_name}"
        assert expected in cat_rings_methods
        forwarder = getattr(type(cat_constructors), expected)

        assert getattr(forwarder, "_cat_constructor_generated_forwarder", False) is True
        assert (
            forwarder.__doc__
            == f"Forward to ``rings.Constructors().{constructor_name}``."
        )
        assert forwarder.__qualname__ == f"Cat.Constructors.{expected}"

    # Round-trip check confirms the route resolves to the owner namespace.
    assert cat_constructors.rings_ZZ() == ring_constructors.ZZ()
    assert cat_constructors.rings_QQ() == ring_constructors.QQ()
    assert (
        cat_constructors.rings_PolynomialRing(ring_constructors.QQ(), name="x")
        == ring_constructors.PolynomialRing(ring_constructors.QQ(), name="x")
    )

    # At least all registered ring constructors are discoverable through Cat.
    assert all(
        f"rings_{name}" in cat_rings_methods for name in ring_constructor_methods
    )
    assert "rings_provenance" not in cat_rings_methods


def test_constructor_surfaces_expose_typed_provenance_records() -> None:
    ring_registry = Rings().Constructors().provenance()
    module_registry = Modules(QQ).Constructors().provenance()
    set_registry = Sets().Constructors().provenance()
    algebra_registry = Algebras(QQ).Constructors().provenance()
    poset_registry = Posets().Constructors().provenance()
    topology_registry = TopologicalSpaces().Constructors().provenance()
    tensor_registry = TensorAlgebraComponents(QQ).Constructors().provenance()
    lattice_registry = Lattices(ZZ).Constructors().provenance()
    cat_registry = Cat().Constructors().provenance()

    assert isinstance(ring_registry, ConstructorRegistry)
    assert isinstance(module_registry, ConstructorRegistry)
    assert isinstance(set_registry, ConstructorRegistry)
    assert isinstance(algebra_registry, ConstructorRegistry)
    assert isinstance(poset_registry, ConstructorRegistry)
    assert isinstance(topology_registry, ConstructorRegistry)
    assert isinstance(tensor_registry, ConstructorRegistry)
    assert isinstance(lattice_registry, ConstructorRegistry)
    assert isinstance(cat_registry, ConstructorRegistry)

    ring_zz = ring_registry.constructor("rings.ZZ")
    assert ring_zz.owner_category == "Rings()"
    assert ring_zz.method_name == "ZZ"
    assert ring_zz.sage_entry_point.endswith("Rings._Constructors.ZZ")
    assert ring_zz.target_refinement_route == ("Rings()", "Ring")

    polynomial_ring = ring_registry.constructor("rings.PolynomialRing")
    assert polynomial_ring.method_name == "PolynomialRing"
    assert polynomial_ring.sage_source.endswith("Rings._Constructors.PolynomialRing")
    assert polynomial_ring.target_category == "Ring"

    free_module = module_registry.constructor("modules.FreeModule")
    assert free_module.owner_category == f"Modules({QQ})"
    assert free_module.method_name == "FreeModule"
    assert free_module.sage_entry_point.endswith("Modules._Constructors.FreeModule")
    assert free_module.target_refinement_route == (f"Modules({QQ})", "RModule")

    finite_set = set_registry.constructor("sets.FiniteEnumeratedSet")
    assert finite_set.owner_category == "Sets()"
    assert finite_set.method_name == "FiniteEnumeratedSet"
    assert finite_set.target_category == "FiniteSet"

    free_algebra = algebra_registry.constructor("algebras.free_algebra_from_set")
    assert free_algebra.owner_category == f"Algebras({QQ})"
    assert free_algebra.sage_source.endswith(
        "Algebras._Constructors.free_algebra_from_set"
    )

    poset = poset_registry.constructor("posets.from_digraph")
    assert poset.owner_category == "Posets()"
    assert poset.method_name == "from_digraph"
    assert poset.target_category == "Poset"

    tensor = tensor_registry.constructor("tensor_algebra_components.component_module")
    assert tensor.owner_category == f"TensorAlgebraComponents({QQ})"
    assert tensor.method_name == "component_module"
    assert tensor.target_category == "TensorAlgebraComponent"

    assert topology_registry.constructors == ()

    integral_lattice = lattice_registry.constructor("lattices.IntegralLattice")
    assert integral_lattice.owner_category == f"Lattices({ZZ})"
    assert integral_lattice.method_name == "IntegralLattice"
    assert integral_lattice.sage_entry_point.endswith(
        "LatticesCategory._Constructors.IntegralLattice"
    )
    assert integral_lattice.target_refinement_route[0] == f"Lattices({ZZ})"

    direct_sum = lattice_registry.constructor("lattices.IntegralLatticeDirectSum")
    assert direct_sum.owner_category == f"Lattices({ZZ})"
    assert direct_sum.method_name == "IntegralLatticeDirectSum"
    assert direct_sum.sage_entry_point.endswith(
        "LatticesCategory._Constructors.IntegralLatticeDirectSum"
    )

    gluing = lattice_registry.constructor("lattices.IntegralLatticeGluing")
    assert gluing.owner_category == f"Lattices({ZZ})"
    assert gluing.method_name == "IntegralLatticeGluing"
    assert gluing.sage_entry_point.endswith(
        "LatticesCategory._Constructors.IntegralLatticeGluing"
    )

    cat_ring_zz = cat_registry.constructor("cat.rings.ZZ")
    assert cat_ring_zz.owner_category == "Rings()"
    assert cat_ring_zz.method_name == "rings_ZZ"
    assert cat_ring_zz.target_refinement_route == (
        "Cat().Constructors()",
        "Rings().Constructors()",
        "Ring",
    )
    cat_free_module = cat_registry.constructor("cat.modules_rational_field.FreeModule")
    assert cat_free_module.method_name == "modules_rational_field_FreeModule"
    assert cat_registry.constructor("cat.sets.FiniteEnumeratedSet").method_name == (
        "sets_FiniteEnumeratedSet"
    )
    cat_free_algebra = cat_registry.constructor(
        "cat.algebras_rational_field.free_algebra_from_set"
    )
    assert (
        cat_free_algebra.method_name
        == "algebras_rational_field_free_algebra_from_set"
    )
    assert cat_registry.constructor("cat.posets.from_digraph").method_name == (
        "posets_from_digraph"
    )
    assert cat_registry.constructor(
        "cat.tensor_algebra_components_rational_field.component_module"
    ).method_name == "tensor_algebra_components_rational_field_component_module"
    assert not cat_registry.has_constructor("cat.rings.provenance")


def test_constructor_registries_cover_every_public_collector_method() -> None:
    collectors = (
        ("rings", Rings().Constructors()),
        ("modules", Modules(QQ).Constructors()),
        ("sets", Sets().Constructors()),
        ("algebras", Algebras(QQ).Constructors()),
        ("posets", Posets().Constructors()),
        ("topological_spaces", TopologicalSpaces().Constructors()),
        ("tensor_algebra_components", TensorAlgebraComponents(QQ).Constructors()),
        ("lattices", Lattices(ZZ).Constructors()),
    )

    for prefix, collector in collectors:
        registry = collector.provenance()
        expected_ids = {
            f"{prefix}.{method_name}"
            for method_name in _public_constructor_methods(type(collector))
        }
        registry_ids = set(registry.constructor_ids)

        assert registry_ids == expected_ids
        assert all(
            hasattr(type(collector), constructor.method_name)
            for constructor in registry.constructors
        )
        assert all(
            constructor.target_refinement_route != (constructor.owner_category,)
            for constructor in registry.constructors
        )
