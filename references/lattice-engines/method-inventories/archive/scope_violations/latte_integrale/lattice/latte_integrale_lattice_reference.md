# LattE Integrale Lattice Method Reference
## Lattice-point counting, integration, and polyhedral optimization

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[CLI]` | Command-line interface |
| `[POLY]` | Polyhedral/cone workflow |
| `[ENUM]` | Lattice-point counting/enumeration |
| `[INT]` | Integration/volume workflows |
| `[OPT]` | Optimization workflows |

---

## 1. Scope

LattE Integrale is an open package for computations over lattice points of rational cones and convex polytopes, including counting, generating functions, integration, and linear optimization.

Primary surface:

- `count` for lattice-point counting and Ehrhart computations,
- `integrate` for integrating polynomial forms / volume valuation,
- `latte-minimize` and `latte-maximize` for optimization over polyhedral regions.

Not in scope:

- indefinite quadratic-form genus/discriminant/isometry classification.

---

## 2. Core CLI Programs

| Program | Synopsis | Description | Tags |
|---------|----------|-------------|------|
| `count` | `count [options] filename` | Compute lattice-point counts (fixed RHS) and related generating-function/Ehrhart outputs. | `[CLI, POLY, ENUM]` |
| `integrate` | `integrate [options] filename` | Integrate polynomial forms over rational convex polytopes, with valuation choice. | `[CLI, POLY, INT]` |
| `latte-minimize` | `latte-minimize [options] fileName` | Minimize linear objective over polyhedral input. | `[CLI, POLY, OPT]` |
| `latte-maximize` | `latte-maximize [options] fileName` | Maximize linear objective over polyhedral input. | `[CLI, POLY, OPT]` |
| `latte-draw` | `latte-draw [options]` | Drawing/visualization helper utility listed by project docs. | `[CLI, POLY]` |

---

## 3. Option Surfaces from User Guide

### 3.1 `count`

| Option | Description | Tags |
|--------|-------------|------|
| `--ehrhart-polynomial` | Compute Ehrhart polynomial mode for parametric dilation counting. | `[CLI, POLY, ENUM]` |
| `--multivariate-generating-function` | Request multivariate generating-function output. | `[CLI, POLY, ENUM]` |
| `--interior` | Compute interior-point counting variant. | `[CLI, POLY, ENUM]` |
| `--cdd` / `--gmp` | Backend arithmetic/solver options shown in command synopsis. | `[CLI, POLY, ENUM]` |

### 3.2 `integrate`

| Option | Description | Tags |
|--------|-------------|------|
| `--valuation=integrate` | Integration valuation mode. | `[CLI, POLY, INT]` |
| `--valuation=volume` | Volume valuation mode. | `[CLI, POLY, INT]` |
| `--cone-decompose` | Use cone-decomposition strategy. | `[CLI, POLY, INT]` |
| `--triangulate` | Use triangulation strategy. | `[CLI, POLY, INT]` |
| `--composite-simplicial-cone` | Composite simplicial cone mode in integration workflow. | `[CLI, POLY, INT]` |

### 3.3 `latte-minimize` / `latte-maximize`

| Option | Description | Tags |
|--------|-------------|------|
| `--cdd` / `--gmp` | Backend options listed in optimization command synopsis. | `[CLI, POLY, OPT]` |
| `--vrep` / `--hrep` | Input-representation mode selection for optimization programs. | `[CLI, POLY, OPT]` |

---

## 4. Domain Caveat

LattE Integrale methods here are polyhedral and lattice-point counting/optimization APIs. They do not define indefinite-form arithmetic classification contracts.

---

## 5. Sources

- LattE Integrale project site: `https://www.math.ucdavis.edu/~latte/`
- LattE downloads/user guide links: `https://www.math.ucdavis.edu/~latte/software/packages/latte_current/`
- LattE user guide PDF: `https://www.math.ucdavis.edu/~latte/software/download/latte-current/latte-intro.pdf`
- local provenance snapshot: `docs/archive/scope_violations/latte_integrale/upstream/latte_integrale_online_provenance_2026-02-17.md`
