# Contribution Guidelines and Policy Index

This document defines the contribution policies for the repository.
All contributions must follow the categorized policy index below.
Each policy has a unique alphanumeric identifier.

* * *

## Preamble design philosophy

The preamble is an **interactive discovery language for mathematics**, not a flat library of globally named functions.  A user should be able to start from the mathematical object already in hand and discover the language locally with tab completion.  If `C` is a category, `C.<TAB>` should expose the constructions and structure that `C` knows; if `M` is a module, `M.<TAB>` should expose module-level operations; if `x` is an element, `x.<TAB>` should expose element operations; if `f` is a morphism, `f.<TAB>` should expose morphism operations; and Homsets, functors, subobjects, and other mathematical objects should likewise expose the operations they own.  The receiver is part of the mathematical documentation: it tells the user what kind of thing an operation acts on and sharply narrows the admissible language before any manual or source file is opened.

This is a deliberate contrast with a GAP/Julia-style global operation catalogue.  A global name such as `Product`, `Kernel`, or `Orbit` gives almost no local information about its domain: the user must already know whether it acts on categories, parents, morphisms, elements, families, or some combination.  As the system grows, that design requires memorizing an ever larger language or repeatedly consulting documentation.  The preamble instead scales by **navigating from mathematical objects to their methods**.  The public global namespace therefore exists primarily for canonical mathematical objects, category/object constructors, notation entry points, and genuinely language-level forms—not as a convenience catalogue of operations on objects that already exist.

**Mathematical ownership determines API placement.**  An operation lives on the mathematical object whose structure makes the operation meaningful.  A category that claims products owns the construction of its selected products.  A Homset owns operations whose hypotheses are properties of that Hom.  Morphisms own morphism-level constructions; parents own parent-level constructions; elements own element-level operations; functors own functorial operations.  The code implementing the operation belongs with that owner or in its mathematical subtree.  Free-standing helpers may support notation internally, but they must not become a second public mathematical language.

The same ownership principle determines implementation dataflow.  Code should teach the repository a mathematical fact **where that fact lives**, and downstream behavior should follow from the object/category graph.  If `C` has products, teach `C` how to construct them; do not teach a global `Product(...)` dispatcher every category for which products happen to exist.  If equality of arrows is determined by structure of a Homset, teach that Homset; do not make a root equality helper enumerate concrete theories.  This is mathematical organization used as implementation compression: the general structure is stated once at its owner and inherited or delegated through the ordinary category machinery.


**Mathematical domain and computational domain are different.** Method placement follows the first category/object/element on which the notion is mathematically defined, not the currently decidable or implemented cases. Every set has a cardinality, so `cardinality()` belongs to sets even though no CAS can compute the cardinality of an arbitrary represented set such as `X = {n in NN | n.is_twin_prime()}`. Every formed module has a well-defined degeneracy predicate, so `is_nondegenerate()` belongs with formed modules even when the current implementation only decides finite-rank represented forms. The implementation may therefore route across the cases currently understood and assert-gate the remainder with an informative statement of the missing computational hypothesis. This is not a stub: supported cases must actually compute. Over time the routing table grows so that the computational domain converges toward the mathematical domain.

This is one of the few places where an explicit `case`/`match` or other routing table is positively desirable. It reads like mathematics: identify which represented situation the object lies in, invoke the theorem/algorithm appropriate to that case, and use an exhaustive final assertion for cases not yet computationally covered. The banned shape is a method whose entire body is failure (`assert False`, `NotImplementedError`, or equivalent) and which therefore advertises functionality without implementing any case at all.

**Infinite-compatible semantics come before finite-coordinate algorithms.**  The mathematical layer should be written so that replacing a finite indexing set by an infinite one, a finite basis by a lazy framing, or a matrix realization by an abstract Hom does not force a redesign of unrelated consumers.  Finite coordinates, rows, columns, exhaustive enumeration, and concrete arrays are computational specializations.  They belong behind semantic objects that remain meaningful in infinite settings: owned sets/families, finite-support elements, subobjects, Homs, kernels/images, products/coproducts, tensor/block constructions, actions, and universal properties.  A large blast radius when moving from finite to infinite data is strong evidence that coordinates or enumeration leaked above their proper layer.

**The public API is an adversarial semantic gate.**  It is judged not only by whether correct code can be written through it, but by which mathematically invalid shortcuts it makes easy to write.  If a caller holding a morphism can casually unwrap a matrix, compute a nullspace, and rebuild a pretend kernel, the interface is too permissive even when `f.kernel()` also exists.  If an element constructor accepts a bare coordinate tuple, the API invites callers to forget the parent and framing that make those coordinates meaningful.  Close these hatches structurally: force construction through mathematical data, keep numerical representations private or one-way, and use assertions that reject a predicted shortcut while naming the correct construction.  The goal is not to trust every future consumer to remember the doctrine; the interface should make the semantic route the path of least resistance and the numerical bypass visibly abnormal.

**Repository prescriptions are part of the executable architecture.**  Issue bodies, plan cards, comments, docstrings, examples, tests, and migration notes train later contributors and agents just as neighboring source code does.  Once a mathematical or architectural ruling falsifies a prescription, correct or delete that prescription before implementation continues.  A stale comment that says “shared ambient,” a test that still unwraps coordinates, or an issue body that asks for a deprecated signature can faithfully regenerate the exact defect that the code was meant to remove.

**Diagnose recurring slop by generator, not by instance.**  A new occurrence of a known pattern is repaired by the existing rule; it does not earn another bespoke exception or workaround.  Add a catalogue entry only when review discovers a genuinely new code-shape generator.  The principal generators include presentation/object confusion, theorem proxies replacing definitions, stored or witness-free structure, signature-porting from a foreign ontology, contaminated prescriptions, and laundering mathematically correct failures instead of repairing what they expose.

**Specialization should be modular and dependency direction should normally point toward foundations.**  Adding a new specialized category should usually mean adding a subtree that imports the general categories it refines, declares its supercategories, and contributes its own methods, constructions, and algorithms.  Existing supercategories and unrelated siblings should ordinarily remain unaware that the new descendant exists.  A design in which `Cat.Products`, `Modules(R)`, or another general ancestor must import or branch on `MyVerySpecialResearchLatticeCategory` has the dependency direction backwards and gives a leaf addition an unreasonable blast radius.  Upward knowledge is not absolutely forbidden—occasionally a new leaf exposes a genuinely missing general abstraction—but it is a strong signal to recheck ownership and dataflow.

A useful extension test follows: **adding a mathematically local feature should have a mathematically local code footprint**.  A new leaf category, refinement, or specialized algorithm should not require edits across generic ancestors merely to register its existence.  Conversely, when implementing a feature forces repeated edits to global dispatchers, ancestor modules, unrelated siblings, or public export surfaces, first ask which mathematical owner or abstraction is missing.

These principles are more important than any current list of prohibited code shapes.  The policy codes below record concrete consequences and reviewable failure modes, but contributors should apply the discovery, ownership, locality, and dependency-direction model to new code even when no existing example names the exact violation.

## Corrective implementation style guide (`STY-*`)

This is a **living catalogue of concrete code shapes**.  Add a new entry whenever review identifies a recurring implementation pattern whose replacement is known.  Do not wait for the same mistake to recur in several files.  The point is to teach the repository's preferred constructions—not merely to ban today's instances.

The default order of preference is:

1. an owned mathematical operation on the category/parent/element/morphism/Homset/functor that owns the notion;
2. a mature library abstraction (`itertools`, `collections`, `functools`, graph/group/CAS APIs, etc.);
3. a declarative Python expression (comprehension, generator expression, `any`, `all`, `sum`, `min`, `max`, `next`, dictionary union, etc.);
4. an explicit stateful loop only when state evolution is actually the algorithm.

An explicit loop is not intrinsically bad.  Search, fixed-point iteration, backtracking, dynamic programming, state-machine protocols, and backend algorithms may be clearest as loops.  The smell is an imperative loop whose only job is to spell a standard map/filter/fold/group/traversal operation manually.

### One-shot red-flag lookup

Use this table during review before reading the longer entries below.  Each left-hand shape should immediately suggest the right-hand replacement; if the replacement is mathematical data rather than private Python data, use the owned mathematical construction first.

| Red flag | First replacement to consider |
| --- | --- |
| `result = []; for x in xs: result.append(f(x))` | `[f(x) for x in xs]`, `map(f, xs)`, generator, or owned image/family |
| `result = []; ... if p(x): result.append(x)` | `[x for x in xs if p(x)]` / `filter(p, xs)` |
| `result = []; for block in blocks: result.extend(block)` | `itertools.chain.from_iterable(blocks)` |
| `sum(rows, [])` | `itertools.chain.from_iterable(rows)` |
| `result = set(); ... result.add(f(x))` | `{f(x) for x in xs}` / `set(map(...))` / owned set |
| `result = {}; ... result[key] = f(x)` | dict comprehension |
| `d.setdefault(key, []).append(value)` | `collections.defaultdict(list)` or `itertools.groupby` for sorted streaming input |
| `d[key] = d.get(key, 0) + 1` | `collections.Counter` |
| `d[key] = d.get(key, zero) + value` | finite-support abstraction / `defaultdict` |
| `total = zero; ... total += term` | owned finite sum/`linear_combination`; otherwise `sum(..., start=zero)` |
| `product = one; ... product *= factor` | owned `product`; numeric `math.prod(..., start=one)`; otherwise `reduce(mul, ..., one)` |
| nested `for a in A: for b in B:` producing all pairs | `itertools.product(A, B)` or owned Cartesian product |
| hand-built subsets/tuples of fixed size | `itertools.combinations` / `combinations_with_replacement` / `permutations` |
| manual first `n` values | `itertools.islice` |
| manual running partial sums/products | `itertools.accumulate` |
| `for x in xs: if not p(x): return False` | `all(p(x) for x in xs)` |
| `for x in xs: if p(x): return True` | `any(p(x) for x in xs)` |
| `for x in xs: if p(x): return x` | `next((x for x in xs if p(x)), default)` |
| manual count with `count += 1` | `sum(p(x) for x in xs)` / `Counter` |
| manual min/max tracking | `min` / `max(..., key=...)` |
| `for x in xs: yield x` | `yield from xs` |
| `for x in xs: yield f(x)` | generator expression / `map(f, xs)` |
| `for i in range(len(xs))` only to pair position/value | `enumerate(xs)` |
| indexing two equal-length collections in parallel | `zip(left, right, strict=True)` |
| repeated `labels.index(x)` inside a loop | owned `rank(x)` or one precomputed rank map |
| list used as FIFO frontier | `collections.deque` |
| hand-built orbit closure | owned action/G-set `.orbit(...)` or GAP/Sage backend |
| hand-built connected components/reachability | Sage/networkx graph API |
| hand-built multiplicity map | `Counter` / owned multiset |
| hand-built ordered deduplication | owned ordered set; private `dict.fromkeys` when appropriate |
| `try/except` in mathematical code | remove exception-driven control flow; assert the mathematical hypotheses and call code that is total under them; catch/translate failures only in engineering adapters |
| `x = f(...); return x` | `return f(...)` unless `x` names a mathematical intermediate |
| `if p: return True; return False` | `return p` |
| whole method is `assert False` / immediate failure | Sage `@abstract_method` for a genuine abstract contract, or correct mathematical placement; an assertion fallback is valid only after real implemented computational cases |
| `assert mathematical_hypothesis` | normally **keep or add it**: assertions loudly state the proof context; move the method only when the operation itself belongs to a narrower mathematical category |
| `hasattr/getattr/isinstance` to discover owned structure | category/method placement; private engine dispatch only at backend boundary |
| module-global `*_CACHE = {}` for canonical objects | shared memoization / `UniqueRepresentation` / `cached_function` |
| repeated `foo = OtherClass.foo` | common superclass/category implementation/delegation |
| repeated cross-engine convert→compute→convert stages | one adapter crossing around the complete engine computation |
| `f.matrix()` followed by nullspace/kernel rows and reconstructed submodule | `f.kernel()`; improve the Hom kernel implementation if necessary |
| structural predicate implemented by determinant/rank/gcd/minors | spell the categorical/module-theoretic definition; hide the numerical criterion underneath it |
| downstream code branches finite/infinite then performs coordinates | semantic owner routes representation cases; caller stays representation-oblivious |
| local `_..._from_matrix/_rows/_coordinates` helper recreates a standard construction | add/fix the kernel/image/pullback/cokernel/quotient/block-Hom/etc. API |
| same numerical workaround appears in a second consumer | treat it as missing semantic API and factor it immediately |
| subobject equality ignores its inclusion morphism | equality in the owned subobject/slice construction; the mono is part of the data |
| quotient equality ignores its projection | equality in the owned quotient/coslice construction; the epi is part of the data |
| normal form mutates/replaces chosen presentation | return a new represented object together with the isomorphism from the source |
| kernel/cokernel/product/etc. returned without canonical arrows | return/attach inclusion, projection, injections/projections, or other universal structure maps |
| test of isomorphism/isometry/genus uses equal objects | use distinct objects/presentations related by the weaker relation |
| `provider`/`manager`/`evidence`/`context` object in math layer | identify the actual morphism/functor/family/choice/standard mathematical datum |
| review finding is patched by moving code to a helper/registry | identify and repair the architectural generator/owner; migrate consumers |
| functor accepts `C` but rejects every non-isomorphism | declare the domain `C.core()` (or the actual slice/coslice/subcategory) |
| parameter redefines a canonical mathematical notion | derive it from existing structural data; use a new name only for genuinely different mathematics |
| deep specialized file computes generic set/Hom/quotient/product semantics | stop local patching and audit the general owner |
| universal construction gains arrows by product/matrix analogy | write the universal diagram and expose only the canonical maps it actually supplies |
| public `*args` / `**kwargs` forwards backend options | replace by closed named mathematical signatures; keep option forwarding private to adapters |
| `None` sentinel changes object/witness/return shape | split operations or accept the actual mathematical datum; only canonical defaults may be omitted |
| boolean mode flag changes mathematical result | named operations/constructors or precise literal overload at a compatibility boundary |
| `not is_X()` where the complementary mathematical property has a standard name | expose the positive predicate; preserve three-valued semantics where relevant |
| one-line `same_*` / per-element action wrapper hides value/morphism object | expose the composable value/morphism/Hom identity directly |
| supplied generators are returned as `O(L)` / `Aut(X)` | canonical group object plus `.subgroup(gens)`; completeness is a separate theorem |
| `Random*` / `Example*` / `Test*` type/category | process generates defining data for the ordinary constructor; named specimens go in catalogues |
| negative/absence test passes if object/result is empty/dead | prove a positive live surface/completeness witness first; prefer the positive universal property |
| easy determinant/count/fingerprint used to prove stronger claim | definition, cited complete invariant, or explicit witness |
| algorithm must exhaust `G`, `M`, `L`, etc. | structural/generator/presentation/theorem-backed check; explicit lazy enumeration only when enumeration is the operation |
| public name contains `partial`/`fast`/`cached`/engine name | use the stable mathematical noun/verb; put algorithm routing in implementation |
| “tensor product of matrices” | Kronecker product of matrices; tensor product belongs to represented maps/modules |
| `dot_product`/Euclidean norm/projection on arbitrary formed object | use the object's declared form/correlation; Euclidean algorithms only under the correct refinement |
| definite/nondegenerate restriction comes only from backend routine | keep general semantic domain; localize current algorithm case beneath it |
| owned upstream defect gets local Protocol/wrapper workaround | repair the authoritative source as part of the dependent task |
| long-lived stored backend twin drives ordinary math | prefer ephemeral construct-compute-convert-discard; durable backend state has one private owner |
| Sage `super_categories()` edge copied as “is-a” | classify actual structural functor first; Sage graph is runtime evidence only |
| Sage category equality/identical parents treated as mathematical equivalence | compare owned normalized constructions/functors |
| runtime bundled type/presentation called the category | separate category, object, runtime type, chosen presentation, property refinement |
| exact upstream class/name not found | compose standard mathematics from existing constructions before declaring a gap |
| mature dependency rejected mainly for package/build weight | compare owned LOC/reasoning, future blast radius, and reuse instead |
| local helper appears before checking Sage/stdlib/upstream idiom | inspect/probe the host first; use native capability behind owned semantics |
| scanner finding “fixed” only by syntax/suppression | diagnose against policy and repair the structural generator |
| generated certificate/status ledger mirrors live category/code facts | encode invariant structurally; live tests/on-demand report; no stored second ledger |
| category constructibility proved by graph BFS/name presence | derive the required canonical structural maps/category expression |
| repeated compliance checks grow around same violation | strengthen type/category/constructor/API so violation is structurally exposed |
| upstream tether shows duplicate general operation but local alias is preserved | delete/resite the local declaration; alignment can expose a defect |
| `pass` in mathematical implementation | implement/delete; genuine contract uses Sage `@abstract_method` + `...` |
| exact predicate returns `False`/`Unknown` because algorithm is missing | assertion-gate the computational frontier; reserve `Unknown` for explicitly soft knowledge predicates |
| `list(...)` / `tuple(...)` only to iterate | keep owned collection/generator lazy |
| multiple eager map/filter stages | generator/`map`/`filter` pipeline |
| raw `while` used only for ordinary iteration | `for`/iterator construct; retain `while` only for genuine evolving state |

### API and ownership patterns

#### `STY-01`: Global operation function -> method on the mathematical owner

**Bad:**

```python
Product(X, Y)
Kernel(f)
Orbit(G, x)
BaseChange(M, S)
```

**Preferred:**

```python
C.product([X, Y])
f.kernel()
G.orbit(x)
M.base_change(S)
```

The receiver supplies domain information and makes the operation discoverable by `<TAB>`.  A public global helper is not justified merely because it can dispatch correctly.

#### `STY-02`: Global dispatcher -> category/Hom/parent method dispatch

**Bad:**

```python
def Product(X, Y):
    if X in Modules(R) and Y in Modules(R):
        return module_product(X, Y)
    if X in Sets() and Y in Sets():
        return set_product(X, Y)
    if X in Schemes(S) and Y in Schemes(S):
        return scheme_product(X, Y)
```

**Preferred:**

```python
C = X.ambient_category()
return C.product([X, Y])
```

and each category subtree defines its own `product` implementation.  The global switchboard is usually a consequence of putting the operation on no mathematical owner.

#### `STY-03`: Ancestor imports descendant -> descendant imports/refines ancestor

**Bad:**

```python
# Cat/products.py
from ...lattices.my_special_lattices import MySpecialLattices
```

**Preferred:**

```python
# lattices/my_special_lattices.py
from ...abstract_categories.products import ProductsOfCategory

class MySpecialLattices(...):
    ...
```

A new specialized subtree should normally be addable without semantic edits to its ancestors or unrelated siblings.  Upward knowledge is a code smell even when not categorically forbidden.

#### `STY-04`: Export convenience operation -> keep global namespace sparse

**Bad:**

```python
# preamble/all.py
from .foo import Product, Kernel, Cokernel, Orbit, Stabilizer, BaseChange
```

**Preferred:** expose constructors/objects/categories globally and discover operations from the object already in hand:

```python
C = Modules(R)
C.<TAB>
f.<TAB>
G.<TAB>
```

A session namespace should not become a catalogue of every verb in the system.

#### `STY-05`: Runtime capability probing -> category-owned operation

**Bad:**

```python
if hasattr(M, "presentation_matrix"):
    return algorithm(M)
```

or:

```python
try:
    presentation = M.presentation_matrix()
except AttributeError:
    ...
```

**Preferred:** put the operation on the category that supplies the hypothesis:

```python
class ModulesWithChosenFinitePresentation(...):
    class ObjectType:
        def operation(self):
            ...
```

If a caller genuinely must branch, branch on owned mathematical category membership, not Python method presence.

#### `STY-06`: Manual sibling-method grafting -> common implementation/inheritance/category mixin

**Bad:**

```python
class GroupModuleHomset(...):
    base_ring = ModuleHomset.base_ring
    scalar_multiple = ModuleHomset.scalar_multiple
    elementwise = ModuleHomset.elementwise
    zero = ModuleHomset.zero
```

**Preferred:**

```python
class GroupModuleHomset(ModuleHomset, ...):
    ...
```

or move the shared API to the common Hom/category abstraction.  Assigning methods one-by-one is manual inheritance.

#### `STY-07`: Hidden source/provenance attributes -> explicit chosen-image/witness object

**Bad:**

```python
image._preamble_scalar_extension_source_module = M
...
M = image._preamble_scalar_extension_source_module
```

**Preferred:**

```python
selected_image = F.Image(M)
M = selected_image.preimage()
image = selected_image.image_object()
```

If later mathematics requires a chosen source, presentation, decomposition, or witness, that datum is part of the mathematical object model.

#### `STY-08`: Import-order-dependent refinement -> stable dependency DAG

**Bad:**

```python
try:
    from .modules import Modules
except ImportError:
    return R   # try again on a later lookup
```

**Preferred:** reorganize dependencies so the canonical structure is available deterministically from the defining object/category.  Function-local imports are for optional/heavy implementation dependencies, not a general cycle-breaking architecture.

### Collection construction patterns

#### `STY-09`: `append(f(x))` loop -> list comprehension or lazy image

**Bad:**

```python
images = []
for x in xs:
    images.append(f(x))
```

**Preferred:**

```python
images = [f(x) for x in xs]
```

or, when materialization is unnecessary:

```python
images = (f(x) for x in xs)
```

If this is a mathematical image/family, use the owned image/indexed-family construction instead of a Python list.

#### `STY-10`: Conditional `append` loop -> filtered comprehension/generator

**Bad:**

```python
compatible = []
for candidate in candidates:
    if agrees(candidate):
        compatible.append(candidate)
```

**Preferred:**

```python
compatible = [candidate for candidate in candidates if agrees(candidate)]
```

or lazily:

```python
compatible = (candidate for candidate in candidates if agrees(candidate))
```

#### `STY-11`: Dict assignment loop -> dictionary comprehension

**Bad:**

```python
images = {}
for label in labels:
    images[label] = f(label)
```

**Preferred:**

```python
images = {label: f(label) for label in labels}
```

This applies only when the loop is a direct map.  Multi-step coefficient accumulation may instead belong to a finite-support or linear-combination abstraction.

#### `STY-12`: Set `add` loop -> set comprehension/constructor

**Bad:**

```python
category_types = set()
for category in categories:
    category_types.add(type(category))
```

**Preferred:**

```python
category_types = {type(category) for category in categories}
```

or simply `set(values)` when no transformation occurs.

#### `STY-13`: Two disjoint dict-building loops -> dict union/comprehensions

**Bad:**

```python
images = {}
for label in left_labels:
    images[("left", label)] = left_map(label)
for label in right_labels:
    images[("right", label)] = right_map(label)
```

**Preferred:**

```python
images = {
    **{("left", label): left_map(label) for label in left_labels},
    **{("right", label): right_map(label) for label in right_labels},
}
```

or Python 3.9+ dictionary union:

```python
images = left_images | right_images
```

If the keys are mathematically tagged coproduct labels, prefer the owned coproduct/family construction.

#### `STY-14`: `extend` flattening loop -> `itertools.chain.from_iterable`

**Bad:**

```python
flat = []
for block in blocks:
    flat.extend(block)
```

**Preferred:**

```python
from itertools import chain
flat = chain.from_iterable(blocks)
```

Materialize with `list(...)` only at an explicitly finite private boundary that requires a Python sequence.

#### `STY-15`: `sum(rows, [])` flattening -> `chain.from_iterable`

**Bad:**

```python
entries = sum(rows, [])
```

This is quadratic for lists and hides flattening as addition.

**Preferred:**

```python
entries = chain.from_iterable(rows)
```

or a nested comprehension when a concrete private array is actually needed:

```python
entries = [entry for row in rows for entry in row]
```

#### `STY-16`: Nested Cartesian loops -> `itertools.product`

**Bad:**

```python
for a in A:
    for b in B:
        use(a, b)
```

**Preferred:**

```python
from itertools import product
for a, b in product(A, B):
    use(a, b)
```

If `A × B` is itself mathematical data used downstream, use the owned Cartesian-product object rather than `itertools.product`.

#### `STY-17`: Hand-built combinations/permutations -> `itertools`

**Bad:** recursive/index code whose only purpose is to enumerate subsets, fixed-size subsets, tuples, or permutations.

**Preferred:**

```python
from itertools import combinations, combinations_with_replacement, permutations
```

For mathematical finite/infinite combinatorial families, wrap or implement the corresponding owned enumerated set rather than leaking raw tuples as the public object.

#### `STY-18`: Slice-by-loop -> `itertools.islice`

**Bad:**

```python
result = []
for i, x in enumerate(xs):
    if i == n:
        break
    result.append(x)
```

**Preferred:**

```python
from itertools import islice
result = islice(xs, n)
```

Again, materialize only if the consumer actually needs a concrete finite sequence.

#### `STY-19`: Forwarding generator loop -> `yield from`

**Bad:**

```python
def values():
    for value in source:
        yield value
```

**Preferred:**

```python
def values():
    yield from source
```

If there is only a transformation, consider returning a generator expression directly.

#### `STY-20`: Consecutive-pair index arithmetic -> `itertools.pairwise`

**Bad:**

```python
for i in range(len(values) - 1):
    compare(values[i], values[i + 1])
```

**Preferred:**

```python
from itertools import pairwise
for left, right in pairwise(values):
    compare(left, right)
```

This is private finite-sequence syntax; mathematical ordered sets should expose their own adjacency/successor structure where appropriate.

#### `STY-21`: Running prefix accumulation -> `itertools.accumulate`

**Bad:**

```python
total = zero
prefixes = []
for value in values:
    total += value
    prefixes.append(total)
```

**Preferred:**

```python
from itertools import accumulate
prefixes = accumulate(values, initial=zero)
```

Use the mathematical additive operation when Python `+` is not the owned operation.

### Predicate/search patterns

#### `STY-22`: Boolean scan -> `all`

**Bad:**

```python
for x in xs:
    if not predicate(x):
        return False
return True
```

**Preferred:**

```python
return all(predicate(x) for x in xs)
```

#### `STY-23`: Existence scan -> `any`

**Bad:**

```python
for x in xs:
    if predicate(x):
        return True
return False
```

**Preferred:**

```python
return any(predicate(x) for x in xs)
```

#### `STY-24`: Find first matching element -> `next`

**Bad:**

```python
answer = None
for x in xs:
    if predicate(x):
        answer = x
        break
return answer
```

**Preferred:**

```python
return next((x for x in xs if predicate(x)), None)
```

If absence is exceptional, omit the default and let `StopIteration` be converted at the appropriate API boundary.

#### `STY-25`: Count matching elements -> `sum`

**Bad:**

```python
count = 0
for x in xs:
    if predicate(x):
        count += 1
```

**Preferred:**

```python
count = sum(predicate(x) for x in xs)
```

For mathematical cardinality, do not enumerate merely to count; ask the owned set/family for its cardinality.

#### `STY-26`: Manual minimum/maximum tracking -> `min`/`max` with `key=`

**Bad:**

```python
best = None
for candidate in candidates:
    if best is None or score(candidate) < score(best):
        best = candidate
```

**Preferred:**

```python
best = min(candidates, key=score)
```

Use `default=` when the empty case is meaningful and Python's API supports it.

#### `STY-27`: `if condition: return True; return False` -> return the predicate

**Bad:**

```python
if condition:
    return True
return False
```

**Preferred:**

```python
return condition
```

Negate directly when needed: `return not condition`.

### Folding and algebraic accumulation patterns

#### `STY-28`: Additive accumulator -> owned sum/linear combination or `sum`

**Bad:**

```python
total = target.zero()
for label, coefficient in coefficients.items():
    total += target.scalar_multiple(coefficient, basis[label])
return total
```

**Preferred:**

```python
return target.linear_combination(coefficients)
```

If this is plain private Python arithmetic:

```python
return sum(terms, start=zero)
```

A manual accumulator should not reimplement a parent/category operation.

#### `STY-29`: Multiplicative accumulator -> owned product or `reduce`

**Bad:**

```python
result = target.one()
for factor in factors:
    result *= factor
return result
```

**Preferred:**

```python
return target.product(factors)
```

At a plain Python/backend boundary:

```python
from functools import reduce
from operator import mul
return reduce(mul, factors, target.one())
```

#### `STY-30`: Nested bilinear sum -> `sum`/linear-combination abstraction

**Bad:**

```python
total = W.zero()
for i, a in left_coefficients.items():
    for j, b in right_coefficients.items():
        total += a * b * gram(i, j)
return total
```

**Preferred:**

```python
return sum(
    (a * b * gram(i, j)
     for i, a in left_coefficients.items()
     for j, b in right_coefficients.items()),
    W.zero(),
)
```

Better still, when this is evaluation of a represented pairing, call the pairing/Hom object rather than reimplementing coordinate evaluation.

#### `STY-31`: Useless identity-update loop -> delete it

**Bad:**

```python
for label in right.support():
    if left.multiplicity(label) == 0:
        coefficient *= 1
```

**Preferred:** delete the loop.  LLM-generated code often contains semantically inert bookkeeping left over from a more complicated derivation; simplify algebraically before preserving control flow.

### Grouping/counting/mapping patterns

#### `STY-32`: `setdefault(..., []).append(...)` -> `defaultdict(list)`

**Bad:**

```python
grouped = {}
for key, value in pairs:
    grouped.setdefault(key, []).append(value)
```

**Preferred:**

```python
from collections import defaultdict

grouped = defaultdict(list)
for key, value in pairs:
    grouped[key].append(value)
```

If input is already sorted by key and streaming behavior matters, consider `itertools.groupby`.

#### `STY-33`: Manual multiplicity dictionary -> `Counter`

**Bad:**

```python
counts = {}
for label in labels:
    counts[label] = counts.get(label, 0) + 1
```

**Preferred:**

```python
from collections import Counter
counts = Counter(labels)
```

If multiplicity is mathematical structure, prefer the owned multiset/fixed-size-selection object.

#### `STY-34`: Manual default-valued accumulation -> `defaultdict`

**Bad:**

```python
coefficients = {}
for label, value in terms:
    coefficients[label] = coefficients.get(label, zero) + value
```

**Preferred:**

```python
from collections import defaultdict
coefficients = defaultdict(lambda: zero)
for label, value in terms:
    coefficients[label] += value
```

Better still, use the parent's finite-support or `linear_combination` machinery if these are mathematical coefficients.

#### `STY-35`: Manual ordered deduplication -> owned ordered set or `dict.fromkeys` privately

**Bad:**

```python
result = []
for x in xs:
    if x not in result:
        result.append(x)
```

**Preferred mathematical form:** construct the owned ordered set.

For private hashable Python data where first-occurrence order is merely serialization order:

```python
result = list(dict.fromkeys(xs))
```

Do not use a Python sequence as the public representation of a mathematical set.

### Indexing and parallel-iteration patterns

#### `STY-36`: Parallel indexing -> `zip(..., strict=True)`

**Bad:**

```python
for i in range(len(labels)):
    use(labels[i], coefficients[i])
```

**Preferred:**

```python
for label, coefficient in zip(labels, coefficients, strict=True):
    use(label, coefficient)
```

If the two families are mathematically indexed by the same set, prefer that common index set directly instead of positional Python synchronization.

#### `STY-37`: Position counter -> `enumerate`

**Bad:**

```python
i = 0
for value in values:
    use(i, value)
    i += 1
```

**Preferred:**

```python
for i, value in enumerate(values):
    use(i, value)
```

Again, if `i` is mathematically a label rather than incidental Python position, use the owned rank/unrank/index set.

#### `STY-38`: Repeated full index lookup -> precomputed mathematical rank map / owned rank

**Bad:**

```python
for label in labels:
    position = labels_list.index(label)
```

**Preferred:** use the owned ordered set's `rank(label)`, or construct a private `{label: position}` mapping once when crossing into a backend that requires dense positions.

Do not force an infinite or abstract framing into a list merely to gain `.index`.

### Stateful traversal patterns

#### `STY-39`: FIFO worklist -> `collections.deque`

**Bad:**

```python
frontier = [seed]
while frontier:
    x = frontier.pop(0)
    ...
    frontier.append(y)
```

**Preferred:**

```python
from collections import deque
frontier = deque([seed])
while frontier:
    x = frontier.popleft()
    ...
```

#### `STY-40`: Bespoke orbit closure -> action/G-set `orbit`

**Bad:**

```python
seen = {seed}
frontier = deque([seed])
while frontier:
    point = frontier.popleft()
    for g in group_generators:
        image = act(g, point)
        if image not in seen:
            seen.add(image)
            frontier.append(image)
```

**Preferred:**

```python
return action.orbit(seed)
```

or the corresponding GAP/Sage group-action routine behind the owned action API.  If a generic orbit algorithm is missing, implement it once on the G-set/action abstraction.

#### `STY-41`: Bespoke connected-components/reachability -> graph library

**Bad:** local DFS/BFS code whose mathematical input is already a graph.

**Preferred:** use the owned graph object, Sage graph API, or `networkx` operation such as connected components, shortest paths, transitive closure, topological sorting, etc.  Do not maintain generic graph algorithms in a mathematical theory module.

#### `STY-42`: Bespoke group stabilizer/orbit algorithm -> GAP/Sage group backend through owned API

**Bad:** enumerate group action manually to recover an orbit or stabilizer when GAP/Sage already implements it.

**Preferred:**

```python
orbit = G.orbit(x)
stabilizer = G.stabilizer(x)
```

with the implementation delegated through the private group backend.  The preamble owns the mathematical object; GAP owns the generic finite-group algorithm.

#### `STY-43`: Genuine fixed-point/search algorithm -> keep explicit loop

Not every `while` should disappear.

**Appropriate:**

```python
changed = True
while changed:
    changed = False
    ...  # one mathematically meaningful closure step
```

when the fixed-point iteration itself is the algorithm and no standard library/upstream routine already owns it.  Use explicit names for state and invariants; do not contort such code into nested `reduce`/lambda expressions.

### Control-flow cleanup patterns

#### `STY-44`: `try`/`except` in mathematical code -> asserted hypotheses and total code

Exception-driven control flow is an engineering pattern, not a mathematical one.  In mathematical code, state the assumptions that make the next construction valid, assert them, and then execute code that is total under those assumptions.

**Bad mathematical code:**

```python
try:
    return optional_construction(X)
except (TypeError, ValueError, AttributeError):
    return fallback(X)
```

**Preferred:**

```python
assert X in CategoryWhereCurrentAlgorithmIsTotal(), (
    "the current implementation assumes ..."
)
return construction(X)
```

If the construction is mathematically defined only on that narrower category, move the method there instead.  `try`/`except` and `contextlib.suppress` remain legitimate inside engineering kernels—backend adapters, parsers, filesystem/network/process interfaces—where the failure is an external protocol event rather than part of the mathematics.

#### `STY-45`: Temporary immediately returned -> direct return

**Bad:**

```python
result = normalize(value)
return result
```

**Preferred:**

```python
return normalize(value)
```

Keep the temporary when its name records a real mathematical intermediate or materially improves readability/debugging.

#### `STY-46`: Nested guard-only `if` -> combined condition

**Bad:**

```python
if x in C:
    if predicate(x):
        return f(x)
```

**Preferred:**

```python
if x in C and predicate(x):
    return f(x)
```

Do not combine conditions when the inner branch represents a distinct mathematical case worth naming.

#### `STY-47`: `if/else` assignment -> conditional expression when both branches are expressions

**Bad:**

```python
if index >= 0:
    name = f"x_{index}"
else:
    name = f"x_m{-index}"
```

**Preferred:**

```python
name = f"x_{index}" if index >= 0 else f"x_m{-index}"
```

#### `STY-48`: Whole-method failure stub -> real implementation cases, `@abstract_method`, or correct placement

A visible mathematical method may legitimately fail on *currently uncomputable instances* of a mathematically meaningful notion. What is forbidden is advertising a method whose implementation contains no successful mathematical case at all.

**Bad deceitful stub:**

