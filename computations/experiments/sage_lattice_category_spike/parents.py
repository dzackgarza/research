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

from sage.arith.functions import lcm
from sage.matrix.constructor import identity_matrix, matrix
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.parent import Parent

from .arithmetic import block_diagonal_matrix, signature_pair
from .categories import Lattices
from .domain_algebra import (
    IntegralNondegenerateLattice as IntegralNondegenerateCarrier,
    Lattice as LatticeCarrier,
    NondegenerateLattice as NondegenerateCarrier,
)
from .elements import SyntheticLatticeElement


def category_for(base_ring, gram):
    category = Lattices(base_ring)
    if gram.det() != 0:
        category = category.Nondegenerate()
    if base_ring is ZZ and all(entry in ZZ for entry in gram.list()):
        category = category.Integral()
        if all(entry % 2 == 0 for entry in gram.diagonal()):
            category = category.Even()
        if gram.det() in (ZZ.one(), -ZZ.one()):
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


class SyntheticLattice(LatticeCarrier, Parent):
    r"""Synthetic based lattice ``(base_ring, G)`` with owned elements and homsets."""

    Element = SyntheticLatticeElement

    def __init__(self, gram_matrix, base_ring, label, ambient=None, inclusion=None):
        gram = matrix(QQ, gram_matrix)
        if not (base_ring in (ZZ, QQ)):
            raise ValueError(f"lattice base ring must be ZZ or QQ; found={base_ring}")
        if not (gram.is_square()):
            raise ValueError(f"Gram matrix must be square; found={gram}")
        if ambient is not None:
            if not isinstance(ambient, SyntheticLattice):
                raise TypeError(f"ambient parent must be a SyntheticLattice; found={type(ambient)}")
            if ambient._ambient is not None:
                raise ValueError("ambient parent must itself be a root lattice (no nested ambients)")
            inclusion = matrix(QQ, inclusion)
            if not (inclusion.nrows() == gram.nrows()):
                raise ValueError("inclusion row count must equal lattice rank; "
                f"rank={gram.nrows()}, rows={inclusion.nrows()}")
            if not (inclusion.ncols() == ambient.rank()):
                raise ValueError("inclusion column count must equal ambient rank; "
                f"ambient_rank={ambient.rank()}, columns={inclusion.ncols()}")
            if not (gram == inclusion * ambient.gram_matrix() * inclusion.transpose()):
                raise ValueError("Gram matrix must be induced by the inclusion into the ambient; "
                f"gram={gram}, inclusion={inclusion}, ambient_gram={ambient.gram_matrix()}")
            inclusion.set_immutable()
        gram.set_immutable()
        self._gram_matrix = gram
        self._ambient = ambient
        self._inclusion = inclusion
        self._label = label
        self._base_ring = base_ring
        Parent.__init__(self, base=base_ring, category=category_for(base_ring, gram))

    def _repr_(self):
        return f"Synthetic lattice {self._label} of rank {self.rank()} over {self.base_ring()}"

    def _element_constructor_(self, coordinates):
        return self.element_class(self, coordinates)

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticLattice)
            and self.base_ring() == other.base_ring()
            and self.gram_matrix() == other.gram_matrix()
        )

    def __hash__(self):
        return hash((self.base_ring(), self.gram_matrix()))

    # -- based-model internals: the shared parent and the inclusion into it ------
    #
    # These are private.  They exist only so the subobject algebra can compute in
    # a common coefficient module; they are never part of the object's identity
    # and are never exposed as public methods (no basis_matrix / coordinates /
    # ambient_* / rationalization / underlying_module on the public surface).

    def _root(self):
        return self if self._ambient is None else self._ambient

    def _ambient_rank(self):
        return self.rank() if self._ambient is None else self._ambient.rank()

    def _ambient_gram(self):
        return self.gram_matrix() if self._ambient is None else self._ambient.gram_matrix()

    def _inclusion_rows(self):
        r"""This lattice's basis, as rows, in the root parent's intrinsic coordinates."""
        if self._ambient is None:
            return identity_matrix(QQ, self.rank())
        return matrix(QQ, self._inclusion)

    def _rationalization_module(self):
        return QQ ** self._ambient_rank()

    def _underlying_module(self):
        return self._rationalization_module().span(self._inclusion_rows().rows(), self.base_ring())

    def _from_ambient_basis(self, inclusion_rows, base_ring, label):
        r"""Build a subobject of this lattice's root from ``inclusion_rows`` (root coordinates)."""
        root = self._root()
        rows = matrix(QQ, inclusion_rows)
        if not (rows.ncols() == root.rank()):
            raise ValueError("inclusion rows must be given in the root's coordinates; "
            f"root_rank={root.rank()}, rows={rows}")
        gram = rows * root.gram_matrix() * rows.transpose()
        return synthetic_lattice(gram, base_ring, label, ambient=root, inclusion=rows)

    def _from_module(self, module, label):
        return self._from_ambient_basis(matrix(QQ, module.basis_matrix()), module.base_ring(), label)

    def _assert_same_ambient(self, other):
        if not (isinstance(other, SyntheticLattice)):
            raise TypeError(f"expected SyntheticLattice; found={type(other)}")
        if not (self._ambient_gram() == other._ambient_gram()):
            raise ValueError("operation requires a common parent lattice; "
            f"left_ambient_gram={self._ambient_gram()}, right_ambient_gram={other._ambient_gram()}")

    # -- Port: intrinsic invariants read straight off (base_ring, G) --------------

    def rank(self):
        return self._gram_matrix.nrows()

    def base_ring(self):
        return self._base_ring

    def ngens(self):
        return self.rank()

    def is_hyperbolic(self):
        pos, neg = self.signature_pair()
        return pos == 1 and neg == self.rank() - 1 and self.rank() >= 2

    def random_element(self):
        return self([self.base_ring().random_element() for _ in range(self.rank())])

    def reflection(self, v):
        r"""The reflection ``sigma_v(x) = x - (2 b(x,v)/q(v)) v`` in ``End(L)``."""
        v = self(v) if not (isinstance(v, SyntheticLatticeElement) and v.parent() is self) else v
        norm = self.q(v)
        if norm == 0:
            raise ValueError(f"reflection requires an anisotropic vector; q(v)=0 for v={v}")
        v_column = matrix(QQ, self.rank(), 1, list(v.coefficient_vector()))
        gram_v = self.gram_matrix() * v_column
        images = identity_matrix(QQ, self.rank()) - (2 / norm) * v_column * gram_v.transpose()
        for j in range(self.rank()):
            if not all(images[i, j] in self.base_ring() for i in range(self.rank())):
                raise ValueError(
                    "reflection does not map the lattice into itself over "
                    f"{self.base_ring()}; failing basis vector index={j}, "
                    f"image column={images.column(j)}, v={v}"
                )
        return self.hom(images.change_ring(self.base_ring()))

    def gram_matrix(self):
        return self._gram_matrix

    def bilinear_form(self):
        return self.b

    def quadratic_form(self):
        return self.q

    def basis(self):
        return tuple(self.gen(i) for i in range(self.rank()))

    def gens(self):
        return self.basis()

    def gen(self, i):
        row = [self.base_ring().zero()] * self.rank()
        row[i] = self.base_ring().one()
        return self(row)

    def zero(self):
        return self([self.base_ring().zero()] * self.rank())

    def lift(self, element):
        element = self(element) if not (isinstance(element, SyntheticLatticeElement) and element.parent() is self) else element
        return element.rational_coordinates()

    def retract(self, element):
        return self(self._underlying_module().coordinate_vector(vector(QQ, element)))

    def b(self, left, right):
        left = self(left) if left.parent() is not self else left
        right = self(right) if right.parent() is not self else right
        row = matrix(QQ, 1, self.rank(), list(left.coefficient_vector()))
        col = matrix(QQ, self.rank(), 1, list(right.coefficient_vector()))
        return (row * self.gram_matrix() * col)[0, 0]

    def q(self, element):
        element = self(element) if element.parent() is not self else element
        return self.b(element, element)

    def rationalization(self):
        return synthetic_lattice(
            self.gram_matrix(), QQ, f"{self._label}_QQ",
            ambient=self._ambient, inclusion=self._inclusion,
        )

    def base_extend(self, base_ring):
        if not (base_ring in (ZZ, QQ)):
            raise ValueError(f"lattice base ring must be ZZ or QQ; found={base_ring}")
        return synthetic_lattice(
            self.gram_matrix(), base_ring, f"{self._label}_over_{base_ring}",
            ambient=self._ambient, inclusion=self._inclusion,
        )

    def determinant(self):
        return self.gram_matrix().determinant()

    def discriminant(self):
        rank_half = self.rank() // 2
        return (-1) ** rank_half * self.determinant()

    def absolute_discriminant(self):
        return abs(self.determinant())

    def signature_pair(self):
        return signature_pair(self.gram_matrix())

    def signature(self):
        pos, neg = self.signature_pair()
        return pos - neg

    def is_integral(self):
        return all(entry in ZZ for entry in self.gram_matrix().list())

    def is_even(self):
        return self.is_integral() and all(entry % 2 == 0 for entry in self.gram_matrix().diagonal())

    def is_unimodular(self):
        return self.base_ring() is ZZ and self.is_integral() and self.determinant() in (1, -1)

    def is_self_dual(self):
        return self.base_ring() is ZZ and self == self.dual()

    def is_degenerate(self):
        return self.determinant() == 0

    def is_nondegenerate(self):
        return self.gram_matrix().rank() == self.rank()

    def is_positive_definite(self):
        pos, neg = self.signature_pair()
        return neg == 0 and pos == self.rank()

    def is_negative_definite(self):
        pos, neg = self.signature_pair()
        return pos == 0 and neg == self.rank()

    def is_definite(self):
        return self.is_positive_definite() or self.is_negative_definite()

    def is_indefinite(self):
        pos, neg = self.signature_pair()
        return pos > 0 and neg > 0

    def radical(self, label="radical"):
        kernel_basis = self.gram_matrix().right_kernel().basis_matrix()
        if kernel_basis.nrows() == 0:
            return self.sublattice(matrix(QQ, 0, self.rank()), label=label)
        return self.sublattice(kernel_basis, label=label)

    def radical_quotient(self, label="radical_quotient"):
        r"""``L / rad(L)``, a nondegenerate based lattice (functor stays in Lattices)."""
        gram = self.gram_matrix()
        kernel = gram.right_kernel()
        if kernel.dimension() == 0:
            return self
        rank = self.rank()
        if kernel.dimension() == rank:
            # Fully degenerate: rad(L) = L, so L/rad(L) is the rank-0 lattice.
            return synthetic_lattice(matrix(QQ, 0, 0), self.base_ring(), label)
        if self.base_ring() is QQ:
            complement = matrix(QQ, kernel.complement().basis_matrix())
        else:
            ambient = ZZ ** rank
            radical_module = ambient.submodule(
                [vector(ZZ, row * lcm([entry.denominator() for entry in row]))
                 for row in kernel.basis()]
            ).saturation()
            quotient = ambient.quotient(radical_module)
            complement = matrix(ZZ, [gen.lift() for gen in quotient.gens()])
        quotient_gram = complement * gram * complement.transpose()
        quotient_lattice = synthetic_lattice(quotient_gram, self.base_ring(), label)
        if not quotient_lattice.is_nondegenerate():
            raise ValueError(
                "radical quotient must be nondegenerate; "
                f"gram={quotient_lattice.gram_matrix()}"
            )
        return quotient_lattice

    # -- Subobject algebra: operations between sublattices of a common parent -----

    def is_submodule(self, other):
        self._assert_same_ambient(other)
        return all(row in other._underlying_module() for row in self._inclusion_rows().rows())

    def sublattice(self, generators, label="sublattice", require_subset=True, require_integral=True):
        generator_matrix = matrix(QQ, generators)
        if not (generator_matrix.ncols() == self.rank()):
            raise ValueError("sublattice generators must be rows in the parent basis; "
            f"parent_rank={self.rank()}, generators={generator_matrix}")
        if require_subset:
            parent_module = self._underlying_module()
            rational_generators = generator_matrix * self._inclusion_rows()
            for row in rational_generators.rows():
                if row not in parent_module:
                    raise ValueError("sublattice generators must lie in the parent lattice; "
                    f"generator={row}, parent={self}")
        if generator_matrix.rank() == generator_matrix.nrows():
            basis_matrix = generator_matrix * self._inclusion_rows()
        else:
            generator_module = (QQ**self.rank()).span(generator_matrix.rows(), self.base_ring())
            basis_matrix = matrix(QQ, generator_module.basis_matrix()) * self._inclusion_rows()
        lattice = self._from_ambient_basis(basis_matrix, self.base_ring(), label)
        if require_integral and not lattice.is_integral():
            raise ValueError(f"sublattice is not integral; gram={lattice.gram_matrix()}")
        return lattice

    def fractional_sublattice(self, generators, label="fractional_sublattice"):
        return self.sublattice(generators, label=label, require_subset=False, require_integral=False)

    def span(self, generators, base_ring=None, check_integral=None, check_even=None, label="span"):
        base_ring = self.base_ring() if base_ring is None else base_ring
        if not (base_ring in (ZZ, QQ)):
            raise ValueError(f"lattice span base ring must be ZZ or QQ; found={base_ring}")
        generator_matrix = matrix(QQ, generators)
        if not (generator_matrix.ncols() == self._ambient_rank()):
            raise ValueError("span generators must be rows in the parent's coordinates; "
            f"parent_rank={self._ambient_rank()}, generators={generator_matrix}")
        module = self._rationalization_module().span(generator_matrix.rows(), base_ring)
        lattice = self._from_module(module, label)
        if check_integral is True and not lattice.is_integral():
            raise ValueError(f"span is not integral; gram={lattice.gram_matrix()}")
        if check_even is True and not lattice.is_even():
            raise ValueError(f"span is not even; gram={lattice.gram_matrix()}")
        return lattice

    def span_of_basis(self, basis, base_ring=None, label="span"):
        base_ring = self.base_ring() if base_ring is None else base_ring
        basis_matrix = matrix(QQ, basis)
        if not (basis_matrix.rank() == basis_matrix.nrows()):
            raise ValueError(f"basis rows must be independent; basis={basis_matrix}")
        return self._from_ambient_basis(basis_matrix, base_ring, label)

    def zero_lattice(self, label="zero_lattice"):
        return self._from_ambient_basis(matrix(QQ, 0, self._ambient_rank()), self.base_ring(), label)

    def overlattice(self, generators, check_integral=False, label="overlattice"):
        generator_matrix = matrix(QQ, generators)
        if not (generator_matrix.ncols() == self._ambient_rank()):
            raise ValueError("overlattice generators must be rows in the parent's coordinates; "
            f"parent_rank={self._ambient_rank()}, generators={generator_matrix}")
        combined = self._inclusion_rows().stack(generator_matrix)
        lattice = self.span(combined, base_ring=self.base_ring(), label=label)
        if not (self.is_submodule(lattice)):
            raise ValueError("overlattice must contain the source lattice")
        if not (not check_integral or lattice.is_integral()):
            raise ValueError(f"overlattice is not integral; gram={lattice.gram_matrix()}")
        return lattice

    def sum(self, other, label="sum"):
        self._assert_same_ambient(other)
        base_ring = QQ if QQ in (self.base_ring(), other.base_ring()) else ZZ
        return self.span(self._inclusion_rows().stack(other._inclusion_rows()), base_ring=base_ring, label=label)

    def intersection(self, other, label="intersection"):
        self._assert_same_ambient(other)
        return self._from_module(self._underlying_module().intersection(other._underlying_module()), label)

    def saturation(self, in_ambient=None, label="saturation"):
        if in_ambient is not None:
            return self.primitive_closure(in_ambient, label=label)
        return self._from_module(self._underlying_module().saturation(), label)

    def primitive_closure(self, ambient=None, label="primitive_closure"):
        if ambient is None:
            return self.saturation(label=label)
        self._assert_same_ambient(ambient)
        rationalization = self._rationalization_module().span(self._inclusion_rows().rows(), QQ)
        return self._from_module(ambient._underlying_module().intersection(rationalization), label)

    def index_in(self, other):
        self._assert_same_ambient(other)
        return self._underlying_module().index_in(other._underlying_module())

    def index_in_saturation(self):
        return self.index_in(self.saturation())

    def denominator(self):
        return lcm([entry.denominator() for entry in self.gram_matrix().list()] or [ZZ.one()])

    def clear_denominators(self, label="clear_denominators"):
        return self.scale(self.denominator(), label=label)

    def finite_quotient(self, sublattice):
        from .discriminant import SyntheticLatticeFiniteQuotient

        return SyntheticLatticeFiniteQuotient(self, sublattice)

    def quotient_map_to(self, sublattice):
        quotient = self.finite_quotient(sublattice)
        return quotient.projection

    def cover_lattice(self):
        return self

    def relation_lattice(self):
        return self

    def orthogonal_complement(self, other, label="orthogonal_complement"):
        self._assert_same_ambient(other)
        pairing = self._inclusion_rows() * self._ambient_gram() * other._inclusion_rows().transpose()
        kernel_basis = pairing.transpose().right_kernel().basis_matrix()
        return self.sublattice(kernel_basis, label=label)

    def direct_sum(self, other, label="direct_sum"):
        base_ring = QQ if QQ in (self.base_ring(), other.base_ring()) else ZZ
        return synthetic_lattice(
            block_diagonal_matrix(self.gram_matrix(), other.gram_matrix()),
            base_ring,
            label,
        )

    def tensor_product(self, other, label="tensor_product"):
        base_ring = QQ if QQ in (self.base_ring(), other.base_ring()) else ZZ
        return synthetic_lattice(
            self.gram_matrix().tensor_product(other.gram_matrix()),
            base_ring,
            label,
        )

    def is_primitive(self, sublattice):
        if not (isinstance(sublattice, SyntheticLattice)):
            raise TypeError(f"expected SyntheticLattice; found={type(sublattice)}")
        if not (sublattice.is_submodule(self)):
            raise ValueError("primitive test requires a sublattice of self")
        return sublattice.primitive_closure(self)._inclusion_rows() == sublattice._inclusion_rows()

    def isometry_group(self, gens=None, check=True, is_finite=None):
        # O(L) as its generating isometries. Generators are computed lazily and only
        # on request: a definite lattice reuses Sage's finite automorphism group
        # (ephemeral -- the Sage object is discarded, only the matrices survive),
        # while an indefinite lattice has an infinite O(L) and requires explicit
        # generators (fails loud otherwise), matching Sage's own restriction.
        if gens is None:
            gens = self._computed_isometry_generators()
        morphisms = tuple(self.Hom(self).from_matrix(g) for g in gens)
        if check:
            for morphism in morphisms:
                if not (morphism.matrix().det() in (1, -1)):
                    raise ValueError(f"isometry generator must be invertible; matrix={morphism.matrix()}")
        return morphisms

    def _computed_isometry_generators(self):
        if not (self.base_ring() is ZZ and self.is_integral() and self.determinant() != 0):
            raise NotImplementedError("O(L) generators are computed only for nondegenerate integral ZZ-lattices")
        if not self.is_definite():
            raise NotImplementedError(
                "indefinite O(L) is infinite; supply explicit generators via isometry_group(gens=...)"
            )
        from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

        # Sage's generators V satisfy V G V^T = G; the synthetic convention U^T G U = G
        # is met by U = V^T.
        orthogonal_group = IntegralLattice(matrix(ZZ, self.gram_matrix())).orthogonal_group()
        return tuple(matrix(ZZ, generator.matrix()).transpose() for generator in orthogonal_group.gens())

    def is_isometric(self, other):
        if not (isinstance(other, SyntheticLattice)):
            raise TypeError(f"expected SyntheticLattice; found={type(other)}")
        if self.rank() != other.rank() or self.signature_pair() != other.signature_pair():
            return False
        if not (self.base_ring() is ZZ and other.base_ring() is ZZ and self.is_integral() and other.is_integral()):
            raise NotImplementedError("isometry testing is implemented for integral ZZ-lattices")
        if not (self.is_definite() and other.is_definite()):
            raise NotImplementedError(
                "indefinite isometry testing is not implemented; compare genus/discriminant form explicitly"
            )
        from sage.quadratic_forms.quadratic_form import QuadraticForm

        # QuadraticForm(matrix) reads the matrix as the Hessian (2 x Gram); sign-normalize
        # to positive definite so is_globally_equivalent_to applies.
        sign = 1 if self.is_positive_definite() else -1
        return QuadraticForm(2 * sign * matrix(ZZ, self.gram_matrix())).is_globally_equivalent_to(
            QuadraticForm(2 * sign * matrix(ZZ, other.gram_matrix()))
        )

    def acts_on(self, other, gens=None, check=True):
        if gens is None:
            raise NotImplementedError("full isometry generator computation is not implemented for the synthetic spike")
        self._assert_same_ambient(other)
        acting_basis = self._inclusion_rows()
        if acting_basis.nrows() != acting_basis.ncols() or acting_basis.rank() != self.rank():
            raise ValueError("acts_on requires the acting lattice to span the ambient")
        morphisms = self.isometry_group(gens=gens, check=check)
        other_module = other._underlying_module()
        for morphism in morphisms:
            action_matrix = matrix(QQ, morphism.matrix())
            for row in other._inclusion_rows().rows():
                coordinates = acting_basis.solve_left(matrix(QQ, 1, acting_basis.ncols(), list(row)))
                image_coordinates = action_matrix * coordinates.transpose()
                image_row = vector(QQ, [
                    sum(image_coordinates[j, 0] * acting_basis[j, i] for j in range(self.rank()))
                    for i in range(acting_basis.ncols())
                ])
                if image_row not in other_module:
                    return False
        return True

    def action_on_discriminant_group(self, gens=None):
        discriminant_group = self.discriminant_group()
        return tuple(discriminant_group.action_of_isometry(g) for g in self.isometry_group(gens=gens))

    def kernel_on_discriminant_group(self, gens):
        actions = self.action_on_discriminant_group(gens)
        return tuple(
            generator
            for generator, action in zip(self.isometry_group(gens=gens), actions)
            if action.is_identity()
        )

    def scale(self, scalar, label="scale"):
        scalar = QQ(scalar)
        return synthetic_lattice(scalar ** 2 * self.gram_matrix(), self.base_ring(), label)

    def twist(self, scalar, label="twist"):
        scalar = QQ(scalar)
        return synthetic_lattice(scalar * self.gram_matrix(), self.base_ring(), label)

    def Hom(self, codomain):
        from .homsets import LatticeHomset

        return LatticeHomset(self, codomain)

    def hom(self, matrix_data, codomain=None):
        codomain = self if codomain is None else codomain
        return self.Hom(codomain).from_matrix(matrix_data)

    def embedding(self, matrix_data, codomain=None, primitive=False):
        codomain = self if codomain is None else codomain
        morphism = self.hom(matrix_data, codomain=codomain)
        if primitive and not codomain.is_primitive(morphism.image()):
            raise ValueError("primitive embedding requires a primitive image sublattice")
        return morphism

    def similarity(self, matrix_data, codomain, scalar):
        from .homsets import LatticeSimilarity

        return LatticeSimilarity(self, codomain, matrix_data, scalar)

    def restriction_to_sublattice(self, morphism, sublattice):
        if not (sublattice.is_submodule(self)):
            raise ValueError("restriction domain must be a sublattice")
        return sublattice.Hom(morphism.codomain()).from_matrix(morphism.matrix())

    def induced_map_on_discriminant_group(self, isometry):
        return self.discriminant_group().action_of_isometry(isometry)

    def induced_map_on_quotient(self, morphism, quotient):
        if not (morphism.domain() == quotient.cover_lattice() and morphism.codomain() == quotient.cover_lattice()):
            raise ValueError("induced quotient endomorphism requires a morphism of the quotient cover lattice")
        relation_lattice = quotient.relation_lattice()
        for row in relation_lattice._inclusion_rows().rows():
            relation_coordinates = morphism.domain()._underlying_module().coordinate_vector(vector(QQ, row))
            image = morphism(morphism.domain()(relation_coordinates))
            if vector(QQ, image.rational_coordinates()) not in relation_lattice._underlying_module():
                raise ValueError("morphism does not preserve the quotient relation lattice")
        return quotient.hom([quotient.projection(morphism(quotient.lift(generator))) for generator in quotient.gens()])


