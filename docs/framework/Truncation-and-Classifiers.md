# Properties, structures, and classifying constructions {#sec-truncation}

Work in the 2-category $\mathbf{Cat}_{\mathcal U}$ fixed in
@def-infinity-category-universe. Each category of structured objects comes with a
specified forgetful functor.

## Properties and structures {#sec-property-structure}

::: {#def-property-structure-stuff}
Let $U\colon\mathcal S\to\mathcal C$ be a forgetful functor.

- If $U$ is fully faithful, it describes at most a property of objects of
  $\mathcal C$.
- If $U$ is faithful, it describes at most structure on those objects.
- A general $U$ may forget stuff [@BS07, §2; @nlab:stuff_structure_property].

Repleteness is separate from these conditions. If $U$ is fully faithful, then it
induces an equivalence from $\mathcal S$ to its replete full essential image in
$\mathcal C$. An isomorphism-invariant property $P$ of objects of $\mathcal C$ defines
the replete full subcategory $\mathcal C_P$ spanned by the objects satisfying $P$.
:::

For higher categories, the same classification can be read from the homotopy fibers of
$U$: empty or contractible fibers give property, discrete fibers give structure, and
general fibers retain stuff. The definitions of truncated spaces and morphisms are in
@def-truncated.

## Chosen structure

::: {#def-chosen-structure}
A structure on $X\in\mathcal C$ is a chosen object of the homotopy fiber of
$U\colon\mathcal S\to\mathcal C$ over $X$. Several nonisomorphic choices may lie over
the same $X$. A morphism in $\mathcal S$ must preserve the chosen structure.

For example, the unit of a monoid is part of its structure. Although a two-sided unit is
unique when it exists, a semigroup homomorphism between unital semigroups need not
preserve it. Hence $\mathbf{Mon}\to\mathbf{Semigrp}$ is faithful and is not full.
:::

## Pullback of a family {#sec-pullback-general}

Let $U\colon\mathcal S\to\mathcal C$ and $F\colon\mathcal D\to\mathcal C$ be
specified functors. The structured objects of $\mathcal D$ obtained from $U$ are given
by the pseudo-pullback $\mathcal P$ in the square

::: {#def-axiom-through-functor}
```{.tikz}
%%| filename: structured-object-pullback
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
\mathcal P
  \arrow[r,"\operatorname{pr}_{\mathcal S}"]
  \arrow[d,"\operatorname{pr}_{\mathcal D}"']
  \arrow[dr,phantom,very near start,"\lrcorner"] &
\mathcal S \arrow[d,"U"]\\
\mathcal D \arrow[r,"F"'] & \mathcal C
\end{tikzcd}
```
If $U$ is a replete full inclusion, it is an isofibration, and the strict pullback
presents this pseudo-pullback up to equivalence (@sec-pullback-cat). Its objects are
exactly the $D\in\mathcal D$ for which $F(D)$ satisfies the stated property.
:::

## Classifying objects and families {#sec-axiom-classifiers-general}

::: {#def-classifying-object}
A functor $H\colon\mathcal C^{\mathrm{op}}\to\mathcal S$ is *represented* by
$B\in\mathcal C$ when there is a natural equivalence
$$
\eta\colon H(-)\simeq\operatorname{Map}_{\mathcal C}(-,B).
$$
Only then is $B$ called a classifying object for $H$.

Suppose $H(X)$ is the space of families of a specified kind over $X$. The *universal
family* $p\colon E\to B$ is the family corresponding under $\eta_B^{-1}$ to
$\operatorname{id}_B$. Naturality identifies pullback of $p$ along
$f\colon X\to B$ with the family corresponding to $f$. Thus the equivalence $\eta$
records existence, equivalences between presentations, and automorphisms of families;
mere existence of some pullback presentation is not a universal property.
:::

**Remark.** A property, equation, or forgetful functor acquires classifying terminology
only from such a represented functor or universal property.

## Operations and endomorphism operads {#sec-operations}

Let $\mathcal C$ have finite products. An $n$-ary operation on $X\in\mathcal C$ is a
morphism
$$
\mu\colon X^{\times n}\longrightarrow X.
$$
For fixed $X$, these morphisms form the arity-$n$ term of the cartesian endomorphism
operad $\operatorname{End}_{\mathcal C}(X)$. Composition is substitution of operations,
and the symmetric-group action permutes the factors.

For an arbitrary morphism $X\to Y$, neither precomposition nor postcomposition defines
a map $\operatorname{Hom}(X^n,X)\to\operatorname{Hom}(Y^n,Y)$. Consequently the
assignment $X\mapsto\operatorname{Hom}(X^n,X)$ is not a presheaf on $\mathcal C$.
Categories of algebras instead use operations and structure-preserving morphisms, as in
[Algebraic categories from operations](Mathematical-Framework.md).

## Equations and coherence {#sec-filled-diagrams}

An equation between terms is equality of two parallel morphisms obtained by composing
the specified operations. In a 2-category, a weak version may instead include a chosen
invertible 2-cell between the composites; its coherence laws are further equations
between 2-cells.

An operad $\mathcal O$ specifies operations, symmetric-group actions, units, and
composition. An $\mathcal O$-algebra is defined by a morphism of operads
$\mathcal O\to\operatorname{End}_{\mathcal C}(X)$. Claims involving
$A_\infty$, $E_n$, or $E_\infty$ structures name the chosen operad or a cited equivalent
model.
