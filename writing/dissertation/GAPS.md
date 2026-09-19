# Open items

Things noticed while moving the dissertation from LaTeX back to Markdown that need the author's judgment.
None of them blocks the build, which compiles with no LaTeX errors.

## Unfinished text

- `sections/3-part-main-theorem/7-chapter/999-appendix.md`, the $D_n$ entry: the sentence stops mid-word, at "We take $D_n$ to mean $D_n(-1)$, and identify th".
  Every neighbouring type ends with its Coxeter diagram; this one has none.
  The break is in the July 2025 draft and in the submitted LaTeX, so it is unfinished writing rather than damage from the move.

- Three `\todo` markers remain, in the lattice classification section, the Scattone section, and the five-cusps section.

- Five `\Cref` targets name results that exist under no label anywhere in the
  text, so they print as bold question marks. Each needs either the statement
  it points at, or a pointer to the statement that replaced it:

  | target | referenced from |
  | --- | --- |
  | `def:hyperbolic-plane` | intro, the K3 and Enriques lattices |
  | `ex:root-lattices` | intro, the K3 and Enriques lattices |
  | `thm:complete-classification-0-cusps-fen2` | part III, main theorem statement |
  | `lem:fent-semitoroidal-semifans-at-cusps` | part III, main theorem statement |
  | `thm:five-semifans` | chapter 7, five cusps |

  The first two were referenced by the LaTeX too, so they predate the move.

## Possibly missing content

- `sections/1-part-combinatorial/3-chapter-enriques-k3/450-scattone.md` carries
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

## Statements to check

- `sections/2-part-moduli/4-chapter-cpt/200-toroidal.md`, the boundary lattice paragraph: it gives $\signature(I)$ and $\rank(I)$ for the isotropic sublattice $I$, but the values quoted are those of the boundary lattice $\bar T_I$.
  Reads as a naming slip rather than a wrong computation.

- `sections/1-part-combinatorial/2-chapter-lattice-theory/200-examples.md`: the definition of $V_k$ is over the 2-adic integers $\ZZ_{\hat 2}$, and the neighbouring $U_k$ over $\ZZ_2$.
  The two displays sit together and should probably agree.

## Structure

- Part II carries only its part heading; Parts I and III each open with framing prose.
  The submitted LaTeX had four subsection headings here that the Markdown never had, so this is a long-standing divergence, not a regression.

## Notes on the move

- Citation keys were remapped to the live Zotero library, so a key in the text now matches the Better BibTeX key of the item.
  Two of them changed meaning: Zotero has `Sha81` for Shah's degree 4 K3 paper and `Sha81a` for his Enriques paper, which is the opposite of the old local bibliography, and the text was swapped to match Zotero.
  Worth spot-checking the two citation sites.

- `[@Alexeev]` appears twice inside HTML comments in `sections/2-part-moduli/4-chapter-cpt/000-ksba.md`. It resolves to nothing, but the comments are invisible to the build, so nothing is broken.
