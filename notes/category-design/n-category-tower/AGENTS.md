<!--
Origin: gitclones/integral_lattice/cat/AGENTS.md
Copied 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of
this corpus.
-->

# Contributing Guidelines

- Use git commits frequently to checkpoint for rollbacks.
- Do not modify original docs or code. Make new ones.
- Use a proper justfile to automate testing, linting, type-checking.
    - Use a uv venv for all commands. Never run the system python.
    - `just test` must invoke all linting, all type-checking, and all tests automatically, and must fail loudly if any of these fail.
    - Use tools like `autopep8`, `black`, `flake8`, `mypy`, `basedpyright`, etc for formatting, linting, and type-checking.
- All scripts are sage scripts, not raw python (so e.g. do not import `sage.all`).
- External dependencies are good and useful. Heavily rely on sage constructs, numpy, GAP/Julia/M2/Singular bridges and libraries. 
    - Never invent a mathematical algorithm from scratch, use known and existing tools.
    - Freely install all dependencies in the uv venv. Never hedge on them not being available.
    - Use a proper pyproject.toml to track dependencies.
    - Never implement "workarounds" or "fallbacks" for environment issues. Fail loudly until the environment has ALL dependencies.
- Write proper *mathematical* tests for new code, that assert mathematical correctness in nontrivial examples. Heavily use tools like `pytest`, `hypothesis`, `deal`, `crosshair`, `pynguin`, etc.
    - Never use pytest.skip, unittest.skip, or any other form of test skipping.
    - Never use mock data, rely on real, concrete, specific mathematical constructions only.
- Do not hesitate to require heavy system dependencies, e.g. Bliss, Nauty, etc.
- Focus on MVPs first. Do not bloat simple methods into hundreds of lines of comments and documentation before it has even been proved to work.
- Every method and every object must be strongly typed. Use type hints everywhere.
- Target python >= 3.14. Never hedge on older versions. Use latest language features.
- Always use `from __future__ import annotations` to enable postponed evaluation of annotations.
- Minimize the use of `try/catch` blocks; never use them for flow control. Let errors surface in tests to inform future development to actually handle currently unhandled cases.
- Heavily lean on constructs like `dataclasses`, `attrs`, `pydantic` models, `TypedDict`, `NamedTuple`, `Enum`, etc to enforce strong typing and data integrity.
- Never raise `NotImplementedError` or stub functionality in non-abstract class. This means there is a design failure, e.g. there is not an algorithm available to implement the functionality. This should be clearly communicated at checkpoint intervals, to receive feedback from the user on whether or not to change the specification. When in doubt, search the internet for actual implementations or algorithms and use them; otherwise use `assert False` to purposefully flag the method and force it to fail all tests that use it until the design is changed or an algorithm is found.
- Prefer automatically generated tests over manual tests. If one has to write tests by hand, ensure they are nontrivial. E.g. no constructs like `result is not None` or `len(result) > 0`. Instead, prefer constructs like `input = ...{a specific matrix}...` and `assert result == ...{a specific matrix}`.
- Encode the documentation and implementation guidelines as ABCs and/or Protocols, potentially with Generics, (e.g. `Cat_w_Interface` with `@abstract_method` decorators) that can be separated from concrete implementations (e.g. `class Sets(Cat_w_interface)`) so that documentation alignment can be assessed separately from implementation, and classes can not be instantiated at runtime without implementing all ABC methods.
- Deeply reconsider using raw libraries like numpy, especially when there are already equivalent sage abstractions which are HEAVILY preferred. 
- Never import packages within a function -- all imports should be at the top level.
- Never implement `if TYPE_CHECKING` clauses: import the packages or types directly.
- HEAVILY prefer `hypothesis` tests and `deal` contracts over manual tests.

# Typing Guidelines I

## 0. General versioning and syntax guidance

1. **Target modern Python versions (3.13+ where possible).**

   * Several features discussed (e.g. `TypeIs`, `type` statements) require very recent Python versions.
   * The article assumes Python ≥ 3.13 and implicitly recommends upgrading if you want to use the full toolkit.

2. **Adopt the modern generic “bracket syntax” in Python 3.12+.**

   * Instead of older patterns like:

     ```python
     from typing import Generic, TypeVar
     T = TypeVar("T")

     class Box(Generic[T]):
         ...
     ```
   * Prefer the more concise:

     ```python
     T = TypeVar("T")

     class Box[T]:
         ...
     ```
   * Same idea applies to other generic definitions (functions, classes, etc.).

