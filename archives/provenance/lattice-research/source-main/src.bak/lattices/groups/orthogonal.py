from __future__ import annotations

from dataclasses import dataclass

from sage.all import QQ, ZZ, Integer, MatrixSpace, matrix, vector
from sage.sets.condition_set import ConditionSet as _ConditionSet
from src.lattices.core.elements import FreeBilinearModuleElement


def _as_coordinate_vector(value):
    if isinstance(value, FreeBilinearModuleElement):
        return vector(QQ, value.to_vector())
    return vector(QQ, value)


def _acts_trivially_on_discriminant(lattice, M) -> bool:
    candidate = matrix(ZZ, M)
    for generator in lattice.discriminant_group().gens():
        lift_vector = generator.lift().to_primal_coordinates()
        diff = candidate * lift_vector - lift_vector
        if vector(QQ, diff).denominator() != 1:
            return False
    return True


@dataclass(frozen=True)
class _FiniteQuotientPresentation:
    determinant_kernel: bool = False
    positive_spinor_kernel: bool = False
    discriminant_preimages: tuple = ()

    def is_ambient(self) -> bool:
        return not self.determinant_kernel and not self.positive_spinor_kernel and not self.discriminant_preimages


def _dedupe_subgroups(subgroups):
    deduped = []
    for subgroup in subgroups:
        if subgroup not in deduped:
            deduped.append(subgroup)
    return tuple(deduped)


def _combine_presentations(left, right):
    if left is None or right is None:
        return None
    return _FiniteQuotientPresentation(
        determinant_kernel=left.determinant_kernel or right.determinant_kernel,
        positive_spinor_kernel=left.positive_spinor_kernel or right.positive_spinor_kernel,
        discriminant_preimages=_dedupe_subgroups((*left.discriminant_preimages, *right.discriminant_preimages)),
    )


