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


class _ConstructionEngine:
    def __init__(self, engine_value, **rest):
        self._engine_value = engine_value
        super().__init__(**rest)

    def engine_value(self):
        return self._engine_value

    def reading(self):
        return "engine"


class _ElementEngine:
    def engine_reading(self):
        return "engine element"


class StrongerConstructionCategory(OwnedCategory):
    def super_categories(self):
        return [OpenConstructionCategory()]

    class ParentMethods:
        def __init__(self, stronger_value, **rest):
            self._stronger_value = stronger_value
            super().__init__(**rest)

        def reading(self):
            return "stronger"

        def stronger_value(self):
            return self._stronger_value


def test_engine_realization_keeps_the_declared_category_and_stronger_methods() -> None:
    owner = OpenConstructionCategory()
    category = StrongerConstructionCategory()
    engine = (owner, _ConstructionEngine, _ElementEngine)
    obj = _object_of(category, _engine=engine, required_value=3, engine_value=5, stronger_value=7)
    other = _object_of(category, _engine=engine, required_value=11, engine_value=13, stronger_value=17)

    assert obj.category() is category
    assert obj in category and obj in owner
    assert obj.required_value() == 3
    assert obj.engine_value() == 5
    assert obj.stronger_value() == 7
    assert obj.reading() == "stronger"
    assert other.engine_value() == 13
    assert type(obj) is type(other)
    assert issubclass(obj.element_class, category.ElementType)
    assert issubclass(obj.element_class, _ElementEngine)


def test_engine_constructor_parameters_are_checked_at_the_same_entry() -> None:
    owner = OpenConstructionCategory()
    engine = (owner, _ConstructionEngine, _ElementEngine)
    with pytest.raises(TypeError, match="engine_value"):
        _object_of(owner, _engine=engine, required_value=3)
    obj = _object_of(owner, _engine=engine, required_value=3, engine_value=5)
    assert obj.reading() == "engine"


def test_engine_methods_do_not_enter_the_category_itself() -> None:
    category = OpenConstructionCategory()
    plain = _object_of(category, required_value=3)
    realized = _object_of(
        category,
        _engine=(category, _ConstructionEngine, _ElementEngine),
        required_value=3,
        engine_value=5,
    )
    assert plain.category() is realized.category()
    assert not issubclass(type(plain), _ConstructionEngine)
    assert issubclass(type(realized), _ConstructionEngine)
