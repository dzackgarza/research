r"""O(L) — the isometry group object (spec section 3; owned substrate, V0c).

O(L) is well-defined for EVERY lattice and ``L.isometry_group()`` returns it,
unique per lattice, in ``Groups()`` (refined ``Groups().Finite()`` iff
``is_finite()``). Elements ARE the End(L) isometries (LatticeMorphism); no
parallel element type exists. The definitional membership equation
``A^T G A = G`` (with invertibility over R) appears exactly once in the
codebase: ``SyntheticIsometryGroup.__contains__``.

Supplied generators NEVER stand in for the canonical group: they live only in
``O(L).subgroup(gens)`` (IsometrySubgroup), which answers subgroup questions
and nothing at the O(L) level.
"""

from __future__ import annotations

from sage.categories.groups import Groups
from sage.matrix.constructor import identity_matrix, matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.parent import Parent

from .domain_algebra import (
    IsometryGroup as IsometryGroupCarrier,
    IsometrySubgroup as IsometrySubgroupCarrier,
)
from .homsets import LatticeMorphism


class SyntheticIsometryGroup(IsometryGroupCarrier, Parent):
    r"""O(L) for a synthetic lattice L (identity of the object: the lattice)."""

    def __init__(self, lattice):
        self._lattice = lattice
        category = Groups().Finite() if self._finiteness(lattice) else Groups()
        Parent.__init__(self, category=category)

    @staticmethod
    def _finiteness(lattice):
        # Engine-grounded domain (user ruling 2026-07-03): finiteness is a
        # property of the computed group, never a remembered classification
        # (which can simply be wrong: O(U) over ZZ is finite of order 4
        # despite U being indefinite). The delegated engine computes O(L)
        # exactly for definite integral nondegenerate ZZ-lattices (plus the
        # trivial rank-0 group); everywhere else no finiteness answer exists
        # yet, and the gating assertion in each consumer says so.
        if lattice.rank() == 0:
            return True
        return (
            lattice.base_ring() is ZZ
            and lattice.is_integral()
            and lattice.determinant() != 0
            and lattice.is_definite()
        )

    def _assert_engine_grounded(self):
        assert self._finiteness(self._lattice), (
            "O(L) finiteness/enumeration is engine-grounded only for definite "
            "integral nondegenerate ZZ-lattices (and the trivial rank-0 group); "
            f"base_ring={self._lattice.base_ring()}, "
            f"gram={self._lattice.gram_matrix()}; for other strata no computation "
            "grounds an answer yet — extend the engine, do not special-case"
        )

    def _repr_(self):
        return f"Isometry group O({self._lattice._label})"

    def lattice(self):
        return self._lattice

    def __contains__(self, f):
        r"""THE definitional membership test (once in the codebase): square,
        invertible over R, and ``A^T G A = G``."""
        if isinstance(f, LatticeMorphism):
            if not (f.domain() == self._lattice and f.codomain() == self._lattice):
                return False
            A = f.matrix()
        else:
            A = matrix(QQ, f)
        gram = self._lattice.gram_matrix()
        base_ring = self._lattice.base_ring()
        if not (A.is_square() and A.nrows() == self._lattice.rank()):
            return False
        if not all(entry in base_ring for entry in A.list()):
            return False
        determinant = A.det()
        invertible_over_R = determinant in (1, -1) if base_ring is ZZ else determinant != 0
        return invertible_over_R and A.transpose() * gram * A == gram

    def from_matrix(self, matrix_data):
        r"""Construct the isometry element; asserts the isometry contract."""
        A = matrix(QQ, matrix_data)
        assert A in self, (
            "matrix is not an isometry of this lattice "
            f"(needs A^T G A = G with A invertible over {self._lattice.base_ring()}); "
            f"matrix={A}, gram={self._lattice.gram_matrix()}"
        )
        return self._lattice.hom(matrix(self._lattice.base_ring(), A))

    def one(self):
        return self._lattice.hom(identity_matrix(self._lattice.base_ring(), self._lattice.rank()))

    def is_finite(self):
        r"""Finiteness of the ACTUAL computed group (engine-grounded); the
        gating assertion rejects strata where no computation grounds an
        answer."""
        self._assert_engine_grounded()
        return True

    def gens(self):
        r"""Generators from the ephemeral Sage engine (Sage's generators V
        satisfy V G V^T = G; the synthetic convention U^T G U = G is met by
        U = V^T), on the engine-grounded domain."""
        self._assert_engine_grounded()
        return tuple(self.from_matrix(g) for g in self._delegated_generator_matrices())

    def order(self):
        self._assert_engine_grounded()
        if self._lattice.rank() == 0:
            return ZZ.one()
        return self._delegated_engine().order()

    def _delegated_engine(self):
        from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

        # Sign-normalize: Sage's orthogonal_group needs a definite lattice and
        # O(L) = O(L(-1)), so the negative-definite case delegates the twist.
        sign = -1 if self._lattice.is_negative_definite() else 1
        return IntegralLattice(sign * matrix(ZZ, self._lattice.gram_matrix())).orthogonal_group()

    def _delegated_generator_matrices(self):
        if self._lattice.rank() == 0:
            return ()
        # integrality/definiteness proven by _assert_engine_grounded upstream
        return tuple(
            matrix(ZZ, generator.matrix()).transpose()
            for generator in self._delegated_engine().gens()
        )

    def __iter__(self):
        r"""Element enumeration from the ephemeral engine, on the
        engine-grounded domain."""
        self._assert_engine_grounded()
        if self._lattice.rank() == 0:
            yield self.one()
            return
        for element in self._delegated_engine():
            yield self.from_matrix(matrix(ZZ, element.matrix()).transpose())

    def as_matrix_group(self):
        r"""GAP-backed matrix-group seam (spec 3.5); implemented exactly where
        the group is finite and generators are computed (the engine-grounded
        domain)."""
        self._assert_engine_grounded()
        assert self._lattice.rank() > 0, (
            "the matrix-group substrate needs degree >= 1 (Sage MatrixGroup "
            "bound); the rank-0 O(L) is the trivial group — compose through "
            f"as_permutation_group instead; lattice={self._lattice}"
        )
        from sage.groups.matrix_gps.finitely_generated import MatrixGroup

        return MatrixGroup([matrix(ZZ, generator.matrix()) for generator in self.gens()])

    def as_permutation_group(self):
        r"""GAP-backed permutation seam (spec 3.5), on the engine-grounded domain."""
        self._assert_engine_grounded()
        from sage.groups.perm_gps.permgroup import PermutationGroup

        if self._lattice.rank() == 0:
            return PermutationGroup([[1]])
        return self.as_matrix_group().as_permutation_group()

    def discriminant_action(self, f):
        r"""The induced action of the single verified isometry ``f`` on A_L.
        Per-element functor; NO group-level claim."""
        assert f in self, (
            f"discriminant_action needs a verified element of O({self._lattice._label}); "
            f"got={f}"
        )
        return self._lattice.discriminant_group().action_of_isometry(f)

    def subgroup(self, gens):
        return SyntheticIsometrySubgroup(self, gens)

    def __eq__(self, other):
        return isinstance(other, SyntheticIsometryGroup) and self._lattice == other._lattice

    def __hash__(self):
        return hash(("O", self._lattice))


