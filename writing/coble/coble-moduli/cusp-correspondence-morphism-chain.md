---
unit: research-program
status: conjectural
tags:
  - coble
  - cusps
  - baily-borel
  - morphisms
---

# The Coble cusp correspondence and the morphism chain {#sec-cusp-correspondence-morphism-chain}

## The chain of morphisms

::: {.proposition #prop:fen2-forgetful-maps title="The two morphisms out of $\fentwo$"}

Let $\fttz=\bD(\tdp)/\Gamma_\dP$ be the moduli space of K3 surfaces of degree $4$ with a del Pezzo involution [@AEGS25, §1, Def. 2.7].

1. The inclusion $\bD(T_\En)\subset\bD(\tdp)$ induces a finite, generically injective morphism $\fentwo\to\fttz$, and $\fentwo$ is the normalization of a closed subvariety of $\fttz$ [@AEGS25, Lemma 2.8].
2. The inclusion $\gent\subseteq\Gamma^K_\En$ of a subgroup of finite index induces a morphism $\fentwo\to F_{(10,10,0)}=\bD(T_\En)/\Gamma^K_\En$ of degree $2^7\cdot17\cdot31$ [@AEGS25, §2.3; @Ste91, Rem. 2.12].
:::

::: {.construction title="The embedding and its two extensions"}

By @lem:locally_closed_embedding_BB, the lattice embeddings $T_\Co\injects\ten$ and $T_\Co\injects\tdp$ induce locally closed embeddings $\fco\injects\fen$ and $\fco\injects\fttz$, which extend to morphisms of Baily--Borel compactifications:
$$
\eta: \bbcpt{\fco} \to \bbcpt{\fen},
\qquad
\tilde\eta: \bbcpt{\fco} \to \bbcpt{\fttz} .
$$
The stratification of $\partial\bbcpt{F^{\mathrm{un}}_\Co}$ is obtained by applying the mirror moves of [@AE22] to $S_{\Co} = (11,11,1)_1$.
On $0$-cusps, $\eta$ induces an injective map from the $527$ $0$-cusps of the stable quotient $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ to the $0$-cusps of $\fen$ of divisibility $2$ (@prop:cusp-map-injective, @prop:cusp-map-not-onto).
:::

## The two cusp identifications

::: {.proposition #prop:fen2-zero-cusp-lattices title="The lattices of the five $0$-cusps of $\fentwo$"}

Let $e\in\ten$ be a primitive isotropic vector, and number the $0$-cusps of $\fentwo$ as in [@Ste91].

1. The lattice $e^{\perp}/e$ is $U(2)\oplus E_8(2)=(10,10,0)_1$ when $e$ represents cusp $1$, and $U\oplus E_8(2)=(10,8,0)_1$ when $e$ represents one of cusps $2$ to $5$ [@AEGS25, Lemmas 3.9, 3.10].
2. The Coxeter diagram of cusp $2$ is the folding of the Coxeter diagram of $(18,0,0)_1$ by the reflection $\alpha_k\mapsto\alpha_{20-k}$ [@AEGS25, Lemma 3.9]. The Coxeter diagrams of cusps $1$, $3$, $4$ and $5$ are foldings of the Coxeter diagram of $(18,2,0)_1$ [@AEGS25, Lemma 3.10].
:::

::: {.corollary #cor:coble-zero-cusp-over-sterk-two-to-five title="The $0$-cusps of $\fentwo$ over the $0$-cusp $(9,9,1)_1$ of $F^{\mathrm{un}}_\Co$"}

Every $0$-cusp of $\fentwo$ over the image in $F^K_\En$ of the $0$-cusp $(9,9,1)_1$ of $F^{\mathrm{un}}_\Co$ is one of cusps $2$ to $5$. The reduced dual complex $\Gamma(\mcz_0)$ of each of these cusps is the disc $\Dc^2$.
:::

::: {.proof}

The morphism $\fentwo\to F^K_\En$ of @prop:fen2-forgetful-maps sends the $0$-cusp of a primitive isotropic vector $e\in\ten$ to the $0$-cusp of the same vector $e$, so it preserves the lattice $e^{\perp}/e$. By @lem:w1_perp_calculation the image of $(9,9,1)_1$ is the $0$-cusp $(10,8,0)_1$ of $F^K_\En$. By @prop:fen2-zero-cusp-lattices the cusps of $\fentwo$ with $e^{\perp}/e=(10,8,0)_1$ are cusps $2$ to $5$. Their dual complexes are listed in @ex:fen2_five_cusps.
:::

::: {.conjecture #conj:coble-zero-cusp-sterk-two title="The Coble $0$-cusp is Sterk cusp $2$"}

The $0$-cusp $(9,9,1)_1$ of $F^{\mathrm{un}}_\Co$ corresponds to cusp $2$ of the cusp diagram of $\fentwo$ [@Ste91].
:::

## Terminal Coble surfaces

::: {.definition title="Terminal"}

A Coble surface is **terminal** when it is not the image of any birational but not biregular morphism from another Coble surface.
The $n=1$ case, the blowup of a plane sextic at $N=10$ ordinary double points (some possibly infinitely near), is terminal.
:::
