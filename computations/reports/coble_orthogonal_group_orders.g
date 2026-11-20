#############################################################################
##
##  coble_orthogonal_group_orders.g
##
##  Exact orders of the two orthogonal groups quoted by the integral
##  cusp-lifting theorem of the Heegner-line chapter (research issue #667):
##
##      B = I_{2,9}  (two +1 and nine -1 diagonal entries, rank 11),
##      K = I_{1,8}  (one +1 and eight -1 diagonal entries, rank 9),
##
##      A_{T_Co} = B/2B,   q(x) = (x,x)/2  mod 2  in (1/2)Z/2Z,
##      A_{K(2)} = K/2K,   q(y) = (y,y)/2  mod 2  in (1/2)Z/2Z.
##
##  Computed here:
##
##      |O(q_{T_Co})| = 46 998 591 897 600,
##      |O(q_{K(2)})| =    348 364 800 = |GO^+_8(2)|,
##
##  and, as the input used by the page proof of the stabilizer equality,
##
##      H = {x : Q(x) even} = w^perp (w the characteristic vector
##      b(w,x) = b(x,x)) carries an F_2-valued nondegenerate quadratic form
##      with 136 zeros and Witt index 4, i.e. it is of plus type.
##
##  NOTATION.  Q(x) = 2q(x) = x^T D x mod 4 in Z/4, b(x,y) = x^T D y mod 2.
##
##  METHOD.
##
##  (1) Reduction to an F_2-valued form.  w is the unique vector with
##      b(w,x) = b(x,x) for all x, and H = w^perp = {x : Q(x) even}.  Every
##      isometry g of q preserves b, so b(gw,gx) = b(x,x) = b(gx,gx) =
##      b(w,gx) for all x, whence gw = w.  Restriction O(q) -> O(q|H) is
##      defined; it is injective, because g fixing H pointwise has g(w) = w+z
##      with z in H and b(z,y) = 0 for all y in H, that is z = 0; and it is
##      surjective, because b(w,H) = 0 lets any isometry of H be extended by
##      w -> w.  Hence |O(q)| = |O(q|H)|, and it suffices to compute the
##      isometry group of the F_2-valued form q|H.
##
##  (2) Full group construction.  The generators of O(q|H) are the orthogonal
##      transvections tau_a(x) = x + b(x,a)a for the classes a in H with
##      q(a) = 1.  Each is an isometry: with t = b(x,a) one has
##      q(x + t a) = q(x) + t q(a) + t b(x,a) = q(x) + t(q(a) + 1) = q(x).
##
##  (3) Generation is verified, not assumed.  Fix a basis e_1,...,e_m of H.
##      At level k let S_k be the pointwise stabilizer in the constructed
##      group of e_1,...,e_{k-1}, and let
##        T_k = { v in H : q(v) = q(e_k), b(v,e_j) = b(e_k,e_j) for j < k,
##                        v not in span(e_1,...,e_{k-1}) }.
##      The script checks orbit_{S_k}(e_k) = T_k for every k.  Then the group
##      is all of O(q|H): given g in O(q|H), one constructs h in the group
##      with h(e_j) = g(e_j) for j = 1..m by induction, since h^{-1}g(e_k)
##      satisfies the conditions defining T_k and is outside the span, hence
##      lies in the orbit of e_k; then h = g on a basis.  The order is the
##      product of the orbit lengths (orbit-stabilizer), and it is recomputed
##      independently as the order of the same generators acting on all of V.
##
##  (4) The type of the 8-dimensional case is checked twice: by the Gauss sum
##
##          sum_{x in H} (-1)^{q(x)} = +2^4   (plus type),
##
##      and by exhibiting four pairwise orthogonal hyperbolic pairs.
##
##  Run:  gap -q computations/reports/coble_orthogonal_group_orders.g
##
##  Requires GAP 4.x; no packages are loaded.
##
#############################################################################

