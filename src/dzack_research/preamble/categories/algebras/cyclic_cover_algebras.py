r"""Cyclic-cover algebras from invertible sheaves and branch sections."""

from typing import Any

from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
)
from dzack_research.preamble.categories.divisors.invertible_sheaves import (
    InvertibleSheaf,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)


def _rank_one_coefficient(module: Any, element: Any) -> Any:
    labels = module.module_generating_set()
    if not labels.cardinality().is_finite() or int(labels.cardinality()) != 1:
        raise TypeError("a cyclic-cover branch trivialization requires rank-one local modules")
    label = next(iter(labels))
    coefficients = module_coefficients(module(element), module)
    return coefficients[label] if label in coefficients else module.base_ring().zero()


class CyclicCoverAlgebra(SageObject):
    r"""The algebra ``oplus_{i=0}^{n-1} L^{-i}`` attached to ``(L,s,n)``.

    On a chart trivializing ``L`` by ``e_i``, write
    ``s = f_i e_i^n``.  The local algebra is the selected finite-free quotient
    ``R_i[z_i]/(z_i^n-f_i)``.  If ``e_i = u_ij e_j`` on an overlap, the algebra
    transition is ``z_i -> u_ij^{-1} z_j``.  The supplied branch section is
    required to carry exactly the ``u_ij^n`` transition data of ``L^n``.
    """

    def __init__(self, line_bundle: InvertibleSheaf, branch_section: Any, degree: int) -> None:
        if not isinstance(line_bundle, InvertibleSheaf):
            raise TypeError("cyclic-cover data requires an invertible sheaf")
        degree = int(degree)
        if degree < 2:
            raise ValueError("a cyclic cover has degree at least two")

        try:
            branch_parent = branch_section.parent()
            branch_datum = branch_parent.gluing_datum()
        except AttributeError as error:
            raise TypeError(
                "the branch section must be a represented compatible section of L^n"
            ) from error
        if branch_datum.cover() is not line_bundle.cover():
            raise ValueError("the branch section and line bundle require one affine cover")

        branch_power = InvertibleSheaf(branch_datum)
        for left in range(len(line_bundle.cover().opens())):
            for right in range(left + 1, len(line_bundle.cover().opens())):
                expected = line_bundle.transition_unit(left, right) ** degree
                actual = branch_power.transition_unit(left, right)
                if actual != expected:
                    raise ValueError(
                        "the branch section is not represented as a section of the stated L^n"
                    )

        self._line_bundle = line_bundle
        self._branch_power = branch_power
        self._branch_section = branch_parent(branch_section)
        self._degree = degree
        self._local_branch_coefficients = tuple(
            _rank_one_coefficient(
                branch_power.local_module(index),
                self._branch_section.component(index),
            )
            for index in range(len(line_bundle.cover().opens()))
        )
        self._local_algebras = tuple(
            self._build_local_algebra(index)
            for index in range(len(line_bundle.cover().opens()))
        )
        self._gluing_datum = self._build_algebra_gluing_datum()

    def line_bundle(self) -> InvertibleSheaf:
        return self._line_bundle

    def branch_power(self) -> InvertibleSheaf:
        return self._branch_power

    def branch_section(self) -> Any:
        return self._branch_section

    def degree(self) -> int:
        return self._degree

    def cover(self) -> Any:
        return self.line_bundle().cover()

    def scheme(self) -> Any:
        return self.line_bundle().scheme()

    def local_branch_coefficient(self, index: int) -> Any:
        return self._local_branch_coefficients[int(index)]

    def _build_local_algebra(self, index: int) -> Any:
        ring = self.cover().open(index).coordinate_algebra()
        presentation = PolynomialRing(ring, "z")
        z = presentation.algebra_generator("z")
        return FinitelyPresentedAlgebra(
            presentation,
            (z ** self.degree() - self.local_branch_coefficient(index),),
        )

    def local_algebra(self, index: int) -> Any:
        return self._local_algebras[int(index)]

    def local_algebras(self) -> tuple[Any, ...]:
        return self._local_algebras

    def local_underlying_module(self, index: int) -> Any:
        r"""Return the same local algebra object, carrying its rank-``n`` module basis."""

        return self.local_algebra(index)

    def local_multiplication(self, index: int) -> Any:
        return self.local_algebra(index).multiplication_morphism()

    def local_presentation(self, index: int) -> Any:
        return self.local_algebra(index).presentation()

    def local_equation(self, index: int) -> Any:
        relations = self.local_algebra(index).relations()
        return relations.value(next(iter(relations.index_set())))

    def _transition(self, source_index: int, target_index: int) -> Isomorphism:
        source = self.cover().restrict_algebra(
            self.local_algebra(source_index),
            source_index,
            target_index,
        )
        target = self.cover().restrict_algebra(
            self.local_algebra(target_index),
            target_index,
            source_index,
        )
        unit = self.line_bundle().transition_unit(source_index, target_index)
        source_z = source.algebra_generator("z")
        target_z = target.algebra_generator("z")
        forward = source.Mor(target)(
            {
                "z": target(unit.inverse_of_unit()) * target_z,
            }
        )
        inverse = target.Mor(source)(
            {
                "z": source(unit) * source_z,
            }
        )
        return Isomorphism(forward, inverse)

    def _build_algebra_gluing_datum(self) -> Any:
        transitions = {
            (left, right): self._transition(left, right)
            for left in range(len(self.local_algebras()))
            for right in range(left + 1, len(self.local_algebras()))
        }
        return self.cover().glue_algebras(self.local_algebras(), transitions)

    def gluing_datum(self) -> Any:
        return self._gluing_datum

    def sheaf(self) -> Any:
        return self.gluing_datum().sheaf()

    def underlying_module_datum(self) -> Any:
        return self.gluing_datum().underlying_module_datum()

    def global_sections(self) -> Any:
        return self.gluing_datum().compatible_sections()

    sections = global_sections

    def restricted_algebra(self, chart_index: int, *intersection_indices: int) -> Any:
        return self.gluing_datum().restricted_algebra(
            chart_index,
            *intersection_indices,
        )

    def transition(self, source_index: int, target_index: int) -> Any:
        return self.gluing_datum().transition(source_index, target_index)

    def _repr_(self) -> str:
        return (
            f"Degree-{self.degree()} cyclic-cover algebra on {self.scheme()} "
            f"from {self.line_bundle()}"
        )


__all__ = ["CyclicCoverAlgebra"]
