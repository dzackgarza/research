See root `AGENTS.md` for general new_spec testing rules.

## Examples

- `R = Rings().Constructors().ZZ()`
- `M = Modules(R).Constructors().FreeModule(R, 3)`
- `assert M in Modules(R)`
- `assert Modules(R).Hom(M, M) in Modules(R)`
