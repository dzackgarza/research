\\ Point counts for z^2 = h(x,y) on P^1 x P^1 over F_q, h of bidegree (4,4).
\\ cnt(c, g, q): c a 5x5 matrix of coefficients c[i+1,j+1] of x^i y^j in F_q.
chi(e) = if(e == 0, 0, if(issquare(e), 1, -1));
\\ #C(F_q) for the smooth genus-1 curve y^2 = h(Y), h a squarefree quartic:
\\ C and its Jacobian have the same number of points, and the Jacobian is
\\ y^2 = x^3 - 27 I x - 27 J with I, J the invariants of the quartic
\\ (the classical invariants of a binary quartic; the counts agree with
\\ hyperellcharpoly for p = 11, n = 1, 2, 3).
jaccard(h) = {
  my(a = polcoef(h, 4, 'Y), b = polcoef(h, 3, 'Y), c = polcoef(h, 2, 'Y),
     d = polcoef(h, 1, 'Y), e = polcoef(h, 0, 'Y), I, J);
  I = 12*a*e - 3*b*d + c^2;
  J = 72*a*c*e + 9*b*c*d - 27*a*d^2 - 27*e*b^2 - 2*c^3;
  ellcard(ellinit([0, 0, 0, -27*I, -27*J]));
}
fib(h, g, q) = {
  my(L = polcoef(h, 4, 'Y));
  if(poldegree(h, 'Y) == 4 && poldisc(h) != 0,
    return(jaccard(h)));
  my(s = 1 + chi(L), e);
  for(k = 0, q - 1, e = subst(Pol(digits(k, g.p)), 'x, g); s += 1 + chi(subst(h, 'Y, e)));
  s;
}
cnt(c, g, q) = {
  my(s = 0, xv, h, p = g.p);
  for(k = 0, q - 1,
    xv = subst(Pol(digits(k, p)), 'x, g);
    h = sum(i = 0, 4, sum(j = 0, 4, c[i+1, j+1] * xv^i * 'Y^j));
    s += fib(h, g, q));
  s + fib(sum(j = 0, 4, c[5, j+1] * 'Y^j), g, q);
}
\\ the coefficients of f_star (coble_a21_chamber_fails.py)
C0 = matrix(5, 5);
C0[5,5]=8; C0[5,3]=7; C0[5,1]=6; C0[4,4]=5; C0[4,2]=4; C0[3,5]=3; C0[3,3]=2;
C0[3,1]=3; C0[2,4]=-13; C0[2,2]=-28; C0[1,5]=-10; C0[1,3]=13;
\\ traces of F^n and F^n.iota (eps = -1 lift) on H^2, for q = p^n
traces(p, n) = {
  my(q = p^n, g = ffgen(p^n, 'a), n0, c, ct, N, Nt);
  n0 = g; while(n0 == 0 || issquare(n0), n0 = random(g));
  c = matrix(5, 5, i, j, C0[i, j] * g^0);
  ct = matrix(5, 5, i, j, if((i + j) % 2, 0, C0[i, j] * n0^((i + j - 2) / 2) * n0));
  N = cnt(c, g, q) + q; Nt = cnt(ct, g, q) + q;
  [N - 1 - q^2, Nt - 1 - q^2];
}
\\ The counts of traces(), split for runs of bounded length: x runs over w^k (w a primitive root of F_q) for
\\ k0 <= k < k1 <= (q-1)/2; the fibre over -x = w^(k+(q-1)/2) has the same
\\ count, since f_star(-x, y) = f_star(x, -y) (every monomial has i+j even),
\\ and likewise for the twist, so each k counts twice.  The fibres over
\\ x = 0 and x = infinity are added when k0 = 0.
half(p, n, k0, k1) = {
  my(q = p^n, g = ffgen(p^n, 'a), w, n0, P, Pt, s = 0, st = 0, xv, h, ht);
  w = ffprimroot(g); n0 = w;
  P = vector(5, j, sum(i = 0, 4, C0[i+1, j] * g^0 * 'X^i));
  Pt = vector(5, j, sum(i = 0, 4, if((i + j - 1) % 2, 0, C0[i+1, j] * n0^((i + j - 1) / 2) * n0 * 'X^i)));
  xv = w^k0;
  for(k = k0, k1 - 1,
    h = sum(j = 1, 5, subst(P[j], 'X, xv) * 'Y^(j-1));
    ht = sum(j = 1, 5, subst(Pt[j], 'X, xv) * 'Y^(j-1));
    s += 2 * fib(h, g, q); st += 2 * fib(ht, g, q);
    xv *= w);
  if(k0 == 0,
    s += fib(subst(sum(j = 1, 5, P[j] * 'Y^(j-1)), 'X, 0*g), g, q) + fib(sum(j = 1, 5, polcoef(P[j], 4, 'X) * 'Y^(j-1)), g, q) + q;
    st += fib(subst(sum(j = 1, 5, Pt[j] * 'Y^(j-1)), 'X, 0*g), g, q) + fib(sum(j = 1, 5, polcoef(Pt[j], 4, 'X) * 'Y^(j-1)), g, q) + q);
  [s, st];
}
