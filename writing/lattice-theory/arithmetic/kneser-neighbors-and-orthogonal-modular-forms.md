# Kneser neighbors and orthogonal modular forms {#sec-kneser-neighbors}

## Cusps and positive-definite lattices

Let $L=II_{n,2}$, with $n>2$, and let $\Gamma$ be its integral orthogonal
or special orthogonal group. The arithmetic quotient

$$
X_\Gamma=\Gamma\backslash\operatorname{O}_{n,2}(\mathbb R)
\big/\bigl(\operatorname{O}_n(\mathbb R)\times
\operatorname{O}_2(\mathbb R)\bigr)
$$

is noncompact. Its Baily–Borel compactification adds finitely many boundary
components of complex dimension zero or one. These cusps correspond to
$\Gamma$-orbits of rational isotropic lines and planes, respectively.

For a rational isotropic plane $U\subset L\otimes\mathbb Q$, put
$I=U\cap L$. This is a primitive isotropic sublattice of rank two. The
induced form on

$$
D_I=I^\perp/I
$$

is positive definite, even, and unimodular, of rank $n-2$. For the orthogonal
group, the isometry classes in the genus $II_{n-2,0}$ parameterize the
one-dimensional cusps. The genus here means the collection of classes,
not a single positive-definite lattice. For the special orthogonal group,
one retains proper isometry classes and the corresponding orientation data;
this is the distinction represented by the oriented class space in the source.

Thus positive-definite lattice classes index the boundary components on which
an orthogonal modular form restricts to elliptic modular forms. The map $\Phi$
collects those restrictions. This explains why its target combines elliptic
modular forms with a vector space of lattice classes, and why Kneser-neighbor
operators enter the boundary-value calculation.

See [@MS26, §§1 and 5].

## Genus classes and enumeration

Distinguish the genus of the indefinite ambient lattice from the
positive-definite genus that indexes its one-dimensional cusps. For
$n>2$ and $n\equiv2\pmod8$, uniqueness of the indefinite even unimodular
lattice gives

$$
\operatorname{Cl}(II_{n,2})=\{[II_{n,2}]\},\qquad
\operatorname{cl}(II_{n,2})=1.
$$

Here $\operatorname{Cl}(L)$ means the isometry classes in the genus of $L$,
and $\operatorname{cl}(L)$ is its cardinality. The uniqueness statement is
recalled in [@MS26, §5].
It does not imply that the positive-definite genus $II_{n-2,0}$ has one class.
Distinct positive-definite complements can give the same indefinite lattice
after adjoining two hyperbolic planes.

The computational notes describe a preamble interface in which `L.genus()`
denotes the finite set of isometry classes, that is, $\operatorname{Cl}(L)$.
The recorded interface separates this set from its enumeration:

| Mathematical datum | Preamble expression | Computation in the source |
| --- | --- | --- |
| Class set in the genus | `G = L.genus()` | Stores the representative lattice; enumeration is deferred |
| A lattice from each class | `G.representatives()` | Calls `_genus_classes` |
| Class number | `G.class_number()` or `L.genus_class_number()` | Counts the computed representatives |
| Cardinality of the class set | `G.cardinality()` | Uses the same enumeration |

For indefinite lattices of rank at least three, the recorded `_genus_classes` route constructs
one representative per improper spinor genus, using the equality of spinor
genus and isometry class in this setting. Thus an indefinite computation route
exists in the source; the class number is not implemented as a separate
constant-time use of unimodular classification.

For a positive-definite representative $D$ of $II_{n-2,0}$, the recorded route
uses neighbor enumeration and checks that the accumulated reciprocal
automorphism orders equal the genus mass. The source imposes
`max_classes=10**6` on each neighbor iteration and asserts mass equality before
returning. This is an implemented enumeration route, not a claim of practical
completion in every rank. Computing the class number follows that enumeration;
the mass alone is a weighted sum, not the number of classes.

These are historical implementation observations from the computational
notes, whose source path was `sage_extensions/categories/lattices.py`.
They do not establish the behavior of a current checkout, and no runtime
computation of these expressions accompanies them. The class number one
for the indefinite family is a mathematical conclusion independent of that
runtime status.

## The eigenvalue identity

Let $II_{n,2}$ be an even unimodular lattice of signature $(n,2)$, with
$n>2$ and $n\equiv2\pmod8$. Put $k=n/2-1$ and
$\Gamma_n=\operatorname{O}^{+}(II_{n,2})$. Use the character
$\chi\in\{1,\det\}$ and the corresponding space
$\mathbb C[II_{n-2,0}^{\chi}]$ of lattice classes from the source.

Müller–Scheithauer prove the following identity [@MS26, Theorem 5.4]. Suppose
$F\in M_k(\Gamma_n,\chi)$ has cusp restriction $\Phi(F)=f\otimes v$, where
$f\in M_k(\operatorname{SL}_2(\mathbb Z))$, $c_f(1)=1$, and
$v\in\mathbb C[II_{n-2,0}^{\chi}]$. For each prime $p$,

$$
T_{\mathbb Z/p\mathbb Z}v
=c_f(p)\frac{p^k-1}{p-1}v.
$$

The determinant-character space retains differences of the two orientations
of chiral lattice classes. Its operator must retain that information.

The paper's broader existence and classification results invoke hypothesis
(H1), a weighted fundamental lemma, where stated. The displayed theorem has
no such assumption.

Source: [@MS26, §§2 and 5; version 1].

## What a neighbor matrix computes

For lattices in a common rational quadratic space, a $p$-neighbor has an
intersection of index $p$ in each lattice. Passing to isometry classes converts
this relation into a finite counting operator in the positive-definite setting
used here. Multiplicities matter: distinct neighbors can belong to the same
isometry class.

For a basis indexed by the relevant classes, fix the convention
$(Nv)_i=\sum_jN_{ij}v_j$. The theorem then prescribes the equation

$$
Nv=c_f(p)(1+p+\cdots+p^{k-1})v.
$$

The finite geometric sum makes the scalar factor exact. If the coefficients
lie in a number field, both sides can be compared in that exact field. A
floating-point residual would weaken an equality that is algebraic.

The vector $v$ must be known in the same basis as $N$. Deriving an eigenvector
from a candidate matrix and observing that the matrix has that eigenvector
does not test the source's prediction. The independent data are the identified
cusp restriction and its coefficients.

## Strength and limits of the assertion

The equation constrains the action on the span of $v$. If an error matrix $E$
satisfies $Ev=0$, then $N+E$ satisfies the same equation. Therefore this relation
alone cannot determine the whole neighbor matrix. Further independently known
vectors or entrywise mathematical assertions can impose further constraints.

Orientation is equally important. Replacing a signed action on orientation
differences by unsigned neighbor counts changes the operator. A SageMath
implementation must match the basis, multiplicities, character, and action
convention before this theorem gives an applicable exact assertion.

The cusp restriction connects indefinite orthogonal geometry to
positive-definite lattices of rank $n-2$. Using that connection for isotropic
plane orbits would additionally require representatives and a proof of
exhaustion under the chosen arithmetic group. Those computational obligations
are separate from the eigenvalue equation.

See also [Modular forms, Hecke operators and L-functions](#sec-modular-forms-hecke)
and the [integral-lattice overview](#sec-computational-integral-lattices).
