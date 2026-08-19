# Dawes: Algorithms for Orbits of Non-Isotropic Vectors

**Source**
- Matthew Dawes, *Orbits in lattices*, §2.1, Algorithms 2.1-2.3, Theorem 2.3, Lemmas 2.4-2.5.

## Scope

This sidecar records only the explicit general algorithms and supporting criteria in
Dawes's paper for deciding whether two non-isotropic vectors lie in the same orbit.

Notation is Dawes's:

- $L$ is a lattice of rank $n$.
- $\Gamma \subset O(L)$ is a subgroup.
- $v_1, v_2 \in L \otimes \mathbb{Q}$ are the vectors to compare.

## Notation and Prerequisites from Dawes §1.2-1.3

The algorithms in §2.1 use the following notation from Dawes's setup.

### Discriminant data

- The **dual lattice** is
  $$
  L^\vee := \operatorname{Hom}(L,\mathbb Z) \subset L \otimes \mathbb Q.
  $$
- The **discriminant group** is
  $$
  D(L) := L^\vee/L.
  $$
- The **discriminant form** is the induced finite quadratic form
  $$
  q_L : D(L) \to \mathbb Q/2\mathbb Z.
  $$
- For lattices $L_1,L_2$, Dawes writes
  $$
  \operatorname{Iso}(q_{L_1},q_{L_2})
  $$
  for the group isomorphisms between $D(L_1)$ and $D(L_2)$ compatible with the
  quadratic forms.
- He writes
  $$
  O(D(L)) := \operatorname{Iso}(q_L,q_L).
  $$

### Real spinor norm and the `+`-subgroups

For $g \in O(L \otimes \mathbb R)$ written as a product of reflections
$$
g = \sigma_{w_1}\cdots\sigma_{w_m},
$$
Dawes defines the real spinor norm
$$
\operatorname{sn}_{\mathbb R}(g)
= \left(\frac{-(w_1,w_1)}{2}\right)\cdots\left(\frac{-(w_m,w_m)}{2}\right)
\in \mathbb R^*/(\mathbb R^*)^2.
$$

He then defines
$$
O^+(L \otimes \mathbb R)
$$
to be the kernel of this spinor norm in $O(L \otimes \mathbb R)$.

For any subgroup $\Gamma \subset O(L \otimes \mathbb R)$, Dawes writes
$$
\Gamma^+ := \Gamma \cap O^+(L \otimes \mathbb R).
$$

### The bar notation and `\mathcal A`

There is a natural map
$$
O(L) \to O(D(L)).
$$
For $g \in O(L)$, Dawes writes
$$
\overline g
$$
for its image in $O(D(L))$.

He also writes
$$
\widetilde O(L)
$$
for the kernel of the natural map
$$
O(L) \to O(D(L)),
$$
that is, the stable orthogonal group.

If
$$
\mathcal A \subset O(D(L))
$$
is a subgroup, then for any $\Gamma \subset O(L)$ Dawes writes
$$
\Gamma_{\mathcal A} := \{g \in \Gamma \mid \overline g \in \mathcal A\}.
$$

More generally, for any $\Gamma \subset O(L)$ he writes
$$
\widetilde \Gamma := \Gamma \cap \widetilde O(L).
$$

Specializing this notation gives:

- $\widetilde O^+(L) := \widetilde O(L) \cap O^+(L \otimes \mathbb R)$,
- $\widetilde{SO}^+(L) := SO(L) \cap \widetilde O^+(L)$,
- $O_{\mathcal A}(L) := \{g \in O(L) \mid \overline g \in \mathcal A\}$,
- $SO_{\mathcal A}(L) := SO(L) \cap O_{\mathcal A}(L)$,
- $O_{\mathcal A}^+(L) := O_{\mathcal A}(L) \cap O^+(L \otimes \mathbb R)$,
- $SO_{\mathcal A}^+(L) := SO(L) \cap O_{\mathcal A}^+(L)$.

These are exactly the subgroup types referenced in Dawes's discussion of membership
tests for Algorithms 2.1-2.3.

## Algorithmic Hierarchy

Dawes presents the following hierarchy.

### Algorithm 2.1

This is the broadest algorithm in §2.1.

Hypotheses:

- $L$ is any lattice of rank $n$.
- $\Gamma \subset O(L)$ is any subgroup.
- $v_1$ is non-isotropic.
- $v_1^\perp$ is definite.

