---
title: KSB88
authors:
- '91'
- "299\u2013338 (1988)"
year: ''
bibkey: KSB88
tags:
- paper
- extraction
abstract: |
  
---

Invent.
math.
91, 299–338 (1988)

Inventiones mathematicae © Springer-Verlag 1988

# Threefolds and deformations of surface singularities

J. Kollár $^{1\star}$ and N.I. Shepherd-Barron $^{2\star\star}$

$^{1}$ Harvard University Cambridge, MA 02138, USA $^{2}$ University of Pennsylvania Philadelphia, PA 19104, USA

## § 1. Introduction

The central theme of this article is the study of deformations of surface singularities using recent advances in three dimensional geometry.
The basic idea is the following.
Let $X_0$ be a surface singularity and consider a one parameter deformation $\{X_0: t \in \Delta\}$.
Then the total space $X = \cup X_t$ is a three-dimensional object.
One can attempt to use the geometry of $X$ to get information about the surface $X_t$.

In general $X$ is very singular and so one can try to study it via a suitable resolution of singularities $f \colon X' \to X$.
The existence of a resolution was established by Zariski; the problem is that there are too many of them, none particularly simple.

Mori and Reid discovered that the best one can hope for is a partial resolution $f \colon X' \to X$ where $X'$ possesses certain mild singularities but otherwise is a good analog of the minimal resolution of surface singularities.

The search for such a resolution is known as Mori’s program (see e.g. [Ko 3, KMM]). After substantial contributions by several mathematicians (Benveniste, Kawamata, Kollár, Mori, Reid, Shokurov, Viehweg) this was recently completed by Mori [Mo 3].

A special case, which is nonetheless sufficient for the applications presented here, was settled by several persons.
A proof was first announced by Tsunoda [TsM], later followed by Shokurov [Sh], Mori [Mo 2] and Kawamata [Kaw 2]. A precise formulation of the result we need will be provided at the end of the introduction.

In certain situations $X_0$ will impose very strong restrictions on $X'$ and one can use this to obtain information about $X$ and $X_t$ for $t \neq 0$.

The first application is in chapter two.
Teissier [Te] posed the following problem.
Let $\{X_s \colon s \in S\}$ be a flat family of surfaces parameterized by the connected space $S$.
Let $\bar{X}_s$ be the minimal resolution of $X_s$.
In general $\{\bar{X}_s \colon s \in S\}$ is not a flat family of surfaces, and it is of interest to find necessary and sufficient conditions for this to hold.

* * *

$^{\star}$ Current address: University of Utah Salt Lake City, UT 84112, USA $^{\star\star}$ Current address: University of Illinois Chicago, IL 60680, USA

300 J. Kollár and N.I. Shepherd-Barron

If $\{\bar{X}*s\colon s\in S\}$ is a flat family, then $K*{\bar{X}_s}^2$ is locally constant on $S$.
One can hope that the converse is also true (at least after a finite and surjective base change).
This was proved by Laufer [La, 5.7] under the additional assumption that the $X_s$ have isolated Gorenstein singularities.
The main result of chapter two (2.10) generalizes this to the case where the $X_s$ have arbitrary isolated singularities.
In the presence of nonisolated singularities the converse is usually false.

Chapter three provides a new approach to the study of the deformation space of a quotient singularity.
The main result (Theorem 3.9) relates the irreducible components of the deformation space to certain partial resolutions of the singularity.
This gives an algorithm to compute the number of components of the deformation space and the dimension of the components in terms of the dual graph of the minimal resolution.
It is our belief that this method will lead eventually to the understanding of all small deformations of a quotient singularity, but so far our attempts have been frustrated.

The next two chapters contain results pertaining to the problem of compactifying the moduli of surfaces.
This involves the study of certain singular surfaces that appear as limits of smooth ones.
A good class of such singular surfaces is suggested by the above-mentioned results of three dimensional geometry.
The possible singularities of such surfaces are introduced and classified in chapter four.
This generalizes earlier results of Kawamata [Kaw1, Kaw2]. In chapter five the deformations of these singularities are analyzed.
The main conclusion is that the proposed compactification of the moduli of surfaces is a separated algebraic space.

The methods of the last two chapters are largely unrelated to the rest of the article.
In chapter six some missing points of the classification of three dimensional terminal singularities are settled.
The proofs are fairly elementary and independent of the theory of minimal models.

The results of the last chapter imply that any small deformation of a cyclic quotient singularity is again a cyclic quotient.
This was conjectured by Riemenschneider.

Now we turn to give a precise formulation of the result from three dimensional geometry that we will repeatedly use.

## Minimal models for semi-stable reductions

First we have to define the class of singularities that we will allow on the partial resolution.

Let $Y$ be a normal variety and let $g \colon Y' \to Y$ be a resolution of singularities of $Y$.
Let $K_Y$ be a canonical divisor on $Y$ and assume that $mK_Y$ is Cartier for some $m &gt; 0$.
Then we can write $mK_Y' \sim g^*(mK_Y) + \sum a_i E_i$, where the $E_i$ are $g$-exceptional divisors.
$Y$ is said to have only terminal (resp.
canonical) singularities if all the $a_i$ are positive (resp.
nonnegative).
The complete list of three-dimensional terminal singularities is reproduced in 6.3–4.

Let $f \colon X \to T$ be a map of an algebraic (or complex analytic) threefold on to a smooth curve $T$.
We say that $f$ admits a semi-stable resolution if there

Threefolds and deformations of surface singularities

exists a bimeromorphic and projective morphism $g \colon X' \to X$ such that $X'$ is smooth and $(g \circ f)^{-1}(t)$ is reduced and has at worst normal crossing singularities.
By a result of Knudsen and Mumford [KKMS], if $h \colon Y \to S$ is arbitrary then there is a finite surjective map $p \colon T \to S$ such that $f = h \times p \colon Y \times_S T \to T$ admits a semi-stable resolution.

Now one can formulate the following result which was proved by Tsunoda, Shokurov, Mori and Kawamata.

Theorem.
Let $f \colon X \to T$ be a morphism of an algebraic (complex analytic) three-dimensional space onto a smooth curve $T$ . Assume that $f$ admits a semi-stable resolution.
Then there is a projective birational (bimeromorphic) morphism $g \colon \bar{X} \to X$ such that $\bar{X}$ has only terminal singularities and such that for every compact curve $C \subset \bar{X}$ such that $g(C) = \text{point}$ we have $C \cdot K_{\bar{X}} \geq 0$ . By [Ben, Kaw3] one can also find a $\tilde{g} \colon \bar{X} \to X$ such that $\bar{X}$ has canonical singularities and such that $C \cdot K_{\bar{X}} &gt; 0$ for every compact curve $C \subset \bar{X}$ such that $\tilde{g}(C) = \text{point}$ . Such an $\bar{X}$ is unique, and is called the relative canonical model of $X$ .

Acknowledgements.
Various parts of this article were discussed with S. Mori, B. Teissier and J. Wahl.
We are very grateful for their comments and suggestions.
Partial financial support was provided by the NSF under grant numbers DMS 85-03734 and DMS 85-03743.

# § 2. Simultaneous resolution of surface singularities

It is well understood how to resolve the singularities of an algebraic surface.
For families of surfaces however, the situation is very complicated.
One could simply desingularize the total space of a family, but usually the resulting family will not even be flat.
Frequently this is the best one can hope for.
Therefore, it is of interest to understand the cases when some particularly "nice" desingularization is possible.
There are several notions of "nice" (cf [Te]); we recall some of them here.

Definition 2.1. Let $f \colon X \to Y$ be a flat family of reduced algebraic surfaces.
Let $g \colon \bar{X} \to X$ be a projective morphism such that $f \circ g \colon \bar{X} \to Y$ is flat too.
The fibre of $f$ (resp.
$f \circ g$ ) above $y \in Y$ will be denoted by $X_y$ (resp.
$\bar{X}_y$ ). We will always assume that $Y$ is reduced.

(i) $g$ is called a simultaneous DuVal (or rational double point) resolution of $f$ if each $\bar{X}_y \to X_y$ is the minimal resolution with DuVal singularities.
(ii) $g$ is called a very weak simultaneous resolution if each $\bar{X}_y \to X_y$ is the minimal resolution of $X_y$ . (iii) If $p \colon Y \to X$ is a section of $f$ , then $f$ is called a weak simultaneous resolution along $p$ if it is a very weak simultaneous resolution near $f(Y)$ and the map $g \colon (g^{-1}(p(Y))) \to p(Y)$ is simple (i.e. locally in the Euclidean topology on $g^{-1}(p(Y))$ ) it is the projection of a direct product.)
(iv) $f$ is said to admit a simultaneous DuVal resolution (respectively a very weak or weak simultaneous resolution) if there exists a $g\colon \bar{X}\to X$ satisfying (i) (resp.
(ii) or (iii)).

J. Kollár and N.I. Shepherd-Barron

(v) It is important to note that very weak simultaneous resolutions are not unique in general, despite the fact that the minimal resolution of the individual surfaces are unique.

One advantage of the DuVal resolution is that it is unique.
If $g \colon \bar{X} \to X$ is a simultaneous DuVal resolution then $K_{\bar{X}/X}$ is $g$-ample.
This implies uniqueness essentially by a result of Matsusaka-Mumford [MM].

One of the early results relating these notions is the following.

Theorem 2.2. (Brieskorn [Br2]) Assume that $f \colon X \to Y$ as above admits a simultaneous DuVal resolution.
Then there exists a finite and surjective map $f \colon Y' \to Y$ such that $f' \colon X \times_Y Y' \to Y'$ admits a very weak simultaneous resolution.

Very weak simultaneous resolution without a base change seems a very delicate property; therefore we will not consider it.

