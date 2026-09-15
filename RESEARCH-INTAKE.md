# Research Intake

Leads for research code whose capabilities belong in the preamble.

Each entry names existing research code that provides mathematical capability not yet owned by the preamble.
The preamble absorbs each capability through its owned category, object, morphism, and functor structure, with maintained computation behind a private adapter.
Do not import the research code directly and do not reimplement its algorithm locally.
Use the intake to select the correct owner, trace the required construction, and link the resulting TODO item and complaint where applicable.

Add a lead with source location, mathematical capability, intended preamble owner, and current status.
Remove a lead when the preamble owns the capability and specimens prove it, with evidence in the delivery commit.

## Leads

| Lead | Source | Capability | Intended owner | Status |
| --- | --- | --- | --- | --- |
| *Example: toric divisor cohomology* | `computations/...` | *What mathematics it computes* | `categories/schemes/...` | Proposed |
| CAP monodromy — rigorous PF transport | https://github.com/taklab-org/CAP_finding_monodromy | Rigorous monodromy of regular-singular Pfaffian system via series enclosure + validated ODE transport | `categories/schemes/monodromy.py` / flat connections / D-modules; `categories/functors/local_system.py` | Proposed — see intake report below |
| Families via f.as_family + periods / PF | User note 2026-09-15 | Scheme morphism as family; period `w(z)=∫_{γ_z}Ω_z` and its Picard-Fuchs equation `PF(w)` | `categories/schemes/families.py` via `Hom(Sch/C)` + `categories/schemes/periods.py` / Gauss-Manin | Proposed — see note below |

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
