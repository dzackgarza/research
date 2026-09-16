"""Algebras graded by a monoid."""

from sage.categories.category_with_axiom import all_axioms
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    _unit_from_multiplication,
    _unit_morphism_from_element,
)
from dzack_research.preamble.categories.modules.graded_modules import (
    GradedModules,
    _concentrated_graded_module,
    _grading_identity,
    _require_grading_monoid,
)
from dzack_research.preamble.categories.modules.pure.modules import BilinearMap, Modules
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedCategoryOverBaseRing,
    OwnedIntegralDomains,
    OwnedRings,
    _engine_element,
    _own_ring,
)
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.refine import refine

# Bourbaki, Algebra III §4.9: an alternating graded algebra is one satisfying
# the Koszul sign rule in which every odd-degree element squares to zero.
if "Alternating" not in all_axioms:
    all_axioms.add("Alternating")


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

        self._underlying = Algebras(self.domain().base_ring()).Associative().Unital().Mor(self.domain(), self.codomain())(images)
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
        source = other.domain()
        homset = GradedAlgebras(
            source.base_ring(),
            _require_grading_monoid(source.grading_monoid()),
        ).Mor(source, self.codomain())
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
        if _require_grading_monoid(domain.grading_monoid()) != self._grading_monoid:
            raise ValueError("the source has the wrong grading monoid")
        if _require_grading_monoid(codomain.grading_monoid()) != self._grading_monoid:
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
        r"""A rank-one unital algebra concentrated in the identity degree."""
        ring = self.base_ring()
        monoid = self.grading_monoid()
        module = _concentrated_graded_module(ring, monoid)
        labels = module.module_generating_set()
        label = labels[0]
        generator = module.module_generator(label)
        multiplication = Modules(ring).tensor_product((module, module)).from_bilinear(
            BilinearMap(
                module,
                module,
                module,
                {(label, label): generator},
            )
        )
        unit = _unit_morphism_from_element(module, generator, ring)
        algebra = Algebras(ring).Associative().Unital()(
            module,
            multiplication,
            unit,
        )
        algebra._preamble_concentrated_degree = _grading_identity(monoid)
        refine(algebra, self)
        return algebra

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None, parity=None):
        r"""``GradedAlgebras(R, M, parity)``: the grading datum is that of ``GradedModules``."""
        graded_modules = GradedModules(base_ring, grading_monoid, parity)
        return OwnedCategoryOverBaseRing.__classcall__(
            cls, graded_modules.base_ring(), graded_modules
        )

    def __init__(self, base_ring, graded_modules: Parent) -> None:
        self._graded_modules = graded_modules
        super().__init__(base_ring)

    def grading_monoid(self) -> Parent:
        return self._graded_modules.grading_monoid()

    def parity_homomorphism(self):
        r"""Return the parity ``M -> ZZ/2`` stated with the grading."""
        return self._graded_modules.parity_homomorphism()

    def _repr_object_names(self) -> str:
        monoid = self.grading_monoid()
        names = "graded algebras" if monoid is _own_ring(SageZZ) else f"algebras graded by {monoid}"
        return f"{names} over {self.base()}"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self._graded_modules)

    def super_categories(self):
        return [
            Algebras(self.base_ring()).Associative().Unital(),
            self._graded_modules,
        ]

    class SubcategoryMethods:
        def Supercommutative(self):
            r"""Return the refinement satisfying the Koszul sign rule."""
            return self._with_axiom("Supercommutative")

    class Supercommutative(CategoryWithAxiom):
        r"""Graded algebras with ``xy = (-1)^(eps(p) eps(q)) yx`` on homogeneous elements.

        ``eps`` is the parity stated with the grading, so a grading that
        recorded none has no supercommutative refinement.  Sage's
        ``Supercommutative`` axiom states the same rule for ``ZZ/2``-gradings.
        """

        def __init__(self, base_category) -> None:
            base_category.parity_homomorphism()
            super().__init__(base_category)

        def grading_monoid(self) -> Parent:
            return self._base_category.grading_monoid()

        def parity_homomorphism(self):
            r"""Return the parity ``M -> ZZ/2`` the Koszul sign is read through."""
            return self._base_category.parity_homomorphism()

        def an_object(self):
            r"""The identity-degree rank-one algebra, where the sign rule is vacuous."""
            algebra = self._base_category.an_object()
            refine(algebra, Algebras(self.base_ring()).Commutative())
            refine(algebra, self)
            return algebra

        class SubcategoryMethods:
            def Alternating(self):
                r"""Return the refinement whose odd-degree elements square to zero."""
                return self._with_axiom("Alternating")

        class Alternating(CategoryWithAxiom):
            r"""Supercommutative graded algebras with ``x^2 = 0`` for ``eps(deg x) = 1``.

            Bourbaki, Algebra III §4.9, "alternating graded algebra"; Sage's
            ``commutative_dga`` calls the differential graded case strictly
            commutative.  The condition is independent of the sign rule over
            rings with 2-torsion.
            """

            def grading_monoid(self) -> Parent:
                return self._base_category.grading_monoid()

            def parity_homomorphism(self):
                r"""Return the parity ``M -> ZZ/2`` odd degree is read through."""
                return self._base_category.parity_homomorphism()

            def an_object(self):
                r"""The identity-degree rank-one algebra, where odd-square conditions are vacuous."""
                algebra = self._base_category.an_object()
                refine(algebra, self)
                return algebra

    class ParentMethods:
        def restrict_scalars(self, ring_map):
            r"""Restrict scalars while retaining this algebra's grading."""
            from dzack_research.preamble.categories.algebras.restricted_graded_algebras import (
                _restrict_graded_algebra_scalars,
            )

            return _restrict_graded_algebra_scalars(self, ring_map)

        def graded_derivations(self, target=None, shift=0):
            r"""Return degree-``shift`` graded derivations into ``target``."""
            from dzack_research.preamble.categories.algebras.derivations import (
                _graded_derivations,
            )

            return _graded_derivations(self, target=target, shift=shift)

        def homogeneous_degree(self, element):
            r"""Return the selected degree of one nonzero homogeneous element."""
            element = self(element)
            if element == self.zero():
                raise ValueError("zero has no selected homogeneous degree here")

            concentrated = self.__dict__.get("_preamble_concentrated_degree")
            if concentrated is not None:
                return concentrated

            components = getattr(element, "homogeneous_components", None)
            if callable(components):
                try:
                    component_items = components().items()
                except (AttributeError, NotImplementedError):
                    component_items = ()
                nonzero_degrees = {
                    int(degree)
                    for degree, component in component_items
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
            is_homogeneous = getattr(backend, "is_homogeneous", None)
            degree_function = getattr(backend, "degree", None)
            assert callable(is_homogeneous) and callable(degree_function), (
                "homogeneous degree is represented here when the graded-algebra backend exposes "
                "homogeneity and degree operations"
            )
            homogeneous = is_homogeneous()
            degree = degree_function()
            if not homogeneous:
                raise ValueError("the algebra element is not homogeneous")
            return self.grading_monoid()(int(degree))

        @cached_method
        def degree_zero_chart(self, localization):
            r"""Return ``(S_f)_0``, the degree-zero part of a graded localization.

            Localizing a graded ring at homogeneous elements grades the result
            by ``deg(a/s) = deg(a) - deg(s)``, now over the integers rather than
            the original monoid.  The degree-zero part is a subring, and for a
            single homogeneous ``f`` it is the affine coordinate ring of the
            standard open ``D_+(f)`` of ``Proj S``: the chart every projective
            construction is read in.

            A fraction is degree zero exactly when its numerator is homogeneous
            of the degree its denominator has, so the chart is cut out by that
            condition rather than by a chosen presentation in new variables.
            The degree of a fraction is well defined because ``a/s = b/t``
            forces ``at = bs``, hence equal degree differences, over an integral
            domain.
            """

            assert localization in LocalizationRings(), (
                "a degree-zero chart is the degree-zero part of a localization"
            )
            assert localization.localization_source() is self, (
                f"{localization} localizes a different ring than {self}"
            )
            assert self in OwnedIntegralDomains(), (
                f"the degree of a fraction over {self} is well defined once "
                "cancellation cannot change it, which an integral domain assures"
            )
            assert all(
                self(inverted).is_homogeneous() for inverted in localization.inverted_elements()
            ), "a graded localization inverts homogeneous elements"

            def is_degree_zero(fraction) -> bool:
                numerator = self(fraction.numerator())
                if numerator == self.zero():
                    return True
                if not numerator.is_homogeneous():
                    return False
                denominator = self(fraction.denominator())
                return self.homogeneous_degree(numerator) == self.homogeneous_degree(denominator)

            return localization.predicate_subring(
                is_degree_zero,
                f"a/s is homogeneous of degree zero in {localization}",
                OwnedRings().Commutative(),
            )

        def degree_zero_chart_restriction(self, source_localization, target_localization):
            r"""Return the overlap map ``(S_f)_0 -> (S_fg)_0`` of two standard charts.

            The restriction ``S_f -> S_fg`` preserves the grading, so it carries
            degree-zero fractions to degree-zero fractions and cuts down to the
            charts.  These maps compose because the localization restrictions
            do, which is the compatibility ``Proj`` needs on overlaps.
            """

            restriction = source_localization.restriction_to(target_localization)
            source_chart = self.degree_zero_chart(source_localization)
            target_chart = self.degree_zero_chart(target_localization)
            return source_chart.Mor(target_chart)(
                lambda element: target_chart(restriction(source_localization(element))),
            )

        def _Hom_(self, codomain, category=None):
            # Object-level Hom defaults to the underlying algebra category.
            # Degree-preserving maps are selected explicitly through
            # ``GradedAlgebras(...).Mor``.
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
        if domain.base_ring() is not self.base_ring() or codomain.base_ring() is not self.base_ring():
            raise ValueError("graded algebra morphisms require one common base ring")
        if _require_grading_monoid(domain.grading_monoid()) != self.grading_monoid():
            raise ValueError("the source has the wrong grading monoid")
        if _require_grading_monoid(codomain.grading_monoid()) != self.grading_monoid():
            raise ValueError("the target has the wrong grading monoid")
        return self.HomCategory().Of(domain, codomain)

    _HomCategory = GradedAlgebraHomCategoryConstruction

    def _call_(self, multiplication):
        module = multiplication.codomain()
        graded = GradedModules(self.base_ring(), self.grading_monoid())
        if module not in graded:
            raise TypeError(
                f"{module} is not a module graded by {self.grading_monoid()}"
            )
        unit = _unit_from_multiplication(multiplication)
        eta = _unit_morphism_from_element(
            module,
            unit,
            self.base_ring(),
        )
        algebra = Algebras(self.base_ring()).Associative().Unital()(
            module,
            multiplication,
            eta,
        )
        refine(algebra, self)
        return algebra


__all__ = [
    "GradedAlgebraHomCategoryConstruction",
    "GradedAlgebraHomset",
    "GradedAlgebraMorphism",
    "GradedAlgebras",
]
