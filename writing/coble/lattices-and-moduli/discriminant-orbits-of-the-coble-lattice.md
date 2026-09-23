# Discriminant orbits of the Coble lattice {#sec:discriminant-orbits}

::: {.Remark}

The Coble period lattice $T_\Co = \gens{2}\oplus E_{10}(2)$ is the twist by $2$ of
an odd unimodular lattice, and this single fact controls both its isometry group
and its discriminant form.
We compute the discriminant quadratic form $(A_{T_\Co}, q_{T_\Co})$ explicitly,
determine its isometry group and the decomposition of its isotropic classes into
orbits, and record the bridge between that finite datum and the primitive
isotropic vectors of $T_\Co$ themselves.
Throughout we use the discriminant apparatus of [the discriminant-form definition](#def:discriminant-forms)
and the invariant triple $(r, a, \delta)$ of the Lattice Theory section.
:::

## The Coble lattice as a twist

::: {.Proposition #prop:tco-as-twist}
### $T_\Co$ is a twisted odd unimodular lattice

Set
$$
B \da \gens{1}\oplus E_{10} = \gens{1}\oplus U\oplus E_8
.
$$
Then $B$ is odd and unimodular of signature $(2,9)$, so $B\cong\latI_{2,9}$, and
$$
T_\Co = \gens{2}\oplus E_{10}(2) = B(2) \cong \latI_{2,9}(2)
.
$$
Consequently $\Orth(T_\Co) = \Orth(B)$ as subgroups of $\GL(B)$, and a vector of
$T_\Co$ is isotropic, respectively primitive, exactly when it is isotropic,
respectively primitive, as a vector of $B$.
:::

::: {.proof}

The lattice $E_{10} = U\oplus E_8$ is even and unimodular of signature $(1,9)$
([the Enriques-lattice definition](#def:enriques-lattice)), so $B = \gens{1}\oplus E_{10}$ is unimodular of
signature $(2,9)$ and is odd because the generator of $\gens{1}$ has norm $1$.
By the classification of indefinite unimodular lattices
([the indefinite unimodular classification](#thm:indefinite-unimodular-classification)) an odd unimodular lattice of
signature $(2,9)$ is isometric to $\latI_{2,9}$.
Twisting distributes over orthogonal direct sums and $\gens{1}(2) = \gens{2}$,
whence $B(2) = \gens{2}\oplus E_{10}(2) = T_\Co$.

A twist leaves the underlying $\ZZ$-module unchanged and multiplies the form by
a nonzero scalar, so an automorphism of the module preserves $\beta_B$ if and
only if it preserves $2\beta_B = \beta_{B(2)}$; this gives
$\Orth(T_\Co) = \Orth(B)$.
The same scaling shows $\beta_{T_\Co}(v,v) = 2\beta_B(v,v)$ vanishes exactly when
$\beta_B(v,v)$ does, and primitivity is a property of the module alone.
:::

::: {.Remark}

The presentation $T_\Co\cong\latI_{2,9}(2)$ is the one recorded in
[the K3-cover invariants remark](#rmk:k3-cover-invariants), and it is the form in which the divisibility
computation of [the divisibility lemma](#lem:divisibilityAlwaysTwoTco) is carried out.
Applying [the indefinite unimodular classification](#thm:indefinite-unimodular-classification) once more to
$U\oplus U\oplus\latI_{0,7}$, which is odd unimodular of signature $(2,9)$, gives
the further presentation
$$
T_\Co \cong U(2)^{\oplus 2}\oplus\gens{-2}^{\oplus 7}
= U(2)^{\oplus 2}\oplus A_1^{\oplus 7}
,
$$
in which the Witt index $2$ and the negative-definite rank-$7$ complement of a
maximal isotropic subspace are visible in the presentation itself.
:::

::: {.Proposition #prop:tco-split-maximal}
### $T_\Co$ is the twist of a split maximal lattice

The lattice $B\cong\latI_{2,9}$ of [the twist proposition](#prop:tco-as-twist) is maximal in the
sense of [the maximal-lattice definition](#def:maximal-lattice) and split in the sense of
[the split-maximal definition](#def:split-maximal):
$$
B \cong U\oplus U\oplus\latI_{0,7}
.
$$
In a decomposition $T_\Co = B(2)$ with $B = U\oplus U\oplus\latI_{0,7}$, an
isotropic generator $e$ of one hyperbolic summand and the plane $J$ spanned by
isotropic generators of both have
$$
e^{\perp}/e \cong \latI_{1,8}(2) = (9,9,1)_1,
\qquad
J^{\perp}/J \cong \latI_{0,7}(2) \cong A_1^{\oplus 7} = (7,7,1)_0
.
$$
:::

::: {.proof}

$B$ is unimodular, hence maximal by [the maximal-overlattice lemma](#lem:maximal-overlattice-exists).
The lattice $U\oplus U\oplus\latI_{0,7}$ is unimodular of signature $(2,9)$ and
odd, because $\latI_{0,7}$ is, so it is isometric to $\latI_{2,9}\cong B$ by
[the indefinite unimodular classification](#thm:indefinite-unimodular-classification); this exhibits $B$ in the shape
required by [the split-maximal definition](#def:split-maximal), as [the maximal-splitting theorem](#thm:maximal-splits-for-large-n)
also predicts for $n = 9\geq 5$.
For the quotients, take $e$ to be an isotropic generator of the first hyperbolic
summand of $B\cong U\oplus U\oplus\latI_{0,7}$; then $e^{\perp B} = \ZZ e\oplus
U\oplus\latI_{0,7}$ and $e^{\perp}/e\cong U\oplus\latI_{0,7}\cong\latI_{1,8}$,
which is odd unimodular of signature $(1,8)$.
Taking $J$ to be spanned by isotropic generators of the two hyperbolic summands
gives $J^{\perp B} = J\oplus\latI_{0,7}$ and $J^{\perp}/J\cong\latI_{0,7}$.
Twisting by $2$ and reading off invariants gives $\latI_{1,8}(2) = (9,9,1)$ of
signature $(1,8)$ and $\latI_{0,7}(2) = \gens{-2}^{\oplus 7} = (7,7,1)$ of
signature $(0,7)$.
:::

::: {.Remark}

Since $\Orth^+(T_\Co) = \Orth^+(B)$ and both isotropy and primitivity are
unchanged by the twist, [the split-maximal proposition](#prop:tco-split-maximal) places $T_\Co$ under
[the split-maximal isotropic transitivity theorem](#thm:split-maximal-isotropic-transitivity): this is the mechanism behind
[the unpolarized-cusp theorem](#theorem-unpolarized-cusps), and the computation above identifies the two
boundary lattices there with the Coble cusp invariants $(9,9,1)_1$ and
$(7,7,1)_0$ used in the cusp correspondence.
The $1$-cusp lattice $\latI_{0,7}(2)\cong A_1^{\oplus 7}$ is negative definite of
rank $7$, consistent with Witt index $2$ in signature $(2,9)$: $11 - 2\cdot 2 = 7$.
:::

## The discriminant form of a twisted unimodular lattice

::: {.Proposition #prop:twisted-unimodular-discriminant}
### Discriminant form of $M(2)$ for $M$ unimodular

Let $M$ be a unimodular lattice of rank $r$ and let $L\da M(2)$.
Then
$$
L\dual = \tfrac{1}{2}M,
\qquad
A_L = \tfrac{1}{2}M/M \cong M/2M \cong (\ZZ/2\ZZ)^r
,
$$
so $L$ is $2$-elementary with $a = r$, and the discriminant quadratic form is
$$
q_L\!\left(\tfrac{1}{2}x + L\right) = \tfrac{1}{2}\,\beta_M(x, x) \bmod 2\ZZ,
\qquad x\in M
.
$$
In particular the class of $\tfrac{1}{2}x$ is isotropic for $q_L$ if and only if
$$
\beta_M(x, x)\equiv 0 \pmod 4
.
$$
:::

::: {.proof}

Under the geometric identification of the dual lattice
([the geometric dual-lattice identification](#thm:dual-geometric-identification)), $L\dual$ is the set of $v\in M_\QQ$
with $2\beta_M(v, M)\containedin\ZZ$, that is $\beta_M(v, M)\containedin\tfrac12\ZZ$.
Since $M$ is unimodular the map $M\to M\dual$ is an isomorphism, so this set is
exactly $\tfrac12 M$.
The quotient $\tfrac12 M/M$ is carried isomorphically to $M/2M$ by multiplication
by $2$, giving $A_L\cong(\ZZ/2\ZZ)^r$ and $a = r$.
For the form, $\beta_L = 2\beta_M$ gives
$$
q_L\!\left(\tfrac12 x + L\right)
= \beta_L\!\left(\tfrac12 x, \tfrac12 x\right)
= 2\cdot\tfrac14\beta_M(x, x)
= \tfrac12\beta_M(x, x) \bmod 2\ZZ
,
$$
and this vanishes in $\QQ/2\ZZ$ precisely when $\beta_M(x,x)\in 4\ZZ$.
:::

::: {.Definition #def:coble-mod-four-form}
### The mod-$4$ norm on $B/2B$

For $B = \gens{1}\oplus E_{10}$ as in [the twist proposition](#prop:tco-as-twist), define
$$
\begin{aligned}
Q: B/2B &\to \ZZ/4\ZZ \\
x + 2B &\mapsto \beta_B(x, x) \bmod 4
.
\end{aligned}
$$
This is well defined, since $\beta_B(x + 2z, x + 2z) = \beta_B(x,x) + 4\beta_B(x,z)
+ 4\beta_B(z,z)$.
Under the identification $A_{T_\Co}\cong B/2B$ of
[the twisted-unimodular discriminant proposition](#prop:twisted-unimodular-discriminant) one has $q_{T_\Co} = \tfrac12 Q$, so
$Q$ and $q_{T_\Co}$ have the same fibers and
$\Orth(A_{T_\Co}, q_{T_\Co})$ is the stabilizer in $\GL(B/2B)$ of the four fibers
of $Q$.
:::

::: {.Proposition #prop:coble-q-fibers}
### The fibers of $Q$

The four fibers of $Q$ on the $2^{11} = 2048$ classes of $B/2B$ have cardinalities
$$
\abs{Q\inv(0)} = 528,\quad
\abs{Q\inv(1)} = 528,\quad
\abs{Q\inv(2)} = 496,\quad
\abs{Q\inv(3)} = 496
.
$$
In particular $A_{T_\Co}$ contains exactly $528$ isotropic classes, of which $527$
are nonzero.
:::

::: {.proof}

Write $B = \gens{v}\oplus E_{10}$ with $v^2 = 1$ and let $x = \varepsilon v + y$
represent a class of $B/2B$, with $\varepsilon\in\ts{0,1}$ and $y$ ranging over
$E_{10}/2E_{10}$.
Then $\beta_B(x,x) = \varepsilon + \beta_{E_{10}}(y,y)$, and since $E_{10}$ is
even the value $\beta_{E_{10}}(y,y)$ is $\equiv 0$ or $2 \pmod 4$.
Hence $Q$ takes the value $0$ or $2$ on the classes with $\varepsilon = 0$ and the
value $1$ or $3$ on those with $\varepsilon = 1$, and in both cases the split is
governed by the single count
$$
N_0 \da \#\ts{ y\in E_{10}/2E_{10} \mid \beta_{E_{10}}(y,y)\equiv 0 \pmod 4 }
.
$$
The four fibers then have sizes $N_0,\ N_0,\ 2^{10} - N_0,\ 2^{10} - N_0$ in the
order listed.

To compute $N_0$, observe that $\bar q(y)\da\tfrac12\beta_{E_{10}}(y,y)\bmod 2$ is a
quadratic form $E_{10}/2E_{10}\to\bF_2$ whose polar form is the reduction of
$\beta_{E_{10}}$ modulo $2$; the latter is nondegenerate because $E_{10}$ is
unimodular.
Thus $\bar q$ is a nondegenerate quadratic form on a $10$-dimensional
$\bF_2$-vector space, and $N_0 = \#\bar q\inv(0)$.
The decomposition $E_{10} = U\oplus E_8$ splits $\bar q$ orthogonally.
On $U/2U$ the form is $\bar q(ae + bf) = ab$, which is the hyperbolic plane over
$\bF_2$ and has $3$ zeros; on $E_8/2E_8$ the form is the reduction of the $E_8$
form and has $136$ zeros.
Both are of plus type, hence so is their sum, and a nondegenerate plus-type form
in dimension $2n$ over $\bF_2$ has $2^{2n-1} + 2^{n-1}$ zeros.
With $n = 5$ this gives
$$
N_0 = 2^{9} + 2^{4} = 512 + 16 = 528
,
$$
in agreement with the two summand counts $3\cdot 136 + 1\cdot 120 = 528$.
The remaining fiber sizes are $2^{10} - 528 = 496$.
:::

::: {.Remark}

The counts $\#A_{E_{10}(2)} = 1024$, $\#I^0 = 528$ and $\#I^1 = 496$ tabulated in
the reference tables are exactly the numbers $2^{10}$, $N_0$ and $2^{10} - N_0$
appearing in this proof, and the summand counts $\#I^0(U(2)) = 3$,
$\#I^0(E_8(2)) = 136$ are the two zero-counts used to identify the type.
The isotropic classes of $A_{T_\Co}$ and of $A_{E_{10}(2)}$ therefore coincide as
sets: a class $\varepsilon\bar v + \bar y$ is isotropic only if $\varepsilon = 0$,
because $q_{T_\Co}(\bar v) = \tfrac12\notin\ZZ$ while $q_{E_{10}(2)}$ is
$\ZZ$-valued.
This is the invariant $\delta = 1$ of $T_\Co$ read off from a distinguished class.
:::

## The isometry group of the discriminant form

::: {.Proposition #prop:coble-discriminant-group}
### $\Orth(q_{T_\Co})$ is the discriminant group of $E_{10}(2)$

Restriction to the subgroup
$$
A^0 \da \ts{ x\in A_{T_\Co} \mid q_{T_\Co}(x)\in\ZZ/2\ZZ } \cong A_{E_{10}(2)}
$$
of index $2$ induces an isomorphism
$$
\Orth(A_{T_\Co}, q_{T_\Co}) \iso \Orth(A_{E_{10}(2)}, q_{E_{10}(2)})
,
$$
and hence
$$
\abs{\Orth(A_{T_\Co}, q_{T_\Co})} = 2^{21}\cdot 3^5\cdot 5^2\cdot 7\cdot 17\cdot 31
= 46\,998\,591\,897\,600
.
$$
:::

::: {.proof}

Write $A_{T_\Co} = \ZZ\bar h\oplus A_{E_{10}(2)}$ with $\bar h$ the class of
$\tfrac12 h$ for $h$ the generator of $\gens{2}$, so that
$q_{T_\Co}(\bar h) = \tfrac12$ and $\bar h$ is orthogonal to $A_{E_{10}(2)}$ for
the discriminant bilinear form.
Since $q_{E_{10}(2)}$ is $\ZZ$-valued, $A^0 = A_{E_{10}(2)}$, and $A^0$ is
intrinsically defined by $q_{T_\Co}$, hence preserved by every isometry.
Restriction therefore gives a homomorphism
$\rho\colon\Orth(A_{T_\Co}, q_{T_\Co})\to\Orth(A^0, q_{T_\Co}|_{A^0})$.

$\rho$ is injective.
If $g$ restricts to the identity on $A^0$ then $g(\bar h) = \bar h + z$ for some
$z\in A^0$, and preservation of the bilinear form gives
$b(z, y) = b(g\bar h, y) - b(\bar h, y) = 0$ for every $y\in A^0$; the form
$q_{E_{10}(2)}$ is nondegenerate ([the discriminant nondegeneracy proposition](#prop:discriminant-nondegenerate)), so
$z = 0$.

$\rho$ is surjective.
Given $g_0\in\Orth(A^0)$, extend it by $\bar h\mapsto\bar h$; the extension
preserves $q_{T_\Co}$ because the decomposition
$A_{T_\Co} = \ZZ\bar h\perp A^0$ is orthogonal.

The order of $\Orth(A_{E_{10}(2)}, q_{E_{10}(2)})$ is the one recorded in the
reference tables.
:::

::: {.Theorem #thm:coble-isotropic-class-orbits}
### Two orbits of isotropic classes

The group $\Orth(A_{T_\Co}, q_{T_\Co})$ has exactly two orbits on the $528$
isotropic classes of $A_{T_\Co}$: the zero class, and the set of all $527$ nonzero
isotropic classes.
:::

::: {.proof}

By [the Coble discriminant-group proposition](#prop:coble-discriminant-group) the action is that of
$\Orth(A_{E_{10}(2)}, q_{E_{10}(2)})$ on the singular vectors of the
nondegenerate plus-type quadratic form $\bar q$ on the $10$-dimensional
$\bF_2$-space $E_{10}/2E_{10}$ identified in the proof of
[the fiber-count proposition](#prop:coble-q-fibers).
Witt's extension theorem for nondegenerate quadratic forms over a field states
that an isometry between subspaces extends to the whole space; applied to the
lines spanned by two nonzero singular vectors it shows that the orthogonal group
is transitive on nonzero singular vectors.
The zero class is fixed, and by [the fiber-count proposition](#prop:coble-q-fibers) there are
$528 - 1 = 527$ nonzero singular vectors.
:::

## From discriminant classes to lattice vectors

::: {.Proposition #prop:coble-primitive-isotropic-classes}
### Primitive isotropic vectors and their discriminant classes

Every primitive isotropic $v\in T_\Co$ has $\di_{T_\Co}(v) = 2$, and its
associated class
$$
v^* \da \tfrac{1}{2}v + T_\Co \in A_{T_\Co}
$$
is a nonzero isotropic class.
All such classes lie in the single nonzero orbit of
[the isotropic-class orbit theorem](#thm:coble-isotropic-class-orbits).
:::

::: {.proof}

The divisibility statement is [the divisibility lemma](#lem:divisibilityAlwaysTwoTco), and $v^*$ has
order $\di_{T_\Co}(v) = 2$ in $A_{T_\Co}$ ([the discriminant-form definition](#def:discriminant-forms) and the
divisibility conventions of the Lattice Theory section), so $v^*\neq 0$.
Writing $v\in B$ and using $\beta_{T_\Co} = 2\beta_B$, isotropy of $v$ gives
$\beta_B(v,v) = 0$, hence $Q(v) = 0$ and $q_{T_\Co}(v^*) = 0$ by
[the twisted-unimodular discriminant proposition](#prop:twisted-unimodular-discriminant).
The final assertion is [the isotropic-class orbit theorem](#thm:coble-isotropic-class-orbits), which has a single
orbit of nonzero isotropic classes.
:::

::: {.Remark}
### What the finite orbit count does and does not determine

For the full orthogonal group the lattice-level statement is stronger than the
finite one: $\Orth^+(T_\Co)$ is transitive on primitive isotropic vectors and on
primitive isotropic planes, with the quotients $e^{\perp}/e\cong\latI_{1,8}(2)$
and $J^{\perp}/J\cong\latI_{0,7}(2)\cong A_1^{\oplus 7}$
([the unpolarized-cusp theorem](#theorem-unpolarized-cusps)), and
[the primitive-isotropic-class proposition](#prop:coble-primitive-isotropic-classes) then places every primitive
isotropic vector in the single nonzero orbit of
[the isotropic-class orbit theorem](#thm:coble-isotropic-class-orbits).

For a subgroup $\Gamma\leq\Orth(T_\Co)$ the passage runs the other way and is not
automatic.
The reduction map sends $\Gamma$-orbits of primitive isotropic vectors to
$\rho(\Gamma)$-orbits of nonzero isotropic classes, but the integral parabolic
stabilizer can have proper image in the finite stabilizer, so a finite orbit may
split.
The $\Gamma_{\En,2}$-induced orbit decomposition of the $528$ isotropic classes is
computed in [the Coble Heegner finite-orbit theorem](#thm:coble-heegner-finite-orbits), and the lift of that finite
decomposition to primitive isotropic vectors of $T_\Co$ is open.
:::

## The Eichler criterion and its hypothesis

::: {.Remark}
### Why the Eichler criterion is unavailable for $T_\Co$

The Eichler criterion ([the Eichler criterion](#thm:eichler-criterion)) reduces
$\widetilde{\SO}^+(L)$-equivalence of primitive vectors to the pair
$(v^2, v^*\bmod L)$, but only for lattices containing $U^{\oplus 2}$.
That hypothesis fails for $T_\Co$: by [the twist proposition](#prop:tco-as-twist) every value of
$\beta_{T_\Co}$ is even, so no two vectors of $T_\Co$ pair to $1$ and $T_\Co$
contains no copy of $U$ at all, let alone two; the remark following
[the Eichler criterion](#thm:eichler-criterion) records the same obstruction for $S_\Co$ and
$S_\En$.
An orbit statement for $T_\Co$ therefore needs a different mechanism.
Two are available: the transitivity of [the unpolarized-cusp theorem](#theorem-unpolarized-cusps) for the
full orthogonal group, resting on [the split-maximal proposition](#prop:tco-split-maximal), and the
algorithms of [@Daw22] for a subgroup specified by its image in $\Orth(q)$.
:::
