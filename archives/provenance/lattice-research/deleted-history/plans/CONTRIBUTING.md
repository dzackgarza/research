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

1. **Encodes mathematical expectations:** The `assert len(I.gens()) == 1` states the
   expectation that we are in a principal ideal domain and the ideal is principal — not
   just that the computation succeeded, but that the mathematical preconditions hold.

2. **Provably correct by reading it:** The code explicitly states the problem ("find the
   generator of an ideal") and the solution ("compute and return the generator"). There
   is no ambiguity about what is being computed or why.

3. **Generalizable to other rings:** The pattern
   `assert len(I.gens()) == 1; return I.gens()[0]` works for any ring where ideals are
   principal, not just $\mathbb{Z}$. The assertion is the mathematical contract.

4. **Self-documenting correctness:** No separate citation is needed to verify the code
   is correct — the assertion itself is the mathematical guarantee.

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
lattices." It does not say "the algorithm fails on indefinite lattices" — it says "this
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

We do not want to "own" the mathematical correctness of anything — we use existing
implementations to minimize the surface area we need to check.
Any code attempting to do nontrivial mathematics *internally* is likely wrong, and
should be a simple wrapper/delegator to existing code elsewhere.

**Bad example:** Computing a generator of an ideal in $\mathbb{Z}$ by manually computing
a gcd.
This implicitly applies a theorem about ideals in PIDs which are Euclidean domains
— extra mathematical surface area that must be checked internally.

**Good example:** `I.gens()` — our surface area is merely constructing the ideal and
feeding it into library code that already does the computation.
We delegate; we don't derive.

### No Backward Compatibility

No backward compatibility, "shims", thin wrappers, or convenience aliases — **except**
those specifically required by a spec.

This is not long-term, user-facing code.
It is code to express, consistently, correctly, uniformly, and canonically, mathematical
experiments and results.
There are no "past" users to support.

Redesigns are always "breaking" if necessary, and must always involve updating all call
sites to use new names, norms, canonical methods or constructors, etc.

### No Needless Indirection

No needless indirection — e.g., functions that are <5 lines that don't do any nontrivial
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

**Why:** A matrix is not an isometry — it is a **representation** of one.
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

The code should not attempt to be "user-friendly" — there is no reason for such
shortcuts. No "hidden" state; everything should be explicit.

### No `__all__` Exports

No `__all__` exports.
Use Python's native public/private guidelines with underscores to communicate what is
meant to be imported.

Other code may want to import private functions, and that should be allowed — linters
will explicitly catch such things.
One should **not** actually import private functions unless the user specifically
requests such shared interop, but in this case, the better long-term solution is moving
to a shared helper/utility module anyway.

### No Optional Types

No usage of optional types, `None`, checking `is not None`, etc.
— unless specifically user-approved.

In most cases, it is better to split the "has X" and "does not have X" cases explicitly
into separate methods or classmethods, rather than adding branching logic for missing
values.

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
At no point should the "existing Sage internals" leak through — there is no reason for
callers to be able to extract a Sage `IntegralLattice` from our code, e.g.

If we are missing crucial methods, those should be floated to the user and recorded in
permanent spec files, as opposed to allowing bypasses that reach into our internals in
ad-hoc ways.

### Mathematical Syntax Sugar

Nouns should have basic syntax sugar expected in Sage, which are usually category-level
constructions:

| Operator | Meaning |
| --- | --- |
| `A + B` | Direct sum (do **not** follow the Sage-internal "span" interpretation) |
| `A^n` | Direct sum $A + A + \dots + A$ ($n$ times) |
| `n * A` | Usually `A.twist(n)` |
| `f + g` | Usually a map $A_1 \oplus A_2 \to B_1 \oplus B_2$ |
| `f * g` | Usually composition (when defined) |
| `n * f` | Usually `Hom(L_1, L_2).element_from_matrix(n * f.to_matrix())` |
| `x in L` | Validates that `x.parent() == L` — note: a lattice does not "contain" a vector; it contains linear combinations of generators, which have **vector representations** |
| `f in O(L)` | Checks isometry |
| `f in Hom(L_1, L_2)` | Checks isometry |

We do **not** automatically coerce when checking membership.

**Quotient notation:** `A / B` := `coker(f: A -> B)` for some specific map `f`, where
sometimes there is a "natural" map returned by something like `Hom(A, B).natural_map()`
or whatever Sage uses to check that e.g. $\mathbb{Z}$ is a subring of $\mathbb{Q}$.

**Generator assignment:** `L.<e1, e2> = {some lattice construction}` is typical sugar
for extracting and assigning generators, which requires special methods to exist on `L`
(see the Sage preparser code).

#### The `__call__` Method for Polymorphic Coercion

The `__call__` method usually handles polymorphic coercion:

- `L.<e1, e2> = Lattice.U()` => `L([1, -2])` produces "$1 \cdot e_1 - 2 \cdot e_2$",
  similarly for tuples, vectors, etc.

- `A_L = L.discriminant_group()`, `A_L(e1) == A_L(0)` might also hold: calling might
  apply natural projections/inclusions, e.g. of lattice elements — here we interpret `0`
  as the identity in the group.

- `H = Hom(L_1, L_2)`, `M = matrix(...)`, `f = H(M)` would convert the matrix to a
  homomorphism.

These should ultimately be defined on `classmethod`s, e.g. `H.element_from_matrix(...)`,
and the `__call__` method should be a thin localized "router".

### Code Structure

**No `pass`:** Use `...` (Ellipsis), and only in the case of explicitly labeled
`abstractmethod` definitions.

**Explicit overrides:** All overrides must be explicitly labeled (e.g., use `@override`
decorator when available).

### Validation and Equality

**Pydantic validation:** Use Pydantic, and add an explicit validation method — not
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
- `__hash__` — for use in sets, dicts, caching
- `__repr__` — standard Python representation
- LaTeX printing — wire into Sage's LaTeX printing functionality (see Sage's preparser
  and `_latex_` methods)