```python
def tensor_shape(self):
    assert False, "a tensor supplies the ranks of its indices"
```

or:

```python
def kernel(self):
    raise NotImplementedError
```

These methods expose a name under tab completion but implement no mathematics.

**Preferred for a genuine abstract implementation contract:**

```python
from sage.misc.abstract_method import abstract_method

@abstract_method
def tensor_shape(self):
    ...
```

**Preferred when the notion is only mathematically defined on a narrower category:** put/mix the method only on that category.

**Preferred when the notion is mathematically general but only some cases are currently computable:** keep the method at the mathematically correct owner and implement those cases, with an informative assertion only for the unhandled remainder. A final `assert False, ...` is acceptable *after real implemented cases* as an exhaustiveness/computability fallback; it is not acceptable as the whole implementation.

#### `STY-49`: Mathematical and algorithmic hypotheses -> assert them loudly

Assertions are executable mathematical commentary. Use them liberally to state category membership, finiteness, nondegeneracy, compatibility, shape, parentage, and identities on which the following derivation relies.

**Good proof-context assertions:**

```python
assert lattice in Lattices(R)
assert f.domain() is M
assert result in TargetCategory()
```

**Good algorithm-domain assertion:**

```python
def is_nondegenerate(self):
    assert self in FiniteRankFormedModules(R), (
        "nondegeneracy is currently decidable here only for finite-rank formed modules"
    )
    return self.gram_tensor().determinant() != 0
```

The method remains on the category where nondegeneracy is mathematically meaningful; the assertion states only the narrower domain of the current algorithm.

Do **not** replace these statements by exception-valued mathematical branches. The assertion records the proof/computability context and should fail loudly at the first unmet assumption.

### Representation and DRY patterns

#### `STY-50`: Parallel representation of a canonical object -> reuse the canonical construction

**Bad:** maintain a tensor-based matrix object with its own determinant/rank/kernel API while `M_{m,n}(R)` is already `Hom_R(F_R([n]), F_R([m]))`.

**Preferred:** the matrix is the Hom element.  Put matrix operations on the appropriate Hom/category refinement and delete the parallel representation.

#### `STY-51`: Equivalent universal data implemented independently -> derive one from the other

**Bad:** every adjunction subclass independently implements:

```python
unit(...)
counit(...)
hom_set_isomorphism_forward(...)
hom_set_isomorphism_inverse(...)
```

**Preferred:** choose one authoritative presentation, e.g. unit+counit, and derive the transpose maps generically:

```python
Phi(f) = U(f) * eta_A
Phi_inverse(g) = epsilon_B * F(g)
```

Do not spend hundreds of lines maintaining mathematically forced coherence by hand.

#### `STY-52`: Duplicate additive object implementation -> reuse/refine the existing additive construction

**Bad:** implement a second class with its own normalization, homogeneous components, addition, negation, scalar multiplication, equality, and display when it is already a graded direct sum with extra multiplication.

**Preferred:** use the existing graded-direct-sum parent/element as the additive/module object and refine/equip it with the additional algebra structure.

#### `STY-53`: Repeated parameterized-category boilerplate -> common parameterized base

**Bad:** several categories each repeat:

```python
@staticmethod
def __classcall_private__(cls, base_ring, group): ...
def __init__(self, base_ring, group): ...
def base_ring(self): ...
def acting_group(self): ...
```

**Preferred:** factor the common `(R, G)`-parameterized category abstraction once and derive `GroupModules`, `GroupLattices`, chosen-finite variants, etc. from it.

#### `STY-54`: Same algorithm in method and functor -> one canonical operation, functor delegates

**Bad:** `M.base_change(S)` and `ScalarExtensionFunctor._apply_object(M)` independently rebuild the same transported action/presentation.

**Preferred:** one is authoritative:

```python
class ScalarExtensionFunctor(...):
    def _apply_object(self, M):
        return M.base_change(self.target_ring())
```

or conversely the object method delegates to the functor if the functor is the mathematical owner.  There must be one implementation.

#### `STY-55`: Theory-local identity cache -> shared memoization/`UniqueRepresentation`

**Bad:**

```python
_MODULE_TENSOR_PRODUCT_CACHE = {}
_POWER_CACHE = {}
_FORM_SPACE_CACHE = {}
```

with custom `id(...)` keys and stale-entry checks in each file.

**Preferred:** `cached_function`, `cached_method`, `UniqueRepresentation`, or one shared identity-sensitive memoization helper with explicit lifetime semantics.

#### `STY-56`: Hand-written generic utility already in stdlib/dependency -> import it

**Bad:** local implementations of graph traversal, topological sort, union-find, memoization, flattening, pairwise traversal, combinations, queues, grouping, or multidispatch.

**Preferred:** use `itertools`, `collections`, `functools`, Sage/networkx, GAP, OSCAR/Singular, or another mature dependency.  Adding a dependency is preferable when it deletes substantial generic machinery and has a better semantic fit.

### Backend and boundary patterns

#### `STY-57`: Cross-backend ping-pong -> one crossing around the complete computation

**Bad:**

```python
A_engine = to_engine(A)
B_engine = engine_step_one(A_engine)
B = from_engine(B_engine)
C_engine = to_engine(B)
D_engine = engine_step_two(C_engine)
return from_engine(D_engine)
```

**Preferred:**

```python
return from_engine(adapter.complete_algorithm(to_engine(A)))
```

When practical, implement the multi-stage routine natively in Singular/Julia/OSCAR/GAP/etc. and return only the final data needed to reconstruct the owned result.

#### `STY-58`: Backend workspace leaks into mathematical code -> private adapter owns it

**Bad:** several mathematical modules directly read `_engine`, construct engine matrices, and continue computation on engine elements.

**Preferred:** one private adapter converts owned inputs, computes, and crosses back.  Ordinary mathematical consumers never receive or manipulate backend parents/elements.

#### `STY-59`: Python loops serialize every intermediate backend object -> batch/native engine operation

**Bad:** repeatedly cross individual rows/elements in a Python loop when the backend accepts a matrix/family and can execute the whole reduction internally.

**Preferred:** serialize the finite input once, invoke one engine routine, deserialize the final result once.

### Laziness and mathematical collections

#### `STY-60`: Eager `list`/`tuple` just to iterate -> iterate the owned collection

**Bad:**

```python
labels = tuple(M.module_generating_set())
for label in labels:
    ...
```

**Preferred:**

```python
for label in M.module_generating_set():
    ...
```

Use `rank`/`unrank`, indexed families, or finite support when positional access is mathematically required.  Materialize only in a private backend serializer after finiteness and order are established.

#### `STY-61`: Eager intermediate list -> generator pipeline

**Bad:**

```python
rows = [transform(x) for x in xs]
nonzero = [row for row in rows if any(row)]
return backend(nonzero)
```

**Preferred:**

```python
rows = (transform(x) for x in xs)
return backend(row for row in rows if any(row))
```

provided the backend/consumer can stream.  Do not create Python containers that have no mathematical identity and exist only to feed the next expression.

#### `STY-62`: Enumerate to decide cardinality/finiteness -> use cardinality/category

**Bad:**

```python
items = list(S)
return len(items)
```

**Preferred:**

```python
return S.cardinality()
```

or dispatch from the appropriate finite/infinite category.  Enumeration is not a proof of finiteness and may be impossible for a perfectly valid infinite object.

### String/display and small-expression patterns

#### `STY-63`: Append strings then concatenate -> comprehension + `join`

**Bad:**

```python
terms = []
for label in support:
    terms.append(format_term(label))
return " + ".join(terms)
```

**Preferred:**

```python
return " + ".join(format_term(label) for label in support)
```

#### `STY-64`: Repeated membership normalization loop -> constructor/comprehension when semantics are simple

**Bad:**

```python
normalized = []
for x in xs:
    x = normalize(x)
    if x:
        normalized.append(x)
```

**Preferred:**

```python
normalized = [y for x in xs if (y := normalize(x))]
```

Use this only when the assignment expression improves clarity; otherwise use a small helper plus comprehension.  If normalization has multiple semantic branches or mathematical assertions, retain explicit code rather than obscuring those hypotheses inside an expression.

#### `STY-65`: Repeated `.get(key, zero) + value` -> finite-support abstraction or `defaultdict`

**Bad:**

```python
result[key] = result.get(key, zero) + value
```

repeated throughout an algorithm.

**Preferred:** use the object's finite-support coefficient type.  At a private Python layer:

```python
result = defaultdict(lambda: zero)
result[key] += value
```

#### `STY-66`: Empty mutable accumulator immediately followed by a loop -> classify before accepting

The shapes `result = []`, `result = {}`, and `result = set()` immediately before an iteration are **review triggers**.  They are not automatically wrong, but they very often mean Python is being used to spell map/filter/group/fold semantics manually.

**Red flags:**

```python
result = []
for x in xs:
    ...

result = {}
for x in xs:
    ...

result = set()
for x in xs:
    ...
```

Before keeping the loop, classify the mutation:

```text
append(f(x))                 -> comprehension / map / owned image
conditional append           -> filtered comprehension / filter
extend(f(x))                 -> chain.from_iterable
add(f(x))                    -> set comprehension / owned set
d[key] = f(x)                -> dict comprehension
d[key] += value              -> defaultdict / Counter / finite-support sum
acc += term                  -> sum / linear_combination / owned fold
acc *= factor                -> product / math.prod / reduce / owned fold
queue append + pop-left      -> deque or higher traversal API
```

If none of these describe the mutation because the evolving state is the algorithm, keep the explicit state machine.

#### `STY-67`: Raw `for x in xs` -> first test map/filter/fold/quantifier/traversal forms

Every new explicit `for` loop in ordinary transformation code is a review trigger.  First ask whether the body is one of the standard forms catalogued here.

**Bad default:**

```python
for x in xs:
    result.append(f(x))
```

**Preferred:**

```python
result = [f(x) for x in xs]
```

The same trigger applies to `for key, value in mapping.items()`, nested `for` loops, and loops over mathematical generating sets.  The explicit loop is appropriate when the iteration carries genuine mutable state, early multi-branch control flow, backtracking, a protocol, or another algorithm whose transitions are the point.

#### `STY-68`: Raw `while` -> require a genuine evolving-state invariant

A `while` loop should normally correspond to a stateful algorithm: fixed point, worklist search, backtracking, iterative refinement, parsing/protocol state, or backend iteration.

**Suspicious:**

```python
while i < len(xs):
    consume(xs[i])
    i += 1
```

**Preferred:**

```python
for x in xs:
    consume(x)
```

**Legitimate:**

```python
while frontier:
    state = frontier.popleft()
    ...
```

provided the search itself is not already owned by a graph/action/group abstraction or dependency.

#### `STY-69`: `.append(...)` inside a loop -> comprehension, filter, or owned image

Treat `.append(...)` inside an ordinary `for` loop as a specific red flag.

**Bad:**

```python
rows = []
for relation in relations:
    rows.append(transform(relation))
```

**Preferred:**

```python
rows = [transform(relation) for relation in relations]
```

If the result is consumed once, prefer the lazy form:

```python
rows = (transform(relation) for relation in relations)
```

If the values form a mathematical image/family/set, construct that owned object instead of a Python list.

#### `STY-70`: `.extend(...)` inside a loop -> `chain` / `chain.from_iterable`

**Bad:**

```python
flat = []
for block in blocks:
    flat.extend(block)
```

**Preferred:**

```python
from itertools import chain
flat = chain.from_iterable(blocks)
```

For a fixed small number of iterables:

```python
flat = chain(left, middle, right)
```

Materialize with `list(...)` only at a private finite serialization boundary.

#### `STY-71`: `.add(...)` inside a loop -> set comprehension / set constructor

**Bad:**

```python
seen_types = set()
for C in categories:
    seen_types.add(type(C))
```

**Preferred:**

```python
seen_types = {type(C) for C in categories}
```

If the set is mathematical, use the owned set construction rather than Python `set`.

#### `STY-72`: `result[key] = expression` in a simple loop -> dict comprehension

**Bad:**

```python
images = {}
for label in labels:
    images[label] = f(label)
```

**Preferred:**

```python
images = {label: f(label) for label in labels}
```

If each key is assigned more than once, this is no longer a simple dict-construction pattern; use the grouping/accumulation rules instead.

#### `STY-73`: `acc += term` inside a loop -> sum/fold/owned additive operation

**Bad:**

```python
total = zero
for term in terms:
    total += term
```

**Preferred for ordinary additive values:**

```python
return sum(terms, start=zero)
```

**Preferred for module coefficients:**

```python
return M.linear_combination(coefficients)
```

Do not force Python `sum` when the mathematical parent has a more informative finite-sum or linear-combination operation.

#### `STY-74`: `acc *= factor` inside a loop -> owned product, `math.prod`, or `reduce`

**Bad:**

```python
product = one
for factor in factors:
    product *= factor
```

**Preferred when the mathematical parent owns the product:**

```python
return parent.product(factors)
```

**Preferred for ordinary numeric scalars:**

```python
from math import prod
return prod(factors, start=one)
```

**Preferred for arbitrary Python objects with associative multiplication but no owner fold:**

```python
from functools import reduce
from operator import mul
return reduce(mul, factors, one)
```

Use `math.prod` rather than `reduce(mul, ...)` for ordinary numbers.  Use the owned mathematical product rather than either Python form when it exists.

#### `STY-75`: `.get(key, zero) + value` / repeated coefficient mutation -> finite-support abstraction first

**Bad:**

```python
coefficients = {}
for key, value in terms:
    coefficients[key] = coefficients.get(key, zero) + value
```

**Preferred mathematical form:** use the repository's finite-support/linear-combination object.

**Private Python fallback:**

```python
from collections import defaultdict
coefficients = defaultdict(lambda: zero)
for key, value in terms:
    coefficients[key] += value
```

For integer multiplicities, use `Counter` instead.

#### `STY-76`: `setdefault(key, []).append(value)` -> `defaultdict(list)`

**Bad:**

```python
grouped = {}
for key, value in pairs:
    grouped.setdefault(key, []).append(value)
```

**Preferred:**

```python
from collections import defaultdict
grouped = defaultdict(list)
for key, value in pairs:
    grouped[key].append(value)
```

If the input is already sorted by the grouping key and streaming behavior is useful, consider `itertools.groupby` instead.

#### `STY-77`: Sorted streaming grouping -> `itertools.groupby`

**Bad:**

```python
# hand-maintain current_key/current_bucket while walking sorted records
```

**Preferred:**

```python
from itertools import groupby
for key, group in groupby(records, key=key_function):
    consume_group(key, group)
```

`groupby` groups adjacent equal keys; sort first only when sorting is mathematically/algorithmically appropriate.  For unsorted accumulation, `defaultdict` is usually the correct tool.

#### `STY-78`: Repeated integer counting -> `Counter` / `Counter.update`

**Bad:**

```python
counts = {}
for label in labels:
    counts[label] = counts.get(label, 0) + 1
```

**Preferred:**

```python
from collections import Counter
counts = Counter(labels)
```

For repeated batches:

```python
counts.update(more_labels)
```

Use an owned multiset when multiplicity is mathematical data in the public preamble.

#### `STY-79`: Named pure transformation -> `map`; named predicate -> `filter`

Use `map` and `filter` when they expose an already named operation directly; use comprehensions when the expression or condition is clearer inline.

**Verbose:**

```python
normalized = []
for x in xs:
    normalized.append(normalize(x))
```

**Concise:**

```python
normalized = map(normalize, xs)
```

**Verbose:**

```python
finite = []
for x in xs:
    if is_finite(x):
        finite.append(x)
```

**Concise:**

```python
finite = filter(is_finite, xs)
```

Do not wrap `list(...)` around these merely by habit; retain laziness unless a concrete sequence is actually required.

#### `STY-80`: Tuple-unpacking transformation -> `itertools.starmap` when clearer

**Bad:**

```python
values = (f(a, b) for a, b in pairs)
```

**Alternative when `f` is already named and the tuple-unpacking is the only syntax:**

```python
from itertools import starmap
values = starmap(f, pairs)
```

Prefer the generator expression when it is more readable.  The point is to recognize the standard higher-order iterator rather than build a helper loop.

#### `STY-81`: Fixed-size chunking loop -> `itertools.batched`

**Bad:**

```python
batch = []
for x in xs:
    batch.append(x)
    if len(batch) == n:
        yield tuple(batch)
        batch.clear()
```

**Preferred:**

```python
from itertools import batched
yield from batched(xs, n)
```

Use `strict=True` when an incomplete final batch is invalid.

#### `STY-82`: Repeated constant values -> `itertools.repeat`

**Bad:**

```python
values = (zero for _ in range(n))
```

**Preferred:**

```python
from itertools import repeat
values = repeat(zero, n)
```

Use this only for immutable values or when sharing the repeated object is intended.

#### `STY-83`: Manual running index paired with values -> `enumerate`; two streams -> strict `zip`

**Bad:**

```python
i = 0
for value in values:
    consume(i, value)
    i += 1
```

**Preferred:**

```python
for i, value in enumerate(values):
    consume(i, value)
```

For two logically equal-length streams:

```python
for left, right in zip(lefts, rights, strict=True):
    ...
```

Do not silently truncate mathematical data with plain `zip` when equal cardinality is part of the contract.

#### `STY-84`: Manual list concatenation with `+` in a loop -> `chain`; repeated string `+=` -> `join`

**Bad:**

```python
result = []
for block in blocks:
    result = result + block
```

**Preferred:**

```python
from itertools import chain
result = chain.from_iterable(blocks)
```

**Bad:**

```python
text = ""
for part in parts:
    text += part
```

**Preferred:**

```python
text = "".join(parts)
```

#### `STY-85`: Manual product/sum of a transformed family -> generator directly into the fold

Do not build a temporary list just to fold it.

**Bad:**

```python
terms = [weight(x) * value(x) for x in xs]
return sum(terms, start=zero)
```

**Preferred:**

```python
return sum((weight(x) * value(x) for x in xs), start=zero)
```

For ordinary numeric products:

```python
from math import prod
return prod((weight(x) for x in xs), start=one)
```

Again, an owned `linear_combination` or `product` outranks the Python fold when the family belongs to a mathematical parent.

#### `STY-86`: Multiple simple stages -> lazy generator pipeline, not repeated materialization

**Bad:**

```python
mapped = [normalize(x) for x in xs]
filtered = [x for x in mapped if valid(x)]
keys = [key(x) for x in filtered]
```

**Preferred:**

```python
mapped = map(normalize, xs)
filtered = filter(valid, mapped)
keys = map(key, filtered)
```

or a readable generator pipeline.  Materialize only the stage whose concrete sequence semantics are actually required.

#### `STY-87`: Collection-building loop with no mutation except construction -> assume a declarative replacement exists

The general red flag is:

```python
result = <empty collection>
for x in xs:
    result.<single construction mutation>(...)
return result
```

Before accepting it, prove that it is *not* one of:

- list/set/dict comprehension;
- `map` / `filter`;
- `chain` / `chain.from_iterable`;
- `defaultdict` / `Counter`;
- `sum` / `math.prod` / `reduce`;
- `any` / `all` / `next` / `min` / `max`;
- an owned set/image/family/linear-combination/product;
- a graph/action/group traversal already implemented elsewhere.

This is deliberately a review trigger because this exact “walk and accrue” pattern is heavily overproduced by generated code.

### Current live-tree exemplars behind the catalogue

The catalogue above is not hypothetical.  These are concrete patterns already observed in the current preamble; they serve as regression examples for future review.

| Current case | What is wrong | Preferred direction | Catalogue |
| --- | --- | --- | --- |
| `categories/abstract_categories/constructions.py`: global `Product`, `Coproduct`, `TensorProduct`, `Kernel`, `Cokernel` | Free-standing operations force callers to know a global language and force implementation to rediscover mathematical ownership | Put the construction on the category/Hom/morphism that owns it; notation delegates there | `STY-01`–`04` |
| `abstract_categories/arrow_categories.py::_morphisms_agree` | Root helper knows schemes, finite sets, groups, and modules to decide arrow equality | Homset/category owns extensional equality | `STY-02`, `05` |
| `tensors/tensor.py` determinant/rank/solve/kernel/trace/row/transpose/inverse methods | A type-(1,1) tensor is being used as a second matrix/linear-map representation | `M_{m,n}(R)=Hom_R(F_R([n]),F_R([m]))`; matrix operations live on that Hom refinement | `STY-50` |
| `categories/forms/forms.py` represented `PairingSpace`/`BilinearFormSpace` hierarchy | Parallel Hom-like representation remains after tensor products exist | Represented pairing is literally `Hom_R(X tensor Y, W)`; quadratic maps use the appropriate universal square where represented | `STY-50`–`52` |
| `functors/core.py::Adjunction` and its subclasses | Unit, counit, forward transpose, and inverse transpose are independently implemented despite determining each other | Choose one standard presentation and derive the rest by the adjunction formulas | `STY-51` |
| `ContravariantFunctor` / `Bifunctor` in `functors/core.py` | Reimplement ordinary functor cache/validation for structures already represented by opposite/product categories | Thin convenience interface over `Functor(C.op(),D)` / `Functor(C×D,E)` | `STY-51`, `54` |
| functor modules attaching `_preamble_*_source_*` attributes | Chosen preimages/provenance are hidden side channels | Explicit functor-image/chosen-preimage object, or derive maps from unit/counit | `STY-07` |
| `schemes.py` `_preamble_coordinate_algebra_morphism` and related attached structure | Affine-Spec contravariance/provenance is reconstructed by side-channel metadata | Actual `Spec` functor and scheme Hom whose pullback is intrinsic | `STY-07`, `17` |
| `rings.py::_refine_canonical_self_module_and_algebra` | Canonical structure can depend on import success and later lookups | Deterministic structure/category packet independent of import history | `STY-08` |
| pervasive `refine(...)` calls that mutate classes/state after construction | Runtime refinement can become a second history-dependent object system | Stable implementation/category structure; refinement only for genuinely established mathematical structure | `STY-08`, `18` |
| `PowerAlgebraElement` versus `GradedDirectSumElement` | Same additive/module implementation repeated in a richer object | Reuse the graded direct sum and add algebra multiplication/unit structure | `STY-52` |
| `GroupModules`, finite/free/presented group-module categories, `GroupLattices` | Same `(R,G)` canonicalization/storage/accessors repeated | Common parameterized category abstraction | `STY-53` |
| `GroupModuleHomset` / `GradedModuleHomset` assignments from `ModuleHomset` | Manual inheritance by method grafting | Common Hom implementation/category inheritance | `STY-06` |
| group-module `base_change` versus scalar-extension functor | Same action-transport algorithm implemented twice | One canonical base-change implementation; functor/object method delegates | `STY-54` |
| `_MODULE_TENSOR_PRODUCT_CACHE`, `_MODULE_POWER_CACHE`, form/Kähler/de Rham/etc. caches | Every theory invents identity/lifetime semantics | Shared identity memoization, `UniqueRepresentation`, `cached_function`/`cached_method` where correct | `STY-55` |
| Fourier/Hermite/Laurent/sinc enumerated-function parents | Same infinite indexed-parent implementation repeated | One indexed-symbol/indexed-function-set abstraction | `STY-52`, `56` |
| `_singular_presentation_kernel` | Python orchestrates a long multi-stage Singular workflow | Native/batched Singular routine behind one adapter crossing | `STY-57`–`59` |
| torsion-form orbit/stabilizer code | Specialized theory directly performs GAP orbit/stabilizer work despite owned action infrastructure | Action/G-set orbit/stabilizer API delegating privately to GAP | `STY-40`–`42`, `57`–`59` |
| `forms.py::_coordinate_values` nested `total += ...` | Hand-written finite bilinear sum | Pairing/Hom evaluation or declarative finite sum | `STY-28`, `30`, `73` |
| `sparse_free_algebras.py::_multiply_in_target` | `result=one; for factor: result *= factor` is pure fold boilerplate | Parent-owned product, otherwise `reduce`; `math.prod` for ordinary numbers | `STY-29`, `74` |
| `modules/powers.py::_divided_product_coefficient` | Manual product fold plus a second loop that only multiplies by `1` | Owned/numeric product fold; delete algebraically inert loop | `STY-29`, `31`, `74` |
| `lattices.py::decomposition_names` | `names=[]; ... names.extend(...)` flattening | Lazy owned family or `chain.from_iterable` at a private Python layer | `STY-14`, `60`, `70` |
| profinite embedding filters | `compatible=[]; for candidate: if all(...): append(candidate)` | filtered comprehension/generator or `filter` | `STY-10`, `22`, `69`, `79` |
| `schemes.py::refine_scheme` category-type accumulation | `set(); for ...: add(type(...))` | set comprehension, subject to broader refinement redesign | `STY-12`, `71` |
| multiple `setdefault(...).append(...)` / `.get(...)+...` coefficient/grouping sites | Repeated generic grouping/accumulation machinery | `defaultdict`, `Counter`, or owned finite-support object | `STY-32`–`34`, `65`, `75`–`78` |
| multiple frontier/seen loops in G-sets, orthogonal quotients, discriminant modules | Generic traversal/orbit machinery is repeatedly open-coded | owned action/G-set/graph operation or mature traversal dependency; explicit loop only if algorithm is genuinely special | `STY-39`–`43`, `68` |
| `assert False` stubs in tensor methods | A visible method is being used as a deceitful placeholder rather than a mathematical promise | Sage `@abstract_method` for a genuine abstract contract, or remove/move the method if it is not defined there | `STY-48` |
| finite-rank/nondegeneracy/category-containment assertions | These loudly record the proof context of an implementation | **Keep/add informative assertions**; move the method only when the operation itself belongs to a narrower mathematical category | `STY-49` |
| `preamble/utilities.py` helpers such as `lmap`/`lzip` have no backend callers | Internal-use grep does not measure a REPL/notebook preamble API | Preserve deliberate session conveniences and ensure they are actually exported/tested as session vocabulary | `STY-88` |

These examples are evidence for the general rules, not a finite whitelist.  When the same code shape appears elsewhere, apply the rule without waiting for that file to be named here.

#### `STY-88`: No internal callers does not imply dead code on a session surface

This repository is a research preamble.  Names may exist specifically so they are available interactively in notebooks and REPL sessions; such functions can correctly have zero call sites in `src/` and `tests/`.

**Bad review heuristic:**

```text
rg finds no internal calls to lmap/lzip -> delete them as dead code
```

**Preferred:** determine whether the name is deliberate session vocabulary.  If it is, ensure it is exported by `preamble.all`, has obvious stable semantics, and is exercised as part of the session surface.  Internal call graphs measure implementation reuse, not interactive usefulness.

Thin wrappers are therefore judged by **session ergonomics**, not by whether backend code calls them.  `lmap(f, xs)` and `lzip(xs, ys)` can be legitimate preamble conveniences precisely because their meanings are obvious and they save repetitive REPL typing.

#### `STY-89`: Method visibility follows mathematical definability, not current decidability

A method visible under tab completion says: **this notion is mathematically defined for this object**. It does *not* promise that the CAS can decide or compute it for every represented instance today.

Canonical example: a set such as

```python
X = {n in NN | n.is_twin_prime()}
```

unquestionably has a cardinality. Hiding `cardinality()` behind a fictional `SetsWithComputableCardinality` category would misstate the mathematics. A user may reasonably encounter an assertion explaining that the current algorithm does not cover this representation.

Likewise `is_nondegenerate()` belongs on formed modules/lattices where nondegeneracy is a defined property, even if an infinite-rank callable form is outside today's decision procedures.

The long-term goal is **hope matches reality**: every mathematically natural method is visible where it belongs, common cases compute correctly, unsupported computational cases fail immediately and informatively, and the implemented case family expands over time.

Never use `NotImplementedError` as the fallback. Never expose a method whose only behavior is failure.

#### `STY-90`: Computability routing may use explicit mathematical case tables

Most switchboards that rediscover category ownership are architectural smells. Computational routing *within an already correctly owned mathematical method* is different and often desirable.

**Good shape:**

```python
def cardinality(self):
    match self:
        case FiniteEnumeratedSet():
            return NN(self._known_size())
        case IntervalIntersectionSet():
            return self._interval_cardinality()
        case RecursivelyEnumerableSet() if self._enumeration_terminates():
            return self._enumerated_cardinality()
        case _:
            assert False, (
                "cardinality is mathematically defined for every set, but the current "
                "implementation has no algorithm for this represented case"
            )
```

The exact cases/algorithms must reflect real repository mathematics; the point is the architecture. The method is owned by `Sets`, implemented on genuine supported cases, and the final assertion documents the current computational frontier.

When static typing genuinely makes the final branch `Never`, prefer `typing.assert_never` as the exhaustiveness marker. When the runtime category/representation partition is not statically expressible, an informative final `assert False, ...` is reasonable here. The distinction from a stub is that preceding branches implement real mathematics.

Similarly:

```python
def is_nondegenerate(self):
    match self:
        case FiniteRankRepresentedForm():
            return self.gram_tensor().determinant() != 0
        case _:
            assert False, (
                "nondegeneracy is currently decidable only for represented finite-rank forms"
            )
```

Prefer specialized subcategory overrides when they give a cleaner implementation, but do not move the *mathematical notion* into a fake computability category merely because one algorithm is partial.

Mathematical code still avoids exception-driven fallback, `hasattr` probing, and try/catch routing. Engineering adapters may catch external failures; the mathematical layer routes by declared mathematical representation/category and asserts the unsupported remainder.

### Finitary-overfitting and semantic-lowering patterns

#### `STY-91`: Eagerly materialize a mathematical family -> keep the owned set/family lazy

**Red flag:**

```python
labels = tuple(M.module_generating_set())
generators = list(G.group_generators())
objects = tuple(C.object(x) for x in C.object_set())
```

The coercion silently changes "this mathematical family exists" into "this family can be exhausted now."  That is a much stronger assumption and often the source of infinite-case blast radius.

**Preferred:** keep the owned set/indexed family itself and use iteration, membership, `cardinality`, `rank`/`unrank`, finite support, images, or lazy enumeration as needed.  If a backend requires a finite array, assert the required finiteness and serialize at that private boundary only.

Concrete smell: `DiscreteCategory.objects()` must not turn an arbitrary enumerable object set into a tuple; the objects of a discrete category are the owned image of its object set, which can be infinite.

#### `STY-92`: Finite-support elements -> do not require a finite indexing set

Many mathematical objects have **finite support over an infinite family**.  Do not confuse these two notions.

**Bad:**

```python
def FormalDivisorGroup(R, prime_divisors):
    return FreshFreeModuleOn(R, finite_ordered_set(prime_divisors))
```

if the intended divisor group is the free module on an arbitrary set of prime divisors.  Individual divisors have finite support; the set of possible prime divisors need not be finite.

**Preferred:** the parent is free on the owned prime-divisor set; each divisor element stores only its finite support.  The same principle applies to free modules, group rings, sparse polynomials, formal sums, configurations, and indexed families.

#### `STY-93`: Raw matrix rows/columns implement a theorem -> ask the semantic mathematical objects instead

Rows, columns, basis matrices, and coordinate vectors are representations.  If the theorem can be stated without coordinates, the implementation should be stated that way too.

**Bad:**

```python
image_rows = matrix_of(d1).row_module()
relation_rows = presentation_matrix(M).row_module()
return image_rows == relation_rows
```

**Preferred:**

```python
return d1.image() == augmentation.kernel()
```

with subobject/Hom equality owning whatever finite-coordinate algorithm is presently available.  This allows future infinite/theorem-backed equality algorithms without rewriting `FreeResolution.is_exact()`.

#### `STY-94`: Assemble block matrices by hand -> construct the block morphism on biproducts/direct sums

**Bad:** concatenate row arrays, slice columns, or call a matrix `stack` operation to represent a map

\[
A_1\oplus A_2 \longrightarrow B_1\oplus B_2.
\]

**Preferred:** construct the morphism from its four components

\[
f_{ij}:A_j\to B_i
\]

through the Hom/biproduct API.  A finite matrix backend may realize this as a block matrix privately.  The public object remains a morphism between biproducts, so the same construction can represent an infinite block family or a formal block Hom without changing consumers.

#### `STY-95`: Compute cohomology from kernel basis matrices -> `ker/im/quotient` semantics

**Bad:** build lift matrices, take a backend right kernel, choose a basis matrix, project rows, append denominator rows, re-coordinate them, and finally synthesize a presentation.

**Preferred mathematical definition:**

```python
cycles = d_n.kernel()
boundaries = d_previous.image()
return cycles.quotient(boundaries)
```

or the corresponding subobject/quotient construction already owned by the complex.  A finite-presentation backend may optimize this entire construction, but it belongs behind `kernel`, `image`, subobject inclusion, and quotient.  `Cohomology` should not know row orientation or basis-matrix conventions.

#### `STY-96`: Compute an intersection/preimage from kernel rows -> categorical pullback/kernel

The current coordinate identity may be correct while still being the wrong abstraction.

**Bad:** form matrices for inclusions, stack `(i,-j)`, compute a left kernel, extract half the coordinates, turn its rows back into generators.

**Preferred:** the intersection of subobjects is the pullback of their inclusions; the inverse image of `S -> N` along `f:M->N` is the pullback of `f` and the inclusion, equivalently the appropriate kernel construction when additive structure is available.  Construct that pullback/kernel as a subobject.  Let the finite-free Hom implementation choose the matrix algorithm privately.

Concrete current sites: `modules/subobjects.py::intersection` and `functors/subobject_images.py::_inverse_image_subobject` already describe this universal property in comments but then drop to raw rows.

#### `STY-97`: Invariants/coinvariants require finite generators -> use the action's equalizer/coequalizer semantics

**Bad:** require a chosen finite group generating set, build one kernel for every generator, intersect them, or build all relations `(g,m) -> gm-m` from a finite Cartesian product of generator sets.

**Preferred:** `M^G` is the fixed-point/equalizer subobject of the action; `M_G` is the corresponding coequalizer/quotient.  The action object owns these constructions.  A finitely generated group gives a convenient finite algorithm, but finite generation must not define the existence or public shape of invariants/coinvariants.

This also avoids the blast radius when `G` is infinitely generated but represented by a stronger action theorem/backend.

#### `STY-98`: Exhaustively test every element to recognize structure -> structural maps/theorems first, finite exhaustion only as a fallback case

**Bad default:** enumerate every element of a finite underlying set and every scalar, then test all triples to decide associativity/module laws or enumerate every element to compute an annihilator.

**Preferred:** express the structure by the mathematical maps that make the law meaningful and use category/theorem-backed algorithms.  For a module, the scalar action is `rho:R -> End(M)`; for the annihilator, use the kernel/ideal of the scalar-action morphism where represented.  An exhaustive finite check can remain one explicit computability case in a routing table, but must not become the ontology or the only architecture.

Concrete smell: `GeneralModuleParent.annihilator()` currently enumerates the scalar ring and entire module; `_verify_module_laws_when_decidable()` performs cubic scans of the underlying set.  Those are acceptable finite diagnostics/fallbacks, not the general mathematical implementation strategy.

#### `STY-99`: Return `tuple`/`list` for a mathematical set/family -> return an owned set/family or lazy enumeration

**Bad:**

```python
def roots_of_square(...):
    return tuple(...)

def vector_orbit_representatives(...):
    return tuple(representatives)
```

unless the Python tuple is explicitly private serialization.

**Preferred:** return the relevant owned finite set, ordered set, indexed family, orbit-representative set, or lazy enumerated set.  Finiteness is a property of that mathematical collection, not a reason to replace it by a Python sequence.

#### `STY-100`: Presentation matrix is an implementation of a presented object, not the object itself

A chosen finite presentation legitimately has a finite matrix realization.  The error is letting ordinary mathematical consumers treat that matrix as the only interface to the presentation.

**Bad:** consumer code calls `.rows()`, slices columns, counts row lengths, takes row modules, and reconstructs subobjects manually.

**Preferred:** consumers ask for the presentation morphism, its image/kernel/cokernel, its relation subobject, base change, or the corresponding universal construction.  The presentation subsystem may use a matrix internally when the chosen framings are finite.

