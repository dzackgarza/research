<!--
Origin: gitclones/integral_lattice/cat/docs/abc_hierarchy_analysis.md
Copied 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of
this corpus.
-->

# ABC Class Hierarchy Architecture Analysis

## Executive Summary

This document analyzes the design of the ABC class hierarchy to optimize **category creation UX**. The core complexity can be as intricate as needed; what matters is:

1. **Creating a new category C should be trivial** — click "implement all unimplemented methods" in VSCode and get a complete scaffold
2. **New categories automatically inherit solved problems** — e.g., Rings shouldn't redefine `cardinality()`
3. **If instantiation succeeds, the framework works** — strong guarantees from ABC enforcement
4. **Cat_w is a minimal container** — handles functor categories but doesn't require full category methods

---

## Part I: Topological Foundation

### Cells as Maps from Cubes

An n-cell `C` in X can be understood as an element of `[I^n, X]`, and can be "shifted":

```
C ∈ [I^n, X] = [I^{n-1}, X^I] = ... = [*, X^{I^n}]
```

**Key insight**: An n-cell can be viewed as a k-cell (for any k ≤ n) by changing the ambient category.

Examples:
- A **1-cell** (morphism) `f: X → Y` in C is a 0-cell in `Hom_C(X, Y)`
- A **2-cell** (modification) `α: f ⇒ g` is a 0-cell in the appropriate higher hom-category
- A **functor** F: C → D is a 1-cell in Cat_w but a 0-cell in Fun(C, D)

### Implication for Design

**A cell is not intrinsically an n-cell** — it has underlying data (set, callable, matrix, etc.) and **"Cell" is a choice of how to view that data** within some ambient structure.

The `as_zero_cell()`, `as_one_cell()`, `as_arrow()` methods encode this shifting:

```python
class _HomC_xy_0Cell_ABC(ABC):
    """A morphism f: X → Y in C, viewed as a 0-cell in Hom_C(X,Y)."""
    
    def as_zero_cell(self) -> CategoryABCs.Cell:
        """Self as 0-cell in Hom_C(X,Y)."""
        ...
    
    def as_one_cell(self) -> CategoryABCs.Cell:
        """Same underlying data, viewed as 1-cell in C."""
        ...
    
    def as_arrow(self) -> OneArrow:
        """Same data, viewed as pure arrow structure."""
        ...
```

The **underlying data is fixed**; only the interpretation changes.

---

## Part II: Existing Architecture

### Cell Hierarchy (`cells.py`)

```python
class _All_Cells_ABC(ABC):
    def source(self) -> CategoryABCs.Cell: ...
    def target(self) -> CategoryABCs.Cell: ...
    def path(self) -> Sequence[CategoryABCs.Cell]: ...
    def cell_dimension(self) -> int: ...
    def container(self) -> CellContainer: ...

class _ZeroCell(_All_Cells_ABC): ...
class _OneCell(_All_Cells_ABC): ...
class _TwoCell(_All_Cells_ABC): ...
```

### Arrow Hierarchy (`abstract_arrows.py`)

Two independent axes combined via multiple inheritance:

**Axis 1: Dimension**
```
_nArrow (base)
    ├── OneArrow   (1-cell: f: X → Y) — is_injective(), kernel(), image()
    └── TwoArrow   (2-cell: α: f ⇒ g) — horizontal_compose(), vertical_compose()
```

**Axis 2: Structure**
```
_nArrow
    └── _EndoArrow   (domain = codomain) — order(), is_idempotent(), to_power()
            └── _AutoArrow   (invertible) — inverse()
```

**Combined:**
```python
class OneEndoArrow(OneArrow, _EndoArrow): ...
class OneAutoArrow(OneEndoArrow, _AutoArrow): ...
class TwoEndoArrow(TwoArrow, _EndoArrow): ...
class TwoAutoArrow(TwoEndoArrow, _AutoArrow): ...
```

This already captures dimension + endo/auto structure in a factored way.

### Three-Layer Architecture (from README.md)

```
Stage 1: ABCs (src/abc_specs/)
    - Pure interface specification
    - All methods are @final @abstractmethod
    - No implementations

Stage 2: Bases (src/abc/bases/)  
    - Partial implementations from abstract structure
    - @override @final on all methods
    - No new methods beyond ABCs

Stage 3: Concrete (src/abc/concrete/)
    - Full implementations
    - Inherit from bases
    - Scaffold pattern: category.py ties together objects.py + homs/ + limits/
```

### Scaffold Pattern for New Categories

```
mycategory/
    homs/
        homC.py      # extends CategoryBases.HomC, CategoryBases.HomC_xy
        endC.py      # extends CategoryBases.EndC, CategoryBases.EndC_x
        autC.py      # extends CategoryBases.AutC, CategoryBases.AutC_x
        morphisms.py # extends CategoryBases.Morphism, Endomorphism, Automorphism
    limits/
        limits.py    # Slice, Span, Product, Pullback, Terminal
        colimits.py  # Coslice, Cospan, Coproduct, Pushout, Initial
        direct_sums.py
        tensor_products.py
    objects.py       # extends CategoryBases.Object
    category.py      # extends CategoryBases.Category (attaches all above)
```

---

## Part III: Design Requirements

### What a New Category C Must Provide

| Requirement | How ABCs Enforce It |
|-------------|---------------------|
| C is a 0-cell in Cat_w | Inherit from `CategoryABCs.Nontrivial_TwoCategory` |
| C has its own 0-cells (objects) | Implement `object_class()` returning ABC-inheriting class |
| C has its own 1-cells (morphisms) | Implement `morphism_class()` returning ABC-inheriting class |
| Objects implement common interface | Object class inherits from `CategoryABCs.Object` |
| Morphisms implement common interface | Morphism class inherits from `CategoryABCs.OneMorphism` |
| Endo/auto morphisms have more structure | Inherit from `CategoryABCs.EndoOneMorphism` / `AutoOneMorphism` |
| C can produce Hom_C, Hom_C(x,y), End_C(x), Aut_C(x) | Inherit from hom-category mixins |
| 1-cells in C can be viewed as 0-cells in Hom_C(x,y) | Implement `as_zero_cell()` method |