class _LatticeOrthogonalSet:
    def __init__(self, lattice, condition_set, *, gens_fn, finite_quotient_presentation):
        self._lattice = lattice
        self._condition_set = condition_set
        self._gens_fn = gens_fn
        self._gens_cache = None
        self._finite_quotient_spec = finite_quotient_presentation

    @property
    def lattice(self):
        return self._lattice

    @property
    def condition_set(self):
        return self._condition_set

    def _finite_quotient_presentation(self):
        return self._finite_quotient_spec

    def gens(self):
        if self._gens_cache is None:
            assert self._gens_fn is not None, "Generator computation requires an explicit generator function"
            self._gens_cache = list(self._gens_fn())
        return list(self._gens_cache)

    def __contains__(self, value):
        return value in self._condition_set

    def act(self, G, value):
        return matrix(ZZ, G) * _as_coordinate_vector(value)

    def subgroup(self, gens_fn=None, predicate=None):
        return LatticeOrthogonalSubgroup(self, gens_fn=gens_fn, predicate=predicate, finite_quotient_presentation=None)

    def __and__(self, other):
        assert self._lattice is other.lattice, "Orthogonal subgroup operations require a common lattice"
        return LatticeOrthogonalSubgroup._from_condition_set(
            self._lattice,
            self._condition_set & other.condition_set,
            finite_quotient_presentation=_combine_presentations(
                self._finite_quotient_presentation(),
                other._finite_quotient_presentation(),
            ),
        )

    def __or__(self, other):
        assert self._lattice is other.lattice, "Orthogonal subgroup operations require a common lattice"
        return LatticeOrthogonalSubgroup._from_condition_set(
            self._lattice,
            self._condition_set | other.condition_set,
            finite_quotient_presentation=None,
        )

    def _structured_subgroup(self, predicate, *, finite_quotient_presentation, gens_fn=None):
        condition = self._condition_set & _ConditionSet(MatrixSpace(ZZ, self._lattice.rank()), predicate)
        return LatticeOrthogonalSubgroup._from_condition_set(
            self._lattice,
            condition,
            gens_fn=gens_fn,
            finite_quotient_presentation=_combine_presentations(
                self._finite_quotient_presentation(),
                finite_quotient_presentation,
            ),
        )

    def special_orthogonal_subgroup(self):
        return self._structured_subgroup(
            lambda M: Integer(M.det()) == 1,
            finite_quotient_presentation=_FiniteQuotientPresentation(determinant_kernel=True),
        )

    def plus_subgroup(self):
        from src.backends.dawes_orbit_backend import real_spinor_norm_sign

        return self._structured_subgroup(
            lambda M, _lattice=self._lattice: real_spinor_norm_sign(_lattice, M) == 1,
            finite_quotient_presentation=_FiniteQuotientPresentation(positive_spinor_kernel=True),
        )

    def special_plus_subgroup(self):
        return self.special_orthogonal_subgroup().plus_subgroup()

    def preimage_of_discriminant_subgroup(self, subgroup):
        from src.backends.dawes_orbit_backend import induced_discriminant_action

        return self._structured_subgroup(
            lambda M, _lattice=self._lattice, _subgroup=subgroup: induced_discriminant_action(_lattice, M) in _subgroup,
            finite_quotient_presentation=_FiniteQuotientPresentation(discriminant_preimages=(subgroup,)),
        )

    def stabilizer(self, value):
        from sage.all import vector as sage_vector
        from src.backends.external.py_polyhedral import indefinite_form_stabilizer_vector

        target = sage_vector(ZZ, list(_as_coordinate_vector(value)))
        raw_value = [int(entry) for entry in target]

        def _stab_vec_gens():
            return self._lattice._matrices_from_raw(indefinite_form_stabilizer_vector(self._lattice._gram_rows(), raw_value))

        return self.subgroup(
            gens_fn=_stab_vec_gens,
            predicate=lambda M, _target=target: M * _target == _target,
        )

    def stabilizer_of_isotropic_line(self, value):
        from sage.all import vector as sage_vector
        from src.backends.external.py_polyhedral import indefinite_form_stabilizer_isotropic_line

        target = sage_vector(ZZ, list(_as_coordinate_vector(value)))
        line = self._lattice._sage_like().ambient_module().span([target])
        raw_value = [int(entry) for entry in target]

        def _stab_line_gens():
            return self._lattice._matrices_from_raw(
                indefinite_form_stabilizer_isotropic_line(self._lattice._gram_rows(), raw_value)
            )

        return self.subgroup(
            gens_fn=_stab_line_gens,
            predicate=lambda M, _target=target, _line=line: M * _target in _line,
        )

    def stabilizer_of_isotropic_plane(self, left, right):
        from sage.all import vector as sage_vector
        from src.backends.external.py_polyhedral import indefinite_form_stabilizer_isotropic_plane_2d

        left_vector = sage_vector(ZZ, list(_as_coordinate_vector(left)))
        right_vector = sage_vector(ZZ, list(_as_coordinate_vector(right)))
        plane = self._lattice._sage_like().ambient_module().span([left_vector, right_vector])
        return self.subgroup(
            gens_fn=lambda: self._lattice._matrices_from_raw(
                indefinite_form_stabilizer_isotropic_plane_2d(
                    self._lattice._gram_rows(),
                    [int(entry) for entry in left_vector],
                    [int(entry) for entry in right_vector],
                )
            ),
            predicate=lambda M, _l=left_vector, _r=right_vector, _p=plane: M * _l in _p and M * _r in _p,
        )

    def stabilizer_of_isotropic_flag(self, ordered_basis):
        from sage.all import vector as sage_vector
        from src.backends.external.py_polyhedral import indefinite_form_stabilizer_isotropic_flag

        columns = [sage_vector(ZZ, list(_as_coordinate_vector(value))) for value in ordered_basis]
        strata = [self._lattice._sage_like().ambient_module().span(columns[: index + 1]) for index in range(len(columns))]
        basis_rows = [[int(entry) for entry in column] for column in columns]

        def predicate(M, _columns=columns, _strata=strata):
            return all(M * column in stratum for column, stratum in zip(_columns, _strata, strict=True))

        def _flag_gens():
            return self._lattice._matrices_from_raw(
                indefinite_form_stabilizer_isotropic_flag(self._lattice._gram_rows(), basis_rows)
            )

        return self.subgroup(gens_fn=_flag_gens, predicate=predicate)

    def centralizer(self, value):
        candidate = matrix(ZZ, value)
        positive_rank, negative_rank = self._lattice.signature_pair()
        gens_fn = None
        if type(self) is LatticeOrthogonalGroup and ((not positive_rank) or (not negative_rank)):

            def gens_fn():
                return self._lattice._centralizer_gens_via_gap(candidate)

        return self.subgroup(
            gens_fn=gens_fn,
            predicate=lambda M, _candidate=candidate: M * _candidate == _candidate * M,
        )

    def find_vector_isometry(self, left, right):
        from src.backends.dawes_orbit_backend import find_vector_isometry_in_group

        return find_vector_isometry_in_group(self, left, right)

    def vectors_are_equivalent(self, left, right):
        from src.backends.dawes_orbit_backend import vectors_are_equivalent_in_group

        return vectors_are_equivalent_in_group(self, left, right)

    def isotropic_line_orbits(self):
        from src.backends.isotropic_gamma_orbit_backend import isotropic_line_orbits_in_group

        return isotropic_line_orbits_in_group(self)

    def isotropic_plane_orbits(self):
        from src.backends.isotropic_gamma_orbit_backend import isotropic_plane_orbits_in_group

        return isotropic_plane_orbits_in_group(self)

    def isotropic_flag_orbits(self, depth):
        from src.backends.isotropic_gamma_orbit_backend import isotropic_flag_orbits_in_group

        return isotropic_flag_orbits_in_group(self, depth)

    def isotropic_lines_are_equivalent(self, left, right):
        from src.backends.isotropic_gamma_orbit_backend import isotropic_lines_are_equivalent_in_group

        return isotropic_lines_are_equivalent_in_group(self, left, right)

    def isotropic_planes_are_equivalent(self, left_basis, right_basis):
        from src.backends.isotropic_gamma_orbit_backend import isotropic_planes_are_equivalent_in_group

        return isotropic_planes_are_equivalent_in_group(self, left_basis, right_basis)

    def kernel_of_discriminant_action(self):
        lattice = self._lattice
        return self._structured_subgroup(
            lambda M, _lattice=lattice: _acts_trivially_on_discriminant(_lattice, M),
            finite_quotient_presentation=_FiniteQuotientPresentation(
                discriminant_preimages=(lattice.discriminant_group().orthogonal_group().subgroup([]),),
            ),
        )


