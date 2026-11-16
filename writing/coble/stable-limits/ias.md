# Integral affine structures {#sec-ias-degenerations}

::: {.definition #def:singular_ias}

The dual complex $\Gamma(\mcx_0)$ of a Type III Kulikov model has a canonical *singular integral affine structure*: away from a finite singular set its charts map to $\RR^2$ with transition functions in $\operatorname{GL}_2(\bZ) \ltimes \RR^2$, and its singularities correspond to the components of positive charge, the non-toric anticanonical pairs.
The total charge is $24$, which constrains the number and type of singularities; for instance one may have $24$ singularities of type $I_1$.
:::

::: {.definition #def:symington_polytope}

Given a monodromy invariant $\lambda$ with barycentric coordinates $\ell_i = \lambda \cdot \alpha_i$, the *Symington polytope* $P(\lambda)$ is the integral affine polygon determined by these coordinates [@Sym02].
Gluing two copies along their boundary,
$$
B(\lambda) = P(\lambda) \union P(\lambda)^{\opop},
$$
produces the integral affine sphere realizing the dual complex $\Gamma(\mcx_0)$; the equator along which the two copies are glued supports the integral affine polarization $R_{\mathrm{IA}}$ [@AE23].
:::

::: {#fig-moduli-degeneration .figure}
\input{tikz/moduli_space_degeneration.tikz}

A one-parameter family $\mcx \to C$ of surfaces over a curve $C \iscontainedin \mcm$ in the moduli space, with fibers $\mcx_0$ and $\mcx_t$ over interior points and the limit $\mcx_\infty$ over the boundary point $\infty$.
:::

::: {#fig-typeiikdg .figure}
\input{tikz/type_ii_kulikov_degeneration.tikz}

A Type II Kulikov degeneration.
:::

::: {#fig-triangulated-sphere-fan .figure}
\input{tikz/triangulated_sphere_fan.tikz}

A triangulated integral affine sphere.
:::

::: {#fig-ias-sterk3-kulikov-model .figure}
\begin{tikzpicture}[scale=1.4]
\pic {object=ias/sterk3-kulikov};
\end{tikzpicture}

A combinatorial Kulikov model whose dual complex is $B_3(\ell)$ at Sterk cusp $3$, $\ell = (2, 0^{15}, 2, 4, 6, 4, 0, 4)$ [@AEGS25, Ex. 4.13, Fig. 13].
:::

## The integral affine structure $B_3(\ell)$ at Sterk cusp 3

::: {#fig-sterk3-ias .figure}
\begin{tikzpicture}
\pic {object=ias/sterk3-ias};
\end{tikzpicture}

The integral affine structure $B_3(\ell)$ at Sterk cusp $3$, $\ell = (2, 0^{15}, 2, 4, 6, 4, 0, 4)$ [@AEGS25, Ex. 4.13, Fig. 13], drawn in the plane: five integral affine singularities are marked with their charges, solid segments are the edges of the triangulation of the shaded region, and dashed segments are the lattice lines outside it.
:::

::: {#fig-ias2-disc-slice .figure}
\input{tikz/fig_ias2_construction.tex}

The integral affine disc $P(\lambda)$, one hemisphere of the sphere $B(\lambda)$, with the outward rays at its boundary points.
:::

::: {#fig-ias2-disc .figure}
\input{tikz/fig_ias2_disc.tex}

The integral affine disc $\bD^2$.
:::

::: {#fig-geometric-degeneration .figure}
\input{tikz/fig_geometric_degeneration.tex}

A triangulated integral affine polytope with its charge distribution, in the directions $(2,2)$ and $(3,-3)$.
:::

::: {#fig-symington-16gon .figure}
\input{tikz/ias_eta3_polygon.tex}

The same polytope after Symington surgeries, marked in red along the boundary.
:::

::: {#fig-16gon-full .figure}
\begin{tikzpicture}[scale=0.8]
\pic[root labels=ell, parity marks=false] {object=coxeter/vinberg-18-2-0};
\end{tikzpicture}

The $16$-gon with its boundary lines $\ell_1, \ell_{16}, \dots, \ell_{21}$ labelled.
:::

## Symmetric parameters at the five Sterk cusps

The following diagrams record parameter assignments on the integral affine
polygons associated with the five Sterk cusps. The labels $\ell_i'$ identify
orbits of the indicated symmetry on the marked vertices. They are parameter
counts before any closure or realizability condition.

\input{tikz/fig_ias_v3_common.tex}

::: {#fig-ias-v3-st-1 .figure}
\input{tikz/fig_ias_v3_sterk_1.tex}

The rotational assignment for $(18,2,0)_1$: eight boundary orbits and two
interior orbits give ten labels. Central symmetry makes the vector closure
sum vanish.
:::

::: {#fig-ias-v3-st-2 .figure}
\input{tikz/fig_ias_v3_sterk_2.tex}

The horizontal assignment for $(18,0,0)_1$ has ten labels. In the archival
construction an additional vector $w$ from the Heegner move closes the
polygon; its admissible choices require a separate check.
:::

::: {#fig-ias-v3-st-3 .figure}
\input{tikz/fig_ias_v3_sterk_3.tex}

The diagonal assignment for $(18,2,0)_1$ has twelve labels. Its closure
conditions and the dimension of the resulting family remain to be
determined.
:::

::: {#fig-ias-v3-st-4 .figure}
\input{tikz/fig_ias_v3_sterk_4.tex}

The horizontal assignment for $(18,2,0)_1$ has eleven orbits: nine on the
outer cycle and two in the interior. Requiring the half-polygon's vector
sum to lie on the symmetry axis imposes one linear condition, giving a
ten-dimensional space of formal length assignments. The alternating
edge weights and geometric realization still require verification.
:::

::: {#fig-ias-v3-st-5 .figure}
\input{tikz/fig_ias_v3_sterk_5.tex}

A candidate twelve-label assignment for cusp $5$. The archival drawing
highlights the even-numbered outer vertices and labels the odd-numbered
ones, while its proposed involution places the odd-numbered root vectors
in the negative eigenspace. The diagram therefore does not yet establish
the asserted eigenspace construction.
:::

::: {.question #qst:ias-sterk-symmetry-realization title="Realizing the symmetric IAS assignments"}
Which closure and integrality conditions turn these formal assignments
into integral affine spheres with an Enriques involution? For cusp $5$,
which marked vertices survive in the positive eigenspace of the ambient
lattice involution?
:::

::: {.question #qst:ias-model-correspondence title="Recovering equivariant Kulikov models"}
Given a Vinberg chamber at an Enriques zero-cusp and an invariant
monodromy vector, which additional affine, triangulation, and gluing data
recover its Type III Kulikov models with both commuting involutions?
Conversely, how does a chosen equivariant Kulikov model determine the
chamber data? The constructions in @sec-type-iii-ias give the local
dictionary; the gluing periods and changes of model must also be tracked.
:::

## Mirror lattices and the Enriques half-twist {#sec-mirror-lattices-half-twist}

::: {.definition #def:admissible-mirror-cusp title="An admissible isotropic vector"}
Let $M\hookrightarrow\lkt$ be a primitive hyperbolic lattice and put
$N=M^\perp$. A primitive isotropic vector $f\in N$ is *$m$-admissible*
if $\operatorname{div}_N(f)=m$ and there is a primitive isotropic
$g\in N$ with $(f,g)=m$ and $\operatorname{div}_N(g)=m$
[@Dol96, §5, Definition preceding Lemma 5.4].
:::

::: {.proposition #prop:mirror-lattice-splitting title="The mirror lattice at an admissible cusp"}
For an $m$-admissible pair $f,g$,
$$
N=\langle f,g\rangle\oplus\check M
\cong U(m)\oplus\check M,
\qquad
\check M\cong f^\perp_N/\ZZ f.
$$
If $M$ has rank $r$, then $\check M$ has signature $(1,19-r)$ and
rank $20-r$.
:::

::: {.proof}
For $x\in N$, divisibility makes both $(x,g)/m$ and $(x,f)/m$ integers,
and
$$
x-\frac{(x,g)}m f-\frac{(x,f)}m g
\in\langle f,g\rangle^\perp.
$$
Thus $\langle f,g\rangle$ splits off integrally. In this decomposition,
$f^\perp_N=\ZZ f\oplus\check M$. Subtracting signatures from
$\operatorname{sig}(\lkt)=(3,19)$ gives the stated signature and rank
[@Dol96, Lemma 5.4 and §6].
:::

After fixing this embedding and a positive chamber, Dolgachev's mirror
moduli space is the moduli of $\check M$-polarized K3 surfaces
[@Dol96, §6]. The summand is the scaled hyperbolic plane $U(m)$,
not an orthogonal sum of $m$ hyperbolic planes. The choice of cusp and
embedding belongs to the mirror construction; the rank relation alone
does not determine a mirror family.

For K3 surfaces with a nonsymplectic involution, the equivariant
Lagrangian torus fibrations of [@AE22, Theorem 7.4] use a mirror invariant
lattice
$$
\widehat S=(r,a,\delta)
=\bigl(10+k-(g-1),\ 10-k-(g-1),\ \delta\bigr)
$$
and an ample rational class $L\in\widehat S_\QQ$. Their base is the
double of a Symington polygon $P$ for an anticanonical quotient pair,
with symplectic class $[L]$. For the Halphen and Enriques cases
$\widehat S=(10,10,1)$ and $(10,10,0)$, respectively, the equator is a
smooth integral affine circle and each hemisphere has twelve $I_1$
singularities. In the Halphen case the boundary identification is the
identity. In the Enriques case it is a half-twist; the resulting
involution is free and its quotient base is $\mathbb{RP}^2$.

The half-twist has an algebraic counterpart. Let $Y$ be an index-two
Halphen surface with multiple fiber $2D$, and put
$a=\OO_D(D)\in\Pic^0(D)[2]$. This is nontrivial. Glue two copies of
$Y$ along $D$ by translation by $a$. Exchanging the two components then
acts on their common elliptic curve by the fixed-point-free translation
$t_a$. The normal bundles satisfy
$$
\OO_D(D)\otimes t_a^*\OO_D(D)\cong\OO_D,
$$
so the glued surface is $d$-semistable. In the smoothing construction
of [@AE22, Lemma 7.1], the invariant numerical lattice before imposing
the period is $E_8(2)\oplus\langle v,d\rangle$, with
$v^2=-2$, $d^2=0$, $(v,d)=1$. The period sends both $v$ and $d$ to $a$,
so its kernel on this summand is
$$
\langle v+d,2d\rangle\cong U(2).
$$
The invariant Picard lattice of a generic smoothing is therefore
$E_8(2)\oplus U(2)$, and the free involution extends to that smoothing.
On the integral affine base, an even equatorial lattice length permits
the half-twist to preserve the marking; replacing $L$ by $2L$ achieves
this condition [@AE22, §8E].

::: {.question #qst:mirror-comparisons title="Comparing mirror constructions"}
How does the lattice-polarized K3 mirror construction above compare with
SYZ dual torus fibrations, homological mirror symmetry, Batyrev's toric
hypersurface construction, and Landau–Ginzburg mirrors? In explicit toric
examples, beginning with $\PP^2$, what is the mirror space and what
superpotential or categorical equivalence forms part of the answer?
:::

## Marked-root structures for the Coble locus

::: {.question #qst:equivariant_triangulation}

Let $r$ be a root of the K3 lattice, and let the period lie on the Heegner divisor $r^{\perp}$, so that the monodromy invariant satisfies
$$
\lambda \cdot r = 0.
$$
Does there exist an equivariant triangulation of the integral affine sphere $B(\lambda)$ compatible with the marked root $r$?
:::
