r"""``Lattices(R)``: projective modules carrying an $R$-valued bilinear form.

This category *is* ``SymmetricBilinearFormModules(R).Projective()``. It is
declared rather than composed: Sage models "this category, plus this axiom" as
the axiom's category class bound onto the category it refines, so a class that
names the pair and is bound with ``setattr`` is that join, under whatever name
suits it.  ``FramedModules`` is ``Modules(R).Framed()`` by the same device.

A lattice is not a module with a bilinear form.  That is
``SymmetricBilinearFormModules(R)``, and it holds anything with a pairing.
What makes a lattice is that the module is **projective**, which is why the
axiom sits on ``Modules`` and this category is its join with the form.

Nothing here is finitely generated, integral, or nondegenerate.  Those are
three further axioms, and declining to impose them is what lets this category
hold $\ZZ^{\infty}$ with the standard form, or $SL_2(\ZZ)$ inside
$SL_2(\RR)$ with $b(x,y)=\operatorname{tr}(xy)$.
"""

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring

from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    SymmetricBilinearFormModules,
)

# Imported for the registration and binding of the ``Projective`` axiom, which
# is what makes the declaration below resolve.
from dzack_research.preamble.categories.modules.pure.projective_modules import (  # noqa: F401
    ProjectiveModules,
)


class Lattices(CategoryWithAxiom_over_base_ring):
    r"""Category of lattices over a base ring."""

    _base_category_class_and_axiom = (SymmetricBilinearFormModules, "Projective")

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattices"


setattr(SymmetricBilinearFormModules, "Projective", Lattices)