### Typing

Everything must have a type, either defined in Sage, or defined in our branch.
- No untyped arguments
- No implicit return types
- No `Any` or `object` or similarly broad types — unless specifically requested by the
  user

Use explicit union types to express allowed inputs.

### Error Handling (String Matching)

No raising errors.
For string matching, **assert** that the string is acceptable — do not
"attempt match and then fail if not".
The assertion documents the precondition.

### Iteration and Cardinality

We expect enumeration on both finite and countably infinite objects:

- `__iter__` should be defined
- **Lazy generators** should be used for infinite objects — don't materialize the full
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

### Warning: Class Hierarchy

**Any class that doesn't extend SOME class is suspect.**

- Hook into Sage primitives when possible (e.g., elements, morphisms, homsets, modules)
- Otherwise, extend `ABC` or `BaseModel` (Pydantic)

### Subobjects as Morphisms

"Subobjects" are really morphisms, not objects themselves.

- A subobject needs some kind of mix-in that endows objects with an attached morphism
  and is where notions like "ambient" make sense
- Or one should have explicit `SubLattice` types which extend `Lattice` and add all of
  these notions

**Bad example:** Making "subobject" semantics optional notions on the object itself.
This violates the optionality rule, pollutes the namespace, and forces optional checks
everywhere.

**Better:** Regard a subobject as a morphism, or have explicit subobject classes.

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

Why? This uses existing code that implements the definition correctly — we are not
re-deriving mathematics ourselves.
The method is not the definition; the method is a tool that implements the definition.
Re-implementing manually adds surface area for potential errors.

When in doubt, delegate to existing code that already owns the mathematical correctness.

### No Ambient Module Assumption

Sage assumes all lattices inject into some "ambient" module.
**We do not assume this.**

An arbitrary indefinite lattice $L$ does admit a natural map $L \to L
\otimes_{\mathbb{Z}} \mathbb{Q}$ given by $v \mapsto v \otimes 1$, and the bilinear form
is $$\tilde{b}(v \otimes q_1, w \otimes q_2) := b(v, w) \otimes_{\mathbb{Z}} (q_1 \cdot
q_2)$$ which technically takes values in $\mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{Q}$.

This is just the general formula for a tensor product in the category of pairs $(L, b)$.

**This is very different from Sage's assumption** that lattices have a "basis" of
vectors in $\mathbb{Z}^n$ or $\mathbb{Q}^n$. An arbitrary indefinite lattice is defined
abstractly, not as a collection of vectors and their inner products (and indeed it can't
be — the inner product is always definite...).

