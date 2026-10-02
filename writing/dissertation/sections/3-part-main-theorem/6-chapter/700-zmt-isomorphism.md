### Identification of the Normalization {#section-7-7}

The previous section proves that the classifying morphism
$$
\phi\colon \normalize{B}\longrightarrow\ksbacpt{\fent}
$$
is finite and birational, with normal source. Therefore it is the normalization morphism of the KSBA compactification. Combining this with the semitoroidal description of $\normalize{B}$ gives the precise form of the main theorem [@AEGS25, Thm. 5.9].

:::{.theorem
    title="Main Isomorphism: Normalized KSBA and Semitoroidal Compactifications"
    #thm:main-isomorphism
}
There are canonical isomorphisms

\begin{align*}
\normalize{B}
\xrightarrow{\sim}
\normksbacpt{\fent}
\xrightarrow{\sim}
\semitorcpt{\fent}
.\end{align*}
where $\semifans{F} = \{\semifan{F}_k\}_{k=1}^5$ denotes the system of folded semifans constructed previously.
The original classifying morphism $\phi\colon\normalize{B}\to\ksbacpt{\fent}$ is the finite normalization morphism; no claim that the possibly non-normal KSBA compactification itself is isomorphic to the semitoroidal compactification is required.
:::

:::{.proof}
By @cor:finiteness-classifying-map, $\phi$ is finite and birational, and $\normalize{B}$ is normal. Hence $\normalize{B}$ identifies with the normalization $\normksbacpt{\fent}$ of its target. By @thm:no-coarsening and the construction of @prop:restriction-semifans, $\normalize{B}$ is the semitoroidal compactification determined by the semifans $\semifans{F}$, giving the second isomorphism. This is exactly [@AEGS25, Thm. 5.9].
:::

:::{.remark
    title="Toroidal vs. Semitoroidal Structure"
    #rem:toroidal-vs-semitoroidal
}
We finally remark that the resulting compactification exhibits hybrid toroidal/semitoroidal structures:

- It is toroidal over the 0-cusps 2 and 4 (where $\semifan{F}_2$ and $\semifan{F}_4$ are honest fans),

- It is toroidal over the 1-cusps adjacent to the 0-cusps 2 and 4,

- It is toroidal over the 1-cusp labeled $35$,

- It is strictly semitoroidal over the remaining cusps; in particular $\semifan{F}_1$, $\semifan{F}_3$, and $\semifan{F}_5$ are not fans and their fundamental cones have infinitely many generators [@AEGS25, Lem. 5.6].

This completes the identification of the normalization of the KSBA compactification with the explicit semitoroidal model obtained by folding and restricting the ambient K3 ramification semifans.
:::
