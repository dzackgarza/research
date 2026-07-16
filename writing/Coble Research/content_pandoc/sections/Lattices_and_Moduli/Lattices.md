# Lattice Summary

We summarize the lattices that will be relevant to our discussion:

$$
\begin{aligned}
    L &= (22, 0, 0)_3 = U^3 \oplus E_8^2 = \latII_{3, 19} &
    E_{10} &= (10, 0, 0)_1 = U \oplus E_8 = \latI_{1, 9} \\
    S_\En &= (10, 10, 0)_1 = E_{10}(2) &
    T_\En &= (12, 10, 0)_2 = U \oplus E_{10}(2) \\
    S_\Co &= (11, 11, 1)_1 = \gens{-2} \oplus E_{10}(2) &
    T_\Co &= (11,11,1)_2 = \gens{2} \oplus E_{10}(2) \\
    S_{\dP} &= (2,2,0)_1 = U(2) &
    T_{\dP} &= (20, 2, 0)_2 = U \oplus U(2) \oplus E_8^2
\end{aligned}
$$

:::{#lem:primitive_embedding_eta .lemma}

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

:::{#lem:sequence_of_embeddings .lemma}

There is a sequence of primitive embeddings

$$
T_{\Co} \injects T_{\En} \injects T_{\dP} \injects L
$$

which is unique up to
$\Orth(L)$.
In particular, this yields an embedding

$$
\begin{aligned}
\gens{2} \oplus U(2) \oplus E_8(2) &\injects U \oplus U(2) \oplus E_8^2 \\
(h,x,y) & \mapsto (\tilde e + \tilde f, x, y, y)
\end{aligned}
$$

and thus an embedding $F_{\Co} \injects F_{(2,2,0)}$.
:::

:::{.proof}

By [@AEGS23 Lem. 2.4], it suffices to show uniqueness of
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

This embedding is unique since one can write the codomain as
$E_{10}^\perp \oplus E_{10}$.
Similarly, by [@Nik79 Cor. 1.5.2, Thm.
3.6.3], the homomorphism $\Orth(L)\to \Orth(T_\Co)$ is surjective. 
:::

:::{#lem:locally_closed_embedding_BB .lemma}

The embeddings of lattices
$\eta: T_\Co\injects T_\En$ (resp.
$T_{\Co} \injects T_{\dP}$) induce
locally closed embedding $F_\Co \injects F_\En$ (resp.
$F_{\Co} \injects F_{(2,2,0)}$) which extend to a morphisms on the
Baily-Borel compactifications.
:::

:::{.proof}

This follows from [@KK72 §5, Thm.2]. 
:::