---

## 1. `assert_never` and the bottom type `Never`

3. **Use `assert_never` to enforce exhaustiveness of unions in conditionals.**

   * For a union type:

     ```python
     type Shape = Circle | Rectangle | Triangle
     ```

     and a conditional:

     ```python
     def area(shape: Shape) -> float:
         if isinstance(shape, Circle):
             ...
         elif isinstance(shape, Rectangle):
             ...
         else:
             assert_never(shape)  # This should never be reachable
     ```
   * When `Shape` is extended (e.g. add `Polygon`), the type checker will flag that the `else` branch is no longer unreachable, forcing you to add a case.

4. **Rely on `Never` as the bottom type to detect logically impossible branches.**

   * `assert_never(value)` tells the checker: “if this line is reachable, `value` must be of type `Never`,” which is impossible.
   * Any reachable path to `assert_never` on a non-`Never` variable becomes a static type error.
   * This is the mechanism that makes exhaustiveness checking work.

5. **Use `assert_never` instead of silent “default” branches in pattern matching.**

   * Rather than a generic `else: raise ValueError("unknown")`, explicitly marking the branch as impossible provides stronger static guarantees.

---

## 2. `get_args` with `Literal` and other parameterized types

6. **Avoid duplicating `Literal` values between types and runtime lists.**

   * Anti-pattern:

     ```python
     type Color = Literal["red", "green", "blue"]

     VALID_COLORS = ["red", "green", "blue"]  # Duplicate source of truth
     ```
   * This requires keeping both the type and the runtime list in sync manually.

7. **Use `typing.get_args` to derive the runtime collection from the type.**

   * Recommended pattern:

     ```python
     from typing import Literal, get_args

     type Color = Literal["red", "green", "blue"]

     VALID_COLORS = list(get_args(Color))
     ```
   * The `Literal` definition becomes the single source of truth; both static checking and runtime validation derive from it.

8. **Generalize `get_args` beyond `Literal` where appropriate.**

   * You can also use `get_args` with unions or other parameterized types when you need runtime reflection that matches static annotations.

---

## 3. User-defined predicates: `TypeGuard` vs `TypeIs`

### 3.1. `TypeGuard`

9. **Use `TypeGuard` to define reusable predicates that narrow types.**

   * Instead of inline `isinstance` checks repeated across the codebase:

     ```python
     def is_int(x: object) -> TypeGuard[int]:
         return isinstance(x, int)
     ```
   * The type checker understands that inside `if is_int(x):`, `x` is an `int`.

10. **Apply `TypeGuard` especially for invariant containers where standard subtyping fails.**

    * Example: `list[float]` is not a subtype of `list[object]`.
    * A predicate:

      ```python
      def is_list_of_floats(xs: list[object]) -> TypeGuard[list[float]]:
          ...
      ```

      tells the checker: “On the `True` branch, treat `xs` as `list[float]`,” even though that isn’t a standard subtype relation.

11. **Understand that `TypeGuard` only narrows the *positive* branch.**

    * On `if is_list_of_floats(xs):`, `xs` narrows to `list[float]`.
    * On `else:`, the type of `xs` is unchanged; the type checker does not compute “the complement.”

12. **Use `TypeGuard` when the target type is not a genuine subtype of the input.**

    * It is appropriate when you want “assert this is that” semantics, even if the type relation is structurally incompatible or involves invariance.

### 3.2. `TypeIs`

13. **Prefer `TypeIs` over `TypeGuard` when the narrowed type is a *subtype* of the input type.**

    * `TypeIs[T]` enables **bi-directional** narrowing:

      * In the `if` branch, the variable narrows to `T`.
      * In the `else` branch, the variable narrows to “original type minus `T`” (set subtraction on the union).

14. **Use `TypeIs` for precise narrowing over unions.**

    * For a union:

      ```python
      type Value = int | str | float

      def is_int(value: Value) -> TypeIs[int]:
          return isinstance(value, int)
      ```
    * Then:

      ```python
      if is_int(v):
          # v: int
      else:
          # v: str | float  (negative branch narrowed)
      ```

