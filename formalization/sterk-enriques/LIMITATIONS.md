# Limitations

What this development does **not** establish.  Maintained from the first stated
node, not written at the end, because a restriction is decided when a statement
is written.

Nothing here is yet proved, so at present the only entries are structural.

## Structural

- **Nothing is proved.** No node of the dependency graph has a proof.  The
  mathematical content in hand is a reconstruction of four of Sterk's five
  Coxeter diagrams from their root data, checked against the printed figures,
  in `../../computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage`.
  That is a Sage computation, not a formal proof, and it certifies nothing about
  Lean.

- **The fifth diagram disagrees with the source.** For $v = 2e+2f+\bar\alpha_1$
  (3.3.12) the reconstruction yields thirteen maximal parabolic subdiagrams in
  six shapes, against the four types Sterk lists.  The transcription of that
  figure is the suspect, and the node is red.

- **Vinberg, Nikulin and Scattone are cited only as Sterk cites them.**  None has
  been read in the original.  Any node resting on them needs its own reading
  before its statement is written.

## Named results will be restricted

When they are stated, the deep inputs will be stated in the strength this
argument needs, and will not be citable as the general classical theorems.  See
the Strength column of `PROOF-PATH.md`.  This follows the practice of
`anthropics/fermats-last-theorem`, whose `docs/limitations.md` says of its own
Ribet, Wiles, Mazur and Langlands–Tunnell that none "should be cited as a
formalisation of the general classical theorem".

## Provenance of the source text

The Zotero item `Ste95a` (Math. Z. 220 (1995), 427–444) carries the 1988 thesis
as its PDF, not the paper.  Section numbers quoted throughout as `3.3.x` are the
thesis numbering; the corresponding published numbers in Math. Z. 207 (1991) are
`4.3.x`.  The Math. Z. 220 text has not been consulted.
