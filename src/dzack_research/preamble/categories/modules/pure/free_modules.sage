r"""Free modules over a base ring."""


from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.sets.owned_sets import Sets as OwnedSets
from dzack_research.preamble.owned_category import OwnedCategoryMixin, object_of
from dzack_research.preamble.owned_category_bases import Category_over_base_ring
from sage.categories.modules import Modules


class FreeModules(OwnedCategoryOverBaseRing):
    r"""Category of free modules over a base ring, without a chosen module_generators."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free modules"

    def super_categories(self) -> list:
        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_free(self) -> bool:
            r"""Return whether this module is free."""
            return True

        def is_torsion_free(self) -> bool:
            r"""Free \(\Rightarrow\) torsion-free, over an integral domain.

            The implication is a theorem *with a hypothesis*: in a free
            module over a domain, \(r\cdot m = 0\) with \(r\neq 0\) forces
            \(m = 0\) coordinatewise.  Over a base with zero divisors the
            statement depends on which torsion convention is in force, so
            the hypothesis is asserted rather than silently assumed.
            """
            assert self.base_ring().is_integral_domain(), (
                f"free => torsion-free is a theorem over an integral "
                f"domain; {self.base_ring()} is not one, and this node "
                "states no torsion answer there"
            )
            return True


class FiniteRankFreeModules(Category_over_base_ring):
    r"""\(R^n\), constructed through the chain rather than framed and placed.

    The module level is where the underlying **set** is worried about: a
    module is a set, and declaring this one to be \(R^n\) is declaring its
    underlying set to be the product \(R\times\cdots\times R\).  That is the
    whole of what this level does about size -- it names the factors, and the
    set level answers from them.

    Contrast ``framed/framed_free_modules.sage``, where ``_free_module_placement``
    reads the axioms of \(R\) and of the framing and *stamps* an answer onto
    the module, with a separate count beside it.  Nothing of that shape is
    here: the factors are the only thing declared.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free modules of finite rank"

    def super_categories(self) -> list:
        return [FreeModules(self.base_ring()), OwnedSets().CartesianProducts()]

    class ParentMethods:
        def __init__(self, rank: "Integer", base: "Ring", **rest: object) -> None:
            self._rank = rank
            super().__init__(factors=(base,) * rank, base=base, **rest)

        def rank(self) -> "Integer":
            return self._rank

        def _repr_(self) -> str:
            return f"{self.base_ring()}^{self._rank}"

    class ElementMethods:
        r"""A coordinate vector: where the arithmetic of \(R^n\) lives.

        Not on the product below.  A point of a product of *sets* has no
        addition; addition is what the module level adds, so it is declared
        here and the components come from the set level unchanged.
        """

        def _add_(self, other: "Element") -> "Element":
            return self.parent()(
                [left + right for left, right in zip(self, other)]
            )

        def _sub_(self, other: "Element") -> "Element":
            return self.parent()(
                [left - right for left, right in zip(self, other)]
            )

        def _neg_(self) -> "Element":
            return self.parent()([-coordinate for coordinate in self])

        def _lmul_(self, scalar: "Element") -> "Element":
            return self.parent()([scalar * coordinate for coordinate in self])

        _rmul_ = _lmul_


def FreeModuleOfRank(base_ring: "Ring", rank: "Integer") -> "Parent":
    r"""Return \(R^n\), built through the chain."""
    return object_of(FiniteRankFreeModules(base_ring), rank=rank, base=base_ring)
