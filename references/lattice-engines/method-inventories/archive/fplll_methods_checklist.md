# fplll Method Test Gap Checklist

Tracks fplll-relevant methods/commands documented in `docs/fplll/lattice/fplll_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. CLI Surface

- [ ] `fplll [-a <algo>] [options] [file]`
- [ ] `bkz [options] [file]`
- [ ] `hkz [options] [file]`
- [ ] `svp [options] [file]`
- [ ] `-a <algo>`
- [ ] `-b <block_size>`
- [ ] `-d <delta>`
- [ ] `-e <eta>`
- [ ] `-p <precision>`
- [ ] `-m <float_type>`
- [ ] `-z <strategy>`

## 2. LLL C++ API

- [ ] `LLLReduction(MatGSOInterface&, delta, eta, flags)`
- [ ] `LLLReduction::lll(kappa_min=0, kappa_start=0, kappa_end=-1, size_reduction_start=0)`
- [ ] `LLLReduction::size_reduction(kappa_min=0, kappa_end=-1, size_reduction_end=-1, y=0)`
- [ ] `LLLReduction::lovasz_tests(kappa, kappa_max)`
- [ ] `LLLReduction::swap(kappa, kappa_max=-1)`

## 3. BKZ C++ API

- [ ] `BKZParam(block_size, ..., delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, ...)`
- [ ] `BKZReduction(MatGSOInterface&, LLLReduction&, BKZParam)`
- [ ] `BKZReduction::bkz()`
- [ ] `BKZReduction::tour(loop, param, min_row, max_row)`
- [ ] `BKZReduction::svp_preprocessing(kappa, block_size, par)`
- [ ] `BKZReduction::svp_reduction(kappa, block_size, par, dual=false)`
- [ ] `BKZReduction::rerandomize_block(min_row, max_row, density)`

## 4. Namespace Helpers

- [ ] `lll_reduction(...)`
- [ ] `bkz_reduction(...)`
- [ ] `is_lll_reduced(...)`

---

## Definiteness and Domain Caveat

- fplll is a Euclidean lattice stack; it does not expose indefinite arithmetic-form classification APIs.

---

## References

- `docs/fplll/lattice/fplll_lattice_reference.md`
- fplll docs home: `https://fplll.github.io/fplll/`
- fplll repository: `https://github.com/fplll/fplll`
