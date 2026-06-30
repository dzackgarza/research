r"""Homsets and morphisms for synthetic lattices."""

from __future__ import annotations

from sage.categories.sets_cat import Sets
from sage.matrix.constructor import matrix
from sage.rings.rational_field import QQ
from sage.structure.element import Element
from sage.structure.parent import Parent

from parents import SyntheticLattice


class LatticeHomset(Parent):
    r"""Homset of form-preserving synthetic lattice morphisms."""

    Element = None

    def __init__(self, domain, codomain):
        assert isinstance(domain, SyntheticLattice), f"expected SyntheticLattice domain; found={type(domain)}"
        assert isinstance(codomain, SyntheticLattice), f"expected SyntheticLattice codomain; found={type(codomain)}"
        self._domain = domain
        self._codomain = codomain
        Parent.__init__(self, category=Sets())

    def _repr_(self):
        return f"Synthetic lattice homset from {self.domain()} to {self.codomain()}"

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def from_matrix(self, matrix_data):
        return LatticeMorphism(self, matrix_data)


class LatticeMorphism(Element):
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
        if pulled_form != domain.gram_matrix():
            raise ValueError("lattice morphisms are form-preserving by definition")
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

    def __call__(self, element):
        return self._call_(element)

    def _call_(self, element):
        element = self.domain()(element) if element.parent() is not self.domain() else element
        image = self.matrix() * matrix(self.domain().base_ring(), self.domain().rank(), 1, list(element.coordinates()))
        return self.codomain()([image[i, 0] for i in range(self.codomain().rank())])

    def kernel(self):
        basis = self.matrix().right_kernel().basis_matrix()
        if basis.nrows() == 0:
            return self.domain().sublattice(matrix(QQ, 0, self.domain().rank()), "ker")
        return self.domain().sublattice(basis, "ker")

    def image(self):
        return self.codomain().sublattice(self.matrix().columns(), "im")

    def im_gens(self):
        return tuple(self(self.domain().gen(i)) for i in range(self.domain().rank()))

    def lift(self, element):
        element = self.codomain()(element) if element.parent() is not self.codomain() else element
        rhs = matrix(QQ, self.codomain().rank(), 1, list(element.coordinates()))
        solution = matrix(QQ, self.matrix()).solve_right(rhs)
        coordinates = [solution[i, 0] for i in range(self.domain().rank())]
        assert all(coordinate in self.domain().base_ring() for coordinate in coordinates), (
            "lift has coordinates outside the domain base ring; "
            f"coordinates={coordinates}, base_ring={self.domain().base_ring()}"
        )
        return self.domain()(coordinates)

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
        if pulled_form != scalar * domain.gram_matrix():
            raise ValueError("lattice similarities preserve the form by the declared scalar")
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
        image = self.matrix() * matrix(self.domain().base_ring(), self.domain().rank(), 1, list(element.coordinates()))
        return self.codomain()([image[i, 0] for i in range(self.codomain().rank())])
