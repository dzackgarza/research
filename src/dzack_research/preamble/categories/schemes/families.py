r"""Owned relative affine families assembled from equation presentations."""

from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
)
from dzack_research.preamble.categories.schemes.schemes import (
    Schemes,
    Spec,
    scheme_fiber_product,
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
        self._presentation_ring = PolynomialRing(parameter_algebra, relative_variables)
        raw_equations = equations(self._presentation_ring) if callable(equations) else equations
        self._equations = tuple(
            self._presentation_ring(equation) for equation in raw_equations
        )
        self._total_algebra = FinitelyPresentedAlgebra(
            self._presentation_ring,
            self._equations,
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
        return scheme_fiber_product(self.morphism(), base_morphism)

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


def affine_equation_family(parameter_algebra, relative_variables, equations):
    r"""Construct a relative affine family from equations over the parameter algebra.

    ``equations`` may be a finite ingress or a callable receiving the selected
    relative polynomial presentation.  The callable form is useful when the
    equations must refer to the exact owned presentation generators.
    """
    return RelativeAffineFamily(parameter_algebra, relative_variables, equations)


__all__ = ["RelativeAffineFamily", "affine_equation_family"]
