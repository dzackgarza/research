# Sterk root-count discrepancy: computed Vinberg fundamental domains vs Sterk's published simple-root counts

Status: open research question (not a migration or software defect). Recorded 2026-08-20 from the in-tree computation in `computations/scripts/init.sage`.

## The discrepancy

For each of the five Sterk cusps of the Enriques period space, the in-tree Vinberg-algorithm computations return **9 or 10 simple roots with 1–2 ideal vertices**, where Sterk's published fundamental-domain counts are **12, 10, 12, 11, 14**.

Reference, as the corpus cites it (`writing/NewCoble/coble_research_report/coble_references.bib`, key `Sterk91`; also cited as `Ste91` in the Research Statement and `@n` in the Coble monograph sources):

> Sterk, Hans. *Compactifications of the Period Space of Enriques Surfaces I*. Mathematische Zeitschrift **207** (1991), no. 1, 1–36.

Per-cusp comparison (published breakdowns as transcribed in the in-tree comments, `init.sage` lines 722–860):

| Cusp | Sterk (published) | Julia (Vinberg.jl) | VinAl |
| --- | --- | --- | --- |
| Sterk 1 | 12 roots: 12× norm −4 | 9 roots (10 s) | 10 roots + 1 ideal vertex (10 s) |
| Sterk 2 | 10 roots: 9× −4, 1× −2 | 10 roots (2 s) | 10 roots + 2 ideal vertices (5 s) — source comment: "Almost exactly matches Sterk." |
| Sterk 3 | 12 roots: 10× −4, 2× −2 | 10 roots (20 s) | 10 roots + 2 ideal vertices (10 s) |
| Sterk 4 | 11 roots: 9× −4, 2× −2 | 10 roots (20 s) | 10 roots + 2 ideal vertices (5 s) |
| Sterk 5 | 14 roots: 10× −4, 4× −2 | 10 roots (2 s) | 10 roots + 2 ideal vertices (5 s) |

## Working hypothesis (the user's mathematical frame)

The two counts measure **different group actions**. The computation takes orbits under the **full reflection group** of the abstract Coxeter group of the lattice $e^\perp/e$, while Sterk's paper implicitly works under a **smaller group — a reflection subgroup of $W(e^\perp/e)$**. A fundamental domain for the smaller group is a union of chambers of the full group, so its wall (simple-root) count is at least the full-group count, matching the observed direction of the discrepancy (published counts ≥ computed counts). This is stated as a hypothesis, not a verified reconciliation: no in-tree computation identifies the subgroup or exhibits the chamber decomposition.

## The computation

All data lives in `computations/scripts/init.sage`.

- **Ambient lattice**: `TEn = U ⊕ E10(2)` (basis `e, f, ep, fp, a1..a8`), lines 322–349.
- **The five cusps** are the isotropic vectors `TEn.isotropic_vectors_Sterk = [e, ep, ep+fp+ω, ep+2fp+α, 2e+2f+α]` with `ω = 2·w8`, `α = 2·w1` in the dual basis (lines 337–349).
- **The rank-10 quotients** `Sterk_j = e_perp_mod_e(v_j)` (lines 356–363). Per the in-tree isometry tests: `Sterk_1 ≅ U(2) ⊕ E8(2) = E10(2)` (two-elementary type $(10,10,0)$); `Sterk_2..5 ≅ U ⊕ E8(2)` (type $(10,8,0)$).
- **The Vinberg runs** use `vinal` (loaded from `~/gitclones/vinal/src/sage`, lines 9–10; wrapper at lines 40–42 calls `VinAl(gram, v0).FindRoots()`) and a Julia implementation ("Julia" in the comments). Each root below is a 10-tuple of coordinates in the recorded basis of the respective rank-10 lattice.
- **Sterk's own root sets, hand-entered from the paper**, are also in-tree for comparison: `Sterk_roots["Sterk_1".."Sterk_5"]` built inside the $(20,2,0)$ model `L_20_2_0 = U ⊕ U(2) ⊕ E8²` (lines 487–581), and direct `sterks1..sterks5` vectors in `TEn` coordinates (lines 585–680). These realize the published counts 12, 10, 12, 11, 14.

