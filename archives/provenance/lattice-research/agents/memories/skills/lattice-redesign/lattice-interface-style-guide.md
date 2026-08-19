# Lattice Interface Style Guide

Lattice-specific code conventions for the `src/lattices/` hierarchy.
For general code style rules, see `CONTRIBUTING.md` at repo root.
For the implementation plans, see `PHASE_0_SAGE_PATCHES.md` and
`PHASE_1_BILINEAR_MODULES.md` in this directory.

This guide consolidates lattice-specific conventions from the original
CONTRIBUTING.md and the normalized design directives from the user
corrections in `lattice_redesign_corrections_spec.md`.


## Design Goal: A Mathematical DSL

This project is **not** a typical software library and should not be
designed like one.

The goal is a **domain-specific language for lattice theory in algebraic
geometry** -- specifically the kind of lattice theory that appears in the
work of Nikulin, Looijenga, Miranda–Morrison, Gritsenko–Nikulin, and
similar authors. The primary users are mathematicians running computations
in support of a paper: checking discriminant form invariants, verifying
genus conditions, constructing orthogonal group elements, tracing orbits
of isotropic vectors.

**The standard for usability is: can the code be read aloud as the
corresponding paragraph in a paper?** If a computation requires five
lines of plumbing before it gets to the mathematics, the API has failed.

### The Sage module ecosystem we are replacing

Sage has multiple largely incompatible hierarchies for finitely generated
modules and lattices, none suited for general indefinite lattice theory:

| Module | Role | Limitation |
|--------|------|------------|
| `sage.modules.free_module.FreeModule` | Free R-modules, linear algebra | No bilinear form |
| `sage.modules.fg_pid_module.FGP_Module` | Finitely generated modules over PIDs, quotients | No form; cokernel machinery used internally |
| `sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule` | Tensor calculus, multilinear algebra over arbitrary rings; no choice of basis | No inner product machinery |
| `sage.combinat.free_module.CombinatorialFreeModule` | Free modules indexed by combinatorial sets (roots, monomials) | No bilinear form; used for Weyl algebras, symmetric functions, etc. |
| `sage.quadratic_forms.quadratic_form.QuadraticForm` | Quadratic forms over ZZ/QQ | **Assumes positive-definite without validation.** Algorithms often silently wrong on indefinite input. |
| `sage.modules.torsion_quadratic_module.TorsionQuadraticModule` | Torsion quadratic modules, discriminant groups | Separate hierarchy, no unified parent with free modules |
| `sage.modules.lattice_homomorphism` | Lattice morphisms | Minimal, tied to ambient-space model |

**The definiteness trap.** Most Sage lattice/form code was written for
definite (positive or negative definite) forms. It was never validated
against indefinite inputs. Code that "happens to work" on indefinite forms
is not the same as code that is correct -- it is an accident, and it will
fail in subtle ways. We must re-derive everything from first principles
and not assume any Sage algorithm is correct for indefinite forms without
independent verification.

**`FiniteRankFreeModule` and `CombinatorialFreeModule`** are useful for
specific sub-computations (tensor products of root spaces, Weyl algebra
actions, symmetric function theory connected to root systems) and will be
recovered as backends for relevant computations. They are not discarded,
just not the primary API.

**We are not extending any of these hierarchies.** We are building a
unified replacement that:
- Works uniformly for free, torsion, and mixed modules
- Works for indefinite forms with correct validation
- Defines a vocabulary that matches the algebraic geometry literature
- Supports the discriminant descent `L → L* → A_L` as a first-class
  operation built on general cokernel machinery
- Carries internal Sage/Julia objects for computation, but exposes only a
  clean mathematical API

The internal Sage/Julia objects are **calculation engines**, not the
public interface. They may be swapped out, supplemented, or replaced
without changing any public-facing method.


## Category Interface vs. Concrete Implementation

The Sage category framework (`Category`, `ParentMethods`, `ElementMethods`,
Hom-category `ElementMethods`, etc.) defines the **minimum interface any
implementation of a category must provide**. Everything else belongs on the
concrete classes. Do not add repo-local `MorphismMethods`; morphism behavior
belongs on Hom-category elements.

**Rule: put something in the category only if someone implementing
`ModulesWithForms` from scratch with completely different internals would
need to implement it.** The test: could they implement it using a
polynomial ring, a Julia object, or a combinatorial free module as the
internal representation, and have every category method work unchanged?

The full category contract now lives exclusively in
**`CATEGORY_ABC_SPEC.md`**. Its source of truth is:

- `ModulesWithForms(R)` as the top-level category of pairs `(M, f)`
- bilinear and quadratic structure as refinements, not separate top-level
  contracts
- named facades such as `BilinearModules`, `QuadraticModules`,
  `FreeBilinearModules`, `TorsionBilinearModules`, `Lattices`,
  `RationalLattices`, and `DiscriminantQuadraticForms` are just meets or
  thin aliases on top of that category
- Sage-style `SubcategoryMethods`, `Homsets`, `TensorProducts`,
  `CartesianProducts`, and `DualObjects`, modeled on
  `sage.categories.modules.Modules`
- codomain and module-theoretic axioms such as `Free`, `Torsion`,
  `NonDegenerate`, `Integral`, and `Rational`

This file is style guidance only. Do not restate the ABCs here.


## Public Mathematical Model

- The working base is a module with form, presented by canonical generators
  together with its form data.
- `ModulesWithForms(R)` is a genuine new Sage category of pairs `(M, f)`,
  with `Bilinear()` and `Quadratic()` as refinements, not merely an
  informal wrapper convention around existing module parents.
- This must be defined generally over a Sage ring `R`, not hard-coded to `ZZ`
  except where a class specifically models integral lattices.
- Public lattice/module nouns are not naturally embedded in ambient spaces.
- Public nouns must not carry `inclusion_matrix`, `projection_matrix`,
  `projection_lattice`, or similar ambient-embedding state.
- Specific embeddings and subobjects must be represented separately, not
  baked into the core noun.
- `gens()` is semantically well-defined throughout the hierarchy and should
  not be omitted.
- Membership is a parent check: coordinate vectors are not automatically
  elements of a lattice.
- `L.element_from(v)` is the semantic conversion from coordinates to an
  element.


## Presented Objects and Equality

The formal object model is in `category-abc-spec.md`, especially
"Presented Object Identity". This section gives the audit posture.

Free bilinear modules and lattices are presented modules with forms. The
presentation includes the selected generators. For a free object, the data is
morally `(M, beta, B)`, where `B` is the selected generating set and the Gram
matrix is the matrix of `beta` in `B`.

Two presentations with different selected generators are distinct objects.
They may be isometric, and an isometry may be canonical in a given
construction, but they are not equal merely because they represent the same
abstract isometry class. Equality is presentation-sensitive; isometry is a
morphism-level fact with a witness in the appropriate Hom space.

Audit rules:

- reject code that silently changes a basis or generator set while preserving
  object equality;
- reject code that models a public lattice noun as an embedded ambient vector
  subspace with mutable preferred basis;
