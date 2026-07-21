# CatDSL — proof of concept

A Lean-hosted categorical DSL: paper-like source over Mathlib's category theory, with a preferred-functor graph that decides membership by reachability and inherits implementations along it.

Everything claimed below is checked by `./scripts/check.sh`.

## Verify

Lake lives at the **repository root** (see [`LEAN.md`](../../../../LEAN.md) and [`LAKE.md`](LAKE.md)).

```bash
# from repo root
lake build CatDSL CatDSLTest

# or from the spike
just -f ../justfile build
just -f ../justfile axioms
./scripts/check.sh   # also cds to repo root
```

Requires **elan** (AUR `elan-lean`), not a distro `lean`. Mathlib's cache is keyed to the exact official toolchain build, so any other Lean silently recompiles all ~7900 modules.
elan reads the root `lean-toolchain` and fetches the right one.
If `lake exe cache get` (at repo root) is honoured, no Mathlib module compiles.

## What is verified

`CatDSL/Example/F2Semantic.lean` — the vertical slice, in ordinary Lean:

```text
Lat(𝔽₂) ─π→ FreeFinMod(𝔽₂) ─Uᶠⁱⁿ→ FiniteSet ─ι→ CountableSet

card_L       : cardinality Lfin = 4
card_L_eq_sq : cardinality Lfin = 𝔽₂.size ^ 2
number_table : number (a,b) = 2a + b, all four elements
nth_table    : nth inverts number; nth 4 = none
nth_number_L : ∀ x, nth (number x) = some x
```

`#print axioms` on each: `[propext, Classical.choice, Quot.sound]`. No `sorryAx`.

The point is that `L` reaches `CountableSet` with **no lattice-specific code**. The `2a+b` numbering comes entirely from `FiniteSetObj.prod`'s mixed-radix equivalence; no lattice, module, or ring code computes it.

`CatDSL/Example/RegistryTest.lean` — the resolver, executed.
It discovers the path itself, infers `R := 𝔽₂` for the parameterized functor families, composes them, and the result is *definitionally* the `Lfin` above.

`CatDSL/Example/SurfaceTest.lean` — the syntax, executed:

```text
prefer CatDSL.Std.Lattice.toFreeFinModule
let L := CatDSL.Example.L ∈ CatDSL.Std.Lattices CatDSL.Std.𝔽₂
#home L
#via L ∈ CatDSL.Std.CountableSets
```

and `surface_L_is_semantic_L : L = CatDSL.Example.L := rfl` — the surface `let` produces an ordinary declaration definitionally equal to the object it names.

## Architecture

| layer |  |
| --- | --- |
| `Foundation` | names Mathlib's `Cat`, `⥤`, `Discrete`. No parallel kernel. |
| `Registry` | enumerable `SimplePersistentEnvExtension` of preferred functors; BFS path resolution; `applyPath` |
| `Std/Sets`, `Std/Algebra` | object type + `Category` instance + `Cat.of` bundle; functors between the object **types** |
| `Syntax` | `let`, `prefer`, `#via`, `#home` |

A category module: define the object type, install its `Category` instance, give it a reducible bundled `Cat` name, define ordinary Mathlib functors between object types.
`Std/Sets.lean` is the reference.

## Known divergences from `GUIDING_PRINCIPLES.md`

**The `.` sentence terminator is not implemented, and is not implementable as specified.** `.` is field-projection syntax and Lean's lexer takes it greedily: `Lat(𝔽₂).` parses as a projection, `Lat(𝔽₂) .` as anonymous-constructor dot-notation, and a `.`-terminated syntax cannot be pattern-matched in a quotation at all.
It would need a custom token or `checkNoWsBefore` guards at every position a term may end.
Commands end at the newline instead.

**`Lat(R)` is the category of *unimodular* lattices.** `form : M ≃ₗ M^∨` is *perfect*, not merely nondegenerate — nondegeneracy is only injectivity of `b̃ : M → M^∨`. The two agree for finite-dimensional `M` over a field, so `𝔽₂` is unaffected, but `coker(b̃ : L ↪ L^∨) = L^∨/L` is the discriminant group.
A general lattice layer needs `form` weakened to a `LinearMap` with a separate nondegeneracy field.

**`|X|`, `number(X,x)`, `nth[n](X)` are not implemented.** They need *operation-implementation* resolution, which is a different search from the membership resolution `resolvePath` performs: `Lat(𝔽₂) ⇝ Sets` has two 3-step routes and only one passes through the finite presentation that cardinality is read from.
Selection is currently by attribute iteration order.
Implementing these as macros over `resolvePath` would paper over that.

## Not yet done

* operation-implementation resolution (above) — the main open design task

* `Hom_𝒞(A,B)` / mapping objects beyond `Maps` being defined

* `FreeFinModuleObj` stores `finiteSet`, `finiteSetEquiv`, and `cardinality_eq` alongside the basis; these should be *derived* from `R`'s finite presentation and the chosen coordinates

* a homotopy-aware backend for `Maps` (the interface is already mapping-object-valued, so the graph should not change)
