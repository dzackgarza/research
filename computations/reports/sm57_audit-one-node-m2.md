# The one-node locus of the direct projective construction: audit and completion

Author: m2 (swarm smvz57fr3), direction d3 (parameter-space geometry).
Repo read at commit `40ab2c8f29` ("docs: the locus is path-connected by a
generic-pencil argument"); the audited texts are
`writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`
(prop:one-node-connected, prop:one-node-family, thm:one-node-transport,
thm:a21-labels) and `writing/coble/heegner-report/coble-heegner-research-report.md`
lines 341-470, 585-700.  Nothing in the repo was modified.

**Verdict in one line.** Disputed item (1) of the task is *resolved in the
affirmative*: the pencil argument is correct, but as written it has two real gaps
(the openness of B in H_p, and the absence of a fixed component needed for
Bertini); both are filled below (`lem:open`, `lem:irred`).  With them the one-node
locus is a non-empty *path-connected* open subset of a P^11, so `thm:a21-labels`
(labels) stands.  Connectedness says nothing about the chamber; see
`uniform-ample-class-and-chamber.md`.

## 0. Notation

Y = P^1 x P^1 with coordinates x = [x_0:x_1], y = [y_0:y_1]; tau(x,y) = (-x,-y);
p = ([1:0],[1:0]) one of the four tau-fixed points; V = |O_Y(4,4)|^tau (the
tau-invariant linear system);

  H_p := { f in V : f(p) = 0 },
  B   := { f in H_p : the branch divisor C_f = {f=0} is smooth away from p
                      and has an ordinary node at p }.

B is the parameter locus of prop:one-node-family, i.e. the set over which the
construction is the one-node family with X^sharp = {z^2 = f}.

## 1. Two bookkeeping lemmas

**lem:dim.** h^0(O_Y(4,4)) = 25 with basis x_0^{4-i}x_1^i y_0^{4-j}y_1^j,
0 <= i,j <= 4; tau acts by (-1)^{i+j} on that monomial, so
h^0(O_Y(4,4))^tau = #{i+j even} = 3*3 + 2*2 = 13, and |V| = P^12.
Evaluation at p is the coefficient of x_0^4 y_0^4, a non-zero linear functional
(that monomial is tau-invariant), so **H_p is a hyperplane P^11 of V** and
dim B = 11.  [This is the report's "dimension 11"; the count 13 is correct.]

**lem:tau.** For f in V and a tau-fixed point q, f vanishes to first order at q
identically: in local coordinates (u,v) at q, tau acts by (u,v) -> (-u,-v), so
f(-u,-v) = f(u,v) forces every odd-degree term to vanish.  Hence
  (i) df(q) = 0 for every f in V: *on H_p, p is automatically a singular point of
      C_f*, and the "node condition" is exactly det Hess_p(f) != 0 (the order at p
      is then exactly 2 and the point is an ordinary node);
  (ii) the four monomials x_0^4y_1^4, x_1^4y_0^4, x_1^4y_1^4 are the only ones
      non-zero at the respective other tau-fixed points, so "f(q) != 0 for the
      other three tau-fixed points" is an open condition inside H_p, and it is
      part of "smooth away from p".
Consequence: B = H_p minus ({det Hess_p = 0} union {C_f singular somewhere away
from p}).  Verified on the report's example and on random members of H_p:
`verification/check_Hp_vs_B.log`.

## 2. Gap 1: B is open in H_p (this is *not* just "smoothness is open")

The source justifies openness by "the node condition is the vanishing of the
coefficient of x_0^4y_0^4 together with nondegeneracy of the quadratic part, an
open condition, and smoothness elsewhere is open".  The last clause is not
sufficient: Y is not compact in a chart, and a second singularity may travel to p
as f varies, so one has to exclude *escape to p*.  The non-degeneracy of Hess_p
does that.

**lem:open.** Let f_k -> f_0 in H_p with f_0 in B and det Hess_p(f_k) != 0 for all
k.  Then for k large, C_{f_k} has no singular point other than p; consequently B
is open in H_p.

*Proof.* Suppose not: there are k_j -> infinity and q_j != p with q_j singular on
C_{f_{k_j}}.  Y is compact, so pass to q_j -> q.  Because f_{k_j} -> f_0
uniformly on Y in the coefficients, f_0(q) = 0 and df_0(q) = 0, so q is a
singular point of C_{f_0}; as f_0 in B, q = p.

Escape to p is excluded as follows.  Fix a chart U around p with coordinates
(u,v), p = 0, and let grad f : U -> C^2 be the gradient map.  Its differential at 0
is the Hessian matrix.  Since A_k := Hess_p(f_k) -> A_0 := Hess_p(f_0) with A_0
invertible, ||A_k^{-1}|| <= C uniformly.  The second-order remainder of f_k is
controlled uniformly on the unit ball (the coefficients converge), say
|grad f_k(u,v) - A_k(u,v)| <= C' |(u,v)|^2.  Hence for 0 < |(u,v)| = r < 1/(CC')
  |grad f_k(u,v)| >= |A_k(u,v)| - C' r^2 >= r/C - C' r^2 > 0,
so grad f_k has no zero in the punctured ball of radius r, uniformly in k.  Thus
q_j is outside that ball for j large, and q = lim q_j is outside the ball of
radius r/2 - contradicting q = p.  (This is the quantitative inverse function
theorem applied to grad f_k, with uniformity coming from convergence of the
coefficients; note that the Hessian of f_k need not be invertible away from 0, so
the argument must be made for the map grad f_k itself and not for its
differential.)  QED

*Remark.* This is the only place where non-degeneracy of Hess_p is used beyond
the definition of B, and it is why B is the right locus: on the hypersurface
{det Hess_p = 0} inside H_p the node at p degenerates and the resolution picture
of prop:del-pezzo-type-on-the-resolution no longer applies.

## 3. Gap 2: members of B are irreducible, so pencils have no fixed component

Bertini's theorem for a pencil requires that the pencil have no fixed component.
The source does not check this.  It holds, but not for the reason one might
expect (a single node does *not* by itself forbid a factorisation - a product of
two smooth curves crossing transversally at p is nodal there); the argument uses
the exclusion of *other* singular points and Bezout.

**lem:irred.** Let f in H_p with det Hess_p(f) != 0 and with no singular point of
C_f except p.  Then f is not a product of two forms of positive bidegree.

*Proof.* Suppose f = gh with g in H^0(O(a,b)), h in H^0(O(4-a,4-b)), a,b in
{0,...,4} and both factors non-constant.  (A divisor of a section of O(4,4) is
itself a section of O(a,b) with a,b >= 0, because H^0(O(a,b)) = 0 otherwise.)
Write m_g, m_h for the vanishing orders at p; m_g + m_h = 2.  Any point of
C_g cap C_h is a singular point of C_f (f and both partials vanish there), so
C_g cap C_h is contained in {p}.  The intersection number is
  (a,b).(4-a,4-b) = 4(a+b) - 2ab   [form ad+bc on Pic(P^1 x P^1)],
which is a positive even integer for every non-trivial split.  Cases:
 - (m_g,m_h) = (0,2) or (2,0): then p is not on one of the two curves, so
   C_g cap C_h, which is non-empty by the positivity of the intersection number,
   contains a point other than p: contradiction.
 - (m_g,m_h) = (1,1): the quadratic part of f at p is the product of the linear
   parts of g and h at p; non-degeneracy forces them to be independent, so the
   local intersection multiplicity at p is 1, and since C_g cap C_h = {p} the
   intersection number equals 1 - contradicting that it is even and positive.
QED

Consequence (**lem:base**): for f_0 != f_1 in B, f_0 is irreducible (lem:irred),
f_1 is not proportional to it, so gcd(f_0,f_1) = 1 and the base locus Z of the
pencil <f_0,f_1> is a finite set (Bezout: 32 points with multiplicity).  Also no
member of the pencil is the zero form (f_0,f_1 are linearly independent as
points of the projective space differ).

## 4. The pencil theorem

**thm:pencil.** Let f_0, f_1 in B, f_0 != f_1, and l = P(<f_0,f_1>) the pencil.
Then l cap (H_p \ B) is finite; equivalently l cap B = l minus a finite set, which
is a non-empty connected (indeed smooth affine) curve.  Consequently any two
points of B are joined by a path inside B, i.e. **B is path-connected**.

*Proof.* l is contained in H_p (evaluation at p is linear).  Write f_t for the
member with parameter t in l = P^1.  Three bad conditions, all of them closed in
l and all of them proper:
 (i) det Hess_p(f_t) = 0.  The entries of the Hessian at the fixed point p are
     linear functionals of f, so det Hess_p is a polynomial of degree <= 3 in t;
     it is not the zero polynomial because det Hess_p(f_0) != 0.  So (i) is
     empty or consists of at most 3 points.
 (ii) there is q in Z \ {p} with df_t(q) = 0 (then automatically f_t(q) = 0).
     For fixed q the conditions df_t(q) = 0 are two *linear* equations in t, so
     the set is empty or a single point; f_0 is smooth at q (q != p, f_0 in B),
     so it is not the whole line.  Z is finite, so (ii) is finite.
 (iii) there is q outside Z, q != p, with f_t(q) = df_t(q) = 0.
     Put T := {t : such a q exists} and
     T' := T union {t : some q in Z \ {p} is singular on C_{f_t}} (= condition
     (ii), already known to be finite).
     *Closedness of T'.*  Let t_n -> t_* in T' and q_n a singular point of C_{f_{t_n}}
     witnessing it.  Y is compact, so q_n -> q after a subsequence, and then q is
     singular on C_{f_{t_*}} by continuity.  If q is outside Z and outside {p}, then
     t_* in T.  If q in Z \ {p}, then t_* satisfies (ii).  If q = p, then t_* satisfies
     (i): indeed, if det Hess_p(f_{t_*}) != 0 the escape-to-p argument of lem:open,
     applied to the sequence f_{t_n} -> f_{t_*} (whose coefficients converge), gives
     a ball around p free of singular points of C_{f_{t_n}} for n large, and q_n is
     in it.  So T' is closed.
     *Properness.*  Bertini's theorem for the pencil <f_0,f_1> (no fixed component by
     lem:base, ground field C) says the general member has no singular point outside
     the base locus Z, i.e. is not in T'.  Hence T' != l.
     Now T \ ((i) union (ii)) is a closed subset of l \ ((i) union (ii)), and it is
     proper there because the general member is in T' only if it is in (i) or (ii),
     both of which are finite and do not contain the general member (f_0 shows (i)
     and (ii) are proper).  A proper closed subset of P^1 minus a finite set is
     finite (a closed subset of an open U in P^1 is U cap F with F closed in P^1,
     and if U cap F is infinite then F is infinite, hence F = P^1, hence U cap F = U).
     So T is contained in the finite set (i) union (ii) union (a finite set).
