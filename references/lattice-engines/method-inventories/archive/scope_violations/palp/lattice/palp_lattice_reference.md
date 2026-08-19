# PALP Lattice Method Reference
## Lattice-polytope and complete-weight-system command surfaces

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[CLI]` | Command-line interface |
| `[POLY]` | Lattice-polytope workflow |
| `[ENUM]` | Enumeration/classification workflow |
| `[SAGE]` | Sage wrapper surface requiring optional PALP package |

---

## 1. Scope

PALP is a command-line package for lattice-polytope and complete-weight-system workflows used in toric and combinatorial geometry pipelines.

Package metadata describes practical scope mainly for lattice polytopes in dimensions up to four.

This surface does not define arithmetic-lattice genus/discriminant/isometry contracts.

---

## 2. Core CLI Programs

| Program | Synopsis | Description | Tags |
|---------|----------|-------------|------|
| `poly.x` | `poly.x [options] [in-file [out-file]]` | Generic lattice-polytope analyzer over integer input/output formats. | `[CLI, POLY]` |
| `class.x` | `class.x [options] [in-file [out-file]]` | Classification/enumeration-oriented PALP driver. | `[CLI, POLY, ENUM]` |
| `cws.x` | `cws.x [options] [in-file [out-file]]` | Complete-weight-system oriented PALP driver. | `[CLI, POLY, ENUM]` |
| `nef.x` | `nef.x [options] [in-file [out-file]]` | Nef-partition and related lattice-polytope workflow driver. | `[CLI, POLY, ENUM]` |
| `mori.x` | `mori.x [options] [in-file [out-file]]` | Mori-cone and triangulation-oriented PALP workflow tool. | `[CLI, POLY, ENUM]` |

---

## 3. Option Surfaces

### 3.1 `poly.x`

| Option | Contract note | Tags |
|--------|----------------|------|
| `-h` | Show help text. | `[CLI]` |
| `-f` | Use file/filter mode described by man page. | `[CLI, POLY]` |
| `-g` | Request general output mode. | `[CLI, POLY]` |
| `-p` | Treat points as input representation. | `[CLI, POLY]` |
| `-r` | Treat CWS weights as input representation. | `[CLI, POLY]` |
| `-v` | Request vertex-oriented output. | `[CLI, POLY]` |

### 3.2 `class.x`

| Option | Contract note | Tags |
|--------|----------------|------|
| `-h` | Show help text. | `[CLI]` |
| `-f` | Use file/filter mode described by man page. | `[CLI, POLY]` |
| `-m` | Enable mode described as `-m # #` in the man page synopsis. | `[CLI, POLY, ENUM]` |
| `-p` | Point-oriented processing mode. | `[CLI, POLY]` |
| `-v` | Vertex-oriented processing/output mode. | `[CLI, POLY]` |

### 3.3 `cws.x`

| Option | Contract note | Tags |
|--------|----------------|------|
| `-h` | Show help text. | `[CLI]` |
| `-f` | Use file/filter mode described by man page. | `[CLI, POLY]` |
| `-w[#]` | Emit full or indexed weight-system output. | `[CLI, POLY, ENUM]` |

### 3.4 `nef.x`

| Option | Contract note | Tags |
|--------|----------------|------|
| `-h` | Show help text. | `[CLI]` |
| `-f*` | File/filter mode family (asterisk form in synopsis). | `[CLI, POLY]` |
| `-N` | Nef-mode switch documented by man page. | `[CLI, POLY, ENUM]` |
| `-H` | Option switch documented by man page. | `[CLI, POLY, ENUM]` |
| `-Lv` | Option switch documented by man page. | `[CLI, POLY, ENUM]` |
| `-p` | Point-oriented mode switch. | `[CLI, POLY]` |
| `-D` | Option switch documented by man page. | `[CLI, POLY, ENUM]` |
| `-P` | Option switch documented by man page. | `[CLI, POLY, ENUM]` |
| `-t` | Triangulation-related mode switch. | `[CLI, POLY, ENUM]` |
| `-c*` | Additional option family documented with star suffix in synopsis. | `[CLI, POLY, ENUM]` |

### 3.5 `mori.x`

| Option | Contract note | Tags |
|--------|----------------|------|
| `-h` | Show help text. | `[CLI]` |
| `-f` | Use file/filter mode described by man page. | `[CLI, POLY]` |
| `-g` | General output mode switch. | `[CLI, POLY, ENUM]` |
| `-m` | Mode switch documented in man page synopsis. | `[CLI, POLY, ENUM]` |
| `-P` | Option switch documented in man page synopsis. | `[CLI, POLY, ENUM]` |
| `-K` | Option switch documented in man page synopsis. | `[CLI, POLY, ENUM]` |
| `-b` | Option switch documented in man page synopsis. | `[CLI, POLY, ENUM]` |

---

## 4. Sage Optional-PALP Methods

Sage `LatticePolytope` documentation explicitly marks selected methods as requiring optional package `palp`:

- `all_points()`
- `all_points_boundary()`
- `all_points_not_interior_to_facets()`
- `integral_points()`
- `fibration_generator(dim)`

These methods are documented in Sage as wrapper-level surfaces that depend on PALP availability.

---

## 5. Assumptions and Constraints

- PALP command surfaces are CLI-first; inputs are lattice-polytope/weight-system text formats rather than typed in-process APIs.
- Option-rich programs (`nef.x`, `mori.x`) expose many mode switches; this reference records only source-backed synopsis-level argument contracts.
- For deterministic documentation/testing, wrapper workflows should pin explicit option selections and input representation mode.

---

## 6. Sources

- PALP package description (`palp`): `https://packages.ubuntu.com/jammy/math/palp`
- PALP package manpage (`palp(1)`): `https://manpages.debian.org/unstable/palp/palp.1.en.html`
- `poly.x(1)`: `https://manpages.org/polyx`
- `class.x(1)`: `https://manpages.org/classx`
- `cws.x(1)`: `https://manpages.org/cwsx`
- `nef.x(1)`: `https://manpages.debian.org/unstable/palp/nef.x.1.en.html`
- `mori.x(1)`: `https://manpages.org/morix`
- Sage lattice polytope docs: `https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/lattice_polytope.html`
- local provenance snapshot: `docs/archive/scope_violations/palp/upstream/palp_online_provenance_2026-02-17.md`
