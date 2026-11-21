::: {.lemma #lem:cremona-second-plane-model-general title="A second plane model by quadratic Cremona at a general ten-nodal sextic"}
For a general point $(Z;p_1,\dots,p_{10})$ of the base $V$ of @not:d2-plane-sextic-base, after relabelling the first three nodes, the following hold. The points $p_1,p_2,p_3$ are not collinear, no fourth node lies on a line $L_{ij}=\overline{p_ip_j}$ with $1\le i<j\le3$, and for every such line
$$
i(Z,L_{ij};p_i)=i(Z,L_{ij};p_j)=2,
$$
while its two remaining intersection points with $Z$ are simple, distinct, and disjoint from $p_1,p_2,p_3$.

For such a point put $S=\Bl_{p_1,\dots,p_{10}}\PP^2$ and let $q$ be the standard quadratic Cremona involution with fundamental points $p_1,p_2,p_3$. Then $q$ lifts to an isomorphism from $S$ to the blowup of $\PP^2$ at ten points, with line class and ten exceptional classes
$$
A=2H-E_1-E_2-E_3,\qquad
G_{12}=H-E_1-E_2,\quad G_{13}=H-E_1-E_3,\quad G_{23}=H-E_2-E_3,\quad G_k=E_k\ (4\le k\le10).
$$
The three $G_{ij}$ are the strict transforms of the $L_{ij}$, smooth disjoint $(-1)$-curves. The strict transform of $q(Z)$ is $-2K_S$, and $q(Z)$ is an irreducible sextic with exactly ten ordinary double points. In particular, $q$ gives a second plane presentation of the same classical Coble surface, and $3A-\tsum_{i<j}G_{ij}-\tsum_{k\ge4}G_k=-K_S$.
:::

::: {.proof}

*General position.* The unlabelled locus $\Sigma=U_{6,0}$ is nonsingular and its ambient Severi variety is irreducible, so an open condition is dense as soon as it is nonempty and the bad incidence or tangency locus is everywhere proper [@HM98, Theorem (1.49)(1)--(3)]. Represent a general rational sextic by $\psi\colon\PP^1\to\PP^2$. Its normal bundle has degree $3d+2g-2=16$ and its Kodaira--Spencer map is onto [@HM98, Corollary (3.42)]; tangency deformations are read from normal sections by [@HM98, Lemma (3.44)]. Since $\PP^1$ has ten double points of $\psi^*L$ for every general line $L$, sections of this degree-$16$ bundle still separate tangent jets after vanishing at the finitely many preimages that preserve a chosen collision. Hence each condition that three nodes be collinear, that a fundamental line be tangent at a base node, or that one of its residual intersections coalesce or be nontransverse is a proper algebraic condition, with a normal deformation destroying it. There are finitely many such conditions, so their complements meet in a dense open set. This is the general point in the statement; an arbitrary member of $V$ need not satisfy it.

*The lifted isomorphism.* After a projective change of coordinates the map is $q([x:y:z])=[yz:xz:xy]$. The closure of its graph is the blowup at the three coordinate vertices, and the second projection contracts the strict transforms of the three coordinate lines: in each standard chart the graph equations are those of the blowup, and gluing the charts proves both assertions. Because no other $p_k$ lies on a fundamental line, blowing up those seven points as well gives the displayed lift to $S$, with $A$ the line class of the target and the ten $G$'s its exceptional curves. Each $G_{ij}$ is the strict transform of a line through two blown-up points, hence a smooth rational curve with $G_{ij}^2=1-1-1=-1$; two of them meet only above a fundamental point and their strict transforms are disjoint. For $k\ge4$, $G_k=E_k$ is disjoint from the three line curves. Thus all ten $G$'s are disjoint smooth $(-1)$-curves. Intersections with $A$ and expansion in the original frame give $A^2=1$, $A\cdot G=0$ for every $G$, and
$$3A-\tsum_{i<j}G_{ij}-\tsum_{k\ge4}G_k=3H-\tsum_{i=1}^{10}E_i=-K_S.$$

*Nodality of the image.* Let $C\subset S$ be the strict transform of $Z$, smooth because every singularity of $Z$ is an ordinary double point. For an old exceptional curve $E_i$, the two distinct tangent directions at the node give two simple points of $C\cap E_i$. For $G_{ij}$, Bézout and removal of the two base points give $C\cdot G_{ij}=2$; the general-position condition makes these two intersection points simple and distinct, and puts them away from every old exceptional curve. Blowing down the ten disjoint curves $G$ therefore gives ten distinct points. At each point the two simple intersections give two smooth branches whose tangent directions correspond to the two distinct points on the contracted exceptional curve, so the image has an ordinary double point. Away from the contracted curves the blowdown is an isomorphism and creates no further singularity. The image is irreducible because $C$ is, its degree is $A\cdot C=-2K_S\cdot A=6$, and the class calculation just displayed identifies $[C]$ with $-2K_S$ in both frames. This proves the second plane presentation.
:::

