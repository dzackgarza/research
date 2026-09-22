r"""Primitive totally isotropic sublattices, flags, and full-orthogonal-group orbits.

The orbit representatives, the equivalence witness and the stabilizer are
mathematical operations of this file; the algorithm realizing each one is
asked for by name from the ordered capability layer, so no engine is named
here.  An operation no registered provider supplies refuses by naming its
capability and what would provision it, which is the owned behaviour until a
provider arrives.
"""

from sage.structure.element import parent as element_parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.modules.pure.modules import ModuleSubobjects
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of

from dzack_research.preamble.engine_capabilities import engine_capabilities


def _held(lattice, element):
    return element if element_parent(element) is lattice else lattice(element)


def _is_lattice_subobject_of_rank(sublattice, lattice, rank) -> bool:
    r"""Whether ``sublattice`` is a module subobject of ``lattice`` of module rank ``rank``."""
    return (
        sublattice in ModuleSubobjects(lattice.base_ring())
        and sublattice.inclusion().codomain() is lattice
        and int(sublattice.module_rank()) == rank
    )


class _PrimitiveIsotropicVectorOrbitEngine:
    r"""Private set realization of one primitive-isotropic vector orbit."""

    def __init__(self, group, locus, representative, **rest) -> None:
        self._group = group
        self._locus = locus
        self._representative = representative
        super().__init__(facade=True, **rest)

    def group(self):
        return self._group

    def universe(self):
        return self._locus

    def representative(self):
        return self._representative

    def stabilizer(self):
        return self.group().stabilizer(self.representative())

    def transporter_from(self, vector):
        return self.group().vector_equivalence_witness(
            vector,
            self.representative(),
        )

    def __contains__(self, vector) -> bool:
        return vector in self.universe() and self.transporter_from(vector) is not None

    is_parent_of = __contains__

    def _element_constructor_(self, vector):
        if vector not in self:
            raise ValueError(f"{vector} is not in {self}")
        return self.universe()(vector)

    def _repr_(self) -> str:
        return f"Primitive-isotropic orbit of {self.representative()} under {self.group()}"


def _primitive_isotropic_vector_orbit(group, locus, representative):
    return _object_of(
        Sets(),
        _engine=(Sets(), _PrimitiveIsotropicVectorOrbitEngine, None),
        group=group,
        locus=locus,
        representative=representative,
    )


class _FiniteOrbitDecompositionSetEngine:
    r"""Private finite-set realization shared by represented orbit decompositions."""

    def __iter__(self):
        return iter(self._orbits)

    def __contains__(self, orbit) -> bool:
        return orbit in self._orbits

    is_parent_of = __contains__

    def _element_constructor_(self, orbit):
        if orbit not in self:
            raise ValueError(f"{orbit} is not an orbit of {self}")
        return orbit

    def orbits(self):
        return self


class _PrimitiveIsotropicVectorOrbitDecompositionEngine(_FiniteOrbitDecompositionSetEngine):
    r"""The finite ``O(L)``-orbit decomposition of primitive isotropic vectors.

    Rank-one primitive isotropic sublattice orbits and primitive isotropic
    vector orbits coincide for the full orthogonal group: a line generator can
    only be sent to either generator of the target primitive line, and ``-id``
    belongs to ``O(L)``.  Thus the existing exact rank-one isotropic backend
    supplies the representatives, while vector stabilizers and transporters
    remain the already-owned group operations.
    """

    def __init__(self, group, locus, **rest) -> None:
        if group.lattice() is not locus.universe():
            raise ValueError("the orbit group and primitive-isotropic locus require one lattice")
        self._group = group
        self._locus = locus
        representatives = []
        for line in group.isotropic_orbit_representatives(1):
            generator = line.module_generator(0)
            representatives.append(line.inclusion()(generator))
        self._orbits = finite_ordered_set(
            tuple(
                _primitive_isotropic_vector_orbit(group, locus, representative)
                for representative in representatives
            )
        )
        super().__init__(facade=True, **rest)

    def group(self):
        return self._group

    def locus(self):
        return self._locus

    def representatives(self):
        return finite_ordered_set(
            tuple(orbit.representative() for orbit in self)
        )

    def orbit_of(self, vector):
        if vector not in self.locus():
            raise ValueError("orbit_of expects a primitive isotropic vector of this lattice")
        for orbit in self:
            if vector in orbit:
                return orbit
        raise ArithmeticError("the exact isotropic orbit list did not cover the primitive isotropic locus")

    def stabilizer(self, representative):
        return self.orbit_of(representative).stabilizer()

    def transporter(self, source, target):
        if source not in self.locus() or target not in self.locus():
            raise ValueError("a primitive-isotropic transporter requires two vectors in the locus")
        return self.group().vector_equivalence_witness(source, target)


