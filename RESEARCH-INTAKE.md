# Research Intake

Leads for research code whose capabilities belong in the preamble.

Each entry names existing research code that provides mathematical capability not yet owned by the preamble.
The preamble absorbs each capability through its owned category, object, morphism, and functor structure, with maintained computation behind a private adapter.
Do not import the research code directly and do not reimplement its algorithm locally.
Use the intake to select the correct owner, trace the required construction, and link the resulting TODO item and complaint where applicable.

Add a lead with source location, mathematical capability, intended preamble owner, and current status.
Remove a lead when the preamble owns the capability and specimens prove it, with evidence in the delivery commit.

## Reference implementations

Where to look first for existing algorithms before writing new code. Check these before claiming a computation has no maintained implementation.

| Domain | Reference implementation | What it provides |
| --- | --- | --- |
| Symbolic summation, recurrences, D-finite / holonomic, creative telescoping, OGF/EGF closure | https://caa.risc.jku.at/software — RISC Computer Algebra (ore_algebra, HolonomicFunctions, etc.) | Ore algebras, closure for D-finite, creative telescoping, recurrence solving, OGF/EGF translation, L-functions as D-finite objects; adapter candidates for generatingfunctionology and `Periods` |
| Constructive algebraic topology — effective homology, loop spaces, fibrations, Whitehead/Postnikov towers, homotopy groups | https://www-fourier.univ-grenoble-alpes.fr/~sergerar/Kenzo/ — Kenzo program (EAT/Kenzo); file-list 36 modules: effective-homology, chain-complexes, simplicial-sets/groups, fibrations, loop-spaces, classifying-spaces, k-pi-n, serre, whitehead, etc. — demo shows H5(Ω^3 Moore(Z/2,4)), H5(ΩΩ(S^3∪_2 D^3)), π7(P∞R/P2R) | Effective homology (reductions/strong equivalences, basic/easy perturbation lemmas, twisted Eilenberg-Zilber), bar/cobar, Kan loop group / classifying space, fibrations as twisted cartesian products, Eilenberg-MacLane K(π,n), Serre spectral sequence, discrete vector fields for EZ/EML, Whitehead/Postnikov tower for π_n of simply connected simplicial sets; adapter candidate for homology of iterated loop spaces and higher homotopy |
| Filtered complexes + Serre/Eilenberg-Moore sseqs — test fixtures + algorithms | https://www-fourier.univ-grenoble-alpes.fr/~sergerar/Papers/Ana-JSC.pdf — Ana Romero et al. JSC (effective homology + spectral sequences) — §3-7 code + didactic/advanced examples | Theorem 15 (filtered C with effective homology, homotopies order ≤t ⇒ E_r(C)≅E_r(HC) for r>t), class Filtered-Complex with flin, functions build-FltrChcm/change-chcm-to-FltrChcm/fltrd-basis/fltr-chcm-dffr-mtrx, sseq functions print-spct-sqn-cmpns/spct-sqn-basis-dvs/spct-sqn-dffr/spct-sqn-cnvg-level, fixtures: S^2×_τ K(Z,1) (τ(s2)=[1] Hopf S^3, τ(s2)=[2] P^3R) with effective S^2⊗_t S^1 and twpr-flin/tnpr-flin filtrations, S^2×_τ K(Z/2,1) (effective bypass), Postnikov tower X4 (X2=K(Z/2,2), k3∈H^4(X2;Z/2), X3=X2×_{k3}K(Z,3), k4∈H^5(X3;Z/2), X4=X3×_{k4}K(Z/2,4) with E_2^{0,4}=Z/2, E_2^{5,0}=Z/4, E_2^{6,0}=Z/2⊕Z/2, d5^{5,0}≠0) and loop-space EM sseq for ΩS^3 vs ΩS^3∪_2 D^3 (Fig.1 E_∞^{p,q} q-p≤8, Fig.2 same); use for specimen oracles and perturbation-order checks |

## Leads

| Lead | Source | Capability | Intended owner | Status |
| --- | --- | --- | --- | --- |
| *Example: toric divisor cohomology* | `computations/...` | *What mathematics it computes* | `categories/schemes/...` | Proposed |
| CAP monodromy — rigorous PF transport | https://github.com/taklab-org/CAP_finding_monodromy | Rigorous monodromy of regular-singular Pfaffian system via series enclosure + validated ODE transport | `categories/schemes/monodromy.py` / flat connections / D-modules; `categories/functors/local_system.py` | Proposed — see intake report below |
| Families via f.as_family + periods / PF | User note 2026-09-15 | Scheme morphism as family; period `w(z)=∫_{γ_z}Ω_z` and its Picard-Fuchs equation `PF(w)` | `categories/schemes/families.py` via `Hom(Sch/C)` + `categories/schemes/periods.py` / Gauss-Manin | Proposed — see note below |
| Generatingfunctionology (Wilf Ch.1-2) | User note 2026-09-15 | Symbolic recurrences, exact solutions, OGF/EGF, L-functions / zeta | `categories/generating_functions/` + `categories/rings/formal_power_series.py` / `D-Mod` | Proposed — see note below |
| Monodromy groups/reps + π1/H1 + CW + graded | User note 2026-09-15 | Semantic `π1(X,x)`, `H1^sing`, monodromy groups/reps; CW complexes with sphere homotopy DB; `ZZ^n`-graded complexes / spectral sequences | `categories/topology/` / `categories/homotopy/` + `categories/graded/` | Proposed — see note below |
| Periods (Lairez) — creative telescoping | https://github.com/lairez/periods | Periods of rational integrals: Picard-Fuchs operators via Griffiths-Dwork / Rham-Koszul | `categories/schemes/periods.py` / `categories/Dmodules/` + `categories/rings/completions.py` | Proposed — see intake below |
| p-curvature | User note 2026-09-15 | `p`-curvature of a connection in characteristic `p` (`ψ_p: T_{X/S} → End(E)`) | `categories/connections/p_curvature.py` + `categories/characteristic_p/` | Proposed — see note below |
| Zeta of varieties / Weil conjectures (concrete cases) | User note 2026-09-15 | `Z(X/F_q,T)` for `X/F_q`; closed forms via explicit `|X(F_{q^r})|` for `A^n, P^n, Gr(k,n)`, some curves; verify Weil (rationality, functional equation, RH) | `categories/zeta/zeta.py` + `categories/varieties/point_counts.py` | Proposed — see note below |
| Lefschetz trace operationalized (Frob) | User note 2026-09-15 | Operationalize `N_r = Σ (-1)^i Tr(Frob^r \| H^i_{c,ét}(Q_ℓ))` — compute `Tr(Frob)` on étale cohomology | `categories/etale/trace_formula.py` + `categories/etale/frobenius.py` | Proposed — see note below |
| HH(A) — Hochschild homology | User note 2026-09-15 | Hochschild homology `HH_*(A)` for (dg) algebras `A`; complex `C(A)`, `HH = H_*(C)`, HKR, etc. | `categories/homology/hochschild.py` + `categories/algebras/dg_algebras.py` | Proposed — see note below |
| Gauss-Manin + six functors + R f_* | User note 2026-09-15 | Gauss-Manin connection, six-functor formalism for sheaves, derived functors (esp. `R f_*`) | `categories/functors/gauss_manifold.py` + `categories/sheaves/six_functors.py` + `categories/derived/` | Proposed — see note below |
| Étale / ℓ-adic and Galois cohomology via sites | User note 2026-09-15 | Honest `Q_ℓ`, `H^i_ét`, `H^i(Gal,-)` as specialization of site cohomology; Grothendieck topologies, sites, sieves, covering families | `categories/topology/sites.py` + `categories/etale/` + `categories/galois/` | Proposed — see note below |
| Derived Hom / tensor — Ext, Tor, D(R-Mod) | User note 2026-09-15 | `RHom`, `Ext^n = R^n Hom`, `⊗^L`, `Tor_n = L_n(⊗)` in `D(R-Mod)`; derived tensor products `A⊗^L_R B` | `categories/derived/derived_category.py` + `categories/homological/ext_tor.py` / `categories/derived/tensor_product.py` | Proposed — see note below |
| Constructive topology — Kenzo effective homology | https://www-fourier.univ-grenoble-alpes.fr/~sergerar/Kenzo/kenzo-demo.html | Constructive homology of iterated loop spaces and higher homotopy: effective homology for C_*(Ω^n X), fibrations, Whitehead/Postnikov towers, H_*(K(π,n)), π_n(X) with k-invariants | `categories/topology/simplicial_sets.py` + `categories/topology/effective_homology.py` + `categories/homotopy/whitehead_tower.py` + `categories/algebras/bar_cobar.py` | Proposed — see intake below |
| Eilenberg-Moore sseq — effective | User note 2026-09-15 + Kenzo | Operationalized Eilenberg-Moore spectral sequence for fibrations/pullbacks via effective homology: E_2 = Tor^{H_*(ΩB)} / Cotor^{H_*(B)} ⇒ H_*(F ×_B E) with constructive differentials and convergence, not table lookup | `categories/homotopy/eilenberg_moore.py` + `categories/topology/effective_homology.py` + `categories/derived/tensor_product.py` (Tor) + `categories/algebras/bar_cobar.py` | Proposed — see note below |
| Hypercohomology + Čech — effective | User note 2026-09-15 | Operationalized hypercohomology RΓ(X, F^•) and Čech cohomology Č^•(U, F) via effective resolutions: Čech nerve, derived global sections, Leray/Čech-to-derived sseq, with constructive EC differentials and acyclic-cover test | `categories/sheaves/hypercohomology.py` + `categories/sheaves/cech.py` + `categories/topology/effective_homology.py` + `categories/derived/derived_category.py` | Proposed — see note below |
| Filtered complexes + HF/Frolicher/Grothendieck sseqs — effective + degeneration | User note 2026-09-15 | Filtered complexes (FiltCh), standard filtrations (stupid/bête, Hodge, conjugate, weight), spectral sequences from filtered complexes: Hodge-to-de Rham/Frölicher, Grothendieck composite-functor (Leray, local-to-global Ext), with operational pages, differentials, and computable degeneration via stabilization/zero-grading tests | `categories/derived/filtered_complexes.py` + `categories/hodge/hodge_filtration.py` + `categories/homotopy/spectral_sequences.py` + `categories/schemes/hodge_frolicher.py` | Proposed — see note below |
| Interactive sseq visualizer — attached to sseq objects | User note 2026-09-15 | Interactive spectral sequence visualizer attached to sseq objects: per-page grid, bigraded entries, toggleable differentials, page flipping, tooltips with mathematical metadata, linked to effective EC data | `categories/homotopy/spectral_sequences.py` (SpectralSequence.visualize) + `notebooks/visualizer` or `src/dzack_research/preamble/visualization/sseq.py` delegating to `sseq` object | Proposed — see note below |
| Concrete BG models + EG→BG, simplicial objects in C, configuration spaces | User note 2026-09-15 | Concrete geometric models for classifying spaces: RP^∞, CP^∞, lens L_p^∞, Gr_n(C^∞), Gr_n(R^∞), BSO_n, BSp_n, BGL_n, BSpin_n, BString_n, HP^∞, HH P^∞, BF_n, Bπ_1(X), B(G×H), BG for braid B_n and pure P_n, plus EG, B(G×H), associated bundles; honest simplicial objects sC = Fun(Δ^{op},C) and simplicial sets; ordered/unordered configuration spaces with/without collisions | `categories/topology/classifying_spaces.py` + `categories/topology/simplicial_objects.py` + `categories/topology/configuration_spaces.py` + `categories/topology/simplicial_sets.py` | Proposed — see note below |
| Character varieties + Betti moduli, GIT quotients, Hilbert schemes, holonomy | User note 2026-09-15 | Character varieties Hom(π_1,G)//G as Betti moduli M_B, general GIT quotients X//G and X^s//G, Hilbert schemes Hilb^n(X), Hilb^P(X), and honest holonomy groups Hol(∇) as subgroups of GL via parallel transport | `categories/moduli/character_varieties.py` + `categories/moduli/git_quotients.py` + `categories/moduli/hilbert_schemes.py` + `categories/connections/holonomy.py` | Proposed — see note below |
| Group (co)homology, surface groups, algebraic/Lie/group schemes, NAH, RR/index, Poincaré OGF, Chern calculus, 4-manifold H^*/Freedman, spinnability, Arf/KS/Â, equivariant, Hodge ops, cobordism/TQFT, normal bundles | User note 2026-09-15 | Group cohomology H^*(G,M), Tate \hat H^*, transfers/traces/norms/induction/restriction and co; surface groups π_1Σ_g as FP groups; algebraic groups/Lie/group schemes; Higgs/local systems/flatness, harmonic metrics, semisimplicity, non-abelian Hodge; operational RR and index theorems (Atiyah-Singer, Gauss-Bonnet, HRR, CGB); Poincaré series OGF → Betti; Chern classes/c_1/ch/Todd calculus; H^*(X;ZZ)/tors as graded ring for 4-manifolds + Freedman lattice check; spinnability via Rohlin/Kervaire-Milnor/Freedman-Kirby and invariants Arf, KS, Â; differential operators symbol/index; G-equivariant cohomology/K; exterior d, Hodge laplacian, ⋆; cobordism rings + cobordant detection; cobordism categories TQFT functors; normal bundles of immersions/embeddings | `categories/group/cohomology.py` + `categories/group/surface_groups.py` + `categories/group/group_schemes.py` + `categories/higgs/nonabelian_hodge.py` + `categories/index_theory/` + `categories/characteristic_classes/chern.py` + `categories/topology/four_manifolds.py` + `categories/differential_operators/` + `categories/equivariant/` + `categories/cobordism/` | Proposed — see note below |
| Almost complex structures, integrability, Nijenhuis, curvature tensors | User note 2026-09-15 | Almost complex J with J^2=-id, integrability N_J=0 via Newlander-Nirenberg, Kähler needs; Nijenhuis tensor N_J, Ricci/Gaussian/scalar/sectional/Riemann curvature tensors, Levi-Civita | `categories/geometry/almost_complex.py` + `categories/geometry/curvature.py` + `categories/geometry/complex_manifolds.py` | Proposed — see note below |
| Curvature refinements — Ricci/Gauss/scalar, Nijenhuis | User note 2026-09-15 | Almost complex J, integral structure N_J=0, Nijenhuis N_J(X,Y)=[JX,JY]-J[JX,Y]-J[X,JY]-[X,Y], Kähler G-structure; Ricci, Gaussian, scalar, sectional, Riemann R, Levi-Civita ∇, curvature forms | `categories/geometry/complex_structures.py` + `categories/geometry/curvature.py` | Proposed — see note below |
| Flatness, moduli of flat connections, curvature, Levi-Civita, gauge group, Hermitian, lattice Hermitian form, covariant derivatives, gradient flow, Hamiltonian flows | User note 2026-09-15 | Flatness F_∇=0, moduli M_flat = FlatConn//G, curvature F_∇=dA+A∧A, Levi-Civita ∇^{LC}, gauge group G=Γ(Aut P), Hermitian modules/vector spaces, Hermitian metrics h, lattice Hermitian form on L⊗_ZZ C vs bilinear, covariant derivatives ∇, gradient flow ẋ=-∇f, Hamiltonian H and flow φ_H^t via ω | `categories/connections/` + `categories/geometry/hermitian.py` + `categories/dynamics/hamiltonian.py` + `categories/moduli/flat_connections.py` | Proposed — see note below |
| Teichmüller space and Weil-Petersson metric | User note 2026-09-15 | Teichmüller T_g, moduli M_g = T_g/MCG, WP metric g_{WP} via L^2 pairing of quadratic differentials, Kähler form ω_{WP}, curvature, pants decompositions, Fenchel-Nielsen | `categories/teichmuller/teichmuller_space.py` + `categories/teichmuller/weil_petersson.py` | Proposed — see note below |
| Slopes of vector bundles | User note 2026-09-15 | Slope μ(E)=deg(E)/rank(E), semistability μ(F)≤μ(E), stability μ(F)<μ(E), polystability E≅⊕E_i stable same μ (⇔ E≅gr_{JH} / Hermite–Einstein), Harder-Narasimhan and Jordan–Hölder filtrations | `categories/vector_bundles/slope.py` + `categories/vector_bundles/stability.py` + `categories/moduli/higgs.py` | Proposed — see note below |

## Intake report: https://github.com/taklab-org/CAP_finding_monodromy — 2026-09-15

Hard codes are data, not method. Generalize data and you get 4 reusable rigorous capabilities:

**1. Rigorous singular locus — hard code: polynomial**
* Hard: `S = {4455...} = 0`, line `2(x-x0)+(y-y0)=0`
* General: For any flat connection `∇ = d - Σ A_i dz_i` with rational `A_i`, enclose `Sing(∇) ∩ L` for any generic line `L` via `kv::allsol` interval Newton. Input: rational equations. Output: disjoint interval boxes containing each intersection point. Method is general.

**2. Rigorous fundamental matrix at base point — hard code: N=4, N_trunc=41, lam0=2^-10, formulas for a_lm**
* Hard: `phi1..4` for this GKZ with `a_lm=(2l+4m)!/(l+m)!l!(m!)^3`
* General: For any regular-singular Pfaffian system `dΦ = Ω Φ` with series `Σ a_{m} z^{m+regular exp} (log z)^k`, enclose `Φ(b0)` by truncated sum + majorant bound.
  * Needs: coefficient growth estimate `|a_m| ≤ C β^m`, truncation `N`, radius `|b0|<1/β`. Theorems 3.4-3.7 are just `β_N,gamma_N,delta_i` for this `a_lm`. Same proof gives `β,delta(N)` for any hypergeometric/GKZ ratio.
  * Operation: `fundamental_matrix(∇, b0, N) -> interval matrix` with guaranteed `|error| < delta`.

**3. Rigorous connection matrices — hard code: `matA,matB` as rational functions of x,y**
* Hard: K3 family `h=1+20x+9y`, `A,B` built from `a..em,B0..C3`
* General: Any integrable `Ω = A(x)dx + B(x)dy`, `A,B ∈ Mat_n( C(x))` with simple poles on `S`. Input: rational matrix functions. `variable_coefficients.hpp` is just the evaluator `Ω(x,y)`. Replace evaluator and code runs.

**4. Rigorous analytic continuation / monodromy — hard code: 6 circles with centers `cx,cy` and `r`, order 15, DD**
* Hard: `x=cx+r e^{±iπt}, y=cy-2r e^{±iπt}`, 3 segments per `Σ_i`
* General: For any path `γ:[0,1]→ B` piecewise smooth, validated ODE `dΦ/dt = (dx/dt A + dy/dt B) Φ`.
  * Integrator `kv::odelong_maffine` is fully general: Taylor order `p`, interval/`dd`/`interval<dd>`, affine arithmetic remainder. Hard codes are `p=15` and `dd`.
  * Operation: `transport(∇, γ, Φ0) -> interval matrix Φ1` with `Φ1 ∋ actual analytic continuation`. Iterate over `γ_{i,1}*...*γ_{i,k}` to get `M_i = Φ0^{-1} Φ1`.
  * Parallel over 4 columns via OpenMP is general rank `n`.

**General object:**
```
Input:  (B = C^k \ S, rank n, Ω ∈ Mat_n(C(B)) integrable, regular singular, base b0, presentation of Φ(b0))
Functor: LocalSystem(∇): π1(B,b0) → GL_n(C)
Method:  Φ(b0) via 2 + transport via 4
Output: interval M_i with width < 0.5 if M_i ∈ GL_n(Z), certifies integer monodromy
```

What does not generalize automatically: the closed-form `delta_i` proof for 2, and the choice of `γ` that generates `π1`. The rigorous transport 4 does.

## Fundamental semantic language required — verbatim — 2026-09-15

You are right. Reformulation in preamble semantic language — only categories, functors, and their objects/morphisms — not data:

**Base language (must exist to name anything)**
* `Sets`, `NN` — `dim = 2` is an element `2 : NN`, not an object
* `CommRings`, `CommAlgebras(C)` — `C`, `C[z1..zk]`, `C(X)`
* `Modules(R)` — free module `E = O_U^n` is object with axiom `Free` of rank `n: NN`; `n` is not a category
* `Schemes/C`, `Smooth(C)` — `X = A^k_C` is object of `Schemes/C`; `S ⊂ X` is object of `Divisors(X)`, not a primitive; `U = X \ S` via open immersion `j: U ↪ X`

**Sheaf language**
* `Sh(X_{Zar})`, `QCoh(X)`, `O_X-Mod` — quasi-coherent sheaves; `Ω^1_X` is object of `QCoh`
* `AnSpaces`, analytification functor `(-)^{an}: Sch/C → An` — `X^{an}`, `U^{an}`
* `Sh(X^{an})`, `O^{an}-Mod`, `LocSys(U^{an})` — locally constant `C`-sheaves; object of `LocSys` is the local system, not its rank

**Connection language**
* `Conn(X) = (E, ∇)` where `E : QCoh(X)`, `∇: E → E ⊗ Ω^1_X` morphism of sheaves
* `FlatConn(X) ⊂ Conn(X)` — subcategory defined by `∇^2 = 0 : E → E ⊗ Ω^2_X` (flatness equation)
* `TrivFlatConn(U)` — Pfaffian system is not fundamental; it is trivialization `E ≅ O_U^n` of object of `FlatConn(U)`. Matrix `Ω = Σ A_i dz_i` is representation of `∇` in that trivialization, not a new notion. General integral form `Ω ∈ Mat_n( Ω^1(log S))` is object of `Ω^1_X(log S)`.

**D-module language**
* `D_X-Mod`, its full subcategory `D^{rh}_X(S)` — regular holonomic `D`-modules with singularities along `S`
* Functor `DR: D_X-Mod → Sh(X^{an})` and `Sol = Hom_{D}( -, O^{an}) : D_X-Mod^{op} → Sh(X^{an})` — solution functor
* Riemann-Hilbert functor `RH: D^{rh}_X(S) → Perv_S(X^{an})` — equivalence. Its restriction to `FlatConn` is `RH: FlatConn^{rs}(X,S) ≃ LocSys(U^{an})`. This is the functor that turns `∇` into monodromy. Source = `D^{rh}`, target = `LocSys`/`Perv`.

**Homotopy / monodromy language**
* `π_1: An_* → Groups` and fundamental groupoid `Π_1(U^{an}) : Cat` — source of local system as functor `Π_1 → Vect_C`
* Equivalence `LocSys(U^{an}) ≃ Rep(π_1(U^{an},b0)) ≃ Fun(Π_1, Vect_C)` — monodromy representation `ρ : π_1 → GL_n(C)` is image of `Sol(M)` under this. Base point `b0 : Spec C → U` is morphism, not an object.
* Path `γ: [0,1] → U^{an}` is morphism in `Π_1`; transport `T_γ` is image of `γ` under `ρ`.

**What is not fundamental**
* `k=2`, `n=4`, `N_trunc=41`, `b0=2^-10`, `S` polynomial, `A_i` rational entries — all are elements/morphisms in the above categories
* `δ(N), β_N` — analysis of series in `O^{an}_{b0}`

Capabilities state as: choose `∇ : FlatConn^{rs}(X,S)`, apply `Sol = RH( D(∇)) : LocSys(U^{an})`, evaluate at `b0`, transport along `γ`, read `ρ([γ])`. Code replaces last two steps by validated enclosure in `IR`-lift.

## Desired capability: families as scheme morphisms — note 2026-09-15

Formulate a scheme morphism `f: X → S` as a family via an interface `f.as_family(...)`.

`f.as_family` must require enough data to be well-defined — it is not a bare cast. Required data includes at least the base scheme `S`, the structure morphism `f`, and the properties that make `f` a family: flatness, and where needed properness / smoothness / finite presentation over `S`. Additional framing (projectivity, chosen relatively ample line bundle, marking of a section) is supplied when the construction needs it, not by default. Without this data the object is not a family; calling `as_family` without it must fail.

Families must support period functions for continuous families of cycles and forms:

* Continuous family of cycles `γ_z` — horizontal family of homology classes `γ : S^{an} → R^k f^{an}_* C` (section of the local system `R^k f_* C` / Betti local system). `γ_z ∈ H_k(X_z, C)` varies locally constantly.
* Continuous family of relative forms `Ω_z` — section `Ω : S → f_* Ω^k_{X/S}` (or relative de Rham sheaf `H^k_{dR}(X/S)`).
* Period function `w(z) = ∫_{γ_z} Ω_z : S^{an} → C` — pairing of the above. For algebraic families `w` is holomorphic on `U = S \ discriminant` and satisfies a Picard-Fuchs equation.

Required operation: `w.Picard_Fuchs()` / `PF(w)` — the regular-singular linear differential equation (Picard-Fuchs equation) satisfied by `w(z)`, as an object of `D_S-Mod` (or as `∇_{GM}` flat connection / Pfaffian system on the Hodge bundle `H^k_{dR}(X/S)`). Construction is via the Gauss-Manin connection `∇_{GM}: H^k_{dR}(X/S) → H^k_{dR}(X/S) ⊗ Ω^1_S`. The family must expose `H^k_{dR}(X/S)`, `∇_{GM}`, its regular singularities, and its monodromy local system, so that `PF(w)` is the annihilator of `w` in `D_S`. This connects families to the monodromy intake above: `ρ` of `∇_{GM}` is the monodromy of periods.

Intended owners: `categories/schemes/families.py` (`f.as_family` constructor, `Hom(Sch/C)`), `categories/schemes/periods.py` (period pairing, Gauss-Manin), `categories/functors/gauss_manifold.py` / `D_S-Mod`. Not a free function `PicardFuchs(...)`.

## Desired capability: generatingfunctionology (Wilf Ch.1-2) — note 2026-09-15

Provide basic generatingfunctionology semantic interfaces, at least Wilf *generatingfunctionology* Chapters 1-2.

Required: formulate recurrence relations symbolically and solve them exactly in known cases, and produce ordinary generating functions (OGFs), exponential generating functions (EGFs), and associated L-functions or zeta functions.

Recurrence relation is not a Python `def` with a loop — it is an object `Rec(R, a(n), relation)` in a category of sequences: `a : NN → R` with defining relation ` Σ_{i=0}^d c_i(n) a(n+i) = b(n)` (linear with polynomial coefficients; constant coefficients as special case) plus initial data `a(0)..a(d-1)`. Interface lives on sequences/recurrences, not as a free solver function. Exact solving means when the recurrence lies in a known solvable class (e.g. C-finite / constant coefficients, P-recursive / D-finite with closed hypergeometric form, rational generating function), return closed form for `a(n)` and certified equality, not a numeric guess. No invented `solve_recurrence` that handles only numerics.

Production of OGF / EGF is a functor:

* `OGF: Seq(R) → R[[x]]`, `a(n) ↦ A(x)= Σ_{n≥0} a(n) x^n` — formal power series as object of `R[[x]]`
* `EGF: Seq(R) → R[[x]]`, `a(n) ↦ Â(x)= Σ_{n≥0} a(n) x^n / n!`
* Both are objects of `FormalPowerSeries(R)` with correct parent (radius, valuation, coefficient ring). Converting between them is not string manipulation.

Associated L-functions / zeta functions: for `a(n)` (or arithmetic function) produce Dirichlet series `L(s,a)= Σ_{n≥1} a(n) n^{-s}` as formal Dirichlet series object, and when the sequence comes from counting (e.g. `a(n)=#{points}`) its zeta/Hasse-Weil incarnation. These are objects of a category of Dirichlet series / Euler products, with Euler factor, functional equation, and convergence data retained, not a bare complex function. Construction is `L = Dirichlet(OGF/EGF)(s)` with preservation of base ring and abscissa.

