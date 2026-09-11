# Period domain embeddings and normalization

We summarize the lattices that will be relevant to our discussion:

$$
\begin{aligned}
    \lkt &= (22, 0, 0)_3 = U^3 \oplus E_8^2 = \latII_{3, 19} &
    E_{10} &= (10, 0, 0)_1 = U \oplus E_8 = \latII_{1, 9} \\
    S_\En &= (10, 10, 0)_1 = E_{10}(2) &
    T_\En &= (12, 10, 0)_2 = U \oplus E_{10}(2) \\
    S_\Co &= (11, 11, 1)_1 = \gens{-2} \oplus E_{10}(2) &
    T_\Co &= (11,11,1)_2 = \gens{2} \oplus E_{10}(2) \\
    S_{\dP} &= (2,2,0)_1 = U(2) &
    T_{\dP} &= (20, 2, 0)_2 = U \oplus U(2) \oplus E_8^2
\end{aligned}
$$

::: {.Lemma #lem:primitive_embedding_eta}

Writing

$$
\begin{aligned}
T_\Co = \gens{2} \oplus E_{10}(2) &= \gens{h, e', f',\alpha_1,\cdots, \alpha_8} \\
T_\En = U \oplus E_{10}(2) &= \gens{\tilde e,\tilde f,\tilde e',\tilde f',\tilde \alpha_1,\cdots,\tilde \alpha_8},
\end{aligned}
$$

there is an embedding of lattices $T_\Co \injects T_\En$:

$$
\begin{aligned}
\eta: \gens{2} \oplus E_{10}(2) &\to U \oplus E_{10}(2) \\
(h, x) &\mapsto (\tilde e + \tilde f, x)
\end{aligned}
$$

which sends the generator $h$ of $\gens{2}$ to $\tilde e+\tilde f\in U$ and is
the identity on the $E_{10}(2)$ summand.
Since $\coker \eta$ is torsionfree, $\eta$ is a primitive embedding.
:::

::: {.Lemma #lem:sequence_of_embeddings}

There is a sequence of primitive embeddings

$$
T_{\Co} \injects T_{\En} \injects T_{\dP} \injects \lkt
$$

which is unique up to
$\Orth(\lkt)$.
In particular, this yields an embedding

$$
\begin{aligned}
\gens{2} \oplus U(2) \oplus E_8(2) &\injects U \oplus U(2) \oplus E_8^2 \\
(h,x,y) & \mapsto (\tilde e + \tilde f, x, y, y)
\end{aligned}
$$

and thus an embedding $F_{\Co} \injects F_{(2,2,0)}$.
:::

::: {.proof}

By [@AEGS25 Lem. 2.4], it suffices to show uniqueness of
$S_{\En} \injects S_{\Co}$, i.e.

$$
E_{10}(2) \injects \gens{-2}\oplus E_{10}(2)
,
$$

or equivalently by untwisting,

$$
E_{10} \injects \gens{-1}\oplus E_{10}
.
$$

This embedding is unique because $E_{10} = U \oplus E_8$ is unimodular.
A primitively embedded unimodular sublattice splits its ambient lattice
(\longref{prop:unimodular-splits}), so the codomain of any primitive embedding of
$E_{10}$ is $E_{10}\oplus E_{10}^{\perp}$.
The gluing datum of such an embedding is the graph of an isometry between a
subgroup of $A_{E_{10}}$ and a subgroup of $A_{E_{10}^\perp}$
(\longref{rmk:embedding-gluing-data}), and $A_{E_{10}} = 0$, so that datum is
trivial and the embedding is determined by the isometry class of the complement.
Similarly, by [@Nik80 Cor. 1.5.2, Thm.
3.6.3], the homomorphism $\Orth(\lkt)\to \Orth(T_\Co)$ is surjective.
:::

::: {.Lemma #lem:locally_closed_embedding_BB}

The embeddings of lattices
$\eta: T_\Co\injects T_\En$ (resp.
$T_{\Co} \injects T_{\dP}$) induce
locally closed embedding $F_\Co \injects F_\En$ (resp.
$F_{\Co} \injects F_{(2,2,0)}$) which extend to a morphisms on the
Baily-Borel compactifications.
:::

::: {.proof}

This follows from [@KK72 §5, Thm.2].
:::

::: {.Theorem #thm:normalization}

$F_{\Co}$ is the normalization of a closed subvariety of $F_{\En}$.
:::

::: {.proof}

It suffices to show that
$D(T_{\Co})/\Orth^+(T_{\Co})^* \to D(T_{\En})/\Orth^+(T_{\En})^*$ is a finite morphism
which is generically injective.
The lattice embedding $T_{\Co}\injects T_{\En}$ induces an injective morphism
$D(T_{\Co}) \injects D(T_{\En})$.
It remains to show that the stabilizer of $T_{\Co}$ in $\Orth(T_{\En})$ is
precisely $\Orth(T_{\Co})$ and the morphism is finite.

This morphism is finite because...

The stabilizer statement follows from...
:::

::: {.Question}
I don't know how to prove this. Maybe one should embed into $T_{\dP}$ instead to get the stabilizer statement? Finiteness is still unclear. Maybe one can use finite $\iff$ proper and finite fibers, using Stacks tag 02LS. This can be checked Zariski locally?
:::

::: {.Question}
Maybe this can be proved using Zariski's main theorem: a birational morphism to a normal variety with finite fibers is an isomorphism onto an open subset. Is this morphism birational? What are the fibers, and how can we tell if they are finite?
:::

::: {.Remark #rmk:descent-of-an-equivariant-inclusion}
### What the stabilizer statement has to supply

The stabilizer step of \longref{thm:normalization} is one instance of a general
criterion for descending a map to a pair of quotients.
Let $f\colon A\injects B$ be an inclusion of sets, and let $G_A$ and $G_B$ be
groups acting on $A$ and on $B$.
Then $f$ descends to a map of orbit spaces
$$
\bar f\colon G_A\backslash A \to G_B\backslash B
$$
precisely when every element of $G_A$ acts on $A$ as the restriction of some
element of $G_B$ preserving $f(A)$, that is when
$$
\im\bigl(G_A\to\Aut(A)\bigr)
\;\subseteq\;
\im\bigl(\Stab_{G_B}(f(A))\to\Aut(f(A))\bigr)
.
$$
For the case at hand, $A = D(T_\Co)$ with $G_A = \Orth^+(T_\Co)^*$ and
$B = D(T_\En)$ with $G_B = \Orth^+(T_\En)^*$, so what is needed is that every
isometry of $T_\Co$ in $G_A$ extends to an isometry of $T_\En$ preserving
$T_\Co$.
The criterion is a containment, not an equality: the stabilizer of $T_\Co$ in
$\Orth(T_\En)$ may restrict to a group strictly larger than $\Orth(T_\Co)$
without obstructing the descent.
What a strictly larger restriction can cost is injectivity, since two
$G_A$-orbits may then be identified in $G_B\backslash B$; that is the separate
burden carried by the generic injectivity in the proof above.
:::
