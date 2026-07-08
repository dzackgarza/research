r"""Homsets and morphisms for synthetic lattices."""

from __future__ import annotations

from typing import Any

from sage.matrix.constructor import matrix
from sage.modules.free_module_element import vector
from sage.rings.rational_field import QQ
from sage.structure.element import Element
from sage.structure.parent import Parent

from .. import lexicon
from ..lexicon import Lattice, LatticeElement
from ..objects.parents import SyntheticLattice
from ..sage_patches import multiplicative_order


class LatticeHomset(Parent):
    r"""Homset of form-preserving synthetic lattice morphisms."""

    def __init__(self, domain: Lattice | SyntheticLattice, codomain: Lattice | SyntheticLattice) -> None:
        assert isinstance(domain, SyntheticLattice), f"expected SyntheticLattice domain; found={type(domain)}"
        assert isinstance(codomain, SyntheticLattice), f"expected SyntheticLattice codomain; found={type(codomain)}"
        self._domain = domain
        self._codomain = codomain
        from ..objects.categories import Lattices

        Parent.__init__(self, category=Lattices(domain.base_ring()).Homsets())

    def _repr_(self) -> str:
        return f"Synthetic lattice homset from {self.domain()} to {self.codomain()}"

    def domain(self) -> SyntheticLattice:
        return self._domain

    def codomain(self) -> SyntheticLattice:
        return self._codomain

    def from_matrix(self, matrix_data: object) -> LatticeMorphism:
        return LatticeMorphism(self, matrix_data)


class LatticeMorphism(lexicon.LatticeMorphism, Element):
    r"""Form-preserving morphism of synthetic lattices."""

    def __init__(self, parent: LatticeHomset, matrix_data: Any) -> None:
        Element.__init__(self, parent)
        domain = parent.domain()
        codomain = parent.codomain()
        matrix_data = matrix(codomain.base_ring(), matrix_data)
        assert matrix_data.nrows() == codomain.rank(), f"morphism matrix rows must equal codomain rank; rows={matrix_data.nrows()}, codomain_rank={codomain.rank()}"
        assert matrix_data.ncols() == domain.rank(), f"morphism matrix columns must equal domain rank; columns={matrix_data.ncols()}, domain_rank={domain.rank()}"
        pulled_form = matrix(QQ, matrix_data).transpose() * codomain.gram_matrix() * matrix(QQ, matrix_data)
        assert pulled_form == domain.gram_matrix(), (
            f"lattice morphisms are form-preserving by definition; pulled_form={pulled_form}, domain_gram={domain.gram_matrix()}; fix the caller's matrix"
        )
        matrix_data.set_immutable()
        self._matrix = matrix_data

    def _repr_(self) -> str:
        return f"Synthetic lattice morphism represented by\n{self.matrix()}"

    def matrix(self) -> Any:
        return self._matrix

    def domain(self) -> Any:
        return self.parent().domain()

    def codomain(self) -> Any:
        return self.parent().codomain()

    def is_isometry(self) -> bool:
        # Every lattice morphism is form-preserving by construction; it is an
        # isometry exactly when it is additionally an isomorphism (invertible),
        # e.g. U -> U^2 on the hyperbolic plane is form-preserving but not one.
        return bool(self.matrix().is_square() and self.matrix().is_invertible())

    def __call__(self, element: LatticeElement) -> Any:
        return self._call_(element)

    def _call_(self, element: LatticeElement) -> Any:
        element = self.domain()(element) if element.parent() is not self.domain() else element
        return self.codomain()(self.matrix() * vector(self.domain().base_ring(), element.coefficient_vector()))

    def kernel(self) -> Any:
        basis = self.matrix().right_kernel().basis_matrix()
        if basis.nrows() == 0:
            return self.domain().sublattice(matrix(QQ, 0, self.domain().rank()), "ker")
        return self.domain().sublattice(basis, "ker")

    def image(self) -> Any:
        return self.codomain().sublattice(self.matrix().columns(), "im")

    def is_injective(self) -> bool:
        r"""[total] — full column rank (spec 3.5; free modules carry no torsion)."""
        return bool(self.matrix().rank() == self.domain().rank())

    def is_primitive_embedding(self) -> bool:
        r"""Whether this injective morphism has primitive image in its codomain.

        Equivalently, the module cokernel is torsion-free.  The spike's
        general infinite-cokernel object is not implemented, so the owned
        computation goes through the codomain's primitive-submodule predicate.
        """
        return bool(self.is_injective() and self.codomain().is_primitive(self.image()))

    def cokernel(self) -> Any:
        r"""``codomain / image`` (spec 3.5: [total] exactly when the cokernel
        is finite, i.e. the image has full rank in the codomain; the
        infinite-cokernel case is a gap-ledger contract)."""
        image = self.image()
        assert image.rank() == self.codomain().rank(), (
            "cokernel is computed exactly when it is finite (full-rank image); "
            f"image rank={image.rank()}, codomain rank={self.codomain().rank()}; "
            "the infinite-cokernel case is gap-ledger work"
        )
        return self.codomain().finite_quotient(image)

    def induced_map_on_discriminant_group(self) -> Any:
        r"""The per-morphism functor to O(q_L) (spec 3.3); defined for
        endomorphisms of an integral nondegenerate lattice — the lattice-side
        discriminant vocabulary gates the rest."""
        assert self.domain() == self.codomain(), f"the induced discriminant action needs an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        return self.domain().discriminant_group().action_of_isometry(self)

    def is_surjective(self) -> bool:
        r"""[total] — the image is the whole codomain (spec 3.5)."""
        return bool(self.image() == self.codomain())

    def im_gens(self) -> tuple[Any, ...]:
        return tuple(self(self.domain().gen(i)) for i in range(self.domain().rank()))

    def lift(self, element: LatticeElement) -> Any:
        element = self.codomain()(element) if element.parent() is not self.codomain() else element
        rhs = vector(QQ, element.coefficient_vector())
        solution = matrix(QQ, self.matrix()).solve_right(rhs)
        coordinates = [solution[i] for i in range(self.domain().rank())]
        assert all(coordinate in self.domain().base_ring() for coordinate in coordinates), (
            f"lift has coordinates outside the domain base ring; coordinates={coordinates}, base_ring={self.domain().base_ring()}"
        )
        return self.domain()(coordinates)

    # -- algebra available under form-preservation (composition monoid; the
    # -- full End(L) RING with sums/nilpotents lives on module endomorphisms,
    # -- V0d ratification 2026-07-03) --------------------------------------

    def __mul__(self, other: object) -> Any:
        r"""Composition: ``(f * g)(x) = f(g(x))``."""
        assert isinstance(other, LatticeMorphism), f"morphism composition needs a LatticeMorphism; found={type(other)}"
        assert other.codomain() == self.domain(), (
            f"morphisms compose only when the inner codomain matches the outer domain; inner_codomain={other.codomain()}, outer_domain={self.domain()}"
        )
        return other.domain().Hom(self.codomain()).from_matrix(self.matrix() * other.matrix())

    def __pow__(self, n: int) -> Any:
        assert self.domain() == self.codomain(), f"powers need an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        n = int(n)
        if n < 0:
            return self.inverse() ** (-n)
        power = self.matrix() ** n if n > 0 else self.matrix().parent().identity_matrix()
        return self.parent().from_matrix(power)

    def inverse(self) -> Any:
        assert self.is_isometry(), f"only isometries are invertible in the lattice category; matrix={self.matrix()}"
        return self.codomain().Hom(self.domain()).from_matrix(self.matrix().inverse())

    def is_identity(self) -> bool:
        return bool(self.domain() == self.codomain() and self.matrix().is_one())

    def order(self) -> Any:
        r"""Multiplicative order (computed by Sage); ``+Infinity`` for infinite order."""
        assert self.domain() == self.codomain(), f"order needs an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        return multiplicative_order(self.matrix())

    def is_nilpotent(self) -> bool:
        assert self.domain() == self.codomain(), f"nilpotence needs an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        return bool((self.matrix() ** self.domain().rank()).is_zero())

    def is_idempotent(self) -> bool:
        assert self.domain() == self.codomain(), f"idempotence needs an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        return bool(self.matrix() * self.matrix() == self.matrix())

    def is_unipotent(self) -> bool:
        r"""Whether ``f - id`` is nilpotent (parabolic-type isometries)."""
        assert self.domain() == self.codomain(), f"unipotence needs an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        return bool(((self.matrix() - self.matrix().parent().identity_matrix()) ** self.domain().rank()).is_zero())

    def __eq__(self, other: object) -> bool:
        return bool(isinstance(other, LatticeMorphism) and self.domain() == other.domain() and self.codomain() == other.codomain() and self.matrix() == other.matrix())

    def __hash__(self) -> int:
        return hash((self.domain(), self.codomain(), self.matrix()))


