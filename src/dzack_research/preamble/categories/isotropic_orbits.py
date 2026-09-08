r"""Primitive totally isotropic sublattices, flags, and full-orthogonal-group orbits.

The orbit representatives, the equivalence witness and the stabilizer are
mathematical operations of this file; the algorithm realizing each one is
asked for by name from the ordered capability layer, so no engine is named
here.  An operation no registered provider supplies refuses by naming its
capability and what would provision it, which is the owned behaviour until a
provider arrives.
"""

from sage.structure.sage_object import SageObject

from dzack_research.preamble.engine_capabilities import engine_capabilities
from dzack_research.preamble.tensors.tensor import tensor
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import ConditionSet


def _held(lattice, element):
    return element if getattr(element, "parent", lambda: None)() is lattice else lattice(element)


def primitive_isotropic_subobject(lattice, basis):
    r"""Return the primitive totally isotropic sublattice spanned by ``basis``.

    The subobject is admitted to ``PrimitiveIsotropicSubobjects``, so every
    orbit representative produced here carries the parabolic subgroup, the
    Levi restrictions and the Eichler transvections of its own cusp.
    """
    from dzack_research.preamble.categories.isotropic_parabolics import (
        primitive_isotropic,
    )

    elements = tuple(_held(lattice, element) for element in basis)
    assert elements, "an isotropic sublattice is spanned by a nonempty family"
    subobject = primitive_isotropic(lattice, elements)
    assert subobject.module_rank() == finite_ordered_set(elements).cardinality(), (
        "the stated isotropic family is linearly dependent, so it does not "
        "frame the sublattice it spans"
    )
    return subobject


class PrimitiveIsotropicVectorLocus(SageObject):
    r"""The exact locus of nonzero primitive isotropic vectors in one lattice."""

    def __init__(self, lattice) -> None:
        self._lattice = lattice
        zero = lattice.zero()
        value_zero = lattice.base_ring().zero()

        def is_primitive_isotropic(vector) -> bool:
            if vector == zero:
                return False
            if lattice.q(vector) != value_zero:
                return False
            return bool(lattice.subobject_on((vector,)).is_primitive())

        self._condition_set = ConditionSet(lattice, is_primitive_isotropic)

    def lattice(self):
        return self._lattice

    def universe(self):
        return self.lattice()

    def condition_set(self):
        return self._condition_set

    def __contains__(self, vector) -> bool:
        return vector in self.condition_set()

    def __repr__(self) -> str:
        return f"Primitive isotropic vectors of {self.lattice()}"


def primitive_isotropic_vectors(lattice):
    r"""Return the exact primitive-isotropic-vector locus of ``lattice``.

    Membership is ``q(v) = 0`` together with the saturation of ``Z v``, which
    is the statement ``div(v) = 1`` in ``Z v``: the vector is not a proper
    multiple of another lattice vector.  Both conditions are decided from
    their definitions, so the set is exact.

    For an indefinite isotropic lattice this set is countably infinite, so it
    is presented by its membership and not by an enumeration.  Its ``O(L)``
    orbits are the cusps, and they are finite in number; representatives come
    from ``L.O().isotropic_orbit_representatives(1)``.
    """
    return PrimitiveIsotropicVectorLocus(lattice)


class PrimitiveIsotropicVectorOrbit(SageObject):
    r"""One ``O(L)``-orbit inside the primitive isotropic vector locus."""

    def __init__(self, group, representative) -> None:
        self._group = group
        self._representative = representative

    def group(self):
        return self._group

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
        return self.transporter_from(vector) is not None


class PrimitiveIsotropicVectorOrbitDecomposition(SageObject):
    r"""The finite ``O(L)``-orbit decomposition of primitive isotropic vectors.

    Rank-one primitive isotropic sublattice orbits and primitive isotropic
    vector orbits coincide for the full orthogonal group: a line generator can
    only be sent to either generator of the target primitive line, and ``-id``
    belongs to ``O(L)``.  Thus the existing exact rank-one isotropic backend
    supplies the representatives, while vector stabilizers and transporters
    remain the already-owned group operations.
    """

    def __init__(self, group, locus) -> None:
        if not isinstance(locus, PrimitiveIsotropicVectorLocus):
            raise TypeError("this decomposition requires the primitive isotropic vector locus")
        if group.lattice() is not locus.lattice():
            raise ValueError("the orbit group and primitive-isotropic locus require one lattice")
        self._group = group
        self._locus = locus
        representatives = []
        for line in group.isotropic_orbit_representatives(1):
            generator = line.module_generator(0)
            representatives.append(line.inclusion()(generator))
        self._orbits = finite_ordered_set(
            tuple(
                PrimitiveIsotropicVectorOrbit(group, representative)
                for representative in representatives
            )
        )

    def group(self):
        return self._group

    def locus(self):
        return self._locus

    def orbits(self):
        return self._orbits

    def representatives(self):
        return finite_ordered_set(
            tuple(orbit.representative() for orbit in self.orbits())
        )

    def orbit_of(self, vector):
        if vector not in self.locus():
            raise ValueError("orbit_of expects a primitive isotropic vector of this lattice")
        for orbit in self.orbits():
            if vector in orbit:
                return orbit
        raise ArithmeticError("the exact isotropic orbit list did not cover the primitive isotropic locus")

    def stabilizer(self, representative):
        return self.orbit_of(representative).stabilizer()

    def transporter(self, source, target):
        if source not in self.locus() or target not in self.locus():
            raise ValueError("a primitive-isotropic transporter requires two vectors in the locus")
        return self.group().vector_equivalence_witness(source, target)


