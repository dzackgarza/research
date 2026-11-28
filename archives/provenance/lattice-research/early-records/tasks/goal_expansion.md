# GOAL_EXPANSION: Tiered Research Backlog

## Sources

- `GOAL.md`
- `REFERENCES.md`
- `STATE_MACHINE.md`
- `PROOF_AUDITING.md`
- `theory/literature_claim_map.md`
- `theory/mathematical_background.md`
- `theory/library_integration.md`
- `theory/oscar_lattices.md`
- `theory/gap_orbits.md`
- `theory/indefinite_jl.md`
- `theory/buildings.md`
- `theory/carat_capabilities.md`
- `theory/moduli_dimension_claim.md`

## GOAL_INGEST Classification

| Goal item | Classification | Exact target | Mandatory expansion / split |
| --- | --- | --- | --- |
| `G1.1` sextic + K3 cover | exact computation | Produce one exact 10-nodal rational sextic and the associated double cover equation | Must fix a special 10-point configuration from literature; generic 10 points do not suffice |
| `G1.2` lattice invariants | exact computation with theorem-support value | Verify the exact lattice invariants, discriminant duality, and genus uniqueness statements for `S_Co` and `T_Co` | No hidden split if canonical constructors and invariant tools are fixed first |
| `G1.3` primitive embeddings | exact computation with theorem-support value | Produce explicit embedding matrices and primitivity certificates | Split direct `T_Co -> Lambda_K3` from the intermediate `T_En` / `T_dP` factorization |
| `G2.1` discriminant-group isotropic orbits | exact finite computation | Enumerate isotropic vectors in `A_{T_Co}` and their `O(q_T)`-orbits | No split once the finite orthogonal action backend is fixed |
| `G2.2` orbit lifting | theorem-support computation | Show the divisibility-2 primitive isotropic vectors form one lifted orbit | Requires an explicit reduction ledger from finite orbit data to the lattice claim |
| `G3.1` `Gamma_Co` generators | ambiguous theorem/computation target | Compute a defensible finite generator package for the stated arithmetic group | Split claim-fixing / finite-quotient data from any full-generator theorem claim; "minimal generators" is not currently well-defined |
| `G3.2` isotropic plane orbits | exact indefinite computation with theorem-support value | Enumerate primitive isotropic plane orbits and compute `J^perp / J` | Must use indefinite-lattice tooling; finite GAP orbit code is not an acceptable surrogate |
| `G4.1` Coxeter parabolics | exact computation with theorem-support value | Derive the Coxeter data from the lattice and classify maximal parabolic subdiagrams | Must generate the chamber/roots from the lattice; hand-entered diagrams are invalid |
| `G5.1` involution `theta` | exact computation with theorem-support value | Construct an involution on `Lambda_K3` whose eigenspaces match the target lattices | No hidden split once the embedding and involution backends are fixed |
| `G6.1` surgery vector + slc stability | mixed; likely staged theorem/conjecture path | Compute the surgery vector and determine whether the slc claim is locally provable | Split `h_Co -> ell` from the KSBA/singularity proof; theorem promotion is blocked until the AEGS/Kollar reduction ledger is explicit |

## Canonical Tool Routing

- Use Oscar/Hecke for lattice construction, genus computations, primitive embeddings,
  invariant and coinvariant lattices, and equivariant extensions.
- Use GAP only for finite group actions on discriminant groups and other finite exact
  orbit computations.
- Use Indefinite.jl and `buildings.sage` for indefinite orbit problems such as primitive
  isotropic lines and planes.
- Use CARAT only for finite positive-definite auxiliary group problems; do not route
  indefinite rank-11 or rank-22 work through CARAT.
- Do not implement ad hoc Nikulin, Vinberg, orbit, or involution algorithms when the
  repo already points to a mature exact backend.

## Shared Primitive Boundary

- Tier 0 must expose **object-level exact primitives**: constructors, coercions,
  transforms, invariant extractors, and exact predicates.
- Tier 0 should not hide task logic inside helpers like `assert_*`, `verify_*`, or
  bundled "proof-by-wrapper" APIs.
- Tier 2 may compose Tier 0 primitives into replayable gates against Tier 1 fixtures,
  expected values, and reduction ledgers.
- The audit target is: if the Tier 0 primitives are correct, the Tier 3 agent code that
  composes them should be locally readable and checkable.
- A hand-rolled replacement for a mature exact primitive is suspect even if a later gate
  passes; the construction path itself must remain in the trusted-base story.

