# Indefinite Isometry Backend Research

This note records the external indefinite-isometry routes that actually exist
upstream, the exact entry points inspected, the commands run locally, and the
current working result.

## Verified upstream routes

### Julia wrapper: `Indefinite.jl`

Repository:
`https://github.com/MathieuDutSik/Indefinite.jl`

Verified entry points:
- `src/Functions.jl`
  - `INDEF_FORM_TestEquivalence(Qmat1::Nemo.QQMatrix, Qmat2::Nemo.QQMatrix)`
  - `INDEF_FORM_AutomorphismGroup(Qmat::Nemo.QQMatrix)`
- `src/Indefinite.jl`
  - loads `Oscar`, `GAP`, `Hecke`, `Nemo`
  - in `__init__()` loads GAP package `grape`, reads `indef/init.g`, then calls
    `full_install_indefinite(...)`
- `test_gap.jl`
  - exercises `Indefinite.INDEF_FORM_TestEquivalence(...)` on shipped fixtures

What this proves:
- there is a real Julia-level API for indefinite form equivalence
- the intended high-level call is `Indefinite.INDEF_FORM_TestEquivalence`

### GAP library under `Indefinite.jl/indef`

Verified entry points:
- `indef/init.g`
  - loads `InputOutput.g`, `LatticeIsomorphy.g`, `IndefiniteFormsFundamental.g`,
    `IndefiniteForms.g`, and the rest of the GAP payload
- `indef/lib/IndefiniteForms.g`
  - defines `INDEF_FORM_TestEquivalence`
- `indef/lib/IndefiniteFormsFundamental.g`
  - defines `IndefiniteReduction`
- `indef/lib/InputOutput.g`
  - defines `MatrixToOscar`, `ReadOscarMatrix`, `ListMatrixToOscar`,
    `JuliaEvalString`, `JuliaToGAP`-dependent helpers

What this proves:
- there is a real GAP implementation of `INDEF_FORM_TestEquivalence`
- it is not standalone GAP in the current upstream layout, because core helpers
  route through Julia/Oscar bridge symbols

### C++ CLI backend: `polyhedral_common/src_indefinite`

Repository:
`https://github.com/MathieuDutSik/polyhedral_common/tree/master/src_indefinite`

Verified entry points:
- `src_indefinite/INDEF_FORM_TestEquivalence.cpp`
- `src_indefinite/INDEF_FORM_AutomorphismGroup.cpp`
- `src_indefinite/CombinedAlgorithms.h`

What this proves:
- there is a real compiled CLI/backend route for indefinite form equivalence
- the executable `INDEF_FORM_TestEquivalence` is a first-class upstream target,
  not an inferred possibility

## Local experiments

### Julia 1.12 route failed at dependency resolution

Command run:

```bash
cd /tmp/indefinite-research-ZtnrdW/Indefinite.jl
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

Observed result:
- dependency resolution failed around the pinned `Oscar` / `Nemo` /
  `libpolymake_julia_jll` stack

Why:
- `Project.toml` in `Indefinite.jl` pins `julia = "1.6"`

### Julia 1.6 route bootstrapped with `juliaup`

Commands run:

```bash
juliaup add 1.6.7
cd /tmp/indefinite-research-ZtnrdW/Indefinite.jl
julia +1.6.7 --project=. -e 'using Pkg; Pkg.instantiate()'
```

Observed result:
- package instantiation succeeded
- the pinned stack installed, including `GAP v0.9.8`, `Nemo v0.33.8`,
  `Oscar v0.12.0`, `Hecke v0.18.10`, and `polyhedral_jll v0.2.0`

### First Julia 1.6 load failed because GAP picked up the user package tree

Command run:

```bash
cd /tmp/indefinite-research-ZtnrdW/Indefinite.jl
julia +1.6.7 --project=. -e 'using Indefinite'
```

Observed result:
- load failed with
  `Error, Variable: '_JuliaGetMainModule' must have a value`
- the failure came from
  `/home/dzack/.gap/pkg/JuliaInterface/gap/JuliaInterface.gi`

What this means:
- the pinned Julia stack is incompatible with the user-installed
  `~/.gap/pkg/JuliaInterface`
- this was an environment collision, not evidence that `Indefinite.jl` itself is
  unusable

### Isolating `HOME` made the Julia route work

Working command:

```bash
cd /tmp/indefinite-research-ZtnrdW/Indefinite.jl
julia +1.6.7 --project=. -e '
ENV["HOME"] = "/tmp/indefinite-julia-home";
using Indefinite, Nemo;
G1 = Nemo.matrix(Nemo.QQ, [0 1 0 0; 1 0 0 0; 0 0 -1 0; 0 0 0 -1]);
G2 = Nemo.matrix(Nemo.QQ, [2 1 0 0; 1 0 0 0; 0 0 -1 0; 0 0 0 -1]);
println("example");
println(Indefinite.INDEF_FORM_TestEquivalence(G1, G2));
H1 = Nemo.matrix(Nemo.QQ, [0 3; 3 0]);
H2 = Nemo.matrix(Nemo.QQ, [0 3; 3 6]);
println("threeU_basis_change");
println(Indefinite.INDEF_FORM_TestEquivalence(H1, H2));
'
```

Observed result:

```text
example
[1 1 0 0; 1 0 0 0; 0 0 1 0; 0 0 0 1]
threeU_basis_change
[0 1; 1 1]
```

What this proves:
- the Julia wrapper route is locally executable
- it returns explicit integral equivalence witnesses
- a shell-out backend from Sage/Python to `julia +1.6.7` is viable right now,
  provided the subprocess uses an isolated `HOME`

### Direct GAP-in-Sage is not a drop-in load

Evidence inspected:
- `indef/lib/IndefiniteFormsFundamental.g` calls `Julia.Indefinite.IndefiniteReduction`
- `indef/lib/InputOutput.g` depends on `JuliaEvalString`,
  `Oscar.GAP.julia_to_gap`, and related bridge helpers

What this means:
- loading `indef/init.g` inside Sage's GAP session is not enough by itself
- a pure GAP route would require either:
  - a compatibility bridge that recreates the Julia/Oscar calls, or
  - a local port/refactor of those bridge-dependent pieces

### C++ backend exists but does not currently build here

Commands run:

```bash
git -C /tmp/indefinite-research-ZtnrdW/polyhedral_common submodule update --init --recursive
cd /tmp/indefinite-research-ZtnrdW/polyhedral_common/src_indefinite
make INDEF_FORM_TestEquivalence
```

Observed result:
- after submodule initialization, the build advanced past the earlier missing-header
  problem
- compilation then failed on
  `boost/archive/tmpdir.hpp: No such file or directory`

What this means:
- the C++ route is real
- it is not immediately usable in this environment without additional Boost
  development headers or a containerized build setup

## Current conclusion

The route that both exists upstream and works locally is:
- `Indefinite.jl`
- Julia `1.6.7` via `juliaup`
- subprocess isolation from the user `~/.gap` tree by overriding `HOME`

That is the first backend route worth wiring into `Lattice.is_isometric_to`.
