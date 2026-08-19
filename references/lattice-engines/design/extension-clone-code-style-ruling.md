# Code Style Requirements for AI Agents

## Type Annotations

- **Strict typing annotations required** - All functions, variables, and class members must have explicit type annotations
- **No `type: ignore` comments** - If type checking fails, fix the underlying code, never suppress with comments
- **No `Any` or `Unknown` types** - Use specific types or bounded type variables instead
  - If a value could be multiple concrete types, use `Union` or `|` syntax
  - Use overloads for functions with multiple valid type signatures
  - Use generics and type variables when dealing with type relationships

## Runtime Execution

- **All scripts must be run with `uv` or `sage` directly**
  - Use `uv run` for Python scripts
  - Use `sage` command for SageMath code
  - Never rely on installed packages; dependencies must be resolved through uv or sage
- **Use system sage, never attempt to install as a dependency**
  - If SageMath functionality is needed, assume `sage` is available on the system
  - Do not add sage to `pyproject.toml` dependencies
  - Call sage as an external command when needed

## Control Flow

- **Use `case`/`match` for exhaustive checks** (Python 3.10+)
  - Prefer pattern matching over if/elif chains
  - Ensure all cases are handled; use `case _:` as fallback only when appropriate
  - Leverage exhaustiveness checking for enum-like patterns

## Type Safety & Semantic Clarity

- **Minimize raw primitive types**
  - Avoid `str`, `int`, `float` for domain-specific values
  - Create wrapper types (dataclasses, TypedDict, NewType) for semantic clarity
  - Example: Use `UserId = NewType('UserId', int)` instead of bare `int`
  - Example: Use dataclasses for structured data instead of dicts with string keys
- **Use wrapper types for maximum semantic expression and safety**
  - Strongly typed return values prevent silent bugs
  - Self-documenting code through types reduces comments needed

## Validation

- **Always run Python compile check and pyright on single Python files after editing**
  ```bash
  python3 -m py_compile <file>
  pyright <file>
  ```
  - This ensures no syntax errors and all type violations are caught
  - Do not commit Python files that fail these checks
