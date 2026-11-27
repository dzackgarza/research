"""Typed data kernel for category specification reports."""

from __future__ import annotations

from .categories import (
    CategorySpec as CategorySpec,
)
from .categories import (
    CategorySpecRegistry as CategorySpecRegistry,
)
from .constructor_adapters import (
    cat_constructor_registry as cat_constructor_registry,
)
from .constructor_adapters import (
    constructor_registry_for_category as constructor_registry_for_category,
)
from .constructors import (
    ConstructorRegistry as ConstructorRegistry,
)
from .constructors import (
    ConstructorSpec as ConstructorSpec,
)
from .inspection import Spec as Spec
from .reports import (
    ComputedValue as ComputedValue,
)
from .reports import (
    ConstructionWitness as ConstructionWitness,
)
from .reports import (
    SpecCheckResult as SpecCheckResult,
)
from .reports import (
    SpecObligation as SpecObligation,
)
from .reports import (
    SpecProvider as SpecProvider,
)
from .reports import (
    SpecRegistry as SpecRegistry,
)
from .reports import (
    SpecReport as SpecReport,
)
