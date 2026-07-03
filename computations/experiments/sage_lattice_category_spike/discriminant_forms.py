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
from sage.misc.cachefunc import cached_method
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.parent import Parent

from .arithmetic import rational_mod
from .categories import DiscriminantForms
from .domain_algebra import (
    BilinearDiscriminantForm as BilinearDiscriminantFormCarrier,
    DiscriminantForm as DiscriminantFormCarrier,
    QuadraticDiscriminantForm as QuadraticDiscriminantFormCarrier,
    SourcedDiscriminantForm as SourcedDiscriminantFormCarrier,
)
from .discriminant import (
    SyntheticDiscriminantAction,
    SyntheticDiscriminantGroupElement,
    SyntheticDiscriminantSubgroup,
    SyntheticGenus,
    SyntheticOrthogonalGroup,
    _all_group_automorphisms,
    _finite_all_subgroups,
    _finite_basis_from_generators,
    _finite_p_torsion,
    _finite_relations_among,
    _form_matrix_on_images,
    _induced_subquotient_form,
    _lattice_key,
    _relation_inclusion_matrix,
)
from .elements import SyntheticLatticeElement
from .value_objects import value_module


class SyntheticDiscriminantForm(DiscriminantFormCarrier, Parent):
    r"""Ordinary finite quotient ``A / H`` of a synthetic discriminant group.

    The single Smith-based finite-quotient parent; ``lift`` returns an element of
    the covering group. The same-rank ``ZZ``-lattice quotient is the
    :class:`SyntheticLatticeQuotient` subclass.
    """

    Element = SyntheticDiscriminantGroupElement

    def __init__(self, ambient_group, relation_subgroup):
        assert isinstance(ambient_group, SyntheticDiscriminantForm), (f"expected a synthetic finite discriminant parent as the quotient cover; found={type(ambient_group)}")
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



class DiscriminantCharacter:
    r"""The character ``b(x, -) : A -> QQ/ZZ`` attached to an element of a
    nondegenerate bilinear discriminant form."""

    def __init__(self, form, element):
        self._form = form
        self._element = form(element)

    def __call__(self, other):
        return self._form.b(self._element, other)

    def __repr__(self):
        return f"Character b({self._element}, -) on {self._form}"


class PontryaginDualIdentification:
    r"""The canonical identification ``A ~ Hom(A, QQ/ZZ)`` of a nondegenerate
    bilinear discriminant form (typed, dict-free)."""

    def __init__(self, form):
        self._form = form

    def domain(self):
        return self._form

    def __getitem__(self, element):
        return DiscriminantCharacter(self._form, element)

    def __repr__(self):
        return f"Pontryagin identification of {self._form} with its character group"


