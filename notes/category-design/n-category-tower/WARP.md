<!--
Origin: gitclones/integral_lattice/cat/WARP.md
Copied 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of
this corpus.
-->

# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

Implementation of n-categories for n = -1, 0, 1, 2, and ∞. This is a **pure mathematical library** built on SageMath that implements category theory structures with extreme type safety and mathematical rigor.

**Critical**: This is a SageMath project, not standard Python. All scripts are Sage scripts and must never import `sage.all`.

## Environment Setup

**Never use system Python.** All commands must run through uv venv or Sage's Python.

### Essential Commands

```bash
# Sync/update environment
just sync              # Create/sync uv virtual environment
just install          # Install all dependencies including dev
just update           # Update all dependencies

# Main development command - runs EVERYTHING
just test             # Runs formatting, linting, type-checking, and all tests
                      # This MUST pass before any work is considered complete

# Cleanup
just clean            # Remove caches and build artifacts

# Environment info
just info             # Show Sage version, Python version, and installed packages
```

### Understanding `just test`

The `just test` command runs in this order:
1. `black` formatting on `src/`
2. `autopep8` auto-formatting on `src/`  
3. `ruff check --fix` for linting
4. `flake8` for additional linting
5. `mypy` for type checking
6. `basedpyright` for strict type checking
7. `pytest` tests via Sage's Python
8. `deal lint` for contract verification

All tools run via `uv run` except pytest and deal which use Sage's venv Python at `~/gitclones/sage/.venv/bin/python`.

**If any step fails, the entire command fails.** This is intentional.

### Running Individual Tests

```bash
# Run specific test file
~/gitclones/sage/.venv/bin/python -m pytest tests/test_terminal_category.py

# Run specific test function
~/gitclones/sage/.venv/bin/python -m pytest tests/test_terminal_category.py::test_terminal_category_singleton_object

# Run with verbose output
~/gitclones/sage/.venv/bin/python -m pytest tests/ -v

# Run with hypothesis debugging
~/gitclones/sage/.venv/bin/python -m pytest tests/ --hypothesis-verbosity=verbose
```

### Type Checking

```bash
# Run mypy only
uv run mypy src/

# Run basedpyright only (stricter)
uv run basedpyright src/

# Check specific file
uv run basedpyright src/abc/abstract/cat_w.py
```

### Linting and Formatting

```bash
# Format code
uv run black src/
uv run autopep8 --in-place --recursive src/

# Lint code
uv run ruff check src/
uv run flake8 src/

# Auto-fix linting issues
uv run ruff check --fix src/
```

## Architecture

### Three-Layer Design Pattern

The codebase follows a strict three-layer architecture to separate concerns:

1. **Abstract Layer** (`src/abc/abstract/`): Pure ABCs defining the mathematical interface
   - Classes end with `_ABC` suffix (e.g., `_CatW_ABC`, `_Morphism_ABC`)
   - Only `@final
    @abstractmethod` declarations - no implementations
   - Define the mathematical specification

2. **Base Layer** (`src/abc/bases/`): Partial implementations with operator mixins
   - Classes end with `_Base` suffix (e.g., `_CatW_Base`, `Morphism_Base`)
   - Implement methods using only abstract structure from ABCs
   - All implemented methods must use `@override` and `@final` decorators
   - Never add methods not present in the abstract class
   - These are what concrete implementations should inherit from

3. **Concrete Layer** (`src/abc/concrete/`, `src/impl/`): Specific category implementations
   - Inherit from bases, not ABCs
   - Examples: `TerminalCategory`, `EmptyCategory`, `Sets`, `Groups`, `Rings`

### Type System and Imports

**CRITICAL RULE**: Never import classes directly. Always import via `src._types`.

```python
# WRONG - circular import hell
from src.abc_specs.cat_w import _CatW_ABC
from src.abc.bases.cat_w import _CatW_Base

# CORRECT - all imports go through _types
from src._types import CategoryABCs, CategoryBases

# Use like this
class MyCategory(CategoryBases.Category):
    def some_method(self) -> CategoryABCs.OneMorphism:
        ...
```

The `_types.py` file provides:
- `CategoryABCs`: Namespace for abstract class references (for type hints, isinstance checks)
- `CategoryBases`: Namespace for base class references (for inheritance)
- `SageType`, `SympyType`, `PythonType`: Type namespaces for external libraries
- Type guards via `TypeIs` and `TypeGuard` (never use `isinstance` outside `_types.py`)
- `BoolProof`: Dataclass for proof results (TRUE, FALSE, NO_PROOF, PROBABILITY_PROOF)
- `cells`: Namespace for cell data structures (zero, one, two, n)

