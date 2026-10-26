# Coursework and tutorial scratch notebooks

These notebooks are archived because they are not research computations. Commit
`1847d9c116` imported them from loose Sage notebooks in the home directory,
Dropbox and notes, and commit `4175dc47eb` merged them by subject. Their content
is exercise and tutorial material: matrix numerics, single-variable calculus,
plotting, curvature of space curves, partitions and point counts on small
examples.

The live notebooks under `computations/notebooks/` measure the preamble session
against research use. A cell from this material that fails in the session is
not evidence that research needs the operation. So these notebooks stay out of
that set, and their failures do not create issues.

They were ported to session spellings before archiving. The commit bodies list
the remaining failing cells (`git log -- <notebook>`). Failures that are real
defects of research operations are tracked in issues #610, #611, #613, #614,
#616, #617, #618, #619 and #446.

| Notebook | Content |
|---|---|
| `linear-algebra.ipynb` | eigenvectors, echelon forms, QR, LU, SVD, random matrices over F_2 |
| `calculus-and-plotting.ipynb` | limits, integrals, partial fractions, plots, elementary number theory |
| `complex-analysis.ipynb` | symbolic residues and roots of polynomials |
| `geometry-and-topology.ipynb` | first fundamental forms, Frenet frames, Poincaré disk tilings |
| `symmetric-functions.ipynb` | partitions, tableaux, Fock-space vectors |
| `number-theory.ipynb` | point counts on a diagonal cubic over GF(5), characters |
| `finitely-presented-groups.ipynb` | jupyter-ai chat scratch about small groups |
