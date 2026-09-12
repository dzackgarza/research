r"""Section rings of supported toric Cartier divisors."""

from sage.geometry.cone import Cone as _SageCone
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.semigroup_algebras import (
    AffineSemigroupAlgebra,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedIntegralDomains,
    _engine_element,
)
from dzack_research.preamble.categories.schemes.toric.fans import _engine_vector
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import NN


class SectionRings(OwnedCategoryOverBaseRing):
    r"""Nonnegatively graded section algebras over the stated coefficient ring."""

    def super_categories(self):
        return [GradedAlgebras(self.base_ring(), NN)]

    @classmethod
    def _repr_object_names(cls):
        return "section rings"

    class ParentMethods:
        def section_scheme(self):
            return self._preamble_section_scheme

        def section_divisor(self):
            return self._preamble_section_divisor

        @cached_method
        def section_semigroup_generators(self):
            labels = self.algebra_generating_set()
            coordinates = self._preamble_section_semigroup_generators
            return finite_indexed_family(
                labels,
                lambda label: coordinates[int(labels.ranking_map()(label))],
                name="Section-ring semigroup generators",
            )

        def generator_degree(self, label):
            point = self.section_semigroup_generators()[label]
            return NN(int(point[-1]))

        def homogeneous_degree(self, element):
            r"""Return the nonnegative degree of one homogeneous section-ring element."""
            element = self(element)
            if element == self.zero():
                raise ValueError("zero has no selected homogeneous section-ring degree")
            presentation = self.presentation_ring()
            representative = self.lift_to_presentation(element)
            backend = _engine_element(presentation, representative)
            labels = tuple(self.algebra_generating_set())
            degrees = []
            for exponents, coefficient in backend.dict().items():
                if not coefficient:
                    continue
                degree = 0
                for position, exponent in enumerate(exponents):
                    degree += int(exponent) * int(self.generator_degree(labels[position]))
                degrees.append(degree)
            if not degrees:
                raise ValueError("zero has no selected homogeneous section-ring degree")
            selected = degrees[0]
            if any(degree != selected for degree in degrees[1:]):
                raise ValueError("the section-ring element is not homogeneous")
            return NN(selected)

        def graded_piece(self, degree):
            r"""Return ``H^0(X,O_X(nD))`` in degree ``n``."""
            degree = NN(degree)
            scheme = self.section_scheme()
            divisor = self.section_divisor()
            integers = divisor.parent().base_ring()
            return scheme.divisor_section_space(integers(int(degree)) * divisor)


def SectionRing(scheme, divisor):
    r"""Construct the semigroup algebra of the cone over the divisor polytope."""
    if not scheme.fan().is_complete():
        raise ValueError("the supported toric section-ring construction requires a complete fan")
    if not scheme.is_cartier(divisor):
        raise ValueError("a divisor section ring requires a Cartier divisor")
    if not scheme.is_basepoint_free(divisor):
        raise ValueError(
            "the supported cone-over-polytope section-ring construction requires a basepoint-free divisor"
        )

    polytope = scheme.divisor_polytope(divisor)
    lattice = polytope.ambient_lattice()
    cone_rays = tuple(
        (*tuple(_engine_vector(lattice, vertex)), 1)
        for vertex in polytope.vertices()
    )
    hilbert_basis = tuple(tuple(int(entry) for entry in vector) for vector in _SageCone(cone_rays).Hilbert_basis())
    return AffineSemigroupAlgebra(
        hilbert_basis,
        scheme.scheme_base_ring(),
        names=tuple(f"s{position}" for position in range(len(hilbert_basis))),
        extra_categories=(
            SectionRings(scheme.scheme_base_ring()),
            OwnedIntegralDomains(),
        ),
        extra_construction_data=(
            ("_preamble_section_scheme", scheme),
            ("_preamble_section_divisor", divisor),
            ("_preamble_section_semigroup_generators", hilbert_basis),
        ),
    )


__all__ = ["SectionRing", "SectionRings"]
