r"""Cox rings of represented toric schemes, with their divisor-class grading."""

from sage.categories.category import Category
from sage.misc.classcall_metaclass import typecall

from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.rings.ring_foundation import _engine_element
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.refine import refine

_COX_RING_CATEGORIES = {}


class CoxRings(Category):
    r"""Cox rings graded by the represented divisor class group of one scheme."""

    @staticmethod
    def __classcall__(category_class, scheme):
        key = id(scheme)
        cached = _COX_RING_CATEGORIES.get(key)
        if cached is not None and cached.scheme() is scheme:
            return cached
        category = typecall(category_class, scheme)
        _COX_RING_CATEGORIES[key] = category
        return category

    def __init__(self, scheme) -> None:
        self._scheme = scheme
        Category.__init__(self)

    def scheme(self):
        return self._scheme

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
        def cox_scheme(self):
            return self._preamble_cox_scheme

        def cox_rays(self):
            return self._preamble_cox_rays

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


def CoxRing(scheme):
    r"""Return ``k[x_rho | rho in Sigma(1)]`` with ``deg(x_rho)=[D_rho]``."""
    rays = scheme.fan().cones(1)
    names = tuple(f"x{position}" for position in range(int(rays.cardinality())))
    ring = PolynomialRing(scheme.scheme_base_ring(), names)
    labels = ring.algebra_generating_set()
    ring._preamble_cox_scheme = scheme
    ring._preamble_cox_rays = finite_indexed_family(
        labels,
        lambda label: rays[int(labels.ranking_map()(label))],
        name="Cox generator rays",
    )
    refine(ring, CoxRings(scheme))
    return ring


__all__ = ["CoxRing", "CoxRings"]
