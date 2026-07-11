r"""Homsets and morphisms for synthetic lattices."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, cast

from sage.matrix.constructor import matrix
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.element import Element
from sage.structure.parent import Parent

from .. import lexicon
from ..lexicon import Lattice, LatticeElement
from ..objects.parents import SyntheticLattice
from ..sage_patches import multiplicative_order


class Subobject:
    r"""A subobject of a lattice: a plain lattice ``L`` together with its
    monomorphism (inclusion) ``f: L -> M`` into an ambient ``M``. A subobject
    IS the pair ``(L, f)`` -- no lattice ever stores its own ambient, and every
    operation relating ``L`` to ``M`` composes ``f`` rather than reindexing
    coordinates.

    Constructed from an injective form-preserving morphism (``M.subobject(...)``,
    an image, a kernel, a complement); ``lattice()`` is the plain ``(R, G)``
    domain and ``inclusion()`` is the embedding.
    """

    def __init__(self, inclusion: lexicon.LatticeMorphism) -> None:
        assert isinstance(inclusion, LatticeMorphism), f"a subobject is built from a lattice morphism; found={type(inclusion)}"
        assert inclusion.is_injective(), f"a subobject's inclusion must be a monomorphism; matrix={inclusion.matrix()}"
        self._inclusion = inclusion

    def _repr_(self) -> str:
        return f"Subobject {self.lattice()!r} of {self.ambient()!r}"

    __repr__ = _repr_

    def lattice(self) -> Any:
        return self._inclusion.domain()

    def inclusion(self) -> lexicon.LatticeMorphism:
        return self._inclusion

    def ambient(self) -> Any:
        return self._inclusion.codomain()

    def rank(self) -> Any:
        return self.lattice().rank()

    def gram_matrix(self) -> Any:
        return self.lattice().gram_matrix()

    def cokernel(self) -> SyntheticLatticeCokernel:
        r"""The cokernel ``M / L`` of the inclusion."""
        return self._inclusion.cokernel()

    def is_primitive(self) -> bool:
        r"""Primitive iff the inclusion's cokernel is torsion-free."""
        return self._inclusion.cokernel().is_torsion_free()

    def __getattr__(self, name: str) -> Any:
        # A subobject exposes its lattice's intrinsic vocabulary (determinant,
        # signature_pair, roots, twist, discriminant_group, is_even, ...); the
        # subobject-specific operations (inclusion, orthogonal_complement,
        # is_primitive, is_isometric/is_submodule against another subobject) are
        # defined explicitly above and take precedence.
        if name.startswith("_"):
            raise AttributeError(name)
        return getattr(self.lattice(), name)

    def direct_sum(self, *others: Any, label: str = "direct_sum") -> Any:
        lattices = [other.lattice() if isinstance(other, Subobject) else other for other in others]
        return self.lattice().direct_sum(*lattices, label=label)

    def is_isometric(self, other: Any) -> bool:
        other_lattice = other.lattice() if isinstance(other, Subobject) else other
        return bool(self.lattice().is_isometric(other_lattice))

    def is_submodule(self, other: Any) -> bool:
        r"""A subobject is a submodule of its own ambient; against another
        subobject of the same ambient, compose the inclusions."""
        if isinstance(other, Subobject):
            assert self.ambient() == other.ambient(), "submodule test needs a common ambient"
            module = self.ambient().base_ring() ** self.ambient().rank()
            return bool(module.span(self._inclusion.matrix().columns()).is_submodule(module.span(other.inclusion().matrix().columns())))
        return bool(self.ambient() == other)

    def orthogonal_complement(self, label: str = "orthogonal_complement") -> Subobject:
        r"""The orthogonal complement of ``L`` inside ``M``, as a subobject
        ``K -> M`` -- ``K`` is the integral points of ``M`` pairing to zero with
        every image of ``L``. Composed from the inclusion matrix and ``M``'s form,
        never from a stored ambient."""
        ambient = self.ambient()
        pairing = ambient.gram_matrix() * self._inclusion.matrix()  # M_rank x L_rank; columns = b(., f(e_i))
        kernel_rows = matrix(ZZ, pairing).transpose().right_kernel().basis_matrix()
        return cast(Subobject, ambient._subobject_from_ambient_rows(kernel_rows, label))

    def saturation(self, label: str = "saturation") -> Subobject:
        r"""The primitive closure of ``L`` in ``M`` (its saturation), as a
        subobject ``K -> M`` with ``L <= K`` and torsion-free cokernel."""
        ambient = self.ambient()
        rational_span = (QQ ** ambient.rank()).span(self._inclusion.matrix().transpose().rows(), QQ)
        saturated_rows = (ZZ ** ambient.rank()).intersection(rational_span).basis_matrix()
        return cast(Subobject, ambient._subobject_from_ambient_rows(saturated_rows, label))


