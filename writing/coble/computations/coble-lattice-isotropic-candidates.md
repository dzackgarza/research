---
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

::: {.remark title="The open problem"}

The enumeration of $\Gamma_{\Co}$-orbits of primitive isotropic vectors in $T_{\Co}$ is open ([Open problems](#sec-open-problems)), and so is the uniqueness of the $\discriminantkernel{T}$-orbit in divisibility $2$, which the proof of @lem:divisibilityTcoOne assumes.
This section lists candidate representatives.
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

## The images under the embedding chain

::: {.construction title="Term-by-term transport along the embedding chain"}

The same 18 vectors are mapped term-by-term along the embedding chain $T_{\Co}\injects \ten\injects \tdp$:

- into $\ten = U \oplus U(2) \oplus E_8(2)$ by $h \mapsto e+f$;

- into $\tdp = U \oplus U(2) \oplus E_8^{\oplus 2}$ by $a_i \mapsto a_i + b_i$.

This yields a parallel norm and divisibility table across all three lattices, which is exactly the vector-by-vector form in which the Enriques-to-Coble cusp correspondence becomes checkable.
:::

## Orbit machinery available

::: {.remark title="Orbit representatives from sage-indefinite-port"}

The function `vector_orbit_representatives` of `sage-indefinite-port` computes orbit representatives of isotropic vectors for indefinite forms.
Applied to $T_\Co$, it computes the open orbit count.
:::

::: {.definition title="The isotropic trichotomy used as a separating invariant"}

A primitive isotropic vector is classified as **Odd**, **Even ordinary**, or **Even characteristic**, by testing $(v^\perp/v)^\perp$ against $U$, $U(2)$ and $I_{1,1}(2)$.
The cusp correspondence sections use this trichotomy.
:::

## Sterk's five representatives, for comparison

In $\ten = U \oplus E_{10}(2)$ with $\omega = 2w_8$ (norm 4) and $\alpha = 2w_1$ (norm 8):
$$
\eta_1 = e,\quad \eta_2 = e',\quad \eta_3 = e'+f'+\omega,\quad \eta_4 = e'+2f'+\alpha,\quad \eta_5 = 2e+2f+\alpha,
$$
with the invariants $\div(e)=1$ and $e^\perp/e \cong E_{10}(2) = \EnriquesInvariants$; $\div(e')=2$ and $e'^\perp/e' \cong U\oplus E_8(2) = (10,8,0)$; $\generators{e,e'}^\perp/\generators{e,e'} \cong E_8(2) = (8,8,0)$; and for $v' = 2e+2f+2w_1$, $\generators{e',v'}^\perp \cong (8,6,0)$.

The $(r,a,\delta)$ invariants of further lattices are $U(2)\to(2,2,0)$, $U(2)\oplus E_8(2)\to\EnriquesInvariants$, $U^3\oplus E_8(2)\to(14,8,0)$, $U\oplus U(2)\oplus E_8^{\oplus2}\to(20,2,0)$, $U\oplus U(2)\oplus E_8(2)\to(12,10,0)$, $E_8(2)\to(8,8,0)$.
Here $\delta = 1$ when some diagonal entry of the discriminant quadratic form, in a basis of $A_L$, is non-integral, and $\delta = 0$ otherwise [@AE22, Def. 2.3].

Related: [cusp-correspondence morphism chain](#sec-cusp-correspondence-morphism-chain), [computational toolchain and recipe](#sec-computational-toolchain-and-recipe).
