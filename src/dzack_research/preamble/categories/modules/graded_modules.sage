r"""Graded modules and graded algebras.

A graded module is $M=\bigoplus_n M_n$, and the decomposition is structure it
carries rather than a fact about it.  Everything else here is read off that:
the degree of an element is where its support sits, an element is homogeneous
when its support sits in one place, and $M_n$ is a submodule of $M$ with its
inclusion, not a separate object built to stand for it.

The preamble spoke about grading in four places before it had this node --
degrees, homogeneous components, "the degree-two piece" -- so each
construction stated its own grading and the tensor algebra ended up owning
accessors that belong to any graded thing.  The grading is one notion, and
this is where it lives.
"""

from typing import Protocol, TYPE_CHECKING, Self

from sage.misc.abstract_method import abstract_method
from sage.rings.infinity import Infinity as _Infinity
from sage.rings.infinity import MinusInfinity

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing

if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element, Module, OrderedSet


if TYPE_CHECKING:
    class GradedModuleParent(Protocol):
        r"""What a parent placed in ``GradedModules(R)`` supplies.

        A graded module is a framed module, so the framing surface the
        grading is read off arrives with the placement.
        """

        def module_generators(self) -> "OrderedSet": ...
        def submodule(self, module_generators: "OrderedSet") -> "Module": ...
        def module_generators_of_degree(self, degree: "Integer") -> "OrderedSet": ...
        def degree_on_module_generator(self, module_generator: "Element") -> "Integer": ...
        def module_generator(self, label: "Element") -> "Element": ...
        def zero(self) -> "Element": ...

    class GradedModuleElement(Protocol):
        r"""What an element of a graded module supplies: the module it lies
        in, and its own finite support in that module's framing."""

        def parent(self) -> "GradedModuleParent": ...
        def coefficients(self) -> dict: ...


class GradedModules(OwnedCategoryOverBaseRing):
    r"""Modules \(M=\bigoplus_n M_n\) over a base ring."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "graded modules"

    def super_categories(self) -> list:
        # Local: the module node reaches this one, so a module-level import
        # would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        @abstract_method
        def degree_on_module_generator(self, module_generator: "Element") -> "Integer":
            r"""Return the degree of a module generator.

            The grading itself: a framed module is graded exactly by saying
            where each of its generators sits, and everything else in this
            category follows from that.
            """

        def module_generators_of_degree(self: "GradedModuleParent", degree: "Integer") -> "OrderedSet":
            r"""Return the module generators sitting in one degree."""
            # Local: the set node reaches this module, so a module-level
            # import would close that cycle.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            return finite_ordered_set(
                [
                    module_generator
                    for module_generator in self.module_generators()
                    if self.degree_on_module_generator(module_generator) == degree
                ]
            )

        def graded_piece(self: "GradedModuleParent", degree: "Integer") -> "Module":
            r"""Return \(M_n\), as the submodule of \(M\) that it is.

            A subobject, so it carries its inclusion \(M_n\hookrightarrow M\):
            the grading says \(M\) *is* the sum of these, which is a statement
            about maps into \(M\) and not about a family of unrelated modules.
            """
            return self.submodule(self.module_generators_of_degree(degree))

    class ElementMethods:
        def degree(self: "GradedModuleElement") -> "Integer | MinusInfinity":
            r"""Return the top degree in this element's support.

            The zero element has degree \(-\infty\), which is what makes the
            degree additive on products.
            """
            parent = self.parent()
            support = self.coefficients()
            if not support:
                return -_Infinity
            return max(
                parent.degree_on_module_generator(module_generator)
                for module_generator in support
            )

        def is_homogeneous(self: "GradedModuleElement") -> bool:
            r"""Return whether the support sits in one degree.

            The zero element is homogeneous, vacuously and usefully: it
            belongs to every graded piece.
            """
            parent = self.parent()
            degrees = {
                parent.degree_on_module_generator(module_generator)
                for module_generator in self.coefficients()
            }
            homogeneous: bool = len(degrees) <= 1
            return homogeneous

        def homogeneous_components(self: "GradedModuleElement") -> dict:
            r"""Return \(d\mapsto\) the degree-\(d\) part, over the support.

            Their sum is this element, which is what makes \(M=\bigoplus_nM_n\)
            a decomposition rather than a filtration.
            """
            parent = self.parent()
            components: dict = {}
            for module_generator, coefficient in self.coefficients().items():
                degree = parent.degree_on_module_generator(module_generator)
                part = components.get(degree, parent.zero())
                components[degree] = part + coefficient * parent.module_generator(
                    module_generator
                )
            return components

        def truncate(self: "GradedModuleElement", degree: "Integer") -> "Element":
            r"""Return the part of degree below ``degree``.

            The image in \(M/M_{\geq d}\), lifted back: the terms it drops are
            exactly the ones that quotient kills.
            """
            parent = self.parent()
            kept = parent.zero()
            for module_generator, coefficient in self.coefficients().items():
                if parent.degree_on_module_generator(module_generator) < degree:
                    kept = kept + coefficient * parent.module_generator(
                        module_generator
                    )
            return kept


class GradedAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras \(A=\bigoplus_nA_n\) with \(A_iA_j\subseteq A_{i+j}\).

    The grading is compatible with the product, which is what makes the degree
    additive and each \(A_n\) a module over \(A_0\).  Every free construction
    in the preamble is one of these: the degree of a monomial is the number of
    letters it has, however that construction spells them.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "graded algebras"

    def super_categories(self) -> list:
        # Local: the algebra node reaches this one, so a module-level import
        # would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        return [GradedModules(self.base_ring()), Algebras(self.base_ring())]