**Rule:** This "everything is in an ambient space" artifact of existing Sage code should
not be used or even acknowledged in our code whatsoever.

### Do Not Leak Sage API

The Sage API should not be leaked through, because it is broken, fragmented, and
theoretically wrong in many places.

**Example:** An `inner_product_matrix` on a lattice makes no sense mathematically — an
indefinite bilinear form never defines an inner product.
Only expose the API that is specifically requested:

1. In the specs and tests
2. By other internal code

**Interop with existing Sage code is not a requirement nor desired.** The entire point
is to replace and unify the existing lattice code and fix the historical cruft in all of
it. (Note: Sage's lattice code was historically only for definite and cryptographic
lattice theory, which is not what we want at all.)

### Discriminant Groups and Duals

One needs to carefully handle the maps:
- $\iota_L: L \to L^* := \operatorname{Hom}_{\mathbb{Z}}(L, \mathbb{Z})$
- $\iota_L^\sharp: L \to \{v \in L_{\mathbb{Q}} \mid \beta(v, L) \subseteq \mathbb{Z}\}$

And when the latter two are identified.
A dual lattice element is literally a morphism $f_v: L \to \mathbb{Z}$, and $\iota_L(v)
:= \beta(v, \cdot)$.

**One should be able to assert:**
- `L.twist(n).dual().is_isometric_to(L.dual().twist(1/n))`
- `E8.dual().is_isometric_to(E8)`
- Each $e_i^*$ (dual basis element) satisfies $e_i^*(e_j) = \delta_{ij}$ where $e_j$ are
  `L.gens()` and $e_i^*$ are `L.dual().gens()`
- If $L$ is unimodular then `L.twist(n).dual().is_isometric(L.twist(1/n))`

**It is not as simple as** constructing an abstract `RationalLattice` from
`L.gram_matrix().inverse()`.

If a lattice is known to be constructed as a dual, it should have extra "functional"
semantics on elements, the explicit map $\iota_L$, etc.

**We regard $\iota_L$ as a morphism of rational lattices**, so that $A_L := L^* /
\iota(L)$ is actually computed as the cokernel of $\iota_L$.

**This should NOT be abstractly constructed from invariants or SNF** — morphisms like
$\iota_L$ should be constructible from matrices and have well-defined cokernel bilinear
modules which are automatically promoted to Lattices or torsion bilinear modules when
appropriate (using FGP module machinery).

In other words, you need a **working vocabulary** of bilinear modules, their morphisms,
cokernels, submodules, etc.
You should **not short-circuit** this when constructing discriminant groups to use the
shortcut theorem that $L$ is finite-index in $L^*$ — you should literally and actually
be computing modules, induced forms, kernels/cokernels, etc.

**Example:** Lifting from quotients is more naturally expressed by keeping track of
projections, e.g. `p_L: L^* -> A_L` and semantically asking for `p_L.lift(v)`.

Most of this exists in existing Sage code and can be leveraged/wrapped.

### Mathematical Correctness in Implementations

Computing invariants incorrectly is a common failure mode.
Example: computing Nikulin's $a$-invariant by indirect checks like "looking at how many
times 2 divides the invariants."

**Correct approach:**
```python
A_L = L.discriminant_group()
assert L.is_p_elementary(2)  # already defined in upstream
# This amounts to: all(inv_i == 2 for inv_i in A_L.invariants())
# Then return a := len(A_L.invariants()), since this means A_L ≅ (C_2)^a
```

**Bad approach:**
```python
sum(2.divides(inv_i) for inv_i in A_L.invariants())
```

This is:
1. Not obviously right (no source, no citation)
2. Ad-hoc computation instead of using existing algorithms
3. **Completely wrong upon inspection:** `AbelianGroup([4])` would return something
   nontrivial, despite the fact that $G \neq C_2^a$ for any $a$

### TDD-First: Tests Must Have Sources

If you are implementing any nontrivial mathematics, you must have a series of explicit
mathematical TDD-first tests asserting known, sourced, citable assertions of correct
calculations.

- **Any test without a source cannot be trusted to be correct.**
- **Any failing test must have the correctness of its assertion checked against its
  source.**