No discriminant-form description of $\Gamma$ is required.
No surjectivity hypothesis on $O(L) \to O(D(L))$ is required.

### Algorithm 2.2

This is a stricter specialization for the indefinite-complement case.

Hypotheses:

- $L$ is a lattice of rank $n$.
- $\Gamma = O_{\mathcal A}(L)$ for some subgroup
  $$
  \mathcal A \subset O(D(L)).
  $$
- $v_1$ is non-isotropic.
- $v_1^\perp$ is indefinite.
- The natural map
  $$
  O(L) \to O(D(L))
  $$
  is surjective.

Algorithm 2.2 replaces direct lattice-isometry testing by discriminant-form and gluing
data.

### Algorithm 2.3

This is Dawes's coordinate rephrasing of Algorithm 2.2.

It uses Smith normal forms, explicit generators for discriminant groups, and explicit
formulas for the gluing subgroups and induced maps on discriminant groups.

## Common Preliminary Invariants

All three algorithms begin by normalizing the rational vectors.

For $i \in \{1,2\}$:

1. Let $c_i \in \mathbb{Q}_{>0}$ be minimal such that
   $$
   w_i := c_i v_i \in L.
   $$
2. Reject immediately if either invariant differs:
   - $v_1^2 \neq v_2^2$,
   - $c_1 \neq c_2$.

These are orbit invariants under every subgroup of $O(L)$.

## Algorithm 2.1

Assume $v_1$ is non-isotropic and $v_1^\perp$ is definite.

### Procedure

1. Normalize to integral vectors $w_1, w_2$.
2. Reject if $v_1^2 \neq v_2^2$ or $c_1 \neq c_2$.
3. For each $i \in \{1,2\}$:
   - compute $w_i$,
   - compute $(q_1|\cdots|q_n) := Q(\hat w_i)$,
   - define
     $$
     K_i := \langle k_{ij} \mid j = 1,\dots,n-1 \rangle
     \quad\text{with}\quad
     k_{ij} = q_{j+1},
     $$
   - define the embedding
     $$
     \iota_i := (w_i|k_{i1}|\cdots|k_{i(n-1)}).
     $$
4. Let $\varphi$ be the map $w_1 \mapsto w_2$.
5. Search over
   $$
   \psi \in \operatorname{Iso}(K_1, K_2).
   $$
6. For each such $\psi$, form
   $$
   \theta := \iota_2 \circ (\varphi \oplus \psi) \circ \iota_1^{-1}.
   $$
7. If some $\theta$ lies in $\Gamma$, return $v_1 \sim_\Gamma v_2$.
8. Otherwise return $v_1 \not\sim_\Gamma v_2$.

### Dawes's explanation

- The Smith normal form shows that each $K_i$ is the primitive orthogonal complement
  $w_i^\perp \subset L$.
- By Lemma 2.1, $w_1 \sim_\Gamma w_2$ if and only if the fixed map on
  $\langle w_1 \rangle$ and some isometry $K_1 \to K_2$ extend simultaneously to an
  element of $\Gamma$.
- Because $K_1$ is definite, $\operatorname{Iso}(K_1,K_2)$ can be computed with
  standard definite-lattice isometry algorithms.

### Membership remarks

Dawes makes the following subgroup-specific remarks:

- If $\Gamma = SO_{\mathcal A}(L)$ or $O_{\mathcal A}(L)$, one can check membership by
  verifying that $\theta$ is integral and that $\overline{\theta} \in \mathcal A$.
- If $\Gamma = SO_{\mathcal A}^+(L)$ or $O_{\mathcal A}^+(L)$, one must also check the
  relevant spinor-norm or positive-cone condition.
- For the spinor-norm check, Dawes points to effective methods for decomposing
  $\psi$ into a product of reflections in Cassels, *Rational Quadratic Forms*,
  pp. 18-20.

## Algorithm 2.2

Assume simultaneously:

- $v_1$ is non-isotropic,
- $v_1^\perp$ is indefinite,
- $\Gamma = O_{\mathcal A}(L)$ for some $\mathcal A \subset O(D(L))$,
- the natural map $O(L) \to O(D(L))$ is surjective.

### Procedure