For t outside (i) cap (ii) cap (iii): p is singular with non-degenerate quadratic
part (lem:tau and not (i)), so p is an ordinary node; every singular point of
C_{f_t} other than p is a base point by not-(iii), and none exists by not-(ii);
so f_t lies in B.  Conversely a bad member lies in (i) cap (ii) cap (iii).  Hence
l cap B = l minus a finite set.  QED

**cor:connected.** B is a non-empty path-connected open subset of H_p = P^11.  In
particular for any two b, b' in B there is a smooth connected curve
l cap B (= P^1 minus finitely many points) containing both, over which the family
of prop:one-node-family is smooth and proper with K3 fibres, a relative
polarization and an exceptional divisor; hence the Gauss-Manin transport of
thm:one-node-transport applies along a path in it and yields
gamma in O(L_K3) with gamma S_Co = S'_Co, gamma S_dP = S'_dP, gamma H = H',
gamma alpha = alpha'.  That is the three label clauses of A21 (thm:a21-labels).

**Non-emptiness.** The report's example
  f = 29x^4y^4+23x^4y^2+19x^4+17x^3y^3+13x^3y+11x^2y^4+7x^2y^2+x^2+5xy^3+xy
      +3y^4+2y^2
has f(p) = 0 (no constant term), is tau-invariant, has quadratic part
x^2+xy+2y^2 (det 7), and the Jacobian ideal of its singular locus is
(x1,y1) on the chart x0=y0=1 and the unit ideal on each of the other three
charts: exactly one singular point, an ordinary node at p.  Rechecked here from
scratch in `verification/check_nodal.log` (Groebner bases, exact rational
arithmetic, all four charts).  So B is non-empty; three perturbations inside H_p
and four random members of H_p (`verification/check_second.log`,
`verification/check_Hp_vs_B.log`) are also one-nodal, and a random member of V
with a non-zero constant term is *not* (it is singular at other tau-fixed
points), which shows H_p \ B is non-trivial and that the openness statement is
not vacuous.

