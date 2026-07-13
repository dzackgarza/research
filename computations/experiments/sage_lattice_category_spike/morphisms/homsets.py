r"""Homsets and morphisms for synthetic lattices."""

from __future__ import annotations

import warnings
from typing import TYPE_CHECKING, Any, ClassVar, cast

from sage.categories.homset import Homset
from sage.matrix.constructor import column_matrix, matrix
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.element import Element
from sage.structure.parent import Parent

from .. import lexicon
from ..lexicon import Lattice, LatticeElement, SageMorphism
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

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Subobject):
            return self.inclusion() == other.inclusion()
        if isinstance(other, SyntheticLattice):
            warnings.warn(
                "a subobject and a plain lattice are categorically distinct; compare a subobject through its inclusion",
                UserWarning,
                stacklevel=2,
            )
        return False

    def __hash__(self) -> int:
        return hash(self.inclusion())

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

    def index(self) -> Any:
        r"""The index ``[M : L]`` of the subobject in its ambient -- the order of
        the cokernel (infinite when ``L`` is not full rank in ``M``)."""
        return self._inclusion.index()

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

    def _span_in_codomain(self) -> Any:
        r"""The image of the carried inclusion as a module inside the
        codomain's coordinate module -- the shared substrate of the subobject
        algebra (sum, intersection)."""
        codomain = self.ambient()
        return (QQ ** codomain.rank()).span(matrix(QQ, self._inclusion.matrix()).columns(), codomain.base_ring())

    def sum(self, other: Subobject, label: str = "sum") -> Subobject:
        r"""The subobject sum ``L1 + L2`` inside the common codomain: the
        span of both images, carried with its inclusion (#100 T4: the burden
        transferred from the deleted bare-lattice spelling)."""
        assert isinstance(other, Subobject), f"subobject sum takes a subobject of the same codomain; found={type(other)}"
        assert self.ambient() == other.ambient(), f"subobject sum needs a common codomain; left={self.ambient()}, right={other.ambient()}"
        module = self._span_in_codomain() + other._span_in_codomain()
        return cast(Subobject, self.ambient()._subobject_from_rows(module.basis_matrix(), label))

    def intersection(self, other: Subobject, label: str = "intersection") -> Subobject:
        r"""The subobject intersection ``L1 ∩ L2`` inside the common
        codomain, carried with its inclusion."""
        assert isinstance(other, Subobject), f"subobject intersection takes a subobject of the same codomain; found={type(other)}"
        assert self.ambient() == other.ambient(), f"subobject intersection needs a common codomain; left={self.ambient()}, right={other.ambient()}"
        module = self._span_in_codomain().intersection(other._span_in_codomain())
        return cast(Subobject, self.ambient()._subobject_from_rows(module.basis_matrix(), label))

    def orthogonal_complement(self, label: str = "orthogonal_complement") -> Subobject:
        r"""The orthogonal complement of ``L`` inside ``M``, as a subobject
        ``K -> M`` -- ``K`` is the points of ``M`` pairing to zero with every
        image of ``L``. Composed from the inclusion matrix and ``M``'s form,
        never from a stored ambient; total over both base rings (the rational
        kernel intersected back with the integral points over ``ZZ``)."""
        ambient = self.ambient()
        pairing = matrix(QQ, ambient.gram_matrix() * self._inclusion.matrix())  # M_rank x L_rank; columns = b(., f(e_i))
        rational_kernel = pairing.transpose().right_kernel()
        if ambient.base_ring() is QQ:
            kernel_rows = rational_kernel.basis_matrix()
        else:
            kernel_rows = (ZZ ** ambient.rank()).intersection(rational_kernel).basis_matrix()
        return cast(Subobject, ambient._subobject_from_rows(kernel_rows, label))

    def saturation(self, label: str = "saturation") -> Subobject:
        r"""The primitive closure of ``L`` in ``M`` (its saturation), as a
        subobject ``K -> M`` with ``L <= K`` and torsion-free cokernel."""
        ambient = self.ambient()
        rational_span = (QQ ** ambient.rank()).span(self._inclusion.matrix().transpose().rows(), QQ)
        saturated_rows = (ZZ ** ambient.rank()).intersection(rational_span).basis_matrix()
        return cast(Subobject, ambient._subobject_from_rows(saturated_rows, label))

    def saturation_factorization(self) -> lexicon.LatticeMorphism:
        r"""The mono factorization ``L -> L^sat`` of the carried inclusion
        through its saturation -- morphism-sited (#100 ratified placement):
        the coordinate solve lives on the inclusion itself."""
        return cast(lexicon.LatticeMorphism, self._inclusion.saturation_factorization())

    def index_in_saturation(self) -> Any:
        r"""The index ``[L^sat : L]`` -- the cokernel cardinality of the
        saturation factorization; ``1`` exactly when the subobject is
        primitive."""
        return self.saturation_factorization().index()


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


