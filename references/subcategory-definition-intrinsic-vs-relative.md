# Subcategory definition: intrinsic vs relative subobjects

Source: ChatGPT conversation on infty-categorical inclusions, 2026-07-15. Establishes the correct definition of subobject/subcategory and the distinction between intrinsic subobjects (monomorphisms) and relative induced subobjects (cartesian over a monic).

## 1. Intrinsic subobjects

Let $\mathbb K$ be an ambient $(\infty,2)$-category and let $\mathcal C$ be an $(\infty,1)$-category represented as an object of $\mathbb K$.
Objects $X,Y\in\mathcal C$ are points
$$
\iota_X,\iota_Y:\mathbf 1\longrightarrow \mathcal C,
$$
and a morphism $m:X\to Y$ is a $2$-cell.
Since $\mathbb K(\mathbf 1,\mathcal C)\simeq \mathcal C$, a condition on this $2$-cell is precisely a condition on $m$ as a morphism of $\mathcal C$.

The canonical intrinsic definition is:
$$
\boxed{
X\hookrightarrow Y \text{ is a subobject of } Y \iff m:X\to Y \text{ is a monomorphism in } \mathcal C.
}
$$
Equivalently, $m$ is a subterminal object of the slice $\mathcal C_{/Y}$.
If the relevant pullback exists:
$$
m \text{ is monic} \iff \Delta_m:X\longrightarrow X\times_Y X \text{ is an equivalence}.
$$

