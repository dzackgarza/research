r"""Local algebra invariants of supported hypersurface singularities."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    SymmetricAlgebras,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _own_ring,
)


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


__all__ = ["IsolatedHypersurfaceSingularity"]
