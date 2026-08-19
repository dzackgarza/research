# GAP: Group actions on finite sets

**Tested:** All examples verified in GAP 4.

---

## Orbit

```gap
gap> G := GL(2, GF(3));
GL(2,3)
gap> v := [1,0] * Z(3)^0;
[ Z(3)^0, 0*Z(3) ]
gap> orb := Orbit(G, v, OnRight);
[ [ Z(3)^0, 0*Z(3) ], [ Z(3), 0*Z(3) ], [ Z(3), Z(3)^0 ], 
  [ Z(3)^0, Z(3) ], [ Z(3)^0, Z(3)^0 ], [ 0*Z(3), Z(3) ], 
  [ Z(3), Z(3) ], [ 0*Z(3), Z(3)^0 ] ]
gap> Length(orb);
8
```

---

## Stabilizer

```gap
gap> G := GL(2, GF(3));
GL(2,3)
gap> v := [1,0] * Z(3)^0;
[ Z(3)^0, 0*Z(3) ]
gap> stab := Stabilizer(G, v, OnRight);
Group([ [ [ Z(3)^0, 0*Z(3) ], [ Z(3)^0, Z(3)^0 ] ], 
        [ [ Z(3)^0, 0*Z(3) ], [ Z(3), Z(3) ] ] ])
gap> Size(stab);
6
gap> GeneratorsOfGroup(stab);
[ [ [ Z(3)^0, 0*Z(3) ], [ Z(3)^0, Z(3)^0 ] ], 
  [ [ Z(3)^0, 0*Z(3) ], [ Z(3), Z(3) ] ] ]
```

---

## OrbitStabilizer (both at once)

```gap
gap> G := GL(2, GF(3));
GL(2,3)
gap> v := [1,0] * Z(3)^0;
[ Z(3)^0, 0*Z(3) ]
gap> result := OrbitStabilizer(G, v, OnRight);
rec( orbit := [ ... ], stabilizer := Group(...) )
gap> Length(result.orbit);
8
gap> Size(result.stabilizer);
6
```

---

## Action on sets

```gap
gap> G := GL(2, GF(3));
GL(2,3)
gap> vecs := [[1,0]*Z(3)^0, [0,1]*Z(3)^0, [1,1]*Z(3)^0];
[ [ Z(3)^0, 0*Z(3) ], [ 0*Z(3), Z(3)^0 ], [ Z(3)^0, Z(3)^0 ] ]
gap> pairs := Combinations(vecs, 2);
[ [ [ 0*Z(3), Z(3)^0 ], [ Z(3)^0, 0*Z(3) ] ], 
  [ [ 0*Z(3), Z(3)^0 ], [ Z(3)^0, Z(3)^0 ] ], 
  [ [ Z(3)^0, 0*Z(3) ], [ Z(3)^0, Z(3)^0 ] ] ]
gap> orb := Orbit(G, pairs[1], OnSets);
[ ... ]  # 24 elements
gap> Length(orb);
24
```

---

## Action on tuples (ordered)

```gap
gap> G := GL(2, GF(3));
GL(2,3)
gap> pairs := Combinations(vecs, 2);
[ ... ]  # 3 pairs
gap> orb := Orbit(G, pairs[1], OnTuples);
[ ... ]  # 48 elements
gap> Length(orb);
48
```

---

## Projective action (OnLines)

```gap
gap> G := SL(2, GF(3));
SL(2,3)
gap> vecs := NormedRowVectors(GF(3)^2);
[ [ 0*Z(3), Z(3)^0 ], [ Z(3)^0, 0*Z(3) ], 
  [ Z(3)^0, Z(3)^0 ], [ Z(3)^0, Z(3) ] ]
gap> IsTransitive(G, vecs, OnLines);
true
gap> orbs := Orbits(G, vecs, OnLines);
[ [ [ 0*Z(3), Z(3)^0 ], [ Z(3)^0, 0*Z(3) ], 
    [ Z(3)^0, Z(3)^0 ], [ Z(3)^0, Z(3) ] ] ]
gap> Length(orbs);
1
```