Definition 2.3. (i) Let $Z$ be an algebraic surface with isolated singularities and $h: Z' \to Z$ be a resolution of singularities, $E_i \subset Z'$ the exceptional curves.
There exists a formal linear combination $\sum a_i E_i$ such that $E_j \cdot \sum a_i E_i = E_j \cdot K_{Z'}$ for every $j$.
The rational number $\sum a_i E_i \cdot \sum a_i E_i$ will be called the self intersection number of the relative canonical class.
If $Z'$ is the minimal resolution of $Z$, then it will be denoted by $K_{\mathrm{rel},Z}^2$.

(ii) If $Z$ is projective and $\bar{Z}$ is the minimal resolution, then we shall write $\bar{K}_Z^2$ instead of $K_Z^2$.

(iii) Mumford [M] defined the intersection number of any two Weil divisors on a normal projective surface $Z$.
In particular $K_Z^2$ is defined for such surfaces.

Note the relationship $\bar{K}*Z^2 = K_Z^2 + K*{\mathrm{rel},Z}^2$.

(iv) If $X_y, y \in Y$, is a family of surfaces we shall write $K_y^2$ instead of $K_{\bar{X}_y}^2$ (similarly $\bar{K}*y^2, K*{\mathrm{rel},y}^2$) if no confusion is likely.

The following theorems were the strongest known results concerning simultaneous resolution of surface singularities.

Theorem 2.4. (i) (Laufer, [La, 5.7]) Let $f \colon X \to Y$ be a flat family of normal, Gorenstein surface singularities.
Then $K_{\mathrm{rel},y}^2$ is lower semi-continuous.
$K_{\mathrm{rel},y}^2$ is locally constant $\Leftrightarrow f$ admits a very weak simultaneous resolution after a finite and surjective base change.

(ii) (Vaquie, [V, 2.4]) If $f$ is a flat family of normal surface singularities, then $K_{\mathrm{rel},y}^2$ is lower semi-continuous.

(iii) (Vaquie, [V, 2.5]) If $f \colon X \to D$ is a flat of rational surface singularities, $K_{\mathrm{rel},y}^2$ is constant and $K_X$ is $\mathbb{Q}$-Cartier, then $f$ admits a simultaneous DuVal resolution.

Theorem 2.5. (Laufer, [La, 6.4]) Let $f \colon X \to Y$ be a family of normal, Gorenstein surfaces over $\mathbb{C}$, and let $p \colon Y \to X$ be a section.
Assume that $Y$ is reduced and connected.
Then $f$ admits a weak simultaneous resolution along $p$ if and only if the following condition is satisfied:

For every $y \in Y$ there exists a Euclidean neighbourhood $V_y \subset X_y$ of $p(y)$ such that the pairs $(V_y, p(y))$ are all homeomorphic to each other.
(we assume that the homeomorphism preserves the natural orientation).

Threefolds and deformations of surface singularities

Definition 2.6. If this condition is satisfied we shall say that the germs of $X_{y}$ along $p$ are pairwise homeomorphic.

Remark 2.7. The previous theorems are valid for complex analytic maps as well.
In fact, one can claim this to be their natural setting since the assumptions are local in the Euclidean topology.

Example 2.8. The following example was noticed by several people (see e.g. [Pi1]) and it shows that one cannot omit the Gorenstein assumption in 2.4.

Let $V \subset \mathbb{P}^5$ be the Veronese surface and $C_V \subset \mathbb{P}*6$ the cone over it.
Let $F \subset \mathbb{P}^5$ be the scroll $\operatorname{Proj}*{\mathbb{P}^1}(\mathcal{O}(2) + \mathcal{O}(2))$ embedded with the relative $\mathcal{O}(1)$ , and $C_F \subset \mathbb{P}^6$ be the cone over it.
Finally, let $C_4 \subset \mathbb{P}^5$ be the cone over the rational normal curve of degree four.
It we cut $C_V$ (resp.
$C_F$ ) with a pencil of hyperplanes, then the hyperplane through the vertex gives a copy of $C_4$ ; the general member will be isomorphic to $V$ (resp.
$F$ ). Obviously $K_{\mathrm{rel},V}^2 = K_{\mathrm{rel},F}^2 = 0$ . The family obtained from $C_F$ admits a simultaneous DuVal resolution: blow up $C_l$ , the cone over a line on $F$ . The family obtained from $C_V$ does not admit a simultaneous DuVal resolution: the singularity at the vertex is $\mathbb{C}^3 / (x \sim -x)$ ; hence for any birational modification the exceptional locus must be of pure dimension two.
Therefore any modification of $C_V$ would introduce a new component to the central fibre.

Note however that $\bar{K}_{C_4}^2 = \bar{K}_F^2 = 8$ , whereas $\bar{K}_V^2 = 9$ . The global invariant detects the existence of simultaneous resolution.
This is the case in general (see 2.10).

Definition 2.9. Recall that a scheme $Y$ is called seminormal [Tr] if the following holds:

Every map $p \colon Y' \to Y$ which is a homeomorphism (in the Zariski topology) is in fact an isomorphism.

Thus a normal scheme is seminormal, and so are varieties with normal crossings only.
For every variety $Z$ there is an $s \colon Z' \to Z$ such that $Z'$ is seminormal and $s$ is a homeomorphism; in particular $s$ is finite.
This $Z'$ is unique and is called the seminormalization of $Z$ (see [Tr]).

Theorem 2.10. Let $f \colon X \to Y$ be a flat family of projective surfaces with isolated singularities only such that $Y$ is seminormal.
Then

(i) $\bar{K}_y^2$ is lower semi-continuous; (ii) $\bar{K}_y^2$ is locally constant if and only if $f$ admits a simultaneous DuVal resolution; (iii) If $p \colon Y \to X$ is a section and $Y$ is connected; then $X$ admits a weak simultaneous resolution along $p$ if and only if the germs of $X_y$ along $p$ are pairwise homeomorphic.

Remark 2.11. Karras informed us that he also proved part (iii) of the theorem.
He considers only the case of normal singularities, but he is able to treat the analytic case as well.
His proof is a generalization of Laufer's ideas [Kar2].

Remark 2.12. There is some hope that the present methods will work in the analytic case as well.
(See 2.25).

J. Kollár and N.I. Shepherd-Barron

**Proposition 2.13.** Let $g \colon \widehat{U} \to V$ be an arbitrary resolution of the projective surface $V$, and let $\widehat{U}$ be the minimal resolution.
Assume that $K_{\widehat{U}} = H - E$, where $H$ is $g$-nef, $E$ is effective and supported on the $g$-exceptional locus.
Then $K_{\widehat{U}}^{2} \geq K_{\widehat{U}}^{2} + E^{2}$, and equality holds iff $E = 0$.

**Proof.** If $K_{\hat{U}}$ is $g$-nef, then $\hat{U} = \hat{U}$.
By [M] we have $E^2 \leq 0$, with $=$ only if $E = 0$.
Hence in this case we are done.

Otherwise, let $C \subset \widehat{U}$ be an exceptional curve such that $C \cdot K_{\widehat{U}} &lt; 0$ and let $h \colon \widehat{U} \to U'$ be the contraction.
$H = h^* H' + aC$, $E = h^* E' + bC$ for some $H', E'$, $a$ and $b$.
$0 \leq H \cdot C = aC^2$ implies $a \leq 0$.
Since $0 \geq K_{\widehat{U}} \cdot C = (a - b)C^2$ we have $a - b \geq 0$.
Hence $-b \geq a - b \geq 0$.

$K_{U'} = H' - E'$, and $E'$ is clearly effective.
If $F \neq C$ is an exceptional curve, then

$$
h(F) \cdot H' = F \cdot h^* H' = F \cdot H + (-a) F \cdot C \geq 0
$$

and therefore $H'$ is $g'$-nef for $g' \colon U' \to V$.
By induction $K_{U'}^2 \geq K_U^2 + E'^2$ with equality iff $E' = 0$.
On the other hand,

$$
\begin{aligned}
K_U^2 - E^2 &amp;= (h^* K_{U'} + (a - b) C)^2 - (h^* E' + b C)^2 \\
&amp;= K_{U'}^2 - E'^2 + [b^2 - (b - a)^2] (-C^2) \\
&amp;\geq K_U^2 + [b^2 - (b - a)^2] (-C^2).
\end{aligned}
$$

As we saw, $-b \geq a - b \geq 0$.
Thus the last term is positive and this proves the inequality.
If equality holds, then $E' = 0$, and $E = bC$.
Since $b \leq 0$, this can be effective only for $b = 0$.

**Corollary 2.14.** Let $g \colon U \to V$ be a regular birational map between projective surfaces and assume that $U$ has only quotient singularities.
Assume that $K_U \equiv H - E$, where $H$ is $g$-nef, $E$ is effective and supported on the $g$-exceptional locus.
Finally, let $\widehat{U}$ be the minimal resolution of $V$.
Then $K_U^2 \geq K_U^2 + E^2$ with equality iff $E = 0$ and $U$ has only DuVal singularities.

**Proof.** Let $j \colon \widehat{U} \to U$ be the minimal resolution of $U$.
Then $K_{\widehat{U}} = j^* K_U - E'$ where $E'$ is effective, $j$-exceptional and $E' = 0$ iff $U$ has only DuVal singularities (cf.
4.12). Let $\widehat{H} = j^* H$, $\widehat{E} = E' + j^* E$.
We can apply 2.13 for $g \circ j \colon \widehat{U} \to V$ and $K_{\widehat{U}} = \widehat{H} - \widehat{E}$.
We obtain that $K_{\widehat{U}}^2 + E'^2 = K_{\widehat{U}}^2 \geq K_{\widehat{U}}^2 + E'^2 + E^2$, and this gives the inequality.
Equality holds if $E = 0$ and $E' = 0$, hence $U$ has only DuVal singularities.

Now we are ready to prove a seemingly very special case of 2.10. The rest, however, turns out to be a formal consequence of it.

**Theorem 2.15.** Let $f \colon X \to D$ be a flat family of complete surfaces with isolated singularities over the unit disc $D$.
Assume that $f$ admits a semi-stable resolution of singularities.
Then

(i) $\widehat{K}_i^2$ is lower semi-continuous;

(ii) $\widehat{K}_i^2$ is constant iff $f$ admits a simultaneous DuVal resolution.

**Proof.** Let $\tilde{g} \colon \widehat{X} \to X$ be a relative minimal model (cf.
chapter 1.). Let $\widehat{X}_i \to X_i$ be the general fibre, $X_0' + \sum E_i$ the central fibre of $\widehat{X}$, and $n \colon \widehat{X}_0 \to X_0'$ the normalization.
Let $F \subset \widehat{X}_0$ be the conductor of $n$.
Thus

$$
K_{X_0} = K_{\tilde{X}} + X_0' |X_0' = K_{\tilde{X}} - \sum E_i |X_0'.
$$

Threefolds and deformations of surface singularities

If we set $E = F + n^{*}\sum E_{i}$, then $K_{\bar{X}_0} = n^* K_{\bar{X}} - E$.
Thus

$$
K _ {\bar {X}} ^ {2} \cdot X _ {0} ^ {\prime} = n ^ {*} K _ {\bar {X}} ^ {2} = K _ {\bar {X} _ {0}} ^ {2} + 2 E \cdot n ^ {*} K _ {\bar {X}} - E ^ {2}.
$$

Substituting this into

$$
\bar {K} _ {t} ^ {2} = K _ {\bar {X}} ^ {2} \cdot X _ {t} = K _ {\bar {X}} ^ {2} \cdot X _ {0} ^ {\prime} + K _ {\bar {X}} ^ {2} \cdot \sum E _ {i},
$$

we get

$$
\bar {K} _ {t} ^ {2} = K _ {\bar {X} _ {0}} ^ {2} - E ^ {2} + 2 E \cdot n ^ {*} K _ {\bar {X}} + K _ {\bar {X}} ^ {2} \cdot \sum E _ {i}.
$$

Since $E$ is effective and exceptional with respect to $\bar{X}*0 \to X_0$, and $n^* K*{\bar{X}}$ is relatively nef the last two terms are non-negative.

This gives $\bar{K}*t^2 \geq K*{\bar{X}*0}^2 - E^2$.
Using 5.1 and taking $H = n^* K*{\bar{X}}$ the conditions of 2.14 are satisfied for $(\bar{X}*0 \to X_0, K*{\bar{X}_0} = H - E)$.
Therefore, if $\bar{X}*0$ is the minimal desingularization of $X_0$, then $K*{\bar{X}_0}^2 \geq \bar{K}_0^2 + E^2$.
These two inequalities give that $\bar{K}_t^2 \geq \bar{K}_0^2$, which is (i). If we have equality, then $E = 0$.
Hence $\sum E_i = 0$ and $X_0'$ is normal and has only DuVal singularities.

This is nearly what we want.
Let $h \colon \bar{X} \to \bar{X}$ be the relative canonical model, $g \colon \bar{X} \to X$.
This is the required simultaneous DuVal resolution.
To see this, first note that $h$ is an isomorphism in codimension one since the central fibre of $\bar{X}$ is irreducible.
Therefore, $K_{\bar{X}} = h^{*}K_{\bar{X}}$.
This in turn gives that $K_{\bar{X}_0} = h^{*}K_{\bar{X}_0}$; thus $\bar{X}*0$ has DuVal singularities only.
Since $K*{\bar{X}}$ is $g$-ample, each fibre of $\bar{X} \to D$ is the minimal DuVal resolution of the corresponding fibre of $X \to D$.
This proves one direction of (ii), and the other one is trivial.

2.16 Proof of 2.10 (i). $Y$ can be written as the union of locally closed subsets $Y_{i}$ such that $f$ admits a simultaneous DuVal resolution over each $Y_{i}$.
This implies that $\bar{K}_y^2$ is a constructible function on $Y$.
By 2.15 it is lower semi-continuous along curves, and therefore it is lower semi-continuous.

2.17 Proof of 2.10 (ii).
If there is a simultaneous DuVal resolution, then $\bar{K}_y^2$ is clearly locally constant.
The proof of the converse is intuitively clear.
We take the minimal DuVal resolutions and by 2.15 these glue together along any curve.
This should imply that they all glue together.
The actual proof is unfortunately rather cumbersome.

Pick a relatively ample divisor $H$ on $X/Y$, and let $H_y$ denote its restriction to $X_y$.
Let $r_y \colon \bar{X}_y \to X_y$ be the minimal DuVal resolution.
There are $n, m &gt; 0$ such that $n(K_y + mr_y^* H_y) = \bar{H}_y$ is very ample for every $y$ and $H^0(\bar{X}_y, H_y) = \chi(\bar{X}_y, \bar{H}_y)$.
This latter is a polynomial in $\bar{K}_y^2$, $\bar{K}*y \cdot r^* H = K_y \cdot H$ and $\chi(\mathcal{O}*{\bar{X}_y})$.
The first of these is assumed to be constant, the second one is automatically constant, and the third one is constant along any curve by 2.15, hence constant.
Therefore $h^0(\bar{X}_y, \bar{H}_y)$ is independent of $y \in Y$.
Let $\mathbb{P}$ be the projective space of dimension $h^0(\bar{X}_y, \bar{H}_y) - 1$.

In $\mathbb{P} \times X$ let the coordinate projections be $p$ and $q$.
We consider subchemes $Z \subset \mathbb{P} \times X$ satisfying the following conditions.

(i) $Z$ has only DuVal singularities (ii) $q\colon Z\to X$ is birational onto a fibre of $f$ (iii) $K_{Z}$ is relatively $q$-ample;

J. Kollár and N.I. Shepherd-Barron

(iv) $p\colon Z\to \mathbb{P}$ is a non-degenerate embedding and

$$
p ^ {*} \mathcal {O} (1) = \mathcal {O} (n (K _ {Z} + m q ^ {*} H)).
$$

(i.e. $Z$ is the graph of an embedding of the minimal DuVal resolution of a fibre $X_{y}$ given by $\bar{H}_y$.)

These subschemes are parametrized by some subscheme $R$ of the relative Hilbert scheme of $\mathbb{P} \times X / Y$.
Let $u \colon U \to R$ be the universal family.
We have a natural map $c \colon R \to Y$ given by $r \to f(q(u^{-1}(r)))$.
$R$ parametrizes pairs (minimal resolution of some $X_y$; an embedding of it given by $\bar{H}_y$). The different embeddings differ by an element of Aut $\mathbb{P}$, so the natural action of Aut $\mathbb{P}$ on $R$ is transitive on the fibers of $c$.
Aut $\mathbb{P}$ clearly operates without fixed points.
Hence the universal family $U$ descends to $Y = R / \mathrm{Aut} \mathbb{P}$ (cf.
[Po, Lecture 3]) and we get a map $\bar{u} \colon \bar{X} = U / \mathrm{Aut} \mathbb{P} \to \bar{Y}$ and a natural map $\bar{c} \colon \bar{Y} \to Y$ which is 1:1 on closed points.
If $\bar{c}$ is an isomorphism, then $\bar{X} \to \bar{Y} = Y$ is the sought after simultaneous DuVal resolution.

We claim that $\bar{c}$ is finite.
By the valuative criterion it is sufficient to check this along curves.
2.15 provides a simultaneous resolution along any smooth curve.
This in turn can be embedded into $\mathbb{P} \times X$, and hence we get a lifting of our curve to $R$ which descends to $\bar{Y}$.
Therefore $c \colon \bar{Y} \to Y$ is finite.
It is 1:1 on closed points, and hence it is an isomorphism since $Y$ is assumed to be seminormal.
This proves 2.10 (ii).

Remark 2.18. The assumption in 2.10 that $Y$ be seminormal is somewhat unnatural.
One certainly has to assume that $Y$ is reduced, since the assumption about $K^2$ makes sense for closed points only and we have no control over the infinitesimal part.
If $Y$ is reduced, then the previous proof shows that $c \colon \bar{Y} \to Y$ is finite and 1:1 on closed points.
Therefore, it is an isomorphism iff it is an isomorphism on the tangent spaces.
This is a question about the infinitesimal deformation of a surface and of its minimal resolution.
This was studied by Wahl [Wa 1], and the situation seems quite complicated.
It is not clear whether 2.10 (ii) is true for arbitrary reduced $Y$ or not.

Before we turn to the proof of 2.10 (iii), some technical results are needed.

Lemma 2.19. Let $Z$ be a reduced complete surface, Gorenstein in codimension one.
Let $S \subset Z$ be a finite set of normal points of $Z$.
Then there exists a constant $c(Z)$ such that for every Weil divisor $D$ which is Cartier outside $S$, we have

$$
\left| \chi (Z, \mathcal {O} (D)) - \frac {1}{2} D (D - K _ {Z}) \right| &lt;   c (Z).
$$

Proof.
Let $f \colon Z' \to Z$ be a resolution of the singularities in $S$.
As in [M] one can define the pull-back $f^*D$, which is a divisor with rational coefficients.
Let $[f^*D]$ be the divisor obtained by rounding up the coefficients.
$f_* \mathcal{O}([f^*D]) = \mathcal{O}(D)$ by [Sak], and one can easily prove that length $R^1 f_* \mathcal{O}([f^*D])$ is bounded by a constant depending on $f$ only.

$|[f^{*}D]\cdot ([f^{*}D] - K_{Z^{\prime}}) - D(D - K_{Z})| &lt; (\text{some constant depending on } f)$ and

$$
\chi (Z ^ {\prime}, \mathcal {O} ([ f ^ {*} D ])) - \frac {1}{2} [ f ^ {*} D ] \cdot ([ f ^ {*} D ] - K _ {Z ^ {\prime}}) = \chi (\mathcal {O} _ {Z ^ {\prime}}).
$$

Putting these together, we get the required estimate.

Threefolds and deformations of surface singularities

Lemma 2.20. Let $f \colon X \to D$ be a family of reduced surfaces which are Gorenstein except at finitely many normal points.
Then $K_{X_t}^2$ is upper semi-continuous.

Proof.
Consider the sheaf $\mathcal{O}(mK_{X / D})$.
For a generic point $t$ we have $\mathcal{O}(mK_{X / D})\otimes \mathcal{O}*{X_t}\cong \mathcal{O}(mK*{X_t})$, and for 0 we still have an injection $\mathcal{O}(mK_{X / D})\otimes \mathcal{O}*{X_0}\to \mathcal{O}(mK*{X_0})$ which is an isomorphism outside the non-Gorenstein locus.
Therefore,

$$
\begin{array}{l}
\chi \left(X _ {0}, \mathcal {O} \left(m K _ {X _ {0}}\right)\right) \geq \chi \left(X _ {0}, \mathcal {O} \left(m K _ {X / D}\right) \otimes \mathcal {O} _ {X _ {0}}\right) \\
= \chi \left(X _ {t}, \mathcal {O} \left(m K _ {X / D}\right) \otimes \mathcal {O} _ {X _ {t}}\right) = \chi \left(X _ {t}, \mathcal {O} \left(m K _ {X _ {t}}\right)\right).
\end{array}
$$

Applying 2.19 for $D = K_{Z}$ gives that the l.h.s. is asymptotic to $\frac{1}{2} m^{2}K_{X_{0}}^{2}$, the r.h.s. to $\frac{1}{2} m^{2}K_{X_{t}}^{2}$.
Dividing by $\frac{1}{2} m^{2}$ gives the required inequality.

We shall also need the following result.

Theorem 2.21. (Neumann, [Ne]) Let $(p_i, V_i)$ be isolated surface singularities, $f_i \colon \bar{V}_i \to V_i$ be the minimal resolutions, $E_i \subset \bar{V}_i$ the exceptional sets.
Assume that the pairs $(p_i, V_i)$ are homeomorphic (orientation preserved).
Then the pairs $(E_i, \bar{V}*i)$ are also homeomorphic.
In particular $K*{\mathrm{rel}, V_i}^2$ is independent of $i$.

Now we can prove the following special case of 2.10 (iii).
As earlier, the general case will follow easily.

Theorem 2.22. Let $f \colon X \to D$ be a flat family of surfaces with isolated singularities.
Let $p \colon D \to X$ be a section.
Assume that the germs of $X_t$ along $p$ are pairwise homeomorphic.
Then, possibly after a base change, there exists a simultaneous DuVal resolution along $p$.

Proof.
Let $S \subset X$ be the union of those irreducible components of $\operatorname{Sing} X$ that contain $p(0)$.
Shrinking $D$, making a base change and applying semi-stable reduction for $\operatorname{Sing} X - S$, we can assume that $S = \operatorname{Sing} X$ (for simplicity the new $f, X, D$ are denoted by the same symbols).
Let $\bar{X}_t \to X_t$ be the minimal resolution of the singularities $S \cap X_t$.
For $t \neq 0$ these are all the singularities, but $X_0$ has other singularities, namely normal crossing points.
Although $X_0$ is reducible, the arguments of 2.15 apply verbatim and we get that $\bar{K}_0^2 \leq \bar{K}_t^2$.

By 2.3 (iii) $\bar{K}*0^2 = K_0^2 + K*{\mathrm{rel},0}^2$ and $\bar{K}*t^2 = K_t^2 + K*{\mathrm{rel},t}^2$.
$K_{\mathrm{rel},t}^2$ is a sum over all singularities of $X_t$.
One of them is $p(t)$, and $K_{\mathrm{rel},p(t)}^2 = K_{\mathrm{rel},p(0)}^2 = K_{\mathrm{rel},0}^2$ by 2.21. Since for any singularity $Z$ we have $K_{\mathrm{rel},2}^2 \leq 0$, this yields that $K_{\mathrm{rel},t}^2 \leq K_{\mathrm{rel},0}^2$.
By 2.20 $K_t^2 \leq K_0^2$ and hence $\bar{K}_t^2 \leq \bar{K}_0^2$.
These imply that $\bar{K}_t^2 = \bar{K}_0^2$.
Thus again by 2.15 there is a simultaneous DuVal resolution.
As in [La, 6.2] this yields that in fact $S = p(D)$ and the exceptional divisors of the DuVal resolutions are homeomorphic.

Now we can blow down the part we blew up at the very beginning, and this gives a simultaneous DuVal resolution along $p$.

2.23. Proof of 2.10 (iii).
We proceed as in 2.17. For each $y \in Y$ let $r_y \colon \bar{X}*y \to X_y$ be the DuVal resolution of the singularity $p(y)$.
If $E*{i,y}$ are the exceptional curves on $\bar{X}*y$, then for some $a_i \in \mathbb{Q}$ we have $E*{j,y} \cdot \sum a_i E_{i,y} = E_{j,y} \cdot \bar{K}*y$ for every $j$.
By 2.20 the $a_i$ are independent of $y$.
Let $K_y' = \sum a_i E*{i,y}$.
Then we define $\bar{H}_y = n(K_y' + mr_y^* H_y)$ to be the polarizing divisor.

J. Kollár and N.I. Shepherd-Barron

Continuing as in 2.17, in $\mathbb{P} \times X$ we consider subschemes $Z$ with the following properties.

(i) $q\colon Z\to X$ is birational onto a fibre of $f$ and is an isomorphism off $p(y)$; (ii) above $p(y)$ it has only DuVal singularities; (iii) the exceptional divisor is homeomorphic to the above $\sum E_{i,y}$ and $\sum a_i E_{i,y}$ is $q$-ample; (iv) $p\colon Z\to \mathbb{P}$ is a non-degenerate embedding and $p^* \mathcal{O}(1) = \mathcal{O}\big(n(\sum a_i E_i + m q^* H)\big)$.

As there we obtain that $f \colon X \to Y$ admits a simultaneous DuVal resolution along $p$.

As was already remarked by Laufer [La, 6.2], this can be blown up to a weak simultaneous resolution.
This completes the proof of 2.10 (iii).

Remark 2.24. (i) Working in a similar manner, but using certain ideas of Laufer [La] and Wahl [Wa1], one can see that 2.9 (iii) is true if $Y$ is only assumed to be reduced, and the fibres are all normal.

(ii) As was pointed out by Laufer [La] non-normal isolated singularities do frequently occur in families with weak simultaneous resolution.
(iii) If $(z,Z)$ is an isolated surface singularity, $\bar{Z}$ the normalization, and $r\colon Z^{\prime}\to Z$ a resolution, then both $R^{1}r_{*}\mathcal{O}*{Z}$ and $\mathcal{O}*{\bar{Z}} / \mathcal{O}*Z$ are of finite length.
Let $h_z$ denote the difference of these lengths.
One can prove that in a flat family $K*{\mathrm{rel},z}^{2}$ constant implies that $h_z$ is constant.

Remark 2.25. As was already pointed out in 2.8, the straightforward local version of 2.10 is false.
Wahl pointed out to us that in certain cases one can define a more local version of $K^2$.
The idea is as follows [LW].

Let $(M, \partial M)$ be a smooth complex surface with boundary.
If $a_i \in H^2(M)$ such that $a_i | \partial M = 0$ in $H^2(\partial M)$, then one can define $a_1 \cap a_2 \in H^4(M, \partial M) \cong \mathbb{Q}$ as follows.
Lift $a_1$ to $H^2(M, \partial M)$ and then cap it with $a_2$.
The resulting class is independent of the lifting.

Now let $f \colon X \to D$ be a flat deformation of the isolated surface singularity $(0, X_0)$.
Let $(B, \partial B)$ be a small ball around 0, and let $(X_t', \partial X_t) = (X_t \cap B, X_t \cap \partial B)$.
For $t$ small $X_t'$ has only isolated singularities and is non-singular along $\partial X_t$.
Let $(M_t, \partial M_t) \to (X_t', \partial X_t)$ be the minimal resolution of the singularities.
Since $\mathrm{im}[H^2(M_0, \mathbb{Q}) \to H^2(\partial M, \mathbb{Q})] = 0$, $c_1(K_{M_0}) | \partial M_0 = 0$ in $H^2(\partial M_0)$; hence by continuity this holds for every $t$.
This way one can define $K_{M_0}^2$ for every nearby $t$.

As in 2.15 one can prove that $K_{M_t}^2$ is lower semicontinuous, and is constant iff $f$ admits a simultaneous DaVal resolution.

It is quite likely that the rest of 2.10 is true in this localized version, but the proofs given here rely heavily on global techniques.
Substantial changes seem to be required.

There is an alternative global approach to 2.15 via the follow result:

Proposition 2.26. Let $f \colon X \to D$ be a flat family of reduced surfaces.
Assume that $m_0 K_X$ is Cartier for some $m_0 &gt; 0$ and $K_X$ is $f$-ample.
Let $X_0 = \cup E_i$ be the central fiber.
Let $k^2(Z) = \lim (2/m^2) h^0(Z', \omega_Z^m)$ for any surface $Z$ with desingularization $Z'$.
Then

$$
\sum k^2(E_i) \leq k^2(X_t) \quad \text{for} \quad t \neq 0.
$$

Threefolds and deformations of surface singularities

Equality holds iff $X_0$ is irreducible and has DuVal singularities only.

Proof.
First note that if $Z$ is a smooth minimal surface, then $k^2(Z) = K_Z^2$ if $Z$ is of general type and $k^2(Z) = 0$ otherwise.

If $m$ is sufficiently large and divisible by $m_0$, then

$$
h^0(X_0, \mathcal{O}(mK_{X_0})) = h^0(X_t, \mathcal{O}(mK_{X_t}))
$$

since $f$ is flat and $K_X$ is $f$-ample.
If $p \colon E_i' \to X_0$ is the natural map then one has a natural map (called trace map)

$$
\sum p_* \mathcal{O}(K_{E_i}) \to \mathcal{O}(K_{X_0})
$$

This gives ups maps

$$
t_m \colon \sum p_* \mathcal{O}(mK_{E_i}) \to \mathcal{O}(mK_{X_0}), \quad \text{and}
$$

every $t_m$ is an injection.
If $m$ is divisible by $m_0$, then $\mathcal{O}(mK_{X_0})$ is invertible; hence one can write the image of $t_m$ as $I_m \cdot \mathcal{O}(mK_{X_0})$ for an ideal sheaf $I_m$.
We have

$$
\begin{array}{l}
\sum h^0(E_1', \mathcal{O}(mK_{E_i})) = h^0(X_0, I_m \cdot \mathcal{O}(mK_{X_0})) \\
\leqslant h^0(X_0, \mathcal{O}(mK_{X_0})).
\end{array}
$$

This gives the required inequality.

To analyze the case when equality holds, note that since the canonical ring of a surface is finitely generated we get that for some $m_1$, if $m = k m_1$ then

$$
h^0(X_0, I_m \cdot \mathcal{O}(mK_{X_0})) = h^0(X_0, I_{m_1}^k \cdot \mathcal{O}(mK_{X_0})).
$$

Now we use the following easy

Lemma 2.27. Let $Z \subset \mathbb{P}^N$ be a projective surface and $I \subset \mathcal{O}_Z$ an ideal sheaf, $I \neq \mathcal{O}_Z$.
Then there exists $\varepsilon &gt; 0$ such that for every large $n$

$$
h^0(Z, I^n \mathcal{O}(n)) &lt; (1 - \varepsilon) h^0(Z, \mathcal{O}(n)).
$$

Applying this for $Z = X_0$, $\mathcal{O}(1) = \mathcal{O}(m_1 K_{X_0})$ and $I = I_{m_1}$, we get that $t_{m_1}$ is an isomorphism.
Therefore, $X_0$ is irreducible and has DuVal singularities only.
This completes the proof.

Remark 2.27. (i) This proposition is very closely related to some results of Nakayama [Na, 11] and Laufer [La, 4.4].

(ii) If all the surfaces $E_i$ are such that their minimal desingularizations are minimal surfaces of general type, then 2.26 implies 2.15. The general case can be reduced to this one via a suitable cyclic covering.

(iii) Nakayama [Na, 11] proves that $\sum h^0(E_i', \mathcal{O}(mK_{E_i})) \leqslant h^0(X_t, \mathcal{O}(mK_{X_t}))$ holds for every $m \geq 1$.
It is possible that equality for a few small $m$ already implies that $X_0$ is irreducible with DuVal singularities only.

310 J. Kollár and N.I. Shepherd-Barron

## § 3. Deformations of quotient singularities

It is well-known that for a rational surface singularity $(X_0, P)$, a one-parameter deformation $X \to \Delta$ of $X_0$ need have no simultaneous resolution, even in the very weak sense or even after making a ramified covering of the base $\Delta$.
In fact, there is a unique irreducible component $Z$ of the local moduli space $\operatorname{Def}(X_0)$ of $X_0$, known as the Artin component [A2], such that a deformation as above admits a simultaneous resolution if and only if the image of $\Delta$ in $\operatorname{Def}(X_0)$ lies in $Z$.
We aim in this section to show, however, that a weakened analogue of simultaneous resolution holds for any one-parameter deformation of a quotient singularity $X_0$, and to use this result to show how the number of components in $\operatorname{Def}(X_0)$ may be computed.
Some analogous results may be proved for a rather wider class of singularities; for the sake of clarity and simplicity these generalizations are postponed to section 5.

We begin by recalling some terminology and a theorem of Kawamata.

**Definition 3.1.** (i) A normal variety $Y$ is $\mathbb{Q}$-Gorenstein if some non-zero integral multiple $mK_Y$ of the canonical divisor $K_Y$ is Cartier and $Y$ is Cohen-Macaulay.

(ii) A germ $Y$ of a normal threefold is *pseudo terminal* if it is canonical and its canonical cover has only cDV singularities.
Equivalently, $Y$ is pseudo-terminal if it is $\mathbb{Q}$-Gorenstein and for some (or equivalently, every) resolution $f\colon \widehat{Y} \to Y$ whose exceptional prime divisors are $E_1, \ldots, E_r$, we have $K_{\widehat{Y}} \sim f^* K_Y + \sum a_i E_i$, where $a_i \geq 0$ for all $i$ and $a_j &gt; 0$ if $f(E_i)$ is a point.

(iii) A normal surface singularity $(X, P)$ is *log terminal* if for some (or equivalently, every) resolution $f \colon \widehat{X} \to X$ whose exceptional locus $E = \bigcup_{i=1}^{r} E_i$ has normal crossings, there are rational numbers $a_1, \ldots, a_r$ such that $K_{\widehat{X}} \equiv -\sum a_i E_i$ and for all $i, a_i &lt; 1$.

**Theorem 3.2.** (Kawamata [Kaw2]). The normal surface singularity $(X, P)$ is *log terminal* if and only if it is a quotient singularity.

**Lemma 3.3.** Suppose that $X \to \Delta$ is a one-parameter deformation of a normal surface singularity $(X_0, P)$, that $\Delta' \to \Delta$ is a finite base change and that $X' = X \times_{\Delta} \Delta'$.
Then if $X'$ has just terminal (resp.
canonical, resp.
pseudo-terminal) singularities the same holds for $X$.

*Proof.* We first deal with the case where $X'$ is terminal (resp.
canonical).
There are uniformizing parameters $t, t'$ on $\Delta, \Delta'$ respectively such that $t = t'^m$, some $m$.
Then the Galois group $G = \operatorname{Gal}(\Delta' / \Delta)$ is cyclic of order $m$; say $G = \langle \tau \rangle$.
Suppose that $X'$ has index $M$; choose a generator $\phi \in \mathcal{O}(M \cdot K_{X'})$.
Then $\omega = \bigotimes_{i=0}^{m-1} (\tau^i)^* \phi$ is a $G$-invariant generator of $\mathcal{O}(mMK_{X'})$, and so $t^{M(m-1)} \cdot \omega$ is a generator of $\mathcal{O}(mM \cdot K_X)$.
I.e. $X$ is $\mathbb{Q}$-Gorenstein.
Put $r = m \cdot M$, so that $r \cdot K_X$ and $r \cdot K_{X'}$ are both Cartier.
Put $\sigma = t^{M(m-1)} \cdot \omega$.
Let $v$ be a discrete rank one valuation of the function field $\mathbb{C}(X)$ that is centred at $P$ (resp.
centred at a point or component of the singular locus of $X$) and let $v'$ be an extension of $v$ to $\mathbb{C}(X')$.
Let $x' \in \mathbb{C}(X')$ be a uniformizing parameter for $v'$; then for some $C \in \mathbb{C}(X')$ with $v'(C) = 0$ and

Threefolds and deformations of surface singularities

some integer $e$ with $e|m, C \cdot x'^e$, say, is a uniformizing parameter for $v$.
We have $t' = D \cdot x'^a$, where $v'(D) = 0$ and $\alpha &gt; 0$.
Choose $y, z \in \mathcal{O}_v$, the valuation ring of $v$, that induce a transcendence basis of the residue field of $\mathcal{O}_v$ over $\mathbb{C}$.
We can write $\sigma = B \cdot x^\delta \cdot (dx \wedge dy \wedge dz)^{\otimes r}$, where $v(B) = 0$, and we must show that $\delta &gt; 0$ (resp.
$\delta \geq 0$). Now $\sigma / t'^r(m-1) = \omega$ generates $\mathcal{O}(r \cdot K_X)$, and so we can write $\omega = A \cdot x'^y (dx' \wedge dy \wedge dz)^{\otimes r}$, where $v'(A) = 0$ and by hypothesis $\gamma &gt; 0$ (resp.
$\gamma \geq 0$). Now $dx = dc \cdot x'^e + e \cdot C \cdot x'^e - 1 dx' = C' \cdot x'^e - 1 (dx' + C_2 dy + C_3 dz)$, where $v'(C') = 0$, and so $\sigma = B \cdot C^\delta \cdot x'^{\delta e} \cdot C'^r \cdot x'^r(e-1) \cdot (dx' \wedge dy \wedge dz)^{\otimes r}$; comparing the powers of $x'$ shows that $\delta e + r(e-1) = \alpha r(m-1) + \gamma$.
Since $\alpha &gt; 0$ and $e \leq m$ it follows that $r(e-1) \leq \alpha r(m-1)$, and so $\delta e \geq \gamma$.
Hence $\delta &gt; 0$ (resp.
$\delta \geq 0$). So, since the geometric generic fibre of $X$ is isomorphic to that of $X'$, it must be smooth (resp.
have only RDP's) and the Lemma is proved in this case.

Finally, to deal with the case where $X'$ is pseudo-terminal, we must show that if $v$ is a valuation of $\mathbb{C}(X)$ centred at the generic point of a curve in the singular locus of $X$, then (in the same notation as above), $\delta \geq 0$, and that if $v$ is centred at $P$, then $\delta &gt; 0$.
Then arguments, however, are the same as those above.
QED

A proof of the next lemma (which is in any case very easy) is implicit in the preceding argument.

**Lemma 3.4.** Suppose that $X \to \Delta$ is a normal one-parameter deformation of the reduced surface $X_0$, $\Delta_1 \to \Delta$ is finite base change and $X_1 = X \times_{\Delta} \Delta_1$.
Then $X$ is $\mathbb{Q}$-Gorenstein if and only if $X_1$ is so.

**Theorem 3.5(a).** Suppose that $X \to \Delta$ is a one-parameter deformation of the quotient singularity $(X_0, P)$.
Then, after making a finite base change if necessary, there is a proper birational morphism $f \colon Y \to X$ with the following properties:

(i) $Y$ has only terminal singularities.
(ii) For all complete curves $C$ contracted by $f$, we have $K_{Y} \cdot C \geq 0$.
(iii) For $t \in \Delta^{*} = \Delta - \{0\}$, the morphism $Y_{t} \to X_{t}$ is the minimal resolution.
(iv) The special fibre $Y_0$ is normal, with only quotient singularities.
(b) Suppose that $X \to \Delta$ is as above.
Then, even without base-change, there is a birational model $g \colon Z \to X$ with following properties: (i) $Z$ has only pseudo-terminal singularities (ii) For all complete curves $C$ contracted by $g$, we have $K_Z \cdot C &gt; 0$.
(iii) For $t \in \Delta^{*}$, the morphism $Z_{t} \to X_{t}$ is the canonical model.
(iv) The special fibre $Z_0$ is normal, with only quotient singularities.

Notice that these results are non-vacuous even if the general fibre $X_{t}$ is smooth, since $X$ need not be $\mathbb{Q}$-Gorenstein.

**Proof (a):** After making a finite base change if necessary, there is by Knudsen's and Mumford's semi-stable reduction theorem [KKMS] a projective birational map $g \colon \tilde{X} \to X$ such that $\tilde{X}$ is smooth and the special fibre $\tilde{X}_0$ is reduced.
Now as explained in the introduction, there is a birationally equivalent model $Y$ with only terminal singularities such that the rational map $f \colon Y \to X$ is a morphism, and $K_Y$ is numerically effective relative to $f$.
Hence conditions (i)-(iii) hold.
Let $V$ denote the strict transform of $X_0$ in $Y_0$ and $\tilde{V}$ the normalization of $V$.
We can write $Y_0 = \sum V_i$, with $V_1 = V$.
Denote the exceptional locus of the

J. Kollár and N.I. Shepherd-Barron

morphism $h: \tilde{V} \to X_0$ by $\cup C_i$, where each $C_i$ is an integral curve.
We have $K_Y|*{\tilde{V}} \sim D - E + h^*F$, where $D, E$ are effective $\mathbb{Q}$-divisors supported on $\cup C_i$ with no common component and $F$ is a $\mathbb{Q}$-divisor on $X_0$.
By the negative definiteness of an exceptional locus, if $D \neq 0$, then there is a component $C_j$ of $D$ such that $C_j \cdot D &lt; 0$; this would imply that $K_Y \cdot C_j &lt; 0$, which is absurd.
So $K_Y|*{\tilde{V}} \sim -E + h^*F$.
Say $E = \sum v_i C_i, v_i \in \mathbb{Q}$ and $v_i \geq 0$.

If $Y_0 \neq \tilde{V}$ (i.e. if $Y_0$ is not normal), then by the adjunction formula $K_{\tilde{V}} \sim -\sum \mu_i C_i$ in a neighbourhood of $\cup C_i$, where for all $i, v_i - \mu_i$ is a non-positive integer, and for some value $j, \mu_j \geq v_j + 1$.
However, this would contradict the log terminal property of $X_0$, and so $Y_0$ is normal.

Consider the canonical model $Z \to \Delta$ of $X$ mentioned in the introduction.
This is obtained via a morphism $h: Y \to Z$ that contracts every complete curve $C$ for which $K_Y \cdot C = 0$.
Since $Y_0$ is irreducible, it follows that every surface contracted by $h$ is flat over $\Delta$, and so $Z$ has only pseudo-terminal singularities.

Since $K_Z$ is ample, $Z \cong \operatorname{Proj} \sum g_*(\omega_X^*)$.
For any finite map $\Delta' \to \Delta$ let $\tilde{X}' = \tilde{X} \times_{\Delta} \Delta'$, $X' = X \times_{\Delta} \Delta'$, $g' = G \times_{\Delta} \Delta'$.
Since $\tilde{X}/\Delta$ is semistable, $\tilde{X}'$ has canonical singularities.
Thus if we put $Z' = \operatorname{Proj} \sum g_*(\omega_{X'}^*)$ then $Z' = Z \times_{\Delta} \Delta'$.
By the above consideration $Z'$ has only pseudo-terminal singularities, hence by 5.1 (b), $Z_0$ has only log-terminal (≡quotient) singularities.
Since $K_{Y_0} \equiv h^* K_{Z_0}$, the same holds for $Y_0$.
This completes the proof of part (a).

In order to complete the proof of (b), suppose that $X \to \Delta$ is a one-parameter deformation of the quotient singularity $X_0$, and that $\Delta_1 \to \Delta$ is a finite base change, with Galois group $G$, such that $X_1 = X \times_{\Delta} \Delta_1$ admits a semi-stable resolution $\tilde{X}_1 \to X_1$.
Let $Z_1 \to \Delta$ be the canonical model of $\tilde{X}*1$; then the birational action of $G$ on $Z_1$ is in fact biregular.
Put $Z = Z_1 / G$; then $Z_1 \cong Z \times*{\Delta} \Delta_1$, and so by Lemma 3.4 $Z$ is $\mathbb{Q}$-Gorenstein.
Since the special fibres of $Z$ and $Z_1$ are the same and that of $Z_1$ is log terminal, it follows from Lemma 3.3 that $Z$ has just pseudo-terminal singularities.
Finally, the ampleness of $K_Z$ can be checked on the special fibre, and the geometric generic fibre of $Z$ is isomorphic to that of $Z_1$, and so has only RDP's. Q.E.D.

Corollary 3.6. If $X \to \Delta$ is a $\mathbb{Q}$-Gorenstein one-parameter deformation of the quotient singularity $X_0$, then $X$ has just a terminal singularity if the general fibre $X_t$ is smooth, and pseudo-terminal singularities if $X_t$ has only RDP's.

Proof.
By Lemma 3.3, we may ignore any base change.
Then by Theorem 3.5, there is a proper birational morphism $f \colon Y \to X$ that has at most one-dimensional fibres and is an isomorphism over the smooth locus of $X$; furthermore $Y$ has only terminal singularities.
Since $X$ is $\mathbb{Q}$-Gorenstein, it has just pseudo-terminal singularities, and terminal singularities if the general fibre $X_t$ is smooth.

Now fix a quotient singularity $(X_0, P)$.
Our aim is to analyze the versal deformation space $\operatorname{Def} X_0$ in terms of certain partial resolutions of $X_0$.

Definition 3.7. A normal surface singularity is of class $T$ if it is a quotient singularity and admits a $\mathbb{Q}$-Gorenstein one-parameter smoothing.
By Corollary 3.6 such a smoothing must be terminal.

These singularities will be given an explicit description below.

Threefolds and deformations of surface singularities

Definition 3.8. A $P$-resolution of $X_0$ is a partial resolution $f \colon Z_0 \to X_0$ such that $Z_0$ has only singularities of class $T$ and $K_{Z_0}$ is ample relative to $f$.

Next, we recall three things that are well-known to hold for any rational surface singularity $Y_0$.

(i) Every component of $\operatorname{Def} Y_0$ contains smoothings (cf [A 2, 3.1]).

(ii) If $f \colon Z \to Y_0$ is a normal partial resolution, then there is an induced map $F \colon \operatorname{Def} Z \to \operatorname{Def} Y_0$ of formal deformation spaces [Wa 1, 1.4].

(iii) If $f \colon Z \to Y_0$ is as above, $Q_1, \ldots, Q_r$ are the singular points of $Z$ and $Z_i$ is a representative of the germ $(Z, Q_i)$, then the natural morphism $\alpha \colon \operatorname{Def} Z \to \Pi_i \operatorname{Def} Z_i$ is smooth.

We can now state our main result; the proof will be given in stages.

Theorem 3.9. (i) If $Z_{i}$ is any germ of class $T$, then there is an irreducible subspace $\operatorname{Def} Z_{i} \subseteq \operatorname{Def} Z_{i}$ that corresponds to the $\mathbb{Q}$-Gorenstein deformations.
(We shall make this precise later.)

(ii) If $f \colon Z \to X_0$ is a $P$-resolution and $F \colon \operatorname{Def} Z \to \operatorname{Def} X_0$ is the induced map of deformation spaces, then $F(\operatorname{Def} Z)$ is an irreducible component of $\operatorname{Def} X_0$, where $\operatorname{Def} Z = \alpha^{-1}(\Pi_i \operatorname{Def}(Z_i))$.

(iii) If $Z, \bar{Z}$ are two $P$-resolutions of $X_0$ that are not isomorphic over $X_0$ and $F, \bar{F}$ are the corresponding maps of deformation spaces, then $F(\operatorname{Def} Z) \oplus \bar{F}(\operatorname{Def} \bar{Z})$.

(iv) Every component of $\operatorname{Def} X_0$ arises in this way.

In other words, there is a one-one correspondence between the components of $\operatorname{Def} X_0$ and the $P$-resolutions of $X_0$.

Before proving this, we shall determine the singularities of class $T$ and show how to find the $P$-resolutions of $X_0$.

Proposition 3.10. Suppose that $X_0$ is a quotient singularity having a terminal smoothing $X \to \Delta$.
Then either $X_0$ is an RDP or $X_0$ is a cyclic quotient singularity of the form $\operatorname{Spec} \mathbb{C}[[u, v]] / H$, where $H = \langle \alpha \rangle$ is of order $r^2 s$ for some integers $r, s$, and there is a primitive $r^2 s$'th root of unity, say $\eta$, such that the action of $H$ on $\operatorname{Spec} \mathbb{C}[[u, v]]$ is given by $\alpha(u, v) = (\eta u, \eta^{dsr-1} v)$, where $d$ is prime to $r$.
Moreover, every such cyclic quotient singularity admits a terminal smoothing.

Proof.
Let $Y \to X$ be the canonical cover, so that as before the special fibre $Y_0$ is the canonical cover of $X_0$.
Say $X = Y / G$, where $G = \langle \sigma \rangle$ is cyclic of order $r$.
Assume that $X_0$ is not an RDP, so that $r \geq 2$.
Then $Y$ is a cDV singularity with a $G$-invariant function on it whose vanishing defines the RDP $Y_0$.
Then the classification due to Danilov, Morrison and Stevens, and Mori of terminal singularities (completed below, in Theorem 6.5) shows that either $Y$ is smooth and $\sigma$ acts via $\sigma(x, y, z) = (\omega x, \omega^{-1} y, \omega^c z)$, where $\omega = \exp(2\pi i / r)$, $(c, r) = 1$ and $x, y, z$ are suitable local coordinates on $Y$, or $Y$ is given by an equation $xy + f(z, u^r) = 0$, where $\sigma$ acts via $\sigma(x, y, z, u) = (\omega x, \omega^{-1} y, z, \omega^c u)$ and $c$ is prime to $r$.
In either case $Y_0$ is of type $A$, and so by [Mo 1, Corollary 4] we can suppose that $Y_0$ is given by the equation $xy - z^{sr} = 0$, and the action of $\sigma$ is given by $\sigma(x, y, z) = (\omega x, \omega^{-1} y, \omega^c z)$.
It follows directly that $X_0$ is as described.

If conversely $X_0$ is one of these quotient singularities, then we can write $X_0 = Y_0 / \langle \sigma \rangle$, where $Y_0$ is given by $xy - z^{sr} = 0$ and $\sigma$ acts via $\sigma(x, y, z) = (\omega x, \omega^{-1} y, \omega^c z)$.

J. Kollár and N.I. Shepherd-Barron

$\omega^{-1}y, \omega^{c}z$). Thus we can write down a $\mathbb{Q}$-Gorenstein smoothing $X \to \varDelta = \operatorname{Spec} \mathbb{C}[[u]]$ by taking $X = Y / \langle \sigma \rangle$, where $Y$ is given by $xy - z^{sr} + u = 0$ and $\sigma$ acts on $Y$ via $\sigma(x, y, z, u) = (\omega x, \omega^{-1}y, \omega^{c}z, u)$.
By corollary 3.6, this is a terminal smoothing.

Another way of proving this first part of Proposition 3.10 is to note that if $X_0$ has a terminal smoothing and if $Z_0$ is a resolution of $X_0$, then $K_{Z_0}^2$ is an integer; Wahl has classified the quotient singularities with this property [Wa 3], and apart from RDP's they are as described in 3.10.

The next result, due essentially to Wahl [Wa 3], tells us how a cyclic quotient singularity of class $T$ may be recognized from its minimal resolution.

**Proposition 3.11** (i). The singularities $^{-4}$ and $^{-3}$ are of class $T$.

(ii) If the singularity $^{-b_1}$ is of class $T$, then so are

$$
\begin{array}{c c c c c c c}
- 2 &amp; - b _ {1} &amp; - b _ {r - 1} &amp; - b _ {r} - 1 \\
\bullet &amp; \bullet &amp; \bullet &amp; \bullet &amp; \bullet &amp; \bullet \\
\end{array}
\quad \text{and} \quad
\begin{array}{c c c c c c c}
- b _ {1} - 1 &amp; - b _ {2} &amp; - b _ {r} &amp; - 2 \\
\bullet &amp; \bullet &amp; \bullet &amp; \bullet &amp; \bullet \\
\end{array}
$$

(iii) Every singularity of class $T$ that is not an RDP can be obtained by starting with one of the singularities described in (i) and iterating the steps described in (ii).

**Proof.** Suppose that $X_0 = \operatorname{Spec} \mathbb{C}[[u, v]] / H$, where $H = \langle \alpha \rangle$ is cyclic of order $dm^2$ and $\alpha$ acts via $\alpha(u, v) = (\eta u, \eta^{adm-1} \cdot v)$, where $a$ is prime to $m$ and $a &lt; m$.
Write $\frac{dm^2}{adm-1} = b_1 - \frac{1}{b_2 - \ldots} = [b_1, \ldots, b_r]$, where each $b_i \geq 2$, so that the dual graph for the minimal resolution of $X_0$ is $\begin{array}{c} -b_1 \\ \bullet \end{array} \begin{array}{c} -b_2 \\ \bullet \end{array} \begin{array}{c} -b_r \\ \bullet \end{array}$.
Then $[b_r, \ldots, b_1] = dm^2 / (m - a)dm - 1$.
Suppose first that $b_1 = b_r = 2$.
Then $dm^2 / \{adm-1\} &lt; 2$ and $dm^2 / \{(m-a)dm-1\} &lt; 2$, so that $a &gt; \frac{1}{2}m$ and $m-a &gt; \frac{1}{2}m$; this is absurd, and so $b_1$ and $b_r$ cannot both be equal to 2. Next, suppose that $b_1 = 2$ and $b_r &gt; 2$, so that $\frac{dm^2}{adm-1} = 2 - \frac{1}{[b_2, \ldots, b_r]}$.
Then $[b_2, \ldots, b_r] = \frac{adm-1}{2(adm-1) - dm^2}$.
Since $(2(adm-1) - dm^2)(ad(m-a) - 1) \equiv 1 \cdot (\bmod adm-1)$, it follows that $[b_r, \ldots, b_2] = \frac{adm-1}{ad(m-a) - 1}$.
Then $[b_r - 1, b_{r-1}, \ldots, b_2] = \frac{da^2}{(m-a)da-1}$, which corresponds to a singularity of type $T$.

Finally, suppose that $b_1 &gt; 2$ and $b_r &gt; 2$.
In this case $a \leq \frac{m}{2}$ and $m - a \leq m / 2$, so that $a = 1$ and $m = 2$.
If $d = 1$, then $\frac{dm^2}{adm - 1} = [4]$; suppose therefore that $d &gt; 1$.
Then

$$
\begin{array}{l}
\frac {d m ^ {2}}{a d m - 1} = \frac {4 d}{2 d - 1} = 3 - \frac {2 d - 3}{2 d - 1} \\
= [ 3, 2, 2, \dots , 2, 3 ],
\end{array}
$$

where 2 appears $d - 2$ times.
This completes the proof.

Threefolds and deformations of surface singularities

We proceed to find the $P$ -resolutions of a fixed quotient singularity $(X, P)$ which is not an RDP.

Definition 3.12. A resolution $f \colon Y \to X$ is maximal if $K_{Y} \sim f^{*}K_{X} - \sum a_{i}E_{i}$ , where $0 &lt; a_{i} &lt; 1$ , and for any proper birational morphism $g \colon Z \to Y$ that is not an isomorphism, we have $K_{Z} \sim h^{*}K_{X} - \sum b_{j}F_{j}$ , where $h = f \circ g$ and some $b_{j} \leq 0$ .

Lemma 3.13. A quotient singularity $(X, P)$ has a unique maximal resolution.

Proof.
for any resolution $\pi_i\colon X_i\to X$ , we can write $K_{X_i}\sim \pi_i^* K_X + \sum_j(-1 + \alpha_j)E_j$

the $E_{j}$ being the exceptional curves.
If $Q = E_{j} \cap E_{j+1}$ , $\sigma \colon X_{i+1} \to X_{i}$ is the blow-up along $Q$ and $E_{k} = \sigma^{-1}(Q)$ , then $\alpha_{k} = \alpha_{i} + \alpha_{i+1}$ . Clearly, we may not blow up along a point lying on only one component.
Now if $\pi_{i}$ is the minimal resolution, every $\alpha_{i}$ lies between 0 and 1, and so to construct a maximal resolution one starts with the minimal resolution and successively blows up points where exceptional curves meet until the quantities $\alpha_{i}$ have the property that $\alpha_{i} &lt; 1$ for all $i$ , while if $E_{i} \cap E_{j} \neq \emptyset$ , then $\alpha_{i} + \alpha_{j} \geq 1$ . This certainly happens, and so a maximal resolution does exist.
Moreover, any two maximal resolutions are isomorphic in codimension one, and so isomorphic, since we are dealing with normal surfaces.

Lemma 3.14. Suppose that $(X, P)$ is a quotient singularity and that $f\colon Z \to X$ is a partial resolution such that $Z$ has only quotient singularities and $K_Z$ is ample relative to $f$ . Then $Z$ is dominated by the maximal resolution $X_m$ of $X$ .

Proof.
Suppose that $X_{m}$ does not dominate $Z$ . Then there is a point $Q \in X_{m}$ corresponding to a curve $C$ in $Z$ . The multiplicity of $C$ in $K_{Z}$ cannot be negative, by the defining property of $X_{m}$ . As we saw in the proof of 3.5, we have $K_{Z} \sim -E$ , with $E$ an effective $\mathbb{Q}$ -divisor.
The multiplicity of $C$ is non-negative, and so $C$ is not a component of $E$ . Hence $\operatorname{Supp} E \neq f^{-1}(P)$ , so that by the connectedness of $f^{-1}(P)$ there is a curve $G$ in $f^{-1}(P)$ such that $K_{Z} \cdot G &lt; 0$ ; this is absurd, and the lemma is proved.

Example 3.15. Consider the quotient $(X, P) = \operatorname{Spec} \mathbb{C}[[u, v]] / \langle \sigma \rangle$ , where $\sigma(u, v) = (\eta u, \eta^7 v)$ , $\eta = \exp(2\pi i / 19)$ . The minimal resolution is

![img-0.jpeg](img-0.jpeg)

where the negative integers are self-intersections and the positive numbers are the $\alpha_{i}$ occurring in the proof of Lemma 3.13. Then the maximal resolution $X_{m}$ is

![img-1.jpeg](img-1.jpeg)

and it is easy to see that the $P$ -resolutions are $Z_{1}, Z_{2}$ and $Z_{3}$ , where $Z_{1}$ is obtained from the minimal resolution by contracting the $(-2)$ curve (i.e. $Z_{1}$ is the RDP model of $X$ ), $Z_{2}$ is obtained from $X_{m}$ by contracting all curves

J. Kollár and N.I. Shepherd-Barron

except the $(-1)$ curve between the $(-4)$ and the $(-6)$ curve and $Z_{3}$ is obtained from the minimal resolution by contracting the $(-4)$ curve.
It will follow from Theorem 3.9 that $\operatorname{Def} X$ has exactly three components, the Artin component corresponding to $Z_{1}$.

Before proceeding with the proof of Theorem 3.9 we need some further preliminary results.

For any deformation $f \colon X \to S$ of $X_0$, define $j \colon X^0 \to X$ as the locus where $f$ is Gorenstein, and then define $\omega_{X / S}^{[n]} = j_*(\omega_{X^0 / S}^{\otimes n})$.
Suppose that $X_0$ is of index $r$.

**Lemma 3.16.** Suppose that $f \colon X \to S$ is a deformation of $X_0$ over the spectrum $S$ of a complete local ring $A$ and that $X$ is of finite index $m$ (i.e. that $\omega_{X / S}^{[m]}$ is invertible and that $m$ is the least positive integer $t$ such that $\omega_{X / S}^{[t]}$ is invertible).
Then $m = r$.

**Proof.** For any $n$ there is a natural map $\omega_{X / S}^{[m]} \otimes_{\mathcal{E}*S} k \to \omega*{X_0}^{[n]}$, where $k$ is the residue field of $S$, which is an isomorphism in codimension one.
Hence if $\omega_{X / S}^{[n]}$ is invertible, so is $\omega_{X_0}^{[n]}$, and so $r|m$.
Conversely, we wish to prove $m|r$.
First suppose that $A$ is Artinian.
Let $\pi \colon Y^0 \to X^0$ be the étale cover corresponding to $\omega_{X^0 / S}$; then $Y^0$ is connected.
To prove that $m|r$ it is enough to show that the special fibre $Y_0^0$ of $Y^0 \to S$ is connected.
But this is obvious, since $Y^0$ and $Y_0^0$ have the same underlying spaces.
In the general case, let $m$ denote the maximal ideal of $A$, put $A_n = A / m^n$, $S_n = \operatorname{Spec} A_n$ and $X_n = X \times_S S_n$.
By what we have just shown, we have $\omega_{X_0^n}^{\otimes r} / S_n \cong \mathcal{O}*{X_0^n}$ for every $n$; it follows that $\omega*{X^0 / S}^{\otimes n} \cong \mathcal{O}_{X^0}$, and the Lemma is proved.

Now suppose that $X_0$ is a singularity of class $T$ of index $r &gt; 1$.
Suppose that $Y_0$ is the canonical cover of $X_0$, and that $X_0 = Y_0 / G$, where $G = \langle \sigma \rangle \cong \mathbb{Z}_r$.
By 3.10 $Y_0$ is given by equation $xy - z^{rs} = 0$; in the notation of 3.10 we have $x = u^{rs}$, $y = v^{rs}$, $z = uv$ and $\sigma = \alpha^{rs}$, so that $\sigma$ acts via $\sigma(x, y, z) = (\varepsilon x, \varepsilon^{-1} y, \varepsilon^d z)$, where $\varepsilon = \eta^{sr}$.
Then it is clear that the locus $\operatorname{Fix} G \subseteq \operatorname{Def} Y_0$ is smooth of dimension $s$.

Our next object is to construct the subspaces $\operatorname{Def}^r$ mentioned in 3.9 (i).

**Definition 3.17.** Suppose that $X_0$ is a quotient singularity of class $T$ and index $r$.
If $\underline{S}$ is the category of finite local $\mathbb{C}$-algebras we define a functor $\operatorname{Def}^r X_0: \underline{S} \to \operatorname{Sets}$ by $\operatorname{Def}^r X_0(S) = \{\text{isomorphism classes of flat morphism } f: X \to S \text{ such that } X \otimes \mathbb{C} \cong X_0 \text{ and the sheaf } \omega_{X / S}^{[r]} \text{ is invertible}\}$.
This is pro-represented by a subspace of $\operatorname{Def}^r X_0$, which we denote by $\operatorname{Def}^r X_0$.

**Lemma 3.18.** In these circumstances, there is a natural morphism $\operatorname{Fix} G \to (\operatorname{Def}^r X_0)*{\mathrm{red}}$ that is $1 - 1$.
In particular, $(\operatorname{Def}^r X_0)*{\mathrm{red}}$ is irreducible and has smooth normalization.
Moreover, $\operatorname{Def}^r X_0$ contains smoothings.

**Proof.** Put $S = \operatorname{Fix} G$.
Let $Y \to S$ be the deformation induced from the versal deformation of $Y_0$, and put $X = Y / G$.
Since $G$ acts trivially on $S$, it follows from the existence of the Reynolds operator that the induced map $g \colon X \to S$ is flat.
Since $X$ is $\mathbb{Q}$-Gorenstein, $f$ is induced from $\operatorname{Def}^r X_0$, by Lemma 3.16. So there is a natural morphism $\beta \colon S \to \operatorname{Def}^r X_0$.

Now let $\varDelta=\operatorname{Spec}\mathbb{C}[[t]]$, and let $p\colon\varDelta\to\operatorname{Def}^r X_0$ be a map (called a formal arc), and let $X\to\varDelta$ the corresponding deformation.
By Lemma 3.16, $X$ and

Threefolds and deformations of surface singularities

$X_0$ have the same index, so that if $Y$ is the canonical cover of $X$ then $Y \to \Delta$ is a deformation of $Y_0$ . Hence $\Delta \subseteq \beta(S)$ , and so the image of $\beta$ is just $(\mathrm{Def}^* X_0)_{\mathrm{red}} = D$ , say and so in particular $D$ is irreducible.
Also, we have just shown that any formal arc in $D$ lifts to an arc in $S$ , and so $\beta$ is of degree one.
Finally since $\beta$ is a map of a local scheme, $\beta$ is $1 - 1$

Now suppose that $X_0$ is an arbitrary quotient singularity and that $f\colon Z_0\to X_0$ is a $P$ -resolution.
Suppose that $Q_{1},\ldots ,Q_{r}$ are the singular points of $Z_{0}$ , and let $Z_{i}^{*}$ denote the germ $(Z_0,Q_i)$ . There is a natural smooth morphism $\phi \colon \operatorname{Def}Z_0 \to \prod_{i = 1}^{r}\operatorname{Def}Z_{i}^{*}$ ; define $\operatorname{Def}^* Z_0$ to be $\phi^{-1}\left(\prod_{i = 1}^{r}\operatorname{Def}^* Z_i^*\right)$ .

Then clearly 3.9 (i) follows from 3.18.

Proof of 3.9 (iv).
Let $B$ be a component of $\operatorname{Def} X_0$ , and suppose that $\Delta$ is a general arc in $B$ ; we know that this corresponds to a smoothing $X \to \Delta$ of $X_0$ . By Theorem 3.5, the canonical model $Z \to \Delta$ of $X$ is a $\mathbb{Q}$ -Gorenstein smoothing of a $P$ -resolution $Z_0$ of $X_0$ . So if $F \colon \operatorname{Def} Z_0 \to \operatorname{Def} X_0$ is the natural map, we have $\Delta \subseteq F(\operatorname{Def}^* Z_0)$ . Since $X_0$ has only finitely many $P$ -resolutions, by 3.14, there is a $P$ -resolution $Z_0$ such that $F(\operatorname{Def}^* Z_0) = B$ . This proves 3.9 (iv).

Proof of 3.9 (ii), (iii).
Suppose that $Z_0, Z_0^*$ are two $P$ -resolutions of $X_0$ that are not isomorphic over $X_0$ . Let $F \colon \operatorname{Def} Z_0 \to \operatorname{Def} X_0$ , $F^* \colon \operatorname{Def} Z_0^* \to \operatorname{Def} X_0$ be the map of versal deformation spaces.
Assume that $F(\operatorname{Def} Z_0) \subseteq F^*(\operatorname{Def} Z_0^*)$ . Let $Z \to \Delta$ be a $\mathbb{Q}$ -Gorenstein smoothing of $Z_0$ ; these smoothings exist because each singularity of $Z_0$ admits such a smoothing, and through a general point of $\operatorname{Def} Z_0$ there passes an arc corresponding to a smoothing.
Consider the surface $Y$ obtained by contracting all the complete curves on $Z_{\mathrm{gen}}$ (the general fibre), and take a smoothing of $Y$ that lies on the Artin component of each singularity of $Y$ . The general fibre of this is smooth and contains no complete curves.
So by the openness of versality, there is a one-parameter smoothing $\tilde{Z} \to \Delta$ of $Z_0$ whose general fibre contains no complete curves, and whose total space $\tilde{Z}$ is a deformation of $Z$ . Since $Z$ is $\mathbb{Q}$ -Gorenstein, so is $\tilde{Z}$ , by [Ko2]. Hence we may assume that $Z_{\mathrm{gen}}$ contains no complete curves.
Thus if $X \to \Delta$ is the deformation of $X_0$ obtained from $Z \to \Delta$ via $F$ , the general fibre $X_{\mathrm{gen}}$ is smooth.
We also know that $X$ can be blown up to give a terminal smoothing $Z^* \to \Delta$ of $Z_0^*$ ; i.e., $Z$ and $Z$ are both canonical models of $X \to \Delta$ , and so $Z_0 \cong Z_0^*$ over $X_0$ . This contradiction completes the proof of Theorem 3.9.

We now indicate briefly how to compute the dimensions of the various components of $\operatorname{Def} X_0$ . Suppose that $Z$ is $P$ -resolution of $X_0$ , $Q_1, \ldots, Q_r$ its singularities and $B$ the component of $\operatorname{Def} X_0$ corresponding to $Z$ . We first refine 3.9 (ii) slightly.

Lemma 3.19. The map $\operatorname{Def}^* Z \to B$ is one to one.

Proof.
This follows from the fact that a one-parameter smoothing $X \to \Delta$ of $X_0$ that lies in $B$ can be blown up to give a unique smoothing $\tilde{Z} \to \Delta$ of $Z$ , by taking the canonical model.

Corollary 3.20. $\operatorname{Dim} B = \sum_{i=1}^{r} \dim \operatorname{Def}^*(Z, Q_i) + d$ , where $d$ is the dimension of the space $D$ of locally trivial deformations of $Z$ .

318 J. Kollár and N.I. Shepherd-Barron

Lemma 3.21. If $(X, P)$ is the singularity $\operatorname{Spec} \mathbb{C}[[u, v]] / G$, where $G = \langle \alpha \rangle \cong Z_{r^2 s}$ and $\alpha$ acts via $\alpha(u, v) = (\eta u, \eta^{dsr-1}v)$, where $\eta = \exp(2\pi i / r^2 s)$ and $(d, r) = 1$, then $\dim \operatorname{Def} X = s$.

Proof.
This follows directly from Proposition 3.10 and Lemma 3.18.

Remark 3.22. The dimension $d$ of the space $D$ occurring in Corollary 3.20 can be computed in terms of the dimensions of various Artin components, as follows.
Let $g \colon Y \to Z$ be the minimal resolution, and put $g^{-1}(Q_i) = C_i$, $C = \cup C_i$.
Put $h = f \circ g \colon Y \to X_0$ and $h^{-1}(P) = E$; let $F_1, \ldots, F_s (S \geq 0)$ denote the connected components of $\overline{E - C}$, let $X_i$ denote the germ of the singularity obtained by contracting $F_i$ and let $A_i$ denote the Artin component of $\operatorname{Def} X_i$.
Since $D$ can be identified with the sublocus of $\operatorname{Def} Y$ corresponding to deformations that preserve every component of $C$ so by 3.8 (iii) $D \cong \prod_{i} A_i$, thus $d = \sum \dim A_i$.

Remark 3.23. Return now to Example 3.15; we shall compute the dimensions of the components $B_{1}, B_{2}, B_{3}$ corresponding respectively to the partial resolutions $Z_{1}, Z_{2}, Z_{3}$.
Recall [Ri] that for a cyclic quotient of type $[b_{1}, \ldots, b_{r}]$, the Artin component has dimension $\sum (b_{i} - 1)$.
So we find

$$
\dim B_{1} = 1 + (3 - 1) + (4 - 1) = 6,
$$

$$
\dim B_{2} = 1 + 1 = 2,
$$

$$
\dim B_{3} = 1 + (3 - 1) + (2 - 1) = 4.
$$

Remark 3.24. In summary, we have shown, for any quotient singularity $X_0$, how to find the components of $\operatorname{Def}(X_0)$, that the components have smooth normalization and how to compute their dimensions, but we have said nothing of how the components intersect, or of what adjacencies occur over the various components.
We know only that singularities deform to quotient singularities [EV] and that the class of cyclic quotient singularities is closed under deformation (see ch. 7 for a direct geometrical proof of this).

§ 4. Semi-log-canonical singularities

Normal surfaces can be very effectively studied via their desingularizations.
One of the reasons is that if $f \colon Y \to X$ is a desingularization of a normal surface, then $f_{*} \mathcal{C}*{Y} = \mathcal{C}*{X}$.
Therefore, most cohomological questions on $X$ can be treated on $Y$ instead.
However, if $X$ is singular in codimension one, the desingularization does not carry any information about the singularities in codimension one.
One might try to remedy the problem by considering some conductor of $f \colon Y \to X$, but this is very cumbersome at best.

An alternate approach is to try to resolve singularities in codimension two only.
This seems to work much better, although we treat just the special case when the singularities in codimension one are normal crossing only.
As we shall see the results parallel very closely the case of normal surfaces.

Threefolds and deformations of surface singularities

An analogous theory can be developed for higher dimensional varieties.
Since for the purposes of the present article the surface case is sufficient, the general problem will be treated elsewhere.

Definition 4.1. A surface singularity $(x, X)$ is called a normal crossing point (resp.
pinch point) if it is analytically isomorphic to $(0, xy = 0) \subset (0, \mathbb{C}^3)$ (resp.
$(0, x^2 = zy^2) \subset (0, \mathbb{C}^3)$ ). Normal crossing will usually be abbreviated to n.c.. Note that we will not call the triple normal crossing point $(xyz = 0)$ an n.c. point.

Definition 4.2. A surface $X$ will be called semi-smooth if every closed point of $X$ is either smooth or n.c. or a pinch point.

The singular locus of a semi-smooth surface is a smooth curve $D_X$ , which will be called the double curve of $X$ . The normalization $\pi \colon \bar{X} \to X$ is smooth.
$\bar{D}_X = \pi^{-1}(D_X)$ is again smooth; $\pi \colon \bar{D}_X \to D_X$ is generically 2:1 and ramifies exactly at the pinch points.

Definition 4.3. A map $f \colon Y \to X$ is called a semi-resolution of $X$ if the following conditions are satisfied:

(i) $f$ is proper; (ii) $Y$ is semi-smooth; (iii) if $D_Y$ is the double curve of $Y$ , then no component of $D_Y$ is mapped to a point; (iv) there is a finite set $S \subset X$ such that $f \colon f^{-1}(X - S) \to X - S$ is an isomorphism.

Definition 4.4. (i) If $f \colon Y \to X$ is a semi-resolution, then a curve $E_i \subset Y$ is called exceptional if $f(E_i)$ is a point.
Let $E = \cup E_i$ be all the exceptional curves.

(ii) $f \colon Y \to X$ is called a good semi-resolution if it is a semi-resolution and $E \cup D_Y$ has smooth components and transverse intersections.
This implies that $E$ has at most double points and $E \cup D_Y$ at most triple points.

It is important to note that $E$ is not a Cartier divisor in general.
The only points where $E$ is non-Cartier are the pinch points; here $E$ is necessarily smooth.

Notions akin to these were introduced independently by the Dutch school.
They informed us that 4.5-4.15 are closely related to some of their results, especially to forthcoming works of van Straten [vS]. The following result is a very special case of a theorem of van Straten [vS].

Proposition 4.5. Let $X$ be a surface such that outside finitely many points $S \subset X$ it is either smooth or has normal crossing.
Then $X$ has a good semi-resolution.

Proposition-Definition 4.6. Notation as in 4.2. Let $E \subset X$ be a curve which is not contained in $D_X$ and let $\bar{E} = \pi^{-1}E$ . Since $\omega_{\bar{X}} = \pi^{*}\omega_{X}(-\bar{D}_{X})$ , the usual adjunction formula gives

$$
2 g (\bar {E}) - 2 = \left(\omega_ {\bar {X}} + \bar {E}\right) \cdot \bar {E} = \bar {E} ^ {2} + \deg_ {E} \omega_ {X} - \bar {E} \cdot \bar {D} _ {X}.
$$

Therefore we get:

(i) $\bar{E}^2 &lt; 0$ and $\deg_E\omega_X &lt; 0$ iff $\bar{E}$ is exceptional of the first kind and does not intersect $\bar{D}_X$ . (ii) $\bar{E}^2 &lt; 0$ and $\deg_E\omega_X = 0$ iff either $\bar{E}$ is exceptional of the first kind and intersects $\bar{D}_X$ once or $\bar{E}^2 = -2$ , $\bar{E}\cong \mathbb{P}^1$ and $\bar{E}$ does not intersect $\bar{D}_X$ .

J. Kollár and N.I. Shepherd-Barron

In the first two cases (i.e. when $\bar{E}^2 = -1$) we shall call $E$ a $-1$ curve on $X$.
It is clear that one can contract $E \subset X$ and the resulting surface $X'$ is again semi-smooth.

Corollary 4.7. Let $X$ be semi-smooth and $f \colon Y \to X$ be semi-resolution.
Then $X$ can be obtained from $Y$ by repeatedly contracting $-1$ curves.

Proof.
Consider $\bar{f} \colon \bar{Y} \to \bar{X}$.
If this is not an isomorphism, then there is an exceptional curve of the first kind $\bar{E} \subset \bar{Y}$, contracted by $\bar{f} \cdot \bar{E} \cdot \bar{D}_Y \leq 1$ since otherwise $\bar{D}_X$ would be singular.
Therefore, $E$ is a $-1$ curve and so it can be contracted.

Corollary 4.8. With the above notation let $E_i \subset Y$ be the exceptional curves.
Then $\omega_Y = f^* \omega_X (\sum a_i E_i)$ and $a_i \geq 0$.

Proof.
It is easy to check this for a single contraction; thus the claim follows from 4.7. We note for 4.6. (ii) we get $a_1 = 0$.

Definition 4.9. A semi-resolution $f \colon Y \to X$ is called minimal if no $-1$ curve is contracted by $f$.

Proposition 4.10. Let $X$ be a surface such that for a finite set of points $S \subset X$, $X - S$ is semi-smooth.
Then $X$ has a unique minimal semi-resolution.

Proof.
Let $f \colon Y \to X$ be a semi-resolution.
Now contract all $-1$ curves on $Y$ that are contracted by $f$.
This way we get a minimal semi-resolution.
Uniqueness can be proved the same way as for normal surfaces.

Definition 4.11. (i) Let $f \colon Y \to X$ be a good semi-resolution of $X$, and let $E_i$ be the exceptional curves.
It is called a minimal good semi-resolution if for every $-1$ curve $E_i$, contracted by $f$, we have $\bar{E}*i \cdot \sum*{j \neq i} \bar{E}_j + \bar{E}_i \cdot \bar{D}_Y &gt; 2$.
If one starts with a good semi-resolution, then one can repeatedly contract $-1$ curves that do not satisfy the above requirement and obtain a minimal good semi-resolution.

Proposition 4.12. (Reid [Re1, 2.6]) Let $f \colon Y \to X$ be a semi-resolution of $X$ and let $E_i$ be the exceptional curves.
Then

(i) There is a unique cycle $Z = -\sum a_i E_i$ such that $\bar{Z} \cdot \bar{E}*i = -\deg*{E_i} \omega_Y$.
(The $a_i$ are rational in general.)

(ii) If $f$ is the minimal semi-resolution then $Z \geq 0$.

(iii) If $X$ is Cohen-Macaulay, $f$ is minimal and $Z = 0$, then $X$ is either a smooth, an n.c. or a pinch point or a DuVal singularity.

(iv) If $X$ is Cohen-Macaulay and $f$ is minimal, then $Z = 0$ or $-a_i &gt; 0$ for every $i$.

(v) If $X$ is Gorenstein and $f$ is a minimal good semi-resolution, then either $Z = 0$ or $-a_i &gt; 0$ for every $i$.

Proof.
The intersection matrix $\bar{E}_i \cdot \bar{E}*j$ is negative definite; this shows the existence of $Z$.
If $f$ is minimal, then $\deg*{E_i} \omega_Y \geq 0$, and (ii) is a formal consequence of this as in [Z, 7.1]

Assume that $a_i = 0$ for some $i$.
Then $\bar{Z} \cdot \bar{E}_i \geq 0$, with equality only if $a_j = 0$ for every $E_j$ such that $\bar{E}*j \cdot \bar{E}*i &gt; 0$.
If $f$ is minimal, then $-\deg*{E_i} \omega_Y \leq 0$; hence we have $\deg*{E_i} \omega_Y = 0$.
By 4.6 (ii) $E_i$ is therefore a $-2$ curve that does not intersect

Threefolds and deformations of surface singularities

$D_{Y}$ . If $\overline{E}*j\cdot \overline{E}*i &gt; 0$ , then again we get that $E*{j}$ is such a $-2$ curve.
$E*{i}$ lies on an irreducible component $Y^{\prime}$ of $Y$ and by the above $Y^{\prime}$ contains no double curve.
Hence it is a connected component.
If $X$ is Cohen-Macaulay, then by [Hart] this implies that $Y^{\prime} = Y$ . Hence $X$ is a DuVal singularity.
This proves both (iii) and (iv).

(v) follows from (iv) as in [Z, 7.1].

Proposition 4.13. Let $f \colon Y \to X$ be a semi-resolution of a Cohen-Macaulay surface.
Then

(i) $f_{*}\mathcal{O}*{Y} = \mathcal{O}*{X},$ (ii) $R^1 f_* \omega_Y = 0$ , (iii) $R^1 f_* \mathcal{O}*Y$ and $\omega_X / f** \omega_Y$ are dual to each other.

Proof.
(i) $\mathcal{O}*X \subseteq f** \mathcal{O}_Y$ and they agree in codimension one.
Since $\mathcal{O}_X$ is $S_2$ they are equal.

(ii) We have an exact sequence $0 \to \pi_* \omega_{\bar{Y}} \to \omega_Y \to Q \to 0$ , where $Q$ is supported on $D_Y$ . $R^1 f_* \pi_* \omega_{\bar{Y}} = 0$ by Grauert-Riemenschneider vanishing [G-R], and $R^1 f_* Q = 0$ since $\pi|D_Y$ is finite.
This proves (ii).
(iii) This can be proved the same way as for normal $X$ . See e.g. [Ko 1, 3.3.3].

Definition 4.14. Let $f \colon Y \to X$ be a semi-resolution of a Cohen-Macaulay surface singularity.
$X$ is called semi-rational if $R^1 f_* \mathcal{O}_Y = 0$ .

Remark 4.15. (i) It is easy to check that this definition is independent of the semi-resolution.

(ii) This definition declares n.c. and pinch points to be "rational".
This is a reasonable thing to do.
We hope that everyone agrees that a n.c. point should be considered "rational".
A pinch point is a quotient of a n.c. point so it should be rational.
(iii) It is true that the deformation of a semi-rational singularity is semirational again [vS].

Definition 4.16. (i) If $F$ is a rank one sheaf, then $F^{[s]}$ denotes the double dual of the $s^{\text{th}}$ tensor power of $F$ .

(ii) A singularity $(x,X)$ is called $\mathbb{Q}$ -Gorenstein if $\omega_X^{[s]}$ is locally free for some $s &gt; 0$ and $X$ is Cohen-Macaulay.
The smallest such $s$ is called the index of $(x,X)$ .

Definition 4.17. Let $(x,X)$ be a $\mathbb{Q}$ -Gorenstein surface singularity such that $X - x$ is semi-smooth.
Let $f\colon Y\to X$ be a good semi-resolution of $X$ . We can write $\omega_{Y}^{s}\cong f^{*}\omega_{X}^{[s]}\otimes \mathcal{O}(\sum sa_{i}E_{i})$ , where the $E_{i}$ are exceptional divisors and the $a_{i}$ are rational.
With the notation of 4.11, we have that $Z = \sum a_{i}E_{i}$ . $(x,X)$ is called

(i) semi-canonical if $a_{i}\geq 0$ (ii) semi-log-terminal if $a_{i} &gt; -1$ (iii) semi-log-canonical if $a_{i}\geq -1$

Remark 4.18. (i) Using 4.8 one can easily see that these notions are independent of the good semi-resolution chosen.

(ii) One could try to define semi-terminal by $a_i &gt; 0$ . This, however, would not be independent of the resolution chosen.

J. Kollár and N.I. Shepherd-Barron

(iii) If $f' \colon Y' \to X$ is any semi-resolution of $X$ and if $Z' = \sum a_i' E_i'$, then $X$ is semi-canonical iff $a_i' \geq 0$.
This follows easily from 4.8.

(iv) With the above notation, if $X$ is semi-log-terminal (resp.
canonical), then $a_{i} &gt; -1$ (resp.
$\geq -1$).

**Definition 4.19.** The rest of this chapter will be devoted to the classification of the above singularities.
For normal surfaces this was done by Kawamata [Kaw1]; see also [Kaw2]. The general case runs very much along the same lines.
Using 4.12 the Gorenstein case can be handled very efficiently.
Therefore we shall give full proofs for this.
First we have to recall the definition of certain singularities.

**Definition 4.20.** (i) [Sai] A normal Gorenstein surface singularity is called simple elliptic if the exceptional divisor of the minimal resolution is a smooth elliptic curve.

(ii) [Kar1] A normal Gorenstein surface singularity is called a cusp if the exceptional divisor of the minimal resolution is a cycle of smooth rational curves or a rational nodal curve.

(iii) [S-B2] Let $X$ be a Gorenstein surface singularity which has a minimal semi-resolution $f \colon Y \to X$.
$X$ is called a degenerate cusp if $X$ is not normal and the exceptional divisor is a cycle of smooth rational curves or a rational nodal curve.
In this case $Y$ has no pinch points and the irreducible components of $X$ have cyclic quotient singularities.

**Theorem 4.21.** Let $(x, X)$ be a Gorenstein surface singularity such that $X - x$ is semi-smooth.
Then

(i) $X$ is semi-canonical iff $x \in X$ is either a smooth, a n.c. point, a pinch point or a DuVal singularity.

(ii) $X$ is semi-log-canonical iff $X$ is either a simple elliptic singularity, a cusp, a degenerate cusp or semi-canonical.

**Proof.** (i) Assume that $X$ is semi-canonical and let $f \colon Y \to X$ be the minimal good semi-resolution.
Let $\omega_{Y} = f^{*} \omega_{X} \otimes \mathcal{O}(-Z)$.
Since $X$ is semi-canonical we have $-Z \geq 0$.
By 4.12 $Z \geq 0$.
So $Z = 0$ and by 4.12 $X$ is one of those listed.

(ii) With the above notation we have $Z = \sum a_{i} E_{i}$.
If $Z = 0$, then $X$ is semi-canonical, so assume that $Z \neq 0$.
Then $a_{i} &gt; 0$ by 4.12 and $a_{i} \leq 1$ by definition.
Thus $Z = \sum E_{i}$, the reduced exceptional divisor.

$$
\omega_{Z} \cong \omega_{Y} \otimes \mathcal{O}(Z) \mid Z \cong f^{*} \omega_{X} \otimes \mathcal{O}(-Z + Z) \mid Z \cong \mathcal{O}_{Z}.
$$

Hence $h^0(\mathcal{O}_Z) = h^1(\mathcal{O}_Z) = 1$ (since $Z$ is reduced and connected).

The adjunction formula now gives

$$
2 g(\bar{E}_{i}) - 2 = \bar{E}_{i}^{2} - Z \cdot \bar{E}_{i} - \bar{E}_{i} \cdot \bar{D}_{Y} = - \bar{E}_{i} \cdot \sum_{j \neq i} \bar{E}_{j} - \bar{E}_{i} \cdot \bar{D}_{Y}.
$$

Therefore $g(\bar{E}_i) \leq 1$.
If $g(\bar{E}_i) = 1$, then $\bar{E}_i$ intersects neither $\bar{D}_Y$ nor any other $\bar{E}_j$.
Hence $E_i$ is the only exceptional curve and $\bar{D}_Y = 0$.
Consequently, $X$ is normal and either simple elliptic or a cusp and $E_i$ is a nodal cubic.
Otherwise, $g(\bar{E}_j) = 0$ for every $j$ and $\bar{E}_j$ has two intersections with the rest of $\bar{E}_i$'s and $\bar{D}_Y$.

Threefolds and deformations of surface singularities

If $X$ is normal, then $D_Y = 0$.
Thus each $E_i$ intersects two others, and hence they form a cycle.
$X$ is a cusp.

If $X$ is not normal, then on each component of $\overline{Y}$ the exceptional curves form a chain and the two curves at the end intersect $\overline{D}_Y$.
On $Y$ the $E_i$'s form either a cycle, in which case $X$ is a degenerate cusp, or a chain.
The latter is impossible since $h^1(\mathcal{O}_Z) = 1$, and this completes the proof.

The classification of the non-Gorenstein case is reduced to the Gorenstein one by the usual Reid-Wahl cyclic covering trick.
The proof is the same as in the normal case [Re 2, 1.7–1.9]; therefore we state only the result in the form best suited to our purpose.

**Proposition 4.22.** Let $(z,Z)$ be a semi-log-canonical surface singularity.
Then there is a Gorenstein semi-log-canonical singularity $(x,X)$ and an action of a cyclic group $\mathbb{Z}_r$ on $(x,X)$ such that

(i) The action is free on $X - x$.

(ii) The action of $\mathbb{Z}*r$ on $\omega_X / m_x\omega_X$ is faithful ($m*{x} =$ the ideal of $x\in X$)

(iii) $(z,Z) = x,X) / \mathbb{Z}_r$

(iv) $r = \text{index of } Z$.

If $Z$ is semi-log-terminal, then $X$ is in fact semi-canonical.

**Theorem 4.23.** The semi-log-terminal surface singularities are exactly the following.

(i) Quotients of $\mathbb{C}^2$, enumerated by Brieskorn [Br1],

(ii) Normal crossing or pinch points,

(iii) $xy = 0$ modulo the group action $x \to \varepsilon^a x$; $y \to \varepsilon^b y$; $z \to \varepsilon z$, where $\varepsilon$ is a primitive $r^{\text{th}}$ root of unity; $(a, r) = 1$, and $(b, r) = 1$.

(iv) $xy = 0$ modulo the group action $x \to \varepsilon^a y$, $y \to x$, $z \to \varepsilon z$ where $\varepsilon$ is a primitive $r$'th root of unity, $4 \mid r$ and $(a, r) = 2$.

(v) $x^{2} = z y^{2}$ modulo the group action $x \to \varepsilon^{1 + a} x$, $y \to \varepsilon^{a} y$, $z \to \varepsilon^{2} z$, $r \text{ odd}, (a, r) = 1$.

**Proof.** Quotients of DuVal points give the first case (cf.
[Br 1]).

A $\mathbb{Z}_r$-action on $xy = 0$ can be assumed to be linear on $\mathbb{C}^3$ and it is easy to enumerate them.
(iii) is the case where the two branches are not interchanged, and (iv) is the case where they are.

The normalization of $(x^{2} = z y^{2})$ is $\mathbb{C}^2$, where the possible actions are understood.
It is easy to decide which ones descend to an action on the pinch point.

**Theorem 4.24.** The semi-log-canonical surface singularities are exactly the following:

(i) The semi-log-terminal ones enumerated in 4.23,

(ii) The Gorenstein ones enumerated in 4.21 (ii),

(iii) $\mathbb{Z}_2, \mathbb{Z}_3, \mathbb{Z}_4$ and $\mathbb{Z}_6$ quotients of simple elliptic ones enumerated in (Kaw 1, pp. 226–227],

(iv) $\mathbb{Z}_2$ quotients of cusp and degenerate cusps.

**Proof.** The only new case is that of quotient of degenerate cusps; the argument of [Kaw 2, 9.6] yields that only $\mathbb{Z}_2$ quotients should be considered.

**Remark 4.25.** [Kaw 1, pp. 226–227] lists the dual graph of the minimal resolution of the singularity.
The first one is a $\mathbb{Z}_2$ quotient of a cusp; this we consider

J. Kollár and N.I. Shepherd-Barron

in (iv).
Note also that the last graph is incorrect.
It should be

![img-2.jpeg](img-2.jpeg)

It is not difficult, and very instructive, to work out the minimal semi-resolution of these singularities.
In the nonnormal case there are three basic building blocks.

Definition 4.26. We define three types of objects that can be components of the pair $(\bar{Y},\bar{D}_Y)$ for a minimal resolution of a semi-log-canonical singularity.

(i) $(A, \mathbb{Z}_n, a, \Delta)$ or $(A, \Delta)$ denotes the minimal resolution of the singularity $\mathbb{C}^2 / \mathbb{Z}_n (x \to \varepsilon x, y \to \varepsilon^a y)$ and $\Delta$ the proper transform of the image of the $x$ -axis.
(ii) $(A, \mathbb{Z}_n, a, 2\Delta)$ or $(A, 2\Delta)$ the same as if $n &gt; 2$ above except that $2\Delta$ is the proper transform of the image of the $x$ and $y$ axes.
For $n = 1$ we blow up the origin of $\mathbb{C}^2$ once.
(iii) $(C, \Delta)$ denotes the minimal resolution of a dihedral quotient of $\mathbb{C}^2$ , $\Delta$ is the proper transform of the coordinate axes.
( $\Delta$ will have only one component.)

These are the same objects as given in [Kaw 2, 9.6 (5), (7) and (6)].

(iv) If $(X, \Delta)$ is one of the above objects, then $\Delta$ is a small disc which intersects the exceptional divisor in one point, which we can take as the origin of some coordinatization of $\Delta$ . By the expression “ $(X, \Delta)$ with $\Delta$ pinched together” we mean the object we obtain from $X$ by identifying $d \in \Delta$ with $-d \in \Delta$ . This way we get a pinch point at the origin.

Proposition 4.27. The minimal semi-resolutions of the semi-log-canonical singularities are given as follows:

4.23 (i) See Brieskorn [Br 1].

(ii) identity resolution.

(iii) $(A, \mathbb{Z}_r, a, \Delta)$ and $(A, \mathbb{Z}*r, b, \Delta)$ attached along the curves $\Delta$ . (iv) $(A, \mathbb{Z}*{r/2}, \frac{1}{2} a, \Delta)$ pinched along $\Delta$ . (v) $(A, \mathbb{Z}_r, a, \Delta)$ pinched along $\Delta$ .

4.24 (iii) see Kawamata [Kaw 2,9] and 4.25.

(vi) The $\mathbb{Z}_2$ quotient of a cusp is in [Kaw1, p. 266] (the first graph).
The quotient of a degenerate cusp is constructed as follows.
There are some components of type $(A, 2\Delta)$ arranged in a chain.
At the ends we have either $a(C, \Delta)$ component or an $(A, 2\Delta)$ component with one component of $\Delta$ pinched.
We can also have only one $(A, 2\Delta)$ with both components of $\Delta$ pinched.

Remark 4.28. Both (iii) and (iv) are of the form $(A, \mathbb{Z}_n, \Delta)$ with $\Delta$ pinched.
However, if $n$ is even, then the index is $2n$ , while if $n$ is odd, then the index is $n$ . This is somewhat surprising.

Remark 4.29. Let $(x,X)$ be a singularity such that $X - x$ is semi-smooth and let $D\subset X$ be the double curve.
Let $g\colon \bar{X}\to X$ be the normalization and $\varDelta=g^{*}D$ . Kawamata [Kaw2, 9] defines the notion of the pair $(\bar{X},\varDelta)$ being log-canonical.
One can easily prove the following.

Threefolds and deformations of surface singularities

Proposition 4.30. If $X$ is $\mathbb{Q}$-Gorenstein, then $X$ is semi-log-canonical iff $(\bar{X}, \Delta)$ is log-canonical.

However, there are many cases when $(\bar{X}, \Delta)$ is log-canonical but $X$ is not $\mathbb{Q}$-Gorenstein.
For example, this is the case when the minimal semi-resolution has two components $(A, \mathbb{Z}_n, \Delta)$ and $(A, \mathbb{Z}_m, \Delta)$ attached along $\Delta$ and $n \neq m$.
This follows at once from 4.24, but it is not easy to get this directly.
This phenomenon, namely that information is lost after normalization or becomes less accessible, was our main reason for considering non-normal surfaces directly.

§ 5. Deformations of semi-log-canonical singularities and surfaces at the boundary of moduli

In the introduction, we mentioned that one of our motivating problems is that of compactifying moduli spaces for surfaces of general type.
In this section we shall first show that the appropriate singularities to permit on the surfaces at the boundaries of moduli spaces are semi-log-canonical (s.l.c.), and secondly we shall make precise the moduli problem to consider.

The first part amounts to showing that if $\bar{X} \to \Delta$ is a semi-stable family of surfaces of general type and $X \to \Delta$ is its canonical model, then the special fibre $X_0$ has just s.l.c. singularities, and that conversely if $X \to \Delta$ is a one-parameter deformation of the surface $X_0$ that has just s.l.c. singularities, if the general fibre $X_t$ has only RDP singularities and if $X$ is $\mathbb{Q}$-Gorenstein, then $X$ has just canonical singularities.
This is made precise in Theorem 5.1, which is a generalization of Corollary 3.6.

Theorem 5.1. Suppose that $X \to \Delta$ is a $\mathbb{Q}$-Gorenstein one-parameter deformation of the surface $X_0$.

(a) Suppose that $X$ admits a resolution $\bar{X} \to X$ such that the composite $\bar{X} \to \Delta$ is semi-stable.
Then $X$ has canonical singularities if and only if $X_0$ has s.l.c. singularities and for $t \neq 0$, $X_t$ has only RDP's.

(b) The product $X \times_{\Delta} \Delta_1$ has canonical (resp.
pseudo-terminal, resp.
terminal) singularities for all finite base changes $\Delta_1 \to \Delta$ if and only if $X_0$ has s.l.c. (resp.
s.l.t., resp.
quotient) singularities and for $t \neq 0$.
$X_t$ has only RDP's (resp.
RDP's, resp.
no singularities).
In particular, if $X_0$ has s.l.c. (resp.
s.l.t., resp.
quotient) singularities and for $t \neq 0$, $X_t$ has RDP's (resp.
RDP's, resp.
no singularities), then $X$ has only canonical (resp.
pseudo-terminal, resp.
terminal) singularities.

