r"""Cox rings of represented toric schemes, with their divisor-class grading."""

from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.rings.ring_foundation import _engine_element
from dzack_research.preamble.categories.schemes.toric.toric_schemes import (
    ToricSchemes,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)


class _CoxRingConstruction:
    r"""The represented toric scheme defining one Cox ring."""

    def __init__(self, scheme) -> None:
        self._scheme = scheme

    def scheme(self):
        return self._scheme


class CoxRings(OwnedParameterizedCategory):
    r"""Cox rings graded by the represented divisor class group of one toric scheme."""

    @staticmethod
    def __classcall__(cls, scheme):
        return OwnedParameterizedCategory.__classcall__(cls, scheme)

    def __init__(self, scheme) -> None:
        OwnedParameterizedCategory.__init__(self, scheme)

    def parameter_category(self):
        r"""The toric schemes over the parameter's own base."""
        return ToricSchemes(self.parameter().scheme_base_ring())

    def scheme(self):
        return self.base()

    def grading_group(self):
        return self.scheme().class_group()

    def super_categories(self):
        return [
            GradedAlgebras(
                self.scheme().scheme_base_ring(),
                self.grading_group(),
            )
        ]

    def _repr_object_names(self):
        return f"Cox rings of {self.scheme()}"

    class ParentMethods:
        def cox_ring_construction(self):
            return self._cox_ring_construction

        def cox_scheme(self):
            return self.cox_ring_construction().scheme()

        def cox_rays(self):
            rays = self.cox_scheme().fan().cones(1)
            labels = self.algebra_generating_set()
            return finite_indexed_family(
                labels,
                lambda label: rays[int(labels.ranking_map()(label))],
                name="Cox generator rays",
            )

        def generator_degree(self, label):
            labels = self.algebra_generating_set()
            label = labels(label)
            ray = self.cox_rays()[label]
            return self.cox_scheme().divisor_class(
                self.cox_scheme().torus_invariant_prime_divisor(ray)
            )

        def homogeneous_degree(self, element):
            r"""Return the class-group degree of a nonzero homogeneous Cox polynomial."""
            element = self(element)
            if element == self.zero():
                raise ValueError("zero has no selected homogeneous Cox degree")
            backend = _engine_element(self, element)
            degrees = []
            labels = tuple(self.algebra_generating_set())
            grading = self.grading_monoid()
            for exponents, coefficient in backend.dict().items():
                if not coefficient:
                    continue
                degree = grading.zero()
                for position, exponent in enumerate(exponents):
                    if exponent:
                        generator_degree = self.generator_degree(labels[position])
                        degree = degree + grading.scalar_multiple(
                            grading.base_ring()(int(exponent)),
                            generator_degree,
                        )
                degrees.append(degree)
            if not degrees:
                raise ValueError("zero has no selected homogeneous Cox degree")
            selected = degrees[0]
            if any(degree != selected for degree in degrees[1:]):
                raise ValueError("the Cox-ring element is not homogeneous")
            return selected


def _cox_ring(scheme):
    r"""Return ``k[x_rho | rho in Sigma(1)]`` with ``deg(x_rho)=[D_rho]``."""
    rays = scheme.fan().cones(1)
    names = tuple(f"x{position}" for position in range(int(rays.cardinality())))
    presentation = scheme.scheme_base_ring().polynomial_ring(names)
    ring = (presentation).quotient_by_relations((),
        _extra_categories=(CoxRings(scheme),),
        _extra_construction_data=(
            ("_cox_ring_construction", _CoxRingConstruction(scheme)),
        ),
    )
    return ring


__all__ = ["CoxRings"]
