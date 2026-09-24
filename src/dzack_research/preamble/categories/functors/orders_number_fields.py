r"""The fraction-field / ring-of-integers adjunction.

For number-field orders and number fields with unital embeddings,

``Frac ⊣ O``:

``Hom_NF(Frac(O), K) ≅ Hom_Ord(O, O_K)``.

An order embedding extends uniquely to fraction fields; a field embedding
restricts to maximal orders because integrality is preserved.
"""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.rings.embeddings import (
    NumberFieldEmbedding,
    OrderEmbedding,
)
from dzack_research.preamble.categories.rings.number_fields import OwnedNumberFields
from dzack_research.preamble.categories.rings.ring_foundation import OwnedOrders, _engine_ring


class _FractionFieldFunctor(Functor):
    r"""``Frac : Orders -> NumberFields``."""

    def __init__(self) -> None:
        super().__init__(OwnedOrders(), OwnedNumberFields())

    def _apply_object(self, order):
        return order.fraction_field()

    def _apply_morphism(self, embedding: OrderEmbedding):
        source = self(embedding.domain())
        target = self(embedding.codomain())
        return source.Mor(target)(embedding.field_embedding())

    def _repr_(self):
        return "Fraction-field functor"


class _RingOfIntegersFunctor(Functor):
    r"""``K -> O_K : NumberFields -> Orders``."""

    def __init__(self) -> None:
        super().__init__(OwnedNumberFields(), OwnedOrders())

    def _apply_object(self, field):
        return field.ring_of_integers()

    def _apply_morphism(self, embedding: NumberFieldEmbedding):
        source = self(embedding.domain())
        target = self(embedding.codomain())
        return source.Mor(target)(embedding)

    def _repr_(self):
        return "Ring-of-integers functor"


class _OrderNumberFieldAdjunction(Adjunction):
    r"""``Frac ⊣ O``."""

    def __init__(self) -> None:
        super().__init__(_FractionFieldFunctor(), _RingOfIntegersFunctor())

    def _unit_component(self, order):
        field = self.left_adjoint()(order)
        maximal_order = self.right_adjoint()(field)
        return order.Mor(maximal_order)(
            field.Mor(field).identity()
        )

    def _counit_component(self, field):
        source = self.left_adjoint()(self.right_adjoint()(field))
        if _engine_ring(source) is _engine_ring(field):
            if source is field:
                return field.Mor(field).identity()
            if _engine_ring(source).degree() == 1:
                return source.Mor(field)(
                    _engine_ring(source).mor(_engine_ring(field))
                )
            return source.Mor(field)(field.primitive_element())
        embeddings = source.Mor(field).embeddings()
        if len(embeddings) != 1:
            raise ValueError(
                f"the counit Frac(O_K) -> K at {field} needs exactly one embedding {source} -> {field}, but "
                f"there are {len(embeddings)}"
            )
        return embeddings[0]


    def _repr_(self):
        return "Fraction-field/ring-of-integers adjunction"


@cached_function
def _order_number_field_adjunction() -> _OrderNumberFieldAdjunction:
    return _OrderNumberFieldAdjunction()


__all__ = []
