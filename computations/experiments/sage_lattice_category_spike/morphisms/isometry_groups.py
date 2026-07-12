r"""O(L) — the isometry group object (spec section 3; owned implementation, V0c).

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

from collections.abc import Iterator
from typing import Any

from sage.categories.groups import Groups
from sage.matrix.constructor import identity_matrix, matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.parent import Parent

from ..lexicon import IsometryGroup, IsometrySubgroup
from ..objects.parents import SyntheticIntegralNondegenerateLattice, SyntheticLattice
from .homsets import LatticeMorphism


class SyntheticIsometryGroup(IsometryGroup, Parent):
    r"""O(L) for a synthetic lattice L (identity of the object: the lattice)."""

    def __init__(self, lattice: SyntheticLattice) -> None:
        self._lattice = lattice
        category = Groups().Finite() if self._finiteness(lattice) else Groups()
        Parent.__init__(self, category=category)

    @staticmethod
    def _finiteness(lattice: SyntheticLattice) -> bool:
        # Domain where Sage's computation applies (user ruling 2026-07-03):
        # finiteness is a property of the computed group, never a remembered
        # classification (which can simply be wrong: O(U) over ZZ is finite of
        # order 4 despite U being indefinite). Sage computes O(L)
        # exactly for definite integral nondegenerate ZZ-lattices (plus the
        # trivial rank-0 group); everywhere else no finiteness answer exists
        # yet, and the gating assertion in each consumer says so.
        if lattice.rank() == 0:
            return True
        return bool(lattice.base_ring() is ZZ and lattice.is_integral() and lattice.determinant() != 0 and lattice.is_definite())

    def _assert_engine_grounded(self) -> None:
        assert self._finiteness(self._lattice), (
            "O(L) finiteness/enumeration is grounded by Sage's computation only for definite "
            "integral nondegenerate ZZ-lattices (and the trivial rank-0 group); "
            f"base_ring={self._lattice.base_ring()}, "
            f"gram={self._lattice.gram_matrix()}; for other subcategories no computation "
            "grounds an answer yet — extend the computation, do not special-case"
        )

    def _repr_(self) -> str:
        return f"Isometry group O({self._lattice._label})"

    def lattice(self) -> Any:
        return self._lattice

    def __contains__(self, f: object) -> bool:
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
        return bool(invertible_over_R and A.transpose() * gram * A == gram)

    def from_matrix(self, matrix_data: object) -> Any:
        r"""Construct the isometry element; asserts the isometry contract."""
        A = matrix(QQ, matrix_data)
        assert A in self, (
            f"matrix is not an isometry of this lattice (needs A^T G A = G with A invertible over {self._lattice.base_ring()}); matrix={A}, gram={self._lattice.gram_matrix()}"
        )
        return self._lattice.hom(matrix(self._lattice.base_ring(), A))

    def one(self) -> Any:
        return self._lattice.hom(identity_matrix(self._lattice.base_ring(), self._lattice.rank()))

    def is_finite(self) -> bool:
        r"""Finiteness of the ACTUAL computed group (grounded by Sage's
        computation); the gating assertion rejects subcategories where no
        computation grounds an answer."""
        self._assert_engine_grounded()
        return True

    def gens(self) -> tuple[Any, ...]:
        r"""Generators from the ephemeral Sage orthogonal group (Sage's generators V
        satisfy V G V^T = G; the synthetic convention U^T G U = G is met by
        U = V^T), on the domain where Sage's computation applies."""
        self._assert_engine_grounded()
        return tuple(self.from_matrix(g) for g in self._delegated_generator_matrices())

    def order(self) -> Any:
        self._assert_engine_grounded()
        if self._lattice.rank() == 0:
            return ZZ.one()
        return self._delegated_engine().order()

    def _delegated_engine(self) -> Any:
        from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

        # Sign-normalize: Sage's orthogonal_group needs a definite lattice and
        # O(L) = O(L(-1)), so the negative-definite case twists the Gram before calling Sage.
        sign = -1 if self._lattice.is_negative_definite() else 1
        return IntegralLattice(sign * matrix(ZZ, self._lattice.gram_matrix())).orthogonal_group()

    def _delegated_generator_matrices(self) -> tuple[Any, ...]:
        if self._lattice.rank() == 0:
            return ()
        # integrality/definiteness proven by _assert_engine_grounded upstream
        return tuple(matrix(ZZ, generator.matrix()).transpose() for generator in self._delegated_engine().gens())

    def __iter__(self) -> Iterator[Any]:
        r"""Element enumeration from the ephemeral Sage orthogonal group, on the
        domain where Sage's computation applies."""
        self._assert_engine_grounded()
        if self._lattice.rank() == 0:
            yield self.one()
            return
        for element in self._delegated_engine():
            yield self.from_matrix(matrix(ZZ, element.matrix()).transpose())

    def as_matrix_group(self) -> Any:
        r"""GAP-backed matrix group — the point where Sage's MatrixGroup is
        called (spec 3.5); implemented exactly where the group is finite and
        generators are computed (the domain where Sage's computation applies)."""
        self._assert_engine_grounded()
        assert self._lattice.rank() > 0, (
            "Sage's MatrixGroup needs degree >= 1 (Sage MatrixGroup "
            "bound); the rank-0 O(L) is the trivial group — compose through "
            f"as_permutation_group instead; lattice={self._lattice}"
        )
        from sage.groups.matrix_gps.finitely_generated import MatrixGroup

        return MatrixGroup([matrix(ZZ, generator.matrix()) for generator in self.gens()])

    def as_permutation_group(self) -> Any:
        r"""GAP-backed permutation group (spec 3.5), on the domain where Sage's computation applies."""
        self._assert_engine_grounded()
        from sage.groups.perm_gps.permgroup import PermutationGroup

        if self._lattice.rank() == 0:
            return PermutationGroup([[1]])
        return self.as_matrix_group().as_permutation_group()

    def structure_description(self) -> str:
        r"""GAP's structure description of O(L) (gap-ledger row 9e), through
        the permutation-group seam, on the domain where Sage's computation
        applies."""
        self._assert_engine_grounded()
        return str(self.as_permutation_group().structure_description())

    def conjugacy_classes_representatives(self) -> tuple[Any, ...]:
        r"""One O(L) element per conjugacy class (gap-ledger row 9e), computed
        by GAP through the matrix-group seam and returned as verified
        isometries; on the domain where Sage's computation applies."""
        self._assert_engine_grounded()
        if self._lattice.rank() == 0:
            return (self.one(),)
        return tuple(self.from_matrix(matrix(ZZ, representative.matrix())) for representative in self.as_matrix_group().conjugacy_classes_representatives())

    def _discriminant_source(self) -> SyntheticIntegralNondegenerateLattice:
        r"""The lattice, narrowed to the subcategory where the discriminant
        vocabulary is defined (integral nondegenerate)."""
        lattice = self._lattice
        assert isinstance(lattice, SyntheticIntegralNondegenerateLattice), (
            f"the discriminant functor O(L) -> O(q_L) is defined for integral nondegenerate lattices; gram={lattice.gram_matrix()}, base_ring={lattice.base_ring()}"
        )
        return lattice

    def discriminant_action(self, f: Any) -> Any:
        r"""The induced action of the single verified isometry ``f`` on A_L.
        Per-element functor; NO group-level claim."""
        assert f in self, f"discriminant_action needs a verified element of O({self._lattice._label}); got={f}"
        return self._discriminant_source().discriminant_group().action_of_isometry(f)

    def discriminant_representation(self) -> Any:
        r"""The image of ``O(L) -> O(q_L)``: the subgroup of the finite O(q)
        generated by the generators' induced actions. Enumeration is grounded
        exactly where ``gens()`` is (the definite integral engine); the
        assertion inside ``gens`` localizes the computational limit."""
        from ..forms.discriminant import SyntheticOrthogonalGroup

        form = self._discriminant_source().discriminant_group()
        return SyntheticOrthogonalGroup(
            form,
            tuple(self.discriminant_action(g) for g in self.gens()),
            close=True,
        )

    def stable_kernel(self) -> SyntheticIsometrySubgroup:
        r"""``O(L)# = ker(O(L) -> O(q_L))``, the stable isometries — computed by
        filtering the enumerated group through the per-element functor (same
        grounded domain as ``__iter__``)."""
        return self.subgroup([f for f in self if self.discriminant_action(f).is_identity()])

    def subgroup(self, gens: Any) -> SyntheticIsometrySubgroup:
        return SyntheticIsometrySubgroup(self, gens)

    def __eq__(self, other: object) -> bool:
        return bool(isinstance(other, SyntheticIsometryGroup) and self._lattice == other._lattice)

    def __hash__(self) -> int:
        return hash(("O", self._lattice))