- require basis reduction, normalization, isometry search, and backend
  canonicalization to return a new object plus an explicit isometry witness
  when they change the presentation;
- require Gram matrices to be understood as presentation data, not as a
  universal identity for the abstract lattice;
- require constructor and equality tests to distinguish "same presented
  object" from "isometric object";
- require `Lattice`/`RationalLattice`/discriminant-form implementations to
  respect codomain changes `R`, `Frac(R)`, `Frac(R)/R`, and `Frac(R)/2R`
  through explicit category predicates.

## No Ambient Module Assumption

Sage assumes all lattices inject into some "ambient" module.
**We do not assume this.**

An arbitrary indefinite lattice $L$ does admit a natural map $L \to L
\otimes_{\mathbb{Z}} \mathbb{Q}$ given by $v \mapsto v \otimes 1$, and the
bilinear form extends by linearity. But this is just the general formula for
a tensor product in the category of pairs $(L, b)$.

**This is very different from Sage's assumption** that lattices have a
"basis" of vectors in $\mathbb{Z}^n$ or $\mathbb{Q}^n$. An arbitrary
indefinite lattice is defined abstractly, not as a collection of vectors and
their inner products.

**Rule:** This "everything is in an ambient space" artifact of existing Sage
code should not be used or even acknowledged in our code whatsoever.


## Do Not Leak Sage API

The Sage API should not be leaked through, because it is broken, fragmented,
and theoretically wrong in many places.

**Example:** An `inner_product_matrix` on a lattice makes no sense
mathematically -- an indefinite bilinear form never defines an inner product.
Only expose the API that is specifically requested:

- In the specs and tests
- By other internal code

Sage's existing lattice public API is not the adequacy standard. The project still
lives inside Sage's category/object universe, so interop with mathematically
appropriate Sage code remains a design constraint. The rule is that interop must pass
through typed category objects, constructors, and backend boundaries; it must not leak
Sage's fragmented definite-lattice conventions into the public lattice vocabulary.

No public object should require a Sage object as its constructor input.
Constructors build and store their internal Sage object themselves.
Separate class methods may accept Sage objects and convert them internally.

### Internal Objects Are Calculation Engines, Not the API

Our objects may carry many internal Sage (and Julia) objects simultaneously:

| Internal field | Role |
|----------------|------|
| `_fgp_module: FGP_Module` | Underlying module arithmetic, Smith form, quotients |
| `_sage_lattice: IntegralLattice` | Sage's lattice methods (definite algorithms) |
| `_quadratic_form: QuadraticForm` | Sage's quadratic form classification |
| `_torsion_module: TorsionQuadraticModule` | Torsion arithmetic |
| `_julia_lattice: object` | Julia/Hecke backend for indefinite algorithms |

**None of these are ever accessible from the public API.** They exist
because they have implementations of algorithms we need. When we call
`L.discriminant_group().is_p_elementary(2)`, we are NOT asking the user
to construct a `TorsionQuadraticModule` -- we are asking a mathematical
question about L, and the answer happens to be computed via an internal
Sage object.

**The discipline:**

```python
# Bad: leak the internal object so the user can call Sage methods on it
def sage_lattice(self):
    return self._sage_lattice  # BAD -- user now depends on Sage API

# Bad: expose the internal representation to work around a missing method
def inner_product_matrix(self):  # BAD -- wrong name, Sage convention
    return self._sage_lattice.inner_product_matrix()

# Good: expose the correct mathematical method using the internal object
def gram_matrix(self):
    return self._fgp_module.gram_matrix()  # delegates, correct name

# Good: when a method is missing, add it to OUR API with the right name,
# delegating internally
def signature(self):
    return self._sage_lattice.signature_pair()  # correct name on our API
```

**When a needed method is missing:** float it to the spec as a required
addition, add it to our public API with the correct mathematical name, and
implement it by delegating to whichever internal object already does the
computation. Never add a `get_sage_lattice()` escape hatch.

The point of this discipline: when we eventually remove the
`_sage_lattice` backend and replace it with Julia calls, nothing in the
public-facing code changes. The mathematical vocabulary is stable; the
calculation engines are interchangeable.


## Mathematical Syntax Sugar

Nouns should have basic syntax sugar expected in Sage, which are usually
category-level constructions:

| Operator | Meaning |
| --- | --- |
| `A + B` | Direct sum (do **not** follow the Sage-internal "span" interpretation) |
| `A^n` | Direct sum $A + A + \dots + A$ ($n$ times) |
| `n * A` | The submodule `{n*v : v in A}`. **NOT** `A.twist(n)`. Gram matrix is `n^2 * G_A`. For `A = R` as an R-module, `n*A` is the ideal `(n)` in R. |
| `f + g` | Usually a map $A_1 \oplus A_2 \to B_1 \oplus B_2$ |
| `f * g` | Usually composition (when defined) |
| `n * f` | Usually `Hom(L_1, L_2).from_matrix(n * f.to_matrix())` |
| `x in L` | Validates that `x.parent() == L` -- a lattice does not "contain" a vector |
| `f in O(L)` | Checks isometry |
| `f in Hom(L_1, L_2)` | Checks isometry |

We do **not** automatically coerce when checking membership.

**Quotient notation:** `A / B` := `coker(f: A -> B)` for some specific map
`f`, where sometimes there is a "natural" map returned by something like
`Hom(A, B).natural_map()`.

**Generator assignment:** `L.<e1, e2> = {some lattice construction}` is
typical sugar for extracting and assigning generators, which requires
special methods to exist on `L` (see the Sage preparser code).

### The `__call__` Method for Polymorphic Coercion

The `__call__` method usually handles polymorphic coercion:

- `L.<e1, e2> = Lattice.U()` => `L([1, -2])` produces "$1 \cdot e_1 - 2
  \cdot e_2$"
- `A_L = L.discriminant_group()`, `A_L(e1) == A_L(0)` might also hold
- `H = Hom(L_1, L_2)`, `M = matrix(...)`, `f = H(M)` would convert the
  matrix to a homomorphism

These should ultimately be defined on `classmethod`s, e.g.
`H.from_matrix(...)`, and the `__call__` method should be a thin
localized "router".

The specs demonstrate this consistently for orthogonal groups:
```python
swap = matrix(ZZ, [[0, 1], [1, 0]])
assert swap not in O_U2             # A matrix is not a hom
assert O_U2(swap) in O_U2           # __call__ dispatches to from_matrix
assert O_U2.from_matrix(swap) in O_U2  # Explicit construction
```


## Morphisms, Not Matrices

We do not semantically work with matrices in the frontend layer.
We work with:
- Morphisms
- Gram matrices (as a special case)
- Collections of vectors
- Sublattices (with embedding morphisms)

**Bad example:**
```python
invariant_sublattice(self, involution_matrix)
```
Why? This encourages public users to bypass the correct hom layer entirely.

**Correct approach:** Construct a valid hom from a desired matrix, and only
in backend algorithms do you deconstruct and/or extract its matrix.

