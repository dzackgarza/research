# Implementation notes

## 1. Trusted boundary

The only trusted mathematical checker is Lean's kernel.
The custom elaborator may fail, choose an inconvenient path, or emit a poor diagnostic, but any generated declaration is checked by Lean.

The graph is not an alternative logic.
Its entries are names of actual Lean functor declarations carrying a persistent tag attribute.

## 2. Why object homes are encoded in declaration types

A common but fragile implementation stores a map

```text
object name ↦ home category
```

in a second environment extension.
This project instead emits:

```lean
def X : Object C := ...
```

and inspects the declaration type.
This has three advantages:

* imports cannot lose or desynchronize object metadata;

* renaming and namespace handling remain Lean's responsibility;

* the kernel-checked type is the source of truth.

The `Object` head symbol is preserved by defining it transparently but not as an `abbrev`.

## 3. Preferred family resolution

For every preferred declaration `F`, the resolver reads its type:

```text
Π p₁ ... pₙ, Functor (source p₁ ... pₙ) (target p₁ ... pₙ).
```

It creates metavariables `?p₁,...,?pₙ` and asks Lean whether

```text
source ?p₁ ... ?pₙ
```

is definitionally equal to the current graph vertex.
Successful unification yields a concrete functor expression:

```text
F p₁ ... pₙ.
```

This is how parameterized categories are handled without inventing a second unifier for category-expression patterns.

## 4. Search

The search is breadth-first and bounded by a configurable depth (default 16).  Vertices are Lean expressions.
Equality of vertices is Lean definitional equality, checked in a saved metavariable state.

The current policy picks the first shortest path in attribute iteration order.
Since membership is existential, this is semantically sound.
When operations compare two views, a later implementation must request a natural-isomorphism witness between the paths; mere reachability is not sufficient for that use.

## 5. Distinct resolvers

The current project implements view resolution only.
A production system must keep two algorithms separate:

* **view resolution:** graph reachability; produces a composite functor and an object/morphism term;

* **capability resolution:** proof search among Lean theorems; produces evidence for propositions such as preservation or creation of limits.

This separation prevents an underlying-data functor from automatically and incorrectly transporting universal constructions.

## 6. Higher-facing semantics

`Maps C X Y` is an object of `Cat`, implemented in this slice as the discrete category on the hom type.
The source-facing contract is therefore already mapping-object-valued.
The implementation can later replace `Discrete` by genuine spaces without changing the commands `let`, `prefer`, `#via`, or the view graph.

`Fun C D` is the category whose objects are functors and whose morphisms are natural transformations.

## 7. Correct finite/countable interface

A function `X → Nat` alone does not witness countability.
The concrete interface includes a partial inverse.
The equation

```text
nth (number x) = some x
```

implies injectivity of `number` and gives the computational “nth element” behavior requested by the example.

## 8. Generalizing the lattice layer

`LatticeObj R` carries a *perfect* symmetric form (`form : M ≃ₗ M^∨`, `symmetric`), so it is the **unimodular** lattice category; morphisms are isometries.
For general lattices, weaken `form` to

```lean
  form : M →ₗ[R] Module.Dual R M
  nondegenerate : Function.Injective form
```

and recover unimodularity as the specialisation where `form` is an equivalence.
`Lattice.toFreeFinModule` and every downstream preferred path are unaffected: they forget the form.