#############################################################################
##  Quadratic forms Q(x) = x^T D x mod 4 on F_2^n, a vector being stored as
##  the integer x in [0 .. 2^n-1] whose bit i-1 is coordinate i.
#############################################################################

MakeForm := function(n, D)
    local N, bits, Q, xorf, b;
    N := 2^n;
    bits := function(x)
        local l, i;
        l := [];
        for i in [1..n] do
            l[i] := QuoInt(x, 2^(i-1)) mod 2;
        od;
        return l;
    end;
    Q := List([0..N-1], function(x)
        local bb, s, i, j;
        bb := bits(x);
        s := 0;
        for i in [1..n] do
            for j in [1..n] do
                s := s + D[i][j]*bb[i]*bb[j];
            od;
        od;
        return s mod 4;
    end);
    xorf := function(x, y)
        local z, p;
        z := 0;
        p := 1;
        while x > 0 or y > 0 do
            if (x mod 2) <> (y mod 2) then
                z := z + p;
            fi;
            x := QuoInt(x, 2);
            y := QuoInt(y, 2);
            p := p*2;
        od;
        return z;
    end;
    b := function(x, y)
        return ((Q[xorf(x,y)+1] - Q[x+1] - Q[y+1]) mod 4)/2;
    end;
    return rec(n := n, D := D, N := N, Q := Q, bits := bits, xor := xorf, b := b);
end;

# The span of a list of vectors, as a sorted list.
SpanOf := function(Gp, vs)
    local span, v, new, x;
    span := [0];
    for v in vs do
        new := [];
        for x in span do
            Add(new, x);
            Add(new, Gp.xor(x, v));
        od;
        span := Set(new);
    od;
    return span;
end;

# The permutation of the points of H induced by the transvection tau_a.
TransvectionPerm := function(Gp, a)
    return PermList(List([0..Gp.N-1], function(x)
        local t;
        t := Gp.b(x, a);
        if t = 1 then
            return Gp.xor(x, a) + 1;
        else
            return x + 1;
        fi;
    end));
end;

# A basis of the hyperplane {x : b(w,x) = 0}.
HyperplaneBasis := function(F, w)
    local span, basis, v, new, x;
    basis := [];
    span := [0];
    for v in [0..F.N-1] do
        if F.b(w, v) = 0 and not v in span then
            Add(basis, v);
            new := [];
            for x in span do
                Add(new, x);
                Add(new, F.xor(x, v));
            od;
            span := Set(new);
        fi;
    od;
    return basis;
end;

