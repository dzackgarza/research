# Outstanding mathematical problems

Writing and mathematics only. Determined by reading `writing/`, not by collecting earlier lists. The
book's own [open-problems chapter](writing/coble/open-problems/open-problems.md) is one input; several
problems below are stated elsewhere in the corpus and never reach it, and one entry there rests on a
hypothesis that fails for the lattice it is applied to. Code, tooling, and computation status are not
in this file: library work is upstream
([`sage-extensions` #7--#13](https://github.com/dzackgarza/sage-extensions/issues)) and evidence
status is in [GAPS](writing/dissertation/GAPS.md).

Three classes, because they need different things. **A** is mathematics nobody has. **B** is open
in this programme: the answer is not known but a finite derivation or computation decides it.
**C** is not open at all and should be repaired in the text.

## A. Open mathematics

**A1. The number of $\Gamma_\Co$-orbits of primitive isotropic vectors of $T_\Co$** — the
$0$-cusps of $\fco$. At least two (@lem:stable-orthogonal-not-transitive), no upper bound known.
Equivalent for the discriminant kernel (@prop:discriminant-kernel-orbits), so one problem, not two.
The Eichler criterion is unavailable because $T_\Co$ contains no $U$. The open content is the
passage from the finite decomposition of $A_{T_\Co}$ back to the lattice: an integral parabolic
stabilizer may have proper image in the finite one.

**A2. The number of $\Gamma_\Co$-orbits of primitive isotropic planes of $T_\Co$** — the $1$-cusps
of $\fco$. $\Orth^+(T_\Co)$ is transitive (@thm:plane-transitivity-tco); for $\Gamma_\Co$ nothing
is known. The candidate separator is the subspace $\bar J\subseteq A_{T_\Co}$ a plane cuts out, and
whether it separates is undecided. $A_{T_\Co}$ has $23\,715$ two-dimensional totally isotropic
subspaces, so the invariant is far from constant but no computation has been made.

**A3. Explicit generators of $\Gamma_\Co$.** The book calls the matrix representation "a stub".
$\Gamma_\Co$ is defined as $\operatorname{Stab}_{\Orth(\ten)}(h_\Co)\cap Z_{\Orth(\ten)}(\theta)$,
and a source-backed candidate $\Gamma_\Co^\En(\delta)$ exists from the Heegner line; whether the two
coincide is itself open. A1, A2 and A4 all wait on this.

**A4. $\Gamma_\Co = \widetilde O^+(T_\Co)$?** The book defines $\Gamma_\Co=\Orth^+(T_\Co)^*$ and
separately $\widetilde O^+(L)=\ker(\rho_L,\chi_{\mathrm{sp}})$, and never says they coincide. They do,
by substitution — but the book also defines $\Gamma_\Co$ twice in incompatible ways (once as the
discriminant kernel, once as the stabilizer of $h_\Co$ cut by $\theta$), so the question of whether
those two definitions agree is real and is not settled anywhere.

**A5. Coble root-orbit uniqueness under $\gent$** (@qst:coble_root_orbit_uniqueness). Namikawa gives
it for the full Enriques group; the polarized problem needs the finite-index subgroup $\gent$, for
which it is not settled. Everything in the KSBA branch waits on it.

**A6. The quarter singularity $\tfrac14(1,1)$** (@conj:coble_quarter_singularity). Stated as the
local model for an $A_1$-node of the K3 cover fixed by $\ien$; the text says plainly it "remains
unproved; it is precisely the input awaited by the slc and ampleness verifications".

**A7. KSBA versus semitoroidal** (@conj:ksba_semitoroidal_comparison, @conj:no_moduli_loss), open on
four counts the chapter enumerates: A5, the ramification-semifan restriction identity, the injection
that the stable quotient determines its marked root, and an explicit cusp computation.

**A8. The admissibility test for Coble roots at a cusp** (@qst:coble_cusp_admissibility). Sterk
cusps $3$ and $5$ are the delicate cases. Without it the boundary dictionaries in the preliminary
KSBA work stay unverified.

**A9. Is $\mch^*_{10A_1}$ empty?** (@qst:coble-arrangement-empty). Decides whether the GIT
compactification of ten-nodal sextics is Baily–Borel or a proper semitoroidal model strictly between.
A reduction is recorded (roots of the sextic have divisibility $1$ in $\Lambda_1$), leaving
divisibility-two roots of $\Lambda_1$ whose hyperplane meets $D(T_\Co)$ properly.

**A10. The position of the three semifans** (@qst:semifan-poset-position): Coxeter, KSBA, Looijenga.
Depends on A9, and includes tracing a named degeneration — a double cubic, say — to the $0$-cusp
$(9,9,1)_1$ or the $1$-cusp $(7,7,1)_0$.

**A11. The reflection subgroup bounding each published Sterk diagram**
(@qst:sterk-reflection-subgroup, @qst:sterk-ideal-vertices). The quotients for $j=2,3,4,5$ are
mutually isometric, so their full Weyl groups are conjugate and cannot explain four inequivalent
published diagrams with $10,12,11,14$ walls. The missing datum is the subgroup induced by the
stabilizer of $\eta_j$ in the ambient arithmetic group, and the index is a covolume ratio that no
Euler characteristic supplies — in odd dimension it vanishes.

**A12. An equivariant triangulation of the integral affine sphere compatible with the marked root**
(@qst:equivariant_triangulation). Absent it, the marked-root prescription is a principle rather than
a model.

**A13. The horizontal folding involution in coordinates** — the $22\times22$ matrix of $\theta_\Co$ on
$U^3\oplus E_8^2$, with the polarization classes and the diagram's roots compared in that basis.
Existence and the eigenlattices are proved (@prop:theta-co-exists); the coordinates, the gluing
anti-isometry, and the comparison to $\Gamma_\Co^\En(\delta)$ are not.

**A14. Scattone's diagram versus AET19's.** Scattone's Figure 6.3.1 and AET19's diagram for the
$(18,2,0)$ lattice should be the same and reportedly are not; how they differ, and which is right, is
unresolved. Everything derived from $\Phi_{(18,2,0)}$ — including the folded Sterk diagrams and
A13's matrix — inherits whatever the discrepancy is.

**A15. The strong $\Gamma_\Co$-lifting in the cusp correspondence.** Weak (pointwise orbit)
compatibility is proved; equivariance and stabilizer comparison need a homomorphism.

**A16. Vector-level transitivity for $\latI_{1,8}$.** Lines only, by
@prop:rank-nine-line-transitivity. For $(2,9)$ it follows because $-\id\in\Orth^+$ supplies the sign;
$(1,8)$ is where that fails.

**A17. The global questions on hyperbolic Coxeter diagrams** (@qst:maximal-parabolic-complexity,
@conj:galois-invariance-parabolics, @qst:parabolic-count-growth, @qst:arithmeticity,
@qst:exact-covolume, @qst:regularized-theta). Genuinely open in the literature, not only here: the
cost of finding maximal parabolic subdiagrams, Galois invariance of their count, its growth with
rank, arithmeticity from the diagram, exact covolumes in odd dimension, and a regularized theta
series for an indefinite lattice.

**A18. The autonomous Coble programme.** The research report states the full chain of "required
theorems" for deriving the compactification: A1–A8 for the Heegner strategy, B2.1–B7.1 for the
autonomous strategy, C1–C5 for the reflection-folding route. They are enumerated at A31 below, where
the ones carrying independent mathematical content are separated out.

**A19. Dawes' Example 2.2 disagrees with the in-tree computation** (@qst:dawes-example-22). The
paper concludes $v_1\sim v_2$ in $U\oplus A_3$; the computation returns $v_1\not\sim v_2$ because
the complements have different discriminants. Unequal discriminants refute equivalence under
$\Orth(L)$ and every subgroup, whatever isometry test runs downstream, so the disagreement is not a
tooling artefact — it lies in the paper's conclusion, the transcription, or the computed
complements. The squares are consistent with the stated Gram matrices, which clears the
transcription of the vectors; recomputing the two complements settles the rest. This matters beyond
the example: Algorithm 2.3 of the same paper is the published route to A1.

**A20. The four arithmetic groups are not known to coincide** (@prob:group-identification, the
research report's §"Four arithmetic groups that must not be conflated"). The report defines
$\Gamma^{\mathrm{geom}}_{\Co,2}$, $\Gamma^{\mathrm{dir}}_{\Co,2}$, $\Gamma^{\mathrm{Hdg}}_{\Co,2}$
and $\Gamma^{\mathrm{cong}}_{\Co,2}$ — geometric monodromy, labeled centralizer image, Heegner
stabilizer image, and the congruence preimage — and proves no two equal. Each equality needs a
separate argument: global Torelli, labeled embedding comparison, discriminant-form gluing. The report
states the trap plainly: defining one of them to be "the group for which the desired semifan works"
is circular. Every other Coble statement inherits whichever group it was stated for.

**A21. Labeled Coble rigidity** (@prob:coble-rigidity). Two labeled tuples
$(L_{K3}, I_\Co, I_{\mathrm{dP}}, H, \alpha, \mathcal C)$ arising from the projective construction
should be conjugate by an element of $\Orth(L_{K3})$ preserving the labels. This is strictly stronger
than uniqueness of the primitive embedding of $S_\Co$, and without it no direct period quotient is
coordinate-independent.

**A22. Projective coverage** (@prob:projective-coverage). The quotient of the open nodal invariant
$(4,4)$ locus by the full centralizer of $\tau$ should be the complete direct moduli stack. The
report gives a dimension count ($12-1-2=9$) and one explicit polynomial, and says both are
insufficient: this needs irreducibility at the level of the arithmetic group and recovery of the K3
cover and both involutions from the Coble datum.

**A23. Equivalence of the resolved-cover and singular-pair moduli stacks**
(@prob:cover-singular-equivalence), compatible with base change and automorphisms. This is the
replacement for silently identifying a Heegner period point with a geometric Coble pair.

**A24. Integral cusp lifting** (@prob:cusp-lifting), and this one now has its finite half in hand.
The report records the finite computation: four orbits of nonzero singular vectors in a
$10$-dimensional plus-type $\mathbb F_2$-space, of sizes $135, 2, 270, 120$, and five orbits of
totally singular planes, of sizes $1575, 270, 9450, 3780, 8640$. The four vector sizes are exactly
the fine Heegner list $[1,2,120,135,270]$ — so B2's numbers are a finite $O(A)$ computation that
exists, and the open content is precisely the identification of that finite group with the image of
the integral parabolic stabilizer. The report's own warning says the two are not interchangeable:
a finite $O(A)$ orbit calculation does not classify cusps without a lifting theorem.

**A25. Coble Vinberg and root completeness at every polarized $0$-cusp**
(@prob:coxeter-completeness). The report's diagnosis: the four candidate wall-slice arrangements
$G^2_{\mathrm{slice}},\dots,G^5_{\mathrm{slice}}$ have $1,3,3,9$ maximal parabolic faces, and those
counts *disagree* with the finite-shadow orbit counts — so chamber completeness, arithmetic diagram
automorphisms and finite-orbit calibration must all be settled before boundary strata are enumerated.
A list of vectors or a Gram computation is not a Coxeter theorem.

**A26. The degeneration chain for the direct Coble theory** — four required theorems that stand or
fall together: integral-affine realization (@prob:affine-realization), algebraic extension of the two
involutions to divisor models (@prob:algebraic-extension), the dlt quotient (@prob:dlt-quotient), the
stable contraction by relative Proj (@prob:stable-proj), and the component classification
(@prob:component-classification). The report notes the Coble case cannot be obtained by substituting
the Coble involution into the Enriques tables, because the resolved Coble involution has a fixed
curve.

**A27. The direct semifan and semitoroidal restriction** (@prob:direct-semifan,
@prob:restricted-semifan). The subtorus lemma is local and toric; the report lists seven separate
statements needed before "intersect the AEGS semifans" is a compactification theorem rather than a
candidate construction. `warn:restrict-semifan` says the same in one line.

**A28. The two target theorems** (@prob:autonomous-theorem, @prob:comparison-theorem). Target A is
the autonomous Coble compactification; Target B is the comparison with the Enriques Heegner divisor,
which is the theorem the problem actually asks for. Target A does not imply Target B.

**A29. "The Coble $0$-cusp is Sterk cusp 2" is a conjecture that no chapter reconciles.** The
morphism-chain note states it and says in the same paragraph that it "is not recorded in open
problems" and "should be reconciled with the $(9,9,1)$ / $(7,7,1)$ Coble cusp data". It also records
the consistency check that would test it: the dissertation proves Sterk cusp 1 is
$\mathbb{RP}^2$-type and cusps 2–5 are $\mathbb D^2$-type, and the author separately claims Coble
degenerations are $\mathbb D^2$-type, so the conjecture *implies* the independently derived claim.
That check is described as "currently unexercised".

**A30. Is the Coble–Mukai lattice the natural home for the group action?**
(@qst:coble-mukai-naturality). $\mathrm{CM}(S)$ has rank $11-n$ and signature $(1,10-n)$; the
boundary configuration is primitive in $L$ but not in $\NS(S)$ for $n\geq2$. Whether the group acting
on $\mathrm{CM}(S)$ is the stable orthogonal group of $L$ or the subgroup induced from $\NS(S)$ is
open, and the odd part of the discriminant — invisible to the $2$-elementary invariants of $S_\Co$ —
is where it would show.

**A31. The strategy lemmas.** The report's Strategy A states eight required lemmas (A1–A8: root-orbit
and embedded-component, root-marked universal family, Coble-pair identification, generic
reconstruction, arithmetic cusp lifting, local toroidal normalization, semitoroidal compatibility, no
further coarsening); Strategy B states twenty-three (B2.1–B7.1) reproducing the AEGS chain
autonomously; Strategy C states five (C1–C5) for the reflection-folding route. Each is stated sharply
in the report at the given label. Strategy C is explicitly demoted: the earlier attempt "produced
wall-slice diagrams rather than Coxeter diagrams".

**A32. The $n\geq 2$ programme.** Three conjectures for $F_{\Co,n}$: that the Baily–Borel boundaries
of all ten families are computable by the $n=1$ techniques; that the ramification locus of the K3 cover
is a recognizable divisor in the Alexeev–Engel sense, which would give a semitoroidal
compactification by AEH21; and that the semifans refine or coarsen the Coxeter fans. The organizing
observation is that the ten lattices $(10+n, 12-n, \delta)$ are exactly the $g=0$ row of Nikulin's
triangle.

**A33. Three of the ten Coble families admit no Coxeter chamber at all.** Alexeev's classification,
recorded in the reflective-two-elementary chapter, shows that the even $2$-elementary lattices
$(17,5,1)$, $(18,4,1)$ and $(19,3,1)$ — rows $n=7,8,9$ of the Coble table — are not reflective, while
every other lattice on the line $r+a=22$ is. For those three, $W_r$ has infinite index in $\Orth(S)$,
Vinberg's algorithm does not terminate, there is no finite Coxeter diagram to fold, and the toroidal
compactification from a Coxeter fan is unavailable. The same theorem gives a second consequence: by
`thm:k3-automorphism-sequence`, $\Aut(X)$ is finite exactly when $S_X$ is two-reflective, so the K3
covers in those three families have infinite automorphism groups. Any programme for the $n\geq2$
families (A32) has to say what replaces the reflection data there.

**A34. Dolgachev–Zhang's open classification.** The coble-moduli chapter records, from the source, that
classifying all surfaces with finitely many smooth rational negative curves up to automorphism is open.
For Coble surfaces the finiteness itself is Coble's theorem; the classification of all such surfaces is
not.

**A35. Do the integral-affine data determine the stable limit?** @conj:classification-ia-data states
that for a fixed monodromy invariant $\lambda$ the combinatorial type $(\Gamma(\mcx_0), R_{\IA})$
determines the KSBA stable limit $(\overline{\mcx}_0, \epsilon\overline{\mcr}_0)$, and that this type
is locally constant in families. The dissertation itself records that only the converse is established
— from the divisor model to the data — and that the forward direction "does not follow from properness
of the KSBA functor or from the invariance of dual complexes under PL homeomorphism, and is not
available in the literature as far as this thesis can determine". This is the hinge the whole
divisor-model method turns on: without it, computing $B(\lambda)$ computes a candidate, not the limit.

**A36. Describe the semifan of a recognizable divisor.** The toroidal chapter states that describing
$\semifan{F}_R$ for a recognizable divisor $R$ is "currently a widely open problem", and that it is open
even for the rational-curve divisor $R_{\rcop}^{\,}$, where the semifan is characterised only as the
coarsest subdivision on which the combinatorial type of stable pairs is constant. The Enriques case is
available only because @AE22 supply the ramification-locus semifans explicitly.

**A37. The finiteness of the classifying map rests on an unproved semifan comparison.**
@lem:semifan-comparison states that $\phi$ is finite if and only if every KSBA semifan $\semifan{G}_k$
equals the constructed $\semifan{F}_k$, and @thm:no-coarsening is its discharge. But the lemma's proof
already assumes what it must show — "the crux is that given any coarsening ... points corresponding to
distinct degenerations would thus be glued together in the target, thus $\phi$ is finite if and only if
no such coarsening occurs" — and @thm:no-coarsening argues from @def:maximality-degenerations, a notion
of "maximal" degeneration introduced there for the purpose, by asserting that "maximality is a complete
moduli invariant — distinct configurations cannot be identified", which is not proved and is the very
point at issue. So the finiteness of $\phi$, on which the identification of the KSBA and semitoroidal
compactifications depends, is asserted through a definition and a claim about KSBA theory that no source
is cited for.

**A38. The restriction of the ambient semifan is taken as formal.** @prop:restriction-semifans asserts
that $\normalize{B}$ is *isomorphic* to the semitoroidal compactification for the restricted semifan
$\semifan{F}_B$, on the ground that "the restriction of the polyhedral structure follows functorially
from intersecting the hyperplane arrangements". The research report states the opposite as a warning
(@warn:restrict-semifan) and lists seven separate statements needed before "intersect the AEGS semifans"
is a theorem (A27). Two chapters of the same book therefore take opposite positions on whether
semitoroidal restriction is formal, and the dissertation's version is the one carrying the theorem.

**A39. Three open questions in the category-theory part.** The section `sec-open-statements` of
`Monoidal-Stable/Stable-Categories-of-Modules-with-Duality.md` states, and says are not proved in the
book: (i) whether the hyperbolic stabilization $S=F_{H(R)}$ of $\mathbf{Lat}_R$ can be inverted into a
pointed $\infty$-category — that is, whether there are $\mcc$ and $\iota\colon\mathbf{Lat}_R^{\simeq}\to
\mcc^{\simeq}$ with $\iota\circ S\simeq\Sigma\circ\iota$; (ii) whether any symmetric monoidal structure on
a category built from $\mathbf{Lat}_R$, other than $\perp$, has an invertible object of nonzero Witt
class; and (iii) whether the discriminant construction factors through the $\epsilon$-quadratic Poincaré
complexes over $\Z$, and through which functor. The first two are sharpened by @thm:invertible-summand,
which proves that on $\mathbf{Lat}_R$ itself the two demands — invertibility and moving the Witt class —
are incompatible.

**A40. Does the presentation of the $2$-elementary form monoid compute its $K_0$?** The classification
chapter records that freely imposing the six relations on the free commutative monoid on $p,q,u,v$ gives
the group $\Z\times\Z/4\Z$ generated by $v$ and $q$, and then says "it is not immediately clear if this
coincides with the corresponding Grothendieck group $K_0$ of the category of such quadratic forms". The
lattice-theory chapter proves the *monoid* statement (@thm:2elementary-decomposition) and is silent on
the group completion. So the presentation is known and the $K_0$ identification is not, and the two
chapters disagree about whether that is a gap.








## B. Open here, decidable by a derivation

**B1. Genus uniqueness of $T_\Co$.** This is where the chapter's own argument fails, and it matters
more than the entry admits. The text proposes to "confirm that $r > a$ forces a unique class in the
genus, so that the reduction of isotropic-orbit questions to $q_{T_\Co}$ is justified" — but
$T_\Co$ has $(r,a,\delta)=(11,11,1)$, so $r=a$, and Nikulin's $r>a$ criterion does not apply. The
same chapter elsewhere relies on exactly this gap ("surjectivity is not available at $r=a=11$").
So the justification for reading orbit questions off the discriminant form is *not* in place, and the
honest statement is not "verify $r>a$" but "settle the genus of a $2$-elementary lattice at $r=a$".

**B2. Whether $[1,2,120,135,270]$ is the $G_\Co$ decomposition.** Asserted; the order
$696\,729\,600$ and the four lengths are unproved. Consistency with $[1,255,272]$ and the index $136$
is a check on the claim and not a proof of it. Waits on A3.

**B3. Whether $[1,255,272]$ are orbits of the stated stabilizer.** The three parts are known to
partition the $528$ isotropic classes; that they are the orbits of the stabilizer of the polarization
class is not established.

**B4. Explicit primitive embedding matrices** for $T_\Co\injects\ten\injects\tdp\injects\lkt$, and
primitivity verified in coordinates rather than invoked. Feeds A13.

**B5. A worked instance of the Coble curve.** An explicit ten-nodal rational sextic $F(x,y,z)=0$ as
the image of a degree-$6$ map $\PP^1\to\PP^2$, with its K3 cover $w^2=F$. Would anchor B4 and A13.

## C. Not open — repair in the text

**C1. `F_{\Nod,2}` is written `???`** in the display of moduli spaces in
[moduli-construction.md](writing/coble/lattices-and-moduli/moduli-construction.md). Either define it
or remove the row.

**C2. The tower diagram's `?` arrow** $F_{\Co,2}\to\fco$, and the uncharacterised $\Gamma_{\Co,2}$.
Either describe the group or remove the arrow and say why the tower stops.

**C3. The open-problems entry on $(r,a,\delta)$.** Its first bullet — "compute the Gram matrices and
verify their $(r,a,\delta)$ invariants" — is done: $S_\Co\cong(11,11,1)_1$ and $T_\Co\cong(11,11,1)_2$
are computed, including the fibre counts and the order of $\Orth$. The entry should be replaced by B1,
which is the real residue.

**C4. Two verification chores phrased as questions:** `morrison-flowerpot-degenerations.md` asks to
check that a surface is $F_4$ with part of its toric boundary, and `divisor-and-dlt-models.md` asks
whether a Kulikov comparison is intended. Neither is a research problem.

**C5. A lemma whose proof assumes the theorem it feeds.** `lem:divisibilityTcoOne` is used to derive
the cusp correspondence, and its proof assumes a unique $\Gamma_\Co$-orbit of isotropic vectors of
$T_\Co$ — which is A1, the enumeration that the same section leaves open. The chapter records this
in passing; it should be stated where the lemma is used, because as it stands the cusp-correspondence
argument is circular: it consumes the very count it is meant to support.

**C6. Two chapters disagree about whether the invariants separate the $S_\Co$ orbits.** The
computations page says the Odd/Even-ordinary/Even-characteristic trichotomy "is what the cusp
correspondence sections rely on"; the open-problems chapter says the two $\Orth^+(S_\Co)$-orbits both
have quotient invariants $(9,9,1)$ and so "are not separated by the invariants of the boundary
lattice". Both cannot be the operative claim. One of them is the correct one and the other should go.

**C7. A Gram entry the report corrects and the figure transcription may not.** The research report
records, twice and as a warning, that the black nodes $\alpha_{20}$ and $\alpha_{21}$ of the square
ambient diagram have inner product $4$ and not $2$, and that "any computation based on the latter
value has the wrong rank" — the rank comes out $20$ instead of $18$. Any transcription of Sterk's
Figure 5 that used $2$ for that bond carries the wrong lattice. The two computations should be
reconciled and the surviving value stated once.

**C8. A discarded calibration is still cited by label.** The report's appendix retains the seven
finite orbit labels $245, 34, 45, 35^{(2)}, 35^{(6)}, 55^{(2)}, 55^{(6)}$ and says explicitly that
the calibration is not retained and that $245$ is incompatible with the $(-2)$-class obstruction. The
labels should not survive anywhere in the book, including in a chapter that explains why they were
discarded.

**C9. One lattice written with two types.** The Scattone method chapter calls $T_\Co$ "the
transcendental lattice $(11,11,1)_1$"; `lattices.md` and every other chapter have
$T_\Co = (11,11,1)_2$, and $S_\Co = (11,11,1)_1$. The two lattices share the triple and differ in the
sign of the form, which is exactly the confusion the chapter's own next sentence guards against. It is
one character in one place, but it is in the paragraph that warns against confusing the two lattices.

**C10. The Type II weight filtration says $W_2 = H^2$ and $W_4 = 0$.** `200-Kulikov.md` lists, for
$N^2 = 0$, "$W_0 = \ker(N)$; $W_2 = H^2$; $W_4 = 0$". The filtration is increasing, so $W_4\supseteq
W_2$; if $W_2 = H^2$ then $W_4 = H^2$. The entry is either a sign error or a transposition, and the
chapter is the one that defines the filtration, so a reader has no other source to fall back on. The
same line's $W_0 = \ker(N)$ is not the monodromy-weight convention either, in which the lowest
nonzero step is $\operatorname{im}(N)$.

**C11. Two definitions of subobject, and the second is the one the lattice part uses.**
`foundations/Categorical-Foundations.md:40` defines a subobject as a monomorphism $m\colon X\to Y$, "the
datum is the arrow $m$, not merely the domain $X$", while `foundations/Elements-and-Containment.md:24`
defines it as an *isomorphism class* of monomorphisms. Both carry distinct labels (`def:subcategory`,
`def:subobject-relation`), neither refers to the other, and the lattice-theory notion of a primitive
subobject is built on the second. One of the two should be the definition and the other a derived remark.

**C12. "Chain equivalence" is used four times and defined nowhere, and is equated with
quasi-isomorphism, which is false.** `algebraic-structures/Chain-Complexes.md:237` asserts that a chain
map is a chain equivalence exactly when it is a quasi-isomorphism. For complexes of $R$-modules that is
false: the acyclic complex $\ZZ/4\xrightarrow{2}\ZZ/4$ is quasi-isomorphic to $0$ but not contractible,
multiplication by $2$ on $\Hom(\ZZ/4,\ZZ/4)$ not being an isomorphism. No projectivity or boundedness is
assumed at `:180`. This is not cosmetic, because `Stable-Categories-of-Modules-with-Duality.md:105`
defines an $n$-dimensional Poincaré complex by requiring $\phi_0$ to be a *chain equivalence*, so the
equation with quasi-isomorphism weakens the defining condition of the book's own Poincaré complex, and
the term itself appears at four sites and is defined at none of them.

**C13. A citation that does not carry its claim.** `coble/heegner-report/coble-heegner-research-report.md:510`
cites `@prop:stabilization-discriminant` for "the discriminant of an orthogonal sum is the orthogonal sum
of the discriminants". That proposition states only $A_{S(L)}\cong A_L$ for hyperbolic stabilization. The
result used is `@prop:discriminant-orthogonal-sum`, whose title is "Discriminants of orthogonal sums".

**C14. A double dual used without statement.** The proof of the perfect-linking theorem at
`forms-quadratic/Torsion-Pairings-and-Linking-Forms.md:83` uses $(L^\#)^\# = L$ to conclude that the
adjoint of the discriminant pairing has zero kernel. The book states the metric-dual identities for
orthogonal sums and twists (`rem:dual-lattice-properties`) and not the double dual, so the step has no
premise on the page.

**C15. A true conclusion drawn from an irrelevant premise.** `foundations/Higher-Categories-and-Universes.md:488`
concludes that $\mathbf{Cat}_{\infty,\infty}$ has no zero object from the fact that $*\amalg*$ is neither
initial nor terminal. Whether $*\amalg*$ is initial or terminal is irrelevant: a zero object must be both
initial and terminal, the initial object here is $\varnothing$, the terminal one is $*$, and the argument
needed is that they are not equivalent.

**C16–C23. Eight defects in the worked examples of the lattice chapter.** All in
`dissertation/sections/1-part-combinatorial/2-chapter-lattice-theory/200-examples.md`, each stated
correctly at a second location in the book.

- *C16.* `:123` describes the half-integer roots of $F_4$ as those with an even number of minus signs.
  That gives $8$, and with $8+24$ integral roots totals $40$, not $48$; and the file's own
  $\alpha_4=\tfrac12(e_1-e_2-e_3-e_4)$ has three minus signs and is excluded by the description. The
  correct statement is `root-systems.md`, `def:root-system-F4`.
- *C17.* `:157–166` says $D_n^+\not\cong D_n^-$ for even $n$ and two lines later that $D_8^+\cong E_8$;
  both $D_8^\pm$ are even unimodular of rank $8$, hence both are $E_8$, so the file contradicts itself
  on one page. The construction is also not closed for odd $n$, and $D_n^\pm$ is not integral for
  $n\equiv2\pmod 4$. Correct form at `root-systems.md:248`.
- *C18.* `:168–189` negates $G_{E_8}^{-1}$ and the fundamental weights relative to the file's own
  positive-definite convention, so that $\beta(w_1,\alpha_1)=-1$.
- *C19.* The $E_8$ sign is unresolved across the file: `:60–62` and `:102` declare one convention,
  `:235` and `:274–290` the other, and under the declared one $\Lambda_{K3}$ has signature $(19,3)$.
- *C20.* `:68` defines a simple system by $\Z_{\ge0}\Phi=R(L)$, which is impossible — $-\alpha_1$ is a root.
- *C21.* `:250` and `:265` prove both classification theorems from "an even unimodular lattice exists
  only in ranks divisible by $8$", which $U$, $U^2$ and $\Lambda_{K3}$ refute.
- *C22.* `:114–115`: $v_8^2=8$ cannot generate $A_1$, and a single vector cannot generate $A_2$; the
  index $q$ in "$q\le i\le n$" at `:119` is never defined.
- *C23.* `:250` contradicts `:54–55` on parity; `:200` writes $w_1,\dots,w_p$ for a rank-$p+q$ lattice;
  `:307` writes "signature $(2,0)$" and reuses $U$ for $U_1$.

**C27. There are two Coble lattice tables, and the one in `tables/` is stale.**
`coble/tables/coble-lattices.md` row $n=4$ prints $D_4^{\oplus2}\oplus A_1^{\oplus4}\oplus U(2)$ beside
$(14,8,1)$, but that lattice has discriminant length $2+2+4+2=10$; row $n=5$ prints
$E_8\oplus A_1^{\oplus5}\oplus U$ beside $(15,7,1)$, but $a=0+5+0=5$. Both contradict the invariants
printed in the same row. `coble/lattices-and-moduli/coble-lattice-table.md:14,:15` has the correct
entries, and that chapter's own remark records these two forms as the *superseded* versions — which is
how they survived: the correction was made in one table and not in the other, and nothing cross-references
the two. A reader who finds `tables/` first has no way to know it is the wrong one.

**C28. The GIT model of $\fco$ is stated with the wrong dimension, twice.**
`research-statement/ResearchStatement.md:111` says $\fco$ "is birational to the moduli space of Coble
surfaces with $n=1$ boundary component constructed as a GIT quotient $(\PP^2)^{10}\sslash \PGL_3$".
That quotient has dimension $20-8=12$; $\fco$ has dimension $9$. The same claim appears at
`coble/coble-moduli/cusp-correspondence-morphism-chain.md`, where it is offered as "an independent
handle on the dimension $9$" — it cannot be, the two numbers differing by $3$.

**C24–C26. Three bibliography errors, one of them widespread.** These are citation defects, not
typographic ones: each names a different work from the one that carries the claim.

- *C24.* `@Kol23` is Kollár's *Arthur Byron Coble, 1878–1966*, a biography; the book carrying KSBA
  theory is `@Kol23a` (*Families of Varieties of General Type*). `@Kol23` is cited for KSBA claims at
  nine sites: `400-ksba-functor.md:34`, `heegner-report:131, 219, 2593`, `000-part-1.md:32`,
  `100-historical-context.md:15`, `100-defining-fen2.md:50`, `700-zmt-isomorphism.md:39`,
  `ResearchStatement.md:11`.
- *C25.* `@Loo03` is *Compactifications Defined by Arrangements. I. The Ball Quotient Case* and
  `@Loo02` is *…II. Locally Symmetric Varieties of Type IV*; `300-semitoroidal.md:7, 65, 75, 84` and
  `heegner-report:185, 223` cite `Loo03` for the Type IV theory, which is in `Loo02`. The Heegner
  bibliography additionally keys Part II as `Loo03`, so the same key names two different papers across
  the two bibliographies.
- *C26.* `@AE23a` is *The Flex Divisor of a K3 Surface*; the tower theorem it is cited for is in
  `@AE23`, *Compact Moduli of K3 Surfaces*. Sites: `000-part-2.md:40` `[@AE23a, Thm. 5.14]`,
  `5-chapter-ias-dlt/000-intro.md:55`, `4-chapter-cpt/000-ksba.md:55`.







## A note on what is not in this list

Certificates are not mathematics. Several claims in the book are true-as-computed and unproved; they
appear above only where the *mathematical* statement is at stake (B2, B3). Their evidential status is
recorded in [GAPS](writing/dissertation/GAPS.md), which is the audit trail and not a problem list.

## Coverage of this list

Read in full: all of `writing/coble` (each of the 64 files, including the Heegner research report at
2 620 lines); `writing/lattice-theory` top level, `arithmetic/`, `classification/`, `definite/`, and
the Part I lattice-theory chapters `500-nikulin-theory.md`, `600-coxeter-vinberg.md`,
`700-folding.md`, `400-group-actions.md`; `writing/dissertation` Parts II and III in full, plus
`100-main-diagram.md`; and `writing/category-theory/monoidal-stable` and `forms-quadratic` in part,
including the section that states its own open questions.

Not yet read at this depth: `writing/lattice-theory`'s remaining subdirectories; in the dissertation,
`100-foundations.md`, `200-examples.md`, `300-classification.md`, `450-scattone.md`,
`475-our-cusps.md` beyond the passages quoted above; and the rest of `writing/category-theory`
(enriched/ and the remaining forms chapters).

Categories C11–C15 and the audit of `writing/category-theory/algebraic-structures` and
`foundations` came from `ultramath` swarm `smvy0k5df`, member m3; C16–C23 from members m5 and m7,
who audited `200-examples.md` independently and agreed on every finding I checked; C24–C26 from
member m6. Every item was checked at the cited lines before entry.

Two directions of the swarm went unexecuted because the members assigned them did other, useful work
instead: the research-statement/part-intro pass, and the cross-chapter consistency pass that produced
C6, C9, C10 and A38/A40 by hand. The inconsistency hunt is the largest remaining gap in this audit.







