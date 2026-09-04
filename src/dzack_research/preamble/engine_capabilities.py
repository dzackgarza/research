r"""Private selection of computational realizations for exact operations.

Mathematical objects do not depend on this registry for identity or category
placement.  They ask for an operation; registered private providers decide
which external engine realizes that computation and return ordinary data that
is crossed back into owned objects by the caller.
"""

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass


class EngineCapabilityUnavailable(RuntimeError):
    r"""Raised when no registered computational realization is available."""


@dataclass(frozen=True)
class EngineProvider:
    r"""One private realization of a named exact computational operation."""

    name: str
    operation: Callable
    available: Callable[[], bool]


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
        available: Callable[[], bool] = lambda: True,
    ) -> None:
        if not capability or not provider:
            raise ValueError("a computational capability and provider need nonempty names")
        if not callable(operation) or not callable(available):
            raise TypeError("a computational provider needs callable operation and availability")
        providers = self._providers[capability]
        if any(candidate.name == provider for candidate in providers):
            raise ValueError(
                f"provider {provider!r} is already registered for capability {capability!r}"
            )
        providers.append(EngineProvider(provider, operation, available))

    def provider_names(self, capability: str) -> tuple[str, ...]:
        return tuple(provider.name for provider in self._providers.get(capability, ()))

    def compute(self, capability: str, /, *args, **kwargs):
        providers = self._providers.get(capability, ())
        if not providers:
            raise EngineCapabilityUnavailable(
                f"no computational realization is registered for {capability!r}"
            )
        unavailable = []
        for provider in providers:
            if not provider.available():
                unavailable.append(provider.name)
                continue
            return provider.operation(*args, **kwargs)
        names = ", ".join(unavailable)
        raise EngineCapabilityUnavailable(
            f"no available computational realization for {capability!r}; "
            f"registered providers: {names}"
        )


engine_capabilities = EngineCapabilities()


__all__ = [
    "EngineCapabilities",
    "EngineCapabilityUnavailable",
    "EngineProvider",
    "engine_capabilities",
]
