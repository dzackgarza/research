r"""Dependency-light access to the canonical associative-algebra Hom owner.

``MatrixEndomorphismSpaces`` lives in the module tree but is also an
associative unital algebra under composition.  The module tree therefore
needs to name the algebra Hom construction without importing ``algebras.py``
while that file is itself importing modules.  This module supplies only that
late-binding category construction.  Its fixed Hom object is the ordinary
``MultiplicativeAlgebraHomset``; there is no second associative-morphism
implementation or verification switch.
"""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
)


class AssociativeAlgebraHomCategoryConstruction(HomCategoryConstruction):
    r"""The canonical multiplicative algebra Hom, imported after module startup."""

    def fixed_category_class_for(self, domain, codomain):
        _ = (domain, codomain)
        from dzack_research.preamble.categories.algebras.algebras import (
            MultiplicativeAlgebraHomset,
        )

        return MultiplicativeAlgebraHomset


__all__ = ["AssociativeAlgebraHomCategoryConstruction"]