15. **Respect the subtype constraint for `TypeIs`.**

    * The narrowed type must be a valid subtype of the input type.
    * Example where `TypeIs` is valid:

      * Input: `Value = int | str | float`, narrowed: `int`.
    * Example where `TypeIs` is *not* valid:

      * Input: `list[object]`, narrowed: `list[int]`.
      * `list[int]` is not a subtype of `list[object]` because the container is invariant.

16. **Reserve `TypeGuard` for structurally incompatible/invariant relations.**

    * When the narrowed type cannot be expressed as a clean subtype and set subtraction would make no sense, use `TypeGuard` instead of `TypeIs`.

---

## 4. Overloading: correlate arguments with return types

17. **Use `@overload` to express that return types depend on argument values.**

    * Naive implementation:

      ```python
      def parse(data: str, as_json: bool) -> dict | list[str]:
          ...
      ```

      The return type is always `dict | list[str]` at call sites.

18. **Provide overloads for different argument patterns.**

    * For example:

      ```python
      from typing import overload

      @overload
      def parse(data: str, as_json: Literal[True]) -> dict: ...
      @overload
      def parse(data: str, as_json: Literal[False]) -> list[str]: ...

      def parse(data: str, as_json: bool) -> dict | list[str]:
          ...
      ```
    * Now:

      * `parse("...", True)` is statically `dict`.
      * `parse("...", False)` is statically `list[str]`.

19. **Keep the implementation in a single function with the union return type.**

    * Overload stubs have `...` bodies and are not executed.
    * The concrete implementation must be compatible with all overload declarations and can use runtime branching as usual.

20. **Use overloading to avoid extra `isinstance` checks at call sites.**

    * With overloads, callers get precise types directly and do not have to re-narrow the result manually.

---

## 5. `Unpack` for keyword-argument expansion

21. **Define a mapping-like type (e.g. `TypedDict`) for grouped keyword arguments.**

    * Example:

      ```python
      from typing import TypedDict

      class ModelConfig(TypedDict):
          learning_rate: float
          batch_size: int
          optimizer: str
      ```

22. **Use `Unpack` to expand that mapping into a function’s `**kwargs`.**

    * Example:

      ```python
      from typing import Unpack

      def train_model(**config: Unpack[ModelConfig]) -> None:
          ...
      ```
    * The type checker now knows exactly which keys are required and the type of each value.

23. **Leverage `Unpack` to catch missing or extra keyword arguments at type-check time.**

    * If you call:

      ```python
      train_model(learning_rate=0.01, batch_size=32, optimizer="adam")
      ```

      this type-checks.
    * If you miss a key or pass an unexpected one, the type checker reports it before runtime.

24. **Use `Unpack` to keep configuration definitions DRY.**

    * One definition (`ModelConfig`) drives:

      * Runtime dictionary structure,
      * Static typing for call sites,
      * Documentation of configuration options.

---

## 6. `Concatenate` + `ParamSpec` for decorators that alter signatures

25. **Avoid annotating decorators as `Callable[..., R]` unless absolutely necessary.**

    * The common shortcut:

      ```python
      from typing import Callable, TypeVar

      R = TypeVar("R")

      def log_calls(fn: Callable[..., R]) -> Callable[..., R]:
          ...
      ```

      discards all information about the function’s parameters, so callers lose typed argument checking for decorated functions.

26. **Use `ParamSpec` to represent “the parameters of the wrapped function”.**

    * Example:

      ```python
      from typing import ParamSpec

      P = ParamSpec("P")
      R = TypeVar("R")
      ```

27. **Use `Concatenate` when the decorator injects or removes a leading parameter.**

    * Scenario: a decorator that injects a `logging.Logger` internally instead of exposing it to callers.
    * Annotate the decorator approximately as:

      ```python
      from typing import Callable, Concatenate
      import logging

      def log_calls(
          fn: Callable[Concatenate[logging.Logger, P], R],
      ) -> Callable[P, R]:
          ...
      ```

      * The wrapped function expects `(Logger, *P)` parameters.
      * The returned function exposes only `P` to the caller; the `Logger` is supplied internally.

28. **Use this pattern for decorators that adjust the public signature.**

    * Common cases:

      * Injected context (`request`, `db_session`, `user`, `logger`, etc.).
      * Decorators that strip an internal parameter from the public API while keeping the rest unchanged.

29. **Preserve both positional and keyword parameters via `ParamSpec`.**

    * `P` can represent arbitrary combinations of `*args` and `**kwargs`.
    * `Callable[P, R]` and `Callable[Concatenate[Extra, P], R]` ensure the type checker maintains the full parameter structure across decoration.