### Category Hierarchy

The mathematical hierarchy:
```
Cat_{-2} = ∅ (EmptyCategory) 
Cat_{-1} = * (TerminalCategory)
Cat_0 = Discrete Categories ≅ Sets
Cat_1 = Categories  
Cat_2 = Cat (the category of categories)
Cat_ω = All ω-categories
```

Ambient (amb) chain: `x → X → Set → Cat → Cat_ω → *`

Each category tracks its level and ambient category. Levels are validated at construction via `__post_init__`.

### Implementing a New Category

Follow this scaffold structure (from README.md):

```
newcategory/
├── homs/
│   ├── homC.py          # extend CategoryBases.HomC, EndC, AutC
│   ├── homC_x_y.py      # extend CategoryBases.HomC_x_y, EndC_x, AutC_x
│   └── morphism.py      # extend CategoryBases.Morphism, Endomorphism, Automorphism
├── limits/
│   ├── limits.py        # extend Slice, Span, Product, Pullback, Terminal
│   ├── colimits.py      # extend Coslice, Cospan, Coproduct, Pushout, Initial
│   ├── direct_sums.py   # extend CategoryBases.DirectSum
│   └── tensor_products.py # extend CategoryBases.TensorProduct
├── objects.py           # extend CategoryBases.Object
└── category.py          # extend CategoryBases.Category
    # Attach all of the above to the category class
```

**Do NOT write `__init__.py` files** - SageMath does not structure things this way.

Workflow:
1. Scaffold all extension classes first
2. Attach all scaffolds to `category.py`
3. Attempt to instantiate - this catches missing abstract methods immediately

## Code Standards

### Type Safety (Rust-like Python)

This project treats Python like Rust with compile-time guarantees:

- **Every method and object must be strongly typed** - use type hints everywhere
- **Never return `None`** - this is pure mathematics, `None` is not a mathematical object
  - Return the initial category or terminal category instead
- **Never use `isinstance`** - use TypeGuard/TypeIs patterns from `_types.py`
- **Never use `hasattr`** outside `_types.py` - violates strong typing
- **Prefer `match/case` over nested `if`** - use `assert_never` for exhaustiveness
- **Never use `try/except` for flow control** - let errors surface in tests
- **Never use `NotImplementedError`** in concrete classes - use `assert False` to fail tests until design is resolved
- **Never add `type: ignore` comments** - these hide design issues

### Modern Python (3.14+)

- Target Python >= 3.14, use latest language features
- Always use `from __future__ import annotations`
- Use modern generic syntax: `class Box[T]:` not `class Box(Generic[T]):`
- Use `@overload` for dependent return types
- Use `TypeIs` over `TypeGuard` when narrowed type is a subtype
- Use `Unpack[TypedDict]` for kwargs expansion
- Use dataclasses, attrs, pydantic for structured data
- Never use tuples or `dict[str, Any]` for structured returns

### Decorators

Required decorators based on context:
- `@final
    @abstractmethod`: On all ABC methods
- `@override`: On all base class implementations of abstract methods
- `@final`: On all base class implementations (prevents further override)
- `@deal.pre`: For preconditions
- `@deal.post` / `@deal.ensure`: For postconditions
- `@deal.inv`: For class invariants

### Testing Philosophy

**No ad-hoc testing.** All verification goes through `just test`.

Tests must be:
- **Mathematical proofs** of correctness, not smoke tests
- **Concrete and specific** - no `assert result is not None`
- Use real mathematical constructions, never mock data
- Prefer `hypothesis` property-based tests over manual tests
- Use `deal` contracts for invariants
- Never use `pytest.skip` or test skipping
- Cap test suite at 4 CPUs (project rule)

Example of good test:
```python
def test_matrix_multiplication():
    A = Matrix(ZZ, [[1, 2], [3, 4]])
    B = Matrix(ZZ, [[5, 6], [7, 8]])
    expected = Matrix(ZZ, [[19, 22], [43, 50]])
    assert A * B == expected
```

Example of bad test:
```python
def test_matrix_multiplication():
    result = multiply_matrices(A, B)
    assert result is not None  # TOO VAGUE
    assert len(result) > 0     # NOT MATHEMATICAL
```

### Mathematical Correctness

