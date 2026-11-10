# Discriminant orbits of the Coble lattice {#sec-discriminant-orbits}

## The Coble lattice as a twist

::: {.proposition #prop:tco-as-twist title="$T_\Co$ is a twisted odd unimodular lattice"}

Set
$$
B \definedas \generators{1}\oplus E_{10} = \generators{1}\oplus U\oplus E_8
.
$$
Then $B$ is odd and unimodular of signature $(2,9)$, so $B\cong\latI_{2,9}$, and
$$
T_\Co = \generators{2}\oplus E_{10}(2) = B(2) \cong \latI_{2,9}(2)
.
$$
Consequently $\Orth(T_\Co) = \Orth(B)$ as subgroups of $\GL(B)$, and a vector of $T_\Co$ is isotropic, respectively primitive, exactly when it is isotropic, respectively primitive, as a vector of $B$.
:::

::: {.proof}

By @def:enriques-lattice, the lattice $E_{10} = U\oplus E_8$ is even and unimodular of signature $(1,9)$, so $B = \generators{1}\oplus E_{10}$ is unimodular of signature $(2,9)$ and is odd because the basis vector of $\generators{1}$ has norm $1$.
By @thm:indefinite-unimodular-classification, an odd unimodular lattice of signature $(2,9)$ is isometric to $\latI_{2,9}$.
Twisting distributes over orthogonal direct sums and $\generators{1}(2) = \generators{2}$, whence $B(2) = \generators{2}\oplus E_{10}(2) = T_\Co$.

A twist leaves the underlying $\ZZ$-module unchanged and multiplies the form by a nonzero scalar, so an automorphism of the module preserves $\beta_B$ if and only if it preserves $2\beta_B = \beta_{B(2)}$; this gives $\Orth(T_\Co) = \Orth(B)$.
The same scaling shows $\beta_{T_\Co}(v,v) = 2\beta_B(v,v)$ vanishes exactly when $\beta_B(v,v)$ does, and primitivity is a property of the module alone.
:::

::: {.proposition #prop:tco-split-maximal title="$T_\Co$ is the twist of a split maximal lattice"}

The lattice $B\cong\latI_{2,9}$ of @prop:tco-as-twist is maximal in the sense of @def:maximal-lattice and split in the sense of @def:split-maximal:
$$
B \cong U\oplus U\oplus\latI_{0,7},
\qquad\text{hence}\qquad
T_\Co \cong U(2)^{\oplus 2}\oplus\latI_{0,7}(2) = U(2)^{\oplus 2}\oplus A_1^{\oplus 7}
.
$$
In a decomposition $T_\Co = B(2)$ with $B = U\oplus U\oplus\latI_{0,7}$, an isotropic basis vector $e$ of one hyperbolic summand and the plane $J$ spanned by isotropic basis vectors of both have
$$
e^{\perp}/e \cong \latI_{1,8}(2) = (9,9,1)_1,
\qquad
J^{\perp}/J \cong \latI_{0,7}(2) \cong A_1^{\oplus 7} = (7,7,1)_0
.
$$
:::

::: {.proof}

$B$ is unimodular, hence maximal by @lem:maximal-overlattice-exists.
The lattice $U\oplus U\oplus\latI_{0,7}$ is unimodular of signature $(2,9)$ and odd, because $\latI_{0,7}$ is, so it is isometric to $\latI_{2,9}\cong B$ by @thm:indefinite-unimodular-classification; this exhibits $B$ in the shape required by @def:split-maximal.
Twisting this isometry by $2$ gives the decomposition of $T_\Co = B(2)$, with $\latI_{0,7}(2) = \generators{-2}^{\oplus 7} = A_1^{\oplus 7}$.
For the quotients, take $e$ to be an isotropic basis vector of the first hyperbolic summand of $B\cong U\oplus U\oplus\latI_{0,7}$; then $e^{\perp B} = \ZZ e\oplus U\oplus\latI_{0,7}$ and $e^{\perp}/e\cong U\oplus\latI_{0,7}\cong\latI_{1,8}$, which is odd unimodular of signature $(1,8)$.
Taking $J$ to be spanned by isotropic basis vectors of the two hyperbolic summands gives $J^{\perp B} = J\oplus\latI_{0,7}$ and $J^{\perp}/J\cong\latI_{0,7}$.
Twisting by $2$ and reading off invariants gives $\latI_{1,8}(2) = (9,9,1)$ of signature $(1,8)$ and $\latI_{0,7}(2) = \generators{-2}^{\oplus 7} = (7,7,1)$ of signature $(0,7)$.
:::

## The discriminant form of $T_\Co$

::: {.definition #def:coble-mod-four-form title="The mod-$4$ norm on $B/2B$"}

For $B = \generators{1}\oplus E_{10}$ as in @prop:tco-as-twist, define
$$
\begin{aligned}
Q: B/2B &\to \ZZ/4\ZZ \\
x + 2B &\mapsto \beta_B(x, x) \bmod 4
.
\end{aligned}
$$
This is well defined, since $\beta_B(x + 2z, x + 2z) = \beta_B(x,x) + 4\beta_B(x,z) + 4\beta_B(z,z)$.
:::

::: {.lemma #lem:coble-discriminant-form title="The discriminant form of $T_\Co$ is half the mod-$4$ norm"}

The map $x\mapsto\pi_{T_\Co}(x/2)$ induces an isomorphism $B/2B\isoto A_{T_\Co}\cong(\ZZ/2\ZZ)^{11}$, under which
$$
q_{T_\Co}\qty{\pi_{T_\Co}(x/2)} = \tfrac12 Q(x+2B)\in\tfrac12\ZZ/2\ZZ
.
$$
Hence:

1. the class $\pi_{T_\Co}(x/2)$ is isotropic if and only if $\beta_B(x,x)\in4\ZZ$;
2. a group automorphism of $A_{T_\Co}$ preserves $q_{T_\Co}$ if and only if, transported to $B/2B$, it maps each of the four fibers $\inverseof{Q}(0),\dots,\inverseof{Q}(3)$ to itself.
:::

::: {.proof}

$B$ is unimodular of rank $11$ and $T_\Co = B(2)$ (@prop:tco-as-twist), so @prop:twisted-unimodular-discriminant gives the isomorphism and the formula $q_{T_\Co}(\pi(x/2)) = \tfrac12\beta_B(x,x)+2\ZZ$, which is $\tfrac12 Q(x+2B)$.
Multiplication by $\tfrac12$ is a bijection $\ZZ/4\ZZ\isoto\tfrac12\ZZ/2\ZZ$, so $q_{T_\Co}$ and $Q$ have the same fibers.
Part 1 is the fiber over $0$.
For part 2, a group automorphism $g$ preserves $q_{T_\Co}$ exactly when $Q\circ g = Q$, which is the condition that $g$ maps each fiber of $Q$ to itself.
:::

::: {.lemma #lem:f2-quadratic-gauss-sum title="The sign of the Gauss sum of a quadratic form over $\bF_2$"}

Let $V$ be an $\bF_2$-vector space of dimension $2m$ with a quadratic form $\bar q\colon V\to\bF_2$ whose polar form is nondegenerate, and put
$$
\Sigma(\bar q)\definedas\sum_{x\in V}(-1)^{\bar q(x)} = \#\inverseof{\bar q}(0) - \#\inverseof{\bar q}(1)
.
$$
Then $\Sigma(\bar q) = 2^m$ if $\bar q$ is of plus type and $\Sigma(\bar q) = -2^m$ if $\bar q$ is of minus type, in the sense of [@CCN+85, Ch. 2, §4]: of Witt index $m$, respectively $m-1$.
Hence
$$
\#\inverseof{\bar q}(0) = 2^{2m-1} + \tfrac12\Sigma(\bar q)
,
$$
and $\bar q$ is of plus type if and only if it has $2^{2m-1}+2^{m-1}$ zeros.
:::

::: {.proof}

Write $b$ for the polar form, $b(x,y) = \bar q(x+y)-\bar q(x)-\bar q(y)$.
Let $W\subseteq V$ be a totally singular subspace of maximal dimension $k$, the Witt index.
For $x\in W^{\perp}$ and $w\in W$, $\bar q(x+w) = \bar q(x) + b(x,w) + \bar q(w) = \bar q(x)$, so $\bar q$ descends to a quadratic form on $W^{\perp}/W$.
For $x\notin W^{\perp}$, the map $w\mapsto b(x,w)$ is a nonzero linear functional on $W$, and $\bar q(x+w) = \bar q(x)+b(x,w)$, so $\bar q$ takes each value on exactly half of the coset $x+W$ and the coset contributes $0$ to $\Sigma(\bar q)$.
Hence
$$
\Sigma(\bar q) = \sum_{x\in W^{\perp}}(-1)^{\bar q(x)} = \abs{W}\cdot\Sigma\qty{\bar q|_{W^{\perp}/W}}
.
$$
Since $b$ is nondegenerate, $\dim W^{\perp} = 2m-k$, so $W^{\perp}/W$ has dimension $2m-2k$; the polar form it induces is nondegenerate, and by maximality of $W$ the induced form has no nonzero singular vector.
So $2m-2k\leq2$: in dimension at least $3$, a nonzero $x$ and some $x'\in x^{\perp}\sm\generators{x}$ give $x+x'\neq0$ with $\bar q(x+x') = \bar q(x)+\bar q(x')+b(x,x') = 1+1+0 = 0$.
If $k = m$ then $W^{\perp} = W$ and $\Sigma(\bar q) = 2^m$.
If $k = m-1$ then $W^{\perp}/W$ is a plane on which $\bar q$ takes the value $1$ at its three nonzero vectors, so $\Sigma\qty{\bar q|_{W^{\perp}/W}} = 1-3 = -2$ and $\Sigma(\bar q) = -2^m$.
The zero count follows from $\#\inverseof{\bar q}(0)+\#\inverseof{\bar q}(1) = 2^{2m}$.
:::

::: {.lemma #lem:even-unimodular-mod-two-form title="The mod-$2$ form of an even unimodular lattice"}

Let $M$ be an even unimodular lattice of rank $2m$, and define $\bar q_M\colon M/2M\to\bF_2$ by $\bar q_M(x+2M) = \tfrac12\beta_M(x,x)\bmod 2$.
Then $\bar q_M$ is a quadratic form with nondegenerate polar form, it is of plus type, and it has $2^{2m-1}+2^{m-1}$ zeros.
In particular $\bar q_{U}$, $\bar q_{E_8}$ and $\bar q_{E_{10}}$ have $3$, $136$ and $528$ zeros.
:::

::: {.proof}

By @prop:twisted-unimodular-discriminant, $x\mapsto\pi_{M(2)}(x/2)$ identifies $M/2M$ with $A_{M(2)}$, and $q_{M(2)}(\pi(x/2)) = \tfrac12\beta_M(x,x)+2\ZZ$, which lies in $\ZZ/2\ZZ$ because $M$ is even; so $q_{M(2)}$ is $\bar q_M$ under the identification $\ZZ/2\ZZ = \bF_2$.
Its polar form is $\beta_M\bmod 2$, which is nondegenerate because the Gram matrix of $M$ has determinant $\pm1$.

Let $(n_+,n_-)$ be the signature of $M$.
The finite quadratic module $A_M$ is zero, so @thm:milgram applied to $M$ gives $n_+-n_-\equiv0\pmod 8$.
The lattice $M(2)$ is even of the same signature, so @thm:milgram applied to $M(2)$ gives $\operatorname{Br}(A_{M(2)}) = 0$, that is, $\gamma(A_{M(2)}) = 1$ in @def:brown-invariant.
Since $\exp(\pi i\,q_{M(2)}) = (-1)^{\bar q_M}$ and $\#A_{M(2)} = 2^{2m}$, this says $\Sigma(\bar q_M) = 2^m$.
By @lem:f2-quadratic-gauss-sum, $\bar q_M$ is of plus type with $2^{2m-1}+2^{m-1}$ zeros.
For $U$, $E_8$ and $E_{10}$ the rank is $2$, $8$ and $10$, which gives $3$, $136$ and $528$.
:::

::: {.proposition #prop:coble-q-fibers title="The fibers of $Q$"}

The four fibers of $Q$ on the $2^{11} = 2048$ classes of $B/2B$ have cardinalities
$$
\abs{\inverseof{Q}(0)} = 528,\quad
\abs{\inverseof{Q}(1)} = 528,\quad
\abs{\inverseof{Q}(2)} = 496,\quad
\abs{\inverseof{Q}(3)} = 496
.
$$
In particular $A_{T_\Co}$ contains exactly $528$ isotropic classes, of which $527$ are nonzero.
:::

::: {.proof}

Write $B = \generators{v}\oplus E_{10}$ with $v^2 = 1$ and let $x = \varepsilon v + y$ represent a class of $B/2B$, with $\varepsilon\in\theset{0,1}$ and $y$ ranging over $E_{10}/2E_{10}$.
Then $\beta_B(x,x) = \varepsilon + \beta_{E_{10}}(y,y)$, and $\beta_{E_{10}}(y,y)\equiv 2\bar q_{E_{10}}(y)\pmod 4$ with $\bar q_{E_{10}}$ as in @lem:even-unimodular-mod-two-form.
Hence $Q(x) = \varepsilon + 2\bar q_{E_{10}}(y)$: the classes with $Q = 0$ and those with $Q = 1$ are each in bijection with the zeros of $\bar q_{E_{10}}$, and the classes with $Q = 2$ and those with $Q = 3$ are each in bijection with its non-zeros.
By @lem:even-unimodular-mod-two-form, $\bar q_{E_{10}}$ has $528$ zeros and $2^{10}-528 = 496$ non-zeros.
The isotropic classes are the fiber $\inverseof{Q}(0)$ by @lem:coble-discriminant-form(1), and the zero class is one of them.
:::

## The isometry group of the discriminant form

::: {.proposition #prop:coble-discriminant-group title="$\Orth(q_{T_\Co})$ is the discriminant group of $E_{10}(2)$"}

Restriction to the subgroup
$$
A^0 \definedas \theset{ x\in A_{T_\Co} \mid q_{T_\Co}(x)\in\ZZ/2\ZZ } \cong A_{E_{10}(2)}
$$
of index $2$ induces an isomorphism
$$
\Orth(A_{T_\Co}, q_{T_\Co}) \iso \Orth(A_{E_{10}(2)}, q_{E_{10}(2)}) \cong \operatorname{GO}^+_{10}(2)
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

Write $A_{T_\Co} = \generators{\bar h}\oplus A_{E_{10}(2)}$ with $\bar h$ the class of $\tfrac12 h$ for $h$ the basis vector of $\generators{2}$, so that $q_{T_\Co}(\bar h) = \tfrac12$ and $\bar h$ is orthogonal to $A_{E_{10}(2)}$ for the discriminant bilinear form.
Since $q_{E_{10}(2)}$ is $\ZZ/2\ZZ$-valued, $A^0 = A_{E_{10}(2)}$, and $A^0$ is intrinsically defined by $q_{T_\Co}$, hence preserved by every isometry.
Restriction therefore gives a homomorphism $\rho\colon\Orth(A_{T_\Co}, q_{T_\Co})\to\Orth(A^0, q_{T_\Co}|_{A^0})$.

$\rho$ is injective.
If $g$ restricts to the identity on $A^0$ then $g(\bar h) = \bar h + z$ for some $z\in A^0$, and preservation of the bilinear form gives $b(z, y) = b(g\bar h, y) - b(\bar h, y) = 0$ for every $y\in A^0$; by @prop:discriminant-nondegenerate, the form $q_{E_{10}(2)}$ is nondegenerate, so $z = 0$.

$\rho$ is surjective.
Given $g_0\in\Orth(A^0)$, extend it by $\bar h\mapsto\bar h$; the extension preserves $q_{T_\Co}$ because the decomposition $A_{T_\Co} = \generators{\bar h}\perp A^0$ is orthogonal.

By @lem:even-unimodular-mod-two-form, $(A_{E_{10}(2)}, q_{E_{10}(2)})$ is the $10$-dimensional $\bF_2$-space $E_{10}/2E_{10}$ with the plus-type form $\bar q_{E_{10}}$, so its isometry group is $\operatorname{GO}^+_{10}(2)$.
For $n = 2m$ and $q$ a prime power, $\abs{\operatorname{GO}^+_{2m}(q)} = 2N$ with $N = q^{m(m-1)}(q^m-1)\prod_{i=1}^{m-1}(q^{2i}-1)$ [@CCN+85, Ch. 2, §4].
At $q = 2$, $m = 5$,
$$
2N = 2\cdot 2^{20}\cdot 31\cdot 3\cdot 15\cdot 63\cdot 255 = 2^{21}\cdot 3^5\cdot 5^2\cdot 7\cdot 17\cdot 31 = 46\,998\,591\,897\,600
.
$$
:::

::: {.theorem #thm:coble-isotropic-class-orbits title="Two orbits of isotropic classes"}

The group $\Orth(A_{T_\Co}, q_{T_\Co})$ has exactly two orbits on the $528$ isotropic classes of $A_{T_\Co}$: the zero class, and the set of all $527$ nonzero isotropic classes.
:::

::: {.proof}

An isotropic class lies in $A^0$, so by @prop:coble-discriminant-group the action is that of $\Orth(A_{E_{10}(2)}, q_{E_{10}(2)})$ on the singular vectors of the nondegenerate quadratic form $\bar q_{E_{10}}$ on the $10$-dimensional $\bF_2$-space $E_{10}/2E_{10}$ (@lem:even-unimodular-mod-two-form).
Witt's extension theorem for nondegenerate quadratic forms over a field states that an isometry between subspaces extends to the whole space; applied to the lines spanned by two nonzero singular vectors it shows that the orthogonal group is transitive on nonzero singular vectors.
The zero class is fixed, and by @prop:coble-q-fibers there are $528 - 1 = 527$ nonzero singular vectors.
:::

## From discriminant classes to lattice vectors

::: {.proposition #prop:coble-primitive-isotropic-classes title="Primitive isotropic vectors and their discriminant classes"}

Every primitive isotropic $v\in T_\Co$ has $\div_{T_\Co}(v) = 2$, and its associated class
$$
v^* \definedas \tfrac{1}{2}v + T_\Co \in A_{T_\Co}
$$
is a nonzero isotropic class.
By @thm:coble-isotropic-class-orbits, all such classes lie in the single nonzero orbit.
:::

::: {.proof}

By @lem:divisibilityAlwaysTwoTco, $\div_{T_\Co}(v)=2$. By @def:coble-discriminant-forms and the divisibility conventions of the Lattice Theory section, $v^*$ therefore has order $2$ in $A_{T_\Co}$, so $v^*\neq0$.
Writing $v\in B$ and using $\beta_{T_\Co} = 2\beta_B$, isotropy of $v$ gives $\beta_B(v,v) = 0$, hence $q_{T_\Co}(v^*) = 0$ by @lem:coble-discriminant-form(1).
By @thm:coble-isotropic-class-orbits, the nonzero isotropic classes form a single orbit.
:::

::: {.lemma #lem:stable-orthogonal-not-transitive title="The stable orthogonal group is not transitive on isotropic lines"}

Let $B = U\oplus U\oplus\latI_{0,7}$ and $T_\Co = B(2)$ as in @prop:tco-split-maximal, and let $e, f$ be the isotropic basis vectors of the first hyperbolic summand of $B$, so that in $T_\Co$ they are primitive isotropic vectors with $e\cdot f = 2$.
Then no $g\in\Gamma_\Co = \Orth^+(T_\Co)^*$ satisfies $g(\ZZ e) = \ZZ f$.
So $\Orth^+(T_\Co)$ is transitive on the primitive isotropic vectors of $T_\Co$ (@thm:unpolarized-cusps) while the arithmetic group of $\fco$ is not, and $\overline{F_\Co}^{\bb}$ has at least two $0$-cusps.
:::

::: {.proof}

By definition of the stable orthogonal group, $g$ acts trivially on $A_{T_\Co}$; and the identification $A_{T_\Co}\cong B/2B$ of @prop:twisted-unimodular-discriminant is $\Orth(B)$-equivariant, $g$ sending the class of $\tfrac12 x$ to the class of $\tfrac12 g(x)$ for $x\in B$.

Suppose $g(\ZZ e) = \ZZ f$, so $g(e) = m f$ for some $m\in\ZZ$. Because $e$ is primitive and $g$ is an isometry, $g(e)$ is primitive, so $m = \pm1$.
Now $\tfrac12 e\in T_\Co^*$, because $\beta_{T_\Co}\bigl(\tfrac12 e, B\bigr) = \beta_{B}(e,B)\subseteq\ZZ$; hence $g(\tfrac12 e) = \pm\tfrac12 f$ is again in $T_\Co^*$, and applying $g$ to the class of $\tfrac12 e$ gives the class of $\pm\tfrac12 f$.
That class is the class of $\tfrac12 e$, since $g$ fixes every class, so $\tfrac12(e\mp f)\in T_\Co = B$, that is $e\mp f\in 2B$.
But $e$ and $f$ are two elements of a $\ZZ$-basis of $B$, and the coordinates of $e - f$ on $e$ and $f$ are $1$ and $-1$, so $e\mp f\notin 2B$. Contradiction.
:::

::: {.lemma #lem:character-kernel-orbits title="Orbits of a group and of the kernel of a character"}

Let a group $G$ act on a set $X$, let $\chi\colon G\to\{\pm1\}$ be a surjective homomorphism and $H=\ker\chi$. Then for $x\in X$
$$
Hx = Gx \quad\Longleftrightarrow\quad \Stab_G(x)\not\subseteq H,
$$
and therefore
$$
\#(H\backslash X) \;=\; \#(G\backslash X) \;+\; \#\bigl\{G\text{-orbits } O : \Stab_G(x)\subseteq H \text{ for } x\in O\bigr\},
$$
the added term counting the $G$-orbits that are unions of exactly two $H$-orbits.
:::

::: {.proof}

The target of $\chi$ is abelian, so $\chi$ is constant on conjugacy classes, conjugates of $\Stab_G(x)$ have the same image, and "$\Stab_G(x)\subseteq H$" is a property of the orbit.

Since $\chi$ is surjective, choose $\sigma\in G$ with $\chi(\sigma)=-1$; then $G = H\cup\sigma H$.
Suppose first that $s\in\Stab_G(x)$ has $\chi(s)=-1$; then $\chi(\sigma s^{-1}) = (-1)(-1) = +1$, so $\sigma s^{-1}\in H$ and $\sigma x = (\sigma s^{-1})sx = (\sigma s^{-1})x\in Hx$, whence $Gx = Hx\cup H\sigma x = Hx$. Conversely if $Gx = Hx$ then $\sigma x\in Hx$, say $\sigma x = hx$ with $h\in H$, and $h^{-1}\sigma\in\Stab_G(x)$ has $\chi = (-1)(-1) = -1$.

Every $G$-orbit is $Hx\cup H\sigma x$, and these two are either equal or disjoint: one or two $H$-orbits. It is one exactly when $\Stab_G(x)\not\subseteq H$. Summing the number of $H$-orbits over the $G$-orbits gives the displayed identity.
:::

::: {.proposition #prop:discriminant-kernel-orbits title="The discriminant kernel and the stable group have the same isotropic orbits"}

Let $B=\latI_{2,9}$, $T_\Co=B(2)$, let $K=\discriminantkernel{T_\Co}$ be the discriminant kernel and $\Gamma_\Co=\Orth^+(T_\Co)\intersect K$. Then

1. $K\neq\Gamma_\Co$, and $[K:\Gamma_\Co]=2$;
2. $K$ and $\Gamma_\Co$ have the same orbits on the primitive isotropic vectors of $T_\Co$, and the same orbits on the primitive isotropic lines.
:::

::: {.proof}

*The groups differ.* $B$ is odd, so it has a unit vector $v$ with $v^2=1$, and the reflection $s_v(x) = x-2(x,v)v$ is integral and orthogonal. Modulo $2B$ it is the identity, so $s_v\in K$; and by the reflection computation of @prop:period-spinor-character, $\chi_{\mathrm{per}}(s_v) = \operatorname{sgn}(-q(v)) = -1$, because $q(v) = \tfrac12 > 0$ and $v$ is a positive vector. So $\chi_{\mathrm{per}}$ is nontrivial on $K$, which is therefore not contained in $\Orth^+$, and $[K:\Gamma_\Co]=2$ since $\chi_{\mathrm{per}}$ takes values in $\{\pm1\}$.

*The orbits agree.* By @lem:character-kernel-orbits, applied to the restriction of $\chi_{\mathrm{per}}$ to $K$, which is surjective by the first part, it is enough to find, for each primitive isotropic $x$, an element of $\Stab_K(x)$ with character $-1$.
By @thm:unpolarized-cusps there is $g\in\Orth(B)$ with $g(\ZZ e) = \ZZ x$ for the vector $e$ of @prop:tco-split-maximal, and $e^{\perp B} = \ZZ e\oplus M_0$ with $M_0 = U\oplus\latI_{0,7}\cong\latI_{1,8}$; so $x^{\perp B} = \ZZ x\oplus M$ with $M = g(M_0)\cong\latI_{1,8}$.
Now $\latI_{1,8}$ has a unit vector $v$, and $v\perp x$, so $s_v$ fixes $x$ while lying in $K$ with $\chi_{\mathrm{per}}(s_v)=-1$ by the computation above. Hence every $K$-orbit is $\Gamma_\Co$-stable and the two partitions coincide.

*Vectors and lines.* The map from vector-orbits to line-orbits is surjective always, and injective here because $-\id\in\Gamma_\Co$: it acts trivially on $A_{T_\Co}$, which is $2$-torsion, and $\chi_{\mathrm{per}}(-\id)=+1$, its determinant on the positive plane being $(-1)^2$. So each line-orbit carries exactly one vector-orbit for either group.
:::

## The Eichler criterion and its hypothesis

::: {.proposition #prop:tco-no-hyperbolic-plane title="$T_\Co$ contains no copy of $U$"}

Every value of $\beta_{T_\Co}$ is even. Hence $T_\Co$ contains no sublattice isometric to $U$, and
@thm:eichler-criterion does not apply to $T_\Co$.
:::

::: {.proof}

By @prop:tco-as-twist, $T_\Co=B(2)$, so $\beta_{T_\Co}=2\beta_B$ takes even values. A sublattice isometric
to $U$ contains two vectors with pairing $1$.
:::

## The two $0$-cusp lattices {#sec-zero-cusp-lattices}

::: {.proposition #prop:zero-cusp-lattices title="The $0$-cusp lattices of $\fen$ and of $\fco$"}

Let $T$ be $T_\En = U\perp U(2)\perp E_8(2)$ or $T_\Co = B(2)$ with $B = U\perp U\perp \I_{0,7}$, and let $v$ be a primitive isotropic vector: the isotropic basis vector of a hyperbolic summand in either case.
Then the cusp lattice $v^{\perp T}/\generators{v}$ is

1. for $T_\En$, $U(2)\oplus E_8(2)$: rank $10$, determinant $-2^{10}$, signature $(1,9)$, even $2$-elementary with invariants $(r,a,\delta) = (10,10,0)$;
2. for $T_\Co$, $U(2)\oplus\generators{-2}^{7} = \I_{1,8}(2)$: rank $9$, determinant $2^{9}$, signature $(1,8)$, even $2$-elementary with invariants $(r,a,\delta) = (9,9,1)$.
:::

::: {.proof}

In both cases $v$ spans a hyperbolic summand and is orthogonal to the rest, so $v^{\perp T} = \generators{v}\perp (\text{the remaining summand})$ and the quotient by $\generators{v}$ drops the hyperbolic direction: for $T_\En = U\perp U(2)\perp E_8(2)$ this leaves $U(2)\oplus E_8(2)$, and for $T_\Co = U(2)\oplus U(2)\oplus\I_{0,7}(2)$ from the splitting of @prop:tco-split-maximal it leaves $U(2)\oplus\I_{0,7}(2) = U(2)\oplus\generators{-2}^{7}$, which is $\I_{1,8}(2)$ because $U\oplus\generators{-1}^{7}$ is the odd unimodular lattice of signature $(1,8)$.

Both lattices are twists $M(2)$ of a unimodular lattice $M$: $U(2)\oplus E_8(2) = (U\oplus E_8)(2)$ with $M = U\oplus E_8$ even of rank $10$, and $\I_{1,8}(2)$ with $M = \I_{1,8}$ odd of rank $9$.
Twisting preserves the signature, so the signatures are $(1,9)$ and $(1,8)$, and $\det M(2) = 2^{\rank M}\det M$ gives $2^{10}\cdot(-1) = -2^{10}$ and $2^{9}\cdot 1 = 2^9$.
By @prop:twisted-unimodular-discriminant, $A_{M(2)}\cong(\ZZ/2\ZZ)^{\rank M}$, so both are $2$-elementary with $a = r$, that is $a = 10$ and $a = 9$, and the quadratic value module is $\ZZ/2\ZZ$ for $M$ even and $\tfrac12\ZZ/2\ZZ$ for $M$ odd.
So $q$ is integral on $A_{(U\oplus E_8)(2)}$, giving $\delta = 0$, and takes the non-integral value $\tfrac12$ on the class of $\tfrac12 u$ for a unit vector $u$ of $\I_{1,8}$, giving $\delta = 1$.
:::

::: {.theorem #thm:zero-cusp-chambers title="The chambers of the two $0$-cusp lattices"}

Let $K_\Co = \I_{1,8}(2)$ and $K_\En = U(2)\oplus E_8(2)$ be the cusp lattices of @prop:zero-cusp-lattices, halves $K'_\Co = \I_{1,8}$ and $K'_\En = U\oplus E_8$, and let $K(2)$ denote $K$ with the form doubled.
Then

1. $\Orth(K(2)) = \Orth(K)$, and the reflection $s_r$ of @def:spinor-norm is unchanged when the form is scaled, so the Coxeter chamber of $K(2)$ is the chamber of $K$ with every root norm doubled;

2. the chamber of $K_\En = \eta_1^{\perp}/\eta_1$ has ten walls, with Coxeter diagram $T_{2,3,7}$, all of whose edges have label $3$, one ideal vertex, and its ten walls are the roots
$$
-\eps_3,\ \dots,\ -\eps_{10},\qquad \eps_1-\eps_2,\qquad \eps_2+2\eps_3+3\eps_4+4\eps_5+6\eps_6+5\eps_7+4\eps_8+3\eps_9+2\eps_{10}
$$
in the basis $\eps_1,\dots,\eps_{10}$ of @sec-sterk-root-counts-and-computed-chambers, the coefficients $(2,3,4,6,5,4,3,2)$ being the marks of the highest root of $E_8$;

3. the chamber of $K_\Co$ has nine walls: in the negative-square convention a chain of eight nodes of norms $(-2,\dots,-2,-1)$ with seven label-$3$ edges and one label-$4$ edge at the end, and a ninth node of norm $-2$ joined to the third node of the chain by a label-$3$ edge --- the chain with a leaf at node $3$, which is the row $5\leq n\leq 9$ of [@Vin72, Table 5, article p. 31] at $n = 8$, and the Gram field is $\QQ[\sqrt2]$;

4. the chamber of the second Enriques $0$-cusp lattice $U\oplus E_8(2) = \eta_2^{\perp}/\eta_2$ has ten walls: the list of item 2 with the coefficient of $\eps_2$ in the last root equal to $2$. Nine of them have norm $-4$ and $\eps_1-\eps_2$ has norm $-2$ and meets the last root with label $4$; the chamber has two ideal vertices and Gram field $\QQ[\sqrt2]$, and, like the chamber of item 2, it has the $f$-vector $(10,45,120,210,252,210,120,45,10,1)$ of a $9$-simplex and finite covolume, so both Enriques $0$-cusp lattices are reflective.

:::

::: {.proof}

*The scaling lemma.* The form of $K(2)$ is $2b_K$, so an endomorphism $g$ satisfies $2b_K(gx,gy) = 2b_K(x,y)$ for all $x,y$ exactly when it is an isometry of $K$: $\Orth(K(2)) = \Orth(K)$ as subgroups of $\GL(K)$. The reflection $s_r(x) = x - 2\frac{b(x,r)}{b(r,r)}r$ is homogeneous of degree $0$ in the form, so the reflection in $r$ is the same map for $K$ and for $K(2)$, and the wall it defines has norm $r^2$ in $K$ and $2r^2$ in $K(2)$. Hence the chambers correspond wall by wall, with the norms doubled.

*The Enriques chambers.* The walls, their norms and the Coxeter diagrams of items 2 and 4 are the simple roots of the two rank-$10$ quotient lattices in @sec-sterk-root-counts-and-computed-chambers; the ideal vertices, Gram fields and $f$-vectors are those of the $(10,10,0)_1$ and $(10,8,0)_1$ rows of @sec-coxiter-results-for-cusp-lattices.

*The Coble chamber.* By item 1 it suffices to treat $K'_\Co = \I_{1,8}$, with basis $v_0,\dots,v_8$ of squares $(1,-1,\dots,-1)$.
Put $e_i = -v_i+v_{i+1}$ for $1\leq i\leq 7$, $e_8 = -v_8$ and $w = v_0+v_1+v_2+v_3$.
Then $e_i^2 = -2$ for $i\leq 7$, $e_8^2 = -1$ and $w^2 = 1-3 = -2$, so each reflection $x\mapsto x - 2\frac{(x,r)}{(r,r)}r$ is integral and these nine vectors are roots.
The pairings are $(e_i,e_{i+1}) = -(v_{i+1},v_{i+1}) = 1$ for $1\leq i\leq 7$, $(e_i,e_j) = 0$ for $\abs{i-j}\geq2$, $(w,e_3) = -(w,v_3)+(w,v_4) = 1$, and $(w,e_i) = 0$ for $i\neq3$, since $(w,v_0) = 1$, $(w,v_j) = -1$ for $1\leq j\leq3$ and $(w,v_j) = 0$ for $j\geq4$.
So the angle between $e_i$ and $e_{i+1}$ has cosine $\tfrac12$ for $i\leq6$ and $\tfrac1{\sqrt2}$ for $i = 7$, and the angle between $w$ and $e_3$ has cosine $\tfrac12$: the Gram matrix of these nine roots is the diagram of item 3, with Gram field $\QQ[\sqrt2]$.
Up to the sign of the form, $e_1,\dots,e_8$ are the initial vectors of Vinberg's algorithm for $\I_{1,8}$ and $w$ is the single further vector listed for $n = 8$ in [@Vin72, Table 4]; by [@Vin72, Table 5] and the finite-volume argument following it, the reflections in these nine roots generate the reflection subgroup of $\Orth(\I_{1,8})$ and the nine walls bound its fundamental chamber.
:::
