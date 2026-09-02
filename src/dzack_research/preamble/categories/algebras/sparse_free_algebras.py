r"""Sparse tensor and symmetric algebras on infinitely framed free modules."""

from dzack_research.preamble.categories.rings import engine_ring as _engine_ring
from itertools import count, product
from typing import Any, cast

from sage.categories.category import Category
from sage.categories.enumerated_sets import EnumeratedSets
from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.categories.sets_cat import Sets
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.rings import OwnedRings as _OwnedRings
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    CommutativeAlgebras,
    FramedAlgebras,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    GradedFreeAlgebras,
    SymmetricAlgebras,
    TensorAlgebras,
)
from dzack_research.preamble.categories.modules.framed.framed_modules import (
    FramedModules,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.rings import owned_ring_view
from dzack_research.preamble.categories.rings import engine_ring
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
)
from dzack_research.preamble.categories.sets import aleph0


def _symmetric_label(factors):
    exponents = {}
    for factor in factors:
        exponents[factor] = exponents.get(factor, 0) + 1
    return frozenset(exponents.items())


def _nested_label(labels):
    labels = tuple(labels)
    if not labels:
        return 0
    result = labels[0]
    for label in labels[1:]:
        result = (result, label)
    return result


def _flatten_nested_label(label, length):
    if length == 0:
        return ()
    if length == 1:
        return (label,)
    left, right = label
    return _flatten_nested_label(left, length - 1) + (right,)


class SparseFreeAlgebraBasis(Parent):
    def __init__(self, algebra, degree=None) -> None:
        self._algebra = algebra
        self._degree = degree
        Parent.__init__(self, category=EnumeratedSets())

    def algebra(self):
        return self._algebra

    def degree(self):
        return self._degree

    def __contains__(self, candidate) -> bool:
        labels = self.algebra().algebra_generating_set()
        if self.algebra().flavor() == "tensor":
            valid = isinstance(candidate, tuple) and all(
                label in labels for label in candidate
            )
            degree = len(candidate) if valid else None
        else:
            valid = isinstance(candidate, frozenset)
            if valid:
                try:
                    valid = all(
                        label in labels and int(exponent) > 0
                        for label, exponent in candidate
                    )
                    degree = sum(int(exponent) for _label, exponent in candidate)
                except (TypeError, ValueError):
                    valid = False
                    degree = None
            else:
                degree = None
        return bool(valid and (self.degree() is None or degree == self.degree()))

    def _element_constructor_(self, candidate):
        if candidate not in self:
            raise ValueError(f"{candidate!r} is not a sparse free-algebra basis label")
        return candidate

    def __iter__(self):
        labels = self.algebra().algebra_generating_set()
        cardinality = labels.cardinality()
        if cardinality not in SageZZ:
            raise NotImplementedError(
                "the infinite basis is represented extensionally; iterate its source labels instead"
            )
        labels = tuple(labels)
        degrees = count() if self.degree() is None else (self.degree(),)
        for degree in degrees:
            if self.algebra().flavor() == "tensor":
                yield from product(labels, repeat=degree)
            else:
                seen = set()
                for factors in product(labels, repeat=degree):
                    label = _symmetric_label(factors)
                    if label not in seen:
                        seen.add(label)
                        yield label

    def cardinality(self):
        return aleph0

    def _repr_(self):
        flavor = self.algebra().flavor()
        return f"Sparse {flavor}-monomial indices of {self.algebra()}"


class SparseFreeAlgebraElement(ModuleElement):
    def __init__(self, parent, coefficients) -> None:
        ModuleElement.__init__(self, parent)
        ring = parent.base_ring()
        normalized: dict[Any, Any] = {}
        for label, coefficient in coefficients.items():
            label = parent.module_generating_set()._element_constructor_(label)
            coefficient = ring(coefficient)
            if coefficient:
                normalized[label] = normalized.get(label, ring.zero()) + coefficient
        self._coefficients = {
            label: coefficient
            for label, coefficient in normalized.items()
            if coefficient
        }

    def monomial_coefficients(self):
        return dict(self._coefficients)

    def _add_(self, other):
        result = self.monomial_coefficients()
        for label, coefficient in other._coefficients.items():
            result[label] = (
                result.get(label, self.parent().base_ring().zero()) + coefficient
            )
        return self.parent()._from_dict(result)

    def _neg_(self):
        return self.parent()._from_dict(
            {label: -coefficient for label, coefficient in self._coefficients.items()}
        )

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _mul_(self, other):
        return self.parent().multiply(self, other)

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = (
            isinstance(other, SparseFreeAlgebraElement)
            and other.parent() is self.parent()
            and other._coefficients == self._coefficients
        )
        return equal if op == op_EQ else not equal

    def _repr_(self):
        if not self._coefficients:
            return "0"
        return " + ".join(
            f"{coefficient}*{label}"
            for label, coefficient in self._coefficients.items()
        )


