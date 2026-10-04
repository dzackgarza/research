### Finiteness by Kulikov Models and a Coarsening Argument {#section-7-6}



We now prove a crucial structural property of the classifying morphism

\begin{align*}
\phi : \normalize{B} \to \cpt{\fentwo}
.\end{align*}

constructed in previous sections: namely, that $\phi$ is finite.
This assertion is the final step needed for modular identification of the compactified moduli of degree-2 polarized stable Enriques pairs via the period map and semitoroidal construction.

#### Semifan Comparison and Finiteness: Addressing the Critical Gap

::: {.lemma title="{Semifan Comparison}" #lem:semifan-comparison}
Let $\semitorcpt{\fentwo}$ be the semitoroidal compactification defined using the five semifans $\semifan{F} = \{\semifan{F}_k\}_{k=1}^5$ as in @AEGS25. There exist semifans $\semifan{G} = \{\semifan{G}_k\}_{k=1}^5$ associated with the normalization of the KSBA compactification $\ksbacpt{\fentwo}$ such that:

1. $\ksbacpt{\fentwo} = \semitorcpt{\fentwo}$ if and only if $\semifan{G}_k = \semifan{F}_k$ for all $k$.

2. Each $\semifan{G}_k$ is a coarsening of $\semifan{F}_k$.

3. The morphism $\phi$ is finite if and only if all $\semifan{G}_k = \semifan{F}_k$.
:::

::: {.proof}
Any KSBA compactification with recognizable divisors admits a semitoroidal structure determined by a tuple of semifans $\semifan{G}_k$.
By construction, these semifans are universal for the normalization and can only coarsen the initially defined Coxeter semifans $\semifan{F}_k$.
Explicitly, a cone in $\semifan{F}_k$ may be identified in $\semifan{G}_k$, corresponding to an identification of the associated boundary stratum in the KSBA moduli space.

The crux is that given any coarsening, there exists some codimension-one cone $\sigma$ in $\semifan{F}_k$ (for some $k$), a common face of two maximal cones $\tau_1, \tau_2$, that is identified in $\semifan{G}_k$.
Points corresponding to distinct degenerations -- specifically, configurations differing by the presence of a double curve in the dual complex -- would thus be glued together in the target.
Thus, $\phi$ is finite if and only if no such coarsening occurs, that is, all semifans agree.
This reduces the global finiteness to the combinatorial modularity of the boundary fans, with no possible positive-dimensional fibers away from the boundary: by normality, properness, and functoriality of the compactification morphisms, any such fiber must arise from a non-separated boundary stratum; but this is precisely what semifan agreement guarantees cannot occur.
:::

#### Maximality, Moduli, and Injectivity: Scheme-Theoretic Proof

::: {.definition title="{Maximality of Degenerations}" #def:maximality-degenerations}
A degeneration $(X_0, \epsilon R_0)$ of K3 pairs is **maximal** if its dual complex realizes the largest possible number of vertices (components) and edges (double curves) among all degenerations with the same monodromy data.
The analogous definition applies for Enriques degenerations $(Z_0, \epsilon R_{Z,0})$.
:::

::: {.proposition title="{The Double Curve Constraint}" #prop:double-curve-constraint}
Let $(X_0, \epsilon R_0)$ be a degeneration of K3 pairs with a fixed-point-free Enriques involution $\ien$, with quotient $(Z_0, \epsilon R_{Z,0})$.
Then:

- The number of irreducible components of $Z_0$ is the number of $\ien$-orbits of components of $X_0$;

- The number of double curves in $Z_0$ is the number of $\ien$-orbits of double curves in $X_0$;

- $(Z_0, \epsilon R_{Z,0})$ is maximal if and only if $(X_0, \epsilon R_0)$ is maximal.
:::

::: {.proof}
This is established by @AEGS25 via an explicit analysis of half-divisor models and their quotients.
The scenarios at each cusp of the compactification -- Type $\mathrm{III}$ cusps (with dual complex $\RP^2$ or $\DD^2$) and Type $\mathrm{II}$ (dual complex $\DD^1$) -- are treated explicitly:

- At cusp $1$ (Type $\mathrm{III}$), all components of $\mcx_0$ map to unique components of $V_i$.

- At cusps $2,3,4,5$ (Type $\mathrm{III}$), the involution may act with isolated fixed points on components or double curves.

- In Type $\mathrm{II}$ degenerations, $\ienzero$ may act by reflection, or as a fixed-point-free involution, or as an elliptic involution with explicit fixed locus on certain double curves.

By @AEGS25, the boundary degenerations (up to isomorphism of stable pairs) are fully classified by the monodromy and dual complex, which is entirely encoded in the semifan.
The folding operations and passage to quotients by $\ien$ preserves this relation.
:::

#### The Core Finiteness-Injectivity Argument

::: {.theorem title="{No Coarsening Occurs}" #thm:no-coarsening}
For each $k \in \{1,2,3,4,5\}$, the boundary semifans satisfy $\semifan{G}_k = \semifan{F}_k$.
:::

::: {.proof}
Suppose, for contradiction, that for some $k$ the semifan $\semifan{G}_k$ is a proper coarsening of $\semifan{F}_k$, and let $\sigma$ be a codimension-one cone which is a face of two maximal cones $\tau_1, \tau_2$ in $\semifan{F}_k$ that become identified in $\semifan{G}_k$.
These maximal cones parameterize distinct maximal degeneration types, specifically boundary degenerations where the dual complex differs by exactly one double curve -- maximality vs. non-maximality for a fixed monodromy.
Under the period map, points of $\normalize{B}$ mapping to $\sigma$ correspond to K3 degenerations $(X_0, \epsilon R_0)$ missing a single double curve from the maximal configuration; the quotient $(Z_0, \epsilon R_{Z,0})$ encodes this as well.
But in the compactification, KSBA theory asserts that each dual complex arises as a distinct boundary stratum, and maximality is a complete moduli invariant -- distinct configurations cannot be identified.
Therefore, identification of such cones in a coarsened semifan would force positive-dimensional or non-separated fibers, contradicting the representability and separatedness of the moduli functor.
Thus, no coarsening occurs, and $\semifan{G}_k = \semifan{F}_k$ for all $k$.
:::

#### Properness, Quasi-finiteness, and Conclusion

::: {.corollary title="{Finiteness of the Classifying Map}" #cor:finiteness-classifying-map}
By the previous lemma, the boundary stratifications, as encoded by semifans, agree identically.
Therefore, the morphism $\phi: \normalize{B} \to \cpt{\fentwo}$ is finite.
:::

::: {.proof}
It remains to ensure that no positive-dimensional fibers exist away from the boundary and that the map is proper.
Since both $\normalize{B}$ and $\cpt{\fentwo}$ are normal, proper algebraic spaces (by the properness of the moduli of stable pairs), and semifan agreement guarantees finite fibers at the boundary, the only possible source of positive-dimensional fibers would be in the interior.
However, in the open moduli, the period map is finite (by Torelli for K3s, and the specific construction of $\halfpd{\ten}$). Hence the morphism is quasi-finite and proper, and by Zariski's Main Theorem, $\phi$ is finite.
:::
