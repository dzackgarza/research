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