class LatticeHomset(lexicon.LatticeHomset, Homset):
    r"""Homset of form-preserving synthetic lattice morphisms."""

    # Sage's parent convention: the homset's element class (assigned after
    # LatticeMorphism is defined below).
    Element: ClassVar[type]

    def __init__(
        self,
        domain: Lattice | SyntheticLattice,
        codomain: Lattice | SyntheticLattice,
        category: lexicon.SageCategory | None = None,
    ) -> None:
        assert isinstance(domain, SyntheticLattice), f"expected SyntheticLattice domain; found={type(domain)}"
        assert isinstance(codomain, SyntheticLattice), f"expected SyntheticLattice codomain; found={type(codomain)}"
        from ..objects.categories import Lattices

        hom_category = Lattices(domain.base_ring()) if category is None else category
        assert domain.base_ring() == codomain.base_ring(), f"a lattice homset has one scalar ring; domain={domain.base_ring()}, codomain={codomain.base_ring()}"
        assert hom_category.is_subcategory(Lattices(domain.base_ring())), f"lattice homset category must refine Lattices({domain.base_ring()}); category={hom_category}"
        assert domain in hom_category and codomain in hom_category, (
            f"lattice homset arguments must belong to {hom_category}; domain={domain.category()}, codomain={codomain.category()}"
        )
        Homset.__init__(self, domain, codomain, category=hom_category)

    def _repr_(self) -> str:
        return f"Synthetic lattice homset from {self.domain()} to {self.codomain()}"

    def domain(self) -> SyntheticLattice:
        return cast(SyntheticLattice, self._domain)

    def codomain(self) -> SyntheticLattice:
        return cast(SyntheticLattice, self._codomain)

    def _element_constructor_(self, matrix_data: Any) -> LatticeMorphism:
        return LatticeMorphism(self, matrix_data)

    # There is no from_matrix: morphisms are built by the public named
    # constructors on lattices (hom/embedding/reflection/similarity) or by
    # constructing the element class on its homset; the element constructor
    # asserts well-definedness (#70).


