r"""Synthetic lattice parents.

A synthetic lattice is a *based* free module over ``R in {ZZ, QQ}`` together with
a symmetric Gram matrix ``G`` in its own intrinsic basis.  Its identity is the
pair ``(base_ring, G)`` -- there is no ambient vector space, no "coordinate
frame", no ``basis_matrix``.  Elements are coefficient columns in ``R^rank`` and
``b(v, w) = v^T G w``.

A *subobject* relationship (sublattice, span, saturation, ...) is an injective
hom ``A`` into a parent lattice ``L0``: the child is ``(R, A^T G0 A)`` and ``A``
records the child's basis in ``L0``'s intrinsic coordinates.  That inclusion is
carried on the child (``_ambient`` = the parent, ``_inclusion`` = ``A``) so the
subobject algebra (intersection, index, orthogonal complement, ...) can compute
in the parent's own coefficient module.  It is *not* part of the child's
identity: equality is by ``(base_ring, G)`` alone.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator, Sequence
from typing import TYPE_CHECKING, Any, ClassVar

if TYPE_CHECKING:
    from ..lexicon.geometry import Polyhedron

from sage.arith.functions import lcm
from sage.matrix.constructor import identity_matrix, matrix
from sage.matrix.special import block_diagonal_matrix
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.category_object import normalize_names
from sage.structure.element import Matrix
from sage.structure.parent import Parent

from ..algebra.arithmetic import as_square_qq_matrix, signature_pair
from ..lexicon import (
    BaseRing,
    CartanType,
    DefiniteLattice,
    DiscriminantFormElement,
    DiscriminantSubgroup,
    EmbeddingHomset,
    ExactScalar,
    FiniteAbelianGroup,
    FreeModule,
    Genus,
    GramMatrix,
    Integer,
    IntegralNondegenerateLattice,
    IsometryGroup,
    IsometryHomset,
    Lattice,
    LatticeElement,
    LatticeHomset,
    LatticeMorphism,
    LatticeSimilarity,
    NondegenerateLattice,
    PositiveDefiniteLattice,
    RawGramMatrix,
    RawMorphismMatrix,
    RawVectors,
    RootGeneratedLattice,
    SageInfinity,
    SignaturePair,
    SourcedDiscriminantForm,
    SymbolicExpression,
    Vector,
)
from .categories import Lattices
from .elements import SyntheticLatticeElement

type EnumerationKwargValue = bool | ExactScalar | float | int | str


def category_for(base_ring: BaseRing, gram: Matrix) -> Lattices:
    category = Lattices(base_ring)
    if gram.det() != 0:
        category = category.Nondegenerate()
    if base_ring is ZZ and all(entry in ZZ for entry in gram.list()):
        category = category.Integral()
        if all(entry % 2 == 0 for entry in gram.diagonal()):
            category = category.Even()
        if gram.det() in (ZZ.one(), -1):
            category = category.Unimodular()
    pos, neg = signature_pair(gram)
    if pos == gram.nrows():
        category = category.Definite().PositiveDefinite()
    elif neg == gram.nrows():
        category = category.Definite().NegativeDefinite()
    elif pos and neg:
        category = category.Indefinite()
        # Hyperbolic: signature (1, rank-1), rank >= 2 (section 1.3). Such a form
        # is nondegenerate (pos + neg == rank), so Nondegenerate is already set.
        if pos == 1 and neg == gram.nrows() - 1 and gram.nrows() >= 2:
            category = category.Hyperbolic()
    return category


if TYPE_CHECKING:
    from ..morphisms.homsets import Subobject

    # Binds the stub's element-type parameter (typings/sage/structure/parent.pyi):
    # Parent.__call__ then returns SyntheticLatticeElement everywhere. Runtime
    # Sage's Parent is a cython extension type and cannot be subscripted.
    SyntheticElementParent = Parent[SyntheticLatticeElement]
else:
    SyntheticElementParent = Parent


class SyntheticLattice(Lattice, SyntheticElementParent):
    r"""Synthetic based lattice ``(base_ring, G)`` with owned elements and homsets."""

    Element = SyntheticLatticeElement

    if TYPE_CHECKING:
        # Sage's category framework injects element_class at construction;
        # for this tower it is the class assigned to Element above.
        element_class: ClassVar[type[SyntheticLatticeElement]]

    def __init__(
        self,
        gram_matrix: RawGramMatrix,
        base_ring: BaseRing,
        label: str,
        cartan_type: CartanType | str | None = None,
        names: Sequence[str] | str | None = None,
    ) -> None:
        # A lattice IS the pair (base_ring, Gram) -- nothing else. It never
        # stores an ambient; a subobject is a lattice together with its
        # inclusion morphism (the Subobject value), not a lattice that remembers
        # a parent. The one Gram codec asserts square + symmetric and
        # immutabilizes; construction is the only producer.
        gram = as_square_qq_matrix(gram_matrix)
        assert base_ring in (ZZ, QQ), f"lattice base ring must be ZZ or QQ; found={base_ring}"
        self._gram_matrix = gram
        self._label = label
        self._base_ring = base_ring
        self._cartan_type = cartan_type
        self._isometry_group_object: IsometryGroup | None = None
        category = category_for(base_ring, gram)
        if cartan_type is not None:
            # provenance axiom: attached only by the section-6 constructors
            # (and direct sums thereof), never detected from the Gram
            category = category.RootGenerated()
        # Generator symbols: Sage's own naming protocol (normalize_names +
        # CategoryObject storage), so `L.<e,f> = ...` preparser binding and
        # variable_names()/inject_variables() work exactly as for polynomial
        # rings. Default symbols are the indexed e_0, ..., e_{n-1}.
        if names is None:
            names = tuple(f"e_{i}" for i in range(gram.nrows()))
        Parent.__init__(self, base=base_ring, category=category, names=normalize_names(gram.nrows(), names))

    def _repr_(self) -> str:
        pos, neg = self.signature_pair()
        summary = f"Synthetic lattice {self._label}: rank {self.rank()}, sig ({pos}, {neg}), det {self.determinant()}"
        if self.base_ring() is ZZ and self.is_integral() and self.is_nondegenerate():
            parity = "even" if self.is_even() else "odd"
            divisors = tuple(d for d in self.gram_matrix().change_ring(ZZ).elementary_divisors() if d != 1)
            structure = "unimodular" if self.is_unimodular() else f"disc {divisors}"
            return f"{summary}, {parity}, {structure}"
        return summary

    def _element_constructor_(self, coordinates: Sequence[ExactScalar] | SyntheticLatticeElement) -> SyntheticLatticeElement:
        return self.element_class(self, coordinates)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, SyntheticLattice) and self.base_ring() == other.base_ring() and self.gram_matrix() == other.gram_matrix()

    def __hash__(self) -> int:
        return hash((self.base_ring(), self.gram_matrix()))

    # -- the one private presentation crossing ------------------------------------
    #
    # A lattice is (R, G) on its own standard basis. The single sanctioned
    # crossing from row data in THIS lattice's coordinates to a new plain
    # lattice lives here; everything relating the new lattice back to this one
    # is a morphism (a ``Subobject``), never stored coordinate state.
    def _from_rows(self, basis_rows: Matrix, base_ring: BaseRing, label: str) -> SyntheticLattice:
        r"""The plain sublattice presented by ``basis_rows`` (rows in this
        lattice's coordinates): Gram ``= B G B^T``. The result stores nothing
        relating it to ``self``; that relationship is an inclusion morphism."""
        rows = matrix(QQ, basis_rows)
        assert rows.ncols() == self.rank(), f"basis rows must be given in this lattice's coordinates; rank={self.rank()}, rows={rows}"
        return synthetic_lattice(rows * self.gram_matrix() * rows.transpose(), base_ring, label)

    # -- Port: intrinsic invariants read straight off (base_ring, G) --------------

    def rank(self) -> int:
        return int(self._gram_matrix.nrows())

    def base_ring(self) -> BaseRing:
        return self._base_ring

    def ngens(self) -> int:
        return self.rank()

    def is_hyperbolic(self) -> bool:
        pos, neg = self.signature_pair()
        return pos == 1 and neg == self.rank() - 1 and self.rank() >= 2

    def random_element(self) -> SyntheticLatticeElement:
        return self([self.base_ring().random_element() for _ in range(self.rank())])

    def _reflection_image_matrix(self, element: SyntheticLatticeElement) -> Matrix:
        r"""The rational matrix of ``sigma_v(x) = x - (2 b(x,v)/q(v)) v`` in the
        basis. Integral over ``base_ring`` exactly when ``v`` is a root, so this
        is the single source shared by ``reflection`` and ``is_root``."""
        norm = self.q(element)
        assert norm != 0, f"reflection requires an anisotropic vector; q(v)=0 for v={element}"
        v_column = matrix(QQ, self.rank(), 1, list(element.coefficient_vector()))
        gram_v = self.gram_matrix() * v_column
        return identity_matrix(QQ, self.rank()) - (2 / norm) * v_column * gram_v.transpose()

    def reflection(self, v: LatticeElement) -> LatticeMorphism:
        r"""The reflection ``sigma_v(x) = x - (2 b(x,v)/q(v)) v`` in ``End(L)``."""
        element = v if isinstance(v, SyntheticLatticeElement) and v.parent() is self else self(v)
        images = self._reflection_image_matrix(element)
        for j in range(self.rank()):
            assert all(images[i, j] in self.base_ring() for i in range(self.rank())), (
                f"reflection does not map the lattice into itself over {self.base_ring()}; failing basis vector index={j}, image column={images.column(j)}, v={element}"
            )
        return self.hom(images.change_ring(self.base_ring()))

    def is_root(self, v: LatticeElement) -> bool:
        r"""``v`` is a root iff its reflection ``sigma_v`` is integral, i.e. lies
        in ``O(L)``. This is the reflective definition; the norm-``\pm 2``
        vectors are the special case, while the AG lattices of interest also
        admit e.g. square-``(-4)`` roots of divisor 2 (Nikulin)."""
        element = v if isinstance(v, SyntheticLatticeElement) and v.parent() is self else self(v)
        if self.q(element) == 0:
            return False
        return all(entry in self.base_ring() for entry in self._reflection_image_matrix(element).list())

    def label(self) -> str:
        r"""The construction label (display surface for reprs across the
        package -- the public spelling of the stored label)."""
        return self._label

    def identity_morphism(self) -> LatticeMorphism:
        r"""The identity isometry ``L -> L``."""
        return self.hom(identity_matrix(self.base_ring(), self.rank()))

    def gram_matrix(self) -> GramMatrix:
        return self._gram_matrix

    def bilinear_form(self) -> Callable[[LatticeElement, LatticeElement], ExactScalar]:
        return self.b

    def quadratic_form(self) -> Callable[[LatticeElement], ExactScalar]:
        return self.q

    def basis(self) -> tuple[SyntheticLatticeElement, ...]:
        return tuple(self.gen(i) for i in range(self.rank()))

    def gens(self) -> tuple[SyntheticLatticeElement, ...]:
        return self.basis()

    def gen(self, i: int) -> SyntheticLatticeElement:
        module: FreeModule = self.base_ring() ** self.rank()
        return self(module.gen(i))

    def zero(self) -> SyntheticLatticeElement:
        return self([self.base_ring().zero()] * self.rank())

    def b(self, left: LatticeElement, right: LatticeElement) -> ExactScalar:
        left = self(left) if left.parent() is not self else left
        right = self(right) if right.parent() is not self else right
        return vector(QQ, left.coefficient_vector()) * self.gram_matrix() * vector(QQ, right.coefficient_vector())

    def q(self, element: LatticeElement) -> ExactScalar:
        element = self(element) if element.parent() is not self else element
        return self.b(element, element)

    def rationalization(self) -> SyntheticLattice:
        return synthetic_lattice(
            self.gram_matrix(),
            QQ,
            f"{self._label}_QQ",
        )

    def base_extend(self, base_ring: BaseRing) -> SyntheticLattice:
        assert base_ring in (ZZ, QQ), f"lattice base ring must be ZZ or QQ; found={base_ring}"
        return synthetic_lattice(
            self.gram_matrix(),
            base_ring,
            f"{self._label}_over_{base_ring}",
        )

    def determinant(self) -> ExactScalar:
        return self.gram_matrix().determinant()

    def discriminant(self) -> ExactScalar:
        # (-1)^(r/2) det(G), written by parity so the arithmetic stays exact.
        rank_half = self.rank() // 2
        return self.determinant() if rank_half % 2 == 0 else -self.determinant()

    def absolute_discriminant(self) -> ExactScalar:
        return self.determinant().abs()

    def signature_pair(self) -> SignaturePair:
        return signature_pair(self.gram_matrix())

    def signature(self) -> SignaturePair:
        r"""The signature ``(p, q)`` -- positive index ``p``, negative index
        ``q``. The classical integer ``p - q`` (Milgram/Sylvester) is derived
        from this, not the name of the method (#9)."""
        return self.signature_pair()

    def is_integral(self) -> bool:
        return all(entry in ZZ for entry in self.gram_matrix().list())

    def is_even(self) -> bool:
        return self.is_integral() and all(entry % 2 == 0 for entry in self.gram_matrix().diagonal())

    def is_unimodular(self) -> bool:
        return self.base_ring() is ZZ and self.is_integral() and self.determinant() in (1, -1)

    def is_degenerate(self) -> bool:
        return self.determinant() == 0

    def is_nondegenerate(self) -> bool:
        return self.gram_matrix().rank() == self.rank()

    def is_positive_definite(self) -> bool:
        pos, neg = self.signature_pair()
        return neg == 0 and pos == self.rank()

    def is_negative_definite(self) -> bool:
        pos, neg = self.signature_pair()
        return pos == 0 and neg == self.rank()

    def is_definite(self) -> bool:
        return self.is_positive_definite() or self.is_negative_definite()

    def is_indefinite(self) -> bool:
        pos, neg = self.signature_pair()
        return pos > 0 and neg > 0

    def radical(self) -> Subobject:
        r"""``rad(L)`` as a subobject: the orthogonal complement of the
        identity morphism -- the kernel of the composed pairing, total on
        every lattice (equal to ``ker(L -> L^dual)`` where the dual exists;
        #100 ratified placement: the object spelling delegates through the
        canonical attached morphism)."""
        return self.identity_morphism().orthogonal_complement()

    def radical_quotient(self, label: str = "radical_quotient") -> SyntheticNondegenerateLattice:
        r"""``L / rad(L)``, a nondegenerate based lattice (functor stays in
        Lattices) -- the coimage of the radical's presentation: derived from
        the carried inclusion of ``radical()``, never from a re-derived
        coordinate kernel (#100 ratified placement)."""
        radical_inclusion = self.radical().inclusion()
        radical_rank = radical_inclusion.domain().rank()
        if radical_rank == 0:
            assert isinstance(self, SyntheticNondegenerateLattice), (
                f"a lattice with trivial radical must have been routed into the nondegenerate subcategory; found={type(self)}"
            )
            return self
        rank = self.rank()
        gram = self.gram_matrix()
        if radical_rank == rank:
            # Fully degenerate: rad(L) = L, so L/rad(L) is the rank-0 lattice.
            zero_quotient = synthetic_lattice(matrix(QQ, 0, 0), self.base_ring(), label)
            assert isinstance(zero_quotient, SyntheticNondegenerateLattice), f"the rank-0 lattice is (vacuously) nondegenerate; dispatch returned {type(zero_quotient)}"
            return zero_quotient
        radical_columns = matrix(QQ, radical_inclusion.matrix()).columns()
        if self.base_ring() is QQ:
            complement = (QQ**rank).span(radical_columns).complement().basis_matrix()
        else:
            module = ZZ**rank
            radical_module = module.submodule([vector(ZZ, column) for column in radical_columns])
            quotient = module.quotient(radical_module)
            complement = matrix(ZZ, [gen.lift() for gen in quotient.gens()])
        quotient_gram = complement * gram * complement.transpose()
        quotient_lattice = synthetic_lattice(quotient_gram, self.base_ring(), label)
        assert isinstance(quotient_lattice, SyntheticNondegenerateLattice), f"radical quotient must be nondegenerate; gram={quotient_lattice.gram_matrix()}"
        return quotient_lattice

    # -- Subobject algebra: operations between sublattices of a common parent -----

    def sublattice(
        self,
        generators: RawVectors,
        label: str = "sublattice",
        require_subset: bool = True,
        require_integral: bool = True,
    ) -> SyntheticLattice:
        generator_matrix = matrix(QQ, generators)
        assert generator_matrix.ncols() == self.rank(), f"sublattice generators must be rows in the parent basis; parent_rank={self.rank()}, generators={generator_matrix}"
        if require_subset:
            parent_module = self.base_ring() ** self.rank()
            for row in generator_matrix.rows():
                assert row in parent_module, f"sublattice generators must lie in the parent lattice; generator={row}, parent={self}; fix the caller's generators"
        if generator_matrix.rank() == generator_matrix.nrows():
            basis_matrix = generator_matrix
        else:
            generator_module = (QQ ** self.rank()).span(generator_matrix.rows(), self.base_ring())
            basis_matrix = matrix(QQ, generator_module.basis_matrix())
        lattice = self._from_rows(basis_matrix, self.base_ring(), label)
        assert not require_integral or lattice.is_integral(), f"sublattice is not integral; gram={lattice.gram_matrix()}"
        return lattice

    def subobject(self, elements: Sequence[LatticeElement], label: str = "subobject") -> Subobject:
        r"""The subobject generated by the given elements of this lattice: the
        sublattice they span together with its inclusion morphism, as a
        ``Subobject`` (lattice + monomorphism). Sublattices are formed from
        spans of elements, kernels, and images -- the generators must be
        elements of this lattice, never raw coordinate lists."""
        rows = []
        for element in elements:
            assert isinstance(element, SyntheticLatticeElement) and element.parent() is self, (
                f"subobject generators must be elements of this lattice (span them, or take a kernel/image); raw coordinates are not accepted. Got {element!r}"
            )
            rows.append(list(element.coefficient_vector()))
        generator_matrix = matrix(QQ, rows) if rows else matrix(QQ, 0, self.rank())
        # Independent generators ARE the basis (preserve the presentation); a
        # dependent family reduces to the span's basis.
        if generator_matrix.nrows() > 0 and generator_matrix.rank() == generator_matrix.nrows():
            span_basis = generator_matrix
        else:
            span_basis = (self.base_ring() ** self.rank()).span(generator_matrix.rows()).basis_matrix()
        return self._subobject_from_rows(span_basis, label)

    def _subobject_from_rows(self, rows: Matrix, label: str) -> Subobject:
        r"""A ``Subobject`` of this lattice from basis rows given in this
        lattice's coordinates: the plain sublattice ``(R, G_L)`` plus its
        inclusion morphism. The sublattice stores nothing relating it to
        ``self``; the embedding is the morphism."""
        from ..morphisms.homsets import Subobject

        rows = matrix(QQ, rows)
        assert rows.ncols() == self.rank(), f"subobject basis rows must be in this lattice's coordinates; rank={self.rank()}, rows={rows}"
        gram = rows * self.gram_matrix() * rows.transpose()
        sublattice = synthetic_lattice(gram, self.base_ring(), label)
        return Subobject(sublattice.embedding(rows.transpose(), codomain=self))

    def lattice_in_rationalization(
        self,
        generators: RawVectors,
        label: str = "lattice_in_rationalization",
    ) -> SyntheticLattice:
        r"""The ZZ-lattice in ``L_QQ = L (x) QQ`` spanned by the given rational
        generators (commensurable with ``L`` when full-rank). Rational generators
        span no ZZ-submodule of ``L`` itself; the object lives in the rational
        quadratic space, so the ambient is always ``L_QQ`` (Nik80 section 1)."""
        return self.sublattice(generators, label=label, require_subset=False, require_integral=False)

    def span(
        self,
        generators: RawVectors,
        base_ring: BaseRing | None = None,
        check_integral: bool | None = None,
        check_even: bool | None = None,
        label: str = "span",
    ) -> SyntheticLattice:
        base_ring = self.base_ring() if base_ring is None else base_ring
        assert base_ring in (ZZ, QQ), f"lattice span base ring must be ZZ or QQ; found={base_ring}"
        generator_matrix = matrix(QQ, generators)
        assert generator_matrix.ncols() == self.rank(), f"span generators must be rows in the parent's coordinates; parent_rank={self.rank()}, generators={generator_matrix}"
        module = (QQ ** self.rank()).span(generator_matrix.rows(), base_ring)
        lattice = self._from_rows(matrix(QQ, module.basis_matrix()), module.base_ring(), label)
        assert check_integral is not True or lattice.is_integral(), f"span is not integral; gram={lattice.gram_matrix()}"
        assert check_even is not True or lattice.is_even(), f"span is not even; gram={lattice.gram_matrix()}"
        return lattice

    def span_of_basis(
        self,
        basis: RawVectors,
        base_ring: BaseRing | None = None,
        label: str = "span",
    ) -> SyntheticLattice:
        base_ring = self.base_ring() if base_ring is None else base_ring
        basis_matrix = matrix(QQ, basis)
        assert basis_matrix.rank() == basis_matrix.nrows(), f"basis rows must be independent; basis={basis_matrix}"
        return self._from_rows(basis_matrix, base_ring, label)

    def zero_lattice(self, label: str = "zero_lattice") -> SyntheticLattice:
        return self._from_rows(matrix(QQ, 0, self.rank()), self.base_ring(), label)

    def overlattice(
        self,
        generators: RawVectors,
        check_integral: bool = False,
        label: str = "overlattice",
    ) -> LatticeMorphism:
        r"""The overlattice ``M >= L`` spanned by this lattice and the given
        rational generators (rows in this lattice's coordinates), returned as
        the inclusion morphism ``L -> M``. The constructor is the once-only
        place the presentation crosses the boundary, so it is the only place
        the witness can be minted; callers wanting the object alone take
        ``.codomain()``, and index questions belong to the morphism
        (``.index()`` = cokernel cardinality)."""
        generator_matrix = matrix(QQ, generators)
        assert generator_matrix.ncols() == self.rank(), (
            f"overlattice generators must be rows in the parent's coordinates; parent_rank={self.rank()}, generators={generator_matrix}"
        )
        combined = identity_matrix(QQ, self.rank()).stack(generator_matrix)
        module = (QQ ** self.rank()).span(combined.rows(), self.base_ring())
        basis_rows = matrix(QQ, module.basis_matrix())
        assert basis_rows.nrows() == self.rank(), f"an overlattice spans the same rational space; rank={self.rank()}, basis={basis_rows}"
        gram = basis_rows * self.gram_matrix() * basis_rows.transpose()
        overlattice = synthetic_lattice(gram, self.base_ring(), label)
        assert not check_integral or overlattice.is_integral(), f"overlattice is not integral; gram={overlattice.gram_matrix()}"
        return self.embedding(basis_rows.inverse().transpose(), codomain=overlattice)

    # sum / intersection / saturation / primitive_closure are NOT defined on a
    # bare lattice: they relate a subobject to the codomain of its inclusion,
    # so they live on ``Subobject`` (saturation, saturation_factorization) and
    # on the subobject algebra the child architecture plan sites there. The
    # witness-compensating object spellings (``in_ambient=``/``ambient=``
    # parameters) were degenerate after the substrate deletion -- saturation
    # was a no-op and sum/intersection ignored their argument -- and are
    # rejected per the P6 siting gate (#100).

    def denominator(self) -> ExactScalar:
        return lcm([entry.denominator() for entry in self.gram_matrix().list()] or [ZZ.one()])

    def clear_denominators(self, label: str = "clear_denominators") -> SyntheticLattice:
        return self.scale(self.denominator(), label=label)

    def finite_quotient(self, relation: Lattice | Subobject) -> FiniteAbelianGroup:
        r"""The finite quotient ``self / relation``. ``relation`` is a subobject
        of this lattice (carrying its inclusion), or -- for the metric dual
        ``L#/L`` -- the plain relation lattice."""
        from ..forms.discriminant_forms import SyntheticLatticeQuotient
        from ..morphisms.homsets import Subobject

        if isinstance(relation, Subobject):
            assert relation.ambient() == self, f"the relation subobject must live in this lattice; ambient={relation.ambient()}, self={self}"
            inclusion = matrix(ZZ, relation.inclusion().matrix().transpose())
            return SyntheticLatticeQuotient(self, relation.lattice(), inclusion)
        return SyntheticLatticeQuotient(self, relation)

    def quotient_map_to(self, sublattice: Lattice) -> Callable[[LatticeElement], DiscriminantFormElement]:
        r"""The canonical projection ``L -> L/M`` — an abelian-group
        homomorphism out of the lattice category (typed as a map; the
        ``AbelianGroupMorphism`` noun is catalogued deferred vocabulary)."""
        from ..forms.discriminant_forms import SyntheticLatticeQuotient

        quotient = self.finite_quotient(sublattice)
        assert isinstance(quotient, SyntheticLatticeQuotient), f"finite_quotient must produce a lattice quotient; found={type(quotient)}"
        return quotient.projection

    def cover_lattice(self) -> SyntheticLattice:
        return self

    def relation_lattice(self) -> SyntheticLattice:
        return self

    def orthogonal_complement(self, subobject: Subobject, label: str = "orthogonal_complement") -> Subobject:
        r"""The orthogonal complement of a subobject inside this lattice, as a
        subobject. Delegates to the subobject, which composes its inclusion with
        this lattice's form -- no stored ambient."""
        from ..morphisms.homsets import Subobject as _Subobject

        assert isinstance(subobject, _Subobject), "orthogonal_complement takes a subobject (M.subobject(...)/an image/kernel), not a bare lattice"
        assert subobject.ambient() == self, f"the subobject must live in this lattice; ambient={subobject.ambient()}, self={self}"
        return subobject.orthogonal_complement(label=label)

    def direct_sum(self, *others: Lattice, label: str = "direct_sum") -> SyntheticLattice:
        r"""The orthogonal direct sum. Associative and variadic:
        ``U.direct_sum(V, W)``, ``U + V + W``, and ``sum([U, V, W])`` all agree."""
        assert others, "direct_sum needs at least one other summand; fix the caller"
        result: SyntheticLattice = self
        for other in others:
            result = result._direct_sum_pair(other, label)
        return result

    def _direct_sum_pair(self, other: Lattice, label: str) -> SyntheticLattice:
        base_ring = QQ if QQ in (self.base_ring(), other.base_ring()) else ZZ
        cartan_type: str | None = None
        if isinstance(self, _RootGeneratedProvenance) and isinstance(other, _RootGeneratedProvenance):
            # direct sums of root-generated lattices keep the provenance axiom;
            # the composite has no single Cartan type (irreducible_root_components
            # is the composite vocabulary)
            cartan_type = "composite"
        return synthetic_lattice(
            block_diagonal_matrix(self.gram_matrix(), other.gram_matrix()),
            base_ring,
            label,
            cartan_type=cartan_type,
        )

    def __add__(self, other: Lattice) -> SyntheticLattice:
        return self.direct_sum(other)

    def __radd__(self, other: object) -> SyntheticLattice:
        # enables sum([U, V, W]), whose implicit start value is the integer 0
        assert other == 0, f"a lattice sums only with lattices or the sum() identity 0; got {other!r}"
        return self

    def direct_sum_with_embeddings(self, other: SyntheticLattice, label: str = "direct_sum") -> tuple[SyntheticLattice, LatticeMorphism, LatticeMorphism]:
        r"""The direct sum together with its two summand embedding morphisms
        (gap-ledger row 9a; parity with Sage's
        ``IntegralLatticeDirectSum(return_embeddings=True)``): returns
        ``(S, left, right)`` with ``left: self -> S`` and ``right: other -> S``
        the primitive orthogonal-summand embeddings."""
        total = self.direct_sum(other, label=label)
        left_matrix = identity_matrix(ZZ, self.rank()).stack(matrix(ZZ, other.rank(), self.rank()))
        right_matrix = matrix(ZZ, self.rank(), other.rank()).stack(identity_matrix(ZZ, other.rank()))
        left = self.embedding(left_matrix, codomain=total)
        right = other.embedding(right_matrix, codomain=total)
        assert left.is_primitive_embedding()
        assert right.is_primitive_embedding()
        return total, left, right

    def tensor_product(self, other: Lattice, label: str = "tensor_product") -> SyntheticLattice:
        base_ring = QQ if QQ in (self.base_ring(), other.base_ring()) else ZZ
        return synthetic_lattice(
            self.gram_matrix().tensor_product(other.gram_matrix()),
            base_ring,
            label,
        )

    def is_primitive(self, subobject: Subobject) -> bool:
        r"""Whether a subobject is primitive in this lattice -- by DEFINITION,
        whether the cokernel of its inclusion is torsion-free. (That this equals
        being saturated is a theorem, not the definition, and saturation carries
        no computability contract over general rings.)"""
        from ..morphisms.homsets import Subobject as _Subobject

        assert isinstance(subobject, _Subobject), "is_primitive takes a subobject (M.subobject(...)/an image/kernel), not a bare lattice"
        assert subobject.ambient() == self, f"the subobject must live in this lattice; ambient={subobject.ambient()}, self={self}"
        return subobject.is_primitive()

    def isometry_group(self) -> IsometryGroup:
        r"""O(L), the isometry group object — total for EVERY lattice (spec
        section 3); unique per lattice. Generators/order are the object's own
        contracts, implemented exactly where it is finite."""
        if self._isometry_group_object is None:
            from ..morphisms.isometry_groups import SyntheticIsometryGroup

            self._isometry_group_object = SyntheticIsometryGroup(self)
        return self._isometry_group_object

    def is_isometric(self, other: Lattice) -> bool:
        r"""Router for ``Isom(self, other)`` being nonempty (ratified method
        placement, #100): existence of an isometry is the homset's emptiness
        question, and the G1 decision table lives on ``IsometryHomset``."""
        return not self.Isom(other).is_empty()

    def scale(self, scalar: ExactScalar | int, label: str = "scale") -> SyntheticLattice:
        scalar = QQ(scalar)
        return synthetic_lattice(scalar**2 * self.gram_matrix(), self.base_ring(), label)

    def twist(self, scalar: ExactScalar | int, label: str = "twist") -> SyntheticLattice:
        r"""The lattice with Gram scaled by ``scalar``. On a subobject the ambient
        is twisted and the inclusion kept, so subobject structure is preserved;
        a sign twist (``scalar == -1``) of a root lattice stays root-generated
        and keeps its Cartan provenance, while a general scale does not (the
        result is no longer generated by its roots)."""
        scalar = QQ(scalar)
        keeps_provenance = scalar == -1 and isinstance(self, _RootGeneratedProvenance)
        return synthetic_lattice(
            scalar * self.gram_matrix(),
            self.base_ring(),
            label,
            cartan_type=self._cartan_type if keeps_provenance else None,
        )

    def Hom(self, codomain: Lattice) -> LatticeHomset:
        from ..morphisms.homsets import LatticeHomset

        return LatticeHomset(self, codomain)

    def Isom(self, codomain: Lattice) -> IsometryHomset:
        r"""``Isom(L, M)`` as a first-class parent (ratified method
        placement, #100): existence, witness, and enumeration of isometries
        are the homset's own questions."""
        from ..morphisms.homsets import IsometryHomset

        return IsometryHomset(self, codomain)

    def Emb(self, codomain: Lattice) -> EmbeddingHomset:
        r"""``Emb(L, M)`` as a first-class parent — the home of embedding
        existence and enumeration (generator patterns in the definite
        regime; the indefinite Nikulin engines are issue #24)."""
        from ..morphisms.homsets import EmbeddingHomset

        return EmbeddingHomset(self, codomain)

    def hom(
        self,
        matrix_data: RawMorphismMatrix,
        codomain: Lattice | None = None,
    ) -> LatticeMorphism:
        from ..morphisms.homsets import LatticeHomset as SyntheticLatticeHomset
        from ..morphisms.homsets import LatticeMorphism as SyntheticLatticeMorphism

        codomain = self if codomain is None else codomain
        return SyntheticLatticeMorphism(SyntheticLatticeHomset(self, codomain), matrix_data)

    def embedding(
        self,
        matrix_data: RawMorphismMatrix,
        codomain: Lattice | None = None,
    ) -> LatticeMorphism:
        codomain = self if codomain is None else codomain
        return self.hom(matrix_data, codomain=codomain)

    # There is no ``inclusion_of(bare_lattice)``: two independently constructed
    # lattices are related only by a witnessing morphism, and fabricating one
    # from presentations is the drift #100 abolishes. Inclusions are minted
    # where they are created: ``subobject()`` / ``embedding()`` / kernels /
    # images / the overlattice constructors.

    def similarity(
        self,
        matrix_data: RawMorphismMatrix,
        codomain: Lattice,
        scalar: ExactScalar,
    ) -> LatticeSimilarity:
        from ..morphisms.homsets import LatticeSimilarity

        return LatticeSimilarity(self, codomain, matrix_data, scalar)

    # Restriction to a sublattice is composition with the carried inclusion --
    # ``morphism * subobject.inclusion()`` -- and needs no method of its own;
    # the deleted spelling took a bare lattice and guarded on the degenerate
    # bare is_submodule.

    # There is no lattice-level ``induced_map_on_quotient(morphism, quotient)``:
    # the body consumed only the morphism and the quotient, never the lattice
    # it was parked on — the method-placement gate (#100) sites it on the
    # morphism itself, ``morphism.induced_map_on_quotient(quotient)``.


class SyntheticNondegenerateLattice(NondegenerateLattice, SyntheticLattice):
    r"""Subcategory with an invertible Gram matrix: the dual vocabulary is defined."""

    def dual(self) -> SyntheticNondegenerateLattice:
        r"""The dual lattice, a based lattice with Gram ``G^{-1}``.

        Two conceptually distinct duals coincide here and resolve to this one
        object, as research usage expects:

        - the *metric dual* ``L^# = {x in L (x) QQ : b(x, L) subset ZZ}``, and
        - the *module dual* ``L^* = Hom_ZZ(L, ZZ)``,

        canonically identified through the nondegenerate form ``b``.  In the basis
        dual to ``L``'s own, the Gram matrix is ``G^{-1}``.  (This ``G^{-1}``
        convention is the correct one: e.g. it is exactly the change from the
        ``E_8`` root basis to its fundamental-weight basis in Bourbaki
        coordinates, where the weights are read off ``G^{-1}``.)

        Over ``QQ`` the canonical identification collapses: ``dual = self``
        (ratified 2026-07-03). The module-dual disambiguation for rational
        lattices (``Hom_ZZ`` vs ``Hom_QQ``, functionals as elements) is
        deferred design — gap-ledger entry 7.
        """
        if self.base_ring() is QQ:
            return self
        dual_lattice = synthetic_lattice(self.gram_matrix().inverse(), ZZ, f"{self._label}#")
        assert isinstance(dual_lattice, SyntheticNondegenerateLattice), (
            f"the dual of a nondegenerate lattice is nondegenerate (Gram G^-1 is invertible); dispatch returned {type(dual_lattice)}"
        )
        return dual_lattice

    def is_self_dual(self) -> bool:
        return self.base_ring() is ZZ and self == self.dual()

    def dual_inclusion(self) -> LatticeMorphism:
        r"""The natural injection ``L -> L^*``, ``v |-> b(v, -)``, with matrix ``G``."""
        return self.hom(self.gram_matrix(), codomain=self.dual())


class SyntheticIntegralNondegenerateLattice(IntegralNondegenerateLattice, SyntheticNondegenerateLattice):
    r"""Integral nondegenerate subcategory: discriminant/genus vocabulary (spec 2.4)."""

    def discriminant_group(self, primary: int | Integer = 0) -> SourcedDiscriminantForm:
        from ..forms.discriminant_forms import SyntheticSourcedDiscriminantForm

        return SyntheticSourcedDiscriminantForm(self, primary)

    def glue(self, isotropic_subgroup_or_gens: DiscriminantSubgroup | Sequence[DiscriminantFormElement], label: str = "glue") -> LatticeMorphism:
        r"""The overlattice glued along an isotropic subgroup of the
        discriminant form, as the inclusion morphism ``L -> L_glued``; its
        ``.index()`` is the subgroup's order."""
        return self.discriminant_group().overlattice_from_isotropic_subgroup(isotropic_subgroup_or_gens, label=label)

    def maximal_overlattice(self, p: int | None = None, label: str = "maximal_overlattice") -> LatticeMorphism:
        r"""A maximal (``p``-maximal when ``p`` is given) even overlattice, as
        the inclusion morphism ``L -> L^max`` composed from the successive
        isotropic glue steps -- the identity when this lattice is already
        maximal."""
        if p is None or ZZ(p) == 2:
            assert self.is_even(), "this lattice must be even to admit an even overlattice"
        embedding: LatticeMorphism = self.identity_morphism()
        while True:
            lattice = embedding.codomain()
            assert isinstance(lattice, SyntheticIntegralNondegenerateLattice), (
                f"an even overlattice of an integral nondegenerate lattice stays integral nondegenerate; found={type(lattice)}"
            )
            discriminant_group = lattice.discriminant_group(primary=0 if p is None else ZZ(p))
            isotropic_element = next(
                (
                    element
                    for element in discriminant_group.elements()
                    if any(coordinate != 0 for coordinate in element.coefficient_vector()) and discriminant_group.q(element) == 0
                ),
                None,
            )
            if isotropic_element is None:
                return embedding
            subgroup = discriminant_group.subgroup_generated_by([isotropic_element])
            assert subgroup.is_quadratic_isotropic(), f"isotropic element generated a non-isotropic subgroup: {isotropic_element}"
            embedding = discriminant_group.overlattice_from_isotropic_subgroup(subgroup, label=label) * embedding

    def local_modification(
        self,
        subgroup_or_gens: Matrix | DiscriminantSubgroup | Sequence[DiscriminantFormElement],
        p: int,
        label: str = "local_modification",
    ) -> Lattice:
        if isinstance(subgroup_or_gens, Matrix):
            gram = matrix(QQ, subgroup_or_gens)
            assert gram.is_square() and gram.nrows() == self.rank(), f"local modification Gram matrix must be square of lattice rank; rank={self.rank()}, gram={gram}"
            from ..lattice_categories import Lattice

            return Lattice(gram, base_ring=self.base_ring(), label=label)
        primary_discriminant_group = self.discriminant_group(primary=p)
        from ..forms.discriminant import SyntheticDiscriminantSubgroup

        if isinstance(subgroup_or_gens, SyntheticDiscriminantSubgroup):
            subgroup_ambient = subgroup_or_gens.ambient()
            assert subgroup_ambient == primary_discriminant_group, (
                "local modification subgroup must belong to this lattice's requested p-primary discriminant form; "
                f"requested_p={p}, subgroup_ambient={subgroup_ambient}, expected={primary_discriminant_group}"
            )
            return subgroup_ambient.overlattice_from_isotropic_subgroup(subgroup_or_gens, label=label).codomain()
        return primary_discriminant_group.overlattice_from_isotropic_subgroup(subgroup_or_gens, label=label).codomain()

    def genus(self) -> Genus:
        return self.discriminant_group().genus(self.signature_pair())

    def same_genus(self, other: IntegralNondegenerateLattice) -> bool:
        return self.genus() == other.genus()


if TYPE_CHECKING:
    # The enumeration/reduction kernels and the root-provenance mixin are never
    # instantiated alone: each is composed with a concrete SyntheticLattice at
    # T1, so inside their bodies ``self`` really is a SyntheticLattice. For type
    # checking we declare that host; at runtime the base stays the domain carrier
    # whose ParentMethods delta Sage installs.
    _PositiveDefiniteSelf = SyntheticNondegenerateLattice
    _DefiniteSelf = SyntheticNondegenerateLattice
    _RootGeneratedSelf = SyntheticLattice
else:
    _PositiveDefiniteSelf = PositiveDefiniteLattice
    _DefiniteSelf = DefiniteLattice
    _RootGeneratedSelf = RootGeneratedLattice


class _PositiveDefiniteEnumeration(_PositiveDefiniteSelf):
    r"""Spec 2.5 enumeration-kernel implementations, shared by the two
    positive-definite subcategories. The definite-level unification names
    (vectors_of_square, roots) are implemented here under the G4-ratified
    convention (positive definite is the natural regime; negative-definite
    lattices transport through L(-1) in their own kernel). The
    spec-2.6 reduction/CVP/Voronoi suite lives here too (decision D1 revised
    2026-07-04): Sage's own crypto lattice implementations presuppose exactly
    positive definiteness, so those methods are ordinary positive-definite
    vocabulary, not an opt-in refinement."""

    def vectors_of_square(self, square: ExactScalar | int) -> tuple[SyntheticLatticeElement, ...]:
        r"""All lattice vectors of the given (nonnegative) norm, by the
        positive-definite enumeration engine (G4 ratified semantics)."""
        square = ZZ(square)
        assert square >= 0, f"a positive-definite form takes no negative values; square={square}, gram={self.gram_matrix()}"
        if square == 0:
            return (self.zero(),)
        return tuple(self.short_vectors(square + 1)[square])

    def roots(self) -> tuple[SyntheticLatticeElement, ...]:
        r"""The norm-2 vectors (root convention in the positive-definite
        regime; the AG regime on negative-definite lattices is the L(-1)
        transport of this convention)."""
        return self.vectors_of_square(2)

    def LLL(self) -> SyntheticLattice:
        from sage.matrix.constructor import matrix
        from sage.rings.integer_ring import ZZ

        assert self.base_ring() is ZZ, "LLL is implemented only for ZZ-lattices in this spike"
        assert self.is_integral(), f"LLL requires an integral Gram matrix; gram={self.gram_matrix()}"
        change_of_basis = matrix(QQ, matrix(ZZ, self.gram_matrix()).LLL_gram())
        return self.sublattice(change_of_basis, label="LLL")

    def short_vectors(self, n: int | Integer, up_to_sign_flag: bool = False) -> list[list[SyntheticLatticeElement]]:
        from sage.quadratic_forms.quadratic_form import QuadraticForm
        from sage.rings.integer_ring import ZZ

        assert self.base_ring() is ZZ, "short vector enumeration is implemented only for ZZ-lattices in this spike"
        assert self.is_integral(), f"short vector enumeration requires an integral Gram matrix; gram={self.gram_matrix()}"
        q = QuadraticForm(2 * self.gram_matrix().change_ring(ZZ))
        return [[self(vector) for vector in vectors] for vectors in q.short_vector_list_up_to_length(n, up_to_sign_flag)]

    def shortest_vector(self) -> SyntheticLatticeElement:
        if self.rank() == 0:
            return self.zero()
        bound = ZZ(min(self.gen(i).q() for i in range(self.rank()))) + 1
        for vectors in self.short_vectors(bound):
            for candidate in vectors:
                if not candidate == self.zero():
                    return candidate
        assert False, "positive-definite short-vector enumeration returned no nonzero vector"

    def minimum(self) -> ExactScalar | SageInfinity:
        # lambda_1^2: the least nonzero norm (Sage IntegralLattice.minimum);
        # +Infinity on rank 0 (infimum over the empty set).
        if self.rank() == 0:
            from sage.rings.infinity import Infinity

            return Infinity
        return self.shortest_vector().q()

    def maximum(self) -> ExactScalar | SageInfinity:
        # Sup of the norm form over a positive-definite lattice is unbounded
        # (Sage IntegralLattice.maximum returns +Infinity).
        from sage.rings.infinity import Infinity

        return Infinity

    def volume(self) -> ExactScalar | SymbolicExpression:
        # Covolume sqrt(det G) (Sage IntegerLattice.volume) — exact, possibly
        # irrational, so the codomain includes exact symbolic values.
        return self.gram_matrix().determinant().sqrt()

    def reduced_basis(self) -> tuple[SyntheticLatticeElement, ...]:
        from sage.matrix.constructor import matrix
        from sage.rings.integer_ring import ZZ

        assert self.base_ring() is ZZ and self.is_integral(), "reduced basis requires an integral ZZ-lattice"
        transform = matrix(ZZ, self.gram_matrix()).LLL_gram()
        return tuple(self(row) for row in transform.rows())

    def enumerate_short_vectors(self, bound: int | Integer) -> Iterator[SyntheticLatticeElement]:
        for vectors in self.short_vectors(bound + 1):
            for lattice_vector in vectors:
                if not lattice_vector == self.zero():
                    yield lattice_vector

    def BKZ(self, block_size: int = 10, **kwargs: EnumerationKwargValue) -> SyntheticLattice:
        from sage.matrix.constructor import matrix
        from sage.rings.integer_ring import ZZ

        assert self.base_ring() is ZZ, "BKZ is implemented only for ZZ-lattices in this spike"
        assert self.is_integral(), f"BKZ requires an integral Gram matrix; gram={self.gram_matrix()}"
        import fpylll

        gram = matrix(ZZ, self.gram_matrix())
        gram_matrix = fpylll.IntegerMatrix.from_matrix(gram)
        transform = fpylll.IntegerMatrix.identity(gram.nrows())
        gso = fpylll.GSO.Mat(gram_matrix, U=transform, gram=True)
        lll = fpylll.LLL.Reduction(gso)
        params = fpylll.BKZ.Param(block_size=block_size, **kwargs)
        reduction = fpylll.BKZ.Reduction(gso, lll, params)
        reduction()
        change_of_basis = matrix(ZZ, transform)
        return self.sublattice(change_of_basis, label="BKZ")

    def closest_vector(self, target: Sequence[ExactScalar] | Vector | LatticeElement) -> SyntheticLatticeElement:
        from itertools import product

        from sage.functions.other import ceil, floor, sqrt
        from sage.matrix.constructor import matrix
        from sage.modules.free_module_element import vector
        from sage.rings.integer_ring import ZZ
        from sage.rings.rational_field import QQ

        from .elements import SyntheticLatticeElement

        point: Vector = vector(
            QQ,
            target.coefficient_vector() if isinstance(target, SyntheticLatticeElement) and target.parent() is self else target,
        )
        assert len(point) == self.rank(), f"closest vector target must have one coordinate per lattice basis vector; rank={self.rank()}, target={point}"
        if self.rank() == 0:
            return self.zero()
        gram = matrix(QQ, self.gram_matrix())

        def distance_squared(coordinates: Sequence[ExactScalar | int]) -> ExactScalar:
            delta = vector(QQ, [QQ(coordinates[i]) - point[i] for i in range(self.rank())])
            return delta * gram * delta

        best_coordinates = tuple(ZZ(point[i].round()) for i in range(self.rank()))
        best_distance = distance_squared(best_coordinates)
        inverse_gram = gram.inverse()
        ranges = []
        for i in range(self.rank()):
            radius = sqrt(best_distance * inverse_gram[i, i])
            lower = ZZ(floor(point[i] - radius)) - 1
            upper = ZZ(ceil(point[i] + radius)) + 1
            ranges.append(range(lower, upper + 1))
        for raw_coordinates in product(*ranges):
            candidate = tuple(ZZ(coordinate) for coordinate in raw_coordinates)
            distance = distance_squared(candidate)
            if distance < best_distance or (distance == best_distance and candidate < best_coordinates):
                best_distance = distance
                best_coordinates = candidate
        return self(best_coordinates)

    def voronoi_cell(self, radius: int | Integer | None = None) -> Polyhedron:
        from sage.geometry.polyhedron.constructor import Polyhedron as polyhedron
        from sage.matrix.constructor import matrix
        from sage.rings.integer_ring import ZZ
        from sage.rings.rational_field import QQ

        if self.rank() == 0:
            return polyhedron(vertices=[[]], base_ring=QQ)
        gram = matrix(QQ, self.gram_matrix())

        def cell_from_bound(bound: int | Integer) -> Polyhedron:
            inequalities: list[list[ExactScalar]] = []
            for vectors in self.short_vectors(bound):
                for lattice_vector in vectors:
                    if lattice_vector == self.zero():
                        continue
                    coordinates = vector(QQ, lattice_vector.coefficient_vector())
                    gram_vector = coordinates * gram
                    row: list[ExactScalar] = [QQ(lattice_vector.q()) / 2]
                    row.extend(-gram_vector[i] for i in range(self.rank()))
                    inequalities.append(row)
            return polyhedron(ieqs=inequalities, base_ring=QQ)

        if radius is not None:
            return cell_from_bound(ZZ(radius))
        bound = ZZ(max(self.gen(i).q() for i in range(self.rank())) + 1)
        for _ in range(8):
            cell = cell_from_bound(bound)
            if cell.is_compact():
                return cell
            bound *= 2
        assert False, "failed to find a compact Voronoi cell from enumerated short vectors"

    def HKZ(self) -> SyntheticLattice:
        # Hermite-Korkine-Zolotarev = full-block BKZ (Sage IntegerLattice.HKZ).
        return self.BKZ(block_size=self.rank())

    def gaussian_heuristic(self, exact_form: bool = False) -> SymbolicExpression:
        # Expected shortest length (Sage IntegerLattice.gaussian_heuristic;
        # both forms are exact symbolic expressions — gap-ledger row 12):
        # Stirling form det^(1/2n) * sqrt(n / (2 pi e)); exact Gamma form
        # (sqrt(det) * Gamma(1 + n/2))^(1/n) / sqrt(pi). Computed in SR with a
        # RATIONAL exponent QQ(1)/n — a Python ``1 / n`` is a float and
        # silently destroys exactness (the gap-ledger row 12 defect).
        from sage.functions.gamma import gamma
        from sage.rings.rational_field import QQ as rationals
        from sage.symbolic.constants import e, pi
        from sage.symbolic.ring import SR

        n = self.rank()
        exponent = rationals(1) / n
        determinant_sqrt = SR(self.gram_matrix().determinant()).sqrt()
        if exact_form:
            return (determinant_sqrt * gamma(1 + rationals(n) / 2)) ** exponent / pi.sqrt()
        return determinant_sqrt**exponent * (n / (2 * pi * e)).sqrt()

    def hadamard_ratio(self) -> SymbolicExpression:
        # Exact symbolic value; the n-th root uses a RATIONAL exponent (see
        # gaussian_heuristic on why ``1 / n`` is banned here).
        from sage.rings.rational_field import QQ as rationals
        from sage.symbolic.ring import SR

        n = self.rank()
        gram = self.gram_matrix()
        product_of_norms = SR(1)
        for i in range(n):
            product_of_norms = product_of_norms * SR(gram[i, i]).sqrt()
        return (SR(gram.determinant()).sqrt() / product_of_norms) ** (rationals(1) / n)

    def approximate_closest_vector(self, target: Sequence[ExactScalar] | Vector | LatticeElement) -> SyntheticLatticeElement:
        from sage.matrix.constructor import matrix
        from sage.modules.free_module_element import vector
        from sage.rings.integer_ring import ZZ
        from sage.rings.rational_field import QQ

        from .elements import SyntheticLatticeElement

        point: Vector = vector(
            QQ,
            target.coefficient_vector() if isinstance(target, SyntheticLatticeElement) and target.parent() is self else target,
        )
        assert len(point) == self.rank(), f"approximate closest vector target must have one coordinate per basis vector; rank={self.rank()}, target={point}"
        if self.rank() == 0:
            return self.zero()
        transform = matrix(QQ, matrix(ZZ, self.gram_matrix()).LLL_gram())
        reduced_coordinates = point * transform.inverse()
        rounded = vector(ZZ, [ZZ(coordinate.round()) for coordinate in reduced_coordinates])
        return self(rounded * transform)

    # babai is Sage's alias for approximate_closest_vector
    babai = approximate_closest_vector

    def voronoi_relevant_vectors(self) -> tuple[SyntheticLatticeElement, ...]:
        from sage.rings.integer_ring import ZZ

        if self.rank() == 0:
            return ()
        bound = ZZ(max(self.gen(i).q() for i in range(self.rank())) + 1)
        for _ in range(8):
            if self.voronoi_cell(radius=bound).is_compact():
                break
            bound *= 2
        candidates = [lattice_vector for vectors in self.short_vectors(2 * bound) for lattice_vector in vectors if not lattice_vector == self.zero()]
        relevant = []
        for v in candidates:
            v_coordinates = v.coefficient_vector()
            v_norm = v.q()
            if all(v == u or v == -u or not all((v_coordinates[i] - u.coefficient_vector()[i]) % 2 == 0 for i in range(self.rank())) or u.q() > v_norm for u in candidates):
                relevant.append(v)
        return tuple(relevant)

    def enumerate_close_vectors(self, target: Sequence[ExactScalar] | Vector | LatticeElement, radius: ExactScalar) -> list[SyntheticLatticeElement]:
        from itertools import product

        from sage.functions.other import ceil, floor, sqrt
        from sage.matrix.constructor import matrix
        from sage.modules.free_module_element import vector
        from sage.rings.integer_ring import ZZ
        from sage.rings.rational_field import QQ

        from .elements import SyntheticLatticeElement

        point: Vector = vector(
            QQ,
            target.coefficient_vector() if isinstance(target, SyntheticLatticeElement) and target.parent() is self else target,
        )
        assert len(point) == self.rank(), f"close vector target must have one coordinate per basis vector; rank={self.rank()}, target={point}"
        gram = matrix(QQ, self.gram_matrix())
        inverse_gram = gram.inverse()
        ranges = []
        for i in range(self.rank()):
            spread = sqrt(QQ(radius) * inverse_gram[i, i])
            ranges.append(range(ZZ(floor(point[i] - spread)) - 1, ZZ(ceil(point[i] + spread)) + 2))
        close = []
        for coordinates in product(*ranges):
            delta = vector(QQ, [QQ(coordinates[i]) - point[i] for i in range(self.rank())])
            if delta * gram * delta <= radius:
                close.append(self(coordinates))
        return close

    def update_reduced_basis(self, w: Sequence[ExactScalar] | SyntheticLatticeElement) -> SyntheticLattice:
        from .elements import SyntheticLatticeElement

        if isinstance(w, SyntheticLatticeElement) and w.parent() is self:
            coordinates = list(w.coefficient_vector())
        else:
            assert not isinstance(w, SyntheticLatticeElement), f"update_reduced_basis expects coordinates or an element of this lattice; found an element of {w.parent()}"
            coordinates = list(w)
        injected = self.overlattice([coordinates], label="update_reduced_basis").codomain()
        # an overlattice lives in the same rational quadratic space, so it stays
        # positive-definite (spec 2.6 deleted the dead non-PD fallback here);
        # the dispatch witness is the enumeration class itself
        assert isinstance(injected, _PositiveDefiniteEnumeration), f"update_reduced_basis overlattice must stay positive-definite; gram={injected.gram_matrix()}"
        reduced = injected.LLL()
        assert isinstance(reduced, SyntheticLattice)
        return reduced


class _NegativeDefiniteEnumeration(_DefiniteSelf):
    r"""G4 + row 9c (ratified 2026-07-04): negative-definite enumeration is BY
    DEFINITION the natural convention on L(-1) — short vectors of a
    negative-definite L ARE short vectors of L(-1). Every engine here
    transports through the sign twist and pulls elements back along the
    identity on coefficient vectors."""

    def _sign_twist(self) -> _PositiveDefiniteEnumeration:
        twisted = self.twist(-1, label="sign_twist")
        assert isinstance(twisted, _PositiveDefiniteEnumeration), f"the (-1)-twist of a negative-definite lattice is positive definite; dispatch returned {type(twisted)}"
        return twisted

    def _pull_element(self, element: LatticeElement) -> SyntheticLatticeElement:
        return self(list(element.coefficient_vector()))

    def minimum(self) -> ExactScalar | SageInfinity:
        # min{x^2} = -max over L(-1) (= -Infinity for positive rank).
        return -self._sign_twist().maximum()

    def maximum(self) -> ExactScalar | SageInfinity:
        # max{x^2 | x != 0} = -min over L(-1).
        return -self._sign_twist().minimum()

    def shortest_vector(self) -> SyntheticLatticeElement:
        return self._pull_element(self._sign_twist().shortest_vector())

    def short_vectors(self, n: int | Integer, up_to_sign_flag: bool = False) -> list[list[SyntheticLatticeElement]]:
        return [[self._pull_element(vector) for vector in vectors] for vectors in self._sign_twist().short_vectors(n, up_to_sign_flag)]

    def enumerate_short_vectors(self, bound: int | Integer) -> Iterator[SyntheticLatticeElement]:
        for twisted in self._sign_twist().enumerate_short_vectors(bound):
            yield self._pull_element(twisted)

    def volume(self) -> ExactScalar | SymbolicExpression:
        return self._sign_twist().volume()

    def vectors_of_square(self, square: ExactScalar | int) -> tuple[SyntheticLatticeElement, ...]:
        square = ZZ(square)
        assert square <= 0, f"a negative-definite form takes no positive values; square={square}, gram={self.gram_matrix()}"
        return tuple(self._pull_element(vector) for vector in self._sign_twist().vectors_of_square(-square))

    def roots(self) -> tuple[SyntheticLatticeElement, ...]:
        r"""The (-2)-vectors: the AG root convention on negative-definite
        lattices (G4 round-2 refinement), i.e. the L(-1) transport of the
        positive-definite norm-2 convention."""
        return self.vectors_of_square(-2)


class SyntheticPositiveDefiniteLattice(_PositiveDefiniteEnumeration, SyntheticNondegenerateLattice):
    r"""Positive-definite subcategory over QQ or with a non-integral form."""


class SyntheticIntegralPositiveDefiniteLattice(_PositiveDefiniteEnumeration, SyntheticIntegralNondegenerateLattice):
    r"""Integral positive-definite subcategory: full discriminant + enumeration kernel."""


class SyntheticNegativeDefiniteLattice(_NegativeDefiniteEnumeration, SyntheticNondegenerateLattice):
    r"""Negative-definite subcategory over QQ or with a non-integral form."""


class SyntheticIntegralNegativeDefiniteLattice(_NegativeDefiniteEnumeration, SyntheticIntegralNondegenerateLattice):
    r"""Integral negative-definite subcategory: discriminant vocabulary plus the
    L(-1)-transported enumeration kernel (G4 + row 9c)."""


class _RootGeneratedProvenance(_RootGeneratedSelf):
    r"""Provenance-attached vocabulary (spec 1.3/6): the axiom is a certificate
    carried from the named constructors, never detected from the Gram."""

    def cartan_type(self) -> CartanType:
        assert self._cartan_type != "composite", "a direct sum of root lattices has no single Cartan type; use irreducible_root_components()"
        assert self._cartan_type is not None and not isinstance(self._cartan_type, str), f"the root-provenance certificate must be a Cartan datum; found={self._cartan_type!r}"
        return self._cartan_type

    def bourbaki_embedding(self) -> LatticeMorphism:
        r"""The canonical embedding into the unimodular lattice ``I_{0,m}`` (or
        ``I_{m,0}`` for the positive twist) that realizes this root lattice as a
        genuine sublattice: the generators map to the Bourbaki simple roots,
        ``e_i |-> r_i``, and the images are the actual root vectors of the
        ambient. ``m`` is the ambient dimension of the root system; for A_n / E_6
        / E_7 it exceeds the rank, and for E-types the roots are half-integral,
        so the embedding is through the ambient's rational span."""
        from sage.combinat.root_system.root_system import RootSystem

        letter, rank = self.cartan_type()
        ambient_space = RootSystem([letter, rank]).ambient_space()
        dimension = ambient_space.dimension()
        roots = matrix(QQ, [ambient_space.simple_root(i).to_vector() for i in ambient_space.index_set()])
        sign = -1 if self.is_negative_definite() else 1
        label = f"I_{{{0 if sign < 0 else dimension},{dimension if sign < 0 else 0}}}"
        ambient: SyntheticLattice = synthetic_lattice(sign * identity_matrix(QQ, dimension), ZZ, label)
        if any(entry not in ZZ for entry in roots.list()):
            ambient = ambient.rationalization()
        return self.embedding(roots.transpose(), codomain=ambient)


class SyntheticRootGeneratedPositiveDefiniteLattice(_RootGeneratedProvenance, SyntheticIntegralPositiveDefiniteLattice):
    r"""Root lattices in the standard (positive definite) convention."""


class SyntheticRootGeneratedNegativeDefiniteLattice(_RootGeneratedProvenance, SyntheticIntegralNegativeDefiniteLattice):
    r"""Root lattices twisted by -1 (the K3/AG convention): the (-2)-vector
    root regime through the L(-1) transport kernel."""


class SyntheticRootGeneratedNondegenerateLattice(_RootGeneratedProvenance, SyntheticIntegralNondegenerateLattice):
    r"""Root-generated lattices of mixed signature (composite direct sums)."""


def synthetic_lattice(
    gram_matrix: RawGramMatrix,
    base_ring: BaseRing,
    label: str,
    cartan_type: CartanType | str | None = None,
    names: Sequence[str] | str | None = None,
) -> SyntheticLattice:
    r"""Private subcategory dispatch: one classification (mirroring ``category_for``),
    one concrete class per subcategory, so axiom vocabulary is reachable exactly
    where the mathematics defines it."""
    gram = matrix(QQ, gram_matrix)
    nondegenerate = gram.det() != 0
    integral = base_ring is ZZ and all(entry in ZZ for entry in gram.list())
    pos, neg = signature_pair(gram)
    concrete: type[SyntheticLattice]
    positive_definite = nondegenerate and pos == gram.nrows()
    if cartan_type is not None:
        even = integral and all(entry % 2 == 0 for entry in gram.diagonal())
        assert integral and nondegenerate and even, (
            "root-lattice provenance requires an integral nondegenerate EVEN Gram "
            "(the RootGenerated axiom lives over Even, and a bare .RootGenerated() "
            "call is a silent Sage no-op without it); "
            f"gram={gram}, cartan_type={cartan_type}; fix the named constructor"
        )
        if positive_definite:
            concrete = SyntheticRootGeneratedPositiveDefiniteLattice
        elif neg == gram.nrows() and gram.nrows() > 0:
            concrete = SyntheticRootGeneratedNegativeDefiniteLattice
        else:
            concrete = SyntheticRootGeneratedNondegenerateLattice
        # Instantiation with open @abstract_method contracts is the framework
        # design (TestSuite._test_not_implemented_methods enumerates the gap);
        # the two Nikulin embedding contracts are issue #24's open engines.
        return concrete(  # type: ignore[abstract]
            gram_matrix,
            base_ring,
            label,
            cartan_type=cartan_type,
            names=names,
        )
    negative_definite = nondegenerate and gram.nrows() > 0 and neg == gram.nrows()
    if integral and positive_definite:
        concrete = SyntheticIntegralPositiveDefiniteLattice
    elif positive_definite:
        concrete = SyntheticPositiveDefiniteLattice
    elif integral and negative_definite:
        concrete = SyntheticIntegralNegativeDefiniteLattice
    elif negative_definite:
        concrete = SyntheticNegativeDefiniteLattice
    elif integral and nondegenerate:
        concrete = SyntheticIntegralNondegenerateLattice
    elif nondegenerate:
        concrete = SyntheticNondegenerateLattice
    else:
        concrete = SyntheticLattice
    return concrete(gram_matrix, base_ring, label, names=names)
