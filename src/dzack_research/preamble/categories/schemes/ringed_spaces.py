"""Owned ringed-space structure used by the scheme hierarchy."""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoryPacketMethods,
)
from dzack_research.preamble.categories.sets import Sets


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
        scheme = self.scheme()
        base_ring = scheme.scheme_base_ring()
        from dzack_research.preamble.categories.rings import own_ring
        from dzack_research.preamble.categories.schemes.schemes import (
            AffineSchemes,
            ProjectiveSpaces,
        )

        if scheme in AffineSchemes(base_ring):
            return own_ring(scheme.coordinate_ring())
        if scheme in ProjectiveSpaces(base_ring):
            return base_ring
        raise NotImplementedError(
            f"global sections of the structure sheaf of {scheme} are not yet represented"
        )

    sections = global_sections

    def sections_on_distinguished_open(self, distinguished_open):
        r"""Return ``O_X(D(f)) = Gamma(X,O_X)_f`` for an affine scheme."""
        scheme = self.scheme()
        base_ring = scheme.scheme_base_ring()
        from dzack_research.preamble.categories.schemes.schemes import AffineSchemes

        if scheme not in AffineSchemes(base_ring):
            raise NotImplementedError(
                "distinguished-open structure-sheaf sections are represented for affine schemes"
            )
        spectrum = scheme.underlying_space()
        if distinguished_open.codomain() is not spectrum:
            raise ValueError("the distinguished open belongs to a different affine spectrum")
        return distinguished_open.coordinate_ring()

    def stalk(self, point):
        r"""Return ``O_{X,p}`` for a represented affine prime point."""
        scheme = self.scheme()
        base_ring = scheme.scheme_base_ring()
        from dzack_research.preamble.categories.schemes.schemes import AffineSchemes

        if scheme not in AffineSchemes(base_ring):
            raise NotImplementedError(
                "the active stalk construction is represented on affine schemes"
            )
        spectrum = scheme.underlying_space()
        if getattr(point, "parent", lambda: None)() is not spectrum:
            point = spectrum(point)
        return point.local_ring()

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
            from dzack_research.preamble.categories.rings import own_ring
            from dzack_research.preamble.categories.schemes.schemes import AffineSchemes

            base_ring = self.scheme_base_ring()
            if self in AffineSchemes(base_ring):
                return own_ring(self.coordinate_ring()).spectrum()
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
