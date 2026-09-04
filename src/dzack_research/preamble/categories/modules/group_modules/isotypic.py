r"""Isotypic components of finite characteristic-zero group modules."""

from __future__ import annotations

from dataclasses import dataclass

from sage.categories.category import Category
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
)
from dzack_research.preamble.refine import refine


@dataclass(frozen=True)
class IsotypicCharacter:
    r"""A coefficient-field irreducible character or a rational Galois orbit."""

    characters: tuple

    def degree(self):
        return sum(character.degree() for character in self.characters)

    def is_trivial(self) -> bool:
        return all(
            all(value == 1 for value in character.values())
            for character in self.characters
        )

    def __call__(self, group_element):
        return sum(character(group_element) for character in self.characters)

    def _repr_(self):
        if len(self.characters) == 1:
            return repr(self.characters[0])
        return "Rational character orbit of " + ", ".join(
            repr(character) for character in self.characters
        )

    __repr__ = _repr_


class IsotypicDecompositions(Category):
    r"""Submodules equipped with their selected isotypic summands."""

    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import Sets

        return [Sets()]

    class ParentMethods:
        def isotypic_characters(self):
            return self._preamble_isotypic_characters

        def isotypic_component(self, character):
            labels = self.isotypic_characters()
            for position, candidate in enumerate(labels):
                if candidate == character or character in candidate.characters:
                    return self._preamble_isotypic_components[position]
            raise ValueError(f"{character!r} does not index this isotypic decomposition")

        def trivial_component(self):
            for character in self.isotypic_characters():
                if character.is_trivial():
                    return self.isotypic_component(character)
            raise ValueError("this decomposition has no trivial character")

        def nontrivial_components(self):
            return tuple(
                component
                for character, component in zip(
                    self.isotypic_characters(),
                    self._preamble_isotypic_components,
                    strict=True,
                )
                if not character.is_trivial()
            )


def _character_rows(group):
    characters = tuple(group.irreducible_characters())
    rows = tuple(tuple(character.values()) for character in characters)
    return characters, rows


def _galois_orbits_of_irreducible_characters(group):
    r"""Return rational central-character orbits of the complex irreducibles."""
    characters, rows = _character_rows(group)
    if not characters:
        return tuple()
    field = group.character_table().base_ring()
    try:
        automorphisms = tuple(field.galois_group())
    except (AttributeError, NotImplementedError, TypeError):
        automorphisms = tuple()
    if not automorphisms:
        return tuple(IsotypicCharacter((character,)) for character in characters)

    unused = set(range(len(characters)))
    result = []
    while unused:
        seed = min(unused)
        orbit_rows = set()
        for automorphism in automorphisms:
            orbit_rows.add(
                tuple(automorphism(field(value)) for value in rows[seed])
            )
        orbit = tuple(
            index for index, row in enumerate(rows) if tuple(row) in orbit_rows
        )
        for index in orbit:
            unused.discard(index)
        result.append(IsotypicCharacter(tuple(characters[index] for index in orbit)))
    return tuple(result)


def _split_irreducible_characters(module):
    r"""Return the correct public character index for the coefficient ring."""
    ring = _engine_ring(module.base_ring())
    group = module.group()
    if ring in (SageZZ, SageQQ):
        return _galois_orbits_of_irreducible_characters(group)
    if not ring.is_field() or ring.characteristic() != 0:
        raise NotImplementedError(
            "isotypic projectors are currently implemented in characteristic zero"
        )
    characters = tuple(group.irreducible_characters())
    for character in characters:
        for value in character.values():
            try:
                ring(value)
            except (TypeError, ValueError) as error:
                raise NotImplementedError(
                    "the coefficient field is not a splitting field for the represented irreducible characters"
                ) from error
    return tuple(IsotypicCharacter((character,)) for character in characters)


def _central_projector(module, character: IsotypicCharacter):
    r"""Return the central idempotent as an owned matrix endomorphism."""
    group = module.group()
    base_ring = module.base_ring()
    engine_ring = _engine_ring(base_ring)
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace

    computation_ring = _own_ring(SageQQ) if engine_ring is SageZZ else base_ring
    rank = int(module.rank())
    matrices = MatrixSpace(computation_ring, rank)
    projector = matrices.zero()
    order = computation_ring(int(group.order()))
    computation_engine = _engine_ring(computation_ring)

    for group_element in group:
        backend_coefficient = sum(
            irreducible.degree() * irreducible(group_element**-1)
            for irreducible in character.characters
        )
        coefficient = computation_ring._from_engine_element(
            computation_engine(backend_coefficient)
        ) / order
        source = module.action_of(group_element).matrix()
        transported = matrices.from_rows(
            [
                [
                    computation_ring._from_engine_element(
                        computation_engine(
                            _engine_element(base_ring, source[row, column])
                        )
                    )
                    for column in range(rank)
                ]
                for row in range(rank)
            ]
        )
        projector += coefficient * transported
    return projector


def _kernel_subobject_of_matrix(module, matrix):
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    labels = tuple(module.module_generating_set())
    images = {
        source_label: module.linear_combination(
            {
                target_label: matrix[target_index, source_index]
                for target_index, target_label in enumerate(labels)
                if matrix[target_index, source_index]
            }
        )
        for source_index, source_label in enumerate(labels)
    }
    return module_homset(module, module)(images).kernel()


def isotypic_component(module, character):
    r"""Return ``M ∩ V_character`` as a subobject of ``M``."""
    characters = _split_irreducible_characters(module)
    selected = next(
        (
            candidate
            for candidate in characters
            if candidate == character or character in candidate.characters
        ),
        None,
    )
    if selected is None:
        raise ValueError(f"{character!r} is not an irreducible-character index for this module")
    projector = _central_projector(module, selected)
    base_ring = module.base_ring()
    relation = projector - projector.parent().identity()
    if _engine_ring(base_ring) is SageZZ:
        integers = base_ring
        denominator = integers.one()
        for entry in relation.list():
            denominator = denominator.lcm(entry.denominator())
        cleared = denominator * relation
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace

        relation = MatrixSpace(integers, int(module.rank())).from_rows(
            [
                [
                    cleared[row, column].numerator()
                    for column in range(int(module.rank()))
                ]
                for row in range(int(module.rank()))
            ]
        )
    return _kernel_subobject_of_matrix(module, relation)


def isotypic_decomposition(module):
    r"""Return ``⊕ M_chi -> M`` with its selected summand structure."""
    characters = _split_irreducible_characters(module)
    components = tuple(isotypic_component(module, character) for character in characters)
    if not components:
        return module.subobject_on(())
    summed = components[0]
    for component in components[1:]:
        summed = summed.sum(component)
    summed._preamble_isotypic_characters = characters
    summed._preamble_isotypic_components = components
    from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import (
        DirectSumObjects,
    )

    summed._preamble_direct_sum_summands = components
    from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

    summed._preamble_direct_sum_index_set = finite_ordered_set(characters)
    return refine(
        summed,
        [summed.category(), DirectSumObjects(), IsotypicDecompositions()],
    )


__all__ = [
    "IsotypicCharacter",
    "IsotypicDecompositions",
    "isotypic_component",
    "isotypic_decomposition",
]
