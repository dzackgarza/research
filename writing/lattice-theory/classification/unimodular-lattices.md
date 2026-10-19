# Classification of unimodular lattices {#sec:unimodular-lattice-classification}

## Indefinite unimodular lattices {#sec-indefinite-unimodular-classification}

::: {.theorem #thm:indefinite-unimodular-classification title="Classification of indefinite unimodular lattices"}
Let $L\in\mathbf{Unimod}_{\bZ}$ be indefinite, with $\operatorname{sig}(L)=(p,q)$, where $p,q>0$ in the convention of @def:signature.

If $L$ is odd, there is an isometry
$$
L\isoto\latI_{p,q}
\definedas\generators{1}^{\perp p}\perp\generators{-1}^{\perp q}.
$$
If $L$ is even, the Brown invariant of its quadratic discriminant form is zero, and by @thm:milgram this forces $\signature{L}\equiv0\pmod8$. There is then an isometry
$$
L\isoto\latII_{p,q},
\qquad
\latII_{p,q}\definedas
\begin{cases}
U^{\perp p}\perp E_8^{\perp(q-p)/8}, &p<q,\\
U^{\perp p},&p=q,\\
U^{\perp q}\perp E_8(-1)^{\perp(p-q)/8},&p>q.
\end{cases}
$$
For each signature $(p,q)$ with $p,q>0$, there is exactly one odd unimodular isometry class; there is exactly one even unimodular isometry class if $\signature{L}\equiv0\pmod8$, and none otherwise [@Ser73, Ch. V; @MH73, Ch. II].
:::

::: {.proof}
The formulas for $\latI_{p,q}$ and $\latII_{p,q}$ exhibit unimodular integral lattices of the indicated signature and parity. Their uniqueness is the indefinite unimodular classification of [@Ser73, Ch. V; @MH73, Ch. II]. In the even case unimodularity gives $A_{L,q}=0$ by @def:discriminant, hence $\operatorname{Br}(A_{L,q})=0$ by @def:brown-invariant; applying @thm:milgram gives the asserted congruence. The displayed models realize every permitted signature.
:::

## Definite unimodular lattices {#sec-definite-unimodular-classification}

::: {.theorem #thm:definite-unimodular-class-numbers title="Class numbers of definite unimodular lattices"}
For each $n\ge1$, the isometry classes of positive-definite odd unimodular integral lattices of rank $n$ form the class set $\Cl(\latI_{n,0})$ of @def:genus. Even positive-definite unimodular lattices exist exactly when $8\mid n$; in rank $n=8k$ their isometry classes form $\Cl(E_8(-1)^{\perp k})$. The class numbers in ranks at most $24$ are recorded in @tbl-unimodular-definite-class-numbers. The odd, even, and total sequences are respectively [OEIS A054911](https://oeis.org/A054911), [OEIS A054909](https://oeis.org/A054909), and [OEIS A005134](https://oeis.org/A005134), in agreement with [@CS10, Chs. 16–18].


The rank-$8$ even lattice is $E_8(-1)$. In rank $16$ the even lattices are $E_8(-1)^{\perp2}$ and $D_{16}^+(-1)$. In rank $24$ the even lattices are the $24$ Niemeier lattices, distinguished by their root lattices, including the rootless Leech lattice [@CS10, Ch. 16].

Twisting by $(-1)$ identifies the positive- and negative-definite isometry classes, so the table gives the counts in either definite sign by the sign-twist equivalence of @def:form-twist.
:::

::: {.proof}
The class-set formulation is that of @def:genus: all positive-definite odd unimodular lattices of rank $n$ lie in the genus of $\latI_{n,0}$, and all positive-definite even unimodular lattices of rank $8k$ lie in the genus of $E_8(-1)^{\perp k}$ [@CS10, Chs. 15–16]. The divisibility $8\mid n$ follows from @thm:milgram; the classes in the table are the classical definite enumeration [@CS10, Chs. 16–18]. The even rank-$24$ classification is due to Niemeier; its $24$ classes are characterized by their root systems [@CS10, Ch. 16].
:::

::: {#tbl-unimodular-definite-class-numbers}

| Rank $n$ | Odd classes | Even classes | Total |
|:--|--:|--:|--:|
| $1\le n\le7$ | 1 | 0 | 1 |
| $8$ | 1 | 1 | 2 |
| $9\le n\le11$ | 2 | 0 | 2 |
| $12\le n\le13$ | 3 | 0 | 3 |
| $14$ | 4 | 0 | 4 |
| $15$ | 5 | 0 | 5 |
| $16$ | 6 | 2 | 8 |
| $17$ | 9 | 0 | 9 |
| $18$ | 13 | 0 | 13 |
| $19$ | 16 | 0 | 16 |
| $20$ | 28 | 0 | 28 |
| $21$ | 40 | 0 | 40 |
| $22$ | 68 | 0 | 68 |
| $23$ | 117 | 0 | 117 |
| $24$ | 273 | 24 | 297 |

Isometry-class numbers of positive-definite unimodular lattices, including the combined total [@CS10, Chs. 16–18].

:::

