# Properties, structures, and classifying constructions {#sec-truncation}

Work in the 2-category $\mathbf{Cat}_{\mcu}$ fixed in @def:infinity-category-universe.
Each category of structured objects comes with a specified forgetful functor.

## Properties and structures {#sec-property-structure}

::: {.definition #def:property-structure-stuff title="Property, structure, and stuff"}
Let $U\colon\mcs\to\mcc$ be a forgetful functor.

- If $U$ is fully faithful, it describes at most a property of objects of $\mcc$.

- If $U$ is faithful, it describes at most structure on those objects.

- A general $U$ may forget stuff [@BS07, §2; @nlab:stuff_structure_property].

Repleteness is separate from these conditions.
If $U$ is fully faithful, then it induces an equivalence from $\mcs$ to its replete full essential image in $\mcc$.
An isomorphism-invariant property $P$ of objects of $\mcc$ defines the replete full subcategory $\mcc_P$ spanned by the objects satisfying $P$.
:::

::: {.proposition #prop:forgetful-homotopy-fibers title="Forgetfulness read from homotopy fibers"}
Let $U\colon\mcs\to\mcc$ be a functor between groupoids.
For $x\in\mcc$, the homotopy fiber $U^{-1}(x)$ is the groupoid of objects $e\in\mcs$ with an isomorphism $U(e)\cong x$, and of morphisms of $\mcs$ compatible with these isomorphisms.

- If every $U^{-1}(x)$ is a $(-1)$-groupoid, that is, empty or equivalent to a point, then $U$ forgets at most properties.
- If every $U^{-1}(x)$ is a $0$-groupoid, that is, equivalent to a set, then $U$ forgets at most structure.
- If the $U^{-1}(x)$ are arbitrary groupoids, then $U$ forgets stuff.

[@BS07, §2, Fact 3]
:::

::: {.proof}
This is [@BS07, §2, Fact 3].
:::

## Chosen structure

::: {.definition #def:chosen-structure title="Chosen structure as a homotopy fiber"}
A structure on $X\in\mcc$ is a chosen object of the homotopy fiber of $U\colon\mcs\to\mcc$ over $X$.
Several nonisomorphic choices may lie over the same $X$.
A morphism in $\mcs$ must preserve the chosen structure.

For example, the unit of a monoid is part of its structure.
Although a two-sided unit is unique when it exists, a semigroup homomorphism between unital semigroups need not preserve it.
Hence $\mathbf{Mon}\to\mathbf{Semigrp}$ is faithful and is not full.
:::

## Pullback of a family {#sec-pullback-general}

Let $U\colon\mcs\to\mcc$ and $F\colon\mcd\to\mcc$ be specified functors.
The structured objects of $\mcd$ obtained from $U$ are given by the pseudo-pullback $\mathcal P$ in the square

::: {.definition #def:axiom-through-functor title="Pulling back structured objects"}
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
If $U$ is a replete full inclusion, it is an isofibration, and the strict pullback presents this pseudo-pullback up to equivalence (@sec-pullback-cat).
Its objects are exactly the $D\in\mcd$ for which $F(D)$ satisfies the stated property.
:::

## Classifying objects and families {#sec-axiom-classifiers-general}

::: {.definition #def:classifying-object title="Classifying objects and universal families"}
A functor $H\colon\mcc^{\opop}\to\mcs$ is *represented* by $B\in\mcc$ when there is a natural equivalence
$$
\eta\colon H(-)\simeq\operatorname{Map}_{\mcc}(-,B).
$$
Only then is $B$ called a classifying object for $H$.

Suppose $H(X)$ is the space of families of a specified kind over $X$.
The *universal family* $p\colon E\to B$ is the family corresponding under $\eta_B^{-1}$ to $\id_B$.
Naturality identifies pullback of $p$ along $f\colon X\to B$ with the family corresponding to $f$.
Thus the equivalence $\eta$ records existence, equivalences between presentations, and automorphisms of families; mere existence of some pullback presentation is not a universal property.
:::

## Operations and endomorphism operads {#sec-operations}

Let $\mcc$ have finite products.
An $n$-ary operation on $X\in\mcc$ is a morphism
$$
\mu\colon X^{\times n}\too X.
$$
For fixed $X$, these morphisms form the arity-$n$ term of the cartesian endomorphism operad $\Endo_{\mcc}(X)$.
Composition is substitution of operations, and the symmetric-group action permutes the factors.

For an arbitrary morphism $X\to Y$, neither precomposition nor postcomposition defines a map $\Hom(X^n,X)\to\Hom(Y^n,Y)$.
Consequently the assignment $X\mapsto\Hom(X^n,X)$ is not a presheaf on $\mcc$.
Categories of algebras instead use operations and structure-preserving morphisms, as in @sec-named-categories.

## Equations and coherence {#sec-filled-diagrams}

An equation between terms is equality of two parallel morphisms obtained by composing the specified operations.
In a 2-category, a weak version may instead include a chosen invertible 2-cell between the composites; its coherence laws are further equations between 2-cells.

An operad $\mathcal O$ specifies operations, symmetric-group actions, units, and composition.
An $\mathcal O$-algebra is defined by a morphism of operads $\mathcal O\to\Endo_{\mcc}(X)$.