class SyntheticBilinearDiscriminantForm(BilinearDiscriminantFormCarrier, SyntheticDiscriminantForm):
    r"""Finite bilinear discriminant form presented by a generator Gram matrix.

    The Bilinear stratum: it owns the finite-abelian-group surface (inherited from
    :class:`SyntheticDiscriminantForm`) plus the bilinear form ``b`` and its
    derived vocabulary (radical, orthogonal complements, isotropy, lagrangians,
    metabolizers, transported forms). The quotient here is Gram-presented, so
    ``cover`` is the form itself, ``relations`` the trivial subgroup, and
    ``lift``/``projection`` are the identity. Internal state: the bilinear Gram
    data on the Smith generators, carried as ``_gram_matrix`` on the active
    (nontrivial-order) generators.
    """

    Element = SyntheticDiscriminantGroupElement

    def __init__(self, gram_matrix, category=None, invariants=None):
        raw_gram = matrix(QQ, gram_matrix)
        assert raw_gram.is_square(), (f"finite discriminant form Gram matrix must be square; found={raw_gram}")
        assert raw_gram == raw_gram.transpose(), (f"finite discriminant form Gram matrix must be symmetric; found={raw_gram}")
        if invariants is not None:
            # explicit group presentation: a twist by a non-unit can make the
            # form integral on a generator WITHOUT killing the group element,
            # which denominator inference cannot represent
            invariants = [ZZ(invariant) for invariant in invariants]
            assert len(invariants) == raw_gram.nrows() and all(invariant > 1 for invariant in invariants), (
                f"explicit invariants must give one nontrivial order per generator; invariants={invariants}, gram={raw_gram}"
            )
            assert all(
                invariants[i] * raw_gram[i, j] in ZZ
                for i in range(raw_gram.nrows()) for j in range(raw_gram.ncols())
            ), (f"generator orders must clear the form's denominators; invariants={invariants}, gram={raw_gram}")
            self._install_bilinear(raw_gram, list(range(raw_gram.nrows())), invariants, category)
            return
        invariants = []
        active_indices = []
        for i in range(raw_gram.nrows()):
            denominators = [raw_gram[i, j].denominator() for j in range(raw_gram.ncols())]
            denominators.extend(raw_gram[j, i].denominator() for j in range(raw_gram.nrows()))
            invariant = ZZ(lcm(denominators))
            if invariant != 1:
                active_indices.append(i)
                invariants.append(invariant)
        self._install_bilinear(raw_gram, active_indices, invariants, category)

    def _install_bilinear(self, raw_gram, active_indices, invariants, category):
        gram = raw_gram.matrix_from_rows_and_columns(active_indices, active_indices) if active_indices else matrix(QQ, 0, 0)
        gram.set_immutable()
        self._gram_matrix = gram
        self._invariants = tuple(invariants)
        if category is None:
            category = DiscriminantForms(ZZ).Bilinear()
        Parent.__init__(self, base=ZZ, category=category)

    def _repr_(self):
        return f"Synthetic finite bilinear discriminant form with invariants {self.invariants()}"

    # Gram-presented forms are identified by object identity (the covering seam
    # the base parent keys equality on is trivial here, so it cannot separate them).
    def __eq__(self, other):
        return self is other

    def __hash__(self):
        return id(self)

    # -- Gram-presented cover/relations seam: the form is its own cover, with no
    # relations, so lift/projection are the identity (no Smith transport). --
    def cover(self):
        return self

    def relations(self):
        return self.subgroup_generated_by(())

    def lift(self, element):
        return self(element)

    def projection(self, element):
        return self(element)

    def permutation_group(self):
        from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup

        return AdditiveAbelianGroup(list(self.invariants())).permutation_group()

    def value_module(self):
        return value_module(ZZ, ZZ.one())

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
        row = matrix(QQ, 1, self.ngens(), list(left.coefficient_vector()))
        col = matrix(QQ, self.ngens(), 1, list(right.coefficient_vector()))
        return rational_mod((row * self.gram_matrix_bilinear() * col)[0, 0], 1)

    def radical(self):
        return self.subgroup_generated_by(element for element in self.elements() if all(self.b(element, other) == 0 for other in self.elements()))

    def is_nondegenerate(self):
        return self.radical().cardinality() == 1

    def orthogonal_submodule_to(self, subgroup_or_gens):
        r"""The subgroup orthogonal to ``subgroup_or_gens`` under ``b``, from an
        ephemeral Sage engine (module arithmetic — element enumeration is
        infeasible at research scale, and handing every orthogonal element to
        the subgroup constructor as a generator makes its closure product
        astronomically large)."""
        subgroup = self._subgroup(subgroup_or_gens)
        if self.ngens() == 0 or subgroup.cardinality() == 1:
            # complement of the trivial subgroup is the whole group; the
            # engine's linear algebra needs at least one nonzero generator
            return self.subgroup_generated_by(self.gens())
        engine = self._sage_engine()
        # the engine's cover basis corresponds 1:1 to the presented generators
        # (TorsionQuadraticForm builds V = (1/d)*ZZ^n with inner product q), so
        # coordinates transfer through V, NOT through the engine's Smith gens —
        # the presentation need not be Smith-normal (e.g. invariants (2, 3))
        cover = engine.V()
        basis = cover.basis()
        assert engine.cardinality() == self.cardinality() and all(
            engine(basis[i]).order() == invariant for i, invariant in enumerate(self.invariants())
        ), (
            "ephemeral Sage engine must reproduce the presented generator orders to "
            "transfer subgroup coordinates; "
            f"synthetic invariants={self.invariants()}, engine invariants={tuple(engine.invariants())}"
        )
        images = [
            engine(cover.linear_combination_of_basis(list(generator.coefficient_vector())))
            for generator in subgroup.gens()
        ]
        oracle = engine.orthogonal_submodule_to(images)
        return self.subgroup_generated_by(
            self([ZZ(coordinate) for coordinate in cover.coordinates(generator.lift())])
            for generator in oracle.gens()
        )

    def orthogonal(self, subgroup_or_gens):
        return self.orthogonal_submodule_to(subgroup_or_gens)

    def is_isotropic_element(self, element):
        return self.q(element) == 0

    def isotropic_elements(self):
        return tuple(element for element in self.elements() if self.is_isotropic_element(element))

    def is_isotropic_subgroup(self, subgroup_or_gens):
        return self._subgroup(subgroup_or_gens).is_quadratic_isotropic()

    def isotropic_subgroups(self):
        return tuple(subgroup for subgroup in self.all_submodules() if self.is_isotropic_subgroup(subgroup))

    def is_lagrangian(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return self.is_isotropic_subgroup(subgroup) and subgroup.cardinality() ** 2 == self.cardinality()

    def lagrangian_subgroups(self):
        return tuple(subgroup for subgroup in self.isotropic_subgroups() if self.is_lagrangian(subgroup))

    def metabolizer(self):
        subgroups = self.lagrangian_subgroups()
        if not subgroups:
            raise ValueError("form is anisotropic; it admits no metabolizer (lagrangian)")
        return subgroups[0]

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

    def restricted_form(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        return _form_matrix_on_images(self, subgroup.gens())

    def orthogonal_quotient(self, subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        if not self.is_isotropic_subgroup(subgroup):
            raise ValueError("orthogonal quotient requires a quadratic-isotropic relation subgroup")
        # H trivial => H-perp/H is the whole form; return it directly rather than
        # materialize orthogonal(H) (the whole group as an all-element subgroup,
        # whose closure enumerates a product over every generator order).
        if subgroup.cardinality() == 1:
            return self
        return _induced_subquotient_form(self, subgroup, self.orthogonal(subgroup))

    def subquotient_form(self, subgroup_or_gens, quotient_subgroup_or_gens):
        subgroup = self._subgroup(subgroup_or_gens)
        quotient_subgroup = self._subgroup(quotient_subgroup_or_gens)
        if not subgroup._key() <= quotient_subgroup._key():
            raise ValueError("subquotient form requires H contained in K")
        if not self.is_isotropic_subgroup(subgroup):
            raise ValueError("subquotient form requires a quadratic-isotropic relation subgroup")
        if not quotient_subgroup._key() <= self.orthogonal(subgroup)._key():
            raise ValueError("subquotient form requires K contained in the orthogonal complement of H")
        return _induced_subquotient_form(self, subgroup, quotient_subgroup)

    def hom(self, images):
        return SyntheticDiscriminantAction.from_images(self, images)

    def pushforward_form(self, phi):
        assert phi.discriminant_form() is self, ("pushforward requires an endomorphism of this finite quadratic form")
        inverse = phi.inverse()
        return _form_matrix_on_images(self, [inverse(generator) for generator in self.gens()])

    def pullback_form(self, phi):
        assert phi.discriminant_form() is self, ("pullback requires an endomorphism of this finite quadratic form")
        return _form_matrix_on_images(self, [phi(generator) for generator in self.gens()])

    def pontryagin_dual(self):
        r"""The canonical identification ``A ~ Hom(A, QQ/ZZ)`` as a typed
        object (spec: not a dict of lambdas): index by an element to get its
        character."""
        if not self.is_nondegenerate():
            raise ValueError("Pontryagin dual identification requires a nondegenerate form; found degenerate")
        return PontryaginDualIdentification(self)

    def is_isomorphic(self, other, kind="quadratic"):
        assert kind in ("group", "bilinear", "quadratic"), (f"isomorphism kind must be group, bilinear, or quadratic; found={kind}")
        assert isinstance(other, SyntheticBilinearDiscriminantForm), (f"expected SyntheticBilinearDiscriminantForm; found={type(other)}")
        # finite abelian groups are classified by their Smith invariant factors
        if self._smith_invariants() != other._smith_invariants():
            return False
        if kind == "group" or self.ngens() == 0:
            return True
        if kind == "bilinear":
            return self._bilinear_normal_presentation() == other._bilinear_normal_presentation()
        return self.normal_form() == other.normal_form()

    def _smith_invariants(self):
        r"""Canonical Smith invariant factors of the underlying group, from Sage's
        group normalization (presented generator orders need not be Smith-normal:
        ``diag(1/2, 1/3)`` presents ``(2, 3)``; the group is ``(6,)``)."""
        from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup

        return tuple(AdditiveAbelianGroup(list(self.invariants())).invariants())

    def _bilinear_normal_presentation(self):
        r"""The complete bilinear-isomorphism invariant from the oracle: re-present
        the ephemeral engine at the bilinear modulus (``modulus_qf = modulus``, the
        same presentation ``_delegated_orthogonal_group`` uses for ``O(b)``) and take
        its normal form. Sage's stated contract: two torsion quadratic modules are
        isomorphic iff they have the same value modules and the same normal form."""
        from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

        engine = self._sage_engine()
        assert engine.cardinality() == self.cardinality(), (
            "ephemeral Sage engine must carry the whole group to decide bilinear "
            "isomorphism (an explicit-invariants presentation can hold a generator "
            "the engine's denominator inference drops); "
            f"synthetic cardinality={self.cardinality()}, engine cardinality={engine.cardinality()}"
        )
        presented = TorsionQuadraticModule(engine.V(), engine.W(), modulus=engine._modulus, modulus_qf=engine._modulus)
        normal = presented.normal_form()
        gram = matrix(QQ, normal.gram_matrix_quadratic())
        gram.set_immutable()
        return (QQ(engine._modulus), tuple(normal.invariants()), gram)

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

    def _generates_full_group(self, images):
        generated = set()
        coefficient_ranges = tuple(range(self.order(image)) for image in images)
        for coefficients in product(*coefficient_ranges):
            generated.add(tuple(self.discrete_exp(coefficients, gens=images).coefficient_vector()))
        return ZZ(len(generated)) == self.cardinality()

    def orthogonal_group(self, gens=None, check=False, kind="quadratic"):
        assert kind in ("quadratic", "bilinear"), (f"orthogonal group kind must be quadratic or bilinear; found={kind}")
        if gens is None:
            return self._delegated_orthogonal_group(kind)
        actions = tuple(SyntheticDiscriminantAction(self, matrix(ZZ, gen)) for gen in gens)
        if check:
            for action in actions:
                assert action.preserves_form(kind=kind), (f"finite quadratic form action does not preserve the form; matrix={action.matrix()}")
        return SyntheticOrthogonalGroup(self, actions, close=True)

    def _delegated_orthogonal_group(self, kind):
        r"""O(q) (or the larger O(b)) from an ephemeral Sage torsion quadratic module
        built from this form's own Gram, translated back onto the owned generators.
        The engine's Smith presentation reproduces those generators, so an oracle
        action matrix (rows = images) becomes an owned action by transposition."""
        engine = self._sage_engine()
        assert tuple(engine.invariants()) == self.invariants() and engine.gram_matrix_quadratic() == self.gram_matrix_quadratic(), (
            "ephemeral Sage engine must reproduce the synthetic Smith presentation to "
            "translate orthogonal-group actions onto the owned generators; "
            f"synthetic invariants={self.invariants()}, engine invariants={tuple(engine.invariants())}"
        )
        if kind == "bilinear":
            from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

            # O(b): present the quadratic refinement at the bilinear modulus, so the
            # oracle's O(q) of this presentation is the bilinear orthogonal group.
            engine = TorsionQuadraticModule(engine.V(), engine.W(), modulus=engine._modulus, modulus_qf=engine._modulus)
        oracle = engine.orthogonal_group()
        actions = [SyntheticDiscriminantAction(self, matrix(ZZ, generator.matrix()).transpose()) for generator in oracle.gens()]
        return SyntheticOrthogonalGroup(self, actions, close=True)

    def bilinear_orthogonal_group(self, gens=None, check=False):
        return self.orthogonal_group(gens=gens, check=check, kind="bilinear")

    def q(self, element):
        r"""The induced diagonal quadratic form ``q(x) := b(x, x)`` — defined
        for EVERY bilinear form (placement ruling 2026-07-03: only
        polarization needs 2 invertible), valued in the bilinear value module.
        The Quadratic stratum overrides with its refined stored-modulus form.
        """
        return self.b(element, element)


class SyntheticQuadraticDiscriminantForm(QuadraticDiscriminantFormCarrier, SyntheticBilinearDiscriminantForm):
    r"""Finite quadratic discriminant form presented by a generator Gram matrix.

    The Quadratic stratum refines the bilinear one with the quadratic form ``q``
    and its genus vocabulary. ``q`` routes through a stored quadratic modulus
    (``2`` for even forms, ``1`` for odd), never a literal in the value path, so
    an odd form is representable; the module-level ``TorsionQuadraticForm``
    factory presents even forms with modulus ``2``.
    """

    def __init__(self, gram_matrix, quadratic_modulus=2, invariants=None):
        self._quadratic_modulus_value = ZZ(quadratic_modulus)
        category = DiscriminantForms(ZZ).Quadratic()
        if self._quadratic_modulus_value == 2:
            category = category.Even()
        SyntheticBilinearDiscriminantForm.__init__(self, gram_matrix, category=category, invariants=invariants)

    def _repr_(self):
        return f"Synthetic finite quadratic discriminant form with invariants {self.invariants()}"

    def _quadratic_modulus(self):
        return self._quadratic_modulus_value

    def value_module_qf(self):
        return value_module(ZZ, self._quadratic_modulus() * ZZ.one())

    def gram_matrix_quadratic(self):
        return self._gram_matrix

    def q(self, element):
        element = self(element) if element.parent() is not self else element
        row = matrix(QQ, 1, self.ngens(), list(element.coefficient_vector()))
        col = matrix(QQ, self.ngens(), 1, list(element.coefficient_vector()))
        return rational_mod((row * self.gram_matrix_quadratic() * col)[0, 0], self._quadratic_modulus())

    def primary_part(self, p):
        p = ZZ(p)
        assert p.is_prime(), (f"primary part requires a prime; found={p}")
        images = []
        for invariant, generator in zip(self.invariants(), self.gens()):
            valuation = ZZ(invariant).valuation(p)
            if valuation:
                images.append((ZZ(invariant) // (p ** valuation)) * generator)
        modulus = self._quadratic_modulus()
        if not images:
            return SyntheticQuadraticDiscriminantForm(matrix(QQ, 0, 0), quadratic_modulus=modulus)
        return SyntheticQuadraticDiscriminantForm(_form_matrix_on_images(self, images), quadratic_modulus=modulus)

    def _sage_engine(self):
        r"""An ephemeral Sage torsion quadratic module built from this form's own
        quadratic Gram. Its Smith presentation reproduces the owned generators, so
        the oracle's per-generator results transfer back without a coordinate map."""
        from sage.modules.torsion_quadratic_module import TorsionQuadraticForm

        return TorsionQuadraticForm(self.gram_matrix_quadratic())

    def _delegated_normal_form(self, return_isometry):
        r"""Sage's torsion-module normal form, returned as the owned ``(invariants,
        Gram)`` pair. The change of generators (when asked) reads Sage's normal-form
        generators back in the engine's Smith coordinates, which are the owned ones."""
        if self.ngens() == 0:
            normal = ((), matrix(QQ, 0, 0))
            if return_isometry:
                return normal, SyntheticDiscriminantAction(self, identity_matrix(ZZ, 0))
            return normal
        engine = self._sage_engine()
        oracle = engine.normal_form()
        gram = matrix(QQ, oracle.gram_matrix_quadratic())
        gram.set_immutable()
        normal = (tuple(oracle.invariants()), gram)
        if not return_isometry:
            return normal
        images = [self(list(engine(generator.lift()).vector())) for generator in oracle.gens()]
        return normal, SyntheticDiscriminantAction.from_images(self, images)

    def normal_form(self, partial=False, return_isometry=False):
        return self._delegated_normal_form(return_isometry)

    def brown_invariant(self):
        r"""Return the Brown invariant in ``ZZ/8`` from the ephemeral Sage engine."""
        return ZZ(self._sage_engine().brown_invariant())

    def is_genus(self, signature_pair, even=True):
        r"""Return whether this discriminant form and signature define an even genus,
        decided by the ephemeral Sage engine."""
        s_plus = ZZ(signature_pair[0])
        s_minus = ZZ(signature_pair[1])
        assert s_plus >= 0 and s_minus >= 0, (
            f"signature invariants must be nonnegative; found s_plus={s_plus}, s_minus={s_minus}; "
            "fix the caller's signature pair"
        )
        assert even, (
            "genus classification through the discriminant-form correspondence is "
            "grounded only for the even case in this spike (the correspondence "
            "itself is parity-agnostic; the odd engine is unbuilt); "
            f"signature_pair={(s_plus, s_minus)}, invariants={self.invariants()}"
        )
        return self._sage_engine().is_genus((s_plus, s_minus), even=even)

    def genus(self, signature_pair, even=True):
        r"""Return the synthetic genus datum determined by signature and discriminant form."""
        if not self.is_genus(signature_pair, even=even):
            raise ValueError("this discriminant form and signature do not define a genus in this spike")
        return SyntheticGenus(self, signature_pair, even=even)

    def twist(self, scalar):
        r"""The form scaled by ``scalar`` on the SAME group (oracle
        round-trip: a non-unit twist can make the form integral on a
        generator without killing the group element, so the result carries
        its group explicitly)."""
        from sage.modules.torsion_quadratic_module import TorsionQuadraticForm as _SageTorsionForm

        engine = _SageTorsionForm(self.gram_matrix_quadratic()).twist(ZZ(scalar))
        return SyntheticQuadraticDiscriminantForm(
            engine.gram_matrix_quadratic(),
            quadratic_modulus=self._quadratic_modulus(),
            invariants=tuple(ZZ(i) for i in engine.invariants()),
        )

    def quadratic_orthogonal_group(self, gens=None, check=False):
        return self.orthogonal_group(gens=gens, check=check, kind="quadratic")


class SyntheticSourcedDiscriminantForm(SourcedDiscriminantFormCarrier, SyntheticQuadraticDiscriminantForm):
    r"""The sourced stratum ``L# / L`` of a nondegenerate integral lattice ``L``.

    The consolidated quadratic discriminant form refined with source-lattice
    provenance (category axiom ``WithSourceLattice``). Its state and form
    computation are source-based, not Gram-presented: the Smith normal form of
    the source Gram fixes the invariant coordinate system, ``cover = L#`` is the
    metric dual and ``relations = L``, and the bilinear/quadratic Gram on the
    invariant generators is read off ``G^{-1}`` through the dual coordinates. The
    parity modulus follows the source lattice (``2`` even, ``1`` odd). Everything
    the quadratic stratum owns generically -- the group surface, ``b``/``q`` on
    the recorded Gram, the isotropic/orthogonal/isomorphism/genus vocabulary --
    is inherited; this class adds only the source-aware seam: the dual cover, the
    Smith-transported lift/projection, coset representatives in the source hull,
    overlattices, the induced action of a lattice isometry, and the orbit
    vocabulary of that action.
    """

    Element = SyntheticDiscriminantGroupElement

    def __init__(self, source_lattice, primary):
        from .parents import SyntheticLattice
        assert isinstance(source_lattice, SyntheticLattice), (f"expected SyntheticLattice source; found={type(source_lattice)}")
        assert primary == 0 or ZZ(primary).is_prime(), (f"primary must be 0 or prime; found={primary}")
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
        self._invariants = tuple(invariants)
        category = DiscriminantForms(ZZ).Bilinear().WithSourceLattice()
        if source_lattice.is_even():
            category = DiscriminantForms(ZZ).Quadratic().Even().WithSourceLattice()
        Parent.__init__(self, base=ZZ, category=category)

    def _repr_(self):
        return f"Synthetic discriminant group with invariants {self.invariants()}"

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticSourcedDiscriminantForm)
            and _lattice_key(self.source_lattice()) == _lattice_key(other.source_lattice())
            and self._primary == other._primary
            and self.invariants() == other.invariants()
        )

    def __hash__(self):
        return hash((_lattice_key(self.source_lattice()), self._primary, self.invariants()))

    # -- source-aware seam: cover = L#, relations = L --
    def rank(self):
        return self._source_lattice.rank()

    def source_lattice(self):
        return self._source_lattice

    def cover(self):
        return self._source_lattice.dual()

    def cover_lattice(self):
        return self.cover()

    def relations(self):
        return self._source_lattice

    def relation_lattice(self):
        return self.relations()

    def is_nondegenerate(self):
        return self.cardinality() == abs(self.source_lattice().determinant())

    def _quadratic_modulus(self):
        return ZZ(2) if self.source_lattice().is_even() else ZZ.one()

    # -- source-based form data: read the Gram on the invariant generators off
    # G^{-1} through the dual coordinates, never a stored Gram presentation. --
    @cached_method
    def _raw_form_matrix(self):
        if self.ngens() == 0:
            return matrix(QQ, 0, 0)
        columns = [self._old_dual_coordinates(self.gen(i)) for i in range(self.ngens())]
        transform = matrix(QQ, self.rank(), self.ngens(), [columns[j][i, 0] for i in range(self.rank()) for j in range(self.ngens())])
        form = transform.transpose() * self.source_lattice().gram_matrix().inverse() * transform
        form.set_immutable()
        return form

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

    def _old_dual_coordinates(self, element):
        full_coordinates = matrix(ZZ, self.rank(), 1)
        for coordinate, position, multiplier in zip(
            element.coefficient_vector(),
            self._invariant_positions,
            self._coordinate_multipliers,
        ):
            full_coordinates[position, 0] = ZZ(coordinate) * ZZ(multiplier)
        return self._smith_right_inverse_transpose * full_coordinates

    # -- Smith-transported lift/projection between L# and the invariant coords --
    def lift(self, element):
        # cover = L# is a based lattice whose intrinsic basis IS the dual basis of L,
        # so the dual-coordinate column produced by the Smith machinery is already the
        # lift's coordinate vector in the cover -- no ambient round-trip.
        z_coordinates = self._old_dual_coordinates(self(element))
        return self.cover()(z_coordinates.column(0))

    def projection(self, element):
        cover = self.cover()
        if isinstance(element, SyntheticLatticeElement):
            assert element.parent() == cover, ("projection expects an element of the dual cover; "
            f"expected={cover}, found={element.parent()}")
        else:
            element = cover(element)
        # cover's intrinsic coordinates are already the dual-basis coordinates the
        # Smith machinery consumes (see lift).
        z_coordinates = matrix(ZZ, self.rank(), 1, list(element.coefficient_vector()))
        smith_coordinates = self._smith_right_transpose * z_coordinates
        projected = []
        for position, invariant, multiplier in zip(
            self._invariant_positions,
            self.invariants(),
            self._coordinate_multipliers,
        ):
            projected.append((ZZ(smith_coordinates[position, 0]) * ZZ(multiplier).inverse_mod(invariant)) % invariant)
        return self(projected)

    def coset_representative(self, element):
        return self.lift(element)

    def _coset_representative_in_source(self, element):
        r"""Coset representative of ``element`` in the source lattice's rational hull.

        A lift lives in ``L# ⊇ L``; its dual-basis column ``z`` has source-basis
        coordinates ``G^{-1} z``.  The source lattice's ``overlattice`` / ``span``
        builders consume rows in the *root* (hull) frame, so map through the source's
        own inclusion into its root.
        """
        z_coordinates = self._old_dual_coordinates(self(element))
        source_coordinates = self.source_lattice().gram_matrix().inverse() * z_coordinates
        return vector(QQ, source_coordinates.column(0)) * self.source_lattice()._inclusion_rows()

    def primary_part(self, p):
        return SyntheticSourcedDiscriminantForm(self.source_lattice(), p)

    # -- overlattices and preimages in the source hull --
    def overlattice_from_isotropic_subgroup(self, subgroup_or_gens, label="overlattice"):
        subgroup = self._subgroup(subgroup_or_gens)
        if not (subgroup.is_bilinear_isotropic()):
            raise ValueError("overlattice construction requires a bilinear-isotropic subgroup")
        lift_rows = [self._coset_representative_in_source(generator) for generator in subgroup.gens()]
        if not lift_rows:
            return self.source_lattice()
        return self.source_lattice().overlattice(lift_rows, check_integral=True, label=label)

    def preimage_lattice(self, subgroup_or_gens, label="preimage_lattice"):
        subgroup = self._subgroup(subgroup_or_gens)
        # pi^{-1}(A_L) = L# exactly; return the canonical dual cover rather than an
        # isometric HNF overlattice representative.
        if subgroup.cardinality() == self.cardinality():
            return self.cover()
        lift_rows = [self._coset_representative_in_source(generator) for generator in subgroup.gens()]
        if not lift_rows:
            return self.source_lattice()
        return self.source_lattice().overlattice(lift_rows, check_integral=False, label=label)

    def discriminant_form_of_overlattice(self, subgroup_or_gens):
        return self.overlattice_from_isotropic_subgroup(subgroup_or_gens).discriminant_group()

    # -- the induced action of a lattice isometry, and its orbit vocabulary --
    def action_of_isometry(self, isometry):
        if self.ngens() == 0:
            return SyntheticDiscriminantAction(self, identity_matrix(ZZ, 0))
        gram = matrix(QQ, self.source_lattice().gram_matrix())
        isometry_matrix = matrix(QQ, isometry.matrix())
        induced_images = []
        for generator in self.gens():
            old_coordinates = self._old_dual_coordinates(generator)
            # dual action on L# in its intrinsic (dual) basis: G U G^{-1}.
            new_coordinates = gram * isometry_matrix * gram.inverse() * old_coordinates
            induced_images.append(self.projection(self.cover()(new_coordinates.column(0))))
        return SyntheticDiscriminantAction.from_images(self, induced_images)

    def action_of_lattice_group(self, gens):
        return self.orthogonal_group_from_lattice_gens(gens)

    def kernel_of_lattice_group_action(self, gens):
        return tuple(
            gen
            for gen in gens
            if self.action_of_isometry(gen).is_identity()
        )

    def orthogonal_group_from_lattice_gens(self, gens):
        from .homsets import LatticeMorphism

        isometries = [
            gen if isinstance(gen, LatticeMorphism)
            else self.source_lattice().isometry_group().from_matrix(gen)
            for gen in gens
        ]
        return SyntheticOrthogonalGroup(self, (self.action_of_isometry(gen) for gen in isometries), close=True)

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
        subgroups = set(self.all_submodules())
        orbits = []
        while subgroups:
            representative = next(iter(subgroups))
            orbit = frozenset(self.subgroup_generated_by(action(element) for element in representative.elements()) for action in group)
            orbits.append(orbit)
            subgroups.difference_update(orbit)
        return tuple(orbits)

    def orbits_on_isotropic_subgroups(self, group=None):
        isotropic = set(self.isotropic_subgroups())
        return tuple(orbit for orbit in self.orbits_on_subgroups(group=group) if orbit & isotropic)

    # -- source-based oracle: the ephemeral engine is the source lattice's own
    # discriminant group (its Smith presentation reproduces the owned generators);
    # normal_form is inherited from the Gram stratum's delegation through it. --
    def _sage_engine(self):
        from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

        engine = IntegralLattice(matrix(ZZ, self.source_lattice().gram_matrix())).discriminant_group()
        if self._primary:
            engine = engine.primary_part(self._primary)
        return engine

    def isometry_to(self, other, kind="quadratic"):
        assert kind in ("quadratic", "bilinear"), (f"isometry kind must be quadratic or bilinear; found={kind}")
        assert isinstance(other, SyntheticSourcedDiscriminantForm), (f"expected SyntheticSourcedDiscriminantForm; found={type(other)}")
        if not self.is_isomorphic(other, kind=kind):
            raise ValueError("discriminant forms are not isomorphic")
        for images in self._isomorphism_images_to(other):
            if self._images_preserve_structure(other, images, kind):
                return SyntheticDiscriminantAction.from_images(self, (self(image.coefficient_vector()) for image in images))
        assert False, (
            "no isometry found despite is_isomorphic; internal invariant broken between "
            f"is_isomorphic and _images_preserve_structure for kind={kind}"
        )

    def _generates_full_group(self, images):
        zero = tuple(ZZ.zero() for _ in self.invariants())
        generated = set()
        coefficient_ranges = tuple(range(invariant) for invariant in self.invariants())
        for coefficients in product(*coefficient_ranges):
            coordinates = zero
            for coefficient, image in zip(coefficients, images):
                coordinates = tuple(
                    (coordinates[i] + ZZ(coefficient) * image.coefficient_vector()[i]) % self.invariants()[i]
                    for i in range(self.ngens())
                )
            generated.add(coordinates)
        return ZZ(len(generated)) == self.cardinality()

    @classmethod
    def trivial(cls, source_lattice):
        return cls(source_lattice, 0)
