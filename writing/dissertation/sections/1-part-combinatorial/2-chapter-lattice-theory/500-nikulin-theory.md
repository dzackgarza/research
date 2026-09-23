### Nikulin's Embedding Theorems {#section-2-5}

Throughout this section, we adopt some simplifying notational conventions: for any lattice $L$, writing $\signature(L) = (p, q)$, we define $\tau(L) = p+q$, $\min \signature(L) = \min\ts{p, q}$, and $\max\signature(L)$ similarly.
Let $S \injects L$ be an embedding of lattices. We say $L$ is an **overlattice** of $S$ if $\iota(S)$ is a finite index sublattice.
We will be primarily interested in the case where $S\injects L$ is a primitive embedding with $T\da S^{\perp L} \injects L$ its (primitively embedded) orthogonal complement. In this situation, $L$ is an overlattice of $S\oplus T$, and we would like to know when it is of index 1. When this happens, we will say that $S$ **splits** $L$.
We first note a basic tool: for any lattice $L$, there is a canonical primitive embedding
\begin{align*}
\delta: L(2) &\to L \oplus L \\
v &\mapsto (v, v)
\end{align*}

#### Scattone's Methods

:::{.remark 
    title="Scattone's Method: Enumerating Boundary Components via Niemeier Lattices"
    #rem:scattone-method-niemeier
}
To motivate the detailed study of primitive embeddings, we note that the method of @Sca87 provides a concrete arithmetic approach to enumerating $0$-cusps in the Baily–Borel compactification $\bbcpt{\ftd}$ of the moduli space of degree-$2d$ polarized K3 surfaces.

By the classification of boundary components for arithmetic quotients of Hermitian symmetric domains [@BB66], $0$-cusps correspond to $\Gamma_{2d}$-orbits of primitive isotropic lines $I \subset L_{2d}$, where
$$
\lkttd \da  \gens{-2d} \oplus U^{ 2} \oplus E_8^{ 2}
$$
is the rank-$21$ lattice of signature $(2,19)$ associated to degree-$2d$ polarized K3 surfaces.

Each such cusp corresponds to a degeneration of K3 surfaces with associated lattice $I^\perp / I$, an even lattice of signature $(1,18)$, which encodes the limiting Hodge structure for degenerations to that cusp.
@Sca87 classified boundary components by studying primitive embeddings $U\injects L$ where $L$ is one of the $24$ **Niemeier lattices** -- the even, negative-definite, unimodular lattices of rank $24$.
For each such embedding $U \injects L$, the orthogonal complement $T \da  U^{\perp_L}$ is an even, negative-definite, unimodular lattice of rank $22$. These are the possible isometry classes of lattices of the form $I^{\perp}/I$ at $0$-cusps of $\bbcpt{\ftd}$.
The enumeration of $0$-cusps is thus reduced to counting the orbits of primitive embeddings $U \injects L$ for each Niemeier lattice $L$ up to $\Orth(L)$, where @Sca87 establishes that each such orbit corresponds to a *distinct* $0$-cusp, allowing for an explicit enumeration and thus an understanding of the entire cusp diagram for $\ftd$ for a wide range of values of $d$.
From this, we find that the class number $\cl(T)$ directly influences the number of 0-cusps, and representatives of isometry classes can be used to provide an explicit indexing set.
:::

#### Existence and Uniqueness

:::{.theorem
    title="Nikulin's Analog of Witt's Theorem [@Nik79, Thm. 1.14.4]"
    #thm:nik79-1-14-4
}
Let $S$ be an even lattice and $L$ an even unimodular lattice. Then

1. **The weak case:**  
  If $\signature(L) > \signature(S)$ and
  $\rank(L) - \rank(S) \geq 2 + \ell(A_S)$,
  then there exists a primitive embedding $S \injects L$ that is unique up to isometry.

1. **The generic case:**  
  If $\signature(L) > \signature(S)$ and
  $\rank(L) - \rank(S) \geq 2 + \max_{p \neq 2} \ell(A_{S_p})$,
  then there exists a primitive embedding $S \injects L$ that is unique up to isometry.

1. **The exceptional 2-adic case:**  
  If $\signature(L) > \signature(S)$ and
  $\rank(L) - \rank(S) = \ell(A_{S_2})$,
  then a primitive embedding exists **if and only if** there exists some $q'$ such that $q_S$ satisfies
  $$
  q_S \cong u_{+}^{(2)}(2) \oplus q' \quad \textor \quad q_S \cong v_{+}^{(2)}(2) \oplus q'
  .$$
:::

