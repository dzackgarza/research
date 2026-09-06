"""Free symmetric, tensor, alternating, and divided-power algebra categories."""

from typing import Any, cast

from sage.algebras.free_algebra import FreeAlgebra as _SageFreeAlgebra
from sage.all import (
    LaurentPolynomialRing as _SageLaurentPolynomialRing,
    PolynomialRing as _SagePolynomialRing,
)
from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_function
from sage.rings.ideal import Ideal_generic
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    AlgebraMorphism,
    CommutativeAlgebraCoproducts,
    CommutativeAlgebraPushouts,
    CommutativeAlgebras,
    FinitelyPresentedAlgebras,
    FramedAlgebras,
    OwnedAlgebras,
    _OwnedAlgebraParent,
    _AlgebraHomsetCommonMethods,
    _default_structure_map,
    algebra_homset,
    refine_algebra,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
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
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.graded_commutative_algebras import StrictlyGradedCommutativeAlgebras
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOn
from dzack_research.preamble.categories.modules.powers import (
    AlternatingPower,
    DividedPower,
    SymmetricPower,
    TensorPower,
)
from dzack_research.preamble.categories.modules.pure.modules import FinitelyGeneratedFreeModules


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


def FreeAlgebraOn(base_ring, algebra_generating_set):
    r"""Return the free commutative algebra ``R[S] = Sym(F_R(S))``."""
    return SymmetricAlgebraOn(base_ring, algebra_generating_set)


def PolynomialRing(base_ring, *args, **kwargs):
    base = _owned_ring(base_ring)
    result = _own_ring(_SagePolynomialRing(_engine_ring(base), *args, **kwargs))
    labels = tuple(_engine_ring(result).variable_names())
    algebra = refine_algebra(
        result,
        base,
        labels,
        FreeAlgebras(base),
        GradedFreeAlgebras(base),
        SymmetricAlgebras(base),
    )

    return algebra


def LaurentPolynomialRing(base_ring, *args, **kwargs):
    base = _owned_ring(base_ring)
    result = _own_ring(
        _SageLaurentPolynomialRing(_engine_ring(base), *args, **kwargs)
    )
    labels = tuple(_engine_ring(result).variable_names())
    algebra = refine_algebra(result, base, labels)

    return algebra


def SymmetricAlgebraOn(base_ring, algebra_generating_set):
    labels = _finite_labels(algebra_generating_set)
    base = _owned_ring(base_ring)
    algebra = PolynomialRing(base, _variable_names(labels))

    return refine_algebra(
        algebra,
        base,
        labels,
        FreeAlgebras(base),
        GradedFreeAlgebras(base),
        SymmetricAlgebras(base),
    )


