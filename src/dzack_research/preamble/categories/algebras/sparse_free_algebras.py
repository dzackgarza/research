r"""Tensor and symmetric products on the module of relationful words."""

from math import prod
from typing import Any

from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.structure.element import parent as element_parent

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.mor_categories import CategoricalMor
from dzack_research.preamble.categories.algebras.algebras import Algebras, _AlgebraMorCommonMethods, _algebra_on_module
from dzack_research.preamble.categories.algebras.free_algebras import FreeAlgebras, GradedFreeAlgebras, TensorAlgebras, SymmetricAlgebras
from dzack_research.preamble.categories.modules.general_modules import GeneralModules
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules, ModulesWithChosenComponentPresentation,
)
from dzack_research.preamble.categories.modules.word_modules import (
    _WordModule, _WordModuleElement, _module_on_word_quotient, _has_component_presentation,
)
from dzack_research.preamble.categories.rings.ring_foundation import OwnedRings
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets as OwnedSets


class _SparseFreeAlgebra(_WordModule):
    r"""The word-module realization with algebra ingress and word maps.

    The root owns the product.  The actual module quotient, homogeneous
    pieces, framing and arithmetic are inherited from its module realization.
    """

    def __init__(self, word_presentation, **rest) -> None:
        source = word_presentation.source_module()
        match source in FramedFreeModules(source.base_ring()):
            case True:
                # This realization is the free algebra on the selected module
                # basis, so its selected free-algebra framing is the identity.
                rest["algebra_framing_source"] = self
            case False:
                pass
        super().__init__(word_presentation, **rest)

    def flavor(self):
        return self.word_flavor()

    def _source_has_component_protocol(self):
        return _has_component_presentation(self.generating_module())

    def _algebra_mor_class(self):
        return SparseFreeAlgebraMor

    def algebra_mor(self, mor_family, codomain):
        return SparseFreeAlgebraMor(mor_family, self, codomain)

    def _element_constructor_(self, value):
        source = element_parent(value)
        match value:
            case _ if source is self:
                return value
            case _ if source is self.generating_module():
                return self.from_component(1, value)
            case dict():
                return super()._element_constructor_(value)
            case _ if source in Modules(self.base_ring()) and self._built_on_the_same_data(source):
                return self._element_on_the_same_data(source, value)
            case _ if value in self.base_ring():
                return self.scalar_multiple(self.base_ring()(value), self.one())
            case _:
                return super()._element_constructor_(value)

    def _realize_graded_piece_basis_label(self, degree, label):
        return self.from_component(degree, self.graded_piece(degree).module_generator(label))

    def is_commutative(self):
        size = self.algebra_generating_set().cardinality()
        match self.flavor():
            case "symmetric":
                return True
            case _ if size.is_finite() and int(size.finite_value()) <= 1:
                return True
            case _ if self.generating_module() in FramedFreeModules(self.base_ring()) and (self.base_ring().one() != self.base_ring().zero()) is True:
                return False
            case _:
                return Unknown

    def is_central(self, element):
        element = self(element)
        if all(
            int(label.summand_index()) == 0
            for label in self._framing_lift(self(element)).support().domain()
        ):
            return True
        if self.is_commutative() is True:
            return True
        labels = self.algebra_generating_set()
        if not labels.cardinality().is_finite():
            return Unknown
        decisions = tuple(element * self.algebra_generator(label) == self.algebra_generator(label) * element for label in labels)
        match (all(value is True for value in decisions), any(value is False for value in decisions)):
            case (True, _):
                return True
            case (_, True):
                return False
            case _:
                return Unknown

    @cached_method
    def ring_center(self):
        if self.is_commutative() is True:
            return self
        return self.predicate_subring(self.is_central, "commutes with all algebra generators", OwnedRings().Commutative())

    def _repr_(self):
        name = "T" if self.flavor() == "tensor" else "Sym"
        return f"{name}({self.generating_module()})"


def _word_product(module, left, right):
    r"""Concatenate words, or add multiset exponents, in the module quotient."""
    def product_label(left_label, right_label):
        s, t = int(left_label.summand_index()), int(right_label.summand_index())
        left_word, right_word = left_label.summand_element(), right_label.summand_element()
        labels = module.degree_basis(s + t)
        match module.word_flavor():
            case "tensor":
                word = labels(lambda i: left_word.component(int(i)) if int(i) < s else right_word.component(int(i) - s))
            case "symmetric":
                support = set(left_word.support()) | set(right_word.support())
                word = labels.from_multiplicities({label: left_word.multiplicity(label) + right_word.multiplicity(label) for label in support})
        return module.basis_label(s + t, word)

    left_coordinates = module.framing_morphism().lift(left)
    right_coordinates = module.framing_morphism().lift(right)
    return sum((
        module.scalar_multiple(left_coordinates(x) * right_coordinates(y), module.module_generator(product_label(x, y)))
        for x in left_coordinates.support().domain()
        for y in right_coordinates.support().domain()
    ), module.zero())


def _uses_free_construction_mor(domain):
    ring = domain.base_ring()
    return domain in TensorAlgebras(ring) or domain in SymmetricAlgebras(ring)


def _compose_with_free_construction(left, right):
    r"""Compose through a sparse/free map without assuming a free source."""
    if right.codomain() is not left.domain():
        return NotImplemented
    source = right.domain()
    target = left.codomain()
    if _uses_free_construction_mor(source):
        return source.Mor(target)(lambda label: left(right(source.algebra_generator(label))))

    underlying = Algebras(source.base_ring()).underlying_module()
    linear = underlying(left) * underlying(right)
    return Algebras(source.base_ring()).Associative().Unital().Mor(source, target)(linear)


