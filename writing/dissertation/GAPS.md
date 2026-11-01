# Open items

Things noticed while moving the dissertation from LaTeX back to Markdown that need the author's judgment.
None of them blocks the build, which compiles with no LaTeX errors.
What has since been settled is listed at the end, so that a reader can tell "resolved" from "never noticed".

## Unfinished text

- None. The last one, `\todo{Separate the Hodge-theoretic work}` in [[450-scattone|Scattone boundary analysis]], is resolved: the lattice-theoretic cusp enumeration and the limiting mixed Hodge structures at the boundary are now separate subsections, and the second opens by saying what it adds that the first does not supply.

## Possibly missing content

- [[450-scattone|Scattone boundary analysis]] carries
  the Scattone boundary analysis only for $F_2$, where it lists the four
  lattices of the genus $G(1)$ containing $A_{17}$. Working notes in the old
  dissertation tree also carried the parallel analysis for $F_4$, where
  $N \cong D_7$: the seven Niemeier lattices containing $D_7$

  $$\tilde E_8^{3},\ \tilde E_8 \oplus \tilde D_{16},\ \tilde E_7^{2} \oplus \tilde D_{10},\ \tilde D_{12}^{2},\ \tilde D_8^{3},\ \tilde D_9 \oplus \tilde A_{15},\ \tilde E_6 \oplus \tilde D_7 \oplus \tilde A_{11}$$

  and their orthogonal complements, giving nine possibilities, among them
  $\tilde D_{17}$, $\tilde D_{12} \oplus \tilde D_5$,
  $\langle -4 \rangle \oplus \tilde D_8^{2}$,
  $\tilde A_1^{2} \oplus \tilde A_{15}$, and $\tilde E_6 \oplus \tilde A_{11}$.
  The list displayed is the one the working notes carried. It is unsettled, and a revision of
  this note that replaced one of its items was wrong to do so; the list as it stands is neither
  verified nor known to be complete.
  Counting subdiagrams of one fixed simple-root diagram does not enumerate root embeddings: in
  the model of $E_8$ whose roots are the $\pm e_i\pm e_j$ and the half-spinors, the simple roots
  $e_1-e_2,\dots,e_6-e_7,e_6+e_7$ generate a $D_7$ inside the coordinates $1,\dots,7$, so $E_8$
  does contain $D_7$, although $D_7$ is no subdiagram of the standard $E_8$ diagram.
  Nor is $D_7$ an orthogonal direct summand of $D_n$ in the coordinate block: $D_7\oplus
  D_{n-7}$ has index $2$ in $D_n$, since $D_n$ imposes one parity condition on the whole
  coordinate vector and that block imposes two, so the gluing has to be kept and primitivity
  checked rather than assumed.
  Both points were got wrong in the previous revision of this note, which therefore does not
  correct the list either: which lattice-theoretic condition on a Niemeier lattice these seven
  items are meant to satisfy is still to be read off Scattone's construction, and until it is,
  the degree-$4$ case is open and no replacement list should be quoted.
  What the certified degree-2 data now says about the shape of the condition.  The four
  boundary lattices computed from the source presentation are one genus: rank 17, signature
  (0,17), even, determinant -2, discriminant module Z/2.  The sentence above, that the four are
  "the four lattices of the genus G(1) containing A_17", is therefore the kind of statement the
  degree-4 case needs -- a genus plus a root lattice contained with finite index -- and not a
  list of complements.  It is not yet reproduced for degree 4: the genus of the corresponding
  T_8 quotient and the root lattice whose containments enumerate the cusps would have to come
  from Scattone's ch. 5-6, which have not been read, and the seven-item list above should not be
  quoted until they are.
  The degree-4 condition has an accessible primary source, and the attribution is to
  Laza--O'Grady directly: *GIT stability of K3 surfaces of degree 4*, arXiv:1801.04845, Appendix A.
  Their Sec. 2.1 sets Lambda_N = U^2 + D_{N-2}, with D_N the negative definite Dynkin lattice and
  D_1 the rank one lattice with generator of square -4 (the family's low-rank convention, not one
  of the root types below), and F(N) = Gamma(N)\D^+(N) with Gamma(N) = O^+(Lambda_N) unless
  N = 6 mod 8, where Gamma(N) is a subgroup of index 3 in O^+(Lambda_N).  So n = 17 in Corollary
  A.5 and Theorem A.6 is N = 19 and Lambda_19 = U^2 + D_17, of rank 21; a rank two isotropic J
  leaves J^perp/J of rank 21 - 4 = 17.  Corollary A.5 identifies the image of alpha_N with the
  lattices in the genus of D_{N-2}; Theorem A.6 says a lattice in the genus of D_n (1 <= n <= 18)
  is determined by its root sublattice and lists them -- for n = 17 nine of them: D_17,
  D_9 + E_8, D_12 + D_5, D_3 + (E_7)^2, A_15 + D_2, A_11 + E_6, (D_8)^2, D_16, (E_8)^2 -- and,
  when the root sublattice has rank one less than the lattice, the lattice is an overlattice of
  R(M) + D_1.  Remark A.7 credits the cases n = 17, 18 to Scattone [Sca87, Sec. 6.3] and Camere,
  the method being the embeddings of D_k into the Niemeier lattices, tabulated in Table 9;
  Theorem A.12 and its table count the Type II components.

  It applies to the manuscript, and that is a computation rather than an inference.  The
  manuscript's convention is T_{2d} = <-2d> + U^2 + E8^2 of rank 21, so degree 4 means 2d = 4 and
  T_4 = <-4> + U^2 + E8^2.  `t4_is_lambda19.py` checks on the maintained baseline that
  T_4 is isometric to Lambda_19 = U^2 + D_17: is_isometric returns True, both being even of rank
  21, signature (2,19), determinant -4 and discriminant module Z/4.  Hence Corollary A.5 and
  Theorem A.6 do classify the rank-17 quotients in the degree-4 case, and the seven-item
  Niemeier list with its nine complements in the working notes is Theorem A.6(9) -- the nine
  lattices above, each named by its root sublattice, with D_1 = <-4> entering only the
  overlattice clause and not the list itself.

  An earlier version of this note got the indexing wrong (writing Lambda_18 = U^2 + D_16 for
  n = 17), called the case hyperelliptic degree 4 on the strength of the source's own summary
  sentence rather than its moduli definition, identified degree 4 with T_8, and called the
  difference a change of polarization.  All four were wrong; the determinant comparison alone
  settles that the n = 18 lattice is not T_4, and the isometry above settles that the n = 17 one
  is.  The count, and the two things it is a count of.  Laza--O'Grady's Sec. A.3 defines, for J in
  I_2(Lambda_N) -- rank two *saturated* isotropic -- the map alpha_N from their group's orbits,
  tilde Gamma^xi_N \ I_2(Lambda_N), to isomorphism classes of negative definite lattices of rank
  N - 2, by [J] -> [J^perp/J]; this is well defined because tilde Gamma^xi_N < O(Lambda_N) and
  O(Lambda_N)-equivalent J give isomorphic quotients.  Proposition A.4 gives the dichotomy for
  saturated J: either Lambda_N -> Hom(J, Z) is surjective, in which case J sits in U + U and
  J^perp/J lies in the genus of D_{N-2}, or its image has index two, in which case J sits in
  U + U(2) and J^perp/J is even, negative definite and unimodular -- and the second case cannot
  occur when N is not 2 mod 8.  Proposition A.11 says alpha_N is injective for N not 6 mod 8
  (with N = 14 the one exception), and Theorem A.12 draws the consequence: for N not 2 mod 8 the
  Type II components are uniquely labelled by the lattices in the genus of D_{N-2} listed in
  Theorem A.6.  For N = 19, which is 3 mod 8, all of that applies, so there are exactly nine Type
  II components, in bijection with the nine lattices.

  Two distinctions have to survive that sentence.  First, nine quotient-lattice classes is not the
  same statement as nine Gamma-orbits of primitive isotropic planes: it is nine orbits for the
  source's group, and the bijection with lattices is Proposition A.11's injectivity, not an
  identity of counts for an arbitrary group.  Second, the source's group is not the manuscript's
  by default.  Laza--O'Grady set Gamma(N) = O^+(Lambda_N) unless N = 6 mod 8, where it is a
  subgroup of index 3, and their alpha_N is defined on orbits of tilde Gamma^xi_N, a subgroup of
  O(Lambda_N); AET's Gamma_{2d}, which the manuscript follows, is the spinor norm one subgroup of
  the stabilizer of h, not the full isometry group.  So before Theorem A.12 can be applied to the
  manuscript the two groups have to be matched, with the saturation hypothesis on J checked in the
  manuscript's normalization too.  The isometry T_4 = Lambda_19 identifies the lattices and says
  nothing about the groups; that comparison is the open step, not a change of polarization.

  The Sterk construction has been run against the five subsections, on the shared image with its
  OCI environment (JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot:) and the canonical
  sage-extensions, and its transcript is kept at computations/reports/sterk-cusp-diagrams-run.txt.
  It works through five named isotropic representatives and, for each, the roots of
  v^perp/Zv and the maximal parabolic subdiagrams:

    v = e                    12 roots    9 maximal parabolic subdiagrams
    v = e'                   10 roots    2
    v = e' + f' + abar_8     12 roots    4
    v = 2e' + f' + abar_1    11 roots    5
    v = 2e + 2f + abar_1     14 roots   13

  What that does and does not settle for the chapter's claims.  The subdiagram arithmetic is
  reproduced with its named representatives, so the *structures* behind the ray counts are now
  machine output rather than assertion.  But the chapter's counts are 4/4, 2/8, 3/15, 4/12, 5/17
  (Type II/III in the Coxeter compactification), and matching those to the five rows above is not
  a lookup: cusp 1's four Type III rays correspond to the four *types* among the nine maximal
  parabolic subdiagrams of v = e (E8, E7 + A1, D8, A7 + A1), i.e. to orbits under the diagram's
  symmetries rather than to the subdiagrams themselves, and the same reduction has to be done for
  the other four before any of the counts is confirmed or corrected.  Nor is the correspondence
  between the manuscript's five cusps and Sterk's five representatives yet written down: the
  manuscript distinguishes cusp 1 by the label (10,10,0) and the others by (10,8,0), which does
  not by itself order them.

  The reduction is done on the maintained API's labelled action on the original vertices
  (G.add_vertices(range(n)) first, so no source root is only a partition member; vertices carry
  their norm through the partition, edges their labels; algorithm="sage" named explicitly, since
  this image's default Bliss backend segfaults on the smallest input).  It verifies the Type II
  counts and says nothing yet about the Type III ones:

    representative                roots  |Aut|  parabolic orbits  manuscript Type II
    3.3.7   v = e                 12     4      4                 4     verified
    3.3.9   v = e'                10     1      2                 2     verified
    3.3.10  v = e' + f' + abar_8  12     2      3                 3     verified
    3.3.11  v = 2e' + f' + abar_1 11     2      4                 4     verified
    3.3.12  v = 2e + 2f + abar_1  14     8      5                 5     verified

  A claim of "Type III does not reproduce" was made here and is withdrawn.  It came from a
  selection error, not from the manuscript: v^perp/Zv has signature (1,9) and rank 10, and by
  AET's Theorem 4.3 the cone dimension is the ambient rank minus the elliptic rank, so a Type III
  *ray* (dimension one) needs elliptic rank 10 - 1 = 9, while rank 8 counts two-dimensional cones;
  parabolic rank 8 stays right for the Type II rays.  The numbers I compared (35, 45, 84, 65, 88
  against 4, 8, 15, 12, 17) were therefore orbits of the wrong-rank subdiagrams, and the agreement
  between my two readings was tautological besides: the local maximal_elliptic(M, rank=8)
  discarded subsets larger than 8 before testing maximality, so "rank exactly 8" and
  "inclusion-maximal within rank 8" were the same set by construction and tested nothing.

  The local checker is retired.  The Type III count is taken from the owner's enumeration instead,
  CoxeterDiagrams().from_roots(labelled root family) followed by
  maximal_elliptic_subdiagrams(connected=False), which is maximality by inclusion with no rank cap,
  and its vertex sets are then acted on by the same verified full-Gram graph automorphisms rather
  than by the coarser Coxeter-order group of the owner's own orbit methods.  That run
  (computations/reports/sterk_owner_subdiagrams.py) is in progress.

  The semifan and irrelevant-subgroup statements, audited against the *retained figure
  numbering* -- which is not the Sterk script's a-indexing and had to be found first.  The diagram
  objects live in the pandoc configuration, not in this repository:
  figures/objects/coxeter/sterk-cusp-{1,3,4,5}.tikz and vinberg-10-8-0.tikz in the .pandoc
  checkout, drawn through styles/macros/tikz/constructors/dzg-coxeter.tex.  Each states its
  provenance and its numbering: "Roots: dzack_research.preamble.sterk, Sterk.sterk_roots()[Sterk_k],
  the folds of the (18,2,0) roots under J_k ... Root i is the (i+1)-th root there and is labelled
  r_i, as in 900-five-cusps.md".  So the manuscript's r_i is the object's root i, and the objects
  also fix the correspondence: cusp 1 is "Sterk 1991, diagram I", cusp 3 diagram III, cusp 4
  diagram IV, cusp 5 diagram V, and vinberg-10-8-0 is "the Coxeter diagram of the 0-cusp eta_2
  (Sterk's diagram II)".

  The exact label correspondence, from the canonical ordered root family.  The objects are the
  pinned pandoc configuration, pandoc-config@a84f0becc5b777cf193b1ca6466cd4922556f5fa, and they
  read their roots from the maintained library rather than from the archived preamble:
  sage-extensions/src/sage_extensions/sterk.py:240-281.  That block orders the five configurations
  explicitly and, zero-based, gives

    Sterk_1  r_9  = v_21                    r_10 = v_22
    Sterk_3  r_10 = orbit_sum(v_20)         r_11 = orbit_sum(v_18)
    Sterk_5  r_12 = v_21                    r_13 = v_22

  with orbit_sum the folded orbit sum used for the two Sterk_3 roots; an earlier version of this
  note called it reflect, after the archived preamble, and that name is wrong for the maintained
  source.  So the pairs the manuscript names are particular roots of these ordered configurations:
  (v_21, v_22) for cusp 1, (orbit_sum(v_20), orbit_sum(v_18)) for cusp 3, (v_21, v_22) again for
  cusp 5.  The assets mark exactly those index pairs with the infinity weight -- cusp 1 "8-9-10-11
  bold (inner products 4)", cusp 3 \coxeteredges{infinity}{10/11}, cusp 5
  \coxeteredges{infinity}{12/13} -- so b(r_i, r_j) = 4 with both norms -4 at each named pair, an
  affine A~1.  The manuscript's named pairs are present in its own diagram source and are not to be
  reinterpreted through the Sterk script's a-numbering.

  Two orderings must not be confused, and the assets say so themselves: vinberg-10-8-0.tikz 5-11
  maps the folded Sterk_2 indices 0..9 to diagram vertices 1, 3, 4, 5, 6, 7, 8, 9, 10, 2, and the
  library exposes sterks_in_TEn() and sterk5_in_U_E8_2() in orderings of their own.  No transport
  from those orderings to the separate Sterk script's a-indices appears in that file, so the
  script-to-manuscript label map is *not* established and must not be read off positions.  Anything
  that needs both numbering systems -- for instance comparing the script's subdiagram lists with the
  objects' edge lists -- waits on that map.

  With that numbering the three named-root statements check out, and my earlier "these pairs are
  not edges" conclusion is withdrawn -- it compared the manuscript's r-indices with the Sterk
  script's unrelated a-labels.  From the object files themselves: cusp 1 has "8-9-10-11 bold
  (inner products 4)", so r_9 . r_10 = 4 with both norms -4 and the pair spans an affine A~1, as
  the text says; cusp 3 has "10-11 bold"; cusp 5 has "12-13 bold".  All three statements are
  therefore consistent with the retained figure data.  What is still not computed is the finiteness
  or infinitude of any irrelevant subgroup, i.e. the semifan statements proper: the Sterk script
  does not implement the semifan construction, and nothing here substitutes for it.

  The representative-to-subsection matching is settled by source, not by counts: each object names
  its Sterk diagram number and its root family, and the root counts agree with the script's five
  representatives in the order 3.3.7, 3.3.9, 3.3.10, 3.3.11, 3.3.12 as 12, 10, 12, 11, 14.  Cusp 1
  is diagram I (12 roots), cusp 2 diagram II (10), cusp 3 diagram III (12), cusp 4 diagram IV (11),
  cusp 5 diagram V (14).

  So, separated: the Type II counts are *computed and accepted*; the lattice data are *computed and
  accepted*; the Type III counts are waiting on the owner enumeration (job jmvx3lwga, not
  restarted); the semifan/irrelevant-subgroup statements are *source claims only*, one of them
  corroborated at the level of named roots and two of them not reconcilable until the manuscript's
  root labelling is matched to the script's.

  The representative-to-subsection matching does not come from the counts: cusps 1 and 4 both have
  four Type II orbits, so the count vector cannot order them.  The matching is read off the
  manuscript's displayed subdiagram vertex sets -- cusp 1's four are
  {0,1,2,4,5,6,7,8,11}, {0,1,3,4,5,6,7,8,10,11}, {0,1,2,3,5,6,7,8,11} and {0,1,2,3,4,5,6,7,9,10} in
  the figure's indexing -- and compared with the owner-returned sets, independently of any count.

  So the chapter unit is not closed.  The actionable step is exact and needs no new source:
  reduce each representative's maximal parabolic subdiagrams to orbits under the symmetry group
  the chapter fixes, and match the five representatives to the five subsections by their quoted
  elliptic subdiagram lists -- cusp 1's four are displayed in the text and can be compared with
  the script's output vertex by vertex.

  The five Enriques cusps' lattice data are checked as one unit in
  enriques_cusp_lattice_data.py.  Cusps 1, 3, 4 and 5 all quote T-bar = (18,2,0)_1 = U(2) + E8^2
  with invariant sublattice U(2) + E8(2); cusp 2 quotes (18,0,0)_1 = U + E8^2 with U + E8(2).  The
  maintained two-elementary API gives (18,2,0) and (10,10,0) for the first pair and (18,0,0) and
  (10,8,0) for the second, matching the text in all five subsections.

  Two things the audit did not settle and does not claim.  The boundary labels (10,10,0)_1 and
  (10,8,0)_1 are the manuscript's Enriques-cusp invariants and were not recomputed here from
  L_- = H + H(2) + E8(-2); they need the five isotropic orbits and their quotients, which is the
  Sterk transcription's job.  And the arithmetic-group comparison stays open exactly as recorded
  above: Laza--O'Grady's group and the manuscript's Gamma have not been matched, so no count is
  transferred between them, in the Enriques chapter or elsewhere.

  The "Sigma versus N zero-cusp invariant" still does not resolve.  Inspected as asked: the
  introduction and historical context carry no such phrase, and the nearest textual home is the
  Enriques chapter's "The five cusps" section, where the five 0-cusps of F_{En,2} carry semifans
  Sigma_k and where N-type lattices appear in the AET sense; a Sigma-versus-N comparison could
  plausibly be about the Enriques transcendental lattice against that N.  That is a reading, not
  an identification, so nothing is asserted and the item needs its original note.
  Acceptance of the glue, when it is done, must keep the source-root images and the maintained
  inclusion and index maps -- the actual inclusion whose codomain is the computed quotient, with
  its index -- rather than resting on an isometry-class match or a determinant ratio.  For
  degree 2 that is in hand for all four rows (one inclusion for A_17 and for E_8^2 + A_1, two
  each for the two D rows, the quotient being determined in the first two cases and one of a
  pair in the others).
  The nine complements listed here and in the working notes have not been recomputed and
  should not be quoted until they are. What a complement names is a root system and not a
  lattice: at $d=1$ the four labels are root lattices of rank $17$ and determinants $2,8,8,18$,
  each sitting with finite index in the boundary lattice $J^\perp/J$ it labels, so a boundary
  lattice may be a proper overlattice of its label, and the glue subgroup is data the root
  system does not carry; for one of the four the boundary lattice is the label itself, and for
  the other three which overlattice occurs is not settled here (see
  [[450-scattone|Scattone boundary analysis]]).
  What is settled is the index. A unimodular sublattice of an integral lattice splits it
  orthogonally with no index, and `formalization/coble-enriques/Splitting.lean` proves that
  (`splits_of_unimodular`, `det_eq_mul_of_unimodular_block_diagonal`); since $J\oplus J'
  \cong U^{\oplus 2}$ for AET's complementary isotropic plane, $\det(J^\perp/J) = \pm 2$ for
  all four, and the index of the label is $1$, $2$, $2$, $3$. The lattice follows for
  $A_1\oplus E_8^{\oplus 2}$ and does not follow for the other three without a certified
  quotient and overlattice computation.
  That computation has not been run. `sage-extensions` at revision
  `441519c574cec12ada06ad586f6c3862fbca96d0` (clean checkout) has every operation it needs --
  `primitive_isotropic_subobject` (`lattices.py:7312`), `isotropic_reduction`
  (`lattices.py:5688`, `:8414`), `even_overlattice_inclusions` (`lattices.py:5937`),
  `discriminant_module` (`lattices.py:5583`), `discriminant_projection` (`lattices.py:5588`),
  `saturation` (`lattices.py:2990`), `is_primitive` (`lattices.py:8379`,
  `module_morphisms.py:1665`) with `is_saturated := is_primitive` (`module_morphisms.py:1671`)
  -- and the calls that express the cusps are written out, unexecuted, in
  `writing/coble/scripts/certificates/cusps_degree_two.sage`.
  The numbered-root Gram data is settled, and the four cusp boundary lattices are computed on
  the maintained baseline from it: each has rank 17, signature (0,17), is even, has determinant
  -2 and discriminant module Z/2, with label index k = 3, 2, 1, 2.  The glue, settled through the marked inclusion rather than through isometry.  The label's
  roots are pushed through P -> Q and the reduction of the plane, and the sublattice S of
  J^perp/J that their images span is recorded with its inclusion, index and gluing subgroup:
  A_17 gives S of determinant -18 and index 3 with glue Z/3; D_10 + E_7 gives index 2 and glue
  Z/2; E_8^2 + A_1 gives index 1 and trivial glue, i.e. the label is the boundary; D_16 + A_1
  gives index 2 and glue Z/2.  So nothing here waits on an invariant that could distinguish
  isometric candidates -- that formulation was withdrawn -- and the marked data is complete for
  all four rows.
  The library targets the research image's Sage development baseline on Python 3.14. It was not
  run on this container's Sage 10.8 / Python 3.12, which is not a supported host: nothing about
  the library is thereby in question, and provisioning an environment, or changing the library,
  belongs to the `sage` and `sage-extensions` projects rather than to this one. Until those
  calls are run on the supported baseline, no result of them is verified -- and in particular
  nothing in `writing/coble/scripts/certificates/two_elementary_checks.py` counts as verified,
  since it reimplements quotient, saturation and discriminant-group arithmetic in plain
  integers instead of going through the library. The same caution applies term by term to the
  nine items below. What the seven-item list is for is the analogue of the
  $d=1$ construction, where the four boundary lattices arise from $E_7$-complements in Niemeier
  lattices — and even there the bookkeeping is not uniform: at the level of root systems only
  three of the four come from an $E_7$ subdiagram (see [[450-scattone|Scattone boundary
  analysis]]), the fourth needing an embedding that is not a root subsystem. So the
  degree-$4$ case is incomplete, and the bound on what is missing is not a list but the
  construction itself.

  The note observes that the complements can be recovered by running Vinberg's algorithm
  on $\langle -4 \rangle \oplus U \oplus E_8^{2}$, and that the resulting
  Coxeter diagram matches Scattone 1987, Figure 6.3.1, while differing from the
  one for $(18,2,0)$ in AET. Whether the thesis wants the degree 4 case is a
  completeness decision, not a loss: the content is in Scattone.

## Structure

- The submitted LaTeX had four subsection headings in Part II that the Markdown never had, so this is a long-standing divergence, not a regression.
  Part II now opens with framing prose like the other two, but those four headings are still absent.

## Notes on the move

- Citation keys were remapped to the live Zotero library, so a key in the text now matches the Better BibTeX key of the item.
  Two of them changed meaning: Zotero has `Sha81` for Shah's degree 4 K3 paper and `Sha81a` for his Enriques paper, which is the opposite of the old local bibliography, and the text was swapped to match Zotero.
  Worth spot-checking the two citation sites.

- `[@Alexeev]` appears twice inside HTML comments in [[000-ksba|the KSBA chapter]]. It resolves to nothing, but the comments are invisible to the build, so nothing is broken.

## Settled since this list was written

Each of these was open when this list was written and is settled now; the two that appeared above have been removed from it.
The check is the one each item names, run over `sections/`.

- **Five targets with no label.** The text no longer uses `\Cref` at all; every cross-reference is written `@label`, and each of those names a label `sections/` declares.
  The five were:

  | target | was referenced from |
  | --- | --- |
  | <code>def:<wbr>hyperbolic-plane</code> | intro, the K3 and Enriques lattices |
  | <code>ex:<wbr>root-lattices</code> | intro, the K3 and Enriques lattices |
  | <code>thm:<wbr>complete-classification-0-cusps-fen2</code> | part III, main theorem statement |
  | <code>lem:<wbr>fent-semitoroidal-semifans-at-cusps</code> | part III, main theorem statement |
  | <code>thm:<wbr>five-semifans</code> | chapter 7, five cusps |

  The first two were referenced by the LaTeX too, so they predate the move.

- **The appendix's $D_n$ entry.** It now reads "We take $D_n$ to mean $D_n(-1)$, and identify the Coxeter diagram as:" and carries the $\dynkin$ diagram, so nothing stops mid-word.

- **Three `\todo` markers.** The lattice-classification and five-cusps markers are gone; the Scattone one remains, and is the only item under "Unfinished text".

- **The two 2-adic displays.** $V_k$ and $U_k$ are both written over $\ZZtwoadic$, so the neighbouring displays agree.

- **The toroidal boundary paragraph.** It now attributes $\signature$ and $\rank$ to the boundary lattice $\bar T_I$ rather than to the isotropic sublattice $I$.

- **Every statement block has a proof block.** The twenty-nine theorem, lemma, proposition and corollary blocks that had none now carry one, in the form the book's chapters use: a short derivation where the statement follows from the definitions on the page, and a one- or two-sentence citing block where it is quoted from the literature. Nothing was padded and no statement was weakened to make a proof easier.

  Three of them were not proofs waiting to be written but claims of a different status, and are now labelled as such. The Noether--Lefschetz non-normality discussion is a remark whose three mechanisms are recorded as observed rather than proved, and its second item no longer asserts that a non-snc intersection of divisors makes a variety non-normal, which is false. The determination of the KSBA limit by its dual complex is a conjecture, and it now says which direction is established (from the divisor model to the data) and that neither properness of the KSBA functor nor the invariance of dual complexes supplies the other. Zariski's Main Theorem is stated in the finite form — a finite birational morphism onto a normal variety is an isomorphism — and proved by integral closure, because that is the case the classifying map uses and the previous list of four hypotheses included normality of the source and properness of the target, neither of which appears in any form of the theorem. The quasi-finite form, which concludes only an open immersion, is recorded with it as the classical statement and is cited at [@Har10a, §V.5]; `Har77` and `Mum70` were the citations before, and neither carries the theorem in this bibliography, the `Mum70` entry being *Varieties defined by quadratic equations*.

- **Six Nikulin citations.** The tree cited `@Nik79` for Witt's analogue, the surjectivity of $\Orth(T)\to\Orth(q_T)$, and the discriminant theory. In the shared bibliography `Nik79` is *Finite groups of automorphisms of Kählerian K3 surfaces*; those results are in *Integral symmetric bilinear forms and some of their applications*, which is `Nik80`. The six sites now cite `@Nik80`, and `@Nik79` is left to the automorphism paper, which the research statement uses it for.

- **The one numeric citation.** The recognition statement in the divisor-models chapter cited `[6, Sec. 5C]`; it cites `[@AEGS25, §5C]`, which is the key the rest of the chapter uses for the same work.

- **Two references in the notation paragraph of the K3 chapter.** It cited `@def:root-lattice` and `@def:weyl-group`; the tree declares neither, and the paragraph states each symbol it introduces, so the parenthetical is gone rather than pointing at nothing.
  The root lattices themselves are presented in [[200-examples|Lattice examples]], which declares no label for them.
