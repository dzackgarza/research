r"""Dependency-light access to the canonical associative-algebra Mor owner.

``MatrixEndomorphismSpaces`` lives in the module tree but is also an
associative unital algebra under composition.  The module tree therefore
needs to name the algebra Mor construction without importing ``algebras.py``
while that file is itself importing modules.  This module supplies only that
late-binding category construction.  Its fixed Mor object is the ordinary
``MultiplicativeAlgebraMor``; there is no second associative-morphism
implementation or verification switch.
"""

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    MorCategoryConstruction,
)


class AssociativeAlgebraMorCategoryConstruction(MorCategoryConstruction):
    r"""The canonical multiplicative algebra Mor, imported after module startup."""

    def fixed_category_class_for(self, domain, codomain):
        _ = (domain, codomain)
        from dzack_research.preamble.categories.algebras.algebras import (
            MultiplicativeAlgebraMor,
        )

        return MultiplicativeAlgebraMor


__all__ = ["AssociativeAlgebraMorCategoryConstruction"]
