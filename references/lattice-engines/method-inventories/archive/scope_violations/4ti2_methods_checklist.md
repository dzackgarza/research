# 4ti2 Method Test Gap Checklist

Tracks 4ti2-relevant methods/commands documented in `docs/archive/scope_violations/4ti2/lattice/4ti2_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Cone and Linear-System Solvers

- [ ] `circuits [options] PROJECT`
- [ ] `rays [options] PROJECT`
- [ ] `qsolve [options] PROJECT`
  - Caveat: the 4ti2 manual documents homogeneous-system restrictions in current `qsolve` workflows.
- [ ] `zsolve [options] PROJECT`
- [ ] `zbasis [options] PROJECT`

## 2. Lattice-Ideal and Basis Computations

- [ ] `hilbert [options] PROJECT`
- [ ] `graver [options] PROJECT`
- [ ] `groebner [options] PROJECT`
- [ ] `markov [options] PROJECT`
- [ ] `minimize [options] PROJECT`
- [ ] `normalform [options] PROJECT`
- [ ] `walk [options] PROJECT`

## 3. Supporting Command Surfaces

- [ ] `genmodel [--options] FILENAME`
- [ ] `gensymm [--options] A B C D FILENAME`
- [ ] `output [--options] FILENAME.EXT`
- [ ] `ppi [--binary-output] N`

---

## Domain Caveat

- 4ti2 surfaces listed here are integer/rational linear-system and lattice-ideal computation workflows, not high-level indefinite genus/isometry classification APIs.

---

## References

- `docs/archive/scope_violations/4ti2/lattice/4ti2_lattice_reference.md`
- 4ti2 command index: `https://4ti2.github.io/toc.html`
- 4ti2 manual (command-line reference): `https://4ti2.github.io/4ti2_manual.pdf`
- 4ti2 project page: `https://4ti2.github.io/h.html`
