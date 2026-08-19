# Origin: gitclones/integral_lattice/cat/src/local_typing.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.


from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from dataclasses import dataclass, field
from enum import Enum, auto
from functools import cached_property, reduce
from typing import (Annotated, Any, Generic, Literal, NamedTuple, Never, Protocol,
                    Self, TypeAlias, TypeGuard, TypeIs, TypeVar, assert_never,
                    cast, final, get_args, overload, override, runtime_checkable, TYPE_CHECKING)

from pydantic import NonNegativeInt