## Tier 0: Shared Tools

| ID | Objective | Parent sufficiency | Dependencies | Risk | Deliverable |
| --- | --- | --- | --- | --- | --- |
| `T-0011` | Decontaminate `src/coble_geometry_foundation.sage` and request trusted-base admission for the exact shared primitive surface that survives the rewrite | Legalizes no `GOAL.md` burden by itself; it is the prerequisite that determines whether any lattice-tier task may reuse the shared base at all | `src/coble_geometry_foundation.sage`, `AGENTS.md`, `STATE_MACHINE.md`, `PROOF_AUDITING.md`, `theory/library_integration.md`, `theory/oscar_lattices.md`, `theory/gap_orbits.md`, `theory/indefinite_jl.md`, `theory/buildings.md` | High | infrastructure prerequisite |
| `T-0001` | Build canonical lattice constructors and coercions for `S_Co`, `T_Co`, `T_En`, `T_dP`, `Lambda_K3`, and the standard `U`, `A_1`, `E_8` factors, with exact conversion between the foundation library and Oscar objects | Supplies the canonical inputs for every lattice-theoretic task; discharges no `GOAL.md` burden by itself | `src/coble_geometry_foundation.sage`, `theory/oscar_lattices.md`, `theory/library_integration.md` | Low | shared tool |
| `T-0002` | Expose invariant and predicate primitives for rank, signature, determinant, `(r,a,delta)`, discriminant forms, Brown invariants, divisibility, and isotropicity in 2-elementary lattices | Supplies the invariant layer needed by `G1.2`, `G2.*`, and `G5.1` | `T-0001`, Nikulin-backed formulas in `theory/mathematical_background.md`, `theory/oscar_lattices.md` | Low | shared tool |
| `T-0003` | Expose composable embedding primitives such as embedding creation, composition, image extraction, orthogonal complement recovery, matrix export, and `is_primitive(...)`, backed by Oscar/Hecke | Supplies the exact embedding infrastructure for `G1.3`, `G5.1`, and the finite-quotient portion of `G3.1` | `T-0001`, `theory/oscar_lattices.md`, `theory/library_integration.md` | Medium | shared tool |
| `T-0004` | Expose finite discriminant-group action primitives: generator import, isotropic-set construction, orbit decomposition, stabilizer computation, and representative transport in GAP | Supplies the finite exact engine for `G2.1` and the finite discriminant-image pieces of `G3.1` | `T-0002`, `theory/gap_orbits.md` | Low | shared tool |
| `T-0005` | Expose indefinite-orbit primitives for primitive isotropic lines and planes, quotient-lattice recovery, and canonical representative export | Supplies the only acceptable engine for `G3.2` and other indefinite cusp-orbit tasks | `T-0001`, `theory/indefinite_jl.md`, `theory/buildings.md`, `theory/library_integration.md` | Medium | shared tool |
| `T-0006` | Expose reflective/Coxeter primitives that derive chambers, simple roots, and parabolic candidates from the lattice rather than from handwritten diagrams | Supplies the exact infrastructure for `G4.1` | `T-0001`, `theory/library_integration.md`, Alexeev reference chain in `REFERENCES.md` | Medium | shared tool |
| `T-0007` | Expose exact nodal-sextic primitives: linear-system construction from a fixed point configuration, singularity checks for ten `A_1` points, rationality/birationality checks, and K3-cover equation export | Supplies the reusable infrastructure for `G1.1` | `theory/literature_claim_map.md`, `theory/mathematical_background.md`, `REFERENCES.md` | Medium | shared tool |
| `T-0008` | Expose involution and polarization primitives: sign involution construction, invariant and coinvariant lattices, distinguished vector transport, and discriminant-image extraction | Supplies the exact infrastructure for `G5.1`, `G3.1`, and `G6.1` | `T-0003`, `theory/oscar_lattices.md`, `theory/library_integration.md` | Medium | shared tool |

## Tier 1: Fixture Discovery

