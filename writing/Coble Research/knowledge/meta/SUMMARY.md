---
title: Complete Moduli Spaces of Coble Surfaces — Summary
author: D. Zack Garza
date: 2024-06-01
tags:
  - project/summary
  - surface/coble
  - surface/enriques
---

# Complete Moduli Spaces of Coble Surfaces — Summary

**Author:** D. Zack Garza (University of Georgia) **Date:** June 2024

## Core Object: Coble Surfaces

A **Coble surface** $S$ is a smooth projective rational surface with $|{-K_S}| = \emptyset$ but $|{-2K_S}| \neq \emptyset$.
The paper focuses on **terminal Coble surfaces of K3 type** with $n=1$ boundary component, where $|{-2K_S}| = \{C\}$ for an irreducible smooth rational curve $C$ with $C^2 = -4$ and $K_S^2 = -1$.

These are constructed as the **blowup of $\mathbb{P}^2$ at 10 points** $p_1, \ldots, p_{10}$ — precisely the $A_1$ singularities of an irreducible rational sextic plane curve.
The number of moduli is $\dim(\mathbb{P}^2)^{10}/\operatorname{PGL}_3 - 3 = 9$, where the 3 conditions are Coble's discriminant conditions.

## K3 Covers and Lattice Theory

Taking a section $s \in H^0(\mathcal{L}^{\otimes 2})$ with $\mathcal{L} = \mathcal{O}_S(-K_S)$ yields a **branched double cover** $f: X \to S$ where $X$ is a K3 surface with a nonsymplectic involution $\sigma$.
The fixed locus $\operatorname{Fix}(\sigma)$ consists of disjoint $(-2)$-curves.

The pullbacks of the exceptional classes generate the **Coble lattice**:

$$S_{\mathrm{Co}} = (11, 11, 1)_1 \cong \langle -2 \rangle \oplus E_{10}(2)$$

Its orthogonal complement in the K3 lattice $\Lambda_{\mathrm{K3}} = U^3 \oplus E_8^2$ is the **transcendental lattice**:

$$T_{\mathrm{Co}} = (11, 11, 1)_2 \cong \langle 2 \rangle \oplus E_{10}(2)$$

The paper establishes a chain of **primitive lattice embeddings**, unique up to $O(\Lambda)$:

$$T_{\mathrm{Co}} \hookrightarrow T_{\mathrm{En}} \hookrightarrow T_{\mathrm{dP}} \hookrightarrow \Lambda_{\mathrm{K3}}$$

where $T_{\mathrm{En}} = U \oplus E_{10}(2)$ (Enriques) and $T_{\mathrm{dP}} = U \oplus U(2) \oplus E_8^2$ (degree-2 K3). The embedding $T_{\mathrm{Co}} \hookrightarrow T_{\mathrm{En}}$ sends $h \mapsto \tilde{e} + \tilde{f}$ (the generator of $\langle 2 \rangle$ to a norm-2 vector in $U$) and is the identity on $E_{10}(2)$.

## Period Domain and Moduli Construction

The coarse moduli space is presented as an arithmetic quotient of a **type IV Hermitian symmetric domain**:

$$F_{\mathrm{Co}} = \mathcal{H}_{-2} / O(T_{\mathrm{En}})$$

where $\mathcal{H}_{-2} = \bigcup_{\delta^2 = -2} \delta^{\perp D_T}$ is the **divisor of $(-2)$-vectors** in the Enriques period domain $D_{T_{\mathrm{En}}}$.
This realizes $F_{\mathrm{Co}}$ as a **9-dimensional rational quasiprojective variety** and a boundary divisor in $F_{\mathrm{En}}$.

Alternatively, $F_{\mathrm{Co}}$ is an open subset of $D_{T_{\mathrm{Co}}}/O(T_{\mathrm{Co}})$, using the Global Torelli theorem for K3 surfaces.

A third construction via **Horikawa's model** uses $Y = \mathbb{P}^1 \times \mathbb{P}^1$ with involution $\tau(x,y) = (-x,-y)$: a $\tau$-invariant anti-bicanonical curve $B$ passing through a fixed point yields a nodal K3 whose quotient is a Coble surface.

## Cusp Correspondence (Main Technical Content)

The **Baily-Borel compactification** $\overline{F}_{\mathrm{Co}}^{\mathrm{BB}}$ has boundary strata classified by cusps.
Using the **mirror move algorithm** of Alexeev–Engel applied to $S_{\mathrm{Co}} = (11, 11, 1)_1$:

| Cusp type | Lattice | Count | Geometry |
| --- | --- | --- | --- |
| 0-cusp | $(9,9,1)_1 \cong \langle 2 \rangle \oplus E_8(2)$ | 1 | Type III boundary, disc $\mathbb{D}^2$ |
| 1-cusp | $(7,7,1)_0 \cong A_1^{\oplus 7}$ | 1 | Modular curve $X = \overline{\mathbb{H}/\operatorname{SL}_2(\mathbb{Z})}$ |

