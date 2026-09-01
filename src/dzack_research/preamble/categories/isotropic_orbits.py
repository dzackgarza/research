r"""Primitive totally isotropic sublattices, flags, and full-orthogonal-group orbits."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.tensors import tensor


def _held(lattice, element):
    return element if getattr(element, "parent", lambda: None)() is lattice else lattice(element)


def primitive_isotropic_subobject(lattice, basis):
    r"""Return the primitive totally isotropic sublattice spanned by ``basis``."""
    elements = tuple(_held(lattice, element) for element in basis)
    if not elements:
        raise ValueError("an isotropic sublattice requires a nonempty basis")
    if any(lattice.b(left, right) != 0 for left in elements for right in elements):
        raise ValueError("the stated basis is not totally isotropic")
    rows = tensor.matrix(SageZZ, [element.to_list() for element in elements])
    if rows.rank() != len(elements):
        raise ValueError("the stated isotropic basis is linearly dependent")
    subobject = lattice.subobject_on(elements)
    if subobject.rank() != len(elements):
        raise ArithmeticError("the represented isotropic subobject has the wrong rank")
    if not subobject.is_primitive():
        raise ValueError("the isotropic sublattice must be primitive")
    return subobject


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

    def rank(self):
        return SageZZ(len(self._terms))

    def top(self):
        return self._terms[-1]

    def __repr__(self) -> str:
        return f"Primitive totally isotropic flag of rank {self.rank()} in {self.lattice()}"


def _embedded_basis(subobject):
    inclusion = subobject.inclusion()
    return tuple(inclusion(generator) for generator in subobject.module_generators())


def _basis_rows(obj):
    basis = obj.basis() if isinstance(obj, IsotropicFlag) else _embedded_basis(obj)
    return [[SageZZ(entry) for entry in element.to_list()] for element in basis]


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


def _image_subobject(lattice, isometry, subobject):
    return lattice.subobject_on(
        tuple(
            isometry(subobject.inclusion()(generator))
            for generator in subobject.module_generators()
        )
    )


def transport_isotropic_object(isometry, obj):
    r"""Transport a primitive isotropic subobject or flag along a lattice isometry."""
    lattice = isometry.codomain()
    if isinstance(obj, IsotropicFlag):
        return IsotropicFlag(lattice, tuple(isometry(element) for element in obj.basis()))
    return primitive_isotropic_subobject(
        lattice,
        tuple(isometry(element) for element in _embedded_basis(obj)),
    )


def _gram_rows(lattice):
    rank = int(lattice.rank())
    return [
        [SageZZ(lattice.gram_tensor()[i, j]) for j in range(rank)]
        for i in range(rank)
    ]


def isotropic_orbit_representatives(orthogonal_group, rank, *, flag=False):
    r"""Return full-``O(L)`` orbit representatives of primitive isotropic subobjects/flags."""
    lattice = orthogonal_group.domain()
    rank = SageZZ(rank)
    if rank <= 0:
        raise ValueError("an isotropic orbit rank must be positive")
    from py_polyhedral.binaries import indefinite_form_isotropic_k_stuff

    nature = "flag" if flag else "plane"
    result = []
    for block in indefinite_form_isotropic_k_stuff(_gram_rows(lattice), int(rank), nature):
        basis = tuple(
            lattice.linear_combination(
                {
                    label: SageZZ(coefficient)
                    for label, coefficient in zip(
                        lattice.module_generating_set(), row, strict=True
                    )
                    if coefficient
                }
            )
            for row in block
        )
        if len(basis) != rank:
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
    left_rows = _basis_rows(left)
    right_rows = _basis_rows(right)
    if len(left_rows) != len(right_rows):
        return None
    from py_polyhedral.binaries import (
        indefinite_form_test_equivalence_isotropic_k_plane,
    )

    nature = "flag" if flag else "plane"
    witness = indefinite_form_test_equivalence_isotropic_k_plane(
        _gram_rows(lattice), left_rows, right_rows, choice=nature
    )
    if witness is None:
        return None
    isometry = orthogonal_group._from_backend_row_action(witness)
    left_terms = _terms(left)
    right_terms = _terms(right)
    checked_left = left_terms if flag else left_terms[-1:]
    checked_right = right_terms if flag else right_terms[-1:]
    if any(
        not _same_subobject(_image_subobject(lattice, isometry, source), target)
        for source, target in zip(checked_left, checked_right, strict=True)
    ):
        raise ArithmeticError("the isotropic-equivalence backend returned a witness with the wrong subobject action")
    return isometry


def isotropic_stabilizer_generators(orthogonal_group, obj, *, flag=False):
    r"""Return generators of the full-orthogonal-group stabilizer of an isotropic subobject/flag."""
    lattice = orthogonal_group.domain()
    from py_polyhedral.binaries import indefinite_form_stabilizer_isotropic_subspace

    nature = "flag" if flag else "plane"
    generators = tuple(
        orthogonal_group._from_backend_row_action(rows)
        for rows in indefinite_form_stabilizer_isotropic_subspace(
            _gram_rows(lattice), _basis_rows(obj), choice=nature
        )
    )
    terms = _terms(obj)
    checked = terms if flag else terms[-1:]
    if any(
        not _same_subobject(_image_subobject(lattice, generator, term), term)
        for generator in generators
        for term in checked
    ):
        raise ArithmeticError("an isotropic-stabilizer backend generator moves a subobject it must preserve")
    return generators


__all__ = [
    "IsotropicFlag",
    "isotropic_equivalence_witness",
    "isotropic_orbit_representatives",
    "isotropic_stabilizer_generators",
    "primitive_isotropic_subobject",
    "transport_isotropic_object",
]
