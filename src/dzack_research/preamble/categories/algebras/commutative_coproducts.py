"""Finite-presentation coproducts of commutative algebras."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.algebras import (
    AlgebraMorphism,
    CommutativeAlgebras,
    FramedAlgebras,
)
from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
    AlgebrasWithChosenFinitePresentation,
    FinitelyPresentedAlgebra,
)
from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebras
from dzack_research.preamble.categories.algebras.framed_free_algebras import (
    SymmetricAlgebraOn,
)
from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing, engine_ring
from dzack_research.preamble.refine import refine


class CommutativeAlgebraCoproducts(OwnedCategoryOverBaseRing):
    r"""Commutative ``R``-algebras equipped as selected binary coproducts."""

    def super_categories(self):
        return [CommutativeAlgebras(self.base_ring())]

    class ParentMethods:
        def coproduct_factors(self):
            return self._preamble_coproduct_factors

        tensor_factors = coproduct_factors

        def coproduct_injection(self, index):
            return self._preamble_coproduct_injections[index]

        def coproduct_injections(self):
            return tuple(self.coproduct_injection(index) for index in range(2))

        def left_coproduct_map(self):
            return self.coproduct_injection(0)

        def right_coproduct_map(self):
            return self.coproduct_injection(1)

        def from_cocone(self, left_map, right_map):
            r"""Return the unique algebra map induced by a compatible binary cocone."""
            left, right = self.coproduct_factors()
            if not isinstance(left_map, AlgebraMorphism) or not isinstance(
                right_map, AlgebraMorphism
            ):
                raise TypeError("a commutative-algebra cocone uses algebra morphisms")
            if left_map.domain() is not left or right_map.domain() is not right:
                raise ValueError("the cocone maps have the wrong factor domains")
            if left_map.codomain() is not right_map.codomain():
                raise ValueError("the cocone maps must have one common codomain")
            target = left_map.codomain()
            images = {}
            for label in left.algebra_generating_set():
                images[("left", label)] = left_map(left.algebra_generator(label))
            for label in right.algebra_generating_set():
                images[("right", label)] = right_map(right.algebra_generator(label))
            return self.hom(images, codomain=target)

        tensor_map = from_cocone


def _presentation_data(algebra):
    base = algebra.base_ring()
    if algebra in AlgebrasWithChosenFinitePresentation(base):
        return algebra.presentation_ring(), tuple(algebra.relations())
    if algebra in SymmetricAlgebras(base) and algebra in FramedAlgebras(base):
        return algebra, ()
    from dzack_research.preamble.categories.rings.commutative_algebra import QuotientRings

    if algebra in QuotientRings():
        source = algebra.quotient_source()
        if source in SymmetricAlgebras(base):
            return source, tuple(algebra.defining_ideal().gens())
    raise NotImplementedError(
        "the active commutative-algebra coproduct backend requires a free polynomial or selected finite presentation"
    )


def _transport_relations(presentation_ring, relations, target, tag):
    if not relations:
        return ()
    source_engine = engine_ring(presentation_ring)
    target_engine = engine_ring(target)
    base_engine = engine_ring(target.base_ring())
    images = [
        target_engine(target.algebra_generator((tag, label)))
        for label in presentation_ring.algebra_generating_set()
    ]
    base_map = target_engine.coerce_map_from(base_engine)
    ring_map = source_engine.hom(images, target_engine, base_map=base_map)
    return tuple(target_engine(ring_map(source_engine(relation))) for relation in relations)


@cached_function
def commutative_algebra_coproduct(left, right):
    r"""Return ``left tensor_R right``, the coproduct in commutative ``R``-algebras."""
    base = left.base_ring()
    if right.base_ring() is not base:
        raise ValueError("commutative-algebra coproducts require one scalar base")
    category = CommutativeAlgebras(base)
    if left not in category or right not in category:
        raise TypeError("both factors must be commutative algebras over the common base")
    if left not in FramedAlgebras(base) or right not in FramedAlgebras(base):
        raise NotImplementedError(
            "the active finite-presentation coproduct backend requires finite algebra framings"
        )

    left_presentation, left_relations = _presentation_data(left)
    right_presentation, right_relations = _presentation_data(right)
    combined_labels = tuple(("left", label) for label in left.algebra_generating_set()) + tuple(
        ("right", label) for label in right.algebra_generating_set()
    )
    presentation = SymmetricAlgebraOn(base, combined_labels)
    relations = _transport_relations(
        left_presentation, left_relations, presentation, "left"
    ) + _transport_relations(right_presentation, right_relations, presentation, "right")
    coproduct = FinitelyPresentedAlgebra(presentation, relations) if relations else presentation

    left_map = left.hom(
        {
            label: coproduct.algebra_generator(("left", label))
            for label in left.algebra_generating_set()
        },
        codomain=coproduct,
    )
    right_map = right.hom(
        {
            label: coproduct.algebra_generator(("right", label))
            for label in right.algebra_generating_set()
        },
        codomain=coproduct,
    )
    coproduct._preamble_coproduct_factors = (left, right)
    coproduct._preamble_coproduct_injections = (left_map, right_map)
    return refine(coproduct, CommutativeAlgebraCoproducts(base))


__all__ = ["CommutativeAlgebraCoproducts", "commutative_algebra_coproduct"]
