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

| $j$ | Sterk's $v$ (4.2.3, p. 16) | $K_j = v^{\perp}/\ZZ v$ (4.3.4, p. 17) | group | our record's lattice | published walls |
|---|---|---|---|---|---|
| 1 | $e$ | $H(2)\oplus E_8(-2) = U(2)\oplus E_8(2)$ | $G_e = \rho(\Stab(e))$ | $K(L_1)$, type $(10,10,0)$ | 12 |
| 2 | $e'$ | $H\oplus E_8(-2) = U\oplus E_8(2)$ | $G_{e'}$ | $K(L_2)$, type $(10,8,0)$ | 10 |
| 3 | $e'+f'+\omega$, $\omega^2 = -4$ | $H\oplus E_8(-2)$ | $G_v$ | $K(L_2)$ | 12 |
| 4 | $e'+2f'+\alpha$, $\alpha^2 = -8$ | $H\oplus E_8(-2)$ | $G_v$ | $K(L_2)$ | 11 |
| 5 | $2e+2f+\alpha$, $\alpha^2 = -8$ | $H\oplus E_8(-2)$ | $G_v$ | $K(L_2)$ | 14 |

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