The Coxeter diagram $G_{(9,9,1)_1}$ has a unique maximal parabolic subdiagram $\widetilde{B}_7(2)$, confirming exactly one 1-cusp.

### Cusp map $F_{\mathrm{Co}} \to F_{\mathrm{En}}$

The embedding induces a map on Baily-Borel boundary strata:

$$\begin{aligned} (9,9,1)_1 &\mapsto (10,8,0)_1 \\
(7,7,1)_0 &\mapsto (8,6,0)_0 \end{aligned}$$

**Proof method**: The key invariant is the **divisibility** of isotropic vectors.
Since $T_{\mathrm{Co}} = (\langle 1 \rangle \oplus E_{10})(2)$, every Gram matrix entry is 2-divisible, forcing $\operatorname{div}_{T_{\mathrm{Co}}}(v) = 2$ for every non-degenerate isotropic vector.
The image $w_1 = \tilde{e}'$ has $\operatorname{div}_{T_{\mathrm{En}}}(w_1) = 2$, matching the divisibility at Enriques 0-cusp $(10,8,0)$.
For the 1-cusp, $w_2 = 2\tilde{e} + 2\tilde{f} + \tilde{\alpha}_1 + \tilde{\alpha}_2$ is shown to be even in $w_1^{\perp}/w_1 \cong U \oplus E_8(2)$.

### Cusp map $F_{\mathrm{Co}} \to F_{(2,2,0)}$

Under the further embedding into the degree-2 K3 moduli:

$$\begin{aligned} (9,9,1)_1 &\mapsto (18,0,0)_1 \quad \text{(Sterk cusp 2)} \\
(7,7,1)_0 &\mapsto (16,0,0)_0 \end{aligned}$$

This identifies the Coble 0-cusp with the **folding of Sterk cusp 2** by horizontal Coxeter diagram symmetry, predicting disc-type IAS and Kulikov models.

## Connections to Degenerations

- **Morrison's flowerpot degenerations**: Certain Coble degenerations correspond to Type I semistable degenerations of Enriques surfaces with klt singularities, built from flowers ($\mathbb{P}^2$ with conic), stalks (rational ruled $\Sigma_4$), and pots (rational surfaces with $(-4)$-curve boundaries).
- **Halphen surfaces**: Every Coble surface is the blowup of a singular point of an irreducible fiber of a **Halphen surface of index 2**. The moduli of Halphen surfaces of index 2 is also 9-dimensional.
- **Conjectured Kulikov models**: The author conjectures that Coble degenerations correspond to integral-affine discs (rather than spheres or $\mathbb{RP}^2$).

## Paper Status

| Section | Content level |
| --- | --- |
| Introduction | Substantial — definitions, K3 covers, moduli overview, Morrison degenerations, Halphen connection |
| Lattice Preliminaries | Complete — key lattices listed, embedding chain proved |
| Moduli Spaces | Substantial — period domain, GIT, Horikawa model; KSBA subsection empty |
| Cusp Correspondence | Most developed — mirror moves, Coxeter diagrams, full cusp map proofs |
| Geometric Considerations | Stub — one remark on del Pezzo maps |
| Integral Affine Structures | Empty (Todo) |
| KSBA Stable Limits | Empty (Todo) |
| Appendix | Reference material — genus-degree formula, canonical class, Dynkin diagrams, Sterk cusps, nodal Enriques lattices |

* * *

## Outline of Logical Units

### Formal Statements (Theorems, Lemmas, Proofs)

#### §1 Introduction (`000_Introduction.tex`)

1. **Lemma** (L107) `lem:coble_halphen_blowdown` — Blowing down a $(-1)$-curve on a Coble surface yields a Halphen surface of index 2; converse also holds.
   Cites [CD12, Prop. 3.1].

#### §2 Lattice Theoretic Preliminaries (`010_Lattices.tex`)

2. **Lemma** (L19) `lem:primitive_embedding_eta` — Primitive embedding $\eta: T_{\mathrm{Co}} = \langle 2 \rangle \oplus E_{10}(2) \hookrightarrow T_{\mathrm{En}} = U \oplus E_{10}(2)$ sending $h \mapsto \tilde{e}+\tilde{f}$.
3. **Lemma** (L33) `lem:sequence_of_embeddings` — Chain of primitive embeddings $T_{\mathrm{Co}} \hookrightarrow T_{\mathrm{En}} \hookrightarrow T_{\mathrm{dP}} \hookrightarrow \Lambda_{\mathrm{K3}}$, unique up to $O(\Lambda)$; induces $F_{\mathrm{Co}} \hookrightarrow F_{(2,2,0)}$.
   - **Proof** (L46) — Uniqueness via $E_{10}(2) \hookrightarrow \langle -2 \rangle \oplus E_{10}(2)$ and Nikulin surjectivity.
