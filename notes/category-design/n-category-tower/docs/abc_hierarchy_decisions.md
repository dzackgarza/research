<!--
Origin: gitclones/integral_lattice/cat/docs/abc_hierarchy_decisions.md
Copied 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of
this corpus.
-->

# ABC Hierarchy Decisions

Actionable architectural decisions extracted from `abc_hierarchy_analysis.md`.

---

## Conceptual Foundation

### Cell vs Arrow vs Entity

| Concept | Definition | Role |
|---------|------------|------|
| **Cell** | A functor from a globe category G_n into C | External/abstract view |
| **Arrow** | Primitive notion intrinsic to C | Internal structure |
| **Entity** | Container/view with `as_arrow()` and `as_cell()` | User-facing type |

- A **cell** is a choice of functor `G_n → C` where `G_n` is the n-th globe category
- An **arrow** is the primitive morphism structure in C (composition, source, target)
- An **entity** (e.g., `_Morphism`) wraps both views: the functorial interpretation and the arrow structure

### n-Morphisms in Categories

Specific categories define **n-Morphisms** for `n = -1, 0, 1, 2`:

| n | n-Morphism | Description |
|---|------------|-------------|
| -1 | Element | Element of an object (if exists) |
| 0 | Object | 0-morphism = object in C |
| 1 | Morphism | 1-morphism = morphism in C |
| 2 | 2-Morphism | 2-morphism in a 2-category |

An **object** is a choice of cell `* → C` which picks out a 0-arrow.

---

## ABC Hierarchy

---

### Layer 0: Cell ABCs

```python
class _nCell(ABC):
    """n-cell. source/target are n-1-cells."""
    def source(self) -> _nCell | None: ...
    def target(self) -> _nCell | None: ...
    def is_invertible(self) -> BoolProof: ...

class _NegativeOneCell(_nCell, ABC):
    """(-1)-cell. The unique cell with no source or target."""
    def source(self) -> None: return None
    def target(self) -> None: return None

EMPTY_CELL = _NegativeOneCell()  # Singleton

class _ZeroCell(_nCell, ABC):
    """0-cell. source/target are empty."""
    def source(self) -> _NegativeOneCell: return EMPTY_CELL
    def target(self) -> _NegativeOneCell: return EMPTY_CELL

class _OneCell(_nCell, ABC):
    """1-cell. source/target are 0-cells."""
    @abstractmethod
    def source(self) -> _ZeroCell: ...
    @abstractmethod
    def target(self) -> _ZeroCell: ...

class _TwoCell(_nCell, ABC):
    """2-cell. source/target are 1-cells."""
    @abstractmethod
    def source(self) -> _OneCell: ...
    @abstractmethod
    def target(self) -> _OneCell: ...
```

---

### Layer 1: Arrow ABCs

Arrows are **primitive** to C (not extending cells).

```python
class _nArrow(ABC):
    """Arrow: primitive notion in C with dimension-specific operations."""
    @abstractmethod
    def amb(self) -> _Category_ABC: ...

class _NegativeOneArrow(_nArrow, ABC):
    """(-1)-arrow: element operations."""
    ...

class _ZeroArrow(_nArrow, ABC):
    """0-arrow: object operations."""
    @abstractmethod
    def identity_morphism(self) -> _OneArrow: ...

class _OneArrow(_nArrow, ABC):
    """1-arrow: morphism operations."""
    @abstractmethod
    def compose(self, other: Self) -> Self: ...
    @abstractmethod
    def is_surjective(self) -> BoolProof: ...
    @abstractmethod
    def is_injective(self) -> BoolProof: ...

class _TwoArrow(_nArrow, ABC):
    """2-arrow: 2-morphism operations."""
    @abstractmethod
    def vertical_compose(self, other: Self) -> Self: ...
    @abstractmethod
    def horizontal_compose(self, other: Self) -> Self: ...
```

### Category-Specific n-Morphisms

Each category defines n-morphisms for n = -1, 0, 1, 2. n-Morphisms **inherit from arrows** and have `as_cell()`.

**Template pattern**: Define `_Morphism_N_ABC` inheriting from arrow, with `as_cell()`, then export friendly names.

