r"""Owned relative affine families assembled from equation presentations."""

from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.schemes.schemes import (
    Schemes,
    Spec,
)


class RelativeAffineFamily(SageObject):
    r"""A represented affine family ``X -> S`` from equations over ``O(S)``.

    The parameter algebra ``T`` is the scalar ring of the relative polynomial
    presentation ``T[x_1,...,x_n]/(f_1,...,f_r)``.  Consequently the
    structure map ``T -> A`` is already the defining algebra datum of the
    family; this object only retains that datum together with the slice arrow
    and delegates fibres, flatness and nonsmoothness to the existing scheme
    and differential owners.
    """

    def __init__(self, parameter_algebra, relative_variables, equations) -> None:
        self._parameter_algebra = parameter_algebra
        self._presentation_ring = parameter_algebra.polynomial_ring(relative_variables)
        raw_equations = equations(self._presentation_ring) if callable(equations) else equations
        self._equations = tuple(
            self._presentation_ring(equation) for equation in raw_equations
        )
        self._total_algebra = (self._presentation_ring).quotient_by_relations(self._equations,
        )
        self._base_scheme = Schemes(parameter_algebra).base_scheme()
        self._total_space = Spec(self._total_algebra, base_ring=parameter_algebra)
        self._morphism = self._total_space.structure_morphism()
        self._slice_object = self._total_space.scheme_category().SliceOver(
            self._base_scheme
        )(self._morphism)

    def parameter_algebra(self):
        return self._parameter_algebra

    def presentation_ring(self):
        return self._presentation_ring

    def equations(self):
        return self._equations

    def total_algebra(self):
        return self._total_algebra

    def base_scheme(self):
        return self._base_scheme

    def total_space(self):
        return self._total_space

    def morphism(self):
        return self._morphism

    def slice_object(self):
        return self._slice_object

    def fiber(self, base_morphism):
        r"""Return ``X x_S S'`` for one represented ``S' -> S``."""
        if base_morphism.codomain() is not self.base_scheme():
            raise ValueError("a family fibre/base change requires a morphism into the family base")
        return base_morphism.codomain().scheme_category().fiber_product(
            self.morphism(),
            base_morphism,
        )

    @cached_method
    def quotient_fiber(self, ideal):
        r"""Return the fibre over ``Spec(T/I) -> Spec(T)``."""
        quotient = self.parameter_algebra().quotient_ring(ideal)
        point = Spec(quotient, base_ring=self.parameter_algebra())
        return self.fiber(point.structure_morphism())

    def is_flat(self) -> bool:
        return self.total_space().is_flat()

    @cached_method
    def nonsmooth_subscheme(self):
        r"""Return the represented relative nonsmooth Fitting subscheme."""
        return self.total_space().relative_nonsmooth_subscheme()

    def as_dvr_family(self):
        r"""Equip this family with the generic/special/completed DVR operations.

        The parameter ring itself remains the authoritative datum.  This
        wrapper uses its fraction-field, residue and maximal-adic completion
        maps; it does not replace the family morphism by a second presentation.
        """
        return DVRRelativeAffineFamily(self)

    def _repr_(self) -> str:
        return f"Relative affine family {self.total_space()} -> {self.base_scheme()}"



class DVRSpecialFiberComparison(SageObject):
    r"""The canonical comparison between direct and completion-first special fibres."""

    def __init__(self, direct, completed, forward, inverse) -> None:
        if forward.domain() is not completed or forward.codomain() is not direct:
            raise ValueError("the forward special-fibre comparison has the wrong endpoints")
        if inverse.domain() is not direct or inverse.codomain() is not completed:
            raise ValueError("the inverse special-fibre comparison has the wrong endpoints")
        if forward * inverse != direct.categorical_identity_morphism():
            raise ArithmeticError("the special-fibre comparison is not a left inverse")
        if inverse * forward != completed.categorical_identity_morphism():
            raise ArithmeticError("the special-fibre comparison is not a right inverse")
        self._direct = direct
        self._completed = completed
        self._forward = forward
        self._inverse = inverse

    def direct_special_fiber(self):
        return self._direct

    def completed_special_fiber(self):
        return self._completed

    def forward(self):
        return self._forward

    def inverse(self):
        return self._inverse


class DVRRelativeAffineFamily(SageObject):
    r"""A relative affine family over a represented DVR-like local domain.

    The supplied parameter algebra must provide its maximal ideal, fraction
    field map and residue map.  Completion is taken at that maximal ideal.
    Every geometric object below is obtained from the original family by the
    existing scheme base-change functor.
    """

    def __init__(self, family) -> None:
        self._family = family
        parameter = family.parameter_algebra()
        self._maximal_ideal = parameter.maximal_ideal()

    def family(self):
        return self._family

    def parameter_algebra(self):
        return self.family().parameter_algebra()

    def maximal_ideal(self):
        return self._maximal_ideal

    @cached_method
    def generic_parameter_map(self):
        return self.parameter_algebra().fraction_field_map()

    @cached_method
    def special_parameter_map(self):
        return self.parameter_algebra().residue_map()

    @cached_method
    def completion(self):
        return self.parameter_algebra().adic_completion(self.maximal_ideal())

    @cached_method
    def completion_parameter_map(self):
        return self.completion().completion_map()

    @cached_method
    def generic_fiber(self):
        total = self.family().total_space()
        return total.scheme_category().base_change_functor(
            self.generic_parameter_map()
        )(total)

    @cached_method
    def special_fiber(self):
        total = self.family().total_space()
        return total.scheme_category().base_change_functor(
            self.special_parameter_map()
        )(total)

    @cached_method
    def completed_total_space(self):
        total = self.family().total_space()
        return total.scheme_category().base_change_functor(
            self.completion_parameter_map()
        )(total)

    @cached_method
    def completed_family_morphism(self):
        return self.completed_total_space().structure_morphism()

    @cached_method
    def completed_special_fiber(self):
        total = self.completed_total_space()
        return total.scheme_category().base_change_functor(
            self.completion().residue_map()
        )(total)

    @cached_method
    def special_fiber_comparison(self):
        r"""Compare ``X_k`` with ``(X_{R^})_k`` through their pullback cones."""
        direct = self.special_fiber()
        completed_total = self.completed_total_space()
        completed_special = self.completed_special_fiber()
        completion_projection = completed_total.left_projection()
        completed_residue_base = completed_total.scheme_category().base_change_functor(
            self.completion().residue_map()
        ).base_morphism()

        forward = direct.from_pullback_cone(
            completion_projection * completed_special.left_projection(),
            completed_special.right_projection(),
        )
        direct_to_completed_total = completed_total.from_pullback_cone(
            direct.left_projection(),
            completed_residue_base * direct.right_projection(),
        )
        inverse = completed_special.from_pullback_cone(
            direct_to_completed_total,
            direct.right_projection(),
        )
        return DVRSpecialFiberComparison(
            direct,
            completed_special,
            forward,
            inverse,
        )


__all__ = [
    "DVRSpecialFiberComparison",
    "DVRRelativeAffineFamily",
    "RelativeAffineFamily",
]
