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
  The numbered-root Gram data is settled (the source incidence: rank 19, kernel 5, all eight
  components carrying their Kac marks, Lemma 4.7's four coincidences as relations), and the four
  cusp boundary lattices are computed on the maintained baseline from it: each has rank 17,
  signature (0,17), is even, has determinant -2 and discriminant module Z/2, with the label of
  index k = 1, 2, 3, 2 respectively.  What remains open is which even overlattice of the label
  each boundary *is*, i.e. the glue: `even_overlattice_inclusions` and one `is_isometric` call
  enter the Julia bridge and fail there with `Package JSON ... is required but does not seem to
  be installed: Run Pkg.instantiate()`, which is a provisioning item for the shared image, not
  a library defect.  `writing/coble/scripts/certificates/cusps_from_presentation.py` holds the
  consumer and its transcript.
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
