# Integral trace lattices of number fields

## The lattice and its invariants

For a number field $K/\mathbb Q$, its ring of integers $\mathcal O_K$ is a free
abelian group. The trace pairing defines the integral lattice

$$
T_K=(\mathcal O_K,B_K),\qquad
B_K(x,y)=\operatorname{Tr}_{K/\mathbb Q}(xy).
$$

With an integral basis $e_1,\ldots,e_r$, its Gram matrix has entries
$A_{ij}=\operatorname{Tr}_{K/\mathbb Q}(e_i e_j)$. Its determinant is the signed
field discriminant. Write $\operatorname{sig}(K)=(r_1,r_2)$, where $r_1$ counts
real embeddings and $r_2$ counts conjugate pairs of complex embeddings.

## Classification theorem

**Theorem (Zhang, Theorem 1.1).** If $K$ and $L$ are cyclic extensions of
$\mathbb Q$, then

$$
T_K\cong T_L
\quad\Longleftrightarrow\quad
([K:\mathbb Q],\operatorname{sig}(K),\operatorname{Disc}(K))
=([L:\mathbb Q],\operatorname{sig}(L),\operatorname{Disc}(L)).
$$

The theorem permits wild ramification. For finite abelian extensions, the paper
also gives a sufficient condition: an isomorphism between their Dirichlet
character groups that preserves the conductor and parity of each character
induces an integral trace-lattice isometry. Parity means the value at $-1$.

Source: Zhi-Lin Zhang, *Integral trace forms of cyclic number fields without
tameness*, [arXiv:2610.29876v1](https://arxiv.org/html/2610.29876v1),
21 October 2026. These are theorem statements in the preprint.

## Why the real signature matters

The distinction between field signature and bilinear-form signature is useful
for implementation. At a complex place, multiplication followed by trace gives
$2\operatorname{Re}(zw)$. In real coordinates this has matrix
$\operatorname{diag}(2,-2)$. Each real place contributes a positive square.
Consequently the trace pairing has signature $(r_1+r_2,r_2)$.

Thus the trace lattice is indefinite when $r_2>0$. The sign of its determinant
only records the parity of the negative index; the full signature records the
negative index itself. Retaining the field signature in the invariant tuple
retains precisely the corresponding real information.

## Exact computation in SageMath

The input must identify the maximal order and establish the cyclic-extension
hypothesis. A power basis of a defining polynomial need not be an integral
basis of the maximal order. Its trace determinant can therefore describe a
different lattice. If $\mathbb Z[\alpha]\subseteq\mathcal O_K$ has index $m$,
the two trace determinants differ by the factor $m^2$, from the determinant
rule for a change of lattice basis.

A decision procedure for the stated family compares degree, signature, and
field discriminant. These are exact arithmetic invariants. The
[Sage number-field reference](https://doc.sagemath.org/html/en/reference/number_fields/sage/rings/number_field/number_field.html)
documents the number-field objects and arithmetic operations from which such
a computation can be built.

An explicit isometry has a stronger output contract. For integral bases giving
matrices $A$ and $B$, it must return an integral matrix $P$ with

$$
\det(P)\in\{-1,1\},\qquad P^{\mathsf T}BP=A.
$$

Agreement of the invariant tuples answers existence under the theorem's
hypotheses; it does not itself specify $P$. An implementation that returns an
isometry must construct this map as well. For general abelian fields, preserving
the group law and the conductor and parity functions is stronger than matching
an unordered list of conductor values.

The theorem concerns trace lattices with their number-field origin established.
Applying the invariant tuple to arbitrary indefinite Gram matrices would
discard its essential hypothesis.

See [Computational integral lattices](integral-lattice-algorithms.md) for the
relation to orbit enumeration and mathematical acceptance.
