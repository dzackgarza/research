r"""Local algebra invariants of supported hypersurface singularities."""

from sage.libs.singular.function import lib as singular_lib
from sage.libs.singular.function import singular_function
from sage.matrix.constructor import matrix
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
    SymmetricAlgebras,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.rings.commutative_ideals import _from_engine_ideal
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _parse_ade_type(ade_type):
    r"""Return ``(letter, index)`` for a supported ADE label."""
    if isinstance(ade_type, str):
        label = ade_type.strip().upper()
        if len(label) < 2:
            raise ValueError("an ADE label has a letter and a positive index")
        return label[0], int(label[1:])
    letter, index = ade_type
    return str(letter).upper(), int(index)


def _ade_normal_form_equation(polynomial_ring, ade_type):
    r"""Return the selected plane-curve ADE normal form in ``k[x,y]``."""
    x, y = tuple(polynomial_ring.algebra_generators())
    letter, index = _parse_ade_type(ade_type)
    match letter:
        case "A":
            if index < 1:
                raise ValueError("A_n requires n >= 1")
            return x**2 + y ** (index + 1)
        case "D":
            if index < 4:
                raise ValueError("D_n requires n >= 4")
            return x**2 * y + y ** (index - 1)
        case "E":
            match index:
                case 6:
                    return x**3 + y**4
                case 7:
                    return x**3 + x * y**3
                case 8:
                    return x**3 + y**5
                case _:
                    raise ValueError("the exceptional simple plane curves are E6, E7 and E8")
        case _:
            raise ValueError("a supported simple plane curve has type A, D or E")


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

    @classmethod
    def from_ade_type(cls, base_ring, ade_type, *, names=("x", "y")):
        r"""Construct the selected-coordinate ADE plane-curve normal form.

        The supported classification table is the characteristic-zero simple
        plane-curve list ``A_n``, ``D_n``, ``E_6``, ``E_7``, ``E_8``.  This
        constructor selects a normal form; it does not assert that an arbitrary
        analytically equivalent equation has already been transformed to it.
        """
        if int(_engine_ring(base_ring).characteristic()) != 0:
            raise NotImplementedError(
                "the represented ADE plane-curve normal forms currently require characteristic zero"
            )
        ring = PolynomialRing(base_ring, tuple(names))
        return cls(ring, _ade_normal_form_equation(ring, ade_type))

    def polynomial_ring(self):
        return self._polynomial_ring

    def equation(self):
        return self._equation

    def ade_normal_form_type(self):
        r"""Return the selected ADE label when this equation is exactly a supported normal form.

        Equality is tested in the chosen polynomial coordinates.  No analytic,
        formal, contact, or right-equivalence algorithm is invoked here.
        """
        ring = self.polynomial_ring()
        if int(_engine_ring(ring.base_ring()).characteristic()) != 0:
            raise NotImplementedError(
                "ADE normal-form recognition is currently represented in characteristic zero"
            )
        if len(tuple(ring.algebra_generators())) != 2:
            return None
        milnor = int(self.milnor_number())
        candidates = [("A", milnor)]
        if milnor >= 4:
            candidates.append(("D", milnor))
        for exceptional in (6, 7, 8):
            if milnor == exceptional:
                candidates.append(("E", exceptional))
        for candidate in candidates:
            if self.equation() == _ade_normal_form_equation(ring, candidate):
                return candidate
        return None

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

    def _plane_curve_origin_data(self):
        r"""Return Singular's local ``(delta, tau, branches)`` data at the origin.

        ``deltaLoc`` is a local plane-curve operation: its second input is the
        prime component of the singular locus selecting the point.  We select
        the coordinate origin by the maximal ideal generated by the two
        polynomial variables, so other singular points of the same affine
        equation do not contribute.
        """
        ring = self.polynomial_ring()
        generators = tuple(ring.algebra_generators())
        if len(generators) != 2:
            raise NotImplementedError(
                "local delta data are currently represented for plane curves"
            )
        engine = _engine_ring(ring)
        equation = _engine_element(ring, self.equation())
        equation_ideal = engine.ideal(equation)
        if equation_ideal.radical() != equation_ideal:
            raise ValueError("delta and conductor require a reduced plane curve")
        if self.is_regular_at_origin():
            return 0, 0, 1
        origin = engine.ideal(*engine.gens())
        singular_lib("normal.lib")
        local_data = singular_function("deltaLoc")(equation, origin, ring=engine)
        return tuple(int(value) for value in local_data)

    def delta_invariant(self):
        r"""Return the local plane-curve delta invariant at the selected origin.

        This is ``dim_k(normalization(A)/A)`` for the local curve ring.  The
        computation is Singular's ``deltaLoc`` from ``normal.lib`` and is
        therefore local at the chosen maximal ideal rather than a sum over all
        affine singularities.
        """
        delta, _tjurina, _branches = self._plane_curve_origin_data()
        if delta < 0:
            raise ValueError("the selected curve germ has infinite delta invariant")
        return _own_ring(SageZZ)(delta)

    def local_tjurina_number(self):
        r"""Return the local Tjurina number from the same selected germ calculation."""
        _delta, tjurina, _branches = self._plane_curve_origin_data()
        return _own_ring(SageZZ)(tjurina)

    def number_of_branches_at_origin(self):
        r"""Return the number of geometric branches of the reduced plane-curve germ."""
        _delta, _tjurina, branches = self._plane_curve_origin_data()
        return _own_ring(SageZZ)(branches)

    def conductor_ideal_at_origin(self):
        r"""Return the conductor ideal in the local ring at the selected origin.

        Singular computes the conductor in the ambient polynomial ring.  Its
        extension to the prime localization at ``(x,y)`` is the conductor of
        the selected local curve germ, with contributions from unrelated
        affine singularities removed by localization.
        """
        ring = self.polynomial_ring()
        generators = tuple(ring.algebra_generators())
        if len(generators) != 2:
            raise NotImplementedError(
                "local conductor data are currently represented for plane curves"
            )
        engine = _engine_ring(ring)
        equation = _engine_element(ring, self.equation())
        equation_ideal = engine.ideal(equation)
        if equation_ideal.radical() != equation_ideal:
            raise ValueError("delta and conductor require a reduced plane curve")
        singular_lib("normal.lib")
        conductor_engine = singular_function("normalConductor")(equation_ideal, ring=engine)
        conductor = _from_engine_ideal(ring, conductor_engine)
        curve = FinitelyPresentedAlgebra(ring, (self.equation(),))
        curve_conductor = curve.ideal(
            *(curve(generator) for generator in conductor.ideal_generators())
        )
        origin = curve.ideal(*(curve(generator) for generator in generators))
        local_ring = curve.localize_at_prime(origin)
        return curve_conductor.extension_to_localization(local_ring)


__all__ = ["IsolatedHypersurfaceSingularity"]