---

Summary:

* Upgrade to recent Python versions and use modern generic syntax.
* Enforce exhaustiveness with `assert_never` and `Never`.
* Use `get_args` to avoid duplicating `Literal` definitions at runtime.
* Define reusable, typed predicates with `TypeGuard` and prefer `TypeIs` whenever the narrowed type is a true subtype.
* Use `@overload` to make return types depend on arguments in a statically visible way.
* Use `Unpack` for typed keyword-argument expansion from a mapping type.
* Use `Concatenate` + `ParamSpec` to correctly type decorators that add/remove parameters while preserving the underlying function's signature.

---

# Typing Guidelines II

Here is a feature-by-feature list of the concrete practices advocated in “Writing Python like it’s Rust,” organized by theme.

---

## 0. Overall philosophy

1. **Adopt a “soundness-first” mindset in Python, inspired by Rust.**

   * Design APIs so that it is hard or impossible to misuse them (“make illegal states unrepresentable”), rather than relying on runtime checks and documentation. ([Kobzol’s blog][1])

2. **Use a static type checker (e.g. Pyright, PyCharm’s analyzer) and let it guide design.**

   * Treat type errors as early feedback, analogous to Rust compile errors. ([Kobzol’s blog][1])

---

## 1. Type hints and interfaces

3. **Type all function signatures and class attributes.**

   * Prefer:

     ```python
     def find_item(
         records: list[Item],
         check: Callable[[Item], bool],
     ) -> Item | None:
         ...
     ```

     over untyped `def find_item(records, check):`. ([Kobzol’s blog][1])

4. **Use type hints to document:**

   * The shape of inputs and outputs,
   * Whether failure is signaled via `None`, exceptions, etc. ([Kobzol’s blog][1])

5. **Let the type checker enforce that callers are updated when signatures change.**

   * Changing parameter or return types without updating uses should become a type error, not a hidden runtime trap. ([Kobzol’s blog][1])

6. **Treat “requires 5 nested type hints” as a smell.**

   * If a parameter’s type is something like `int | tuple[str, str] | dict[str, int]`, treat that as a sign that the design is too complicated and should be refactored, not as an excuse to avoid typing. ([Kobzol’s blog][1])

---

## 2. Dataclasses vs tuples/dicts

7. **Do not return “opaque” tuples for multi-value results.**

   * Avoid:

     ```python
     def find_person(...) -> tuple[str, str, int]:
         ...
     ```

     where the meaning of each position is unclear. ([Kobzol’s blog][1])

8. **Do not return untyped dictionaries (`dict[str, Any]`) as a “structured result” escape hatch.**

   * This loses information about which keys exist, their types, and makes refactors (renames/removals) hard to track. ([Kobzol’s blog][1])

9. **Instead, define dataclasses to represent structured data.**

   * Example:

     ```python
     @dataclass
     class City:
         name: str
         zip_code: int

     @dataclass
     class Person:
         name: str
         city: City
         age: int

     def find_person(...) -> Person:
         ...
     ```

10. **Use dataclasses (or similar) to:**

    * Make return values self-documenting,
    * Enable IDE autocompletion for attributes,
    * Allow refactors (e.g. renames) to be tracked by the type checker/IDE. ([Kobzol’s blog][1])

11. **Consider `TypedDict` or `NamedTuple` for field-objects when appropriate.**

    * These are mentioned as alternatives to dataclasses when they better fit the use case. ([Kobzol’s blog][1])

---

## 3. Algebraic data types (ADTs) via unions

12. **Model closed sets of variants as explicit union types of dataclasses.**

    * Example:

      ```python
      @dataclass
      class Header:
          protocol: Protocol
          size: int

      @dataclass
      class Payload:
          data: str

      @dataclass
      class Trailer:
          data: str
          checksum: int

      Packet = Header | Payload | Trailer
      ```

13. **Use unions to encode “sum types” rather than ad-hoc inheritance when the variant set is closed.**

    * When you know all variants upfront and want exhaustiveness checks, ADT-like unions are preferred over open-ended OOP interfaces. ([Kobzol’s blog][1])