class LatticeSimilarity(Element):
    r"""Similarity of synthetic lattices preserving the form up to a scalar."""

    def __init__(
        self,
        domain: Lattice | SyntheticLattice,
        codomain: Lattice | SyntheticLattice,
        matrix_data: Any,
        scalar: Any,
    ) -> None:
        Element.__init__(self, LatticeHomset(domain, codomain))
        matrix_data = matrix(codomain.base_ring(), matrix_data)
        scalar = QQ(scalar)
        assert matrix_data.nrows() == codomain.rank(), f"similarity matrix rows must equal codomain rank; rows={matrix_data.nrows()}, codomain_rank={codomain.rank()}"
        assert matrix_data.ncols() == domain.rank(), f"similarity matrix columns must equal domain rank; columns={matrix_data.ncols()}, domain_rank={domain.rank()}"
        pulled_form = matrix(QQ, matrix_data).transpose() * codomain.gram_matrix() * matrix(QQ, matrix_data)
        assert pulled_form == scalar * domain.gram_matrix(), (
            "lattice similarities preserve the form by the declared scalar; "
            f"pulled_form={pulled_form}, scalar={scalar}, domain_gram={domain.gram_matrix()}; fix the caller's matrix or scalar"
        )
        matrix_data.set_immutable()
        self._matrix = matrix_data
        self._scalar = scalar

    def _repr_(self) -> str:
        return f"Synthetic lattice similarity with scalar {self.scalar()} represented by\n{self.matrix()}"

    def matrix(self) -> Any:
        return self._matrix

    def scalar(self) -> Any:
        return self._scalar

    def domain(self) -> Any:
        return self.parent().domain()

    def codomain(self) -> Any:
        return self.parent().codomain()

    def __call__(self, element: LatticeElement) -> Any:
        element = self.domain()(element) if element.parent() is not self.domain() else element
        image = self.matrix() * matrix(
            self.domain().base_ring(),
            self.domain().rank(),
            1,
            list(element.coefficient_vector()),
        )
        return self.codomain()([image[i, 0] for i in range(self.codomain().rank())])


LatticeHomset.Element = LatticeMorphism
