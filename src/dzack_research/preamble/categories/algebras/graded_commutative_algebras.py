r"""Graded-commutative algebra categories.

Graded commutativity is the Koszul rule
``xy = (-1)^(eps(p) eps(q)) yx`` on homogeneous elements of degrees ``p`` and
``q``, where ``eps`` is a homomorphism from the grading monoid to
``ZZ/2``.  The sign is read through that parity and through nothing else, so
the hypothesis the rule places on a grading monoid ``M`` is not that ``M`` is
the integers but that ``M`` comes with such an ``eps``.

Strict graded commutativity additionally imposes ``x^2 = 0`` in odd degree,
odd meaning ``eps(p) = 1``; this distinction is essential over rings with
2-torsion.
"""

from sage.misc.cachefunc import cached_function
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.graded_modules import (
    require_grading_monoid,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    Zmod,
    _own_ring,
    ring_morphism,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras


@cached_function
def koszul_parity(grading_monoid, parity=None):
    r"""Return the parity homomorphism ``M -> ZZ/2`` the Koszul rule reads through.

    A monoid admits many homomorphisms to ``ZZ/2`` -- the trivial one among
    them, which recovers ordinary commutativity -- so the parity is chosen
    structure and the caller states it.  The integers are the grading with a
    canonical choice, reduction mod 2, which is the classical convention this
    module's rule is written in, and which is what the omitted argument means.
    Naming ``ZZ`` to select its own canonical structure is a different act
    from testing a monoid's identity in order to refuse every other one.

    A superalgebra is graded by ``ZZ/2`` and states its parity as the identity
    of ``ZZ/2``; a multigrading states the total-degree parity.
    """
    parity_target = Zmod(2)
    if parity is None:
        assert grading_monoid is _own_ring(SageZZ), (
            f"{grading_monoid} is a grading monoid with no canonical parity "
            f"homomorphism to {parity_target}; state the parity the Koszul "
            "sign rule is to read its degrees through"
        )
        parity = ring_morphism(grading_monoid, parity_target, parity_target)
    assert parity.domain() is grading_monoid, (
        "the parity homomorphism is defined on the grading monoid"
    )
    assert parity.codomain() is parity_target, (
        f"a Koszul sign is read through a parity in {parity_target}"
    )
    return parity


class GradedCommutativeAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""That de Rham algebra, graded-commutative."""
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebras

        return DeRhamAlgebras(self.base_ring()).an_object()

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None, parity=None):
        monoid = require_grading_monoid(grading_monoid)
        return OwnedCategoryOverBaseRing.__classcall__(
            cls, base_ring, monoid, koszul_parity(monoid, parity)
        )

    def __init__(self, base_ring, grading_monoid, parity) -> None:
        self._grading_monoid = grading_monoid
        self._parity = parity
        super().__init__(base_ring)

    def grading_monoid(self):
        return self._grading_monoid

    def parity_homomorphism(self):
        r"""Return the ``M -> ZZ/2`` this category's Koszul sign is read through."""
        return self._parity

    @classmethod
    def _repr_object_names(cls):
        return "graded-commutative algebras"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.grading_monoid())

    def super_categories(self):

        return [GradedAlgebras(self.base_ring(), self.grading_monoid())]


class StrictlyGradedCommutativeAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""That de Rham algebra, strictly graded-commutative."""
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebras

        return DeRhamAlgebras(self.base_ring()).an_object()

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None, parity=None):
        monoid = require_grading_monoid(grading_monoid)
        return OwnedCategoryOverBaseRing.__classcall__(
            cls, base_ring, monoid, koszul_parity(monoid, parity)
        )

    def __init__(self, base_ring, grading_monoid, parity) -> None:
        self._grading_monoid = grading_monoid
        self._parity = parity
        super().__init__(base_ring)

    def grading_monoid(self):
        return self._grading_monoid

    def parity_homomorphism(self):
        r"""Return the ``M -> ZZ/2`` this category's Koszul sign is read through."""
        return self._parity

    @classmethod
    def _repr_object_names(cls):
        return "strictly graded-commutative algebras"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.grading_monoid())

    def super_categories(self):
        return [
            GradedCommutativeAlgebras(
                self.base_ring(),
                self.grading_monoid(),
                self.parity_homomorphism(),
            )
        ]


__all__ = [
    "GradedCommutativeAlgebras",
    "StrictlyGradedCommutativeAlgebras",
]
