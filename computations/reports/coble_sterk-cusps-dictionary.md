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
| 1 | $e$ | $U(2)\oplus E_8(2)$ | $G_e\cong\{\pm1\}W_e\rtimes S_e$, $S_e\cong\ZZ/2\times\ZZ/2$ (§4.3.5, p. 19) | $K(L_1)$, $(10,10,0)$ | **12** (p. 19, Fig. 4) | 12 (`Sterk1.coxiter`, p. 19) |
| 2 | $e'$ | $U\oplus E_8(2)$ | $G_{e'} = \Orth(H\oplus E_8(-2)) = \{\pm1\}W_{e'}$ (§4.3.6, p. 21) | $K(L_2)$, $(10,8,0)$ | **10** (p. 21, Fig. 6) | 10 (`Sterk2.coxiter`, p. 21) |
| 3 | $e'+f'+\bar\alpha_8$ | $U\oplus E_8(2)$ | $G_v = \{\pm1\}W_v\rtimes\ZZ/2$ (§4.3.7, p. 22) | $K(L_2)$ | **12** (p. 22, Fig. 8) | 12 (`Sterk3.coxiter`, p. 22) |
| 4 | $2e'+f'+\bar\alpha_1$ (§4.3.8, p. 23) | $U\oplus E_8(2)$ | $G_v$, symmetry from $\Gamma_v$ (4.3.10) | $K(L_2)$ | **11** (p. 23, Fig. 10) | 11 (`Sterk4.coxiter`, p. 23) |
| 5 | $2e+2f+\bar\alpha_1$ (§4.3.9, p. 24) | $U\oplus E_8(2)$ | $G_v$, symmetries lift to $\Gamma_v$ (4.3.10) | $K(L_2)$ | **14** (p. 24, Fig. 12) | 14 (`Sterk5.coxiter`, p. 24) |

## The plates, read where read

The figures are read from `pdftoppm -r 300` renders of the plate pages of the Sterk scan
(`.scratch/figtest/`: `s3-22.png` and `s-300-{19,23,24}-*`); the captions carry no text and the text
layer renders every root name as `~`, so both the counts and the bonds below are read off the images.
The plates' conventions are the ones `computations/coxiter/README.md` records: a single bond is
$m = 3$, a bold or arrowed bond $m = 4$, an $\infty$-bond is labelled $\infty$.

- **$j = 1$, Fig. 4, p. 19: 12 nodes.** $\alpha_1,\dots,\alpha_{12}$ in a circle-with-cross: the
  outline $\alpha_1$–$\alpha_3$–$\alpha_4$–$\alpha_5$–$\alpha_6$–$\alpha_7$–$\alpha_8$–$\alpha_{11}$–$\alpha_1$
  with all eight bonds plain, and the horizontal chain $\alpha_4$–$\alpha_2$–$\alpha_{12}$–$\alpha_9$–
  $\alpha_{10}$–$\alpha_8$ whose **three middle bonds** $\alpha_2\alpha_{12}$, $\alpha_{12}\alpha_9$,
  $\alpha_9\alpha_{10}$ are the three $\infty$-bonds, the two end bonds being plain; the labelled roots
  $\alpha_9 = f'-e'$, $\alpha_{10} = \bar\alpha_8+2e'$, $\alpha_{11} = 2e'+2f'+\bar\alpha_1+\bar\alpha_8$,
  $\alpha_{12} = 5e'+3f'+2\bar\alpha_2$. **Agrees with CoxIter's 12.**
- **$j = 2$, Fig. 6, p. 21: 10 nodes.** $\alpha_1,\alpha_3,\alpha_4,\dots,\alpha_{10}$ on a chain with
  $\alpha_2$ hanging below $\alpha_4$, one bold (double) bond near the right end and a terminal
  arrow; legend "$\circ$: $(-4)$-vector, $\bullet$: $(-2)$-vector"; $\alpha_9 = \bar\alpha_8+2f$,
  $\alpha_{10} = e-f$. **Agrees with CoxIter's 10**, and agrees with the full-group chamber computed in
  `coble_TEn-chambers.py` — as it must, since Sterk's $G_{e'}$ *is* $\Orth(H\oplus E_8(-2))$ (§4.3.6).
