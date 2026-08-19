# Bilinear Form And Lattice Spec Semantics

Trigger: designing or reviewing lattice/module/category specs, bilinear-form morphisms, discriminant forms, duals, cokernels, Sage category wrappers, or method-owner tables.

Bilinear form semantics to store:

- Define the adjoint map abstractly before matrices: `ad_beta(v) = beta(v, -) in L^*`. No nondegeneracy is required for this definition.
- With basis `e_j` of `L` and dual basis `e_i^*`, `ad_beta(e_j) = sum_i beta(e_j,e_i) e_i^*`. If Gram entries are defined as `G_ij = beta(e_j,e_i)`, then `G` represents `ad_beta`; if using `Gtilde_ij = beta(e_i,e_j)`, the representing matrix is `Gtilde^t`.
- The diagram is `L -> L^*`, `L -> L#`, `L# -> L^*`, `L# -> L_K`, with `ad_beta = lambda o i` and `j = iota o i`. In a nondegenerate finite-free situation, after choosing the `L#` basis via `lambda^{-1}(e_i^*)`, the matrix of `L -> L#` is `G` and the inclusion `L# -> L_K` is `G^{-1}`.
- Do not define `L#` by the matrix `G^{-1}`. `G^{-1}` is only the matrix of the inclusion after the dual-lattice basis is chosen.
- For objects over an `R`-algebra `S`, the form object is not merely an `R`-module with an `R`-bilinear map. It is an `S`-module `L` plus an `S`-bilinear form `b: L tensor_S L -> S` or `beta in Hom_S(Sym^2_S(L), M)`.
- A morphism over `g: S_1 -> S_2` is formulated in the target fiber after base change: an `S_2`-linear `phi: S_2 tensor_{S_1} L_1 -> L_2` with the form square commuting in `S_2`-Mod.
- Triple morphism data are `(f,g,h)` where `g: S_1 -> S_2`, and `f,h` are target-fiber maps `S_2 tensor_{S_1} L_1 -> L_2` and `S_2 tensor_{S_1} M_1 -> M_2`.
- Cokernel of a triple morphism: first form `Q = coker(f_{S_2})` and `N0 = coker(h_{S_2})`; then quotient `N0` by images of cross-terms `beta_2(E * L_2)` with `E = im(f_{S_2})`. The coefficient quotient, not an underlying submodule quotient alone, makes the form descend.
- Recovering the discriminant form is not `S_1=ZZ, S_2=QQ`; use `R=ZZ`, `S_1=S_2=ZZ`, coefficient modules `M_1=ZZ`, `M_2=QQ`, source objects `(L,beta_Z)` and `(L#,beta_Q|_{L#})`, morphism `L -> L#`, and coefficient inclusion `ZZ -> QQ`. Module cokernel is `L#/L = A_L`.

Lattice/spec object store from preserved theory backup:

- Fix the base ring `R := ZZ` for lattice specs until an explicit design says otherwise.
- Core public API should be `Lattice` and `DiscriminantForm`/`DiscriminantGroup`; most other computational work should be backend code.
- `RationalLattice` is the home for `QQ`-valued forms and dual lattices. It should be the one place that promotes to `Lattice` when the Gram matrix is integral.
- `Lattice` is the integral subtype with `ZZ`-valued symmetric bilinear form. It maintains symbolic generators and an internal Sage `IntegralLattice` for delegation/wrapping.
- Almost all named constructors belong on `Lattice`, even when they may return a `RationalLattice`; construction from Gram matrices belongs in `RationalLattice` with promotion.
- `DiscriminantGroup/Form` represents the torsion quadratic/bilinear module `L#/L`; construct from a lattice, Sage abelian group plus quadratic Gram matrix, or invariant factors plus form matrix.
- `LatticeElement` semantics: `v*w`, `v.b(w)`, `v.bilinear_product_with(w)`, `v^2`, and `v.q()` all refer to the parent bilinear/quadratic form. `v.to_vector()` and `element_from(vector)` convert between symbolic elements and coordinates.
- Morphisms should be constructed through Hom spaces, not ad hoc matrices. Example constructors: `L1.Hom(L2).element_from_dict(...)`, `Lattice.Hom(L1,L2).element_from_matrix(...)`. Isometry testing belongs in homspace containment/validation.
- `LatticeMorphism` kernel/image/cokernel work must respect that lattices are not closed under every morphism operation. Promote to lattice only when free, integral, and nondegenerate; otherwise return torsion/discriminant-like or degenerate bilinear-module objects.
- Perps are defined with respect to inclusions/subobjects. External direct sums and spans are different: `e.span() + f.span()` is an orthogonal external direct sum, not necessarily `L.span([e,f])`.
- Isotropic reduction is `e.perp()/e` for a primitive isotropic vector/subobject; it may promote back to a lattice even when `e.perp()` itself is degenerate.