### The VSCode Scaffolding Workflow

```
1. Create new file: src/abc/concrete/my_category/category.py
2. Write: class MyCategory(CategoryBases.Category): ...
3. VSCode shows: "Implement all abstract methods" (red squiggle)
4. Click to scaffold ALL required methods
5. Fill in implementations
6. If class instantiates → it works correctly with framework
```

This workflow requires:
- **All required methods are `@abstractmethod`** in ABCs
- **Base classes provide sensible defaults** where possible
- **Type annotations guide the implementation**

---

## Part IV: Architectural Decisions

### Decision 1: Object Hierarchy via Inheritance

**Question**: How should `SetObject`, `GroupObject`, `RingObject`, etc. relate?

**Mathematical reality**:
```
Set ⊃ Group ⊃ Ring
    (forgetful functors)
```

**Design options**:

| Approach | How `cardinality()` Works for GroupObject | Trade-off |
|----------|-------------------------------------------|-----------|
| **A. Inheritance chain** | GroupObject extends SetObject → inherits directly | Clean for users; conflates "group" with "underlying set" |
| **B. Composition** | GroupObject has `as_set() → SetObject`; call `g.as_set().cardinality()` | Mathematically precise; verbose for users |
| **C. Mixin + delegation** | `HasUnderlyingSet` mixin provides `cardinality()` that delegates to abstract `underlying_set()` | Balance; requires mixin per forgetful functor |

**Recommended**: Option A (inheritance) at the ABC layer. The semantic distinction between "a group" and "its underlying set" is already captured by the category-level forgetful functor.

**Proposed hierarchy**:
```
Object_In_A_1_Cat
    └── SetObject_ABC      — cardinality(), is_finite(), __iter__, etc.
            ├── GroupObject_ABC    — identity_element(), order(), etc.
            │       └── RingObject_ABC     — zero(), one(), characteristic()
            └── ModuleObject_ABC   — (R-module structure)
```

### Decision 2: Morphism Structure via `as_arrow()`

**Question**: How do per-category morphisms integrate with the Arrow hierarchy?

**Recommended**: Morphism classes don't duplicate Arrow methods; they return Arrow objects via `as_arrow()`:

```python
class GroupHomomorphism(_HomC_xy_0Cell_ABC):
    def as_arrow(self) -> OneArrow: ...  # Returns concrete arrow

class GroupEndomorphism(GroupHomomorphism):
    def as_arrow(self) -> OneEndoArrow: ...  # Covariant override

class GroupAutomorphism(GroupEndomorphism):
    def as_arrow(self) -> OneAutoArrow: ...  # Covariant override
```

The Arrow hierarchy provides `is_invertible()`, `order()`, `inverse()`; morphism classes get these via delegation.

### Decision 3: Cat_w is Minimal

**Question**: What does Cat_w need vs. regular categories?

**Cat_w NEEDS:**
- `fun(C, D) → Fun(C, D)` — construct functor category
- `compose_functors(F, G) → F ∘ G`
- `identity_functor(C) → id_C`
- Cell containers for 0-cells (categories), 1-cells (functors), 2-cells (nat. trans.)

**Cat_w does NOT need:**
- `is_abelian()` — Cat_w is not abelian
- `terminal_object_C()` — differs from regular categories
- Full category predicate infrastructure

**Implication**: Cat_w should inherit from `_Minimal_Two_Category_ABC`, not `_Nontrivial_Two_Category_ABC`.

### Decision 4: Forgetful Functors at Both Levels

**At category level** (already exists):
```python
class _GroupsCategory_ABC(ABC):
    def forgetful_functor_to_sets(self) -> CategoryABCs.Functor: ...
```

**At object level** (proposed addition for clarity):
```python
class _GroupObject_ABC(CategoryABCs.SetObject, ABC):
    def as_set(self) -> CategoryABCs.SetObject:
        """Explicit view as underlying set."""
        return self  # Identity since inherits from SetObject
```

This makes the forgetful functor action explicit at the object level.

---

## Part V: Open Questions

### Q1: Monoid Objects?

Should there be `_MonoidObject_ABC` between `SetObject` and `GroupObject`?
- Pro: Captures multiplicative monoid of rings cleanly
- Con: Adds another layer; most uses are abelian groups anyway

### Q2: Generic Hom Categories?

Can we use `Generic[C]` to define `HomC[C]` once?
```python
class _HomC_ABC(Generic[C], ABC):
    """The category of hom-sets in C."""
    base_category: type[C]
    ...
```
- Pro: Single definition for all categories
- Con: Python generics have limitations; may not work cleanly with ABC enforcement

---

## Summary

The ABC hierarchy should:

1. **Use inheritance for objects**: `SetObject ← GroupObject ← RingObject` so methods like `cardinality()` propagate
2. **Delegate morphism structure to Arrow classes**: Via `as_arrow()` with covariant return types
3. **Keep Cat_w minimal**: Separate ABC without full category predicates
4. **Implement multi-view via methods**: `as_zero_cell()`, `as_one_cell()`, `as_arrow()`

---

## Part VI: Category-Specific Methods and Defaults

### The Method Layering Problem

Consider `kernel()`. It appears at **multiple levels**:

| Level | Location | Method | Returns |
|-------|----------|--------|---------|
| **Arrow** | `abstract_arrows.py:286` | `kernel(self)` | `Any` |
| **Category** | `two_category_mixins.py:639` | `kernel_C(self, f)` | `CategoryABCs.Object` |

