r"""Free lattices of finite rank, constructed through the chain.

A lattice **is** a module with a form -- one object, not a form paired with a
separate module.  That is what this level makes true: the form is built on
``self``, so ``L.form().module() is L`` and an element of the lattice is an
element of its own underlying module.  There is no forgetful step to reach
around, at this level or any other.

The rest follows from the levels below.  Rank and coordinates come from
``FiniteRankFreeModules``, which declares the underlying set to be the product
\(R\times\cdots\times R\); this level adds a form and nothing else.
"""

from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    SymmetricBilinearFormModules,
)
from dzack_research.preamble.categories.modules.pure.free_modules import (
    FiniteRankFreeModules,
)
from dzack_research.preamble.owned_category import OwnedCategoryMixin, object_of
from sage.categories.category_types import Category_over_base_ring


class FiniteRankFreeLattices(OwnedCategoryMixin, Category_over_base_ring):
    r"""\(R^n\) with a symmetric bilinear form."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free lattices of finite rank"

    def super_categories(self) -> list:
        return [
            SymmetricBilinearFormModules(self.base_ring()),
            FiniteRankFreeModules(self.base_ring()),
        ]

    class ParentMethods:
        def __init__(self, gram: tuple, **rest: object) -> None:
            self._gram = gram
            super().__init__(rank=len(gram), **rest)

        def gram_matrix(self) -> tuple:
            r"""The matrix of the form on the coordinate generators."""
            return self._gram

        def _form_morphism(self) -> "Form":
            r"""Return the form, built on this object.

            Built here rather than handed in, because a form on \(M\) cannot
            exist before \(M\) does: its homset is the forms *on this module*.
            Stated as a pairing rather than a Gram matrix -- the form surface
            takes either, and a matrix is a presentation against a chosen
            framing, which this level does not have and does not need.
            """
            # Local: the form surface is a level below and imports upward.
            from dzack_research.preamble.categories.forms.forms import (
                BilinearFormHomset,
            )

            gram = self._gram
            rank = self.rank()
            zero = self.base_ring().zero()

            def pairing(left: "Element", right: "Element") -> "Element":
                r"""\(b(x,y)=\sum_{i,j}x_i g_{ij} y_j\)."""
                return sum(
                    (
                        left[i] * gram[i][j] * right[j]
                        for i in range(rank)
                        for j in range(rank)
                    ),
                    zero,
                )

            return BilinearFormHomset(self, self.base_ring())(pairing)

        def _repr_(self) -> str:
            return f"Free lattice of rank {self.rank()} over {self.base_ring()}"


def FreeLatticeOfRank(base_ring: "Ring", gram: tuple) -> "Parent":
    r"""Return \(R^n\) with the symmetric bilinear form given by ``gram``."""
    return object_of(
        FiniteRankFreeLattices(base_ring),
        gram=tuple(tuple(base_ring(entry) for entry in row) for row in gram),
        base=base_ring,
    )
