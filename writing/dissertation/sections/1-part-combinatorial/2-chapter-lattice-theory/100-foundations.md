### Foundations {#section-2-1}

#### Bilinear and Quadratic Forms

##### Pairings

:::{.definition title="{Symmetric Bilinear Form}" #def:symmetric-bilinear-form}

Let $L$ be a $\ZZ$-module. A **bilinear form** $\beta$ on $L$ is a morphism $\beta: L \tensor_{\ZZ} L \to \QQ$. We often write $v \cdot w$ or $vw$ for $\beta(v,w)$.
A bilinear form $\beta$ is:

- **$\eps$-symmetric** for $\eps \in \QQ$ if $\beta(a,b) = \eps \cdot \beta(b,a)$.
- **Symmetric** if $\eps = 1$.
- **Skew-symmetric** if $\eps = -1$.
- **Alternating** if $\beta(a,a) = 0$ for all $a \in L$.
- **Integral** if its image $\beta(L,L)$ is contained in $\ZZ$.
- **Nondegenerate** if the map $L\to \Hom_\ZZ(L, \ZZ)$ given by $v\mapsto \beta(v, \cdot)$ is injective.
:::

:::{.definition title="{Quadratic Form and Associated Bilinear Form}" #def:quadratic-form}
A **quadratic form** on a $\ZZ$-module $L$ is a map of sets $q: L \to \QQ$ such that $q(\lambda v) = \lambda^2 q(v)$ for all $v \in L, \lambda \in \QQ$, and such that its **polar form** $\beta_q$ is a symmetric bilinear form on $L$:
\begin{align*}
\beta_q: L \tensor_{\ZZ} L &\to \QQ \\
(v,w) &\mapsto \beta_q(v,w) \da q(v+w) - q(v) - q(w)
\end{align*}
We say $q$ is **integral** if $q(L) \containedin \ZZ$. The pair $(L,q)$ is called a **quadratic $\ZZ$-module**.
:::

:::{.lemma title="{Correspondence between Bilinear and Quadratic Forms}" #lem:bilinear-quadratic-correspondence}

Every $\QQ$-valued bilinear module $(L,\beta)$ determines a $\QQ$-valued quadratic module $(L,q_\beta)$ by $q_\beta(v) \da \beta(v,v)$, which depends only on the symmetric part of $\beta$. Conversely, every $\QQ$-valued quadratic module $(L,q)$ determines a symmetric bilinear module $(L,\beta_q)$ via the polar form.
:::

:::{.lemma title="{Bijection for Even Lattices}" #lem:even-lattice-bijection}

There is a bijection between even symmetric integral forms and integral quadratic forms:
$$\begin{aligned}
\{\beta \in \Sym_{\ZZ}^2(L\dual) \st \beta \text{ is even}\} &\mapstofrom \Quad_{\ZZ}(L) \\
\beta &\mapsto q(v) \da {1\over 2}\beta(v,v) \\
\beta_q &\mapsfrom q
\end{aligned}$$
In other words, the polar form of any integral quadratic form is an even symmetric integral form. Conversely, every even symmetric integral form $\beta$ is the polar form of the integral quadratic form $q(v) \da {1\over 2}\beta(v,v)$.
:::

##### Lattices

:::{.definition title="{Lattice}" #def:lattice}
A **lattice** is a pair $(L,\beta)$ where $L$ is a free $\ZZ$-module of finite rank and $\beta$ is a nondegenerate symmetric bilinear form, which is typically integral but may be $\QQ$-valued. A **quadratic lattice** is a pair $(L,q)$ where $q$ is a nondegenerate quadratic form.
A lattice $(L,\beta)$ is **even** if $\beta(v,v) \in 2\ZZ$ for all $v \in L$, and **odd** otherwise.
:::

##### Gram Matrices

:::{.definition title="{Gram Matrix}" #def:gram-matrices}
Given a basis $B_L = (e_i)_{1 \leq i \leq n}$ for a bilinear module $(L,\beta)$, the **Gram matrix** of $\beta$ is $G_\beta \da (\beta(e_i, e_j))_{i,j} \in \Mat_{n \times n}(\QQ)$. For vectors $v = \Sum a_j e_j$ and $w = \Sum b_j e_j$, we have $\beta(v,w) = v^t G_\beta w$.
Similarly, for a quadratic module $(L,q)$, a **Gram matrix** $G_q$ is any matrix such that $q(v) = v^t G_q v$.
We define the **discriminant** $\disc(L)$ of $L$ as $\det(G_\beta)$ in any choice of basis.
We note that for any sublattice $S \leq L$, we have the formula 
$$
\disc(S) = [L:S]^2 \disc(L)
,$$
so the discriminant typically *increases* when passing to a sublattice.
We say $L$ is **unimodular** of $\disc(L) = \pm 1$.
The Gram matrix reflects properties of the form: $\beta$ is symmetric $\iff G_\beta^t = G_\beta$, skew-symmetric $\iff G_\beta^t = -G_\beta$, and an integral lattice is even $\iff G_\beta$ is an integer matrix with diagonal entries in $2\ZZ$.
:::

:::{.proposition title="{Primitive Isotropic Vectors, Divisibility, and Hyperbolic Splittings}" #prop:divisibility-properties-revised}
Let $S$ be any unimodular lattice admitting a primitive embedding into a nondegenerate lattice $L$.
Then $L \cong S \oplus T$ where 
$$
T\da S^{\perp} = \ts{v\in L \st \beta(v, S) = 0}
$$ 
is the **orthogonal complement** of $S$ in $L$.
Moreover, if $S$ is unimodular, then so is $T$.
:::

:::{.proof}
This follows from [@PS24, Lem. 1.3.1]: we can write $\disc(S) = [S\oplus T: L]\cdot c_S$ for some $c_S\in \ZZ$. 
By unimodularity, $\disc(S) = \pm 1$ forces $c_S = \pm 1$ and $[S\oplus T: L] = 1$, yielding the first claim.
For the second, we note that $\disc(S\oplus T) = \disc(S) \cdot \disc(T)$ by standard properties of determinants, forcing $\disc(T) = \pm 1$.
:::

:::{.definition title="{Rank and Signature}" #def:rank-signature}
Let $(L, \beta)$ be a nondegenerate lattice. We say it is:

- **positive definite** if $\beta(v,v) > 0$ for all nonzero $v \in L$.
- **positive semidefinite** if $\beta(v,v) \geq 0$ for all $v \in L$.
- **negative definite** if $\beta(v,v) < 0$ for all nonzero $v \in L$.
- **negative semidefinite** if $\beta(v,v) \leq 0$ for all $v \in L$.
- **indefinite** if it is neither positive nor negative semidefinite.

Letting $(L_{\RR}, \beta_{\RR})$ be the extension of $L$ to $\RR$, the diagonalization of the Gram matrix $p$ positive terms and $q$ negative terms.
We define the following:

- The **rank** of $L$ is $\rank(L) = p + q$.
- The **signature** of $L$ is $\signature(L) = (p,q)$.
- The **index** of $L$ is $\tau(L) = p - q$.

We note that $L$ is positive-definite if $q=0$, negative-definite if $p=0$, and indefinite if both $p,q > 0$.
We say $L$ is **hyperbolic** if its signature is $(1, n-1)$ or $(n-1, 1)$.
:::

:::{.definition title="{Scaled Lattices}" #def:scaled-lattices}
```meta
corpus-references: ""
depends-on: "#def:lattice"
audited: false
```
For any lattice $(L,\beta)$ and positive integer $m$, the **scaled lattice** $L(m)$ is the same $\ZZ$-module $L$ equipped with the bilinear form $\beta_m(v,w) = m \cdot \beta(v,w)$. The signature of $L(m)$ is the same as $L$, but the discriminant scales as $\disc(L(m)) = m^{\rank(L)} \cdot \disc(L)$. If $L$ is unimodular and $m>1$, $L(m)$ is not unimodular.
:::

:::{.example title="{Diagonal and Hyperbolic Lattices}"}
The **diagonal lattice** $\gens{a_1, \ldots, a_n}$ is $\ZZ^n$ with the bilinear form $\beta(x,y) = \Sum a_i x_i y_i$ and diagonal Gram matrix $\diag(a_1, \ldots, a_n)$.
In the special case $a_1,\cdots, a_{p} = 1$ and $a_{m+1}, \cdots, a_n = -1$, we write this lattice as $\I_{p, q}$, due to its distinguished nature as the unique nondegenerate odd unimodular lattice of signature $p, q$. 
The **hyperbolic lattice** $U$ is the free $\ZZ$-module $\ZZ^2$ with basis $e,f$ such that $\beta(e,e) = \beta(f,f) = 0$ and $\beta(e,f) = 1$. It is an even, integral, rank 2 lattice with Gram matrix 
$$
G_U = \matt 0110
.$$
:::

#### Sublattices, Embeddings, and Isometries

:::{.definition title="{Lattice Morphisms and Embeddings}" #def:lattice-morphisms}
A **morphism** between lattices $(L_1, \beta_1)$ and $(L_2, \beta_2)$ is a morphism of $\ZZ$-modules $f: L_1 \to L_2$ that preserves the bilinear form: $\beta_1(v,w) = \beta_2(f(v), f(w))$ for all $v,w \in L_1$.
We write $\Lat$ for the category of integral lattices, and $\Hom_{\Lat}(L_1, L_2)$ for their spaces of morphisms.
An **embedding** is an injective morphism.
An embedding is **primitive** if its cokernel, $\coker(f)$, is a torsion-free $\ZZ$-module.
An **isometry** is a morphism of lattices that is also an isomorphism of $\ZZ$-modules. Two lattices $L_1, L_2$ are **isometric**, written $L_1 \iso L_2$, if an isometry exists between them.
The **orthogonal group** of a lattice $L$ is its group of self-isometries $\Orth(L) \da \Aut_{\Lat}(L)$.
In terms of a Gram matrix $G_\beta$, the orthogonal group has the characterization:
$$
\Orth(L) = \{M \in \GL_n(\ZZ) \st M G_\beta M^t = G_\beta\}
$$
:::

:::{.definition title="{Primitive and Saturated Sublattices}" #def:primitive-sublattice}
A sublattice $S \leq L$ is **primitive** (or **saturated**) if the quotient module $L/S$ is torsion-free. An element $v \in L$ is **primitive** if the sublattice $\gens{v}_{\ZZ}$ is primitive.
:::

:::{.proposition title="{Characterization of Primitive Sublattices}" #prop:saturation-characterization}

For a sublattice $S \containedin L$, the following are equivalent:

- $S$ is a primitive sublattice of $L$.
- The inclusion $S \injects L$ is a primitive embedding.
- $S$ is saturated in $L$, meaning $S = \Sat_L(S) \da \{v \in L \st nv \in S \text{ for some } n \in \ZZ \sm \{0\}\}$.
- $S$ is a direct summand of $L$ as a $\ZZ$-module (i.e., $L \cong S \oplus T$ for some submodule $T$).
- Any $\ZZ$-basis of $S$ can be extended to a $\ZZ$-basis of $L$.
- $S_\QQ \intersect L = S$.
- $S = (S^{\perp L})^{\perp L}$.
- Every integral linear functional on $S$ can be lifted to an integral linear functional on $L$.
:::


:::{.definition 
    title="{Equivalence of Embeddings}" 
    #def:embedding-equivalence
}
Two primitive embeddings $\iota_1\colon S \injects L_1$ and $\iota_2\colon S \injects L_2$ are **equivalent** if there exists an isometry $f \in \Isom(L_1, L_2)$ such that $f \circ \iota_1 = \iota_2$, so the following diagram commutes

\begin{tikzcd}
S \arrow[r, "\iota_1"] \arrow[rd, "\iota_2"'] & L_1 \arrow[d, "f", dashed] \\
& L_2
\end{tikzcd}

If $L_1 = L_2 = L$ is a single lattice, two primitive embeddings $\iota_1, \iota_2: S \injects L$ are **equivalent** if they are equivalent by an element of $\Orth(L)$ as above.
The set of equivalence classes of primitive embeddings of $S$ into $L$ is denoted $\Emb(S, L)$.
:::

:::{.definition title="{Isotropic Submodules and Vectors}" #def:isotropic-submodules}
```meta
corpus-references: ""
depends-on: "#def:lattice"
audited: false
```
For a lattice $(L,\beta)$, a submodule $W \containedin L$ is **isotropic** if $\beta|_W = 0$ (equivalently, $W \containedin W^{\perp L}$). An **isotropic vector** is an element $v \in L$ with $\beta(v,v) = 0$. The **Witt index** $\WI(L)$ is the maximal rank of an isotropic sublattice.
:::

:::{.definition title="{Divisibility}" #def:divisibility-primitive-elements}
Let $L$ be a lattice with form $\beta$, and let $v \in L$. The **divisibility** of $v$ in $L$, denoted $\div_L(v)$, is the positive generator of the ideal $\ts{ \beta(v, w)\st w \in L} \containedin \ZZ$.
:::

:::{.proposition title="{Divisibility and Discriminant for Primitive Vectors}" #prop:divisibility-discriminant}
Let $L$ be a nondegenerate lattice, and $v \in L$ an arbitrary (not necessarily isotropic) vector. The element $v^* \da v/\div_L(v) \in L\dual$ is primitive in the dual lattice, and its image in the discriminant group $A_L \da L\dual/L$ has order $\div_L(v)$. In particular, $\div_L(v)$ divides the order of $A_L$, and hence $|\disc(L)|$.
:::

:::{.proof}
Since the divisibility $\div_L(v) = d$ is by definition the positive generator of the ideal $\{(v, w)\st w \in L\}$, one has $v/d \in L\dual$ and this vector is primitive in $L\dual$. Indeed, if $v/d = m y$ for some $m \in \ZZ$, $y \in L\dual$, then $v = d m y \in L$, and primitivity of $v$ in $L$ implies $m = \pm 1$.
The order of $v^*$ in $A_L$ is the minimal positive $n$ such that $n v^* \in L$. This occurs precisely when $n$ is divisible by $d$, so the order is $d = \div_L(v)$. Since $A_L$ is finite of order $|\disc(L)|$, it follows in particular that $\div_L(v)$ divides $|\disc(L)|$.
:::

:::{.lemma title="Divisibility of Isotropic Vectors in Unimodular Lattices" #lem:isotropic-pairing-unimodular}
Let $L$ be a nondegenerate unimodular lattice, and let $v \in L$ be a primitive isotropic vector. Then there exists $w \in L$ such that $(v, w) = 1$.
In particular, $\div_L(v) = 1$ for all $v\in L$.
:::

:::{.proof}
Since $L$ is unimodular, $L \iso L\dual$. The linear form $x \mapsto (v, x)$ is a nonzero element of $\Hom(L, \ZZ )$, and is surjective because $v$ is primitive and $L$ is unimodular. Hence there exists $w \in L$ with $(v, w) = 1$.
:::

#### Dual Lattices and Discriminant Forms

:::{.definition title="{Dual Lattice}" #def:dual-lattice-construction}
For an integral lattice $(L,\beta)$, the **dual lattice** is the $\ZZ$-module of linear functionals $L\dual \da \Hom_{\ZZ}(L, \ZZ)$.
:::

:::{.theorem title="{Geometric Identification of the Dual Lattice}" #thm:geometric-identification-dual}
For a nondegenerate integral lattice $(L,\beta)$, the dual lattice can be identified with a sublattice of $L_{\QQ} \da L \tensor_{\ZZ} \QQ$ via the bijection:
\begin{align*}
L\dual \cong \{ v \in L_{\QQ} \st \beta_{\QQ}(v,L) \containedin \ZZ\}
\end{align*}
where a functional $\phi \in L\dual$ corresponds to the unique vector $v_\phi \in L_\QQ$ such that $\phi(w) = \beta(v_\phi, w)$ for all $w \in L$. Under this identification, we have the inclusions $L \containedin L\dual \containedin L_{\QQ}$.
:::

:::{.remark title="{Properties of Dual Lattices}" #rem:dual-lattice-properties}
We summarize some standard properties of dual lattices

- Duality commutes with direct sums, $(L \oplus M)^\vee = L\dual \oplus M^\vee$.
- If $L$ has Gram matrix $G_\beta$ in a basis $B_L$, then the dual basis satisfies $B_{L\dual} = (B_L^t)\inv$, and the Gram matrix of the dual form is $G_{\beta^\vee} = G_\beta\inv$.
- The discriminant of the dual satisfies $\disc(L\dual) = 1/\disc(L)$, and the dual of a scaled lattice is $(L(m))^\vee = L\dual(1/m)$.
:::

:::{.definition title="{Discriminant Group and Discriminant}" #def:discriminant-group}

For a nondegenerate lattice $(L,\beta)$, the **discriminant group** is the finite abelian group $A_L \da L\dual / L$.
The order of the discriminant group equals the absolute value of the discriminant, i.e. $|A_L| = |\disc(L)| = [L\dual\colon L]$, so $L$ is unimodular if and only if $A_L$ is trivial.
:::

:::{.definition title="Discriminant Forms, [@PS24, Def. 1.6.5]" #def:discriminant-forms}
For a nondegenerate *even* lattice $(L,\beta)$, the **discriminant bilinear form** is $\beta_{A_L}: A_L \times A_L \to \QQ/\ZZ$, given by $\beta_{A_L}(\bar{x}, \bar{y}) = \beta(x,y) \bmod \ZZ$ for any lifts $x,y \in L\dual$ and $\beta$ the induced form on $L\dual$.
It admits an associated quadratic form $q_{A_L}(\bar x) = \beta(x,x)\pmod{\ZZ} \in \QQ/\ZZ$ for any lift $x$.
We note that there are two conventions in the literature, where one sometimes defines $q_{A_L}(\bar x) \da \beta(x,x)\pmod{2\ZZ}\in \QQ/2\ZZ$; these agree by the isomorphism $\QQ/\ZZ \iso \QQ/2\ZZ$ induced by multiplication by $2$.
We define its **orthogonal group** $\Orth(A_L)$ as the automorphisms that preserve $q_{A_L}$.
The **length** $\ell(L)$ of $L$ is the minimal number of generators for the abelian group $A_L$.
:::

:::{.proposition title="{Properties of Discriminant Forms}" #prop:discriminant-form-properties}
The discriminant forms $b_L$ and $q_L$ of a nondegenerate lattice $L$ are themselves nondegenerate. For any $[v], [w] \in A_L$, the bilinear and quadratic forms are related by $\beta_{A_L}([v],[w]) = {1\over 2}(q_{A_L} ([v]+[w]) - q_{A_L} ([v]) - q_{A_L} ([w]))$, where multiplication by ${1\over 2}$ is interpreted as an isomorphism $\QQ/2\ZZ \to \QQ/\ZZ$.
:::

:::{.proposition title="{Exact Sequence for Scaled Lattices}" #prop:scaled-lattice-sequence}
For any lattice $L$ and positive integer $m$, there is a short exact sequence:
$$
0 \to L/mL \injects A_{L(m)} \to A_L \to 0
$$
If $L$ is unimodular, this implies $A_{L(m)} \cong L/mL$.
Similarly, by functoriality, any isometry $f \in \Orth(L)$ lifts to an isometry of $L\dual$ and thus induces an isometry on the discriminant group $A_L$. This defines a group homomorphism $\psi: \Orth(L) \to \Orth(A_L)$, which fits into an exact sequence:
$$
0 \to \OStab(L) \to \Orth(L) \xrightarrow{\psi} \Orth(A_L) \to \OStab(A_L) \to 0
$$
where $\OStab(L) \da \ker(\psi)$ and $\OStab(A_L) \da \coker(\psi)$ are the **stable orthogonal groups** of $L$ and $A_L$. The cokernel, $\OStab(A_L) \da \coker(\psi)$, measures the obstruction to lifting isometries from the discriminant form $A_L$ to the lattice $L$.
We note that $\psi$ is surjective (i.e., $\OStab(A_L) = 0$) when $L$ is indefinite and satisfies $\ell(A_L) + 2 \leq \rank(L)$, where $\ell(A_L)$ is the minimal number of generators of $A_L$. For unimodular lattices like $U$ and $E_8$, the discriminant group is trivial, so $\OStab(L) = \Orth(L)$.
:::

:::{.example title="$U$ and $U(2)$" #ex:hyperbolic-duals}
The hyperbolic lattice $U$ is unimodular, so $U^\vee = U$ and its discriminant group $A_U$ is trivial.
For the scaled lattice $U(2)$, with Gram matrix $\matt 0220$, the dual is $U(2)^\vee = {1\over 2}U = U$ and we have $A_{U(2)} = U/U(2) \cong (\ZZ/2\ZZ)^2 \cong U/2U$.
:::

#### Torsion Forms over $\QQ/\ZZ$

:::{.definition title="{Torsion Bilinear and Quadratic Forms}" #def:torsion-forms}
A **torsion bilinear form** is a pair $(G,\beta)$ where $G$ is a finitely generated torsion $\ZZ$-module and $\beta: G \tensor_{\ZZ} G \to \QQ/\ZZ$ is a bilinear form. A **torsion quadratic form** is a pair $(G,q)$ where $G$ is a torsion module and $q: G \to \QQ/\ZZ$ is a quadratic form.
:::