# Backend Environment Notes

## Indefinite.jl with GAP

`Indefinite.jl` on Julia 1.6.7 works in this environment only if GAP is isolated from the user `~/.gap/pkg/JuliaInterface` tree. Without isolation, the failure mode is `_JuliaGetMainModule` from `/home/dzack/.gap/pkg/JuliaInterface/gap/JuliaInterface.gi`.

Set `ENV["HOME"]` inside the Julia process before `using Indefinite`. That avoids the GAP collision while still using the normal Julia depot for packages and precompile cache.

## ore_algebra on conda Sage 10.7

On 2026-04-10, `ore_algebra` was tested against `/home/dzack/miniforge3/envs/sage` with conda-forge Sage 10.7, Python 3.12.13, and libflint 3.3.1.

### Findings

- Current `ore_algebra` master resolved by pip to commit `2904d75321ef50f5b02b5e8bc355c7d9d74a484f` and fails to build in `src/ore_algebra/analytic/dac_sum_c.c` because `_fmpq_poly_interpolate_fmpq_vec` is undeclared. Local headers expose only `_fmpq_poly_interpolate_fmpz_vec` in `include/flint/fmpq_poly.h`.
- Upstream issue `#155` from 2026-04-01 matches this exact Flint 3 build failure and proposes the `fmpq -> fmpz` patch in `dac_sum_c.pyx`. A temporary checkout with that patch built and imported successfully here.
- The immediate parent commit before the 2026-03-08 Flint change, `afbe4dad50bd63f5b2ce112193555d6f9740e0d3`, also builds and imports successfully on this machine.
- Tagged release `0.5` is not a clean fallback here. Metadata generation failed before compilation because its older `setup.py` used broad `sage.env.cython_aliases()` and raised `pkgconfig PackageNotFoundError` for `fflas-ffpack`.
- Even when build/import succeeds with either the Flint patch or the pre-regression commit, analytic runtime on conda Sage 10.7 is still broken: `monodromy_matrices()` on the Legendre operator failed with `TypeError: C variable sage.rings.integer._small_primes_table has wrong signature`.
- Upstream issue `#150` reports the same `_small_primes_table` failure mode on conda or prebuilt Sage setups. The reporter later said installing `ore_algebra` with `passagemath` instead of `sagemath` avoided the issue.
- The most useful local workaround was to force `ore_algebra` `setup.py` to disable Cython extensions entirely. A temporary master checkout patched to set `extensions = []` through the existing old-Sage fallback logic built as a pure-Python wheel, imported, and successfully ran `monodromy_matrices()` for the Legendre example on this exact environment. Warnings reported slower Python fallbacks in `local_solutions.py` and `naive_sum.py`, but the analytic API worked.

### Practical Guidance

- For immediate use on this machine, prefer a no-Cython `ore_algebra` install over trying to fix the Cython extensions under conda Sage.
- If analytic performance becomes unacceptable, the next candidates are a separate `passagemath`-based environment or deeper Sage and `ore_algebra` ABI work.
- If only symbolic or non-analytic `ore_algebra` features are needed, patched master or commit `afbe4dad50bd63f5b2ce112193555d6f9740e0d3` are viable here.
