"""Spec-core reports for free finite-rank module construction witnesses."""

from __future__ import annotations

from typing import Final

from category_specs.spec_core import (
    CategorySpec,
    CategorySpecRegistry,
    ComputedValue,
    ConstructionWitness,
    SpecObligation,
    SpecProvider,
    SpecRegistry,
    SpecReport,
)

_MODULE_MAPPING_SOURCE: Final = (
    ".agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/"
    "SPEC-MAPPING-MODULES.md"
)
_SET_MAPPING_SOURCE: Final = (
    ".agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/"
    "SPEC-MAPPING-SETS.md"
)
_MODULE_OWNERSHIP_SOURCE: Final = (
    ".agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/"
    "SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING.md"
)
_SAGE_FREE_MODULE_SOURCE: Final = "sage.modules.free_module"
_SAGE_SETS_SOURCE: Final = "sage.categories.sets_cat"
_SAGE_ENUMERATED_SETS_SOURCE: Final = "sage.categories.enumerated_sets"

_CARRIER_OBLIGATION_ID: Final = "modules.free_finite_rank.cartesian_power_carrier"
_PRODUCT_CARDINALITY_OBLIGATION_ID: Final = "sets.cartesian_product.cardinality"
_PRODUCT_COUNTABILITY_OBLIGATION_ID: Final = "sets.cartesian_product.countability"
_PRODUCT_ENUMERATION_OBLIGATION_ID: Final = (
    "sets.cartesian_product.deterministic_enumeration"
)

_CARRIER_OBLIGATION: Final = SpecObligation(
    id=_CARRIER_OBLIGATION_ID,
    title="Free finite-rank modules expose their carrier as a Cartesian power",
    source=_MODULE_MAPPING_SOURCE,
    description=(
        "Owner: Modules(R).Free().FiniteRank(); prerequisite: a rank and base "
        "carrier whose finite Cartesian power is the underlying set."
    ),
)
_PRODUCT_CARDINALITY_OBLIGATION: Final = SpecObligation(
    id=_PRODUCT_CARDINALITY_OBLIGATION_ID,
    title="Cartesian products expose product cardinality",
    source="category_specs/sets/subcategories/cartesian_product.py",
    description=(
        "Owner: Sets().CartesianProducts(); prerequisite: factor cardinalities."
    ),
)
_PRODUCT_COUNTABILITY_OBLIGATION: Final = SpecObligation(
    id=_PRODUCT_COUNTABILITY_OBLIGATION_ID,
    title="Finite Cartesian powers of countable carriers remain countable",
    source=_SET_MAPPING_SOURCE,
    description=(
        "Owner: Sets().CartesianProducts(); prerequisite: countable factor "
        "enumerations and finite product arity."
    ),
)
_PRODUCT_ENUMERATION_OBLIGATION: Final = SpecObligation(
    id=_PRODUCT_ENUMERATION_OBLIGATION_ID,
    title="Countable Cartesian powers expose deterministic enumeration",
    source=_SET_MAPPING_SOURCE,
    description=(
        "Owner: Sets().CartesianProducts(); prerequisite: a canonical product "
        "enumeration provider for countable factors. This is intentionally not "
        "satisfied by module-local iteration."
    ),
)

_PRODUCT_CARDINALITY_PROVIDER: Final = SpecProvider(
    id="sets.cartesian_product.cardinality",
    category="Sets().CartesianProducts()",
    provides=(_PRODUCT_CARDINALITY_OBLIGATION_ID,),
    source="category_specs/sets/subcategories/cartesian_product.py",
    description=(
        "Delegates to Sage Sets.CartesianProducts.ParentMethods.cardinality; "
        "module reports consume this as set/product evidence."
    ),
)
_PRODUCT_COUNTABILITY_PROVIDER: Final = SpecProvider(
    id="sets.cartesian_product.countable_finite_power",
    category="Sets().CartesianProducts()",
    provides=(_PRODUCT_COUNTABILITY_OBLIGATION_ID,),
    source=_SAGE_ENUMERATED_SETS_SOURCE,
    description=(
        "Finite Cartesian powers of Sage EnumeratedSets factors carry a countable "
        "factor-enumeration witness; the project countability contract is recorded "
        "in SPEC-MAPPING-SETS."
    ),
)


def gf5_rank3_report() -> SpecReport:
    """Return the vertical-slice report for ``GF(5)^3``."""
    from sage.all import GF

    return free_finite_rank_module_report(GF(5), 3, base_label="GF(5)")


def zz_rank2_report() -> SpecReport:
    """Return the vertical-slice report for ``ZZ^2``."""
    from sage.all import ZZ

    return free_finite_rank_module_report(ZZ, 2, base_label="ZZ")


def free_finite_rank_module_report(
    base_ring: object, rank: int, *, base_label: str | None = None
) -> SpecReport:
    """Build a spec-core report for the free module ``base_ring^rank``."""
    if rank < 0:
        raise ValueError("rank must be nonnegative")

    label = base_label or str(base_ring)
    carrier_label = _cartesian_power_label(label=label, rank=rank)
    declared_category = f"Modules({label}).Free().FiniteRank()"

    from sage.all import cartesian_product
    from sage.rings.infinity import infinity

    carrier = cartesian_product([base_ring] * rank)
    cardinality = carrier.cardinality()
    base_is_countable = _base_carrier_is_countable(base_ring)
    countable_product = cardinality == infinity and base_is_countable

    inherited_obligation_ids = _select_inherited_obligation_ids(
        base_is_countable=base_is_countable, product_is_infinite=countable_product
    )
    registry = _build_registry(
        declared_category=declared_category,
        base_label=label,
        rank=rank,
    )

    return registry.report(
        subject=f"{label}^{rank}",
        declared_category=declared_category,
        inherited_obligation_ids=inherited_obligation_ids,
        computed_values=_build_computed_values(
            carrier_label=carrier_label,
            cardinality=cardinality,
            include_countability=countable_product,
        ),
    )


