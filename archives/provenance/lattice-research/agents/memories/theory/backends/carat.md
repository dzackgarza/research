# CARAT capability audit for lattice-group computations

## Scope

This note records a doc-first audit of CARAT as a possible exact-computation backend for
this repo's lattice-group tasks.

Primary upstream sources reviewed:

- `README.md`
- `tex/progs/Aut_grp.html`
- `tex/progs/Normalizer.html`
- `tex/progs/Normalizer_in_N.html`
- `tex/progs/Orbit.html`
- `tex/progs/Isometry.html`
- `tex/progs/Shortest.html`
- `tex/progs/Form_space.html`
- `tex/progs/Tr_bravais.html`
- `tex/progs/First_perfect.html`
- `functions/Orbit/README`

## Critical limitation: CARAT requires positive-definite forms

**CARAT cannot handle indefinite quadratic forms.** The following tools require positive-definite input:

- `Aut_grp` — first form must be symmetric positive-definite
- `Isometry` — first form in each file must be positive-definite
- `Shortest` — positive-definite forms only

**For indefinite forms, use Indefinite.jl instead.**

**Indefinite.jl** (Dawes, arXiv:2205.10601) provides:
- Automorphism groups of indefinite forms
- Isometry testing for indefinite forms
- Orbit representatives of vectors, isotropic k-planes, isotropic k-flags

**Documentation:** `theory/backends/indefinite-jl`

**BibTeX:** `@article{dawes2022orbits, ...}` in `references.bib`

## What CARAT can plausibly replace here

### `Aut_grp`

- Upstream description: computes generators for the finite group of all `g ∈ GL_n(Z)`
  with `g^T F g = F` for every input form `F`.
- Repo relevance: exact automorphism / orthogonal-group generation for integral
  symmetric forms, especially when a task reduces to preserving one positive-definite
  Gram matrix or a tuple of exact forms.
- Likely use here: exact stabilizer/orthogonal-group computations for positive-definite
  auxiliary lattices, small-rank quotients, or finite form-preserving searches.

### `Normalizer`

- Upstream description: computes matrices which, together with a finite unimodular group
  `G`, generate the normalizer `N_GL_n(Z)(G)`.
- Repo relevance: exact normalizer/stabilizer workflows once a finite matrix group has
  been isolated.
- Likely use here: replacing hand-rolled normalizer searches in finite positive-definite
  settings related to Task 3.1 or finite quotient/stabilizer problems.

### `Orbit`

- Upstream description: computes orbits under several actions and can also compute
  stabilizers.
- Repo relevance: exact orbit/stabilizer calculations for finite matrix-group actions.
- Likely use here: orbit representatives and stabilizers for finite exact searches after
  a group has already been constructed.

### Supporting tools

- `Isometry`: exact integral isometry test between tuples of forms.
- `Shortest`: shortest vectors of a positive-definite form; useful preprocessing for
  `Aut_grp` / `Isometry`.
- `Form_space`: invariant-form space of a group.
- `Tr_bravais`: computes `G^T`, which `Normalizer` can consume.
- `First_perfect`: produces a nearby `G`-perfect form for `Normalizer` workflows.

## Most relevant upstream cautions

- CARAT was developed mainly for crystallographic groups in dimensions up to 6; higher
  dimensions may still work, but the README explicitly warns that integer overflow is
  not trapped in general.
- Building from a GitHub checkout requires `./autogen.sh`, then `./configure && make`.
- CARAT depends on GMP headers/libraries.
- `Aut_grp` / `Shortest` are tailored to positive-definite symmetric-form workflows.
- `Orbit` may be infinite; upstream docs explicitly recommend bounding such runs.
- `Normalizer` complexity is controlled by the dimension of the invariant-form space.

## Incorporation guidance for this repo

### Good targets

- Exact orthogonal-group computations for finite positive-definite lattices.
- Exact stabilizer/normalizer computations once a finite matrix group is already known.
- Exact orbit/stabilizer computations on finite sets where Sage code is currently doing
  bespoke enumeration.

### Poor targets / caution cases

- Directly trusting CARAT as a black-box replacement for indefinite rank-11 or rank-22
  lattice problems without a smaller positive-definite reduction.