#### `STY-101`: Fiber/rank/minimal-generators via hand-specialized relation matrix -> construct the fiber/residue module and ask it

**Bad:** specialize every relation row modulo a prime/maximal ideal, build a backend matrix, compute its rank, then subtract from a generator count inside `fiber_dimension()` or `minimal_number_of_generators()`.

**Preferred:**

```python
fiber = M.fiber(p)
return fiber.dimension()
```

and for a local ring use `M.residue_module().dimension()` as Nakayama dictates.  The vector-space/presented-module implementation may compute that dimension by matrix rank privately.  This keeps localization, base change, residue fields, and dimension as the semantic spine.

#### `STY-102`: Verify structure by checking every pair of chosen basis generators -> verify the structure morphism

**Bad:** for every chosen group generator and every pair of lattice generators, compare all pairings to verify that an action preserves the form.

**Preferred:** the action is a morphism

\[
G \longrightarrow \operatorname{Aut}(L,b)
\]

or its image maps are verified by the formed-module Hom/automorphism category.  Form preservation is equality/commutation of the correlation/form morphism, not a nested finite basis loop.  A finite Gram check may be the implementation of that Hom predicate, but callers should not know it.

Concrete current site: `group_modules/group_lattices.py::GroupLattice` explicitly assumes finite rank and finite group generation solely to run this exhaustive check.

#### `STY-103`: Coordinate/numeric algorithm appears above the semantic owner -> push it down behind the owner

Use this as the general review test.  If code in cohomology, exactness, lattice structure, group actions, subobjects, or geometry manipulates raw `rows`, `columns`, `basis_matrix`, flattened entries, or coordinate vectors, ask whether that numeric code belongs instead in the Hom/module/tensor/subobject/backend operation it is trying to compute.

**Preferred layering:**

```text
mathematical consumer
    -> semantic operation (kernel/image/pullback/product/dimension/...)
        -> category/representation-specific algorithm
            -> finite coordinates / matrix / CAS backend
```

not:

```text
mathematical consumer
    -> rows/columns/coordinates
        -> manually reconstruct the semantic result
```

The latter makes every consumer finite-coordinate-aware and gives infinite generalization a repository-wide blast radius.


#### `STY-104`: `morphism -> matrix -> nullspace -> rebuilt submodule` -> `morphism.kernel()`

This is a canonical LLM over-lowering pattern.

**Bad:**

```python
A = f.matrix()
rows = A.right_kernel().basis_matrix().rows()
K = FreeModule(R, len(rows))
inclusion = ...  # rebuild the vectors as elements of f.domain()
return K, inclusion
```

**Preferred:**

```python
return f.kernel()
```

The kernel implementation owns coordinate algorithms and returns an honest subobject/inclusion. A caller that only needs the kernel never sees a matrix.

#### `STY-105`: Numerical criterion for a structural predicate -> spell the mathematical definition

**Bad:**

```python
def is_primitive(i):
    A = i.matrix()
    return gcd(maximal_minors(A)) == 1
```

**Preferred:**

```python
def is_primitive(i):
    return i.cokernel().is_torsion_free()
```

Similarly, prefer `f.kernel().is_zero()` to rank comparison for injectivity, the correlation morphism to determinant tests for nondegeneracy, and `correlation.is_isomorphism()` to determinant-unit tests for unimodularity. Numerical criteria belong inside the implementations of these semantic predicates, where their hypotheses can be routed correctly.

#### `STY-106`: Consumer extracts coordinates because the semantic operation is missing -> add the semantic operation first

**Bad development behavior:**

```python
# There is no useful Subobject.pullback yet, so this one caller manually
# stacks inclusion matrices and takes a kernel.
```

**Preferred:** implement/fix the pullback, kernel, subobject, or other semantic operation at its mathematical owner, then make the consumer one or two semantic calls.

A missing semantic API is not external scope. It is evidence that the local feature has reached a foundational abstraction that must be strengthened. The smallest architecturally correct patch may therefore touch a lower-level category/Hom/subobject module before simplifying the original caller.

#### `STY-107`: Downstream finite/infinite case split -> move representation routing into the semantic owner

**Bad:**

```python
if M.is_finite_rank():
    A = f.matrix()
    ...
else:
    ...  # every consumer invents another infinite branch
```

**Preferred:**

```python
K = f.kernel()
```

with `kernel()` itself routing finite-free, finitely-presented, sparse/infinite, theorem-backed, or engine-specific cases. Downstream mathematics should normally be representation-oblivious.

#### `STY-108`: Local helper that reconstructs a universal construction -> delete it in favor of the universal construction

**Red flags:** helpers named or behaving like `_kernel_from_matrix`, `_intersection_from_rows`, `_preimage_from_coefficients`, `_quotient_from_relations`, `_image_basis`, `_block_matrix_for_map`, or `_rank_from_presentation` in a downstream theory module.

Before retaining such a helper, ask whether it is merely rebuilding `kernel`, `image`, `pullback`, `cokernel`, `quotient`, biproduct/block-Hom, `fiber`, `dimension`, or another existing universal construction. If yes, use or repair that construction instead.

#### `STY-109`: A theorem stated semantically but implemented numerically in the caller -> make the code resemble the theorem

**Bad:** a comment says “the intersection is the pullback” or “cohomology is cycles modulo boundaries,” followed by dozens of lines manipulating matrices.

**Preferred:** the executable code should retain the same nouns and arrows as the mathematical statement:

```python
intersection = pullback(i, j)
H_n = d_n.kernel().quotient(d_previous.image())
exact = d1.image() == augmentation.kernel()
```

If these calls are not yet capable enough, repair them. A comment stating the correct abstraction does not excuse implementation at the wrong layer.

#### `STY-110`: Repeated numerical extraction is API feedback, not a reason for another extraction

The first downstream `.matrix()`/`.rows()` workaround may reveal a missing method. The second occurrence is strong evidence of a missing semantic abstraction. Do not copy the workaround into a third consumer.

When several callers need “kernel as subobject,” “span as subobject,” “block morphism,” “dimension after base change,” “torsion-free quotient,” or another recurring mathematical result, promote that operation to the common owner and delete the caller-specific numeric implementations.

#### `STY-111`: Optimize the semantic method, not each consumer

If a semantic composition is mathematically right but slow, preserve it as the mathematical route and optimize underneath it.

**Bad:** replace `i.cokernel().is_torsion_free()` in one lattice routine by a hand-written gcd/minor test because it is faster there.

**Preferred:** teach `cokernel()`/`is_torsion_free()` the efficient finite-presentation or Smith-form case. Every caller then gets the optimization, and future infinite cases still have one routing point.

This remains the preferred direction even when the low-level optimization internally collapses several semantic stages into one backend call.

#### `STY-112`: Coordinate tuple/vector as element input -> construct the element in its parent

Coordinates are observations relative to chosen data, not a second element language.

**Bad:** `x = L([1, 2])` or `y = M(tuple(coefficients))` when the bare sequence is admitted as an alternate public spelling for an element.

**Preferred:** use the parent's named generators / finite-support mathematical construction and form the element in the parent's language, e.g. `x = e + 2*f`, or an owned finite-support coefficient datum whose parent/index set is explicit.  A private backend adapter may serialize that element to a vector after construction.

#### `STY-113`: Matrix -> morphism may be construction; morphism -> matrix -> conclusion is a red flag

The coordinate boundary is directional.  A finite framed Hom constructor may consume matrix data to construct the actual morphism, validate domain/codomain/relations, and return the Hom element.  Once `f` exists, stay with `f`.

**Bad:** `A = f.matrix()` followed by a conclusion about injectivity, image, kernel, cokernel, primitivity, or form preservation.

**Preferred:** `f.kernel()`, `f.image()`, `f.cokernel()`, `f.is_injective()`, `f.is_surjective()`, composition, and Hom predicates.  The owner may internally return to a matrix for the finite case.

#### `STY-114`: Zero-matrix/entry-fill loops -> whole-object constructor, then semantic wrapper

Inside a private finite-coordinate boundary, do not manually own standard row/column layout when Sage already names it.

**Bad:** allocate a zero matrix and fill diagonal/block/column entries with nested index loops.

**Preferred finite backend idioms:** `matrix(rows)`, `column_matrix(columns)`, `diagonal_matrix`, `block_matrix`, `block_diagonal_matrix`, `identity_matrix`, `zero_matrix`, sparse constructors, `.apply_map`, and slicing.  Better still, if the object is mathematically a biproduct morphism, form, or endomorphism, construct that semantic object and let its backend choose the matrix constructor.

#### `STY-115`: Ported Sage signature -> resite the mathematics; never port the ontology

A foreign method name/signature is evidence about available computation, not a contract for the owned API.

**Red flags:** `ambient=`, `in_ambient=`, `even=`, `negative=`, mode booleans naming category membership, or a method on a bare object whose actual datum is an inclusion/morphism/base change.

**Bad:** `L.saturation(in_ambient=M)` or `Lattice(G, even=True)` when the parameter compensates for missing categorical structure.

**Preferred:** saturation on the subobject/inclusion; construct the general lattice/form and let category refinement record evenness or other derived structure.  Port **semantic capability**, not signature parity.

#### `STY-116`: Structure/category membership flag -> infer/refine it as output

Do not ask the caller to state a property the constructed mathematical datum already determines.

**Bad:** `Lattice(G, even=True)`, `Form(..., nondegenerate=True)`, `Module(..., torsion=True)` when those facts are decidable/declared from the datum.

**Preferred:** construct from the defining datum, then place/refine the result into the strongest justified categories.  A genuinely chosen structure is different and must be supplied as its actual datum, not as a boolean.

#### `STY-117`: Witness-compensating parameter -> first-class witness object

**Bad:** an operation on `A` accepts `ambient=B`, `inclusion=...`, or another optional parameter solely because `A` does not carry the relationship the operation needs.

**Preferred:** construct/use the subobject, morphism, functor image, base-changed object, or other witness-bearing object and put the operation there.  For a subobject, the “ambient” is simply `inclusion().codomain()`.

#### `STY-118`: Compatibility shim/alias after a redesign -> update callers and delete the old route

**Bad:** keep an obsolete ambiguous API and add the precise name as a wrapper over it, or retain an old constructor solely so internal callers continue to work.

**Preferred:** make the precise/canonical API the implementation, migrate all callers in the same change, and delete the superseded route.  Deliberate REPL conveniences such as `lmap` are not compatibility shims; they are intentional session vocabulary.

#### `STY-119`: Tiny internal wrapper with no semantic role -> call the existing operation directly

A short function is justified when it is a canonical semantic owner, a boundary, a constructor, or deliberate session notation.  It is not justified merely to rename an already-clear operation locally.

**Bad:** `def _make_identity(n): return identity_matrix(ZZ, n)`.

**Preferred:** call `identity_matrix(ZZ, n)` directly, or introduce a wrapper only when it centralizes mathematical validation/ownership that every caller must share.

#### `STY-120`: `globals()` mutation / dynamic sibling import -> static names and a repaired DAG

**Bad:** `globals().update(...)`, `global X` used to install exports dynamically, or `importlib.import_module(...)` used to postpone a sibling import and hide a cycle.

**Preferred:** ordinary module-scope imports/type aliases, or move the shared definition into a dependency-light defining module.  Optional external plugins may require dynamic loading at an engineering boundary; ordinary mathematical modules do not.

#### `STY-121`: QC-only statement/suppression -> fix the code or the shared tooling

Do not add executable or annotation noise whose only purpose is to silence a checker.

**Red flags:** `del arg` in an abstract/overload body, gratuitous casts, broad `Any`, `# type: ignore`, `# noqa`, or compatibility wrappers introduced only to reduce a warning count.

**Preferred:** if the diagnostic exposes a real mathematical/API defect, repair it.  If the checker lacks knowledge of Sage/category machinery, repair the shared stub/plugin/QC configuration.  A narrow suppression is admissible only for a genuinely untyped external boundary and must document that boundary.

#### `STY-122`: Test unwraps coordinates/matrices to state a semantic claim -> test the mathematical object

**Bad:** a test claims something about a kernel/image/subobject/isometry but compares matrix ranks, coordinate tuples, kernel basis rows, or raw backend objects.

**Preferred:** construct typed elements/morphisms and assert `f.kernel()`, `f.image()`, `f.cokernel()`, `f.is_surjective()`, subobject equality, isomorphism witnesses, or the named invariant.  If the test cannot state the claim without unwrapping coordinates, add the missing semantic noun/verb first.

#### `STY-123`: Numerical shadow used as the test claim -> assert the named invariant/structure

Determinants, ranks, coordinate lists, and cardinalities are legitimate when *they are the mathematical invariant under test*.  They are not substitutes for a stronger structural claim.

**Bad:** determinant equality as the sole claim that two lattices are isometric; row equality as the sole claim that two morphisms agree; rank equality as surjectivity.

**Preferred:** assert the actual isomorphism/equality/morphism predicate, and optionally cross-check the numerical shadow as a secondary invariant.

#### `STY-124`: Stale issue/docstring/comment/test after a ruling -> repair the prescription before code

A prescription that describes the rejected model is a code generator for future regressions.

**Red flags:** issue bodies naming old constructor signatures, comments explaining a coordinate workaround that policy has rejected, dead docstrings claiming a semantic implementation above numerical proxy code, generated/reference tests preserving a superseded API.

**Preferred:** update or delete the authoritative record immediately when the ruling lands, then continue implementation from the corrected record.

#### `STY-125`: Correct failure is inconvenient -> repair the defect; never launder the failure

**Bad remediation:** delete/weaken a mathematically correct assertion or red test, narrow the stated requirement after implementation fails, patch an unrelated symptom, or make the condemned representation “work” just enough to turn the check green.

**Preferred:** preserve the proposition/contract, treat the failure as evidence locating the real defect, and repair that defect.  Restarting an implementation while preserving the contract is acceptable; manufacturing success by weakening truth is not.

#### `STY-126`: Copy/port old implementation structure -> semantic reconciliation

When absorbing archived/legacy code, first map every notion onto the current owned ontology.

**Bad:** copy a module/class hierarchy because it already implements the algorithm, or quarantine only a tiny slice while leaving duplicate notions.

**Preferred:** reuse current categories/functors/Homs where the notion already exists; rewrite only genuinely missing mathematics into current owners and style.  Preserve semantics, not directory layout, class names, or historical architecture.

#### `STY-127`: Bare multi-structure generator name -> qualify the structure

**Bad owned vocabulary:** `generator`, `generators`, `generating_set`, `ngens`, `embedded_gens` when an object can simultaneously carry module, algebra, and group structures.

**Preferred:** `module_generator`, `module_generating_set`, `group_generators`, `algebra_generating_set`, `number_of_module_generators`, etc.  Do not keep the bare name as a compatibility alias.  Native Sage `.gens()` names remain native inside backend calls.

#### `STY-128`: Public presentation-facing constructor -> canonical constructor from mathematical datum

**Bad primary API:** `from_matrix`, `from_relations`, `with_action(G, matrices)`, or a subobject constructor from raw rows when the actual datum is a morphism/action/inclusion/presentation.

**Preferred:** construct the defining morphism in its Hom, then pass that object to the canonical constructor.  Coordinate/matrix conveniences, where mathematically unambiguous for a canonically framed Hom, immediately produce the mathematical object and are not a second downstream language.

#### `STY-129`: “Not computable in full” -> still construct the predicate-defined mathematical object

Do not confuse inability to enumerate/generate an object with inability to represent it.

**Bad:** refuse to construct `O(L)`, a stabilizer, a center, or another predicate carve-out because generators/relations are unavailable.

**Preferred:** construct the owned predicate-defined subgroup/subset/category with membership and the operations that are available.  Add enumeration/generator algorithms as computable cases later.  A predicate must not claim `True` merely on trust; construction-time trust, when unavoidable, is a separately documented choice.

#### `STY-130`: Definition hard-codes a removable hypothesis -> formulate generally, recover the special case by refinement

**Red flags:** a framing requires a finite/ordered set although the definition only needs a set; a direct-sum notion is defined only for finite families because the first backend is matrix-based; a construction is named after one base ring even though its definition works over a wider ring class.

**Preferred:** state the notion at the weakest hypotheses under which it remains mathematically meaningful, then recover finite/free/projective/ordered/enumerable/commutative special cases as axioms, subcategories, or algorithmic cases.  Use extreme infinite/nonenumerable objects as stress tests of the interface even when the current computation does not handle them.

#### `STY-131`: Hidden mathematical choice / definite article -> name the selecting datum

**Red flags:** “the dual”, “the extension”, “the normalization”, `normalize=True`, `map=True`, or another flag whose value changes which mathematical object/morphism is selected, without the choice being represented explicitly.

**Preferred:** determine whether the object is canonical.  If not, give the alternatives distinct mathematical names or accept/store the selected morphism/object/structure as first-class data.  A normalization/re-presentation is a new object together with its isomorphism; a chosen framing, orientation, action, embedding, closure presentation, or section is an actual datum, not a boolean mode.

#### `STY-132`: Subobject equality that forgets the inclusion -> compare the slice object

A subobject is not merely an object that happens to be isomorphic to something inside another object.  It is the object **together with its witnessing monomorphism**.

**Bad:**

```python
def __eq__(self, other):
    return self.underlying_object() == other.underlying_object()
```

for subobjects `i:S -> M` and `j:T -> M`.  Two isomorphic copies of the same abstract module embedded differently in `M` are different subobjects.

**Preferred:** equality of subobjects is equality in the relevant slice/subobject category: compare the underlying owned object together with the inclusion morphism (or delegate to the owned subobject/category equality that already does so).  Never reconstruct equality from common coordinates in the codomain.

#### `STY-133`: Quotient equality that forgets the projection -> compare the coslice/quotient object

The dual error occurs for quotients.  A quotient is not just its abstract codomain `Q`; it is the epimorphism `p:M ->> Q` together with that codomain.

**Bad:** treat two quotient presentations as the same quotient because their codomains are isomorphic or have equal invariant factors.

**Preferred:** keep the quotient/projection morphism first-class.  Equality as quotient objects includes the epi; an abstract codomain may be isomorphic while representing a different quotient of `M`.

#### `STY-134`: Identify an object with its image -> keep the morphism and image subobject distinct

**Bad:** because `f:X -> Y` is injective or surjective, silently identify `X` with `f(X)` or `Y` with the image, then let later code use equality where a morphism is the actual relationship.

**Preferred:** `f` is the relationship; `f.image()` is a subobject of the codomain; `X` remains the domain object.  Even when `f` is an isomorphism, equality and the exhibited isomorphism are different mathematical statements unless the construction is canonically identical by repository policy.

This applies to dual inclusions, rationalization/base change maps, quotient projections, embeddings, and all other arrows.  Do not erase the arrow merely because its image has a familiar description.

#### `STY-135`: Normalization mutates the object / hides behind a flag -> return the new object and isomorphism

A normal form or re-presentation changes chosen data.  That means it produces a different object of the framed/presented category, related to the source by an isomorphism.

**Bad:**

```python
M.normalize(in_place=True)
M.normal_form(transformation=False)
```

or replacing `M`'s chosen framing/presentation internally by a Smith/Hermite/canonical one.

**Preferred:**

```python
iso = M.invariant_factor_form()
normalized = iso.codomain()
```

where the returned isomorphism is part of the mathematical result.  The transformation is not optional metadata: it is what states why the new presentation represents the same abstract mathematics.

#### `STY-136`: Universal construction returns only a naked object -> return/attach its canonical structure morphism

A kernel, image, cokernel, quotient, pullback, pushout, product, coproduct, or similar construction is incomplete if the universal structure maps have been discarded.

**Bad:** `f.kernel()` returns a module whose basis happens to span the nullspace but has no inclusion into `f.domain()`; `f.cokernel()` returns an abstract presented module with no canonical projection from `f.codomain()`.

**Preferred:** the owned result carries or canonically exposes the relevant maps: kernel inclusion, image inclusion/factorization, cokernel projection, product projections, coproduct injections, pullback legs, pushout legs, and so on.  Downstream code should be able to use the universal property without reconstructing those arrows from coordinates.

A quotient element's `lift()` may select a representative; it is not a canonical inverse to the quotient projection and must not be presented as one.

#### `STY-137`: Test a weaker equivalence relation on equal objects -> use genuinely different objects

**Bad:** test `is_isomorphic`, `is_isometric`, same-genus, or another relation weaker than equality using `X` and `X` or two constructions that canonicalize to the same owned object.  Equality makes the weaker claim tautological.

**Preferred:** choose distinct objects/presentations known to be related in the weaker sense: two differently framed but isomorphic modules, two different Gram presentations of isometric lattices, or genuinely distinct representatives in one genus.  The test must be capable of falsifying the weaker-relation implementation.

#### `STY-138`: Implementation-role noun -> identify the standard mathematical object or datum

LLM-generated code often invents an implementation ontology around words such as `provider`, `manager`, `context`, `evidence`, `knowledge`, `metadata`, `payload`, or `wrapper` when the thing is already a standard mathematical object.

**Bad:** ask a caller for a `SubobjectEvidence`, `GeneratorProvider`, or `NormalizationContext` when the actual datum is an inclusion morphism, indexed family, isomorphism, framing, or functor.

**Preferred:** name and type the actual mathematics.  Before introducing a helper noun, ask whether a mathematician could define it independently of this codebase and whether an existing category/object/morphism/functor already is that thing.  Engineering records may exist at engineering boundaries; they do not become public mathematical ontology.

#### `STY-139`: Brainstorm wrappers/overloads/adapters before stating the mathematics -> state the mathematical model first

**Bad review sequence:** encounter a signature collision or missing operation and immediately compare overloads, optional arguments, wrappers, adapters, casts, aliases, registries, or dispatch tricks.

**Preferred sequence:** first state what `self` is mathematically, what datum the operation consumes, where it is well-defined, what object owns it, and what its mathematical return object is.  Only after that model is fixed choose the smallest Python/Sage mechanism that realizes it.  If naming the mathematics makes the engineering alternatives disappear, discard them.

#### `STY-140`: Reviewer names one symptom -> patch only that symptom while preserving the contaminated implementation

A review finding is evidence about a generator, not a specification saying “remove this exact line and preserve everything else.”

**Bad:** a reviewer flags matrix-based kernel reconstruction, so move the same reconstruction into a helper/adapter and leave all callers and tests semantically unchanged; a reviewer flags a global dispatcher, so hide the switchboard behind a registry without changing ownership.

**Preferred:** identify the architectural generator that produced the finding, inspect sibling instances and consumers, repair the semantic owner, and simplify the callers.  Do not make preservation of the currently contaminated implementation or its representation-level tests an unstated acceptance criterion.

#### `STY-141`: Invent canonical arrows from analogy -> read the actual universal diagram

Do not infer structure maps because an object “looks like” a product, quotient, tensor, or coordinate construction.  The universal property determines the canonical arrows.

**Bad:** treat `M tensor N` like a Cartesian product and invent projections `M tensor N -> M`, `M tensor N -> N`, or canonical maps `M -> M tensor N` without chosen elements.

**Preferred:** state the defining diagram.  For a tensor product, the canonical map is the bilinear set map

\[
M\times N \longrightarrow M\otimes_R N,
\]

and maps out of `M tensor N` correspond to bilinear maps out of `M × N`.  No map from either factor alone is canonical without extra selected data.  Apply the same discipline to every universal construction.

#### `STY-142`: Functor accepts too broad a category then rejects arrows -> restrict the domain category

**Bad:** define `F:C -> D`, then inside `_apply_morphism` assert/reject every non-isomorphism because the construction is only functorial on isomorphisms.

**Preferred:** declare `F:C.core() -> D`.  If the mathematical variance/domain is a slice, coslice, arrow category, subgroupoid, or other subcategory, make that the functor's actual domain.  Runtime assertions may still document internal assumptions, but they do not substitute for a mathematically wrong functor signature.

#### `STY-143`: Parameterize an intrinsic notion -> derive it from the existing structural maps

A notion with an a priori mathematical meaning is not a customization hook.

**Bad:** ask for an `integrality_submodule`, an `integral_over=` mode, or another parameter redefining what “integral” means when the existing ring map already determines integrality.

**Preferred:** derive the notion from the relevant structure already present—for example integrality in a ring extension from the specified ring morphism.  If a genuinely different notion is wanted, give it a different mathematical name rather than parameterizing the standard one into ambiguity.

#### `STY-144`: “Safe” horizontal patch during an architectural migration -> make the breaking vertical move

**Bad:** preserve every old caller, wrapper, and intermediate representation while moving one method at a time because each commit is expected to remain locally green, even though the target architecture makes much of that code disappear.

**Preferred:** move the mathematical responsibility to its final owner, migrate the affected vertical slice, delete superseded routes, and allow intermediate repository states to be broken when the active architectural work explicitly permits it.  Do not spend effort polishing code scheduled for deletion merely to preserve incremental compatibility.

#### `STY-145`: Deep specialized file owns an obviously general concern -> stop and audit placement

**Red flag:** a lattice-only file contains generic cardinality/set logic; a subobject implementation contains generic quotient machinery; a scheme leaf implements a generic product/Hom construction.

**Preferred:** stop before patching the local code and ask which more general category/object should own the concern.  Search sibling implementations for duplication and move the abstraction upward/downward to its mathematical owner.  A misplaced concern is evidence that the architecture around the site may be wrong.

#### `STY-146`: Exact mathematical result vs soft knowledge result -> use the correct codomain

Do not force every question into a Python boolean, and do not use `Unknown` to replace an exact mathematical value.

**Exact operation/predicate:** `cardinality()`, `is_nondegenerate()`, `kernel()`, etc. retain their mathematical codomain.  If today's algorithm does not cover a represented case, route known cases and assertion-gate the unsupported computational remainder as specified by `CAT-01`.

**Soft knowledge/computability predicate:** a deliberately epistemic API such as `generators_are_computable()` or `has_computed_group_generators()` may have the explicit three-valued codomain `True | False | Unknown` when “not currently known/decided” is itself what the method is asking.

**Bad:** return `False` from `is_nondegenerate()` because no algorithm is known; return `Unknown` as the “cardinality” of a set; return `True` from a soft predicate merely because construction trusted an input.

#### `STY-147`: Universal-property test checks one factorization only -> test existence and uniqueness

**Bad:** construct one factorization through a tensor product/kernel/product/etc. and assert that it commutes, while never testing the uniqueness clause—or compare the same generated map to itself twice.

**Preferred:** test the actual universal property: construct the canonical factorization, verify the diagram, and verify uniqueness against a genuinely independently constructed competing morphism where practical.  Choose nonzero/nontrivial specimens so uniqueness is not vacuous.

#### `STY-148`: Parallel Set Hom / exponential / power-set objects -> canonical identification

**Bad:** implement `Hom_Set(X,Y)`, an independent function-set parent `Y^X`, and a separate power-set parent `P(X)` with overlapping iteration/cardinality/map behavior.

**Preferred:** represent the canonical identities

\[
\operatorname{Hom}_{\mathbf{Set}}(X,Y)=Y^X,
\qquad
P(X)=2^X=\operatorname{Hom}_{\mathbf{Set}}(X,2)
\]

as object identity/one owned construction with the relevant category placements.  Cardinality and set operations then follow once from that object.  Do not preserve parallel parents merely because different callers arrived through different notation.

#### `STY-149`: Literal mathematical expected values scattered through tests -> cited reusable fact data

**Bad:** dozens of tests independently write facts such as named-lattice ranks, discriminants, orbit counts, genus classes, number-field invariants, or classification-table rows as inline literals, often with duplicated or missing provenance.

**Preferred:** put the independently verified mathematical fact in the repository's topic-organized fixture/fact corpus with its construction/identifier, value(s), citation/oracle provenance, and verification status.  Tests become thin parametrized drivers that compute the repository result and compare it to that fact.

#### `STY-150`: Current implementation output used as its own expected value -> independent source/oracle

**Bad:** run the method being tested, copy its output into a fixture, then assert future runs reproduce that output; or treat a Sage result as mathematical truth merely because Sage is the current backend under test.

**Preferred:** expected mathematical values come from an independent cited source, a separately justified oracle/reference implementation, or a migrated source-system test corpus appropriate to the task.  The implementation under test is never the provenance for its own expected result.

#### `STY-151`: Element repr exposes coordinate storage -> render the mathematical expression

**Bad:** an element of a framed/free module or lattice prints as `(2, -1, 0)` or as a backend vector, making its storage representation look like the element itself.

**Preferred:** render the owned formal linear combination in the selected generator/framing symbols, using the coefficient ring's own representation and the symbols' own representation.  Coordinates may be inspectable through an explicit framing/coordinate operation, but ordinary `repr`/LaTeX presents the mathematical element.

Do not hard-code integer-specific sign/absolute-value formatting into a generic `R`-module printer; an arbitrary coefficient ring need not have those notions.

#### `STY-152`: “Framing” stored as a finite generator list -> selected epimorphism from a free module

**Bad:** define a framed module as `M` plus `tuple(generators)` and then infer that the tuple is finite, ordered, injectively labelled, or a basis.

**Preferred:** a framing is the selected epimorphism

\[
\operatorname{Free}_R(S) \twoheadrightarrow M
\]

for an owned set `S`.  The distinguished-generator map is the underlying-set image of this morphism.  `S` may be infinite, nonenumerable, unordered, and different labels may map to the same module element.  A basis/free framing is a stronger refinement, not the generic meaning of “framed.”

#### `STY-153`: Backend-category graph used as mathematical taxonomy -> capability correspondence

**Bad:** mirror Sage's `super_categories()` graph, manufacture owned categories solely so every Sage name has a destination, or use Sage category equality/edge layout to decide mathematical identity.

**Preferred:** the owned category/functor graph defines the mathematics.  A private/versioned correspondence records which Sage categories/implementations can compute for which owned categories and operations.  Several Sage categories may provide one owned capability; one Sage category may require a normalized owned expression.  Backend taxonomy is empirical implementation data, not ontology.

#### `STY-154`: Descendants repeat inherited operations -> fulfill obligations through the preferred functor

**Bad:** lattices reimplement cardinality/iteration, modules reimplement generic set products, every structured category writes its own version of an operation already owned below a forgetful/structure functor.

**Preferred:** declare the semantic operation once and identify a preferred structure-forgetting/projection functor at the appropriate rollup point.  Delegate `X.operation()` through that functor when the target category already owns the operation.  A descendant implements only the new structure or a genuinely better algorithm justified by its refinement.

#### `STY-155`: Constructor named after a derived subcategory -> construct at the owning root and refine the result

**Bad:** require the user to choose `RootLattice(...)`, `EvenLattice(...)`, `TorsionModule(...)`, or another specialized constructor merely because the resulting object happens to satisfy that property.

**Preferred:** construct through the ordinary owning category/object constructor from the defining datum, then let the resulting object acquire every justified refinement.  The researcher should construct the mathematics they know, not predict the internal category routing first.

A specialized constructor remains justified only when the specialized name denotes genuinely additional **input structure**, not a property derivable from the supplied datum.

#### `STY-156`: Hand-authored forgetful/projection graph -> derive structural arrows from category expressions

**Bad:** maintain one table saying `C.A -> C`, another registry of ancestor forgetful functors, and hand-written forwarding paths that duplicate what the category/classifier construction already determines.

**Preferred:** if `C.A` is defined as a classifier application/pullback, its projection to `C` is part of that definition; ancestor projections are compositions of those structural arrows.  Store/implement the defining category expression and derive the canonical projection hierarchy from it rather than maintaining a second graph that can drift.

#### `STY-157`: Public `*args` / `**kwargs` option bag -> closed mathematical signature

**Red flag:**

```python
def construct(x, *args, **kwargs):
    return backend_constructor(x, *args, **kwargs)
```

on a public mathematical surface.

**Preferred:** enumerate the actual mathematical input shapes the preamble supports and give them precise signatures, named constructors, or source-grounded overloads.  A homogeneous variadic family is acceptable only when the mathematics itself is genuinely variadic and the element type/meaning is fixed; arbitrary backend option forwarding is not.

Private backend adapters may use `*args`/`**kwargs` when their entire job is literal protocol forwarding inside the boundary and the option bag cannot escape into the public mathematical contract.

#### `STY-158`: `None` sentinel selects a different mathematical operation/object -> split or make the datum explicit

**Bad:**

```python
def normalize(M, map=None): ...
def construction(X, ambient=None): ...
```

where `None` versus a value changes the mathematical object, witness, domain, codomain, or return shape.

**Preferred:** use distinct mathematical operations/constructors or accept the actual selected datum (morphism, ambient object when genuinely part of the definition, section, framing, etc.).  If omission means a genuinely canonical default such as the unit `1` or identity morphism, that default may be stated explicitly by the API; do not use `None` to conceal a noncanonical choice.

#### `STY-159`: Boolean mode flag changes mathematics or return type -> named operations / literal overloads

**Bad:** `normal_form(transformation=True)`, `roots(all=True)`, `galois_closure(map=True)` when the flag selects a different mathematical result or tuple shape.

**Preferred:** expose the mathematical objects/witnesses directly (`normal_form_isomorphism()`, chosen closure with its embedding, all-roots set, etc.), or—when compatibility with a source-level operation is intentionally retained at a non-mathematical boundary—use precise literal overloads there.  Do not make ordinary preamble callers memorize boolean modes.

#### `STY-160`: `pass` in a mathematical implementation -> implement, delete, or mark a genuine abstract contract

**Bad:** a visible concrete method/class body contains `pass` merely to postpone mathematics, silence a branch, or satisfy syntax.

**Preferred:** a genuine abstract category contract uses Sage `@abstract_method` with an ellipsis body; a concrete mathematical method is implemented; an impossible branch is asserted with its mathematical invariant; an unnecessary empty wrapper/class is deleted or replaced by the actual category refinement it represented.

`pass` remains ordinary Python in private engineering situations where “do nothing” is literally the intended protocol behavior, but it is a review flag in the mathematical subtree.

#### `STY-161`: Negated predicate where the complementary mathematical notion has a name -> expose the positive predicate

**Bad:** force users/callers to write `not L.is_nondegenerate()`, `not f.is_injective()`, or another negation when the complementary mathematical property has a standard name used in the field.

**Preferred:** expose the named positive concept (`is_degenerate()`, etc.) at its natural owner.  Do not implement a genuinely three-valued/partially decidable concept merely by Python negation: the positive predicates must preserve the intended mathematical/knowledge semantics of their codomains.

#### `STY-162`: One-use convenience wrapper hides a composable mathematical object -> expose the object

**Bad:**

```python
L1.same_genus(L2)
g.action_on_discriminant_group(x)
f.from_identity_matrix()
```

when the real mathematics is a genus value object, a group morphism, or an identity element of a Homset.

**Preferred:**

```python
L1.genus() == L2.genus()
rho = L.O().action_on(L.discriminant_module())
rho(x)
L.Hom(L).identity()
```

Expose the value/morphism/universal object because it can then be compared, composed, restricted, factored, have kernel/image taken, etc.  A wrapper that only packages one obvious use hides that structure and adds another name to memorize.

#### `STY-163`: Generic software-role suffix in the public mathematical API -> name the actual mathematical noun

**Red flags:** public names ending in or centered on `Model`, `Descriptor`, `Record`, `Info`, `Result`, `Context`, `Manager`, `Factory`, `Payload`, `Adapter`, `Backend`, `Provider`, or `Evidence` when those words merely describe the software role.

**Preferred:** identify the standard mathematical object/data: category, family, morphism, section, presentation, isomorphism, stratification, graph, action, form, quotient, etc.  If the object is genuinely an engineering record/adapter/backend, keep it private in the engineering subtree/boundary instead of promoting it into the mathematical language.

#### `STY-164`: Supplied generators returned as a canonical group -> construct a typed subgroup

**Bad:**

```python
O_L = L.orthogonal_group(generators=user_generators)
```

and then use `O_L` for canonical-group orbit/stabilizer/kernel/invariant statements.

