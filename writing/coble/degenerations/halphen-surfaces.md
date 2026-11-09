# Halphen surfaces {#sec-halphen-surfaces}

::: {.remark}

It is well-known (e.g. as in [@DZ99] and [@CDL25 Ch.5 §6]) that a Halphen surface of index $n$ is a relative minimal elliptic surface $S$ with $F_1$ the divisor class of a fibre satisfying $F_1 = -n K_S$.
By [@DZ99 §2.4], an index 1 Halphen surface admits a section and has no multiple fibres, and an index 2 Halphen surface has a unique double fibre $2F_1$.
By [@DK25 Prop. 9.1.4], any terminal Coble surface of K3 type is isomorphic to one of the following:

- A blowup of a Halphen surface of index 1 at two singular points of two simple reduced fibres of types $\tilde A_k, \tilde A_m$ where $k+m\leq 8$, or

- A blowup of a Halphen surface of index 2 at one singular point of a single simple reduced fibre of type $\tilde A_n$ where $n\geq 8$

This is used in [@DK25 Cor. 9.1.5] to show that $K_S^2 \geq -10$, and since $K_S^2 = -n$, this shows that such Coble surfaces have at most ten boundary components.

Of most immediate relevance to us is the case considered in [@Cob19] where $n=1$.
Following [@DK25 Ex. 9.1.7], the image $W \definedas V(f_6) \definedas \eta(C)$ is an irreducible plane sextic with 10 $A_1$ singularities (or $A_2$ singularities in the indicated variant). One can find a cubic $V(f_3)$ passing through nine of them and form a pencil $V(\lambda f_6 + \mu f_3^2)$ such that the minimal resolution of its basepoints is a Halphen surface of index 2. A terminal Coble surface $V$ of K3 type with $n$ boundary components $C$ has $h^1(\Theta_{V/k}) = 10+2n$ [@DK25 Prop. 9.1.8] and $h^1(\Theta_{V/k}(-C)) = 10-n$ [@DK25 Rem. 9.1.9]; for $n=1$ the number of moduli is $9$, which is also the number of moduli of general Halphen surfaces of index 2 [@DK25 Rem. 9.1.9].
:::

The following is [@CD12 Prop. 3.1]:

::: {.lemma #lem:coble_halphen_blowdown title="Cobles to Halphens"}

Let $X$ be a Coble surface and $\pi_{E}: X \to Y$ be the blowing down of a (-1)-curve E. Then

- $Y$ is a Halphen surface of index 2;

- $C$ is the proper transform of the fiber $F$ containing $y_{0}=\pi_{E}(E)$;

- the fiber $F$ is irreducible, and $y_{0}$ is its unique singular point.

Conversely, the blow-up of a singular point of an irreducible non-multiple fiber of a Halphen surface of index 2 is a Coble surface.
:::

::: {.proof}

Let $C$ be the anti-bicanonical curve of the Coble surface $X$, so that $|-2K_X|=\{C\}$ and $C$ is a sum of $(-4)$-curves.

*$C$ passes through $y_0$. *
The curve $C$ is the fixed curve of the involution on the K3 cover, and $E$ is a $(-1)$-curve disjoint from $C$: a curve meeting $C$ would meet $-2K_X$ positively and, being a $(-1)$-curve, would have to be a component of $|-2K_X|$, which is a sum of $(-4)$-curves.
So $E$ contracts and $C$ maps to a curve $F=\pi_E(C)$ on $Y$ passing through $y_0=\pi_E(E)$, which is therefore a singular point of $F$.

*The anti-bicanonical class.*
By adjunction for the blowup, $K_X=\pi_E^*(K_Y)+E$ and $C=\pi_E^*(F)-mE$ where $m=C\cdot E$ is the multiplicity of $F$ at $y_0$.
From $-2K_X=C$,
$$
-2\pi_E^*K_Y-2E=\pi_E^*F-mE,
$$
which forces $m=2$ and $F=-2K_Y$: so $F\in|-2K_Y|$, the point $y_0$ is a double point of $F$, and $\pi_E^*(F)=C+2E$.

*$F$ is the non-multiple fibre and $Y$ is Halphen of index $2$.*
Since $C^2=-4$ and $C\cdot E=0$, the projection formula gives $F^2=\pi_E^*F\cdot\pi_E^*F=C^2+4E^2=-4-4=-8$; and $F$ is connected because $C$ is, the fibers of $\pi_E$ other than $E$ being points.
So $F$ is an irreducible curve of arithmetic genus $1$ — adjunction, $2p_a-2=F^2+K_Y\cdot F=-8-F^2/2=-8+4=-4$, giving $p_a=1$ — and its self-intersection is $0$ on the elliptic fibration obtained by completing $|-2K_Y|=|F|$ to a pencil.
Hence $F$ is a fibre of the Halphen fibration, and it is non-multiple because $2F$ is not a member of $|-2K_Y|$: it is $2$ times the unique member, so the fibration has index $2$ and $F$ is its non-multiple fibre.

*Conversely.*
If $F$ is an irreducible non-multiple fibre of a Halphen fibration of index $2$ on $Y$ and $y_0\in F$ is a singular point, then $\pi_E$ the blowup of $y_0$ has $K_X=\pi^*K_Y+E$ and $|-2K_X|\ni\pi^*F-2E$; the proper transform $\pi^*F-2E$ has square $F^2-4=-4$ and arithmetic genus $1$ by adjunction, so it is a $(-4)$-curve, and the surface $X$ has an effective anti-bicanonical divisor with those properties: a Coble surface.
:::

::: {.remark}

Why introduce Halphen surfaces?
I conjecture that the geometric construction(s) above yield some kind of correspondence between moduli spaces of Coble surfaces with $n$ boundary components and the various moduli spaces of index 2 Halphen pencils on the $g=0$ line of Nikulin's diagram of $2$-elementary lattices, whose vertices are the triples $(r, a, \delta)$.
Regarding the coarse spaces as quotients of the period domains attached to these lattices, the lattices match up precisely; see [the Coble lattice table](#sec-coble-lattice-table).
Applications of mirror moves indicate that the cusp diagrams would correspondingly coincide as well.
:::

