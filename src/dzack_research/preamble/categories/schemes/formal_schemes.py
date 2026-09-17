r"""Adic formal spectra and their compatible infinitesimal thickenings."""

from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject


from dzack_research.preamble.categories.schemes.schemes import _affine_spec_morphism


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
        assert ideal_of_definition.ring() is source_ring, (
            "an ideal of definition belongs to the formal source ring"
        )
        self._source_ring = source_ring
        self._ideal = ideal_of_definition

    def source_ring(self):
        return self._source_ring

    def ideal_of_definition(self):
        return self._ideal

    @cached_method(key=lambda self, precision=20: int(precision))
    def completion(self, precision=20):
        r"""The ``I``-adic completion ``A^`` realized at one computation precision."""
        return self.source_ring().adic_completion(
            self.ideal_of_definition(),
            precision=int(precision),
        )

    def completed_affine_scheme(self, precision=20):
        r"""Return ``Spec(A^)`` for one computational realization, not ``Spf(A,I)``."""
        completion = self.completion(precision)
        return (completion).affine_spectrum(base_ring=completion)

    def thickening_ring(self, exponent):
        exponent = int(exponent)
        assert exponent > 0, "an infinitesimal thickening exponent is positive"
        return self.source_ring().quotient_ring(
            self.ideal_of_definition().power(exponent)
        )

    def thickening(self, exponent):
        r"""Return the finite stage ``Spec(A/I^exponent)``."""
        quotient = self.thickening_ring(exponent)
        return (quotient).affine_spectrum(base_ring=quotient)

    def transition_ring_map(self, higher_exponent, lower_exponent):
        r"""Return ``A/I^higher -> A/I^lower`` in the inverse system."""
        higher_exponent = int(higher_exponent)
        lower_exponent = int(lower_exponent)
        assert higher_exponent >= lower_exponent > 0, (
            "formal transition exponents satisfy higher >= lower > 0"
        )
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
    r"""A continuous affine formal morphism ``Spf(A,I) -> Spf(B,J)``.

    It is given contravariantly by a ring map ``phi: B -> A`` with
    ``phi(J)`` contained in ``I``.  This sufficient continuity hypothesis
    also gives maps at matching powers ``B/J^n -> A/I^n``.  General adic
    continuity may instead require different powers and is not equivalent
    to this chosen same-power presentation.
    """

    def __init__(self, domain, codomain, coordinate_ring_morphism) -> None:
        assert coordinate_ring_morphism.domain() is codomain.source_ring(), (
            "a formal affine morphism has the wrong coordinate-ring source"
        )
        assert coordinate_ring_morphism.codomain() is domain.source_ring(), (
            "a formal affine morphism has the wrong coordinate-ring target"
        )
        assert all(
            domain.ideal_of_definition().contains_ambient_element(
                coordinate_ring_morphism(generator)
            )
            for generator in codomain.ideal_of_definition().ideal_generators()
        ), "the same-power formal presentation requires phi(J) contained in I"
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