**Preferred:**

```python
O_L = L.O()                         # canonical group object exists independently
H = O_L.subgroup(user_generators)  # exactly the group the supplied data proves
```

The supplied generators certify only `H = <generators> <= O(L)`.  Equality `H = O(L)` is a separate mathematical claim requiring an independent group-generation algorithm/theorem.  Downstream computations name the group they actually use.

#### `STY-165`: `Random*` / `Example*` / `Test*` mathematical type or category -> generate input data for the ordinary constructor

Randomness, example status, and fixture status describe a **process/use**, not a new mathematical kind.

**Bad:** `RandomLattice`, `ExampleModule`, `TestGroup`, `RandomLattices()`.

**Preferred:** a random/example generator produces legitimate defining data (Gram form, presentation, polynomial, relations, etc.) and feeds that data into the existing canonical constructor.  The returned object is an ordinary lattice/module/group and is refined by its mathematics.  Named standard examples belong in catalogues when useful; they do not automatically create new category vocabulary.

#### `STY-166`: Absence/rejection assertion can pass on a dead object -> assert positive capability/witness first

**Bad:**

```python
assert not hasattr(T, "projection")
assert invalid not in results
```

when an empty/broken `T` or empty `results` would pass equally well.

**Preferred:** state the positive mathematical structure that makes the negative claim meaningful, then test the actual positive universal/property statement.  For a tensor product, test the bilinear universal factorization and uniqueness rather than the absence of product projections.  For a filtered enumeration, first assert a sourced/nonzero expected population or independently established completeness before exclusions count as evidence.

A test of code removal that only asserts the removed name is absent is a closed loop around the edit, not a mathematical regression test.

#### `STY-167`: Sage `Element.__eq__` -> `_richcmp_` plus compatible `__hash__`

This rule is specifically for subclasses/runtime types of `sage.structure.element.Element`, not ordinary Python records or Sage `Parent` classes.

**Bad:**

```python
class MyElement(Element):
    def __eq__(self, other):
        return self.data == other.data
```

Sage's inherited zero/truthiness/coercion machinery compares elements through `_richcmp_`, so a bespoke Python `__eq__` can disagree with `is_zero()` and `bool(x)`.

**Preferred:** implement the one Sage comparison primitive:

```python
def _richcmp_(self, other, op):
    return richcmp(self.data, other.data, op)

def __hash__(self):
    return hash(self.data)
```

using the same immutable mathematical data for equality and hashing.  Let Sage's inherited `is_zero()`/`__bool__`/comparison machinery delegate to that primitive.  Put the implementation at the highest owned element type where the equality semantics are shared, not on every leaf.

#### `STY-168`: Hand-built linear-combination `repr` -> the host's symbolic representation helper

**Bad:** manually join coefficients/signs/generator labels in `_repr_`, usually assuming integer signs, absolute value, unit coefficients, or string labels.

**Preferred:** represent the element as the actual finite formal combination of its owned symbols and coefficients, and use Sage's `repr_lincomb` (or the corresponding owned formal-sum renderer) when its semantics match.  Let the coefficient ring and symbol objects supply their own representations.  Do not rebuild sign/`±1`/zero formatting by hand in every module/lattice/algebra element class.

This is not cosmetic: a symbolic `2*e - f` display reinforces that the element is a formal mathematical element, while a raw tuple or hand-formatted coordinate vector trains the numerical ontology the API is trying to prevent.

#### `STY-169`: Algorithm exhausts an entire mathematical object -> use structural data/theorem or make enumeration the explicit operation

**Red flag:**

```python
for x in G:
    ...
for x in M:
    ...
all(property(x) for x in X)
```

where correctness/termination requires eventually visiting **every** element of a group, module, lattice, ring, or other potentially infinite object.

**Preferred:** ask what finite/structural datum actually proves the claim: a chosen generating family when a finite-generation theorem makes that sufficient, a presentation/relation check, a morphism identity, category membership, a backend theorem, finite support of the particular element, or another semantic invariant.  If the operation genuinely is “enumerate all elements,” return/use the owned enumerated set lazily and let the caller explicitly request/consume enumeration.

A lazy `__iter__` implementation is not the smell; an unrelated algorithm whose success assumes the iterator terminates is.  An upstream `assert X.is_finite()` added solely because a loop needs exhaustion is the loop confessing that it lowered the mathematical domain.

#### `STY-170`: “Tensor product of matrices” -> Kronecker product / tensor product of the represented morphisms

Matrices as arrays have a **Kronecker product**.  Tensor product is the mathematical construction on modules/vector spaces/algebras and on linear maps between them.

**Bad:** describe `A.tensor_product(B)` or a block array `(a_ij B)` as “the tensor product of matrices,” then reason about it as though matrices themselves carried that universal construction.

**Preferred:** if `A` and `B` are matrices representing `f:V1->W1` and `g:V2->W2`, construct/consider the tensor morphism

\[
f\otimes g:V_1\otimes V_2\to W_1\otimes W_2.
\]

In chosen finite bases, its representing matrix is the Kronecker product of `A` and `B`.  Backend calls may use the engine's historical `.tensor_product` spelling privately, but public prose/API names the correct mathematical operation.

#### `STY-171`: Euclidean vector operation on a formed object -> use the object's actual form

**Red flags:** `dot_product`, standard-coordinate `norm`, Euclidean projection, Gram-Schmidt, shortest-vector language, or orthogonality code applied to an object carrying an arbitrary bilinear/quadratic form without explicitly routing through that form.

**Preferred:** ask the formed object for `b(x,y)`, `q(x)`, its correlation morphism, orthogonal complement, radical, or the appropriately named form operation.  A Euclidean/positive-definite algorithm lives only at the mathematical subcategory where that extra structure makes it valid, and its private backend may then use standard inner-product routines after the correct form has been transported/normalized.

#### `STY-172`: Definite/nondegenerate assumption appears because the backend wants it -> keep the general form semantics and localize the algorithmic case

**Bad:** make the base formed-object API positive definite or nondegenerate because the first available matrix routine needs an invertible/PD Gram matrix.

**Preferred:** arbitrary (including degenerate/indefinite) forms are first-class at the general owner.  Methods whose **mathematical definition** requires definiteness/nondegeneracy live on that narrower category; methods defined generally keep their general name/domain and route/assertion-gate the currently computable cases.  Backend assumptions never redefine the base mathematical object.

#### `STY-173`: Defect found in an owned dependency -> local facade/protocol workaround -> fix the owner

**Bad:** discover that the preamble lacks an annotation/semantic method, then add a local `Protocol`, stub, wrapper, copied helper, or workaround in the downstream consumer and merely file/report the upstream defect.

**Preferred:** if the defective dependency is part of the user's owned project stack and the fix is within the active task's mathematical dependency, correct it at its authoritative source, then consume the repaired interface.  A TODO/report is useful only when the source genuinely cannot be changed in the current ownership boundary.

#### `STY-174`: Stored backend object as long-lived implementation twin -> reconstruct ephemeral computation state when practical

**Bad:** an owned mathematical object stores a Sage/GAP/etc. twin and ordinary downstream methods repeatedly dig into it, allowing the backend ontology to become durable hidden state.

**Preferred:** for large standard algorithms whose inputs/outputs are mathematical data, construct the private backend representation from the owned data at the computation boundary, perform the complete operation, convert back, and discard it.  Durable backend state is justified only when the representation itself is a required long-lived computational resource and then remains behind one private owner/boundary (`BND-01`).

#### `STY-175`: Read every Sage `super_categories()` edge as inclusion -> classify the structural map first

Sage uses one graph edge mechanism for mathematically different relationships: full-subcategory inclusion, forgetting one operation/projection from a structured object, parameterized-family relationships, and implementation/MRO organization.

**Bad:** see `A in B.super_categories()` and conclude “every `B` is an `A`” or copy the edge directly into the owned category graph.

**Preferred:** determine the actual mathematical map represented by that Sage declaration—subcategory inclusion, forgetful/projection functor, reindexing/base-family map, or merely host implementation organization—then encode that owned construction/functor.  The Sage edge is empirical evidence about Sage, not the mathematical theorem.

#### `STY-176`: Sage category equality/parent lists used as category equivalence -> compare owned mathematical constructions

**Bad:** conclude two categories are mathematically different because Sage `C != D`, or identical because `C.super_categories() == D.super_categories()`.

**Preferred:** identify the owned normalized mathematical construction each Sage category models and compare those.  Two different Sage presentations of one pullback/category may compare unequal; two genuinely different refinements can have identical declared parents.  Missing Sage edges are implementation gaps, not mathematical non-inclusions.

#### `STY-177`: Bundled object type/presentation called “the category” -> keep the levels separate

Before naming an implementation artifact, separately identify:

1. the mathematical category;
2. an object of it;
3. the runtime/bundled Python/Sage type representing such objects;
4. any category structure placed on that runtime type;
5. any chosen presentation (basis, enumeration, coordinates, generators);
6. any property-cut full subcategory.

**Bad:** call a `Fintype`-like presentation “the category of finite sets,” or identify based modules with finite free modules because choice can produce a basis.

**Preferred:** name each level explicitly.  Equivalence between presentations does not erase which choice/structure the API actually carries.

#### `STY-178`: Exact upstream name not found -> compose standard mathematics before declaring a gap

**Bad:** search Sage/Mathlib for one class/function with the exact local spelling, find none, and conclude the concept must be newly implemented or contributed upstream.

**Preferred:** attempt to express it as a standard composition: a full subcategory cut out by a property, structured objects, a Hom/category construction, slice/coslice, inclusion/forgetful functor, base change, or transport through an equivalence.  A missing packaged noun is not a missing mathematical primitive.

#### `STY-179`: Upstream correspondence found -> preserve redundant local declaration -> delete/resite it if the correspondence exposes wrong ownership

**Bad:** discover that a ring-specific `size()` is exactly underlying-set cardinality and “fix” the design by delegating `Ring.size()` to that set cardinality, preserving the duplicate public word.

**Preferred:** use the correspondence diagnostically.  If the standard owner is `Sets`, remove the ring-local synonym and let the ring recover `cardinality()` through the forgetful/structural functor.  Alignment can prove a declaration redundant or misplaced; it does not automatically justify keeping it.

#### `STY-180`: Avoid a mature dependency because it is “heavy” -> compare human ownership and blast radius instead

**Bad reasoning:** reject `networkx`, a parser/grammar package, a multidispatch library, or another mature dependency because it adds packages, a build toolchain, or installation scaffolding, then implement the generic machinery locally.

**Preferred reasoning:** treat ordinary dependency/build/package substrate as baseline engineering.  Compare designs by the mathematics/generic logic the repository must now own and review, the blast radius of adding/changing a case, and whether other consumers can reuse the external abstraction instead of relearning it.  Use the mature dependency when it removes substantial owned machinery and is semantically appropriate.

#### `STY-181`: Hand-roll against Sage because the relevant host idiom was not checked -> inspect the host first

**Bad:** manually implement generator naming, identity construction, conformance checking, matrix reshaping, coercion, graph traversal, or another operation before checking Sage/stdlib/upstream for the native idiom.

**Preferred:** inspect the live host API/source and, when behavior matters, run a distinguishing probe.  Use the host operation where its semantics match; wrap it only at the owned mathematical boundary if vocabulary/ontology differs.  Lack of familiarity with Sage is not a reason to create a second local language.

#### `STY-182`: Nontrivial local algorithm appears before backend search -> map the semantic operation to mature software first

**Red flag:** a new multi-step algorithm for groups, ideals, lattices/forms, polyhedra, number theory, symbolic algebra, or graph structure appears in Python without any indication that the installed/open-source capability stack was checked.

**Preferred:** name the semantic operation, search the repository capability map and relevant mature exact systems, then either delegate through the owned boundary or document the true gap that forces local ownership.  “It was straightforward to code here” is not evidence that the repository should own it.

#### `STY-183`: Named composite/classifier spelling -> duplicate category vertex -> preserve one identity

**Bad:** represent `Semigroups` and `Magmas.Associative` as two independent categories connected by an equivalence/alias edge; similarly create a second category solely for every readable composite name.

**Preferred:** the standard name and the classifier expression are two presentations of **one category identity**.  The public name may be `Semigroups`; the defining expression may be `Magmas.Associative`; no second vertex/object is created.

#### `STY-184`: Same axiom word reused globally -> interpret classifier relative to its host category

Names such as `Commutative`, `Distributive`, `Graded`, `Finite`, etc. have meaning only together with the mathematical category/construction they classify.

**Bad:** create one global `Commutative` node because Sage happens to reuse that axiom spelling across unrelated theories.

**Preferred:** `Groups.Commutative`, `Rings.Commutative`, a lattice-poset classifier, etc. are classifier applications whose actual mathematics is determined by the host/defining morphism.  Transport a classifier to another category via the corresponding pullback when that is the mathematics; do not identify classifiers by string.

#### `STY-185`: Readable name for a pullback/refinement -> independent species -> retain the defining category expression

**Bad:** mint `FiniteRings`, `GradedAlgebras`, `BasedModules`, etc. as unrelated categories merely because a readable plural name is convenient.

**Preferred:** first represent the actual expression, e.g. `Rings.Finite` or `Algebras(R).Graded`, with the appropriate classifier/pullback structure.  A standard established plural may be registered as the public name/alias of that same identity; the name does not replace or duplicate the construction.

#### `STY-186`: Generated “certificate/evidence/status” artifact for facts derivable from live code -> live semantic structure plus on-demand report

**Bad:** add a per-object certificate/attestation JSON, proof-metadata ABC, generated status ledger, or stored compliance manifest whose fields are all recomputable from category placement, MRO, constructors, functors, and runtime behavior.

**Preferred:** put the actual invariant into the type/category/constructor language; verify live behavior with mathematical specimens or the host's native conformance mechanism; generate any human-readable inventory on demand.  Store only genuinely authored mathematical design commitments that cannot be derived from the live system.  Do not create a second ledger that must be synchronized forever.

#### `STY-187`: Category constructibility decided by graph reachability/name lookup -> derive canonical structural maps

**Bad:** say a category/refinement is “constructible” because a named node exists or because BFS finds some path through an implementation graph; traverse projection arrows backwards to manufacture structure.

**Preferred:** use the owned category expression/finite-limit grammar: canonical structural maps compose in their declared direction; classifiers/refinements are introduced only when the required map to their host exists; pullback/classifier constructions create their own projections.  Constructibility is derivability in this typed structural calculus, not arbitrary graph connectivity.

### Review rule for new imperative code

Before accepting a new global helper, explicit `for`/`while`, mutable accumulator, cache, registry, runtime probe, or bespoke data structure, check the catalogue above and answer:

1. Which mathematical object owns this operation?
2. Can the user discover it from that object with tab completion?
3. Is this exactly map/filter/fold/search/group/flatten/count/queue/traversal syntax already named by Python or a dependency?
4. Is there already a repository abstraction for the same mathematical operation?
5. Does the same skeleton occur elsewhere, implying a missing abstraction rather than several loops to shorten?
6. Can the computation remain lazy or finite-support instead of materializing a whole family?
7. Is the loop genuinely stateful mathematics/algorithmics?  If yes, keep it explicit and use the standard worklist/data structure.
8. Does adding this specialized feature force an ancestor to import or name the descendant?  If yes, recheck dependency direction.
9. Does a backend already own the generic algorithm?  If yes, delegate and cross back.

A construct that survives these questions is allowed.  The catalogue exists to make the routine cases routine and to keep review attention on the mathematics.

* * *


## Policy Index

| Family | Governs |
| --- | --- |
| `ARC-*` | mathematical architecture and ownership |
| `API-*` | the public mathematical surface of owned objects |
| `CON-*` | constructors, witnesses, actions, and structural transport |
| `CAT-*` | category placement, chosen data, and computational capability |
| `DEF-*` | definitions, predicates, structural results, and special cases |
| `LEX-*` | mathematical vocabulary and public type names |
| `SET-*` | mathematical collections, underlying sets, and cardinality |
| `ENG-*` | delegation of heavy computation to exact engines |
| `BND-*` | private engine crossings and representation boundaries |
| `BRG-*` | external-system interoperability and bridge transport |
| `ENV-*` | repository execution and environment conventions |
| `DEV-*` | development, verification, migrations, and policy promotion |
| `STY-*` | corrective implementation style and declarative Python patterns |

### 1. Mathematical Architecture & Ownership (`ARC-*`)

#### `ARC-00`: The Preamble Is a Closed Mathematical Universe

- **Rule**: Once code enters the public preamble API, it remains in the preamble universe.
  The preamble does not extend Sage, wrap Sage's public object model, or provide an interoperability layer with ordinary Sage objects.
  It is an independent mathematical system built on top of computational services such as Sage, Singular, GAP, Julia, OSCAR, or Macaulay2.
  Every publicly constructible parent, element, morphism, category, subobject, tensor, ideal, group, ring, module, algebra, scheme, and derived construction is a preamble object and composes only through preamble APIs.

- **Rationale**: The backend boundary is an implementation boundary, not part of the mathematical language available to users or ordinary repository code.
  If a mathematical operation must leave the preamble universe in order to continue, then the missing result, operation, or construction belongs in the preamble and must be owned there.
  Backend choice must be replaceable without changing any caller-visible object, element, signature, or method.

- **Violation Example**: Treating preamble `ZZ` as a view of Sage `ZZ`; `from sage.all import *` inside the public preamble session; leaving Sage's preparser binding `Integer` or `RealNumber` to raw Sage element constructors; returning a Sage integer, vector, ideal, group element, matrix, or homset from a public operation; requiring callers to construct a Sage object and pass it into a preamble constructor; documenting a method as "use Sage's object here"; exposing an engine so downstream code can continue the computation outside the preamble.

- **Correct Example**: `ZZ(3)` is an element of preamble `ZZ`; the session's integer-literal constructor resolves to that same owned integer construction; `ZZ**2` has preamble module elements; `Groups.C(4)` has preamble group elements.  A Smith-form implementation may privately translate these objects to Sage `ZZ`, Sage free modules, and FGP data, but the caller sees only preamble inputs and preamble outputs.

#### `ARC-01`: Own Universal Properties and Categories Natively

- **Rule**: Define mathematical categories, morphisms, functors, adjunctions, and universal constructions natively in the repository category framework.

- **Rationale**: Categories and universal properties establish the semantic mathematical foundation.
  They provide consistent compositional behavior across modules.

- **Violation Example**: Defining an ideal or basis as an isolated tuple or matrix operation without an underlying category, module, or algebra structure.

#### `ARC-02`: Morphism-Centric Subobjects and Witness Placement

- **Rule**: Represent subobjects as pairs $(S, \iota: S \hookrightarrow M)$.
  Place predicates, isometries, embeddings, and containment checks on morphism spaces or hom-sets.

- **Rationale**: Mathematical invariants depend on the embedding morphism, not on presentation-dependent coordinate choices.

- **Violation Example**: Storing ambient coordinates or adding `ambient=` parameters directly to parent objects.

#### `ARC-03`: Build Structural Objects Before Downstream Numerical Invariants

- **Rule**: Never bypass an intermediate mathematical object or functorial stage (such as the localized module $M_{\mathfrak{p}} = M \otimes_R R_{\mathfrak{p}}$, base-changed algebras $K \otimes_R \mathcal{O}$, or derived complexes) to compute a single numerical scalar or pointwise fiber (such as $\dim_{\kappa(\mathfrak{p})}(M \otimes_R \kappa(\mathfrak{p}))$). Always construct the foundational parent object and base-change/localization functor first; derive pointwise invariants as generic operations on the resulting object.

- **Rationale**: Bypassing structural objects destroys mathematical compression and composability.
  When the structural object exists ($M_{\mathfrak{p}}$ as an $R_{\mathfrak{p}}$-module), all local invariants (rank, minimal generators, local torsion, localization of morphisms) become generic consequences of base change.
  Skipping to point queries forces every downstream invariant to reinvent ad-hoc algorithmic logic.

- **Violation Example**: Implementing `local_number_of_generators(p)` by evaluating the residue field vector-space dimension $M \otimes_R \kappa(\mathfrak{p})$ while the localized module $M_{\mathfrak{p}}$ over the local ring $R_{\mathfrak{p}}$ remains absent from the category layer.

#### `ARC-04`: Owned Objects Over Interchangeable Computational Services

- **Rule**: Mathematical objects, elements, morphisms, categories, subobjects, universal properties, and functors are owned.
  Sage/Singular/GAP/Julia/OSCAR/M2/etc. are interchangeable computational services behind those objects.
  The preamble neither subclasses their mathematical universe nor exposes it as an alternate API.
  No CAS-specific object, element, category membership, constructor, or coercion is needed to state, construct, or use preamble mathematics.

- **Rationale**: The owned category graph is the single surface for stating what an object is.
  A computational engine only supplies computations behind that surface, so the engine choice never enters the statement of the mathematics, and engines remain swappable.

- **Violation Example**: Requiring a CAS-specific category membership or class (Sage, Singular, GAP, OSCAR, or Macaulay2-specific) to state, construct, or identify an object.

#### `ARC-05`: Owned Parents and Elements Are Outside Every Engine

- **Rule**: An owned mathematical object is a parent constructed through the owned category chain, and its elements are elements of that owned parent.
  Backend parents and backend elements are private computational representations only.
  No Sage/Julia/GAP/OSCAR object is the public parent or public element merely because an internal algorithm delegates to that system.
  No backend constructor receives an owned parent or owned element directly; private adapter code first converts every input to backend representations.

- **Rationale**: Ownership is a firewall around the whole mathematical universe, not only around parent objects.
  If an owned parent returns Sage elements, then Sage's element parent, coercion graph, methods, and representation remain part of the effective public ontology even when the parent itself is nominally owned.
  That is the same ownership inversion at the element level.

- **Violation Example**: `ZZ(3).parent() is SageZZ`; an owned free module whose `module_generator(i)` is a Sage free-module element; an owned group whose `group_generators()` are GAP/Sage group elements; passing an owned ring element directly to `FGP_Module`, `FreeModule`, or a GAP constructor.

- **Correct Example**: Owned `ZZ` has owned integer elements.  An owned free module has owned module elements whose coefficients lie in owned `ZZ`.  A private FGP adapter converts the owned ring, presentation matrix, and elements to Sage `ZZ`, a Sage free module, and Sage FGP elements, performs the computation, and converts the answer back to owned elements and morphisms before returning.


#### `ARC-06`: Backend Adoption Creates a New Owned Object; It Is Never Reclassification or a Facade

- **Rule**: Importing or selecting a backend representation constructs or attaches private computational state for an independently owned object.
  It does not reclass the backend parent, expose the backend parent as a facade, or reuse backend elements as the owned object's elements.
  Backend identity is never owned-object identity.

- **Rationale**: Reclassification and facade parenting both leave the backend's ontology in the public object model: reclassification mutates the backend object, while a facade leaves backend elements and coercions authoritative.
  The owned category must instead control parents, elements, operations, equality, morphisms, and public return types; the backend is only an implementation service behind private crossings.

- **Violation Example**: A post-init hook that refines a Sage group in place; `Parent(..., facade=sage_free_module)` for an owned module; `OwnedRingView._element_constructor_` returning `SageZZ(value)`; rebuilding or preserving a Sage Cython element class as the element class of an owned group.

- **Correct Example**: `own_group(G_backend)` returns an owned group with owned group elements and a private conversion between those elements and `G_backend` elements.  `own_free_module(F_backend)` returns an owned free module with owned coefficient-bearing elements and privately records `F_backend` only as an optional computation service.  Neither backend parent nor its elements are changed or exposed.


#### `ARC-07`: A Morphism Is Asked of Its Endpoints

- **Rule**: A Hom object is obtained from its endpoints, `A.Hom(B)`, so the owned `_Hom_` hook of their category chooses the homset.
  A category is named at the call site only when the morphism deliberately lives in a coarser owned category, `Sets().hom(A, B)` for a map of underlying sets.
  A Sage category is never named at a Hom site.

- **Rationale**: Naming a category at the call site restates what the endpoints already know and, when the name is Sage's, asks Sage to admit owned objects it does not hold.
  The endpoints' own category is the single place the choice of homset is made.

- **Violation Example**: `Hom(source, target, Groups())` with owned groups as endpoints; `Hom(base_ring, self, Rings())` inside an owned algebra.

#### `ARC-08`: Engine Availability Does Not Define Mathematical Existence

- **Rule**: The mathematical data of an owned object is sufficient to state and construct that object independently of any computation engine.
  A backend may be present, absent, or replaceable without changing the object's defining mathematical data or identity.
  A backend may establish an additional mathematical property that justifies a valid category refinement, but the backend's class or availability is never itself category data.
  Missing backend support limits a computation; it does not turn the mathematical object into a backend object or make the object cease to exist.

- **Rationale**: A chosen presentation `F_1 -> F_0 -> M`, for example, already defines the presented module.
  A Sage FGP module can accelerate Smith-form computations when the coefficient ring admits that engine, but it is not the definition of `M`.
  Keeping those facts separate makes backend choice genuinely optional and interchangeable.

- **Violation Example**: Refusing to construct a presented module because Sage cannot build an FGP module over its coefficient ring; selecting the public class or category by checking which Sage implementation class happened to be available.

- **Correct Example**: Retain the owned presentation morphism and tensor-valued relation matrix independently of any Smith engine.  Expose an algorithmic method only where its implementation is supplied by category structure, or keep a mathematically general method with an informative assertion stating the stronger mathematical hypothesis under which the current algorithm is total.  Missing engine support is handled at the private engineering boundary, never represented as a mathematical `NotImplementedError` result.

#### `ARC-09`: Fundamental Mathematical Objects Are First-Class Before Their Refinements

- **Rule**: When a standard mathematical object is not already canonically an instance of an owned universal construction, give that object an owned parent and category before implementing any of its specializations.
  When it *is* canonically an existing construction, use that construction rather than minting a parallel parent.
  Additional algebraic, geometric, topological, smooth, scheme-theoretic, group, or representation-theoretic structures are refinements or functorial constructions on the same mathematical object; they do not replace its underlying identity.
  Do not force the object to live as a backend object or one particular richer structure, but equally do not duplicate an object already supplied by `Hom`, `End`, tensor product, quotient, subobject, free object, or another universal construction.

- **Rationale**: A fundamental mathematical object can be the common domain on which many theories meet.
  If it is absent, every higher construction invents its own representation and API, so backend matrix methods appear in tensors, matrix multiplication appears in generic rings, and geometric structure has nowhere canonical to attach.
  Owning that object first lets later category refinements contribute exactly the operations justified by their hypotheses.

- **Violation Example**: Implementing every finite matrix as `tensor.matrix(...)`; returning Sage `MatrixSpace(R,m,n)` for rectangular matrices; creating a second matrix parent even though `Hom_R(F_R([n]),F_R([m]))` already is the canonical matrix object; encoding a matrix scheme or matrix group as a separate unrelated object.

- **Correct Example**: For the canonical finite ordered set `[n]`, `F_R([n])` is the free module with its canonical framing.  Define `M_{m,n}(R)` as the existing Hom object `Hom_R(F_R([n]),F_R([m]))`; its elements acquire matrix entry/row/column/normal-form methods from the Hom category when both endpoints have these canonical framings.  `M_n(R)=End_R(F_R([n]))` inherits composition as multiplication and may acquire further algebra/Lie/geometric refinements without changing object identity.

#### `ARC-10`: Canonical Identifications Are Object Identity, Not Conversion APIs

- **Rule**: When standard notation names an object that is canonically an existing owned construction, implement the notation as that construction itself rather than as a new parent plus conversion maps.
  Preserve the canonical chosen data that makes the identification literal.

- **Rationale**: Parallel parents for canonically identical objects create artificial coercions, duplicate APIs, and force downstream code to choose representations that mathematics does not distinguish.

- **Violation Example**: Creating a distinct `MatrixSpace(R,m,n)` parent plus `as_module_morphism()` even though the canonical framings identify it with `Hom_R(F_R([n]),F_R([m]))`; creating a separate endomorphism-matrix ring instead of using `End_R(F_R([n]))`.

- **Correct Example**: `[n]` is the canonical finite ordered set, `F_R([n])` is the corresponding canonically framed free module, and `MatrixSpace(R,m,n)` returns `F_R([n]).Hom(F_R([m]))` with the matrix-Hom refinement installed.  A matrix element *is* that module morphism; `matrix()` is its coordinate array/object only when such a coordinate view is requested, not another mathematical object.

#### `ARC-11`: Export Aggregators Are Not Architectural Dependencies

- **Rule**: Internal code imports a mathematical construction from the module that defines it, or from a deliberately dependency-light core module for that theory.
  Package `__init__.py` files, session aggregators such as `preamble.all`, catalogues, and convenience export surfaces are leaves of the dependency graph; foundational category/module/ring/algebra code never imports through them.

- **Rationale**: An aggregator describes what a user may import together; it does not state a mathematical dependency.  Using it internally makes every exported higher construction an implicit dependency of every lower one, creates circular imports, and lets import order determine which mathematical structures exist.

- **Violation Example**: `modules/connections.py` importing `KahlerDifferentials` from `categories.algebras.__init__`, while that aggregator imports finitely presented algebras which import the modules package; a core functor importing through `preamble.all`; loading the lattice catalogue before the categories on which its objects depend.

- **Correct Example**: A connection module imports `KahlerDifferentials` from `algebras.kahler_differentials`; the session aggregator imports both only after their defining modules are available.  The dependency graph follows mathematical construction dependencies and is independent of session import order.

#### `ARC-12`: Mathematical Operations Live on Their Mathematical Owners

- **Rule**: Public mathematical operations are methods on the element, parent/object, category, morphism, Homset, functor, or other mathematical object whose structure determines the operation and its admissible inputs.  Do not expose an operation primarily as a free-standing global function when there is a mathematical object from which the operation can be discovered.  If a category `C` has products, `C` owns its product construction, e.g. `C.product(factors)`; if a morphism has a kernel in its category, expose that through the morphism/Hom/category API; if an element has an operation, expose it on the element.  A global helper may exist only as non-primary notation or constructor syntax and must delegate immediately to the owning object.

- **Rationale**: Sage is a discovery-oriented mathematical language.  In an interactive session the user should be able to construct the mathematical object they know, type `<TAB>`, and discover the operations that make sense for that object.  The owning object supplies both namespace and domain information: `C.<TAB>` answers what the category can construct; `M.<TAB>` what the module supports; `f.<TAB>` what can be done with the morphism; `H.<TAB>` what the Homset knows; `x.<TAB>` what operations belong to the element.  A flat global namespace destroys that locality.  Seeing `Product`, `Kernel`, `Orbit`, or `TensorProduct` globally does not tell the user whether the function expects categories, parents, elements, morphisms, finite families, or some mixture, so using the language requires prior knowledge of the entire global API or constant documentation lookup.  This is the GAP/Julia-style failure mode the preamble is specifically intended to avoid.

  Mathematical ownership and implementation dataflow follow from the same rule.  Saying that `C` has products includes teaching the implementation of `C` how its selected products are constructed.  The information flows from `C` to `C.product(...)`, not from a global `Product(...)` dispatcher back into every possible category.  Consequently the code implementing the operation belongs in the subtree for the mathematical owner, and adding the operation to a new category does not require extending a global switchboard.

- **Violation Example**: Exporting a global `Product(X, Y)` leaves its domain unknowable from the name alone: does `Product(x, y)` multiply natural-number elements, form a categorical product of `Sets()` with itself, construct a product of two objects of a category, or accept a family of categories?  Likewise global `Kernel(f)`, `TensorProduct(X, Y)`, `Orbit(G, x)`, or `_morphisms_agree(f, g)` force the user or caller to know an external function catalogue and force the implementation to rediscover the relevant mathematical owner from its arguments.  A stand-alone `Product` that imports modules, sets, schemes, and algebras is one concrete consequence of this wrong API shape, but the free-standing operation is already the primary defect even if its dispatcher were perfectly generic.

- **Correct Example**: Write `C = Sets()` and inspect `C.<TAB>` to discover `C.product(...)`; if `X` and `Y` are objects with `C = X.ambient_category()`, notation such as `X * Y` may delegate to `C.product([X, Y])`.  `Modules(R)` supplies its own product/biproduct method in the module-category subtree; a scheme category supplies its product/fiber-product method in the scheme subtree.  A morphism exposes `f.kernel()` when its category supports kernels; a Homset exposes Hom-level constructions and equality; an element exposes its own operations.  The user discovers valid mathematics by navigating from objects already in hand rather than searching a global language.

#### `ARC-13`: Mathematical Structure Is Independent of Import Order and Call History

- **Rule**: The mathematical structure and category placement of an owned object are determined by its construction data and explicit mathematical refinements, not by which module happened to finish importing first or which accessor was called earlier in the session.
  Do not use import-cycle flags, `ImportError` fallbacks, lazy "try again on the next lookup" installation, or incidental method calls to make standard structure appear on an already existing object.
  A legitimate later refinement must correspond to newly established mathematical data or a proved property, not merely to runtime availability of implementation code.

- **Rationale**: Import order and call history are properties of the Python process, not of the mathematical object.
  If `R` is canonically an `R`-module and `R`-algebra, or an object carries a selected decomposition, those facts cannot depend on whether the module/algebra package had completed importing when `R` was first requested.
  History-dependent mutation makes identical mathematical expressions expose different APIs in different sessions and turns initialization order into hidden state.

- **Violation Example**: `_own_ring()` attempting to install the canonical self-module/self-algebra structure, catching `ImportError`, and deferring that mathematical structure until a later lookup; an accessor that calls `refine(...)` merely because asking the question made another category implementation importable.

- **Correct Example**: Canonical self-structure is part of the ring construction/category packet from the outset, or is supplied by a dependency-safe structure functor whose result is deterministic for the same ring.  A later refinement occurs only when a new chosen datum is attached or a mathematical predicate has actually been established.

#### `ARC-14`: Equivalent Universal Data Has One Authoritative Representation

- **Rule**: When standard mathematics gives equivalent presentations of the same universal structure, choose one authoritative datum and derive the others mechanically.
  Do not require subclasses or sibling implementations to independently encode mutually determining units, counits, Hom-set bijections, opposite/product-domain functor machinery, or parallel Hom-like parents for the same universal object.

- **Rationale**: Equivalent formulations are mathematical compression.  Implementing every equivalent formulation independently creates coherence obligations that the mathematics already solves and multiplies LOC without adding expressive power.
  The derived interfaces should be consequences of one structure, not separate sources of truth that can drift apart.

- **Violation Example**: Every adjunction subclass independently implementing `unit`, `counit`, `hom_set_isomorphism_forward`, and `hom_set_isomorphism_inverse`; a separate `ContravariantFunctor` reimplementing functor caching and endpoint checks instead of using a functor on `C^op`; a separate `Bifunctor` object model instead of a functor on `C x D`; represented pairings using a second `PairingSpace` even when `Hom_R(X tensor Y, W)` exists.

- **Correct Example**: An adjunction records one standard presentation—e.g. the adjoint functors with unit and counit—and derives the Hom bijection by composition, with triangle identities tested as the coherence law.  Contravariant and bifunctor convenience syntax delegates to ordinary `Functor` on the owned opposite/product category.  A represented bilinear pairing is literally an element of `Hom_R(TensorProduct(X,Y), W)`.

#### `ARC-15`: Upward Knowledge of Descendants Is an Architectural Smell

- **Rule**: Treat knowledge flowing from a general category, construction, or foundational module toward one of its specialized descendants as suspicious by default.  This is a code-smell heuristic, not an absolute prohibition: there are legitimate exceptional cases, but a supercategory or generic construction should normally not import, name, enumerate, or branch on its subcategories.  Adding a new specialized category should ordinarily consist of adding a modular subtree whose imports point inward toward existing foundations; it should not require edits to unrelated ancestors merely so they learn that the new category exists.