class PrimitiveIsotropicSublatticeLocus(SageObject):
    r"""Primitive totally isotropic rank-``k`` lattice subobjects of ``L``."""

    def __init__(self, lattice, rank) -> None:
        rank = int(rank)
        if rank <= 0:
            raise ValueError("a primitive isotropic sublattice rank must be positive")
        self._lattice = lattice
        self._rank = rank

    def lattice(self):
        return self._lattice

    def rank(self):
        return self._rank

    def __contains__(self, sublattice) -> bool:
        from dzack_research.preamble.categories.modules.pure.modules import (
            ModuleSubobjects,
        )

        if not callable(getattr(sublattice, "inclusion", None)):
            return False
        if sublattice not in ModuleSubobjects(self.lattice().base_ring()):
            return False
        try:
            if sublattice.ambient_lattice() is not self.lattice():
                return False
        except (AttributeError, TypeError):
            return False
        return (
            int(sublattice.module_rank()) == self.rank()
            and sublattice.is_primitive()
            and sublattice.is_totally_isotropic()
        )

    def __repr__(self) -> str:
        return (
            f"Primitive totally isotropic rank-{self.rank()} sublattices "
            f"of {self.lattice()}"
        )


def primitive_isotropic_sublattices(lattice, rank=1):
    r"""Return the exact rank-``rank`` primitive isotropic sublattice locus."""
    return PrimitiveIsotropicSublatticeLocus(lattice, rank)


class PrimitiveIsotropicSublatticeOrbitDecomposition(SageObject):
    r"""The finite cusp decomposition of one primitive isotropic sublattice locus."""

    def __init__(self, group, locus) -> None:
        if not isinstance(locus, PrimitiveIsotropicSublatticeLocus):
            raise TypeError("this decomposition requires a primitive isotropic sublattice locus")
        if group.lattice() is not locus.lattice():
            raise ValueError("the orbit group and isotropic-sublattice locus require one lattice")
        self._group = group
        self._locus = locus
        self._orbits = cusps(locus.lattice(), rank=locus.rank())

    def group(self):
        return self._group

    def locus(self):
        return self._locus

    def orbits(self):
        return self._orbits

    def representatives(self):
        return finite_ordered_set(
            tuple(cusp.representative() for cusp in self.orbits())
        )

    def orbit_of(self, sublattice):
        if sublattice not in self.locus():
            raise ValueError("orbit_of expects a primitive isotropic sublattice in this locus")
        for cusp in self.orbits():
            if sublattice in cusp:
                return cusp
        raise ArithmeticError("the exact cusp list did not cover the isotropic-sublattice locus")

    def stabilizer(self, sublattice):
        return self.group().stabilizer(sublattice, action="setwise")

    def transporter(self, source, target):
        if source not in self.locus() or target not in self.locus():
            raise ValueError("an isotropic-sublattice transporter requires two locus members")
        return self.group().isotropic_equivalence_witness(source, target)


class IsotropicFlag:
    r"""A primitive totally isotropic flag, recorded by its nested lattice subobjects."""

    def __init__(self, lattice, basis) -> None:
        self._lattice = lattice
        self._basis = tuple(_held(lattice, element) for element in basis)
        if not self._basis:
            raise ValueError("an isotropic flag requires a nonempty basis")
        self._terms = tuple(
            primitive_isotropic_subobject(lattice, self._basis[: rank + 1])
            for rank in range(len(self._basis))
        )

    def lattice(self):
        return self._lattice

    def basis(self):
        return self._basis

    def terms(self):
        return self._terms

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


class Cusp:
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

    def __init__(self, representative) -> None:
        self._representative = representative

    def lattice(self):
        return self._representative.ambient_lattice()

    def module_rank(self):
        return self._representative.module_rank()

    def representative(self):
        r"""Return the member of this orbit the backend chose."""
        return self._representative

    def parabolic_subgroup(self):
        r"""Return ``Gamma = Stab_{O(L)}(I)`` of the representative."""
        return self._representative.parabolic_subgroup()

    def stabilizer_generators(self):
        r"""Return backend generators of the representative's stabilizer."""
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
        assert subobject.ambient_lattice() is self.lattice(), (
            "a cusp decides membership for isotropic subobjects of its own lattice"
        )
        if subobject.module_rank() != self.module_rank():
            return False
        return self.transporter_witness(subobject) is not None

    def __repr__(self) -> str:
        return f"Cusp of rank {self.module_rank()} in {self.lattice()}"


