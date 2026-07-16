# Lattice Spike Style Guide

Concrete, checkable rules for writing code, notebooks, and documentation against the `sage_lattice_category_spike` package.
These rules govern both the spike's own implementation and any artifact that uses it.

Load this guide before writing or editing any spike code, notebook cell, README example, or test against the lattice spike.

## 1. Use the host language, do not reinvent it

Sage is the host system.
The spike extends it; it does not replace the language layer.
Every idiom Sage already provides must be used, not reimplemented.

| Wrong | Right | Why |
| --- | --- | --- |
| `QQ(1)/2` | `1/2` | The preparser converts `1/2` to `QQ(1)/2` automatically |
| `L.gen(0); L.gen(1)` | `L.<e,f> = Lattice(...)` | Sage provides generator-naming syntax like polynomial rings |
| `U.direct_sum(U).direct_sum(U)` | `sum([U, U, U])` or `U + U + U` | Direct sum is associative |
| `Hom(L,L).from_matrix(identity_matrix(ZZ, n))` | `L.identity_morphism()` | Access the identity semantically |

Before writing any Sage code: learn the preparser, generator syntax, coercion system, and idiomatic construction patterns.
Every instance of reinventing the host language reveals a knowledge gap, not a style choice.

## 2. Symbolic, not numerical, at the API boundary

The spike is a DSL. Its purpose is to lift the user above the implementation.
Raw numerical objects are the implementation, not the interface.

- **Elements print as symbolic**: `2*e - f`, not `(2, -1)`. A lattice element is like `x` in `k[x]`.
- **Generators are named**: `L.<e,f> = Lattice(...)` binds names at construction.
  Access by name (`e`, `f`), not by index (`L.gen(0)`).
- **`*` is the bilinear pairing**: `v * w = b(v, w)`, `v * v = q(v)`. The Elements API exists for this.
  Do not write `v.b(w)` or `v.q()` in user-facing code.
  Those are internal.
- **Sublattice construction requires symbolic elements**: `L.sublattice([e])` or `L.sublattice([L(vector([...]))])` with explicit coercion.
  Raw lists `[[1, 0, ...]]` must be rejected at the boundary.

## 3. Semantic verbs, not arithmetic checks

Express the mathematical concept directly.
Do not make the user reconstruct it from primitives.

| Wrong | Right |
| --- | --- |
| `abs(L.determinant()) == 1` | `L.is_unimodular()` |
| `not L.is_nondegenerate()` | `L.is_degenerate()` |
| `L1.same_genus(L2)` | `L1.genus() == L2.genus()` |
| `L.signature_pair()` | `L.signature()` |
| `A.invariants()` | `A.invariant_factors()` |
| `O.discriminant_action(g)` | `phi = O.discriminant_action(); phi.image(); phi.kernel()` |

If the mathematical concept has a name, the API uses that name.
If the negation has a name, provide both forms — do not force double negation (`not is_X`) when `is_not_X` has a natural name.

## 4. Literature conventions, not Sage conventions

Where Sage and the mathematical literature differ, the spike follows the literature.
The spike is a replacement layer — it fixes conventions, it does not perpetuate them.

- **Signature**: `L.signature()` returns `(p, q)`. The Witt index is `p - q`, a derived quantity, not the method name.
- **Root lattices**: AG assumes negative-definite (roots have square `-2`). The spike's default convention must match AG, not crystallography.
- **Invariant factors**: `A.invariant_factors()`, not `A.invariants()`.
- **Bilinear pairing**: `v * w`, not `v.b(w)`.

## 5. No convenience wrappers over semantic objects

Do not add methods that wrap a single use of a more semantic, composable operation.
The wrapper hides the mathematical structure.

- `same_genus(L2)` hides that genus is a value object — use `L1.genus() == L2.genus()`.
- `discriminant_action(g)` hides the morphism `O(L) -> O(A_L)` — expose the morphism with `.image()`, `.kernel()`, not a per-element wrapper.
- `from_matrix(I)` hides the identity morphism — use `identity_morphism()`.

Expose the object (value, morphism, identity), not a per-instance method that wraps it.

## 6. Do not identify an object with its image

A morphism `f: A -> B` produces an image `f(A) <= B`. The image is a subobject of `B`; `f` is the relationship.
They are distinct even when `f` is surjective.

