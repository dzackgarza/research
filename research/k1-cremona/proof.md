# Status

PROVED. There is a nonempty open locus \(V^\circ\subset V\) on which the
quadratic Cremona transformation of three nodes gives an actual second
plane presentation: the three joins become disjoint smooth \((-1)\)-curves
and the transformed sextic is irreducible with exactly ten ordinary nodes.
The full proof is `lem:cremona-second-plane-model-general` in
`writing/coble/lattices-and-moduli/moduli-construction.md`.

The general-open assertion uses a special fibre at \(101\), not the
withdrawn Harris–Morrison moving-line argument. A squarefree zero-dimensional
Jacobian algebra of rank ten gives ten geometric \(A_1\) nodes, while
rational parametrization excludes any further singularity. Exact
restrictions of the three joins have double factors at both endpoints and
nonzero residual discriminants; every other node misses those joins.
Because bad incidence and tangency are closed, existence at that special
fibre proves nonemptiness in characteristic zero. No density statement for
\(V\) is used.

Checks:

- self: PASS, scope, three singularity cases and frame identities.
- compute: PASS, exact special fibre in the Sage image, fresh rerun.
- external geometric review of the earlier draft: no gap in the
  blowup/contraction/nodality chain.
- independent review of this final special-fibre/base-change version: NOT
  OBTAINED. The second two-member review exhausted without a report or
  finding. This is not recorded as a check or as a MET review.

Scope: this proves item (1) only. Assembly from #804 and the widened stack
are not worked in this turn. The full item-by-item verdict is
`computations/reports/799-acceptance-item-by-item.txt`: the original
finite-group alternative is refuted, the widened stack and the required
independent Kimi MET review remain open.
