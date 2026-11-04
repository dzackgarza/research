# Deposited sources

Each entry here is a copy of a paper the book cites, or of one deposited while a citation was
being checked, kept so that statements can be verified against the source rather than against
a recollection of it. The directory name is
the **bibliography key** of the work it holds, not the author-year label the files were
downloaded under; where the two differed, the directory was renamed and the file names were
left alone.

| directory | bibliography key | title as printed in the deposited file |
| --- | --- | --- |
| `ABE22/` | `ABE22` | Compactification of moduli of elliptic K3 surfaces |
| `AE22/` | `AE22` | Compactifications of moduli spaces of K3 surfaces with a nonsymplectic involution |
| `AE23a/` | `AE23a` | The flex divisor of a K3 surface |
| `AEGS23.pdf` | `AEGS25` | Compact moduli of Enriques surfaces with a numerical polarization of degree 2 |
| `AET23/` | `AET23` | Stable pair compactification of moduli of K3 surfaces of degree 2 |
| `AB19/` | `AB19` | Compact Moduli of elliptic K3 surfaces |
| `YZZ25/` | `YZZ25` | Moduli spaces of sextic curves with simple singularities and their compactifications |
| `Kim20/` | `Kim20` | $SU(N)\times\mathbb{Z}_2$ in F-theory on K3 surfaces without section as double covers of Halphen surfaces |

Two of these names were wrong in the way that matters most — the directory named a
different paper from the one it contained. `papers/AE23/` held the flex divisor paper, which
the bibliography carries as `AE23a`, while `AE23` is *Compact moduli of K3 surfaces*; and
`papers/AKSZ23/` held the nonsymplectic-involution paper, which is `AE22`. A reader checking
a citation against the directory would have been checking the wrong paper, and someone
reading `[@AE23, Thm. 5.14]` in the text and opening `papers/AE23/` would not have found
Theorem 5.14 in it.

Left as they are, with the reason:

Two deposits were named for a paper they do not contain, and one for its posting year rather
than its key:

- `papers/AET19/` held *Compact Moduli of elliptic K3 surfaces* by Kenneth Ascher and Dori
  Bejleri, which the bibliography carries as `AB19`. The name `AET19` belongs to a different
  paper: those initials and that arXiv year are Alexeev--Engel--Thompson, *Stable pair
  compactification of moduli of K3 surfaces of degree 2*, whose arXiv number is 1903.09742 and
  whose bibliography key is `AET23`, for its year of publication. The two titles are nearly the
  same and the papers are otherwise unrelated. The directory is now `papers/AB19/` and the
  deposited file keeps its original name, `elliptic_k3.tex`, which is what identifies the
  download; the Alexeev--Engel--Thompson paper has its own deposit at `papers/AET23/`, and the
  book cites it as `@AET23`. No bibliography entry is named `AET19`, and neither the book nor
  the dissertation cites one, though a few working notes abbreviate this paper to `AET19` in
  prose; where that shorthand occurs it is text and not a key.
- `AEGS23.pdf` is named for its posting year, while the book cites it as `AEGS25`; a PDF
  cannot be renamed as cheaply as a directory and the key is unambiguous in the text, so the
  mismatch is recorded here instead. Its first page carries `arXiv:2312.03638`, which is the
  record the key resolves to.

- `papers/Zan20/` held `file1806.tex`, which is *not* the bibliography's `Zan20` (Zanardini,
  *Explicit constructions of Halphen pencils*): the file is Kimura's paper of the same
  subject, which the bibliography carries as `Kim20`, and its author line gives a KEK Theory
  Center address. The directory is now `papers/Kim20/` with the file name unchanged, and the
  bibliography's `Zan20` has no deposit here at all — so a citation of `@Zan20` cannot be
  checked against this directory and should be checked against the paper itself.

One deposit is a preprint of a paper the bibliography keys by its year of publication.
`papers/AET23/` holds `1903.09742v3.pdf`, the arXiv version (v3, 14 February 2023) of the paper
the bibliography carries as `AET23` — Crelle **799** (2023), 1--56, DOI
`10.1515/crelle-2023-0011`; the published version has the same title and authors and was not
downloaded, so the locators the text gives for it are the preprint's. The passage quoted in the
dissertation's Scattone boundary analysis, with the four root-sublattice labels for the $d=1$
one-cusps, is printed p.~16 there, in \S3B, "Baily-Borel compactification".

Every deposit above is now named for the bibliography key of the paper it actually contains.
The check in each case was the title printed in the file, and for the PDFs the arXiv line on
the first page, against the title in `writing/.assets/references.bib`.
