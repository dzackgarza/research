# Discriminant orbits of the Coble lattice {#sec-discriminant-orbits}

::: {.remark title="Which group $\Gamma_\Co$ is on this page"}
The four groups of the Coble lattice are named in @def:gamma-co-groups and tabulated in [lattice and diagram conventions](#sec-lattice-and-diagram-conventions). Where this page writes $\Gamma_\Co$ it means the stable subgroup $\tilde\Orth^+(T_\Co) = \Orth^+(T_\Co)\intersect\ker\bar\rho$, and every count of $0$-cusps below names that group; the group of the Coble divisor and the group of the moduli space are the other two entries of that table.
:::


::: {.remark}

The Coble period lattice $T_\Co = \generators{2}\oplus E_{10}(2)$ is the twist by $2$ of an odd unimodular lattice, and this single fact controls both its isometry group and its discriminant form.
We compute the discriminant quadratic form $(A_{T_\Co}, q_{T_\Co})$ explicitly, determine its isometry group and the decomposition of its isotropic classes into orbits, and record the bridge between that finite datum and the primitive isotropic vectors of $T_\Co$ themselves.
Throughout we use the discriminant apparatus of @def:coble-discriminant-forms and the invariant triple $(r, a, \delta)$ of the Lattice Theory section.
:::

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

By @def:enriques-lattice, the lattice $E_{10} = U\oplus E_8$ is even and unimodular of signature $(1,9)$, so $B = \generators{1}\oplus E_{10}$ is unimodular of signature $(2,9)$ and is odd because the generator of $\generators{1}$ has norm $1$.
By @thm:indefinite-unimodular-classification, an odd unimodular lattice of signature $(2,9)$ is isometric to $\latI_{2,9}$.
Twisting distributes over orthogonal direct sums and $\generators{1}(2) = \generators{2}$, whence $B(2) = \generators{2}\oplus E_{10}(2) = T_\Co$.

A twist leaves the underlying $\ZZ$-module unchanged and multiplies the form by a nonzero scalar, so an automorphism of the module preserves $\beta_B$ if and only if it preserves $2\beta_B = \beta_{B(2)}$; this gives $\Orth(T_\Co) = \Orth(B)$.
The same scaling shows $\beta_{T_\Co}(v,v) = 2\beta_B(v,v)$ vanishes exactly when $\beta_B(v,v)$ does, and primitivity is a property of the module alone.
:::

::: {.remark}

The presentation $T_\Co\cong\latI_{2,9}(2)$ is recorded in @rmk:k3-cover-invariants; @lem:divisibilityAlwaysTwoTco carries out the divisibility computation in this presentation.
Applying the indefinite unimodular classification (@thm:indefinite-unimodular-classification) once more to $U\oplus U\oplus\latI_{0,7}$, which is odd unimodular of signature $(2,9)$, gives the further presentation
$$
T_\Co \cong U(2)^{\oplus 2}\oplus\generators{-2}^{\oplus 7}
= U(2)^{\oplus 2}\oplus A_1^{\oplus 7}
,
$$
in which the Witt index $2$ and the negative-definite rank-$7$ complement of a maximal isotropic subspace are visible in the presentation itself.
:::

::: {.proposition #prop:tco-split-maximal title="$T_\Co$ is the twist of a split maximal lattice"}

The lattice $B\cong\latI_{2,9}$ of @prop:tco-as-twist is maximal in the sense of @def:maximal-lattice and split in the sense of @def:split-maximal:
$$
B \cong U\oplus U\oplus\latI_{0,7}
.
$$
In a decomposition $T_\Co = B(2)$ with $B = U\oplus U\oplus\latI_{0,7}$, an isotropic generator $e$ of one hyperbolic summand and the plane $J$ spanned by isotropic generators of both have
$$
e^{\perp}/e \cong \latI_{1,8}(2) = (9,9,1)_1,
\qquad
J^{\perp}/J \cong \latI_{0,7}(2) \cong A_1^{\oplus 7} = (7,7,1)_0
.
$$
:::

::: {.proof}

$B$ is unimodular, hence maximal by @lem:maximal-overlattice-exists.
The lattice $U\oplus U\oplus\latI_{0,7}$ is unimodular of signature $(2,9)$ and odd, because $\latI_{0,7}$ is, so it is isometric to $\latI_{2,9}\cong B$ by @thm:indefinite-unimodular-classification; this exhibits $B$ in the shape required by @def:split-maximal, as @thm:maximal-splits-for-large-n also predicts for $n = 9\geq 5$.
For the quotients, take $e$ to be an isotropic generator of the first hyperbolic summand of $B\cong U\oplus U\oplus\latI_{0,7}$; then $e^{\perp B} = \ZZ e\oplus U\oplus\latI_{0,7}$ and $e^{\perp}/e\cong U\oplus\latI_{0,7}\cong\latI_{1,8}$, which is odd unimodular of signature $(1,8)$.
Taking $J$ to be spanned by isotropic generators of the two hyperbolic summands gives $J^{\perp B} = J\oplus\latI_{0,7}$ and $J^{\perp}/J\cong\latI_{0,7}$.
Twisting by $2$ and reading off invariants gives $\latI_{1,8}(2) = (9,9,1)$ of signature $(1,8)$ and $\latI_{0,7}(2) = \generators{-2}^{\oplus 7} = (7,7,1)$ of signature $(0,7)$.
:::

::: {.remark}

Since $\Orth^+(T_\Co) = \Orth^+(B)$ and both isotropy and primitivity are unchanged by the twist, @prop:tco-split-maximal places $T_\Co$ under @thm:split-maximal-isotropic-transitivity; @thm:unpolarized-cusps gives the corresponding full-group cusp classification, and the computation above identifies its two boundary lattices with the Coble cusp invariants $(9,9,1)_1$ and $(7,7,1)_0$ used in the cusp correspondence.
The $1$-cusp lattice $\latI_{0,7}(2)\cong A_1^{\oplus 7}$ is negative definite of rank $7$, consistent with Witt index $2$ in signature $(2,9)$: $11 - 2\cdot 2 = 7$.
The gluing datum of the plane is computed too: every primitive vector of $J$ has divisibility $2$, so $J$ cuts out of $A_{T_\Co}$ the two-dimensional subspace $\bar J$ that is its image in $T_\Co/2T_\Co\cong B/2B$, and the plane $\generators{e',\,2h+\alpha_1+\alpha_2}$ of the cusp correspondence cuts out, in its own presentation, the subspace spanned by the images of $e'$ and $\alpha_1+\alpha_2$ (`computations/reports/plane_gluing_subgroup.py`).
Both are $(\ZZ/2)^2$ with zero pairing, and that is forced rather than informative: the two planes are primitive isotropic planes of a lattice of signature $(2,9)$, hence one $\Orth^+$ orbit by @thm:plane-transitivity-tco, so every *isometry* invariant of the pair $(T_\Co,J)$ — in particular the isomorphism type of $\bar J$ with its form — is the same for all planes.
The datum that can separate $\Gamma_\Co$-orbits is the subspace itself and not its type: $\Gamma_\Co$ acts trivially on $A_{T_\Co}$, so $\bar J$ is $\Gamma_\Co$-invariant, while an isometry $g$ carries it to $\overline{g(J)}$, so $\bar J$ is *not* an isometry invariant. Comparing the two exhibited subspaces would require identifying the two presentations of $T_\Co$, which this book does not construct; so nothing is claimed about whether the two exhibited planes lie in one $\Gamma_\Co$-orbit, and the count of $1$-cusps of $\fco$ stays open with it (@sec-open-problems).
:::

## The discriminant form of $T_\Co$

Applying @prop:twisted-unimodular-discriminant to $T_\Co=B(2)$ gives
$$
A_{T_\Co}\cong B/2B\cong(\ZZ/2\ZZ)^{11},
\qquad
q_{T_\Co}\!\left(\tfrac12x+T_\Co\right)=\tfrac12\beta_B(x,x)\bmod2\ZZ.
$$
Thus the isotropic classes are exactly the residue classes of vectors of $B$ whose norm is divisible by $4$.

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
Under the identification $A_{T_\Co}\cong B/2B$ of @prop:twisted-unimodular-discriminant one has $q_{T_\Co} = \tfrac12 Q$, so $Q$ and $q_{T_\Co}$ have the same fibers and $\Orth(A_{T_\Co}, q_{T_\Co})$ is the stabilizer in $\GL(B/2B)$ of the four fibers of $Q$.
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
Then $\beta_B(x,x) = \varepsilon + \beta_{E_{10}}(y,y)$, and since $E_{10}$ is even the value $\beta_{E_{10}}(y,y)$ is $\equiv 0$ or $2 \pmod 4$.
Hence $Q$ takes the value $0$ or $2$ on the classes with $\varepsilon = 0$ and the value $1$ or $3$ on those with $\varepsilon = 1$, and in both cases the split is governed by the single count
$$
N_0 \definedas \#\theset{ y\in E_{10}/2E_{10} \mid \beta_{E_{10}}(y,y)\equiv 0 \pmod 4 }
.
$$
The four fibers then have sizes $N_0,\ N_0,\ 2^{10} - N_0,\ 2^{10} - N_0$ in the order listed.

To compute $N_0$, observe that $\bar q(y)\definedas\tfrac12\beta_{E_{10}}(y,y)\bmod 2$ is a quadratic form $E_{10}/2E_{10}\to\bF_2$ whose polar form is the reduction of $\beta_{E_{10}}$ modulo $2$; the latter is nondegenerate because $E_{10}$ is unimodular.
Thus $\bar q$ is a nondegenerate quadratic form on a $10$-dimensional $\bF_2$-vector space, and $N_0 = \#\inverseof{\bar q}(0)$.
The decomposition $E_{10} = U\oplus E_8$ splits $\bar q$ orthogonally.
On $U/2U$ the form is $\bar q(ae + bf) = ab$, which is the hyperbolic plane over $\bF_2$ and has $3$ zeros; on $E_8/2E_8$ the form is the reduction of the $E_8$ form and has $136$ zeros.
Both are of plus type, hence so is their sum, and a nondegenerate plus-type form in dimension $2n$ over $\bF_2$ has $2^{2n-1} + 2^{n-1}$ zeros.
With $n = 5$ this gives
$$
N_0 = 2^{9} + 2^{4} = 512 + 16 = 528
,
$$
in agreement with the two summand counts $3\cdot 136 + 1\cdot 120 = 528$.
The remaining fiber sizes are $2^{10} - 528 = 496$.
:::

::: {.remark}

The counts $\#A_{E_{10}(2)} = 1024$, $\#I^0 = 528$ and $\#I^1 = 496$ tabulated in the reference tables are exactly the numbers $2^{10}$, $N_0$ and $2^{10} - N_0$ appearing in this proof, and the summand counts $\#I^0(U(2)) = 3$, $\#I^0(E_8(2)) = 136$ are the two zero-counts used to identify the type.
The isotropic classes of $A_{T_\Co}$ and of $A_{E_{10}(2)}$ therefore coincide as sets: a class $\varepsilon\bar v + \bar y$ is isotropic only if $\varepsilon = 0$, because $q_{T_\Co}(\bar v) = \tfrac12\notin\ZZ$ while $q_{E_{10}(2)}$ is $\ZZ$-valued.
This is the invariant $\delta = 1$ of $T_\Co$ read off from a distinguished class.
Both the four fiber sizes and the two summand zero-counts are reproduced from the lattice itself in `computations/reports/coble_528_isotropic_classes.py`: $B$ is assembled from the Cartan matrix of $E_8$ and the hyperbolic plane, twisted to $T_\Co$, and its discriminant quadratic form counted, the lattice counted being checked to be the one this chapter means by its signature $(2,9)$ and its $2$-elementary type $(11,11,1)$.
:::

## The isometry group of the discriminant form

::: {.proposition #prop:coble-discriminant-group title="$\Orth(q_{T_\Co})$ is the discriminant group of $E_{10}(2)$"}

Restriction to the subgroup
$$
A^0 \definedas \theset{ x\in A_{T_\Co} \mid q_{T_\Co}(x)\in\ZZ/2\ZZ } \cong A_{E_{10}(2)}
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

Write $A_{T_\Co} = \ZZ\bar h\oplus A_{E_{10}(2)}$ with $\bar h$ the class of $\tfrac12 h$ for $h$ the generator of $\generators{2}$, so that $q_{T_\Co}(\bar h) = \tfrac12$ and $\bar h$ is orthogonal to $A_{E_{10}(2)}$ for the discriminant bilinear form.
Since $q_{E_{10}(2)}$ is $\ZZ$-valued, $A^0 = A_{E_{10}(2)}$, and $A^0$ is intrinsically defined by $q_{T_\Co}$, hence preserved by every isometry.
Restriction therefore gives a homomorphism $\rho\colon\Orth(A_{T_\Co}, q_{T_\Co})\to\Orth(A^0, q_{T_\Co}|_{A^0})$.

$\rho$ is injective.
If $g$ restricts to the identity on $A^0$ then $g(\bar h) = \bar h + z$ for some $z\in A^0$, and preservation of the bilinear form gives $b(z, y) = b(g\bar h, y) - b(\bar h, y) = 0$ for every $y\in A^0$; by @prop:discriminant-nondegenerate, the form $q_{E_{10}(2)}$ is nondegenerate, so $z = 0$.

$\rho$ is surjective.
Given $g_0\in\Orth(A^0)$, extend it by $\bar h\mapsto\bar h$; the extension preserves $q_{T_\Co}$ because the decomposition $A_{T_\Co} = \ZZ\bar h\perp A^0$ is orthogonal.

The order of $\Orth(A_{E_{10}(2)}, q_{E_{10}(2)})$ is the one recorded in the reference tables.
:::

::: {.theorem #thm:coble-isotropic-class-orbits title="Two orbits of isotropic classes"}

The group $\Orth(A_{T_\Co}, q_{T_\Co})$ has exactly two orbits on the $528$ isotropic classes of $A_{T_\Co}$: the zero class, and the set of all $527$ nonzero isotropic classes.
:::

::: {.proof}

By @prop:coble-discriminant-group, the action is that of $\Orth(A_{E_{10}(2)}, q_{E_{10}(2)})$ on the singular vectors of the nondegenerate plus-type quadratic form $\bar q$ on the $10$-dimensional $\bF_2$-space $E_{10}/2E_{10}$ identified in @prop:coble-q-fibers.
Witt's extension theorem for nondegenerate quadratic forms over a field states that an isometry between subspaces extends to the whole space; applied to the lines spanned by two nonzero singular vectors it shows that the orthogonal group is transitive on nonzero singular vectors.
The zero class is fixed, and by @prop:coble-q-fibers there are $528 - 1 = 527$ nonzero singular vectors.
:::

::: {.remark}

The statement is also checked at the maintained action in `computations/reports/coble_isotropic_orbits.py`, and the check is worth reading as a warning: the orbit partition of the $2048$ classes has six orbits, of sizes $1, 1, 496, 496, 527, 527$, and the two orbits of size $527$ are *not* both isotropic --- one is the nonzero isotropic classes and the other lies in the fiber $q = \tfrac12$. Classified by the value of $q$ they are $(1,0)$, $(1,\tfrac12)$, $(496,1)$, $(496,\tfrac32)$, $(527,0)$ and $(527,\tfrac12)$, and restricting to $\inverseof{q}(0)$ leaves exactly the orbits of sizes $1$ and $527$ claimed above.
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
Writing $v\in B$ and using $\beta_{T_\Co} = 2\beta_B$, isotropy of $v$ gives $\beta_B(v,v) = 0$, hence $Q(v) = 0$ and, by @prop:twisted-unimodular-discriminant, $q_{T_\Co}(v^*) = 0$.
By @thm:coble-isotropic-class-orbits, the nonzero isotropic classes form a single orbit.
:::

::: {.remark title="What the finite orbit count does and does not determine"}

For the full orthogonal group, @thm:unpolarized-cusps states that $\Orth^+(T_\Co)$ is transitive on primitive isotropic vectors and on primitive isotropic planes, with quotients $e^{\perp T_\Co}/e\cong\latI_{1,8}(2)$ and $J^{\perp T_\Co}/J\cong\latI_{0,7}(2)\cong A_1^{\oplus 7}$. By @prop:coble-primitive-isotropic-classes and @thm:coble-isotropic-class-orbits, every primitive isotropic vector maps to the unique nonzero orbit.

For a subgroup $\Gamma\leq\Orth(T_\Co)$ the passage runs the other way and is not automatic.
The reduction map sends $\Gamma$-orbits of primitive isotropic vectors to $\rho(\Gamma)$-orbits of nonzero isotropic classes, but the integral parabolic stabilizer can have proper image in the finite stabilizer, so a finite orbit may split.
Conversely a *smaller* group need not have strictly finer orbits: by @lem:character-kernel-orbits the partitions of a group and of a subgroup agree exactly when every orbit's stabilizer meets the subgroup, and @prop:discriminant-kernel-orbits exhibits the case that matters here, the discriminant kernel being strictly larger than $\Gamma_\Co$ with the same orbits.
The $\gent$-induced orbit decomposition of the $528$ isotropic classes is computed in @thm:coble-heegner-finite-orbits, and it lifts: by @sec-cusp-lifting the parabolic stabilizer's image is the whole finite stabilizer, so each finite orbit is exactly one class of primitive isotropic vectors and not several.
:::

::: {.lemma #lem:stable-orthogonal-not-transitive title="The stable orthogonal group is not transitive on isotropic lines"}

Let $B = U\oplus U\oplus\latI_{0,7}$ and $T_\Co = B(2)$ as in @prop:tco-split-maximal, and let $e, f$ be isotropic generators of the first hyperbolic summand of $B$, so that in $T_\Co$ they are primitive isotropic vectors with $e\cdot f = 2$.
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

::: {.remark}

The number of $0$-cusps is a property of the pair $(T_\Co,\Gamma_\Co)$ and not of the lattice: with $\Orth^+(T_\Co)$ in place of $\Gamma_\Co$ it is one (@thm:unpolarized-cusps), and the group attached to $\fco$ is the stable one throughout (@sec-moduli-construction).

The lemma gives two orbits of the full orthogonal group; for $\Gamma_\Co$ the count is $527$, one per nonzero isotropic class of $A_{T_\Co}$ (@sec-cusp-lifting), so the discriminant form does give the exact number and not only a lower bound.
The $527$ and the $1$ above are **proved in prose only**: no computation record decides either, and the library call that would is sage-extensions#286.
:::

::: {.proposition #prop:coble-cusp-count title="The $0$-cusp count of $\fco$"}

Let $\rho_{T_\Co}\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ be the discriminant representation and let $v\in T_\Co$ be primitive isotropic.
Then the number of $\Gamma_\Co$-orbits of primitive isotropic vectors of $T_\Co$ is $527$, one for each nonzero isotropic class of $A_{T_\Co}$; the number of $\Gamma_\Co$-orbits of primitive isotropic lines is the same, so $\overline{F_\Co}^{\bb}$ has exactly $527$ $0$-cusps.
This count is **proved in prose only**: no computation record decides it. The computation that would is the library call that returns the $\ker\rho_{T_\Co}$- and $\Gamma_\Co$-orbit counts on $T_\Co$ directly, sage-extensions#286; until that record exists the number stands on the proof of @sec-cusp-lifting and on the class count of @prop:coble-q-fibers, and on nothing computed.
:::

::: {.proof}

$\Gamma_\Co$ acts trivially on $A_{T_\Co}$, so for $g\in\Gamma_\Co$ the class of $g(v)$ is $g(\tfrac12 v)+T_\Co = v^*$: primitive isotropic vectors with different classes lie in different $\Gamma_\Co$-orbits.
The classes attained by primitive isotropic vectors form one orbit of $\rho_{T_\Co}(\Orth(T_\Co))$, because $\Orth^+(T_\Co)$ is transitive on primitive isotropic lines (@thm:unpolarized-cusps) and $-\id\in\Gamma_\Co$, so $\Orth(T_\Co)$ is transitive on primitive isotropic vectors.
$T_\Co$ is even, indefinite and $2$-elementary, so $\rho_{T_\Co}$ is surjective (@thm:two-elementary-surjectivity) --- the surjectivity that [discriminant-form descent](#sec-discriminant-descent) names as its hypothesis (H1) --- and that orbit is an orbit of $\Orth(q_{T_\Co})$; by @prop:coble-primitive-isotropic-classes it contains a nonzero isotropic class, so by @thm:coble-isotropic-class-orbits it is the set of all $527$ nonzero isotropic classes.
So the $527$ nonzero isotropic classes give $527$ pairwise distinct orbits, and no vector has a class outside them: the count is $527$.

For the exact count, let $K = \ker\rho_{T_\Co}$; it has the same orbits as $\Gamma_\Co$ (@prop:discriminant-kernel-orbits).
$K$ is normal in $\Orth(T_\Co)$ with quotient $\Orth(q_{T_\Co})$, and $\Orth(T_\Co)$ acts transitively with stabilizer $S = \Stab_{\Orth(T_\Co)}(v)$, so the $K$-orbits correspond to the cosets of $KS$ in $\Orth(T_\Co)$, and their number is $[\Orth(q_{T_\Co}) : \rho_{T_\Co}(S)]$.
Since $\rho_{T_\Co}(S)$ fixes $v^*$, it lies in $\Stab_{\Orth(q_{T_\Co})}(v^*)$, whose index in $\Orth(q_{T_\Co})$ is the orbit length $527$.

That inclusion is an equality, and it is the content of @sec-cusp-lifting: writing $B = U\perp K$ with $\latI_{1,8}\cong K$, the Levi part $\Orth(K)$ maps onto the Levi quotient of $\Stab_{\Orth(q)}(v^*)$ and the Eichler transvections $E(v,k)$ supply the kernel, of order $2^8 = 89\,181\,388\,800/348\,364\,800$, so $\rho_{T_\Co}(S) = \Stab_{\Orth(q_{T_\Co})}(v^*)$ and the index is $1$.
Hence the count is $527$ and not merely at least that.
Vectors and lines give the same count because $-\id\in\Gamma_\Co$, as in the proof of @prop:discriminant-kernel-orbits.
:::

::: {.remark}

What the finite calculation determines is the other end: @thm:coble-isotropic-class-orbits shows the $527$ nonzero isotropic *classes* form a single orbit under $\Orth(q_{T_\Co})$, so a count in $A_{T_\Co}$ is a statement about the finite group, and the passage to the cusps of $\fco$ is the index of @prop:coble-cusp-count.
:::

::: {.lemma #lem:character-kernel-orbits title="Orbits of a group and of the kernel of a character"}

Let a group $G$ act on a set $X$, let $\chi\colon G\to\{\pm1\}$ be a homomorphism and $H=\ker\chi$. Then for $x\in X$
$$
Hx = Gx \quad\Longleftrightarrow\quad \Stab_G(x)\not\subseteq H,
$$
and therefore
$$
\#(H\backslash X) \;=\; \#(G\backslash X) \;+\; \#\bigl\{G\text{-orbits } O : \Stab_G(x)\subseteq H \text{ for } x\in O\bigr\},
$$
the added term counting the $G$-orbits that are unions of exactly two $H$-orbits.
In particular an index $[G:H]\leq2$ constrains the two partitions only through the stabilizers: it gives $Hx\subseteq Gx$ and no equality in either direction, and whether the counts agree is decided orbit by orbit, not by the group.
:::

::: {.proof}

The target of $\chi$ is abelian, so $\chi$ is constant on conjugacy classes, conjugates of $\Stab_G(x)$ have the same image, and "$\Stab_G(x)\subseteq H$" is a property of the orbit.

Suppose first that $s\in\Stab_G(x)$ has $\chi(s)=-1$, and let $\sigma\in G$ have $\chi(\sigma)=-1$; then $\chi(\sigma s^{-1}) = (-1)(-1) = +1$, so $\sigma s^{-1}\in H$ and $\sigma x = (\sigma s^{-1})sx = (\sigma s^{-1})x\in Hx$, whence $Gx = Hx\cup H\sigma x = Hx$. Conversely if $Gx = Hx$ then $\sigma x\in Hx$, say $\sigma x = hx$ with $h\in H$, and $h^{-1}\sigma\in\Stab_G(x)$ has $\chi = (-1)(-1) = -1$.

Since $[G:H]\leq2$, $G = H\cup\sigma H$ for any $\sigma$ with $\chi(\sigma)=-1$ when $\chi$ is nontrivial, so every $G$-orbit is $Hx\cup H\sigma x$, and these two are either equal or disjoint: one or two $H$-orbits. It is one exactly when $\Stab_G(x)\not\subseteq H$. Summing the number of $H$-orbits over the $G$-orbits gives the displayed identity.

The last sentence is not a formality: `computations/reports/orbit_splitting_criterion.py` checks the criterion orbit by orbit on the orthogonal groups of $A_1^{\oplus n}$ and $D_4$ acting on roots, on norm-$4$ vectors, on $L/2L$ and on root lines, and it exhibits both outcomes with $\chi$ onto $G$ — $\Orth(A_1^{\oplus2})$ on the four roots has equal counts, its regular action has unequal counts.
:::

::: {.proposition #prop:discriminant-kernel-orbits title="The discriminant kernel and the stable group have the same isotropic orbits"}

Let $B=\latI_{2,9}$, $T_\Co=B(2)$, let $K=\discriminantkernel{T_\Co}$ be the discriminant kernel and $\Gamma_\Co=\Orth^+(T_\Co)\intersect K$. Then

1. $K\neq\Gamma_\Co$, and $[K:\Gamma_\Co]=2$;
2. $K$ and $\Gamma_\Co$ have the same orbits on the primitive isotropic vectors of $T_\Co$, and the same orbits on the primitive isotropic lines.

The number of $\Gamma_\Co$-orbits is $527$ (@sec-cusp-lifting): the lifting theorem makes the $\Gamma_\Co$-orbits of primitive isotropic vectors correspond to the nonzero isotropic classes of $A_{T_\Co}$, of which there are $527$ (@prop:coble-q-fibers), which is the count of @prop:coble-cusp-count, proved in prose only with sage-extensions#286 the computation owed.
:::

::: {.proof}

*The groups differ.* $B$ is odd, so it has a unit vector $v$ with $v^2=1$, and the reflection $s_v(x) = x-2(x,v)v$ is integral and orthogonal. Modulo $2B$ it is the identity, so $s_v\in K$; and by the reflection computation of @prop:period-spinor-character, $\chi_{\mathrm{per}}(s_v) = \operatorname{sgn}(-q(v)) = -1$, because $q(v) = \tfrac12 > 0$ and $v$ is a positive vector. So $\chi_{\mathrm{per}}$ is nontrivial on $K$, which is therefore not contained in $\Orth^+$, and $[K:\Gamma_\Co]=2$ since $\chi_{\mathrm{per}}$ takes values in $\{\pm1\}$.

*The orbits agree.* By @lem:character-kernel-orbits it is enough to find, for each primitive isotropic $x$, an element of $\Stab_K(x)$ with character $-1$. Put $L=\ZZ x$; then $L^{\perp}=L\perp M$ with $M\cong\latI_{1,8}$, the splitting of @thm:plane-transitivity-tco whose quotient is computed at the owner in `computations/reports/split_quotient_I18.py`. Now $\latI_{1,8}\cong\latI_{1,1}\perp\latI_{0,7}$ has a unit vector $v$, and $v\perp L$, so $s_v$ fixes $x$ and fixes $L$ pointwise while lying in $K$ with $\chi_{\mathrm{per}}(s_v)=-1$ by the computation above. Hence every $K$-orbit is $\Gamma_\Co$-stable and the two partitions coincide.

*Vectors and lines.* The map from vector-orbits to line-orbits is surjective always, and injective here because $-\id\in\Gamma_\Co$: it acts trivially on $A_{T_\Co}$, which is $2$-torsion, and $\chi_{\mathrm{per}}(-\id)=+1$, its determinant on the positive plane being $(-1)^2$. So each line-orbit carries exactly one vector-orbit for either group.
:::

## The Eichler criterion and its hypothesis

::: {.remark title="Why the Eichler criterion is unavailable for $T_\Co$"}

By @thm:eichler-criterion, for lattices containing $U^{\oplus 2}$, $\widetilde{\SO}^+(L)$-equivalence of primitive vectors is determined by the pair $(v^2, v^*\bmod L)$.
For $T_\Co$, @prop:tco-as-twist implies that every value of $\beta_{T_\Co}$ is even, so no two vectors pair to $1$ and $T_\Co$ contains no copy of $U$; the same obstruction is recorded after @thm:eichler-criterion for $S_\Co$ and $\sen$.
An orbit statement for $T_\Co$ therefore needs a different mechanism.
For the full orthogonal group, @thm:unpolarized-cusps gives transitivity using @prop:tco-split-maximal, and for the odd $B = \latI_{2,9}$ that transitivity has a direct source which does not go through the even-lattice results at all: James' integral Witt theorem [@Jam68] applies with $r - \abs{\fs} = 11 - 7 = 4 = 2(1+1)$, and its characteristic clause is vacuous because a characteristic vector of $\latI_{p,q}$ has odd coordinates and square $\equiv p-q \equiv 1 \pmod 8$, never $0$. So transitivity on primitive isotropic *vectors* is settled for $B$; the rank-two case is not, the inequality there needing $6$, and it is recorded at @thm:split-maximal-isotropic-transitivity.

For a subgroup specified by its image in $\Orth(q)$, the algorithms of [@Daw22] do *not* apply as the citation would suggest, and the mismatch is worth stating because it is on both sides. Dawes' setup assumes even lattices from §1.1, and the split-maximal stabilizer results of §3.1 and §3.2 assume a $U^{\oplus2}$ decomposition. The Coble lattice is even but not $U^{\oplus2}$-decomposable --- as the Eichler remark below proves, $T_\Co$ contains no copy of $U$ at all --- while the odd lattice $B$ with the decomposition is outside the parity hypothesis. So neither presentation satisfies both hypotheses, and the passage from $\rho(\Gamma)$-orbits on the finite group to $\Gamma$-orbits on primitive isotropic vectors is not available from that source for $\Gamma_\Co$. What the finite computation can still do is bound: since $\Gamma_\Co$ fixes every class of $A_{T_\Co}$, vectors with different classes lie in different $\Gamma_\Co$-orbits, so the finite orbit count is a lower bound for the integral one and never an upper one.
:::

## The two $0$-cusp lattices {#sec-zero-cusp-lattices}

::: {.proposition #prop:zero-cusp-lattices title="The $0$-cusp lattices of $\fen$ and of $\fco$"}

Let $T$ be $T_\En = U\perp U(2)\perp E_8(2)$ or $T_\Co = B(2)$ with $B = U\perp U\perp \I_{0,7}$, and let $v$ be a primitive isotropic vector: the isotropic generator of a hyperbolic summand in either case.
Then the cusp lattice $v^{\perp T}/\generators{v}$ is

1. for $T_\En$, $U(2)\oplus E_8(2)$: rank $10$, determinant $-2^{10}$, signature $(1,9)$, even $2$-elementary with invariants $(r,a,\delta) = (10,10,0)$;
2. for $T_\Co$, $U(2)\oplus\generators{-2}^{7} = \I_{1,8}(2)$: rank $9$, determinant $2^{9}$, signature $(1,8)$, even $2$-elementary with invariants $(r,a,\delta) = (9,9,1)$.
:::

::: {.proof}

In both cases $v$ spans a hyperbolic summand and is orthogonal to the rest, so $v^{\perp T} = \generators{v}\perp (\text{the remaining summand})$ and the quotient by $\generators{v}$ drops the hyperbolic direction: for $T_\En = U\perp U(2)\perp E_8(2)$ this leaves $U(2)\oplus E_8(2)$, and for $T_\Co = U(2)\oplus U(2)\oplus\I_{0,7}(2)$ from the splitting of @prop:tco-split-maximal it leaves $U(2)\oplus\I_{0,7}(2) = U(2)\oplus\generators{-2}^{7}$, which is $2\cdot\I_{1,8}$ because $U\oplus\generators{-1}^{7}$ is the odd unimodular lattice of signature $(1,8)$.

The invariants are computed in `computations/reports/coble_zero-cusp-lattices.py` and its run, which builds each lattice and prints rank, determinant, signature, the elementary divisors of the Gram matrix, the order of the discriminant group, and whether the values of $q$ are all integral --- that is $\delta$: $U(2)\oplus E_8(2)$ has divisors $[2,\dots,2]$ of length $10$, $\abs{A} = 1024$, all values integral and $\delta = 0$; $\I_{1,8}(2)$ has divisors $[2,\dots,2]$ of length $9$, $\abs{A} = 512$, non-integral values and $\delta = 1$.
:::

::: {.theorem #thm:zero-cusp-chambers title="The chambers of the two $0$-cusp lattices"}

Let $K_\Co = \I_{1,8}(2)$ and $K_\En = U(2)\oplus E_8(2)$ be the cusp lattices of @prop:zero-cusp-lattices, halves $K'_\Co = \I_{1,8}$ and $K'_\En = U\oplus E_8$, and let $K(2)$ denote $K$ with the form doubled.
Then

1. $\Orth(K(2)) = \Orth(K)$, and the reflection $s_r$ of @def:spinor-norm is unchanged when the form is scaled, so the Coxeter chamber of $K(2)$ is the chamber of $K$ with every root norm doubled;

2. the chamber of $K_\En$ has **ten** walls, with Coxeter diagram the all-label-$3$ diagram CoxIter records as $\widetilde E_{10}$-shaped, one ideal vertex, and its ten walls are the roots Vinberg's algorithm returns on $E_{10}(2)$:
$$
-\eps_3,\ \dots,\ -\eps_{10},\qquad \eps_1-\eps_2,\qquad \eps_2+2\eps_3+3\eps_4+4\eps_5+6\eps_6+5\eps_7+4\eps_8+3\eps_9+2\eps_{10}
$$
in the recorded basis $\eps_1,\dots,\eps_{10}$ of $\eta_1^{\perp}/\eta_1$, the coefficients $(2,3,4,6,5,4,3,2)$ being the marks of the highest root of $E_8$;

3. the chamber of $K_\Co$ has **nine** walls: in the negative-square convention a chain of eight nodes of norms $(-2,\dots,-2,-1)$ with seven label-$3$ edges and **one** label-$4$ edge at the end, and a ninth node of norm $-2$ joined to the *third* node of the chain by a label-$3$ edge --- the chain with a leaf at node $3$, which is the row $5\leq n\leq 9$ of [@Vin72, Table 5, article p. 31] at $n = 8$, and the Gram field is $\QQ[\sqrt2]$.
:::

4. the two cusps of $T_\En$ have the same shape of chamber, both computed: on $K(L_1) = U(2)\oplus E_8(2)$ (the div-$1$ class, $\eta = e_1$) and on $K(L_2) = U\oplus E_8(2)$ (the div-$2$ class, $\eta = e_3$) Vinberg's algorithm returns **ten** walls each, with the Gram matrices printed in `computations/reports/coble_TEn-chambers-run.txt` --- nine of $-4$ and one of $-2$ in $K(L_2)$, all $-4$ in $K(L_1)$, and $b = 2$ between the pairs $(1,3),(2,4),(3,4),(4,5),(5,6),(6,7),(7,8),(8,10),(9,10)$ --- so eight label-$3$ edges and one label-$4$ edge in $K(L_2)$, nine label-$3$ edges in $K(L_1)$; CoxIter on the two graphs `computations/reports/coble_TEn-chambers_K1.coxiter` and `_K2.coxiter` reports **one ideal vertex** and field $\QQ$ for $K(L_1)$, **two ideal vertices** and field $\QQ[\sqrt2]$ for $K(L_2)$, with the simplex $f$-vector $(10,45,120,210,252,210,120,45,10,1)$ and finite covolume in both cases, so both cusp lattices are reflective; the walls lift into $T_\En = U\oplus U(2)\oplus E_8(2)$ through $K(L_1) = e_1^{\perp}/\generators{e_1}$ on the slots $e_3,f_3,\dots$ and $K(L_2) = e_3^{\perp}/\generators{e_3}$ on the slots $e_1,f_1,\dots$, and `computations/reports/coble_TEn-dictionaries.py` verifies that each lifted Gram matrix equals the provider's, both printing True.

::: {.proof}

*The scaling lemma.* The form of $K(2)$ is $2b_K$, so an endomorphism $g$ satisfies $2b_K(gx,gy) = 2b_K(x,y)$ for all $x,y$ exactly when it is an isometry of $K$: $\Orth(K(2)) = \Orth(K)$ as subgroups of $\GL(K)$. The reflection $s_r(x) = x - 2\frac{b(x,r)}{b(r,r)}r$ is homogeneous of degree $0$ in the form, so the reflection in $r$ is the same map for $K$ and for $K(2)$, and the wall it defines has norm $r^2$ in $K$ and $2r^2$ in $K(2)$. Hence the chambers correspond wall by wall, with the norms doubled.

*The Enriques half.* The record is @sec-sterk-root-counts-and-computed-chambers, whose input it names: Vinberg's algorithm on $\eta_1^{\perp}/\eta_1\cong E_{10}(2)$, of type $(10,10,0)$, returns ten roots and one ideal vertex, and the ten roots are printed there in the recorded basis; CoxIter's separate run on the same diagram, @sec-coxiter-results-for-cusp-lattices, reports dimension $9$, one vertex at infinity, Gram field $\QQ$, the simplex $f$-vector of a $9$-simplex, and the diagram as $\widetilde E_{10}$-shaped. Wall count and ideal-vertex count agree between the two, which is the check.

*The Coble half.* Computed by the recursion of [@Vin72, p. 30]: on $\I_{1,8}$ with basis $v_0,\dots,v_8$ of squares $(1,-1,\dots,-1)$, the initial roots are $e_i = -v_i+v_{i+1}$ and $e_8 = -v_8$, and the candidates are the $k_1^2+\dots+k_8^2 = k_0^2+\epsilon$ with $k_0\geq 1$, $k_1\geq\dots\geq k_8\geq0$, taken in increasing $k_0^2/\epsilon$ and kept when they pair $\geq0$ with every wall already found --- the negative-square convention, where adjacent walls of a chamber pair positively.
The bound $k_0\geq1$ is not cosmetic: the roots with $k_0 = 0$ lie in $v_0^{\perp}$, whose isometry group is $\Orth(\I_{0,8})$, of type $B_8$, and their simple system is exactly the initial $e_1,\dots,e_8$; the recursion enumerates only the walls with $(e,v_0)>0$.
The record, `computations/reports/coble_I18_vinberg-chamber.py` and its run, prints nine walls. Eight of them form the chain $e_1,\dots,e_8$ with norms $(-2,\dots,-2,-1)$, seven label-$3$ edges and one label-$4$ edge; the ninth is $v_0-v_1-v_2-v_3$ hmm more precisely the coefficient vector $(1,1,1,1,0,\dots,0)$, of norm $-2$ and $\nu = \tfrac12$, joined to $e_3$ by a label-$3$ edge.
So the diagram agrees with the published row, including the position of the leaf.

One defect is recorded with it. The in-tree row of @sec-coxiter-results-for-cusp-lattices describes the $(9,9,1)$ diagram as a "rank-$9$ chain, one label-$4$ edge"; the computed chamber has a branch node, so **that description is contradicted** --- the label count agrees, the word "chain" does not. Since the row does not name the diagram CoxIter was run on, whether its words or its input are wrong cannot be decided here, and CoxIter is to be re-run on the nine-node diagram this record prints, the row then replaced by that run.

::: {.remark title="What is not decided here"}

Reflectivity, and the Coxeter diagram the cusp lattice carries, are not decided by that record: deciding them means running Vinberg's algorithm *anchored at the chosen cusp*, which the library does not expose --- the operation would take a hyperbolic lattice together with the isotropic vector defining the cusp and return the chamber's walls with their inner products, and it is sage-extensions#285.
It is needed here on $U(2)\oplus E_8(2)$ (the Enriques cusp, where Sterk publishes the diagram) and on $\I_{1,8}(2)$ (the Coble cusp); until it exists the wall count and the identification of the diagram with the published one are not asserted, and @sec-open-problems carries them.
:::
