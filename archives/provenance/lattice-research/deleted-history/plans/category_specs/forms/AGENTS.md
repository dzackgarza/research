# AGENTS.md — forms

This subtree owns category specs for modules equipped with forms.

Rules:

- `FormedModules(R)` is the named owner for `Modules(R).WithForms()`.
- Keep generic formed-module structure here: `WithForms`, `Bilinear`, `Quadratic`,
  symmetry, alternating, nondegeneracy, definiteness, integrality, rationality, and
  free bilinear modules.
- Modules may route or re-export these categories, but they do not own the form
  method surface.
- Lattices own only the lattice endpoint and lattice-specific refinements such as
  `Lattice`, `OverIntegers`, `Even`, `Unimodular`, and lattice construction categories.
- Tensor algebra components own tensor objects. Scalar-valued bilinear forms may be
  constructed as `(0,2)` tensors there and then interpreted through this subtree.
