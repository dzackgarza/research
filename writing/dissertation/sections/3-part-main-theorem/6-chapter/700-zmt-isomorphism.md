### Application of Zariski's Main Theorem {#section-7-7}

In this section, we apply Zariski’s Main Theorem to the classifying morphism $\phi: \normalize{B} \to \cpt{\fentwo}$ constructed in previous sections, obtaining a precise modular isomorphism between the KSBA compactification and the explicit semitoroidal model described via folded ramification semifans.

::: {.theorem
    title="Zariski's main theorem"
    #thm:zariski-main-theorem
}
Let $f: X \to Y$ be a birational morphism of varieties.

1. If $f$ is quasi-finite and $Y$ is normal, then $f$ is an isomorphism of $X$ onto an open subset of $Y$.

2. If in addition $f$ is proper, then $f$ is an isomorphism.
:::

::: {.proof}

This is Zariski's main theorem in the birational form of [@Mum70, §III.9].
The first assertion is the theorem; the second follows because a proper morphism has closed image, so an image that is open is also closed, hence all of $Y$ when $Y$ is connected.
A finite morphism is proper and quasi-finite, so the finite case of the classical statement is the case in which both clauses apply at once: there normality of the target alone suffices.
:::

::: {.lemma
    title="{Verification of Hypotheses for the Classifying Map}"
    #lem:verification-hypotheses
}
The morphism $\phi: \normalize{B} \to \cpt{\fentwo}$ constructed above satisfies the hypotheses of Zariski's Main Theorem:

1. Birationality: By @prop:properties-classifying, $\phi$ restricts to an isomorphism over the dense open subset $\fentwo$.

2. Quasi-finiteness: By @cor:finiteness-classifying-map, $\phi$ is finite, hence proper and quasi-finite.

3. Normality of the target: $\ksbacpt{\fentwo}$ is normal as the normalization of the proper algebraic stack $\cpt{\fentwo}$.
:::

::: {.proof}

The three items verify the hypotheses of @thm:zariski-main-theorem: birational, quasi-finite, and normal target, which give that $\phi$ is an isomorphism onto an open subset, and finiteness, which gives properness and hence the isomorphism.
$\normalize{B}$ is normal by construction, which the theorem does not require.
Properness of the KSBA moduli stack [@Kol23] enters through $\phi$ being a map of proper spaces, not as a hypothesis of the theorem.
:::

We are thus led to the following:

::: {.theorem
    title="{Main Isomorphism: KSBA and Semitoroidal Compactifications}"
    #thm:main-isomorphism
}
The classifying morphism induces canonical isomorphisms:

\begin{align*}
\phi: \normalize{B} \xrightarrow{\sim} \ksbacpt{\fentwo}
.\end{align*}

and hence,

\begin{align*}
\ksbacpt{\fentwo} \cong \semitorcpt{\fentwo}
.\end{align*}

where $\mathcal{F} = \{\mathcal{F}_k\}_{k=1}^5$ denotes the system of folded semifans constructed previously.
:::

::: {.proof}
We know that $\phi$ is an isomorphism of normal proper spaces.
Surjectivity onto $\ksbacpt{\fentwo}$ follows from the construction of $\phi$ itself.
Finally, $\normalize{B}$ is canonically identified, as a semitoroidal compactification via $\mathcal{F}$, with $\semitorcpt{\fentwo}$.
:::

::: {.remark
    title="{Toroidal vs. Semitoroidal Structure}"
    #rem:toroidal-vs-semitoroidal
}
We finally remark that the resulting compactification exhibits hybrid toroidal/semitoroidal structures:

- It is toroidal over the 0-cusps 2 and 4 (where $\mathcal{F}_2$ and $\mathcal{F}_4$ are honest fans),

- It is toroidal over the 1-cusps adjacent to the 0-cusps 2 and 4,

- It is toroidal over the 1-cusp labeled $35$,

- It is strictly semitoroidal (i.e., not toroidal but modeled on an infinite semifan) over the remaining cusps ($\mathcal{F}_1$, $\mathcal{F}_3$, $\mathcal{F}_5$).

This completes the identification of the KSBA compactification with the explicit semitoroidal model given by folding and restricting the ambient K3 ramification semifans.
All boundary and degeneration structures in $\ksbacpt{\fentwo}$ are thus characterized in terms of folded data for $\fttz$.
:::