- **Tests should carve out the precise correctness, mathematically.**

**Example:** `nikulin_a`'s algorithm:
- Returns 2 for $C_2^2$
- Returns 1 for $C_2$
- Raises an assertion for $C_4$
- Returns $a$ for $C_2^a$ for a wide range of known $a$ values
- Raises assertions for $C_n^a$ for various $n$ and $a$

**Prefer** using Hypothesis or other parameter-exploration and checking frameworks.

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
p, q = self.signature_pair()  # Bad: signature_pair is Sage convention; use signature()
outside_domain = not is_even() or not p or not q or not...
```
- Checking truthiness of signature instead of mathematical property
- Indirects indefinite check into raw signature manipulation
- Indirects basic logical conditional into `outside_domain` variable

### No Raw Matrices for Semantic Objects

**Convention:** Subspaces are defined by lists of vectors, not e.g. rows of a matrix.

Typical numpy-like manipulations should not be used, e.g. collecting vectors into a
matrix at the semantic level of the API.

**Why?** What semantic object does that matrix represent?
Usually nothing — it is not a well-defined morphism.
(And if it were, it should be constructed as a morphism, not passed around as raw
numbers in matrices.)

### Frontend: Morphisms, Not Matrices

We do not semantically work with matrices in the frontend layer.
We work with:
- Morphisms
- Maybe Gram matrices
- Collections of vectors
- Sublattices (with embedding morphisms)

**Bad example:**
```python
invariant_sublattice(self, involution_matrix)
```
Why? This encourages public users to bypass the correct hom layer entirely.

**Correct approach:** Construct a valid hom from a desired matrix, and only in backend
algorithms do you deconstruct and/or extract its matrix.

**Why?** Morphisms of free modules are defined symbolically by sending generators to
linear combinations of generators.
These are more properly defined in terms of dicts, or list of images, with explicit
symbolic generator manipulation, from which the matrices are automatically constructed
and extractible.

You cannot and will not construct a $20 \times 20$ matrix for a large lattice, and you
certainly can't include such a thing in a paper.
The semantic layer is meant to easily translate to understandable, minimal constructions
that can easily be written up.

### Stabilizers and Centralizers

Stabilizers, centralizers, etc.
should be defined on Orthogonal group objects:

```python
G = L.orthogonal_group()
f = ...
H = G.centralizer(f)
Hp = G.stabilizer(v)
Hp2 = G.stabilizer_of_flag([v1, v2, ...])
```

**Not** as indirected spaghetti methods like `L.stabilizer_of_flag([v1, v2, ...])`.

Elements can have methods though:
- `v.stabilizer()`
- `v.stabilizer(in_group=Gamma)`
- `f.centralizer()`
- `f.centralizer(in_group=Gamma)`

**No restricted functions** like `centralizer_of_involution`. Instead, have a generic
centralizer function — if you only support involutions right now, assert:
```python
assert f.is_involution(), "Non-involutions are not yet supported"
```

### Subobjects and Division

**Subobject mixin:** Keep track of inclusion morphisms when constructing subobjects.

- Every element $v$ in $L$ has an inclusion morphism $\iota_v: v.\text{span()} \to L$
- Every submodule is defined as a span $M := L.\text{span}([v_1, \dots, v_n])$ and a morphism $\iota_M: M \to L$

**Division (`/`):** `B / A` always means `B / im(f)` for some $f: A \to B`. This requires
the subobject mixin which keeps track of inclusion morphisms.

**General cokernel machinery:** Division is completely general and always yields some
bilinear module. Special case: $\iota_L: L \to L^*$ yields the discriminant group $A_L$,
which is a case of automatic promotion.

**Implementation:** You need a `classmethod` on bilinear modules which accepts a morphism
of bilinear modules:
1. Extract its matrix
2. Construct the FGP module
3. Descend the bilinear form
4. Automatically promote to Lattice, RationalLattice, DiscriminantGroup, Torsion forms,
   etc.

**Bad example:** A `truediv` function which asserts "this is a dual lattice" and "the
other lattice is the original lattice" and only returns the discriminant group. This
bypasses implementing the correct general cokernel and bilinear module machinery.

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

### No Dataclasses

