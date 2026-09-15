r"""Archive reconciliation for corestriction of algebra maps to the centre."""
import pytest

from dzack_research.preamble.all import (
    QQ,
    MatrixSpace,
    OwnedRings,
)
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def test_exterior_algebra_center_is_the_archived_predicate_subring() -> None:
    exterior = QQ.free_module(finite_ordered_set(("e1", "e2"))).exterior_algebra()
    first = exterior.algebra_generator("e1")
    second = exterior.algebra_generator("e2")
    center = exterior.ring_center()

    assert first * second in center
    assert first not in center
    assert center.ambient_ring() is exterior
    assert center.inclusion()(first * second) == first * second
    assert center in OwnedRings().Commutative()


def test_archived_free_algebra_map_corestricts_to_the_exterior_center() -> None:
    exterior = QQ.free_module(finite_ordered_set(("e1", "e2"))).exterior_algebra()
    first = exterior.algebra_generator("e1")
    second = exterior.algebra_generator("e2")
    source = QQ.free_module(finite_ordered_set(("t",))).symmetric_algebra()
    morphism = source.Mor(exterior)({"t": first * second})

    factor = morphism.corestrict_to_center()
    center = exterior.ring_center()
    variable = source.algebra_generator("t")

    assert factor.domain() is source
    assert factor.codomain() is center
    assert factor(variable) == first * second
    assert center.inclusion()(factor(variable)) == morphism(variable)


def test_archived_noncentral_free_algebra_map_refuses_corestriction() -> None:
    exterior = QQ.free_module(finite_ordered_set(("e1", "e2"))).exterior_algebra()
    first = exterior.algebra_generator("e1")
    source = QQ.free_module(finite_ordered_set(("t",))).symmetric_algebra()
    morphism = source.Mor(exterior)({"t": first})

    with pytest.raises(ValueError, match="not central"):
        morphism.corestrict_to_center()


def test_central_algebra_map_corestricts_through_the_actual_center() -> None:
    source = MatrixSpace(QQ, 1)
    matrices = MatrixSpace(QQ, 2)
    source_module = source.underlying_module()
    target_module = matrices.underlying_module()
    source_label = next(iter(source_module.module_generating_set()))
    underlying = source_module.module_category().Mor(source_module, target_module)(
        {
            source_label: matrices._carrier_element(matrices.identity()),
        }
    )
    morphism = Algebras(source.base_ring()).Associative().Unital().Mor(source, matrices)(underlying)

    factor = morphism.corestrict_to_center()
    center = matrices.ring_center()
    inclusion = center.inclusion()

    assert factor.domain() is source
    assert factor.codomain() is center
    for label in source.algebra_generating_set():
        generator = source.algebra_generator(label)
        central_image = factor(generator)
        assert inclusion(central_image) == morphism(generator)


def test_noncentral_generator_image_refuses_center_corestriction() -> None:
    matrices = MatrixSpace(QQ, 2)
    morphism = Algebras(matrices.base_ring()).Associative().Unital().Mor(matrices, matrices).identity()

    with pytest.raises(ValueError, match="not central"):
        morphism.corestrict_to_center()
