# The classifying map and the Enriques involution

::: {.remark title="Orientation"}

The results collected here are the intended culmination of the compactification program for $F_{\En, 2}$: the classifying morphism $\phi$ from the normalized Noether--Lefschetz closure $B^\nu$ to the KSBA compactification of the polarized moduli space should be shown to be an isomorphism, so that the geometric KSBA limits are identified with the explicitly constructible semitoroidal boundary.
The three ingredients are a *global extension of the Enriques involution* over $B$, a *finiteness statement* for $\phi$, and the *application of Zariski's Main Theorem* that combines them.

These are the program's own in-progress steps rather than settled theorems.
They are stated conjecturally throughout, and they are exactly parallel to the open comparison of \cref{conj:ksba_semitoroidal_comparison} and to the incomplete normalization argument of \cref{thm:normalization}, whose migrated proof sketch records the author's remark that finiteness is *still unclear*.
Zariski's Main Theorem itself is a classical, proven theorem; only its application to $\phi$ is conjectural here.
\todo{The three source notes ("Extension of Enriques Involution", "Finiteness of the Classifying Map", "Zariski's Main Theorem in Moduli") carried no inline citations. Standard sources are supplied below for the concepts the notes name (the KSBA compactification $\overline{F_{\En,2}}$ and separatedness of KSBA limits via AEGS25/Kol23a; Zariski's Main Theorem via Har10a); the author should confirm the intended primary references and pin locators.}
:::

## Global extension of the Enriques involution

::: {.conjecture ref="conj:enriques_involution_extension" title="Global extension of the Enriques involution"}

Over the Noether--Lefschetz closure $B \subseteq \overline{F_{(2,2,0)}}$ of \cref{def:nl-locus-enriques}, there is a universal KSBA family $(\mathcal{X}_B, \varepsilon \mathcal{R}_B)$.
The fixed-point-free Enriques involution $\iota_{\En}$ on the smooth fibers is expected to extend uniquely to a global involution on the entire family $\mathcal{X}_B$.

This global involution should preserve the slc pair structure, preserve the ramification divisor $\mathcal{R}_B$, and commute with the global del Pezzo involution $\iota_{\dP}$.
The quotient $(\mathcal{X}_B, \varepsilon \mathcal{R}_B) / \iota_{\En}$ would then form a flat family of stable Enriques pairs over $B$.
:::

::: {.remark title="Intended mechanism"}

The uniqueness of the extension is the expected consequence of the separatedness of KSBA stable limits: on the smooth locus the involution is the fixed-point-free deck transformation $\iota_{\En}$ of the canonical cover, and a fiberwise automorphism of a family of stable pairs extends across the boundary by uniqueness of the limit [@AEGS25; @Kol23a].
This is the same extension-by-uniqueness step invoked in the proposed KSBA-to-semitoroidal comparison (\cref{conj:ksba_semitoroidal_comparison}), where the Enriques involution is extended over the stable limits and the ramification divisor descended.
The source note asserted the extension, the preservation of the slc structure and of $\mathcal{R}_B$, the commutation with $\iota_{\dP}$, and the flatness of the quotient family, without proof; each remains an obligation of the program.
:::

## Finiteness of the classifying map

::: {.conjecture ref="conj:classifying_map_finite" title="Finiteness of the classifying map"}

The classifying morphism
$$
\phi\colon B^\nu \to \overline{F_{\En, 2}}
$$
from the normalization $B^\nu$ of the Noether--Lefschetz closure is finite.
:::

::: {.remark title="Proposed combinatorial argument"}

The source note proposes to establish finiteness by a combinatorial comparison of semifans.
The normal KSBA compactification induces its own semifans $\mathcal{G}_k$, which are coarsenings of the folded Coxeter semifans $\mathcal{F}_k$.
The map is finite if and only if no coarsening occurs, i.e. $\mathcal{G}_k = \mathcal{F}_k$ for all $k$.

If a strict coarsening occurred, then distinct maximal degenerations -- differing by a double curve -- would be identified in the target.
The proposed input is the KSBA principle that the dual complex uniquely identifies maximally degenerate limits; granting this, no such identification can occur, and hence no coarsening occurs.

This argument is presented as the program's intended route, not as a completed proof.
\todo{Note-vs-note conflict: the source note states finiteness is "proved via a combinatorial comparison", whereas the parallel normalization argument (\cref{thm:normalization}) is migrated with the author's inline remark that "finiteness is still unclear" and a suggestion to use $\text{finite} \iff \text{proper with finite fibers}$ (Stacks 02LS) or Zariski's Main Theorem. These two accounts should be reconciled; until then finiteness is rendered conjecturally. The no-coarsening statement is moreover the same phenomenon as the no-moduli-loss conjecture (\cref{conj:no_moduli_loss}), which is itself open.}
:::

## Zariski's Main Theorem and the classifying isomorphism

::: {.theorem ref="thm:zariski_main_theorem" title="Zariski's Main Theorem (classical)"}

Let $f\colon X \to Y$ be a birational, finite morphism between normal varieties, with $Y$ proper.
Then $f$ is an isomorphism.
:::

::: {.remark}

\cref{thm:zariski_main_theorem} is a classical theorem [@Har10a]; a finite birational morphism onto a normal variety is an isomorphism.
It is invoked here only as an external tool; the content below -- that the classifying map $\phi$ satisfies its hypotheses -- is the program's own claim.
:::

::: {.conjecture ref="conj:classifying_map_isomorphism" title="The classifying map is an isomorphism"}

For the Enriques compactification, the classifying map
$$
\phi\colon B^\nu \to \overline{F_{\En, 2}}^{\,\nu}
$$
is expected to satisfy the four hypotheses of \cref{thm:zariski_main_theorem}:

1. **Birational**: $\phi$ is an isomorphism on the interior $F_{\En, 2}$.

2. **Finite**: by the proposed "no coarsening" semifan argument of \cref{conj:classifying_map_finite}.

3. **Normal**: both spaces are normal by construction ($B^\nu$ as a normalization, $\overline{F_{\En, 2}}^{\,\nu}$ likewise).

4. **Proper**: the KSBA moduli stacks are proper [@AEGS25; @Kol23a].

Granting these, Zariski's Main Theorem would give that $\phi$ is an isomorphism, identifying the geometric KSBA limits with the explicitly constructible semitoroidal boundary.
:::

::: {.remark title="Status of the hypotheses"}

Of the four inputs to \cref{conj:classifying_map_isomorphism}, properness and normality are the ambient structural facts of the KSBA and Baily--Borel constructions, while birationality on the interior and finiteness are the load-bearing steps: finiteness is the still-open \cref{conj:classifying_map_finite}, and the extension of the Enriques involution (\cref{conj:enriques_involution_extension}) is what makes the universal quotient family -- and hence $\phi$ -- available over the boundary in the first place.
The isomorphism statement therefore inherits the open status of \cref{conj:classifying_map_finite,conj:enriques_involution_extension}, and is the compactification-side counterpart of the semitoroidal comparison \cref{conj:ksba_semitoroidal_comparison}.
This conclusion also refines the incomplete normalization statement \cref{thm:normalization}, whose migrated proof leaves both the stabilizer identity and finiteness unestablished.
:::