| ID | Objective | Parent sufficiency | Dependencies | Risk | Deliverable |
| --- | --- | --- | --- | --- | --- |
| `T-1001` | Assemble standard lattice fixtures for `U`, `A_1`, `E_8`, and `Lambda_K3` with published rank/signature/determinant/isometry data | Gives `T-0001`, `T-0002`, `T-0003`, and `T-0008` known-good sanity checks | `REFERENCES.md`, `theory/oscar_lattices.md` | Low | fixture data |
| `T-1002` | Assemble the literature-backed invariant ledger for `S_Co`, `T_Co`, `T_En`, and `T_dP`, including the claimed `(r,a,delta)`, signatures, determinant data, and discriminant-form relations | Gives `G1.2`, `G1.3`, `G2.*`, and `G5.1` their canonical expected values | `GOAL.md`, `REFERENCES.md`, `theory/mathematical_background.md`, `theory/literature_claim_map.md` | Low | fixture data |
| `T-1003` | Assemble finite quadratic-form fixtures for 2-elementary forms, including known isotropic counts and small-orbit examples that exercise the discriminant-group machinery | Gives `T-0002` and `T-0004` finite exact targets before they touch `A_{T_Co}` | `theory/mathematical_background.md`, `theory/gap_orbits.md`, Nikulin references in `REFERENCES.md` | Medium | fixture data |
| `T-1004` | Assemble primitive-embedding fixtures with known complements or uniqueness properties, using standard examples and Oscar documentation-backed cases | Gives `T-0003` and downstream embedding tasks exact expected outcomes on trusted examples | `theory/oscar_lattices.md`, Nikulin/Huybrechts sources in `REFERENCES.md` | Medium | fixture data |
| `T-1005` | Assemble indefinite-orbit fixtures from Dawes and `buildings.sage`, including vector and isotropic-plane examples with published or doc-backed outputs | Gives `T-0005` a reference suite before it is used on `T_Co` | `theory/indefinite_jl.md`, `theory/buildings.md`, Dawes reference in `REFERENCES.md` | Medium | fixture data |
| `T-1006` | Assemble reflective-lattice and maximal-parabolic fixtures from the Alexeev line of references, restricted to cases already described explicitly in local docs | Gives `T-0006` known-good chamber/parabolic outputs before `S_Co` is attempted | `REFERENCES.md`, `theory/carat_capabilities.md` | Medium | fixture data |
| `T-1007` | Assemble a canonical 10-nodal sextic fixture package from local literature, including the point configuration, expected nodal profile, and parametrization data when available | Gives `T-0007` a literature-anchored target instead of a guessed point set | `REFERENCES.md`, `theory/literature_claim_map.md`, `theory/mathematical_background.md` | High | fixture data |
| `T-1008` | Assemble KSBA/stable-model fixtures and theorem-instance sheets from AEGS, Kollar, and Pieroni that are directly relevant to `B(ell)` and slc verification | Gives `G6.1` a chance to reach theorem status without improvised geometry | `REFERENCES.md`, `theory/mathematical_background.md` | High | fixture data |

## Tier 2: Thin Gates

| ID | Objective | Parent sufficiency | Dependencies | Risk | Deliverable |
| --- | --- | --- | --- | --- | --- |
| `T-2001` | Gate the lattice constructors and coercions by replaying `T-0001` and `T-0002` on `T-1001` and `T-1002`, then matching the exact object identities and invariant outputs | Any T-3 result using repo lattice objects must pass this before its lattice inputs are trusted | `T-0001`, `T-0002`, `T-1001`, `T-1002` | Low | assertion gate |
| `T-2002` | Gate the discriminant-form and invariant primitives by replaying them on `T-1002` and `T-1003`, then matching Brown invariants, divisibilities, and isotropic counts exactly | Blocks all discriminant-group and lifting claims until the finite quadratic data is exact | `T-0002`, `T-1002`, `T-1003` | Low | assertion gate |
| `T-2003` | Gate the embedding primitives by constructing embeddings with `T-0003` and then separately checking matrices, image lattices, complements, and `is_primitive(...)` against fixtures | Blocks all embedding and involution claims until the matrix-level objects and predicates are exact | `T-0003`, `T-1004`, `T-1002` | Medium | assertion gate |
| `T-2004` | Gate the finite-action primitives by replay, orbit-stabilizer consistency, and independent count checks on the discriminant-group action backend | Blocks `G2.1` and the finite quotient portion of `G3.1` until the GAP layer is trustworthy | `T-0004`, `T-1003` | Medium | assertion gate |
| `T-2005` | Gate the indefinite-orbit primitives by quotient-lattice reconstruction, representative normalization, and fixture comparison against the Dawes/buildings suite | Blocks `G3.2` until the indefinite orbit layer is exact and reproducible | `T-0005`, `T-1005`, `T-1002` | Medium | assertion gate |
| `T-2006` | Gate the sextic primitives by checking exact nodal multiplicities, rationality/birationality criteria, and K3-cover singularity profiles against `T-1007` | Blocks `G1.1` until the chosen sextic really matches the literature-backed geometry | `T-0007`, `T-1007` | Medium | assertion gate |
| `T-2007` | Gate the Coxeter primitives by checking that chamber/parabolic outputs are lattice-derived, match fixture cases where available, and never depend on handwritten adjacency matrices | Blocks `G4.1` until the reflective backend is doing real mathematics | `T-0006`, `T-1006` | Medium | assertion gate |
| `T-2008` | Gate the involution primitives by checking order, isometry, eigensublattice invariants, transported vectors, and discriminant-image consistency against the standard fixtures | Blocks `G5.1`, `G3.1`, and `G6.1` until the involution layer is exact | `T-0008`, `T-1001`, `T-1002`, `T-1004` | Medium | assertion gate |
| `T-2009` | Require a reduction ledger for every T-3 task that promotes exact computation toward a stronger `GOAL.md` statement | Prevents proof-burden laundering across `G1.2`, `G2.2`, `G3.*`, `G4.1`, `G5.1`, and `G6.1` | `STATE_MACHINE.md`, `GOAL.md` | Medium | assertion gate |
| `T-2010` | Require theorem-instance sheets mapping every KSBA/singularity hypothesis used in `G6.1` to local objects before any slc theorem claim is made | Prevents the `G6.1` stability task from collapsing back into prose theater | `T-1008`, `STATE_MACHINE.md`, `PROOF_AUDITING.md` | High | assertion gate |

