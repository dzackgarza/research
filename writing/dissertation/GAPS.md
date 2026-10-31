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
  The note observes that these can be recovered by running Vinberg's algorithm
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
