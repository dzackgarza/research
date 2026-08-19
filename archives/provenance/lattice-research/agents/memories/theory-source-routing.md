# Theory Stored Claim Facts

Trigger: before writing specs/plans/prose that uses Coble, K3, Enriques, two-elementary, discriminant-form, cusp, or period-domain claims.

Stored repo facts from `theory/`:

- `theory/` is the durable mathematical knowledge base, not a task tracker. Use its facts to implement/spec, but cite literature from `theory/references/` when writing standard claims.
- Source authority for standard claims is `theory/references/index.md`, `theory/references/claim-map.md`, `theory/references/references.bib`, and extracted files under `theory/references/literature/`.
- The classical Coble starting point is a rational plane sextic with ten nodes. Blow up the ten nodes to get the rational surface model; the K3 double cover and pullback of the hyperplane plus ten exceptional classes give the lattice with diagonal form `diag(2, -2, ..., -2)`.
- In the Coble moduli comparison, do not conflate the plane hyperplane class with the degree-2 polarization. `H^2 = 1` on the blowup and `f^*H` has square `2`; `K_S = -3H + sum_i E_i`, so `D = aH - sum_i b_iE_i` lies in `K_S^perp` iff `sum_i b_i = 3a`; the moduli polarization is `h_Co in K_S^perp subset Pic(S)` with `h_Co^2 = 2`, and its K3 pullback `tilde h_Co` has square `4`.
- Plane sextic arithmetic genus: `(d-1)(d-2)/2`; for `d = 6`, `g_a = 10`. Ten ordinary nodes have total delta `10`, so the geometric genus is `0`.
- For generic ten points in `P^2`, a nodal sextic is not expected because ten nodes impose `30` linear conditions on the `28`-dimensional space `H^0(O_{P^2}(6))`; explicit examples need special dependent configurations.
- The K3 lattice is `Lambda_K3 = U^3 + E_8(-1)^2`, signature `(3,19)`, rank `22`, even unimodular.
- `T_Co` is the orthogonal complement in `Lambda_K3` of the rank-11 pullback lattice computed from the geometric pipeline; do not define it by expected notation alone.
- Expected Coble transcendental lattice signature is `(2,9)`, rank `11`. Once that signature is established, the Type IV period domain has complex dimension `9`.
- The 9-dimensional Coble period-domain claim is standard literature, not a repo theorem. Repo computations are supporting evidence or exact worked examples.
- Primitive sublattice discriminant duality in a unimodular lattice: for primitive `S subset Lambda`, `rank(T) = rank(Lambda) - rank(S)`, `det(T) = det(S)` up to sign, and `q_T = -q_S`.
- Two-elementary lattices use Nikulin invariants `(r, a, delta)`: `r` rank, `a` F2-rank of the discriminant group, `delta` coparity. For the Coble pullback lattice, the diagonal model predicts 2-elementary discriminant order `2^11`, but that is a verification target, not an input axiom.
- For a computed discriminant group `(Z/2Z)^11`, the finite group has order `2048`; the note records `528` isotropic vectors in `A_T` including zero.
- Isotropic lines in Baily-Borel correspond to 0-cusps; isotropic planes correspond to 1-cusps/modular curves. Incidence is containment of representatives.
- A primitive isotropic plane `J` in rank-11 `T_Co` has `rank(J^perp) = 9` and `rank(J^perp/J) = 7`; the theory note predicts `J^perp/J = A_1^7`, but the orbit uniqueness claim is explicitly unverified computationally.
- `Gamma_Co` computations must name the typed Coble polarization being stabilized or transported. Downstairs `h_Co in K_S^perp` has square `2`; K3-side `tilde h_Co = f^*h_Co` has square `4`; `T_En = U + E_10(2)` has rank `12` and signature `(2,10)`. No explicit generators have been computed in the stored theory docs.
- `Gamma_En,2` is the image in `O(T_En)` of K3-lattice isometries commuting with `I_En` and fixing `h = e + f in U(2)`. It is not just an arbitrary hand-generated subgroup.
- The surgery-vector fact stored in theory must be typed before use: only pair `h_Co` or `tilde h_Co` with roots `alpha_i` after they have been placed in a common lattice or transported pairing. The slc stability verification was not established by old scripts.
- The old computational verification scripts were invalidated as print-theater or self-validating assertions. Treat their status claims as rejected unless rederived by source-backed code.

Source anchors for provenance: `theory/index.md`, `theory/references/index.md`, `theory/references/claim-map.md`, `theory/foundations/coble-task-background.md`, `theory/moduli/moduli-dimension-claim.md`, `theory/foundations/reflective-two-elementary-lattices.md`.

Verification: a future plan/spec should use the stored facts above directly, cite the relevant theory source when writing public prose, and mark any old-script-derived claim as unverified unless reproduced from actual lattice/geometric data.
