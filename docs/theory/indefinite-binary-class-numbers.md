# Class numbers of indefinite binary quadratic forms

## The equivalence relation

Write a binary quadratic form as $q(x,y)=ax^2+bxy+cy^2$, with integral
coefficients and discriminant $D=b^2-4ac$. Primitivity means
$\gcd(a,b,c)=1$. Proper equivalence uses changes of variables in
$\operatorname{SL}_2(\mathbb Z)$.

For positive nonsquare $D\equiv0,1\pmod4$, let $h^+(D)$ count these proper
equivalence classes. The discriminants in this definition include those of
nonmaximal quadratic orders.

## Average bound

**Theorem (Diao, Theorem 1.1).** For $X\geq3$,

$$
\sum_{\substack{0<D<X\\D\text{ nonsquare}\\D\equiv0,1\pmod4}}
h^+(D)
\ll \frac{X^{3/2}\sqrt{\log\log X}}{(\log X)^{3/2}}.
$$

The proof uses bounds for the frequency of small fundamental solutions of
Pell equations. The source relates the proper class number to the least
totally positive unit $\eta_D^+$ of the order of discriminant $D$ by

$$
h^+(D)\log\eta_D^+=\sqrt D\,L(1,\chi_D),\qquad
\eta_D^+=\min_{\substack{t,u>0\\t^2-Du^2=4}}
\frac{t+u\sqrt D}{2},
$$

where $\chi_D$ is the Kronecker character.

Source: Yijie Diao, *On the average of class numbers of indefinite binary
quadratic forms*, [arXiv:2610.28001v1](https://arxiv.org/html/2610.28001v1),
20 October 2026, Section 1.1. The bound is a theorem in the preprint.

## Interpretation of the bound

The notation $\ll$ asserts an upper bound up to a constant independent of $X$.
Without an explicit usable constant, the displayed function is not a numerical
ceiling for a particular enumeration. Even with such a constant, an upper bound
on a total does not prove that a returned list contains every class.

An enumeration needs to establish that each representative has the specified
discriminant and is primitive, that distinct representatives are inequivalent,
and that every eligible form is equivalent to one on the list. The average
bound constrains the possible aggregate size of those lists. It does not
supply their representatives or their equivalence decisions.

The class-number formula also explains the role of Pell equations: with $D$
and $L(1,\chi_D)$ fixed, a larger regulator $\log\eta_D^+$ gives a smaller
class number. It does not turn a numerical approximation to the regulator or
the $L$-value into an exact class number without adequate error bounds.

## SageMath conventions

The [Sage binary-form reference](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/binary_qf.html)
uses the coefficient convention $(a,b,c)$ for $ax^2+bxy+cy^2$ and provides
reduction and equivalence operations. Any use for this counting problem must
retain proper equivalence. Allowing determinant $-1$ changes the equivalence
relation and can merge proper classes.

The associated even bilinear Gram matrix is
$\left(\begin{smallmatrix}2a&b\\b&2c\end{smallmatrix}\right)$, whose determinant
is $-D$. Confusing this determinant with $D$ changes both sign and convention.
Likewise, replacing all order discriminants by fundamental discriminants
changes the summation domain.

Ordinary field class groups also identify principal ideals using a different
positivity convention from narrow class groups. Their orders cannot be
substituted for $h^+(D)$ without the corresponding arithmetic relation. These
choices determine the mathematical object being counted before any reduction
algorithm is selected.

See [Computational integral lattices](integral-lattice-algorithms.md).
