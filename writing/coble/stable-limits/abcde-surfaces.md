# ADE and folded components of stable Enriques limits {#sec-abcde-surfaces}

## Anticanonical and del Pezzo ADE surfaces

An irreducible component of a stable K3 pair with a nonsymplectic involution is an anticanonical ADE surface of the form
$$
\pi\colon (X,D+\eps R)\longrightarrow
\left(Y,C+\frac{1+\eps}{2}B\right).
$$
Here $(Y,C)$ is a log del Pezzo pair of index $2$ with reduced boundary and nonempty non-klt locus, $B\in\abs{-2(K_Y+C)}$ is ample Cartier, and
$$
X=\operatorname{Spec}_Y\bigl(\mathcal O_Y\oplus\mathcal O_Y(K_Y+C)\bigr),
\qquad R=\tfrac12\pi^*B,\quad D=\pi^*C.
$$
The equation of $B$ supplies the multiplication in the algebra. The index-one cover satisfies $K_X+D\sim0$, and the Hurwitz identity is
$$
K_X+D+\eps R
=\pi^*\left(K_Y+C+\frac{1+\eps}{2}B\right).
$$
The two kinds of pair correspond bijectively [@AT17, Lem. 2.3; @AEGS25, §6]. The components in Type III carry ordinary ADE Dynkin labels; those in Type II carry affine $\widetilde A$, $\widetilde D$, or $\widetilde E$ labels.

## Type III equations and priming

For the toric examples, let $Q\subset\ZZ^2$ be the polygon of the del Pezzo pair $(Y,C)$ and $L_Q$ its ample line bundle. Two sides at a distinguished vertex give $C=C_1+C_2$. A section $f$ of $L_Q$ has coefficient $1$ at the three distinguished vertices, coefficients $a_i$ at the Dynkin nodes, and zero at the other lattice points. In the examples of [@AEGS25, §6], the equations are

| Type | Section $f$ |
| --- | --- |
| $A_5$ | $1+y^2+x^6+\sum_{i=1}^{5}a_ix^i$ |
| $A_1^-$ | $x+y^2+x^3+a_1x^2$ |
| $A_0^-$ | $1+y^2+x$ |
| $A_4^-$ with a primed end | $y+x^2y^2+x^3+a_1xy+a_2+a_3x+a_4x^2$ |
| $D_5^-$ | $y^2+x^2y^2+x^3+a_1xy+a_2y+a_3+a_4x+a_5x^2$ |
| $D'_8$ | $y^2+x^2y^2+x^4y+a_1xy+a_2y+\sum_{i=0}^{4}a_{i+3}x^i+a_8x^3y$ |
| $E_7$ with a short side | $y^3+x^2y^2+x^4+a_1xy+a_2y^2+a_3y+a_4+a_5x+a_6x^2+a_7x^3$ |

The remaining sides of $Q$ have lattice distance $2$ from the distinguished vertex, the polygonal form of $B\sim-2(K_Y+C)$. Put $Q$ in $\ZZ^2\times\{0\}$ and add the vertex $p_0+(0,0,2)$ over the distinguished vertex $p_0$. The pyramid $P$ gives the toric variety $V_P$; the anticanonical ADE surface is the hypersurface
$$
X=\{z^2+f(x,y)=0\}\subset V_P,
\qquad \iota_{\mathrm{dP}}(x,y,z)=(x,y,-z).
$$
Its quotient is $Y=V_Q$. Varying the Dynkin coefficients gives $\CC^n$, the Weyl quotient of $\operatorname{Hom}(\Lambda^*,\CC^*)$ for the ADE root lattice $\Lambda$ of rank $n$ [@AEGS25, §6].