class SyntheticIsometrySubgroup(IsometrySubgroup):
    r"""The ONLY home for caller-supplied generators (spec 3.3). Answers
    subgroup questions only; nothing here answers an O(L)-level question,
    and there is deliberately NO __contains__ (subgroup membership is not
    decidable in general and no partial claim is exposed)."""

    def __init__(self, ambient: SyntheticIsometryGroup, gens: Any) -> None:
        self._ambient = ambient
        validated = []
        for gen in gens:
            validated.append(gen if isinstance(gen, LatticeMorphism) and gen in ambient else ambient.from_matrix(gen if not isinstance(gen, LatticeMorphism) else gen.matrix()))
        self._gens = tuple(validated)

    def _repr_(self) -> str:
        return f"Subgroup of O({self._ambient._lattice._label}) on {len(self._gens)} generators"

    __repr__ = _repr_

    def gens(self) -> tuple[Any, ...]:
        return self._gens

    def lattice(self) -> Any:
        return self._ambient.lattice()

    def ambient(self) -> SyntheticIsometryGroup:
        return self._ambient

    def preserves(self, subobject: Any) -> bool:
        r"""Whether every generator maps the subobject into itself: for each
        generator ``g`` the composite ``g . iota`` factors through ``iota`` --
        the images of the subobject's generators land back in the inclusion's
        image. Sited on the carried witness; a bare lattice carries none."""
        from sage.modules.free_module_element import vector

        from .homsets import Subobject as _Subobject

        assert isinstance(subobject, _Subobject), f"preserves takes a subobject (M.subobject(...)/an image/kernel), not a bare lattice; found={type(subobject)}"
        acting = self.lattice()
        assert subobject.inclusion().codomain() == acting, f"the subobject must live in the acting lattice; codomain={subobject.inclusion().codomain()}, acting={acting}"
        inclusion_matrix = matrix(QQ, subobject.inclusion().matrix())
        image_module = (QQ ** acting.rank()).span(inclusion_matrix.columns(), acting.base_ring())
        return all(vector(QQ, matrix(QQ, morphism.matrix()) * column) in image_module for morphism in self._gens for column in inclusion_matrix.columns())

    def discriminant_image(self) -> Any:
        r"""The subgroup of the finite O(q_L) generated by the generators'
        actions (spec 3.3, the typed group object — the successor of the
        deleted lattice-gens methods); defined when L is integral
        nondegenerate."""
        from ..forms.discriminant import SyntheticOrthogonalGroup

        form = self.lattice().discriminant_group()
        return SyntheticOrthogonalGroup(
            form,
            (self._ambient.discriminant_action(gen) for gen in self._gens),
            close=True,
        )

    def order(self) -> Any:
        assert self._ambient.is_finite(), f"subgroup order is computed only when the ambient O(L) is finite (closure computable); ambient={self._ambient}"
        from sage.groups.matrix_gps.finitely_generated import MatrixGroup

        if not self._gens:
            return ZZ.one()
        return MatrixGroup([g.matrix() for g in self._gens]).order()

    def as_matrix_group(self) -> Any:
        r"""GAP-backed matrix group (spec 3.5); same finiteness condition
        as ``order``/``__iter__`` (ambient O(L) finite)."""
        assert self._ambient.is_finite(), (
            f"subgroup matrix and permutation groups are computed only when the ambient O(L) is finite (closure computable); ambient={self._ambient}"
        )
        assert self.lattice().rank() > 0, (
            "Sage's MatrixGroup needs degree >= 1 (Sage MatrixGroup "
            "bound); the rank-0 subgroup is trivial — compose through "
            f"as_permutation_group instead; lattice={self.lattice()}"
        )
        from sage.groups.matrix_gps.finitely_generated import MatrixGroup

        if not self._gens:
            return MatrixGroup([identity_matrix(ZZ, self.lattice().rank())])
        return MatrixGroup([matrix(ZZ, generator.matrix()) for generator in self._gens])

    def as_permutation_group(self) -> Any:
        r"""GAP-backed permutation group (spec 3.5), same finiteness condition."""
        assert self._ambient.is_finite(), (
            f"subgroup matrix and permutation groups are computed only when the ambient O(L) is finite (closure computable); ambient={self._ambient}"
        )
        from sage.groups.perm_gps.permgroup import PermutationGroup

        if self.lattice().rank() == 0:
            return PermutationGroup([[1]])
        return self.as_matrix_group().as_permutation_group()

    def __iter__(self) -> Iterator[Any]:
        r"""Closure enumeration through the Sage matrix group; implemented
        under the same finiteness condition as ``order`` (spec 3.3)."""
        assert self._ambient.is_finite(), f"subgroup enumeration is computed only when the ambient O(L) is finite (closure computable); ambient={self._ambient}"
        if not self._gens:
            yield self._ambient.one()
            return
        for element in self.as_matrix_group():
            yield self._ambient.from_matrix(matrix(QQ, element.matrix()))

    def __eq__(self, other: object) -> bool:
        return bool(isinstance(other, SyntheticIsometrySubgroup) and self._ambient == other._ambient and self._gens == other._gens)

    def __hash__(self) -> int:
        return hash((self._ambient, self._gens))
