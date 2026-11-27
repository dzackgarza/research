# Polyhedral Common Reference

Consolidated pointer to Mathieu Dutour Sikirić's `polyhedral_common` library (the
`dutsik_polyhedral` external tool). Replaces 15 vendored upstream documentation files
(BINARIES.md, INSTALL.md, DEVELOPER.md, the CI_tests/* and src_*/ READMEs, and the nav
index) that were previously copied verbatim into agent memory. The upstream docs are not
durable agent knowledge; what matters is which method families the tool provides and
where they live. For build/install specifics, read the upstream repository directly
rather than a stale copy.

## What the tool provides (method families relevant to this research)

- **Automorphism groups and isomorphism of forms** — automorphism group of a
  positive-definite or weighted graph/form; equivalence/isomorphism testing.
  (`src_latt`, `src_poly`)
- **Vector stabilizer / vector equivalence** — stabilizers of vectors and orbit
  equivalence under a form's automorphism group.
- **Isotropic k-plane / k-flag orbits** — enumeration of orbits of isotropic subspaces
  and flags, relevant to cusp/orbit classification. (`src_isotropy`)
- **Indefinite-form reduction** — indefinite LLL-style reduction and indefinite-form
  handling. (`src_latt`, see also the repo-specific synthesis in
  Polyhedral Common Indefinite Methods)
- **Lorentzian edge-walk / perfect-form enumeration** — perfect-form and T-space
  enumeration, Delaunay/IsoDelaunay computations. (`src_perfect`, `src_ctype`,
  `src_copos`, the Tspaces/L-domains CI tests)
- **Short-vector and sparse-solver utilities** — supporting numerical kernels.
  (`src_short`, `src_sparse_solver`)

## Provenance

Upstream: the `polyhedral_common` C++ library by M. Dutour Sikirić. The detailed
repo-specific decision guide (positive-definite vs indefinite pipeline contrast, the
`_Kernel` naming convention, and the per-task decision tables) is preserved separately as
the **Polyhedral Common Indefinite Methods** memory, which contains genuine local
synthesis rather than verbatim upstream text.
