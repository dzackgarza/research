# Integral affine structures

::: {.remark}

Following [@AEGS25], a **Kulikov model** is a $K$-trivial semistable model
$\cX \to (C, 0)$ of a degeneration of K3 surfaces over a pointed curve $C$.
For each such degeneration, one can define the dual complex of the central
fiber $\Gamma(\cX_0)$.
For Type II degenerations of K3 surfaces the dual complex is an interval
$\bD^1$, and for Type III it is an integral affine $S^2$ with singularities of
total charge $24$.
The additional data of an integral affine polarization
$R_{\mathrm{IA}} \subset \Gamma(\cX_0)$ describes the KSBA stable limit of a
degeneration $(\cX^*, \varepsilon \cR^*)$.
The geometry of such a degeneration is depicted in \cref{fig:moduli-degeneration}:
the family $\cX$ is fibred over a curve $C$ in the moduli space $\cM$, and the
stable limit is the fiber over the point where $C$ meets the boundary.
For Enriques (and hence Coble) surfaces, we take the corresponding dlt models
$\cZ \da \cX/\iota_{\En}$ and half-divisor models
$(\cZ, \cR_{\cZ}) \da (\cX, \cR)/\iota_{\En}$ where $\cX \to (C, 0)$ and
$(\cX, \cR)$ are Kulikov and divisor models of their K3 covers.
:::

::: {.definition ref="def:singular_ias"}

The dual complex $\Gamma(\cX_0)$ of a Type III Kulikov model carries a canonical
*singular integral affine structure*: away from a finite singular set its charts
map to $\RR^2$ with transition functions in $\operatorname{GL}_2(\bZ) \ltimes \RR^2$,
and its singularities correspond to the components of positive charge, the
non-toric anticanonical pairs.
The total charge is $24$, which constrains the number and type of singularities;
for instance one may have $24$ singularities of type $I_1$.
:::

::: {.definition ref="def:symington_polytope"}

Given a monodromy invariant $\lambda$ with barycentric coordinates
$\ell_i = \lambda \cdot \alpha_i$, the *Symington polytope* $P(\lambda)$ is the
integral affine polygon determined by these coordinates [@Sym02].
Gluing two copies along their boundary,
$$
B(\lambda) = P(\lambda) \cup P(\lambda)^{\mathrm{op}},
$$
produces the integral affine sphere realizing the dual complex $\Gamma(\cX_0)$; the
equator along which the two copies are glued supports the integral affine
polarization $R_{\mathrm{IA}}$ [@AE23].
:::

![A one-parameter family $\cX \to C$ of surfaces over a curve $C \subseteq \cM$ in the moduli space, with fibers $\cX_0$ and $\cX_t$ over interior points and the limit $\cX_\infty$ over the boundary point $\infty$.](rendered/moduli_space_degeneration.svg){#fig:moduli-degeneration width=48%}

::: {.remark}

The following is a representation of a Type II degeneration -- it is a chain of
surfaces whose dual complex is an interval $\bD^1$, where the ends $V_1$ and
$V_n$ are rational and the remaining $V_i$ are isomorphic to $E\times \PP^1$
for a fixed elliptic curve $E$.
The intersections $V_i \intersect V_{i+1}$ are double curves isomorphic to $E$.

![A Type II Kulikov degeneration.](rendered/type_ii_kulikov_degeneration.svg){#fig:typeiikdg}

A Type III degeneration can be represented by a triangulation of $S^2$ with
singularities, depicted as follows:

![A triangulated integral affine sphere.](rendered/triangulated_sphere_fan.svg){#fig:triangulated-sphere-fan}
:::

::: {.remark}

The following is a combinatorial representation of a Kulikov model for Sterk 2.

![A combinatorial Kulikov model for Sterk 2.](rendered/ias_sterk2_kulikov_model.svg){#fig:ias-sterk2-kulikov-model}
:::

## The Sterk 2 integral affine structure

\todo[inline]{The figures below were drawn for this construction but their accompanying text has not been written; they are collected here so that the artwork is not orphaned. Each caption states only what the picture shows.}

![An integral affine structure for Sterk 2 drawn in the plane: five integral affine singularities are marked $\times$, solid segments carry the triangulation and dashed segments the boundary of the region.](rendered/sterk2_ias_singularities.svg){#fig:sterk2-ias width=52%}

![The disc slice $B(\lambda)$ of the inverted cone, with the outward rays at its boundary points.](rendered/fig_ias2_construction.svg){#fig:ias2-disc-slice width=58%}

![The integral affine disc $\bD^2$.](rendered/fig_ias2_disc.svg){#fig:ias2-disc width=28%}

![A triangulated integral affine polytope with its charge distribution, in the directions $(2,2)$ and $(3,-3)$.](rendered/fig_geometric_degeneration.svg){#fig:geometric-degeneration width=52%}

![The same polytope after Symington surgeries, marked in red along the boundary.](rendered/fig_symington_16gon.svg){#fig:symington-16gon width=52%}

![The $16$-gon with its boundary lines $\ell_1, \ell_{16}, \dots, \ell_{21}$ labelled.](rendered/fig_16gon_full.svg){#fig:16gon-full width=42%}

::: {.remark}

We leverage the theory of [@AEGS25; @AE22; @AE23; @AET23; @ABE22].
:::

## Marked-root structures for the Coble locus

::: {.remark}

For Enriques and Coble surfaces the integral affine data is built on the K3 cover
first and only then folded downstairs.
One starts from the K3 monodromy (Coxeter) data behind the integral affine sphere,
imposes the Coble condition by marking a root $r$ of zero length,
$$
\lambda \cdot r = 0,
$$
and only afterwards passes to the folded Enriques data and the Coble hyperplane.
The marked root records the vanishing cycle producing the node on the K3 cover; it
is what distinguishes the Coble integral affine structure from an ordinary Enriques
boundary structure.
:::

::: {.question ref="que:equivariant_triangulation"}

Does there exist an equivariant triangulation of the integral affine sphere
compatible with the marked root $r$?
Absent such a triangulation, the marked-root prescription remains a construction
principle rather than a finished combinatorial model.
:::

::: {.remark}

Under the cusp correspondence, the Coble $0$-cusp corresponds to Sterk cusp $2$,
realized as the folding of the cusp $(18,0,0)_1$ by the horizontal symmetry of its
Coxeter diagram [@AEGS25].
The associated integral affine and Kulikov models are therefore of *disc* type,
matching the folding involution of Sterk $2$; the Coble boundary is expected to
produce disc-type integral affine structures rather than sphere- or
$\mathbf{RP}^2$-type limits, in agreement with the flowerpot degenerations of
Morrison [@Mor81; @AEGS25].
The combinatorial disc-type model of \cref{fig:ias-sterk2-kulikov-model} and the
integral affine structure for Sterk $2$ of \cref{fig:sterk2-ias} illustrate this
case.
:::