- **Rationale**: Category inheritance and mathematical specialization are naturally extensible when dependencies point from specialized theories toward the general structures they refine.  If an ancestor must know every descendant, the blast radius of adding one new research category grows with the size of the entire hierarchy, generic code accumulates special cases, and independent subtrees cease to be independently loadable or maintainable.  The smell is especially strong when a generic construction such as products, Homs, kernels, scalar extension, or equality must be edited to mention a highly specialized descendant.

- **Smell Example**: `Cat.Products` or another generic categorical layer importing `MyVerySpecialResearchLatticeCategory` so that products work there; `Modules(R)` importing a particular arithmetic-lattice subcategory merely to recognize it; a root construction maintaining a registry or conditional chain of every specialized theory that supports it.

- **Healthy Shape**: `MyVerySpecialResearchLatticeCategory` imports the general category machinery, declares its supercategories, and supplies its specialized methods/refinements inside its own subtree.  Existing ancestors remain unchanged.  Imports therefore flow from the specialized subtree toward the stable foundation, while generic ancestors stay oblivious to the existence of the new descendant unless there is a specific mathematical reason otherwise.

#### `ARC-16`: Finitary Coordinates Are Computational Specializations, Not the Mathematical Architecture

- **Rule**: State objects and operations through their mathematical semantics first: owned sets/families, finite-support elements, Homs, subobjects, kernels/images, products/coproducts, actions, quotients, tensor constructions, and universal maps.  Finite enumeration, bases, coordinates, rows/columns, block matrices, and exhaustive checks are algorithms/representations supplied underneath those objects.  Ordinary mathematical consumers do not lower to finite coordinates merely because today's easiest algorithm is finite.

- **Rationale**: Premature lowering makes finiteness contagious.  Once cohomology, exactness, intersections, actions, or divisor groups know about row counts and Python tuples, extending the underlying object to an infinite framing or a theorem-backed representation requires rewriting every consumer.  A semantic layer localizes the finite assumption: a finite-free Hom may use matrices while an infinite Hom later uses formal blocks, sparse operators, callable maps, or another theorem/engine without changing callers.

- **Violation Example**: `FreeResolution.is_exact()` comparing backend row modules instead of image and kernel subobjects; `Cohomology` rebuilding cycles/boundaries from basis matrices; a formal divisor group forcing its entire prime-divisor index set to be finite because individual divisors have finite support; constructing a block morphism by concatenating finite row arrays.

- **Correct Example**: State exactness as `im(d_1)=ker(epsilon)`, cohomology as `ker(d_n)/im(d_{n-1})`, subobject intersection as a pullback, and a divisor group as the free module on its owned prime-divisor set with finite-support elements.  The finite represented cases dispatch internally to matrix/Sage/Singular algorithms; future infinite cases supply different implementations of the same semantic methods.


#### `ARC-17`: Repair the Semantic API Before Writing a Local Numerical Workaround

- **Rule**: When a consumer needs a mathematical result canonically expressed through an owned semantic construction, the consumer calls that construction. It does not extract coordinates, matrices, rows, columns, basis vectors, engine objects, or finite presentations and reimplement the construction locally. If the required semantic method is missing, incomplete, or awkward to compose, improving that lower-level API is part of the implementation task. Do not preserve a local numerical workaround merely to keep the patch geographically small.

- **Rationale**: A common LLM failure mode is **myopic semantic lowering**: receive an honest mathematical object, immediately forget its semantics, compute on a convenient finite representation, and reconstruct an approximation to the mathematical result. One such patch looks harmless; dozens produce a second numerical implementation layer scattered through consumers. Every consumer then learns finiteness, basis choice, row/column conventions, matrix algorithms, and backend details, so an infinite or theorem-backed implementation requires a repository-wide rewrite. The semantic API is the compression boundary: only `kernel`, `cokernel`, `image`, `pullback`, `quotient`, `torsion_subobject`, `is_torsion_free`, `dimension`, `Hom`, and analogous owners should know how their current representations are computed.

- **Violation Example**: Given `f : M -> N`, call `f.matrix()`, compute a backend nullspace, construct a free module on the nullspace rows, and manufacture an inclusion into `M`. This duplicates `f.kernel()` and hard-codes finite free coordinates in the caller. Likewise, decide whether an inclusion is primitive by taking gcds/minors of its matrix rather than asking whether its cokernel is torsion-free.

- **Correct Example**: `K = f.kernel()` returns the owned kernel together with its inclusion. A subobject inclusion `i : S -> M` is primitive exactly when `i.cokernel().is_torsion_free()`. The finite-free implementation of `kernel()` or `is_torsion_free()` may privately use nullspaces, Smith form, or determinants; an infinite implementation may use a theorem, sparse operator, formal presentation, or another engine. The consumer does not change.
  The live `ModuleMorphism.is_primitive()` already has the right shape: it asks injectivity and then returns `self.cokernel().is_torsion_free()`. Treat this as a model for structural predicates rather than replacing it with a matrix criterion in specialized consumers.

- **Extension Test**: After writing a consumer, mentally replace every finite-rank object by a plausible infinite analogue. If the consumer itself must change because it knows about matrix sizes, complete bases, exhaustive generator lists, or backend rows, the numerical boundary is probably too high. If only a low-level semantic method needs a new case, the architecture is correctly localized.


#### `ARC-18`: The Interface Is Judged by the Invalid Mathematics It Permits

- **Rule**: Design public constructors and methods adversarially against representation shortcuts.  A semantic API is insufficient if an equally public coordinate/vector/matrix path lets downstream code bypass the mathematical object and reimplement its theorems locally.  Close or privatize such hatches; force callers through parents, elements, Homs, structure morphisms, universal constructions, and owned collections.

- **Rationale**: Encapsulation by convention does not survive repeated local implementation pressure.  An exposed numerical representation becomes training data for the next patch, and each patch silently acquires theorem hypotheses, basis conventions, and finite assumptions.  Semantic gating concentrates those proof obligations once.  The interface is therefore evaluated by asking not only “can correct mathematics be expressed?” but also “what plausible nonsense does this API make easy to express?”

- **Violation Example**: A public lattice element constructor accepts arbitrary coordinate lists; an owned morphism exposes a convenient raw matrix accessor used by ordinary consumers; a group action constructor accepts raw matrices without first constructing `rho:G->Aut(M)`.

- **Correct Example**: Elements are formed in their parent from named/owned generators and finite-support mathematical data; matrix data may enter only at the narrow finite-framed Hom construction that returns a genuine morphism; all downstream operations stay on that morphism.  Assertions at likely misuse sites explain the mathematical ambiguity and name the correct construction.


#### `ARC-19`: Formulate at the Generality That Survives Relaxing a Hypothesis

- **Rule**: Define each mathematical notion at the weakest natural hypotheses under which its definition remains valid, then recover stronger cases by parameter, axiom, subcategory, chosen structure, or algorithmic specialization.  Before accepting an interface, test it conceptually by removing common accidental assumptions: finiteness, finite generation, freeness, projectivity, orderedness, enumerability, commutativity, and concrete coordinate realization.

- **Rationale**: Overfitting the definition to today's fixtures or backend makes every later generalization a migration.  A mathematically general semantic owner localizes future work: the finite/free case can have an optimized implementation without teaching every consumer that those hypotheses exist.  Extreme examples are design tests, not necessarily currently computable workloads.

- **Violation Example**: Define a framed module only for a finite ordered basis because the first implementation uses matrices; define a free module only from an integer rank; define formal divisors only over a finite list of possible prime divisors; place an operation on lattices when its definition only uses module structure and a form morphism.

- **Correct Example**: A framing is a selected epimorphism `Free_R(S) -> M` for an arbitrary set `S`; `[n]` is the canonical finite ordered specialization.  Individual elements have finite support even when `S` is infinite or nonenumerable.  Finite matrix realizations and rank-based algorithms live in the finite/framed subcategories while callers retain the same semantic construction.

- **Sweep Question**: “If I drop one hypothesis from the current examples, does the definition still make sense?”  If yes, that hypothesis belongs to an implementation/subcategory, not the definition.



#### `ARC-20`: Structured Objects Include Their Witnessing Arrows

- **Rule**: When the mathematical object is a subobject, quotient, image, re-presentation, or other structured occurrence of an underlying object, the witnessing morphism is part of the mathematical data and therefore part of identity/equality at that structured level.  Do not collapse the structured object to its underlying abstract object or to the image subset suggested by a coordinate realization.

- **Rationale**: A subobject of `Y` is represented by a monomorphism `i:X -> Y`; two copies of the same abstract `X` embedded by different monomorphisms are distinct subobjects.  Dually, quotients remember the epimorphism `Y -> Q`.  Forgetting the arrow loses exactly the relationship that downstream constructions—intersection, saturation, quotienting, pullback, factorization—consume.

- **Violation Example**: Compare subobjects only by their domains or Gram data; identify `L` with the image of `L -> L^#`; compare quotients only by invariant factors while ignoring the quotient maps.

- **Correct Example**: Subobject equality is equality in the owned subobject/slice construction and includes the inclusion; quotient equality includes the projection.  The underlying-object forgetful operation may return equal/isomorphic abstract objects without making the structured objects equal.


#### `ARC-21`: Categories of Arrows, Homs, and Functors Are First-Class Objects of `Cat`

- **Rule**: Treat `Ar(C)`, `Fun(C,D)`, Hom categories, endomorphism/automorphism arrow categories, cores, slices, coslices, and analogous category constructions as actual owned objects of `Cat`, not as implementation namespaces around special Python classes.  Their objects/elements inherit ordinary categorical structure through the same graph as every other category.

- **Rationale**: A morphism is an element of a Hom object, Hom objects themselves participate in arrow-category structure, and functors/natural transformations form ordinary categories.  Making these constructions first-class centralizes method inheritance and eliminates parallel “morphism methods” or “functor utility” mechanisms that bypass the category graph.

- **Violation Example**: Treat morphisms as a third API species unrelated to Hom elements; attach special methods directly to a morphism wrapper because arrow categories are not represented; implement `Fun(C,D)` as a utility registry rather than a category.

- **Correct Example**: `Ar(C)` and `Fun(C,D)` are owned categories; `Hom_C(A,B)` is the appropriate owned Hom/category object; `End`/`Aut` refinements and their elements inherit through the same categorical construction machinery.  Convenience aliases may expose familiar syntax without creating a second ontology.


#### `ARC-22`: Inherited Mathematics Propagates Through Named Functors and Composition

- **Rule**: When a structured category obtains operations from a less-structured mathematical object, represent the passage by the appropriate owned functor and let operations propagate through composition.  Do not make every descendant independently reimplement obligations from `Sets`, modules, groups, or another underlying structure, and do not confuse a faithful/forgetful functor with literal object identity or a backend inheritance edge.

- **Rationale**: The same module can be viewed through its underlying additive group and set without those categories being identical.  A named functor records exactly what structure is forgotten and gives one route for cardinality, iteration, set maps, and other inherited operations.  Composition creates rollup points where a whole family of obligations is discharged once rather than leaf-by-leaf.

- **Violation Example**: A lattice implements `cardinality()` independently of its underlying module/set; every algebraic category duplicates set iteration; Python MRO order silently chooses one of several possible forgetful routes.

- **Correct Example**: Lattice structure maps to the underlying module by an owned functor, module structure maps toward its underlying set, and generic set operations are answered there.  Alternative canonical routes either coincide by construction or are related by an owned natural isomorphism; MRO order never decides the mathematics.

#### `ARC-23`: Additional Structure Refines One Mathematical Object; It Does Not Create Wrapper Ontologies

- **Rule**: Prefer one generic owned representation of a mathematical object together with categorical refinements for additional properties/structure.  Do not create a new concrete wrapper class for every combination of symmetric, alternating, integral, torsion, group-equivariant, graded, or similar refinements when the underlying datum is the same object plus additional structure/properties.

- **Rationale**: Parallel wrapper classes duplicate element behavior, Hom behavior, equality, construction, and backend conversion while obscuring the common object.  Category refinement lets one represented form/module/etc. acquire exactly the additional operations justified by its structure without changing identity or forcing conversions between wrappers.

- **Violation Example**: Separate concrete classes `SymmetricBilinearForm`, `IntegralBilinearForm`, `GroupLatticeForm`, and `TorsionBilinearForm` each storing the same module/form data and copying methods.

- **Correct Example**: Use one generic represented form/morphism object and one formed-module construction; refine it into symmetric/integral/nondegenerate/lattice/group-action categories as the defining data establishes those properties.


#### `ARC-24`: Structural Functors Are Outputs of Category Constructions, Not a Parallel Hand-Written Graph

- **Rule**: A named category expression—root, classifier application, product/pullback, slice/coslice, core, or other owned construction—is authoritative.  Canonical projection/forgetful/structural functors implied by that expression are derived from the construction and composed recursively.  Do not maintain a second manually authored “forgets-to” or preferred-path graph encoding the same relationships.

- **Rationale**: If `C.A` is defined by a classifier pullback over `C`, the projection `C.A -> C` is part of the mathematical definition.  Re-entering that edge in a separate registry duplicates truth and invites mismatches between category identity, method inheritance, and functor routing.  Structural recursion also makes adding a new category expression local rather than requiring registration in every ancestor/path table.

- **Violation Example**: Add `forgets_to = Modules(R)` beside a category whose defining expression already projects to modules; maintain BFS/preferred-functor tables for ancestor routes that the category expression canonically composes; hand-author every axiom projection.

- **Correct Example**: classifier/category constructors create their primary structural maps; `project(C.A,K)` composes the primary projection with `project(C,K)`.  Explicit alternative functors remain first-class when they are genuinely different mathematics, rather than entries in a duplicate hierarchy table.


#### `ARC-25`: Formed Mathematics Starts With the Arbitrary Form Actually Carried by the Object

- **Rule**: In formed-module/lattice mathematics, the base semantics use the declared bilinear/quadratic/sesquilinear form itself.  Do not silently import the standard Euclidean inner product, positive definiteness, nondegeneracy, or finite-dimensional coordinate geometry.  Additional hypotheses refine the category exactly where the mathematical notion requires them.

- **Rationale**: CAS vector APIs are saturated with Euclidean defaults (`dot_product`, standard norms, projections, Gram-Schmidt) whose answers are unrelated to an arbitrary form on the same underlying module.  Letting those operations leak into general formed code is a pervasive silent-wrongness source and makes degenerate/indefinite/infinite analogues impossible without rewriting consumers.

- **Violation Example**: Compute orthogonality by a backend vector dot product rather than `b`; define all lattices as nondegenerate because dual-coordinate code needs an inverse Gram matrix; use a positive-definite shortest-vector routine as the meaning of `roots()` or `norm()` on the base category.

- **Correct Example**: pairings/norms route through the owned form/correlation; radical and orthogonal complement are morphism/subobject constructions; positive-definite reduction/shortest-vector algorithms live behind the definite refinement while the general formed object remains valid for arbitrary forms.


#### `ARC-26`: Category, Object, Runtime Representation, and Presentation Are Distinct Levels

- **Rule**: Keep distinct the mathematical category, an object of that category, the runtime type representing such objects, the owned/Sage category structure attached to that runtime type, chosen presentation data, and property-cut subcategories.  Equivalences or convenient representations do not collapse these levels into one noun or one identity relation.

- **Rationale**: Chosen enumeration/basis data can represent a finite set/free module without being the category itself; a runtime class can represent category objects without being the category; an object and its chosen presentation can be equivalent while carrying different structure.  Collapsing the levels promotes implementation choices into ontology and makes later changes of representation appear to change the mathematics.

- **Violation Example**: Call the Python class of bundled finite-set objects “the category of finite sets”; identify finite free modules with based modules because a basis exists by choice; treat `Cat.of(SomeType)` as the mathematical category rather than one representation of its objects.

- **Correct Example**: explicitly name the owned category and its morphisms, the objects it contains, the generated `ObjectType`/`ElementType` used at runtime, and any framing/enumeration/presentation as additional data/refinement.


* * *

### 2. Public Mathematical API (`API-*`)

#### `API-01`: Public Methods Return Owned Mathematics, Never Backend Objects or Elements

- **Rule**: Every public method on an owned object returns a value in the owned mathematical ontology.
  Public methods never return a Sage module, Sage submodule, Sage vector, Sage matrix, Sage/GAP/Julia element, GAP model, engine pointer, engine parent, or another backend structure merely because that representation is convenient internally.
  Elements returned by an owned parent are owned elements parented by that owned parent.
  There is no public engine accessor or public engine-element escape hatch.

- **Rationale**: Once a raw backend parent or element escapes, every consumer can speak the engine's ontology and the category layer no longer controls what can be stated.
  Public ownership therefore includes element identity and return types, not only method names on the parent.

- **Violation Example**: Public `cover()`, `relation_submodule()`, `coordinate_vector()`, `optimized()`, or `engine()` methods returning Sage objects from an owned presented module; `module_generator(i)` returning a Sage vector; `group_generators()` returning GAP/Sage elements; returning `kernel.V()` or a Sage submodule from an owned Hom computation.

- **Correct Example**: `presentation()` returns the owned relation morphism, `presentation_matrix()` returns a tensor, `module_generator(i)` returns an element parented by the owned module, `group_generators()` returns elements parented by the owned group, `smith_form_module_generators()` returns owned module elements in an owned set, and `invariant_factor_form()` returns an owned isomorphism.


#### `API-05`: Public APIs Accept Preamble Data, Never Raw Backend Objects

- **Rule**: The public boundary is closed on inputs as well as outputs.
  A public constructor or method does not accept a raw Sage/Singular/GAP/Julia/OSCAR/Macaulay2 parent, element, vector, matrix, ideal, morphism, category, or handle as an alternate input form.
  There are no convenience constructors whose purpose is to adopt, wrap, refine, or coerce a backend object into the preamble universe.
  Backend representations are created only by private adapters from already-owned preamble data.

- **Rationale**: Accepting raw backend data makes the backend object model a second public constructor language and forces public code to decide how backend identity, categories, coercions, elements, and chosen data map into owned mathematics.
  That is the same backdoor as returning backend data, only on ingress.

- **Violation Example**: Public `own_ring(SageZZ)`, `own_group(SagePermutationGroup(...))`, `refine_free_module(SageFreeModule(...))`, `FinitelyPresentedModule(sage_submodule)`, or a morphism constructor that accepts a Sage `Map` as a supported public datum.

- **Correct Example**: Public `PolynomialRing(ZZ, "x")`, `FreeModule(ZZ, 3)`, `Groups.S(4)`, `FinitelyPresentedModule(presentation_morphism)`, and `A.Hom(B)(...)` consume preamble objects and mathematical data.  Any Sage/GAP representation needed to execute them is selected and constructed privately after the public call has crossed the API boundary.

#### `API-02`: Coordinates Are Framing Data; Coordinate Objects Keep Their Mathematical Type

- **Rule**: Coordinates of an element are exposed through the chosen framing as the owned `module_coefficients` map.
  When an algorithm genuinely requires an ordered coordinate array, use the owned object whose mathematics describes that array.
  A coordinate vector may be a typed tensor when only variance/index data is intended.  A matrix of a linear map between finitely generated framed free modules is the corresponding Hom element
  `Hom_R(F_R(S), F_R(T))`, framed by the matrix units indexed by `T × S`; it is not replaced by a tensor or backend matrix.
  A public coordinate operation never returns a Sage vector or Sage matrix.

- **Rationale**: Coordinates depend on chosen framings, but the coordinate object can itself have intrinsic mathematics.
  Raw backend arrays erase that structure; treating every array as a tensor erases it in a different way.
  The coefficient map records the framing, tensors record variance when that is the intended structure, and matrices retain their canonical Hom interpretation.

- **Violation Example**: `M.coordinate_vector(x)` returning `M_engine.V().coordinate_vector(...)`; representing `Hom_R(R^n,R^m)` by `tensor.matrix(...)`; passing a raw Sage matrix downstream to reconstruct a morphism later.

- **Correct Example**: Use `module_coefficients(x, M)` for the finite support of an element.  Use a typed tensor for a genuine tensor coordinate array.  For finite framed free modules, `MatrixSpace(R,m,n)` is literally `Hom_R(F_R([n]),F_R([m]))`, and a matrix element is that module morphism itself.

#### `API-06`: The Session Namespace and Literal Constructors Are Owned

- **Rule**: The public session module exports only preamble mathematics and ordinary Python support objects explicitly chosen by the preamble.
  It never wildcard-imports a backend namespace.
  Interactive literal constructors installed or consulted by the host parser/preparser (`Integer`, `RealNumber`, complex-number constructors, generator syntax hooks, and analogous names) resolve to preamble-owned constructions or ordinary Python literals according to the preamble language contract.

- **Rationale**: A closed object universe cannot be enforced only at method signatures if the session itself still publishes backend constructors or silently creates backend elements before the first preamble call.
  The parser is part of the public mathematical language.

- **Violation Example**: `from sage.all import *` followed by selectively shadowing a few names; leaving `Integer(3)` as Sage's integer while `ZZ(3)` is owned; allowing `matrix(...)` to remain Sage's constructor because no owned matrix spelling has shadowed it yet.

- **Correct Example**: The session binds `Integer` to the owned integer constructor, binds `MatrixSpace`/matrix notation to the matrix-Hom construction, and omits backend constructors that have no owned preamble meaning.  Backend imports remain module-private implementation dependencies.

#### `API-07`: The Global Session Namespace Is Not an Operation Catalogue

- **Rule**: Keep the public session namespace sparse in mathematical operations.  Global names are appropriate for canonical mathematical objects, category/object constructors, notation entry points, and deliberately chosen **session-language conveniences**; ordinary mathematical operations on already-constructed objects belong to methods on their mathematical owners.  Do not export a free-standing `Product`, `Kernel`, `Orbit`, etc. merely to shorten `owner.operation(...)` or to reproduce a GAP/Julia-style global operation catalogue.

- **Rationale**: Tab completion on a global namespace scales with the entire library and provides no type/domain context.  Tab completion on an owned mathematical object is contextual documentation: the receiver already tells the user what kind of mathematics is being acted on and narrows the valid operations before any documentation is opened.  A small personal preamble may still deliberately include obvious ergonomic forms such as `lmap`/`lzip`; those are language conveniences, not alternative homes for mathematical operations that already have an owner.

- **Violation Example**: Adding `Product`, `Coproduct`, `Kernel`, `Cokernel`, `Orbit`, `Stabilizer`, `DirectSum`, `BaseChange`, `Dual`, or analogous operation functions to `preamble.all` so users call them by remembering global spellings.  Even if each function internally performs perfect categorical dispatch, the public interface still requires the user to know which arguments make each global meaningful.

- **Correct Example**: The session exposes `Sets`, `Modules`, `Groups`, rings such as `ZZ`, constructors needed to create mathematical objects, and a small deliberate set of obvious personal conveniences such as `lmap` and `lzip`.  From mathematical objects the user discovers `C.product`, `M.base_change`, `f.kernel`, `G.orbit`, `G.stabilizer`, Hom-level operations, or element methods by tab-completing the object in hand.

#### `API-08`: Session Use Is First-Class Use

- **Rule**: Do not classify a public preamble name as dead merely because repository source and tests do not call it.  The preamble exists to populate notebooks and REPL sessions, so deliberate session-only constructors, aliases, formatting helpers, and convenience functions are first-class API even when their internal call count is zero.  Before deleting an apparently unused public name, determine whether it is intentional session vocabulary and inspect its export/documentation history.

- **Rationale**: Static internal call graphs measure implementation reuse, not interactive usefulness.  A convenience such as `lmap(f, xs)` can be valuable precisely because a researcher types it at a prompt rather than because backend code imports it.  Treating all internally unused names as dead would systematically erase the purpose of a preamble.

- **Violation Example**: Running `rg lmap src tests`, finding only its definition, and deleting it as dead code without checking whether `preamble.all` is intended to expose it in research sessions.

- **Correct Example**: Keep a deliberate session helper with obvious stable semantics, export it from `preamble.all`, and assess it as part of the interactive language.  Remove a public name only after establishing that it is neither used internally nor intended as session vocabulary.

#### `API-09`: Interactive Representation Shows the Mathematical Element, Not Its Storage Coordinates

- **Rule**: Ordinary `repr`/LaTeX of owned elements should display the mathematical expression in the object's selected symbols/structure rather than a Python tuple, backend vector, flattened coordinate array, or implementation class.  Coordinate representations are explicit derived views through the selected framing and are never allowed to become the default identity of the element.

- **Rationale**: The first thing a researcher sees in a notebook trains how the object is conceptualized.  Printing `(1,2)` for elements of two different framed modules makes equal coordinate strings look like equal mathematical objects and encourages downstream coordinate programming.  A formal linear combination keeps the parent/framing semantics visible.

- **Violation Example**: A lattice element prints as `[1, 2]`; a quotient element prints only its Smith-coordinate vector; a generic module printer applies integer sign tricks that assume an ordered coefficient ring.

- **Correct Example**: An element of `Free_R(S)` renders as its finite formal `R`-linear combination of the actual symbols in `S`, using each coefficient/symbol's own representation.  Explicit `module_coefficients(...)` exposes coordinates when the researcher asks for them.

#### `API-10`: Public Mathematical Signatures Are Closed and Precise

- **Rule**: Public mathematical constructors and methods enumerate the exact mathematical inputs they accept and the mathematical result they return.  Do not expose arbitrary `*args`/`**kwargs` option bags, backend constructor passthrough, sentinel-driven polymorphism, or mode flags that change mathematical meaning/return shape.  Split genuinely different constructions into named methods/constructors or precise source-grounded overloads.

- **Rationale**: An open option bag delegates the definition of the preamble API to whichever backend version happens to receive it and hides required hypotheses/choices from both tab completion and static inspection.  Sentinel/mode polymorphism makes one name denote several different mathematical operations and encourages downstream branch-heavy handling.

- **Violation Example**: `NumberField(*args, **kwargs)` forwarding Sage's whole constructor surface; `foo(x, ambient=None)` where the optional ambient is actually the missing subobject witness; `normal_form(map=True)` changing the return object from a normal form to `(normal_form, map)`.

- **Correct Example**: provide named constructors for the exact number-field/presentation shapes the preamble owns; make subobject structure an inclusion morphism; return a normal-form isomorphism as the canonical result when the witness is mathematically part of the construction.  Private engine adapters may retain exact protocol-level option forwarding when it is quarantined behind the owned operation.

#### `API-11`: Expose Composable Mathematical Objects, Not Convenience Wrappers Around One Use

- **Rule**: When the useful result is itself a standard mathematical object—an invariant/value object, morphism, action, identity, inclusion, quotient map, functor, decomposition, etc.—expose that object directly.  Do not proliferate convenience predicates/actions whose bodies merely perform one obvious comparison/application of the richer object.

- **Rationale**: The object carries additional mathematics for free: equality, composition, kernel/image, restriction, factorization, transport, and reuse.  A one-use wrapper hides this structure and creates a parallel vocabulary that does not compose.

- **Violation Example**: `same_genus(other)` instead of comparing genus objects; `action_on_discriminant_element(g,x)` instead of exposing `O(L) -> O(A_L)`; constructing identity through an identity matrix instead of asking the Homset.

- **Correct Example**: return `genus()`, the induced action morphism/functor, and `Hom.identity()`; callers compose/apply/compare those objects using their ordinary mathematical APIs.

#### `API-12`: Prefer Named Positive Mathematical Predicates Over Negated API Expressions

- **Rule**: When the literature has a standard name for a complementary property, expose that positive predicate rather than requiring users to express it as `not is_X()`.  The two names retain their proper mathematical/computability semantics; do not assume ordinary Python negation is a valid implementation when the predicate is three-valued or assertion-gated.

- **Rationale**: `is_degenerate()` communicates the mathematical concept directly; `not is_nondegenerate()` makes the reader reconstruct a logical complement and can become wrong when “unknown/not currently computable” is distinct from false.

- **Violation Example**: require `not L.is_nondegenerate()` throughout code/notebooks even though degeneracy is a named property; define `is_degenerate = lambda: not self.is_nondegenerate()` across a soft/three-valued boundary.

- **Correct Example**: expose and implement the named positive predicates at their mathematical owner, sharing semantic lower-level constructions where appropriate.

#### `API-03`: Engine Vocabulary Is Not a Compatibility Surface

- **Rule**: An owned API is not a name-for-name facade over Sage.
  Consumers speak the repository's mathematical vocabulary even when the engine has an analogous operation under another name.
  Do not add a public delegation solely because existing Sage code expects `.gen()`, `.gens()`, `.V()`, `.optimized()`, `.basis_matrix()`, `.coordinate_vector()`, `.submodule()`, or `.hom()`.

- **Rationale**: Compatibility delegations preserve the engine as the effective API and make later consumers depend on representation accidents.
  The owned spelling must be the only ordinary route, so a wrong consumer fails visibly instead of silently crossing the boundary.

- **Violation Example**: Adding `M.gen(i)` to an owned free module because one lattice invariant still calls Sage's free-module API; adding `M.submodule(vectors)` because a discriminant-form routine expects Sage submodules.

- **Correct Example**: Rewrite the consumers to use `module_generator`, `module_generating_set`, `framing_morphism`, `subobject_on`, `module_coefficients`, `presentation_matrix`, `invariant_factors`, `smith_form_module_generators`, and `invariant_factor_form` as the mathematics requires.

#### `API-04`: Chosen Presentations Survive Engine Normalization

- **Rule**: A chosen framing or presentation is mathematical data and is never silently replaced by an engine's optimized, Smith-normalized, reduced, or otherwise canonicalized representation.
  A normalization that changes the chosen data produces a new owned object together with the owned morphism or isomorphism relating it to the original.

- **Rationale**: Isomorphic presentations are not identical chosen presentations.
  Engine normalization is algorithmic and choice-bearing; overwriting the original framing loses exactly the data the framed category says the object carries.

- **Violation Example**: Replacing the selected module generators by `smith_form_gens()` after constructing an FGP engine; mutating the relation matrix to the Smith matrix and then treating it as the original presentation; feeding the selected relation rows into a backend submodule constructor that canonicalizes its basis and then treating the backend Smith change-of-basis matrices as changes from the original selected relations.

- **Correct Example**: Keep the selected presentation unchanged and let `invariant_factor_form()` return an explicit owned isomorphism from the original framed module to the Smith-normalized framed module.  A private backend either reduces the selected presentation matrix itself or records the explicit change from the selected relation framing to any canonical backend relation basis before composing normal-form witnesses.

* * *

### 3. Construction & Witness Interfaces (`CON-*`)

#### `CON-01`: Canonical Constructors Consume the Mathematical Datum

- **Rule**: A canonical public constructor takes the datum that defines the mathematical object: a morphism, action, form, inclusion, presentation, generating map, or other named structure.
  A coordinate matrix, row list, backend object, or collection of implementation fields does not replace that datum merely because it can encode it.
  A coordinate convenience constructor is admissible only when the coordinates genuinely determine the mathematical datum, it immediately constructs that datum, and it delegates to the canonical constructor without establishing a second object model.

- **Rationale**: The constructor is where invalid states become unrepresentable.
  If the public constructor accepts a weaker representation, callers can bypass the homset, relation checks, form-preservation checks, or other structure that makes the datum mathematically meaningful.

- **Violation Example**: Constructing a presented module directly from a Sage relation submodule; `with_action(G, matrices)` constructing the group morphism internally; `submodule_from_rows(matrix)` treating rows as the subobject rather than constructing the inclusion.

- **Correct Example**: `FinitelyPresentedModule(presentation)` consumes the selected morphism `F_1 -> F_0`; a module with a `G`-action consumes `rho: G -> Aut(M)`; a Gram-matrix convenience first constructs the corresponding form morphism on the specified framed free module and then invokes the canonical formed-module constructor.

#### `CON-02`: Structure Maps Are First-Class Morphisms Constructed by Their Caller

- **Rule**: Actions, representations, inclusions, scalar actions, form maps, comparison maps, and other structure maps exist as morphisms in their own homsets before another object consumes them.
  An object does not accept a source object plus raw generator images and secretly construct a morphism belonging to another category.

- **Rationale**: The morphism carries information that its image does not.
  For a group action `rho: G -> Aut(M)`, for example, `rho` need not be injective; replacing `G` by the subgroup generated by action matrices silently replaces the acting group by `rho(G)` and loses the kernel.

- **Violation Example**: `M.with_action(G, images)` constructing `rho` inside the module; recovering "the acting group" from the matrices appearing in a representation.

- **Correct Example**: Construct `G`, construct `Aut(M)`, construct `rho` in `G.Hom(Aut(M))`, then pass `rho` to the structured-module construction.  If the intended group literally is a subgroup of `Aut(M)`, construct that subgroup and use its inclusion.

#### `CON-03`: Transport Existing Structure Functorially

- **Rule**: When a construction changes an object carrying structure, transport that structure by the corresponding functor or named morphism construction.
  Do not reconstruct the transported structure from coordinate matrices when the defining morphism is already available.

- **Rationale**: Coordinate reconstruction duplicates the mathematics and introduces convention-dependent formulas at every consumer.
  Functorial transport states the definition once and automatically preserves composition and change of presentation.

- **Violation Example**: Building the form on a lattice direct sum by manually assembling a block Gram matrix; constructing the form on a subobject by slicing a matrix; implementing scalar extension by copying coefficients into a fresh matrix without applying the scalar-extension functor to the form morphism.

- **Correct Example**: Direct sum, tensor product, duality, and base change act on the module and on its form morphism; for an inclusion `i: S -> M` and bilinear form `b: M tensor M -> W`, the induced form is `b * (i tensor i)` in the appropriate Hom object.

#### `CON-05`: Chosen Preimages and Construction Provenance Are First-Class Data

- **Rule**: If a later mathematical operation requires not merely an output `F(A)` but the chosen presentation of that output as an image of `A`, represent the pair `(A, F(A))` or the corresponding functor-image object explicitly.
  Do not recover mathematically required preimages by attaching ad-hoc `_preamble_*_source_*` attributes to ordinary output objects and probing those attributes later.
  Incidental diagnostic provenance that is never part of a mathematical operation may remain private metadata, but it cannot be the hidden witness on which an adjunction, inverse transpose, or constructor depends.

- **Rationale**: A general functor output need not determine its preimage.  When a chosen preimage matters, that choice is mathematical data and deserves a type/construction that states it.
  Hidden source attributes create a second undocumented object model and make ordinary codomain objects behave differently depending on which constructor happened to produce them.

- **Violation Example**: Scalar extension setting `_preamble_scalar_extension_source_module` and the inverse Hom transpose later reading it; induction/coinduction attaching `_preamble_induction_source_group_module` or `_preamble_coinduction_source_group_module`; free/cofree `G`-set functors attaching source sets solely so an adjunction can recover them.

- **Correct Example**: Use the existing functor-image construction (or another explicit chosen-image object) when a chosen preimage is required, and let the adjunction consume that selected presentation.  If the inverse transpose can be derived from the unit/counit without recovering a hidden source object, derive it directly instead.  For `Spec`, make the contravariant functor's action on an algebra morphism produce the scheme morphism whose pullback is intrinsic to that morphism, rather than attaching `_preamble_coordinate_algebra_morphism` afterward as a side channel.


#### `CON-06`: Constructor Admission Is a Semantic Firewall

- **Rule**: Judge a constructor by the invalid states and alternate ontologies it admits.  The canonical constructor consumes the defining mathematical datum and performs the containment/well-definedness check exactly once.  Do not broaden constructor inputs for convenience when doing so lets callers bypass that datum.

- **Rationale**: Construction is the point where “this is an element of Hom”, “this map preserves the form”, “this action respects the relations”, or “this is the stated subobject” becomes true.  If arbitrary objects with a `.matrix()` method, coordinate arrays, or loose image lists are also admitted, every downstream caller can bypass the proof encoded by construction.

- **Violation Example**: A Hom accepting any object with matching endpoints and a matrix; `with_action(G, images)` constructing the group morphism internally; an element constructor accepting a bare vector whose parent/framing is unstated.

