r"""Sparse tensor and symmetric algebras on infinitely framed free modules."""

from typing import Any, cast

from sage.categories.category import Category
from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_function
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.constructions import TensorProduct
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
)
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    CommutativeAlgebras,
    FramedAlgebras,
    _AlgebraHomsetCommonMethods,
    algebra_homset,
)
from dzack_research.preamble.categories.algebras.finitely_presented_algebras import _canonical_smith_representative
from dzack_research.preamble.categories.algebras.free_algebras import (
    GradedFreeAlgebras,
    SymmetricAlgebras,
    TensorAlgebras,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import _SelectedFinitePresentationModules
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FramedFreeModules,
    ring_as_module,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.powers import SymmetricPower
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring as _engine_ring,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _owned_ring,
    ring_morphism,
)
from dzack_research.preamble.categories.sets.fixed_size_selections import multisets_of_size
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    NN,
    CartesianProductOfFamily,
    CoproductOfFamily,
)
from dzack_research.preamble.categories.sets.set_categories import (
    Sets as OwnedSets,
)


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
        self._coefficients = {label: coefficient for label, coefficient in normalized.items() if coefficient}

    def monomial_coefficients(self):
        return dict(self._coefficients)

    def _add_(self, other):
        result = self.monomial_coefficients()
        for label, coefficient in other._coefficients.items():
            result[label] = result.get(label, self.parent().base_ring().zero()) + coefficient
        return self.parent()._from_dict(result)

    def _neg_(self):
        return self.parent()._from_dict({label: -coefficient for label, coefficient in self._coefficients.items()})

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def __rmul__(self, scalar):
        # Bridge Python's concrete Element numeric slot to the module scalar
        # action owned by the parent/category.
        return self.parent().scalar_multiple(scalar, self)

    def _mul_(self, other):
        return self.parent().multiply(self, other)

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = isinstance(other, SparseFreeAlgebraElement) and other.parent() is self.parent() and other._coefficients == self._coefficients
        return equal if op == op_EQ else not equal

    def _repr_(self):
        if not self._coefficients:
            return "0"
        return " + ".join(f"{coefficient}*{label}" for label, coefficient in self._coefficients.items())


