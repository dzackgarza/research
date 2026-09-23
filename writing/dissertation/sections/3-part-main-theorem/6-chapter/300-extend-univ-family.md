### Extension of $\ien$ to the Universal Family over $B$ {#section-7-3}

In this section, we construct and analyze the global extension of the Enriques involution $\ien$ to the universal KSBA family of K3 surfaces over the Noether–Lefschetz locus $B \subset \cpt{\fttz}$. Unless stated otherwise, all notation, functors, and structures are as established in the preceding sections.

#### The Universal Family in the KSBA Context

Let $\cpt{\fttz}$ be the KSBA compactification of the moduli space of degree-4 polarized K3 surfaces with a specified nonsymplectic involution $\idp$. There exists a universal family of stable pairs

\begin{align*}
\pi: (\mcx, \epsilon\mcr) \to \cpt{\fttz}
.\end{align*}

satisfying:

- The total space $\mcx$ is flat and proper over $\cpt{\fttz}$, specializing to smooth K3 surfaces over a dense open locus and possibly degenerating to semi-log-canonical surfaces in the boundary.
- The divisor $\mcr \subset \mcx$ is the ramification locus of $\idp$, defined as the fixed locus of the involution.
- The pair structure is preserved globally, including at all singular fibers.

:::{.proposition
    title="{Existence and Uniqueness of the Universal Family with Involution}"
    #prop:existence-uniqueness-universal-family
}
The existence, functoriality, and separatedness of the universal family $(\mcx, \epsilon\mcr)$, including a prescribed pair of commuting involutions, are standard consequences of the general theory of KSBA moduli of stable surface pairs with finite automorphism group action acting fiberwise and preserving the pair. Explicitly, the automorphism scheme is proper and separated, and such an involution preserving the pair extends uniquely to the stable limit in families.
:::

#### Restriction to the Noether–Lefschetz Locus

Let $B \subset \cpt{\fttz}$ be the Zariski closure of the Noether–Lefschetz locus parameterizing degree 2 polarized Enriques surfaces constructed in the previous step. Consider the base change

\begin{align*}
\pi_B: (\mcx_B, \epsilon \mcr_B) \to B
.\end{align*}

where $\mcx_B = \mcx \times_{\cpt{\fttz}} B$ and $\mcr_B = \mcr|_{\mcx_B}$. 
This family retains the following structure:

- Each geometric point $b \in B$ parametrizes a (possibly degenerate) K3 surface equipped with a degree-4 polarization and a prescribed involution $(\idp)_b$.

- Over the open locus $\open{B}$ parameterizing smooth K3 surfaces, each fiber $\mcx_b$ admits a del Pezzo involution $(\idp)_b$ with ramification divisor $\mcr_b$, as well as a fixed-point-free Enriques involution $(\ien)_b$.

For all $b \in \open{B}$, the involutions $(\idp)_b$ and $(\ien)_b$ commute and both preserve the polarized pair $(\mcx_b, \mcr_b)$. These involutions are compatible with the moduli-theoretic structure and cover the appropriate automorphism data underlying the Enriques construction.
We now globalize the involution $\ien$ over the entire family $(\mcx_B, \mcr_B)$, including all degenerate fibers.

:::{.theorem
    title="{Global Extension of the Enriques Involution}"
    #thm:global-extension-enriques-involution
}
There exists a unique global involution

\begin{align*}
\ien : \mcx_B \to \mcx_B
.\end{align*}

with the following properties:

- $\ien$ restricts over $\open{B}$ to the fixed-point-free Enriques involution on each smooth fiber.
- $\ien \circ \idp = \idp \circ \ien$ fiberwise on all of $\mcx_B$.
- $\ien(\mcr_B) = \mcr_B$.
- For every $b \in B$, the restriction $(\ien)_b$ is fixed-point-free on the smooth locus of the fiber $\mcx_b$.
:::

:::{.proof}
Over $\open{B}$ the involution $\ien$ is part of the moduli data. Since the universal family in the KSBA moduli problem is separated and proper for automorphism group actions preserving the pair structure, any automorphism defined on the $\mcx_t$ extends uniquely to the $\mcx_0$s, as in the valuative criterion for the separatedness of the moduli functor. The extension respects all divisor and commutativity data because these are closed conditions on the moduli stack of stable pairs with automorphism. Functoriality and the rigidity of automorphism schemes in the KSBA theory propagate these compatibilities to all fibers.
:::

Once constructed, this global involution $\ien$ satisfies all required compatibilities:

- Commutativity $\ien \circ \idp = \idp \circ \ien$ holds everywhere. This is checked on $\open{B}$ and then globalized via the uniqueness of the extension.

- Preservation of the ramification divisor: $\ien(\mcr_B) = \mcr_B$. Again, this is a closed condition propagated by the structure of the moduli functor.

- On any smooth fiber, $(\ien)_b$ is fixed-point-free, as dictated by the monodromy and period data of the Enriques surface. In degenerate fibers, fixed points may occur in higher codimension, but the geometric meaning of the involution is unambiguous due to the rigidity of the automorphism structure and the stability properties of the KSBA compactification.


For clarity in all subsequent arguments, we adopt the following consistent notation:

- $(\mcx, \mcr)$ is the universal KSBA family over $\cpt{\fttz}$;

- $(\mcx_B, \mcr_B)$ is the restriction of the family to the Noether–Lefschetz locus $B$;

- $\idp$ is the global del Pezzo involution acting on each fiber;

- $\ien$ is the global Enriques involution, commuting with $\idp$ and preserving the pair;

- For each geometric point $b \in B$, the fiber $\mcx_b$ is equipped with involutions $(\idp)_b, (\ien)_b$, and the ramification divisor is $\mcr_b$.