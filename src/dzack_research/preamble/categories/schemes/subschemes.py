"""Owned closed-subsheme structure."""

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.schemes import (
    Schemes,
    _has_scheme_placement,
    refine_scheme,
    refine_scheme_morphism,
)


class ClosedSubschemes(OwnedCategoryOverBaseRing):
    r"""Closed subschemes equipped with their ambient closed immersion."""

    def _repr_object_names(self):
        return f"closed subschemes over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        return (
            candidate in Schemes(self.base_ring())
            and _has_scheme_placement(candidate, ClosedSubschemes)
        )

    class ParentMethods:
        def ambient_scheme(self):
            ambient = getattr(self, "_preamble_ambient_scheme", None)
            return self.ambient_space() if ambient is None else ambient

        def inclusion(self):
            morphism = self.embedding_morphism()
            return refine_scheme_morphism(morphism, self.scheme_base_ring())

        def codimension(self):
            return self.ambient_scheme().dimension() - self.dimension()

        def defining_equations(self):
            return tuple(self.defining_polynomials())

        def defining_ideal_owned(self):
            return self.defining_ideal()


class EquationDefinedClosedSubschemes(OwnedCategoryOverBaseRing):
    def _repr_object_names(self):
        return f"equation-defined closed subschemes over {self.base_ring()}"

    def super_categories(self):
        return [ClosedSubschemes(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        return (
            candidate in ClosedSubschemes(self.base_ring())
            and _has_scheme_placement(candidate, EquationDefinedClosedSubschemes)
        )


class OpenSubschemes(OwnedCategoryOverBaseRing):
    r"""Open subschemes equipped with their open immersion."""

    def _repr_object_names(self):
        return f"open subschemes over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        return (
            candidate in Schemes(self.base_ring())
            and _has_scheme_placement(candidate, OpenSubschemes)
        )


def refine_closed_subscheme(subscheme, ambient=None):
    ambient = subscheme.ambient_space() if ambient is None else ambient
    base = ambient.scheme_base_ring()
    subscheme._preamble_ambient_scheme = ambient
    return refine_scheme(
        subscheme,
        base,
        [ClosedSubschemes(base), EquationDefinedClosedSubschemes(base)],
    )


__all__ = [
    "ClosedSubschemes",
    "EquationDefinedClosedSubschemes",
    "OpenSubschemes",
    "refine_closed_subscheme",
]
