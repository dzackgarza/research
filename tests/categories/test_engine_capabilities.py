import pytest

from dzack_research.preamble.engine_capabilities import (
    EngineAbsence,
    EngineCapabilities,
    EngineCapabilityUnavailable,
)


def test_engine_capabilities_select_the_first_available_registered_realization() -> None:
    registry = EngineCapabilities()
    calls = []

    def absent_operation(value):
        calls.append(("absent", value))
        return value

    def exact_operation(value):
        calls.append(("exact", value))
        return value + 1

    registry.register(
        "example.operation",
        "absent-engine",
        absent_operation,
        available=lambda: False,
        provisioning="install the absent engine",
    )
    registry.register(
        "example.operation",
        "exact-engine",
        exact_operation,
        available=lambda: True,
        provisioning="ships with Sage",
    )

    assert registry.provider_names("example.operation") == (
        "absent-engine",
        "exact-engine",
    )
    assert registry.compute("example.operation", 4) == 5
    assert calls == [("exact", 4)]


def test_an_unprovisioned_engine_is_a_stated_absence_with_its_remedy() -> None:
    registry = EngineCapabilities()
    with pytest.raises(EngineCapabilityUnavailable) as unregistered:
        registry.compute("missing.operation")
    assert unregistered.value.capability == "missing.operation"
    assert unregistered.value.absent == ()

    registry.register(
        "present.operation",
        "unavailable-engine",
        lambda: None,
        available=lambda: False,
        provisioning="run `just setup` in the engine checkout",
    )
    with pytest.raises(EngineCapabilityUnavailable) as absent:
        registry.compute("present.operation")
    assert absent.value.absent == (
        EngineAbsence("unavailable-engine", "run `just setup` in the engine checkout"),
    )
