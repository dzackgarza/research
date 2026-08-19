# External notebooks

Saved renderings of notebooks written elsewhere, kept as reference material.
Nothing here is authored in this repository.

- `fermat-quartic-periods-lefschetz-family.html` — an nbviewer rendering of the
  `lefschetz_family` package's own worked example, run under SageMath 9.5: the
  Fermat quartic surface \(X^4 + Y^4 + Z^4 + W^4 = 0\) in \(\mathbb{P}^3\) with
  a chosen linear fibration, the fibre's cohomology basis
  \([Z, Y, X, Z^5, YZ^4, XZ^4]\), six Picard-Fuchs operators of order three,
  the fibre period matrix computed to about 1000 bits by numerical analytic
  continuation, and the surface's integral homology reconstructed from the
  monodromy together with its intersection data.
  The page states that it renders a notebook hosted elsewhere, so it is a
  demonstration by the package's author, not a computation of ours. The two
  extraction specs under `notes/computations/extraction-specs/` assess what of
  this machinery is worth reimplementing.