Morphisms of free modules are defined symbolically by sending generators to
linear combinations of generators. These are more properly defined in terms
of dicts or list of images, from which the matrices are automatically
constructed and extractible.


## Morphism Construction

Preferred construction is a **dict of generators and their images**.

Allowed classmethods:
- Take a domain and a sequence of images
- Take domain/codomain/matrix when applicable

**Do not** coerce matrices to morphisms. Force users to declare
domain/codomain and explicitly construct using element methods.


## Hom Spaces

`H := A.Hom(B)` is a **space of morphisms** $A \to B$, not a specific
morphism.

Create morphisms via:
- `H.from_dict(...)` (preferred)
- `H.from_matrix(...)`

Homs should have a reasonable method of infinite enumeration. Since every
$f \in \operatorname{Hom}(L_1, L_2)$ is a $\mathbb{Z}$-matrix, we can
bootstrap a centralized enumeration algorithm for $\mathbb{Z}^m$ to provide
an iterable generator for hom spaces.


## Morphisms and Categorical Semantics

- `hom()` constructs a hom-space, not a specific morphism requiring images.
- Elements of a hom-space are the morphisms.
- Bilinear-module objects need category-owned elements and morphisms, not
  plain Python wrappers carrying Sage objects on the side.
- The category should be hooked properly through Sage parent/category
  machinery, modeled on `sage.categories.modules`, with its own parent
  methods, element methods, and homset category.
- The actual Sage hook for custom homset construction is `_Hom_`; redefining
  `Hom` alone is not sufficient.
- Wrapped elements must be real Sage elements (`Element` /
  `ElementWrapper`-based), not plain Python wrappers carrying Sage objects on
  the side, or Sage morphisms will not compose through `Map.__call__`.
- Morphisms are not containers; no morphism class should define semantic
  containment for arbitrary values.
- `perp` / orthogonal-complement verbs do not belong on morphisms; those
  belong on the relevant subobject or ambient bilinear-module noun.
- General verbs should live as high in the hierarchy as their semantics
  allow: on `BilinearModule`, `BilinearModuleMorphism`,
  `BilinearModuleHomSpace`, and only specialize lower when extra structure
  genuinely appears.
- Cokernels must construct the correct mathematical object, which may be a
  lattice, torsion bilinear module, discriminant form, or another appropriate
  object depending on the context.
- `A_L := coker(L -> L^*)` must be modeled correctly.
- Dual lattices are rational lattices and may be quotiented by more than the
  original lattice.


## Subobjects as Morphisms

"Subobjects" are really morphisms, not objects themselves.

- A subobject needs some kind of mix-in that endows objects with an attached
  morphism and is where notions like "ambient" make sense
- Or one should have explicit `SubLattice` types which extend `Lattice` and
  add all of these notions

**Rule:** Regard a subobject as a morphism, or have explicit subobject
classes. Do not make "subobject" semantics optional notions on the object
itself.


## Subobjects and Division

**Subobject mixin:** Keep track of inclusion morphisms when constructing
subobjects.

- Every element $v$ in $L$ has an inclusion morphism
  $\iota_v: v.\text{span()} \to L$
- Every submodule is defined as a span
  $M := L.\text{span}([v_1, \dots, v_n])$ and a morphism $\iota_M: M \to L$

**Division (`/`):** `B / A` always means `B / im(f)` for some $f: A \to B$.
This requires the subobject mixin which keeps track of inclusion morphisms.

**General cokernel machinery:** Division is completely general and always
yields some bilinear module. Special case: the metric inclusion
$\iota_L^\#: L \to L^\#$ yields the discriminant group $A_L$ as a case of
automatic promotion.


## Discriminant Groups and Duals

One needs to carefully distinguish the maps:

- the module Hom dual $L^\ast := \operatorname{Hom}_{\mathbb{Z}}(L, \mathbb{Z})$,
  whose elements are functionals and live in `Modules(ZZ).DualObjects()`;
- the metric dual $L^\# := \{v \in L_{\mathbb{Q}} \mid \beta(v, L) \subseteq
  \mathbb{Z}\}$, whose elements live in scalar extension and are not functionals by
  definition;
- the metric inclusion $\iota_L^\#: L \to L^\#$;
- the form-induced transport $L^\# \to L^\ast$, `x |-> beta(x, -)`, which is a
  recorded map or isomorphism only under the necessary nondegeneracy hypotheses.

The discriminant group is computed from the metric-dual diagram:

```text
L  ->  L^#  ->  A_L = coker(L -> L^#).
```

Do not describe elements of `L^#` as "dual objects" merely because classical lattice
notation calls `L^#` the dual lattice. Category-theoretic dual objects are
evaluation-bearing Hom objects. In unimodular identity-form examples these
constructions can be canonically identified, but the identification is extra structure,
not the definition.

This should NOT be abstractly constructed from invariants or SNF -- morphisms
like $\iota_L$ should be constructible from matrices and have well-defined
cokernel bilinear modules which are automatically promoted.

One should have a **working vocabulary** of bilinear modules, their morphisms,
cokernels, submodules, etc. One should **not short-circuit** this when
constructing discriminant groups.

Discriminant form values live in quotient codomains. For `R = ZZ`, the
bilinear codomain is `QQ/ZZ` and the quadratic codomain is `QQ/2ZZ` when
that refinement exists. A method that computes by calling `lift()` on a
Sage torsion element must be localized interop; the public object and its
tests should ask quotient-valued questions directly.

Discriminant group morphisms follow the same Hom-space discipline as lattice
morphisms. Constructors belong on the declared Hom object and may accept
generator-image dictionaries, ordered images, callables, or matrices. The
result is a morphism object; image, kernel, injectivity, surjectivity, and
identity checks must use the morphism's actual categorical image/kernel, not
cardinality comparisons or helper names such as `image_generators`.

Nikulin-style invariants belong to the lattice theorem context. The invariant
`a` is meaningful in the even indefinite 2-elementary branch; a generic
`p_rank` method is not admitted unless a source-backed definition states the
object and hypotheses. The discriminant group may expose
`is_p_elementary(p)`, but `delta`, `coparity`, and the tuple `(r, a, delta)`
are lattice invariants, not free-standing invariants of `A_L`.


## Stabilizers and Centralizers

Stabilizers, centralizers, etc. should be defined on Orthogonal group
objects:

```python
G = L.orthogonal_group()
f = ...
H = G.centralizer(f)
Hp = G.stabilizer(v)
Hp2 = G.stabilizer_of_flag([v1, v2, ...])
```

**Not** as indirected spaghetti methods like
`L.stabilizer_of_flag([v1, v2, ...])`.

Elements can have convenience methods:
- `v.stabilizer()`, `v.stabilizer(in_group=Gamma)`
- `f.centralizer()`, `f.centralizer(in_group=Gamma)`

**No restricted functions** like `centralizer_of_involution`. Instead, have a
generic centralizer function -- if you only support involutions right now,
assert:
```python
assert f.is_involution(), "Non-involutions are not yet supported"
```