These must be integrated closely with formal power series rings and other I-adic completions. OGF/EGF are not a separate `GeneratingFunctions` hierarchy — they are the `(x)`-adic completion `R[[x]] = lim← R[x]/(x^n)` (and more generally `Î = lim← R/I^n` for any ideal `I`). The same I-adic completion construction that gives `C[[t]]`, `Z_p`, `m-adic` completions and the period rings must own `R[[x]]`, its universal property, its ideal of definition, and its functorial `completion` maps. A recurrence's OGF is then `A(x)` in that completed ring, its truncated `R[x]/(x^N)` images are finite stages of the inverse system, and operations between OGFs (Cauchy product, Hadamard product, composition) use the completed ring's operations, not a second generating-function class. D-finite closure (Wilf Ch.2), P-recursive ⇔ D-finite equivalence, and transforms `Rec → R[[x]] → Dirichlet` all compose through this one completion/coefficient owner. Do not build a parallel `PowerSeriesForGF` that duplicates `R[[x]]`.

Intended owners: `categories/generating_functions/recurrences.py` (recurrence objects, `RecurrenceCategory`), `categories/rings/formal_power_series.py` (`FormalPowerSeries`, `OGF`, `EGF` functors) which delegates to the shared I-adic completion owner `categories/rings/completions.py` / `categories/completions.py`, `categories/rings/dirichlet_series.py` (`DirichletSeries`, `LFunction`, `Zeta`), and their `D-Mod` / `C-finite` solvers behind private adapters (e.g. `ore_algebra`, `sage.combinat`). No free `ogf(...)` at top level — `a.ogf()`, `a.egf()`, `a.dirichlet_series()`, `rec.solution().closed_form()` on the owning objects.

Reference: H. Wilf, *generatingfunctionology*, Ch.1 (ordinary/enumerative) and Ch.2 (exponential) — symbolic recurrence → generating function dictionary, rational / algebraic / D-finite closure.

## Desired capability: monodromy groups/representations + π1/H1 + CW + graded — note 2026-09-15

Want a semantic interface for monodromy groups and monodromy representations, computable in some cases.

This requires a well-established `π_1(X, x)` interface as a functor `π_1: An_* → Groups` (and `Π_1: An → Cat` for the groupoid), not an ad-hoc method returning a string. Monodromy group is the image `im(ρ) ≤ GL_n(C)` of the monodromy representation `ρ: π_1(U^{an}, b0) → GL_n(C)` from the intake above; monodromy representation is the functor `ρ` itself (object of `Rep(π_1)` / `LocSys`). Interface must be `∇.monodromy_group()`, `∇.monodromy_representation(b0)`, `local_system.monodromy()`, on the owning connection/local-system objects — computable via rigorous transport when `∇` is regular-singular and `π_1` has known generators, otherwise retained as formal object with known type.

Requires `π_1(X, x)` and `H_1^{sing}(X, ZZ)` computable for a collection of concrete varieties (at least: `A^1 \ {0..n}`, `P^1 \ {pts}`, complements of discriminants, punctured planes, tori `G_m^k`, elliptic curves, abelians, configuration spaces). Computation routes through topology, not scheme code: analytification `X ↦ X^{an}` then singular/simplicial.

Needs a good CW complex interface: CW complex is object `K = (K^0 ⊂ K^1 ⊂ …)` with skeleta, cells `e^n_α`, and attaching maps `φ_α: S^{n-1} → K^{n-1}` as morphisms of spaces. Gluing is the colimit `K^n = K^{n-1} ∪_{∐ φ_α} ∐ D^n_α` in `Top`. Interface must construct `K` cell-by-cell, expose its cellular chain complex `C_*(K)`, and compute `π_1(K,x)` via van Kampen from the 2-skeleton and `H_*(K)` from `C_*`. No bare list of cells without attaching data.

Needs a static database of all known homotopy groups of spheres `π_{n+k}(S^n)` (stable and unstable ranges as tabled — e.g. Toda, Mimura, etc.) and, when possible, explicit named generators and relations (e.g. `η: S^3 → S^2` Hopf, `η^2`, `ν`, `σ`, Whitehead products) as elements with certified relation `2η = 0` after suspension, etc. This DB supplies the attaching data: a map `S^{n-1} → K^{n-1}` that factors through a sphere can be named as `a·η` etc. Without it CW gluing cannot be specified — a cell attached by `2·id: S^1 → S^1` is the datum for `RP^2`.

Needs a good interface for `ZZ^n`-graded modules: category `GrMod_{ZZ^n}(R)` with `ZZ^n`-graded objects `M = ⊕_{d∈ZZ^n} M_d`, morphisms preserving degree, shifts `M(d)`. From this: complexes `Ch(GrMod)` (single grading + homological degree), double complexes `Ch(Ch(Gr))` with bidegree `(p,q)`, total complex, filtrations, and spectral sequences as objects `E_r^{p,q}` with differentials `d_r: E_r^{p,q} → E_r^{p+r, q-r+1}` and convergence data `E_∞ ⇒ H^*(Tot)`. Support at least Serre spectral sequence (fibration), Atiyah-Hirzebruch, Leray-Serre, and in some easy cases compute them: when `E_2` is known from `H_*(base) ⊗ H_*(fiber)` and differentials are forced by degree / known `k-invariants` / known `π_*(S^n)`, return `E_3, E_∞` and the associated graded of `H^*`. This is computable when the `ZZ^n`-graded module is finite and the differential is sparse.

In some easy cases the whole pipeline must compute: `X` concrete variety → `K = CW(X^{an})` via known decomposition → `C_*(K)` → `π_1(K)`, `H_1(K)`; plus `E_2` from CW cohomology + sphere DB → Serre → `π_*(X)` or `H^*(X)` in range. All via owned categories, not via ad-hoc Python lists of cells.

Intended owners: `categories/topology/cw_complexes.py` (`CWComplex`, `Cell`, `AttachingMap` in `Top`), `categories/topology/homotopy_groups.py` (`HomotopyGroupsDB` with `π_{n+k}(S^n)`, generators `Hopf`, `Whitehead`), `categories/topology/fundamental_group.py` (`π_1`, `H_1 = abelianization`), `categories/graded/graded_modules.py` (`ZZ^n-GrMod`, `GrComplex`, `DoubleComplex`), `categories/graded/spectral_sequences.py` (`SpectralSequence`, `SerreSS`) with unstable support. Monodromy ties back to `categories/functors/local_system.py` and `categories/schemes/monodromy.py`.

## Intake: https://github.com/lairez/periods — functionality — 2026-09-15

*Periods* is a Magma package for Lairez "Computing periods of rational integrals" (arXiv:1404.5069). Implements Griffiths-Dwork / Dimca Rham-Koszul reduction for hypersurface complements.

Input `f ∈ Q(t,x1..xn)` rational, `t = A.1` parameter. Output differential operator `L ∈ Q[t]<∂_t>` (or `t∂_t`) annihilating periods `p(t)=∫_γ f(t,x)dx`, where `γ_t ∈ H_n(A^n \ V(q_t))` horizontal. `L·p=0` for all `γ`.

* `Periods(f : r, variant)` — periods of `f` dx
* `Diagonal(f : r)` — diagonal `Σ [x^n y^n z^n]F · t^n` via `1/(1-t xyz)` trick
* `LaurentSequence(f)` — constant term of Laurent powers via residues — all reduce to periods

Core steps:

* Homogenize `f → fsf` square-free part, degree `d`
* `InitRK(f : r, variant)` builds `R=k[x0..xn,u,v]` with Jacobian ideal `Jac(f)` and trivial syzygy ideal `tsyz`, Groebner `jac`, `syz` — reduction basis `W_r`
* `TotDiff = ExtDiff - ExtProd` implements pole-order reduction `p/f^k → [p'] / f^{k-1}` modulo `Jac` + syzygies (Dimca)
* `GaussManin(f,r,L)` — at generic `t=ipoint` compute cohomology basis `H = H^n_{dR}(complement)` and connection matrix `M: H' = M·H` via `HomReduceMatrix`. Loop over many `ipoint` (100,101,…) over many primes `p` and rationally reconstruct `M(t)=mat/den ∈ Q(t)^{m×m}` via `RHAddRat/RHAddMod` + `RatInterp`/`PolInterp` (Chinese remainder)
* `Storjohann(A,b)` — high-order lifting + Keller-Gehrig + Padé to solve `A x = b` over `k[t]` without blow-up
* `CyclicEquation(mat/den, vec)` — cyclic vector to scalar operator `L`

Example: `f1=1/(1-(1-xy)z - t xy z(1-x)(1-y)(1-z))` → Apery operator order 3-4. `f2..f6` same operator via different `F`.

Magma-only, CeCILL, preliminary. Provides no standalone D-module library — extraction is `RhamKoszul` reduction + `Storjohann` + `RatInterp` pattern.

## How periods generalize — verbatim — 2026-09-15

Hard code is choice of `f`. Method is for any `f`:

**Fundamental object** (not hard-coded): For `f = p/q ∈ C(t,x1..xn) = C(S×A^n)` with `t` parameter (first variable hard-coded as `A.1`), family of hypersurfaces `V_t = V(q_t) ⊂ A^n`, complement `U_t = A^n \ V_t`. Period
```
p_γ(t) = ∫_{γ_t} f(t,x) dx1∧..∧dxn ,  γ_t ∈ H_n(U_t, C) horizontal
```
is pairing `H_n ⊗ H^n_{dR}(U_t)`. All `p_γ` satisfy same `L ∈ C(t)<∂_t>` — Picard-Fuchs. `Periods(f)` returns that `L`. `Diagonal` and `LaurentSequence` are not new — they are `Periods` after
```
Diag F(t) = [x^n y^n z^n]F = res F(x,y,z)/ (1-txyz)  → 1/(1 - y(1+x)... )
ct(f^n) = res f^n dx/x
```
transforms coded in `misc/apery.m`. One computation replaces 6 examples.

**What generalises directly** — change data, same functor:

* `n = Rank(A)-1` variables, `deg f` arbitrary — `InitRK` builds `R=k[x0..xn,u,v]` with `jac = (∂_i f·u - ...)` generally. Groebner `jac` + syzygy `tsyz` via `LeadingMonomialIdeal` is generic.
* `q_t` arbitrary denominator — `prepare_fraction` takes square-free part `fsf` and degree `deg`. No Apery coefficients remain.
* `r` pole-order bound — `r=1` is Griffiths, `r>1` adds syzygy filtration `W_r`. Algorithm is generic in `r`; completeness threshold is `r ≥ n+1` (Dimca). `variant {"mindeg","profile"}` is heuristic choice of `C[t]`-basis minimizing `deg(den)` — generic rational-function minimisation.
* Evaluation-interpolation — `GaussManin(f,r)` evaluates `f|_{t=ipoint}` at `ipoint=100,101,...` (or random `mod p`), computes `M(ipoint) ∈ F_p^{m×m}` via `HomReduceMatrix`, then `RatInterp`/`PolInterp` reconstructs `M(t) ∈ Q(t)` from many `F_p` evaluations. Method is generic `Q(t) = lim RatInterp(F_p)` via `RHNew` Chinese remainder. Replace `Q` by any number field `K` via `CoefficientRing(K)`.
* Linear solve — `Storjohann(A,b,prec)` solves `A x = b` over `k[t]` for any `A,b`; not Apery-specific. `PolynomialLinearAlgebra` linearises any `k[x]`-module to matrix over `k`.

**What changes category when you vary `S`:**
* `Periods: Rat(S×A^n) → D_S-Mod`, `f ↦ L = Ann_{D_S}(p_γ)`. Hard: `S=A^1`. General: `S=A^k` → Pfaffian system `∂_i Φ = M_i(t) Φ` (Gauss-Manin connection `∇_{GM}: H^n_{dR}(U/S) → H^n_{dR} ⊗ Ω^1_S`). `LinearHomotopies.m: GaussManinLin(f0,f1)` already computes one direction of this: family `f_t=(1-t)f0+t f1` gives `mat(t)/den(t)`. Full multivariate is same `InitRK` with `k` parameters and `k` matrices.
* Target `L` in `D_S` is cyclic vector reduction of `∇_{GM}`: `CyclicEquation(mat/den, vec) → L`. Generic for any `∇_{GM}`.

**What does not generalise without new math:**
* Single `t` only — need `D_S` in `k` variables for true multivariate PF ideal, not just one `mat/den`
* Hypersurface complement only — general `X → S` proper smooth family needs Griffiths-Dwork for `P^n` complete intersections, not just `A^n \ V(q)`
* No cycle choice — `L` annihilates *all* horizontal `γ`; to get *specific* `p_γ` need initial conditions `InitialConditionsOfCoordinate(gm,i,order)` which is only evaluation of `M` at `t=0` via `HomReduce`

In preamble terms: `f: U → S` as family (`f.as_family`), `H = R^n f_* Ω^•_{U/S}` object of `QCoh(S)`, `∇_{GM}: H → H ⊗ Ω^1_S` flat connection, `L = Ann(w)` in `D_S-Mod` where `w = ∫_γ Ω` section of `H`. `periods` package is private adapter computing `∇_{GM}` via `Dwork` reduction + `Storjohann` + `RatInterp`, and `L` via cyclic vector.

## Fundamental semantic language for periods generalization — verbatim — 2026-09-15

For `Periods: Rat(S×A^n) → D_S-Mod` to be statable, these must exist as categories/functors — not data:

**Base**
* `Sets`, `NN` — `n, r, deg` are ` : NN`
* `CommRings`, `CommAlgebras(C)`, `Fields` — `C`, `Q(t)`, `C(t,x) = Frac C[t,x]`
* `FctField(C)` — rational function `f = p/q : S×A^n ⇢ A^1` is morphism in `Rat(S×A^n)` (object of function field), `q` defines divisor

**Geometry / families**
* `Sch/C`, `Smooth(C)`, `Aff_n = A^n_C : Sch/C`
* `Div(X)` — hypersurface `V(q_t) ⊂ A^n` is `div(q) : Div`
* Open immersion `j: U = (S×A^n) \ V(q) ↪ S×A^n`, complement of divisor — object of `Open(S×A^n)`
* Morphism `f: U → S` via projection `Hom(Sch/C)`; family structure `f.as_family` requires flatness object in `Fam(S)` where `Fam(S) ⊂ Hom(Sch/C)_{/S}` defined by `flat + (proper/smooth where needed)`

**Sheaf / de Rham**
* `QCoh(X)`, `Sh(X_{Zar})`, `Ω^1_{X/S} : QCoh` — Kähler differentials
* De Rham complex `Ω^•_{U/S} : Ch(QCoh(U))` and its cohomology sheaf `H^n_{dR}(U/S) = R^n f_* Ω^•_{U/S} : QCoh(S)` — object carrying periods
* Rham-Koszul/Jacobian presentation: `Jac(f) = (∂_{x_i} f) : QCoh`, syzygy module `Syz(Jac)` — subobjects used to present `H^n_{dR}`; `W_r, U_r` filtration by pole order is filtration of this `QCoh(S)`-module
* `Ω^•(log S)` — not new; `H` with its Hodge filtration is object of `Filt(QCoh)`

**Connection / D-module**
* `Conn(S) = (E,∇)`, `E:H`, `∇: H → H ⊗ Ω^1_S` — Gauss-Manin connection `∇_{GM}` is object of `Conn(S)`
* `FlatConn(S) ⊂ Conn(S)` by `∇^2=0`
* `D_S-Mod` — `D_S = DiffOps(O_S)` sheaf of rings; flat connection ↔ left `D_S`-module via `∇ ↔ D_S`-action
* Cyclic presentation: for `w ∈ H`, `Ann_{D_S}(w) = {P : P·w=0} ⊂ D_S` — left ideal; Picard-Fuchs operator `L = generator of Ann(w)` is element `L : D_S`, `D_S/(L)` is quotient object. `CyclicEquation` is functor `FlatConn → D_S-Mod` via cyclic vector.

**Betti / pairing (to define `w`)**
* Analytification `(-)^{an}: Sch/C → An` and `H_n(U_t, C) = H_n^{sing}(U_t^{an}, C)` — fiber of local system `R^n f^{an}_* C : LocSys(S^{an})`
* Pairing `∫: H_n ⊗ H^n_{dR} → O^{an}_S` — morphism `w = ∫_{γ} Ω : S^{an} → C` section of `H^∨`; `γ` section of `R_n f_* C` is horizontal (local system section)

**Functor being generalised**
* `Periods: Rat(S×A^n) → FlatConn(S) → D_S-Mod`, `f ↦ (H,∇_{GM}) ↦ L`
* Source varies only as element `f : Rat`; target category `D_S-Mod` is fixed. `S=A^1` hard-coded → general `S=A^k` gives `∇_{GM} ∈ Mat_m(Ω^1_S)` Pfaffian system, not one `mat/den`. Reduction data `EchelonForm`, `Storjohann(A,b)` are linear-algebra adapters for `Modules(Q(t))`, not new categories.

**Not fundamental**
* `f1..f6`, `t= A.1`, `n=3`, `r=2`, `ipoint=100`, `p` prime, `den`, `mat` coefficients — elements/morphisms in above
* `Diagonal, LaurentSequence` — composites `Rat → Rat` via `F ↦ 1/(1-t xyz)F` then `Periods`; no new functor

## Intake: Monodromy of Family of Cubic Surfaces — 2026-09-15 — verbatim

No general method beyond intake. Paper-specific notebooks for family `w^3 = f`, `f=y^2z - x^3 + xz^2` (cubic surface 3-fold branched over cubic curve):

* `Intersection Pattern...sagews` + `Translation to Hesse Form.sagews` — enumerates 27 lines on `V(w^3-f)` as pairs of linear forms `[a0,a1,a2,a3]` with `ζ = e^{2πi/3}`, `α: 3t^4-6t^2-1=0` (x of flexes `≠[0:0:1]`). Test `L_i ∩ L_j ≠ ∅ ⇔ det M_{4×4}(rows_i,rows_j)=0` → `27×27` 0/1 matrix (diag -1), finds one sextuple of pairwise skew lines `(1,5,7,12,14,18)` as basis of `Pic = H^2` (blow-up of `P^2` at 6 points). Hard-coded flex data.

* `MonodromyOfRootsControllingCubicFlexes.nb` — `NSolve`/`Animate` of roots of `3x^4 -4(-1+e^{2πit})x^3 -6x^2 +12(-1+e^{2πit})x -4(-1+e^{2πit})^2 -1` (flex abscissae along loop), `rootPlot` animation. Naive numerics, no validated ODE.

* `UnderstandingW(E6).nb` — `6×6` matrices `X, s1..s5` for `W(E6)=O(E6)` as reflection group on `Pic` orthogonal to `K`, `charpoly (t-1)^5(t+1)`, 36 positive roots. Ad-hoc.

All hard-coded to `f=y^2z-x^3+xz^2` and its Hesse form. No `GaussManin`, `Periods`, `kv`, or reusable `CW/π1` framework. Intersection via `det`, flexes via `NSolve`, Weyl via explicit matrices — instances of already-intaken families `f.as_family`, `H^2_{dR}(X/S)`, `Weyl(O(L))`, `π1`/discriminant complement, not a new abstraction to absorb. Do not add as reference implementation.

## Intake: Fermat Jacobians — functionality — 2026-09-15 — verbatim

Yes — new vs CAP/periods. Narrow to Fermat Jacobians `J_m = Jac(y^2 = x^m-1)` (CM by `Q(ζ_m)`), not general `∇`.

**What it does** — Magma, `m` param (mostly odd `m`, `g=(m-1)/2`; even handled):

* `FermatJacobians1_computeMTandKconn.m` (620l) — Mumford-Tate:
  * `MatrixOfNorm(m,d)`, `MatrixOfReflexNorm(d)` with CM type `{i<d/2 : (i,d)=1}`, `PartialMTMatrix = Norm·Reflex` — builds `MTMatrix = BuildMTMatrix(m)` by joining divisors `d|m`. `Ker(Transpose(MT))` gives multiplicative equations `∏ x_j^{v_j}=1` for `MT(J_m) ⊂ G_m^{φ(m)}` (Deligne). `ListOrderCharacters` fixes order. `P_gamma(α)= ∏Γ(i/m)^2/Γ(2i/m) / (2πi)^{#α/2}` via `Gamma(C)`, minimal polynomial `MinimalPolynomial(...,2m)` → element `true_gamma ∈ Kconn`.
  * `compute_Kconn()` → connected monodromy field `K^{conn} = Q( P_gamma )` (field generated by Gamma ratios). Uses `SplittingField(CyclotomicPolynomial(m))`.

* `FermatJacobians2_computeST.m` (272l) — Sato-Tate:
  * Tensor rep `STcoeff(tau,α)= μ(target)Gal(P_target)/μ(start)P_start` with `μ(α)=∏(m-2i)/m`. `small_a_matrix`, `relation_from_character: ∏ T[i, u^{-1}i] - STcoeff =0`. `compute_component(tau)` builds ideal `I(τ) ⊂ Kconn[t_{ij}]` with permutation structure `j≠u·i`, `TT^8=1`, and all `relations_from_character_eigenspace` from `MT` equations. Groebner → ideal of component `ST^0·τ`.

* `FermatJacobians3_computeEndomorphismFields.m` + `J60.m, X20.m` — endomorphism fields via splitting field of `Frob` charpolys, counting factorisation of `p` in `K1/K12` etc., `HeuristicEndomorphismLatticeDescription`.

* `FastCharPolyJ60.m` / `Example649...` — `FrobCharpolyC60Jacobi(p)` : `f_p(T)=∏(T-α_a)` where `α_a = -χ^a(-1) J(χ^a,φ)` Jacobi sum. Implemented by counting `x∈F_p`: `logs` discrete log via `PrimitiveElement`, `counts[r][s] = #{x: log_g(x)=r mod60, log_g(1-x)=s mod2}`, then `Ja= Σ counts·z^{a r+30s}`. Coerce `K=Q(ζ60) → Z`. Also `BaseFieldDataFromFrobCharpoly`, `EndomorphismFieldFromFrobCharpoly` via splitting field degrees.

* `J60.out, Example428...` — data for `m=60,15,10`, `Kconn` polynomials, MT equations.

**New vs intake:** None of this is in CAP (rigorous ODE) or Lairez (Griffiths-Dwork). Intake has generic `monodromy(reps)/π1` but not `MT/ST/K^{conn}` via Gamma/reflex norms, nor `Jacobi-sum Frobenius` for CM Jacobians. Belongs to arithmetic Hodge / Sato-Tate, not just `∇_{GM}` transport.

**Generalises?** Hard-coded to `y^2=x^m-1` CM family. Matrices `Norm(m,d)` and `Γ-product` use `Q(ζ_m)` class field theory (Shioda, Deligne). Same functor generalises to any CM abelian variety with explicit CM type (replace `TriplicateExponents` and reflex type), but not to general `J(C)` without CM. `FrobCharpoly` Jacobi method generalises to any Fermat-type `x^m+y^n=1`.

Add as intake if you want `MumfordTate/SatoTate/EndomorphismField` as owned `Hodge → Groups` functors; otherwise no reusable `D-mod` piece beyond what `families/periods` already covers.

## Fundamental objects for Fermat Jacobians generalization — verbatim — 2026-09-15

For `J_m = Jac(y^2=x^m-1)` MT/ST to be statable, these must exist as categories/functors — not `m=60`:

**Base**
* `Sets`, `NN` — `m,g = φ(m)/2, d|m` are `:NN`
* `Fields`, `NumberFields`, `CMFields ⊂ Fields` — `Q(ζ_m)=SplittingField(Φ_m) : Fields`, its subfields `Q(ζ_d)`
* `AbVar/Q : Cat` — abelian variety `J_m : AbVar`, Jacobian functor `Jac: Curves → AbVar`; `CM` is property (`End^0(J_m) ⊃ Q(ζ_m)`), not a category. `g = dim J_m` is rank of `H^1`, not an object
* `HodgeStr(Q)` — pure `Q`-Hodge structure of weight 1; functor `H^1_B: AbVar → HodgeStr`, `H^1_{dR}(J_m) : Vect_{Q(ζ_m)}`

**Torus / character language (where `MTMatrix` lives)**
* `Tori_Q : Cat` — torus `T_K = Res_{K/Q} G_m : Tori`, its character group `X^*(T_K) = ⊕_{σ:K↪C} Z·χ_σ`
* Homomorphism of tori `Norm_{m,d}: T_{Q(ζ_m)} → T_{Q(ζ_d)}` — morphism in `Tori`. Matrix `MatrixOfNorm(m,d) : Mat_{φ(d)×φ(m)}(Z)` is its `X_*` representation. Not fundamental; the functor `Res` is.
* CM type `Φ = {i<d/2 : (i,d)=1} ⊂ Hom(Q(ζ_d),C) : Sets(Sets)` — datum defining reflex. Reflex norm `N_{Φ^*}: T_{Q(ζ_d)} → T_{Q(ζ_d)}` — morphism `MatrixOfReflexNorm(d)`
* Product `PartialMT = Norm ∘ N_{Φ^*} : T_{Q(ζ_m)} → T_{Q(ζ_d)}` — `MT(J_m)` is subtorus `⋂_d Ker( character )` where `Ker` is kernel in `Tori`. Equation `∏ x_j^{v_j}=1` is element `v ∈ Ker( Transpose(BuildMTMatrix(m)) : Z^{Σφ(d)} → Z^{φ(m)})`; `B = Basis(Ker)` is `X^*(T/Q)` basis. The matrix is presentation of `X^*(MT)`.

**Hodge / Mumford-Tate language**
* `MumfordTate: AbVar → SubTori_{GSp(H^1_B)}` functor — `MT(J_m) = Stab_{GSp}(Hodge tensors) =` smallest `Q`-torus containing Hodge cocharacter `μ: G_m → GL(H^1_B⊗C)`. For CM, `MT ⊂ T_{Q(ζ_m)}` via `Norm/Reflex` description above. General `A` CM by `E` uses `Φ_A` and reflex `Φ^*`.
* Field `K^{conn} ⊂ Q^{ab}` — connected monodromy field. Object `K^{conn} : Fields` is field generated by normalized Gamma ratios `P_γ(α)= ∏Γ(i/m)^2/Γ(2i/m) / (2πi)^{#α/2} : C^×` for `α ∈ X^*(MT)`. `MinimalPolynomial(P_γ,2m)` and `Roots(-,K^{conn})` pick the `Q^{ab}`-realisation. Not fundamental; `Γ` value is `C` element, `K^{conn}` is subfield of period field.

**Galois / Sato-Tate language**
* `ℓ-adic representation` `ρ_{ℓ}: Gal_Q → GSp(H^1_{ℓ}) : Groups` and Zariski closure `G_{ℓ} : GrpSch/Q_ℓ`; `G_{ℓ}^0 = MT ⊗ Q_ℓ` after `K^{conn}` (Mumford-Tate conjecture, theorem for CM)
* Sato-Tate group `ST(J_m) ⊂ USp(2g)` — maximal compact of `MT⊗R`, object of `CompactLieGroups`; `ST^0` is identity component, `π_0(ST)=Gal(K^{conn}/Q)`. `compute_component(τ)` builds ideal `I(τ) ⊂ K^{conn}[t_{ij}]` whose variety is `τ·ST^0` as algebraic set `∏ T[i,u^{-1}i] - STcoeff(τ,α)=0` plus `TT^8=1, T[i,j]=0` for `j≠u·i`. This is coordinate ring of `ST` in `AffVar_{K^{conn}}`.
* Endomorphism algebra `End^0(J_m)=End(J_m)⊗Q : Algebras_Q` and field `EndField ⊂ K^{conn}` where all endomorphisms defined — object of `Fields`; `Frobenius` conjugacy `Frob_p : H^1_{ℓ} → H^1_{ℓ}` with charpoly `f_p(T)=det(T-Frob_p|H^1) = ∏(T+χ^a(-1)J(χ^a,φ))` where Jacobi sum `J(χ^a,φ)= Σ_{x} χ^a(x)φ(1-x) : Q(ζ_m)` is period. `FastCharPoly` counts `x∈F_p` via `log_g` discrete log is evaluation of this character, not a new functor.

**Not fundamental**
* `m=15,60,20`, `z_m=ζ_m : C`, `g, coprimes_to_m`, `OrderCharacters`, `ipoint`, `p=1021` — elements/morphisms in above
* `X,Y,Z` matrices `s1..s5` in `UnderstandingW(E6)` — specific `Weyl(O(H^2))` elements, instance of `Weyl(Lattice)` already in intake