Proof.
(a) By localizing, we can replace $X_0$ by the germ $(X_0, P)$.
Suppose that $X$ has canonical singularities.
Let $V$ be a component of $X_0$, $D$ its double curve with reduced structure and $W$ the strict transform of $V$ in $\bar{X}$.
Let $\mu: W \to V$ denote the induced map.
We can write $K_W \sim \mu^*(K_V + D) + \sum a_i F_i$, where $\cup F_i$ is the union of the exceptional locus of $\mu$ with the strict transform of $D$ and $a_i = -1$ if $\dim \mu(F_i) = 1$.
Now $K_{\bar{X}} \sim \pi^* K_X + \sum v_i E_i$, where the $E_i$ are the exceptional divisors in $\bar{X}$ and every $v_i \geq 0$, then by the adjunction formula $a_j \geq -1$ for every $j$.
I.e. the pair $(V, D)$ is log canonical in the sense of Kawamata [Kaw2] and so by 4.30, $X_0$ is s.l.c. That $X_t$ has only RDP's is clear.

J. Kollár and N.I. Shepherd-Barron

Conversely, suppose that $X_0$ has s.l.c. singularities and that $X_t$ has RDP's for $t \neq 0$ . Let $X'$ denote a minimal model of $\tilde{X}$ , so that there is a factorization $\tilde{X} \to X' \to X$ over $\Delta$ . Let $V, D$ be as above and $W'$ the strict transform of $V$ in $X'$ . Let $v: W' \to V$ denote the induced map.
Since by 4.30 $X_0$ has log canonical singularities, we can write $K_{W'} \sim v^*(K_V + D) + \sum a_i F_i$ , where $a_i \geq -1$ and $a_i = -1$ if $\dim v(F_i) = 1$ . Since by the adjunction formula $K_{X'} | W' \sim K_{W'} + G$ , where $G$ is the reduced sum of the double curves on $W'$ , we get $K_{X'} | W' \sim v^*(K_V + D) + \sum b_j H_j$ , where the $H_j$ are the exceptional curves of $v, b_j = a_j + 1$ if $H_j$ is a double curve in $X_0'$ and $b_j = a_j$ otherwise.
Then since $\cup_{H_j}$ is connected and $K_{X'}$ is numerically effective, it follows that if some $H_j$ is a double curve in $X_0'$ , then every $H_j$ is double and every $a_i = -1$ . In this case, $K_{X'} \cdot H_j = 0$ for all $j$ . Now let $X''$ denote the canonical model of $X'$ and $g: X' \to X''$ the corresponding contraction.
Then for every component $V$ of $X_0$ with strict transform $W''$ in $X''$ , no exceptional curve of the contraction $W'' \to V$ is a double curve in $X_0''$ . Hence for every exceptional divisor $E$ of the morphism $h: X'' \to X$ , the centre of $E$ on $X$ is not $P$ . Since $X$ certainly has canonical (in fact $cDV$ ) singularities outside $P$ , it follows that $K_{X'} \sim h^* K_X + B$ , where $B \geq 0$ , and so $X$ has canonical singularities.

The proof of (b) is very similar, and so omitted.

5.2. We pause to consider which s.l.c. singularities admit one-parameter $\mathbb{Q}$ -Gorenstein deformations to RDP's. We refer to the classification given in Theorems 4.21, 4.23, 4.24.

4.21. (i): All

(ii) The simple elliptic singularities of multiplicity at most 9 [Pi2]. For cusps the problem is unsolved, and we have nothing to contribute.
Recently J. Stevens showed that all degenerate cusps are smoothable (unpublished).

4.23. (i): See Proposition 3.10

(iii) Only those with $a + b = r$ (iv), (v): None

All these can be proved as in 3.10.

4.24. (iii) The $\mathbb{Z}_2$ -quotients of simple elliptic points have dual graph

![img-3.jpeg](img-3.jpeg)

and admit deformations as above if and only if $3 \leq d \leq 6$ . There are examples of $\mathbb{Z}_3$ - and $\mathbb{Z}_4$ -quotients possessing the deformations we see.

(iv) This is at least as hard as determining which cusps are smoothable, but there are examples of arbitrarily high multiplicity.

Theorem 5.3. Suppose that $X \to \Delta$ is a one-parameter deformation of the normal s.l.c. singularity $(X_0, P)$ , and that $X$ has a semistable $\tilde{X}$ . Let $X' \to \Delta$ be a minimal model of $\tilde{X} \to \Delta$ . Then either the special fibre $X_0'$ has only RDP's or quotient

Threefolds and deformations of surface singularities

singularities of class $T$ (i.e. normal log terminal singularities) or $X$ has just canonical singularities.

Proof.
Write $X_0' = \cup V_i$ , where $V_1 = V$ is the strict transform of $X_0$ . Let $\tilde{V}$ be the normalization of $V$ and let $f \colon \tilde{V} \to X_0$ be the contraction.
Write $K_X | \tilde{W} \sim -E + f^* F$ , where $F$ is a $\mathbb{Q}$ -divisor on $X_0$ and $E = \sum v_i C_i$ , where the $C_i$ are exceptional curves of $f$ , where $v_i \in \mathbb{Q}$ , and $v_i \geq 0$ since $K_X$ is numerically effective and the exceptional locus of $f$ is negative definite.
So in a neighbourhood of $f^{-1}(p) = \cup C_i$ , we have $K_{X'} | \tilde{W} \sim -\sum v_i C_i$ . By the adjunction formula, $K_{\tilde{V}} \sim -\sum \mu_i C_i$ , where $\mu_i = v_i$ if $C_i$ is not a double curve and $\mu_i = v_i + 1$ if $C_i$ is a double curve.
The condition that $X_0$ be log canonical implies that $\mu_i \leq 1$ for all $i$ , so that if we assume $C_r$ to be double, then $\mu_r = 1$ and $v_r = 0$ . Since $K_{X'}$ is numerically effective and $\cup C_i$ is connected, it follows that $v_i = 0$ for all $i$ . Then $K_{X'}$ is numerically trivial on $\cup C_i$ , so that if $\pi \colon X' \to X''$ is the contraction to the canonical model, then $\pi$ contracts $\cup C_i$ to a point.
So either no curve $C_i$ is double, in which case $X_0'$ is normal, or $X'' = X$ , and the theorem follows from the classification of log-terminal singularities.

5.4. We shall now make precise the moduli problem that we want to consider.
Fix positive integers $A, B, N$ ; then we should like to construct a coarse moduli space (at least in the category of algebraic spaces) for those schemes $S$ satisfying the following properties:

(i) $S$ is a reduced projective surface; (ii) $S$ is connected with only s.l.c. singularities; (iii) the sheaf $\omega_{S}^{[N]}$ , defined by $\omega_{S}^{[N]} = j_{*}(\omega_{S_{0}}^{\otimes N})$ , where $j\colon S_0\to S$ is the locus of Gorenstein points of $S$ in an ample line bundle; (iv) the self-intersection $K_S^2$ , defined to be $\frac{1}{N^2} (\omega_S^{[N]}\cdot \omega_S^{[N]})$ , equals $A$ ; (v) $\chi (\mathcal{C}_S) = B$

The functor $\mathcal{M}$ : (Schemes) $\rightarrow$ (Sets) under consideration is given by $\mathcal{M}(T) = \{\text{isomorphism classes of flat projective morphisms } f\colon \mathcal{S} \to T \text{ such that (i)-(v) above hold for every geometric fibre of } f \text{ and for every geometric point } t \in T, \text{ the natural map } \omega_{\mathcal{S}/T}^{[N]} \otimes k(t) \to \omega_{\mathcal{S}/T}^{[N]}\}$ is an isomorphism, where $\omega_{\mathcal{S}/T}^{[N]} = j_*(\omega_{\mathcal{S}_0/T}^{N}), j\colon \mathcal{S}_0 \to \mathcal{S}$ being the inclusion of the locus where $f$ is a Gorenstein morphism\}. More briefly, we should be concerned with families of semi-log canonical surfaces in which the formation of $\omega^{[N]}$ commutes with specialization; this is required to ensure that any resulting moduli space will be separated.

This approach raises several questions:

(1) Given positive integers $A, B$ , does there exist an integer $N$ , depending only on $A$ and $B$ , and such that whenever $S$ is the special fibre of a relative canonical model $X \to \Delta$ whose general fibre satisfies $K^2 = A$ and $\chi(\mathcal{C}) = B$ , the index of $S$ divides $N$ ? (2) Given positive integers $A, B, N$ , is there a number $M$ such that for every s.l.c. surface $S$ with $K_S^2 = A$ , $\chi(\mathcal{C}*S) = B$ whose index divides $N$ , the sheaf $(\omega_S^{[N]})^{\otimes M}$ is very ample?
(3) Given an s.l.c. surface $S$ with $\omega*{S}$ ample, is Aut $S$ finite?
(4) If $X \to \Delta$ is a one-parameter family of surfaces such that the special fibre $S$ is an s.l.c. surface with $K_S^2 = A$ , $\chi(\mathcal{C}*S) = B$ whose index divides $N$ , and if $\omega*{X/\Delta}^{[N]}$ is invertible, then is the geometric generic fibre also an s.l.c. surface?
Of course,

J. Kollár and N.I. Shepherd-Barron

it would be of interest to know the answer to this without the hypothesis that $\omega_{X / \Delta}^{[N]}$ be invertible, but for our moduli problem this generality would be superfluous.

We shall (Corollary 5.5 and Remark 5.6) answer question (4) affirmatively.
Question (1) seems rather hard, and we leave it completely open.
However, the answer to both (2) and (3) is yes.
The first by [Ko1, 2.1.2] and the second by Iitaka [I], who has shown that a surface of log general type (and so every component of $S$) has finite automorphism group.

Corollary 5.5. Suppose that $X \to \Delta$ is a one-parameter deformation of the (germ of the) normal s.l.c. singularity $(X_0, P)$ and that for some $N &gt; 0$, the sheaf $\omega_{X / \Delta}^{[N]} is invertible.
Then the general fibre $X_t$ has just s.l.c. singularities.

Proof.
One may assume that $X \to \Delta$ admits a semistable resolution.
By Theorem 5.3, either $X$ is cannonical, in which case the general fibre has only RDP'S, or every relative minimal model $X'$ has normal special fibre $X_0'$.
In the first case there is nothing to prove, while in the second we argue as follows.
Let $f \colon X' \to X$ be a minimal model of $X$.
We can write $K_{X'} \sim f^* K_X + \sum a_i E_i$ as $\mathbb{Q}$-divisors, where the exceptional prime divisors $E_i$ are flat over $\Delta$.
So $K_{X_0} \sim f^* K_{X0} + \sum a_i (E_i|*{X_0})$; since $X_0$ has only s.l.c. singularities and $E_i|*{X_0}$ is an effective integral divisor, it follows that $a_i \geq -1$ for all $i$, and so, since $X_1'$ is smooth for $t \neq 0$, we see that $X_t$ has only s.l.c. singularities.

Remark 5.6. If $X_0$ is not normal, then Corollary 5.5 still holds.
For by the classification of ch.4, we may assume that $X_0$ is a degenerate cusp or a $\mathbb{Z}_2$-quotient of one; in the first case the techniques of [S-B1] prove the result, and in the second case one can apply the same approach to the $\mathbb{Z}_2$ cover.
(In outline, the proof depends on analyzing the tangent cone at the origin of $X$ if $X_0$ is not a double point, and by considering the branch locus of a 2:1 projection if $X_0$ is a double point.)

Corollary 5.7. The functor $\mathcal{M}$ is coarsely represented by a separated algebraic space $M$ of finite type.

Proof.
Since questions (2)-(4) have affirmative answers, we can apply the results described in ch. 4 of Popp's book [Po] to prove the result.

Remark 5.8. Of course, if we knew how to bound the index in terms of the Chern numbers, as asked in question (1), then for sufficiently divisible $N$, $M$ would be proper.

Finally, we can sometimes analyze the versal deformation space of a normal s.l.c. singularity, as we did for quotient singularities in ch. 3.

Theorem 5.9. Suppose that $(X, P)$ is a normal s.l.c. singularity whose canonical cover $(Y, Q)$ has a smooth versal deformation space.
Then the irreducible components of $\operatorname{Def}(X)$ are in $1 - 1$ correspondence with the partial resolutions $f \colon Z \to X$ such that $K_Z$ is ample and either

(i) $Z$ has only singularities of class $T$, or (ii) $f$ is an isomorphism and $X$ admits a $\mathbb{Q}$-Gorenstein one-parameter deformation to RDP's.

Threefolds and deformations of surface singularities

Proof.
This is proved in much the same way as Theorem 3.9. The hypothesis that $\operatorname{Def}(Y)$ be smooth is used to ensure that if $X = Y / H$ , then the locus $\operatorname{Fix}(H) \subset \operatorname{Def}(Y)$ is irreducible.

Remark 5.10. If we drop the hypothesis that $\operatorname{Def}(Y)$ be smooth, then the same result holds except that in (ii) we must count one component for each $V$ of $\operatorname{Fix}(H)$ for which the deformation $\mathcal{Y} \to V$ induced from a versal deformation of $Y$ gives, upon taking quotients by $H$ , a deformation of $X$ whose generic fibre has only RDP's.

Example 5.11. Suppose that $X$ is the singularity with dual graph

![img-4.jpeg](img-4.jpeg)

Then $X$ is s.l.c. and its canonical cover $Y$ is the singularity $x^3 + y^3 + z^3 = 0$ on which $H = \langle \sigma \rangle$ acts via $\sigma(x, y, z) = (\omega x, \omega y, \omega^2 z)$ , where $\omega = \exp(2\pi i / 3)$ . Then Def $X$ has five components.
One corresponding to Fix $H \subset \operatorname{Def} Y$ , one (the Artin component) corresponding to the canonical model of $X$ and one for each of the partial resolutions obtained by contracting one of [3, 2, 3] configurations in the diagram above.
To check that these are all is a little tedious, especially as here there is no maximal resolution.

Example 5.12. We give an example to show that our partial compactifications can lead to disconnected components of the moduli space becoming joined together.
To see this, let $Y_0 \subset \mathbb{P}^8$ be the projective cone over an octic elliptic curve in $\mathbb{P}^7$ . Then there are (projective) smoothings $Y \to \varLambda$ and $Y' \to \varLambda$ of $Y_0$ , where for $t \neq 0$ , $Y_t$ and $Y_t'$ are octic Del Pezzo surfaces, isomorphic to $\mathbb{P}^1 \times \mathbb{P}^1$ and the rational ruled surface $\mathbb{F}*1$ , respectively.
Let $X \to \varLambda$ and $X' \to \varLambda$ be the double covers of $Y$ and $Y'$ , respectively, branched in a general quartic hypersurface section, both of which cut out the same smooth curve on $Y_0$ . Then for $t \neq 0$ , both $X_t$ and $X_t'$ have $K^2 = 16$ , $\chi = 10$ , while $K*{X_t}$ is even and $K_{X_t'}$ is not.
Hence $X_t$ and $X_t'$ are not homeomorphic, and so lie on different components of the moduli space; introducing the moduli point of $X_0(\cong X_0')$ connects these two components together.

Notice also that the singularities of $X_0$ are of multiplicity eight, so that $X_0$ is asymptotically unstable [M2].

# $\S 6$ Three dimensional terminal singularities

The aim of this chapter is to settle some questions that were left open in Mori [Mo1]. This will complete the classification of three dimensional terminal singularities.

Most of the work was done earlier by various persons, we now recall their relevant results.

J. Kollár and N.I. Shepherd-Barron

Theorem 6.1. (Reid [Re 3])

(i) A three dimensional terminal Gorenstein singularity is either smooth or an isolated cDV point.
(ii) if $(y, Y)$ is a 3-dimensional terminal singularity then there exists a 3-dimensional terminal Gorenstein singularity $(x, X)$ and an action of some cyclic group $\mathbb{Z}_m$ on $(x, X)$ such that $(y, Y) = (x, X) / \mathbb{Z}_m$.
Moreover the action is free outside $x \in X$.

Convention 6.2. In order to simplify notation we shall use the following system.
If it is understood that $\mathbb{Z}_m$ acts on certain objects, then we fix a primitive $m^{\mathrm{th}}$ root of unity $\varepsilon$, and a generator $\sigma$ of $\mathbb{Z}_m$.
If ? is an eigenvector of the action satisfying $\sigma (?) = \varepsilon^a \cdot ?$ then we say that ? has weight $a$ and write $w (?) = a$.

Theorem 6.3. (Danilov [D], Morrison-Stevens [M-S]) Terminal singularities that are quotients of a smooth point are the following: $\mathbb{C}^3 /\mathbb{Z}_m$ where $\mathbb{Z}_m$ acts with weights $(1,a,m - a)$ on the coordinates and $(a,m) = 1$.

Theorem 6.4. (Mori [Mo1]) Assume that $\mathbb{Z}_m(m &gt; 1)$ acts on a cDV point, freely outside the origin, and the quotient is terminal.
Then one can take a suitable embedding of the cDV point into $\mathbb{C}^4$ and suitable coordinates such that the equation $g$ of the cDV point and the action of the group are given by one of the following cases:

(1) $m$ arbitrary, $g = xy + f(z,u^{m}), w(x) + w(y) = m, w(z) = 0, w(x), w(y)$ and $w(u)$ prime to $m$.
(2) $m = 2, g = x^{2} + y^{2} + f(z,u), f \in m^{4}$, weight of $x, y, z, u$ are 1, 0, 1, 1. (3) $m = 2, g = u^2 + f(x, y, z), f \in m^3, xyz$ or $y^2z$ appears in $f$ with non-zero coefficient, weights of variables are 1, 1, 0, 1. (4) $m = 2, g = u^2 + x^3 + f(y, z) x + h(y, z), h \notin m^5$, weights are 0, 1, 1, 1. (5) $m = 3, g = u^2 + f(x, y, z), f \in m^3$, cubic term of $f$ is $x^3 + y^3 + z^3$, $x^3 + yz^2$ or $x^3 + y^3$, weights are 1, 2, 2, 0. (6) $m = 4, g = x^{2} + y^{2} + f(z,u^{2})$, weights are 1, 3, 2, 1.

(It is understood that $f$ and $h$ are such that $g$ is an eigenvector of $\mathbb{Z}_m$.)

Furthermore, if $f$ (and $h$) are sufficiently generic, then the quotient is terminal.

The aim of this chapter is to complete the classification by proving the following.

Theorem 6.5. Assume that in any of the above situations $f$ (and $h$) are chosen such that $g = 0$ has an isolated singularity at the origin and the action of $\mathbb{Z}_m$ on $g = 0$ is free outside the origin.
Then the quotient is terminal.

Remark 6.6. (i) (1) should be considered as the main series and (2)-(6) as the exceptional ones.
We shall use two different methods to handle these two cases.
Neither of the methods seems to work for the other case.

(ii) We shall give two proofs for (1). The first uses 3.6. The second, communicated to us by Mori, does not use any hard result from three dimensional geometry.

6.7. Proof in case of (1). First proof.
$z$ is invariant under the group action and therefore $(xy + f(0,u^{m}) = 0) / \mathbb{Z}_{m}$ is a hyperplane section of the 3-dimensional quotient singularity.
$xy + f(0,u^{m}) = 0$ is either a n.c. point $(f\equiv 0)$ or a DV point

Threefolds and deformations of surface singularities

$(f \neq 0)$ , and hence the quotient is semi-log-terminal by 4.23. Therefore, 3.6 implies that the 3-dimensional quotient is terminal (the n.c. case is the same).

Second proof (by S. Mori).
Since $\mathbb{Z}_m$ acts freely on $X$ , $z$ does not divide $f(z, u^m)$ . Therefore by Puiseux expansion we can write $f(z, u^m) = \Pi(u^m - h_i(v))$ , where $v^n = z$ for some $n$ . By 3.3 it is sufficient to show that the $\mathbb{Z}_m$ quotient of $xy + \Pi(u^m - h_i(v)) = 0$ is terminal.
If we blow up the ideal $(x, u^m - h_1(v))$ , then we get a small morphism $\pi_1 \colon X_1 \to X$ and easy computation shows that the only singularities of $X_1$ are the $\mathbb{Z}_m$ quotient of $xy + u^m - h_1(v) = 0$ and the $\mathbb{Z}*m$ quotient of $xy + \Pi*{i \geq 2}(u^m - h_i(v)) = 0$ . Repeating this procedure, we get a small morphism $\pi \colon \bar{X} \to Y$ such that the only singularities of $\bar{X}$ are of the form $(xy + u^m - h_i(v) = 0) / \mathbb{Z}_m$ . By a suitable choice of $v_i = v g_i(v)$ , this becomes $(xy + u^m - v_i^s = 0) / \mathbb{Z}*m$ . By 6.4 and 6.8 (v) $\bar{X}$ has terminal singularities.
Since $\pi$ is small $K*{\bar{K}} = \pi^* K_X$ and consequently $X$ is terminal as well.

Facts 6.8. For convenient references here we gather some facts that will be used in the sequel.

(i) For any $f$ consider the family $f(x_{1},\ldots ,x_{n - 1},tx_{n}) = 0$ ; this is a flat family of hypersurfaces.
If $t\neq 0$ then the hypersurface is isomorphic to $f(x_{1},\dots,x_{n}) = 0$ ; if $t = 0$ , to $f(x_{1},\dots,x_{n - 1},0) = 0$ . (ii) If $f(t, x_1, \ldots, x_n)$ is a family of hypersurfaces such that the multiplicity of $f(t, x_1, \ldots, x_n) \subset \mathbb{C}^n$ at the origin is independent of $t$ , then the family $B_0f(t, \underline{x})$ is also flat, where $B_0f(t, \underline{x})$ is the blow-up of $f(t, \underline{x}) \subset \mathbb{C}^n$ at the origin.
(iii) [MT, Re2] Assume the $\sum a_{I}x^{I}$ defines a rational singularity at the origin.
Then the following condition is satisfied: (\*) If $0 \leq v_{1}, \ldots, v_{n}$ are such that for any $I = (i_{1}, \ldots, i_{n})$ , $a_{I} \neq 0 \Rightarrow \sum i_{j} v_{j} \geq 0$ , then we necessarily have $\sum v_{i} &gt; 1$ .

For any given polynomial it is standard linear algebra to check if $(^{*})$ is satisfied or not.
We shall omit such computations.

(iv) [Re2, §4] Assume that $\sum a_{I}x^{I}$ satisfies condition $(^{*})$ . The for generic $\lambda_I\neq 0$ the singularity of $\sum \lambda_I a_I x^I$ is rational at the origin.
(v) For certain polynomials one can always find a change of variables $\bar{x}_i = \mu_i x_i$ such that $\sum \lambda_I a_I x^I = \sum a_I \bar{x}^I$ (e.g. $\sum a_i x_i^{b_i}$ ). We shall call such a polynomial generic.
A generic polynomial defines a rational singularity iff (\*) is satisfied.
It is easy to check whether a polynomial is generic or not, and we shall omit such computations.
(vi) [Hin] Let $\mathbb{Z}_m$ act on $X = (f(x_1, \ldots, x_n) = 0)$ such that the $x_i$ are eigenvectors.
Assume that the action is free in codimension one.
Then $X / \mathbb{Z}_m$ is Gorenstein iff $\sum w(x_i) - w(f) \equiv 0(m)$ .

Proposition 6.9. Let $X \subset \mathbb{C}^4$ be a cDV point and let $B_0X$ be the blow-up of the origin.
Then $B_0X$ has rational singularities only.

Proof.
In a generic coordinate system $X$ is given by $f(x_{1},\ldots ,x_{4})$ and by 6.8 (i) is specializes to $f(x_{1},x_{2},x_{3},0) = 0$ , which is the trivial deformation of a DuVal singularity.
By a suitable change of coordinates we can assume that $f(x_{1},x_{2},x_{3},0)$ is in one of the standard forms as in [Re2, 0.2]. In each case one can write down explicit equations for $B_0f(x_1,x_2,x_3,0)$ , and it is easy to check that all these equations are generic and satisfy (\*) . Therefore $B_0f(x_1,x_2,x_3,0)$ has rational singularities only.

J. Kollár and N.I. Shepherd-Barron

By 6.8 (ii) $B_0X$ is a flat deformation of $B_0f(x_1, x_2, x_3, 0)$.
Hence by [E1] it too has rational singularities.

**Proposition 6.10.** Let $X \subset \mathbb{C}^4$ be an isolated cDV point with a $\mathbb{Z}_m$-action which is free outside the origin.
Let $B_0X$ be the blow-up of the origin and let $E \subset B_0X$ be the exceptional divisor.
Assume that

(i) The induced $\mathbb{Z}_m$-action is faithful on every component of $E$ and (ii) $B_0X / \mathbb{Z}_m$ has canonical singularities only.

Then $X / \mathbb{Z}_m$ is terminal.

**Proof.** Let $Y = X / \mathbb{Z}_m$, $q \colon X \to Y$ the natural map.
Let $B_0Y = B_0X / \mathbb{Z}_m$, $g \colon B_0X \to X$, $h \colon B_0Y \to Y$, $\bar{g} \colon B_0X \to B_0Y$ be the natural maps.
Finally, let $f \colon Y' \to B_0Y$ be a resolution of singularities.

Since $X$ has a double point at the origin, an easy computation gives that $K_{BX} = g^{*}K_{X} + E$.
By (i) the map $\bar{q}\colon BX\to BY$ is étale in codimension one.
Hence $K_{BX} = \bar{q}^{*}K_{BY}$, and similarly $K_{X} = q^{*}K_{Y}$.
This gives that $K_{BY} = h^{*}K_{Y} + F$.
Since $BY$ has canonical singularities $K_{Y^{\prime}} = f^{*}K_{BY} + G$, where $G$ is effective.
Therefore $K_{Y^{\prime}} = f^{*}K_{BY} + G = (h\circ f)^{*}K_{Y} + f^{*}F + G$.

If $D \subset Y'$ is an $h \circ f$ exceptional divisor, then $f(D) \subseteq F$.
Thus $D$ appears in $f^{*}F$ with a positive coefficient.
This shows that $Y$ is terminal.

**Remark 6.11.** For $m = 1$ this gives a simple proof of the terminality of isolated cDV points.

**Proposition 6.12.** Let $X \subset \mathbb{C}^4$ be a cDV singularity with a $\mathbb{Z}_2$-action which is free in codimension one.
Then $X / \mathbb{Z}_2$ is canonical iff it is Gorenstein outside the origin.

**Proof.** The condition is clearly necessary.
To prove sufficiency we employ the notation of 6.10. Let $X = (\phi = 0)$.

First we consider the cases when the condition 6.10 (i) is not satisfied.
This can happen in three cases:

(i) $E$ is reduced, $w(x_{i}) = 1$ for every $i$.
Then $w(\phi) = 0$ thus by 6.8 (vi) $Y$ is Gorenstein, hence canonical.
(ii) $\phi = x_{1}x_{2} + \Psi (x_{3},x_{4}),w(x_{1}) = 0,w(x_{i}) = 1$ for $i &gt; 1$.
Then $w(\phi) = 1$ and again $Y$ is Gorenstein.
(iii) $\phi = x_1^2 + \Psi(x_2, x_3, x_4)$, $w(x_i) = 1$ for $i &gt; 1$, and $w(\phi) = 0$.
If $\Psi$ contains a degree $\leq 2$ term, then we are in one of the above situations.
By weight considerations $\Psi$ cannot contain a cubic term, but then $\phi = 0$ is not a cDV point.

Therefore we may assume for the rest of the proof that the $\mathbb{Z}*2$-action on any component of $E$ is faithful.
Therefore, we obtain that $K*{BY} = h^{*}K_{Y} + F$.

Let $D_{i} \subset Y'$ be the $f$-exceptional divisors, and let $K_{Y'} = f^{*}K_{BY} + \sum a_{i}D_{i}$.
BY has only log-terminal singularities; hence $a_{i} &gt; -1$.
Since $2K_{BY}$ is Cartier, the $a_{i}$ are half-integers.
Therefore $a_{i} \geq -\frac{1}{2}$.
Let $f^{*}F = \sum b_{i}D_{i}$, where $b_{i} &gt; 0$ if $f(D_{i}) \subseteq F$ and $b_{i} = 0$ otherwise.
Furthermore, since $2F$ is Cartier, the $b_{i}$ are half-integers.

$$
K_{Y'} = f^{*}K_{BY} + \sum a_{i}D_{i} = (h\circ f)^{*}K_{Y} + \sum (a_{i} + b_{i})D_{i}.
$$

If $f(D_i) \subseteq F$, then $b_i \geq \frac{1}{2}$, $a_i \geq -\frac{1}{2}$.
Hence $a_i + b_i \geq 0$.
If $f(D_i) \nsubseteq F$, then $b_i = 0$ and $a_i \geq 0$ since by assumption $Y$ is Gorenstein outside the origin.
This proves that $Y$ is canonical.

Threefolds and deformations of surface singularities

6.13 Proof of 6.5 in cases (2)-(6). Let $Y = X / \mathbb{Z}_m$ be one of the cases.
We want to check the conditions of 6.10. Condition (i) is easy to see.
By 6.9 all points of $BX$ are rational.
Therefore all the singularities of $BY$ are rational again.
Therefore the Gorenstein points of $BY$ are canonical and we have to check the non-Gorenstein points only.
These come from points of the $\mathbb{Z}_m$-action on $E$.
These in turn come from fixed lines in $\mathbb{C}^4$.
If this line is the $x_j$ axis, 6.8 (vi) and the computation of the blowing-up yield that the corresponding point in $BY$ is Gorenstein iff $\sum w(x_i) - w(\phi) - w(x_j) \equiv 0$ (m).

Armed with this information, we can consider the cases.

(2) All the points of $BY$ are Gorenstein.
(3) The $z$-axis gives the only non-Gorenstein point.
On $BX$ this gives a cDV point (just compute the blow-up); hence by 6.12 the quotient is canonical.
(4) We have to consider the $x$-axis only.
On $BX$ this gives a smooth point; hence the quotient is canonical (even terminal) by 6.3. (5) Again the $x$-axis is the only fixed line to be checked.
On $BX$ we get a smooth point and again by 6.3 all isolated $\mathbb{Z}_3$ quotients of $\mathbb{C}^3$ are canonical.
(6) The $z$-axis is the only one to be checked (both for $\mathbb{Z}_4$ and $\mathbb{Z}_2$ fixed points).
Here $BX$ is given by the equation $x'^2 + y'^2 + z'^{-2}f(z', z'^2u'^2) = 0$, and the action is given by weights 3, 1, 2, 3, which is the same we started with.
The action of $\mathbb{Z}_4$ on the $z$-axis is not free.
Therefore $f(z,0)\not\equiv 0$.
Thus we can use induction on the smallest $z$-power appearing in $f$.
The starting point is the linear case.
This is the same as $\mathbb{C}^3/\mathbb{Z}_4(1,1,3)$, which is terminal by 6.3. Therefore we are done in this case as well.

This completes the proof of 6.5.

§ 7. Deformation of minimal singularities

The aim of this chapter is to give a simple geometric proof that the deformation of a cyclic quotient singularity is again a cyclic quotient.

The idea of the proof is the following.

7.1. Let $f \colon X \to \Delta$ be a 1-parameter deformation of the singularity $f^{-1}(0)$.
Let $s \colon \Delta \to X$ be a section.
Let $X_t = f^{-1}(t)$ and $x_t = s(t)$.
We say that $(x_t, X_t)$ is a small deformation of $(x_0, X_0)$.
We would like to get some information about the tangent cone of $(x_t, X_t)$ in terms of the tangent cone of $(x_0, X_0)$.
We proceed as follows.

First assume that $X$ is normally flat along $s(\Delta)$.
Then the tangent cone of $(x_t, X_t)$ is a flat deformation of the tangent cone of $(x_0, X_0)$.
This is the good case.

Otherwise, let $X^0 = X$, $s^0 = s$.
If we have $X^i$ and $s^i$, then let $X^{i+1}$ be the blow up of $s^i(0) \in X^i$ and $s^{i+1} \colon \Delta \to X^{i+1}$ the natural map.
Let $F^{i+1}$ be the exceptional divisor of $X^{i+1} \to X^i$.

By Hironaka's resolution theorem there is an $m$ such that $X^m$ is normally flat along $s^m(\Delta)$.
This means that $(x_t, X_t)$ for $t \neq 0$ is a normally flat deformation of $(s^m(0), F^m)$.
If we can control the singularities of $F^m$ in terms of $(x_0, X_0)$, then we get some information about $(x_t, X_t)$.

For the proof the natural context is the class of minimal singularities studied in [Ko1, 3.4]. We recall some of the definitions and results.

J. Kollár and N.I. Shepherd-Barron

Proposition-Definition 7.2. [Ko1, 3.4.1–2.] Let $(x, X)$ be a reduced Cohen-Macaulay singularity.
Then $\mathrm{mult}_x X \geq \mathrm{emdim}_x X - \dim_x X + 1$.
$(x, X)$ is called minimal if equality holds and tangent cone is reduced.

Proposition 7.3. ([Ko1, 3.4], Sally [Sa] and Xambó [X]). Let $(x, X)$ be a minimal singularity.
Then the projectivized tangent cone $F = \cup F_i$ is a subvariety of some $\mathbb{P}^n$ of minimal degree, connected in codimension one.
Its irreducible components $F_i$ satisfy $\deg F_i = \mathrm{emdim} F_i - \dim F_i$ and any two intersect in a linear subspace.
For any $y \in F$ the singularity $(y, F)$ is minimal again.

The above result implies that the deformation of a minimal singularity is minimal.
Here we shall need a more precise result which requires a detailed study of the tangent cones.
The following result describes the irreducible components.

Proposition 7.4. ([Ber, Harr])

(i) A reduced, irreducible, non-degenerate curve $C \subset \mathbb{P}^k$ satisfying $\deg C = k$ is a rational normal curve.
(ii) A reduced, irreducible, non-degenerate surface $F \subset \mathbb{P}^k$ satisfying $\deg F = k - 1$ is one of the following; (a) Veronese in $\mathbb{P}^5$; (b) a cone over a rational normal curve; (c) a ruled surface $\operatorname{Proj}_{\mathbb{P}^1}(\mathcal{O}(a) \otimes \mathcal{O}(b))$ embedded by $\mathcal{O}(1)$ for $a, b \geq 1$.

Definition 7.5. Let $C = \cup C_i \subset \mathbb{P}^n$ be a reduced, connected curve of degree $n$.
We associated to it a labeled graph as follows.
To each curve $C_i$ we associate a vertex and label it $\deg C_i$.
We connect two vertices if the corresponding curves intersect.
We shall call this the graph of the curve and denote it by $G(C)$.

Definition 7.6. Let $(x, X)$ be a minimal surface singularity, and let $C$ be the projectivized tangent cone of $(x, X)$.
Then by 7.3 $C$ satisfies the conditions of 7.5. $G(C)$ will be denoted by $G(x, X)$ and called the graph of $(x, X)$.

Definition 7.7. Assume that $C$ and $C'$ both satisfy the conditions of 7.5. We shall say that $G(C')$ is a simplification of $G(C)$ if it can be obtained from $G(C)$ by repeated application of the following procedures:

(i) Replace $G(C)$ with a connected subgraph, keeping the labeling fixed; or (ii) change the labeling of a vertex to 1; or (iii) if a vertex $v$ is connected with vertices $v_1, \ldots, v_2$ and $v_1$ is labeled 1, then erase $v$ and connect $v_1$ with each of $v_2, \ldots, v_k$; or (iv) if $v_1, \ldots, v_k$ are vertices such that any two of them are connected, then replace $G(C)$ with some $G(C'')$ where $\deg C'' \leq k$.

The reason for this definition is the following.

Lemma 7.8. Let $F = \cup F_i \subset \mathbb{P}^n$ be a reduced surface of degree $n - 1$, connected in codimension one.
Let $\cup C_j = C = F \cap H$ be a hyperplane section of $F$.
Let $x \in F$ be a closed point.
Then $(x, F)$ is a minimal surface singularity and $G(x, F)$ is a simplification of $G(C)$.

Proof.
The first statement is a special case of 7.3. As for the second part, let $X \subseteq F$ be the union of those components that contain $x$.
Then $G(x, G) = G(X, F)$,

Threefolds and deformations of surface singularities

and $G(H \cap X)$ is a connected component of $G(C)$.
Therefore, we may assume that $X = F$.

If $x \in H$, then $\mathrm{mult}_x X \leq \#$ (components of $C$ through $x$); this corresponds to 7.7 (iv).