class LatticeMorphism(lexicon.LatticeMorphism, SageMorphism):
    r"""Form-preserving morphism of synthetic lattices."""

    if TYPE_CHECKING:
        # The parent is always a synthetic lattice homset.
        def parent(self) -> LatticeHomset: ...

    def __init__(self, parent: LatticeHomset, matrix_data: Any) -> None:
        SageMorphism.__init__(self, parent)
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

    def index(self) -> Any:
        r"""The index ``[codomain : image]`` -- the order of the cokernel."""
        return self.cokernel().cardinality()

    # -- morphism-sited geometry (ratified method placement, #100): each
    # -- operation below consumes this morphism's data, so it lives here;
    # -- object spellings are delegations through a canonical attached
    # -- morphism. ----------------------------------------------------------

    def restrict(self, subobject: Subobject) -> Any:
        r"""Precomposition with the carried inclusion:
        ``self * subobject.inclusion()`` -- restriction IS composition."""
        assert isinstance(subobject, Subobject), f"restrict consumes a subobject (the carried inclusion), not a bare lattice; found={type(subobject)}"
        return self * subobject.inclusion()

    def preserves(self, subobject: Subobject) -> bool:
        r"""Factorization query for an endomorphism: does
        ``self * subobject.inclusion()`` factor through the inclusion again --
        i.e. does every generator image land back in the subobject's span?"""
        assert isinstance(subobject, Subobject), f"preserves consumes a subobject (the carried inclusion), not a bare lattice; found={type(subobject)}"
        assert self.domain() == self.codomain(), f"preservation is an endomorphism question; domain={self.domain()}, codomain={self.codomain()}"
        restricted = self.restrict(subobject)
        inclusion_matrix = matrix(QQ, subobject.inclusion().matrix())
        span = (QQ ** self.codomain().rank()).span(inclusion_matrix.columns(), self.codomain().base_ring())
        return all(vector(QQ, column) in span for column in matrix(QQ, restricted.matrix()).columns())

    def saturation(self) -> Subobject:
        r"""The saturation of the image in the codomain -- the smallest
        primitive subobject this monomorphism factors through."""
        assert self.is_injective(), f"saturation is monomorphism vocabulary; matrix={self.matrix()}"
        return self.image().saturation()

    def saturation_factorization(self) -> Any:
        r"""The mono ``A -> A^sat`` through which this monomorphism factors:
        ``f.saturation().inclusion() * f.saturation_factorization() == f``.
        The one coordinate solve lives here, inside the morphism's
        construction; its index is ``[A^sat : A]``, ``1`` exactly when the
        morphism is a primitive embedding."""
        assert self.is_injective(), f"the saturation factorization is monomorphism vocabulary; matrix={self.matrix()}"
        saturated = self.saturation()
        factor = saturated.inclusion().matrix().solve_right(self.matrix())
        return self.domain().embedding(factor, codomain=saturated.lattice())

    def orthogonal_complement(self) -> Subobject:
        r"""The subobject of the codomain pairing to zero with the image --
        the kernel of the composed pairing (asked of the image subobject,
        which carries the inclusion)."""
        return self.image().orthogonal_complement()

    def induced_map_on_quotient(self, quotient: Any) -> Any:
        r"""The endomorphism of ``cover/relations`` induced by this morphism
        of the cover -- an action on the finite quotient (its parent left the
        lattice category).

        The morphism descends exactly when it preserves the relation
        subobject: the composite ``relation -> cover -> cover ->
        cover/relation`` is zero (``pi . phi . iota = 0``), asked through the
        quotient's carried inclusion morphism and its own projection."""
        from ..forms.discriminant_forms import SyntheticLatticeQuotient

        assert isinstance(quotient, SyntheticLatticeQuotient), f"the induced action lives on a finite lattice quotient carrying its inclusion; found={type(quotient)}"
        assert self.domain() == quotient.cover_lattice() and self.codomain() == quotient.cover_lattice(), (
            "induced quotient endomorphism requires a morphism of the quotient cover lattice"
        )
        inclusion = quotient.relation_inclusion()
        relation = inclusion.domain()
        for index in range(relation.rank()):
            descends = quotient.projection(self(inclusion(relation.gen(index)))) == quotient.zero()
            assert descends, f"morphism does not preserve the quotient relation lattice; relation generator index={index}"
        return cast(lexicon.DiscriminantAction, quotient.hom([quotient.projection(self(quotient.lift(generator))) for generator in quotient.gens()]))

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
        return other.domain().hom(self.matrix() * other.matrix(), codomain=self.codomain())

    def __pow__(self, n: int) -> Any:
        assert self.domain() == self.codomain(), f"powers need an endomorphism; domain={self.domain()}, codomain={self.codomain()}"
        n = int(n)
        if n < 0:
            return self.inverse() ** (-n)
        power = self.matrix() ** n if n > 0 else self.matrix().parent().identity_matrix()
        return self.parent()(power)

    def inverse(self) -> Any:
        assert self.is_isometry(), f"only isometries are invertible in the lattice category; matrix={self.matrix()}"
        return self.codomain().hom(self.matrix().inverse(), codomain=self.domain())

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
        assert domain.base_ring() == codomain.base_ring(), f"a lattice similarity needs one scalar ring; domain={domain.base_ring()}, codomain={codomain.base_ring()}"
        homset = domain.Hom(codomain)
        assert isinstance(homset, LatticeHomset), f"a lattice similarity must belong to a lattice homset; found={type(homset)}"
        Element.__init__(self, homset)
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


