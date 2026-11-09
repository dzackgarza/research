# The classifying map and the Enriques involution

::: {.remark title="Orientation"}

The results collected here are the intended culmination of the compactification program for $\fentwo$: the classifying morphism $\phi$ from the normalized Noether--Lefschetz closure $\normalize{B}$ to the KSBA compactification of the polarized moduli space should be shown to be an isomorphism, so that the geometric KSBA limits are identified with the explicitly constructible semitoroidal boundary.
The three ingredients are a *global extension of the Enriques involution* over $B$, a *finiteness statement* for $\phi$, and the *application of Zariski's Main Theorem* that combines them.

They are stated conjecturally throughout, and they are exactly parallel to the open comparison of the KSBA--semitoroidal comparison conjecture (@conj:ksba_semitoroidal_comparison). The period-domain counterpart of the finiteness step is the normalization theorem (@thm:normalization), which is proved; what is open here is the KSBA-side statement for $\phi$.
Zariski's Main Theorem itself is a classical, proven theorem; only its application to $\phi$ is conjectural here.
:::

::: {.remark}
The KSBA compactification $\ksbacpt{\fentwo}$ and the separatedness of its limits are [@AEGS25] and [@Kol23a]; Zariski's Main Theorem in the form used below is [@Har77].
:::

## Global extension of the Enriques involution

::: {.conjecture #conj:enriques_involution_extension title="Global extension of the Enriques involution"}

Over the Noether--Lefschetz closure $B \iscontainedin \ksbacpt{\fttz}$ of the Enriques Noether--Lefschetz-locus definition (@def:nl-locus-enriques), there is a universal KSBA family $(\mcx_B, \eps \mcr_B)$.
The fixed-point-free Enriques involution $\ien$ on the smooth fibers extends uniquely to an involution of $\mcx_B$.
This involution preserves the slc pair structure and the ramification divisor $\mcr_B$, and commutes with the del Pezzo involution $\idp$, so the quotient $(\mcx_B, \eps \mcr_B) / \ien$ is a flat family of stable Enriques pairs over $B$.
:::

::: {.remark}

On the smooth locus the involution is the deck transformation $\ien$ of the canonical cover. The moduli of stable pairs is separated [@AEGS25; @Kol23a], so an automorphism of a family of stable pairs over the smooth locus has at most one extension across the boundary.
:::

## Finiteness of the classifying map

::: {.conjecture #conj:classifying_map_finite title="Finiteness of the classifying map"}

The classifying morphism
$$
\phi\colon \normalize{B} \to \ksbacpt{\fentwo}
$$
from the normalization $B^\nu$ of the Noether--Lefschetz closure is finite.
:::

::: {.remark title="A semifan criterion"}

The normal KSBA compactification induces semifans $\semifan{G}_k$, which are coarsenings of the folded Coxeter semifans $\semifan{F}_k$.
The map $\phi$ is finite if and only if $\semifan{G}_k = \semifan{F}_k$ for all $k$.

A strict coarsening identifies in the target two maximal degenerations that differ by a double curve.
So $\phi$ is finite if the dual complex of a maximally degenerate stable limit determines the limit.
:::

## Zariski's Main Theorem and the classifying isomorphism

::: {.theorem #thm:zariski_main_theorem title="Finite birational maps onto a normal variety"}

Let $f\colon X \to Y$ be a finite birational morphism of varieties, with $Y$ normal.
Then $f$ is an isomorphism.
:::

::: {.proof}

A finite morphism is affine, so locally $Y = \Spec A$ and $X = \Spec B$ with $B$ a finite $A$-module containing $A$; birationality identifies $\Frac B$ with $\Frac A = K$, giving $A\iscontainedin B\iscontainedin K$.
Since $Y$ is normal, $A$ is integrally closed in $K$, and $B$ is integral over $A$, so $B = A$.

:::

::: {.conjecture #conj:classifying_map_isomorphism title="The classifying map is an isomorphism"}

The classifying map
$$
\phi\colon \normalize{B} \to \normksbacpt{\fentwo}
$$
is an isomorphism.
:::

The target $\normksbacpt{\fentwo}$ is normal, and $\phi$ is a morphism of proper spaces [@AEGS25; @Kol23a], so $\phi$ is finite if and only if its fibres are finite [@stacks-02LS].
By @thm:zariski_main_theorem, @conj:classifying_map_isomorphism follows from three statements: $\phi$ is defined over the boundary, which holds if @conj:enriques_involution_extension holds; $\phi$ is an isomorphism over $\fentwo$; and $\phi$ is finite (@conj:classifying_map_finite).