We note that this is not how @Nik79 originally states the theorem, but rather extracts the case that is more commonly used in applications for clarity.
The generic case is both necessary and sufficient for the existence and uniqueness of a primitive embedding, 
The weak case, which uses the global invariant $\ell(A_S)$ is easier to check in practice, but only gives a sufficient condition and is thus strictly weaker than the generic case. This is because if $A$ is any finite abelian group, one can consider the primary decomposition $A = \bigoplus_p A_p$, 
and there is an inequality
$\max_p \ell(A_p) \leq \ell(A) \leq \Sum_p \ell(A_p)$.
Thus, using $\ell(A_S)$ in place of $\max_{p \neq 2} \ell(A_{S_p})$ can exclude embeddings that the generic case would allow.

The weak and generic embedding criteria for Nikulin's theorem coincide if and only if the minimal number of generators of the group equals the maximum of the minimal numbers of generators of its $p$-primary parts, i.e., $\ell(A) = \max_p \ell(A_p)$. When $\ell(A) > \max_p \ell(A_p)$, the weak criterion requires a larger difference in ranks than the generic criterion, and thus gives only a sufficient (not necessary) condition for embedding.
This is best illustrated through concrete examples:

Let $A = \ZZ_6 \cong \ZZ_2 \times \ZZ_3$.
Then $A_2 = \ZZ_2$ with $\ell(A_2) = 1$, and $A_3 = \ZZ_3$ with $\ell(A_3) = 1$.
Since $A$ is cyclic, we have $\ell(A) = 1$,
and $\max\{\ell(A_2), \ell(A_3)\} = 1$.
The weak and generic criteria coincide, since $\ell(A) = \max\{\ell(A_2), \ell(A_3)\}$.

Let $A = \ZZ_2 \oplus \ZZ_3$.
Then $A_2 = \ZZ_2$ with $\ell(A_2) = 1$, $A_3 = \ZZ_3$ with $\ell(A_3) = 1$, and $\ell(A) = 2$, since both factors are needed to generate $A$.
We have $\max\{\ell(A_2), \ell(A_3)\} = 1$, and the weak criterion now requires rank difference $d$ to satisfy $d\geq 2 + 2$, while the generic criterion only requires $d \geq 2 + 1$. Thus, the weak case is strictly weaker and more restrictive: it may exclude embeddings allowed by the generic criterion.
Similarly, let $A = \ZZ_2 \oplus \ZZ_2$
Then $A_2 = \ZZ_2 \oplus \ZZ_2$ with $\ell(A_2) = 2$, and $\ell(A) = 2$ with $\max\{\ell(A_2)\} = 2$.
Here, the weak and generic criteria again coincide.
Thus the weak criterion is **always** sufficient, but only necessary when $\ell(A) = \max_p \ell(A_p)$, and the actual difference between the two cases depends highly on the structure of the group in question.
When $\ell(A) > \max_p \ell(A_p)$, the weak criterion is strictly more restrictive and does not capture all cases allowed by the generic condition.

#### Finiteness


:::{.proposition
  title="Finiteness of embeddings for even, unimodular lattices"
}
If $S$ and $L$ are even lattices and $L$ is unimodular, then $\Emb(S, L)$ is a finite set.
:::

:::{.proof}
By [@Nik79a, Prop. 1.6.1], such a primitive embedding $\iota: S \injects L$ is determined by an isometry $\gamma: A_{S} \iso A_{T}(-1)$, two such primitive embeddings are equivalent if and only if $\gamma_{1}$ is conjugate to $\gamma_{2}$ under $\Orth\left(A_{T}\right)$, and $\iota_{1}\left(S_{1}\right) \iso \iota_{2}\left(S_{2}\right)$ are equivalent primitive sublattices if $\exists(\phi, \psi) \in \Orth(S) \oplus \Orth(T)$ such that $\left.\gamma_{1} \circ \phi\right|_{A_{S}}=\left.\psi\right|_{A_{T}} \circ \gamma_{2}$.
Since $A_{S}, A_{T}$ are finite abelian groups, $\Isom\left(A_{S}, A_{T}\right)$ is a finite set, as is $\Orth\left(A_{T}\right)$. Moreover, noting that if $S_{1} \iso S_{2}$ then $A_{S_{1}} \iso A_{S_{2}}$ and thus $\Emb\left(S_{1}, L\right) \cong \Emb\left(S_{2}, L\right)$, so $\Emb(S, L)$ only depends on the isometry class of $S$. Since gen $(S)$ is a finite set, there are only finitely many isometry classes of $S$, so the class group $\cl(S)$ is finite and thus $\Emb(S, L)$ a finite set.
:::