**Question**: How do these interact? If `GroupHomomorphism` wants a specific kernel implementation, where does it go?

### The Layering Design

```
                                ┌─────────────────────────────────────┐
                                │          Category Level              │
                                │  kernel_C(f: OneMorphism) → Object   │
                                │  - Constructs kernel in THIS category│
                                │  - Returns object with category ops  │
                                └───────────────────┬─────────────────┘
                                                    │ delegates to
                                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           Morphism Level                                 │
│  GroupHomomorphism.kernel() → GroupObject                                │
│  - Category-specific return type                                         │
│  - May call self.amb().kernel_C(self) or implement directly             │
└───────────────────────────────────────────────────────────────────────┘
                                                    │ has_a
                                                    ▼
                                ┌─────────────────────────────────────┐
                                │           Arrow Level                │
                                │  OneArrow.kernel() → Any             │
                                │  - Abstract, generic interface       │
                                │  - Pure structural, no category ops  │
                                └─────────────────────────────────────┘
```

**Key principle**: `as_arrow()` returns a **view** of the morphism as pure structure. Category-specific methods like `kernel()` are defined on the **morphism class itself**, NOT accessed via `as_arrow()`.

```python
class GroupHomomorphism(_OneMorphism_ABC):
    
    def kernel(self) -> CategoryABCs.GroupObject:
        """Return ker(f) as a group (subgroup of domain)."""
        return self.amb().kernel_C(self)  # Delegates to category
    
    def as_arrow(self) -> OneArrow:
        """View as pure arrow structure (no kernel method on result)."""
        return self._arrow_view
```

**The `as_arrow()` pattern is for structural properties only** — predicates like `is_invertible()`, `domain()`, `codomain()`. Category-specific constructions live on the morphism class.

---

### How Does a New Category Default to Base Implementations?

The `Object_And_Morphism_Classes` mixin requires 12 class methods:

```python
class Object_And_Morphism_Classes(ABC):
    @classmethod
    def object_class(cls) -> type[CategoryABCs.Object]: ...
    @classmethod
    def morphism_class(cls) -> type[CategoryABCs.OneMorphism]: ...
    @classmethod
    def homC_category_class(cls) -> type[CategoryABCs.HomC]: ...
    @classmethod
    def homC_xy_category_class(cls) -> type[CategoryABCs.HomC_xy]: ...
    @classmethod
    def endC_category_class(cls) -> type[CategoryABCs.EndC]: ...
    @classmethod
    def endC_x_category_class(cls) -> type[CategoryABCs.EndC_x]: ...
    @classmethod
    def endomorphism_class(cls) -> type[CategoryABCs.EndoOneMorphism]: ...
    @classmethod
    def autC_category_class(cls) -> type[CategoryABCs.AutC]: ...
    @classmethod
    def autC_x_category_class(cls) -> type[CategoryABCs.AutC_x]: ...
    @classmethod
    def automorphism_class(cls) -> type[CategoryABCs.AutoOneMorphism]: ...
    # ... etc
```

**Defaulting mechanism**: The base layer provides default implementations that return generic base classes:

```python
# In CategoryBases (partial implementations):
class _Nontrivial_TwoCategory_Base(CategoryABCs.Nontrivial_TwoCategory):
    
    @classmethod
    def homC_category_class(cls) -> type[CategoryABCs.HomC]:
        return CategoryBases.HomC  # Default base implementation
    
    @classmethod
    def homC_xy_category_class(cls) -> type[CategoryABCs.HomC_xy]:
        return CategoryBases.HomC_xy  # Default base implementation
    
    # ... etc for all 12 methods
```

**A new category that inherits from the base automatically gets defaults**:

```python
class MyCategory(CategoryBases.Category):
    
    # Only override what's different!
    @classmethod
    def object_class(cls) -> type[MyObject]:
        return MyObject  # Custom object class
    
    @classmethod  
    def morphism_class(cls) -> type[MyMorphism]:
        return MyMorphism  # Custom morphism class
    
    # homC_category_class, endC_category_class, etc. 
    # ALL DEFAULT to base implementations inherited from CategoryBases.Category
```

---

### When Must a Category Write Custom Hom Variants?

**Corrected understanding**: `Hom_C(X, Y)` is **simultaneously**:

1. A **category** (always) — with 0-cells (morphisms f: X → Y), 1-cells (2-morphisms), composition
2. An **object in C** (when C is closed/enriched) — with all the structure of C-objects
3. An **object in other categories** — topological space, group, dg-module, etc.

These are **not exclusive**. The same entity participates in multiple categorical structures.

**Examples:**

| Category C | `Hom_C(X, Y)` is also... |
|------------|--------------------------|
| Mod_R | An R-module (pointwise operations) |
| Ab | An abelian group |
| Top | A topological space (compact-open topology) |
| Ch(Mod_R) | A chain complex of R-modules |
| dg-Mod | A dg-module |

**Architectural implication**: `_HomC_xy` classes often need **multiple inheritance**:

```python
class _HomModR_xy_ABC(
    CategoryABCs.HomC_xy,       # It's a hom-category (always)
    CategoryABCs.ModuleObject,  # It's an R-module
    ABC
):
    """Hom_{Mod_R}(M, N) — simultaneously a category AND an R-module."""
    
    # From HomC_xy: composition, source, target, identity
    # From ModuleObject: zero(), scalar_multiply(), add()
    ...
```

**When is this needed?**

| Scenario | Custom HomC_xy ABC? |
|----------|---------------------|
| C is a 1-category with no enrichment (Set, FinSet) | No — use base `CategoryBases.HomC_xy` |
| C is enriched over Ab (Mod_R, Ab, Vec_k) | Yes — inherit `HomC_xy` + object ABC of enrichment |
| C is enriched over Top | Yes — inherit `HomC_xy` + `TopObject` |
| C is a 2-category or higher | Base `HomC_xy` may suffice, but 2-cell structure matters |

