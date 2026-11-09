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

::: {.remark title="The four-term chain"}

The moduli spaces are related by the maps
$$
\fco \too \fen \too \fentwo \longleftarrow \fttz ,
$$
where $\fttz$ is the moduli space of quartic hyperelliptic K3 surfaces of [@AEGS25], and the normalized KSBA compactification of $\fentwo$ is a semitoroidal compactification [@AEGS25 Thm. 1].
:::

::: {.construction title="The embedding and its two extensions"}

By @lem:locally_closed_embedding_BB, the lattice embeddings $T_\Co\injects\ten$ and $T_\Co\injects\tdp$ induce locally closed embeddings $\fco\injects\fen$ and $\fco\injects\fttz$, which extend to morphisms of Baily--Borel compactifications:
$$
\eta: \bbcpt{\fco} \to \bbcpt{\fen},
\qquad
\tilde\eta: \bbcpt{\fco} \to \bbcpt{\fttz} .
$$
The stratification of $\partial\bbcpt{\fco}$ is obtained by applying the mirror moves of [@AE22] to $S_{\Co} = (11,11,1)_1$.
On $0$-cusps, $\eta$ induces an injective map from the $527$ $0$-cusps of $\fco$ to the $0$-cusps of $\fen$ of divisibility $2$ (@prop:cusp-map-injective, @prop:cusp-map-not-onto).
:::

## The two cusp identifications

::: {.remark title="Coble cusps under the extension to $\fttz$"}

Under $\tilde\eta$, the $0$-cusp of the vector $v_1$ of @lem:divisibilityTcoOne maps to the $0$-cusp $(18,0,0)_1 = U\oplus E_8^{\oplus 2}$ of $\fttz$, and the $1$-cusp of $J$ maps to a $1$-cusp with boundary lattice $(16,0,0)_0\cong D_{16}^+$ (@lem:cusp_map_dP, @prop:rank_16_cusp_D16).
:::

::: {.conjecture #conj:coble-zero-cusp-sterk-two title="The Coble $0$-cusp is Sterk cusp $2$"}

The Coble $0$-cusp corresponds to cusp $2$ of the cusp diagram of $\fentwo$ [@Ste91].
:::

::: {.remark}

The five $0$-cusps of $\fentwo$ have boundary lattices $(10,10,0)_1$ for cusp $1$ and $(10,8,0)_1$ for cusps $2$ to $5$ [@AEGS25 Lemmas 3.9, 3.10]. The Coble $0$-cusp maps to the $0$-cusp $(10,8,0)_1$ of $\fen$ (@lem:w1_perp_calculation), so a cusp of $\fentwo$ over its image is one of cusps $2$ to $5$, whose integral-affine structures are all $\DD^2$ (@ex:fen2_five_cusps). Cusp $2$ is the only one of these folded from $(18,0,0)_1$, by the reflection $\alpha_k\mapsto\alpha_{20-k}$ of its Coxeter diagram [@AEGS25 Lemma 3.9].
:::

## Orbits of isotropic sublattices

::: {.remark}

The $0$-cusps and $1$-cusps of $\fco$ are the $\Gamma_\Co$-orbits of primitive isotropic lines and planes of $T_\Co$, where $\Gamma_\Co = \Orth^+(T_\Co)^*$. By @thm:cusp-lifting these orbits are in bijection with finite orbit sets in the discriminant group $A_{T_\Co}$: there are $527$ orbits of lines and $189\,720$ orbits of planes.
:::

::: {.remark title="The GIT model"}

The moduli space of Coble surfaces obtained by blowing up the ten nodes of a rational plane sextic is a locally closed subvariety of the GIT quotient $(\PP^2)^{10}\modmod\PGL_3$, and an open subset of $\bD(T_\Co)/\Orth(T_\Co)$ [@DK13 §3].
:::

## Terminal Coble surfaces

::: {.definition title="Terminal"}

A Coble surface is **terminal** when it is not the image of any birational but not biregular morphism from another Coble surface.
The $n=1$ case, the blowup of a plane sextic at $N=10$ ordinary double points (some possibly infinitely near), is terminal.
:::

Related: [The research program for $F_{\Co,n}$, $2 \leq n \leq 10$](#sec-coble-families-research-program), [Candidate isotropic vectors in $T_{\Co}$](#sec-coble-lattice-isotropic-candidates), [Moduli of index 2 Halphen and rational elliptic surfaces](#sec-halphen-index-2-moduli-program).
