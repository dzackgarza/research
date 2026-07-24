# Lean workspace (repository root)

This repository is a **single** Lake project.

| Path | Role |
| --- | --- |
| `lean-toolchain` | `leanprover/lean4:v4.32.0` (elan) |
| `lakefile.toml` | mathlib + all libs/exes |
| `.lake/` | packages (mathlib, …) and build products — gitignored |

Source trees stay under `computations/experiments/lean_category_dsl_spike/`; the root lakefile sets `srcDir` for each library.

```bash
lake exe cache get                                          # mathlib oleans
lake build NormalizedCategoryGraph CatDSL ncg-export ncg-export-full
lake build CatDSLTest
just -f computations/experiments/lean_category_dsl_spike/justfile test
```

Do **not** add nested `lakefile` / `lean-toolchain` / `.lake` under experiments — that reintroduces duplicate mathlib clones and URL/cache fights.