class SyntheticNondegenerateLattice(NondegenerateCarrier, SyntheticLattice):
    r"""Stratum with an invertible Gram matrix: the dual vocabulary is defined."""

    def dual(self):
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
        """
        if not (self.base_ring() is ZZ):
            raise ValueError("dual lattice is a ZZ-lattice construction")
        return synthetic_lattice(self.gram_matrix().inverse(), ZZ, f"{self._label}#")

    def dual_inclusion(self):
        r"""The natural injection ``L -> L^*``, ``v |-> b(v, -)``, with matrix ``G``."""
        return self.Hom(self.dual()).from_matrix(self.gram_matrix())


class SyntheticIntegralNondegenerateLattice(IntegralNondegenerateCarrier, SyntheticNondegenerateLattice):
    r"""Integral nondegenerate stratum: discriminant/genus vocabulary (spec 2.4)."""

    def discriminant_group(self, primary=0):
        from .discriminant import SyntheticDiscriminantGroup

        return SyntheticDiscriminantGroup(self, primary)

    def glue(self, isotropic_subgroup_or_gens, label="glue"):
        return self.discriminant_group().overlattice_from_isotropic_subgroup(isotropic_subgroup_or_gens, label=label)

    def maximal_overlattice(self, p=None, label="maximal_overlattice"):
        if p is None or ZZ(p) == 2:
            if not (self.is_even()):
                raise ValueError("this lattice must be even to admit an even overlattice")
        lattice = self
        while True:
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
                return lattice
            subgroup = discriminant_group.subgroup_generated_by([isotropic_element])
            if not (subgroup.is_quadratic_isotropic()):
                raise ValueError(f"isotropic element generated a non-isotropic subgroup: {isotropic_element}")
            lattice = discriminant_group.overlattice_from_isotropic_subgroup(subgroup, label=label)

    def local_modification(self, subgroup_or_gens, p, label="local_modification"):
        if hasattr(subgroup_or_gens, "is_square"):
            gram = matrix(QQ, subgroup_or_gens)
            if not (gram.is_square() and gram.nrows() == self.rank()):
                raise ValueError("local modification Gram matrix must be square of lattice rank; "
                f"rank={self.rank()}, gram={gram}")
            from .lattice_categories import Lattice

            return Lattice(gram, base_ring=self.base_ring(), label=label)
        primary_discriminant_group = self.discriminant_group(primary=p)
        return primary_discriminant_group.overlattice_from_isotropic_subgroup(subgroup_or_gens, label=label)

    def genus(self):
        return self.discriminant_group().genus(self.signature_pair(), even=self.is_even())

    def same_genus(self, other):
        return self.genus() == other.genus()


def synthetic_lattice(gram_matrix, base_ring, label, ambient=None, inclusion=None):
    r"""Private stratum router: one classification (mirroring ``category_for``),
    one concrete class per stratum, so axiom vocabulary is reachable exactly
    where the mathematics defines it."""
    gram = matrix(QQ, gram_matrix)
    nondegenerate = gram.det() != 0
    integral = base_ring is ZZ and all(entry in ZZ for entry in gram.list())
    if integral and nondegenerate:
        concrete = SyntheticIntegralNondegenerateLattice
    elif nondegenerate:
        concrete = SyntheticNondegenerateLattice
    else:
        concrete = SyntheticLattice
    return concrete(gram_matrix, base_ring, label, ambient=ambient, inclusion=inclusion)
