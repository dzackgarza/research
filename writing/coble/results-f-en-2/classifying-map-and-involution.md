# The classifying map and the Enriques involution

::: {.Remark}
### Orientation

The results collected here are the intended culmination of the compactification program for $\fentwo$: the classifying morphism $\phi$ from the normalized Noether--Lefschetz closure $\normalize{B}$ to the KSBA compactification of the polarized moduli space should be shown to be an isomorphism, so that the geometric KSBA limits are identified with the explicitly constructible semitoroidal boundary.
The three ingredients are a *global extension of the Enriques involution* over $B$, a *finiteness statement* for $\phi$, and the *application of Zariski's Main Theorem* that combines them.

These are the program's own in-progress steps rather than settled theorems.
They are stated conjecturally throughout, and they are exactly parallel to the open comparison of [the KSBA--semitoroidal comparison conjecture](#conj:ksba_semitoroidal_comparison).
The period-domain counterpart of the finiteness step is [the normalization theorem](#thm:normalization), which is proved; what is open here is the KSBA-side statement for $\phi$.
Zariski's Main Theorem itself is a classical, proven theorem; only its application to $\phi$ is conjectural here.

::: {.Remark}
The KSBA compactification $\ksbacpt{\fentwo}$ and the separatedness of its limits are
[@AEGS25] and [@Kol23a]; Zariski's Main Theorem in the form used below is [@Har10a].
:::
:::

## Global extension of the Enriques involution

::: {.Conjecture #conj:enriques_involution_extension}
### Global extension of the Enriques involution

Over the Noether--Lefschetz closure $B \containedin \ksbacpt{\fttz}$ of [the Enriques Noether--Lefschetz-locus definition](#def:nl-locus-enriques), there is a universal KSBA family $(\mathcal{X}_B, \varepsilon \mathcal{R}_B)$.
The fixed-point-free Enriques involution $\ien$ on the smooth fibers is expected to extend uniquely to a global involution on the entire family $\mathcal{X}_B$.

This global involution should preserve the slc pair structure, preserve the ramification divisor $\mathcal{R}_B$, and commute with the global del Pezzo involution $\idp$.
The quotient $(\mathcal{X}_B, \varepsilon \mathcal{R}_B) / \ien$ would then form a flat family of stable Enriques pairs over $B$.
:::

::: {.Remark}
### Intended mechanism

The uniqueness of the extension is the expected consequence of the separatedness of KSBA stable limits: on the smooth locus the involution is the fixed-point-free deck transformation $\ien$ of the canonical cover, and a fiberwise automorphism of a family of stable pairs extends across the boundary by uniqueness of the limit [@AEGS25; @Kol23a].
This is the same extension-by-uniqueness step invoked in the proposed KSBA-to-semitoroidal comparison ([the comparison conjecture](#conj:ksba_semitoroidal_comparison)), where the Enriques involution is extended over the stable limits and the ramification divisor descended.
The source note asserted the extension, the preservation of the slc structure and of $\mathcal{R}_B$, the commutation with $\idp$, and the flatness of the quotient family, without proof; each remains an obligation of the program.
:::

## Finiteness of the classifying map

::: {.Conjecture #conj:classifying_map_finite}
### Finiteness of the classifying map

The classifying morphism
$$
\phi\colon \normalize{B} \to \ksbacpt{\fentwo}
$$
from the normalization $B^\nu$ of the Noether--Lefschetz closure is finite.
:::

::: {.Remark}
### Proposed combinatorial argument

The source note proposes to establish finiteness by a combinatorial comparison of semifans.
The normal KSBA compactification induces its own semifans $\semifan{G}_k$, which are coarsenings of the folded Coxeter semifans $\semifan{F}_k$.
The map is finite if and only if no coarsening occurs, i.e. $\semifan{G}_k = \semifan{F}_k$ for all $k$.

If a strict coarsening occurred, then distinct maximal degenerations -- differing by a double curve -- would be identified in the target.
The proposed input is the KSBA principle that the dual complex uniquely identifies maximally degenerate limits; granting this, no such identification can occur, and hence no coarsening occurs.

This argument is presented as the program's intended route, not as a completed proof.

::: {.Remark}
### Which morphism is being made finite

The statement above is finiteness of $\phi\colon \normalize{B}\to\ksbacpt{\fentwo}$, a morphism of KSBA compactifications, and its proposed proof is the semifan comparison just described.
It is a different statement from the finiteness of the period map $\fco\to \fen$ established in [the normalization theorem](#thm:normalization).
The two share the criterion -- a proper morphism with finite fibres is finite [Stacks Project, Tag 02LS](https://stacks.math.columbia.edu/tag/02LS) -- and nothing else: on the period side the fibre count is a count of $(-2)$-vectors in a negative definite lattice, whereas here the fibres are controlled by whether the induced semifans coarsen.
The no-coarsening statement is moreover the same phenomenon as [the no-moduli-loss conjecture](#conj:no_moduli_loss), which is itself open.
:::
:::

## Zariski's Main Theorem and the classifying isomorphism

::: {.Theorem #thm:zariski_main_theorem}
### Zariski's Main Theorem (classical)

Let $f\colon X \to Y$ be a birational, finite morphism between normal varieties, with $Y$ proper.
Then $f$ is an isomorphism.
:::

::: {.Remark}

[Zariski's Main Theorem](#thm:zariski_main_theorem) is a classical theorem [@Har10a]; a finite birational morphism onto a normal variety is an isomorphism.
It is invoked here only as an external tool; the content below -- that the classifying map $\phi$ satisfies its hypotheses -- is the program's own claim.
:::

::: {.Conjecture #conj:classifying_map_isomorphism}
### The classifying map is an isomorphism

For the Enriques compactification, the classifying map
$$
\phi\colon \normalize{B} \to \normksbacpt{\fentwo}
$$
is expected to satisfy the four hypotheses of [Zariski's Main Theorem](#thm:zariski_main_theorem):

1. **Birational**: $\phi$ is an isomorphism on the interior $\fentwo$.

2. **Finite**: by the proposed "no coarsening" semifan argument of [the finiteness conjecture](#conj:classifying_map_finite).

3. **Normal**: both spaces are normal by construction ($\normalize{B}$ as a normalization, $\normksbacpt{\fentwo}$ likewise).

4. **Proper**: the KSBA moduli stacks are proper [@AEGS25; @Kol23a].

Granting these, Zariski's Main Theorem would give that $\phi$ is an isomorphism, identifying the geometric KSBA limits with the explicitly constructible semitoroidal boundary.
:::

::: {.Remark}
### Status of the hypotheses

Of the four inputs to [the classifying-map isomorphism conjecture](#conj:classifying_map_isomorphism), properness and normality are the ambient structural facts of the KSBA and Baily--Borel constructions, while birationality on the interior and finiteness are the load-bearing steps: finiteness is the still-open [finiteness conjecture](#conj:classifying_map_finite), and [the Enriques-involution extension conjecture](#conj:enriques_involution_extension) is what makes the universal quotient family -- and hence $\phi$ -- available over the boundary in the first place.
The isomorphism statement therefore inherits the open status of [the finiteness conjecture](#conj:classifying_map_finite) and [the Enriques-involution extension conjecture](#conj:enriques_involution_extension), and is the compactification-side counterpart of [the KSBA--semitoroidal comparison conjecture](#conj:ksba_semitoroidal_comparison).
The same three-step shape -- stabilizer, finite fibres, properness -- is what carries [the normalization theorem](#thm:normalization) on the period side; the open part here is that the semifan comparison replacing the fibre count is not yet established.
:::
