# g6k Method Test Gap Checklist

Tracks g6k-relevant methods documented in `docs/g6k/lattice/research_readme.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Script and CLI Surface

- [ ] `python full_sieve.py [--threads T] [--verbose V] [--seed S] d`
- [ ] `python hkz.py [--threads T] [--verbose V] [--seed S] d`
- [ ] `python hkz_maybe.py [--threads T] [--verbose V] [--seed S] d`
- [ ] `python bkz.py [options]`
- [ ] `python svp_challenge.py [options]`
- [ ] `python svp_exact.py [options]`
- [ ] `python svp_exact_find_norm.py [options]`
- [ ] `python lwe_challenge.py [options]`
- [ ] `--threads`
- [ ] `--verbose`
- [ ] `--seed`
- [ ] `--PARAM VAL` (script parameter override form)

## 2. `g6k.siever.Siever` Python API

- [ ] `Siever(A, params=None, seed=None)`
- [ ] `initialize_local(ll, l, r)`
- [ ] `__call__(alg=None, tracer=None, **kwds)` (runtime use: `g6k(alg="gauss")`)
- [ ] `itervalues()`
- [ ] `__contains__(x)`
- [ ] `insert(kappa, x)`
- [ ] `best_lifts()`
- [ ] `db_size(compressed=False)`
- [ ] `shrink_db(size)`
- [ ] `lll(start, stop)`
- [ ] `extend_left(lp)`
- [ ] `shrink_left(lp)`
- [ ] `extend_right(rp)`
- [ ] `shrink_right(rp)`
- [ ] `resize_db(new_size)`
- [ ] `global_histo_update(value)`

## 3. Parameter-Model Surface

- [ ] `SieverParams(...)`
- [ ] `load_siever_params(...)`

---

## Domain Caveats

- `g6k` is a Euclidean lattice reduction/sieving stack (SVP/BKZ-family workflows), not an indefinite arithmetic-form genus/isometry classifier.
- Script-level parameters are documented in runtime-flag form (`--PARAM VAL`) and are passed to siever parameter handling.

---

## References

- `docs/g6k/lattice/research_readme.md`
- `docs/g6k/upstream/g6k_online_provenance_2026-02-17.md`
- g6k repository: `https://github.com/fplll/g6k`
- g6k siever API source: `https://raw.githubusercontent.com/fplll/g6k/master/g6k/siever.pyx`
