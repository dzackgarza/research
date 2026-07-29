r"""Discriminant quadratic modules.

Refine a ``TorsionQuadraticModule`` into this category to gain::

    gram_matrix()              # the form matrix for this category
    associated_bilinear_form() # the bilinear form attached to a quadratic module
    normal_form()              # new quadratic form in normal form
    _latex_()                  # multi-line display
    as_finitely_presented_group() # Sage-native FinitelyPresentedGroup
    abelian_group()               # Sage AbelianGroup (invariant factors)
    is_p_elementary(p)            # via abelian_group().permutation_group()

Elements gain::

    is_characteristic()        # q(x) = b(x, self) mod Z for all x

EXAMPLES::

    sage: from dzack_research.preamble import catalogue
    sage: from dzack_research.preamble.categories import DiscriminantQuadraticModules
    sage: A = Lattices.U.discriminant_group()
    sage: A._refine_category_(DiscriminantQuadraticModules())
"""

from typing import Any

from sage.categories.category import Category
from sage.rings.rational_field import QQ

class DiscriminantQuadraticModules(Category):
    r"""Category of discriminant quadratic modules.

    The category's ``gram_matrix`` is the quadratic Gram matrix. Its bilinear
    matrix is obtained from the associated bilinear form, not by duplicating the
    native method here.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "discriminant quadratic modules"

    def super_categories(self) -> list:
        return [DiscriminantBilinearModules()]

    class ParentMethods:
        r"""Methods available on discriminant quadratic modules."""

        def gram_matrix(self: Any) -> Any:
            r"""Return the quadratic Gram matrix with induced block subdivisions."""
            from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

            return TorsionQuadraticModule.gram_matrix_quadratic.f(self)

        def associated_bilinear_form(self: Any) -> Any:
            r"""Return this quadratic module's associated bilinear form."""
            from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

            raw = TorsionQuadraticModule.gram_matrix_bilinear.f(self)
            return DiscriminantBilinearForm(self.invariants(), self.source_lattice(), raw)

        def _form_matrix_latex_label(self: Any) -> str:
            r"""Return the LaTeX label for the quadratic Gram matrix."""
            return "G_{q_{A_L}}"

        def _form_matrix_latex_codomain(self: Any) -> str:
            r"""Return the LaTeX codomain for the quadratic Gram matrix entries."""
            return "\\mathbb{Q}/2\\mathbb{Z}"

        def normal_form(self: Any) -> Any:
            r"""Return this discriminant quadratic form in normal form."""
            from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

            norm = TorsionQuadraticModule.normal_form(self)
            norm.source_lattice = self.source_lattice
            return norm

    class ElementMethods:
        r"""Methods available on elements of discriminant quadratic modules."""

        def is_characteristic(self: Any) -> bool:
            r"""Return whether this discriminant element is characteristic.

            An element \(v^*\in A_L\) is characteristic when
            \(q(x)=b(x,v^*)\pmod{\mathbb Z}\) for every \(x\in A_L\).
            Sage's torsion quadratic values may live in ``Q/2Z`` while
            bilinear values live in ``Q/Z``, so the comparison is explicitly
            reduced modulo \(\mathbb Z\).
            """
            for x in self.parent():
                if not _equal_mod_integers(x.q(), x * self):
                    return False
            return True

# ---- internal helpers ----

def _equal_mod_integers(left: Any, right: Any) -> bool:
    r"""Return whether two torsion-form values agree modulo $\mathbb Z$."""
    return QQ(left.lift() - right.lift()) in ZZ

# ---- install: post-init hooks only ----

_DISCRIMINANT_GROUPS_INSTALLED = False


def install_discriminant_groups() -> None:
    """Hook post-init on torsion quadratic modules."""
    global _DISCRIMINANT_GROUPS_INSTALLED
    if _DISCRIMINANT_GROUPS_INSTALLED:
        return

    from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

    hook_post_init(TorsionQuadraticModule, DiscriminantQuadraticModules())
    _DISCRIMINANT_GROUPS_INSTALLED = True
