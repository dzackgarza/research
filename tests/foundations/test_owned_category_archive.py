r"""Archive reconciliation for category-owned implementation types.

The archive introduced the category-owned object implementation protocol.  The
live runtime preserves that protocol and strengthens it with deterministic
category-graph ordering and validated construction contracts.  These
specimens record the three semantic invariants the archived public surface
carried: inherited implementation declarations remain visible, categories
are objects of ``Cat``, and ``_object_of`` constructs the category's own object
type without changing category identity.
"""

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import (
    OwnedCategoryObject,
    declared_implementation_types,
    _object_of,
)
from dzack_research.preamble.owned_category_bases import (
    Category as OwnedCategoryBase,
)
from dzack_research.preamble.owned_category_bases import (
    MorCategoryConstruction,
)

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/owned_category.py",
        "live_owner": "src/dzack_research/preamble/owned_category.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/owned_category_bases.py",
        "live_owner": "src/dzack_research/preamble/owned_category_bases.py",
        "disposition": "reconciled-live-owner",
    },
)


class _DeclarationBase:
    class ParentMethods:
        def base_operation(self):
            return "base"


class _DeclarationDerived(_DeclarationBase):
    class ParentMethods:
        def derived_operation(self):
            return "derived"


class _ArchiveConstructionCategory(OwnedCategory):
    def an_object(self):
        return _object_of(self, archive_value=0)

    class ParentMethods:
        def __init__(self, archive_value, **rest):
            self._archive_value = archive_value
            super().__init__(**rest)

        def archive_value(self):
            return self._archive_value


def test_declared_implementation_types_retain_the_outer_class_graph() -> None:
    provider, inherited = declared_implementation_types(
        _DeclarationDerived,
        ("ParentMethods",),
    )

    assert provider is _DeclarationDerived.ParentMethods
    assert inherited == (_DeclarationBase.ParentMethods,)


def test_owned_categories_are_objects_of_cat() -> None:
    category = Sets()

    assert isinstance(category, OwnedCategoryObject)
    assert category.category() is Cat()


def test_object_of_constructs_the_category_object_type_with_literal_identity() -> None:
    category = _ArchiveConstructionCategory()
    obj = _object_of(category, archive_value=7)

    assert isinstance(obj, category.ObjectType)
    assert obj.category() is category
    assert obj.archive_value() == 7


def test_owned_category_base_shapes_remain_in_the_owned_cat_graph() -> None:
    sets = Sets()
    mor_category = sets.MorCategory()

    assert isinstance(sets, OwnedCategoryBase)
    assert isinstance(mor_category, MorCategoryConstruction)
    assert sets.category() is Cat()
    assert mor_category.category() is Cat()