- Any workflow that fundamentally needs dimensions beyond CARAT's documented sweet spot
  without an exact audit of overflow risk and output correctness.

## Current repo-specific conclusion

CARAT is worth incorporating as an **audited auxiliary tool**, not as a blanket rewrite
of the current Sage workflows.

Best immediate route:

- use CARAT selectively for finite positive-definite subproblems arising inside Tasks
  3.1, 3.2, 4.1, or 5.1;
- prefer `Aut_grp`, `Normalizer`, and `Orbit` only after reducing to an exact finite
  matrix-group problem with small/runnable dimension;
- keep Sage as the orchestration layer and document every CARAT call with its exact
  input matrices and downstream verification.

---

## Practical usage guide

### Tool capability matrix

| Tool | Definite required? | Input format | Output |
|------|-------------------|--------------|--------|
| `Aut_grp` | **Yes** — first form must be symmetric positive-definite | `matrix_TYP` (multi-form) | Generators of Aut({F_i}) ⊂ GL_n(Z) |
| `Isometry` | **Yes** — first form in each file must be positive-definite | Two `matrix_TYP` files | g ∈ GL_n(Z) with g^T F₁ g = F₂, or "not isometric" |
| `Normalizer` | No — works with any finite G ⊂ GL_n(Z) | `bravais_TYP` (group generators) | Generators of N_{GL_n(Z)}(G) |
| `Orbit` | No — works with any G ⊂ GL_n(Z) | `matrix_TYP` + `bravais_TYP` | Orbit representatives (use `-L` to bound infinite orbits) |
| `Z_equiv` | No — but G, H must be **finite** subgroups of GL_n(Z) | Two `bravais_TYP` files | X ∈ GL_n(Z) conjugating G to H, or "not conjugate" |
| `Is_finite` | No | `bravais_TYP` | "finite" + order, or "infinite" |
| `Shortest` | **Yes** — positive-definite forms only | `matrix_TYP` (symmetric) | Shortest vectors |

**Key insight:** CARAT's **definite-only** tools are `Aut_grp`, `Isometry`, `Shortest`. Everything else (`Normalizer`, `Orbit`, `Z_equiv`, `Is_finite`) works with arbitrary finite matrix groups, regardless of how they were obtained.

### Input file formats

**bravais_TYP format** (for groups — used by `Normalizer`, `Orbit`, `Z_equiv`, `Is_finite`):
```
#g<n>          % number of generators
<dim>          % generator 1
<row 1>
<row 2>
...
<dim>          % generator 2
...
```

**matrix_TYP format** (for forms — used by `Aut_grp`, `Isometry`):
```
#<num_forms>

<dim> d0
1

<dim> d1
<coefficients>

<dim>x0        % Gram matrix (lower triangle)
<diag>
<off> <diag>
...
```

### Worked examples

#### Example 1: Automorphism group of a positive-definite lattice

```bash
# A2 lattice Gram matrix
cat > A2.mat << 'EOF'
#1

2 d0
1

2x0
2
-1 2
EOF

./bin/Aut_grp A2.mat
```

Output:
```
#g3 % 
2       % generator
 -1  0
  0 -1
2       % generator
 0 1
 1 0
2       % generator
 1  0
 0 -1
2^3   = 8 % order of the group
```

**Use case:** Compute O(L) for auxiliary positive-definite lattices (e.g., finite quotients, sublattices).

#### Example 2: Normalizer of a finite matrix group

```bash
# Group G generated by -I in dimension 2
cat > group << 'EOF'
#g1
2
 -1  0
  0 -1
EOF

./bin/Normalizer group > norm
```

Output includes generators extending G to N_{GL_2(Z)}(G).

**Use case:** Given a finite subgroup G ⊂ GL_n(Z) (e.g., from `Aut_grp` or constructed in Sage), compute its normalizer. This works for **any** finite G, not just those from definite forms.

**Workflow from Ex7:** After computing normalizer, edit output to make it reusable:
```bash
# Edit 'norm': change header to #g<N> where N = original + new generators
# Remove invariant form data if present
./bin/Is_finite norm   # Verify still finite (or infinite, as expected)
```