**The VSCode workflow (corrected)**:

```
1. For Set: inherit CategoryBases.Category, use default HomC classes
2. For Mod_R: define custom _HomModR_xy_ABC inheriting HomC_xy AND ModuleObject
3. The class specifying methods (object_class, homC_xy_class, etc.) point to these
```

Most "interesting" algebraic categories require custom HomC_xy classes because their hom-categories carry the same structure as their objects.

---

### The `as_arrow()` ≠ Full Morphism Access

**Critical distinction**:

```python
f: GroupHomomorphism = ...

# Via morphism class — has category-specific methods
f.kernel()           # ✓ Returns GroupObject (subgroup)
f.domain()           # ✓ Returns GroupObject  
f.image()            # ✓ Returns GroupObject (subgroup of codomain)

# Via as_arrow() — only structural methods
arrow = f.as_arrow()
arrow.is_invertible()    # ✓ Returns BoolProof
arrow.domain()           # ✓ Returns Any (type erased)
arrow.kernel()           # ✗ May not exist, or returns Any
```

**`as_arrow()` is for**:
- Predicates (`is_invertible()`, `is_endomorphism()`)
- Generic composition algorithms
- Passing to code that works on "any arrow"

**The morphism class is for**:
- Category-specific constructions (`kernel()`, `image()`, `cokernel()`)
- Correct return types (`GroupObject` not `Any`)
- Access to ambient category methods

---

## Part VII: Views via Functors and the Lifting Problem

### The Core Principle: Views via Explicit Functors

Instead of inheritance for accessing underlying structure, use **explicit functors**:

```python
# WRONG (inheritance-based):
class ModuleObject(GroupObject):  # Module "is a" group?
    def cardinality(self):
        return super().cardinality()  # Inherited from SetObject

# CORRECT (functor-based):
class ModuleObject(ABC):
    def as_abelian_group(self) -> GroupObject:
        """Forgetful functor U: Mod_R → Ab applied to self."""
        ...
    
    def cardinality(self):
        # Explicitly use forgetful functor to Set
        return self.forgetful_to_set().cardinality()
```

To say "an object x in Mod_R has cardinality" means:
- Mod_R has a forgetful functor U: Mod_R → Set
- U(x).cardinality() is the cardinality

This makes the functorial relationships **explicit**, not hidden in inheritance.

---

### The Kernel Lifting Problem

Consider `kernel()` for morphisms:

```
Mod_R ──U──> Ab ──V──> Set
  │           │
  f           U(f)
  │           │
  ▼           ▼
ker(f)?    ker(U(f)) = subgroup, NOT submodule
```

**Problem**: `U(f).kernel()` returns a subgroup. But:
1. The computation might be identical for Mod_R and Ab
2. The result has the **wrong type** — it's a Group, not a Module
3. There's no automatic "lift" from Group back to Module

**Not all subgroups lift to submodules!** (e.g., subgroups not closed under scalar multiplication). However, **kernels always lift** because kernels are defined algebraically.

---

### Solution Options

#### Option A: Each Category Implements Its Own `kernel()`

```python
class _ModuleMorphism_ABC(ABC):
    def kernel(self) -> CategoryABCs.ModuleObject:
        """Compute kernel directly in Mod_R."""
        # Implementation specific to modules
        ...

class _GroupMorphism_ABC(ABC):
    def kernel(self) -> CategoryABCs.GroupObject:
        """Compute kernel directly in Groups."""
        # Implementation specific to groups, may be identical code
        ...
```

**Tradeoff**:
- ✓ Types always correct
- ✗ Code duplication when algorithms are identical
- ✗ Changes to kernel algorithm must propagate to all categories

---

#### Options B, C, D: Lifting-Based Approaches (ANALYSIS: Limited Applicability)

The following options have **limited applicability**:

**Option B: Compute + Verify + Construct** — Compute in underlying category, then lift result:
```python
underlying_ker = self.as_ab_morphism().kernel()  # Returns GroupObject
return self.amb().submodule_from_group(underlying_ker)  # Lift to Module
```

**Option C: Mixin + Factory** — Shared algorithm computes "raw data", category wraps it:
```python
data = self._compute_kernel_data(f)  # Shared algorithm
return self._wrap_as_subobject(data)  # Category-specific wrapping
```

**Option D: Explicit Lifting Functors** — Forgetful functor with partial inverse:
```python
ab_kernel = self.forgetful_to_ab().target().kernel_C(ab_morphism)
result = self.lift_from_ab(ab_kernel)  # Lift back to Module
```

**When lifting DOES work**:

1. **Finitely-presented objects with shared representation**: For f.g. R-modules, kernel is computed via Smith normal form on the presentation matrix. The same generators work in Ab or Mod_R because kernels are closed under scalar multiplication. The "lift" is trivial — same data, different type wrapper.

2. **Categories sharing algorithmic infrastructure**: When Mod_R and Ab both use matrix presentations, the kernel algorithm is identical; only the wrapping differs.

**When lifting FAILS**:

1. **Descending to Set**: You cannot meaningfully compute kernel at the Set level for infinite sets (cannot enumerate), and even for finite sets the result has no algebraic structure to "lift."

2. **Infinitely-presented objects**: For groups/modules without finite presentations, there is no shared "raw data" format. Each category requires its own representation (e.g., recursive presentations, transfinite constructions).

3. **Incompatible representations**: If the source category uses one representation and the target uses another (e.g., permutation groups vs matrix groups), lifting requires non-trivial translation.

**Concrete examples**:

