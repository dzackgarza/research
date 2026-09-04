"""Dependency-light bases for the owned mathematical category graph."""

from sage.categories.category import Category
from sage.misc.abstract_method import abstract_method


class OwnedCategory(Category):
    r"""Base class for categories belonging to the owned mathematical graph."""

    @abstract_method
    def an_object(self):
        r"""Return one object of this category.

        A witness that the category is inhabited, and the datum every construction
        parameterized by a category needs: where ``C`` takes an object of ``D``,
        ``C(D.an_object())`` builds one without the caller knowing anything else
        about ``D``.

        Distinct from ``an_element``, which every parent carries and which produces
        an element *of that object*.  This produces an object *of this category*.

        Sage's ``Category.example`` is not this operation: it looks for a template
        module under ``sage.categories.examples`` and returns the ``NotImplemented``
        singleton when it finds none, so it answers for Sage's graph and is silent
        where it should be loud.

        A contract on every owned category, not a default: exhibiting an inhabitant
        is per-category mathematics, and a category that cannot is a gap in that
        category.
        """

    class SubcategoryMethods:
        r"""Helpers every owned subcategory needs, a join included."""

        def _fold_construction(self, binary_construction, factors, *, name):
            r"""Return the construction over a finite family, from the binary one.

            A construction is taken over an index set, so the argument is an
            indexed family and never an arity (`CON-14`); a bare sequence of
            factors is normalized to the family on the canonical labels.  The
            binary construction the category supplies is folded over the family's
            values in index order, which is what associativity of these
            constructions entitles the caller to.
            """
            from dzack_research.preamble.categories.abstract_categories.products import (
                _finite_factor_family,
            )

            family = _finite_factor_family(factors, name=name)
            index_set = family.index_set()
            assert index_set.cardinality().is_finite(), (
                f"{name} over an infinite index set is defined, but the represented "
                "construction currently folds a finite family"
            )
            values = [family.value(index) for index in index_set]
            assert values, f"{name} requires at least one factor"
            result = values[0]
            for factor in values[1:]:
                result = binary_construction(result, factor)
            return result


class OwnedParameterizedCategory(OwnedCategory):
    r"""An owned category parameterized by one arbitrary mathematical object.

    The parameter is stored verbatim; this base performs no Sage-category
    membership test. Subclasses normalize their own parameters when needed.
    """

    def __init__(self, parameter) -> None:
        self._owned_parameter = parameter
        super().__init__()

    def parameter(self):
        return self._owned_parameter

    def base(self):
        return self.parameter()


class Objects(OwnedCategory):
    r"""The root of the owned mathematical category graph.

    This category carries no mathematical supercategory. Sage's own
    ``Objects``/``Sets`` categories remain runtime substrate only and are not
    semantic ancestors of owned categories.
    """

    def super_categories(self):
        return []

    @classmethod
    def _repr_object_names(cls):
        return "represented mathematical objects"


__all__ = [
    "Objects",
    "OwnedCategory",
    "OwnedParameterizedCategory",
]
