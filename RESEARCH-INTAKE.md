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
| Algebraic surface geography, Enriques–Kodaira classification, Chern numbers (c_1^2, c_2), Hodge diamonds | https://superficie.info/ — le superficie algebriche (Belmans–Commelin) + https://github.com/superficie/superficie-algebriche | Numerical invariants and geography of minimal complex algebraic surfaces (c_1^2, c_2, Kodaira dimension κ, irregularity q, geometric genus p_g, Euler characteristic e, Betti and Hodge numbers); source of oracle calculations for surface invariants and specimen tests; reference architecture for interactive mathematical geography tools |
| Fano 3-folds geography, Iskovskikh–Mori–Mukai classification, derived categories | https://fanography.info/ — Fanography (Belmans) + https://github.com/fanography/fanography | Classification and numerical invariants of 105 smooth Fano 3-fold families; Picard rank ρ=1..10, index r, degree (-K_X)^3, genus g, Betti/Hodge numbers, intermediate Jacobians, derived categories D^b(X) (Kuznetsov components, semi-orthogonal decompositions), Hilbert schemes of lines/conics, blowup/contraction diagrams; oracle source for 3-fold geometry |
| Generalized Grassmannians G/P, homogeneous spaces, Schubert calculus, exceptional collections | https://www.grassmannian.info/ — grassmannian.info (Belmans) + https://github.com/pbelmans/grassmannian.info | Homogeneous varieties G/P for simple groups of types A..G; dimension, index, Picard number, Betti numbers (Schubert calculus, Bruhat order), cohomology rings H^*(G/P;ZZ), homogeneous vector bundles via Borel–Weil–Bott, full exceptional collections in D^b(G/P); oracle source for homogeneous spaces and Schubert calculus |
| Scheme and morphism adjectives, automated property deduction, Stacks Project counterexamples | https://adjectivesproject.org/ — The Adjectives Project (Vogel–Holmes) + https://github.com/jessetvogel/adjectives-project-data | 19 scheme properties, 44 morphism properties, 95 implication theorems, 107 concrete examples/counterexamples; deductive inference engine for geometric properties; normative reference for preamble scheme/morphism predicate calculus and test oracles |
| General topology counterexamples, separation/compactness/countability axioms, topological spaces | https://topology.pi-base.org/ — π-Base + https://github.com/pi-base/data | 246 topological properties, 224 canonical topological spaces, 931 deduction theorems, universal constructions (subspaces, products, coproducts, quotients); comprehensive counterexample and predicate suite for preamble topology |

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
| Zeta of varieties / Weil conjectures (concrete cases) | User note 2026-09-15 | `Z(X/F_q,T)` for `X/F_q`; closed forms via explicit `|X(F_{q^r})|` for `A^n, P^n, Gr(k,n)`, some curves; verify Weil (rationality, functional equation, RH) via graded `H^*_{c,ét} : GrMod` with `H^*.graded_piece(i)=H^i_{c,ét}` | `categories/zeta/zeta.py` + `categories/varieties/point_counts.py` | Proposed — see note below |
| Lefschetz trace operationalized (Frob) | User note 2026-09-15 | Operationalize `N_r = Σ (-1)^i Tr(Frob^r \| H^*_{c,ét}(Q_ℓ).graded_piece(i))` — compute `Tr(Frob)` on graded `H^*_{c,ét} : GrMod` | `categories/etale/trace_formula.py` + `categories/etale/frobenius.py` | Proposed — see note below |
| HH(A) — Hochschild (co)homology | User note 2026-09-16 | Hochschild homology `HH_*(A) : GrMod` with `HH_n = Tor_n^{A^e}(A,A)` and cohomology `HH^*(A) : GrAlg` with `HH^n = Ext^n_{A^e}(A,A) = H^n(RHom_{A^e}(A,A))`; complex `C(A)`, `HH = H_*(C)`, `HH^* = H^*(RHom)`, HKR, Gerstenhaber bracket, cup product | `categories/homology/hochschild.py` + `categories/algebras/dg_algebras.py` | Proposed — see note below |
| Content ideal `c_M(x)` of an element `x∈M` | User note 2026-09-16 | For `R : CommRings`, `M : R-Mod`, `x∈M`, evaluation `ev_x: Hom_R(M,R) → R, f↦f(x)` is `R`-linear, image `c_M(x) ⊲ R` ideal (content of `x`); Lemma 3.4: if `M` free finite rank and `x≠0` then `c_M(x) ≠ 0` in `R` | `categories/modules/content.py` + `categories/modules/dual.py` + `categories/modules/free_modules.py` | Proposed — see note below |
| Annihilators and element-wise methods via annihilator ideals | User note 2026-09-16 | For `R : CommRings`, `M : R-Mod`, `x∈M` and `N≤M`, `Ann_R(x) = {r∈R | r·x=0} ⊲ R`, `Ann_R(M) = {r∈R | r·M=0} = ∩_{x∈M} Ann_R(x) ⊲ R`, `Ann_R(N) = ∩_{x∈N} Ann_R(x)`; `M=0 ⇔ Ann_R(M)=R`, `M` faithful `⇔ Ann_R(M)=0`, `x=0 ⇔ Ann_R(x)=R`, `x` torsion `⇔ Ann_R(x)≠0` (when `R` domain), replace element-wise `is_zero`, `is_torsion`, `is_faithful` with ideal properties | `categories/modules/annihilator.py` + `categories/modules/torsion.py` + `categories/modules/faithful.py` | Proposed — see note below |
| Shortcuts for common matrices — Jordan blocks, banded, tridiagonal, antidiagonal, symplectic form | User note 2026-09-16 | Shortcuts `JordanBlock_n(λ)`, `BandedMatrix(bandwidth)`, `TridiagonalMatrix(diag, super, sub)`, `AntidiagonalMatrix(vec)`, `SymplecticFormMatrix(g) = [0 I_g; -I_g 0]` and variants, `J_{2g}` standard symplectic, etc., as `Mat_{n}(R) : R-Mod` endomorphisms with correct parent, not hand-rolled `Matrix([...])` lists | `categories/matrices/common_matrices.py` + `categories/matrices/jordan.py` + `categories/matrices/banded.py` + `categories/matrices/symplectic.py` | Proposed — see note below |
| Rational canonical form (Frobenius normal form) | User note 2026-09-16 | For `A : Mat_n(F)` over field `F` (or PID `R`), `RCF(A) = diag(C(p_1),…,C(p_r))` with companion matrices `C(p_i)` of invariant factors `p_1 | … | p_r`, `p_r = m_A` minimal polynomial, `∏ p_i = χ_A` characteristic polynomial, `F^n ≅ ⊕ R[x]/(p_i)` as `F[x]`-module via `x·v = Av` | `categories/matrices/rational_canonical.py` + `categories/modules/frobenius_form.py` + `categories/matrices/companion.py` | Proposed — see note below |
| Matrix spaces over `R` as fibered category `Mat(R)` with objects `NN` and `Mat_{n,m}(R)`, module morphisms via matrices as honest functor | User note 2026-09-16 | Reformulate `Mat_{n×m}(R)` as hom-sets of category `Mat(R)` fibered over `Rings` with `Ob = NN` and `Hom_{Mat(R)}(n,m)=Mat_{m×n}(R)`, composition via matrix multiplication, fiber over `R` is `Mat(R)`, and formalize that `Hom_R(R^n,R^m) ≅ Mat_{m×n}(R)` and more generally for modules with chosen basis/presentation, `Hom_R(M,N)` realized via matrices as functor `Mat(R) ⇄ Free(R-Mod)` and `Mat(R) → Mod_R` (and for f.p. modules via presentation matrices) | `categories/matrices/fibered_category.py` + `categories/modules/free_modules.py` + `categories/functors/matrix_functor.py` + `categories/matrices/hom_sets.py` | Proposed — see note below |
| Honest products and pullbacks of categories, categories fibred over other categories, stacks | User note 2026-09-16 | For `C,D : Cat`, product `C×D` with `Ob(C×D)=Ob(C)×Ob(D)`, `Hom((c,d),(c',d'))=Hom_C(c,c')×Hom_D(d,d')`; pullback `C×_E D` for `C→E←D` with `Ob = {(c,d,α: F(c)≅G(d))}` (or strict `F(c)=G(d)`), fiber products in `Cat`; categories fibred over `B` via `p: E→B` with cartesian lifts, fiber `E_b = p^{-1}(b)`, cleavage, descent; stacks as fibred categories satisfying effective descent for covers, 2-sheaf condition leading to algebraic stacks | `categories/cat/products.py` + `categories/cat/pullbacks.py` + `categories/fibered/fibered_categories.py` + `categories/stacks/stacks.py` | Proposed — see note below |
| `Top` and `Top_*`, `S = Spaces =` homotopy types `= ∞-groupoids` | User note 2026-09-16 | `Top : Cat` with `Ob =` topological spaces, `Hom =` continuous maps, `Top_* = Top_{*/}` pointed with `Ob = (X,x_0)` and `Hom_*` basepoint-preserving; `S = Spaces = ∞Grpd` as `∞`-category of homotopy types (`Kan` complexes / `CW` up to weak equivalence), `S ≃ Top[W^{-1}]` with `W =` weak homotopy equivalences, `S ≃ ∞Grpd` via `Sing`/`|-|` | `categories/top/top.py` + `categories/top/pointed.py` + `categories/spaces/spaces.py` | Proposed — see note below |
| Simplicial complexes and Kan complexes operationalized | User note 2026-09-16 | Simplicial complex `K` as finite family of simplices closed under faces, geometric realization `|K| : Top`, specialization to Kan complex `Kan ⊂ sSet` with horn fillers `Λ^n_k → K` for `0≤k≤n`, effective Kan via `Sing(X)` and as fibrant replacement `Ex^∞`, Quillen model `sSet_{Quillen}` with `Kan` fibrant | `categories/simplicial/complexes.py` + `categories/simplicial/kan.py` + `categories/topology/simplicial_sets.py` | Proposed — see note below |
| Categories from finitary data — graphs, posets, topologies on a space | User note 2026-09-16 | Construct `Cat` from finitary data: `Graph → FreeCat(Graph)` free category on directed graph, `Poset → PosetCat` with `Hom(x,y)=1` if `x≤y` else `∅`, `Top(X,τ) → Cat` via `Op(X)` poset category of opens or `Π_1(X)` fundamental groupoid, more generally `FinSet` data → `Cat` with finite `Ob`, `Hom` via generators and relations | `categories/cat/finitary.py` + `categories/graphs/free_category.py` + `categories/posets/poset_category.py` + `categories/topology/topology_to_category.py` | Proposed — see note below |
| (Homotopy coherent) nerve of finitary category as Kan complex | User note 2026-09-16 | For `C : Cat` relatively finitary (finite `Ob`, finite `Hom` via graph/poset/topology presentation), (homotopy coherent) nerve `N(C) : sSet` with `N(C)_n = Fun([n],C)` (or `N_{hc}(C)` with `Map(i,j) = Hom_C(i,j)` as spaces), and when `C` is groupoid or `S`-enriched, `N(C)` is Kan; need actual `Kan` complex object computable from finitary presentation, with `Sing`, `|-|`, `Ex^∞` and effective horn fillers | `categories/nerve/nerve.py` + `categories/nerve/homotopy_coherent_nerve.py` + `categories/simplicial/kan.py` | Proposed — see note below |
| Lurie's tangent category, cotangent complex, classical obstruction theories, DGLAs, Sullivan minimal models | User note 2026-09-16 | `T_C : Cat` tangent category at `C : Cat` via `T_C = Exc_*(S^{fin}_*, C)` or `T_X = Stab(C_{/X})` for `X : C`, cotangent complex `L_{X} : T_X` as `L_{X}=L_{X/C}` with `L_{A/k}` for `A : CAlg_k`, obstruction theory `E → L_{X}` perfect with `h^i(E)`, DGLA `g` governing deformations via Maurer-Cartan `MC(g)`, Sullivan minimal model `M_X = (ΛV,d) → A_{PL}(X)` for `X : Top_{nil}` | `categories/tangent/tangent_category.py` + `categories/deformation/cotangent_complex.py` + `categories/deformation/obstruction_theories.py` + `categories/dgla/dglas.py` + `categories/rational/sullivan.py` | Proposed — see note below |
| Yoneda and coYoneda embeddings, Mor as functor from `C×C^{op}` with currying, functor of points | User note 2026-09-16 | For any `C : Cat`, Yoneda `y: C → Fun(C^{op},Set)` with `y(c)=Hom_C(-,c)` and coYoneda `y^{op}: C^{op} → Fun(C,Set)` with `y^{op}(c)=Hom_C(c,-)` as fully faithful honest functors; operationalize `Mor: C^{op}×C → Set` as functor from honest product `C×C^{op}` admitting currying `C → Fun(C^{op},Set)` via `Hom_C(-,-)` to produce Yoneda/coYoneda; functor of points `h_X = Hom(-,X) : C^{op} → Set` for any `X : C` | `categories/yoneda/yoneda.py` + `categories/yoneda/coyoneda.py` + `categories/hom/mor_functor.py` + `categories/functor_of_points.py` | Proposed — see note below |
| Abelianization, centers, centralizers, stabilizers, Hurewicz | User note 2026-09-16 | `Ab: Groups → AbGroups` abelianization `G^{ab}=G/[G,G]` left adjoint to inclusion `Ab⊂Groups`; center `Z(G)={g∈G | ∀h, gh=hg} ⊲ G`, centralizer `C_G(S)={g | ∀s∈S, gs=sg} ≤ G`, stabilizer `Stab_G(x)={g | g·x=x} ≤ G` for `G↷X`, center `Z(R)={r∈R | ∀s, rs=sr} ⊂ R` for `R : Rings`; Hurewicz `h_{n}: π_n(X,x) → H_n(X;ZZ)` for `X : Top_*` (and stable `π_n^s → H_n`) via `π_n(X)→π_n(X,X^{n-1})≅H_n` | `categories/groups/abelianization.py` + `categories/groups/center.py` + `categories/groups/centralizer.py` + `categories/rings/center.py` + `categories/homotopy/hurewicz.py` | Proposed — see note below |
| Implicitly deriving tensor and hom, tensor-hom and power/copowering adjunctions, enriched structures, induction/restriction | User note 2026-09-16 | Implicitly derive `⊗` and `Hom` where possible (`⊗^L`, `RHom`, `L f^*`, `R f_*`), tensor-hom adjunction `Hom(X⊗Y,Z) ≅ Hom(X,Hom(Y,Z))` and enriched/2-categorical version, more general power `X^K` / copower `K·X` adjunctions `Hom(K·X,Y) ≅ Hom(K,Map(X,Y)) ≅ Hom(X,Y^K)` for `K : S`, `V`-enriched `Hom_V`; attach `V`-enriched structures where theorems give them (`Top` is `S`-enriched, `Cat` is `Cat`-enriched, `Ch(R)` is `Ch`-enriched, etc.); induction `Ind_H^G = R[G]⊗_{R[H]} - : R[H]-Mod → R[G]-Mod` left adjoint to restriction `Res_H^G`, `Frobenius reciprocity Hom_{R[G]}(Ind V,W) ≅ Hom_{R[H]}(V,Res W)` and `CoInd` right adjoint | `categories/derived/implicit_deriving.py` + `categories/monoidal/tensor_hom.py` + `categories/enriched/power_copower.py` + `categories/enriched/enriched.py` + `categories/representation/induction_restriction.py` | Proposed — see note below |
| Axiomatic subcategories of `Cat`, `show(C)`, limits/colimits, monads, `QX`, interchange | User note 2026-09-16 | Place existing categories into axiomatic subcategories of `Cat`: `Abelian`, `Complete`, `Cocomplete`, `Bicomplete`, `HasProducts`, `HasCoproducts`, `HasPullbacks`, `HasPushouts`, `HasEqualizers`, `HasCoequalizers`, `HasLimits`, `HasColimits`, `CartesianClosed`, etc., enrich `show(C)` to display known properties for audit; reasonable computational limits/colimits at least filtered or `ZZ`-indexed (directed colimits, inverse limits), equalizers `Eq(f,g)` and coequalizers `Coeq(f,g)`; monads `T: C→C` with `η,μ` and algebras `Alg_T`; `QX` for `X : Top` (e.g. `QX = Ω^∞Σ^∞ X` or `Q-construction`); basic interchange for limit/colimit calculus: `Hom(lim_i X_i, Y) ≅ lim_i Hom(X_i,Y)`, `Hom(X, colim_i Y_i) ≅ colim?` when adjoints, commuting with adjoints `L ⊣ R` gives `L(colim) ≅ colim L`, `R(lim) ≅ lim R`, Fubini `lim_i lim_j ≅ lim_{i,j}`, etc. | `categories/cat/axioms.py` + `categories/cat/show.py` + `categories/limits/filtered.py` + `categories/limits/equalizers.py` + `categories/monads/monads.py` + `categories/top/qx.py` + `categories/limits/interchange.py` | Proposed — see note below |
| Gauss-Manin + six functors + R f_* | User note 2026-09-15 | Gauss-Manin connection, six-functor formalism for sheaves, derived functors (esp. `R f_*`) | `categories/functors/gauss_manifold.py` + `categories/sheaves/six_functors.py` + `categories/derived/` | Proposed — see note below |
| Étale / ℓ-adic and Galois cohomology via sites — honest and operationalized, computable in some cases | User note 2026-09-16 | Honest `Q_ℓ`, `H^*_ét : GrMod`, `H^*(Gal,-) : GrMod` as specialization of site cohomology with `H^*.graded_piece(i)=H^i`; Grothendieck topologies, sites, sieves, covering families — operationalized and computable in some cases (finite-type `X/F_q` with finite affine/étale cover, lisse `Q_ℓ` via `Z/ℓ^n` system, comparison via `RΓ` as effective `Ch`, MW/rigid adapter when needed) | `categories/topology/sites.py` + `categories/etale/` + `categories/galois/` | Proposed — see note below |
| Derived Hom / tensor — Ext, Tor, D(R-Mod) | User note 2026-09-15 | `RHom`, `Ext^n = R^n Hom`, `⊗^L`, `Tor_n = L_n(⊗)` in `D(R-Mod)`; derived tensor products `A⊗^L_R B` | `categories/derived/derived_category.py` + `categories/homological/ext_tor.py` / `categories/derived/tensor_product.py` | Proposed — see note below |
| Attaching homological notions to modules — free resolutions then apply functor and take homology for derived functors | User note 2026-09-16 | For `M : R-Mod`, attach `Tor, Ext, L_nF, R^nF` as homological notions to the module; operationalize via free (or projective) resolution `P_• → M → 0` with `P_i` free finite rank, apply functor `F` (e.g. `Hom_R(-,N)`, `-⊗_R N`, `f^*`, etc.) to `P_•` to get `F(P_•) : Ch`, then `H_n(F(P_•)) = L_nF(M)` or `H^n(F(P_•)) = R^nF(M)` as graded `H_*`/`H^* : GrMod` with `H.graded_piece(n)` | `categories/modules/homological.py` + `categories/homological/free_resolutions.py` + `categories/derived/derived_functors.py` + `categories/modules/free_modules.py` | Proposed — see note below |
| Yoneda product on `Ext` operationalized | User note 2026-09-16 | Yoneda splice `Ext^p(B,C) ⊗ Ext^q(A,B) → Ext^{p+q}(A,C)` as composition `Hom_{D(R)}(B,C[p]) ⊗ Hom_{D(R)}(A,B[q]) → Hom_{D(R)}(A,C[p+q])` via `RHom`, `D(R-Mod)` with `Ext^n(A,B)=Hom_{D(R)}(A,B[n])`; splice of extensions `0→C→E_1→B→0` and `0→B→E_2→A→0` to `0→C→…→A→0`; computable via free resolutions `P_•→A`, `Q_•→B` and chain maps `P_•→Q_•[q]` representing classes, then compose | `categories/homological/yoneda_product.py` + `categories/derived/derived_category.py` + `categories/homological/ext_tor.py` + `categories/homological/free_resolutions.py` | Proposed — see note below |
| `MU` and `BP`, spectra, `E_n` ring spectra, `E_n` module spectra, `A_n` ring spectra, free `E_n` algebra functors | User note 2026-09-16 | `MU = Thom(MU)` complex cobordism `MU_* = π_*(MU) = ZZ[x_1,x_2,…]`, `BP = BP_{(p)}` summand of `MU_{(p)}` with `BP_* = ZZ_{(p)}[v_1,…]`, spectra `Sp` as `Spectra` stable `∞`-category `Sp = Sp(Top_*)`, `E_n` ring spectra as `E_n`-algebras in `Sp` (`E_n` operad), `E_n`-modules, free `E_n` algebra `Free_{E_n}: Sp → Alg_{E_n}(Sp)` left adjoint to forgetful, `A_n` ring spectra as `A_n`-algebras (`A_n` operad interpolating associative) | `categories/spectra/spectra.py` + `categories/spectra/mu.py` + `categories/spectra/bp.py` + `categories/spectra/e_n_ring.py` + `categories/spectra/e_n_modules.py` + `categories/spectra/free_e_n.py` + `categories/spectra/a_n.py` | Proposed — see note below |
| Morava `K(n)` and `K(n)`-local spheres, heights of Morava `E`-theories, `p`-local and `p`-complete spheres, fibers and cofibers in spectra | User note 2026-09-16 | `K(n)` Morava K-theory at prime `p` height `n` with `K(n)_* = F_p[v_n^{±1}]`, `|v_n|=2(p^n-1)`, `K(n)`-localization `L_{K(n)}: Sp → Sp_{K(n)}` and `K(n)`-local sphere `L_{K(n)}S^0`, heights `n = ht(E)` for Morava `E = E_n = E(k,Γ)` Lubin-Tate `E_* = W(k)[[u_1,…,u_{n-1}]][u^{±1}]`, `p`-local `S^0_{(p)}` and `p`-complete `S^0^{∧}_p = lim_k S^0/p^k` as `L_{M(p)}` and `L_{S/p}`, and fibers `fib(f: X→Y)` and cofibers `cofib(f)= Y ∪_X CX` in `Sp` as `Sp` is stable with `fib ≃ cofib[-1]` | `categories/spectra/morava_k.py` + `categories/spectra/morava_e.py` + `categories/spectra/localization.py` + `categories/spectra/p_local.py` + `categories/spectra/fibers_cofibers.py` | Proposed — see note below |
| Framed manifolds, factorization homology | User note 2026-09-16 | `Mfld^{fr}_n` category of framed `n`-manifolds with embeddings as morphisms, factorization homology `∫_M A = colim_{Disk^{fr}_{n/M}} A` for `E_n`-algebra `A : Alg_{E_n}(Sp)` (or `C`), with `∫_{R^n} A ≃ A` and excision `∫_{M ∪_{M_0×R} N} A ≃ ∫_M A ⊗_{∫_{M_0×R} A} ∫_N A`, for `A =` `E_n`-algebra, computes `HH` etc. | `categories/manifolds/framed.py` + `categories/factorization/factorization_homology.py` | Proposed — see note below |
| `(-)^{hG}` and `(-)_{hG}` functors | User note 2026-09-16 | For `G : Groups` finite (or `G : Spaces` as `∞`-group), `X : Sp^{BG} = Fun(BG,Sp)` with `G`-action, homotopy fixed points `X^{hG} = lim_{BG} X = Map_{Sp^{BG}}(1, X)` and homotopy orbits `X_{hG} = colim_{BG} X = 1 ⊗_{G} X` as `Sp`-valued `lim`/`colim` over `BG`, with `X^{hG} = (X)^{G}` derived and `X_{hG} = X/G` derived, norm `Nm: X_{hG} → X^{hG}` and Tate `X^{tG} = cofib(Nm)` | `categories/spectra/homotopy_fixed_points.py` + `categories/spectra/homotopy_orbits.py` + `categories/spectra/tate.py` | Proposed — see note below |
| `MString` and `tmf` spectra | User note 2026-09-16 | `MString = Thom(MString)` as `E_∞` ring spectrum `MString = Thom(BString → BO)` with `π_*(MString)` string bordism, and `tmf = O^{top}(M_{ell})` topological modular forms as `E_∞` ring spectrum `tmf` with `π_*(tmf)` computed via Adams-Novikov `E_2 = Ext_{A}^{...}` and `tmf → MString` orientation `σ: MString → tmf` as `E_∞` map, with `tmf_*` connective and `TMF = tmf[Δ^{-1}]` periodic | `categories/spectra/mstring.py` + `categories/spectra/tmf.py` | Proposed — see note below |
| Sieves, Grothendieck topologies, pullbacks as intersections operationalized | User note 2026-09-16 | Sieve `S ⊂ h_U` on `U : C` as subfunctor `S ⊂ Hom_C(-,U) : C^{op}→Set` with `S` closed under precomposition; Grothendieck topology `J` on `C` as collection `J(U) = {S ⊂ h_U covering}` with maximal, stability, transitivity axioms; pullback `V ×_U W` in `C` as intersection when `C = Op(X)` or `C = Sub(X)` (pullbacks in poset are intersections `V∩W`), operationalize `Sieve`, `J`, `pullback` as computable for `FinSets`, `Op(X)` | `categories/sites/sieves.py` + `categories/sites/grothendieck_topology.py` + `categories/limits/pullbacks_as_intersections.py` + `categories/topology/sites.py` | Proposed — see note below |
| Topoi | User note 2026-09-16 | Topos `E : Topoi` as Grothendieck topos `E = Sh(C,J)` sheaves on site `(C,J)` with finite limits, colimits, exponentials, subobject classifier `Ω`, and `E` is `∞`-topos `E = Sh_∞(C,J)` when `S`-valued; `E = PSh(C)` presheaves and sheafification `a: PSh(C) → Sh(C,J)` left exact left adjoint to inclusion, with `E` as left exact localization of `PSh(C)`; need `Topoi` as 2-category with `Sh(C,J)` as objects, geometric morphisms `f: E→F` as adjunction `f^*: F→E` left exact left adjoint `⊣ f_*: E→F` | `categories/topoi/topoi.py` + `categories/topoi/sheaves.py` + `categories/sites/sheafification.py` | Proposed — see note below |
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
| Composition series, filtrations, associated graded, semidirect, is_simple, Jordan-Hölder, Inn/Out, artinian/noetherian, subgroup poset | User note 2026-09-15 | Composition series for groups/modules/algebras, filtrations with `gr`, `is_simple` in any abelian category, `Jordan-Hölder`, semidirect `N⋊H`, `Inn(G)⊲Aut(G)↠Out(G)`, `is_artinian`/`is_noetherian` for modules/rings, subgroup poset `Sub(G)` as honest `Poset` | `categories/algebra/composition_series.py` + `categories/abelian/is_simple.py` + `categories/groups/semidirect.py` + `categories/groups/automorphisms.py` + `categories/modules/chain_conditions.py` + `categories/groups/subgroup_poset.py` | Proposed — see note below |
| Open-set categories, powersets, topologies, poset ↔ poset-category | User note 2026-09-15 | `Op(X)`, `P(X)=2^X`, topologies `τ⊂P(X)` as `Top`, poset structure on `P(X)`/`Op(X)` by inclusion, fluid `Poset ⇄ PosetCat` interface | `categories/topology/open_sets.py` + `categories/sets/powerset.py` + `categories/topology/topologies.py` + `categories/posets/poset_category.py` | Proposed — see note below |
| Short exact sequences `1→A→B→C→1` and fibrations `F→E→B` via Ext / twisting cocycle | User note 2026-09-15 | SES `1→A→B→C→1` (resp. `0→A→B→C→0` in `R-Mod`) with middle term isomorphic to twisted product `A×_c C` classified by `[c]∈H^2(C,A)≅Ext^1(C,A)`; fibration sequence `F→E→B` with `E≃F×_τ B` classified by twisting operator `τ` / `[τ]∈H^{n+1}(B;π_n(F))` or `[B→BAut(F)]`, via bar/cobar and `Ext` | `categories/groups/short_exact_sequences.py` + `categories/algebras/short_exact_sequences.py` + `categories/topology/fibrations.py` + `categories/homotopy/twisted_products.py` + `categories/derived/ext_tor.py` | Proposed — see note below |
| Lie groups → Lie algebras, matrix groups as Lie groups | User note 2026-09-15 | For `G : LieGroups` extract `g = Lie(G) : LieAlgebras` functor `Lie: LieGroups → LieAlgebras`; all standard matrix groups `GL_n, SL_n, O_n, SO_n, U_n, SU_n, Sp_{2n}` promoted to `LieGroups` (and to `AlgGroups`/`GrpSch`), `Lie(GL_n)=Mat_{n×n}`, `Lie(SL_n)=sl_n` etc., with `exp: g → G` | `categories/lie/lie_groups.py` + `categories/lie/lie_algebras.py` + `categories/groups/matrix_groups.py` | Proposed — see note below |
| Algebraic groups / Lie groups / group schemes interfaces, Ad/ad | User note 2026-09-15 | Honest interfaces `AlgGroups`, `LieGroups`, `GrpSch` with functors `AlgGroups → LieGroups` (`G ↦ G^{an}` analytification), `GrpSch → Groups` (`G ↦ G(k)`), base-change `G_R = G×Spec R`; `Ad(G) : Rep(G)` adjoint on `g = Lie(G)`, `ad_g` on Lie algebra level | `categories/groups/algebraic_groups.py` + `categories/lie/lie_groups.py` + `categories/groups/group_schemes.py` + `categories/representations/adjoint.py` | Proposed — see note below |
| Group cohomology pairings via composition + tangent of character varieties | User note 2026-09-15 + https://www.math.umd.edu/~wmg/SymplecticNature.pdf | Pairings `H^p(G,M)⊗H^q(G,N)→H^{p+q}(G, M⊗N)` via composition morphisms `Hom⊗Hom → Hom` / cup product `∪` from `BarRes` / Yoneda composition; Zariski tangent `T_{[ρ]} X(π,G) ≅ T_{[ρ]} M_B ≅ H^1(π, g_{Ad∘ρ}) = Z^1/B^1` (Goldman) and `T_{[ρ]} Rep` etc. | `categories/group/cohomology.py` (pairings) + `categories/moduli/character_varieties.py` (tangent) + `categories/representations/adjoint.py` (`Ad∘ρ`) | Proposed — see note below |
| de Rham cohomology with coefficients in flat connections / local systems (Bott & Tu), honest K(G,n) | User note 2026-09-15 + Bott & Tu | de Rham `H^*_{dR}(X; E,∇)` with `∇` flat on `E : VecBun(X)`, `H^*_{dR}(X;∇)= H^*(Ω^*_X(E), d_∇)` with `d_∇^2=0 ⇔ F_∇=0`; cohomology with coefficients in local system `L : LocSys` as `H^*(X;L)= RΓ(X,L)` / de Rham comparison `H^*_{dR}(X;∇) ≅ H^*(X^{an}; L)` where `L = ker ∇`; honest `K(G,n)` as `K(G,n)=B^n G` with `ΩK(G,n)≃K(G,n-1)`, `K(G,1)≅BG` for common `G`, higher via loops/suspension/delooping | `categories/de_rham/de_rham_coeff.py` + `categories/sheaves/local_systems.py` + `categories/topology/eilenberg_maclane.py` + `categories/topology/classifying_spaces.py` | Proposed — see note below |
| Modular / automorphic forms, symbolic factors of automorphy, automorphic bundles | User note 2026-09-16 | Modular form `f: HH→C` with `f(γz)=j(γ,z)^k f(z)` for `j: Γ×HH→C^×` factor of automorphy, automorphic `F: G→C` with `F(γg)=j(γ,g)F(g)`, automorphic vector bundle `V_{j}= (HH×V)/Γ` via `j` | `categories/modular/forms.py` + `categories/automorphic/forms.py` + `categories/automorphic/factors.py` + `categories/automorphic/bundles.py` | Proposed — see note below |
| Spaces `M_k(N), S_k(N)`, dimensions, bases, Eisenstein, q-expansions, linear combination via sampling | User note 2026-09-16 | `M_k(Γ) : Vect_Q` / `Vect_C` with `dim M_k(Γ)` (Riemann-Roch / trace formula), explicit basis `{E_k, E_k^N, Δ·…}` with `q`-expansion `Σ a_n q^n ∈ R[[q]]`, expressing `f = Σ c_i b_i` via `N_{eval}=dim M_k` pointwise evaluations | `categories/modular/spaces.py` + `categories/modular/eisenstein.py` + `categories/modular/q_expansions.py` + `categories/rings/formal_power_series.py` | Proposed — see note below |
| Congruence subgroups, arithmetic subgroups (first-class) | User note 2026-09-16 | `Γ(N)⊲Γ_1(N)⊲Γ_0(N)⊲SL_2(ZZ)` as `ArithmeticSubgroups` with `Γ(N)=ker(SL_2(ZZ)→SL_2(ZZ/N))`, `Γ_0(N)={c≡0 mod N}`, `Γ_1(N)`, `Γ(N)`, `Γ⊂SL_2(ZZ)` finite index, `Γ⊂G(Q)` arithmetic in `G=SL_2, Sp_{2g}, U(p,q)` via `G(ZZ)` | `categories/modular/congruence_subgroups.py` + `categories/groups/arithmetic_subgroups.py` | Proposed — see note below |
| Modular curves `X(N), X_0(N), X_1(N)`, algebro-geometric invariants, fundamental domains as hyperbolic polytopes | User note 2026-09-16 | `X(Γ)=Γ\HH^*` compactified `HH^*=HH∪P^1(Q)` as `Curve/Q` (or `Sch/ZZ[1/N]`), genus `g(X(Γ))`, `Hodge(Ω^1)`, `canonical`, arithmetic genus, `HH^2` / `HH^3` fundamental domain `F_Γ⊂HH^n` as `HyperbolicPolytope` with side-pairings, visualization in `HH^2, HH^3` | `categories/modular/modular_curves.py` + `categories/modular/fundamental_domains.py` + `categories/hyperbolic/polytopes.py` + `categories/schemes/curve_genus.py` | Proposed — see note below |
| del Pezzo, Hirzebruch, common algebraic surfaces | User note 2026-09-16 | `F_e=P(O_{P^1}⊕O_{P^1}(-e))` Hirzebruch, `dP_n=Bl_{p_1…p_n}P^2` `0≤n≤8` del Pezzo with `(-1)`-curves, `P^1×P^1`, `K3`, `Enriques`, rational/ruled surfaces as `Surfaces/k` with `Pic`, `(-1)`-curves, `K_X` | `categories/schemes/surfaces/hirzebruch.py` + `categories/schemes/surfaces/del_pezzo.py` + `categories/schemes/surfaces/common_surfaces.py` | Proposed — see note below |
| Character / cocharacter lattices as preamble-owned lattices | User note 2026-09-16 | For torus `T≅G_m^r`, `X^*(T)=Hom(T,G_m)≅ZZ^r` character, `X_*(T)=Hom(G_m,T)≅ZZ^r` cocharacter, as `Lattices` `X^*, X_* : Lattices` with perfect pairing `⟨,⟩: X^*×X_*→ZZ`, `T↦X^*(T)` anti-equivalence `Tori≃Lattices` | `categories/tori/character_lattices.py` + `categories/lattices/lattices.py` + `categories/group/characters.py` | Proposed — see note below |
| Lattice cones and polytopes wired to honest lattices | User note 2026-09-16 | Cone `σ⊂N_R=N⊗R` strongly convex rational polyhedral `σ=cone(v_i)`, polytope `P⊂M_R` lattice polytope `P=conv(m_i)` with `vertices ⊂M`, both retaining ambient `Lattices` `N,M`, with face lattice, dual `σ^∨⊂M_R`, normal fan | `categories/cones/lattice_cones.py` + `categories/polytopes/lattice_polytopes.py` + `categories/schemes/toric/fans.py` + `categories/polyhedral_cones.py` | Proposed — see note below |
| Toric surfaces — classification, recognition, Fulton operationalized | User note 2026-09-16 | Smooth complete toric surface `S_Σ` from fan `Σ⊂N_R` `dim N_R=2`, classification by `Σ` with rays `v_i∈N`, recognition via `Fan` combinatorial invariants; Fulton *Introduction to toric varieties* operationalized: `T`-Weil `D=Σ a_ρ D_ρ`, `T`-Cartier, `H^i(O(D))`, `Chow`, cohomology `H^*(S_Σ)` | `categories/schemes/toric/surfaces.py` + `categories/schemes/toric/classification.py` + `categories/schemes/toric/fulton.py` | Proposed — see note below |
| Rational / birational maps, resolving indeterminacy, blowups at points, blowdowns | User note 2026-09-16 | Rational `φ: X ⇢ Y` as `U⊂X` open dense with `φ: U→Y` morphism, birational as `∃ψ: Y⇢X` inverse on opens, resolution via `π: \tilde X→X` blowup sequence `Bl_{p_i}` eliminating indeterminacy (`\tilde φ=φ∘π : \tilde X→Y` morphism), blowup `Bl_p X` at `p: Spec k→X` with exceptional `E≅P^{n-1}`, blowdown as inverse | `categories/schemes/rational_maps.py` + `categories/schemes/birational_maps.py` + `categories/schemes/blowups.py` + `categories/schemes/resolution.py` | Proposed — see note below |
| Contractions of curves on surfaces | User note 2026-09-16 | Contraction `c: S→S'` of curve `C⊂S` (`S` smooth surface) with `c(C)=pt`, `c: S\C ≅ S'\{pt}` iso, e.g. Castelnuovo `C≅P^1, C^2=-1` contractible to smooth point, Grauert for `C^2<0` to normal singularity, toric `v_i+v_{i+1}` removal | `categories/schemes/surfaces/contractions.py` + `categories/schemes/blowups.py` | Proposed — see note below |
| Isolated point singularities — normal forms, Milnor/Tjurina, higher codim | User note 2026-09-16 | Isolated hypersurface `f:(C^n,0)→(C,0)` normal forms `A_k,D_k,E_6,E_7,E_8` (and `A-D-E` surface du Val), `μ=dim C{x}/(∂f)`, `τ=dim C{x}/(f,∂f)` Milnor/Tjurina, classification in codim ≥1 via available algorithms (SINGULAR adapter) | `categories/schemes/singularities/isolated.py` + `categories/schemes/singularities/milnor_tjurina.py` + `categories/singularities/classification.py` | Proposed — see note below |
| Fibrations, Kodaira singular fibers, dual graphs of resolutions | User note 2026-09-16 | Fibration `f: S→C` (surface over curve) with generic fiber `F`, Kodaira list `I_n,I_n^*,II,III,IV,II^*,III^*,IV^*` for elliptic `f`, dual graph `Γ(Exc(π))` of exceptional `E_i≅P^1` in resolution `π: \tilde S→S` with vertices `E_i`, edges `E_i·E_j` | `categories/schemes/fibrations.py` + `categories/schemes/elliptic_surfaces/kodaira.py` + `categories/schemes/resolution/dual_graphs.py` | Proposed — see note below |
| Weighted vertex-edge graphs → Coxeter/Dynkin/s.e. laced; bilinear ↔ graph | User note 2026-09-16 | Generalized graph `D=(V,E,w_V:V→ZZ,w_E:E→ZZ)` with `w_V∈{±2,±4}` Coxeter (Dynkin `±2`, simply laced `2`), passage `b ↔ D` via `b(v_i,v_i)=w_V(v_i)`, `b(v_i,v_j)=w_E({i,j})` when `i≠j` and `0` else, `M_b = ⊕ ZZ·v_i` bilinear module ↔ `D` | `categories/graphs/weighted_graphs.py` + `categories/coxeter/coxeter_diagrams.py` + `categories/forms/bilinear_graphs.py` + `categories/lattices/graph_lattices.py` | Proposed — see note below |
| Invariants/coinvariants under `G→O(M,b)`, folding, converse `G→Aut(D)→O(M,b)` | User note 2026-09-16 | For `(M,b)` lattice/bilinear module with `G→O(M,b)`, invariants `M^G=ker(g-1)`, coinvariants `M_G=M/⟨gm-m⟩`, folding `D→D/G` via orbit identification, and conversely `G→Aut(D)` graph automorphisms induce `G→O(M_D,b_D)` on associated bilinear module | `categories/lattices/invariants.py` + `categories/lattices/coinvariants.py` + `categories/graphs/folding.py` + `categories/lattices/group_actions.py` | Proposed — see note below |
| Vector fields on Lie groups / manifolds, Lie/Poisson brackets, flows, ad/Ad | User note 2026-09-16 | `X∈Γ(TM)` vector field on `M: Man` (esp. `G: LieGroups`), Lie bracket `[X,Y]∈Γ(TM)`, Poisson `{f,g}`, flow `φ_X^t: M→M` with `d/dt φ_X^t = X∘φ_X^t`, left-invariant `X↔g`, `ad_X(Y)=[X,Y]`, `Ad_g(Y)=gYg^{-1}=d(c_g)_e` | `categories/manifolds/vector_fields.py` + `categories/lie/vector_fields.py` + `categories/geometry/brackets.py` + `categories/dynamics/flows.py` + `categories/representations/adjoint.py` | Proposed — see note below |
| Canonical sheaves, Serre duality | User note 2026-09-16 | `ω_X = ∧^n Ω^1_{X/k}` canonical (`det T^*X`) for `X: Sm/k` `n`-dim, `ω_X : Pic(X)`, duality `Ext^i(F,ω_X) ≅ H^{n-i}(X,F)^∨` for coherent `F`, `H^i(X,F)^∨ ≅ Ext^{n-i}(F,ω_X)`, `RΓ(F)^∨ ≅ RHom(F,ω_X[n])` via `Rf^!` | `categories/sheaves/canonical.py` + `categories/duality/serre.py` + `categories/schemes/canonical.py` + `categories/sheaves/six_functors.py` | Proposed — see note below |
| Siegel half-spaces | User note 2026-09-16 | `HH_g = {Z∈Mat_{g×g}(C) | Z^t=Z, Im Z>0}` Siegel upper half-space `Sp_{2g}(RR)/U(g)`, `dim_C = g(g+1)/2`, action `γ·Z=(AZ+B)(CZ+D)^{-1}` for `γ=(A B;C D)∈Sp_{2g}`, `Γ=Sp_{2g}(ZZ)` arithmetic, `A_g=Γ\HH_g` moduli of ppav, generalization of `HH=HH_1` | `categories/modular/siegel_half_space.py` + `categories/hermitian/siegel.py` + `categories/moduli/ppav.py` | Proposed — see note below |
| Derivations of modules / augmented ZZ-algebras, Fox free differential calculus | User note 2026-09-16 | `d: A→M` `R`-derivation `d(ab)=a·d(b)+d(a)·b`, `Der_R(A,M)=Hom_A(Ω_{A/R},M)`, `Ω_{A/R}` Kähler, augment `ε: A→ZZ`, `I=ker ε`, Fox `∂/∂x_i: ZZ[F_n]→ZZ[F_n]` free derivatives with `∂(uv)=∂(u)+u·∂(v)`, `d: ZZ[F]→⊕ ZZ[F]·dx_i`, `Ω_{ZZ[F]/ZZ}` free | `categories/algebras/derivations.py` + `categories/algebras/augmented_algebras.py` + `categories/algebras/fox_calculus.py` + `categories/modules/derivations.py` | Proposed — see note below |
| Surface geography oracles (superficie.info) + lattice geography / classification interactive tool | https://superficie.info/ + user intake 2026-09-19 | Oracle calculations for complex algebraic surface invariants (Chern numbers c_1^2, c_2, Kodaira dimension, Hodge numbers); TODO: produce similar interactive geography/classification tool for lattices (signatures (p,q), determinant, discriminant form, genus, root systems, Coxeter diagrams, K3/Enriques embeddings) | `categories/schemes/surfaces/` + `categories/lattices/` + `computations/` / `src/dzack_research/preamble/visualization/` | Proposed — see note below |
| Fano 3-fold geography, classification, derived categories (Fanography) | https://fanography.info/ + https://github.com/fanography/fanography | Classification and invariants of 105 Fano 3-fold families (Picard rank ρ, index r, degree (-K)^3, genus, Betti/Hodge numbers, D^b(X) semi-orthogonal decompositions, Hilbert schemes of lines/conics) | `categories/schemes/fano/` + `categories/derived/` + `categories/schemes/surfaces/del_pezzo.py` | Proposed — see note below |
| Generalized Grassmannians G/P, Schubert calculus, exceptional collections (Grassmannian.info) | https://www.grassmannian.info/ + https://github.com/pbelmans/grassmannian.info | Homogeneous varieties G/P for all Dynkin types, dimension, index, Picard number, Betti numbers (Schubert calculus, Bruhat order), cohomology rings H^*(G/P;ZZ), Borel–Weil–Bott, full exceptional collections in D^b(G/P) | `categories/schemes/grassmannian.py` + `categories/lie/homogeneous_spaces.py` + `categories/derived/exceptional_collections.py` | Proposed — see note below |
| Scheme and morphism adjectives, automated property deduction (The Adjectives Project) | https://adjectivesproject.org/ + https://github.com/jessetvogel/adjectives-project-data | 19 scheme properties, 44 morphism properties, 95 implication theorems, 107 concrete examples/counterexamples; operationalized property calculus and oracle test suite for Schemes and Hom(Sch) | `categories/schemes/properties.py` + `categories/schemes/morphism_properties.py` + `categories/schemes/theorems.py` | Proposed — see note below |
| General topology counterexamples, 246 properties, 931 theorems, universal constructions (pi-Base) | https://topology.pi-base.org/ + https://github.com/pi-base/data | 246 topological properties (separation, compactness, countability, connectedness, metrizability), 224 canonical spaces, 931 theorems, universal constructions (subspaces, products, coproducts, quotients); operationalized topological predicate suite | `categories/topology/spaces.py` + `categories/topology/properties.py` + `categories/topology/constructions.py` + `categories/topology/theorems.py` | Proposed — see note below |
| Bilinear forms to polynomial schemes and 1-parameter quadric families | User intake 2026-09-19 | Passage from bilinear form b: M⊗_R M→R on free M≅R^n to polynomial b(x,x)∈R[x_0..x_{n-1}] (and b(x,y)); 1-parameter family V(b(x,x)-t) over AA^1(R); transport problem b(v,v)=t to finding integral points on fibers, utilizing specialized number theory and lattice algorithms | `categories/forms/polynomial.py` + `categories/schemes/families.py` + `categories/schemes/quadrics.py` + `categories/lattices/representations.py` | Proposed — see note below |
| Category of Hodge structures (pure, mixed, polarized) and operations | User intake 2026-09-19 | Category of pure Hodge structures HS_k(R), mixed Hodge structures MHS(R) (Deligne), polarized HS_k^{pol}(R); standard operations: tensor product, direct sum, dual, internal Hom, exterior powers ⋀^n H, symmetric powers Sym^n H, Tate twist ZZ(m) / H(m), weight and Hodge filtrations, Hodge classes, intermediate Jacobians | `categories/hodge/hodge_structures.py` + `categories/hodge/mixed_hodge.py` + `categories/hodge/polarized.py` + `categories/hodge/tate_twist.py` | Proposed — see note below |
| Projectivization of linear groups and subgroups (PGL, PO, PSL, PSp) | User intake 2026-09-19 | Projectivization functor P: G ↦ PG = G / (G ∩ R^×·id) for linear groups G ≤ GL(V) (e.g. GL_n → PGL_n, O(b) → PO(b) ≅ O(b)/{±id}, SL_n → PSL_n, Sp_{2g} → PSp_{2g}, and arithmetic subgroups Γ ≤ O(L)); quotient projection π: G ↠ PG; faithful action on projective space PP(V) and hyperbolic space HH^n | `categories/groups/projectivization.py` + `categories/groups/matrix_groups.py` + `categories/lattices/orthogonal_group.py` | Proposed — see note below |
| Lambert expansions of generating functions | User intake 2026-09-19 | Lambert series L(q) = \sum a_n q^n/(1-q^n) and bidirectional conversion to/from OGF \sum b_N q^N via divisor convolution b_N = \sum_{d|N} a_d and Mobius inversion a_n = \sum_{d|n} \mu(n/d) b_d; Dirichlet series link D_b(s) = D_a(s)\zeta(s); q-expansions of Eisenstein series E_{2k}, Dedekind \eta, and Euler products | `categories/generating_functions/lambert.py` + `categories/rings/formal_power_series.py` + `categories/modular/eisenstein.py` | Proposed — see note below |
| Computing Picard-Fuchs operators of families (Gauss-Manin, Weierstrass, twists, and Fano/K3 mirrors) | https://arxiv.org/abs/2403.07349 + user intake 2026-09-19 | Computation of Picard-Fuchs differential operators for algebraic families \pi: X \to B; explicit Weierstrass reduction \nabla = d/dt - M(t) with \Delta, \delta (arXiv:2403.07349 p. 13 Eq. 2.17); Doran-Malmendier Hadamard twist construction L_{n+1} = L_twist \star L_n; recovery of 17 rank-1 Fano anticanonical K3 operators L_{3,N} (Table 1), modular elliptic pencils L_{2,n} (Table 4), quantum differential operators D_{4,N} = \theta \cdot L_{3,N} (Table 2), and P^3 instanton pullback (Eq. 6.1) | `categories/differential_equations/picard_fuchs.py` + `categories/schemes/elliptic_surfaces/weierstrass_picard_fuchs.py` + `categories/cohomology/gauss_manin.py` + `categories/schemes/k3/fano_mirrors.py` | Proposed — see note below |
| Converting linear recurrences to differential equations symbolically (Ore algebras, D-finite/holonomic systems) | User intake 2026-09-19 | Symbolic translation from linear recurrence relations \sum p_i(n) a_{n+i} = 0 (shift Ore algebra K[n]\langle S_n \rangle) to linear differential equations \sum q_j(t) F^{(j)}(t) = 0 and Euler form \mathcal{L}(\theta) F(t) = P(t) (Weyl/differential Ore algebra K[t]\langle \partial_t \rangle); handles initial conditions, OGF/EGF (Borel/Laplace transform); connects Apéry sequences to Calabi-Yau Picard-Fuchs operators | `categories/differential_equations/ore_algebra.py` + `categories/differential_equations/recurrence_to_diffeq.py` + `categories/algebras/ore_algebras.py` | Proposed — see note below |
| Large poset navigation, 2D grid layouts, Coxeter subdiagrams, and G-poset quotients | User intake 2026-09-19 | 2D grid/ranked layout and interactive navigation for extremely large posets (10^3–10^6 nodes); subdiagram posets of Coxeter diagrams (< 25 nodes): elliptic, parabolic, Lanner, and their maximal elements; chain tracing to maximal/minimal elements; diagram quotients by symmetries G = Aut(Γ) or Aut(M); G-posets and bidirectional projection/unrolling P \leftrightarrow P/G | `categories/posets/large_poset.py` + `categories/coxeter/subdiagram_posets.py` + `categories/graphs/diagram_automorphisms.py` + `src/dzack_research/preamble/visualization/` | Proposed — see note below |
| q-analogues (q-integers, q-factorials, Gaussian binomials, Jackson calculus, and basic hypergeometric series) | User intake 2026-09-19 | Comprehensive q-analogue infrastructure: q-numbers [n]_q, q-factorials [n]_q!, Gaussian binomial/multinomial coefficients \binom{n}{k}_q (subspace counts in Gr(k,n)(F_q), Bruhat inversions); Jackson q-derivative and integral; q-Pochhammer symbols (a;q)_n, (a;q)_\infty; basic hypergeometric series {}_r\phi_s; q-exponential/gamma; Poincaré polynomials of Coxeter groups and Hecke/quantum group algebra connections | `categories/combinatorics/q_analogues.py` + `categories/special_functions/q_hypergeometric.py` + `categories/quantum_groups/quantum_integers.py` + `categories/algebras/hecke_algebra.py` | Proposed — see note below |
| Elliptic surfaces, fibrations, Weierstrass forms, Néron models, and Mordell-Weil lattices | User intake 2026-09-19 | Comprehensive elliptic surface architecture: fibrations \pi: S \to C, Jacobian fibrations with zero section O, fundamental line bundle L = (R^1 \pi_* O_S)^\vee, canonical bundle formula; Weierstrass models y^2 = 4x^3 - g_2 x - g_3, discriminant \Delta, j-invariant J(t), Miranda resolution; Néron models, Kodaira singular fiber classification (I_n, I_n^*, II, III, IV, II^*, III^*, IV^*) via Tate's algorithm; Mordell-Weil group MW(S/C) of sections, Shioda-Tate formula, Mordell-Weil lattice with height pairing \langle P, Q \rangle and local correction terms contr_v(P, Q) | `categories/schemes/elliptic_surfaces/elliptic_surface.py` + `categories/schemes/elliptic_surfaces/weierstrass_models.py` + `categories/schemes/elliptic_surfaces/kodaira.py` + `categories/schemes/elliptic_surfaces/mordell_weil.py` | Proposed — see note below |
| Euler operator $\theta = t \partial_t$ and standard formal power series operators on $R[[t]]$ | User intake 2026-09-19 | Complete differential and algebraic operator calculus on $R[[t]]$: Euler/theta operator $\theta = t \frac{d}{dt}$ ($\theta(t^n) = n t^n$, Stirling conversions $\theta^k \leftrightarrow t^j \partial_t^j$, ODE Euler forms $P(\theta)$); formal derivation $\partial_t$ and integration $\int$; forward/backward shifts $S^{\pm}$, coefficient extraction $[t^n]$; multiplications (Cauchy, Hadamard $\odot$, Hurwitz binomial convolution); composition $f \circ g$ and formal inversion via Lagrange Inversion Formula / Lagrange-Bürmann; logarithmic derivatives $\operatorname{dlog}(f) = f'/f$ and $\operatorname{dlog}_\theta(f) = \theta f / f$; exponential of integral $\exp(\int f)$ (integrating factors, combinatorial exponential formula) and formal logarithm $\log(f)$; Witt algebra generators $L_n = -t^n \theta$ | `categories/rings/formal_power_series.py` + `categories/differential_operators/formal_series.py` + `categories/generating_functions/operators.py` + `categories/algebras/weyl_algebra.py` | Proposed — see note below |
| Known mirror family pairs from the literature (Greene-Plesser, Batyrev-Borisov, Dolgachev-Nikulin, BHK, 14 hypergeometric CY3s, Doran-Harder-Thompson) | Literature survey + user intake 2026-09-19 | Comprehensive classification and catalogue of mirror family pairs across dimensions: (1) Greene-Plesser orbifold pairs (quintic $X_5 \leftrightarrow Y_5$ and 27 weighted projective complete intersections); (2) Batyrev-Borisov dual reflexive polytopes $(\Delta, \Delta^\circ)$ (16 in 2D, 4319 in 3D, 473M in 4D) and nef-partitions; (3) Dolgachev-Nikulin lattice-polarized K3 mirror pairs ($M \leftrightarrow \check{M} = U \oplus M^\perp$, e.g. quartic $\leftrightarrow$ Dwork pencil); (4) Berglund-Hübsch-Krawitz (BHK) transpose polynomials $(W, G) \leftrightarrow (W^\mathrm{T}, G^\mathrm{T})$ (Fermat, loop, chain); (5) The 14 one-parameter hypergeometric Calabi-Yau threefolds (Doran-Morgan / Morrison / AESZ, 7 arithmetic / 7 thin monodromy); (6) Doran-Harder-Thompson fibration / degeneration mirrors (K3 fibrations over $\mathbb{P}^1$ and Kulikov component gluing); (7) Fano / Landau-Ginzburg mirrors $(X \leftrightarrow (\mathbb{C}^\times)^n, W)$; (8) Abelian varieties and SYZ dual tori | `categories/schemes/mirror_symmetry/mirror_catalogue.py` + `categories/schemes/mirror_symmetry/batyrev_borisov.py` + `categories/schemes/mirror_symmetry/dolgachev_nikulin.py` + `categories/schemes/mirror_symmetry/bhk.py` + `categories/schemes/mirror_symmetry/hypergeometric_cy3.py` | Proposed — see note below |
| Operationalized convergence criteria, Dirichlet irrationality, symbolic integration by parts, and L-function zeta regularization | User intake 2026-09-19 | Operationalized convergence and analytic toolkit: (1) Dirichlet's irrationality criterion (Diophantine approximation $|\alpha - p/q| < 1/(qN) \le 1/q^2$, continued fractions, Apéry-type certificates, irrationality measures $\mu(\alpha)$); (2) Dirichlet's convergence test for series $\sum a_n b_n$ (bounded partial sums + monotonic $b_n \to 0$ via Abel summation by parts, alternating/Fourier/Dirichlet series); (3) Cauchy condensation test $\sum a_n \leftrightarrow \sum 2^k a_{2^k}$ (automated logarithmic/geometric convergence decider); (4) Symbolic integration by parts (recursive, tabular, reduction formulas, LIATE heuristic, cyclic integral solver in differential algebra); (5) Zeta and L-function regularization (spectral zeta functions $\zeta_A(s) = \operatorname{Tr}(A^{-s})$, functional determinants $\operatorname{det}_\zeta(A) = \exp(-\zeta_A'(0))$, Ramanujan/Euler-Maclaurin summation, completed L-functions $\Lambda(s, \pi)$, and values at integers) | `categories/analysis/convergence_tests.py` + `categories/number_theory/diophantine_approximation.py` + `categories/calculus/symbolic_integration.py` + `categories/zeta/regularization.py` + `categories/l_functions/analytic_continuation.py` | Proposed — see note below |
| Gerstenhaber algebra structure on Hochschild cohomology $HH^*(A, A)$ (operadic $e_2$ algebra, brace algebra, Schouten bracket) | User intake 2026-09-19 | Full Gerstenhaber algebra structure $(\smile, [-,-])$ on Hochschild cohomology $HH^*(A, A)$: graded commutative cup product $HH^p \otimes HH^q \to HH^{p+q}$, graded Lie bracket $[-,-] \colon HH^p \otimes HH^q \to HH^{p+q-1}$ (degree -1, degree 0 on $HH^*[1]$), Poisson/derivation compatibility $[a, b \smile c] = [a, b] \smile c + (-1)^{(|a|-1)|b|} b \smile [a, c]$; cochain realization via Gerstenhaber circle product $f \circ g = \sum (-1)^{(i-1)(q-1)} f \circ_i g$, graded pre-Lie algebra $C^*(A, A)[1]$, DGLA differential $d = [m, -]$; brace algebra $B_\infty$ operations $f\{g_1, \dots, g_k\}$; Deligne's conjecture ($E_2$ / little 2-disks operad action on $C^*(A, A)$); HKR isomorphism matching $[-,-]$ with Schouten-Nijenhuis bracket on polyvector fields $\bigwedge^* T_X$; deformation theory (Maurer-Cartan equation $d\alpha + \frac{1}{2}[\alpha, \alpha] = 0$, obstructions in $HH^3$); Batalin-Vilkovisky (BV) structure $\Delta$ on Calabi-Yau / Frobenius algebras | `categories/homology/gerstenhaber.py` + `categories/homology/hochschild.py` + `categories/operads/little_disks.py` + `categories/algebras/brace_algebras.py` + `categories/deformation/deformation_quantization.py` | Proposed — see note below |
| Continuous actions of topological groups on topological spaces (G-Top, orbit spaces, proper actions, slice theorem, and equivariant topology) | User intake 2026-09-19 | Comprehensive topological group action framework: topological group $G \in \mathbf{TopGrp}$ and continuous left/right actions $\alpha \colon G \times X \to X$ in $\mathbf{Top}$; orbits $G \cdot x$, stabilizers $G_x \le G$ (closed subgroups), canonical homeomorphism $G/G_x \cong G \cdot x$; quotient orbit space $X/G$ with open projection $\pi \colon X \twoheadrightarrow X/G$, separation criteria ($T_1 \iff$ closed orbits, $T_2 \iff$ closed orbit relation); action predicates: transitive ($X \cong G/H$), free, faithful, proper ($(g,x) \mapsto (gx, x)$ proper, compact stabilizers, Hausdorff quotient), properly discontinuous, cocompact; Palais-Koszul slice theorem $G \times_H S \cong U$; equivariant category $G\mathbf{-Top}$ ($G$-maps, invariant subspaces, fixed points $X^G$, induction $\operatorname{Ind}_H^G = G \times_H -$, coinduction $\operatorname{CoInd}_H^G$); Borel homotopy quotient $X_{hG} = EG \times_G X$, equivariant cohomology $H_G^*(X) = H^*(X_{hG})$; principal $G$-bundles and associated bundles $P \times_G F$ | `categories/topology/topological_groups.py` + `categories/topology/group_actions.py` + `categories/topology/equivariant.py` + `categories/topology/principal_bundles.py` | Proposed — see note below |
| Associated real/complex torus $T(L) = L_\mathbb{R}/L$ and abelian varieties from $\mathbb{Z}$-lattices | User intake 2026-09-19 | Construction of the associated torus $T(L) = L_\mathbb{R}/L \cong (S^1)^n$ for any $\mathbb{Z}$-lattice $L$: compact abelian Lie group, $\pi_1 \cong L$, $H_1 \cong L$, $H^1 \cong L^\vee$, dual torus $T(L)^\vee = L_\mathbb{R}^\vee/L^\vee$; complex structures $J$ ($J^2 = -\operatorname{id}$ on $L_\mathbb{R}$ for $\operatorname{rank}(L) = 2g$) yielding complex tori $V/\Lambda$; Riemann bilinear relations for polarizations $E \in \bigwedge^2 L^\vee$: $E(Ju, Jv) = E(u, v)$ and $E(u, Ju) > 0$ (Hodge type (1,1) + positive-definiteness); criterion for $T(L)$ to be an abelian variety (existence of Riemann form $E$); elementary divisors $(d_1, \dots, d_g)$, principal polarizations ($d_i = 1$) and period matrices $Z \in \mathbb{H}_g$ in Siegel upper half-space; Appell-Humbert theorem and theta functions $\theta(z)$; Euclidean lattices with symmetric form $b$ as flat Riemannian tori, Laplace spectrum from $L^\vee$, and Milnor isospectral pairs; Jacobian $\operatorname{Jac}(C) = H_1(C, \mathbb{R})/H_1(C, \mathbb{Z})$ and Albanese $\operatorname{Alb}(X)$ varieties | `categories/lattices/torus.py` + `categories/complex_geometry/complex_tori.py` + `categories/abelian_varieties/abelian_variety.py` + `categories/modular/siegel_half_space.py` + `categories/riemannian/flat_tori.py` | Proposed — see note below |
| Cartier and Pontryagin dualities (LCA groups, finite commutative group schemes, Hopf algebras, and Weil pairings) | User intake 2026-09-19 | Categorical duality theories for abelian topological groups and commutative group schemes: (1) Pontryagin duality on locally compact abelian groups $\mathbf{LCA}$: character group $\widehat{G} = \operatorname{Hom}_{\mathbf{LCA}}(G, \mathbb{T})$, biduality isomorphism $G \xrightarrow{\sim} \widehat{\widehat{G}}$, compact-discrete duality, torsion-profinite duality, connected-torsion-free duality, annihilators $H^\perp \cong \widehat{G/H}$, dual exact sequences, Haar measure, Fourier transform, and Plancherel theorem; (2) Cartier duality on finite locally free commutative group schemes over $S$ (and finite-dimensional commutative cocommutative Hopf algebras $A$ via dual Hopf algebra $A^*$): $D(G) = \underline{\operatorname{Hom}}(G, \mathbb{G}_m)$, canonical biduality $G \xrightarrow{\sim} D(D(G))$, dual pairs $(\mathbb{Z}/n)_k \leftrightarrow \mu_{n,k}$ and self-dual $\alpha_p$, four Oort-Tate classes (étale-étale, étale-local, local-étale, local-local), Frobenius-Verschiebung exchange $D(F) = V_{D(G)}$; (3) Dieudonné module duality $\mathbb{M}(D(G))$; (4) Abelian varieties: Cartier duality $D(A[n]) \cong A^\vee[n]$ yielding the Weil pairing $e_n \colon A[n] \times A^\vee[n] \to \mu_n$; (5) Barsotti-Tate ($p$-divisible) groups and Serre-Tate duality | `categories/topology/pontryagin.py` + `categories/schemes/group_schemes/cartier_duality.py` + `categories/algebras/hopf_algebras.py` + `categories/abelian_varieties/weil_pairing.py` + `categories/schemes/group_schemes/p_divisible.py` | Proposed — see note below |
| Operationalized Grothendieck spectral sequences (generic functor composition, automated differentials, 5-term solver, and concrete specializations: Leray, Serre, LHS, local-to-global Ext/Tor, Frölicher) | Literature survey + user intake 2026-09-19 | Comprehensive computational framework for Grothendieck spectral sequences: (1) Abstract Grothendieck spectral sequence $E_2^{p, q} = (R^p F)(R^q G(A)) \implies R^{p+q}(F \circ G)(A)$ for composable functors $\mathcal{A} \xrightarrow{G} \mathcal{B} \xrightarrow{F} \mathcal{C}$ with $G(\operatorname{Inj})$ $F$-acyclic, homological dual $E^2_{p, q} = (L_p F)(L_q G(A)) \implies L_{p+q}(F \circ G)(A), Cartan-Eilenberg double complex resolutions; (2) Algorithmic engine: bigraded page structures $E_r^{p, q}$, differential complexes $d_r$, page transitions $E_{r+1} = H(E_r, d_r)$, automated quadrant/sparsity vanishing, 5-term exact sequence solver ($0 \to E_2^{1, 0} \to H^1 \to E_2^{0, 1} \xrightarrow{d_2} E_2^{2, 0} \to \dots$), multiplicative Leibniz propagation $d_r(xy) = d_r(x)y + (-1)^{|x|} x d_r(y)$, transgression tracking, abutment filtration reconstruction, and extension problem solving; (3) Concrete computable specializations: Leray SS ($H^p(Y, R^q f_* \mathcal{F}) \implies H^{p+q}(X, \mathcal{F})$), Serre fibration SS ($H^p(B; \mathcal{H}^q(F)) \implies H^{p+q}(E)$), Lyndon-Hochschild-Serre (LHS) for group cohomology ($H^p(G/N, H^q(N, M)) \implies H^{p+q}(G, M)$), Lie algebra Hochschild-Serre, local-to-global Ext ($H^p(X, \mathcal{E}xt^q(\mathcal{F}, \mathcal{G})) \implies \operatorname{Ext}^{p+q}(\mathcal{F}, \mathcal{G})$), local-to-global Tor, change of rings (Cartan-Eilenberg Ext/Tor), Frölicher/Hodge-to-de Rham ($H^q(X, \Omega_X^p) \implies H_{\mathrm{dR}}^{p+q}$), and local cohomology SS | `categories/homology/spectral_sequences/grothendieck.py` + `categories/homology/spectral_sequences/spectral_sequence.py` + `categories/homology/spectral_sequences/leray.py` + `categories/homology/spectral_sequences/lyndon_hochschild_serre.py` + `categories/homology/spectral_sequences/local_ext.py` + `categories/homology/spectral_sequences/froelicher.py` | Proposed — see note below |
| Operationalized Riemann-Hurwitz formula, ramification theory, different and discriminant ideals (curves, varieties, Dedekind domains, and number fields) | Literature survey + user intake 2026-09-19 | Unified operational ramification theory and Hurwitz formulas across algebraic geometry and algebraic number theory: (1) Ramification invariants: ramification index $e_i = e(\mathfrak{P}_i/\mathfrak{p})$, inertia degree $f_i = f(\mathfrak{P}_i/\mathfrak{p})$, fundamental identity $\sum e_i f_i = n$, tame ($p \nmid e$) vs wild ($p \mid e$) ramification; (2) Different ideal $\mathfrak{D}_{B/A}$ and discriminant $\mathfrak{d}_{B/A} = N(\mathfrak{D}_{B/A})$, Dedekind's different theorem ($\mathfrak{P} \mid \mathfrak{D} \iff e > 1$), lower and upper bounds $e - 1 \le d \le e - 1 + v_\mathfrak{P}(e)$, equality $d = e - 1$ for tame; (3) Galois ramification filtration: decomposition group $D_\mathfrak{P}$, inertia group $I_\mathfrak{P} = G_0$, lower ramification groups $G_i$, Hilbert's different formula $d = \sum_{i=0}^\infty (|G_i| - 1) = (e - 1) + \text{wild excess}$; (4) Riemann-Hurwitz formula for curves: canonical divisor $K_X \sim f^* K_Y + R$ where $R = \sum d_P P$, genus formula $2 g_X - 2 = n(2 g_Y - 2) + \deg(R)$, topological Euler characteristic $\chi(X) = n \chi(Y) - \deg(R)$; (5) Normal varieties: purity of the branch locus (Zariski-Nagata) in codimension 1, ramification divisor $R = \sum d_D D$, canonical class formula $K_X \sim f^* K_Y + R$; (6) Automated solver: genus solver, prime factorization $\mathfrak{p} \mathcal{O}_L = \prod \mathfrak{P}_i^{e_i}$, different/discriminant computer, and branch locus verifier | `categories/algebraic_geometry/hurwitz.py` + `categories/number_theory/ramification.py` + `categories/schemes/ramification_divisor.py` + `categories/galois/ramification_groups.py` | Proposed — see note below |
| DG-modules over DG-algebras, graded module foundations, derived categories $\mathcal{D}(A)$, and semi-free resolutions | User intake 2026-09-19 | Complete categorical and homological hierarchy for differential graded (DG) modules over DG-algebras: (1) Graded foundations: $\mathbb{Z}$-graded modules $\mathbf{GrMod}_k$, Koszul braiding $\tau(x \otimes y) = (-1)^{|x||y|} y \otimes x$, graded associative/commutative algebras, graded module categories; (2) Differential graded objects: cochain complexes $(\mathbf{Ch}_k, \otimes, \underline{\operatorname{Hom}})$, Koszul sign convention $d(x \otimes y) = d(x) \otimes y + (-1)^{|x|} x \otimes d(y)$, $[d, f] = d \circ f - (-1)^{|f|} f \circ d$; (3) DG-algebras $(A, d_A)$ with Leibniz rule $d(a b) = d(a) b + (-1)^{|a|} a d(b)$ and CDGAs; (4) DG-modules $(M, d_M)$ over $A$ with module Leibniz rule $d_M(a m) = d_A(a) m + (-1)^{|a|} a d_M(m)$, DG-bimodules, cohomology modules $H^*(M) \in H^*(A)\mathbf{-Mod}$; (5) The DG-category $\underline{\mathbf{DGMod}}_A$: Hom complexes $\underline{\operatorname{Hom}}_A(M, N)$, shifts $M[k]$, mapping cones $\operatorname{Cone}(f)$; (6) Homological & model structures: quasi-isomorphisms, derived category $\mathcal{D}(A)$, projective model structure, semi-free (cell) resolutions $\mathbf{p} M \xrightarrow{\sim} M$, semi-injective resolutions, compact/perfect DG-modules $\operatorname{Perf}(A)$; (7) Derived operations: derived tensor product $M \otimes_A^{\mathbf{L}} N$, derived Hom $\mathbf{R}\operatorname{Hom}_A(M, N)$, Tor and Ext groups, two-sided bar resolution $B(A, A, M)$; (8) Computational engine: polynomial/exterior DGAs (Koszul complexes), matrix factorizations, de Rham flat modules, and semi-free resolution generators | `categories/algebras/dg_algebras.py` + `categories/modules/dg_modules.py` + `categories/derived/dg_derived_category.py` + `categories/modules/graded_modules.py` + `categories/homology/bar_cobar.py` | Proposed — see note below |
| Witt vectors, $p$-adics as explicit power series, and ghost vector representations (exact and symbolic arithmetic) | User intake 2026-09-19 | Algebraic and algorithmic infrastructure for $p$-typical and big Witt vectors, and $p$-adic series arithmetic: (1) $p$-typical Witt ring $W(R)$ and truncated $W_n(R)$: ghost map $w_n = \sum_{i=0}^n p^i x_i^{p^{n-i}}$, bijection over $\mathbb{Q}$-algebras, componentwise ghost addition/multiplication, universal polynomials $S_n, P_n \in \mathbb{Z}[X, Y]$, and triangular back-substitution; (2) Perfect field Witt vectors $W(k)$ as complete DVR of characteristic 0, $W(\mathbb{F}_p) \cong \mathbb{Z}_p$, unramified extensions $W(\mathbb{F}_{p^d}) \cong \mathbb{Z}_{p^d}$; (3) Teichmüller lifts $[a] = (a, 0, \dots)$, $p$-adic expansion $x = \sum [c_n] p^n$, Newton-Hensel quadratic convergence; (4) Operators: Verschiebung $V(x) = (0, x_0, \dots)$, Frobenius $F$, relations $FV = p$, $VF = p$, Dieudonné ring $W(k)[F, V]$; (5) Big Witt vectors $\mathbb{W}(R) \cong 1 + t R[[t]]^\times$, power series multiplication link, Cartier decomposition $\mathbb{W}(R) \cong \prod_{(k, p)=1} W(R)$; (6) Explicit $p$-adic series in $\mathbb{Z}_p, \mathbb{Q}_p$: formal power series expansions $\sum a_n p^n$, ultrametric valuations $v_p$, Hensel's lemma, Artin-Hasse exponential $E_p(t) = \exp(\sum t^{p^n}/p^n) \in \mathbb{Z}_p[[t]]$, and symbolic ghost arithmetic engine | `categories/number_theory/witt_vectors.py` + `categories/number_theory/p_adics.py` + `categories/rings/formal_power_series.py` + `categories/algebraic_geometry/dieudonne.py` | Proposed — see note below |
| Operationalized algebraic topology calculational theorems (Mayer-Vietoris, Universal Coefficient Theorems, Künneth formulas, cellular homology, excision, Poincaré duality, van Kampen, and Hurewicz) | User intake 2026-09-19 | Comprehensive computational framework implementing Hatcher-style topological theorems as exact solvers: (1) Mayer-Vietoris sequence solver for homology and cohomology: $H_n(A \cap B) \to H_n(A) \oplus H_n(B) \to H_n(X) \to H_{n-1}(A \cap B)$, reduced/relative variants, connecting homomorphisms $\partial, \delta$; (2) Universal Coefficient Theorems (UCT): automated evaluation of $H_n(X; G) \cong (H_n(X) \otimes G) \oplus \operatorname{Tor}_1(H_{n-1}(X), G)$ and $H^n(X; G) \cong \operatorname{Hom}(H_n(X), G) \oplus \operatorname{Ext}^1(H_{n-1}(X), G)$ across arbitrary coefficients ($\mathbb{Q}, \mathbb{F}_p, \mathbb{Z}/m$); (3) Künneth formula solver for products $X \times Y$ with $\otimes$ and $\operatorname{Tor}_1$ terms; (4) Cellular homology engine: attaching maps, cellular boundary matrices $d_n = [\deg(\Delta_{\alpha, \beta})]$, and Euler characteristic $\chi(X) = \sum (-1)^n c_n$; (5) Long exact sequences of pairs $(X, A)$, excision, suspension isomorphisms $\widetilde{H}_{n+1}(\Sigma X) \cong \widetilde{H}_n(X)$, and wedge sums; (6) Cohomology rings: cup and cap products, Poincaré duality isomorphisms $H^k(M) \cong H_{n-k}(M)$, and intersection pairings; (7) Homotopy theory solvers: Seifert-van Kampen amalgamated free product solver $\pi_1(A) *_{\pi_1(A \cap B)} \pi_1(B)$, Hurewicz abelianization $\pi_1^{\mathrm{ab}} \cong H_1$ and higher Hurewicz isomorphisms $\pi_n(X) \cong H_n(X)$ | `categories/topology/computational_topology.py` + `categories/topology/mayer_vietoris.py` + `categories/topology/uct.py` + `categories/topology/kunneth.py` + `categories/topology/cellular.py` + `categories/topology/poincare_duality.py` + `categories/topology/van_kampen.py` | Proposed — see note below |







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

## Desired capability: honest and operationalized Q_ℓ, étale cohomology, Galois cohomology as specialization — computable in some cases — note 2026-09-16

Need honest and operationalized `Q_ℓ`, étale cohomology, and Galois cohomology as a specialization — not a formal `H^1_ℓ` string — and it must be computable in some cases via effective models.

* `Q_ℓ` is not `Q` with `ℓ` appended. It is the `ℓ`-adic completion `Q_ℓ = (lim← Z/ℓ^n) ⊗ Q` as object of `Fields` with its `ℓ`-adic topology, valuation, and absolute Galois action. Need `Z_ℓ`, `Q_ℓ`, `Q_ℓ^{ur}` as coefficient rings for sheaves, with `ℓ`-adic lisse sheaves `Q_ℓ(n)` as objects of `Sh(X_ét, Q_ℓ)` obtained via inverse system `(Z/ℓ^n)_{n}` and tensor with `Q_ℓ`. Without this, `ρ_ℓ: Gal_Q → GSp(H^1_ℓ)` cannot be stated.

* Étale cohomology `H^*_ét(X_{ét}, Q_ℓ) : GrMod` is sheaf cohomology of the étale site `X_ét` as graded object `H^*_ét = ⊕_i H^i_ét` with `H^i_ét = H^i(RΓ(X_ét,-))` and uniform interface `H^*_ét.graded_piece(i) = H^i_ét`, not a family of separate `H^i` requests. Requires site `(C_X, J_ét)` where `C_X = Ét_{/X}` and `J_ét` is Grothendieck topology given by covering families `{U_i → U}` jointly surjective, equivalently sieves `S ⊂ h_U`. Sheaf condition is `F(U) ≅ lim_{S} F` for covering sieves. This gives topos `Sh(X_ét)` and derived `RΓ(X_ét,-): D(Sh)→D(Ab)` whose cohomology is the graded `H^*_ét = H^*(RΓ) : GrMod` with `H^*_ét.graded_piece(i)=H^i_ét`.

* Galois cohomology as graded specialization: for `X = Spec K` (`K` field, e.g. `K=Q`), `X_ét` is the site of finite étale `Spec L → Spec K` (finite separable extensions), equivalent to finite discrete `Gal_K`-sets. Then `Sh((Spec K)_ét) ≃ Gal_K-Sets` (discrete `Gal_K`-modules), and `H^*_ét(Spec K, F) : GrMod` with `H^*_ét.graded_piece(i)=H^i_ét(Spec K,F)=H^i(Gal_K,F_{K^{sep}})` — graded `H^*(Gal_K,-)` is the value of the same site cohomology functor at the terminal object. Need this identification as theorem on graded `H^*`, not as separate definition. Without sites, `H^*(Gal,-)` and `H^*_ét` are two unrelated functors.

* Requires: category `Sites` with objects `(C, J)` (small category + Grothendieck topology via sieves/covering families), morphisms of sites (continuous functors), associated sheaf functor `a: PSh(C) → Sh(C,J)`, and cohomology `RΓ`. Specializations: Zariski site `(Open(X), J_Zar)`, étale site `(Ét_{/X}, J_ét)`, pro-étale, fppf — each is an object of `Sites`. The same formalism must own Zariski, étale, and Galois as instances.

* Operationalized and computable in some cases (not merely honest): for `X: Sch/F_q` finite type with a finite affine/étale cover `U={U_i→X}` and `F : Sh(X_ét,Q_ℓ)` constructible lisse (e.g. `Q_ℓ(n)` via `Z/ℓ^n` system `lim← F_n ⊗ Q_ℓ`), `RΓ(X_ét,F)` must be an effective object `EC: Ch^{eff}` with finite `ℓ`-adic coefficients via Čech `Č(U,F)` as `Tot` and graded `H^*_ét(X,Q_ℓ)=H^*(EC) : GrMod` with `H^*_ét.graded_piece(i)=H^i(EC)` and `Frob` action, computable via `X.etale_cohomology(Q_ℓ) : GrMod` with `H^*.graded_piece(i)` and comparable to `RΓ_c` already intaken for zeta/Weil. In the smooth proper case, comparison `H^*_ét(X_{\bar F_q},Q_ℓ) ≅ H^*_{MW/rigid}(X)⊗Q_ℓ : GrMod` via Monsky-Washnitzer / rigid cohomology gives a private computational adapter when the site model is not yet effective; for general singular `X`, retain `RΓ` as formal `D` with known type. Without this, `H^*_ét` remains a definition with no computational route, and the zeta/Weil and Lefschetz-trace leads would have no honest cohomology to compute against.

Intended owners: `categories/topology/sites.py` (`Site`, `GrothendieckTopology`, `Sieve`, `CoveringFamily` with axioms), `categories/topology/sheaves_on_site.py` (`Sh(C,J)`), `categories/etale/etale_site.py` (`X_ét`), `categories/etale/ladic_sheaves.py` (`Q_ℓ`, `Q_ℓ(n)` lisse), `categories/galois/galois_cohomology.py` (`H^*(Gal_K,-)=H^*_ét(Spec K,-) : GrMod` as graded specialization, not a parallel definition), `categories/etale/effective.py` (`RΓ` as effective `Ch` via `Č(U,F)` and MW/rigid adapter), `categories/graded/graded_modules.py` (`GrMod` with `graded_piece(i)` and `euler_characteristic : GrMod_{ZZ} → ZZ` via `χ(H^*) = Σ (-1)^i rank H^*.graded_piece(i)`), `categories/graded/euler_characteristic.py` (`Euler characteristic from ZZ-graded objects in complete generality`). Not a free `etale_cohomology(X, Q_ell)` function — `X.etale_site().cohomology(Q_ell) : GrMod` with `H^*.graded_piece(i)=H^i_ét`, `Spec(K).etale_cohomology(Q_ell) : GrMod`, with `X.etale_cohomology(Q_ell).effective_complex()` when computable; do not add `cohomology(i, Q_ell)` returning a bare `H^i`. Almost all cohomology requested in this intake is requested as graded `H^* : GrMod` with uniform `H.graded_piece(i)`, not as `H^i`; Euler characteristics just come from `GrMod_{ZZ}` in complete generality via `χ(H^*) = Σ (-1)^i rank H^*.graded_piece(i)` for any `H^* : GrMod_{ZZ}`, with `χ(H^*_{c,ét}) = Σ (-1)^i b_i` as instance.

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

* Must get closed forms: `Z(X,T) = ∏_{i=0}^{2 dim X} P_i(T)^{(-1)^{i+1}}` with `P_i(T) = det(1 - T·Frob | H^*_{c,ét}(X_{\bar F_q}, Q_ℓ).graded_piece(i)) ∈ Z[T]` (`H^*_{c,ét} : GrMod` with `H^*.graded_piece(i)=H^i_{c,ét}`), `P_0 = 1-T`, `P_{2n}=1-q^n T` for connected `X`. Construction is `X → (N_r = |X(F_{q^r})|) → Z = exp` with rational reconstruction (compare coefficients `N_r` with `log Z` expansion), not numeric `exp`.

* Must verify all Weil conjectures for these concrete `X` and return certificates, not just claim:
  * (W1) Rationality: `Z ∈ Q(T)` — check `Z` is rational function with `Z ∈ 1+T·Z[[T]]`
  * (W2) Functional equation: `Z(X, 1/(q^n T)) = ± q^{nχ/2} T^{χ} Z(X,T)` with `χ = Σ (-1)^i b_i`, `n=dim X`; verify as identity in `Q(T)`
  * (W3) Riemann hypothesis: `P_i(T)=∏(1-α_{ij} T)` with `|α_{ij}| = q^{w/2}` for `w=i` (purity) — verify by factoring `P_i` over `C` and checking `|α| = q^{i/2}` via `QQbar` absolute value, or via `ℓ`-adic weights. For concrete cases this is checkable: `P_i` split with known roots `q^{j}` or Weil numbers `α, \bar α`.
   * (W4) Betti numbers: `deg P_i = b_i = dim H^*_{c,ét}.graded_piece(i)` — compare with known `b_i` from `ℓ`-adic graded `H^*_{c,ét} : GrMod` (e.g. `b_i(P^n)=1` for even `i≤2n` else `0`; `b_i(Gr)` via Schubert cells).

* Requires: site cohomology `RΓ_c(X_{ét}, Q_ℓ)` from six-functor `R f_!` already noted, trace formula `N_r = Σ (-1)^i Tr(Frob^r | H^*_c.graded_piece(i))` with `H^*_c : GrMod`, and the comparison `Z = ∏ det(1-T·Frob|H^*_c.graded_piece(i))^{(-1)^{i+1}}`. The same `R f_!` and `Q_ℓ` owners above must supply `H^*_c : GrMod` and `Frob` action on each `graded_piece(i)`.

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
* Site `X_ét : Sites` and `ℓ≠p`, `Q_ℓ : Fields` as before; `Sh(X_ét,Q_ℓ) : AbCat` and derived `RΓ_c = R(p_!) : D(Sh) → D(Vect_{Q_ℓ})` for `p: X→Spec F_q` (proper-support pushforward from six functors). Object `H^*_{c,ét}(X_{\bar F_q}, Q_ℓ) = H^*(RΓ_c(Q_ℓ)) : GrMod_{Q_ℓ}` with `H^*_{c,ét}.graded_piece(i)=H^i_{c,ét}=H^i(RΓ_c) : Vect_{Q_ℓ}` finite-dimensional, with continuous `Gal(\bar F_q/F_q)`-action; `Fr_q` acts as `Frob : H^*_c.graded_piece(i) → H^*_c.graded_piece(i)`
* Grothendieck-Lefschetz trace formula (must exist to link counting to cohomology):
  ```
  N_r = Σ_{i=0}^{2n} (-1)^i Tr( Fr_q^r | H^*_c.graded_piece(i) )  with H^*_c : GrMod
  ```
  Without `R f_!` and `Tr` on the graded `H^*_c` this is not statable.

**Factorisation and statements**
* From trace, `Z` factors as
  ```
  Z(X,T)= ∏_{i=0}^{2n} P_i(T)^{(-1)^{i+1}},  P_i(T)=det(1-T·Fr_q | H^*_c.graded_piece(i)) ∈ Z[T] : Poly(Z)  with H^*_c : GrMod
  ```
  Need `Poly(Z) → Q(T)` and `deg P_i = b_i = dim H^*_c.graded_piece(i) : NN` (fourth Weil/Betti). This is rationality refinement.
* Functional equation needs Poincaré duality for `H^*_c` (`f^! Q_ℓ ≅ Q_ℓ(n)[2n]`) and `f_! ⊣ f^!` on graded `H^*_c`:
  ```
  Z(X, 1/(q^n T)) = ± q^{nχ/2} T^{χ} Z(X,T),  χ=χ(H^*_{c,ét}) = Σ(-1)^i b_i : ZZ  with b_i = rank H^*_{c,ét}.graded_piece(i), Euler characteristic of the ZZ-graded object H^*_{c,ét} : GrMod_{ZZ} (or GrMod_{Q_ℓ}) in complete generality — χ just comes from GrMod_{ZZ} via χ(H^*) = Σ (-1)^i rank H^*.graded_piece(i), not specific to étale
  ```
  as identity in `Q(T)` (needs `⊗` and dualizing complex).
* Riemann hypothesis needs algebraic numbers and weights: `P_i(T)=∏_j (1-α_{ij} T)`, `α_{ij} : \bar Q ⊂ C` via chosen `\bar Q↪C`, condition `|α_{ij}| = q^{i/2}` for all embeddings `|·|: \bar Q→C` (Weil numbers of weight `i`). Needs `Fields`, `AlgClosure`, `Abs: C→R_{≥0}`, and `Weight` as `NN` element. No numerics — `|α|=q^{i/2}` is equality in `R`.

**Not fundamental**
* `q=7`, `X=A^n,P^n,Gr(k,n)`, `N_r = q^{nr}` or `q`-binomial, explicit `P_i = 1-q^j T` — elements `:NN` and morphisms `Spec F_{q^r}→X` whose counts give closed `Z = 1/(1-q^n T)` etc.; the functor `X ↦ Z(X)` and its factorisation are.

## Desired capability: operationalize Lefschetz trace for Frob — note 2026-09-15

Need a way to operationalize the Lefschetz trace formula, especially on étale cohomology for the trace of Frobenius.

Need `Tr(Frob^r | H^*_{c,ét}(X_{\bar F_q}, Q_ℓ).graded_piece(i)) : Q_ℓ` as computable morphism on the graded cohomology `H^*_{c,ét} : GrMod`, not a formal symbol. Formula
```
N_r = Σ_{i=0}^{2n} (-1)^i Tr( Fr_q^r | H^*_{c}.graded_piece(i) )  with H^*_c : GrMod
```
must be executable: from `X : Sch/F_q` produce graded `H^*_c : GrMod` with `H^*_c.graded_piece(i)=H^i_c : Vect_{Q_ℓ}` and `Frob : End(H^*_c.graded_piece(i))` (via `X_ét`, `RΓ_c = R(p_!)`, `Q_ℓ(n)`), compute its trace via `Vect_{Q_ℓ}` linear algebra, and compare with `|X(F_{q^r})| : NN` (finite-set count). This is the bridge between counting and cohomology that makes `Z(X,T)=∏ P_i(T)^{(-1)^{i+1}}` effective, where `P_i(T)=det(1 - T·Frob | H^*_c.graded_piece(i))`.

Requires: `Frob : X_{\bar F_q} → X_{\bar F_q}` as `Fr_q × id` on `X×_{F_q}\bar F_q`, its action `Frob^*: H^*_c.graded_piece(i) → H^*_c.graded_piece(i)` via functoriality of `RΓ_c` on graded `H^*_c : GrMod`, and `Tr: End(V) → Q_ℓ` on `Vect_{Q_ℓ}` (finite-dimensional). Operationalization means: when `H^*_c : GrMod` is presented (e.g. via known cell decomposition for `A^n, P^n, Gr` or via Monsky-Washnitzer / crystalline `RΓ_c` with Frobenius lift for general `X`), actually return matrix `M_i = Frob|_{H^*_c.graded_piece(i)} : Mat_{b_i}(Q_ℓ)` and compute `Tr(M_i^r)`, `det(1 - T M_i)` exactly in `Z[T]`. Not a placeholder `trace_of_frob` stub.

For concrete families (`A^n, P^n, Gr(k,n)` and some curves) the trace is already known from explicit `P_i`: e.g. `Tr(Frob|H^*_c.graded_piece(2j))=q^j`, otherwise `0`; for `Gr`, `Tr` is `q^{something}` via Schubert. The operational trace must reproduce those `N_r` via the sum, certifying the formula for those `X`. For general `X`, the trace is the computational content of Monsky-Washnitzer / rigid cohomology `H^*_{MW}: GrMod` with Frobenius lift, behind the same `RΓ_c` interface — private adapter, but `X.etale_cohomology(Q_ell) : GrMod` with `H^*.graded_piece(i)` and `Frob.matrix()` stay owned.

Intended owners: `categories/etale/trace_formula.py` (`LefschetzTrace` with `Tr(Frob^r|H^*_c.graded_piece(i))` and `N_r = Σ (-1)^i Tr`), `categories/etale/frobenius.py` (`Frobenius : End(H^*_c.graded_piece(i))` as `RΓ_c(Fr_q)` on graded `H^*_c`), `categories/etale/monsky_washnitzer.py` (private MW adapter for general `X` when `RΓ_c` not yet known). Not a free `trace_frobenius(X)` — `X.etale_cohomology_c(Q_ell) : GrMod` with `X.etale_cohomology_c(Q_ell).graded_piece(i).frobenius().trace(r)` on the graded cohomology, with `X.point_count(r)` on the variety object for comparison; do not add `etale_cohomology_c(i, Q_ell)` returning bare `H^i`.

## Desired capability: HH(A) — Hochschild (co)homology — note 2026-09-16

Support `HH(A)` — Hochschild (co)homology of an (associative, possibly dg) algebra `A`.

* `HH(A)` is not a bare list of groups computed by a helper. Homology is the homology of the Hochschild complex `C(A): ... → A^{⊗ n+1} → A^{⊗ n} → ...` with differential `b(a0⊗...⊗an)= Σ (-1)^i ... + (-1)^n a_n a_0 ⊗ ...`, as object `HH_*(A) = ⊕_n HH_n(A) : GrMod` (`HH_0 = A/[A,A]`, etc.) with `HH_*(A).graded_piece(n)=HH_n(A)`. For dg `A`, `C(A)` is the derived tensor `C(A)= A ⊗^{L}_{A⊗A^{op}} A : Ch`, i.e. `HH_*(A)= Tor^{A⊗A^{op}}_*(A,A) : GrMod`. Need `HH_*(A)` as functor `HH_*: Alg_{dg} → GrMod` (or `D(Ab)`), with `HH_*(A)` computed as `H_*(C(A))` and `HH_*(A).graded_piece(n)=H_n(C(A))`. Cohomology is `HH^*(A) = ⊕_n HH^n(A) : GrAlg` with `HH^n(A)=Ext^n_{A^e}(A,A)=H^n(RHom_{A^e}(A,A)) : Mod_k` and `HH^*(A).graded_piece(n)=HH^n(A)`, with cup product `HH^p⊗HH^q→HH^{p+q}` via Yoneda `Ext^p⊗Ext^q→Ext^{p+q}` and Gerstenhaber bracket `[-,-]: HH^p⊗HH^q→HH^{p+q-1}`. Need `HH^*(A)` as functor `HH^*: Alg_{dg} → GrAlg` with `HH^*(A)=H^*(RHom_{A^e}(A,A)) : GrAlg`.

* Requires: category `Alg_{dg}(k)` (dg algebras over `k` with `k` a commutative ring), enveloping algebra `A^e = A⊗A^{op} : Alg`, `Bimod_A = Mod_{A^e}`, and derived `⊗^L` and `RHom`. Homology uses `⊗^L : HH_*(A)=Tor^{A^e}_*(A,A)`; cohomology uses `RHom : HH^*(A)=Ext^*_{A^e}(A,A)`. Interface must be `A.hochschild_complex() → C(A) : Ch(k)` and `A.hochschild_homology() → HH_*(A) : GrMod` with `HH_*(A).graded_piece(n)=HH_n(A)` and `A.hochschild_cohomology() → HH^*(A) : GrAlg` with `HH^*.graded_piece(n)=HH^n(A)`, with `HH_0 = abelianization` and `HH^0 = center Z(A)`.

* Expected compatibilities (at least for smooth cases): HKR isomorphisms — homology `HH_n(A) ≅ Ω^n_{X/k}` for smooth commutative `A = O(X)` as `GrMod` with Connes differential `B: HH_n → HH_{n+1}` matching `d_{dR}`, and cohomology `HH^n(A) ≅ PolyVect^n_{X/k} = ∧^n T_{X/k}` as `GrAlg` with Gerstenhaber bracket matching Schouten bracket `[-,-]_S` and cup product matching wedge `∧`. For scheme `X`, `HH_*(X)=HH_*(Perf(X))` with `HH_*(X) ≅ ⊕ H^i(X, Ω^j)` and `HH^*(X)=HH^*(Perf(X))` with `HH^*(X) ≅ ⊕ H^i(X, ∧^j T_X)` as `GrMod`/`GrAlg`. Need `HH_*` and `HH^*` to compose with `Perf` and `QCoh` via Morita invariance `HH_*(A) ≅ HH_*(Perf_A)` and `HH^*(A) ≅ HH^*(Perf_A)`.

* In some cases (smooth proper `X` of dimension `n`, e.g. `P^n, Gr(k,n),` smooth curves) `HH_*(X) : GrMod` and `HH^*(X) : GrAlg` are finite and explicitly computable via HKR, and must be verified. For general `A`, `HH_*` and `HH^*` are retained as formal (co)complexes with known graded type, not forced to compute.

Intended owners: `categories/homology/hochschild.py` (`HochschildComplex` `C(A)`, `HH_*(A)=Tor^{A^e}_*` as `GrMod` with `graded_piece(n)` and `HH^*(A)=Ext^*_{A^e}` as `GrAlg` with `graded_piece(n)`, Gerstenhaber and cup), `categories/algebras/dg_algebras.py` (`DgAlgebra` with `A^e`, `Bimod` and `⊗^L`/`RHom`), `categories/schemes/hochschild_kostant_rosenberg.py` (HKR `HH_n(O_X) ≅ Ω^n` and `HH^n(O_X) ≅ PolyVect^n`). Not a free `hochschild_homology(A)` — `A.hochschild_complex() : Ch`, `A.hochschild_homology() : GrMod` with `A.hochschild_homology().graded_piece(n)` and `A.hochschild_cohomology() : GrAlg` with `A.hochschild_cohomology().graded_piece(n)`, with `Perf(X).hh()` and `Perf(X).hh_cohomology()` for schemes; do not add `hochschild_homology(n)` returning bare `HH_n` or `hochschild_cohomology(n)` returning bare `HH^n`.

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

## Desired capability: composition series, filtrations, associated graded, semidirect, is_simple, Jordan-Hölder, Inn/Out, artinian/noetherian, subgroup poset — note 2026-09-15

Need composition series for groups, modules, algebras, etc. Need filtrations to support associated graded. Need semidirect product support, is_simple for objects in any abelian category, Jordan-Hölder decompositions, inner and outer automorphisms of groups, need is_artinian and is_noetherian for modules and rings. Need to support entire subgroup poset of a group as an honest poset.

* Composition series is not a list of subgroups with a name. For `G : Groups` (finite, profinite, `FPGroups` with `Groups().framed`), `M : R-Mod` (`R: Rings`), `A : Alg_R`, a composition series is `0 = G_0 ⊲ G_1 ⊲ … ⊲ G_n = G` (resp. `0 ⊂ M_0 ⊂ … ⊂ M_n = M` as `R`-submodules, `0 ⊂ A_0 ⊂ …`) with each factor `G_{i+1}/G_i` simple (no nontrivial proper normal subgroup), `M_{i+1}/M_i` simple `R`-module, etc. Length `n = ℓ(G) : NN` is Jordan-Hölder length. Interface `G.composition_series() → 0⊲G_1⊲…⊲G : Filt(Groups)` with `gr_i = G_{i+1}/G_i : GrAb/Groups` simple, and `M.composition_series() → Filt(R-Mod)` similarly; when `G` finite, series exists iff `G` finite length (trivially); when `M` finite length `R`-module, same. Not a free `composition_series(G)` returning Python `list` — `G.composition_series()` as filtered object with `F^pG` and `gr_F^pG` simple.

* Filtrations to support associated graded: for any `X : AbCat` abelian (groups with normal series, `R-Mod`, `Alg_R`, `Ch`), filtration `F : Filt(X)` is decreasing `… ⊃ F^pX ⊃ F^{p+1}X ⊃ …` by subobjects (`F^pX ↪ X` mono) or increasing `0=F_0⊂F_1⊂…` with `∪F_p=X`. Associated graded `gr_F(X) = ⊕_p gr_F^p X` where `gr_F^p X = F^pX / F^{p+1}X : X` as `GrMod_{ZZ}` object `gr: Filt(X) → Gr(X)` functor with `gr_F^p` simple when `F` is composition series. Requires `FiltCh` lead already intaken for chain complexes; now extend to `Filt(Groups)`, `Filt(R-Mod)`, `Filt(Alg)` uniformly via `Subobjects` construction `Sub_G` category, not a bare `filtration` attribute.

* Semidirect product support: for `N,H : Groups` with action `φ: H → Aut(N)` as group morphism `φ: H → Aut(N)` already intaken via `G-action is morphism` (caller constructs `ρ: G→Aut(M)`), `N⋊_φ H : Groups` is `N ⋊ H = {(n,h) | (n_1,h_1)(n_2,h_2)=(n_1·φ_{h_1}(n_2), h_1h_2)}` with `N ⊲ N⋊H`, `H ≤ N⋊H`, `N⋊H/N ≅ H`, `1→N→N⋊H→H→1` split via `s: H→N⋊H, s(h)=(1,h)`. Interface `N.semidirect_product(H, φ) → N⋊_φ H : Groups` with `inclusion N↪N⋊H`, `projection N⋊H↠H`, `section H↪N⋊H`, and detection `G.is_semidirect_product ⇒ (N,H,φ)` via complement `H≤G` with `G=NH`, `N∩H=1`. When `H` acts on `R-Mod` similarly `M⋊G`.

* `is_simple` for objects in any abelian category: for `X : AbCat` (any `C` abelian with `0`, kernels, cokernels, `Hom`), `X.is_simple() ⇔ X≠0 ∧ ∀ mono i: S↪X (S=0 ∨ S≅X)` i.e. no nonzero proper subobject `0⊂S⊂X`. Equivalently `X` has exactly two subobjects `{0,X}` in `Sub(X)` lattice. For `G : Groups` not abelian category but simple group means no nontrivial proper normal subgroup; for `R-Mod` simple means no nontrivial proper submodule. Interface is `X.is_simple() → Bool` as predicate on the object in its category, with `X in AbCat` dispatched by `X.category().is_abelian()` and `Sub(X)` lattice already via `Subobjects` construction. No separate `is_simple_group` vs `is_simple_module` — one `is_simple` on `C` when `C` abelian, plus `G.is_simple_group()` when `Groups` non-abelian variant.

* Jordan-Hölder decompositions: any finite-length `X : AbCat` has composition series and `gr(X) = ⊕ gr_i` multiset of simple factors is unique up to permutation/isomorphism (Jordan-Hölder theorem): if `0⊂X_1⊂…⊂X_n=X` and `0⊂Y_1⊂…⊂Y_m=X` are composition series, then `n=m` and `{gr_i(X_•)} ≅ {gr_j(Y_•)}` as sets with multiplicity. Interface `X.jordan_holder_factors() → Multiset(SimpleObjects)` as `Gr` or `Multiset` of simples with `X.jordan_holder_series()` returning one series and `X.length() → n: NN` plus witness that any two series have same `gr` up to permutation (via Schreier refinement). For groups finite, `G.composition_factors() → Multiset(SimpleGroups)` via `gr_i = G_{i+1}/G_i`.

* Inner and outer automorphisms of groups: for `G : Groups`, `Inn(G) = {c_g : x↦gxg^{-1} | g∈G} ≤ Aut(G)` as normal subgroup `Inn(G) ⊲ Aut(G)`, `Aut(G) : Groups` already as `AutCat`, `Out(G)=Aut(G)/Inn(G) : Groups` quotient. Interface `G.inner_automorphisms() → Inn(G) : Subgroups(Aut(G))` via `g ↦ c_g` morphism `G→Aut(G)` with kernel `Z(G)`, `G.outer_automorphism_group() → Out(G) = Aut(G)/Inn(G) : Groups` as quotient, and `Aut(G) → Out(G)` projection. Distinguish `Inn` as image of `Ad: G→Aut(G)` vs `Out` as group of outer classes.

* `is_artinian` and `is_noetherian` for modules and rings: for `M : R-Mod` (`R: Rings`), `M.is_artinian() ⇔` every descending chain `M⊃M_1⊃M_2⊃…` stabilizes (`∃n M_n=M_{n+1}`) ⇔ every nonempty set of submodules has minimal element; `M.is_noetherian() ⇔` every ascending chain `M_1⊂M_2⊂…` stabilizes / every submodule finitely generated. For `R : Rings`, `R.is_artinian()` as `R`-module over itself (left-artinian), `R.is_noetherian()` left-noetherian. When `R` commutative PID, `is_noetherian` holds. For finite-length `M`, both artinian and noetherian. Interface `M.is_artinian()`, `M.is_noetherian()`, `R.is_artinian()`, `R.is_noetherian()` on the module/ring objects with `Sub(M)` lattice already, not a free `is_artinian(M)` function returning bare `Bool` without `Sub` data.

* Entire subgroup poset of a group as an honest poset: for `G : Groups` (finite, finitely presented with computable `Sub(G)` when finite index bound), `Sub(G) = {H ≤ G} : Sets(Sets)` with partial order `H ≤ K ⇔ H⊆K` as poset `Pos = (Sub(G), ⊆)` with `⊥ = {1}`, `⊤ = G`, meets `H∧K = H∩K`, joins `H∨K = ⟨H∪K⟩` when computable, and lattice when `G` finite. Need `Poset` object `P = SubPoset(G) : Posets` with `P.elements() → Set(Sub)`, `P.le(H,K) ⇔ H≤K`, `P.cover_relations()`, `P.hasse_diagram()`, and as poset category `PosCat(P) : Cat` with `Hom_P(H,K)=1` if `H≤K` else `∅`. Interface `G.subgroup_poset() → P : Posets` honest `Poset`, not a `list` of subgroups, with `P.as_category() → Cat` and `P.as_poset()` roundtrip.

Intended owners: `categories/algebra/composition_series.py` (`CompositionSeries` `0=G_0⊲…⊲G_n=G` with `gr` simple, `length`), `categories/abelian/filtrations.py` (`Filt(X)`, `gr_F`, `AssociatedGraded` functor), `categories/groups/semidirect.py` (`SemidirectProduct N⋊_φ H` with `φ: H→Aut(N)` morphism, `split ses`), `categories/abelian/is_simple.py` (`is_simple` predicate on any `AbCat` via `Sub`), `categories/algebra/jordan_holder.py` (`JordanHolder` with `gr` multiset uniqueness), `categories/groups/automorphisms.py` (`Inn(G)⊲Aut(G)`, `Out(G)=Aut/Inn` via `Ad`), `categories/modules/chain_conditions.py` (`is_artinian`, `is_noetherian` via ACC/DCC on `Sub`), `categories/groups/subgroup_poset.py` (`SubPoset(G) : Posets` with `PosetCat`). Not a free `composition_series(G)` list — `G.composition_series()`, `X.is_simple()`, `N.semidirect_product(H,φ)`, `G.subgroup_poset()` on the group/module/abelian objects.

## Desired capability: open-set categories, powersets, topologies, poset ↔ poset-category fluid interface — note 2026-09-15

Need to support open set categories `Op(X)`, powersets, topologies as subsets of power sets, poset structure on `P(X)` and `Op(X)`, need fluid interface between posets and poset categories.

* Open set category `Op(X)` is not a bare set of opens. For `X : Top` topological space with `τ_X : Top` as set of opens `τ_X ⊂ P(X)` (below), `Op(X) : Cat` is the poset category whose objects are `U ∈ τ_X` (each `U⊂X` open) and morphisms `Hom_{Op(X)}(U,V)=1` if `U⊆V` else `∅` (single inclusion `U↪V` when `U⊆V`). Composition is inclusion transitivity. `Op(X)` is a poset category (thin, skeletal) with terminal `X`, initial `∅`, pullbacks `U∧V = U∩V` as categorical product (meet), coproduct `U∨V = U∪V` as join, and `Op(X) = (τ_X, ⊆)` as `PosetCat`. Interface `X.open_set_category() → Op(X) : PosCat` with `X.open_sets() → τ_X : Sets(Sets)` and `Op(X).inclusion(U,V) → Hom` and `Op(X).as_poset() → (τ_X,⊆)`; for `X : Sch` with `Top(X)` Zariski, `Op(X)` is Zariski opens.

* Powerset `P(X) = 2^X : Sets(Sets)` is not a Python `set`. For `X : Sets` (or `X : Top` underlying set `U(X)`), `P(X) = {A | A⊆X} : Sets` as object `P(X) : Sets` with `|P(X)| = 2^{|X|}` cardinality via `|P(X)| = 2^{|X|}` when `|X| : Cardinal` computable and finite, `∅∈P(X)` as bottom, `X∈P(X)` top, operations `∪: P×P→P` union, `∩: P×P→P` intersection, `^c: P→P` complement `A^c = X\A`, `Δ` symmetric difference, all as morphisms in `Sets`. Poset structure `P(X) : Posets` with `A ≤ B ⇔ A⊆B` via `PosCat` below; lattice `P(X)` is Boolean lattice `B = (P(X),⊆,∪,∩,^c)`. Interface `X.powerset() → P(X) : Sets` with `P(X).as_poset() → Posets` (see fluid below) and `P(X).as_boolean_algebra()`.

* Topologies as subsets of power sets: `τ ⊂ P(X)` collection of subsets of `X` satisfying `∅∈τ`, `X∈τ`, `τ` closed under arbitrary unions `⋃_{i∈I}U_i ∈ τ` (finite vs arbitrary distinguished for topology vs Grothendieck `J` already intaken) and finite intersections `U∩V ∈ τ`. `τ : Topologies(X)` is object of `Top(X) : Sets` where `Top(X) = {τ ⊂ P(X) | τ topology}`. Interface `Topology(X, τ)` constructor with `X.topology() → τ_X : Topologies(X)` for `X: Top` (its defining `τ`), `Powerset.poset` etc. For `X` finite, `τ` enumerable; for `X` general, retained as formal `τ` with axioms.

* Poset structure on `P(X)` and `Op(X)` by inclusion: both `P(X)` and `Op(X)` (via underlying `τ_X`) carry poset ` (P, ⊆)` with `A≤B` as `A⊆B`, meet `A∧B=A∩B`, join `A∨B=A∪B`, order `≤` as relation `R⊂P×P`. Need `Poset` object `P = (E, ≤)` with `E : Sets` elements, `≤: E×E→Bool` reflexive/transitive/antisymmetric, `P.hasse`, `P.comparable`, `P.meet`, `P.join` when lattice. Interface `P(X).poset() → (P(X),⊆) : Posets` and `Op(X).poset() → (τ_X,⊆)` via same `PosCat`; for `P(X)` Boolean lattice, `P.dual()`, `P.intervals()` etc.

* Fluid interface between posets and poset categories: every `Poset P=(E,≤): Posets` has associated thin category `PosCat(P): Cat` with `Ob = E`, `Hom_P(x,y)=1` if `x≤y` else `0`, `id_x` the `x≤x` witness, `∘` is transitivity. Conversely every poset category `C : Cat` thin skeletal with at most one morphism between objects has underlying poset `Pos(C) = (Ob(C), ≤_C)` where `x ≤_C y ⇔ Hom_C(x,y)≠∅`. Need functors `PosCat: Posets → Cat_pos` and `Pos: Cat_pos → Posets` inverse (equivalence `Posets ≃ Cat_{pos}`), with natural isomorphism `Pos(PosCat(P))≅P` and `PosCat(Pos(C))≅C`. Interface must be fluid: `P.as_category() → PosCat(P) : Cat` and `C.as_poset() → Pos(C) : Posets` with `P.as_category().as_poset() == P` and `Op(X).as_poset()` / `P(X).as_category()` roundtrip, and `P.as_category().as_poset().as_category() == PosCat(P)` etc. Reuse category `Posets` lead's `SubPoset(G)` above — same `Posets` owner, so `Sub(G)` poset and `Op(X)` poset share `Posets` type, and `Cat` thin categories are objects of `Cat` already.

Intended owners: `categories/topology/open_sets.py` (`OpenSetCategory Op(X): Cat` with `X.open_set_category()`, `Hom=Inclusion`), `categories/sets/powerset.py` (`Powerset P(X)=2^X : Sets` with `∪,∩,^c` and `as_poset()` Boolean lattice), `categories/topology/topologies.py` (`Topology τ⊂P(X)` with `∅,X∈τ`, `⋃∈τ`, `∩∈τ`), `categories/posets/poset_category.py` (`Posets`, `PosCat: Posets ⇄ Cat_pos :Pos` fluid `as_category()`/`as_poset()` equivalence). Not a free `open_sets(X)` list — `X.open_set_category()` with `Op(X).poset()` and `P(X).as_poset().as_category()` roundtrip on the space/set objects.

## Desired capability: short exact sequences `1→A→B→C→1` and fibrations `F→E→B` classified by Ext / twisting cocycle — note 2026-09-15

Ask for a way to compute, algorithmically, given a short exact sequence of groups `1→A→B→C→1`, computing `B` as a twisted product/sum of `A` and `C` determined by an `Ext` class/cocycle. Similarly for fibrations `F→E→B`.

A group extension is not an object; a short exact sequence of groups is. A group can be isomorphic to an extension of `C` by `A`, but `B` alone is just a group. The object is the SES

```
1 → A —i→ B —p→ C → 1
```

with `i: A↪B` mono (identified with normal `i(A)⊲B`) and `p: B↠C` epi, `im i = ker p`. Morphisms of SES are triples of group homomorphisms commuting with `i,p`. Similarly `0→A→B→C→0` in `R-Mod` is the object in the abelian category, not a new `Extension` wrapper. A fibration sequence `F→E→B` (Serre fibration `F↪E↠B` with `F` fiber over `b0∈B`) is the object, not a `TwistedProduct` wrapper. Constructing the SES / fibration sequence is the work; returning `B` or `E` alone forgets the structure.

* For groups: the SES `1→A→B→C→1` (e.g. `A,C : Groups` with `A` normal in `B`, `B/A≅C`; `A` abelian or general, `C` acting via `C→Out(A)`) has class `α ∈ H^2(C,A)` / `Ext^1(C,A)` / `H^2(C,Z(A))`. Choose a set-theoretic section `s: C→B` (`p∘s=id_C`, `s(1)=1` after normalization), then factor set `c: C×C→A`, `c(x,y)=s(x)s(y)s(xy)^{-1}∈A`, with twisted multiplication on the underlying set `A×C` as `(a1,c1)(a2,c2)=(a1·^{c1}a2·c(c1,c2), c1c2)` where `^{c}a=s(c)a s(c)^{-1}` is the `C↷A` action. Class `[c]∈H^2(C,A)` (or `Ext^1` when `A` abelian `Z[C]`-module, or `H^2(C,Z(A))` for `A` nonabelian via center) classifies the SES up to isomorphism of SES. `Ext` already intaken via `RHom` on `D(ZZ[C]-Mod)` / `D(ZZ-Mod)` with `Ext^n=R^n Hom`; given `[c]` construct SES `1→A→B_c→C→1` with `B_c` underlying set `A×C` and law `*_c` and `(i_c,p_c)` as above and `[B_c]=[c]`. Split case `c=0` gives `B≅A⋊C` semidirect (`∃s` homomorphism); central `A≤Z(B)` when action trivial. Interface is on the SES object: `SES(1→A→B→C→1).extension_class() → [c]∈H^2(C,A)` where `cocycle c: C×C→A` satisfies `dc=0` (`c(xy,z)·c(x,y)^z=c(x,yz)·c(y,z)`) modulo coboundaries `[c]=[c']⇔∃b:C→A c'=c·db`, and conversely `SES_from_cocycle(A,C,c) → (1→A→A×_c C→C→1) : SES`. No `GroupExtension` object — the SES is the object and `B` is its middle term.

* Algorithmically realizing the middle term from `[c]`/`c` uses: group cohomology `H^n(G,M)=Ext_{ZZ[G]}^n(ZZ,M)` via `BarRes→RHom` with `M:ZZ[C]-Mod` (the `C`-module `A` via action), cocycle `c∈Z^2(C,A)=ker d^2⊂C^2`, class `[c]∈H^2=Z^2/B^2`, and the twisted law above. For `A` abelian finite with `H^2(C,A)` via Smith over `ZZ` when `C` finite / `C=ZZ^n` etc., the SES middle `B` is constructed as `Groups` with `A×C` underlying set and `*_c`.

* Similarly for modules/algebras: SES `0→A→B→C→0` in `R-Mod` (abelian category) is determined by `Ext^1_R(C,A)=H^1(RHom(C,A))` class `ξ: C→A[1]` in `D(R-Mod)`; `ξ=0` gives split `B≅A⊕C`. Class `ξ` is Baer sum `0→A→B→C→0 = pushout of `0→K→P→C→0` (projective presentation) along `i:K→A` representing `ξ`. Interface: SES `0→A→B→C→0` has `ses.extension_class() → ξ∈Ext^1(C,A)`, and `ses_from_class(C,A,ξ) → (0→A→B_ξ→C→0)`. No `ModuleExtension` wrapper — the SES is the object.

* Similarly for fibrations `F→E→B` (Serre fibration `F↪E↠B` with `B` path-connected, `F` fiber over `b0∈B`): already intaken via Kenzo `F×_τ B` with twisting operator `τ: B_{∗+1}→G_∗` where `G` acts on `F` via `G=Aut(F)` or `ΩB`. Here `E≃F×_τ B` twisted cartesian product is the middle term of the fibration sequence, determined by `k`-invariant / twisting cocycle `τ∈Z^{n+1}(B;π_n(F))` / `H^{n+1}(B;π_n(F))` when `F=K(π_n,n)` iteratively (Postnikov), or more generally `[τ]∈[B,BAut(F)]` classifying map. Construction uses `tEZ` / `BPL` / `Bar/Cobar` as `F×_τ B ⇔ F⊗_t B`; algorithmically `B` base `sSet` with `EC` effective, `F` fiber with `EC`, and `τ` simplicial twisting operator (`B_{n+1}→F_n`, Kan condition `d_0 τ(b)=τ(d_0b)·∂b`), then `F×_τ B` sSet with simplices `(f,b)`, `d_0(f,b)=(d_0f·τ(b), d_0b)`. Interface: fibration sequence `F→E→B` has `fib_seq.twisting_class() → [τ]∈H^{n+1}(B;π_n(F))` / `[B→BAut(F)]`, and `fib_seq_from_twisting(F,B,τ) → (F→F×_τ B→B)`. No `TwistedProduct` object type — the fibration sequence is the object and `F×_τ B` is its total space.

* Requires: `H^n(G,M)=Ext_{ZZG}` (group cohomology), `Ext^1_R(C,A)=R^1Hom` (`RHom`/`D(R-Mod)`), `H^n(B;π)` via `sSet` cohomology via `EC`/`Ω/B`, `Bar`/`Cobar` for `H^2(C,A)` as `Ext`, and `sSet` twisting operator `τ` / `G⊣W̄`, all already intaken. No new cohomology — reuse `Ext`/`Tor`/`D` and `sSet`/`τ`.

Intended owners: `categories/groups/short_exact_sequences.py` (`SES 1→A→B→C→1` with `i: A↪B`, `p: B↠C`, `ses.extension_class()∈H^2(C,A)` via `c∈Z^2`; constructor `ses_from_cocycle(A,C,c)→SES` with middle `A×_c C`), `categories/algebras/short_exact_sequences.py` (`SES 0→A→B→C→0` in `R-Mod` via `ξ∈Ext^1_R(C,A)` Baer sum; `ses_from_class(C,A,ξ)→SES`), `categories/topology/fibrations.py` + `categories/homotopy/fibration_sequences.py` (`FibrationSequence F→E→B` with `τ: B→G` twisting operator, `fib_seq.twisting_class()∈[B,BAut(F)]`/`H^{n+1}`; constructor `fib_seq_from_twisting(F,B,τ)→FibrationSequence` with total `F×_τ B`), delegating to `categories/derived/ext_tor.py` (`Ext^1`, `H^2`), `categories/group/cohomology.py` (`H^2(C,A)` via `Bar`), `categories/topology/simplicial_sets.py` (`τ` Kan condition). Not a free `extension(A,C,cocycle)` returning bare group — SES `1→A→B→C→1` is the object `B=(A×C,*_c)` with `i:A↪B`, `p:B↠C`, and `F→E→B` is fibration sequence with class in `H^2`/`H^{n+1}`.

## Desired capability: Lie groups → Lie algebras, matrix groups as Lie groups, algebraic / Lie / group scheme interfaces, Ad/ad — note 2026-09-15

For `G` a Lie group, extract `g = Lie(G)` its Lie algebra. All standard matrix groups promoted to Lie groups, `Mat_{n×n}` being the Lie algebra of `GL_n`, etc. Need good interfaces for both algebraic groups and Lie groups and general group schemes.

* Lie functor: `Lie: LieGroups → LieAlgebras_R` (over `R = RR` or `CC` where `LieGroups` lives) is functor sending `G : LieGroups` (smooth manifold `G : Man` with smooth `m:G×G→G`, `e:Spec R→G`, `inv:G→G`) to `g = Lie(G) = T_e G : LieAlgebras` with Lie bracket `[X,Y] = [X^L,Y^L]_e` from left-invariant vector fields `X^L, Y^L ∈ Γ(TG)` (`X^L_g = dL_g(X)`). Morphism `φ: G→H` in `LieGroups` induces `Lie(φ)=dφ_e: g→h` Lie algebra homomorphism ` [dφ_e(X), dφ_e(Y)] = dφ_e([X,Y])`. Need `G.lie_algebra() → g : LieAlgebras` and `φ.lie_map()` on morphisms, with `Lie(G×H)≅Lie(G)⊕Lie(H)`, `Lie(G^{an})` compatibility for algebraic `G` below. Exponential `exp_G: g → G` via flow of left-invariant field, with `d(exp)_0 = id_g` and `exp((t+s)X)=exp(tX)exp(sX)`, natural `φ∘exp_G = exp_H∘Lie(φ)`.

* Matrix groups promoted to Lie groups (and to `AlgGroups`/`GrpSch`): `GL_n(R) = {M∈Mat_{n×n}(R) | det M ∈ R^×} : LieGroups` with underlying manifold `GL_n(R) ⊂ Mat_{n×n} ≅ R^{n^2}` open, `Lie(GL_n)=Mat_{n×n} = gl_n` with `[A,B]=AB-BA` as `Mat` commutator; `SL_n(R)=ker(det:GL_n→G_m)` `Lie(SL_n)=sl_n={A|tr A=0}`; `O_n(R)={M|M^tM=I}` `Lie(O_n)=so_n={A|A^t=-A}`; `SO_n` identity component; `U_n={M|M^*\!M=I}` `Lie(U_n)=u_n={A|A^*=-A}`; `SU_n=U_n∩SL_n(C)` `Lie=su_n`; `Sp_{2n}={M|M^t J M=J}` `Lie=sp_{2n}` etc., with correct `R=RR,CC`. Each is object `G : LieGroups` with `G.underlying_manifold() : Man`, `G.lie_algebra() = gl_n` etc. as above, not a bare matrix group alias. Also as algebraic groups `G : AlgGroups/k` (`GL_n=Spec k[x_{ij},det^{-1}]` etc.) with same `Lie` after analytification `G^{an}:LieGroups`.

* Interfaces for algebraic groups / Lie groups / group schemes: distinct categories with faithful functors:
  - `AlgGroups_k : Cat` — `G : Sch/k` smooth affine with `m:G×G→G`, `e:Spec k→G`, `inv` as `Sch/k` morphisms, e.g. `GL_n, SL_n, SO_n, Sp_{2n}, G_m, G_a`, reductive, etc.; `AlgGroups_k → LieGroups` via analytification `G ↦ G^{an}` when `k=RR,CC` (`G^{an}=G(C)` with analytic topology), `G^{an}.lie_algebra() = Lie(G)` as algebraic Lie algebra `Lie(G)=T_eG` same `R`-module.
  - `LieGroups : Cat` as above (smooth manifold group); forgetful `LieGroups → Groups` via underlying abstract group `G ↦ G^{abs}`.
  - `GrpSch_S : Cat` — group schemes over base `S=Spec R` / `Spec ZZ` (`G: Sch/S` with group law), e.g. `μ_n, α_p`, `GL_{n,ZZ}`; base-change `G_R = G×_S Spec R : GrpSch_R`; `GrpSch_S → Groups` via `G ↦ G(R)` points; `AlgGroups_k ⊂ GrpSch_k` smooth finite-type.
  Base-change functor `(-)_R: GrpSch_S → GrpSch_R` compatible with `Lie` when smooth (`Lie(G_R)=Lie(G)⊗_S R`). Need `G.base_change(R) → G_R` and `G.analytification() → G^{an}`.

* `Ad` and `ad`: for `G : LieGroups` (or `G : AlgGroups` smooth) with `g=Lie(G)`, adjoint representation `Ad_G: G → GL(g) : Groups` is group morphism `Ad_G(g)= d(c_g)_e` where `c_g: G→G, c_g(h)=ghg^{-1}` conjugation, so `Ad_G(g)(X)= gXg^{-1}` for matrix groups; on Lie algebra level `ad_g: g → gl(g)` is `ad_g(X)(Y)=[X,Y]` (`ad = Lie(Ad)`). Concretely `ad: LieAlgebras → End(g)` as Lie algebra morphism `ad_X = [X,-]`. Interface `G.adjoint_representation() → Ad_G : G → Aut(g)` as `Rep(G)` object ` (g, Ad_G) : Rep(G)` and `g.adjoint_representation() → ad_g : g → End(g)` as `Rep(g)`; for algebraic `G`, `Ad_G : G → GL(g)` is `AlgGroups` morphism (algebraic representation), with same analytification.

Intended owners: `categories/lie/lie_algebras.py` (`LieAlgebra` with `[,-]`, `ad`), `categories/lie/lie_groups.py` (`LieGroup` with `G.lie_algebra() → g`, `exp: g→G`, `Lie: LieGroups→LieAlgebras` functor), `categories/groups/matrix_groups.py` (`GL_n, SL_n, O_n, SO_n, U_n, SU_n, Sp_{2n}` as `LieGroups` and `AlgGroups` with `Lie(GL_n)=Mat_{n×n}=gl_n`, `Lie(SL_n)=sl_n` etc.), `categories/groups/algebraic_groups.py` (`AlgGroups` with `G^{an}`), `categories/groups/group_schemes.py` (`GrpSch` with `G_R` base-change), `categories/representations/adjoint.py` (`Ad_G: G→GL(g)`, `ad_g: g→gl(g)` with `ad=Lie(Ad)`). Not free `lie_algebra(G)` on bare matrix group — `G.lie_algebra()` on the `LieGroups`/`GrpSch` object with `Mat_{n×n}` as `Lie(GL_n)`.

## Desired capability: group cohomology pairings via composition morphisms, Zariski tangent of character varieties as group cohomology — note 2026-09-15

Use composition morphisms to define pairings in group cohomology. Identify Zariski tangent space of character varieties with group cohomology per Goldman / https://www.math.umd.edu/~wmg/SymplecticNature.pdf.

* Pairings in group cohomology via composition morphisms: for `G : Groups` (discrete, finitely presented `G=⟨S|R⟩`, profinite, Lie) and `M,N,P : ZZ[G]-Mod` (`G`-modules as `Ab` with `G`-action `ρ: G→Aut(M)`), the `Ext` description `H^n(G,M)=Ext^n_{ZZ[G]}(ZZ,M)=H^n(RHom_{ZZ[G]}(ZZ,M))` already intaken via `BarRes → RHom` in `D(ZZ[G]-Mod)`. Pairings are not ad-hoc `H^p⊗H^q→H^{p+q}` numbers; they are induced by composition of morphisms in `D`:
  - Cup product / Yoneda composition: `RHom(ZZ,M) ⊗^L RHom(ZZ,N) → RHom(ZZ, M⊗N)` via `Hom_{ZZ[G]}(P_•,M) ⊗ Hom_{ZZ[G]}(P_•,N) → Hom_{ZZ[G]}(P_•, M⊗N)` using Alexander-Whitney `P_• → P_•⊗P_•` on bar `B_•(G)=ZZ[G^{n+1}]` (coalgebra diagonal) and tensor `M⊗N` with diagonal `G`-action `g·(m⊗n)=gm⊗gn`; on cochains ` (f∪g)(g_1,…,g_{p+q}) = f(g_1,…,g_p) ⊗ g_{p+1}·g(g_{p+1},…,g_{p+q})` etc., giving `∪: H^p(G,M)⊗H^q(G,N)→H^{p+q}(G,M⊗N)`.
  - Composition `Ext^p(B,C)⊗Ext^q(A,B)→Ext^{p+q}(A,C)` as Yoneda splice `ξ∘η = ξ[ q]∘η` in `D`; for `A=B=C=ZZ` with coefficients, this is same `∪`.
  - Internal Hom composition `Hom(M,N)⊗Hom(L,M)→Hom(L,N)` induces `RHom` composition `RHom(M,N)⊗^L RHom(L,M)→RHom(L,N)` and on `H^0` the `Ext` pairing `Ext^p⊗Ext^q→Ext^{p+q}`.
  Interface `G.cohomology_pairing(p,q,M,N)` / `M.cup_product(N)` as morphism `H^p(G,M)⊗H^q(G,N)→H^{p+q}(G,M⊗N)` via `BarRes` `∪` with `M⊗N` diagonal, delegating to `Ext` composition already in `D`.

* Zariski tangent of character varieties / Betti moduli as `H^1`: for `π : Groups` finitely presented (`π=π_1(X,x)` etc., `π=⟨S|R⟩` via `Framed` already) and `G : AlgGroups` / `LieGroups` reductive (`GL_n, SL_n, PGL_n, Sp_{2n}, O_n, G_2` etc.) with representation scheme `Rep(π,G)=Hom_{Groups}(π,G) ⊂ G^S` cut by `r((g_s))=1 ∀r∈R`, point `ρ: π→G` i.e. `ρ ∈ Rep(π,G)(k)` as object `ρ: Hom(π,G)`, and character variety `X(π,G)=Rep(π,G)//G : Sch/k` `GIT` quotient by conjugation already intaken. The Zariski tangent at `ρ` is
  ```
  T_ρ Rep(π,G) ≅ Z^1(π, g_{Ad∘ρ})  (1-cocycles u: π→g, u(gh)=u(g)+Ad_{ρ(g)}u(h))
  T_ρ (G·ρ)    ≅ B^1(π, g_{Ad∘ρ})  (1-coboundaries u(g)=Ad_{ρ(g)}X - X for X∈g)
  T_{[ρ]} X(π,G) ≅ H^1(π, g_{Ad∘ρ}) = Z^1/B^1    when ρ has closed orbit / stable (and ≅ H^1 at smooth points)
  ```
  where `g_{Ad∘ρ} : π-Mod` is `g = Lie(G)` as `π`-module via `π →^{ρ} G →^{Ad_G} GL(g)`, i.e. `Ad∘ρ: π→GL(g)` (`Ad_G` already above). For `G` algebraic over `k` char 0, this is Goldman's theorem: `T_{[ρ]} M_B(X,G) ≅ H^1(π_1(X), g_{Ad∘ρ})` as `k`-vector space, with symplectic form `ω_{Goldman}` on `H^1` via cup `∪` above composed with invariant pairing `B: g⊗g→k` (`B(X,Y)=tr(ad_X ad_Y)` Killing) and Poincaré `H^1⊗H^1 → H^2(π, k) ≅ k` when `X` surface (Theorem 1.1 of https://www.math.umd.edu/~wmg/SymplecticNature.pdf). Need `ρ.adjoint_module() → g_{Ad∘ρ} : π-Mod` (as `ZZ[π]-Mod` via `Ad∘ρ`) already via `Rep`, then `H^1(π, g_{Ad∘ρ})` via group cohomology `H^1(G,M)` already intaken (`BarRes→Ext`). Interface `ρ.zariski_tangent() → H^1(π, g_{Ad∘ρ}) : Vect_k`, `ρ.cocycles() → Z^1`, `ρ.coboundaries() → B^1`, and `X(π,G).tangent_at([ρ]) → H^1` with Goldman symplectic `H^1⊗H^1 → H^2 → k` via `∪` + `B`.

Intended owners: `categories/group/cohomology.py` (`cup_product` / `yoneda_product` `H^p⊗H^q→H^{p+q}` via `Hom⊗Hom→Hom` composition `∪` from `BarRes` `P_•→P_•⊗P_•` and `M⊗N` diagonal, `Ext^p⊗Ext^q→Ext^{p+q}`), `categories/representations/adjoint.py` (`Ad_G` already, `Ad∘ρ` as `π`-module `g_{Ad∘ρ}` via `ρ:π→G`), `categories/moduli/character_varieties.py` (`Rep(π,G) ⊂ G^S`, `X(π,G)=Rep//G`, `ρ.zariski_tangent() → Z^1/B^1 = H^1(π,g_{Ad∘ρ})` with `Goldman symplectic` via cup+B). Not free `tangent_space(ρ)` number — `ρ.zariski_tangent()` as `H^1` group cohomology with `g_{Ad∘ρ}` coefficients via `BarRes` and Yoneda `∪`.

## Desired capability: de Rham cohomology with coefficients in a flat vector bundle / local system (Bott & Tu), honest K(G,n) — note 2026-09-15

Honest constructions of `K(G,n)` spaces, at least for `n=1` and common groups `G` where e.g. `K(G,1)≅BG`; obtain higher `K` spaces by loops/suspension/etc. Plus de Rham cohomology with coefficients in flat vector bundles and cohomology with coefficients in local systems, following Bott & Tu.

* de Rham cohomology with coefficients in a flat vector bundle: for `X : Man` smooth manifold (or `X : SmSch/k` with `k=RR,CC`) and `(E,∇)` flat vector bundle `E : VecBun(X)` rank `r` with `∇: E→E⊗Ω^1_X` flat `F_∇=∇^2=0 : E→E⊗Ω^2` (i.e. `(E,∇): FlatConn(X)` already intaken), the twisted de Rham complex is
  ```
  Ω^*(X;E,∇) = ( Γ(X, E⊗Ω^*_X), d_∇ )
  ```
  with `d_∇: E⊗Ω^q → E⊗Ω^{q+1}` defined in trivialization `∇=d+A` by `d_∇(s⊗ω)=∇(s)∧ω + s⊗dω = ds⊗ω + s⊗dω + A∧s⊗ω`, satisfying `d_∇^2 = F_∇∧- =0` iff `∇` flat. Then `H^*_{dR}(X;E,∇) = H^*(Ω^*(X;E), d_∇) : GrMod` as graded module `⊕_q H^q_{dR}(X;∇)`. For trivial `∇=d` this is `H^*_{dR}(X)⊗E_x`. Flatness is the condition for `d_∇` to be a complex; without it `d_∇^2≠0` and cohomology is not defined. Interface `∇.de_rham_complex() → Ω^*(X;E) : Ch` with `d_∇`, and `∇.de_rham_cohomology(q) → H^q_{dR}(X;∇) : Vect` as `H^q` of that `Ch`, with `∇.is_flat()` gate `F_∇==0` already.

* Cohomology with coefficients in a local system following Bott & Tu: for `L : LocSys(X)` locally constant sheaf of `k`-vector spaces (`L : Sh(X^{an})` with `L|_{U_α}≅k^{r}`), with equivalence `LocSys(X^{an}) ≃ FlatConn^{rs}(X)` via Riemann-Hilbert already intaken (`L = ker ∇` as `C`-local system, `E = L⊗O^{an}`), the cohomology with local coefficients is sheaf cohomology `H^*(X;L) = RΓ(X,L) = H^*(X^{an}, L) : GrMod` (`RΓ = R(p_*)` from six functors). For manifold `X` with good cover `U={U_α}` (finite open cover with all `U_{α_0…α_p}` contractible), Bott & Tu compute it via Čech-de Rham double complex `K^{p,q}= Č^p(U, Ω^q⊗L)` / `C^p(U)⊗L` with `D = d_∇ + δ_Č` and `H^*(X;L) ≅ H^*(Tot(K), D)`. De Rham theorem with local coefficients is the quasi-isomorphism `L → Ω^*(X;E,∇)` as resolution `0→L→E →^{∇} E⊗Ω^1 →^{d_∇} …`, giving `H^*_{dR}(X;∇) ≅ H^*(X^{an};L)` as `GrMod` isomorphism natural in `(E,∇)`. Interface `L.cohomology(q) → H^q(X;L)` via `RΓ`, and `∇.de_rham_cohomology(q) ≅ L.cohomology(q)` comparison as isomorphism in `Vect`, with Bott & Tu `Čech-de Rham` as effective `Tot` when `U` finite good cover (reuse `EffHom` Čech already intaken). Not free `local_system_cohomology(L)` number — `L.cohomology()` on the `LocSys` object and `∇.de_rham_cohomology()` on `FlatConn` with comparison `∇.local_system().cohomology() ≅ ∇.de_rham_cohomology()`.

* Honest `K(G,n)` spaces: for `G : Groups` (abelian when `n≥2`, arbitrary when `n=1`) `K(G,n) : HoTop` is Eilenberg-MacLane with `π_n(K(G,n))=G`, `π_{≠n}=0`. At least for `n=1` and common `G` where `K(G,1)≅BG`: `K(G,1)=BG` for any discrete `G` via `BG = B G = |W̄(N G)|` already intaken as classifying space `G.classifying_space() → BG : HoTop` with `ΩBG≃G`, `EG→BG`. Common groups include `G = Z, Z/n, Z/2, S_n, B_n, F_n, π_1 Σ_g, GL_n(Z)` etc. with already intaken concrete `BG` models `RP^∞=B(Z/2)`, `CP^∞=B(Z)=K(Z,2)` no — `CP^∞=K(Z,2)` is `n=2`, `L_p^∞=B(Z/p)`, `Gr_n(C^∞)=B U(n)` not `K`, `BF_n=∨^n S^1 =K(F_n,1)` etc. So `K(G,1)` owner reuses `ClassifyingSpace` already: `K(G,1) := BG`.
  Higher `K(G,n)` obtained by loops/suspension/delooping:
  - Looping: `ΩK(G,n) ≃ K(G,n-1)` as `HoTop` (`Ω` already intaken via `G ⊣ W̄` loop `Ω = G` simplicial or `Map_*(S^1,-)`), so `K(G,n-1) = ΩK(G,n)` when `K(G,n)` already has `EC` effective (Kenzo `loop-space`).
  - Suspension/delooping: `K(G,n) ≃ B K(G,n-1)` as classifying space of the simplicial abelian group `K(G,n-1)`, i.e. `K(G,n)=W̄ K(G,n-1)` via bar `B = W̄` already intaken (`Bar`/`W̄`), inductively `K(G,n)=B^n G` as `n`-fold delooping `B^n(K(G,0))` with `K(G,0)=G` discrete, `K(Z,n)` via `B^n Z`.
  - Equivalently via Dold-Kan: `K(G,n)` as `Γ( G[n] )` where `G[n]` is chain complex with `G` in degree `n`, via `DK: Ch_{\geq0}(Ab) → sAb → sSet` forgetting to `sSet`.
  Interface `EilenbergMacLane(G,n) → K(G,n) : HoTop` with `K(G,1)=BG` reuse, and `K(G,n).loop_space() → K(G,n-1)`, `K(G,n).delooping() → K(G,n+1) = B K(G,n)`, and `ΩK(G,n) ≅ K(G,n-1)` as natural isomorphism in `HoTop` with `π_*` verification `π_n(K(G,n))=G` via effective homology `EC(K(G,n))`.

Intended owners: `categories/de_rham/de_rham_coeff.py` (`FlatConn.de_rham_complex() → Ω^*(E,∇)` with `d_∇`, `H^*_{dR}(∇)`), `categories/sheaves/local_systems.py` (`LocalSystem.cohomology() → H^*(X;L)=RΓ(L)` with Bott & Tu `Čech-de Rham Tot` and comparison `H^*_{dR}(∇)≅H^*(L)`), `categories/topology/eilenberg_maclane.py` (`K(G,n)=B^n G` with `ΩK(G,n)≃K(G,n-1)` via `B=W̄`/`Ω=G`, `K(G,1)=BG` reusing `ClassifyingSpace`, Dold-Kan `Γ(G[n])`), delegating to `categories/topology/classifying_spaces.py` (`BG`), `categories/topology/simplicial_sets.py` (`Ω`, `W̄`), `categories/topology/effective_homology.py` (`EC` for `K(G,n)`). Not free `k_g_n(G,n)` — `EilenbergMacLane(G,n)` on the group object with `K(G,1)=G.classifying_space()` reuse.

## Desired capability: modular forms, automorphic forms, factors of automorphy, automorphic bundles — note 2026-09-16

Need symbolic modular forms, automorphic forms, factors of automorphy, and associated automorphic bundles when explicit and computable.

* Modular form is not a `q`-series alone. For `Γ ≤ SL_2(RR)` Fuchsian (e.g. `Γ=SL_2(ZZ)`, `Γ(N),Γ_1(N),Γ_0(N)`) and weight `k : ZZ` (or `k∈½ZZ` with multiplier), `f: HH→C` holomorphic with `f(γz)=j(γ,z)^k f(z)` for `j: Γ×HH→C^×` factor of automorphy `j(γ,z)=cz+d` (`γ=(a b;c d)`) and `j(γ_1γ_2,z)=j(γ_1,γ_2z)j(γ_2,z)` cocycle, plus holomorphy at cusps `f|_k γ` bounded as `Im z→∞`. Interface must be `ModularForm(Γ,k,j)` as section `f : HH→C` with `f.automorphy_factor()→j` and `f.slash(k,γ)`; `f` is object with parent `M_k(Γ)`. `q`-expansion `f(z)=Σ_{n≥0} a_n q^n`, `q=e^{2πiz}`, is `FormalPowerSeries` coefficient view `f.q_expansion() → Σa_n q^n : R[[q]]`, not the definition.

* Factor of automorphy is not a function `j(z)`. For `Γ` acting on `HH` via `γ·z=(az+b)/(cz+d)`, a factor is `j: Γ×HH→GL(V)` holomorphic with cocycle `j(γ_1γ_2,z)=j(γ_1,γ_2z)j(γ_2,z)`; weight `k` is `j_k(γ,z)=(cz+d)^k`, Nebentypus `χ` is `j_{k,χ}=χ(d)(cz+d)^k`. Symbolic factors means `j` as object `FactorOfAutomorphy(Γ,HH,V)` with `j.cocycle(γ_1,γ_2,z)` test, not a bare exponent `k`. Composition of factors `j_1⊗j_2` is tensor of `GL` representations.

* Automorphic form generalization: for `G` reductive `G=SL_2, Sp_{2g}, U(p,q), GL_n` with symmetric space `X=G/K` (`HH=SL_2(RR)/SO(2)`), `Γ⊂G(Q)` arithmetic, `j: Γ×X→GL(V)` factor as above, automorphic form is `F: G→C` with `F(γg)=j(γ,g·o)F(g)`, `F(gk)=σ(k)^{-1}F(g)` for `K`-type `σ`, plus growth/K-finiteness. When `G=SL_2`, this specializes to `f` via `F(g)=j(g,o)^{-k} f(g·o)`. Interface `AutomorphicForm(G,Γ,j,σ)` on the group `G`, not just `HH`.

* Associated automorphic bundle is not a `VecBun` with no `Γ`. For `j: Γ×HH→GL(V)` factor, bundle is `V_j = (HH×V)/Γ` where `Γ` acts by `γ·(z,v)=(γz, j(γ,z)v)` as `VecBun` over `X(Γ)=Γ\HH` (or `Γ\G/K` generally), with `Γ(HH,V_j) ≅ {f: HH→V | f(γz)=j(γ,z)f(z)}` modular forms as `H^0(X(Γ),V_j)`. When `j=j_k`, `V_j = ω^{⊗k}` power of Hodge bundle `ω = e^*Ω^1_{E/X(Γ)}` for universal elliptic `E→X(Γ)`. Explicit and computable means transition `j` on good cover `U_α⊂X(Γ)` computable via `cz+d`, with `V_j|_{U_α}≅O_{U_α}⊗V`. Interface `AutomorphicBundle(Γ,j) → V_j : VecBun(X(Γ))` with `V_j.sections() = M(Γ,j)`; `ModularForms` app is `X(Γ).automorphic_bundle(j).global_sections()`.

Intended owners: `categories/modular/forms.py` (`ModularForm(Γ,k)` with `f(γz)=j(γ,z)^k f(z)`, `q_expansion`), `categories/automorphic/forms.py` (`AutomorphicForm(G,Γ,j)`), `categories/automorphic/factors.py` (`FactorOfAutomorphy` with cocycle `j(γ_1γ_2,z)=j(γ_1,γ_2z)j(γ_2,z)`), `categories/automorphic/bundles.py` (`AutomorphicBundle V_j=(HH×V)/Γ : VecBun(X(Γ))` with `H^0 = M(Γ,j)`). Not a free `modular_form(q_series)` — `M_k(Γ).element(q_series)` with automorphy `j` retained.

## Desired capability: spaces of modular forms, bases, Eisenstein, q-expansions, containment and sampling — note 2026-09-16

Need `M_k(Γ)` spaces, computable dimensions/bases (Eisenstein), `q`-expansions, weight/level extraction, and ability to express a given form via basis through sampling, plus containment testing.

* Space `M_k(Γ) : Vect` (over `Q`, `QQbar`, `C`) is not a Python `list` of `q`-series. For `Γ≤SL_2(ZZ)` congruence (`Γ(N),Γ_1(N),Γ_0(N)`) or general finite-index Fuchsian, `M_k(Γ) = {f: HH→C | f|_k γ = f ∀γ∈Γ, holomorphic at cusps}` as `Vect` with `M_k(Γ)⊂O(HH)`, graded ring `M_*(Γ)=⊕_k M_k(Γ)` with multiplication `M_k⊗M_ℓ→M_{k+ℓ}` (`f·g`), filtration by order at cusps `S_k⊂M_k` cuspidal (`a_0=0` at all cusps). Similarly `AutomorphicForms(G,Γ,j)` as `Vect`. Interface `Gamma.modular_forms(k) → M_k(Γ) : Vect` and `M_k(Γ).dimension() → dim : NN` via genus formula / Riemann-Roch / trace (see modular curves below), basis `M_k(Γ).basis() → [b_i : M_k]`.

* Dimensions when known: `dim M_k(SL_2(ZZ))` via `k≡0 mod4` etc., `dim M_k(Γ_0(N))`, `dim S_k` via `Riemann-Roch` on `X(Γ)`: `M_k(Γ) ≅ H^0(X(Γ), ω^{⊗k}⊗O(…cusps…))` with `ω` Hodge, `dim = deg(ω^{⊗k})+1-g + h^1` via `RR` / `Hirzebruch-RR` already intaken, plus trace formula `Eichler-Selberg`. Not enumerated by brute enumeration of `q`-series.

* Bases when known, e.g. Eisenstein series: `E_k(z)= ½ζ(1-k)^{-1} Σ_{(c,d)=1} (cz+d)^{-k} = 1 - (2k/B_k) Σ_{n≥1} σ_{k-1}(n)q^n` for even `k≥4`, `E_k∈M_k(SL_2(ZZ))` (normalized `E_4, E_6` generate `M_*=C[E_4,E_6]`), `E_k^{χ,ψ}` with characters (`χψ(-1)=(-1)^k`) level `N`, `E_k(N)∈M_k(Γ_0(N))`, oldforms `E_k(dz)`. Symbolic formulas and series: `E_k.q_expansion(N_terms) → Σ_{n<N} a_n q^n` as `R[[q]]` truncated image of `R[[q]]=lim R[q]/(q^N)` already intaken. Interface `EisensteinSeries(k) → E_k : M_k`, `EisensteinSeries(k,N,χ) → E_{k,χ}`, with `E_k.q_expansion()` via `σ_{k-1}` divisor sum (not numeric guess).

* Weight and level extraction: for `f ∈ O(HH)` presented as `q`-series or function, `f.weight()` asks `k` with `f|_k γ =j(γ,z)^{-k}f(γz)` testing `k∈ZZ`, `f.level() → N : NN` minimal `N` with `f∈M_k(Γ_0(N)) ∩ …` (or `Γ_1(N)`, `Γ(N)`) via Sturm bound test `f|_k γ = f` on generators of `Γ(N)`. Returns `k : ZZ`, `N : NN` (or `Unknown` when not modular/automorphic), with certificate via generators `S=(0 -1;1 0)`, `T=(1 1;0 1)` etc., not by string tag.

* Containment testing `is_modular`, maybe discovering modularity/automorphicity/quasi-modularity by search: given `f : HH→C` or `F : FormalPowerSeries` (`Σ a_n q^n`), predicate `f ∈ M_k(Γ)` is tested via `f.slash(k,γ) == f` on generating set `gens(Γ) ⊂ SL_2(ZZ)` (`S,T` plus `Γ_0(N)` coset reps) up to Sturm bound, plus cusp holomorphy (`a_n=0` for `n<0` in each `f|_k α`, `α∈SL_2(ZZ)`). Discovery/search means when weight/level unknown, enumerate candidate `(k,N)` bounded by conductor estimates (`k≤K_max`, `N|N_max`) and test `f∈M_k(Γ_0(N))` via equality in `R[[q]]/(q^{Sturm(N,k)})`, returning minimal `(k,N)` with success or `Unknown`. Quasi-modular `E_2` is `f|_2 γ = f + (6/πi) c/(cz+d)` as extension `QMod = M_* ⊕ M_*·E_2 ⊕ …` with derivation `D=q d/dq` (Ramanujan). Interface `f.is_modular(Γ,k) → Bool` with witness `Sturm` bound, `f.find_level(K_max,N_max) → (k,N)` / `Unknown`, `f.is_quasimodular() → (M_{k-2} component)` via `E_2`.

* Expressing a given form as linear combination of basis forms via pointwise / `q`-coefficient evaluations: for known `M_k(Γ)` with `d=dim M_k` basis `[b_i]_{i<d} : GrMod` and `f∈M_k(Γ)`, there exist `c_i ∈ k` with `f = Σ c_i b_i` unique. Determining how many evaluations are needed: Sturm bound `Sturm(k,Γ)` (`k·[SL_2(ZZ):Γ]/12` etc.) is `N_0` such that `a_n(b_i)` for `n<N_0` determines `f`, i.e. `N_0 = dim M_k(Γ)`-many `q`-coefficients suffice generically, more precisely `N_0 = Sturm(k,Γ)` guarantees equality as `R[[q]]` elements; pointwise `f(z_j)` at `d` generic `z_j∈HH` with `z_i≠z_j` gives Vandermonde `V_{j,i}=b_i(z_j)` invertible for Zariski-generic `z_j`. Interface `M_k(Γ).coordinates(f) → (c_i)` via linear solve `V·c = [f(z_j)]` or `A·c = [a_n(f)]` where `A_{n,i}=a_n(b_i) ∈ Mat_{N_0×d}`, communicating required count: `M_k(Γ).sturm_bound() → N_0 : NN`, `M_k(Γ).num_evaluations_needed() → d : NN`, and method `f.as_linear_combination()` returns `[c_i]` with certificate `Sturm` or condition number of `V`. Search/discovery variant uses same bound to certify modularity.

Intended owners: `categories/modular/spaces.py` (`M_k(Γ) : Vect` with `dimension` via `RR` on `X(Γ)`, `basis` with `Eisenstein`+`cusp`), `categories/modular/eisenstein.py` (`E_k, E_{k,χ} → M_k` with `σ_{k-1}` q-expansion `Σa_n q^n`), `categories/modular/q_expansions.py` (`q_expansion : R[[q]]` via `R[[q]]=lim R[q]/(q^n)`), `categories/modular/containment.py` (`is_modular`, `find_level`, `is_quasimodular`, `Sturm`), `categories/rings/formal_power_series.py` (`R[[q]]` `(q)`-adic). Not a free `is_modular_series(series)` number — `M_k(Γ).contains(f)` with `Sturm` and `f ∈ M_k(Γ)` as sections of `V_{j_k}`.

## Desired capability: congruence subgroups, arithmetic subgroups, modular curves and their invariants, fundamental domains — note 2026-09-16

Need congruence subgroups and arithmetic subgroups as first-class objects, geometric models of modular curves of various levels with algebro-geometric invariants, and real fundamental domains as Euclidean/spherical/hyperbolic polytopes with visualization in low dimensions.

* Congruence subgroups as first-class objects: for `N : NN`, `Γ(N)=ker(π_N: SL_2(ZZ)→SL_2(ZZ/N))` principal, `Γ_1(N)={ (a b;c d)∈SL_2(ZZ) | a≡d≡1, c≡0 mod N}`, `Γ_0(N)={c≡0 mod N}`, and `Γ(N)⊲Γ_1(N)⊲Γ_0(N)⊲SL_2(ZZ)` with indices `[SL_2(ZZ):Γ(N)]=N^3∏_{p|N}(1-1/p^2)`, `[SL_2:Γ_0]=N∏_{p|N}(1+1/p)`. Object `Γ : CongruenceSubgroups` with `Γ.level()→N`, `Γ.index()→[SL_2:Γ]`, `Γ.generators()→[S,T,…]` finite generating set, `Γ.cusps()→P^1(Q)/Γ` coset enumeration, `Γ.coset_reps()→ SL_2(ZZ)/Γ`, membership `γ∈Γ` decidable via `γ mod N`. Interface `Gamma0(N)`, `Gamma1(N)`, `Gamma(N)` constructors as `Subgroups(SL_2(ZZ))` with `Sub(G)` lattice, not bare integers `N`.

* Arithmetic subgroups in general: for semisimple `G/Q` (e.g. `SL_2, Sp_{2g}, SL_n, U(p,q), SO(p,q)`), `G(ZZ)=G∩GL_n(ZZ)` and `Γ⊂G(Q)` commensurable with `G(ZZ)` (finite index in `G(ZZ)∩gG(ZZ)g^{-1}`) as `ArithmeticSubgroups(G) : Sub(G(Q))` with `Γ` neat/cofinite, `Γ\G/K` finite volume. Includes `SL_2(ZZ)`, `Γ⊂Sp_{2g}(ZZ)` Siegel, `SL_n(ZZ)`, Bianchi `SL_2(O_K)` for imaginary quadratic `K` acting on `HH^3`. Interface `ArithmeticSubgroup(G, level)` with `Γ.ambient_group()→G`, `Γ.congruence_closure()`, `Γ.is_congruence() → Bool` (congruence subgroup problem), commensurator.

* Geometric models of modular curves of various levels: for `Γ` as above, `Y(Γ)=Γ\HH : RiemannSurface` (orbifold when `-I∈Γ` elliptic points) and compactified `X(Γ)=Γ\HH^*` with `HH^*=HH∪P^1(Q)` adding cusps `C_Γ=P^1(Q)/Γ` finite set, as smooth projective curve `X(Γ) : Curve/Q` (canonical model over `Q` via `j` and `j_N`, over `ZZ[1/N]` integral model). Concrete models: `X(1)=P^1_j` via `j`, `X_0(N)=Γ_0(N)\HH^*` via `q`-expansion at `∞`, `X_1(N)`, `X(N)` via `Tate` / `Katz-Mazur` moduli `E→S` elliptic with level structure `α: (ZZ/N)^2 ≃ E[N]` etc. `X(N)` moduli functor `F_N(S)={E/S with α}` representable by `X(N)` when `N≥3`. Interface `ModularCurve(Gamma) → X(Γ) : SmoothProjectiveCurve` with `X(Γ)(C) ≅ Γ\HH^*` as `AnSpaces`, `X(Γ).integral_model()` over `ZZ[1/N]` when `Γ=Γ(N)`.

* Algebro-geometric invariants, known algorithms and formulas: `genus g(X(Γ)) = 1 + [SL_2:Γ]/12 - e_2/4 - e_3/3 - c/2` with `e_2,e_3` elliptic points, `c=|C_Γ|` cusps (for `Γ⊂SL_2(ZZ)`; general via Riemann-Hurwitz `X(Γ)→X(1)=P^1`). For `Γ_0(N)`, explicit `g(N)=1+μ(N)/12 - ν_2/4 - ν_3/3 - ν_∞/2` with `μ=[SL_2:Γ_0]`, `ν_2,ν_3,ν_∞` via divisor counts of `N`. Arithmetic genus `p_a` vs geometric `p_g=g` (smooth), `Hodge` `h^{1,0}=g`, `h^{0,1}=g`, `H^1≅H^0(Ω^1)⊕\overline{H^0(Ω^1)}`, `canonical K_{X}= (2g-2)·pt` divisor class with `deg K=2g-2`, `H^0(K)=H^0(Ω^1)` dimension `g`, etc., via `Riemann-Roch` `χ(O(D))=deg D+1-g`. Algorithms: `X.genus()`, `X.hodge_numbers()`, `X.canonical_divisor()`, `X.cusp_divisor()`, `X.elliptic_points()` from `Γ` coset/elliptic enumeration (Sage `Gamma0(N).genus()` etc. as private adapter).

* Real fundamental domains as subsets of other first-class spaces, e.g. Euclidean/spherical/hyperbolic polytopes: for `Γ` Fuchsian acting on `HH` (`HH^2` hyperbolic plane `ds^2=(dx^2+dy^2)/y^2`, curvature `-1`) or `SL_2(O_K)` on `HH^3 = C×R_{>0}` (`ds^2=(|dz|^2+dt^2)/t^2`), Kleinian, etc., a fundamental domain `F_Γ⊂HH^n` is `closure{ z | d(z,p_0) ≤ d(γz,p_0) ∀γ≠1}` Dirichlet (`p_0∈HH^n` not fixed by `Γ\{1}`) or Ford `F={z | |cz+d|≥1 ∀(c d)}` for `Γ⊂SL_2(ZZ)`. `F_Γ` is `HyperbolicPolytope` in `HH^n` as finite-sided convex polytope with geodesic sides (circular arcs in `HH^2`, hemispheres in `HH^3`), side-pairings `γ_s: s→s'` with `γ_s∈Γ` and cycle relations `∏γ_{s_i}=1`. For `SL_2(ZZ)`, `F={|Re z|≤½, |z|≥1}` standard. For `Γ_0(N)`, `F_{Γ_0}` is `[SL_2:Γ_0]`-fold union of `F_{SL_2}` translates via coset reps.

* Visualization in low dimensions (`HH^2, HH^3`): `F_Γ : HyperbolicPolytope` as subset `F_Γ⊂HH^n` with `F_Γ.sides()→[geodesic]`, `F_Γ.side_pairings()→Γ`, and `F_Γ.visualize() → InteractivePolytope` widget bound to `F_Γ` (reuse `SpectralSequence.visualize` pattern) rendering in `HH^2` Poincaré disk / upper half-plane with arcs, and in `HH^3` via `H^3` upper half-space with hemispherical faces, using hyperbolic isometry `PSL_2(R)` / `PSL_2(C)` private adapter (Sage `HyperbolicPlane`, `HyperbolicSpace(3)`). Not a free `plot_fundamental_domain(Gamma)` PNG — `F_Γ = Gamma.fundamental_domain(p0) : HyperbolicPolytope` in `HH^n` with `F_Γ.as_subset(HH^n)` and `F_Γ.show()`.

Intended owners: `categories/modular/congruence_subgroups.py` (`Gamma(N),Gamma1(N),Gamma0(N) : Sub(SL_2(ZZ))` with `level,index,generators,cusps`), `categories/groups/arithmetic_subgroups.py` (`ArithmeticSubgroup(G) ⊂ G(Q)` commensurable with `G(ZZ)`), `categories/modular/modular_curves.py` (`X(Gamma)=Gamma\HH^* : Curve/Q` with `Y(Gamma)=Gamma\HH` open, integral model, moduli `F_N`), `categories/schemes/curve_genus.py` (`genus`, `hodge_numbers`, `canonical`, `RiemannHurwitz`), `categories/modular/fundamental_domains.py` (`FundamentalDomain Gamma→F_Γ⊂HH^n` as `HyperbolicPolytope` with side-pairings), `categories/hyperbolic/polytopes.py` + `categories/hyperbolic/visualization.py` (`HyperbolicPolytope` `F_Γ.visualize()` in `HH^2,HH^3`). Not a free `fundamental_domain(Gamma)` list — `Gamma.fundamental_domain()` as polytope object in `HH^n` with `HH^n` owning the metric.

## Desired capability: del Pezzo, Hirzebruch, common surfaces; toric surfaces classification and Fulton — note 2026-09-16

Need del Pezzo, Hirzebruch, and other common algebraic surfaces; lattice cones/polytopes wired to honest lattices; character/cocharacter lattices as preamble lattices; classification of toric surfaces with recognition; all of Fulton *Introduction to toric varieties* operationalized.

* Common surfaces: `Hirzebruch F_e = P(O_{P^1}⊕O_{P^1}(-e)) : Surfaces/k` for `e : NN`, `Pic(F_e)=ZZ·C_0 ⊕ ZZ·f` with `C_0^2=-e`, `f^2=0`, `C_0·f=1`, `K_{F_e}=-2C_0-(e+2)f`, `(-1)`-curves etc.; `del Pezzo dP_n = Bl_{p_1…p_n} P^2` `0≤n≤8` with `p_i` in general position (no 3 collinear, no 6 on conic), `K_{dP_n}^2=9-n`, degree `d=9-n`, `Pic(dP_n)=ZZ·H ⊕⊕_{i}ZZ·E_i` with `H^2=1`, `E_i^2=-1`, `K=-3H+ΣE_i`, `(-1)`-curves = `240,27,16…` Weyl orbit `W(E_n)`. `P^1×P^1 = F_0`, `Bl_p P^2 = F_1` etc., plus `K3` (`K=0`), `Enriques`, rational/ruled. Interface `Hirzebruch(e) → F_e : Surfaces`, `DelPezzo(n, points) → dP_n : Surfaces` with `dP_n.picard_lattice()→Pic≅Lattices`, `dP_n.minus_one_curves()→[C]`, not bare self-intersection numbers.

* Classification of toric surfaces and recognition: smooth complete toric surface `S_Σ` from fan `Σ⊂N_R` `dim N_R=2` with `Σ` complete (`|Σ|=N_R`), `Σ` smooth iff each cone `σ=cone(v_i,v_{i+1})` has `det(v_i,v_{i+1})=±1` (`v_i∈N` primitive). `S_Σ` determined by cyclic ordered rays `v_0…v_{r-1}∈N` with `v_{i+r}=v_i`, relation `v_{i-1}+v_{i+1}=a_i v_i` with `a_i = -D_i^2 = -self-intersection` of torus-invariant divisor `D_i = V(v_i) ≅ P^1`. Isomorphism type recognition: toric surface is either `P^2` (`r=3`) or `F_e` or blow-up of `F_e` (iterated toric blow-up adding ray `v_i+v_{i+1}` subdividing cone). Algorithm: from `S : Surfaces/k` smooth complete, test if `S` toric via `Cox ring` / `T-invariant divisor` basis, and if so compute `Σ(S)` by `N=X_*(T)` and rays = primitive generators of `T`-invariant prime divisors (`D_ρ`), then match cyclic `v_i` sequence up to `GL_2(ZZ)` (`Aut(N)`) to recognize as `F_e` / `Bl` / `P^2`.

* Character and cocharacter lattices as preamble-owned lattices: for split torus `T≅G_m^r : Tori/k`, `X^*(T)=Hom_{GrpSch}(T,G_m) ≅ ZZ^r` character lattice, `X_*(T)=Hom(G_m,T) ≅ ZZ^r` cocharacter lattice, both as `Lattices` objects `X^*,X_* : Lattices` (`Str Lattices` even unimodular `ZZ^r` with standard pairing `X^*×X_*→ZZ`, `(χ,λ)↦χ∘λ ∈ Hom(G_m,G_m)=ZZ`), anti-equivalence `T↦X^*(T) : Tori → Lattices^{op}` (`T≅Spec k[X^*(T)]`). Interface `T.character_lattice() → X^*(T) : Lattices` and `T.cocharacter_lattice() → X_*(T) : Lattices` as honest `Lattices` (with `Lattices.gram_matrix` etc.), not as bare `ZZ^r` vectors; pairing `X^*(T).pairing(X_*(T))→ZZ` as `BilinearForm`. Already `categories/group/characters.py` owns `X^*(T)` as group, but `Lattices` owner supplies lattice structure (`X^*(T).as_lattice()` returns same object with `Lattices` refinement).

* Lattice cones and polytopes as independent constructions wired to honest preamble lattices: cone `σ⊂N_R=N⊗R` strongly convex rational polyhedral `σ=cone(v_i)`, `v_i∈N`, with `σ∩N` monoid `S_σ`, `σ^∨⊂M_R` dual `σ^∨={u∈M_R | ⟨u,v⟩≥0 ∀v∈σ}` with `M=X^*(T)`, `N=X_*(T)` dual lattices; polytope `P⊂M_R` lattice polytope `P=conv(m_i)`, `m_i∈M`, with vertices `vert(P)⊂M`, faces `face(P)` as `LatticePolytope` with `P⊂M_R` retaining `M : Lattices` as ambient, normal fan `Σ_P⊂N_R`. Both are independent first-class objects `LatticeCone(N, rays)` and `LatticePolytope(M, vertices)` with `σ.ambient_lattice()→N`, `P.ambient_lattice()→M`, `σ.dual()→σ^∨⊂M_R`, `P.normal_fan()→Σ⊂N_R`, `P.face_lattice()→Poset`. Wired into honest `Lattices`: no `σ.ambient` stored as bare `ZZ^2` matrix but as `Lattices` object with `N.dual() = M`. Reuse `polyhedral_cones.RationalPolyhedralCones` and `schemes/polytopes.py` as adapters for `SageCone` / `Polyhedron` private engines, but public objects retain `N,M : Lattices`. Interface `LatticeCone(N, [v_i]) → σ⊂N_R` with `σ.dual_cone()→σ^∨`, `LatticePolytope(M, [m_i]) → P` with `P.normal_fan()`.

* Fulton operationalized — all computational results from W. Fulton *Introduction to toric varieties* as owned functors: for toric `X_Σ : ToricVarieties/k` with fan `Σ⊂N_R` already intaken via `RationalPolyhedralFans` / `ToricSchemes`, need `T`-invariant prime divisors `D_ρ = V(ρ)` for `ρ∈Σ(1)` ray with `v_ρ∈N` primitive, `T`-Weil divisor `D=Σ_{ρ} a_ρ D_ρ : WeilDiv(X_Σ)` (`a_ρ: ZZ`), `T`-Cartier via support function `ψ: |Σ|→R` piecewise linear with `ψ|_σ ∈M` and `D_ψ = -Σ ψ(v_ρ)D_ρ`; exact `0→M→⊕_{ρ} ZZ·D_ρ → Cl(X_Σ)→0` with `Cl ≅ Pic` when smooth, `0→M→⊕ ZZ·D_ρ → Pic →0`? For smooth complete, `Pic(X_Σ) ≅ ⊕ZZ·D_ρ / M` with `M→⊕` by `m↦ Σ⟨m,v_ρ⟩D_ρ`, `A^*(X_Σ)=Z[D_ρ]/(SR+linear)` Chow ring with Stanley-Reisner `SR=(∏_{ρ∈S} D_ρ | S∉Σ)` and linear `Σ⟨m,v_ρ⟩D_ρ=0`. Cohomology `H^i(X_Σ, O(D))` via Demazure vanishing / `H^i = ⊕_{m∈M} H^i_{m}` with `H^i_m = \tilde H^{i-1}(|Σ|\…)` combinatorial via `Σ_D`, `χ(O(D))` via `Ehrhart` of polytope `P_D={m | ⟨m,v_ρ⟩≥-a_ρ}` when `D` nef: `H^0(O(D))` has basis `χ^m` for `m∈P_D∩M` and `h^0=|P_D∩M|`. Need `X_Σ.divisor_class_group()`, `X_Σ.chow_ring()`, `X_Σ.cohomology(D,i)`, etc., all via `M,N` lattices.

Intended owners: `categories/schemes/surfaces/hirzebruch.py` (`Hirzebruch(e) → F_e` with `Pic=ZZ^2`), `categories/schemes/surfaces/del_pezzo.py` (`DelPezzo(n)→dP_n` with `Pic=ZZ^{n+1}`, `(-1)-curves`), `categories/schemes/surfaces/common_surfaces.py` (`P^1×P^1, K3, Enriques, rational`), `categories/schemes/toric/surfaces.py` (`ToricSurface Σ⊂N_R` smooth complete, rays `v_i∈N`), `categories/schemes/toric/classification.py` (`is_toric_surface`, `recognize_toric_surface` via `Σ` and `v_{i-1}+v_{i+1}=a_i v_i`), `categories/tori/character_lattices.py` (`T.character_lattice()→X^* : Lattices`, `T.cocharacter_lattice()→X_*`, pairing `⟨,⟩`), `categories/cones/lattice_cones.py` (`LatticeCone(N,rays) ⊂N_R` with `dual`), `categories/polytopes/lattice_polytopes.py` (`LatticePolytope(M,verts) ⊂M_R` with `normal_fan`, `face_lattice`), `categories/schemes/toric/fulton.py` (`TDivisor D_ρ`, `WeilDiv Σa_ρD_ρ`, `Cartier via ψ`, `Cl,Pic, Chow SR+linear, H^i(O(D))` via `P_D∩M`). Not a free `toric_divisor(fan)` list — `X_Σ.divisor(D_ρ)` on the `ToricVariety` with `N,M : Lattices` as dual pair.

## Desired capability: rational maps, birational maps, blowups, blowdowns, contractions — note 2026-09-16

Need support for rational maps, birational maps, resolving indeterminacy, blowups (at least along points), blowdowns, contractions of curves (at least on surfaces).

* Rational map is not a morphism with missing points ignored. For `X,Y : Sch/k` integral separated finite type, `φ: X ⇢ Y` is `U⊂X` open dense with `φ: U→Y` morphism, with `U = dom(φ)` maximal domain of definition, equivalently `φ ∈ Hom_{Sch/k}(Spec k(X), Y)` where `k(X)=Frac O_X` function field. Composition is only where domains intersect: `ψ∘φ` defined on `φ^{-1}(dom ψ)∩dom φ`. Interface `X.rational_map(Y, dom, morphism)` as object `RationalMap` with `φ.domain()→U : Open(X)` and `φ.morphism()→U→Y`.

* Birational map is not a rational map with an inverse as set map. For `X,Y` integral, `φ: X ⇢ Y` birational means `∃ψ: Y ⇢ X` with `ψ∘φ = id_X` as rational maps (equality on dense open where both defined) and `φ∘ψ=id_Y`, equivalently `k(X)≅k(Y)` as fields via `φ^*`. Group `Bir(X)=Aut_{Bir}(X)` is group of birational self-maps. Interface `X.birational_map(Y, φ, ψ)` with `φ.is_birational() → Bool` via `k(X)≅k(Y)`, `φ.inverse()` returning `ψ`.

* Resolving indeterminacy is the theorem `φ: X ⇢ Y` with `Y` proper and `X` smooth (or normal) admits `π: \tilde X→X` proper birational (sequence of blowups) with `\tilde φ = φ∘π : \tilde X→Y` morphism. At least for surfaces, resolution is by point blowups: `π = Bl_{p_r}∘…∘Bl_{p_1}` where `p_i∈X_{i-1}`. Need `φ.resolve_indeterminacy() → (π: \tilde X→X, \tilde φ: \tilde X→Y)` with `π` as `Blowup` composition and `\tilde φ` regular. Hardness is Hironaka in general; at least point case is required.

* Blowup at a point `p: Spec k→X` (closed point, `X` smooth of dimension `n`) is `Bl_p X = Proj ⊕_{d≥0} I_p^d : Sch/k` with `π: Bl_p X→X` proper birational, iso over `X\{p}`, exceptional `E=π^{-1}(p)≅P^{n-1}_k` with `O_E(E)=O_{P^{n-1}}(-1)`, `Pic(Bl_p X)=π^*Pic(X)⊕ZZ·E`, `K_{Bl}=π^*K_X+(n-1)E`. For surface `n=2`, `E≅P^1`, `E^2=-1`, `K·E=-1`. Interface `X.blowup(p) → (Bl_p X, π, E)` with `π: Bl_p X→X` and `E: Div(Bl_p X)`.

* Blowdown is the inverse: given `S` smooth surface with `(-1)`-curve `E⊂S`, `E≅P^1`, `E^2=-1`, Castelnuovo criterion gives `π: S→S'` with `S'=S` contracted `E↦pt` smooth, `S=Bl_{π(E)} S'`. More generally blowdown of exceptional locus of `π: \tilde X→X` recovers `X`. Interface `S.blowdown(E) → S'` when `E` is contractible, with certificate `E^2=-1` and `E≅P^1`.

* Contraction of curves on surfaces (at least): for `S : Surfaces/k` smooth projective and `C⊂S` curve (effective divisor `C=∪C_i`), contraction `c: S→S'` with `c(C)=pt`, `c: S\C ≅ S'\{pt}` iso, `S'` normal (smooth when `C` is `(-1)`-curve, singular otherwise). Grauert criterion: `C` contractible iff intersection matrix `(C_i·C_j)` negative definite. For `C≅P^1, C^2=-1` get smooth `S'` (Castelnuovo); for `C^2=-2` chain get du Val singularity on `S'`. Toric contraction is `v_i` removal from fan (coarsening). Interface `S.contract_curve(C) → (S', c)` with `c: S→S'` and `S'.singularity_at(c(C))` when not `(-1)`.

Intended owners: `categories/schemes/rational_maps.py` (`RationalMap X⇢Y` with `domain`, `morphism`), `categories/schemes/birational_maps.py` (`BirationalMap` with `is_birational` via `k(X)≅k(Y)`), `categories/schemes/blowups.py` (`Bl_p X` with `π, E≅P^{n-1}`, `Pic` splitting), `categories/schemes/resolution.py` (`resolve_indeterminacy` via `Bl_{p_i}` sequence), `categories/schemes/surfaces/contractions.py` (`contract_curve(C) → S'` with `Grauert`/`Castelnuovo` `E^2=-1`). Not a free `blowup(X,point)` matrix — `X.blowup(p)` on the scheme object with exceptional `E`.

## Desired capability: singularities — normal forms, Milnor/Tjurina, Kodaira fibers, dual graphs — note 2026-09-16

Need normal form classification of isolated point singularities, computing and classifying singularities in other codimensions when possible, Milnor and Tjurina numbers, fibrations with Kodaira classification, and dual graphs of exceptional curves.

* Isolated hypersurface singularity `f: (C^n,0)→(C,0)` with `f(0)=0`, `df(0)=0`, isolated means `μ<∞` where `μ=dim_C C{x_1…x_n}/(∂f)` finite. Normal forms: for `n=2`, `A_k: x^2+y^{k+1}`, `D_k: x^2y+y^{k-1}`, `E_6: x^3+y^4`, `E_7: x^3+xy^3`, `E_8: x^3+y^5` (simple / du Val / rational double points, `μ=τ`); for `n≥3` add `A_k` suspension etc. Classification is Arnold's `A-D-E` plus unimodal etc. Interface `f.normal_form() → (type, k)` with `type ∈ {A_k,D_k,E_6,E_7,E_8}` when simple, `Unknown` else, computed via `μ,τ` and resolved via `SINGULAR` adapter when available, not by brute Groebner in preamble.

* Milnor `μ(f)=dim_C C{x}/J(f)` where `J(f)=(∂f/∂x_i)` Jacobian ideal, and Tjurina `τ(f)=dim_C C{x}/(f,J(f))` where `T(f)=(f,J(f))`. For isolated `f`, `τ ≤ μ` with `τ=μ` iff `f` weighted homogeneous. Also `μ = rank H_{n-1}(F)` Milnor fiber `F=f^{-1}(δ)∩B_ε` (`F ≃ ∨_{i=1}^μ S^{n-1}`), `τ = dim T^1_{f}` base of miniversal deformation. For complete intersection `f=(f_1…f_c)`, `μ` via `Ω` etc. Interface `f.milnor_number() → μ : NN`, `f.tjurina_number() → τ : NN` on the germ object `HypersurfaceSingularity(f)` with `C{x}` as `Rings` completion.

* Computing and classifying singularities in other codimensions when possible: for `X⊂A^n` defined by `I=(f_1…f_m)`, singular locus `Sing X = V(I+Jac_c)` where `Jac_c` is ideal of `c×c` minors of Jacobian `Jac(f)` (`c=codim X`), `dim Sing X` is codim of singularity. Classify `p∈X` as `regular ⇔ rank Jac(p)=c`, else `singular` with `embdim = n - rank`, `mult = ord_p(I)`, `type` via `μ,τ` when isolated hypersurface, otherwise via `Singular` stratification (`Whitney`, `Hilbert-Samuel`). Find algorithms means delegate to maintained `SINGULAR`/`Oscar` for `Sing`, `mult`, `μ,τ` when isolated, and report `Unknown` with reason when not decidable (non-isolated requires different invariants). Do not claim classification by Hilbert polynomial alone.

* Fibrations operationalized: flat proper morphism `f: S→C` with `S` surface, `C` curve, generic fiber `F = S_η` smooth curve over `k(C)`. For elliptic fibration, `F` is genus-1 curve with section `σ: C→S`. Need `f.fibers() → [F_p]` over `p∈C` with `F_p = f^{-1}(p)` divisor, smooth vs singular.

* Kodaira classification of singular fibers for minimal elliptic `f: S→C` with section (Kodaira-Néron): each singular fiber `F_p` is Kodaira type with dual graph affine Dynkin: `I_n` (`n≥0`, `I_0` smooth, `I_1` nodal rational, `I_n` `n`-gon of `P^1`s), `I_n^*` (`D_{n+4}`), `II` (cusp, `1` rational with cusp), `III` (`2` rationals tangent), `IV` (`3` concurrent), `II^*` (`E_8`), `III^*` (`E_7`), `IV^*` (`E_6`) with multiplicities `m_i` and self-intersections `F_{p,i}^2=-2`. Fiber given by valuations `v_p(g_2), v_p(g_3), v_p(Δ)` in Weierstrass `y^2=4x^3-g_2x-g_3`, `Δ=g_2^3-27g_3^2`. Interface `f.kodaira_fiber(p) → Type` with `type ∈ {I_n,I_n^*,II,III,IV,II^*,III^*,IV^*}` and `F_p = Σ m_i Θ_i`.

* Dual graphs of exceptional curves in resolutions: for `π: \tilde S→S` resolution of `p∈S` (e.g. du Val), exceptional `Exc(π)=∪_{i}E_i` with `E_i≅P^1`, graph `Γ(Exc)` with vertex `v_i` per `E_i`, edge `v_i—v_j` when `E_i·E_j=1` (or `>0`), vertex weight `w(v_i)=E_i^2` (usually `-2` for du Val, `-1` for blowup), edge multiplicity `E_i·E_j`. For `A_k`, `Γ=A_k`; `D_k→D_k`, `E_6/E_7/E_8→E_6/E_7/E_8`; for general cusp, `Γ` is cycle. Interface `π.dual_graph() → Γ : WeightedGraph` with `Γ.vertices()=E_i`, `Γ.edge_weight(v_i,v_j)=E_i·E_j`, `Γ.vertex_weight(v_i)=E_i^2`.

Intended owners: `categories/schemes/singularities/isolated.py` (`HypersurfaceSingularity(f)` with `normal_form` `A_k/D_k/E_6/E_7/E_8`, `is_isolated`), `categories/schemes/singularities/milnor_tjurina.py` (`milnor_number μ=dim C{x}/J`, `tjurina_number τ=dim C{x}/(f,J)`), `categories/singularities/classification.py` (`classify(p∈X)` via `Sing X` minors, `mult`, `embdim`), `categories/schemes/fibrations.py` (`Fibration f: S→C` with `fibers`), `categories/schemes/elliptic_surfaces/kodaira.py` (`kodaira_fiber(p)` `I_n/I_n^*/II/III/IV/II^*/III^*/IV^*` via `v_p(g_2),v_p(g_3),v_p(Δ)`), `categories/schemes/resolution/dual_graphs.py` (`dual_graph(Exc) → Γ` weighted). Not a free `kodaira_type(fiber)` string — `f.kodaira_fiber(p)` on the fibration with Weierstrass data.

## Desired capability: generalized weighted graphs, Coxeter/Dynkin/s.e. laced, bilinear ↔ graph — note 2026-09-16

Need generalized weighted-edge-and-vertex graphs, specializing to Coxeter diagrams (nodes weights ±2 or 4), further to Dynkin (±2), further to simply laced, with smooth passage between any bilinear form and associated (di)graph.

* Generalized graph is `D=(V,E,w_V,w_E)` with `V : FiniteOrderedSets` vertices `v_i`, `E⊂{{i,j}|i≠j}` undirected (or directed for `(di)graph` variant `E⊂V×V` with `i≠j`), vertex weight `w_V: V→ZZ` (`w_V(v_i)=b(v_i,v_i)`) and edge weight `w_E: E→ZZ` (`w_E({i,j})=b(v_i,v_j)` when nonzero). Allow loops via `w_V`, but edge only when `b(v_i,v_j)≠0`. Need object `WeightedGraph` with `D.vertex_weight(v_i)`, `D.edge_weight(e)`, `D.adjacency_matrix()→Mat_{|V|}(ZZ)` with `diag=w_V`, `off-diag=w_E`.

* Specializations as full subcategories with weight restrictions:
  `WeightedGraphs ⊃ CoxeterGraphs ⊃ DynkinGraphs ⊃ SimplyLacedDynkinGraphs`
  where `CoxeterGraphs` is `w_V(v)∈{±2,±4}` and `w_E` corresponds to Coxeter label `m_{ij}∈{2,3,4,6,∞}` via `w_E = -2cos(π/m_{ij})` normalized to `±1,±√2` etc., but in this integral normalization `Coxeter` means vertex weights `±2` (long/short root lengths `2` vs `4`) with edge weights `w_E∈{0,∓1,∓2}` encoding bond multiplicity; `DynkinGraphs` further restricts `w_V∈{±2}` (all roots length `2` or all `±2` after scaling), `SimplyLacedDynkinGraphs` further restricts `w_V=2` and `w_E∈{0,-1}` (i.e. `A-D-E` with single bonds). More precisely per prompt: nodes `w_V=±2` or `4` for Coxeter, `±2` for Dynkin, `2` (with `w_E∈{0,-1}`) for simply laced. Interface must enforce via `CoxeterGraphs` predicate `D.vertex_weights()⊂{±2,±4}` and `Dynkin` `⊂{±2}`.

* Smooth passage between any bilinear form and associated (di)graph with nodes `v_i` of weight `b(v_i,v_i)` and edges weight `b(v_i,v_j)` when nonzero: for `(M,b)` where `M : Modules(ZZ)` free of rank `n` with basis `v=(v_i)_{i<n}` (`v_i ∈ M`) and `b: M×M→ZZ` bilinear (not necessarily symmetric; symmetric for lattices, but general for Coxeter), define `graph(M,b,v) → D` with `D.vertex_weight(v_i)=b(v_i,v_i)` and for `i≠j`, if `b(v_i,v_j)≠0` or `b(v_j,v_i)≠0` put edge `{i,j}` with `w_E({i,j})=b(v_i,v_j)` (or `b(v_j,v_i)` for directed, or unordered with `w_E = b(v_i,v_j)` when symmetric). Conversely, from `D` with `|V|=n`, define `M_D = ⊕_{i<n} ZZ·v_i : Lattices` (free `ZZ`-module) with `b_D(v_i,v_i)=w_V(v_i)`, `b_D(v_i,v_j)=w_E({i,j})` when `{i,j}∈E` else `0`, extended bilinearly. Then `graph(M_D,b_D,canonical_basis)=D` and `module(graph(M,b)) ≅ (M,b)` when basis is the graph's basis. Need functors `BilinearModule→WeightedGraph` and `WeightedGraph→BilinearModule` inverse on framed objects (choice of basis / vertex ordering). For (di)graph, directed variant keeps `b(v_i,v_j)` and `b(v_j,v_i)` separately as two directed edge weights.

Intended owners: `categories/graphs/weighted_graphs.py` (`WeightedGraph D=(V,E,w_V,w_E)` with `vertex_weight`, `edge_weight`), `categories/coxeter/coxeter_diagrams.py` (`CoxeterGraphs` `w_V∈{±2,±4}`, `DynkinGraphs` `w_V∈{±2}`, `SimplyLaced` `w_V=2,w_E∈{0,-1}` as subcats), `categories/forms/bilinear_graphs.py` (`bilinear_to_graph(M,b) → D`, `graph_to_bilinear(D) → (M_D,b_D)`), `categories/lattices/graph_lattices.py` (`GraphLattice` `M_D`). Not a free `graph_of_bilinear_form(matrix)` list — ` (M,b).associated_graph(basis) → D` on the bilinear module with basis datum.

## Desired capability: invariants/coinvariants under `G→O(M,b)`, folding, converse `G→Aut(D)→O(M,b)` — note 2026-09-16

Need invariants and coinvariants under action `G→O(M,b)`, induced folding of associated diagrams, and conversely actions `G→Aut(D)` inducing `G→O(M,b)`.

* Invariants and coinvariants: for `G : Groups` (finite, or finitely generated with action) acting on `(M,b) : BilinearModules` via `ρ: G→O(M,b)` (`O(M,b)={g∈GL(M) | b(gx,gy)=b(x,y) ∀x,y}` orthogonal group of `b`), invariants `M^G = {m∈M | gm=m ∀g∈G} = ker(⊕_{g}(g-1))` as `Sub(M)` pure submodule (fixed sublattice when `M` lattice, `b|_{M^G}` restricted), coinvariants `M_G = M / ⟨gm-m | g∈G,m∈M⟩ = M / span(g-1)M` as `Quot(M)` with quotient map `π: M→M_G` and induced `b_G` when `G` preserves `b` and quotient is torsion-free (or with torsion retained as `Quot`). Need `M.invariants(G,ρ)→M^G : Sub(M)` and `M.coinvariants(G,ρ)→M_G : Quot(M)` on the `G`-module object `M_G = ZZ[G]-Mod` structure, with `M^G = Hom_{ZZ[G]}(ZZ,M)` and `M_G = ZZ⊗_{ZZ[G]}M`.

* Induced folding of associated diagrams: from `(M,b)` with basis `v=(v_i)` giving `D=graph(M,b,v)` (above), `G→O(M,b)` permutes basis up to isometry. Folding is quotient graph `D/G` where orbit `O_i=G·v_i` becomes vertex `w_O` with weight `w(w_O)= Σ_{x,y∈O} b(x,y)` / `|O|`? More invariantly, choose `G`-stable partition of `V` and folded bilinear form `b^G` on `M^G` or on orbit sums `s_O = Σ_{v∈O} v ∈ M^G` with `b^G(s_O,s_{O'}) = Σ_{x∈O,y∈O'} b(x,y)`. Diagram folding `fold(D,G) → D/G` has vertices `O`, vertex weight `b^G(s_O,s_O)`, edge weight `b^G(s_O,s_{O'})` when nonzero, specializing to Dynkin folding `A_{2n-1}→B_n`, `D_{n+1}→B_n`, `E_6→F_4`, `D_4→G_2` when `G` graph automorphism. Need `D.fold(G, action) → D/G : WeightedGraphs`.

* Conversely, action `G→Aut(D)` of the (di)graph inducing `G→O(M,b)`: for `D=(V,E,w)` weighted graph, `Aut(D)={g∈Sym(V) | w_V(gv)=w_V(v), w_E(g e)=w_E(e)}` as `Groups` (finite), and `G→Aut(D)` as permutation representation. Then `M_D=⊕ ZZ·v_i` with `b_D` as above inherits `G→O(M_D,b_D)` via `g·v_i = v_{g(i)}` extending linearly, preserving `b_D` because `w` preserved: `b_D(gv_i,gv_j)=w_E(g{i,j})=w_E({i,j})=b_D(v_i,v_j)`. So graph automorphisms give orthogonal bimodule automorphisms. Need functor `AutGraphToOrthogonal: Aut(D)→O(M_D,b_D)` and `G→Aut(D) ⇒ G→O(M_D,b_D)` composition. Both directions together give equivalence between `G`-stable weighted graphs and `G`-bilinear modules with permutation basis.

Intended owners: `categories/lattices/invariants.py` (`invariants(G,ρ) → M^G = ker(g-1) : Sub`), `categories/lattices/coinvariants.py` (`coinvariants(G,ρ) → M_G = M/⟨gm-m⟩ : Quot`), `categories/graphs/folding.py` (`fold(D,G) → D/G` with `b^G(s_O,s_{O'})`), `categories/lattices/group_actions.py` (`GroupAction G→O(M,b)` with `M^G, M_G`, and `GraphAction G→Aut(D) → G→O(M_D,b_D)`). Not a free `invariants(gens)` list — `M.invariants(rho)` with `rho: G→O(M,b)` morphism as `G-Module` structure.

## Desired capability: vector fields on Lie groups and manifolds, brackets, flows, ad/Ad — note 2026-09-16

Need vector fields on Lie groups (and manifolds more generally), their brackets (Lie and Poisson), associated flows, `ad(X,Y)` and `Ad_X(Y)`.

* Vector field on `M : Man` (`SmMfd`, `RiemMfd`, `ComplexMfd`) is `X: TM→M` section `X∈Γ(TM)` with `X_p∈T_pM`, `X: C^∞(M)→C^∞(M)` derivation `X(fg)=X(f)g+fX(g)`. On Lie group `G : LieGroups` with `g=Lie(G)=T_eG`, left-invariant `X^L` ↔ `X_e∈g` via `X^L_g = dL_g(X_e)` where `L_g: G→G` left translation, similarly right-invariant `X^R_g=dR_g(X_e)`. Space `Γ(TG)^L ≅ g` as `LieAlgebras` via `X^L↦X_e` with bracket preserved. For general `M`, `Γ(TM)` is `LieAlgebras_R` infinite-dimensional with `C^∞(M)`-module structure.

* Lie bracket `[X,Y]∈Γ(TM)` is `LieAlgebras` bracket: `[X,Y](f)=X(Y(f))-Y(X(f))` as derivation, satisfying Jacobi `[[X,Y],Z]+[[Y,Z],X]+[[Z,X],Y]=0` and ` [fX,Y]=f[X,Y]-Y(f)X`. For left-invariant fields on `G`, `[X^L,Y^L]=[X,Y]^L` corresponds to `g` bracket. Need `X.bracket(Y) → [X,Y] : Γ(TM)` on the `Man` object, not as matrix commutator list.

* Poisson bracket `{f,g}∈C^∞(M)` for Poisson manifold `(M, π)` with bivector `π∈Γ(∧^2 TM)` via `{f,g}=π(df,dg)` and Hamiltonian vector field `X_f = π^♯(df)` with `X_f(g)={f,g}`, ` [X_f,X_g]=X_{ {f,g} }`. When `M=T^*Q` or `g^*` dual of Lie algebra, `{ , }` is canonical / Lie-Poisson `{f,g}(ξ)=⟨ξ,[df_ξ,dg_ξ]⟩`. Need `PoissonBracket(f,g) → {f,g}` with Jacobi from `π` integrability ` [π,π]_S=0` Schouten, not as ` {f,g}=∂f∂g` string.

* Flow of `X∈Γ(TM)` is `φ_X^t: M→M` (local flow) with `d/dt φ_X^t(p)=X_{φ_X^t(p)}`, `φ_X^0=id`, `φ_X^{t+s}=φ_X^t∘φ_X^s` where defined, complete when `M` compact or `X` left-invariant on `G` (then `φ_X^t = R_{exp(tX_e)}` or `L_{exp(tX_e)}` depending on invariance). For `G`, exponential `exp: g→G` is flow at `e`: `exp(X)=φ_{X^L}^1(e)`. Need `X.flow(t) → φ_X^t : Diffeomorphisms(M)` with `φ_X^t(p)` ODE, and `X.is_complete()` predicate.

* `ad` and `Ad`: for `G` with `g=Lie(G)`, `Ad: G→GL(g)` adjoint representation `Ad_g = d(c_g)_e` where `c_g(h)=ghg^{-1}`, so `Ad_g(Y)=gYg^{-1}` for matrix `G`, `Ad: G→Aut_{LieAlg}(g)` group morphism with `Ad_{gh}=Ad_g∘Ad_h`. At Lie algebra level `ad: g→gl(g)`, `ad_X(Y)=[X,Y]` with `ad = Lie(Ad) = d(Ad)_e`, so `ad_X = d/dt|_0 Ad_{exp(tX)}`. Relation `Ad_{exp X}=exp(ad_X)` (`exp: gl(g)→GL(g)`). Interface must be `g.ad(X,Y) → [X,Y]=ad_X(Y) : g` and `G.Ad(g,Y) → Ad_g(Y) : g` with `ad = dAd`, `Ad_{exp}` vs `exp∘ad` compatibility, computed via matrix `Ad` when `G` linear, else via `L_g,R_g` derivatives. Not a free `ad_matrix` — `X.ad(Y)` on `g` and `g.Ad(Y)` on `G` objects with `g=Lie(G)` retained.

Intended owners: `categories/manifolds/vector_fields.py` (`VectorField X∈Γ(TM)` on `M: Man` with `bracket`, `flow`), `categories/lie/vector_fields.py` (`LeftInvariantVectorField` `X^L↔g`, `exp` via flow), `categories/geometry/brackets.py` (`LieBracket [X,Y]`, `PoissonBracket {f,g}` with `π`), `categories/dynamics/flows.py` (`Flow φ_X^t: M→M` with `d/dt φ = X`), `categories/representations/adjoint.py` (`ad_X(Y)=[X,Y]: g→gl(g)`, `Ad_g(Y)=gYg^{-1}: G→GL(g)` with `ad=Lie(Ad)`, `Ad_{exp}=exp∘ad`). Not a free `bracket(X,Y)` list — `X.bracket(Y)` and `g.Ad(Y)` on the manifold/Lie objects.

## Desired capability: canonical sheaves, Serre duality — note 2026-09-16

Need canonical sheaves, operationalize Serre duality.

* Canonical sheaf `ω_X` is not a line bundle assigned by hand. For `X: Sm/k` smooth of dimension `n` (or `X: Sch/k` smooth proper), `ω_X = ∧^n Ω^1_{X/k} = det Ω^1_{X/k} : Pic(X)` as `QCoh(X)` invertible, with `ω_X = det T^*X`. For `X` normal Gorenstein, `ω_X` is dualizing sheaf; for `X` proper, `ω_X ≅ f^! O_{Spec k}` where `f: X→Spec k` and `f^!` from six functors. Need `X.canonical_sheaf() → ω_X : Pic(X)` as object `ω_X : InvertibleSheaves(X)` with `ω_X = det Ω^1`, not a divisor class number.

* For singular or non-proper settings, dualizing complex `ω_X^• = f^! O_{Spec k} : D^b_{coh}(X)` in `D(QCoh)` with `ω_X = H^{-n}(ω_X^•)` when `X` smooth `n`-dim; `ω_X^•` is the `f^!` object from `six_functors` already intaken. Interface `X.dualizing_complex() → ω_X^•` and `X.canonical_sheaf() → ω_X` when `X` smooth.

* Serre duality is not `h^i = h^{n-i}` equality of numbers. For `X : SmProj/k` smooth projective `n`-dim and `F : Coh(X)` coherent, duality is natural isomorphism
  `Ext^i_X(F, ω_X) ≅ H^{n-i}(X, F)^∨` (`k`-dual), functorially `RΓ(F)^∨ ≅ RHom_X(F, ω_X[n])` in `D(k)`, and `Ext^i(F, ω_X) ≅ H^{n-i}(F)^*`. In derived form `RHom_X(F, ω_X[n]) ≅ RΓ(F)^∨` with shift `[n]`, and `Rf_* RHom(F, f^! G) ≅ RHom(Rf_*F, G)` adjunction for `f: X→Spec k` proper. For vector bundle `F`, `H^i(X, F)^∨ ≅ H^{n-i}(X, F^∨⊗ω_X)` via `Ext^i(F,ω)=H^i(F^∨⊗ω)`. Trace `tr: H^n(X, ω_X) → k` is the duality pairing.

* Operationalize means: from `X: SmProj` with `ω_X` as above and `F: QCoh` with `RΓ(F) : D(k)` effective via Čech `Č(U,F)` already intaken, construct `RHom(F, ω_X)` and the Yoneda pairing `Ext^i⊗H^{n-i}→k` via `∪` and `tr`, and certify `dim Ext^i = dim H^{n-i}` with explicit `k`-linear iso `SD_{X,F,i}: Ext^i(F,ω_X) → H^{n-i}(F)^∨` as `Vect_k` isomorphism, not as dimension equality. When `F=O_X(D)` for divisor `D`, `SD` gives `h^i(O(D))^∨ = h^{n-i}(O(K-D))`.

Intended owners: `categories/sheaves/canonical.py` (`canonical_sheaf X→ω_X=∧^nΩ^1 : Pic` and `dualizing_complex f^!O`), `categories/duality/serre.py` (`SerreDuality` `Ext^i(F,ω_X) ≅ H^{n-i}(F)^∨`, `RHom(F,ω_X[n]) ≅ RΓ(F)^∨` via `Rf^!`), delegating to `categories/sheaves/six_functors.py` (`f^!`, `Rf_* ⊣ f^!`), `categories/schemes/canonical.py` (`X.canonical_divisor() → K_X` with `O(K_X)=ω_X`). Not a free `serre_dual(F)` number — `X.serre_duality(F,i) → Hom(Ext^i, H^{n-i∨})` on the scheme with `ω_X`.

## Desired capability: Siegel half-spaces — note 2026-09-16

Need Siegel half-spaces.

* Siegel upper half-space `HH_g = { Z∈Mat_{g×g}(C) | Z^t=Z, Im Z >0 }` (`Im Z` positive definite Hermitian `g×g`) as `ComplexMfd` of dimension `n=g(g+1)/2` (`n : NN`), with `HH_1 = HH` upper half-plane, `HH_g = Sp_{2g}(RR)/U(g)` as symmetric space `G/K` where `G=Sp_{2g}(RR)`, `K=U(g)` maximal compact, `Sp_{2g} = { M∈GL_{2g} | M^t J M = J }`, `J=(0 I_g; -I_g 0)`. As `ComplexMfd`, `HH_g` has bounded domain model via Cayley `Z↦(Z-iI)(Z+iI)^{-1}`.

* Action `γ·Z = (AZ+B)(CZ+D)^{-1}` for `γ=(A B; C D)∈Sp_{2g}(RR)` with `A,B,C,D∈Mat_{g×g}(RR)` (`γ^t J γ =J`), `γ·Z∈HH_g` when `Z∈HH_g`, transitive with stabilizer `U(g)` at `Z_0=iI_g`. Arithmetic subgroup `Γ_g = Sp_{2g}(ZZ) ⊂ Sp_{2g}(Q)` acting properly discontinuously, quotient `A_g = Γ_g\HH_g : QuasiProjVar` is moduli of principally polarized abelian varieties of dimension `g` (`A_g ≅ M_{ppav,g}`), with `A_1 = SL_2(ZZ)\HH = M_{1,1}` elliptic curves. Need Siegel modular forms `f: HH_g→C` with `f(γ·Z)=det(CZ+D)^k f(Z)`.

* As generalization of `HH=HH_1`, need `HH_g` as object `SiegelHalfSpace(g) : HermitianSymmetricSpaces` with `HH_g.dimension()→g(g+1)/2`, `HH_g.group()→Sp_{2g}`, `HH_g.arithmetic_subgroup()→Sp_{2g}(ZZ)`, and `HH_g.quotient()→A_g`.

Intended owners: `categories/modular/siegel_half_space.py` (`SiegelHalfSpace HH_g={Z|Z^t=Z,Im Z>0} : ComplexMfd` with `Sp_{2g}(RR)/U(g)`, action `(AZ+B)(CZ+D)^{-1}`), `categories/hermitian/siegel.py` (`Siegel domain` as `HermitianSymmetric`), `categories/moduli/ppav.py` (`A_g=Sp_{2g}(ZZ)\HH_g` moduli). Not a free `siegel_half_space(g)` matrix — `SiegelHalfSpace(g)` object in `ComplexMfd` with `Sp_{2g}` action.

## Desired capability: derivations of modules and augmented ZZ-algebras, Fox free differential calculus — note 2026-09-16

Need derivations of modules and augmented `ZZ`-algebras, more generally Fox's algebraic differential forms (the free differential calculus).

* Derivation of augmented algebra: for `R=ZZ` (or `R : CommRings`), `A : Alg_R` augmented means `ε: A→R` as `R`-algebra morphism with section `η: R→A` (`ε∘η=id_R`), equivalently `A = R⊕I` with `I=ker ε` augmentation ideal as `R`-module. For `A`-module `M`, `R`-derivation `d: A→M` is `R`-linear with Leibniz `d(ab)=a·d(b)+d(a)·b` and `d(r)=0` for `r∈R` (via `η`), with `d(1)=0`. Universal derivation `d_A: A→Ω_{A/R}` with `Ω_{A/R}` Kähler differentials as `A`-module generated by `da` with relations `d(ab)=a db + b da`, and `Der_R(A,M)=Hom_A(Ω_{A/R},M)` natural. For augmented `A`, `Ω_{A/R}⊗_A R ≅ I/I^2` via `da↦a-ε(a)`.

* Derivation of module: for `R`-module `M` with `G`-action or `A`-module structure, derivation `d: G→M` or `d: A→M` with appropriate `g·d(h)+d(g)` etc. In group case `d: G→M` satisfies `d(gh)=d(g)+g·d(h)` (`1`-cocycle `Z^1(G,M)`), which is same as algebra derivation when `A=ZZ[G]` augmented via `ε: ZZ[G]→ZZ`, `g↦1`. Need `M.derivations()` as `Der` object.

* Fox free differential calculus is the case `A=ZZ[F_n]` group ring of free group `F_n=⟨x_1…x_n⟩`, augmented via `ε: ZZ[F_n]→ZZ`, `x_i↦1`, `I=(x_i-1)`. Fox derivatives `∂/∂x_i: ZZ[F_n]→ZZ[F_n]` are `ZZ`-linear with `∂x_j/∂x_i=δ_{ij}`, `∂(uv)/∂x_i = ∂u/∂x_i + u·∂v/∂x_i` (twisted Leibniz with left `u`), and `u-ε(u)= Σ_{i} (x_i-1)·∂u/∂x_i` fundamental formula, and `∂(u^{-1})/∂x_i = -u^{-1}·∂u/∂x_i`. Universal `d: ZZ[F_n]→⊕_{i=1}^n ZZ[F_n]·dx_i` free `A`-module `Ω_{ZZ[F_n]/ZZ} ≅ ⊕ A·dx_i` with `d(u)=Σ ∂u/∂x_i dx_i`. So `Der` is free. This computes `H_1(F_n, M)` etc., and `I/I^2` etc.

* Need functors: `AugmentedAlgebra(A,ε) → Der_R(A,M)=Hom(Ω,M)` with `Ω_{A/R}` as `A`-module, `FoxDerivatives(F_n) → ∂/∂x_i` on `ZZ[F_n]`, and more generally for `F` free group / free algebra `T(V)` / `R⟨X⟩`, `Ω` free with basis `dx_i`. Interface `A.derivations(M) → Der_R(A,M) : Modules`, `ZZ[F_n].fox_derivative(x_i, u) → ∂u/∂x_i`, `A.kahler_differentials() → Ω_{A/R}` as `A`-module with `d_A: A→Ω`.

Intended owners: `categories/algebras/derivations.py` (`Der_R(A,M)=Hom_A(Ω_{A/R},M)` with `Ω` Kähler, augment case `Ω⊗_A R ≅ I/I^2`), `categories/algebras/augmented_algebras.py` (`AugmentedAlgebra(A,ε: A→R)` with `I=ker ε`), `categories/algebras/fox_calculus.py` (`FoxDerivatives` `∂/∂x_i: ZZ[F_n]→ZZ[F_n]` with `∂(uv)=∂u+u∂v`, `Ω_{ZZ[F_n]}=⊕A·dx_i` free), `categories/modules/derivations.py` (`ModuleDerivation` `d: G→M` `d(gh)=d(g)+g·d(h)` as `Z^1`). Not a free `fox_derivative(word)` string — `ZZ[F_n].fox_derivative(x_i)` on the augmented group algebra with `Ω` free.

## Desired capability: content ideal `c_M(x)` of an element `x∈M` — note 2026-09-16

Let `R : CommRings` and `M : R-Mod`. An element `x∈M` determines a map
```
(3)  ev_x: Hom_R(M,R) → R,  f ↦ f(x)
```
This map is `R`-linear: `ev_x(r·f)=r·f(x)=r·ev_x(f)` and `ev_x(f+g)=f(x)+g(x)`, hence `im(ev_x) ⊲ R` is an ideal. Denote `c_M(x) = im(ev_x) ⊂ R` and call it the content of `x`. Interface must be `M.content_ideal(x) → c_M(x) : Ideals(R)` as object `c_M(x) : Ideals(R)` with `c_M(x) = { f(x) | f∈Hom_R(M,R) }`, not a bare set of evaluations.

* Lemma 3.4. If `M` is free of finite rank and `x∈M` is non-zero, then `c_M(x)` is a non-zero ideal in `R`. Proof via a basis `M ≅ R^n` with `x=(r_1,…,r_n) ≠ 0`, then `Hom_R(M,R) ≅ R^n` via dual basis `e_i^*`, `ev_x(e_i^*) = r_i`, so `c_M(x) = (r_1,…,r_n) ⊲ R` is the ideal generated by the coordinates, non-zero because some `r_i≠0`. Need `M.is_free()`, `M.rank() : NN`, `M.basis()`, `Hom_R(M,R)` dual module, and `Ideal(R)` construction to state and prove the lemma as `c_M(x) ≠ 0` when `x≠0` and `M∈FreeFiniteRank`.

Intended owners: `categories/modules/content.py` (`content_ideal M.content_ideal(x) → c_M(x) = im(Hom_R(M,R) → R, f↦f(x)) : Ideals(R)`), `categories/modules/dual.py` (`Hom_R(M,R) : R-Mod` dual), `categories/modules/free_modules.py` (`FreeFiniteRank` with `basis`, `rank`), `categories/rings/ideals.py` (`Ideals(R)`). Not a free `content_of_element(M,x)` returning list of values — `M.content_ideal(x)` on the module with `Hom_R(M,R)` dual.

## Desired capability: shortcuts for common matrices — Jordan blocks, banded, tridiagonal, antidiagonal, symplectic form — note 2026-09-16

Need shortcuts for matrices which are extremely common as constructors, not as hand-rolled `Matrix(R, [[...]])` lists.

* Jordan block `J_n(λ) : Mat_n(R)` for `R : CommRings`, `n : NN`, `λ : R` is `J_n(λ) = λ·I_n + N_n` where `N_n` is nilpotent with `(N_n)_{i,i+1}=1` for `1≤i<n` and `0` else, so `J_n(λ) = [[λ,1,0,…],[0,λ,1,…],…,[0,…,λ]]`. Interface `JordanBlock(n, λ) → J_n(λ) : Mat_n(R)` with `JordanBlock(1,λ)=[λ]`, `JordanBlock(n,0)=N_n`. Need `J_n(λ).charpoly() = (T-λ)^n` and `J_n(λ)` as `End_R(R^n)` with `R^n : R-Mod` free.

* Banded matrix of bandwidth `(k,l)` (or `w = max(k,l)`) is `A : Mat_{m×n}(R)` with `A_{ij}=0` if `j-i > k` (super-band) or `i-j > l` (sub-band). Specialization `w=1` with `k=l=1` is tridiagonal. Need `BandedMatrix(m,n,k,l, entries)` constructor where entries are given as bands `a^{(d)}_i = A_{i,i+d}` for `-l≤d≤k`, not as full `m×n` list. The matrix is sparse by construction, not by zero-filling.

* Tridiagonal `T_n(a,b,c) : Mat_n(R)` with diagonal `a = (a_1,…,a_n) : R^n`, superdiagonal `b = (b_1,…,b_{n-1})`, subdiagonal `c = (c_1,…,c_{n-1})`, `T_{ii}=a_i`, `T_{i,i+1}=b_i`, `T_{i+1,i}=c_i`, `0` else. Interface `TridiagonalMatrix(diag=a, super=b, sub=c) → T : Mat_n(R)` and `TridiagonalMatrix(n, a,b,c)` variant. Includes symmetric tridiagonal when `b=c`.

* Antidiagonal `A_n(v) : Mat_n(R)` for `v=(v_1,…,v_n) : R^n` is `A_{i, n+1-i}=v_i` and `0` else, so `A = [[0,…,v_1],[0,v_2,0,…],…,[v_n,…,0]]` with anti-diagonal `v`. Permuted identity `J_n = AntidiagonalMatrix(1,…,1)` is the reversal matrix `J_n^2=I_n`, `J_n A J_n` reverses. Interface `AntidiagonalMatrix(vec) → A : Mat_n(R)` with `vec : R^n` as module element.

* Basic symplectic form matrix `J_{2g} : Mat_{2g}(R)` is `J_{2g} = [0 I_g; -I_g 0]` block matrix with `I_g : Mat_g(R)` identity, `0 : Mat_g(R)` zero, so `J_{2g} = [[0, I_g],[-I_g,0]]` with `J_{2g}^t = -J_{2g}`, `J_{2g}^2 = -I_{2g}`, `det J_{2g}=1`. This is the standard symplectic form `⟨x,y⟩ = x^t J_{2g} y` preserved by `Sp_{2g}(R) = { M | M^t J_{2g} M = J_{2g} }`. Variant with `R=ZZ` gives `Sp_{2g}(ZZ)`. Need `SymplecticFormMatrix(g) → J_{2g} : Mat_{2g}(R)` and `SymplecticFormMatrix(g, R)` over `R`, with `J_2 = [0 1; -1 0]` for `g=1`. When `R` not commutative, use appropriate sign.

Intended owners: `categories/matrices/common_matrices.py` (`JordanBlock(n,λ)`, `BandedMatrix(m,n,k,l)`, `TridiagonalMatrix`, `AntidiagonalMatrix`, `SymplecticFormMatrix(g)`), `categories/matrices/jordan.py` (`JordanBlock` with `N_n`), `categories/matrices/banded.py` (`BandedMatrix` with bandwidth), `categories/matrices/symplectic.py` (`J_{2g} = [0 I_g; -I_g 0]` with `Sp_{2g}`). Not a free `Matrix([[λ,1],[0,λ]])` — `JordanBlock(n, λ)` etc. on `R` with `Mat_n(R)` parent.

## Desired capability: rational canonical form (Frobenius normal form) — note 2026-09-16

Need rational canonical form as owned normal form, not as hand-rolled `Matrix.diagonal([companion(...)])` list.

* Companion matrix `C(p) : Mat_d(F)` for monic `p(x)=x^d + a_{d-1}x^{d-1}+…+a_0 ∈ F[x]` (or `R[x]` monic over PID) is `C(p) = [[0,0,…,0,-a_0],[1,0,…,0,-a_1],[0,1,…,0,-a_2],…,[0,…,1,-a_{d-1}]]` with `1` on subdiagonal and `-a_i` in last column, so `charpoly(C(p))=p` and `m_{C(p)}=p`, and `F^d ≅ F[x]/(p)` as `F[x]`-module via `x·v = C(p)v`. For `deg p =0` (`p=1`), `C(p)` is `0×0` empty block.

* Rational canonical form `RCF(A) : Mat_n(F)` for `A : Mat_n(F)` over field `F` (or PID `R` with `R[x]` PID) is `RCF(A) = diag(C(p_1),…,C(p_r))` block diagonal with invariant factors `p_1 | p_2 | … | p_r` monic in `F[x]`, `p_r = m_A` minimal polynomial, `∏_{i=1}^r p_i = χ_A` characteristic polynomial, and `r =` number of invariant factors = `dim_F` of `F^n` as `F[x]`-module decomposition `F^n ≅ ⊕_{i=1}^r F[x]/(p_i)` where `x·v = A v`. Similarly elementary divisors refine via factorization `p_i = ∏ q_j^{e_{ij}}` with `q_j` irreducible. The invariant factors are obtained from Smith normal form of `xI_n - A : Mat_n(F[x])` via `diag(1,…,1,p_1,…,p_r)` with `p_i | p_{i+1}`. Two matrices are similar `B = P A P^{-1}` iff `RCF(B)=RCF(A)` (i.e. same `p_i`). Jordan form over algebraic closure is refinement when `p_i` splits: `J_n(λ)` blocks are `C((x-λ)^k)` companion.

* As `F[x]`-module structure, the invariant factors classify: `M_A = F^n` with `x·m = A m` is finite `F[x]`-module, `M_A ≅ ⊕ F[x]/(p_i)` with `p_i|p_{i+1}`, and `RCF(A)` is the matrix of `x` on `⊕ F[x]/(p_i)` in the basis `1, x, …, x^{d_i-1}` per summand. Over PID `R`, same with `R[x]` and `p_i∈R[x]` monic.

* Interface must be `A.rational_canonical_form() → RCF(A) : Mat_n(F)` as object `RCF(A) : Mat_n(F)` with `RCF(A).invariant_factors() → [p_1,…,p_r] : List(F[x])` monic with `p_i|p_{i+1}`, `RCF(A).companion_blocks() → [C(p_i)]`, and `A.rational_canonical_form_transformation() → P : GL_n(F)` with `P A P^{-1} = RCF(A)` when `P` exists (e.g. via Smith). For `F = QQ`, `QQbar`, `F_p`, `R=ZZ`, need `F[x] = PolynomialRing(F)` as `Rings` owner. Do not use `A.jordan_form()` as substitute over non-splitting fields.

Intended owners: `categories/matrices/rational_canonical.py` (`RationalCanonicalForm` `RCF(A)=diag(C(p_i))` with `p_i|p_{i+1}`, `m_A=p_r`, `χ_A=∏p_i`), `categories/matrices/companion.py` (`CompanionMatrix(p) → C(p) : Mat_{deg p}(F)`), `categories/modules/frobenius_form.py` (`F[x]`-module `M_A = R^n` with `x·v = A v` and `M_A ≅ ⊕ R[x]/(p_i)`). Not a free `diagonal_matrix([companion(p) for p in factors])` — `A.rational_canonical_form()` on the matrix with `F[x]` Smith.

## Desired capability: annihilators and element-wise methods via annihilator ideals — note 2026-09-16

For `R : CommRings` and `M : R-Mod`, and for `x∈M` and `N≤M` submodule, define annihilators as ideals of `R`:

* Element annihilator `Ann_R(x) = { r∈R | r·x = 0 } ⊲ R` as `Ideals(R)` with `0∈Ann_R(x)`, closed under `+` and `R·Ann⊂Ann`. The annihilator is the kernel of the orbit map `R → M, r↦r·x`, so `R/Ann_R(x) ≅ R·x ≤ M` as `R-Mod`. Interface `M.annihilator(x) → Ann_R(x) : Ideals(R)` with `M.annihilator(x) = {r | r·x=0}`.

* Module and submodule annihilators `Ann_R(M) = { r∈R | r·M=0 } = ∩_{x∈M} Ann_R(x) ⊲ R` and `Ann_R(N) = ∩_{x∈N} Ann_R(x) ⊲ R` as `Ideals(R)` (possibly intersection over infinite `M`, but ideal is well-defined; compute via generating set when `M` finitely generated `M = Σ R·x_i` then `Ann_R(M)=∩_i Ann_R(x_i)`). Need `M.annihilator() → Ann_R(M) : Ideals(R)` for the whole module and `M.annihilator_of_submodule(N) → Ann_R(N)`.

* Element-wise methods replaced with properties of annihilators (as ideals, not as element tests):
  - `M.is_zero() ⇔ M=0 ⇔ Ann_R(M)=R ⇔ 1∈Ann_R(M)` (the zero module is the unique module annihilated by `1`), not by enumerating `x∈M`.
  - `M.is_faithful() ⇔ Ann_R(M)=0` in `R` (faithful means no non-zero `r` kills all of `M`), not by testing `r·x` for all `r,x`.
  - `x.is_zero() ⇔ x=0 ⇔ Ann_R(x)=R ⇔ 1·x=0`.
  - `x.is_torsion() ⇔ Ann_R(x)≠0` when `R` domain (torsion means non-zero `r` with `r·x=0`); more generally `x` is `I`-torsion for `I⊲R` when `I⊆Ann_R(x)`. This replaces ad-hoc `x.is_torsion()` that would test `r·x` by enumerating `r`.
  - Similarly `M.is_torsion()` means `∀x∈M, Ann_R(x)≠0` (or `Ann_R(x)` contains a regular element), not a separate predicate.
  The annihilator ideal carries the uniform interface: `Ann_R(x).is_zero_ideal()`, `Ann_R(x).is_whole_ring()`, `Ann_R(x).contains(r)`, `Ann_R(x).is_nonzero()`.

Intended owners: `categories/modules/annihilator.py` (`annihilator M.annihilator(x) → Ann_R(x) : Ideals(R)`, `M.annihilator() → Ann_R(M)`, with `R/Ann_R(x) ≅ R·x`), `categories/modules/torsion.py` (`is_torsion` via `Ann_R(x)≠0`), `categories/modules/faithful.py` (`is_faithful` via `Ann_R(M)=0`, `is_zero` via `Ann_R(M)=R`), `categories/rings/ideals.py` (`Ideals(R)` as lattice). Not a free `is_zero_element(x)` or `annihilator(x)` returning list of `r` — `M.annihilator(x)` on the module with `Ideals(R)`.

## Desired capability: matrix spaces over `R` as fibered category `Mat(R)` and module morphisms via matrices as honest functor — note 2026-09-16

Reformulate matrix spaces over `R` via the category fibered over rings whose objects are `NN` and whose morphisms are `Mat_{n,m}(R)`, and formalize e.g. the fact that module morphisms can sometimes be realized or constructed via matrices as an honest functor to or from this category.

* Fibered category `Mat` over `Rings`: total category `Mat` with objects `(R,n)` where `R : Rings` and `n : NN`, and morphisms `(R,n) → (S,m)` are pairs `(φ: R→S ring morphism, A: Mat_{m×n}(S))` with composition `(ψ,B)∘(φ,A) = (ψ∘φ, B·φ_*(A))` where `φ_*(A)` is base-change of matrix entries along `φ`. Fiber over fixed `R` is `Mat(R)` with `Ob(Mat(R)) = NN` and `Hom_{Mat(R)}(n,m) = Mat_{m×n}(R)` as `R`-module of `m×n` matrices, composition via matrix multiplication `B∘A = B·A : Mat_{p×n} = Mat_{p×m}·Mat_{m×n}`, identities `I_n : Mat_{n×n}(R)`. This is the skeletal category of finite free `R`-modules: `R^n` is object `n`.

* As skeletal model, `Mat(R)` is equivalent to `Free_{fin}(R-Mod)` (finite free `R`-modules with `R`-linear maps) via functors `Free: Mat(R) → R-Mod` sending `n ↦ R^n` and `A: Mat_{m×n}(R) ↦ (R^n → R^m, v↦Av)` as `R`-linear map, and `Coord: Free_{fin}(R-Mod) → Mat(R)` choosing a basis (when `M ≅ R^n` free finite rank) sending `M` with basis `e` to `n` and `f: M→N` to its matrix `[f]_e` in bases. Need equivalence `Mat(R) ≃ Free_{fin}(R-Mod)` as categories, with `Hom_R(R^n,R^m) ≅ Mat_{m×n}(R)` as `R-Mod` isomorphism via `A ↦ (v↦Av)`, natural in `R` along base-change `⊗_R S`.

* Module morphisms via matrices as honest functor to or from this category: for `M,N : R-Mod` with chosen finite presentations `R^a → R^b → M → 0` and `R^c → R^d → N → 0` (or with chosen bases when `M,N` free `M≅R^n, N≅R^m`), a morphism `f: M→N` is sometimes realized by a matrix `A : Mat_{d×b}(R)` (or `m×n` when free) with `A·relations_M ⊆ relations_N`. Formalize as functor `MatrixRealization: Free(R-Mod) ⇄ Mat(R)` and more generally for finitely presented `M,N`, a functor `PresMat: Mod_{f.p.}(R) → Mat(R)`-arrows up to homotopy, where `f` lifts to `A: R^b→R^d` with `A∘present_M = present_N∘B` for some `B`. The fact that `f` can be constructed from `A` when bases/presentations are fixed is an honest functor, not an ad-hoc `matrix_of_morphism(f)` returning a list. Similarly base-change along `R→S` is functorial `Mat(R) → Mat(S)` via `A ↦ φ_*(A)`.

* Interface must be fibered: `R.matrix_category() → Mat(R) : Cat` with `Mat(R).objects() = NN`, `Mat(R).hom_set(n,m) → Mat_{m×n}(R) : R-Mod`, `Mat(R).composition(A,B) → B·A`, and `Rings` base `Rings.mat_fibration() → Mat` total. For modules, `FreeModule(R,n).as_mat_object() → n : Mat(R)` and `Hom_R(R^n,R^m).as_matrix(f) → Mat_{m×n}(R)` with `Hom_R(R^n,R^m) ≅ Mat_{m×n}(R)`. For general `M,N` with `M.is_free_finite_rank()` or `M.is_finitely_presented()`, `f.matrix(basis_M, basis_N) → Mat` and conversely `Mat(R).morphism(matrix, domain_basis, codomain_basis) → f : M→N` as honest functor, with `matrix(f∘g)=matrix(f)·matrix(g)`.

Intended owners: `categories/matrices/fibered_category.py` (`Mat(R)` fibered over `Rings` with `Ob=NN`, `Hom(n,m)=Mat_{m×n}(R)`, composition `·`), `categories/modules/free_modules.py` (`R^n : Free_{fin}` with `Mat(R) ≃ Free_{fin}(R-Mod)`), `categories/functors/matrix_functor.py` (`MatrixRealization : Mat(R) ⇄ Free(R-Mod)` with `Hom_R(R^n,R^m) ≅ Mat_{m×n}(R)`), `categories/matrices/hom_sets.py` (`Hom_{Mat(R)}(n,m) = Mat_{m×n}(R) : R-Mod`). Not a free `matrix_of_morphism(f)` returning `List[List[R]]` — `Hom_R(R^n,R^m).as_matrix()` and `Mat(R).morphism(matrix)` as functor between `Mat(R)` and `R-Mod`.

## Desired capability: honest products and pullbacks of categories, categories fibred over other categories, stacks — note 2026-09-16

Need honest products and more generally pullbacks of categories, as well as categories fibred over other categories. This leads to defining stacks.

* Honest products of categories: for `C,D : Cat`, product `C×D : Cat` with `Ob(C×D)=Ob(C)×Ob(D)`, `Hom_{C×D}((c,d),(c',d')) = Hom_C(c,c')×Hom_D(d,d')` with componentwise composition `(f',g')∘(f,g) = (f'∘f, g'∘g)` and identities `(id_c,id_d)`, projections `π_C: C×D→C`, `π_D: C×D→D` universal for pairs `E→C, E→D`. This is the categorical product in `Cat` (2-category). Similarly n-ary `∏_{i} C_i`. Need `C.product(D) → C×D : Cat` and `Cat.has_products`.

* More generally pullbacks of categories: for functors `F: C→E` and `G: D→E`, pullback (fiber product) `C×_E D : Cat` with `Ob(C×_E D) = {(c,d,α: F(c) → G(d) iso)}` for pseudo-pullback (or `F(c)=G(d)` for strict), morphisms `(f: c→c', g: d→d')` with `G(g)∘α = α'∘F(f)`, projections to `C,D` and 2-cell `α`. Universal for cones `E'→C, E'→D` with `F∘p_C ≅ G∘p_D`. Strict pullback `C×_E^{str} D` when `F(c)=G(d)` on nose is special case for discrete fibrations. This generalizes products (`C×D = C×_1 D` over terminal `1`). Need `C.pullback(E,D, F,G) → C×_E D : Cat` with universal property.

* Categories fibred over other categories: functor `p: E→B` is Grothendieck fibration (category fibred over `B`) if for every `f: b'→b` in `B` and `e∈E_b` over `b`, there is cartesian lift `φ: f^*e → e` over `f` universal for lifts: for any `ψ: e''→e` over `h: p(e'')→b` factoring as `h = f∘g`, there is unique `χ: e''→f^*e` over `g` with `φ∘χ=ψ`. Equivalently cleavage `f^*: E_b → E_{b'}` pullback functor, with coherence ` (g∘f)^* ≅ f^*∘g^*`. Fiber `E_b = p^{-1}(b)` is subcategory of objects over `b` and vertical morphisms over `id_b`. Examples: `Mat → Rings` fibered with fiber `Mat(R)`, `Mod → Rings` with fiber `R-Mod`, `QCoh → Sch`, `Fam → Sch`. Need `p: E→B` as `FiberedCategory` with `p.is_fibred()`, `p.cartesian_lift(f,e)`, `p.fiber(b) → E_b : Cat`, `p.pullback_functor(f) → f^*: E_b→E_{b'}`.

* Stacks: a category fibred over a site `(B,J)` (e.g. `Sch` with étale topology `J_ét`, or `Top` with open covers) satisfying effective descent — i.e. 2-sheaf condition. For cover `U = {u_i: b_i→b}` in `J`, descent data is family `e_i∈E_{b_i}` with isomorphisms `α_{ij}: pr_1^* e_i ≅ pr_2^* e_j` over `b_i×_b b_j` satisfying cocycle `α_{jk}∘α_{ij}=α_{ik}` over triple overlaps `b_i×_b b_j×_b b_k`. Effectivity means descent data glue to `e∈E_b` with `e|_{b_i} ≅ e_i` via `α`. Stack condition requires descent for objects (effective) and for morphisms (sheaf condition `Hom_{E_b}(e,e')` is sheaf on `B/b`). Algebraic stacks are stacks on `Sch_{ét}` representable by groupoid presentation `R⇉U` with `R,U : Sch` and `p: E→Sch` fibered. This leads to defining stacks as 2-sheaves: `Stacks(B,J) ⊂ FiberedCat(B)` full subcategory of fibred categories satisfying descent. Need `p.is_stack(J)`, `p.descent_data(U)`, `p.effective_descent(U) → E_b`.

Intended owners: `categories/cat/products.py` (`Cat` product `C×D` with `Ob×Ob`, `Hom×Hom`), `categories/cat/pullbacks.py` (`Cat` pullback `C×_E D` with `Ob(c,d,α)`, universal), `categories/fibered/fibered_categories.py` (`FiberedCategory p: E→B` with `cartesian_lift`, `fiber(b)`, `pullback_functor`), `categories/stacks/stacks.py` (`Stack` as fibered category satisfying effective descent for `J`, 2-sheaf, leading to algebraic stacks). Not a free `product_category(C,D)` returning tuple of objects — `C.product(D) → C×D : Cat` with `C×_E D` pullback and `p: E→B` fibered with cleavage and stacks as descent-satisfying fibred categories.

## Desired capability: `Top` and `Top_*`, `S = Spaces =` homotopy types `= ∞-groupoids` — note 2026-09-16

Need categories `Top` and `Top_*` (if not already present), and `S = Spaces =` homotopy types `= ∞-groupoids`.

* `Top : Cat` with `Ob(Top) =` topological spaces `X` (e.g. `Top` as convenient category of compactly generated weak Hausdorff or all spaces with `k`-ification), `Hom_Top(X,Y) = C^0(X,Y)` continuous maps with compact-open topology as `Top`-enriched `Hom`, composition via `∘`, identities `id_X`. Similarly `Top_* = Top_{*/}` pointed with `Ob(Top_*) = (X,x_0)` pointed spaces, `Hom_{Top_*}((X,x_0),(Y,y_0)) = { f: X→Y continuous | f(x_0)=y_0 }` basepoint-preserving, with smash `∧: Top_*×Top_*→Top_*` and wedge `∨`, and `Top_* = */Top` slice.

* `S = Spaces = ∞Grpd` is the `∞`-category of homotopy types / `∞`-groupoids, obtained as localization `S = Top[W^{-1}]` with `W =` weak homotopy equivalences `f: X→Y` inducing `π_n(f): π_n(X,x)→π_n(Y,f(x))` isomorphisms for all `n≥0`, `x∈X`, or equivalently `S ≃ sSet[W^{-1}]` with `W =` weak equivalences of simplicial sets, or `S ≃ CW[W^{-1}]` with `CW` finite CW complexes. As `∞`-category, `S ≃ ∞Grpd` via `X ↦ Π_∞(X) = Sing(X) : Kan` and `|-| : Kan → Top` adjunction `|-| ⊣ Sing` exhibiting `S` as `∞`-groupoids. Need `S` as `∞Cat` with `Ob(S) =` spaces up to weak equivalence, `Map_S(X,Y) = Map_Top(X,Y)` as `S` itself (mapping space), with `S` cartesian closed, `S` as `∞`-topos.

Intended owners: `categories/top/top.py` (`Top : Cat` with `Ob = TopSpaces`, `Hom = C^0`), `categories/top/pointed.py` (`Top_* : Cat` with `Ob = (X,x_0)`, `Hom_*`), `categories/spaces/spaces.py` (`S = Spaces = ∞Grpd : ∞Cat` with `S = Top[W^{-1}]`, `S ≃ sSet[W^{-1}]`, `S ≃ ∞Grpd` via `Sing/|-|`). Not a free `top_category()` returning list of spaces — `Top`, `Top_*`, `S` as categories/`∞`-categories with `Hom` as mapping spaces.

## Desired capability: simplicial complexes and Kan complexes operationalized — note 2026-09-16

Need simplicial complexes operationalized and specialize to Kan complexes.

* Simplicial complex `K` is finite (or locally finite) collection of simplices `σ ⊂ V` with `V : FiniteSets` vertices, closed under faces `τ⊂σ ⇒ τ∈K` and intersections `σ∩τ ∈ K` (or as `σ∈K`), with geometric realization `|K| : Top` via `|K| = (∐_{σ∈K} Δ^{|σ|-1})/∼` gluing along faces. Need `K : SimplicialComplexes` with `K.vertices() → V : FinSets`, `K.simplices() → {σ}`, `K.realization() → |K| : Top` and `K.chain_complex() → C_*(K)`.

* Kan complex specialization: `sSet : Cat` simplicial sets `X: Δ^{op}→Set` with `X_n` n-simplices, `Kan ⊂ sSet` full subcategory with `Kan` fibrancy: every horn `Λ^n_k → X` for `0≤k≤n`, `n≥1` extends to `Δ^n → X` (horn filler). Every `Sing(X)` for `X: Top` is Kan, and any `sSet` has fibrant replacement `Ex^∞(X) : Kan` via Kan's `Ex^∞` (or `Sing(|X|)`). Quillen model `sSet_{Quillen}` has `Kan` as fibrant objects, `W =` weak equivalences, `Cof =` monomorphisms, `Fib =` Kan fibrations. Need `KanComplex : sSet` with `Kan.is_kan()`, `Kan.horn_filler(Λ^n_k→Kan) → Δ^n→Kan`, and `X.kan_replacement() → Ex^∞(X) : Kan` with `X → Ex^∞(X)` weak equivalence. `SimplicialComplex` to `Kan` via `Sing(|K|)` or via `N_{simp}(K)` as `Kan` when ordered.

Intended owners: `categories/simplicial/complexes.py` (`SimplicialComplex` with `realization : Top`, `chain_complex`), `categories/simplicial/kan.py` (`KanComplex : sSet` with `horn_filler`, `kan_replacement = Ex^∞`), `categories/topology/simplicial_sets.py` (`sSet`, `Sing`, `|-|`, `Ex^∞`). Not a free `simplicial_complex(vertices)` returning list — `SimplicialComplex` as `Top` via `|K|` and `Kan` with horn fillers.

## Desired capability: categories from finitary data — graphs, posets, topologies — note 2026-09-16

Need to generalize to allow manually constructing categories from finitary data like graphs, posets, topologies on a space, etc.

* From directed graph `G = (V,E,s,t: E→V)` (finite `V,E : FinSets`), free category `FreeCat(G) : Cat` with `Ob = V`, `Hom_{FreeCat(G)}(x,y) =` paths `x = v_0 →^{e_1} v_1 → … →^{e_k} v_k = y` with `s(e_i)=v_{i-1}`, `t(e_i)=v_i`, composition via concatenation, identities as empty path at `v`. More generally `G` with relations `R ⊂ Mor(FreeCat(G))×Mor(FreeCat(G))` gives `Cat⟨G|R⟩ = FreeCat(G)/R`.

* From poset `P = (P,≤)` (finite `P : Posets`), poset category `PosCat(P) : Cat` already intaken with `Ob = P`, `Hom(x,y)=1` if `x≤y` else `∅`, composition via transitivity. This is thin skeletal.

* From topology `τ` on finite set `X` (finite `X : FinSets`, `τ ⊂ P(X)` topology with `∅,X∈τ`, closed under `∪,∩`), the specialization preorder `x ≤_τ y ⇔ x∈cl({y}) ⇔ every U∈τ with x∈U implies y∈U` gives poset `P_τ` when `τ` is `T_0` (or preorder otherwise), and `Top(X,τ) → Cat` via `PosCat(P_τ)` or via `Op(X) = (τ,⊆)` poset category of opens. More generally `X : Top` with finite `τ` as Alexandroff space gives `Cat` with `Ob = X` and `Hom(x,y)=1` if `x` specializes to `y`. Need `TopologyToCategory(X,τ) → Cat` with finite presentation.

* General finitary data `→ Cat` must be uniform: input `D : FinData` with `D.objects : FinSets` and `D.generators : FinSets` and `D.relations : FinSets`, output `Cat(D) : Cat` with finite `Ob` and `Hom` via generators and relations, computable via path concatenation modulo `R` (Knuth-Bendix when confluent). Need `Cat.from_graph(G) → FreeCat(G)`, `Cat.from_poset(P) → PosCat(P)`, `Cat.from_topology(X,τ) → TopCat(X,τ)` all as instances of `FinitaryCategory` construction.

Intended owners: `categories/cat/finitary.py` (`FinitaryCategory` from `D : FinData` with `Ob : FinSets`, `Hom` via generators/relations), `categories/graphs/free_category.py` (`FreeCat(G)` from graph `G`), `categories/posets/poset_category.py` (`PosCat(P)` already), `categories/topology/topology_to_category.py` (`TopCat(X,τ)` via `Op(X)` or specialization poset). Not a free `category_from_graph(graph)` returning dict — `Cat.from_graph(G) : Cat` with finite `Ob`/`Hom` via path category.

## Desired capability: (homotopy coherent) nerve of finitary category as Kan complex — note 2026-09-16

Need to express the (homotopy coherent) nerve of a relatively finitary category like any of these as an actual Kan complex that one can work with and compute with.

* Ordinary nerve `N(C) : sSet` for `C : Cat` (finitary with finite `Ob` and `Hom` via graph/poset/topology) has `N(C)_n = Fun([n],C)` with `[n] = 0→1→…→n` ordinal category, face `d_i` via composition at `i`, degeneracy `s_i` via identities. This is `N: Cat → sSet` fully faithful, `N(C)` is 2-coskeletal and weak Kan when `C` is groupoid, but not Kan in general. Need `C.nerve() → N(C) : sSet` with `N(C)_n` as `Set` of `n`-chains of composable morphisms, computable from finitary presentation via `Ob`, `Hom`, `∘`.

* Homotopy coherent nerve `N_{hc}(C) : sSet` for `C` enriched in `S` (`S`-enriched category, e.g. `S = Kan` or `S = Top` or `S = Cat`) has `N_{hc}(C)_n = Hom_{S-Cat}(\mathfrak{C}[n], C)` where `\mathfrak{C}[n]` is Boardman-Vogt resolution of `[n]` with `Hom_{\mathfrak{C}[n]}(i,j) =` nerve of poset of subsets `P_{i,j}` as `Kan` complex. When `C` is `S`-enriched with `S = Kan`, `N_{hc}(C)` is a quasicategory (`∞`-category), and when `C` is `∞`-groupoid enriched (i.e. `Kan`-enriched groupoid), `N_{hc}(C)` is Kan.

* For relatively finitary `C` (finite `Ob`, `Hom` finite via graph/poset/topology), the (homotopy coherent) nerve must be an actual `Kan` complex when `C` is groupoid/ Kan-enriched (e.g. `C = Π_1(X)` fundamental groupoid of finite `CW` with `Hom(x,y) =` paths up to homotopy as `Kan`, or `C = Op(X)` with `Hom` discrete as `Kan` via constant simplicial set, but `N(C)` then is not Kan unless `C` is groupoid — need fibrant replacement `Ex^∞(N(C)) : Kan` as `Kan` replacement. Need `C.homotopy_coherent_nerve() → N_{hc}(C) : sSet` and when `C` is suitably enriched (e.g. `S`-enriched with Kan mapping spaces), `N_{hc}(C)` is Kan with effective horn fillers via `C`'s composition and `Kan` fillers.

* Need actual Kan complex object one can work with and compute with: `Kan` with `Kan.horn_filler(Λ^n_k → Kan) → Δ^n → Kan` effective via `C`'s finitary `Hom` and via `Ex^∞` Kan replacement when not fibrant, with `Kan.simplices(n) → Kan_n : FinSets` when `C` finitary (finite `Ob`, `Hom` finite sets give finite `N(C)_n` for each `n` bounded). For `C` from graph/poset/topology with finite `Ob` and finite generating `Hom`, `N(C)_n` is finite for each `n` (composable chains), and `N_{hc}(C)_n` is finite `Kan` complex via `P_{i,j}` posets. Need `C.nerve_as_kan() → Kan` as `Kan` complex with `Kan_n` finite sets for bounded `n`, computable horn fillers via `C` presentation.

Intended owners: `categories/nerve/nerve.py` (`Nerve` `N(C) : sSet` with `N(C)_n = Fun([n],C)`), `categories/nerve/homotopy_coherent_nerve.py` (`HomotopyCoherentNerve` `N_{hc}(C) : sSet` with `Map(i,j) = Kan`), `categories/simplicial/kan.py` (`Kan` with `horn_filler`, `Ex^∞` fibrant replacement). Not a free `nerve_of_category(C)` returning list of simplices — `C.nerve() : sSet` and `C.homotopy_coherent_nerve() : Kan` with effective `Kan` structure.

## Desired capability: Lurie's tangent category, cotangent complex, obstruction theories, DGLAs, Sullivan minimal models — note 2026-09-16

Need Lurie's tangent category construction, the cotangent complex, classical obstruction theories, DGLAs, Sullivan minimal models.

* Lurie's tangent category `T_C : Cat` for `C : Cat` presentable (or for `X : C` with `C` presentable stable) is `T_C = Exc_*(S^{fin}_*, C)` excisive functors, or more concretely `T_X = Stab(C_{/X}) = Sp(C_{/X})` stabilization of slice `C_{/X}` as `Spectra` object, with `T_X → C_{/X}` via `Ω^∞`. For `C = CAlg_k`, `T_{A} = Mod_A` via `T_{CAlg_k, A} ≃ Mod_A` and cotangent complex `L_{A/k} : Mod_A` is image of `A ∈ CAlg_{k/A}`. More generally for `X : C`, `L_X : T_X` is the cotangent complex as suspension of diagonal. Need `T_C` as `Stab` and `L_X : T_X`.

* Cotangent complex `L_{X/Y} : T_X` for `X→Y` in `C` (e.g. `A→B` in `CAlg_k` gives `L_{B/A} : Mod_B` with `L_{B/A} ∈ D(B)` as `B`-module). For `A : CAlg_k` (simplicial commutative algebras), `L_{A/k}` controls deformations: `Map_{CAlg_k/A}(A, A⊕M) ≃ Map_{Mod_A}(L_{A/k}, M)` for `M : Mod_A`. Classical `L_{B/A}` for ordinary rings is truncation `τ_{\le0} L_{B/A}^{der}`. Need `X.cotangent_complex() → L_X : T_X` with `L_{B/A}` via Kähler `Ω_{B/A}` when `B = A[x_1,…,x_n]/(f_j)` and resolution.

* Classical obstruction theories: for `X : Schemes` (or `Artin stacks`), perfect obstruction theory `E → L_X` with `E : Perf(X)` perfect complex `[-1,0]` and `h^0(E) ≅ h^0(L_X)`, `h^{-1}(E) → h^{-1}(L_X)` surjective, giving virtual class `[X]^{vir} ∈ A_*(X)` and obstruction `o ∈ Ext^1(L_X, I)` for deformations of maps `Spec A → X` to `Spec A' → X` with square-zero `I`. DGLA `g` governs deformations via Maurer-Cartan `MC(g) = { x∈g^1 | dx + ½[x,x]=0 }/ gauge`, with `g = RHom(E, O_X)` etc. Need `E.obstruction_theory() → (E→L_X)` and `g = RHom`.

* DGLAs and Sullivan minimal models: DGLA `g = ⊕_{i∈ZZ} g^i` with `d: g^i→g^{i+1}`, `[ -,- ]: g^i⊗g^j→g^{i+j}` graded Lie with Jacobi and `d[x,y]=[dx,y]+(-1)^{|x|}[x,dy]`, Maurer-Cartan `MC(g)`, gauge `exp(g^0)`. Sullivan minimal model `M_X = (ΛV, d) → A_{PL}(X)` for `X : Top_{nil}` nilpotent finite-type with `V = ⊕_{n≥1} V^n` graded `V^n ≅ Hom(π_n(X),Q)`, `d(V)⊂Λ^{≥2}V` decomposable, `ΛV` free graded-commutative, `M_X → A_{PL}(X)` quasi-isomorphism minimal. Need `DGLA` as `LieAlg(Ch)` and `SullivanMinimalModel(X) → (ΛV,d)` with `V^n`.

Intended owners: `categories/tangent/tangent_category.py` (`T_C = Stab(C_{/X})`, `T_X`), `categories/deformation/cotangent_complex.py` (`L_{X/Y} : T_X` with `L_{A/k}`), `categories/deformation/obstruction_theories.py` (`E→L_X` perfect, `o∈Ext^1`), `categories/dgla/dglas.py` (`DGLA` with `MC`), `categories/rational/sullivan.py` (`SullivanMinimalModel` `M_X=(ΛV,d)`). Not a free `cotangent_complex(X)` returning matrix — `X.cotangent_complex() : T_X` with `L_{A/k}`.

## Desired capability: Yoneda and coYoneda, Mor, functor of points — note 2026-09-16

Need the Yoneda and coYoneda embeddings for any category sending objects to honest functors, operationalizing `Mor(*,*)` as a functor from an honest product category `C×C^{op}` which admits currying arguments to produce the above functors.

* For any `C : Cat`, Yoneda embedding `y: C → Fun(C^{op},Set)` sending `c ↦ y(c) = Hom_C(-,c) : C^{op}→Set` with `y(c)(d)=Hom_C(d,c)` and `y(f: c→c')_d = f∘- : Hom(d,c)→Hom(d,c')`, fully faithful via Yoneda lemma `Nat(y(c),F) ≅ F(c)`. CoYoneda `y^{co}: C^{op} → Fun(C,Set)` with `y^{co}(c)=Hom_C(c,-)`. Need `C.yoneda() → y : C → Fun(C^{op},Set)` and `C.coyoneda() → y^{co}` as honest functors `C → Fun(C^{op},Set)` and `C^{op} → Fun(C,Set)`, not as ad-hoc `Hom` functions.

* Operationalize `Mor := Hom_C(-,-): C^{op}×C → Set` as functor from honest product category `C^{op}×C : Cat` with `Ob = Ob(C)×Ob(C)`, `Hom((a,b),(a',b')) = Hom_{C^{op}}(a,a')×Hom_C(b,b') = Hom_C(a',a)×Hom_C(b,b')` via product `C×C^{op}` already intaken, with `Mor(a,b)=Hom_C(a,b)`, `Mor(f: a'→a, g: b→b') = g∘-∘f : Hom(a,b)→Hom(a',b')`. Need `C.mor_functor() → Mor: C^{op}×C → Set` as `Fun(C^{op}×C,Set)` with `Mor(a,b)=Hom_C(a,b)`.

* Currying: `Hom_{Fun(C^{op},Set)}(y(c), F) ≅ F(c)` is currying of `Mor`. More generally `Fun(C^{op}×C,Set) ≅ Fun(C, Fun(C^{op},Set))` via currying `F ↦ (c ↦ F(-,c))` and `Fun(C^{op}, Fun(C,Set))`. So `Mor: C^{op}×C→Set` curries to `y: C→Fun(C^{op},Set)` via `y(c)=Mor(-,c)` and to `y^{co}: C^{op}→Fun(C,Set)` via `y^{co}(c)=Mor(c,-)`. Need `Mor.curry() → y` and `Mor.curry_op() → y^{co}` as functors, with `y(c).evaluated_at(d)=Mor(d,c)`.

* Functor of points `h_X` for any object in any category: for `C : Cat` and `X : C`, `h_X = Hom_C(-,X) = y(X) : C^{op}→Set` is the functor of points, with `h_X(Y)=Hom(Y,X)`, `h_X(f: Y'→Y)= -∘f`. This is the Yoneda image `y(X)`. Need `X.functor_of_points() → h_X : Fun(C^{op},Set)` with `h_X = y(X)`, and `h^X = Hom(X,-) : Fun(C,Set)` co-points. For `C = Sch`, `h_X` is the usual `Sch`-valued functor of points `h_X(T)=Hom(T,X)`.

Intended owners: `categories/yoneda/yoneda.py` (`Yoneda` `y: C→Fun(C^{op},Set)`), `categories/yoneda/coyoneda.py` (`CoYoneda` `y^{co}: C^{op}→Fun(C,Set)`), `categories/hom/mor_functor.py` (`Mor: C^{op}×C→Set` from honest `C×C^{op}` with currying `Mor.curry()→y`), `categories/functor_of_points.py` (`h_X = Hom(-,X) : C^{op}→Set` for any `X:C`). Not a free `yoneda_embedding(C)` returning dict of Homs — `C.yoneda() : C → Fun(C^{op},Set)` with `Mor: C^{op}×C→Set` from product `C×C^{op}` and currying.

## Desired capability: abelianization, centers, centralizers, stabilizers, Hurewicz — note 2026-09-16

Need abelianization of a group, center of a group, centralizers and stabilizers for groups, centers for rings, the Hurewicz morphism(s).

* Abelianization of a group `G : Groups` is `Ab(G)=G^{ab}=G/[G,G] : AbGroups` with quotient `π: G→G^{ab}` universal for maps to abelian groups: for any `A : AbGroups` and `f: G→A`, there is unique ` \bar f: G^{ab}→A` with `f = \bar f∘π`. This is left adjoint `Ab ⊣ Incl: AbGroups → Groups`. Need `G.abelianization() → G^{ab} : AbGroups` with `G.abelianization_map() → π: G→G^{ab}` and adjunction `Hom_{Ab}(G^{ab},A) ≅ Hom_{Groups}(G,A)`.

* Center of a group `Z(G) = { g∈G | ∀h∈G, gh=hg } ⊲ G` as normal subgroup `Z(G) ≤ G` with `Z(G) = ker(G → Aut(G), g↦conj_g)` where `conj_g(h)=ghg^{-1}`. Centralizer of `S⊂G` is `C_G(S) = { g∈G | ∀s∈S, gs=sg } ≤ G`, with `C_G(S)=∩_{s∈S} C_G({s})`, and `Z(G)=C_G(G)`. Stabilizer for `G↷X` action `a: G×X→X` and `x∈X` is `Stab_G(x) = { g∈G | g·x = x } ≤ G` with `G·x ≅ G/Stab_G(x)` as `G`-set. Need `G.center() → Z(G) : Sub(G)`, `G.centralizer(S) → C_G(S)`, `G.stabilizer(x) → Stab_G(x)` for `G`-set `X`.

* Centers for rings `R : Rings` (associative, possibly non-commutative) is `Z(R) = { r∈R | ∀s∈R, rs=sr } ≤ R` as subring `Z(R) : Rings` commutative, with `Z(R) = End_{R⊗R^{op}}(R)` as bimodule endomorphisms. For `R : CommRings`, `Z(R)=R`. Need `R.center() → Z(R) : Rings`.

* Hurewicz morphism(s) `h_n: π_n(X,x) → H_n(X;ZZ)` for `X : Top_*` pointed connected (or `X : CW`) with `π_n = [S^n,X]_*` and `H_n = H_n^{sing}(X;ZZ)` via `H_n : GrMod`, induced by `π_n(X) → π_n(X,X^{n-1}) ≅ H_n(X^n,X^{n-1}) → H_n(X)` or via `h_n([f]) = f_*[S^n]` with `f: S^n→X` and `[S^n]∈H_n(S^n)`. Stable Hurewicz `h^s_n: π_n^s(X) → H_n(X)` similarly. Need `X.hurewicz(n) → h_n: π_n(X)→H_n(X)` as `Groups→Ab` morphism with `h_n` natural in `X` and `h_1 : π_1^{ab} ≅ H_1` isomorphism (Hurewicz theorem for 1-connected `X` with `π_i=0` for `i<n` gives `h_n` iso).

Intended owners: `categories/groups/abelianization.py` (`Ab(G)=G/[G,G]` with `π: G→G^{ab}`), `categories/groups/center.py` (`Z(G)`, `C_G(S)`, `Stab_G(x)`), `categories/rings/center.py` (`Z(R)`), `categories/homotopy/hurewicz.py` (`Hurewicz` `h_n: π_n→H_n` with `h_1^{ab}`). Not a free `abelianization(G)` returning quotient list — `G.abelianization() : AbGroups` with `G.center() : Sub(G)` and `X.hurewicz(n) : π_n→H_n`.

## Desired capability: implicitly deriving tensor and hom, tensor-hom and power/copowering adjunctions, enriched, induction/restriction — note 2026-09-16

Need implicitly deriving as much as possible, especially tensor and hom, tensor-hom adjunction, and more general power/copowering adjunctions, attaching enriched structures where they are known to hold by theorems, induction and restriction functors for `k[G]` modules / `G`-reps (Frobenius reciprocity).

* Implicitly deriving means for `C : Cat` with weak equivalences `W` (e.g. `Ch(R)`, `sSet`, `Top`, `Mod_R`), derive functors `L F : Ho(C) → Ho(D)` and `R G : Ho(C) → Ho(D)` automatically where `F ⊣ G` Quillen or where `C` has enough projectives/injectives, without hand-written `L⊗` per case. Especially `⊗ : C×C→C` and `Hom: C^{op}×C→C` derive to `⊗^L : Ho(C)×Ho(C)→Ho(C)` and `RHom: Ho(C)^{op}×Ho(C)→Ho(C)` as `Ho(C)`-enriched, with `L(⊗) = ⊗^L` and `R(Hom)=RHom`. Need `C.implicitly_derive(F) → LF` or `RF` via cofibrant/fibrant replacement `Q,R`.

* Tensor-hom adjunction `Hom(X⊗Y,Z) ≅ Hom(X,Hom(Y,Z))` as `Set` iso natural in `X,Y,Z` for closed monoidal `C` with `⊗ : C×C→C` left adjoint to `Hom: C^{op}×C→C` on each variable: ` -⊗Y ⊣ Hom(Y,-)` with counit `ev: Hom(Y,Z)⊗Y→Z` and unit `coev: X→Hom(Y,X⊗Y)`. Derived version `RHom(X⊗^L Y,Z) ≅ RHom(X,RHom(Y,Z))` in `Ho(C)`. More generally power `X^K` and copower `K·X` for `K : S` (`S = Set, sSet, Spaces`) with adjunctions `Hom(K·X,Y) ≅ Hom(K,Map(X,Y)) ≅ Hom(X,Y^K)` for `C` tensored/cotensored over `S`.

* Power/copowering adjunctions: for `C` enriched over `V` and tensored/copowered over `V` (e.g. `sSet` over `Set`, `Top` over `S`, `Ch(R)` over `Ch(ZZ)`), power `X^K : C` cotensor and copower `K·X : C` tensor over `K : V` with `Map(K·X,Y) ≅ Map(K,Map(X,Y)) ≅ Map(X,Y^K)` in `V`. Need `C.power(K,X) → X^K` and `C.copower(K,X) → K·X` with adjunctions.

* Attaching enriched structures where they are known to hold by theorems: e.g. `Top` is `S`-enriched via `Map(X,Y)∈S`, `Cat` is `Cat`-enriched (2-category) via `Fun(C,D)`, `sSet` is `sSet`-enriched, `Ch(R)` is `Ch(R)`-enriched, `Spectra` is `Spectra`-enriched, etc. Need `C.enrichment() → V` and `C.enriched_hom(X,Y) → Map_C(X,Y) : V` when theorem holds (e.g. `Top` is cartesian closed and `S`-enriched, `Cat` is cartesian closed as 2-category).

* Induction and restriction functors for `k[G]` modules / `G`-reps (Frobenius reciprocity): for `H ≤ G` groups and `k : CommRings`, restriction `Res^G_H: k[G]-Mod → k[H]-Mod` via `k[H]→k[G]` and induction `Ind_H^G = k[G]⊗_{k[H]} - : k[H]-Mod → k[G]-Mod` left adjoint to `Res`, with Frobenius reciprocity `Hom_{k[G]}(Ind_H^G V,W) ≅ Hom_{k[H]}(V,Res_H^G W)` natural, and `CoInd_H^G = Hom_{k[H]}(k[G],-) : k[H]-Mod → k[G]-Mod` right adjoint to `Res` with `Hom_{k[H]}(Res V,W) ≅ Hom_{k[G]}(V,CoInd W)`. Similarly for `G`-reps `Rep_k(G) = k[G]-Mod` with same. Need `Res_H^G`, `Ind_H^G`, `CoInd_H^G` with adjunctions.

Intended owners: `categories/derived/implicit_deriving.py` (`ImplicitlyDerive` `LF`, `RF` for `⊗, Hom`), `categories/monoidal/tensor_hom.py` (`TensorHomAdj` `Hom(X⊗Y,Z)≅Hom(X,Hom(Y,Z))`), `categories/enriched/power_copower.py` (`Power` `X^K`, `Copower` `K·X`), `categories/enriched/enriched.py` (`EnrichedCategory` with `Map`), `categories/representation/induction_restriction.py` (`Res^G_H`, `Ind_H^G ⊣ Res`, `FrobeniusReciprocity`). Not a free `derive_tensor(X,Y)` returning list — `C.derived_tensor(X,Y) → X⊗^L Y` with `RHom` and adjunctions.

## Desired capability: axiomatic subcategories of `Cat`, `show(C)`, limits/colimits, monads, `QX`, interchange — note 2026-09-16

Need existing categories placed into axiomatic subcategories of `Cat`: Abelian, Complete, Cocomplete, Bicomplete, HasProducts, HasCoproducts, HasPullbacks, etc., enrich `show(C)` to display known properties like this so that they can be seen and audited by users, reasonable computational abilities of limits and colimits at least in filtered or `ZZ`-indexed cases; equalizers and coequalizers, etc., monads, algebras over monads, `QX` for a topological space, basic interchange for limit/colimit calculus.

* Place existing categories `C : Cat` into axiomatic subcategories of `Cat` via `C ∈ Abelian`, `C ∈ Complete`, `C ∈ Cocomplete`, `C ∈ Bicomplete`, `C ∈ HasProducts`, `C ∈ HasCoproducts`, `C ∈ HasPullbacks`, `C ∈ HasPushouts`, `C ∈ HasEqualizers`, `C ∈ HasCoequalizers`, `C ∈ CartesianClosed`, etc., as `Cat` with axiom `with_axiom(HasProducts)` etc. Need `C.is_abelian()`, `C.is_complete()`, `C.has_products()` as predicates via `C ∈ Cat_{Abelian}` etc., not as separate `has_products(C)` functions.

* Enrich `show(C)` to display known properties like this so that they can be seen and audited by users: `C.show()` or `show(C)` in REPL/notebook must display `C` with its `Cat` axioms (`Abelian`, `Complete`, `HasProducts`, …) as tags, e.g. `Abelian(C) = AbGroups` shows `Abelian, Complete, Cocomplete, HasLimits, HasColimits`, so users can audit which `Cat` axioms a category satisfies.

* Reasonable computational abilities of limits and colimits, at least in filtered or `ZZ`-indexed cases; equalizers and coequalizers, etc.: `lim: Fun(I,C)→C` for `I : Cat` small, with `lim_I : Fun(I,C)→C` right adjoint to `diag: C→Fun(I,C)`, and `colim: Fun(I,C)→C` left adjoint. Need at least filtered colimits `colim_{i∈I}` with `I` filtered (`ZZ`-directed `I = ZZ` with `i≤j` gives `ZZ`-indexed `colim_{n∈ZZ} X_n` as sequential colimit, similarly `lim_{n∈ZZ} X_n` for `ZZ^{op}`-indexed inverse limit), and equalizers `Eq(f,g) = lim( X ⇉ Y )` for `f,g: X→Y` and coequalizers `Coeq(f,g) = colim( X ⇉ Y )`, with products `X×Y = lim(X→1←Y)` and coproducts `X⊕Y = colim(1←0→1)` etc. Need `C.limit(diagram) → lim_I F : C` with universal cone `lim → F(i)` and `C.colimit(diagram) → colim_I F` when `I` filtered or `ZZ`.

* Monads, algebras over monads: monad `T: C→C` with `η: Id_C → T`, `μ: T^2 → T` satisfying `μ∘Tη = id = μ∘ηT` and `μ∘Tμ = μ∘μT`, and `T`-algebras `Alg_T` with `Ob = (X, a: TX→X)` with `a∘η_X = id_X`, `a∘μ_X = a∘T(a)`, morphisms `f: (X,a)→(Y,b)` with `f∘a = b∘T(f)`. Examples: `List` monad on `Set`, `FreeGroup` on `Set`, `Free_R-Mod` on `Set`, `Powerset` monad, etc. Need `Monad(T,η,μ)` and `C.algebras(T) → Alg_T : Cat` with forgetful `U: Alg_T→C` and free `F: C→Alg_T`.

* `QX` for a topological space `X : Top`: e.g. `QX = Ω^∞Σ^∞ X = colim_n Ω^n Σ^n X` as stabilization `Q = Ω^∞Σ^∞ : Top→Top` with `QX` the free infinite loop space on `X`, or `QX` as `Q-construction` for `K`-theory, or `QX` as rationalization depending on context. In this intake, `QX` is the `Q`-construction for `X : Top` as `QX = Ω^∞Σ^∞ X` (or `B^{∞}X` for `X` connected), with `Q: Top → Top` monad `X ↦ QX` and `QX ≃ colim_{n} Ω^n Σ^n X` via `Σ ⊣ Ω`. Need `X.Q() → QX : Top` with `QX = colim_n Ω^n Σ^n X`.

* Basic interchange for limit/colimit calculus: moving through `Hom` arguments, commuting with adjoints, etc.: `Hom_C(lim_i X_i, Y) ≅ lim^{op}_i Hom_C(X_i,Y)` (limit in first variable becomes colimit), `Hom_C(X, lim_i Y_i) ≅ lim_i Hom_C(X,Y_i)`, `Hom_C(colim_i X_i, Y) ≅ lim_i Hom_C(X_i,Y)`, `Hom_C(X, colim_i Y_i) ≅ colim_i Hom_C(X,Y_i)` when `X` compact, and `L ⊣ R` gives `L(colim_i X_i) ≅ colim_i L(X_i)` and `R(lim_i X_i) ≅ lim_i R(X_i)` (left adjoints preserve colimits, right adjoints preserve limits), Fubini `lim_i lim_j X_{i,j} ≅ lim_{i,j} X_{i,j} ≅ lim_j lim_i X_{i,j}` and `colim_i colim_j ≅ colim_{i,j}`, and `lim`/`colim` commute with `×` when `C` has appropriate limits. Need `Hom(lim, -)`, `Hom(-, lim)`, `L(colim)`, `R(lim)` interchanges.

Intended owners: `categories/cat/axioms.py` (`CatAxioms` `Abelian`, `Complete`, `Cocomplete`, `HasProducts`, etc.), `categories/cat/show.py` (`show(C)` displaying `Cat` axioms), `categories/limits/filtered.py` (`FilteredColimit` `colim_{i∈I}` for `I` filtered/`ZZ`), `categories/limits/equalizers.py` (`Equalizer` `Eq(f,g)`, `Coequalizer` `Coeq(f,g)`), `categories/monads/monads.py` (`Monad` `T: C→C` with `η,μ` and `Alg_T`), `categories/top/qx.py` (`QX = Ω^∞Σ^∞ X` for `X : Top`), `categories/limits/interchange.py` (`Interchange` `Hom(lim, -) ≅ lim Hom`, `L(colim) ≅ colim L`). Not a free `limit_of_diagram(diagram)` returning list — `C.limit(I, F: I→C) → lim_I F : C` with `lim` as right adjoint to `diag` and `show(C)` displaying axioms.

## Desired capability: attaching homological notions to modules — free resolutions then apply functor and take homology for derived functors — note 2026-09-16

Attaching homological notions to modules. Operationalize taking a free resolution and applying a functor and taking homology in order to compute derived functors.

* For `R : Rings` (commutative `R : CommRings` or general) and `M : R-Mod`, attach homological notions `Tor^R_n(M,N)`, `Ext^n_R(M,N)`, `L_nF(M)`, `R^nF(M)` as objects `L_nF(M) : R-Mod` or `Ab` with `L_nF(M) = H_n(F(P_•))` etc., as graded `H_* : GrMod` with `H_*.graded_piece(n)=H_n`. The notions are attached to the module `M`, not as free `Tor(M,N)` functions returning numbers.

* Operationalize via free (or projective) resolution `P_• → M → 0` with `P_• : Ch(R-Mod)` and `P_i` free finite rank (or `P_i = R^{b_i}`) with differential `d_i: P_i → P_{i-1}` and augmentation `ε: P_0 → M` exact: `… → P_1 →^{d_1} P_0 →^{ε} M → 0` and `H_i(P_•)=0` for `i>0`, `H_0(P_•) ≅ M`. Need `M.free_resolution() → P_• : Ch` with `P_i` free, `P_•.augmentation() → M`, and `P_•.is_exact()`.

* Then apply functor `F : R-Mod → Ab` (or `R-Mod → R-Mod`, `R-Mod → D(Ab)`) — e.g. `F = Hom_R(-,N)` contravariant, `F = -⊗_R N` covariant, `F = Hom_R(P,-)`, `F = G∘F` etc. — to `P_•` (or to `P_•` without augmentation) to get complex `F(P_•) : Ch(Ab)` with `F(P_•)_n = F(P_n)` and differential `F(d_n): F(P_n) → F(P_{n-1})` (or `F(d^n)` for contravariant with degree shift). Then take homology `H_n(F(P_•)) = ker F(d_n) / im F(d_{n+1}) : Ab` as `GrMod` graded `H_*(F(P_•)) : GrMod` with `H_*.graded_piece(n)=H_n`. For left exact `F` (e.g. `Hom_R(-,N)`), this computes right derived `R^nF(M) = H^n(F(P_•))` after appropriate `Hom` and `Ext^n_R(M,N) = H^n(Hom_R(P_•,N))`; for right exact `F` (e.g. `-⊗_R N`), this computes left derived `L_nF(M)=H_n(F(P_•))` and `Tor_n^R(M,N)=H_n(P_•⊗_R N)`.

* This is the standard free-resolution model for derived functors: `L_nF(M) = H_n(F(P_•))` with `P_• → M` free resolution, and `R^nF(M) = H^n(F(I^•))` for injective `I^•` when needed, but the operationalized version requested is free resolution + apply `F` + take homology. Need `M.derived_functor(F, n) → H_n(F(P_•)) : Ab` with `P_• = M.free_resolution()`, `F(P_•) : Ch`, `H_n : GrMod`. For `F = -⊗_R N`, this is `Tor_n^R(M,N)`; for `F = Hom_R(-,N)`, this is `Ext^n_R(M,N)` as `Ext^n = R^n Hom`.

* Interface must be on the module with its resolution: `M.free_resolution() → P_• : Ch(R-Mod)` with `P_i` free, `M.apply_functor_to_resolution(F) → F(P_•) : Ch`, `H_n(F(P_•)) → L_nF(M) : Ab` as `GrMod`. For `F = Hom_R(-,N)`, `M.ext(N,n) → Ext^n_R(M,N) = H^n(Hom_R(P_•,N))`; for `F = -⊗_R N`, `M.tor(N,n) → Tor_n^R(M,N) = H_n(P_•⊗_R N)`. The free resolution is the computational engine; the derived functor is the homology of the resulting complex.

Intended owners: `categories/modules/homological.py` (`HomologicalNotions` attached to `M : R-Mod` with `Tor`, `Ext`, `L_nF`), `categories/homological/free_resolutions.py` (`FreeResolution` `P_• → M` with `P_i` free, `M.free_resolution() → P_•`), `categories/derived/derived_functors.py` (`DerivedFunctor` `L_nF(M)=H_n(F(P_•))`, `R^nF(M)=H^n(F(P_•))`), `categories/modules/free_modules.py` (`FreeFiniteRank` with `basis`). Not a free `free_resolution(M)` returning list of matrices — `M.free_resolution() : Ch` with `P_•` as complex of free modules and `H_n(F(P_•)) : GrMod` as derived functor.

## Desired capability: Yoneda product on `Ext` operationalized — note 2026-09-16

Operationalize Yoneda product on `Ext`.

* Yoneda product is not a formal `Ext^p⊗Ext^q→Ext^{p+q}` symbol. For `R : Rings` (or `R : CommRings`) and `A,B,C : R-Mod` (or `D(R-Mod)`), the product
  ```
  Yoneda: Ext^p_R(B,C) ⊗ Ext^q_R(A,B) → Ext^{p+q}_R(A,C)
  ```
  is composition in the derived category `D(R-Mod)` via `Ext^n_R(A,B) = Hom_{D(R)}(A, B[n])` (`B[n]` shift). Explicitly, for `ξ ∈ Ext^p(B,C)` represented by `ξ: B → C[p]` in `D(R)` and `η ∈ Ext^q(A,B)` represented by `η: A → B[q]`, the Yoneda product is `ξ·η = (ξ[q] ∘ η) : A → C[p+q]` where `ξ[q]: B[q] → C[p+q]` is shift of `ξ`. Equivalently via extensions, `ξ` is `0→C→E_1→…→E_p→B→0` and `η` is `0→B→F_1→…→F_q→A→0`, splice at `B` to `0→C→E_1→…→E_p→F_1→…→F_q→A→0` of length `p+q`, modulo Yoneda equivalence (pushout/pullback). Need `Ext^p ⊗ Ext^q → Ext^{p+q}` as `R-Mod` morphism with `p,q : NN`.

* Operationalize via free resolutions and chain maps: choose free resolution `P_• → A →0` with `P_i` free finite rank, then `Ext^q_R(A,B) = H^q(Hom_R(P_•,B))` with cocycle `f: P_q → B` representing class, similarly `Q_• → B` for `Ext^p(B,C)`. Lift `f` to chain map `F_•: P_{•+q} → Q_•` covering `f: P_q → B`, then compose with `g: Q_p → C` representing `Ext^p` to get `g∘F_q: P_{p+q} → C` representing `Yoneda(g,f) ∈ Ext^{p+q}(A,C)`. Concretely via `RHom_R(A,B) = Hom_R(P_•,B) : Ch` and composition `RHom(B,C) ⊗^L RHom(A,B) → RHom(A,C)` as chain map composition.

* Graded structure: `Ext^*_R(A,B) = ⊕_{n≥0} Ext^n_R(A,B) : GrMod` with `Ext^n.graded_piece(n)=Ext^n` and Yoneda product makes `Ext^*_R(A,A) : GrAlg` graded `R`-algebra with `Ext^p⊗Ext^q→Ext^{p+q}` and `Ext^0(A,A)=Hom_R(A,A)`, and `Ext^*_R(A,B)` as graded `Ext^*(A,A)`-module. Similarly `Tor_*` has shuffle product.

* Interface must be on the modules with resolutions: `A.ext(B,q) → Ext^q_R(A,B) : R-Mod` as `Hom_{D(R)}(A,B[q])`, `B.ext(C,p) → Ext^p_R(B,C)`, then `Ext^p(B,C).yoneda_product(Ext^q(A,B)) → Ext^{p+q}(A,C) : R-Mod` with `Ext^p.graded_piece` compatibility, and `RHom_R(A,B) ⊗ RHom_R(B,C) → RHom_R(A,C)` via composition. For `F = Hom_R(P_•,-)` and `F = -⊗_R N`, Yoneda product is induced by `Hom` composition and `⊗^L` shuffle.

Intended owners: `categories/homological/yoneda_product.py` (`YonedaProduct` `Ext^p(B,C)⊗Ext^q(A,B)→Ext^{p+q}(A,C)` via `Hom_{D(R)}(B,C[p])⊗Hom_{D(R)}(A,B[q])→Hom_{D(R)}(A,C[p+q])`, splice, chain maps), `categories/derived/derived_category.py` (`D(R-Mod)` with `Hom(A,B[n])=Ext^n`), `categories/homological/ext_tor.py` (`Ext^n`, `Tor_n`), `categories/homological/free_resolutions.py` (`P_•→A` with `Hom(P_•,B)`). Not a free `yoneda_product(ext1, ext2)` returning list — `Ext^p(B,C).yoneda(Ext^q(A,B)) → Ext^{p+q}(A,C)` on the `Ext` graded objects with `RHom` composition.

## Desired capability: `MU` and `BP`, spectra, `E_n` and `A_n` ring spectra, free `E_n` algebras — note 2026-09-16

Operationalize `MU` and `BP`, spectra, `E_n` ring spectra, `E_n` module spectra, `A_n` ring spectra, free `E_n` algebra functors.

* Spectra `Sp : Cat` as stable `∞`-category `Sp = Sp(Top_*) = lim(… → Top_* →^{Σ} Top_* →^{Σ} …)` or as `Spectra` sequential spectra `X = (X_n, σ_n: ΣX_n → X_{n+1})` with `X_n : Top_*`, `Ω`-spectra when `σ_n^♭: X_n → ΩX_{n+1}` is weak equivalence, with smash `∧: Sp×Sp→Sp` and `S = Σ^∞ S^0` sphere spectrum. Need `Sp` as stable `∞Cat` with `Σ ⊣ Ω` as `Σ^∞ ⊣ Ω^∞` and `Sp` is `∞`-categorical stabilization of `S`.

* `MU = Thom(MU)` complex cobordism as `E_∞` ring spectrum `MU = colim_n Thom(BU(n))` with `MU_* = π_*(MU) = ZZ[x_1,x_2,…]` `|x_i|=2i` (`x_i = [CP^i]`), Thom spectrum `MU = Thom(BU → BO)` via `J: BO→BGL_1(S)`. Similarly `BP` at prime `p` is summand of `MU_{(p)}` via Quillen idempotent `e: MU_{(p)} → MU_{(p)}` with `e^2=e` and `BP = e MU_{(p)}` as `p`-local `E_∞` (or `E_4`) ring spectrum with `BP_* = ZZ_{(p)}[v_1,v_2,…]` `|v_i|=2(p^i-1)` and `BP_*BP = BP_*[t_1,t_2,…]`. Need `MU : CAlg(Sp)` and `BP : CAlg(Sp)_{(p)}` with `MU_*`, `BP_*`.

* `E_n` ring spectra as `E_n`-algebras in `Sp` for `E_n` operad (`n = 1` associative `A_∞`, `n = ∞` `E_∞` commutative): `Alg_{E_n}(Sp)` with `E_n`-operad `E_n(k) ≃ Conf_k(R^n)` little `n`-cubes, `A : Alg_{E_n}(Sp)` has multiplications `E_n(k) ⊗ A^{⊗k} → A`. `E_n` ring spectrum `R` is `R : Alg_{E_n}(Sp)` with `π_*(R)` graded ring. Example `MU` is `E_∞`, `BP` is `E_4` (or `E_∞` for `p>2` recent), Morava `E_n` is `E_∞`. `E_n` module spectra `Mod_{E_n}(Sp)` is `Mod_R = Fun_{E_n}(R, Sp)` with `R-Mod` stable. Need `E_n`-algebras and modules as `Alg_{E_n}(Sp)` and `Mod_R`.

* Free `E_n` algebra functors `Free_{E_n}: Sp → Alg_{E_n}(Sp)` left adjoint to forgetful `U: Alg_{E_n}→Sp`, with `Free_{E_n}(X) = ∐_{k≥0} E_n(k) ⊗_{Σ_k} X^{⊗k}` as `∐ E_n(k) ×_{Σ_k} X^{∧k}` in `Sp`, and `Free_{E_n}(S^0) ≃ ∐_{k} BΣ_k` etc. For `n=∞`, `Free_{E_∞}(X) ≃ Sym^*(X) = ∐_{k} X^{∧k}_{hΣ_k}`. `A_n` ring spectra are `A_n`-algebras for `A_n` operad (`A_n(k)=*` for `k≤n` else `∅`, with `A_∞ = E_1`).

Intended owners: `categories/spectra/spectra.py` (`Sp` as `Spectra` stable `∞`-category), `categories/spectra/mu.py` (`MU : CAlg(Sp)` with `MU_*`), `categories/spectra/bp.py` (`BP : CAlg(Sp)_{(p)}` with `BP_*`), `categories/spectra/e_n_ring.py` (`E_n`-algebras `Alg_{E_n}(Sp)`), `categories/spectra/e_n_modules.py` (`E_n`-modules `Mod_R`), `categories/spectra/free_e_n.py` (`Free_{E_n}: Sp → Alg_{E_n}`), `categories/spectra/a_n.py` (`A_n`-algebras). Not a free `e_n_algebra(X)` returning list — `Free_{E_n}(X) : Alg_{E_n}(Sp)` with `E_n(k)⊗_{Σ_k} X^{⊗k}`.

## Desired capability: Morava `K(n)` and `K(n)`-local spheres, heights, `p`-local/`p`-complete, fibers/cofibers in spectra — note 2026-09-16

Operationalize Morava `K(n)` and `K(n)`-local spheres, `p`-local and `p`-complete spheres, and more generally fibers and cofibers in spectra. Heights of Morava `E`-theories.

* Morava `K(n)` at prime `p` height `n` is `K(n)` as `E_∞` (or `A_∞`) ring spectrum with `K(n)_* = F_p[v_n^{±1}]` `|v_n|=2(p^n-1)` and `K(n)^* K(n) =` Morava stabilizer etc., with `K(0)=Q`, `K(∞)=F_p`. `K(n)`-localization `L_{K(n)}: Sp → Sp_{K(n)}` is Bousfield localization at `K(n)` with `L_{K(n)}X` initial `K(n)`-local under `X→L_{K(n)}X` with `K(n)_*(X→L_{K(n)}X)` iso, and `K(n)`-local sphere `L_{K(n)}S^0` as `L_{K(n)}` of sphere `S^0`. Height `n = ht(E)` for Morava `E = E_n = E(k,Γ)` Lubin-Tate spectrum `E_* = W(k)[[u_1,…,u_{n-1}]][u^{±1}]` with `|u|=-2`, `|u_i|=0`, height `n` of formal group `Γ` over `k : Fields` char `p`.

* `p`-local sphere `S^0_{(p)} = L_{M(p)}S^0` localization at `M(p)=S/p` Moore spectrum, and `p`-complete sphere `S^0^{∧}_p = lim_k S^0/p^k = L_{S/p}S^0` as `p`-completion `X^{∧}_p = lim_k X/p^k` with `X/p^k = cofib(X →^{p^k} X)`. More generally `L_{S/p}` Bousfield at `S/p`. Need `S^0_{(p)} : Sp` and `S^0^{∧}_p : Sp` with `π_*(S^0_{(p)}) = ZZ_{(p)}` etc.

* Fibers and cofibers in spectra more generally: for `f: X→Y` in `Sp`, fiber `fib(f) = X×_Y 0` as pullback `0→Y` and cofiber `cofib(f)= Y ∪_X 0` as pushout `X→Y` with `0 : Sp` zero object, and `Sp` is stable so `fib(f) ≃ cofib(f)[-1]` and `cofib(f) ≃ fib(f)[1]` and distinguished triangles `fib→X→Y→fib[1]`. Need `f.fiber() → fib(f) : Sp` and `f.cofiber() → cofib(f) : Sp` with `fib ≃ Σ^{-1}cofib`.

Intended owners: `categories/spectra/morava_k.py` (`K(n) : CAlg(Sp)` with `K(n)_*`, `L_{K(n)}`), `categories/spectra/morava_e.py` (`E_n : CAlg(Sp)` Lubin-Tate with height `n`), `categories/spectra/localization.py` (`L_{K(n)}`, `p`-local `S^0_{(p)}`, `p`-complete `S^0^{∧}_p`), `categories/spectra/fibers_cofibers.py` (`fib(f)`, `cofib(f)` in `Sp` stable, `fib ≃ cofib[-1]`). Not a free `localize_sphere(n)` returning number — `L_{K(n)}S^0 : Sp` with height `n`.

## Desired capability: framed manifolds, factorization homology, `(-)^{hG}` and `(-)_{hG}`, `MString` and `tmf` — note 2026-09-16

Operationalize framed manifolds, factorization homology, `(*)^{hG}` and `(*)_{hG}` functors, `MString` and `tmf` spectra.

* Framed `n`-manifold is `M : Mfld^{fr}_n` with `M : Man` smooth `n`-manifold and framing `φ: TM ≅ M×R^n` as `Vect` trivialization, equivalently lift of classifying map `M → BO(n)` to `BString?` actually `BO(n)` via `EO(n)`, with `Mfld^{fr}_n : Cat` with morphisms embeddings `M↪N` preserving framing. Need `FramedManifold` with `TM` framing.

* Factorization homology `∫_M A` for `E_n`-algebra `A : Alg_{E_n}(Sp)` (or `Alg_{E_n}(C)` for `C : Cat` like `Ch`, `Sp`, `Vect`) and framed `M : Mfld^{fr}_n` is `∫_M A = colim_{Disk^{fr}_{n/M}} A` as colimit over `Disk^{fr}_{n/M} = { U = ∐_{i∈I} R^n ↪ M }` with `A(U)=A^{⊗I}`, with `∫_{R^n} A ≃ A` and excision `∫_{M ∪_{M_0×R} N} A ≃ ∫_M A ⊗_{∫_{M_0×R} A} ∫_N A`. For `A` as `E_∞` algebra, `∫_M A ≃ A⊗ Σ^∞_+ M` etc. Need `A.factorization_homology(M) → ∫_M A : C` with `A` as `E_n`-algebra.

* `(-)^{hG}` and `(-)_{hG}` functors: for `G : Groups` finite (or `G : Spaces` as `∞`-group `BG`), `X : Sp^{BG} = Fun(BG,Sp)` is spectrum with `G`-action, homotopy fixed points `X^{hG} = lim_{BG} X = Map_{Sp^{BG}}(1, X) : Sp` as limit over `BG` and homotopy orbits `X_{hG} = colim_{BG} X = 1 ⊗_{G} X : Sp` as colimit, with `X^{hG} = (X)^{G}` derived and `X_{hG}=X/G` derived, norm `Nm: X_{hG} → X^{hG}` and Tate construction `X^{tG}=cofib(Nm)` with `X^{tG}= (X^{hG})_{?}` etc. Need `X.homotopy_fixed_points(G) → X^{hG} : Sp` and `X.homotopy_orbits(G) → X_{hG} : Sp`.

* `MString` and `tmf` spectra: `MString = Thom(MString)` as `E_∞` ring spectrum `MString = Thom(BString → BO)` with `BString = BSpin⟨½p_1⟩` and `π_*(MString)` string bordism, and `tmf = O^{top}(M_{ell})` topological modular forms as `E_∞` ring spectrum `tmf` with `π_*(tmf)` via `tmf_* =` `E_∞` with `tmf → MString` orientation `σ: MString → tmf` Witten genus, `TMF = tmf[Δ^{-1}]` periodic, `Tmf` compactified. Need `MString : CAlg(Sp)` and `tmf : CAlg(Sp)` with `σ`.

Intended owners: `categories/manifolds/framed.py` (`FramedManifold` `Mfld^{fr}_n`), `categories/factorization/factorization_homology.py` (`∫_M A : C` for `E_n`-algebra `A`), `categories/spectra/homotopy_fixed_points.py` (`X^{hG}=lim_{BG} X`), `categories/spectra/homotopy_orbits.py` (`X_{hG}=colim_{BG} X`), `categories/spectra/mstring.py` (`MString : CAlg(Sp)`), `categories/spectra/tmf.py` (`tmf : CAlg(Sp)` with `σ: MString→tmf`). Not a free `factorization_homology(M,A)` returning list — `A.factorization_homology(M)` with `∫_M A`.

## Desired capability: sieves, Grothendieck topologies, pullbacks as intersections, topoi — note 2026-09-16

Operationalize sieves, Grothendieck topologies, pullbacks as intersections, and topoi.

* Sieve `S ⊂ h_U` on `U : C` is subfunctor `S ⊂ Hom_C(-,U) : C^{op}→Set` with `S` closed under precomposition: if `f ∈ S(V)` and `g: W→V` then `f∘g ∈ S(W)`. Equivalently collection of morphisms into `U` stable under precomposition. Need `Sieve(C,U)` with `S.subobject(h_U)` and `S.is_sieve()`.

* Grothendieck topology `J` on `C : Cat` is collection `J(U) = { S ⊂ h_U | S covering}` for each `U : C` with axioms: maximal `h_U ∈ J(U)`, stability `S∈J(U)` and `f: V→U` implies `f^*S = { g: W→V | f∘g ∈ S } ∈ J(V)`, transitivity `S∈J(U)` and `T ⊂ h_U` with `f^*T ∈ J(V)` for all `f∈S` implies `T∈J(U)`. Covering families `{U_i→U}` generate sieves `S = { f: V→U | f factors through some U_i→U }`. Need `GrothendieckTopology` with `J.covering_sieves(U)`.

* Pullbacks as intersections operationalized: in `C = Op(X)` poset of opens of `X : Top` with `U ≤ V` iff `U⊆V`, pullback `U×_X V = U∩V` as intersection, and more generally for `C = Sub(X)` or `C = FinSets`, pullback is intersection `A×_C B = A∩B` when `A,B ⊂ C` as subobjects. In general `Cat`, pullback `V×_U W` for `V→U←W` is fiber product, and when `C` is poset, it is meet `V∧W`. Need `C.pullback(V→U←W) → V×_U W : C` with `V×_U W = V∩W` when `C` is `Op(X)` or `Sub`.

* Topos `E : Topoi` as Grothendieck topos `E = Sh(C,J)` sheaves on site `(C,J)` with finite limits, colimits, exponentials, subobject classifier `Ω`, and `E` is `∞`-topos `E = Sh_∞(C,J)` when `S`-valued; `E = PSh(C)` presheaves and sheafification `a: PSh(C) → Sh(C,J)` left exact left adjoint to inclusion, with `E` as left exact localization of `PSh(C)`; `E` has `E = Sh(C,J) = PSh(C)[J^{-1}]`. Need `Topoi` as 2-category with `Sh(C,J)` as objects, geometric morphisms `f: E→F` as `f^*: F→E` left exact left adjoint. Also elementary topos axioms.

Intended owners: `categories/sites/sieves.py` (`Sieve` `S⊂h_U`), `categories/sites/grothendieck_topology.py` (`J` with `J(U)` covering sieves), `categories/limits/pullbacks_as_intersections.py` (`pullback` as `∩` for `Op(X)`), `categories/topoi/topoi.py` (`Topos` `E=Sh(C,J)` with `a: PSh→Sh`), `categories/topoi/sheaves.py` (`Sh(C,J)`). Not a free `sieve_on(U)` returning list — `Sieve(C,U)` with `S⊂h_U` and `J.covering_sieves(U)`.

## Desired capability: superficie.info as oracle source for surface invariants, and interactive geography/classification tool for lattices — intake 2026-09-19

Intake item from https://superficie.info/ (Belmans–Commelin, repository: https://github.com/superficie/superficie-algebriche).

* **Source of oracle calculations for algebraic surfaces:**
  * `superficie.info` catalogs minimal complex algebraic smooth surfaces structured by the Enriques–Kodaira classification ($\kappa \in \{-\infty, 0, 1, 2\}$) and pairs of Chern numbers $(c_1^2, c_2)$.
  * Numerical invariants provided: Kodaira dimension $\kappa$, Chern numbers $(c_1^2, c_2)$, topological Euler characteristic $e = c_2$, holomorphic Euler characteristic $\chi(\mathcal{O}_X) = \frac{1}{12}(c_1^2 + c_2)$, irregularity $q = h^{0,1}$, geometric genus $p_g = h^{0,2}$, Betti numbers $b_1, b_2, b_3, b_4$, and full Hodge diamond $h^{p,q}$.
  * Preamble integration: serves as an oracle and specimen test-fixture database for preamble surface invariants and scheme constructions (`categories/schemes/surfaces/`, `Surfaces/C`), validating intersection numbers, canonical divisor properties $K_X^2 = c_1^2$, and Hodge numbers against literature citations.

* **TODO: Produce a similar tool for lattices:**
  * Design and implement a lattice geography / classification explorer analogous to `superficie.info` (and related sites `fanography.info`, `grassmannian.info`, `hyperkaehler.info`).
  * Mathematical domain: integral lattices $(L, b)$ up to isometry, classified by signature $(p, q)$ (definite and indefinite/Lorentzian), rank $n = p + q$, determinant $\det(L)$, discriminant group $A_L = L^\vee / L$, discriminant quadratic/bilinear form $q_L: A_L \to \mathbb{Q}/2\mathbb{Z}$, parity (even/odd), genus of lattices (via Conway–Sloane / Nikulin $p$-adic invariants), root systems (roots of norm $\pm 2$, Dynkin diagrams), reflection groups / Coxeter–Vinberg polyhedra, and special geometric lattices (hyperbolic lattices, $E_8$, Leech $\Lambda_{24}$, K3 lattice $\mathrm{II}_{3,19}$, Enriques lattice $E_8(-1) \oplus U$, Coble lattices, and their primitive embeddings).
  * Interactive tool architecture:
    * 2D geography / parameter space grid (e.g. signature $(p, q)$, or $(n, \det(L))$, or $(\mathrm{rank}, \mathrm{length}(A_L))$).
    * Filtering by mathematical properties: unimodular, even/odd, definite/indefinite, signature, reflective, projective/hyperbolic.
    * Detail view per lattice/genus: Gram matrix representative, discriminant form, automorphism group $\mathrm{O}(L)$, root system components, embedding relations (e.g. primitive sublattices and orthogonal complements in $\mathrm{II}_{3,19}$ or $\mathrm{II}_{1,25}$).
    * Exportable test specimens / oracle fixtures formatted for direct verification in `tests/lattices/` and preamble lattice modules.

Intended owners: `categories/schemes/surfaces/` (surface invariants and oracle verification), `categories/lattices/` (`Lattices` category, discriminant forms, genus classification, invariants), and `computations/` or `src/dzack_research/` / web visualizer (interactive lattice geography explorer).

## Desired capability: Fano 3-folds geography, classification, and derived categories (Fanography) — intake 2026-09-19

Intake item from https://fanography.info/ (Pieter Belmans, repository: https://github.com/fanography/fanography).

* **Source of oracle calculations for Fano 3-folds:**
  * Exhaustive catalog of the 105 deformation families of smooth complex Fano 3-folds classified by Iskovskikh and Mori–Mukai.
  * Stratification by Picard rank $\rho(X) \in \{1, \dots, 10\}$:
    * $\rho = 1$: 17 families (e.g. index $r=4$: $\mathbb{P}^3$; index $r=3$: quadric $Q^3 \subset \mathbb{P}^4$; index $r=2$: del Pezzo 3-folds $V_1, \dots, V_5$; index $r=1$: prime Fano 3-folds $X_{2g-2}$ with genus $g \in \{2, \dots, 10, 12\}$).
    * $\rho = 2$: 36 families.
    * $\rho = 3$: 31 families.
    * $\rho = 4$: 13 families.
    * $\rho = 5$: 3 families.
    * $\rho = 6$: 1 family (blowup of $\mathbb{P}^3$ at 6 points).
    * $\rho = 7$: 1 family.
    * $\rho = 8$: 1 family.
    * $\rho = 9$: 1 family.
    * $\rho = 10$: 1 family ($\mathbb{P}^1 \times S_1$ where $S_1$ is del Pezzo surface of degree 1).
  * Numerical invariants provided per family:
    * Picard rank $\rho = b_2$, Fano index $r = \max \{m \in \mathbb{Z}_{>0} \mid -K_X = m H \text{ for } H \in \mathrm{Pic}(X)\}$.
    * Anticanonical degree $(-K_X)^3$, genus $g = \frac{1}{2}(-K_X)^3 + 1$.
    * Betti numbers $b_2, b_3, b_4$ (with $b_1 = 0$, $b_5 = 0$, $b_2 = b_4 = \rho$, $b_3 = 2 h^{1,2}$).
    * Hodge diamond: $h^{1,1} = \rho$, $h^{1,2} = \frac{1}{2} b_3$, and $h^{p,q} = 0$ for $p \neq q$ and $p + q \neq 3$.
    * Topological Euler characteristic $e(X) = 2 + 2\rho - 2 h^{1,2}$.
    * Dimension of automorphism group $\dim \mathrm{Aut}^0(X)$ and reductivity/Lie algebra structure.
    * Intermediate Jacobian $J(X) = H^{1,2}(X)^\vee / H_3(X, \mathbb{Z})$: dimension $g(J) = h^{1,2}$, principally polarized abelian variety structure, Torelli theorem validity.
  * Categorical and moduli data:
    * Bounded derived category $\mathbf{D}^b(X)$: semi-orthogonal decompositions (SOD), exceptional collections, and residual Kuznetsov components $\mathcal{A}_X$ (e.g. cubic 3-fold Kuznetsov component, quartic double solid, Gushel–Mukai 3-folds).
    * Moduli of curves on $X$: Hilbert scheme of lines $\mathrm{F}(X)$ (Fano surface of lines) and conics $\mathcal{C}(X)$, including smoothness, dimension, and Abel–Jacobi map to $J(X)$.
    * Mori fiber space structures: conic bundles, del Pezzo fibrations, and extremal contractions.
  * Preamble integration:
    * Preamble must construct Fano varieties as objects in `Schemes/C` (`categories/schemes/fano/`).
    * Compute numerical invariants $(\rho, r, (-K)^3, g, b_i, h^{p,q})$ directly from defining equations, complete intersections, or blowup data.
    * Wire semi-orthogonal decompositions in $\mathbf{D}^b(X)$ to derived category foundations (`categories/derived/`).

Intended owners: `categories/schemes/fano/` (`FanoThreefold`, `FanoClassification`), `categories/derived/` (`SemiOrthogonalDecomposition`, `KuznetsovComponent`), `categories/schemes/surfaces/del_pezzo.py` (del Pezzo surfaces and fibrations).

## Desired capability: Generalized Grassmannians $G/P$, Schubert calculus, and homogeneous bundles (Grassmannian.info) — intake 2026-09-19

Intake item from https://www.grassmannian.info/ (Pieter Belmans, repository: https://github.com/pbelmans/grassmannian.info).

* **Source of oracle calculations for generalized Grassmannians:**
  * Complete periodic table of generalized Grassmannians $G/P$ where $G$ is a simple complex Lie group of any Dynkin type ($A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2$) and $P$ is a maximal parabolic subgroup (corresponding to a marked node on the Dynkin diagram).
  * Types covered:
    * Type $A_n$: Classical Grassmannians $\mathrm{Gr}(k, n+1)$.
    * Type $B_n$: Odd orthogonal Grassmannians $\mathrm{OGr}(k, 2n+1)$.
    * Type $C_n$: Symplectic Grassmannians $\mathrm{SGr}(k, 2n)$ (including Lagrangian Grassmannian $\mathrm{LGr}(n, 2n)$).
    * Type $D_n$: Even orthogonal Grassmannians $\mathrm{OGr}(k, 2n)$ (including orthogonal spinor varieties $\mathrm{OGr}_+(n, 2n)$).
    * Exceptional types: Cayley plane $E_6/P_1 \cong E_6/P_6$ (dimension 16, Severi variety), Freudenthal variety $E_7/P_7$ (dimension 27), adjoint $E_8/P_8$, $F_4$-Grassmannians $F_4/P_1, F_4/P_4$, and $G_2$-Grassmannian $G_2/P_1$ (five-dimensional quadric section) and $G_2/P_2$ (adjoint $G_2$-variety).
  * Invariants and structures provided:
    * Dimension $\dim(G/P) = \dim(G) - \dim(P)$.
    * Fano index $r(G/P)$ and Picard number $\rho = 1$ (for maximal parabolics).
    * Schubert calculus: Weyl group $W = W(G)$, parabolic subgroup $W_P$, minimal length coset representatives $W^P \subset W$. Schubert cells $X_w = B w P / P$ indexed by $w \in W^P$ with $\dim X_w = \ell(w)$.
    * Poincaré polynomial $P(t) = \sum_{w \in W^P} t^{2 \ell(w)}$, giving Betti numbers $b_{2k} = \# \{w \in W^P \mid \ell(w) = k\}$ and odd Betti numbers $b_{2k+1} = 0$.
    * Cohomology ring $H^*(G/P, \mathbb{Z})$: Schubert classes $[X_w]$, Littlewood–Richardson coefficients and Schubert intersection products $\sigma_u \cdot \sigma_v = \sum c_{u,v}^w \sigma_w$.
    * Homogeneous vector bundles: tautological subbundle $\mathcal{S}$ and quotient bundle $\mathcal{Q}$ on $\mathrm{Gr}(k, V)$, universal spinor bundles on orthogonal Grassmannians; irreducible $G$-equivariant vector bundles $\mathcal{E}_\lambda = G \times_P V_\lambda$ associated to dominant weights $\lambda$ of $P$.
    * Borel–Weil–Bott theorem: constructive computation of cohomology groups $H^q(G/P, \mathcal{E}_\lambda)$ via the dot action $w \cdot \lambda = w(\lambda + \rho) - \rho$ of the Weyl group $W$.
    * Derived categories $\mathbf{D}^b(G/P)$: full exceptional collections of homogeneous vector bundles (Kapranov collections on $\mathrm{Gr}(k,n)$, Kuznetsov–Polishchuk collections on quadrics and symplectic Grassmannians).
    * Automorphism group $\mathrm{Aut}(G/P) \cong G_{ad}$ and tangent bundle $T(G/P) \cong G \times_P (\mathfrak{g}/\mathfrak{p})$.
  * Preamble integration:
    * Preamble must construct $G/P$ as owned homogeneous scheme objects in `Schemes/C` (`categories/schemes/grassmannian.py`, `categories/lie/homogeneous_spaces.py`).
    * Operationalize Schubert cell enumeration, Bruhat order posets, Poincaré polynomials, and intersection rings from the Weyl group representation of $G$.
    * Operationalize Borel–Weil–Bott functor: $\mathrm{Rep}(P) \to \mathrm{Coh}(G/P)$ and its pushforward to derived vector spaces $R\Gamma(G/P, -) \in \mathbf{D}^b(\mathrm{Vect})$.

Intended owners: `categories/schemes/grassmannian.py` (`Grassmannian`, `GeneralizedGrassmannian`), `categories/lie/homogeneous_spaces.py` (`HomogeneousSpace` $G/P$, Borel–Weil–Bott), `categories/derived/exceptional_collections.py` (Kapranov and Kuznetsov exceptional collections).

## Desired capability: Scheme and morphism adjectives, automated deduction, and counterexamples (The Adjectives Project) — intake 2026-09-19

Intake item from https://adjectivesproject.org/ (Jesse Vogel and David Holmes, repositories: https://github.com/jessetvogel/adjectives-project and https://github.com/jessetvogel/adjectives-project-data).

* **Extensive mining of scheme properties and morphism properties:**
  * Complete repository of mathematical "adjectives" (predicates), implication theorems, and specimen counterexamples mined from the Stacks Project and EGA.
  * **Scheme adjectives (19 properties):**
    1. `affine`: admitting an isomorphism $X \cong \mathrm{Spec}(R)$ for a commutative ring $R$.
    2. `cohen-macaulay`: local rings $\mathcal{O}_{X,x}$ satisfy $\mathrm{depth}(\mathcal{O}_{X,x}) = \dim(\mathcal{O}_{X,x})$ for all $x \in X$.
    3. `connected`: underlying topological space is connected (no partition into disjoint nonempty opens).
    4. `excellent`: locally Noetherian, universally catenary, and all formal completions have geometrically regular fibers.
    5. `finite-dimensional`: Krull dimension $\dim(X) < \infty$.
    6. `integral`: reduced and irreducible (equivalently, $\mathcal{O}_X(U)$ is an integral domain for all connected open $U$).
    7. `irreducible`: underlying topological space is not the union of two proper closed subsets.
    8. `jacobson`: the set of closed points is dense in every closed subscheme; all local rings have Jacobson property.
    9. `locally-factorial`: every local ring $\mathcal{O}_{X,x}$ is a unique factorization domain (UFD).
    10. `locally-noetherian`: admitting an open affine covering $X = \bigcup \mathrm{Spec}(A_i)$ with each $A_i$ a Noetherian ring.
    11. `noetherian`: locally Noetherian and quasi-compact.
    12. `normal`: every local ring $\mathcal{O}_{X,x}$ is an integrally closed integral domain.
    13. `quasi-affine`: isomorphic to an open subscheme of an affine scheme.
    14. `quasi-compact`: every open covering has a finite subcovering.
    15. `quasi-separated`: the diagonal morphism $\Delta_{X}: X \to X \times_{\mathrm{Spec}\mathbb{Z}} X$ is quasi-compact.
    16. `reduced`: every local ring $\mathcal{O}_{X,x}$ has zero nilradical ($\mathcal{N}(\mathcal{O}_{X,x}) = 0$).
    17. `regular`: every local ring $\mathcal{O}_{X,x}$ is regular ($\dim_{\kappa(x)} \mathfrak{m}_x/\mathfrak{m}_x^2 = \dim \mathcal{O}_{X,x}$).
    18. `semi-separated`: the intersection of any two affine open subschemes is affine.
    19. `separated`: the diagonal morphism $\Delta_{X}: X \to X \times_{\mathrm{Spec}\mathbb{Z}} X$ is a closed immersion.

  * **Morphism adjectives (44 properties):**
    1. `affine`: preimage of every affine open is affine ($f_* \mathcal{O}_X$ is quasi-coherent $\mathcal{O}_Y$-algebra).
    2. `bundle-projective`: isomorphic to $\mathbb{P}(\mathcal{E}) \to Y$ for a locally free sheaf $\mathcal{E}$ on $Y$.
    3. `closed-immersion`: homeomorphism onto a closed subset with surjective sheaf map $\mathcal{O}_Y \twoheadrightarrow f_* \mathcal{O}_X$.
    4. `closed`: image of every closed subset is closed.
    5. `etale`: flat and unramified (formally étale and locally of finite presentation).
    6. `faithfully-flat`: flat and surjective on points.
    7. `finite-fibers`: every fiber $f^{-1}(y)$ is a finite discrete set.
    8. `finite-locally-free`: finite and $f_* \mathcal{O}_X$ is a locally free $\mathcal{O}_Y$-module of finite rank.
    9. `finite`: affine and $f_* \mathcal{O}_X$ is a finite $\mathcal{O}_Y$-module.
    10. `flat`: local rings $\mathcal{O}_{X,x}$ are flat $\mathcal{O}_{Y,f(x)}$-modules for all $x \in X$.
    11. `formally-etale`: Infinitesimal lifting criterion holds uniquely for square-zero ring extensions.
    12. `formally-smooth`: Infinitesimal lifting criterion holds (existence of lifts) for square-zero extensions.
    13. `formally-unramified`: Infinitesimal lifting criterion holds (at most one lift) for square-zero extensions.
    14. `g-unramified`: unramified in the sense of Grothendieck (diagonal is an open immersion).
    15. `h-projective`: homogeneous projective morphism (factors through a closed immersion into $\mathbb{P}^n_Y$).
    16. `homeomorphism`: $f$ is a topological homeomorphism on underlying spaces.
    17. `immersion`: composition of an open immersion and a closed immersion.
    18. `injective`: injective on underlying sets of points.
    19. `integral`: affine and every element of $f_* \mathcal{O}_X$ is integral over $\mathcal{O}_Y$.
    20. `locally-of-finite-presentation`: locally $X \to Y$ is given by $B = A[x_1,\dots,x_n]/(f_1,\dots,f_m)$.
    21. `locally-of-finite-type`: locally $X \to Y$ is given by $B = A[x_1,\dots,x_n]/I$.
    22. `locally-projective`: admitting open cover of $Y$ over which $f$ is projective.
    23. `monomorphism`: monic in the category of schemes ($\mathrm{Hom}(T, X) \hookrightarrow \mathrm{Hom}(T, Y)$ is injective).
    24. `of-finite-presentation`: locally of finite presentation, quasi-compact, and quasi-separated.
    25. `of-finite-type`: locally of finite type and quasi-compact.
    26. `open-immersion`: isomorphism onto an open subscheme.
    27. `open`: image of every open subset is open.
    28. `projective`: factors as a closed immersion $X \hookrightarrow \mathbb{P}(\mathcal{E})$ followed by projection to $Y$.
    29. `proper`: universally closed, separated, and of finite type.
    30. `quasi-affine`: quasi-compact and factors as an open immersion into an affine $Y$-scheme.
    31. `quasi-compact`: preimage of every quasi-compact open is quasi-compact.
    32. `quasi-finite`: of finite type with finite fibers.
    33. `quasi-separated`: diagonal $\Delta_{X/Y}: X \to X \times_Y X$ is quasi-compact.
    34. `regular`: flat with all fibers geometrically regular.
    35. `semi-separated`: diagonal $\Delta_{X/Y}$ is an affine morphism.
    36. `separated`: diagonal $\Delta_{X/Y}$ is a closed immersion.
    37. `smooth`: flat, locally of finite presentation, and all fibers geometrically smooth.
    38. `surjective`: surjective on underlying sets of points ($f(X) = Y$).
    39. `syntomic`: flat, locally of finite presentation, and all fibers local complete intersections.
    40. `universally-closed`: for every base change $Y' \to Y$, $X \times_Y Y' \to Y'$ is closed.
    41. `universally-homeomorphism`: universally bijective, universally closed, and universally open.
    42. `universally-injective`: for every base change $Y' \to Y$, $X \times_Y Y' \to Y'$ is injective.
    43. `universally-open`: for every base change $Y' \to Y$, $X \times_Y Y' \to Y'$ is open.
    44. `unramified`: formally unramified and locally of finite type.

  * **Theorems / Deduction Lattice (95 theorems):**
    * Scheme deductions (15 theorems):
      * `regular` $\implies$ `locally-factorial` $\implies$ `normal` $\implies$ `reduced`.
      * `integral` $\iff$ `reduced` + `irreducible`.
      * `noetherian` $\iff$ `locally-noetherian` + `quasi-compact`.
      * `locally-noetherian` $\implies$ `cohen-macaulay` if local rings CM.
      * `affine` $\implies$ `separated` $\implies$ `semi-separated` $\implies$ `quasi-separated`.
      * `affine` $\implies$ `quasi-compact`.
      * `excellent` $\implies$ `locally-noetherian`.
      * `jacobson` preserved under finite type extensions over Jacobson bases.
    * Morphism deductions (80 theorems):
      * `closed-immersion` $\implies$ `proper` $\implies$ `separated`.
      * `open-immersion` $\implies$ `etale` $\implies$ `smooth` $\implies$ `syntomic` $\implies$ `flat`.
      * `etale` $\iff$ `smooth` + `unramified` $\iff$ `flat` + `unramified` (under finite presentation).
      * `finite` $\iff$ `proper` + `quasi-finite` (Zariski's Main Theorem).
      * `finite` $\implies$ `affine` $\implies$ `quasi-affine` $\implies$ `separated`.
      * `projective` $\implies$ `proper` $\implies$ `universally-closed` + `separated` + `of-finite-type`.
      * `monomorphism` + `proper` $\implies$ `closed-immersion`.
      * Base change stability: flat, smooth, étale, proper, affine, closed immersion, open immersion are all stable under arbitrary pullback.
      * Composition stability: all 44 adjectives (except relative/fiber conditions) are stable under morphism composition.
      * Cancellation properties (2-out-of-3): if $g \circ f$ has property $P$ and $g$ is separated, $f$ inherits properties.
  * **Specimen Database (107 examples):**
    * 49 schemes (affine line with doubled origin [non-separated], $\mathrm{Spec}(\mathbb{Z})$, cusp $y^2=x^3$ [non-normal], node $y^2=x^2(x+1)$ [non-normal, reduced], non-reduced fat point $\mathrm{Spec}(k[x]/(x^2))$, infinite disjoint union $\coprod \mathrm{Spec}(k)$ [non-quasi-compact], etc.).
    * 58 morphisms (Frobenius morphism [homeomorphism, not étale in char $p$], normalization map [finite, birational, not isomorphism], blowup of point [projective, birational, not finite], open immersion, diagonal morphism, etc.).
  * **Preamble implementation requirement:**
    * In `categories/schemes/` (`categories/schemes/properties.py`, `categories/schemes/morphism_properties.py`), properties must be first-class predicates: `X.is_affine()`, `X.is_proper()`, `f.is_flat()`, `f.is_smooth()`, `f.is_etale()`, `f.is_closed_immersion()`, etc.
    * An automated property deduction engine must derive known properties from established ones using the 95 implication theorems without recomputing from raw rings.
    * Every counterexample must exist as a constructible test fixture in `tests/schemes/` verifying that negative properties are correctly refuted and positive properties proven.

Intended owners: `categories/schemes/properties.py` (`SchemeProperties`, deduction graph), `categories/schemes/morphism_properties.py` (`MorphismProperties`, base change and composition preservation), `categories/schemes/theorems.py` (95 implication theorems).

## Desired capability: General topology counterexamples, properties, and universal constructions (pi-Base) — intake 2026-09-19

Intake item from https://topology.pi-base.org/ (repositories: https://github.com/pi-base/data and https://github.com/pi-base/web).

* **Comprehensive mining of general topology:**
  * Complete operationalization of 246 topological properties, 224 canonical topological spaces, 931 deductive theorems, and universal topological constructions based on Steen & Seebach *Counterexamples in Topology*.
  * **Topological Properties (246 properties categorized):**
    * **Separation Axioms:**
      * $T_0$ (Kolmogorov): distinct points have distinct closure.
      * $T_1$ (Fréchet): points are closed.
      * $T_2$ (Hausdorff): distinct points have disjoint open neighborhoods.
      * $T_{2.5}$ (Urysohn / completely Hausdorff): distinct points separated by closed neighborhoods.
      * Functionally Hausdorff: distinct points separated by continuous real-valued function.
      * $T_3$ (Regular Hausdorff): $T_1$ and closed set and point separated by open neighborhoods.
      * $T_{3.5}$ (Completely regular / Tychonoff): $T_1$ and closed set and point separated by continuous function to $[0,1]$.
      * $T_4$ (Normal Hausdorff): $T_1$ and disjoint closed sets separated by open neighborhoods.
      * $T_5$ (Completely normal Hausdorff): every subspace is $T_4$; separated subsets separated by opens.
      * $T_6$ (Perfectly normal Hausdorff): normal and every closed set is a $G_\delta$ set.
    * **Compactness Notions:**
      * `compact`: every open cover has a finite subcover.
      * `countably-compact`: every countable open cover has a finite subcover.
      * `sequentially-compact`: every sequence has a convergent subsequence.
      * `pseudocompact`: every continuous real function is bounded.
      * `locally-compact`: every point has a compact neighborhood base.
      * `paracompact`: every open cover has a locally finite open refinement.
      * `metacompact`: every open cover has a point-finite open refinement.
      * `orthocompact`: every open cover has an interior-preserving open refinement.
      * `hemicompact`: admitting an exhaustion by compact subsets.
      * `sigma-compact`: countable union of compact subspaces.
      * `lindelof`: every open cover has a countable subcover.
    * **Connectedness:**
      * `connected`: no partition into two nonempty disjoint open sets.
      * `path-connected`: every pair of points joined by continuous path $[0,1] \to X$.
      * `locally-connected`: admitting a neighborhood base of connected sets.
      * `locally-path-connected`: admitting a neighborhood base of path-connected sets.
      * `hyperconnected`: no two disjoint nonempty open sets (every open set dense).
      * `ultraconnected`: no two disjoint nonempty closed sets.
      * `totally-disconnected`: connected components are singletons.
      * `totally-separated`: points separated by clopen sets.
      * `extremally-disconnected`: closure of every open set is open.
    * **Countability and Separability:**
      * `first-countable`: every point has a countable neighborhood base.
      * `second-countable`: topology has a countable base of open sets.
      * `separable`: admitting a countable dense subset.
      * `ccc` (countable chain condition): every family of pairwise disjoint opens is countable.
      * `resolvable`: partitionable into two dense subsets.
      * `baire-space`: intersection of countably many dense open sets is dense.
    * **Metrizability and Uniformity:**
      * `metrizable`: topology induced by a metric.
      * `completely-metrizable` (Polish): admitting a complete metric.
      * `pseudometrizable`: induced by a pseudometric.
      * `moore-space`: developable and regular.
    * **Dimension Theory:**
      * `zero-dimensional`: admitting a base of clopen sets.
      * `strongly-zero-dimensional`: completely regular and $\dim(X) = 0$ in covering dimension.
      * Small inductive dimension $\mathrm{ind}(X)$, large inductive dimension $\mathrm{Ind}(X)$, Lebesgue covering dimension $\dim(X)$.

  * **Canonical Spaces (224 spaces):**
    * Standard spaces: Discrete space $D$, Indiscrete space, Sierpiński space $S = \{0, 1\}$, Finite spaces, Euclidean space $\mathbb{R}^n$, Unit interval $I = [0,1]$, Circle $S^1$, Spheres $S^n$, Torus $T^n$.
    * Counterexample spaces:
      * Cantor set $2^\omega$, Baire space $\omega^\omega$, Hilbert cube $[0,1]^\omega$.
      * Sorgenfrey line $\mathbb{R}_l$ (lower limit topology: paracompact, first countable, separable, Lindelöf, but $\mathbb{R}_l^2$ is not normal [Sorgenfrey plane]).
      * Niemytzki plane (Moore plane: completely regular, separable, but not normal).
      * Long line $L$ and Long ray (locally homeomorphic to $\mathbb{R}$, path-connected, sequentially compact, but not Lindelöf, not metrizable).
      * Tychonoff plank $[0, \omega_1] \times [0, \omega] \setminus \{(\omega_1, \omega)\}$ (completely regular, not normal).
      * Stone–Čech compactification $\beta\mathbb{N}$ (compact Hausdorff, extremally disconnected, not first countable, cardinality $2^{2^{\aleph_0}}$).
      * Arens–Fort space (countable, Hausdorff, normal, but not first countable).
      * Ordinal spaces $[0, \omega_1)$ (first countable, countably compact, locally compact, not compact, not Lindelöf) and $[0, \omega_1]$ (compactification).
      * Warsaw circle (compact, connected, path components $\neq$ components, not locally connected).
      * Hawaiian earring $\bigcup_{n=1}^\infty C_n$ (compact, path connected, not locally path connected, $\pi_1$ is uncountable).
      * Topologist's sine curve (connected, not path connected).
      * Comb space and Deleted comb space (connected, path connected, not contractible).
      * Alexandroff double circle (compact, Hausdorff, first countable, separable, not second countable).
      * Line with two origins (locally Euclidean, non-Hausdorff manifold).

  * **Universal Constructions:**
    * `Subspace(X, U)`: subspace topology on $S \subset X$.
    * `Product(X_i)_{i \in I}`: arbitrary Cartesian product with product topology (Tychonoff topology).
    * `Coproduct(X_i)_{i \in I}`: disjoint union topology.
    * `Quotient(X, ~)`: quotient topology by equivalence relation.
    * `OnePointCompactification(X)`: Alexandroff compactification $X^* = X \cup \{\infty\}$.
    * `StoneCechCompactification(X)`: universal compactification $\beta X$ for Tychonoff $X$.
    * `Cone(X) = (X \times [0,1]) / (X \times \{0\})`, `Suspension(X) = Cone(X) / (X \times \{1\})`.
    * `WedgeSum(X, Y, x_0, y_0) = (X \sqcup Y) / (x_0 \sim y_0)`.
    * `SmashProduct(X, Y, x_0, y_0) = (X \times Y) / (X \vee Y)`.

  * **Theorems / Deduction Lattice (931 theorems):**
    * Tychonoff Theorem: $\prod X_i$ compact $\iff$ each $X_i$ compact.
    * Urysohn Metrization Theorem: $T_3$ + second countable $\implies$ metrizable.
    * Nagata–Smirnov / Bing Metrization Theorems: regular + $\sigma$-locally finite base $\iff$ metrizable.
    * Compact Hausdorff implies normal ($T_2$ + compact $\implies T_4$).
    * Second countable implies Lindelöf, separable, and first countable.
    * Metrizable implies paracompact, first countable, and $T_6$.
    * Paracompact Hausdorff implies normal ($T_2$ + paracompact $\implies T_4$).
    * Subspace preservation: $T_0, T_1, T_2, T_{2.5}, T_3, T_{3.5}$ are hereditary; compactness is closed-hereditary; second countability is hereditary.
    * Product preservation: $T_0, T_1, T_2, T_{2.5}, T_3, T_{3.5}$, connectedness, compactness are productive; normality and Lindelöf are not productive (Sorgenfrey counterexample).

  * **Preamble implementation requirement:**
    * `categories/topology/` must provide:
      * Constructible canonical spaces in `categories/topology/spaces.py`.
      * Universal constructions (subspaces, products, coproducts, quotients, compactifications) in `categories/topology/constructions.py`.
      * Evaluatable predicates for the 246 properties in `categories/topology/properties.py`.
      * Deductive theorem inference engine in `categories/topology/theorems.py` resolving implications across all 931 theorems.

Intended owners: `categories/topology/spaces.py` (`TopologicalSpace`, canonical space catalogue), `categories/topology/properties.py` (`TopologicalProperties`, 246 predicates), `categories/topology/constructions.py` (`Product`, `Coproduct`, `Quotient`, `Subspace`, `Alexandroff`, `StoneCech`), `categories/topology/theorems.py` (931 deduction rules).

## Desired capability: Bilinear forms to polynomial schemes, 1-parameter quadric families, and integral point transport — intake 2026-09-19

Intake note from user 2026-09-19.

* **Algebraic translation from bilinear forms to polynomials:**
  * Let $R$ be a commutative ring and let $M$ be a free $R$-module of finite rank $n$ equipped with an ordered basis $(e_0, \dots, e_{n-1})$ identifying $M \cong R^n$.
  * Any $R$-bilinear form $b\colon M \otimes_R M \to R$ induces an explicit homogeneous degree-2 polynomial in the polynomial ring $R[x_0, \dots, x_{n-1}]$ by evaluating on coordinate vectors $\vec{x} \coloneqq [x_0, \dots, x_{n-1}]^t$:
    $$
    f_b(\vec{x}) \coloneqq b(\vec{x}, \vec{x}) = \sum_{i,j=0}^{n-1} b(e_i, e_j)\, x_i x_j \in R[x_0, \dots, x_{n-1}].
    $$
    This is the associated polynomial equation of the quadratic/bilinear form.
  * More generally, adjoining a second set of variables $\vec{y} \coloneqq [y_0, \dots, y_{m-1}]^t$ for a bilinear pairing $b\colon M \otimes_R N \to R$ on free modules produces the bilinear polynomial:
    $$
    b(\vec{x}, \vec{y}) = \sum_{i=0}^{n-1}\sum_{j=0}^{m-1} b(e_i, f_j)\, x_i y_j \in R[x_0, \dots, x_{n-1}, y_0, \dots, y_{m-1}].
    $$
  * Functorial passage: defines a canonical passage $\mathrm{Sym}^2(M^\vee) \to R[x_0, \dots, x_{n-1}]$ mapping a form module $(M, b)$ to a graded algebra element / hypersurface equation in $\mathbb{A}^n_R$.

* **1-parameter family of schemes over $\mathbb{A}^1_R$:**
  * Adjoining a parameter $t$ as coordinate on the affine line $\mathbb{A}^1_R = \operatorname{Spec}(R[t])$, the relative equation
    $$
    b(\vec{x}, \vec{x}) - t = 0
    $$
    defines an affine relative scheme:
    $$
    \mathcal{X} \coloneqq \operatorname{Spec}\bigl(R[t, x_0, \dots, x_{n-1}] / (b(\vec{x}, \vec{x}) - t)\bigr) \longrightarrow \mathbb{A}^1_R = \operatorname{Spec}(R[t]).
    $$
  * This morphism $\pi\colon \mathcal{X} \to \mathbb{A}^1_R$ defines an honest flat 1-parameter family of quadric hypersurfaces over $\mathbb{A}^1_R$.
  * For each scalar $t_0 \in R$ (an $R$-point of the base $\mathbb{A}^1_R$), the scheme-theoretic fiber is the affine quadric:
    $$
    \mathcal{X}_{t_0} \coloneqq \pi^{-1}(t_0) = V(b(\vec{x}, \vec{x}) - t_0) \subset \mathbb{A}^n_R.
    $$

* **Transport of representation problems to integral points on scheme fibers:**
  * The fundamental problem in lattice and form theory — "find $v \in M$ such that $b(v, v) = t_0$" (e.g. finding roots, minimal vectors, or representations of numbers by quadratic forms) — is canonically transported to finding $R$-integral points on the fiber $\mathcal{X}_{t_0}$:
    $$
    \{v \in M \mid b(v, v) = t_0\} \;\cong\; \mathcal{X}_{t_0}(R) \;\coloneqq\; \operatorname{Hom}_{\mathbf{Sch}/R}(\operatorname{Spec}(R), \mathcal{X}_{t_0}).
    $$
  * Preamble dispatch rule: schemes cut out by bilinear and quadratic forms admit highly optimized, specialized algorithms from algebraic number theory and classical lattice theory:
    * Finite search and enumeration: Fincke–Pohst algorithm, Schnorr–Euchner enumeration, sphere decoding, and Voronoi cell algorithms for definite lattices over $\mathbb{Z}$.
    * Reduction algorithms: LLL, Korkine–Zolotarev (HKZ), and Minkowski reduction on the underlying free $\mathbb{Z}$-module.
    * Arithmetic geometry: Hasse–Minkowski local-global principle for representation over $\mathbb{Q}$, Siegel mass formulas, representation densities / local densities, and theta series coefficients generating modular forms.
  * The preamble must not route $\mathcal{X}_{t_0}(R)$ for quadric fibers through generic commutative algebra or generic Gröbner basis / Diophantine solvers; it must identify the quadratic/bilinear form origin and delegate directly to maintained lattice and number-theoretic engines behind the private adapter.

Intended owners: `categories/forms/polynomial.py` (`b.as_polynomial(basis)`), `categories/schemes/families.py` (`b.as_family(parameter='t')`), `categories/schemes/quadrics.py` (`QuadricHypersurface`, fiber specialization), `categories/lattices/representations.py` (integral points $\mathcal{X}_t(R)$ via Fincke–Pohst and Siegel mass computation).

## Desired capability: Category of Hodge structures (pure, mixed, polarized) and operations — intake 2026-09-19

Intake note from user 2026-09-19.

* **Pure Hodge structures ($\mathbf{HS}_k(R)$):**
  * Base ring $R \in \{\mathbb{Z}, \mathbb{Q}, \mathbb{R}\}$.
  * A pure Hodge structure of weight $k \in \mathbb{Z}$ over $R$ is a finite-rank $R$-module $H_R$ together with a Hodge decomposition of its complexification $H_\mathbb{C} \coloneqq H_R \otimes_R \mathbb{C}$:
    $$
    H_\mathbb{C} = \bigoplus_{p + q = k} H^{p,q}, \qquad \text{with } \overline{H^{p,q}} = H^{q,p},
    $$
    where conjugation is with respect to the real form $H_\mathbb{R} = H_R \otimes_R \mathbb{R}$.
  * Equivalent specification via decreasing Hodge filtration $F^\bullet$ on $H_\mathbb{C}$:
    $$
    F^p H_\mathbb{C} = \bigoplus_{r \ge p} H^{r, k-r}, \qquad \text{satisfying } F^p H_\mathbb{C} \oplus \overline{F^{k-p+1} H_\mathbb{C}} = H_\mathbb{C},
    $$
    with recovery $H^{p,q} = F^p H_\mathbb{C} \cap \overline{F^q H_\mathbb{C}}$.
  * Category $\mathbf{HS}(R) = \bigoplus_{k \in \mathbb{Z}} \mathbf{HS}_k(R)$: abelian, semi-simple for $R = \mathbb{Q}, \mathbb{R}$. Morphisms $f\colon H \to H'$ are $R$-linear maps preserving the bigrading $f_\mathbb{C}(H^{p,q}) \subseteq H'^{p,q}$ (or equivalently, strictly preserving the Hodge filtration).
  * Invariants: weight $k$, Hodge numbers $h^{p,q} = \dim_\mathbb{C} H^{p,q}$, Hodge diamond, and Hodge polynomial $\sum h^{p,q} u^p v^q$.

* **Polarized Hodge structures ($\mathbf{HS}_k^{\mathrm{pol}}(R)$):**
  * A polarization of $(H_R, H^{p,q})$ of weight $k$ is a bilinear form $Q\colon H_R \otimes_R H_R \to R$ satisfying:
    1. Symmetry: $Q(u, v) = (-1)^k Q(v, u)$ (symmetric for $k$ even, alternating for $k$ odd).
    2. Hodge-Riemann bilinear relations:
       - Orthogonality: $Q_\mathbb{C}(H^{p,q}, H^{p',q'}) = 0$ unless $p = q'$ and $q = p'$ (equivalently, $Q_\mathbb{C}(F^p, F^{k-p+1}) = 0$).
       - Positivity: The Hermitian form $h(u, v) \coloneqq i^{p-q} Q_\mathbb{C}(u, \bar{v})$ is positive definite on $H^{p,q}$.
  * The Weil operator $C\colon H_\mathbb{C} \to H_\mathbb{C}$, acting as $i^{p-q} \operatorname{id}$ on $H^{p,q}$, defines a positive-definite Riemannian metric $Q(C u, \bar{v}) > 0$ on $H_\mathbb{C}$.
  * Category $\mathbf{HS}_k^{\mathrm{pol}}(\mathbb{Q})$ is a semi-simple neutral Tannakian category.

* **Mixed Hodge structures ($\mathbf{MHS}(R)$ / Deligne):**
  * A mixed Hodge structure consists of:
    1. A finite-rank $R$-module $H_R$.
    2. An increasing weight filtration $W_\bullet$ on $H_\mathbb{Q} \coloneqq H_R \otimes_R \mathbb{Q}$:
       $$
       \cdots \subseteq W_{k-1} H_\mathbb{Q} \subseteq W_k H_\mathbb{Q} \subseteq W_{k+1} H_\mathbb{Q} \subseteq \cdots
       $$
    3. A decreasing Hodge filtration $F^\bullet$ on $H_\mathbb{C}$:
       $$
       \cdots \supseteq F^{p-1} H_\mathbb{C} \supseteq F^p H_\mathbb{C} \supseteq F^{p+1} H_\mathbb{C} \supseteq \cdots
       $$
    such that for each $k \in \mathbb{Z}$, the induced filtration $F^\bullet$ on the graded piece
    $$
    \operatorname{Gr}_k^W(H) \coloneqq W_k H_\mathbb{Q} / W_{k-1} H_\mathbb{Q}
    $$
    is a pure $\mathbb{Q}$-Hodge structure of weight $k$.
  * Deligne canonical bigrading: $H_\mathbb{C} = \bigoplus_{p,q} I^{p,q}$ with
    $$
    I^{p,q} = F^p \cap W_{p+q} \cap \left( \overline{F^q} \cap W_{p+q} + \sum_{j \ge 2} \overline{F^{q-j+1}} \cap W_{p+q-j} \right),
    $$
    satisfying $I^{p,q} \equiv \overline{I^{q,p}} \pmod{W_{p+q-2}}$.
  * Morphisms in $\mathbf{MHS}$: $R$-linear maps strictly compatible with both $W_\bullet$ and $F^\bullet$.
  * Theorem (Deligne): $\mathbf{MHS}$ is an abelian category; every morphism is strictly compatible with both filtrations; kernels, cokernels, images exist and inherit mixed Hodge structures.
  * Polarized mixed Hodge structures: graded-polarized MHS, where each pure graded piece $\operatorname{Gr}_k^W(H)$ is equipped with a polarization $Q_k$.

* **Tate twists and $\mathbb{Z}(1)$:**
  * The fundamental Tate twist $\mathbb{Z}(1) \coloneqq 2\pi i \mathbb{Z} \subset \mathbb{C}$ is the pure Hodge structure of weight $-2$, rank 1, with $H^{-1,-1} = \mathbb{C}$ and $H^{p,q} = 0$ otherwise.
  * For $m \in \mathbb{Z}$, $\mathbb{Z}(m) \coloneqq (2\pi i)^m \mathbb{Z}$ is pure of weight $-2m$ and type $(-m, -m)$.
  * Tate twist of a Hodge structure $H$: $H(m) \coloneqq H \otimes \mathbb{Z}(m)$.
    * Weight shift: $\operatorname{Gr}_{k-2m}^W(H(m)) = \operatorname{Gr}_k^W(H)(m)$ (weight lowered by $2m$).
    * Hodge filtration shift: $F^p(H(m)_\mathbb{C}) = F^{p+m}(H_\mathbb{C})$.
    * Bigrading shift: $H(m)^{p,q} = H^{p+m, q+m}$.

* **Standard operations and symmetric monoidal structure:**
  * **Direct Sum ($H \oplus H'$):**
    $W_k(H \oplus H') = W_k H \oplus W_k H'$, $F^p(H \oplus H') = F^p H \oplus F^p H'$, $(H \oplus H')^{p,q} = H^{p,q} \oplus H'^{p,q}$.
  * **Tensor Product ($H \otimes H'$):**
    * Weight filtration: $W_k(H \otimes H') = \sum_{i+j=k} W_i H \otimes W_j H'$.
    * Hodge filtration: $F^p(H \otimes H')_\mathbb{C} = \sum_{r+s=p} F^r H_\mathbb{C} \otimes F^s H'_\mathbb{C}$.
    * Bigrading: $(H \otimes H')^{p,q} = \bigoplus_{r+r'=p, s+s'=q} H^{r,s} \otimes H'^{r',s'}$.
    * Unit object: $\mathbb{Z}(0) = \mathbb{Z}$ of weight 0, type $(0,0)$.
  * **Dual ($H^\vee$) and Internal Hom ($\underline{\operatorname{Hom}}(H, H')$):**
    * $H^\vee \coloneqq \underline{\operatorname{Hom}}(H, \mathbb{Z}(0))$ with $W_{-k}(H^\vee) = (W_{k-1} H)^\perp$ and $(H^\vee)^{p,q} = (H^{-p, -q})^\vee$.
    * $\underline{\operatorname{Hom}}(H, H') \cong H^\vee \otimes H'$ with Hodge components $\underline{\operatorname{Hom}}(H, H')^{p,q} = \bigoplus_{r,s} \operatorname{Hom}(H^{r,s}, H'^{r+p, s+q})$.
  * **Exterior Powers ($\bigwedge^n H$) and Symmetric Powers ($\operatorname{Sym}^n H$):**
    * Sub- and quotient Hodge structures of $H^{\otimes n}$ via Young symmetrizers.
    * For pure $H$ of weight $k$, $\bigwedge^n H$ is pure of weight $n k$ with components $(\bigwedge^n H)^{p,q} = \sum_{\sum p_i = p, \sum q_i = q} \bigwedge^{p_1, q_1} \otimes \cdots$.
    * Determinant line: $\det(H) = \bigwedge^{\operatorname{rk}(H)} H$, rank-1 pure Hodge structure of weight $k \cdot \operatorname{rk}(H)$.
  * **Hodge classes:**
    $$
    \operatorname{Hdg}^{2p}(H) \coloneqq \operatorname{Hom}_{\mathbf{HS}}(\mathbb{Z}(-p), H) = H_R \cap H^{p,p}.
    $$
  * **Extensions and Intermediate Jacobians:**
    * The extension group $\operatorname{Ext}^1_{\mathbf{MHS}}(\mathbb{Z}(0), H)$ in the abelian category $\mathbf{MHS}$ is canonically identified with the generalized intermediate Jacobian:
      $$
      J(H) \coloneqq H_\mathbb{C} / (F^0 H_\mathbb{C} + H_\mathbb{Z}).
      $$
    * For $X$ smooth projective of dimension $n$, $J^k(X) = \operatorname{Ext}^1_{\mathbf{MHS}}(\mathbb{Z}(0), H^{2k-1}(X, \mathbb{Z})(k))$.

* **Preamble implementation requirement:**
  * Provide categories `PureHodgeStructures(R, weight=k)` (`HS`), `MixedHodgeStructures(R)` (`MHS`), `PolarizedHodgeStructures(R, weight=k)` (`PolHS`) in `categories/hodge/`.
  * Morphisms must be strictly filtered $R$-linear maps with exact kernel, cokernel, image, and direct sum functors.
  * Implement symmetric monoidal operations on objects: `H + H'`, `H * H'` (tensor), `H.dual()`, `H.exterior_power(n)`, `H.symmetric_power(n)`, `H.tate_twist(m)`, `H.weight()`, `H.hodge_diamond()`, `H.polarization()`, `H.intermediate_jacobian()`, and `H.hodge_classes()`.

Intended owners: `categories/hodge/hodge_structures.py` (`PureHodgeStructure`, `HodgeDecomposition`), `categories/hodge/mixed_hodge.py` (`MixedHodgeStructure`, `WeightFiltration`, `DeligneBigrading`), `categories/hodge/polarized.py` (`PolarizedHodgeStructure`, `RiemannHodgeRelations`), `categories/hodge/tate_twist.py` (`TateTwist` $\mathbb{Z}(m)$, $H(m)$), `categories/hodge/operations.py` (tensor, exterior, symmetric, dual, intermediate Jacobian).

## Desired capability: Projectivization of linear groups and matrix subgroups — intake 2026-09-19

Intake note from user 2026-09-19.

* **General algebraic projectivization of linear groups:**
  * Let $R$ be a commutative ring and let $V$ be a free $R$-module (or vector space over a field $k$).
  * For any linear group $G \le \operatorname{GL}(V)$ (or representation $\rho\colon G \to \operatorname{GL}(V)$), the *projectivization* of $G$ is the quotient by the central normal subgroup of scalar homotheties:
    $$
    \mathrm{P}G \coloneqq G / \bigl(G \cap (R^\times \cdot \operatorname{id}_V)\bigr),
    $$
    equipped with the canonical surjective projection homomorphism $\pi\colon G \twoheadrightarrow \mathrm{P}G$.
  * Realization as quotient by central signs: For groups over $\mathbb{Z}$, $\mathbb{R}$, or fields where the intersection consists of signs, $\mathrm{P}G$ typically realizes as:
    $$
    \mathrm{P}G = G / (G \cap \{\pm \operatorname{id}_V\}) = G / \langle -\operatorname{id}_V \rangle \quad (\text{when } -\operatorname{id}_V \in G).
    $$

* **Standard family specializations:**
  1. **General linear group:** $\operatorname{PGL}_n(R) \coloneqq \operatorname{GL}_n(R) / (R^\times \cdot I_n)$.
  2. **Special linear group:** $\operatorname{PSL}_n(R) \coloneqq \operatorname{SL}_n(R) / (\mu_n(R) \cdot I_n)$, where $\mu_n(R) = \{\lambda \in R^\times \mid \lambda^n = 1\}$. For $R = \mathbb{Z}$ or $\mathbb{R}$ with $n$ even, $\mu_n(R) = \{\pm 1\}$, so $\operatorname{PSL}_n(R) = \operatorname{SL}_n(R) / \{\pm I_n\}$.
  3. **Orthogonal groups of forms and lattices:** For a nondegenerate symmetric bilinear form module or lattice $(M, b)$, the center of the orthogonal group $\operatorname{O}(b)$ is $\{\pm \operatorname{id}_M\}$ (for char $\neq 2$). The projectivized orthogonal group is:
     $$
     \operatorname{PO}(b) \coloneqq \operatorname{O}(b) / \{\pm \operatorname{id}_M\}.
     $$
     Similarly, for the special orthogonal group $\operatorname{SO}(b)$, $\operatorname{PSO}(b) = \operatorname{SO}(b) / (\operatorname{SO}(b) \cap \{\pm \operatorname{id}_M\})$.
  4. **Symplectic groups:** $\operatorname{PSp}_{2g}(R) \coloneqq \operatorname{Sp}_{2g}(R) / \{\pm I_{2g}\}$.
  5. **Subgroups and arithmetic lattices:** For any subgroup $H \le \operatorname{GL}(V)$ (including arithmetic groups $\Gamma \le \operatorname{O}(L)$, congruence subgroups $\Gamma(N) \le \operatorname{SL}_2(\mathbb{Z})$, and Coxeter/reflection groups $W \le \operatorname{O}(L)$):
     $$
     \mathrm{P}H \coloneqq H / (H \cap \{\pm \operatorname{id}_V\}).
     $$

* **Geometric action on projective and hyperbolic spaces:**
  * **Projective space:** While $G \curvearrowright V$ has kernel $G \cap R^\times \cdot \operatorname{id}_V$, the projectivization $\mathrm{P}G$ acts faithfully on the projective space $\mathbb{P}(V) \coloneqq (V \setminus \{0\}) / R^\times$:
    $$
    \mathrm{P}G \curvearrowright \mathbb{P}(V), \qquad [g] \cdot [v] = [g(v)].
    $$
  * **Hyperbolic geometry:** For a Lorentzian lattice $L$ of signature $(1, n)$ (or $(n, 1)$), the hyperbolic space $\mathbb{H}^n$ is realized as an open convex domain in $\mathbb{P}(L_\mathbb{R})$ (the projective Klein model, or the future cone in $\mathbb{P}(L_\mathbb{R})$). The group of isometries preserving $\mathbb{H}^n$ acts faithfully via the projectivization:
    $$
    \operatorname{Isom}(\mathbb{H}^n) \cong \operatorname{PO}^+(1, n) \coloneqq \operatorname{O}^+(1, n) / \{\pm \operatorname{id}_L\}.
    $$
  * **Period domains:** For K3 and Enriques lattices, the period domain $\mathcal{D}_L \subset \mathbb{P}(L_\mathbb{C})$ admits a faithful action of the arithmetic quotient $\operatorname{PO}^+(L) \coloneqq \operatorname{O}^+(L) / \{\pm \operatorname{id}\}$.

* **Preamble implementation requirement:**
  * Provide an operational projectivization constructor/functor on matrix and linear groups:
    `G.projectivization() -> PG : ProjectiveGroups`
    with canonical projection morphism `G.projection_to_projectivization() -> Hom(G, PG)`.
  * Specialized subclasses: `PGL(n, R)`, `PSL(n, R)`, `PO(b)`, `PSO(b)`, `PSp(2g, R)`.
  * Support for arbitrary subgroups: `H.projectivization()` computing $H / (H \cap Z(\operatorname{GL}(V)))$ with explicit quotient presentation or permutation representation via GAP / libGAP adapter.
  * Faithful action on projective spaces: `PG.action_on(ProjectiveSpace(V))`.

Intended owners: `categories/groups/projectivization.py` (`ProjectiveGroup`, `ProjectivizationFunctor`), `categories/groups/matrix_groups.py` (`PGL`, `PSL`, `PSp`), `categories/lattices/orthogonal_group.py` (`PO(L)`, `PSO(L)`), `categories/hyperbolic/isometries.py` ($\operatorname{PO}^+(1,n)$ action on $\mathbb{H}^n$).


## Desired capability: Lambert expansions of generating functions — intake 2026-09-19

* **Mathematical background:**
  * **Lambert series definition:** Let $R$ be a commutative ring (e.g. $\mathbb{Z}$, $\mathbb{Q}$, or $\mathbb{C}$). A formal Lambert series with coefficients $a = (a_n)_{n \ge 1}$ is a formal power series expansion of the form:
    $$
    L_a(q) \coloneqq \sum_{n=1}^\infty a_n \frac{q^n}{1 - q^n} \in q R[[q]].
    $$
  * **Expansion to ordinary generating function (OGF):**
    Expanding each geometric term $\frac{q^n}{1 - q^n} = \sum_{k=1}^\infty q^{nk}$ and collecting powers of $q$:
    $$
    L_a(q) = \sum_{n=1}^\infty a_n \sum_{k=1}^\infty q^{nk} = \sum_{N=1}^\infty b_N q^N,
    $$
    where the OGF coefficients $b_N$ are given by the Dirichlet convolution of $a$ with the constant sequence $\mathbf{1}$:
    $$
    b_N = (a * \mathbf{1})(N) = \sum_{d \mid N} a_d.
    $$
  * **Lambert inversion (OGF to Lambert expansion via Möbius inversion):**
    Given an arbitrary formal power series with vanishing constant term $F(q) = \sum_{N=1}^\infty b_N q^N \in q R[[q]]$, there exists a unique sequence of coefficients $(a_n)_{n \ge 1}$ such that $F(q) = \sum_{n=1}^\infty a_n \frac{q^n}{1 - q^n}$.
    By Möbius inversion on the Dirichlet convolution $b = a * \mathbf{1}$:
    $$
    a_n = (b * \mu)(n) = \sum_{d \mid n} \mu(n/d) b_d = \sum_{d \mid n} \mu(d) b_{n/d},
    $$
    where $\mu$ is the classical arithmetic Möbius function ($\mu(1)=1$, $\mu(n)=(-1)^k$ for squarefree $n$ with $k$ prime factors, and $0$ otherwise).
  * **Relation to Dirichlet series and the Riemann zeta function:**
    Let $D_a(s) \coloneqq \sum_{n=1}^\infty \frac{a_n}{n^s}$ and $D_b(s) \coloneqq \sum_{N=1}^\infty \frac{b_N}{N^s}$ be the formal Dirichlet series of $a$ and $b$. Then:
    $$
    D_b(s) = D_a(s) \cdot \zeta(s), \qquad D_a(s) = \frac{D_b(s)}{\zeta(s)},
    $$
    reflecting the convolution $b = a * \mathbf{1}$ and the identity $\zeta(s)^{-1} = \sum_{n=1}^\infty \frac{\mu(n)}{n^s}$.
    Analytically, the Mellin transform of $L_a(e^{-t})$ recovers $\Gamma(s) D_a(s) \zeta(s) = \Gamma(s) D_b(s)$.

* **Canonical arithmetic and modular specimens:**
  1. **Divisor powers and Eisenstein series:**
     For $a_n = n^k$, $b_N = \sigma_k(N) = \sum_{d \mid N} d^k$.
     $$
     \sum_{n=1}^\infty n^k \frac{q^n}{1 - q^n} = \sum_{N=1}^\infty \sigma_k(N) q^N.
     $$
     * $k = 0$: $\sum_{n=1}^\infty \frac{q^n}{1 - q^n} = \sum_{N=1}^\infty d(N) q^N$ (divisor counting function $d(N) = \tau(N)$).
     * $k = 1$: $\sum_{n=1}^\infty n \frac{q^n}{1 - q^n} = \sum_{N=1}^\infty \sigma_1(N) q^N$.
     * Eisenstein series $q$-expansions for modular forms:
       $$
       E_2(q) = 1 - 24 \sum_{n=1}^\infty \frac{n q^n}{1 - q^n} = 1 - 24 \sum_{N=1}^\infty \sigma_1(N) q^N,
       $$
       $$
       E_4(q) = 1 + 240 \sum_{n=1}^\infty \frac{n^3 q^n}{1 - q^n} = 1 + 240 \sum_{N=1}^\infty \sigma_3(N) q^N,
       $$
       $$
       E_6(q) = 1 - 504 \sum_{n=1}^\infty \frac{n^5 q^n}{1 - q^n} = 1 - 504 \sum_{N=1}^\infty \sigma_5(N) q^N.
       $$
  2. **Euler totient function:**
     For $a_n = \phi(n)$, since $\sum_{d \mid N} \phi(d) = N$:
     $$
     \sum_{n=1}^\infty \phi(n) \frac{q^n}{1 - q^n} = \sum_{N=1}^\infty N q^N = \frac{q}{(1 - q)^2}.
     $$
  3. **Möbius function:**
     For $a_n = \mu(n)$, since $\sum_{d \mid N} \mu(d) = \delta_{N, 1}$:
     $$
     \sum_{n=1}^\infty \mu(n) \frac{q^n}{1 - q^n} = q.
     $$
  4. **Liouville function and Jacobi theta functions:**
     For $a_n = \lambda(n) = (-1)^{\Omega(n)}$, $\sum_{d \mid N} \lambda(d) = 1$ if $N$ is a square, $0$ otherwise:
     $$
     \sum_{n=1}^\infty \lambda(n) \frac{q^n}{1 - q^n} = \sum_{m=1}^\infty q^{m^2} = \frac{\theta_3(q) - 1}{2}.
     $$
  5. **Von Mangoldt function:**
     For $a_n = \Lambda(n)$, $\sum_{d \mid N} \Lambda(d) = \log N$:
     $$
     \sum_{n=1}^\infty \Lambda(n) \frac{q^n}{1 - q^n} = \sum_{N=1}^\infty \log(N) q^N.
     $$
  6. **Euler products, partition functions, and logarithmic derivatives:**
     For an infinite product $P(q) = \prod_{n=1}^\infty (1 - q^n)^{-c_n}$, the logarithm has a natural Lambert expansion:
     $$
     \log P(q) = \sum_{n=1}^\infty c_n \log \frac{1}{1 - q^n} = \sum_{n=1}^\infty c_n \sum_{k=1}^\infty \frac{q^{nk}}{k} = \sum_{m=1}^\infty \left(\sum_{d \mid m} \frac{c_d \cdot d}{m}\right) q^m.
     $$
     The Euler-operator / logarithmic derivative $q \frac{d}{dq} \log P(q)$ is directly a Lambert series:
     $$
     q \frac{d}{dq} \log P(q) = \sum_{n=1}^\infty n c_n \frac{q^n}{1 - q^n}.
     $$
     For the partition generating function $P(q) = \sum_{n=0}^\infty p(n) q^n = \prod_{n=1}^\infty (1 - q^n)^{-1}$ (with $c_n = 1$):
     $$
     \log P(q) = \sum_{m=1}^\infty \frac{1}{m} \frac{q^m}{1 - q^m}, \qquad q \frac{d}{dq} \log P(q) = \sum_{n=1}^\infty \frac{n q^n}{1 - q^n} = \sum_{N=1}^\infty \sigma_1(N) q^N.
     $$
     For Dedekind's eta function $\eta(\tau) = q^{1/24} \prod_{n=1}^\infty (1 - q^n)$:
     $$
     q \frac{d}{dq} \log \eta(\tau) = \frac{1}{24} - \sum_{n=1}^\infty \frac{n q^n}{1 - q^n} = \frac{E_2(q)}{24}.
     $$
  7. **Generalized Lambert series:**
     Series of the shape $\sum_{n=1}^\infty a_n \frac{q^{\alpha n + \beta}}{1 - c q^n}$, appearing in Ramanujan's ${}_1\psi_1$ summation formula, basic hypergeometric series, Jacobi forms, and mock modular forms.

* **Preamble implementation requirement:**
  * Define `LambertSeries(R)` over commutative rings $R$:
    * Representation: sequence of coefficients $(a_n)_{n \ge 1}$ (finite list/tuple with precision or lazy generator).
    * `LambertSeries.to_ogf(precision=N) -> FormalPowerSeries`: computes the truncated OGF $\sum_{n=1}^N b_n q^n$ via divisor sum convolution $b_n = \sum_{d \mid n} a_d$.
    * `FormalPowerSeries.to_lambert_series(precision=N) -> LambertSeries`: converts an OGF with $b_0 = 0$ to a Lambert series via Möbius inversion $a_n = \sum_{d \mid n} \mu(n/d) b_d$.
    * `LambertSeries.to_dirichlet_series() -> DirichletSeries`: associates $D_a(s)$, with identity $D_b(s) = D_a(s) \zeta(s)$.
    * Logarithmic derivative constructor: for infinite products $\prod (1 - q^n)^{-c_n}$, generate the corresponding Lambert series directly.
    * Integration with modular forms: provide explicit Lambert series representations for $E_2, E_4, E_6$, Jacobi theta functions, and partition generating functions.

Intended owners: `categories/generating_functions/lambert.py` (`LambertSeries`, `LambertExpansions`), `categories/rings/formal_power_series.py` (`to_lambert_series`, `from_lambert_series`), `categories/modular/eisenstein.py` (`EisensteinSeries.lambert_expansion()`).


## Desired capability: Computing Picard-Fuchs operators of families — intake 2026-09-19

* **Reference:** Malmendier & Schultz, *On mirror symmetry and irrationality of zeta values*, [arXiv:2403.07349v1](https://arxiv.org/abs/2403.07349) (see specifically p. 12–14 Eq. (2.17), Table 1, Table 2, Table 4, Section 5, and Section 6).

* **Mathematical background & algorithms:**
  * **Gauss-Manin connection and Picard-Fuchs equations:**
    For a smooth algebraic family $\pi \colon \mathcal{X} \to B$ over a 1-dimensional base curve $B$ (parameterized by $t \in \mathbb{P}^1$), the relative algebraic de Rham cohomology bundle $\mathcal{H}^k_{\mathrm{dR}}(\mathcal{X}/B) \coloneqq R^k \pi_* \Omega^\bullet_{\mathcal{X}/B}$ is equipped with the flat Gauss-Manin connection $\nabla \colon \mathcal{H}^k_{\mathrm{dR}} \to \mathcal{H}^k_{\mathrm{dR}} \otimes \Omega^1_B$.
    Periods $\omega_i(t) = \int_{\gamma_i} \Omega_t$ of a relative holomorphic form $\Omega_t \in H^{k,0}(X_t)$ over locally constant topological cycles $\gamma_i \in H_k(X_t, \mathbb{Z})$ are annihilated by a linear ordinary differential operator $\mathcal{L} \in \mathbb{C}(t)[\frac{d}{dt}]$ (or in terms of the Euler operator $\theta \coloneqq t \frac{d}{dt}$):
    $$
    \mathcal{L}(\omega) = a_n(t) \frac{d^n \omega}{dt^n} + \dots + a_1(t) \frac{d\omega}{dt} + a_0(t) \omega = 0.
    $$
  * **Explicit Weierstrass reduction (arXiv:2403.07349, p. 13, Eq. (2.17)):**
    For any 1-parameter family of elliptic curves in Weierstrass form:
    $$
    E_t \colon y^2 = 4x^3 - g_2(t)x - g_3(t),
    $$
    with discriminant $\Delta(t) = g_2(t)^3 - 27g_3(t)^2 \neq 0$ and the invariant differential $\delta(t) \coloneqq 3g_3(t)g_2'(t) - 2g_2(t)g_3'(t)$, the period vector $\vec{\omega}(t) = \begin{pmatrix} \omega_0(t) \\ \omega_1(t) \end{pmatrix}$ for the holomorphic 1-form $\Omega_t = \frac{dx}{y}$ and quasi-holomorphic forms satisfies the first-order Gauss-Manin system:
    $$
    \frac{d}{dt} \begin{pmatrix} \omega_0 \\ \omega_1 \end{pmatrix} = \begin{pmatrix} -\frac{1}{12} \frac{\Delta'(t)}{\Delta(t)} & \frac{3}{2}\frac{\delta(t)}{\Delta(t)} \\ -\frac{1}{8}\frac{g_2(t)\delta(t)}{\Delta(t)} & \frac{1}{12} \frac{\Delta'(t)}{\Delta(t)} \end{pmatrix} \begin{pmatrix} \omega_0 \\ \omega_1 \end{pmatrix}.
    $$
    Eliminating $\omega_1$ yields the explicit second-order Picard-Fuchs operator $\mathcal{L}_2$:
    $$
    \omega_1 = \frac{2\Delta}{3\delta} \left( \frac{d\omega_0}{dt} + \frac{1}{12}\frac{\Delta'}{\Delta} \omega_0 \right) \implies \mathcal{L}_2(\omega_0) = 0.
    $$
  * **Doran-Malmendier twist construction and Hadamard product:**
    Given an elliptic Calabi-Yau family $\mathcal{X} \to \mathbb{P}^1$ with Weierstrass model $W_t$ and a generalized functional invariant $(i, j, \alpha)$, the twist construction produces a new family $\widetilde{\mathcal{X}} \to \mathbb{P}^1$ of dimension $\dim X_t + 1$ (e.g. $M_n$-polarized K3 surfaces or Calabi-Yau threefolds).
    The periods of the twisted family are given by the Hadamard product:
    $$
    \widetilde{\omega}(t) = (\omega \star h)(t) = \sum_{n=0}^\infty a_n b_n t^n,
    $$
    where $h(t) = {}_2F_1(\dots)$ is the hypergeometric twist function. Consequently, the Picard-Fuchs operator of the twisted family factorizes as the Hadamard convolution of differential operators:
    $$
    \mathcal{L}_{n+1} = \mathcal{L}_{\mathrm{twist}} \star \mathcal{L}_n.
    $$
    For generalized functional invariant $(1, 1, 1)$, the twist function is $h(t) = {}_2F_1(1/2, 1/2; 1; 4t) = \sum_{n=0}^\infty \binom{2n}{n}^2 t^n$, annihilated by $\mathcal{L}_1 = \theta - 4t(2\theta + 1)$ (or $t(2+4\theta) - \theta$).
  * **Quantum differential operators and almost Calabi-Yau operators:**
    For an $n$-th order Calabi-Yau operator $\mathcal{L}_n$, the $(n+1)$-th order operator $\mathcal{D}_{n+1} \coloneqq \theta \cdot \mathcal{L}_n$ is maximally unipotent (MUM) at $t=0$, having canonical solutions $\omega_0, \dots, \omega_n$ with maximal log-depth $\log^n(t)$, recovering the quantum differential equation and virtual Yukawa coupling.

* **Explicit benchmarks & models from arXiv:2403.07349 to recover:**
  1. **Modular elliptic pencils (Table 4):**
     * **$X_0(3)$ (Hesse mirror):**
       $y^2 = 4x^3 + (-27 + 648t)x - (5832t^2 - 972t + 27)$,
       $\mathcal{L}_{2,3} = \theta^2 - 3t(3\theta+1)(3\theta+2)$.
     * **$X_0(4)$:**
       $\mathcal{L}_{2,4} = \theta^2 - 4t(2\theta+1)^2$.
     * **$X_1(5)$ (Apéry elliptic pencil for $\zeta(2)$):**
       $y^2 = 4x^3 - \frac{1}{12}(1 - 12t + 14t^2)x - \frac{1}{216}(1 - 18t + 30t^2 - t^3)$,
       $\mathcal{L}_{2,5} = \theta^2 - t(11\theta^2+11\theta+3) - t^2(\theta+1)^2$.
     * **$X_0(6)$:**
       $\mathcal{L}_{2,6} = \theta^2 - t(7\theta^2+7\theta+2) - 8t^2(\theta+1)^2$.
  2. **Anticanonical K3 pencils of rank-1 Fano threefolds $\mathcal{L}_{3,N}$ (Table 1):**
     * $N=2$ (Dwork K3 mirror / $M_2$-polarized):
       $\mathcal{L}_{3,2} = \theta^3 - 8t(2\theta+1)(4\theta+1)(4\theta+3) = \mathcal{L}_3 \star \mathcal{L}_{2,3}$.
     * $N=3$ ($M_3$-polarized):
       $\mathcal{L}_{3,3} = \theta^3 - 6t(2\theta+1)(3\theta+1)(3\theta+2) = \mathcal{L}_1 \star \mathcal{L}_{2,3}$.
     * $N=4$:
       $\mathcal{L}_{3,4} = \theta^3 - 8t(2\theta+1)^3$.
     * $N=5$:
       $\mathcal{L}_{3,5} = \theta^3 - 2t(2\theta+1)(11\theta^2+11\theta+3) - 4t^2(\theta+1)(2\theta+1)(2\theta+3)$.
     * $N=6$ (Beukers-Peters K3 pencil for Apéry $\zeta(3)$):
       $\mathcal{L}_{3,6} = \theta^3 - t(2\theta+1)(17\theta^2+17\theta+5) + t^2(\theta+1)^3$.
     * $N=7$:
       $\mathcal{L}_{3,7} = \theta^3 - 3t(2\theta+1)(13\theta^2+13\theta+4) - 3t^2(\theta+1)(3\theta+2)(3\theta+4)$.
     * $N=8$:
       $\mathcal{L}_{3,8} = \theta^3 - 4t(2\theta+1)(3\theta^2+3\theta+1) + 16t^2(\theta+1)^3$.
     * $N=9$:
       $\mathcal{L}_{3,9} = \theta^3 - 3t(2\theta+1)(3\theta^2+3\theta+1) - 27t^2(\theta+1)^3$.
     * $N=11$:
       $\mathcal{L}_{3,11} = \theta^3 - \frac{2}{5}t(2\theta+1)(17\theta^2+17\theta+6) - \frac{56}{25}t^2(\theta+1)(11\theta^2+22\theta+12) - \frac{126}{125}t^3(\theta+1)(\theta+2)(2\theta+3) - \frac{1504}{625}t^4(\theta+1)(\theta+2)(\theta+3)$.
  3. **Associated quantum operators and local Calabi-Yau 4-folds (Table 2 & Section 6):**
     * $\mathcal{D}_{4,N} = \theta \cdot \mathcal{L}_{3,N}$.
     * For $(N, d) = (2, 4)$ corresponding to Fano threefold $\mathbb{P}^3$, the pullback under $t \mapsto t^4$ of $\mathcal{L}_{3,2}$ gives the operator whose normalized dual instanton numbers $\mathsf{N}_k = -\frac{1}{4} \widetilde{N}_k$ match the genus-zero Gromov-Witten invariants of local $K_{\mathbb{P}^3}$ (Klemm-Pandharipande):
       $\mathsf{N}_1 = -20, \mathsf{N}_2 = -820, \mathsf{N}_3 = -68060, \mathsf{N}_4 = -7486440, \dots$

* **Preamble implementation requirements:**
  * **Fuchsian differential operator algebra:**
    `FuchsianDifferentialOperator(R, var='t', d_var='theta')` supporting algebraic operations, conversion between $\frac{d}{dt}$ and $\theta = t\frac{d}{dt}$, indicial equation at singular points, and MUM classification.
  * **Weierstrass Picard-Fuchs constructor:**
    `PicardFuchsFromWeierstrass(g2, g3, t)` implementing Stiller's matrix formula Eq. (2.17) via $\Delta(t)$ and $\delta(t)$, automatically eliminating to output $\mathcal{L}_2$.
  * **Griffiths-Dwork reduction:**
    For projective hypersurfaces $F(x_0, \dots, x_n; t) = 0$, pole-order reduction of rational differential forms in the Jacobian ideal $J(F)$ to generate the Gauss-Manin matrix and Picard-Fuchs operator.
  * **Hadamard convolution of differential operators:**
    `hadamard_product_operator(L1, L2)` computing the differential operator annihilating the Hadamard product $\sum a_n b_n t^n$.
  * **Pullback and base-change:**
    `L.pullback(t_map)` computing the operator under substitution $t \mapsto f(s)$.

Intended owners: `categories/differential_equations/picard_fuchs.py` (`FuchsianOperator`, `PicardFuchsEquation`), `categories/schemes/elliptic_surfaces/weierstrass_picard_fuchs.py` (`WeierstrassPicardFuchs`), `categories/cohomology/gauss_manin.py` (`GaussManinConnection`, `GriffithsDworkReduction`), `categories/schemes/k3/fano_mirrors.py` (`FanoK3PicardFuchsCatalogue`).


## Desired capability: Converting linear recurrences to differential equations symbolically — intake 2026-09-19

* **Mathematical background & algorithms:**
  * **Holonomic / D-finite correspondence:**
    A sequence $a = (a_n)_{n \ge 0}$ over a field $K$ of characteristic zero (e.g. $\mathbb{Q}$ or $\mathbb{Q}(t)$) is *P-recursive* (or holonomic) of order $r$ if it satisfies a linear recurrence relation with polynomial coefficients:
    $$
    \sum_{i=0}^r p_i(n) a_{n+i} = 0 \quad (\text{or } = g(n)), \qquad p_i(n) \in K[n], \; p_r(n) \neq 0.
    $$
    A formal power series $F(t) = \sum_{n=0}^\infty a_n t^n$ (ordinary generating function, OGF) or $E(t) = \sum_{n=0}^\infty a_n \frac{t^n}{n!}$ (exponential generating function, EGF) is *D-finite* (differentially finite) if its formal derivatives generate a finite-dimensional $K(t)$-vector space, i.e., it satisfies a linear ordinary differential equation:
    $$
    \sum_{j=0}^d q_j(t) F^{(j)}(t) = 0 \quad (\text{or } = P(t)), \qquad q_j(t) \in K[t], \; q_d(t) \neq 0.
    $$
    A foundational theorem of Stanley, Lipshitz, and Zeilberger establishes that a sequence $(a_n)_{n \ge 0}$ is P-recursive if and only if its OGF $F(t)$ is D-finite, if and only if its EGF $E(t)$ is D-finite.

  * **Ore algebras and non-commutative operator rings:**
    The transformation is algebraically formulated as an isomorphism / module transition between Ore algebras $R[X; \sigma, \delta]$ with commutation relation $X \cdot r = \sigma(r) X + \delta(r)$:
    1. **Shift Ore algebra (recurrence operators):**
       $\mathbb{A}_{\mathrm{shift}} \coloneqq K[n]\langle S_n \rangle$, where $\sigma(n) = n+1$ and $\delta = 0$, so that $S_n \cdot n = (n+1) S_n$.
       A recurrence is an annihilating operator $L_{\mathrm{rec}} = \sum_{i=0}^r p_i(n) S_n^i \in K[n]\langle S_n \rangle$.
    2. **Differential / Weyl Ore algebra:**
       $\mathbb{A}_{\mathrm{diff}} \coloneqq K[t]\langle \partial_t \rangle$, where $\sigma = \mathrm{id}$ and $\delta = \frac{d}{dt}$, with Heisenberg commutation $[\partial_t, t] = \partial_t t - t \partial_t = 1$.
    3. **Euler / theta Ore algebra:**
       $\mathbb{A}_{\theta} \coloneqq K[t]\langle \theta \rangle$, where $\theta \coloneqq t \partial_t$, with commutation $[\theta, t] = \theta t - t \theta = t$, or equivalently $\theta \cdot t = t(\theta + 1)$.

  * **Symbolic conversion dictionary for ordinary generating functions (OGF):**
    For $F(t) = \sum_{n=0}^\infty a_n t^n$:
    * Multiplication by $n$:
      $$
      \sum_{n=0}^\infty n a_n t^n = t \frac{d}{dt} F(t) = \theta F(t), \qquad \sum_{n=0}^\infty n^k a_n t^n = \theta^k F(t).
      $$
    * Shifted terms:
      Writing the recurrence in backward form with shifts $a_{n-j}$:
      $$
      \sum_{n=j}^\infty a_{n-j} n^k t^n = t^j \sum_{m=0}^\infty a_m (m+j)^k t^m = t^j (\theta + j)^k F(t).
      $$
    * General operator translation:
      Given a recurrence $\sum_{j=0}^r \sum_{k=0}^d c_{j,k} n^k a_{n-j} = 0$ valid for $n \ge n_0$:
      $$
      \mathcal{L}(\theta, t) \coloneqq \sum_{j=0}^r t^j P_j(\theta), \qquad P_j(\theta) = \sum_{k=0}^d c_{j,k} (\theta + j)^k.
      $$
      Initial terms $a_0, \dots, a_{n_0-1}$ generate an explicit polynomial inhomogeneous right-hand side $P(t) \in K[t]$:
      $$
      \mathcal{L}(\theta, t) F(t) = P(t).
      $$
    * Converting from Euler operator $\theta = t \partial_t$ to standard derivatives $\partial_t^m = \frac{d^m}{dt^m}$:
      $$
      \theta^k = \sum_{m=0}^k \left\{ \begin{matrix} k \\ m \end{matrix} \right\} t^m \partial_t^m,
      $$
      where $\left\{ \begin{matrix} k \\ m \end{matrix} \right\}$ are the Stirling numbers of the second kind.

  * **Symbolic conversion dictionary for exponential generating functions (EGF):**
    For $E(t) = \sum_{n=0}^\infty a_n \frac{t^n}{n!}$:
    $$
    a_{n+1} \longleftrightarrow \partial_t E(t), \qquad n a_n \longleftrightarrow t \partial_t E(t).
    $$
    This realizes a direct algebra isomorphism between the shift algebra $K[n]\langle S_n \rangle$ and the Weyl algebra $K[t]\langle \partial_t \rangle$.
    The map between OGF and EGF differential equations corresponds to the formal Borel and Laplace transforms on differential operators ($\partial_t \longleftrightarrow t^{-1} \theta$).

* **Canonical specimens & test benchmarks:**
  1. **Apéry recurrence for $\zeta(2)$:**
     Recurrence: $n^2 a_n - (11n^2 - 11n + 3) a_{n-1} - (n-1)^2 a_{n-2} = 0$, with $a_0 = 1, a_1 = 3$.
     Transforms into the second-order Picard-Fuchs operator for $X_1(5)$ modular curves:
     $$
     \mathcal{L}_2 = \theta^2 - t(11\theta^2 + 11\theta + 3) - t^2(\theta+1)^2.
     $$
     The second Apéry sequence $b_0=0, b_1=5$ satisfies the non-homogeneous equation $\mathcal{L}_2(b(t)) = 5t$.
  2. **Apéry recurrence for $\zeta(3)$:**
     Recurrence: $n^3 A_n - (2n-1)(17n^2 - 17n + 5) A_{n-1} + (n-1)^3 A_{n-2} = 0$, with $A_0 = 1, A_1 = 5$.
     Transforms into the third-order Calabi-Yau Picard-Fuchs operator for the Beukers-Peters K3 pencil:
     $$
     \mathcal{L}_3 = \theta^3 - t(2\theta+1)(17\theta^2 + 17\theta + 5) + t^2(\theta+1)^3.
     $$
     The auxiliary sequence $B_n$ satisfies the non-homogeneous equation $\mathcal{L}_3(B(t)) = 6t$.
  3. **Hypergeometric sequence:**
     $(n+1)^2 a_{n+1} - (n + 1/2)^2 a_n = 0 \implies \left( \theta^2 - 4t(\theta + 1/2)^2 \right) F(t) = 0$ (the twist operator $\mathcal{L}_1$).
  4. **Factorial / divergent series:**
     $a_n - n a_{n-1} = 0 \implies (1 - t(\theta + 1)) F(t) = 1 \implies t^2 F'' + (3t - 1) F' + F = -1$.

* **Preamble implementation requirements:**
  * **Ore algebra representation:**
    `OreAlgebra(BaseRing, generator_name, derivation=None, endomorphism=None)`:
    Representing non-commutative polynomial rings $R[X; \sigma, \delta]$, covering the shift ring $K[n]\langle S_n \rangle$, the Weyl algebra $K[t]\langle \partial_t \rangle$, and the Euler ring $K[t]\langle \theta \rangle$.
  * **Recurrence-to-differential-equation conversion:**
    `recurrence_to_diffeq(rec_expr, a_seq, n_var, t_var, form='theta', kind='ogf', initial_values=None)`:
    Translates a polynomial linear recurrence into an annihilating differential operator $\mathcal{L} \in K[t][\theta]$ or $K[t][\partial_t]$, tracking the exact inhomogeneous polynomial $P(t)$ contributed by initial values.
  * **Differential-equation-to-recurrence conversion:**
    `diffeq_to_recurrence(diffeq_op, t_var, n_var, a_seq, form='theta', kind='ogf')`:
    Inverse translation from a Fuchsian / linear differential operator to the corresponding recurrence on series coefficients.
  * **Algorithmic reuse and adapters:**
    Wrap existing CAS implementations (e.g. SageMath `sage.rings.polynomial.ore_algebra` / `rectodiffeq` and `diffeqtorec`, SymPy `sympy.holonomic.recurrence_to_diffeq`, and Maple `gfun` reference algorithms) behind owned preamble interfaces adhering strictly to `OWN-01` through `OWN-14`.

Intended owners: `categories/differential_equations/ore_algebra.py` (`OreAlgebra`, `OrePolynomial`), `categories/differential_equations/recurrence_to_diffeq.py` (`recurrence_to_diffeq`, `diffeq_to_recurrence`), `categories/algebras/weyl_algebra.py` (`WeylAlgebra`, `EulerAlgebra`).


## Desired capability: Large poset navigation, 2D grid layouts, Coxeter subdiagrams, and G-poset quotients — intake 2026-09-19

* **Functional & Mathematical Requirements:**
  * **2D Grid and Planar Layout for Extremely Large Posets ($10^3$ to $10^6$ nodes):**
    * Stratified / ranked grid coordinates $(x, y) \in \mathbb{R}^2$:
      - Vertical coordinate $y = \rho(v)$ indexed by the rank function $\rho \colon P \to \mathbb{Z}_{\ge 0}$ (e.g. cardinality of vertex subset $|J|$, dimension, or rank of parabolic subgroup).
      - Horizontal coordinate $x$ determined by barycentric, force-directed, or order-preserving band layout to minimize edge crossings and separate connected components.
    * Virtualized viewport rendering (WebGL / HTML5 Canvas / SVG with level-of-detail aggregation) supporting smooth zooming, panning, and dense cluster collapse.
    * Node decorations & visual styling:
      - Shape, stroke, and fill parameterized by mathematical classification (e.g. elliptic / finite, parabolic / affine, compact hyperbolic / Lanner, non-compact hyperbolic).
      - Distinct visual markers for maximal elements (maximal elliptic, maximal parabolic).
      - Badges indicating subgroup rank, Coxeter determinant $\det(B_J)$, or orbit multiplicity.
    * Information inspectors:
      - Interactive tooltips on hover displaying concise summaries (vertex set $J$, Dynkin label, determinant).
      - Click-to-pin inspector in a dedicated sidebar/drawer displaying detailed invariants: full induced subgraph diagram, Gram matrix, signature $(p, q, z)$, root basis, Weyl group order $|W_J|$, and automorphism group $\operatorname{Aut}(J)$.

  * **Chain Tracing & Filtration Navigation:**
    * Interactive element selection: clicking an element $x \in P$ enters chain-tracing mode.
    * Upward filtration / principal filter $\uparrow x \coloneqq \{ y \in P \mid x \le y \}$:
      - Highlights all saturated chains from $x$ up to all maximal elements containing $x$.
    * Downward filtration / principal ideal $\downarrow x \coloneqq \{ y \in P \mid y \le x \}$:
      - Highlights all saturated chains from $x$ down to minimal elements ($\emptyset$ or rank-1 singletons).
    * Visual dimming of all poset nodes and covering edges not belonging to $\uparrow x \cup \downarrow x$.

  * **Coxeter Subdiagram Posets for Small Diagrams ($n < 25$ vertices):**
    * For an ambient Coxeter diagram $\Gamma = (V, E, m)$ with $|V| < 25$:
      - Full subdiagram poset $\mathcal{P}(\Gamma) \cong 2^V$ ordered by inclusion $J \subseteq J'$.
      - Induced sub-poset of **elliptic subdiagrams** $\mathcal{P}_{\mathrm{ell}}(\Gamma)$: subdiagrams whose Gram matrix $B_J$ is positive definite (finite reflection subgroups).
      - Induced sub-poset of **parabolic subdiagrams** $\mathcal{P}_{\mathrm{par}}(\Gamma)$: subdiagrams whose connected components are positive semidefinite (affine / parabolic reflection subgroups).
      - Identification of **maximal elliptic** subdiagrams and **maximal parabolic** subdiagrams (fundamental cusps and facets of Vinberg polytopes).
      - **Lanner subdiagrams**: minimal non-elliptic connected subdiagrams with signature $(|J|-1, 1, 0)$ (compact hyperbolic simplices).

  * **$G$-Posets and Symmetries of Coxeter Diagrams:**
    * Group action $G \curvearrowright P$: an order-preserving automorphism action, where $g \cdot x \le g \cdot y$ whenever $x \le y$.
    * Symmetry groups $G$:
      - Full diagram automorphism group $G = \operatorname{Aut}(\Gamma)$ preserving vertex labels and edge weights.
      - Automorphism group of a maximal element $G = \operatorname{Aut}(M)$ for $M \in \max(P)$.
      - Diagram folding groups (e.g. $\mathbb{Z}/2$ or $\mathfrak{S}_3$ outer automorphisms inducing non-simply laced folded diagrams).
    * **Quotient Poset $P/G$:**
      - Nodes are $G$-orbits $[x] = G \cdot x = \{ g \cdot x \mid g \in G \}$.
      - Induced partial order on orbits:
        $$
        [x] \le [y] \iff \exists g \in G \text{ such that } x \le g \cdot y.
        $$
      - Canonical orbit representative selection (e.g. lexicographically minimal vertex subset).
    * **Bidirectional Navigation between $P$ and $P/G$:**
      - **Projection ($P \twoheadrightarrow P/G$):** Collapse the full subdiagram poset $P$ into the much smaller quotient poset $P/G$, displaying orbit classes with node size proportional to orbit size $|G \cdot x| = [G : \operatorname{Stab}_G(x)]$.
      - **Unrolling / Lifting ($P/G \hookrightarrow P$):** Clicking an orbit node $[x] \in P/G$ unrolls its complete fiber of isomorphic subdiagrams in $P$, displaying their mutual covering relations and cross-orbit arrows.

* **Preamble implementation requirements:**
  * **Mathematical core:**
    - `LargePoset(elements, covering_relation)`: memory-efficient poset representation with fast transitive closure, interval queries, and bitset-accelerated filters/ideals.
    - `CoxeterSubdiagramPoset(Gamma)`: specialized generator for subdiagram lattices of Coxeter diagrams, computing Gram matrices, determinants, and classification predicates (elliptic, parabolic, Lanner).
    - `GPoset(poset, group, action)`: $G$-poset structure supporting orbit decomposition, stabilizer computation, and quotient poset construction $P/G$.
  * **Visualization and interactive UI:**
    - `PosetGrid2DLayout(poset)`: algorithm assigning 2D coordinates $(x, y)$ with layer ranking and horizontal crossing minimization.
    - Interactive front-end module (HTML/SVG/Canvas export with embedded JS): tooltips, sidebar inspector, chain tracing toggle, and $P \leftrightarrow P/G$ orbit toggle.

Intended owners: `categories/posets/large_poset.py` (`LargePoset`, `GPoset`, `QuotientPoset`), `categories/coxeter/subdiagram_posets.py` (`CoxeterSubdiagramPoset`, `EllipticPoset`, `ParabolicPoset`), `categories/graphs/diagram_automorphisms.py` (`DiagramAutomorphisms`, `DiagramQuotient`), `src/dzack_research/preamble/visualization/poset_navigator.py`.


## Desired capability: q-analogues — intake 2026-09-19

* **Mathematical background & foundational operations:**
  * **$q$-numbers ($q$-brackets) and quantum integers:**
    For an indeterminate $q$ (or specialized value in a ring $R$):
    - Classical $q$-bracket:
      $$
      [n]_q \;\coloneqq\; \frac{1 - q^n}{1 - q} \;=\; 1 + q + q^2 + \dots + q^{n-1} \;=\; \sum_{k=0}^{n-1} q^k \;\in\; \mathbb{Z}[q], \qquad \lim_{q \to 1} [n]_q = n.
      $$
    - Symmetric quantum integer (Lie theory / quantum groups):
      $$
      [n]_q^{\mathrm{sym}} \;\coloneqq\; \frac{q^n - q^{-n}}{q - q^{-1}} \;=\; q^{n-1} + q^{n-3} + \dots + q^{-(n-1)} \;\in\; \mathbb{Z}[q, q^{-1}].
      $$

  * **$q$-factorials:**
    $$
    [n]_q! \;\coloneqq\; \prod_{k=1}^n [k]_q \;=\; [1]_q [2]_q \cdots [n]_q, \qquad [0]_q! \;\coloneqq\; 1.
    $$

  * **Gaussian binomial coefficients ($q$-binomials):**
    For integers $0 \le k \le n$:
    $$
    \binom{n}{k}_q \;\coloneqq\; \frac{[n]_q!}{[k]_q! [n-k]_q!} \;=\; \frac{\prod_{i=0}^{k-1} (1 - q^{n-i})}{\prod_{i=1}^k (1 - q^i)} \;\in\; \mathbb{Z}[q].
    $$
    * **Geometric interpretation:**
      Counts the number of $k$-dimensional linear subspaces in an $n$-dimensional vector space over the finite field $\mathbb{F}_q$:
      $$
      \binom{n}{k}_q \;=\; \left| \operatorname{Gr}(k, n)(\mathbb{F}_q) \right| \;=\; \frac{(q^n - 1)(q^n - q)\cdots(q^n - q^{k-1})}{(q^k - 1)(q^k - q)\cdots(q^k - q^{k-1})}.
      $$
    * **Combinatorial generating function:**
      Generating function for integer partitions fitting inside a $k \times (n-k)$ rectangle:
      $$
      \binom{n}{k}_q \;=\; \sum_{\lambda \subseteq k \times (n-k)} q^{|\lambda|}.
      $$
      Also computes the Poincaré polynomial of the Grassmannian Bruhat quotient $\mathfrak{S}_n / (\mathfrak{S}_k \times \mathfrak{S}_{n-k})$ by Coxeter length $\ell(w)$ (number of inversions).
    * **Recurrence relations ($q$-Pascal identities):**
      $$
      \binom{n}{k}_q \;=\; \binom{n-1}{k-1}_q + q^k \binom{n-1}{k}_q \;=\; q^{n-k} \binom{n-1}{k-1}_q + \binom{n-1}{k}_q.
      $$
    * **$q$-binomial theorem:**
      $$
      \prod_{i=0}^{n-1} (1 + q^i x) \;=\; \sum_{k=0}^n q^{\binom{k}{2}} \binom{n}{k}_q x^k, \qquad \frac{1}{(x; q)_n} \;=\; \sum_{k=0}^\infty \binom{n+k-1}{k}_q x^k.
      $$

  * **$q$-multinomial coefficients:**
    For a composition $n = k_1 + \dots + k_m$:
    $$
    \binom{n}{k_1, \dots, k_m}_q \;\coloneqq\; \frac{[n]_q!}{[k_1]_q! \cdots [k_m]_q!}.
    $$
    Counts partial flag varieties of type $(k_1, \dots, k_m)$ in $\mathbb{F}_q^n$.

  * **$q$-Pochhammer symbol:**
    $$
    (a; q)_n \;\coloneqq\; \prod_{k=0}^{n-1} (1 - a q^k), \qquad (a; q)_\infty \;\coloneqq\; \prod_{k=0}^\infty (1 - a q^k).
    $$

  * **Jackson $q$-calculus:**
    * **Jackson $q$-derivative:**
      $$
      D_q f(x) \;\coloneqq\; \frac{f(x) - f(qx)}{(1 - q)x}, \qquad D_q(x^n) = [n]_q x^{n-1}, \qquad \lim_{q \to 1} D_q f(x) = f'(x).
      $$
      Product rule: $D_q(f(x)g(x)) = f(qx) D_q g(x) + g(x) D_q f(x)$.
    * **Jackson $q$-integral:**
      $$
      \int_0^a f(x) \, d_q x \;\coloneqq\; (1 - q) a \sum_{n=0}^\infty q^n f(a q^n).
      $$

  * **$q$-exponential, $q$-gamma, and $q$-beta functions:**
    - Little $q$-exponential: $e_q(z) \coloneqq \sum_{n=0}^\infty \frac{z^n}{[n]_q!} = \frac{1}{((1-q)z; q)_\infty}$.
    - Big $q$-exponential: $E_q(z) \coloneqq \sum_{n=0}^\infty q^{\binom{n}{2}} \frac{z^n}{[n]_q!} = (-(1-q)z; q)_\infty$, with $e_q(z) E_q(-z) = 1$.
    - $q$-Gamma function: $\Gamma_q(x) \coloneqq \frac{(q; q)_\infty}{(q^x; q)_\infty} (1 - q)^{1-x}$, satisfying $\Gamma_q(x+1) = [x]_q \Gamma_q(x)$.

  * **Basic hypergeometric series ($q$-hypergeometric functions):**
    Generalized basic hypergeometric series:
    $$
    {}_r\phi_s\left(\begin{matrix} a_1, \dots, a_r \\ b_1, \dots, b_s \end{matrix}; q, z\right) \;\coloneqq\; \sum_{n=0}^\infty \frac{(a_1; q)_n \cdots (a_r; q)_n}{(b_1; q)_n \cdots (b_s; q)_n} \frac{z^n}{(q; q)_n} \left((-1)^n q^{\binom{n}{2}}\right)^{1 + s - r}.
    $$
    Covers Heine's transformations, Ramanujan's ${}_1\psi_1$ summation formula, and the Rogers–Ramanujan identities:
    $$
    \sum_{n=0}^\infty \frac{q^{n^2}}{(q; q)_n} \;=\; \frac{1}{(q; q^5)_\infty (q^4; q^5)_\infty}, \qquad \sum_{n=0}^\infty \frac{q^{n^2+n}}{(q; q)_n} \;=\; \frac{1}{(q^2; q^5)_\infty (q^3; q^5)_\infty}.
    $$

  * **Poincaré polynomials of Coxeter groups and Hecke algebras:**
    - For a finite Coxeter group $W$ with simple reflections $S$ and exponent degrees $d_1, \dots, d_n$:
      $$
      W(q) \;\coloneqq\; \sum_{w \in W} q^{\ell(w)} \;=\; \prod_{i=1}^n [d_i]_q.
      $$
    - For the symmetric group $\mathfrak{S}_n$: $\mathfrak{S}_n(q) = [n]_q!$.
    - Iwahori–Hecke algebra $\mathcal{H}_q(W)$ over $\mathbb{Z}[q^{1/2}, q^{-1/2}]$ with generators $T_s$ satisfying quadratic relations $(T_s - q)(T_s + 1) = 0$ and braid relations.
    - Quantum groups $U_q(\mathfrak{g})$: quantum Serre relations and quantum Casimir operators defined via Gaussian binomials and $[n]_q!$.

* **Preamble implementation requirements:**
  * **Core combinatorics module:** `categories/combinatorics/q_analogues.py`
    - `q_bracket(n, q=None, sym=False)`: computes $[n]_q$ as an integer, polynomial in $\mathbb{Z}[q]$, or Laurent polynomial $\mathbb{Z}[q, q^{-1}]$.
    - `q_factorial(n, q=None)`: computes $[n]_q!$.
    - `q_binomial(n, k, q=None)`: computes $\binom{n}{k}_q$, with fast computation via $q$-Pascal recurrence or product formula.
    - `q_multinomial(n, parts, q=None)`: computes Gaussian multinomial coefficients.
    - `q_pochhammer(a, q, n=None)`: computes finite product $(a; q)_n$ or lazy power series for $(a; q)_\infty$.
  * **Jackson calculus and special functions:** `categories/special_functions/q_hypergeometric.py`
    - `q_derivative(f, var='x', q='q')`: applies Jackson derivative operator $D_q$ to symbolic expressions and polynomials.
    - `q_integral(f, var='x', a=1, q='q', terms=50)`: evaluates Jackson $q$-integral.
    - `q_hypergeometric(num, den, q, z, prec)`: evaluates ${}_r\phi_s$ basic hypergeometric series to precision.
    - `q_exponential(z, q, kind='little', prec=20)`: computes $e_q(z)$ or $E_q(z)$.
  * **Algebraic integration:**
    - Integration with `categories/algebras/hecke_algebra.py` for Poincaré polynomials and Kazhdan–Lusztig polynomials.
    - Integration with `categories/quantum_groups/quantum_integers.py` for representation theory and quantum Casimir invariants.

Intended owners: `categories/combinatorics/q_analogues.py` (`QBracket`, `QFactorial`, `QBinomial`, `QPochhammer`), `categories/special_functions/q_hypergeometric.py` (`JacksonDerivative`, `QHypergeometricSeries`), `categories/quantum_groups/quantum_integers.py` (`QuantumInteger`, `QuantumBinomial`), `categories/algebras/hecke_algebra.py` (`HeckeAlgebra`, `PoincarePolynomial`).


## Desired capability: Elliptic surfaces, elliptic fibrations, Mordell-Weil groups, Weierstrass forms, and Néron models — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **Elliptic fibrations and Jacobian surfaces:**
    * An *elliptic fibration* is a smooth projective surface $S$ equipped with a surjective morphism $\pi \colon S \to C$ to a smooth complete curve $C$ such that the generic fiber $E_\eta \coloneqq \pi^{-1}(\eta)$ is a smooth curve of genus 1 over the function field $K = k(C)$.
    * A *Jacobian elliptic surface* admits a section $O \colon C \to S$ (the zero section), identifying the generic fiber $E_\eta$ with an elliptic curve over $K$.
    * **Fundamental line bundle:**
      $\mathbb{L} \coloneqq (R^1 \pi_* \mathcal{O}_S)^\vee \cong \mathcal{O}_C(-O(C))|_{O(C)}^\vee$.
    * **Kodaira canonical bundle formula:**
      $$
      K_S \;\cong\; \pi^*(K_C \otimes \mathbb{L}) \otimes \mathcal{O}_S\left(\sum_i (m_i - 1) F_i\right),
      $$
      where $F_i$ are multiple fibers of multiplicity $m_i$.
      For a relatively minimal Jacobian surface over $C = \mathbb{P}^1$ without multiple fibers:
      $\deg(\mathbb{L}) = \chi(\mathcal{O}_S) = \frac{c_1(S)^2 + c_2(S)}{12}$.
      - $\chi(\mathcal{O}_S) = 1$: Rational elliptic surfaces ($c_2 = 12$, $K_S = -F$, e.g. Hesse pencil, pencil of cubics through 9 base points).
      - $\chi(\mathcal{O}_S) = 2$: Elliptic K3 surfaces ($c_2 = 24$, $K_S = \mathcal{O}_S$).
      - Enriques surfaces: $\chi = 1, 2K_S = 0$, elliptic fibrations over $\mathbb{P}^1$ having exactly two double fibers $2F_1, 2F_2$.

  * **Weierstrass models and resolution:**
    * Projective bundle $\mathbf{P} = \mathbb{P}(\mathcal{O}_C \oplus \mathbb{L}^{\otimes 2} \oplus \mathbb{L}^{\otimes 3})$ over $C$, with fiber coordinates $[z : x : y]$.
    * In the affine chart $z=1$, the Weierstrass model $W \subset \mathbf{P}$ is defined by:
      $$
      y^2 + a_1 x y + a_3 y \;=\; x^3 + a_2 x^2 + a_4 x + a_6,
      $$
      or in short form (characteristic $\neq 2, 3$):
      $$
      y^2 \;=\; 4x^3 - g_2 x - g_3 \quad (\text{or } y^2 = x^3 + f x + g),
      $$
      where sections $g_2 \in H^0(C, \mathbb{L}^{\otimes 4})$, $g_3 \in H^0(C, \mathbb{L}^{\otimes 6})$.
    * **Discriminant section:** $\Delta \coloneqq g_2^3 - 27 g_3^2 \in H^0(C, \mathbb{L}^{\otimes 12})$. The Euler characteristic satisfies $c_2(S) = \sum_{v} e(F_v) = \deg(\Delta) = 12 \chi(\mathcal{O}_S)$.
    * **Functional $j$-invariant:** $J \coloneqq 1728 \frac{g_2^3}{\Delta} \colon C \to \mathbb{P}^1$.
    * **Miranda resolution:** The Weierstrass model $W$ has rational double point (ADE / du Val) singularities at points where $\Delta$ vanishes to high order. A canonical resolution of singularities $S \to W$ recovers the minimal regular elliptic surface by blowing up along non-transverse components.

  * **Néron models and Kodaira singular fiber classification:**
    * The **Néron model** $\mathcal{E} \to C$ of $E_\eta$ is a smooth, separated group scheme representing the functor of sections: $\mathcal{E}(U) \cong E_\eta(K(U))$ for smooth $U \to C$.
    * At each critical point $v \in C$ where $\Delta(v) = 0$, the special fiber $\mathcal{E}_v$ decomposes as:
      $$
      0 \longrightarrow \mathcal{E}_v^0 \longrightarrow \mathcal{E}_v \longrightarrow \Phi_v \longrightarrow 0,
      $$
      where $\mathcal{E}_v^0$ is connected and $\Phi_v \coloneqq \mathcal{E}_v / \mathcal{E}_v^0$ is the finite component group.
    * **Kodaira fiber classification:**
      - $I_0$: smooth elliptic curve ($\mathcal{E}_v^0 \cong E_v$, $\Phi_v = 0$).
      - $I_n$ ($n \ge 1$): cycle of $n$ smooth rational curves, multiplicative reduction ($\mathcal{E}_v^0 \cong \mathbb{G}_m$), component group $\Phi_v \cong \mathbb{Z}/n\mathbb{Z}$.
      - $I_n^*$ ($n \ge 0$): affine $\widetilde{D}_{n+4}$ dual graph, additive reduction ($\mathcal{E}_v^0 \cong \mathbb{G}_a$), component group $\Phi_v \cong (\mathbb{Z}/2\mathbb{Z})^2$ ($n$ even) or $\mathbb{Z}/4\mathbb{Z}$ ($n$ odd).
      - $II$: cuspidal rational curve ($\widetilde{A}_0^*$), additive $\mathbb{G}_a$, $\Phi_v = 0$.
      - $III$: two tangent rational curves ($\widetilde{A}_1$), additive $\mathbb{G}_a$, $\Phi_v \cong \mathbb{Z}/2\mathbb{Z}$.
      - $IV$: three concurrent rational curves ($\widetilde{A}_2$), additive $\mathbb{G}_a$, $\Phi_v \cong \mathbb{Z}/3\mathbb{Z}$.
      - $IV^*$: affine $\widetilde{E}_6$ dual graph, additive $\mathbb{G}_a$, $\Phi_v \cong \mathbb{Z}/3\mathbb{Z}$.
      - $III^*$: affine $\widetilde{E}_7$ dual graph, additive $\mathbb{G}_a$, $\Phi_v \cong \mathbb{Z}/2\mathbb{Z}$.
      - $II^*$: affine $\widetilde{E}_8$ dual graph, additive $\mathbb{G}_a$, $\Phi_v = 0$.
    * **Tate's algorithm:**
      Determines the Kodaira fiber type, component group $\Phi_v$, and minimal Weierstrass model from local valuations $\operatorname{ord}_v(a_i)$ and $\operatorname{ord}_v(\Delta)$.

  * **Mordell-Weil groups and the Mordell-Weil lattice (Shioda-Tate):**
    * The **Mordell-Weil group** is the group of sections $\operatorname{MW}(S/C) \cong E_\eta(K)$, finitely generated by the Mordell-Weil theorem:
      $$
      \operatorname{MW}(S/C) \;\cong\; \mathbb{Z}^r \oplus E_\eta(K)_{\mathrm{tors}}.
      $$
    * **Trivial lattice $T(S) \subset \operatorname{NS}(S)$:**
      Sublattice spanned by the zero section $O$, a generic fiber $F$, and all non-identity fiber components $\Theta_{v, i}$ ($v \in \operatorname{Sing}$, $i = 1, \dots, m_v - 1$):
      $$
      T(S) \;\cong\; U \oplus \bigoplus_{v \in \operatorname{Sing}} T_v,
      $$
      where $U = \mathbb{Z}O \oplus \mathbb{Z}F$ has Gram matrix $\begin{pmatrix} -\chi & 1 \\ 1 & 0 \end{pmatrix}$, and $T_v$ is the negative-definite root lattice of type $A_{n-1}, D_{n+4}, E_6, E_7, E_8$.
    * **Shioda-Tate formula:**
      $$
      \operatorname{NS}(S) \otimes \mathbb{Q} \;\cong\; T(S) \otimes \mathbb{Q} \oplus \left( \operatorname{MW}(S/C) \otimes \mathbb{Q} \right),
      $$
      yielding the Picard number $\rho(S) = 2 + \sum_{v \in \operatorname{Sing}} (m_v - 1) + \operatorname{rank}(\operatorname{MW}(S/C))$.
    * **Shioda height pairing (Mordell-Weil lattice):**
      For sections $P, Q \in \operatorname{MW}(S/C)$, orthogonal projection $P \mapsto P^\sharp \in T(S)_\mathbb{Q}^\perp$ equips $\operatorname{MW}(S/C) / \operatorname{MW}(S/C)_{\mathrm{tors}}$ with a positive-definite symmetric bilinear form:
      $$
      \langle P, Q \rangle \;\coloneqq\; - (P^\sharp \cdot Q^\sharp) \;=\; \chi(\mathcal{O}_S) + (P \cdot O) + (Q \cdot O) - (P \cdot Q) - \sum_{v \in \operatorname{Sing}} \operatorname{contr}_v(P, Q),
      $$
      where $\operatorname{contr}_v(P, Q) \in \mathbb{Q}_{\ge 0}$ is the local correction term computed from the inverse Cartan matrix of the root lattice $T_v$.
    * **Narrow Mordell-Weil lattice $\operatorname{MW}(S/C)^0$:**
      Sublattice of sections intersecting the identity component $\Theta_{v, 0}$ of every singular fiber. In this case, $\operatorname{contr}_v(P, Q) = 0$, so $\langle P, P \rangle = 2\chi + 2(P \cdot O)$ is an even positive integer.
    * **Discriminant formula:**
      $$
      |\det \operatorname{NS}(S)| \;=\; \frac{|\det \operatorname{MW}(S/C)| \cdot \prod_{v \in \operatorname{Sing}} |\Phi_v|}{|E_\eta(K)_{\mathrm{tors}}|^2}.
      $$

* **Preamble implementation requirements:**
  * **Elliptic surface category and fibrations:** `categories/schemes/elliptic_surfaces/elliptic_surface.py`
    - `EllipticSurface(base_curve, total_space, projection)`: invariants $\chi(\mathcal{O}_S)$, $c_1^2$, $c_2$, canonical class $K_S$, fundamental line bundle $\mathbb{L}$.
    - `JacobianEllipticSurface(fibration, zero_section)`: structure with designated identity section $O$.
  * **Weierstrass models:** `categories/schemes/elliptic_surfaces/weierstrass_models.py`
    - `WeierstrassModel(C, g2, g3)` / `GeneralWeierstrassModel(C, a1, a2, a3, a4, a6)`.
    - Methods: `discriminant()`, `j_invariant()`, `is_minimal()`, `minimal_weierstrass_model()`, and Miranda blow-up resolution to smooth surface.
  * **Kodaira classification and Tate's algorithm:** `categories/schemes/elliptic_surfaces/kodaira.py`
    - `KodairaFiberType` enum: $I_0, I_n, I_n^*, II, III, IV, IV^*, III^*, II^*$.
    - `tate_algorithm(W, v)`: computes fiber type, component group $\Phi_v$, and minimal model at point $v \in C$.
  * **Néron models:** `categories/schemes/elliptic_surfaces/neron_model.py`
    - `NeronModel(elliptic_surface)`: special fibers $\mathcal{E}_v$, identity component $\mathcal{E}_v^0$, component groups $\Phi_v$.
  * **Mordell-Weil groups and lattices:** `categories/schemes/elliptic_surfaces/mordell_weil.py`
    - `MordellWeilGroup(elliptic_surface)`: group of sections, torsion subgroup, rank.
    - `trivial_lattice(elliptic_surface)`: root lattice $T(S)$.
    - `mordell_weil_lattice(elliptic_surface)`: positive-definite lattice on $\operatorname{MW}(S/C)$ with height pairing $\langle P, Q \rangle$ and local correction terms $\operatorname{contr}_v(P, Q)$.
    - `narrow_mordell_weil_lattice(elliptic_surface)`.

Intended owners: `categories/schemes/elliptic_surfaces/elliptic_surface.py` (`EllipticSurface`, `JacobianEllipticSurface`), `categories/schemes/elliptic_surfaces/weierstrass_models.py` (`WeierstrassModel`, `MirandaResolution`), `categories/schemes/elliptic_surfaces/kodaira.py` (`KodairaFiberType`, `TateAlgorithm`), `categories/schemes/elliptic_surfaces/neron_model.py` (`NeronModel`, `ComponentGroup`), `categories/schemes/elliptic_surfaces/mordell_weil.py` (`MordellWeilGroup`, `MordellWeilLattice`, `HeightPairing`).


## Desired capability: Euler operator $\theta = t \partial_t$ and standard formal operators on $R[[t]]$ — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **Formal power series ring $R[[t]]$ and operator algebras:**
    * Let $R$ be a commutative ring (or $\mathbb{Q}$-algebra when dividing by integers is required, such as for integration, exponential, logarithm, or Lagrange inversion).
    * $R[[t]]$ is the ring of formal power series $f(t) = \sum_{n=0}^\infty a_n t^n$ equipped with the $(t)$-adic topology, with filtration ideals $F^k = t^k R[[t]]$.
    * Continuous $R$-linear endomorphisms $\operatorname{End}_R^{\mathrm{cont}}(R[[t]])$ and derivations $\operatorname{Der}_R(R[[t]])$.
    * Ring of formal differential operators $\mathcal{D}(R[[t]]) \coloneqq R[[t]]\langle \partial_t \rangle \cong R[[t]]\langle \theta \rangle$, where $\partial_t = \frac{d}{dt}$ and $\theta = t \partial_t$.

  * **The Euler operator $\theta \coloneqq t \frac{d}{dt} = t \partial_t$ (degree / scaling operator):**
    * Action on monomials: $\theta(t^n) = n t^n$. Thus $\theta$ diagonalizes the grading on $R[[t]]$, acting as the infinitesimal generator of dilatations $t \mapsto e^{\epsilon} t$.
    * Action on series:
      $$
      \theta\left(\sum_{n=0}^\infty a_n t^n\right) \;=\; \sum_{n=0}^\infty n a_n t^n.
      $$
    * Powers and polynomial operators: For any polynomial $P(x) \in R[x]$:
      $$
      P(\theta)\left(\sum_{n=0}^\infty a_n t^n\right) \;=\; \sum_{n=0}^\infty P(n) a_n t^n.
      $$
    * Stirling number conversions:
      $$
      \theta^k \;=\; \sum_{j=1}^k \left\{ \begin{matrix} k \\ j \end{matrix} \right\} t^j \partial_t^j, \qquad t^k \partial_t^k \;=\; \theta(\theta - 1)\cdots(\theta - k + 1) \;=\; (\theta)_k,
      $$
      where $\left\{ \begin{matrix} k \\ j \end{matrix} \right\}$ are Stirling numbers of the second kind and $(\theta)_k$ is the falling factorial.
    * Commutation relations:
      $$
      [\theta, t] \;=\; t, \qquad [\theta, \partial_t] \;=\; -\partial_t, \qquad [\partial_t, t] \;=\; 1,
      $$
      and more generally $[\theta, t^k] = k t^k$, $[\theta, \partial_t^k] = -k \partial_t^k$.
    * Euler form of differential equations (Picard-Fuchs and D-finite systems):
      A linear differential operator with a regular singularity at $t = 0$ is canonically written in Euler form:
      $$
      \mathcal{L} \;=\; P_0(\theta) + t P_1(\theta) + \dots + t^m P_m(\theta),
      $$
      where $P_0(s) = 0$ is the indicial equation governing local exponents at $t=0$.

  * **Derivation, formal integration, and shifts:**
    * **Formal derivative:** $\partial_t \colon R[[t]] \to R[[t]]$, $\partial_t\left(\sum_{n=0}^\infty a_n t^n\right) = \sum_{n=0}^\infty (n+1) a_{n+1} t^n$.
    * **Formal integration (anti-derivation):** For $R$ a $\mathbb{Q}$-algebra, $\int \colon R[[t]] \to t R[[t]]$, defined by:
      $$
      \int \left(\sum_{n=0}^\infty a_n t^n\right) dt \;\coloneqq\; \sum_{n=0}^\infty \frac{a_n}{n+1} t^{n+1}.
      $$
      Satisfies the fundamental theorem of calculus: $\partial_t \left(\int f dt\right) = f(t)$, and $\int (\partial_t f) dt = f(t) - f(0)$.
    * **Backward shift (difference quotient / division by $t$):**
      $$
      S^-(f)(t) \;\coloneqq\; \frac{f(t) - f(0)}{t} \;=\; \sum_{n=0}^\infty a_{n+1} t^n.
      $$
      Higher-order backward shifts: $S^{-m}(f)(t) \coloneqq \frac{f(t) - \sum_{k=0}^{m-1} a_k t^k}{t^m} = \sum_{n=0}^\infty a_{n+m} t^n$.
    * **Forward shift (multiplication by $t^m$):** $S^{+m}(f)(t) \coloneqq t^m f(t)$.
    * **Coefficient extraction functional:** $[t^n] \colon R[[t]] \to R$, sending $f \mapsto a_n$.

  * **Multiplication, convolutions, and dilations:**
    * **Cauchy product (ring multiplication):** Operator $M_g \colon f \mapsto g \cdot f$, with $[t^n](g \cdot f) = \sum_{k=0}^n a_k b_{n-k}$.
    * **Hadamard product (coefficient-wise / Schur multiplication):**
      $$
      (f \odot g)(t) \;\coloneqq\; \sum_{n=0}^\infty a_n b_n t^n.
      $$
      Endows $R[[t]]$ with a second commutative ring structure with unit $\frac{1}{1-t} = \sum_{n=0}^\infty t^n$.
      Euler operator via Hadamard product: $\theta f = f \odot \frac{t}{(1-t)^2}$.
    * **Hurwitz product (binomial convolution for EGFs):**
      $$
      (f \ast_H g)(t) \;\coloneqq\; \sum_{n=0}^\infty \left(\sum_{k=0}^n \binom{n}{k} a_k b_{n-k}\right) \frac{t^n}{n!}.
      $$
    * **Dilation / Scaling operator (Adams operator):**
      $\sigma_c(f)(t) \coloneqq f(ct) = \sum_{n=0}^\infty a_n c^n t^n$, with infinitesimal generator $\theta = \left. \frac{d}{dc} \sigma_c \right|_{c=1}$.

  * **Composition and formal inversion (Lagrange inversion):**
    * **Composition operator:** For $g(t) \in R[[t]]$ with $\operatorname{ord}(g) \ge 1$ (or $g(0)$ nilpotent):
      $$
      C_g(f)(t) \;\coloneqq\; (f \circ g)(t) \;=\; f(g(t)) \;=\; \sum_{n=0}^\infty a_n (g(t))^n.
      $$
      Continuous $R$-algebra homomorphism. Chain rules: $\partial_t(f \circ g) = (\partial_t f \circ g) \cdot \partial_t g$, and $\theta(f \circ g) = (\theta f \circ g) \cdot \frac{\theta g}{g}$.
    * **Formal inversion (Lagrange Inversion Formula / LIF):**
      For a reversible series $g(t) = c_1 t + c_2 t^2 + \dots \in R[[t]]$ with $c_1 \in R^\times$, there exists a unique compositional inverse $\check{g}(t) = g^{\langle -1 \rangle}(t) \in t R[[t]]$ satisfying $g(\check{g}(t)) = \check{g}(g(t)) = t$.
      - **Lagrange Inversion Formula:**
        $$
        [t^n] \check{g}(t) \;=\; \frac{1}{n} [t^{n-1}] \left( \frac{t}{g(t)} \right)^n.
        $$
      - **Lagrange-Bürmann formula:** For any series $H(t) \in R[[t]]$:
        $$
        [t^n] H(\check{g}(t)) \;=\; \frac{1}{n} [t^{n-1}] \left( H'(t) \left( \frac{t}{g(t)} \right)^n \right).
        $$

  * **Logarithmic derivatives and formal logarithm:**
    * **Standard logarithmic derivative:**
      $$
      \operatorname{dlog}(f) \;\coloneqq\; \frac{\partial_t f}{f} \;=\; \frac{f'(t)}{f(t)} \in R[[t]] \quad (\text{for } f(0) \in R^\times).
      $$
    * **Euler logarithmic derivative:**
      $$
      \operatorname{dlog}_\theta(f) \;\coloneqq\; \frac{\theta f}{f} \;=\; t \frac{f'(t)}{f(t)} \in t R[[t]].
      $$
    * Group homomorphism: $\operatorname{dlog}(f \cdot g) = \operatorname{dlog}(f) + \operatorname{dlog}(g)$, $\operatorname{dlog}(f^k) = k \operatorname{dlog}(f)$, $\operatorname{dlog}(1/f) = -\operatorname{dlog}(f)$.
    * **Relation to Newton sums and power sums:**
      If $f(t) = \prod_{i=1}^d (1 - \alpha_i t)$ is the reverse characteristic polynomial, then:
      $$
      - \operatorname{dlog}_\theta(f) \;=\; - t \frac{f'(t)}{f(t)} \;=\; \sum_{k=1}^\infty p_k t^k, \quad \text{where } p_k = \sum_{i=1}^d \alpha_i^k.
      $$
    * **Formal logarithm:** For $f(t) \in 1 + t R[[t]]$ ($R$ a $\mathbb{Q}$-algebra):
      $$
      \log(f(t)) \;\coloneqq\; \int \frac{f'(t)}{f(t)} dt \;=\; \sum_{k=1}^\infty \frac{(-1)^{k-1}}{k} (f(t) - 1)^k.
      $$

  * **Formal exponential of an integral ($e^{\int f}$):**
    * For $f(t) \in R[[t]]$ ($R$ a $\mathbb{Q}$-algebra), let $F(t) = \int f(t) dt \in t R[[t]]$.
    * Then:
      $$
      y(t) \;\coloneqq\; \exp\left(\int f(t) dt\right) \;=\; \sum_{k=0}^\infty \frac{1}{k!} \left( \int f(t) dt \right)^k \in 1 + t R[[t]].
      $$
    * **First-order ODE and integrating factor:**
      $y(t)$ is the unique solution to the homogeneous initial value problem:
      $$
      \partial_t y \;=\; f(t) y, \quad y(0) = 1, \qquad \text{or equivalently} \quad \theta y \;=\; (t f(t)) y.
      $$
      For an inhomogeneous equation $y' + a(t) y = b(t)$, the integrating factor $\mu(t) = \exp(\int a(t) dt)$ yields:
      $$
      y(t) \;=\; \mu(t)^{-1} \left( y(0) + \int_0^t b(s) \mu(s) ds \right).
      $$
    * **Combinatorial exponential formula:**
      Let $A(t) = \sum_{n=1}^\infty a_n \frac{t^n}{n!}$ be the EGF of connected combinatorial structures. Then:
      $$
      \exp(A(t)) \;=\; \sum_{n=0}^\infty c_n \frac{t^n}{n!}
      $$
      is the EGF of all structures (sets of connected components).
    * **Plethystic exponential $\operatorname{PE}[f]$:**
      For $f(t) \in t R[[t]]$:
      $$
      \operatorname{PE}[f(t)] \;\coloneqq\; \exp\left( \sum_{k=1}^\infty \frac{f(t^k)}{k} \right) \;=\; \prod_{n=1}^\infty \frac{1}{(1 - t^n)^{a_n}} \quad (\text{when } f(t) = \sum a_n t^n).
      $$

  * **Lie algebra of vector fields / Witt algebra generators on $R[[t]]$:**
    * Derivations $\operatorname{Der}_R(R[[t]]) \cong R[[t]] \partial_t$.
    * Witt algebra basis: $L_n \coloneqq -t^{n+1} \partial_t = -t^n \theta$ for $n \in \mathbb{Z}_{\ge -1}$.
    * Commutation relations:
      $$
      [L_m, L_n] \;=\; (m - n) L_{m+n}.
      $$
      Here $L_{-1} = -\partial_t$ (translation), $L_0 = -\theta$ (dilation/Euler), $L_1 = -t\theta$ (special conformal).

* **Preamble implementation requirements:**
  * **Formal power series operator methods:** `categories/rings/formal_power_series.py`
    - `FormalPowerSeries.derivative()`: formal differentiation $\partial_t f$.
    - `FormalPowerSeries.euler_derivative()` (or `f.theta()`): Euler derivative $\theta f = t \partial_t f$.
    - `FormalPowerSeries.integral()`: formal integration $\int f dt$ (asserting $\mathbb{Q} \subseteq R$).
    - `FormalPowerSeries.shift(k)`: backward shift $S^{-k} f = (f - \sum_{j<k} a_j t^j)/t^k$ or forward shift $t^k f$.
    - `FormalPowerSeries.hadamard(g)`: coefficient-wise product $(f \odot g)(t)$.
    - `FormalPowerSeries.hurwitz_product(g)`: binomial convolution for exponential generating functions.
    - `FormalPowerSeries.compose(g)`: composition $f(g(t))$ for $\operatorname{ord}(g) \ge 1$.
    - `FormalPowerSeries.revert()`: functional/compositional inverse $f^{\langle -1 \rangle}(t)$ via Lagrange inversion.
    - `FormalPowerSeries.dlog()`: standard logarithmic derivative $f'/f$.
    - `FormalPowerSeries.dlog_theta()`: Euler logarithmic derivative $\theta f / f = t f'/f$.
    - `FormalPowerSeries.exp_integral()`: formal exponential of integral $\exp(\int f dt)$.
    - `FormalPowerSeries.log()`: formal logarithm $\log f(t)$.
  * **Differential operator calculus on formal series:** `categories/differential_operators/formal_series.py`
    - `EulerOperator(ring, var='t')`: standalone operator $\theta = t \partial_t$.
    - `FormalDifferentialOperator`: polynomial expression in $\theta$ or $(t, \partial_t)$; supports evaluation on series, composition, and conversion between $\theta$-basis and $\partial_t$-basis via Stirling numbers of the second kind.
    - `IntegratingFactor(a, b)`: solves $y' + a(t) y = b(t)$ via formal exponential of integral.
  * **Combinatorial and generating function operators:** `categories/generating_functions/operators.py`
    - `LagrangeInversion(g, H=None, n=10)`: coefficient extractor using Lagrange-Bürmann formula.
    - `PlethysticExponential(f, prec=20)`: evaluates $\operatorname{PE}[f(t)]$.
    - `ExponentialFormula(connected_egf)`: maps connected EGF $A(t)$ to total EGF $\exp(A(t))$.

Intended owners: `categories/rings/formal_power_series.py` (`FormalPowerSeries` operator suite), `categories/differential_operators/formal_series.py` (`EulerOperator`, `FormalDifferentialOperator`, `IntegratingFactor`), `categories/generating_functions/operators.py` (`LagrangeInversion`, `PlethysticExponential`, `ExponentialFormula`), `categories/algebras/weyl_algebra.py` (`WeylAlgebra`, `WittAlgebra`).


## Desired capability: Catalogue of known mirror family pairs from the literature — intake 2026-09-19

* **Mathematical background & classification frameworks of mirror pairs:**
  * **(1) Greene-Plesser Orbifold Mirror Families:**
    * Construction: Hypersurfaces in projective or weighted projective space $\mathbb{P}(w_0, \dots, w_{n+1})$ cut out by Fermat-type polynomials with complex structure deformation parameter $\psi$, quotiented by a maximal group of phase symmetries $G \subset \operatorname{SL}(n+2, \mathbb{C})$.
    * **The quintic threefold mirror pair:**
      - Large family: $X_\psi \subset \mathbb{P}^4$ defined by $\sum_{i=0}^4 x_i^5 - 5\psi x_0 x_1 x_2 x_3 x_4 = 0$.
      - Discrete symmetry group: $G = \{ (a_0, \dots, a_4) \in (\mathbb{Z}/5\mathbb{Z})^5 \mid \sum a_i \equiv 0 \pmod 5\} / \text{diag} \cong (\mathbb{Z}/5\mathbb{Z})^3$.
      - Mirror Calabi-Yau threefold: $Y_\psi \coloneqq \widetilde{X_\psi / G}$ (crepant resolution of singularities).
      - Hodge number exchange: $(h^{1,1}(X), h^{2,1}(X)) = (1, 101) \longleftrightarrow (h^{1,1}(Y), h^{2,1}(Y)) = (101, 1)$.
      - Euler characteristics: $\chi(X) = 2(1 - 101) = -200 \longleftrightarrow \chi(Y) = 2(101 - 1) = +200$.
    * **The 27 Greene-Plesser mirror pairs in weighted projective spaces:**
      - Hypersurfaces in $\mathbb{P}(w_0, \dots, w_4)$ with $\sum w_i = d$:
        * Sextic $X_6 \subset \mathbb{P}(1,1,1,1,2)$, $\chi = -252 \longleftrightarrow Y_6$, $\chi = +252$.
        * Octic $X_8 \subset \mathbb{P}(1,1,1,1,4)$, $\chi = -296 \longleftrightarrow Y_8$, $\chi = +296$.
        * Decic $X_{10} \subset \mathbb{P}(1,1,1,2,5)$, $\chi = -288 \longleftrightarrow Y_{10}$, $\chi = +288$.
        * Duodecic $X_{12} \subset \mathbb{P}(1,1,1,3,6)$, $\chi = -252 \longleftrightarrow Y_{12}$, $\chi = +252$.
      - Complete intersections:
        * Two cubics $X_{3,3} \subset \mathbb{P}^5$, $\chi = -144 \longleftrightarrow Y_{3,3}$, $\chi = +144$.
        * Quadric and quartic $X_{2,4} \subset \mathbb{P}^5$, $\chi = -168 \longleftrightarrow Y_{2,4}$, $\chi = +168$.
        * Two quadrics and a cubic $X_{2,2,3} \subset \mathbb{P}^6$, $\chi = -144 \longleftrightarrow Y_{2,2,3}$, $\chi = +144$.
        * Four quadrics $X_{2,2,2,2} \subset \mathbb{P}^7$, $\chi = -128 \longleftrightarrow Y_{2,2,2,2}$, $\chi = +128$.
      - Homological mirror symmetry proven by Sheridan and Smith (2021).

  * **(2) Batyrev-Borisov Toric Mirror Symmetry (Reflexive Polytopes & Nef-Partitions):**
    * **Polar duality of reflexive polytopes (Batyrev 1994):**
      - Let $M \cong \mathbb{Z}^n$ be a lattice, $N = \operatorname{Hom}(M, \mathbb{Z})$ its dual.
      - A convex lattice polytope $\Delta \subset M_\mathbb{R}$ containing the origin in its interior is *reflexive* if all vertices are primitive and its polar dual:
        $$
        \Delta^\circ \;\coloneqq\; \{ y \in N_\mathbb{R} \mid \langle x, y \rangle \ge -1 \; \forall x \in \Delta \}
        $$
        is also a lattice polytope in $N$.
      - Anticanonical Calabi-Yau hypersurfaces $X_\Delta \subset \mathbb{P}_{\Sigma(\Delta)}$ and $Y_{\Delta^\circ} \subset \mathbb{P}_{\Sigma(\Delta^\circ)}$.
      - Combinatorial Hodge numbers:
        $$
        h^{1,1}(X_\Delta) \;=\; l(\Delta^\circ) - (n+1) - \sum_{\operatorname{codim} \theta^\circ = 1} l^*(\theta^\circ) + \sum_{\operatorname{codim} \theta^\circ = 2} l^*(\theta^\circ) l^*(\theta) \;=\; h^{n-2, 1}(Y_{\Delta^\circ}).
        $$
    * **Kreuzer-Skarke classification of reflexive polytopes:**
      - Dimension 2 (elliptic curves): exactly 16 reflexive polygons (self-dual and dual pairs).
      - Dimension 3 (K3 surfaces): exactly 4,319 reflexive 3-polytopes.
      - Dimension 4 (Calabi-Yau 3-folds): exactly 473,800,776 reflexive 4-polytopes, generating 30,108 distinct Hodge pairs $(h^{1,1}, h^{2,1})$.
    * **Nef-partitions for complete intersections (Borisov 1993):**
      - Partitions of the vertices of $\Delta = \Delta_1 + \dots + \Delta_r$ and $\nabla = \nabla_1 + \dots + \nabla_r$ in $M$ and $N$.
      - Generates mirror pairs of Calabi-Yau complete intersections in Gorenstein toric Fano varieties.

  * **(3) Dolgachev-Nikulin Lattice-Polarized Mirror Symmetry for K3 Surfaces:**
    * K3 cohomology lattice: $\Lambda_{K3} \cong U^{\oplus 3} \oplus E_8(-1)^{\oplus 2}$, even unimodular of signature $(3, 19)$.
    * Let $M \hookrightarrow \Lambda_{K3}$ be an even non-degenerate primitive sublattice of signature $(1, \rho - 1)$ ($1 \le \rho \le 19$).
    * An $M$-polarized K3 surface has a primitive embedding $M \hookrightarrow \operatorname{Pic}(X)$.
    * The transcendental lattice is $T_X = M^\perp \subset \Lambda_{K3}$, signature $(2, 20 - \rho)$.
    * **Dolgachev's mirror lattice $\check{M}$:**
      When $M^\perp$ contains a hyperbolic plane $U$, the mirror polarization lattice is defined by:
      $$
      \check{M} \;\coloneqq\; U \oplus (M^\perp \cap U^\perp) \;\subset\; \Lambda_{K3}.
      $$
      Satisfies $\operatorname{rank}(\check{M}) = 22 - \rho$, exchanging the Picard rank and transcendental rank:
      $$
      \dim \mathcal{M}_M \;=\; 20 - \rho, \qquad \dim \mathcal{M}_{\check{M}} \;=\; \rho - 2, \qquad \dim \mathcal{M}_M + \dim \mathcal{M}_{\check{M}} \;=\; 18.
      $$
    * **Canonical K3 mirror pairs:**
      - Quartic in $\mathbb{P}^3$ ($M = \langle 4 \rangle$, $\rho = 1$, $\dim = 19$) $\longleftrightarrow$ Dwork pencil mirror ($M^\vee = U \oplus E_8^{\oplus 2} \oplus \langle -4 \rangle$, $\rho = 19$, $\dim = 1$).
      - Degree 2 K3 (double cover of $\mathbb{P}^2$ branched along sextic, $M = \langle 2 \rangle$) $\longleftrightarrow$ Mirror with $\rho = 19$, $M^\vee = U \oplus E_8^{\oplus 2} \oplus \langle -2 \rangle$.
      - Degree 6 K3 (complete intersection of quadric and cubic in $\mathbb{P}^4$, $M = \langle 6 \rangle$) $\longleftrightarrow$ rank 19 mirror.
      - Degree 8 K3 (complete intersection of three quadrics in $\mathbb{P}^5$, $M = \langle 8 \rangle$) $\longleftrightarrow$ rank 19 mirror.
      - Kummer surfaces $\operatorname{Km}(A)$ ($M = \operatorname{Kum} \cong \mathbb{Z}^{16}$) $\longleftrightarrow$ Kummer surfaces of the dual abelian surface $\operatorname{Km}(\widehat{A})$.
      - Elliptic K3 surfaces with section: $M = U \oplus W$ (where $W$ is the root lattice of singular fibers) $\longleftrightarrow$ Shioda-Inose partners.

  * **(4) Berglund-Hübsch-Krawitz (BHK) Landau-Ginzburg Mirror Symmetry:**
    * Invertible potential: $W(x_1, \dots, x_n) = \sum_{i=1}^n \prod_{j=1}^n x_j^{A_{ij}}$ where $A = (A_{ij}) \in \operatorname{Mat}_n(\mathbb{Z}_{\ge 0})$ is invertible over $\mathbb{Q}$.
    * Transpose polynomial: $W^\mathrm{T}(y_1, \dots, y_n) \coloneqq \sum_{i=1}^n \prod_{j=1}^n y_j^{(A^\mathrm{T})_{ij}}$.
    * Symmetry groups: Maximal diagonal symmetry group $G_W^{\mathrm{max}} = \{ (\lambda_1, \dots, \lambda_n) \in (\mathbb{C}^\times)^n \mid W(\lambda \cdot x) = W(x) \}$.
    * Krawitz duality: For any subgroup $G \le G_W \cap \operatorname{SL}(n, \mathbb{C})$, the dual group $G^\mathrm{T} \le G_{W^\mathrm{T}} \cap \operatorname{SL}(n, \mathbb{C})$ is defined via the pairing on characters.
    * BHK mirror pair: $(W, G) \longleftrightarrow (W^\mathrm{T}, G^\mathrm{T})$.
    * Kreuzer-Skarke classification of invertible potentials: Every invertible potential is a decoupled sum of atomic potentials of three elementary types:
      1. Fermat: $x^a$.
      2. Loop: $x_1^{a_1} x_2 + x_2^{a_2} x_3 + \dots + x_n^{a_n} x_1$.
      3. Chain: $x_1^{a_1} x_2 + x_2^{a_2} x_3 + \dots + x_{n-1}^{a_{n-1}} x_n + x_n^{a_n}$.
    * Proved by Artebani-Boissière-Sarti and Kelly to coincide with Dolgachev-Nikulin lattice-polarized mirror symmetry for K3 surfaces admitting non-symplectic automorphisms.

  * **(5) The 14 One-Parameter Hypergeometric Calabi-Yau 3-Fold Families (Doran-Morgan / AESZ / Morrison):**
    * Classification of all fourth-order Calabi-Yau Picard-Fuchs operators of hypergeometric type over $\mathbb{P}^1 \setminus \{0, 1, \infty\}$ with MUM at $z=0$:
      $$
      \theta^4 - C z (\theta + \alpha_1)(\theta + \alpha_2)(\theta + \alpha_3)(\theta + \alpha_4) = 0, \quad \text{with } \alpha_4 = 1 - \alpha_1, \; \alpha_3 = 1 - \alpha_2.
      $$
    * Table of the 14 families with geometric realizations:
      1. $\boldsymbol{\alpha} = (1/5, 2/5, 3/5, 4/5)$, $C = 5^5 = 3125$: Quintic threefold $X_5 \subset \mathbb{P}^4$, $\chi = -200$.
      2. $\boldsymbol{\alpha} = (1/6, 1/3, 2/3, 5/6)$, $C = 2^4 3^3 = 432$: Complete intersection $X_{3,3} \subset \mathbb{P}^5$, $\chi = -144$.
      3. $\boldsymbol{\alpha} = (1/4, 1/2, 1/2, 3/4)$, $C = 2^8 = 256$: Complete intersection $X_{2,4} \subset \mathbb{P}^5$, $\chi = -168$.
      4. $\boldsymbol{\alpha} = (1/3, 1/2, 1/2, 2/3)$, $C = 108$: Complete intersection $X_{2,2,3} \subset \mathbb{P}^6$, $\chi = -144$.
      5. $\boldsymbol{\alpha} = (1/2, 1/2, 1/2, 1/2)$, $C = 2^8 = 256$: Complete intersection $X_{2,2,2,2} \subset \mathbb{P}^7$, $\chi = -128$.
      6. $\boldsymbol{\alpha} = (1/8, 3/8, 5/8, 7/8)$, $C = 2^{14} = 16384$: Hypersurface $X_8 \subset \mathbb{P}(1,1,1,1,4)$, $\chi = -296$.
      7. $\boldsymbol{\alpha} = (1/10, 3/10, 7/10, 9/10)$, $C = 2^4 5^5 = 50000$: Hypersurface $X_{10} \subset \mathbb{P}(1,1,1,2,5)$, $\chi = -288$.
      8. $\boldsymbol{\alpha} = (1/12, 5/12, 7/12, 11/12)$, $C = 2^{10} 3^3 = 27648$: Hypersurface $X_6 \subset \mathbb{P}(1,1,1,1,2)$ / $X_{12} \subset \mathbb{P}(1,1,1,3,6)$, $\chi = -252$.
      9. $\boldsymbol{\alpha} = (1/6, 1/2, 1/2, 5/6)$, $C = 2^6 3^3 = 1728$: Complete intersection $X_{4,4} \subset \mathbb{P}(1,1,1,1,2,2)$.
      10. $\boldsymbol{\alpha} = (1/6, 1/4, 3/4, 5/6)$, $C = 2^6 3^3 = 1728$: Complete intersection $X_{3,4} \subset \mathbb{P}(1,1,1,1,1,2)$.
      11. $\boldsymbol{\alpha} = (1/12, 5/12, 1/2, 1/2)$, $C = 2^8 3^3 = 6912$: Complete intersection $X_{2,6} \subset \mathbb{P}(1,1,1,1,1,3)$.
      12. $\boldsymbol{\alpha} = (1/8, 3/8, 1/2, 1/2)$, $C = 2^{10} = 1024$: Complete intersection $X_{2,4} \subset \mathbb{P}(1,1,1,1,2,2)$.
      13. $\boldsymbol{\alpha} = (1/10, 3/10, 1/2, 1/2)$, $C = 2^6 5^5 = 200000$: Complete intersection $X_{2,10} \subset \mathbb{P}(1,1,1,2,2,5)$.
      14. $\boldsymbol{\alpha} = (1/6, 1/3, 1/2, 2/3)$, $C = 432$: Pfaffian Calabi-Yau threefold in $\mathbb{P}^6$ / Grassmannian section.
    * **Monodromy arithmeticity dichotomy:**
      - 7 families have arithmetic monodromy in $\operatorname{Sp}(4, \mathbb{Z})$ (cases 1, 2, 3, 4, 5, 8, 9).
      - 7 families have thin monodromy (non-arithmetic Zariski-dense subgroups of infinite index, Brav-Thomas 2014, Singh-Venkataramana 2014).

  * **(6) Doran-Harder-Thompson Mirror Symmetry for Fibrations & Degenerations:**
    * K3 fibrations: Calabi-Yau 3-folds admitting a fibration $\pi \colon X \to \mathbb{P}^1$ by K3 surfaces.
    * Mirror family $\check{X} \to \mathbb{P}^1$ is fibered by dual lattice-polarized K3 surfaces.
    * **Kulikov Type II degeneration gluing:**
      At a degeneration point $0 \in \mathbb{P}^1$ where $X_0 = V \cup_D W$ is a Type II Kulikov degeneration (with $V, W$ quasi-Fano surfaces glued along a smooth anticanonical elliptic curve $D$), the mirror $\check{X}$ is constructed by gluing the Landau-Ginzburg mirror models of $(V, D)$ and $(W, D)$.
    * Connects fibration mirror symmetry directly to the Gross-Siebert program and the Strominger-Yau-Zaslow (SYZ) fibration.

  * **(7) Fano Varieties and Landau-Ginzburg Models (Coates-Corti-Galkin-Golyshev-Kasprzyk):**
    * For a smooth Fano variety $X$ of dimension $n$, its mirror is a Landau-Ginzburg model $(\check{X}, W)$, where $\check{X} \cong (\mathbb{C}^\times)^n$ is an algebraic torus and $W \colon (\mathbb{C}^\times)^n \to \mathbb{C}$ is a Laurent polynomial (superpotential).
    * **Quantum period matching:**
      $$
      I_0^X(t) \;=\; 1 + \sum_{d=1}^\infty J_d t^d \;=\; \frac{1}{(2\pi i)^n} \oint \frac{1}{1 - t W(x)} \frac{dx_1}{x_1} \cdots \frac{dx_n}{x_n} \;=\; \sum_{k=0}^\infty [x^0](W(x)^k) t^k.
      $$
    * Canonical pairings:
      - Projective space $\mathbb{P}^n \longleftrightarrow W = x_1 + \dots + x_n + \frac{1}{x_1 \cdots x_n}$.
      - Quadric hypersurface $Q^n \subset \mathbb{P}^{n+1} \longleftrightarrow W = x_1 + \dots + x_n + \frac{1}{x_1 \cdots x_{n-1}} + \frac{1}{x_n}$.
      - del Pezzo surfaces $dP_k = \mathrm{Bl}_k \mathbb{P}^2$ ($0 \le k \le 8$) $\longleftrightarrow$ Givental Laurent polynomials; under Doran-Malmendier twist, their periods yield Picard-Fuchs operators of 17 rank-1 Fano K3 mirror families.
      - 105 smooth Fano 3-folds $\longleftrightarrow$ 105 Laurent polynomials in 3 variables classified in the Fano / GRDB project.

  * **(8) Abelian Varieties and Dual Tori (SYZ Mirror Symmetry):**
    * Dimension 1 (elliptic curves): Complex elliptic curve $E_\tau = \mathbb{C}/(\mathbb{Z} \oplus \tau \mathbb{Z})$ with complex structure $\tau \in \mathbb{H}$ and complexified symplectic area $\rho = b + i A$ is mirror to $E_{\check{\tau}}$ with $\check{\tau} = \rho$ and $\check{\rho} = \tau$.
    * Higher dimension: Principally polarized abelian variety $A = V/\Lambda \longleftrightarrow$ dual abelian variety $\check{A} = \operatorname{Pic}^0(A) = V^\vee / \Lambda^\vee$.
    * SYZ T-duality: Special Lagrangian torus fibration $\pi \colon X \to B$ with fiber $T^n \cong (S^1)^n$; the mirror $\check{X} \to B$ has fibers given by the dual tori $\check{T}^n = H^1(T^n, \mathbb{R}/\mathbb{Z})$.

* **Preamble implementation requirements:**
  * **Mirror catalogue registry:** `categories/schemes/mirror_symmetry/mirror_catalogue.py`
    - `MirrorPair(source_family, target_family, duality_type, invariants)`: unified interface for mirror pairs.
    - `DualityType` enum: `GREENE_PLESSER`, `BATYREV_BORISOV`, `DOLGACHEV_NIKULIN`, `BHK`, `DORAN_MORGAN_14`, `DORAN_HARDER_THOMPSON`, `FANO_LG`, `SYZ_ABELIAN`.
    - Methods: `picard_fuchs_operator()`, `mirror_map()`, `yukawa_coupling()`, `instanton_numbers()`.
  * **Toric reflexive polytope mirror symmetry:** `categories/schemes/mirror_symmetry/batyrev_borisov.py`
    - `ReflexivePolytope(vertices)`: polar dual $\Delta^\circ$, Hodge numbers $h^{1,1}, h^{n-2,1}$, Kreuzer-Skarke database lookup.
    - `NefPartition(polytope, partition)`: computes dual partition and complete intersection mirror.
  * **Lattice-polarized K3 mirror symmetry:** `categories/schemes/mirror_symmetry/dolgachev_nikulin.py`
    - `LatticePolarizedK3(polarization_lattice)`: computes dual polarization lattice $\check{M} = U \oplus (M^\perp \cap U^\perp)$, Picard number $\check{\rho} = 22 - \rho$, transcendental lattice $T_X$.
  * **Berglund-Hübsch-Krawitz (BHK) duality:** `categories/schemes/mirror_symmetry/bhk.py`
    - `InvertiblePolynomial(matrix_or_terms)`: computes transpose polynomial $W^\mathrm{T}$, dual group $G^\mathrm{T}$, and atomic decomposition (Fermat, loop, chain).
  * **14 hypergeometric Calabi-Yau threefolds:** `categories/schemes/mirror_symmetry/hypergeometric_cy3.py`
    - `HypergeometricCY3(index)`: index 1..14, rational parameters $(\alpha_1, \alpha_2, \alpha_3, \alpha_4)$, constant $C$, Picard-Fuchs operator, Euler characteristic $\chi$, and arithmeticity predicate (`is_arithmetic`).
  * **Fano / Landau-Ginzburg models:** `categories/schemes/mirror_symmetry/fano_lg.py`
    - `FanoLGMirror(fano_variety)`: superpotential $W(x_1, \dots, x_n)$, constant term sequence $[x^0](W^k)$, Picard-Fuchs operator of $I_0(t)$.

Intended owners: `categories/schemes/mirror_symmetry/mirror_catalogue.py` (`MirrorPair`, `DualityType`), `categories/schemes/mirror_symmetry/batyrev_borisov.py` (`ReflexivePolytope`, `NefPartition`), `categories/schemes/mirror_symmetry/dolgachev_nikulin.py` (`LatticePolarizedK3`, `DualPolarizationLattice`), `categories/schemes/mirror_symmetry/bhk.py` (`InvertiblePolynomial`, `KrawitzDuality`), `categories/schemes/mirror_symmetry/hypergeometric_cy3.py` (`HypergeometricCY3`), `categories/schemes/mirror_symmetry/fano_lg.py` (`FanoLGMirror`, `Superpotential`).


## Desired capability: Operationalized convergence criteria, Dirichlet irrationality, symbolic integration by parts, and L-function zeta regularization — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **(1) Dirichlet's Irrationality Criterion and Diophantine Approximation:**
    * **Dirichlet's criterion:** A real number $\alpha \in \mathbb{R}$ is irrational if and only if for every $\epsilon > 0$, there exist integers $p, q \in \mathbb{Z}$ with $q > 0$ such that:
      $$
      0 \;<\; |q\alpha - p| \;<\; \epsilon.
      $$
    * **Dirichlet's approximation theorem (effective bound):** For any $\alpha \in \mathbb{R}$ and any integer $N \ge 1$, there exist $p, q \in \mathbb{Z}$ with $1 \le q \le N$ such that:
      $$
      \left| \alpha - \frac{p}{q} \right| \;<\; \frac{1}{q N} \;\le\; \frac{1}{q^2}.
      $$
    * **Operational certificate of irrationality:**
      A sequence of pairs $(p_n, q_n) \in \mathbb{Z} \times \mathbb{Z}_{>0}$ constitutes a formal certificate of irrationality for $\alpha$ if:
      $$
      q_n \alpha - p_n \;\neq\; 0 \quad \forall n, \qquad \text{and} \qquad \lim_{n \to \infty} |q_n \alpha - p_n| \;=\; 0.
      $$
      - Recovers Apéry's proofs: For $\zeta(3) = \sum \frac{1}{n^3}$ and $\zeta(2) = \frac{\pi^2}{6}$, sequences $a_n, b_n$ generated by second-order recurrences satisfy $2 \operatorname{lcm}(1, \dots, n)^3 |a_n \zeta(3) - b_n| \to 0$.
      - Legendre's theorem: Any fraction $p/q$ satisfying $|\alpha - p/q| < \frac{1}{2q^2}$ is necessarily a continued fraction convergent $p_n/q_n$.
    * **Irrationality measure / exponent $\mu(\alpha)$:**
      $$
      \mu(\alpha) \;\coloneqq\; \inf \left\{ \mu \in \mathbb{R} \;\middle|\; \left| \alpha - \frac{p}{q} \right| > \frac{1}{q^\mu} \text{ for all but finitely many } (p, q) \in \mathbb{Z} \times \mathbb{Z}_{>0} \right\}.
      $$
      - For rational numbers: $\mu(p/q) = 1$.
      - Roth's theorem: For any algebraic irrational number $\alpha$, $\mu(\alpha) = 2$.
      - Transcendental numbers: $\mu(e) = 2$, $\mu(\pi) \le 7.10320533$, $\mu(\zeta(3)) \le 5.513891$. Liouville numbers have $\mu = \infty$.

  * **(2) Dirichlet's Convergence Test and Summation by Parts:**
    * **Dirichlet's test:** Let $(a_n)_{n \ge 1}$ be a sequence of complex numbers with bounded partial sums:
      $$
      \left| \sum_{n=1}^N a_n \right| \;\le\; M \quad \forall N \ge 1,
      $$
      and let $(b_n)_{n \ge 1}$ be a sequence of real numbers that is monotonic and converges to $0$ ($\lim_{n \to \infty} b_n = 0$).
      Then the series $\sum_{n=1}^\infty a_n b_n$ converges, and its tail satisfies the effective bound:
      $$
      \left| \sum_{n=N+1}^\infty a_n b_n \right| \;\le\; 2 M b_{N+1}.
      $$
    * **Summation by parts (Abel transformation):**
      With $A_n \coloneqq \sum_{k=1}^n a_k$ and $A_0 = 0$:
      $$
      \sum_{n=1}^N a_n b_n \;=\; A_N b_{N+1} + \sum_{n=1}^N A_n (b_n - b_{n+1}).
      $$
    * **Operational specializations:**
      - Alternating series (Leibniz test): $a_n = (-1)^n$, $A_N \in \{0, -1\}$, bounded by $M = 1$.
      - Trigonometric series: $\sum_{n=1}^\infty \frac{\sin(n x)}{n^\alpha}$ and $\sum_{n=1}^\infty \frac{\cos(n x)}{n^\alpha}$ for $\alpha > 0$ and $x \not\in 2\pi\mathbb{Z}$, with Dirichlet kernel bound $|D_N(x)| \le \frac{1}{|\sin(x/2)|}$.
      - General Dirichlet series $\sum_{n=1}^\infty \frac{a_n}{n^s}$: Determines the abscissa of convergence $\sigma_c \le \sigma_b \le \sigma_a$.

  * **(3) Cauchy Condensation Test:**
    * **Cauchy criterion:** Let $(a_n)_{n \ge 1}$ be a non-negative, monotonically non-increasing sequence ($a_1 \ge a_2 \ge \dots \ge 0$).
      The series $\sum_{n=1}^\infty a_n$ converges if and only if the condensed series:
      $$
      \sum_{k=0}^\infty 2^k a_{2^k} \;=\; a_1 + 2 a_2 + 4 a_4 + 8 a_8 + \dots
      $$
      converges.
    * **Two-sided bounds:**
      $$
      \sum_{k=0}^K 2^k a_{2^{k+1}} \;\le\; \sum_{n=1}^{2^{K+1}-1} a_n \;\le\; \sum_{k=0}^K 2^k a_{2^k}.
      $$
    * **Base-$b$ condensation (Schlömilch generalization):** For any fixed integer $b \ge 2$:
      $\sum a_n$ converges $\iff \sum_{k=0}^\infty b^k a_{b^k}$ converges.
    * **Algorithmic condensation engine:**
      Transforms slow logarithmic/harmonic scales into geometric/exponential scales:
      - $a_n = \frac{1}{n^p} \implies 2^k a_{2^k} = 2^k \frac{1}{2^{k p}} = (2^{1-p})^k$ (geometric series, converges iff $p > 1$).
      - $a_n = \frac{1}{n (\log n)^p} \implies 2^k a_{2^k} = \frac{1}{(k \log 2)^p} = \frac{1}{(\log 2)^p} \frac{1}{k^p}$ (reduces to $p$-series).
      - Iterated logarithms $\frac{1}{n \log n \log \log n \cdots (\log^{(m)} n)^p}$ reduced inductively in $m$ steps.

  * **(4) Symbolic Integration by Parts and Differential Algebra:**
    * **Integration by parts:**
      $$
      \int u(x) v'(x) \, dx \;=\; u(x) v(x) - \int u'(x) v(x) \, dx, \qquad \int u \, dv \;=\; u v - \int v \, du.
      $$
    * **Repeated / Tabular integration by parts:**
      For smooth functions $f, g$:
      $$
      \int f(x) g(x) \, dx \;=\; \sum_{k=0}^{n-1} (-1)^k f^{(k)}(x) g^{(-k-1)}(x) + (-1)^n \int f^{(n)}(x) g^{(-n)}(x) \, dx,
      $$
      where $g^{(-j)}$ denotes the $j$-th iterated anti-derivative.
      When $f$ is a polynomial of degree $d$, choosing $n = d+1$ yields an exact closed-form anti-derivative without remaining integrals.
    * **Reduction formulas and recurrences:**
      Systematic generation of contiguous relation recurrences for parameterized integral families:
      - $I_n(x) \coloneqq \int x^n e^{a x} dx \implies I_n = \frac{x^n e^{a x}}{a} - \frac{n}{a} I_{n-1}$.
      - $S_n(x) \coloneqq \int \sin^n(x) dx \implies S_n = -\frac{1}{n} \sin^{n-1}(x) \cos(x) + \frac{n-1}{n} S_{n-2}$.
      - $L_n(x) \coloneqq \int (\log x)^n dx \implies L_n = x (\log x)^n - n L_{n-1}$.
    * **Cyclic integral solver (linear system in anti-derivatives):**
      Recognizes loops in repeated integration by parts:
      $$
      \int e^{a x} \cos(b x) dx \;=\; \frac{e^{a x} (a \cos(b x) + b \sin(b x))}{a^2 + b^2}.
      $$
    * **LIATE rule & differential algebra pass:**
      Logarithmic > Inverse trigonometric > Algebraic > Trigonometric > Exponential priority heuristic for assigning $u$ versus $dv$, integrated within the differential field framework $(K, \partial)$ and Risch integration algorithm.

  * **(5) Zeta Regularization and L-Function Analytic Continuation:**
    * **Spectral zeta function of an operator:**
      For an elliptic differential operator $A$ (e.g. Laplace-Beltrami operator $\Delta$ on a compact Riemannian manifold $(M, g)$) with discrete positive spectrum $0 < \lambda_1 \le \lambda_2 \le \dots \to \infty$:
      $$
      \zeta_A(s) \;\coloneqq\; \operatorname{Tr}(A^{-s}) \;=\; \sum_{n=1}^\infty \frac{1}{\lambda_n^s} \quad (\text{for } \operatorname{Re}(s) > \frac{\dim M}{2}).
      $$
      Admits a meromorphic continuation to $s \in \mathbb{C}$ with $s = 0$ as a regular point.
    * **Zeta-regularized functional determinant (Ray-Singer / Hawking):**
      $$
      \operatorname{det}_\zeta(A) \;\coloneqq\; \exp\left( - \left. \frac{d}{ds} \zeta_A(s) \right|_{s=0} \right) \;=\; \exp(-\zeta_A'(0)).
      $$
      - Harmonic oscillator: $A = -\frac{d^2}{dx^2} + \omega^2$ on $L^2(\mathbb{R})$.
      - Circle Laplacian: $A = -\frac{d^2}{dx^2}$ on $S^1$ has $\zeta_A(s) = 2 \left(\frac{L}{2\pi}\right)^{2s} \zeta(2s)$, yielding $\operatorname{det}_\zeta(A) = 4 \sin^2(\pi \dots)$ or $L^2$.
    * **Ramanujan and Euler-Maclaurin regularization:**
      Regularized summation of divergent series $\sum_{n=1}^\infty f(n)$:
      $$
      \sum_{n=1}^\infty n^k \;\rightsquigarrow\; \zeta(-k) \;=\; -\frac{B_{k+1}}{k+1}.
      $$
      Specifically: $\sum_{n=1}^\infty 1 = \zeta(0) = -\frac{1}{2}$, $\sum_{n=1}^\infty n = \zeta(-1) = -\frac{1}{12}$, $\sum_{n=1}^\infty n^2 = \zeta(-2) = 0$, $\sum_{n=1}^\infty n^3 = \zeta(-3) = \frac{1}{120}$.
    * **General $L$-functions and functional equations:**
      For an automorphic or motivic $L$-function $L(s, \pi) = \sum_{n=1}^\infty \frac{a_n}{n^s}$:
      - Completed $L$-function:
        $$
        \Lambda(s, \pi) \;\coloneqq\; N^{s/2} \gamma(s) L(s, \pi), \qquad \gamma(s) = \prod_{j=1}^r \Gamma_{\mathbb{R}}(s + \mu_j).
        $$
      - Functional equation: $\Lambda(s, \pi) = \epsilon(\pi) \Lambda(1 - s, \widetilde{\pi})$, where $|\epsilon(\pi)| = 1$.
      - Regularization at non-convergent points: evaluation of $L(s, \pi)$ at critical and non-critical integers $s \in \mathbb{Z}_{\le 0}$ via reflection formula and Bernoulli / modular symbols (Deligne's period conjecture, Beilinson regulator).

* **Preamble implementation requirements:**
  * **Convergence test suite:** `categories/analysis/convergence_tests.py`
    - `DirichletTest(a_seq, b_seq)`: certifies convergence of $\sum a_n b_n$ with explicit tail error bound $2 M b_{N+1}$.
    - `AbelSummation(a_seq, b_seq, N)`: formal summation by parts $A_N b_{N+1} + \sum_{n=1}^N A_n (b_n - b_{n+1})$.
    - `CauchyCondensation(a_seq, base=2)`: transforms monotonic sequence $a_n$ into condensed series $\sum b^k a_{b^k}$; automated decider for logarithmic/power series.
    - `AlternatingSeriesTest(b_seq)`: Leibniz test specialization.
  * **Diophantine approximation and irrationality:** `categories/number_theory/diophantine_approximation.py`
    - `DirichletApproximation(alpha, N)`: computes $p, q$ with $q \le N$ such that $|\alpha - p/q| < 1/(qN)$.
    - `IrrationalityCertificate(alpha, p_seq, q_seq)`: verifies condition $q_n \alpha - p_n \neq 0$ and $|q_n \alpha - p_n| \to 0$.
    - `ContinuedFractionConvergents(alpha, terms)`: generates best rational approximations $p_n/q_n$.
    - `IrrationalityMeasure(alpha)`: upper and lower bounds on $\mu(\alpha)$.
  * **Symbolic integration by parts:** `categories/calculus/symbolic_integration.py`
    - `IntegrationByParts(u, dv, var='x')`: applies $u v - \int v du$.
    - `TabularIntegration(f, g, var='x')`: generates tabular differentiation/integration table for polynomial $\times$ transcendental.
    - `ReductionFormula(integrand_family, param='n')`: derives contiguous recurrence relation.
    - `CyclicIntegralSolver(integrand, var='x')`: detects linear algebraic loop in repeated integration by parts and solves for $\int f dx$.
  * **Zeta regularization and functional determinants:** `categories/zeta/regularization.py`
    - `SpectralZetaFunction(eigenvalues_or_symbol)`: computes $\zeta_A(s) = \sum \lambda_n^{-s}$ and its analytic continuation.
    - `ZetaRegularizedDeterminant(spectral_zeta)`: computes $\operatorname{det}_\zeta(A) = \exp(-\zeta_A'(0))$.
    - `RamanujanSum(divergent_series)`: evaluates Euler-Maclaurin regularized sum $\sum^{\mathcal{R}} f(n)$.
  * **L-function analytic continuation:** `categories/l_functions/analytic_continuation.py`
    - `CompletedLFunction(l_series, gamma_factors, conductor, root_number)`: evaluates $\Lambda(s)$ and computes $L(s)$ via functional equation $\Lambda(s) = \epsilon \Lambda(1 - s)$.
    - `SpecialLValues(l_function, s_points)`: computes regularized values at negative integers and critical points.

Intended owners: `categories/analysis/convergence_tests.py` (`DirichletTest`, `CauchyCondensation`, `AbelSummation`), `categories/number_theory/diophantine_approximation.py` (`DirichletApproximation`, `IrrationalityCertificate`), `categories/calculus/symbolic_integration.py` (`IntegrationByParts`, `TabularIntegration`, `ReductionFormula`), `categories/zeta/regularization.py` (`SpectralZetaFunction`, `ZetaRegularizedDeterminant`, `RamanujanSum`), `categories/l_functions/analytic_continuation.py` (`CompletedLFunction`, `SpecialLValues`).


## Desired capability: Gerstenhaber algebra structure on Hochschild cohomology $HH^*(A, A)$ — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **Definition of a Gerstenhaber algebra:**
    * A *Gerstenhaber algebra* (or $G$-algebra) is a graded vector space $V = \bigoplus_{n \in \mathbb{Z}} V^n$ over a field $k$ (or commutative ring $R$) equipped with two bilinear operations:
      1. **Graded commutative associative cup product:**
         $$
         \smile \colon V^p \otimes V^q \longrightarrow V^{p+q}, \qquad a \smile b = (-1)^{p q} b \smile a, \qquad (a \smile b) \smile c = a \smile (b \smile c).
         $$
      2. **Graded Lie bracket of degree $-1$ (Gerstenhaber bracket):**
         $$
         [- , -] \colon V^p \otimes V^q \longrightarrow V^{p+q-1}.
         $$
         Equivalently, on the desuspended graded space $\mathfrak{g} \coloneqq V[1]$ with shifted grading $|a|' \coloneqq |a| - 1 = p - 1$, the bracket $[-,-]$ has degree 0 and satisfies:
         - Graded skew-symmetry:
           $$
           [a, b] \;=\; -(-1)^{(|a|-1)(|b|-1)} [b, a] \;=\; -(-1)^{p' q'} [b, a].
           $$
         - Graded Jacobi identity:
           $$
           [a, [b, c]] \;=\; [[a, b], c] + (-1)^{(|a|-1)(|b|-1)} [b, [a, c]].
           $$
      3. **Poisson derivation rule (Leibniz compatibility):**
         The adjoint action $[a, -]$ is a graded derivation of the cup product of degree $|a| - 1$:
         $$
         [a, b \smile c] \;=\; [a, b] \smile c + (-1)^{(|a|-1) |b|} b \smile [a, c].
         $$
    * Operadic interpretation: A Gerstenhaber algebra is an algebra over the operad $e_2 \coloneqq H_*(\mathcal{D}_2, k)$, the homology of the little 2-disks operad.

  * **Hochschild cochains and the Gerstenhaber bracket at cochain level:**
    * For an associative $k$-algebra $A$, the Hochschild cochain complex is $C^*(A, A) \coloneqq \bigoplus_{n \ge 0} C^n(A, A)$ where $C^n(A, A) \coloneqq \operatorname{Hom}_k(A^{\otimes n}, A)$ (with $C^0(A, A) = A$).
    * **Cup product at cochain level:** For $f \in C^p(A, A)$ and $g \in C^q(A, A)$:
      $$
      (f \smile g)(a_1, \dots, a_{p+q}) \;\coloneqq\; f(a_1, \dots, a_p) g(a_{p+1}, \dots, a_{p+q}).
      $$
      Associative, but not graded commutative on cochains ($f \smile g - (-1)^{p q} g \smile f$ is a coboundary).
    * **Gerstenhaber circle products (insertion operations):**
      For $1 \le i \le p$, the $i$-th composition $f \circ_i g \in C^{p+q-1}(A, A)$ substitutes $g$ into the $i$-th input of $f$:
      $$
      (f \circ_i g)(a_1, \dots, a_{p+q-1}) \;\coloneqq\; f(a_1, \dots, a_{i-1}, g(a_i, \dots, a_{i+q-1}), a_{i+q}, \dots, a_{p+q-1}).
      $$
      The total circle product is:
      $$
      f \circ g \;\coloneqq\; \sum_{i=1}^p (-1)^{(i-1)(q-1)} f \circ_i g \;\in\; C^{p+q-1}(A, A).
      $$
    * **Graded pre-Lie algebra structure:**
      On the shifted space $C^*(A, A)[1]$, the circle product $\circ$ satisfies the graded right pre-Lie identity:
      $$
      (f \circ g) \circ h - f \circ (g \circ h) \;=\; (-1)^{(q-1)(r-1)} \left( (f \circ h) \circ g - f \circ (h \circ g) \right).
      $$
    * **Cochain Gerstenhaber bracket:**
      The graded commutator of the pre-Lie product:
      $$
      [f, g] \;\coloneqq\; f \circ g - (-1)^{(p-1)(q-1)} g \circ f \;\in\; C^{p+q-1}(A, A).
      $$
      Equips $C^*(A, A)[1]$ with the structure of a differential graded Lie algebra (DGLA).
    * **Hochschild differential via multiplication $m$:**
      Let $m \in C^2(A, A)$ be the algebra multiplication $m(a, b) = a b$.
      Associativity of $A$ is equivalent to $[m, m] = 2 m \circ m = 0$.
      The Hochschild coboundary operator $d \colon C^n(A, A) \to C^{n+1}(A, A)$ is given by the adjoint action of $m$:
      $$
      d(f) \;=\; [m, f] \;=\; m \circ f - (-1)^{p-1} f \circ m.
      $$
      Nilpotence $d^2 = 0$ follows immediately from Jacobi: $d^2(f) = [m, [m, f]] = \frac{1}{2} [[m, m], f] = 0$.
    * **Descent to cohomology:**
      The Hochschild differential is a derivation of both the cup product and the Gerstenhaber bracket:
      $$
      d(f \smile g) \;=\; d(f) \smile g + (-1)^p f \smile d(g), \qquad d[f, g] \;=\; [d(f), g] + (-1)^{p-1} [f, d(g)].
      $$
      The Leibniz rule holds up to homotopy at the cochain level, inducing an exact Gerstenhaber algebra structure on $HH^*(A, A) = H^*(C^*(A, A), d)$.

  * **Brace algebras and higher homotopy structures ($B_\infty$):**
    * Brace operations (Getzler, Kadeishvili, Voronov):
      $f\{g_1, \dots, g_k\} \in C^{p + \sum q_j - k}(A, A)$ simultaneously substitutes $k$ cochains into disjoint slots of $f$.
      $f\{g\} = f \circ g$.
    * Satisfies the higher brace relations:
      $$
      f\{g_1, \dots, g_k\}\{h_1, \dots, h_m\} \;=\; \sum \pm f\{h_1, \dots, g_1\{h_i, \dots\}, \dots, g_k\{ \dots \}, \dots, h_m\}.
      $$
    * **Deligne's conjecture (proved by Tamarkin, Kontsevich, Voronov, McClure-Smith):**
      The Hochschild cochain complex $C^*(A, A)$ carries the action of an operad quasi-isomorphic to the singular chain operad $C_*(\mathcal{D}_2)$ of the little 2-disks operad $E_2$.
      Passing to cohomology $H^*(C^*(A, A))$ yields the Gerstenhaber operad $H_*(E_2) = \operatorname{Gerst}$.

  * **Hochschild-Kostant-Rosenberg (HKR) isomorphism and Schouten bracket:**
    * For a smooth affine variety $X$ (or smooth commutative algebra $A = \mathcal{O}(X)$ over a field of characteristic 0):
      The HKR map defines an isomorphism of graded commutative algebras:
      $$
      \operatorname{HKR} \colon HH^*(A, A) \;\xrightarrow{\sim}\; \Gamma(X, \bigwedge\nolimits^{\!*} T_X) \;=\; \operatorname{PolyVect}^*(X).
      $$
    * Under the HKR isomorphism:
      - The cup product $\smile$ on $HH^*(A, A)$ corresponds to the exterior product $\wedge$ of polyvector fields.
      - The Gerstenhaber bracket $[-,-]$ on $HH^*(A, A)$ corresponds to the **Schouten-Nijenhuis bracket** $[-,-]_{\mathrm{SN}}$ on polyvector fields $\bigwedge^* T_X$.
    * At the cochain level, Kontsevich's Formality Theorem establishes an $L_\infty$ quasi-isomorphism between the DGLA $C^*(A, A)[1]$ and the DGLA of polyvector fields $\operatorname{PolyVect}^*(X)[1]$ (with zero differential), yielding deformation quantization (star-products).

  * **Low-degree interpretations and deformation theory:**
    * **Degree 0:** $HH^0(A, A) = Z(A)$ (the center of $A$).
      Cup product is algebra multiplication in $Z(A)$.
      The bracket $[z, f] = 0$ for all $z \in HH^0(A)$ and $f \in HH^*(A)$ (since degree is $0 + p - 1 = p - 1 < p$).
    * **Degree 1:** $HH^1(A, A) = \operatorname{Der}_k(A) / \operatorname{InnDer}(A) = \operatorname{OutDer}(A)$ (outer derivations).
      For $D_1, D_2 \in HH^1(A)$: $[D_1, D_2]$ is the standard Lie bracket of derivations $[D_1, D_2] = D_1 \circ D_2 - D_2 \circ D_1$.
      For $D \in HH^1(A)$ and $z \in HH^0(A)$: $[D, z] = D(z)$ (derivation applied to center).
      For $D \in HH^1(A)$ and $\omega \in HH^p(A)$: $[D, \omega] = \mathcal{L}_D(\omega)$ (Lie derivative).
    * **Degree 2:** $HH^2(A, A)$ classifies infinitesimal associative deformations of $A$:
      A first-order deformation $a \ast_t b = a b + t \mu_1(a, b) + \mathcal{O}(t^2)$ is associative mod $t^2$ iff $d \mu_1 = 0 \in C^3(A, A)$.
      Primary obstruction to second-order extension is $\frac{1}{2}[\mu_1, \mu_1] \in HH^3(A, A)$.
      The Maurer-Cartan equation in $C^*(A, A)[1]$:
      $$
      d \alpha + \frac{1}{2} [\alpha, \alpha] \;=\; 0, \qquad \alpha \in t C^2(A, A)[[t]],
      $$
      classifies formal deformations / star-products $A[[t]]$.

  * **Batalin-Vilkovisky (BV) structure on Frobenius and Calabi-Yau algebras:**
    * When $A$ is a symmetric Frobenius algebra or Calabi-Yau algebra of dimension $d$:
      Van den Bergh duality yields an isomorphism:
      $$
      HH^n(A, A) \;\cong\; HH_{d-n}(A, A).
      $$
    * Transporting the Connes boundary operator $B \colon HH_k(A) \to HH_{k+1}(A)$ across Van den Bergh duality yields a degree $-1$ operator:
      $$
      \Delta \colon HH^n(A, A) \longrightarrow HH^{n-1}(A, A), \qquad \Delta^2 = 0.
      $$
    * The Gerstenhaber bracket is recovered from $\Delta$ and the cup product via the 7-term relation / BV deviation formula:
      $$
      [a, b] \;=\; (-1)^{|a|} \left( \Delta(a \smile b) - \Delta(a) \smile b - (-1)^{|a|} a \smile \Delta(b) \right).
      $$
      Equips $HH^*(A, A)$ with the structure of a **Batalin-Vilkovisky (BV) algebra** (algebra over the framed little 2-disks operad $f\mathcal{D}_2$).

* **Preamble implementation requirements:**
  * **Hochschild cochains and pre-Lie/bracket operations:** `categories/homology/gerstenhaber.py`
    - `HochschildCochain(A, degree, map)`: cochain $f \colon A^{\otimes n} \to A$.
    - `cup_product(f, g)`: associative cochain cup product $f \smile g \in C^{p+q}(A, A)$.
    - `circle_product_i(f, g, i)`: substitution $f \circ_i g$.
    - `circle_product(f, g)`: total graded pre-Lie product $f \circ g = \sum (-1)^{(i-1)(q-1)} f \circ_i g$.
    - `gerstenhaber_bracket(f, g)`: graded commutator $[f, g] = f \circ g - (-1)^{(p-1)(q-1)} g \circ f$.
    - `hochschild_differential(f, m)`: evaluates $[m, f]$.
  * **Gerstenhaber algebra structure on cohomology:** `categories/homology/hochschild.py`
    - `GerstenhaberAlgebra`: structure on `HH^*(A, A)` providing:
      * `cup(a, b)`: graded commutative product $HH^p \otimes HH^q \to HH^{p+q}$.
      * `bracket(a, b)`: graded Lie bracket $HH^p \otimes HH^q \to HH^{p+q-1}$.
      * `check_poisson_rule(a, b, c)`: certifies $[a, b \smile c] = [a, b] \smile c + (-1)^{(|a|-1)|b|} b \smile [a, c]$.
      * `check_jacobi_identity(a, b, c)`: certifies graded Jacobi on $HH^*[1]$.
  * **Brace algebra structure:** `categories/algebras/brace_algebras.py`
    - `BraceAlgebra`: implementation of operations $f\{g_1, \dots, g_k\}$ and higher homotopy relations.
  * **Schouten-Nijenhuis bracket comparison:** `categories/schemes/hochschild_kostant_rosenberg.py`
    - `HKR_Gerstenhaber_isomorphism(X)`: maps Gerstenhaber bracket on $HH^*(\mathcal{O}(X))$ to Schouten-Nijenhuis bracket on $\bigwedge^* T_X$.
  * **Deformation and Maurer-Cartan:** `categories/deformation/deformation_quantization.py`
    - `MaurerCartanElement(C_star)`: cochain $\alpha \in C^2(A, A)$ satisfying $d\alpha + \frac{1}{2}[\alpha, \alpha] = 0$.
    - `DeformationObstruction(mu)`: evaluates $[\mu, \mu] \in HH^3(A, A)$.
  * **Batalin-Vilkovisky operator:** `categories/homology/batalin_vilkovisky.py`
    - `BVOperator(HH_cohomology, connes_B, vdb_dual)`: computes $\Delta \colon HH^n \to HH^{n-1}$ and verifies $[a, b] = (-1)^{|a|} (\Delta(a \smile b) - \dots)$.

Intended owners: `categories/homology/gerstenhaber.py` (`GerstenhaberBracket`, `CircleProduct`, `PreLieAlgebra`), `categories/homology/hochschild.py` (`GerstenhaberAlgebra`, `HochschildCohomology`), `categories/algebras/brace_algebras.py` (`BraceAlgebra`), `categories/schemes/hochschild_kostant_rosenberg.py` (`HKR_Schouten`), `categories/deformation/deformation_quantization.py` (`MaurerCartan`, `AssociativeDeformation`), `categories/homology/batalin_vilkovisky.py` (`BVAlgebra`, `BVOperator`).


## Desired capability: Continuous actions of topological groups on topological spaces — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **Topological groups ($G \in \mathbf{TopGrp}$):**
    * A *topological group* is a group $G$ equipped with a topology such that the group multiplication $\mu \colon G \times G \to G$, $(g, h) \mapsto g h$, and the inversion $\iota \colon G \to G$, $g \mapsto g^{-1}$, are continuous maps (with $G \times G$ endowed with the product topology).
    * Homogeneity: Left translations $L_g \colon h \mapsto g h$ and right translations $R_g \colon h \mapsto h g$ are homeomorphisms of $G$ for all $g \in G$.
    * Uniform structures: The topology of $G$ is induced by canonical left and right uniform structures. Every topological group satisfying the $T_0$ separation axiom is completely regular ($T_{3\frac{1}{2}}$) and Hausdorff ($T_2$).
    * Subgroups: Any subgroup $H \le G$ is a topological group with the subspace topology. If $H$ is open, then $H$ is also closed.
    * Quotient groups: For a normal subgroup $N \triangleleft G$, the quotient group $G/N$ with the quotient topology is a topological group, and the projection $\pi \colon G \twoheadrightarrow G/N$ is a continuous open homomorphism. $G/N$ is Hausdorff iff $N$ is closed in $G$.
    * Identity component: The connected component $G_0$ of the identity $e \in G$ is a closed normal subgroup, and the quotient group $G/G_0$ is totally disconnected.

  * **Continuous group actions ($G \curvearrowright X$ in $\mathbf{Top}$):**
    * A *continuous left action* of a topological group $G$ on a topological space $X$ is a continuous map $\alpha \colon G \times X \to X$, $(g, x) \mapsto g \cdot x$, such that:
      1. $e \cdot x = x$ for all $x \in X$.
      2. $g \cdot (h \cdot x) = (g h) \cdot x$ for all $g, h \in G, x \in X$.
    * Equivalently, a group homomorphism $\rho \colon G \to \operatorname{Homeo}(X)$ into the homeomorphism group of $X$. When $X$ is locally compact Hausdorff, the action $\alpha$ is continuous if and only if $\rho \colon G \to \operatorname{Homeo}(X)$ is continuous when $\operatorname{Homeo}(X)$ carries the compact-open topology.
    * Continuous right actions $\beta \colon X \times G \to X$ defined symmetrically or via $x \cdot g \coloneqq g^{-1} \cdot x$.

  * **Orbits, stabilizers, and quotient orbit spaces ($X/G$):**
    * **Stabilizer (isotropy subgroup):** For each $x \in X$, the stabilizer is:
      $$
      G_x \;\coloneqq\; \{ g \in G \mid g \cdot x = x \}.
      $$
      If $X$ is $T_1$, $G_x$ is a closed subgroup of $G$ (as the preimage of the closed point $\{x\}$ under the continuous orbit map $g \mapsto g \cdot x$).
    * **Orbit:** The orbit of $x \in X$ is the subset $G \cdot x \coloneqq \{ g \cdot x \mid g \in G \} \subseteq X$.
      The canonical orbit map induces a continuous bijection:
      $$
      \phi_x \colon G / G_x \longrightarrow G \cdot x, \qquad g G_x \longmapsto g \cdot x.
      $$
      If $G$ is compact, or if $G$ is locally compact $\sigma$-compact and $X$ is Baire with locally closed orbit, $\phi_x$ is a homeomorphism onto its image.
    * **Orbit space $X/G$:**
      The set of orbits $X/G$ equipped with the quotient topology induced by the canonical surjective projection $\pi \colon X \twoheadrightarrow X/G$, $x \mapsto G \cdot x$.
      - **Open mapping theorem for orbit projections:** The quotient projection $\pi \colon X \to X/G$ is always an **open map**:
        For any open set $U \subset X$, $\pi^{-1}(\pi(U)) = \bigcup_{g \in G} g \cdot U$ is an open set in $X$ (as an arbitrary union of open homeomorphic images $g \cdot U$), hence $\pi(U)$ is open in $X/G$.
      - **Separation criteria for $X/G$:**
        * $X/G$ is $T_1$ if and only if every orbit $G \cdot x$ is a closed subset of $X$.
        * $X/G$ is Hausdorff ($T_2$) if and only if the orbit equivalence relation:
          $$
          R \;\coloneqq\; \{ (x, y) \in X \times X \mid \exists g \in G \text{ with } y = g \cdot x \} \;\subset\; X \times X
          $$
          is a closed subset of $X \times X$.

  * **Action predicates and geometric classifications:**
    * **Transitive action:** $X$ consists of a single orbit ($G \cdot x = X$). Then $X \cong G/H$ is a homogeneous space for $H = G_{x_0}$.
    * **Free action:** $G_x = \{e\}$ for all $x \in X$ (no non-trivial fixed points).
    * **Faithful / effective action:** $\bigcap_{x \in X} G_x = \{e\}$ (the kernel of the action is trivial, so $G \hookrightarrow \operatorname{Homeo}(X)$).
    * **Proper action:**
      The action $\alpha \colon G \times X \to X$ is *proper* if the map:
      $$
      \Theta \colon G \times X \longrightarrow X \times X, \qquad (g, x) \longmapsto (g \cdot x, x)
      $$
      is a proper continuous map (i.e. the preimage of every compact subset of $X \times X$ is compact in $G \times X$).
      - **Structural consequences of properness:**
        * Every stabilizer $G_x$ is a compact subgroup of $G$.
        * Every orbit $G \cdot x$ is closed in $X$, and $G/G_x \cong G \cdot x$ is a homeomorphism.
        * The orbit space $X/G$ is Hausdorff (and locally compact if $X$ is).
      - **Discrete case (properly discontinuous actions):**
        When $G$ is a discrete group, an action on a locally compact Hausdorff space $X$ is proper if and only if for every compact subset $K \subset X$, the set $\{ g \in G \mid (g \cdot K) \cap K \neq \emptyset \}$ is finite.
    * **Cocompact action:** The quotient space $X/G$ is compact.
    * **Slice theorem (Koszul, Palais):**
      Let $G$ be a Lie group acting properly on a smooth manifold $X$. For every $x \in X$ with compact stabilizer $H = G_x$, there exists an $H$-invariant submanifold $S \subset X$ containing $x$ (a *slice* at $x$) such that the equivariant map:
      $$
      G \times_H S \longrightarrow X, \qquad [g, s] \longmapsto g \cdot s
      $$
      is an open equivariant embedding onto a $G$-invariant neighborhood of $G \cdot x$.

  * **The category of $G$-spaces ($G\mathbf{-Top}$):**
    * **Category $G\mathbf{-Top}$:**
      - Objects: $G$-spaces $(X, \alpha)$, where $X \in \mathbf{Top}$ and $\alpha \colon G \times X \to X$ is a continuous action.
      - Morphisms: Continuous $G$-equivariant maps $f \colon X \to Y$ satisfying $f(g \cdot x) = g \cdot f(x)$ for all $g \in G, x \in X$.
    * **Universal constructions in $G\mathbf{-Top}$:**
      - **Fixed point space:** $X^G \coloneqq \{ x \in X \mid g \cdot x = x \; \forall g \in G \}$. If $X$ is Hausdorff, $X^G$ is a closed subspace of $X$.
      - **Subgroup fixed points:** For any subgroup $H \le G$, $X^H \coloneqq \{ x \in X \mid h \cdot x = x \; \forall h \in H \}$, which is a $W(H)$-space where $W(H) \coloneqq N_G(H)/H$ is the Weyl group.
      - **Products:** $X \times Y$ with diagonal action $g \cdot (x, y) = (g \cdot x, g \cdot y)$.
      - **Equivariant mapping spaces:** $\operatorname{Map}(X, Y)$ with conjugation action $(g \cdot f)(x) \coloneqq g \cdot f(g^{-1} \cdot x)$, where $G$-equivariant maps are the fixed points $\operatorname{Map}_G(X, Y) = \operatorname{Map}(X, Y)^G$.
      - **Induction and restriction adjunction:**
        For a closed subgroup $H \le G$, the restriction functor $\operatorname{Res}_H^G \colon G\mathbf{-Top} \to H\mathbf{-Top}$ has:
        * Left adjoint (induction): $\operatorname{Ind}_H^G(Y) \coloneqq G \times_H Y = (G \times Y) / H$, where $(g h, y) \sim (g, h \cdot y)$.
        * Right adjoint (coinduction): $\operatorname{CoInd}_H^G(Y) \coloneqq \operatorname{Map}_H(G, Y)$.
        Natural bijection: $\operatorname{Hom}_G(G \times_H Y, X) \cong \operatorname{Hom}_H(Y, \operatorname{Res}_H^G X)$.

  * **Equivariant homotopy and Borel equivariant cohomology:**
    * **Borel construction (homotopy quotient):**
      Let $EG \to BG$ be the universal principal $G$-bundle, where $EG$ is a contractible space with a continuous free $G$-action, and $BG = EG/G$ is the classifying space.
      The *homotopy quotient* (or Borel construction) is:
      $$
      X_{hG} \;\coloneqq\; EG \times_G X \;=\; (EG \times X) / G.
      $$
      - If the action $G \curvearrowright X$ is free, the canonical projection $X_{hG} \to X/G$ is a homotopy equivalence.
      - If $X = \text{pt}$, then $X_{hG} = BG$.
    * **Borel equivariant cohomology:**
      $$
      H_G^*(X; R) \;\coloneqq\; H^*(X_{hG}; R) \;=\; H^*(EG \times_G X; R).
      $$
      Equipped with the canonical $H^*(BG; R)$-algebra structure via the fibration $X \to X_{hG} \to BG$.
    * **Equivariant localization theorem (Borel-Atiyah-Segal):**
      For a compact torus $T \cong (S^1)^r$ acting on a compact space $X$, the restriction homomorphism $H_T^*(X; \mathbb{Q}) \to H_T^*(X^T; \mathbb{Q})$ becomes an isomorphism upon inverting the non-zero elements of $H^*(BT; \mathbb{Q}) \cong \mathbb{Q}[t_1, \dots, t_r]$.
    * **Homotopy fixed points:** $X^{hG} \coloneqq \operatorname{Map}_G(EG, X)$.

  * **Principal bundles and associated bundles:**
    * A *principal $G$-bundle* is a continuous map $p \colon P \to B$ equipped with a continuous right action $P \times G \to P$ such that $p$ is locally trivial and $G$ acts freely and transitively on the fibers ($P/G \cong B$).
    * **Associated bundle functor:**
      Given a principal $G$-bundle $P \to B$ and a left $G$-space $F$, the associated fiber bundle is:
      $$
      P \times_G F \;\coloneqq\; (P \times F) / G \longrightarrow B,
      $$
      with standard fiber $F$.

* **Preamble implementation requirements:**
  * **Topological groups:** `categories/topology/topological_groups.py`
    - `TopologicalGroup(underlying_group, topology)`: verifies continuity of multiplication $\mu$ and inversion $\iota$.
    - Properties & predicates: `is_connected()`, `identity_component()`, `is_compact()`, `is_locally_compact()`, `is_hausdorff()`.
    - `quotient_group(N)`: constructs $G/N$ with quotient topology.
  * **Continuous group actions:** `categories/topology/group_actions.py`
    - `TopologicalGroupAction(G, X, action_map, side='left')`: validates action axioms $e \cdot x = x$, $(g h) x = g(h x)$ and continuity.
    - `orbit(x)`: returns $G \cdot x \subset X$.
    - `stabilizer(x)`: returns $G_x \le G$ as a closed subgroup.
    - `orbit_space()`: constructs quotient space $X/G$ with open projection map $\pi$.
    - Predicates: `is_transitive()`, `is_free()`, `is_faithful()`, `is_proper()`, `is_properly_discontinuous()`, `is_cocompact()`.
    - `slice(x)`: Palais slice $S$ and diffeomorphism $G \times_H S \cong U$ for proper Lie actions.
  * **Equivariant category $G\mathbf{-Top}$:** `categories/topology/equivariant.py`
    - `GSpace(G, X, action)`: object in $G\mathbf{-Top}$.
    - `EquivariantMap(f, source_gspace, target_gspace)`: certifies $f(g x) = g f(x)$.
    - `fixed_points(H=None)`: constructs $X^G$ or $X^H$.
    - `induction(H, Y)`: evaluates $G \times_H Y$.
    - `borel_construction(EG)`: constructs homotopy quotient $X_{hG} = EG \times_G X$.
    - `equivariant_cohomology(coeff_ring)`: computes $H_G^*(X; R) = H^*(X_{hG}; R)$.
  * **Principal and associated bundles:** `categories/topology/principal_bundles.py`
    - `PrincipalBundle(P, B, G, action, projection)`: validates principal $G$-bundle structure.
    - `associated_bundle(F)`: constructs $P \times_G F \to B$.

Intended owners: `categories/topology/topological_groups.py` (`TopologicalGroup`, `QuotientGroup`), `categories/topology/group_actions.py` (`TopologicalGroupAction`, `OrbitSpace`, `Stabilizer`, `Slice`), `categories/topology/equivariant.py` (`GSpace`, `EquivariantMap`, `BorelConstruction`, `EquivariantCohomology`), `categories/topology/principal_bundles.py` (`PrincipalBundle`, `AssociatedBundle`).

## Desired capability: Associated torus $T(L) = L_\mathbb{R}/L$ and abelian varieties from $\mathbb{Z}$-lattices — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **The real torus $T(L) = L_\mathbb{R}/L$ of a $\mathbb{Z}$-lattice:**
    * Let $L$ be a free $\mathbb{Z}$-module of finite rank $n$ (a $\mathbb{Z}$-lattice).
    * Ambient real vector space: $L_\mathbb{R} \coloneqq L \otimes_\mathbb{Z} \mathbb{R} \cong \mathbb{R}^n$.
    * $L \subset L_\mathbb{R}$ is a discrete, cocompact subgroup.
    * The associated **real torus** is the quotient Lie group:
      $$
      T(L) \;\coloneqq\; L_\mathbb{R} / L \;\cong\; (\mathbb{R}/\mathbb{Z})^n \;\cong\; (S^1)^n.
      $$
      $T(L)$ is a compact, connected abelian Lie group of real dimension $n$.
    * **Topological invariants:**
      - Fundamental group: $\pi_1(T(L), 0) \cong L$.
      - Homology: $H_1(T(L), \mathbb{Z}) \cong L$, and $H_k(T(L), \mathbb{Z}) \cong \bigwedge^k L$.
      - Cohomology ring: $H^*(T(L), \mathbb{Z}) \cong \bigwedge^* L^\vee$, where $L^\vee \coloneqq \operatorname{Hom}_\mathbb{Z}(L, \mathbb{Z})$ is the dual lattice.
    * **Dual torus (character group):**
      $$
      T(L)^\vee \;\coloneqq\; L_\mathbb{R}^\vee / L^\vee \;\cong\; \operatorname{Hom}_{\mathbf{Grp}}(T(L), S^1) \;\cong\; \operatorname{Pic}^0_{\mathrm{top}}(T(L)).
      $$

  * **Complex structures and complex tori ($n = 2g$):**
    * When $\operatorname{rank}(L) = n = 2g$ is even, a complex structure on the real torus $T(L)$ is specified by an $\mathbb{R}$-linear map $J \colon L_\mathbb{R} \to L_\mathbb{R}$ satisfying $J^2 = -\operatorname{id}_{L_\mathbb{R}}$.
    * Induces a direct sum decomposition of the complexification:
      $$
      L_\mathbb{C} \;\coloneqq\; L_\mathbb{R} \otimes_\mathbb{R} \mathbb{C} \;=\; V \oplus \bar{V},
      $$
      where $V = L_\mathbb{R}^{(1,0)} = \{ v - i J v \mid v \in L_\mathbb{R} \} \cong \mathbb{C}^g$ is the $+i$-eigenspace of $J$.
    * Projection $\pi \colon L_\mathbb{R} \xrightarrow{\sim} V$ embeds $L$ as a full lattice $\Lambda \coloneqq \pi(L) \subset V \cong \mathbb{C}^g$.
    * The quotient $X = (L_\mathbb{R}, J) / L \cong V / \Lambda$ is a **complex torus** of complex dimension $g$, equipped with a canonical holomorphic Lie group structure.
    * Tangent and cotangent spaces: $T_0 X \cong V$, $T_0^* X \cong V^* \cong H^0(X, \Omega_X^1)$.

  * **Criterion for $T(L)$ to be an abelian variety (Riemann bilinear relations):**
    * A complex torus $X = V/\Lambda$ is an **abelian variety** (algebraic complex torus embeddable in projective space) if and only if it admits a **Riemann form** (a polarization).
    * **Riemann form (polarization):** An alternating $\mathbb{Z}$-bilinear form $E \colon L \times L \to \mathbb{Z}$ ($E \in \bigwedge^2 L^\vee \cong H^2(X, \mathbb{Z})$) satisfying the two **Riemann Bilinear Relations**:
      1. **Hodge type $(1, 1)$:** $E(J u, J v) = E(u, v)$ for all $u, v \in L_\mathbb{R}$ (so $c_1(\mathcal{L}) = E \in H^{1,1}(X) \cap H^2(X, \mathbb{Z}) \cong \operatorname{NS}(X)$).
      2. **Positive-definiteness:** $g_E(u, v) \coloneqq E(u, J v)$ is positive-definite, i.e. $E(u, J u) > 0$ for all $u \neq 0$ (so $H(u, v) = E(J u, v) + i E(u, v)$ is positive-definite Hermitian on $V$).
    * **Polarization type:** By Frobenius normal form for skew-symmetric integer matrices, there exists a symplectic basis of $L$ with matrix $[E] = \begin{pmatrix} 0 & D \\ -D & 0 \end{pmatrix}$, $D = \operatorname{diag}(d_1, \dots, d_g)$ with $d_1 \mid \dots \mid d_g \in \mathbb{Z}_{>0}$.
    * **Principal polarization:** $d_1 = \dots = d_g = 1$, inducing an isomorphism $\lambda_E \colon X \xrightarrow{\sim} \check{X} \coloneqq \operatorname{Pic}^0(X)$.

  * **Period matrices and the Siegel upper half-space $\mathbb{H}_g$:**
    * In an adapted symplectic basis, the period matrix of $\Lambda$ in $V$ takes normalized form $\Pi = (Z \;\; I_g)$ with $Z \in \operatorname{Mat}_{g \times g}(\mathbb{C})$.
    * Riemann bilinear relations: $Z^{\mathrm{T}} = Z$ and $\operatorname{Im}(Z) > 0$. Thus $Z \in \mathbb{H}_g$.
    * Moduli space of principally polarized abelian varieties (PPAVs): $\mathcal{A}_g \cong \operatorname{Sp}_{2g}(\mathbb{Z}) \backslash \mathbb{H}_g$.

  * **Appell-Humbert theorem and line bundles:**
    * Line bundles $\mathcal{L}(H, \chi)$ on $X$ are classified by Hermitian forms $H$ on $V$ with $\operatorname{Im} H(\Lambda, \Lambda) \subset \mathbb{Z}$ and semi-characters $\chi \colon \Lambda \to U(1)$.
    * Exact sequence: $0 \to \operatorname{Pic}^0(X) \to \operatorname{Pic}(X) \to \operatorname{NS}(X) \to 0$.
    * Riemann-Roch: $h^0(X, \mathcal{L}) = d_1 \cdots d_g = \sqrt{\det E}$. Global sections are Riemann theta functions with characteristics.

  * **Euclidean lattices and flat Riemannian tori:**
    * A positive-definite symmetric form $b \colon L \times L \to \mathbb{Z}$ (or $\mathbb{R}$) induces a flat Riemannian metric $g_b$ on $T(L)$.
    * Volume: $\operatorname{Vol}(T(L)) = \sqrt{\det B}$.
    * Laplace spectrum: $\operatorname{Spec}(\Delta) = \{ 4\pi^2 b^*(v, v) \mid v \in L^\vee \}$, where $b^*$ is the dual metric on $L^\vee$.
    * Spectral theta series: $\Theta_{T(L)}(t) = \operatorname{Tr}(e^{-t \Delta}) = \sum_{v \in L^\vee} e^{-4\pi^2 t b^*(v, v)}$.
    * Milnor isospectral non-isometric tori: the even unimodular lattices $E_8 \oplus E_8$ and $D_{16}^+$ in dimension 16 have identical theta series $\Theta_L(t)$ but non-isomorphic lattices, producing isospectral non-isometric flat tori.

  * **Jacobian and Albanese varieties:**
    * For a compact Riemann surface $C$ of genus $g$: $L = H_1(C, \mathbb{Z})$ with intersection pairing $E = (\cdot, \cdot)$ unimodular symplectic. The Jacobian $\operatorname{Jac}(C) = H^0(C, \Omega^1_C)^\vee / H_1(C, \mathbb{Z})$ is a canonically principally polarized abelian variety.
    * For a smooth projective variety $X$: the Albanese variety $\operatorname{Alb}(X) = H^0(X, \Omega_X^1)^\vee / H_1(X, \mathbb{Z})/\operatorname{tors}$ is an abelian variety equipped with the universal morphism $X \to \operatorname{Alb}(X)$.

* **Preamble implementation requirements:**
  * `categories/lattices/torus.py`:
    - `LatticeTorus(L)`: constructs real torus $T(L) = L_\mathbb{R}/L$.
    - `dimension()`: returns $\operatorname{rank}(L)$.
    - `fundamental_group()`: returns $L$.
    - `homology(k)`: returns exterior power $\bigwedge^k L$.
    - `cohomology(k)`: returns $\bigwedge^k L^\vee$.
    - `dual_torus()`: returns $T(L)^\vee = L_\mathbb{R}^\vee / L^\vee$.
  * `categories/complex_geometry/complex_tori.py`:
    - `ComplexTorus(L, J)`: complex structure $J \in \operatorname{End}(L_\mathbb{R})$ with $J^2 = -\operatorname{id}$.
    - `period_matrix()`: period matrix $\Pi \in \operatorname{Mat}_{g \times 2g}(\mathbb{C})$.
    - `is_algebraic()`: checks whether a polarizing Riemann form exists.
  * `categories/abelian_varieties/abelian_variety.py`:
    - `AbelianVariety(L, J, E)`: abelian variety certified by polarization $E \in \bigwedge^2 L^\vee$.
    - `polarization_type()`: elementary divisors $(d_1, \dots, d_g)$.
    - `is_principally_polarized()`: checks $d_1 = \dots = d_g = 1$.
    - `siegel_period_matrix()`: normalized period matrix $Z \in \mathbb{H}_g$.
    - `dual_abelian_variety()`: constructs $\check{X} = \operatorname{Pic}^0(X)$.
  * `categories/riemannian/flat_tori.py`:
    - `FlatRiemannianTorus(L, b)`: flat metric from positive-definite symmetric form $b$.
    - `volume()`: $\sqrt{\det B}$.
    - `laplace_spectrum(cutoff=None)`: eigenvalues with multiplicities from $L^\vee$.
    - `spectral_theta_series()`: $\operatorname{Tr}(e^{-t \Delta})$.
    - `is_isospectral_to(other)`: tests isospectrality via lattice theta series equality.
  * `categories/abelian_varieties/jacobians.py`:
    - `JacobianVariety(curve)`: Torelli map from algebraic curves to PPAVs.
    - `AlbaneseVariety(variety)`: universal morphism to Albanese variety.

Intended owners: `categories/lattices/torus.py` (`LatticeTorus`, `DualTorus`), `categories/complex_geometry/complex_tori.py` (`ComplexTorus`, `PeriodMatrix`), `categories/abelian_varieties/abelian_variety.py` (`AbelianVariety`, `RiemannForm`, `Polarization`), `categories/riemannian/flat_tori.py` (`FlatRiemannianTorus`, `LaplaceSpectrum`), `categories/abelian_varieties/jacobians.py` (`JacobianVariety`, `AlbaneseVariety`).

## Desired capability: Cartier and Pontryagin dualities — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **Pontryagin duality on locally compact abelian groups ($\mathbf{LCA}$):**
    * Let $\mathbf{LCA}$ be the category of Hausdorff, locally compact topological abelian groups with continuous group homomorphisms.
    * **Circle group:** $\mathbb{T} \coloneqq \mathbb{R}/\mathbb{Z} \cong U(1) = \{ z \in \mathbb{C} \mid |z| = 1 \}$, a compact connected abelian Lie group.
    * **Pontryagin dual (character group):** For $G \in \mathbf{LCA}$, the dual group is:
      $$
      \widehat{G} \;\coloneqq\; \operatorname{Hom}_{\mathbf{LCA}}(G, \mathbb{T}),
      $$
      endowed with the compact-open topology (uniform convergence on compact sets $K \subset G$). $\widehat{G}$ is also an object of $\mathbf{LCA}$.
    * **Pontryagin Duality Theorem:** The canonical evaluation homomorphism
      $$
      \alpha_G \colon G \longrightarrow \widehat{\widehat{G}}, \quad \alpha_G(x)(\chi) \coloneqq \chi(x),
      $$
      is an isomorphism of topological groups (both an algebraic isomorphism and a homeomorphism).
    * **Categorical equivalence:** The functor $(-)\,\widehat{}\colon \mathbf{LCA}^{\mathrm{op}} \xrightarrow{\sim} \mathbf{LCA}$ is a contravariant equivalence of categories, and is canonically self-inverse.
    * **Dual pairs & topological correspondences:**
      - **Compact $\longleftrightarrow$ Discrete:** $G$ is compact if and only if $\widehat{G}$ is discrete.
        Examples: $\widehat{\mathbb{Z}} \cong \mathbb{T}$, $\widehat{\mathbb{T}} \cong \mathbb{Z}$.
      - **Finite groups are self-dual:** For finite abelian $G$, $\widehat{G} \cong G$ (non-canonically).
      - **Self-dual continuous groups:** $\widehat{\mathbb{R}} \cong \mathbb{R}$ under $(x, y) \mapsto e^{2\pi i x y}$; $p$-adic fields $\widehat{\mathbb{Q}_p} \cong \mathbb{Q}_p$ under additive characters $\psi_p(x) = e^{2\pi i \{x\}_p}$; adele ring $\widehat{\mathbb{A}_\mathbb{Q}} \cong \mathbb{A}_\mathbb{Q}$ (Tate's thesis).
      - **Connected $\longleftrightarrow$ Torsion-free:** $G$ is connected if and only if $\widehat{G}$ is torsion-free.
      - **Torsion $\longleftrightarrow$ Profinite:** Discrete torsion groups dualize to compact totally disconnected (profinite) groups (e.g. $\widehat{\mathbb{Q}/\mathbb{Z}} \cong \widehat{\mathbb{Z}} = \varprojlim \mathbb{Z}/n\mathbb{Z}$).
    * **Annihilators and exact sequences:**
      - For a closed subgroup $H \le G$, its **annihilator** is the closed subgroup
        $$
        H^\perp \;\coloneqq\; \{ \chi \in \widehat{G} \mid \chi(h) = 1 \text{ for all } h \in H \} \le \widehat{G}.
        $$
      - Canonical isomorphisms:
        $$
        \widehat{G/H} \;\cong\; H^\perp, \qquad \widehat{H} \;\cong\; \widehat{G} / H^\perp.
        $$
      - Double annihilator: $(H^\perp)^\perp = \alpha_G(H) \cong H$.
      - Duality turns short exact sequences in $\mathbf{LCA}$ into short exact sequences:
        $$
        0 \to A \to B \to C \to 0 \quad \Longrightarrow \quad 0 \to \widehat{C} \to \widehat{B} \to \widehat{A} \to 0.
        $$
    * **Harmonic analysis and Fourier transform:**
      - Unique (up to scale) Haar measure $\mu_G$ on $G$ determines a dual Haar measure $\mu_{\widehat{G}}$ on $\widehat{G}$.
      - Fourier transform $\mathcal{F} \colon L^1(G) \to C_0(\widehat{G})$, $\widehat{f}(\chi) = \int_G f(x) \overline{\chi(x)} \, d\mu_G(x)$.
      - Plancherel theorem: $\mathcal{F}$ extends to a unitary isomorphism $L^2(G) \xrightarrow{\sim} L^2(\widehat{G})$.
      - Poisson summation formula: for discrete cocompact $\Gamma \subset G$, $\sum_{\gamma \in \Gamma} f(\gamma) = \operatorname{Vol}(G/\Gamma)^{-1} \sum_{\chi \in \Gamma^\perp} \widehat{f}(\chi)$.

  * **Cartier duality on finite commutative group schemes and Hopf algebras:**
    * Let $S$ be a base scheme. Let $\mathbf{FinCommGrp}_S$ be the category of finite locally free commutative group schemes over $S$.
    * **Functor of points definition:** The **Cartier dual** $D(G)$ (or $G^\vee$) represents the functor:
      $$
      D(G)(T) \;\coloneqq\; \operatorname{Hom}_{T\mathbf{-Grp}}(G \times_S T, \mathbb{G}_{m, T})
      $$
      for any $S$-scheme $T$, where $\mathbb{G}_m \coloneqq \operatorname{Spec}(\mathcal{O}_S[t, t^{-1}])$ is the multiplicative group scheme.
    * **Hopf algebra formulation over a commutative ring $k$:**
      - An affine group scheme $G = \operatorname{Spec}(A)$ is finite locally free and commutative if and only if $A$ is a finite locally free $k$-algebra endowed with the structure of a commutative, cocommutative Hopf algebra:
        * Multiplication $m \colon A \otimes_k A \to A$, unit $\eta \colon k \to A$.
        * Comultiplication $\Delta \colon A \to A \otimes_k A$, counit $\epsilon \colon A \to k$.
        * Antipode $S \colon A \to A$.
      - The Cartier dual is $D(G) \coloneqq \operatorname{Spec}(A^*)$, where $A^* \coloneqq \operatorname{Hom}_k(A, k)$ is the $k$-linear dual:
        * Product on $A^*$: $m_{A^*} = \Delta^*$ (dual of comultiplication).
        * Coproduct on $A^*$: $\Delta_{A^*} = m^*$ (dual of multiplication).
        * Unit on $A^*$: $\eta_{A^*} = \epsilon^*$.
        * Counit on $A^*$: $\epsilon_{A^*} = \eta^*$.
        * Antipode on $A^*$: $S_{A^*} = S^*$.
      - Since $A$ is commutative and cocommutative, $A^*$ is also commutative and cocommutative, defining a finite commutative group scheme of the same rank $\operatorname{rk}_k(A^*) = \operatorname{rk}_k(A)$.
    * **Cartier Duality Theorem:**
      - The canonical biduality homomorphism $G \to D(D(G))$ is an isomorphism.
      - Cartier duality gives a contravariant anti-equivalence:
        $$
        D \colon \mathbf{FinCommGrp}_S^{\mathrm{op}} \xrightarrow{\sim} \mathbf{FinCommGrp}_S, \qquad D \circ D \cong \operatorname{id}.
        $$
      - Preserves rank: $[D(G) : S] = [G : S]$.
      - Short exact sequences dualize: $0 \to G' \to G \to G'' \to 0 \implies 0 \to D(G'') \to D(G) \to D(G') \to 0$.
    * **Fundamental dual pairs over a field $k$:**
      1. **Constant group schemes $\longleftrightarrow$ Roots of unity:**
         $$
         D\big((\mathbb{Z}/n\mathbb{Z})_k\big) \;\cong\; \mu_{n, k} \;\coloneqq\; \operatorname{Spec}\big(k[t]/(t^n - 1)\big).
         $$
         - When $\operatorname{char}(k) \nmid n$ and $k$ contains all $n$-th roots of unity, $(\mathbb{Z}/n)_k \cong \mu_{n, k}$.
         - In $\operatorname{char}(k) = p > 0$: $\mu_p = \operatorname{Spec}(k[t]/(t^p - 1)) \cong \operatorname{Spec}(k[u]/(u^p))$ ($u = t - 1$) is non-reduced and local/connected, while $(\mathbb{Z}/p)_k$ is reduced and étale.
      2. **The infinitesimal group $\alpha_p$:**
         - In characteristic $p > 0$: $\alpha_p \coloneqq \operatorname{Spec}(k[x]/(x^p))$ with additive coproduct $\Delta(x) = x \otimes 1 + 1 \otimes x$.
         - **Self-duality:** $D(\alpha_p) \cong \alpha_p$.
    * **Classification of finite $p$-group schemes (Oort-Tate / connected-étale decomposition):**
      - Over a perfect field $k$ of characteristic $p$, every finite commutative $p$-group scheme has a canonical connected-étale composition:
        $$
        0 \to G^0 \to G \to G^{\mathrm{et}} \to 0.
        $$
      - Combining $G$ and $D(G)$ yields four distinct Oort-Tate types:
        - **étale-étale:** $G$ and $D(G)$ are both étale (order coprime to $p$, or Galois modules).
        - **étale-local:** $G$ étale, $D(G)$ connected (e.g., $\mathbb{Z}/p\mathbb{Z}$, with dual $\mu_p$).
        - **local-étale:** $G$ connected, $D(G)$ étale (e.g., $\mu_p$, with dual $\mathbb{Z}/p\mathbb{Z}$).
        - **local-local:** both $G$ and $D(G)$ connected (e.g., $\alpha_p$).
    * **Frobenius and Verschiebung exchange:**
      - Relative Frobenius $F \colon G \to G^{(p)}$ and Verschiebung $V \colon G^{(p)} \to G$.
      - Cartier duality exchanges $F$ and $V$:
        $$
        D(F_G) \;=\; V_{D(G)}, \qquad D(V_G) \;=\; F_{D(G)}.
        $$
      - $G$ is étale $\iff F_G$ is an isomorphism $\iff V_{D(G)}$ is an isomorphism $\iff D(G)$ is of multiplicative type.
    * **Dieudonné module duality:**
      - Under the contravariant Dieudonné module equivalence $\mathbb{M}$ over a perfect field of characteristic $p$:
        $$
        \mathbb{M}(D(G)) \;\cong\; \operatorname{Ext}^1_W(\mathbb{M}(G), W) \;\cong\; \mathbb{M}(G)^*,
        $$
        with operators swapped: $F_{\mathbb{M}(D(G))} = V_{\mathbb{M}(G)}^*$ and $V_{\mathbb{M}(D(G))} = F_{\mathbb{M}(G)}^*$.
    * **Abelian varieties and the Weil pairing:**
      - For an abelian variety $A$ over $k$ and its dual abelian variety $A^\vee = \operatorname{Pic}^0(A)$:
        The $n$-torsion subgroup scheme $A[n]$ has Cartier dual canonically isomorphic to $A^\vee[n]$:
        $$
        D(A[n]) \;\cong\; A^\vee[n].
        $$
      - The canonical Cartier pairing
        $$
        e_n \colon A[n] \times A^\vee[n] \longrightarrow \mathbb{G}_m
        $$
        factors through $\mu_n$ and is the **Weil pairing**.
      - For a principal polarization $\lambda \colon A \xrightarrow{\sim} A^\vee$, the induced pairing $e_n \colon A[n] \times A[n] \to \mu_n$ is alternating and non-degenerate.
    * **Barsotti-Tate ($p$-divisible) groups and Serre-Tate duality:**
      - A $p$-divisible group $G = \varinjlim G[p^\nu]$ has Cartier dual $G^\vee \coloneqq \varinjlim D(G[p^\nu])$.
      - Invariants: $\operatorname{ht}(G^\vee) = \operatorname{ht}(G)$, $\dim(G^\vee) = \operatorname{ht}(G) - \dim(G)$.

  * **Comparison and bridge between Pontryagin and Cartier dualities:**
    - For a finite abstract abelian group $G$, the constant group scheme $G_\mathbb{C}$ over $\mathbb{C}$ has Cartier dual:
      $$
      D(G_\mathbb{C}) \;\cong\; \underline{\operatorname{Hom}}(G, \mathbb{G}_{m, \mathbb{C}}) \;\cong\; \operatorname{Spec}\big(\mathbb{C}[G]^*\big) \;\cong\; (\widehat{G})_\mathbb{C}.
      $$
      Thus over $\mathbb{C}$, Cartier duality on finite group schemes coincides with classical Pontryagin duality.
    - In arithmetic geometry and positive characteristic, Cartier duality refines Pontryagin duality by retaining infinitesimal (nilpotent) coordinate structures ($\mu_p \not\cong \mathbb{Z}/p\mathbb{Z}$, $\alpha_p$).

* **Preamble implementation requirements:**
  * `categories/topology/pontryagin.py`:
    - `LCAGroup(G)`: object in $\mathbf{LCA}$ with topology and group operations.
    - `CharacterGroup(G)`: constructs Pontryagin dual $\widehat{G} = \operatorname{Hom}_{\mathbf{LCA}}(G, \mathbb{T})$ with compact-open topology.
    - `EvaluationMap(G)`: certifies topological isomorphism $\alpha_G \colon G \xrightarrow{\sim} \widehat{\widehat{G}}$.
    - `Annihilator(G, H)`: computes closed subgroup $H^\perp \le \widehat{G}$ for $H \le G$.
    - `DualHomomorphism(f)`: computes $\widehat{f} \colon \widehat{H} \to \widehat{G}$ for $f \colon G \to H$.
    - `StandardDuals`: canonical duals for $\mathbb{Z}$, $\mathbb{T}$, $\mathbb{R}$, $\mathbb{Z}/n\mathbb{Z}$, $\mathbb{Q}_p$, and finite abelian groups.
    - `HaarMeasure(G)` and `FourierTransform(f)`: harmonic analysis and Plancherel transform on $L^2(G)$.
  * `categories/schemes/group_schemes/cartier_duality.py`:
    - `FiniteCommutativeGroupScheme(S, A, Delta, epsilon, S_antipode)`: finite flat commutative group scheme over $S$.
    - `CartierDual(G)`: constructs $D(G) = \operatorname{Spec}(A^*)$ with dual Hopf operations $\Delta^*, m^*$.
    - `BidualityIsomorphism(G)`: canonical isomorphism $G \xrightarrow{\sim} D(D(G))$.
    - `CartierPairing(G)`: canonical pairing $G \times_S D(G) \to \mathbb{G}_m$.
    - `connected_etale_type(G)`: classifies $G$ into one of the four Oort-Tate types (étale/connected $\times$ étale/connected).
    - `frobenius_verschiebung_check(G)`: verifies $D(F) = V_{D(G)}$ and $D(V) = F_{D(G)}$.
    - `ConstantGroupScheme(G, k)` and `RootsOfUnity(n, k)`: certifies $D((\mathbb{Z}/n)_k) \cong \mu_{n, k}$.
    - `AlphaP(p, k)`: certifies self-duality $D(\alpha_p) \cong \alpha_p$.
  * `categories/abelian_varieties/weil_pairing.py`:
    - `TorsionSubgroupScheme(A, n)`: represents $A[n]$ as a finite commutative group scheme.
    - `WeilPairing(A, n)`: computes the Cartier duality pairing $A[n] \times A^\vee[n] \to \mu_n$.
  * `categories/schemes/group_schemes/p_divisible.py`:
    - `BarsottiTateGroup(stages)`: inductive system $G = \varinjlim G[p^\nu]$.
    - `SerreTateDual(G)`: dual $p$-divisible group $G^\vee = \varinjlim D(G[p^\nu])$.

Intended owners: `categories/topology/pontryagin.py` (`LCAGroup`, `CharacterGroup`, `PontryaginDual`, `Annihilator`), `categories/schemes/group_schemes/cartier_duality.py` (`FiniteCommutativeGroupScheme`, `CartierDual`, `CartierPairing`, `RootsOfUnity`, `AlphaP`), `categories/algebras/hopf_algebras.py` (`HopfAlgebra`, `DualHopfAlgebra`), `categories/abelian_varieties/weil_pairing.py` (`WeilPairing`, `TorsionSubgroupScheme`), `categories/schemes/group_schemes/p_divisible.py` (`BarsottiTateGroup`, `SerreTateDual`).

## Desired capability: Operationalized Grothendieck spectral sequences and concrete specializations — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **The abstract Grothendieck spectral sequence (composition of derived functors):**
    * Let $\mathcal{A}, \mathcal{B}, \mathcal{C}$ be abelian categories.
    * Let $G \colon \mathcal{A} \to \mathcal{B}$ and $F \colon \mathcal{B} \to \mathcal{C}$ be additive functors.
    * **Right-derived (cohomological) hypotheses:**
      - $\mathcal{A}$ and $\mathcal{B}$ have enough injectives.
      - $G$ sends injective objects of $\mathcal{A}$ to $F$-acyclic objects of $\mathcal{B}$ (i.e. $(R^q F)(G(I)) = 0$ for all $q > 0$ whenever $I \in \operatorname{Inj}(\mathcal{A})$).
    * **The Grothendieck Spectral Sequence Theorem:**
      For any object $A \in \mathcal{A}$, there is a first-quadrant cohomological spectral sequence:
      $$
      E_2^{p, q} \;=\; (R^p F)\big(R^q G(A)\big) \;\Longrightarrow\; R^{p+q}(F \circ G)(A).
      $$
      Differentials on page $r \ge 2$:
      $$
      d_r \colon E_r^{p, q} \longrightarrow E_r^{p+r, q-r+1}, \quad d_r \circ d_r = 0.
      $$
      Page transitions: $E_{r+1}^{p, q} = \ker(d_r^{p, q}) / \operatorname{im}(d_r^{p-r, q+r-1})$.
    * **Left-derived (homological) hypotheses & variant:**
      - $\mathcal{A}$ and $\mathcal{B}$ have enough projectives; $G$ and $F$ are right exact.
      - $G$ sends projective objects of $\mathcal{A}$ to $F$-acyclic objects of $\mathcal{B}$ (i.e. $(L_q F)(G(P)) = 0$ for all $q > 0$ whenever $P \in \operatorname{Proj}(\mathcal{A})$).
      - Yields the homological spectral sequence:
        $$
        E^2_{p, q} \;=\; (L_p F)\big(L_q G(A)\big) \;\Longrightarrow\; L_{p+q}(F \circ G)(A),
        $$
        with differentials $d^r \colon E^r_{p, q} \to E^r_{p-r, q+r-1}$.
    * **Cartan-Eilenberg double complex construction:**
      - Choose an injective resolution $A \to I^\bullet$ in $\mathcal{A}$.
      - Applying $G$ produces a complex $G(I^\bullet)$ in $\mathcal{B}$.
      - Choose a Cartan-Eilenberg injective resolution $I^{\bullet, \bullet}$ of $G(I^\bullet)$ in $\mathcal{B}$ (resolving objects, boundaries, and cohomologies by injectives).
      - Applying $F$ yields a double complex $K^{p, q} = F(I^{p, q})$.
      - Vertical filtration $'F$ produces $'E_1^{p, q} = R^q F(G(I^p)) = 0$ for $q > 0$ by the acyclicity hypothesis, so $'E_2^{p, 0} = R^p(F \circ G)(A)$ and the spectral sequence degenerates at $'E_2$.
      - Horizontal filtration $''F$ produces $''E_2^{p, q} = R^p F(R^q G(A))$.
      - Since both filtrations converge to the cohomology of the total complex $\operatorname{Tot}(K)$, $''E_r^{p, q} \implies R^{p+q}(F \circ G)(A)$.
    * **Low-degree terms and the five-term exact sequence:**
      - Every first-quadrant spectral sequence induces an exact sequence of low-degree terms:
        $$
        0 \longrightarrow R^1 F(G(A)) \longrightarrow R^1(F \circ G)(A) \longrightarrow F(R^1 G(A)) \xrightarrow{d_2^{0, 1}} R^2 F(G(A)) \longrightarrow R^2(F \circ G)(A),
        $$
        associated with edge homomorphisms:
        * Inflation / Inclusion: $E_2^{1, 0} = R^1 F(G(A)) \hookrightarrow H^1$.
        * Restriction / Projection: $H^1 \twoheadrightarrow E_\infty^{0, 1} \subseteq E_2^{0, 1} = F(R^1 G(A))$.
        * Transgression / Connecting map: $d_2^{0, 1} \colon E_2^{0, 1} \to E_2^{2, 0}$.

  * **Catalogue of concrete specializations from the literature:**
    1. **Leray spectral sequence (sheaf cohomology under continuous or scheme maps):**
       - Map: $f \colon X \to Y$ (continuous map of topological spaces or morphism of schemes).
       - Functors: $G = f_* \colon \mathbf{Sh}(X) \to \mathbf{Sh}(Y)$ (direct image / pushforward) and $F = \Gamma(Y, -) \colon \mathbf{Sh}(Y) \to \mathbf{Ab}$ (global sections).
       - Composition: $F \circ G = \Gamma(Y, f_*(-)) = \Gamma(X, -)$.
       - Acyclicity: injective sheaves are flasque; pushforwards of flasque sheaves are flasque; flasque sheaves on $Y$ are $\Gamma(Y, -)$-acyclic ($H^q(Y, \mathcal{F}) = 0$ for $q > 0$).
       - Grothendieck SS yields:
         $$
         E_2^{p, q} \;=\; H^p(Y, R^q f_* \mathcal{F}) \;\Longrightarrow\; H^{p+q}(X, \mathcal{F}).
         $$
    2. **Serre spectral sequence of a fibration:**
       - Specialization of Leray for a Serre fibration $F \to E \xrightarrow{p} B$:
         The higher direct images $R^q p_* \underline{A}$ form a local coefficient system on $B$ with fiber isomorphic to $H^q(F; A)$.
       - Grothendieck SS yields:
         $$
         E_2^{p, q} \;=\; H^p(B; \mathcal{H}^q(F; A)) \;\Longrightarrow\; H^{p+q}(E; A).
         $$
         When $B$ is simply connected or the monodromy action of $\pi_1(B)$ on $H^*(F; A)$ is trivial, $E_2^{p, q} \cong H^p(B; A) \otimes H^q(F; A)$.
    3. **Local-to-global Ext spectral sequence:**
       - Category: $\mathcal{O}_X\mathbf{-Mod}$ for a ringed space or scheme $X$.
       - Functors: $G = \mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, -) \colon \mathcal{O}_X\mathbf{-Mod} \to \mathcal{O}_X\mathbf{-Mod}$ and $F = \Gamma(X, -) \colon \mathcal{O}_X\mathbf{-Mod} \to \mathbf{Ab}$.
       - Composition: $\Gamma(X, \mathcal{H}om(\mathcal{F}, \mathcal{G})) = \operatorname{Hom}_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$.
       - Acyclicity: injective $\mathcal{O}_X$-modules are flasque, hence $\Gamma(X, -)$-acyclic.
       - Grothendieck SS yields:
         $$
         E_2^{p, q} \;=\; H^p\big(X, \mathcal{E}xt^q_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})\big) \;\Longrightarrow\; \operatorname{Ext}^{p+q}_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G}).
         $$
    4. **Local-to-global Tor spectral sequence (homological):**
       - Functors: $G = \mathcal{F} \otimes_{\mathcal{O}_X} -$, $F = \Gamma(X, -)$.
       - Grothendieck SS yields:
         $$
         E^2_{p, q} \;=\; H_p\big(X, \mathcal{T}or_q^{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})\big) \;\Longrightarrow\; \operatorname{Tor}_{p+q}^{\mathcal{O}_X}(\mathcal{F}, \mathcal{G}).
         $$
    5. **Lyndon-Hochschild-Serre (LHS) spectral sequence (group cohomology):**
       - Group extension: $1 \to N \to G \to Q \to 1$ with $Q = G/N$, and $G$-module $M$.
       - Functors: $G\text{-functor} = (-)^N \colon \mathbb{Z}[G]\mathbf{-Mod} \to \mathbb{Z}[Q]\mathbf{-Mod}$ ($N$-invariants) and $F\text{-functor} = (-)^Q \colon \mathbb{Z}[Q]\mathbf{-Mod} \to \mathbf{Ab}$ ($Q$-invariants).
       - Composition: $((-)^N)^Q = (-)^G$.
       - Acyclicity: an injective $G$-module $I$ is coinduced, its restriction to $N$ is coinduced, and $I^N$ is coinduced as a $Q$-module, hence $H^q(Q, I^N) = 0$ for $q > 0$.
       - Grothendieck SS yields:
         $$
         E_2^{p, q} \;=\; H^p(G/N, H^q(N, M)) \;\Longrightarrow\; H^{p+q}(G, M).
         $$
       - Homology version:
         $$
         E^2_{p, q} \;=\; H_p(G/N, H_q(N, M)) \;\Longrightarrow\; H_{p+q}(G, M).
         $$
       - 5-term exact sequence recovers the classical inflation-restriction sequence:
         $$
         0 \longrightarrow H^1(G/N, M^N) \xrightarrow{\operatorname{inf}} H^1(G, M) \xrightarrow{\operatorname{res}} H^1(N, M)^{G/N} \xrightarrow{d_2^{0, 1}} H^2(G/N, M^N) \xrightarrow{\operatorname{inf}} H^2(G, M).
         $$
    6. **Hochschild-Serre spectral sequence for Lie algebras:**
       - Ideal $\mathfrak{h} \trianglelefteq \mathfrak{g}$ in Lie algebra $\mathfrak{g}$ over a field $k$, representation $M$.
       - Functors: $(-)^{\mathfrak{h}} \colon \mathfrak{g}\mathbf{-Mod} \to (\mathfrak{g}/\mathfrak{h})\mathbf{-Mod}$ and $(-)^{\mathfrak{g}/\mathfrak{h}} \colon (\mathfrak{g}/\mathfrak{h})\mathbf{-Mod} \to k\mathbf{-Mod}$.
       - Grothendieck SS yields:
         $$
         E_2^{p, q} \;=\; H^p(\mathfrak{g}/\mathfrak{h}, H^q(\mathfrak{h}, M)) \;\Longrightarrow\; H^{p+q}(\mathfrak{g}, M).
         $$
    7. **Change of rings spectral sequences (Cartan-Eilenberg):**
       - Ring homomorphism $f \colon R \to S$, $S$-module $N$, $R$-module $M$.
       - Ext variant ($F = \operatorname{Hom}_S(N, -)$, $G = \operatorname{Hom}_R(S, -)$):
         $$
         E_2^{p, q} \;=\; \operatorname{Ext}_S^p(N, \operatorname{Ext}_R^q(S, M)) \;\Longrightarrow\; \operatorname{Ext}_R^{p+q}(N, M).
         $$
       - Tor variant ($F = N \otimes_S -$, $G = S \otimes_R -$):
         $$
         E^2_{p, q} \;=\; \operatorname{Tor}_p^S(N, \operatorname{Tor}_q^R(S, M)) \;\Longrightarrow\; \operatorname{Tor}_{p+q}^R(N, M).
         $$
    8. **Local cohomology spectral sequence:**
       - Closed subschemes $Z \subseteq Y \subseteq X$ and sheaf $\mathcal{F}$.
       - Functors: $\Gamma_Y$ (sections supported on $Y$) and $\Gamma_Z$.
       - Grothendieck SS yields:
         $$
         E_2^{p, q} \;=\; H_Z^p(X, \mathcal{H}_Y^q(\mathcal{F})) \;\Longrightarrow\; H_Z^{p+q}(X, \mathcal{F}).
         $$
    9. **Čech-to-derived functor spectral sequence:**
       - Open cover $\mathcal{U} = \{U_i\}_{i \in I}$ of $X$.
       - Grothendieck SS yields:
         $$
         E_2^{p, q} \;=\; \check{H}^p(\mathcal{U}, \mathcal{H}^q(\mathcal{F})) \;\Longrightarrow\; H^{p+q}(X, \mathcal{F}).
         $$
    10. **Frölicher (Hodge-to-de Rham) spectral sequence:**
        - Hypercohomology of the algebraic de Rham complex $\Omega_X^\bullet$ via horizontal filtration:
          $$
          E_1^{p, q} \;=\; H^q(X, \Omega_X^p) \;\Longrightarrow\; H_{\mathrm{dR}}^{p+q}(X).
          $$
        - Deligne-Illusie theorem: degenerates at $E_1$ for smooth projective varieties over characteristic 0 (or over characteristic $p$ lifting to $W_2(k)$ with $\dim X < p$).
    11. **Hochschild-Serre spectral sequence for étale cohomology:**
        - Scheme $X$ over field $k$, separable closure $k^s$, Galois group $\Gamma = \operatorname{Gal}(k^s/k)$.
        - Grothendieck SS yields:
          $$
          E_2^{p, q} \;=\; H^p\big(\Gamma, H^q(X_{k^s}, \mathcal{F})\big) \;\Longrightarrow\; H_{\mathrm{et}}^{p+q}(X, \mathcal{F}).
          $$

* **Operationalization and effective computation engine:**
  * **Bigraded page data structures and linear algebra:**
    - `SpectralSequence`: manages bigraded components $E_r^{p, q}$ over a ground ring $R$ (fields $\mathbb{Q}, \mathbb{F}_p$ or PID $\mathbb{Z}$).
    - Sparse matrix representation for differentials $d_r^{p, q} \colon E_r^{p, q} \to E_r^{p+r, q-r+1}$.
    - Complex validation: automatically checks $d_r^{p+r, q-r+1} \circ d_r^{p, q} = 0$.
    - Exact homology computation: $E_{r+1}^{p, q} = \ker(d_r^{p, q}) / \operatorname{im}(d_r^{p-r, q+r-1})$ via Smith Normal Form (over $\mathbb{Z}$) or Gaussian elimination (over fields).
  * **Automated differential deduction and inference rules:**
    - **Quadrant and bounding box vanishing:**
      Differentials $d_r^{p, q}$ are automatically asserted to be zero whenever either source $(p, q)$ or target $(p+r, q-r+1)$ lies outside the support window $[p_{\min}, p_{\max}] \times [q_{\min}, q_{\max}]$.
    - **Parity / lacunary sparsity:**
      When $E_2^{p, q} = 0$ for all odd $q$ (e.g. spaces with cohomology concentrated in even degrees, such as $\mathbb{C}\mathbb{P}^n$), $d_2^{p, q} \colon E_2^{p, q} \to E_2^{p+2, q-1}$ must land in an odd row, hence $d_2 = 0$ identically and $E_2 = E_3$. The engine automatically bypasses zero-differential pages.
    - **Five-term exact sequence solver:**
      Given the five-term exact sequence $0 \to E_2^{1, 0} \to H^1 \to E_2^{0, 1} \xrightarrow{d_2} E_2^{2, 0} \to H^2$, the engine inverts ranks or maps to solve for unknown differentials (e.g. computing $d_2^{0, 1}$ from known $H^1$).
    - **Multiplicative Leibniz rule propagation:**
      For spectral sequences with an algebra structure (cup product on Serre, de Rham, or LHS), $d_r$ satisfies the graded derivation law:
      $$
      d_r(u \smile v) \;=\; d_r(u) \smile v \;+\; (-1)^{\operatorname{deg}(u)} u \smile d_r(v).
      $$
      The user provides $d_r$ only on algebra generators; the engine automatically computes $d_r$ on all basis monomials.
    - **Transgression tracker:**
      Identifies transgressive classes $x \in E_2^{0, q}$ where $d_2(x) = \dots = d_q(x) = 0$, giving $d_{q+1}(x) \in E_{q+1}^{q+1, 0}$, connecting fiber cohomology classes directly to base classes.
  * **Convergence and abutment reconstruction:**
    - Detects stability at degree $n$: when all differentials into and out of diagonal $p + q = n$ vanish for $r \ge r_0$, the terms $E_{r_0}^{p, n-p}$ are certified as stable $E_\infty^{p, n-p}$.
    - Target filtration reconstruction: computes filtration quotients $\operatorname{gr}^p H^n \cong E_\infty^{p, n-p}$.
    - Solves extension problems:
      * Over fields $k$: $\dim_k H^n = \sum_{p=0}^n \dim_k E_\infty^{p, n-p}$.
      * Over $\mathbb{Z}$: analyzes extension groups $\operatorname{Ext}^1_\mathbb{Z}(E_\infty^{p, n-p}, E_\infty^{p+1, n-p-1})$ to bound or resolve group extension ambiguities.

* **Preamble implementation requirements:**
  * `categories/homology/spectral_sequences/spectral_sequence.py`:
    - `SpectralSequence(r_start=2, ring=QQ)`: generic first-quadrant spectral sequence engine.
    - `set_term(p, q, module)`: populates $E_{r_{\mathrm{start}}}^{p, q}$.
    - `set_differential(r, p, q, matrix)`: assigns differential $d_r^{p, q}$.
    - `verify_differentials(r)`: verifies $d_r \circ d_r = 0$.
    - `step_page(r)`: computes $E_{r+1}$ homology page.
    - `is_stable(n)`: checks if total degree $n$ has stabilized ($E_\infty$).
    - `abutment(n)`: returns the filtration layers and graded components of $H^n$.
    - `solve_extension(graded_pieces, base_ring)`: reconstructs $H^n$.
  * `categories/homology/spectral_sequences/grothendieck.py`:
    - `GrothendieckSpectralSequence(F, G, A, p_max=4, q_max=4)`: generic Grothendieck spectral sequence constructor.
    - `check_acyclicity(G, F, inj_generator)`: tests $R^q F(G(I)) = 0$ for $q > 0$.
    - `five_term_exact_sequence()`: extracts and solves the 5-term exact sequence.
    - `cartan_eilenberg_double_complex(complex, F, G)`: explicit double complex generation.
  * `categories/homology/spectral_sequences/leray.py`:
    - `LeraySpectralSequence(f, sheaf)`: constructs Leray SS for continuous / scheme maps.
    - `SerreFibrationSpectralSequence(base, fiber, coeff_ring)`: Serre SS with automated cup-product Leibniz propagation.
  * `categories/homology/spectral_sequences/lyndon_hochschild_serre.py`:
    - `LyndonHochschildSerre(G, N, M, mode='cohomology')`: computes $H^p(G/N, H^q(N, M))$ using GAP/Sage group cohomology algorithms.
    - `inflation_restriction_sequence()`: computes 5-term sequence for group extensions.
  * `categories/homology/spectral_sequences/local_ext.py`:
    - `LocalToGlobalExt(F, G, X)`: computes $H^p(X, \mathcal{E}xt^q(\mathcal{F}, \mathcal{G})) \implies \operatorname{Ext}^{p+q}(\mathcal{F}, \mathcal{G})$ on projective schemes via syzygies.
    - `LocalToGlobalTor(F, G, X)`: computes $H_p(X, \mathcal{T}or_q(\mathcal{F}, \mathcal{G})) \implies \operatorname{Tor}_{p+q}(\mathcal{F}, \mathcal{G})$.
  * `categories/homology/spectral_sequences/froelicher.py`:
    - `FroelicherSpectralSequence(X)`: Hodge-to-de Rham spectral sequence $E_1^{p, q} = H^q(X, \Omega_X^p) \implies H_{\mathrm{dR}}^{p+q}(X)$ with Deligne-Illusie degeneration check.

Intended owners: `categories/homology/spectral_sequences/grothendieck.py` (`GrothendieckSpectralSequence`, `CartanEilenbergResolution`), `categories/homology/spectral_sequences/spectral_sequence.py` (`SpectralSequence`, `Page`, `Differential`, `FiveTermSequenceSolver`), `categories/homology/spectral_sequences/leray.py` (`LeraySpectralSequence`, `SerreFibrationSpectralSequence`), `categories/homology/spectral_sequences/lyndon_hochschild_serre.py` (`LyndonHochschildSerre`), `categories/homology/spectral_sequences/local_ext.py` (`LocalToGlobalExt`, `LocalToGlobalTor`), `categories/homology/spectral_sequences/froelicher.py` (`FroelicherSpectralSequence`).

## Desired capability: Operationalized Riemann-Hurwitz formula and ramification theory — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **Unified setting: 1-dimensional regular schemes and Dedekind covers:**
    * Morphism $f \colon X \to Y$ of smooth projective curves over an algebraically closed field $k$, or $\operatorname{Spec} B \to \operatorname{Spec} A$ where $A$ is a Dedekind domain and $B$ is the integral closure of $A$ in a finite separable extension $L/K$ of degree $n = [L : K] = [k(X) : k(Y)]$.
    * For any maximal ideal / closed point $\mathfrak{P}$ lying over $\mathfrak{p} = f(\mathfrak{P})$:
      - **Ramification index:** $e_i = e(\mathfrak{P}_i/\mathfrak{p}) = v_{\mathfrak{P}_i}(f^* t_\mathfrak{p})$, where $\mathfrak{p} B = \prod_{i=1}^g \mathfrak{P}_i^{e_i}$.
      - **Inertia (residue) degree:** $f_i = f(\mathfrak{P}_i/\mathfrak{p}) = [\kappa(\mathfrak{P}_i) : \kappa(\mathfrak{p})] = [B/\mathfrak{P}_i : A/\mathfrak{p}]$.
      - **Fundamental identity:**
        $$
        \sum_{i=1}^g e_i f_i \;=\; n \;=\; [L : K].
        $$
      - **Ramification classification:**
        * **Unramified:** $e_i = 1$ for all $i$, and $\kappa(\mathfrak{P}_i)/\kappa(\mathfrak{p})$ is separable.
        * **Tamely ramified:** $\operatorname{char}(\kappa(\mathfrak{p})) \nmid e_i$ for all $i$, and $\kappa(\mathfrak{P}_i)/\kappa(\mathfrak{p})$ is separable.
        * **Wildly ramified:** $\operatorname{char}(\kappa(\mathfrak{p})) = p > 0$ and $p \mid e_i$ for some $i$.
        * **Totally ramified:** $g = 1$, $f = 1$, $e = n$.
        * **Completely split:** $g = n$, all $e_i = 1, f_i = 1$.
        * **Inert:** $g = 1$, $e = 1$, $f = n$.

  * **Different and discriminant ideals in Dedekind domains and number fields:**
    * **Trace pairing:** Non-degenerate $K$-bilinear form $\operatorname{Tr}_{L/K} \colon L \times L \to K$.
    * **Inverse different (codifferent):**
      $$
      \mathfrak{D}_{B/A}^{-1} \;\coloneqq\; \{ x \in L \mid \operatorname{Tr}_{L/K}(x B) \subseteq A \}.
      $$
      $\mathfrak{D}_{B/A}^{-1}$ is a fractional ideal of $B$ containing $B$.
    * **Different ideal $\mathfrak{D}_{B/A}$:** The integral ideal $\mathfrak{D}_{B/A} \coloneqq (\mathfrak{D}_{B/A}^{-1})^{-1} \subseteq B$:
      $$
      \mathfrak{D}_{B/A} \;=\; \prod_{i=1}^g \mathfrak{P}_i^{d(\mathfrak{P}_i/\mathfrak{p})}.
      $$
      - **Dedekind's Different Theorem:** $\mathfrak{P} \mid \mathfrak{D}_{B/A} \iff e(\mathfrak{P}/\mathfrak{p}) > 1$ (ramification criterion).
      - **Bounds on different exponent $d$:**
        $$
        e - 1 \;\le\; d(\mathfrak{P}/\mathfrak{p}) \;\le\; e - 1 + v_\mathfrak{P}(e).
        $$
        Equality $d(\mathfrak{P}/\mathfrak{p}) = e - 1$ holds if and only if $\mathfrak{P}$ is tamely ramified over $\mathfrak{p}$.
      - **Kähler differentials relation:**
        $$
        \Omega_{B/A}^1 \;\cong\; B / \mathfrak{D}_{B/A}.
        $$
        The different ideal is the 0-th Fitting ideal / annihilator of relative Kähler differentials.
    * **Discriminant ideal $\mathfrak{d}_{B/A}$:** The ideal of $A$ defined by the norm of the different:
      $$
      \mathfrak{d}_{B/A} \;\coloneqq\; N_{B/A}(\mathfrak{D}_{B/A}) \;=\; \prod_\mathfrak{p} \mathfrak{p}^{\sum_i f_i d(\mathfrak{P}_i/\mathfrak{p})}.
      $$
      - **Dedekind's Discriminant Theorem:** A prime $\mathfrak{p} \subset A$ ramifies in $L$ if and only if $\mathfrak{p} \mid \mathfrak{d}_{B/A}$.

  * **Galois ramification filtration and Hilbert's Different Formula:**
    * When $L/K$ is a Galois extension with Galois group $G = \operatorname{Gal}(L/K)$:
      - The primes $\mathfrak{P}_1, \dots, \mathfrak{P}_g$ over $\mathfrak{p}$ are transitively permuted by $G$; all $e_i = e$ and $f_i = f$ are equal, with $e f g = n$.
      - **Decomposition group:** $D_\mathfrak{P} \coloneqq \{ \sigma \in G \mid \sigma(\mathfrak{P}) = \mathfrak{P} \}$, order $|D_\mathfrak{P}| = e f$.
      - **Inertia group:** $I_\mathfrak{P} \coloneqq \{ \sigma \in D_\mathfrak{P} \mid \sigma(x) \equiv x \pmod \mathfrak{P} \text{ for all } x \in B \}$, order $|I_\mathfrak{P}| = e$.
      - **Lower ramification groups:** For integer $i \ge -1$:
        $$
        G_i \;\coloneqq\; \{ \sigma \in D_\mathfrak{P} \mid v_\mathfrak{P}(\sigma(x) - x) \ge i + 1 \text{ for all } x \in B \}.
        $$
        * $G_{-1} = D_\mathfrak{P}$, $G_0 = I_\mathfrak{P}$.
        * $G_1 = P_\mathfrak{P}$ is the unique $p$-Sylow subgroup of $I_\mathfrak{P}$ (wild inertia group).
        * Quotient $G_0/G_1$ is cyclic of order prime to $p$ (tame inertia quotient).
        * Quotients $G_i/G_{i+1}$ for $i \ge 1$ are elementary abelian $p$-groups.
      - **Hilbert's Different Formula:**
        $$
        d(\mathfrak{P}/\mathfrak{p}) \;=\; \sum_{i=0}^\infty (|G_i| - 1) \;=\; (e - 1) \;+\; \sum_{i=1}^\infty (|G_i| - 1).
        $$
        The excess $\sum_{i=1}^\infty (|G_i| - 1)$ is the wild ramification contribution (Artin conductor / Swan conductor).
      - **Herbrand's transition function:**
        $$
        \phi(u) \;=\; \int_0^u \frac{dt}{[G_0 : G_t]},
        $$
        inducing the upper ramification filtration $G^v = G_{\psi(v)}$ ($\psi = \phi^{-1}$), invariant under quotient group passage (fundamental in local class field theory).

  * **The Riemann-Hurwitz formula for curves and Riemann surfaces:**
    * Let $f \colon X \to Y$ be a finite separable morphism of smooth projective curves over an algebraically closed field $k$ (or a branched cover of compact Riemann surfaces) of degree $n$.
    * **Ramification divisor:**
      $$
      R \;\coloneqq\; \sum_{P \in X} d_P \cdot P
      $$
      where $d_P = d(P/f(P))$ is the order of vanishing of the canonical bundle map $f^* \Omega_Y^1 \to \Omega_X^1$.
      - Tame ramification: $d_P = e_P - 1$.
      - Wild ramification: $d_P \ge e_P$ with wild excess computed via Hilbert's formula.
    * **Canonical divisor formula:**
      $$
      K_X \;\sim\; f^* K_Y \;+\; R, \qquad \Omega_X^1 \;\cong\; f^* \Omega_Y^1 \otimes \mathcal{O}_X(R).
      $$
    * **Riemann-Hurwitz genus formula:**
      Taking degrees ($\deg K_X = 2 g_X - 2$ and $\deg f^* K_Y = n(2 g_Y - 2)$):
      $$
      2 g_X - 2 \;=\; n(2 g_Y - 2) \;+\; \deg(R) \;=\; n(2 g_Y - 2) \;+\; \sum_{P \in X} d_P.
      $$
      For tame covers (including all covers in characteristic 0):
      $$
      2 g_X - 2 \;=\; n(2 g_Y - 2) \;+\; \sum_{P \in X} (e_P - 1).
      $$
    * **Topological Euler characteristic (over $\mathbb{C}$):**
      $$
      \chi_{\mathrm{top}}(X) \;=\; n \cdot \chi_{\mathrm{top}}(Y) \;-\; \sum_{P \in X} (e_P - 1).
      $$
    * **Special cases & geometric consequences:**
      - If $f$ is unramified ($\deg R = 0$): $2 g_X - 2 = n(2 g_Y - 2)$. Thus $g_Y = 1 \implies g_X = 1$ (étale covers of elliptic curves are elliptic curves).
      - Lüroth's theorem: if $X = \mathbb{P}^1$ ($g_X = 0$) and $f$ is non-constant, then $g_Y = 0$, so any subfield of $k(t)$ is rational.
      - Hyperelliptic curves ($n = 2, Y = \mathbb{P}^1$): $2 g - 2 = 2(-2) + \sum (2 - 1) = -4 + 2g + 2$, exactly $2g + 2$ branch points (Weierstrass points).

  * **Generalization to higher-dimensional normal varieties:**
    * Let $f \colon X \to Y$ be a finite, surjective morphism of normal integral varieties of dimension $m \ge 1$.
    * **Purity of the branch locus (Zariski-Nagata theorem):**
      If $Y$ is regular and $X$ is normal, the branch locus $B \subset Y$ is either empty or of pure codimension 1!
      Consequently, ramification is completely governed in codimension 1 by the discrete valuation rings $\mathcal{O}_{X, D}$ and $\mathcal{O}_{Y, f(D)}$ associated to prime divisors.
    * **Ramification divisor on varieties:**
      $$
      R \;\coloneqq\; \sum_{D \subset X} d_D \cdot D,
      $$
      summed over all prime divisors $D \subset X$, where $d_D$ is the length of $\Omega_{X/Y}^1$ along the generic point $\eta_D$.
      For tame covers, $d_D = e_D - 1$.
    * **Canonical class formula:**
      $$
      K_X \;\sim\; f^* K_Y \;+\; R.
      $$
    * **Chern classes and cyclic covers:**
      - First Chern class: $c_1(X) = f^* c_1(Y) - [R]$.
      - Cyclic covers: let $D \subset Y$ be a smooth divisor with $D \sim n L$ for some line bundle $L$. The cyclic $n$-fold cover $X \to Y$ branched over $D$ has ramification divisor $R = (n - 1) f^* D_{\mathrm{red}}$, yielding canonical class $K_X \sim f^*(K_Y + (n - 1) L)$.

* **Operationalization and effective computation engine:**
  * **Unified Ramification Datum:**
    - `RamificationDatum`: represents ramification at a prime or point:
      * `prime_up`: $\mathfrak{P}$ or point $P \in X$.
      * `prime_down`: $\mathfrak{p}$ or point $Q \in Y$.
      * `ramification_index`: integer $e \ge 1$.
      * `inertia_degree`: integer $f \ge 1$.
      * `different_exponent`: integer $d \ge e - 1$.
      * `is_tame`: predicate $p \nmid e$ and separable residue.
      * `is_wild`: predicate $p \mid e$.
      * `is_unramified`: predicate $e = 1$ and $d = 0$.
  * **Computational capabilities:**
    1. **Hurwitz Genus & Topology Solver:**
       - Forward evaluation: computes $g_X$ from $g_Y, n$, and branch profile.
       - Inverse Hurwitz solver: determines all admissible integer tuples of ramification indices $(e_1, \dots, e_k)$ and branch orders satisfying $2 g_X - 2 = n(2 g_Y - 2) + \sum (e_i - 1)$ and Riemann surface monodromy conditions.
       - Computes topological Euler characteristics $\chi(X) = n \chi(Y) - \deg(R)$.
    2. **Kummer-Dedekind & Prime Decomposition:**
       - Computes factorization of primes $\mathfrak{p} \mathcal{O}_L = \prod \mathfrak{P}_i^{e_i}$ for number fields $L/\mathbb{Q}$ and function fields $k(C)$.
       - Evaluates residue degrees $f_i$ and certifies the fundamental identity $\sum e_i f_i = n$.
    3. **Different and Discriminant Ideals:**
       - Relative trace matrix computation of codifferent $\mathfrak{D}_{B/A}^{-1} = \{ x \in L \mid \operatorname{Tr}(x B) \subseteq A \}$ and different $\mathfrak{D}_{B/A}$.
       - Relative norm computation of discriminant ideal $\mathfrak{d}_{B/A} = N(\mathfrak{D}_{B/A})$.
       - Verifies Dedekind's criterion: ramification occurs precisely at prime divisors of $\mathfrak{d}_{B/A}$.
    4. **Galois Ramification Filtration Engine:**
       - For Galois number fields or Galois curve covers, computes decomposition groups $D_\mathfrak{P}$, inertia groups $I_\mathfrak{P} = G_0$, and lower ramification subgroups $G_i$ for $i \ge 0$.
       - Evaluates Hilbert's different formula $d = \sum_{i=0}^\infty (|G_i| - 1)$ and separates tame ($e - 1$) from wild excess.
       - Computes Herbrand's function $\phi(u)$ and upper filtration $G^v$.
    5. **Variety Ramification Divisor & Cover Constructor:**
       - Evaluates codimension-1 branch divisors and ramification divisors $R = \sum d_D D$.
       - Computes canonical class $K_X \sim f^* K_Y + R$.
       - Explicit constructions for cyclic covers, double covers ($y^2 = f(x)$), and abelian covers.

* **Preamble implementation requirements:**
  * `categories/algebraic_geometry/hurwitz.py`:
    - `HurwitzFormula(g_Y, n, ramification_data)`: computes genus $g_X$, Euler characteristic $\chi(X)$, and canonical divisor.
    - `HurwitzInverseSolver(g_X, g_Y, n)`: solves for all valid ramification profiles and branch number combinations.
    - `CurveCover(f, X, Y)`: finite morphism of smooth projective curves.
  * `categories/number_theory/ramification.py`:
    - `PrimeRamification(P, p, e, f, d)`: unified data container for prime/place ramification.
    - `DedekindCover(B, A)`: finite extension of Dedekind domains / number fields $\mathcal{O}_L / \mathcal{O}_K$.
    - `different_ideal(B, A)`: computes codifferent $\mathfrak{D}^{-1}$ and different $\mathfrak{D}_{B/A}$.
    - `discriminant_ideal(B, A)`: computes discriminant $\mathfrak{d}_{B/A} = N(\mathfrak{D}_{B/A})$.
    - `verify_fundamental_identity(primes, n)`: asserts $\sum e_i f_i = n$.
  * `categories/galois/ramification_groups.py`:
    - `DecompositionGroup(G, P)`: computes $D_\mathfrak{P} \le G$.
    - `InertiaGroup(G, P)`: computes $I_\mathfrak{P} \le D_\mathfrak{P}$.
    - `LowerRamificationFiltration(G, P)`: computes filtration $G_i$ for $i \ge -1$.
    - `HilbertDifferentFormula(G, P)`: computes $d = \sum (|G_i| - 1)$.
    - `UpperRamificationFiltration(G, P)`: computes Herbrand function $\phi$ and $G^v$.
  * `categories/schemes/ramification_divisor.py`:
    - `RamificationDivisor(f, X, Y)`: evaluates codimension-1 ramification divisor $R$ on normal varieties.
    - `CanonicalClassCover(f, K_Y, R)`: calculates $K_X \sim f^* K_Y + R$.
    - `CyclicCover(Y, D, n)`: constructs cyclic cover $X \to Y$ branched along divisor $D$.

Intended owners: `categories/algebraic_geometry/hurwitz.py` (`HurwitzFormula`, `HurwitzInverseSolver`, `CurveCover`), `categories/number_theory/ramification.py` (`PrimeRamification`, `DedekindCover`, `DifferentIdeal`, `DiscriminantIdeal`), `categories/galois/ramification_groups.py` (`DecompositionGroup`, `InertiaGroup`, `LowerRamificationFiltration`, `HilbertDifferentFormula`), `categories/schemes/ramification_divisor.py` (`RamificationDivisor`, `CanonicalClassCover`, `CyclicCover`).

## Desired capability: Differential graded modules over DG-algebras and graded foundations — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **Graded module and algebra foundations (underlying base categories):**
    * Let $k$ be a commutative base ring.
    * **Graded modules:** Category $\mathbf{GrMod}_k$ of $\mathbb{Z}$-graded $k$-modules $M = \bigoplus_{n \in \mathbb{Z}} M^n$.
    * **Symmetric monoidal structure $(\mathbf{GrMod}_k, \otimes, k)$:**
      - Graded tensor product: $(M \otimes N)^n = \bigoplus_{p+q=n} M^p \otimes_k N^q$.
      - Koszul sign / braiding isomorphism:
        $$
        \tau_{M, N} \colon M \otimes N \xrightarrow{\sim} N \otimes M, \quad \tau(x \otimes y) \;=\; (-1)^{|x||y|} y \otimes x.
        $$
      - Internal Hom: $\underline{\operatorname{Hom}}^n(M, N) = \prod_p \operatorname{Hom}_k(M^p, N^{p+n})$.
    * **Graded algebras:** Monoids in $\mathbf{GrMod}_k$.
      - Associative $k$-algebra $A = \bigoplus_{n \in \mathbb{Z}} A^n$ with $A^p \cdot A^q \subseteq A^{p+q}$ and unit $1 \in A^0$.
      - Graded commutativity: $a \cdot b = (-1)^{|a||b|} b \cdot a$, with $x^2 = 0$ for odd $|x|$ if $2 \neq 0$.
    * **Graded modules over graded algebras:**
      - Left graded module $M = \bigoplus M^n$ with $A^p \cdot M^q \subseteq M^{p+q}$, $(ab)m = a(bm)$, $1m = m$.
      - Homogeneous morphisms of degree $d$: $f(a \cdot m) = (-1)^{d |a|} a \cdot f(m)$.

  * **Differential graded objects (Cochain complexes of $k$-modules):**
    * Category of cochain complexes $\mathbf{Ch}_k$: graded modules with $k$-linear differential $d \colon M^n \to M^{n+1}$ satisfying $d^2 = 0$.
    * Tensor product of complexes: differential on $M \otimes N$:
      $$
      d_{M \otimes N}(x \otimes y) \;=\; d_M(x) \otimes y \;+\; (-1)^{|x|} x \otimes d_N(y).
      $$
    * Internal Hom complex: differential on $\underline{\operatorname{Hom}}(M, N)$:
      $$
      d(f)(x) \;=\; d_N(f(x)) \;-\; (-1)^{|f|} f(d_M(x)) \;=\; [d, f].
      $$
      Cycles $Z^0(\underline{\operatorname{Hom}}(M, N))$ are chain maps; boundaries $B^0$ are null-homotopic maps; cohomology $H^0(\underline{\operatorname{Hom}}(M, N)) = [M, N]$ is the homotopy category of complexes.

  * **Differential Graded Algebras (DGAs):**
    * A DG-algebra $(A, d_A)$ is a monoid in the symmetric monoidal category $(\mathbf{Ch}_k, \otimes)$:
      - Graded associative $k$-algebra $A = \bigoplus_{n \in \mathbb{Z}} A^n$ with unit $1 \in A^0$.
      - Differential $d_A \colon A^n \to A^{n+1}$ with $d_A^2 = 0$ and $d_A(1) = 0$.
      - **Graded Leibniz rule:** For all $a, b \in A$:
        $$
        d_A(a \cdot b) \;=\; d_A(a) \cdot b \;+\; (-1)^{|a|} a \cdot d_A(b).
        $$
    * **Commutative DGAs (CDGAs):** DGAs that are graded commutative: $a \cdot b = (-1)^{|a||b|} b \cdot a$.
      Examples: algebraic de Rham complex $\Omega_X^\bullet$; Koszul complexes $k[x_1, \dots, x_n] \otimes \bigwedge(\theta_1, \dots, \theta_n)$ with $d(\theta_i) = f_i$; Sullivan minimal models in rational homotopy theory.
    * Cohomology $H^*(A) = \bigoplus_n H^n(A)$ is a graded associative $k$-algebra (graded commutative if $A$ is CDGA).

  * **Differential Graded Modules (DG-Modules):**
    * Let $(A, d_A)$ be a DG-algebra.
    * A **left DG-module** over $A$ is a pair $(M, d_M)$ where:
      - $M = \bigoplus_{n \in \mathbb{Z}} M^n$ is a graded left $A$-module.
      - $d_M \colon M^n \to M^{n+1}$ is a $k$-linear differential ($d_M^2 = 0$).
      - **Module Leibniz rule:** For all $a \in A$ and $m \in M$:
        $$
        d_M(a \cdot m) \;=\; d_A(a) \cdot m \;+\; (-1)^{|a|} a \cdot d_M(m).
        $$
    * **Right DG-modules and DG-bimodules:**
      - Right dg-module: $d_M(m \cdot a) = d_M(m) \cdot a + (-1)^{|m|} m \cdot d_A(a)$.
      - $(A, B)$-dg-bimodule: left $A$-dg-module and right $B$-dg-module satisfying $(a \cdot m) \cdot b = a \cdot (m \cdot b)$.
    * **Cohomology module:** $H^*(M) = \bigoplus_n H^n(M)$ is naturally a graded $H^*(A)$-module via $[a] \cdot [m] \coloneqq [a \cdot m]$.

  * **The Category and DG-Category of DG-Modules:**
    * **The abelian category $\mathbf{DGMod}_A$:**
      - Morphisms are chain maps $f \colon M \to N$ of degree 0 commuting strictly with $A$-action: $f(a \cdot m) = a \cdot f(m)$ and $f \circ d_M = d_N \circ f$.
      - $\mathbf{DGMod}_A$ is an abelian Grothendieck category with all limits and colimits.
    * **The DG-category $\underline{\mathbf{DGMod}}_A$:**
      - Internal Hom complex $\underline{\operatorname{Hom}}_A(M, N)^\bullet$:
        $\underline{\operatorname{Hom}}_A^n(M, N)$ is the $k$-module of graded $A$-module maps of degree $n$ (satisfying $f(a \cdot m) = (-1)^{n |a|} a \cdot f(m)$).
        Differential:
        $$
        d(f)(m) \;=\; d_N(f(m)) \;-\; (-1)^{|f|} f(d_M(m)).
        $$
      - 0-cycles: $Z^0(\underline{\operatorname{Hom}}_A(M, N)) = \operatorname{Hom}_{\mathbf{DGMod}_A}(M, N)$.
      - 0-boundaries: null-homotopic morphisms.
      - Homotopy category: $H^0(\underline{\operatorname{Hom}}_A(M, N)) = \operatorname{Hom}_{K(A)}(M, N)$.
    * **Suspensions (Shifts) and Mapping Cones:**
      - Shift $M[k]$: $(M[k])^n = M^{n+k}$, $d_{M[k]} = (-1)^k d_M$, $a \cdot m[k] = (-1)^{k |a|} (a \cdot m)[k]$.
      - Mapping cone $\operatorname{Cone}(f)$ for $f \colon M \to N$: $M[1] \oplus N$ with differential $\begin{pmatrix} -d_M & 0 \\ f & d_N \end{pmatrix}$.

  * **Derived Category $\mathcal{D}(A)$ and Model Category Structures:**
    * **Quasi-isomorphisms:** Morphisms $f \colon M \to N$ inducing isomorphisms on all cohomology groups $H^n(f) \colon H^n(M) \xrightarrow{\sim} H^n(N)$.
    * **Derived category $\mathcal{D}(A)$:**
      $$
      \mathcal{D}(A) \;\coloneqq\; \mathbf{DGMod}_A[\text{q.i.}^{-1}] \;\cong\; K(A) / \mathbf{Ac}(A),
      $$
      where $\mathbf{Ac}(A)$ is the thick subcategory of acyclic dg-modules ($H^*(M) = 0$).
      $\mathcal{D}(A)$ is a triangulated category with translation $[1]$ and triangles from mapping cones.
    * **Projective model structure on $\mathbf{DGMod}_A$:**
      - Weak equivalences: quasi-isomorphisms.
      - Fibrations: degreewise epimorphisms.
      - Cofibrations: retracts of semi-free (cell) dg-modules.
    * **Semi-free (cell / K-projective) DG-modules:**
      - A dg-module $P$ is **semi-free** if it has an exhaustive filtration $0 = P_{-1} \subseteq P_0 \subseteq P_1 \subseteq \dots$ such that $P_k / P_{k-1}$ is a free graded $A$-module generated by a set $S_k$ with $d_P(S_k) \subseteq P_{k-1}$.
      - Every semi-free dg-module is cofibrant: for any quasi-isomorphism $M \xrightarrow{\sim} N$, $\operatorname{Hom}_{K(A)}(P, M) \xrightarrow{\sim} \operatorname{Hom}_{K(A)}(P, N)$.
      - Every dg-module $M$ admits a semi-free resolution $\mathbf{p} M \xrightarrow{\sim} M$.
    * **Semi-injective (K-injective) DG-modules:**
      - Dually, $I$ is semi-injective if $\operatorname{Hom}_{K(A)}(N, I) = 0$ for all acyclic $N$.
      - Every dg-module admits a semi-injective resolution $M \xrightarrow{\sim} \mathbf{i} M$.
    * **Compact and Perfect DG-modules:**
      - $M \in \mathcal{D}(A)$ is compact (small) if $\operatorname{Hom}_{\mathcal{D}(A)}(M, -)$ commutes with arbitrary direct sums.
      - Compact objects form the triangulated subcategory $\operatorname{Perf}(A) \subset \mathcal{D}(A)$ of **perfect dg-modules** (direct summands of finite semi-free dg-modules).

  * **Derived Tensor Products, Derived Hom, Tor, and Ext:**
    * **Derived tensor product:**
      For right dg-module $M$ and left dg-module $N$:
      $$
      M \otimes_A^{\mathbf{L}} N \;\coloneqq\; (\mathbf{p} M) \otimes_A N \;\cong\; M \otimes_A (\mathbf{p} N).
      $$
      Derived Tor: $\operatorname{Tor}_i^A(M, N) \coloneqq H^{-i}(M \otimes_A^{\mathbf{L}} N)$.
    * **Derived Hom:**
      $$
      \mathbf{R}\operatorname{Hom}_A(M, N) \;\coloneqq\; \underline{\operatorname{Hom}}_A(\mathbf{p} M, N) \;\cong\; \underline{\operatorname{Hom}}_A(M, \mathbf{i} N).
      $$
      Ext groups: $\operatorname{Ext}_A^i(M, N) \coloneqq H^i(\mathbf{R}\operatorname{Hom}_A(M, N))$.
    * **Bar resolution of a DG-module:**
      The two-sided bar complex $B(A, A, M)$ provides a canonical, functorial semi-free resolution of $M$ over $A$.

* **Operationalization and effective computation engine:**
  * **Layered representation architecture:**
    1. `GradedModule`: $\mathbb{Z}$-graded vector spaces/modules with degree extraction, graded direct sum, shift $[k]$, and graded tensor product with Koszul signs.
    2. `GradedAlgebra`: graded associative algebra with multiplication table and commutativity checking.
    3. `DGAlgebra`: differential graded algebra $(A, d_A)$ with automated Leibniz verification $d(ab) = d(a)b + (-1)^{|a|} a d(b)$ and differential matrix generators.
    4. `DGModule`: differential graded module $(M, d_M)$ over a DGA with automated module Leibniz verification $d(am) = d(a)m + (-1)^{|a|} a d(m)$.
    5. `DGHomComplex`: internal Hom complex $\underline{\operatorname{Hom}}_A(M, N)$ with differential $[d, f]$.
  * **Computational capabilities:**
    1. **Semi-Free Resolution Generator:**
       - For finitely presented / bounded dg-modules over a DGA, iteratively builds cell filtration $P_0 \subseteq P_1 \subseteq \dots$ to kill cohomology kernels and cokernels, generating minimal semi-free resolutions $\mathbf{p} M \xrightarrow{\sim} M$.
    2. **Derived Hom and Ext Evaluation:**
       - Evaluates $\mathbf{R}\operatorname{Hom}_A(M, N) = \underline{\operatorname{Hom}}_A(\mathbf{p} M, N)$.
       - Computes $\operatorname{Ext}_A^i(M, N)$ as cohomology of the Hom complex via exact linear algebra.
    3. **Derived Tensor and Tor Evaluation:**
       - Computes $M \otimes_A^{\mathbf{L}} N = (\mathbf{p} M) \otimes_A N$.
       - Computes $\operatorname{Tor}_i^A(M, N) = H^{-i}(M \otimes_A^{\mathbf{L}} N)$.
    4. **Cone and Triangle Solver:**
       - Constructs mapping cones $\operatorname{Cone}(f)$ and long exact cohomology sequences $\dots \to H^n(M) \to H^n(N) \to H^n(\operatorname{Cone}(f)) \to H^{n+1}(M) \to \dots$.
    5. **Standard DG-Algebras & Modules Catalogue:**
       - Koszul complexes: $k[x_1, \dots, x_n]$ with exterior variables $\theta_i$ and $d(\theta_i) = f_i(x)$.
       - Matrix factorizations: $\mathbb{Z}/2$-graded dg-modules $(M_0 \oplus M_1, d)$ with $d^2 = W \cdot \operatorname{id}$.
       - De Rham flat modules: flat bundles $(E, \nabla)$ as dg-modules over de Rham CDGA $(\Omega^*(X), d)$.
       - Endomorphism DGAs: $\operatorname{End}_A(M) = \underline{\operatorname{Hom}}_A(M, M)$.

* **Preamble implementation requirements:**
  * `categories/modules/graded_modules.py`:
    - `GradedModule(grades_dict)`: $\mathbb{Z}$-graded $k$-module.
    - `graded_tensor_product(M, N)`: tensor product with Koszul symmetry $\tau(x \otimes y) = (-1)^{|x||y|} y \otimes x$.
    - `graded_shift(M, k)`: suspension $M[k]$.
  * `categories/algebras/dg_algebras.py`:
    - `DGAlgebra(graded_alg, differential_dict)`: differential graded algebra with Leibniz rule certification.
    - `CDGAlgebra(dg_alg)`: commutative differential graded algebra.
    - `KoszulDGA(polynomial_ring, relations)`: Koszul complex DGA.
  * `categories/modules/dg_modules.py`:
    - `DGModule(dga, graded_mod, action_dict, differential_dict)`: left/right DG-module over a DGA with module Leibniz certification.
    - `DGBimodule(left_dga, right_dga, mod, l_action, r_action, diff)`: DG-bimodule.
    - `mapping_cone(f)`: mapping cone of a dg-module morphism.
    - `dg_cohomology(M)`: computes $H^*(M)$ as a graded $H^*(A)$-module.
  * `categories/derived/dg_derived_category.py`:
    - `DGDerivedCategory(dga)`: triangulated derived category $\mathcal{D}(A)$.
    - `semi_free_resolution(M, max_stage=5)`: automated semi-free cofibrant resolution $\mathbf{p} M \xrightarrow{\sim} M$.
    - `derived_hom(M, N)`: computes $\mathbf{R}\operatorname{Hom}_A(M, N)$ and $\operatorname{Ext}_A^i(M, N)$.
    - `derived_tensor_product(M, N)`: computes $M \otimes_A^{\mathbf{L}} N$ and $\operatorname{Tor}_i^A(M, N)$.
    - `is_perfect(M)`: tests whether $M \in \operatorname{Perf}(A)$.
  * `categories/homology/bar_cobar.py`:
    - `BarResolution(A, M)`: canonical two-sided bar resolution $B(A, A, M)$.

Intended owners: `categories/modules/graded_modules.py` (`GradedModule`, `GradedTensor`), `categories/algebras/dg_algebras.py` (`DGAlgebra`, `CDGAlgebra`, `KoszulDGA`), `categories/modules/dg_modules.py` (`DGModule`, `DGBimodule`, `MappingCone`), `categories/derived/dg_derived_category.py` (`DGDerivedCategory`, `SemiFreeResolution`, `DerivedHom`, `DerivedTensor`), `categories/homology/bar_cobar.py` (`BarResolution`).

## Desired capability: Witt vectors, $p$-adics as explicit power series, and ghost vector representations — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **The $p$-typical Witt ring $W(R)$ and truncated rings $W_n(R)$:**
    * Let $R$ be a commutative ring with unit, and $p$ a prime number.
    * The $n$-truncated $p$-typical Witt ring $W_n(R)$ has underlying set $R^n$; the infinite Witt ring $W(R) \coloneqq \varprojlim W_n(R)$ has underlying set $R^{\mathbb{N}}$.
    * Element coordinates (Witt components): $x = (x_0, x_1, x_2, \dots) \in W(R)$.
    * **Ghost map (ghost coordinates):**
      The ghost map $w = (w_0, w_1, w_2, \dots) \colon W(R) \to R^{\mathbb{N}}$ assigns to each Witt vector its ghost components via the universal Witt polynomials:
      $$
      w_n(x_0, \dots, x_n) \;\coloneqq\; \sum_{i=0}^n p^i x_i^{p^{n-i}} \;=\; x_0^{p^n} + p x_1^{p^{n-1}} + p^2 x_2^{p^{n-2}} + \dots + p^n x_n.
      $$
    * **Ghost component ring operations:**
      When $p$ is invertible in $R$ (e.g. $R$ is a $\mathbb{Q}$-algebra), the ghost map $w \colon W(R) \to R^{\mathbb{N}}$ is a ring isomorphism:
      $$
      w_n(x + y) \;=\; w_n(x) + w_n(y), \qquad w_n(x \cdot y) \;=\; w_n(x) \cdot w_n(y).
      $$
    * **Universal Witt polynomials:**
      There exist unique universal polynomials $S_n, P_n \in \mathbb{Z}[X_0, \dots, X_n, Y_0, \dots, Y_n]$ defining ring addition and multiplication on $W(R)$ for any commutative ring $R$:
      $$
      (x + y)_n \;=\; S_n(x_0, \dots, x_n, y_0, \dots, y_n), \qquad (x \cdot y)_n \;=\; P_n(x_0, \dots, x_n, y_0, \dots, y_n).
      $$
      Lowest terms:
      - $S_0(X_0, Y_0) = X_0 + Y_0$.
      - $S_1(X_0, X_1, Y_0, Y_1) = X_1 + Y_1 - \sum_{i=1}^{p-1} \frac{1}{p} \binom{p}{i} X_0^i Y_0^{p-i}$.
      - $P_0(X_0, Y_0) = X_0 Y_0$.
      - $P_1(X_0, X_1, Y_0, Y_1) = X_0^p Y_1 + X_1 Y_0^p + p X_1 Y_1$.
    * **Triangular back-substitution (Ghost inversion):**
      In any torsion-free ring $R$, Witt components are uniquely recovered from ghost components:
      $$
      x_0 = w_0, \qquad x_n \;=\; \frac{1}{p^n} \left( w_n - \sum_{i=0}^{n-1} p^i x_i^{p^{n-i}} \right).
      $$

  * **Witt vectors over perfect fields and $p$-adic integers:**
    * For a perfect field $k$ of characteristic $p > 0$ (such as $\mathbb{F}_p$ or finite field extensions $\mathbb{F}_{p^d}$):
      - $W(k)$ is a complete, Hausdorff discrete valuation ring of characteristic 0, with unique maximal ideal $\mathfrak{m} = p W(k)$ and residue field $W(k)/p W(k) \cong k$.
      - Canonical identification for $k = \mathbb{F}_p$: $W(\mathbb{F}_p) \cong \mathbb{Z}_p$ ($p$-adic integers).
      - For $k = \mathbb{F}_{p^d}$: $W(\mathbb{F}_{p^d}) \cong \mathbb{Z}_{p^d} = \mathcal{O}_{K}$, the ring of integers in the unique unramified extension $K/\mathbb{Q}_p$ of degree $d$.
    * **Teichmüller representative map:**
      $$
      [- ] \colon k \longrightarrow W(k), \quad [a] \;\coloneqq\; (a, 0, 0, \dots).
      $$
      Multiplicative: $[a \cdot b] = [a] \cdot [b]$, and $[a]^p = [a^p]$.
      In ghost coordinates: $w_n([a]) = a^{p^n}$.
    * **$p$-adic expansion via Teichmüller digits:**
      Every element $x \in W(k)$ has a unique, canonical convergent $p$-adic series expansion:
      $$
      x \;=\; \sum_{n=0}^\infty [c_n] p^n, \quad \text{where } c_n = x_n^{p^{-n}} \in k.
      $$
      Conversion to standard base-$p$ digit expansions $a_n \in \{0, \dots, p-1\}$ is performed via Hensel's lemma Newton iteration on $t^{p-1} - 1 = 0$.

  * **Operators and Dieudonné structure:**
    * **Verschiebung (Shift operator):**
      $$
      V \colon W(R) \longrightarrow W(R), \quad V(x_0, x_1, \dots) \;\coloneqq\; (0, x_0, x_1, \dots).
      $$
      Ghost effect: $w(V(x)) = (0, p w_0(x), p w_1(x), \dots)$. $V$ is additive.
    * **Frobenius operator:**
      $$
      F \colon W(R) \longrightarrow W(R), \quad w_n(F(x)) \;=\; w_{n+1}(x).
      $$
      When $\operatorname{char}(R) = p$: $F(x_0, x_1, \dots) = (x_0^p, x_1^p, \dots)$, acting as the Frobenius ring endomorphism.
    * **Operator commutation relations:**
      $$
      F \circ V \;=\; p \cdot \operatorname{id}_{W(R)}, \qquad V(F(x) \cdot y) \;=\; x \cdot V(y), \qquad V(x) \cdot V(y) \;=\; p V(x \cdot y).
      $$
      When $\operatorname{char}(R) = p$, also $V \circ F = p \cdot \operatorname{id}_{W(R)}$.
    * **Dieudonné ring:**
      The non-commutative polynomial ring $\mathbb{D}_k \coloneqq W(k)[F, V] / (FV - p, VF - p, Fa - \sigma(a)F, aV - V\sigma(a))$, where $\sigma$ is the Frobenius automorphism on $W(k)$.

  * **Big Witt vectors $\mathbb{W}(R)$ and formal power series:**
    * Big Witt vectors are indexed by positive integers $n \in \mathbb{Z}_{\ge 1}$: $x = (x_1, x_2, x_3, \dots) \in \mathbb{W}(R)$.
    * Ghost components: $w_n(x) = \sum_{d \mid n} d x_d^{n/d}$.
    * **Universal isomorphism with formal power series:**
      $$
      \Lambda(R) \;\coloneqq\; 1 + t R[[t]]^\times \;\xrightarrow{\sim}\; \mathbb{W}(R), \quad \gamma(x)(t) \;\coloneqq\; \prod_{n=1}^\infty (1 - x_n t^n)^{-1} \;=\; \exp\left( \sum_{n=1}^\infty \frac{w_n(x)}{n} t^n \right).
      $$
      - Addition in $\mathbb{W}(R)$ is power series multiplication: $\gamma(x +_{\mathbb{W}} y)(t) = \gamma(x)(t) \cdot \gamma(y)(t)$.
      - Multiplication in $\mathbb{W}(R)$ is the unique functorial continuous operation satisfying $(1 - a t^n)^{-1} \star (1 - b t^m)^{-1} = (1 - a^{m/d} b^{n/d} t^{nm/d})^{-d}$ with $d = \gcd(n, m)$.
    * **Cartier decomposition:** Over any $\mathbb{Z}_{(p)}$-algebra $R$, the big Witt ring splits into a product of $p$-typical Witt rings:
      $$
      \mathbb{W}(R) \;\cong\; \prod_{k \ge 1, \; p \nmid k} W(R).
      $$

  * **Explicit $p$-adic series and analysis ($\mathbb{Z}_p$ and $\mathbb{Q}_p$):**
    * Representation of $x \in \mathbb{Q}_p$ as formal Laurent power series in $p$:
      $$
      x \;=\; \sum_{n = v_p(x)}^\infty a_n p^n, \quad a_n \in \{0, 1, \dots, p-1\}, \quad a_{v_p(x)} \neq 0.
      $$
    * Non-archimedean valuation $v_p(x) \in \mathbb{Z} \cup \{+\infty\}$, absolute value $|x|_p = p^{-v_p(x)}$.
    * Ultrametric property: $|x + y|_p \le \max(|x|_p, |y|_p)$, with equality whenever $|x|_p \neq |y|_p$.
    * **Artin-Hasse exponential:**
      $$
      E_p(t) \;\coloneqq\; \exp\left( \sum_{n=0}^\infty \frac{t^{p^n}}{p^n} \right) \;\in\; \mathbb{Z}_p[[t]].
      $$
      Has integral $p$-adic coefficients in $\mathbb{Z}_p$ and ghost components $(t, t^p, t^{p^2}, \dots)$.
    * **$p$-adic logarithm and exponential:**
      - $\log_p(1 + x) = \sum_{n=1}^\infty (-1)^{n-1} \frac{x^n}{n}$, convergent for $v_p(x) > 0$.
      - $\exp_p(x) = \sum_{n=0}^\infty \frac{x^n}{n!}$, convergent for $v_p(x) > \frac{1}{p-1}$.

* **Operationalization and effective computation engine:**
  * **Layered representation:**
    1. `WittVector`: exact truncated/infinite $p$-typical vector $(x_0, \dots, x_{n-1})$ over an arbitrary ring $R$.
    2. `GhostVector`: vector of ghost components $(w_0, \dots, w_{n-1}) \in R^n$ with $O(n)$ componentwise ring operations.
    3. `BigWittVector`: elements of $\mathbb{W}_n(R)$ represented as truncated polynomials in $1 + t R[[t]]$.
    4. `PadicSeries`: exact/symbolic $p$-adic number $\sum a_n p^n$ with tracking of precision $O(p^N)$, exact rational reconstruction via lattice reduction / Farey fractions.
  * **Fast and exact algorithmic workflows:**
    1. **Universal Witt Polynomial Generator:**
       - Computes $S_n(X, Y)$ and $P_n(X, Y)$ via ghost coordinates and polynomial interpolation/elimination over $\mathbb{Q}$ and reduction to $\mathbb{Z}$.
       - Caches polynomials $S_n, P_n$ for reusable arithmetic.
    2. **Ghost Vector Round-Trip Engine:**
       - Forward map: $x \mapsto w(x)$ via Horner's evaluation of Witt polynomials.
       - Backward map: $w \mapsto x$ via fast triangular inversion $\frac{1}{p^n}(w_n - \dots)$.
       - Enables exact symbolic multiplication of Witt vectors by transforming to ghost coordinates in characteristic 0 extensions.
    3. **Teichmüller Extraction and Conversion:**
       - Converts between standard $p$-adic digit expansion $a = \sum a_n p^n$ and Teichmüller expansion $a = \sum [\tau_n] p^n$.
       - Implements Hensel's lemma quadratic Newton iteration for Teichmüller lifts in $W(\mathbb{F}_p)$ or $W(\mathbb{F}_{p^d})$.
    4. **Operator Evaluation:**
       - Exact action of Frobenius $F$ and Verschiebung $V$.
       - Dieudonné module linear algebra over $W(k)[F, V]$.
    5. **Artin-Hasse and Formal Group Operations:**
       - Power series expansion of Artin-Hasse exponential $E_p(t)$ and formal group law of $W$.

* **Preamble implementation requirements:**
  * `categories/number_theory/witt_vectors.py`:
    - `WittVector(components, p, ring)`: $p$-typical Witt vector.
    - `witt_addition_polynomial(n, p)`: computes $S_n(X, Y) \in \mathbb{Z}[X, Y]$.
    - `witt_multiplication_polynomial(n, p)`: computes $P_n(X, Y) \in \mathbb{Z}[X, Y]$.
    - `to_ghost(x)`: evaluates ghost vector $w(x)$.
    - `from_ghost(w, p, ring)`: triangular back-substitution from ghost coordinates.
    - `frobenius(x)`: evaluates $F(x)$.
    - `verschiebung(x)`: evaluates $V(x)$.
    - `teichmuller_lift(a, p, precision)`: computes $[a] \in W_n(R)$.
  * `categories/number_theory/big_witt_vectors.py`:
    - `BigWittVector(components, ring)`: universal Witt vectors.
    - `to_power_series(x, precision)`: converts to $1 + t R[[t]]$.
    - `from_power_series(series)`: converts from monic formal power series.
    - `cartier_component(x, p)`: projects to $p$-typical Witt vector.
  * `categories/number_theory/p_adics.py`:
    - `PadicSeries(valuation, digits, p, precision)`: exact $p$-adic number representation.
    - `teichmuller_expansion(x)`: computes $\sum [\tau_n] p^n$.
    - `padic_valuation(x, p)`: computes $v_p(x)$.
    - `artin_hasse_exponential(t, p, precision)`: computes $E_p(t) \in \mathbb{Z}_p[[t]]$.
    - `padic_log(x, precision)`: evaluates $\log_p(x)$.
    - `padic_exp(x, precision)`: evaluates $\exp_p(x)$.
  * `categories/algebraic_geometry/dieudonne.py`:
    - `DieudonneRing(p, k)`: non-commutative ring $W(k)[F, V]$.
    - `DieudonneModule(generators, relations, p, k)`: Dieudonné module over $W(k)$.

Intended owners: `categories/number_theory/witt_vectors.py` (`WittVector`, `GhostVector`, `TeichmullerLift`), `categories/number_theory/big_witt_vectors.py` (`BigWittVector`, `CartierDecomposition`), `categories/number_theory/p_adics.py` (`PadicSeries`, `ArtinHasseExponential`, `PadicLog`, `PadicExp`), `categories/algebraic_geometry/dieudonne.py` (`DieudonneRing`, `DieudonneModule`).

## Desired capability: Operationalized algebraic topology calculational theorems (Hatcher toolkit) — intake 2026-09-19

* **Mathematical background & foundational structures:**
  * **Mayer-Vietoris sequences for homology and cohomology:**
    * Excisive triad $(X; A, B)$ with $X = A \cup B$ (open covers or CW subcomplexes whose union is $X$ and whose intersection is a deformation retract of a neighborhood).
    * **Short exact sequence of chain complexes:**
      $$
      0 \longrightarrow C_n(A \cap B) \xrightarrow{(i_A, -i_B)} C_n(A) \oplus C_n(B) \xrightarrow{j_A + j_B} C_n(A + B) \longrightarrow 0.
      $$
    * **Homology Mayer-Vietoris sequence:**
      $$
      \dots \longrightarrow H_n(A \cap B) \xrightarrow{(i_A_*, -i_B_*)} H_n(A) \oplus H_n(B) \xrightarrow{j_A_* + j_B_*} H_n(X) \xrightarrow{\partial_*} H_{n-1}(A \cap B) \longrightarrow \dots
      $$
      Connecting homomorphism $\partial_* \colon H_n(X) \to H_{n-1}(A \cap B)$ comes from the Snake Lemma: for cycle $\gamma = \alpha + \beta$ ($\alpha \in C_n(A), \beta \in C_n(B)$), $\partial_*[\gamma] = [\partial \alpha] = -[\partial \beta] \in H_{n-1}(A \cap B)$.
    * Reduced homology Mayer-Vietoris: for non-empty $A \cap B$, replaces $H_0$ with $\widetilde{H}_0$, terminating with $\widetilde{H}_0(X) \to 0$.
    * Relative Mayer-Vietoris sequence: for pairs $(X, Y) = (A \cup B, C \cup D)$.
    * **Cohomology Mayer-Vietoris sequence:**
      $$
      \dots \longrightarrow H^{n-1}(A \cap B) \xrightarrow{\delta^*} H^n(X) \longrightarrow H^n(A) \oplus H^n(B) \longrightarrow H^n(A \cap B) \longrightarrow \dots
      $$
      Compatible with cup products.

  * **Universal Coefficient Theorems (UCT):**
    * **UCT for Homology:**
      Let $C_\bullet$ be a chain complex of free abelian groups, and $G$ an abelian group.
      Functorial split short exact sequence:
      $$
      0 \longrightarrow H_n(C) \otimes_\mathbb{Z} G \xrightarrow{\alpha} H_n(C; G) \xrightarrow{\beta} \operatorname{Tor}_1^\mathbb{Z}(H_{n-1}(C), G) \longrightarrow 0.
      $$
      Splitting yields the isomorphism:
      $$
      H_n(C; G) \;\cong\; \big(H_n(C) \otimes_\mathbb{Z} G\big) \;\oplus\; \operatorname{Tor}_1^\mathbb{Z}\big(H_{n-1}(C), G\big).
      $$
      For finitely generated homology $H_n(C) \cong \mathbb{Z}^{b_n} \oplus \bigoplus_i \mathbb{Z}/p_i^{k_i}$:
      - Field coefficients $\mathbb{Q}$: $H_n(X; \mathbb{Q}) \cong \mathbb{Q}^{b_n}$.
      - Finite field coefficients $\mathbb{F}_p$: $H_n(X; \mathbb{F}_p) \cong \mathbb{F}_p^{b_n + t_n(p) + t_{n-1}(p)}$, where $t_k(p)$ is the number of $\mathbb{Z}/p^r$ factors in $H_k(X)$.
    * **UCT for Cohomology:**
      Let $C_\bullet$ be a chain complex of free abelian groups, and $G$ an abelian group.
      Functorial split short exact sequence:
      $$
      0 \longrightarrow \operatorname{Ext}_\mathbb{Z}^1\big(H_{n-1}(C), G\big) \xrightarrow{\delta} H^n(C; G) \xrightarrow{h} \operatorname{Hom}_\mathbb{Z}\big(H_n(C), G\big) \longrightarrow 0.
      $$
      Splitting yields the isomorphism:
      $$
      H^n(C; G) \;\cong\; \operatorname{Hom}_\mathbb{Z}\big(H_n(C), G\big) \;\oplus\; \operatorname{Ext}_\mathbb{Z}^1\big(H_{n-1}(C), G\big).
      $$
      The Kronecker evaluation map $h([\phi])([\alpha]) = \phi(\alpha)$ is surjective with kernel $\operatorname{Ext}^1$.
      For $G = \mathbb{Z}$:
      $$
      H^n(X; \mathbb{Z}) \;\cong\; \operatorname{Free}\big(H_n(X)\big) \;\oplus\; \operatorname{Tors}\big(H_{n-1}(X)\big).
      $$
      Torsion in $H_{n-1}(X)$ shifts by degree $+1$ into $H^n(X)$.

  * **Künneth Formulas for Product Spaces:**
    * **Künneth formula for Homology:**
      For chain complexes $C, C'$ over a PID $R$ with $C$ flat:
      $$
      0 \longrightarrow \bigoplus_{i+j=n} H_i(C) \otimes_R H_j(C') \longrightarrow H_n(C \otimes C') \longrightarrow \bigoplus_{i+j=n-1} \operatorname{Tor}_1^R\big(H_i(C), H_j(C')\big) \longrightarrow 0.
      $$
      For product topological spaces $X \times Y$:
      $$
      H_n(X \times Y; R) \;\cong\; \bigoplus_{p+q=n} \big(H_p(X; R) \otimes_R H_q(Y; R)\big) \;\oplus\; \bigoplus_{p+q=n-1} \operatorname{Tor}_1^R\big(H_p(X; R), H_q(Y; R)\big).
      $$
    * **Künneth formula for Cohomology:**
      Cross product $\times \colon H^p(X; R) \otimes_R H^q(Y; R) \to H^{p+q}(X \times Y; R)$.
      Over a field $k$, cross product is an isomorphism of graded rings:
      $$
      H^*(X \times Y; k) \;\cong\; H^*(X; k) \otimes_k H^*(Y; k).
      $$
      Over a PID $R$, split exact sequence with $\operatorname{Ext}_R^1$ terms.

  * **Cellular Homology and CW Complexes:**
    * For a CW complex $X = \bigcup X^n$:
      - Cellular chain complex: $C_n^{\mathrm{CW}}(X) \coloneqq H_n(X^n, X^{n-1}) \cong \mathbb{Z}^{c_n}$, where $c_n$ is the number of $n$-cells $e_\alpha^n$.
      - Cellular boundary map $d_n \colon C_n^{\mathrm{CW}}(X) \to C_{n-1}^{\mathrm{CW}}(X)$:
        Matrix entries $d_{\alpha, \beta} = \deg(\Delta_{\alpha, \beta})$ where $\Delta_{\alpha, \beta} \colon S^{n-1} \xrightarrow{\phi_\alpha} X^{n-1} \twoheadrightarrow S_\beta^{n-1}$ is the attaching map collapsed to the $\beta$-th cell.
      - Homology isomorphism: $H_n^{\mathrm{CW}}(X) \cong H_n(X)$.
      - Euler characteristic theorem: $\chi(X) = \sum_{n} (-1)^n c_n = \sum_n (-1)^n b_n$.

  * **Excision, Pairs, Suspensions, and Wedges:**
    * Long exact sequence of a pair $(X, A)$:
      $$
      \dots \longrightarrow H_n(A) \xrightarrow{i_*} H_n(X) \xrightarrow{j_*} H_n(X, A) \xrightarrow{\partial} H_{n-1}(A) \longrightarrow \dots
      $$
    * Excision theorem: If $Z \subset A \subset X$ with $\bar{Z} \subset \operatorname{int}(A)$, then $(X \setminus Z, A \setminus Z) \hookrightarrow (X, A)$ induces isomorphism $H_n(X \setminus Z, A \setminus Z) \xrightarrow{\sim} H_n(X, A)$.
    * Suspension isomorphism: $\widetilde{H}_{n+1}(\Sigma X) \cong \widetilde{H}_n(X)$ and $\widetilde{H}^{n+1}(\Sigma X) \cong \widetilde{H}^n(X)$.
    * Wedge sum theorem: $\widetilde{H}_n(\bigvee_\alpha X_\alpha) \cong \bigoplus_\alpha \widetilde{H}_n(X_\alpha)$.

  * **Cohomology Rings, Cup and Cap Products, and Poincaré Duality:**
    * Cup product: $\smile \colon H^p(X; R) \times H^q(X; R) \to H^{p+q}(X; R)$.
      Graded commutativity: $\alpha \smile \beta = (-1)^{p q} \beta \smile \alpha$.
    * Cap product: $\frown \colon H_n(X; R) \times H^k(X; R) \to H_{n-k}(X; R)$, satisfying $\psi(\sigma \frown \phi) = (\phi \smile \psi)(\sigma)$.
    * Poincaré Duality: For a closed, $R$-orientable $n$-manifold $M$ with fundamental class $[M] \in H_n(M; R)$:
      $$
      D_M \coloneqq - \frown [M] \colon H^k(M; R) \xrightarrow{\sim} H_{n-k}(M; R)
      $$
      is an isomorphism for all $k$.
    * Intersection pairing: $H^k(M) \times H^{n-k}(M) \to R$, $(\alpha, \beta) \mapsto \langle \alpha \smile \beta, [M] \rangle$.

  * **Fundamental Group, Seifert-van Kampen, and Hurewicz Theorem:**
    * **Seifert-van Kampen Theorem:**
      For $X = A \cup B$ with $A, B, A \cap B$ path-connected and $x_0 \in A \cap B$:
      $$
      \pi_1(X, x_0) \;\cong\; \pi_1(A, x_0) *_{\pi_1(A \cap B, x_0)} \pi_1(B, x_0)
      $$
      (amalgamated free product / pushout in $\mathbf{Grp}$).
    * **Hurewicz Theorem:**
      - Degree 1: For path-connected $X$, the Hurewicz homomorphism $h \colon \pi_1(X, x_0) \to H_1(X; \mathbb{Z})$ induces an isomorphism:
        $$
        \pi_1(X, x_0)^{\mathrm{ab}} \;\cong\; H_1(X; \mathbb{Z}).
        $$
      - Higher degrees: If $X$ is $(n-1)$-connected ($n \ge 2$, so $\pi_i(X) = 0$ for $i < n$):
        $\widetilde{H}_i(X) = 0$ for $i < n$, and $h \colon \pi_n(X) \xrightarrow{\sim} H_n(X; \mathbb{Z})$ is an isomorphism, with $h \colon \pi_{n+1}(X) \twoheadrightarrow H_{n+1}(X)$ surjective.

* **Operationalization and effective computation engine:**
  * **Algorithmic Exact Sequence Solver (`ExactSequenceSolver`):**
    - Solves long exact sequences $\dots \to A_n \xrightarrow{\alpha_n} B_n \xrightarrow{\beta_n} C_n \xrightarrow{\gamma_n} A_{n-1} \to \dots$:
      * Zero propagation: $A_n = 0 \implies \beta_n$ injective; $C_n = 0 \implies \alpha_n$ surjective; $A_n = 0$ and $A_{n-1} = 0 \implies B_n \cong C_n$.
      * Rank / Euler characteristic conservation: $\sum (-1)^i \operatorname{rank}(V_i) = 0$ for exact sequences of free modules / vector spaces.
      * Short exact sequence splitter: detects split extensions when the quotient is free.
      * Boundary map deduction via Smith Normal Form on partial homomorphisms.
  * **Automated UCT Calculator (`UCTCalculator`):**
    - Takes finitely generated homology $H_*(X; \mathbb{Z})$ presented as Betti numbers $b_k$ and torsion lists $[d_1, \dots, d_m]$.
    - Evaluates $H_*(X; G)$ and $H^*(X; G)$ for any $G \in \{\mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{F}_p, \mathbb{Z}/m\mathbb{Z}, \mathbb{Z}\}$.
    - Handles $\operatorname{Tor}_1^\mathbb{Z}$ and $\operatorname{Ext}_\mathbb{Z}^1$ table lookups:
      $\operatorname{Tor}_1(\mathbb{Z}/a, \mathbb{Z}/b) \cong \mathbb{Z}/\gcd(a, b)$, $\operatorname{Ext}^1(\mathbb{Z}/a, \mathbb{Z}/b) \cong \mathbb{Z}/\gcd(a, b)$, $\operatorname{Ext}^1(\mathbb{Z}/a, \mathbb{Z}) \cong \mathbb{Z}/a$.
  * **Künneth Product Engine (`KunnethCalculator`):**
    - Computes homology and cohomology of $X \times Y$ given $H_*(X)$ and $H_*(Y)$.
    - Computes graded cohomology rings $H^*(X \times Y; k) \cong H^*(X; k) \otimes H^*(Y; k)$ with cup product multiplication matrices.
  * **Cellular Complex Homology Engine (`CellularComplex`):**
    - Constructs cellular chain complexes from cell numbers and attaching degree matrices $[d_{\alpha, \beta}]$.
    - Computes homology groups $H_n^{\mathrm{CW}}(X)$ with cycle generators and boundary boundaries.
    - Computes Euler characteristics and Betti numbers.
  * **Seifert-van Kampen Engine (`VanKampenSolver`):**
    - Computes amalgamated free products of finitely presented groups $\langle X_A \mid R_A \rangle *_{\langle X_\cap \mid R_\cap \rangle} \langle X_B \mid R_B \rangle$ via Tietze transformations and abelianization.
  * **Poincaré Duality & Intersection Pairing Engine (`PoincareDuality`):**
    - Verifies orientation and calculates intersection matrix on middle cohomology $H^{n/2}(M)$ for even-dimensional manifolds (signature, type I/II definite/indefinite).

* **Preamble implementation requirements:**
  * `categories/topology/exact_sequence.py`:
    - `LongExactSequence(terms, maps)`: exact sequence data model with automated deduction.
    - `solve_exact_sequence(les)`: infers unknown groups and maps.
  * `categories/topology/mayer_vietoris.py`:
    - `MayerVietoris(A, B, A_cap_B)`: Mayer-Vietoris homology and cohomology solver.
    - `RelativeMayerVietoris(pair_A, pair_B)`: relative Mayer-Vietoris solver.
  * `categories/topology/uct.py`:
    - `UniversalCoefficientHomology(H_Z, G)`: evaluates $H_*(X; G)$.
    - `UniversalCoefficientCohomology(H_Z, G)`: evaluates $H^*(X; G)$.
    - `tor_group(A, B)`: computes $\operatorname{Tor}_1^\mathbb{Z}(A, B)$.
    - `ext_group(A, B)`: computes $\operatorname{Ext}_\mathbb{Z}^1(A, B)$.
  * `categories/topology/kunneth.py`:
    - `KunnethHomology(H_X, H_Y, ring)`: computes $H_*(X \times Y)$.
    - `KunnethCohomologyRing(H_X, H_Y, field)`: computes graded cohomology ring.
  * `categories/topology/cellular.py`:
    - `CWComplex(cells_per_dim, attaching_degrees)`: CW complex model.
    - `cellular_homology()`: computes $H_n^{\mathrm{CW}}(X)$.
    - `euler_characteristic()`: computes $\chi(X)$.
  * `categories/topology/van_kampen.py`:
    - `VanKampen(G_A, G_B, G_cap, phi_A, phi_B)`: amalgamated free product.
    - `hurewicz_abelianization(G)`: computes $\pi_1^{\mathrm{ab}} \cong H_1$.
  * `categories/topology/poincare_duality.py`:
    - `PoincareDuality(M, orientation_class)`: cap product isomorphism $H^k(M) \cong H_{n-k}(M)$.
    - `intersection_form(M)`: intersection pairing on middle cohomology.

Intended owners: `categories/topology/exact_sequence.py` (`LongExactSequence`, `ExactSequenceSolver`), `categories/topology/mayer_vietoris.py` (`MayerVietoris`), `categories/topology/uct.py` (`UniversalCoefficientHomology`, `UniversalCoefficientCohomology`), `categories/topology/kunneth.py` (`KunnethHomology`, `KunnethCohomologyRing`), `categories/topology/cellular.py` (`CWComplex`), `categories/topology/van_kampen.py` (`VanKampen`, `Hurewicz`), `categories/topology/poincare_duality.py` (`PoincareDuality`, `IntersectionForm`).
