- **$j = 3$, Fig. 8, p. 22: 12 nodes.** $\alpha_1,\dots,\alpha_7,\alpha_9,\dots,\alpha_{13}$: the ring
  $\alpha_4$–$\alpha_3$–$\alpha_1$–$\alpha_{12}$–$\alpha_9$–$\alpha_{11}$–$\alpha_{10}$–$\alpha_{13}$–$\alpha_7$–$\alpha_6$–$\alpha_5$–$\alpha_4$
  with $\alpha_2$ hanging below $\alpha_4$; seven plain bonds, four arrowed (mixed-length) bonds
  $\alpha_{13}$–$\alpha_7$, $\alpha_{12}$–$\alpha_9$, $\alpha_9$–$\alpha_{11}$, $\alpha_{13}$–$\alpha_{10}$,
  and the $\infty$-bond $\alpha_{11}$–$\alpha_{10}$; labelled $\alpha_9 = f-e$, $\alpha_{10} = 2f'+\bar\alpha_8$,
  $\alpha_{11} = 2e-2f'-\bar\alpha_8$, $\alpha_{12} = 2e+(\bar\alpha_1-\bar\alpha_8)$,
  $\alpha_{13} = (e+f)+(\alpha_8-f')$. **$\alpha_8$ is not a node**: it enters only through these labels,
  as the dual basis vector of $E_8(-2)$ with $(\bar\alpha_i,\alpha_j) = 2\delta_{ij}$ (Sterk §2, p. 32),
  which is what produced the thirteen-node misreading recorded earlier on this page. The $\ZZ$-span of
  the roots is $\ZZ\{\alpha_1,\dots,\alpha_7,\alpha_8-f',e+f,e-f\}$. **Agrees with CoxIter's 12**, on the
  input `computations/coxiter/Sterk3.coxiter`: 12 vertices, dimension 9, finite covolume yes, 4 vertices
  at infinity, transcript `computations/coxiter/logs/Sterk3.txt`.

- **$j = 4$, Fig. 10, p. 23: 11 nodes.** Chain $\alpha_{11},\alpha_3,\alpha_4,\dots,\alpha_8,\alpha_{12},\alpha_9$
  with $\alpha_2$ below $\alpha_4$ and $\alpha_{10}$ below $\alpha_8$, an arrow at each end; roots span
  $\ZZ\{e+f,e-f,-e'+\alpha_1,\alpha_2,\dots,\alpha_8\}$; $\alpha_9 = f-e$, $\alpha_{10} = \bar\alpha_8+2e'$,
  $\alpha_{11} = e+f+\alpha_1-e'$, $\alpha_{12} = 2e-2e'+\bar\alpha_8-\alpha_1$. **Agrees with
  CoxIter's 11.**
- **$j = 5$, Fig. 12, p. 24: 14 nodes.** Outer octagon $\alpha_6$–$\alpha_7$–$\alpha_8$–$\bar\alpha_8$–
  $\alpha_{10}$–$\alpha_2$–$\alpha_4$–$\alpha_5$–$\alpha_6$, all eight bonds plain; the inner vertical
  $\alpha_6$–$\alpha_{12}$–$\alpha_9$–$\alpha_{11}$–$\alpha_{10}$, all four bonds arrowed; two arrowed
  diagonals $\alpha_4$–$\alpha_{14}$–$\bar\alpha_1$ and $\bar\alpha_1$–$\alpha_{13}$–$\alpha_8$; and
  **one** $\infty$-bond, $\alpha_9$–$\bar\alpha_1$. Roots span $\ZZ\{\tilde e+\tilde f,\tilde e-\tilde f,
  \tilde\alpha_1,\dots,\tilde\alpha_8\}$. **Agrees with CoxIter's 14**, and 17 edges.
  An earlier entry on this page described this plate as carrying three $\infty$-bonds on an inner
  hexagon: that was wrong, and the plate at 300 dpi has one, as the reconstruction's Gram has one
  ($\alpha_9$–$\bar\alpha_1$, pairing 4 between two $(-4)$-vectors).

A note on the representatives: §4.3.8 and §4.3.9 use $2e'+f'+\bar\alpha_1$ and $2e+2f'+\bar\alpha_1$,
which differ from the Prop. 4.2.3 list ($e'+2f'+\alpha$, $2e+2f+\alpha$) by $\Gamma$-equivalence;
the lattice $v^{\perp}/\ZZ v$ is $U\oplus E_8(2)$ either way (Lemma 4.3.4, p. 17).

### The input for $j = 3$, and the count that was withdrawn

The number in @sec-coxiter-results-for-cusp-lattices had no input in `computations/coxiter/` until
this record: that directory held `10-10-0_1`, `10-8-0_1`, `9-9-1_1`, `Sterk2` and the benchmark
graphs, and no Sterk 1, 3, 4 or 5. It now holds all five. The $j = 3$ input is `Sterk3.coxiter`, and
`computations/reports/coble_sterk3-coxiter-input.py` is what produces it: the twelve roots are written
from Sterk's closed forms on p. 22 through `cusp_epfpa8()` of
`computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage`, their Gram is computed, and each
nonzero pairing $b$ is turned into the Coxeter weight exactly, by comparing $b^2$ against
$|n_in_j|$ ($4b^2 = |n_in_j|$ gives $3$, $2b^2 = |n_in_j|$ gives $4$, $b^2 = |n_in_j|$ gives
$\infty$). That run also checks the file against the derivation, so the input cannot drift from its
source:

- the norms are $-4$ on ten of the twelve vertices and $-2$ on $\alpha_9$ and $\alpha_{13}$;
- the edges are $\alpha_1\alpha_3$, $\alpha_1\alpha_{12}$, $\alpha_2\alpha_4$, $\alpha_3\alpha_4$,
  $\alpha_4\alpha_5$, $\alpha_5\alpha_6$, $\alpha_6\alpha_7$ at $3$;
  $\alpha_7\alpha_{13}$, $\alpha_9\alpha_{11}$, $\alpha_9\alpha_{12}$, $\alpha_{10}\alpha_{13}$ at
  $4$; and $\alpha_{10}\alpha_{11}$ at $\infty$ — twelve edges in all;
- the Gram has rank $10$ and inertia $(1,9,2)$, the Schläfli signature $(9,1)$ of $v^{\perp}/\ZZ v$;
- CoxIter's own Gram matrix for the file equals $-x\cdot y/\sqrt{n_xn_y}$ in every entry, which is
  the claim that the input encodes that form and not merely a graph of the same shape.

An earlier draft of the input carried the bond $\alpha_1$–$\alpha_{12}$ as an arrowed ($m = 4$) one.
That is not what the plate or the roots say — it is plain, $m = 3$ — and it is enough to break the
form: CoxIter then reported `Finite covolume: no` with a Gram of signature $(10,2)$. The check above
is what caught it, which is the reason the record carries the derivation rather than the file alone.

**The thirteen-node count recorded earlier on this page is withdrawn.** It came from reading the
label $\alpha_8$ in the label list as a node. Fig. 8 has twelve nodes; the record's "Sterk 3: 12
vertices" was right, and the defect was the missing input, which now exists. The OCR state of the
scan is not a property of this record: every root name in the text layer extracts as `~`, so no count
on this page comes from the text layer — they come from the rendered plates.

Three columns need their page stated exactly:

- **Lattice, $j = 1$:** $U(2)\oplus E_8(2)$ is my $K(L_1)$, which `coble_TEn-chambers.py` builds as
  the Gram matrix $2H\oplus 2E_8(-1)$; the identification is by the invariants of
  `prop:zero-cusp-lattices` (rank 10, determinant $-2^{10}$, $(10,10,0)$) and is the same lattice
  Sterk names in 4.3.4. **$j = 2,\dots,5$:** all four are $U\oplus E_8(2) = K(L_2)$, rank 10,
  determinant $-2^8$, $(10,8,0)$.
- **Wall counts:** 12, 10, 12, 11, 14 are Sterk's, read from the plates of Figs 4, 6, 8, 10 and 12 on
  pp. 19, 21, 22, 23 and 24 and recorded in this tree at `sec-coxiter-results-for-cusp-lattices`
  (CoxIter runs on the folded diagrams, "Vertices" column: 12, 10, 12, 11, 14) and in
  `qst:sterk-reflection-subgroup`. The plate pages carry no caption text and their figures are not in
  the text layer: the counts come from `pdftoppm` renders at 300 dpi, and all five now have an input
  in `computations/coxiter/` — `Sterk1`, `Sterk2`, `Sterk3`, `Sterk4`, `Sterk5`. Cusps 1, 3, 4 and 5
  are checked against the reconstruction of their roots, by
  `computations/reports/coble_sterk-cusp-coxiter-inputs.py` for 1, 4 and 5 and by
  `computations/reports/coble_sterk3-coxiter-input.py` for 3; `Sterk2.coxiter` predates this batch and
  is not checked. The subgroup-chamber script below is still not run, and now only because the
  chamber of a prescribed subgroup is the operation this tree does not have.
- **Signature line:** the five entries $9,1,2$; $9,1,0$; $9,1,2$; $9,1,1$; $9,1,4$ of
  `sec-coxiter-results-for-cusp-lattices` are $(n_+,n_-,n_0)$ of the *sign-flipped* Gram of Sterk's
  roots, $-x\cdot y$ — rank 10, nine space-like and one time-like direction, and the third entry the
  nullity, i.e. the number of linear dependencies among that diagram's roots. All five reproduce that
  way in `computations/reports/coble_sterk-cusp-signatures-run.txt`, which is what identifies the
  column. It is **not** CoxIter's own `Signature (numerically)` line: at $j = 3$ that line reads
  `10,2,0` for the Gram of the same diagram, rank 10, inertia $(9,1,2)$ — see the note on
  `computations/coxiter/logs/Sterk3.txt` in `computations/coxiter/README.md`. Quote one or the other,
  not the two interchangeably.
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