class IsometryHomset(lexicon.IsometryHomset, Parent):
    r"""``Isom(L, M)`` as a first-class parent: the (possibly empty) set of
    isometries ``L -> M``. Emptiness owns the isometry decision (the G1
    routing table); ``Lattice.is_isometric`` is this homset's emptiness
    router. When nonempty, the homset is a torsor under ``O(M)``, which
    powers iteration and cardinality exactly where that group carries a
    grounded finiteness answer."""

    def __init__(self, domain: Lattice | SyntheticLattice, codomain: Lattice | SyntheticLattice) -> None:
        assert isinstance(domain, SyntheticLattice), f"expected SyntheticLattice domain; found={type(domain)}"
        assert isinstance(codomain, SyntheticLattice), f"expected SyntheticLattice codomain; found={type(codomain)}"
        # The homset is an object of Lattices(R).Homsets() for ONE base ring R:
        # a cross-ring premise is an incoherent construction, not an empty
        # homset -- the coherent cross-ring question is asked of the base-changed
        # object (L.base_extend(R')), applying the functor explicitly.
        assert domain.base_ring() is codomain.base_ring(), (
            f"Isom(L, M) is sited in Lattices(R).Homsets() for a single base ring; "
            f"domain is over {domain.base_ring()} but codomain is over {codomain.base_ring()}; "
            f"base-change explicitly (base_extend) before asking for isometries"
        )
        self._domain = domain
        self._codomain = codomain
        from ..objects.categories import Lattices

        Parent.__init__(self, category=Lattices(domain.base_ring()).Homsets())

    def _repr_(self) -> str:
        return f"Isometries from {self.domain()} to {self.codomain()}"

    def domain(self) -> SyntheticLattice:
        return self._domain

    def codomain(self) -> SyntheticLattice:
        return self._codomain

    def is_empty(self) -> bool:
        r"""The isometry decision, over Sage's own engines (gap-ledger G1,
        Rulings round 3): the whole case analysis is the single match table
        below; mathematics Sage's stack cannot decide asserts out by name.

        Indefinite rank >= 3 is decided by genus + spinor-genus theory
        (Eichler; SPLAG Ch. 15 Theorem 14 and section 9 [CS10, Zotero
        T2WVLTDB]): when the genus carries a single improper spinor genus,
        genus equality IS the isometry decision. Sage exposes spinor-genus
        ENUMERATION (spinor_generators / representatives) but no PLACEMENT
        of a given form into its spinor genus, so a split genus asserts out
        per the round-2 ruling (assert-gated sufficient condition; full
        spinor comparison is follow-up work confined to the spike per the
        2026-07-04 directive — Dutour Sikirić INDEF_FORM_TestEquivalence
        adapter)."""
        left, right = self._domain, self._codomain
        if left.rank() != right.rank() or left.signature_pair() != right.signature_pair():
            return True
        from sage.quadratic_forms.quadratic_form import QuadraticForm

        # QuadraticForm(matrix) reads the matrix as the Hessian (2 x Gram).
        integral = left.base_ring() is ZZ and right.base_ring() is ZZ and left.is_integral() and right.is_integral()
        pos, neg = left.signature_pair()
        radical_rank = left.rank() - pos - neg
        match (radical_rank, integral, left.rank()):
            case (r, _, _) if r > 0:
                # Degenerate: rad(L) is a saturated summand pairing to zero, so
                # L ~ 0^r  (+)  L/rad(L); equal signature pairs force equal
                # radical ranks, and the nondegenerate quotients recurse.
                return left.radical_quotient().Isom(right.radical_quotient()).is_empty()
            case (_, False, _):
                # Rational lattices: the grounded relation is rational equivalence of
                # quadratic forms over QQ (the 2x Hessian scaling is applied to both).
                return not QuadraticForm(matrix(QQ, 2 * left.gram_matrix())).is_rationally_isometric(QuadraticForm(matrix(QQ, 2 * right.gram_matrix())))
            case (_, True, rank) if rank <= 1:
                # Trivial: rank 0 is unique; rank 1 has diag(a) ~ diag(b) iff
                # a == b (the units of ZZ are +-1, acting by squares).
                return left.gram_matrix() != right.gram_matrix()
            case (_, True, _) if left.is_definite():
                # Definite: Sage's global equivalence (PARI qfisom),
                # sign-normalized to positive definite.
                sign = 1 if left.is_positive_definite() else -1
                return not QuadraticForm(2 * sign * matrix(ZZ, left.gram_matrix())).is_globally_equivalent_to(QuadraticForm(2 * sign * matrix(ZZ, right.gram_matrix())))
            case (_, True, 2):
                assert False, (
                    "binary indefinite isometry is outside the spinor-genus theorem "
                    "(SPLAG Ch. 15 section 9 assumes dimension >= 3; the binary theory is "
                    "Gauss composition / real quadratic class groups — gap-ledger entry 1); "
                    f"left_gram={left.gram_matrix()}, right_gram={right.gram_matrix()}"
                )
            case (_, True, _):
                # Indefinite rank >= 3: class = improper spinor genus (Eichler,
                # SPLAG Thm 14); genus equality decides iff the genus carries a
                # single improper spinor genus (empty spinor-generator set).
                from sage.quadratic_forms.genera.genus import Genus

                genus_left = Genus(matrix(ZZ, left.gram_matrix()))
                if genus_left != Genus(matrix(ZZ, right.gram_matrix())):
                    return True
                if not genus_left.spinor_generators(proper=False):
                    return False
                assert False, (
                    "this genus splits into more than one improper spinor genus; Sage's "
                    "spinor stack enumerates spinor genera (representatives) but cannot PLACE "
                    "a given form into one, so the decision is assert-gated per the G1 round-2 "
                    "ruling (follow-up engine: Dutour Sikirić INDEF_FORM_TestEquivalence "
                    "adapter, spike-bound per the 2026-07-04 directive); "
                    f"spinor_generators={genus_left.spinor_generators(proper=False)}, "
                    f"left_gram={left.gram_matrix()}, right_gram={right.gram_matrix()}"
                )
        assert False, f"unreachable: the G1 routing table is total; gram={left.gram_matrix()}"

    def an_element(self) -> LatticeMorphism:
        r"""A distinguished isometry; defined exactly when the homset is
        nonempty. The witness comes from Sage's global-equivalence engine
        (PARI qfisom transformation) in the definite integral regime; the
        identity when domain and codomain are the same object."""
        assert not self.is_empty(), f"Isom({self._domain}, {self._codomain}) is empty; existence is the homset's emptiness question"
        if self._domain == self._codomain:
            return cast(LatticeMorphism, self._domain.identity_morphism())
        left, right = self._domain, self._codomain
        assert left.base_ring() is ZZ and left.is_integral() and right.is_integral() and left.is_definite(), (
            "an explicit isometry witness is implemented on the definite integral regime "
            "(PARI qfisom); other regimes have no witness engine in Sage's stack; "
            f"left_gram={left.gram_matrix()}, right_gram={right.gram_matrix()}"
        )
        from sage.quadratic_forms.quadratic_form import QuadraticForm

        sign = 1 if left.is_positive_definite() else -1
        transformation = QuadraticForm(2 * sign * matrix(ZZ, right.gram_matrix())).is_globally_equivalent_to(
            QuadraticForm(2 * sign * matrix(ZZ, left.gram_matrix())), return_matrix=True
        )
        # The morphism constructor asserts form-preservation, so a convention
        # mismatch in the engine's transformation fails loudly here.
        return cast(LatticeMorphism, left.hom(matrix(ZZ, transformation), codomain=right))

    def cardinality(self) -> Any:
        r"""``0`` when empty; ``|O(M)|`` otherwise (the nonempty homset is an
        ``O(M)``-torsor). Computed exactly where ``O(M)`` carries a grounded
        finiteness answer — the ``Groups().Finite()`` category refinement
        stamped on the group at construction; elsewhere no computation
        grounds any answer (finite or infinite) yet, and the assertion below
        says so under this contract's own name."""
        if self.is_empty():
            return ZZ(0)
        from sage.categories.groups import Groups

        group = self._codomain.isometry_group()
        assert group in Groups().Finite(), (
            f"Isom({self._domain.label()}, {self._codomain.label()}).cardinality() is "
            "|O(M)| (the nonempty homset is an O(M)-torsor), computed exactly where "
            f"O(M) carries a grounded finiteness answer; O({self._codomain.label()}) "
            "carries none — extend the group engine, do not special-case; "
            f"codomain_gram={self._codomain.gram_matrix()}"
        )
        return group.order()

    def __iter__(self) -> Any:
        r"""Torsor enumeration: ``{g . f0 : g in O(M)}``; implemented exactly
        where ``O(M)`` is finite."""
        if self.is_empty():
            return
        base = self.an_element()
        for isometry in self._codomain.isometry_group():
            yield isometry * base

    def __contains__(self, candidate: Any) -> bool:
        return isinstance(candidate, LatticeMorphism) and candidate.domain() == self._domain and candidate.codomain() == self._codomain and candidate.is_isometry()