The sublattice $2\ZZ^2$ marks even vertices. A blue boundary edge ending at an even vertex has length $2$ and is undecorated; an edge ending at an odd vertex has length $1$ and receives a minus or prime decoration. Priming blows up $D\cap R$ on $X$, or makes the corresponding weighted blowup at $C\cap B$ on $Y$ (@def:priming). A long side meets $R$ twice and a short side once. Once every such point on a side has been blown up, the strict transforms satisfy $D_i'\cdot R'=0$, and $\abs{mR'}$, for sufficiently large $m$, contracts $D_i'$. This explains the loss of one or both boundary components in the primed shapes [@AT17, §3C; @AEGS25, §6].

## Type II equations

The two ends of the distinguished boundary segment have coefficient $1$; its interior distinguished point has coefficient $\lambda$. Three sections from [@AEGS25, §6] are

| Type | Section $f$ |
| --- | --- |
| $\widetilde E_7$ | $y^4+\lambda x^2y^2+x^4+a_1xy+a_2y^3+a_3y^2+a_4y+a_5+a_6x+a_7x^2+a_8x^3$ |
| $\widetilde E_8^-$ | $y^3+\lambda x^2y^2+x^6+a_1xy+a_2y^2+a_3y+\sum_{i=0}^{5}a_{4+i}x^i$ |
| $\widetilde D_8^-$ | $y^2+\lambda x^2y^2+x^4y^2+a_1xy+a_2x^3y+a_4x^4y+\sum_{i=0}^{4}a_{i+5}x^i$ |

The nonzero tuple $(a_i)$ has weighted projective coordinates with weights equal to lattice distances from the distinguished segment. For fixed $\lambda$ the parameter spaces are, respectively,
$$
\PP(1^2,2^3,3^2,4),\qquad
\PP(1,2^2,3^2,4^2,5,6),\qquad
\PP(1^4,2^{2n-3})\quad(\widetilde D_{2n}).
$$
The section on the distinguished segment defines a double cover of $\PP^1$ by an elliptic curve. Varying $\lambda$ gives a family of weighted projective spaces over the $j$-line; its fiber over $j(E)$ is the Weyl quotient of $\operatorname{Hom}(\Lambda,E)$ [@AEGS25, §6].

The affine $\widetilde A_{2n-1}$ case is instead a double cover of a cone over an elliptic curve. For $E_q=\CC^*/q^{\ZZ}$, $0<|q|<1$, and a line bundle $L$ of degree $n$, set
$$
\theta_i(x)=\sum_{k\equiv i\pmod{2n}}q^{k(k-1)/2}x^k,
\qquad g(x)=\sum_{i\in\ZZ/(2n)}c_i\theta_i(x),
\qquad f(x,y)=y^2+g(x).
$$
The $\theta_i$ are sections of $L^2$. For a nonzero coefficient tuple, $f$ descends from the square of the tautological line bundle on $\PP(\mathcal O_E\oplus L)$ to the cone obtained by contracting its exceptional section. The equation $z^2+f=0$ defines the anticanonical double cover, with $\iota_{\mathrm{dP}}(x,y,z)=(x,y,-z)$ [@AEGS25, §6].

## Two commuting involutions

For a log canonical pair $(X,D)$ with $K_X+D\sim0$, call an involution symplectic or nonsymplectic according as it acts by $+1$ or $-1$ on $H^0(X,\mathcal O_X(K_X+D))$. The local form $dx\wedge dy/y$ shows that a nonsymplectic quotient cannot ramify along an irreducible component of $D$ [@AEGS25, §6].

::: {.proposition #prop:abcde-two-covers title="The index-one and index-two quotient surfaces"}

Let $\pi\colon(X,D+\eps R)\to(Y,C+\tfrac{1+\eps}{2}B)$ be an anticanonical ADE cover with involution $\iota_{\mathrm{dP}}$. Let $\iota_{\mathrm{En}}$ be a second, commuting, nonsymplectic involution. Assume its induced involution $\tau$ on $Y$ and $\iota_{\mathrm{dP}}$ have finite fixed loci. Put $\iota_{\mathrm{Nik}}=\iota_{\mathrm{dP}}\iota_{\mathrm{En}}$ and form the quotients
$$
Z=X/\iota_{\mathrm{En}},\qquad Z'=X/\iota_{\mathrm{Nik}},
\qquad W=Y/\tau.
$$
Write $\psi\colon X\to Z$, $\psi'\colon X\to Z'$, $\varphi\colon Y\to W$, $\rho\colon Z\to W$, and $\rho'\colon Z'\to W$. Let $D_Z,R_Z,D_{Z'},R_{Z'},C_W,B_W$ be the descended divisors. Then $R=\psi^*R_Z=\psi'^*R_{Z'}$, $D=\psi^*D_Z=\psi'^*D_{Z'}$, and
$$
R_Z=\tfrac12\rho^*B_W,\quad R_{Z'}=\tfrac12\rho'^*B_W,
\qquad D_Z=\rho^*C_W,\quad D_{Z'}=\rho'^*C_W.
$$
The pair $(W,C_W+\tfrac{1+\eps}{2}B_W)$ is del Pezzo ADE and $Z'$ is its index-one anticanonical cover. The quotient $Z$ has index $2$:
$$
2(K_Z+D_Z)\sim0,\qquad K_Z+D_Z\not\sim0.
$$
For $T=Z,Z'$, with its corresponding divisor pair $(D_T,R_T)$ and map $\rho_T\colon T\to W$,
$$
K_X+D+\eps R=\psi_T^*(K_T+D_T+\eps R_T),\qquad
K_T+D_T+\eps R_T=\rho_T^*(K_W+C_W+\tfrac{1+\eps}{2}B_W).
$$
The map $\rho'$ branches along $C_W$ and some isolated branch points of $\varphi$. The map $\rho$ branches along these loci and along components of $C_W$ that branch in $Y\to W$. At a point $p\in\operatorname{Branch}(\varphi)\setminus C_W$, exactly one of $\rho$ and $\rho'$ branches [@AEGS25, Prop. 6.1].
:::

::: {.proof}

The quotient diagram gives the divisor pullbacks. Hurwitz gives the canonical identities. The involution $\iota_{\mathrm{Nik}}$ is symplectic, so its invariant canonical eigensheaf satisfies $\mathcal O_{Z'}(K_{Z'}+D_{Z'})\simeq\mathcal O_{Z'}$; the index-one assertion follows from the ADE double-cover correspondence [@AT17, Lem. 2.3].

For either quotient $T$, the norm of $K_X+D$ is $2(K_T+D_T)$, so $2(K_T+D_T)\sim0$. The eigensheaf decomposition is $\psi_{T*}\mathcal O_X=\mathcal O_T\oplus\mathcal A_T$, with $\mathcal A_T\not\simeq\mathcal O_T$ because $X$ is connected. The canonical eigensheaf is invariant for $Z'$ and anti-invariant for $Z$, hence $\mathcal O_Z(K_Z+D_Z)\simeq\mathcal A_Z$ is nontrivial.

Finally, let $p\in\operatorname{Branch}(\varphi)\setminus C_W$ and let the two points over it in the anticanonical cover be $r_1,r_2$, interchanged by $\iota_{\mathrm{dP}}$. They coalesce in $Z$ exactly when $\iota_{\mathrm{En}}(r_1)=r_2$; as $\iota_{\mathrm{Nik}}=\iota_{\mathrm{dP}}\iota_{\mathrm{En}}$, this is exactly when they do not coalesce in $Z'$. This proves the complementary branching statement [@AEGS25, proof of Prop. 6.1].
:::

## Quotients on the torus and by polytope symmetries

Suppose $X$ has equation $z^2+f(x,y)=0$ and $\iota_{\mathrm{En}}(x,y,z)=(-x,-y,-z)$. If all monomials of $f$ lie in
$$
\ZZ^2_{\mathrm{even}}=\{(a,b)\in\ZZ^2:a+b\in2\ZZ\},
$$
then $Y$ and $W$ are toric for the same polygon $Q$, with lattices $\ZZ^2$ and $\ZZ^2_{\mathrm{even}}$, respectively. Likewise $X$ and $Z$ use the same pyramid $P$ with lattices $\ZZ^3$ and $\{(a,b,c):a+b+c\in2\ZZ\}$. The quotient map $Y\to W$ branches at the torus-fixed vertices, and on the long boundary sides adjacent to the distinguished vertex. The index-two cover $Z\to W$ branches at that vertex and on those boundary sides; at isolated branch points away from $C_W$, the index-one cover $Z'\to W$ branches at the complementary subset (@prop:abcde-two-covers). In the square example $Q=[0,2]^2$, $Y=\PP^1\times\PP^1$ and $W$ has four $A_1$ torus-fixed points. In the triangle with vertices $(0,0),(2,0),(2,2)$, $Y=\PP^2$ and $W=\PP(1,1,2)$ [@AEGS25, §6B].

Write $\alpha:2={}_2\beta\subset\gamma$ when $\alpha$ is the ADE type of $X\to Y$, ${}_2\beta$ is the type of the index-two cover $Z\to W$, and $\gamma$ is the ADE type of the index-one cover $Z'\to W$; omit $\gamma$ when $\beta=\gamma$. The torus involution gives the following families [@AEGS25, §6B]:

| ADE cover | Index-two type | Index-one type when distinct |
| --- | --- | --- |
| $A_{4n-1}$ | ${}_2A_{2n-1}$ | |
| $A_{4n+1}$ | ${}_2\bar A_{2n-1}^{-}$, ${}_2{}^{-}\!A_{2n}$, or ${}_2A_{2n}^{-}$ | |
| $D_{4n}$ | ${}_2{}'B_{2n}^{-}$ | ${}'D_{2n+1}^{-}$ |
| $D_{4n+2}$ | ${}_2{}'B_{2n+1}^{-}$ | ${}'D_{2n+2}$ |
| $\widetilde D_{4n}$ | ${}_2\widetilde C_{2n}$ | $\widetilde D_{2n+2}$ |
| $\widetilde E_7$ | ${}_2\widetilde B_3$ | $\widetilde D_4$ |
| $\widetilde A_{4n-1}$ | ${}_2\widetilde A_{2n-1}$ | |

The toric quotient $(W,C_W)$ has the same polygon $Q$ in the even lattice. Its ADE label is read from this polygon, with the decorated cases determined by the non-klt singularities [@AT17, Fig. 9, Tables 2–3]. If $c$ is the distinguished vertex and $v_i$ the adjacent vertices, the sides $(c,v_i)$ that are long in the even lattice can be indexed by $i\equiv0\pmod4$. The map $Z\to W$ branches along their boundary divisors and at $c$, has two $A_1$ points over each intersection of such a divisor with $B_W$, and is unramified over the vertices $v_i$ indexed by $i\equiv2\pmod4$ [@AEGS25, §6B].

For $Q=[0,2]^2$, take the two boundary fibers through $(2,2)$ and $B\in|\mathcal O(2,2)|$. The del Pezzo ADE type of $(Y,C+B/2)$ is $D_4$, that of $(W,C_W)$ is ${}'D_3^{-}$, and the index-two type is ${}_2{}'B_2^{-}$. The two anticanonical double covers of $W$ branch over complementary pairs of its four torus-fixed $A_1$ points, as well as over $B_W$. For the triangular $Q$, take the two sides through $(2,2)$ and $B\in|\mathcal O_{\PP^2}(2)|$. The quotient $W$ is the quadratic cone; $(Y,C)$ has type $A_1$ and $(W,C_W)$ type $A_0^-$. The index-two cover branches over $B_W$ and the long boundary side, with two $A_1$ points over that side's intersection with $B_W$ and two over the apex. The index-one cover branches over $B_W$ and the apex and is isomorphic to $\PP^2$ [@AEGS25, §6B].

For a polytope involution $\tau(x,y)=(x^{-1},-y)$, take $\iota_{\mathrm{En}}(x,y,z)=(x^{-1},-y,-z)$. In the affine $\widetilde A_{2n-1}$ case, the involution is $(x,y,z)\mapsto(qx^{-1},-y,-z)$ and sends $\theta_i$ to $\theta_{4n-i}$; the defining equation is invariant exactly when $c_i=c_{-i}$ [@AEGS25, §6C]. In the finite $A_{4n-1}$ example, the symmetric equation has
$$
f=y^2+x^{-2n}+\sum_{i=1}^{2n-1}a_ix^{-2n+i}+a_{2n}
+\sum_{i=1}^{2n-1}a_{4n-i}x^{2n-i},
\qquad a_i=a_{4n-i},
$$
giving $2n$ free parameters. With $u=y+\sqrt{-1}z$ and $v=y-\sqrt{-1}z$, the equation becomes $uv+f=0$ and the involution on the eliminated-coordinate chart is $(x,u)\mapsto(x^{-1},-u)$ [@AEGS25, §6C].

The polytope involution gives these further families [@AEGS25, §6C]:

| ADE cover | Index-two type | Index-one type |
| --- | --- | --- |
| $A_{4n-1}$ | ${}_2{}''B_{2n}$ | ${}''D_{2n+2}$ |
| $\bar A_{4n-3}^{-}$ | ${}_2{}''B_{2n-1}^{-}$ | ${}''D_{2n+1}^{-}$ |
| ${}'A_{4n-1}'$ | ${}_2{}''B_{2n}'$ | ${}''D_{2n+2}'$ |
| $\widetilde D_{4n}$ | ${}_2\widetilde B_{2n}$ | $\widetilde D_{2n+2}^{\prime\prime}$ |
| $\widetilde A_{4n-1}$ | ${}_2\widetilde C_{2n}$ | $\widetilde D_{2n+4}^{\prime\prime\prime\prime}$ |

In the first row $Y=\PP(1,1,2n)$ and its minimal resolution is $\mathbb F_{2n}$. The lifted involution fixes four points: two on the negative section and two on a positive section. Their images give four $A_1$ points in the quotient of $\mathbb F_{2n}$; after the contraction to $W$, three singularities remain. The one on $C_W$ has resolution chain with negatives of self-intersections $(2,n+1,2)$. The symmetry condition $a_i=a_{4n-i}$ yields the $2n$ parameters above. The corresponding formula for $A_{4n-3}$ has a fixed curve, so it does not define an Enriques-type involution [@AEGS25, §6C].

## Components in stable Enriques degenerations

For the $(18,2,0)_1$ cusp of the degree-four hyperelliptic K3 moduli space, the maximal Type III degeneration has sixteen $A_0^-$ components; the other degenerations arise by smoothing double curves according to relevant elliptic subdiagrams. For the $(18,0,0)_1$ cusp, the maximal model starts with eighteen $A_0^-$ components. The blowup at $R\cap D_1$ on adjacent components, followed by contraction of the resulting fiber classes, produces the partially collapsed “smashed pumpkin” model. Relevant maximal parabolic subdiagrams determine Type II components of affine ADE type [@AEGS25, §7A–B].

The Enriques quotient of a Type III K3 stable model is determined by the folding involution at each of the five cusps. At cusp $1$ the action on the spherical dual complex is antipodal, and the quotient has dual complex $\RP^2$; its components occur in exchanged pairs. At cusps $2$, $3$, and $4$ the action is a reflection, giving both exchanged components and fixed components of B type. At cusp $5$ the action agrees on the dual complex with the del Pezzo involution: every component is fixed and its quotient belongs to the torus-involution family above. The ramification divisor forms a cycle at cusps $1$ and $5$ and a chain at cusps $2$, $3$, and $4$. Type II components correspond to relevant connected parts of maximal parabolic subdiagrams, with the same folding rule [@AEGS25, §7C–D].

The Coxeter diagram and its folded elliptic or parabolic subdiagram therefore specify which component shapes and double curves survive. The invariant root coordinates $\ell_i$ specify the corresponding integral affine sphere or its Type II segment (@sec-ias-degenerations). An equivariant divisor model realizes that affine data; quotienting by the Enriques involution gives the dlt Enriques model, and contracting by the descended ramification divisor gives its KSBA pair [@AEGS25, §§4, 7]. On the moduli space, an irrelevant folded root labels a wall that this contraction erases. Deleting precisely the faces made only of irrelevant folded roots yields the generalized Coxeter semifans of @thm:ksba_semitoroidal_En2 [@AEGS25, Def. 5.4, Lem. 5.5].