def _primitive_isotropic_vector_orbit_decomposition(group, locus):
    return _object_of(
        Sets().Finite(),
        _engine=(Sets(), _PrimitiveIsotropicVectorOrbitDecompositionEngine, None),
        group=group,
        locus=locus,
    )


class _IsotropicSublatticeLocusEngine:
    r"""Private set realization of isotropic sublattices of one fixed rank."""

    def __init__(self, lattice, rank, *, primitive=False, **rest) -> None:
        rank = int(rank)
        if rank <= 0:
            raise ValueError("an isotropic sublattice rank must be positive")
        self._lattice = lattice
        self._rank = rank
        self._primitive = bool(primitive)
        super().__init__(facade=True, **rest)

    def lattice(self):
        return self._lattice

    def rank(self):
        return self._rank

    def requires_primitive(self) -> bool:
        return self._primitive

    def __contains__(self, sublattice) -> bool:
        return (
            _is_lattice_subobject_of_rank(sublattice, self.lattice(), self.rank())
            and sublattice.is_totally_isotropic()
            and (not self.requires_primitive() or sublattice.is_primitive())
        )

    is_parent_of = __contains__

    def _element_constructor_(self, sublattice):
        if sublattice not in self:
            raise ValueError(f"{sublattice} is not in {self}")
        return sublattice

    def _repr_(self) -> str:
        qualifier = "primitive " if self.requires_primitive() else ""
        return (
            f"{qualifier}totally isotropic rank-{self.rank()} sublattices "
            f"of {self.lattice()}"
        )


class _PrimitiveIsotropicSublatticeLocusEngine(_IsotropicSublatticeLocusEngine):
    r"""The primitive locus, with its arithmetic-group orbit construction."""

    def orbit_decomposition(self, group):
        r"""Return the decomposition of this locus into ``group``-orbits, its cusps."""
        return _primitive_isotropic_sublattice_orbit_decomposition(group, self)


class _PrimitiveIsotropicSublatticeOrbitDecompositionEngine(_FiniteOrbitDecompositionSetEngine):
    r"""The finite cusp decomposition of one primitive isotropic sublattice locus."""

    def __init__(self, group, locus, **rest) -> None:
        if group.supergroup().domain() is not locus.lattice():
            raise ValueError("the orbit group and isotropic-sublattice locus require one lattice")
        self._group = group
        self._locus = locus
        self._orbits = group.cusps(rank=locus.rank())
        super().__init__(facade=True, **rest)

    def group(self):
        return self._group

    def locus(self):
        return self._locus

    def representatives(self):
        return finite_ordered_set(
            tuple(cusp.representative() for cusp in self)
        )

    def orbit_of(self, sublattice):
        if sublattice not in self.locus():
            raise ValueError("orbit_of expects a primitive isotropic sublattice in this locus")
        for cusp in self:
            if sublattice in cusp:
                return cusp
        raise ArithmeticError("the exact cusp list did not cover the isotropic-sublattice locus")

    def stabilizer(self, sublattice):
        return self.orbit_of(sublattice).stabilizer()

    def transporter(self, source, target):
        if source not in self.locus() or target not in self.locus():
            raise ValueError("an isotropic-sublattice transporter requires two locus members")
        return self.group().isotropic_equivalence_witness(source, target)


