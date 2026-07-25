# Kulikov models and limiting mixed Hodge structures

::: {.remark}

We collect the local structure theory attached to a one-parameter degeneration
of K3 surfaces: the Kulikov models that provide a well-behaved semistable
representative of a degeneration, the trichotomy of such models by the
nilpotency of the log monodromy operator, and the limiting mixed Hodge
structure whose monodromy weight filtration records the same trichotomy on the
Baily--Borel boundary.
:::

## Kulikov degenerations

::: {.definition ref="def:kulikov-model" title="Kulikov models"}

A *Kulikov model* is a degeneration $\cX \to \Delta$ of K3 surfaces where:

1.  The total space $\cX$ is regular (smooth as a threefold).

2.  The central fiber $\cX_0$ is a reduced simple normal crossings (snc)
    divisor.

3.  The relative dualizing sheaf is trivial: $\omega_{\cX/\Delta} \cong \OO_{\cX}$.

Such a model is *semistable* by conditions (1) and (2) and *$K$-trivial* by condition (3).
:::

::: {.remark title="Existence and attribution"}

The Kulikov model is the semistable, $K$-trivial representative constructed for
degenerations of K3 (and Enriques) surfaces in [@Kul77], with the
$K$-trivialization of the semistable reduction supplied for surfaces of trivial
canonical bundle by [@PP81].
:::

::: {.definition ref="def:kulikov-types" title="Type I, II, III Kulikov degenerations"}

Let $T$ be the unipotent Picard--Lefschetz monodromy of a Kulikov model and let
$N = \log T$ be the associated *log monodromy* operator, a nilpotent
endomorphism.
Depending on the nilpotency index of $N$, Kulikov models are classified into
three types:

- **Type $\latI$** ($N = 0$): $\cX_0$ is a smooth K3 surface.

- **Type $\latII$** ($N^2 = 0$, $N \neq 0$): $\cX_0$ is a chain of surfaces
  glued along elliptic curves.
  The dual complex is an interval $\mathbf{IAD}^1$.

- **Type $\mathrm{III}$** ($N^3 = 0$, $N^2 \neq 0$): $\cX_0$ is a union of
  rational surfaces glued along rational curves, forming an anticanonical cycle
  on each component.
  The dual complex is a sphere $\mathrm{IAS}^2$.
:::

::: {.remark title="The Type III dual complex"}

The identification of the Type $\mathrm{III}$ central fiber as a union of
rational surfaces whose dual complex triangulates a sphere is the subject of
[@FS86].
:::

## The monodromy weight filtration

::: {.remark title="The weight filtration by type"}

The **weight filtration** $W_\bullet$ on $H^2(\cX_t; \CC)$ (weight $2$, centered
at $n = 2$) reflects the three types, by the nilpotency of $N$.
For Type $\latI$ ($N = 0$), only $\Gr^W_2$ is non-trivial: a pure weight-$2$
Hodge structure.
For Type $\latII$ ($N \neq 0$, $N^2 = 0$), the non-trivial graded pieces are
$\Gr^W_1, \Gr^W_2, \Gr^W_3$ (weights $1, 2, 3$), with
$\Gr^W_0 = \Gr^W_4 = 0$.
For Type $\mathrm{III}$ ($N^2 \neq 0$, $N^3 = 0$), the non-trivial graded pieces
are $\Gr^W_0, \Gr^W_2, \Gr^W_4$ (weights $0, 2, 4$), of Hodge--Tate type.
:::

::: {.theorem ref="thm:lmhs" title="Limiting mixed Hodge structure and degenerations"}

For a one-parameter degeneration of polarized K3 surfaces over a punctured disk,
the unipotent monodromy operator $T \in \Orth(T_{2d})$ and its nilpotent
logarithm $N = \log T$ induce a canonical monodromy weight filtration
$W^{\bullet}$.

The boundary components of $\overline{F_{2d}}^{\bb}$ are classified by the
nilpotency index of $N$:

- **Type $\latII$ degenerations (1-cusps)**: $N \neq 0$, $N^2 = 0$.
  The weight filtration is 3-step ($W_0 \subset W_1 \subset W_2 \subset W_3$),
  and $\Gr_2^W = I^\perp / I = \overline{T}_I$ carries a pure polarized Hodge
  structure of weight 2.

- **Type $\mathrm{III}$ degenerations (0-cusps)**: $N^2 \neq 0$, $N^3 = 0$.
  The weight filtration is of maximal length.
  These correspond to normal crossing varieties whose dual complex is a
  triangulation of $S^2$.
:::

::: {.remark title="Attribution of the weight filtration"}

The canonical monodromy weight filtration attached to the nilpotent operator
$N = \log T$ is that of [@Sch73].
:::

::: {.remark title="Indexing of the weight filtration"}

The apparent discrepancy between the two accounts above is not a matter of
indexing convention but a distinction between Kulikov types. For Type $\latII$
the non-trivial graded pieces sit at weights $1, 2, 3$, with $\Gr^W_0 = 0$,
matching the $3$-step chain $W_0 \subset W_1 \subset W_2 \subset W_3$ of
\cref{thm:lmhs}. The even-weight pieces at $0, 2, 4$ occur instead for Type
$\mathrm{III}$, which is of Hodge--Tate type.
:::

::: {.remark title="Source notes carried no citations"}

\todo{The two migrated research notes (Kulikov Models; Limiting Mixed Hodge Structure and Degenerations) contained no inline citations. The attributions above (Kul77, PP81, Sch73, FS86) were supplied from verified bibliography keys as standard attributions of the concepts the notes name; the author should confirm the intended primary sources. The notes contained no Clemens--Schmid statement, no explicit semistable-reduction theorem, and no $N^k$ nilpotent-orbit computation beyond the trichotomy reproduced above.}
:::