Invariant and coinvariant sublattices are not raw-matrix methods on `L`.
They are subobjects obtained from an endomorphism: construct
`f in End(L)` first, then take the kernel of `f - id` or `f + id`. The same
rule applies to centralizers: a matrix backend result is converted to an
orthogonal-group element at the boundary, and `O(L).centralizer(f)` owns the
predicate.

Definite and indefinite backend paths are different obligations. A definite
centralizer may route through GAP after sign-normalizing a definite Gram
matrix, but an indefinite centralizer requires a real indefinite backend such
as Oscar/Hecke data. Do not manufacture a fallback subgroup or placeholder
generator set when the required backend is absent.


## Set Operations

- Use `&` and `|` to mean **intersect** and **union**.
- For modules and lattices, always mean the **span** of such.
- For groups or subsets of lattices (e.g., centralizers, isotropic vectors),
  use **ConditionSets**, and simply use `&` or `|` on those.


## ConditionSets and Membership

### Uniformization Principle

Every object in the hierarchy has two components:

1. **A universe set** -- the maximal ambient set from which elements of this
   type can come. Usually countable and canonically enumerable.
2. **A predicate** -- a condition on the universe that narrows it to exactly
   this object's elements. For most "plain" objects the predicate is trivially
   true (every element of the universe is in the object). For subobjects the
   predicate is nontrivial.

Together these form a `ConditionSet(universe, predicate)` that owns all
membership testing for the object. `x in obj` means exactly:
`x in universe` and `predicate(x)`.

### Universe Choices

| Object type | Universe |
|-------------|----------|
| `M = ZZ^n` (free module) | `ZZ^n` (all integer vectors of length n) |
| `T = ZZ/a + ZZ/b` (torsion module) | `ZZ/a × ZZ/b` (finite product) |
| `L` (integral lattice, rank n) | `ZZ^n` |
| `L*` (dual lattice) | `QQ^n` |
| `O(L)` (orthogonal group) | `GL_n(ZZ)` with predicate `M^T G_L M == G_L` |
| `Hom(L1, L2)` | `Mat_{m×n}(ZZ)` with predicate = module morphism condition |
| Submodule `S <= M` | Same universe as `M`, predicate = span containment |
| `G.centralizer(f)` in `O(L)` | Same universe as `G`, predicate = `O(L)` predicate AND commutativity |
| `G.stabilizer(v)` in `O(L)` | Same universe as `G`, predicate = `O(L)` predicate AND fixation |

The universe is always **the natural ambient object from which elements
are drawn**. Picking a too-small universe (e.g., using `O(L)` itself as
the universe for a subgroup) forces all membership testing through the
parent object, which is fine; picking a too-large universe (e.g., all
matrices over QQ) creates unnecessary predicate complexity.

### Predicate Composition via Native ConditionSet Operators

Sage's `ConditionSet` already implements `&` (intersection) and `|` (union).
**Use these native operators -- never hand-roll conjunction or disjunction
classes.**

```python
isometry_cs  = ConditionSet(universe, IsometryPredicate(G_L))
commute_cs   = ConditionSet(universe, CentralizerPredicate(f))
fixation_cs  = ConditionSet(universe, StabilizerPredicate(v))

centralizer_cs  = isometry_cs & commute_cs      # ConditionSet &
stabilizer_cs   = isometry_cs & fixation_cs     # ConditionSet &
combined_cs     = centralizer_cs & stabilizer_cs  # chain as needed
```

`x in combined_cs` reduces to: `x in universe` and
`IsometryPredicate(G_L)(x)` and `CentralizerPredicate(f)(x)` and
`StabilizerPredicate(v)(x)`.

This is why `&` and `|` work uniformly on any pair of subgroups,
submodules, or condition sets without special-casing.

From the specs:
```python
combined = O_U.centralizer(f_neg) & O_U.stabilizer(e)
# predicate(g) = is_isometry(g) AND g*f_neg == f_neg*g AND g(e) == e
assert O_U.identity() in combined    # identity satisfies all three
assert f_neg not in combined         # f_neg(e) = -e, fails fixation
```

### Centralized Predicates

**Common predicates must be defined once and referenced everywhere.**
Do not reproduce the matrix equation `M^T G M == G` at every call site.
Instead, define once:

```python
# predicates.py -- centralized predicate definitions

class IsometryPredicate:
    """f preserves the bilinear form: M^T G M == G."""
    def __init__(self, gram_matrix):
        self._G = gram_matrix

    def __call__(self, f):
        M = f.to_matrix()
        return M.T * self._G * M == self._G

class CentralizerPredicate:
    """f commutes with g: f * g == g * f."""
    def __init__(self, g):
        self._g = g

    def __call__(self, f):
        return f * self._g == self._g * f

class StabilizerPredicate:
    """f fixes v: f(v) == v."""
    def __init__(self, v):
        self._v = v

    def __call__(self, f):
        return f(self._v) == self._v

class LinePredicate:
    """f preserves <v>: f(v) in {v, -v}."""
    def __init__(self, v):
        self._v = v

    def __call__(self, f):
        return f(self._v) == self._v or f(self._v) == -self._v
```

All subgroup constructors (`centralizer`, `stabilizer`,
`stabilizer_of_isotropic_line`, `kernel_of_discriminant_action`, etc.)
compose these centralized predicates rather than writing new matrix
equations.

### Example: O(L) and Its Subgroups

```python
# O(L):
# universe = GL_n(ZZ)
# condition_set = ConditionSet(GL_n(ZZ), IsometryPredicate(G_L))

O_L = LatticeOrthogonalGroup(L)

# centralizer(f): intersect O(L)'s ConditionSet with a new one
commute_cs = ConditionSet(GL_n(ZZ), CentralizerPredicate(f))
centralizer_f = LatticeOrthogonalSubgroup(O_L, O_L.condition_set & commute_cs)

# stabilizer(v): intersect O(L)'s ConditionSet with a new one
fix_cs = ConditionSet(GL_n(ZZ), StabilizerPredicate(v))
stabilizer_v = LatticeOrthogonalSubgroup(O_L, O_L.condition_set & fix_cs)

# Intersection via native &:
# ConditionSet & ConditionSet uses Sage's built-in operator
combined = centralizer_f & stabilizer_v
# combined.condition_set = (O_L.condition_set & commute_cs) & fix_cs
```

**The result:** `__contains__` on any subgroup reduces to one `ConditionSet`
membership test. No ad-hoc matrix equations scattered across methods.
Predicate logic is compositional and uses only Sage's existing machinery.

Backends may use row-action matrices, but the public group API uses left
column action. Conversion from a backend row-action matrix to a public
orthogonal-group element is a boundary operation, after which membership in
`O(L)` is tested only by the centralized predicate
`G.T * gram(L) * G == gram(L)`. Do not repeat the opposite row-action equation
in public methods.


## Julia Backend via sage-julia-bridge

The project at `~/sage-julia-bridge` provides a lightweight bridge to a
long-lived Julia subprocess. It evaluates Julia code, converts results
(integers, rationals, vectors, matrices) back to Sage objects, and
supports packages such as Oscar/Hecke/Nemo loaded on the Julia side.