class SparseFreeAlgebraDegreeElement(ModuleElement):
    r"""An element of one homogeneous piece of a sparse free algebra."""

    def __init__(self, parent, algebra_element) -> None:
        ModuleElement.__init__(self, parent)
        algebra_element = parent.algebra()(algebra_element)
        if any(
            label not in parent.module_generating_set()
            for label in algebra_element.monomial_coefficients()
        ):
            raise ValueError(
                "the sparse algebra element has another homogeneous degree"
            )
        self._algebra_element = algebra_element

    def algebra_element(self):
        return self._algebra_element

    def monomial_coefficients(self):
        return self.algebra_element().monomial_coefficients()

    def _add_(self, other):
        return self.parent().from_algebra_element(
            self.algebra_element() + other.algebra_element()
        )

    def _neg_(self):
        return self.parent().from_algebra_element(-self.algebra_element())

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = (
            isinstance(other, SparseFreeAlgebraDegreeElement)
            and other.parent() is self.parent()
            and other.algebra_element() == self.algebra_element()
        )
        return equal if op == op_EQ else not equal

    def _repr_(self):
        return repr(self.algebra_element())


class SparseFreeAlgebraDegreeModule(Parent):
    r"""One exact homogeneous module of a sparse free algebra."""

    Element = SparseFreeAlgebraDegreeElement

    def __init__(self, algebra, degree) -> None:
        self._algebra = algebra
        self._degree = int(degree)
        self._basis = SparseFreeAlgebraBasis(algebra, self._degree)
        Parent.__init__(
            self,
            base=algebra.base_ring(),
            category=FramedModules(algebra.base_ring()),
        )

    def algebra(self):
        return self._algebra

    def degree(self):
        return self._degree

    def base_ring(self):
        return self.algebra().base_ring()

    def module_generating_set(self):
        return self._basis

    def module_generator(self, label):
        label = self.module_generating_set()._element_constructor_(label)
        return self.from_algebra_element(
            self.algebra()._from_dict({label: self.base_ring().one()})
        )

    def linear_combination(self, coefficients):
        return self.from_algebra_element(self.algebra()._from_dict(coefficients))

    def from_algebra_element(self, element):
        return self.element_class(self, element)

    def _element_constructor_(self, value):
        if isinstance(value, SparseFreeAlgebraDegreeElement):
            if value.parent() is self:
                return value
            raise TypeError("the element belongs to another homogeneous piece")
        if isinstance(value, dict):
            return self.linear_combination(value)
        return self.from_algebra_element(value)

    def zero(self):
        return self.from_algebra_element(self.algebra().zero())

    def scalar_multiple(self, scalar, element):
        element = self(element)
        return self.from_algebra_element(
            self.algebra().scalar_multiple(scalar, element.algebra_element())
        )

    def realize(self, element):
        return self(element).algebra_element()

    def _repr_(self):
        return f"Degree-{self.degree()} piece of {self.algebra()}"


