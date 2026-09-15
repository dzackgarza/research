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

## Leads

| Lead | Source | Capability | Intended owner | Status |
| --- | --- | --- | --- | --- |
| *Example: toric divisor cohomology* | `computations/...` | *What mathematics it computes* | `categories/schemes/...` | Proposed |
| CAP monodromy — rigorous PF transport | https://github.com/taklab-org/CAP_finding_monodromy | Rigorous monodromy of regular-singular Pfaffian system via series enclosure + validated ODE transport | `categories/schemes/monodromy.py` / flat connections / D-modules; `categories/functors/local_system.py` | Proposed — see intake report below |
| Families via f.as_family + periods / PF | User note 2026-09-15 | Scheme morphism as family; period `w(z)=∫_{γ_z}Ω_z` and its Picard-Fuchs equation `PF(w)` | `categories/schemes/families.py` via `Hom(Sch/C)` + `categories/schemes/periods.py` / Gauss-Manin | Proposed — see note below |
| Generatingfunctionology (Wilf Ch.1-2) | User note 2026-09-15 | Symbolic recurrences, exact solutions, OGF/EGF, L-functions / zeta | `categories/generating_functions/` + `categories/rings/formal_power_series.py` / `D-Mod` | Proposed — see note below |
| Monodromy groups/reps + π1/H1 + CW + graded | User note 2026-09-15 | Semantic `π1(X,x)`, `H1^sing`, monodromy groups/reps; CW complexes with sphere homotopy DB; `ZZ^n`-graded complexes / spectral sequences | `categories/topology/` / `categories/homotopy/` + `categories/graded/` | Proposed — see note below |
| Periods (Lairez) — creative telescoping | https://github.com/lairez/periods | Periods of rational integrals: Picard-Fuchs operators via Griffiths-Dwork / Rham-Koszul | `categories/schemes/periods.py` / `categories/Dmodules/` + `categories/rings/completions.py` | Proposed — see intake below |

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
