# ZZLatWithIsom Online Provenance Note (2026-02-17)

This note localizes the online source evidence used in pass `20260217-11` for `ZZLatWithIsom` attribute-forwarding methods.

## Online sources surveyed

- OSCAR stable Hecke manual, lattices with isometry:
  - https://docs.oscar-system.org/stable/Hecke/manual/lattices/lattices_with_isometry/
- OSCAR dev Hecke manual, lattices with isometry (cross-check for drift):
  - https://docs.oscar-system.org/dev/Hecke/manual/lattices/lattices_with_isometry/

Access date (UTC): 2026-02-17

## Methods verified from online docs

The online manual explicitly documents `ZZLatWithIsom` attribute-forwarding methods including:

- `genus(Lf::ZZLatWithIsom)`
- `is_even(Lf::ZZLatWithIsom)`
- `is_integral(Lf::ZZLatWithIsom)`
- `is_primary(Lf::ZZLatWithIsom, p)` / `is_primary_with_prime(Lf::ZZLatWithIsom)`
- `is_elementary(Lf::ZZLatWithIsom, p)` / `is_elementary_with_prime(Lf::ZZLatWithIsom)`
- `rank(Lf::ZZLatWithIsom)` / `degree(Lf::ZZLatWithIsom)`
- `det(Lf::ZZLatWithIsom)` / `discriminant(Lf::ZZLatWithIsom)`
- `gram_matrix(Lf::ZZLatWithIsom)` / `rational_span(Lf::ZZLatWithIsom)`
- `signature_tuple(Lf::ZZLatWithIsom)`
- `scale(Lf::ZZLatWithIsom)` / `norm(Lf::ZZLatWithIsom)`
- `minimum(Lf::ZZLatWithIsom)`
- `is_positive_definite(Lf::ZZLatWithIsom)` / `is_negative_definite(Lf::ZZLatWithIsom)` / `is_definite(Lf::ZZLatWithIsom)`

The manual wording indicates these are accessed by calling the corresponding lattice function on the pair `(L, f)`, i.e., contracts are inherited from the underlying lattice unless method docs state otherwise.

## Local snapshot linkage

For reproducible offline context, see the in-repo snapshot:

- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom.md`

