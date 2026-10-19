---
title: Candidate isotropic vectors in T_Co and their transport to T_En and T_dP
unit: computation
status: partial
tags:
  - coble
  - isotropic-orbits
  - divisibility
  - cusps
notes: >-
  Provenance: archived notebook `Coble Lattice Invariants.ipynb` and Sage bootstrap `init.sage` in the computational-research corpus. Absent from the dissertation, which contains no Coble lattice at all.
---

# Candidate isotropic vectors in $T_{\Co}$ {#sec-coble-lattice-isotropic-candidates}

::: {.remark title="What open problem this addresses"}

[[open-problems|Open problems]] records as open the enumeration of $\Gamma_{\Co}$-orbits of primitive isotropic vectors in $T_{\Co}$, and the verification that exactly one $\discriminantkernel{T}$-orbit exists in divisibility 2; the proof of @lem:divisibilityTcoOne currently *assumes* that uniqueness.
This note records the concrete candidate list and the machinery assembled to settle it.
:::

## The lattices as constructed

$$
T_{\Co} = \generators{2} \oplus E_{10}(2) = \generators{2}\oplus U(2)\oplus E_8(2),
\qquad
S_{\Co} = \generators{-2} \oplus E_{10}(2),
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

::: {.construction title="Term-by-term transport along the embedding chain"}

The same 18 vectors are transported term-by-term along the embedding chain $T_{\Co}\injects \ten\injects \tdp$:

- into $\ten = U \oplus U(2) \oplus E_8(2)$ by $h \mapsto e+f$;

- into $\tdp = U \oplus U(2) \oplus E_8^{\oplus 2}$ by $a_i \mapsto a_i + b_i$.

This yields a parallel norm and divisibility table across all three lattices, which is exactly the vector-by-vector form in which the Enriques-to-Coble cusp correspondence becomes checkable.
:::

::: {.remark title="Recorded gap: the numbers were not saved"}

The notebook cells that evaluate norm and divisibility on these vectors, in all three lattices, have their outputs **cleared**. The vectors and the method survive; the resulting numbers do not.
Re-running is the obvious first step, and is cheap: the lattices, the vectors and the helper are all in `init.sage`.
:::

## Orbit machinery available

::: {.remark title="Orbit representatives from sage-indefinite-port"}

The function `vector_orbit_representatives`, which `sage-indefinite-port` owns, computes orbit representatives of isotropic vectors for indefinite forms.
This is the tool that would settle the open orbit count directly, rather than by hand.
A raw trace of an earlier run on a rank-10 form with diagonal $(-4,-4,-4,-4,-2,-4,-4,-4,-4,-2)$ survives in the archived computational report; its two input Gram matrices are worth keeping even though the remaining 8800 lines are per-iteration bookkeeping.
:::

::: {.definition title="The isotropic trichotomy used as a separating invariant"}

`init.sage` provides `get_isotrop_type`, which classifies a primitive isotropic vector as **Odd**, **Even ordinary**, or **Even characteristic**, by testing $(v^\perp/v)^\perp$ against $U$, $U(2)$ and $I_{1,1}(2)$.
This trichotomy is what the cusp correspondence sections of this project rely on.
:::

## Sterk's five representatives, for comparison

In $\ten = U \oplus E_{10}(2)$ with $\omega = 2w_8$ (norm 4) and $\alpha = 2w_1$ (norm 8):
$$
\eta_1 = e,\quad \eta_2 = e',\quad \eta_3 = e'+f'+\omega,\quad \eta_4 = e'+2f'+\alpha,\quad \eta_5 = 2e+2f+\alpha,
$$
with the asserted invariants $\div(e)=1$ and $e^\perp/e \cong E_{10}(2) = \EnriquesInvariants$; $\div(e')=2$ and $e'^\perp/e' \cong U\oplus E_8(2) = (10,8,0)$; $\generators{e,e'}^\perp/\generators{e,e'} \cong E_8(2) = (8,8,0)$; and for $v' = 2e+2f+2w_1$, $\generators{e',v'}^\perp \cong (8,6,0)$.

Also recorded, from a separate OSCAR/Julia notebook, the $(r,a,\delta)$ invariants with printed discriminant forms: $U(2)\to(2,2,0)$, $U(2)\oplus E_8(2)\to\EnriquesInvariants$, $U^3\oplus E_8(2)\to(14,8,0)$, $U\oplus U(2)\oplus E_8^{\oplus2}\to(20,2,0)$, $U\oplus U(2)\oplus E_8(2)\to(12,10,0)$, $E_8(2)\to(8,8,0)$.
Here $\delta$ is computed as "some diagonal entry of the discriminant quadratic form is non-integral", citing AE22 Def.
2.3 for coparity.

Related: [[cusp-correspondence-morphism-chain|cusp-correspondence morphism chain]], [[computational-toolchain-and-recipe|computational toolchain and recipe]].
