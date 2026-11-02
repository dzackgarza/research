# The A21 tuple: hypotheses as authored, and as they stand

The obligation of A21 is defined by the bullet list in
`writing/coble/heegner-report/coble-heegner-research-report.md`, section "Labeled lattice
data" (`#sec-labeled-lattice-data`). That list has been rewritten more than once in recent
rounds. This note records the authored text, the text as it stands, and what was changed in
between — so that a later round cannot mistake a rewritten condition for an authored one.

## Baseline

* Commit `a145cea4a5` ("the `T_Co` surjectivity failure recorded with its full traceback …"),
  file `writing/coble/heegner-report/coble-heegner-research-report.md`, lines 601–631.
* The same text is in `938216edbc` and in every earlier commit that carries the section; the
  two were checked and agree, so the baseline is not an artefact of one commit.

Authored bullets, verbatim from `a145cea4a5`:

1. `$I_{\Co}$ and $I_{\mathrm{dP}}$ are commuting nonsymplectic involutions;`
2. `$H^2=4$ is fixed by both involutions;`
3. `$\alpha^2=-2$, $H\cdot\alpha=0$, and $\alpha$ is fixed by $I_{\Co}$;`
4. `$\mcc$ is the chosen positive/nef chamber in which $\alpha$ is effective and $H$ is nef and big;`
5. `the product $I_{\Co}I_{\mathrm{dP}}$ has the required symplectic character.`

Authored problem statement: "Any two tuples $\mathfrak L_{\Co,2}$ arising from the direct
projective construction are conjugate by an element of $O(L_{K3})$ preserving the labels, the
degree-$4$ class, the effective root, and the chosen chamber."

## Before and after

| # | As authored (`a145cea4a5`) | As it stood after the recent rounds | Now |
|---|---|---|---|
| 1 | commuting *nonsymplectic involutions* of the surface | rewritten to "commuting nonsymplectic involutions **of the lattice** $L_{K3}$", with "not required to be the action of an automorphism of the Coble cover" appended | authored text restored verbatim; the lattice reading is stated in a separate paragraph, labelled as a weaker abstract reading |
| 2 | `$H^2=4$` fixed by both | unchanged | unchanged |
| 3 | `$\alpha^2=-2$`, `$H\cdot\alpha=0$`, `$\alpha$` fixed by `$I_{\Co}$` | unchanged | unchanged |
| 4 | the chamber $\mcc$ in which `$\alpha$` is effective and `$H$` is nef and big | rewritten into a statement about `$h_\Co$` being nef and about "the missing premise no source supplies" | authored text restored verbatim; the analysis moved to a separate paragraph |
| 5 | the product "has the required symplectic character" | rewritten into "is an involution, and is symplectic whenever both factors are realized …; listed as a condition it is redundant" | authored text restored verbatim; the observation moved to a separate paragraph |

Reason for each restoration: the authored conditions are geometric (involutions of the K3
cover), and the rewritten forms had quietly replaced them by conditions on the lattice, which
is a strictly weaker requirement. The lattice statements are not withdrawn — they are kept,
labelled, in `@prop:del-pezzo-placement`, `@prop:coble-cover-marking` and
`@cor:no-del-pezzo-involution-coble-cover` — but they are not the authored obligation and do
not close it.

The second bullet of the *strategy* list ("Define a direct moduli problem of K3 covers with a
Coble involution, a commuting del Pezzo involution, a degree-4 class …") was rewritten in the
same way and is restored for the same reason; the analysis it had acquired now stands as a
paragraph after the list, headed so that it cannot be read as the requirement.

## The claim that no authored condition relates `$I_{\mathrm{dP}}$` to `$\alpha$`

Checked against the baseline text rather than asserted:

* `$I_{\mathrm{dP}}$` occurs in bullets 1, 2 and 5.
* `$\alpha$` occurs in bullets 3 and 4.
* No bullet contains both. Bullet 3 ties `$\alpha$` to `$I_{\Co}$` only ("fixed by
  `$I_{\Co}$`"), and bullet 4 ties `$\alpha$` to the chamber only ("effective in `$\mcc$`").

So any relation between `$I_{\mathrm{dP}}$` and `$\alpha$` is an addition, not a reading of the
authored list. This is what `@prop:del-pezzo-placement` relies on when it says the abstract
conditions do not constrain the placement of `$\sdp$` relative to `$\alpha$`.

## What is proved about the abstract reading, and what is only not excluded

* `@prop:del-pezzo-placement`: the integral statement is a finite-index one. Commutation gives
  `$S_\Co\otimes\QQ = A_\QQ\oplus B_\QQ$` with `$A = S_\Co\cap\sdp$`, `$B = S_\Co\cap\sdp^{\perp\lkt}$`,
  and `$2S_\Co\subseteq A\oplus B\subseteq S_\Co$`; the halves `$(x\pm\psi x)/2$` need not be
  integral, so the integral sum can be proper — as it is for `$S_\Co\oplus T_\Co$` inside
  `$L_{K3}$`, of index `$2^{11}$`. For the published candidate the index is `$1$`, by
  `$\det\sdp\cdot\det B = [S_\Co:\sdp\oplus B]^2\det S_\Co$` with values `$-4\cdot(-512) = 2048$`.
* The case `$A = \ZZ H$` (the del Pezzo slot meeting `$\Pic$` only in `$\langle H\rangle$`) is
  **not excluded** by the stated constraints. No witness for it is exhibited anywhere in the
  repository, so "not excluded" is all that may be said.
* Nor is uniqueness claimed in the rank-two case: the placement problem there is finite
  (`a\mapsto a-H/2` lands in the negative definite `$H^{\perp}\cap S_\Co^\#$`), and a search over
  `$|a_0|\le 24$` returns only the published pair, but the norm-`$(-1)$` enumeration that would
  settle it has not been run.