- **Never invent algorithms** - use existing tools from Sage, numpy, GAP, Julia, M2, Singular
- Freely install dependencies via uv - never hedge on availability
- Fail loudly if environment lacks dependencies - no workarounds/fallbacks
- Never import packages within functions - all imports at top level
- Never use `if TYPE_CHECKING` - import types directly
- Prefer Sage abstractions over numpy when available

### BoolProof Pattern

Equality and property checks return `BoolProof` objects, not `bool`:

```python
# Checking properties
if obj.is_terminal_object().is_true():
    ...

if morphism.is_invertible().has_proof():
    ...

# Accumulating proof attempts
proof = BoolProof()
proof += check_strategy_1(...)
if proof.has_proof():
    return proof
proof += check_strategy_2(...)
```

`BoolProof` tracks:
- `kind`: TRUE, FALSE, NO_PROOF, PROBABILITY_PROOF
- `witness_strategy`: Method that succeeded
- `attempted_strategies`: List of attempted methods
- `counterexample`: For FALSE results
- `probability`, `sample_size`: For probabilistic proofs

### Commit Hygiene

- Commit frequently to checkpoint for rollbacks
- Do not modify original docs or code - make new files
- Never commit unless explicitly asked by the user

## Key Files

- `pyproject.toml`: Dependencies, tool configurations (black, ruff, mypy, basedpyright, pytest)
- `justfile`: All development commands
- `AGENTS.md`: Extended coding guidelines (auto-loaded as rules)
- `README.md`: Category implementation patterns
- `src/abc/_types.py`: Central type definitions - READ THIS FIRST
- `src/abc/abstract/`: Mathematical specifications (ABCs)
- `src/abc/bases/`: Partial implementations  
- `src/abc/concrete/`: Concrete category implementations
- `tests/conftest.py`: Shared test fixtures and hypothesis strategies

## Common Patterns

### Creating TypeGuards

All type guards live in `_types.py`:

```python
class CategoryTypeChecks:
    @staticmethod
    def is_morphism(f: Any) -> TypeGuard[CategoryABCs.OneMorphism]:
        return isinstance(f, CategoryABCs.OneMorphism)
    
    @staticmethod
    def is_endomorphism(f: Any) -> TypeGuard[CategoryABCs.Endomorphism]:
        if not CategoryTypeChecks.is_morphism(f):
            return False
        return f.domain.is_equal_to(f.codomain).has_proof()
```

### Deal Contracts

Use `deal` for preconditions, postconditions, and invariants:

```python
@deal.pre(lambda self, n: 0 <= n <= self.level())
@deal.ensure(lambda self, n, result: all(isinstance(c, CategoryABCs.Nontrivial_TwoCategory) for c in result))
def n_cells(self, n: int) -> set[CategoryABCs.Nontrivial_TwoCategory]:
    return self.cells()[n]
```

### Hypothesis Strategies

Define reusable strategies in `conftest.py`:

```python
@st.composite
def categories(draw: st.DrawFn, min_objects: int = 1) -> CategoryABCs.Nontrivial_TwoCategory:
    n_objects = draw(st.integers(min_value=min_objects, max_value=10))
    # ... construct category
    return cat
```

## What NOT to Do

- ❌ Use system Python directly
- ❌ Import abstract classes directly (use `_types.CategoryABCs`)
- ❌ Import base classes directly (use `_types.CategoryBases`)
- ❌ Return `None` from mathematical functions
- ❌ Use `isinstance` outside `_types.py`
- ❌ Use `hasattr` outside `_types.py`
- ❌ Add `type: ignore` comments
- ❌ Use `NotImplementedError` in concrete classes
- ❌ Skip tests with `pytest.skip`
- ❌ Use mock data in tests
- ❌ Write `__init__.py` files
- ❌ Import within functions
- ❌ Use `if TYPE_CHECKING` blocks
- ❌ Invent algorithms - use existing mathematical libraries
- ❌ Commit changes unless explicitly asked

## Troubleshooting

### Type errors with Sage types

Sage types may show as unknown to type checkers. This is expected. Check `pyproject.toml` for configured `extraPaths` pointing to Sage source.

### Import errors

If seeing circular imports, you're probably importing classes directly instead of through `_types.py`.

### Tests failing on `BoolProof`

Remember to call `.is_true()`, `.has_proof()`, etc. on `BoolProof` objects:
```python
# WRONG
if obj.is_terminal():

# CORRECT  
if obj.is_terminal().has_proof():
```

### Deal contract failures

Deal contracts validate at runtime. If a contract fails, it means either:
1. The precondition/postcondition is wrong (fix the contract)
2. The implementation violates the contract (fix the implementation)

Never silence contract failures.