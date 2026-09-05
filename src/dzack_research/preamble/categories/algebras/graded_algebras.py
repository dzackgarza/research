"""Algebras graded by a monoid."""

from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.modules.graded_modules import (
    require_grading_monoid,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_element,
    _own_ring,
)
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    algebra_from_multiplication,
    algebra_homset,
)
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.refine import refine


def _homogeneous_degree(element):
    r"""Return the degree owned by ``element.parent()``."""
    parent = element.parent()
    try:
        return parent.homogeneous_degree(element)
    except AttributeError as error:
        raise NotImplementedError(
            "this graded object does not expose homogeneous element degrees"
        ) from error


class GradedAlgebraMorphism(Morphism):
    r"""An algebra morphism preserving the selected grading."""

    def __init__(self, parent, images, *, check_degrees=True) -> None:
        Morphism.__init__(self, parent)

        self._underlying = algebra_homset(self.domain(), self.codomain())(images)
        if check_degrees:
            self._check_degrees()

    def underlying_algebra_morphism(self):
        return self._underlying

    def _check_degrees(self) -> None:
        domain = self.domain()
        codomain = self.codomain()
        try:
            labels = domain.algebra_generating_set()
        except AttributeError as error:
            raise NotImplementedError(
                "a represented graded morphism currently requires a selected algebra framing"
            ) from error
        try:
            finite = labels.cardinality().is_finite()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            finite = False
        if not finite:
            raise NotImplementedError(
                "an arbitrary graded generator map on an infinite framing cannot be "
                "verified by exhaustive evaluation"
            )
        for label in labels:
            generator = domain.algebra_generator(label)
            source_degree = _homogeneous_degree(generator)
            image = self._underlying(generator)
            if image == codomain.zero():
                continue
            target_degree = _homogeneous_degree(image)
            if target_degree != source_degree:
                raise ValueError(
                    f"a graded algebra morphism must preserve degree: generator {label!r} "
                    f"has degree {source_degree}, but its image has degree {target_degree}"
                )

    def _call_(self, element):
        return self._underlying(element)

    def __call__(self, element):
        return self._call_(element)

    def __mul__(self, other):
        if not isinstance(other, GradedAlgebraMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        homset = graded_algebra_homset(other.domain(), self.codomain())
        return homset._from_degree_preserving_generator_map(
            lambda label: self(
                other(other.domain().algebra_generator(label))
            )
        )


class GradedAlgebraHomset(CategoricalHomset):
    Element = GradedAlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        self._grading_monoid = hom_family.base_category().grading_monoid()
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("graded algebra morphisms require one common base ring")
        if require_grading_monoid(domain.grading_monoid()) != self._grading_monoid:
            raise ValueError("the source has the wrong grading monoid")
        if require_grading_monoid(codomain.grading_monoid()) != self._grading_monoid:
            raise ValueError("the target has the wrong grading monoid")
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
        )

    def grading_monoid(self):
        return self._grading_monoid

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    def _from_degree_preserving_generator_map(self, images):
        r"""Construct a graded map whose degree preservation is structural."""
        return self.element_class(self, images, check_degrees=False)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a graded algebra endomorphism homset")
        return self._from_degree_preserving_generator_map(
            lambda label: self.domain().algebra_generator(label)
        )


class GradedAlgebraHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return GradedAlgebraHomset


def graded_algebra_homset(domain, codomain) -> GradedAlgebraHomset:
    ring = domain.base_ring()
    if codomain.base_ring() is not ring:
        raise ValueError("graded algebra morphisms require one common base ring")
    source_monoid = require_grading_monoid(domain.grading_monoid())
    if require_grading_monoid(codomain.grading_monoid()) != source_monoid:
        raise ValueError("graded algebra morphisms require one common grading monoid")
    graded = GradedAlgebras(ring, source_monoid)
    if domain not in graded or codomain not in graded:
        raise TypeError("both endpoints must be objects of the same graded algebra category")
    return graded.Mor(domain, codomain)