class SparseFreeAlgebra(Parent):
    r"""A free algebra whose elements are finite sums of sparse monomials."""

    Element = SparseFreeAlgebraElement

    def __init__(self, module, flavor) -> None:
        if flavor not in {"tensor", "symmetric"}:
            raise ValueError("the sparse free-algebra flavor is tensor or symmetric")
        self._source_module = module
        self._flavor = flavor
        self._base_ring = owned_ring_view(module.base_ring())
        self._basis = None
        self._component_cache: dict[Any, Any] = {}
        self._graded_piece_cache: dict[int, SparseFreeAlgebraDegreeModule] = {}
        flavor_category = (
            TensorAlgebras(self._base_ring)
            if flavor == "tensor"
            else SymmetricAlgebras(self._base_ring)
        )
        categories: list[Any] = [
            Algebras(self._base_ring),
            flavor_category,
            GradedFreeAlgebras(self._base_ring),
            FramedAlgebras(self._base_ring),
            FramedModules(self._base_ring),
        ]
        if flavor == "symmetric":
            categories.append(CommutativeAlgebras(self._base_ring))
        Parent.__init__(
            self,
            base=_engine_ring(self._base_ring),
            category=Category.join(tuple(categories)),
        )

    def flavor(self):
        return self._flavor

    def base_ring(self):
        return self._base_ring

    algebra_base_ring = base_ring

    def engine(self):
        return self

    def free_source_module(self):
        return self._source_module

    def _source_has_component_protocol(self):
        source = self.free_source_module()
        return all(
            hasattr(source, name)
            for name in (
                "module_component_key",
                "module_component",
                "module_component_generator_label",
                "module_label_from_component",
            )
        )

    def algebra_generating_set(self):
        return self.free_source_module().module_generating_set()

    def _generator_basis_label(self, label):
        if label not in self.algebra_generating_set():
            raise ValueError(f"{label!r} is not an algebra-generator label")
        return (label,) if self.flavor() == "tensor" else frozenset(((label, 1),))

    def algebra_generator(self, label):
        return self._from_dict(
            {self._generator_basis_label(label): self.base_ring().one()}
        )

    def module_generating_set(self):
        if self._basis is None:
            self._basis = SparseFreeAlgebraBasis(self)
        return self._basis

    def module_generator(self, label):
        label = self.module_generating_set()._element_constructor_(label)
        return self._from_dict({label: self.base_ring().one()})

    def graded_piece(self, degree):
        degree = int(degree)
        if degree < 0:
            raise ValueError("a graded degree is nonnegative")
        if degree == 0:
            from dzack_research.preamble.categories.modules.framed.finitely_generated.ring_as_module import (
                ring_as_module,
            )

            return ring_as_module(self.base_ring())
        if degree == 1:
            return self.free_source_module()
        cached = self._graded_piece_cache.get(degree)
        if cached is None:
            cached = SparseFreeAlgebraDegreeModule(self, degree)
            self._graded_piece_cache[degree] = cached
        return cached

    def linear_combination(self, coefficients):
        return self._from_dict(coefficients)

    def _from_dict(self, coefficients):
        if self._source_has_component_protocol():
            coefficients = self._normalize_component_relations(coefficients)
        return self.element_class(self, coefficients)

    def _monomial_component_key(self, basis_label):
        source = self.free_source_module()
        if self.flavor() == "tensor":
            return tuple(source.module_component_key(label) for label in basis_label)
        multiplicities = {}
        for label, exponent in basis_label:
            key = source.module_component_key(label)
            multiplicities[key] = multiplicities.get(key, 0) + int(exponent)
        return frozenset(multiplicities.items())

    def _component_items(self, key):
        return tuple(sorted(key, key=lambda item: repr(item[0])))

    def _component_module(self, key):
        cached = self._component_cache.get(key)
        if cached is not None:
            return cached

        source = self.free_source_module()
        if self.flavor() == "tensor":
            factors = tuple(source.module_component(source_key) for source_key in key)
        else:
            from dzack_research.preamble.categories.modules.powers import SymmetricPower

            factors = tuple(
                SymmetricPower(source.module_component(source_key), multiplicity)
                for source_key, multiplicity in self._component_items(key)
            )

        if not factors:
            from dzack_research.preamble.categories.modules.framed.finitely_generated.ring_as_module import (
                ring_as_module,
            )

            component = ring_as_module(self.base_ring())
        else:
            component = factors[0]
            if len(factors) > 1:
                from dzack_research.preamble.categories.abstract_categories import (
                    TensorProduct,
                )

                for factor in factors[1:]:
                    component = TensorProduct(component, factor)
        self._component_cache[key] = component
        return component

    def _component_generator_label(self, basis_label):
        source = self.free_source_module()
        if self.flavor() == "tensor":
            return _nested_label(
                source.module_component_generator_label(label) for label in basis_label
            )

        grouped = {}
        for source_label, exponent in basis_label:
            key = source.module_component_key(source_label)
            component_label = source.module_component_generator_label(source_label)
            counts = grouped.setdefault(key, {})
            counts[component_label] = counts.get(component_label, 0) + int(exponent)

        factor_labels = []
        for key, multiplicity in self._component_items(
            self._monomial_component_key(basis_label)
        ):
            counts = grouped[key]
            source_component = source.module_component(key)
            if multiplicity == 1:
                factor_labels.append(next(iter(counts)))
            else:
                factor_labels.append(
                    tuple(
                        counts.get(label, 0)
                        for label in source_component.module_generating_set()
                    )
                )
        return _nested_label(factor_labels)

    def _basis_label_from_component(self, key, component_label):
        source = self.free_source_module()
        if self.flavor() == "tensor":
            component_labels = _flatten_nested_label(component_label, len(key))
            return tuple(
                source.module_label_from_component(source_key, source_label)
                for source_key, source_label in zip(key, component_labels, strict=True)
            )

        items = self._component_items(key)
        factor_labels = _flatten_nested_label(component_label, len(items))
        counts = {}
        for (source_key, multiplicity), factor_label in zip(
            items, factor_labels, strict=True
        ):
            source_component = source.module_component(source_key)
            if multiplicity == 1:
                labelled_factors = ((factor_label, 1),)
            else:
                labelled_factors = zip(
                    source_component.module_generating_set(),
                    tuple(factor_label),
                    strict=True,
                )
            for source_component_label, exponent in labelled_factors:
                exponent = int(exponent)
                if not exponent:
                    continue
                source_label = source.module_label_from_component(
                    source_key, source_component_label
                )
                counts[source_label] = counts.get(source_label, 0) + exponent
        return frozenset(counts.items())

    def _normalize_component_relations(self, coefficients):
        grouped = {}
        ring = self.base_ring()
        for basis_label, coefficient in coefficients.items():
            basis_label = self.module_generating_set()._element_constructor_(
                basis_label
            )
            coefficient = ring(coefficient)
            if not coefficient:
                continue
            key = self._monomial_component_key(basis_label)
            component_label = self._component_generator_label(basis_label)
            component_coefficients = grouped.setdefault(key, {})
            component_coefficients[component_label] = (
                component_coefficients.get(component_label, ring.zero()) + coefficient
            )

        normalized = {}
        for key, component_coefficients in grouped.items():
            component = self._component_module(key)
            element = component.linear_combination(component_coefficients)
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
                ModulesWithChosenFinitePresentation,
            )

            if component in ModulesWithChosenFinitePresentation(self.base_ring()):
                from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
                    _canonical_smith_representative,
                )

                element = _canonical_smith_representative(component, element)
            for component_label, coefficient in module_coefficients(
                element, component
            ).items():
                basis_label = self._basis_label_from_component(key, component_label)
                normalized[basis_label] = normalized.get(
                    basis_label, ring.zero()
                ) + ring(coefficient)
        return {
            label: coefficient
            for label, coefficient in normalized.items()
            if coefficient
        }

    # Present this sparse algebra, as a module, by finite relation components.
    # This makes another sparse free construction on it exact as well.
    def module_component_key(self, label):
        label = self.module_generating_set()._element_constructor_(label)
        if self._source_has_component_protocol():
            return self._monomial_component_key(label)
        return label

    def module_component(self, key):
        if self._source_has_component_protocol():
            return self._component_module(key)
        from dzack_research.preamble.categories.modules.framed.finitely_generated.ring_as_module import (
            ring_as_module,
        )

        return ring_as_module(self.base_ring())

    def module_component_generator_label(self, label):
        label = self.module_generating_set()._element_constructor_(label)
        if self._source_has_component_protocol():
            return self._component_generator_label(label)
        return 0

    def module_label_from_component(self, key, component_label):
        if self._source_has_component_protocol():
            return self.module_generating_set()._element_constructor_(
                self._basis_label_from_component(key, component_label)
            )
        if component_label != 0:
            raise ValueError("a rank-one free component has generator label 0")
        return self.module_generating_set()._element_constructor_(key)

    def _element_constructor_(self, value):
        if isinstance(value, SparseFreeAlgebraElement):
            if value.parent() is self:
                return value
            raise TypeError("the element belongs to a different sparse free algebra")
        if value in self.free_source_module():
            result = self.zero()
            for label, coefficient in module_coefficients(
                value, self.free_source_module()
            ).items():
                result += coefficient * self.algebra_generator(label)
            return result
        try:
            scalar = self.base_ring()(value)
        except (TypeError, ValueError):
            if isinstance(value, dict):
                return self._from_dict(value)
            raise TypeError(f"{value!r} does not define an element of {self}") from None
        return self._from_dict({self._unit_label(): scalar})

    def _unit_label(self):
        return () if self.flavor() == "tensor" else frozenset()

    def zero(self):
        return self._from_dict({})

    def one(self):
        return self._from_dict({self._unit_label(): self.base_ring().one()})

    def scalar_multiple(self, scalar, element):
        element = self(element)
        scalar = self.base_ring()(scalar)
        return self._from_dict(
            {
                label: scalar * coefficient
                for label, coefficient in element.monomial_coefficients().items()
            }
        )

    def _multiply_labels(self, left, right):
        if self.flavor() == "tensor":
            return left + right
        # A label may occur in both frozensets; union alone loses that overlap.
        counts = {}
        for monomial in (left, right):
            for label, exponent in monomial:
                counts[label] = counts.get(label, 0) + int(exponent)
        return frozenset(counts.items())

    def multiply(self, left, right):
        left = self(left)
        right = self(right)
        result = {}
        for left_label, left_coefficient in left.monomial_coefficients().items():
            for right_label, right_coefficient in right.monomial_coefficients().items():
                label = self._multiply_labels(left_label, right_label)
                result[label] = (
                    result.get(label, self.base_ring().zero())
                    + left_coefficient * right_coefficient
                )
        return self._from_dict(result)

    def _ring_morphism_defining_algebra_structure(self):
        return SetMorphism(
            Hom(self.base_ring(), self, _OwnedRings()),
            lambda scalar: self(scalar),
        )

    algebra_structure_morphism = _ring_morphism_defining_algebra_structure

    def ring_center(self):
        if self.flavor() == "symmetric":
            return self
        raise NotImplementedError("the center of this tensor algebra is not selected")

    def hom(self, images, codomain=None):
        if codomain is None:
            raise TypeError("the target algebra is required")
        return sparse_free_algebra_homset(self, codomain)(images)

    def _repr_(self):
        name = "T" if self.flavor() == "tensor" else "Sym"
        return f"{name}({self.free_source_module()})"


