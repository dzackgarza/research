<!--
Origin: gitclones/integral_lattice/cat/docs/variance_issues.md
Copied 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of
this corpus.
-->


## Part X: Solving the Variance Problem

### The Problem

Python's type system enforces Liskov Substitution:
- Parameters are **contravariant** (can widen, not narrow)
- Returns are **covariant** (can narrow)

But when an ABC declares:
```python
class _Functor_ABC:
    def apply_to_object(self, x: _Object_ABC) -> _Object_ABC: ...
```

A concrete implementation MUST narrow:
```python
class ForgetfulFunctor(_Functor_ABC):
    def apply_to_object(self, x: GroupObject) -> SetObject: ...  # TYPE ERROR!
```

The type checker rejects this as a contravariance violation, even though it's **mathematically correct**.

Additionally, if a TypeVar `Obj` is used in both input and output positions, it becomes **invariant**, breaking subtyping entirely.

---

### The Solution: Decorator Metadata + `__init_subclass__` Verification

**Principle**: 
1. ABC methods use `Any` for types (so overrides are allowed)
2. Decorators store metadata about expected categorical relationships
3. `__init_subclass__` reads metadata from base class, verifies subclass overrides

**Step 1: Define the decorator**

```python
from typing import Any, get_type_hints
import inspect

def requires_signature(**expected):
    """Mark expected parameter/return types relative to category attributes.
    
    Usage:
        @requires_signature(x='SourceCategory.Object', returns='TargetCategory.Object')
        def apply_to_object(self, x): ...
    """
    def decorator(fn):
        fn._expected_signature = expected
        return fn
    return decorator
```

**Step 2: ABC declares methods with decorator**

```python
class _Functor_ABC(_Morphism_ABC):
    # Declared associated types (set by subclasses)
    SourceCategory: ClassVar[type[_Category_ABC]]
    TargetCategory: ClassVar[type[_Category_ABC]]
    
    @abstractmethod
    @requires_signature(x='SourceCategory.Object', returns='TargetCategory.Object')
    def apply_to_object(self, x: Any) -> Any:
        """Apply functor to an object. Signature verified at class definition."""
        ...
    
    @abstractmethod
    @requires_signature(f='SourceCategory.Morphism', returns='TargetCategory.Morphism')
    def apply_to_morphism(self, f: Any) -> Any:
        """Apply functor to a morphism. Signature verified at class definition."""
        ...
```

**Step 3: `__init_subclass__` verifies overrides**

```python
class _Functor_ABC(_Morphism_ABC):
    ...
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        verify_categorical_signatures(cls)

def verify_categorical_signatures(cls):
    """Verify that overridden methods have correct categorical types."""
    for name in dir(cls):
        # Walk MRO to find base method with _expected_signature
        for base in cls.__mro__[1:]:
            base_method = getattr(base, name, None)
            if callable(base_method) and hasattr(base_method, '_expected_signature'):
                expected = base_method._expected_signature
                override = getattr(cls, name)
                
                if override is base_method:
                    continue  # Not overridden, skip
                
                actual_hints = get_type_hints(override) if hasattr(override, '__annotations__') else {}
                verify_method_signature(cls, name, expected, actual_hints)
                break

def verify_method_signature(cls, method_name, expected, actual_hints):
    """Verify actual type hints match expected categorical types."""
    for param, expected_path in expected.items():
        if param == 'returns':
            actual_type = actual_hints.get('return')
        else:
            actual_type = actual_hints.get(param)
        
        if actual_type is None:
            continue  # No hint provided, can't verify
        
        # Resolve expected_path like 'SourceCategory.Object'
        expected_type = resolve_type_path(cls, expected_path)
        
        if expected_type and not is_compatible(actual_type, expected_type):
            raise TypeError(
                f"{cls.__name__}.{method_name}: "
                f"parameter '{param}' has type {actual_type}, "
                f"expected {expected_type} (from {expected_path})"
            )

def resolve_type_path(cls, path: str):
    """Resolve 'SourceCategory.Object' to the actual type."""
    parts = path.split('.')
    obj = cls
    for part in parts:
        obj = getattr(obj, part, None)
        if obj is None:
            return None
    return obj

def is_compatible(actual, expected):
    """Check if actual type is compatible with expected."""
    if actual is Any:
        return True
    try:
        return issubclass(actual, expected)
    except TypeError:
        return True  # Can't determine, assume ok
```

**Step 4: Concrete implementation**

```python
class ForgetfulFunctor_Grp_to_Set(_Functor_ABC):
    SourceCategory = Groups  # Groups.Object = GroupObject
    TargetCategory = Sets    # Sets.Object = SetObject
    
    def apply_to_object(self, x: GroupObject) -> SetObject:
        # __init_subclass__ verifies:
        # - x should be Groups.Object = GroupObject ✓
        # - return should be Sets.Object = SetObject ✓
        ...
    
    def apply_to_morphism(self, f: GroupHomomorphism) -> SetMorphism:
        ...
```