## Desired capability: honest Q_ℓ, étale cohomology, Galois cohomology as specialization — note 2026-09-15

Need honest `Q_ℓ`, étale cohomology, and Galois cohomology as a specialization — not a formal `H^1_ℓ` string.

* `Q_ℓ` is not `Q` with `ℓ` appended. It is the `ℓ`-adic completion `Q_ℓ = (lim← Z/ℓ^n) ⊗ Q` as object of `Fields` with its `ℓ`-adic topology, valuation, and absolute Galois action. Need `Z_ℓ`, `Q_ℓ`, `Q_ℓ^{ur}` as coefficient rings for sheaves, with `ℓ`-adic lisse sheaves `Q_ℓ(n)` as objects of `Sh(X_ét, Q_ℓ)` obtained via inverse system `(Z/ℓ^n)_{n}` and tensor with `Q_ℓ`. Without this, `ρ_ℓ: Gal_Q → GSp(H^1_ℓ)` cannot be stated.

* Étale cohomology `H^i_ét(X_{ét}, Q_ℓ)` is sheaf cohomology of the étale site `X_ét`, not singular cohomology with `Q_ℓ` coefficients spliced in. Requires site `(C_X, J_ét)` where `C_X = Ét_{/X}` (étale morphisms `U → X`) and `J_ét` is Grothendieck topology given by covering families `{U_i → U}` jointly surjective, equivalently sieves `S ⊂ h_U` satisfying (maximal sieve, stability under pullback, local character). Sheaf condition is `F(U) ≅ lim_{S} F` for covering sieves. This gives topos `Sh(X_ét)` and derived functor `RΓ(X_ét, -) : D(Sh) → D(Ab)` whose cohomology is `H^i_ét`.

* Galois cohomology as specialization: for `X = Spec K` (`K` field, e.g. `K=Q`), `X_ét` is the site of finite étale `Spec L → Spec K` (finite separable extensions), which is equivalent to the site of finite discrete `Gal_K`-sets with covering families given by jointly surjective families. Then `Sh((Spec K)_ét) ≃ Gal_K-Sets` (discrete `Gal_K`-modules), and `H^i_ét(Spec K, F) = H^i(Gal_K, F_{K^{sep}})` — Galois cohomology is the value of the same site cohomology functor at the terminal object. Need this identification as theorem, not as separate definition. Without sites, `H^i(Gal, -)` and `H^i_ét` are two unrelated functors.

* Requires: category `Sites` with objects `(C, J)` (small category + Grothendieck topology via sieves/covering families), morphisms of sites (continuous functors), associated sheaf functor `a: PSh(C) → Sh(C,J)`, and cohomology `RΓ`. Specializations: Zariski site `(Open(X), J_Zar)`, étale site `(Ét_{/X}, J_ét)`, pro-étale, fppf — each is an object of `Sites`. The same formalism must own Zariski, étale, and Galois as instances.

Intended owners: `categories/topology/sites.py` (`Site`, `GrothendieckTopology`, `Sieve`, `CoveringFamily` with axioms), `categories/topology/sheaves_on_site.py` (`Sh(C,J)`), `categories/etale/etale_site.py` (`X_ét`), `categories/etale/ladic_sheaves.py` (`Q_ℓ`, `Q_ℓ(n)` lisse), `categories/galois/galois_cohomology.py` (`H^i(Gal_K, -) = H^i_ét(Spec K, -)` as specialization, not a parallel definition). Not a free `etale_cohomology(X, Q_ell)` function — `X.etale_site().cohomology(i, Q_ell)`, `Spec(K).etale_cohomology()` on the site objects.

## Desired capability: Gauss-Manin, six functors, derived pushforwards — note 2026-09-15

Need the Gauss-Manin connection, some basic six-functor formalism for sheaves, and derived functors — particularly right-derived pushforwards.

* Gauss-Manin connection `∇_{GM}: H^k_{dR}(X/S) → H^k_{dR}(X/S) ⊗ Ω^1_S` is not an ad-hoc matrix `M(t)` from `periods`. It is the flat connection on the relative de Rham cohomology sheaf `H^k_{dR}(X/S) = R^k f_* Ω^•_{X/S}` obtained as the `d_1` differential of the Hodge-de Rham spectral sequence or, equivalently, as the connection induced by the derived pushforward of the relative de Rham complex. Construction lives in `D_S-Mod` via `∇_{GM} ↔ D_S`-action; `PF(w)` is `Ann_{D_S}(w)` for `w = ∫_γ Ω`. Need `∇_{GM}` as object of `FlatConn(S)` with its regular singularities and Griffiths transversality, not just `mat/den`.

* Six functors for sheaves: for any morphism `f: X → S` need functors between derived categories `D(Sh(X)), D(Sh(S))` (étale, coherent, analytic — same formalism via sites):
  * `f^*: D(S) → D(X)` (pullback, left adjoint to `f_*`), `f_*: D(X) → D(S)` (pushforward)
  * `f_!: D(X) → D(S)` (pushforward with proper support), `f^!: D(S) → D(X)` (exceptional pullback, right adjoint to `f_!`)
  * `⊗, Hom` internal tensor and internal hom in `D`
  * Adjunctions `f^* ⊣ f_*`, `f_! ⊣ f^!`, projection formula `f_!(F ⊗ f^*G) ≅ f_!F ⊗ G`, base change, duality. These are required to state `f.as_family` cohomology, dualizing complexes, and `R f_*` compatibility.

* Derived functors — particularly right-derived pushforwards: `R f_*: D(Sh(X)) → D(Sh(S))` is right derivation of `f_*: Sh(X) → Sh(S)` via injective resolutions. Need `R^i f_* = H^i(R f_*)` as objects `R^i f_* Ω^•`, `R^i f_* Q_ℓ` etc., with `R f_*` preserving constructibility under proper/base-change hypotheses. Period sheaf `H^k_{dR}(X/S) = R^k f_* Ω^•_{X/S}` and `R^k f^{an}_* Q_ℓ`, `R^k f^{an}_* C` (Betti local system) are all instances of the same `R f_*`. The comparison `R^k f_*^{dR} ⊗ C ≅ R^k f^{an}_* C ⊗ O^{an}` is the comparison isomorphism that makes `∇_{GM}` and monodromy agree. Without `R f_*` as derived functor, each `H^k` is a separate ad-hoc construction.

* Requires: category `Derived(C)` for Grothendieck abelian `C = Sh(X_ét), QCoh, Mod_{D_S}`, functors `L f^*, R f_*, R f_!, f^!` as triangulated functors with adjunctions, and the full six-functor package (not just `R f_*`). Specializations: `RΓ(X, -) = R p_*` for `p: X → Spec k`; `H^i_ét = R^iΓ`; `H^i(Gal, -)` is `R^iΓ` for `Spec K`.

Intended owners: `categories/functors/gauss_manifold.py` (`GaussManin` as `∇_{GM}` on `H_{dR}`), `categories/sheaves/six_functors.py` (`f^*, R f_*, R f_!, f^!, ⊗, Hom` with adjunctions), `categories/derived/derived_category.py` (`D(-)`, `R f_*` via injectives, `L f^*`), `categories/derived/pushforward.py` (`R^i f_*` as cohomology sheaves). Not free `pushforward(f, sheaf)` with no derived structure — `f.derived_pushforward(sheaf)` in `D(Sh)` on the site objects, with `R^i` as `H^i`.

## Desired capability: p-curvature — note 2026-09-15

Need `p`-curvature.

For a flat connection `∇: E → E ⊗ Ω^1_{X/S}` on a smooth `S`-scheme `X` in characteristic `p>0` (or reduction mod `p` of a characteristic-zero connection), the `p`-curvature is the `O_X`-linear map
```
ψ_p(∇): T_{X/S} → End_{O_X}(E),  ψ_p(D) = ∇(D)^p - ∇(D^{[p]})
```
where `D^{[p]}` is the `p`-th iterate (restricted Lie algebra structure on derivations) and `∇(D)^p` is `p`-th iterate as differential operator. For `X = Spec R[t]` and `∇ = d + A dt`, this is `ψ_p(∂_t) = (∂_t + A)^p - (∂_t^p + A^{(p)})` as `p`-linear operator. Vanishing `ψ_p = 0` is Cartier descent: `∇` has full set of horizontal sections `E^{∇}` with `E ≅ F^* E^{∇}` via Frobenius `F: X → X^{(1)`. The `p`-curvature measures obstruction to descending `∇` along Frobenius and controls Grothendieck-Katz `p`-curvature conjecture: `∇` has algebraic solutions iff `ψ_p ≡ 0 mod p` for almost all `p`.

Requires: category `Conn(X/S)` in characteristic `p`, restricted Lie algebra `T_{X/S}` with `D ↦ D^{[p]}`, Frobenius twist `X^{(1)}`, Cartier operator, and functor `ψ_p: Conn → Higgs_{X^{(1)}}` to Higgs fields (`End(E)`-valued 1-forms). Need `ψ_p` as morphism `T_{X/S} → End(E)` on the connection object, not a bare matrix `A_p`. Instances: Gauss-Manin `∇_{GM}` reduced mod `p`, its `p`-curvature is the obstruction whose vanishing detects algebraicity of periods; for `PF(w)` operator `L ∈ D_S`, `ψ_p(L)` is its `p`-curvature as `p`-linear operator on `D_S`-module.

Intended owners: `categories/connections/p_curvature.py` (`p_curvature(∇): Higgs`), `categories/characteristic_p/cartier.py` (`Frobenius`, `Cartier descent`), `categories/connections/characteristic_p.py` (`Conn_p`, `ψ_p` with `D^{[p]}`). Not a free `p_curvature(matrix)` — `∇.p_curvature(D)` on the connection object in `FlatConn(X/S)` over `F_p`.

## Desired capability: zeta functions of varieties over F_q and Weil verification — note 2026-09-15

Need to work with zeta functions of varieties over `F_q`, and at least for (some) curves, affine spaces, projective spaces, Grassmannians, etc. where point counts have explicit formulas, get closed forms and verify all Weil conjectures hold for them.

* Zeta function is not a Python `float` from `exp(Σ N_r T^r/r)` numerically. It is the formal series/exponential
  ```
  Z(X/F_q, T) = exp( Σ_{r≥1} |X(F_{q^r})| T^r / r ) ∈ 1 + T·Q[[T]]
  ```
  equivalently Euler product `∏_{x∈|X|} (1 - T^{deg x})^{-1}`, object of `Q(T)` (rational function when Weil holds) with its `T`-adic parent `Q[[T]]`. Interface lives on the variety: `X.zeta()` returns `Z` as element `Z : Q(T)` with numerator/denominator `P_i(T)`, not a bare power series guess.

* Concrete point counts with closed forms (must be exact, not enumerating `F_{q^r}` for large `r`):
  * `A^n: |A^n(F_{q^r})| = q^{n r}` → `Z = 1/(1 - q^n T)`
  * `P^n: |P^n(F_{q^r})| = (q^{(n+1)r}-1)/(q^r-1) = 1+q^r+…+q^{nr}` → `Z = 1/((1-T)(1-qT)…(1-q^n T))`
  * `Gr(k,n): |Gr(k,n)(F_{q^r})| = Gaussian binomial  [n choose k]_{q^r}` with `q`-factorial formula → `Z = ∏_{i=0}^{k(n-k)} 1/(1-q^i T)^{c_i}` with explicit `c_i` or product of `q`-integers; closed via `q`-binomial rationality
  * Some curves: `A^1` minus `n` points, elliptic curve `E: y^2 = x^3+ax+b` with `|E(F_{q^r})| = q^r+1 - α^r - \bar α^r` (`α\bar α = q`), hyperelliptic of low genus where `L`-polynomial is known; at least need interface `Curve.point_count(r)` that is exact and `Z`-rational.

* Must get closed forms: `Z(X,T) = ∏_{i=0}^{2 dim X} P_i(T)^{(-1)^{i+1}}` with `P_i(T) = det(1 - T·Frob | H^i_{c,ét}(X_{\bar F_q}, Q_ℓ)) ∈ Z[T]`, `P_0 = 1-T`, `P_{2n}=1-q^n T` for connected `X`. Construction is `X → (N_r = |X(F_{q^r})|) → Z = exp` with rational reconstruction (compare coefficients `N_r` with `log Z` expansion), not numeric `exp`.

* Must verify all Weil conjectures for these concrete `X` and return certificates, not just claim:
  * (W1) Rationality: `Z ∈ Q(T)` — check `Z` is rational function with `Z ∈ 1+T·Z[[T]]`
  * (W2) Functional equation: `Z(X, 1/(q^n T)) = ± q^{nχ/2} T^{χ} Z(X,T)` with `χ = Σ (-1)^i b_i`, `n=dim X`; verify as identity in `Q(T)`
  * (W3) Riemann hypothesis: `P_i(T)=∏(1-α_{ij} T)` with `|α_{ij}| = q^{w/2}` for `w=i` (purity) — verify by factoring `P_i` over `C` and checking `|α| = q^{i/2}` via `QQbar` absolute value, or via `ℓ`-adic weights. For concrete cases this is checkable: `P_i` split with known roots `q^{j}` or Weil numbers `α, \bar α`.
  * (W4) Betti numbers: `deg P_i = b_i = dim H^i_{ét}` — compare with known `b_i` from `ℓ`-adic cohomology (e.g. `b_i(P^n)=1` for even `i≤2n` else `0`; `b_i(Gr)` via Schubert cells).

* Requires: site cohomology `RΓ_c(X_{ét}, Q_ℓ)` from six-functor `R f_!` already noted, trace formula `N_r = Σ (-1)^i Tr(Frob^r | H^i_c)`, and the comparison `Z = ∏ det(1-T·Frob|H^i_c)^{(-1)^{i+1}}`. The same `R f_!` and `Q_ℓ` owners above must supply `H^i_c` and `Frob` action.

Intended owners: `categories/zeta/zeta.py` (`Variety.zeta(): Q(T)` via `N_r`), `categories/varieties/point_counts.py` (`X.point_count(r): NN` exact for `A^n`, `P^n`, `Gr(k,n)`, some curves), `categories/etale/weil.py` (`WeilVerification` with `rationality`, `functional_equation`, `rh_roots`, `betti` checks). Not a free `zeta_via_brute_force(X,q)` — `X.zeta()` on the variety object in `Sch/F_q` with `Q_ℓ`-cohomology behind the same site, and `Z.verify_weil()` returning certificates for the concrete families.

## Fundamental objects to even state Weil conjectures — verbatim — 2026-09-15

To state `W(X/F_q)` you need these as categories/functors — not `q=5`, `X=P^2`:

**Base**
* `FinFields` — object `F_q : Fields` with `q=p^a : NN`, `Fr_q: Spec \bar F_q → Spec \bar F_q` Frobenius morphism `x↦x^q`; `Gal(\bar F_q/F_q)= \hat Z·Fr_q : Groups`
* `Sch/F_q : Cat` — variety `X : Sch/F_q` finite type, `dim X = n : NN` (element), base-change `X_{\bar F_q}=X×_{F_q}\bar F_q : Sch/\bar F_q`; `|X(F_{q^r})| = Hom_{Sch/F_q}(Spec F_{q^r}, X) : Sets` has `cardinality : NN`

**Counting / zeta (no cohomology yet)**
* Formal series `Q[[T]] = (T)-adic completion of `Q[T]`; subobject `1+T·Q[[T]]` and `Q(T)=Frac Q[T] : Fields`
* Euler product as identity in `Q[[T]]`: for `|X|` closed points, `deg x = [κ(x):F_q]`
  ```
  Z(X,T)=exp( Σ_{r≥1} N_r T^r/r ) = ∏_{x∈|X|} (1-T^{deg x})^{-1} : Q[[T]]
  ```
  where `N_r = |X(F_{q^r})|`. This is definition of `Z`, element `Z : Q[[T]]`. Rationality `Z ∈ Q(T)` is first Weil statement.

**Cohomology (to state factorisation)**
* Site `X_ét : Sites` and `ℓ≠p`, `Q_ℓ : Fields` as before; `Sh(X_ét,Q_ℓ) : AbCat` and derived `RΓ_c = R(p_!) : D(Sh) → D(Vect_{Q_ℓ})` for `p: X→Spec F_q` (proper-support pushforward from six functors). Object `H^i_{c,ét}(X_{\bar F_q}, Q_ℓ) = H^i(RΓ_c(Q_ℓ)) : Vect_{Q_ℓ}` finite-dimensional, with continuous `Gal(\bar F_q/F_q)`-action; `Fr_q` acts as `Frob : H^i_c → H^i_c`
* Grothendieck-Lefschetz trace formula (must exist to link counting to cohomology):
  ```
  N_r = Σ_{i=0}^{2n} (-1)^i Tr( Fr_q^r | H^i_{c} )
  ```
  Without `R f_!` and `Tr` this is not statable.

**Factorisation and statements**
* From trace, `Z` factors as
  ```
  Z(X,T)= ∏_{i=0}^{2n} P_i(T)^{(-1)^{i+1}},  P_i(T)=det(1-T·Fr_q | H^i_c) ∈ Z[T] : Poly(Z)
  ```
  Need `Poly(Z) → Q(T)` and `deg P_i = b_i = dim H^i_c : NN` (fourth Weil/Betti). This is rationality refinement.
* Functional equation needs Poincaré duality for `H^i_c` (`f^! Q_ℓ ≅ Q_ℓ(n)[2n]`) and `f_! ⊣ f^!` :
  ```
  Z(X, 1/(q^n T)) = ± q^{nχ/2} T^{χ} Z(X,T),  χ=Σ(-1)^i b_i : ZZ
  ```
  as identity in `Q(T)` (needs `⊗` and dualizing complex).
* Riemann hypothesis needs algebraic numbers and weights: `P_i(T)=∏_j (1-α_{ij} T)`, `α_{ij} : \bar Q ⊂ C` via chosen `\bar Q↪C`, condition `|α_{ij}| = q^{i/2}` for all embeddings `|·|: \bar Q→C` (Weil numbers of weight `i`). Needs `Fields`, `AlgClosure`, `Abs: C→R_{≥0}`, and `Weight` as `NN` element. No numerics — `|α|=q^{i/2}` is equality in `R`.

**Not fundamental**
* `q=7`, `X=A^n,P^n,Gr(k,n)`, `N_r = q^{nr}` or `q`-binomial, explicit `P_i = 1-q^j T` — elements `:NN` and morphisms `Spec F_{q^r}→X` whose counts give closed `Z = 1/(1-q^n T)` etc.; the functor `X ↦ Z(X)` and its factorisation are.

## Desired capability: operationalize Lefschetz trace for Frob — note 2026-09-15

Need a way to operationalize the Lefschetz trace formula, especially on étale cohomology for the trace of Frobenius.

Need `Tr(Frob^r | H^i_{c,ét}(X_{\bar F_q}, Q_ℓ)) : Q_ℓ` as computable morphism on the cohomology object, not a formal symbol. Formula
```
N_r = Σ_{i=0}^{2n} (-1)^i Tr( Fr_q^r | H^i_{c}(X_{\bar F_q}, Q_ℓ) )
```
must be executable: from `X : Sch/F_q` produce `H^i_c : Vect_{Q_ℓ}` with `Frob : End(H^i_c)` (via `X_ét`, `RΓ_c = R(p_!)`, `Q_ℓ(n)`), compute its trace via `Vect_{Q_ℓ}` linear algebra, and compare with `|X(F_{q^r})| : NN` (finite-set count). This is the bridge between counting and cohomology that makes `Z(X,T)=∏ P_i(T)^{(-1)^{i+1}}` effective, where `P_i(T)=det(1 - T·Frob | H^i_c)`.

Requires: `Frob : X_{\bar F_q} → X_{\bar F_q}` as `Fr_q × id` on `X×_{F_q}\bar F_q`, its action `Frob^*: H^i_c → H^i_c` via functoriality of `RΓ_c`, and `Tr: End(V) → Q_ℓ` on `Vect_{Q_ℓ}` (finite-dimensional). Operationalization means: when `H^i_c` is presented (e.g. via known cell decomposition for `A^n, P^n, Gr` or via Monsky-Washnitzer / crystalline `RΓ_c` with Frobenius lift for general `X`), actually return matrix `M_i = Frob|_{H^i_c} : Mat_{b_i}(Q_ℓ)` and compute `Tr(M_i^r)`, `det(1 - T M_i)` exactly in `Z[T]`. Not a placeholder `trace_of_frob` stub.

For concrete families (`A^n, P^n, Gr(k,n)` and some curves) the trace is already known from explicit `P_i`: e.g. `Tr(Frob|H^{2j}(P^n))=q^j`, otherwise `0`; for `Gr`, `Tr` is `q^{something}` via Schubert. The operational trace must reproduce those `N_r` via the sum, certifying the formula for those `X`. For general `X`, the trace is the computational content of Monsky-Washnitzer / rigid cohomology `H^i_{MW}` with Frobenius lift, behind the same `RΓ_c` interface — private adapter, but `X.etale_cohomology(i)` and `Frob.matrix()` stay owned.

Intended owners: `categories/etale/trace_formula.py` (`LefschetzTrace` with `Tr(Frob^r|H^i_c)` and `N_r = Σ (-1)^i Tr`), `categories/etale/frobenius.py` (`Frobenius : End(H^i_c)` as `RΓ_c(Fr_q)`), `categories/etale/monsky_washnitzer.py` (private MW adapter for general `X` when `RΓ_c` not yet known). Not a free `trace_frobenius(X)` — `X.etale_cohomology_c(i, Q_ell).frobenius().trace(r)` on the cohomology object, with `X.point_count(r)` on the variety object for comparison.

## Desired capability: HH(A) — Hochschild homology — note 2026-09-15

Support `HH(A)` — Hochschild homology of an (associative, possibly dg) algebra `A`.

* `HH(A)` is not a bare list of groups computed by a helper. It is the homology of the Hochschild complex `C(A): ... → A^{⊗ n+1} → A^{⊗ n} → ...` with differential `b(a0⊗...⊗an)= Σ (-1)^i ... + (-1)^n a_n a_0 ⊗ ...`, as object `HH(A) = ⊕_n HH_n(A) : GrMod` (`HH_0 = A/[A,A]`, etc.). For dg `A`, `C(A)` is the derived tensor `C(A)= A ⊗^{L}_{A⊗A^{op}} A : Ch`, i.e. `HH(A)= Tor^{A⊗A^{op}}_*(A,A)`. Need `HH(A)` as functor `HH: Alg_{dg} → GrMod` (or `D(Ab)`), with `HH(A)` computed as `H_*(C(A))`.

* Requires: category `Alg_{dg}(k)` (dg algebras over `k` with `k` a commutative ring), `Enveloping algebra `A^e = A⊗A^{op} : Alg`, `Bimod_A = Mod_{A^e}`, and derived `⊗^L`. Interface must be `A.hochschild_complex()` returning `C(A) : Ch(k)` and `A.hochschild_homology(n)` returning `HH_n(A) : Mod_k` with `HH_0 = abelianization`.

* Expected compatibilities (at least for smooth cases): HKR isomorphism for smooth commutative `A = O(X)`: `HH_n(A) ≅ Ω^n_{X/k}` as objects of `GrMod`, with Connes differential `B: HH_n → HH_{n+1}` matching `d_{dR}`. For scheme `X`, `HH(X)=HH(Perf(X))` and `HH(X) ≅ ⊕ H^i(X, Ω^j)`. Need `HH` to compose with `Perf` and `QCoh` via Morita invariance `HH(A) ≅ HH(Perf_A)`.

* In some cases (smooth proper `X` of dimension `n`, e.g. `P^n, Gr(k,n),` smooth curves) `HH_*(X)` is finite and explicitly computable via HKR, and must be verified. For general `A`, `HH` is retained as formal complex with known type, not forced to compute.

Intended owners: `categories/homology/hochschild.py` (`HochschildComplex`, `HH(A)` functor with `Tor^{A^e}`), `categories/algebras/dg_algebras.py` (`DgAlgebra` with `A^e`, `Bimod`), `categories/schemes/hochschild_kostant_rosenberg.py` (HKR `HH_n(O_X) ≅ Ω^n`). Not a free `hochschild_homology(A)` — `A.hochschild_complex()`, `A.hh(n)` on the algebra object, with `Perf(X).hh()` for schemes.

## Desired capability: right-derived Hom and left-derived tensor — Ext, Tor, derived tensor products — note 2026-09-15

> One also needs basic right-derived functor machinery for (at least) R-modules, for (at least) Hom and tensor (so Ext and Tor). Derived tensor products are especially important

Need basic right-derived functor machinery for `R-Mod` for Hom and tensor — `Ext` and `Tor` — derived tensor products especially.

* `R-Mod : AbCat` Grothendieck abelian (for `R : CommRings` or associative `R : Rings`) with enough injectives and enough projectives/flats. Need derived category `D(R-Mod) : TriCat` as Verdier localization `D = K(R-Mod)[qis^{-1}]` (homotopy category of complexes localized at quasi-isomorphisms), with shift `[1]`, distinguished triangles from mapping cones, and cohomology functors `H^n: D → R-Mod`. Interface lives on `D(R-Mod)`, not as a free `derived_category(R)` helper returning bare complexes.

* Right-derived Hom: `Hom_R(-,-): R-Mod^{op} × R-Mod → Ab` left exact in second variable; its right derivation `RHom_R: D(R-Mod)^{op} × D(R-Mod) → D(Ab)` via injective (or `K`-injective) resolutions `M → I^•`, `RHom(M,N)=Hom^•(M,I^•)` (or `Hom^•(P^•,I^•)` for unbounded). Then `Ext^n_R(M,N) = H^n(RHom_R(M,N)) = R^n Hom_R(M,N) : Ab` (and `R-Mod` when `R` commutative), with `Ext^0 = Hom`, long exact sequences from `D` triangles, and functoriality `Ext^n: R-Mod^{op}×R-Mod → R-Mod`. Need `M.rhom(N) : D(Ab)` and `M.ext(n,N) : Ab` on the module objects in `D`, not a free `ext(M,N,n)` with no derived parent. Requires `InjectiveResolution` and `KInjective` presentation; Yoneda `Ext` via extensions is comparison, not replacement.

* Left-derived tensor: `⊗_R: R-Mod × R-Mod → R-Mod` (or `Mod-R × R-Mod → Ab`) right exact; its left derivation `⊗^L_R: D(R-Mod) × D(R-Mod) → D(R-Mod)` (resp. `D(Mod-R)×D(R-Mod)→D(Ab)`) via flat / projective / `K`-flat resolutions `P^• → M`, `M⊗^L N = P^•⊗ N` total complex. Then `Tor^R_n(M,N) = H^{-n}(M⊗^L N) = L_n(⊗)(M,N) : Ab` (homological grading `Tor_n = H_n`), with `Tor_0 = ⊗`, balanced via either argument's resolution, long exact sequences, and base-change compatibility. Need `M.derived_tensor(N) : D(R-Mod)` object `M⊗^L_R N` and `M.tor(n,N) : Ab` on the module objects, with `⊗^L` as bifunctor on `D`, not a bare `tor(M,N)`.

* Derived tensor products especially: need `⊗^L` as symmetric monoidal structure on `D(R-Mod)` when `R` commutative (unit `R`, associator, braiding from complexes), internal Hom `RHom` right adjoint to `⊗^L` (`Hom_D(L⊗^L M,N) ≅ Hom_D(L,RHom(M,N))`), projection formula and base-change for `R→S`, and for schemes `L f^*` / `⊗^L_{O_X}` on `D(QCoh(X))`. All `HH(A)=A⊗^L_{A^e} A` and `RΓ`, `R f_*` compatibility above must compose through this same `⊗^L`/`RHom` machinery, not a parallel `hochschild_tensor`.

* In concrete computable cases (finite projective resolutions over `ZZ`, `k[x]`, `k[x]/(x^n)`, PID) `Ext` and `Tor` must be explicitly computable via the resolution and return owned modules with presentation and class maps, and verify `Ext^1(Z/n, Z/m)=Z/gcd(n,m)` etc. For general `R-Mod`, `Ext`/`Tor` retained as formal derived objects with known type.