## 5. Audit of disputed item (2): the family and the transport

(a) *The simultaneous resolution.*  Locally at the node the total space is
  { z^2 = x^2 + y^2 + (terms of order >= 3 in x,y, coefficients in the parameter) }
and the singular locus is the section sigma(B).  Blow up the smooth centre
sigma(B).  In the chart x != 0 put y = xu, z = xv: the strict transform is
u - v^2 = 0 (smooth); in the chart z != 0 put x = zu, y = zv: the strict
transform is 1 - u^2 - v^2 - z(...) = 0, smooth because its derivative in z is
non-zero along z = 0; the chart y != 0 is the same as the first.  So the strict
transform is smooth over B and its fibres are the minimal resolutions of the
fibres.  This is the one computation prop:one-node-family(1) asserts without
giving, and it is correct.

(b) *Flatness and properness.*  X^sharp is the closed subscheme z^2 = f_b of the
total space of O(-2,-2) over Y x B; z^2 - f_b is a non-zero-divisor, so the
quotient is flat over B, finite hence proper, and projective.  Correct.  (Only
typing: the sheaf of algebras in the source is written O + L^{-1} with
L = O(2,2), i.e. O_Y + O_Y(-2,-2), which is the right thing; the multiplication
uses f_b in H^0(O(4,4)) = H^0(L^2).)