## Computed root sets (verbatim from `init.sage` lines 720–860)

```python
##### [12, 10, 12, 11, 14] ##################

# Sterk 1 roots: 9 (10s Julia). Sterk had 12: 12x -4 roots
Sterk1_Julia = [
[0,0,-1,-1,-2,-3,-2,-2,-2,-1],
[0,0,2,2,3,4,3,2,1,1],
[0,0,0,1,0,1,1,1,1,1],
[0,0,1,1,1,2,2,1,1,0],
[0,0,-1,-1,-1,-1,-1,0,0,0],
[0,0,1,2,3,4,3,2,1,0],
[0,0,-1,-2,-2,-4,-3,-2,-1,0],
[0,0,0,0,0,0,-1,-1,0,0],
[1,0,0,-1,-1,-2,-2,-1,-1,-1]
]

# Sterk 1 roots: 10 (10s VinAl) 1 ideal vertex
Sterk1_vinal = [
(0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
(0, 0, 0, -1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, -1, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
(0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
(0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
(1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
(0, 1, 2, 3, 4, 6, 5, 4, 3, 2)
 ]

# Sterk 2 roots: 10 (2s Julia). Sterk had 10: 9x -4 roots, 1x -2 root
Sterk2_julia = [
[0,0,1,2,3,4,3,2,1,1],
[0,0,-1,-1,-2,-2,-1,-1,-1,-1],
[0,0,1,1,2,3,2,2,1,0],
[0,0,0,-1,-1,-2,-2,-2,-1,-1],
[0,0,-1,-1,-2,-3,-3,-2,-1,0],
[0,0,-2,-3,-3,-5,-4,-3,-2,-1],
[0,0,2,2,3,4,4,3,2,1],
[0,0,0,1,1,2,2,2,2,1],
[-1,1,0,0,0,0,0,0,0,0],
[2,0,0,-1,-1,-1,-1,-1,-1,0]
]

# Sterk 2 roots: 10 (5s VinAl) 2 ideal vertices
Sterk2_vinal = [
(0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
(0, 0, 0, -1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, -1, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
(0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
(0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
(1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
(0, 2, 2, 3, 4, 6, 5, 4, 3, 2)
 ]
# Almost exactly matches Sterk.

# Sterk 3: 10 (20s Julia). Sterk had 12: 10x -4 roots, 2x -2 roots
Sterk3_julia = [
[0,0,-1,0,1,1,1,2,2,2],
[0,0,0,1,-1,-2,-2,-3,-2,-2],
[0,0,-1,0,1,2,2,3,2,1],
[0,0,1,1,-1,-2,-2,-3,-3,-2],
[0,0,-1,-1,0,1,1,2,2,2],
[0,0,1,1,-1,-2,-3,-5,-4,-3],
[0,0,1,0,-1,0,-1,-1,-1,-1],
[0,0,0,-1,1,1,2,2,2,1],
[-1,1,0,0,0,0,0,0,0,0],
[2,0,0,-1,1,1,1,2,1,1]
]

# Sterk 3: 10 (10s VinAl) 2 ideal vertices
Sterk3_vinal = [
(0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, -1, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
(0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
(0, 0, 0, 1, 0, 0, 0, 0, 0, -1),
(0, 0, 1, -1, 0, 0, 0, 0, 0, 0),
(1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
(0, 2, -1, -1, 2, 3, 4, 6, 5, 4)
]

# Sterk 4: 10 (20s Julia). Sterk had 11: 9x -4 roots, 2x -2 roots
Sterk4_julia = [
[0,0,0,0,-1,0,-1,-1,-1,-1],
[0,0,2,3,-8,-4,-17,-14,-11,-7],
[0,0,-1,-2,5,2,10,8,6,4],
[0,0,2,4,-11,-5,-22,-18,-13,-9],
[0,0,-2,-4,11,5,22,18,14,10],
[0,0,0,2,-2,-1,-4,-3,-3,-2],
[0,0,0,0,0,0,0,1,1,0],
[0,0,-2,-5,11,5,21,17,13,9],
[-1,1,0,0,0,0,0,0,0,0],
[2,0,1,2,-4,-2,-8,-7,-5,-4]
]

# Sterk 4: 10 (5s Vinal) 2 ideal vertices
Sterk4_vinal = [
(0, 0, 0, -1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
(0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
(0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
(0, 0, 0, 2, -2, -1, -4, -3, -2, -1),
(0, 0, 1, 0, -2, -1, -4, -3, -2, -1),
(1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
(0, 2, -3, -6, 16, 7, 31, 25, 19, 13)
]

# Sterk 5: 10 (2s Julia). Sterk had 14: 10x -4 roots, 4x -2 roots
Sterk5_julia = [
[-1,1,0,0,0,0,0,0,0,0],
[6,6,0,0,-15,-7,-30,-24,-18,-12],
[0,0,0,0,0,0,0,1,1,0],
[-6,-6,0,0,15,7,30,24,18,13],
[2,0,0,0,-3,-1,-5,-4,-3,-2],
[0,0,0,0,0,0,0,0,-1,-1],
[0,0,0,0,1,0,1,0,0,0],
[0,0,0,0,0,0,-1,-1,0,0],
[-2,-2,1,0,4,2,9,7,6,4],
[0,0,-1,1,0,0,0,0,0,0]
]

# Sterk 5: 10 (5s VinAl) 2 ideal vertices
Sterk5_vinal = [
(0, 0, -1, 1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
(0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
(0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
(0, 2, 0, 0, -2, -1, -4, -3, -2, -1),
(1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
(4, 4, 0, 0, -10, -5, -21, -17, -13, -9),
(-6, -6, 1, 0, 16, 7, 31, 25, 19, 13)
]
```

