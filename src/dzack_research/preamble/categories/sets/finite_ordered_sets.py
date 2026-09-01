"""Finite sets carrying the displayed total order."""

from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.posets import Posets
from sage.rings.integer_ring import ZZ
from sage.structure.parent import Parent


class FiniteOrderedSet(Parent):
    r"""A finite ordered facade set which never hashes its members.

    Sage's :class:`TotallyOrderedFiniteSet` deduplicates through a Python set.
    That can make merely recording a finite presentation hash expensive group
    elements and trigger group-normalization algorithms.  Equality scanning is
    sufficient here and keeps construction semantic rather than computational.
    """

    def __init__(self, elements) -> None:
        unique = []
        for element in elements:
            if element not in unique:
                unique.append(element)
        self._elements = tuple(unique)
        Parent.__init__(
            self,
            facade=True,
            category=(Posets(), FiniteEnumeratedSets()),
        )

    def __iter__(self):
        return iter(self._elements)

    def __contains__(self, element) -> bool:
        return element in self._elements

    is_parent_of = __contains__

    def __call__(self, element):
        r"""Return the displayed member equal to ``element``.

        Facade input such as a Python integer is normalized to the actual
        represented Sage element stored by this set; it never creates a second
        spelling of the same mathematical point.
        """
        return self._element_constructor_(element)

    def _element_constructor_(self, element):
        if element not in self:
            raise ValueError(f"{element!r} is not in {self}")
        return self._elements[self.position(element)]

    def __getitem__(self, index):
        return self._elements[index]

    def position(self, element) -> int:
        return self._elements.index(element)

    index = position

    def cardinality(self):
        return ZZ(len(self._elements))

    def __len__(self) -> int:
        return len(self._elements)

    def le(self, left, right) -> bool:
        return self.position(left) <= self.position(right)

    def _repr_(self) -> str:
        return "{" + ", ".join(repr(element) for element in self._elements) + "}"


def finite_ordered_set(elements) -> FiniteOrderedSet:
    r"""Transport the displayed finite enumeration to a total order."""
    if isinstance(elements, FiniteOrderedSet):
        return elements
    return FiniteOrderedSet(elements)
