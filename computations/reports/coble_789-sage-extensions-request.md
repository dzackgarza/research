# sage-extensions request: a certified-complete plane-stabilizer generator family

Filed as a report rather than an issue: the connected GitHub connection is
read-only for issues on this repository, so the body below is the text to post.

## What is missing

`IntegralLattice.Aut().setwise_stabilizer(embedding)` returns a generator family
for the setwise stabilizer of a primitive totally isotropic plane in an
indefinite lattice (`lattice_morphisms.py`, `setwise_stabilizer`). The
returned family is not certified to generate the stabilizer, and on the objects
of research#789 it does not.

## The witness

Run `computations/reports/coble_789-plane-stabilizer-orbits.py`, transcript
`-run.txt`, on `NamedLattices.TEn` = U + U(2) + E8(2), for Sterk's five 1-cusp
planes, restricted to Gamma_En,2 = rho^{-1}(M) (AEGS Def. 2.6, Sterk Prop. 2.7):

    type (2,4,5): 104 of 134 generators in Stab_{Gamma_En,2}(Pi); orbits on the 8 pairs: 1
    type (4,5):    52 of 134;                                                       4
    type (3,5):    66 of 134;                                                       2
    type (3,4):    63 of 133;                                                       2
    type (5,5):    79 of 133;                                                       3

The number of orbits of a subgroup is an upper bound for the number for the
whole stabilizer.  The independently computed values, by the discriminant route
(`thm:coble-integral-lifting-fibre(4)(b)` with `prop:coble-flag-orbits-and-edges`),
are 1, 1, 2, 1, 2.  The two agree at {2,4,5} and {3,5} and disagree at
{4,5}, {3,4}, {5,5}, so the returned family generates a PROPER subgroup there.

## What a fix must supply

Either a generator family for the plane stabilizer that is certified complete,
or a completeness certificate for the family returned (a reduction-complex or
Vinberg argument covering the plane case), in the sense that the same call is
documented as untrusted for the vector case at
`lattice_morphisms.py` (`vector_stabilizer_generators`).  Without it, no orbit
count on K_Pi can be reported as the fibre of the 1-cusp map, which is what
research#789 asks for.

## Consequence for research#789

The multiplicities (1,1,2,1,2) remain those of the discriminant route; the B2
cusp-stabilizer route is blocked on this family, not on the mathematics of the
reducing theorem (`thm:b2-one-cusps` with `lem:one-cusp-fibre-finite`), which is
proved.
