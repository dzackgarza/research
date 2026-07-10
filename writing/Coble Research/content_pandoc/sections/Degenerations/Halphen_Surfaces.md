# Halphen Surfaces

::: {.remark}

It is well-known (e.g. as in [@DZ99] and [@CDL24 Ch.5 §6]) that a Halphen
surface of index $n$ is a relative minimal elliptic surface $S$ with $F_1$ the
divisor class of a fibre satisfying $F_1 = -n K_S$.
By [@DZ99 §2.4], an index 1 Halphen surface admits a section and has no multiple
fibres, and an index 2 Halphen surface has a unique double fibre $2F_1$.
By [@DK24 Prop. 9.1.4], any terminal Coble surface of K3 type is
isomorphic to one of the following:

- A blowup of a Halphen surface of index 1 at two singular points of two simple
  reduced fibres of types $\tilde A_k, \tilde A_m$ where $k+m\leq 8$, or

- A blowup of a Halphen surface of index 2 at one singular point of a single
  simple reduced fibre of type $\tilde A_n$ where $n\geq 8$

This is used in [@DK24 Prop. 9.1.5] to show that $K_S^2 \geq -10$, and
since $K_S^2 = -n$, this shows that such Coble surfaces have at most ten
boundary components.

Of most immediate relevance to us is the case considered in [@Cob19] where
$n=1$.
Following [@DK24 Ex. 9.1.7], the image $W \da V(f_6) \da \eta(C)$ is an
irreducible plane sextic with 10 $A_1$ singularities[^5].
One can find a cubic $V(f_3)$ passing through nine of them and form a pencil
$V(\lambda f_6 + \mu f_3^2)$ such that the minimal resolution of its basepoints
is a Halphen surface of index 2. The proof of [@DK24 Prop. 9.1.8]
indicates that the moduli space of general Halphen surfaces of index 2 has
dimension 9.

:::

The following is [@CDL24 Prop. 3.1]:

::: {#lem:coble_halphen_blowdown .lemma}

Let $X$ be a Coble surface and $\pi_{E}: X \to Y$ be the blowing down of
a (-1)-curve E.
Then

- $Y$ is a Halphen surface of index 2;

- $C$ is the proper transform of the fiber $F$ containing $y_{0}=\pi_{E}(E)$;

- the fiber $F$ is irreducible, and $y_{0}$ is its unique singular point.

Conversely, the blow-up of a singular point of an irreducible non-multiple fiber
of a Halphen surface of index 2 is a Coble surface.

:::

::: {.remark}

Why introduce Halphen surfaces? I conjecture that the geometric construction(s)
above yield some kind of correspondence between moduli spaces of Coble surfaces
with $n$ boundary components and the various moduli spaces of index 2 Halphen
pencils on the $g=0$ line of Nikulin's triangle diagram of 2-elementary
lattices.
Regarding the coarse spaces as period domains attached to lattices, the lattices
match up precisely; see \cref{table:coble-lattices}.
Applications of mirror moves indicate that the cusp diagrams would
correspondingly coincide as well.

:::

[^5]: $A_1$ or $A_2$ singularities.