class SyntheticIsometrySubgroup(IsometrySubgroupCarrier):
    r"""The ONLY home for caller-supplied generators (spec 3.3). Answers
    subgroup questions only; nothing here answers an O(L)-level question,
    and there is deliberately NO __contains__ (subgroup membership is not
    decidable in general and no partial claim is exposed)."""

    def __init__(self, ambient, gens):
        self._ambient = ambient
        validated = []
        for gen in gens:
            validated.append(gen if isinstance(gen, LatticeMorphism) and gen in ambient
                             else ambient.from_matrix(gen if not isinstance(gen, LatticeMorphism) else gen.matrix()))
        self._gens = tuple(validated)

    def _repr_(self):
        return f"Subgroup of O({self._ambient._lattice._label}) on {len(self._gens)} generators"

    __repr__ = _repr_

    def gens(self):
        return self._gens

    def lattice(self):
        return self._ambient.lattice()

    def ambient(self):
        return self._ambient

    def preserves(self, sublattice):
        r"""Whether every generator maps ``sublattice`` into itself."""
        acting = self.lattice()
        acting._assert_same_ambient(sublattice)
        acting_basis = acting._inclusion_rows()
        assert acting_basis.nrows() == acting_basis.ncols() and acting_basis.rank() == acting.rank(), (
            "preserves() requires the acting lattice to span the ambient; "
            f"inclusion={acting_basis}"
        )
        from sage.modules.free_module_element import vector

        other_module = sublattice._underlying_module()
        for morphism in self._gens:
            action_matrix = matrix(QQ, morphism.matrix())
            for row in sublattice._inclusion_rows().rows():
                coordinates = acting_basis.solve_left(matrix(QQ, 1, acting_basis.ncols(), list(row)))
                image_coordinates = action_matrix * coordinates.transpose()
                image_row = vector(QQ, [
                    sum(image_coordinates[j, 0] * acting_basis[j, i] for j in range(acting.rank()))
                    for i in range(acting_basis.ncols())
                ])
                if image_row not in other_module:
                    return False
        return True

    def discriminant_image(self):
        r"""The subgroup of the finite O(q_L) generated by the generators'
        actions (spec 3.3, the typed group object — the successor of the
        deleted lattice-gens surfaces); defined when L is integral
        nondegenerate."""
        from .discriminant import SyntheticOrthogonalGroup

        form = self.lattice().discriminant_group()
        return SyntheticOrthogonalGroup(form, (self._ambient.discriminant_action(gen) for gen in self._gens), close=True)

    def order(self):
        assert self._ambient.is_finite(), (
            "subgroup order is computed only when the ambient O(L) is finite "
            f"(closure computable); ambient={self._ambient}"
        )
        from sage.groups.matrix_gps.finitely_generated import MatrixGroup

        if not self._gens:
            return ZZ.one()
        return MatrixGroup([g.matrix() for g in self._gens]).order()

    def as_matrix_group(self):
        r"""GAP-backed matrix-group seam (spec 3.5); same finiteness condition
        as ``order``/``__iter__`` (ambient O(L) finite)."""
        assert self._ambient.is_finite(), (
            "subgroup seams are computed only when the ambient O(L) is finite "
            f"(closure computable); ambient={self._ambient}"
        )
        assert self.lattice().rank() > 0, (
            "the matrix-group substrate needs degree >= 1 (Sage MatrixGroup "
            "bound); the rank-0 subgroup is trivial — compose through "
            f"as_permutation_group instead; lattice={self.lattice()}"
        )
        from sage.groups.matrix_gps.finitely_generated import MatrixGroup

        if not self._gens:
            return MatrixGroup([identity_matrix(ZZ, self.lattice().rank())])
        return MatrixGroup([matrix(ZZ, generator.matrix()) for generator in self._gens])

    def as_permutation_group(self):
        r"""GAP-backed permutation seam (spec 3.5), same finiteness condition."""
        assert self._ambient.is_finite(), (
            "subgroup seams are computed only when the ambient O(L) is finite "
            f"(closure computable); ambient={self._ambient}"
        )
        from sage.groups.perm_gps.permgroup import PermutationGroup

        if self.lattice().rank() == 0:
            return PermutationGroup([[1]])
        return self.as_matrix_group().as_permutation_group()

    def __iter__(self):
        r"""Closure enumeration through the matrix-group engine; implemented
        under the same finiteness condition as ``order`` (spec 3.3)."""
        assert self._ambient.is_finite(), (
            "subgroup enumeration is computed only when the ambient O(L) is finite "
            f"(closure computable); ambient={self._ambient}"
        )
        if not self._gens:
            yield self._ambient.one()
            return
        for element in self.as_matrix_group():
            yield self._ambient.from_matrix(matrix(QQ, element.matrix()))

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticIsometrySubgroup)
            and self._ambient == other._ambient
            and self._gens == other._gens
        )

    def __hash__(self):
        return hash((self._ambient, self._gens))