def _primitive_isotropic_sublattice_orbit_decomposition(group, locus):
    return _object_of(
        Sets().Finite(),
        _engine=(Sets(), _PrimitiveIsotropicSublatticeOrbitDecompositionEngine, None),
        group=group,
        locus=locus,
    )


class _IsotropicFlagLocusEngine:
    r"""Nested represented isotropic sublattices with prescribed ranks."""

    def __init__(self, lattice, ranks, **rest) -> None:
        ranks = tuple(int(rank) for rank in ranks)
        if not ranks or any(rank <= 0 for rank in ranks):
            raise ValueError("an isotropic flag requires positive term ranks")
        if any(left >= right for left, right in zip(ranks, ranks[1:])):
            raise ValueError("isotropic flag ranks must be strictly increasing")
        self._lattice = lattice
        self._ranks = ranks
        super().__init__(facade=True, **rest)

    def lattice(self):
        return self._lattice

    def ranks(self):
        return self._ranks

    def __contains__(self, flag) -> bool:
        match flag:
            case IsotropicFlag():
                terms = tuple(flag.terms())
            case tuple() | list():
                terms = tuple(flag)
            case _:
                return False
        if len(terms) != len(self.ranks()):
            return False
        if any(
            term not in _isotropic_sublattice_locus(self.lattice(), rank)
            for term, rank in zip(terms, self.ranks(), strict=True)
        ):
            return False
        return all(
            _factors_through(smaller.inclusion(), larger.inclusion())
            for smaller, larger in zip(terms, terms[1:])
        )

    is_parent_of = __contains__

    def _element_constructor_(self, flag):
        if flag not in self:
            raise ValueError(f"{flag} is not in {self}")
        return flag

    def _repr_(self) -> str:
        return f"Totally isotropic flags of ranks {self.ranks()} in {self.lattice()}"


def _primitive_isotropic_sublattice_locus(lattice, rank):
    return _object_of(
        Sets(),
        _engine=(Sets(), _PrimitiveIsotropicSublatticeLocusEngine, None),
        lattice=lattice,
        rank=rank,
        primitive=True,
    )


def _isotropic_sublattice_locus(lattice, rank):
    return _object_of(
        Sets(),
        _engine=(Sets(), _IsotropicSublatticeLocusEngine, None),
        lattice=lattice,
        rank=rank,
        primitive=False,
    )


def _isotropic_flag_locus(lattice, ranks):
    return _object_of(
        Sets(),
        _engine=(Sets(), _IsotropicFlagLocusEngine, None),
        lattice=lattice,
        ranks=tuple(ranks),
    )


class IsotropicFlag:
    r"""A primitive totally isotropic flag, recorded by its nested lattice subobjects."""

    def __init__(self, lattice, basis) -> None:
        self._lattice = lattice
        self._basis = tuple(_held(lattice, element) for element in basis)
        if not self._basis:
            raise ValueError("an isotropic flag requires a nonempty basis")
        self._terms = tuple(
            lattice.primitive_isotropic_subobject(*self._basis[: rank + 1])
            for rank in range(len(self._basis))
        )

    def lattice(self):
        return self._lattice

    def isotropic_basis(self):
        return self._basis

    def terms(self):
        return finite_ordered_set(self._terms)

    def flag_length(self):
        r"""Return how many terms this flag has.

        This counts the steps of the flag and is not a rank: the terms are
        subobjects of growing rank, and the flag's own invariant is how many
        of them there are.
        """
        return finite_ordered_set(self._terms).cardinality()

    def top(self):
        return self._terms[-1]

    def __repr__(self) -> str:
        return (
            f"Primitive totally isotropic flag of length {self.flag_length()} "
            f"in {self.lattice()}"
        )