def _multiply_in_target(target, factors):
    result = target.one()
    for factor in factors:
        result *= factor
    return result


def _uses_free_construction_homset(domain):
    if isinstance(domain, SparseFreeAlgebra):
        return True
    ring = domain.base_ring()
    return domain in TensorAlgebras(ring) or domain in SymmetricAlgebras(ring)


def compose_with_free_construction(left, right):
    r"""Compose through a sparse/free map without assuming a free source."""
    if right.codomain() is not left.domain():
        return NotImplemented
    source = right.domain()
    target = left.codomain()
    if _uses_free_construction_homset(source):
        return free_construction_homset(source, target)(
            lambda label: left(right(source.algebra_generator(label)))
        )

    from dzack_research.preamble.categories.algebras.algebras import algebra_homset

    engine_source = engine_ring(source)
    engine_target = engine_ring(target)
    composite = SetMorphism(
        engine_source.Hom(engine_target),
        lambda element: engine_target(left(right(engine_source(element)))),
    )
    return algebra_homset(source, target)(composite)


class SparseFreeAlgebraMorphism(Morphism):
    def __init__(self, parent, images) -> None:
        Morphism.__init__(self, parent)
        domain = cast(SparseFreeAlgebra, self.domain())
        labels = domain.algebra_generating_set()
        if isinstance(images, dict):
            if labels.cardinality() not in SageZZ:
                raise TypeError(
                    "an infinite generator assignment is specified by a callable"
                )
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(f"algebra-generator assignment omits {missing}")
            self._raw_image = images.__getitem__
        elif callable(images):
            self._raw_image = images
        else:
            raise TypeError(
                "an algebra morphism is specified on its algebra generators"
            )
        self._component_maps: dict[Any, Any] = {}

    def _component_map(self, key):
        cached = self._component_maps.get(key)
        if cached is not None:
            return cached
        source = self.domain().free_source_module()
        component = source.module_component(key)
        images = {
            component_label: self._raw_image(
                source.module_label_from_component(key, component_label)
            )
            for component_label in component.module_generating_set()
        }
        certified = module_homset(component, self.codomain())(images)
        self._component_maps[key] = certified
        return certified

    def _image(self, label):
        source = self.domain().free_source_module()
        if not self.domain()._source_has_component_protocol():
            return self._raw_image(label)
        key = source.module_component_key(label)
        component_label = source.module_component_generator_label(label)
        component = source.module_component(key)
        return self._component_map(key)(component.module_generator(component_label))

    def _basis_image(self, basis_label):
        if self.domain().flavor() == "tensor":
            factors = (self._image(label) for label in basis_label)
        else:
            factors = (
                self._image(label)
                for label, exponent in basis_label
                for _ in range(int(exponent))
            )
        return _multiply_in_target(self.codomain(), factors)

    def _call_(self, element):
        element = self.domain()(element)
        return sum(
            (
                coefficient * self._basis_image(label)
                for label, coefficient in element.monomial_coefficients().items()
            ),
            self.codomain().zero(),
        )

    def __call__(self, element):
        return self._call_(element)

    def __mul__(self, other):
        return compose_with_free_construction(self, other)


