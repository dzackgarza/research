r"""Categorical tensor products and bilinear maps of finitely presented modules."""

from itertools import product

from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    owned_ring_view,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.tensors import tensor
from dzack_research.preamble.refine import refine


def _nested_tensor_label(word):
    r"""Return the label of the iterated tensor of the factors in ``word``.

    Iterated tensor products are left-associated, so the label of
    ``a (x) b (x) c`` is ``((a, b), c)``.  The empty word labels the unit.
    """
    word = tuple(word)
    if not word:
        return 0
    label = word[0]
    for next_label in word[1:]:
        label = (label, next_label)
    return label


def _flatten_tensor_label(label, degree):
    r"""Return the ``degree`` factor labels of a left-associated tensor label."""
    if degree == 1:
        return (label,)
    left, right = label
    return _flatten_tensor_label(left, degree - 1) + (right,)


class BilinearMap(SageObject):
    r"""A bilinear map specified on selected module generators.

    The constructor checks the relations in each argument.  Thus this is not
    merely a callable tagged "bilinear": its generator assignment descends
    through both selected finite presentations.
    """

    def __init__(self, left, right, codomain, generator_images) -> None:
        if left.base_ring() != right.base_ring() or left.base_ring() != codomain.base_ring():
            raise ValueError("a bilinear map requires one common base ring")
        self._left = left
        self._right = right
        self._codomain = codomain
        left_labels = tuple(left.module_generating_set())
        right_labels = tuple(right.module_generating_set())
        pairs = tuple(product(left_labels, right_labels))
        missing = [pair for pair in pairs if pair not in generator_images]
        if missing:
            raise ValueError(f"bilinear generator assignment omits {missing}")
        self._generator_images = {
            pair: generator_images[pair]
            for pair in pairs
        }
        self._check_relations()

    def left_factor(self):
        return self._left

    def right_factor(self):
        return self._right

    def codomain(self):
        return self._codomain

    def generator_image(self, left_label, right_label):
        return self._generator_images[(left_label, right_label)]

    def _check_relations(self) -> None:
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            _presentation_matrix,
        )

        zero = self.codomain().zero()
        left_labels = tuple(self.left_factor().module_generating_set())
        right_labels = tuple(self.right_factor().module_generating_set())
        for row in _presentation_matrix(self.left_factor()).rows():
            for right_label in right_labels:
                value = sum(
                    (
                        coefficient * self.generator_image(left_label, right_label)
                        for left_label, coefficient in zip(left_labels, row, strict=True)
                        if coefficient
                    ),
                    zero,
                )
                if value != zero:
                    raise ValueError("the bilinear map does not kill a left-factor relation")
        for row in _presentation_matrix(self.right_factor()).rows():
            for left_label in left_labels:
                value = sum(
                    (
                        coefficient * self.generator_image(left_label, right_label)
                        for right_label, coefficient in zip(right_labels, row, strict=True)
                        if coefficient
                    ),
                    zero,
                )
                if value != zero:
                    raise ValueError("the bilinear map does not kill a right-factor relation")

    def __call__(self, left_element, right_element):
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_coefficients,
        )

        left_coefficients = module_coefficients(left_element, self.left_factor())
        right_coefficients = module_coefficients(right_element, self.right_factor())
        return sum(
            (
                left_coefficient
                * right_coefficient
                * self.generator_image(left_label, right_label)
                for left_label, left_coefficient in left_coefficients.items()
                for right_label, right_coefficient in right_coefficients.items()
            ),
            self.codomain().zero(),
        )


class TensorProductModules(OwnedCategoryOverBaseRing):
    r"""Chosen tensor products of finitely presented modules over one ring."""

    @classmethod
    def _repr_object_names(cls):
        return "tensor products of finitely presented modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            FinitelyPresentedModules,
        )

        return [FinitelyPresentedModules(self.base_ring())]

    class ParentMethods:
        def tensor_factors(self):
            return self._preamble_tensor_factors

        def tensor_factor(self, index):
            return self.tensor_factors()[index]

        def pure_tensor(self, left_element, right_element):
            r"""Return the image of ``(left_element, right_element)`` under \(\otimes\)."""
            left, right = self.tensor_factors()
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_coefficients,
            )

            left_coefficients = module_coefficients(left_element, left)
            right_coefficients = module_coefficients(right_element, right)
            return self.linear_combination(
                {
                    (left_label, right_label): left_coefficient * right_coefficient
                    for left_label, left_coefficient in left_coefficients.items()
                    for right_label, right_coefficient in right_coefficients.items()
                    if left_coefficient * right_coefficient
                }
            )

        def universal_bilinear_map(self):
            r"""Return the canonical bilinear map \(M\times N\to M\otimes_RN\)."""
            left, right = self.tensor_factors()
            return BilinearMap(
                left,
                right,
                self,
                {
                    (left_label, right_label): self.module_generator((left_label, right_label))
                    for left_label in left.module_generating_set()
                    for right_label in right.module_generating_set()
                },
            )

        def from_bilinear(self, bilinear):
            r"""Return the unique linear factorization of a bilinear map through this tensor product."""
            left, right = self.tensor_factors()
            if bilinear.left_factor() is not left or bilinear.right_factor() is not right:
                raise ValueError("the bilinear map has different tensor factors")
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            return module_homset(self, bilinear.codomain())(
                {
                    (left_label, right_label): bilinear.generator_image(left_label, right_label)
                    for left_label in left.module_generating_set()
                    for right_label in right.module_generating_set()
                }
            )