Intended owners: `categories/derived/derived_category.py` (`D(R-Mod)` with `qis` localization, `H^n`), `categories/homological/ext_tor.py` (`RHom`, `Ext^n = R^n Hom`, `⊗^L`, `Tor_n = L_n(⊗)` via `K`-injective/`K`-flat resolutions), `categories/derived/tensor_product.py` (`derived_tensor_product` as monoidal on `D`). Not a free `Ext(M,N)` or `Tor(M,N)` — `M.rhom(N)`, `M.ext(n,N)`, `M.derived_tensor(N)` / `M.tensor_L(N)` on the module/complex objects in `D(R-Mod)`, with `D(Ab)` / `D(R-Mod)` as the ambient.

## Intake: https://www-fourier.univ-grenoble-alpes.fr/~sergerar/Kenzo/kenzo-demo.html — functionality — 2026-09-15 — verbatim

Kenzo (Sergeraert et al., EAT→Kenzo, incl. Dousson, Romero, Siret) implements Constructive Algebraic Topology via effective homology. Demo page http://www-fourier.univ-grenoble-alpes.fr/~sergerar/Kenzo/kenzo-demo.html shows three computations from actual Lisp listing on PC Isabelle (GDR Medicis), with file-list 36 modules: classes, macros, chain-complexes, effective-homology, homology-groups, cones, tensor-products, coalgebras, cobar, algebras, bar, simplicial-sets/mrphs, suspensions, disk-pasting, cartesian-products, eilenberg-zilber, kan, simplicial-groups, fibrations, loop-spaces, classifying-spaces, k-pi-n, serre, whitehead, etc.

* `H5(Ω^3(Moore(Z/2,4))) = Z/2^5` — Moore space `Moore(Z/2,4)` as simplicial set `m` via `(moore 2 4)`, then `o3m = loop-space(m,3)` as simplicial group `[K30 Simplicial-Group]`, then `(homology o3m 5)` computes boundary matrices in dimensions 5 (rank 23) and 6 (rank 53) via effective homology → 5 copies `Z/2` in 2 minutes.

* `H5(ΩΩ(S^3 ∪_2 D^3)) = Z + Z/2^6` — `s3 = sphere 3` → `os3 = loop-space(s3)` → attach 3-disk `D^3 = Δ^3` with faces 0,2 identified to fundamental simplex of loop space, faces 1,3 collapsed → space `S^3 ∪_2 D^3` (attach by degree 2), then double loop `ΩΩ(...)` and `(homology ... 5)` gives `Z + Z/2^6` in 40 seconds.

* `π7(P∞R/P2R) = Z/2 + Z/4` — `P∞R` has cellular model with one cell `E_n` each dimension, `P3 = r-proj-space 3` as `P∞R` collapsed 2-skeleton; verify `H_*(P3)` to dim 9 then iterative Postnikov/Whitehead fibrations: `ch5 = chml-clss(x4,5)` cohomology class degree 5 → `f5 = z2-whitehead(x4,ch5)` fibration `[K249 Fibration]` → `x6 = fibration-total(f5)` → `(homology x6 6)` gives `π6(P3)=Z/2` in 1s, repeat to `x?` with `ch6` etc. to `π7 = Z/2+Z/4` in 20 hours total; also examples `π4(Σ K(A4,1)) = Z/12` vs literature `Z/4` (Mikhailov-Wu correction) and generalizations listed in Kenzo overview.

What generalizes: hard code is choice of spaces (`Moore(Z/2,4)`, `S^3∪_2 D^3`, `P∞R/P2R`); method is general effective homology for any locally effective simplicial set.

## How Kenzo generalizes — what is new vs intake — verbatim — 2026-09-15

Hard codes are data (particular spaces), not method. Existing intake already has: CW complexes `K = (K^0⊂K^1⊂…)` with attaching maps `φ_α: S^{n-1}→K^{n-1}` and cellular `C_*(K)` finite effective chain complex; static DB `π_{n+k}(S^n)` (Hopf η,ν,σ, Whitehead); `ZZ^n`-GrMod complexes/double/SerreSS for finite sparse `E2`; computable `π1(X,x)=π1(K)` via van Kampen on 2-skeleton and `H_*` via `C_*` for concrete varieties via analytification. None of that computes homology of *infinite* complexes such as `Ω^3 Moore`, `Ω^n X`, `K(π,n)`, `X^I`, or arbitrary fibrations — `C_*(Ω^3 Moore)` has infinitely many non-degenerate simplices in degree 5 (rank 23 after reduction vs. infinite before).

What Kenzo does that is new and belongs in preamble:

**1. Effective homology as object** — not method. Object with effective homology is triple `(X, EC, ε)` where `X : sSet` (locally effective simplicial set: each `X_n : Sets` and face/degeneracy are computable), `C_*(X) : Ch_{ZZ}` its normalized chain complex (possibly infinite type), `EC : Ch_{ZZ}` effective (`EC_n` finitely generated free finite rank in each degree with computable differential/boundary matrices), and `ε : C_*(X) ⇔ EC` strong chain equivalence — span of two reductions `C_*(X) ⇐ Ĉ ⇒ EC`. Reduction `ρ = (f,g,h)` with `f: C→D`, `g: D→C`, `h: C→C_{+1}` satisfying `fg=id_D`, `gf + dh + hd = id_C`, `fh=0`, `hg=0`, `hh=0`. Perturbation lemmas (Basic BPL, Easy EPL) transfer reductions along twisting cochains `t: C→A` or differentials `δ`. This is the category `EffHom_sSet` with forgetful `U: EffHom→sSet` and `EC: EffHom→Ch^{eff}`. Intake has no such object; it has only finite CW `C_*`.

**2. Simplicial Kan model** — `sSet` with `Kan` axiom (horn fillers) via simplicial groups `G(X)=Kan loop group` and `W̄(G)` classifying space. Functors `G: sSet_* → sGrp` and `W̄: sGrp → sSet_*` with `G ⊣ W̄` and `Ω|X| ≃ |G X|` geometric. Operations `suspension Σ`, `cone`, `disk-pasting`, `cartesian-product` `X×Y` with Eilenberg-Zilber reduction `C_*(X×Y) ⇔ C_*(X)⊗C_*(Y)` and twisted Eilenberg-Zilber for twisted cartesian product `E = F ×_τ B` (fibration with twisting operator `τ: B_{n+1}→G_n` satisfying Kan condition). File modules 16-34 own this. Intake has `Top` CW colimits but not `sSet` Kan or `τ`.

**3. Fibrations with effective homology** — Serre fibration `F ↪ E → B` as `E = F ×_τ B` with structure group `G` acting on `F`; chain level `C_*(E) ≅ C_*(F) ⊗_t C_*(B)` twisted tensor product with differential `d = d_F⊗1+1⊗d_B + perturbation δ_τ`. Effective homology of base `B` and fiber `F` → effective homology of total `E` via twisted Eilenberg-Zilber + BPL (Kenzo `fibration-total` object with its `efhm`). Intake mentions Serre SS only as `E2=H_*(B)⊗H_*(F) ⇒ H_*(E)` finite/sparse determinable; Kenzo's is constructive cycle-level reduction, not spectral sequence table.

**4. Loop/classifying effective homology** — `Ω X = G X` loop space as simplicial group (Kan) with cobar construction at chain level: `C_*(Ω X)` effective via `Ω C_*(X)` cobar on coalgebra `C_*(X)` (modules 12-15 bar/cobar, coalgebras). Iterated loops `Ω^n X` require iterated cobar with effective homology at each step — demo's `Ω^3 Moore(Z/2,4)` is this iteration. Classifying `B G = W̄ G` similarly via bar construction. No finite CW model exists for `Ω^n X` in general; effective homology is the only computable model.

**5. Eilenberg-MacLane effective homology** — `K(π,n)` via `k-pi-n` module: Dold-Kan + bar construction inductively, with `EC` effective and Smith normal form `smith` for homology invariants `H_q(K(π,n))`. Prerequisite for Postnikov k-invariants and for H_{*} of EM spaces in towers.

**6. Whitehead/Postnikov tower for π_n** — For simply connected finite `X : sSet` with effective homology, Kenzo builds Whitehead tower `⋯→X_{n+1}→X_n→⋯→X_1=X` where `X_{n+1} = homotopy fiber of k-invariant κ_n ∈ H^{n+1}(X_n; π_n(X))` classified by `k-pi-n` twisting. Each `X_n` gets effective homology via fibration 3; then `π_n(X) = H_n(X_n)` as `Ext`? Actually `π_n = H_n(F_n)` where `F_n` fiber, computed via homology of effective complex `EC(X_n)` in that degree using `homology-groups` Smith. Demo's `π7(P∞R/P2R)` and `π4(ΣK(A4,1))` are this method (Xavier Dousson thesis). Intake has only `π1` via 2-skeleton + `π_{*}(S^n)` DB lookup; it cannot compute `π7` of arbitrary finite complex — this functor `π_n: sSet^{1-conn,eff} → Ab` is new. Requires `H^{n+1}(-;π)` model via Eilenberg-MacLane effective.

**7. Discrete vector fields** — Kenzo 1.1.8 upgrade (Forman) improves reductions for Eilenberg-Zilber and `K(π,n)` effective homology by Morse reductions `C → C^c` via admissible vector field `V` on cellular basis, with `f,g,h` from `V`. This is new discrete Morse category `DVF(Ch)` not in intake.

**8. Integration with derived functors** — Effective homology core is exactly derived tensor products: `C_*(X×_τ B) ≃ C_*(F) ⊗^L_{C_*(G)}`? More precisely `C_*(F×_τ B) ≅ C_*(F)⊗_t C_*(B)` with twisted differential = `C_*(F)⊗^L C_*(B)` perturbed, and cohomology operations `Ext, Tor` over `ZZ` via effective chain models feed homological algebra `Tor, Ext` already noted but now with concrete topological `⊗^L`. Intake's `Derived Hom/tensor — Ext,Tor,D(R-Mod)` with `R=ZZ` and `⊗^L` as monoidal on `D(ZZ-Mod)` is the algebraic owner; Kenzo's `EffHom, Bar, Cobar, EZ` are topological adapters that `⊗^L` must consume — `EC ⊗^L EC'` effective computes `Tor` over chain algebras.

**What does not generalize without new math**: General `X` must be simply connected and with effective homology presented; non-nilpotent/unbounded homotopy requires additional spectral sequence convergence not implemented; real coefficients `R` vs `ZZ` Smith needs PID; `π_n(X)` for non-finite `X` (e.g. infinite CW) needs local effectiveness hypothesis to stay in `EffHom`.

## Fundamental semantic language for Kenzo generalization — verbatim — 2026-09-15

For `EffHom / loop / Postnikov` to be statable, these must exist as categories/functors — not data `Moore(Z/2,4)`:

**Base**
* `Sets`, `NN` — degrees `n : NN`, ranks `rank EC_n : NN`
* `sSet : Cat` — simplicial set `X = (X_n, d_i 위원, s_i)` object; `sSet_*` pointed version `*∈X_0`; `Kan(sSet)⊂sSet` subcategory where every horn `Λ^k[n]→X` has filler
* `sGrp : Cat` — simplicial group `G`, underlying `G_n : Groups` with simplicial structure; forgetful `U: sGrp→sSet` via underlying Kan complex
* `Ch(R) : AddCat` — chain complexes `C = (C_n, d_n: C_n→C_{n-1})` over `R=ZZ` (more generally `R : CommRings`), with shift `[1]`, cone `Cone(f)`, tensor `C⊗D`, internal hom

**Reductions / effective homology**
* `Red(C,D) : Sets` — reduction `ρ=(f,g,h)` as above, with axioms `fg=id`, `gf+dh+hd=id`, `fh=hg=hh=0` (chain homotopy `h`); composition and transport
* `StrongEquiv(C,EC)` — strong equivalence `C ⇐ Ĉ ⇒ EC` span of two reductions; object `EC : Ch^{eff}` effective meaning `EC_n = R^{rank_n}` free finite rank and `d_n` given by finite matrix `Mat_{rank_{n-1}×rank_n}(R)` computable
* `EffHom(sSet)` — objects `(X, ε_X)` where `ε_X: C_*(X)⇔EC_X` strong equivalence; morphisms `f: X→Y` in `sSet` lift to `C_*(f): C_*(X)→C_*(Y)` compatible with `ε`; forgetful `U(X,ε)=X`, `EC(X,ε)=EC_X : Ch^{eff}`. Interface is `X.effective_homology() → (EC,ε)` not free `effective_homology(X)`
* Perturbation `δ: C→C_{*-1}` with `(d+δ)^2=0` small (`id+δh` invertible); Basic Perturbation Lemma `BPL(ρ,δ) → ρ' : (C,d+δ) ⇔ (D,d'+δ')` and Easy `EPL` — functors `PertRed : Red×Pert → Red`

**Simplicial / Eilenberg-Zilber**
* `Susp(X), Cone(f), DiskPasting, CartProd(X,Y)` — constructions in `sSet`; `C_*: sSet→Ch` normalized chain functor (Dold-Kan normalized)
* Eilenberg-Zilber `EZ: C_*(X×Y) ⇔ C_*(X)⊗C_*(Y)` reduction (Alexander-Whitney `f`, shuffle `g`, Shih `h`); twisted EZ `tEZ(τ): C_*(F×_τ B) ⇔ C_*(F)⊗_t C_*(B)` where `⊗_t` has twisted differential `δ_τ` from twisting cochain `τ: C_*(B)_{*+1}→C_*(F)_*` / twisting operator `τ: B_{*+1}→F_*`
* Bar `B A` and cobar `Ω C` for dg algebra `A` and dg coalgebra `C`: `B A = T^c(s\bar A)` coalgebra, `Ω C = T(s^{-1}\bar C)` algebra — objects in `dgAlg/dgCoalg`; `C_*(G X) ≃ Ω C_*(X)` as `dgAlg` equivalence (Adams) underlying loop-space effective homology

**Fibrations**
* `Fibration = (F, B, G, τ, E=F×_τ B)` where `G : sGrp` acts on `F`, `τ: B→G` twisting operator satisfies `d0 τ(b)=τ(d0 b)·∂ b` etc.; projection `p: E→B` Kan fibration with fiber `F`; `E.total()` object of `sSet` with `efhm` from base+ fiber `efhm` via `tEZ+BPL`
* `LoopSpace(X) = G X : sGrp` and `ClassifyingSpace(G)=W̄G : sSet_*` with `G ⊣ W̄` adjunction `Hom_{sGrp}(G X, H) ≅ Hom_{sSet_*}(X, W̄H)`; iterates `Ω^n X = G^n X` as `sGrp`/`sSet` with `EC(Ω^n X)` via iterated `Ω` cobar + `BPL`

**Eilenberg-MacLane / classifying**
* `K(π,n): AbGroups×NN → sSet^{eff}` with `π_n(K(π,n))=π`, `π_{≠n}=0` and `EC(K(π,n))` effective via bar inductively `K(π,n)=B K(π,n-1)` (n>1) or standard resolution (`K(Z,1)=S^1` etc.); homology `H_*(K(π,n))` via Smith on `EC`
* `Smith : Mat_{m×n}(ZZ) → diag(d1|d2|…)` invariant factors for `H_n(EC)` — `H_n(EC)= ZZ^{rank}` ⊕ ⊕_i `ZZ/d_i` from `d_n` boundary matrices `Mat(R)` in `Ch^{eff}`

**Postnikov / Whitehead tower**
* `Postnikov(X): sSet^{1-conn}→Tower` where `X^{(n)}` with `π_{>n}(X^{(n)})=0`, `π_{≤n}=π_{≤n}(X)` and fibration `K(π_{n+1}, n+1)↪X^{(n+1)}→X^{(n)}` classified by k-invariant `κ_n∈H^{n+2}(X^{(n)};π_{n+1})` as cohomology class `[c]∈H^{n+2}(EC(X^{(n)}))` represented by twisting cochain; dually Whitehead `X⟨n⟩`  (n-1)-connected cover with same `π_{≥n}`
* Functor `π_n: sSet^{1-conn,eff}→Ab` via `π_n(X)=H_n(X⟨n⟩)` or `H_{n+1}(X^{(n+1)}, X)`; computable as `homology( EC(X⟨n⟩), n )` via Smith — Kenzo's `z2-whitehead`, `fibration-total`, `homology`

**Not fundamental**
* `Moore(Z/2,4)`, `S^3∪_2 D^3`, `P∞R/P2R`, `rank EC5=23`, `shift`, `n=4`, `2 minutes/20 hours`, matrices in `C_*(X)` — elements/morphisms in above
* `φ_α: S^{n-1}→K^{n-1}` CW attaching (already intaken) is special case of `sSet` cell attachment `Δ^n/∂Δ^n→X`; effective homology reduces to that when `C_*(X)` already effective

## Fundamental semantic language for stable/characteristic/chromatic machinery — verbatim — 2026-09-15

For Kenzo's `π_*, Adams, BP` to be statable without coding by fiat, these must exist as categories/functors — not numbers `ΣS^n=S^{n+1}` or a bare `steenrod_square(n)` function:

**Homology theories**
* `HomologyTheory: HoTop_* → GrAb` as functor satisfying Eilenberg-Steenrod axioms (homotopy, excision, exactness, dimension) for singular/simplicial models `H^{sing}_*(X;R)=H_*(C^{sing}_*(X)⊗R)` via `C^{sing}_*: sSet→Ch(R)` normalized / Moore complex, vs. extraordinary theories `E_*: HoTop_*→GrAb` (stable, wedge, suspension isomorphism `E_n(X)≅E_{n+1}(ΣX)` without dimension axiom); cohomology `E^*: HoTop_*^{op}→GrAb`. Reduced vs. unreduced as `Ẽ_*(X)=ker(E_*(X)→E_*(pt))`. Object `E_*` is the theory, not its value on a space.

**Moore, Eilenberg-MacLane, classifying**
* `Moore(G,n): Ab→HoTop_*`, `H̃_i(Moore(G,n))=G` if `i=n` else `0` (via `M(G,n)= cone` on Moore presentation `F1→F0→G`); `K(π,n): Groups/Ab→HoTop_*` with `π_n=K(π,n)=π` else `0` and `EC(K(π,n))` effective as already intaken via `B^n K(π,0)` bar iteration; `BG = B G = W̄(N G)` classifying space `G : Groups→HoTop` with universal bundle `EG→BG` `EG` contractible and `Ω BG ≃ G` as `H-group`, functor `B: sGrp→sSet_*` already in Kenzo layer, now as `B: Grp(Top)→HoTop`. Distinguish `K(π,n)=B^n π`.

**Model categories**
* `ModelCat : Cat` with classes `W` (weak equivalences, 2-of-3), `Cof`, `Fib` satisfying lifting `Cof ⋔ Fib∩W`, `Cof∩W ⋔ Fib` and factorization `f = p∘i` with `i∈Cof∩W, p∈Fib` etc. Examples: `sSet` (Kan-Quillen: `W`=weak homotopy equivalences on realization, `Cof`=monomorphisms, `Fib`=Kan fibrations), `Top` (Serre/Quillen), `Ch(R)` (projective: `W`=quasi-isomorphisms `qis`, `Cof`=degreewise split monos with projective cokernel, `Fib`=degreewise epis). Homotopy category `Ho(M)=M[W^{-1}]` localization as `∞-categorical` localization; derived category `D(R)=Ho(Ch(R))`. Quillen adjunction `F: M⇄N:U` with `F(Cof)⊂Cof, U(Fib)⊂Fib` and derived adjunction `LF ⊣ RU` on `Ho`.

**Derived / homotopy categories already intaken but made explicit**
* `D(R-Mod)=Ch(R-Mod)[qis^{-1}]` and `D(R)=Ho(Ch(R))` triangulated (`shift [1]`, cones, distinguished triangles `X→Y→Cone→X[1]`); `HoTop_* = Top_*[WHE^{-1}]`, `Ho(sSet)=sSet[W^{-1}]` via `|-| ⊣ Sing`. Interface `L f^*, R f_*, ⊗^L, RHom` already intaken in derived `Ext/Tor` lead — now as left/right derived of Quillen functors on model categories, not ad-hoc free resolutions.

**Loop / suspension / smash (pointed)**
* `Σ: HoTop_*→HoTop_*` via `ΣX = S^1∧X = (I∧X)/(0∧X ∪1∧X)` as homotopy pushout `*←X→CX` (cone), `Ω: HoTop_*→HoTop_*` via `ΩX = Map_*(S^1,X)` as homotopy pullback `*→X←X^I` (path space). Adjunction `Σ ⊣ Ω` as homotopy adjunction `[ΣX,Y]≅[X,ΩY]` graded. Smash `∧: HoTop_*×HoTop_*→HoTop_*` monoidal with unit `S^0`, associator, braiding; internal hom `Map_*`. Computable is not fiat `ΣS^n = S^{n+1}` — must exhibit `sSet` model `ΣΔ^n/∂Δ^n ≅ S^{n+1}` via simplicial suspension `ΣX = (X×Δ^1)/(X×∂Δ^1 ∪ *×Δ^1)` with `EC(ΣX)` via `EC(X)` shift `C_*(ΣX)≅C_*(X)[1]` effective, not a table entry.
* `sSet_*` models: `Σ = S^1∧-`, `Ω = G ⊣ W̄` Kan loop group equivalence already in Kenzo section, now as pointed simplicial `Σ ⊣ Ω` Quillen.

**Bar / cobar**
* `Bar B: dgAlg→dgCoalg` `B A = T^c(s\bar A)` with coproduct deconcatenation and differential `d_B = d_A + product`, `Cobar Ω: dgCoalg→dgAlg` `Ω C = T(s^{-1}\bar C)` with differential `d_Ω = d_C + coproduct`; adjunction `Ω ⊣ B` and `C_*(G X) ≃ Ω C_*(X)` (Adams) and `C_*(B G) ≃ B C_*(G)`, both as `EffHom` reductions perturbed via BPL — loop effective homology 4 already, now as `Ho(dgAlg)≃Ho(dgCoalg)` equivalence behind spectra.

**Towers**
* `PostnikovTower(X) = (X^{(n)}, p_n: X^{(n)}→X^{(n-1)})` inverse tower with `X^{(n)}` n-truncated (`π_{>n}=0`, `π_{≤n}=π_{≤n}(X)`), fiber `K(π_{n+1}, n+1)` classified by k-invariant `κ_n∈H^{n+2}(X^{(n)};π_{n+1})`; `X ≃ holim X^{(n)}`. Dually `WhiteheadTower(X)` `⋯→X⟨n+1⟩→X⟨n⟩→⋯→X` with `X⟨n⟩` (n-1)-connected cover, `π_{≥n}=π_{≥n}(X)`, `π_{<n}=0`. More generally infinite fibration tower `⋯→E_{n+1}→E_n→⋯` and cofibration tower `X_0→X_1→⋯` as objects `Tower(Fib)=Fun(N^{op}, M)` / `Tower(Cof)=Fun(N,M)` with `holim/hocolim`. Killing homotopy `X→X'` with `π_{>n}(X')=π_{>n}(X)`, `π_{≤n}=0` via cell attachment `X' = X ∪_{representative of π_n} D^{n+1}` iteratively.

**Homotopy fibers/cofibers, skeleta, maps**
* `Skeleta` `sk_n X`, `cosk_n X` in `sSet/CW` as `n`-truncation via `Δ_{≤n}` left Kan extension; `CW_n ⊂ CW_{n+1}` via pushout `∐_α S^{n-1}→K^{n-1}` already intaken, now with `CWMaps: CW→CW` whose cellular approximation is functor. `SimplicialMaps` similarly. Homotopy fiber `hofib(f)= X×^h_Y * = X×_Y Y^I` and cofiber `hocofib(f)= Y ∪^h_X * = Y ∪_X X∧I`; fiber sequence `F→E→B` vs cofiber `X→Y→C_f` as distinguished triangles in `Ho(M)`.

**Graded structures**
* `GrAb_{ZZ^n}, GrRings, GrMod, GrAlg` with bigraded `E^{p,q}_r`, `π_{p+q}(X)` bigraded, `Ext^{p,q}, Tor_{p,q}` as usual. More generally `G-GrMod` for `G: AbGroups` (e.g. `ZZ`, `ZZ/2`, `ZZ^n`, `RO(G)`) as functor `Gr: Ab→Cat` `M=⊕_{g∈G} M_g` with `G`-graded tensor `M⊗N` in degree `g+h`. Needed for `E_2^{p,q}=H^p(B;H^q(F))` etc.

**π_* as graded Lie**
* `π_*(X)=⊕_{n≥1}π_n(X)` as graded Lie algebra under Whitehead product `[α,β]∈π_{p+q-1}` with Jacobi and graded antisymmetry, and Toda brackets `⟨α,β,γ⟩⊂π_{p+q+r+1}` secondary operation where `αβ=0, βγ=0` as coset of indeterminacy; higher Toda operations. Structure maps `[-,-]: π_p⊗π_q→π_{p+q-1}` as `HoTop_*(S^p∧S^q→S^{p+q-1})` via universal Whitehead.

**Sullivan minimal models**
* `DGA_{Q}^{≥0}` Sullivan algebras `(Λ V,d)` with `V=⊕_{n≥1}V^n` graded vector space, `Λ` free graded-commutative, `d` decomposable and nilpotent filtration; minimal `d(V)⊂Λ^{≥2}V` and `V` well-ordered so `d(v_i)∈Λ(V_{<i})`. Functor `A_{PL}: sSet→DGA_Q` (PL forms) and minimal model `M_X → A_{PL}(X)` quasi-isomorphism with `M_X = (ΛV,d)` minimal and `V^n ≅ Hom(π_n(X),Q)` for nilpotent finite-type `X`; model category `DGA_Q` with `W=qis`. Not a free `minimal_model(X)` returning matrices — object of `Ho(DGA)` with `π_*⊗Q` read off `V`.

**Stabilization / spectra**
* `Stab(C)` stabilization of pointed `∞-category` C with finite limits/colimits as `Sp(C)=lim(⋯→C →Ω C →Ω C)` or `Exc_*(S^{fin}_*, C)` excisive functors; universal property `Fun^{lex}(Sp(C),D)≃Fun^{lex}(C,D)` stable. For `C=Top_*`, `Sp = Sp(Top_*)` is category `Spectra` stable, with `Σ^∞: Top_* ⇄ Sp: Ω^∞` stabilization adjunction `Σ^∞ ⊣ Ω^∞` and `Σ^∞ X = (Σ^n X)_n` sequential spectrum. Models: sequential spectra `E=(E_n, σ_n: ΣE_n→E_{n+1})` vs `Ω`-spectra `σ^♭: E_n→ΩE_{n+1}` weak equivalence, symmetric spectra with `Σ_n` action. Sphere spectrum `S = Σ^∞ S^0`, `S^n = Σ^∞ S^n` as `S` shift `S[n]`. Suspension spectrum `Σ^∞_+: Top→Sp` as `Σ^∞(X_+)` unreduced (`X_+=X⊔*`), left adjoint to `Ω^∞` on unpointed. Smash `∧: Sp×Sp→Sp` symmetric monoidal with unit `S`, internal hom `F(-,-)`.
* `Ho(Spectra)` triangulated with shift `Σ = S^1∧-`.

**E_∞ / ring spectra, modules, mod p reduction**
* `CAlg(Sp)=E_∞-Alg` as commutative algebra objects in `Sp` via `E_∞` operad `Comm_{E_∞}`; `Mod_R` for `R: E_∞` as `Sp^{R-mod}` stable symmetric monoidal `⊗_R`. Examples: `S, HZ, HF_p, MU, MO, MSO, K, BP, E_n`. Mod p reduction: at module level first `M/p = M⊗^L_Z F_p : D(Z-mod)` via two-term `Z→^p Z`, then `A/p = A⊗^L_{E_∞} HF_p : CAlg_{HF_p}` for `A: CAlg_{HZ}` or `A: CAlg_S`; more generally `R`-algebra `A` at prime `𝔭∈Spec R` via `κ(𝔭)=Frac(R/𝔭)` or `R_𝔭` completion `A_{𝔭}=A⊗^L_R R_𝔭` and cofiber `A→A_{𝔭}→A/𝔭^∞`. Need `⊗^L` already intaken as `D(R-Mod)` monoidal.