class SparseFreeAlgebraHomset(CategoricalHomset):
    Element = SparseFreeAlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        if not isinstance(domain, SparseFreeAlgebra):
            raise TypeError("the sparse free-algebra Hom has a sparse free domain")
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
            homset_category=Sets(),
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism Hom-set")
        return self(lambda label: self.domain().algebra_generator(label))


def sparse_free_algebra_homset(domain, codomain):
    from dzack_research.preamble.categories.algebras.algebras import algebra_homset

    return algebra_homset(domain, codomain)


class FramedFreeAlgebraMorphism(Morphism):
    r"""A generator-defined map from an engine-backed free algebra to any algebra."""

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
        try:
            source_module = domain.free_source_module()
        except (AttributeError, ValueError):
            source_module = None
        if source_module is not None:
            module_homset(source_module, self.codomain())(self._images.__getitem__)

    def _tensor_terms(self, element):
        domain = self.domain()
        presented = (
            domain.lift_to_presentation(element)
            if hasattr(domain, "lift_to_presentation")
            else engine_ring(domain)(element)
        )
        engine = presented.parent()
        labels = tuple(domain.algebra_generating_set())
        generator_labels = dict(zip(engine.monoid().gens(), labels, strict=True))
        for monomial, coefficient in presented.monomial_coefficients().items():
            word = tuple(
                generator_labels[generator]
                for generator, exponent in monomial
                for _ in range(int(exponent))
            )
            yield word, coefficient

    def _symmetric_terms(self, element):
        domain = self.domain()
        presented = (
            domain.lift_to_presentation(element)
            if hasattr(domain, "lift_to_presentation")
            else engine_ring(domain)(element)
        )
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
            yield factors, coefficient

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

    def __mul__(self, other):
        return compose_with_free_construction(self, other)