14. **Discriminate union variants with `isinstance` or `match`.**

    * Example with `isinstance`:

      ```python
      def handle_is_instance(packet: Packet) -> None:
          if isinstance(packet, Header):
              ...
          elif isinstance(packet, Payload):
              ...
          elif isinstance(packet, Trailer):
              ...
          else:
              assert False  # or raise, or assert_never
      ```
    * Example with `match`:

      ```python
      def handle_pattern_matching(packet: Packet) -> None:
          match packet:
              case Header(protocol, size):
                  ...
              case Payload(data):
                  ...
              case Trailer(data, checksum):
                  ...
              case _:
                  assert False
      ```

15. **Use `typing.assert_never` rather than `assert False` for unreachable branches.**

    * `assert False` can be optimized out with `python -O`; `typing.assert_never` clearly signals to the type checker that this branch must be impossible, enabling “compile-time” exhaustiveness enforcement. ([Kobzol’s blog][1])

16. **Define unions outside the member classes to reduce coupling.**

    * Classes (`Header`, `Payload`, `Trailer`) remain oblivious to which unions they participate in.
    * You can define multiple unions over the same classes:

      ```python
      Packet = Header | Payload | Trailer
      PacketWithData = Payload | Trailer
      ```

17. **Exploit unions for typed (de)serialization.**

    * Use libraries like `pyserde` that understand type annotations and can automatically serialize/deserialize union types:

      ```python
      @dataclass
      class Data:
          packet: Packet

      serialized = serde.to_dict(Data(packet=Trailer(...)))
      deserialized = serde.from_dict(Data, serialized)
      ```

18. **Use unions to version configuration/data formats.**

    * Example:

      ```python
      Config = ConfigV1 | ConfigV2 | ConfigV3
      ```

      Deserializing `Config` lets you read all historical config formats with one type, maintaining backwards compatibility. ([Kobzol’s blog][1])

---

## 4. Newtypes for domain-specific scalar types

19. **Wrap primitive types (e.g. `int`) in `NewType` to prevent mix-ups.**

    * Example:

      ```python
      CarId = NewType("CarId", int)
      DriverId = NewType("DriverId", int)

      class Database:
          def get_car_id(self, brand: str) -> CarId: ...
          def get_driver_id(self, name: str) -> DriverId: ...
          def get_ride_info(self, car_id: CarId, driver_id: DriverId) -> RideInfo: ...
      ```

20. **Use NewType to catch argument-swapping bugs that would be invisible with plain ints/floats.**

    * Passing `(driver_id, car_id)` where `(car_id, driver_id)` is expected becomes a type error instead of a silent logical bug. ([Kobzol’s blog][1])

21. **Apply NewType systematically for conceptually different kinds of the same primitive.**

    * Different ID types (`UserId`, `OrderId`), or different physical dimensions (`Speed`, `Length`, `Temperature`), to avoid accidental mixing. ([Kobzol’s blog][1])

---

## 5. “Construction functions” instead of overloaded constructors

22. **Avoid stuffing all construction logic into a single overloaded `__init__` with many orthogonal parameters.**

    * This leads to tangled initialization rules and invalid combinations of parameters. ([Kobzol’s blog][1])

23. **Use named factory/constructor functions with explicit semantics.**

    * For example, via static methods:

      ```python
      class Rectangle:
          @staticmethod
          def from_x1x2y1y2(x1: float, x2: float, y1: float, y2: float) -> "Rectangle":
              ...

          @staticmethod
          def from_tl_and_size(top: float, left: float,
                               width: float, height: float) -> "Rectangle":
              ...
      ```

24. **Choose construction functions that prohibit invalid parameter combinations.**

    * Users cannot accidentally combine incompatible subsets of parameters (e.g. `y1` with `width`) because each factory defines a coherent construction path. ([Kobzol’s blog][1])

---

## 6. Encoding invariants in types (typestate-like patterns)

### 6.1. Client state machine

25. **Do not encode multiple exclusive states in one mutable “god” object with docstring rules.**

    * Example of what to avoid: a `Client` with methods `connect`, `authenticate`, `send_message`, `close`, plus doc-comments like “do not call `send_message` before `connect` and `authenticate`, do not call `close` twice,” etc. ([Kobzol’s blog][1])

26. **Split mutually exclusive states into distinct types (typestate pattern).**

    * Use separate types to encode “connected” and “authenticated” invariants. ([Kobzol’s blog][1])

