r"""Projective modules over a base ring.

Defines the ``Projective`` axiom for ``Modules(R)``, enabling
``Modules(R).Projective()`` and ``ProjectiveModules(R)``.

$P$ is projective when it is a direct summand of a free module -- equivalently
when every surjection onto $P$ splits.  The axiom sits here, on modules, and
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

import sage.categories.category_with_axiom as cwa
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.category_types import Category_module
from sage.categories.modules import Modules
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from sage.misc.cachefunc import cached_method

if "Projective" not in cwa.all_axioms:
    cwa.all_axioms.add("Projective")


class ProjectiveModules(CategoryWithAxiom_over_base_ring):
    r"""Category of projective modules over a base ring."""

    _base_category_class_and_axiom = (Modules, "Projective")

    class ParentMethods:
        def is_projective(self) -> bool:
            r"""Return ``True``.

            Membership in this category is the statement; a module reaches it
            by being placed there, not by a test run at the call site.
            """
            return True


@cached_method
def _projective_subcategory(self: "Category") -> "Category":
    subcategory: "Category" = self._with_axiom("Projective")
    return subcategory


# Two bindings, as the sibling axioms do: the axiom category on ``Modules``,
# and the method on ``Category_module`` so every module category -- the
# form-bearing ones included -- can take the axiom.
setattr(Modules, "Projective", ProjectiveModules)
setattr(Category_module, "Projective", _projective_subcategory)
# The preamble's own parametrized categories are not ``Category_module``:
# ``OwnedCategoryOverBaseRing`` sits on ``Category_over_base_ring``, because
# ``Category_module`` also asserts ``AbelianCategory`` and the algebra
# categories in that family are not abelian.  Every member of the family is
# nonetheless a category of modules or of algebras, so each of them can be
# asked for its projective objects.
setattr(OwnedCategoryOverBaseRing, "Projective", _projective_subcategory)
