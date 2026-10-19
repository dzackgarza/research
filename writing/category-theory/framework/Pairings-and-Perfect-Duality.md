# Module pairings and perfect duality {#sec-module-pairings}

Fix a commutative ring $R$. The tensor product, internal Hom, and duality of $R\text{-}\mathbf{Mod}$ are those of @def:closed-monoidal and @def:dualizable-object.

## Pairings of two modules {#sec-general-pairings}

::: {.definition #def:module-pairing title="Bilinear pairings with general source and value modules"}
For $A,B,W\in R\text{-}\mathbf{Mod}$, an **$R$-bilinear pairing** of $A$ and $B$ with values in $W$ is a morphism
$$
b\colon A\tensor_R B\longrightarrow W
$$
in $R\text{-}\mathbf{Mod}$. Such pairings form the $R$-module
$$
\operatorname{Pair}_{R,W}(A,B)
\definedas
\Hom_R(A\tensor_RB,W).
$$
Precomposition with $f\tensor_Rg$ for $f\colon A'\too A$ and $g\colon B'\too B$ makes $\operatorname{Pair}_{R,W}$ a contravariant functor on $R\text{-}\mathbf{Mod}\times R\text{-}\mathbf{Mod}$.

The fixed-value **category of pairings** $\mathbf{Pair}_{R,W}$ has objects $(A,B,b)$ and morphisms
$$
(f,g)\colon(A,B,b)\too(A',B',b')
$$
satisfying $b=b'\circ(f\tensor_Rg)$. Pullback along the diagonal $M\mapsto(M,M)$ gives the bilinear-form presheaf $\Bil_{R,W}$ of @def:form-presheaves. A pairing of two possibly different modules does not require symmetry or a choice of identification between them.
:::

::: {.definition #def:pairing-adjoints title="The adjoints and their exact sequences"}
For $b\colon A\tensor_RB\too W$, the tensor–Hom adjunction gives the **left** and **right adjoints**
$$
\begin{aligned}
b^\ell\colon A&\longrightarrow\Hom_R(B,W),
&a&\longmapsto(b\mapsto b(a,b)),\\
b^r\colon B&\longrightarrow\Hom_R(A,W),
&b&\longmapsto(a\mapsto b(a,b)).
\end{aligned}
$$
Here the symbols in parentheses designate evaluation of the original pairing; the adjoints are morphisms in $R\text{-}\mathbf{Mod}$.

The **left radical**, **right radical**, **left coradical**, and **right coradical** are the kernels and cokernels in the complete exact sequences
$$
\begin{aligned}
0&\too\radic_\ell(b)\too A\xrightarrow{b^\ell}\Hom_R(B,W)
\twoheadrightarrow\operatorname{corad}_\ell(b)\too0,\\
0&\too\radic_r(b)\too B\xrightarrow{b^r}\Hom_R(A,W)
\twoheadrightarrow\operatorname{corad}_r(b)\too0.
\end{aligned}
$$
The pairing is **left nondegenerate** when $\radic_\ell(b)=0$, **right nondegenerate** when $\radic_r(b)=0$, and **nondegenerate** when both radicals vanish. It is **perfect** when both adjoints are isomorphisms, equivalently when all four kernel and cokernel obstructions vanish.
:::

::: {.proposition #prop:perfect-pairing-projective title="Perfectness on finitely generated projective modules"}
Suppose $A$ and $B$ are finitely generated projective and $W=R$. Then $b^\ell$ is an isomorphism if and only if $b^r$ is an isomorphism; either condition is equivalent to perfectness.

The evaluation pairing
$$
\operatorname{ev}_A\colon A^\vee\tensor_RA\longrightarrow R,
\qquad A^\vee\definedas\Hom_R(A,R),
$$
is perfect for every finitely generated projective $A$.
:::

::: {.proof}
Finitely generated projective modules are dualizable by @prop:projective-dualizable, and the evaluation morphism $B\longrightarrow B^{\vee\vee}$ is an isomorphism. The right adjoint is the composite
$$
B\xrightarrow{\sim}B^{\vee\vee}
\xrightarrow{(b^\ell)^\vee}A^\vee.
$$
Thus $b^\ell$ is invertible precisely when $b^r$ is. For $b=\operatorname{ev}_A$, the right adjoint is $\id_{A^\vee}$ and the left adjoint is the evaluation biduality isomorphism $A\xrightarrow{\sim}A^{\vee\vee}$, up to the symmetry of the tensor product.
:::

## Orthogonality for pairings {#sec-pairing-orthogonality}

::: {.definition #def:general-pairing-orthogonals title="The two orthogonal-complement functors"}
Fix $b\colon A\tensor_RB\too W$. For a monomorphism $i\colon S\injects A$, the **right orthogonal complement** is the kernel of
$$
B\xrightarrow{b^r}\Hom_R(A,W)
\xrightarrow{\Hom_R(i,W)}\Hom_R(S,W).
$$
For a monomorphism $j\colon T\injects B$, the **left orthogonal complement** is the kernel of
$$
A\xrightarrow{b^\ell}\Hom_R(B,W)
\xrightarrow{\Hom_R(j,W)}\Hom_R(T,W).
$$
These yield order-reversing functors between the two module-subobject posets of @def:subobject-relation. They satisfy the Galois connection
$$
S\subseteq{}^{\perp_A}T
\quad\Longleftrightarrow\quad
T\subseteq S^{\perp_B}.
$$
For $A=B=M$ and $b$ symmetric, the two constructions agree with the orthogonal-complement functor of @prop:orthogonal-galois-connection.
:::

::: {.proposition #prop:pairing-duality-base-change title="Flat base change of adjoints and radicals"}
Let $\varphi\colon R\too S$ be a homomorphism of commutative rings and suppose $A,B$ are finitely generated projective $R$-modules. The base-changed pairing
$$
b_S\colon(S\tensor_RA)\tensor_S(S\tensor_RB)
\longrightarrow S\tensor_RW
$$
has adjoints canonically isomorphic to $S\tensor_Rb^\ell$ and $S\tensor_Rb^r$. If $S$ is flat over $R$, the four exact kernel–cokernel sequences of @def:pairing-adjoints remain exact after base change, so the radicals and coradicals commute with scalar extension. If $S$ is faithfully flat, $b$ is nondegenerate, respectively perfect, if and only if $b_S$ is.
:::

::: {.proof}
Dualizability gives natural isomorphisms
$$
S\tensor_R\Hom_R(A,W)
\xrightarrow{\sim}
\Hom_S(S\tensor_RA,S\tensor_RW)
$$
and the corresponding isomorphisms with $B$. They identify the adjoints after extension of scalars with the stated tensor products. Flatness preserves kernels and cokernels of the two complete exact sequences. Faithfully flat scalar extension also reflects zero modules, yielding the last equivalences.
:::

## Perfectness depends on the value module {#sec-value-module-duality}

::: {.example #ex:pairing-nondegenerate-not-perfect title="Nondegenerate and perfect are distinct"}
The pairing $b\colon\bZ\tensor_\bZ\bZ\too\bZ$ with $b(a,b)=2ab$ has zero left and right radicals. Each adjoint is multiplication by $2$, with nonzero coradical $\bZ/2\bZ$. Thus it is nondegenerate but not perfect.

For the finite module $C_2\definedas\bZ/2\bZ$, the pairing
$$
C_2\tensor_\bZ C_2\too\bQ/\bZ,
\qquad
(\bar a,\bar b)\longmapsto \tfrac{ab}{2}+\bZ
$$
is perfect: its adjoints are isomorphisms $C_2\xrightarrow{\sim}\Hom_\bZ(C_2,\bQ/\bZ)$. Hence perfectness is a condition on the two adjoints with their specified value module, not a freeness condition on the source modules.
:::
