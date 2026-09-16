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

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.modules.graded_modules import (
    _require_grading_monoid,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    Zmod,
    _own_ring,
)
from dzack_research.preamble.refine import refine


class _ParityKey:
    r"""Identity-stable cache key for a chosen parity morphism.

    Sage morphism equality can require generator comparison and is not a valid
    cache-key operation for arbitrary owned ring morphisms.  Chosen parity is
    structure, so its identity is the stable parameter until a separate
    extensional morphism equality is available.
    """

    def __init__(self, morphism) -> None:
        self._morphism = morphism

    def morphism(self):
        return self._morphism


_PARITY_KEYS = {}


def _parity_key(parity):
    identity = id(parity)
    known = _PARITY_KEYS.get(identity)
    if known is not None and known.morphism() is parity:
        return known
    key = _ParityKey(parity)
    _PARITY_KEYS[identity] = key
    return key


@cached_function
def _integer_koszul_parity():
    r"""Return the canonical reduction ``ZZ -> ZZ/2`` once."""
    integers = _own_ring(SageZZ)
    parity_target = Zmod(2)
    return integers.Mor(parity_target)(parity_target)


def _koszul_parity(grading_monoid, parity=None):
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
        parity = _integer_koszul_parity()
    assert parity.domain() is grading_monoid, (
        "the parity homomorphism is defined on the grading monoid"
    )
    assert parity.codomain() is parity_target, (
        f"a Koszul sign is read through a parity in {parity_target}"
    )
    return parity


class GradedCommutativeAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The identity-degree rank-one algebra with the selected parity."""
        algebra = GradedAlgebras(
            self.base_ring(),
            self.grading_monoid(),
        ).an_object()
        refine(algebra, Algebras(self.base_ring()).Commutative())
        refine(algebra, self)
        return algebra

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None, parity=None):
        monoid = _require_grading_monoid(grading_monoid)
        selected_parity = _koszul_parity(monoid, parity)
        return OwnedCategoryOverBaseRing.__classcall__(
            cls, base_ring, monoid, _parity_key(selected_parity)
        )

    def __init__(self, base_ring, grading_monoid, parity_key) -> None:
        self._grading_monoid = grading_monoid
        self._parity = parity_key.morphism()
        self._parity_key = parity_key
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
        return (
            super()._make_named_class_key(name),
            self.grading_monoid(),
            self._parity_key,
        )

    def super_categories(self):

        return [GradedAlgebras(self.base_ring(), self.grading_monoid())]


class StrictlyGradedCommutativeAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The identity-degree rank-one algebra, where odd-square conditions are vacuous."""
        algebra = GradedCommutativeAlgebras(
            self.base_ring(),
            self.grading_monoid(),
            self.parity_homomorphism(),
        ).an_object()
        refine(algebra, self)
        return algebra

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None, parity=None):
        monoid = _require_grading_monoid(grading_monoid)
        selected_parity = _koszul_parity(monoid, parity)
        return OwnedCategoryOverBaseRing.__classcall__(
            cls, base_ring, monoid, _parity_key(selected_parity)
        )

    def __init__(self, base_ring, grading_monoid, parity_key) -> None:
        self._grading_monoid = grading_monoid
        self._parity = parity_key.morphism()
        self._parity_key = parity_key
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
        return (
            super()._make_named_class_key(name),
            self.grading_monoid(),
            self._parity_key,
        )

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
