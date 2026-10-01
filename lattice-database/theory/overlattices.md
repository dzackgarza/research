---
title: Overlattices and the genus symbol
summary: Integral overlattices of a lattice, counted through the discriminant form, and the genus symbol.
order: 5
---

Let $L$ be an [integral](lattices.html#integral) lattice that is [nondegenerate](lattices.html#degenerate), with [discriminant group](discriminant-forms.html#discriminant-group) $A_L \cong L^*/L$ and discriminant form $b_{A_L}$.

## Integral overlattices {#overlattices}

::: {.definition}
An *integral overlattice* of $L$ is an integral lattice $M$ with $L \subseteq M \subseteq L^*$.
:::

::: {.proposition}
$M \mapsto M/L$ is a bijection from the integral overlattices to the subgroups $H$ of $A_L$ with $b_{A_L}(H, H) = 0$.
:::

::: {.example}
An even $L$ can have odd overlattices: for $L = \langle 4 \rangle = \mathbb{Z}v$, $M = \mathbb{Z}\tfrac{v}{2} \cong \langle 1 \rangle$.
:::

The page states the number of integral overlattices, with $M = L$ counted.
Each subgroup $H$ counts once, so overlattices that are isometric to each other count separately.
The number is stated when $A_L$ has at most 100000 subgroups; otherwise it is [not decided](records.html#not-decided).

## Genus symbol {#genus-symbol}

::: {.definition}
The genus symbol of $L$ is $\mathrm{I}$ when $L$ is odd and $\mathrm{II}$ when $L$ is even, with the signature as subscript, such as $\mathrm{II}_{1,9}$.
When the determinant is not $1$ or $-1$, the local symbol at each prime that divides twice the determinant follows in parentheses, in the notation that SageMath prints.
:::

## Class number of the genus {#class-number}

::: {.definition}
Two lattices are in the same *genus* when they have the same signature and $L \otimes \mathbb{Z}_p \cong L' \otimes \mathbb{Z}_p$ for every prime $p$.
The *class number* of the genus of $L$ is the number of isometry classes of lattices in that genus, the class of $L$ counted.
:::

The page states the class number when the record has it.
It is computed with `Genus(G).representatives()` of SageMath.

## Spinor genera {#spinor-genera}

::: {.definition}
Let $L$ and $M$ be in the same genus, of rank at least 3, with determinant $d$.
There are lattices in their isometry classes with $[L : L \cap M] = [M : L \cap M] = r$ for an integer $r$ prime to $2d$.
$L$ and $M$ are in the same *spinor genus* when the spinor operator $\Delta(r)$ is in the spinor kernel (Conway and Sloane, *Sphere Packings, Lattices and Groups*, 3rd edition, Chapter 15, §9.2–§9.4, Theorems 15–17). The database counts spinor genera up to isometry, proper or improper: the spinor kernel is enlarged by the spinor operator of one improper isometry, so that each spinor genus is a union of isometry classes.
:::

A genus is partitioned into spinor genera, and their number is a power of 2 (Conway and Sloane, Chapter 15, §9.1). The record states that number as `spinor_genus_count`, computed with `Genus(G).spinor_generators(proper=False)` of SageMath.

The record states the partition of the class number as `spinor_genera`: the number of isometry classes in the spinor genus of $L$, then the number in each other spinor genus, in decreasing order.
The first entry is the *spinor class number* of $L$, and the sum is the class number of the genus.

For an indefinite lattice of rank at least 3, a spinor genus contains exactly one isometry class (Eichler; Conway and Sloane, Chapter 15, Theorem 14), so every entry is $1$ and the class number equals the number of spinor genera.
For a definite lattice the class number and the number of spinor genera do not determine the partition: the genus of $\langle 1 \rangle \oplus \langle 4 \rangle \oplus \langle 64 \rangle$ has three classes in two spinor genera.
`latticedb certify` finds the classes of each spinor genus by Kneser's neighbour method at a prime $p$ whose spinor operator is in the kernel, which stays in one spinor genus, and checks that the sum of $1/|O(M)|$ over all classes found equals the mass of the genus.

## Hyperbolic index {#hyperbolic-index}

::: {.definition}
Let $U$ be the hyperbolic plane, with Gram matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
The *hyperbolic index* of a nondegenerate integral lattice $L$ is the largest $n \geq 0$ with $L \cong U^n \oplus L'$ for a lattice $L'$.
:::

::: {.proposition}
Let $L$ be integral and let $M \subseteq L$ be a unimodular sublattice.
Then $L = M \oplus M^{\perp}$.
So the hyperbolic index of $L$ is also the largest $n$ with an embedding $U^n \hookrightarrow L$.
:::

::: {.proof}
For $x \in L$, the map $y \mapsto b(x, y)$ on $M$ takes integer values.
Because $M$ is unimodular, this map is $b(m, \cdot)$ for one $m \in M$, and then $x - m \in M^{\perp}$.
So $L = M + M^{\perp}$, and $M \cap M^{\perp} = 0$ because $b$ is nondegenerate on $M$.
:::

So an embedding of $U^n$ into an integral lattice is primitive, and $L$ is never a proper overlattice of $U^n \oplus (U^n)^{\perp}$.
The proposition requires $L$ integral: $U \subseteq U(\tfrac{1}{2})$ has index 2, and $U(\tfrac{1}{2})$ has no summand $U$.

::: {.theorem data-name="Kneser"}
An indefinite lattice $S$ of rank at least 3 is alone in its genus when, for each odd prime $p$, $S \otimes \mathbb{Z}_p$ has two orthogonal summands of rank 1 and the same scale, and $S \otimes \mathbb{Z}_2$ has a summand $U(2^k)$ or one of two other forms that the theorem lists ([Nikulin 1980](https://doi.org/10.1070/IM1980v014n01ABEH001060): V. V. Nikulin, *Integral symmetric bilinear forms and some of their applications*, Math.
USSR-Izv.
14 (1980), 103–167, Theorem 1.13.1*).
:::

A lattice $U \oplus L'$ of rank at least 3 satisfies these conditions with $k = 0$.
A lattice in the genus of $U$ is even, unimodular and binary with determinant $-1$, so it has a primitive isotropic vector $e$; unimodularity gives $f$ with $b(e, f) = 1$, so it contains a copy of $U$, which is all of it by the proposition.
So $L \cong U^n \oplus L'$ for some $L'$ exactly when the genus of $L$ is the sum of the genus of $U^n$ and a genus of signature $(n_+ - n, n_- - n)$, and the hyperbolic index depends only on the genus of $L$.
`latticedb certify` computes it so: for $n$ from $\min(n_+, n_-)$ down to 1, it searches the genera of that signature with determinant $(-1)^n \det L$ and the parity of $L$, with `genera` and `Genus.direct_sum` of SageMath.
A definite lattice has hyperbolic index 0.

A morphism file that embeds $U^n$ into $L$ is a lower bound $n$ for the hyperbolic index of $L$.
`latticedb check` refuses a stored hyperbolic index that is less than such a bound, and the page of a lattice without a stored value states the bound.
