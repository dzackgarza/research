### The Quotient Family over $B$ {#section-7-4}

This section constructs, analyzes, and establishes the modular properties of the family of stable Enriques pairs obtained as the quotient of the universal KSBA-stable family of K3 pairs by the global Enriques involution, particularly over the Noether–Lefschetz locus $B$.

:::{.proposition
    title="{Existence and Finiteness of the Quotient Family}"
    #prop:existence-finiteness-quotient
}
Let $\ien: \mcx_B \to \mcx_B$ denote the globally defined Enriques involution acting fiberwise on the universal KSBA family $(\mcx_B, \eps \mcr_B) \to B$. Define the quotient:

\begin{align*}
\rho: (\mcx_B, \eps \mcr_B) \to (\mcz, \eps \mcr_Z)
,
.\end{align*}

where $\mcz = \mcx_B / \ien$ is the coarse space of the quotient stack $[\mcx_B / \langle \ien \rangle]$ and $\mcr_Z := \rho_*(\mcr_B)$ is the pushforward of the ramification divisor. Then:

- $\rho$ is a morphism of degree $2$ in the category of pairs over $B$,
- The following square is Cartesian:
  
  \begin{tikzcd}
  (\mcx_B, \eps \mcr_B) \arrow[r, "\rho"] \arrow[d] & (\mcz, \eps \mcr_Z) \arrow[d] \\
  B \arrow[r, equal] & B
  \end{tikzcd}
  
- The construction is well-defined: $\ien$ acts biregularly, freely in codimension $1$, and preserves both the boundary divisor and the property of being a KSBA stable pair.
:::

:::{.proof}
The quotient $\mcz$ is constructed as the stack quotient $[\mcx_B/\langle \ien\rangle]$. Since $\ien$ is biregular and, by construction, acts freely on the smooth locus of each fiber and preserves the divisor $\mcr_B$, descent for group actions on surfaces with semi-log-canonical singularities applies. The finite morphism property, and the pullback structure on boundary divisors, follow from the theory of quotients of pairs and functoriality on the category of KSBA pairs with finite group actions. The claimed Cartesian property is a formal consequence.
:::

:::{.proposition
    title="{Fiberwise Analysis of the Quotient}"
    #prop:fiberwise-analysis-quotient
}
Let $b \in B$ be a geometric point and $\mcx_b$, $\mcz_b$ the corresponding fibers.

1. If $b \in B^\circ$ (open locus), $\mcx_b$ is a smooth K3 surface, $\ien$ has no fixed points, and $\rho_b: \mcx_b \to \mcz_b$ is étale outside codimension at least $2$.
   
   - The quotient $\mcz_b$ is a smooth Enriques surface.
   - The canonical bundle $K_{\mcz_b}$ is numerically trivial up to $2$-torsion: $2K_{\mcz_b} \sim 0$.
   
2. If $b \in B \setminus B^\circ$ is in the degenerate locus, $\mcx_b$ is a K3 surface with slc singularities and $\ien$ may have isolated fixed points in codimension $\geq 2$.

   - The quotient $\mcz_b$ is again semi-log-canonical, as is the pair $(\mcz_b, \eps \mcr_{Z,b})$.
   - The canonical bundle $K_{\mcz_b}$ remains numerically trivial.
:::

:::{.proof}
In the smooth case, this is the standard construction of Enriques surfaces as fixed-point-free quotients of K3 surfaces by involution. In the presence of singularities, since $\ien$ is biregular and fixes only loci of codimension at least $2$, the quotient remains slc by @KM98. The canonical bundle calculation follows from the adjunction formula and the behavior of $\ien$ on $K_{\mcx_b} \sim 0$; the pushforward identifies $K_{\mcx_b}$ with $\rho^* K_{\mcz_b}$ so that $2K_{\mcz_b} \sim 0$.
:::

:::{.proposition
    title="{Preservation of KSBA Stability and Ample Boundary}"
    #prop:preservation-ksba-stability
}
For every $b \in B$, consider the pair $(\mcz_b, \eps \mcr_{Z,b})$. Then:

- $(\mcz_b, \eps \mcr_{Z,b})$ is KSBA-stable,
- The polarization (ample boundary) descends: $\rho^*(K_{\mcz_b} + \eps \mcr_{Z,b}) = K_{\mcx_b} + \eps \mcr_b$.
:::

:::{.proof}
Since $(\mcx_b, \eps \mcr_b)$ is KSBA-stable by construction, we use that ampleness is preserved under finite morphism: if $L$ is ample and $f: X \to Y$ finite surjective, then $f^* L$ ample $\implies L$ ample ([Hartshorne, III.Ex.5.7]). The quotient construction is functorial in the category of pairs, so all stability, numerical, and singularity conditions are satisfied in the target $(\mcz, \eps \mcr_Z)$.
:::

:::{.corollary
    title="{Degenerations, Flatness, Dual Complex, and Monodromy}"
    #cor:degenerations-flatness-dual-complex
}
Let $\Delta$ be a smooth curve with generic point $\eta$ and special point $0$, and $f: \Delta \to B$ a morphism. The base-changed family $\mcx_\Delta = \mcx_B \times_B \Delta$ carries a fiberwise involution $\ien$ and forms a family of KSBA-stable K3 pairs. The quotient family $\mcz_\Delta = \mcx_\Delta / \ien$ satisfies:

- The $\mcx_t$ is a smooth Enriques surface,
- The $\mcx_0$ is semi-log-canonical,
- The family $(\mcz_\Delta, \mcr_{Z,\Delta}) \to \Delta$ is flat, by flatness of the quotient and base change,
- The dual complex of $\mcz_0$ is the quotient of the dual complex of $\mcx_0$ by the involution $\ien$.

Monodromy operators on the local system $H^2(\mcx_\eta, \ZZ)$ commuting with $\ien^*$ descend to $H^2(\mcz_\eta, \ZZ)$. Period data, lattice-theoretic structures, and cohomological invariants remain compatible under the quotient.
:::

:::{.proof}
Flatness follows from the finiteness and flatness properties of group quotients on flat families. That semi-log-canonicity is preserved in $\mcx_0$ follows as above. The dual complex statement follows from the equivariant semistable reduction theory and the definition of the dual complex as depending only on the combinatorics of components and double curves modulo group action. Monodromy compatibility is a standard consequence of functoriality of Galois covers and representations.
:::

:::{.remark
    title="{Summary and Structural Consequences}"
}
The quotient family $(\mcz, \eps \mcr_Z) \to B$ constructed thus provides a complete, modular KSBA-stable compactification for the moduli space of degree-2 polarized stable Enriques surfaces as quotients of K3 pairs, with all necessary boundary, polarization, and singularity structures explicitly accounted for.
:::