- `L.dual()` returns `L#` (different Gram matrix).
- `L.dual_inclusion()` returns the morphism `iota: L -> L#`.
- `iota.image().index_in(L#)` returns `|det L|`.
- When `|det L| = 1` (unimodular), `iota` is surjective, but `L != L#` as objects — they are isometric, not equal.

Never write `L == L.dual()` or `L.dual().index_in(L)`. Use the morphism, its image, and the image's index.

## 7. Reflections return proper homs

`L.reflection(v)` must:

1. Check integrality: is `2*b(x,v)/q(v)` in `R` for all `x`?
2. Return a hom in `Hom(L, L)` when integral (an isometry).
3. Return a hom in `Hom(L_QQ, L_QQ)` when rational, with a warning.
4. Never silently produce a rational isometry from an integral lattice.

## 8. Exact values, not floats

Sage is an exact-arithmetic system.
Geometric quantities must return exact values:

- `hadamard_ratio()` returns an exact real, not a `float`.
- `volume()` returns an exact real (or algebraic number).
- `gaussian_heuristic()` returns an exact real.

A float is an implementation artifact, not a mathematical answer.

## 9. Notebooks: every claim is code

In usage notebooks, demos, and documentation examples:

- **Every claim is a code assertion**, not a comment.
  `assert sigma(v) == -v`, not `# should be -v`.
- **No self-affirming prints**. `print("correctly distinguished")` is noise.
  Print the witness: `print(f"is_isometric = {K3.is_isometric(I)}")`.
- **No comment-assertions**. Comments that assert standard properties (orders, equalities, "should be" statements) are unverified.
  Assert them in code or omit them.

## 10. Notebooks: choose informative cases

Every example must be the case that FAILS if the API is broken, not the one that passes regardless.

- **Isometry**: test between DIFFERENT constructions (Cartan vs gluing), not a lattice vs itself.
  Equality implies isometry; testing equal objects is vacuous.
- **Morphisms**: test a non-trivial morphism (reflection, projection), not the identity.
  The identity satisfies every property trivially.
- **Enumeration**: if the task says "enumerate all X", iterate and show all of them.
  Do not assert one exists and stop.
- **Genus**: test genus comparison between lattices in the same genus built differently, not a lattice vs itself.

The value of a demo assertion is proportional to how surprising its passage would be.

## 11. Notebooks: answer the question

Each notebook section answers a mathematical question, not demonstrates a method.

- "What lattice is this?"
  concludes with an isometry type to a named lattice, not just a list of invariants.
- "Enumerate all overlattices" shows all of them with their discriminant forms.
- "Is this isometric?"
  tests non-trivial cases and shows the witness.

## 12. Notebooks: researcher perspective, not developer perspective

Write from the researcher's perspective: "how do I use this to do mathematics?"
— not the developer's: "what does the API do?"

- Show EXISTENCE of methods on lattices that use them, not ABSENCE on lattices that do not.
- When something expected is absent, explain WHY (the mathematical reason — e.g., "CVP is defined only for positive-definite lattices"), not just that it is absent.
- Axiom gating (which methods are undefined on which lattices) is a development concern.
  Users do not care.
  If an operation is mathematically undefined, say why once, in prose, and move on.

## 13. Lattice string representation

Printing a lattice should surface cheap invariants a researcher needs:

```sage
print(Lattice("A2"))
# Synthetic lattice A2: rank 2, sig (2,0), det 3, even, disc (3,)
```

Not just `Synthetic lattice A2 of rank 2 over Integer Ring`. The repr is the first thing a researcher sees; it should be informative.

## 14. No duplication across surfaces

- GitHub issues own: what is broken, what should happen, why.
- Plan cards own: execution sequence, dependencies, notebook outline, verification gates.
- Memories own: behavioral rules, design principles.
- This style guide owns: concrete, checkable, repo-specific rules.

No fact lives in two places.
When a rule changes, update the authoritative surface; everything else points to it.

## References

- Terminology dictionary: `.agents/references/terminology-dictionary.md`
- Spike specification: `computations/experiments/sage_lattice_category_spike/SYNTHETIC_LATTICE_MODEL.md`
- Governing memories: see agent-memory vault keys listed in `PLAN-demo-notebook-research-instrument`