Otherwise, we have to check the possible configurations of $x$, $F_i$, $F_i \cap H$; using 7.4 it is easy to see that the procedures 7.7 (ii) and (iii) account for all the possibilities.

This in turn implies the following

**Proposition 7.9.** Let $(x_0, X) \supset (x_0, X_0)$ be a 1-parameter deformation.
Let $BX \to X$ be the blow-up of $x_0 \in X$ and let $F \subset BX$ be the exceptional divisor.
If $(x_0, X_0)$ is a minimal singularity then so is $(y, F)$ for any $y$ and $G(y, F)$ is a simplification of $G(x_0, X_0)$.

**Proof.** The statement is trivial if $X$ is smooth.
Otherwise 7.2 easily gives that $\mathrm{mult}*{x_0} X = \mathrm{mult}*{x_0} X_0$.
Let $C$ (resp.
$F$) be the projectivized tangent cone of $(x_0, X_0)$ (resp.
$(x_0, X)$). Then $C$ is a hyperplane section of $F$.
This implies that $F$ is reduced.
Hence $(x_0, X)$ is minimal.
The rest follows from 7.8.

Using the above result the argument given in 7.1 leads at once to the main result of this section:

**Theorem 7.10.** Let $(x_0, X_0)$ be a minimal surface singularity and let $(x_t, X_t)$ be a small deformation.
Then there exists a minimal singularity $(y, F)$ such that $G(y, F)$ is a simplification of $G(x_0, X_0)$ and the tangent cone of $(x_t, X_t)$ is a flat deformation of the tangent cone of $(y, F)$.