- **Correct Example**: `G.Hom(Aut(M))(generator_images)` constructs and validates the action morphism, and the structured module consumes that `rho`; a free/presented module consumes its framing/presentation morphism; a matrix convenience, when mathematically unambiguous for a canonically framed Hom, immediately constructs that Hom element and returns no parallel representation.

#### `CON-07`: Chosen Structure Is Data; Derived Subcategory Membership Is Output

- **Rule**: Do not encode a derived mathematical property or category membership as a mode boolean or constructor switch.  Construct from the defining datum and refine/place the resulting object according to properties established from that datum.  If an additional *choice* is genuinely part of the structure, accept the actual chosen datum, not a boolean claiming it exists.

- **Rationale**: Flags such as `even=True`, `negative=True`, `torsion=True`, or `nondegenerate=True` make the caller duplicate facts the object/category should own and permit contradictions between the flag and the data.  Conversely, a selected orientation, framing, action, embedding, or volume form is real extra data and must remain explicit.

- **Violation Example**: `Lattice(G, even=True)`; `Form(..., nondegenerate=True)`; `saturation(in_ambient=M)` where the missing datum is actually an inclusion morphism.

- **Correct Example**: Construct `Lattice(G)` and refine it into `EvenLattices` when justified; pass an actual `rho:G->Aut(M)` for an action; call saturation on the subobject/inclusion that already carries its codomain.


#### `CON-08`: A Mathematical Choice Is Represented by Its Selecting Datum

- **Rule**: Whenever several mathematically valid objects/maps could satisfy a phrase such as “the extension”, “the lift”, “the normalization”, “the dual”, “the section”, or “the presentation”, either identify the canonical construction that removes the choice or represent the chosen datum explicitly.  Do not hide a choice in a boolean, mode string, import state, or undocumented constructor convention.

- **Rationale**: A definite article silently asserts uniqueness/canonicity.  When the mathematics supplies only a family of choices, downstream functoriality and equality depend on which one was selected.  First-class selected data makes that dependency visible and composable.

- **Violation Example**: `normalize=True` mutates/re-presents an object without returning the isomorphism; `map=True` changes a constructor's mathematical return object; `dual()` ambiguously chooses among module, metric, or Pontryagin duals; a chosen preimage is recovered from hidden provenance.

- **Correct Example**: `invariant_factor_form()` returns the normalized framed module with its explicit isomorphism; different dual functors have distinct owned names; a selected section/lift/preimage is stored as a morphism or functor-image datum.


#### `CON-09`: Universal Constructions Return Complete Mathematical Data

- **Rule**: A universal construction returns an owned object together with the canonical arrows that make it that construction, either as explicit components of the returned construction or as intrinsic methods on the returned structured object.  Never return only a presentation, basis, underlying abstract object, or numerical representative and require callers to reconstruct the universal maps.

- **Rationale**: The kernel is not merely an isomorphic module of solutions; it is a subobject with a canonical inclusion.  The cokernel is not merely an abstract quotient module; it comes with the canonical projection.  Products have projections, coproducts have injections, pullbacks/pushouts have their legs.  These maps are what make the construction composable and let callers state universal properties without descending to coordinates.

- **Violation Example**: `f.kernel()` returns generators/basis rows with no inclusion into `domain(f)`; `f.cokernel()` returns a normalized module but drops `codomain(f) -> coker(f)`; a pullback returns an object but not the maps to the two factors.

- **Correct Example**: `K = f.kernel()` is an owned subobject whose `inclusion()` has codomain `f.domain()`; `Q = f.cokernel()` owns `Q.projection(): f.codomain() -> Q`; a quotient element may provide a chosen `lift()` as representative selection, explicitly not as an inverse to the projection.


#### `CON-10`: Do Not Parameterize a Notion Already Determined by Existing Mathematical Data

- **Rule**: If the current object, morphism, base map, or category structure already determines the standard mathematical notion uniquely, derive it from that data.  Do not add a parameter, flag, policy object, or user-selected convention that silently redefines the notion.  Extra input is accepted only when the mathematics genuinely contains a choice, in which case `CON-08` requires the selecting datum itself.

- **Rationale**: Parameters suggest a family of legitimate meanings.  For intrinsic notions this creates false degrees of freedom and lets callers contradict the structure already present.  It also encourages API proliferation (`foo(..., mode=...)`) where distinct mathematical operations should either be derived canonically or have distinct names.

- **Violation Example**: Add `integral_over=D` to redefine integrality of a ring-valued form when the structural map `R -> W` already determines integrality over `R`; pass `even=True` or `torsion=True`; make “the dual” selectable by a mode string instead of using distinct dual functors.

- **Correct Example**: Compute integrality from the specified ring extension; derive evenness/torsion as properties; represent a genuinely chosen orientation, embedding, section, framing, or presentation by its actual mathematical datum.


#### `CON-11`: A Framing Is a Selected Epimorphism `Free_R(S) -> M`

- **Rule**: Model a framed module by an actual owned set `S` and a selected epimorphism `Free_R(S) -> M`.  The framing set is the domain of the distinguished-generator map; generator evaluation is the image of its free generators.  Do not identify a framing with a Python sequence, an ordered basis, or a reversible label-to-element correspondence unless stronger chosen structure supplies those properties.

- **Rationale**: Finite generation, freeness, a basis, order, and enumerability are independent hypotheses.  A generic framing may use an infinite/nonenumerable set, and an epimorphism may identify distinct free generators.  Treating a framing as a tuple/basis silently adds all of those hypotheses and creates exactly the finite-coordinate blast radius `ARC-16` forbids.

- **Violation Example**: `self._module_generators = tuple(generators)` as the definition of framing; recover a framing label from every generator image; require a rank integer when the natural input is an arbitrary set `S`.

- **Correct Example**: retain `S`, `Free_R(S)`, and the selected epimorphism.  The canonical rank-`n` free module is the specialization `S=[n]`; a based module is the refinement in which the framing morphism is an isomorphism and the additional ordering/indexing data is actually present.



#### `CON-12`: Public Construction Enters Through the Owning Mathematical Root; Refinement Is an Output

- **Rule**: Public constructors are owned by the natural general category/object whose defining datum the caller has.  The construction validates that datum, builds the object, and places/refines it into every stronger category justified by the result.  Do not require callers to choose a specialized subcategory or concrete implementation class before construction unless that choice is itself additional mathematical input.

- **Rationale**: A researcher who knows a Gram form, presentation, group action, polynomial, scheme datum, etc. should not need to predict which internal refinement or backend class the finished object will occupy.  Constructors on every subcategory duplicate routing knowledge and make refinement a user obligation instead of a consequence of construction.

- **Violation Example**: Require `RootLattice("E8")` instead of constructing the lattice and discovering/refining its root-lattice structure; expose a private `BasedFreeModuleImpl(...)` alongside the owned free-module constructor; ask the caller to select `Even`/`Nondegenerate` constructor variants from properties the datum determines.

- **Correct Example**: construction enters through `Lattices(R)`, `Modules(R)`, the appropriate Hom/category root, or a canonical object constructor such as `Lattice(...)`; the constructor returns the owned object already placed in its strongest established refinements.  Private implementation selection occurs after mathematical construction/routing.



#### `CON-13`: Supplied Generating Data Constructs the Generated Subobject/Subgroup, Never the Canonical Whole

- **Rule**: Caller-supplied generators, relations, samples, or other uncertified finite data construct exactly the mathematical object generated by that data.  They do not stand in for a canonical ambient object/group whose completeness is a separate theorem/computation.  Canonical objects exist independently at their natural owner even when enumeration/generator computation is unavailable.

- **Rationale**: A list of isometries proves only a subgroup `H <= O(L)`.  Treating it as `O(L)` makes every orbit, stabilizer, kernel, index, and invariant computation silently answer the wrong group when the list is incomplete, while each local operation can remain internally valid.  The same distinction applies to supplied spanning data versus an entire canonical subobject whenever completeness is not established.

- **Violation Example**: `L.O(generators=gens)` returns the canonical orthogonal group; `Aut(X, generators=...)` substitutes a finitely generated subgroup for the automorphism group; downstream invariants are labeled as canonical-group invariants.

- **Correct Example**: `L.O()` is the canonical predicate-defined group object with membership/element operations available; `L.O().subgroup(gens)` is the supplied subgroup.  A specialized algorithm may later compute/prove a generating family for `L.O()` and then its own `group_generators()` method returns that chosen family.



* * *

### 4. Category Placement & Capability (`CAT-*`)

#### `CON-04`: Coordinate Matrices Belong Exactly to Free-Module Homs

- **Rule**: A matrix of a linear map is the element of `Hom_R(F_R(S),F_R(T))` determined by chosen free framings.  Do not assign a coordinate matrix to an arbitrary morphism of finitely generated or finitely presented modules merely because source and target have generating sets.  Constructions on nonfree modules use their presentations, generating morphisms, and relations directly.

- **Rationale**: A generating family of a nonfree module is not a basis.  Recording images of generators is sufficient to define a morphism subject to the source relations, but it is not a matrix in a Hom between free modules.  Confusing the two silently treats a presentation as an isomorphism with a free module.

- **Violation Example**: Constructing `coker(f: M -> N)` for presented modules by calling `f.matrix()` and appending its rows to a presentation matrix, even though `M` or `N` is not free.

- **Correct Example**: If `N` has selected presentation relations and `M` has a chosen generating morphism, present `coker(f)` by the existing relations of `N` together with the coefficient rows of `f(m_s)` in the chosen framing of `N`.  Only when both endpoints are framed free modules is that same data literally the matrix of `f`.


#### `CAT-01`: Place the Method by Mathematical Domain; Route Algorithms by Computable Case

- **Rule**: Put a mathematical method on the first category/object/element where the notion itself is well-defined. Do not invent computability categories merely to hide methods whose values mathematically exist more generally. Inside that correctly owned method, route among the cases for which exact algorithms are currently implemented, preferably by category/representation-aware `match`/`case` or specialized overrides. The unhandled remainder may terminate with an informative assertion stating the current computational limitation. A method whose entire implementation is immediate failure is forbidden; `NotImplementedError` is not a mathematical implementation strategy.

- **Rationale**: Mathematical domain and computational domain are different. Every set has a cardinality, but exact cardinality is undecidable/unavailable for arbitrary represented sets. Every formed module has a well-defined nondegeneracy property, but a callable form on an infinite-rank projective module may be outside current algorithms. Hiding such methods on `SetsWithComputableCardinality` or `FormedModulesWithDecidableNondegeneracy` would encode today's software limitations as false mathematics. Assertion-gated case routing instead keeps the ontology correct while making the present computational frontier explicit and auditable.

- **Violation Example**: Creating `SetsWithCardinality` so only those sets expose `cardinality()`; moving `is_nondegenerate()` off general formed modules merely because the current implementation needs a finite Gram tensor; exposing `kernel()` with a body consisting only of `NotImplementedError`; using `hasattr`/exception fallback to discover an algorithm.

- **Correct Example**: `Sets().ObjectType.cardinality` routes finite/enumerated/symbolic cases to exact algorithms and ends with an informative assertion for a represented case not yet handled. `FormedModules(R).ObjectType.is_nondegenerate` computes from the correlation/Gram tensor where available and assertion-gates currently undecidable representations. A truly positive-definite-only construction, by contrast, belongs on `PositiveDefiniteLattices` because its **mathematical definition**, not merely its algorithm, has that hypothesis.

#### `CAT-09`: Semantic Parity Never Means Signature Parity

- **Rule**: When importing capability from Sage, archived code, another CAS, or a reference implementation, first determine the mathematical entity on which the operation is well-defined and the datum it actually consumes.  Recreate that semantic capability in the owned category graph; do not copy the foreign method signature, placement, mode flags, or witness-compensating parameters merely because the upstream implementation exposes them.

- **Rationale**: A signature embodies an ontology.  APIs without first-class subobjects/morphisms often hang morphism-dependent operations on bare objects and add `ambient=` parameters; APIs without category refinement often add `even=`/`negative=` modes.  Porting those signatures imports the old mathematical model along with the computation.

- **Violation Example**: Port Sage's `saturation(in_ambient=...)` directly onto an owned lattice; mirror an upstream `even=` constructor flag; expose `is_submodule(M)` on a bare object rather than an embedding/existence question in the appropriate Hom.

- **Correct Example**: Site saturation on the subobject/inclusion, derive category membership from the constructed object, and represent embedding existence by the relevant `Emb(A,B)`/Hom object.  Reuse the upstream algorithm privately after the semantic interface has been corrected.

#### `CAT-10`: The Owned Category Type Protocol Is `ObjectType` / `ElementType` / Hom-Category Types

- **Rule**: The public owned category architecture speaks in the preamble's type protocol: `ObjectType`, `ElementType`, `HomCatType`, `EndCatType`, `AutCatType`, and the corresponding arrow types (`ArrowType`, `EndArrowType`, `AutArrowType`).  `ArrowType` is conceptually the element type of the Hom-category object, not an independent third method mechanism.  Sage `ParentMethods`, `ElementMethods`, `MorphismMethods`, dynamic classes, and related machinery may remain private runtime implementation details while this protocol is completed; new doctrine and APIs do not treat those Sage names as the mathematical architecture.

- **Rationale**: The owned category graph is supposed to describe objects, elements, and Homs uniformly.  Reusing Sage's method-container vocabulary as public ontology repeatedly causes contributors to think of attached mixin buckets rather than instantiated implementation types generated by the category graph.

- **Violation Example**: Specify a new preamble feature as “put this in `MorphismMethods`” without first stating the Hom/arrow category that owns it; document `ParentMethods` as a public mathematical type; build a separate morphism-class hierarchy because the Hom-category element type was not considered.

- **Correct Example**: State that category `C` supplies an `ObjectType`; `Hom_C` supplies its object/element types; arrows are elements of the Hom-category construction.  Map those owned declarations onto Sage's dynamic method installation privately until the runtime migration is complete.

#### `CAT-11`: Functorial Domain Restrictions Are Categories, Not Runtime Rejection Branches

- **Rule**: A functor's declared domain is the most general category on which the mapping is actually functorial.  If a construction transports only isomorphisms, declare it on `C.core()`; if it needs a slice/coslice/arrow category or a parameterized base-change category, use that category.  Do not advertise a functor on a larger domain and reject ordinary morphisms inside `_apply_morphism`.

- **Rationale**: Functoriality is part of the mathematical type.  A runtime branch that says “this morphism is unsupported” after accepting it into the functor's domain encodes a false signature and moves a categorical hypothesis into control flow.

- **Violation Example**: Define the center as a functor on all rings and assert that each incoming ring map happens to preserve centers; define a construction on `C` while every non-isomorphism branch immediately fails.

- **Correct Example**: When only isomorphisms transport the construction, use `C.core()` as the domain.  Other restrictions are modeled by the appropriate owned subcategory/category construction, after which the functor action is total on its declared arrows.

#### `CAT-12`: Sage's Category Graph Is Empirical Runtime Evidence, Not Mathematical Authority

- **Rule**: Read Sage source/runtime behavior to learn exactly what Sage encodes and which algorithms/methods a Sage category supplies.  Decide mathematical category identity, inclusions, forgetful/projection functors, and equivalences in the owned graph independently.  Never treat Sage `==`, `is_subcategory`, `super_categories()`, `all_super_categories()`, or absence/presence of an edge as proof of the corresponding mathematical statement.

- **Rationale**: Sage's graph is intentionally shaped by dynamic dispatch/MRO and historical API choices.  A `super_categories()` edge can represent several kinds of structural maps; “immediate” parents are a generating set selected for linearization; equal parent lists do not imply equal categories; mathematically required edges can be absent; two presentations of the same construction can compare unequal.

- **Violation Example**: copy Sage's `Modules(R) -> Bimodules(R,R)` or a facade/category edge into the owned graph merely from its spelling; infer that two refinements are equivalent because their Sage parent lists coincide; infer a mathematical non-inclusion because Sage lacks the edge.

- **Correct Example**: first identify the normalized mathematical objects/structures and their actual functors; then maintain a backend correspondence that records how Sage's declarations/behaviors realize or approximate those owned categories for computation.

#### `CAT-13`: Category Identity, Standard Name, and Classifier Expression Are Three Distinct Layers

- **Rule**: Maintain one mathematical category identity.  Attach an established public noun/notation when one exists, and separately retain the classifier/category expression that defines or constructs that identity.  A named composite or alias does not create another category object.  Classifier names are interpreted relative to their host/defining morphism, not as globally meaningful Boolean labels.

- **Rationale**: `Semigroups` and `Magmas.Associative` can be a standard name and a defining presentation of one category.  `Commutative` on groups and a similarly spelled property in another theory need not be the same classifier.  Conflating name, identity, and presentation creates duplicate vertices, string-based ontology, and ad-hoc alias edges.

- **Violation Example**: create separate `Semigroups` and `Magmas.Associative` vertices; mint one global `Finite`/`Commutative` classifier keyed only by its word; make `GradedAlgebras` an independent species instead of the relevant classifier pullback/refinement.

- **Correct Example**: one owned category identity carries its standard name and its definitional expression; classifiers are declared at their natural host and transported by pullback/composition to categories where the same structure/property is induced.

#### `CAT-14`: Category Constructibility Is Derivability of Canonical Structural Maps, Not Graph Reachability

- **Rule**: Determine whether a classifier/category expression can be formed from the canonical structural maps supplied by the owned grammar: projections/forgetful functors, composition, classifier application/pullback, slice/coslice/core/etc. as defined.  Do not use arbitrary graph reachability, name presence, reverse traversal of projections, or Sage MRO paths as a proof that the mathematical construction exists.

- **Rationale**: A graph can connect vertices by arrows whose direction/type do not provide the data required by a pullback/classifier.  Reachability forgets roles and universal properties, and reverse traversal fabricates structure.  Typed structural derivation keeps construction aligned with the actual mathematical diagram and makes ephemeral classifier towers possible without minting named nodes.

- **Violation Example**: infer `C.A` because a path from `C` eventually reaches a node named `A`; search backwards from a classifier projection to claim the classified structure; require every constructible classifier tower to have a named category vertex.

- **Correct Example**: the defining structural functor `C -> H` together with classifier `H.A -> H` yields `C.A = C x_H H.A` and its projection; ancestor routes are compositions of those canonical maps.  No extra named node or graph-search witness is required.

#### `CAT-02`: Property Categories Do Not Manufacture Chosen Data

- **Rule**: Distinguish a property from a chosen witness of that property.
  A property category such as finitely generated or finitely presented states existence; a data category such as framed or chosen-presentation carries a specified generating morphism or presentation and owns operations that consume that choice.
  A property category never silently computes or selects the witness on demand.

- **Rationale**: Existence of a presentation is weaker than a chosen presentation.
  Conflating them makes algorithms depend on arbitrary hidden choices and incorrectly turns unavailable witness computation into failure of the mathematical property.

- **Violation Example**: `FinitelyPresentedGroups().ObjectType.presenting_free_group()` computing a presentation merely because the group is known finitely presented; asking every finitely generated module for a preferred generating set.

- **Correct Example**: `FinitelyPresentedGroups()` records the property; `GroupsWithChosenFinitePresentation()` carries and exposes the selected presentation.  `FramedModules(R)` carries the chosen epimorphism from a free module, while `FinitelyGeneratedModules(R)` only states existence of some finite framing.

#### `CAT-03`: Constructibility Does Not Require Enumeration or Generators

- **Rule**: A mathematically defined object may be useful and constructible through membership, universal properties, or predicate carve-outs even when no algorithm enumerates it or returns a finite generating set.
  Do not identify "construct the object" with "compute a presentation of all of its elements."

- **Rationale**: Many important objects are first-class long before a full presentation is available.
  Orthogonal groups, stabilizers, centralizers, kernels, and ring centers can support containment, individual elements, morphisms, and further subobjects without globally enumerating generators.

- **Violation Example**: Refusing to provide `O(L)` because the available backend cannot compute generators for an indefinite lattice; replacing it by `None` or by a tuple of known isometries.

- **Correct Example**: Represent `O(L)` as the subgroup of `GL(L)` cut out by the form-preservation predicate, so membership and individual isometries are meaningful; a definite-lattice subcategory may additionally compute a finite generating set.

#### `CAT-04`: Category Placement Is a Mathematical Declaration, Not a Proof-Certificate System

- **Rule**: Category membership is an auditable mathematical declaration enforced by the category's operational contracts and, where appropriate, a participant's named predicate.
  Do not invent proof objects, evidence records, certificate registries, or trust ontologies to justify ordinary category placement.

- **Rationale**: Runtime certificate machinery duplicates the category graph without proving the mathematics it purports to certify.
  The useful contract is the mathematical operation itself: an object claiming a data-bearing category supplies its datum; an object claiming a predicate subcategory supplies the named predicate or algorithm required there.

- **Violation Example**: Introducing `FinitePresentationCertificate`, `ProofOfNondegeneracy`, or an evidence registry that must accompany refinement into the corresponding category.

- **Correct Example**: A finitely generated formed module computes `is_nondegenerate` from the defining correlation when that is decidable; an object whose nondegeneracy is a theorem may explicitly provide the named predicate returning `True`, with the claim visible on the participant and reviewable as mathematics.

#### `CAT-05`: Operations Live on the First Category Where They Are Mathematically Defined

- **Rule**: Put an operation on the appropriate owned `ObjectType`, `ElementType`, Hom-category/arrow type, or functor type of the most general owned category on which the operation is actually defined.
  A more structured subcategory inherits that API and adds only the operations supplied by the additional structure.  Sage method-container classes may realize this privately but are not the public placement vocabulary.
  Do not place an operation on a ubiquitous underlying object and guard it with shape, type, backend, or capability tests when category placement can state the hypothesis.

- **Rationale**: The category graph is the API graph.
  An element should acquire methods because of what mathematical object it is, not because a monolithic implementation class recognizes a special runtime case.
  This also keeps multiple independent refinements composable: algebraic, Lie, scheme, smooth, topological, and arithmetic APIs can coexist on one mathematical object without one implementation pretending to own the others.

- **Violation Example**: A generic tensor element exposes `smith_form()` only when `hasattr(engine_matrix, "smith_form")`; every matrix exposes `determinant()` and raises unless it happens to be square over a commutative ring; `MatrixSpace` always installs Lie methods merely because `m == n`.

- **Correct Example**: Entry access, rows, columns, and transpose live on matrix spaces; square-matrix multiplication lives on square matrix rings; determinant lives where square matrices over commutative scalars have it; Smith normal form is available because the coefficient ring is a PID and its matrix-reduction operation acts on `M_{m,n}(R)`; the commutator bracket is inherited from a suitable associative algebra; scheme/manifold/topological methods come from their respective refinements.

#### `CAT-06`: Structure Induced by Parameters Belongs to the Parameter Categories

- **Rule**: When an operation on a mathematical object exists because one of its parameters has a mathematical property, model that capability on the parameter category and let the object use it; do not manufacture a parallel object category whose only purpose is to restate the parameter hypothesis.
  Shape-dependent structure may refine the object itself when shape changes the operations on its elements, but coefficient-ring properties remain properties of the coefficient ring.

- **Rationale**: `M_{m,n}(R)` is the same kind of matrix space whether or not `R` is a PID.  The PID hypothesis explains why Smith reduction is available; it does not create a new species of matrix.  Conversely, the distinction `m=n` genuinely changes the matrix object's intrinsic multiplication and can justify square-matrix-ring structure.

- **Violation Example**: Introducing `PIDMatrices`, `MatricesOverFields`, `MatricesOverEuclideanDomains`, or similar parallel matrix categories solely so ordinary matrices acquire algorithms implied by the coefficient ring.

- **Correct Example**: `M_{m,n}(R)=Hom_R(F_R([n]),F_R([m]))` remains the same Hom object.  When `R` is a PID, an element `A` presents `coker(A)`; invariant-factor normalization of that presentation yields the Smith diagonal and its source/target basis changes.  When `m=n`, the same object is `End_R(F_R([n]))`, whose multiplication is already composition.

* * *

### 5. Definition Fidelity (`DEF-*`)

#### `CAT-07`: Owned Category Types Supply the Object and Element API

- **Rule**: Operations shared by every element of a mathematical category belong on that category's owned `ElementType`; object-wide constructions belong on its `ObjectType`; arrow operations belong on the element type of the appropriate Hom/arrow category.  Concrete/runtime classes store only representation-specific data/primitives that the categorical API delegates to.

- **Rationale**: The category graph states the mathematics and is therefore the correct place for uniform syntax and operations.  Duplicating scalar multiplication, inversion, bracket, matrix entry, or similar methods on each concrete representation class makes those classes define the theory and causes one representation to miss operations another happens to implement.

- **Violation Example**: Adding Python-literal scalar multiplication separately to presented-module, lattice, tensor-product, and localized-module element classes; putting matrix operations on a backend matrix wrapper instead of the matrix-Hom category.

- **Correct Example**: the `ElementType` supplied by `Modules(R)` carries left scalar syntax through the object's scalar action; the matrix-Hom element type supplies entries/rows/columns; a concrete presented-module runtime element supplies only the representation primitive needed by those owned methods.


#### `DEF-01`: A Predicate's Body Is Its Definition, Not a Recognition Criterion

- **Rule**: Implement a mathematical predicate from its definition, expressed through the owned objects and morphisms that occur in that definition.
  Do not substitute a theorem-equivalent determinant, rank, gcd, coordinate, or matrix criterion as the predicate body merely because it is cheaper in a familiar special case.  Such criteria are permitted **underneath the semantic owner** as implementation cases or cross-check assertions once their hypotheses are explicit; downstream callers never see or repeat them.

- **Rationale**: A recognition criterion used as the public definition carries an unstated theorem and its hypotheses at every call site.
  A semantic definition has one visible proof obligation: that the body spells the definition correctly.  The low-level operations named by that definition may route to theorem-equivalent exact criteria in the represented categories where those theorems apply, so the optimization/theorem is stated once and remains private forever.

- **Violation Example**: `is_nondegenerate()` as `gram.det() != 0`; `is_unimodular()` as `abs(gram.det()) == 1`; `is_primitive()` as a gcd of coordinates; `is_injective()` as a matrix-rank comparison.

- **Correct Example**: Nondegeneracy asks whether the correlation `M -> dual_module(M)` is injective; unimodularity asks whether that correlation is an isomorphism; primitivity asks whether the cokernel of the inclusion is torsion-free; injectivity asks whether the kernel is zero.

#### `DEF-02`: Numerical Data Does Not Replace the Structural Object It Describes

- **Rule**: When a numerical invariant or normal form is derived from a structural object, keep the structural object as the public mathematical result and quarantine the numerical computation behind its owner.
  Do not let a matrix, basis, rank, content, determinant, or invariant-factor tuple stand in for a kernel, cokernel, subobject, quotient, normal form, or morphism.

- **Rationale**: Numerical data often determines the desired object only under additional hypotheses and chosen coordinates.
  Returning the structural object preserves its universal property and lets downstream code compose mathematically instead of re-proving the reconstruction theorem.

- **Violation Example**: Returning kernel basis vectors instead of `ker(f)` with its inclusion; implementing saturation as `Matrix.saturation()`; returning a Smith matrix as "the normalized module."

- **Correct Example**: `f.kernel()` returns the owned kernel subobject; saturation is the kernel of `M -> M/S -> (M/S)/Tor(M/S)`; invariant-factor form returns a new framed module together with the explicit isomorphism from the original.

#### `DEF-03`: Derive Special Cases from the General Construction; Do Not Presume Them

- **Rule**: A constructor or general operation returns the object dictated by its definition and then refines the result when a stronger property is established.
  Do not construct the result directly in a special subcategory merely because current examples usually land there.

- **Rationale**: Presuming the special case turns an accidental property of test data into part of the operation's codomain.
  General construction followed by valid refinement keeps the mathematical codomain correct and lets special algorithms remain available when justified.

- **Violation Example**: Defining every cokernel of a lattice embedding as a torsion module even when the quotient can have positive rank; constructing a quotient as finite because all current fixtures are finite.

- **Correct Example**: Construct the cokernel as a finitely presented module from the presenting morphism, then refine it into the torsion category exactly when its invariant factors establish torsion.

#### `DEF-04`: Matrix Normal Forms Are Presentation Normalizations

- **Rule**: For a matrix representing a morphism of finite free modules, define Smith/invariant-factor normal form through equivalence of the corresponding presentation, not as an unrelated primitive matrix routine.
  Over a PID, `A : R^n -> R^m` presents `coker(A)`; the structure theorem for finitely generated `R`-modules gives an invariant-factor presentation.  The normal-form witness consists of the diagonal presentation together with the source and target basis-change isomorphisms relating it to `A`.
  A backend matrix routine may compute those basis changes privately, but the public mathematical construction is the presentation normalization.

- **Rationale**: The diagonal entries are the invariant factors of the presented module, and left/right multiplication are changes of chosen bases in the two free modules.  Treating Smith form as a standalone array algorithm duplicates the module-classification theorem and disconnects the witness from the cokernel it classifies.

- **Violation Example**: Defining `R.smith_form(A)` as a primitive ring method whose contract is merely whatever triple Sage returns; computing invariant factors separately in the presented-module layer and Smith matrices separately in the tensor layer.

- **Correct Example**: Normalize the presentation `R^n -> R^m -> coker(A)` to its invariant-factor presentation, retaining isomorphisms of the presenting free modules.  `A.smith_form()` is then the coordinate matrix of that normalized presentation together with the coordinate matrices of those basis changes.  If a backend canonicalizes a relation submodule before reduction, its basis change must be included in this presentation isomorphism; it may not be discarded.


#### `DEF-05`: A Normal Form Is a New Object Together With an Isomorphism

- **Rule**: When normalization, reduction, canonicalization, or re-presentation changes chosen framing/presentation data, the result is a new owned object of the same mathematical category together with an explicit isomorphism from the original.  Do not mutate the source into its normal form and do not make the comparison morphism an optional flag.

- **Rationale**: Chosen presentations are structure.  Smith/Hermite/invariant-factor reduction may produce an isomorphic abstract module while changing its framing and relations.  Without the isomorphism there is no mathematical statement connecting the two represented objects, and downstream transported structures have no witness along which to move.

- **Violation Example**: Replace a module's selected presentation with its Smith matrix in place; `normal_form(transformation=False)` returns only the diagonal object; use `normalize=True` to alter constructor semantics without representing the map.

- **Correct Example**: `M.invariant_factor_form()` returns an isomorphism `M -> M_normal`; the matrix normal form is the private/coordinate computation used to construct that arrow.  Normal forms of actual matrix objects may remain matrix operations, while normal forms of framed modules are object-plus-isomorphism constructions.



#### `DEF-06`: Exact Mathematical Questions and Soft Knowledge Questions Have Different Codomains

- **Rule**: Preserve the actual mathematical codomain of an exact operation or predicate.  Do not return `False`, `None`, or `Unknown` merely because the current implementation cannot decide/compute a represented case; use the assertion-gated computational frontier of `CAT-01`.  Separately, an explicitly **soft knowledge/computability predicate** may be designed with a three-valued codomain `True | False | Unknown` when the proposition being returned is itself “what is currently known/computable/available.”

- **Rationale**: “The object is not nondegenerate” and “the current system does not know whether it is nondegenerate” are different statements.  So are “this group is not finitely generated” and “no generating-set algorithm is currently available.”  Collapsing them creates confident mathematical falsehoods; returning `Unknown` from an exact-valued operation changes its mathematics just as badly.

- **Violation Example**: `is_nondegenerate()` returns `False` when no algorithm handles an infinite callable form; `cardinality()` returns `Unknown`; `generators_are_computable()` returns `True` merely because the constructor trusted external input.

- **Correct Example**: `is_nondegenerate()` computes known cases and assertion-gates the current frontier.  A distinct `generators_are_computable()` or `has_computed_group_generators()` may return Sage's `Unknown` when that explicitly three-valued knowledge question has not been decided.


* * *

#### `CAT-08`: Mathematical Enumeration Is Lazy; Materialization Is Backend-Only

- **Rule**: Mathematical code never replaces an owned set, framing, basis, generating family, index set, group, Hom index, or other mathematical collection by `tuple(...)`, `list(...)`, or another eagerly materialized Python container, even when the collection is known finite.  Consumers iterate the owned collection lazily or use its membership, cardinality, rank/unrank, indexing, finite-support, image, product, or family structure.  Whole-family materialization is permitted only inside a private backend adapter whose external API specifically requires a finite concrete array; that adapter must establish finiteness before serialization and the Python container must not escape it.
- **Rationale**: Finiteness does not turn a mathematical collection into a Python sequence.  Keeping one collection interface for finite and infinite cases prevents downstream code from acquiring accidental `len`, slicing, whole-family traversal, or representation assumptions.  Enumerability, order, cardinality, and finiteness remain mathematical structure; backend arrays are only a final serialization format.
- **Violation Example**: `labels = tuple(M.module_generating_set())` before ordinary module logic, even when `M` is finite; storing `self._generators = list(generators)`; converting a finite index set to a tuple merely to enumerate it twice; checking a callable section by evaluating it at every index; implementing `Sym^n(M)` by first materializing the framing.
- **Correct Example**: Keep `M.module_generating_set()` as the owned ordered/indexed set and iterate it directly.  Use `rank(label)`/`unrank(i)` or finite support when positional access is needed.  A private Sage/GAP/Julia bridge may serialize a mathematically finite ordered set to a Python row/column array immediately before the backend call and discard that array on return.  A finite-presentation algorithm dispatches from `ModulesWithChosenFinitePresentation`, not merely from a weaker existence property.

### 6. Mathematical Vocabulary & Public Types (`LEX-*`)

#### `LEX-01`: Every Public Name and Type Has a Standard Mathematical Referent

- **Rule**: A public name denotes a standard mathematical object, morphism, construction, invariant, property, or chosen structure with its defining data understood from the category.
  Do not mint public wrapper types or names for implementation roles, storage formats, backend distinctions, or local workflow conveniences.

- **Rationale**: A type name is part of the mathematical theory exposed by the repository.
  An implementation-flavored noun creates a parallel ontology that downstream code will start treating as mathematics.

- **Violation Example**: `ExactScalar`, `NativeLattice`, `DiscriminantGroup` as a new type distinct from the finite abelian group underlying a discriminant form, or a wrapper whose only purpose is to package a tuple of constructor arguments.

- **Correct Example**: Use `RingElement`, `RealApproximation`, `FiniteAbelianGroup`, `DiscriminantForm`, `ModuleMorphism`, and the existing categorical constructions whose definitions state the actual mathematics.

#### `LEX-02`: Names State the Structure They Belong To

- **Rule**: When the same noun exists for several structures on one object, the public name states the structure explicitly.
  Use `group_generators`, `module_generators`, `algebra_generators`, `module_generating_set`, and similarly qualified dual or action names.
  Do not keep a bare ambiguous name as a compatibility alias underneath the precise one.

- **Rationale**: An algebra can simultaneously have group, module, and algebra generators; an object can carry several dualities.
  A bare `generators()` or `dual()` therefore has no stable mathematical referent even when today's concrete class happens to have only one candidate.

- **Violation Example**: `generators()`, `gens()`, `generating_set()`, or `dual()` on an owned multi-structured object; `module_generators()` implemented as a delegation to the still-public ambiguous `generators()`.

- **Correct Example**: The module framing exposes `module_generating_set()` and `module_generator(label)`; a group exposes `group_generators()`; metric, module, and group dualities have distinct names tied to the functors that produce them.

#### `LEX-03`: Exact Mathematics Is the Default; Approximation Carries the Adjective

- **Rule**: Public mathematical nouns denote exact objects unless approximation is explicitly part of the type or operation name.
  Approximate numerical representations are extracted at plotting, display, numerical-analysis, or other explicitly approximate boundaries.

- **Rationale**: Marking the exact case as exceptional reverses the mathematical default and can make exact objects such as algebraic or symbolic reals impossible to state.

- **Violation Example**: Using `RealNumber` to mean an MPFR approximation while exact `sqrt(2)` needs a separate exceptional type; a public `ExactScalar = Integer | Rational` union that describes implementation classes rather than the mathematical field `QQ`.