class GradedAlgebras(OwnedCategoryOverBaseRing):
    r"""Associative unital algebras graded by a monoid.

    Let \(M\) be a monoid. An \(M\)-graded \(R\)-algebra is an associative
    unital \(R\)-algebra \(A\) together with a direct-sum decomposition
    \(A = \bigoplus_{m \in M} A_m\) of the underlying module such that the
    product sends \(A_m \times A_{m'}\) into \(A_{mm'}\).

    The default monoid is \(\mathbb{Z}\) (additive), which is Sage's graded
    algebra axiom. The additive monoid \(\mathbb{N}\) is the nonnegative
    case. This is the nLab definition of a graded algebra; Stacks Project
    tag 00JL is the special case \(M = \mathbb{N}\).
    """

    def an_object(self):
        r"""The de Rham algebra of the polynomial algebra, graded by form degree."""
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebras

        return DeRhamAlgebras(self.base_ring()).an_object()

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None):
        monoid = require_grading_monoid(grading_monoid)
        return OwnedCategoryOverBaseRing.__classcall__(cls, base_ring, monoid)

    def __init__(self, base_ring, grading_monoid: Parent) -> None:
        self._grading_monoid = grading_monoid
        super().__init__(base_ring)

    def grading_monoid(self) -> Parent:
        return self._grading_monoid

    def _repr_object_names(self) -> str:
        monoid = self.grading_monoid()
        names = "graded algebras" if monoid is _own_ring(SageZZ) else f"algebras graded by {monoid}"
        return f"{names} over {self.base()}"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.grading_monoid())

    def super_categories(self):

        graded_modules = GradedModules(self.base_ring(), self.grading_monoid())
        algebra = Algebras(self.base_ring())
        return [algebra, graded_modules]

    class ParentMethods:
        def homogeneous_degree(self, element):
            r"""Return the selected degree of one nonzero homogeneous element."""
            element = self(element)
            if element == self.zero():
                raise ValueError("zero has no selected homogeneous degree here")

            components = getattr(element, "homogeneous_components", None)
            if callable(components):
                nonzero_degrees = {
                    int(degree)
                    for degree, component in components().items()
                    if component != component.parent().zero()
                }
                if nonzero_degrees:
                    if len(nonzero_degrees) != 1:
                        raise ValueError("the algebra element is not homogeneous")
                    return self.grading_monoid()(next(iter(nonzero_degrees)))

            coefficients = getattr(element, "monomial_coefficients", None)
            if callable(coefficients):
                degrees = set()
                for label, coefficient in coefficients().items():
                    if not coefficient:
                        continue
                    if hasattr(label, "summand_index"):
                        degrees.add(int(label.summand_index()))
                    elif hasattr(label, "degree"):
                        degrees.add(int(label.degree()))
                if degrees:
                    if len(degrees) != 1:
                        raise ValueError("the algebra element is not homogeneous")
                    return self.grading_monoid()(next(iter(degrees)))

            presentation = self
            representative = element
            if hasattr(self, "lift_to_presentation") and hasattr(
                self, "presentation_ring"
            ):
                presentation = self.presentation_ring()
                representative = self.lift_to_presentation(element)
            backend = _engine_element(presentation, representative)
            try:
                homogeneous = backend.is_homogeneous()
                degree = backend.degree()
            except AttributeError as error:
                raise NotImplementedError(
                    "this graded algebra has no represented homogeneous-degree backend"
                ) from error
            if not homogeneous:
                raise ValueError("the algebra element is not homogeneous")
            return self.grading_monoid()(int(degree))

        def _Hom_(self, codomain, category=None):
            # Object-level Hom defaults to the underlying algebra category.
            # Degree-preserving maps are selected explicitly through
            # ``GradedAlgebras(...).Hom`` / ``graded_algebra_homset``.
            return super()._Hom_(codomain, category=category)

    class ElementMethods:
        def is_homogeneous(self):
            try:
                self.parent().homogeneous_degree(self)
            except ValueError:
                return False
            return True

        def degree(self):
            return self.parent().homogeneous_degree(self)

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a graded-algebra Hom requires two objects of this category")
        return graded_algebra_homset(domain, codomain)

    _HomCategory = GradedAlgebraHomCategoryConstruction

    def _call_(self, multiplication):

        algebra = algebra_from_multiplication(
            multiplication, self.base_ring(), unital=True
        )
        module = multiplication.codomain()
        graded = GradedModules(self.base_ring(), self.grading_monoid())
        if module not in graded:
            raise TypeError(
                f"{module} is not a module graded by {self.grading_monoid()}"
            )
        return refine(algebra, [graded, self])


__all__ = [
    "GradedAlgebraHomCategoryConstruction",
    "GradedAlgebraHomset",
    "GradedAlgebraMorphism",
    "GradedAlgebras",
    "graded_algebra_homset",
]
