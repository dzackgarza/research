r"""Discriminant quotients for synthetic integral lattices."""

from __future__ import annotations

from itertools import permutations, product

from sage.arith.functions import lcm
from sage.matrix.constructor import identity_matrix, matrix
from sage.misc.cachefunc import cached_method
from sage.misc.prandom import choice
from sage.modules.free_module_element import vector
from sage.rings.complex_mpfr import ComplexField
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.element import Element
from sage.structure.parent import Parent

from .arithmetic import rational_mod
from .categories import DiscriminantForms
from .value_objects import value_module
from .elements import SyntheticLatticeElement
from .parents import SyntheticLattice


def _lattice_key(lattice):
    return (
        repr(lattice.base_ring()),
        lattice.rank(),
        tuple(lattice._basis_matrix.list()),
        tuple(lattice.gram_matrix().list()),
        tuple(lattice._rational_gram_matrix.list()),
    )


def _finite_group_invariant_factors(elements, zero, scalar_multiply):
    cardinality = ZZ(len(elements))
    if cardinality == 1:
        return ()
    primary_powers_by_prime = []
    for prime, exponent_bound in cardinality.factor():
        c_values = [ZZ.zero()]
        for exponent in range(1, ZZ(exponent_bound) + 1):
            killed = ZZ(
                sum(
                    1
                    for element in elements
                    if scalar_multiply(ZZ(prime) ** ZZ(exponent), element) == zero
                )
            )
            c_values.append(killed.valuation(prime))
        at_least = [ZZ.zero()] + [c_values[i] - c_values[i - 1] for i in range(1, len(c_values))]
        powers = []
        for exponent in range(1, len(c_values)):
            next_count = at_least[exponent + 1] if exponent + 1 < len(at_least) else ZZ.zero()
            exact_count = at_least[exponent] - next_count
            powers.extend([ZZ(prime) ** ZZ(exponent)] * ZZ(exact_count))
        primary_powers_by_prime.append(tuple(powers))
    rank = max(len(powers) for powers in primary_powers_by_prime)
    invariant_factors = [ZZ.one()] * rank
    for powers in primary_powers_by_prime:
        offset = rank - len(powers)
        for i, power in enumerate(sorted(powers)):
            invariant_factors[offset + i] *= power
    return tuple(invariant for invariant in invariant_factors if invariant != 1)


def _finite_coordinates(group, element):
    element = group(element)
    if hasattr(element, "coordinates"):
        return tuple(element.coordinates())
    return tuple(group.coordinates(element))


def _all_group_automorphisms(group):
    if group.ngens() == 0:
        return (SyntheticDiscriminantAction(group, identity_matrix(ZZ, 0)),)
    automorphisms = []
    candidates = tuple(group.elements())
    for images in product(candidates, repeat=group.ngens()):
        action = SyntheticDiscriminantAction.from_images(group, images)
        if action.is_automorphism():
            automorphisms.append(action)
    return tuple(automorphisms)


def _finite_all_subgroups(parent):
    seen = {}
    zero = parent.subgroup(())
    seen[zero._key()] = zero
    frontier = [zero]
    while frontier:
        subgroup = frontier.pop()
        for element in parent.elements():
            generated = parent.subgroup(tuple(subgroup.gens()) + (element,))
            key = generated._key()
            if key not in seen:
                seen[key] = generated
                frontier.append(generated)
    return tuple(seen[key] for key in sorted(seen, key=lambda item: sorted(item)))


def _finite_relations_among(parent, gens):
    gens = tuple(parent(gen) for gen in gens)
    ranges = tuple(range(parent.order(generator)) for generator in gens)
    return tuple(
        tuple(ZZ(coefficient) for coefficient in coefficients)
        for coefficients in product(*ranges)
        if parent.discrete_exp(coefficients, gens=gens) == parent.zero()
    )


def _finite_basis_from_generators(parent, gens):
    subgroup = parent.subgroup(gens)
    if not (subgroup.cardinality() == parent.cardinality()):
        raise ValueError("generators do not span the whole group")
    return tuple(parent(gen) for gen in gens)


def _finite_scalar_multiply(parent, scalar, element):
    if hasattr(parent, "_scalar_multiply_element"):
        return parent._scalar_multiply_element(scalar, element)
    return ZZ(scalar) * element


def _finite_p_torsion(parent, p, k=1):
    p = ZZ(p)
    k = ZZ(k)
    if not p.is_prime():
        raise ValueError(f"p-torsion requires a prime; found={p}")
    if not k >= 1:
        raise ValueError(f"p-torsion exponent must be positive; found={k}")
    return parent.subgroup(element for element in parent.elements() if _finite_scalar_multiply(parent, p ** k, element) == parent.zero())


def _form_matrix_on_images(group, images):
    images = tuple(group(image) for image in images)
    form = matrix(QQ, len(images), len(images))
    for i, left in enumerate(images):
        for j, right in enumerate(images):
            form[i, j] = group.q(left) if i == j else group.b(left, right)
    form.set_immutable()
    return form


class SyntheticDiscriminantGroupElement(Element):
    r"""Element of ``L# / L`` in Smith invariant coordinates."""

    def __init__(self, parent, coordinates):
        Element.__init__(self, parent)
        if isinstance(coordinates, SyntheticDiscriminantGroupElement):
            coordinates = coordinates.coordinates()
        if coordinates == 0:
            coordinates = [ZZ.zero()] * parent.ngens()
        coords = vector(ZZ, coordinates)
        if not (len(coords) == parent.ngens()):
            raise ValueError("discriminant coordinates must match Smith invariant count; "
            f"invariants={parent.invariants()}, coordinates={coordinates}")
        coords = vector(ZZ, [coords[i] % parent.invariants()[i] for i in range(parent.ngens())])
        coords.set_immutable()
        self._coordinates = coords

    def _repr_(self):
        return repr(self._coordinates)

    def coordinates(self):
        return self._coordinates

    def b(self, other):
        return self.parent().b(self, other)

    def q(self):
        return self.parent().q(self)

    def _add_(self, other):
        return self.parent()(self.coordinates() + other.coordinates())

    def _sub_(self, other):
        return self.parent()(self.coordinates() - other.coordinates())

    def _neg_(self):
        return self.parent()(-self.coordinates())

    def _lmul_(self, scalar):
        return self.parent()(ZZ(scalar) * self.coordinates())

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticDiscriminantGroupElement)
            and self.parent() == other.parent()
            and self.coordinates() == other.coordinates()
        )

    def __hash__(self):
        return hash((self.parent(), tuple(self.coordinates())))