---

### How It Works

1. **At ABC definition**: `@requires_signature` stores expected type paths as metadata on method
2. **At subclass definition**: `__init_subclass__` runs automatically
3. **Verification**: For each method with `_expected_signature` in a base class:
   - Get the subclass's override
   - Read its type hints via `get_type_hints()`
   - Resolve expected paths (e.g., `'SourceCategory.Object'` → `GroupObject`)
   - Verify compatibility
4. **If mismatch**: Raise `TypeError` at import time

---

### Benefits

| Aspect | Benefit |
|--------|---------|
| Static type checking | Overrides with specific types are **accepted** (ABC uses `Any`) |
| Mathematical correctness | Verified at **class definition time** via `__init_subclass__` |
| Fails fast | Errors raised at **import**, not at method call |
| Lightweight | No per-call overhead, only runs once per class definition |
| Self-documenting | `@requires_signature` expresses intent in the ABC |
| No generics explosion | No need for `Generic[Obj, Mor, ...]` everywhere |

---

### Limitations

1. **Cannot verify missing type hints**: If implementer omits hints, verification is skipped
2. **Complex type expressions**: Union, Optional, etc. may need special handling
3. **Forward references**: May need `from __future__ import annotations` and careful resolution

---

### Alternative: Using `Annotated`

Instead of a separate decorator, embed metadata in the type:

```python
from typing import Annotated, Any

class CatType:
    """Marker for categorical type relationships."""
    def __init__(self, path: str):
        self.path = path

class _Functor_ABC:
    def apply_to_object(
        self, 
        x: Annotated[Any, CatType('SourceCategory.Object')]
    ) -> Annotated[Any, CatType('TargetCategory.Object')]:
        ...
```

`__init_subclass__` can extract `CatType` from `Annotated` metadata and verify the same way.

---

### Class-Level vs Instance-Level Source/Target

The pattern above assumes source/target categories are fixed at the **class level**:

```python
class ForgetfulFunctor_Grp_to_Set(_Functor_ABC):
    SourceCategory = Groups  # Fixed for all instances
    TargetCategory = Sets
```

But not all functors work this way. A **generic functor class** might have variable source/target per instance:

```python
class IdentityFunctor(_Functor_ABC):
    # source() and target() are instance-specific, not class-level
    def __init__(self, category: _Category_ABC):
        self._category = category
    
    def source(self) -> _Category_ABC:
        return self._category
    
    def target(self) -> _Category_ABC:
        return self._category
```

**Two verification strategies**:

---

#### Case 1: Class-Level Fixed (verified at class definition)

```python
class ForgetfulFunctor_Grp_to_Set(_Functor_ABC):
    SourceCategory = Groups
    TargetCategory = Sets
    
    def apply_to_object(self, x: GroupObject) -> SetObject: ...
    
    # __init_subclass__ verifies at import time
```

---

#### Case 2: Instance-Level Variable (verified at instantiation)

For functors where source/target vary per instance, use `__post_init__` or `__init__`:

```python
@dataclass
class IdentityFunctor(_Functor_ABC):
    _category: _Category_ABC
    
    def __post_init__(self):
        # Verify signature compatibility with this instance's categories
        verify_instance_signatures(self)
    
    def source(self) -> _Category_ABC:
        return self._category
    
    def target(self) -> _Category_ABC:
        return self._category
    
    def apply_to_object(self, x: Any) -> Any:
        # Can't statically type this — varies per instance
        return x

def verify_instance_signatures(functor):
    """Verify functor's methods are compatible with its instance-specific categories."""
    src = functor.source()
    tgt = functor.target()
    
    # For instance-level, we can't check static type hints
    # (they're fixed at class definition, not instance creation)
    # Instead, we verify that source/target have expected structure
    assert hasattr(src, 'Object'), f"{src} must have Object attribute"
    assert hasattr(tgt, 'Object'), f"{tgt} must have Object attribute"
```

---

#### Hybrid: Class Declares Categories, Instance Confirms

```python
class FunctorFromGrp(_Functor_ABC):
    """A functor from Groups to some target."""
    SourceCategory = Groups  # Fixed at class level
    # TargetCategory varies per instance
    
    def __init__(self, target_category: _Category_ABC):
        self._target = target_category
    
    def __post_init__(self):
        # Verify apply_to_object return type matches self._target.Object
        # at instance creation time
        ...
```

---

### Summary: When to Use Each Pattern

| Pattern | Source/Target | Verification Time | Type Hints |
|---------|---------------|-------------------|------------|
| Class-level `ClassVar` | Fixed per class | `__init_subclass__` (import) | Concrete types |
| Instance-level methods | Variable per instance | `__post_init__` (instantiation) | `Any` |
| Hybrid | Some fixed, some variable | Both | Mixed |