def cusps(lattice, rank=1):
    r"""Return the cusps of ``lattice``: its ``O(L)``-orbits of rank-``k`` subobjects.

    The orbits are finite in number and come back as an ordered set, each
    carrying its representative, that representative's parabolic subgroup and
    stabilizer generators, and the transporter witnessing any membership.  For
    rank one these are the zero-dimensional cusps of the arithmetic quotient,
    for rank two the one-dimensional ones.
    """
    return finite_ordered_set(
        tuple(
            Cusp(representative)
            for representative in lattice.Aut().isotropic_orbit_representatives(rank)
        )
    )


def _embedded_basis(subobject):
    inclusion = subobject.inclusion()
    return tuple(inclusion(generator) for generator in subobject.module_generators())


def _basis_rows(obj):
    basis = obj.basis() if isinstance(obj, IsotropicFlag) else _embedded_basis(obj)
    return [[int(entry) for entry in element.to_list()] for element in basis]


def _terms(obj):
    return obj.terms() if isinstance(obj, IsotropicFlag) else (obj,)


def _same_subobject(left, right) -> bool:
    if left.inclusion().codomain() is not right.inclusion().codomain():
        return False
    try:
        left.inclusion().factor_through(right.inclusion())
        right.inclusion().factor_through(left.inclusion())
    except ValueError:
        return False
    return True


def _image_subobject(isometry, subobject):
    return (isometry * subobject.inclusion()).image()


def transport_isotropic_object(isometry, obj):
    r"""Transport a primitive isotropic subobject or flag along a lattice isometry."""
    lattice = isometry.codomain()
    if isinstance(obj, IsotropicFlag):
        return IsotropicFlag(lattice, tuple(isometry(element) for element in obj.basis()))
    return _image_subobject(isometry, obj)


def _gram_rows(lattice):
    rank = int(lattice.module_rank())
    return [
        [int(lattice.gram_tensor()[i, j]) for j in range(rank)]
        for i in range(rank)
    ]


def isotropic_orbit_representatives(orthogonal_group, rank, *, flag=False):
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
            else primitive_isotropic_subobject(lattice, basis)
        )
    return tuple(result)


def isotropic_equivalence_witness(orthogonal_group, left, right, *, flag=False):
    r"""Return an isometry carrying one primitive isotropic subobject/flag to another."""
    lattice = orthogonal_group.domain()
    if flag:
        left_terms = _terms(left)
        right_terms = _terms(right)
        if len(left_terms) != len(right_terms):
            return None
        if all(
            _same_subobject(source, target)
            for source, target in zip(left_terms, right_terms, strict=True)
        ):
            return orthogonal_group.one()
    elif _same_subobject(left, right):
        return orthogonal_group.one()
    left_rows = _basis_rows(left)
    right_rows = _basis_rows(right)
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
    isometry = orthogonal_group._from_backend_row_action(witness)
    left_terms = _terms(left)
    right_terms = _terms(right)
    checked_left = left_terms if flag else left_terms[-1:]
    checked_right = right_terms if flag else right_terms[-1:]
    if any(
        not _same_subobject(_image_subobject(isometry, source), target)
        for source, target in zip(checked_left, checked_right, strict=True)
    ):
        raise ArithmeticError("the isotropic-equivalence backend returned a witness with the wrong subobject action")
    return isometry


def isotropic_stabilizer_generators(orthogonal_group, obj, *, flag=False):
    r"""Return generators of the full-orthogonal-group stabilizer of an isotropic subobject/flag."""
    lattice = orthogonal_group.domain()
    nature = "flag" if flag else "plane"
    isometries = finite_ordered_set(
        tuple(
            orthogonal_group._from_backend_row_action(rows)
            for rows in engine_capabilities.compute(
                "lattice.indefinite_isotropic_subspace_stabilizer",
                _gram_rows(lattice),
                _basis_rows(obj),
                choice=nature,
            )
        )
    )
    terms = _terms(obj)
    checked = terms if flag else terms[-1:]
    if any(
        not _same_subobject(_image_subobject(isometry, term), term)
        for isometry in isometries
        for term in checked
    ):
        raise ArithmeticError("an isotropic-stabilizer backend isometry moves a subobject it must preserve")
    return isometries


__all__ = [
    "Cusp",
    "IsotropicFlag",
    "PrimitiveIsotropicSublatticeLocus",
    "PrimitiveIsotropicSublatticeOrbitDecomposition",
    "PrimitiveIsotropicVectorLocus",
    "PrimitiveIsotropicVectorOrbit",
    "PrimitiveIsotropicVectorOrbitDecomposition",
    "cusps",
    "isotropic_equivalence_witness",
    "isotropic_orbit_representatives",
    "isotropic_stabilizer_generators",
    "primitive_isotropic_subobject",
    "primitive_isotropic_sublattices",
    "primitive_isotropic_vectors",
    "transport_isotropic_object",
]
