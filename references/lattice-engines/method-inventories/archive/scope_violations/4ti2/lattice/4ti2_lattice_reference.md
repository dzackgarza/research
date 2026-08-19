# 4ti2 Lattice and Linear-Space Reference
## Command-line method surfaces for integer/rational linear and lattice-ideal workflows

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[LS]` | Linear-system workflow |
| `[CONE]` | Cone/extreme-ray/circuit workflow |
| `[LAT]` | Integer-lattice basis workflow |
| `[IDEAL]` | Lattice/toric ideal workflow |
| `[CLI]` | Command-line surface |

---

## 1. Scope

4ti2 exposes lattice-relevant workflows through project-file-based command-line programs for:

- cone generators/extreme rays/circuits,
- integer and rational linear-system solution sets,
- lattice basis extraction,
- Hilbert/Graver/Markov/Groebner computations for lattice and toric ideals,
- lattice-program optimization via Groebner workflows.

The standard model uses `PROJECT`-prefixed matrix/vector files (`.mat`, `.rel`, `.rhs`, `.sign`, `.lat`, `.cost`, ...).

---

## 2. Cone and Solver Surfaces

| API | Description | Tags |
|-----|-------------|------|
| `circuits [options] PROJECT` | Computes circuits of a cone from matrix/sign/relation inputs. | `[LS, CONE, CLI]` |
| `rays [options] PROJECT` | Computes extreme rays of a cone. | `[LS, CONE, CLI]` |
| `qsolve [options] PROJECT` | Computes generator descriptions for cone/rational linear workflows. | `[LS, CONE, CLI]` |
| `zsolve [options] PROJECT` | Solves linear inequalities/equalities over integers. | `[LS, LAT, CLI]` |
| `zbasis [options] PROJECT` | Computes an integer lattice basis (`PROJECT.lat`). | `[LS, LAT, CLI]` |

Key contract caveat from the 4ti2 manual:

- homogeneous-system restrictions are documented for current `qsolve` workflows.

---

## 3. Lattice-Ideal and Basis Surfaces

| API | Description | Tags |
|-----|-------------|------|
| `hilbert [options] PROJECT` | Computes Hilbert bases for matrix/lattice input. | `[LAT, IDEAL, CLI]` |
| `graver [options] PROJECT` | Computes Graver bases for matrix/lattice input. | `[LAT, IDEAL, CLI]` |
| `groebner [options] PROJECT` | Computes Groebner bases of toric/lattice ideals. | `[LAT, IDEAL, CLI]` |
| `markov [options] PROJECT` | Computes Markov bases (lattice-ideal generating sets). | `[LAT, IDEAL, CLI]` |
| `minimize [options] PROJECT` | Solves integer/lattice programs using Groebner-basis workflows. | `[LAT, IDEAL, CLI]` |
| `normalform [options] PROJECT` | Computes normal forms of feasible-point lists using Groebner data. | `[LAT, IDEAL, CLI]` |
| `walk [options] PROJECT` | Groebner-walk-based lattice/integer programming workflow. | `[LAT, IDEAL, CLI]` |

---

## 4. Supporting Command Surfaces

| API | Description | Tags |
|-----|-------------|------|
| `genmodel [--options] FILENAME` | Builds problem matrices for graphical statistical model encodings. | `[LS, CLI]` |
| `gensymm [--options] A B C D FILENAME` | Generates symmetry-group generators for table-model workflows. | `[LS, CLI]` |
| `output [--options] FILENAME.EXT` | Transforms 4ti2 matrix files into alternate algebraic/combinatorial outputs. | `[LS, CLI]` |
| `ppi [--binary-output] N` | Computes primitive partition identities (Graver basis of `[1,2,...,N]`). | `[LAT, IDEAL, CLI]` |

---

## 5. Input/Output Contract Notes

- The command-line programs consume project-file bundles and emit output by extension (`.ray`, `.cir`, `.zhom`, `.zinhom`, `.gra`, `.gro`, `.mar`, `.lat`, etc.).
- Command behavior depends on the presence of companion files (`.lat`, `.cost`, `.gro`, `.sign`) as documented in each command section of the manual.

---

## 6. Domain Caveat

4ti2 methods here are Euclidean/integer linear and lattice-ideal computational surfaces. They are not high-level arithmetic-form genus/discriminant/isometry classifiers.

---

## 7. Sources

- 4ti2 usage index: `https://4ti2.github.io/toc.html`
- 4ti2 command-line manual (Chapter 3): `https://4ti2.github.io/4ti2_manual.pdf`
- 4ti2 project page (release/news context): `https://4ti2.github.io/h.html`
