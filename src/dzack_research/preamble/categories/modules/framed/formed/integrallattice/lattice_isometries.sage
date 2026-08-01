r"""``LatticeIsometries`` — morphisms of integral lattices that preserve the form.

``L.Aut()`` is the isometry Homset.  Its element constructor takes a dict of
generator images ``{e_i: image}`` (or a list of images / a matrix); isometry
is checked on ``morphism.to_matrix()``.

Invariant / coinvariant lattices live on the lattice
(``L.invariant_lattice(action)``, ``L.coinvariant_lattice(action)``);
morphisms delegate to their domain.
"""

from typing import Any

from sage.categories.category import Category
from sage.matrix.constructor import matrix
from sage.matrix.special import identity_matrix
from sage.rings.integer_ring import ZZ

class LatticeIsometries(Category):
    r"""Isometries of integral lattices (as Hom morphisms / Aut elements)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice isometries"

    def super_categories(self) -> list:
        return [LatticeHomomorphisms()]

    class ParentMethods:
        r"""Homset methods: element construction is the isometry constructor."""

        def __call__(self: Any, x: Any, *args: Any, **kwargs: Any) -> Any:
            r"""Construct an isometry from images, a dictionary, or a matrix.

            For a chosen direct sum, a dictionary may specify images of entire
            summand subobjects.

            An isometry is a morphism that is invertible, and over $\mathbb Z$
            that is the determinant being a unit.  Preserving the form is the
            morphism's own condition and is checked there.
            """
            domain = self.domain()
            codomain = self.codomain()
            morphism = LatticeHomomorphisms.ParentMethods.__call__(self, x)

            mat = matrix(ZZ, morphism.matrix())
            assert mat.nrows() == domain.rank() and mat.ncols() == codomain.rank(), (
                f"isometry matrix shape {mat.nrows()}×{mat.ncols()} does not "
                f"match ranks {domain.rank()}→{codomain.rank()}"
            )
            assert mat.det() in (ZZ(1), ZZ(-1)), (
                f"an isometry is invertible over Z, so its determinant is a "
                f"unit; got {mat.det()}"
            )
            return refine(morphism, LatticeIsometries())

    class MorphismMethods:
        r"""Methods on isometries refined into this category.

        ``to_matrix`` / ``is_identity`` / ``is_involution`` / composition are
        the isometry vocabulary; application is Sage's native morphism call.
        """

        def to_matrix(self: Any) -> Any:
            """Return the matrix of this isometry on the domain basis."""
            return self.matrix()

        def is_identity(self: Any) -> bool:
            """Return whether this isometry is the identity (matrix test)."""
            mat = self.to_matrix()
            return bool(mat == identity_matrix(ZZ, mat.nrows()))

        def is_involution(self: Any) -> bool:
            r"""Return whether $I^{2}=\mathrm{id}$."""
            return (self * self).is_identity()

        def __mul__(self: Any, other: Any) -> Any:
            """Compose isometries by matrix product through the Homset."""
            if not isinstance(other, FormMorphism):
                return NotImplemented
            return self.domain().Aut()(self.to_matrix() * other.matrix())

        def invariant_lattice(self: Any) -> Any:
            r"""Return $L^{+}=L^{\langle I\rangle}$ via the domain lattice."""
            return self.domain().invariant_lattice(self)

        def coinvariant_lattice(self: Any) -> Any:
            r"""Return the coinvariant lattice via the domain lattice."""
            return self.domain().coinvariant_lattice(self)

        def coinvariant_inclusion(self: Any) -> Any:
            r"""Return the coinvariant inclusion via the domain lattice."""
            return self.domain().coinvariant_inclusion(self)
