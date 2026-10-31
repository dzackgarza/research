# Deposited sources

Each entry here is a copy of a paper the book cites, kept so that its statements can be
checked against the source rather than against a recollection of it. The directory name is
the **bibliography key** of the work it holds, not the author-year label the files were
downloaded under; where the two differed, the directory was renamed and the file names were
left alone.

| directory | bibliography key | title as printed in the deposited file |
| --- | --- | --- |
| `ABE22/` | `ABE22` | Compactification of moduli of elliptic K3 surfaces |
| `AE22/` | `AE22` | Compactifications of moduli spaces of K3 surfaces with a nonsymplectic involution |
| `AE23a/` | `AE23a` | The flex divisor of a K3 surface |
| `AEGS23.pdf` | `AEGS25` | Compact moduli of Enriques surfaces with a numerical polarization of degree 2 |
| `AET19/` | no key yet | Compact Moduli of elliptic K3 surfaces |
| `YZZ25/` | `YZZ25` | Moduli spaces of sextic curves with simple singularities and their compactifications |
| `Zan20/` | `Zan20` | Explicit constructions of Halphen pencils |

Two of these names were wrong in the way that matters most — the directory named a
different paper from the one it contained. `papers/AE23/` held the flex divisor paper, which
the bibliography carries as `AE23a`, while `AE23` is *Compact moduli of K3 surfaces*; and
`papers/AKSZ23/` held the nonsymplectic-involution paper, which is `AE22`. A reader checking
a citation against the directory would have been checking the wrong paper, and someone
reading `[@AE23, Thm. 5.14]` in the text and opening `papers/AE23/` would not have found
Theorem 5.14 in it.

Left as they are, with the reason:

- `AET19/` holds *Compact Moduli of elliptic K3 surfaces*, and no bibliography entry carries
  that title; the book cites `@AET19` nowhere, so nothing depends on it here. If the work is
  cited later, the entry should be added from the paper rather than from memory.
- `AEGS23.pdf` is named for its posting year, while the book cites it as `AEGS25`; a PDF
  cannot be renamed as cheaply as a directory and the key is unambiguous in the text, so the
  mismatch is recorded here instead.
