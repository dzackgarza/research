# chain-complexes — corpus INDEX

Four documents, landed 2026-08-20 from `gitclones/Coxeter/research/` under
`PLAN-coxeter-deletion-audit-registry` (reader H). One design: a category
$\mathrm{Ch}(\mathcal{C})$ of chain complexes as a Sage category, plus the
attempt to attach a bilinear form in each degree.

The preamble has no complexes node, so nothing here is superseded. It is the
prerequisite for any $\mathrm{Ext}$ or $\mathrm{Tor}$ in this repository, and
that is why the homotopy corpus (`notes/homotopy-bilinear-modules/`) stalls
where it does.

## The documents

- `chain_complexes.md` — the category itself. Objects are $(C_\bullet,
  d_\bullet)$ with $d_{n-1}d_n = 0$; morphisms are the chain maps. The design
  point is that **exactness is a property asked of the complex, not of a
  caller-supplied triple**: `is_exact`, `is_exact_at(n)`, `homology(n)`,
  `cone`, `shift` are category methods, and a short exact sequence is the
  complex that happens to be exact, not a separate type.
- `chain_complex_notation.md` — the notation question: how a complex is
  written at a Sage prompt, and how the differentials are supplied (a list of
  morphisms, from which the objects are read off, rather than objects and
  matrices entered twice).
- `chain_complex_usage.md` — worked session transcripts of the intended
  interface: `ChC = Ch(Modules(R))`, complexes built from `Hom(A,B)`
  elements, homology and exactness asked of the result.
- `bilinear_chain_complex_extension.md` — the extension to formed modules: a
  complex with a form $b_i$ in each degree and form-preserving
  differentials, tensor product by the Kronecker product of the forms,
  resolutions and derived functors computed in that setting. Written against
  Sage's `sage.homology.chain_complex.ChainComplex` as the base.

## Disposition against the preamble

Absent, all four. The eventual home of the first three is a
`categories/complexes/` node; the fourth belongs under
`categories/modules/framed/formed/` once that node exists.

**The obstruction the fourth document does not state.** A chain complex needs
$d^2 = 0$, hence an additive homset. With form-preserving morphisms,
$\mathrm{Hom}((M,b),(N,c))$ has no addition — a sum of isometries is not an
isometry, and the zero map preserves $b$ only when $b = 0$. So
$\mathrm{Ch}(\mathrm{Bil}_R\text{-}\mathrm{Mod})$ as written is undefined.
The same obstruction is what the homotopy corpus meets; its INDEX states it in
full, along with the two mathematically live repairs (forms as structure over
$\mathrm{Mod}_R$, so the underlying complex is a complex of $R$-modules; or
Ranicki-style chain duality, where the form is a chain map $C^{-*} \to C$).
`bilinear_chain_complex_extension.md` is readable as a proposal for the first
of those, since its differentials are matrices over $R$ and the forms sit
alongside them.

Sage's own `ChainComplex` over $\mathbb{Z}$ is unaffected by any of this and
is the working implementation the first three documents assume.

## Errors recorded

None recorded against these four files by the audit.
