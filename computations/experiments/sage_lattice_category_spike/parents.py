r"""Synthetic lattice parents."""

from __future__ import annotations

from sage.arith.functions import lcm
from sage.matrix.constructor import matrix
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.parent import Parent

from .arithmetic import block_diagonal_matrix, signature_pair
from .categories import RationalLattices
from .elements import SyntheticLatticeElement


def category_for(base_ring, gram):
    category = RationalLattices(base_ring).WithDistinguishedBasis().Symmetric()
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
    return category


class SyntheticLattice(Parent):
    r"""Synthetic lattice parent with owned elements and homsets."""

    Element = SyntheticLatticeElement

    def __init__(
        self,
        gram_matrix,
        base_ring,
        basis_matrix_over_rational_span,
        rational_gram_matrix,
        label,
    ):
        gram = matrix(QQ, gram_matrix)
        basis_matrix = matrix(QQ, basis_matrix_over_rational_span)
        rational_gram = matrix(QQ, rational_gram_matrix)
        if not (base_ring in (ZZ, QQ)):
            raise ValueError(f"lattice base ring must be ZZ or QQ; found={base_ring}")
        if not (gram.is_square()):
            raise ValueError(f"Gram matrix must be square; found={gram}")
        if not (basis_matrix.nrows() == gram.nrows()):
            raise ValueError("basis matrix row count must equal lattice rank; "
            f"rank={gram.nrows()}, rows={basis_matrix.nrows()}")
        if not (basis_matrix.ncols() == rational_gram.nrows()):
            raise ValueError("basis matrix columns must match rationalization rank; "
            f"basis columns={basis_matrix.ncols()}, rational rank={rational_gram.nrows()}")
        if not (gram == basis_matrix * rational_gram * basis_matrix.transpose()):
            raise ValueError("Gram matrix must be induced from the rationalization coordinates; "
            f"gram={gram}, basis={basis_matrix}, rational_gram={rational_gram}")
        gram.set_immutable()
        basis_matrix.set_immutable()
        rational_gram.set_immutable()
        self._gram_matrix = gram
        self._basis_matrix = basis_matrix
        self._rational_gram_matrix = rational_gram
        self._label = label
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
            and self.basis_matrix() == other.basis_matrix()
            and self._rational_gram_matrix == other._rational_gram_matrix
        )

    def value_ring(self):
        return QQ

    def rank(self):
        return self._gram_matrix.nrows()

    def degree(self):
        return self.rank()

    def basis_matrix(self, kind="user"):
        if not (kind in ("user", "echelon")):
            raise ValueError(f"basis kind must be 'user' or 'echelon'; found={kind}")
        if kind == "echelon":
            return self.echelonized_basis_matrix()
        return self._basis_matrix

    def echelonized_basis_matrix(self):
        return matrix(QQ, self.underlying_module().basis_matrix())

    def echelonized_basis(self):
        return tuple(vector(QQ, row) for row in self.echelonized_basis_matrix().rows())

    def has_user_basis(self):
        return True

    def user_to_echelon_matrix(self):
        echelon_module = self.rationalization_module().span(self.echelonized_basis_matrix().rows(), self.base_ring())
        return matrix(self.base_ring(), [echelon_module.coordinate_vector(vector(QQ, row)) for row in self.basis_matrix().rows()])

    def echelon_to_user_matrix(self):
        return self.user_to_echelon_matrix().inverse()

    def gram_matrix(self, basis="user"):
        if not (basis in ("user", "echelon")):
            raise ValueError(f"Gram matrix basis must be 'user' or 'echelon'; found={basis}")
        if basis == "user":
            return self._gram_matrix
        basis_matrix = self.basis_matrix(kind="echelon")
        gram = basis_matrix * self.ambient_gram_matrix() * basis_matrix.transpose()
        gram.set_immutable()
        return gram

    def inner_product_matrix(self, basis="user"):
        return self.gram_matrix(basis=basis)

    def ambient_gram_matrix(self):
        return self._rational_gram_matrix

    def bilinear_form(self):
        return self.b

    def quadratic_form(self):
        return self.q

    def rationalization_module(self):
        return QQ**self._rational_gram_matrix.nrows()

    def underlying_module(self):
        return self.rationalization_module().span(self.basis_matrix().rows(), self.base_ring())

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

    def coordinate_vector(self, element):
        if isinstance(element, SyntheticLatticeElement) and element.parent() is self:
            return element.coordinates()
        return self.underlying_module().coordinate_vector(vector(QQ, element))

    def echelon_coordinate_vector(self, element):
        if isinstance(element, SyntheticLatticeElement) and element.parent() is self:
            rational_coordinates = element.rational_coordinates()
        else:
            rational_coordinates = vector(QQ, element)
        return self.rationalization_module().span(self.echelonized_basis_matrix().rows(), self.base_ring()).coordinate_vector(rational_coordinates)

    def echelon_coordinates(self, element):
        return tuple(self.echelon_coordinate_vector(element))

    def coordinates(self, element, basis="user"):
        if not (basis in ("user", "echelon")):
            raise ValueError(f"coordinate basis must be 'user' or 'echelon'; found={basis}")
        if basis == "echelon":
            return self.echelon_coordinates(element)
        element = self(element) if not (isinstance(element, SyntheticLatticeElement) and element.parent() is self) else element
        return tuple(element.coordinates())

    def ambient_coordinates(self, element):
        element = self(element) if not (isinstance(element, SyntheticLatticeElement) and element.parent() is self) else element
        return tuple(element.rational_coordinates())

    def linear_combination_of_basis(self, coefficients):
        return self(coefficients)

    def lift(self, element):
        element = self(element) if not (isinstance(element, SyntheticLatticeElement) and element.parent() is self) else element
        return element.rational_coordinates()

    def retract(self, element):
        return self(self.coordinate_vector(element))

    def b(self, left, right):
        left = self(left) if left.parent() is not self else left
        right = self(right) if right.parent() is not self else right
        row = matrix(QQ, 1, self.rank(), list(left.coordinates()))
        col = matrix(QQ, self.rank(), 1, list(right.coordinates()))
        return (row * self.gram_matrix() * col)[0, 0]

    def q(self, element):
        element = self(element) if element.parent() is not self else element
        return self.b(element, element)

    def rational_span(self):
        return SyntheticLattice(
            self.gram_matrix(),
            QQ,
            self.basis_matrix(),
            self._rational_gram_matrix,
            f"{self._label}_QQ",
        )

    def change_ring(self, base_ring):
        if not (base_ring in (ZZ, QQ)):
            raise ValueError(f"lattice base ring must be ZZ or QQ; found={base_ring}")
        return SyntheticLattice(
            self.gram_matrix(),
            base_ring,
            self.basis_matrix(),
            self._rational_gram_matrix,
            f"{self._label}_over_{base_ring}",
        )

    change_base_ring = change_ring

    def dual_lattice(self):
        if not (self.base_ring() is ZZ):
            raise ValueError("metric dual is a ZZ-lattice construction")
        if not (self.determinant() != 0):
            raise ValueError(f"metric dual requires a nondegenerate form; gram={self.gram_matrix()}")
        dual_basis = self.gram_matrix().inverse() * self.basis_matrix()
        return self._from_module(self.rationalization_module().span(dual_basis.rows(), ZZ), f"{self._label}#")

    dual = dual_lattice

    def codual(self, value_ring=ZZ):
        if not (value_ring is ZZ):
            raise ValueError(f"only ZZ-valued coduals are implemented in this spike; found={value_ring}")
        return self.dual_lattice()

    def dual_pairing_lattice(self):
        return self.dual_lattice()

    def determinant(self):
        return self.gram_matrix().determinant()

    def discriminant(self):
        rank_half = self.rank() // 2
        return (-1) ** rank_half * self.determinant()

    signed_discriminant = discriminant

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
        return self.base_ring() is ZZ and self == self.dual_lattice()

    def is_degenerate(self):
        return self.determinant() == 0

    def radical(self, label="radical"):
        kernel_basis = self.gram_matrix().right_kernel().basis_matrix()
        if kernel_basis.nrows() == 0:
            return self.sublattice(matrix(QQ, 0, self.rank()), label=label)
        return self.sublattice(kernel_basis, label=label)

    def is_submodule(self, other):
        if not (isinstance(other, SyntheticLattice)):
            raise TypeError(f"expected SyntheticLattice; found={type(other)}")
        if not (self._rational_gram_matrix == other._rational_gram_matrix):
            raise ValueError("submodule comparison requires the same rationalization form; "
            f"left={self._rational_gram_matrix}, right={other._rational_gram_matrix}")
        return all(row in other.underlying_module() for row in self.basis_matrix().rows())

    def sublattice(self, generators, label="sublattice", check_integral=False):
        generator_matrix = matrix(QQ, generators)
        if not (generator_matrix.ncols() == self.rank()):
            raise ValueError("sublattice generators must be rows in the parent basis; "
            f"parent_rank={self.rank()}, generators={generator_matrix}")
        if generator_matrix.rank() == generator_matrix.nrows():
            basis_matrix = generator_matrix * self.basis_matrix()
        else:
            generator_module = (QQ**self.rank()).span(generator_matrix.rows(), self.base_ring())
            basis_matrix = matrix(QQ, generator_module.basis_matrix()) * self.basis_matrix()
        lattice = self._from_rational_basis(basis_matrix, self.base_ring(), label)
        if not (not check_integral or lattice.is_integral()):
            raise ValueError(f"sublattice is not integral; gram={lattice.gram_matrix()}")
        return lattice

    submodule = sublattice
    submodule_with_basis = sublattice

    def fractional_sublattice(self, generators, label="fractional_sublattice"):
        return self.sublattice(generators, label=label, check_integral=False)

    def span(self, generators, base_ring=None, label="span"):
        base_ring = self.base_ring() if base_ring is None else base_ring
        if not (base_ring in (ZZ, QQ)):
            raise ValueError(f"lattice span base ring must be ZZ or QQ; found={base_ring}")
        generator_matrix = matrix(QQ, generators)
        if not (generator_matrix.ncols() == self._rational_gram_matrix.nrows()):
            raise ValueError("span generators must be rows in rationalization coordinates; "
            f"rational_rank={self._rational_gram_matrix.nrows()}, generators={generator_matrix}")
        module = self.rationalization_module().span(generator_matrix.rows(), base_ring)
        return self._from_module(module, label)

    def span_of_basis(self, basis, base_ring=None, label="span"):
        base_ring = self.base_ring() if base_ring is None else base_ring
        basis_matrix = matrix(QQ, basis)
        if not (basis_matrix.rank() == basis_matrix.nrows()):
            raise ValueError(f"basis rows must be independent; basis={basis_matrix}")
        return self._from_rational_basis(basis_matrix, base_ring, label)

    def vector_space_span(self, generators, label="vector_space_span"):
        return self.span(generators, base_ring=QQ, label=label)

    def vector_space_span_of_basis(self, basis, label="vector_space_span"):
        return self.span_of_basis(basis, base_ring=QQ, label=label)

    def zero_lattice(self, label="zero_lattice"):
        return self._from_rational_basis(matrix(QQ, 0, self._rational_gram_matrix.nrows()), self.base_ring(), label)

    zero_submodule = zero_lattice

    def overlattice(self, generators, check_integral=False, label="overlattice"):
        generator_matrix = matrix(QQ, generators)
        if not (generator_matrix.ncols() == self._rational_gram_matrix.nrows()):
            raise ValueError("overlattice generators must be rows in rationalization coordinates; "
            f"rational_rank={self._rational_gram_matrix.nrows()}, generators={generator_matrix}")
        combined = self.basis_matrix().stack(generator_matrix)
        lattice = self.span(combined, base_ring=self.base_ring(), label=label)
        if not (self.is_submodule(lattice)):
            raise ValueError("overlattice must contain the source lattice")
        if not (not check_integral or lattice.is_integral()):
            raise ValueError(f"overlattice is not integral; gram={lattice.gram_matrix()}")
        return lattice

    def sum(self, other, label="sum"):
        self._assert_same_rationalization(other)
        base_ring = QQ if QQ in (self.base_ring(), other.base_ring()) else ZZ
        return self.span(self.basis_matrix().stack(other.basis_matrix()), base_ring=base_ring, label=label)

    def intersection(self, other, label="intersection"):
        self._assert_same_rationalization(other)
        return self._from_module(self.underlying_module().intersection(other.underlying_module()), label)

    def saturation(self, in_ambient=None, label="saturation"):
        if in_ambient is not None:
            return self.primitive_closure(in_ambient, label=label)
        return self._from_module(self.underlying_module().saturation(), label)

    def integral_saturation(self, label="integral_saturation"):
        lattice = self.saturation(label=label)
        if not (lattice.is_integral()):
            raise ValueError(f"integral saturation is not integral; gram={lattice.gram_matrix()}")
        return lattice

    def primitive_closure(self, ambient=None, label="primitive_closure"):
        if ambient is None:
            return self.saturation(label=label)
        self._assert_same_rationalization(ambient)
        rational_span = self.rationalization_module().span(self.basis_matrix().rows(), QQ)
        return self._from_module(ambient.underlying_module().intersection(rational_span), label)

    def index_in(self, other):
        self._assert_same_rationalization(other)
        return self.underlying_module().index_in(other.underlying_module())

    relative_index = index_in

    def index_in_saturation(self):
        return self.index_in(self.saturation())

    def denominator(self):
        return lcm([entry.denominator() for entry in self.basis_matrix().list()] or [ZZ.one()])

    def clear_denominators(self, label="clear_denominators"):
        return self.scale_basis(self.denominator(), label=label)

    def scale(self, scalar, label="scale"):
        return self.scale_basis(scalar, label=label)

    def underlying_quadratic_module(self):
        return self

    def underlying_quotient_module(self):
        raise NotImplementedError("lattices are not quotient modules; use finite_quotient or discriminant_group for quotients")

    def quotient_by_sublattice(self, sublattice):
        from .discriminant import SyntheticLatticeFiniteQuotient

        return SyntheticLatticeFiniteQuotient(self, sublattice)

    finite_quotient = quotient_by_sublattice

    def quotient_map_to(self, sublattice):
        quotient = self.quotient_by_sublattice(sublattice)
        return quotient.projection

    def cover_lattice(self):
        return self

    def relation_lattice(self):
        return self

    def orthogonal_complement(self, other, label="orthogonal_complement"):
        self._assert_same_rationalization(other)
        pairing = self.basis_matrix() * self._rational_gram_matrix * other.basis_matrix().transpose()
        kernel_basis = pairing.transpose().right_kernel().basis_matrix()
        return self.sublattice(kernel_basis, label=label)

    def direct_sum(self, other, label="direct_sum"):
        base_ring = QQ if QQ in (self.base_ring(), other.base_ring()) else ZZ
        return SyntheticLattice(
            block_diagonal_matrix(self.gram_matrix(), other.gram_matrix()),
            base_ring,
            block_diagonal_matrix(self.basis_matrix(), other.basis_matrix()),
            block_diagonal_matrix(self._rational_gram_matrix, other._rational_gram_matrix),
            label,
        )

    def tensor_product(self, other, label="tensor_product"):
        base_ring = QQ if QQ in (self.base_ring(), other.base_ring()) else ZZ
        rational_gram = self._rational_gram_matrix.tensor_product(other._rational_gram_matrix)
        basis_matrix = self.basis_matrix().tensor_product(other.basis_matrix())
        return SyntheticLattice(
            basis_matrix * rational_gram * basis_matrix.transpose(),
            base_ring,
            basis_matrix,
            rational_gram,
            label,
        )

    def is_primitive(self, sublattice):
        if not (isinstance(sublattice, SyntheticLattice)):
            raise TypeError(f"expected SyntheticLattice; found={type(sublattice)}")
        if not (sublattice.is_submodule(self)):
            raise ValueError("primitive test requires a sublattice of self")
        return sublattice.primitive_closure(self).basis_matrix() == sublattice.basis_matrix()

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
                    if any(coordinate != 0 for coordinate in element.coordinates()) and discriminant_group.q(element) == 0
                ),
                None,
            )
            if isotropic_element is None:
                return lattice
            subgroup = discriminant_group.submodule_with_gens([isotropic_element])
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

    def isometry_group(self, gens=None, check=True, is_finite=None):
        if gens is None:
            raise NotImplementedError("full isometry generator computation is not implemented for the synthetic spike")
        morphisms = tuple(self.Hom(self).from_matrix(g) for g in gens)
        if check:
            for morphism in morphisms:
                if not (morphism.matrix().det() in (1, -1)):
                    raise ValueError(f"isometry generator must be invertible; matrix={morphism.matrix()}")
        return morphisms

    automorphisms = isometry_group

    def acts_on(self, other, gens=None, check=True):
        if gens is None:
            raise NotImplementedError("full isometry generator computation is not implemented for the synthetic spike")
        self._assert_same_rationalization(other)
        if self.basis_matrix().nrows() != self.basis_matrix().ncols() or self.basis_matrix().rank() != self.rank():
            raise ValueError("acts_on requires the acting lattice to span the rationalization")
        morphisms = self.isometry_group(gens=gens, check=check)
        acting_basis = matrix(QQ, self.basis_matrix())
        other_module = other.underlying_module()
        for morphism in morphisms:
            action_matrix = matrix(QQ, morphism.matrix())
            for row in other.basis_matrix().rows():
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

    def scale_basis(self, scalar, label="scaled_basis"):
        scalar = QQ(scalar)
        scaled_basis = scalar * self.basis_matrix()
        return SyntheticLattice(
            scaled_basis * self._rational_gram_matrix * scaled_basis.transpose(),
            self.base_ring(),
            scaled_basis,
            self._rational_gram_matrix,
            label,
        )

    def twist(self, scalar, label="twist"):
        scalar = QQ(scalar)
        return SyntheticLattice(
            scalar * self.gram_matrix(),
            self.base_ring(),
            self.basis_matrix(),
            scalar * self._rational_gram_matrix,
            label,
        )

    def Hom(self, codomain):
        from .homsets import LatticeHomset

        return LatticeHomset(self, codomain)

    def hom(self, matrix_data, codomain):
        return self.Hom(codomain).from_matrix(matrix_data)

    module_hom = hom
    lattice_hom = hom
    isometry = hom
    embedding = hom

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
        return quotient.hom([quotient.projection(morphism(quotient.lift(generator))) for generator in quotient.gens()])

    def discriminant_group(self, primary=0):
        if not (self.base_ring() is ZZ):
            raise ValueError("discriminant group requires a ZZ-lattice")
        if not (self.determinant() != 0):
            raise ValueError(f"discriminant group requires a nondegenerate lattice; gram={self.gram_matrix()}")
        if not (self.is_integral()):
            raise ValueError(f"discriminant group requires an integral lattice; gram={self.gram_matrix()}")
        from .discriminant import SyntheticDiscriminantGroup

        return SyntheticDiscriminantGroup(self, primary)

    def _from_module(self, module, label):
        return self._from_rational_basis(matrix(QQ, module.basis_matrix()), module.base_ring(), label)

    def _from_rational_basis(self, basis_matrix, base_ring, label):
        basis_matrix = matrix(QQ, basis_matrix)
        return SyntheticLattice(
            basis_matrix * self._rational_gram_matrix * basis_matrix.transpose(),
            base_ring,
            basis_matrix,
            self._rational_gram_matrix,
            label,
        )

    def _assert_same_rationalization(self, other):
        if not (isinstance(other, SyntheticLattice)):
            raise TypeError(f"expected SyntheticLattice; found={type(other)}")
        if not (self._rational_gram_matrix == other._rational_gram_matrix):
            raise ValueError("operation requires the same rationalization form; "
            f"left={self._rational_gram_matrix}, right={other._rational_gram_matrix}")