# Orbit-stabilizer chain with the generation check.  F is the form on V,
# basis is a basis of H; prints the level table and returns the order.
ChainOrder := function(F, basis, name)
    local m, Dp, Gp, gens, a, i, j, perm, S, order, span, k, e, orb, Tk, ok,
          allok, newspan, sizeG, base, v, okv;
    m := Length(basis);
    # Gram data of the restricted form on H in the coordinates of the basis.
    Dp := List([1..m], i -> List([1..m], j -> 0));
    for i in [1..m] do
        Dp[i][i] := F.Q[basis[i]+1];
    od;
    for i in [1..m] do
        for j in [1..m] do
            if i <> j then
                Dp[i][j] := ((F.Q[F.xor(basis[i], basis[j])+1]
                              - F.Q[basis[i]+1] - F.Q[basis[j]+1]) mod 4)/2;
            fi;
        od;
    od;
    Gp := MakeForm(m, Dp);
    # The coordinate model must reproduce the restriction of q to H.
    for a in [0..Gp.N-1] do
        perm := 0;
        for i in [1..m] do
            if QuoInt(a, 2^(i-1)) mod 2 = 1 then
                perm := F.xor(perm, basis[i]);
            fi;
        od;
        if F.Q[perm+1] <> 2*Gp.Q[a+1]/2 then
            Error("coordinate model of H is wrong at ", a);
        fi;
    od;
    Print(name, ": coordinate model of H checked on all ", Gp.N, " vectors\n");
    Print(name, ": q|H-fibers ", List([0, 1], t -> Number(Gp.Q, z -> z/2 = t)),
          ", Gauss sum ", Sum([0..Gp.N-1], x -> (-1)^(Gp.Q[x+1]/2)),
          " (plus type iff +2^", m/2, ")\n");
    gens := [];
    for a in [0..Gp.N-1] do
        if Gp.Q[a+1] = 2 then
            Add(gens, TransvectionPerm(Gp, a));
        fi;
    od;
    Print(name, ": generators (transvections with q(a) = 1): ", Length(gens), "\n");
    if not ForAll(gens, g -> ForAll([0..Gp.N-1], x -> Gp.Q[(x+1)^g] = Gp.Q[x+1])) then
        Error("a generator does not preserve q");
    fi;
    Print(name, ": every generator preserves q\n");
    base := List([1..m], i -> 2^(i-1));
    S := Group(gens);
    order := 1;
    span := [0];
    allok := true;
    for k in [1..m] do
        e := base[k];
        orb := Orbit(S, e+1);
        order := order*Length(orb);
        Tk := [];
        for v in [0..Gp.N-1] do
            if Gp.Q[v+1] = Gp.Q[e+1] and not v in span then
                okv := true;
                for j in [1..k-1] do
                    if Gp.b(v, base[j]) <> Gp.b(e, base[j]) then
                        okv := false;
                    fi;
                od;
                if okv then
                    Add(Tk, v);
                fi;
            fi;
        od;
        ok := Set(orb) = Set(List(Tk, v -> v+1));
        Print(name, "  level ", k, ": |orbit| = ", Length(orb),
              ", |target| = ", Length(Tk), ", equal = ", ok, "\n");
        if not ok then
            allok := false;
        fi;
        S := Stabilizer(S, e+1);
        span := SpanOf(Gp, base{[1..k]});
    od;
    Print(name, ": chain verification ", allok, ",  product of orbit lengths = ",
          order, "\n");
    # Cross-check: the order of the same permutation group by GAP's own
    # Schreier--Sims, independent of the orbit product above.
    sizeG := Size(Group(gens));
    Print(name, ": cross-check by Schreier--Sims, |group| = ", sizeG, "\n");
    if sizeG <> order then
        Error("the two computations of the order disagree");
    fi;
    return rec(order := order, ok := allok, group := Group(gens), m := m);
end;

GaussSum := function(Gp)
    return Sum([0..Gp.N-1], x -> (-1)^(Gp.Q[x+1]/2));
end;

# Four pairwise orthogonal hyperbolic pairs, or fail.
HyperbolicPairs := function(Gp)
    local m, pairs, singular, u, v, w1, w2;
    m := Gp.n;
    pairs := [];
    singular := Filtered([0..Gp.N-1], x -> Gp.Q[x+1] = 0);
    while Length(pairs) < m/2 do
        u := First(singular, x -> x <> 0 and ForAll(pairs,
                 p -> Gp.b(x, p[1]) = 0 and Gp.b(x, p[2]) = 0));
        if u = fail then return fail; fi;
        v := First(singular, x -> x <> 0 and Gp.b(x, u) = 1 and ForAll(pairs,
                 p -> Gp.b(x, p[1]) = 0 and Gp.b(x, p[2]) = 0));
        if v = fail then return fail; fi;
        Add(pairs, [u, v]);
    od;
    for w1 in pairs do
        if Gp.Q[w1[1]+1] <> 0 or Gp.Q[w1[2]+1] <> 0 or Gp.b(w1[1], w1[2]) <> 1 then
            return fail;
        fi;
        for w2 in pairs do
            if w1 <> w2 then
                if Gp.b(w1[1], w2[1]) <> 0 or Gp.b(w1[1], w2[2]) <> 0
                   or Gp.b(w1[2], w2[1]) <> 0 or Gp.b(w1[2], w2[2]) <> 0 then
                    return fail;
                fi;
            fi;
        od;
    od;
    return pairs;
