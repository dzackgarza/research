# Lake workspace

This spike is **not** an independent Lake project.

The repository root owns:

- `lean-toolchain`

- `lakefile.toml`

- `.lake/` (mathlib + build products)

Build from the repo root:

```bash
lake build NormalizedCategoryGraph CatDSL ncg-export ncg-export-full
lake exe cache get
```

Or use this directory's `justfile` (it `cd`s to the git root).