- **Works**: ker(φ: ℤⁿ → ℤᵐ) computed via Smith normal form — same algorithm for Ab, Mod_ℤ, Mod_R.
- **Fails**: ker(φ: ℤ → ℤ/nℤ) computed set-theoretically would require checking all x ∈ ℤ. Algebraically, ker(φ) = nℤ is computed from the presentation.


---

### Recommended Approach: Option A (Category-Specific Implementations)

**Reasoning**:
1. For infinite objects, there is no alternative — each category must implement constructions using category-specific representations (generators, presentations, etc.)
2. "Code duplication" is often illusory — the algorithms genuinely differ between categories (e.g., kernel of a group homomorphism vs kernel of a ring homomorphism)
3. Types are always correct without runtime verification
4. Implementations can share utility functions where genuine overlap exists

**Design pattern for shared utilities**:

```python
# Low-level utilities can be shared
def _kernel_via_smith_normal_form(matrix: Matrix) -> MatrixSubspace:
    """Shared algorithm for finitely-presented abelian groups/modules."""
    ...

# Category-specific methods call utilities
class _ModuleMorphism_ABC(ABC):
    def kernel(self) -> CategoryABCs.ModuleObject:
        if self.is_finitely_presented():
            return self._wrap_submodule(_kernel_via_smith_normal_form(self.matrix()))
        else:
            return self._kernel_from_presentation()
```

This keeps type safety while allowing algorithm reuse at the utility level.

---

### Open Questions

1. **When do algorithms genuinely overlap?** Primarily for finitely-presented objects where matrix methods apply (Smith normal form, etc.)

2. **How to handle limits/colimits uniformly?** Products, coproducts, etc. may have more uniform structure than kernels/cokernels.

3. **When computation genuinely differs**, Option C (mixin + factory) may be more appropriate. How to detect this?

---

## Part VIII: Composition vs Inheritance — Deep Analysis

### Current Architecture: Inheritance-Heavy Design

The existing ABC hierarchy uses multiple inheritance extensively:

```
_Minimal_Two_Category_ABC(
    Required_Sage_Methods,
    Basic_Metadata,
    Object_And_Morphism_Classes,
    Predicates_On_This_Category,
    Ambient_Category_Interactions,
    Self_With_Other_Operators,
    Equivalence_Of_Self_With_Other_Checks,
    ABC
)

_Nontrivial_Two_Category_ABC(
    MinimalCategory,
    Hom_Constructors,
    Predicates_On_Objects,
    Limit_C_Classes,
    Internal_Object_And_Morphism_Constructors,
    Object_Enumerating_And_Sampling,
    ABC
)
```

**Observed patterns**:
2. **Cell hierarchy** with dimension-specific classes (`_ZeroCell`, `_OneCell`, `_TwoCell`)
3. **Arrow hierarchy** combining dimension × structure axes via multiple inheritance
4. **View methods** (`as_zero_cell()`, `as_one_cell()`, `as_arrow()`) for dimension-shifting

---

### The Core Tension: A Morphism's Many Identities

A single entity can simultaneously be:

| Context | Entity is viewed as |
|---------|---------------------|
| Base category C | 1-cell (morphism f: X → Y) |
| Hom_C(X,Y) | 0-cell (object) |
| Arrow category Arr(C) | 0-cell |
| If X = Y, End_C(X) | 0-cell (endomorphism) |
| If invertible, Aut_C(X) | 0-cell (automorphism) |
| Cat_w | Functor (1-cell between categories) |
| Fun(C,D) | 0-cell in the functor category |

**Key insight**: The underlying data is fixed; only the categorical context changes.

---

### Alternative Framework: Everything as an n-Cell

Consider a unified design where:

```python
@dataclass
class Cell:
    """Universal n-cell. Methods available depend on dimension."""
    
    dimension: int  # -1, 0, 1, 2, ...
    source: Cell | None  # None for (-1)-cells
    target: Cell | None
    
    # Structural data
    _underlying: Any
    _container: CellContainer
    
    # Dynamic method dispatch based on dimension
    def is_identity(self) -> BoolProof:
        """Works for any n ≥ 0."""
        if self.dimension < 0:
            return BoolProof.true("empty cell is vacuously identity")
        return self.source.is_equivalent_to(self.target)
    
    def compose_with(self, other: Cell) -> Cell:
        """Composition at dimension n."""
        assert self.dimension == other.dimension
        assert self.target.is_equivalent_to(other.source)
        # Dispatch to appropriate composition
        ...
    
    # Methods conditional on dimension
    def is_invertible(self) -> BoolProof:
        """Only meaningful for n ≥ 1."""
        ...
    
    def kernel(self) -> Cell:
        """Only meaningful for 1-cells with appropriate structure."""
        ...
    
    def vertical_compose(self, other: Cell) -> Cell:
        """Only meaningful for 2-cells."""
        assert self.dimension >= 2
        ...
    
    def horizontal_compose(self, other: Cell) -> Cell:
        """Only meaningful for 2-cells."""
        assert self.dimension >= 2
        ...
```

**Pros of unified Cell approach**:
1. Single class hierarchy instead of `_ZeroCell`, `_OneCell`, `_TwoCell`, etc.
2. Natural handling of "same data, different view" via dimension parameter
3. Dimension-shifting becomes trivial: `cell.at_dimension(n)`
4. Reduced class explosion: No need for `_HomC_xy_0Cell_ABC`, `_HomC_xy_1Cell_ABC`, etc.

**Cons**:
1. **Loss of static type safety**: Cannot distinguish 1-cells from 2-cells at compile time
2. **Runtime errors instead of type errors**: `horizontal_compose` on a 1-cell fails at runtime
3. **IDE support degraded**: No autocomplete for dimension-specific methods
4. **Mathematical structure obscured**: The categorical structure isn't reflected in types

---

### Critical Analysis: Benefits of Strong Typing for Categorical Correctness

**Why inheritance matters for this domain**:

