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

## Marked-root structures for the Coble locus

::: {.question #qst:equivariant_triangulation}

Let $r$ be a root of the K3 lattice, and let the period lie on the Heegner divisor $r^{\perp}$, so that the monodromy invariant satisfies
$$
\lambda \cdot r = 0.
$$
Does there exist an equivariant triangulation of the integral affine sphere $B(\lambda)$ compatible with the marked root $r$?
:::
