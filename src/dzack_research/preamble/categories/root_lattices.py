r"""Root-lattice provenance and root-system operations."""

from sage.categories.category import Category
from sage.combinat.root_system.root_system import RootSystem
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.refine import refine


class RootLattices(Category):
    r"""Negative-definite ADE root lattices with a chosen simple-root framing."""

    @classmethod
    def _repr_object_names(cls):
        return "root lattices"

    def super_categories(self):
        from dzack_research.preamble.categories.lattice_properties import (
            EvenLattices,
            FiniteRankLattices,
            NondegenerateLattices,
        )

        return [
            FiniteRankLattices(SageZZ),
            NondegenerateLattices(SageZZ),
            EvenLattices(SageZZ),
        ]

    class ParentMethods:
        def cartan_type(self):
            return self._cartan_type

        def simple_roots(self):
            r"""Return the selected framing, which is the chosen simple system."""
            return self.module_generators()

        def coxeter_number(self):
            cartan_type = self.cartan_type()
            if not cartan_type.is_irreducible():
                raise ValueError(
                    "a reducible root system has one Coxeter number per irreducible component"
                )
            return cartan_type.coxeter_number()

        def highest_root(self):
            r"""Return the highest root in the selected simple-root framing."""
            cartan_type = self.cartan_type()
            if not cartan_type.is_irreducible():
                raise ValueError(
                    "a reducible root system has one highest root per irreducible component"
                )
            coefficients = tuple(
                RootSystem(cartan_type).root_lattice().highest_root().to_vector()
            )
            return sum(
                (
                    coefficient * root
                    for coefficient, root in zip(
                        coefficients, self.simple_roots(), strict=True
                    )
                ),
                self.zero(),
            )

        def simple_reflections(self):
            return tuple(self.reflection(root) for root in self.simple_roots())

        def fundamental_weights(self):
            r"""Return the weights dual to the simple coroots.

            For a simply-laced root lattice the simple roots have common square
            ``2*epsilon`` with ``epsilon = +/-1``.  Since
            ``alpha^vee = epsilon*alpha``, the fundamental weights are
            ``epsilon`` times the metric-dual basis.  In this project's
            negative-definite convention they are therefore the negatives of
            the dual basis.
            """
            from dzack_research.preamble.categories.sets import finite_ordered_set

            norm = self.simple_roots()[0].norm()
            if norm not in (2, -2):
                raise ValueError(
                    f"a simply-laced root framing has simple-root square +/-2, got {norm}"
                )
            sign = SageZZ(norm) // 2
            return finite_ordered_set(sign * weight for weight in self.dual_basis())

    class ElementMethods:
        def is_positive_root(self) -> bool:
            r"""Return whether this root has nonnegative simple-root coordinates."""
            return bool(
                self.is_root()
                and all(
                    coefficient >= 0
                    for coefficient in self.monomial_coefficients().values()
                )
            )

        def is_negative_root(self) -> bool:
            return bool((-self).is_positive_root())

        def height(self):
            r"""Return the sum of the simple-root coordinates."""
            return sum(self.monomial_coefficients().values(), SageZZ.zero())

        def coroot(self):
            r"""Return ``alpha^vee = 2*b(alpha,-)/b(alpha,alpha)`` in ``L^#``."""
            parent = self.parent()
            if not self.is_root():
                raise ValueError("the coroot in this lattice is defined for an integral root")
            norm = SageZZ(self.norm())
            dual_lattice = parent.dual_lattice()
            return dual_lattice.linear_combination(
                {
                    label: SageZZ(2 * parent.module_generator(label).b(self) / norm)
                    for label in parent.module_generating_set()
                    if parent.module_generator(label).b(self) != 0
                }
            )


def refine_root_lattice(lattice, cartan_type):
    r"""Record the Cartan type whose negative Cartan form built ``lattice``."""
    lattice._cartan_type = cartan_type
    return refine(lattice, RootLattices())


__all__ = ["RootLattices", "refine_root_lattice"]