1. For each $i \in \{1,2\}$:
   - normalize to $w_i := c_i v_i \in L$,
   - reject if $c_1 \neq c_2$ or $v_1^2 \neq v_2^2$,
   - define
     $$
     K_i := w_i^\perp \subset L,
     $$
   - for the natural inclusion
     $$
     \langle w_i \rangle \oplus K_i \subset L \subset L^\vee
     \subset \langle w_i \rangle^\vee \oplus K_i^\vee,
     $$
     define
     $$
     H_i := L / (\langle w_i \rangle \oplus K_i)
     \subset D(\langle w_i \rangle) \oplus D(K_i),
     $$
   - define
     $$
     \iota_i :
     D(L) \xrightarrow{\sim}
     \bigl(D(\langle w_i \rangle) \oplus D(K_i)\bigr) \bmod H_i.
     $$
2. If $K_1 \not\cong K_2$, return $v_1 \not\sim_\Gamma v_2$.
3. Search over
   $$
   \overline{\varphi} \oplus \overline{\psi}
   \in \{\pm 1\} \oplus \operatorname{Iso}(q_{K_1}, q_{K_2}).
   $$
4. If
   $$
   (\overline{\varphi} \oplus \overline{\psi})(H_1) = H_2
   $$
   and
   $$
   \iota_2^{-1} \circ (\overline{\varphi} \oplus \overline{\psi}) \circ \iota_1
   \in \mathcal A,
   $$
   return $v_1 \sim_\Gamma v_2$.
5. Otherwise return $v_1 \not\sim_\Gamma v_2$.

### What changed from Algorithm 2.1

Algorithm 2.1 searches over actual lattice isometries
$$
\psi : K_1 \to K_2.
$$

Algorithm 2.2 replaces that search by finite data:

- the discriminant forms $q_{K_i}$,
- the gluing subgroups $H_i$,
- the allowed image $\mathcal A \subset O(D(L))$.

## Algorithm 2.3

Algorithm 2.3 is Dawes's coordinate form of Algorithm 2.2.

Assume the same hypotheses as Algorithm 2.2.

### Procedure

1. For each $i \in \{1,2\}$:
   - let $c_i \in \mathbb{Q}_{>0}$ be minimal such that $w_i := c_i v_i \in L$,
   - let
     $$
     \alpha_i := \frac{w_i^2}{|w_i^2|}.
     $$
2. Reject if $v_1^2 \neq v_2^2$ or $c_1 \neq c_2$.
3. For each $i \in \{1,2\}$:
   - compute $(q_1|\cdots|q_n) := Q(\hat w_i)$,
   - define
     $$
     K_i := \langle k_{ij} \mid j = 1,\dots,n-1 \rangle
     \quad\text{with}\quad
     k_{ij} = q_{j+1},
     $$
   - compute the Smith normal form
     $$
     [d_1,\dots,d_n]_{n,n} := P(G(K_i))\,G(K_i)\,Q(G(K_i)),
     $$
     and identify
     $$
     D(K_i) \cong \bigoplus_j C_{d_j},
     $$
   - choose explicit representatives $f_{il} \in K_i^\vee$ for the canonical basis
     of $D(K_i)$,
   - construct the coordinate maps $\theta_{i1}$, $\theta_{i2}$, $\theta_{i3}$, and
     $\lambda_i$ from Dawes's displayed Smith-normal-form formulas.
4. If $K_1 \not\cong K_2$, return $v_1 \not\sim_\Gamma v_2$.
5. For each $i \in \{1,2\}$:
   - let $H_i$ be the subgroup of
     $D(\langle w_i\rangle)\oplus D(K_i)$ generated by the columns of $\lambda_i$,
   - let
     $$
     \iota_i := \lambda_i \circ G(L)^{-1}.
     $$
6. Search over
   $$
   \overline{\varphi} \oplus \overline{\psi}
   \in \{\pm 1\} \oplus \operatorname{Iso}(q_{K_1}, q_{K_2}).
   $$
7. If
   $$
   (\overline{\varphi} \oplus \overline{\psi})(H_1) = H_2
   $$
   and
   $$
   \theta := \iota_2^{-1} \circ
   (\overline{\varphi} \oplus \overline{\psi}) \circ \iota_1 \bmod L
   \in \mathcal A,
   $$
   return $v_1 \sim_\Gamma v_2$.
8. Otherwise return $v_1 \not\sim_\Gamma v_2$.

### Role of Algorithm 2.3

