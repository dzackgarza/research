"""Pushouts of finitely presented commutative algebra morphisms."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.algebras import (
    AlgebraMorphism,
    CommutativeAlgebras,
    FramedAlgebras,
)
from dzack_research.preamble.categories.algebras.commutative_coproducts import (
    commutative_algebra_coproduct,
)
from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
    AlgebrasWithChosenFinitePresentation,
    FinitelyPresentedAlgebra,
)
from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebras
from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.refine import refine


class CommutativeAlgebraPushouts(OwnedCategoryOverBaseRing):
    r"""Commutative ``R``-algebras equipped as selected pushouts of one span."""

    def super_categories(self):
        return [CommutativeAlgebras(self.base_ring())]

    class ParentMethods:
        def pushout_span(self):
            return self._preamble_pushout_span

        def pushout_maps(self):
            return self._preamble_pushout_maps

        def left_pushout_map(self):
            return self.pushout_maps()[0]

        def right_pushout_map(self):
            return self.pushout_maps()[1]

        def from_pushout_cocone(self, left_map, right_map):
            source_map, target_map = self.pushout_span()
            left_factor = source_map.codomain()
            right_factor = target_map.codomain()
            if not isinstance(left_map, AlgebraMorphism) or not isinstance(
                right_map, AlgebraMorphism
            ):
                raise TypeError("a pushout cocone uses algebra morphisms")
            if left_map.domain() is not left_factor or right_map.domain() is not right_factor:
                raise ValueError("the pushout cocone has the wrong factor domains")
            if left_map.codomain() is not right_map.codomain():
                raise ValueError("the pushout cocone maps require one common codomain")
            common_source = source_map.domain()
            for label in common_source.algebra_generating_set():
                element = common_source.algebra_generator(label)
                if left_map(source_map(element)) != right_map(target_map(element)):
                    raise ValueError("the cocone does not agree on the common algebra")

            target = left_map.codomain()
            images = {}
            for label in left_factor.algebra_generating_set():
                images[("left", label)] = left_map(left_factor.algebra_generator(label))
            for label in right_factor.algebra_generating_set():
                images[("right", label)] = right_map(right_factor.algebra_generator(label))
            # The selected quotient has the same tagged framing as the intermediate
            # coproduct, so a generator assignment is the unique factorization.
            return self.hom(images, codomain=target)


def _quotient_by_elements(algebra, elements):
    base = algebra.base_ring()
    selected = tuple(elements)
    if not selected:
        identity = CommutativeAlgebras(base).Hom(algebra, algebra).identity()
        return algebra, identity
    if algebra in AlgebrasWithChosenFinitePresentation(base):
        presentation = algebra.presentation_ring()
        relations = tuple(algebra.relations()) + tuple(
            algebra.lift_to_presentation(element) for element in selected
        )
    elif algebra in SymmetricAlgebras(base):
        presentation = algebra
        relations = selected
    else:
        raise NotImplementedError(
            "quotienting a commutative-algebra pushout requires a selected polynomial presentation"
        )
    quotient = FinitelyPresentedAlgebra(presentation, relations)
    quotient_map = algebra.hom(
        {
            label: quotient.algebra_generator(label)
            for label in algebra.algebra_generating_set()
        },
        codomain=quotient,
    )
    return quotient, quotient_map


@cached_function
def commutative_algebra_pushout(left_map, right_map):
    r"""Return the pushout of ``A -> B`` and ``A -> C`` in commutative algebras."""
    if not isinstance(left_map, AlgebraMorphism) or not isinstance(right_map, AlgebraMorphism):
        raise TypeError("a commutative-algebra pushout is specified by algebra morphisms")
    if left_map.domain() is not right_map.domain():
        raise ValueError("pushout maps require one common domain")
    common = left_map.domain()
    left = left_map.codomain()
    right = right_map.codomain()
    base = common.base_ring()
    if left.base_ring() is not base or right.base_ring() is not base:
        raise ValueError("the pushout span must lie over one scalar base")
    if common not in FramedAlgebras(base):
        raise NotImplementedError(
            "the active pushout backend requires a finite algebra framing on the common source"
        )

    tensor = commutative_algebra_coproduct(left, right)
    left_injection, right_injection = tensor.coproduct_injections()
    equalities = tuple(
        left_injection(left_map(common.algebra_generator(label)))
        - right_injection(right_map(common.algebra_generator(label)))
        for label in common.algebra_generating_set()
    )
    pushout, quotient_map = _quotient_by_elements(tensor, equalities)
    left_pushout = quotient_map * left_injection
    right_pushout = quotient_map * right_injection
    pushout._preamble_pushout_span = (left_map, right_map)
    pushout._preamble_pushout_maps = (left_pushout, right_pushout)
    pushout._preamble_pushout_coproduct = tensor
    return refine(pushout, CommutativeAlgebraPushouts(base))


__all__ = ["CommutativeAlgebraPushouts", "commutative_algebra_pushout"]
