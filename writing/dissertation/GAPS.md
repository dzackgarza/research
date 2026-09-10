# Open items

Things noticed while moving the dissertation from LaTeX back to Markdown that need the author's judgment.
None of them blocks the build, which compiles with no LaTeX errors.

## Unfinished text

- `sections/3-part-main-theorem/7-chapter/999-appendix.md`, the $D_n$ entry: the sentence stops mid-word, at "We take $D_n$ to mean $D_n(-1)$, and identify th".
  Every neighbouring type ends with its Coxeter diagram; this one has none.
  The break is in the July 2025 draft and in the submitted LaTeX, so it is unfinished writing rather than damage from the move.

- Three `\todo` markers remain, in the lattice classification section, the Scattone section, and the five-cusps section.

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

- `\cite{Alexeev}` appears twice inside HTML comments in `sections/2-part-moduli/4-chapter-cpt/000-ksba.md`. It resolves to nothing, but the comments are invisible to the build, so nothing is broken.