Algorithm 2.3 is the implementation-ready form of Algorithm 2.2.
Its purpose is to replace the abstract gluing and discriminant-form constructions of
Algorithm 2.2 by explicit coordinate formulas.

## Supporting Results Used by Algorithms 2.2-2.3

### Theorem 2.3

If a discriminant form $q$ satisfies:

1. $t_+ \ge 1$, $t_- \ge 1$, and $t_+ + t_- \ge 3$;
2. $t_+ + t_- \ge 2 + l(q)$,

then there exists a lattice $L$ of signature $(t_+, t_-)$ with $q_L = q$.
Moreover:

- the natural map $O(L) \to O(D(L))$ is surjective;
- the genus of $L$ contains a single class.

This is the criterion Dawes uses to identify indefinite lattices from signature plus
discriminant form and to justify the surjectivity hypothesis in many examples.

### Lemma 2.4

In the notation of Algorithm 2.3, if $K_1$ represents both $\pm 2$, then
$$
v_1 \sim_{O_{\mathcal A}(L)} v_2
\quad\Longleftrightarrow\quad
v_1 \sim_{SO_{\mathcal A}^+(L)} v_2.
$$

This is the mechanism Dawes uses to pass from $O_{\mathcal A}(L)$-equivalence to
$SO_{\mathcal A}^+(L)$-equivalence without a separate spinor-norm computation.

### Lemma 2.5

Let $K$ be an indefinite lattice with discriminant form $q_K$ and signature
$(t_+, t_-)$.
If $S := \langle \pm 2 \rangle$ and $\delta$ is one of:

1. $\delta = q_S \oplus (-q_K)$;
2. $\delta = ((q_S \oplus (-q_K)) \mid \Gamma_\gamma^\perp)/\Gamma_\gamma$,

and if:

- $K$ is unique in its genus,
- there exists a lattice of signature $(t_+, t_-)$ with discriminant form $-\delta$,

then $S \subset K$.

Dawes uses this together with Theorem 2.3 to prove that $K$ represents $\pm 2$, which is
the input needed for Lemma 2.4.

## Paper Examples as Validation Extracts

The examples in §2.1 are useful because they supply exact intermediate objects and
witnesses that an implementation can assert against.

For machine fixtures, use the explicit Gram matrices written below, cross-checked
against the arXiv source payload `orbits_in_lattices.tex`. Do not derive these
fixtures from Sage's named `A_3` constructors, whose sign convention differs from
the one fixed in Dawes's examples.

### Example 2.2: Algorithm 2.1 fixture

Input data:

- lattice
  $$
  L = U \oplus A_3,
  $$
  with
  $$
  G(U)=
  \begin{pmatrix}
  0 & 1 \\
  1 & 0
  \end{pmatrix},
  \qquad
  G(A_3)=-
  \begin{pmatrix}
  2 & 1 & 0 \\
  1 & 2 & 1 \\
  0 & 1 & 2
  \end{pmatrix};
  $$
- vectors
  $$
  v_1=(4,4,1,2,-1),
  \qquad
  v_2=(36,144,5,-30,83);
  $$
- subgroup
  $$
  \Gamma=\widetilde O^+(L).
  $$

Validation targets from Dawes's calculation:

- normalization and norms:
  $$
  c_1=c_2=1,
  \qquad
  w_1=v_1,
  \qquad
  w_2=v_2,
  \qquad
  v_1^2=v_2^2=20;
  $$
- Smith-normal-form output matrices:
  $$
  Q(\hat w_1)=
  \begin{pmatrix}
  0 & 1 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 1 & 0 \\
  -1 & 1 & 1 & -1 & 0 \\
  0 & 0 & 0 & 0 & 1
  \end{pmatrix},
  $$
  $$
  Q(\hat w_2)=
  \begin{pmatrix}
  0 & 1 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 1 & 0 \\
  -5 & 180 & 45 & 25 & 34 \\
  1 & -36 & -9 & -5 & -7
  \end{pmatrix};
  $$
- embeddings
  $$
  \iota_1=
  \begin{pmatrix}
  4 & 1 & 0 & 0 & 0 \\
  4 & 0 & 1 & 0 & 0 \\
  1 & 0 & 0 & 1 & 0 \\
  2 & 1 & 1 & -1 & 0 \\
  -1 & 0 & 0 & 0 & 1
  \end{pmatrix},
  \qquad
  \iota_2=
  \begin{pmatrix}
  36 & 1 & 0 & 0 & 0 \\
  144 & 0 & 1 & 0 & 0 \\
  5 & 0 & 0 & 1 & 0 \\
  -30 & 180 & 45 & 25 & 34 \\
  83 & -36 & -9 & -5 & -7
  \end{pmatrix};
  $$