class SyntheticDiscriminantGroup(Parent):
    r"""Owned finite discriminant quotient ``L# / L``."""

    Element = SyntheticDiscriminantGroupElement

    def __init__(self, source_lattice, primary):
        if not (isinstance(source_lattice, SyntheticLattice)):
            raise TypeError(f"expected SyntheticLattice source; found={type(source_lattice)}")
        if not (primary == 0 or ZZ(primary).is_prime()):
            raise ValueError(f"primary must be 0 or prime; found={primary}")
        self._source_lattice = source_lattice
        self._primary = ZZ(primary)
        smith, _smith_left, smith_right = matrix(ZZ, source_lattice.gram_matrix()).smith_form()
        self._smith_right_transpose = smith_right.transpose()
        self._smith_right_inverse_transpose = smith_right.inverse().transpose()
        positions = []
        invariants = []
        multipliers = []
        for i in range(smith.nrows()):
            invariant = abs(smith[i, i])
            if invariant == 1:
                continue
            if self._primary:
                valuation = ZZ(invariant).valuation(self._primary)
                if valuation == 0:
                    continue
                primary_invariant = self._primary ** valuation
                positions.append(i)
                invariants.append(primary_invariant)
                multipliers.append(invariant // primary_invariant)
            else:
                positions.append(i)
                invariants.append(invariant)
                multipliers.append(ZZ.one())
        self._invariant_positions = tuple(positions)
        self._coordinate_multipliers = tuple(multipliers)
        if self._primary:
            invariants = tuple(invariants)
        self._invariants = tuple(invariants)
        category = DiscriminantForms(ZZ).Bilinear().WithSourceLattice()
        if source_lattice.is_even():
            category = DiscriminantForms(ZZ).Quadratic().Even().WithSourceLattice()
        Parent.__init__(self, base=ZZ, category=category)

    def _repr_(self):
        return f"Synthetic discriminant group with invariants {self.invariants()}"

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticDiscriminantGroup)
            and _lattice_key(self.source_lattice()) == _lattice_key(other.source_lattice())
            and self._primary == other._primary
            and self.invariants() == other.invariants()
        )

    def __hash__(self):
        return hash((_lattice_key(self.source_lattice()), self._primary, self.invariants()))

    def _element_constructor_(self, coordinates):
        if isinstance(coordinates, SyntheticDiscriminantGroupElement) and coordinates.parent() is self:
            return coordinates
        return self.element_class(self, coordinates)

    def rank(self):
        return self._source_lattice.rank()

    def ngens(self):
        return len(self.invariants())

    def source_lattice(self):
        return self._source_lattice

    def cover(self):
        return self._source_lattice.dual_lattice()

    V = cover
    dual_cover = cover
    dual_lattice = cover
    cover_lattice = cover

    def relations(self):
        return self._source_lattice

    W = relations
    relation_lattice = relations

    def invariants(self):
        return self._invariants

    invariant_factors = invariants

    def underlying_abelian_group(self):
        return self

    def cardinality(self):
        if not self.invariants():
            return ZZ.one()
        return ZZ.prod(self.invariants())

    def is_finite(self):
        return True

    def annihilator(self):
        if not self.invariants():
            return ZZ.one()
        return lcm(self.invariants())

    exponent = annihilator

    def is_cyclic(self):
        return len(self.invariants()) <= 1

    def short_name(self):
        if not self.invariants():
            return "0"
        return " + ".join(f"Z/{invariant}" for invariant in self.invariants())

    def generator_orders(self):
        return self.invariants()

    def elementary_divisors(self):
        divisors = []
        for invariant in self.invariants():
            for prime, exponent in ZZ(invariant).factor():
                divisors.append(ZZ(prime) ** ZZ(exponent))
        return tuple(sorted(divisors))

    def rank_p(self, p):
        p = ZZ(p)
        if not (p.is_prime()):
            raise ValueError(f"p-rank requires a prime; found={p}")
        return ZZ(sum(1 for invariant in self.invariants() if ZZ(invariant) % p == 0))

    length_p = rank_p

    def value_module(self):
        return value_module(ZZ, ZZ.one())

    def value_module_qf(self):
        return value_module(ZZ, self._quadratic_modulus() * ZZ.one())

    @cached_method
    def gram_matrix_bilinear(self):
        raw_form = self._raw_form_matrix()
        form = matrix(QQ, raw_form.nrows(), raw_form.ncols())
        for i in range(raw_form.nrows()):
            for j in range(raw_form.ncols()):
                form[i, j] = rational_mod(raw_form[i, j], 1)
        form.set_immutable()
        return form

    @cached_method
    def gram_matrix_quadratic(self):
        raw_form = self._raw_form_matrix()
        form = matrix(QQ, raw_form.nrows(), raw_form.ncols())
        bilinear_form = self.gram_matrix_bilinear()
        for i in range(raw_form.nrows()):
            for j in range(raw_form.ncols()):
                form[i, j] = bilinear_form[i, j]
        for i in range(raw_form.nrows()):
            form[i, i] = rational_mod(raw_form[i, i], self._quadratic_modulus())
        form.set_immutable()
        return form

    def b(self, left, right):
        left = self(left) if left.parent() is not self else left
        right = self(right) if right.parent() is not self else right
        row = matrix(QQ, 1, self.ngens(), list(left.coordinates()))
        col = matrix(QQ, self.ngens(), 1, list(right.coordinates()))
        return rational_mod((row * self.gram_matrix_bilinear() * col)[0, 0], 1)

    inner_product = b

    def q(self, element):
        element = self(element) if element.parent() is not self else element
        row = matrix(QQ, 1, self.ngens(), list(element.coordinates()))
        col = matrix(QQ, self.ngens(), 1, list(element.coordinates()))
        return rational_mod((row * self.gram_matrix_quadratic() * col)[0, 0], self._quadratic_modulus())

    quadratic_product = q

    def is_nondegenerate(self):
        return self.cardinality() == abs(self.source_lattice().determinant())

    def gens(self):
        return tuple(self.gen(i) for i in range(self.ngens()))

    def smith_form_gens(self):
        transform = self.smith_to_gens()
        raw = self.gens()
        return tuple(self.discrete_exp(transform.column(j), gens=raw) for j in range(transform.ncols()))

    smith_generators = smith_form_gens

    def gen(self, i):
        row = [ZZ.zero()] * self.ngens()
        row[i] = ZZ.one()
        return self(row)

    def smith_form_gen(self, i):
        return self.smith_form_gens()[i]

    def zero(self):
        return self([ZZ.zero()] * self.ngens())

    identity = zero

    @cached_method
    def elements(self):
        if not self.invariants():
            return (self([]),)
        return tuple(self(coordinates) for coordinates in product(*[range(invariant) for invariant in self.invariants()]))

    def list(self):
        return self.elements()

    def random_element(self):
        return choice(self.elements())

    def order(self, element=None):
        if element is None:
            return self.cardinality()
        element = self(element) if element.parent() is not self else element
        orders = []
        for coordinate, invariant in zip(element.coordinates(), self.invariants()):
            if coordinate == 0:
                orders.append(ZZ.one())
            else:
                orders.append(invariant // ZZ(coordinate).gcd(invariant))
        return lcm(orders) if orders else ZZ.one()

    def lift(self, element):
        z_coordinates = self._old_dual_coordinates(self(element))
        source_coordinates = self.source_lattice().gram_matrix().inverse() * z_coordinates
        rational_coordinates = vector(QQ, source_coordinates.column(0)) * self.source_lattice()._basis_matrix
        cover = self.cover()
        cover_coordinates = cover.underlying_module().coordinate_vector(vector(QQ, rational_coordinates))
        return cover(cover_coordinates)

    def projection(self, element):
        cover = self.cover()
        if isinstance(element, SyntheticLatticeElement):
            if not (element.parent() == cover):
                raise ValueError("projection expects an element of the dual cover; "
                f"expected={cover}, found={element.parent()}")
        else:
            element = cover(element)
        rational_coordinates = vector(QQ, element.rational_coordinates())
        source_rational_module = self.source_lattice().rationalization_module().span(self.source_lattice()._basis_matrix.rows(), QQ)
        source_coordinates = matrix(QQ, self.rank(), 1, list(source_rational_module.coordinate_vector(rational_coordinates)))
        z_coordinates = self.source_lattice().gram_matrix() * source_coordinates
        smith_coordinates = self._smith_right_transpose * matrix(ZZ, z_coordinates)
        projected = []
        for position, invariant, multiplier in zip(
            self._invariant_positions,
            self.invariants(),
            self._coordinate_multipliers,
        ):
            projected.append((ZZ(smith_coordinates[position, 0]) * ZZ(multiplier).inverse_mod(invariant)) % invariant)
        return self(projected)

    lift_to_dual = lift
    project_from_dual = projection
    coset_representative = lift

    def primary_part(self, p):
        return SyntheticDiscriminantGroup(self.source_lattice(), p)

    p_primary_part = primary_part

    def primary_decomposition(self):
        return tuple(self.primary_part(p) for p in ZZ(self.annihilator()).prime_divisors())

    primary_parts = primary_decomposition

    def submodule_with_gens(self, gens):
        return SyntheticDiscriminantSubgroup(self, gens)

    submodule = submodule_with_gens
    subgroup = submodule_with_gens
    subgroup_generated_by = submodule_with_gens
    from_generators = submodule_with_gens

    def torsion_subgroup(self):
        return self

    def contains_subgroup(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return subgroup.ambient() is self

    def coordinates(self, element, gens=None, reduce=True):
        if gens is None:
            return tuple(self(element).coordinates())
        return self.discrete_log(element, gens=gens)

    def discrete_exp(self, coefficients, gens=None):
        gens = self.gens() if gens is None else tuple(self(gen) for gen in gens)
        if not (len(coefficients) == len(gens)):
            raise ValueError("coefficient vector length must match generator count; "
            f"coefficients={coefficients}, gens={gens}")
        value = self.zero()
        for coefficient, generator in zip(coefficients, gens):
            value += ZZ(coefficient) * generator
        return value

    def discrete_log(self, element, gens=None):
        element = self(element)
        if gens is None:
            return tuple(element.coordinates())
        gens = tuple(self(gen) for gen in gens)
        ranges = tuple(range(self.order(generator)) for generator in gens)
        for coefficients in product(*ranges):
            if self.discrete_exp(coefficients, gens=gens) == element:
                return tuple(ZZ(coefficient) for coefficient in coefficients)
        raise ValueError(f"element is not generated by the supplied generators: {element}")

    def linear_combination_of_smith_form_gens(self, coefficients):
        return self.discrete_exp(coefficients, gens=self.smith_form_gens())

    def gens_to_smith(self):
        return identity_matrix(ZZ, self.ngens())

    def smith_to_gens(self):
        return identity_matrix(ZZ, self.ngens())

    def gens_vector(self, element, reduce=True):
        return vector(ZZ, self.coordinates(element))

    coordinate_vector = gens_vector
    coordinates_in_smith_basis = coordinates
    coordinates_in_generators = coordinates

    def generator_relations(self):
        return matrix.diagonal(ZZ, self.invariants())

    def relations_among(self, gens):
        gens = tuple(self(gen) for gen in gens)
        ranges = tuple(range(self.order(generator)) for generator in gens)
        return tuple(
            tuple(ZZ(coefficient) for coefficient in coefficients)
            for coefficients in product(*ranges)
            if self.discrete_exp(coefficients, gens=gens) == self.zero()
        )

    def basis_from_generators(self, gens):
        subgroup = self.subgroup(gens)
        if not (subgroup.cardinality() == self.cardinality()):
            raise ValueError("generators do not span the whole group")
        return tuple(self(gen) for gen in gens)

    def orthogonal_submodule_to(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return self.submodule_with_gens(
            element
            for element in self.elements()
            if all(self.b(element, subgroup_element) == 0 for subgroup_element in subgroup.elements())
        )

    def all_submodules(self):
        seen = {}
        zero = self.submodule_with_gens(())
        seen[zero._key()] = zero
        frontier = [zero]
        while frontier:
            subgroup = frontier.pop()
            for element in self.elements():
                generated = self.submodule_with_gens(tuple(subgroup.gens()) + (element,))
                key = generated._key()
                if key not in seen:
                    seen[key] = generated
                    frontier.append(generated)
        return tuple(seen[key] for key in sorted(seen, key=lambda item: sorted(item)))

    all_subgroups = all_submodules
    subgroups = all_submodules

    def isotropic_subgroups(self):
        return tuple(subgroup for subgroup in self.all_submodules() if self.is_isotropic_subgroup(subgroup))

    isotropic_submodules = isotropic_subgroups

    def is_isotropic_element(self, element):
        return self.q(element) == 0

    def isotropic_elements(self):
        return tuple(element for element in self.elements() if self.is_isotropic_element(element))

    def is_isotropic_subgroup(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return subgroup.is_quadratic_isotropic()

    is_totally_isotropic = is_isotropic_subgroup

    def is_lagrangian(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return self.is_isotropic_subgroup(subgroup) and subgroup.cardinality() ** 2 == self.cardinality()

    def lagrangian_subgroups(self):
        return tuple(subgroup for subgroup in self.isotropic_subgroups() if self.is_lagrangian(subgroup))

    metabolizers = lagrangian_subgroups

    def is_metabolic(self):
        return bool(self.lagrangian_subgroups())

    def is_anisotropic(self):
        return all(element == self.zero() for element in self.isotropic_elements())

    def is_maximal_isotropic(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        if not self.is_isotropic_subgroup(subgroup):
            return False
        subgroup_key = subgroup._key()
        for candidate in self.isotropic_subgroups():
            if subgroup_key < candidate._key():
                return False
        return True

    def maximal_isotropic_subgroups(self):
        return tuple(subgroup for subgroup in self.isotropic_subgroups() if self.is_maximal_isotropic(subgroup))

    def orthogonal(self, subgroup_or_gens):
        return self.orthogonal_submodule_to(subgroup_or_gens)

    orthogonal_complement = orthogonal

    def orthogonal_quotient(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        if not self.is_isotropic_subgroup(subgroup):
            raise ValueError("orthogonal quotient requires a quadratic-isotropic relation subgroup")
        if subgroup.cardinality() == 1:
            return self
        orthogonal = self.orthogonal(subgroup)
        if orthogonal._key() == subgroup._key():
            return SyntheticDiscriminantSubquotient(self, subgroup, orthogonal)
        return SyntheticDiscriminantSubquotient(self, subgroup, orthogonal)

    def quotient_group(self, subgroup_or_gens):
        return SyntheticDiscriminantGroupQuotient(self, self._subgroup(subgroup_or_gens))

    quotient = quotient_group

    def quotient_map(self, subgroup_or_gens):
        quotient = self.quotient(subgroup_or_gens)
        return lambda element: quotient.projection(element)

    def cosets(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        unseen = set(self.elements())
        cosets = []
        while unseen:
            representative = min(unseen, key=lambda element: tuple(element.coordinates()))
            coset = frozenset(representative + element for element in subgroup.elements())
            cosets.append(coset)
            unseen.difference_update(coset)
        return tuple(cosets)

    def p_torsion(self, p, k=1):
        p = ZZ(p)
        k = ZZ(k)
        if not (p.is_prime()):
            raise ValueError(f"p-torsion requires a prime; found={p}")
        return self.subgroup(element for element in self.elements() if (p ** k) * element == self.zero())

    def overlattice_from_isotropic_subgroup(self, subgroup_or_gens, label="overlattice"):
        subgroup = self._subgroup(subgroup_or_gens)
        if not (subgroup.is_bilinear_isotropic()):
            raise ValueError("overlattice construction requires a bilinear-isotropic subgroup")
        lift_rows = [self.lift(generator).rational_coordinates() for generator in subgroup.gens()]
        if not lift_rows:
            return self.source_lattice()
        return self.source_lattice().overlattice(lift_rows, check_integral=True, label=label)

    def preimage_lattice(self, subgroup_or_gens, label="preimage_lattice"):
        subgroup = self._subgroup(subgroup_or_gens)
        lift_rows = [self.lift(generator).rational_coordinates() for generator in subgroup.gens()]
        if not lift_rows:
            return self.source_lattice()
        return self.source_lattice().overlattice(lift_rows, check_integral=False, label=label)

    def discriminant_form_of_overlattice(self, subgroup_or_gens):
        return self.overlattice_from_isotropic_subgroup(subgroup_or_gens).discriminant_group()

    def action_of_isometry(self, isometry):
        if self.ngens() == 0:
            return SyntheticDiscriminantAction(self, identity_matrix(ZZ, 0))
        gram = matrix(QQ, self.source_lattice().gram_matrix())
        isometry_matrix = matrix(QQ, isometry.matrix())
        induced_images = []
        for generator in self.gens():
            old_coordinates = self._old_dual_coordinates(generator)
            new_coordinates = gram * isometry_matrix * gram.inverse() * old_coordinates
            source_coordinates = gram.inverse() * new_coordinates
            rational_coordinates = vector(QQ, source_coordinates.column(0)) * self.source_lattice()._basis_matrix
            cover = self.cover()
            cover_coordinates = cover.underlying_module().coordinate_vector(vector(QQ, rational_coordinates))
            induced_images.append(self.projection(cover(cover_coordinates)))
        return SyntheticDiscriminantAction.from_images(self, induced_images)

    action_of_lattice_isometry = action_of_isometry

    def action_of_lattice_group(self, gens):
        return self.orthogonal_group_from_lattice_gens(gens)

    image_of_lattice_group = action_of_lattice_group

    def kernel_of_lattice_group_action(self, gens):
        return tuple(
            gen
            for gen in gens
            if self.action_of_lattice_isometry(gen).is_identity()
        )

    def orbit(self, element, group=None):
        element = self(element)
        group = self.orthogonal_group() if group is None else group
        return frozenset(action(element) for action in group)

    def orbits(self, group=None):
        unseen = set(self.elements())
        orbits = []
        while unseen:
            representative = next(iter(unseen))
            orbit = self.orbit(representative, group=group)
            orbits.append(orbit)
            unseen.difference_update(orbit)
        return tuple(orbits)

    def orbits_on_subgroups(self, group=None):
        group = self.orthogonal_group() if group is None else group
        subgroups = set(self.all_subgroups())
        orbits = []
        while subgroups:
            representative = next(iter(subgroups))
            orbit = frozenset(self.subgroup(action(element) for element in representative.elements()) for action in group)
            orbits.append(orbit)
            subgroups.difference_update(orbit)
        return tuple(orbits)

    def orbits_on_isotropic_subgroups(self, group=None):
        isotropic = set(self.isotropic_subgroups())
        return tuple(orbit for orbit in self.orbits_on_subgroups(group=group) if orbit & isotropic)

    def hom(self, images):
        return SyntheticDiscriminantAction.from_images(self, images)

    def orthogonal_group(self, gens=None, check=False, kind="quadratic"):
        if not (kind in ("quadratic", "bilinear")):
            raise ValueError(f"orthogonal group kind must be quadratic or bilinear; found={kind}")
        if gens is None:
            return SyntheticOrthogonalGroup(self, self._brute_force_orthogonal_group(kind=kind))
        actions = tuple(SyntheticDiscriminantAction(self, matrix(ZZ, gen)) for gen in gens)
        if check:
            for action in actions:
                if not (action.preserves_form(kind=kind)):
                    raise ValueError(f"discriminant action does not preserve the form; matrix={action.matrix()}")
        return SyntheticOrthogonalGroup(self, actions, close=True)

    isometry_group = orthogonal_group

    def automorphism_group(self):
        return SyntheticOrthogonalGroup(self, _all_group_automorphisms(self))

    def bilinear_orthogonal_group(self, gens=None, check=False):
        return self.orthogonal_group(gens=gens, check=check, kind="bilinear")

    def quadratic_orthogonal_group(self, gens=None, check=False):
        return self.orthogonal_group(gens=gens, check=check, kind="quadratic")

    def orthogonal_group_from_lattice_gens(self, gens):
        isometries = []
        for gen in gens:
            if hasattr(gen, "matrix"):
                isometries.append(gen)
            else:
                isometries.append(self.source_lattice().isometry_group(gens=[gen])[0])
        return SyntheticOrthogonalGroup(self, (self.action_of_isometry(gen) for gen in isometries), close=True)

    @cached_method
    def normal_form(self, partial=False, return_isometry=False):
        r"""Return a canonical generator-presentation Gram matrix."""
        best_key = None
        best_matrix = None
        best_images = None
        for images in self._invariant_basis_candidates():
            gram = self._transformed_quadratic_gram(images)
            key = tuple(gram.list())
            if best_key is None or key < best_key:
                best_key = key
                best_matrix = gram
                best_images = images
        if not (best_matrix is not None):
            raise ValueError("finite invariant-basis enumeration produced no presentation; "
            f"invariants={self.invariants()}")
        best_matrix.set_immutable()
        normal_form = self.invariants(), best_matrix
        if return_isometry:
            return normal_form, SyntheticDiscriminantAction.from_images(self, best_images)
        return normal_form

    def is_isomorphic(self, other, kind="quadratic"):
        if not (isinstance(other, SyntheticDiscriminantGroup)):
            raise TypeError(f"expected SyntheticDiscriminantGroup; found={type(other)}")
        if not (kind in ("group", "bilinear", "quadratic")):
            raise ValueError(f"isomorphism kind must be group, bilinear, or quadratic; found={kind}")
        if self.invariants() != other.invariants():
            return False
        if kind == "group":
            return True
        return any(self._images_preserve_structure(other, images, kind) for images in self._isomorphism_images_to(other))

    is_isomorphic_to = is_isomorphic

    def isometry_to(self, other, kind="quadratic"):
        if not (kind in ("quadratic", "bilinear")):
            raise ValueError(f"isometry kind must be quadratic or bilinear; found={kind}")
        if not (isinstance(other, SyntheticDiscriminantGroup)):
            raise TypeError(f"expected SyntheticDiscriminantGroup; found={type(other)}")
        if not self.is_isomorphic(other, kind=kind):
            raise ValueError("discriminant forms are not isomorphic")
        for images in self._isomorphism_images_to(other):
            if self._images_preserve_structure(other, images, kind):
                return SyntheticDiscriminantAction.from_images(self, (self(image.coordinates()) for image in images))
        raise ValueError("no isometry found")

    def _isomorphism_images_to(self, other):
        candidates_by_generator = tuple(
            tuple(element for element in other.elements() if other.order(element) == invariant)
            for invariant in self.invariants()
        )
        return (images for images in product(*candidates_by_generator) if other._generates_full_group(images))

    def _mapped_to(self, other, element, images):
        return other.discrete_exp(self.coordinates(element), gens=images)

    def _images_preserve_structure(self, other, images, kind):
        for left in self.elements():
            mapped_left = self._mapped_to(other, left, images)
            if kind == "quadratic" and self.q(left) != other.q(mapped_left):
                return False
            for right in self.elements():
                mapped_right = self._mapped_to(other, right, images)
                if self.b(left, right) != other.b(mapped_left, mapped_right):
                    return False
        return True

    def radical(self):
        return self.subgroup(element for element in self.elements() if all(self.b(element, other) == 0 for other in self.elements()))

    left_kernel = radical
    right_kernel = radical
    annihilator_subgroup = orthogonal

    def restricted_form(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return matrix(QQ, [[self.q(element) if i == j else self.b(element, other) for j, other in enumerate(subgroup.gens())] for i, element in enumerate(subgroup.gens())])

    def pushforward_form(self, phi):
        if not (phi.discriminant_group() is self):
            raise ValueError("pushforward requires an endomorphism of this discriminant group")
        inverse = phi.inverse()
        return _form_matrix_on_images(self, [inverse(generator) for generator in self.gens()])

    def pullback_form(self, phi):
        if not (phi.discriminant_group() is self):
            raise ValueError("pullback requires an endomorphism of this discriminant group")
        return _form_matrix_on_images(self, [phi(generator) for generator in self.gens()])

    def subquotient_form(self, subgroup_or_gens, quotient_subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        quotient_subgroup = self._subgroup(quotient_subgroup_or_gens)
        if not subgroup._key() <= quotient_subgroup._key():
            raise ValueError("subquotient form requires H contained in K")
        if not self.is_isotropic_subgroup(subgroup):
            raise ValueError("subquotient form requires a quadratic-isotropic relation subgroup")
        if not quotient_subgroup._key() <= self.orthogonal(subgroup)._key():
            raise ValueError("subquotient form requires K contained in the orthogonal complement of H")
        return SyntheticDiscriminantSubquotient(self, subgroup, quotient_subgroup)

    def character_group(self):
        return self

    def pontryagin_dual(self):
        if not self.is_nondegenerate():
            raise ValueError("Pontryagin dual identification requires a nondegenerate form; found degenerate")
        return self.pairing_isomorphism_to_dual()

    def pairing_character(self, element):
        element = self(element)
        return lambda other: self.b(element, other)

    def pairing_isomorphism_to_dual(self):
        return {element: self.pairing_character(element) for element in self.elements()}

    def brown_invariant(self):
        r"""Return the Brown invariant in ``ZZ/8`` for finite quadratic forms."""
        if self._quadratic_modulus() != 2:
            raise ValueError("Brown invariant requires a quadratic form with values in QQ / 2 ZZ")
        if self.cardinality() == 1:
            return ZZ.zero()
        values = [QQ(self.q(element)) / 2 for element in self.elements()]
        root_order = lcm([value.denominator() for value in values] or [ZZ.one()])
        CC = ComplexField(200)
        zeta = CC.zeta(root_order)
        gauss_sum = sum(zeta ** ZZ(value * root_order) for value in values)
        normalized = gauss_sum / CC(self.cardinality()).sqrt()
        zeta8 = CC.zeta(8)
        tolerance = CC(2) ** (-120)
        for residue in range(8):
            if abs(normalized - zeta8 ** residue) < tolerance:
                return ZZ(residue)
        raise ArithmeticError(f"Gauss sum is not an eighth root of unity: {normalized}")

    def is_genus(self, signature_pair, even=True):
        r"""Return whether this discriminant form passes Sage's even-genus tests."""
        s_plus = ZZ(signature_pair[0])
        s_minus = ZZ(signature_pair[1])
        if s_plus < 0 or s_minus < 0:
            raise ValueError("signature invariants must be nonnegative")
        if not even:
            raise NotImplementedError("odd genus classification is not implemented in this spike")
        if self._quadratic_modulus() != 2:
            raise ValueError("the discriminant form of an even lattice has values modulo 2")
        rank = s_plus + s_minus
        if rank < len(self.invariants()):
            return False
        return ZZ((s_plus - s_minus) - self.brown_invariant()) % 8 == 0

    def genus(self, signature_pair, even=True):
        r"""Return the synthetic genus datum determined by signature and discriminant form."""
        if not self.is_genus(signature_pair, even=even):
            raise ValueError("this discriminant form and signature do not define a genus in this spike")
        return SyntheticGenus(self, signature_pair, even=even)

    def twist(self, scalar):
        return TwistedSyntheticDiscriminantGroup(self, scalar)

    def _old_dual_coordinates(self, element):
        full_coordinates = matrix(ZZ, self.rank(), 1)
        for coordinate, position, multiplier in zip(
            element.coordinates(),
            self._invariant_positions,
            self._coordinate_multipliers,
        ):
            full_coordinates[position, 0] = ZZ(coordinate) * ZZ(multiplier)
        return self._smith_right_inverse_transpose * full_coordinates

    @cached_method
    def _raw_form_matrix(self):
        if self.ngens() == 0:
            return matrix(QQ, 0, 0)
        columns = [self._old_dual_coordinates(self.gen(i)) for i in range(self.ngens())]
        transform = matrix(QQ, self.rank(), self.ngens(), [columns[j][i, 0] for i in range(self.rank()) for j in range(self.ngens())])
        form = transform.transpose() * self.source_lattice().gram_matrix().inverse() * transform
        form.set_immutable()
        return form

    def _subgroup(self, subgroup_or_gens):
        if isinstance(subgroup_or_gens, SyntheticDiscriminantSubgroup):
            if not (subgroup_or_gens.ambient() is self):
                raise ValueError("subgroup belongs to a different discriminant group")
            return subgroup_or_gens
        return self.submodule_with_gens(subgroup_or_gens)

    def _quadratic_modulus(self):
        return ZZ(2) if self.source_lattice().is_even() else ZZ.one()

    def _invariant_basis_candidates(self):
        if self.ngens() == 0:
            return ((),)
        elements = tuple(self.elements())
        candidates_by_generator = tuple(
            tuple(element for element in elements if self.order(element) == invariant)
            for invariant in self.invariants()
        )
        return (
            images
            for images in product(*candidates_by_generator)
            if self._generates_full_group(images)
        )

    def _generates_full_group(self, images):
        zero = tuple(ZZ.zero() for _ in self.invariants())
        generated = set()
        coefficient_ranges = tuple(range(invariant) for invariant in self.invariants())
        for coefficients in product(*coefficient_ranges):
            coordinates = zero
            for coefficient, image in zip(coefficients, images):
                coordinates = tuple(
                    (coordinates[i] + ZZ(coefficient) * image.coordinates()[i]) % self.invariants()[i]
                    for i in range(self.ngens())
                )
            generated.add(coordinates)
        return ZZ(len(generated)) == self.cardinality()

    def _transformed_quadratic_gram(self, images):
        transform = matrix(
            QQ,
            self.ngens(),
            self.ngens(),
            [images[column].coordinates()[row] for row in range(self.ngens()) for column in range(self.ngens())],
        )
        raw = transform.transpose() * self.gram_matrix_quadratic() * transform
        normalized = matrix(QQ, raw.nrows(), raw.ncols())
        for i in range(raw.nrows()):
            for j in range(raw.ncols()):
                modulus = self._quadratic_modulus() if i == j else ZZ.one()
                normalized[i, j] = rational_mod(raw[i, j], modulus)
        return normalized

    def _brute_force_orthogonal_group(self, kind="quadratic"):
        if not (kind in ("quadratic", "bilinear")):
            raise ValueError(f"orthogonal group kind must be quadratic or bilinear; found={kind}")
        if self.ngens() == 0:
            return (SyntheticDiscriminantAction(self, identity_matrix(ZZ, 0)),)
        automorphisms = []
        candidates = tuple(self.elements())
        for images in product(candidates, repeat=self.ngens()):
            action = SyntheticDiscriminantAction.from_images(self, images)
            if action.is_automorphism() and action.preserves_form(kind=kind):
                automorphisms.append(action)
        return tuple(automorphisms)

    @classmethod
    def trivial(cls, source_lattice):
        return cls(source_lattice, 0)


class SyntheticDiscriminantSubgroup:
    r"""Finite subgroup of a synthetic discriminant group."""

    def __init__(self, ambient, gens):
        if not (all(hasattr(ambient, name) for name in ("ngens", "order", "zero", "elements"))):
            raise ValueError(f"expected finite additive parent; found={type(ambient)}")
        self._ambient = ambient
        self._gens = tuple(self._coerce(gen) for gen in gens)
        self._elements = tuple(sorted(self._closure(), key=self._element_key))

    def ambient(self):
        return self._ambient

    def gens(self):
        return self._gens

    def elements(self):
        return self._elements

    def cardinality(self):
        return ZZ(len(self.elements()))

    def __contains__(self, element):
        return self._element_key(element) in self._key()

    def is_bilinear_isotropic(self):
        return all(
            self.ambient().b(left, right) == 0
            for left in self.elements()
            for right in self.elements()
        )

    def is_quadratic_isotropic(self):
        return all(self.ambient().q(element) == 0 for element in self.elements())

    def orthogonal_submodule(self):
        return self.ambient().orthogonal_submodule_to(self)

    def _key(self):
        return frozenset(self._element_key(element) for element in self.elements())

    def __eq__(self, other):
        return isinstance(other, SyntheticDiscriminantSubgroup) and self.ambient() is other.ambient() and self._key() == other._key()

    def __hash__(self):
        return hash((id(self.ambient()), self._key()))

    def _closure(self):
        if not self._gens:
            return {self.ambient().zero()}
        ranges = [range(self.ambient().order(generator)) for generator in self._gens]
        elements = set()
        for coefficients in product(*ranges):
            element = self.ambient().zero()
            for coefficient, generator in zip(coefficients, self._gens):
                element = self._add_elements(element, self._scalar_multiply(ZZ(coefficient), generator))
            elements.add(element)
        return elements

    def _coerce(self, element):
        return self.ambient()(element)

    def _element_key(self, element):
        return tuple(self.ambient().coordinates(self._coerce(element)))

    def _add_elements(self, left, right):
        if hasattr(self.ambient(), "_add_elements"):
            return self.ambient()._add_elements(left, right)
        return left + right

    def _scalar_multiply(self, scalar, element):
        if hasattr(self.ambient(), "_scalar_multiply_element"):
            return self.ambient()._scalar_multiply_element(scalar, element)
        return scalar * element


class SyntheticDiscriminantGroupQuotient(Parent):
    r"""Ordinary finite quotient ``A / H`` of a synthetic discriminant group."""

    Element = SyntheticDiscriminantGroupElement

    def __init__(self, ambient_group, relation_subgroup):
        if not (all(hasattr(ambient_group, name) for name in ("ngens", "invariants", "gens", "order"))):
            raise ValueError(f"expected finite additive parent; found={type(ambient_group)}")
        relation_subgroup = ambient_group._subgroup(relation_subgroup)
        self._ambient_group = ambient_group
        self._relation_subgroup = relation_subgroup
        relation_rows = []
        for i, invariant in enumerate(ambient_group.invariants()):
            row = [ZZ.zero()] * ambient_group.ngens()
            row[i] = ZZ(invariant)
            relation_rows.append(row)
        relation_rows.extend([list(ambient_group.coordinates(generator)) for generator in relation_subgroup.gens()])
        relation_matrix = matrix(ZZ, relation_rows) if relation_rows else matrix(ZZ, 0, 0)
        smith, _smith_left, smith_right = relation_matrix.smith_form()
        self._smith_right = smith_right
        self._smith_right_inverse = smith_right.inverse()
        positions = []
        invariants = []
        for i in range(min(smith.nrows(), smith.ncols())):
            invariant = abs(smith[i, i])
            if invariant != 1:
                positions.append(i)
                invariants.append(ZZ(invariant))
        self._invariant_positions = tuple(positions)
        self._invariants = tuple(invariants)
        Parent.__init__(self, base=ZZ, category=DiscriminantForms(ZZ))

    def _repr_(self):
        return f"Synthetic finite discriminant quotient with invariants {self.invariants()}"

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticDiscriminantGroupQuotient)
            and self.ambient_group() is other.ambient_group()
            and self.relations() == other.relations()
            and self.invariants() == other.invariants()
        )

    def __hash__(self):
        return hash((id(self.ambient_group()), self.relations(), self.invariants()))

    def _element_constructor_(self, coordinates):
        if isinstance(coordinates, SyntheticDiscriminantGroupElement) and coordinates.parent() is self:
            return coordinates
        return self.element_class(self, coordinates)

    def ambient_group(self):
        return self._ambient_group

    def underlying_abelian_group(self):
        return self

    def cover(self):
        return self._ambient_group

    V = cover

    def relations(self):
        return self._relation_subgroup

    W = relations

    def invariants(self):
        return self._invariants

    invariant_factors = invariants

    def elementary_divisors(self):
        divisors = []
        for invariant in self.invariants():
            for prime, exponent in ZZ(invariant).factor():
                divisors.append(ZZ(prime) ** ZZ(exponent))
        return tuple(sorted(divisors))

    def annihilator(self):
        return lcm(self.invariants() or (ZZ.one(),))

    exponent = annihilator

    def is_cyclic(self):
        return len(self.invariants()) <= 1

    def short_name(self):
        if not self.invariants():
            return "0"
        return " + ".join(f"Z/{invariant}" for invariant in self.invariants())

    def generator_orders(self):
        return self.invariants()

    def rank_p(self, p):
        p = ZZ(p)
        if not p.is_prime():
            raise ValueError(f"p-rank requires a prime; found={p}")
        return ZZ(sum(1 for invariant in self.invariants() if ZZ(invariant) % p == 0))

    length_p = rank_p

    def ngens(self):
        return len(self.invariants())

    def cardinality(self):
        if not self.invariants():
            return ZZ.one()
        return ZZ.prod(self.invariants())

    order = cardinality

    def is_finite(self):
        return True

    def gens(self):
        return tuple(self.gen(i) for i in range(self.ngens()))

    def smith_form_gens(self):
        transform = self.smith_to_gens()
        raw = self.gens()
        return tuple(self.discrete_exp(transform.column(j), gens=raw) for j in range(transform.ncols()))

    smith_generators = smith_form_gens

    def gen(self, i):
        row = [ZZ.zero()] * self.ngens()
        row[i] = ZZ.one()
        return self(row)

    def smith_form_gen(self, i):
        return self.smith_form_gens()[i]

    def zero(self):
        return self([ZZ.zero()] * self.ngens())

    identity = zero

    def elements(self):
        if not self.invariants():
            return (self([]),)
        return tuple(self(coordinates) for coordinates in product(*[range(invariant) for invariant in self.invariants()]))

    def list(self):
        return self.elements()

    def random_element(self):
        return choice(self.elements())

    def order(self, element=None):
        if element is None:
            return self.cardinality()
        element = self(element)
        orders = []
        for coordinate, invariant in zip(element.coordinates(), self.invariants()):
            orders.append(ZZ.one() if coordinate == 0 else invariant // ZZ(coordinate).gcd(invariant))
        return lcm(orders) if orders else ZZ.one()

    def coordinates(self, element, gens=None, reduce=True):
        if gens is None:
            return tuple(self(element).coordinates())
        return self.discrete_log(element, gens=gens)

    def discrete_exp(self, coefficients, gens=None):
        coefficients = tuple(coefficients)
        gens = self.gens() if gens is None else tuple(self(gen) for gen in gens)
        if not (len(coefficients) == len(gens)):
            raise ValueError("coefficient vector length must match generator count; "
            f"coefficients={coefficients}, gens={gens}")
        value = self.zero()
        for coefficient, generator in zip(coefficients, gens):
            value += ZZ(coefficient) * generator
        return value

    def discrete_log(self, element, gens=None):
        element = self(element)
        if gens is None:
            return tuple(element.coordinates())
        gens = tuple(self(gen) for gen in gens)
        for coefficients in product(*[range(self.order(generator)) for generator in gens]):
            if self.discrete_exp(coefficients, gens=gens) == element:
                return tuple(ZZ(coefficient) for coefficient in coefficients)
        raise ValueError(f"element is not generated by the supplied generators: {element}")

    def linear_combination_of_smith_form_gens(self, coefficients):
        return self.discrete_exp(coefficients, gens=self.smith_form_gens())

    def gens_to_smith(self):
        return identity_matrix(ZZ, self.ngens())

    def smith_to_gens(self):
        return identity_matrix(ZZ, self.ngens())

    def gens_vector(self, element, reduce=True):
        return vector(ZZ, self.coordinates(element))

    coordinate_vector = gens_vector
    coordinates_in_smith_basis = coordinates
    coordinates_in_generators = coordinates

    def generator_relations(self):
        return matrix.diagonal(ZZ, self.invariants())

    def subgroup_generated_by(self, gens):
        return SyntheticDiscriminantSubgroup(self, gens)

    submodule_with_gens = subgroup_generated_by
    submodule = subgroup_generated_by
    subgroup = subgroup_generated_by
    from_generators = subgroup_generated_by

    def _subgroup(self, subgroup_or_gens):
        if isinstance(subgroup_or_gens, SyntheticDiscriminantSubgroup):
            if not (subgroup_or_gens.ambient() is self):
                raise ValueError("subgroup belongs to a different finite quotient")
            return subgroup_or_gens
        return self.subgroup(subgroup_or_gens)

    def contains_subgroup(self, subgroup_or_gens):
        return self._subgroup(subgroup_or_gens).ambient() is self

    def quotient_group(self, subgroup_or_gens):
        return SyntheticDiscriminantGroupQuotient(self, self._subgroup(subgroup_or_gens))

    quotient = quotient_group

    def quotient_map(self, subgroup_or_gens):
        quotient = self.quotient_group(subgroup_or_gens)
        return lambda element: quotient.projection(element)

    def cosets(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        unseen = set(self.elements())
        cosets = []
        while unseen:
            representative = min(unseen, key=lambda element: tuple(element.coordinates()))
            coset = frozenset(representative + element for element in subgroup.elements())
            cosets.append(coset)
            unseen.difference_update(coset)
        return tuple(cosets)

    def primary_part(self, p):
        p = ZZ(p)
        if not p.is_prime():
            raise ValueError(f"primary part requires a prime; found={p}")
        return self.subgroup(element for element in self.elements() if (p ** ZZ(element.parent().annihilator().valuation(p))) * element == self.zero())

    p_primary_part = primary_part

    def primary_decomposition(self):
        return tuple(self.primary_part(p) for p in ZZ(self.annihilator()).prime_divisors())

    primary_parts = primary_decomposition

    def torsion_subgroup(self):
        return self

    def all_submodules(self):
        return _finite_all_subgroups(self)

    all_subgroups = all_submodules
    subgroups = all_submodules

    def p_torsion(self, p, k=1):
        return _finite_p_torsion(self, p, k=k)

    def relations_among(self, gens):
        return _finite_relations_among(self, gens)

    def basis_from_generators(self, gens):
        return _finite_basis_from_generators(self, gens)

    def automorphism_group(self):
        return SyntheticOrthogonalGroup(self, _all_group_automorphisms(self))

    def projection(self, element):
        element = self.ambient_group()(element)
        ambient_row = matrix(ZZ, 1, self.ambient_group().ngens(), list(self.ambient_group().coordinates(element)))
        smith_row = ambient_row * self._smith_right
        return self([ZZ(smith_row[0, position]) % invariant for position, invariant in zip(self._invariant_positions, self.invariants())])

    def lift(self, element):
        element = self(element)
        smith_row = matrix(ZZ, 1, self.ambient_group().ngens())
        for coordinate, position in zip(element.coordinates(), self._invariant_positions):
            smith_row[0, position] = ZZ(coordinate)
        ambient_coordinates = smith_row * self._smith_right_inverse
        return self.ambient_group()([ZZ(ambient_coordinates[0, i]) for i in range(self.ambient_group().ngens())])


class SyntheticDiscriminantSubquotient:
    r"""Finite subquotient ``K / H`` represented by explicit cosets."""

    def __init__(self, ambient_group, relation_subgroup, cover_subgroup):
        self._ambient_group = ambient_group
        self._relation_subgroup = ambient_group._subgroup(relation_subgroup)
        self._cover_subgroup = ambient_group._subgroup(cover_subgroup)
        if not (self._relation_subgroup._key() <= self._cover_subgroup._key()):
            raise ValueError("relations must lie in the cover subgroup")
        self._cosets = self._compute_cosets()

    def cardinality(self):
        return ZZ(len(self._cosets))

    order = cardinality

    def __call__(self, element):
        if isinstance(element, frozenset):
            return self._coerce_coset(element)
        if hasattr(element, "parent") and element.parent() is self._ambient_group:
            return self._coerce_coset(element)
        if element == 0:
            return self.zero()
        coordinates = tuple(element)
        if len(coordinates) == self.ngens():
            return self.discrete_exp(coordinates)
        return self._coerce_coset(element)

    def underlying_abelian_group(self):
        return self

    def is_finite(self):
        return True

    def invariants(self):
        return _finite_group_invariant_factors(
            self.elements(),
            self.zero(),
            self._scalar_multiply_coset,
        )

    invariant_factors = invariants

    def elementary_divisors(self):
        divisors = []
        for invariant in self.invariants():
            for prime, exponent in ZZ(invariant).factor():
                divisors.append(ZZ(prime) ** ZZ(exponent))
        return tuple(sorted(divisors))

    def is_cyclic(self):
        return len(self.invariants()) <= 1

    def short_name(self):
        if not self.invariants():
            return "0"
        return " + ".join(f"Z/{invariant}" for invariant in self.invariants())

    def rank_p(self, p):
        p = ZZ(p)
        if not p.is_prime():
            raise ValueError(f"p-rank requires a prime; found={p}")
        return ZZ(sum(1 for invariant in self.invariants() if ZZ(invariant) % p == 0))

    length_p = rank_p

    def ngens(self):
        return len(self.gens())

    def cover(self):
        return self._cover_subgroup

    V = cover

    def relations(self):
        return self._relation_subgroup

    W = relations

    def ambient_group(self):
        return self._ambient_group

    def _compute_cosets(self):
        unseen = set(self._cover_subgroup.elements())
        cosets = []
        while unseen:
            representative = min(unseen, key=lambda element: tuple(element.coordinates()))
            coset = frozenset(representative + element for element in self._relation_subgroup.elements())
            cosets.append(coset)
            unseen.difference_update(coset)
        return tuple(sorted(cosets, key=lambda coset: tuple(self._coset_representative(coset).coordinates())))

    def elements(self):
        return self._cosets

    def list(self):
        return self.elements()

    def random_element(self):
        return choice(self.elements())

    def zero(self):
        return self._coset_containing(self._ambient_group.zero())

    identity = zero

    def gens(self):
        generators = []
        generated = {self.zero()}
        for coset in self.elements():
            if coset in generated:
                continue
            generators.append(coset)
            generated = self._closure(generators)
            if len(generated) == self.cardinality():
                break
        return tuple(generators)

    def smith_form_gens(self):
        transform = self.smith_to_gens()
        raw = self.gens()
        return tuple(self.discrete_exp(transform.column(j), gens=raw) for j in range(transform.ncols()))

    smith_generators = smith_form_gens

    def gen(self, i):
        return self.gens()[i]

    def smith_form_gen(self, i):
        return self.smith_form_gens()[i]

    def generator_orders(self):
        return tuple(self.order(generator) for generator in self.gens())

    def annihilator(self):
        return lcm(self.generator_orders() or (ZZ.one(),))

    exponent = annihilator

    def order(self, element=None):
        if element is None:
            return self.cardinality()
        element = self._coerce_coset(element)
        value = self.zero()
        for order in range(1, self.cardinality() + 1):
            value = self._add_cosets(value, element)
            if value == self.zero():
                return ZZ(order)
        raise ArithmeticError(f"finite subquotient element has no finite order: {element}")

    def discrete_exp(self, coefficients, gens=None):
        coefficients = tuple(coefficients)
        gens = self.gens() if gens is None else tuple(self._coerce_coset(gen) for gen in gens)
        if not (len(coefficients) == len(gens)):
            raise ValueError("coefficient vector length must match generator count; "
            f"coefficients={coefficients}, gens={gens}")
        value = self.zero()
        for coefficient, generator in zip(coefficients, gens):
            value = self._add_cosets(value, self._scalar_multiply_coset(ZZ(coefficient), generator))
        return value

    def discrete_log(self, element, gens=None):
        element = self._coerce_coset(element)
        gens = self.gens() if gens is None else tuple(self._coerce_coset(gen) for gen in gens)
        ranges = tuple(range(self.order(generator)) for generator in gens)
        for coefficients in product(*ranges):
            if self.discrete_exp(coefficients, gens=gens) == element:
                return tuple(ZZ(coefficient) for coefficient in coefficients)
        raise ValueError(f"element is not generated by the supplied generators: {element}")

    def coordinates(self, element, gens=None, reduce=True):
        return self.discrete_log(element, gens=gens)

    def linear_combination_of_smith_form_gens(self, coefficients):
        return self.discrete_exp(coefficients, gens=self.smith_form_gens())

    def gens_to_smith(self):
        return identity_matrix(ZZ, self.ngens())

    def smith_to_gens(self):
        return identity_matrix(ZZ, self.ngens())

    def gens_vector(self, element, reduce=True):
        return vector(ZZ, self.coordinates(element))

    coordinate_vector = gens_vector
    coordinates_in_smith_basis = coordinates
    coordinates_in_generators = coordinates

    def generator_relations(self):
        return matrix.diagonal(ZZ, self.invariants())

    def subgroup_generated_by(self, gens):
        return SyntheticDiscriminantSubgroup(self, gens)

    submodule_with_gens = subgroup_generated_by
    submodule = subgroup_generated_by
    subgroup = subgroup_generated_by
    from_generators = subgroup_generated_by

    def _subgroup(self, subgroup_or_gens):
        if isinstance(subgroup_or_gens, SyntheticDiscriminantSubgroup):
            if not (subgroup_or_gens.ambient() is self):
                raise ValueError("subgroup belongs to a different finite subquotient")
            return subgroup_or_gens
        return self.subgroup(subgroup_or_gens)

    def contains_subgroup(self, subgroup_or_gens):
        return self._subgroup(subgroup_or_gens).ambient() is self

    def quotient_group(self, subgroup_or_gens):
        return SyntheticDiscriminantGroupQuotient(self, self._subgroup(subgroup_or_gens))

    quotient = quotient_group

    def cosets(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        unseen = set(self.elements())
        cosets = []
        while unseen:
            representative = min(unseen, key=lambda coset: self.coordinates(coset))
            coset = frozenset(self._add_cosets(representative, element) for element in subgroup.elements())
            cosets.append(coset)
            unseen.difference_update(coset)
        return tuple(cosets)

    def primary_part(self, p):
        p = ZZ(p)
        if not p.is_prime():
            raise ValueError(f"primary part requires a prime; found={p}")
        exponent = ZZ(self.annihilator()).valuation(p)
        return self.subgroup(element for element in self.elements() if self._scalar_multiply_coset(p ** exponent, element) == self.zero())

    p_primary_part = primary_part

    def primary_decomposition(self):
        return tuple(self.primary_part(p) for p in ZZ(self.annihilator()).prime_divisors())

    primary_parts = primary_decomposition

    def torsion_subgroup(self):
        return self

    def all_submodules(self):
        return _finite_all_subgroups(self)

    all_subgroups = all_submodules
    subgroups = all_submodules

    def p_torsion(self, p, k=1):
        return _finite_p_torsion(self, p, k=k)

    def relations_among(self, gens):
        return _finite_relations_among(self, gens)

    def basis_from_generators(self, gens):
        return _finite_basis_from_generators(self, gens)

    def automorphism_group(self):
        return SyntheticOrthogonalGroup(self, _all_group_automorphisms(self))

    def projection(self, element):
        element = self._ambient_group(element)
        return self._coset_containing(element)

    def quotient_map(self, subgroup_or_gens=None):
        if subgroup_or_gens is None:
            return self.projection
        quotient = self.quotient_group(subgroup_or_gens)
        return lambda element: quotient.projection(element)

    def lift(self, element):
        return self._coset_representative(self._coerce_coset(element))

    def gram_matrix_bilinear(self):
        return matrix(QQ, [[self.b(left, right) for right in self.gens()] for left in self.gens()])

    def gram_matrix_quadratic(self):
        return matrix(QQ, [[self.q(left) if i == j else self.b(left, right) for j, right in enumerate(self.gens())] for i, left in enumerate(self.gens())])

    def b(self, left, right):
        return self._ambient_group.b(self.lift(left), self.lift(right))

    inner_product = b

    def q(self, element):
        return self._ambient_group.q(self.lift(element))

    quadratic_product = q

    def value_module(self):
        return self._ambient_group.value_module()

    def value_module_qf(self):
        return self._ambient_group.value_module_qf()

    def _coerce_coset(self, element):
        if isinstance(element, frozenset):
            for coset in self._cosets:
                if element == coset:
                    return coset
            raise ValueError(f"coset is not an element of this subquotient: {element}")
        return self._coset_containing(element)

    def _coset_representative(self, coset):
        return min(coset, key=lambda element: tuple(element.coordinates()))

    def _coset_containing(self, element):
        element = self._ambient_group(element)
        for coset in self._cosets:
            if element in coset:
                return coset
        raise ValueError(f"element is outside the subquotient cover subgroup: {element}")

    def _closure(self, gens):
        if not gens:
            return {self.zero()}
        ranges = tuple(range(self.order(generator)) for generator in gens)
        return {self.discrete_exp(coefficients, gens=gens) for coefficients in product(*ranges)}

    def _add_cosets(self, left, right):
        left = self._coerce_coset(left)
        right = self._coerce_coset(right)
        return self._coset_containing(self._coset_representative(left) + self._coset_representative(right))

    def _scalar_multiply_coset(self, scalar, coset):
        scalar = ZZ(scalar)
        coset = self._coerce_coset(coset)
        scalar = scalar % self.order(coset)
        value = self.zero()
        for _ in range(scalar):
            value = self._add_cosets(value, coset)
        return value

    def _add_elements(self, left, right):
        return self._add_cosets(left, right)

    def _scalar_multiply_element(self, scalar, element):
        return self._scalar_multiply_coset(scalar, element)


class SyntheticLatticeFiniteQuotient(Parent):
    r"""Finite quotient ``cover / relations`` of same-rank synthetic ``ZZ``-lattices."""

    Element = SyntheticDiscriminantGroupElement

    def __init__(self, cover_lattice, relation_lattice):
        if not (isinstance(cover_lattice, SyntheticLattice)):
            raise TypeError(f"expected SyntheticLattice cover; found={type(cover_lattice)}")
        if not (isinstance(relation_lattice, SyntheticLattice)):
            raise TypeError(f"expected SyntheticLattice relation lattice; found={type(relation_lattice)}")
        if not (cover_lattice.base_ring() is ZZ):
            raise ValueError("finite lattice quotient cover must be a ZZ-lattice")
        if not (relation_lattice.base_ring() is ZZ):
            raise ValueError("finite lattice quotient relations must be a ZZ-lattice")
        if not (relation_lattice.is_submodule(cover_lattice)):
            raise ValueError("relations must be a sublattice of the cover")
        if not (relation_lattice.rank() == cover_lattice.rank()):
            raise ValueError("finite quotients require same-rank lattices")
        self._cover_lattice = cover_lattice
        self._relation_lattice = relation_lattice
        inclusion = matrix(
            ZZ,
            [
                cover_lattice.underlying_module().coordinate_vector(vector(QQ, row))
                for row in relation_lattice._basis_matrix.rows()
            ],
        )
        if cover_lattice.rank() == 0:
            inclusion = matrix(ZZ, 0, 0)
        smith, _smith_left, smith_right = inclusion.smith_form()
        self._smith_right = smith_right
        self._smith_right_inverse = smith_right.inverse()
        positions = []
        invariants = []
        for i in range(smith.nrows()):
            invariant = abs(smith[i, i])
            if invariant != 1:
                positions.append(i)
                invariants.append(ZZ(invariant))
        self._invariant_positions = tuple(positions)
        self._invariants = tuple(invariants)
        Parent.__init__(self, base=ZZ, category=DiscriminantForms(ZZ))

    def _repr_(self):
        return f"Synthetic finite lattice quotient with invariants {self.invariants()}"

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticLatticeFiniteQuotient)
            and self.cover_lattice() == other.cover_lattice()
            and self.relation_lattice() == other.relation_lattice()
            and self.invariants() == other.invariants()
        )

    def __hash__(self):
        return hash((_lattice_key(self.cover_lattice()), _lattice_key(self.relation_lattice()), self.invariants()))

    def _element_constructor_(self, coordinates):
        if isinstance(coordinates, SyntheticDiscriminantGroupElement) and coordinates.parent() is self:
            return coordinates
        return self.element_class(self, coordinates)

    def cover_lattice(self):
        return self._cover_lattice

    cover = cover_lattice
    V = cover_lattice

    def relation_lattice(self):
        return self._relation_lattice

    relations = relation_lattice
    W = relation_lattice

    def underlying_abelian_group(self):
        return self

    def invariants(self):
        return self._invariants

    invariant_factors = invariants

    def elementary_divisors(self):
        divisors = []
        for invariant in self.invariants():
            for prime, exponent in ZZ(invariant).factor():
                divisors.append(ZZ(prime) ** ZZ(exponent))
        return tuple(sorted(divisors))

    def ngens(self):
        return len(self.invariants())

    def cardinality(self):
        if not self.invariants():
            return ZZ.one()
        return ZZ.prod(self.invariants())

    def is_finite(self):
        return True

    def is_cyclic(self):
        return len(self.invariants()) <= 1

    def short_name(self):
        if not self.invariants():
            return "0"
        return " + ".join(f"Z/{invariant}" for invariant in self.invariants())

    def generator_orders(self):
        return self.invariants()

    def rank_p(self, p):
        p = ZZ(p)
        if not p.is_prime():
            raise ValueError(f"p-rank requires a prime; found={p}")
        return ZZ(sum(1 for invariant in self.invariants() if ZZ(invariant) % p == 0))

    length_p = rank_p

    def annihilator(self):
        if not self.invariants():
            return ZZ.one()
        return lcm(self.invariants())

    exponent = annihilator

    def gens(self):
        return tuple(self.gen(i) for i in range(self.ngens()))

    def smith_form_gens(self):
        transform = self.smith_to_gens()
        raw = self.gens()
        return tuple(self.discrete_exp(transform.column(j), gens=raw) for j in range(transform.ncols()))

    smith_generators = smith_form_gens

    def gen(self, i):
        row = [ZZ.zero()] * self.ngens()
        row[i] = ZZ.one()
        return self(row)

    def smith_form_gen(self, i):
        return self.smith_form_gens()[i]

    def zero(self):
        return self([ZZ.zero()] * self.ngens())

    identity = zero

    def elements(self):
        if not self.invariants():
            return (self([]),)
        return tuple(self(coordinates) for coordinates in product(*[range(invariant) for invariant in self.invariants()]))

    def list(self):
        return self.elements()

    def random_element(self):
        return choice(self.elements())

    def order(self, element=None):
        if element is None:
            return self.cardinality()
        element = self(element) if element.parent() is not self else element
        orders = []
        for coordinate, invariant in zip(element.coordinates(), self.invariants()):
            orders.append(ZZ.one() if coordinate == 0 else invariant // ZZ(coordinate).gcd(invariant))
        return lcm(orders) if orders else ZZ.one()

    def coordinates(self, element, gens=None, reduce=True):
        if gens is None:
            return tuple(self(element).coordinates())
        return self.discrete_log(element, gens=gens)

    def discrete_exp(self, coefficients, gens=None):
        coefficients = tuple(coefficients)
        gens = self.gens() if gens is None else tuple(self(gen) for gen in gens)
        if not (len(coefficients) == len(gens)):
            raise ValueError("coefficient vector length must match generator count; "
            f"coefficients={coefficients}, gens={gens}")
        value = self.zero()
        for coefficient, generator in zip(coefficients, gens):
            value += ZZ(coefficient) * generator
        return value

    def discrete_log(self, element, gens=None):
        element = self(element)
        if gens is None:
            return tuple(element.coordinates())
        gens = tuple(self(gen) for gen in gens)
        for coefficients in product(*[range(self.order(generator)) for generator in gens]):
            if self.discrete_exp(coefficients, gens=gens) == element:
                return tuple(ZZ(coefficient) for coefficient in coefficients)
        raise ValueError(f"element is not generated by the supplied generators: {element}")

    def subgroup_generated_by(self, gens):
        return SyntheticDiscriminantSubgroup(self, gens)

    submodule_with_gens = subgroup_generated_by
    submodule = subgroup_generated_by
    subgroup = subgroup_generated_by
    from_generators = subgroup_generated_by

    def _subgroup(self, subgroup_or_gens):
        if isinstance(subgroup_or_gens, SyntheticDiscriminantSubgroup):
            if not (subgroup_or_gens.ambient() is self):
                raise ValueError("subgroup belongs to a different finite lattice quotient")
            return subgroup_or_gens
        return self.subgroup(subgroup_or_gens)

    def contains_subgroup(self, subgroup_or_gens):
        return self._subgroup(subgroup_or_gens).ambient() is self

    def quotient_group(self, subgroup_or_gens):
        return SyntheticDiscriminantGroupQuotient(self, self._subgroup(subgroup_or_gens))

    quotient = quotient_group

    def cosets(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        unseen = set(self.elements())
        cosets = []
        while unseen:
            representative = min(unseen, key=lambda element: tuple(element.coordinates()))
            coset = frozenset(representative + element for element in subgroup.elements())
            cosets.append(coset)
            unseen.difference_update(coset)
        return tuple(cosets)

    def primary_part(self, p):
        p = ZZ(p)
        if not p.is_prime():
            raise ValueError(f"primary part requires a prime; found={p}")
        exponent = ZZ(self.annihilator()).valuation(p)
        return self.subgroup(element for element in self.elements() if (p ** exponent) * element == self.zero())

    p_primary_part = primary_part

    def primary_decomposition(self):
        return tuple(self.primary_part(p) for p in ZZ(self.annihilator()).prime_divisors())

    primary_parts = primary_decomposition

    def torsion_subgroup(self):
        return self

    def all_submodules(self):
        return _finite_all_subgroups(self)

    all_subgroups = all_submodules
    subgroups = all_submodules

    def p_torsion(self, p, k=1):
        return _finite_p_torsion(self, p, k=k)

    def relations_among(self, gens):
        return _finite_relations_among(self, gens)

    def basis_from_generators(self, gens):
        return _finite_basis_from_generators(self, gens)

    def linear_combination_of_smith_form_gens(self, coefficients):
        return self.discrete_exp(coefficients, gens=self.smith_form_gens())

    def gens_to_smith(self):
        return identity_matrix(ZZ, self.ngens())

    def smith_to_gens(self):
        return identity_matrix(ZZ, self.ngens())

    def gens_vector(self, element, reduce=True):
        return vector(ZZ, self.coordinates(element))

    coordinate_vector = gens_vector
    coordinates_in_smith_basis = coordinates
    coordinates_in_generators = coordinates

    def generator_relations(self):
        return matrix.diagonal(ZZ, self.invariants())

    def automorphism_group(self):
        return SyntheticOrthogonalGroup(self, _all_group_automorphisms(self))

    def lift(self, element):
        element = self(element)
        smith_row = matrix(ZZ, 1, self.cover_lattice().rank())
        for coordinate, position in zip(element.coordinates(), self._invariant_positions):
            smith_row[0, position] = ZZ(coordinate)
        cover_coordinates = smith_row * self._smith_right_inverse
        return self.cover_lattice()([ZZ(cover_coordinates[0, i]) for i in range(self.cover_lattice().rank())])

    coset_representative = lift

    def projection(self, element):
        cover = self.cover_lattice()
        if isinstance(element, SyntheticLatticeElement):
            if not (element.parent() == cover):
                raise ValueError("projection expects an element of the quotient cover; "
                f"expected={cover}, found={element.parent()}")
        else:
            element = cover(element)
        cover_row = matrix(ZZ, 1, cover.rank(), list(element.coordinates()))
        smith_row = cover_row * self._smith_right
        return self([ZZ(smith_row[0, position]) % invariant for position, invariant in zip(self._invariant_positions, self.invariants())])

    def quotient_map(self, subgroup_or_gens=None):
        if subgroup_or_gens is None:
            return self.projection
        quotient = self.quotient_group(subgroup_or_gens)
        return lambda element: quotient.projection(element)

    def preimage_lattice(self, subgroup_or_gens, label="preimage_lattice"):
        subgroup = self._subgroup(subgroup_or_gens)
        lift_rows = [self.lift(generator).rational_coordinates() for generator in subgroup.gens()]
        if not lift_rows:
            return self.relation_lattice()
        return self.relation_lattice().overlattice(lift_rows, check_integral=False, label=label)

    def hom(self, images):
        return SyntheticDiscriminantAction.from_images(self, images)


class SyntheticDiscriminantAction:
    r"""Endomorphism of a synthetic discriminant group in invariant coordinates."""

    def __init__(self, discriminant_group, matrix_data):
        if not (hasattr(discriminant_group, "ngens") and hasattr(discriminant_group, "invariants")):
            raise ValueError(f"expected finite discriminant parent; found={type(discriminant_group)}")
        matrix_data = matrix(ZZ, matrix_data)
        if not (matrix_data.nrows() == discriminant_group.ngens()):
            raise ValueError("action matrix rows must match invariant count; "
            f"rows={matrix_data.nrows()}, invariants={discriminant_group.invariants()}")
        if not (matrix_data.ncols() == discriminant_group.ngens()):
            raise ValueError("action matrix columns must match invariant count; "
            f"columns={matrix_data.ncols()}, invariants={discriminant_group.invariants()}")
        reduced = matrix(ZZ, matrix_data.nrows(), matrix_data.ncols())
        for i, invariant in enumerate(discriminant_group.invariants()):
            for j in range(matrix_data.ncols()):
                reduced[i, j] = matrix_data[i, j] % invariant
        reduced.set_immutable()
        self._discriminant_group = discriminant_group
        self._matrix = reduced

    @classmethod
    def from_images(cls, discriminant_group, images):
        columns = []
        for image in images:
            columns.extend(_finite_coordinates(discriminant_group, image))
        return cls(discriminant_group, matrix(ZZ, discriminant_group.ngens(), discriminant_group.ngens(), columns).transpose())

    def discriminant_group(self):
        return self._discriminant_group

    def matrix(self):
        return self._matrix

    def __call__(self, element):
        group = self.discriminant_group()
        column = self.matrix() * matrix(ZZ, group.ngens(), 1, _finite_coordinates(group, element))
        return group([column[i, 0] for i in range(group.ngens())])

    def is_identity(self):
        return all(self(element) == element for element in self.discriminant_group().elements())

    def is_automorphism(self):
        group = self.discriminant_group()
        images = {_finite_coordinates(group, self(element)) for element in group.elements()}
        return len(images) == group.cardinality()

    def kernel(self):
        group = self.discriminant_group()
        return SyntheticDiscriminantSubgroup(group, (element for element in group.elements() if self(element) == group.zero()))

    def inverse_image(self, subgroup_or_gens):
        group = self.discriminant_group()
        subgroup = group._subgroup(subgroup_or_gens)
        return SyntheticDiscriminantSubgroup(group, (element for element in group.elements() if self(element) in subgroup))

    def image(self):
        group = self.discriminant_group()
        return SyntheticDiscriminantSubgroup(group, (self(generator) for generator in group.gens()))

    def im_gens(self):
        return self.image().gens()

    def lift(self, element):
        group = self.discriminant_group()
        element = group(element)
        preimages = tuple(candidate for candidate in group.elements() if self(candidate) == element)
        if not preimages:
            raise ValueError(f"element is not in the image of this finite homomorphism: {element}")
        return min(preimages, key=lambda candidate: _finite_coordinates(group, candidate))

    def inverse(self):
        if not (self.is_automorphism()):
            raise ValueError(f"only automorphisms have inverses; matrix={self.matrix()}")
        inverse_images = []
        for generator in self.discriminant_group().gens():
            preimages = tuple(
                element
                for element in self.discriminant_group().elements()
                if self(element) == generator
            )
            if not (len(preimages) == 1):
                raise ValueError("automorphism inverse must have a unique preimage for each generator; "
                f"generator={generator}, preimages={preimages}")
            inverse_images.append(preimages[0])
        return SyntheticDiscriminantAction.from_images(self.discriminant_group(), inverse_images)

    def preserves_bilinear_form(self):
        group = self.discriminant_group()
        return all(
            group.b(self(left), self(right)) == group.b(left, right)
            for left in group.elements()
            for right in group.elements()
        )

    def preserves_quadratic_form(self):
        group = self.discriminant_group()
        return all(group.q(self(element)) == group.q(element) for element in group.elements())

    def preserves_form(self, kind="quadratic"):
        if not (kind in ("quadratic", "bilinear")):
            raise ValueError(f"form kind must be quadratic or bilinear; found={kind}")
        if kind == "bilinear":
            return self.preserves_bilinear_form()
        return self.preserves_bilinear_form() and self.preserves_quadratic_form()

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticDiscriminantAction)
            and self.discriminant_group() is other.discriminant_group()
            and self.matrix() == other.matrix()
        )

    def __hash__(self):
        return hash((id(self.discriminant_group()), self.matrix()))


class SyntheticOrthogonalGroup:
    r"""Finite group wrapper for owned discriminant-form automorphisms."""

    def __init__(self, discriminant_group, actions, close=False):
        self._discriminant_group = discriminant_group
        self._generators = tuple(actions)
        self._actions = self._closure(self._generators) if close else self._generators

    def discriminant_group(self):
        return self._discriminant_group

    def gens(self):
        return self._generators

    def order(self):
        return ZZ(len(self._actions))

    def __iter__(self):
        return iter(self._actions)

    def __len__(self):
        return len(self._actions)

    def __getitem__(self, index):
        return self._generators[index]

    def __call__(self, action):
        action = action if isinstance(action, SyntheticDiscriminantAction) else SyntheticDiscriminantAction(self.discriminant_group(), action)
        if not (any(action == group_action for group_action in self._actions)):
            raise ValueError(f"action is not in this orthogonal group: {action.matrix()}")
        return action.matrix()

    def _closure(self, generators):
        identity = SyntheticDiscriminantAction(self.discriminant_group(), identity_matrix(ZZ, self.discriminant_group().ngens()))
        seen = {identity}
        frontier = [identity]
        generators = tuple(generators)
        while frontier:
            current = frontier.pop()
            for generator in generators:
                product_action = SyntheticDiscriminantAction(self.discriminant_group(), generator.matrix() * current.matrix())
                if product_action not in seen:
                    seen.add(product_action)
                    frontier.append(product_action)
        return tuple(sorted(seen, key=lambda action: tuple(action.matrix().list())))


class SyntheticFiniteQuadraticForm(Parent):
    r"""Owned finite quadratic form presented by a generator Gram matrix."""

    Element = SyntheticDiscriminantGroupElement

    def __init__(self, gram_matrix):
        raw_gram = matrix(QQ, gram_matrix)
        if not (raw_gram.is_square()):
            raise ValueError(f"finite quadratic form Gram matrix must be square; found={raw_gram}")
        if not (raw_gram == raw_gram.transpose()):
            raise ValueError(f"finite quadratic form Gram matrix must be symmetric; found={raw_gram}")
        invariants = []
        active_indices = []
        for i in range(raw_gram.nrows()):
            denominators = [raw_gram[i, j].denominator() for j in range(raw_gram.ncols())]
            denominators.extend(raw_gram[j, i].denominator() for j in range(raw_gram.nrows()))
            invariant = ZZ(lcm(denominators))
            if invariant != 1:
                active_indices.append(i)
                invariants.append(invariant)
        gram = raw_gram.matrix_from_rows_and_columns(active_indices, active_indices) if active_indices else matrix(QQ, 0, 0)
        gram.set_immutable()
        self._gram_matrix = gram
        self._invariants = tuple(invariants)
        Parent.__init__(self, base=ZZ, category=DiscriminantForms(ZZ).Quadratic())

    def _repr_(self):
        return f"Synthetic finite quadratic form with invariants {self.invariants()}"

    def _element_constructor_(self, coordinates):
        if isinstance(coordinates, SyntheticDiscriminantGroupElement) and coordinates.parent() is self:
            return coordinates
        return self.element_class(self, coordinates)

    def invariants(self):
        return self._invariants

    invariant_factors = invariants

    def ngens(self):
        return len(self.invariants())

    def cardinality(self):
        if not self.invariants():
            return ZZ.one()
        return ZZ.prod(self.invariants())

    def is_finite(self):
        return True

    def underlying_abelian_group(self):
        return self

    def cover(self):
        return self

    V = cover

    def relations(self):
        return self.subgroup(())

    W = relations

    def annihilator(self):
        if not self.invariants():
            return ZZ.one()
        return lcm(self.invariants())

    exponent = annihilator

    def is_cyclic(self):
        return len(self.invariants()) <= 1

    def short_name(self):
        if not self.invariants():
            return "0"
        return " + ".join(f"Z/{invariant}" for invariant in self.invariants())

    def generator_orders(self):
        return self.invariants()

    def elementary_divisors(self):
        divisors = []
        for invariant in self.invariants():
            for prime, exponent in ZZ(invariant).factor():
                divisors.append(ZZ(prime) ** ZZ(exponent))
        return tuple(sorted(divisors))

    def rank_p(self, p):
        p = ZZ(p)
        if not (p.is_prime()):
            raise ValueError(f"p-rank requires a prime; found={p}")
        return ZZ(sum(1 for invariant in self.invariants() if ZZ(invariant) % p == 0))

    length_p = rank_p

    def value_module(self):
        return value_module(ZZ, ZZ.one())

    def value_module_qf(self):
        return value_module(ZZ, 2 * ZZ.one())

    def gens(self):
        return tuple(self.gen(i) for i in range(self.ngens()))

    def smith_form_gens(self):
        transform = self.smith_to_gens()
        raw = self.gens()
        return tuple(self.discrete_exp(transform.column(j), gens=raw) for j in range(transform.ncols()))

    smith_generators = smith_form_gens

    def gen(self, i):
        row = [ZZ.zero()] * self.ngens()
        row[i] = ZZ.one()
        return self(row)

    def smith_form_gen(self, i):
        return self.smith_form_gens()[i]

    def zero(self):
        return self([ZZ.zero()] * self.ngens())

    identity = zero

    def elements(self):
        if not self.invariants():
            return (self([]),)
        return tuple(self(coordinates) for coordinates in product(*[range(invariant) for invariant in self.invariants()]))

    def list(self):
        return self.elements()

    def random_element(self):
        return choice(self.elements())

    def order(self, element=None):
        if element is None:
            return self.cardinality()
        element = self(element) if element.parent() is not self else element
        orders = []
        for coordinate, invariant in zip(element.coordinates(), self.invariants()):
            orders.append(ZZ.one() if coordinate == 0 else invariant // ZZ(coordinate).gcd(invariant))
        return lcm(orders) if orders else ZZ.one()

    def coordinates(self, element, gens=None, reduce=True):
        if gens is None:
            return tuple(self(element).coordinates())
        return self.discrete_log(element, gens=gens)

    def discrete_exp(self, coefficients, gens=None):
        coefficients = tuple(coefficients)
        gens = self.gens() if gens is None else tuple(self(gen) for gen in gens)
        if not (len(coefficients) == len(gens)):
            raise ValueError("coefficient vector length must match generator count; "
            f"coefficients={coefficients}, gens={gens}")
        value = self.zero()
        for coefficient, generator in zip(coefficients, gens):
            value += ZZ(coefficient) * generator
        return value

    def discrete_log(self, element, gens=None):
        element = self(element)
        if gens is None:
            return tuple(element.coordinates())
        gens = tuple(self(gen) for gen in gens)
        for coefficients in product(*[range(self.order(generator)) for generator in gens]):
            if self.discrete_exp(coefficients, gens=gens) == element:
                return tuple(ZZ(coefficient) for coefficient in coefficients)
        raise ValueError(f"element is not generated by the supplied generators: {element}")

    def linear_combination_of_smith_form_gens(self, coefficients):
        return self.discrete_exp(coefficients, gens=self.smith_form_gens())

    def gens_to_smith(self):
        return identity_matrix(ZZ, self.ngens())

    def smith_to_gens(self):
        return identity_matrix(ZZ, self.ngens())

    def gens_vector(self, element, reduce=True):
        return vector(ZZ, self.coordinates(element))

    coordinate_vector = gens_vector
    coordinates_in_smith_basis = coordinates
    coordinates_in_generators = coordinates

    def generator_relations(self):
        return matrix.diagonal(ZZ, self.invariants())

    def lift(self, element):
        return self(element)

    def projection(self, element):
        return self(element)

    def subgroup_generated_by(self, gens):
        return SyntheticDiscriminantSubgroup(self, gens)

    submodule_with_gens = subgroup_generated_by
    submodule = subgroup_generated_by
    subgroup = subgroup_generated_by
    from_generators = subgroup_generated_by

    def torsion_subgroup(self):
        return self

    def contains_subgroup(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return subgroup.ambient() is self

    def _subgroup(self, subgroup_or_gens):
        if isinstance(subgroup_or_gens, SyntheticDiscriminantSubgroup):
            if not (subgroup_or_gens.ambient() is self):
                raise ValueError("subgroup belongs to a different finite quadratic form")
            return subgroup_or_gens
        return self.subgroup(subgroup_or_gens)

    def all_submodules(self):
        seen = {}
        zero = self.subgroup(())
        seen[zero._key()] = zero
        frontier = [zero]
        while frontier:
            subgroup = frontier.pop()
            for element in self.elements():
                generated = self.subgroup(tuple(subgroup.gens()) + (element,))
                key = generated._key()
                if key not in seen:
                    seen[key] = generated
                    frontier.append(generated)
        return tuple(seen[key] for key in sorted(seen, key=lambda item: sorted(item)))

    all_subgroups = all_submodules
    subgroups = all_submodules

    def primary_part(self, p):
        p = ZZ(p)
        if not (p.is_prime()):
            raise ValueError(f"primary part requires a prime; found={p}")
        images = []
        for invariant, generator in zip(self.invariants(), self.gens()):
            valuation = ZZ(invariant).valuation(p)
            if valuation:
                images.append((ZZ(invariant) // (p ** valuation)) * generator)
        if not images:
            return SyntheticFiniteQuadraticForm(matrix(QQ, 0, 0))
        return SyntheticFiniteQuadraticForm(_form_matrix_on_images(self, images))

    p_primary_part = primary_part

    def primary_decomposition(self):
        return tuple(self.primary_part(p) for p in ZZ(self.annihilator()).prime_divisors())

    primary_parts = primary_decomposition

    def p_torsion(self, p, k=1):
        return _finite_p_torsion(self, p, k=k)

    def relations_among(self, gens):
        return _finite_relations_among(self, gens)

    def basis_from_generators(self, gens):
        return _finite_basis_from_generators(self, gens)

    def orthogonal_submodule_to(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return self.subgroup(
            element
            for element in self.elements()
            if all(self.b(element, subgroup_element) == 0 for subgroup_element in subgroup.elements())
        )

    def orthogonal(self, subgroup_or_gens):
        return self.orthogonal_submodule_to(subgroup_or_gens)

    orthogonal_complement = orthogonal

    def is_isotropic_element(self, element):
        return self.q(element) == 0

    def isotropic_elements(self):
        return tuple(element for element in self.elements() if self.is_isotropic_element(element))

    def is_isotropic_subgroup(self, subgroup_or_gens):
        return self._subgroup(subgroup_or_gens).is_quadratic_isotropic()

    is_totally_isotropic = is_isotropic_subgroup

    def isotropic_subgroups(self):
        return tuple(subgroup for subgroup in self.all_subgroups() if self.is_isotropic_subgroup(subgroup))

    isotropic_submodules = isotropic_subgroups

    def is_lagrangian(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return self.is_isotropic_subgroup(subgroup) and subgroup.cardinality() ** 2 == self.cardinality()

    def lagrangian_subgroups(self):
        return tuple(subgroup for subgroup in self.isotropic_subgroups() if self.is_lagrangian(subgroup))

    metabolizers = lagrangian_subgroups

    def is_metabolic(self):
        return bool(self.lagrangian_subgroups())

    def is_anisotropic(self):
        return all(element == self.zero() for element in self.isotropic_elements())

    def is_maximal_isotropic(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        if not self.is_isotropic_subgroup(subgroup):
            return False
        return all(
            not (subgroup._key() < candidate._key())
            for candidate in self.isotropic_subgroups()
        )

    def maximal_isotropic_subgroups(self):
        return tuple(subgroup for subgroup in self.isotropic_subgroups() if self.is_maximal_isotropic(subgroup))

    def quotient_group(self, subgroup_or_gens):
        return SyntheticDiscriminantGroupQuotient(self, self._subgroup(subgroup_or_gens))

    quotient = quotient_group

    def quotient_map(self, subgroup_or_gens):
        quotient = self.quotient_group(subgroup_or_gens)
        return lambda element: quotient.projection(element)

    def cosets(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        unseen = set(self.elements())
        cosets = []
        while unseen:
            representative = min(unseen, key=lambda element: tuple(element.coordinates()))
            coset = frozenset(representative + element for element in subgroup.elements())
            cosets.append(coset)
            unseen.difference_update(coset)
        return tuple(cosets)

    def restricted_form(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return _form_matrix_on_images(self, subgroup.gens())

    def orthogonal_quotient(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        if not self.is_isotropic_subgroup(subgroup):
            raise ValueError("orthogonal quotient requires a quadratic-isotropic relation subgroup")
        return SyntheticDiscriminantSubquotient(self, subgroup, self.orthogonal(subgroup))

    def subquotient_form(self, subgroup_or_gens, quotient_subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        quotient_subgroup = self._subgroup(quotient_subgroup_or_gens)
        if not subgroup._key() <= quotient_subgroup._key():
            raise ValueError("subquotient form requires H contained in K")
        if not self.is_isotropic_subgroup(subgroup):
            raise ValueError("subquotient form requires a quadratic-isotropic relation subgroup")
        if not quotient_subgroup._key() <= self.orthogonal(subgroup)._key():
            raise ValueError("subquotient form requires K contained in the orthogonal complement of H")
        return SyntheticDiscriminantSubquotient(self, subgroup, quotient_subgroup)

    def _quadratic_modulus(self):
        return ZZ(2)

    def gram_matrix_quadratic(self):
        return self._gram_matrix

    def gram_matrix_bilinear(self):
        form = matrix(QQ, self._gram_matrix.nrows(), self._gram_matrix.ncols())
        for i in range(self._gram_matrix.nrows()):
            for j in range(self._gram_matrix.ncols()):
                form[i, j] = rational_mod(self._gram_matrix[i, j], 1)
        form.set_immutable()
        return form

    def b(self, left, right):
        left = self(left) if left.parent() is not self else left
        right = self(right) if right.parent() is not self else right
        row = matrix(QQ, 1, self.ngens(), list(left.coordinates()))
        col = matrix(QQ, self.ngens(), 1, list(right.coordinates()))
        return rational_mod((row * self.gram_matrix_bilinear() * col)[0, 0], 1)

    inner_product = b

    def q(self, element):
        element = self(element) if element.parent() is not self else element
        row = matrix(QQ, 1, self.ngens(), list(element.coordinates()))
        col = matrix(QQ, self.ngens(), 1, list(element.coordinates()))
        return rational_mod((row * self.gram_matrix_quadratic() * col)[0, 0], 2)

    quadratic_product = q

    def hom(self, images):
        return SyntheticDiscriminantAction.from_images(self, images)

    def pushforward_form(self, phi):
        if not (phi.discriminant_group() is self):
            raise ValueError("pushforward requires an endomorphism of this finite quadratic form")
        inverse = phi.inverse()
        return _form_matrix_on_images(self, [inverse(generator) for generator in self.gens()])

    def pullback_form(self, phi):
        if not (phi.discriminant_group() is self):
            raise ValueError("pullback requires an endomorphism of this finite quadratic form")
        return _form_matrix_on_images(self, [phi(generator) for generator in self.gens()])

    def normal_form(self, partial=False, return_isometry=False):
        if self.ngens() == 0:
            normal = ((), matrix(QQ, 0, 0))
            if return_isometry:
                return normal, SyntheticDiscriminantAction(self, identity_matrix(ZZ, 0))
            return normal
        best_key = None
        best_normal_form = None
        best_images = None
        for images in self._invariant_basis_candidates():
            invariants = tuple(self.order(image) for image in images)
            form = _form_matrix_on_images(self, images)
            key = (invariants, tuple(form.list()))
            if best_key is None or key < best_key:
                best_key = key
                best_normal_form = (invariants, form)
                best_images = images
        if not (best_normal_form is not None):
            raise ValueError("finite invariant-basis enumeration produced no presentation; "
            f"invariants={self.invariants()}")
        if return_isometry:
            return best_normal_form, SyntheticDiscriminantAction.from_images(self, best_images)
        return best_normal_form

    def _invariant_basis_candidates(self):
        elements = tuple(self.elements())
        for invariants in sorted(set(permutations(self.invariants()))):
            candidates_by_generator = tuple(
                tuple(element for element in elements if self.order(element) == invariant)
                for invariant in invariants
            )
            for images in product(*candidates_by_generator):
                if self._generates_full_group(images):
                    yield images

    def _generates_full_group(self, images):
        generated = set()
        coefficient_ranges = tuple(range(self.order(image)) for image in images)
        for coefficients in product(*coefficient_ranges):
            generated.add(tuple(self.discrete_exp(coefficients, gens=images).coordinates()))
        return ZZ(len(generated)) == self.cardinality()

    def _isomorphism_images_to(self, other):
        candidates_by_generator = tuple(
            tuple(element for element in other.elements() if other.order(element) == invariant)
            for invariant in self.invariants()
        )
        return (images for images in product(*candidates_by_generator) if other._generates_full_group(images))

    def _mapped_to(self, other, element, images):
        return other.discrete_exp(self.coordinates(element), gens=images)

    def _images_preserve_structure(self, other, images, kind):
        for left in self.elements():
            mapped_left = self._mapped_to(other, left, images)
            if kind == "quadratic" and self.q(left) != other.q(mapped_left):
                return False
            for right in self.elements():
                mapped_right = self._mapped_to(other, right, images)
                if self.b(left, right) != other.b(mapped_left, mapped_right):
                    return False
        return True

    def is_isomorphic(self, other, kind="quadratic"):
        if not (kind in ("group", "bilinear", "quadratic")):
            raise ValueError(f"isomorphism kind must be group, bilinear, or quadratic; found={kind}")
        if not (isinstance(other, SyntheticFiniteQuadraticForm)):
            raise TypeError(f"expected SyntheticFiniteQuadraticForm; found={type(other)}")
        if self.cardinality() != other.cardinality():
            return False
        if kind == "group":
            return any(True for _images in self._isomorphism_images_to(other))
        if kind == "bilinear":
            return any(self._images_preserve_structure(other, images, kind) for images in self._isomorphism_images_to(other))
        return self.normal_form() == other.normal_form()

    is_isomorphic_to = is_isomorphic

    def radical(self):
        return self.subgroup(element for element in self.elements() if all(self.b(element, other) == 0 for other in self.elements()))

    left_kernel = radical
    right_kernel = radical
    annihilator_subgroup = orthogonal

    def is_nondegenerate(self):
        return self.radical().cardinality() == 1

    def character_group(self):
        return self

    def pontryagin_dual(self):
        if not self.is_nondegenerate():
            raise ValueError("Pontryagin dual identification requires a nondegenerate form; found degenerate")
        return self.pairing_isomorphism_to_dual()

    def pairing_character(self, element):
        element = self(element)
        return lambda other: self.b(element, other)

    def pairing_isomorphism_to_dual(self):
        if not (self.is_nondegenerate()):
            raise ValueError("pairing identification with the dual requires a nondegenerate bilinear form")
        return {element: self.pairing_character(element) for element in self.elements()}

    def brown_invariant(self):
        return SyntheticDiscriminantGroup.brown_invariant(self)

    def is_genus(self, signature_pair, even=True):
        return SyntheticDiscriminantGroup.is_genus(self, signature_pair, even=even)

    def genus(self, signature_pair, even=True):
        return SyntheticDiscriminantGroup.genus(self, signature_pair, even=even)

    def twist(self, scalar):
        return SyntheticFiniteQuadraticForm(self.gram_matrix_quadratic() * QQ(scalar))

    def orthogonal_group(self, gens=None, check=False, kind="quadratic"):
        if not (kind in ("quadratic", "bilinear")):
            raise ValueError(f"orthogonal group kind must be quadratic or bilinear; found={kind}")
        if gens is None:
            actions = []
            candidates = tuple(self.elements())
            for images in product(candidates, repeat=self.ngens()):
                action = SyntheticDiscriminantAction.from_images(self, images)
                if action.is_automorphism() and action.preserves_form(kind=kind):
                    actions.append(action)
            return SyntheticOrthogonalGroup(self, actions)
        actions = tuple(SyntheticDiscriminantAction(self, matrix(ZZ, gen)) for gen in gens)
        if check:
            for action in actions:
                if not (action.preserves_form(kind=kind)):
                    raise ValueError(f"finite quadratic form action does not preserve the form; matrix={action.matrix()}")
        return SyntheticOrthogonalGroup(self, actions, close=True)

    isometry_group = orthogonal_group

    def automorphism_group(self):
        return SyntheticOrthogonalGroup(self, _all_group_automorphisms(self))

    def quadratic_orthogonal_group(self, gens=None, check=False):
        return self.orthogonal_group(gens=gens, check=check, kind="quadratic")

    def bilinear_orthogonal_group(self, gens=None, check=False):
        return self.orthogonal_group(gens=gens, check=check, kind="bilinear")


def TorsionQuadraticForm(gram_matrix):
    r"""Public Sage-compatible constructor for an owned finite quadratic form."""
    return SyntheticFiniteQuadraticForm(gram_matrix)


class SyntheticGenus:
    r"""Minimal owned genus datum determined by a signature and discriminant form."""

    def __init__(self, discriminant_group, signature_pair, even=True):
        self._discriminant_group = discriminant_group
        self._signature_pair = (ZZ(signature_pair[0]), ZZ(signature_pair[1]))
        self._even = bool(even)

    def discriminant_group(self):
        return self._discriminant_group

    def signature_pair(self):
        return self._signature_pair

    def signature(self):
        return self._signature_pair[0] - self._signature_pair[1]

    def is_even(self):
        return self._even

    def brown_invariant(self):
        return self.discriminant_group().brown_invariant()

    def __eq__(self, other):
        if not isinstance(other, SyntheticGenus):
            return False
        if self.signature_pair() != other.signature_pair() or self.is_even() != other.is_even():
            return False
        left = self.discriminant_group()
        right = other.discriminant_group()
        if left.source_lattice().gram_matrix() == right.source_lattice().gram_matrix():
            return True
        return left.normal_form() == right.normal_form()

    def __repr__(self):
        return (
            "Synthetic genus with signature "
            f"{self.signature_pair()} and discriminant invariants {self.discriminant_group().invariants()}"
        )


class TwistedSyntheticDiscriminantGroup(Parent):
    r"""Discriminant form with bilinear and quadratic forms scaled by a unit."""

    Element = SyntheticDiscriminantGroupElement

    def __init__(self, discriminant_group, scalar):
        if not (isinstance(discriminant_group, SyntheticDiscriminantGroup)):
            raise TypeError(f"expected SyntheticDiscriminantGroup; found={type(discriminant_group)}")
        self._discriminant_group = discriminant_group
        self._scalar = QQ(scalar)
        Parent.__init__(self, base=ZZ, category=discriminant_group.category())

    def _element_constructor_(self, coordinates):
        return self.element_class(self, coordinates)

    def __getattr__(self, name):
        return getattr(self._discriminant_group, name)

    def invariants(self):
        return self._discriminant_group.invariants()

    def ngens(self):
        return self._discriminant_group.ngens()

    def source_lattice(self):
        return self._discriminant_group.source_lattice()

    def cardinality(self):
        return self._discriminant_group.cardinality()

    def annihilator(self):
        return self._discriminant_group.annihilator()

    def gens(self):
        return tuple(self.gen(i) for i in range(self.ngens()))

    def gen(self, i):
        row = [ZZ.zero()] * self.ngens()
        row[i] = ZZ.one()
        return self(row)

    def elements(self):
        if not self.invariants():
            return (self([]),)
        return tuple(self(coordinates) for coordinates in product(*[range(invariant) for invariant in self.invariants()]))

    def order(self, element):
        return self._discriminant_group.order(self._discriminant_group(element.coordinates()))

    def value_module(self):
        return self._discriminant_group.value_module()

    def value_module_qf(self):
        return self._discriminant_group.value_module_qf()

    def gram_matrix_bilinear(self):
        return matrix(QQ, self._scalar * self._discriminant_group.gram_matrix_bilinear())

    def gram_matrix_quadratic(self):
        return self.gram_matrix_bilinear()

    def b(self, left, right):
        left = self(left) if left.parent() is not self else left
        right = self(right) if right.parent() is not self else right
        return rational_mod(
            self._scalar
            * self._discriminant_group.b(
                self._discriminant_group(left.coordinates()),
                self._discriminant_group(right.coordinates()),
            ),
            1,
        )

    inner_product = b

    def q(self, element):
        element = self(element) if element.parent() is not self else element
        return rational_mod(
            self._scalar * self._discriminant_group.q(self._discriminant_group(element.coordinates())),
            self._quadratic_modulus(),
        )

    quadratic_product = q

    def normal_form(self, partial=False):
        return self.invariants(), self.gram_matrix_bilinear()

    def brown_invariant(self):
        return SyntheticDiscriminantGroup.brown_invariant(self)

    def is_genus(self, signature_pair, even=True):
        return SyntheticDiscriminantGroup.is_genus(self, signature_pair, even=even)

    def genus(self, signature_pair, even=True):
        return SyntheticDiscriminantGroup.genus(self, signature_pair, even=even)

    def _quadratic_modulus(self):
        return self._discriminant_group._quadratic_modulus()
