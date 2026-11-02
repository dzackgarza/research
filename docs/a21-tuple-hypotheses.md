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

## The completeness contract of the enumeration, at the pin

The rank-two result rests on one provider guarantee, so it is recorded here verbatim rather
than paraphrased. At provider pin `c546077dce79a76eb32e92d080aa9c44e4c67552`, file
`sage_extensions/categories/lattices.py`, `elements_of_norm` begins at line 6902, and its
docstring says:

> "Return the full norm fibre, retaining finite integral enumeration.
> For definite integral lattices the existing finite square-shell computation supplies every
> point, so exhausting this fibre terminates, including at norm zero. Nonzero fibres of split
> nondegenerate binary integral forms also retain their complete finite divisor enumeration. …
> Other fibres use the general equalizer locus; no enumeration is inferred over an uncountable
> coefficient ring."

and the branch that implements it, at lines 6932–6939, is

```python
value = self.value_module()(value)
if (
    self.base_ring() is _owned_integers()
    and self.module_rank().is_finite()
    and (self.module_rank() == 0 or self.is_definite())
):
    return self.vectors_of_square(value).domain()
```

So: over `ZZ`, at finite rank, on a lattice for which `is_definite()` is `True`, the returned
object is the *complete* square-shell fibre, enumerated. On anything else — in particular on
the indefinite `S_Co^#` — the return is the general equalizer locus, which is not a list of
points and is not exhaustive. That is why the earlier probe could not have been a certificate,
and why the witness checks `is_definite() is True` on `H^\perp\cap S_Co` before enumerating.

The witness `computations/reports/coble_del_pezzo_placement.py` prints, in order: the rank and
determinant of the complement (10 and 2048), `definite: True`, the cardinality of the norm
`(-4)` fibre (242), and the two solutions.

## Why the enumeration covers every contained primitive U(2)

The enumeration lists the isotropic `a` of `S_Co` with `a.H = 2`. It covers the primitive
`U(2)`-sublattices of `S_Co` containing `H` by the following chain, which is stated in the
manuscript at `@prop:del-pezzo-placement` and in the remark that follows it:

1. if `N` is a `U(2)` inside `S_Co` containing `H`, then `H` splits in `N` as `a + b` over a
   hyperbolic basis, so `a, b` lie in `S_Co` and `a.H = 2`;
2. the enumerated set is `{f^*F_1, f^*F_2}`, so `N` contains one of them;
3. `H - f^*F_1 = f^*F_2`, so containing one gives both, hence `N` contains
   `<f^*F_1, f^*F_2>`;
4. `<f^*F_1, f^*F_2>` is **primitive** in `S_Co` — the decomposition
   `S_Co = <f^*F_1, f^*F_2> perp N` has index 1, since `det` is `-4` and `-512` against
   `det S_Co = 2^11` (`@prop:coble-cover-marking`) — so `S_Co/<f^*F_1, f^*F_2>` is
   torsion-free; `N/<f^*F_1, f^*F_2>` is a subgroup of it, and being finite of equal rank it is
   trivial, whence `N = <f^*F_1, f^*F_2>`.

Step 4 is the only step that needs more than rank: equal rank plus containment does **not**
give equality in general (`2Z` is contained in `Z` at equal rank). What gives it here is
primitivity, and the index-1 determinant computation is the witness for that. Step 3 is where
the specific shape of the solution set enters — had the two solutions not been a pair summing
to `H`, the conclusion would not follow. An earlier version of this note stopped at "both
lattices have rank two", which was not enough.

## The gluing: what is in hand, and where the explicit arrow is blocked

The pair `S_Co + T_Co -> L_K3` with index `2^{11}` is the graph of an anti-isometry
`gamma_Co : A_{S_Co} -> A_{T_Co}`, and an anti-isometry is an isometry
`A_{S_Co} -> A_{T_Co}(-1)`. Two facts were established at the pin
(`computations/reports/coble_gluing_discriminants.py`, `-run.txt`, 19 s, exit 0):

1. **The forms are anti-isometric.**
   `A_{S_Co}.is_anti_isometric(A_{T_Co})` returns `True`; equivalently
   `A_{S_Co}.is_isometric_to(A_{T_Co}.twist(-1))` returns `True`. Both discriminant groups have
   order `2048`. By Nikulin's gluing correspondence (`@thm:nikulin-gluing`) the pair therefore
   admits a unimodular overlattice with the full graph gluing, so the index `2^{11}` stated for
   `L_K3` is consistent with the pair, and the gluing datum exists up to isometry.

2. **The explicit arrow is blocked, at a located call.** `normal_form_isometry()` returns the
   normal-form-to-original morphism, so it does give `NF(A_{S_Co}) -> A_{S_Co}` and
   `NF(A_{T_Co}(-1)) -> A_{T_Co}(-1)`. Composing them to get `A_{S_Co} -> A_{T_Co}(-1)` fails:

   * `f.domain() is g.domain()` returns `False`: the two normal forms are constructed per form
     and are distinct objects, so no arrow `NF(A_{S_Co}) -> NF(A_{T_Co}(-1))` is available to
     compose with;
   * consequently the correctly-directed `f.inverse().then(g)` is refused — `then` is
     `other ∘ self` and requires `other.domain() is self.codomain()` — with
     `ValueError: cannot compose Morphism from Finitely presented module ...`;
   * the multiplicative and at-sign products raise
     `TypeError: unsupported operand type(s) for *: 'CategoricalIsomorphism' and
     'CategoricalIsomorphism'`;
   * `f.then(g)`, the reverse direction, is refused for the same documented reason and its
     refusal says nothing about the provider.

   These are failures **under the documented contract**, executed in the script and reported
   with the tracebacks Python produced. The candidate constructors were also searched and
   called: `then` is guarded by object identity (`mor_categories.py:637`), `normal_form` is
   recomputed per call (`form_modules.py:2736`, `torsion_form_modules.py:1014`),
   `reframing_isometry` re-presents one form on new generators (`form_modules.py:2630`),
   `equip_quadratic_form` sits on a pure module (`pure/modules.py:1980`), `isometry_to` exists
   at the lattice level only (`lattices.py:4373`), and the call
   `A_{S_Co}.isometry_to(A_{T_Co}(-1))` is refused with its own traceback, recorded in the run
   log. The request to the owner is therefore precise: an isometry constructor between two
   isometric torsion quadratic forms (or a normal form published once per isometry class), with
   the runnable specimen committed beside this note. An earlier version of this note asserted
   that "no isometry constructor ... is available at this pin" without any such call; that
   assertion is withdrawn and replaced by the executed record. That is A20 item 1(b).

`glue_map` is the operation that returns the anti-isometry in the form the book wants, but its
docstring requires the two primitive orthogonal subobjects *inside* the ambient lattice, which
is the object being built; it is not a substitute for the constructor above.

Not claimed, and corrected from an earlier round: having the gluing does not by itself make the
embedding or automorphism questions finite. Making them finite needs a reduction theorem — a
definite fibre or a finite quotient of the non-definite one — and chamber criteria, none of
which is supplied here.
