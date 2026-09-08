r"""Local algebra invariants of supported hypersurface singularities."""

from sage.rings.integer_ring import ZZ as SageZZ
from sage.matrix.constructor import matrix
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    SymmetricAlgebras,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


class IsolatedHypersurfaceSingularity:
    r"""A hypersurface germ at the origin with finite Jacobian algebra."""

    def __init__(self, polynomial_ring, equation) -> None:
        base = polynomial_ring.base_ring()
        if polynomial_ring not in SymmetricAlgebras(base):
            raise TypeError("a hypersurface singularity requires a polynomial algebra")
        self._polynomial_ring = polynomial_ring
        self._equation = polynomial_ring(equation)
        engine = _engine_ring(polynomial_ring)
        f = _engine_element(polynomial_ring, self._equation)
        variables = tuple(engine.gens())
        derivatives = tuple(f.derivative(variable) for variable in variables)
        jacobian = engine.ideal(derivatives)
        dimension = jacobian.vector_space_dimension()
        if dimension not in SageZZ:
            raise ValueError("the Jacobian algebra is not finite-dimensional at the selected origin")
        self._engine_derivatives = derivatives
        self._milnor_number = int(dimension)

    def polynomial_ring(self):
        return self._polynomial_ring

    def equation(self):
        return self._equation

    def jacobian_generators(self):
        ring = self.polynomial_ring()
        return tuple(ring._from_engine_element(value) for value in self._engine_derivatives)

    def milnor_algebra(self):
        return FinitelyPresentedAlgebra(self.polynomial_ring(), self.jacobian_generators())

    def milnor_number(self):
        return _own_ring(SageZZ)(self._milnor_number)

    def tjurina_algebra(self):
        return FinitelyPresentedAlgebra(
            self.polynomial_ring(),
            (self.equation(), *self.jacobian_generators()),
        )

    def tjurina_number(self):
        engine = _engine_ring(self.polynomial_ring())
        ideal = engine.ideal(
            _engine_element(self.polynomial_ring(), relation)
            for relation in (self.equation(), *self.jacobian_generators())
        )
        dimension = ideal.vector_space_dimension()
        if dimension not in SageZZ:
            raise ValueError("the Tjurina algebra is not finite-dimensional at the selected origin")
        return _own_ring(SageZZ)(dimension)

    def completed_local_ring(self, *, precision=20):
        hypersurface = FinitelyPresentedAlgebra(self.polynomial_ring(), (self.equation(),))
        maximal = hypersurface.ideal(*tuple(hypersurface.algebra_generators()))
        return hypersurface.adic_completion(maximal, precision=precision)

    @cached_method
    def ambient_tangent_space(self):
        r"""Return the coordinate tangent space of the ambient affine space at the origin."""
        ring = self.polynomial_ring()
        return FreshFreeModuleOn(ring.base_ring(), ring.algebra_generating_set())

    @cached_method
    def zariski_tangent_space(self):
        r"""Return ``ker(df_0)`` as a finite free vector space over the residue field.

        For a hypersurface ``f=0`` at the coordinate origin, the Zariski
        tangent space is the kernel of the linear form whose coefficients are
        the constant terms of the partial derivatives of ``f``.  Computing
        that kernel in the selected field backend gives an actual basis, which
        is retained by :meth:`zariski_tangent_embedding`.
        """
        ring = self.polynomial_ring()
        base = ring.base_ring()
        base_engine = _engine_ring(base)
        coefficients = tuple(
            base_engine(derivative.constant_coefficient())
            for derivative in self._engine_derivatives
        )
        differential = matrix(base_engine, 1, len(coefficients), coefficients)
        kernel_basis = tuple(differential.right_kernel().basis())
        labels = finite_ordered_set(range(len(kernel_basis)))
        tangent = FreshFreeModuleOn(
            base,
            labels,
            _extra_construction_data={
                "ambient_tangent_space": self.ambient_tangent_space(),
                "ambient_coordinate_vectors": kernel_basis,
                "source_singularity": self,
            },
        )
        return tangent

    @cached_method
    def zariski_tangent_embedding(self):
        r"""Return the represented inclusion ``T_0 X -> T_0 A^n``."""
        tangent = self.zariski_tangent_space()
        ambient = self.ambient_tangent_space()
        ambient_labels = tuple(ambient.module_generating_set())
        vectors = tangent._preamble_ambient_coordinate_vectors

        def image(label):
            vector = vectors[int(label)]
            return ambient.linear_combination(
                {
                    ambient_label: ambient.base_ring()._from_engine_element(coefficient)
                    for ambient_label, coefficient in zip(ambient_labels, vector, strict=True)
                    if coefficient
                }
            )

        return module_homset(tangent, ambient)(image)

    def is_regular_at_origin(self) -> bool:
        r"""Return the hypersurface Jacobian criterion at the selected origin."""
        return int(self.zariski_tangent_space().module_rank()) == len(
            tuple(self.polynomial_ring().algebra_generating_set())
        ) - 1

    def is_singular_at_origin(self) -> bool:
        return not self.is_regular_at_origin()


__all__ = ["IsolatedHypersurfaceSingularity"]