**Steenrod / Adams / characteristic**
* `Steenrod algebra A = A_2, A_p : GrAlg_{F_p}` with `A = End_{Sp}(HF_p⊗HF_p)` ≅ `H^*(HF_p;F_p)` and basis `Sq^i` (`p=2`) / `P^i, β` (`p>2`) with Adem relations and Cartan `Sq^k(xy)=Σ_{i+j=k}Sq^i(x)Sq^j(y)`; action `A ⊗ H^*(X;F_p)→H^*(X;F_p)` as `Dyer-Lashof` unstable module over `A`. `CohomologyOperations: HoTop^{op}→GrSets` `H^n(-;F_p)→H^{n+k}(-;F_p)` represented by `K(F_p,n)`.
* `Adams spectral sequence` `E_2^{s,t}=Ext^{s,t}_{A}(H^*(X),F_p) ⇒ π_{t-s}(X)^{∧}_p` (stable for `X: Sp`, unstable via `Ext` over Lambda algebra); `Adams resolution` `X→I^•` with `I_s = HF_p∧\bar{HF_p}^{∧s}∧X` tower `⋯→X_{s+1}→X_s` whose `E_1 = π_*(I_s/I_{s+1})`. Next layers: `Adams-Novikov SS` `E_2^{s,t}=Ext^{s,t}_{MU_*MU}(MU_*,MU_*(X))⇒π_{t-s}(X)` with `MU_*MU` Hopf algebroid, `BP` Brown-Peterson `BP_*=Z_{(p)}[v1,…]` (`|v_n|=2(p^n-1)`) as summand of `MU_{(p)}` via Quillen idempotent, `BP_*BP` and `Adams-Novikov` for `BP`. Division algebras over `Q` via Brauer `Br(k)=H^2(Gal, \bar k^×)`, central simple.

**Cobordism / characteristic classes**
* `Cobordism rings` `MO_* = π_*(MO)` unoriented (`MO = Thom(O)` with `π_*(MO)=F_2[x_i]`), `MU_*` complex (`MU = Thom(U)`, `π_*(MU)=Z[x_1,x_2,…]` `|x_i|=2i`, Lazard), `MSO_*`, `MSpin`, `MSp`. Thom spectrum `M(G)=Thom(EG×_G R^n)` and Pontryagin-Thom `Ω^{fr}_* = π_*(S)`, `Ω^{un}_*=π_*(MO)` etc.
* `Characteristic classes` as natural transformations `H^*(BO)→H^*(-)` etc.: Stiefel-Whitney `w_i∈H^i(BO;F_2)` via `BO = colim Gr(k,∞)`, `w = Σw_i = ∏(1+x_i)` total, Whitney sum `w(ξ⊕η)=w(ξ)∪w(η)`, Pontryagin `p_i∈H^{4i}(BSO;Z[1/2])` via Chern `p_i(ξ)=(-1)^i c_{2i}(ξ⊗C)`, Chern `c_i∈H^{2i}(BU;Z)`, Euler `e∈H^n(BSO(n))`. Numbers `⟨∏w_{i_k}^{e_k} ∪ μ_X, [X]⟩∈F_2` and `⟨∏p_j^{e_j}, [X]⟩∈Z` as `CharNumbers: Bordism→F_2/Z` detecting bordism class (Thom). More general `E^*(BG)` characteristic maps for `G=T, U(n), O(n), etc.` via `H^*(BG;R)` / `E^*(BG)` as `Cohomology of classifying`.

**What else needs general + bigraded**
* `E∞` pages `E_r^{p,q}` as objects of `GrMod_{ZZ^2}(R)` already intaken bigraded, now with differentials `d_r: E_r^{p,q}→E_r^{p+r, q-r+1}` and convergence `E_∞^{p,q}=F^pH^{p+q}/F^{p+1}` for filtered `H^*`. Used in Serre, Atiyah-Hirzebruch `E_2^{p,q}=H^p(X; E^q(pt))⇒E^{p+q}(X)`, Adams `E_2^{s,t}`, Adams-Novikov `E_2^{s,t}`.

**Not fundamental**
* Specific `Sq^1(x)=βx`, `MU_*=Z[x1,..]` generator `x1=CP^1`, `π_*(S)=Z/24` etc. — elements `x_i: π_{2i}(MU)` and classes `w_i: H^i(BO)` as morphisms `BO→K(F_2,i)`, not new categories
* `ΣS^n≃S^{n+1}` must be proven as `|ΣΔ^n/∂|≅S^{n+1}` via `EC` shift, not table — instance of `Σ ⊣ Ω` on `sSet`

## Desired capability: Eilenberg-Moore sseq operationalized for effective computations — note 2026-09-15

Note the Eilenberg-Moore spectral sequence should be operationalized for effective computations — not a table of `E_2=E_∞` coincidences.

* EM is not a formal `E_2^{p,q}=Tor` display. For a (homotopy) pullback `E = X ×_B Y` of spaces over `B` with `B` 1-connected (more generally path-connected, nilpotent), and for a fibration `F ↪ E → B` as `E = F ×_B *`, the Eilenberg-Moore sseq is the spectral sequence of the two-sided bar construction `B(C_*(X), C_*(ΩB), C_*(Y))`:
  ```
  E_2^{p,q} = Tor^{H_*(ΩB)}_{p,q}(H_*(X), H_*(Y)) ⇒ H_{p+q}(X ×_B Y)
  Cotor^{H_*(B)}_{p,q}(H_*(X), H_*(Y)) ⇒ H_{p+q}(X ×_B Y)   (coalgebra form when B coaugmented)
  ```
  and cohomology `E_2^{p,q}=Ext^{p,q}_{H^*(B)}(H^*(X),H^*(Y)) ⇒ H^{p+q}(X×_B Y)` / `E_2^{p,q}=Ext_{H_*(ΩB)}^{p,q}` dual. Specialization to a fibration is `Y=*`. Without derived `Tor` over `H_*(ΩB)` / `Cotor` over `H_*(B)` and bar/cobar, this is not statable.

* Operationalized means: from `B,X,Y : sSet` with `B` effective (hence `C_*(B)` and `H_*(ΩB)` via cobar `ΩC_*(B)`), construct `B(C_*(X), C_*(ΩB), C_*(Y))` as effective chain complex via reductions, and compute `E_r^{p,q}` as objects of `GrMod_{ZZ^2}(R)` (`R=ZZ, F_p` via `smith` base-change) with explicit differentials `d_r: E_r^{p,q}→E_r^{p+r, q-r+1}` induced by bar filtration `F^pB = B^{≤p}` and perturbation `δ_τ`. Interface must be `(f: X→B, g: Y→B).eilenberg_moore(r) → E_r` and `E_r.differential(p,q)` and `E_r.next_page()` and convergence `E_∞^{p,q}=F^p H_{p+q}/F^{p+1}` as filtration quotient of `H_*(X×_B Y)` via `EC` of pullback `X×_B Y = X×_τ (ΩB) × Y` twisted product, not a bare list of groups.

* Effective computation requires: loop space effective homology `C_*(ΩB) ≃ ΩC_*(B)` already intaken (Kenzo `Ω` cobar + BPL), bar construction `B(A,M,N)=M⊗T(s\bar A)⊗N` with differential `d_B = d_M⊗1⊗1 +1⊗d_A⊗1+1⊗1⊗d_N + twisting from product/coproduct`, two-sided bar `B(R, C_*(ΩB), H_*(X))` etc., and the reduction `B(C_*(X),C_*(ΩB),C_*(Y)) ⇔ B(H_*(X),H_*(ΩB),H_*(Y))` via Eilenberg-Moore comparison when `B` 1-connected; differentials must be computable from `EC` boundary matrices via `smith` over `ZZ` or over `F_p` after `⊗^L F_p`.

* In easy cases when `H_*(B)` is free / `B` formal and `H_*(ΩB)` known, `E_2` already gives answer — but general case requires `d_r` for `r≥2` and must not declare `E_2=E_∞` by fiat. For concrete fibrations `K(Z/2,1)↪E→S^2`, `ΩS^n→PS^n→S^n` (path-loop), Postnikov fibrations `K(π,n+1)↪X^{(n+1)}→X^{(n)}`, the EM `E_2` via `Tor` must be returned as effective `GrMod` and `E_3, E_∞` via actual `d_2` from twisting cochain / Massey products, certifying the filtration on `H_*(E)` vs. direct `EC(E)` homology (agreement test).

* Requires: derived tensor already intaken `⊗^L : D(R-Mod)×D(R-Mod)→D(R-Mod)` with `Tor_{p,q}=H_{p+q}( -⊗^L -)` in graded context; `C_*(ΩB)` as dg algebra (`H_*(ΩB)=Ext_{C_*(B)}(R,R)`) via cobar; `B` as Reedy / model fibrant `B` so `X×_B Y` is `h×`; effective homology `ε_B, ε_X, ε_Y` for base/fiber/pullback. Without model category fibrancy `F ↪ E→B` (`Kan fibration` in `sSet`, Serre in `Top`) the pullback is not homotopy pullback and EM does not apply.

* Relation to prior leads: EM `E_2=Tor` is not a new `Tor`; it is the topological `Tor^{H_*(ΩB)}` instance of the same derived `Ext/Tor/D(R-Mod)` lead (`R=ZZ`) with `⊗^L_{H_*(ΩB)}`. Bar/cobar lead already provides `B/Ω`. Serre sseq lead already provides `E_r` interface; EM reuses that `SpectralSequence` object with `E_2^{p,q}=Tor` instead of `E_2^{p,q}=H^p(B;H^q(F))`, and with bar filtration instead of skeletal filtration. Do not build a second `SpectralSequenceEM` type duplicating `E_r`.

Intended owners: `categories/homotopy/eilenberg_moore.py` (`EilenbergMooreSpectralSequence` with `E_2 = Tor^{H_*(ΩB)}(H_*(X),H_*(Y))` / `Cotor^{H_*(B)}` via `Bar`, `E_r.next_page()`, convergence to `H_*(X×_B Y)`), delegating to `categories/topology/effective_homology.py` (`BPL` for `B(A,M,N)`), `categories/derived/tensor_product.py` (`Tor` as `⊗^L`), `categories/algebras/bar_cobar.py` (`Bar`, `Cobar`, twisting cochain `τ`), `categories/homotopy/model_categories.py` (`Kan fibration`, `h-pullback`). Not a free `eilenberg_moore(X,Y,B)` returning lists — `(X→B←Y).eilenberg_moore()` on the cospan in `Ho(sSet)` with `E_r^{p,q}` as `GrMod_{ZZ^2}` objects and differentials as morphisms, converging to `EC(X×_B Y).homology()`.

## Desired capability: hypercohomology and Čech cohomology operationalized and effective — note 2026-09-15

Also note that hypercohomology and Čech cohomology should similarly be operationalized and effective — not formal `H^i(X,F)` symbols or a bare `cech_cohomology(cover)` list.

* Hypercohomology is not `H^i(X,F)` for a single sheaf. For a complex of sheaves `F^• ∈ Ch(Sh(X))` (`Sh(X)=Sh(X_ét), QCoh, Ab, etc.`) on a site `X` with global sections `Γ(X,-): Sh(X)→Ab` and derived `RΓ: D(Sh(X))→D(Ab)`, hypercohomology is `H^i(X, F^•) = H^i(RΓ(F^•)) = R^iΓ(F^•) : Ab` with `RΓ` the total right derived of `Γ` via `K`-injective resolutions `F^• → I^•` (Spaltenstein) and `RΓ(F^•)=Γ(I^•)` as effective complex object `RΓ(F^•) : Ch(Ab)` / `D(Ab)`. Specialization to a single sheaf is `F[0]`; general `F^•` is needed for `R f_*(Ω^•_{X/S})` (Gauss-Manin) `H^k_{dR}=R^k f_*Ω^•`, `R f_*(Q_ℓ)` for constructible `ℓ`-adic, Hodge `RΓ(X, Ω^p)`, de Rham `RΓ_{dR}=RΓ(X, Ω^•_X)`, etc. Without `RΓ` as `D`, hypercohomology is not statable.

* Čech cohomology is the simplicial cover method that computes `RΓ` effectively. For a covering `U = {U_i → X}_{i∈I}` in site `(C_X,J)` (e.g. étale covering family, Zariski open cover, `sSet` hypercover), form Čech nerve `N(U)_p = ∐_{i_0<…<i_p} U_{i_0…i_p}` as simplicial object in `C_X` with `U_{i_0…i_p}=U_{i_0}×_X …×_X U_{i_p}` fiber product. For `F ∈ Sh(X)` define Čech cochains `Č^p(U,F)=∏ F(U_{i_0…i_p})` with Čech differential `d_Č: Č^p→Č^{p+1}` alternating sum of restriction maps `res_{k}: F(U_{i_0…\hat{k}…}) → F(U_{i_0…})`. Then `Č^•(U,F) : Ch(Ab)` and `Ȟ^p(U,F)=H^p(Č^•)`. For complex `F^•`, double `Č^{p,q}=Č^p(U,F^q)` with `d_Č + (-1)^p d_{F}` and total `Tot^•(U,F^•)`; hyper-Čech is `Ȟ^p(U,F^•)=H^p(Tot)`. This is the `U`-effective model of `RΓ(F^•)` when `U` is `F^•`-acyclic (Leray: `H^q(U_{i_0…}, F^r)=0` for `q>0`, or `U_{i_0…}` affine for `QCoh`).

* Operationalized and effective means: given `X : Sites` + `F^• : Ch(Sh(X))` (with `F^q` presented as `Sh` objects on site) + covering `U : CoveringFamily(X)` with `U_{i_0…}` effectively computable (e.g. affine opens `Spec R_{i_0…}`, étale `Spec S → X`), construct `Č^•(U,F)` / `Tot^•` as effective chain complex `EC(U,F^•) : Ch^{eff}` with finite-rank `EC_n` in each degree and explicit matrices `d_n: Mat`, via reductions from effective homology of the local sections `F(U_{i_0…})`. Interface must be `F^•.cech_complex(U) → Č^•`, `F^•.cech_cohomology(U,p) → Ȟ^p`, and `RΓ(F^•)` as `D` object with Čech-to-derived spectral sequence `E_1^{p,q}=Ȟ^q?` Actually `E_1^{p,q}=Č^p(U, H^q(F^•))` no — for hypercohomology `E_1^{p,q}=Ȟ^q?` Standard: `E_1^{p,q}= Č^p(U, H^q(F^•)) ⇒ H^{p+q}(X,F^•)` vs. `E_2^{p,q}=H^p(X, H^q(F^•)) ⇒ H^{p+q}` — the Čech-to-derived sseq `E_2^{p,q}=Ȟ^p(U, H^q(F^•)) ⇒ H^{p+q}(X,F^•)`. Must expose `E_r^{p,q} : GrMod` with `d_r` and convergence `E_∞^{p,q}=F^pH^{p+q}/F^{p+1}`, and test acyclicity: when `U` is `F^•`-acyclic, comparison `Ȟ^p(U,F^•) ≅ H^p(X,F^•)` as isomorphism `Tot(U,F^•) ⇔ RΓ(F^•)` via `Čech augmentation` `F^• → Č^•` quasi-isomorphism.

* Effective weakens finiteness: `Č^p` need not be finite — `∏_{i_0<…}` over infinite cover is not effective. Effective hypothesis is `U` finite cover (Zariski finite affine cover, finite étale cover, finite hypercover) and each `F(U_{i_0…})` effective (e.g. `QCoh` on affine `Spec R` has `Γ(U_{i_0…},F)=M_{i_0…} : R-mod` computable, `Sh` on finite simplicial nerve). Then `Tot` is finite double complex and `EC(Tot)` via `EC` of each `M_{i_0…}` + perturbation from nerve differentials `d_Č` as `BPL` twist on tensor with simplicial cochain `C_*(N(U))`.

* In easy effective cases when cover is finite affine and `F^q` is `QCoh` vector bundle / `Q_ℓ` lisse with `H^{>0}=0` on affines, `Ȟ^p(U,F)=R^pΓ(F)` directly and `Tot` collapse gives `RΓ(F^•)` as `Tot` with one filtration. For general `F^•` (e.g. de Rham `Ω^•_X` on smooth `X` with Hodge filtration) need `d_r` for `r≥2` and not declare `E_2=E_∞` by fiat. For concrete fibrations/pullbacks, Čech and Eilenberg-Moore interact: `Čech_{U}(R f_* F)` via hypercohomology base-change `RΓ(X,F) ≃ RΓ(S,R f_*F)`.

* Requires: site effective covering families `CoveringFamily(X,J)` with `J` via sieves already intaken plus `Nerve: Covering→sSet` (Čech nerve); `Sh(X)` abelian with `Γ` left exact and `RΓ` via `D(Sh)` injective already intaken in derived `R f_*` lead; derived tensor `⊗^L` for `Čech` Alexander-Whitney / Eilenberg-Zilber on overlaps `U_{i_0…}×`; effective homology `ε: C→EC` for each local `F(U_{i_0…})` via `EffHom` already intaken; model for hypercover `U_• → X` Kan hypercover in `sSet`/`Sites`. Without `EffHom` and `D`, hyper/Čech remain table lookups.

Intended owners: `categories/sheaves/hypercohomology.py` (`Hypercohomology` with `RΓ: Ch(Sh)→D(Ab)` → `H^i = H^i(RΓ)`, `RΓ(F^•).effective_complex()` via injective/`K`-injective + `BPL`), `categories/sheaves/cech.py` (`CechNerve(U) : sSet`, `CechComplex(Č^•(U,F^•)) : Ch`, `CechToDerivedSpectralSequence` with `E_2^{p,q}=Ȟ^p(U, H^q(F^•)) ⇒ H^{p+q}`), delegating to `categories/topology/effective_homology.py` (reductions for `Tot` perturbation), `categories/derived/derived_category.py` (`RΓ` as `RΓ = R(p_*)` from six-functor `R f_*` lead), `categories/topology/sites.py` (`Site`, `CoveringFamily`, `Nerve`). Not free `hypercohomology(X,F)` or `cech_cohomology(cover,F)` lists — `F^•.hypercohomology() → RΓ(F^•) : D` with `F^•.hypercohomology(i) → H^i`, and `U.cech_complex(F) → Č^• : Ch^{eff}` with `Ȟ^p` and `Čech→RΓ` comparison as quasi-isomorphism when acyclic.

## Desired capability: filtered complexes, standard filtrations, Hodge-Frölicher and Grothendieck sseqs, with computable degeneration — note 2026-09-15

Plus filtered complexes, and the standard filtrations (e.g. the stupid filtration, Hodge filtrations, etc). One also needs the Hodge-Frölicher sseq and the sseqs from Grothendieck's seminal algebraic paper. Ideally it should be possible to compute, sometimes, that a sseq degenerates on a specific page, purely from considerations regarding stabilization of differentials, zero or stabilized entries in certain gradings, etc.

* Filtered complex is not a bare `Ch` with a tag. Object ` (K^•, F) : FiltCh(Ab)` with `F^•` decreasing filtration `⋯ ⊃ F^p K^• ⊃ F^{p+1} K^• ⊃ ⋯` by subcomplexes, exhaustive `⋃F^p=K`, separated `⋂F^p=0` (or complete), finite or bounded variants; filtered maps `f: (K,F)→(L,F)` with `f(F^pK)⊂F^pL`. In non-abelian model stable setting, `Filt(Sp)` similarly. Interface `K.filtered()` and `K.filtration(p) → F^pK : Ch` with `F^pK/F^{p+1}K = gr_F^p K` associated graded.

* Standard filtrations as functors, not ad-hoc integers:
  - Stupid/bête `σ_{≥p}K` / `σ_{≤p}K` (naive truncation): `(σ_{≥p}K)^n = K^n` if `n≥p` else `0` (for decreasing) or `σ_{≤p}` dually; `σ` is the filtration whose `gr^p = K^p[-p]` single degree. Provides `sseq` that collapses at `E_1 = K`.
  - Hodge filtration `F^p Ω^{•}_{X/k}` on algebraic de Rham `Ω^{•}_{X/k}` as `F^p = Ω^{≥p}` (forms of degree ≥p), `gr_F^p = Ω^p[-p]`; conjugate filtration on same underlying `de Rham` with `F_{conj}` via Cartier; weight filtration `W` on mixed Hodge.
  Each is an object `FiltCh → FiltCh` with `gr` known.

* From a filtered complex, spectral sequence is object `E_r^{p,q}` with `E_0^{p,q}=gr_F^p K^{p+q}`, `E_1^{p,q}=H^{p+q}(gr_F^p K)`, differentials `d_r^{p,q}: E_r^{p,q}→E_r^{p+r,q-r+1}` induced by `d_K`, pages `E_{r+1}=H(E_r,d_r)`, abutment `E_∞^{p,q}=gr_F^p H^{p+q}(K)` as `GrMod_{ZZ^2}` with filtration quotients. Need `FilteredComplex.spectral_sequence() → SpectralSequence` with `E_r(p,q)`, `d_r` as morphisms `E_r^{p,q}→E_r^{p+r,q-r+1}` effective via `EC` when `gr_F^p K` and `K` effective, and `E_r.next_page()`.

* Hodge-to-de Rham / Frölicher (Hodge–Frölicher) sseq is the `F`-sseq for `K= RΓ(X, Ω^{•}_{X/k})` with Hodge filtration `F^pK = RΓ(X, F^pΩ^{•})` (`F^pΩ^{•}=Ω^{≥p}`):
  ```
  E_1^{p,q}=H^q(X, Ω^p_{X/k}) = H^{p+q}(gr_F^p) ⇒ H^{p+q}_{dR}(X/k) = H^{p+q}(X, Ω^{•})
  ```
  `d_1 = d_{dR}` on Hodge cohomology, higher `d_r` are the Frölicher differentials. Operationalized and effective when `X : Sch/k` smooth proper with finite affine Čech `U` and `Ω^p(U_{i0…})` effective; then `gr_F^p K = Tot(Č(U, Ω^p[-p]))` effective and `E_r` via `FilteredComplex` above with `EC` for each `Tot`. Degeneration at `E_1` (`Hodge degeneration`) means `d_r=0` for `r≥1` as morphism, not as numeric coincidence; `Frölicher inequality` `Σ dim E_1^{p,q} ≥ dim H_{dR}` becomes testable via `EC` ranks.

* Grothendieck's sseqs from his Tohoku / Hartshorne Residues / Leray (his seminal algebraic paper) are composite-functor sseqs:
  - Grothendieck composite `Γ = G∘F` with `F: A→B` left exact sending injectives to `G`-acyclic → `E_2^{p,q}=R^pG(R^qF(A)) ⇒ R^{p+q}Γ(A)` (`Filt` from Cartan-Eilenberg resolution `I^{•,•}` of `F(I^•)`).
  - Leray sseq for `f: X→Y` as instance `Γ = Γ(Y,-)∘f_*`: `E_2^{p,q}=H^p(Y, R^qf_*F) ⇒ H^{p+q}(X,F)` / `E_2^{p,q}=R^pf_*(R^qg_*F) ⇒ R^{p+q}(f∘g)_*F`.
  - Local-to-global Ext `E_2^{p,q}=H^p(X, Ext^q(F,G)) ⇒ Ext^{p+q}(F,G)` (`Γ = Hom(F,-)∘Γ`), and `Tor` analog `E^2_{p,q}=H_p(X, Tor_q)`.
  Interface same `FilteredComplex` from double complex of injective resolutions `I^{p,q}` / Čech double `Č^{p}(U, I^q)` — need `K`-injective `F^•→I^{•,•}` effective when site finite.

* Computable degeneration on a specific page, purely from stabilization of differentials, zero or stabilized entries, etc., means the sseq object must expose decision procedures:
  ```
  E_r.degenerates_at(r0) ⇔ ∀r≥r0 ∀p,q d_r^{p,q}=0 as morphism E_r^{p,q}→E_r^{p+r,q-r+1}
  E_r.collapses() ⇔ E_r = E_∞ as GrMod
  periphery bounds: if E_r^{p,q}=0 for p<0 or q<0 or p>n or q>m (first-quadrant, etc.) then d_r^{p,q}=0 automatically for r large
  stabilization: if for fixed (p,q) the groups E_r^{p,q} stabilize (E_{r+1}^{p,q} ≅ E_r^{p,q} via cycles = ker d_r and boundaries = im d_{r-?}) and all outgoing/incoming d_r into/out of that bidegree vanish because source/target is 0, then certify E_r^{p,q}=E_∞^{p,q}
  ```
  Implement as methods `E_r.is_zero(p,q)`, `E_r.differential_is_zero(p,q,r)` via `EC` matrix `d_r` on `E_r^{p,q}` computed from `Filt` cycles/boundaries (choose `EC` basis, compute `d_r` as `Mat_{rank_target × rank_source}(R)` and test `=0` as morphism, not as `rank` equality). Then `degenerates_at(r0)` checks all `(p,q)` in support box where `E_{r0}` non-zero has `d_{≥r0}=0` because either matrix is zero or source/target zero — purely effective grading/zero-entry reasoning. Do not declare degeneration by a single coinciding dimension `dim E_2 = dim abutment`; need `d_r=0` as maps.

* Effective weakens to exhaustive bounded filtrations (stupid, Hodge `0≤p≤dim X`, weight finite) where `FiltCh` has finite length `ℓ = max p - min p` and `E_1` has finite support box `0≤p≤ℓ`, so degeneration test is finite over `EC` box; for unbounded/infinite-lengthfiltrations (complete, non-exhaustive) retain formal `E_r` with known type but no finiteness claim.

* Requires: `FiltCh` with `F^p` decreasing, `gr_F^p`, `E_0` already needed for hypercohomology/Čech/Serre/EM/Frölicher sharing one `SpectralSequence` type (no duplicate `FrölicherSS`); effective homology `EC` for `Tot` of `Č(U, gr_F^p)` as above; model `RΓ` via `D(Sh)` for `X` site; Hodge data `Ω^p_{X/k} : QCoh(X)` with `F^p` on `Ω^{•}` as decreasing filtration by subcomplexes.

Intended owners: `categories/derived/filtered_complexes.py` (`FilteredComplex` with `F^p`, `gr_F^p`, `E_0/E_1`, `spectral_sequence() → SpectralSequence`), `categories/hodge/hodge_filtration.py` (`HodgeFiltration` as `F^pΩ^{•}=Ω^{≥p}` with `gr`, `F^pRΓ` as `Filtered`), `categories/schemes/hodge_frolicher.py` (`FrolicherSS` as `E_1^{p,q}=H^q(X,Ω^p) ⇒ H^{p+q}_{dR}` via `FilteredComplex`, delegating to filtered `EC`), `categories/homotopy/spectral_sequences.py` (`SpectralSequence` with `E_r(p,q)`, `d_r`, `is_zero`, `degenerates_at(r0)`, `stabilizes_at(p,q,r0)`), `categories/sheaves/grothendieck_sseq.py` (`GrothendieckSpectralSequence` / `LeraySS` as `E_2^{p,q}=R^pG(R^qF) ⇒ R^{p+q}Γ` from Cartan-Eilenberg/Čech double). Not a free `hodge_sseq(X)` list — `X.filtered_de_rham().spectral_sequence()` and `U.cech_double(F^•).filtered()` on filtered objects, with degeneration tested as morphism-zero via `EC` matrices, not dimension coincidence.

## Intake: https://www-fourier.univ-grenoble-alpes.fr/~sergerar/Papers/Ana-JSC.pdf — fixtures + algorithms — 2026-09-15 — verbatim

Paper is Ana Romero–Julio Rubio–Francis Sergeraert–Alberto Alzola *Effective homology of filtered complexes*, JSC (Kenzo team). Provides explicit test fixtures and algorithms for the filtered effective-homology sseq machinery already intaken via Kenzo; does not introduce a new mathematical theory beyond §3 definitions but supplies oracles a preamble must reproduce.

**What it contains (verbatim extraction for fixtures):**