#### Example 3: Isometry testing (Z-equivalence of forms)

```bash
# Form 1: A2
cat > F1.mat << 'EOF'
#1
2 d0
1
2x0
2
-1 2
EOF

# Form 2: A2 (same, for testing)
cp F1.mat F2.mat

./bin/Isometry F1.mat F2.mat
```

Output: transformation matrix g with g^T F₁ g = F₂, or indication that no isometry exists.

**Use case:** Test if two positive-definite Gram matrices represent isometric lattices. Returns explicit isometry if it exists.

#### Example 4: Conjugacy testing of finite groups (Z_equiv)

```bash
# Group G
cat > G << 'EOF'
#g1
2
 -1  0
  0 -1
EOF

# Group H (conjugate to G)
cat > H << 'EOF'
#g1
2
 -1  0
  0 -1
EOF

./bin/Z_equiv G H
```

Output: X ∈ GL_n(Z) with X G X^{-1} = H, or indication that groups are not conjugate.

**Use case:** Test if two finite subgroups of GL_n(Z) are conjugate. Both groups must be finite, but need not come from definite forms.

#### Example 5: Orbit computation

```bash
# Matrix X to compute orbit of
cat > X.mat << 'EOF'
2
1 0
0 1
EOF

# Group G (bravais_TYP format)
cat > G << 'EOF'
#g1
2
 -1  0
  0 -1
EOF

# Compute orbit under conjugation
./bin/Orbit -c X.mat G
```

Options:
- `-c`: conjugation action (X → g X g^{-1})
- `-l`: left multiplication (X → g X)
- `-r`: right multiplication (X → X g)
- `-q`: quadratic form action (X → g^{-T} X g^{-1})
- `-L <n>`: limit orbit size to n (essential for infinite orbits)

**Use case:** Compute orbit representatives under finite group actions. Use `-L` to bound computation when orbit may be infinite.

### Typical workflows for this repo

**Compute O(L) for positive-definite L:**
```bash
# 1. Write Gram matrix in matrix_TYP format
# 2. Run Aut_grp
# 3. Parse generators and order
```

**Compute Stab_v(O(L)) for v ∈ L:**
```bash
# 1. Compute G = Aut(L) via Aut_grp (definite L only)
# 2. Write v as matrix/column
# 3. Run Orbit -l v.mat G to get orbit
# 4. Stabilizer is subgroup fixing v (may need post-processing in Sage)
```

**Compute N_{GL_n(Z)}(G) for finite G:**
```bash
# 1. Write G generators in bravais_TYP format
# 2. Run Normalizer
# 3. Edit output to extract new generators
# Works for ANY finite G, not just from definite forms
```

**Test if G, H ⊂ GL_n(Z) are conjugate:**
```bash
# 1. Write both in bravais_TYP format
# 2. Run Z_equiv
# 3. Returns conjugating matrix or "not conjugate"
# Both G and H must be finite
```

**Test if two positive-definite forms are isometric:**
```bash
# 1. Write both in matrix_TYP format
# 2. Run Isometry
# 3. Returns isometry g with g^T F1 g = F2
# Requires positive-definite input
```

### Common pitfalls

1. **Aut_grp on indefinite forms**: Will hang or return garbage. Only use with positive-definite input.
2. **Isometry on indefinite forms**: Explicitly requires positive-definite input.
3. **Normalizer on infinite groups**: May not terminate. Use `Is_finite` first if unsure.
4. **Orbit without bounds**: Infinite orbits will run forever. Always use `-L <n>` for exploratory runs.
5. **bravais_TYP format errors**: Generator count (`#g<n>`) must match actual number of generators.
6. **Editing Normalizer output**: Output includes invariant forms; must remove them and update generator count before reusing as input.

### Verification strategy

1. **Aut_grp**: Verify each generator g satisfies g^T F g = F
2. **Normalizer**: Verify new generators normalize G: g^{-1} G g = G
3. **Isometry**: Verify g^T F1 g = F2 explicitly
4. **Z_equiv**: Verify X G X^{-1} = H
5. **Orbit**: Verify orbit representatives are in distinct G-orbits
6. **Cross-check with Sage**: Group orders, generator relations, known classifications
