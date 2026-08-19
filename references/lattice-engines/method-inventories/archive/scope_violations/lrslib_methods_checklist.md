# lrslib Method Test Gap Checklist

Tracks lrslib-relevant methods/commands documented in `docs/archive/scope_violations/lrslib/lattice/lrslib_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Core Driver Commands

- [ ] `lrs [input-file]`
- [ ] `mplrs [options] input output`
- [ ] `redund [input-file]`
- [ ] `minrep [input-file]`
- [ ] `lrsnash [input-file]`
- [ ] `nash [input-file]`
- [ ] `2nash [input-file]`
- [ ] `fel [input-file] [output-file]`
- [ ] `xref [input-file [output-file]]`
- [ ] `hvref [input-file [output-file]]`
- [ ] `polyv [flags] [input-file [output-file]]`

## 2. `lrs` Option/Keyword Surface

- [ ] `arithmetic in|mp|lr|gmp|flint|hybrid`
- [ ] `maximize` / `minimize`
- [ ] `nonnegative`
- [ ] `redund <list>`
- [ ] `minrep`
- [ ] `project <list>`
- [ ] `eliminate <list>`
- [ ] `extract <list>`
- [ ] `truncate <list>`
- [ ] `bound x`
- [ ] `volume`
- [ ] `voronoi`
- [ ] `allbases`
- [ ] `printcobasis`
- [ ] `printslack`
- [ ] `maxoutput n`
- [ ] `maxcobases n`
- [ ] `prune`
- [ ] `restart n`
- [ ] `restartp n`
- [ ] `seed n`
- [ ] `verbose`
- [ ] `time_estimate m`

## 3. `mplrs` Option Surface

- [ ] `-processes n`
- [ ] `-scale n`
- [ ] `-maxtreesize n`
- [ ] `-maxdepth n`
- [ ] `-mindepth n`
- [ ] `-checkfrequency n`
- [ ] `-stop n`
- [ ] `-estimatelimit n`
- [ ] `-cache n`

## 4. Script Surface (`lrsscripts`)

- [ ] `projred`
- [ ] `mfel`
- [ ] `mlrs`
- [ ] `tlrs`
- [ ] `plotV`
- [ ] `plotR`
- [ ] `plotL`

---

## Domain Caveats

- lrslib is a reverse-search polyhedral/lattice-point stack (H/V conversion, redundancy removal, vertex/ray enumeration, and Nash-equilibrium drivers).
- It is not an indefinite arithmetic quadratic-form genus/isometry classification stack.

---

## References

- `docs/archive/scope_violations/lrslib/lattice/lrslib_lattice_reference.md`
- `docs/archive/scope_violations/lrslib/upstream/lrslib_online_provenance_2026-02-17.md`
- lrslib package page: `https://cgm.cs.mcgill.ca/~avis/C/lrslib/USERGUIDE.html`
- lrs man page mirror: `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/lrs.1`
