r"""Homsets and morphisms for synthetic lattices."""

from __future__ import annotations

from sage.categories.sets_cat import Sets
from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.element import Element
from sage.structure.parent import Parent

from .domain_algebra import LatticeMorphism as LatticeMorphismCarrier
from .parents import SyntheticLattice


class LatticeHomset(Parent):
    r"""Homset of form-preserving synthetic lattice morphisms."""

    def __init__(self, domain, codomain):
        assert isinstance(domain, SyntheticLattice), (f"expected SyntheticLattice domain; found={type(domain)}")
        assert isinstance(codomain, SyntheticLattice), (f"expected SyntheticLattice codomain; found={type(codomain)}")
        self._domain = domain
        self._codomain = codomain
        from .categories import Lattices

        Parent.__init__(self, category=Lattices(domain.base_ring()).Homsets())

    def _repr_(self):
        return f"Synthetic lattice homset from {self.domain()} to {self.codomain()}"

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def from_matrix(self, matrix_data):
        return LatticeMorphism(self, matrix_data)


class LatticeMorphism(LatticeMorphismCarrier, Element):
    r"""Form-preserving morphism of synthetic lattices."""

    def __init__(self, parent, matrix_data):
        Element.__init__(self, parent)
        domain = parent.domain()
        codomain = parent.codomain()
        matrix_data = matrix(codomain.base_ring(), matrix_data)
        assert matrix_data.nrows() == codomain.rank(), (
            "morphism matrix rows must equal codomain rank; "
            f"rows={matrix_data.nrows()}, codomain_rank={codomain.rank()}"
        )
        assert matrix_data.ncols() == domain.rank(), (
            "morphism matrix columns must equal domain rank; "
            f"columns={matrix_data.ncols()}, domain_rank={domain.rank()}"
        )
        pulled_form = matrix(QQ, matrix_data).transpose() * codomain.gram_matrix() * matrix(QQ, matrix_data)
        assert pulled_form == domain.gram_matrix(), (
            "lattice morphisms are form-preserving by definition; "
            f"pulled_form={pulled_form}, domain_gram={domain.gram_matrix()}; fix the caller's matrix"
        )
        matrix_data.set_immutable()
        self._matrix = matrix_data

    def _repr_(self):
        return f"Synthetic lattice morphism represented by\n{self.matrix()}"

    def matrix(self):
        return self._matrix

    def domain(self):
        return self.parent().domain()

    def codomain(self):
        return self.parent().codomain()

    def is_isometry(self):
        # Every lattice morphism is form-preserving by construction; it is an
        # isometry exactly when it is additionally an isomorphism (invertible),
        # e.g. U -> U^2 on the hyperbolic plane is form-preserving but not one.
        return self.matrix().is_square() and self.matrix().is_invertible()

    def __call__(self, element):
        return self._call_(element)

    def _call_(self, element):
        element = self.domain()(element) if element.parent() is not self.domain() else element
        image = self.matrix() * matrix(self.domain().base_ring(), self.domain().rank(), 1, list(element.coefficient_vector()))
        return self.codomain()([image[i, 0] for i in range(self.codomain().rank())])

    def kernel(self):
        basis = self.matrix().right_kernel().basis_matrix()
        if basis.nrows() == 0:
            return self.domain().sublattice(matrix(QQ, 0, self.domain().rank()), "ker")
        return self.domain().sublattice(basis, "ker")

    def image(self):
        return self.codomain().sublattice(self.matrix().columns(), "im")

    def is_injective(self):
        r"""[total] — full column rank (spec 3.5; free modules carry no torsion)."""
        return self.matrix().rank() == self.domain().rank()

    def induced_map_on_discriminant_group(self):
        r"""The per-morphism functor to O(q_L) (spec 3.3); defined for
        endomorphisms of an integral nondegenerate lattice — the lattice-side
        discriminant vocabulary gates the rest."""
        assert self.domain() == self.codomain(), (
            "the induced discriminant action needs an endomorphism; "
            f"domain={self.domain()}, codomain={self.codomain()}"
        )
        return self.domain().discriminant_group().action_of_isometry(self)

    def is_surjective(self):
        r"""[total] — the image is the whole codomain (spec 3.5)."""
        return self.image() == self.codomain()

    def im_gens(self):
        return tuple(self(self.domain().gen(i)) for i in range(self.domain().rank()))

    def lift(self, element):
        element = self.codomain()(element) if element.parent() is not self.codomain() else element
        rhs = matrix(QQ, self.codomain().rank(), 1, list(element.coefficient_vector()))
        solution = matrix(QQ, self.matrix()).solve_right(rhs)
        coordinates = [solution[i, 0] for i in range(self.domain().rank())]
        if not all(coordinate in self.domain().base_ring() for coordinate in coordinates):
            raise ValueError(
                "lift has coordinates outside the domain base ring; "
                f"coordinates={coordinates}, base_ring={self.domain().base_ring()}"
            )
        return self.domain()(coordinates)

    # -- algebra available under form-preservation (composition monoid; the
    # -- full End(L) RING with sums/nilpotents lives on module endomorphisms,
    # -- V0d ratification 2026-07-03) --------------------------------------

    def __mul__(self, other):
        r"""Composition: ``(f * g)(x) = f(g(x))``."""
        assert isinstance(other, LatticeMorphism), (
            f"morphism composition needs a LatticeMorphism; found={type(other)}"
        )
        assert other.codomain() == self.domain(), (
            "morphisms compose only when the inner codomain matches the outer "
            f"domain; inner_codomain={other.codomain()}, outer_domain={self.domain()}"
        )
        return other.domain().Hom(self.codomain()).from_matrix(self.matrix() * other.matrix())

    def __pow__(self, n):
        assert self.domain() == self.codomain(), (
            f"powers need an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        )
        n = int(n)
        if n < 0:
            return self.inverse() ** (-n)
        power = self.matrix() ** n if n > 0 else self.matrix().parent().identity_matrix()
        return self.parent().from_matrix(power)

    def inverse(self):
        if not self.is_isometry():
            raise ValueError(
                "only isometries are invertible in the lattice category; "
                f"matrix={self.matrix()}"
            )
        return self.codomain().Hom(self.domain()).from_matrix(self.matrix().inverse())

    def is_identity(self):
        return self.domain() == self.codomain() and self.matrix().is_one()

    def order(self):
        r"""Multiplicative order (delegated); ``+Infinity`` for infinite order."""
        assert self.domain() == self.codomain(), (
            f"order needs an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        )
        if self.is_identity():
            # Sage's multiplicative_order IndexErrors on the identity matrix
            # (upstream bug; gap-ledger row records it)
            return ZZ.one()
        return self.matrix().multiplicative_order()

    def is_nilpotent(self):
        assert self.domain() == self.codomain(), (
            f"nilpotence needs an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        )
        return (self.matrix() ** self.domain().rank()).is_zero()

    def is_idempotent(self):
        assert self.domain() == self.codomain(), (
            f"idempotence needs an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        )
        return self.matrix() * self.matrix() == self.matrix()

    def is_unipotent(self):
        r"""Whether ``f - id`` is nilpotent (parabolic-type isometries)."""
        assert self.domain() == self.codomain(), (
            f"unipotence needs an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        )
        return ((self.matrix() - self.matrix().parent().identity_matrix()) ** self.domain().rank()).is_zero()

    def __eq__(self, other):
        return (
            isinstance(other, LatticeMorphism)
            and self.domain() == other.domain()
            and self.codomain() == other.codomain()
            and self.matrix() == other.matrix()
        )

    def __hash__(self):
        return hash((self.domain(), self.codomain(), self.matrix()))


class LatticeSimilarity(Element):
    r"""Similarity of synthetic lattices preserving the form up to a scalar."""

    def __init__(self, domain, codomain, matrix_data, scalar):
        Element.__init__(self, LatticeHomset(domain, codomain))
        matrix_data = matrix(codomain.base_ring(), matrix_data)
        scalar = QQ(scalar)
        assert matrix_data.nrows() == codomain.rank(), (
            "similarity matrix rows must equal codomain rank; "
            f"rows={matrix_data.nrows()}, codomain_rank={codomain.rank()}"
        )
        assert matrix_data.ncols() == domain.rank(), (
            "similarity matrix columns must equal domain rank; "
            f"columns={matrix_data.ncols()}, domain_rank={domain.rank()}"
        )
        pulled_form = matrix(QQ, matrix_data).transpose() * codomain.gram_matrix() * matrix(QQ, matrix_data)
        assert pulled_form == scalar * domain.gram_matrix(), (
            "lattice similarities preserve the form by the declared scalar; "
            f"pulled_form={pulled_form}, scalar={scalar}, domain_gram={domain.gram_matrix()}; fix the caller's matrix or scalar"
        )
        matrix_data.set_immutable()
        self._matrix = matrix_data
        self._scalar = scalar

    def _repr_(self):
        return f"Synthetic lattice similarity with scalar {self.scalar()} represented by\n{self.matrix()}"

    def matrix(self):
        return self._matrix

    def scalar(self):
        return self._scalar

    def domain(self):
        return self.parent().domain()

    def codomain(self):
        return self.parent().codomain()

    def __call__(self, element):
        element = self.domain()(element) if element.parent() is not self.domain() else element
        image = self.matrix() * matrix(self.domain().base_ring(), self.domain().rank(), 1, list(element.coefficient_vector()))
        return self.codomain()([image[i, 0] for i in range(self.codomain().rank())])


LatticeHomset.Element = LatticeMorphism