class SparseFreeAlgebraDegreeElement(ModuleElement):
    r"""An element of one homogeneous piece of a sparse free algebra."""

    def __init__(self, parent, algebra_element) -> None:
        ModuleElement.__init__(self, parent)
        algebra_element = parent.algebra()(algebra_element)
        if any(int(label.summand_index()) != parent.degree() for label in algebra_element.monomial_coefficients()):
            raise ValueError("the sparse algebra element has another homogeneous degree")
        self._algebra_element = algebra_element

    def algebra_element(self):
        return self._algebra_element

    def monomial_coefficients(self):
        return {label.summand_element(): coefficient for label, coefficient in self.algebra_element().monomial_coefficients().items()}

    def _add_(self, other):
        return self.parent().from_algebra_element(self.algebra_element() + other.algebra_element())

    def _neg_(self):
        return self.parent().from_algebra_element(-self.algebra_element())

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def __rmul__(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = isinstance(other, SparseFreeAlgebraDegreeElement) and other.parent() is self.parent() and other.algebra_element() == self.algebra_element()
        return equal if op == op_EQ else not equal

    def _repr_(self):
        return repr(self.algebra_element())


class SparseFreeAlgebraDegreeModule(Parent):
    r"""One exact homogeneous module of a sparse free algebra."""

    Element = SparseFreeAlgebraDegreeElement

    def __init__(self, algebra, degree) -> None:
        self._algebra = algebra
        self._degree = int(degree)
        self._basis = algebra.degree_basis(self._degree)
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
        label = self.module_generating_set()(label)
        algebra_label = self.algebra().basis_label(self.degree(), label)
        return self.from_algebra_element(self.algebra()._from_dict({algebra_label: self.base_ring().one()}))

    def linear_combination(self, coefficients):
        return self.from_algebra_element(
            self.algebra()._from_dict(
                {self.algebra().basis_label(self.degree(), self.module_generating_set()(label)): coefficient for label, coefficient in coefficients.items()}
            )
        )

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
        return self.from_algebra_element(self.algebra().scalar_multiple(scalar, element.algebra_element()))

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
        self._base_ring = _owned_ring(module.base_ring())
        self._basis = None
        self._degree_basis_cache: dict[int, Any] = {}
        self._component_cache: dict[Any, Any] = {}
        self._graded_piece_cache: dict[int, SparseFreeAlgebraDegreeModule] = {}
        flavor_category = TensorAlgebras(self._base_ring) if flavor == "tensor" else SymmetricAlgebras(self._base_ring)
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

    def is_commutative(self) -> bool:
        r"""The symmetric algebra commutes; the tensor algebra only on at most one generator."""
        if self._flavor == "symmetric":
            return True
        generators = self.algebra_generating_set().cardinality()
        return generators.is_finite() and int(generators.finite_value()) <= 1

    def base_ring(self):
        return self._base_ring

    algebra_base_ring = base_ring

    def algebra_homset(self, hom_family, codomain):
        return SparseFreeAlgebraHomset(hom_family, self, codomain)

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

    def degree_basis(self, degree):
        degree = int(degree)
        if degree < 0:
            raise ValueError("a graded degree is nonnegative")
        cached = self._degree_basis_cache.get(degree)
        if cached is not None:
            return cached
        if self.flavor() == "tensor":
            indices = OwnedSets.Δ[degree - 1]
            basis = CartesianProductOfFamily(
                indices,
                lambda _position: self.algebra_generating_set(),
            )
        else:
            basis = multisets_of_size(self.algebra_generating_set(), degree)
        self._degree_basis_cache[degree] = basis
        return basis

    def basis_label(self, degree, degree_label):
        degree = int(degree)
        return self.module_generating_set()(degree, self.degree_basis(degree)(degree_label))

    def _generator_basis_label(self, label):
        labels = self.algebra_generating_set()
        if label not in labels:
            raise ValueError(f"{label!r} is not an algebra-generator label")
        label = labels(label)
        degree_basis = self.degree_basis(1)
        if self.flavor() == "tensor":
            inner = degree_basis(lambda _position: label)
        else:
            inner = degree_basis.from_multiplicities({label: 1})
        return self.basis_label(1, inner)

    def algebra_generator(self, label):
        return self._from_dict({self._generator_basis_label(label): self.base_ring().one()})

    def module_generating_set(self):
        if self._basis is None:
            self._basis = CoproductOfFamily(
                NN,
                lambda degree: self.degree_basis(int(degree)),
            )
        return self._basis

    def module_generator(self, label):
        label = self.module_generating_set()(label)
        return self._from_dict({label: self.base_ring().one()})

    def graded_piece(self, degree):
        degree = int(degree)
        if degree < 0:
            raise ValueError("a graded degree is nonnegative")
        if degree == 0:
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
        basis_label = self.module_generating_set()(basis_label)
        inner = basis_label.summand_element()
        if self.flavor() == "tensor":
            return tuple(source.module_component_key(inner.component(position)) for position in inner.parent().index_set())
        multiplicities = {}
        for label in inner.support():
            key = source.module_component_key(label)
            multiplicities[key] = multiplicities.get(key, 0) + inner.multiplicity(label)
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
            factors = tuple(SymmetricPower(source.module_component(source_key), multiplicity) for source_key, multiplicity in self._component_items(key))

        if not factors:
            component = ring_as_module(self.base_ring())
        else:
            component = factors[0]
            if len(factors) > 1:
                for factor in factors[1:]:
                    component = TensorProduct(component, factor)
        self._component_cache[key] = component
        return component

    def _component_generator_label(self, basis_label):
        source = self.free_source_module()
        basis_label = self.module_generating_set()(basis_label)
        inner = basis_label.summand_element()
        if self.flavor() == "tensor":
            return _nested_label(source.module_component_generator_label(inner.component(position)) for position in inner.parent().index_set())

        grouped = {}
        for source_label in inner.support():
            exponent = inner.multiplicity(source_label)
            key = source.module_component_key(source_label)
            component_label = source.module_component_generator_label(source_label)
            counts = grouped.setdefault(key, {})
            counts[component_label] = counts.get(component_label, 0) + int(exponent)

        factor_labels = []
        for key, multiplicity in self._component_items(self._monomial_component_key(basis_label)):
            counts = grouped[key]
            source_component = source.module_component(key)
            if multiplicity == 1:
                factor_labels.append(next(iter(counts)))
            else:
                factor = SymmetricPower(source_component, multiplicity)
                factor_labels.append(factor.module_generating_set().from_multiplicities(counts))
        return _nested_label(factor_labels)

    def _basis_label_from_component(self, key, component_label):
        source = self.free_source_module()
        if self.flavor() == "tensor":
            component_labels = _flatten_nested_label(component_label, len(key))
            degree = len(key)
            inner = self.degree_basis(degree)(
                lambda position: source.module_label_from_component(
                    key[int(position)],
                    component_labels[int(position)],
                )
            )
            return self.basis_label(degree, inner)

        items = self._component_items(key)
        factor_labels = _flatten_nested_label(component_label, len(items))
        counts = {}
        for (source_key, multiplicity), factor_label in zip(items, factor_labels, strict=True):
            source_component = source.module_component(source_key)
            if multiplicity == 1:
                labelled_factors = ((factor_label, 1),)
            elif hasattr(factor_label, "support"):
                labelled_factors = ((label, factor_label.multiplicity(label)) for label in factor_label.support())
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
                source_label = source.module_label_from_component(source_key, source_component_label)
                counts[source_label] = counts.get(source_label, 0) + exponent
        degree = sum(counts.values())
        inner = self.degree_basis(degree).from_multiplicities(counts)
        return self.basis_label(degree, inner)

    def _normalize_component_relations(self, coefficients):
        grouped = {}
        ring = self.base_ring()
        for basis_label, coefficient in coefficients.items():
            basis_label = self.module_generating_set()._element_constructor_(basis_label)
            coefficient = ring(coefficient)
            if not coefficient:
                continue
            key = self._monomial_component_key(basis_label)
            component_label = self._component_generator_label(basis_label)
            component_coefficients = grouped.setdefault(key, {})
            component_coefficients[component_label] = component_coefficients.get(component_label, ring.zero()) + coefficient

        normalized = {}
        for key, component_coefficients in grouped.items():
            component = self._component_module(key)
            element = component.linear_combination(component_coefficients)

            if component in _SelectedFinitePresentationModules(self.base_ring()):
                element = _canonical_smith_representative(component, element)
            for component_label, coefficient in module_coefficients(element, component).items():
                basis_label = self._basis_label_from_component(key, component_label)
                normalized[basis_label] = normalized.get(basis_label, ring.zero()) + ring(coefficient)
        return {label: coefficient for label, coefficient in normalized.items() if coefficient}

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

        return ring_as_module(self.base_ring())

    def module_component_generator_label(self, label):
        label = self.module_generating_set()._element_constructor_(label)
        if self._source_has_component_protocol():
            return self._component_generator_label(label)
        return 0

    def module_label_from_component(self, key, component_label):
        if self._source_has_component_protocol():
            return self.module_generating_set()._element_constructor_(self._basis_label_from_component(key, component_label))
        if component_label != 0:
            raise ValueError("a rank-one free component has generator label 0")
        return self.module_generating_set()._element_constructor_(key)

    def __call__(self, value):
        r"""Construct an element through the owned sparse-algebra parser."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        if isinstance(value, SparseFreeAlgebraElement):
            if value.parent() is self:
                return value
            raise TypeError("the element belongs to a different sparse free algebra")
        if value in self.free_source_module():
            result = self.zero()
            for label, coefficient in module_coefficients(value, self.free_source_module()).items():
                result += coefficient * self.algebra_generator(label)
            return result
        try:
            scalar = self.base_ring()(value)
        except TypeError, ValueError:
            if isinstance(value, dict):
                return self._from_dict(value)
            raise TypeError(f"{value!r} does not define an element of {self}") from None
        return self._from_dict({self._unit_label(): scalar})

    def _unit_label(self):
        basis = self.degree_basis(0)
        inner = basis(lambda _position: None) if self.flavor() == "tensor" else basis.from_multiplicities({})
        return self.basis_label(0, inner)

    def zero(self):
        return self._from_dict({})

    def one(self):
        return self._from_dict({self._unit_label(): self.base_ring().one()})

    def scalar_multiple(self, scalar, element):
        element = self(element)
        scalar = self.base_ring()(scalar)
        return self._from_dict({label: scalar * coefficient for label, coefficient in element.monomial_coefficients().items()})

    def _multiply_labels(self, left, right):
        left = self.module_generating_set()(left)
        right = self.module_generating_set()(right)
        left_degree = int(left.summand_index())
        right_degree = int(right.summand_index())
        degree = left_degree + right_degree
        left_inner = left.summand_element()
        right_inner = right.summand_element()
        target = self.degree_basis(degree)
        if self.flavor() == "tensor":
            inner = target(lambda position: left_inner.component(int(position)) if int(position) < left_degree else right_inner.component(int(position) - left_degree))
        else:
            counts = {}
            for monomial in (left_inner, right_inner):
                for label in monomial.support():
                    counts[label] = counts.get(label, 0) + monomial.multiplicity(label)
            inner = target.from_multiplicities(counts)
        return self.basis_label(degree, inner)

    def multiply(self, left, right):
        left = self(left)
        right = self(right)
        result = {}
        for left_label, left_coefficient in left.monomial_coefficients().items():
            for right_label, right_coefficient in right.monomial_coefficients().items():
                label = self._multiply_labels(left_label, right_label)
                result[label] = result.get(label, self.base_ring().zero()) + left_coefficient * right_coefficient
        return self._from_dict(result)

    def _ring_morphism_defining_algebra_structure(self):
        return ring_morphism(
            self.base_ring(),
            self,
            lambda scalar: self(scalar),
        )

    algebra_structure_morphism = _ring_morphism_defining_algebra_structure

    def ring_center(self):
        if self.flavor() == "symmetric":
            return self
        raise NotImplementedError("the center of this tensor algebra is not selected")

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
        return free_construction_homset(source, target)(lambda label: left(right(source.algebra_generator(label))))

    engine_source = _engine_ring(source)
    engine_target = _engine_ring(target)
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
        if isinstance(images, IndexedFamily):
            source_indices = images.index_set()
            self._generator_images = indexed_family(
                labels,
                lambda label: self.codomain()(images[source_indices(label)]),
                name="Sparse free-algebra morphism generator-image family",
            )
        elif isinstance(images, dict):
            if not labels.cardinality().is_finite():
                raise TypeError("an infinite generator assignment is specified by a callable or indexed family")
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(f"algebra-generator assignment omits {missing}")
            self._generator_images = indexed_family(
                labels,
                lambda label: self.codomain()(images[label]),
                name="Sparse free-algebra morphism generator-image family",
            )
        elif callable(images):
            self._generator_images = indexed_family(
                labels,
                lambda label: self.codomain()(images(label)),
                name="Sparse free-algebra morphism generator-image family",
            )
        else:
            raise TypeError("an algebra morphism is specified on its algebra generators")
        self._raw_image = self._generator_images.value
        self._component_maps: dict[Any, Any] = {}

    def algebra_generator_images(self):
        return self._generator_images

    def algebra_generator_morphism(self):
        return SetMorphism(
            OwnedSets().Mor(self.domain().algebra_generating_set(), self.codomain()),
            self._generator_images.value,
        )

    def _component_map(self, key):
        cached = self._component_maps.get(key)
        if cached is not None:
            return cached
        source = self.domain().free_source_module()
        component = source.module_component(key)
        images = {component_label: self._raw_image(source.module_label_from_component(key, component_label)) for component_label in component.module_generating_set()}
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
        basis_label = self.domain().module_generating_set()(basis_label)
        inner = basis_label.summand_element()
        if self.domain().flavor() == "tensor":
            factors = (self._image(inner.component(position)) for position in inner.parent().index_set())
        else:
            factors = (self._image(label) for label in inner.support() for _ in range(int(inner.multiplicity(label))))
        return _multiply_in_target(self.codomain(), factors)

    def _call_(self, element):
        element = self.domain()(element)
        return sum(
            (coefficient * self._basis_image(label) for label, coefficient in element.monomial_coefficients().items()),
            self.codomain().zero(),
        )

    def __call__(self, element):
        return self._call_(element)

    def __mul__(self, other):
        return compose_with_free_construction(self, other)

    def _postcompose_algebra_morphism(self, morphism):
        r"""Return ``morphism ∘ self`` through the free-construction Hom."""
        return compose_with_free_construction(morphism, self)


class SparseFreeAlgebraHomset(_AlgebraHomsetCommonMethods, CategoricalHomset):
    Element = SparseFreeAlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        if not isinstance(domain, SparseFreeAlgebra):
            raise TypeError("the sparse free-algebra Hom has a sparse free domain")
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


def sparse_free_algebra_homset(domain, codomain):

    return algebra_homset(domain, codomain)


def free_construction_homset(domain, codomain):

    return algebra_homset(domain, codomain)


def SparseTensorAlgebraOf(module):
    return _sparse_free_algebra_of(module, "tensor")


def SparseSymmetricAlgebraOf(module):
    return _sparse_free_algebra_of(module, "symmetric")


@cached_function(key=lambda module, flavor: (id(module), flavor))
def _sparse_free_algebra_of(module, flavor):
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
        if module not in FramedFreeModules(module.base_ring()):
            raise NotImplementedError("an infinite relationful source requires finite presented module components")
    algebra = SparseFreeAlgebra(module, flavor)
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
