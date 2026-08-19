# TOPCOM Method Test Gap Checklist

Tracks TOPCOM lattice-relevant commands documented in `docs/archive/scope_violations/topcom/lattice/topcom_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that command.

---

## 1. Point/Chirotope Conversion and Oriented-Matroid Surfaces

- [ ] `points2chiro [options]`
- [ ] `chiro2dual [options]`
- [ ] `points2circuits [options]`
- [ ] `chiro2circuits [options]`
- [ ] `points2cocircuits [options]`
- [ ] `chiro2cocircuits [options]`

## 2. Seed Triangulation Surfaces

- [ ] `points2triangs [options]`
- [ ] `chiro2triangs [options]`
- [ ] `points2ntriangs [options]`
- [ ] `chiro2ntriangs [options]`
- [ ] `points2finetriang [options]`
- [ ] `chiro2finetriang [options]`
- [ ] `points2nfinetriang [options]`
- [ ] `chiro2nfinetriang [options]`

## 3. Full Triangulation Enumeration and Flip-Graph Surfaces

- [ ] `points2alltriangs [options]`
- [ ] `chiro2alltriangs [options]`
- [ ] `points2allfinetriangs [options]`
- [ ] `chiro2allfinetriangs [options]`
- [ ] `points2nalltriangs [options]`
- [ ] `chiro2nalltriangs [options]`
- [ ] `points2nallfinetriangs [options]`
- [ ] `chiro2nallfinetriangs [options]`
- [ ] `points2flips [options]`
- [ ] `chiro2flips [options]`

## 4. Secondary Polytope / Extremal and Configuration Utilities

- [ ] `points2facets [options]`
- [ ] `points2volume [options]`
- [ ] `points2nvolume [options]`
- [ ] `points2placingtriang [options]`
- [ ] `points2symmetries [options]`
- [ ] `checkregularity [options]`
- [ ] `allfinetriangs2subdivs [options]`
- [ ] `gen_points [options]`
- [ ] `gen_chiro [options]`

## 5. Common Option Surface

- [ ] `--regular`
- [ ] `--nonregular`
- [ ] `--unimodular`
- [ ] `--reducepoints`
- [ ] `--noinsertion`
- [ ] `--heights`
- [ ] `--flipdeficiency`
- [ ] `--checktriang`
- [ ] `-i` / `--input-chiro`
- [ ] `-v` / `--verbose`

---

## Domain Caveats

- TOPCOM is a triangulation/oriented-matroid stack centered on point configurations, symmetry, and secondary-polytope workflows.
- It is not an indefinite arithmetic quadratic-form genus/isometry classification API.

---

## References

- `docs/archive/scope_violations/topcom/lattice/topcom_lattice_reference.md`
- `docs/archive/scope_violations/topcom/upstream/topcom_online_provenance_2026-02-17.md`
- TOPCOM project page: `https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/`
- TOPCOM manual PDF: `https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/TOPCOM-manual.pdf`
- TOPCOM command manual mirror (`topcom(7)`): `https://manpages.debian.org/testing/topcom/topcom.7.en.html`
