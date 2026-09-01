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
from dzack_research.preamble.categories.group.groups import refine_group
from dzack_research.preamble.categories.modules.group_modules.group_modules import (
    FinitelyPresentedGroupModules,
    GroupModule,
    group_module_homset,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
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
from dzack_research.preamble.categories.rings import owned_ring_view
from dzack_research.preamble.categories.sets import finite_ordered_set


def _subgroup_data(subgroup, supergroup=None):
    subgroup = refine_group(subgroup)
    if supergroup is None:
        supergroup = subgroup.supergroup()
    if supergroup is None:
        raise ValueError("change of acting group requires a specified containing group")
    supergroup = refine_group(supergroup)
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


def _finite_coset_sum(module, representatives):
    r"""Return the finite direct sum of copies of ``module`` indexed by cosets.

    The presentation is block diagonal.  Thus all torsion and non-diagonal
    relations of the source module are retained exactly rather than replacing
    the summands by free coordinate modules.
    """
    representatives = tuple(representatives)
    source_labels = tuple(module.module_generating_set())
    labels = finite_ordered_set(
        (representative, label)
        for representative in representatives
        for label in source_labels
    )
    source_relations = _presentation_matrix(module)
    if source_relations.nrows() == 0:
        return BasedFreeModule(module.base_ring(), labels)

    from dzack_research.preamble.categories.rings import engine_ring
    from dzack_research.preamble.tensors import tensor

    engine = engine_ring(module.base_ring())
    positions = {
        pair: position
        for position, pair in enumerate(labels)
    }
    rows = []
    relation_labels = []
    for representative in representatives:
        for relation_index, relation in enumerate(source_relations.rows()):
            row = [engine.zero()] * len(labels)
            for source_label, coefficient in zip(source_labels, relation, strict=True):
                if coefficient:
                    row[positions[(representative, source_label)]] = coefficient
            rows.append(row)
            relation_labels.append((representative, relation_index))
    relations = tensor.matrix(engine, rows)
    presentation = _presentation_from_relation_rows(
        module.base_ring(),
        labels,
        finite_ordered_set(relation_labels),
        relations,
    )
    return FinitelyPresentedModule(presentation)


class RestrictionOfActingGroupFunctor(Functor):
    r"""``Res_H^G : R[G]-Mod_fp -> R[H]-Mod_fp``."""

    def __init__(self, base_ring, subgroup, supergroup=None) -> None:
        self._base_ring = owned_ring_view(base_ring)
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
        restricted._preamble_restriction_source_group_module = group_module
        return restricted

    def original_group_module(self, restricted):
        source = getattr(restricted, "_preamble_restriction_source_group_module", None)
        if source is None:
            raise ValueError("the H-module is not an object produced by this restriction functor")
        return source

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return group_module_homset(source, target)(
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
        self._base_ring = owned_ring_view(base_ring)
        self._subgroup, self._supergroup, self._inclusion = _subgroup_data(
            subgroup, supergroup
        )
        self._left_cosets = tuple(
            self._supergroup.cosets(self._subgroup, side="left")
        )
        self._representatives = finite_ordered_set(
            coset[0] for coset in self._left_cosets
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
            for (representative, label), coefficient in module_coefficients(
                vector, module
            ).items():
                target_representative, subgroup_element = self._decompose_left(
                    group_element * representative
                )
                acted = group_module.act(
                    subgroup_element, group_module.module_generator(label)
                )
                for target_label, acted_coefficient in module_coefficients(
                    acted, group_module
                ).items():
                    target_label_pair = (target_representative, target_label)
                    output_coefficients[target_label_pair] = (
                        output_coefficients.get(
                            target_label_pair, self._base_ring.zero()
                        )
                        + coefficient * acted_coefficient
                    )
            return module.linear_combination(output_coefficients)

        induced = GroupModule(module, self.supergroup(), action)
        induced._preamble_induction_source_group_module = group_module
        return induced

    def source_group_module(self, induced):
        source = getattr(induced, "_preamble_induction_source_group_module", None)
        if source is None:
            raise ValueError("the G-module is not an object produced by this induction functor")
        return source

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        images = {}
        for representative in self.representatives():
            for label in morphism.domain().module_generating_set():
                image = morphism(morphism.domain().module_generator(label))
                coefficients = module_coefficients(image, morphism.codomain())
                images[(representative, label)] = target.linear_combination(
                    {
                        (representative, target_label): coefficient
                        for target_label, coefficient in coefficients.items()
                    }
                )
        return group_module_homset(source, target)(images)

    def _repr_(self):
        return f"Induction from {self.subgroup()} to {self.supergroup()}"


class CoinductionFunctor(Functor):
    r"""``Coind_H^G : R[H]-Mod_fp -> R[G]-Mod_fp``."""

    def __init__(self, base_ring, subgroup, supergroup=None) -> None:
        self._base_ring = owned_ring_view(base_ring)
        self._subgroup, self._supergroup, self._inclusion = _subgroup_data(
            subgroup, supergroup
        )
        self._right_cosets = tuple(
            self._supergroup.cosets(self._subgroup, side="right")
        )
        self._representatives = finite_ordered_set(
            coset[0] for coset in self._right_cosets
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
            return group_module.linear_combination(
                {
                    label: coefficients[(representative, label)]
                    for label in group_module.module_generating_set()
                    if (representative, label) in coefficients
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
                        output_coefficients[(representative, label)] = coefficient
            return module.linear_combination(output_coefficients)

        coinduced = GroupModule(module, self.supergroup(), action)
        coinduced._preamble_coinduction_source_group_module = group_module
        return coinduced

    def source_group_module(self, coinduced):
        source = getattr(coinduced, "_preamble_coinduction_source_group_module", None)
        if source is None:
            raise ValueError("the G-module is not an object produced by this coinduction functor")
        return source

    def value_at(self, coinduced, vector, representative):
        source = self.source_group_module(coinduced)
        coefficients = module_coefficients(vector, coinduced)
        return source.linear_combination(
            {
                label: coefficients[(representative, label)]
                for label in source.module_generating_set()
                if (representative, label) in coefficients
            }
        )

    def element_from_values(self, coinduced, value_function):
        source = self.source_group_module(coinduced)
        coefficients = {}
        for representative in self.representatives():
            value = value_function(representative)
            for label, coefficient in module_coefficients(value, source).items():
                if coefficient:
                    coefficients[(representative, label)] = coefficient
        return coinduced.linear_combination(coefficients)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        images = {}
        for representative in self.representatives():
            for label in morphism.domain().module_generating_set():
                image = morphism(morphism.domain().module_generator(label))
                images[(representative, label)] = target.linear_combination(
                    {
                        (representative, target_label): coefficient
                        for target_label, coefficient in module_coefficients(
                            image, morphism.codomain()
                        ).items()
                    }
                )
        return group_module_homset(source, target)(images)

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
        return group_module_homset(group_module, restricted)(
            {
                label: _transport_element(
                    induced.module_generator((representative, label)),
                    induced,
                    restricted,
                )
                for label in group_module.module_generating_set()
            }
        )

    def counit(self, group_module):
        restricted = self.right_adjoint()(group_module)
        induced = self.left_adjoint()(restricted)
        return group_module_homset(induced, group_module)(
            {
                (representative, label): group_module.act(
                    representative, group_module.module_generator(label)
                )
                for representative in self.left_adjoint().representatives()
                for label in group_module.module_generating_set()
            }
        )

    def hom_set_isomorphism_forward(self, induced_morphism):
        induced = induced_morphism.domain()
        source = self.left_adjoint().source_group_module(induced)
        target = induced_morphism.codomain()
        restricted_target = self.right_adjoint()(target)
        representative = self.left_adjoint().identity_representative()
        return group_module_homset(source, restricted_target)(
            {
                label: _transport_element(
                    induced_morphism(
                        induced.module_generator((representative, label))
                    ),
                    target,
                    restricted_target,
                )
                for label in source.module_generating_set()
            }
        )

    def hom_set_isomorphism_inverse(self, restricted_morphism, codomain=None):
        restricted_target = restricted_morphism.codomain()
        target = self.right_adjoint().original_group_module(restricted_target)
        if codomain is not None and codomain is not target:
            raise ValueError("the stated G-module is not the module being restricted")
        source = self.left_adjoint()(restricted_morphism.domain())
        return group_module_homset(source, target)(
            {
                (representative, label): target.act(
                    representative,
                    _transport_element(
                        restricted_morphism(
                            restricted_morphism.domain().module_generator(label)
                        ),
                        restricted_target,
                        target,
                    ),
                )
                for representative in self.left_adjoint().representatives()
                for label in restricted_morphism.domain().module_generating_set()
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
        return group_module_homset(group_module, coinduced)(
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
        return group_module_homset(restricted, group_module)(
            {
                label: self.right_adjoint().value_at(
                    coinduced,
                    coinduced.module_generator(label),
                    representative,
                )
                for label in restricted.module_generating_set()
            }
        )

    def hom_set_isomorphism_forward(self, restricted_morphism):
        restricted_source = restricted_morphism.domain()
        source = self.left_adjoint().original_group_module(restricted_source)
        target = restricted_morphism.codomain()
        coinduced_target = self.right_adjoint()(target)
        return group_module_homset(source, coinduced_target)(
            {
                label: self.right_adjoint().element_from_values(
                    coinduced_target,
                    lambda representative, label=label: restricted_morphism(
                        _transport_element(
                            source.act(
                                representative, source.module_generator(label)
                            ),
                            source,
                            restricted_source,
                        )
                    ),
                )
                for label in source.module_generating_set()
            }
        )

    def hom_set_isomorphism_inverse(self, coinduced_morphism, codomain=None):
        coinduced_target = coinduced_morphism.codomain()
        target = self.right_adjoint().source_group_module(coinduced_target)
        if codomain is not None and codomain is not target:
            raise ValueError("the stated H-module is not the coinduction source")
        source = self.left_adjoint()(coinduced_morphism.domain())
        representative = self.right_adjoint().identity_representative()
        return group_module_homset(source, target)(
            {
                label: self.right_adjoint().value_at(
                    coinduced_target,
                    coinduced_morphism(
                        coinduced_morphism.domain().module_generator(label)
                    ),
                    representative,
                )
                for label in coinduced_morphism.domain().module_generating_set()
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
