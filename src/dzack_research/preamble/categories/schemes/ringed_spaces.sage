r"""Subtree for ringed spaces and locally ringed spaces under the schemes category tree.

Hierarchy:
  RingedSpaces()
    ├── .LocallyRinged()
    └── LocallyRingedSpaces() = RingedSpaces().LocallyRinged()
"""

from dzack_research.preamble.categories.rings.rings import engine_ring
from dzack_research.preamble.refine import refine
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent
from dzack_research.preamble.categories.rings.rings import OwnedBaseRing
from sage.structure.element import Element
from sage.categories.category import Category
from sage.categories.category_with_axiom import (
    all_axioms,
    axiom,
)
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.sets.owned_sets import Sets

# Register LocallyRinged axiom in Sage's axiom registry if not already present
if "LocallyRinged" not in all_axioms:
    all_axioms.add("LocallyRinged")


# ---------------------------------------------------------------------------
# RingedSpaces and LocallyRinged Axiom
# ---------------------------------------------------------------------------


class RingedSpaceElement(Element):
    r"""Element / section or point of a ringed space."""


class RingedSpace(OwnedBaseRing, Parent):
    r"""A ringed space (X, O_X): a topological space equipped with a sheaf of rings."""

    Element = RingedSpaceElement

    def __init__(self, base_ring=SageZZ) -> None:
        r"""Initialize the ringed space and refine into RingedSpaces.

        Every scheme in this file's tower reaches ``Parent.__init__`` here, so
        this is where the base ring crosses to the engine: the categories the
        tower refines into are named by the engine's ring, and a space whose
        base is the owned view of it would belong to none of them.
        """
        Parent.__init__(self, base=engine_ring(base_ring))
        refine(self, RingedSpaces())


class RingedSpaceMorphism(Morphism):
    r"""Morphism of ringed spaces (f, f#): (X, O_X) -> (Y, O_Y)."""


class RingedSpaces(Category):
    r"""Category of ringed spaces."""

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

        def structure_sheaf(self):
            r"""Return O_X, the sheaf of rings."""
            assert False, "structure_sheaf must be implemented by concrete RingedSpace"

        def underlying_space(self):
            r"""Return the underlying topological space X."""
            assert False, "underlying_space must be implemented by concrete RingedSpace"

    class ElementMethods:
        r"""Ringed space element methods."""

    class MorphismMethods:
        r"""Ringed space morphism methods."""


# ---------------------------------------------------------------------------
# LocallyRingedSpaces = RingedSpaces().LocallyRinged()
# ---------------------------------------------------------------------------


class LocallyRingedSpace(RingedSpace):
    r"""A locally ringed space: a ringed space whose stalks are local rings."""

    Element = RingedSpaceElement

    def __init__(self, base_ring=SageZZ) -> None:
        r"""Initialize the locally ringed space and refine into LocallyRingedSpaces."""
        RingedSpace.__init__(self, base_ring=base_ring)
        refine(self, LocallyRingedSpaces())


class LocallyRingedSpaces(Category):
    r"""Category of locally ringed spaces: ringed spaces satisfying the LocallyRinged axiom."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "locally ringed spaces"

    def super_categories(self) -> list:
        r"""Return RingedSpaces() with the LocallyRinged axiom."""
        return [RingedSpaces().LocallyRinged()]

    class ParentMethods:
        r"""Locally ringed space parent methods."""

        def stalk(self, point):
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