def _build_registry(
    *, declared_category: str, base_label: str, rank: int
) -> SpecRegistry:
    """Build the reusable free-finite-rank witness registry."""
    return SpecRegistry(
        obligations=_module_and_product_obligations(),
        providers=_set_product_providers(),
        witnesses=(
            _build_cartesian_power_witness(base_label, rank, declared_category),
        ),
    )


def _slice_category_registry() -> CategorySpecRegistry:
    """Return the source-truth category graph for this vertical slice."""
    return CategorySpecRegistry(
        categories=(
            CategorySpec(id="Sets()", name="Sets()"),
            CategorySpec(
                id="Sets().CartesianProducts()",
                name="Sets().CartesianProducts()",
                direct_obligation_ids=(_PRODUCT_CARDINALITY_OBLIGATION_ID,),
                super_category_ids=("Sets()",),
            ),
            CategorySpec(
                id="Sets().CartesianProducts().CountableFinitePowers()",
                name="Sets().CartesianProducts().CountableFinitePowers()",
                direct_obligation_ids=(
                    _PRODUCT_COUNTABILITY_OBLIGATION_ID,
                    _PRODUCT_ENUMERATION_OBLIGATION_ID,
                ),
                super_category_ids=("Sets().CartesianProducts()",),
            ),
            CategorySpec(
                id="Modules(R).Free().FiniteRank()",
                name="Modules(R).Free().FiniteRank()",
                direct_obligation_ids=(_CARRIER_OBLIGATION_ID,),
                super_category_ids=("Sets().CartesianProducts()",),
            ),
            CategorySpec(
                id="Modules(R).Free().FiniteRank().CountableCarrier()",
                name="Modules(R).Free().FiniteRank().CountableCarrier()",
                super_category_ids=(
                    "Modules(R).Free().FiniteRank()",
                    "Sets().CartesianProducts().CountableFinitePowers()",
                ),
            ),
        ),
        obligation_ids=(
            _CARRIER_OBLIGATION_ID,
            _PRODUCT_CARDINALITY_OBLIGATION_ID,
            _PRODUCT_COUNTABILITY_OBLIGATION_ID,
            _PRODUCT_ENUMERATION_OBLIGATION_ID,
        ),
    )


def _source_category_id(*, base_is_countable: bool, product_is_infinite: bool) -> str:
    if base_is_countable and product_is_infinite:
        return "Modules(R).Free().FiniteRank().CountableCarrier()"
    return "Modules(R).Free().FiniteRank()"


def _module_and_product_obligations() -> tuple[SpecObligation, ...]:
    """Return obligations shared by all free finite-rank module slice subjects."""
    return (
        _CARRIER_OBLIGATION,
        _PRODUCT_CARDINALITY_OBLIGATION,
        _PRODUCT_COUNTABILITY_OBLIGATION,
        _PRODUCT_ENUMERATION_OBLIGATION,
    )


def _set_product_providers() -> tuple[SpecProvider, ...]:
    """Return product-related set providers shared by this registry."""
    return (
        _PRODUCT_CARDINALITY_PROVIDER,
        _PRODUCT_COUNTABILITY_PROVIDER,
    )


def _cartesian_power_label(*, label: str, rank: int) -> str:
    """Create the canonical free-module carrier label."""
    return f"CartesianPower({label}, {rank})"


def _build_cartesian_power_witness(
    base_label: str, rank: int, declared_category: str
) -> ConstructionWitness:
    """Create the cartesian-power carrier witness for one module subject."""
    return ConstructionWitness(
        id=f"modules.free_finite_rank.cartesian_power.{base_label}.{rank}",
        construction=_cartesian_power_label(label=base_label, rank=rank),
        source_category=declared_category,
        target_category="Sets().CartesianProducts()",
        provides=(_CARRIER_OBLIGATION_ID,),
        source=_MODULE_MAPPING_SOURCE,
        description=(
            "Witnesses the underlying set of a free finite-rank module "
            "as the finite Cartesian power of its base carrier."
        ),
    )


def _select_inherited_obligation_ids(
    *, base_is_countable: bool, product_is_infinite: bool
) -> tuple[str, ...]:
    """Return inherited obligations that this subject is expected to satisfy."""
    return _slice_category_registry().inherited_obligation_ids(
        _source_category_id(
            base_is_countable=base_is_countable,
            product_is_infinite=product_is_infinite,
        )
    )


def _build_computed_values(
    *,
    carrier_label: str,
    cardinality: object,
    include_countability: bool,
) -> tuple[ComputedValue, ...]:
    """Build computed evidence values for a slice report."""
    values = (
        ComputedValue(
            name="carrier",
            value=carrier_label,
            source=f"{_MODULE_MAPPING_SOURCE}; {_SET_MAPPING_SOURCE}",
        ),
        ComputedValue(
            name="cardinality",
            value=str(cardinality),
            source=f"{_SAGE_SETS_SOURCE}; {_MODULE_OWNERSHIP_SOURCE}",
        ),
    )
    if not include_countability:
        return values

    return (
        *values,
        ComputedValue(
            name="countability",
            value="countably infinite",
            source=f"{_SET_MAPPING_SOURCE}; {_SAGE_FREE_MODULE_SOURCE}",
        ),
    )


def _base_carrier_is_countable(base_ring: object) -> bool:
    from sage.categories.enumerated_sets import EnumeratedSets

    return bool(base_ring in EnumeratedSets())
