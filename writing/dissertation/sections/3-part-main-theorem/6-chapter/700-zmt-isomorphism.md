### Application of Zariski's Main Theorem {#section-7-7}

In this section, we apply Zariski’s Main Theorem to the classifying morphism $\phi: \normalize{B} \to \cpt{\fent}$ constructed in previous sections, obtaining a precise modular isomorphism between the KSBA compactification and the explicit semitoroidal model described via folded ramification semifans.

:::{.theorem
    title=""
    #thm:zariski-main-theorem
}
Let $f: X \to Y$ be a morphism of varieties. Suppose:

1. $f$ is birational,
2. $f$ is finite,
3. $X$ and $Y$ are normal,
4. $Y$ is proper.

Then $f$ is an isomorphism.
:::

:::{.lemma
    title="{Verification of Hypotheses for the Classifying Map}"
    #lem:verification-hypotheses
}
The morphism $\phi: \normalize{B} \to \cpt{\fent}$ constructed above satisfies all hypotheses of Zariski's Main Theorem:

1. Birationality: By @prop:properties-classifying, $\phi$ restricts to an isomorphism over the dense open subset $\fent$.
2. Finiteness: By @cor:finiteness-classifying-map, $\phi$ is finite.
3. Normality: $\normalize{B}$ is normal by definition as normalization; $\ksbacpt{\fent}$ is normal as the normalization of the proper algebraic stack $\cpt{\fent}$.
4. Properness: $\cpt{\fent}$ is proper by the general theory of KSBA compactification for surfaces with numerically trivial canonical class (see Kollár[\text{Theorem 1.2}]).
:::

We are thus led to the following:

:::{.theorem
    title="{Main Isomorphism: KSBA and Semitoroidal Compactifications}"
    #thm:main-isomorphism
}
The classifying morphism induces canonical isomorphisms:

\begin{align*}
\phi: \normalize{B} \xrightarrow{\sim} \ksbacpt{\fent}
.\end{align*}

and hence,

\begin{align*}
\ksbacpt{\fent} \cong \semitorcpt{\fent}
.\end{align*}

where $\mathcal{F} = \{\mathcal{F}_k\}_{k=1}^5$ denotes the system of folded semifans constructed previously.
:::

:::{.proof}
We know that $\phi$ is an isomorphism of normal proper spaces. Surjectivity onto $\ksbacpt{\fent}$ follows from the construction of $\phi$ itself. Finally, $\normalize{B}$ is canonically identified, as a semitoroidal compactification via $\mathcal{F}$, with $\semitorcpt{\fent}$.
:::

:::{.remark
    title="{Toroidal vs. Semitoroidal Structure}"
    #rem:toroidal-vs-semitoroidal
}
We finally remark that the resulting compactification exhibits hybrid toroidal/semitoroidal structures:

- It is toroidal over the 0-cusps 2 and 4 (where $\mathcal{F}_2$ and $\mathcal{F}_4$ are honest fans),

- It is toroidal over the 1-cusps adjacent to the 0-cusps 2 and 4,

- It is toroidal over the 1-cusp labeled $35$,

- It is strictly semitoroidal (i.e., not toroidal but modeled on an infinite semifan) over the remaining cusps ($\mathcal{F}_1$, $\mathcal{F}_3$, $\mathcal{F}_5$).

This completes the identification of the KSBA compactification with the explicit semitoroidal model given by folding and restricting the ambient K3 ramification semifans. All boundary and degeneration structures in $\ksbacpt{\fent}$ are thus characterized in terms of folded data for $\fttz$.
:::
