# Joins, meets, and closure {#sec-join-meet}

## The inclusion preorder

Fix a $\mathcal U$-small category $C$. Let $\operatorname{RFull}(C)$ be the preorder of
replete full subcategories of $C$, ordered by inclusion. Equivalently, its elements are
isomorphism-invariant properties of objects of $C$, ordered by implication.

::: {#def-replete-full-meet}
## Meets

For $A,B\in\operatorname{RFull}(C)$, their meet is the replete full subcategory on the
objects lying in both $A$ and $B$. It is represented by the pullback

```{.tikz}
%%| filename: full-subcategory-intersection
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
A\cap B
  \arrow[r,"\operatorname{pr}_B"]
  \arrow[d,"\operatorname{pr}_A"']
  \arrow[dr,phantom,very near start,"\lrcorner"] &
B \arrow[d,hook]\\
A \arrow[r,hook] & C
\end{tikzcd}
```
Its universal property is the greatest lower bound in
$\operatorname{RFull}(C)$.
:::

::: {#def-join-diagram}
## Joins

The join of $A$ and $B$ is the replete full subcategory on the objects lying in $A$ or
$B$. It is the least upper bound in $\operatorname{RFull}(C)$. Thus disjunction of two
object properties is a valid property and defines a full subcategory.

**Remark.** The categorical coproduct $A\sqcup B$ remembers which summand supplied an
object. Its universal property differs from the least-upper-bound property of the join.
:::

## Closure under specified operations

Suppose a family of operations on subcategories has been specified. The closure of a
family $\{A_i\}$ is the meet in $\operatorname{RFull}(C)$ of all replete full
subcategories containing every $A_i$ and closed under those operations. Since $C$ is
$\mathcal U$-small, this collection is a $\mathcal U$-set. The operations and the
required closure conditions are part of the definition.

## Categories of structured objects

The compatible combination of forgetful functors $U\colon\mathcal A\to C$ and
$V\colon\mathcal B\to C$ is the pseudo-pullback
$\mathcal A\times_C\mathcal B$ from @sec-pullback-cat. When both functors identify
replete full subcategories, this pseudo-pullback represents their meet in
$\operatorname{RFull}(C)$. A general pair of forgetful functors specifies structured
objects over $C$ and hence lies outside that preorder.

Implementation functions whose names include "join" or "meet" are interpreted only
after their own order convention and universal property have been stated. The Sage
convention is documented in the Sage realization chapters.