In order to use this theorem we should know which surface singularities are minimal and how to compare $G(x, X)$ with more customary invariants.

**Proposition 7.11.** ([Ko1, 3.4.9–10]) A normal surface singularity is minimal iff it is rational and its fundamental cycle is reduced.

**Remark 7.12.** Let $(x, X)$ be a rational surface singularity with minimal resolution $f: Y \to X$.
Let $E_i \subset Y$ be the exceptional curves.
Let $b_i = -E_i^2$ and $a_i = \# \{j \neq i: E_j \cap E_i \neq \emptyset\}$.
The fundamental cycle is reduced iff $b_i \geq a_i$ for every $i$.
By a result of Artin [A 1], in this case $G(x, X)$ can be constructed as follows.

The vertices correspond to the those $i$ such that $b_i &gt; a_i$.
They are labeled $b_i - a_i$.
The vertices corresponding to $E_i$ and $E_j$ are connected iff there is a chain of curves $E_i = E_{k_0}, \ldots, E_{k_m} = E_j$ such that $E_{k_a} \cap E_{k_{a+1}} \neq \emptyset$ and $b_{k_a} - a_{k_a} = 0$ for all $0 &lt; s &lt; m$.

**Definition 7.13.** With notation as in 7.12 we define $\operatorname{end}(X)$ to be the number of those curves $E_i$ that intersect at most one other exceptional curve $E_j$.