## Tier 3: Mathematical Application

| ID | Objective | Parent sufficiency | Dependencies | Risk | Deliverable |
| --- | --- | --- | --- | --- | --- |
| `T-3001` | Fix a literature-backed special 10-point configuration and derive one exact rational sextic `F(x,y,z)=0` with ten nodes together with the K3-cover equation `w^2 = F` | Discharges the explicit-example burden of `G1.1`; it does not prove uniqueness or classify all such sextics | `T-0007`, `T-1007`, `T-2006` | High | exact computation |
| `T-3002` | Verify the exact invariants of `S_Co` and `T_Co`, their discriminant-form duality, and the genus/cardinality uniqueness claims stated in `GOAL.md` | Discharges the lattice-invariant burden of `G1.2`; broader moduli claims remain external literature | `T-0001`, `T-0002`, `T-1001`, `T-1002`, `T-2001`, `T-2002`, `T-2009` | Low | exact computation |
| `T-3003` | Construct an explicit primitive embedding `T_Co -> Lambda_K3` with matrix data, complement certificate, and exact provenance | Discharges the direct `Lambda_K3` portion of `G1.3`; the intermediate factorization remains separate | `T-0003`, `T-1002`, `T-1004`, `T-2003`, `T-2009` | Medium | exact computation |
| `T-3004` | Construct exact matrices for the factorization through `T_En` and `T_dP`, or return `REPLAN_REQUIRED` if the intermediate models are not fixed locally enough for an exact statement | Discharges the intermediate embedding-chain burden of `G1.3` only if the exact models are pinned; otherwise it exposes the missing prerequisite | `T-0001`, `T-0003`, `T-1002`, `T-1004`, `T-2001`, `T-2003`, `T-2009` | High | exact computation or replan delta |
| `T-3005` | Enumerate isotropic vectors in `A_{T_Co}` and compute the `O(q_{T_Co})`-orbit decomposition exactly | Discharges the finite discriminant-group computation in `G2.1` | `T-0002`, `T-0004`, `T-1002`, `T-1003`, `T-2002`, `T-2004` | Low | exact computation |
| `T-3006` | Combine the divisibility computation in `T_Co` with the finite orbit data to verify the unique divisibility-2 primitive isotropic orbit claim, with an explicit reduction ledger citing the Nikulin/Sterk step | Discharges the lifting burden of `G2.2`; it does not by itself settle higher-cusp geometry | `T-0002`, `T-0004`, `T-1002`, `T-1003`, `T-2002`, `T-2004`, `T-2009` | Medium | theorem-support exact computation |
| `T-3007` | Compute the finite discriminant-image and centralizer/stabilizer data that make the `Gamma_Co` claim surface precise, and state exactly what full-group burden remains | Discharges the claim-fixing and finite-quotient prerequisite of `G3.1`; it does not yet claim a full generator theorem | `T-0003`, `T-0008`, `T-1002`, `T-1004`, `T-2003`, `T-2008`, `T-2009` | High | exact computation |
| `T-3008` | Produce a defensible finite generator package for `Gamma_Co` if the kernel description is locally grounded, otherwise downgrade cleanly to a smaller exact claim or `REPLAN_REQUIRED` | Discharges `G3.1` only if the full arithmetic-group claim is justified exactly as stated | `T-3007`, `T-0005`, `T-2005`, `T-2008`, `T-2009` | Very high | exact computation or conjecture/replan delta |
| `T-3009` | Enumerate primitive isotropic plane orbits in `T_Co` and compute `J^perp / J` for each representative, testing the `A_1^{\oplus 7}` prediction exactly | Discharges the orbit/quotient burden of `G3.2`; global cusp statements still need their own reduction ledger | `T-0005`, `T-1002`, `T-1005`, `T-2005`, `T-2009` | High | exact computation |
| `T-3010` | Derive the Coxeter chamber for `S_Co` and classify maximal parabolic subdiagrams, including whether `\u007eB_7(2)` is the unique maximal parabolic type | Discharges the exact computation burden of `G4.1`; any geometric cusp interpretation still depends on a stated reduction ledger | `T-0006`, `T-1002`, `T-1006`, `T-2007`, `T-2009` | Medium | exact computation |
| `T-3011` | Construct an explicit involution `theta` on `Lambda_K3` and verify that its `+1` and `-1` eigensublattices match `T_Co` and `S_Co` with the required primitivity data | Discharges `G5.1` if the lattice and embedding certificates all pass | `T-0003`, `T-0008`, `T-1002`, `T-1004`, `T-2003`, `T-2008`, `T-2009` | Medium | exact computation |
| `T-3012` | Compute the map `h_Co -> ell` exactly and write the theorem-instance sheet that would be needed to promote the associated `B(ell)` stability claim | Discharges the mapping half of `G6.1` and determines whether the stability half is locally executable | `T-0008`, `T-1002`, `T-1008`, `T-2008`, `T-2010` | High | exact computation plus reduction ledger |
| `T-3013` | Verify the slc stability of `B(ell)` only if `T-3012` produces a complete theorem-instance sheet; otherwise preserve only a conjectural package with an explicit non-proof boundary | Discharges the stability half of `G6.1` only if the KSBA reduction is exact and complete | `T-3012`, `T-1008`, `T-2010`, `T-2009` | Very high | theorem or conjecture-evidence bundle |

