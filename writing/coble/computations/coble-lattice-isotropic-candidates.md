---
title: Candidate isotropic vectors in T_Co and their transport to T_En and T_dP
unit: computation
status: partial
tags:
  - coble
  - isotropic-orbits
  - divisibility
  - cusps
---

# Candidate isotropic vectors in $T_{\Co}$

**Provenance.** `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/computational-research/canonical/notebooks/Coble Lattice Invariants.ipynb` and `.../sage-scripts/init.sage`. Absent from the dissertation, which contains no Coble lattice at all.

::: {.Remark}
## What open problem this addresses

`content_pandoc/sections/Open_Problems/Open_Problems.md` records as open the enumeration of $\Gamma_{\Co}$-orbits of primitive isotropic vectors in $T_{\Co}$, and the verification that exactly one $\OStab(T)$-orbit exists in divisibility 2; the proof of `lem:divisibilityTcoOne` currently *assumes* that uniqueness.
This note records the concrete candidate list and the machinery assembled to settle it.
:::

## The lattices as constructed

$$
T_{\Co} = \gens{2} \oplus E_{10}(2) = \gens{2}\oplus U(2)\oplus E_8(2),
\qquad
S_{\Co} = \gens{-2} \oplus E_{10}(2),
$$
of rank 11, matching this project's $T_{\Co} = (11,11,1)_2$ and $S_{\Co} = (11,11,1)_1$.

## The 18 candidate vectors

In the basis $h,\, e',\, f',\, a_1,\ldots,a_8$ of $T_{\Co}$, the candidates are

$$
\begin{aligned}
&e', \quad f', \quad 2h+a_1+a_2, \quad e'+f'+a_1, \quad 2h-f'-a_1-a_6-a_7-a_8, \\
&8e'+f'+a_4-2a_5-a_8, \quad 2h+e'-a_1-a_2, \quad 2h+e'-a_2-a_3, \quad 2h-a_1+a_2-a_3, \\
&2e'+f'-a_1-a_8, \quad 5e'+f'+a_2+2a_3, \quad 2h+a_1-a_4, \quad 2h+a_2-a_5, \\
&2h+a_3-a_6, \quad 2h+a_4-a_7, \quad 2h+a_5-a_8, \quad 2h-a_6-a_8 .
\end{aligned}
$$

Norm and divisibility were evaluated on each by a helper `divisibility(v, L)` returning the minimum of $|\inner{v}{x}|$ over nonzero $x$, together with the full list of inner products.

## The three-way parallel transport

::: {.Construction}
### Term-by-term transport along the embedding chain

The same 18 vectors are transported term-by-term along the embedding chain $T_{\Co}\injects \ten\injects \tdp$:

- into $\ten = U \oplus U(2) \oplus E_8(2)$ by $h \mapsto e+f$;

- into $\tdp = U \oplus U(2) \oplus E_8^{\oplus 2}$ by $a_i \mapsto a_i + b_i$.

This yields a parallel norm and divisibility table across all three lattices, which is exactly the vector-by-vector form in which the Enriques-to-Coble cusp correspondence becomes checkable.
:::

::: {.Remark}
### Recorded gap: the numbers were not saved

The notebook cells that evaluate norm and divisibility on these vectors, in all three lattices, have their outputs **cleared**. The vectors and the method survive; the resulting numbers do not.
Re-running is the obvious first step, and is cheap: the lattices, the vectors and the helper are all in `init.sage`.
:::

## Orbit machinery available

::: {.Remark}
### The GAP bridge to polyhedral_common

The notebook drives GAP's `INDEF_FORM_GetOrbitRepresentative` from `polyhedral_common`, an orbit-representative solver for indefinite forms.
This is the tool that would settle the open orbit count directly, rather than by hand.
A raw trace of one such run on a rank-10 form with diagonal $(-4,-4,-4,-4,-2,-4,-4,-4,-4,-2)$ survives in `reports/logs.txt`, whose two input Gram matrices are worth keeping even though the remaining 8800 lines are per-iteration bookkeeping.
:::

::: {.Definition}
### The isotropic trichotomy used as a separating invariant

`init.sage` provides `get_isotrop_type`, which classifies a primitive isotropic vector as **Odd**, **Even ordinary**, or **Even characteristic**, by testing $(v^\perp/v)^\perp$ against $U$, $U(2)$ and $I_{1,1}(2)$.
This trichotomy is what the cusp correspondence sections of this project rely on.
:::

## Sterk's five representatives, for comparison

In $\ten = U \oplus E_{10}(2)$ with $\omega = 2w_8$ (norm 4) and $\alpha = 2w_1$ (norm 8):
$$
\eta_1 = e,\quad \eta_2 = e',\quad \eta_3 = e'+f'+\omega,\quad \eta_4 = e'+2f'+\alpha,\quad \eta_5 = 2e+2f+\alpha,
$$
with the asserted invariants $\div(e)=1$ and $e^\perp/e \cong E_{10}(2) = \EnriquesInvariants$; $\div(e')=2$ and $e'^\perp/e' \cong U\oplus E_8(2) = (10,8,0)$; $\gens{e,e'}^\perp/\gens{e,e'} \cong E_8(2) = (8,8,0)$; and for $v' = 2e+2f+2w_1$, $\gens{e',v'}^\perp \cong (8,6,0)$.

Also recorded, from a separate OSCAR/Julia notebook, the $(r,a,\delta)$ invariants with printed discriminant forms: $U(2)\to(2,2,0)$, $U(2)\oplus E_8(2)\to(10,10,0)$, $U^3\oplus E_8(2)\to(14,8,0)$, $U\oplus U(2)\oplus E_8^{\oplus2}\to(20,2,0)$, $U\oplus U(2)\oplus E_8(2)\to(12,10,0)$, $E_8(2)\to(8,8,0)$.
Here $\delta$ is computed as "some diagonal entry of the discriminant quadratic form is non-integral", citing AE22 Def.
2.3 for coparity.

Related: [cusp-correspondence morphism chain](../coble-moduli/cusp-correspondence-morphism-chain.md), [computational toolchain and recipe](computational-toolchain-and-recipe.md).