class _CuspEngine:
    r"""One ``O(L)``-orbit of primitive totally isotropic subobjects of a rank.

    A cusp is the orbit itself, so membership is its primary operation:
    ``subobject in cusp`` asks the exact indefinite backend for an isometry
    carrying the stated subobject to this orbit and answers whether one
    exists.  ``representative`` is the member that backend chose, and
    ``transporter_witness`` returns one isometry realizing a membership.

    The set of primitive isotropic subobjects is infinite whenever the lattice
    is indefinite and isotropic, so this orbit is not a finite ``G``-set
    quotient and does not present its points.  What is finite is the number of
    cusps, which is why ``cusps`` enumerates them and no cusp enumerates its
    members.

    For rank one the stabilizer is the cusp's arithmetic group ``Gamma_v =
    P_v``, delivered as the representative's ``parabolic_subgroup``; its
    ``unipotent_radical`` and Eichler transvections describe the boundary
    component, and ``reduction_lattice`` is the lattice ``v^perp/v`` in which
    that component's reflection group acts.
    """

    def __init__(self, representative, **rest) -> None:
        self._representative = representative
        super().__init__(facade=True, **rest)

    def universe(self):
        return _primitive_isotropic_sublattice_locus(
            self.lattice(),
            self.module_rank(),
        )

    def lattice(self):
        return self._representative.ambient_lattice()

    def module_rank(self):
        return self._representative.module_rank()

    def representative(self):
        r"""Return the selected representative of this orbit."""
        return self._representative

    def parabolic_subgroup(self):
        r"""Return ``Gamma = Stab_{O(L)}(I)`` of the representative."""
        return self._representative.parabolic_subgroup()

    stabilizer = parabolic_subgroup

    def stabilizer_generators(self):
        r"""Return generators of the representative's stabilizer."""
        return self.lattice().Aut().isotropic_stabilizer_generators(
            self._representative
        )

    def reduction_lattice(self):
        r"""Return ``I^perp/I``, the lattice this boundary component acts in."""
        return self._representative.isotropic_reduction()

    def transporter_witness(self, subobject):
        r"""Return one ``g`` in ``O(L)`` carrying ``subobject`` to the representative.

        The full transporter is a coset of the subobject's own parabolic
        subgroup, infinite whenever that group is; one witness together with
        ``parabolic_subgroup`` presents it.
        """
        return subobject.transporter_witness_to(self._representative)

    def __contains__(self, subobject) -> bool:
        if subobject not in self.universe():
            return False
        return self.transporter_witness(subobject) is not None

    is_parent_of = __contains__

    def _element_constructor_(self, subobject):
        if subobject not in self:
            raise ValueError(f"{subobject} is not in {self}")
        return subobject

    def _repr_(self) -> str:
        return f"Cusp of rank {self.module_rank()} in {self.lattice()}"


