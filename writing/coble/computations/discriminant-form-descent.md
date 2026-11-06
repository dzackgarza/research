---
title: Discriminant-form descent
unit: method
status: reusable
tags:
  - discriminant-form
  - descent
  - isotropic-orbits
  - cusps
  - method
notes: |-
  Provenance: the invariant-orbit statements of [@AE22] and [@GHS08] as used by the Coble chapter; the
  failure entries are the records named in the register, each of which was run at the provider pin it
  names.
---

# Discriminant-form descent {#sec-discriminant-descent}

A counting problem about primitive isotropic vectors of an indefinite lattice is often attacked by passing to the discriminant group, where the set of classes is finite and the isometries act through the representation $\rho_{L,q}$.
This page states the mechanism, the hypotheses under which it holds, and the cases in the tree where it was tried and did not hold, each with the record that shows it.

## The mechanism {#sec-descent-mechanism}

::: {.definition #def:descent-class title="The descent class of a primitive vector"}

Let $L$ be an even nondegenerate lattice with discriminant group $A_L=L^\sharp/L$ and discriminant form $q_L$.
For a nonzero $v\in L$ the divisibility $\div_L(v)$ of @def:lattice-divisibility is a positive integer, and
$$
v^* \definedas \frac{v}{\div_L(v)} \in A_L
$$
is its **descent class**.
Write
$$
\mathcal C(L) \definedas \theset{c \in A_L \st q_L(c) = 0}
$$
for the set of isotropic classes, the zero class included.
:::

::: {.lemma #lem:descent-well-defined title="The descent class is isotropic and equivariant"}

Let $v \in L^{\mathrm{prim}}[0]$ be a primitive isotropic vector.
Then $q_L(v^*) = 0$, so $v^* \in \mathcal C(L)$; and for every $g \in \Orth(L)$ one has $(gv)^* = \rho_{L,q}(g)(v^*)$, where $\rho_{L,q}$ is the quadratic discriminant representation of $\Orth(L)$ on $A_L$.
:::

::: {.proof}

$v$ primitive means $v/\div_L(v) \in L^\sharp$, so $v^*$ is a class, and $q_L(v^*) = (v^*)^2 \bmod 2\bZ = v^2/\div_L(v)^2 = 0$ because $v$ is isotropic.
An isometry preserves $\beta$, hence $\div_L(gv) = \div_L(v)$, and it passes to $A_L$ because it maps $L$ to $L$; so $(gv)^* = \rho_{L,q}(g)(v^*)$.
:::

So the class is an invariant of the orbit, and the orbits of $\Gamma\leq\Orth(L)$ map onto the orbits of $\rho_{L,q}(\Gamma)$ on the *finite* set $\mathcal C(L)$.
Everything that can still differ inside a fibre is the subject of the next section.

## The fibre over a class {#sec-descent-fibre}

::: {.proposition #prop:descent-fibre title="The fibre index"}

Let $L$ be an even nondegenerate lattice whose quadratic discriminant representation is *onto* its image group, so that $\rho_{L,q}(\Orth(L)) = \Orth(A_L,q_L)$; this is hypothesis (H1) below.
Let $c \in \mathcal C(L)$ be a class attained by a primitive isotropic vector $v$, and put
$$
\iota(c) \definedas \qty[\Stab_{\Orth(A_L,q_L)}(c) : \rho_{L,q}\qty(\Stab_{\Orth(L)}(v))].
$$
Then the primitive isotropic vectors of $L$ with $v^* = c$ meet exactly $\iota(c)$ orbits of $\Orth(L)$, and $\iota(c)$ does not depend on the choice of the vector $v$ representing $c$.
:::

::: {.proof}

Write $\mathcal F_c$ for the set of primitive isotropic $v$ with $v^*=c$, and let $v\in\mathcal F_c$.
An isometry $g$ carries $v$ into $\mathcal F_c$ exactly when $\rho_{L,q}(g)$ fixes $c$: indeed $(gv)^* = \rho_{L,q}(g)(c)$ by @lem:descent-well-defined, and $\rho_{L,q}(g)$ fixing $c$ is what makes that class equal to $c$.
Consequently the isometries carrying $v$ to a point of $\mathcal F_c$ are those with $\rho_{L,q}(g) \in \Stab_{\Orth(A_L,q_L)}(c)$.

For $w \in \mathcal F_c$ choose $g$ with $gv = w$; then $\rho_{L,q}(g)$ fixes $c$, and the set of isometries carrying $v$ to $w$ is the coset $g\,\Stab_{\Orth(L)}(v)$.
Its image under $\rho_{L,q}$ is the coset $\rho_{L,q}(g)\,\rho_{L,q}(\Stab_{\Orth(L)}(v))$ of the subgroup $\rho_{L,q}(\Stab_{\Orth(L)}(v))$ inside $\Stab_{\Orth(A_L,q_L)}(c)$, so two points of $\mathcal F_c$ lie in the same orbit exactly when these cosets agree; and conversely every coset is realized, by (H1), by taking $g$ with the required image.
So the orbits on $\mathcal F_c$ are the cosets of $\rho_{L,q}(\Stab_{\Orth(L)}(v))$ in $\Stab_{\Orth(A_L,q_L)}(c)$, and their number is the index.

For independence of $v$: if $w = gv$ then $\Stab_{\Orth(L)}(w) = g\Stab_{\Orth(L)}(v)g^{-1}$, whose image is the conjugate $\rho_{L,q}(g)\rho_{L,q}(\Stab_{\Orth(L)}(v))\rho_{L,q}(g)^{-1}$ inside $\Stab_{\Orth(A_L,q_L)}(c)$, and conjugates have equal index.
:::

::: {.corollary #cor:descent-count title="The count of orbits by classes"}

Keep (H1) and let $\Gamma\leq\Orth(L)$ be a subgroup with $\rho_{L,q}(\Gamma) = \Orth(A_L,q_L)$ as well.
Let $\mathcal O$ be a set of representatives of the orbits of $\rho_{L,q}(\Gamma)$ on the attained classes of $\mathcal C(L)$.
Then the number of $\Gamma$-orbits of primitive isotropic vectors of $L$ is
$$
\sum_{c\in\mathcal O}\qty[\Stab_{\Orth(A_L,q_L)}(c) : \rho_{L,q}(\Stab_\Gamma(v_c))],
$$
where $v_c$ is any primitive isotropic vector with $v_c^* = c$.
In particular, for $\Gamma$ inside the discriminant kernel — where $\rho_{L,q}(\Gamma) = 1$ and every attained class is its own orbit — the sum collapses to one orbit per class as soon as each fibre is filled in the sense of @prop:descent-eichler.
:::

::: {.proof}

A $\Gamma$-orbit lies inside a single fibre, because the class is $\rho_{L,q}(\Gamma)$-invariant (@lem:descent-well-defined), and $\rho_{L,q}(\Gamma)$ acts transitively on the classes of each of its orbits, so the fibres over one $\rho_{L,q}(\Gamma)$-orbit contribute together.
Within the fibre over $c$, the coset argument of @prop:descent-fibre applies with $\Orth(L)$ replaced by $\Gamma$ and hypothesis (H1) by $\rho_{L,q}(\Gamma) = \Orth(A_L,q_L)$: the orbits are the cosets of $\rho_{L,q}(\Stab_\Gamma(v_c))$ in $\Stab_{\Orth(A_L,q_L)}(c)$, and their number is the index shown.
:::

## When the fibre is a single orbit {#sec-descent-eichler}

::: {.proposition #prop:descent-eichler title="Eichler filling"}

Let $L$ contain $U\perp U_1\perp L_0$ as an orthogonal summand, with $U_1$ a second hyperbolic plane.
Then for primitive isotropic $v,v'$ with $v^* = v'^*$ in $A_L$ there is $g\in\widetilde{\SO}^+(L)$ with $g(v) = v'$; in particular every fibre of the descent map is a single orbit of the discriminant kernel, $\iota(c) = 1$, and for every $\Gamma$ with $\widetilde{\SO}^+(L)\subseteq\Gamma\subseteq\Orth^+(L)$ the $\Gamma$-orbits of primitive isotropic vectors are exactly the $\rho_{L,q}(\Gamma)$-orbits of the classes in $\mathcal C(L)$.
:::

::: {.proof}

This is @thm:eichler-criterion with $v_1^2 = v_2^2 = 0$: equal squares and equal classes are its two hypotheses, and its conclusion is an element of $\widetilde{\SO}^+(L)$ carrying $v$ to $v'$.
A single orbit on the fibre means the index of @prop:descent-fibre is $1$; and a $\Gamma$ containing the kernel inherits the transitivity on each fibre while acting on the set of fibres through $\rho_{L,q}(\Gamma)$.
:::

The two propositions measure the two ways the mechanism can fail to give a count directly: the *lattice* can fail to contain two hyperbolic planes, or the *group* can fail to see enough of $\Orth(A_L,q_L)$.
What neither covers is the case in which the descent is run against a different lattice, or in which the fibre itself needs a gluing invariant; those are entries in the register below.

## The register of failures {#sec-descent-failures}

| Work unit | What was attempted | Evidence | Replacement in use |
|:---|:---|:---|:---|
| $F_{\ten}$ 0-cusps, #684 | Descent to an auxiliary lattice $K=U\oplus E_8\oplus \latI_{1,1}$ of a *different* discriminant, $A_K=0$ against $A_{\ten}\cong(\bZ/2)^{10}$ | `computations/reports/coble_enriques-zero-cusps.py` and its run: $\abs{A_{\ten}} = 1024$, $q$ integral, $527$ nonzero isotropic classes | Withdrawn; the count is proved in `sections/1-part-combinatorial/3-chapter-enriques-k3/450-scattone.md` from the type trichotomy, which needs no descent at all |
| Dawes' Example 2.2, #662 | Equal square, equal divisibility, isometric complement and equal class in $A_L$, read as one orbit | `computations/reports/coble_dawes-example-2-2_gluing-class.py`: the fibre over the class also needs the gluing class of $\Lambda\leq A_{\generators{v}}\oplus A_N$, and here two of its three classes are excluded by integrality | The gluing class, counted as one class, so that $v_1\sim v_2$ |
| Coble plane half, #667 and #737 | The filling step of @prop:descent-eichler applied to the plane quotient $P^{\perp}/P\cong\latI_{0,7}$ | `computations/reports/coble_theta-half-requirements.md` | Open; see @sec-descent-coble |
| $\Gamma_\Co$ stabilizer, #689 | $\Orth(A,q)$ acting on the $2048$ classes, and `stabilizer_of_element` on a class | `computations/reports/coble_discriminant-stabilizer-orbits.py`: the call did not return in $900$ s or $1800$ s, while $|\Orth(A,q)|$ took $83$ s | Subgroup on generators, then the action restricted to the isotropic classes; the full-module orbit call does not finish |
| Heegner generator checks, #722 | The global `strict_checking(True)` around the discriminant form | `computations/reports/coble_heegner-generator-checks.py`: $T.\texttt{discriminant\_quadratic\_form}()$ raises `AttributeError: 'OwnedModuleMor…' object has no attribute 'is_zero'` through `correlation_morphism().cokernel()` | The flag stays off, and the three checks that do not need it are applied |
| $O(T_\Co)$ surjectivity, #667 | `discriminant_quadratic_form()` on the odd lattice $B$ | `computations/reports/coble_tco_surjectivity_specimen-port991b88b0-run.txt` | The even twist $B(2) = T_\Co$ of @prop:tco-as-twist, on which the refinement exists |

: Failures of discriminant-form descent in this tree. {#tbl:descent-failures}

## The Coble case {#sec-descent-coble}

Take $T_\Co = B(2)$ with $B = \generators{1}\oplus U\oplus E_8(-1)$ (@prop:tco-as-twist), so that $\Orth(T_\Co) = \Orth(B)$ as subgroups of $\GL(B)$ and the discriminant form is that of $B$.
The provider run in `computations/reports/coble_528_isotropic_classes.py` returns $2048$ classes for $A_{T_\Co}$, of which $528$ are isotropic, the zero class among them; so $\mathcal C(T_\Co)$ has $527$ nonzero elements.
The order is $|\Orth(A,q)| = 46\,998\,591\,897\,600$, and $\rho_{T_\Co,q}$ is onto $\Orth(A,q)$ by @thm:two-elementary-surjectivity, so (H1) holds.

*The vector half, settled.* For $\Gamma_\Co$ the descent group is the kernel, $\rho_{T_\Co,q}(\Gamma_\Co) = 1$; every isotropic class is then its own orbit, and @cor:descent-count with the filling of @prop:descent-eichler — $T_\Co$ contains $U\perp U(2)$, two hyperbolic planes — gives $527$ orbits of primitive isotropic vectors, one per nonzero isotropic class. That is the count recorded in `computations/reports/coble_isotropic_orbits.py`, and it is what the $0$-cusp statements of @sec-discriminant-orbits use.

*The plane half, open.* For a primitive isotropic plane $P$ the same mechanism would run on the quotient $P^{\perp}/P$, which is $\latI_{0,7}$; the fibre over the class of $P$ is governed by
$$
\Stab_{\Orth(A,q)}(c_P)\,\big/\,\rho_{T_\Co,q}\qty(\Stab_{\Orth(B)}(P)),
$$
and filling it requires the image of $\Orth(\latI_{0,7})$, of order $2^7\cdot 7! = 645\,120$, in $\Orth(\generators{-\tfrac12}^{7})$.
Hypothesis (H1) is not available there: $\latI_{0,7}$ is negative definite, and the surjectivity of @thm:two-elementary-surjectivity is a statement about indefinite lattices.
The missing hypothesis is exactly that surjectivity, equivalently the provider operation that returns the image of $\Orth$ of a *definite* lattice in the orthogonal group of its discriminant form, which is sage-extensions#286; the plane table $1575, 270, 9450, 3780, 8640$ of @sec-open-problems is marked unverified for this reason, and `computations/reports/coble_theta-half-requirements.md` states the requirement in full.

The pages that use the mechanism are @sec-isotropic-orbits-and-tits-buildings for the orbit algorithms, @sec-discriminant-orbits for the $0$-cusp count; and the Enriques section of `sections/1-part-combinatorial/3-chapter-enriques-k3/450-scattone.md` reaches its count through the type trichotomy instead, recording why descent is not needed there.
