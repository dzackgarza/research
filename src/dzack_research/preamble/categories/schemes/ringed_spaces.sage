r"""Subtree for ringed spaces and locally ringed spaces under the schemes category tree.

Hierarchy:
  RingedSpaces()
    ├── .LocallyRinged()
    └── LocallyRingedSpaces() = RingedSpaces().LocallyRinged()
"""

from dzack_research.preamble.categories.rings.rings import engine_ring
from dzack_research.preamble.categories.rings.rings import owned_ring_view
from sage.structure.parent import Parent
from sage.structure.element import Element
from dzack_research.preamble.owned_category_bases import Category
from sage.categories.category_with_axiom import (
    all_axioms,
    axiom,
)
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.sets.owned_sets import Sets

from typing import Self, TYPE_CHECKING

if TYPE_CHECKING:
    from sage.categories.rings import Ring
    from dzack_research.preamble.owned_category import ConstructionData

# Register LocallyRinged axiom in Sage's axiom registry if not already present
if "LocallyRinged" not in all_axioms:
    all_axioms.add("LocallyRinged")


# ---------------------------------------------------------------------------
# RingedSpaces and LocallyRinged Axiom
# ---------------------------------------------------------------------------


class RingedSpaces(Category):
    r"""Category of ringed spaces (X, O_X): a space with a sheaf of rings."""

    if TYPE_CHECKING:
        # Offered through ``SubcategoryMethods`` below.  Sage synthesizes the
        # axiom application from the registry entry, so nothing here defines
        # it and the checker is told what the axiom offers.
        def LocallyRinged(self) -> Category: ...

    @classmethod
    def _repr_object_names(cls) -> str:
        return "ringed spaces"

    def super_categories(self) -> list:
        r"""Return Sets(), of which ringed spaces are sets with structure."""
        return [Sets()]

    class SubcategoryMethods:
        r"""Axiom subcategories offered on RingedSpaces."""

        LocallyRinged = axiom("LocallyRinged")

    class ParentMethods:
        r"""Ringed space parent methods."""

        def __init__(
            self: Self,
            base_ring: "Ring" = SageZZ,
            **rest: "ConstructionData",
        ) -> None:
            r"""Build the ringed space over ``base_ring``.

            Every scheme in this tower reaches the set level through here, so
            this is where the base ring crosses to the engine: the categories
            the tower names are named by the engine's ring, and a space whose
            base is the owned view of it would belong to none of them.
            """
            super().__init__(base=engine_ring(base_ring), **rest)

        def base_ring(self: Self) -> "Ring":
            r"""Return the base ring, in the name the session gave it.

            ``base()`` reports what the construction handed the set level,
            which is the engine's ring.  A session that wrote \(\ZZ\) asked
            about *its* \(\ZZ\), and the two are one ring.
            """
            return owned_ring_view(self.base())

        def structure_sheaf(self: Self) -> "Sheaf":
            r"""Return O_X, the sheaf of rings."""
            assert False, "structure_sheaf must be implemented by concrete RingedSpace"

        def underlying_space(self: Self) -> Parent:
            r"""Return the underlying topological space X."""
            assert False, "underlying_space must be implemented by concrete RingedSpace"

    class ElementMethods:
        r"""Ringed space element methods: a section or a point."""

    class MorphismMethods:
        r"""Ringed space morphism methods: (f, f#): (X, O_X) -> (Y, O_Y)."""


# ---------------------------------------------------------------------------
# LocallyRingedSpaces = RingedSpaces().LocallyRinged()
# ---------------------------------------------------------------------------


class LocallyRingedSpaces(Category):
    r"""Category of locally ringed spaces: ringed spaces whose stalks are local rings."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "locally ringed spaces"

    def super_categories(self) -> list:
        r"""Return RingedSpaces() with the LocallyRinged axiom."""
        return [RingedSpaces().LocallyRinged()]

    class ParentMethods:
        r"""Locally ringed space parent methods."""

        def stalk(self: Self, point: Element) -> "Ring":
            r"""Return O_{X, x}, the stalk at point x (a local ring)."""
            assert False, "stalk must be implemented by concrete LocallyRingedSpace"

    class ElementMethods:
        r"""Locally ringed space element methods."""

    class MorphismMethods:
        r"""Locally ringed space morphism methods."""


def install_ringed_spaces() -> None:
    r"""Register post-init hooks and installation for ringed spaces."""
    pass


install_ringed_spaces()