- complement Gram matrices:
  $$
  G(K_1)=
  \begin{pmatrix}
  -2 & -1 & 1 & -1 \\
  -1 & -2 & 1 & -1 \\
  1 & 1 & -2 & 1 \\
  -1 & -1 & 1 & -2
  \end{pmatrix},
  $$
  $$
  G(K_2)=
  \begin{pmatrix}
  -54432 & -13607 & -7740 & -10260 \\
  -13607 & -3402 & -1935 & -2565 \\
  -7740 & -1935 & -1102 & -1459 \\
  -10260 & -2565 & -1459 & -1934
  \end{pmatrix};
  $$
- explicit witness isometry on the complements:
  $$
  \psi=
  \begin{pmatrix}
  -2 & -8 & 2 & -9 \\
  -8 & -30 & 5 & -36 \\
  -1 & -1 & 1 & -2 \\
  22 & 83 & -18 & 97
  \end{pmatrix};
  $$
- resulting extension to $L$:
  $$
  \theta=
  \begin{pmatrix}
  11 & 5 & -11 & -13 & -9 \\
  43 & 21 & -46 & -51 & -36 \\
  1 & 1 & -1 & -2 & -2 \\
  -9 & -5 & 10 & 12 & 8 \\
  25 & 12 & -26 & -30 & -21
  \end{pmatrix};
  $$
- stable-discriminant check:
  $$
  w=\frac14(0,0,3,-2,1)\in L^\vee
  $$
  generates the cyclic group $D(L)$, and Dawes verifies
  $$
  w \equiv \theta w \pmod L;
  $$
- positive-cone check for membership in $\widetilde O^+(L)$:
  $$
  P=
  \begin{pmatrix}
  0 & -1 & 1 & 0 & 0 \\
  0 & 1 & 1 & 0 & 0 \\
  -1 & 0 & 0 & 1 & 1 \\
  0 & 0 & 0 & \sqrt2 & -\sqrt2 \\
  1 & 0 & 0 & 1 & 1
  \end{pmatrix}
  $$
  diagonalizes the quadratic form, and with
  $$
  x=(1,0,0,0,0)\in \mathcal C(L)^+
  $$
  Dawes checks
  $$
  (P^{-1}\theta P)^\tau x=
  \left(3,4,6,-\frac12\sqrt2+1,\frac12\sqrt2+1\right)
  \in \mathcal C(L)^+.
  $$

Expected outcome:
$$
v_1\sim_{\widetilde O^+(L)} v_2.
$$

### Example 2.6: Algorithm 2.3 fixture

Input data:

- lattice
  $$
  L=U\oplus A_3
  $$
  with the same Gram matrices as in Example 2.2;
- vectors
  $$
  v_1=(1,-1,0,0,0),
  \qquad
  v_2=(1,0,1,0,0);
  $$
- subgroup
  $$
  \Gamma=\widetilde{SO}^+(L).
  $$

Validation targets from Dawes's calculation:

- normalization data:
  $$
  c_1=c_2=1,
  \qquad
  w_1=v_1,
  \qquad
  w_2=v_2,
  \qquad
  w_1^2=w_2^2=-2,
  \qquad
  \alpha_1=\alpha_2=1;
  $$
- bases for the complements:
  $$
  K_1=
  \begin{pmatrix}
  1 & 0 & 0 & 0 \\
  1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 \\
  0 & 0 & 1 & 0 \\
  0 & 0 & 0 & 1
  \end{pmatrix},
  \qquad
  K_2=
  \begin{pmatrix}
  1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 \\
  0 & 0 & 1 & 0 \\
  0 & 1 & -2 & 0 \\
  0 & 0 & 0 & 1
  \end{pmatrix};
  $$