- **Correct Example**: `RealNumber` denotes an exact real in the repository's mathematical vocabulary where represented; `RealApproximation` or an explicitly precision-bearing operation denotes an MPFR approximation.


#### `LEX-04`: Software Roles Do Not Define Mathematical Ontology

- **Rule**: Interpret fields, accessors, aliases, wrappers, helper classes, registries, and implementation edges by the mathematics they denote, not by their software role.  Public mathematical nouns must be standard mathematical objects/data whenever such a referent exists.  Do not create an epistemic or administrative vocabulary (`knowledge`, `evidence`, `provider`, `manager`, `context`, `metadata`, `model`, `descriptor`, `record`, `info`, `result`, `factory`, `payload`, `adapter`, `backend`) to stand in for morphisms, functors, bases, sections, predicates, isomorphisms, or other standard data.

- **Rationale**: Code is one presentation of mathematics.  Treating declaration shape as ontology causes real mathematical content to be demoted to “plumbing” and then replaced by project-private concepts.  That private vocabulary expands rapidly because every later operation has to translate between it and the actual mathematical objects.

- **Violation Example**: `SubobjectEvidence` containing an inclusion; `GeneratorProvider` containing an indexed family; `NormalizationContext` containing an isomorphism; dismissing a local functor as a mere “realization edge” because it is stored in a helper field.

- **Correct Example**: Name the inclusion morphism, indexed family, isomorphism, or functor directly.  An engineering cache/adapter may have engineering vocabulary privately, but the mathematical layer exposes the standard object it implements.



#### `LEX-05`: Standard Mathematical Vocabulary Outranks Backend Vocabulary

- **Rule**: Public names follow the standard terminology of the mathematical literature and the repository's mathematical lexicon, even when Sage or another backend uses a different historical spelling.  Backend class/method names are preserved only inside backend calls and adapters; they do not determine the owned public noun or verb.

- **Rationale**: The preamble is a mathematical language, not a compatibility facade.  Importing backend terminology into the public API imports its historical conventions, implementation distinctions, and sometimes mathematically misleading names.  Standard vocabulary makes the same concept recognizable independently of the current engine.

- **Violation Example**: Call invariant factors merely `invariants` because Sage does; expose an FGP/backend class name as a mathematical category; retain an implementation-specific normal-form name for the object rather than the literature's object/invariant.

- **Correct Example**: Use `invariant_factors`, standard signature terminology, standard dual/functor names, and ordinary categorical nouns.  Private adapters may call Sage's `.invariants()`, `.gens()`, or exact backend class names while converting the result back into owned vocabulary.



#### `LEX-06`: Processes and Named Examples Do Not Become Mathematical Kinds

- **Rule**: A public type/category/constructor name must denote a reusable mathematical concept, not the process by which an ordinary object was generated or its role in a test/example.  Randomness, fixture/example status, “standard test object”, and similar modifiers generate/select data for existing constructors.  A named specimen may live in a catalogue without becoming a new category-level concept.

- **Rationale**: Reifying process labels produces artificial `Random*`, `Example*`, `Test*`, `Factory*` ontologies and then forces routing, methods, and documentation to distinguish objects that are mathematically just ordinary members of an existing category.

- **Violation Example**: `RandomLattices`, `RandomLatticeOfSignature`, `ExampleModule`, or a category API obligation for a local `rankTwo` example.

- **Correct Example**: `random_gram(...)` produces legitimate construction data and the ordinary lattice constructor consumes it; named objects such as `E8` live as catalogue specimens constructed by the same public lattice language.



#### `LEX-07`: Public Mathematical Names Never Encode the Current Algorithm or Computability Frontier

- **Rule**: Name a public operation by the mathematical concept it denotes.  Words describing the present decision procedure, engine, performance profile, or implementation branch—`partial`, `fast`, `cached`, `sage`, `gap`, `brute`, `PDOnly`, theorem-name-as-algorithm-adjective, etc.—belong in implementation notes/private adapters, not in the mathematical noun/verb.

- **Rationale**: The mathematical predicate stays the same as algorithms improve.  Encoding today's route in the name freezes a temporary computational boundary into the ontology and invites duplicate methods when a second algorithm arrives.

- **Violation Example**: `eichler_partial_is_isometric`, `sage_computable_genus`, `fast_kernel`, `cached_discriminant_group` as public mathematical operations.

- **Correct Example**: `is_isometric`, `genus`, `kernel`, `discriminant_group`; their implementations route among exact algorithms and assertion-gate the current frontier as needed.  The docstring/private implementation records which theorem/backend handles each case.

#### `LEX-08`: Distinguish a Mathematical Construction From the Numerical Operation Representing It

- **Rule**: When a numerical operation is the coordinate representation of a mathematical construction, name each at its own level.  In particular, matrices have a **Kronecker product**; linear maps/modules have tensor products.  Similar distinctions apply to Gram matrices versus forms, Smith matrices versus invariant-factor presentations, and coordinate vectors versus elements.

- **Rationale**: Reusing the mathematical noun for its representation makes callers reason about arrays as if they satisfied the universal property themselves and obscures where basis choices entered.

- **Violation Example**: “tensor product of two matrices”; “the Smith form of the module” when referring to the backend matrix; “the vector is primitive because its coordinate gcd is one.”

- **Correct Example**: the tensor product of morphisms has a Kronecker matrix in chosen bases; Smith normal form is the matrix computation producing an invariant-factor re-presentation; primitivity is the cokernel torsion-freeness predicate.



#### `LEX-09`: Public Category Names Are Standard Names for Identities, Not Substitutes for Their Definitions

- **Rule**: Use the standard plural/category notation when established, but retain the underlying owned construction/classifier expression as the mathematical definition.  Project/Sage aliases are metadata/presentations on that identity, never extra categories whose existence must be reconciled later.

- **Rationale**: Good names make the interactive language readable; definitions make the graph coherent.  Treating either as the other yields the two bad extremes: unreadable classifier-only APIs or a forest of independently named categories with duplicated semantics.

- **Violation Example**: expose only `Magmas.Associative.Unital.Inverse` when `Groups` is the established mathematical noun; or create `Groups` as a separate wrapper category around that classifier expression.

- **Correct Example**: `Groups` is the standard public name of the one owned category whose definition is the corresponding classifier/category expression; aliases and backend names resolve to that identity.


* * *

### 7. Sets, Collections & Cardinality (`SET-*`)

#### `SET-01`: Mathematical Collections Are Owned Sets or Families, Never Python Sequences

- **Rule**: Every mathematical collection inside the preamble—not only a public return value—is represented by its mathematical collection object: set, ordered set, multiset, ordered multiset, indexed family, image, product, coproduct, or another named construction.  Raw Python `list` and `tuple` are not mathematical storage types.  They may appear only as transient serialization at a private backend boundary after finiteness and ordering have already been established mathematically.

- **Rationale**: The mathematical collection determines equality, multiplicity, order, membership, cardinality, ranking/unranking, and available morphisms.  A Python sequence silently supplies finiteness and eager materialization.  Once a mathematical family is stored as a sequence, every downstream consumer is encouraged to use `len`, indexing, slicing, and whole-family traversal even when the same construction should work for an infinite ordered/indexed set.

- **Violation Example**: `self._generators = tuple(generators)`; `labels = list(M.module_generating_set())`; `module_generators() -> tuple[...]`; returning a list of subgroup representatives; converting an index set to a tuple merely to enumerate it twice; widening an input type to `Sequence` because callers pass lists.

- **Correct Example**: A generating family is an owned ordered/indexed set with `__iter__`, membership, cardinality, and when appropriate `rank`/`unrank`; repeated framing images form an indexed family over the framing set; conjugacy representatives form an owned set.  Consumers iterate lazily.  A private CAS adapter may finally serialize a *known finite* ordered set to the row/column array demanded by that backend, and that sequence does not escape the adapter.

#### `SET-02`: Cardinality and Order Are Cardinal-Valued; Finiteness Is Never Smuggled in by `len`

- **Rule**: Cardinality, group order, and element order use the repository's mathematical cardinal/integer objects appropriate to their definitions and do not silently assume finiteness.
  Use `cardinality()` for mathematical sets; use sequence length only for a private implementation container already known to be finite.

- **Rationale**: `len` is a programming operation with a finite machine-integer result.
  Treating it as cardinality makes infinite ordinary inputs unanswerable or converts a missing enumeration algorithm into a false mathematical finiteness claim.

- **Violation Example**: `order() -> int: return len(elements)`; raising from `cardinality()` merely because a module has positive rank; refusing to state the cardinality of a finitely generated infinite group because only finite groups are enumerable by the current engine.

- **Correct Example**: A finite free module over `F_q` has cardinality `q^n`; a finitely generated infinite group has countable underlying set when that theorem applies; an unknown cardinality is represented as unknown rather than forced through `len`.

#### `SET-03`: Set-Level Operations Are Owned Once by Sets and Standard Constructions

- **Rule**: Cardinality, finiteness, countability, membership, enumeration, products, coproducts, and other generic set operations live at the owned set layer or the standard construction that first has enough data to implement them.
  Structured descendants obtain those operations through their canonical forgetful/construction path rather than reimplementing the same set theory at every leaf.

- **Rationale**: A lattice, module, algebra, or group has an underlying set; it does not acquire a second definition of cardinality because it has extra structure.
  Centralizing set behavior prevents coordinate models and leaf-specific enumerators from becoming alternate definitions of the underlying set.

- **Violation Example**: A lattice-specific `cardinality()` multiplying invariant factors directly while the underlying finite group already owns cardinality; a module-level iterator returning coordinate tuples instead of module elements because a basis is available.

- **Correct Example**: A discriminant form inherits cardinality from its underlying finite abelian group; a chosen basis may supply an isomorphism with a coordinate product for computation, but iteration crosses back through the inverse and returns elements of the owned module.

#### `SET-04`: Finite Support Does Not Imply a Finite Underlying Family

- **Rule**: Distinguish an element having finite support from its parent/indexing set being finite.  Free modules, formal divisor groups, group/algebra monoid rings, sparse polynomial-like objects, and indexed sums may be built on infinite owned sets while each represented element uses only finitely many indices.  Do not coerce the whole indexing family to a finite ordered set merely because the current element or backend input is finite.

- **Rationale**: Conflating finite support with finite parent data is one of the main ways finitary assumptions spread through the API.  The correct abstraction keeps the parent infinite/lazy and lets each element expose its finite support.

- **Violation Example**: Defining the group of formal divisors by `finite_ordered_set(prime_divisors)`; materializing every module generator before forming a sparse linear combination; requiring a group ring's entire group to be enumerable in order to represent one finite group-ring element.

- **Correct Example**: `FormalDivisorGroup(R,S)` is the free `R`-module on the owned set `S`; a divisor is a finite-support coefficient map on `S`.  Algorithms consume only that support unless their theorem genuinely requires a finite parent.


#### `SET-05`: The Set API Is Closed Under Standard Set Constructions and Canonical Identifications

- **Rule**: Every owned object that is mathematically a set—ordinary sets, exponentials/function sets, Set-Homs, power sets, Cartesian products, coproducts, images, subobjects, and similar constructions—participates in the same owned set API.  Canonically identical set constructions are represented by one parent/object, not parallel implementations reached through different notation.

- **Rationale**: Set-level operations such as membership, cardinality, enumeration, indexing, maps, products, and coproducts should propagate through the standard construction graph.  If `Hom_Set(X,Y)` and `Y^X` are implemented separately, each acquires its own cardinality/enumeration/equality behavior and the architecture immediately forks.

- **Violation Example**: Maintain an independent power-set implementation beside exponentials; make Set-Homs a Homset object that does not receive ordinary set methods; compute function-set cardinality separately from Set-Hom cardinality.

- **Correct Example**: Own the canonical identifications `Hom_Set(X,Y)=Y^X` and `P(X)=2^X`; the one resulting parent has both Hom/exponential placements and inherits the complete set interface.  Cartesian products/coproducts likewise own their standard projections/injections and cardinal arithmetic at the set-construction level.



* * *

### 8. Computational Backend Delegation (`ENG-*`)

#### `ENG-01`: Delegate Heavy Algorithmic Computations to Exact Engines

- **Rule**: Route algorithmic algebra to established exact backends (SageMath, Singular, OSCAR, Macaulay2, PARI/GP) when a reliable implementation exists.

- **Scope**: Gröbner bases, syzygies, primary decompositions, Hilbert series, polynomial reduction, and local algebra computations.

- **Rationale**: Battle-tested engines provide numerical stability, optimized C/C++ implementations, and mathematical verification.

- **Violation Example**: Writing custom Python algorithms for multivariate polynomial division or Gröbner basis calculation.

#### `ENG-02`: Prohibition of Hand-Rolled Standard Mathematics

- **Rule**: Do not hand-roll algorithms or data structures available in mature upstream dependencies or Mathlib.

- **Rationale**: Custom mathematical algorithms create high maintenance overhead and lack formal verification.

- **Violation Example**: Implementing custom Smith Normal Form or LLL reduction instead of delegating to native library routines.

#### `ENG-03`: Minimal Owned Computation and Ecosystem Offloading

- **Rule**: Keep owned algorithmic logic strictly minimal.
  Always offload engine computations to established computational backends:

  - Upstream SageMath native modules

  - Heavy Python libraries (`networkx`, `numpy`, `scipy`)

  - Julia / OSCAR / Hecke (routed via `sage_julia_bridge`)

  - GAP (routed via `libgap`)

  - Singular, Macaulay2, Maxima, and PARI/GP

- **Rationale**: The preamble owns categorical representations, universal properties, and mathematical structures.
  Concrete computations belong to dedicated, verified engines.

- **Violation Example**: Writing custom graph connectivity or automorphism algorithms instead of delegating to `networkx` or Sage graph backends.

#### `ENG-04`: Native Engine Implementation with Preamble Category Wrappers

- **Rule**: When an algorithm requires multi-step engine computations, implement the engine logic directly in the target engine language (such as Julia/OSCAR or Singular) and wrap it with preamble category interfaces, whenever this reduces complexity or eliminates excessive cross-bridge data transport.
  The Python mathematical layer should prepare the owned mathematical input, cross once into the engine routine, and reconstruct the owned mathematical output; it should not become a line-by-line orchestration language for the engine's matrices, syzygies, lifts, or stabilizer workspaces.

- **Rationale**: Executes compute-heavy algebra natively in the host engine while exposing a uniform categorical interface to Sage sessions.
  A long Python routine whose dominant content is translating and reshaping intermediate engine objects is backend code in the wrong language and location.

- **Violation Example**: Transporting intermediate matrices back and forth across a language bridge in a loop when one native Julia routine can perform the reduction and return the final invariant; a hundreds-of-lines Python kernel routine manually building Singular augmented matrices, calling `syz` twice, reshaping every intermediate result, and calling `lift` before finally reconstructing the owned kernel.

- **Correct Example**: Pass the finite presentation and morphism data through one private Singular adapter whose native routine computes kernel generators, their relations, and lift data; cross back once and construct the owned presented kernel together with its inclusion and lifting morphism.

#### `ENG-05`: Rank Architectures by Human-Owned Complexity and Change Blast Radius, Not Dependency Weight

- **Rule**: Do not count an ordinary external dependency, build toolchain, package scaffold, or install step as an architectural disadvantage by itself.  When choosing between mature reusable infrastructure and a local implementation, compare the amount/scrutability of logic humans in this project must own, the future edit/review blast radius, and whether understanding is centralized for reuse rather than reimplemented by each consumer.

- **Rationale**: Most substrate complexity is shifted rather than eliminated.  Avoiding one dependency by writing a parser, graph algorithm, dispatcher, traversal, or algebra engine locally transfers the same conceptual cost into bespoke code that this project must reason about indefinitely and often multiplies it across consumers.

- **Violation Example**: reject a maintained tree-sitter grammar because it adds a C/build dependency and instead maintain handwritten parsing logic; avoid `networkx` to save a package while owning DFS/SCC/toposort implementations; avoid a mature dispatch library and accumulate hand-written case registries.

- **Correct Example**: prefer the dependency when it centralizes the generic problem and leaves the preamble owning only its mathematical semantics/adaptation.  Reject a dependency for semantic mismatch, correctness, maintenance/reliability, or inability to satisfy the owned boundary—not merely because it exists.



#### `ENG-06`: A New Nontrivial Mathematical Algorithm Requires a Demonstrated Backend Gap

- **Rule**: Before the preamble owns a new nontrivial mathematical algorithm, search the repository's backend/capability references and the relevant mature open-source systems for the semantic operation.  If a suitable exact implementation exists, wire it behind the owned mathematical method.  Bespoke implementation is justified only after the relevant alternatives have been checked and a real semantic/capability gap is established; if owning the algorithm materially expands the project's correctness burden, it requires an explicit project/user decision rather than an agent convenience choice.

- **Rationale**: The preamble should own the mathematical ontology and thin semantic routing, not duplicate decades of exact algebra/group/geometry algorithms.  LLMs readily write plausible local algorithms because doing so completes the immediate method; that silently transfers correctness, performance, and edge-case responsibility into this repository.

- **Violation Example**: implement local orbit/stabilizer enumeration without checking GAP; write polynomial syzygy/Groebner logic instead of Singular; implement lattice/form equivalence from scratch while Oscar/Hecke/Indefinite.jl/Sage already provide an exact route.

- **Correct Example**: identify the owned operation first, inspect the capability map/upstream documentation, add the narrow backend crossing, and return the owned result.  If no mature implementation actually exists, record that concrete gap and only then design the smallest source-grounded algorithm the project deliberately chooses to own.



* * *

### 9. Engine Crossing Boundaries (`BND-*`)

#### `BND-01`: Backend State Has One Private Owner and One Controlled Crossing

- **Rule**: Durable backend state is private to the owned object or private adapter that owns that computational realization.
  A backend datum has one private accessor or boundary helper at its owning layer; do not create public accessors, aliases, or unrelated direct field reads.
  A protected crossing used by another owned subsystem must be explicitly documented at its declaration and kept narrower than the public mathematical API.

- **Rationale**: Multiple ways to reach the same engine are multiple APIs.
  A single visible crossing makes the representation dependency auditable and prevents backend operations from spreading through ordinary mathematical consumers.

- **Violation Example**: Reading `_preamble_pid_engine` directly from discriminant modules while Internal Hom uses a separate engine accessor and a third consumer reaches Sage's `V()` through the owned module.

- **Correct Example**: A private presented-module adapter owns one optional Smith engine and one documented conversion boundary used by the few algorithms that require the FGP implementation; ordinary consumers never receive its parent or elements.


#### `BND-02`: Cross In, Compute, Cross Back

- **Rule**: A backend crossing converts owned inputs to the backend representation, performs the backend computation, and converts the result back before the boundary returns.
  Backend parents, elements, vectors, matrices, submodules, homsets, normal-form workspaces, GAP objects, and all other representation structures do not propagate past that computation site.
  There is no element exception: a backend element is backend data and must be converted to an owned element before return.

- **Rationale**: Backend delegation is safe only when the backend computes for the owned mathematics rather than becoming a second mathematical universe used by downstream code.
  Immediate conversion back keeps representation-specific assumptions local and makes backend replacement possible without changing mathematical callers.

- **Violation Example**: Internal Hom computes an FGP kernel and returns that Sage FGP module or its elements for later consumers to inspect; a lattice invariant returns a Sage kernel basis and expects its caller to reconstruct the lattice; an owned group operation returns a GAP element because GAP performed the multiplication.

- **Correct Example**: Cross an owned module morphism and its owned coefficients into Sage's FGP representation to compute a kernel, then construct the owned presented kernel, owned kernel elements, and owned inclusion before returning.


#### `BND-05`: Backend Conversion Is Private and Non-Exported

- **Rule**: Conversions such as "owned ring to Sage ring", "owned element to Sage element", "owned group to GAP group", and their inverses are private implementation functions or private adapter methods.
  They are not exported from `preamble.all`, package `__init__` modules, public classes, or notebook-facing namespaces.
  Ordinary repository code outside the owning adapter does not call them merely to continue computation in the backend.

- **Rationale**: A public `engine_ring`, `engine_element`, `engine_group`, `to_sage`, `from_sage`, or similar helper is an intentional escape hatch even if individual parents hide their `_engine` field.
  The firewall is real only when backend representations are unreachable through the public API and crossings are confined to the implementation that immediately converts back.

- **Violation Example**: Exporting `engine_ring(R)` so callers can construct Sage matrices over it; exposing `_smith_engine()` broadly enough that unrelated modules perform FGP operations directly; retaining `own_ring(raw_sage_ring)` as a notebook-facing adoption constructor.

- **Correct Example**: A private FGP adapter owns `_to_sage_ring`, `_to_sage_element`, and `_from_sage_element` locally, performs the whole Smith computation, and returns an owned tensor/module/morphism.  No public caller can obtain or supply those Sage objects.

#### `BND-03`: Dispatch on Declared Owned Mathematics, Never by Type Peeking

- **Rule**: Public and category-level behavior is selected by owned category membership, owned structure, or the object's owned operations.
  Do not use `isinstance`, `type(...)`, `hasattr`, `getattr`-probing, or `try/except AttributeError` to discover what mathematical structure an owned object has or which mathematical operation it supports.
  Matching on engine classes is permitted only inside a private engine boundary whose job is to select an engine-specific implementation after the mathematical operation has already been chosen.

- **Rationale**: Python class identity and method presence answer how an object happened to be implemented, not what mathematical structure it carries.
  Type- and capability-peeking recreate implementation hierarchies as hidden second category graphs and let consumers infer stronger structure than was declared.

- **Violation Example**: A scalar-multiplication routine branches on `FreeModule_generic`, FGP module, and quotient-module classes after receiving an owned module; code asks `hasattr(M, "presentation_matrix")` to decide whether `M` is presented; a public group method decides group structure by inspecting the Sage class of the owned parent.

- **Correct Example**: Ask the owned module for its scalar action or `scalar_multiple`; inside the private group-engine boundary, match on the Sage engine class only to choose the corresponding GAP/Sage algorithm and return owned results.

#### `BND-06`: Backend Correspondence Provides Capabilities; It Does Not Define the Category Taxonomy

- **Rule**: Maintain backend mappings as implementation/capability correspondences from owned mathematical categories/constructions to available Sage/GAP/Julia/etc. realizations and algorithms.  The correspondence need not be injective and is not an equality of taxonomies.  Backend category names, graph edges, MRO order, and equality do not create or identify owned mathematical categories.

- **Rationale**: Several backend categories may implement the same normalized mathematics, and one backend category may package a combination of structures differently from the owned graph.  The useful question is “which backend capabilities are available for this owned object/operation?”, not “how do I make the owned hierarchy mirror Sage's?”.

- **Violation Example**: Add an owned category only because a Sage category has no current target; require one-to-one mapping between Sage category names and owned categories; copy `super_categories()` edges into the mathematical graph as authoritative inclusions.

- **Correct Example**: the owned graph is fixed by mathematics; a private/versioned bridge records each meaningful backend realization and the operations it can supply.  Multiple backend realizations may inhabit the same capability fiber, and updating Sage versions changes only the bridge, not the mathematical ontology.

#### `BND-07`: Choose Incumbent-Library Coupling Deliberately: Owned Semantics, Ephemeral Computation, or Audited Runtime Adoption

- **Rule**: For each subsystem overlapping Sage/GAP/another incumbent, use exactly the coupling appropriate to the mathematics: (1) own/rewrite the semantic identity layer when the incumbent ontology is what the preamble replaces; (2) use an ephemeral backend realization for large standard algorithms returning owned mathematical data; or (3) adopt/extend an incumbent runtime type only for an adjacent structure whose ontology is mathematically sound and whose inherited surface has been audited for leaks.  Never drift accidentally between these modes.

- **Rationale**: Rewriting large mature algorithms is waste; durably wrapping the very ontology being replaced imports its assumptions; indiscriminate subclassing leaks host vocabulary.  Separating the modes keeps the public mathematics owned while still exploiting mature computation and legitimate host runtime structures.

- **Violation Example**: own a Python Smith-normal-form implementation (Mode 1 where Mode 2 is appropriate); store a Sage ambient-lattice object as the public/private identity of an owned lattice (Mode 3 on the replaced ontology); subclass a backend type without auditing inherited `ambient`/coordinate methods.

- **Correct Example**: the preamble owns lattice/subobject/Hom semantics; a private ephemeral Sage/Singular object computes SNF/genus/syzygies and is discarded; an adjacent backend group/matrix/runtime type may be adopted privately when its mathematical role is correct and its leakage is contained by the owned API/bridge.

#### `BND-04`: Never Repair an Ownership Violation with Compatibility Machinery

- **Rule**: When an owned object or element has been placed inside an engine object, an engine object has been reclassed as owned, or an owned parent has been made a facade over backend elements, fix that ownership seam.
  Do not compensate by joining Sage categories into owned parents, teaching Sage constructors to accept owned rings, adding coercion hooks, skipping problematic engine element types, preserving backend elements through facade parents, or installing backend protocol methods solely to keep the invalid embedding working.

- **Rationale**: These patches are symptoms of the same inversion: the engine has become responsible for understanding the owned universe.
  Each workaround expands the coupling and creates the next failure at coercion, element identity, category comparison, or constructor dispatch.

- **Violation Example**: Joining a Sage engine category into an owned ring so `FreeModule(owned_ring, n)` succeeds; skipping Cython element refinement because a reclassed permutation group loops in coercion; declaring Sage vectors to be the elements of an owned free module; adding `_im_gens_` only because a Sage algebra constructor received an owned module parent.

- **Correct Example**: A private adapter converts owned ring elements to Sage ring elements, builds a Sage free module or FGP workspace entirely on the backend side, computes there, and converts all outputs back.  A private group adapter may use a Sage/GAP group model, but public group parents and elements remain owned.  No backend category join, facade parent, reclassification, or backend-element exception is required.


#### `BRG-01`: Structured Engine Bridges Over Ad-Hoc Shelling

- **Rule**: Route communication with external systems (such as Julia, OSCAR, or Macaulay2) through persistent bridge interfaces (`sage_julia_bridge`, `JuliaHandle`, or C-APIs).

- **Rationale**: Shelling out via subprocesses with temporary disk files causes process overhead, unmanaged temporary state, and fragile error handling.

- **Violation Example**: Using `subprocess.run(["julia", "script.jl", tmp_file])` inside an inner loop instead of calling a persistent `JuliaHandle`.

#### `BRG-02`: Explicit Mathematical Interface Boundaries

- **Rule**: Translate data explicitly across bridge boundaries.
  Validate input types and convert results into owned repository types immediately upon return.

- **Rationale**: Keeps engine-specific representation leaks out of the public category API.

- **Violation Example**: Leaking raw engine pointers or un-wrapped backend matrix wrappers into user-facing category elements.

* * *

### 11. Environment, Execution & Tooling (`ENV-*`)

#### `ENV-01`: Strict Physical Path Resolution for Commands

- **Rule**: Use exact physical filesystem paths (such as `/home/dzack/research`) for shell commands, execution targets, and subprocess invocations.

- **Rationale**: Virtual mount aliases (such as `/research`) fail in standard POSIX shells and background tasks.

- **Violation Example**: Passing virtual root `/research` to a shell execution tool.

#### `ENV-02`: Deterministic Recipe Execution via Justfile

- **Rule**: Declare all project orchestration, gates, and documentation generators in the root [`justfile`](justfile).

- **Rationale**: Ensures reproducible execution across developer environments, CI pipelines, and automation tools.

- **Violation Example**: Running undocumented one-off ad-hoc bash scripts for builds or tests.

* * *

### 12. Development Discipline & Verification (`DEV-*`)

#### `DEV-01`: Strict Typing Without Opaque Types

- **Rule**: Type all public functions, methods, and classes explicitly.
  Do not use `Any`, `object`, `unknown`, or silent type ignores.

- **Rationale**: Types communicate mathematical intent and enable static correctness checks.

- **Violation Example**: Annotating a morphism constructor with `def __init__(self, data: Any) -> object:`.

#### `DEV-02`: Specimen-First Falsification Discipline

- **Rule**: Accompany every new category, functor, or operation with a concrete, falsifiable mathematical specimen.

- **Rationale**: Progress is measured by mathematical specimens that can fail, not by uninstantiated schemas.

- **Violation Example**: Adding abstract category definitions without a test specimen or executable verification.

#### `DEV-03`: Consult Megadoc, TODOs, Reuse Constructions, and Implement at Maximal Generality

- **Rule**: Before adding or changing code under `src/dzack_research/preamble/`, read the generated megadoc output `docs/preamble-megadoc.md` and all current root-level `*TODO*.md` files governing preamble work (currently `TODO.md`, `TODO-ORGANIZATION.md`, and `PORT_TODO.md`).
  Reading the generator `src/dzack_research/utilities/megadoc.py` does not satisfy the megadoc requirement; if the generated document may be stale, run `just preamble-megadoc` and then read the generated output.
  Always reuse existing constructions when they are mathematically correct and principled.
  When a required construction does not exist, implement it at its most mathematically general level (in its native abstract category or module layer) and progressively specialize and share it across concrete domains.

- **Rationale**: Prevents duplicate definitions, competing APIs, already-recorded remediation from being reintroduced, and siloed mathematical implementations while ensuring global functorial coherence.

- **Violation Example**: Implementing an ad-hoc direct sum or orthogonal quotient exclusively for lattices without checking the megadoc for the general construction; adding a new tuple-valued framing helper while `TODO.md` already records the owned-family remediation; recreating a known architecture problem already catalogued in `TODO-ORGANIZATION.md`.

- **Correct Example**: Read the generated construction inventory and active remediation queues first; reuse the existing tensor product, Hom, subobject, or functor when it already expresses the mathematics, and add a missing operation at the category where its definition belongs rather than at the first concrete consumer that needs it.

#### `DEV-04`: Real Sets Over Manual Deduplication

- **Rule**: Never manually use "iterate + seen" patterns to deduplicate. Always form actual sets, usually a one-liner with a comprehension, or map/filter/reduce equivalents.

- **Rationale**: Forming a set states the mathematical operation — the collection, its membership, its cardinality — in one expression. A hand-written "seen" loop re-implements set semantics silently, hiding the operation and inviting order- and mutability-dependent bugs.

- **Violation Example**: Accumulating into a `seen` list with `if x not in seen` inside a loop instead of writing `set(xs)` or a set comprehension.

#### `DEV-05`: Architecture Conformance Precedes Suite Counts

- **Rule**: For an architectural change, first state what the affected mathematical object is: its owned data, category, public operations and return types, optional private engine state, and permitted engine crossings.
  Implement to that statement and read the resulting code against it before using aggregate test or type-error counts as feedback.
  Only then run tests as falsifiable specimens of the mathematics and its real consumers.

- **Rationale**: A pass count over a wrong architecture measures compatibility with the wrong architecture.
  Treating failures as a work queue encourages adding delegations, coercions, and backend aliases until the number falls, which can make the ownership defect deeper while making the suite greener.

- **Violation Example**: Seeing 53 failures after an ownership refactor and adding `coordinate_vector`, `gen`, `cover`, and Sage-category delegations one-by-one because each makes several tests pass.

- **Correct Example**: State that a presented module owns its presentation and framing, has only a private optional Smith engine, and returns no Sage module/vector/submodule; inspect every public method and consumer against that statement, then run the module, Hom, discriminant, and lattice specimens.

#### `DEV-06`: Tests Specify Mathematics and Consumer Contracts, Not Delegation

- **Rule**: Tests of owned mathematics assert mathematical objects, morphisms, categories, domains and codomains, chosen data, invariants, subobjects, tensors, and actual downstream operations.
  Do not add a test whose claim is merely that an owned object still carries an engine method or delegates to the engine under Sage's spelling.

- **Rationale**: A delegation test converts an implementation leak into a compatibility promise and makes deleting the leak look like a regression.
  Tests should fail when the mathematics is wrong, not when a backend escape hatch has been closed.

- **Violation Example**: Asserting `M.coordinate_vector(x) == M._engine.coordinate_vector(x)`, `hasattr(M, "gen")`, or that an owned subobject is a Sage submodule.

- **Correct Example**: Assert that `module_coefficients(x, M)` gives the coefficients in the selected framing, that a presentation matrix is the expected tensor, that a computed kernel comes with the correct owned inclusion, or that an invariant-factor normalization is connected to the original module by the claimed isomorphism.

#### `DEV-07`: Ownership Migrations Rewrite Their Consumers; They Do Not Preserve the Leak

- **Rule**: When an owned representation or boundary changes, sweep the repository for consumers of the old representation and rewrite those consumers to the owned operations in the same architectural change.
  Do not retain or reintroduce a public compatibility alias merely to defer that consumer migration.

- **Rationale**: A public compatibility layer makes the old representation a supported second API and guarantees that new code will continue to use it.
  The purpose of an ownership migration is to remove that route, so downstream breakage identifies consumers that must be repaired rather than methods that must be delegated.

- **Violation Example**: After replacing a reclassed or backend-element free module by a genuinely owned module, keep `.gen()`, `.basis_matrix()`, and `.coordinate_vector()` because Internal Hom, free resolutions, and lattice invariants still use those names.

- **Correct Example**: Rewrite those consumers to `module_generator`, `module_coefficients`, morphism tensors, `presentation_matrix`, `subobject_on`, and the documented private engine crossing where a specialized Smith computation is genuinely irreducible; then delete the old engine spellings from the public surface.

#### `DEV-08`: Promote Durable Repository Memory into Concrete Policy Codes

- **Rule**: Agent memory records history, rationale, traps, and prior decisions; it is not the repository's contributor-policy surface.
  When a ruling is stable, repository-wide, repeatedly relevant, and recognizable from concrete code or API shape, promote it into a uniquely named policy code in this document with a rule, rationale, violation example, and correct example.
  Task-local decisions, historical implementation details, contradictory records, and superseded rulings remain memory and are not promoted.

- **Rationale**: A durable architectural rule that exists only in agent memory is invisible to contributors who do not retrieve that exact record and will be rediscovered after the same mistake recurs.
  Concrete policy codes make the rule reviewable at the point of contribution while memory remains the provenance and historical explanation.

- **Violation Example**: Relying on a memory titled "close the coordinate hatch" to reject public Sage vectors while `CONTRIBUTING.md` contains only a generic backend-encapsulation rule; copying an old contradictory memory into policy without checking the current architecture.

- **Correct Example**: Promote the stable coordinate ruling as `API-02`, the constructor/witness rulings as `CON-*`, and the definition-vs-criterion ruling as `DEF-01`; leave episode-specific history and superseded mechanisms in the memory vault.

#### `DEV-09`: Promote Newly Discovered Architectural Rules Before Continuing the Remediation

- **Rule**: When investigation or a failed remediation reveals a repository-wide architectural principle that is absent, ambiguous, or contradicted in this document, update the relevant policy code before continuing implementation.
  The implementation then proceeds against the corrected written rule.
  Do not rely on the current conversation, agent memory, or an informal correction as the only statement of a newly discovered invariant.

- **Rationale**: Architectural remediation is iterative: a local failure can expose a missing lower-level object or an incorrect ontology.
  If that discovery is not immediately made durable, the next contributor or agent can repeat the same mistake while still technically following the written policies.

- **Violation Example**: Discovering that matrices need a first-class owned category, discussing that conclusion in chat, and then continuing to patch `tensor.matrix` while `CONTRIBUTING.md` still teaches only generic backend encapsulation.

- **Correct Example**: Add the fundamental-object/refinement and category-method rules (`ARC-09`, `CAT-05`) first, then implement owned matrix spaces and rewrite tensor/module consumers to those rules.

#### `DEV-10`: Repeated Mathematical Implementations Signal a Missing Abstraction

- **Rule**: When two or more implementations repeat the same mathematical state and operations, factor the shared mathematics into the appropriate category, common parent/element implementation, universal construction, or parameterized abstraction.
  Do not preserve duplication by copying methods, assigning sibling methods one-by-one, or maintaining parallel classes whose differences are only additional structure.
  The abstraction must remove implementations, not merely add another wrapper around the duplicates.

