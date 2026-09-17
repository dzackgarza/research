r"""Categorical tensor products and bilinear maps of represented modules."""

from dzack_research.preamble.categories.modules.pure.modules import Modules, _tensor_pair
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets


def _nested_tensor_label(module, word):
    r"""Return the label of the iterated left-associated tensor word."""
    iterator = iter(word)
    try:
        first = next(iterator)
    except StopIteration:
        return 0
    current_module = module
    current_label = first
    modules = Modules(module.base_ring())
    for next_label in iterator:

        current_module = modules.tensor_product((current_module, module))
        current_label = _tensor_pair(
            current_module.module_generating_set(),
            current_label,
            next_label,
        )
    return current_label


def _flatten_tensor_label(label, degree):
    r"""Return the indexed family of factors of a left-associated tensor label."""

    degree = int(degree)
    indices = Sets.Δ[degree - 1]

    def factor(position):
        position = int(position)
        current = label
        current_degree = degree
        while current_degree > 1:
            left = current.component(0)
            right = current.component(1)
            if position == current_degree - 1:
                return right
            current = left
            current_degree -= 1
        if position == 0:
            return current
        raise IndexError(position)

    return indexed_family(indices, factor, name="Tensor-factor word")



def _tensor_product_morphism(left_morphism, right_morphism, source=None, target=None):
    r"""Return ``f tensor g`` on the chosen tensor products."""
    if left_morphism.domain().base_ring() != right_morphism.domain().base_ring():
        raise ValueError("tensoring morphisms requires one common base ring")
    if source is None:
        source = Modules(left_morphism.domain().base_ring()).tensor_product(
            (left_morphism.domain(), right_morphism.domain())
        )
    if target is None:
        target = Modules(left_morphism.codomain().base_ring()).tensor_product(
            (left_morphism.codomain(), right_morphism.codomain())
        )
    if (
        source.tensor_factor(0) is not left_morphism.domain()
        or source.tensor_factor(1) is not right_morphism.domain()
    ):
        raise ValueError("the source tensor product has different factors")
    if (
        target.tensor_factor(0) is not left_morphism.codomain()
        or target.tensor_factor(1) is not right_morphism.codomain()
    ):
        raise ValueError("the target tensor product has different factors")


    return source.from_bilinear_map(
        target,
        lambda left, right: target.pure_tensor(left_morphism(left), right_morphism(right)),
    )



__all__ = [
    "_flatten_tensor_label",
    "_nested_tensor_label",
]