**When to use the Julia backend.** Julia's lattice packages (Oscar, Hecke)
handle algorithms where Sage is weak or absent:

| Method | Preferred backend |
|--------|------------------|
| Indefinite integral isometry | Julia (Oscar/Hecke `is_isometric`) |
| Genus computations, local conditions | Julia (Hecke `genus`) |
| Class groups, automorphism groups | Julia (Hecke `automorphism_group`) |
| Fast LLL / short vectors | Julia (if ever needed -- see Banned) |
| Quadratic form theory (genus symbols) | Julia (Hecke) |
| Discriminant form classification | Sage (small group methods are fine) |
| Direct sums, spans, cokernel | Sage (our own morphism machinery) |
| Named constructors, parsing | Sage (our own code) |

**Architectural rule.** Every `Lattice` object stores TWO backends:

```python
class Lattice(RationalLattice):
    _sage_lattice: IntegralLattice    # Sage backend (always present)
    _julia_lattice: object | None     # Julia repr, lazily initialized
```

The Julia representation is lazily constructed on first use of a
Julia-backed method. It is NOT part of the public API -- callers use
`L.is_isometric_to(M)`, not `L._julia_lattice`. Backends are an
implementation detail.

**Bridge usage pattern:**

```python
from sage_julia_bridge import julia

def _julia_repr(self):
    """Lazily construct Julia lattice from Gram matrix."""
    if self._julia_lattice is None:
        julia.eval("using Hecke")
        julia.set("G", self.gram_matrix())
        self._julia_lattice = julia.eval("integer_lattice(G)")
    return self._julia_lattice

def is_isometric_to(self, other, witness=False):
    """Isometry check, delegated to Julia for indefinite lattices."""
    self._julia_repr()
    other._julia_repr()
    julia.set("G1", self.gram_matrix())
    julia.set("G2", other.gram_matrix())
    result = julia.sage(
        "is_isometric_with_isometry(integer_lattice(G1), integer_lattice(G2))"
    )
    # result is (bool, matrix) or similar; parse and wrap
    ...
```

**No leakage.** The Julia session is an internal implementation detail.
Public callers never receive Julia objects, never see Oscar/Hecke types,
and never construct the bridge directly. The bridge is accessed only
through methods on our objects.


## Invariants and Theory Placement

- `delta` / `coparity` are invariants of lattices `L`, not of discriminant
  groups `A_L`.
- `outside_domain` should not be a separate ad hoc notion when the meaningful
  predicate is `is_p_elementary(2)`.
- Isometry verification belongs in the containment semantics of `O(L)`, not
  scattered matrix-equation assertions.
- Theorem-domain warnings belong on the lattice-level method that invokes the
  theorem. Generic discriminant-group helpers must not claim Nikulin
  invariants outside the even indefinite 2-elementary lattice hypotheses.


## API Hierarchy and File Organization

- The redesign must use a real hierarchy of files under a subdirectory
  structure, not a monolithic public file.
- The existing generated code should be migrated into the organized
  hierarchy, not discarded and restarted from scratch.
- Public API terminology should be semantic and stable; do not preserve stale
  names from older designs.


## Typing, Validation, and Dispatch

- Do not use `hasattr` or ad hoc runtime probing where proper typing and
  dispatch are intended.
- Add real type annotations throughout the hierarchy.
- Use Pydantic validation rather than loose assertions for public-object
  validation.
- Do not use `pass` where simple ABCs should be defined.
- Do not use `assert False` in places where mathematically meaningful objects
  must be constructed.
- A discriminant form built from invariant factors and quotient-valued Gram
  data must validate symmetry, rank agreement, positive invariant factors, and
  compatibility `d_i * d_j * gram[i, j] in ZZ` for the chosen generators. The
  empty invariant list still constructs the zero object in the discriminant
  category, not `None` or a special-case data record.


## Anti-Wrapper / Anti-Slop Rules

- Do not introduce helper functions that merely wrap obvious one-line Sage
  functionality.
- Do not create helpers like `zero_gram` when `zero_matrix()` already exists.
- Do not create helpers like identity-column builders when `identity_matrix()`
  already exists.
- Do not create row-oriented constructor helpers when the semantics are really
  about generators or standard objects already available in Sage.


## Terminology and Interop

- Do not expose `native` terminology on the public API.
- If Sage interop must exist, use explicit "sage-like" extraction, not leaked
  wrapper passthroughs.
- Constructors should build and store their internal Sage object themselves.
- Separate class methods may accept Sage objects and convert them internally.
- No public object should require a Sage object as its constructor input.


## Semantics Explicitly Rejected

- `signature_vector` on the public API.
- `merge_orbit_constraints` or parallel subgroup-constraint bookkeeping when
  `ConditionSet` should express subgroup restrictions directly.
- `scaled_element` as a semantic public operation on free-module elements.
- `submodule_from_rows`; submodules are defined by generators, not matrix
  rows as a public noun.
- `projection_lattice`; lattices do not canonically project onto sublattices.
- `lift_vector`; lifts in this context are elements of `L^*`, not bare
  vectors.
- `vec_to_list` style shims.
- old shim names like `has_isomorphic_group_structure_to`.
- ill-defined invariants or algorithms such as the cited `p-rank` method.


## Banned / Out-of-Scope Constructs

- LLL
- Short vectors/closest vectors
- min/max vectors
- `signature_pair` [the pair (p,q) is just called the signature]
- signature defined as p-q [this is the index, not the signature]
- `rescale`, or "scale" used as a verb instead of a noun [scale is an
  invariant, not an operation]
- `IntegralLattice`, `IntegralLatticeGluing`, etc [LatticeGlueData is its
  own class, and `from_glue_data` is a verb for construction]
- `IntegralLatticeDirectSum` [need a bilinear module native solution]
- bases, echelon forms, ambient modules [our lattices are not subsets of any
  "ambient" object]
- Regarding vectors as elements and matrices as morphisms [ill-defined:
  vectors must be EXTRACTED from semantically constructed lattice elements;
  morphisms must be CONSTRUCTED, possibly from a matrix]
