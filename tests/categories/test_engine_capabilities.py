import pytest

from dzack_research.preamble.engine_capabilities import (
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
    )
    registry.register("example.operation", "exact-engine", exact_operation)

    assert registry.provider_names("example.operation") == (
        "absent-engine",
        "exact-engine",
    )
    assert registry.compute("example.operation", 4) == 5
    assert calls == [("exact", 4)]


def test_engine_capabilities_fail_loudly_when_no_realization_is_available() -> None:
    registry = EngineCapabilities()
    with pytest.raises(EngineCapabilityUnavailable, match="no computational realization"):
        registry.compute("missing.operation")

    registry.register(
        "present.operation",
        "unavailable-engine",
        lambda: None,
        available=lambda: False,
    )
    with pytest.raises(EngineCapabilityUnavailable, match="unavailable-engine"):
        registry.compute("present.operation")
