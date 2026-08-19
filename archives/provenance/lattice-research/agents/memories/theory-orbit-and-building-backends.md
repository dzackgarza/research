# Theory Orbit And Building Implementation Store

Trigger: implementing/specifying vector orbit equivalence, isotropic line/plane/flag orbits, cusp counts, Baily-Borel boundary graphs, Dawes algorithms, buildings.sage, or subgroup-sensitive orthogonal group methods.

Public nouns and API constraints:

- Do not create a public `Gamma` class. Keep public group API on `LatticeOrthogonalGroup`, `LatticeOrthogonalSubgroup`, `DiscriminantOrthogonalGroup`, and `DiscriminantOrthogonalSubgroup`.
- Subgroups are represented by condition-set predicates plus private structured metadata. Membership is mandatory; generator computation is optional and lazy.
- Public non-isotropic subgroup methods should live on both orthogonal group nouns: `special_orthogonal_subgroup()`, `plus_subgroup()`, `special_plus_subgroup()`, `preimage_of_discriminant_subgroup(A)`, `find_vector_isometry(v1,v2)`, `vectors_are_equivalent(v1,v2)`.
- Public isotropic subgroup methods should live on both orthogonal group nouns: `isotropic_line_orbits()`, `isotropic_plane_orbits()`, `isotropic_flag_orbits(k)`, `isotropic_lines_are_equivalent(v1,v2)`, `isotropic_planes_are_equivalent(basis1,basis2)`.
- Keep orchestration private. Non-isotropic vector-orbit logic belongs in `src/research/dawes_orbit_backend.py`. Isotropic subgroup splitting belongs in `src/research/isotropic_gamma_orbit_backend.py`. Raw binary wrappers belong in `src/external/py_polyhedral/binaries.py`. Public method shims belong in the existing lattice/group file, not on a new helper module.

Non-isotropic vector orbit store:

- Dawes common invariants: for rational vectors `v_i`, choose minimal positive `c_i` with `w_i = c_i v_i in L`. Reject immediately if `v_1^2 != v_2^2` or `c_1 != c_2`.
- Fast ambient route: call `INDEF_FORM_TestEquivalenceVector` for full `O(L)` if installed. If it returns `None`, no subgroup of `O(L)` can relate the vectors. If it returns a witness in the subgroup, accept. If witness is outside the subgroup, continue to a valid Dawes subgroup branch.
- Dawes Algorithm 2.1 applies when `v_1^perp` is definite. It works for arbitrary `Gamma subset O(L)` and only needs subgroup membership. Build primitive complements `K_i = w_i^perp`, enumerate `Iso(K_1,K_2)` with a definite-lattice backend, assemble candidate `theta = iota_2 (phi + psi) iota_1^{-1}`, and accept the first candidate in `Gamma`.
- Dawes Algorithms 2.2/2.3 apply only when `v_1^perp` is indefinite, `Gamma = O_A(L)` or a sufficiently structured arithmetic variant, the natural map `O(L) -> O(D(L))` is surjective, and discriminant/gluing data are available. They replace infinite lattice-isometry search by finite discriminant-form data: `D(<w_i>)`, `D(K_i)`, glue subgroups `H_i`, maps `iota_i`, and search over `{±1} + Iso(q_K1,q_K2)`.
- Do not run Algorithms 2.2/2.3 for opaque predicates. If complement is indefinite and subgroup metadata is black-box only, assert the missing branch hypothesis rather than weakening to ambient `O(L)`.
- Dawes `O^+` means kernel of the real spinor norm, not positive-cone preservation in general. Use Oscar `rational_spinor_norm`; positive-cone shortcuts require proof for the special case.
- Stable orthogonal group is the kernel of `O(L) -> O(D(L))`; keep `kernel_of_discriminant_action()` as the canonical public verb. Compose it with plus/special/preimage constructors rather than adding duplicate names.
- Structured subgroup metadata should track determinant restriction, real-spinor restriction, discriminant-subgroup restriction, and opaque/black-box status. Merge metadata through structured intersections; unions become opaque.

Isotropic subgroup orbit store:

