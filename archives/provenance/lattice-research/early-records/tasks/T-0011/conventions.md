# Conventions

- Ambient mathematical objects are exact integral lattices and exact morphisms between
  them.
- Shared-base nouns are exact mathematical objects only: lattice objects, embedding
  objects, discriminant data objects, and orbit-problem objects.
- Shared-base verbs are exact operations on those objects only: construct, coerce,
  transform, extract invariant, compute stabilizer/orbit representative when the theory
  docs route that operation to a mature exact backend.
- Equality and equivalence claims in this task mean exact backend-certified equality,
  isometry, or orbit equivalence only; no sampled, bounded, or heuristic surrogate is an
  admissible substitute.
- Basis/order/signature conventions for standard lattice objects follow the canonical
  local sources cited in `GOAL.md` and `theory/oscar_lattices.md`; this task may not
  silently switch conventions to fit implementation convenience.
- For the current pre-audit package, the public shared surface is defined by the
  exported `__all__` list in `src/coble_geometry_foundation.sage`; defined but
  unexported symbols are not admitted by implication.
- The named lattice objects fixed in the current admitted candidate surface are
  `Lambda_K3_lattice`; `S_Co_lattice`, `T_Co_lattice`, `T_En_lattice`, `T_dP_lattice`,
  and `S_En_lattice` remain outside the admitted candidate surface until their exact
  local backend provenance is pinned in a later replan.
- `Lambda_K3_lattice` must follow the canonical K3-lattice backend object routed by
  `theory/oscar_lattices.md`, not an ad hoc block-diagonal surrogate.
- `S_Co_lattice`, `T_Co_lattice`, and `T_En_lattice` are downstream-required named
  objects, but they are not admitted by `T-0011` under the current pre-audit package
  because their exact local backend constructor provenance is not yet fixed.
- `is_primitive_embedding` is not admitted by `T-0011` under the current pre-audit
  package because the local docs fix its intended predicate meaning but not one exact
  backend binding for the wrapper symbol.
- The admitted discriminant-side surface stops at `discriminant_group` returning the
  backend torsion quadratic module object; wrapper symbols for discriminant form,
  structure, or element-value access are not admitted in the current package.
- `rank_one_lattice` is admitted only as the exact rank-one constructor routed through
  Oscar's `integer_lattice(gram = ...)` creation interface.
- `A1_lattice` and `E8_lattice` are not admitted by `T-0011` under the current pre-audit
  package because the local docs pin the `root_lattice` family but do not yet freeze a
  symbol-level sign/scaling contract for these wrapper names.
- `divisibility` is not admitted by `T-0011` under the current pre-audit package because
  the local docs pin the backend operation name but do not yet freeze a symbol-level
  input representation contract and certificate obligation for the wrapper.
- `orthogonal_complement` is not admitted by `T-0011` under the current pre-audit
  package because the local docs pin an operation name but not a fully frozen
  symbol-level input contract and replay obligation for the wrapper.
- `compute_orbits_gap`, `stabilizer_subgroup`, and `orbit_of_element` are not admitted
  by `T-0011` under the current pre-audit package because the local docs pin the GAP
  operation names but not one exact action model, domain representation, and certificate
  obligation for the wrapper symbols.
- Shared-base code may expose exact primitives only; reusable contract assertions belong
  in downstream gate tasks, not in the admitted shared base.
- If a routed backend cannot provide an exact operation for a candidate primitive, that
  primitive is excluded from admission rather than replaced with hand-rolled search.