(c) *The classes.*  H = pi^*O(1,1) and [D] = pi^*[e] (e the exceptional curve of
Y-hat = Bl_p Y).  For the second: e is not a component of the branch divisor
(e . B-tilde = e . ((4,4) - 2e) = 2), so pi^{-1}(e) is the preimage cycle, and for
the finite flat pi it equals pi^*e; over e = P^1 it is a double cover branched in
the e . B-tilde = 2 points e cap B-tilde, hence connected, hence isomorphic to
P^1; it contains pi^{-1}(p), and pi^{-1}(p) is the node, which the resolution
replaces by D, so pi^{-1}(e) = D.  (Consistently (pi^*e)^2 = 2e^2 = -2 = D^2.)
[The weaker statement "(pi^*e - D) . D = 0 and (pi^*e - D)^2 = 0" does *not*
by itself force pi^*e = D, so the connectedness argument above is the one to use.]
Both H and [D] are first Chern classes of line bundles on the total space, hence
flat sections of R^2 pi_* Z, hence preserved by Gauss-Manin transport; correct.
What the transport does *not* give is the chamber - agreed, and sharpened in
`uniform-ample-class-and-chamber.md`.

**Verdict.** (2) holds as stated, with (a) supplied.  (1) holds, with lem:open and
lem:irred supplied.  Both earlier failed routes (plain discriminant argument;
Tjurina constancy) are beside the point: the pencil argument is not a
semi-continuity argument about the discriminant, and the two gaps above are the
only ones it has.

## 6. What this does and does not establish

Established: B is non-empty, open and path-connected; hence, *given* the family
and transport of prop:one-node-family / thm:one-node-transport (audited in §5),
the label clauses of A21 hold for every pair of one-node members.  This is exactly
thm:a21-labels of the repo, now with a complete proof.

Not established, and not touched by any argument above: the chamber clause.
Connectedness transports the local system, not the Kaehler cone; a connected base
gives no information about the effective (-2)-classes.  That is
`uniform-ample-class-and-chamber.md`, where the chamber clause is settled for all
pairs whose transported Picard lattices agree (a comeager set of pairs), and the
exact residual condition is named.
