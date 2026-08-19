# Conventions — design corpus

The sign, notation and construction conventions the two Coxeter corpora were
written under. Landed 2026-08-20 from `~/gitclones/Coxeter`.

The one convention that governs everything else is the **negative-definite
Gram convention**

$$B_{ij} = 2\cos(\pi/m_{ij}),$$

so that $B_{ii} = 2\cos\pi = -2$ and, for $A_2$, $B = [[-2,1],[1,-2]]$. This
is $-2$ times the standard geometric Gram matrix of unit normals (diagonal
$1$, off-diagonal $-\cos(\pi/m_{ij})$), hence the negative of the Schläfli
matrix $C_{ij} = -2\cos(\pi/m_{ij})$. Every definiteness criterion inverts
accordingly: finite type is negative definite, affine type negative
semidefinite of corank $1$, hyperbolic type stays indefinite.

**This convention is in force in the repository.** Its in-tree owner is
`tests/coxeter_tdd_specs/literature/PROJECT_CONVENTIONS.md`, which states the
same formula. In the preamble, `DefiniteLattices.roots`
(`definite_lattices.sage:139`) returns the vectors of square $-2$ in the
negative definite regime, `minimal_edge_lattices`
(`coxeter_diagrams.sage:94`) admits roots of square $-2$ and $-4$ and derives
the crystallographic edge labels from them, and the Gram matrix of a named
type is $-\text{scale}$ times the symmetrized Cartan matrix
(`coxeter_diagrams.sage`, `from_cartan_type`). The documents below are the
fuller statement of the convention and the reasoning that fixed it.

---

## 1. Documents

| Document | Origin | Content |
|---|---|---|
| `docs-CONVENTIONS.md` | `Coxeter/tmp_restore/docs/CONVENTIONS.md` | The fullest statement. Ten sections: graph-first construction (never write a Gram matrix by hand — build it from a Sage root system), LaTeX type notation, the Gram formula with its $A_2$ verification and the inverted classification table, the data-source hierarchy, the lattice-versus-vector-space distinction, exact arithmetic and the field extension needed per type, no index loops for linear algebra, caching and enumeration, signature-based classification, and test-verification rules. |
| `implementation-CONVENTIONS.md` | `Coxeter/implementation/conventions/CONVENTIONS.md` | The agent-facing subset, leading with two distinctions: a bilinear form is not an inner product (an inner product is additionally symmetric and positive definite, so indefinite, skew and degenerate forms are excluded), and a Gram matrix is not a Cartan matrix ($G_{ij} = \langle e_i, e_j\rangle$ is symmetric; $A_{ij} = 2\langle\alpha_i,\alpha_j\rangle/\langle\alpha_j,\alpha_j\rangle$ need not be). |
| `tmp-restore-CONVENTIONS.md` | `Coxeter/tmp_restore/CONVENTIONS.md` | The same document as the previous row. The two differ only in the four Quick Reference paths at the end, which point at each tree's own layout. |
| `extracted-conventions.md` | `Coxeter/tmp_restore/extracted-conventions.md` | The distinctions consolidated with a source attribution per item, plus three sections the others lack: **common errors** (using "inner product" for a general form; taking an eigenvalue count as the *primary* definition of a type rather than a consequence; confusing a mathematical definition with the algorithm that computes it; orthogonal-complement confusion under a degenerate form), **forbidden approaches**, and the definitions of the components of a Coxeter system and of a maximal parabolic subdiagram. |
| `planning-corpus-conventions.md` | `Coxeter/implementation/planning/CLAUDE.md` | How the planning corpus itself was to be written: no implementation, only category, class, factory and method stubs; Sage docstrings used as fail-first TDD recording known mathematical properties; planning documents append-only; a five-phase method for refactoring a category. |

---

## 2. Divergences and open points

### 2.1 The convention is used but its relation to the Schläfli matrix is unstated

The preamble independently uses the algebraic-geometry negative-definite
convention. What it does not say anywhere is that this matrix is the
*negation of the Schläfli matrix* $C_{ij} = -2\cos(\pi/m_{ij})$. The audit
found that this unstated relation is precisely where the sign errors in the
literature corpus entered — a captured article's $C$ was transcribed as if it
were the project's $B$. A sentence in the `coxeter_diagrams.sage` module
docstring tying the $-2/-4$ root normalisation to $C_{ij}$ would close it.

### 2.2 Specimens from canonical constructions

Both `docs-CONVENTIONS.md` §1.1–1.2 and `extracted-conventions.md` state a
rule the repository follows in practice but does not state in-tree: a test
specimen comes from Sage's own root-system construction — simple roots and
their pairings, or a Cartan matrix — never from a matrix entered by hand.
Reader D recorded this as unowned.

### 2.3 Definition before algorithm

`extracted-conventions.md` §3.2–3.3 is the clearest statement in either
corpus of a rule the preamble now enforces structurally: a type is *defined*
by definiteness of the form, and an eigenvalue computation or a determinant
sign is at most an algorithm that decides it under hypotheses. The preamble's
`refine_one_lattice` (`integral_lattices.sage:2061`) routes by the radical of
the correlation morphism and records in comment that it is deliberately not a
determinant proxy. The convention document is where that position was first
written down.

---

## 3. Errors recorded in these documents

The audit recorded no mathematical error in this corpus. The sign errors it
did record sit in the *literature* extracts, which apply this convention to
matrices transcribed from sources that use the opposite one; those are
recorded with the literature corpus, not here.
