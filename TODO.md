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

**A18. The autonomous Coble compactification.** The research report states about sixty "required
theorem" targets (B2.1–B7.1, C1–C5 and the A-series lemmas) for deriving the compactification
without appeal to the Enriques programme. Not enumerated individually here; they are one programme,
and most are stated sharply enough in the report to be worked.

**A19. Dawes' Example 2.2 disagrees with the in-tree computation** (@qst:dawes-example-22). The
paper concludes $v_1\sim v_2$ in $U\oplus A_3$; the computation returns $v_1\not\sim v_2$ because
the complements have different discriminants. Unequal discriminants refute equivalence under
$\Orth(L)$ and every subgroup, whatever isometry test runs downstream, so the disagreement is not a
tooling artefact — it lies in the paper's conclusion, the transcription, or the computed
complements. The squares are consistent with the stated Gram matrices, which clears the
transcription of the vectors; recomputing the two complements settles the rest. This matters beyond
the example: Algorithm 2.3 of the same paper is the published route to A1.


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


## A note on what is not in this list

Certificates are not mathematics. Several claims in the book are true-as-computed and unproved; they
appear above only where the *mathematical* statement is at stake (B2, B3). Their evidential status is
recorded in [GAPS](writing/dissertation/GAPS.md), which is the audit trail and not a problem list.

## Coverage of this list

Read in full for this list: the open-problems chapter; `coble/lattices-and-moduli` (lattice table,
moduli basics, discriminant orbits, K3 periods and monodromy, normalization); `coble/computations`
(isotropic candidates, toolchain, CoxIter results, chamber polyhedra, isotropic orbits and Tits
buildings, lattice algorithms, periods and local monodromy); `coble/stable-limits`; `coble/degenerations`.

Not yet read at this depth: the Heegner research report (16 500 words, and the source of A18's
programme), `coble/cusp-correspondence` beyond its problem blocks, `coble/compactifications`,
`coble/surfaces-and-moduli`, `coble/coble-moduli`, the `lattice-theory` and `dissertation` trees
except where cited above. The list above is therefore complete for the chapters read and incomplete
for the corpus; treating it as final before the remainder is read would repeat the mistake it was
written to correct.