Orthogonal group/spec method store:

- Public orthogonal group action convention is left action on column vectors: `G.act(v) = G * v`, with membership equation `G^T Q G = Q`.
- Sage/Dutour-Sikiric raw backend matrices may be row-action; convert by transpose before exposing in the public API. Do not mix `G Q G^T == Q` into public membership checks.
- `Lattice.orthogonal_group()` returns a lazy `LatticeOrthogonalGroup`; `gens()` computes generators on first call.
- Stabilizer method ownership: `stabilizer_of_vector(v)`, `stabilizer_of_isotropic_line(v)`, `stabilizer_of_isotropic_plane(v,w)`, and `stabilizer_of_isotropic_flag(ordered_basis)` return `LatticeOrthogonalSubgroup` with membership predicates by column action.
- Isotropic ambient orbit methods: `isotropic_line_orbits()`, `isotropic_plane_orbits()`, and `isotropic_flag_orbits(k)` wrap `indefinite_form_isotropic_k_plane`/`indefinite_form_isotropic_k_flag` and return lattice elements/bases.
- Invariant/coinvariant sublattices for an involution use the `ZZ` kernel of `iota - eigenvalue*I` and restrict the Gram matrix to that kernel basis.
- `centralizer_of_involution(iota)` is membership `M*iota = iota*M`. Definite generators may use GAP centralizer after sign-adjusting negative definite forms to positive definite. Indefinite generators require Oscar `integer_lattice_with_isometry` plus `image_centralizer_in_Oq` data.
- `_acts_trivially_on_discriminant(lattice,M)` checks all dual-basis vectors from rows of `Q^{-1}`: `M*x - x in L`.
- `kernel_of_discriminant_action()` is the stable orthogonal subgroup and should merge structured orbit metadata with a trivial discriminant subgroup.

Conventions to enforce:

- Root lattices are negative definite in repo mathematics unless explicitly stated. Oscar/Hecke default root lattices are positive definite; flip sign at backend boundary.
- Hyperbolic lattices have signature `(1,r-1)`, and the hyperbolic plane `U` has Gram `[[0,1],[1,0]]`.
- `O^*(L)`/`~O(L)` is the stable orthogonal group, kernel of `O(L)->O(D(L))`.
- `SO(L)` is determinant `1`; `SO^+(L)=O^+(L) cap SO(L)`; `~SO^+(L)=O^+(L) cap O^*(L) cap SO(L)`.

Source anchors: `theory/foundations/bilinear-forms-duals-morphisms`, `.agents/theory/spec-backups/lattices_written_spec_backup.py`, `.agents/theory/spec-backups/lattice_methods_recovered_from_codex_transcript_2026_04_13.sage`, and visible `theory/foundations/reflective-two-elementary-lattices.md`.

Verification: a future spec should be able to name the object fiber, base-change functor, coefficient module, action convention, and return object class before adding a method row or implementation.
