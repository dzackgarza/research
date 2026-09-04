r"""Induction, restriction, and coinduction for finite-group modules.

For a subgroup ``H <= G`` and a coefficient ring ``R`` the represented
finitely-presented module categories are closed under the standard adjoint triple

``Ind_H^G ⊣ Res_H^G ⊣ Coind_H^G``.

The implementation uses Sage's finite cosets only to choose coordinates for
``R[G]`` over ``R[H]``.  The returned objects are ordinary public
``GroupModule`` objects, and all morphisms live in ``GroupModuleHomset``.
"""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.group.groups import _owned_group
from dzack_research.preamble.categories.modules.group_modules.group_modules import (
    FinitelyPresentedGroupModules,
    GroupModule,
    group_module_homset,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    FinitelyPresentedModule,
    _presentation_from_relation_rows,
    _presentation_matrix,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.categories.sets.set_categories import CartesianProductOfFamily
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_image
from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace


def _subgroup_data(subgroup, supergroup=None):
    subgroup = _owned_group(subgroup)
    if supergroup is None:
        supergroup = subgroup.supergroup()
    if supergroup is None:
        raise ValueError("change of acting group requires a specified containing group")
    supergroup = _owned_group(supergroup)
    inclusion = subgroup.inclusion()
    if inclusion.codomain() is not supergroup:
        raise ValueError("the subgroup inclusion has a different containing group")
    if supergroup.is_finite() is not True:
        raise NotImplementedError(
            "the represented induction/coinduction model currently requires a finite containing group"
        )
    return subgroup, supergroup, inclusion


def _transport_element(element, source, target):
    r"""Transport one framed vector across equal selected module labels."""
    return target.linear_combination(module_coefficients(element, source))


def _equivariant_hom(domain, codomain, images):
    r"""Construct a group-module map whose equivariance is structural."""
    return group_module_homset(domain, codomain)._from_equivariant_images(images)


def _coset_sum_labels(representatives, source_labels):
    return CartesianProductOfFamily(
        Sets.Δ[1],
        lambda index: representatives if int(index) == 0 else source_labels,
    )


def _coset_label(labels, representative, source_label):
    return labels(
        lambda index: representative if int(index) == 0 else source_label
    )


def _finite_coset_sum(module, representatives):
    r"""Return the finite direct sum of copies of ``module`` indexed by cosets.

    The framing is the actual product of the representative set with the source
    framing.  Presentation rows are generated directly from this product; no
    Python pair family or block-row list is a mathematical carrier.
    """
    source_labels = module.module_generating_set()
    labels = _coset_sum_labels(representatives, source_labels)
    source_relations = _presentation_matrix(module)
    relation_count = int(source_relations.nrows())
    if relation_count == 0:
        return BasedFreeModule(module.base_ring(), labels)

    representative_count = int(representatives.cardinality())
    width = int(labels.cardinality())
    relation_indices = Sets.Δ[relation_count - 1]
    relation_labels = _coset_sum_labels(representatives, relation_indices)
    row_count = representative_count * relation_count
    ring = module.base_ring()

    def entry(row_position, column_position):
        relation_label = relation_labels.unrank(row_position)
        column_label = labels.unrank(column_position)
        if relation_label.component(0) != column_label.component(0):
            return ring.zero()
        source_position = int(source_labels.rank(column_label.component(1)))
        relation_position = int(relation_label.component(1))
        return source_relations[relation_position, source_position]


    relations = MatrixSpace(
        ring,
        row_count,
        width,
    ).from_rows(
        tuple(
            tuple(entry(row_position, column_position) for column_position in range(width))
            for row_position in range(row_count)
        )
    )
    presentation = _presentation_from_relation_rows(
        ring,
        labels,
        relation_labels,
        relations,
    )
    return FinitelyPresentedModule(presentation)


class RestrictionOfActingGroupFunctor(Functor):
    r"""``Res_H^G : R[G]-Mod_fp -> R[H]-Mod_fp``."""

    def __init__(self, base_ring, subgroup, supergroup=None) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._subgroup, self._supergroup, self._inclusion = _subgroup_data(
            subgroup, supergroup
        )
        super().__init__(
            FinitelyPresentedGroupModules(self._base_ring, self._supergroup),
            FinitelyPresentedGroupModules(self._base_ring, self._subgroup),
        )

    def subgroup(self):
        return self._subgroup

    def supergroup(self):
        return self._supergroup

    def inclusion(self):
        return self._inclusion

    def _apply_object(self, group_module):
        restricted = GroupModule(
            group_module,
            self.subgroup(),
            lambda subgroup_element, vector: group_module.act(
                self.inclusion()(subgroup_element), vector
            ),
        )
        return restricted

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return _equivariant_hom(source, target,
            {
                label: _transport_element(
                    morphism(morphism.domain().module_generator(label)),
                    morphism.codomain(),
                    target,
                )
                for label in morphism.domain().module_generating_set()
            }
        )

    def _repr_(self):
        return f"Restriction from {self.supergroup()} to {self.subgroup()}"


class InductionFunctor(Functor):
    r"""``Ind_H^G : R[H]-Mod_fp -> R[G]-Mod_fp``."""

    def __init__(self, base_ring, subgroup, supergroup=None) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._subgroup, self._supergroup, self._inclusion = _subgroup_data(
            subgroup, supergroup
        )
        self._left_cosets = self._supergroup.left_cosets(self._subgroup)
        self._representatives = finite_ordered_image(
            self._left_cosets,
            lambda coset: coset.unrank(0),
            name="Left-coset representatives",
        )
        super().__init__(
            FinitelyPresentedGroupModules(self._base_ring, self._subgroup),
            FinitelyPresentedGroupModules(self._base_ring, self._supergroup),
        )

    def subgroup(self):
        return self._subgroup

    def supergroup(self):
        return self._supergroup

    def inclusion(self):
        return self._inclusion

    def representatives(self):
        return self._representatives

    def identity_representative(self):
        identity = self.supergroup().one()
        for representative in self.representatives():
            if identity in next(
                coset for coset in self._left_cosets if coset[0] == representative
            ):
                return representative
        raise AssertionError("the subgroup coset must contain the identity")

    def _decompose_left(self, group_element):
        for coset in self._left_cosets:
            if group_element in coset:
                representative = coset[0]
                subgroup_element = self.subgroup()(
                    representative**-1 * group_element
                )
                return representative, subgroup_element
        raise AssertionError("finite left cosets partition the containing group")

    def _apply_object(self, group_module):
        module = _finite_coset_sum(group_module, self.representatives())

        def action(group_element, vector):
            output_coefficients = {}
            for pair, coefficient in module_coefficients(vector, module).items():
                representative = pair.component(0)
                label = pair.component(1)
                target_representative, subgroup_element = self._decompose_left(
                    group_element * representative
                )
                acted = group_module.act(
                    subgroup_element, group_module.module_generator(label)
                )
                for target_label, acted_coefficient in module_coefficients(
                    acted, group_module
                ).items():
                    target_label_pair = _coset_label(
                        module.module_generating_set(),
                        target_representative,
                        target_label,
                    )
                    output_coefficients[target_label_pair] = (
                        output_coefficients.get(
                            target_label_pair, self._base_ring.zero()
                        )
                        + coefficient * acted_coefficient
                    )
            return module.linear_combination(output_coefficients)

        return GroupModule(module, self.supergroup(), action)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        images = {}
        for representative in self.representatives():
            for label in morphism.domain().module_generating_set():
                image = morphism(morphism.domain().module_generator(label))
                coefficients = module_coefficients(image, morphism.codomain())
                images[_coset_label(
                    source.module_generating_set(), representative, label
                )] = target.linear_combination(
                    {
                        _coset_label(
                            target.module_generating_set(),
                            representative,
                            target_label,
                        ): coefficient
                        for target_label, coefficient in coefficients.items()
                    }
                )
        return _equivariant_hom(source, target, images)

    def _repr_(self):
        return f"Induction from {self.subgroup()} to {self.supergroup()}"


class CoinductionFunctor(Functor):
    r"""``Coind_H^G : R[H]-Mod_fp -> R[G]-Mod_fp``."""

    def __init__(self, base_ring, subgroup, supergroup=None) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._subgroup, self._supergroup, self._inclusion = _subgroup_data(
            subgroup, supergroup
        )
        self._right_cosets = self._supergroup.right_cosets(self._subgroup)
        self._representatives = finite_ordered_image(
            self._right_cosets,
            lambda coset: coset.unrank(0),
            name="Right-coset representatives",
        )
        super().__init__(
            FinitelyPresentedGroupModules(self._base_ring, self._subgroup),
            FinitelyPresentedGroupModules(self._base_ring, self._supergroup),
        )

    def subgroup(self):
        return self._subgroup

    def supergroup(self):
        return self._supergroup

    def inclusion(self):
        return self._inclusion

    def representatives(self):
        return self._representatives

    def identity_representative(self):
        identity = self.supergroup().one()
        for representative in self.representatives():
            if identity in next(
                coset for coset in self._right_cosets if coset[0] == representative
            ):
                return representative
        raise AssertionError("the subgroup coset must contain the identity")

    def _decompose_right(self, group_element):
        for coset in self._right_cosets:
            if group_element in coset:
                representative = coset[0]
                subgroup_element = self.subgroup()(
                    group_element * representative**-1
                )
                return subgroup_element, representative
        raise AssertionError("finite right cosets partition the containing group")

    def _apply_object(self, group_module):
        module = _finite_coset_sum(group_module, self.representatives())

        def value_at(vector, representative):
            coefficients = module_coefficients(vector, module)
            module_labels = module.module_generating_set()
            return group_module.linear_combination(
                {
                    label: coefficients[
                        _coset_label(module_labels, representative, label)
                    ]
                    for label in group_module.module_generating_set()
                    if _coset_label(module_labels, representative, label)
                    in coefficients
                }
            )

        def action(group_element, vector):
            output_coefficients = {}
            for representative in self.representatives():
                subgroup_element, source_representative = self._decompose_right(
                    representative * group_element
                )
                acted = group_module.act(
                    subgroup_element, value_at(vector, source_representative)
                )
                for label, coefficient in module_coefficients(
                    acted, group_module
                ).items():
                    if coefficient:
                        output_coefficients[
                            _coset_label(
                                module.module_generating_set(),
                                representative,
                                label,
                            )
                        ] = coefficient
            return module.linear_combination(output_coefficients)

        return GroupModule(module, self.supergroup(), action)

    def value_at(self, coinduced, vector, representative):
        source = self.chosen_preimage(coinduced)
        coefficients = module_coefficients(vector, coinduced)
        labels = coinduced.module_generating_set()
        return source.linear_combination(
            {
                label: coefficients[_coset_label(labels, representative, label)]
                for label in source.module_generating_set()
                if _coset_label(labels, representative, label) in coefficients
            }
        )

    def element_from_values(self, coinduced, value_function):
        source = self.chosen_preimage(coinduced)
        coefficients = {}
        for representative in self.representatives():
            value = value_function(representative)
            for label, coefficient in module_coefficients(value, source).items():
                if coefficient:
                    coefficients[
                        _coset_label(
                            coinduced.module_generating_set(),
                            representative,
                            label,
                        )
                    ] = coefficient
        return coinduced.linear_combination(coefficients)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        images = {}
        for representative in self.representatives():
            for label in morphism.domain().module_generating_set():
                image = morphism(morphism.domain().module_generator(label))
                images[_coset_label(
                    source.module_generating_set(), representative, label
                )] = target.linear_combination(
                    {
                        _coset_label(
                            target.module_generating_set(),
                            representative,
                            target_label,
                        ): coefficient
                        for target_label, coefficient in module_coefficients(
                            image, morphism.codomain()
                        ).items()
                    }
                )
        return _equivariant_hom(source, target, images)

    def _repr_(self):
        return f"Coinduction from {self.subgroup()} to {self.supergroup()}"


class InductionRestrictionAdjunction(Adjunction):
    r"""``Ind_H^G ⊣ Res_H^G`` on represented finitely-presented group modules."""

    def __init__(self, base_ring, subgroup, supergroup=None) -> None:
        subgroup, supergroup, _inclusion = _subgroup_data(subgroup, supergroup)
        super().__init__(
            InductionFunctor(base_ring, subgroup, supergroup),
            RestrictionOfActingGroupFunctor(base_ring, subgroup, supergroup),
        )

    def unit(self, group_module):
        induced = self.left_adjoint()(group_module)
        restricted = self.right_adjoint()(induced)
        representative = self.left_adjoint().identity_representative()
        return _equivariant_hom(group_module, restricted,
            {
                label: _transport_element(
                    induced.module_generator(_coset_label(induced.module_generating_set(), representative, label)),
                    induced,
                    restricted,
                )
                for label in group_module.module_generating_set()
            }
        )

    def counit(self, group_module):
        restricted = self.right_adjoint()(group_module)
        induced = self.left_adjoint()(restricted)
        return _equivariant_hom(induced, group_module,
            {
                _coset_label(induced.module_generating_set(), representative, label): group_module.act(
                    representative, group_module.module_generator(label)
                )
                for representative in self.left_adjoint().representatives()
                for label in group_module.module_generating_set()
            }
        )



class RestrictionCoinductionAdjunction(Adjunction):
    r"""``Res_H^G ⊣ Coind_H^G`` on represented finitely-presented group modules."""

    def __init__(self, base_ring, subgroup, supergroup=None) -> None:
        subgroup, supergroup, _inclusion = _subgroup_data(subgroup, supergroup)
        super().__init__(
            RestrictionOfActingGroupFunctor(base_ring, subgroup, supergroup),
            CoinductionFunctor(base_ring, subgroup, supergroup),
        )

    def unit(self, group_module):
        restricted = self.left_adjoint()(group_module)
        coinduced = self.right_adjoint()(restricted)
        return _equivariant_hom(group_module, coinduced,
            {
                label: self.right_adjoint().element_from_values(
                    coinduced,
                    lambda representative, label=label: _transport_element(
                        group_module.act(
                            representative,
                            group_module.module_generator(label),
                        ),
                        group_module,
                        restricted,
                    ),
                )
                for label in group_module.module_generating_set()
            }
        )

    def counit(self, group_module):
        coinduced = self.right_adjoint()(group_module)
        restricted = self.left_adjoint()(coinduced)
        representative = self.right_adjoint().identity_representative()
        return _equivariant_hom(restricted, group_module,
            {
                label: self.right_adjoint().value_at(
                    coinduced,
                    coinduced.module_generator(label),
                    representative,
                )
                for label in restricted.module_generating_set()
            }
        )



@cached_function
def induction_restriction_adjunction(
    base_ring, subgroup, supergroup=None
) -> InductionRestrictionAdjunction:
    return InductionRestrictionAdjunction(base_ring, subgroup, supergroup)


@cached_function
def restriction_coinduction_adjunction(
    base_ring, subgroup, supergroup=None
) -> RestrictionCoinductionAdjunction:
    return RestrictionCoinductionAdjunction(base_ring, subgroup, supergroup)


__all__ = [
    "CoinductionFunctor",
    "InductionFunctor",
    "InductionRestrictionAdjunction",
    "RestrictionCoinductionAdjunction",
    "RestrictionOfActingGroupFunctor",
    "induction_restriction_adjunction",
    "restriction_coinduction_adjunction",
]