27. **Use a free function to construct the initial “connected” state.**

    * Example:

      ```python
      def connect(address: str) -> ConnectedClient | None:
          ...
      class ConnectedClient:
          def authenticate(...): ...
          def send_message(...): ...
          def close(...): ...
      ```

      * Only `ConnectedClient` exists; there is no “unconnected `Client`” that can be misused. ([Kobzol’s blog][1])

28. **Introduce a separate type for the “authenticated” state.**

    * Example:

      ```python
      class ConnectedClient:
          def authenticate(self, ...) -> AuthenticatedClient | None: ...

      class AuthenticatedClient:
          def send_message(self, msg: str) -> None: ...
          def close(self) -> None: ...
      ```

      * Only `AuthenticatedClient` has `send_message` available, so calling it before authentication is made impossible by the type system. ([Kobzol’s blog][1])

29. **Handle “resource closed” invariants with context managers instead of `close` methods.**

    * Replace manual `close` with:

      ```python
      with connect(...) as client:
          client.send_message("foo")
      # client is closed here
      ```

      * You eliminate the possibility of double-close via the public API. ([Kobzol’s blog][1])

### 6.2. Strongly-typed bounding boxes

30. **Split conceptually distinct shapes into separate types rather than a single ambiguous one.**

    * For bounding boxes: differentiate normalized (`[0, 1]` coordinates) vs denormalized (pixel-space) boxes. ([Kobzol’s blog][1])

31. **Define separate dataclasses for each representation.**

    * Initial version:

      ```python
      @dataclass
      class NormalizedBBox:
          left: float
          top: float
          width: float
          height: float

      @dataclass
      class DenormalizedBBox:
          left: float
          top: float
          width: float
          height: float
      ```

32. **Factor out shared fields into a common base to reduce duplication.**

    * Either via composition or inheritance:

      ```python
      @dataclass
      class BBoxBase:
          left: float
          top: float
          width: float
          height: float

      # Composition
      class NormalizedBBox:
          bbox: BBoxBase

      class DenormalizedBBox:
          bbox: BBoxBase

      # or inheritance
      class NormalizedBBox(BBoxBase): ...
      class DenormalizedBBox(BBoxBase): ...
      ```

33. **Add runtime assertions to check invariants that types themselves cannot express.**

    * E.g. in `NormalizedBBox.__post_init__`:

      ```python
      def __post_init__(self) -> None:
          assert 0.0 <= self.left <= 1.0
          ...
      ```

34. **Provide conversion methods between representations on the base class.**

    * Example:

      ```python
      class BBoxBase:
          def as_normalized(self, size: Size) -> "NormalizedBBox": ...
          def as_denormalized(self, size: Size) -> "DenormalizedBBox": ...

      class NormalizedBBox(BBoxBase):
          def as_normalized(self, size: Size) -> "NormalizedBBox":
              return self
          def as_denormalized(self, size: Size) -> "DenormalizedBBox":
              return self.denormalize(size)
      ```

      * Similarly for `DenormalizedBBox`. ([Kobzol’s blog][1])

35. **Use `typing.Self` (Python 3.11+) for fluent APIs that preserve concrete subclass types.**

    * For shared methods on the base:

      ```python
      class BBoxBase:
          def move(self, x: float, y: float) -> typing.Self:
              ...
      ```

      * Then `bbox.move(...)` is typed as `NormalizedBBox` if `bbox` was `NormalizedBBox`, not just `BBoxBase`. ([Kobzol’s blog][1])

### 6.3. Safer mutexes

36. **Avoid separate “lock + data” designs where the link between them is informal.**

    * Standard patterns like:

      ```python
      mutex = Lock()
      data = []

      def thread_fn(data):
          mutex.acquire()
          data.append(1)
          mutex.release()

      # elsewhere
      data.append(2)  # access without locking
      ```

      make it easy to forget locking before accessing the data. ([Kobzol’s blog][1])

37. **Use context managers for locks (always `with lock:`).**

    * Leverage Python’s context manager support for automatic unlock, similar to RAII in Rust/C++. ([Kobzol’s blog][1])

38. **Wrap the protected value *inside* a generic mutex type.**

    * Define:

      ```python
      T = TypeVar("T")

      class Mutex(Generic[T]):
          def __init__(self, value: T):
              self.__value = value
              self.__lock = Lock()

          @contextlib.contextmanager
          def lock(self) -> ContextManager[T]:
              self.__lock.acquire()
              try:
                  yield self.__value
              finally:
                  self.__lock.release()
      ```

