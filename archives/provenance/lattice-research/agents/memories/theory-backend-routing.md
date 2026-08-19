# Theory Backend Method Store

Trigger: before implementing mathematical methods, exact tests, fixtures, spec method owners, or backend bridges.

Stored invariant: implement a semantic method on the repo noun, then thinly bridge to mature exact software. Do not write local mathematical algorithms until a backend-gap card proves a true open-source gap and the user approves bespoke work.

Backend method map:

- SageMath owns orchestration, Sage category machinery, and bridges to GAP, Singular, PARI/GP, and native Sage constructs.
- GAP owns finite groups, group actions, orbits, stabilizers, double-cosets when available, and finite quotient computations. Core calls: `Orbit`, `Orbits`, `OrbitsDomain`, `Stabilizer`, `OrbitStabilizer`, `IsTransitive`; action selectors include `OnRight`, `OnSets`, `OnTuples`, `OnLines`, and `OnSubspacesByCanonicalBasis`.
- Singular owns curve singularities, polynomial solving, Brill-Noether/Riemann-Roch spaces, normalization, and resolution. Stored calls: `Adj_div`, `NSplaces`, `BrillNoether`, `HNexpansion`, `Param`, `solve`, `isolate`, `triangLf`, `triang_solve`, `regDecomp`.
- Macaulay2 owns abstract blowups, exceptional divisors, sheaf cohomology, Hilbert polynomials, tangent/cotangent sheaves, divisors, and algebraic-geometry computations. Stored calls: Schubert2 `blowup(i)`, `exceptionalDivisor`, `canonicalDivisor`, `hilbertPolynomial`, `dim HH^i(F)`, `cotangentSheaf(p, X)`, `tangentSheaf(X)`, `chern`, `integrate`.
- Oscar/Hecke/Nemo owns integer lattices, quadratic forms, discriminant groups, primitive embeddings/extensions, equivariant extensions, centralizer images, genera, local isometry, and exact algebra. Stored calls: `integer_lattice`, `root_lattice`, `hyperbolic_plane_lattice`, `k3_lattice`, `rank`, `det`, `signature_tuple`, `genus`, `class_number`, `discriminant_group`, `primitive_embeddings`, `primitive_extensions`, `equivariant_primitive_extensions`, `admissible_equivariant_primitive_extensions`, `integer_lattice_with_isometry`, `invariant_lattice`, `coinvariant_lattice`, `invariant_coinvariant_pair`, `kernel_lattice`, `image_centralizer_in_Oq`, `discriminant_representation`, `rational_spinor_norm`, `vinberg_algorithm`.
- Indefinite.jl owns indefinite form automorphism/isometry/orbit work. Stored calls: `INDEF_FORM_AutomorphismGroup(Qmat)`, `INDEF_FORM_TestEquivalence(Q1,Q2)`, `INDEF_FORM_GetOrbitRepresentative(Qmat, Xval)`, `INDEF_FORM_GetOrbit_IsotropicKplane(Qmat,k)`, `INDEF_FORM_GetOrbit_IsotropicKflag(Qmat,k)`.
- CARAT is only an audited auxiliary for positive-definite forms and finite matrix groups. `Aut_grp`, `Isometry`, and `Shortest` require positive-definite form input. `Normalizer`, `Orbit`, `Z_equiv`, and `Is_finite` work with finite matrix groups; verify finiteness first. Use `Orbit -L <n>` when an orbit may be infinite.
- buildings.sage owns Tits buildings for O(2,n) subgroups: isotropic line/plane orbits and incidence. Stored calls/classes: `SubGp_A2t`, `SubGp_GK`, `SubGp_UU2A2t`, `SubGp_UUmA2t(m,N)`, `SubGp_U2U2A2t`, `BigGp`, `Ell(N)`, `building()`, `identify_bc_e()`, `identify_bc_E()`, `incid_rels()`, `line_plane_incid()`, `eichler_equiv()`, `iso_classes_in_E()`.
- PARI/GP, FLINT, Arb, Nemo, and Sage wrappers own exact arithmetic kernels; do not hand-roll arithmetic kernels.
- polymake, Normaliz, LattE, barvinok, 4ti2, and Sage/Oscar wrappers are candidate owners for cones, Hilbert bases, lattice-point enumeration, toric and polyhedral work; audit current docs before implementation.

Repo abstract-method ownership from theory:

