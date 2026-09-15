import pytest

from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.owned_category import _construction_contract, _object_of


class ClosedConstructionCategory(OwnedCategory):
    def super_categories(self):
        return [Objects()]

    def an_object(self):
        return _object_of(self, required_value=0)

    class ParentMethods:
        def __init__(self, required_value, optional_value=1):
            self._required_value = required_value
            self._optional_value = optional_value

        def required_value(self):
            return self._required_value

        def optional_value(self):
            return self._optional_value


class OpenConstructionCategory(OwnedCategory):
    def super_categories(self):
        return [Objects()]

    def an_object(self):
        return _object_of(self, required_value=0)

    class ParentMethods:
        def __init__(self, required_value, **rest):
            self._required_value = required_value
            super().__init__(**rest)

        def required_value(self):
            return self._required_value


def test_closed_contract_requires_named_data_before_construction() -> None:
    category = ClosedConstructionCategory()
    contract = _construction_contract(category)

    assert contract.required_names() == frozenset({"required_value"})
    assert contract.optional_names() == frozenset({"optional_value"})
    assert not contract.is_open()
    with pytest.raises(TypeError, match="required_value"):
        _object_of(category)


def test_closed_contract_rejects_undeclared_data() -> None:
    category = ClosedConstructionCategory()

    with pytest.raises(TypeError, match="undeclared data: stray"):
        _object_of(category, required_value=2, stray=3)


def test_open_contract_still_requires_its_named_data_but_forwards_the_rest() -> None:
    category = OpenConstructionCategory()
    contract = _construction_contract(category)

    assert contract.required_names() == frozenset({"required_value"})
    assert contract.is_open()
    with pytest.raises(TypeError, match="required_value"):
        _object_of(category, stray=3)


def test_existing_object_construction_uses_the_same_contract() -> None:
    category = OpenConstructionCategory()
    obj = _object_of(category, required_value=7)

    assert obj.required_value() == 7