**Remark 7.14.** (i) From [Br1] it follows that $(x, X)$ is a cyclic quotient iff $\operatorname{end}(x, X) \leq 2$.

(ii) Using 7.12 we can compute $\operatorname{end}(X)$ from $G(x, X)$ as follows: $\operatorname{end}(X)$ is the number of vertices $V_i$ such that two vertices $V_j$ and $V_k$ are connected with $V_i$ only if $V_j$ and $V_k$ are connected.

(iii) It is quite easy to see from this that if $G(C')$ is a simplification of $G(C)$, then $\operatorname{end} G(C') \leq \operatorname{end} G(C)$.

J. Kollár and N.I. Shepherd-Barron

This easily yields the following:

Corollary 7.15. Let $(x_{t},X_{t})$ be a small deformation of a minimal surface singularity $(x,X)$.
Then $\operatorname{end}(x_t,X_t) \leq \operatorname{end}(x,X)$.
In particular if $(x,X)$ is a cyclic quotient then so is $(x_{t},X_{t})$.

This latter result was conjectured by Riemenschneider.
It should be compared with the result of [EV].

Remark 7.16. Let $(x_0, X_0)$ be a quotient singularity.
From 7.12 it is clear that the tangent cone carries no information about the $-2$ curves of the minimal resolution.
Therefore the above results do not give complete information about the possible deformations of $(x_0, X_0)$.

