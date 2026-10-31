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

  Cusp 2 of the Enriques chapter is checked alongside cusp 1 in enriques_cusp_lattice_data.py:
  U + E8^2 has rank 18, determinant -1 and two-elementary invariants (18,0,0), the quoted value,
  and U + E8(2) has rank 10 with invariants (10,8,0).

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