1. **Category theory is about types**: The whole point of category theory is that composition respects types. A morphism f: X → Y can only compose with g: Y → Z, not g: W → Z. Strong typing enforces this.

2. **Hierarchy encodes mathematical structure**:
   ```
   _nArrow
       └── _EndoArrow (source = target)
               └── _AutoArrow (invertible)
   ```
   This isn't accidental — it reflects that:
   - End(X) ⊆ Hom(X, X) ⊆ Hom(X, Y)
   - Aut(X) ⊆ End(X)
   
   Inheritance captures this **mathematically correct** containment.

3. **Type covariance matches mathematical covariance**:
   ```python
   class GroupHomomorphism:
       def as_arrow(self) -> OneArrow: ...
   
   class GroupEndomorphism(GroupHomomorphism):
       def as_arrow(self) -> OneEndoArrow: ...  # Covariant refinement
   
   class GroupAutomorphism(GroupEndomorphism):
       def as_arrow(self) -> OneAutoArrow: ...  # Further refinement
   ```
   
   The type system tracks that automorphisms have more structure than general homomorphisms.

4. **Method availability encodes theorems**:
   - `kernel()` existing on `GroupHomomorphism` encodes: "Group homomorphisms have kernels"
   - `inverse()` existing only on `_AutoArrow` encodes: "Only automorphisms are invertible"
   - The type system becomes a theorem prover

---

### Hybrid Approach: Composition for Views, Inheritance for Structure

The current design already uses a hybrid:

**Inheritance for structural hierarchy**:
```python
class _EndoArrow(_nArrow): ...  # Structural property: domain = codomain
class _AutoArrow(_EndoArrow): ...  # Structural property: invertible

class GroupHomomorphism(_HomC_xy_0Cell_ABC): ...
class GroupEndomorphism(GroupHomomorphism): ...
class GroupAutomorphism(GroupEndomorphism): ...
```

**Composition (via methods) for views**:
```python
class _HomC_xy_0Cell_ABC:
    def as_zero_cell(self) -> CategoryABCs.Cell: ...
    def as_one_cell(self) -> CategoryABCs.Cell: ...
    def as_arrow(self) -> OneArrow: ...
```

This is the **correct** hybrid:
- **Inheritance** captures what an entity **is** (structural identity)
- **View methods** capture how an entity can be **regarded** (interpretation)

---

### The Object Hierarchy Problem

Current approach has objects in a linear chain:
```
Object_In_A_1_Cat
    └── SetObject_ABC
            └── GroupObject_ABC
                    └── RingObject_ABC
                            └── ModuleObject_ABC
```

**Problem**: A ring has *two* group structures (additive and multiplicative monoid). Linear inheritance can't express this.

**Better model**:
```python
class RingObject(
    SetObject,          # Underlying set
    AbelianGroupMixin,  # (R, +) is abelian group
    MonoidMixin,        # (R, ×) is monoid
    ABC
):
    """A ring: set with two operations satisfying axioms."""
    
    def additive_group(self) -> GroupObject:
        """View (R, +) as a group."""
        ...
    
    def multiplicative_monoid(self) -> MonoidObject:
        """View (R, ×) as a monoid (not group unless units)."""
        ...
```

This uses **multiple inheritance for structures** and **composition (via methods) for views**.

---

### Recommended Architecture

| Use Case | Mechanism |
|----------|-----------|
| Structural hierarchy (End ⊆ Hom) | Single inheritance |
| Multiple structures (Ring = AddGrp + MultMonoid) | Multiple inheritance from mixins |
| Different views of same data | View methods (`as_zero_cell()`, `as_arrow()`) |
| Shared algorithms (f.p. objects only) | Shared utility functions called by category-specific methods |
| Dimension-specific behavior | Separate classes (`_ZeroCell`, `_OneCell`) with shared base |

---

### Why Not Pure Composition?

**Pure composition approach**:
```python
@dataclass
class Morphism:
    domain: Object
    codomain: Object
    map_data: Callable
    
    arrow: Arrow  # Composed-in arrow behavior
    cell: Cell    # Composed-in cell behavior
```

**Problems**:
1. **Lost type hierarchy**: Can't distinguish `GroupHomomorphism` from `SetMorphism`
2. **No covariant return types**: `GroupHomomorphism.kernel()` can't statically return `GroupObject`
3. **Category-specific constraints lost**: Nothing enforces that Group homomorphisms preserve identity
4. **Duplication of data**: `arrow.domain` vs `self.domain`

**The fundamental issue**: In category theory, the *type* of a morphism carries meaning. A group homomorphism isn't just a function; it's a function that respects group structure. This is a typing property, not a runtime property.

---

### Summary: Inheritance is Correct for This Domain

For this categorical framework:

1. **Keep inheritance for cell dimension hierarchy** — `_ZeroCell`, `_OneCell`, `_TwoCell` should remain separate types
2. **Keep inheritance for endo/auto structure** — `_AutoArrow` extends `_EndoArrow` extends `_nArrow`
3. **Keep inheritance for object hierarchy** — `GroupObject` extends `SetObject`
4. **Use multiple inheritance for multiple structures** — `RingObject` inherits from both group and monoid mixins
5. **Use view methods for dimension-shifting** — `as_zero_cell()`, `as_one_cell()`, `as_arrow()`
6. **Each category implements its own constructions** — shared utilities only for finitely-presented objects with common representations

**Do NOT adopt**:
- Single unified `Cell` class with dimension parameter (loses type safety)
- Pure composition where capabilities are objects (loses typing information)
- Replacing inheritance with delegation (loses the mathematical hierarchy encoding)

The current architecture is fundamentally sound. The complexity isn't accidental — it reflects the inherent complexity of higher category theory where entities have multiple identities.

---

## Part IX: Complete ABC Hierarchy

