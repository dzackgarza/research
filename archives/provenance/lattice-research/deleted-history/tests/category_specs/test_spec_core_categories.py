"""Category hierarchy tests for typed obligation-closure behavior."""

from __future__ import annotations

import importlib

import pytest

importlib.import_module("sage.all")

from category_specs.spec_core import CategorySpec, CategorySpecRegistry  # noqa: E402

_SETS_BASE_OBLIGATION = "sets.category"
_SETS_COUNTABLE_OBLIGATION = "sets.countable"
_SETS_CARTESIAN_PRODUCT_OBLIGATION = "sets.cartesian_product.cardinality"
_MODULE_BASE_OBLIGATION = "modules.base"
_MODULE_FREE_OBLIGATION = "modules.free"
_MODULE_FINITE_RANK_OBLIGATION = "modules.free_finite_rank.cartesian_power_carrier"


def _module_family(base_label: str) -> tuple[CategorySpec, ...]:
    modules = CategorySpec(
        id=f"Modules({base_label})",
        name=f"Modules({base_label})",
        direct_obligation_ids=(_MODULE_BASE_OBLIGATION,),
        super_category_ids=("Sets()",),
    )
    free = CategorySpec(
        id=f"Modules({base_label}).Free()",
        name=f"Modules({base_label}).Free()",
        direct_obligation_ids=(_MODULE_FREE_OBLIGATION,),
        super_category_ids=(f"Modules({base_label})",),
    )
    finite_rank = CategorySpec(
        id=f"Modules({base_label}).Free().FiniteRank()",
        name=f"Modules({base_label}).Free().FiniteRank()",
        direct_obligation_ids=(_MODULE_FINITE_RANK_OBLIGATION,),
        super_category_ids=(
            f"Modules({base_label}).Free()",
            "Sets().CartesianProducts()",
        ),
    )
    return (modules, free, finite_rank)


def _build_registry() -> CategorySpecRegistry:
    return CategorySpecRegistry(
        categories=(
            CategorySpec(
                id="Sets()",
                name="Sets()",
                direct_obligation_ids=(_SETS_BASE_OBLIGATION,),
            ),
            CategorySpec(
                id="Sets().Countable()",
                name="Sets().Countable()",
                direct_obligation_ids=(_SETS_COUNTABLE_OBLIGATION,),
                super_category_ids=("Sets()",),
            ),
            CategorySpec(
                id="Sets().CartesianProducts()",
                name="Sets().CartesianProducts()",
                direct_obligation_ids=(_SETS_CARTESIAN_PRODUCT_OBLIGATION,),
                super_category_ids=("Sets()",),
            ),
            CategorySpec(
                id="Modules(R).Free().FiniteRank()",
                name="Modules(R).Free().FiniteRank()",
                direct_obligation_ids=(_MODULE_FINITE_RANK_OBLIGATION,),
                super_category_ids=(
                    "Modules(R).Free()",
                    "Sets().CartesianProducts()",
                ),
            ),
            CategorySpec(
                id="Modules(R).Free()",
                name="Modules(R).Free()",
                direct_obligation_ids=(_MODULE_FREE_OBLIGATION,),
                super_category_ids=("Modules(R)",),
            ),
            CategorySpec(
                id="Modules(R)",
                name="Modules(R)",
                direct_obligation_ids=(_MODULE_BASE_OBLIGATION,),
                super_category_ids=("Sets()",),
            ),
            *_module_family("GF(5)"),
            *_module_family("ZZ"),
        ),
        obligation_ids=(
            _SETS_BASE_OBLIGATION,
            _SETS_COUNTABLE_OBLIGATION,
            _SETS_CARTESIAN_PRODUCT_OBLIGATION,
            _MODULE_BASE_OBLIGATION,
            _MODULE_FREE_OBLIGATION,
            _MODULE_FINITE_RANK_OBLIGATION,
        ),
    )


def test_inherited_closure_includes_upstream_obligations_without_duplicates() -> None:
    registry = _build_registry()
    inherited = registry.inherited_obligation_ids("Modules(GF(5)).Free().FiniteRank()")

    assert inherited == (
        _SETS_BASE_OBLIGATION,
        _MODULE_BASE_OBLIGATION,
        _MODULE_FREE_OBLIGATION,
        _SETS_CARTESIAN_PRODUCT_OBLIGATION,
        _MODULE_FINITE_RANK_OBLIGATION,
    )
    assert len(inherited) == len(set(inherited))
    assert _MODULE_FINITE_RANK_OBLIGATION in inherited
    assert inherited[-1] == _MODULE_FINITE_RANK_OBLIGATION
    assert (
        registry.category("Modules(GF(5)).Free().FiniteRank()").direct_obligation_ids
        == (_MODULE_FINITE_RANK_OBLIGATION,)
    )


def test_lookup_by_id_and_transitive_set_graph_nodes() -> None:
    registry = _build_registry()

    countable = registry.inherited_obligation_ids("Sets().Countable()")
    cartesian = registry.inherited_obligation_ids("Sets().CartesianProducts()")
    modules_r = registry.inherited_obligation_ids("Modules(R).Free().FiniteRank()")

    assert countable == (_SETS_BASE_OBLIGATION, _SETS_COUNTABLE_OBLIGATION)
    assert cartesian == (_SETS_BASE_OBLIGATION, _SETS_CARTESIAN_PRODUCT_OBLIGATION)
    assert modules_r[0] == _SETS_BASE_OBLIGATION
    assert modules_r[-1] == _MODULE_FINITE_RANK_OBLIGATION
    assert registry.category("Modules(R).Free().FiniteRank()").name == (
        "Modules(R).Free().FiniteRank()"
    )
    with pytest.raises(KeyError):
        registry.category("Modules(QQ).Free().FiniteRank()")


def test_registry_rejects_unknown_obligation_ids() -> None:
    with pytest.raises(ValueError):
        CategorySpecRegistry(
            categories=(
                CategorySpec(
                    id="Modules(R)",
                    name="Modules(R)",
                    direct_obligation_ids=("modules.unknown",),
                    super_category_ids=("Sets()",),
                ),
            ),
            obligation_ids=(_SETS_BASE_OBLIGATION,),
        )


def test_registry_rejects_unknown_super_ids() -> None:
    with pytest.raises(ValueError):
        CategorySpecRegistry(
            categories=(
                CategorySpec(
                    id="Modules(R)",
                    name="Modules(R)",
                    direct_obligation_ids=(_MODULE_BASE_OBLIGATION,),
                    super_category_ids=("Sets().Nope()",),
                ),
                CategorySpec(
                    id="Sets()",
                    name="Sets()",
                    direct_obligation_ids=(_SETS_BASE_OBLIGATION,),
                ),
            ),
            obligation_ids=(
                _SETS_BASE_OBLIGATION,
                _MODULE_BASE_OBLIGATION,
            ),
        )


def test_registry_rejects_cycles() -> None:
    with pytest.raises(ValueError):
        CategorySpecRegistry(
            categories=(
                CategorySpec(
                    id="A",
                    name="A",
                    direct_obligation_ids=(_SETS_BASE_OBLIGATION,),
                    super_category_ids=("B",),
                ),
                CategorySpec(
                    id="B",
                    name="B",
                    direct_obligation_ids=(),
                    super_category_ids=("C",),
                ),
                CategorySpec(
                    id="C",
                    name="C",
                    direct_obligation_ids=(),
                    super_category_ids=("A",),
                ),
            ),
            obligation_ids=(_SETS_BASE_OBLIGATION,),
        )