No functor $\Pi_\infty$ or passage to an underlying space is needed.
The mapping-space formulation is merely one semantic characterization of the diagonal condition.
Kerodon defines subobjects exactly as monomorphisms, regarded as subterminal objects of a slice.
([Kerodon, Tag 04VD](https://kerodon.net/tag/04VD))

**The datum is the arrow $m:X\to Y$, not merely the domain $X$.**

## 2. This recovers the strict 1-categorical examples

For $\mathbf{Set}$, monomorphisms are injective functions, and their isomorphism classes over $Y$ are precisely subsets of $Y$.

For $R$-modules, monoids, groups, rings, and $R$-algebras, monomorphisms are injective homomorphisms.
Each such map is isomorphic over its codomain to the inclusion of its image.

### Proposition

A functor $F:\mathcal A\longrightarrow\mathcal B$ is a monomorphism in the ordinary category $\mathbf{Cat}$ if and only if $F$ is injective on objects and faithful.

### Proof

If $F$ is monic, apply left cancellation to functors $\mathbf 1\rightrightarrows\mathcal A$ to obtain injectivity on objects.
Given $f,g:a\to a'$ with $Ff=Fg$, regard $f$ and $g$ as functors $[1]\rightrightarrows\mathcal A$.
Their composites with $F$ agree, so monicity gives $f=g$.
Hence $F$ is faithful.

Conversely, suppose $F$ is injective on objects and faithful.
If $FG=FH$ for $G,H:\mathcal X\to\mathcal A$, injectivity gives $Gx=Hx$ for every object $x$, and faithfulness gives $G\alpha=H\alpha$ for every morphism $\alpha$.
Thus $G=H$.
∎

$$
\boxed{
\text{subobjects in } \mathbf{Cat} = \text{ordinary subcategories, up to isomorphism over the parent.}
}
$$

## 3. The distinction between $N(\mathbf{Cat})$ and $\operatorname{Cat}_\infty$

The remaining issue is not the definition of subobject.
It is the ambient category in which monicity is tested.

In $N(\mathbf{Cat})$, mapping spaces are discrete sets of functors.
Hence an ordinary monomorphism in $\mathbf{Cat}$ remains a monomorphism in $N(\mathbf{Cat})$.

By contrast, the mapping space in $\operatorname{Cat}_\infty$ from $\mathcal A$ to $\mathcal B$ contains functors together with natural equivalences between them.
Consequently, the evident functor $N(\mathbf{Cat})\longrightarrow\operatorname{Cat}_\infty$ is not fully faithful.

It follows that this functor need not preserve monomorphisms.
Indeed, $B\mathbb N\longrightarrow B\mathbb Z$ is not monic in $\operatorname{Cat}_\infty$.
A monomorphism $F:\mathcal A\to\mathcal B$ in $\operatorname{Cat}_\infty$ must induce monomorphisms on mapping spaces and must contain, in their effective images, every equivalence between objects in the image.
For $B\mathbb N\to B\mathbb Z$, the negative integers are ambient automorphisms which have no preimage.
([MathOverflow](https://mathoverflow.net/questions/345686))

Thus the inference $\mathbf{Cat}_1\subseteq\mathbf{Cat}_\infty \Longrightarrow \text{monos in } \mathbf{Cat}_1 \text{ remain monos in } \mathbf{Cat}_\infty$ is invalid unless the displayed arrow is genuinely a fully faithful inclusion of the relevant higher categories.

$$
\begin{aligned}
\operatorname{Sub}_{N(\mathbf{Cat})}(\mathcal B) &= \text{ordinary subcategories of } \mathcal B,\\
\operatorname{Sub}_{\operatorname{Cat}_\infty}(\mathcal B) &= \text{homotopy-invariant categorical subobjects of } \mathcal B.
\end{aligned}
$$

The latter is necessarily saturated with respect to specified ambient equivalences.
An arbitrary strict subcategory is not invariant under equivalence of presentations.

## 4. Relative subobjects obtained by imposing structure

Let $U:\mathcal C\longrightarrow\mathcal D$ be a functor, where objects of $\mathcal C$ are objects of $\mathcal D$ equipped with additional structure.
For $X\in\mathcal C$, define an induced $U$-subobject of $X$ to be a morphism $m:X'\longrightarrow X$ such that $U(m):U(X')\hookrightarrow U(X)$ is an intrinsic subobject in $\mathcal D$, and $m$ is $U$-cartesian.

$$
\boxed{
\operatorname{Sub}_U(X) = \left\{ m:X'\to X : U(m)\in\operatorname{Mono}(\mathcal D),\ m\text{ is }U\text{-cartesian} \right\}/\simeq .
}
$$

Cartesianness says that the structure on $X'$ is exactly the structure induced from $X$ along the underlying subobject, rather than an unrelated structure on the same underlying datum.
The defining universal property is a pullback condition on hom-objects.
([Kerodon, Tag 01TK](https://kerodon.net/tag/01TK))

Moreover, such an $m$ is automatically an intrinsic monomorphism in $\mathcal C$: for every $Z$, cartesianness identifies composition with $m$ as the pullback of composition with $U(m)$, and pullbacks preserve monomorphisms.

Examples:

| $U$ | $U(m)$ | $U$-cartesian lift |
| --- | --- | --- |
| $R\text{-}\mathbf{Mod}\to\mathbf{Set}$ | subset | submodule with restricted operations |
| $\mathbf{Mon}\to\mathbf{Set}$ | subset | submonoid |
| $R\text{-}\mathbf{Alg}\to\mathbf{Set}$ | subset | subalgebra |
| $\mathbf{Pos}\to\mathbf{Set}$ | subset | induced subposet |
| $\mathbf{Top}\to\mathbf{Set}$ | subset | subspace topology |

## 5. Resulting architecture

$$
\boxed{
\begin{aligned}
\textbf{Intrinsic subobject:}\quad& m:X\to Y \text{ monic in } \mathcal C;\\
\textbf{Relative induced subobject:}\quad& m:X'\to X \text{ cartesian over a monic } U(m);\\
\textbf{Subobject classifier:}\quad& \text{an object representing the resulting subobject doctrine.}
\end{aligned}}
$$

The classifier is optional.
The intrinsic subobject notion exists before and independently of it.

The only unresolved point is which ambient higher category is intended when an $\infty$-category itself is treated as an object.
Monicity in $N(\mathbf{Cat})$, monicity in $\operatorname{Cat}_\infty$, and a higher-cell embedding inside an $(\infty,2)$-category are genuinely different notions.

## References

- [Kerodon, Tag 04VD](https://kerodon.net/tag/04VD) — Monomorphisms

- [Kerodon, Tag 01TK](https://kerodon.net/tag/01TK) — Cartesian Morphisms of $\infty$-Categories

- [MathOverflow: Monomorphisms in $\mathcal{C}at_\infty$](https://mathoverflow.net/questions/345686)