### Overview

```
Layer 0: CELLS — source()/target() interface by dimension
    (-1)-Cell → EmptyCell (source=None, target=None)
    0-Cell → source() → EmptyCell, target() → EmptyCell
    1-Cell → source() → 0-Cell, target() → 0-Cell
    2-Cell → source() → 1-Cell, target() → 1-Cell

Layer 1: ARROWS — Cells with dimension-specific operations
    0-Arrow = 0-Cell (objects have no arrow operations beyond cell interface)
    1-Arrow = 1-Cell + compose(), is_surjective(), kernel(), ...
    2-Arrow = 2-Cell + vertical_compose(), horizontal_compose(), ...

Layer 2: ENTITIES — Arrows in specific categorical contexts
    0-Entity: _Object_ABC(0-Arrow) — an object in a category
    1-Entity: _Morphism_ABC(1-Arrow) — a morphism in a category
    2-Entity: _TwoMorphism_ABC(2-Arrow) — a 2-morphism in a 2-category

Layer 3: SPECIFIC ENTITIES — Extend generic entities
    _Functor_ABC(_Morphism_ABC) — extends morphism
    _NatTrans_ABC(_TwoMorphism_ABC) — extends 2-morphism
    _GroupHomomorphism_ABC(_Morphism_ABC) — extends morphism
```

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
    
    def source(self) -> None:
        return None
    
    def target(self) -> None:
        return None

EMPTY_CELL = _NegativeOneCell()  # Singleton


class _ZeroCell(_nCell, ABC):
    """0-cell. source/target are empty."""
    
    def source(self) -> _NegativeOneCell:
        return EMPTY_CELL
    
    def target(self) -> _NegativeOneCell:
        return EMPTY_CELL


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

Arrows extend cells with dimension-specific operations.

```python
class _nArrow(_nCell, ABC):
    """Arrow = cell + dimension-specific operations."""
    
    @abstractmethod
    def amb(self) -> _Category_ABC:
        """The ambient category containing this arrow."""
        ...

class _NegativeOneArrow(_NegativeOneCell, _nArrow, ABC):
    """(-1)-arrow = (-1)-cell + element operations."""
    ...

class _ZeroArrow(_ZeroCell, _nArrow, ABC):
    """0-arrow = 0-cell + object operations."""

    @abstractmethod
    def identity_morphism(self) -> _OneArrow: ...

class _OneArrow(_OneCell, _nArrow, ABC):
    """1-arrow = 1-cell + morphism operations."""
    
    @abstractmethod
    def compose(self, other: Self) -> Self: ...
    
    @abstractmethod
    def is_surjective(self) -> BoolProof: ...
    
    @abstractmethod
    def is_injective(self) -> BoolProof: ...
    


class _TwoArrow(_TwoCell, _nArrow, ABC):
    """2-arrow = 2-cell + 2-morphism operations."""
    
    @abstractmethod
    def vertical_compose(self, other: Self) -> Self: ...
    
    @abstractmethod
    def horizontal_compose(self, other: Self) -> Self: ...
    
```

---

### Layer 2: Entity ABCs

Entities are arrows in a specific categorical context. They inherit from arrow ABCs and add context-specific semantics.

```python

class _Element_ABC(_NegativeOneArrow, ABC):
    """An element in a category. A (-1)-arrow with categorical context."""
    
    @abstractmethod
    def parent_object(self) -> _Object_ABC: ...

class _Object_ABC(_ZeroArrow, ABC):
    """An object in a 2-category. A 0-arrow with categorical context."""

    @abstractmethod
    def some_elements(self): ...

class _Morphism_ABC(_OneArrow, ABC):
    """A morphism in a category. A 1-arrow with categorical context."""
    
    # Inherits source(), target(), compose(), is_surjective(), etc.
    
    @abstractmethod
    def apply(self, x: Any) -> _Element_ABC:
        """Apply this morphism to an element/object."""
        ...
    
    @abstractmethod
    def is_surjective(self) -> BoolProof: ...
    
    @abstractmethod
    def is_injective(self) -> BoolProof: ...

class _TwoMorphism_ABC(_TwoArrow, ABC):
    """A 2-morphism in a 2-category. A 2-arrow with categorical context."""
    
    # Inherits source(), target(), vertical_compose(), horizontal_compose(), etc.
    ...

class _Two_Category_ABC(_ZeroArrow, ABC):
    """A 2-category. A 0-arrow with categorical context."""

    @abstractmethod
    def element_class(self) -> Type[_Element_ABC]: ...
    
    @abstractmethod
    def objects(self) -> Iterable[_Object_ABC]: ...
    
    @abstractmethod
    def morphisms(self) -> Iterable[_Morphism_ABC]: ...

    @abstractmethod
    def two_morphisms(self) -> Iterable[_TwoMorphism_ABC]: ...

class _Product_Two_Category_ABC(_Two_Category_ABC, ABC):
    """A 2-category. A 0-arrow with categorical context."""

    @abstractmethod
    @override
    def element_class(self) -> Type[_Element_ABC]: ...
    
    @abstractmethod
    @override
    def objects(self) -> Iterable[_Object_ABC]: ...
    
    @abstractmethod
    @override
    def morphisms(self) -> Iterable[_Morphism_ABC]: ...

    @abstractmethod
    @override
    def two_morphisms(self) -> Iterable[_TwoMorphism_ABC]: ...

```

---

### Layer 3: Specific Entity ABCs

Specific entities extend the generic entity ABCs with domain-specific operations.

