r"""Adic formal spectra and their compatible infinitesimal thickenings."""

from sage.structure.sage_object import SageObject


from dzack_research.preamble.categories.schemes.schemes import Spec, _affine_spec_morphism


class FormalCompletionComparison(SageObject):
    r"""Two computational realizations of one adic completion."""

    def __init__(self, formal_spectrum, first_precision, second_precision) -> None:
        self._formal_spectrum = formal_spectrum
        self._first = formal_spectrum.completion(first_precision)
        self._second = formal_spectrum.completion(second_precision)
        identity = formal_spectrum.source_ring().Mor(formal_spectrum.source_ring()).identity()
        self._forward = self._first.induced_map(identity, self._second)
        self._backward = self._second.induced_map(identity, self._first)

    def formal_spectrum(self):
        return self._formal_spectrum

    def first_completion(self):
        return self._first

    def second_completion(self):
        return self._second

    def forward(self):
        return self._forward

    def backward(self):
        return self._backward


class FormalSpectrum(SageObject):
    r"""The formal affine scheme ``Spf(A,I)``, distinct from ``Spec(A^)``.

    The formal object is the pair ``(A,I)`` together with its compatible
    thickenings ``Spec(A/I^n)``.  A completion precision is only a selected
    computational realization and is never stored as part of this object's
    identity.
    """

    def __init__(self, source_ring, ideal_of_definition) -> None:
        if ideal_of_definition.ring() is not source_ring:
            raise ValueError("an ideal of definition belongs to the formal source ring")
        self._source_ring = source_ring
        self._ideal = ideal_of_definition
        self._completions = {}

    def source_ring(self):
        return self._source_ring

    def ideal_of_definition(self):
        return self._ideal

    def completion(self, precision=20):
        precision = int(precision)
        selected = self._completions.get(precision)
        if selected is None:
            selected = self.source_ring().adic_completion(
                self.ideal_of_definition(),
                precision=precision,
            )
            self._completions[precision] = selected
        return selected

    def completed_affine_scheme(self, precision=20):
        r"""Return ``Spec(A^)`` for one computational realization, not ``Spf(A,I)``."""
        completion = self.completion(precision)
        return Spec(completion, base_ring=completion)

    def thickening_ring(self, exponent):
        exponent = int(exponent)
        if exponent <= 0:
            raise ValueError("an infinitesimal thickening exponent is positive")
        return self.source_ring().quotient_ring(
            self.ideal_of_definition().power(exponent)
        )

    def thickening(self, exponent):
        r"""Return the finite stage ``Spec(A/I^exponent)``."""
        quotient = self.thickening_ring(exponent)
        return Spec(quotient, base_ring=quotient)

    def transition_ring_map(self, higher_exponent, lower_exponent):
        r"""Return ``A/I^higher -> A/I^lower`` in the inverse system."""
        higher_exponent = int(higher_exponent)
        lower_exponent = int(lower_exponent)
        if lower_exponent <= 0 or higher_exponent < lower_exponent:
            raise ValueError("formal transition exponents satisfy higher >= lower > 0")
        higher = self.thickening_ring(higher_exponent)
        lower = self.thickening_ring(lower_exponent)
        lower_projection = lower.quotient_map()
        return higher.Mor(lower).elementwise(
            lambda element: lower_projection(element.lift())
        )

    def formal_restriction(self, higher_exponent, lower_exponent):
        r"""Return ``Spec(A/I^lower) -> Spec(A/I^higher)`` contravariantly."""
        return _affine_spec_morphism(
            self.transition_ring_map(higher_exponent, lower_exponent)
        )

    def completion_projection(self, precision, exponent):
        r"""Return the actual map ``A^ -> A/I^exponent`` from one realization."""
        return self.completion(precision).adic_projection(exponent)

    def compare_precisions(self, first_precision, second_precision):
        return FormalCompletionComparison(
            self,
            first_precision,
            second_precision,
        )

    def morphism_to(self, codomain, coordinate_ring_morphism):
        r"""Return the continuous formal-affine morphism to ``codomain``."""
        return FormalAffineMorphism(self, codomain, coordinate_ring_morphism)

    def _repr_(self):
        return f"Spf({self.source_ring()}, {self.ideal_of_definition()}-adic)"


class FormalAffineMorphism(SageObject):
    r"""A continuous affine formal morphism given contravariantly on rings."""

    def __init__(self, domain, codomain, coordinate_ring_morphism) -> None:
        if coordinate_ring_morphism.domain() is not codomain.source_ring():
            raise ValueError("a formal affine morphism has the wrong coordinate-ring source")
        if coordinate_ring_morphism.codomain() is not domain.source_ring():
            raise ValueError("a formal affine morphism has the wrong coordinate-ring target")
        if any(
            not domain.ideal_of_definition().contains_ambient_element(
                coordinate_ring_morphism(generator)
            )
            for generator in codomain.ideal_of_definition().ideal_generators()
        ):
            raise ValueError("the coordinate map is not continuous for the selected adic topologies")
        self._domain = domain
        self._codomain = codomain
        self._ring_map = coordinate_ring_morphism

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def coordinate_ring_morphism(self):
        return self._ring_map

    def thickening_ring_map(self, exponent):
        source = self.codomain().thickening_ring(exponent)
        target = self.domain().thickening_ring(exponent)
        target_projection = target.quotient_map()
        ring_map = self.coordinate_ring_morphism()
        return source.Mor(target).elementwise(
            lambda element: target_projection(ring_map(element.lift()))
        )

    def thickening_morphism(self, exponent):
        return _affine_spec_morphism(self.thickening_ring_map(exponent))

    def completed_ring_map(self, domain_precision=20, codomain_precision=20):
        r"""Return the continuous map on selected completion realizations."""
        codomain_completion = self.codomain().completion(codomain_precision)
        domain_completion = self.domain().completion(domain_precision)
        return codomain_completion.induced_map(
            self.coordinate_ring_morphism(),
            domain_completion,
        )
__all__ = [
    "FormalAffineMorphism",
    "FormalCompletionComparison",
    "FormalSpectrum",
]