class LatticeOrthogonalGroup(_LatticeOrthogonalSet):
    @classmethod
    def from_lattice(cls, lattice, gens_fn):
        return cls(lattice, gens_fn)

    def __init__(self, lattice, gens_fn):
        gram = lattice.gram_matrix()
        super().__init__(
            lattice,
            _ConditionSet(MatrixSpace(ZZ, lattice.rank()), lambda M: M.transpose() * gram * M == gram),
            gens_fn=gens_fn,
            finite_quotient_presentation=_FiniteQuotientPresentation(),
        )


class LatticeOrthogonalSubgroup(_LatticeOrthogonalSet):
    @classmethod
    def _from_condition_set(cls, lattice, condition_set, *, gens_fn=None, finite_quotient_presentation):
        result = object.__new__(cls)
        _LatticeOrthogonalSet.__init__(
            result,
            lattice,
            condition_set,
            gens_fn=gens_fn,
            finite_quotient_presentation=finite_quotient_presentation,
        )
        return result

    def __init__(self, parent: LatticeOrthogonalGroup, gens_fn=None, predicate=None, finite_quotient_presentation=None):
        if predicate is None:
            condition = parent.condition_set
        else:
            condition = parent.condition_set & _ConditionSet(MatrixSpace(ZZ, parent.lattice.rank()), predicate)
        super().__init__(
            parent.lattice,
            condition,
            gens_fn=gens_fn,
            finite_quotient_presentation=finite_quotient_presentation,
        )


class DiscriminantOrthogonalGroup:
    def __init__(self, disc):
        self._disc = disc
        self._sage_group = None
        self._gens_cache = None

    def _require_sage_group(self):
        if self._sage_group is None:
            self._sage_group = self._disc._sage_like().orthogonal_group()
        return self._sage_group

    @property
    def discriminant_group(self):
        return self._disc

    def gens(self):
        if self._gens_cache is None:
            self._gens_cache = [matrix(ZZ, generator.matrix()) for generator in self._require_sage_group().gens()]
        return list(self._gens_cache)

    def __contains__(self, value):
        sage_group = self._require_sage_group()
        candidate = sage_group(matrix(ZZ, value))
        return candidate in sage_group

    def act(self, G, value):
        element = value if value in self._disc else self._disc(value)
        return matrix(ZZ, G) * vector(ZZ, element.vector())

    def subgroup(self, generators):
        return DiscriminantOrthogonalSubgroup(self._disc, list(generators), self._require_sage_group())

    def stabilizer(self, element):
        sage_stabilizer = self._require_sage_group().stabilizer(self._disc(element)._sage_like())
        return DiscriminantOrthogonalSubgroup(
            self._disc,
            [matrix(ZZ, generator.matrix()) for generator in sage_stabilizer.gens()],
            self._require_sage_group(),
        )


class DiscriminantOrthogonalSubgroup:
    def __init__(self, disc, generators: list, parent_sage_group):
        self._disc = disc
        self._generators = list(generators)
        self._parent_sage_group = parent_sage_group
        self._sage_subgroup = parent_sage_group.subgroup([parent_sage_group(matrix(ZZ, generator)) for generator in generators])

    @classmethod
    def _from_sage_subgroup(cls, disc, parent_sage_group, sage_subgroup):
        generators = [matrix(ZZ, generator.matrix()) for generator in sage_subgroup.gens()]
        subgroup = cls.__new__(cls)
        subgroup._disc = disc
        subgroup._generators = generators
        subgroup._parent_sage_group = parent_sage_group
        subgroup._sage_subgroup = sage_subgroup
        return subgroup

    @property
    def discriminant_group(self):
        return self._disc

    def gens(self):
        return list(self._generators)

    def __contains__(self, value):
        candidate = self._parent_sage_group(matrix(ZZ, value))
        return candidate in self._sage_subgroup

    def act(self, G, value):
        element = value if value in self._disc else self._disc(value)
        return matrix(ZZ, G) * vector(ZZ, element.vector())

    def __and__(self, other):
        assert self._disc is other.discriminant_group, "Discriminant subgroup intersections require a common parent"
        return DiscriminantOrthogonalSubgroup._from_sage_subgroup(
            self._disc,
            self._parent_sage_group,
            self._sage_subgroup.intersection(other._sage_subgroup),
        )