class SparseFreeAlgebraMorphism(Morphism):
    def __init__(self, parent, images) -> None:
        Morphism.__init__(self, parent)
        domain = self.domain()
        labels = domain.algebra_generating_set()
        if isinstance(images, IndexedFamily):
            source_indices = images.index_set()
            self._generator_images = indexed_family(
                labels,
                lambda label: self.codomain()(images[source_indices(label)]),
                name="Generator images",
            )
        elif isinstance(images, dict):
            if not labels.cardinality().is_finite():
                raise TypeError(
                    f"a dictionary of generator images needs finitely many algebra generators of {domain}, but it "
                    f"has {labels.cardinality()}; give a function or an indexed family"
                )
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(
                    f"the images of the algebra generators of {domain} must be given for every generator, but "
                    f"{missing} are missing"
                )
            self._generator_images = indexed_family(
                labels,
                lambda label: self.codomain()(images[label]),
                name="Generator images",
            )
        elif callable(images):
            self._generator_images = indexed_family(
                labels,
                lambda label: self.codomain()(images(label)),
                name="Generator images",
            )
        else:
            raise TypeError(
                f"a morphism out of {domain} is given by the images of its algebra generators, but got {images!r}"
            )
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
        source = self.domain().generating_module()
        component = source.module_component(key)
        images = {component_label: self._raw_image(source.module_label_from_component(key, component_label)) for component_label in component.module_generating_set()}
        certified = component.module_category().Mor(component, self.codomain())(images)
        self._component_maps[key] = certified
        return certified

    def _image(self, label):
        source = self.domain().generating_module()
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
        return prod(factors, start=self.codomain().one())

    def _call_(self, element):
        coordinates = self.domain().framing_morphism().lift(element)
        return sum(
            (coordinates(label) * self._basis_image(label) for label in coordinates.support().domain()),
            self.codomain().zero(),
        )

    def __call__(self, element):
        return self._call_(element)

    def __mul__(self, other):
        return _compose_with_free_construction(self, other)

    def _postcompose_algebra_morphism(self, morphism):
        r"""Return ``morphism ∘ self`` through the free-construction Mor."""
        return _compose_with_free_construction(morphism, self)


class SparseFreeAlgebraMor(_AlgebraMorCommonMethods, CategoricalMor):
    Element = SparseFreeAlgebraMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        assert domain in TensorAlgebras(domain.base_ring()) or domain in SymmetricAlgebras(domain.base_ring()), (
            f"a morphism given on words needs a tensor algebra or a symmetric algebra as domain, but "
            f"{domain} is neither"
        )
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
            raise ValueError(
                f"the identity morphism exists only on Mor(A, A), but this is Mor({self.domain()}, {self.codomain()})"
            )
        return self(lambda label: self.domain().algebra_generator(label))



def SparseFreeAlgebra(module, flavor):
    return _sparse_free_algebra_of(module, flavor)


def SparseFreeAlgebraElement(parent, coefficients):
    return parent.linear_combination(coefficients)


def SparseFreeAlgebraDegreeModule(algebra, degree):
    return algebra.graded_piece(degree)


def SparseFreeAlgebraDegreeElement(parent, algebra_element):
    return parent(algebra_element.homogeneous_component(parent.degree()))


def _sparse_tensor_algebra_of(module):
    return _sparse_free_algebra_of(module, "tensor")


def _sparse_symmetric_algebra_of(module):
    return _sparse_free_algebra_of(module, "symmetric")


@cached_function(key=lambda source, flavor: (id(source), flavor))
def _sparse_free_algebra_of(source, flavor):
    r"""Construct the module quotient, its tensor multiplication, then the algebra."""
    ring = source.base_ring()
    module = _module_on_word_quotient(source, flavor)
    tensor = Modules(ring).tensor_product((module, module))
    multiplication = tensor.from_bilinear_map(module, lambda x, y: _word_product(module, x, y))
    flavor_category = TensorAlgebras(ring) if flavor == "tensor" else SymmetricAlgebras(ring)
    categories = (flavor_category,)
    match source.module_generating_set().cardinality().is_finite():
        case True:
            categories = (
                *categories,
                Algebras(ring)
                .Associative()
                .Unital()
                .FinitelyGeneratedAsAlgebra(),
            )
        case False:
            pass
    if source in FramedFreeModules(ring):
        categories = (*categories, FreeAlgebras(ring), GradedFreeAlgebras(ring))
    realization_owner = Cat().meet((
        GeneralModules(ring), GradedModules(ring),
        ModulesWithChosenComponentPresentation(ring), Algebras(ring), *categories,
    ))
    unit_piece = module.graded_piece(0)
    law_decisions = {"associativity": True, "unit": True, "grading": True}
    match flavor:
        case "symmetric":
            law_decisions["commutativity"] = True
        case "tensor":
            pass
    algebra_generating_family = indexed_family(
        source.module_generating_set(),
        lambda label: module.from_component(1, source.module_generator(label)),
    )
    return _algebra_on_module(
        module, multiplication, placement=categories,
        unit=module.from_component(0, unit_piece.module_generator(0)),
        construction_data={
            "_engine": (realization_owner, _SparseFreeAlgebra, _WordModuleElement),
            "algebra_generating_family": algebra_generating_family,
        },
        law_decisions=law_decisions,
    )


__all__ = [
    "SparseFreeAlgebra", "SparseFreeAlgebraDegreeElement", "SparseFreeAlgebraDegreeModule",
    "SparseFreeAlgebraElement", "SparseFreeAlgebraMor", "SparseFreeAlgebraMorphism",
]