## Pointers

- Computation and data: `computations/scripts/init.sage` — cusp construction lines 322–363; Sterk's hand-entered root sets lines 487–581 (in the $(20,2,0)$ model) and 585–680 (in `TEn`); computed Julia/VinAl root sets lines 720–860.
- Downstream consumer: `archives/notebooks/Classification of Sterk Elliptic Subdiagrams.ipynb` (elliptic-subdiagram classification over `Sterk_roots`), whose plot output is `computations/enriques-paper-artifacts/Sterk/Sterk_1..5/`.
- Cross-reference: `computations/enriques-paper-artifacts/Sterk/README.md`.

## Open questions

1. Identify the reflection subgroup Sterk works with per cusp, and exhibit his 12/10/12/11/14-wall domain as a union of full-group chambers bounded by the computed 9–10 walls.
2. Reconcile the ideal vertices: VinAl reports 1–2 ideal vertices per cusp that Sterk's finite root lists do not carry; determine how they correspond under the chamber decomposition.
3. The two computed sets themselves differ (Sterk 1: Julia 9 vs VinAl 10); check whether the Julia run terminated early or the sets generate the same reflection group.
4. Check which lattice the recorded runs were actually given. `run_vin` (`init.sage:943–960`) intends to hand `vinal` the twist of a signature-$(1,n)$ lattice, because `vinal` expects signature $(n,1)$, and then to negate the returned roots. It initializes `doTwist = False` and then assigns to a differently spelled name `do_twist` inside the branch, so `doTwist` is never true and the negation never runs. Whether the recorded root lists came through that path is not recorded. The preamble's own delegation (`preamble/.../hyperbolic_lattices.sage`, `vinberg_algorithm`) handles the signature convention explicitly and is the surface to re-run against.
