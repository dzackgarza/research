# Kulikov models and limiting mixed Hodge structures {#sec-kulikov-models}

::: {.remark}

We collect the local structure theory attached to a one-parameter degeneration of K3 surfaces: the Kulikov models that provide a well-behaved semistable representative of a degeneration, the trichotomy of such models by the nilpotency of the log monodromy operator, and the limiting mixed Hodge structure whose monodromy weight filtration records the same trichotomy on the Baily--Borel boundary.
:::

## Kulikov degenerations

::: {.definition #def:kulikov-model title="Kulikov models"}

A *Kulikov model* is a degeneration $\mcx \to \Delta$ of K3 surfaces where:

1. The total space $\mcx$ is regular (smooth as a threefold).

2. The central fiber $\mcx_0$ is a reduced simple normal crossings (snc) divisor.

3. The relative dualizing sheaf is trivial: $\omega_{\mcx/\Delta} \cong \OO_{\mcx}$.

Such a model is *semistable* by conditions (1) and (2) and *$K$-trivial* by condition (3).
:::

::: {.remark title="Existence and attribution"}

The Kulikov model is the semistable, $K$-trivial representative constructed for degenerations of K3 (and Enriques) surfaces in [@Kul77], with the $K$-trivialization of the semistable reduction supplied for surfaces of trivial canonical bundle by [@PP81].
:::

::: {.definition #def:kulikov-types title="Type I, II, III Kulikov degenerations"}

Let $T$ be the unipotent Picard--Lefschetz monodromy of a Kulikov model and let $N = \log T$ be the associated *log monodromy* operator, a nilpotent endomorphism.
Depending on the nilpotency index of $N$, Kulikov models are classified into three types:

- **Type $\latI$** ($N = 0$): $\mcx_0$ is a smooth K3 surface.

- **Type $\latII$** ($N^2 = 0$, $N \neq 0$): $\mcx_0$ is a chain of surfaces glued along elliptic curves.
  The dual complex is an interval.

- **Type $\mathrm{III}$** ($N^3 = 0$, $N^2 \neq 0$): $\mcx_0$ is a union of rational surfaces glued along rational curves, forming an anticanonical cycle on each component.
  The dual complex is a sphere $\ias$.
:::

::: {.remark title="The Type III dual complex"}

The identification of the Type $\mathrm{III}$ central fiber as a union of rational surfaces whose dual complex triangulates a sphere is the subject of [@FS86].
:::

## The monodromy weight filtration

::: {.remark title="The weight filtration by type"}

The **weight filtration** $W_\bullet$ on $H^2(\mcx_t; \CC)$ (weight $2$, centered at $n = 2$) reflects the three types, by the nilpotency of $N$.
For Type $\latI$ ($N = 0$), only $\Gr^W_2$ is non-trivial: a pure weight-$2$ Hodge structure.
For Type $\latII$ ($N \neq 0$, $N^2 = 0$), the non-trivial graded pieces are $\Gr^W_1, \Gr^W_2, \Gr^W_3$ (weights $1, 2, 3$), with $\Gr^W_0 = \Gr^W_4 = 0$.
For Type $\mathrm{III}$ ($N^2 \neq 0$, $N^3 = 0$), the non-trivial graded pieces are $\Gr^W_0, \Gr^W_2, \Gr^W_4$ (weights $0, 2, 4$), of Hodge--Tate type.
:::

::: {.theorem #thm:lmhs title="Limiting mixed Hodge structure and degenerations"}

For a one-parameter degeneration of polarized K3 surfaces over a punctured disk, the unipotent monodromy operator $T \in \Orth(T_{2d})$ and its nilpotent logarithm $N = \log T$ induce a canonical monodromy weight filtration $W^{\bullet}$.

The boundary components of $\bbcpt{\ftd}$ are classified by the nilpotency index of $N$:

- **Type $\latII$ degenerations (1-cusps)**: $N \neq 0$, $N^2 = 0$.
  The weight filtration is 3-step ($W_0 \subset W_1 \subset W_2 \subset W_3$), and $\Gr_2^W = I^\perp / I = \overline{T}_I$ carries a pure polarized Hodge structure of weight 2.

- **Type $\mathrm{III}$ degenerations (0-cusps)**: $N^2 \neq 0$, $N^3 = 0$.
  The weight filtration is of maximal length.
  These correspond to normal crossing varieties whose dual complex is a triangulation of $S^2$.
:::

::: {.proof}

The construction of the limiting mixed Hodge structure is the nilpotent orbit theorem together with the Clemens-Schmid sequence [@Sch73; @Cle77], and the relation between the nilpotency index of $N$ and the type of the degeneration is Kulikov's classification [$@Kul77; @PP81].

The graded piece is identified in the book's notation as follows.
For a degeneration of type II the monodromy is unipotent with $N\neq0$, $N^2=0$, so the weight filtration has the three steps $0\subset W_1\subset W_2\subset W_3$ with $\Gr^W_i=0$ otherwise; the primitive part of $H^2$ contributing to $\Gr^W_2$ is annihilated by $N$ and by its transpose, hence is the orthogonal complement of the isotropic subspace $I$ of the special fibre, quotiented by $I$ itself, which is $\overline{T}_I$ of the boundary lattice.
So the pure Hodge structure of weight $2$ on $\Gr^W_2$ is the one on $\overline{T}_I$, and by @def:signature its signature is $(2-k,n-k)$ for $\rank I=k$, which is the statement of the toroidal boundary that this chapter uses.
For type III the index is $3$ and the weight filtration has the maximal length, which is why the dual complex of the special fibre is two-dimensional, and the tripod description of @sec-ias-degenerations is that geometry.
:::

::: {.remark title="Attribution of the weight filtration"}

The canonical monodromy weight filtration attached to the nilpotent operator $N = \log T$ is that of [@Sch73].
:::

::: {.remark title="Indexing of the weight filtration"}

The apparent discrepancy between the two accounts above is not a matter of indexing convention but a distinction between Kulikov types.
For Type $\latII$ the non-trivial graded pieces sit at weights $1, 2, 3$, with $\Gr^W_0 = 0$, matching the $3$-step chain $W_0 \subset W_1 \subset W_2 \subset W_3$ of the limiting mixed-Hodge theorem (@thm:lmhs).
The even-weight pieces at $0, 2, 4$ occur instead for Type $\mathrm{III}$, which is of Hodge--Tate type.
:::

::: {.warning title="Source notes carried no citations"}
The underlying notes on Kulikov models and limiting mixed Hodge structures contained no inline citations.
The attributions above (Kul77, PP81, Sch73, FS86) were supplied from verified bibliography keys as standard attributions of the concepts the notes name; the author should confirm the intended primary sources.
The notes contained no Clemens--Schmid statement, no explicit semistable-reduction theorem, and no $N^k$ nilpotent-orbit computation beyond the trichotomy reproduced above.
:::
