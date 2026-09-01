r"""Finite biproducts of finitely presented modules."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    owned_ring_view,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.tensors import tensor
from dzack_research.preamble.refine import refine


class BiproductModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "chosen biproducts of finitely presented modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules import FinitelyPresentedModules

        return [FinitelyPresentedModules(self.base_ring())]

    class ParentMethods:
        def biproduct_factors(self):
            return self._preamble_biproduct_factors

        def left_inclusion(self):
            left, _right = self.biproduct_factors()
            from dzack_research.preamble.categories.modules import module_homset

            return module_homset(left, self)(
                {
                    label: self.module_generator(("left", label))
                    for label in left.module_generating_set()
                }
            )

        def right_inclusion(self):
            _left, right = self.biproduct_factors()
            from dzack_research.preamble.categories.modules import module_homset

            return module_homset(right, self)(
                {
                    label: self.module_generator(("right", label))
                    for label in right.module_generating_set()
                }
            )

        def left_projection(self):
            left, right = self.biproduct_factors()
            from dzack_research.preamble.categories.modules import module_homset

            return module_homset(self, left)(
                {
                    **{
                        ("left", label): left.module_generator(label)
                        for label in left.module_generating_set()
                    },
                    **{
                        ("right", label): left.zero()
                        for label in right.module_generating_set()
                    },
                }
            )

        def right_projection(self):
            left, right = self.biproduct_factors()
            from dzack_research.preamble.categories.modules import module_homset

            return module_homset(self, right)(
                {
                    **{
                        ("left", label): right.zero()
                        for label in left.module_generating_set()
                    },
                    **{
                        ("right", label): right.module_generator(label)
                        for label in right.module_generating_set()
                    },
                }
            )

        def from_summands(self, left_map, right_map):
            r"""Return the unique map ``self -> X`` extending maps from both summands."""
            if left_map.domain() is not self.biproduct_factors()[0]:
                raise ValueError("the left map has the wrong source")
            if right_map.domain() is not self.biproduct_factors()[1]:
                raise ValueError("the right map has the wrong source")
            if left_map.codomain() is not right_map.codomain():
                raise ValueError("the summand maps require one common target")
            from dzack_research.preamble.categories.modules import module_homset

            return module_homset(self, left_map.codomain())(
                {
                    **{
                        ("left", label): left_map(
                            self.biproduct_factors()[0].module_generator(label)
                        )
                        for label in self.biproduct_factors()[0].module_generating_set()
                    },
                    **{
                        ("right", label): right_map(
                            self.biproduct_factors()[1].module_generator(label)
                        )
                        for label in self.biproduct_factors()[1].module_generating_set()
                    },
                }
            )

        def to_product(self, left_map, right_map):
            r"""Return the unique map ``X -> self`` with the specified projections."""
            if left_map.domain() is not right_map.domain():
                raise ValueError("the product maps require one common source")
            if left_map.codomain() is not self.biproduct_factors()[0]:
                raise ValueError("the left map has the wrong target")
            if right_map.codomain() is not self.biproduct_factors()[1]:
                raise ValueError("the right map has the wrong target")
            from dzack_research.preamble.categories.modules import module_homset
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_coefficients,
            )

            source = left_map.domain()
            return module_homset(source, self)(
                {
                    label: self.linear_combination(
                        {
                            **{
                                ("left", target_label): coefficient
                                for target_label, coefficient in module_coefficients(
                                    left_map(source.module_generator(label)),
                                    self.biproduct_factors()[0],
                                ).items()
                            },
                            **{
                                ("right", target_label): coefficient
                                for target_label, coefficient in module_coefficients(
                                    right_map(source.module_generator(label)),
                                    self.biproduct_factors()[1],
                                ).items()
                            },
                        }
                    )
                    for label in source.module_generating_set()
                }
            )


@cached_function
def _module_biproduct(left, right):
    ring = owned_ring_view(left.base_ring())
    if owned_ring_view(right.base_ring()) != ring:
        raise ValueError("a biproduct requires one common base ring")
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
        _presentation_from_relation_rows,
        _presentation_matrix,
    )

    left_labels = tuple(left.module_generating_set())
    right_labels = tuple(right.module_generating_set())
    labels = finite_ordered_set(
        [("left", label) for label in left_labels]
        + [("right", label) for label in right_labels]
    )
    rows = []
    relation_labels = []
    engine = engine_ring(ring)
    left_relations = _presentation_matrix(left).change_ring(engine)
    right_relations = _presentation_matrix(right).change_ring(engine)
    for index, relation in enumerate(left_relations.rows()):
        rows.append(tuple(relation) + (engine.zero(),) * len(right_labels))
        relation_labels.append(("left", index))
    for index, relation in enumerate(right_relations.rows()):
        rows.append((engine.zero(),) * len(left_labels) + tuple(relation))
        relation_labels.append(("right", index))
    relations = (
        tensor.matrix(engine, rows)
        if rows
        else tensor.matrix(engine, 0, len(labels))
    )
    presentation = _presentation_from_relation_rows(
        ring,
        labels,
        finite_ordered_set(relation_labels),
        relations,
    )
    result = FinitelyPresentedModule(presentation)
    result._preamble_biproduct_factors = (left, right)
    return refine(result, BiproductModules(ring))


def biproduct_morphism(left_morphism, right_morphism, source=None, target=None):
    if source is None:
        from dzack_research.preamble.categories.abstract_categories import Biproduct

        source = Biproduct(left_morphism.domain(), right_morphism.domain())
    if target is None:
        from dzack_research.preamble.categories.abstract_categories import Biproduct

        target = Biproduct(left_morphism.codomain(), right_morphism.codomain())
    left_source, right_source = source.biproduct_factors()
    from dzack_research.preamble.categories.modules import module_homset
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
    )

    images = {}
    for label in left_source.module_generating_set():
        image = left_morphism(left_source.module_generator(label))
        images[("left", label)] = target.linear_combination(
            {
                ("left", target_label): coefficient
                for target_label, coefficient in module_coefficients(
                    image, left_morphism.codomain()
                ).items()
            }
        )
    for label in right_source.module_generating_set():
        image = right_morphism(right_source.module_generator(label))
        images[("right", label)] = target.linear_combination(
            {
                ("right", target_label): coefficient
                for target_label, coefficient in module_coefficients(
                    image, right_morphism.codomain()
                ).items()
            }
        )
    return module_homset(source, target)(images)


__all__ = ["BiproductModules", "_module_biproduct", "biproduct_morphism"]
