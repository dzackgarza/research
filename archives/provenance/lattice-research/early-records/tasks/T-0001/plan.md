# Initial Plan

- Block PRE_AUDIT until T-0011 determines the admitted shared-base surface and trust
  limits for `src/coble_geometry_foundation.sage`.
- After T-0011, pin the exact primitive API and input/output contract against the
  admitted base only.
- Identify the mature backend entry points and local wrappers needed without
  reintroducing hand-rolled lattice logic.
- Complete TASK_SPECIFICATION only after the shared-code prerequisite is explicit and
  locally auditable.
