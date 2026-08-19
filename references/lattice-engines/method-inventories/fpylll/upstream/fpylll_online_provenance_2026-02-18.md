# fpylll Online Provenance Capture (2026-02-18)

Date captured: 2026-02-18  
Assignment context: documentation coverage audit for in-scope lattice-theory methods.

## Canonical sources used

- fpylll modules index:
  - `https://fpylll.readthedocs.io/en/latest/modules.html`
- fpylll GSO module:
  - `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.fplll.gso`
- fpylll LLL module:
  - `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.fplll.lll`
- fpylll enumeration module:
  - `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.fplll.enumeration`
- fpylll utility module:
  - `https://fpylll.readthedocs.io/en/latest/modules.html#module-fpylll.util`
- fpylll source files (for signatures missing/incomplete in modules page):
  - `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/bkz.pyx`
  - `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/bkz_param.pyx`
  - `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/svpcvp.pyx`
  - `https://raw.githubusercontent.com/fplll/fpylll/master/src/fpylll/fplll/pruner.pyx`

## Signature fidelity notes captured

- `GSO.Mat` / `MatGSO` signature includes `flags=GSO_DEFAULT`; no `precision` parameter in this constructor surface.
- `BKZ` members in `modules.html` are not fully rendered with explicit signatures; BKZ signatures were source-anchored to `bkz.pyx` and `bkz_param.pyx`.
- `Enumeration(...)` constructor signature includes `nr_solutions`, `strategy`, and `sub_solutions`; no `threads` parameter in constructor signature.
- `SVP.shortest_vector(...)` and `CVP.closest_vector(...)` defaults were source-anchored to `svpcvp.pyx`.
- `Pruning.run(...)` was source-anchored to `pruner.pyx` (`run` aliasing the static pruning entry point).

## Scope gate note

This capture supports Euclidean lattice reduction/search APIs only. It does not broaden scope to non-bilinear-form polyhedral or optimization stacks.

## Pass addendum (2026-02-18): BKZ placeholder-signature cleanup

- Updated active documentation surfaces to remove residual BKZ `...` placeholders where source-backed signatures were already available.
- Normalized BKZ coverage rows to:
  - `BKZ.reduction(B, param, U=None, float_type=None, precision=0)` with explicit contract that `param` is a `BKZ.Param` object.
  - full `BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)` signature.
- Goal 1 cursory maintenance check in the same pass found no new in-scope package-surface checklist gaps.
