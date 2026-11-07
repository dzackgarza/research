# Sterk's five cusps: lattice, group, wall count, and where each lives in this record

Source: `tmp/sources/sterk-1991-compactifications-of-the-period-space-of-enriques-surfaces-i.pdf`,
read directly. Article pages are given per item; the numbering below is Sterk's.

## The five cusps and their lattices (Sterk Prop. 4.2.3, p. 16; Lemma 4.3.4, p. 17)

> **4.2.3 Proposition.** Let $v\in L_\sim$ be a primitive isotropic vector. Then $v$ is in the
> $\Gamma$-orbit of one of the following vectors: $e$, $e'$, $e'+f'+\omega$, $e'+2f'+\alpha$,
> $2e+2f+\alpha$ ($\alpha,\omega\in E_8(-2)$, $\alpha^2 = -8$, $\omega^2 = -4$). Moreover, these
> five vectors are all inequivalent modulo $\Gamma$.
>
> **4.2.4 Remark.** It follows from (4.2.3) that $\overline{\mathcal{F}}/\Gamma$ contains precisely
> five zero-dimensional boundary components. (p. 17)
>
> **4.3.4 Lemma.** Let $v$ be one of the five vectors in (4.2.3). Then
> $v^{\perp}/\ZZ v \cong H\oplus E_8(-2)$ for $v\ne e$, and
> $e^{\perp}/\ZZ e \cong H(2)\oplus E_8(-2)$. (p. 17)

## The group Sterk takes the chamber of (Sterk 4.3.1, p. 17)

> **4.3.1** If $v\in L$ is primitive isotropic, then the quotient $v^{\perp}/\ZZ v$ inherits a
> quadratic form of hyperbolic signature (which is $(1,9)$ here), and the stabilizer $\Gamma_v$ of
> $v$ determines a subgroup $G_v\subset \mathrm{O}(v^{\perp}/\ZZ v)$. … Vinberg's results can be
> used to find $\mathrm{I}_1(v^{\perp}/\ZZ v)/G_v$.

So the group is **$G_v$, the image of the integral stabilizer $\Gamma_v$** — not the full
$\mathrm{O}(v^{\perp}/\ZZ v)$. This is the same $G_v$ that `coble_TEn-sandwich.py` computes as
$\rho(S_{\eta_j})$, and the reason Sterk's diagrams for $j = 2,\dots,5$ differ although the lattices
are mutually isometric is exactly that the subgroups $G_v$ differ.

## The dictionary

| $j$ | Sterk's $v$ (4.2.3, p. 16) | $K_j$ (4.3.4, p. 17) | group (page) | our lattice | nodes read from the plate (page, figure) | CoxIter |
|---|---|---|---|---|---|---|
| 1 | $e$ | $U(2)\oplus E_8(2)$ | $G_e\cong\{\pm1\}W_e\rtimes S_e$, $S_e\cong\ZZ/2\times\ZZ/2$ (§4.3.5, p. 19) | $K(L_1)$, $(10,10,0)$ | **12** (p. 19, Fig. 4) | 12 |
| 2 | $e'$ | $U\oplus E_8(2)$ | $G_{e'} = \Orth(H\oplus E_8(-2)) = \{\pm1\}W_{e'}$ (§4.3.6, p. 21) | $K(L_2)$, $(10,8,0)$ | **10** (p. 21, Fig. 6) | 10 |
| 3 | $e'+f'+\bar\alpha_8$ | $U\oplus E_8(2)$ | $G_v = \{\pm1\}W_v\rtimes\ZZ/2$ (§4.3.7, p. 22) | $K(L_2)$ | **13** (p. 22, Fig. 8) | 12 |
| 4 | $2e'+f'+\bar\alpha_1$ (§4.3.8, p. 23) | $U\oplus E_8(2)$ | $G_v$, symmetry from $\Gamma_v$ (4.3.10) | $K(L_2)$ | **11** (p. 23, Fig. 10) | 11 |
| 5 | $2e+2f+\bar\alpha_1$ (§4.3.9, p. 24) | $U\oplus E_8(2)$ | $G_v$, symmetries lift to $\Gamma_v$ (4.3.10) | $K(L_2)$ | **14** (p. 24, Fig. 12) | 14 |

## The plates, read where read

The figures are read from `pdftoppm -r 150` renders of PDF pp. 19-24 of the Sterk scan
(`.scratch/figtest/st-19..24.png`); the captions carry no text, so the counts are read off the images.

- **$j = 1$, Fig. 4, p. 19: 12 nodes.** $\alpha_1,\dots,\alpha_{12}$ in a circle-with-cross, the
  horizontal chain $\alpha_4$–$\alpha_8$ carrying three $\infty$-bonds; the labelled roots
  $\alpha_9 = f'-e'$, $\alpha_{10} = \bar\alpha_8+2e'$, $\alpha_{11} = 2e'+2f'+\bar\alpha_1+\bar\alpha_8$,
  $\alpha_{12} = 5e'+3f'+2\bar\alpha_2$. **Agrees with CoxIter's 12.**
- **$j = 2$, Fig. 6, p. 21: 10 nodes.** $\alpha_1,\alpha_3,\alpha_4,\dots,\alpha_{10}$ on a chain with
  $\alpha_2$ hanging below $\alpha_4$, one bold (double) bond near the right end and a terminal
  arrow; legend "$\circ$: $(-4)$-vector, $\bullet$: $(-2)$-vector"; $\alpha_9 = \bar\alpha_8+2f$,
  $\alpha_{10} = e-f$. **Agrees with CoxIter's 10**, and agrees with the full-group chamber computed in
  `coble_TEn-chambers.py` — as it must, since Sterk's $G_{e'}$ *is* $\Orth(H\oplus E_8(-2))$ (§4.3.6).
