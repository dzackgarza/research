r"""Complete linear systems represented by their section spaces."""

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.categories.schemes.schemes import (
    ProjectiveSchemes,
    ProjectiveSpace,
    Schemes,
    refine_scheme,
)


class CompleteLinearSystems(OwnedCategoryOverBaseRing):
    r"""Projective spaces ``|D| = P(H^0(X,O_X(D)))`` with their defining data."""

    @classmethod
    def _repr_object_names(cls):
        return "complete linear systems"

    def super_categories(self):
        return [ProjectiveSchemes(self.base_ring())]

    class ParentMethods:
        def linear_system_scheme(self):
            return self._preamble_linear_system_scheme

        def linear_system_divisor(self):
            return self._preamble_linear_system_divisor

        def section_space(self):
            return self._preamble_linear_system_section_space

        def projective_dimension(self):
            return self.relative_dimension()


def CompleteLinearSystem(scheme, divisor, section_space):
    r"""Return the complete linear system of ``divisor`` on ``scheme``.

    The represented convention is the projective space of nonzero global
    sections modulo scalars.  Hence a section space of dimension ``r`` gives
    ``P^(r-1)``; the empty section space has no projectivization and is refused.
    """
    base = scheme.scheme_base_ring()
    if scheme not in Schemes(base):
        raise TypeError("a complete linear system requires a represented scheme")
    if section_space.base_ring() is not base:
        raise ValueError("the section space must be over the scheme base field")
    dimension = int(section_space.dimension())
    if dimension == 0:
        raise ValueError("the empty linear system has no represented projective space")
    system = ProjectiveSpace(dimension - 1, base)
    system._preamble_linear_system_scheme = scheme
    system._preamble_linear_system_divisor = divisor
    system._preamble_linear_system_section_space = section_space
    return refine_scheme(system, base, [CompleteLinearSystems(base)])


__all__ = ["CompleteLinearSystem", "CompleteLinearSystems"]
