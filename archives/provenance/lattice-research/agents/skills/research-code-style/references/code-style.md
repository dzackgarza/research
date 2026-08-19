# Research Code Style Reference

This is the canonical detailed contribution and code-style reference for the research repo.

## Contents

- [Code Style](#code-style)
  - [Mathematical Prose](#mathematical-prose)
  - [Assertions Over Exceptions](#assertions-over-exceptions)
  - [No Try/Except](#no-tryexcept)
  - [Glue, Not Math](#glue-not-math)
  - [No Backward Compatibility](#no-backward-compatibility)
  - [No Needless Indirection](#no-needless-indirection)
  - [No Stub Implementations in Specs](#no-stub-implementations-in-specs)
  - [Single Source of Truth (SSOT)](#single-source-of-truth-ssot)
  - [No Internal Renaming](#no-internal-renaming)
  - [No Optional Arguments](#no-optional-arguments)
  - [No `__all__` Exports](#no-all-exports)
  - [No Optional Types](#no-optional-types)
  - [Introspection Red Flags](#introspection-red-flags)
  - [No `del` in Abstract or Overload Bodies](#no-del-in-abstract-or-overload-bodies)
  - [No `globals()` Manipulation or `importlib` Imports](#no-globals-manipulation-or-importlib-imports)
  - [Semantic Checks Over Manual Implementation](#semantic-checks-over-manual-implementation)
  - [Backend Encapsulation](#backend-encapsulation)
  - [Code Structure](#code-structure)
  - [Validation and Equality](#validation-and-equality)
  - [Standard Methods](#standard-methods)
  - [Typing](#typing)
  - [Error Handling (String Matching)](#error-handling-string-matching)
  - [Iteration and Cardinality](#iteration-and-cardinality)
  - [Avoid Non-Obviously-Correct Code](#avoid-non-obviously-correct-code)
  - [Class Hierarchy](#class-hierarchy)
  - [Pydantic Constructors](#pydantic-constructors)
  - [Manual Calculations Require Citations](#manual-calculations-require-citations)
  - [Backend Isolation](#backend-isolation)
  - [Assertions Mirror Literature](#assertions-mirror-literature)
  - [TDD-First: Tests Must Have Sources](#tdd-first-tests-must-have-sources)
  - [Identity vs Equality](#identity-vs-equality)
  - [No Dataclasses](#no-dataclasses)
  - [No Re-Export Files](#no-re-export-files)
  - [Abstract Base Classes](#abstract-base-classes)

## Reference Body

# Contributing Guidelines

## Code Style

### Mathematical Prose

All code must read like mathematical prose, and semantically follow either a
**definition** or a **theorem**, preferably cited.

**Bad example:** Computing the generator of an ideal $(c_1, c_2, \dots, c_n)$ in
$\mathbb{Z}$ by computing a gcd.

**Good example:**
```python
I = ZZ.ideal([...])
assert len(I.gens()) == 1
return I.gens()[0]
```

This is superior for several reasons:

- **Encodes mathematical expectations:** The `assert len(I.gens()) == 1` states the
  expectation that we are in a principal ideal domain and the ideal is principal -- not
  just that the computation succeeded, but that the mathematical preconditions hold.

- **Provably correct by reading it:** The code explicitly states the problem ("find the
  generator of an ideal") and the solution ("compute and return the generator"). There
  is no ambiguity about what is being computed or why.

- **Generalizable to other rings:** The pattern
  `assert len(I.gens()) == 1; return I.gens()[0]` works for any ring where ideals are
  principal, not just $\mathbb{Z}$. The assertion is the mathematical contract.

- **Self-documenting correctness:** No separate citation is needed to verify the code
  is correct -- the assertion itself is the mathematical guarantee.

### Assertions Over Exceptions

Never raise an error, especially not `NotImplementedError`. Instead, all mathematical
code must **assert** the mathematical conditions under which the algorithm/code is
written to work.

**Bad example:**
```python
if not L.is_definite():
    raise NotImplementedError("...")
```

**Good example:**
```python
assert L.is_definite(), "This algorithm currently only works for definite lattices"
# continue algorithm
```

The assertion documents the precondition: "This algorithm is *defined* only for definite
lattices." It does not say "the algorithm fails on indefinite lattices" -- it says "this
code does not claim to work there."
The algorithm is not incomplete; it is *defined* only for the stated domain.

### No Try/Except

Never use `try`/`except`. Mathematical code should **never** throw errors under expected
conditions. It is not typical user-facing software.
It should never attempt to "massage" malformed inputs, or "fail gracefully."

A mathematical function doesn't have an "error" output in mathematical theory, ever.
It is well-defined on an exact set of inputs, and ill-defined on other inputs.
Gate early with assertions on domain containment.

**Rule:** If you think code **must** use error-handling, this must be designed and
specifically signed off by a user, with extensive comments on why it is an exception to
this rule (extremely rare).

### Glue, Not Math

This codebase should not be doing nontrivial mathematics itself.
It is meant to be **glue** between existing implementations, and should primarily
consist of data manipulation, conversion, and feeding into existing mathematical code
(e.g., Sage, Julia, Singular, GAP, etc.).

We do not want to "own" the mathematical correctness of anything -- we use existing
implementations to minimize the surface area we need to check.
Any code attempting to do nontrivial mathematics *internally* is likely wrong, and
should be a simple wrapper/delegator to existing code elsewhere.

**Bad example:** Computing a generator of an ideal in $\mathbb{Z}$ by manually computing
a gcd.
This implicitly applies a theorem about ideals in PIDs which are Euclidean domains
-- extra mathematical surface area that must be checked internally.

**Good example:** `I.gens()` -- our surface area is merely constructing the ideal and
feeding it into library code that already does the computation.
We delegate; we don't derive.

### No Backward Compatibility

No backward compatibility, "shims", thin wrappers, or convenience aliases -- **except**
those specifically required by a spec.

This is not long-term, user-facing code.
It is code to express, consistently, correctly, uniformly, and canonically, mathematical
experiments and results.
There are no "past" users to support.

Redesigns are always "breaking" if necessary, and must always involve updating all call
sites to use new names, norms, canonical methods or constructors, etc.

### No Needless Indirection

No needless indirection -- e.g., functions that are <5 lines that don't do any nontrivial
logic.

**Bad example:**
```python
def identity_lattice(n):
    return matrix(ZZ, identity_matrix(ZZ, n))
```

Why? `identity_matrix(ZZ, n)` already exists and is perfectly clear.
The code isn't doing anything nontrivial:

- Not using exotic rings
- Not constructing entries $i, j$ for more complex matrices
- Not doing any validation (e.g., checking agreement of size of matrix with ranks of
  lattices for homs)
- Not requested or required by the spec as a specific alias
- Not serving as a "canonical" site to uniformize constructions to make sure they don't
  forget steps or validation

If a function doesn't do any of the above, just call the existing library function
directly.

### No Stub Implementations in Specs

When writing specs, never leave functions with broken or undefined implementations.
No raising `NotImplementedError`, no silently skipping, no doing some alternative
computation when the intention is for subclasses to implement real logic.

Force `ABC` and `abstractmethod` for genuinely deferred logic, so that the class can
never even be instantiated until the correct logic is written.

### Single Source of Truth (SSOT)

There should be one place any nontrivial construction happens, typically in a
`classmethod` constructor, and **all** other instances of constructing an object must
defer and delegate to it.

Similarly, use **semantic membership checks** whenever possible.

**Bad example:** Checking a matrix $M$ defines an isometry by checking $M^T G_1 M =
G_2$.

**Why:** A matrix is not an isometry -- it is a **representation** of one.
The check $M^T G_1 M = G_2$ repeats the definition in every call site.

**Good example:** Construct `Hom(L_1, L_2)` and use the matrix to construct a real
homomorphism $f$ from $M$. Then `f in Hom(L_1, L_2)` should be the canonical place such
an equation is checked.

This prevents convention drift (left vs.
right action) and freezes decisions to one place.

### No Internal Renaming

No internal renaming of objects that are sufficiently semantically expressed by their
constructions.

**Bad example:**
```python
A1_LATTICE = ...
```

**Good example:** Use `Lattice.A(1)` wherever needed.

Why? Unless the computation is expensive or the explicit construction is convoluted,
there is no reason to have two naming conventions for a single object.

### No Optional Arguments

No `**kwargs`, optional arguments, or polymorphic overloading.
Every method has a **precise** set of arguments it takes.

If you need to allow "polymorphic" inputs, enumerate the **exact** set of input shapes
you need, and set up `classmethod`s that handle and route each individually.

The code should not attempt to be "user-friendly" -- there is no reason for such
shortcuts. No "hidden" state; everything should be explicit.

### No `__all__` Exports

No `__all__` exports.
Use Python's native public/private guidelines with underscores to communicate what is
meant to be imported.

Other code may want to import private functions, and that should be allowed -- linters
will explicitly catch such things.

### No Optional Types

No usage of optional types, `None`, checking `is not None`, etc.
-- unless specifically user-approved.

In most cases, it is better to split the "has X" and "does not have X" cases explicitly
into separate methods or classmethods, rather than adding branching logic for missing
values.

### Introspection Red Flags

`isinstance`, `hasattr`, `getattr`, `type()`, `issubclass`, and `callable()` are
diagnostic signals that code is guessing about input shapes at runtime rather than
asserting them through the type system. They are not banned, but each occurrence
must survive a reasoning chain that asks: Is this a legitimate boundary? Is the
check minimal and localized? What structured alternative would eliminate it?

See the `anti-slop` skill, `references/code-patterns.md#introspection-red-flags`,
for the full catalog of signals, the reasoning chain, and the acceptance criteria
table.

### No `del` in Abstract or Overload Bodies

Using `del param` (or `del (param1, param2, ...)`) inside `@abstractmethod` or
`@overload` bodies to suppress unused-parameter lint is **banned**.

```python
# BAD — silences lint by injecting a real statement into a body that should be `...`
@abstractmethod
def foo(self, x: int, y: str) -> bool:
    del x, y   # or: del (x, y,)
    ...

# GOOD
@abstractmethod
def foo(self, x: int, y: str) -> bool:
    ...
```

**Why it is banned:**

- `@abstractmethod` and `@overload` bodies are **never executed**. Suppressing
  "unused parameter" warnings in them is meaningless noise.
- `del X` is a real statement. Adding it to an otherwise-`...` body turns the
  body non-trivial: mypy now sees a function with statements but no `return`,
  and correctly fires `[return]` — a false positive caused entirely by the
  suppression idiom.
- The correct fix for "unused parameter" in a *concrete* method body is to
  prefix the parameter with `_` in the signature, or restructure the method.
  In abstract/overload stubs the parameter name is documentation; the warning
  is irrelevant.
- If the lint rule that fires on unused parameters is not in the project's
  selected rule set (e.g. `ARG` is not selected in ruff), then `del` is doubly
  pointless: it suppresses a warning that was never enabled.

The rule generalises: **never introduce code whose sole purpose is to silence a
QC tool**. Fix the code or fix the QC config (with documented justification).
Inline silencing — whether `del`, `# noqa`, `# type: ignore`, or equivalent —
is always banned.

### No `globals()` Manipulation or `importlib` Imports

`globals().update({...})`, `global X` inside functions, and
`importlib.import_module()` are banned. Each is a code smell signaling that a
module is breaking rank with the established category export pattern.

**Why `globals()` manipulation is banned:**

```python
# BAD — name injected at runtime; invisible to mypy and all static analysis
def _load_exports():
    global MetricSpacesCategory
    globals().update({"MetricSpacesObject": ..., "MetricSpacesMorphism": ...})
_load_exports()
```

Any name injected via `globals()` does not exist in the module's static scope.
mypy cannot see it, IDEs cannot autocomplete it, and `grep` will not find its
definition. The module's public surface is then inconsistent between static
analysis time and runtime — a hidden contract.

**Why `importlib.import_module()` is banned:**

```python
# BAD — deferred loading to mask a circular import
_cat_autsets = import_module("category_specs.cat.autsets")
type CatAutCategory = _cat_autsets.CatAutCategory
```

`import_module()` used to load a sibling submodule is a symptom of an unresolved
circular import. The correct fix is structural:

- Move the shared definition to a base module that neither side imports
  (e.g., `base_category_types.py`)
- Or guard the import under `TYPE_CHECKING` if only type annotations need it

Dynamic loading does not fix the dependency cycle — it hides it while
simultaneously defeating static analysis.

**The canonical export pattern** for `category_specs` modules is:

```python
# At module scope — visible to mypy, grep, and importers
type MetricSpacesObject = MetricSpacesCategory.ParentMethods
type MetricSpacesHomCategory = MetricSpaceHomCategory
```

All public names must be bound at module scope by ordinary `import` statements
or `type` aliases. If a name cannot be bound this way, the import structure needs
to be fixed, not bypassed.

### Semantic Checks Over Manual Implementation

Use semantic checks and Sage's coercion when possible to match mathematical semantics.

**Bad example:**
```python
def is_integral(self):
    return matrix_has_entries_in(ZZ, self.gram_matrix())
```

**Good example:**
```python
self.gram_matrix() in GL(n, ZZ)
```

Why? The former reads like software; the latter reads like mathematics.
And we trust existing implementations to already own efficient membership checks, which
may be **better** than ours.
In this case, probably `M.base_ring() == ZZ` suffices, because the construction
*already* validated integrality.

**Another bad example:**
```python
all(vi in ZZ for vi in v)
```

This is "programmer" language, not mathematical language.

**Good example:**
```python
v in ZZ^(len(v))
```

The overarching guidance: **say what sets objects are in, not what properties an object
must satisfy**, whenever possible.
We trust the backend to implement efficient membership checks.

### Backend Encapsulation

This codebase is **parallel** to existing Sage module and lattice machinery (of which
there are 3+ separate branches).
As such, it should hook into low-level Sage category machinery: properly extending
morphisms, hom sets, using low-level module types (e.g. FGP modules), and taking care of
the boilerplate required for that in separate "Sage backend" classes which separate it
from the more nontrivial gluing and mathematical code.

However, since we don't want to reinvent things immediately, this means **wrapping**
Sage objects, and exposing a new "API" that internally delegates to Sage objects.
At no point should the "existing Sage internals" leak through -- there is no reason for
callers to be able to extract a Sage `IntegralLattice` from our code, e.g.

If we are missing crucial methods, those should be floated to the user and recorded in
permanent spec files, as opposed to allowing bypasses that reach into our internals in
ad-hoc ways.

### Code Structure

**No `pass`:** Use `...` (Ellipsis), and only in the case of explicitly labeled
`abstractmethod` definitions.

**Explicit overrides:** All overrides must be explicitly labeled (e.g., use `@override`
decorator when available).

### Validation and Equality

**Pydantic validation:** Use Pydantic, and add an explicit validation method -- not
validation per variable, just an overall validation which runs after construction, to
ensure that all constructors create a mathematically valid object.

Assert on mathematical properties that carve out your object.

**Equality semantics (`__eq__`):**

- **Lattices:** "Equal" means "isometric via the identity matrix", not programmatic
  equality.

- **Hom spaces:** "Equal" means equal domains/codomains and equal matrix
  representations.

- **Varieties:** "Equal" means equality of coordinate rings.

**Isomorphisms:** Should generally have options to return witnesses that can be checked,
with logging warnings when computations are expensive.

### Standard Methods

All objects must implement:
- `__hash__` -- for use in sets, dicts, caching
- `__repr__` -- standard Python representation
- LaTeX printing -- wire into Sage's LaTeX printing functionality (see Sage's preparser
  and `_latex_` methods)

### Typing

Everything must have a type, either defined in Sage, or defined in our branch.
- No untyped arguments
- No implicit return types
- No `Any` or `object` or similarly broad types -- unless specifically requested by the
  user

Use explicit union types to express allowed inputs.

Typing work must improve the proof surface of the code. A type annotation says what
mathematical object, morphism, constructor, or backend value the expression denotes.
It is not acceptable to add a cast, wrapper, helper protocol, or narrower annotation
only because a QC tool reports `Any` or cannot follow dynamic library behavior.

Before any typing fix, ask whether the static checker is exposing a real defect that
downstream implementers should see. Real defects include missing obligations, wrong
owners, broad or unsourced public signatures, untyped boundary data that should have a
named mathematical type, and mismatched constructor inputs. If the code already states
the intended mathematical operation clearly and the checker is missing knowledge of
Sage, category method containers, dynamic inheritance, classcall behavior, or other
trusted backend semantics, the repair is not to silence the checker locally. File or
advance the plugin, stub, global QC, or static-surface task that teaches the checker
the correct mathematics.

Local casts are last-resort boundary documentation. They are appropriate only at a
specific untyped external API boundary or a narrow mathematical refinement whose
hypotheses are already asserted in the code. They are not appropriate around correct
category selectors, constructor collectors, or backend calls merely to make a mypy
count decrease.

### Error Handling (String Matching)

No raising errors.
For string matching, **assert** that the string is acceptable -- do not
"attempt match and then fail if not".
The assertion documents the precondition.

### Iteration and Cardinality

We expect enumeration on both finite and countably infinite objects:

- `__iter__` should be defined
- **Lazy generators** should be used for infinite objects -- don't materialize the full
  set

**Iteration patterns:**
- Canonically define an efficient "diagonal argument" iteration of $\mathbb{Z}^n$ in
  backend code
- Use that to bootstrap iteration of lattices

**ConditionSets:** Use when necessary to check membership in infinite sets without
computing them (e.g., isotropic vectors in a lattice).

**Cardinalities:** All objects must report meaningful cardinalities.

### Avoid Non-Obviously-Correct Code

Avoid not-obviously-correct code.
For example:

**Bad:**
```python
def is_p_elementary(self, p):
    return all(invariant == p for invariant in self.invariants())
```

Why? *Probably* this is correct, but not **obviously** correct.

**Good:**
```python
def is_p_elementary(self, p):
    return self._underlying_group.is_p_elementary(p)
```

What *is* obviously correct?
Storing a Sage object and asking it directly.
We should not be reinventing any nontrivial mathematics.

### Class Hierarchy

**Any class that doesn't extend SOME class is suspect.**

- Hook into Sage primitives when possible (e.g., elements, morphisms, homsets, modules)
- Otherwise, extend `ABC` or `BaseModel` (Pydantic)

### Pydantic Constructors

We should see explicit constructors on almost every class, along with `classmethod`
constructors that automatically handle conversion/coercion/etc from specific known data.

**Pydantic post-validation is mandatory:**
- Should assert nontrivial mathematical properties
- Can add debug logging here

### Manual Calculations Require Citations

Any "manual" calculations that are NOT deferring to existing code for the actual
computation must cite a repo-local definition or source in the literature.

**Bad example:** `is_primitive()` defined as `gcd(coordinates) == 1`.

This is not the definition.
The actual mathematical definition is:
> $v$ is primitive iff $v = kw$ for some $k \geq 2$ and some $w$ in $L$.

**Correct approach:** `f = v.sublattice_inclusion()`, `f.is_primitive()`, etc.

Why? This uses existing code that implements the definition correctly -- we are not
re-deriving mathematics ourselves.
The method is not the definition; the method is a tool that implements the definition.
Re-implementing manually adds surface area for potential errors.

When in doubt, delegate to existing code that already owns the mathematical correctness.

### Backend Isolation

Algorithms that only depend on e.g. an underlying group or module should be in backend
code, independently testable on explicitly constructed groups or modules.
Lattice-theoretic code should extract the underlying object and call the appropriate
backend algorithm.

### Assertions Mirror Literature

Assertions should mirror mathematical literature, not semantically indirect it.

**Example:** Nikulin's invariants are defined for even indefinite 2-elementary lattices.
Checking applicability should simply check:
```python
assert L.is_even() and L.is_indefinite() and L.is_p_elementary(2)
```

**Bad example:**
```python
p, q = self.signature_pair()
outside_domain = not is_even() or not p or not q or not...
```
- Checking truthiness of signature instead of mathematical property
- Indirects indefinite check into raw signature manipulation
- Indirects basic logical conditional into `outside_domain` variable

### TDD-First: Tests Must Have Sources

If you are implementing any nontrivial mathematics, you must have a series of explicit
mathematical TDD-first tests asserting known, sourced, citable assertions of correct
calculations.

- **Any test without a source cannot be trusted to be correct.**
- **Any failing test must have the correctness of its assertion checked against its
  source.**
- **Tests should carve out the precise correctness, mathematically.**

**Prefer** using Hypothesis or other parameter-exploration and checking frameworks.

### Identity vs Equality

**Do not use `is`** in mathematical code. Two totally separate constructions may
produce isometric lattices that are isometric via the identity.

Overload `==` for mathematical equality, with early-outs when objects are literally
the same in Python.

### No Dataclasses

No dataclasses, ever. We use Pydantic.

### No Re-Export Files

No files that exist only to re-export.

### Abstract Base Classes

There is no real reason to leave anything as a pure `ABC` in this codebase,
**unless** it is purely spec-driven work that doesn't fit into the hierarchy and is being
used to uniformize the spec.

**Bad use of ABC:** Making `BilinearFormElement` an `ABC` with unimplemented methods.
Why? One needs actual such elements.

**Good use of ABC:** Centralizing a spec for all elements of lattice, bilinear modules,
quadratic modules, torsion forms, etc., moving all of the boilerplate non-mathematical
code into "hidden" backend.

**Rule:** It is a bad sign if there is any code in our base that is purely abstract
and doesn't integrate into real Sage internals in some nontrivial way. If there IS a category
of such things, you need properly instantiated and working abstract Bilinear modules
(e.g. the cokernel of a morphism).
