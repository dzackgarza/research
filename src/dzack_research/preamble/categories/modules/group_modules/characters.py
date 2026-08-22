r"""Characters of finite groups as elements of their character sets."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from sage.groups.class_function import ClassFunction
from sage.libs.gap.libgap import libgap
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category

if TYPE_CHECKING:
    from sage.categories.groups import Group, GroupElement
    from sage.rings.integer import Integer
    from sage.structure.element import RingElement
    from sage.structure.parent import ElementConstructorInput, Parent

    from dzack_research.preamble.owned_category import ConstructionData

__all__ = ["Character", "CharacterSets", "character_set"]


def _identity_argument(element: "GroupElement") -> "GroupElement":
    return element


class CharacterSets(Category):
    r"""The sets \(\operatorname{Char}(G)\) of characters of finite groups."""

    def super_categories(self) -> list:
        return [Sets()]

    @classmethod
    def _repr_object_names(cls) -> str:
        return "character sets"

    class ParentMethods:
        def __init__(
            self,
            group: "Group",
            **rest: "ConstructionData",
        ) -> None:
            self._group = group
            super().__init__(**rest)

        def group(self) -> "Group":
            r"""Return the group whose characters form this set."""
            return self._group

        def _element_constructor_(
            self,
            class_function: "ClassFunction | Character",
        ) -> "Character":
            if isinstance(class_function, Character):
                assert class_function.parent() is self, (
                    "a character converts only within the character set of its group"
                )
                return class_function
            assert isinstance(class_function, ClassFunction), (
                f"{class_function!r} is not a computed class function"
            )
            assert class_function.domain() is self.group(), (
                "a character belongs to the character set of its domain group"
            )
            return Character(class_function, self.group())

        def __contains__(self, character: "ElementConstructorInput") -> bool:
            return isinstance(character, Character) and character.parent() is self

        def _repr_(self) -> str:
            return f"Characters of {self.group()}"

    class ElementMethods:
        r"""A character \(\chi:G\to K\)."""

        def __init__(
            self,
            parent: "Parent",
            class_values: tuple["RingElement", ...],
            element_argument: Callable[["GroupElement"], "ElementConstructorInput"],
        ) -> None:
            self._class_values = class_values
            self._element_argument = element_argument
            super().__init__(parent)

        def class_values(self) -> tuple["RingElement", ...]:
            r"""Return the values on the conjugacy classes of \(G\)."""
            return self._class_values

        def argument_map(
            self,
        ) -> Callable[["GroupElement"], "ElementConstructorInput"]:
            r"""Return the map into the GAP realization of \(G\)."""
            return self._element_argument

        def group(self) -> "Group":
            r"""Return the domain group \(G\)."""
            return self.parent().group()

        def element_argument(self, element: "GroupElement") -> "ElementConstructorInput":
            r"""Return the argument used in the computed class-function model."""
            return self.argument_map()(element)

        def _computed_class_function(self) -> ClassFunction:
            r"""Construct GAP's computation object from the owned value data."""
            return ClassFunction(self.group(), list(self.class_values()))

        def __call__(self, element: "GroupElement") -> "RingElement":
            r"""Return \(\chi(g)\)."""
            computed = self._computed_class_function()
            value = (
                libgap(self.element_argument(element))
                ** computed.gap()
            )
            return value.sage(ring=self.class_values()[0].parent())

        def degree(self) -> "Integer":
            r"""Return \(\chi(1)\)."""
            degree: "Integer" = self.class_values()[0]
            return degree

        def irreducible_constituents(self) -> tuple["Character", ...]:
            r"""Return the absolutely irreducible constituents of \(\chi\)."""
            engine_constituents = (
                self._computed_class_function().gap().ConstituentsOfCharacter()
            )
            return tuple(
                Character(
                    ClassFunction(self.group(), constituent),
                    self.group(),
                    element_argument=self.argument_map(),
                )
                for constituent in engine_constituents
            )

        def __add__(self, other: "ElementConstructorInput") -> "Character":
            r"""Return the character of the direct sum."""
            assert isinstance(other, Character) and self.parent() is other.parent(), (
                "a character is added to another character of the same group"
            )
            values = tuple(
                left + right
                for left, right in zip(
                    self.class_values(), other.class_values(), strict=True
                )
            )
            return Character(
                ClassFunction(self.group(), list(values)),
                self.group(),
                element_argument=self.argument_map(),
            )

        def __eq__(self, other: "ElementConstructorInput") -> bool:
            return (
                isinstance(other, Character)
                and self.parent() is other.parent()
                and self.class_values() == other.class_values()
            )

        def __hash__(self) -> int:
            return hash((self.parent(), self.class_values()))

        def _repr_(self) -> str:
            return f"Character of degree {self.degree()} of {self.group()}"


@cached_function
def character_set(group: "Group") -> "Parent":
    r"""Return \(\operatorname{Char}(G)\)."""
    return object_of(CharacterSets(), group=group)


class Character(CharacterSets().ElementType):
    r"""Construction data for an element of \(\operatorname{Char}(G)\)."""

    def __init__(
        self,
        class_function: "ClassFunction | Character",
        group: "Group | None" = None,
        element_argument: Callable[
            ["GroupElement"], "ElementConstructorInput"
        ] = _identity_argument,
    ) -> None:
        if isinstance(class_function, Character):
            if group is None:
                group = class_function.group()
            element_argument = class_function.argument_map()
            class_values = class_function.class_values()
        else:
            assert isinstance(class_function, ClassFunction), (
                f"{class_function!r} is not a computed class function"
            )
            class_values = tuple(class_function.values())
        if group is None:
            group = class_function.domain()
        super().__init__(
            character_set(group),
            class_values,
            element_argument,
        )