- `Variety.blowup(center)` -> Macaulay2 Schubert2 `blowup(i)`.
- `Variety.resolve_singularities()` -> Singular `resbin.lib`.
- `Variety.picard_group()` -> Sage `PicardGroup` or Oscar integer-lattice machinery.
- `Variety.kodaira_dimension()` -> compute `h^0(nK_X)` via Macaulay2 for `n = 1..d+2`, interpolate in Sage with `R.lagrange_polynomial(points)`, return `-∞` if all sections vanish.
- `Variety.hilbert_polynomial()` -> Macaulay2 `hilbertPolynomial`.
- `Variety.hodge_number(p,q)` -> Macaulay2 `dim HH^i(cotangentSheaf(p, X))`.
- `Variety.holomorphic_euler_characteristic()` -> Macaulay2 sheaf cohomology, `χ(O_X) = Σ(-1)^i h^i(O_X)`.
- `Variety.canonical_class()` -> Macaulay2 `canonicalDivisor(X)`.
- `Curve.genus()` and `Curve.arithmetic_genus()` -> Singular `brnoeth.lib: Adj_div` or Macaulay2 `geometricGenus`.
- `Curve.normalization()` and `RationalSextic.normalization()` -> Sage/Singular normalization.
- `RationalSextic.is_nodal()` and `.nodes()` -> Singular `solve.lib` on partial derivatives, then verify nodes.
- `Surface.birational_involution()` -> Sage Enriques surface support where available.
- `Blowup.exceptional_divisor()` -> Macaulay2 Schubert2 `exceptionalDivisor`.
- `CobleSurface.from_singular_sextic()` -> Singular for nodes, Sage for blowup.
- `CobleSurface.coble_lattice()` -> Oscar integer-lattice construction.
- `Divisor.riemann_roch_space_dimension()` -> Singular `BrillNoether` or Macaulay2.
- `Divisor.is_ample()` -> Macaulay2 `isVeryAmple` or Nakai-Moishezon check.
- `Divisor.is_nef()` -> intersection with all relevant curves.
- `Divisor.self_intersection()` and `.intersection(other)` -> Macaulay2 intersection theory.
- `PicardGroup.intersection_matrix()` -> Oscar `gram_matrix`.
- `Lattice.discriminant_group()` -> Oscar `discriminant_group(L)`.
- `Lattice.primitive_embedding()` -> Oscar `primitive_embeddings`.
- `Lattice.automorphism_group()` -> CARAT for definite, Indefinite.jl for indefinite.
- `Lattice.isometry_test()` -> Indefinite.jl `INDEF_FORM_TestEquivalence` for indefinite; Oscar definite methods when applicable.
- `Lattice.orbit_representatives()` -> Indefinite.jl `INDEF_FORM_GetOrbitRepresentative`.
- `Lattice.vinberg_*()` -> Oscar `vinberg_algorithm` or a verified Vinberg backend, not an ad hoc implementation.
- `DoubleCover.total_space()` -> Sage weighted projective space.
- `K3DoubleCover.cover_surface()` and `EnriquesQuotient.k3_cover()` -> Sage K3/Enriques constructors where available.
- `CoherentSheaf.h0/h1/euler_characteristic/rank()` -> Macaulay2 `HH^i`, `chi`, and `rank`.
- `FamilyOfVarieties.specialization()` and `.monodromy()` -> Sage degeneration/monodromy when curves; Picard-Fuchs route for surfaces.

Critical backend limitations:

- Oscar/Hecke `root_lattice(:E,8)` is positive-definite by default. Repo root lattices are negative-definite unless stated. Use `root_lattice(:E,8,-1)` or `rescale(...,-1)`.
- Oscar automorphism group generators, `is_isometric`, root-lattice recognition, shortest vectors, and many short-vector routines require definite input. Use Indefinite.jl for indefinite isometry/orbits.
- Indefinite.jl locally works through Julia `1.6.7` with an isolated `HOME`; user `~/.gap/pkg/JuliaInterface` can break the pinned stack. A subprocess bridge must isolate `HOME`.
- Direct GAP-in-Sage loading of Indefinite.jl internals is not a drop-in route because upstream calls Julia/Oscar bridge helpers.
- The C++ `polyhedral_common` indefinite backend exists but did not build locally because Boost headers were missing; treat it as real but not immediately available here without environment work.

Gap protocol: if a needed method is not listed here, stop implementation and create/update a backend-gap research card with the exact operation, mathematical objects, candidate software, docs checked, and blocker.

Source anchors: `theory/backends/software-capability-map`, `theory/backends/library-integration`, `theory/backends/abstract-to-external-mapping`, `theory/backends/comprehensive-tool-docs`, `theory/backends/oscar-lattices`, `theory/backends/gap-orbits`, `theory/backends/indefinite-jl`, `theory/backends/indefinite-isometry`, `theory/backends/carat`, `theory/backends/buildings`.

Verification: a future implementation card should name the backend call above, list the public repo noun receiving the method, and use status `preferred-backend`, `bridge-needed`, `candidate-backend`, `true-gap`, or `out-of-scope`.
