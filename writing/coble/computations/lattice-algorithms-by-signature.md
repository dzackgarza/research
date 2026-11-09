---
unit: method
status: reusable
tags:
  - lattices
  - signature
  - subdiagrams
  - method
notes: |-
  Provenance: seven Coxeter-algorithm survey documents landed 2026-08-20, together with the archived isometry-search decomposition notes.
---

# Which lattice algorithms apply in which signature {#sec-lattice-algorithms-by-signature}


## The definite and indefinite cases

::: {.proposition #prop:vectors-of-given-square title="Vectors of a given square"}

1. Let $L$ be a definite lattice of rank $n$ with Gram matrix $G$ in a basis, let $\varepsilon = 1$ if $L$ is positive definite and $\varepsilon = -1$ if it is negative definite, and let $\lambda > 0$ be the smallest eigenvalue of $\varepsilon G$.
   Then for every $c\geq 0$
   $$
   \#\theset{v\in L : \varepsilon v^2 \leq c} \leq \left(2\sqrt{c/\lambda}+1\right)^{n} ,
   $$
   so the set $\theset{v\in L : v^2 = c}$ of vectors of square $c$ is finite for every $c\in\ZZ$.

2. In $U$ with $\beta_U(v,w) = x_1y_2+x_2y_1$ for $v = (x_1,x_2)$ and $w = (y_1,y_2)$, the vectors of square $0$ are $\theset{(x,0)}\union\theset{(0,y)}$, an infinite set.
:::

::: {.proof}

For (1), write $v = \sum_i x_ib_i$ in the basis.
Then $\varepsilon v^2 = x^{\mathsf T}(\varepsilon G)x \geq \lambda\, x^{\mathsf T}x$, so $\varepsilon v^2\leq c$ forces $\lvert x_i\rvert\leq\sqrt{c/\lambda}$ for each $i$.
Each $x_i$ is an integer in an interval of length $2\sqrt{c/\lambda}$, which holds at most $2\sqrt{c/\lambda}+1$ integers.
The vectors of square $c$ lie in the set with $\varepsilon v^2 \leq \lvert c\rvert$.

For (2), $v^2 = \beta_U(v,v) = 2x_1x_2$, which vanishes exactly when $x_1 = 0$ or $x_2 = 0$.
:::

::: {.proposition #prop:theta-series-convergence title="Theta series"}

Let $L$ be definite and let $\varepsilon$ be as in @prop:vectors-of-given-square.
The series $\Sum_{v\in L} q^{\varepsilon v^2}$ converges absolutely for $\lvert q\rvert < 1$, and its coefficient of $q^c$ is the number of vectors of square $\varepsilon c$.
For $L = U$ the coefficient of $q^0$ in $\Sum_{v\in U} q^{v^2}$ is infinite.
:::

::: {.proof}

Let $N(c)$ be the number of $v\in L$ with $\varepsilon v^2 = c$.
By @prop:vectors-of-given-square(1), $N(c)\leq(2\sqrt{c/\lambda}+1)^n$, a bound polynomial in $c$.
Hence $\Sum_{c\geq0} N(c)\lvert q\rvert^{c}$ converges for $\lvert q\rvert<1$, by the ratio test applied to the bound.
The statement for $U$ is @prop:vectors-of-given-square(2).
:::

::: {.proposition #prop:orthogonal-group-of-definite-lattice title="Orthogonal groups of a definite lattice and of $U$"}

1. If $L$ is definite, then $\Orth(L)$ is finite.

2. $\Orth(U)$ has order $4$: in the basis $e = (1,0)$, $f = (0,1)$ it consists of $\pm\mathrm{id}$ and $\pm\sigma$, where $\sigma$ exchanges $e$ and $f$.
:::

::: {.proof}

For (1), let $b_1,\dots,b_n$ be a basis of $L$ and let $c = \max_i \lvert b_i^2\rvert$.
An isometry $g$ maps each $b_i$ to a vector of the same square, so $g(b_i)$ lies in the finite set of @prop:vectors-of-given-square(1).
An isometry is determined by $g(b_1),\dots,g(b_n)$, so $\Orth(L)$ is finite.

For (2), the primitive vectors of square $0$ in $U$ are $\pm e$ and $\pm f$, by @prop:vectors-of-given-square(2).
An isometry permutes them and preserves $\beta_U(e,f) = 1$.
So $(g(e),g(f))$ is one of $(e,f)$, $(f,e)$, $(-e,-f)$, $(-f,-e)$, and each of these four assignments is an isometry.
:::

| Question | Definite $L$ | Indefinite $L$ |
| --- | --- | --- |
| Vectors of square $c$ | finite list | orbit representatives and group generators |
| Theta series | convergent for $\lvert q\rvert<1$ | coefficient of $q^0$ infinite for $U$ |
| $\Orth(L)$ | finite, by action on the vectors of a fixed square | order $4$ for $U$ (@prop:orthogonal-group-of-definite-lattice) |
| $W(L)$ | finite Weyl group | simple roots by Vinberg's algorithm |
| Isometry class | reduction and finite search | genus invariants and Nikulin's criteria [@Nik80] |
| Primitive embedding $L_1\injects L_2$ | finite search | genus criteria [@Nik80] |
| Finite covolume of $W(L)$ | vacuous | CoxIter certificate [@Gug15] |

## Deciding the type of a subdiagram

::: {.lemma #lem:subdiagram-type-integer-gram title="The type of a subdiagram is the signature of an integer matrix"}

Let $L$ be an integral lattice, let $\theset{r_i}_{i\in I}$ be simple roots of a Coxeter polytope with $r_i^2<0$, and suppose that $g_{ij}\leq 1$ for all $i\neq j$ in $I$, so that $\Sigma_I$ has a Coxeter matrix $M[I,I]$ with $g_{ij} = \cos(\pi/m_{ij})$ (@def:coxeter-vinberg-diagram).
Let $R_I = (r_i\cdot r_j)_{i,j\in I}$, an integer matrix.
Then $\operatorname{sig}(\RR^I, G[I,I]) = \operatorname{sig}(\QQ^I, R_I)$, and $G[I,I]$ and $R_I$ have the same connected components.
Hence the type of $\Sigma_I$ in @def:coxeter-system-type, and the type of the subdiagram in @def:elliptic-subdiagram, are determined by the signature over $\QQ$ of the integer matrix $R_I$, componentwise.
:::

::: {.proof}

Let $D = \operatorname{diag}(\lvert r_i^2\rvert)_{i\in I}$, a diagonal matrix with positive entries.
For $i\neq j$, $G[I,I]_{ij} = 2\cos(\pi/m_{ij}) = 2g_{ij}$ by @def:coxeter-gram-form and @def:coxeter-vinberg-diagram, so $r_i\cdot r_j = g_{ij}\sqrt{r_i^2r_j^2} = \tfrac12 G[I,I]_{ij}\sqrt{\lvert r_i^2\rvert\,\lvert r_j^2\rvert}$.
For $i = j$, $r_i^2 = -\lvert r_i^2\rvert = \tfrac12 G[I,I]_{ii}\,\lvert r_i^2\rvert$, since $G[I,I]_{ii} = -2$ (@def:coxeter-gram-form).
So $R_I = \tfrac12 D^{1/2}\, G[I,I]\, D^{1/2}$, a congruence by an invertible real matrix followed by a positive scalar.
Both preserve the signature by @thm:sylvester, and both preserve the zero pattern of the off-diagonal entries, hence the connected components.
Over $\QQ$, the form $R_I$ has an orthogonal basis (@thm:orthogonal-decomposition), and a $\QQ$-orthogonal basis is an $\RR$-orthogonal basis of $R_I\otimes\RR$, so the signature over $\QQ$ equals the signature over $\RR$.
:::

## Recognizing a lattice as a sum of standard blocks

::: {.construction #cons:decomposition-search title="Search over signature-additive multisets"}

Signature is additive over orthogonal direct sums, so a decomposition $L\cong\bigoplus_i L_i$ satisfies $\Sum_i (p_i,q_i) = (p,q)$ where $(p,q)$ is the signature of $L$.
Fixing a catalogue $\mathcal B$ of standard blocks, a decomposition of $L$ within $\mathcal B$ is found by

1. grouping $\mathcal B$ by signature;

2. enumerating the multisets of signatures from that grouping whose sum is $(p,q)$;

3. forming the direct sum of each choice of blocks realizing such a multiset;

4. testing each sum for isometry with $L$.

The catalogue $\mathcal B$ is $A_n$, $D_n$ and $E_n$ up to rank $20$, the odd and even unimodular lattices $I_{p,q}$ and $II_{p,q}$, and the $2$-twists of all of these.
The even unimodular lattices are indexed by the signatures with $p\equiv q \bmod 8$.
When $L$ and the sum are indefinite, even and $2$-elementary, step 4 is the comparison of signature, $a$ and $\delta$, by @thm:two-elementary-classification.
:::

Related: [Toolchain and recipe for a hyperbolic 2-elementary lattice](#sec-computational-toolchain-and-recipe), [Orbits of isotropic vectors and the Tits building of a cusp configuration](#sec-isotropic-orbits-and-tits-buildings), [CoxIter results for the Sterk cusps and the 0-cusp lattices](#sec-coxiter-results-for-cusp-lattices), [Open problems and technical gaps](#sec-open-problems).
