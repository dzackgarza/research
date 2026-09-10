### Defining $\fent$ and $\cpt{\fent}$ {#section-7-1}


:::{.definition
    title="{Moduli Stack $\fent$ of Numerically Polarized Enriques Surfaces of Degree Two}"
    #def:fent
}
Let $\fent$ be the Deligne–Mumford stack over $\CC$ parameterizing isomorphism classes of pairs $(Z, L)$, where

- $Z$ is a smooth Enriques surface,
- $L \in \mathrm{Pic}(Z)$ is a nef and big divisor class satisfying
  
\begin{align*}
L^2 = 2, \qquad L \cdot C > 0 \text{ for every } (-2)\text{-curve } C \subset Z.
\end{align*}

Two pairs $(Z, L)$ and $(Z', L')$ are isomorphic if there exists an isomorphism $\varphi : Z \xrightarrow{\sim} Z'$ such that $\varphi^* L' \equiv L$. The numerical equivalence represents the action of the automorphism group of $Z$ and preserves the polarization class up to numerical type.
:::

:::{.definition
    title="{KSBA Compactification $\cpt{\fent}$ of $\fent$}"
    #def:cpt-fent
}
Fix a rational $0 < \varepsilon \ll 1$. The KSBA compactification $\cpt{\fent}$ is defined as the Deligne–Mumford stack whose objects over $\CC$-schemes are isomorphism classes of pairs $(Z, \varepsilon R_Z)$, satisfying:

- $Z$ is a projective surface with numerically trivial canonical divisor, $K_Z \equiv 0$,
- $R_Z$ is an effective $\QQ$-Cartier divisor such that the pair $(Z, \varepsilon R_Z)$ is semi-log-canonical (slc),
- The divisor $K_Z + \varepsilon R_Z$ is ample,
- On the open locus where $Z$ is smooth, $R_Z$ is numerically equivalent to $2L$ for some $(Z, L) \in \fent$.

The open substack consisting of pairs with smooth $Z$ and $R_Z$ the branch divisor of the associated K3 double cover is canonically isomorphic to $\fent$.
:::


:::{.theorem
    title="{Basic Properties of $\cpt{\fent}$}"
    #thm:basic-fent
}
The stack $\cpt{\fent}$ is a proper, separated, normal Deligne–Mumford stack of finite type over $\CC$ . The inclusion $\fent \hookrightarrow \cpt{\fent}$ realizes $\fent$ as the maximal open substack whose geometric points correspond to smooth numerically polarized Enriques surfaces of degree two. Each one-parameter family in $\fent$ admits a unique extension, up to unique isomorphism, to $\cpt{\fent}$. That is, the KSBA compactification provides unique stable limits for degenerating families.
:::

Pairs $(Z, L)$ as above parameterize the interior of the moduli problem, encoding the data of smooth numerically polarized Enriques surfaces of degree two. The KSBA compactification $\cpt{\fent}$ systematically includes stable degenerations: objects $(Z, \varepsilon R_Z)$ where $Z$ may acquire slc singularities and $R_Z$ encodes the polarization determined by the ramification divisor of $\idp$ on the K3 cover.
We will develop further refinements of this construction -- such as the explicit realization of $\fent$ and its compactification as a Noether–Lefschetz locus in $\fttz$, and the construction of the semitoroidal boundary.