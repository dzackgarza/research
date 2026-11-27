See root `AGENTS.md` for general new_spec testing rules.

## Examples

- `R = Rings().NamedRings().ZZ()`
- `M = Modules(R).NamedModules().FreeModule(R, 3)`
- `assert M in Modules(R)`
- `assert Modules(R).Hom(M, M) in Modules(R)`