No dataclasses, ever. We use Pydantic.

### Set Operations: `&` and `|`

- Use `&` and `|` to mean **intersect** and **union**.
- For modules and lattices, always mean the **span** of such.
- For groups or subsets of lattices (e.g., centralizers, isotropic vectors), use **ConditionSets**,
  and simply use `&` or `|` on those.

### Morphism Construction

Preferred construction is a **dict of generators and their images**.

Allowed classmethods:
- Take a domain and a sequence of images
- Take domain/codomain/matrix when applicable

### Hom Spaces

`H := A.Hom(B)` is a **space of morphisms** $A \to B$, not a specific morphism.

Create morphisms via:
- `H.element_from_dict(...)` (preferred)
- `H.element_from_matrix(...)`

**Do not** coerce matrices to morphisms. Force users to declare domain/codomain and
explicitly construct using element methods.

### Identity vs Equality

**Do not use `is`** in mathematical code. Two totally separate constructions may
produce isometric lattices that are isometric via the identity.

Overload `==` for mathematical equality, with early-outs when objects are literally
the same in Python.

### ConditionSets and Membership

Each object we use should truly have some kind of underlying Sage set. Wire a
**ConditionSet** that can be used to check abstract membership "lazily" based on
centralized predicates.

### Hom Space Enumeration

Homs should have a reasonable method of infinite enumeration. Since every
$f \in \operatorname{Hom}(L_1, L_2)$ is a $\mathbb{Z}$-matrix, we can bootstrap a
centralized enumeration algorithm for $\mathbb{Z}^m$ to provide an iterable generator
for hom spaces.

### No Re-Export Files

No files that exist only to re-export.

### Banned / Out-of-Scope Constructs

- LLL
- Short vectors/closest vectors
- min/max vectors
- signature_pair [the pair (p,q) is just called the signature]
- signature defines as p-q [this is -the index]
- rescale, or "scale" used as a verb instead of a noun [scale is an invariant, not an operation]
- IntegralLattice, IntegralLatticeGluing, etc [LatticeGlueData is its own class, and from_glue_data is a verb for construction, not a noun to be exposed]
- IntegralLatticeDirectSum [need a bilinear module native solution to handling decomposable lattices
- bases, echelon forms, ambient modules [our lattices are not naturally subsets of any other "ambient" object, they exist mathematically a priori in their own categories]
- Regarding vectors as elements and matrices as morphisms [ill-defined: if v = [0, 1] and you want to regard it as an "element" of a lattice, this implies it must be an element of EVERY rank 2 lattice, e.g. U(n) for EVERY n -- wildly ill-defined. vectors must be EXTRACTED from semantically constructed lattice elements, which are symbolic. Similarly, if 2x2 matrix is regarded as an element of Hom(U, U), it must be in Hom(U(n), U(n)) for every n -- instead, construct a MORPHISM (possibly FROM a matrix) and extract coordinate representations when needed]
- basis() [modules have generators, not bases -- "basis" means "generators of a K-module" where K is a field]
- ambient_vector_space, vector_space, etc [should happen behind the scenes, L.base_change(QQ) HAS an associated vector space, but is really a bilinear QQ-module, which can hook into sage vector spaces if needed, but module machinery is more natural]
- basis_matrix  [doesn't make sense, the "basis matrix" is always the identity for us]
- dimension [free modules have ranks, not dimensions]
- inner_product [we do not special case positive definite nondegenerate forms in any way. an arbitrary bilinear form is NOT an inner product, there is no "inner product matrix",etc]
- sparse/dense vectors, matrices, etc [numerical optimizations that are irrelevant to the semantic vocabulary needed]
- pseudohoms [we will implement a real derivation module Der_R(L_1, L_2) if needed]
- complement [the set-theoretic complement is irrelevant in module theory, only use perp() == orthogonal_complement()]
- intersections, subspaces, sage's A+B notation for the span of two submodules in a larger ambient module [use explicit L.span([..]) semantics, reserve + for direct sum, use & and | for low-level intersections and unions when needed for specific internal module computations]
- top-level `span` function [not well-defined: can only take the span of elements or sublattices of a specific lattice, in which case L.span([..]) must make explicit where the span is taken, which implicitly handles the ring coefficients allowed]
-