def TensorAlgebraOn(base_ring, algebra_generating_set):
    labels = _finite_labels(algebra_generating_set)
    base = _owned_ring(base_ring)
    names = _variable_names(labels)
    algebra = _SageFreeAlgebra(_engine_ring(base), len(labels), names=names)
    return refine_algebra(
        algebra,
        base,
        labels,
        FreeAlgebras(base),
        GradedFreeAlgebras(base),
        TensorAlgebras(base),
    )


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
            lambda index: presentation_ring._from_engine_element(
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
        presentation_ring._engine_element(selected_relations.value(index))
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
    target_presentation_ring = SymmetricAlgebraOn(
        target_base, algebra.algebra_generating_set()
    )
    source_base = algebra.base_ring()
    source_engine = _engine_ring(source_base)
    target_base_engine = _engine_ring(target_base)
    target_engine = _engine_ring(target_presentation_ring)

    def map_backend_scalar(scalar):
        owned_scalar = source_base._from_engine_element(source_engine(scalar))
        return _engine_element(target_base, ring_map(owned_scalar))

    backend_base_map = SetMorphism(
        source_engine.Hom(target_base_engine),
        map_backend_scalar,
    )
    source_presentation = algebra.presentation_ring()
    mapped_relations = tuple(
        target_presentation_ring._from_engine_element(
            target_engine(
                _engine_element(source_presentation, relation).map_coefficients(
                    backend_base_map,
                    new_base_ring=target_base_engine,
                )
            )
        )
        for relation in algebra.relations()
    )
    return FinitelyPresentedAlgebra(target_presentation_ring, mapped_relations)


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
        free_source_module=None,
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
        self._preamble_presentation_ring = presentation_ring
        self._preamble_presentation_relations = selected_relations
        self._preamble_presentation_ideal = presentation_ideal
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
            return presentation_ring._from_engine_element(representative)

        self._preamble_lift_to_presentation = lift_to_presentation
        if free_source_module is not None:
            self._preamble_free_algebra_source_module = free_source_module

        placement = [
            FinitelyPresentedAlgebras(base),
            AlgebrasWithChosenFinitePresentation(base),
            CommutativeAlgebras(base),
            *tuple(extra_categories),
        ]
        if finite_free_degree is not None:
            module_labels = Sets.Δ[finite_free_degree - 1]
            self._preamble_module_generating_set = module_labels
            module_primitive = (
                quotient_engine.gen()
                if finite_free_generator is None
                else finite_free_generator
            )
            self._preamble_module_generator_values = indexed_family(
                module_labels,
                lambda exponent: self._from_engine_element(module_primitive) ** int(exponent),
                name="Quotient module generator values",
            )

            def module_coordinates(element):
                backend = quotient_engine(self._engine_element(self(element)))
                coordinates = (
                    backend
                    if finite_free_coordinates is None
                    else finite_free_coordinates(backend)
                )
                return (
                    base._from_engine_element(coefficient)
                    for coefficient in coordinates
                )

            self._preamble_module_coordinate_function = module_coordinates
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

        _OwnedAlgebraParent.__init__(
            self,
            quotient_engine,
            base,
            labels,
            generator_values=selected_generator_values,
            categories=tuple(placement),
        )
        self._preamble_algebra_presentation_morphism = algebra_homset(
            presentation_ring,
            self,
        )(
            lambda label: self.algebra_generator(label)
        )
        if commutative_backend:
            self._preamble_base_change_selected_presentation = lambda ring_map: (
                _base_change_commutative_presentation(self, ring_map)
            )
            self._preamble_commutative_algebra_coproduct_backend = lambda left, right: (
                _commutative_algebra_coproduct_backend(left, right)
            )
            self._preamble_commutative_algebra_pushout_backend = lambda left_map, right_map: (
                _commutative_algebra_pushout_backend(left_map, right_map)
            )


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


def FinitelyPresentedAlgebra(
    presentation_ring,
    relations,
    *,
    _extra_categories=(),
    _extra_construction_data=None,
    _free_source_module=None,
):
    r"""Return the selected quotient ``R[S] / (relations)``."""
    base = presentation_ring.base_ring()
    if presentation_ring in AlgebrasWithChosenFinitePresentation(base):
        # A quotient of a quotient is one quotient of the same polynomial
        # presentation: for A = P/I, the algebra A/(J) is P/(I + J~) where J~
        # lifts the new relations to P.  Consolidating here keeps one chosen
        # presentation and one scalar ring, so a second closed embedding into
        # an already presented algebra reaches the same construction as the
        # first rather than needing a tower of quotient objects.
        source = presentation_ring.presentation_ring()
        existing = presentation_ring.relations()
        return FinitelyPresentedAlgebra(
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
            _free_source_module=_free_source_module,
        )
    if presentation_ring not in SymmetricAlgebras(base):
        raise NotImplementedError(
            "the active native finite-presentation adapter currently handles commutative polynomial presentations"
        )

    presentation_ideal, selected_relations = _relations_to_ideal(
        presentation_ring, relations
    )
    presentation_engine = _engine_ring(presentation_ring)
    presentation_flattening = None
    quotient_presentation_engine = presentation_engine
    quotient_ideal = presentation_ideal
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
                    presentation_ring._engine_element(
                        selected_relations.value(index)
                    )
                )
                for index in selected_relations.index_set()
            ]
        )
    quotient_engine = quotient_presentation_engine.quotient(quotient_ideal)
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

    return _PresentedAlgebraParent(
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
        free_source_module=_free_source_module,
        commutative_backend=True,
        finite_free_degree=finite_free_degree,
        presentation_flattening=presentation_flattening,
    )


class FreeAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The free algebra on one generator."""
        from dzack_research.preamble.categories.functors.free_algebras import TensorAlgebraFunctor
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return TensorAlgebraFunctor(self.base_ring())(Modules(self.base_ring()).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "free algebras"

    def super_categories(self):

        return [Algebras(self.base_ring())]

    class ParentMethods:
        def is_free(self) -> bool:
            return True

        def algebra_homset(self, hom_family, codomain):
            return FramedFreeAlgebraHomset(hom_family, self, codomain)


class GradedFreeAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The polynomial algebra on one generator, graded by degree."""
        from dzack_research.preamble.categories.functors.free_algebras import SymmetricAlgebraFunctor
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return SymmetricAlgebraFunctor(self.base_ring())(Modules(self.base_ring()).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "graded free algebras"

    def super_categories(self):

        return [FreeAlgebras(self.base_ring()), GradedAlgebras(self.base_ring())]

    class ParentMethods:
        def graded_piece(self, degree):
            r"""Return the canonical degree piece of this free construction.

            The flavor, not this common superclass, determines the degree
            piece: ``T^n(M)``, ``Sym^n(M)``, ``Lambda^n(M)``, or
            ``Gamma^n(M)``.  This is one construction path -- the algebra does
            not build a second model of those modules.
            """
            degree = int(degree)
            if degree < 0:
                raise ValueError("a graded degree is nonnegative")

            try:
                source = self.free_source_module()
            except (AttributeError, ValueError):

                source = FreeModuleOn(
                    self.algebra_base_ring(),
                    self.algebra_generating_set(),
                )

            ring = self.algebra_base_ring()
            # These free constructions are connected: their canonical
            # degree-zero algebra and module is the scalar ring itself.
            if degree == 0:
                # The represented exterior/divided-power algebras are assembled
                # from their authoritative module-power pieces.  Their concrete
                # degree-zero piece is therefore the existing degree-zero power
                # module; do not let this generic free-algebra method replace it.
                if self in AlternatingAlgebras(ring):

                    return AlternatingPower(source, 0)
                if self in DividedPowerAlgebras(ring):

                    return DividedPower(source, 0)
                return ring

            if self in TensorAlgebras(ring):
                return TensorPower(source, degree)
            if self in SymmetricAlgebras(ring):
                return SymmetricPower(source, degree)
            if self in AlternatingAlgebras(ring):
                return AlternatingPower(source, degree)
            if self in DividedPowerAlgebras(ring):
                return DividedPower(source, degree)
            raise TypeError(
                f"the graded free-algebra flavor of {self} is not represented"
            )


class PowerAlgebraHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class_for(self, domain, codomain):
        _ = codomain
        return domain._power_algebra_homset_class()


class TensorAlgebras(OwnedCategoryOverBaseRing):
    r"""Tensor algebras of represented modules."""

    def an_object(self):
        r"""The tensor algebra on the free module of rank one."""
        from dzack_research.preamble.categories.functors.free_algebras import TensorAlgebraFunctor
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return TensorAlgebraFunctor(self.base_ring())(Modules(self.base_ring()).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "tensor algebras"

    def super_categories(self):

        return [GradedAlgebras(self.base_ring())]

    class ParentMethods:
        def free_source_module(self):
            r"""Return the module whose tensor algebra this object represents."""
            return self._preamble_free_algebra_source_module


class SymmetricAlgebras(OwnedCategoryOverBaseRing):
    r"""Symmetric algebras of represented modules."""

    def an_object(self):
        r"""The symmetric algebra on the free module of rank one."""
        from dzack_research.preamble.categories.functors.free_algebras import SymmetricAlgebraFunctor
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return SymmetricAlgebraFunctor(self.base_ring())(Modules(self.base_ring()).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "symmetric algebras"

    def super_categories(self):

        return [
            GradedAlgebras(self.base_ring()),
            CommutativeAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def free_source_module(self):
            r"""Return the module whose symmetric algebra this object represents."""
            return self._preamble_free_algebra_source_module

        def _commutative_algebra_coproduct(self, left, right):
            return _commutative_algebra_coproduct_backend(left, right)

        def _commutative_algebra_pushout(self, left_map, right_map):
            return _commutative_algebra_pushout_backend(left_map, right_map)


class AlternatingAlgebras(OwnedCategoryOverBaseRing):
    r"""Exterior/alternating algebras."""

    def an_object(self):
        r"""The exterior algebra on the free module of rank one."""
        from dzack_research.preamble.categories.functors.free_algebras import AlternatingAlgebraFunctor
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return AlternatingAlgebraFunctor(self.base_ring())(Modules(self.base_ring()).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "alternating algebras"

    def super_categories(self):

        return [StrictlyGradedCommutativeAlgebras(self.base_ring())]

    _HomCategory = PowerAlgebraHomCategoryConstruction

    class ParentMethods:
        def free_source_module(self):
            return self._preamble_free_algebra_source_module

        def Mor(self, codomain, category=None):
            alternating = AlternatingAlgebras(self.base_ring())
            if category is None and codomain in alternating:
                return alternating.Mor(self, codomain)
            return super().Mor(codomain, category=category)

        def graded_piece(self, degree):

            return AlternatingPower(self.free_source_module(), degree)


def _presentation_data(algebra):
    base = algebra.base_ring()
    if hasattr(algebra, "presentation_ring") and hasattr(algebra, "relations"):
        return algebra.presentation_ring(), tuple(algebra.relations())
    if algebra in SymmetricAlgebras(base) and algebra in FramedAlgebras(base):
        return algebra, ()
    if hasattr(algebra, "quotient_source") and hasattr(algebra, "defining_ideal"):
        source = algebra.quotient_source()
        if source in SymmetricAlgebras(base):
            return source, tuple(algebra.defining_ideal().gens())
    raise NotImplementedError(
        "the active commutative-algebra backend requires a free polynomial or selected finite presentation"
    )


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
    category = CommutativeAlgebras(base)
    if left not in category or right not in category:
        raise TypeError("both factors must be commutative algebras over the common base")
    if left not in FramedAlgebras(base) or right not in FramedAlgebras(base):
        raise NotImplementedError(
            "the active finite-presentation coproduct backend requires finite algebra framings"
        )

    left_presentation, left_relations = _presentation_data(left)
    right_presentation, right_relations = _presentation_data(right)
    combined_labels = tuple(
        ("left", label) for label in left.algebra_generating_set()
    ) + tuple(("right", label) for label in right.algebra_generating_set())
    presentation = SymmetricAlgebraOn(base, combined_labels)
    relations = _transport_relations(
        left_presentation, left_relations, presentation, "left"
    ) + _transport_relations(
        right_presentation, right_relations, presentation, "right"
    )
    construction_data = (("_preamble_coproduct_factors", (left, right)),)
    if relations:
        return FinitelyPresentedAlgebra(
            presentation,
            relations,
            _extra_categories=(CommutativeAlgebraCoproducts(base),),
            _extra_construction_data=construction_data,
        )
    return refine_algebra(
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
        identity = CommutativeAlgebras(base).Mor(algebra, algebra).identity()
        return algebra, identity
    if hasattr(algebra, "presentation_ring") and hasattr(algebra, "relations"):
        presentation = algebra.presentation_ring()
        relations = tuple(algebra.relations()) + tuple(
            algebra.lift_to_presentation(element) for element in selected
        )
    elif algebra in SymmetricAlgebras(base):
        presentation = algebra
        relations = selected
    else:
        raise NotImplementedError(
            "quotienting a commutative algebra requires a selected polynomial presentation"
        )
    quotient = FinitelyPresentedAlgebra(
        presentation,
        relations,
        _extra_categories=tuple(extra_categories),
        _extra_construction_data=extra_construction_data,
    )
    quotient_map = algebra.Mor(quotient)(
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
            "the pushout span maps must belong to the represented algebra Homs "
            "of their endpoints"
        )
    if common not in FramedAlgebras(base):
        raise NotImplementedError(
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

        return [
            GradedAlgebras(self.base_ring()),
            CommutativeAlgebras(self.base_ring()),
        ]

    _HomCategory = PowerAlgebraHomCategoryConstruction

    class ParentMethods:
        def free_source_module(self):
            return self._preamble_free_algebra_source_module

        def Mor(self, codomain, category=None):
            divided = DividedPowerAlgebras(self.base_ring())
            if category is None and codomain in divided:
                return divided.Mor(self, codomain)
            return super().Mor(codomain, category=category)

        def graded_piece(self, degree):

            return DividedPower(self.free_source_module(), degree)


def _multiply_in_target(target, factors):
    result = target.one()
    for factor in factors:
        result *= factor
    return result


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
                name="Free-algebra morphism generator-image family",
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
                name="Free-algebra morphism generator-image family",
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
                name="Free-algebra morphism generator-image family",
            )
        elif callable(images):
            self._images = indexed_family(
                labels,
                lambda label: self.codomain()(images(label)),
                name="Free-algebra morphism generator-image family",
            )
        else:
            raise TypeError(
                "an algebra morphism is specified on its algebra generators"
            )
        self._generator_images = self._images
        self._engine_morphism = None
        self._element_function = None
        self._preamble_is_identity = False
        try:
            source_module = domain.free_source_module()
        except (AttributeError, ValueError):
            source_module = None
        if source_module is not None:
            module_homset(source_module, self.codomain())(self._images.value)

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
            yield word, base._from_engine_element(_engine_ring(base)(coefficient))

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
            yield factors, base._from_engine_element(_engine_ring(base)(coefficient))

    def _finite_engine_generator_labels(self):
        labels = self.domain().algebra_generating_set()
        if not labels.cardinality().is_finite():
            raise NotImplementedError(
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
                * _multiply_in_target(
                    self.codomain(), (self._images[label] for label in factors)
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


class FramedFreeAlgebraHomset(_AlgebraHomsetCommonMethods, CategoricalHomset):
    Element = FramedFreeAlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism Hom-set")
        identity = self(lambda label: self.domain().algebra_generator(label))
        identity._preamble_is_identity = True
        return identity
