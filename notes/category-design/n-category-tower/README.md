<!--
Origin: gitclones/integral_lattice/cat/README.md
Copied 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of
this corpus.
-->

# Cat: Implementation of n-Categories

> **⚠️ Do NOT use system Python.** Always run scripts with Sage or the uv venv's Python. Do not use pytest, pyright, or any other python tools directly, always route through the venv.

Implementation of n-categories for n = -1, 0, 1, 2, and ∞.

---

# Architecture: Three Stages

The codebase follows a strict three-stage architecture:

## Stage 1: Speccing (ABCs)

**Location:** `src/abc/abstract/`

ABCs define the **implementation-agnostic specification** for all categorical structures.

### Rules:

1. **Override Rule:** Only use `@override` when **tightening types** (narrowing return types in subclasses). Do not redeclare methods with the same signature as the base class - remove them and rely on inheritance.

2. **Type Routing:** All types used outside the ABC module must be routed through `_types.py`. Never import directly from ABC files elsewhere.

3. **Category Definition Pattern:** Every category must:
   - Define its cells (ZeroCell, OneCell, TwoCell, etc.)
   - Inherit from being an object in wCat (using `CategoryABCs.Nontrivial_TwoCategory` from `_types`)
   - Cells inherit from arrow mixins and cell ABCs

4. **No Implementations:** ABCs contain only `@final
    @abstractmethod` declarations and type annotations. No concrete logic.

```python
# In ABC file:
from src._types import CategoryABCs

class _MyCategory_ABC(CategoryABCs.Nontrivial_TwoCategory, ABC):
    @final
    @abstractmethod
    def objects(self) -> Sequence[CategoryABCs.Object]: ...
```

---

## Stage 2: Base (Partial) Implementations

**Location:** `src/abc/bases/`

Bases provide **partial implementations** that follow almost entirely from the established spec ABCs. These are opinionated defaults leveraging only the abstract structure.

### Rules:

1. **Partial Only:** Bases must NOT make full architectural decisions. They offer inheritable partial solutions that work generically.

2. **Agnostic Implementations:** Implementations must be agnostic to specific category details:
   ```python
   # GOOD: Delegates to ambient category
   def product(self, other: Self) -> CategoryABCs.Object:
       return self.amb().product_C([self, other])
   
   # BAD: Assumes specific implementation
   def product(self, other: Self) -> CategoryABCs.Object:
       return MyConcreteProduct(self.data + other.data)
   ```

3. **Decorators Required:** All implemented methods must use:
   - `@override` - marks it as implementing an abstract method
   - `@final` - prevents subclasses from overriding (forces them to use the abstract interface)

4. **No New Methods:** No base may add methods not present in the abstract class it extends.

5. **Type Routing:** Import from `_types`:
   ```python
   from src._types import CategoryBases, CategoryABCs
   
   class _MyCategory_Base(CategoryBases.Category):
       @override
       @final
       def product(self, other: Self) -> CategoryABCs.Object:
           return self.amb().product_C([self, other])
   ```

---

## Stage 3: Full Implementations

**Location:** `src/abc/concrete/`

Full implementations provide complete, working categories with all methods implemented.

### Rules:

1. **Must Inherit from Base:** All concrete implementations must inherit from a base class, routed through `_types`:
   ```python
   from src._types import CategoryBases
   
   class MyCategory(CategoryBases.Category):
       ...
   ```

2. **Scaffold Pattern:** When implementing a new category:
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

3. **Greenfield Pattern:** Scaffold all extensions first, attach to `category.py`, then instantiate. Missing abstract methods will surface as errors.

---

# Guidelines

Do NOT write `__init__.py` files, this is not how sagemath structures things. 

> [!CAUTION]
> **No ad-hoc testing.** Do NOT verify behavior with one-off `sage -c` scripts or similar. All tests must go through `just test` as formal, documented proofs that behaviors work as intended.

Run with:
```bash
just test
```

Test framework: `pytest` + `hypothesis`. See `tests/` for patterns.

Regarding type checking and linting, never attempt to use system python packages. Refer to `justfile` for proper commands.

---

# Style Guidelines

- Never **add** additional `type: ignore` comments -- these should only be added by humans in extreme cases where type issues can not be resolved by architecture redesign. Do not hide these issues, since they should guide a correct design.
- NEVER set a field to a default value of `None` and then use `field(default=None)` -- this is a code smell and indicates a design issue.
    - More broadly, it is almost NEVER correct to set default fields, period. Most categories are singletons, and only their objects and morphisms have instantiations.
- NEVER use `type: ignore` to suppress type errors -- this is a code smell and indicates a design issue.
- Never return `None` anywhere: this is pure mathematics, and "None" is not a valid mathematical object. Determine instead if it's more appropriate to return the initial category or the terminal category.
- Never use `NotImplementedError` to suppress type errors -- this is a code smell and indicates a design issue.
- Never purposefully throw an error. Instead, use assertions of correctness, and let failed assertions surface errors to inform redesign.
- Do not use `isinstance`. Instead, use TypeGuard/TypeIs patterns provided in `_types`, or add your own there.
- NEVER use `has_attr` outside of `_types.py`. This violates strong typing. Assert proper typeguards instead.
- Prefer `case/match` constructions over nested `if` statements. Use `assert_never` to catch unhandled cases.