39. **Ensure that the only way to access the protected data is via the mutex guard.**

    * Use:

      ```python
      mutex = Mutex([])
      with mutex.lock() as value:
          value.append(1)
      ```

      * `value` is correctly typed (`list[...]`) inside the `with` block.
      * Outside, you don’t even see the raw list unless you deliberately subvert the API. ([Kobzol’s blog][1])

40. **Accept that Python cannot enforce Rust-level guarantees, but make misuse non-trivial.**

    * You can still violate invariants (e.g. by holding extra references), but the API design biases you toward correct use. ([Kobzol’s blog][1])

---

Summary:

* Use type hints pervasively and let them shape your APIs.
* Replace unstructured tuples/dicts with dataclasses or similar field-objects.
* Emulate ADTs with unions of dataclasses and pattern matching, plus `assert_never`-style exhaustiveness.
* Introduce NewTypes for semantically distinct scalars.
* Use named “construction functions” instead of overburdened constructors.
* Encode object states and invariants in the type graph (typestate pattern), and use context managers and generic wrappers (e.g. `Mutex[T]`) to restrict how resources and data can be accessed.

[1]: https://kobzol.github.io/rust/python/2023/05/20/writing-python-like-its-rust.html "Writing Python like it’s Rust | Kobzol’s blog"

# External Reviews

# Using Gemini CLI for Large Codebase Analysis

When analyzing large codebases or multiple files that might exceed context limits, use the Gemini CLI with its massive
context window. Use `gemini -p` to leverage Google Gemini's large context capacity.

## File and Directory Inclusion Syntax

Use the `@` syntax to include files and directories in your Gemini prompts. The paths should be relative to WHERE you run the
gemini command:

### Examples:

**Single file analysis:**
```bash
gemini -p "@src/main.py Explain this file's purpose and structure"
```

**Multiple files:**
```bash
gemini -p "@package.json @src/index.js Analyze the dependencies used in the code"
```

**Entire directory:**
```bash
gemini -p "@src/ Summarize the architecture of this codebase"
```

**Multiple directories:**
```bash
gemini -p "@src/ @tests/ Analyze test coverage for the source code"
```

**Current directory and subdirectories:**
```bash
gemini -p "@./ Give me an overview of this entire project"
```

**Or use --all_files flag:**
```bash
gemini --all_files -p "Analyze the project structure and dependencies"
```

### Implementation Verification Examples

**Check if a feature is implemented:**
```bash
gemini -p "@src/ @lib/ Has dark mode been implemented in this codebase? Show me the relevant files and functions"
```

**Verify authentication implementation:**
```bash
gemini -p "@src/ @middleware/ Is JWT authentication implemented? List all auth-related endpoints and middleware"
```

**Check for specific patterns:**
```bash
gemini -p "@src/ Are there any React hooks that handle WebSocket connections? List them with file paths"
```

**Verify error handling:**
```bash
gemini -p "@src/ @api/ Is proper error handling implemented for all API endpoints? Show examples of try-catch blocks"
```

**Check for rate limiting:**
```bash
gemini -p "@backend/ @middleware/ Is rate limiting implemented for the API? Show the implementation details"
```

**Verify caching strategy:**
```bash
gemini -p "@src/ @lib/ @services/ Is Redis caching implemented? List all cache-related functions and their usage"
```

**Check for specific security measures:**
```bash
gemini -p "@src/ @api/ Are SQL injection protections implemented? Show how user inputs are sanitized"
```

**Verify test coverage for features:**
```bash
gemini -p "@src/payment/ @tests/ Is the payment processing module fully tested? List all test cases"
```

### When to Use Gemini CLI

Use gemini -p when:
- Analyzing entire codebases or large directories
- Comparing multiple large files
- Need to understand project-wide patterns or architecture
- Current context window is insufficient for the task
- Working with files totaling more than 100KB
- Verifying if specific features, patterns, or security measures are implemented
- Checking for the presence of certain coding patterns across the entire codebase

### Important Notes

- Paths in @ syntax are relative to your current working directory when invoking gemini
- The CLI will include file contents directly in the context
- No need for --yolo flag for read-only analysis
- Gemini's context window can handle entire codebases that would overflow Claude's context
- When checking implementations, be specific about what you're looking for to get accurate results