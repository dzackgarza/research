# Lean categorical DSL proof of concept {#sec-written-form}

The experiment in `computations/experiments/lean_category_dsl_spike/catdsl_poc` adds a small surface language to Lean.
Mathlib supplies the categories, functors, natural transformations, and kernel checking.
The experiment supplies object declarations, registration of distinguished functors, and queries along composites of those functors.

## Implemented source forms {#sec-written-forms}

| source form | generated declaration or action |
| --- | --- |
| `let X ∈ C` | declare an axiom `X : CatDSL.Object C` |
| `let X := t ∈ C` | define `X : CatDSL.Object C := t` |
| `prefer F` | register the Lean functor declaration `F` as distinguished |
| `#home X` | report the category recovered from the type of `X` |
| `#via X ∈ D` | report a registered composite from the category of `X` to `D` |

These commands extend Lean's command language.
Each generated object declaration has type `CatDSL.Object C`, and `CatDSL.Object C` reduces to the object type of the bundled Mathlib category `C`.

## Object declarations

The command

```lean
let L := CatDSL.Example.L ∈ CatDSL.Std.Lattices CatDSL.Std.𝔽₂
```

generates an ordinary Lean declaration.
The theorem

```lean
theorem surface_L_is_semantic_L : L = CatDSL.Example.L := rfl
```

checks that the source form names the same object definitionally.
The elaborator recovers its category from the declaration type.

## Distinguished functors and composites

The `prefer` command accepts a declaration only when, after introducing its parameters, its result is a Mathlib functor.
The registry contains names of such functors.
Given `#via X ∈ D`, the elaborator searches for a shortest composite from the category of definition of `X` to `D` and reports the functors in the selected composite.

For the finite-field example, the checked commands include

```lean
prefer CatDSL.Std.Lattice.toFreeFinModule
prefer CatDSL.Std.FreeFinModule.toFiniteSet
prefer CatDSL.Std.FiniteSet.toCountable

#home L
#via L ∈ CatDSL.Std.FreeFinModules CatDSL.Std.𝔽₂
#via L ∈ CatDSL.Std.FiniteSets
#via L ∈ CatDSL.Std.CountableSets
```

The selected composite acts on the object through ordinary applications of `CategoryTheory.Functor.obj`.

## Current boundary

The proof of concept has four explicit limits:

- `Maps C X Y` is the discrete category on the Mathlib hom type.

- `LatticeObj R` currently requires a perfect symmetric form, so its objects are unimodular lattices.
  General nondegenerate lattices are outside this definition.

- Cardinality, enumeration, and other operations have no resolver.
  The forms `|X|`, `number(X,x)`, and `nth[n](X)` are therefore absent.

- Commands end at a newline.
  A trailing period conflicts with Lean's existing syntax.

The experiment's README and executable examples exhibit the implemented commands and these limits.