## Dependency and Activation Order

### Wave A: canonical objects and low-risk exact claims

- Activate `T-0001`, `T-0002`, `T-0003`, `T-0007`, `T-0008`
- Activate `T-1001`, `T-1002`, `T-1003`, `T-1004`, `T-1007`
- Activate `T-2001`, `T-2002`, `T-2003`, `T-2006`, `T-2008`, `T-2009`
- Then activate `T-3002`, `T-3001`, `T-3003`, `T-3011`

### Wave B: finite orbit work and controlled extensions

- Activate `T-0004`, `T-1003`, `T-2004`
- Then activate `T-3005`, `T-3006`
- Activate `T-3004` only after the intermediate lattice models are fixed in the task
  spec

### Wave C: indefinite, Coxeter, and arithmetic-group work

- Activate `T-0005`, `T-0006`, `T-1005`, `T-1006`, `T-2005`, `T-2007`
- Then activate `T-3009`, `T-3010`, `T-3007`
- Activate `T-3008` only if `T-3007` leaves a precise, locally grounded full-group claim

### Wave D: KSBA / stability tail

- Activate `T-1008`, `T-2010`
- Then activate `T-3012`
- Activate `T-3013` only if the theorem-instance sheet is complete; otherwise route to
  `CONJECTURE_TRIAGE` or `REPLAN_REQUIRED`

## Immediate Notes for TASK_SELECTION

- `G1.2`, `G1.3` (direct `Lambda_K3` embedding), `G2.1`, `G2.2`, and `G5.1` are the best
  first wave: exact, source-backed, and close to the current foundation library.
- `G3.1` and `G6.1` are intentionally split because the current `GOAL.md` wording hides
  theorem-level burden that must not be smuggled through as "implementation details."
- `G3.2` must route through indefinite-lattice tooling.
  Any plan that reduces it to finite GAP orbit enumeration on a guessed finite subset
  fails pre-audit.
- `G4.1` is valid only if the root/chamber data are generated from the lattice.
  Hand-fed Coxeter matrices or copied adjacency tables are outside the accepted claim
  surface.
