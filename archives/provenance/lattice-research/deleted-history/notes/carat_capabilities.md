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