```python
# === Functors extend Morphisms ===

class _Functor_ABC(_Morphism_ABC, ABC):
    """A functor F: C → D. Extends morphism with functor-specific operations."""
    
    # Inherited from _Morphism_ABC (which inherits from _OneArrow):
    # - source() returns C (a category, which is a 0-cell in Cat_w)
    # - target() returns D
    # - compose(G) returns F ∘ G
    # - is_surjective(), is_injective(), kernel(), image()
    
    # Functor-SPECIFIC operations:
    @abstractmethod
    def apply_to_object(self, x: _Object_ABC) -> _Object_ABC: ...
    
    @abstractmethod
    def apply_to_morphism(self, f: _Morphism_ABC) -> _Morphism_ABC: ...
    
    @abstractmethod
    def is_faithful(self) -> BoolProof: ...
    
    @abstractmethod
    def is_full(self) -> BoolProof: ...
    
    @abstractmethod
    def is_essentially_surjective_on_objects(self) -> BoolProof: ...
    


# === Natural Transformations extend 2-Morphisms ===

class _NatTrans_ABC(_TwoMorphism_ABC, ABC):
    """A natural transformation η: F ⇒ G. Extends 2-morphism."""
    
    # Inherited from _TwoMorphism_ABC (which inherits from _TwoArrow):
    # - source() returns F (a functor, which is a 1-cell)
    # - target() returns G
    # - vertical_compose(θ) for η ∘ θ
    # - horizontal_compose(θ) for η * θ
    
    # Nat trans-SPECIFIC operations:
    @abstractmethod
    def component_at(self, x: _Object_ABC) -> _Morphism_ABC:
        """η_x: F(x) → G(x)."""
        ...
    
    @abstractmethod
    def is_natural_isomorphism(self) -> BoolProof: ...


# === Group Homomorphisms extend Morphisms ===

class _GroupHomomorphism_ABC(_Morphism_ABC, ABC):
    """A group homomorphism φ: G → H. Extends morphism."""
    
    # Inherited: source(), target(), compose(), is_surjective(), kernel(), ...
    
    # Group hom-SPECIFIC operations:
    @abstractmethod
    def apply_to_element(self, g: _Element_ABC) -> _Element_ABC: ...
    
    def apply(self, x: Any) -> Any:
        return self.apply_to_element(x)
```

---

### Viewing as Lower-Dimensional Cells

An n-cell in C can naturally be viewed as a k-cell (0 ≤ k ≤ n-1) in a related category:

| Original Cell | As k-cell | In Category |
|--------------|-----------|-------------|
| 1-cell f: X → Y in C | 0-cell | Hom_C(X, Y) or Arr(C) |
| 2-cell η: f ⇒ g in C | 1-cell | Arr(C) |
| 2-cell η: f ⇒ g in C | 0-cell | Hom_{Arr(C)}(f, g) |
| 2-cell η: F ⇒ G in Cat_w | 1-cell | Arr(Cat_w) |
| 2-cell η: F ⇒ G in Cat_w | 0-cell | Fun(C, D) |

**Implementation**: Add `as_k_cell(k)` to `_All_Cells_ABC`:

```python
class _All_Cells_ABC(ABC):
    def as_k_cell(self, k: int) -> CategoryABCs.Cell:
        """
        View this n-cell as a k-cell in a related category.
        
        Args:
            k: Target dimension (0 <= k <= self.cell_dimension() - 1)
            
        Returns:
            This cell viewed as a k-cell. The ambient category changes
            based on the dimension shift.
        """
        ...
```

This avoids wrapper classes — each entity is canonically its highest cell dimension, with `as_k_cell()` providing interpretations as lower-dimensional cells in other categories.

---

### Category Declarations

Categories declare their cell/arrow/entity types:

```python
class _TwoCategory_ABC(_ZeroArrow, ABC):
    """A 2-category. Is a 0-cell in Cat_w."""
    
    @classmethod
    def object_class(cls) -> type[_Object_ABC]: ...
    
    @classmethod
    def morphism_class(cls) -> type[_Morphism_ABC]: ...
    
    @classmethod
    def two_morphism_class(cls) -> type[_TwoMorphism_ABC]: ...


class _Cat_W_ABC(_TwoCategory_ABC):
    """Cat_w: the 2-category of categories."""
    
    @classmethod
    def object_class(cls) -> type[_TwoCategory_ABC]:
        return _Category_ABC  # 0-cells are categories
    
    @classmethod
    def morphism_class(cls) -> type[_Functor_ABC]:
        return _Functor_ABC  # 1-cells are functors
    
    @classmethod
    def two_morphism_class(cls) -> type[_NatTrans_ABC]:
        return _NatTrans_ABC  # 2-cells are nat trans
```

---

### Summary Table

| Layer | ABC | Inherits | Purpose |
|-------|-----|----------|---------|
| Cell | `_NegativeOneCell` | — | (-1)-cell, no source/target |
| Cell | `_ZeroCell` | — | 0-cell, source/target → EmptyCell |
| Cell | `_OneCell` | — | 1-cell, source/target → ZeroCell |
| Cell | `_TwoCell` | — | 2-cell, source/target → OneCell |
| Arrow | `_ZeroArrow` | `_ZeroCell` | 0-arrow (object-like) |
| Arrow | `_OneArrow` | `_OneCell` | 1-arrow + compose, kernel, ... |
| Arrow | `_TwoArrow` | `_TwoCell` | 2-arrow + v/h compose, whisker |
| Entity | `_Object_ABC` | `_ZeroArrow` | Object in a category |
| Entity | `_Morphism_ABC` | `_OneArrow` | Morphism in a category |
| Entity | `_TwoMorphism_ABC` | `_TwoArrow` | 2-morphism in a 2-category |
| Specific | `_Functor_ABC` | `_Morphism_ABC` | Functor = morphism in Cat_w |
| Specific | `_NatTrans_ABC` | `_TwoMorphism_ABC` | Nat trans = 2-morph in Cat_w |
| Specific | `_GroupHom_ABC` | `_Morphism_ABC` | Group hom = morphism in Grp |

---