#### Splitting

:::{.remark title="Discriminant form and anti-isometry"}
The discriminant group $A_S = S^\vee/S$ of $S$ carries a finite quadratic form $q_S$. The structure of the orthogonal complement $T$ and the existence of an overlattice are governed by the existence of an **anti-isometry** between $(A_S, q_S)$ and $(A_T, -q_T)$. This anti-isometry encodes the gluing data for constructing $L$ as an overlattice of $S \oplus T$.
The following results collect the relevant facts for this aspect of the theory:
:::


:::{.theorem
    title="Primitive Embedding Theorem [@PS24, Prop. 15.1.1]"
    #thm:primitive-embedding-corrected
}
Let $S$ be a primitive non-degenerate sublattice of a unimodular lattice $L$, and let $T = S^{\perp L}$ be its orthogonal complement. Then:

1. $S \oplus T$ is a sublattice of $L$ of finite index.

2. $[L\colon S \oplus T] = |A_S| = |A_T|$, where $A_S = S^*/S$ and $A_T = T^*/T$ are the discriminant groups.

3. There is a canonical isomorphism $\psi: A_S \to A_T$ such that the discriminant forms are related by an **anti-isometry**:
   $$
   q_{A_T}(\psi(x)) = -q_{A_S}(x) \qquad \forall x\in A_S
   .$$

:::


#### Gluing and Overlattices

Throughout this section, for a discriminant group $(G, q)$, we write $G(n)$ for the group $G$ with quadratic form $\tilde q \da n q$.
In particular, $G_1\iso G_2(-1)$ are isometric by a map $f$ if and only if $G_1\cong G_2$ as groups and $q_1(v) = -q_2(f(v))$ for all $v\in G_1$. 
Let $L$ be as above; a primitive embedding $S \injects L$ with $T\da S^{\perp L}$ is uniquely determined by the choice of

1. A subgroup $H \leq A_{L}$, the *embedding subgroup*, and

2. An isometry $\gamma: H \iso H^{\prime} \containedin A_{S}$, the *embedding isometry*, where $H'$ is the image of $H$.

Letting $\Gamma$ be the graph of $\gamma$ in $A_{L} \oplus A_{S}(-1)$, one has $A_{T}=\Gamma^{\perp} / \Gamma$ and we note that there is a discriminant formula
$$
|\disc T|=\frac{|\disc L| \cdot|\disc S|}{(\sharp H)^{2}} 
.$$
Now let $\iota: S \injects L$ be an embedding of even lattices where $L$ is unimodular, and define $H_{L}\da L / \iota(S)$. Using the chain of embeddings $S \injects L \injects L^{\vee} \injects S^{\vee}$ to produce embeddings $H_{L} \injects L^{\vee} / S \injects A_{S}$, one can regard $H_L$ as a subgroup of $A_S$.
Conversely, for a subgroup $H \leq A_{S}$, write $\eta: S^{\vee} \to A_{S}$ and define a lattice $S_{H}\da \eta\inv(H) \containedin S^{\vee}$. We note that $S_{H} \supseteq S$, so $S_{H}$ is an overlattice of $S$.

These constructions are mutually inverse and define a bijection:
\begin{align*}
\{\text { Even overlattices } L \text { of } S\} & \mapstofrom
\left\{\text { Isotropic subgroups } H \leq A_{S}\right\} \\
L &\mapsto H_{L}\da L / S \\
L\da S_{H} & \leftarrow H
\end{align*}

We apply this to the following:

:::{.proposition}
Let $L$ be a unimodular lattice and $\iota: S \injects L$ be a primitively embedded sublattice. Then $|\disc(S)|=|\disc(T)|$, and if $S$ is unimodular, then $L \cong$ $S \oplus T$.
:::

:::{.proof}
We have
$$
|\disc(S)|=\sharp A_{S} = \size A_{T}=|\disc(T)| .
$$
The isometry follows from Proposition 1.3.7: since $S \oplus T \leq L$ is a full-rank sublattice, $T$ is also unimodular and thus
$$
[L: S \oplus T]^{2}=\frac{\disc(S \oplus T)}{\disc(L)}=\frac{\disc(S) \cdot \disc(T)}{\disc(L)}=1 .
$$
Finally, a pair of isometries of $S$ and $T$ lifts to an isometry of $L$ if and only if they preserve $H_{L}$, or equivalently commute with the glue map.
Thus given $S\injects L$ as above with $T\da S^{\perp L}$, even if $S$ does not split $L$, we still have a way to construct isometries on $L$: one first constructs isometries $f_S\in \Orth(S)$ and $f_T \in \Orth(T)$ such that the restricted action of $f_S$ to $A_S$ and that of $f_T$ to $A_T$ agree, using the anti-isometry $A_S\iso A_T(-1)$, then produces a lift of $f_S \oplus f_T$ to an element of $f\in \Orth(L)$ that restricts to both $f_S$ and $f_T$. In particular, $f$ stabilizes both $S$ and $T$, and thus defines isometries in the stabilizers $\Stab_{\Orth(L)}(S)$ and $\Stab_{\Orth(L)}(T)$.
:::