```python
# === n-Morphisms ===
class _Morphism_m1_ABC(_NegativeOneArrow, ABC):
    """(-1)-morphism: element of an object."""
    @override
    def as_cell(self) -> _NegativeOneCell: ...
    def parent_object(self) -> _Morphism_0_ABC: ...

class _Morphism_0_ABC(_ZeroArrow, ABC):
    """0-morphism: object in C."""
    @override
    def as_cell(self) -> _ZeroCell: ...
    def some_elements(self): ...

class _Morphism_1_ABC(_OneArrow, ABC):
    """1-morphism in C."""
    # Contexts:
    def __zero_arrow_class(self) -> Type[_Morphism_0_ABC]: ...
    def as_zero_arrow(self) -> _Morphism_0_ABC: ...
    # Methods
    def as_cell(self) -> _OneCell: ...
    def apply(self, x: Any) -> _Morphism_m1_ABC: ...

class _Morphism_2_ABC(_TwoArrow, ABC):
    """2-morphism in C."""
    # Contexts:
    def __zero_arrow_class(self) -> Type[_Morphism_0_ABC]: ...
    def as_zero_arrow(self) -> _Morphism_0_ABC: ...
    def __one_arrow_class(self) -> Type[_Morphism_1_ABC]: ...
    def as_one_arrow(self) -> _Morphism_1_ABC: ...
    # Methods
    def as_cell(self) -> _TwoCell: ...

# Friendly exports
Element = _Morphism_m1_ABC
Morphism = [_Morphism_0_ABC, _Morphism_1_ABC, _Morphism_2_ABC]
```

Defining functors:

```python

# Trivial morphisms
class _Identity_Morphism_As_ZeroArrow_ABC(Morphism[0], ABC):
    ...
    
class _Identity_Morphism_As_OneArrow_ABC(Morphism[1], ABC):
    ...

class _Identity_Morphism_As_TwoArrow_ABC(Morphism[2], ABC):
    ...

class IdentityMorphism:
    type m0 = _Identity_Morphism_As_ZeroArrow_ABC
    type m1 = _Identity_Morphism_As_OneArrow_ABC
    type m2 = _Identity_Morphism_As_TwoArrow_ABC

# Categories
class _Category_As_ZeroArrow_ABC(Morphism[0], ABC):
    def amb(self) -> Any: ...
    morphisms = ClassVar[tuple[
        Morphism[0],
        Morphism[1],
        Morphism[2]
    ]]
    def _zero_morphism_class(self) -> Type[Morphism[0]]: ...
    def _one_morphism_class(self) -> Type[Morphism[1]]: ...
    def _two_morphism_class(self) -> Type[Morphism[2]]: ...

class Category:
    type m0 = _Category_As_ZeroArrow_ABC
    type m1 = None
    type m2 = None

# Functors
class _Functor_As_ZeroArrow_ABC(Morphism[0], ABC):
    ...

class _Functor_As_OneArrow_ABC(Morphism[1], ABC):
    def apply_to_object(self, x: Object) -> Object: ...
    def apply_to_morphism(self, f: Morphism) -> Morphism: ...
    def is_faithful(self) -> BoolProof: ...
    def is_full(self) -> BoolProof: ...

class Functor:
    type m0 = _Functor_As_ZeroArrow_ABC
    type m1 = _Functor_As_OneArrow_ABC
    type m2 = None

# Natural transformations
class _Natural_Transformation_As_ZeroArrow_ABC(Morphism[0], ABC):
    ...

class _Natural_Transformation_As_OneArrow_ABC(Morphism[1], ABC):
    ...

class _Natural_Transformation_As_TwoArrow_ABC(Morphism[2], ABC):
    def component_at(self, x: Object) -> Morphism: ...
    def is_natural_isomorphism(self) -> BoolProof: ...

class Natural_Transformation:
    type m0 = _Natural_Transformation_As_ZeroArrow_ABC
    type m1 = _Natural_Transformation_As_OneArrow_ABC
    type m2 = _Natural_Transformation_As_TwoArrow_ABC

# Sets
class _Set_As_ZeroArrow_ABC(Category[0], ABC):
    def elements(self) -> Iterable[Any]: ...
    def as_category(self) -> Category: ...

class Set:
    type m0 = _Set_As_ZeroArrow_ABC
    type m1 = None
    type m2 = None

```

```python
# === Cat_w ===

class _CatW_Morphism_0_ABC(Category[0], ABC):
    """0-morphism in Cat_w: a category."""
    ...

class _CatW_Morphism_1_ABC(Functor[1], ABC):
    """1-morphism in Cat_w: a functor."""
    ...

class _CatW_Morphism_2_ABC(NaturalTransformation[2], ABC):
    """2-morphism in Cat_w: a natural transformation."""
    ...

class CatW:
    type m0 = _CatW_Morphism_0_ABC
    type m1 = _CatW_Morphism_1_ABC
    type m2 = _CatW_Morphism_2_ABC

class CatW(Category[0], ABC):
    morphisms = ClassVar[tuple[
        CatW_nMorphisms[0],
        CatW_nMorphisms[1],
        CatW_nMorphisms[2]
    ]]

    def _zero_morphism_class(self) -> Type[CatW_nMorphisms[0]]: ...
    def _one_morphism_class(self) -> Type[CatW_nMorphisms[1]]: ...
    def _two_morphism_class(self) -> Type[CatW_nMorphisms[2]]: ...

# === Set ===

class _Set_Morphism_0_ABC(Category[0], ABC):
    """0-morphism in Set: a set."""
    ...

class _Set_Morphism_1_ABC(Morphism[1], ABC):
    """1-morphism in Set: a set function."""
    ...

class _Set_Morphism_2_ABC(IdentityMorphism[2], ABC):
    """2-morphism in Set: identities."""
    ...

class Set:
    type m0 = _Set_Morphism_0_ABC
    type m1 = _Set_Morphism_1_ABC
    type m2 = _Set_Morphism_2_ABC

# Friendly exports
Category = CatW.m0
Functor = CatW.m1
NaturalTransformation = CatW.m2
Set = Set.m0
SetFunction = Set.m1
```