class EmbeddingHomset(lexicon.EmbeddingHomset, Parent):
    r"""``Emb(L, M)`` as a first-class parent: the form-preserving
    monomorphisms ``L -> M``. Enumeration is by generator patterns where the
    codomain is INTEGRAL definite (each generator has finitely many candidate
    images, the vectors of its square, delivered by the ZZ short-vector
    engine); emptiness and the distinguished element ride on the enumeration.
    Other regimes assert out by name at this homset's own boundary:
    non-integral definite codomains have no enumeration engine, and
    indefinite existence is issue #24's Nikulin engine."""

    def __init__(self, domain: Lattice | SyntheticLattice, codomain: Lattice | SyntheticLattice) -> None:
        assert isinstance(domain, SyntheticLattice), f"expected SyntheticLattice domain; found={type(domain)}"
        assert isinstance(codomain, SyntheticLattice), f"expected SyntheticLattice codomain; found={type(codomain)}"
        self._domain = domain
        self._codomain = codomain
        from ..objects.categories import Lattices

        Parent.__init__(self, category=Lattices(domain.base_ring()).Homsets())

    def _repr_(self) -> str:
        return f"Embeddings of {self.domain()} into {self.codomain()}"

    def domain(self) -> SyntheticLattice:
        return self._domain

    def codomain(self) -> SyntheticLattice:
        return self._codomain

    def __iter__(self) -> Any:
        r"""Depth-first assignment of generator images: candidate images of
        the ``i``-th generator are the codomain vectors of its square, pruned
        by the pairing constraints against the already-placed generators.
        Finite and total for an integral definite codomain (the supported
        regime, asserted by name below)."""
        domain, codomain = self._domain, self._codomain
        from ..objects.parents import (
            SyntheticIntegralNegativeDefiniteLattice,
            SyntheticIntegralPositiveDefiniteLattice,
        )

        integral_definite_leaves = (
            SyntheticIntegralNegativeDefiniteLattice,
            SyntheticIntegralPositiveDefiniteLattice,
        )
        assert isinstance(codomain, integral_definite_leaves) and codomain.rank() > 0, (
            "embedding enumeration is implemented for INTEGRAL definite codomains: "
            "finiteness/totality of the generator-pattern engine is proven only for the "
            "ZZ short-vector enumeration; non-integral definite codomains are outside the "
            "engine, and indefinite existence is issue #24's Nikulin engine; "
            f"codomain_gram={codomain.gram_matrix()}"
        )
        gram = domain.gram_matrix()
        wrong_sign = 1 if codomain.is_negative_definite() else -1
        if any(wrong_sign * gram[i, i] > 0 for i in range(domain.rank())):
            return  # a definite form takes values of one sign only: Emb is empty
        if any(gram[i, i] not in ZZ for i in range(domain.rank())):
            return  # an integral form represents only integers: Emb is empty
        candidate_pools = [codomain.vectors_of_square(gram[i, i]) for i in range(domain.rank())]

        def assign(placed: list[Any]) -> Any:
            position = len(placed)
            if position == domain.rank():
                columns = column_matrix(ZZ, [image.coefficient_vector() for image in placed])
                if columns.rank() == domain.rank():
                    yield domain.embedding(columns, codomain=codomain)
                return
            for candidate in candidate_pools[position]:
                if all(placed[j].b(candidate) == gram[j, position] for j in range(position)):
                    yield from assign([*placed, candidate])

        yield from assign([])

    def is_empty(self) -> bool:
        for _ in self:
            return False
        return True

    def an_element(self) -> LatticeMorphism:
        for embedding in self:
            return cast(LatticeMorphism, embedding)
        assert False, f"Emb({self._domain}, {self._codomain}) is empty; existence is the homset's emptiness question"

    def __contains__(self, candidate: Any) -> bool:
        return isinstance(candidate, LatticeMorphism) and candidate.domain() == self._domain and candidate.codomain() == self._codomain and candidate.is_injective()