- **Rationale**: DRY in this repository is mathematical, not textual.  Repeated code for the same finite-support graded sum, Homset module structure, indexed enumeration, or transported action means the common mathematical object has not been represented strongly enough.
  Copying the implementation makes later fixes theory-by-theory and lets supposedly identical operations drift.

- **Violation Example**: `PowerAlgebraElement` reimplementing the component normalization, homogeneous pieces, addition, negation, scalar multiplication, equality, and display already implemented by `GradedDirectSumElement`; `GroupModuleHomset` and `GradedModuleHomset` copying a dozen `ModuleHomset` methods by assignments such as `base_ring = ModuleHomset.base_ring`; four indexed symbolic-function parents each reimplementing the same `rank`/`unrank`/membership/infinite iteration loop.

- **Correct Example**: Use the graded direct sum as the additive/module realization of a power algebra and refine it with multiplication/unit structure; express specialized module Homsets through the common module-Hom category/implementation; provide one parameterized indexed-symbol set whose prefix/indexing data specializes to Hermite, Fourier, Laurent, and sinc families.

#### `DEV-11`: Assertions State Proof Context and the Current Computational Frontier

- **Rule**: Use assertions liberally throughout mathematical code to state hypotheses, category containments, parentage relations, finiteness/nondegeneracy assumptions, shape constraints, derived identities, and the hypotheses under which the selected algorithm is currently total. Assertions are part of the readable proof skeleton of the code. They are not exception-style control flow and are not used as whole-method placeholders.

- **Rationale**: This repository is a Sage research preamble used interactively. Mathematical code should read like a derivation under explicit assumptions. The implementation should loudly expose both what mathematics is being assumed and where current computability stops. This keeps API placement mathematically correct without pretending that every mathematically defined operation is currently decidable for every represented object.

- **Violation Example**: Omitting a finite-rank hypothesis and letting a later matrix constructor fail opaquely; replacing `assert self.is_nondegenerate()` by exception-valued mathematical control flow; defining a method whose first and only statement is `assert False`; using `NotImplementedError` as the default implementation.

- **Correct Example**: Keep `cardinality()` on all sets and assertion-gate only a represented case not covered by current algorithms. Keep `is_nondegenerate()` on formed modules and assert the representation/finite-rank hypothesis needed by the current decision procedure. Use Sage `@abstract_method` only for a genuine implementation contract, and place genuinely narrower mathematics on the narrower category.

#### `DEV-12`: Canonical Identity and Memoization Use One Shared Mechanism

- **Rule**: Do not invent a new module-global `dict` cache for each mathematical construction when the repository or Sage already provides the required canonicalization/memoization semantics.
  Identity-sensitive constructions use one shared identity-memoization helper or an appropriate `UniqueRepresentation`/`cached_function`/`cached_method` mechanism with an explicit lifetime and identity policy.
  A theory-local cache is justified only when its semantics genuinely differ and that difference is documented at the cache definition.

- **Rationale**: Ad-hoc `id(obj)` dictionaries repeatedly reimplement weak identity checks, stale-entry handling, ownership of cached results, and lifetime policy.
  Different theories then acquire subtly different notions of when "the same construction" returns the same object.
  Canonical object identity is architectural behavior and should be reviewable in one place.

- **Violation Example**: Separate `_MODULE_TENSOR_PRODUCT_CACHE`, `_MODULE_POWER_CACHE`, `_DIVIDED_SQUARE_CACHE`, `_KAHLER_CACHE`, `_DE_RHAM_CACHE`, three form-space caches, and similar dictionaries each implementing their own identity-key convention and cached-object verification.

- **Correct Example**: Route identity-sensitive mathematical factories through one shared identity cache that verifies referent identity (and uses weak references where appropriate), or use `UniqueRepresentation`/`cached_function` when their equality/key semantics are mathematically correct.  A specialized cache documents why the shared mechanism cannot express its required semantics.

#### `DEV-13`: A Missing Semantic Abstraction Is Part of the Current Task

- **Rule**: Do not optimize for the smallest local diff when the requested feature exposes a missing or defective semantic API. Strengthen the common mathematical owner first, then implement the feature through it. A task that needs `f.kernel()`, a subobject pullback, a block Hom, an owned orbit set, or a theorem-backed predicate includes making that operation usable if the alternative is a local coordinate workaround.

- **Rationale**: LLMs strongly prefer completing the visible local TODO with information already at hand. In mathematical software this produces papercuts that permanently encode implementation accidents. Repository quality improves only if local work is allowed to reveal and repair lower-level semantic gaps. This is not uncontrolled scope growth: the lower-level change is justified exactly by the mathematical dependency of the requested feature and should make the original caller simpler.

- **Violation Example**: A cohomology task discovers that `image()`/`kernel()` do not compose cleanly, so it builds a bespoke augmented matrix and returns a presentation. An isotypic-component task lacks a suitable subobject kernel and writes `_kernel_subobject_of_matrix`. A lattice predicate lacks a structural cokernel predicate and computes minors locally.

- **Correct Example**: Repair `kernel`/`image`/subobject quotient composition, then define cohomology by those operations; improve the common module-Hom kernel and delete `_kernel_subobject_of_matrix`; expose torsion-freeness on the cokernel and define primitivity through it. The local feature becomes shorter while the semantic spine becomes more capable for every future consumer.

- **Review Question**: “If the low-level semantic API were complete, would most of this new code disappear?” If yes, repair that API before accepting the local implementation.


#### `DEV-14`: Contaminated Prescriptions Are Architecture Defects

- **Rule**: Treat issue bodies, plans, comments, docstrings, examples, tests, migration notes, and generated/reference artifacts as executable prescriptions for future contributors.  When a ruling falsifies one, repair or delete it at the source before implementation continues.  Do not leave contradictory prose beside corrected code.

- **Rationale**: Agents and humans correctly follow authoritative-looking records.  A stale prescription therefore has multiplicative blast radius: it recruits compliant future work to recreate a rejected ontology.  Documentation consistency is not cleanup after implementation; it is part of preventing recurrence.

- **Violation Example**: Correct the subobject implementation but leave an issue body requiring “shared ambient coordinates”; replace a numerical `is_primitive` implementation but retain a docstring describing its old matrix criterion; delete an API while preserving a generated reference test that demonstrates it.

- **Correct Example**: Update the governing issue/plan/docstring/test in the same ruling/migration, remove fossils, and ensure every surviving example teaches the current semantic route.

#### `DEV-15`: Mathematically Correct Failures Are Evidence, Never Targets for Weakening

- **Rule**: If a mathematically correct assertion, sourced test, or original acceptance claim fails, preserve the proposition and repair the code/architecture it falsifies.  Do not delete the assertion, weaken the test, narrow the claimed requirement after the fact, or patch an unrelated symptom merely to make the run green.

- **Rationale**: The failure is the information.  Weakening the proposition destroys the evidence and converts an incomplete implementation into a false success.  Once that weakened record becomes authoritative, it contaminates future work as well.

- **Violation Example**: A correct subobject test fails because ambient-coordinate machinery is wrong, so the test is removed as “oversized”; a true assertion is called incidental and deleted; a PR description silently drops a requirement that the implementation missed.

- **Correct Example**: Keep the assertion/test/contract fixed, trace the failure to the semantic defect, and repair or restart the implementation while preserving the original mathematics.

#### `DEV-16`: No Compatibility Shims for Superseded Preamble APIs

- **Rule**: When the owned API is corrected, migrate all repository callers and remove the superseded spelling/representation.  Do not preserve aliases, adapters, fallback signatures, or old constructor forms solely for backward compatibility unless the user explicitly designates a stable compatibility surface.

- **Rationale**: This research preamble is allowed to make breaking corrections.  A shim leaves the rejected ontology constructible, creates two sources of truth, and teaches new code to keep using the route the migration was meant to eliminate.

- **Violation Example**: Keep `generators()` and add `module_generators()` as a wrapper over it; retain `from_matrix()` publicly after introducing the presentation-morphism constructor; accept both `ambient=` and the new inclusion object.

- **Correct Example**: Make the precise semantic API canonical, update every caller, remove the old route, and let failures expose any consumer that has not migrated.  Deliberate session shorthand is judged separately as language design, not compatibility debt.

#### `DEV-17`: QC Findings Never Justify Semantically Empty Code

- **Rule**: Do not add code, wrappers, casts, suppressions, dynamic imports, or annotations whose only function is to silence a linter/type checker or reduce a diagnostic count.  First decide whether the diagnostic exposes a real mathematical/API defect or a missing fact in shared tooling.  Repair the appropriate layer.

- **Rationale**: Local suppression launders useful evidence in exactly the same way as weakening a mathematical test.  In a Sage-heavy dynamic system, checker gaps should be repaired in stubs/plugins/configuration rather than by corrupting otherwise correct mathematical source.

- **Violation Example**: `del x` inside an `@abstract_method`; a broad `cast(Any, ...)` around a category operation; `# type: ignore` on every dynamic category method; an import wrapper created solely because static analysis cannot follow Sage.

- **Correct Example**: Fix the real signature/owner when wrong; otherwise improve the Sage stub/plugin/QC rule centrally.  A narrow external-boundary suppression requires an explicit boundary reason and must not mask owned mathematical structure.

#### `DEV-18`: Nontrivial Mathematical Claims and Manual Algorithms Are Source-Grounded

- **Rule**: A nontrivial mathematical test, hand-coded criterion, or owned algorithm is grounded in a definition/theorem already encoded by the semantic API or in an authoritative mathematical source.  Prefer delegating to an existing trusted implementation.  When project code must own a nontrivial computation, record the theorem/hypotheses it implements and test sourced specimens.

- **Rationale**: LLM recall reliably preserves the shape of conclusions while dropping hypotheses.  Source grounding makes the theorem and its domain reviewable and prevents an attractive numerical criterion from silently becoming a universal claim.

- **Violation Example**: Implement a lattice predicate by a remembered determinant/gcd criterion with no cited hypotheses; add a fixture whose expected invariant was guessed from another example; manually diagonalize a quadratic form when Sage already provides the exact invariant.

- **Correct Example**: Implement the predicate from its mathematical definition through owned operations; let the low-level owner use a sourced criterion in the category where its hypotheses hold; cite/test canonical literature specimens for any genuinely owned nontrivial mathematics.


#### `DEV-19`: Stress-Test New Abstractions Against Infinite and Weak-Hypothesis Examples

- **Rule**: During design/review of a new mathematical interface, deliberately test examples outside the easiest finite-coordinate regime: infinite or nonenumerable index sets, nonfree/projective modules, noncanonical presentations, infinitely generated groups/actions, and base rings outside the first engine's sweet spot.  The example need not be currently computable; it tests whether the API states the mathematics without accidental hypotheses.

- **Rationale**: Ordinary fixtures overwhelmingly come from finite free objects and therefore fail to expose representational assumptions.  A stress object such as `Free_R(S)` for a nonenumerable set `S`, or an infinite-rank callable formed module, reveals immediately whether the proposed API incorrectly stores tuples, assumes complete enumeration, or identifies a morphism with a matrix.

- **Violation Example**: Approve an indexing API because all tests use `[n]`; approve `is_nondegenerate()` only after testing finite Gram matrices; define a group-action construction solely from finite generator images because every current group fixture is finitely generated.

- **Correct Example**: Ask whether the same method signature and mathematical return type still make sense for arbitrary `S`, infinite rank, or a predicate-defined group.  Keep the semantic API if it does; assertion-gate or specialize only the current algorithmic cases.



#### `DEV-20`: Tests of Weaker Equivalence Relations Use Distinct Objects

- **Rule**: A test of isomorphism, isometry, same-genus, equivalence, conjugacy, or another relation weaker than equality uses specimens that are not already equal by the repository's equality semantics.  Prefer independently constructed presentations/objects so the tested relation has real work to do.

- **Rationale**: Equality implies every weaker equivalence relation.  Testing `X.is_isomorphic(X)` or testing two inputs that canonicalize to identical objects cannot falsify the nontrivial algorithm and gives a misleading green result.

- **Violation Example**: Test lattice isometry using the same lattice object twice; test invariant-factor classification only by normalizing one module and comparing it with itself.

- **Correct Example**: Construct two non-equal framed modules known to be isomorphic and test the returned witness; construct two different Gram presentations of an isometry class; use distinct representatives known to lie in one genus when testing genus equivalence.

#### `DEV-21`: The Mathematical Model Precedes Engineering Mechanism

- **Rule**: Before proposing overloads, optional parameters, adapters, wrappers, registries, casts, dispatch tables, or inheritance changes, state the mathematical objects involved, the defining datum, the natural owner of the operation, its domain hypotheses, and its mathematical codomain.  Choose engineering machinery only after this model is fixed.

- **Rationale**: Many apparent software-design dilemmas disappear when two conflated mathematical operations are named correctly.  Starting from Python mechanisms encourages preserving the accidental current signature and solving around it; starting from mathematics determines whether the method should move, split, disappear, or become a standard categorical construction.

- **Violation Example**: Debate overload signatures for `is_open` before distinguishing an ambient-space predicate `X.is_open(U)` from a subobject predicate `U.is_open()`; design adapters around a matrix-returning API before asking whether the result is actually a Hom element.

- **Correct Example**: Write the intended mathematical signature first—object/morphism/Hom/functor and codomain—then select the simplest implementation mechanism that realizes it.  If the mathematical statement makes the proposed machinery unnecessary, delete the machinery from the plan.

#### `DEV-22`: Review Findings Diagnose Generators; They Are Not Local Patch Specifications

- **Rule**: When review reports an architectural violation, do not turn the literal finding into a work unit whose hidden constraint is “remove this occurrence while preserving the current implementation and tests.”  Reconstruct the governing mathematical rule, inspect sibling instances/consumers, and repair the generator/owner that produced the finding.

- **Rationale**: A local remediation prompt makes an agent optimize the contaminated tree.  Responsibility then migrates from one helper to another—wrapper, adapter, alias, registry, fixture—while the same semantic defect survives.  Architectural review is useful precisely because the reported occurrence points beyond itself.

- **Violation Example**: Move an illicit matrix kernel from `cohomology()` into `_kernel_helper()` and call the finding resolved; replace a global switchboard by a registry that still owns every descendant; remove an old public API while forbidding edits to all of its known consumers.

- **Correct Example**: Identify the missing `kernel`/subobject/category abstraction, fix it at its mathematical owner, migrate all consumers, then delete the local workaround.  Treat representation-level tests that only preserve the condemned implementation as migration targets rather than immutable acceptance criteria.



#### `DEV-23`: Architectural Migrations Are Allowed to Be Sweeping and Breaking

- **Rule**: During an explicitly architectural preamble migration, optimize for the final mathematical architecture rather than for a sequence of horizontally “safe” compatibility-preserving edits.  Move responsibility to its final owner, migrate the vertical consumer slice, and delete superseded machinery.  Do not invent an incremental-green requirement that the user/project has not imposed.

- **Rationale**: A local compatibility constraint causes work to be spent stabilizing code that the correct architecture will delete and encourages wrappers/shims that preserve the rejected model.  Long-horizon research infrastructure may legitimately be temporarily inconsistent while a coherent vertical migration is in progress.

- **Violation Example**: Keep the public coordinate-vector API because rewriting all kernel consumers in one pass would temporarily break tests; add adapters around a global dispatcher instead of moving each operation to its owner; refactor code scheduled for deletion merely to keep every intermediate commit green.

- **Correct Example**: Make the owner/category change, migrate all affected consumers in that architectural slice, remove the old route, and evaluate correctness against the final mathematical model.  Verification requirements remain whatever the active repository instructions actually state; “safe” incrementalism is not assumed.

#### `DEV-24`: A Misplaced Mathematical Concern Triggers an Ownership Audit

- **Rule**: When a specialized/deep module is performing mathematics that obviously belongs to a more general construction, stop local implementation and audit ownership before adding another patch.  Search for sibling copies, identify the general semantic owner, and determine why the abstraction failed to propagate there.

- **Rationale**: Misplaced concerns are high-signal architecture defects.  A lattice leaf calculating generic set cardinality, or a subobject leaf implementing generic quotient machinery, means downstream code has crossed a boundary that should have been closed.  Fixing only the immediate line makes the architecture harder to see and usually leaves duplicates elsewhere.

- **Violation Example**: Optimize a cardinality algorithm inside a lattice-specific file; add another quotient helper to a deeply nested subobject implementation; repair a scheme-specific product routine without checking the generic categorical product owner.

- **Correct Example**: Pause the local change, trace the operation to `Sets`, `Hom`, quotient/cokernel, product, or other general owner, repair that layer, then let the specialized code reduce to delegation or disappear.



#### `DEV-25`: Verified Mathematical Facts Are Reusable Data; Tests Are Thin Drivers

- **Rule**: Stable externally verified mathematical facts used as test expectations belong in a centralized topic-organized fact/fixture corpus independent of any one implementation spike.  Each fact records enough mathematical identification to reconstruct the specimen, the expected value/statement, provenance (literature bibkey, source-system doctest, or independent oracle as appropriate), and verification status.  Tests consume this corpus parametrically rather than scattering literal expectations throughout test bodies.

- **Rationale**: A named invariant, classification row, orbit count, discriminant form, genus separation, or number-field fact is mathematical data reusable by multiple implementations and frontends.  Embedding it separately into individual tests duplicates provenance and allows contradictory expectations to accumulate.  A centralized corpus also prevents the implementation under test from silently becoming its own oracle.

- **Violation Example**: Copy `240`, a discriminant tuple, or a list of genus representatives into several test functions with no citation; generate a “golden” expected value by running the same method and saving its output.

- **Correct Example**: Store the cited/verified fact once in the mathematical fixture corpus; a thin test constructs the specimen through the current preamble API and checks the computed invariant against the fixture.  Backend parity data is clearly marked as such and is not promoted to mathematical truth without an independent basis.




#### `DEV-26`: Scope Defaults to the Strongest Coherent Mathematical Interpretation

- **Rule**: When a requested mathematical capability has a clear coherent general meaning, implement/analyze that capability rather than silently reducing it to representative examples, a percentage target, a wrapper, an audit artifact, or the currently easiest backend-supported subset.  Decomposition into work units is allowed; relaxation/removal of the mathematical target requires an explicit user/project ruling.

- **Rationale**: LLMs often convert difficult implementation obligations into tractable proxies and then optimize the proxy.  In a long-horizon research workbench this permanently shrinks the language around today's implementation limitations and produces exactly the local-special-case architecture the project is designed to avoid.

- **Violation Example**: Replace “support arbitrary framed modules” by “support the finite free fixtures”; turn “implement all relevant set constructions” into an inventory report; declare an infinite analogue out of scope solely because the current matrix engine is finite.

- **Correct Example**: keep the general semantic object/API as the target, implement the currently computable cases with the documented assertion frontier, and leave genuinely unimplemented cases as explicit remaining work rather than redefining the feature downward.



#### `DEV-27`: Mathematical Verification Uses a Definition, Complete Invariant, or Explicit Witness—Never an Easier Necessary Proxy

- **Rule**: A test/check claiming a mathematical property must be capable of failing on a false instance of that property.  Verify through the definition/universal property, an explicit witness, or a cited complete invariant/classification theorem whose hypotheses are stated.  A necessary but insufficient numerical invariant is not verification merely because it is easy to compute.

- **Rationale**: The characteristic LLM shortcut under mathematical difficulty is to replace “find/prove the isometry”, “prove completeness”, or “check reducedness” by a determinant, count, fingerprint, invariant-factor, or cardinality comparison.  Such checks can remain true for mathematically false outputs and therefore certify nothing about the claimed result.

- **Violation Example**: equal discriminant-group invariant factors used as proof that two discriminant **forms** are isometric; determinant preservation used as proof of basis reducedness; equal cardinalities used to certify a computed orbit/root/vector set is complete; a tautological `|H|^2=|A|` check used as proof that a generated subgroup has the required property.

- **Correct Example**: exhibit/check the isometry; call a genuine reducedness verifier; compare against an independent complete enumeration; or invoke a cited complete classification invariant at its semantic owner.  Difficulty of the correct check is a blocker/algorithmic frontier, never permission to weaken the proposition.

#### `DEV-28`: Negative Tests Must Establish a Live Positive Surface First

- **Rule**: A test whose main claim is absence, rejection, non-membership, or lack of a capability must also establish enough positive behavior that a dead/empty/misconstructed object could not pass it.  Prefer testing the positive mathematical universal property that implies the intended absence rather than testing deletion itself.

- **Rationale**: `not hasattr`, empty-result exclusions, and “this removed API is absent” assertions pass on objects with no functionality at all.  They are especially dangerous after refactors because they test the agent's own deletion rather than the behavior the deletion was meant to protect.

- **Violation Example**: assert a tensor product has no projections by `not hasattr`; assert a forbidden element is not in a result without proving the enumerator returned the expected nonempty/complete population; fabricate a removed compatibility artifact and assert the new code ignores it.

- **Correct Example**: test the tensor-product universal property positively; establish a sourced positive result/count/completeness witness before exclusions; regression-test the owned behavior that previously failed instead of the textual absence of the old code.



#### `DEV-29`: Use Sage's Native Conformance/TestSuite Machinery for Sage Runtime Contracts

- **Rule**: When verifying that an adopted/generated Sage `Parent` or `Element` satisfies Sage-level abstract/runtime obligations, use Sage's existing `TestSuite` / `_test_not_implemented_methods` / category tests rather than hand-rolling `dir()`, `getattr`, exception filtering, or a parallel conformance checker.  This is host-runtime verification only; mathematical behavior still uses the repository's sourced specimens and semantic tests.

- **Rationale**: Sage already knows how its dynamic category/abstract-method machinery is surfaced.  A custom introspection sweep is narrower, duplicates framework behavior, and tends to turn host implementation details into a second project ontology.

- **Violation Example**: loop over `dir(obj)`, call each attribute, catch `NotImplementedError`, and maintain a project list of “required Sage methods.”

- **Correct Example**: use Sage's native conformance test for the adopted runtime object, while separate mathematical tests assert kernels, universal properties, invariants, morphisms, and other owned semantics.



#### `DEV-30`: Fix Owned Defects at Their Authoritative Source During the Task

- **Rule**: When implementing a feature exposes a concrete defect/papercut in an authoritative component of the user's owned project stack and that defect lies on the feature's actual dependency path, repair it at its source before continuing.  Recording it in a TODO, filing an issue, reporting it, or adding a downstream workaround is not completion of the discovered defect.  Preserve unrelated dirty work and normal scope boundaries; this rule is about following the real mathematical/implementation dependency to its owner, not gratuitous cleanup.

- **Rationale**: Reporting a fixable upstream defect as “known” feels cautious to an agent but leaves every downstream caller compensating for it.  The resulting Protocols, local stubs, facades, aliases, and copied computations turn one source defect into permanent distributed complexity.

- **Violation Example**: the preamble's type/API is wrong, so a downstream research script defines a local Protocol instead of repairing the preamble; a missing semantic `kernel` capability is noted in `TODO.md` while the current feature ships a matrix workaround; a clean reference mirror is known to be on the wrong pinned revision and the mismatch is merely documented.

- **Correct Example**: repair/wire the authoritative preamble annotation or semantic method, consume it normally downstream, and keep only genuinely deferred research work in the TODO.  If the source cannot be modified because it is external/unowned, use the narrow documented boundary appropriate to that external dependency.



#### `DEV-31`: Missing Packaging Is Not a Mathematical Gap

- **Rule**: Before declaring that Sage/another library lacks a mathematical concept because no exact class/function/name matches the preamble's desired noun, attempt to build the notion compositionally from standard categories, properties, Homs, structured-object constructions, functors, or universal constructions already available.  Only a genuinely missing primitive/theorem/reusable construction is an upstream mathematical gap.

- **Rationale**: Standard mathematics is often expressed compositionally rather than by one canonical software constant.  Exact-name search encourages unnecessary new wrapper types and duplicated categories merely because another library packages the same mathematics differently.

- **Violation Example**: declare “enumerated finite sets” or “symmetric bilinear objects” absent because no upstream class has exactly that phrase while existing finite-set/property/structured-form machinery already composes to the notion.

- **Correct Example**: write the mathematical construction from existing primitives first; if that construction itself cannot be expressed because a primitive/theorem is missing, record the actual missing primitive rather than the absent spelling.

#### `DEV-32`: Completion Metrics Do Not Change Their Denominator to Make the Residue Vanish

- **Rule**: For audits, migrations, replacement/parity sweeps, and architectural inventories, freeze the original population/success condition before classifying the residue.  An unresolved item leaves the denominator only when evidence establishes that it never belonged to the original semantic domain, not merely because it can be relabeled “helper”, “plumbing”, “example”, “alias”, “implementation detail”, or “deferred research.”

- **Rationale**: LLMs under completion pressure can make a metric reach zero by reclassifying difficult cases rather than resolving them.  The resulting count can be internally correct under the new taxonomy while being false relative to the user's original question.

- **Violation Example**: report “zero unanchored mathematical concepts” after moving every difficult unmatched declaration into an “implementation-only” bucket without proving those declarations are semantically irrelevant.

- **Correct Example**: report the raw residue, separately argue any proposed reclassification against the original scope, and update the denominator only after that semantic judgment is established.



#### `DEV-33`: Understand and Probe the Host System Before Writing Code Around It

- **Rule**: Before implementing a low-level operation that plausibly belongs to Sage, Python stdlib, or another installed mathematical system, inspect the host documentation/source/API and run a small distinguishing probe when semantics/conventions are uncertain.  Do this before inventing wrappers, compatibility shims, local algorithms, or claims that the host cannot support the desired mathematics.

- **Rationale**: Many slop patterns are knowledge gaps disguised as implementation: explicit rational constructors in preparsed Sage, positional generator APIs instead of named-generator syntax, identity matrices instead of Hom identities, custom conformance sweeps instead of `TestSuite`, row loops instead of matrix constructors.  A quick host probe can delete whole designs before they are written.

- **Violation Example**: claim a Sage category/matrix operation behaves a certain way from its name/docstring alone; hand-roll a transformation because the native method was never searched; speculate that a dependency cannot handle Sage objects without installing/probing it.

- **Correct Example**: inspect the exact Sage implementation and test a specimen that distinguishes the competing interpretations, then use or quarantine the verified native capability through the owned semantic API.

#### `DEV-34`: Automated Findings Are Inputs to Structural Diagnosis, Not Syntax-Golf Targets

- **Rule**: When a linter/scanner/static analysis flags a recurring code shape, first disposition it against source semantics and repository policy.  If it is a real violation, fix the underlying state/ownership/mathematical model.  Do not make code denser, indirect, suppressed, or syntactically different merely so the detector stops matching, and do not treat a clean rerun alone as proof of remediation.

- **Rationale**: Detector-first remediation optimizes a proxy.  The offending shape usually exists because the architecture made it natural; syntax substitution can silence the signal while preserving the defect and making source harder to inspect.

- **Violation Example**: replace an accumulator loop with obscure mutation solely to evade a pattern check; add `# noqa`/`type: ignore`; inspect detector internals and rewrite around its exact AST pattern before deciding whether the code violates policy.

- **Correct Example**: decide whether the finding represents eager enumeration, hidden structure, wrong ownership, a typing-boundary gap, etc.; apply the corresponding `STY`/architectural correction, then rerun the detector as confirmation rather than as the definition of correctness.



#### `DEV-35`: Enforce Architecture in the Mathematical Language; Keep Compliance Machinery Thin

- **Rule**: Prefer stronger owned types/categories, constructors, signatures, visibility, and semantic APIs that make an invalid state/shortcut difficult or impossible to express.  Audits, reflection gates, manifests, source-pattern scans, and compliance reports are secondary backstops.  When a compliance mechanism repeatedly catches the same generator, move the invariant into the language rather than expanding the auditor.

- **Rationale**: Downstream enforcement machinery grows into a second project: it gains schemas, tests of tests, suppression rules, and gameable metrics.  Structural domain modeling makes the desired behavior the ordinary construction path and turns violations into obvious boundary escapes instead of compliance puzzles.

- **Violation Example**: add a generated certificate to each category stating which methods it supposedly supports; write runtime tests that inspect source layout/method placement instead of constructing mathematical specimens; add another reflection gate for coordinate leakage while keeping public coordinate escape hatches.

- **Correct Example**: close the coordinate constructor, put the operation on its mathematical owner, require the defining morphism/structure in the constructor, and keep one lightweight static inventory/report as a review aid.  Architecture is checked by source inspection and mathematical behavior, not by making the runtime suite prove the repository organization to itself.

#### `DEV-36`: Judge Preamble Health Against Upstream Sage, Never Against Zero

- **Rule**: The goal is source a mathematician can read against a definition.  Every numerical measure is a weak proxy for that goal, so a measure is admissible only as a differential signal naming a site to go and read, and only beside a calibrated comparator.  The comparator is upstream Sage under the same instrument (`python3 -m dzack_research.utilities.complexity_analysis <tree>`), never zero and never the previous run alone.  Report a measure with its comparator or do not report it.  Before treating any measure as a defect signal, establish that the healthy comparator does not exhibit it.

- **Rationale**: A mathematical universe is intrinsically interconnected, so measures borrowed from ordinary software carry assumptions that do not hold here.  Acyclicity is the type case: `sage/categories` runs 154 of its 229 modules in one strongly-connected component and `sage/rings` 116 of 239, and both have been in service for over a decade.  Mutual reference between the set and ring layers is not evidence of a defect.  An uncalibrated measure invites optimizing a number that the field's own reference implementation would fail, which is `DEV-32` and `DEV-34` arriving through the assessment surface instead of the detector surface.

- **Observed comparator** (`sage-dev-allopts` checkout, 2026-09-04):

  | measure | `sage/categories` | `sage/rings` | what it is evidence for |
  | --- | ---: | ---: | --- |
  | largest strongly-connected component | 154 / 229 | 116 / 239 | **nothing** — cycles are normal here |
  | imports through package aggregators | 3 | 63 | real: aggregator routing is avoidable and Sage largely avoids it |
  | function complexity p90 / p95 / p99 / max | 4 / 7 / 14 / 49 | 7 / 10 / 23 / 70 | real: docstring-immune, counts branches a reader holds |
  | non-code share of physical lines | 79% | 74% | real: worked mathematical examples per operation |

  Function-length percentiles are **not** comparable across these trees.  Sage carries its doctests inside function bodies, so its lengths measure documentation, not logic.  Use complexity instead.

- **Violation Example**: reporting a strongly-connected-component count as a health result; setting a target such as "reduce probe sites below 217"; treating a falling `tuple(...)` count as evidence that collection ownership improved, without opening a converted site; comparing this quarter's number to last quarter's with no external comparator.

- **Correct Example**: measuring dependency direction against the mathematical dependency order — an import from `categories/rings/` up into `categories/modules/` is a signal, an import from `categories/modules/` down into `categories/rings/` is not — then reading the flagged file to decide whether the edge is a filing error or correct mathematics.  Quoting a complexity percentile beside Sage's.  Naming what a count made you go and read, and what you found there.



* * *

### 13. Notebook, REPL & Mathematical Example Style (`NB-*`)

#### `NB-01`: Every Mathematical Claim in an Executable Example Is Executable

- **Rule**: In research notebooks, demos, doctests, and executable documentation, state checkable mathematical claims as assertions or computations that display the witness.  Do not leave “should be”, “correctly”, expected orders, equalities, or classifications only in comments/prose beside unverified code.

- **Rationale**: A notebook is part of the research instrument.  A prose claim beside code can remain true-looking after the implementation changes underneath it; an executable proposition fails at the point of drift.

- **Violation Example**: `# this reflection sends v to -v`; `print("correctly distinguished the genera")`; a markdown sentence claiming an automorphism has order five without checking it.

- **Correct Example**: `assert sigma(v) == -v`; compute and display the actual genus/isometry witness; assert the element order or cited invariant through the semantic API.

#### `NB-02`: Examples Use Specimens That Can Falsify the Claimed Feature

- **Rule**: Choose examples for which the feature under demonstration has nontrivial work to do.  Avoid identities, an object compared with itself, zero maps, or degenerate fixtures when those make the claimed property tautological.

- **Rationale**: A demonstration is useful in proportion to how surprising its passage would be if the implementation were broken.  Equality implies isomorphism/isometry, identity maps satisfy many laws automatically, and zero maps make many factorization tests vacuous.

- **Violation Example**: Demonstrate `is_isometric` using `L.is_isometric(L)`; demonstrate morphism behavior only with the identity; “test” uniqueness of a factorization by constructing the same route twice.

- **Correct Example**: Use two distinct presentations known to be isometric, a nontrivial reflection/projection, or two independently constructed candidate factorizations.  Prefer small specimens whose mathematical answer is independently sourced and transparent.

#### `NB-03`: A Notebook Section Answers a Mathematical Question, Not “Shows an API”

- **Rule**: Organize research examples around mathematical questions and conclusions.  Methods are means, not the subject of the section.  End with the mathematical object, invariant, classification, enumeration, witness, or conclusion the researcher wanted.

- **Rationale**: The preamble is an interactive mathematical language.  API-tour examples encourage users to think in method inventories and implementation boundaries rather than in the mathematical workflow the API exists to support.

- **Violation Example**: A section titled “Using `roots()`” that prints one returned object; “Testing the genus API” that merely shows a method exists.

- **Correct Example**: “What is the root system of this lattice?”, “Are these two lattices in the same genus?”, or “Enumerate the overlattices and their discriminant forms”, with the section computing the complete requested mathematical answer.

#### `NB-04`: Session Examples Use Sage/Preamble Host-Language Idioms

- **Rule**: In notebook/REPL-facing examples, use the concise Sage/preamble language already available instead of manually spelling its lower-level constructors.  This rule is scoped to preparsed/session code; ordinary `.py` implementation modules must not assume Sage preparser semantics.

- **Rationale**: The session language is part of the product.  Reimplementing it in examples teaches users to bypass the concise mathematical syntax and makes the documented workflow look lower-level than actual research use.

- **Violation Example**: In a Sage notebook, spell a rational as `QQ(1)/2`; construct an identity morphism from an identity matrix when the object exposes its identity; access named generators only through positional engine APIs.

- **Correct Example**: Use preparsed exact literals where active, named-generator syntax where supported, semantic identity maps, direct-sum notation, and the public preamble methods discoverable from the objects in hand.

#### `NB-05`: Show Mathematical Witnesses, Not Self-Affirming Status Text

- **Rule**: Output in examples displays mathematical data/witnesses or concise conclusions derived from them.  Do not print prose declaring that the preceding computation was correct, successful, or properly distinguished.

- **Rationale**: Self-affirming output contains no independently inspectable evidence and survives even if the computation above changes.  Showing the actual isomorphism, kernel, factorization, class, invariant, or boolean mathematical predicate lets the reader inspect what happened.

- **Violation Example**: `print("correctly found the primitive embedding")`.

- **Correct Example**: display the embedding and its cokernel/torsion-freeness, or assert the relevant predicate and print the resulting mathematical object when useful.



* * *

## Detailed Documentation References

For in-depth guides and stylistic standards, see the documentation book:

- **Contribution Workflow**: [`docs/contributing/Contribution-Guidelines.md`](docs/contributing/Contribution-Guidelines.md)

- **Categorical Principles**: [`docs/contributing/Categorical-Presentation-Principles.md`](docs/contributing/Categorical-Presentation-Principles.md)

- **Mathematical Style Guide**: [`docs/contributing/Mathematical-Language-Style-Guide.md`](docs/contributing/Mathematical-Language-Style-Guide.md)

- **Design Hazards Ledger**: [`docs/contributing/Design-Hazard-Ledger.md`](docs/contributing/Design-Hazard-Ledger.md)

- **Mathematical Lexicon**: [`docs/contributing/Mathematical-Lexicon.md`](docs/contributing/Mathematical-Lexicon.md)