*Theorem 15 (p.7):* Let `C` filtered with effective homology `(HC, ε)`, `ε=(D,ρ,ρ')`, `ρ=(f,g,h)`, `ρ'=(f',g',h')`. If filtrations also on `HC,D` and `f,f',g,g'` filtered and `h,h'` have order ≤t (`h(F_pD)⊂F_{p+t}D` ∀p), then spectral sequences `E_r(C) ≅ E_r(HC)` for `r>t`. Proof uses `f_r g_r=id` and `h: gf≃id ⇒ (gf)_r=(id)_r` for `r>t` via [MacLane Homology Prop.3.5 p.331].

*Definitions:* filtration `F_pC⊂C` with `d(F_p)⊂F_p`, bounded `F_sC_n=0, F_tC_n=C_n` for `s<t` per `n`; Z-bigraded `E={E_{p,q}}`, differential `d:E→E` bidegree `(-r,r-1)`, spectral sequence `E={E_r,d_r}` with `H(E_r,d_r)≅E_{r+1}`; `Z^r_{p,q}={a∈F_pC_{p+q} | d(a)∈F_{p-r}C_{p+q-1}}`, `E^r_{p,q}=Z^r_{p,q}/(dZ^{r-1}_{p+r,q-r+1}∪F_{p-1}C_{p+q})`, `d_r` induced by `d` (Thm.8). Note: formal expression not sufficient when `Z^r_{p,q}` not finite type — needs effective homology (p.6).

*Effective homology:* reduction `ρ:D⇒C` is `(f:D→C, g:C→D, h:D→D[1])` with `fg=id_C, gf+d h+ h d=id_D, f h=0, h g=0, h h=0` (Def.9, Rem.10 `D=Ker f⊕Im g`, `H(D)≅H(C)`). Strong equivalence `C⇔E` via `C⇐D⇒E`. Object with effective homology `(X,HC,ε)` with `HC` effective (each `HC_n` finitely generated free with algorithm for Z-basis, [9]) and `ε: C_*(X)⇔HC` (Def.12). Example 13 (Serre): `G↪E→B` with `E=B×_τG`, `C(B×G) ⇒ C(B)⊗C(G)` EZ reduction + BPL with twisting `τ` gives `C(B×_τG)⇒C(B)⊗_tC(G)`; with `C(B)⇔HB`, `C(G)⇔HG` gives `C(B)⊗_tC(G)⇔HB⊗_t HG` effective via second BPL; composite is `ε_E`. Example 14 (EM): `ΩX` via cobar on coalgebra.

*Kenzo objects:* `kz1 = K(Z,1)` as `K(Z,1)_n=Z^n(Δ^n,Z)=Z^n` (minimal model, locally effective, `K1Abelian-Simplicial-Group`), `basiskz1 3` error locally-effective, `efhm(kz1)=[K22 Homotopy-Equivalence K1⇐K?⇒K16]` with `orgn(K16)=(CIRCLE)`, `basis(K16) 0=(*) 1=(S1)`, `?(K16) 1 S1 =0` ⇒ `H_0=H_1=Z`.

*Class `Filtered-Complex : Chain-Complex` with slot `flin: (degr, gen)↦p=min{t|gen∈F_tC}`. Functions: `build-FltrChcm :cmpr :basis :bsgn :intr-dffr :dffr-strt :flin :orgn`, `change-chcm-to-FltrChcm(chcm, flin, orgn)`, `fltrd-basis(fltrcm,degr,fltr-index)` (=basis of `F_pC_n`), `fltr-chcm-dffr-mtrx(fltrcm,degr,fltr-index)` (=matrix of `d: F_pC_n→F_pC_{n-1}`). Sseq core: `print-spct-sqn-cmpns(fltrcm,r,p,q)` (components `Z`/`Z_m`), `spct-sqn-basis-dvs(fltrcm,r,p,q)` (numerator generators vs denominator `dZ^{r-1}∪F_{p-1}`), `spct-sqn-dffr(fltrcm,r,p,q,int-list)` (`d_r` on coordinate list, e.g. `(1)` for generator `(s2,η_1η_0[])` maps to `(1)` = `(η_0*,[1])`), `spct-sqn-cnvg-level(fltrcm,degr)` (smallest `r` with `E_{p,q}^∞=E_{p,q}^r` for `p+q=degr`).

*Section 6 didactic fixtures (hand-computable, for verbatim oracles):*

- *6.1 `S^2×_τ K(Z,1)`* `τ:S^2→K(Z,1)` `τ(s2)=[1]` (if `[2]` then `P^3R`). `s2=sphere2` `[K23]`, `kz1=K(Z,1)` `[K1]`, `tau=build-smmr :src s2 :trg kz1 :degr -1 :sintr λ(_,_)->absm 0 '(1)`, total `s2-tw1-kz1=fibration-total(tau)` `[K34]`. Effective `rbcc(efhm(s2-tw1-kz1))=[K95]` with `orgn=(ADD[K74][K93(degree -1)])`, `K74 = TNSR-PRDC[K23][K16]` = `S^2⊗S^1`. So effective is `S^2⊗_t S^1` perturbed differential. Filtrations: `twpr-flin(degr,crpr)= -degr + length(dgop-int-ext(dgop))` i.e. degeneracy degree w.r.t. base (count `s_i` in second factor), implemented as `#'(lambda(degr,crpr) (- degr (length (dgop-int-ext (Car crpr))))...)`; `tnpr-flin(degr,tnpr)=degr1(tnpr)` = base dimension on tensor product `F_p(C(B)⊗C(G))=⊕_{m≤p}C(B)_m⊗C(G)`. Then `change-chcm-to-FltrChcm(s2-tw1-kz1, twpr-flin)` `[K34Filtered]` and `change-chcm-to-FltrChcm(s2xts1, tnpr-flin)` `[K95Filtered]`. Homotopies order 0 ⇒ `E_r(s2-tw1-kz1)≅E_r(s2⊗_tS^1)` for all `r`. Oracles: `E^2_{2,0}=Z` generator `-1*(s2, η_1η_0[])` (0 denominator), `E^2_{0,1}=Z` generator `-1*(η_0*,[1])`, `d^2_{2,0}(1)=(1)` i.e. `(s2,η_1η_0[])↦(η_0*,[1])`, hence `E^3_{0,1}=0, E^3_{2,0}=0`, convergence `r=1` for total degree 0 and `r=3` for degree 1 (`spct-sqn-cnvg-level` 0→1, 1→3), abutment `E^1_{0,0}=Z` only.

- *6.2 `S^2×_τ K(Z/2,1)`* same base with `kz21=K(Z/2,1)` `[K110]` where non-degenerate `n`-simplex is integer `n` representing sequence `1^n`, void `[]` =0; `tau2` same with `absm 0 1` and total `s2-tw2-kz21` `[K128Filtered]`. Now finite type (no effective bypass needed) but same filtration. Oracles: `E^2_{0,1}=Z/2` (`(η_0*,1)` with divisor `2`), `E^2_{2,0}=Z` (numerator 5 gens, denominator 4 gens, surviving `(s2,η_1η_00)`), `E^2_{0,3}=Z/2`, `d^2_{2,0}(1)=(1)` i.e. `(s2,η_1η_00)↦(η_0*,1)` again, convergence levels `deg1→3, deg2→1, deg3→1`.

*Section 7 advanced fixtures (beyond literature, for stress tests):*

- *7.1 Postnikov tower `X4`* with `π_i=Z/2` at each stage and simplest nontrivial invariants (`[10 pp.142-145]`): `X2=K(Z/2,2)` `[K133]`, `k3=chml-clss(X2,4)` `[K245]` on `K150`, `F3=z2-whitehead(X2,k3)` `[K260]`, `X3=fibration-total(F3)` `[K266]`, `k4=chml-clss(X3,5)` `[K479]`, `F4=z2-whitehead(X3,k4)` `[K494]`, `X4=fibration-total(F4)` `[K500]`, `effX4=rbcc(efhm(X4))` `[K696]`. As twisted products `K(Z/2,4)×_{k4}X3` where `X3=K(Z,3)×_{k3}K(Z/2,2)`. Filtrations as before (`fbrt-flin` on total, `tnpr-flin` on effective). Oracles for `r=2`: `E^2_{0,4}=Z/2, E^2_{5,0}=Z/4, E^2_{6,0}=Z/2⊕Z/2` and for `p+q=4..7` convergence at `r=6`; differentials `d^5_{5,0}(1)=(1): Z/4→Z/2` (`E^5_{5,0}→E^5_{0,4}`) and `d^5_{7,0}(1)=(1): Z/2→Z/2` (`E^5_{7,0}→E^5_{2,4}`); `E^6_{0,7}=Z/2, E^6_{3,4}=Z/2` else 0 in total degree 7.

- *7.2 Eilenberg-Moore `X` vs `ΩX`* for `m`-reduced `X` with effective homology, `ΩX` via cobar, iterated `Ω^k` for `k≤m`; filtration is cobar filtration on `B(C_*(X))`. Figures: Fig.1 `E_∞^{p,q}` `q-p≤8` for `ΩS^3` vs `ΩΩS^3` and Fig.2 for `ΩS^3∪_2 D^3` vs `Ω(ΩS^3∪_2 D^3)` with tables of `Z`, `Z/2, Z/3, Z/5, Z/6, Z/10` components as listed pp.14-15 — exact effective homology oracles for `Ω` attachment.

**Additional algorithms beyond Kenzo core (p.15):** exact couples `G.W.Whitehead [12]` as more general than filtered complexes — a filtered complex determines an exact couple whose sseq is that of the filtered complex, but not conversely; Bousfield-Kan sseq does not arise from a filtration. Paper proposes future programs for exact couples analogously to `Filtered-Complex` ⇒ `E_r` via exact couple `D↔E` with `d_r`.

**Use:** intake already owns `FilteredComplex(flin)`, `SpectralSequence(E_r,d_r)` with `degenerates_at` etc.; this paper supplies the executable `flin` definitions (`twpr-flin`, `tnpr-flin`), the `change-chcm-to-FltrChcm` adapter contract, the perturbation-order theorem that justifies computing `E_{>t}` on `HC`, and the explicit `E_r^{p,q}` and `d_r` fixture values above for `S^2×_τ K(Z,1)` etc. that any preamble adapter must reproduce as `GrMod` specimens.

## Desired capability: interactive spectral sequence visualizer attached to sseq objects — note 2026-09-15

Note the need for an interactive spectral sequence visualizer attached to sseq objects. Should be able to show each page, differentials toggleable, entries in each bigraded slot, allow flipping pages, have tooltips with additional mathematical information.

* Visualizer is not a detached notebook helper. It is a method/view attached to the sseq object `E = SpectralSequence(E_r,d_r)` from `FilteredComplex`, `EilenbergMoore`, `Serre`, `Hodge-Frölicher`, `Grothendieck` etc.: `E.visualize()` / `E.show()` / `E._repr_html_()` returns an interactive widget bound to that `E`, not a free `plot_sseq(E)` with duplicated state. State lives on `E`; the widget reads `E_r^{p,q}`, `d_r`, `E_r.next_page()`, `converges`, `degenerates_at`, and `EC` evidence.

* Per-page grid: bigraded `(p,q)` plane as interactive grid/table where each cell `E_r^{p,q}` displays its `GrMod` value (e.g. `Z`, `Z/2`, `Z/4`, `Z/2⊕Z/2`, `0`, free rank + torsion invariants from `Smith` as effective `EC`) with compact label and color for zero vs non-zero vs stabilized. Axes `p` (filtration) horizontal, `q` complementary vertical, with bounds derived from `FiltCh` support box (e.g. `0≤p≤dim B` for Serre fibre of dim B).

* Bigraded entries: each slot `E_r^{p,q}` is a `GrMod` object (often `Ab = Z-mod`) with presentation `Z^{r}⊕⊕ Z/d_i` from `Smith` on `EC` differential matrices; cell shows summary `Z^a⊕Z/2^b⊕...` and expands to generators/relations on demand. For effective `EC`, entries are computable matrices, not formal symbols.

* Differentials toggleable: `d_r^{p,q}: E_r^{p,q}→E_r^{p+r,q-r+1}` as arrows on grid; toggle per `r` (`d_1`, `d_2`, …) on/off, with arrow opacity/thickness reflecting rank, and click to highlight kernel `Z_r^{p,q}` vs image `B_r^{p,q}`. `d_r` matrices come from `E.filtered_complex().differential(r,p,q)` via `EC` (via `spct-sqn-dffr` analog); zero `d_r` shown dashed.

* Page flipping: controls to advance `E_r → E_{r+1}=H(E_r,d_r)` with animation/morph of cells (surviving `Z_r/B_r`), back/forward, jump to `E_2`, `E_∞`, and `r`-slider with `convergence level` `r_∞(p+q)` per total degree from `spct-sqn-cnvg-level` analog (`E.degenerates_at(r0)`, `E.stabilizes_at(p,q,r0)`). `E_∞^{p,q}=F^pH^{p+q}/F^{p+1}` abutment shown as final page with filtration quotients linking to `H^{p+q}(X)` via `EC(X)`.

* Tooltips with additional mathematical information: hover/click on `E_r^{p,q}` shows `Z^r_{p,q}` numerator vs `dZ^{r-1}_{p+r,q-r+1}∪F_{p-1}C_{p+q}` denominator (exactly the `spct-sqn-basis-dvs` data: numerator generator combinations as `CrPr`/`CmBn` symbols from `K(Z,n)` etc. and denominator divisors), filtration index `p=min{t|gen∈F_t}`, degree `p+q`, `d_r` matrix on basis, cycles `ker d_r` vs boundaries `im d_r`, and convergence provenance (e.g. `S^2×_τK(Z,1) d^2_{2,0}: (s2,η_1η_0[])↦(η_0*,[1])` with coordinate `(1)↦(1)`). For `k-invariant` pages, tooltip links `κ_n∈H^{n+2}(X^{(n)};π_{n+1})` classifying `K(π,n+1)↪X^{(n+1)}→X^{(n)}`.

* Interaction contracts: widget subscribes to `E` (no duplicate state), `E` remains effective via `EC` reductions; widget works in Jupyter via `_repr_html_`/`ipywidgets`/Bokeh/Plotly or Quarto HTML export without server, and degrades to ASCII table when headless. Reuses `SpectralSequence` owners already intaken (`categories/homotopy/spectral_sequences.py` with `E_r`, `d_r`, `E_r.next_page()`), `categories/derived/filtered_complexes.py` (`flin` degeneracy degree `twpr-flin` etc.), and `categories/topology/effective_homology.py` (`EC` Smith); does not reimplement `E_r` logic in JS.

Intended owners: `categories/homotopy/spectral_sequences.py` (`SpectralSequence.visualize() → InteractiveSseq` widget bound to `E`, with `show_page(r)`, `toggle_differential(r)`, `cell_tooltip(p,q)` reading `E_r^{p,q}` as `GrMod` and `d_r` as `Mat`), delegating to `src/dzack_research/preamble/visualization/sseq.py` or `notebooks/visualizer` adapter for rendering (grid, arrows, tooltips), and to `categories/derived/filtered_complexes.py` for `flin` metadata. Not a detached `plot_sseq(E)` function returning static PNG — `E.visualize()` on the sseq object with page state, bigraded slots, and tooltips driven by `EC` differentials.

## Desired capability: concrete geometric models for classifying spaces BG, EG→BG, simplicial objects in C, configuration spaces — note 2026-09-15

Note the need for concrete geometric representations of many classifying spaces `BG`. E.g. `RP^∞`, `CP^∞`, lens spaces `L_p^∞`, `F_n` the free group on `n` gens, `Gr_n(C^∞)`, `Gr_n(R^∞)`, `BSO_n`, `BSp_n`, `BGL_n`, `X = Bπ_1(X)` in good cases, `BG` for the (pure) braid groups `B_n` and `P_n`, `BSpin_n`, `BString_n`, `HP^∞`, needs `HH` and `HH^∞` to exist, needs to understand `B(G×H)`, the associated bundle construction, and the fibrations `EG→BG` for all of these. Should also be able to construct `EG` and `BG` explicitly categorically and simplicially. Needs an honest way to construct simplicial objects in `C`, and particularly simplicial sets. Needs various configuration spaces: ordered, unordered, allowing points to coincide vs not, etc.

* `BG` is not a formal symbol `B(G)`. For `G : Groups` (discrete), topological group, Lie group, simplicial group, `BG : HoTop` is the classifying space with `ΩBG ≃ G` as `H-group` and `π_{i+1}(BG)≅π_i(G)`, `π_0(BG)=*` (connected), universal principal `G`-bundle `EG→BG` with `EG` contractible and `G` free action. For discrete `G`, `BG = K(G,1)`. Interface must be `G.classifying_space() → BG : HoTop` with `EG : Top` and `p: EG→BG` Kan/Serre fibration with fiber `G`, not a bare list of cells.

* Concrete models (each is an object `BG : HoTop` with effective homology when `G` finite type, plus `EG→BG` fibration with `EG` contractible):
  - `RP^∞ = B(Z/2) = K(Z/2,1)` as `colim_n RP^n` with `RP^n = S^n/(x∼-x)` and cellular `e_0∪e_1∪…` one cell each dimension, `H^*(RP^∞;F_2)=F_2[w_1]` `|w_1|=1` with `w_1` universal Stiefel-Whitney; `EG=S^∞`.
  - `CP^∞ = B U(1)=B S^1 = K(Z,2)` as `colim_n CP^n`, `H^*(CP^∞;Z)=Z[c_1]` `|c_1|=2`, `EG=S^∞` with `S^1` Hopf `S^∞→CP^∞`; also `CP^∞=Gr_1(C^∞)`.
  - Lens `L_p^∞ = B(Z/p)` as `S^∞/(z∼ζ_p z)` with `ζ_p=e^{2πi/p}`, `H^*(L_p^∞;F_p)=F_p[x]⊗Λ(y)` `|y|=1,|x|=2, βy=x`, universal `Z/p` bundle `S^∞→L_p^∞`; needs `S^∞` as simplicial `EG` already.
  - `F_n` free group on `n` gens: `BF_n = ∨^n S^1` wedge of `n` circles (graph with one vertex, `n` loops), `π_1(BF_n)=F_n`, higher `π=0`; `EF_n` is `n`-regular tree (Cayley graph of `F_n`) contractible.
  - `Gr_n(C^∞)=B U(n)`, `Gr_n(R^∞)=B O(n)` Grassmannians as `colim_k Gr_n(C^k)` / `colim_k Gr_n(R^k)` with Schubert cells, `H^*(BO(n);F_2)=F_2[w_1,…,w_n]`, `H^*(BU(n);Z)=Z[c_1,…,c_n]`; `EG=V_n(C^∞)=Stiefel manifold` `V_n(C^∞)=U(∞)/U(∞-n)` contractible with `O(n)`/`U(n)` free.
  - `BSO_n`, `BSp_n = BSp(n)`, `BGL_n = BGL_n(C)` / `BGL_n(R)` variants: `BSO_n = Gr_n^+(R^∞)` oriented Grassmannian (double cover of `Gr_n(R^∞)`), `BSp_n` quaternionic `Gr_n(H^∞)`, `BGL_n` algebraic vs topological (need `Top` vs `Alg` model). All via Stiefel `EG→BG` with `EG` Stiefel `V_n`.
  - `X = Bπ_1(X)` good cases: when `X` aspherical (`π_{>1}=0`), e.g. `X` closed surface of genus `g≥1`, `X` `K(π,1)` already, so `X ≃ Bπ_1(X)` as `HoTop` equivalence (not formal).
  - `BG` for braid `B_n` and pure `P_n`: `B_n = π_1(Conf_n^{unord}(C))` with `Conf_n^{unord}(C)=Conf_n(C)/Σ_n`, `P_n=π_1(Conf_n(C))`; models `Conf_n(C)=C^n\Δ` complements of arrangement `Δ=∪_{i<j}{z_i=z_j}`; `BB_n = Conf_n^{unord}(C) ≃ K(B_n,1)` aspherical (Fadell-Neuwirth fibrations). Needs `Conf` intaken below.
  - `BSpin_n`, `BString_n` higher connected covers of `BO_n`: `BSpin_n = BSO_n` with `w_2` killed (`π_1` cover), `BString_n` with `(1/2)p_1` killed (`π_3`); as homotopy fibers of `w_2: BSO_n→K(Z/2,2)` and `(1/2)p_1: BSpin_n→K(Z,4)`. Needs `K(G,n)` effective already.
  - `HP^∞ = BSp(1)=BS^3 = K?` `HP^∞ = Gr_1(H^∞) = S^∞/S^3` with `H^*(HP^∞;Z)=Z[u]` `|u|=4`, `EG=S^∞`; `HH` `=H` and `HH^∞` `=B?` (quaternionic). Need `H = {quaternions}` as `NormedDivAlg`.

* `HH` and `HH^∞` to exist: `H = Hamilton quaternions` as `R`-algebra `H = R⟨i,j | i^2=j^2=-1, ij=-ji=k⟩` object of `Alg_R` with `|H:R|=4`, norm `N: H→R`, `Sp(1)=S^3 = {q∈H | N(q)=1}` as Lie group `G : Groups` with `Lie(G)=im H`. Then `HP^n = Gr_1(H^{n+1})` and `HP^∞ = colim HP^n = BSp(1)`. `HH^∞` is infinite quaternionic projective limit / `BSp(∞)=BSp`.

* `B(G×H)` understanding: for `G,H : Groups`, `B(G×H) ≃ BG × BH` as `HoTop` with `EG×H = EG×EH`, projections give `B(G×H)=E(G×H)/(G×H)`. More generally `B` preserves products `B: Grp(Top)→HoTop` product-preserving. Associated bundle construction: given principal `G`-bundle `P→X` (`P = f^*EG` for `f:X→BG`) and left `G`-space `F`, associated `P×_G F = (P×F)/G → X` with fiber `F`, transition `τ: U_{ij}→G` acting on `F`. Interface `P.associated_bundle(F) → E : Top` with `E = P×_G F`.