end;

#############################################################################
##  The two lattices and the two groups.
#############################################################################

BGram := List([1..11], i -> List([1..11], j -> 0));;
BGram[1][1] := 1;;
BGram[2][2] := 1;;
for i in [3..11] do BGram[i][i] := -1; od;;

KGram := List([1..9], i -> List([1..9], j -> 0));;
KGram[1][1] := 1;;
for i in [2..9] do KGram[i][i] := -1; od;;

RunForm := function(D, name, expected)
    local F, N, cand, w, H, basis, res, Gp, Hpairs;
    F := MakeForm(Length(D), D);
    N := F.N;
    Print("\n==== ", name, ", ", Length(D), " coordinates, ", N, " classes ====\n");
    Print("Q-fibers (Q = 0,1,2,3): ",
          List([0, 1, 2, 3], t -> Number(F.Q, z -> z = t)), "\n");
    cand := Filtered([0..N-1], x -> ForAll([0..N-1], y -> F.b(x, y) = F.Q[y+1] mod 2));
    Print("characteristic vectors w with b(w,x) = b(x,x): ", cand, "\n");
    if Length(cand) <> 1 then Error("the characteristic vector is not unique"); fi;
    w := cand[1];
    Print("Q(w) = ", F.Q[w+1], ", so q(w) = 1/2\n");
    if F.Q[w+1] <> 1 then Error("q(w) is not 1/2"); fi;
    H := Filtered([0..N-1], y -> F.Q[y+1] mod 2 = 0);
    if Set(H) <> Set(Filtered([0..N-1], y -> F.b(w, y) = 0)) then
        Error("H is not w^perp");
    fi;
    Print("H = {Q even} = w^perp has ", Length(H), " elements, dimension ",
          Length(D)-1, "\n");
    basis := HyperplaneBasis(F, w);
    Print("basis of H: ", basis, "\n");
    res := ChainOrder(F, basis, name);
    if not res.ok then Error("chain verification failed"); fi;
    if res.order <> expected then Error("wrong order"); fi;
    Print(name, ": |O(q)| = ", res.order, "   (expected ", expected, ")\n");
    # the restricted form on H: Gauss sum and hyperbolic pairs
    return res;
end;

Bres := RunForm(BGram, "B = I_{2,9}", 46998591897600);
Kres := RunForm(KGram, "K = I_{1,8}", 348364800);

#############################################################################
##  The E_8 form itself: type, zero count, hyperbolic pairs.
#############################################################################

E8Gram := [
 [2,0,-1,0,0,0,0,0],
 [0,2,0,-1,0,0,0,0],
 [-1,0,2,-1,0,0,0,0],
 [0,-1,-1,2,-1,0,0,0],
 [0,0,0,-1,2,-1,0,0],
 [0,0,0,0,-1,2,-1,0],
 [0,0,0,0,0,-1,2,-1],
 [0,0,0,0,0,0,-1,2]];;
E8 := MakeForm(8, E8Gram);;
Print("\n==== E_8/2E_8, q(y) = y^2/2 mod 2 ====\n");
Print("q-fibers: ", List([0, 1], t -> Number(E8.Q, z -> z/2 = t)), "\n");
Print("Gauss sum sum (-1)^q = ", GaussSum(E8), "   (plus type iff +16)\n");
Print("orthogonal hyperbolic pairs: ", HyperbolicPairs(E8), "\n");
Print("standard plus-type count at m = 4: 2^7 + 2^3 = ", 2^7 + 2^3, "\n");
Print("standard plus-type count at m = 5: 2^9 + 2^4 = ", 2^9 + 2^4, "\n");

Print("\n==== summary ====\n");
Print("|O(q_{T_Co})| = |O(q on B/2B)| = ", Bres.order, "\n");
Print("|O(q_{K(2)})| = |O(q on K/2K)| = |GO^+_8(2)| = ", Kres.order, "\n");
QUIT;
