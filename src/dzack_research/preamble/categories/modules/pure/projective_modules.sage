r"""Projective modules over a base ring.

``ProjectiveModules(R)`` is the owned category; it consumes the preamble's own
``Modules(R)`` as its supercategory.

$P$ is projective when it is a direct summand of a free module -- equivalently
when every surjection onto $P$ splits.  The category sits here, on modules, and
not on anything form-bearing: projectivity is a statement about the module and
says nothing about a pairing.

It is what separates a lattice from a module carrying a bilinear form.  Over a
PID the two coincide with freeness, which is why the distinction can be missed
by working only over $\ZZ$; over a Dedekind domain that is not principal a
projective module of rank one need not be free, and over a general ring the
gap is wider still.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Module

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing


class ProjectiveModules(OwnedCategoryOverBaseRing):
    r"""Category of projective modules over a base ring."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "projective modules"

    def super_categories(self) -> list:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_projective(self) -> bool:
            r"""Return ``True``.

            Membership in this category is the statement; a module reaches it
            by being placed there, not by a test run at the call site.
            """
            return True
