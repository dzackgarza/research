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
from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.misc.cachefunc import cached_function
from sage.rings.abc import Order as SageNumberFieldOrder
from sage.rings.ideal import Ideal_generic

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
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreeModuleBaseRings,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_if_ring,
    _own_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSet,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.refine import refine


class RingAdjunctionConstructions(Category):
    r"""Rings equipped with selected polynomial/algebraic adjunction syntax."""

    def super_categories(self):
        return [FreeModuleBaseRings()]

    class ParentMethods:
        def __getitem__(self, names):
            match names:
                case str():
                    return refine(PolynomialRing(self, names), RingAdjunctionConstructions())
                case tuple() if all(isinstance(part, str) for part in names):
                    return refine(PolynomialRing(self, names), RingAdjunctionConstructions())
                case list():
                    result = _own_if_ring(_engine_ring(self)[names])
                case _ if names in self:
                    return self
                case _:
                    result = _own_if_ring(_engine_ring(self)[names])

            if result not in OwnedRings():
                return result
            engine = _engine_ring(result)
            if isinstance(engine, SageNumberFieldOrder):
                from dzack_research.preamble.categories.rings.number_fields import (
                    _refine_order_view,
                )

                result = _refine_order_view(result)
            elif engine in SageNumberFields():
                from dzack_research.preamble.categories.rings.number_fields import (
                    _refine_number_field_view,
                )

                result = _refine_number_field_view(result)
            return refine(result, RingAdjunctionConstructions())


def _finite_labels(labels) -> FiniteOrderedSet:
    if isinstance(labels, FiniteOrderedSet):
        return labels
    if isinstance(labels, int):
        return finite_ordered_set(range(labels))
    return finite_ordered_set(labels)


def _variable_names(labels: FiniteOrderedSet) -> tuple[str, ...]:
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
    from dzack_research.preamble.categories.rings.commutative_algebra import (
        refine_commutative_ring_constructions,
    )

    return refine_commutative_ring_constructions(algebra)


def LaurentPolynomialRing(base_ring, *args, **kwargs):
    base = _owned_ring(base_ring)
    result = _own_ring(
        _SageLaurentPolynomialRing(_engine_ring(base), *args, **kwargs)
    )
    labels = tuple(_engine_ring(result).variable_names())
    algebra = refine_algebra(result, base, labels)
    from dzack_research.preamble.categories.rings.commutative_algebra import (
        refine_commutative_ring_constructions,
    )

    return refine_commutative_ring_constructions(algebra)


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


def FinitelyPresentedAlgebra(presentation_ring, relations):
    r"""Return the selected quotient ``R[S] / (relations)``."""
    base = presentation_ring.base_ring()
    if presentation_ring not in SymmetricAlgebras(base):
        raise NotImplementedError(
            "the active native finite-presentation adapter currently handles commutative polynomial presentations"
        )

    presentation_ideal, selected_relations = _relations_to_ideal(
        presentation_ring, relations
    )
    quotient_engine = _engine_ring(presentation_ring).quotient(presentation_ideal)
    labels = presentation_ring.algebra_generating_set()
    presented = _OwnedAlgebraParent(
        quotient_engine,
        base,
        labels,
        quotient_engine.coerce_map_from(_engine_ring(base)),
    )
    presented._preamble_structure_map = _default_structure_map(base, presented)
    presented._preamble_presentation_ring = presentation_ring
    presented._preamble_presentation_relations = selected_relations
    presented._preamble_presentation_ideal = presentation_ideal
    presented._preamble_lift_to_presentation = lambda element: presentation_ring._from_engine_element(
        quotient_engine(presented._engine_element(element)).lift()
    )
    presented._preamble_base_change_selected_presentation = lambda ring_map: (
        _base_change_commutative_presentation(presented, ring_map)
    )
    presented._preamble_commutative_algebra_coproduct_backend = lambda left, right: (
        _commutative_algebra_coproduct_backend(left, right)
    )
    presented._preamble_quotient_by_algebra_elements_backend = lambda elements: (
        _quotient_by_algebra_elements_backend(presented, elements)
    )
    presented._preamble_commutative_algebra_pushout_backend = lambda left_map, right_map: (
        _commutative_algebra_pushout_backend(left_map, right_map)
    )

    module_categories = []
    label_size = cardinal(labels.cardinality())
    if (
        label_size.is_finite()
        and int(label_size.finite_value()) == 1
        and hasattr(quotient_engine, "modulus")
    ):
        modulus = quotient_engine.modulus()
        degree = int(modulus.degree())
        if degree > 0:
            from dzack_research.preamble.categories.modules.pure.modules import (
                FinitelyGeneratedFreeModules,
            )

            module_labels = Sets.Δ[degree - 1]
            quotient_generator = presented._from_engine_element(quotient_engine.gen())
            presented._preamble_base_ring = base
            presented._preamble_module_generating_set = module_labels
            presented._preamble_module_generator_values = indexed_family(
                module_labels,
                lambda exponent: quotient_generator ** int(exponent),
                name="Quotient module generator values",
            )
            presented._preamble_module_coordinate_function = lambda element: (
                base._from_engine_element(coefficient)
                for coefficient in quotient_engine(
                    presented._engine_element(presented(element))
                )
            )
            module_categories.append(FinitelyGeneratedFreeModules(base))

    presented = refine(
        presented,
        [
            Algebras(base),
            OwnedAlgebras(base),
            CommutativeAlgebras(base),
            FramedAlgebras(base),
            FinitelyPresentedAlgebras(base),
            AlgebrasWithChosenFinitePresentation(base),
        ]
        + module_categories,
    )
    presented._preamble_algebra_presentation_morphism = algebra_homset(
        presentation_ring,
        presented,
    )(
        lambda label: presented.algebra_generator(label)
    )
    from dzack_research.preamble.categories.rings.commutative_algebra import (
        refine_commutative_ring_constructions,
    )

    return refine_commutative_ring_constructions(presented)