- **$j = 3$, Fig. 8, p. 22: 13 nodes.** $\alpha_1,\dots,\alpha_{13}$ in a hexagonal ring with
  $\alpha_{11}$–$\alpha_{10}$ joined by an $\infty$-bond and arrowed bonds on the lower flanks;
  labelled $\alpha_9 = f-e$, $\alpha_{10} = 2f'+\bar\alpha_8$, $\alpha_{11} = 2e-2f'-\bar\alpha_8$,
  $\alpha_{12} = 2e+(\bar\alpha_1-\bar\alpha_8)$, $\alpha_{13} = (e+f)+(\bar\alpha_8-f')$; the
  $\ZZ$-span of the roots is $\ZZ\{\alpha_1,\dots,\alpha_7,\alpha_8-f',e+f,e-f\}$.

- **$j = 4$, Fig. 10, p. 23: 11 nodes.** Chain $\alpha_{11},\alpha_3,\alpha_4,\dots,\alpha_8,\alpha_{12},\alpha_9$
  with $\alpha_2$ below $\alpha_4$ and $\alpha_{10}$ below $\alpha_8$, an arrow at each end; roots span
  $\ZZ\{e+f,e-f,-e'+\alpha_1,\alpha_2,\dots,\alpha_8\}$; $\alpha_9 = f-e$, $\alpha_{10} = \bar\alpha_8+2e'$,
  $\alpha_{11} = e+f+\alpha_1-e'$, $\alpha_{12} = 2e-2e'+\bar\alpha_8-\alpha_1$. **Agrees with
  CoxIter's 11.**
- **$j = 5$, Fig. 12, p. 24: 14 nodes.** Outer octagon $\alpha_6,\alpha_5,\alpha_4,\alpha_2,\alpha_{10},
  \bar\alpha_8,\alpha_8,\alpha_7$ and inner hexagon $\alpha_{12},\bar\alpha_1,\alpha_{14},\alpha_9,
  \alpha_{13},\alpha_{11}$, with three $\infty$-bonds; roots span $\ZZ\{\tilde e+\tilde f,\tilde e-\tilde f,
  \tilde\alpha_1,\dots,\tilde\alpha_8\}$. **Agrees with CoxIter's 14.**

A note on the representatives: §4.3.8 and §4.3.9 use $2e'+f'+\bar\alpha_1$ and $2e+2f'+\bar\alpha_1$,
which differ from the Prop. 4.2.3 list ($e'+2f'+\alpha$, $2e+2f+\alpha$) by $\Gamma$-equivalence;
the lattice $v^{\perp}/\ZZ v$ is $U\oplus E_8(2)$ either way (Lemma 4.3.4, p. 17).

### The record's own input for $j = 3$, traced

The number in @sec-coxiter-results-for-cusp-lattices comes from the per-figure vertex maps in the
Sage artifact `.scratch/sterk_figure_labels-reps-run.txt`, whose block for this cusp reads

```
3.3.10  v = e' + f' + abar_8    |Aut| = 2, so the map is determined up to 2 relabellings
   script a_{i+1} -> manuscript vertex 0..11
   one representative: [6, 9, 5, 4, 3, 2, 1, 8, 10, 11, 7, 0]
```

so the diagram the record ran CoxIter on has **twelve** vertices, $0..11$, with a representative
permutation of twelve entries --- not thirteen. Two consequences, both recorded:

1. **No `Sterk3.coxiter` input exists in `computations/coxiter/`** (that directory holds
   `10-10-0_1`, `10-8-0_1`, `9-9-1_1`, `Sterk2`, and the benchmark graphs, and no Sterk 1, 3, 4 or
   5). The record's "Sterk 3: 12 vertices" is therefore a number without a reproducible input, which
   is a record defect whatever Fig. 8 says.
2. The artifact and the plate do not describe the same vertex set: the artifact's twelve vertices
   against Fig. 8's thirteen. So the answer to the question is **not** "the record's input omitted a
   root of Fig. 8" in the sense of a transcription slip: the input is a twelve-vertex diagram, and the
   question is which of Fig. 8's thirteen nodes is the extra one.

The candidates are narrow, from Sterk's own labels on p. 22: $\alpha_{11} = (e+f)-\alpha_9-\alpha_{10}$
is determined by $\alpha_9 = f-e$ and $\alpha_{10} = 2f'+\bar\alpha_8$, and the $\ZZ$-span of the roots is
the nine-generator lattice $\ZZ\{\alpha_1,\dots,\alpha_7,\alpha_8-f',e+f,e-f\}$. The node not pinned by
those relations is $\alpha_{12} = 2e+(\bar\alpha_1-\bar\alpha_8)$, which is the candidate for the
thirteenth.

**Not yet decided**, and the deciding computation needs one reading first: the $\Gamma$-transform
$\bar\alpha_i$ is defined earlier in Sterk than p. 22, and without its definition the vectors
$\alpha_{10},\alpha_{12},\alpha_{13}$ cannot be written in the §4.3.7 basis $e,f,\alpha_1,\dots,\alpha_7,
-f'+\alpha_8$. Guessing them would put an unverifiable Gram matrix under a real citation.

**A disagreement, stated as a defect in one of the two and not resolved here:** for $j = 3$ the plate
(Fig. 8, p. 22) shows **13** nodes while the tree's CoxIter record reports **12** vertices for Sterk 3
(`sec-coxiter-results-for-cusp-lattices`, "Vertices" column). One of the two is wrong: either the
CoxIter run was made on a diagram that is not Fig. 8, or a node of Fig. 8 belongs to a different
figure's count (for instance if Sterk's Fig. 8 includes a root that is not a wall of the chamber).
This is the next question and is not settled by preferring either number.

Two columns need their page stated exactly:

- **Lattice, $j = 1$:** $U(2)\oplus E_8(2)$ is my $K(L_1)$, which `coble_TEn-chambers.py` builds as
  the Gram matrix $2H\oplus 2E_8(-1)$; the identification is by the invariants of
  `prop:zero-cusp-lattices` (rank 10, determinant $-2^{10}$, $(10,10,0)$) and is the same lattice
  Sterk names in 4.3.4. **$j = 2,\dots,5$:** all four are $U\oplus E_8(2) = K(L_2)$, rank 10,
  determinant $-2^8$, $(10,8,0)$.
- **Wall counts:** 12, 10, 12, 11, 14 are Sterk's, recorded in this tree at
  `sec-coxiter-results-for-cusp-lattices` (CoxIter runs on the folded diagrams, "Vertices"
  column: 12, 10, 12, 11, 14) and in `qst:sterk-reflection-subgroup`. **I did not locate Sterk's
  diagram page in the scan** (the figures are not OCR-readable and the plate pages carry no caption
  text): the counts are cited from the tree's CoxIter record, not from a page of Sterk read here.
  This is stated as such rather than attached to a page of Sterk I have not verified.
- **Group:** 4.3.1, p. 17, states it as $G_v = \rho(\Stab_{\Gamma}(v))$ — the transcribing sentence
  is quoted above. The *identification* of each $G_v$ with a subgroup of $\mathrm{O}(K_j)$
  computed in this tree is `coble_TEn-sandwich.py`'s $\rho(S_{\eta_j})$, and for $j = 2,\dots,5$ it
  is the same lattice with four a priori different subgroups.

## The script, ready to run after the vector job

`computations/reports/coble_sterk-cusps-chambers.py` (written, not run): for each $j$ it builds $K_j$
by the invariants above, computes $G_v \approx \rho(S_{\eta_j})$ by the sandwich construction of
`coble_TEn-sandwich.py`, and asks for the chamber *under that subgroup* — which is the operation
this tree does not have (a chamber for a prescribed finite-index subgroup of $\mathrm{O}(K)$, filed
under sage-extensions#281 after #285). Until it exists the script can print the full-group chamber
(known: 10 walls for $K(L_2)$, recorded) and the subgroup's index, and nothing about Sterk's 12, 11,
14.