- Do not use the Dawes non-isotropic backend for Sterk/Dutour-Sikiric/Hulek cusp claims. Isotropic line/plane/flag orbits use ambient isotropic orbit/stabilizer data plus finite quotient/double-coset splitting.
- Ambient full-group isotropic line, plane, and flag orbits should use Dutour-Sikiric `polyhedral_common`/Indefinite.jl binaries or buildings.sage. Stored Indefinite.jl calls: `INDEF_FORM_GetOrbit_IsotropicKplane(Q,k)` and `INDEF_FORM_GetOrbit_IsotropicKflag(Q,k)`.
- Structured subgroup splitting method: choose ambient arithmetic group `G_0`, compute ambient orbit representative `x` and stabilizer `G_x`, compute a finite quotient of `G_0`, compute image of target subgroup `Gamma`, compute double cosets `G_x \ G_0 / Gamma` in the finite quotient, lift quotient representatives back to ambient isometries, and apply them to `x`.
- The decisive abstraction is finite image data, not infinite generators for `Gamma`. Generate ambient `O(L)` generators, ambient isotropic stabilizer generators, finite quotient subgroup generators, and quotient-generator lifts. Do not require infinite subgroup generators merely for `Gamma`-orbits.
- Initial supported structured subgroup families: `O(L)`, `SO(L)`, `O^+(L)`, `SO^+(L)`, preimages of finite discriminant subgroups, intersections of those, and Enriques-style centralizer/stabilizer image subgroups. Exclude opaque `ConditionSet` subgroups with no finite quotient image.
- For degree-2 Enriques, construct `Gamma_En,2` as a preimage of the finite paper image intersected with the plus condition, not from ambient infinite generators. Use `N = U + U(2) + E_8(-2)`, ambient `O^+(N)`, and the stable-plus kernel for quotient reduction.
- Verification target for the degree-2 Enriques Case 1 is exactly `5` zero-cusps and `9` one-cusps; Sterk's five primitive isotropic representatives should be primitive, isotropic, and pairwise non-equivalent modulo `Gamma_En,2`.
- Stop and split prerequisite work if the subgroup quotient image cannot be computed, quotient words cannot be lifted to ambient matrices, the subgroup is opaque without finite-image data, or the task needs a new shared mathematical noun.

Buildings and Baily-Borel store:

- For a lattice of signature `(2,n)`, building nodes are orbits of primitive totally isotropic lines (0-cusps) and planes (1-cusps). Edges encode containment after choosing representatives.
- `buildings.sage` classes return `[lines, planes, incid]` from `H.building()`, with `lines` line orbit reps, `planes` plane orbit reps, and `incid` `(plane_idx,line_idx)` incidence pairs.
- Use `SubGp_A2t` for `~O^+(2U + A2)`, `SubGp_GK` for `~O^+(2U + <-6> + <-2>)`, `SubGp_UU2A2t` for `~O^+(U + U(2) + A2)`, `SubGp_UUmA2t(m,N)` for `~O^+(U + U(m) + A2)`, and `SubGp_U2U2A2t` for `~O^+(U(2)+U(2)+A2)`.
- `BigGp` methods: `ip`, `make_eichler`, `make_reflection`, `SL_emb_left`, `SL_emb_right`, `make_gens`, `make_gens_stab_E`, `make_gens_stab_e`.
- `Ell(N)` models principal congruence subgroup `Gamma(N) subset SL(2,Z)`; `expected_size() = N^3 prod_{p|N}(1 - 1/p^2)`.
- Lemma 3.10 level store: for `L subset L'` maximal overlattice, choose `M` with `L'(M) subset L`; congruence level `N` is exponent of `L^vee / L'(M)`. Larger safe levels may be used but increase cosets.
- Eichler transvections use `t(e,a): v -> v - (a,v)e + (e,v)a - 1/2(a,a)(e,v)e` and belong to the stable plus group. buildings.sage `eichler_equiv(x,y)` implements the primitive-isotropic equivalence element.

Source anchors: `theory/algorithms/dawes-nonisotropic-vector-orbits`, `theory/algorithms/dawes-orbit-backend`, `theory/algorithms/isotropic-gamma-orbit-backend`, `theory/algorithms/buildings`, `theory/backends/buildings`, `theory/backends/indefinite-jl`.

Verification: a future orbit implementation should state the branch regime, assert the exact hypotheses before entering it, use the public group nouns above, and test with paper-backed fixtures rather than mocked orbit counts.