class FreeAlgebras(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "free algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        return [Algebras(self.base_ring())]

    class ParentMethods:
        def is_free(self) -> bool:
            return True

        def _algebra_homset(self, hom_family, codomain):
            return FramedFreeAlgebraHomset(hom_family, self, codomain)


class GradedFreeAlgebras(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "graded free algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.graded_algebras import (
            GradedAlgebras,
        )

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
                from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                    FreeModuleOn,
                )

                source = FreeModuleOn(
                    self.algebra_base_ring(),
                    self.algebra_generating_set(),
                )

            ring = self.algebra_base_ring()
            # These free constructions are connected: their canonical
            # degree-zero algebra and module is the scalar ring itself.
            if degree == 0:
                # The represented exterior/divided-power carriers are assembled
                # from their authoritative module-power pieces.  Their concrete
                # degree-zero piece is therefore the existing degree-zero power
                # module; do not let this generic free-algebra method replace it.
                if self in AlternatingAlgebras(ring):
                    from dzack_research.preamble.categories.modules.powers import (
                        AlternatingPower,
                    )

                    return AlternatingPower(source, 0)
                if self in DividedPowerAlgebras(ring):
                    from dzack_research.preamble.categories.modules.powers import (
                        DividedPower,
                    )

                    return DividedPower(source, 0)
                return ring
            from dzack_research.preamble.categories.modules.powers import (
                AlternatingPower,
                DividedPower,
                SymmetricPower,
                TensorPower,
            )

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
    def fixed_category_class(self):
        from dzack_research.preamble.categories.algebras.power_algebras import (
            PowerAlgebraHomset,
        )

        return PowerAlgebraHomset


class TensorAlgebras(OwnedCategoryOverBaseRing):
    r"""Tensor algebras of represented modules."""

    @classmethod
    def _repr_object_names(cls):
        return "tensor algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.graded_algebras import (
            GradedAlgebras,
        )

        return [GradedAlgebras(self.base_ring())]

    class ParentMethods:
        def free_source_module(self):
            r"""Return the module whose tensor algebra this object represents."""
            return self._preamble_free_algebra_source_module


class SymmetricAlgebras(OwnedCategoryOverBaseRing):
    r"""Symmetric algebras of represented modules."""

    @classmethod
    def _repr_object_names(cls):
        return "symmetric algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import (
            CommutativeAlgebras,
        )
        from dzack_research.preamble.categories.algebras.graded_algebras import (
            GradedAlgebras,
        )

        return [
            GradedAlgebras(self.base_ring()),
            CommutativeAlgebras(self.base_ring()),
        ]

    _HomCategory = PowerAlgebraHomCategoryConstruction

    class ParentMethods:
        def free_source_module(self):
            r"""Return the module whose symmetric algebra this object represents."""
            return self._preamble_free_algebra_source_module

        def _commutative_algebra_coproduct(self, left, right):
            return _commutative_algebra_coproduct_backend(left, right)

        def _quotient_by_algebra_elements(self, elements):
            return _quotient_by_algebra_elements_backend(self, elements)

        def _commutative_algebra_pushout(self, left_map, right_map):
            return _commutative_algebra_pushout_backend(left_map, right_map)