(ii) Most of the non-cyclic quotient singularities are minimal; they have three ends.
Our results however do not imply that their deformations are again quotient singularities.

# References

[A1] Artin, M.: On isolated rational singularities of surfaces.
Am.
J. Math.
88, 129–136 (1966) [A2] Artin, M.: Algebraic construction of Brieskorn’s resolutions.
J. Algebra 29, 330–348 (1974) [Ben] Benveniste, X.: Sur l’anneau canonique de certaines variétés de dimension trois.
Invent.
Math.
73, 157–164 (1983) [Ber] Bertini, E.: Introduzione alla geometria proiettiva degli iperspazi.
Messina 1923 [Br1] Brieskorn, E.: Rationale Singularitäten komplexer Flächen, Invent.
Math.
4, 336–358 (1968) [Br2] Brieskorn, E.: Singular elements in semi-simple algebraic groups.
Proc.
Int.
Con.
Math., Nice, 2, 279–284 (1971) [D] Danilov, V.I.: Birational geometry of toric 3-folds, Math.
USSR Izv.
21, 269–279 (1983) [E1] Elkik, R.: Singularités rationelles et déformations, Invent.
Math.
47, 139–147 (1978) [EV] Esnault, H., Viehweg, E.: Two-dimensional quotient singularities deform to quotient singularities.
Math.
Ann.
271, 439–449 (1985) [GR] Grauert, H., Riemenschneider, O.: Verschwindungssätze für analytische Kohomolgiegruppen auf komplexen Räumen.
Invent.
Math.
11, 263–292 (1970) [Harr] Harris, J.: A bound on the geometric genus of projective varieties.
Ann.
Scu.
Norm.
Pisa 8, 35–68 (1981) [Hart] Hartshorne, R.: Complete intersections and connectedness.
Am.
J. Math.
84, 497–508 (1962) [Hin] Hinic, V.A.: On the Gorenstein property of a ring of invariants.
Izv.
Akad.
Nauk SSSR 40, 50–56 (1976) (= Math USSR. Izv 10, 47–53 (1976)) [I] Iitaka, S.: Birational geometry for open varieties.
Sém.
Math.
Sup., Montreal, 76 (1981) [Kar1] Karras, U.: Deformations of cusp singularities.
Proc.
Symp.
Pure Math.
30, 37–44 (1970) [Kar2] Karras, U.: Weak simultaneous resolution (to appear) [Kaw1] Kawamata, Y.: On singularities in the classification theory of algebraic varieties.
Math.
Ann.
251, 51–55 (1980) [Kaw2] Kawamata, Y.: Crepant blowings-up of three-dimensional canonical singularities and its application to degenerations of surfaces.
Ann.
Math.
(to appear) [Kaw3] Kawamata, Y.: On the finiteness of generators of a pluricanonical ring for a 3-fold of general type.
Am.
J. Math.
106, 1503–1512 (1984) [KMM] Kawamata, Y., Matsuda, K., Matsuki, K.: Introduction to the minimal model problem.
In: T. Oda (ed.)
Alg.
Geom.
Sendai Adv.
Stud.
Pure Math.
10 (1987) Kinokuniya-North-Holland, pp. 283–360

Threefolds and deformations of surface singularities

[KKMS] Kempf, G., Knudsen, F., Mumford, D., Saint Donat, B.: Toroidal Embeddings I (Lect.
Notes Math., vol. 339), Berlin Heidelberg New York: Springer 1973 [Ko1] Kollár, J.: Toward moduli of singular varieties.
Comp.
Math.
56, 369-398 (1985) [Ko2] Kollár, J.: Deformations of related singularities (Preprint) [Ko3] Kollár, J.: The structure of algebraic threefolds, Bull.
AMS 17, 211-273 (1987) [La] Laufer, H.A.: Weak simultaneous resolution of surface singularities.
Proc.
Symp.
Pure.
Math.
40, part 2, 1-29 (1983) [LW] Looijenga, E., Wahl, J.: Quadratic functions and smoothing surface singularities.
Topology 25, 261-297 (1986) [MM] Matsusaka, T., Mumford, D.: Two fundamental theorems on deformations of polarized varieties.
Am.
J. Math.
86, 668-684 (1964) [MT] Merle, M., Teissier, B.: Conditions d'adjonction, d'après DuVal (Lect.
Notes Math., vol 777) Berlin Heidelberg New York: Springer 1980 [Mo1] Mori, S.: On three dimensional terminal singularities.
Nagoya Math.
J. 98, 43-66 (1985) [Mo2] Mori, S.: Minimal models for semi-stable degenerations of surfaces (unpublished) [Mo3] Mori, S.: Flip conjecture and the existence of minimal models for 3-folds.
J. Am.
Math.
Soc.
(to appear) [MS] Morrison, D., Stevens, G.: Terminal quotient singularities in dimensions three and four.
Proc.
Am.
Math.
Soc.
90, 15-20 (1984) [M1] Mumford, D.: The topology of normal singularities of an algebraic surface and a criterion or simplicity.
Pub.
Math.
IHES 9, 5-22 (1961) [M2] Mumford, D.: The stability of projective varieties, L'Ens.
Math.
23, 39-110 (1977) [Na] Nakayama, N.: Invariance of plurigenera under deformation.
Topology 25, 237-251 (1986) [Ne] Neumann, W.: A calculus for plumbing and the topology of links.
Trans.
Am.
Math.
Soc.
268, 299-344 (1981) [Pi1] Pinkham, H.: Deformations of algebraic varieties with $G_{m}$ -action.
Astérisque 20, (1974) [Pi2] Pinkham, H.: Simple elliptic singularities.
Proc.
Symp.
Pure.
Math.
30, 69-71 (1977) [Po] Popp, H.: Moduli theory and classification theory for algebraic varieties (Lect.
Notes Math., vol 620) Berlin Heidelberg New York: Springer 1977 [Re1] Reid, M.: Elliptic Gorenstein singularities of surfaces.
(preprint, 1976) [Re2] Reid, M.: Canonical threefolds, Journées de Géométrie algébrique d'Angers.
Sijthoff and Nordhoff (1980), pp. 273-310 [Re3] Reid, M.: Minimal models of canonical threefolds, Algebraic and Analytic Varieties.
Adv.
Stud.
Pure Math.
1, 131-180 (1983) [Ri] Riemenschneider, O.: Deformation von Quotientsingularitäten (nach zyklischen Gruppen).
Math.
Ann.
209, 211-248 (1974) [Sai] Saito, K.: Einfach-elliptische Singularitäten.
Invent.
Math.
23, 284-375 (1974) [Sak] Sakai, F.: Weil divisors on normal surfaces.
Duke Math.
J. 512, 877-888 (1984) [Sal] Sally, J.: On the associated graded ring of a Cohen-Macaulay ring.
J. Math.
Kyoto Univ. 17, 19-21 (1977) [S-B1] Shepherd-Barron, N.: Some questions on singularities in two and three dimensions, Thesis, Warwick Univ., 1981 (unpublished) [S-B2] Shepherd-Barron, N.: Degenerations with numerically effective canonical divisor, The Birational Geometry of Degenerations, Progr.
Math.
29, 33-84 (1983) [Sh] Shokurov, V.V.: Letter to M. Reid [vS] Straten, D. van: Weakly normal surface singularities and their improvements, Thesis, Leiden, 1987 [Te] Teissier, B.: Résolution simultanée I, II (Lect.
Notes Math., vol. 777, pp. 71-146) Berlin Heidelberg New York: Springer 1980 [Tr] Traverso, C.: Seminormality and the Picard group.
Ann.
Scu.
Norm.
Pisa 75, 585-595 (1970) [Ts] Tsunoda, S.: Minimal models for semi-stable degenerations of surfaces (Preprint) [TsM] Tsunoda, S., Miyanishi, M.: The structure of open algebraic surfaces II, Classification of algebraic and analytic manifolds.
Progr.
Math.
39, (1983) [V] Vaquie M.: Résolution simultanée de surfaces normales.
Ann.
Inst.
Fourier 35, 1-38 (1985) [Wa1] Wahl, J.: Equisingular deformations of normal surfaces singularities.
Ann.
Math.
104, 325-356

J. Kollár and N.I. Shepherd-Barron

[Wa2] Wahl, J.: Elliptic deformations of minimally elliptic singularities.
Math.
Ann.
253, 241–262 (1980) [Wa3] Wahl, J.: Smoothing of normal surface singularities.
Topology 20, 219–246 (1981) [X] Xambò, S.: On projective varieties of minimal degree.
Collectanea Math.
32, 149–163 (1981) [Z] Zariski, O.: The problem of Riemann-Roch for high multiples of an effective divisor.
Ann.
Math.
76, 560–615 (1962)

Oblatum 15-V-1987