- complement Gram matrices:
  $$
  G(K_1)=
  \begin{pmatrix}
  2 & 0 & 0 & 0 \\
  0 & -2 & -1 & 0 \\
  0 & -1 & -2 & -1 \\
  0 & 0 & -1 & -2
  \end{pmatrix},
  \qquad
  G(K_2)=
  \begin{pmatrix}
  0 & 1 & 0 & 0 \\
  1 & -2 & 3 & -1 \\
  0 & 3 & -6 & 2 \\
  0 & -1 & 2 & -2
  \end{pmatrix};
  $$
- discriminant-group structure:
  $$
  D(K_1)\cong C_1\oplus C_1\oplus C_2\oplus C_4\cong D(K_2);
  $$
  Dawes then invokes Theorem 2.3 to conclude
  $$
  K_1\cong K_2;
  $$
- Smith-normal-form output matrices:
  $$
  Q(G(K_1))=
  \begin{pmatrix}
  0 & -1 & 3 & 2 \\
  -1 & 0 & 2 & 1 \\
  1 & 0 & -2 & -2 \\
  -1 & -1 & 4 & 3
  \end{pmatrix},
  \qquad
  Q(G(K_2))=
  \begin{pmatrix}
  1 & 1 & 1 & 0 \\
  1 & 0 & 0 & 0 \\
  0 & 0 & -1 & -1 \\
  -1 & 0 & -2 & -3
  \end{pmatrix};
  $$
- discriminant generators:
  $$
  x_1=\frac12(3,3,2,-2,4),
  \qquad
  x_2=\frac14(2,2,1,-2,3),
  $$
  $$
  y_1=\frac12(1,0,-1,2,-2),
  \qquad
  y_2=\frac14(0,0,-1,2,-3),
  $$
  with
  $$
  D(K_1)\cong \langle x_1,x_2\rangle \bmod L,
  \qquad
  D(K_2)\cong \langle y_1,y_2\rangle \bmod L;
  $$
- discriminant-form formulas on $C_2\oplus C_4$:
  $$
  q_{K_1}(a,b)=-\frac{3a^2}{2}-\frac{b^2}{4}-ab \pmod{2\mathbb Z},
  $$
  $$
  q_{K_2}(a,b)=-\frac{3a^2}{2}-\frac{3b^2}{4} \pmod{2\mathbb Z};
  $$
- gluing maps:
  $$
  \lambda_1=
  \begin{pmatrix}
  1 & -1 & 0 & 0 & 0 \\
  1 & 1 & 0 & -1 & -2 \\
  1 & 1 & 1 & -2 & -3 \\
  1 & 1 & 2 & 0 & -2 \\
  0 & 0 & 4 & -4 & 0
  \end{pmatrix},
  \qquad
  \lambda_2=
  \begin{pmatrix}
  0 & -1 & 2 & 1 & 0 \\
  0 & 1 & 0 & 0 & 0 \\
  1 & 0 & -1 & -2 & -1 \\
  0 & -1 & 0 & 3 & 2 \\
  0 & 0 & 0 & 4 & -4
  \end{pmatrix};
  $$
- resulting gluing subgroups:
  $$
  H_1\cong H_2\cong \langle (1,0)\rangle
  \subset C_2\oplus C_4
  \cong D(K_1)\cong D(K_2);
  $$
- discriminant-action check:
  $$
  P(G(L))=
  \begin{pmatrix}
  1 & 0 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 1 & 0 \\
  0 & 0 & -1 & -2 & 1
  \end{pmatrix},
  $$
  $$
  \overline\varphi=(1),
  \qquad
  \overline\psi=
  \begin{pmatrix}
  1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 \\
  0 & 0 & 1 & 1 \\
  0 & 0 & 0 & 3
  \end{pmatrix},
  $$
  and Dawes checks that the resulting $\theta$ acts trivially on $D(L)$.

Expected outcome:

- first
  $$
  v_1\sim_{O_{\{1\}}(L)} v_2,
  \qquad
  O_{\{1\}}(L)=\widetilde O(L),
  $$
  since the required discriminant action is trivial;
- then, by Lemma 2.4,
  $$
  v_1\sim_{\widetilde{SO}^+(L)} v_2.
  $$

## Bottom Line

Dawes gives one general algorithm and then two stricter specializations:

- **Algorithm 2.1** handles the definite-complement case for arbitrary
  $\Gamma \subset O(L)$.
- **Algorithm 2.2** handles a narrower indefinite-complement case under explicit
  discriminant-form and surjectivity hypotheses.
- **Algorithm 2.3** is the coordinate implementation of Algorithm 2.2.
