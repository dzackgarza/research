# Repo-scoped stubs; see lexicon/README.md.
#
# The image of a set under a map, as a set in its own right -- what the
# preamble returns where the lexicon noun ``Set`` is declared (a framed
# module's generators may be infinite, so the image object is the answer, not
# a coerced tuple). Declares the ``Sets.ParentMethods`` MRO edge, so it
# satisfies the noun.
from collections.abc import Iterator

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.parent import Parent

class ImageSubobject(Sets.ParentMethods[Element], Parent[Element]):
    def __init__(
        self,
        map: Morphism,
        domain_subset: Parent,
        *,
        category: Category | None = ...,
        is_injective: bool | None = ...,
        inverse: Morphism | None = ...,
    ) -> None: ...
    # The set the image sits inside (the map's codomain).
    def ambient(self) -> Parent: ...
    def lift(self, x: Element) -> Element: ...
    def retract(self, x: Element) -> Element: ...
    # The image of an infinite domain may be infinite: over ZZ in QQ the
    # cardinality is +Infinity (verified), so Integer alone would be false.
    def cardinality(self) -> Integer | PlusInfinity: ...
    def __iter__(self) -> Iterator[Element]: ...

class ImageSet(ImageSubobject): ...