For most mathematical constructions (e.g., "the forgetful functor from Groups to Sets"), source/target are fixed at the class level and class-level verification works.

For generic constructions (e.g., "the identity functor on any category C"), instance-level verification is needed.

---

### Generalizing: Decorators for Category-Internal Type Relationships

The pattern extends beyond functors. **Any method** whose parameters/return types must relate to the category's own types can use decorators:

```python
class _Category_ABC(ABC):
    Object: ClassVar[type[_Object_ABC]]
    Morphism: ClassVar[type[_Morphism_ABC]]
    
    @signature(returns='self.Object')
    def random_object(self) -> Any:
        """Return type must be this category's Object type."""
        ...
    
    @signature(x='self.Object', y='self.Object', returns='self.Morphism')
    def hom(self, x: Any, y: Any) -> Any:
        """Parameters and return must match this category's types."""
        ...
    
    @signature(f='self.Morphism', returns='self.Object')
    def kernel(self, f: Any) -> Any:
        """f must be this category's Morphism, return is Object."""
        ...
    
    @signature(obj='self.Object', returns='self.EndC')
    def end_C(self, obj: Any) -> Any:
        """Endomorphism category of obj."""
        ...
```

**Concrete implementation**:

```python
class Groups(_Category_ABC):
    Object = GroupObject
    Morphism = GroupHomomorphism
    EndC = GroupEndomorphismCategory
    
    def random_object(self) -> GroupObject:
        # Verified: return type is Groups.Object ✓
        ...
    
    def hom(self, x: GroupObject, y: GroupObject) -> GroupHomomorphism:
        # Verified: x, y are Groups.Object, return is Groups.Morphism ✓
        ...
    
    def kernel(self, f: GroupHomomorphism) -> GroupObject:
        # Verified: f is Groups.Morphism, return is Groups.Object ✓
        ...
```

---

### Complete Decorator Implementation

```python
from typing import Any, get_type_hints, ClassVar
from abc import ABC, abstractmethod
import functools

def signature(**spec):
    """Decorator specifying expected parameter/return types as paths.
    
    Paths like 'self.Object' resolve to the class's Object attribute.
    
    Usage:
        @signature(x='self.Object', returns='self.Morphism')
        def some_method(self, x): ...
    """
    def decorator(fn):
        fn._signature_spec = spec
        return fn
    return decorator


def verify_all_signatures(cls):
    """Verify all methods with @signature decorators in cls."""
    for name in dir(cls):
        for base in cls.__mro__:
            base_method = getattr(base, name, None)
            if callable(base_method) and hasattr(base_method, '_signature_spec'):
                spec = base_method._signature_spec
                override = getattr(cls, name)
                
                if override is base_method:
                    continue  # Not overridden
                
                verify_against_spec(cls, name, spec, override)
                break


def verify_against_spec(cls, method_name, spec, method):
    """Verify method's type hints match spec."""
    try:
        hints = get_type_hints(method)
    except Exception:
        return  # Can't get hints, skip
    
    for param, path in spec.items():
        expected_type = resolve_path(cls, path)
        if expected_type is None:
            continue
        
        if param == 'returns':
            actual_type = hints.get('return')
        else:
            actual_type = hints.get(param)
        
        if actual_type is None or actual_type is Any:
            continue  # Not specified or Any, skip
        
        if not is_subclass_safe(actual_type, expected_type):
            raise TypeError(
                f"{cls.__name__}.{method_name}: "
                f"'{param}' has type {actual_type.__name__}, "
                f"expected {expected_type.__name__} (from {path})"
            )


def resolve_path(cls, path: str):
    """Resolve 'self.Object' to cls.Object."""
    if path.startswith('self.'):
        attr_name = path[5:]  # Remove 'self.'
        return getattr(cls, attr_name, None)
    return None


def is_subclass_safe(actual, expected):
    """Check if actual is a subclass of expected, handling edge cases."""
    try:
        return issubclass(actual, expected)
    except TypeError:
        return True  # Can't determine, assume ok
```

---

### ABC Base with Verification

```python
class _Category_ABC(ABC):
    Object: ClassVar[type[_Object_ABC]]
    Morphism: ClassVar[type[_Morphism_ABC]]
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        verify_all_signatures(cls)
    
    @abstractmethod
    @signature(returns='self.Object')
    def random_object(self) -> Any: ...
    
    @abstractmethod
    @signature(f='self.Morphism', returns='self.Object')
    def kernel(self, f: Any) -> Any: ...
```

**Benefits**:
- Every category method can express type relationships via `@signature`
- Concrete categories declare `Object`, `Morphism`, etc. as class attributes
- `__init_subclass__` verifies at import time
- No generics explosion — just decorator metadata + verification
