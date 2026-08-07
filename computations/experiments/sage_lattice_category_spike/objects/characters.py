r"""The character of a representation of a finite group.

An owned noun over a computed class function, in the same spirit as
``MorphismMatrix`` over a Sage matrix: the seam exists so that a caller asks
a character the questions a character answers -- its value at a group
element, its degree, its values on the conjugacy classes, the absolutely
irreducible characters occurring in it -- and never reaches the engine that
computed the table.

The computation is GAP's, reached through Sage's ``ClassFunction``: the
conjugacy classes, the character table, the irreducible characters, and the
degrees are all read from there and none of them is written here.  What is
written here is which of those readings is a mathematical question.
"""

from __future__ import annotations

from sage.groups.class_function import ClassFunction

__all__ = ["Character"]


class Character:
    r"""A class function $\chi:G\to K$ afforded by a representation of $G$."""

    def __init__(self, class_function: "ClassFunction | Character") -> None:
        match class_function:
            case Character():
                self._class_function = class_function._class_function
            case ClassFunction():
                self._class_function = class_function
            case _:
                assert False, (
                    f"{class_function!r} is not a computed class function"
                )

    def group(self) -> "Group":
        r"""Return the group $G$ this character is a class function on."""
        return self._class_function.domain()

    def __call__(self, element: "GroupElement") -> "Element":
        r"""Return $\chi(g)$, the trace of $g$ in a representation affording $\chi$."""
        return self._class_function(element)

    def degree(self) -> "Integer":
        r"""Return $\chi(1)$, the dimension of a representation affording $\chi$."""
        return self._class_function.degree()

    def class_values(self) -> tuple:
        r"""Return the values of $\chi$ on the conjugacy classes of $G$.

        A character is constant on a conjugacy class, so this family is the
        whole of it: two characters are equal exactly when these agree.  The
        order is the group's own enumeration of its classes, which is why the
        family is compared as a whole and never indexed by position here.
        """
        return tuple(self._class_function.values())

    def irreducible_constituents(self) -> tuple:
        r"""Return the absolutely irreducible characters occurring in $\chi$.

        Each with multiplicity one in the tuple: what is returned is the set
        of constituents, not the decomposition.  For an absolutely
        irreducible $\chi$ this is $(\chi)$, and for an $F$-irreducible one it
        is the Galois orbit whose sum $\chi$ is.
        """
        return tuple(
            Character(constituent)
            for constituent in self._class_function.irreducible_constituents()
        )

    def __add__(self, other: object) -> "Character":
        r"""Return $\chi+\psi$, the character of a direct sum."""
        assert isinstance(other, Character), (
            "a character is added to another character of the same group"
        )
        return Character(self._class_function + other._class_function)

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Character)
            and self.group() is other.group()
            and self.class_values() == other.class_values()
        )

    def __hash__(self) -> int:
        return hash((id(self.group()), self.class_values()))

    def __repr__(self) -> str:
        return f"Character of degree {self.degree()} of {self.group()}"