- `basis()` [modules have generators, not bases -- "basis" means "generators
  of a K-module" where K is a field]
- `ambient_vector_space`, `vector_space`, etc [module machinery is more
  natural; `L.base_change(QQ)` HAS an associated vector space but is really
  a bilinear QQ-module]
- `basis_matrix` [doesn't make sense, always identity for us]
- `dimension` [free modules have ranks, not dimensions]
- `inner_product` [we do not special case positive definite forms; an
  arbitrary bilinear form is NOT an inner product]
- sparse/dense vectors, matrices [irrelevant numerical optimizations]
- pseudohoms [implement real `Der_R(L_1, L_2)` if needed]
- `complement` [only use `perp()` == orthogonal complement]
- intersections, subspaces, Sage's `A+B` span notation [use explicit
  `L.span([..])` semantics, reserve `+` for direct sum]
- top-level `span` function [not well-defined without specifying the ambient
  lattice; use `L.span([..])`]


## Style Principles

The following principles are distilled from the authoritative `*.sage` spec
files in `tests/`. They generalize the style to any new code, including
objects and constructions not yet specced. For concrete method signatures
and behavioral contracts, read the spec files themselves:

- `tests/sage_spec/misc.sage` -- module theory
- `tests/sage_spec/lattice_methods.sage` -- orthogonal groups, spans, perps,
  eigenlattices, roots, Weyl, Coxeter, enumeration
- `tests/lattice_spec/interface_semantics.sage` -- constructors, elements,
  discriminant, orbits, stabilizers
- `tests/lattice_spec/interface_extensions.sage` -- duals, embeddings,
  saturation, explicit groups, Eichler
- `tests/lattice_spec/more_specs.sage` -- dual functionals, twist vs
  multiplication, torsion bilinear modules
- `tests/sage_spec/coxeter.sage` -- root lattices, Coxeter diagrams,
  folding


### Write Code That Reads as Mathematics

Prefer syntax that mirrors how a mathematician would write it on a
blackboard. Sage's preparser and operator overloading exist precisely for
this.

| Prefer | Avoid |
|--------|-------|
| `ZZ^n` | `FreeModule(ZZ, n)` |
| `ZZ/2` | `ZZ.quotient(ZZ.ideal(2))` |
| `2*ZZ` | `ZZ.ideal(2)` |
| `M + N` | `M.direct_sum(N)` |
| `M * N` | `M.tensor_product(N)` |
| `B / A` | `B.quotient_by(A)` |
| `L^G` | `G.invariant_sublattice()` |
| `G <= H` | `G.is_subgroup_of(H)` |
| `f^2 == id` | `f.is_involution()` (as a definition; ok as a convenience) |

The test for whether syntax is right: could you copy-paste it into a
textbook and have it be understood? `ZZ^3` reads as "$\mathbb{Z}^3$";
`FreeModule(ZZ, 3)` reads as a Java constructor.

**This requires extensive operator overloading.** Every object must
implement all mathematically meaningful dunder methods: `__eq__`,
`__contains__`, `__add__`, `__mul__`, `__rmul__`, `__sub__`, `__pow__`,
`__truediv__`, `__and__`, `__or__`, `__le__`, `__iter__`, `__abs__`, etc.
If a mathematical operation exists for the object, the corresponding Python
operator must work. No object should force the user into method-call syntax
for an operation that has standard mathematical notation.


### Exact and Algebraic, Never Floating Point

All computations must remain exact and symbolic. Never use `RR`, `CC`,
floating point, or numerical approximation as a working medium. Instead,
name the minimal ring or field extension where the computation lives
exactly.

| Prefer | Avoid |
|--------|-------|
| `cos(pi/3)` as a symbolic expression | `0.5` or `RR(0.5)` |
| `QQ[pi]` (transcendental extension) for Coxeter angles | `RR` or `QQbar` |
| `QQ(sqrt(2))` (algebraic extension) when needed | `AA` or `RDF` |
| `Zp(5)` (exact p-adics) | floating-point approximations |
| `n()` called explicitly and late, only for display | numerical intermediates |

The principle: every intermediate value should live in a named exact ring.
If you compute `cos(pi/3)`, keep it as the symbolic expression `cos(pi/3)`
or as `QQ(1/2)` -- either way it's exact. An angle matrix should live in
`GL(n, QQ[pi])`, not `GL(n, RR)`.

This is not a performance concern; it is a correctness concern. Floating
point breaks equality testing, breaks containment checks, and silently
introduces errors that are invisible until they compound. Exact arithmetic
makes `==`, `in`, and all the other mathematical operators actually
trustworthy.


### Containment Over Equations

The single most important principle. To verify a property of an object,
**check that it lives in the right set**, don't reproduce the defining
equations of that set.

**Bad:**
```python
assert all(m in ZZ for m in M.gram_matrix().list())
assert f.to_matrix().T * G * f.to_matrix() == G
```

**Good:**
```python
assert M.gram_matrix() in GL(n, ZZ)
assert f in L.O()
```

Why: `f in O(L)` asserts a *mathematical theorem* -- that `f` is an
isometry. The manual matrix equation asserts a *programming fact* that
happens to be equivalent. The set-membership version:

- Has one source of truth for the defining equation (inside `O(L).__contains__`)
- Prevents convention drift (left vs right action, transpose conventions)
- Reads like mathematics
- Generalizes: the same pattern works for `f in Hom(L_1, L_2)`,
  `v in ZZ^n`, `M in Modules(ZZ)`, `G in Groups`

**Corollary -- assert mathematical content, not implementation
tautologies:**

```python
# Rich mathematical fact: base change preserves module structure
assert L.base_change(ZZ/2) in Modules(ZZ) and L.base_change(ZZ/2) in Modules(ZZ/2)

# Tautology: reads back a constructor argument
assert L.base_ring() == ZZ
```

The first tells you something about the *category theory* of base change.
The second tells you nothing you didn't already know from constructing `L`.
Prefer assertions that would be nontrivial theorems.


### Categories Over Classes

Never use `isinstance` or `hasattr` to determine what an object is. These
are Python implementation details. Use category containment instead --
this is the mathematically meaningful test, and it is what determines
interoperability.

**Bad:**
```python
isinstance(M, FreeModule)
hasattr(f, 'kernel')
type(L) == IntegralLattice
```

**Good:**
```python
M in Modules(ZZ)
f in L.Hom(L)
L in Lattices(ZZ)
```

Why: the literal Python class is an implementation artifact. What matters
is which *category* the object lives in, because that determines which
verbs it supports, what morphisms exist between it and other objects, and
how constructions (limits, colimits, functors) apply to it. An object can
be in `Modules(ZZ)` and `Modules(ZZ/2)` simultaneously; no `isinstance`
check can express this.

This applies equally to dispatch: where Python code would use `isinstance`
to branch, mathematical code should branch on category membership.


### Specs Assert Nontrivial Mathematics

Spec assertions should encode real computations and mathematical facts, not
just "construct and check the type." The right way to spec an object is to
do the math by hand, then record the calculation so that anyone can
rederive it and verify the assertion independently.

**Bad spec -- construction check:**
```python
G = L.orthogonal_group()
assert G is not None
assert len(G.gens()) > 0
```

**Good spec -- explicit mathematical content:**
```python
G = L.O()
f1 = G.from_matrix(minus_I2)
f2 = G.from_matrix(swap)
assert f1 in G and f2 in G                     # Category containment
assert f1^2 == G.identity() and f2^2 == G.identity()  # Orders
assert {F.to_matrix() for F in G} == {id, m1, m2, m1*m2}  # Exhaustive enumeration
assert [f2(x) for x in [e,f]] == [f, e]        # Explicit evaluation on generators
assert G.stabilizer(e+f) == f2.cyclic_subgroup()  # Structural consequence
```

The good spec:
- Constructs morphisms explicitly from matrices, routed through hom sets
- Shows they generate the group by enumerating it
- Evaluates them on specific generators to verify the computation
- Asserts structural consequences (stabilizer equals a specific subgroup)
- Tests categorical interop (where objects live, what categories they're in)
- Can be independently verified by hand

Every assertion should be something a mathematician would find nontrivial
enough to write as a lemma, or an explicit computation they would include
in a proof.


### Equality Means Canonical Isomorphism

`==` has a precise mathematical meaning: two objects are equal when there
is a *canonical* isomorphism between them -- one that is uniquely
determined by the universal property, not one chosen by an algorithm.

```python
assert M/(2*M) == M.tensor(ZZ/2)          # Universal property of tensor
assert M.base_change(ZZ/2) == M.tensor(ZZ/2)  # Universal property of base change
assert M.dual() == M.Hom(ZZ)              # Definition of module Hom dual
assert L.discriminant_group() == L.dual_lattice() / L  # Metric-dual cokernel
```

This is not just sugar. It enforces that the universal property is actually
implemented: the base change of `M` to `ZZ/2` must *be* the tensor product,
not merely be isomorphic to it.

**For lattices:** `L1 == L2` means isometric via the identity matrix --
i.e., the same lattice, not just an isomorphic one. `L1.is_isometric_to(L2)`
is the weaker statement.

**For subobjects:** a subobject whose inclusion morphism is the identity is
`==` to the ambient object restricted to those generators. A subobject with
a nontrivial inclusion is `is_isometric_to` but not `==`.

**For morphisms:** `f == g` means equal domains, equal codomains, and equal
matrix representations (or equivalently, equal on all generators).


### Verbs Live on the Right Noun

Every mathematical verb belongs on the object that *owns* that concept.
When in doubt, ask: "In a textbook, what object is the subject of this
sentence?"

- Stabilizers, centralizers, orbits -> methods on the group, not the lattice
- Perp, span -> methods on the element or subobject, not the ambient space
- Kernel, cokernel, image -> methods on the morphism
- Invariants (delta, coparity) -> methods on the lattice, not its
  discriminant group

**Bad:** `L.centralizer_of_involution(f)` -- the lattice is not computing
centralizers; the group is.

**Good:** `L.O().centralizer(f)` -- the orthogonal group owns the concept.

This generalizes: if you're adding a new verb and it feels awkward on the
noun you've chosen, you probably need a different noun.


### Constructions Return Objects, Not Data

Every categorical construction (kernel, cokernel, image, dual, span, perp,
etc.) must return a fully-formed object in the appropriate category, not
raw data.

- `f.kernel()` returns a bilinear module, not a matrix or a list of vectors
- `f.cokernel()` returns a bilinear module with `.projection()` and `.lift()`
- `v.span()` returns a subobject (with inclusion morphism), not a set
- `M.dual()` for a module returns a Hom-dual object whose elements are functionals
- `L.dual_lattice()` returns the metric dual `L^#`; its elements become functionals
  only after applying a recorded form-induced transport map when the hypotheses hold

The returned object must be complete: it must live in the right category,
support all the verbs that category provides, and have correct morphisms
connecting it back to its source. If `f.cokernel()` doesn't have a
projection morphism from `B`, it's not a cokernel -- it's a data leak.


### Every Category Has Explicit Constructors

Every category must provide simple, concrete ways to create its objects
and morphisms from data. Objects are created from mathematical data (a
module and a form, a ring and a matrix, etc.). Morphisms are created from
hom spaces, which accept dicts, image lists, matrices, or callables -- but
the morphism is never *literally equal to* any of those things.

```python
# Objects from data
L = BilinearModule(ZZ^3 + ZZ/2, gram_matrix)
H = L1.Hom(L2)

# Morphisms from data (not equal to the data)
f = H.from_dict({e: f, f: e})
g = H.from_matrix(M)
h = H.element_from_function(lambda x: ...)

assert f.to_matrix() == M      # Can extract the matrix
assert f != M                  # But the morphism is not the matrix
assert M not in H              # And the matrix is not in the hom space
```

This applies recursively: the elements of a module are constructed via the
module's `__call__` or `element_from` methods, not by passing raw vectors.
The elements of a group are constructed via the group's element
constructors, not by passing raw matrices.


### Automatic Category Promotion

Objects promote to the richest category their invariants support. This is
not optional; all constructions must check and promote.

```python
assert e.span() in ModulesWithForms(ZZ).Bilinear()  # Degenerate, not a lattice
assert e.span() not in Lattices(ZZ)
assert e.perp()/e in Lattices(ZZ)              # Quotient happens to be nondegenerate
```

The principle: **don't force the user to know in advance what category the
result will land in.** When a quotient of bilinear modules happens to be
nondegenerate, it should automatically be a `Lattice`, not a generic
`BilinearModule` that the user must manually cast. Similarly, a root
sublattice should automatically be in `RootLattices`, a hyperbolic lattice
in `HyperbolicLattices`, etc.

Rational-to-integral promotion has one owner. A rational free bilinear object
constructed from a Gram matrix should decide, in that constructor or refinement
route, whether the form is integral and then promote to `Lattice` when
appropriate. Call sites should not each re-run their own integrality check.
Named constructors may return the richest correct object; for example an
integralized presentation of an `F_4` root object comes from an explicit twist
of the rational presentation, not from hiding the rational presentation inside
an integral-only constructor.


### Operators Mean One Thing

Each operator has exactly one mathematical meaning across the entire
hierarchy. Never overload an operator to mean different things in different
contexts.

| Operator | Universal meaning |
|----------|-------------------|
| `+` | Direct sum (external). Never "span" or "union" |
| `*` | Tensor product (of modules), or composition (of morphisms) |
| `/` | Cokernel of the natural inclusion |
| `^` | Power: `L^n` = n-fold direct sum, `f^n` = n-fold composition, `L^G` = invariant sublattice |
| `in` | Category or parent containment. Never automatic coercion |
| `&` | Intersection (of sets, groups, condition sets) |
| `|` | Union / join |
| `<=` | Subset / subgroup containment |

**Critical distinction -- `+` vs `span`:**
`e.span() + f.span()` is the *external* direct sum (zero off-diagonal
entries). `L.span([e, f])` is the *internal* span within `L` (inherits the
bilinear form of `L`). These are mathematically different and must not be
confused.

**Critical distinction -- `twist` vs scalar multiplication:**
`L.twist(n)` scales the *form* by `n`: the gram matrix becomes `n*G`.
`n*L` scales the *generators* by `n`: the sublattice `{n*v : v in L}`.
The resulting gram matrix of `n*L` is `n^2 * G`, not `n*G`.


### Elements Are Symbolic, Not Numerical

In `U`, the expression `e + f` is the formal symbol $e + f$, not the
vector `[1, 1]`. Elements live in their parent; numerical representations
are extracted explicitly when needed.

```python
L.<e, f> = Lattice.U()
v = e + f               # A formal element of L
assert v in L            # Yes
assert [1, 1] not in L   # A list is not an element
assert v.to_vector() == vector(ZZ, [1, 1])  # Explicit extraction
```

**Matrices are not morphisms. Vectors are not elements.** A matrix is a
numerical representation of a morphism in a chosen basis. A vector is a
numerical representation of an element in a chosen basis. The
basis-dependent data is never conflated with the basis-independent object:

```python
swap = matrix(ZZ, [[0,1],[1,0]])
assert swap not in L.O()                    # A matrix is not a hom
assert L.O().from_matrix(swap) in L.O()  # Construct, then check
```

This separation defers basis-dependent choices until they are absolutely
necessary for numerical computation. Code that works with formal elements
and morphisms is more general, more readable, and less error-prone than
code that works with vectors and matrices directly.


### Explicit Morphisms, No Implicit Identifications

Subobjects, inclusions, and containment always go through explicit
morphisms. The type system should catch mathematical errors during
experimentation by refusing to silently identify objects across different
parents.

```python
L.<e, f> = Lattice.U()
S = e.span()                # <e> as a sublattice
iota = S.inclusion()        # The chosen embedding iota: <e> -> U

# e was constructed as a generator of U, so e is an element of U
assert e in L

# S has its own generator
ep = S.gens()[0]
assert ep in S              # ep is an element of S

# ep is NOT automatically an element of U -- it lives in a different parent
assert ep not in L

# Its IMAGE under the inclusion IS an element of U
assert iota(ep) == e
assert iota(ep) in L
```

**The general principle:** very few surprise coercions, at the cost of
needing to explicitly work categorically. This forces proper mathematical
hygiene. If `A` is isomorphic to `B` but not by the identity, then `v in A`
does NOT mean `v in B`. Only `f(v)` is in `B`, where `f` is the specific
isomorphism.

**Containment cascades through morphisms:** `e in S` and `S <= L` are both
true. But "moving" `e` from `S` to `L` requires applying `iota`. The
chain of inclusions is explicit, not automatic. This is what makes it
possible to catch errors like confusing an element of `L` with an element
of `L^*`, or an element of `A_L` with its lift to `L^*` -- mistakes that
silent coercion would hide and that are genuinely hard to debug in
numerical lattice computations.

**The basic idea:** make the type system work FOR you. During
experimentation and computation, the strict containment rules will catch
mathematical errors (wrong parent, wrong ambient, confused identification)
at the point where they happen, not three steps later when a matrix
equation silently produces garbage.


### Validation at Construction

Whether a map is a morphism in a given category is checked at construction
time, as part of hom-space element creation -- not as a post-hoc assertion.

```python
# Good: validation happens inside from_matrix
f = L.O().from_matrix(swap)  # Checks isometry condition internally
assert f in L.O()                    # Redundant but readable

# Bad: construct a raw object, then separately check validity
f = SomeMap(swap)
assert f.to_matrix().T * G * f.to_matrix() == G  # Post-hoc verification
```

This applies generally: all categories should validate their construction
contracts at the point where objects are created. Hom spaces validate that
maps preserve the relevant structure. Module constructors validate that the
gram matrix is symmetric. Group element constructors validate the group
axioms. The resulting objects are then *known* to be valid by construction,
and post-hoc checks are unnecessary (though acceptable as spec assertions
that encode mathematical content).


### Witnesses for Existence Claims

Any method that answers an existence question ("is there an isometry?",
"is this isomorphic?") should optionally return a witness:

```python
is_isom, f = L1.is_isometric_to(L2, witness=True)
assert f in L1.Hom(L2)
```

The witness is itself a mathematical object (a morphism, an element, etc.)
that lives in the appropriate hom space or parent. It is not a matrix, a
dict, or a boolean -- it is a proof.

Conversely, all objects support `is_isomorphic_to` (or the appropriate
variant for the category: `is_isometric_to` for bilinear modules,
`isomorphic_as_groups` for groups, etc.).


### Every Object Has a Universe and a Predicate

Every object carries two things: a **universe set** (the maximal ambient
set elements can come from) and a **predicate** (the condition that
narrows the universe to exactly this object's members). Together they form
a `ConditionSet` that owns all membership testing.

For a "plain" module or lattice, the predicate is trivially true: every
element of the universe (e.g., `ZZ^n`) is in the object. For a subobject,
the predicate is nontrivial: centralizers add a commutativity condition,
stabilizers add a fixation condition, orthogonal groups add an isometry
condition. But in all cases the architecture is the same.

```python
# O(L): universe = GL_n(ZZ), predicate = M^T G M == G
O_L = L.O()

# Centralizer: same universe, AND commutativity with f
C_f = O_L.centralizer(f)

# Stabilizer: same universe, AND fixes v
S_v = O_L.stabilizer(v)

# Intersection via & = AND of predicates
# x in (C_f & S_v)  iff  x in O_L and f*x == x*f and x(v) == v
combined = C_f & S_v
```

**Predicates are centralized, not repeated.** Define `IsometryPredicate`,
`CentralizerPredicate`, `StabilizerPredicate`, etc. once in
`predicates.py`. All subgroup and subobject constructors compose these
centralized predicates instead of writing inline matrix equations. The
defining equation `M^T G M == G` appears exactly once in the codebase.

See the "ConditionSets and Membership" section for the full architectural
details and universe-choice table.


### Everything Has an Underlying Set

Every mathematical object carries an underlying set. This set must be a
real object: it has a cardinality, it supports membership testing via `in`,
and it supports iteration via `__iter__`. This is not optional
infrastructure -- it is the mathematical content.

```python
assert (ZZ/4).as_set() == {(ZZ/4)(0), (ZZ/4)(1), (ZZ/4)(2), (ZZ/4)(3)}
assert (ZZ^3).rank() == 3  # Finite rank but infinite cardinality
```

**Generators on everything:** All countable objects support `__iter__`.
Infinite objects use lazy generators that "spiral" outward from small
elements. Iteration follows the mathematical structure, not an
implementation-convenient ordering. For `ZZ^n`, this means a
diagonal-argument enumeration visiting elements of increasing norm. For
a group, this means enumerating by word length in generators.

**Cardinality on everything:** `len()` for finite objects, and
mathematically meaningful cardinality invariants for infinite ones (rank
for free modules, invariants for FGP modules, etc.).

The user should be able to iterate over the elements of any hom space, any
group, any lattice, any discriminant group -- anything with a well-defined
underlying set. The implementation may be lazy, but the *contract* is that
the set exists and can be queried.


## Spec Authority and Execution Discipline

- The lattice spec is authoritative.
  If a behavior appears in the normative spec files, it is required target
  behavior until the user explicitly revises that status.
- Do not describe unmet spec surface as "aspirational", "optional",
  "migration-only", or otherwise outside the redesign gate merely because the
  implementation does not satisfy it yet.
- Do not describe unfinished required implementation as a "blocker".
  It is remaining required work on the spec itself.
- Do not treat completion of a local redesign slice as completion of the task.
  The task ends only when the required spec surface is actually implemented.
- The redesign plan is a signoff artifact and must stay truthful.
  It must not claim architectural completion while required spec work remains.
