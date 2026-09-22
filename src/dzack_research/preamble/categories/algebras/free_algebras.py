"""Free symmetric, tensor, alternating, and divided-power algebra categories."""

from math import prod
from typing import Any, cast

from sage.algebras.free_algebra import FreeAlgebra as _SageFreeAlgebra
from sage.all import (
    LaurentPolynomialRing as _SageLaurentPolynomialRing,
)
from sage.all import (
    PolynomialRing as _SagePolynomialRing,
)
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.ideal import Ideal_generic
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.algebras import (
    AlgebraMorphism,
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    CommutativeAlgebraCoproducts,
    CommutativeAlgebraPushouts,
    FinitelyPresentedAlgebras,
    FramedAlgebras,
    _AlgebraMorCommonMethods,
    _OwnedAlgebraParent,
    _SelectedFiniteAlgebraPresentation,
    _refine_algebra,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.power_algebras import _PowerAlgebra
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedCategoryOverBaseRing,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
    _set_owned_ring_display,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import NN, Sets


class _NativeMonomialEvaluation:
    r"""Native word evaluation shared by free algebras and their linear quotients."""

    def _native_word_representative(self, element):
        return self._engine_element(element)

    def _native_word_generator(self, position):
        return self._engine.gen(position)

    def _native_basis_image(self, label):
        r"""Evaluate one canonical graded framing label in the native algebra."""
        inner = label.summand_element()
        labels = self._generating_module.module_generating_set()
        ranking = labels.ranking_map()
        match self._native_free_flavor:
            case "tensor":
                native = prod(
                    (self._native_word_generator(int(ranking(inner.component(position))))
                     for position in inner.parent().index_set()),
                    start=self._engine.one(),
                )
            case "symmetric":
                native = prod(
                    (self._native_word_generator(int(ranking(item))) ** int(inner.multiplicity(item))
                     for item in inner.support()),
                    start=self._engine.one(),
                )
        return self._from_engine_element(native)

    def _native_basis_coefficients(self, element):
        r"""Decode finite native support in the selected word-module frame.

        Univariate polynomial keys are exponents, multivariate keys are
        exponent tuples, and free-algebra keys are free-monoid words.  A
        linear quotient supplies its lift into that native free algebra.
        """
        generating = self._generating_module
        base = generating.base_ring()
        labels = generating.module_generating_set()
        module_labels = self._native_module_basis.source().module_generating_set()
        representative = self._native_word_representative(element)
        engine = representative.parent()
        coefficients = {}
        for monomial, coefficient in representative.monomial_coefficients().items():
            match self._native_free_flavor:
                case "tensor":
                    native_labels = dict(zip(engine.monoid().gens(), labels, strict=True))
                    word = tuple(
                        native_labels[generator]
                        for generator, exponent in monomial
                        for _ in range(int(exponent))
                    )
                    degree = len(word)
                    inner = module_labels.cofactor(NN(degree))(
                        lambda position, word=word: word[int(position)]
                    )
                case "symmetric":
                    match engine:
                        case PolynomialRing_generic():
                            exponents = (int(monomial),)
                        case _:
                            exponents = tuple(int(exponent) for exponent in monomial)
                    degree = sum(exponents)
                    powers = dict(zip(labels, exponents, strict=True))
                    inner = module_labels.cofactor(NN(degree)).from_multiplicities(powers)
            coefficients[module_labels(NN(degree), inner)] = _owned_engine_element(base,
                _engine_ring(base)(coefficient)
            )
        return coefficients


class _NativeFreeAlgebraParent(_NativeMonomialEvaluation, _OwnedAlgebraParent):
    r"""Native polynomial/word arithmetic on the canonical free module.

    For a free module M, T(M) = direct_sum_d T^d(M) and
    Sym(M) = direct_sum_d Sym^d(M) (Stacks, Tag 00DM).  The module
    construction supplies these exact pieces.  The free module on the
    disjoint union of their word bases supplies their summed framing.
    Its free source is the basis of all words or monomials, not the
    degree-one generating module M.  Native coefficient extraction is the
    inverse of monomial evaluation in that basis.

    This engine adapter supplies that correspondence before the common
    native ring constructor classifies multiplication.  It introduces no
    module arithmetic, framing accessor, or alternative algebra entry.
    """

    def __init__(self, engine, generating_module, flavor, *, categories=(), construction_data=()) -> None:
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
        from dzack_research.preamble.categories.modules.native_modules import _NativeModuleBasis

        base = generating_module.base_ring()
        assert generating_module in FramedFreeModules(base), (
            "a native free algebra is presented on a free generating module"
        )
        self._generating_module = generating_module
        self._native_free_flavor = flavor
        labels = generating_module.module_generating_set()
        match flavor:
            case "tensor":
                basis = labels.finite_words()
                algebra_category = TensorAlgebras(base)
            case "symmetric":
                basis = labels.finite_multisets()
                algebra_category = SymmetricAlgebras(base)
            case _:
                raise ValueError("the native free algebra is tensor or symmetric")
        self._native_module_basis = _NativeModuleBasis(
            base.free_module(basis),
            self._native_basis_image,
            self._native_basis_coefficients,
        )
        super().__init__(
            engine, base, generating_module.module_generating_set(),
            categories=(FreeAlgebras(base), GradedFreeAlgebras(base), algebra_category, *categories),
            construction_data=construction_data,
            law_decisions=(("grading", True),),
        )

    def _refined_specialized_algebra(
        self,
        base_ring,
        labels,
        categories,
        construction_data,
    ):
        r"""Preserve this native free-algebra realization under common refinement."""
        if self.base_ring() is not base_ring:
            return None
        selected_labels = (
            self.algebra_generating_set()
            if labels is None
            else finite_ordered_set(labels)
        )
        generating = self.generating_module()
        if selected_labels == self.algebra_generating_set():
            if (
                not construction_data
                and all(self in category for category in categories)
            ):
                return self
        else:
            generating = base_ring.free_module(selected_labels)
        return _native_free_algebra(
            _engine_ring(self),
            generating,
            self._native_free_flavor,
            categories=categories,
            construction_data=construction_data,
        )

@cached_function(key=lambda engine, generating_module, flavor, categories=(), construction_data=(): (
    engine, id(generating_module), flavor, categories, construction_data,
))
def _native_free_algebra(engine, generating_module, flavor, *, categories=(), construction_data=()):
    r"""The native realization of the free functor on this exact module."""
    return _NativeFreeAlgebraParent(
        engine, generating_module, flavor,
        categories=categories, construction_data=construction_data,
    )


def _finite_labels(labels):
    if labels in FiniteOrderedSets():
        return labels
    if isinstance(labels, int):
        return finite_ordered_set(range(labels))
    return finite_ordered_set(labels)


def _variable_names(labels) -> tuple[str, ...]:
    names = []
    used: set[str] = set()
    for index, label in enumerate(labels):
        candidate = str(label)
        if not candidate.isidentifier() or candidate in used:
            candidate = f"x{index}"
        while candidate in used:
            candidate = f"x{index}_{len(used)}"
        names.append(candidate)
        used.add(candidate)
    return tuple(names)


def _polynomial_ring(base_ring, *args, **kwargs):
    base = _owned_ring(base_ring)
    engine = _SagePolynomialRing(_engine_ring(base), *args, **kwargs)
    labels = tuple(engine.variable_names())
    algebra = _native_free_algebra(engine, base.free_module(labels), "symmetric")
    _set_owned_ring_display(
        algebra, f"{base}[{', '.join(labels)}]", kind="polynomial"
    )

    return algebra


def _laurent_polynomial_ring(base_ring, *args, **kwargs):
    base = _owned_ring(base_ring)
    result = _own_ring(
        _SageLaurentPolynomialRing(_engine_ring(base), *args, **kwargs)
    )
    labels = tuple(_engine_ring(result).variable_names())
    algebra = _refine_algebra(result, base, labels)
    _set_owned_ring_display(
        algebra,
        f"{base}[{', '.join(labels)}^±1]",
        kind="laurent_polynomial",
    )

    return algebra


def _symmetric_algebra_on(base_ring, algebra_generating_set, *, source_module=None):
    base = _owned_ring(base_ring)
    if (
        algebra_generating_set in Sets()
        and not cardinal(algebra_generating_set.cardinality()).is_finite()
    ):
        from dzack_research.preamble.categories.algebras.sparse_free_algebras import (
            _sparse_symmetric_algebra_of,
        )

        return _sparse_symmetric_algebra_of(
            base.free_module(algebra_generating_set) if source_module is None else source_module
        )
    labels = _finite_labels(algebra_generating_set)
    generating = base.free_module(labels) if source_module is None else source_module
    return _native_free_algebra(
        _SagePolynomialRing(_engine_ring(base), _variable_names(labels)),
        generating, "symmetric",
    )


def _tensor_algebra_on(base_ring, algebra_generating_set, *, source_module=None):
    base = _owned_ring(base_ring)
    if (
        algebra_generating_set in Sets()
        and not cardinal(algebra_generating_set.cardinality()).is_finite()
    ):
        from dzack_research.preamble.categories.algebras.sparse_free_algebras import (
            _sparse_tensor_algebra_of,
        )

        return _sparse_tensor_algebra_of(
            base.free_module(algebra_generating_set) if source_module is None else source_module
        )
    labels = _finite_labels(algebra_generating_set)
    names = _variable_names(labels)
    algebra = _SageFreeAlgebra(_engine_ring(base), len(labels), names=names)
    generating = base.free_module(labels) if source_module is None else source_module
    return _native_free_algebra(algebra, generating, "tensor")


def _relations_to_ideal(presentation_ring, relations):
    r"""Return the backend ideal and the owned finite relation family."""
    engine = _engine_ring(presentation_ring)
    if isinstance(relations, Ideal_generic):
        if relations.ring() is not engine:
            raise ValueError("the relation ideal belongs to a different presenting algebra")
        backend_by_position = {
            position: relation for position, relation in enumerate(relations.gens())
        }
        indices = Sets.Δ[len(backend_by_position) - 1]
        selected_relations = indexed_family(
            indices,
            lambda index: _owned_engine_element(presentation_ring,
                backend_by_position[int(index)]
            ),
            name="Defining relation family",
        )
        return relations, selected_relations

    if hasattr(relations, "index_set") and callable(getattr(relations, "value", None)):
        size = cardinal(relations.cardinality())
        if not size.is_finite():
            raise TypeError("a chosen finite algebra presentation requires finitely many relations")
        selected_relations = indexed_family(
            relations.index_set(),
            lambda index: presentation_ring(relations.value(index)),
            name="Defining relation family",
        )
    elif isinstance(relations, (tuple, list)):
        by_position = {position: relation for position, relation in enumerate(relations)}
        indices = Sets.Δ[len(by_position) - 1]
        selected_relations = indexed_family(
            indices,
            lambda index: presentation_ring(by_position[int(index)]),
            name="Defining relation family",
        )
    elif hasattr(relations, "cardinality"):
        size = cardinal(relations.cardinality())
        if not size.is_finite():
            raise TypeError("a chosen finite algebra presentation requires finitely many relations")
        selected_relations = indexed_family(
            relations,
            lambda relation: presentation_ring(relation),
            name="Defining relation family",
        )
    else:
        raise TypeError(
            "relations are a finite indexed family/set or explicit finite ingress"
        )

    backend_relations = [
        _engine_element(presentation_ring, selected_relations.value(index))
        for index in selected_relations.index_set()
    ]
    return engine.ideal(backend_relations), selected_relations


def _base_change_commutative_presentation(algebra, ring_map):
    if not isinstance(ring_map, Map):
        raise TypeError("algebra base change is specified by a ring morphism")
    if _engine_ring(ring_map.domain()) is not _engine_ring(algebra.base_ring()):
        raise ValueError(
            f"the scalar map starts at {ring_map.domain()}, not {algebra.base_ring()}"
        )
    target_base = _owned_ring(ring_map.codomain())
    target_presentation_ring = target_base.free_module(algebra.algebra_generating_set()).symmetric_algebra()
    source_base = algebra.base_ring()
    source_engine = _engine_ring(source_base)
    target_base_engine = _engine_ring(target_base)
    target_engine = _engine_ring(target_presentation_ring)

    def map_backend_scalar(scalar):
        owned_scalar = _owned_engine_element(source_base, source_engine(scalar))
        return _engine_element(target_base, ring_map(owned_scalar))

    backend_base_map = SetMorphism(
        source_engine.Hom(target_base_engine),
        map_backend_scalar,
    )
    source_presentation = algebra.presentation_ring()
    mapped_relations = tuple(
        _owned_engine_element(target_presentation_ring,
            target_engine(
                _engine_element(source_presentation, relation).map_coefficients(
                    backend_base_map,
                    new_base_ring=target_base_engine,
                )
            )
        )
        for relation in algebra.relations()
    )
    return (target_presentation_ring).quotient_by_relations(mapped_relations)


class _PresentedAlgebraParent(_OwnedAlgebraParent):
    r"""An algebra with one selected finite presentation fixed at construction."""

    def __init__(
        self,
        quotient_engine,
        base,
        labels,
        presentation_ring,
        selected_relations,
        presentation_ideal,
        *,
        extra_categories=(),
        extra_construction_data=None,
        generating_module=None,
        commutative_backend=False,
        finite_free_degree=None,
        presentation_flattening=None,
        generator_values=None,
        presentation_lift=None,
        finite_free_generator=None,
        finite_free_coordinates=None,
    ) -> None:
        if extra_construction_data is not None:
            for name, value in extra_construction_data:
                setattr(self, name, value)
        unflatten = (
            None if presentation_flattening is None else presentation_flattening.section()
        )

        def lift_to_presentation(element):
            backend = quotient_engine(self._engine_element(element))
            representative = (
                backend.lift()
                if presentation_lift is None
                else presentation_lift(backend)
            )
            if unflatten is not None:
                representative = unflatten(representative)
            return _owned_engine_element(presentation_ring, representative)

        def presentation_morphism():
            return Algebras(
                presentation_ring.base_ring()
            ).Associative().Unital().Mor(presentation_ring, self)(
                lambda label: self.algebra_generator(label)
            )

        self._selected_algebra_presentation = _SelectedFiniteAlgebraPresentation(
            presentation_ring,
            selected_relations,
            presentation_ideal,
            lift_to_presentation,
            presentation_morphism,
        )
        if generating_module is not None:
            self._generating_module = generating_module

        extra_categories = tuple(extra_categories)
        placement = [
            FinitelyPresentedAlgebras(base),
            AlgebrasWithChosenFinitePresentation(base),
            Algebras(base).Associative().Unital(),
            *extra_categories,
        ]
        match commutative_backend:
            case True:
                placement.append(Algebras(base).Commutative())
        if finite_free_degree is not None:
            from dzack_research.preamble.categories.modules.native_modules import _NativeModuleBasis

            module_labels = Sets.Δ[finite_free_degree - 1]
            source = base.free_module(module_labels)
            module_primitive = quotient_engine.gen() if finite_free_generator is None else finite_free_generator

            def basis_image(exponent):
                return self._from_engine_element(module_primitive) ** int(exponent)

            def basis_coordinates(element):
                backend = self._engine_element(self(element))
                coordinates = backend if finite_free_coordinates is None else finite_free_coordinates(backend)
                return {
                    label: _owned_engine_element(base, coefficient)
                    for label, coefficient in zip(module_labels, coordinates, strict=True)
                    if coefficient != 0
                }

            self._native_module_basis = _NativeModuleBasis(source, basis_image, basis_coordinates)
            placement.append(FinitelyGeneratedFreeModules(base))

        selected_generator_values = generator_values
        if presentation_flattening is not None:
            if selected_generator_values is not None:
                raise ValueError(
                    "a flattened presentation computes its algebra-generator values canonically"
                )
            presentation_engine = _engine_ring(presentation_ring)
            # The flattened engine lists parameter variables before these
            # outer algebra generators, so positional backend generators no
            # longer represent the selected algebra framing.
            selected_generator_values = tuple(
                quotient_engine(presentation_flattening(presentation_engine.gen(position)))
                for position in range(presentation_engine.ngens())
            )

        law_decisions = ()
        match any(
            category.is_subcategory(GradedAlgebras(base))
            for category in extra_categories
        ):
            case True:
                law_decisions = (("grading", True),)
            case False:
                pass
        _OwnedAlgebraParent.__init__(
            self,
            quotient_engine,
            base,
            labels,
            generator_values=selected_generator_values,
            categories=tuple(placement),
            law_decisions=law_decisions,
        )
        if commutative_backend:
            self._preamble_commutative_algebra_coproduct_backend = lambda left, right: (
                _commutative_algebra_coproduct_backend(left, right)
            )
            self._preamble_commutative_algebra_pushout_backend = lambda left_map, right_map: (
                _commutative_algebra_pushout_backend(left_map, right_map)
            )




class _NativeLinearRelationAlgebra(_NativeMonomialEvaluation, _PresentedAlgebraParent):
    r"""A native tensor/symmetric quotient on its actual module of words.

    If M = F/N, maps from T(F)/(N) to any associative algebra are exactly
    linear maps from F that vanish on N, hence maps from M.  Thus its
    degree-d module is M tensor ... tensor M.  The same argument with
    commutative targets gives Sym^d(M).  The word-module owner constructs
    these quotients; native multiplication only realizes that same module.
    """

    def __init__(self, engine, base, labels, presentation_ring, relations,
                 presentation_ideal, *, generating_module, **options):
        from dzack_research.preamble.categories.modules.native_modules import _NativeModuleFrame
        from dzack_research.preamble.categories.modules.word_modules import _module_on_word_quotient

        self._generating_module = generating_module
        match presentation_ring:
            case _ if presentation_ring in TensorAlgebras(base):
                self._native_free_flavor = "tensor"
            case _:
                assert presentation_ring in SymmetricAlgebras(base), (
                    "a linear-relation free algebra is tensor or symmetric"
                )
                self._native_free_flavor = "symmetric"
        # Fix the native images before any lower constructor can evaluate a
        # word. Flattened coefficient variables are not algebra generators.
        match options.get("generator_values"), options.get("presentation_flattening"):
            case (None, None):
                self._native_word_generators = tuple(engine.gen(i) for i in range(int(labels.cardinality())))
            case (None, flattening):
                free_engine = _engine_ring(presentation_ring)
                self._native_word_generators = tuple(
                    engine(flattening(free_engine.gen(i))) for i in range(int(labels.cardinality()))
                )
            case (values, _):
                self._native_word_generators = tuple(values)
        word_module = _module_on_word_quotient(generating_module, self._native_free_flavor)
        self._native_module_basis = _NativeModuleFrame(
            word_module, self._native_basis_image, self._native_basis_coefficients,
        )
        super().__init__(
            engine, base, labels, presentation_ring, relations, presentation_ideal,
            generating_module=generating_module, **options,
        )

    def _native_word_generator(self, position):
        return self._native_word_generators[position]

    def _native_word_representative(self, element):
        presentation = self.presentation_ring()
        return _engine_element(presentation, self.lift_to_presentation(self(element)))


def _presented_algebra_on_engine(
    engine,
    presentation_ring,
    relations,
    *,
    generator_values=None,
    finite_free_degree=None,
    finite_free_generator=None,
    finite_free_coordinates=None,
    presentation_lift=None,
):
    r"""Represent a chosen polynomial presentation on an authoritative engine.

    This is the crossing for an algebra whose computation parent already exists
    independently of the polynomial presentation (a number field is the first
    consumer).  The returned object keeps ``engine`` as its ring realization;
    ``presentation_ring`` and ``relations`` supply the algebra framing, quotient
    map, scalar-change data, and finite-presentation module structure.
    """
    base = presentation_ring.base_ring()
    if presentation_ring not in SymmetricAlgebras(base):
        raise TypeError(
            "an authoritative-engine algebra requires a commutative polynomial presentation"
        )
    presentation_ideal, selected_relations = _relations_to_ideal(
        presentation_ring, relations
    )
    return _PresentedAlgebraParent(
        engine,
        base,
        presentation_ring.algebra_generating_set(),
        presentation_ring,
        selected_relations,
        presentation_ideal,
        commutative_backend=True,
        finite_free_degree=finite_free_degree,
        generator_values=generator_values,
        presentation_lift=presentation_lift,
        finite_free_generator=finite_free_generator,
        finite_free_coordinates=finite_free_coordinates,
    )


def _localized_coefficient_presentation_backend(
    presentation_ring,
    selected_relations,
):
    r"""Realize a finite presentation over a finitely generated localization.

    For ``S^{-1}A[x_1,...,x_n]/I`` with a chosen finite generating family for
    ``S``, compute in the standard polynomial presentation

    ``A[x_1,...,x_n,t_1,...,t_r]/(t_i s_i - 1, I~)``.

    The public algebra keeps its selected presentation over ``S^{-1}A``.  This
    helper supplies only the private Sage quotient, the images of the selected
    algebra generators in that quotient, and the exact lift back to the
    selected presentation.  The construction therefore changes no public
    scalar ring or presentation data.
    """

    base = presentation_ring.base_ring()
    if base not in LocalizationRings():
        return None
    try:
        inverted = tuple(base.inverted_elements())
    except NotImplementedError:
        return None
    if not inverted:
        return None

    coefficient_source = base.localization_source()
    presentation_engine = _engine_ring(presentation_ring)
    coefficient_source_engine = _engine_ring(coefficient_source)
    base_engine = _engine_ring(base)
    try:
        variable_names = tuple(presentation_engine.variable_names())
        polynomial_bottom = _SagePolynomialRing(
            coefficient_source_engine,
            names=variable_names,
        )
        flattening_factory = getattr(
            polynomial_bottom,
            "flattening_morphism",
            None,
        )
        if not callable(flattening_factory):
            return None
        flattening = flattening_factory()
        flattened = flattening.codomain()
        unflatten = flattening.section()
    except (AttributeError, TypeError, ValueError):
        return None

    flat_names = tuple(flattened.variable_names())
    occupied = set(flat_names)
    inverse_names = []
    for position in range(len(inverted)):
        candidate = f"localization_inverse_{position}"
        while candidate in occupied:
            candidate = "localization_" + candidate
        occupied.add(candidate)
        inverse_names.append(candidate)
    engine_presentation = _SagePolynomialRing(
        flattened.base_ring(),
        names=(*flat_names, *inverse_names),
    )
    engine_generators = tuple(engine_presentation.gens())
    flattened_generators = engine_generators[: flattened.ngens()]
    inverse_generators = engine_generators[flattened.ngens() :]
    flattened_to_engine = flattened.mor(
        flattened_generators,
        engine_presentation,
    )

    def bottom_polynomial(element):
        represented = presentation_engine(
            _engine_element(presentation_ring, element)
        )
        coefficients = represented.dict()
        common_denominator = coefficient_source_engine.one()
        represented_coefficients = {}
        for exponent, coefficient in coefficients.items():
            represented_coefficient = base_engine(coefficient)
            represented_coefficients[exponent] = represented_coefficient
            common_denominator *= coefficient_source_engine(
                represented_coefficient.denominator()
            )

        cleared = {}
        for exponent, represented_coefficient in represented_coefficients.items():
            denominator = coefficient_source_engine(
                represented_coefficient.denominator()
            )
            multiplier, remainder = common_denominator.quo_rem(denominator)
            if remainder != coefficient_source_engine.zero():
                raise ArithmeticError(
                    "the selected common denominator does not clear a presentation coefficient"
                )
            cleared[exponent] = (
                coefficient_source_engine(represented_coefficient.numerator())
                * multiplier
            )
        return polynomial_bottom(cleared)

    engine_relations = []
    for inverse, inverted_element in zip(
        inverse_generators,
        inverted,
        strict=True,
    ):
        bottom_element = coefficient_source_engine(
            _engine_element(coefficient_source, inverted_element)
        )
        represented = flattened_to_engine(
            flattening(polynomial_bottom(bottom_element))
        )
        engine_relations.append(
            inverse * represented - engine_presentation.one()
        )
    engine_relations.extend(
        flattened_to_engine(flattening(bottom_polynomial(relation)))
        for relation in selected_relations
    )

    quotient_engine = engine_presentation.quotient(
        engine_presentation.ideal(tuple(engine_relations))
    )

    coefficient_generators = tuple(coefficient_source_engine.gens())
    base_generators = tuple(base_engine.gens())
    if len(coefficient_generators) == len(base_generators):
        scalar_images = [
            quotient_engine(
                flattened_to_engine(
                    flattening(polynomial_bottom(generator))
                )
            )
            for generator in coefficient_generators
        ]
        engine_scalar_map = base_engine.mor(
            scalar_images,
            quotient_engine,
        )
        if not quotient_engine.has_coerce_map_from(base_engine):
            # This quotient engine is a private realization of an algebra over
            # ``base``.  Register exactly that represented scalar embedding so
            # Sage's affine-scheme engine sees the same map; no public owned
            # coercion is introduced.
            quotient_engine.register_coercion(engine_scalar_map)

    generator_values = tuple(
        quotient_engine(
            flattened_to_engine(flattening(polynomial_bottom.gen(position)))
        )
        for position in range(polynomial_bottom.ngens())
    )

    reverse_images = [
        presentation_engine(unflatten(generator))
        for generator in flattened.gens()
    ]
    reverse_images.extend(
        presentation_engine(
            base_engine(
                _engine_element(coefficient_source, inverted_element)
            )
            ** -1
        )
        for inverted_element in inverted
    )
    engine_to_presentation = engine_presentation.mor(
        reverse_images,
        presentation_engine,
    )

    def presentation_lift(element):
        return engine_to_presentation(quotient_engine(element).lift())

    return quotient_engine, generator_values, presentation_lift


def _finitely_presented_algebra_from_data(
    presentation_ring,
    relations,
    *,
    _extra_categories=(),
    _extra_construction_data=None,
    _generating_module=None,
):
    r"""Return the selected quotient ``R[S] / (relations)``."""
    base = presentation_ring.base_ring()
    assert (
        presentation_ring in AlgebrasWithChosenFinitePresentation(base)
        or presentation_ring in SymmetricAlgebras(base)
    ), (
        "a selected finite commutative-algebra presentation is represented by a polynomial algebra or an algebra already carrying such a presentation"
    )
    if presentation_ring in AlgebrasWithChosenFinitePresentation(base):
        # A quotient of a quotient is one quotient of the same polynomial
        # presentation: for A = P/I, the algebra A/(J) is P/(I + J~) where J~
        # lifts the new relations to P.  Consolidating here keeps one chosen
        # presentation and one scalar ring, so a second closed embedding into
        # an already presented algebra reaches the same construction as the
        # first rather than needing a tower of quotient objects.
        source = presentation_ring.presentation_ring()
        existing = presentation_ring.relations()
        return _finitely_presented_algebra_from_data(
            source,
            (
                *(existing.value(index) for index in existing.index_set()),
                *(
                    presentation_ring.lift_to_presentation(presentation_ring(relation))
                    for relation in relations
                ),
            ),
            _extra_categories=_extra_categories,
            _extra_construction_data=_extra_construction_data,
            _generating_module=_generating_module,
        )
    presentation_ideal, selected_relations = _relations_to_ideal(
        presentation_ring, relations
    )
    presentation_engine = _engine_ring(presentation_ring)
    presentation_flattening = None
    quotient_presentation_engine = presentation_engine
    quotient_ideal = presentation_ideal
    quotient_engine = None
    generator_values = None
    presentation_lift = None
    if isinstance(presentation_engine, MPolynomialRing_base) and isinstance(
        presentation_engine.base_ring(),
        (PolynomialRing_generic, MPolynomialRing_base),
    ):
        # Sage's multivariate quotient reduction over a polynomial
        # coefficient ring need not have a Gröbner backend.  Keep the owned
        # relative presentation nested, but compute in the canonically
        # flattened polynomial ring where the coefficient variables become
        # ordinary variables over the ultimate coefficient ring.
        presentation_flattening = presentation_engine.flattening_morphism()
        quotient_presentation_engine = presentation_flattening.codomain()
        quotient_ideal = quotient_presentation_engine.ideal(
            [
                presentation_flattening(
                    _engine_element(
                        presentation_ring,
                        selected_relations.value(index)
                    )
                )
                for index in selected_relations.index_set()
            ]
        )
    elif (
        isinstance(presentation_engine, MPolynomialRing_base)
        and base in LocalizationRings()
    ):
        localized_backend = _localized_coefficient_presentation_backend(
            presentation_ring,
            selected_relations,
        )
        if localized_backend is not None:
            quotient_engine, generator_values, presentation_lift = localized_backend

    if quotient_engine is None:
        quotient_engine = quotient_presentation_engine.quotient(quotient_ideal)
        if quotient_engine is quotient_presentation_engine:

            def presentation_lift(element):
                return element

    labels = presentation_ring.algebra_generating_set()
    finite_free_degree = None
    label_size = labels.cardinality()
    if (
        label_size.is_finite()
        and int(label_size.finite_value()) == 1
        and hasattr(quotient_engine, "modulus")
    ):
        modulus = quotient_engine.modulus()
        degree = int(modulus.degree())
        if degree > 0:
            finite_free_degree = degree

    match _generating_module, finite_free_degree:
        case (None, _) | (_, int()):
            constructor = _PresentedAlgebraParent
        case _:
            constructor = _NativeLinearRelationAlgebra
    return constructor(
        quotient_engine,
        base,
        labels,
        presentation_ring,
        selected_relations,
        presentation_ideal,
        extra_categories=tuple(_extra_categories),
        extra_construction_data=(
            None
            if _extra_construction_data is None
            else tuple(_extra_construction_data)
        ),
        generating_module=_generating_module,
        commutative_backend=True,
        finite_free_degree=finite_free_degree,
        presentation_flattening=presentation_flattening,
        generator_values=generator_values,
        presentation_lift=presentation_lift,
    )


class FreeAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The free algebra on one generator."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(self.base_ring())
        return modules.tensor_algebra()(modules.an_object())

    @classmethod
    def _repr_object_names(cls):
        return "free algebras"

    def super_categories(self):
        return [FramedAlgebras(self.base_ring())]

    class ParentMethods:
        def is_free(self) -> bool:
            return True

        def _algebra_mor_class(self):
            return FramedFreeAlgebraMor

        def Mor(self, codomain, category=None):
            r"""Use the free-algebra universal Mor before the inherited ring Mor."""
            ordinary = Algebras(self.base_ring()).Associative().Unital()
            if category is None:
                return ordinary.Mor(self, codomain)
            return super().Mor(codomain, category=category)


class GradedFreeAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The polynomial algebra on one generator, graded by degree."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(self.base_ring())
        return modules.symmetric_algebra()(modules.an_object())

    @classmethod
    def _repr_object_names(cls):
        return "graded free algebras"

    def super_categories(self):

        return [FreeAlgebras(self.base_ring()), GradedAlgebras(self.base_ring())]

    class ParentMethods:
        def _realize_graded_piece_basis_label(self, degree, label):
            r"""Return the algebra monomial represented by one basis label of ``A_degree``.

            The authoritative basis is the basis of :meth:`graded_piece`; this
            method only realizes that basis element back in the algebra.  It
            does not construct a second monomial system.
            """
            degree = int(degree)
            if degree < 0:
                raise ValueError("a graded degree is nonnegative")
            if degree == 0:
                return self.one()
            if degree == 1:
                return self.algebra_generator(label)

            piece = self.graded_piece(degree)

            if self in AlternatingAlgebras(self.base_ring()) or self in DividedPowerAlgebras(self.base_ring()):
                return self.from_component(degree, piece.module_generator(label))

            ring = self.algebra_base_ring()
            result = self.one()
            if self in TensorAlgebras(ring):
                from dzack_research.preamble.categories.modules.tensor_products import (
                    _flatten_tensor_label,
                )

                for source_label in _flatten_tensor_label(label, degree):
                    result *= self.algebra_generator(source_label)
                return result

            if self in SymmetricAlgebras(ring):
                for source_label in label.support():
                    for _ in range(int(label.multiplicity(source_label))):
                        result *= self.algebra_generator(source_label)
                return result

            raise TypeError(f"the graded-piece basis of {self} has no represented realization")

        def from_graded_piece(self, degree, element):
            r"""Include an element of the canonical degree piece into this algebra."""
            degree = int(degree)
            piece = self.graded_piece(degree)
            element = piece(element)
            coefficients = piece.framing_coefficients(element)
            return sum(
                (
                    coefficient
                    * self._realize_graded_piece_basis_label(degree, label)
                    for label, coefficient in coefficients.items()
                    if coefficient
                ),
                self.zero(),
            )

        def degree_on_module_generator(self, module_generator):
            r"""Return the degree of one represented homogeneous algebra basis element."""
            return self.homogeneous_degree(module_generator)

        def graded_piece_monomials(self, degree):
            r"""Return the selected algebra basis of the canonical degree piece.

            The index set is literally the framing of :meth:`graded_piece`;
            values are those basis generators realized in this algebra.
            """
            degree = int(degree)
            if degree < 0:
                raise ValueError("a graded degree is nonnegative")
            if degree == 0:
                labels = finite_ordered_set((0,))
            else:
                try:
                    labels = self.graded_piece(degree).module_generating_set()
                except ValueError:
                    labels = finite_ordered_set(())
            return indexed_family(
                labels,
                lambda label: self._realize_graded_piece_basis_label(degree, label),
                name=f"Degree-{degree} algebra monomial basis of {self}",
            )

        def ideal_generators_in_degree(self, relations, degree):
            r"""Return generators of the degree-``degree`` ideal generated in degree one.

            For tensor/symmetric/exterior algebras this is
            ``sum_{i+j=d-1} A_i K A_j``.  For divided powers the divided
            powers of the selected degree-one relations are included as well,
            which is the divided-power ideal rather than an ordinary
            polynomial ideal.
            """
            degree = int(degree)
            if degree < 0:
                raise ValueError("a graded degree is nonnegative")
            selected = tuple(self(relation) for relation in relations)
            if any(self.homogeneous_degree(relation) != 1 for relation in selected):
                raise ValueError("these graded-ideal generators must lie in degree one")
            if degree == 0:
                return ()

            generators = []
            for relation in selected:
                for left_degree in range(degree):
                    right_degree = degree - 1 - left_degree
                    left_basis = self.graded_piece_monomials(left_degree)
                    right_basis = self.graded_piece_monomials(right_degree)
                    for left_label in left_basis.index_set():
                        for right_label in right_basis.index_set():
                            generators.append(
                                left_basis[left_label] * relation * right_basis[right_label]
                            )

            ring = self.algebra_base_ring()
            if self in DividedPowerAlgebras(ring):
                for relation in selected:
                    for divided_degree in range(2, degree + 1):
                        divided = self.divided_power(relation, divided_degree)
                        complementary = self.graded_piece_monomials(
                            degree - divided_degree
                        )
                        for label in complementary.index_set():
                            generators.append(divided * complementary[label])
            return tuple(generators)

        def graded_piece(self, degree):
            r"""Return the canonical degree piece of this free construction.

            The flavor, not this common superclass, determines the degree
            piece: ``T^n(M)``, ``Sym^n(M)``, ``Lambda^n(M)``, or
            ``Gamma^n(M)``.  This is one construction path -- the algebra does
            not build a second model of those modules.
            """
            degree = int(degree)
            assert degree >= 0, "a graded degree is nonnegative"

            ring = self.algebra_base_ring()
            match self:
                # The represented exterior/divided-power algebras are assembled
                # from their authoritative module-power pieces, in every degree
                # including zero; do not let this generic free-algebra method
                # replace their degree-zero power module with the scalar ring.
                case _ if self in AlternatingAlgebras(ring):
                    return self.generating_module().exterior_power(degree)
                case _ if self in DividedPowerAlgebras(ring):
                    return self.generating_module().divided_power_module(degree)
                # Every flavor uses its authoritative module-power owner in
                # every degree.  In degree zero this is the rank-one scalar
                # module, not the ring parent viewed through an unrelated API.
                case _ if self in TensorAlgebras(ring):
                    return self.generating_module().tensor_power(degree)
                case _ if self in SymmetricAlgebras(ring):
                    return self.generating_module().symmetric_power(degree)
            raise TypeError(
                f"the graded free-algebra flavor of {self} is not represented"
            )


class PowerAlgebraMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class_for(self, domain, codomain):
        _ = codomain
        return domain._power_algebra_mor_class()


class TensorAlgebras(OwnedCategoryOverBaseRing):
    r"""Tensor algebras of represented modules."""

    def an_object(self):
        r"""The tensor algebra on the free module of rank one."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(self.base_ring())
        return modules.tensor_algebra()(modules.an_object())

    @classmethod
    def _repr_object_names(cls):
        return "tensor algebras"

    def super_categories(self):

        return [GradedAlgebras(self.base_ring())]

    class ParentMethods:
        def homogeneous_degree(self, element):
            r"""Return the degree of a homogeneous tensor-algebra element.

            Sage's free associative algebra stores monomials on free-monoid
            words.  Word length is the tensor grading, and the coefficient
            dictionary is the maintained exact representation of a finite
            algebra element.
            """
            element = self(element)
            if element == self.zero():
                raise ValueError("zero has no selected homogeneous degree here")
            backend = _engine_element(self, element)
            degrees = {
                len(word)
                for word, coefficient in backend.monomial_coefficients().items()
                if coefficient
            }
            if len(degrees) != 1:
                raise ValueError("the algebra element is not homogeneous")
            return self.grading_monoid()(degrees.pop())

        def from_component(self, degree, component):
            r"""Embed ``T^degree(M)`` through the shared graded-piece inclusion."""
            return self.from_graded_piece(degree, component)

        def homogeneous_component(self, element, degree):
            r"""Project an element onto the authoritative tensor-power piece."""
            degree = int(degree)
            element = self(element)
            piece = self.graded_piece(degree)
            backend = _engine_element(self, element)
            coefficients = backend.monomial_coefficients()
            word_to_label = {}
            for label in piece.module_generating_set():
                monomial = _engine_element(
                    self,
                    self._realize_graded_piece_basis_label(degree, label),
                )
                entries = tuple(monomial.monomial_coefficients().items())
                if len(entries) != 1 or entries[0][1] != 1:
                    raise ArithmeticError(
                        "a tensor-power basis element did not realize as one monomial"
                    )
                word_to_label[entries[0][0]] = label
            ring = self.algebra_base_ring()
            engine_ring = _engine_ring(ring)
            return piece.linear_combination(
                {
                    word_to_label[word]: _owned_engine_element(ring, engine_ring(coefficient))
                    for word, coefficient in coefficients.items()
                    if coefficient and len(word) == degree
                }
            )

        def homogeneous_components(self, element):
            r"""Return all nonzero tensor-degree components as tensor-power elements."""
            backend = _engine_element(self, self(element))
            degrees = sorted(
                {
                    len(word)
                    for word, coefficient in backend.monomial_coefficients().items()
                    if coefficient
                }
            )
            return {
                degree: self.homogeneous_component(element, degree)
                for degree in degrees
            }

        def generating_module(self):
            r"""The exact input M of this chosen tensor-algebra construction.

            This is the degree-one module, not U(T(M)), the direct sum of
            all tensor powers.  The native and relationful entries supply M
            before constructing the algebra; this accessor never reconstructs
            it from generator labels.
            """
            return self._generating_module

        @cached_method
        def ring_center(self):
            r"""Return the exact center of the represented free tensor algebra.

            On zero or one generator the tensor algebra is commutative.  On at
            least two generators, comparison of coefficients in the word basis
            shows that an element commuting with two distinct generators has no
            nonconstant word, so the center is exactly the scalar ring.
            """
            size = self.algebra_generating_set().cardinality()
            if size.is_finite() and int(size.finite_value()) <= 1:
                return self
            return self.algebra_base_ring()

        @cached_method
        def center_inclusion(self):
            r"""Return the inclusion ``Z(T) -> T`` under the selected center identification."""


            center = self.ring_center()
            if center is self:
                return self.Mor(self)(lambda element: element)
            return center.Mor(self)(lambda scalar: self(scalar))


    class ElementMethods:
        def homogeneous_components(self):
            return self.parent().homogeneous_components(self)

        def homogeneous_component(self, degree):
            return self.parent().homogeneous_component(self, degree)


class SymmetricAlgebras(OwnedCategoryOverBaseRing):
    r"""Symmetric algebras of represented modules."""

    def an_object(self):
        r"""The symmetric algebra on the free module of rank one."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(self.base_ring())
        return modules.symmetric_algebra()(modules.an_object())

    @classmethod
    def _repr_object_names(cls):
        return "symmetric algebras"

    def super_categories(self):
        return [GradedAlgebras(self.base_ring()).Commutative()]

    class ParentMethods:
        def generating_module(self):
            r"""The exact input M of this chosen symmetric-algebra construction.

            For polynomial syntax the constructor supplies F_R(S) on its
            variables.  For Sym_R(M) it supplies M itself, including its
            relations.  Neither is the full underlying module U(Sym_R(M)).
            """
            return self._generating_module

        def from_component(self, degree, component):
            r"""Embed ``Sym^degree(M)`` through the shared graded-piece inclusion."""
            return self.from_graded_piece(degree, component)

        def homogeneous_component(self, element, degree):
            r"""Project onto the canonical symmetric-power degree piece."""
            degree = int(degree)
            element = self(element)

            def monomial_degree(exponent):
                try:
                    return sum(exponent)
                except TypeError:
                    return int(exponent)
            piece = self.graded_piece(degree)
            backend = _engine_element(self, element)
            coefficients = backend.monomial_coefficients()
            exponent_to_label = {}
            for label in piece.module_generating_set():
                monomial = _engine_element(
                    self,
                    self._realize_graded_piece_basis_label(degree, label),
                )
                entries = tuple(monomial.monomial_coefficients().items())
                if len(entries) != 1 or entries[0][1] != 1:
                    raise ArithmeticError(
                        "a symmetric-power basis element did not realize as one monomial"
                    )
                exponent_to_label[entries[0][0]] = label
            ring = self.algebra_base_ring()
            engine_ring = _engine_ring(ring)
            return piece.linear_combination(
                {
                    exponent_to_label[exponent]: _owned_engine_element(ring,
                        engine_ring(coefficient)
                    )
                    for exponent, coefficient in coefficients.items()
                    if coefficient and monomial_degree(exponent) == degree
                }
            )

        def homogeneous_components(self, element):
            r"""Return all nonzero polynomial-degree components."""
            backend = _engine_element(self, self(element))

            def monomial_degree(exponent):
                try:
                    return sum(exponent)
                except TypeError:
                    return int(exponent)

            degrees = sorted(
                {
                    monomial_degree(exponent)
                    for exponent, coefficient in backend.monomial_coefficients().items()
                    if coefficient
                }
            )
            return {
                degree: self.homogeneous_component(element, degree)
                for degree in degrees
            }

        def _commutative_algebra_coproduct(self, left, right):
            r"""Supply the symmetric-algebra coproduct to the generic algebra owner.

            Protected construction contract: the sole external caller role is
            ``Algebras._categorical_coproduct``. The backend implementation is
            selected here by the symmetric-algebra owner and returns only the
            owned coproduct object and owned maps.
            """
            return _commutative_algebra_coproduct_backend(left, right)

        def _commutative_algebra_pushout(self, left_map, right_map):
            r"""Supply the symmetric-algebra pushout to the generic algebra owner.

            Protected construction contract: the sole external caller role is
            ``Algebras._categorical_pushout``. The specialized computation
            remains in this owner and returns an owned pushout.
            """
            return _commutative_algebra_pushout_backend(left_map, right_map)

    class ElementMethods:
        def homogeneous_components(self):
            return self.parent().homogeneous_components(self)

        def homogeneous_component(self, degree):
            return self.parent().homogeneous_component(self, degree)

        def number_field(self, *args, **kwargs):
            r"""Return the number field defined by this polynomial."""
            from dzack_research.preamble.categories.rings.number_fields import (
                _number_field,
            )

            return _number_field(self, *args, **kwargs)


class AlternatingAlgebras(OwnedCategoryOverBaseRing):
    r"""Exterior/alternating algebras."""

    def an_object(self):
        r"""The exterior algebra on the free module of rank one."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(self.base_ring())
        return modules.exterior_algebra()(modules.an_object())

    @classmethod
    def _repr_object_names(cls):
        return "alternating algebras"

    def super_categories(self):
        return [GradedAlgebras(self.base_ring()).Supercommutative().Alternating()]

    _MorCategory = PowerAlgebraMorCategoryConstruction

    def _call_(self, module):
        from dzack_research.preamble.categories.algebras.power_algebras import _power_algebra_of

        assert module.base_ring() is self.base_ring(), "the power construction uses its module's scalars"
        return _power_algebra_of(module, "alternating")

    class ParentMethods(_PowerAlgebra):
        def Mor(self, codomain, category=None):
            alternating = AlternatingAlgebras(self.base_ring())
            if category is None and codomain in alternating:
                return alternating.Mor(self, codomain)
            return super().Mor(codomain, category=category)



def _presentation_data(algebra):
    base = algebra.base_ring()
    has_selected_presentation = hasattr(algebra, "presentation_ring") and hasattr(
        algebra, "relations"
    )
    is_free_polynomial = algebra in SymmetricAlgebras(base) and algebra in FramedAlgebras(base)
    has_quotient_presentation = hasattr(algebra, "quotient_source") and hasattr(
        algebra, "defining_ideal"
    )
    quotient_source = algebra.quotient_source() if has_quotient_presentation else None
    assert (
        has_selected_presentation
        or is_free_polynomial
        or (has_quotient_presentation and quotient_source in SymmetricAlgebras(base))
    ), (
        "the active commutative-algebra backend requires a free polynomial or selected finite presentation"
    )
    if has_selected_presentation:
        return algebra.presentation_ring(), tuple(algebra.relations())
    if is_free_polynomial:
        return algebra, ()
    return quotient_source, tuple(algebra.defining_ideal().gens())


def _transport_relations(presentation_ring, relations, target, tag):
    if not relations:
        return ()
    transport = presentation_ring.Mor(target)(
        {
            label: target.algebra_generator((tag, label))
            for label in presentation_ring.algebra_generating_set()
        }
    )
    return tuple(transport(relation) for relation in relations)


@cached_function
def _commutative_algebra_coproduct_backend(left, right):
    base = left.base_ring()
    if right.base_ring() is not base:
        raise ValueError("commutative-algebra coproducts require one scalar base")
    category = Algebras(base).Associative().Unital().Commutative()
    if left not in category or right not in category:
        raise TypeError("both factors must be commutative algebras over the common base")
    assert left in FramedAlgebras(base) and right in FramedAlgebras(base), (
        "the active finite-presentation coproduct backend requires finite algebra framings"
    )

    left_presentation, left_relations = _presentation_data(left)
    right_presentation, right_relations = _presentation_data(right)
    combined_labels = tuple(
        ("left", label) for label in left.algebra_generating_set()
    ) + tuple(("right", label) for label in right.algebra_generating_set())
    presentation = base.free_module(combined_labels).symmetric_algebra()
    relations = _transport_relations(
        left_presentation, left_relations, presentation, "left"
    ) + _transport_relations(
        right_presentation, right_relations, presentation, "right"
    )
    construction_data = (("_preamble_coproduct_factors", (left, right)),)
    if relations:
        return (presentation).quotient_by_relations(relations,
            _extra_categories=(CommutativeAlgebraCoproducts(base),),
            _extra_construction_data=construction_data,
        )
    return _refine_algebra(
        presentation,
        base,
        combined_labels,
        FreeAlgebras(base),
        GradedFreeAlgebras(base),
        SymmetricAlgebras(base),
        CommutativeAlgebraCoproducts(base),
        construction_data=construction_data,
    )


def _quotient_by_algebra_elements_backend(
    algebra,
    elements,
    *,
    extra_categories=(),
    extra_construction_data=None,
):
    base = algebra.base_ring()
    selected = tuple(elements)
    if not selected:
        identity = Algebras(base).Associative().Unital().Commutative().Mor(algebra, algebra).identity()
        return algebra, identity
    has_selected_presentation = hasattr(algebra, "presentation_ring") and hasattr(
        algebra, "relations"
    )
    assert has_selected_presentation or algebra in SymmetricAlgebras(base), (
        "quotienting by represented algebra elements requires a selected polynomial presentation"
    )
    if has_selected_presentation:
        presentation = algebra.presentation_ring()
        relations = tuple(algebra.relations()) + tuple(
            algebra.lift_to_presentation(element) for element in selected
        )
    elif algebra in SymmetricAlgebras(base):
        presentation = algebra
        relations = selected
    quotient = (presentation).quotient_by_relations(relations,
        _extra_categories=tuple(extra_categories),
        _extra_construction_data=extra_construction_data,
    )
    quotient_map = Algebras(algebra.base_ring()).Associative().Unital().Mor(algebra, quotient)(
        {
            label: quotient.algebra_generator(label)
            for label in algebra.algebra_generating_set()
        }
    )
    return quotient, quotient_map


@cached_function
def _commutative_algebra_pushout_backend(left_map, right_map):
    try:
        common = left_map.domain()
        left = left_map.codomain()
        right_common = right_map.domain()
        right = right_map.codomain()
    except AttributeError as error:
        raise TypeError(
            "a commutative-algebra pushout is specified by represented algebra morphisms"
        ) from error
    if common is not right_common:
        raise ValueError("pushout maps require one common domain")
    base = common.base_ring()
    if left.base_ring() is not base or right.base_ring() is not base:
        raise ValueError("the pushout span must lie over one scalar base")
    if left_map.parent() is not common.Mor(left) or right_map.parent() is not common.Mor(
        right
    ):
        raise TypeError(
            "the pushout span maps must belong to the represented algebra Mors "
            "of their endpoints"
        )
    assert common in FramedAlgebras(base), (
        "the active pushout backend requires a finite algebra framing on the common source"
    )

    tensor = _commutative_algebra_coproduct_backend(left, right)
    left_injection, right_injection = tensor.coproduct_injections()
    equalities = tuple(
        left_injection(left_map(common.algebra_generator(label)))
        - right_injection(right_map(common.algebra_generator(label)))
        for label in common.algebra_generating_set()
    )
    pushout, _quotient_map = _quotient_by_algebra_elements_backend(
        tensor,
        equalities,
        extra_categories=(CommutativeAlgebraPushouts(base),),
        extra_construction_data=(
            ("_preamble_pushout_span", (left_map, right_map)),
            ("_preamble_pushout_coproduct", tensor),
        ),
    )
    return pushout

class DividedPowerAlgebras(OwnedCategoryOverBaseRing):
    r"""Divided-power algebras ``Gamma(M)`` with their canonical grading."""

    @classmethod
    def _repr_object_names(cls):
        return "divided power algebras"

    def super_categories(self):
        return [GradedAlgebras(self.base_ring()).Commutative()]

    _MorCategory = PowerAlgebraMorCategoryConstruction

    def _call_(self, module):
        from dzack_research.preamble.categories.algebras.power_algebras import _power_algebra_of

        assert module.base_ring() is self.base_ring(), "the power construction uses its module's scalars"
        return _power_algebra_of(module, "divided")

    class ParentMethods(_PowerAlgebra):
        def Mor(self, codomain, category=None):
            divided = DividedPowerAlgebras(self.base_ring())
            if category is None and codomain in divided:
                return divided.Mor(self, codomain)
            return super().Mor(codomain, category=category)



class FramedFreeAlgebraMorphism(AlgebraMorphism):
    r"""A generator-defined map from a framed free algebra to any algebra."""

    def __init__(self, parent, images) -> None:
        Morphism.__init__(self, parent)
        domain = cast(Any, self.domain())
        labels = domain.algebra_generating_set()
        if isinstance(images, IndexedFamily):
            source_indices = images.index_set()
            self._images = indexed_family(
                labels,
                lambda label: self.codomain()(images[source_indices(label)]),
                name="Generator images",
            )
        elif isinstance(images, dict):
            if not labels.cardinality().is_finite():
                raise TypeError(
                    "dictionary algebra-generator syntax requires a finite framing; "
                    "use a callable or indexed family for an infinite framing"
                )
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(f"algebra-generator assignment omits {missing}")
            self._images = indexed_family(
                labels,
                lambda label: self.codomain()(images[label]),
                name="Generator images",
            )
        elif isinstance(images, (tuple, list)):
            size = labels.cardinality()
            if not size.is_finite():
                raise TypeError(
                    "sequence algebra-generator syntax requires a finite framing; "
                    "use a callable or indexed family for an infinite framing"
                )
            values = tuple(images)
            if len(values) != int(size.finite_value()):
                raise ValueError(
                    "the number of algebra-generator images must equal the framing size"
                )
            self._images = indexed_family(
                labels,
                lambda label: self.codomain()(values[int(labels.ranking_map()(label))]),
                name="Generator images",
            )
        elif callable(images):
            self._images = indexed_family(
                labels,
                lambda label: self.codomain()(images(label)),
                name="Generator images",
            )
        else:
            raise TypeError(
                "an algebra morphism is specified on its algebra generators"
            )
        self._generator_images = self._images
        self._engine_morphism = None
        self._element_function = None
        self._preamble_is_identity = False
        generating = domain.generating_module()
        generating.module_category().Mor(
            generating, self.codomain().underlying_module()
        )(self._images.value)

    def _tensor_terms(self, element):
        domain = self.domain()
        if hasattr(domain, "lift_to_presentation"):
            presentation_ring = domain.presentation_ring()
            presented = _engine_element(
                presentation_ring,
                domain.lift_to_presentation(element),
            )
        else:
            engine_domain = _engine_ring(domain)
            if getattr(element, "parent", lambda: None)() is engine_domain:
                presented = engine_domain(element)
            else:
                presented = _engine_element(domain, domain(element))
        engine = presented.parent()
        labels = self._finite_engine_generator_labels()
        generator_labels = dict(zip(engine.monoid().gens(), labels, strict=True))
        for monomial, coefficient in presented.monomial_coefficients().items():
            word = tuple(
                generator_labels[generator]
                for generator, exponent in monomial
                for _ in range(int(exponent))
            )
            base = domain.base_ring()
            yield word, _owned_engine_element(base, _engine_ring(base)(coefficient))

    def _symmetric_terms(self, element):
        domain = self.domain()
        if hasattr(domain, "lift_to_presentation"):
            presentation_ring = domain.presentation_ring()
            presented = _engine_element(
                presentation_ring,
                domain.lift_to_presentation(element),
            )
        else:
            engine_domain = _engine_ring(domain)
            if getattr(element, "parent", lambda: None)() is engine_domain:
                presented = engine_domain(element)
            else:
                presented = _engine_element(domain, domain(element))
        labels = self._finite_engine_generator_labels()
        for monomial, coefficient in presented.monomial_coefficients().items():
            try:
                exponents = tuple(int(exponent) for exponent in monomial)
            except TypeError:
                if hasattr(monomial, "exponents"):
                    exponents = tuple(monomial.exponents()[0])
                else:
                    exponents = (int(monomial),)
            factors = tuple(
                label
                for label, exponent in zip(labels, exponents, strict=True)
                for _ in range(int(exponent))
            )
            base = domain.base_ring()
            yield factors, _owned_engine_element(base, _engine_ring(base)(coefficient))

    def _finite_engine_generator_labels(self):
        labels = self.domain().algebra_generating_set()
        assert labels.cardinality().is_finite(), (
            "the private free-algebra engine realization requires a finite generator framing"
        )
        return tuple(labels)

    def _call_(self, element):
        domain = self.domain()
        terms = (
            self._tensor_terms(element)
            if domain in TensorAlgebras(domain.base_ring())
            else self._symmetric_terms(element)
        )
        return sum(
            (
                coefficient
                * prod(
                    (self._images[label] for label in factors),
                    start=self.codomain().one(),
                )
                for factors, coefficient in terms
            ),
            self.codomain().zero(),
        )

    def __call__(self, element):
        return self._call_(element)

    def is_identity(self) -> bool:
        return self._preamble_is_identity

    def __mul__(self, other):
        if not isinstance(other, FramedFreeAlgebraMorphism) or other.codomain() is not self.domain():
            return super().__mul__(other)
        if self.is_identity():
            return other
        if other.is_identity():
            return self
        return super().__mul__(other)


class FramedFreeAlgebraMor(_AlgebraMorCommonMethods, CategoricalMor):
    Element = FramedFreeAlgebraMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism Mor object")
        identity = self(lambda label: self.domain().algebra_generator(label))
        identity._preamble_is_identity = True
        return identity