class AlternatingAlgebras(OwnedCategoryOverBaseRing):
    r"""Exterior/alternating algebras."""

    @classmethod
    def _repr_object_names(cls):
        return "alternating algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.graded_commutative_algebras import (
            StrictlyGradedCommutativeAlgebras,
        )

        return [StrictlyGradedCommutativeAlgebras(self.base_ring())]

    _HomCategory = PowerAlgebraHomCategoryConstruction

    class ParentMethods:
        def free_source_module(self):
            return self._preamble_free_algebra_source_module

        def graded_piece(self, degree):
            from dzack_research.preamble.categories.modules.powers import (
                AlternatingPower,
            )

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
    coproduct = FinitelyPresentedAlgebra(presentation, relations) if relations else presentation
    left_map = left.Mor(coproduct)(
        {
            label: coproduct.algebra_generator(("left", label))
            for label in left.algebra_generating_set()
        }
    )
    right_map = right.Mor(coproduct)(
        {
            label: coproduct.algebra_generator(("right", label))
            for label in right.algebra_generating_set()
        }
    )
    coproduct._preamble_coproduct_factors = (left, right)
    coproduct._preamble_coproduct_injections = (left_map, right_map)
    return refine(coproduct, CommutativeAlgebraCoproducts(base))


def _quotient_by_algebra_elements_backend(algebra, elements):
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
    quotient = FinitelyPresentedAlgebra(presentation, relations)
    quotient_map = algebra.Mor(quotient)(
        {
            label: quotient.algebra_generator(label)
            for label in algebra.algebra_generating_set()
        }
    )
    return quotient, quotient_map


@cached_function
def _commutative_algebra_pushout_backend(left_map, right_map):
    if not isinstance(left_map, AlgebraMorphism) or not isinstance(
        right_map, AlgebraMorphism
    ):
        raise TypeError("a commutative-algebra pushout is specified by algebra morphisms")
    if left_map.domain() is not right_map.domain():
        raise ValueError("pushout maps require one common domain")
    common = left_map.domain()
    left = left_map.codomain()
    right = right_map.codomain()
    base = common.base_ring()
    if left.base_ring() is not base or right.base_ring() is not base:
        raise ValueError("the pushout span must lie over one scalar base")
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
    quotient_operation = getattr(tensor, "_quotient_by_algebra_elements", None)
    if quotient_operation is None:
        raise NotImplementedError(
            "the represented coproduct has no selected algebra-quotient backend"
        )
    pushout, quotient_map = quotient_operation(equalities)
    left_pushout = quotient_map * left_injection
    right_pushout = quotient_map * right_injection
    pushout._preamble_pushout_span = (left_map, right_map)
    pushout._preamble_pushout_maps = (left_pushout, right_pushout)
    pushout._preamble_pushout_coproduct = tensor
    return refine(pushout, CommutativeAlgebraPushouts(base))

class DividedPowerAlgebras(OwnedCategoryOverBaseRing):
    r"""Divided-power algebras ``Gamma(M)`` with their canonical grading."""

    @classmethod
    def _repr_object_names(cls):
        return "divided power algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import (
            CommutativeAlgebras,
        )
        from dzack_research.preamble.categories.algebras.graded_algebras import (
            GradedAlgebras,
        )

        return [
            GradedAlgebras(self.base_ring()),
            CommutativeAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def free_source_module(self):
            return self._preamble_free_algebra_source_module

        def graded_piece(self, degree):
            from dzack_research.preamble.categories.modules.powers import DividedPower

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
        labels = tuple(domain.algebra_generating_set())
        if isinstance(images, dict):
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(f"algebra-generator assignment omits {missing}")
            self._images = {label: images[label] for label in labels}
        elif isinstance(images, (tuple, list)):
            if len(images) != len(labels):
                raise ValueError(
                    "the number of algebra-generator images must equal the framing size"
                )
            self._images = dict(zip(labels, images, strict=True))
        elif callable(images):
            self._images = {label: images(label) for label in labels}
        else:
            raise TypeError(
                "an algebra morphism is specified on its algebra generators"
            )
        self._generator_images = dict(self._images)
        self._engine_morphism = None
        self._element_function = None
        try:
            source_module = domain.free_source_module()
        except (AttributeError, ValueError):
            source_module = None
        if source_module is not None:
            module_homset(source_module, self.codomain())(self._images.__getitem__)

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
        labels = tuple(domain.algebra_generating_set())
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
        labels = tuple(domain.algebra_generating_set())
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
        return self(lambda label: self.domain().algebra_generator(label))
