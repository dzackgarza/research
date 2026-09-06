r"""Private selection of computational realizations for exact operations.

Mathematical objects do not depend on this registry for identity or category
placement.  They ask for an operation; registered private providers decide
which external engine realizes that computation and return ordinary data that
is crossed back into owned objects by the caller.

An engine that is not provisioned is a stated absence: the refusal names the
capability, every registered provider that is absent, and the command that
provisions each one.  Nothing here substitutes another engine silently.
"""

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class EngineProvider:
    r"""One private realization of a named exact computational operation.

    ``provisioning`` is the command a user runs to make this provider
    available; it is quoted whenever the provider is absent.
    """

    name: str
    operation: Callable
    available: Callable[[], bool]
    provisioning: str


@dataclass(frozen=True)
class EngineAbsence:
    r"""A registered provider that is not provisioned, with its remedy."""

    provider: str
    provisioning: str


class EngineCapabilityUnavailable(RuntimeError):
    r"""No registered computational realization of ``capability`` is available."""

    def __init__(self, capability: str, absent: tuple[EngineAbsence, ...]) -> None:
        self.capability = capability
        self.absent = absent
        if not absent:
            message = f"no computational realization is registered for {capability!r}"
        else:
            statements = "; ".join(
                f"{absence.provider} is not provisioned ({absence.provisioning})"
                for absence in absent
            )
            message = f"no available computational realization for {capability!r}: {statements}"
        super().__init__(message)


class EngineCapabilities:
    r"""Ordered private providers for named exact computational operations."""

    def __init__(self) -> None:
        self._providers: dict[str, list[EngineProvider]] = defaultdict(list)

    def register(
        self,
        capability: str,
        provider: str,
        operation: Callable,
        *,
        available: Callable[[], bool],
        provisioning: str,
    ) -> None:
        assert capability and provider, "a computational capability and provider need nonempty names"
        assert provisioning, f"provider {provider!r} must state how it is provisioned"
        providers = self._providers[capability]
        assert all(candidate.name != provider for candidate in providers), (
            f"provider {provider!r} is already registered for capability {capability!r}"
        )
        providers.append(EngineProvider(provider, operation, available, provisioning))

    def provider_names(self, capability: str) -> tuple[str, ...]:
        return tuple(provider.name for provider in self._providers.get(capability, ()))

    def compute(self, capability: str, /, *args, **kwargs):
        absent = []
        for provider in self._providers.get(capability, ()):
            if not provider.available():
                absent.append(EngineAbsence(provider.name, provider.provisioning))
                continue
            return provider.operation(*args, **kwargs)
        raise EngineCapabilityUnavailable(capability, tuple(absent))


engine_capabilities = EngineCapabilities()


__all__ = [
    "EngineAbsence",
    "EngineCapabilities",
    "EngineCapabilityUnavailable",
    "EngineProvider",
    "engine_capabilities",
]