class _ArithmeticCuspEngine:
    r"""One orbit of primitive isotropic subobjects under an arithmetic subgroup.

    The subgroup is part of the object.  Its stabilizer is therefore the
    actual intersection ``Gamma cap P_I``, not the full parabolic in
    ``O(L)``.  Membership retains an explicit transporter lying in ``Gamma``.
    """

    def __init__(self, subgroup, representative, **rest) -> None:
        if subgroup.supergroup().domain() is not representative.ambient_lattice():
            raise ValueError(
                "an arithmetic cusp subgroup and representative must belong to the same lattice"
            )
        self._subgroup = subgroup
        self._representative = representative
        super().__init__(facade=True, **rest)

    def universe(self):
        return _primitive_isotropic_sublattice_locus(
            self.lattice(),
            self.module_rank(),
        )

    def subgroup(self):
        return self._subgroup

    def lattice(self):
        return self.subgroup().supergroup().domain()

    def module_rank(self):
        return self.representative().module_rank()

    def representative(self):
        return self._representative

    def stabilizer(self):
        r"""Return ``Gamma cap P_I`` for the chosen representative ``I``."""
        from dzack_research.preamble.categories.group.predicate_subgroups import (
            StabilizerSubgroups,
        )

        parabolic = self.representative().parabolic_subgroup()
        return StabilizerSubgroups(self.subgroup())(
            self.representative(),
            "setwise on the represented isotropic sublattice",
            lambda element: element in parabolic,
        )

    parabolic_subgroup = stabilizer

    def reduction_lattice(self):
        return self.representative().isotropic_reduction()

    def transporter_witness(self, subobject):
        r"""Return one ``g in Gamma`` carrying ``subobject`` to the representative."""
        return self.subgroup().isotropic_equivalence_witness(
            subobject,
            self.representative(),
        )

    def __contains__(self, subobject) -> bool:
        if subobject not in self.universe():
            return False
        return self.transporter_witness(subobject) is not None

    is_parent_of = __contains__

    def _element_constructor_(self, subobject):
        if subobject not in self:
            raise ValueError(f"{subobject} is not in {self}")
        return subobject

    def _repr_(self) -> str:
        return (
            f"Rank-{self.module_rank()} cusp of {self.subgroup()} "
            f"in {self.lattice()}"
        )


def _cusp(representative):
    return _object_of(
        Sets(),
        _engine=(Sets(), _CuspEngine, None),
        representative=representative,
    )


def _arithmetic_cusp(subgroup, representative):
    return _object_of(
        Sets(),
        _engine=(Sets(), _ArithmeticCuspEngine, None),
        subgroup=subgroup,
        representative=representative,
    )


class CuspIncidence(SageObject):
    r"""One rank-``(1,2)`` isotropic flag orbit in the quotient Tits building.

    The edge is not reduced to two vertex labels: it retains an actual flag
    ``I_1 < I_2`` in the lattice, the line and plane cusp orbits containing
    its two terms, transporters from those terms to the chosen cusp
    representatives, and generators of the stabilizer of the whole flag.
    Distinct flag orbits with the same pair of cusp vertices therefore remain
    distinct incidence records.
    """

    def __init__(
        self,
        flag,
        line_cusp,
        plane_cusp,
        line_transporter,
        plane_transporter,
        stabilizer_generators,
    ) -> None:
        terms = tuple(flag.terms())
        if len(terms) != 2:
            raise ValueError("a cusp incidence is represented by a two-step isotropic flag")
        if int(terms[0].module_rank()) != 1 or int(terms[1].module_rank()) != 2:
            raise ValueError("a cusp incidence has ranks one and two")
        terms[0].inclusion().factor_through(terms[1].inclusion())
        self._flag = flag
        self._line_cusp = line_cusp
        self._plane_cusp = plane_cusp
        self._line_transporter = line_transporter
        self._plane_transporter = plane_transporter
        self._stabilizer_generators = stabilizer_generators

    def lattice(self):
        return self._flag.lattice()

    def flag(self):
        return self._flag

    def line(self):
        return self.flag().terms()[0]

    def plane(self):
        return self.flag().terms()[1]

    def line_cusp(self):
        return self._line_cusp

    def plane_cusp(self):
        return self._plane_cusp

    def line_transporter(self):
        return self._line_transporter

    def plane_transporter(self):
        return self._plane_transporter

    def stabilizer_generators(self):
        return self._stabilizer_generators

    def __repr__(self) -> str:
        return f"Tits-building incidence {self.line_cusp()} < {self.plane_cusp()}"


