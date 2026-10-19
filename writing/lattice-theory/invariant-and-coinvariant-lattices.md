# Invariant and coinvariant lattices

::: {.definition #def:invariant_coinvariant_lattices title="Invariants and coinvariants of integral group actions"}
Let $L\in\mathbf{Lat}_{\bZ}^{\mathrm{nd}}$ and let $\rho\colon G\too\Orth(L)$ be an action of a finite group. The homomorphism $\rho$ makes $L$ a left module over the integral group ring $\bZ[G]$, with augmentation $\epsilon_G\colon\bZ[G]\too\bZ$ and augmentation ideal $J_G\definedas\ker(\epsilon_G)$.

The **invariant lattice** is the evaluation sublattice $L^G\isoto\Hom_{\bZ[G]}(\bZ,L)\injects L$, with $\bZ$ carrying the trivial action. Its **geometric coinvariant lattice** is $L_G\definedas(L^G)^{\perp_L}$, the orthogonal complement of @def:orthogonal-complement.

The **translation submodule** is $I_G L\definedas J_G L\injects L$, the image of the group-ring multiplication $J_G\tensor_{\bZ[G]}L\too L$. The **module coinvariants** are $L_G^{\mathrm{mod}}\definedas\bZ\tensor_{\bZ[G]}L$, with their defining cokernel sequence in $\bZ\text{-}\mathbf{Mod}$
$$
0\too I_G L\injects L\twoheadrightarrow L_G^{\mathrm{mod}}\too0.
$$
:::

## Integral norm and coinvariant sequences {#sec-integral-coinvariants}

::: {.theorem #thm:invariants-coinvariants-integral title="Integral invariants, coinvariants, and splitting"}
Let $G,L$ be as in @def:invariant_coinvariant_lattices, put $n\definedas\cardinality{G}$, and let the integral norm $N_G\definedas\sum_{g\in G}\rho(g)$ factor as $\nu_G\colon L\too L^G\injects L$. Then
$$
L_G=\ker(\nu_G)=\Sat_L(I_G L),
\qquad
nL_G\subseteq I_G L\subseteq L_G.
$$
Both $L^G$ and $L_G$ are primitive and nondegenerate. Writing $\kappa_G\colon I_G L\injects L_G$, the norm induces the complete exact sequence in $\bZ\text{-}\mathbf{Mod}$
$$
0\too\coker(\kappa_G)\too L_G^{\mathrm{mod}}
\xrightarrow{\bar\nu_G}L^G
\twoheadrightarrow\coker(\nu_G)\too0.
$$ {#eq-integral-coinvariant-norm}

The orthogonal-sum morphism $j_G\colon L^G\perp L_G\injects L$ has the module-component exact sequence
$$
0\too L^G\oplus L_G
\xrightarrow{U_{\mathrm{mod}}(j_G)}L
\twoheadrightarrow C_G\too0,
\qquad C_G\definedas\coker(U_{\mathrm{mod}}(j_G)).
$$ {#eq-integral-coinvariant-gluing}

The modules $\coker(\kappa_G)$, $\coker(\nu_G)$ and $C_G$ are finite and annihilated by $n$.
:::

::: {.proof}
For $y\in L^G$, invariance of the pairing gives $\beta_L(N_Gx,y)=n\beta_L(x,y)$. This proves both nondegeneracy of the restriction to $L^G$ and $\ker\nu_G=(L^G)^{\perp_L}=L_G$. The norm annihilates $I_G L$, while
$$
n\id_L-N_G=\sum_{g\in G}(\id_L-\rho(g)).
$$
Thus $nL_G\subseteq I_G L\subseteq L_G$, proving the saturation identity and primitivity of $L_G$. The invariant lattice is primitive because it is the common kernel of the maps $\rho(g)-\id_L$. Its orthogonal complement $L_G$ is nondegenerate because $L^G_\bQ$ is nondegenerate in $L_\bQ$.

Passing the norm through $L/I_G L$ gives $\ker\bar\nu_G=L_G/I_G L=\coker(\kappa_G)$ and $\coker\bar\nu_G=\coker(\nu_G)$. The displayed identity also yields $nL\subseteq L^G+L_G$, so $C_G$ is finite and $n$-torsion. Finally $\nu_G(s)=ns$ for $s\in L^G$, establishing the same annihilator for $\coker(\nu_G)$; that for $\coker(\kappa_G)$ follows from $nL_G\subseteq I_G L$.
:::

::: {.proposition #prop:group-augmentation-exact title="Derived augmentation sequences"}
The augmentation sequence $0\too J_G\too\bZ[G]\xrightarrow{\epsilon_G}\bZ\too0$ is exact as a sequence of both left and right $\bZ[G]$-modules. It gives the complete exact sequences in $\bZ\text{-}\mathbf{Mod}$
$$
0\too\operatorname{Tor}_1^{\bZ[G]}(\bZ,L)
\too J_G\tensor_{\bZ[G]}L\xrightarrow{\mu_G}L
\twoheadrightarrow L_G^{\mathrm{mod}}\too0,
$$
$$
0\too L^G\too L
\too\Hom_{\bZ[G]}(J_G,L)
\twoheadrightarrow\operatorname{Ext}^1_{\bZ[G]}(\bZ,L)\too0.
$$
The image of $\mu_G$ is $I_G L$. The outer derived modules are $H_1(G,L)$ and $H^1(G,L)$, respectively.
:::

::: {.proof}
Apply $-\tensor_{\bZ[G]}L$ to the right-module augmentation sequence and $\Hom_{\bZ[G]}(-,L)$ to the left-module sequence. The middle ring module is free, while $\bZ\tensor_{\bZ[G]}L=L_G^{\mathrm{mod}}$ and $\Hom_{\bZ[G]}(\bZ,L)=L^G$.
:::

::: {.proposition #prop:integral-tate-gluing title="Norm and orthogonal-splitting obstructions"}
The outer terms of @eq-integral-coinvariant-norm are the Tate cohomology modules
$$
\widehat H^{-1}(G,L)\isoto L_G/I_G L,\qquad
\widehat H^0(G,L)\isoto L^G/\nu_G(L).
$$
The obstruction $C_G$ of @eq-integral-coinvariant-gluing fits into an isomorphism and exact sequence
$$
C_G\xrightarrow{\sim}\nu_G(L)/nL^G,
\qquad [x]\longmapsto[\nu_G(x)],
$$
$$
0\too C_G\too L^G/nL^G
\twoheadrightarrow\widehat H^0(G,L)\too0.
$$
In particular the ideal $(n)$ is contained in the annihilators over $\bZ$ of all three modules $C_G$, $\widehat H^{-1}(G,L)$ and $\widehat H^0(G,L)$.
:::

::: {.proof}
The first two modules are the kernel and cokernel of the norm on module coinvariants. The surjection $L\too\nu_G(L)/nL^G$ has kernel $L^G+L_G$: if $\nu_G(x)=ns$, then $x-s\in\ker\nu_G=L_G$, and the converse is immediate. This gives the isomorphism with $C_G$. The inclusions $nL^G\subseteq\nu_G(L)\subseteq L^G$ yield the remaining exact sequence and annihilator containments.
:::

## Integral isotypic sublattices {#sec-integral-isotypic-sublattices}

::: {.definition #def:isotypic-sublattices title="Integral isotypic sublattices"}
For a two-sided ideal $\mathfrak a$ of the group ring $\bZ[G]$, let $\operatorname{Ann}_L(\mathfrak a)\injects L$ be its annihilator. Let $\mathcal P_G$ be the finite set of minimal two-sided prime ideals of $\bZ[G]$. The **integral isotypic sublattice** indexed by $\mathfrak p\in\mathcal P_G$ is $L_{\mathfrak p}\definedas\operatorname{Ann}_L(\mathfrak p)$.

The quotient-ring morphisms assemble into the module exact sequence
$$
0\too\bZ[G]\xrightarrow{\Delta_G}
\prod_{\mathfrak p\in\mathcal P_G}\bZ[G]/\mathfrak p
\twoheadrightarrow\coker(\Delta_G)\too0.
$$
:::

::: {.theorem #thm:integral-isotypic-decomposition title="Integral isotypic decomposition and its conductor"}
Every nonzero $L_{\mathfrak p}$ is primitive, nondegenerate, and stable under $\bZ[G]$, and distinct components are orthogonal. Their orthogonal-sum map $j_\rho\colon\mathop{\perp}_{\mathfrak p\in\mathcal P_G}L_{\mathfrak p}\injects L$ has finite module-component cokernel, with
$$
\operatorname{Ann}_{\bZ}(\coker\Delta_G)
\subseteq\operatorname{Ann}_{\bZ}\qty{\coker(U_{\mathrm{mod}}(j_\rho))}.
$$
The augmentation ideal $J_G$ is a minimal two-sided prime and
$$
L_{J_G}=L^G,\qquad
L_G=\Sat_L\qty{\sum_{\substack{\mathfrak p\in\mathcal P_G\\\mathfrak p\ne J_G}}L_{\mathfrak p}}.
$$
Thus invariant lattices are trivial integral isotypic components, and geometric coinvariants are saturations of the nontrivial components.
:::

::: {.proof}
The integral group ring is an order in the semisimple rational algebra $\bQ[G]$, so $\Delta_G$ is injective with finite cokernel. Let $d>0$ annihilate this cokernel. For each $\mathfrak p$, choose $a_{\mathfrak p}\in\bZ[G]$ mapping to $d$ in its factor and zero in all others. Since $\Delta_G$ is injective, $\sum_{\mathfrak p}a_{\mathfrak p}=d$ and $\mathfrak p\,a_{\mathfrak p}=0$. Consequently $a_{\mathfrak p}L\subseteq L_{\mathfrak p}$ and $dL\subseteq\sum L_{\mathfrak p}$, proving finite index and the annihilator containment. Each $L_{\mathfrak p}$ is saturated as an intersection of kernels on the torsion-free module $L$.

Every simple rational $G$-module admits a $G$-invariant positive-definite rational symmetric form and hence is self-dual. Thus the group-ring involution $g\mapsto g^{-1}$ fixes each minimal prime, making $a_{\mathfrak p}$ self-adjoint. For $x\in L_{\mathfrak p}$ and $y\in L_{\mathfrak q}$ with $\mathfrak p\ne\mathfrak q$, $a_{\mathfrak p}x=dx$ while $a_{\mathfrak p}y=0$, so $d\beta_L(x,y)=\beta_L(x,a_{\mathfrak p}y)=0$. This gives orthogonality; nondegeneracy follows because the components span $L_\bQ$.

The quotient $\bZ[G]/J_G=\bZ$ identifies $L_{J_G}=L^G$. The other components lie in $L_G$. For $x\in L_G$, self-adjointness makes $a_{J_G}x\in L^G$ orthogonal to $L^G$, hence zero by @thm:invariants-coinvariants-integral. Thus $dx=\sum_{\mathfrak p\ne J_G}a_{\mathfrak p}x$, proving the asserted saturation equality.
:::

::: {.example #ex:integral-cyclic-three-isotypic title="The regular lattice of a cyclic group of order three"}
Let $G=C_3=\generators{g}$ and let $L=\bZ[G]$ carry the orthonormal integral bilinear form on the basis $(1,g,g^2)$. The regular left action preserves this form. The minimal prime ideals of $\bZ[C_3]\isoto\bZ[t]/(t^3-1)$ are $(t-1)$ and $(t^2+t+1)$. Their integral isotypic lattices are
$$
L_{(t-1)}=\bZ(1+g+g^2),\qquad
L_{(t^2+t+1)}=(g-1)\bZ[C_3]
=\ker(\epsilon_G).
$$
The first has Gram matrix $(3)$ and the second has Gram matrix
$$
\begin{pmatrix}2&-1\\-1&2\end{pmatrix}
$$
in the basis $(g-1,g^2-g)$; their sum embeds into $L$ with index $3$. The conductor cokernel $\coker(\Delta_G)$ and the geometric orthogonal-splitting cokernel $C_G$ are both isomorphic to $\bZ/3\bZ$.

Here $I_G L=L_G$, and the norm maps $L$ onto $L^G$, so
$$
\widehat H^{-1}(G,L)=0,\qquad
\widehat H^0(G,L)=0,\qquad
C_G\isoto\bZ/3\bZ.
$$
Thus even for the regular integral module, the nontrivial index-three isotypic gluing cannot be recovered from the vanishing of either norm-cohomology group.
:::


## Discriminant annihilators of integral group actions {#sec-discriminant-invariants}

::: {.theorem #thm:coinvariant-discriminant-annihilator title="Discriminant annihilators of fixed and complementary lattices"}
For $G,L$ as in @def:invariant_coinvariant_lattices, put $n=\cardinality{G}$. Assume the integral discriminant group $A_L^\sharp$ is annihilated by $n$ and the image of $G\too\Orth(L)$ lies in the bilinear discriminant kernel $\widetilde\Orth(L)$ of @def:discriminant-rep. Then the discriminant annihilator ideals satisfy
$$
(n)\subseteq\operatorname{Ann}_{\bZ}(A_{L^G}^\sharp),
\qquad
(n)\subseteq\operatorname{Ann}_{\bZ}(A_{L_G}^\sharp).
$$
:::

::: {.proof}
Put $S=L^G$, $T=L_G$. By @thm:invariants-coinvariants-integral both sublattices are primitive. Each module cokernel $L/M$, for $M=S,T$, is therefore free, so restriction of integral functionals is epic. With the form-induced identifications this says that every $x\in M^\#$ is the projection $P_M(w)$ of some $w\in L^\#$, where $P_S=N_G/n$ and $P_T=\id-N_G/n$.

The hypotheses give $nw\in L$ and $gw-w\in L$ for every $g\in G$. Thus
$$
nP_S(w)=N_Gw\in L,\qquad
nP_T(w)=nw-N_Gw\in L.
$$
Each left-hand side lies in $M_\bQ$; primitivity gives $L\cap M_\bQ=M$, hence $nM^\#\subseteq M$. Taking the metric-dual cokernel proves both ideal containments.
:::

::: {.theorem #thm:unimodular-finite-group-gluing title="Discriminant gluing of a finite isometry group"}
Let $L$ be an even unimodular lattice and let $\rho\colon G\too\Orth(L)$ be an action of a finite group of order $n$. Put $S=L^G$ and $T=L_G$. The primitive-complement gluing correspondence of @thm:nikulin-gluing supplies a quadratic anti-isometry
$$
\gamma_G\colon A_{S,q}\xrightarrow{\sim}A_{T,q}(-1),
$$
whose graph is the image of the module-component cokernel sequence
$$
0\too S\oplus T\xrightarrow{U_{\mathrm{mod}}(j_G)}L
\twoheadrightarrow C_G\too0.
$$
In particular
$$
C_G\isoto A_S^\sharp\isoto A_T^\sharp,\qquad
nA_S^\sharp=0,\qquad nA_T^\sharp=0,
$$
and $\ell(A_S^\sharp)=\ell(A_T^\sharp)$. The induced action of $G$ on the quadratic discriminant module $A_{T,q}$ is trivial:
$$
G\longrightarrow\Orth(T)\xrightarrow{\rho_{T,q}}
\Orth(A_{T,q})
$$
is the trivial homomorphism.
:::

::: {.proof}
The fixed and orthogonal coinvariant lattices are primitive, nondegenerate, mutually orthogonal, and have finite-index sum by @thm:invariants-coinvariants-integral. The unimodular gluing correspondence identifies their discriminant modules anti-isometrically and with the gluing cokernel $C_G$. The integral norm identity gives $nC_G=0$, hence the annihilator and length assertions.

The gluing graph is invariant under $G$ because $G$ preserves $L$. Its first projection identifies it with $A_{S,q}$, on which $G$ acts trivially because it fixes $S$ pointwise. Its other projection identifies it with $A_{T,q}$, so equivariance of the graph forces the action on that module to be trivial as well.
:::



## Involutions {#sec-integral-involutions}

::: {.proposition #prop:involution_eigenspaces}

Suppose $G = \generators{I}$ is generated by an involution $I\in\Orth(L)$, so that $I^2 = \id$.
Then, for the induced action of $I$ on $L_\QQ$, the rational spans $(L^G)_\QQ$ and $(L_G)_\QQ$ are precisely the eigenspaces of $I$ for the eigenvalues $+1$ and $-1$ respectively, and
$$
L_\QQ = (L^G)_\QQ \operatorname{\perp} (L_G)_\QQ
.
$$
:::

::: {.proof}

Since $I^2 = \id$, the induced isometry of $L_\QQ$ is diagonalizable with all eigenvalues in $\theset{+1, -1}$, so $L_\QQ = V_+ \oplus V_-$ where $V_\pm$ denotes the $\pm 1$ eigenspace.
The fixed space $V_+$ is by definition $(L^G)_\QQ$.
For $v\in V_+$ and $w\in V_-$, using that $I$ is an isometry,
$$
\beta_{L_\QQ}(v, w) = \beta_{L_\QQ}(I v, I w) = \beta_{L_\QQ}(v, -w) = -\beta_{L_\QQ}(v, w)
,
$$
so $\beta_{L_\QQ}(v, w) = 0$.
Let $\iota_-\colon V_-\injects L_\QQ$ denote the eigenspace monomorphism and $\kappa_+\colon V_+^{\perp}\injects L_\QQ$ the orthogonal-complement kernel.
The equality $\beta_{L_\QQ}(V_+,V_-)=0$ induces the unique monomorphism $\lambda_-\colon V_-\injects V_+^{\perp}$ with $\kappa_+\circ\lambda_-=\iota_-$.
Equality of dimensions gives $\lambda_-\colon V_-\isoto V_+^{\perp}$, and $V_+^{\perp}\isoto(L_G)_\QQ$.
:::


::: {.proposition #prop:involution_decomposition}

Let $L\in\mathbf{Lat}_{\bZ}^{\mathrm{nd}}$ and let $G=\generators{I}$ for an isometry $I\in\Orth(L)$ satisfying $I^2=\id_L$.
The invariant and coinvariant sublattices $L^G$ and $L_G$ are primitive and mutually orthogonal.
Moreover, each $v\in L$ decomposes orthogonally, up to a factor of $2$, as
$$
2\cdot v = v_+ + v_-,
\qquad
v_+ \definedas v + I(v)\in L^G,
\qquad
v_- \definedas v - I(v)\in L_G
.
$$
:::

::: {.proof}

By @thm:invariants-coinvariants-integral, $L^G$ and $L_G$ are primitive; by definition, $L_G = (L^G)^{\perp L}$, so they are orthogonal.
For the decomposition, fix $v\in L$ and set $v_+ \definedas v + I(v)$ and $v_- \definedas v - I(v)$, both of which lie in $L$.
Applying $I$ and using $I^2 = \id$,
$$
I(v_+) = I(v) + I^2(v) = I(v) + v = v_+,
\qquad
I(v_-) = I(v) - v = -v_-
,
$$
so $v_+\in L^G$.
By @prop:involution_eigenspaces, $v_-\in(L_G)_\QQ$.
Since $L_G\injects L$ is primitive by @thm:invariants-coinvariants-integral, @def:saturation gives
$$
L_G
\isoto
L\mathbin{\times}_{L_\QQ}(L_G)_\QQ.
$$
Because $v_-\in L\cap(L_G)_\QQ$, this pullback isomorphism gives $v_-\in L_G$.
Adding the two expressions gives $v_+ + v_- = 2v$, and the summands are orthogonal since $v_+\in L^G$ and $v_-\in L_G = (L^G)^{\perp L}$.
:::

::: {.proposition #prop:coinvariant_involution_2elementary}

Let $L\in\mathbf{Lat}_{\bZ}^{\mathrm{nd}}$ be $2$-elementary and let $I\in\widetilde\Orth(L)$ be an involution.
Then the invariant lattice $L^{\generators{I}}$ and geometric coinvariant lattice $L_{\generators{I}}$ have $2$-elementary discriminant groups.
:::

::: {.proof}

Write $\pi_\pm\colon L\tensor_\ZZ\QQ\to L^\pm\tensor_\ZZ\QQ$ for
$$
\pi_\pm(v)=\tfrac12(v\pm Iv),
\qquad
L^+=L^{\generators{I}},
\qquad
L^-=L_{\generators{I}}.
$$
Both $L^\pm\injects L$ are primitive.
Restriction therefore gives an epimorphism $\dualof{L}\twoheadrightarrow\dualof{L^\pm}$, which is $\pi_\pm$ under the form-induced maps.
Thus each $x\in\dualof{L^\pm}$ has $x=\pi_\pm(w)$ for some $w\in\dualof{L}$, and $2x=w\pm Iw$.

Let $\pi_L\colon L^\#\twoheadrightarrow A_L^\sharp$ be the cokernel morphism of @def:metric-dual.
Since $I\in\widetilde\Orth(L)$, $\pi_L\circ I=\pi_L$, and since $L$ is $2$-elementary, $2\,\id_{A_L^\sharp}=0$.
Hence
$$
\pi_L(Iw-w)=0,
\qquad
\pi_L(2w)=0.
$$
Exactness of
$$
0\too L\xrightarrow{\iota_L}L^\#\xrightarrow{\pi_L}A_L^\sharp\too0
$$
therefore gives unique $a_w,b_w\in L$ with $\iota_L(a_w)=Iw-w$ and $\iota_L(b_w)=2w$.

Primitivity of $L^\pm\injects L$ gives the pullback square
```tikzcd
L^\pm \arrow[r] \arrow[d] & L \arrow[d] \\
(L^\pm)_\QQ \arrow[r] & L_\QQ .
```

Since $2x\in L$ and $2x\in(L^\pm)_\QQ$, the pullback square gives a unique element $y_\pm\in L^\pm$ mapping to $2x$.
Thus multiplication by $2$ annihilates $A_{L^\pm}^\sharp$, so $L^\pm$ is $2$-elementary by @def:p-elementary.
:::



## Involution gluing and discriminant forms {#sec-involution-gluing}

::: {.corollary #cor:unimodular-involution-gluing title="Gluing of invariant and coinvariant lattices of an involution"}
Let $L$ be an even unimodular lattice and let $I\in\Orth(L)$ be an involution. Put $S=L^{\generators{I}}$ and $T=L_{\generators{I}}$. The gluing graph of @thm:unimodular-finite-group-gluing is a quadratic anti-isometry
$$
\gamma_I\colon A_{S,q}\xrightarrow{\sim}A_{T,q}(-1)
$$
and the module-component cokernel satisfies
$$
C_{\generators{I}}\isoto A_S^\sharp\isoto A_T^\sharp,
\qquad
2A_S^\sharp=2A_T^\sharp=0,
\qquad
\ell(A_S^\sharp)=\ell(A_T^\sharp).
$$
The involution restricts to the identity on the discriminant quadratic module $A_{T,q}$.
:::

::: {.example #ex:swap-involution-u2 title="Exchange of two hyperbolic planes"}
Let $L=U\perp U$ and let $I$ exchange the two summands. The two eigensublattices are
$$
\begin{aligned}
U(2)&\xrightarrow{\sim}L^{\generators{I}},
&x&\longmapsto(x,x),\\
U(2)&\xrightarrow{\sim}L_{\generators{I}},
&x&\longmapsto(x,-x).
\end{aligned}
$$
Their orthogonal-sum embedding has cokernel $C_{\generators{I}}\isoto U/2U\isoto(\bZ/2\bZ)^2$. On the other hand, the augmentation translation submodule equals the geometric coinvariant lattice, and the norm $L\too L^{\generators{I}}$ is surjective. Therefore
$$
\widehat H^{-1}(\generators{I},L)=0,\qquad
\widehat H^0(\generators{I},L)=0,\qquad
C_{\generators{I}}\isoto(\bZ/2\bZ)^2.
$$
The integral orthogonal-splitting cokernel is thus distinct from both norm-cohomology obstructions of @prop:integral-tate-gluing.
:::