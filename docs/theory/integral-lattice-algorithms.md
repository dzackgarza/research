# Computational integral lattices

These notes explain recent results relevant to exact lattice computation. The
source versions are fixed below. “Theorem” refers to a result proved in the
cited preprint; implementation consequences are deductions from its stated
hypotheses.

| Topic | Source version | Mathematical contribution | Exposition |
| --- | --- | --- | --- |
| Trace lattices | Zhang, 21 October 2026, v1 | Integral isometry classification for cyclic number fields, including wild ramification | [Trace lattices](integral-trace-lattices.md) |
| Kneser neighbors | Müller–Scheithauer, 19 October 2026, v1 | An exact eigenvalue identity from singular-weight orthogonal modular forms | [Neighbor operators](kneser-neighbors-and-orthogonal-modular-forms.md) |
| Indefinite binary forms | Diao, 20 October 2026, v1 | An upper bound for the sum of proper class numbers | [Class numbers](indefinite-binary-class-numbers.md) |
| Finite automorphism groups | Drecun, 20 October 2026, v1 | A polynomial infeasibility criterion for completeness of graph automorphism generators | [Finite automorphism groups](finite-automorphism-groups-and-polynomial-certificates.md) |

## Distinct computational questions

For integral lattices with Gram matrices $A,B$ of equal rank $r$, an integral
isometry is a matrix $P\in\operatorname{GL}_r(\mathbb Z)$ satisfying
$P^{\mathsf T}BP=A$. An isometry criterion decides whether such a matrix exists.
Constructing one is a separate computational task. A classification by complete
invariants can solve the first task without supplying the second.

An orbit problem requires a specified group and its action. Primitive isotropic
sublattices, isotropic vectors, and isotropic planes give different sets on which
an orthogonal group acts. A result about the boundary values of modular forms
does not by itself enumerate these orbits. Enumeration also needs a termination
argument, representatives, and a criterion for equivalence under the specified
group.

A class number counts equivalence classes. An analytic bound on a sum of class
numbers constrains their collective growth. It does not produce the individual
classes. Likewise, an identity satisfied by a neighbor operator constrains that
operator but need not determine every entry of its matrix.

The cited results address these particular questions. Their hypotheses do not
supply a general indefinite-lattice isometry algorithm, a general primitive
isotropic-orbit enumeration, or a new exact mass formula.

## Mathematical use in this programme

The [architecture](../../INTENT.md) assigns mathematical definitions and theorems
to `lean-categories`. The `lean-cas-dsl` acceptance suite states permanent
mathematical assertions with independently established expected values.
Implementations supply answers to those assertions.

The results here can supply mathematical requirements and cited examples for
that sequence. A preprint statement, a conditional theorem, an implementation
proposal, and an executed computation have different status. In particular,
software that constructs a certificate does not acquire authority over the
programme's acceptance judgment. The graph-certificate note explains the
mathematical reduction separately from that architectural boundary.
