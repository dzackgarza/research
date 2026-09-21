r"""Differential graded algebra categories and their morphisms."""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    _algebra_on_module,
    _root_algebra_law_decisions,
)
from dzack_research.preamble.categories.algebras.derivations import GradedDerivation
from dzack_research.preamble.categories.algebras.graded_algebras import (
    GradedAlgebraMorphism,
    GradedAlgebras,
)
from dzack_research.preamble.categories.modules.cochain_complexes import CochainComplexes
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets


class DegreewiseLinearMorphism(Morphism):
    r"""An ``R``-linear map between two represented homogeneous pieces.

    This is deliberately independent of a selected finite framing. When the
    source and target pieces admit the finite module-morphism realization,
    :meth:`represented_module_morphism` exposes it and therefore enables the
    usual kernel/image algorithms; otherwise the component remains a genuine
    morphism with exact evaluation but no fabricated finite presentation.
    """

    def __init__(self, domain, codomain, function) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("a differential component requires one base ring")
        self._function = function
        Morphism.__init__(
            self,
            Sets().Mor(domain, codomain),
        )

    def _call_(self, element):
        if element.parent() is not self.domain():
            element = self.domain()(element)
        image = self._function(element)
        return image if image.parent() is self.codomain() else self.codomain()(image)

    def __call__(self, element):
        return self._call_(element)

    def represented_module_morphism(self):

        source = self.domain()
        target = self.codomain()
        ring = source.base_ring()
        assert source in FramedModules(ring) and target in FramedModules(ring), (
            "materializing a differential component as a module morphism requires selected framings on both endpoints"
        )
        labels = source.module_generating_set()
        assert labels.cardinality().is_finite(), (
            "materializing a differential component as a module morphism requires a finite selected source framing"
        )
        return source.module_category().Mor(source, target)(
            {label: self(source.module_generator(label)) for label in labels}
        )

    def kernel(self):
        return self.represented_module_morphism().kernel()

    def image(self):
        return self.represented_module_morphism().image()


class DifferentialComponentMorphism(DegreewiseLinearMorphism):
    r"""A degreewise component of a represented DGA differential."""


class DifferentialGradedAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""That de Rham algebra, whose differential makes it a DGA."""
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebras

        ring = self.base_ring()
        return DeRhamAlgebras(ring).an_object()

    def _call_(self, algebra, differential):
        r"""Equip one exact graded algebra with one selected differential.

        The graded algebra is retained as defining data.  A caller-supplied
        differential may leave its graded-Leibniz or square-zero law at the
        declared ``Unknown`` frontier; construction-derived differentials use
        :meth:`_from_constructed_differential` instead of turning generator
        observations into proofs.
        """
        graded = GradedAlgebras(self.base_ring())
        if algebra not in graded:
            raise TypeError(
                "a differential graded algebra is constructed on a graded algebra over the same base ring"
            )
        if isinstance(differential, Differential):
            if differential.algebra() is not algebra:
                raise ValueError("the selected differential belongs to another graded algebra")
            function = differential
            decisions = (
                differential.graded_leibniz_decision(),
                differential.square_zero_decision(),
            )
        elif callable(differential):
            function = differential
            decisions = (Unknown, Unknown)
        else:
            raise TypeError("a differential is a represented degree-one element map")
        return self._from_differential_data(algebra, function, decisions)

    def _from_constructed_differential(self, algebra, differential):
        r"""Construct when the supplying owner proves Leibniz and square-zero."""
        if not callable(differential):
            raise TypeError("a constructed differential is represented by an element map")
        return self._from_differential_data(algebra, differential, (True, True))

    def _from_differential_data(self, algebra, differential, decisions):
        graded = GradedAlgebras(self.base_ring())
        if algebra not in graded:
            raise TypeError(
                "a differential graded algebra is constructed on a graded algebra over the same base ring"
            )
        leibniz, square_zero = decisions
        if not (leibniz is True or leibniz is Unknown) or not (
            square_zero is True or square_zero is Unknown
        ):
            raise ValueError("differential law decisions are True or Unknown")
        placements = [self]
        ring = self.base_ring()
        supercommutative = algebra in graded.Supercommutative()
        if (
            not supercommutative
            and algebra in graded.Commutative()
            and (-ring.one() == ring.one()) is True
        ):
            # In characteristic two the Koszul sign is always +1, so ordinary
            # graded commutativity implies the supercommutative sign rule.
            supercommutative = True
        if supercommutative:
            placements.append(self.Supercommutative())
        if algebra in graded.Supercommutative().Alternating():
            placements.append(self.Supercommutative().Alternating())
        law_decisions = _root_algebra_law_decisions(algebra)
        law_decisions["grading"] = algebra.grading_compatibility_decision()
        return _algebra_on_module(
            algebra,
            algebra.multiplication_morphism(),
            placement=tuple(placements),
            unit=algebra.one(),
            construction_data={
                "dga_underlying_algebra": algebra,
                "dga_differential_function": differential,
                "dga_differential_decisions": (leibniz, square_zero),
            },
            law_decisions=law_decisions,
        )

    @classmethod
    def _repr_object_names(cls):
        return "differential graded algebras"

    def super_categories(self):

        return [GradedAlgebras(self.base_ring()), CochainComplexes(self.base_ring())]

    _MorCategory = None

    def degree_zero_algebra(self):
        r"""Return the functor taking a DGA to its degree-zero algebra."""
        from dzack_research.preamble.categories.functors.de_rham import (
            _degree_zero_dga_functor,
        )

        return _degree_zero_dga_functor(self.base_ring())

    def cohomology_algebra(self):
        r"""Return the graded cohomology-algebra functor ``H^*`` on this category."""
        from dzack_research.preamble.categories.functors.cohomology import (
            _cohomology_algebra_functor,
        )

        return _cohomology_algebra_functor(self.base_ring())

    class ParentMethods:
        def __init__(
            self,
            dga_underlying_algebra=None,
            dga_differential_function=None,
            dga_differential_decisions=None,
            **rest,
        ) -> None:
            if dga_underlying_algebra is not None:
                self._preamble_dga_underlying_algebra = dga_underlying_algebra
            super().__init__(**rest)
            if dga_differential_function is not None:
                decisions = (
                    (Unknown, Unknown)
                    if dga_differential_decisions is None
                    else tuple(dga_differential_decisions)
                )
                _fix_selected_differential(
                    self,
                    dga_differential_function,
                    graded_leibniz=decisions[0],
                    square_zero=decisions[1],
                )

        def underlying_graded_algebra(self):
            r"""Return the exact graded algebra equipped with this differential."""
            return self.__dict__.get("_preamble_dga_underlying_algebra", self)

        def cohomology_algebra(self):
            r"""Return the represented graded cohomology algebra ``H^*(self)``."""
            from dzack_research.preamble.categories.algebras.cohomology_algebras import (
                CohomologyAlgebras,
            )

            return CohomologyAlgebras(self.base_ring())(self)

        def degree_index_set(self):
            r"""Return the grading object as the inherited cochain degree set."""
            return self.grading_monoid()

        def graded_algebra(self):
            return self

        def dga(self):
            return self

        def regular_dg_module(self):
            r"""Read this DGA as its canonical right DG-module over itself."""
            return self

        def right_action(self):
            return lambda module_element, algebra_element: module_element * algebra_element

        def act(self, module_element, algebra_element):
            return module_element * algebra_element

        def is_differential_graded_module(self) -> bool:
            return True

        def _Hom_(self, codomain, category=None):
            dgas = DifferentialGradedAlgebras(self.base_ring())
            if codomain in dgas and (
                category is None or category.is_subcategory(dgas)
            ):
                return dgas.Mor(self, codomain)
            return super()._Hom_(codomain, category=category)

        def differential(self):
            return self._preamble_differential

        def d(self, element):
            return self.differential()(element)

        @cached_method
        def _negative_cochain_zero_module(self):
            r"""The represented zero module used by the inherited cochain complex."""
            return self.base_ring().free_module(finite_ordered_set(()))

        def differential_component(self, degree):
            degree = int(degree)
            if degree < 0:
                source = self._negative_cochain_zero_module()
                if degree == -1:
                    target = self.graded_piece(0)
                else:
                    target = source
                return DifferentialComponentMorphism(
                    source,
                    target,
                    lambda _element: target.zero(),
                )
            source = self.graded_piece(degree)
            target = self.graded_piece(degree + 1)

            def component(element):
                source_element = self.from_graded_piece(degree, element)
                image = self.d(source_element)
                return image.homogeneous_component(degree + 1)

            return DifferentialComponentMorphism(source, target, component)


def StrictlyCommutativeDifferentialGradedAlgebras(base_ring):
    r"""The computed join ``DifferentialGradedAlgebras(R).Supercommutative().Alternating()``.

    The specification names the category; the join has no class of its own.
    """
    return DifferentialGradedAlgebras(base_ring).Supercommutative().Alternating()


class Differential(GradedDerivation):
    r"""A represented degree-one square-zero graded derivation."""

    def __init__(self, algebra, function) -> None:
        GradedDerivation.__init__(
            self,
            algebra.graded_derivations(algebra, shift=1),
            function,
        )
        observed = self._square_zero_on_generators()
        match observed:
            case False:
                raise ValueError("the proposed differential does not square to zero")
            case _:
                pass
        derived = self._square_zero_derivation()
        match derived:
            case None:
                self._square_zero_decision = Unknown
            case decision if decision is True or decision is Unknown:
                self._square_zero_decision = decision
            case _:
                raise ValueError("a differential square-zero premise is True or Unknown")

    def _square_zero_derivation(self):
        return None

    def square_zero_decision(self):
        return self._square_zero_decision

    def _square_zero_on_generators(self):
        algebra = self.algebra()
        try:
            labels = algebra.algebra_generating_set()
            finite = labels.cardinality().is_finite()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return Unknown
        match finite:
            case True:
                pass
            case False:
                return Unknown
        for label in labels:
            generator = algebra.algebra_generator(label)
            match self(self(generator)) == algebra.zero():
                case True:
                    pass
                case False:
                    return False
                case _:
                    return Unknown
        return True


class _RetainedDifferential(Differential):
    r"""A differential carrying law decisions established by its constructor."""

    def __init__(self, algebra, function, graded_leibniz, square_zero) -> None:
        self._retained_graded_leibniz = graded_leibniz
        self._retained_square_zero = square_zero
        super().__init__(algebra, function)

    def _graded_derivation_derivation(self):
        return self._retained_graded_leibniz

    def _square_zero_derivation(self):
        return self._retained_square_zero


def _fix_selected_differential(
    algebra,
    function,
    *,
    graded_leibniz=Unknown,
    square_zero=Unknown,
) -> None:
    r"""Install one selected DGA differential after the algebra datum exists."""
    if algebra.__dict__.get("_preamble_differential") is not None:
        raise ValueError(f"{algebra} already has a selected differential")
    if not (graded_leibniz is True or graded_leibniz is Unknown) or not (
        square_zero is True or square_zero is Unknown
    ):
        raise ValueError("differential law decisions are True or Unknown")
    algebra._preamble_differential = _RetainedDifferential(
        algebra,
        function,
        graded_leibniz,
        square_zero,
    )


class DGAMorphism(Morphism):
    r"""A graded algebra morphism commuting with the selected differentials."""

    def __init__(
        self,
        parent,
        morphism,
        *,
        differential_compatibility=None,
    ) -> None:
        Morphism.__init__(self, parent)
        source = self.domain()
        graded_mor = GradedAlgebras(
            source.base_ring(), source.grading_monoid()
        ).Mor(source, self.codomain())
        if isinstance(morphism, GradedAlgebraMorphism) and morphism.parent() is graded_mor:
            self._underlying = morphism
        else:
            self._underlying = graded_mor(morphism)
        observed = self._decide_differential_compatibility()
        if observed is False:
            raise ValueError("a DGA morphism must commute with the differential")
        if differential_compatibility is None:
            self._differential_compatibility = observed
        else:
            if not (
                differential_compatibility is True
                or differential_compatibility is Unknown
            ):
                raise ValueError("differential compatibility is True or Unknown")
            self._differential_compatibility = differential_compatibility

    def underlying_graded_algebra_morphism(self):
        return self._underlying

    def underlying_algebra_morphism(self):
        return self._underlying.underlying_algebra_morphism()

    def degree_preservation_decision(self):
        return self._underlying.degree_preservation_decision()

    def differential_compatibility_decision(self):
        return self._differential_compatibility

    def _decide_differential_compatibility(self):
        source = self.domain()
        target = self.codomain()
        try:
            labels = source.algebra_generating_set()
            finite = labels.cardinality().is_finite()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return Unknown
        if not finite:
            return Unknown
        comparisons = tuple(
            self._underlying(source.d(source.algebra_generator(label)))
            == target.d(self._underlying(source.algebra_generator(label)))
            for label in labels
        )
        if any(answer is False for answer in comparisons):
            return False
        linear = (
            self.underlying_algebra_morphism().linearity_decision() is True
            and source.differential().linearity_decision() is True
            and target.differential().linearity_decision() is True
        )
        return True if linear and all(answer is True for answer in comparisons) else Unknown

    def _call_(self, element):
        return self._underlying(element)

    def __call__(self, element):
        return self._call_(element)

    def component(self, degree):
        r"""Return the degree-``degree`` linear component of this DGA map."""
        degree = int(degree)
        if degree < 0:
            source = self.domain()._negative_cochain_zero_module()
            target = self.codomain()._negative_cochain_zero_module()
            return DegreewiseLinearMorphism(
                source,
                target,
                lambda _element: target.zero(),
            )
        source = self.domain().graded_piece(degree)
        target = self.codomain().graded_piece(degree)

        def image(element):
            source_element = self.domain().from_graded_piece(degree, element)
            return self(source_element).homogeneous_component(degree)

        return DegreewiseLinearMorphism(source, target, image)

    def __mul__(self, other):
        if not isinstance(other, DGAMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain()
        decision = (
            True
            if self.differential_compatibility_decision() is True
            and other.differential_compatibility_decision() is True
            else Unknown
        )
        return DifferentialGradedAlgebras(source.base_ring()).Mor(
            source, self.codomain()
        )._from_differential_preserving_underlying_morphism(
            self.underlying_graded_algebra_morphism()
            * other.underlying_graded_algebra_morphism(),
            decision,
        )


class DGAMor(CategoricalMor):
    Element = DGAMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("DGA morphisms require one common differential base ring")
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, morphism):
        return self.element_class(self, morphism)

    def _from_differential_preserving_generator_map(self, images):
        r"""Construct from generator images when the construction proves all DGA laws."""
        source = self.domain()
        graded = GradedAlgebras(source.base_ring(), source.grading_monoid())
        underlying = graded.Mor(source, self.codomain())._from_degree_preserving_generator_map(
            images
        )
        return self.element_class(
            self,
            underlying,
            differential_compatibility=True,
        )

    def _from_differential_preserving_underlying_morphism(self, morphism, decision=True):
        r"""Lift an actual graded algebra morphism with a retained differential-law premise."""
        return self.element_class(
            self,
            morphism,
            differential_compatibility=decision,
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a DGA endomorphism Mor")
        source = self.domain()
        underlying = GradedAlgebras(
            source.base_ring(), source.grading_monoid()
        ).Mor(source, source).identity()
        return self._from_differential_preserving_underlying_morphism(
            underlying,
            True,
        )


class DGAMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self):
        return DGAMor


DifferentialGradedAlgebras._MorCategory = DGAMorCategoryConstruction


__all__ = [
    "DGAMor",
    "DGAMorCategoryConstruction",
    "DGAMorphism",
    "DegreewiseLinearMorphism",
    "Differential",
    "DifferentialComponentMorphism",
    "DifferentialGradedAlgebras",
    "StrictlyCommutativeDifferentialGradedAlgebras",
]
