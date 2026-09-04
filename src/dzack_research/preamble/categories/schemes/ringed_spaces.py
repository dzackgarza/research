"""Owned ringed-space structure used by the scheme hierarchy."""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoryPacketMethods,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


class SchemeUnderlyingSpace(SageObject):
    r"""The underlying topological space of a represented ringed space.

    Sage's scheme parents do not expose a separate topological-space parent.
    The owned API nevertheless keeps the mathematical structure explicit: this
    object remembers the represented scheme and is the carrier on which open
    and closed-subspace structure can later be attached.
    """

    def __init__(self, ringed_space) -> None:
        self._ringed_space = ringed_space

    def ringed_space(self):
        return self._ringed_space

    scheme = ringed_space

    def _repr_(self) -> str:
        return f"Underlying topological space of {self.ringed_space()}"


class StructureSheaf(SageObject):
    r"""The represented structure sheaf ``O_X`` of a ringed space ``X``."""

    def __init__(self, ringed_space) -> None:
        self._ringed_space = ringed_space

    def ringed_space(self):
        return self._ringed_space

    scheme = ringed_space

    def global_sections(self):
        r"""Return ``Gamma(X,O_X)`` in the exact cases represented live."""
        operation = getattr(self.ringed_space(), "_structure_sheaf_global_sections", None)
        if operation is None:
            raise NotImplementedError(
                f"global sections of the structure sheaf of {self.ringed_space()} are not represented"
            )
        return operation()

    sections = global_sections

    def sections_on_distinguished_open(self, distinguished_open):
        r"""Return ``O_X(D(f)) = Gamma(X,O_X)_f`` for an affine scheme."""
        operation = getattr(
            self.ringed_space(),
            "_structure_sheaf_sections_on_distinguished_open",
            None,
        )
        if operation is None:
            raise NotImplementedError(
                "distinguished-open structure-sheaf sections are not represented for this ringed space"
            )
        return operation(distinguished_open)

    def stalk(self, point):
        r"""Return ``O_{X,p}`` for a represented affine prime point."""
        operation = getattr(self.ringed_space(), "_structure_sheaf_stalk", None)
        if operation is None:
            raise NotImplementedError(
                "structure-sheaf stalks are not represented for this ringed space"
            )
        return operation(point)

    def _repr_(self) -> str:
        return f"Structure sheaf O_{{{self.scheme()}}}"


class RingedSpaces(CategoryPacketMethods, Category):
    r"""Ringed spaces ``(X,O_X)``."""

    @classmethod
    def _repr_object_names(cls):
        return "ringed spaces"

    def super_categories(self):
        return [Sets()]

    def __contains__(self, candidate) -> bool:
        return hasattr(candidate, "_preamble_scheme_base_ring")

    def LocallyRinged(self):
        return LocallyRingedSpaces()

    class ParentMethods:
        @cached_method
        def structure_sheaf(self):
            return StructureSheaf(self)

        @cached_method
        def underlying_space(self):
            specialized = getattr(self, "_scheme_underlying_space", None)
            if specialized is not None:
                return specialized()
            return SchemeUnderlyingSpace(self)


class LocallyRingedSpaces(CategoryPacketMethods, Category):
    r"""Ringed spaces whose stalks are local rings."""

    @classmethod
    def _repr_object_names(cls):
        return "locally ringed spaces"

    def super_categories(self):
        return [RingedSpaces()]

    def __contains__(self, candidate) -> bool:
        return candidate in RingedSpaces()

    class ParentMethods:
        def stalk(self, point):
            return self.structure_sheaf().stalk(point)


__all__ = [
    "LocallyRingedSpaces",
    "RingedSpaces",
    "SchemeUnderlyingSpace",
    "StructureSheaf",
]