#### Applications to $\fent$ {#sec:applications-fent}

To see some of this theory applied to the moduli problem at hand, we take a small detour to prove that $\fent$ is the normalization of a closed subvariety of $\fttz$ -- an essential ingredient in the main theorem.
The strategy is as follows:

1. Identify a morphism $\Psi: \fent \to \fttz$ arising from a lattice embedding $\tilde \Psi: \ten \injects \tdp$.
  
2. Establish a rigidity theorem at the level of lattice embeddings to assert that $\Psi$ is well-defined and canonically determined.

3. Restrict $\Psi$ to its scheme-theoretic image, i.e. the smallest closed subscheme of $\fttz$ through which $\Psi$ factors, to obtain $\Psi: \fent \to X$

4. Since $\fent$ is known to be normal by the general theory of @BB66, we then appeal to Zariski's main theorem: since $X$ is a closed subscheme of a normal variety, if $\Psi$ is finite and birational, it satisfies the universal property of normalization.

We first claim there is a holomorphic, algebraic morphism of period domains
\begin{align*}
\tilde \Psi: \halfpd{\ten} \to \halfpd{\tdp} \\
\end{align*}

This follows from defining an embedding of lattices by
\begin{align*}
\tilde \Psi: \ten \da U \oplus U(2) \oplus E_8(2) &\injects \tdp\da  U \oplus U(2) \oplus E_8^2 \\
(u_1, u_2, v) &\mapsto (u_1, u_2, v, v)
\end{align*}
which in block form is $(\id, \id, \delta)$ where $\delta$ is the canonical doubling embedding.
To see that this induces a well-defined morphism after passing from lattices to period domains, note that its construction is functorial: 
it involves tensoring to $\CC$, projectivizing, restricting to a quadric, and then further restricting to a semialgebraic subset in both the source and the target, cut out by precisely the same conditions.
The map $\tilde \Psi$ is holomorphic because it is the restriction of a linear map to an open set, and algebraic (and hence a morphism) because both varieties are quasiprojective and $\tilde \Psi$ is linear.

We now claim this morphism is well-defined and canonical in the following sense: let $A_i\to B_i \to C_i$ for $i=1,2$ be two sequences of primitive embeddings. We say two such sequences are **equivalent** if there exist isometries making the following diagram commute:

\begin{tikzcd}
A_1 \arrow[r, "f_1"] \arrow[d, "\phi_A", "\simeq"'] & B_1 \arrow[r, "g_1"] \arrow[d, "\phi_B", "\simeq"'] & C_1 \arrow[d, "\phi_C", "\simeq"'] \\
A_2 \arrow[r, "f_2"] & B_2 \arrow[r, "g_2"] & C_2
\end{tikzcd}

In particular, if $C_1 = C_2 = L$ is a fixed lattice, then $\phi_C\in\Orth(L)$ and we say the sequences are *equivalent up to $\Orth(L)$*.
If $A_1 = A_2 = A$ and $B_1=B_2 = B$ are also fixed and any two such sequences $A \to B \to L$ are equivalent, we say the sequence is **unique up to isometry** or **unique up to $\Orth(L)$**.
We observe several useful facts:

- $A\injects B\injects L$ is unique up to $\Orth(L)$ if and only if $A^{\perp L} \injects B^{\perp L}\injects L$ is,

- $A\injects B\injects L$ is unique if $B\injects L$ is unique and $A\injects B$ is unique,

- $A(n) \injects B(n)$ is unique if $A\injects B$ is unique

The following is proved as [@AEGS25, Lem. 2.4]:

:::{.proposition}
The following sequence of primitive embeddings is unique up to isometry:
\begin{align*}
\tilde \Psi: \ten \injects \tdp \injects \lkt 
.\end{align*}
:::


:::{.proof}
Passing to orthogonal complements in $\lkt$ yields the sequence
$$
\qty{ 
  \sen \injects \sdp \injects L
} = 
\qty{
  U(2) \injects U(2) \oplus E_8(2) \injects L
}
.$$
We first claim $U(2) \injects U(2) \oplus E_8(2)$ is unique.
By untwisting, it suffices to show that $U\injects U\oplus E_8$ is unique.
Write $U = S = \II_{1,1}$ and $U \oplus E_8 = L = \II_{1, 9}$, noting that both are the unique even unimodular lattices with those signatures. 
The existence of an embedding $S\injects L$, is clear, since one can simply take $x\mapsto (x, 0)$ and check that the cokernel is isometric to $E_8$ and thus free.
For uniqueness, let $T\da S^{\perp L}$: then $T$ is an even unimodular lattice of signature $(0, 8)$, and thus isometric to $E_8 = \II_{0, 8}$, which is unique up to isometry.
So if $j_i: S_i \injects L$ are any two primitive embeddings, there are decompositions $L \cong S_1 \oplus T_1$ and $L\cong S_2 \oplus T_2$ where $S_1\cong S_2 \cong \II_{1,1}$ and $T_1\cong T_2 \cong \II_{0, 8}$ are both unique up to isometry. 
So there exist isometries $\phi_S: S_1\to S_2$ and $\phi_T: T_1\to T_2$, and thus an isometry $\phi_S \oplus \phi_T: S_1\oplus T_1\to S_2\oplus T_2$. 
Since $S_i, T_i$ are unimodular, $\phi_S$ and $\phi_T$ trivially act identically on the discriminant groups, and thus lift to an isometry $\phi\in \Orth(L)$.
So $j_1$ is equivalent to $j_2$ as an embedding.

We now claim that the second embedding $U(2)\oplus E_8(2)\injects \lkt = U^2 \oplus E_8^3$ is unique.
This follows from Nikulin's version of Witt's @thm:nik79-1-14-4:

1. $\signature(\lkt) = (3, 19) > \signature(U(2) \oplus E_8(2)) = (1, 9)$,
2. $\rank(\lkt) - \rank(U(2) \oplus E_8(2)) = 22-10 \geq 2 + \ell(A_S) = 2 + 10$.

We conclude by the observations above.
:::

:::{.proposition}
The map $\tilde \Psi$ descends to a well-defined algebraic morphism on arithmetic quotients:
$$
\Psi: \fent = \halfpd{\ten}/\gent \to \fttz = \halfpd{\tdp}/\Orth(\tdp)
.$$
:::

:::{.proof}
It suffices to show that every isometry of $\ten$ extends to an isometry of $\tdp$ preserving $\ten$.
This follows from a standard lattice-theoretic argument involving discriminant groups:
let $S = \ten = U \oplus U(2) \oplus E_8(2)$ and $T = \sen = U(2) \oplus E_8(2) = S^{\perp L}$ where $L = \lkt$.
We note that 
$$
A_S = A_{U(2)} \oplus A_{E_8(@)} = C_2^2 \oplus C_2^{8} \cong C_2^{10} \cong A_T
,$$
and that $S$ and $T$ are both even indefinite 2-elementary lattices.
By [@Nik79, Thm. 3.6.3], the restrictions $\Orth(S)\to\Orth(A_S)$ and $\Orth(T) \to\Orth(A_T)$ are surjective, and thus of $f\in \Orth(S)$, using the fact that $A_S\cong A_T$, the restricted isometry $f_{A_S}$ induces an isometry $f_{A_T}$ on $A_T$, which can be be lifted to an isometry $f_T$ on $T$.
By construction, $f_{T}$ and $f_{S}$ act identically on $A_S$ and $A_T$, and so lift to an isometry $f\in \Orth(L)$ preserving both $S$ and $T$.
:::



:::{.lemma 
  title="[@AEGS25, Lemma 2.8]"
  #lem:fent-to-fttz-closed-immersion
}
There exists a closed subscheme $X \subset \fttz$ such that $\fent$ is canonically isomorphic to the normalization of $X$.
:::

:::{.proof}
The result follows by restricting the period morphism $\Psi$ to its scheme-theoretic image $X$ and replacing it by $\Psi: \fent \to X$. The morphism $\Psi$ is finite and birational. Birationality is established by the fact that $\Psi$ is an open immersion over the locus of smooth, generic Enriques surfaces, and thus is birational onto its image. Finiteness holds since $\Psi$ is proper and quasi-finite. Both $\fent$ and $\fttz$ are normal since they are complex analytic manifolds, following @BB66. The closed subscheme $X$ inherits normality as a subscheme of a normal variety. 

By Zariski's Main Theorem, a finite birational morphism from a normal variety to an integral variety identifies the source with the normalization of the target. Therefore, $\Psi\colon \fent \to X$ exhibits $\fent$ as the normalization of $X$.
:::