class FramedFreeAlgebraHomset(CategoricalHomset):
    Element = FramedFreeAlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
            homset_category=Sets(),
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism Hom-set")
        return self(lambda label: self.domain().algebra_generator(label))


def free_construction_homset(domain, codomain):
    from dzack_research.preamble.categories.algebras.algebras import algebra_homset

    return algebra_homset(domain, codomain)


_SPARSE_FREE_ALGEBRA_CACHE: dict[tuple[int, str], SparseFreeAlgebra] = {}


def SparseTensorAlgebraOf(module):
    return _sparse_free_algebra_of(module, "tensor")


def SparseSymmetricAlgebraOf(module):
    return _sparse_free_algebra_of(module, "symmetric")


def _sparse_free_algebra_of(module, flavor):
    key = (id(module), flavor)
    cached = _SPARSE_FREE_ALGEBRA_CACHE.get(key)
    if cached is not None and cached.free_source_module() is module:
        return cached
    component_protocol = all(
        hasattr(module, name)
        for name in (
            "module_component_key",
            "module_component",
            "module_component_generator_label",
            "module_label_from_component",
        )
    )
    if not component_protocol:
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FramedFreeModules,
        )

        if module not in FramedFreeModules(module.base_ring()):
            raise NotImplementedError(
                "an infinite relationful source requires finite presented module components"
            )
    algebra = SparseFreeAlgebra(module, flavor)
    _SPARSE_FREE_ALGEBRA_CACHE[key] = algebra
    return algebra


__all__ = [
    "SparseFreeAlgebra",
    "SparseFreeAlgebraDegreeElement",
    "SparseFreeAlgebraDegreeModule",
    "SparseFreeAlgebraElement",
    "SparseFreeAlgebraHomset",
    "SparseFreeAlgebraMorphism",
    "SparseSymmetricAlgebraOf",
    "SparseTensorAlgebraOf",
    "compose_with_free_construction",
    "free_construction_homset",
    "sparse_free_algebra_homset",
]