class ArithmeticCuspIncidence(SageObject):
    r"""One rank-``(1,2)`` flag orbit in an arithmetic-subgroup quotient building."""

    def __init__(
        self,
        subgroup,
        flag,
        line_cusp,
        plane_cusp,
        line_transporter,
        plane_transporter,
    ) -> None:
        terms = tuple(flag.terms())
        if len(terms) != 2:
            raise ValueError(
                "an arithmetic cusp incidence is represented by a two-step isotropic flag"
            )
        line, plane = terms
        if int(line.module_rank()) != 1 or int(plane.module_rank()) != 2:
            raise ValueError("an arithmetic cusp incidence has ranks one and two")
        line.inclusion().factor_through(plane.inclusion())
        if line_cusp.subgroup() is not subgroup or plane_cusp.subgroup() is not subgroup:
            raise ValueError("both cusp vertices must belong to the selected subgroup quotient")
        if line_transporter not in subgroup or plane_transporter not in subgroup:
            raise ValueError("cusp transporters must lie in the selected arithmetic subgroup")
        if not _same_subobject(
            line_transporter.transport_isotropic_object(line),
            line_cusp.representative(),
        ):
            raise ValueError("the retained line transporter has the wrong target cusp")
        if not _same_subobject(
            plane_transporter.transport_isotropic_object(plane),
            plane_cusp.representative(),
        ):
            raise ValueError("the retained plane transporter has the wrong target cusp")
        self._subgroup = subgroup
        self._flag = flag
        self._line_cusp = line_cusp
        self._plane_cusp = plane_cusp
        self._line_transporter = line_transporter
        self._plane_transporter = plane_transporter

    def subgroup(self):
        return self._subgroup

    def lattice(self):
        return self.subgroup().supergroup().domain()

    def flag(self):
        return self._flag

    def line(self):
        return self.flag().terms()[0]

    def plane(self):
        return self.flag().terms()[1]

    def line_cusp(self):
        return self._line_cusp

    def plane_cusp(self):
        return self._plane_cusp

    def line_transporter(self):
        return self._line_transporter

    def plane_transporter(self):
        return self._plane_transporter

    def stabilizer(self):
        r"""Return the subgroup of ``Gamma`` preserving both terms of the flag."""
        from dzack_research.preamble.categories.group.predicate_subgroups import (
            StabilizerSubgroups,
        )

        line_stabilizer = self.line().parabolic_subgroup()
        plane_stabilizer = self.plane().parabolic_subgroup()
        return StabilizerSubgroups(self.subgroup())(
            self.flag(),
            "setwise on both terms of the isotropic flag",
            lambda element: element in line_stabilizer and element in plane_stabilizer,
        )

    def __repr__(self) -> str:
        return (
            f"Arithmetic Tits-building incidence "
            f"{self.line_cusp()} < {self.plane_cusp()}"
        )


def _embedded_basis(subobject):
    inclusion = subobject.inclusion()
    return tuple(inclusion(generator) for generator in subobject.module_generators())


def _basis_rows(obj, flag):
    match flag:
        case True:
            basis = obj.isotropic_basis()
        case False:
            basis = _embedded_basis(obj)
    rows = []
    for element in basis:
        parent = element.parent()
        coefficients = parent.framing_coefficients(element)
        rows.append(
            [
                int(coefficients.get(label, parent.base_ring().zero()))
                for label in parent.module_generating_set()
            ]
        )
    return rows


def _terms(obj, flag):
    match flag:
        case True:
            return tuple(obj.terms())
        case False:
            return (obj,)


def _factors_through(inclusion, target_inclusion) -> bool:
    r"""Whether the image of ``inclusion`` lies in the image of ``target_inclusion``."""
    source = inclusion.domain()
    return all(
        target_inclusion.is_in_image(inclusion(source.module_generator(label)))
        for label in source.module_generating_set()
    )


def _same_subobject(left, right) -> bool:
    return (
        left.inclusion().codomain() is right.inclusion().codomain()
        and _factors_through(left.inclusion(), right.inclusion())
        and _factors_through(right.inclusion(), left.inclusion())
    )


def _gram_rows(lattice):
    rank = int(lattice.module_rank())
    return [
        [int(lattice.gram_tensor()[i, j]) for j in range(rank)]
        for i in range(rank)
    ]