* Fibrations `EG→BG` for all: principal bundle with fiber `G`, structure map `EG = W̄?`? Models: `EG = W̄?` Choose: `EG = |W G|` geometric realization of simplicial `WG` (Kan's `WG_n = G_n×…×G_0`) contractible with free `G`-action `WG×G→WG`, `BG = W̄G = WG/G`. Or `EG = colim Gr` Stiefel model for matrix groups. Need both explicit categorical and simplicial constructions of `EG` and `BG` as objects `EG : sSet` / `Top` with `G`-action and `BG = EG/G` quotient.

* Honest simplicial objects in `C`: for any category `C` (here `C=Top, Sets, Groups, Mod_R, Alg, etc.`), `sC = Fun(Δ^{op}, C)` simplicial objects `X_•` with `X_n : C`, face `d_i: X_n→X_{n-1}`, degeneracy `s_i: X_n→X_{n+1}` satisfying simplicial identities `d_i d_j = d_{j-1}d_i (i<j)` etc. Interface `SimplicialObject(C)` with `X : sC` and `C(X)_*: Ch` via Dold-Kan when `C` abelian. Specialization to `C=Sets` gives `sSet` as already intaken `sSet = sSets`, but now as instance of `sC`. Needs `Δ` as simplex category `Δ(n,m)=Hom_{Ord}([n],[m])` and `Nerve: Cat→sSet` as `N(C)_n = Fun([n],C)`.

* Configuration spaces: for `X : Top` (e.g. `X=R^2=C, R^n, manifold M`), ordered `Conf_n^{ord}(X)=X^n\Δ` where `Δ = {(x_i) | ∃i≠j x_i=x_j}` fat diagonal, `Σ_n`-action permuting coordinates; unordered `Conf_n^{unord}(X)=Conf_n^{ord}(X)/Σ_n` quotient by free `Σ_n` when `X` Hausdorff and points distinct, and more generally `Conf_n^{≤}(X)=X^n` allowing collisions (fat diagonal kept) vs `Conf_n^{<}(X)=Conf_n^{ord}` not allowing. Generalizations: `Conf_{n,k}(X)` allowing at most `k` coincidences, and `Conf_n(X; ≤m)` bounded multiplicity. For `X` manifold, Fadell-Neuwirth fibration `Conf_{n+1}(X)→Conf_n(X)` with fiber `X \ {n points}` when `X` connected manifold dim≥2. Ordered vs unordered `B_n, P_n` already above via `Conf_n(C)`. Need models: complements `R^n\Δ` as semialgebraic `Top`, simplicial `Conf_n^{Δ}` via `sSet` triangulation of `X^n` minus `Δ`, and effective homology for `Conf_n` (when `X`sSet effective, `Conf_n` inherits `EffHom` via product `X^n` and `EffHom` of complement as subspace, not formal).

Intended owners: `categories/topology/classifying_spaces.py` (`ClassifyingSpace(G) → BG : HoTop` with `EG→BG` `G`-bundle, `B: Grp→HoTop` product-preserving, plus concrete models `RP_infty=K(Z/2,1)`, `CP_infty=K(Z,2)`, `Lens_p`, `Gr_n(C^∞)=B U(n)`/`Gr_n(R^∞)=B O(n)`/`Gr_n^+(R^∞)=B SO_n`, `BSp_n`, `BGL_n`, `BSpin_n`, `BString_n`, `HP_infty=BSp(1)` and `HH`, `BF_n=∨^n S^1`, `BB_n=Conf_n^{unord}(C)`, `BP_n=Conf_n(C)` as `K(B_n,1)/K(P_n,1)`, `B(G×H)≅BG×BH`, associated `P×_G F`), delegating to `categories/algebras/division_algebras.py` (`H`, `Sp(1)`), `categories/topology/simplicial_sets.py` (`sSet`, `Δ`), `categories/topology/simplicial_objects.py` (`sC = Fun(Δ^{op},C)` with `Δ` simplex category, `Nerve`, `Realization`), `categories/topology/configuration_spaces.py` (`Conf_n^{ord}(X)`, `Conf_n^{unord}(X)=Conf_n^{ord}/Σ_n`, `Conf_n^{≤}=X^n`, Fadell-Neuwirth fibrations), `categories/topology/effective_homology.py` (`EC` for `Conf_n` via `EC(X)^n` and complement). Not a free `classifying_space(G)` returning bare list — `G.classifying_space() → BG` with `G.universal_bundle() → EG→BG` as `G`-space fibration object.

## Desired capability: character varieties, Betti moduli space, general GIT quotients and Hilbert schemes, honest holonomy groups — note 2026-09-15

Note the need for character varieties, the Betti moduli space. Need general GIT quotients and Hilbert schemes. Need honest holonomy groups.

* Character variety is not a bare `Hom(π,G)/G` set. For `π : Groups` (e.g. `π=π_1(X,x) : Groups` finitely presented `π=⟨S|R⟩`, or `π=π_1^{ét}(X)`, `Gal_K`) and `G : GrpSch/k` (reductive, e.g. `GL_n, SL_n, PGL_n, Sp_{2n}, O_n, G_2`, or algebraic torus), `Rep(π,G)=Hom_{Groups}(π,G) : Sch/k` is the representation scheme with `Rep(π,G)(A)=Hom(π,G(A))` as `A`-points; for `π=⟨S|R⟩`, `Rep = {(g_s)∈G^S | r((g_s))=1 ∀r∈R} ⊂ G^S` closed subscheme via equations `r=1` in `G`. Character variety `X(π,G)=Rep(π,G)//G : Sch/k` is the GIT quotient by conjugation `G` acting by `g·ρ = gρg^{-1}` (conjugation on each generator). Betti moduli `M_B(X,G)=X(π_1(X),G)` for `X : Sch/C` smooth with `U=X^{an}` is the Betti component of nonabelian Hodge: `M_B = Hom(π_1(U),G)//G` as categorical quotient `Spec(k[Rep]^G)` (affine). Distinguish `Rep^s` stable, `Rep^{irr}` irreducible, `X^{irr}=Rep^{irr}/G` geometric quotient; `X(π,G)(k)` points are `G(k)`-conjugacy classes of semisimple representations. Interface `π.character_variety(G) → X(π,G) : Sch` and `X.betti_moduli(G) → M_B` on the space, not free `character_variety(π,G)` with matrices.

* Needs GIT quotients generally: for `X : Sch/k` with linearized `G`-action (`G : GrpSch` reductive acting via `σ: G×X→X` and `L : Pic^G(X)` ample linearization), `X//_L G = Proj(⊕_{n≥0} Γ(X,L^{⊗n})^G) : Sch/k` categorical quotient with `π: X^{ss}→X//G` (`X^{ss}` semistable as `∃s∈Γ(X,L^{⊗n})^G, s(x)≠0` and `X_s` affine), and `X^s⊂X^{ss}` stable with `π|_{X^s}: X^s→X^s/G` geometric quotient (free action, orbits closed). For affine `X=Spec A` with `G` reductive, `X//G = Spec(A^G)` via invariants `A^G = {a∈A | g·a=a}`. Quotient is object `GITQuotient(X,G,L) : Sch` with `π: X^{ss}→X//G` morphism, not a set quotient `X/G`.

* Needs Hilbert schemes generally: for `X : Sch/k` projective with `O(1)` ample, `Hilb^P(X) : Sch/k` is the Hilbert scheme parametrizing flat families `Z⊂X×S` with Hilbert polynomial `P` (`χ(O_{Z_s}(m))=P(m)` for all `s∈S`), i.e. functor `Hilb^P_X(S)={Z⊂X×S closed, flat over S, P_{Z_s}=P}` representable by `Hilb^P`. In particular `Hilb^n(X)=Hilb^{P=n}(X)` for 0-dimensional length-`n` subschemes as `P(m)=n`, and `Hilb_X = ∐_P Hilb^P`. Object `Hilb^P(X) : Sch` with universal family `U⊂X×Hilb^P` flat over `Hilb`. Interface `X.hilbert_scheme(P) → Hilb^P(X) : Sch` and `X.hilbert_scheme_of_points(n) → Hilb^n(X)`, and for `C` curve `Hilb^n(C)=Sym^n C`, for `S` surface `Hilb^n(S)` smooth `2n`-dim with Hilbert-Chow `Hilb^n(S)→Sym^n S`.

* Honest holonomy groups: for `E→X` vector bundle `E: Vect(X)` with connection `∇: E→E⊗Ω^1_X` (flat or not), `Hol(∇)` is not a formal `monodromy_group` string. It is the subgroup `Hol_x(∇) ≤ GL(E_x)` generated by parallel transport `P_γ: E_x→E_x` along loops `γ: [0,1]→X` piecewise smooth with `γ(0)=γ(1)=x`, where `P_γ` is defined by ODE `∇_{γ'}s=0`. For flat `∇`, `P_γ` depends only on ` [γ]∈π_1(X,x)` and `Hol_x = Mon_x` is the monodromy image `ρ: π_1→GL(E_x)` already intaken via `FlatConn → LocSys`; for non-flat, `Hol` is the Ambrose-Singer group generated by curvature via `Hol_x = ⟨P_γ^{-1}∘R(u,v)∘P_γ⟩`. For Riemannian `∇=Levi-Civita` on `X : RiemMfd` with `T_X`, `Hol_x ≤ O(T_x)` Berger list, and for `G_2`, `Spin(7)` etc. restricted holonomy. Interface `∇.holonomy_group(x) → Hol_x : Groups` as subgroup `Hol_x ≤ GL_{rank E}(k)` presented via generators `P_{γ_i}` for loops `γ_i` generating `π_1` (effective via validated ODE transport as in CAP monodromy lead), and restricted `Hol^0_x` identity component via null-homotopic loops.

Intended owners: `categories/moduli/character_varieties.py` (`CharacterVariety(π,G)=Rep(π,G)//G : Sch` with `Rep(π,G) ⊂ G^S`, `M_B(X,G)=X(π_1(X),G)` Betti moduli as `Spec(k[Rep]^G)`), `categories/moduli/git_quotients.py` (`GITQuotient(X,G,L)=X//_L G : Sch` via `Proj(⊕Γ(L^n)^G)` with `π: X^{ss}→X//G` and `X^s/G`), `categories/moduli/hilbert_schemes.py` (`HilbertScheme(X,P)=Hilb^P(X) : Sch` with `HilbertFunctor` representability, `Hilb^n` as `P=n`, universal `U`), `categories/connections/holonomy.py` (`HolonomyGroup(∇,x) ≤ GL(E_x)` via `P_γ` transport, `Hol^0`, Berger/Ambrose-Singer). Not a free `character_variety(π,G)` or `holonomy(∇)` returning matrices — `π.character_variety(G)` and `∇.holonomy_group(x)` on the group/bundle objects with `Rep` scheme `G^S` and `G`-invariants behind `X//G` and `P_γ` ODE.

## Desired capability: group (co)homology with Tate/transfers/traces/norms/induction, surface groups, group objects, Higgs/NAH, RR/index/Poincaré/Chern, 4-manifold Freedman, spinnability/Arf/KS/Â, equivariant, Hodge ops, cobordism/TQFT, normal bundles — note 2026-09-15

Need group homology/cohomology, Tate cohomology, transfers, traces, norms, induction/restriction and their co-versions. Need surface groups `π_1Σ_g` as explicitly finitely presented groups, algebraic groups, Lie groups, group schemes, Higgs bundles, local systems, flatness for vector bundles, (harmonic) metrics, semisimplicity and complete reducibility for representations, basic non-abelian Hodge theory, operationalize Riemann-Roch computations, various index theorems (e.g. Atiyah-Singer), Gauss-Bonnet. Need to be able to compute full Poincaré series as OGFs (formal power series) and thus extra Betti numbers. Need to operationalize calculus with Chern classes and Chern characters. Ideally be able to get `H^*(X;ZZ)/tors` for at least 4-manifolds, as a graded group but ideally a ring/`ZZ`-algebra, and thus be able to check homeomorphism for 4-manifolds using Freedman's theorem and constructing the lattice on `H^2`. Operationalize algorithms and theorems to decide when a smooth manifold is spinnable (e.g. by Rohlin, Kervaire–Milnor theorem, Freedman-Kirby). Need the Arf invariant, Kirby–Siebenmann invariant, `Â` genus. Need enough to operationalize Hirzebruch–Riemann–Roch and Chern-Gauss-Bonnet. Differential operators and the symbol map, and their index maps. Todd class. Need to be able to operational `G`-equivariant cohomology and `K` theory. Need exterior derivatives, Hodge Laplacians, Hodge star, etc. Need operationalizations of known cobordism rings, and in some cases the ability to detect if manifolds are cobordant. Need cobordism categories in order to define TQFTs as functors. Need normal bundles of immersions and embeddings.

* Group (co)homology is not `H^n(G,M)=Ext^n_{Z[G]}(Z,M)` as a bare `Ext` call without `G`-structure. For `G : Groups` (finite, finitely presented `G=⟨S|R⟩`, Lie, profinite, group scheme), `M : ZZ[G]-Mod` (`G`-module as `Ab` with `G`-action `ρ: G→Aut(M)`), `H_n(G,M)=Tor_n^{ZZ[G]}(ZZ,M)=H_n(M⊗_{ZZ[G]} P_•)` and `H^n(G,M)=Ext^n_{ZZ[G]}(ZZ,M)=H^n(Hom_{ZZ[G]}(P_•,M))` where `P_•→ZZ` is projective resolution of trivial `G`-module `ZZ` (e.g. bar resolution `B_•(G)=ZZ[G^{n+1}]` as free `ZZ[G]`-module). Tate cohomology `Ĥ^n(G,M)` for finite `G` extends to `n∈ZZ` via complete resolution `P̂_•` (norm `N=Σ_{g∈G}g: M_G→M^G`), with `Ĥ^0=M^G/NM`, `Ĥ^{-1}=ker N / I_G M`, `Ĥ^n=H^n` (`n≥1`), `Ĵ_n=H_n` (`n≥1`). Transfers `tr^G_H: H^*(H,M)→H^*(G,M)` and co-transfer `cor: H_*(H)→H_*(G)`, traces `tr: M→M^G`, norms `N_G: M→M^G`, induction `Ind_H^G: H-Mod→G-Mod` `Ind_H^G M = ZZ[G]⊗_{ZZ[H]}M` left adjoint to restriction `Res_H^G`, and coinduction `CoInd_H^G = Hom_{ZZ[H]}(ZZ[G],M)` right adjoint, with Shapiro `H^*(G,CoInd)=H^*(H,M)` and `H_*(G,Ind)=H_*(H,M)`. Also co-versions `coInd` vs `coRes` via `Hom`/`⊗` duality. Interface `G.group_cohomology(n,M) → H^n`, `G.tate_cohomology(n,M) → Ĥ^n`, `H.transfer(G,M)` etc. on the group object, with `P_•` as `D(ZZ[G])` object and `⊗^L_{ZZ[G]}` already intaken.

* Surface groups `π_1Σ_g` as explicitly finitely presented groups: `π_1Σ_g = ⟨a_1,b_1,…,a_g,b_g | ∏_{i=1}^g [a_i,b_i]=1⟩ : FinitelyPresentedGroups` with `g: NN`, genus `g`, `Σ_g` closed orientable surface `Chi=2-2g`, `H_1=Z^{2g}`, `H_2=Z`. Object `SurfaceGroup(g) : FPGroups` with presentation as datum `F(S)↠π` as framed group `Framed(F(S), rels)` with word `r=∏[a_i,b_i] : F(S)`. Non-orientable `N_g` variant `⟨c_1,…,c_g|∏c_i^2=1⟩` when needed. This is data-bearing `Framed` FP group already modeled via `Groups().framed` / `FrGroups`, not a string presentation.

* Group objects taxonomy as distinct categories with forgetful functors, not one `Groups` type:
  - Algebraic groups `G : GrpSch/k` (`G : Sch/k` with `m:G×G→G`, `e:Spec k→G`, `inv`), e.g. `GL_n, SL_n, SO_n, Sp_{2n}, PGL_n, G_m, G_a, elliptic`.
  - Lie groups `G : LieGroups` smooth manifold with smooth `m`, e.g. `U(n), SU(n), Sp(n), SO(n)`, with `Lie(G)=T_eG` and `exp: Lie(G)→G`.
  - Group schemes over `ZZ` / `Spec k` with base-change `G_R = G×_{Spec Z} Spec R`; `G(k)` `k`-points.
  Each has `AlgGrp→LieGrp` analytification `G^{an}`, `GrpSch→Groups` forgetful `G↦G(k)`.

* Higgs bundles, local systems, flatness, metrics, NAH: for `X : SmProj/C` (`X` smooth projective curve/surface/variety), `Higgs bundle = (E, φ)` with `E : VecBun(X)` (`E : QCoh` locally free), `φ: E→E⊗Ω^1_X` `O_X`-linear (`φ∧φ=0` integrability, as `Higgs field`), semistability via `μ(F)<μ(E)` for `φ`-invariant `F⊂E`. `Local system = L : LocSys(X^{an})` as `FlatConn^{rs}` object `(E,∇)` with `∇^2=0` already intaken via `Conn→FlatConn→LocSys` and Riemann-Hilbert. Flatness for `E` means existence of flat `∇` (i.e. `E` in `FlatConn` image under forgetful `FlatConn→VecBun`; Atiyah class `at(E)∈Ext^1(E,E⊗Ω^1)=0` iff flat when `X` curve). Harmonic metric `h: E→\bar E^∨` Hermitian with Hitchin equations `F_h + [φ, φ^{*h}]=0, \bar ∂_E φ=0` (Kobayashi-Hitchin). Semisimplicity / complete reducibility for `ρ: π_1(X)→GL_n(C)` = `ρ` semisimple (`C[π]-module` sum of simples) ⇔ polystable Higgs `(E,φ)` with `deg=0` via NAH. Basic non-abelian Hodge is the homeomorphism of moduli `M_{Dol}(X,r) ≅ M_{dR}(X,r) ≅ M_B(X,r)` where `M_{Dol}=Higgs^{ss}/∼`, `M_{dR}=Flat^{ss}/∼` (flat connections), `M_B=Rep(π_1,r)//GL_r` (Betti). Correspondence `(E,φ) ↔ (E,∇=∂_E+φ+…) ↔ ρ` via harmonic metric and `D''= \bar ∂_E+φ`. Interface same moduli functors already intaken via `M_B`, plus `M_{Dol}, M_{dR}` as `Sch` with same `GITQuotient` and `HiggsField` as morphism `φ`.

* Operationalize Riemann-Roch computations, index theorems (Atiyah-Singer, Gauss-Bonnet): RR is not `χ(E)=∫ch(E)Todd`. It is the equality of `K-theory` pushforward `f_!: K_0(X)→K_0(Y)` (for proper `f: X→Y`) with cohomological `ch(f_!E)=f_*(ch(E)·Todd(T_f))` as `Chow/cohomology` pushforward (Grothendieck-RR), specialization to `X→Spec k` gives `χ(X,E)=∫_X ch(E) Todd(T_X)` as `Ab` integer. Operationalize as `X.riemann_roch(E) → χ` via `K_0` object `E: K_0(X)` and `ch: K_0→A^*(X)_Q` (Chow) and `Todd: Vect→A^*`. Atiyah-Singer index: for elliptic differential operator `D: Γ(E)→Γ(F)` on compact oriented Riemannian `X : RiemMfd` with symbol `σ(D): π^*E→π^*F` over `T^*X\0`, analytic index `ind(D)=dim ker D - dim coker D : ZZ` equals topological `ind_t(σ(D))=∫_{T^*X} ch([σ])·Todd(T_X⊗C)`. Gauss-Bonnet is specialization `D=d+d^*` or Euler `χ(X)=∫_X Pf(Ω/2π) = ⟨e(T_X),[X]⟩`. Interface `D.analytic_index() → ZZ`, `σ(D).topological_index() → ZZ` with `D=symbol_map(D)` agreement testable when `D` is `DiffOp` object of `PDiffOp(X;E,F)` with `σ(D): Sym(T^*X)→Hom(E,F)` polynomial symbol.

* Compute full Poincaré series as OGFs (formal power series) and thus extra Betti numbers: for `X : Top` with `b_i=dim H_i(X;Q)` (or `b_i(X;F_p)`), `P_X(t)=Σ_{i≥0} b_i t^i : ZZ[[t]]` as `OGF` object of `FormalPowerSeries(ZZ) = (t)-adic completion `ZZ[[t]]=lim Z[t]/(t^n)` already intaken via `R[[x]]` and `(x)-adic `, not a list `[b_0,…]`. Extra Betti via `P_X(t)= (1-t)^{-?}` rational when `X` fibration or Koszul. Interface `X.poincare_series() → P_X : ZZ[[t]]` with `b_i = [t^i]P` and `χ= P(-1)`.

* Operationalize calculus with Chern classes and Chern characters: for `E : VecBun(X)` rank `r`, total Chern `c(E)=1+c_1(E)+…+c_r(E) : A^*(X)` with `c_i∈A^i`, Whitney `c(E⊕F)=c(E)c(F)`, `c(L)=1+c_1(L)` for line `L` with `c_1: Pic(X)→A^1` via `divisor`. Chern character `ch(E)= Σ exp(x_i)= r + c_1 + (c_1^2-2c_ `…` : A^*(X)_Q` with `x_i` Chern roots via splitting `π: Fl(E)→X` with `π^*E = ⊕ L_i`, `ch: K_0(X)→A^*(X)_Q` ring homomorphism `ch(E⊗F)=ch(E)ch(F)`. Interface `E.chern_class(i)→c_i : Chow`, `E.chern_character()→ch : Chow_Q` as `GrMod` graded, with `c(E⊕F)` relation test.

* Get `H^*(X;ZZ)/tors` for at least 4-manifolds, as graded group but ideally ring/`ZZ`-algebra, and thus check homeomorphism via Freedman: for closed simply-connected topological 4-manifold `X : Top4Mfd`, `H_2(X;ZZ)≅ZZ^{b_2}⊕Tors` is free when simply-connected (by `H_1=0`, `Tors H^2≅Tors H_1=0`), intersection form `Q_X: H_2×H_2→ZZ` via `(a,b)↦⟨a∪b,[X]⟩` as symmetric unimodular bilinear `Q_X : Lattices` (`det=±1` by Poincaré duality), with parity `even` iff `w_2(X)=0` (spin) else `odd`. `H^*(X;ZZ)/tors ≅ ZZ ⊕ 0 ⊕ H^2 ⊕ 0 ⊕ ZZ` as `GrAlg` with `∪: H^2×H^2→H^4≅ZZ` equal to `Q_X`. Freedman theorem: homeomorphism class of simply-connected closed topological 4-manifold is determined by `Q_X` (isometry class) and `ks(X)∈Z/2` (Kirby-Siebenmann, zero when smoothable). Interface `X.intersection_lattice()→Q_X : Lattices` and `X.cohomology_ring_mod_tors()→H^*/tors : GrAlg` with `∪` product via `C^*(X)` effective `EC` cup product `⌣: C^p⊗C^q→C^{p+q}` on `EC` cochains.

* Decide when smooth manifold is spinnable via `w_2` and refinements: `X` closed `n`-manifold `X : SmMfd` is spin ⇔ `w_2(TX)=0 ∈ H^2(X;F_2)` via `w_2` universal from `BSO_n` (`w: BSO_n→K(Z/2,2)`), plus when `w_2≠0` distinction `spin^c`. Rohlin: for smooth closed spin 4-manifold `σ(X)≡0 mod 16` where `σ=b^+_2 - b^-_2` signature of `Q_X`; contrapositive `σ≠0 mod16 ⇒ not spin`. Kervaire–Milnor on exotic spheres `Θ_n` via `bP_{n+1}` etc.; Freedman–Kirby on topological spin with `ks` obstruction for smoothing: closed topological 4-manifold smoothable iff `ks(X)=0` after correcting `σ` parity. Interface `X.is_spin()→Bool` via `w_2(X).is_zero() : H^2(F_2)`, `X.rohlin_invariant()→σ mod16`, `X.kervaire_obstruction()`.

* Arf invariant, Kirby–Siebenmann invariant, `Â` genus: Arf `Arf(q)∈Z/2` for nondegenerate quadratic refinement `q: H^{2k+1}(M;F_2)→Z/2` with `q(x+y)=q(x)+q(y)+⟨x∪y,[M]⟩`, as `Arf(H^{2k+1},q)` for framed `(4k+1)`-manifold or characteristic `Σ^{2k+1}`. `ks: Top4Mfd→Z/2` Kirby–Siebenmann as `ks(X)∈H^4(X;Z/2)≅Z/2` obstruction to PL structure, with `σ/8 ≡ ks mod2` for spin with boundary. `Â` genus `Â(X)=⟨\hat A(TX),[X]⟩ : Q` with `\hat A = ∏ x_i/2 / sinh(x_i/2)` where `x_i` formal Pontryagin roots (`p_i = σ_i(x_j^2)`), as `Q`-number via `Todd`-like class, zero for positive scalar curvature on spin via Lichnerowicz. Interface `E.arf_invariant()`, `X.kirby_siebenmann()`, `X.a_hat_genus()`.

* Enough for Hirzebruch–Riemann–Roch and Chern–Gauss–Bonnet: HRR for `X` smooth projective `n`-fold and `E : VecBun(X)` is `χ(X,E)=∫_X ch(E)·Todd(T_X)` with `Todd(T_X)=∏ x_i/(1-e^{-x_i}) : A^*(X)_Q` (Todd class of tangent), where `x_i` Chern roots of `T_X`; specialization to `X` curve `χ=deg E + rank(1-g)` etc. CGB for `X` closed oriented `2n`-manifold `χ(X)=⟨e(T_X),[X]⟩ = (1/(2π)^n)∫_X Pf(Ω)` where `e(T_X)=c_n(T_X⊗C)` top Chern as Euler class, `Ω` curvature of Levi-Civita. Both as derived from `ch`/`Todd`/`e` calculus plus `∫_X : A^{dim X}→ZZ` via fundamental class ` [X] : H_{dim X}`. Interface `X.hirzebruch_riemann_roch(E)` and `X.chern_gauss_bonnet()` with numerical `χ` via `RΓ`.

* Differential operators and symbol map, and their index maps: `DiffOp^m(X;E,F)` order `m` `P: Γ(E)→Γ(F)` with local expression `P= Σ_{|α|≤m} a_α(x) D^α`, principal symbol `σ_m(P): T^*X\0 → Hom(π^*E,π^*F)` homogeneous degree `m` via `σ_m(P)(x,ξ)= Σ_{|α|=m} a_α(x) ξ^α : Sym^m(T^*X)⊗Hom(E,F)` as element `σ(P)∈Γ(T^*X, Hom(π^*E,π^*F))`. Symbol exact sequence `0→Diff^{m-1}→Diff^m → Sym^m(T^*X)⊗Hom→0`. Index maps `ind: [σ]∈K^0(T^*X)→ZZ` topological via `ch([σ])·Todd` integral, matching `ind(D)`. Interface `P.symbol() → σ(P) : Sym` with `is_elliptic ⇔ σ(P)(x,ξ) invertible ∀ξ≠0`, `P.index_map()`.

* Todd class `Todd(E)=∏ x_i/(1-e^{-x_i})` already for RR, similarly `L`-class, `Â`-class.

* Operational `G`-equivariant cohomology and `K` theory: for `G : Groups` (compact Lie `S^1, SU(n)`, finite), `X : G-Spaces` with `G`-action `G×X→X`, Borel construction `X_G = (EG×X)/G : HoTop` with fibration `X→X_G→BG`, `H^*_G(X;R)=H^*(X_G;R) : GrMod_R` with `H^*_G(pt)=H^*(BG)`, and `K^0_G(X)=K_G(X)` equivariant `K` via `G`-vector bundles `Vec_G(X)` Grothendieck `K_G(X)=K_0(Vec_G(X))` with `K_G(pt)=R(G)` representation ring. Interface `X.equivariant_cohomology(G,R) → H^*_G : GrMod` via `EC(EG×X)/G` effective, `X.equivariant_k_theory(G) → K_G` with `G`-bundle `E`.

* Exterior derivatives, Hodge Laplacians, Hodge star: on oriented Riemannian `X : RiemMfd` `n`-dim with metric `g`, volume `vol`, Hodge `⋆: Ω^k_X→Ω^{n-k}_X` via `α∧⋆β = ⟨α,β⟩_g vol`, exterior `d: Ω^k→Ω^{k+1}` with `d^2=0`, codifferential `δ = (-1)^{nk+n+1}⋆d⋆: Ω^k→Ω^{k-1}`, Laplacian `Δ = dδ+δd: Ω^k→Ω^k` self-adjoint elliptic, harmonic `H^k = ker Δ ≅ H^k_{dR}` via Hodge. Interface `Ω^k(X).hodge_star() → Ω^{n-k}`, `Ω^k.exterior_derivative() → Ω^{k+1}`, `Δ` as `DiffOp^2`.

* Known cobordism rings operational and cobordant detection: `MO_* = π_*(MO) = F_2[x_i | i≠2^k-1]` unoriented, `MU_* = ZZ[x_1,x_2,…]` `|x_i|=2i` complex (Milnor), `MSO_*`, `MSpin_*`, `MSU`, `MString`, etc. as `E_∞` ring spectra `MO=Thom(O)`, `MU=Thom(U)` with `π_*(MO)=Ω^{un}_*` etc. Ring `Ω^{un}_*` via Stiefel-Whitney numbers `w_{I}(M)=⟨∏w_{i_k}(TM),[M]⟩∈F_2`, `M` null-cobordant iff all `w_I=0`; `Ω^{SO}_*⊗Q = Q[Pontryagin numbers]` etc. Detection `M.is_cobordant(N) ⇔ [M]=[N]∈Ω_* ⇔ invariants equal` (Pontryagin/Stiefel-Whitney numbers, `Â`, `σ`). Interface `M.cobordism_class() → [M] : MO_*/MU_*` with `StiefelWhitneyNumbers`, `PontryaginNumbers`.

* Cobordism categories to define TQFTs as functors: `Bord_n` objects `M^{n-1}` closed oriented `(n-1)`-manifolds, morphisms `W: M_0→M_1` as `n`-bordisms `W` with `∂W = M_0⊔\bar M_1` up to diffeomorphism, monoidal `∐`, symmetric via `M∐N ≅ N∐M`. `n=1` is intervals/circles, `n=2` pair-of-pants. Extended `Bord_{n,m}` with corners. TQFT is symmetric monoidal functor `Z: Bord_n → Vect_k` (or `Ch, Sp`) with `Z(M∐N)=Z(M)⊗Z(N)`, `Z(∅)=k`, `Z(W): Z(M_0)→Z(M_1)` linear. Requires `Bord_n` as `∞-category` `Bord_n : Cat` with `Bord_n(M_0,M_1) : Spaces` via moduli of bordisms.

* Normal bundles of immersions and embeddings: for immersion `f: M^n ↬ N^{n+k}` with `df: TM→TN` injective bundle map, normal bundle `ν_f = f^*TN / df(TM) : VecBun(M)` rank `k` with `f^*TN ≅ TM⊕ν_f` as `Vect`; for embedding `i: M↪N` same with `ν_i` astubular neighborhood `ν_i ≅` neighborhood `U⊂N` via exponential `exp: ν_i → N`. For `M⊂R^{n+k}` standard, `ν` classifies immersion up to regular homotopy via Hirsch-Smale `Imm(M,N)≃ Mono(TM,TN)`. Self-intersection via `e(ν)` Euler.

Intended owners: `categories/group/cohomology.py` (`GroupCohomology` `H^*(G,M)` via `BarRes→Ext`, `Tate Ĥ^*`, `transfer`, `norm`, `Ind/Res` as `D(ZZ[G])` adjoints), `categories/group/surface_groups.py` (`SurfaceGroup(g) → π_1Σ_g` framed `⟨a_i,b_i|∏[a_i,b_i]⟩`), `categories/group/group_schemes.py` + `categories/group/lie_groups.py` (`AlgGroup`/`LieGroup`/`GrpSch` with `Lie`), `categories/higgs/nonabelian_hodge.py` (`HiggsBundle(E,φ)` semisimple, `M_{Dol}/M_{dR}/M_B` with `harmonic_metric`), `categories/index_theory/` (`RiemannRoch`, `AtiyahSingerIndex` `σ↦ind`, `GaussBonnet` `χ=∫e`, `HirzebruchRR` `χ=∫ch·Todd`, `ChernGaussBonnet`), `categories/characteristic_classes/chern.py` (`chern_class`, `chern_character`, `Todd`, `PoincareSeries` `P_X(t)∈ZZ[[t]]` as `(t)-adic` `OGF`), `categories/topology/four_manifolds.py` (`IntersectionLattice` `Q_X`, `CohomologyRingModTors` `H^*/tors` as `GrAlg_{ZZ}`, `is_homeomorphic_via_Freedman` from `Q_X,ks`), `categories/topology/spinnability.py` (`is_spin` via `w_2`, `Rohlin σ mod16`, `Kervaire–Milnor`, `Freedman-Kirby ks` → `Arf`, `KirbySiebenmann`, `a_hat_genus`), `categories/differential_operators/` (`DiffOp`, `principal_symbol`, `index_map`), `categories/equivariant/` (`Borel H^*_G`, `K_G`), `categories/hodge/hodge_star.py` (`d`, `⋆`, `δ`, `Δ`), `categories/cobordism/rings.py` (`MO_*`, `MU_*`, `MSO_*`, `cobordant(M,N)` via numbers), `categories/cobordism/bordism_category.py` (`Bord_n` `n`-category, `TQFT: Bord_n→Vect` functor), `categories/topology/normal_bundles.py` (`NormalBundle(immersion) → ν_f` with `f^*TN≅TM⊕ν`). Not free `group_cohomology(G,M)` list or `chernClass(E)` bare number — `G.group_cohomology(n,M)` via `BarRes` `D(ZZ[G])`, `E.chern_class(i)` as `Chow` graded, `M.normal_bundle()` as `VecBun` with `ν` as quotient/ tubular.

## Desired capability: almost complex structures, integral structure, Nijenhuis tensor, curvature tensors — note 2026-09-15

One needs almost complex structures, integral such structure, the Nijenhuis tensor, Ricci/gaussian/scalar curvature tensors, etc.

* Almost complex structure is not a matrix `J` with `J^2=-1` as bare `Mat_{2n}(R)`. For `M : SmMfd` real `2n`-manifold with `TM : VecBun_R(M)` rank `2n`, `J: TM→TM` is `J ∈ End(TM)` as `VecBun` endomorphism with `J^2 = -id_{TM}` as morphism `J∘J = -id` in `End(TM)` (`J_x: T_xM → T_xM`, `J_x^2=-1` pointwise). Equivalently `G`-structure reduction of frame bundle `Fr(TM)` from `GL_{2n}(R)` to `GL_n(C)` via `J`. Automorphism `J` makes each `T_xM` a `C`-vector space (`(a+ib)·v = a v + b J(v)`). Interface `M.almost_complex_structure() → J : End(TM)` with `J.is_almost_complex()` `J^2=-id` test as `End` morphism.

* Integral structure (integrable) means `J` comes from holomorphic atlas `M : ComplexMfd`. Newlander-Nirenberg: `J` integrable iff Nijenhuis tensor `N_J =0`. Also `J` integrable iff `T^{0,1} = ker(J+i) ⊂ TM⊗C` is involutive `[T^{0,1}, T^{0,1}]⊂T^{0,1}`.

* Nijenhuis tensor `N_J: Λ^2 TM → TM` as `VecBun` morphism `N_J(X,Y)= [JX,JY] - J[JX,Y] - J[X,JY] - [X,Y]` where `X,Y ∈ Γ(TM)` vector fields, `[-,-]` Lie bracket of fields, `JX ∈ Γ(TM)`. `N_J` is tensorial (`C^∞(M)`-linear in `X,Y`) despite appearance, and `N_J∈Γ(Λ^2 T^*M⊗TM)` with `N_J=0` iff `J` integrable. More generally for `M` with `J`, `N_J` measures failure of `J` to be integrable; interface `J.nijenhuis_tensor() → N_J : Hom(Λ^2TM, TM)` and `J.is_integrable() ⇔ N_J==0` as morphism zero.

* Curvature tensors all derive from a connection `∇` on `TM` (Levi-Civita `∇^{LC}` for `g` metric, or Chern `∇^{Ch}` for `Hermitian` `J`-compatible). For `R : RiemMfd` with `g`, Levi-Civita is unique torsion-free metric-compatible `∇: Γ(TM)→Γ(T^*⊗TM)` with `Γ^k_{ij}` Christoffel and `R(X,Y)Z = ∇_X∇_Y Z - ∇_Y∇_X Z - ∇_{[X,Y]}Z` as `R ∈ Γ(Λ^2 T^*⊗End(TM))` Riemann `(4,0)` via `R(W,Z,X,Y)=g(R(X,Y)Z,W)`. Ricci `Ric(Y,Z)= tr(X↦R(X,Y)Z) ∈ Γ(Sym^2 T^*)` as contraction `Ric_{jk}=R^i_{ijk}`, scalar `S = tr_g Ric = g^{jk}Ric_{jk} : C^∞(M)` function, sectional `K(σ)= R(X,Y,Y,X)/(|X|^2|Y|^2-⟨X,Y⟩^2)` for 2-plane `σ=span{X,Y}`, Gaussian `K = S/2` when `dim=2` via `K = det(Weingarten)` for surface `Σ⊂R^3` vs intrinsic `K = R_{1212}/det g`. Gaussian curvature already intaken as `K` for surfaces via shape operator; now general `R, Ric`.

* For almost Hermitian `(M,J,g)` with `g(JX,JY)=g(X,Y)`, Ricci forms `ρ = Ric(J·,·) ∈ Ω^{1,1}` and `*`-Ricci etc.; integrability links `Ric` to Chern classes `c_1(T^{1,0}) = [Ric(ω)/2π]` via `∇^{Ch}` when `J` integrable Kähler (`∇^{LC}J=0` ⇔ Kähler with `ω=g(J·,·)` closed `dω=0`). Need operators `∇`, `R`, `Ric`, `S`, `N_J` as morphisms `J : End(TM)`, `N_J : Hom(Λ^2TM,TM)`, `R : Hom(Λ^2TM⊗TM,TM)` / `R ∈ Ω^2(End)`, `Ric ∈ Sym^2`, `S ∈ C^∞` on the manifold object `M : SmMfd` with `TM : VecBun_R(M)` (`TM = T_{M/R}`), not as free `curvature(matrix)` lists.

Intended owners: `categories/geometry/almost_complex.py` (`AlmostComplexStructure` `J: TM→TM` with `J^2=-id`, `is_almost_complex`, `is_integrable via N_J==0`), `categories/geometry/complex_structures.py` (`NijenhuisTensor N_J : Λ^2TM→TM` with `N_J(X,Y)=[JX,JY]-J[JX,Y]-J[X,JY]-[X,Y]`, `NewlanderNirenberg`), `categories/geometry/curvature.py` (`RiemannCurvature R∈Γ(Λ^2⊗End)`, `Ricci Ric=tr R`, `Scalar S=tr_g Ric`, `Sectional K(σ)`, `Gaussian K=S/2` in 2d as `det II`, Levi-Civita `∇^{LC}` as `Conn(TM)`), `categories/geometry/kahler.py` (`KahlerStructure` `ω=g(J·,·)` closed, `ChernConnection`). Not a free `nijenhuis(J)` matrix or `ricci(metric)` list — `J.nijenhuis_tensor()` and `g.riemann_tensor()`, `g.ricci()`, `g.scalar_curvature()` on the manifold/structure objects.

## Desired capability: flatness, moduli of flat connections, curvature, Levi-Civita, gauge group, Hermitian, covariant derivatives, gradient/Hamiltonian flows — note 2026-09-15

One needs flatness for connections, moduli of flat connections, curvature associated to a connection, Levi-Civita, the gauge group, Hermitian modules/vector spaces, hermitian metrics, the hermitian form associated to a lattice on `L⊗_ZZ C` (as opposed to its bilinear extension), covariant derivatives. Basic gradient flow, Hamiltonians and Hamiltonian flows.

* Flatness for a connection `∇: E→E⊗Ω^1_X` on `X : Sm` (`X` smooth scheme/manifold `C`), `E: VecBun(X)` rank `n`, is the curvature equation `F_∇ = ∇^2 =0 : E→E⊗Ω^2_X` (`F_∇∈Γ(Ω^2_X⊗End(E))`). Curvature associated to any connection (flat or not) is `F_∇ = ∇∘∇ : E→E⊗Ω^2` as `F_∇(X,Y)=[∇_X,∇_Y]-∇_{[X,Y]} ∈ End(E)`, i.e. `F_∇=dA+A∧A` in trivialization `∇=d+A` with `A∈Ω^1(End)`. Bianchi `d_∇F_∇=0`. Flatness `F_∇=0` ⇔ local system `E^∇ = ker ∇` is `C`-local system rank `n` via Riemann-Hilbert and `∇` corresponds to representation `ρ: π_1→GL_n`. For line bundles, `F_∇=dA` as `Ω^2` class `c_1(E)` via `ch`. Interface `∇.curvature() → F_∇ : Hom(E, E⊗Ω^2)` and `∇.is_flat() ⇔ F_∇==0` as morphism, not as numeric `norm(F)<eps`.

* Levi-Civita `∇^{LC}` is the unique torsion-free metric-compatible connection on `TM` for `M : RiemMfd` with metric `g : Sym^2 T^*M` (`g` positive-definite). Existence via Koszul `2g(∇_XY,Z)=…` Christoffel `Γ^k_{ij}`. `∇^{LC}` has `T(∇^{LC})=0` torsion `T(X,Y)=∇_XY-∇_YX-[X,Y]` and `∇^{LC}g=0`. Curvature above gives `R^{LC}=F_{∇^{LC}}` Riemann, `Ric`, `S` as before. For Kähler `(M,J,g)` with `J` integrable and `ω=g(J·,·)` closed `dω=0`, Levi-Civita coincides on `T^{1,0}` with Chern `∇^{Ch}` and `∇^{LC}J=0`.

* Moduli of flat connections `M_flat = FlatConn(X)//G` as `G`-quotient of affine space `A = {∇=∇_0 + A | A∈Ω^1(End E)}` by gauge `G`. More precisely `M^{ss}_{flat}= {∇ flat, semistable}/∼` via NAH when `X` compact Kähler, but bare `M_flat = {F_∇=0}/G` as Betti `M_B` via `RH: FlatConn^{rs}≃LocSys` and `LocSys ≃ Rep(π_1)//G` already intaken as `M_B`. Need `M_flat` as `GITQuotient(A,G)` stacky `M_flat : Stack` with `π: A^{ss}→M_flat` and `T_{[∇]}M_flat ≅ H^1(X, End(E)⊗…)` deformation via `Ext^1` already intaken. Distinguish `M_flat` (analytic quotient by `G=C^∞` gauge) vs `M_B` (algebraic `//G`).

* Gauge group `G = G(P)= Γ(X, Aut(P))` for principal `G`-bundle `P→X` (`P: Bun_G(X)`) as `Maps_G(P,G)` or `Γ(X, Ad P)` where `Ad P = P×_G G` via conjugation. For vector bundle `E`, `G = Γ(X, GL(E)) = Aut(E)` as sheaf `G(U)=GL(Γ(U,E))`. Lie algebra `Lie(G)=Ω^0(End E)=Γ(End E)`. Action on `A`: `g·∇ = g∇g^{-1}= g∘∇∘g^{-1}` with infinitesimal `g=1+εφ : δ_φ A = -d_∇φ`. Quotient `A/G` stack, stabilizer `Stab(∇)=Aut(∇)= {g | g·∇=∇}=H^0(End E)^{∇}`.

* Hermitian modules/vector spaces: `H : HermSpaces` / `HermModules_R` where `R=ZZ, RR, CC` with `Hilbert` inner product. Object `H = (V, h)` with `V : Vect_C` finite `n` and `h: V×V→C` sesquilinear `h(λv,w)=λh(v,w)`, `h(v,w)=\overline{h(w,v)}`, positive-definite `h(v,v)>0` (`v≠0`). Morphisms are `C`-linear `f: V→W` with `h_W(fv,fw)=h_V` when unitary else `f^*h_W = h_V`. For `R=ZZ`, `HermModules_ZZ` as lattices with Hermitian form after `⊗C`.

* Hermitian metrics `h: E×\bar E → C` on complex vector bundle `E→X` (`X : ComplexMfd / SmMfd` with `C`-structure) as smooth family `h_x: E_x×\bar E_x→C` positive Hermitian, i.e. section `h ∈ Γ(E^∨⊗\bar E^∨)` with `h= \bar h^t`. Chern connection `∇^h = ∂_h + \bar ∂_E` uniquely `∇^h h=0` and `(∇^h)^{0,1}= \bar ∂_E`. Interface `E.hermitian_metric() → h : HermMetrics(E)` with `h.chern_connection() → ∇^h : Conn(E)` and curvature `F_{∇^h} ∈ Ω^{1,1}(End)`.

* Hermitian form associated to a lattice `L` on `L⊗_ZZ C` (as opposed to its bilinear extension): `L : Lattices` integral lattice with bilinear `b: L×L→ZZ` (`b(x,y)=x·y`), e.g. even lattice `A_2, E_8, hyperbolic `U`. Extend scalars `V_C = L⊗_ZZ C : Vect_C` (`V_C = V_R ⊗_R C` with `V_R=L⊗R`). Bilinear extension `b_C: V_C×V_C→C` is `C`-bilinear `b_C(v⊗λ, w⊗μ)= λμ b(v,w)` symmetric. Hermitian form `h_C: V_C×\overline{V_C}→C` is instead sesquilinear `h_C(v⊗λ, w⊗μ)= λ\bar μ b(v,w)` when `b` already extended to `R`-bilinear and then sesquilinear via `C`-antilinear second factor, or more generally `h_C(v,w)=b_C(v, \bar w)` with `w↦\bar w` conjugation on `C` factor. Difference matters: `b_C` is `GL_n(C)` invariant but not positive-definite; `h_C` is `U(n)`-invariant Hermitian `h_C(v,v)∈R_{≥0}` positive when `b_R` positive. For period lattices `L=H^2(X,ZZ)` of K3 `L≅U^3⊕E8(-1)^2`, `h_C` gives Hodge Hermitian `⟨α,\bar β⟩` on `H^{p,q}` and Weil `i^{p-q}h_C` positive. Need both `L.bilinear_form()` `b: Sym^2(L^∨)` vs `L.hermitian_form() → h: Herm(V_C)` as `Sesq`.

* Covariant derivatives: for `∇: E→E⊗Ω^1_X` on `E: VecBun(X)`, `∇_X = ⟨∇,X⟩ : Γ(E)→Γ(E)` for `X∈Γ(TX)`, with Leibniz `∇(fs)= f∇s + s⊗df` and `∇_{fX}=f∇_X`. Iterated `∇^k: Γ(E)→Γ(E⊗Ω^{1⊗k})` via `∇_{X_1,…,X_k}`. For function `f: X→R`, `∇f = df ∈ Ω^1` as `T^*X`; for vector field `Y`, `∇_X Y ∈ Γ(TX)`. For principal `P`, `D_A: Γ(Ad P)→Γ(Ad P⊗T^*X)`.

* Basic gradient flow `γ: R→M` on `M : RiemMfd` with `f: M→R` smooth: `γ̇(t)= -∇f(γ(t))` where `∇f = g^♯(df) ∈ Γ(TM)` via musical `♯: T^*M→TM` (`df(Y)=g(∇f,Y)`). Stable/unstable manifolds, Morse `Hess f = ∇^2 f : Sym^2 T^*M` at `crit(f)`. Interface `f.gradient_flow(γ_0)→γ` as `ODE` in `C^∞(R,M)` via exponential map `exp_p`.

* Hamiltonians and Hamiltonian flows: on symplectic `(M,ω)` `ω∈Ω^2(M)` closed nondegenerate (`ω^n` volume when `dim=2n`), Hamiltonian `H: M→R` defines `X_H ∈ Γ(TM)` via `ι_{X_H}ω = dH` (`ω(X_H,·)=dH`), i.e. `X_H = ω^♯(dH)` via `♯_ω: T^*M→TM`. Flow `φ_H^t: M→M` generated by `X_H` with `d/dt φ_H^t = X_H∘φ_H^t`, `φ_H^0=id`, preserves `ω` (`L_{X_H}ω=0`) and `H` along flow when `H` time-independent (`d/dt H∘φ=0` if `∂_tH=0`). Lagrangian `Lagrangian(H)=graph(dH) ⊂ T^*M` etc. For time-dependent `H_t: M×R→R`, `X_{H_t}` similarly. Interface `H.hamiltonian_vector_field(ω)→X_H`, `H.hamiltonian_flow(ω, t)→φ^t`.

Intended owners: `categories/connections/curvature.py` (`curvature(F_∇)=∇^2 : E→E⊗Ω^2`, `is_flat ⇔ F=0`, `Bianchi`), `categories/moduli/flat_connections.py` (`ModuliFlat = FlatConn//G` as `GITQuotient` stack `M_flat = {F=0}/G` with `T_{[∇]}≅H^1(End)`), `categories/connections/gauge_group.py` (`GaugeGroup(P)=Γ(Aut P)` with `Lie(G)=Ω^0(End)`, action `g·∇=g∇g^{-1}`), `categories/geometry/levi_civita.py` (`LeviCivita(g) → ∇^{LC}: Γ(TM)→Γ(T^*⊗TM)` `T=0`, `∇g=0`), `categories/geometry/hermitian.py` (`HermitianSpace (V,h)`, `HermitianMetric h:E×\bar E→C`, `chern_connection` `∇^h`), `categories/lattices/hermitian_forms.py` (`Lattice.hermitian_form() → h: V_C×\bar V_C→C` vs `bilinear_form() → b: V_C×V_C→C` sesquilinear vs bilinear), `categories/connections/covariant_derivative.py` (`∇_X : Γ(E)→Γ(E)` `∇(fs)=f∇s+s⊗df`), `categories/dynamics/gradient_flow.py` (`GradientFlow(f,g) → γ̇=-∇f`), `categories/dynamics/hamiltonian.py` (`Hamiltonian H: M→R` with `X_H=ω^♯ dH`, `hamiltonian_flow φ_H^t` preserving `ω`). Not free `curvature(A)` matrix or `hamiltonian_flow(H)` bare ODE — `∇.curvature()`, `g.levi_civita()`, `P.hermitian_form()` vs `bilinear_form()`, `∇_X(s)`, `f.gradient_flow()`, `H.hamiltonian_flow(ω)` on the bundle/manifold/symplectic objects.

## Desired capability: Teichmüller space and Weil-Petersson metric — note 2026-09-15

Teichmüller and the Weil-Petersson metric.

* Teichmüller space is not a bare `T_g` symbol. For `g: NN`, `g≥2`, `Σ_g : Top` closed orientable surface genus `g` with `π=π_1Σ_g = ⟨a_i,b_i|∏[a_i,b_i]=1⟩` (already intaken as `SurfaceGroup(g)`), `T_g : ComplexMfd` is `T_g = {J : AlmostComplex on Σ_g with J integrable, orientation preserving}/Diff_0(Σ_g)` i.e. `ComplexStructures(Σ_g)/∼` where `J_1∼J_2` if `∃φ∈Diff_0(Σ_g)` isotopic to `id` with `φ^*J_2=J_1`. Point `[J]∈T_g` is marked Riemann surface `X_J=(Σ_g,J)` genus `g` with marking `Σ_g→X_J` up to isotopy. `dim_C T_g = 3g-3`, `dim_R =6g-6`, contractible Stein manifold `T_g ≅ C^{3g-3}` via Bers embedding. Interface `SurfaceGroup(g).teichmuller_space() → T_g : ComplexMfd` with `T_g.marked_surface() → X_J : RiemannSurface` and `Diff_0` quotient as `MCG` action below.

* Moduli `M_g = T_g / MCG_g` where `MCG_g = Mod(Σ_g)= Diff^+(Σ_g)/Diff_0(Σ_g)= Out(π_1Σ_g)` mapping class group action `MCG_g ↷ T_g` properly discontinuous by `φ·[J]=[φ^*J]`. `M_g : DeligneMumfordStack` (orbifold) `dim_C=3g-3` with coarse moduli `M_g^{coarse}` quasi-projective; `T_g→M_g` is `MCG_g`-covering (orbifold universal cover) and universal curve `C_g→T_g` with fiber `X_J`.

* Weil-Petersson metric `g_{WP}` is not a formal `wp_metric`. For `[J]∈T_g`, tangent `T_{[J]}T_g ≅ H^1(X_J, T_{X_J}) ≅ H^0(X_J, K_{X_J}^{⊗2})^∨` via Kodaira-Spencer (Bers: Beltrami differentials `μ∈Ω^{-1,1}=Γ(\bar K^{-1}⊗K)` modulo ` \bar ∂`); cotangent `T^*_{[J]}T_g ≅ Q(X_J)=H^0(X_J, K^{⊗2})` quadratic differentials `q = q(z)dz^2`. Pairing via hyperbolic metric `ρ_J` on `X_J` (unique metric of curvature `-1` in conformal class of `J`, `ρ_J = λ(z)|dz|^2` with `λ=1/Im z` for uniformization `X_J= H/Γ`). Then for `μ_1, μ_2 ∈ H^1(T_X)` corresponding to `q_1,q_2`, `g_{WP}(μ_1, μ_2)= ∫_{X_J} μ_1 \bar μ_2 ρ_J^{-1}` as `L^2` pairing, or dually `⟨q_1,q_2⟩_{WP}= ∫_{X_J} q_1 \bar q_2 / ρ_J`. More invariantly `g_{WP}= ∫_{X_J} |q|^2 / ρ` after identifying `μ = \bar q / ρ`. This defines Hermitian metric `h_{WP}` on `T^{1,0}T_g`, Kähler with Kähler form `ω_{WP}= i∂\bar ∂ log det`? Actually `ω_{WP} = i/2 ∂\bar ∂ S` where `S` is Liouville? Equivalent via `ω_{WP}` closed. Weil-Petersson is Kähler, negatively curved, incomplete, with completion ` \bar T_g` Deligne-Mumford ` \bar M_g`.

* Interface `T_g.weil_petersson_metric() → g_{WP} : HermitianMetric` on `T_g : ComplexMfd` with `g_{WP}: T_{T_g}×\overline{T_{T_g}}→C` as above, `ω_{WP}= Im g_{WP}` Kähler `2`-form, curvature `R_{WP}` as `Ω^{1,1}(End(T_{T_g}))` with dual Nakano negativity, etc. Coupled to Teichmüller metric `g_T` (Finsler via `||q||_1 = ∫|q|`), but WP is Hermitian `L^2`.

* Pants decompositions, Fenchel-Nielsen: `T_g` parametrized by `3g-3` length-twist pairs `(ℓ_i, τ_i)∈R_{>0}×R` from maximal collection of disjoint simple closed curves `C_i` cutting `Σ_g` into `2g-2` pairs of pants `P_j≅S^2\3disks`. For `X_J` with hyperbolic `ρ_J`, `ℓ_i = length_{ρ_J}(C_i)` geodesic length, `τ_i` twist around `C_i`. `T_g ≅ R_{>0}^{3g-3}×R^{3g-3}` via FN, and `ω_{WP}= Σ_i dℓ_i ∧ dτ_i` (Wolpert). Effective model needs `CurveComplex(Σ_g)` and `PantsDecomposition` objects.

Intended owners: `categories/teichmuller/teichmuller_space.py` (`TeichmullerSpace(g) → T_g : ComplexMfd` as `ComplexStructures/Diff_0`, `ModuliSpace M_g = T_g/MCG_g` with `MCG_g=Mod(Σ_g)` action, pants `PantsDecomposition`), `categories/teichmuller/weil_petersson.py` (`WeilPeterssonMetric` `g_{WP}` as `HermitianMetric` on `T_g` via `L^2` of `Q(X)=H^0(K^{⊗2})` against `ρ_J`, `ω_{WP}` Kähler, with `hyperbolic_metric X_J → ρ_J` via uniformization, and `fenchel_nielsen_coords` with `ω_{WP}=Σ dℓ∧dτ`). Not a free `weil_petersson(g)` number — `T_g.weil_petersson_metric()` on the Teichmüller object with `Q(X)` and `ρ_J` as data.

## Desired capability: slopes of vector bundles — and checking (semi)stability — note 2026-09-15

Slopes of vector bundles. And checking (semi)stability.

* Slope is not a bare rational `deg/rank` with `deg` as integer. For `X : SmProj` (curve, surface, higher) with polarization `H : AmpleDiv(X)` (or Kähler form `ω`) and `E : VecBun(X)` / `CohSh(X)` torsion-free coherent, `rank(E)=ch_0(E) : ZZ_{>0}` and `deg_H(E)=c_1(E)·H^{dim X-1} : ZZ` (intersection number via `A^1·A^{dim-1}`, or `deg_H(E)=∫_X c_1(E)∧ω^{n-1}`) — both as `Chow`/`cohomology` classes already intaken via Chern calculus. Slope `μ_H(E)= deg_H(E)/rank(E) : QQ` as element `μ: CohTorsionFree(X) → QQ` (or `RR` when `ω` real). For Higgs `(E,φ)`, same `μ(E)` with `φ`-invariant `F` in semistability test; for parabolic bundles `par μ = (deg + Σ α_i· wt_i)/rank`.

* (Semi)stability is not a string tag. `E` is semistable (resp. stable) if for every proper nonzero subsheaf `F⊂E` (resp. proper `φ`-invariant `F` for Higgs, or subbundle) with `0<rank(F)<rank(E)` and torsion-free quotient, `μ_H(F) ≤ μ_H(E)` (resp. `<`). Equivalently maximal destabilizing subsheaf `F_max ⊂ E` with `μ(F_max)=μ_max(E) = max_{F⊂E} μ(F)` satisfies `μ_max ≤ μ(E)` (semistable) / `<` (stable). Polystable means `E ≅ ⊕_i E_i` with each `E_i` stable and `μ(E_i)=μ(E)` (direct sum of stable of same slope; equivalently `E` semistable and `gr_{JH}(E)=⊕ gr_i` polystable Jordan–Hölder graded). And polystability (and checking it) is required: `E` is polystable iff `E` is semistable and `E ≅ gr_{JH}(E)` as `⊕_i` of its Jordan–Hölder stable factors (or via Kobayashi-Hitchin: admits Hermite–Einstein `h` with `iΛF_h = μ(E)·id`). Unstable means ∃`F` with `μ(F)>μ(E)`.

* Checking (semi)stability must be operational for effective bundles where subsheaves are enumerable via `QCoh` `Sub(F)` as Quot scheme `Quot(E,P)` strata. For `E` on curve `X` smooth projective curve (already intaken with `Hilb` and `Quot`), use existing `Quot(E)` parameterization: `Quot(E) = ∐_P Quot(E,P)` with `P` Hilbert polynomial `P_F(m)= rank(F)·deg H·m + deg(F)+ rank(F)(1-g)`; each `Quot(E,P)` projective `Sch` with computable `EC` when `X` with finite affine cover. Then `μ_max(E)` is `max_{F∈Quot}` finite over destabilizing candidates bounded by `deg(F) ≤ rank(F)·μ_max` plus boundedness theorem (Grothendieck ` Quot` bounded). For `E` on curve, Harder-Narasimhan filtration provides certificate: unique `0=E_0⊂E_1⊂…⊂E_ℓ=E` with each `gr_i=E_i/E_{i-1}` semistable and `μ(gr_1)>…>μ(gr_ℓ)` strictly decreasing; then `E` semistable ⇔ `ℓ=1`, stable ⇔ `ℓ=1` and no proper `F` with same `μ` (i.e. `E` simple `End(E)=k`). HN is computed via iterative maximal destabilizing `E_1 = F_max` and recursion. Interface `E.slope(H) → μ : QQ`, `E.is_semistable(H) → Bool` via `μ_max(E) ≤ μ(E)` with witness `F_max` when false, `E.is_stable(H)`, `E.harder_narasimhan(H) → 0⊂E_1⊂…⊂E` as filtered bundle with `gr_i` semistable.

* For `X` higher dimension (`dim≥2`) with polarization `H`, same definition but `Quot` boundedness via `μ`-bounded family uses `deg_H` and `rank` as above and Bogomolov-type bounds `Δ(E)=2rc_2-(r-1)c_1^2` already intaken via Chern; effective check requires bounding `deg(F)` candidates via `F∈Quot(E, c_1,d)` finite. Not just curve case; Higgs `φ`-invariance restricts to `F` with `φ(F)⊂F⊗Ω^1`.

* Requires: Chern data `c_1, rank` already intaken via `chern_class`; `Quot` scheme `Quot(E,P) : Sch` with `EC` effective (already via Hilbert schemes lead); `Hilbert polynomial` `P: QQ[t]` via `RΓ`; `Filt` from earlier `FiltCh` lead for HN filtration as filtered vector bundle.

Intended owners: `categories/vector_bundles/slope.py` (`slope(E,H)=deg_H/rank : QQ`, `mu_max(E,H)` via `Quot`), `categories/vector_bundles/stability.py` (`is_semistable(E,H) ⇔ ∀F⊂E μ(F)≤μ(E)` with certificate `F_max`, `is_stable`, `is_polystable` ⇔ `E ≅ ⊕_i E_i` stable same `μ` / `E ≅ gr_{JH}(E)` / Hermite–Einstein `iΛF_h=μ·id`, `harder_narasimhan(E,H)→Filt(E)` with `gr` semistable and `μ` decreasing, `jordan_holder` for `S`-equivalence and `gr_{JH}`), `categories/moduli/higgs.py` (`HiggsSemistable` via `φ`-invariant `F`). Not a free `is_semistable(E)` bare `deg/rank` table — `E.slope(H)`, `E.is_semistable(H)`, `E.is_polystable(H)`, `E.harder_narasimhan(H)` on the bundle with `H: Ample` polarization and `Quot(E)` behind `μ_max`.

