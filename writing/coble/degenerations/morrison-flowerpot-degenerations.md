# Morrison's degenerations

::: {.definition #def:flower-pot-degeneration title="Flowers, stalks, pots and flower pot degenerations"}

A **marked surface** $(V, D)$ is an algebraic surface $V$ with a reduced effective divisor $D\subset V$ with local normal crossings.

- A **flower** is a marked surface $(\PP^2, C)$ with $C\subset\PP^2$ a conic.
- A **stalk** is a marked surface $(\FF_4, \sigma_0 + \sigma_\infty)$, where $\sigma_0$ and $\sigma_\infty$ are the $0$- and $\infty$-sections of the Hirzebruch surface $\FF_4$, of self-intersection $4$ and $-4$.
- A **stalk assembly** of length $k$ is a flower joined to $k - 1$ stalks.
- A **pot** is a rational surface $V$ marked by $D = \Sum C_\alpha$, with each $C_\alpha$ rational and $C_\alpha\cdot C_\beta = -4\delta_{\alpha\beta}$.
- A **flower pot degeneration** is a semistable degeneration $X\to\Delta$ such that $X_0$ consists of a pot meeting stalk assemblies along its double curves.

[@Mor81, Ex. 1.6; @Sha81a, Appendix].
:::

::: {.proposition #prop:flower-pot-periods title="Periods of flower pot degenerations"}

Let $\Lambda$ be the $(-1)$-eigenlattice of the covering involution on the second homology of the K3 cover of an Enriques surface, and for $\lambda\in\Lambda$ with $\lambda^2 = -2$ let $H_\lambda\subset\Gamma\backslash D$ be the hypersurface of periods of K3 surfaces on which $\lambda$ is of type $(1,1)$.

1. Let $X\to\Delta$ be a flower pot degeneration, with period map $\Phi\colon\Delta^*\to\Gamma\backslash D$.
   If $\Phi$ extends to $\Phi\colon\Delta\to\Gamma\backslash D$, then $\Phi(0)\in H_\lambda$ for some $\lambda$ [@Mor81, Lemma 7.1].

2. Let $X\to\Delta$ be a weakly projective flower pot degeneration.
   Then $2K_{\tilde X}\not\equiv 0$ for every semistable birational model $\tilde X$ of $X$ [@Mor81, Cor. 7.2].
:::

::: {.proposition #prop:morrison-dlt-correspondence title="Morrison's degenerations and dlt models"}

The cases (i a), (i b), (ii a), (ii b), (iii a) and (iii b) of the classification of semistable degenerations of Enriques surfaces [@Mor81, Cor. 6.2] correspond, respectively, to:

- Type $\latI$ degenerations;
- Type $\latI$ degenerations with a klt singularity;
- Type $\latII$ degenerations with Enriques involution flipping the segment;
- Type $\latII$ degenerations with Enriques involution fixing the segment;
- Type $\mathrm{III}$ degenerations with $\Gamma(Z_0) = \RP^2$ (cusp $1$);
- Type $\mathrm{III}$ degenerations with $\Gamma(Z_0) = \Dc^2$ (cusps $2$ to $5$).

Case (i b) is the flower pot.
The flowers and stalk assemblies are the semistable resolutions of the $S_2$-quotients of the $ADE$ singularities in the total space of the smoothing.
The pots are the components of the dlt models (@def:dlt-model) along which the flower and stalk assembly are attached [@AEGS25, Rem. 4.12].
:::