4. **Lemma** (L58) `lem:locally_closed_embedding_BB` — The lattice embeddings induce locally closed embeddings on period domains extending to Baily-Borel compactifications.
   Cites [KK72].
   - **Proof** (L61) — Direct application of Kiernan–Kobayashi.

#### §4 Cusp Correspondence (`030_Cusp_Correspondence.tex`)

5. **Theorem** (L443) `thm:cusp_correspondence` — The embedding $F_{\mathrm{Co}} \to F_{\mathrm{En}}$ induces the cusp correspondence $(9,9,1) \mapsto (10,8,0)$ and $(7,7,1) \mapsto (8,6,0)$.
6. **Lemma** (L473) `lem:divisibility_always_two_Tco` — Every non-degenerate vector in $T_{\mathrm{Co}}$ has divisibility 2.
   - **Proof** (L476) — Gram matrix 2-divisibility argument.
7. **Lemma** (L489) `lem:divisibility_Tco_one` — Isotropic vectors $v_1, v_2$ and their images under $\eta$; $\operatorname{div}_{T_{\mathrm{En}}}(w_1)=2$.
   - **Proof** (L499) — Direct computation of pairing $\tilde{e}' \cdot \tilde{f}' = 2$.
8. **Lemma** (L513) `lem:w1_perp_calculation` — 0-cusp $(9,9,1)$ maps to $(10,8,0)$.
   - **Proof** (L517) — Quotient $w_1^{\perp}/w_1 \cong U \oplus E_8(2)$; alternative via divisibility characterization.
9. **Lemma** (L536) `lem:1_cusp_correspondence` — 1-cusp $(7,7,1)$ maps to $(8,6,0)$.
   - **Proof** (L540) — Divisibility of $w_2$ in $U \oplus E_8(2)$ is 2; $E_8(2)$ pairings are even.
10. **Lemma** (L570) `lem:cusp_map_dP` — Cusp map under $F_{\mathrm{Co}} \hookrightarrow F_{(2,2,0)}$: $(9,9,1) \mapsto (18,0,0)$ and $(7,7,1) \mapsto (16,0,0)$.
    - **Proof** (L583) — Quotient computation; divisibility of $\tilde{w}_2$ is 1 (odd case).

#### Appendix (`999_Appendix.tex`, currently commented out)

11. **Lemma** (L7) `lem:rational_sextic_ten_nodes` — Genus-degree formula: a generic irreducible sextic is rational iff it has exactly 10 $A_1$ singularities.
    - **Proof** (L11) — Direct genus-degree formula computation.

* * *

### Figures and Tables

| # | Type | Location | Label | Description |
| --- | --- | --- | --- | --- |
| 1 | Table | `000_Introduction.tex` L47 | `table:coble-lattices` | Lattices $M, N$ for Coble surfaces with $n$ boundary components |
| 2 | Figure | `030_Cusp_Correspondence.tex` L12 | *(unlabeled)* | Mirror move tree for $(11,11,1)_1$ |
| 3 | Figure | `030_Cusp_Correspondence.tex` L59 | `fig:enriques-cusps` | Cusp diagram for $F_{\mathrm{En}}$ |
| 4 | Figure | `030_Cusp_Correspondence.tex` L76 | `fig:enriques-coxeter-diagrams` | Coxeter diagrams $G_{(10,10,0)_1}$ and $G_{(10,8,0)_1}$ |
| 5 | Figure | `030_Cusp_Correspondence.tex` L166 | `fig:enriques-maximal-parabolics-10-10-0` | Maximal parabolic $\widetilde{E}_8(2)$ in $(10,10,0)_1$ |
| 6 | Figure | `030_Cusp_Correspondence.tex` L218 | `fig:enriques-maximal-parabolics-10-8-0` | Maximal parabolics $\widetilde{E}_8, \widetilde{B}_8$ in $(10,8,0)_1$ |
| 7 | Figure | `030_Cusp_Correspondence.tex` L319 | `fig:coble-cusps` | Cusp diagram for $F_{\mathrm{Co}}$: one 0-cusp, one 1-cusp |
| 8 | Figure | `030_Cusp_Correspondence.tex` L335 | `fig:coble-coxeter-diagrams` | Coxeter diagram $G_{(9,9,1)_1}$ |
| 9 | Figure | `030_Cusp_Correspondence.tex` L388 | `fig:coble-cusp-9-9-1-parabolics` | Unique maximal parabolic $\widetilde{B}_7(2)$ in $(9,9,1)_1$ |
| 10 | Figure | `030_Cusp_Correspondence.tex` L446 | `fig:enriques-coble-correspondence` | Cusp correspondence diagram $F_{\mathrm{Co}} \to F_{\mathrm{En}}$ |
| 11 | Table | `999_Appendix.tex` L59 | `tab:dynkin-diagrams-table` | Classical and affine Dynkin diagrams $A_n$ through $G_2$ |
| 12 | Table | `999_Appendix.tex` L102 | `tab:sterk-cusps` | Sterk cusps 1–5: isotropic vectors and divisibilities |
| 13 | Figure | `999_Appendix.tex` L190 | `fig:coble-coxeter-diagrams` | Coxeter diagrams $G_{(9,9,1)_1}$ and $G_{(7,7,1)_1}$ |