_MODULE_TENSOR_PRODUCT_CACHE = {}


def _module_tensor_product(left, right):
    r"""Return the categorical tensor product \(left\otimes_R right\).

    The exact backend uses the standard presentation
    ``(relations(left) tensor F_right) + (F_left tensor relations(right))``.
    The returned object owns its factors and universal bilinear map; the
    relation matrix is only the computation model for that quotient.
    """
    cache_key = (id(left), id(right))
    cached = _MODULE_TENSOR_PRODUCT_CACHE.get(cache_key)
    if cached is not None:
        cached_left, cached_right = cached.tensor_factors()
        if cached_left is left and cached_right is right:
            return cached

    ring = owned_ring_view(left.base_ring())
    if owned_ring_view(right.base_ring()) != ring:
        raise ValueError("a tensor product requires one common base ring")

    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
        _presentation_from_relation_rows,
        _presentation_matrix,
    )

    left_labels = tuple(left.module_generating_set())
    right_labels = tuple(right.module_generating_set())
    tensor_labels = finite_ordered_set(tuple(product(left_labels, right_labels)))
    positions = {
        pair: position
        for position, pair in enumerate(tensor_labels)
    }
    left_relations = _presentation_matrix(left).change_ring(engine_ring(ring))
    right_relations = _presentation_matrix(right).change_ring(engine_ring(ring))
    rows = []
    relation_labels = []

    for relation_index, relation in enumerate(left_relations.rows()):
        for right_label in right_labels:
            row = [engine_ring(ring).zero()] * len(tensor_labels)
            for left_label, coefficient in zip(left_labels, relation, strict=True):
                if coefficient:
                    row[positions[(left_label, right_label)]] = coefficient
            rows.append(row)
            relation_labels.append(("left relation", relation_index, right_label))

    for left_label in left_labels:
        for relation_index, relation in enumerate(right_relations.rows()):
            row = [engine_ring(ring).zero()] * len(tensor_labels)
            for right_label, coefficient in zip(right_labels, relation, strict=True):
                if coefficient:
                    row[positions[(left_label, right_label)]] = coefficient
            rows.append(row)
            relation_labels.append(("right relation", left_label, relation_index))

    relations = (
        tensor.matrix(engine_ring(ring), rows)
        if rows
        else tensor.matrix(engine_ring(ring), 0, len(tensor_labels))
    )
    presentation = _presentation_from_relation_rows(
        ring,
        tensor_labels,
        finite_ordered_set(relation_labels),
        relations,
    )
    result = FinitelyPresentedModule(presentation)
    result._preamble_tensor_factors = (left, right)
    result = refine(result, TensorProductModules(ring))
    _MODULE_TENSOR_PRODUCT_CACHE[cache_key] = result
    return result


def tensor_product_morphism(left_morphism, right_morphism, source=None, target=None):
    r"""Return \(f\otimes g\) on the chosen tensor products."""
    if left_morphism.domain().base_ring() != right_morphism.domain().base_ring():
        raise ValueError("tensoring morphisms requires one common base ring")
    if source is None:
        from dzack_research.preamble.categories.abstract_categories import TensorProduct

        source = TensorProduct(left_morphism.domain(), right_morphism.domain())
    if target is None:
        from dzack_research.preamble.categories.abstract_categories import TensorProduct

        target = TensorProduct(left_morphism.codomain(), right_morphism.codomain())
    if source.tensor_factors() != (left_morphism.domain(), right_morphism.domain()):
        raise ValueError("the source tensor product has different factors")
    if target.tensor_factors() != (left_morphism.codomain(), right_morphism.codomain()):
        raise ValueError("the target tensor product has different factors")

    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    left = left_morphism.domain()
    right = right_morphism.domain()
    return module_homset(source, target)(
        {
            (left_label, right_label): target.pure_tensor(
                left_morphism(left.module_generator(left_label)),
                right_morphism(right.module_generator(right_label)),
            )
            for left_label in left.module_generating_set()
            for right_label in right.module_generating_set()
        }
    )


__all__ = [
    "BilinearMap",
    "TensorProductModules",
    "_module_tensor_product",
    "tensor_product_morphism",
]
