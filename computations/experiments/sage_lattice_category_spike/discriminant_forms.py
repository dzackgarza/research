r"""The one consolidated finite-quotient discriminant-form parent (form-free layer).

A single Smith-based ``A / H`` quotient surface, implemented once. The two legacy
duplicates (an ordinary finite quotient of a discriminant group, and a same-rank
``ZZ``-lattice quotient) differed only in a construction-provenance seam: how the
covering object's coordinates are read (``ngens``/``coordinates`` vs
``rank``/``coefficient_vector``) and what ``lift`` returns. That seam is three tiny
hooks; everything else is shared here. The lattice-quotient case is the
:class:`SyntheticLatticeQuotient` subclass, not a second surface.
"""

from __future__ import annotations

from itertools import product

from sage.arith.functions import lcm
from sage.matrix.constructor import identity_matrix, matrix
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.parent import Parent

from .categories import DiscriminantForms
from .domain_algebra import DiscriminantForm as DiscriminantFormCarrier
from .discriminant import (
    SyntheticDiscriminantAction,
    SyntheticDiscriminantGroupElement,
    SyntheticDiscriminantSubgroup,
    SyntheticOrthogonalGroup,
    _all_group_automorphisms,
    _finite_all_subgroups,
    _finite_basis_from_generators,
    _finite_p_torsion,
    _finite_relations_among,
    _relation_inclusion_matrix,
)
from .elements import SyntheticLatticeElement


