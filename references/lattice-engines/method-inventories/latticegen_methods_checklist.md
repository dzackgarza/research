# latticegen Method Test Gap Checklist

Tracks latticegen-relevant method/command surfaces documented in `docs/latticegen/reference/latticegen_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. fplll `latticegen` CLI (IN SCOPE)

### 1.1 Global flags

- [ ] `latticegen --help`
- [ ] `latticegen --version`

### 1.2 Deterministic generation controls

- [ ] `-randseed <integer>`
- [ ] `-randseed time`

### 1.3 Generator methods

- [ ] `latticegen r <d> <b>` — knapsack-like matrix
- [ ] `latticegen s <d> <b> <b2>` — simultaneous Diophantine
- [ ] `latticegen u <d> <b>` — uniform random
- [ ] `latticegen n <d> <b> <c>` — NTRU-like [[I, Rot(h)], [0, q*I]]
  - Caveat: selector `c` in `{'b', 'q'}`
- [ ] `latticegen N <d> <b> <c>` — NTRU-like alternate [[q*I, 0], [Rot(h), I]]
  - Caveat: selector `c` in `{'b', 'q'}`
- [ ] `latticegen q <d> <k> <b> <c>` — q-ary SIS/LWE
  - Caveat: selector `c` in `{'b', 'q', 'p'}`
- [ ] `latticegen t <d> <f>` — triangular geometric decay
- [ ] `latticegen T <d>` — triangular with stdin weights

---

## 2. Python `latticegen` Package (`TAdeJong/moire-lattice-generator`) — OUT OF SCOPE

This package provides moire/image-space lattice generation and does not expose bilinear-form lattice-theoretic APIs. Excluded from project scope per scope definition.

---

## References

- `docs/latticegen/reference/latticegen_lattice_reference.md`
- `docs/latticegen/upstream/latticegen_online_provenance_2026-02-19.md`
- fplll README: `https://raw.githubusercontent.com/fplll/fplll/master/README.md`
- fplll source (`latticegen.cpp`): `https://raw.githubusercontent.com/fplll/fplll/master/fplll/latticegen.cpp`
