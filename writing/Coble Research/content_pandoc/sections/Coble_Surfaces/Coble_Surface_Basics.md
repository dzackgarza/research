# Basics of Coble surfaces

:::{.remark}

Following [@DM19 §5.1], a **Coble surface** is a smooth projective rational
surface with $\abs{-K_S} = \emptyset$ but $\abs{-2K_S} \neq \emptyset$.
Such surfaces were first studied in [@Cob19], [@Oda85], and were ultimately
classified in [@DZ99].
We say $S$ is **terminal of K3 type** if $\abs{-2K_S}$ contains a smooth[^1]
divisor $C = C_1 + \cdots + C_{n}$, the disjoint union of $n$ reduced smooth
rational curves $C_i$ satisfying $C_i^2 = -4$[^2], and thus
$C_i C_j = -4\delta_{ij}$.
The $C_i$ are referred to as the _boundary components_ of $S$.
One can show $n = -K_S^2$ and $n\leq 10$.
:::

:::{.remark}

Such a Coble surface $S$ can be shown to be a _basic rational surface_, i.e. it
admits a birational morphism to $\pi: S\to \PP^2$ which decomposes as blowups of
$N$ points.[^3] The number of points $N$ depends on $n$; more precisely, one can
show $N = 9+n$.
The image of $C$ is a divisor in $\abs{-2K_{\PP^2}} = \abs{\OO_{\PP^2}(6)}$ and
is thus always a sextic curve.
We primarily restrict to the case $n=1$, whence $K_S^2=-1$ and $S$ is obtained
as the blowup of a special set of ten points in
$\ts{p_1,\cdots, p_{10}} \subset \PP^2$.

In this case, $\tilde C \da \pi(C)$ is an irreducible rational sextic plane
curve, and the ten points $p_i$ are precisely its 10 $A_1$ singularities, some
of which may be infinitely near.
This is the classical example studied in [@Cob19] and [@Oda85] -- the blowup $S$
of $\PP^2$ at the ten $A_1$ singularities of an irreducible plane sextic curve
with at worst $A_1$ singularities, corresponding to the $n=1, N=10$ case above.
[@Cob19] shows, among other things, that there are finitely many
$\Aut(S)$-orbits of smooth rational curves of negative self-intersection.

Note that conversely, starting with such a plane sextic $\tilde C$, one can show
that the proper transform $C$ of $\tilde C$ is in $\abs{-2K_S}$.
Blowing up the singularities of $C$ yields a Coble surface with _smooth_
anti-bicanonical divisor; such Coble surfaces are not the image of any
birational but not biregular morphism from another Coble surface and are said to
be **terminal**.
We say $S$ is **minimal** if the blowdown of any $(-1)$-curve on $S$ is no
longer a Coble surface, or equivalently if $S$ does not admit a birational but
not biregular morphism onto another Coble surface.
:::

:::{.remark}

Following [@CDL24 §1.4], a point set
$\mathcal{P}=\ts{p_{1}, \ldots, p_{n}}$ of $\PP^{2}$ is called
**Cremona special** if $n \geq 9$ and if the surface $S$ obtained by blowing up
$\mathcal{P}$ is such that $\Aut^*(S)$, the image of $\Aut(S)$ in
$\Orth(\Pic(S))$, has finite index in the infinite Weyl group $W_{S}$.
The surface $S$ is then also called Cremona special.
This condition of finiteness roughly expresses that $\Aut^*(X)$ is as large as
possible.
A point set is called _unnodal_ if its blowup does not contain any
$(-2)$-curves.
In [@CDL24], it is proved that a Cremona special complex rational surface is
either an unnodal Halphen surface (with $n=9$) or an unnodal Coble surface (with
$n=10$), that unnodal point sets define a Zariski open subset in the moduli
space of point sets defining Halphen and Coble surfaces, and that Cremona
special Halphen and Coble surfaces are precisely the unnodal ones.
:::

[^1]: More generally, by [@DK24], this can be relaxed to a reduced simple normal crossings divisor.

[^2]: This follows from an application of the genus formula: $$p_{a}(C)=1+\frac{1}{2}\qty{ C^{2} + C \cdot K_S }=1+K_S^{2}=0,$$

```
and so $C$ is a smooth rational curve satisfying $C^2 = 4K_S^2 = -4$ since
$K_S^2 = -1$.
This is [@CDL24 §. 3.1].
```

[^3]: By the proof of [@DK24 Prop 9.13].