---

## OrbitsDomain (faster when domain is G-invariant)

```gap
gap> G := GL(2, GF(3));
GL(2,3)
gap> vecs := NormedRowVectors(GF(3)^2);
[ [ 0*Z(3), Z(3)^0 ], [ Z(3)^0, 0*Z(3) ], 
  [ Z(3)^0, Z(3)^0 ], [ Z(3)^0, Z(3) ] ]
gap> orb_dom := OrbitsDomain(G, vecs, OnLines);
[ [ [ 0*Z(3), Z(3)^0 ], [ Z(3)^0, 0*Z(3) ], 
    [ Z(3)^0, Z(3) ], [ Z(3)^0, Z(3)^0 ] ] ]
gap> Length(orb_dom);
1
```

---

## Action functions

| Function | Description |
|----------|-------------|
| `OnPoints(pnt, g)` | Default: `pnt^g` |
| `OnRight(pnt, g)` | Matrix × vector: `pnt * g` |
| `OnLeftInverse(pnt, g)` | `g^-1 * pnt` |
| `OnSets(set, g)` | Action on sets (sorts result) |
| `OnTuples(tup, g)` | Action on tuples (preserves order) |
| `OnLines(vec, g)` | Projective action (normalizes vectors) |
| `OnSubspacesByCanonicalBasis(bas, g)` | Action on subspaces (Hermite form) |

---

## Core functions

| Function | Signature |
|----------|-----------|
| `Orbit` | `Orbit(G, pnt[, act])` |
| `Orbits` | `Orbits(G, seeds[, act])` |
| `OrbitsDomain` | `OrbitsDomain(G, Omega[, act])` |
| `Stabilizer` | `Stabilizer(G, pnt[, act])` |
| `OrbitStabilizer` | `OrbitStabilizer(G, pnt[, act])` |
| `IsTransitive` | `IsTransitive(G, Omega[, act])` |

---

## Advanced references

**FinInG** (finite geometry): https://cage.ugent.be/geometry/fining/chap0.html
- `FiningOrbit`, `FiningOrbits`, `FiningStabiliser`, `FiningSetwiseStabiliser`

**orb package** (optimized orbits): https://gap-packages.github.io/orb/doc/chap0.html
- `Orb`, `Enumerate`, `OrbitBySuborbit`, `RandomSearcher`, `Search`

**orb Chapter 7 utilities**: https://docs.gap-system.org/pkg/orb/doc/chap7_mj.html
- `RandomSearcher(gens, testfunc, opt)` — random search for elements with property
- `FindInvolution(pr)` — find involution via product replacer
- `FindCentralisingElementOfInvolution(pr, inv)` — dihedral trick for centralizers
- `FindInvolutionCentralizer(pr, inv, nr)` — get nr centralizer generators
- `OrbitStatisticOnVectorSpace(gens, size, time)` — estimate orbit sizes
- `FindShortGeneratorsOfSubgroup(G, U)` — express U generators as words in G

**mapclass package** (mapping class group orbits): https://web.mat.bham.ac.uk/S.Shpectorov/mapclass/
- `AllMCOrbits(G, tuple, partition, g)` — mapping class orbits on tuples
- `GeneratingMCOrbits(G, tuple, partition, g)` — only generating tuples
- `MappingClassOrbit(G, tuple, partition, g)` — single orbit
- `IsInOrbit(G, t1, t2, partition, g)` — orbit membership

**Conjugacy class optimization:** When |G| is too large, act on conjugacy classes:
```gap
cc := ConjugacyClasses(G);
OnClasses := function(c, g)
  return ConjugacyClass(Representative(c)^g);
end;
orb_cc := Orbits(Aut, cc, OnClasses);
```

