# src/backends/external

Vendored third-party binaries and Python wrappers used by the research codebase.
This directory is excluded from repo quality-control checks.

## carat/ — CARAT submodule

`carat/` is the upstream CARAT submodule from
`https://github.com/lbfm-rwth/carat.git`.

Use it only through documented backend-routing work. The repo capability audit is
`theory/backends/carat.md`; the important boundary is that CARAT is useful for
positive-definite form automorphism/isometry work and finite matrix-group auxiliary
work, not as a general indefinite lattice backend.

## py_polyhedral/ — Python wrapper

`py_polyhedral/` is vendored from
[MathieuDutSik/py_polyhedral](https://github.com/MathieuDutSik/py_polyhedral),
modified so `get_binary_path` resolves against `src/backends/external/bin/`.
All Python code in the research codebase accesses polyhedral_common binaries
through this wrapper.
Missing binaries raise `FileNotFoundError` at call time with a pointer to this file.

## bin/ — polyhedral_common binaries

Compiled C++ binaries from
[MathieuDutSik/polyhedral_common](https://github.com/MathieuDutSik/polyhedral_common).
Each is built from the corresponding `src_*/` subdirectory using `make` directly
(**not** the top-level `CMakeLists.txt`, which requires MPI for parallel variants).

| Binary | Source dir | Purpose |
|---|---|---|
| `INDEF_FORM_TestEquivalence` | `src_indefinite` | Integral equivalence of indefinite forms; returns witness matrix |
| `INDEF_FORM_AutomorphismGroup` | `src_indefinite` | Automorphism group generators |
| `INDEF_FORM_GetOrbitRepresentative` | `src_indefinite` | Orbit representatives at given norm |
| `INDEF_FORM_GetOrbit_IsotropicKplane` | `src_indefinite` | Orbits of isotropic k-planes |
| `INDEF_FORM_StabilizerVector` | `src_indefinite` | Generators of Stab_{O(Q)}(v) for any integer vector v |
| `INDEF_FORM_StabilizerIsotropicPlane` | `src_indefinite` | Generators of stabilizer of an isotropic k-plane or k-flag |
| `LATT_FindIsotropic` | `src_isotropy` | Find an isotropic vector |
| `LATT_Canonicalize` | `src_latt` | Canonical form of a positive-definite lattice |
| `CP_TestCopositivity` | `src_copos` | Test copositivity of a form |
| `CP_TestCompletePositivity` | `src_copos` | Test complete positivity |
| `POLY_DirectFaceLattice` | `src_poly` | Face lattice of a polyhedron |

The following binaries from `py_polyhedral`'s full surface were not built due to
OOM or link failures during compilation on this machine (heavy C++20 template
instantiation in enormous translation units):

| Binary | Source dir | Obstacle |
|---|---|---|
| `LORENTZ_ReflectiveEdgewalk` | `src_lorentzian` | OOM: `LORENTZ_FundDomain_AllcockEdgewalk.cpp` killed by kernel |
| `POLY_DirectSerialDualDesc` | `src_dualdesc` | OOM: `POLY_SerialDualDesc.cpp` (~4 GB RAM during compile) |
| `LATT_SerialComputeDelaunay` | `src_delaunay` | Depends on MPI objects; see below |
| `LATT_SerialLattice_IsoDelaunayDomain` | `src_delaunay` | Depends on MPI objects; see below |

---

## Rebuilding the binaries

### Prerequisites

```sh
sudo apt-get install -y \
    g++ make \
    libeigen3-dev \
    libboost-serialization-dev \
    libgmp-dev libgmpxx4ldbl \
    libbliss-dev \
    libflint-dev \
    libglpk-dev \
    libcdd-dev \
    libopenmpi-dev
```

### Clone polyhedral_common (with submodules)

```sh
git clone --recursive https://github.com/MathieuDutSik/polyhedral_common /tmp/polyhedral_common
BASE=/tmp/polyhedral_common
```

### Build Mathieu's nauty fork (required: system nauty 2.9+ is incompatible)

```sh
git clone --depth=1 --branch 2.8.9 https://github.com/MathieuDutSik/nauty /tmp/nauty-mathieu
cd /tmp/nauty-mathieu
CC=/usr/bin/gcc ./configure --prefix=/tmp/nauty-install
make -j$(nproc) && make install
```

### Common make variables

All per-directory builds use these variables (adjust paths if nauty or headers
are in different locations). If conda/miniforge gcc appears before system gcc on
PATH, the `CC=` override is required — the conda linker cannot find the OpenMPI
runtime libraries.

```sh
MAKE_VARS='
  CC="/usr/bin/g++ -std=c++20 -Wall -Wextra -O3 -g"
  GMP_INCDIR=/usr/include/x86_64-linux-gnu
  GMP_CXX_LINK="-lgmp -lgmpxx"
  BOOST_INCDIR=/usr/include
  BOOST_LINK="-lboost_serialization"
  EIGEN_PATH=/usr/include/eigen3
  NAUTY_INCLUDE="-I/tmp/nauty-install/include"
  NAUTY_LINK="/tmp/nauty-install/lib/libnauty.a"
  LIBBLISS_LINK="-lbliss"
  LIBBLISS_INCDIR=/usr/include
  GLPK_LINK="-lglpk"
  GLPK_INCDIR=/usr/include
  MPI_LINK_CPP=""
  CHOICE_COMPILATION=""
'
```

### src_indefinite

```sh
cd $BASE/src_indefinite
make $MAKE_VARS \
    INDEF_FORM_TestEquivalence INDEF_FORM_AutomorphismGroup \
    INDEF_FORM_GetOrbitRepresentative INDEF_FORM_GetOrbit_IsotropicKplane \
    INDEF_FORM_StabilizerVector INDEF_FORM_StabilizerIsotropicPlane
```

### src_isotropy

```sh
cd $BASE/src_isotropy
make $MAKE_VARS LATT_FindIsotropic
```

### src_latt

```sh
cd $BASE/src_latt
make $MAKE_VARS LATT_Canonicalize
```

### src_copos

```sh
cd $BASE/src_copos
make $MAKE_VARS CP_TestCopositivity CP_TestCompletePositivity
```

### src_poly

```sh
cd $BASE/src_poly
make $MAKE_VARS \
    FLINT_LINK="-lflint" \
    CDDLIB_GMP_LINK="-lcddgmp" \
    POLY_DirectFaceLattice
```

### src_delaunay (Serial variants only)

src_delaunay's Makefile builds all objects before linking any binary, including
MPI variants.  Pass MPI include headers so the MPI object files compile even
though we omit the MPI runtime from the link step:

```sh
cd $BASE/src_delaunay
make $MAKE_VARS \
    "CFLAGS=-I/usr/include/x86_64-linux-gnu -I/usr/include -I/usr/include/eigen3 \
     -I/tmp/nauty-install/include -I/usr/lib/x86_64-linux-gnu/openmpi/include" \
    LATT_SerialComputeDelaunay LATT_SerialLattice_IsoDelaunayDomain
```

### src_lorentzian / src_dualdesc

These subdirectories contain translation units (`LORENTZ_FundDomain_AllcockEdgewalk.cpp`,
`POLY_SerialDualDesc.cpp`) that require up to 4 GB of RAM during compilation.
On memory-constrained machines the kernel OOM-killer terminates the compiler.
To build on a machine with ≥ 16 GB RAM:

```sh
# lorentzian
cd $BASE/src_lorentzian
make $MAKE_VARS \
    CDDLIB_GMP_LINK="-lcddgmp" \
    CDDLIB_INCLUDE="-I/usr/include/cddlib" \
    "CFLAGS=-I/usr/include/x86_64-linux-gnu -I/usr/include -I/usr/include/eigen3 \
     -I/tmp/nauty-install/include -I/usr/lib/x86_64-linux-gnu/openmpi/include" \
    LORENTZ_ReflectiveEdgewalk

# dualdesc
cd $BASE/src_dualdesc
make $MAKE_VARS \
    CDDLIB_GMP_LINK="-lcddgmp" \
    "CFLAGS=-I/usr/include/x86_64-linux-gnu -I/usr/include -I/usr/include/eigen3 \
     -I/tmp/nauty-install/include -I/usr/include/cddlib \
     -I/usr/lib/x86_64-linux-gnu/openmpi/include" \
    POLY_DirectSerialDualDesc
```

### Copy into repo

```sh
REPO=/path/to/research
cp $BASE/src_indefinite/INDEF_FORM_* $REPO/src/external/bin/
cp $BASE/src_isotropy/LATT_FindIsotropic $REPO/src/external/bin/
cp $BASE/src_latt/LATT_Canonicalize $REPO/src/external/bin/
cp $BASE/src_copos/CP_Test* $REPO/src/external/bin/
cp $BASE/src_poly/POLY_DirectFaceLattice $REPO/src/external/bin/
# If delaunay/lorentzian/dualdesc were built:
cp $BASE/src_delaunay/LATT_Serial* $REPO/src/external/bin/
cp $BASE/src_lorentzian/LORENTZ_ReflectiveEdgewalk $REPO/src/external/bin/
cp $BASE/src_dualdesc/POLY_DirectSerialDualDesc $REPO/src/external/bin/
```

### Notes

- **Do not use** the top-level `CMakeLists.txt` — it requires MPI for all targets.
- Compilation of each binary takes 5–30 minutes (heavy C++20 template instantiation).
- Each binary is ~600 MB unstripped. Run `strip bin/*` to reduce to ~2 MB each.
- All binaries use `PYTHON` output mode: pass `PYTHON <output_file>` as the last
  two arguments; results are written as Python literals readable by `ast.literal_eval`.