class SyntheticLatticeCokernel(lexicon.LatticeCokernel):
    r"""The cokernel ``M / im(f)`` of a lattice morphism, as a finitely generated
    R-module (free plus torsion). A first-class object in the abelian category
    ``R-Mod``: it exists and is computable by contract for any morphism, so its
    predicates (torsion-freeness, order) are asked of the object, never
    reconstructed by the caller from matrix internals."""

    def __init__(self, module_quotient: Any) -> None:
        self._quotient = module_quotient

    def is_torsion_free(self) -> bool:
        r"""No torsion: every invariant factor of the module is a free (``ZZ``)
        summand. This is exactly the primitivity condition on the inclusion."""
        return all(invariant == 0 for invariant in self._quotient.invariants())

    def cardinality(self) -> Any:
        r"""The order of the cokernel (infinite when the image is not full rank)."""
        return self._quotient.cardinality()

    def invariants(self) -> tuple[Any, ...]:
        return tuple(self._quotient.invariants())


class LatticeHomset(lexicon.LatticeHomset, Parent):
    r"""Homset of form-preserving synthetic lattice morphisms."""

    # Sage's parent convention: the homset's element class (assigned after
    # LatticeMorphism is defined below).
    Element: ClassVar[type]

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

    if TYPE_CHECKING:
        # The parent is always a synthetic lattice homset.
        def parent(self) -> LatticeHomset: ...

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

    def kernel(self) -> Subobject:
        r"""The kernel as a subobject of the domain."""
        domain = self.domain()
        basis = self.matrix().right_kernel().basis_matrix()
        return cast(Subobject, domain.subobject([domain(list(row)) for row in basis.rows()], "ker"))

    def image(self) -> Subobject:
        r"""The image as a subobject of the codomain: the sublattice spanned by
        the images of the domain generators, together with its inclusion."""
        codomain = self.codomain()
        return cast(Subobject, codomain.subobject([codomain(list(column)) for column in self.matrix().columns()], "im"))

    def is_injective(self) -> bool:
        r"""[total] — full column rank (spec 3.5; free modules carry no torsion)."""
        return bool(self.matrix().rank() == self.domain().rank())

    def is_primitive_embedding(self) -> bool:
        r"""An injective morphism whose cokernel is torsion-free -- i.e. it has
        primitive image. Nothing more than "the cokernel is torsion-free"."""
        return self.is_injective() and self.cokernel().is_torsion_free()

    def cokernel(self) -> SyntheticLatticeCokernel:
        r"""The cokernel ``codomain / image`` (spec 3.5). ``R-Mod`` is an abelian
        category, so the cokernel exists and is computable by contract for EVERY
        morphism -- the finite (full-rank image) case is the special one, not the
        only one."""
        codomain = self.codomain()
        codomain_module = codomain.base_ring() ** codomain.rank()
        image_span = codomain_module.span(self.matrix().columns())
        return SyntheticLatticeCokernel(codomain_module.quotient(image_span))

    def induced_map_on_discriminant_group(self) -> Any:
        r"""The per-morphism functor to O(q_L) (spec 3.3); defined for
        endomorphisms of an integral nondegenerate lattice — the lattice-side
        discriminant vocabulary gates the rest."""
        assert self.domain() == self.codomain(), f"the induced discriminant action needs an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        return self.domain().discriminant_group().action_of_isometry(self)

    def is_surjective(self) -> bool:
        r"""[total] — the cokernel is trivial (spec 3.5)."""
        return bool(self.cokernel().cardinality() == 1)

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


class LatticeSimilarity(lexicon.LatticeSimilarity, Element):
    r"""Similarity of synthetic lattices preserving the form up to a scalar."""

    if TYPE_CHECKING:
        # The parent is the homset of the underlying domain/codomain pair.
        def parent(self) -> LatticeHomset: ...

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