---

## Object Hierarchy

### Decision: Inheritance Chain for Objects

```
Object_In_A_1_Cat
    └── SetObject_ABC      — cardinality(), is_finite(), __iter__
            ├── GroupObject_ABC    — identity_element(), order()
            │       └── RingObject_ABC     — zero(), one(), characteristic()
            └── ModuleObject_ABC   — base_ring(), scalar_multiply()
```

**Rationale**: Methods propagate automatically. Semantic distinction captured by forgetful functors.

### Decision: Multiple Inheritance for Multiple Structures

Rings have two operations:
```python
class RingObject(SetObject, AbelianGroupMixin, MonoidMixin, ABC):
    def additive_group(self) -> GroupObject: ...
    def multiplicative_monoid(self) -> MonoidObject: ...
```

---

## Morphism Structure

### Decision: `as_arrow()` Delegation

Morphism classes return Arrow objects via `as_arrow()`:

```python
class GroupHomomorphism(_HomC_xy_0Cell_ABC):
    def as_arrow(self) -> OneArrow: ...

class GroupAutomorphism(GroupEndomorphism):
    def as_arrow(self) -> OneAutoArrow: ...  # Covariant refinement
```

Arrow hierarchy provides `is_invertible()`, `order()`, `inverse()`.

### Decision: Arrow Hierarchy Structure

```
_nArrow (base)
    ├── OneArrow   — compose(), is_injective(), kernel(), image()
    │       └── OneEndoArrow   — order(), is_idempotent()
    │               └── OneAutoArrow   — inverse()
    └── TwoArrow   — horizontal_compose(), vertical_compose()
            └── TwoEndoArrow
                    └── TwoAutoArrow
```

---

## View Methods

### Decision: Dimension-Shifting via `as_k_cell()`

Add to `_All_Cells_ABC`:

```python
def as_k_cell(self, k: int) -> CategoryABCs.Cell:
    """View n-cell as k-cell (0 <= k <= n-1) in related category."""
    ...
```

| Original | As | In Category |
|----------|-----|-------------|
| 1-cell f: X → Y in C | 0-cell | Hom_C(X, Y) |
| 2-cell η: f ⇒ g | 0-cell | Hom_{Arr(C)}(f, g) |

### Decision: Forgetful Functor Methods on Objects

```python
class GroupObject(SetObject):
    def as_set(self) -> SetObject: return self

class RingObject(GroupObject):
    def as_set(self) -> SetObject: return self
    def as_additive_group(self) -> GroupObject: return self
    def as_multiplicative_monoid(self) -> Object: ...
```

---

## Category-Specific Methods

### Decision: Each Category Implements Its Own Constructions

```python
class _ModuleMorphism_ABC(ABC):
    def kernel(self) -> CategoryABCs.ModuleObject: ...

class _GroupMorphism_ABC(ABC):
    def kernel(self) -> CategoryABCs.GroupObject: ...
```

**Rationale**: Types always correct. Shared utilities only for finitely-presented objects.

### Decision: Cat_w is Minimal

Cat_w provides:
- `fun(C, D)` → functor category
- `compose_functors(F, G)`
- `identity_functor(C)`

Cat_w does NOT provide:
- `is_abelian()`, `terminal_object_C()`, full predicate infrastructure

---

## Inheritance Principles

### Decision: What Inheritance Encodes

| Use Case | Mechanism |
|----------|-----------|
| Structural hierarchy (End ⊆ Hom) | Single inheritance |
| Multiple structures (Ring = AddGrp + MultMonoid) | Multiple inheritance from mixins |
| Different views of same data | View methods (`as_zero_cell()`, `as_arrow()`) |
| Shared algorithms | Utility functions called by category-specific methods |
| Dimension-specific behavior | Separate classes with shared base |

### Decision: What NOT to Do

- ✗ Single unified `Cell` class with dimension parameter (loses type safety)
- ✗ Pure composition where capabilities are objects (loses typing)
- ✗ Replacing inheritance with delegation (loses hierarchy encoding)

---

## Open Questions

### Q1: Monoid Objects?
Should `_MonoidObject_ABC` exist between `SetObject` and `GroupObject`?

### Q2: Generic Hom Categories?
Can we use `Generic[C]` to define `HomC[C]` once?