class SyntheticDiscriminantForm(DiscriminantFormCarrier, Parent):
    r"""Ordinary finite quotient ``A / H`` of a synthetic discriminant group.

    The single Smith-based finite-quotient parent; ``lift`` returns an element of
    the covering group. The same-rank ``ZZ``-lattice quotient is the
    :class:`SyntheticLatticeQuotient` subclass.
    """

    Element = SyntheticDiscriminantGroupElement

    def __init__(self, ambient_group, relation_subgroup):
        assert all(hasattr(ambient_group, name) for name in ("ngens", "invariants", "gens", "order")), (f"expected finite additive parent; found={type(ambient_group)}")
        relation_subgroup = ambient_group._subgroup(relation_subgroup)
        relation_rows = []
        for i, invariant in enumerate(ambient_group.invariants()):
            row = [ZZ.zero()] * ambient_group.ngens()
            row[i] = ZZ(invariant)
            relation_rows.append(row)
        relation_rows.extend([list(ambient_group.coordinates(generator)) for generator in relation_subgroup.gens()])
        presentation = matrix(ZZ, relation_rows) if relation_rows else matrix(ZZ, 0, 0)
        self._install(ambient_group, relation_subgroup, presentation)

    def _install(self, cover, relations, presentation_matrix):
        r"""Normalize the presentation to a Smith form and record the invariants.

        The single normalized internal representation: the covering object, the
        relation object, and the Smith change-of-basis ``smith_right`` (with its
        inverse) that carries cover coordinates into invariant coordinates.
        """
        self._cover = cover
        self._relations = relations
        smith, _smith_left, smith_right = presentation_matrix.smith_form()
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

    # -- construction-provenance seam: how the cover's coordinates are read --
    # The subclass overrides these three for the lattice-quotient case; every
    # other method is shared verbatim.
    def _cover_dim(self):
        return self._cover.ngens()

    def _cover_coordinates(self, element):
        element = self._cover(element)
        return list(self._cover.coordinates(element))

    def _cover_element(self, coordinates):
        return self._cover(list(coordinates))

    def _repr_(self):
        return f"Synthetic finite discriminant quotient with invariants {self.invariants()}"

    def __eq__(self, other):
        return (
            type(self) is type(other)
            and self.cover() is other.cover()
            and self.relations() == other.relations()
            and self.invariants() == other.invariants()
        )

    def __hash__(self):
        return hash((id(self.cover()), self.relations(), self.invariants()))

    def _element_constructor_(self, coordinates):
        if isinstance(coordinates, SyntheticDiscriminantGroupElement) and coordinates.parent() is self:
            return coordinates
        return self.element_class(self, coordinates)

    def cover(self):
        return self._cover

    def relations(self):
        return self._relations

    def underlying_abelian_group(self):
        return self

    def invariants(self):
        return self._invariants

    def elementary_divisors(self):
        divisors = []
        for invariant in self.invariants():
            for prime, exponent in ZZ(invariant).factor():
                divisors.append(ZZ(prime) ** ZZ(exponent))
        return tuple(sorted(divisors))

    def annihilator(self):
        return lcm(self.invariants() or (ZZ.one(),))

    def exponent(self):
        return self.annihilator()

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
        assert p.is_prime(), (f"p-rank requires a prime; found={p}")
        return ZZ(sum(1 for invariant in self.invariants() if ZZ(invariant) % p == 0))

    def ngens(self):
        return len(self.invariants())

    def cardinality(self):
        if not self.invariants():
            return ZZ.one()
        return ZZ.prod(self.invariants())

    def is_finite(self):
        return True

    def gens(self):
        return tuple(self.gen(i) for i in range(self.ngens()))

    def smith_form_gens(self):
        transform = self.smith_to_gens()
        raw = self.gens()
        return tuple(self.discrete_exp(transform.column(j), gens=raw) for j in range(transform.ncols()))

    def gen(self, i):
        row = [ZZ.zero()] * self.ngens()
        row[i] = ZZ.one()
        return self(row)

    def smith_form_gen(self, i):
        return self.smith_form_gens()[i]

    def zero(self):
        return self([ZZ.zero()] * self.ngens())

    def elements(self):
        if not self.invariants():
            return (self([]),)
        return tuple(self(coordinates) for coordinates in product(*[range(invariant) for invariant in self.invariants()]))

    def list(self):
        return self.elements()

    def random_element(self):
        from sage.misc.prandom import choice
        return choice(self.elements())

    def order(self, element=None):
        if element is None:
            return self.cardinality()
        element = self(element)
        orders = []
        for coordinate, invariant in zip(element.coefficient_vector(), self.invariants()):
            orders.append(ZZ.one() if coordinate == 0 else invariant // ZZ(coordinate).gcd(invariant))
        return lcm(orders) if orders else ZZ.one()

    def coordinates(self, element, gens=None, reduce=True):
        if gens is None:
            return tuple(self(element).coefficient_vector())
        return self.discrete_log(element, gens=gens)

    def discrete_exp(self, coefficients, gens=None):
        coefficients = tuple(coefficients)
        gens = self.gens() if gens is None else tuple(self(gen) for gen in gens)
        assert len(coefficients) == len(gens), ("coefficient vector length must match generator count; "
        f"coefficients={coefficients}, gens={gens}")
        value = self.zero()
        for coefficient, generator in zip(coefficients, gens):
            value += ZZ(coefficient) * generator
        return value

    def discrete_log(self, element, gens=None):
        element = self(element)
        if gens is None:
            return tuple(element.coefficient_vector())
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

    def generator_relations(self):
        return matrix.diagonal(ZZ, self.invariants())

    def subgroup_generated_by(self, gens):
        return SyntheticDiscriminantSubgroup(self, gens)

    def _subgroup(self, subgroup_or_gens):
        if isinstance(subgroup_or_gens, SyntheticDiscriminantSubgroup):
            assert subgroup_or_gens.ambient() is self, ("subgroup belongs to a different finite quotient")
            return subgroup_or_gens
        return self.subgroup_generated_by(subgroup_or_gens)

    def contains_subgroup(self, subgroup_or_gens):
        return self._subgroup(subgroup_or_gens).ambient() is self

    def quotient_group(self, subgroup_or_gens):
        return SyntheticDiscriminantForm(self, self._subgroup(subgroup_or_gens))

    def quotient_map(self, subgroup_or_gens=None):
        if subgroup_or_gens is None:
            return self.projection
        quotient = self.quotient_group(subgroup_or_gens)
        return lambda element: quotient.projection(element)

    def cosets(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        unseen = set(self.elements())
        cosets = []
        while unseen:
            representative = min(unseen, key=lambda element: tuple(element.coefficient_vector()))
            coset = frozenset(representative + element for element in subgroup.elements())
            cosets.append(coset)
            unseen.difference_update(coset)
        return tuple(cosets)

    def primary_part(self, p):
        p = ZZ(p)
        assert p.is_prime(), (f"primary part requires a prime; found={p}")
        exponent = ZZ(self.annihilator()).valuation(p)
        return self.subgroup_generated_by(element for element in self.elements() if (p ** exponent) * element == self.zero())

    def primary_decomposition(self):
        return tuple(self.primary_part(p) for p in ZZ(self.annihilator()).prime_divisors())

    def torsion_subgroup(self):
        return self

    def all_submodules(self):
        return _finite_all_subgroups(self)

    def p_torsion(self, p, k=1):
        return _finite_p_torsion(self, p, k=k)

    def relations_among(self, gens):
        return _finite_relations_among(self, gens)

    def basis_from_generators(self, gens):
        return _finite_basis_from_generators(self, gens)

    def automorphism_group(self):
        return SyntheticOrthogonalGroup(self, _all_group_automorphisms(self))

    def projection(self, element):
        row = matrix(ZZ, 1, self._cover_dim(), self._cover_coordinates(element))
        smith_row = row * self._smith_right
        return self([ZZ(smith_row[0, position]) % invariant for position, invariant in zip(self._invariant_positions, self.invariants())])

    def lift(self, element):
        element = self(element)
        smith_row = matrix(ZZ, 1, self._cover_dim())
        for coordinate, position in zip(element.coefficient_vector(), self._invariant_positions):
            smith_row[0, position] = ZZ(coordinate)
        cover_coordinates = smith_row * self._smith_right_inverse
        return self._cover_element([ZZ(cover_coordinates[0, i]) for i in range(self._cover_dim())])


class SyntheticLatticeQuotient(SyntheticDiscriminantForm):
    r"""Finite quotient ``cover / relations`` of same-rank synthetic ``ZZ``-lattices.

    ``lift`` lands in the cover lattice. Carries the lattice-quotient vocabulary
    (``cover_lattice``/``relation_lattice``/``preimage_lattice``/
    ``coset_representative``/``hom``) that the group case does not.
    """

    def __init__(self, cover_lattice, relation_lattice):
        from .parents import SyntheticLattice
        assert isinstance(cover_lattice, SyntheticLattice), (f"expected SyntheticLattice cover; found={type(cover_lattice)}")
        assert isinstance(relation_lattice, SyntheticLattice), (f"expected SyntheticLattice relation lattice; found={type(relation_lattice)}")
        if not (cover_lattice.base_ring() is ZZ):
            raise ValueError("finite lattice quotient cover must be a ZZ-lattice")
        if not (relation_lattice.base_ring() is ZZ):
            raise ValueError("finite lattice quotient relations must be a ZZ-lattice")
        assert relation_lattice.rank() == cover_lattice.rank(), ("finite quotients require same-rank lattices")
        self._inclusion = _relation_inclusion_matrix(cover_lattice, relation_lattice)
        self._install(cover_lattice, relation_lattice, self._inclusion)

    def _cover_dim(self):
        return self._cover.rank()

    def _cover_coordinates(self, element):
        cover = self._cover
        if isinstance(element, SyntheticLatticeElement):
            assert element.parent() == cover, ("projection expects an element of the quotient cover; "
            f"expected={cover}, found={element.parent()}")
        else:
            element = cover(element)
        return list(element.coefficient_vector())

    def _repr_(self):
        return f"Synthetic finite lattice quotient with invariants {self.invariants()}"

    def __eq__(self, other):
        return (
            type(self) is type(other)
            and self.cover_lattice() == other.cover_lattice()
            and self.relation_lattice() == other.relation_lattice()
            and self.invariants() == other.invariants()
        )

    def __hash__(self):
        from .discriminant import _lattice_key
        return hash((_lattice_key(self.cover_lattice()), _lattice_key(self.relation_lattice()), self.invariants()))

    def cover_lattice(self):
        return self._cover

    def relation_lattice(self):
        return self._relations

    def coset_representative(self, element):
        return self.lift(element)

    def preimage_lattice(self, subgroup_or_gens, label="preimage_lattice"):
        subgroup = self._subgroup(subgroup_or_gens)
        # pi^{-1}(cover/relation) = cover exactly; return the given cover lattice
        # rather than an isometric HNF overlattice representative.
        if subgroup.cardinality() == self.cardinality():
            return self.cover_lattice()
        if self.cover_lattice().rank() == 0:
            return self.relation_lattice()
        # lift lands in the cover's basis; the relation lattice's overlattice builder
        # consumes rows in the relation's basis, so re-express through the inclusion M
        # (relation-coords = cover-coords . M^{-1}).
        inclusion_inverse = self._inclusion.inverse()
        lift_rows = [
            vector(QQ, self.lift(generator).coefficient_vector()) * inclusion_inverse
            for generator in subgroup.gens()
        ]
        if not lift_rows:
            return self.relation_lattice()
        return self.relation_lattice().overlattice(lift_rows, check_integral=False, label=label)

    def hom(self, images):
        return SyntheticDiscriminantAction.from_images(self, images)