* * *

### Remarks (Expository / Contextual)

#### §1 Introduction (`000_Introduction.tex`)

| # | Line | Title | Content |
| --- | --- | --- | --- |
| 1 | L7 | "On defining Cobles" | Definition of Coble surface, terminal of K3 type, boundary components $C_i$ with $C_i^2=-4$, bound $n \leq 10$ |
| 2 | L11 | "Cobles as blowups" | Coble as blowup of $\mathbb{P}^2$ at $N=9+n$ points; $n=1$ case: 10 nodes of rational sextic. Terminal vs. minimal |
| 3 | L19 | "On the importance of Cobles" | Cremona special point sets; unnodal Coble surfaces maximize $\operatorname{Aut}^*(S)$ |
| 4 | L25 | "On relation to K3s" | Branched double cover $f: X \to S$; fixed locus; 2-elementary invariants $(r,a,\delta)$; ramification cases |
| 5 | L37 | "Coble moduli as divisor in Enriques moduli" | $F_{\mathrm{Co}}$ as 9-dim boundary divisor $\mathcal{H}_{-2}$ in $F_{\mathrm{En}}$ |
| 6 | L41 | "Hodge/lattice theoretic moduli" | Period domain construction; 2-elementary lattice table for $n=1,\ldots,10$ |
| 7 | L72 | "On nonsymplectic involutions" | K3s with nonsymplectic involution; conjecture on flowerpot degenerations and IAS discs |
| 8 | L83 | "On Morrison's degenerations" | Flowers, pots, stalks, flowerpots; Type I semistable degenerations with klt singularities |
| 9 | L91 | *(unlabeled)* | Halphen surfaces of index $n$; terminal Cobles as blowups of index-2 Halphen at singular fibers |
| 10 | L118 | *(unlabeled)* | Conjectured Coble–Halphen moduli correspondence; lattices match on Nikulin's triangle |

#### §3 Moduli Spaces (`020_Moduli_Construction.tex`)

| # | Line | Title | Content |
| --- | --- | --- | --- |
| 11 | L26 | "GIT construction" | $F_{\mathrm{Co}} \subset (\mathbb{P}^2)^{10}/\operatorname{PGL}_3$; dimension count; 3 discriminant conditions |
| 12 | L35 | "Horikawa's construction" | $\tau$-invariant anti-bicanonical curves on $\mathbb{P}^1 \times \mathbb{P}^1$; Coble vs. Enriques quotients |

#### §4 Cusp Correspondence (`030_Cusp_Correspondence.tex`)

| # | Line | Title | Content |
| --- | --- | --- | --- |
| 13 | L556 | *(unlabeled)* | Alternative proof via $\mathcal{H}_{-2}/O(T_{\mathrm{En}})$; orthogonality to $(-2)$-vectors |
| 14 | L564 | *(unlabeled)* | 1-cusps as modular curves $X_0(2)$ and $X$; conjecture on cusp–modular curve correspondence |
| 15 | L599 | *(unlabeled)* | Sterk cusp 2 identification; disc-type IAS and Kulikov models predicted |

#### §5 Geometric Considerations (`040_Geometric.tex`)

| # | Line | Title | Content |
| --- | --- | --- | --- |
| 16 | L5 | *(unlabeled)* | Cobles via K3 degeneration; degree-2 map to quartic del Pezzo; isotropic sequences in $E_{10}$ |

#### Appendix (`999_Appendix.tex`)

| # | Line | Title | Content |
| --- | --- | --- | --- |
| 17 | L19 | `\cref{rmk:severi-sextics}` "Severi varieties and degenerate sextics" | Discusses $V_{6,10}$ and lower-dimensional strata of rational sextics with $A_2$ or higher order singularities |
| 18 | L23 | "Canonical class of Cobles" | $K_S^2 = -1$ computation; $\rho(X)=11$; Hurwitz formula yields $C \sim -2K_S$ |
| 18 | L38 | "Invariants of antibicanonical curves" | Genus formula: $p_a(C)=0$, $C^2=-4$ |
| 19 | L82 | *(unlabeled)* | Adjunction formula for blowups |
| 20 | L93 | *(unlabeled)* | Hurwitz formula for branched covers |
