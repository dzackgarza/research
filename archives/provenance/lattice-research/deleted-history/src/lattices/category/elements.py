r"""Parent and element method providers for singular lattice objects."""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, final

if TYPE_CHECKING:
    from category_specs.types import (
        DiscriminantGroup,
        Lattice,
        LatticeAut,
        Matrix,
        RingElement,
        RModuleElement,
        SubModule,
    )


class LatticeParentMethods(metaclass=ABCMeta):
    r"""Methods carried by a single algebraic lattice parent.

    A lattice here is a finite-rank free module equipped with a symmetric,
    nondegenerate integral bilinear form. This is the algebraic-geometry
    lattice notion, not Sage's order-theoretic lattice-poset category.
    """

    @final
    def is_lattice(self) -> bool:
        r"""Return ``True`` because membership in this category is the witness."""
        return True

    @abstractmethod
    def gram_matrix(self) -> Matrix:
        r"""Return the Gram matrix of the bilinear form in the chosen generators."""
        ...

    @abstractmethod
    def rank(self) -> int:
        r"""Return the finite rank of the underlying free module."""
        ...

    @abstractmethod
    def gens(self) -> tuple[RModuleElement, ...]:
        r"""Return the chosen generators used by the lattice presentation."""
        ...

    @abstractmethod
    def b(
        self,
        left: LatticeElementMethods,
        right: LatticeElementMethods,
    ) -> RingElement:
        r"""Evaluate the lattice bilinear form ``b(left, right)``."""
        ...

    @final
    def q(self, vector: LatticeElementMethods) -> RingElement:
        r"""Return the associated diagonal value ``b(vector, vector)``."""
        return self.b(vector, vector)

    @abstractmethod
    def signature_pair(self) -> tuple[int, int]:
        r"""Return the pair ``(positive_rank, negative_rank)``."""
        ...

    @final
    def signature(self) -> int:
        r"""Return ``positive_rank - negative_rank``."""
        positive_rank, negative_rank = self.signature_pair()
        return positive_rank - negative_rank

    @abstractmethod
    def dual_lattice(self) -> Lattice:
        r"""Return the metric dual lattice ``L^\#``."""
        ...

    @abstractmethod
    def discriminant_group(self) -> DiscriminantGroup:
        r"""Return the discriminant group ``L^\# / L`` with its descended form."""
        ...

    @final
    def orthogonal_group(self) -> LatticeAut:
        r"""Return ``O(L)`` as the automorphism object in this lattice category."""
        return self.category().AutCategory().Of(self)


class LatticeElementMethods(metaclass=ABCMeta):
    r"""Methods carried by elements of a single lattice parent."""

    @abstractmethod
    def parent(self) -> LatticeParentMethods:
        r"""Return the lattice parent containing this element."""
        ...

    @abstractmethod
    def to_vector(self) -> tuple[RingElement, ...]:
        r"""Return coordinates in the parent lattice presentation."""
        ...

    @final
    def b(self, other: LatticeElementMethods) -> RingElement:
        r"""Evaluate the parent bilinear form against ``other``."""
        return self.parent().b(self, other)

    @final
    def q(self) -> RingElement:
        r"""Return the diagonal value ``b(self, self)``."""
        return self.parent().q(self)

    @abstractmethod
    def perp(self) -> SubModule:
        r"""Return the orthogonal complement of this element in its parent."""
        ...