def _isotropic_orbit_representatives(orthogonal_group, rank, *, flag=False):
    r"""Return full-``O(L)`` orbit representatives of primitive isotropic subobjects/flags."""
    lattice = orthogonal_group.domain()
    rank = lattice.base_ring()(rank)
    if rank <= lattice.base_ring().zero():
        raise ValueError("an isotropic orbit rank must be positive")
    nature = "flag" if flag else "plane"
    result = []
    for block in engine_capabilities.compute(
        "lattice.indefinite_isotropic_subspace_orbits",
        _gram_rows(lattice),
        int(rank),
        nature,
    ):
        basis = tuple(
            lattice.linear_combination(
                {
                    label: lattice.base_ring()(int(coefficient))
                    for label, coefficient in zip(
                        lattice.module_generating_set(), row, strict=True
                    )
                    if coefficient
                }
            )
            for row in block
        )
        if len(basis) != int(rank):
            raise ArithmeticError("the isotropic-orbit backend returned a basis of the wrong rank")
        result.append(
            IsotropicFlag(lattice, basis)
            if flag
            else lattice.primitive_isotropic_subobject(*basis)
        )
    return finite_ordered_set(tuple(result))


def _isotropic_equivalence_witness(orthogonal_group, left, right, *, flag=False):
    r"""Return an isometry carrying one primitive isotropic subobject/flag to another."""
    lattice = orthogonal_group.domain()
    if flag:
        left_terms = _terms(left, flag)
        right_terms = _terms(right, flag)
        if len(left_terms) != len(right_terms):
            return None
        if all(
            _same_subobject(source, target)
            for source, target in zip(left_terms, right_terms, strict=True)
        ):
            return orthogonal_group.one()
    elif _same_subobject(left, right):
        return orthogonal_group.one()
    left_rows = _basis_rows(left, flag)
    right_rows = _basis_rows(right, flag)
    if len(left_rows) != len(right_rows):
        return None
    nature = "flag" if flag else "plane"
    witness = engine_capabilities.compute(
        "lattice.indefinite_isotropic_subspace_isometry_witness",
        _gram_rows(lattice),
        left_rows,
        right_rows,
        choice=nature,
    )
    if witness is None:
        return None
    isometry = orthogonal_group(tuple(lattice(tuple(row)) for row in witness))
    left_terms = _terms(left, flag)
    right_terms = _terms(right, flag)
    checked_left = left_terms if flag else left_terms[-1:]
    checked_right = right_terms if flag else right_terms[-1:]
    if any(
        not _same_subobject(isometry.transport_isotropic_object(source), target)
        for source, target in zip(checked_left, checked_right, strict=True)
    ):
        raise ArithmeticError("the isotropic-equivalence backend returned a witness with the wrong subobject action")
    return isometry


def _isotropic_stabilizer_generators(orthogonal_group, obj, *, flag=False):
    r"""Return generators of the full-orthogonal-group stabilizer of an isotropic subobject/flag."""
    lattice = orthogonal_group.domain()
    nature = "flag" if flag else "plane"
    isometries = finite_ordered_set(
        tuple(
            orthogonal_group(tuple(lattice(tuple(row)) for row in rows))
            for rows in engine_capabilities.compute(
                "lattice.indefinite_isotropic_subspace_stabilizer",
                _gram_rows(lattice),
                _basis_rows(obj, flag),
                choice=nature,
            )
        )
    )
    terms = _terms(obj, flag)
    checked = terms if flag else terms[-1:]
    if any(
        not _same_subobject(isometry.transport_isotropic_object(term), term)
        for isometry in isometries
        for term in checked
    ):
        raise ArithmeticError("an isotropic-stabilizer backend isometry moves a subobject it must preserve")
    return isometries


__all__ = [
    "ArithmeticCuspIncidence",
    "CuspIncidence",
    "IsotropicFlag",
]
