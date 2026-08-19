# Ergebnisse der Mathematik und ihrer Grenzgebiete

![](images/712423ee04bf0bb54cc94c272775bf0461eebdf42b89456d9261d6e6a1edc415.jpg)

![](images/a4ec622226500c5318745125c8eec3c6c70107b5bc986a509561d99930d6344f.jpg)

J. Milnor ·D.Husemoller

![](images/d600e1809639e4c4732488941e493779ac9b313b6b45303b600ee41ed811ed66.jpg)

John Milnor The Institute for Advanced Study,Princeton, New Jersey 08540, U.S.A.

Dale Husemoller Haverford College,Haverford,Pennsylvania 19041, U.S.A.

# ISBN 0-387-06009-X Springer-Verlag New York Heidelberg Berlin ISBN 3-540-06009-X Springer-Verlag Berlin Heidelberg New York

This work is subject to copyright.Allrights arereserved,whether the whole or part of the material is concerned,specifically those of translation,reprinting,re-use of ilustrations,broadcasting,reproduction by photocopying machine or similar means,and storage in data banks. Under $\ S 5 4$ of the German Copyright Law where {copies are made for other than private use,afee is payable to the publisher, the amount of the fee to be determined by agreement with the publisher. $\circledcirc$ by Springer-Verlag BerlinHeidelberg 1973.Library of Congress Catalog Card Number 72-90190.Printedin Germany. Typeseting, printing and binding: Universitatsdruckerei H.Sturtz AG,Wurzburg.

![](images/0578a1f4c7abd984cf1c9a93d50a71d09c548dba8e6c12b16a4fc8c358cb4108.jpg)

The theory of quadratic forms and the intimately related theory of symmetric bilinear forms have a long and rich history,highlighted by the work of Legendre, Gauss,Minkowski, and Hasse. (Compare [Dickson] and [Bourbaki, 24, p.185].) Our exposition will concentrate on the relatively recent developments which begin with and are inspired by Witt's 1937 paper “Theorie der quadratischen Formen in beliebigen Korpern.” We will be particularly interested in the work of A.Pfister and M. Knebusch. However,some older material willbe described, particularly in ChapterII. The presentation is based on lectures by Milnor at the Institute for Advanced Study, and at Haverford College under the Phillips Lecture Program,during the Fall of 1970,as well as lectures at Princeton University in 1966. We want to thank J. Cunningham, M. Knebusch,M. Kneser, A. Rosenberg, W. Scharlau and J.-P. Serre for helpful suggestions and corrections.   
Prerequisites. The reader should be familiar with the rudiments of algebra, including for example the concept of tensor product for modules over a commutative ring. A few individual sections will require quite a bit more.

The logical relationship between the various chapters can be roughly described by the diagram below. There are also five appendices,largely self-contained, which treat special topics.

I. Arbitrary commutative rings ← ← ←   
II. The ring of II. Fields V. Miscellaneous   
integers examples ← IV.Dedekind domains

![](images/60b8dfef6381a83d1e94465a04c5bf0422c4b77f2ee992ef81148142c109cbe4.jpg)

![](images/78addfb9d47373f39056917e1f2a0b1af48df1d2f98dc30daa7436154d88aeab.jpg)

# Chapter I. Basic Concepts.．．.

$\ S 1$ . Bilinear Forms and Inner Products.. 1   
$\ S 2$ .Bilinear Forms over a Free Module . 3   
$\ S 3$ .Orthogonal Sums 4   
$\ S 4 .$ .Witt's Theorem. 7   
$\ S$ 5.Tensor Products and Exterior Powers 9   
$\ S 6$ .Split Inner Product Spaces 12   
$\ S 7$ The Witt Ring.. 14

Chapter II.Symmetric Inner Product Spaces over Z ....．. 15

$\ S 1$ . Minkowski's Convex Body Theorem 15   
$\ S 2$ .Inner Product Spaces of Rank ≤4 over Z 18   
$\ S 3$ . The Hasse-Minkowski Theorem and Meyer's Theorem 20   
$\ S 4$ Indefinite Spaces over Z. 22   
$\ S 5$ .Spaces of Type II . 24   
$\ S 6$ .The Classification Problem for Positive Definite Spaces 26   
$\ S 7 .$ .The Packing of Equal Balls in $\mathbf { R } ^ { n }$ 29   
$\ S 8$ . Sums of Two and Four Squares. 39   
$\ S 9$ A Theorem of Siegel ：. 41

# Chapter II. Inner Product Spaces over a Field．．.....．． 56

\$1. Anisotropic Inner Product Spaces . . .. 56   
\$2.Ordered Fields． 59   
\$ 3.Prime Ideals in the Witt Ring. 65   
\$ 4.Multiplicative Inner Product Spaces . 72   
\$5.The Powers of the Fundamental Ideal .. 76

Chapter IV. Discrete Valuations and Dedekind Domains ..... 84

$\ S 1$ . The Homomorphism $\partial _ { v } \colon W ( F ) \to W ( { \overrightarrow { F } } )$ 84   
$\ S 2 .$ Computation of $W ( \mathbf { Q } )$ 87   
$\ S 3 .$ Dedekind Domains 91   
$\ S 4$ Number Fields. 94

Chapter V. Some Examples ... ..100

$\ S 1$ .Homology Theory of Manifolds．．．．．． ．．．100   
$\ S 2$ .Rings of Smooth Real Valued Functions．．． ．． 105   
\$ 3.The Discriminant of a Field Extension. 107

Appendix 1. Quadratic Forms 110

Appendix 2. Hermitian Forms... ．.．..114

Appendix 3.The Hass-Minkowski Theorem．..．．..．．.120

![](images/0fe9f4ca69b7df164f84aea71a906b6b9443d7e6fca25e78bf47a905966bd0b6.jpg)

![](images/59b449e494b55c42cd64cd111bc0c358236e73edc0d7689fea35886e05071614.jpg)

This chapter will define the concept of an inner product space over a commutative ring $R$ ，and describe basic constructions which are independent of the ring $R$ .In particular it introduces the Witt ring $W ( R ) _ { : }$ which will play a central role in later chapters.Roughly speaking, $W ( R )$ is the collection of all symmetric inner product spaces $X$ over $R$ modulo the collection of “ split" inner product spaces. The inner product space $X$ is said to be split if $X { = } X _ { 1 } { + } X _ { 2 }$ where the submodules $X _ { 1 }$ and $X _ { 2 }$ are dually paired by the inner product, and $X _ { 1 } \cdot X _ { 1 } { = } 0 .$

# §1.Bilinear Forms and Inner Products

Let $R$ be a commutative ring with 1,and let $X$ be a left $R$ -module.

(1.1) Definition. A bitinear form on $\boldsymbol { \cal X }$ is a function

$$
\beta \colon X \times X \to R
$$

such that $\beta ( x , y )$ is $R$ -linear as a function of $x$ for fixed $y _ { : }$ and $R$ -linear as a function of $y$ for fixed $x$ .Such a bilinear form $\beta$ will be called an inner product on $X$ if the following strong non-degeneracy conditions are satisfied. For each $R$ -linear map

$$
\varphi \colon X \to R
$$

there should exist one and only one element ${ \mathfrak { x } } _ { 0 }$ in $\yen 80$ that the homomorphism $y \mapsto \beta ( x _ { 0 } , y )$

from $X$ to $\textbf {  { R } }$ is equal to $\varphi$ .Furthermore there should exist one and only one $y _ { 0 } \in X$ so that the homomorphism

$$
{ \mathfrak { x } } \mapsto \beta ( x , y _ { 0 } )
$$

is equal to $\varphi$ . In other words the two homomorphisms

$$
x _ { 0 } \mapsto \beta ( x _ { 0 } , ) , ~ y _ { 0 } \mapsto \beta ( { \mathrm { ~ , ~ } } y _ { 0 } )
$$

from X to the dual module ${ \mathrm { H o m } } _ { R } ( X , R )$ should be bijective.

The notation $\beta ( x , y ) = x \cdot y$ will usually be used for an inner product.

If $\beta$ is a bilinear form or inner product on $X$ ,then the pair $( X , \beta )$ is called a bilinear form module or an inner product module over $R$ Two bilinear form modules $( X , \beta )$ and $( X ^ { \prime } , \beta ^ { \prime } )$ are isomorphic if there is an $\overline { { R } }$ -linear bijection $\mathcal { f }$ ：： $X \to X ^ { \prime }$ satisfying $\begin{array} { r } { \beta ^ { \prime } \left( f ( x ) , f ( y ) \right) = \beta ( x , y ) } \end{array}$ for all $x$

![](images/42161930f9a3c268884ff7616265b8aba30a028aca5c5cb8da7a1f4ada72bb60.jpg)

# $\ S 2 .$ Bilinear Forms over a Free Module

If $X$ is a finitely generated free $R$ -module with basis $e _ { 1 } , \ldots , e _ { n }$ ,then the integer $n$ is called the rank or dimension of $X$ ，denoted $\mathbf { r k } ( X )$ . Since $R$ is commutative, the rank is uniquely defined.

If $\overline { { X } }$ has basis $e _ { 1 } , \ldots , e _ { n }$ ，then any bilinear form $\beta$ on $X$ gives rise to an $n \times n$ matrix $\scriptstyle B = ( \beta _ { i j } )$ where

$$
\beta _ { i j } { = } \beta ( e _ { i } , e _ { j } ) .
$$

This matrix determines the bilinear form uniquely, since if $\textstyle { x = \sum } \xi _ { i } e _ { i }$ and $\boldsymbol { y = } \sum \eta _ { j } \boldsymbol { e } _ { j }$ then

$$
\beta ( x , y ) { = } \sum \beta _ { i j } \xi _ { i } \eta _ { j } .
$$

(2.1) Definition. Given any $n \times n$ matrix $B { = } ( \beta _ { i j } )$ with entries in $R$

$$
\langle B \rangle { = } \langle B \rangle _ { R }
$$

will stand for the free bilinear form space over R with basis $e _ { 1 } , \ldots , e _ { n }$ andwith bilinear form $\beta ( e _ { i } , e _ { j } ) { = } \beta _ { i j }$

(2.2)Lemma. This bilinear form is an inner product if and only if the matrixBis invertible(i.e.,has a 2-sidedinverse).

This is clear since the homomorphism x-→β(x, ) from $\overline { { \boldsymbol X } }$ to the dual module ${ \mathrm { H o m } } _ { R } ( X , R ) .$ equipped with the dual basis $e _ { 1 } ^ { * } , \ldots , e _ { n } ^ { * }$ , is given by $e _ { i } \mathrm { { i } } \xrightarrow [ { j } ] { } \beta _ { i j } e _ { j } ^ { * }$ □

Note that the bilinear form space $\langle B \rangle$ is symmetric if and only if $B = B ^ { t }$ ,skew-symmetric if and only if $B ^ { t } { = } - B _ { ; }$ ,and symplectic if and only if the matrix $B$ has zeros along the diagonal and satisfies $B ^ { t } = - B$ (Here $B ^ { t }$ stands, of course, for the transpose of the matrix $B$ ）

Now let us see what happens if we change the basis.

(2.3) Lemma. The bilinear form space $\langle B \rangle$ is isomorphic to <B'>if and onlv if

for some invertible $n \times n$ matrix A.

For if $e _ { 1 } ^ { \prime } , \ldots , e _ { n } ^ { \prime }$ is a new basis, then

$$
e _ { i } ^ { \prime } { = } \alpha _ { i 1 } e _ { 1 } { + } \cdots { + } \alpha _ { i n } e _ { n }
$$

for some invertible matrix $( \alpha _ { i k } ) _ { : }$ ,and it follows that

$$
B ( e _ { i } ^ { \prime } , e _ { j } ^ { \prime } ) { = } \sum { \alpha } _ { i k } \beta _ { k l } { \alpha } _ { j l } ,
$$

The following special case is of particular interest.

(2.4) Example. Let $u$ be any element in the group $R ^ { \bullet }$ consisting of all units in $R$ .Then the symbol $\langle u \rangle$ denotes the symmetric inner product -space having one basis element $e _ { 1 } ,$ where $e _ { 1 } \cdot e _ { 1 } { = } u$ Note that

$$
\langle u \rangle \cong \langle u ^ { \prime } \rangle
$$

if and only if $u ^ { \prime } { = } { \alpha } ^ { 2 } u$ for some $\alpha \in R ^ { \bullet }$ ：

A useful invariant of free inner product spaces is the determinant. Let $R ^ { \bullet 2 }$ denote the subgroup of $R ^ { \bullet }$ consisting of all squares of units.

(2.5) Definition. The determinant of a free inner product space $X$ is the element of the quotient group $R ^ { \bullet } / R ^ { \bullet 2 }$ represented by det $( B ) _ { : }$ ，where $B$ is any matrix with $\langle B \rangle \cong X$

More generally, if $\boldsymbol { X }$ is a free bilinear form module, then det $( X )$ is the element of the quotient monoid $R / R ^ { \bullet 2 }$ represented by det $( B ) _ { : }$ where $B$ is any matrix with $\langle B \rangle \cong X$ . It follows from (2.3) that this determinant is well defined.

We conclude with one more useful and classical construction. Given a basis $e _ { 1 } , \ldots , e _ { n }$ for a fre inerproduct space $X$ , the dual basis $e _ { 1 } ^ { \# } , \ldots , e _ { n } ^ { \# }$ for $X$ is defined by the conditions

and

(2.6) Lemma. To each basis for $a$ free inner product space there corresponds a unique dual basis.

For the matrix $( \beta _ { i j } ) { = } ( e _ { i } \cdot e _ { j } )$ is invertible, with inverse matrix ${ { \left( { \gamma } _ { j k } \right) } }$ The equations

$$
e _ { k } ^ { \mp } = \gamma _ { 1 k } e _ { 1 } + \cdots + \gamma _ { n k } e _ { n }
$$

now yield the required dual basis.□

# S 3. Orthogonal Sums

Let $X _ { 1 } , \ldots , X _ { n }$ be bilinear form modules,with bilinear forms $\beta _ { 1 } , \ldots , \beta _ { n }$ respectively. The orthogonal sum $X _ { 1 } \oplus \cdots \oplus X _ { n }$ is defined to be the direct sum of the modules $X _ { i }$ with bilinear form $\beta$ defined by the equation

$$
\begin{array} { r } { \beta ( x _ { 1 } \oplus \cdots \oplus x _ { n } , y _ { 1 } \oplus \cdots \oplus y _ { n } ) = \sum \beta _ { i } ( x _ { i } , y _ { i } ) } \end{array}
$$

summed over $1 \leq i \leq n .$

Evidently $X _ { 1 } \oplus \cdots \oplus X _ { n }$ is an inner product module (or an inner product space) if and only if each $X _ { i }$ is an inner product module (or an inner product space). If the $X _ { i }$ are free and finitely generated, note that

$$
\mathrm { \bf ~ r k } ( X _ { 1 } \oplus \cdots \oplus X _ { n } ) { \bf = } \sum \mathrm { \bf ~ r k } ( X _ { i } ) ,
$$

$$
\begin{array} { r } { \operatorname* { d e t } ( X _ { 1 } \oplus \cdots \oplus X _ { n } ) { = } \prod \operatorname* { d e t } ( X _ { i } ) . } \end{array}
$$

The following lemma is easy to prove, but extremely important.Let $X$ be a bilinear form module,and $M$ a submodule. We assume that the bilinear form $\beta$ is either symmetric or skew-symmetric, so that $\beta ( x , y ) { = } 0$ implies $\beta ( y , x ) = 0$ ，

(3.1) Orthogonal decomposition lemma. If the bilinear form $\beta$ re-stricted to $M \times M$ is an inner product on $M _ { ; }$ then $X$ is isomorphic to the orthogonal sum $M \oplus M ^ { \perp }$

Here $M ^ { \perp }$ denotes the orthogonal complement, consisting of all xeX such that $\beta ( x , M ) = 0$ ：

Proof. If $m { \in } M \cap M ^ { \bot }$ ，then $\beta ( m , m ^ { \prime } ) { = } 0$ for all $m ^ { \prime } { \in } M _ { \mathrm { { \ell } } }$ ，and therefore $m { = } 0 .$ Thus to prove (3.1) it suffices to show that every $_ x$ in $X$ can be written as a sum m+y with m∈M and y∈M-.

Given ${ \mathbf { { \mathit { x } } } } \in X ,$ consider the linear form $m ^ { \prime } \mapsto \beta ( x , m ^ { \prime } )$ on M. By the definition of inner product, there exists one and only one element m∈M so that

$$
\beta ( m , m ^ { \prime } ) { = } \beta ( x , m ^ { \prime } )
$$

for all $m ^ { \prime }$ .Then $x - m \in M ^ { \bot }$ ,and we have

$$
{ \pmb x } = m + ( { \pmb x } - m )
$$

as required. This completes the proof.

(3.2) Theorem. Let $X$ be a symmetric or skew-symmetric bilinear form module, and let $\overline { { x _ { 1 } , \ldots , x _ { k } } }$ be elements such that the k×k matrix $\left( \beta ( x _ { i } , x _ { j } ) \right)$ is invertible. Then $x _ { 1 } , \ldots , x _ { k }$ are linearly independent, and

$$
X \cong M \oplus M ^ { \perp }
$$

where M denotes the free module spanned by the $x _ { i }$

Proof. Since any relation $\rho _ { 1 } x _ { 1 } + \cdots + \rho _ { k } x _ { k } { = } 0$ would contradict the hypothesis that $\left( \beta ( x _ { i } , x _ { j } ) \right)$ isinvertible, this follows easily from the lemma.

This theorem has many applications. Here are some examples.

(3.3) Corollary. If $X$ is $^ { a }$ finitely generated symmetric bilinear form module, then

$$
X \cong \langle u _ { 1 } \rangle \oplus \dots \oplus \langle u _ { k } \rangle \oplus N
$$

where $\boldsymbol { u } _ { 1 } , \ldots , \boldsymbol { u } _ { k }$ are units, and $\beta ( x , x )$ is a non-unit for every $\mathbf { \boldsymbol { x } } \in N$

For if X contains some element $x _ { 1 }$ such that $\beta ( x _ { 1 } , x _ { 1 } ) { = } u _ { 1 }$ is a unit, then

$$
X \cong ( R x _ { 1 } ) \oplus ( R x _ { 1 } ) ^ { \perp }
$$

by (3.2), where the submodule

$$
R x _ { 1 } \cong \langle u _ { 1 } \rangle
$$

is free. Now apply the same construction to $( R x _ { 1 } ) ^ { \perp }$ ,and continue inductively.

This procedure must terminate after finitely many steps.For suppose that the module X is generated by $_ n$ elements. If the construction continued for more than n steps, we could construct a homomorphism from a free module of rank $n$ onto a free module of rank $n + 1$ Since $R$ is commutative, this is impossible; and this completes the proof.□

If R is a field,it follows that $\beta ( x , x ) = 0$ for every $\mathbf { \boldsymbol { x } } \in N ,$ so that N is symplectic. In fact if $\pmb R$ is a field of characteristic $\neq 2 ,$ then $\beta$ restricted to $\mathcal { N } \times N$ being both symmetric and symplectic must actually be zero. In the case of an inner product, this implies that $N$ itself must be zero. More generally consider a local ring (i.e.,a ring with unique maximal ideal).

(3.4) Corollary. If $R$ is $a$ local ring in which 2 is $a$ unit, then every symmetric inner product space $X$ over $R$ possesses an orthogonal basis.

That is, $X$ possesses a basis $e _ { 1 } , \ldots , e _ { k }$ so that $e _ { i } \cdot e _ { j } { = } 0$ for $i \neq j .$ In other words

$$
X \cong \langle u _ { 1 } \rangle \oplus \dots \oplus \langle u _ { k } \rangle
$$

for suitable units u1,. uk:

Proof of (3.4). Consider the submodule $_ N$ of (3.3). As an orthogonal summand of an inner product space, $\overline { { N } }$ must itself be an inner product space. Suppose that $N$ were non-zero. Since every finitely generated projective over a local ring is free,see [Swan,1968] or [Milnor, Intr. algebr. $K$ -theory],we could choose a basis $e _ { 1 } , \ldots , e _ { n }$ for $N ,$ with $n { \geq } 1$ Let $e _ { 1 } ^ { \# } , \ldots , e _ { n } ^ { \# }$ be the dual basis.Then the computation

$$
\scriptstyle 2 = 2 e _ { 1 } \cdot e _ { 1 } ^ { \# } = ( e _ { 1 } + e _ { 1 } ^ { \# } ) \cdot ( e _ { 1 } + e _ { 1 } ^ { \# } ) - e _ { 1 } \cdot e _ { 1 } - e _ { 1 } ^ { \# } \cdot e _ { 1 } ^ { \# }
$$

would show that 2 belonged to the ideal of non units, contradicting our hypothesis. Thus $N { = } 0 $ ，which completes the proof.□

Here is a final example. Let $X$ be a symplectic inner product space. By a symplectic basis for $X$ we will mean a basis $e _ { 1 } , \ldots , e _ { n }$ such that the associated inner product matrix $( e _ { i } \cdot e _ { j } )$ has the form $\left( \begin{array} { l l } { 0 } & { I } \\ { - I } & { 0 } \end{array} \right)$

(3.5) Corollary. If R is either a Dedekind domain (see p.91 for a definition) or a local ring, then every symplectic inner product space over R is free, and possesses a symplectic basis.

Thus the rank of such a space is always even, and the determinant is always the identity element of $R ^ { \bullet } / R ^ { \bullet 2 }$ .(More generally, for any free symplectic bilinear form space,the determinant in $R / R ^ { \bullet 2 }$ has a canonical square root in $R / R ^ { \bullet }$ called the“Pfaffian" See [Bourbaki, v.24,p.83].)

Proof.We must first construct two elements $x _ { 1 }$ and $x _ { 2 }$ in $X$ so that free,sochoosinga basis $x _ { 1 } \cdot x _ { 2 } { = } 1$ If R is a local ring,then the projective module $e _ { 1 } , \ldots , e _ { n }$ and a dual basis $e _ { 1 } ^ { \# } , \ldots , e _ { n } ^ { \# }$ $X$ is necessarily ,the two vectors $e _ { 1 }$ and $e _ { 1 } ^ { \# }$ will serve.

In the case of a Dedekind ring, a classical theorem of Steinitz² asserts that the projective module $X$ is the direct sum of a free module with basis $e _ { 1 } , \ldots , e _ { n }$ and an ideal ${ \mathfrak { a } } \subset R$ If $n \geq 1 ,$ ,then we can again choose $e _ { 1 } ^ { \# }$ so that $e _ { 1 } \cdot e _ { 1 } ^ { \# } = 1$ Butif $\underline { { n = 0 } }$ then $X { \cong } { \mathfrak { a } } ,$ and a bilinear form $\beta \colon { \mathfrak { a } } \times { \mathfrak { a } } \to R$ which is symplectic must clearly be zero.Hence the case $X { \cong } { \mathfrak { a } } \neq 0$ cannot occur.

Thus if $X { \neq } 0$ there exist elements $x _ { 1 }$ and $x _ { 2 }$ with $x _ { 1 } \cdot x _ { 2 } { = } 1$ The $2 \times 2$ matrix

$$
( x _ { i } \cdot x _ { j } ) { = } \left( \begin{array} { l l } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right)
$$

is evidently invertible, so by (3.2) these two elements span a free orthogonal summand. An easy inductive argument now completes the proof.□

An example of a symplectic inner product space with no symplectic basis will be constructed in Chapter V, \$ 2.

# $\ S$ 4. Witt's Theorem

Let $X$ be a symmetric bilinear form module over the ring $R$ .Suppose that we are given an orthogonal sum decomposition $X = M \oplus N .$

(4.1) Definition. The reflection of $X$ with respect to $( M , N )$ is the linear transformation r: $X \to X$ which leaves $\boldsymbol { M }$ pointwise fixed and carries each point of $\mathcal { N }$ to its negative.

Thus r maps each sum $x = m + n$ in $X$ to $r ( x ) = m - n .$ Evidently $r$ is an involution

$$
r ( r ( x ) ) = x ,
$$

and evidently $r$ preserves the bilinear form,

$$
\left. \beta ( r ( x ) , r ( y ) ) = \beta ( x , y ) \right.
$$

for all $\boldsymbol { x }$ and y. If 2 is a unit in $\pmb R$ ,then conversely it is easy to show that every linear involution preserving the bilinear form on $X$ is a reflection.

(4.2) Lemma. Suppose that $R$ is $a$ local ring in which 2 is $a$ unit. If $x$ and y are elements in the symmetric bilinear form module $X$ such that

$$
\beta ( x , x ) { = } \beta ( y , y )
$$

is a unit of R,then there exists $a$ reflection of $X$ carrying x to y.

Proof. Express $\overline { { x } }$ as the sum of two mutually orthogonal vectors $\scriptstyle u = ( x + y ) / 2$ and $v = ( x - y ) / 2$ .Then

$$
\beta ( x , x ) = \beta ( u , u ) + \beta ( v , v ) .
$$

Since $R$ is local,at least one of the two ring elements $\beta ( u , u )$ and $\beta ( v , v )$ must be a unit. If $\beta ( u , u )$ is a unit, then $X { = } ( R u ) \oplus ( R u ) ^ { \perp }$ ,and the reflection with respect to $( ( R u ) , ( R u ) ^ { \perp } )$ carries $\textbf { \em u }$ + $v = x$ to $\scriptstyle u - v = y$ Similarly， if $\beta ( v , v )$ is a unit, then reflection with respect to $( ( R v ) ^ { \perp } , ( R v ) )$ carries $\boldsymbol { x }$ to y. This completes the proof.

(4.3) Corollary. With $R$ as above, if $X$ is $a$ symmetric inner product space of rank n over $R$ ,then every automorphism $f$ of $X$ can be expressed as the composition of n reflections.

Proof by induction. By (3.4) there exists an orthogonal basis $e _ { 1 } , \ldots , e _ { n }$ for $X$ .Choose a reflection $r _ { 1 }$ carrying $f ( e _ { 1 } )$ to $e _ { 1 }$ . Then $r _ { 1 } f$ fixes $e _ { 1 }$ and hence carries the space $( R e _ { 1 } ) ^ { \perp }$ of rank $\overline { { n - 1 } }$ to itself. Therefore $\overline { { r _ { 1 } f } }$ restricted to $( R e _ { 1 } ) ^ { \perp }$ is a composition $r _ { 2 } \ldots r _ { n }$ of reflections. Extending each $\underline { { r _ { i } } }$ to $\overline { { X } }$ by setting $\underline { { r _ { i } ( e _ { 1 } ) } } = e _ { 1 }$ for $i > 1$ we have $\overline { { f = r _ { 1 } \ldots r _ { n } } }$ asrequired.

Another corollary, more important for our purposes, is the following. We continue to assume that $R$ is a local ring in which 2 is a unit.

(4.4) Witt's theorem. Let $X$ Y $Z$ be inner product spaces over R. If $X \oplus Y \cong X \oplus Z$ ,then $Y \cong Z$

Proof. Since $X$ is an orthogonal sum of rank 1 spaces by (3.4), it suffices to prove this theorem when $X$ is free of rank 1.Let e be a basis element for $X$ ,and let

be an arbitrary isomorphism. To avoid confusion, let $0 _ { X } , ~ 0 _ { Y }$ ，and $0 _ { z }$ denote the zero elements in $X , ~ Y$ and $Z$ respectively. Then the two elements $f ( e \oplus 0 _ { Y } )$ and $e \oplus 0 _ { z }$ of $X \oplus Z$ satisfy the hypothesis of (4.2), so there exists a reflection $r$ of $X \oplus Z$ carrying $f ( e \oplus 0 _ { Y } )$ to $e \oplus 0 _ { z }$ . Now the isomorphism

$$
r f \colon X \oplus Y \to X \oplus Z
$$

carries $e \oplus 0 _ { \scriptscriptstyle { Y } } \mathrm { t o } e \oplus 0 _ { z }$ ， and hence carries the orthogonal complement $0 _ { X } \oplus Y$ isomorphically to $0 _ { X } \oplus Z$ .This completes the proof.□

Note that Witt's theorem is definitely false when 2 is a non-unit in $R$ .To prove this, start with the isomorphism

$$
\langle - 1 \rangle \oplus \langle - 1 \rangle \oplus \langle 1 \rangle \cong \langle - 1 \rangle \oplus H ,
$$

where H denotes the hyperbolic plane, free of rank 2 with inner product matrix $\frac { 7 0 \quad 1 } { 1 \quad 0 }$ In fact if $e _ { 1 } , e _ { 2 } , e _ { 3 }$ are orthogonal vectors with $e _ { 1 } \cdot e _ { 1 } =$

$e _ { 2 } \cdot e _ { 2 } = - 1$ and $e _ { 3 } \cdot e _ { 3 } { = } 1$ ,then the three vectors

$$
e _ { 1 } + e _ { 2 } + e _ { 3 } , e _ { 1 } + e _ { 3 } , e _ { 2 } + e _ { 3 }
$$

form a new basis, with inner product matrix

But if 2 is a non-unit, then

$$
\langle - 1 \rangle \oplus \langle 1 \rangle \not \cong H ,
$$

since every $h \in H$ clearly satisfies

(Compare the discussion in Chapter V, \$ 1.)

It is interesting to note that Witt's theorem remains true for quadratic forms over a field of characteristic 2; see Appendix 1.

# S 5.Tensor Products and Exterior Powers

Let $X _ { 1 } , . . . , X _ { n }$ be bilinear form modules over $R ,$ with bilinear forms $\beta _ { 1 } , \ldots , \beta _ { n }$ respectively. Then the tensor product $X _ { 1 } \otimes \cdots \otimes X _ { n }$ Over R can be made into a bilinear form module as follows.

(5.1) Lemma. There is one and only one bilinear form $\beta$ on $X _ { 1 } \otimes \cdots \otimes X _ { n }$ which satisfies the identity.

$$
\beta ( x _ { 1 } \otimes \cdots \otimes x _ { n } , y _ { 1 } \otimes \cdots \otimes y _ { n } ) { \stackrel { } { = } } \prod _ { i = 1 } ^ { n } \beta _ { i } ( x _ { i } , y _ { i } )
$$

for all $x _ { i }$ and yiin X,1≤i≤n.

Proof. The 2n-linear function

$$
( x _ { 1 } , . . . , x _ { n } , y _ { 1 } , . . . , y _ { n } ) { \mapsto } \beta _ { 1 } ( x _ { 1 } , y _ { 1 } ) . . . \beta _ { n } ( x _ { n } , y _ { n } )
$$

from $X _ { 1 } \times \cdots \times X _ { n } \times X _ { 1 } \times \cdots \times X _ { n }$ to $R$ gives rise to an associated linear function

$$
X _ { 1 } \otimes \cdots \otimes X _ { n } \otimes X _ { 1 } \otimes \cdots \otimes X _ { n } { \longrightarrow } R .
$$

Composing with the canonical bilinear function

$$
( X _ { 1 } \otimes \cdots \otimes X _ { n } ) \times ( X _ { 1 } \otimes \cdots \otimes X _ { n } ) { \longrightarrow } X _ { 1 } \otimes \cdots \otimes X _ { n } \otimes X _ { 1 } \otimes \cdots \otimes X _ { n } ,
$$

we obtain the required bilinear form $\beta$ □

(5.2) Remark. If each $X _ { i }$ is symmetric, then the tensor product is clearly symmetric. More generally, if each $X _ { i }$ is $\varepsilon _ { i }$ -symmetric (where 1-symmetric means symmetric and $( - 1 )$ -symmetric means skewsymmetric), then the tensor product $X _ { 1 } \otimes \cdots \otimes X _ { n }$ is $( \varepsilon _ { 1 } . . . \varepsilon _ { n } )$ -symmetric. Similarly, if $X _ { 1 }$ is symmetric and $X _ { 2 }$ is sympleetie, then $X _ { 1 } \otimes X _ { 2 }$ is symplectic.

Now let us suppose that each $X _ { i }$ is an inner product space.

(5.3) Lemma. If $X _ { 1 } , . . . , X _ { n }$ are inner product spaces over $R$ ，then $X _ { 1 } \otimes \cdots \otimes X _ { n }$ is an inner product space over $R$

Proof. Since each module $X _ { i }$ is a direct summand of a finitely generated free $R$ -module, it follows easily that the tensor product $X _ { 1 } \otimes \cdots \otimes X _ { n }$ is a direct summand of a finitely generated free $R$ -module. Let $X ^ { * }$ denote the module Hom $( X , R )$ dual to X. Each inner product $\beta _ { i }$ gives rise to an associated bijection

$$
{ \bar { \beta } } _ { i } \colon X _ { i } \to X _ { i } ^ { * } ,
$$

where $\bar { \beta } _ { i } ( x ) ( y ) { = } \beta _ { i } ( x , y )$ .The homomorphism

$$
\bar { \beta } \colon X _ { 1 } \otimes \cdots \otimes X _ { n } { \longrightarrow } ( X _ { 1 } \otimes \cdots \otimes X _ { n } ) ^ { * }
$$

associated with our bilinear form $\beta _ { : }$ ，can be expressed as a composition

$$
\bar { \beta } { = } \eta \circ ( \bar { \beta } _ { 1 } \otimes \cdots \otimes \bar { \beta } _ { n } )
$$

where n is the homomorphism from $X _ { 1 } ^ { * } \otimes \cdots \otimes X _ { n } ^ { * }$ to $( X _ { 1 } \otimes \cdots \otimes X _ { n } ) ^ { * }$ which maps each generator $f _ { 1 } \otimes \cdots \otimes f _ { n }$ to the homomorphism X1@·-@xn→

$f ( x _ { 1 } ) \ldots f ( x _ { n } ) .$ But each $X _ { i }$ is finitely generated and projective,so it is easy to check that $\eta$ is an isomorphism. This completes the proof.

In this lemma the hypothesis that the $X _ { i }$ are projective is essential. (For a counter-example in the non-projective case, consider modules of -order 3 over $\mathbf { Z } / 9 \mathbf { Z } . )$

As examples of this tensor product operation, note that

$$
\overline { { \langle u \rangle \otimes \langle v \rangle \cong \langle u v \rangle } }
$$

for any $u$ and $v$ in $R ^ { \bullet }$ ,and that

$$
\langle 1 \rangle \otimes X { \cong } X
$$

for any $X$ If $X$ and $Y$ are free modules, note that

$$
\operatorname { r k } { ( X \otimes Y ) } { = } \operatorname { r k } { ( X ) } \operatorname { r k } { ( Y ) } .
$$

The tensor product operation will play a very important role in subsequent sections. In particular, it is used to provide the product operation in the Witt ring (S7)./Here is a related construction which will also play an important role.

(5.4) Change of rings. Let $f \colon R \to R ^ { \prime }$ be a ring homomorphism. Then any inner product space $X$ over $R$ gives rise to an inner product space

$$
f _ { \# } ( X ) { = } R _ { \# } ^ { \prime } X
$$

over the ring $R ^ { \prime }$ ,the inner product on $f _ { \# } ( X )$ being defined by the formula

$$
( \alpha \otimes x ) \cdot ( \beta \otimes y ) { \stackrel { } { = } } \alpha \beta f ( x \cdot y ) .
$$

As an example, if $X$ is free over $R$ with basis $e _ { 1 } , \ldots , e _ { n }$ and inner product matrix $( e _ { i } \cdot e _ { j } ) _ { }$ then $f _ { \# } ( X )$ is free over $R ^ { \prime }$ with basis $1 \otimes e _ { 1 } , \ldots , 1 \otimes e _ { n }$ and inner product matrix $\left( f ( e _ { i } \cdot e _ { j } ) \right)$ .The correspondence $X \mapsto f _ { \# } ( X )$ preserves orthogonal sums and tensor products.

$$
\mathrm { r a n k } ( P ) { \in } \mathbf { Z } ^ { \mathrm { S p e c } ( R ) }
$$

is the function which assigns to each prime ideal p the dimension of the   
vector space $F _ { \otimes P } { \otimes } P ,$ where ${ \bf \nabla } ^ { F }$ is the quotient field of $\mathbf { \mathcal { R } } / \mathbf { \bar { p } }$ . This coincides R   
with our previous definition whenever $P$ is free.

(5.6) Exterior powers. If $X$ is a bilinear form module over $R _ { ; }$ ，then the exterior power $\wedge ^ { k } X$ over $R$ possesses a unique bilinear form $\hat { \beta }$ satisfying the identity

$$
\widehat { \beta } ( x _ { 1 } \wedge \ldots \wedge x _ { k } , y _ { 1 } \wedge \ldots \wedge y _ { k } ) = { \tt d e t } ( \beta ( x _ { i } , y _ { j } ) ) .
$$

See [Bourbaki, $2 4 , \mathsf { p } . 3 0 ]$ If X is ε-symmetric,then $\triangle ^ { k } X$ is $\varepsilon ^ { k } .$ -symmetric.   
If X is an inner product space, then $\triangle ^ { k } X$ is also an inner product space.

(5.7) The determinant. Let $X$ be a bilinear form space over $R$ whose underlying projective module has rank $n$ at every prime ideal. Then the bilinear form space $\textstyle { \bigwedge } ^ { n } X$ of rank 1 is called the“determinant”of $X$ Compare [Knebusch, $1 9 6 9 / 7 0 ]$ . This subsumes our previous concept of determinant, since if $X$ is free with basis $e _ { 1 } , \ldots , e _ { n }$ ,then $\wedge ^ { n } X$ is free with basis $e { = } e _ { 1 } \wedge \ldots \wedge e _ { n }$ , and hence

where the element

$$
d _ { 0 } = \hat { \beta } ( e , e ) = \operatorname * { d e t } \left( \beta ( e _ { i } , e _ { j } ) \right)
$$

is well defined up to multiplication by squares of units.

An illustration of this concept of “determinant” willbe given in Chapter V, \$ 3.

# 6. Split Inner Product Spaces

(6.1) Definition. A symmetric inner product space $s$ over the ring $R$ is split if there exists a submodule $N { \subset } S $ ,such that $N$ is a direct summand of S,and such that $N$ is precisely equal to its orthogonal complement $N ^ { \perp }$

This concept is due to Knebusch, who uses the term“metabolic”in place of our“split".

An equivalent form of the definition would be the following. The space S is split if it is the direct sum of two submodules M, $\overline { { N } }$ which are dually paired to $R$ by the inner product,

$$
{ \cal M } \stackrel { \cong } { \longrightarrow } \mathrm { H o m } _ { R } ( N , R ) , ~ N { \stackrel { \cong } { \longrightarrow } } \mathrm { H o m } _ { R } ( M , R ) ,
$$

and such that $N$ is self-orthogonal, $N \cdot N { = } 0$ [Still another formulation would be that $s$ is split if it contains a self-orthogonal direct summand $N$ whose rank,in the sense of $\ S 5 . 5 .$ , is equal to $\textstyle { \frac { 1 } { 2 } }$ rank (S).]

Here are two examples. The hyperbolic plane, with inner product matrix 10 is clearly split. Furthermore, for any unit ${ \underline { { \boldsymbol { u } } } } .$ the orthois split. For if $e _ { 1 } , e _ { 2 }$ is an orthogonal basis with inner product matrix $\left( { \begin{array} { c c } { u } & { 0 } \\ { 0 } & { - u } \end{array} } \right)$ , then the element $e _ { 1 } + e _ { 2 }$ spans the required irect summand $N$ with $N = N ^ { \perp }$

(6.2) Lemma. Let S and $\pmb { S } ^ { \prime }$ be split inner product spaces, and let $X = ( X , \beta )$ be an arbitrary inner product space. Then the orthogonal sum SS' is split, and the tensor product $S \otimes X$ is split.Furthermore the orthogonal sum

$$
( X , \beta ) \oplus ( X , - \beta )
$$

is split.

Proofs of the first two assertions are easily supplied. To prove the third, we use the split inner product space $\langle 1 \rangle \oplus \langle - 1 \rangle$ to conclude that the tensor product

$$
\displaystyle \begin{array} { r l } & { \frac { ( \langle 1 \rangle \oplus \langle - 1 \rangle ) \otimes ( X , \beta ) \cong \left( \langle 1 \rangle \otimes ( X , \beta ) \right) \oplus \left( \langle - 1 \rangle \otimes ( X , \beta ) \right) } { \mathrm { ~ a ~ n ~ } } } \\ & { \frac { \mathrm { ~ p l i t . ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } } { \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } } } \end{array}
$$

is also

In special cases we can give a more precise description of split spaces.

(6.3) Lemma. Let R be a ring such that every finitely generated projective over R is free. Then an inner product space over R is split if and only if it possesses a basis so that the associated inner product matrix has theform().Ifweasoasuetat2sunit,teneverysplitier product space has matrix $\binom { 0 } { I } \binom { I } { 0 }$ with respect to a suitble basis.

Thus every split space is isomorphic to an orthogonal sum of hyperbolic planes,when all of the hypotheses of (6.3) are satisfied. This is the case when $R$ is a field of characteristic ≠2.

Proof. Given any direct summand $N \subset X$ ,choose a basis basis. Then clearly for $\underline { { N } } ,$ and extend to a basis $e _ { n + 1 } ^ { \# } , \ldots , e _ { k } ^ { \# }$ $e _ { 1 } , \ldots , e _ { k }$ forbasis fortherogoalco for $X$ Let $e _ { 1 } ^ { \# } , \ldots , e _ { k } ^ { \# }$ be the dual plement $N ^ { \perp }$

Suppose that $N = N ^ { \perp }$ . Then substituting $e _ { 1 } , \ldots , e _ { n }$ for $e _ { n + 1 } ^ { \# } , \ldots , e _ { k } ^ { \# }$ we see that the elements

$$
e _ { 1 } , \ldots , e _ { n } , e _ { 1 } ^ { \# } , \ldots , e _ { n } ^ { \# }
$$

form a basis for $X$ . (In particular the rank $k$ of $X$ must be equal to $2 n .$ ） The inner product matrix of $X$ with respect to this new basis takes the 10 1 form (1 A)for some symmetric matrix $\boldsymbol { A }$ .The converse is clear.

Now suppose that 2 is a unit in $R$ Setting $\begin{array} { r } { B = - \frac { 1 } { 2 } \mathbf { A } , } \end{array}$ ，computation shows that

$$
\left( { \begin{array} { c c } { I } & { 0 } \\ { B } & { I } \end{array} } \right) \left( { \begin{array} { c c } { 0 } & { I } \\ { I } & { A } \end{array} } \right) \left( { \begin{array} { c c } { I } & { 0 } \\ { B } & { I } \end{array} } \right) ^ { t } = \left( { \begin{array} { c c } { 0 } & { I } \\ { I } & { 0 } \end{array} } \right) .
$$

This completes the proof.0

# \$7. The Witt Ring

Following Knebusch,we bring some order into the collection of all inner product spaces over $R$ by introducing an equivalence relation. (See also [Frohlich-McEvett].)

(7.1) Definition. Two symmetric inner product spaces $X$ and $X ^ { \prime }$   
over $R$ belong to the same Witt class, written $X { \sim } X ^ { \prime }$ ，if there exist split   
inner product spaces S and S' so that $X \oplus S$ is isomorphic to $X ^ { \prime } \oplus S ^ { \prime }$ Evidently this is an equivalence relation.Furthermore:

(7.2) Lemma. If $X { \sim } X ^ { \prime }$ and $Y { \sim } Y ^ { \prime }$ ,then $X \oplus Y { \sim } X ^ { \prime } \oplus Y ^ { \prime }$ and $X \otimes Y \sim$ $X ^ { \prime } { \otimes } Y ^ { \prime }$

Proof. These statements follow easily from (6.2).

Now recalling that $( X , \beta ) \oplus ( X , - \beta ) { \sim } 0 \operatorname { a n d } \langle 1 \rangle \otimes X { \cong } X ,$ we evidentlyobtain the following.

(7.3) Theorem. The collection $W ( R )$ of all Witt classes of symmetric inner product spaces over $R$ forms $a$ commutative ring with 1,using the orthogonal sum as addition operation and the tensor product as multiplication operation.

Following Knebusch, $W ( R )$ is called the Witt ring of R.Using (5.4) we see that any ring homomorphism $R \to R ^ { \prime }$ induces a ring homomorphism $W ( R ) \to W ( R ^ { \prime } ) .$ We will investigate the structure of this ring $W ( R )$ in subsequent chapters.

Note the following.

(7.4) Lemma. If $R$ is a local ring in which 2 is a unit,then two symmetric inner product spaces over R are isomorphic if and only if they belong to the same Witt class and have the same rank.

Proof. This follows easily from (4.4) and (6.3).□

# Chapter II. Symmetric Inner Product Spaces over Z

This chapter will discuss the classification problem for inner product spaces over the ring $\mathbf { Z }$ of rational integers. All inner products are to be symmetric. Our presentation is based on the classical theorem of Minkowski concerning lattice points in a convex symmetric subset of $\mathbf { R } ^ { n }$ .This theorem is first used to classify inner product spaces of rank $\leq 4$ over Z. Making use of the Hasse-Minkowski theorem (which we do not prove), it is shown that an indefinite inner product space over Z is completely determined by its rank, type, and signature; where the type is defined to be either I or $H$ according as the space does or does not contain a vector of odd norm. It follows that the Wit ring $W ( \mathbf { Z } )$ is isomorphic to Z.

The classification problem for positive definite inner product spaces, on the other hand, is extraordinarily difficult. After a discussion of this problem, and the related problem of close packing of balls in euclidean space,we present the classical characterization of sums of two or four squares in Z. The chapter concludes with an outline of Siegel’s work on positive definite bilinear forms over Z.

# \$1.Minkowski's Convex Body Theorem

Let $\mathbf { R } ^ { n }$ be the cartesian space consisting of all $\boldsymbol { n }$ -tuples ${ \mathfrak { x } } = ( x _ { 1 } , \ldots , x _ { n } )$ of real numbers, and provided with the standard Lebesgue measure $\overline { { d { x _ { 1 } } . . . d { x _ { n } } } }$ ：

(1.1) Definition. A lattice in $\mathbf { \mathbf { R } } ^ { n }$ is an additive subgroup $L { \bf C } { \bf R } ^ { n }$ which is additively generated by some basis $\boldsymbol { b } _ { 1 } , \ldots , \boldsymbol { b } _ { n }$ for the real vector space $\mathbf { R } ^ { n }$

$\mathrm { ~ \ , ~ }$ Choosing some basis $b _ { 1 } , \ldots , b _ { n }$ for $L _ { ; }$ ，we can form the fundamental domain $P$ consisting of all $\xi _ { 1 } b _ { 1 } + \cdots + \xi _ { n } b _ { n }$ with $0 \leq \xi _ { i } < 1$ . Clearly every point of $\mathbf { R } ^ { n }$ is congruent modulo $L$ to one and only one point of $P .$ The volume (or Lebesgue measure)

can be identified with the volume of the quotient torus $\mathbb { R } ^ { n } / L$ . This volume is of course equal to the absolute value of the determinant of the matrix whose rows are $b _ { 1 } , \ldots , b _ { n }$ . (See for example [Birkhof-MacLane].） We write this briefly as

$$
\operatorname { v o l } ( \mathbf { R } ^ { n } / L ) { = } | \operatorname* { d e t } ( b _ { 1 } , . . . , b _ { n } ) | .
$$

A lattice is called unimodular if $\mathbb { R } ^ { n } / L$ has volume 1.

(1.2) Examples. Clearly $\mathbf { Z } ^ { n } { \subset } \mathbf { R } ^ { n }$ is a lattice with $\operatorname { v o l } ( \mathbf { R } ^ { n } / \mathbf { Z } ^ { n } ) = 1$ If $L$ and $L ^ { \prime }$ are lattices with $L \supset L ^ { \prime }$ ,then clearly the index $| L / L ^ { \prime } |$ is finite and

$$
\operatorname { v o l } \left( \mathbf { R } ^ { n } / L ^ { \prime } \right) { \bmod { \left( \mathbf { R } ^ { n } / L \right) } } \left| L / L ^ { \prime } \right| .
$$

If we think of $\mathbf { R } ^ { n }$ as a euclidean inner product space, with inner product $x \cdot y { } { } = \sum { x _ { i } } y _ { i }$ ，then the volume $| \mathsf { d e t } ( b _ { 1 } , . . . , b _ { n } ) |$ can also be written as ${ \sqrt { \operatorname* { d e t } ( b _ { i } \cdot b _ { j } ) } } { = } { \sqrt { \operatorname* { d e t } L } } .$ Note that any inner product space $X$ over $\mathbf { Z }$ embeds canonically as a lattice in the real inner product space $\mathbf { R } \otimes X$ .If $\boldsymbol { X }$ is positive definite (that is if ${ \overline { { x \cdot x } } } { \overline { { 0 } } }$ for $\mathbf { \nabla } \overline { { \boldsymbol { x } + \boldsymbol { 0 } } }$ ，then $\mathbf { R } \otimes X$ must be isomorphic to the euclidean space $\mathbf { \Delta } \mathbf { R } ^ { n }$ ,and $X$ corresponds to a unimodular lattice in $\mathbf { R } ^ { n }$

Recall that a subset $K \subset \mathbf { \mathbb { R } } ^ { n }$ is convex if x, $\boldsymbol { x ^ { \prime } } { \in } K$ implies that $\lambda { \boldsymbol { x } } +$ $( 1 - \lambda ) { x ^ { \prime } } \in K$ for all real numbers λ in the interval $\mathbf { 0 } \leq \lambda \leq 1$ . A subset $\kappa$ of R" is symmetric about 0, if x∈ K implies -x∈ K.

(1.3) Minkowski's theorem. Let K be $\mathbf { \delta } \mathbf { \overline { { \alpha } } } \mathbf { \overline { { \alpha } } } \mathbf { \overline { { \alpha } } } $ convex subset of $\mathbf { R } ^ { n }$ which is symmetric about O. If the volume (or Lebesgue measure) of $\kappa$ is greater than $2 ^ { n }$ times the volume of $a$ fundamental domain for $L$ ,then $K$ contains a non-zero lattice point.

Proof. The subset $K ^ { \prime }$ consisting of all $\textstyle { \frac { 1 } { 2 } } x$ with $\boldsymbol { x } \in K$ clearly satisfies

$$
\operatorname { v o l } ( K ^ { \prime } ) > \operatorname { v o l } \left( \mathbf { R } ^ { n } / L \right) .
$$

Hence the canonical map $K ^ { \prime } {  } \mathbb { R } ^ { n } / L ,$ which is locally a volume preserving embedding, cannot be one-to-one. There must exist two distinct points say $\textstyle { \frac { 1 } { 2 } } x$ and $\textstyle { \frac { 1 } { 2 } }$ yin $\pmb { K } ^ { \prime }$ with the same image in $\mathbf { R } ^ { n } / L$ ; so that

$$
0 \neq { \frac { 1 } { 2 } } x - { \frac { 1 } { 2 } } y \in L .
$$

But $\scriptstyle { \frac { 1 } { 2 } } ( x - y )$ is the midpoint of two points $x$ and $- y$ of $K$ ,and hence itself belongs to $K$ .This completes the proof.□

Example.Let $D ( r )$ denote the closed euclidean disk of radius $r$ in $\mathbf { R } ^ { n }$ Then the volume of $D ( r )$ is equal to $\omega _ { n } r ^ { n }$ where the numbers

$$
\stackrel { \_ } { \_ } { \_ } { \_ } = 2 , \omega _ { 2 } = \pi , . \omega _ { 3 } = \frac { 4 } { 3 } \pi , \omega _ { 4 } = \frac { \pi ^ { 2 } } { 2 } , \ldots
$$

can be computed inductively by the formula

$$
\omega _ { n } = \intop _ { 0 } ^ { 2 \pi } \intop _ { 0 } ^ { 1 } \omega _ { n - 2 } ( \sqrt { 1 - r ^ { 2 } } ) ^ { n - 2 } r d r d \theta { = } 2 \pi \omega _ { n - 2 } / n .
$$

It follows that $\overline { { \omega _ { n } = \pi ^ { n / 2 } / ( n / 2 ) ! } }$ for even values of n.(In terms of the gamma function, we have $\omega _ { n } { = } \pi ^ { n / 2 } / \Gamma ( 1 { + } \textstyle { \frac { 1 } { 2 } } n )$ for all values of n.） Applying Minkowski's theorem to $D ( r ) ,$ we obtain the following.

(1.4) Corollary. If $r ^ { n } \geq \left( 2 ^ { n } / \omega _ { n } \right) \mathrm { v o l } ( \mathbf { R } ^ { n } / L ) .$ then the disk $D ( r )$ contains $a$ non-zero lattice point.

Proof. If $r ^ { n }$ is strictly larger than $( 2 ^ { n } / \omega _ { n } ) \mathrm { v o l } ( \mathbf { R } ^ { n } / L ) .$ ,this follows immediately. If equality holds, we simply note that $D ( r + \varepsilon )$ contains a non-zero lattice point for every $\varepsilon > 0$ .But the compact set $D ( r + \varepsilon )$ can contain only finitely many non-zero lattice points, so the closest one to the origin must lie in $D ( r )$ □

Setting $\underline { { r _ { 0 } } }$ precisely equal to the n-th root of $( 2 ^ { n } / \omega _ { n } ) \mathrm { v o l } ( \mathbf { R } ^ { n } / L ) .$ this yields the following.

(1.5) Corollary. Every lattce $L \subset \mathbf { \mathbf { \mathbf { R } } } ^ { n }$ contains $a$ point $( x _ { 1 } , \ldots , x _ { n } )$ with

$$
\begin{array} { r } { 0 < x _ { 1 } ^ { 2 } + \cdots + x _ { n } ^ { 2 } \le r _ { 0 } ^ { 2 } = 4 ( \omega _ { n } ^ { - 1 } \operatorname { v o l } ( \mathbf { R } ^ { n } / L ) ) ^ { 2 / n } . } \end{array}
$$

In particular every unimodular lattice in $\mathbf { R } ^ { n }$ contains $a$ point with

$$
\overline { { 0 < x _ { 1 } ^ { 2 } + \cdots + x _ { n } ^ { 2 } \leq 4 / ( \omega _ { n } ) ^ { 2 / n } } } .
$$

By Stirling's formula, this upper bound $4 / ( \omega _ { n } ) ^ { 2 / n }$ is asymptotic to $2 n / \pi e$ as $n \to \infty$ . (Compare $\ S 7 .$ )Here is a table listing values of $4 / ( \omega _ { n } ) ^ { 2 / n }$ rounded to the nearest hundredth.

![](images/a383fcd40791b48113921f0a1c54a92c0d11d96528bd98d5c9e86b1dfb31121d.jpg)

Note in particular that $4 / ( \omega _ { n } ) ^ { 2 / n } < 2$ whenever n≤4.

Remark. More generally,for any positive integer $\pmb { n }$ one has the estimate

$$
4 / ( \omega _ { n } ) ^ { 2 / n } < 1 + { \textstyle \frac { 1 } { 4 } } n .
$$

For $n < 1 2$ this can be verified by inspecting the table, and for $n { \geq } 1 2$ it can be proved as follows.Setting $A _ { n } { = } ( 1 + \textstyle { \frac { 1 } { 4 } } n ) ^ { n / 2 } \omega _ { n } / 2 ^ { n }$ andsetting $\scriptstyle n = 2 u - 2 ,$ we have

$$
\overline { { { \underline { { A _ { n } / A _ { n - 2 } } } } = { \frac { \pi } { 8 } } { \frac { u ^ { 2 } } { u ^ { 2 } - 1 } } \left( 1 + { \frac { 1 } { u } } \right) ^ { u } } }
$$

where the expression ${ \frac { \pi } { 8 } } \left( 1 + { \frac { 1 } { u } } \right) ^ { u }$ is monotone increasing for $u \geq 2$ and greater than 1 for $u = 7$ .It follows inductively that $A _ { n } > A _ { n - 2 } > 1$ for $n { \geq } 1 2$ □

We will describe some non-trivial examples in $\ S 6$ ； and describe a sharper upper bound for the number

$$
\operatorname* { m i n } _ { x \in L \atop x \neq 0 } ( x _ { 1 } ^ { 2 } + \cdots + x _ { n } ^ { 2 } )
$$

in $\ S 7$

Here is an important qualitative result which follows from (1.5).

(1.6) Lemma (Eisenstein,Hermite). For each integer n there exist only finitely many distinct isomorphism classes of positive definite inner product spaces of rank n over Z.

In fact, given positive integers n and d, there exist only finitely many distinct positive definite bilinear form spaces over Z with rank n and determinant d. (Compare $\ S 7 . 4 . )$ The proof, by induction on n, can be outlined as follows.Clearly any such space can be embedded isometrically as a lattice $L \subset \mathbf { \mathbf { R } } ^ { n } .$ ， where R" has the euclidean inner product. The volume of a fundamental domain for $L$ will be $\overline { { d } }$ .Using (1.5), there is a constant $c ( n , d ) { = } 4 \sqrt [ n ] { d / \omega _ { n } ^ { 2 } } \ \mathrm { s o }$ that every such lattice $\scriptstyle { \pmb { L } }$ contains a vector $_ { x }$ with

Let $L _ { 0 }$ be the sublattice, of index at most $x \cdot x ,$ ,consisting of all $y \in L$ with

$$
x \cdot y { \equiv } 0 \mod x \cdot x .
$$

Then $L _ { 0 }$ decomposes as the orthogonal sum of the subgroup spanned by $x ,$ and its orthogonal complement.Using the induction hypothesis, there exist only finitely many possibilities for $L _ { 0 } ,$ up to isomorphism. Hence there exist only finitely many possibilities for $\scriptstyle L$

A similar argument can be given for indefinite bilinear forms.

# § 2. Inner Product Spaces of Rank $\leq 4$ over Z

(2.1) Lemma. If $L$ is an inner product space of rank n over Z, then $L$ contains a vector $x \neq 0$ with

In particular,if $n { \le } 4$ then L contains a vector x=O with |x· xl<2.

Proof. Note that $L$ embeds isometrically as a lattice in the real inner product space $\mathbf { R } \otimes L$ If $L$ is positive definite, then we can identify $\mathbf { R } \otimes L$ with euclidean $n$ -space,and apply (1.5) directly. In any case, it is possible to choose an orthogonal basis $e _ { 1 } , \ldots , e _ { n }$ for $\mathbf { \delta } \mathbf { \mathcal { R } } \otimes L$ so that $e _ { i } \cdot e _ { i } { = \pm 1 }$ Using this basis to identify $\mathbf { R } \otimes L$ with the cartesian space $\mathbf { R } ^ { n }$ ,and to introduce the volume element $\operatorname { d } x _ { 1 } . . . d x _ { n }$ ，note that the volume of （24号 $( { \pmb { \mathrm { R } } } \otimes { \cal L } ) / L$ is equal to 1. For if $b _ { 1 } , \ldots , b _ { n }$ is a basis for $L ,$ then the matrix equation

$$
( b _ { i } \cdot b _ { j } ) = \left( \begin{array} { c } { { b _ { 1 } } } \\ { { \cdot } } \\ { { \cdot } } \\ { { b _ { n } } } \end{array} \right) \left( \begin{array} { c } { { \pm 1 } } \\ { { \cdot } } \\ { { \cdot } } \\ { { \phantom { - } } } \\ { { \phantom { - } } } \end{array} \right) ( b _ { 1 } ^ { t } \ldots b _ { n } ^ { t } )
$$

implies that det $( b _ { i } \cdot b _ { j } ) = \pm 1$ is equal to $\pm \mathsf { d e t } ( b _ { 1 } , \ldots , b _ { n } ) ^ { 2 }$

Therefore,by(1.5), thereexistsalatticeelement $\scriptstyle \mathbf { x } = x _ { 1 } e _ { 1 } + \cdots + x _ { n } e _ { n } \neq 0$ with $\displaystyle { x _ { 1 } ^ { 2 } + \dots + x _ { n } ^ { 2 } \leq 4 / ( \omega _ { n } ) ^ { 2 / n } } .$

Evidently it follows that

$$
| x \cdot x | = | \pm x _ { 1 } ^ { 2 } \pm \cdots \pm x _ { n } ^ { 2 } | \le 4 / ( \omega _ { n } ) ^ { 2 / n } ,
$$

as required. Since it is easy to check that $4 / ( \omega _ { n } ) ^ { 2 / n } < 2 \ \mathrm { f o r } \ n { \stackrel { < } { = } } 4 ,$ this completes the proof.□

(2.2) Theorem. Every inner product space of rank ≤4 over Z either possesses an orthogonal basis, and hence is isomorphic to a sum of copies of <1>and <-1>,or is “hyperbolic",with inner product matrix of the form $\binom { 0 } { I } \binom { I } { 0 } .$

Proof. We argue by induction. The statement is certainly true in the -rank 1 case. Suppose then that the rank is n>1. If we can find a vector $_ { x }$ in $X$ with ${ \mathbf x } \cdot { \mathbf x } = \pm 1$ ，then evidently

If $X ^ { \prime }$ has an orthogonal basis, we are finished; while if $X ^ { \prime }$ is hyperbolic, spanned by $y$ and $z$ with $y \cdot y = z \cdot z = 0 ,$ $y \cdot z = 1 ,$ ，then the vectors $x + y$ ， $x \mp z ,$ and $x + y \mp z$ form the required orthogonal basis.

Suppose on the other hand that we can find a vector $x _ { 1 } \neq 0$ with $x _ { 1 } \cdot x _ { 1 } = 0 .$ . Without loss of generality, we may assume that $x _ { 1 }$ is indivisible, so that $\mathbf { x _ { 1 } }$ forms part of a basis $x _ { 1 } , \ldots , x _ { n }$ for $X$ Let $y _ { 1 } , \ldots , y _ { n }$ be the dual basis. Then the subspace spanned by $\mathbf { x _ { 1 } }$ and $y _ { 1 }$ has an inner product 0 1 matrix of the form 1 a There are two possibilities.

Case 1. If the entry $a = y _ { 1 } \cdot y _ { 1 }$ is even, then the subspace spanned by   
$x _ { 1 }$ and $y _ { 1 }$ is hyperbolic,with a basis $x _ { 1 }$ and $y _ { 1 } - { \textstyle \frac { 1 } { 2 } } a x _ { 1 }$ consisting of self  
orthogonal vectors. The inner product matrix with respect to this new   
basis is $\textstyle { \left[ { \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} } \right] }$ Thus $X$ is isomorphic to an orthogonal sum X'；

and applying the induction hypothesis to $X ^ { \prime }$ the proof is easily completed.

Case 2. If $\scriptstyle a = 2 k + 1$ is odd, then the two vectors

$$
x ^ { \prime } { = } y _ { 1 } { - } k x _ { 1 } , ~ y ^ { \prime } { = } y _ { 1 } { - } ( k { + } 1 ) x _ { 1 }
$$

are mutually orthogonal, with inner product matrix $\displaystyle \int _ { 0 } ^ { 1 } \frac { 0 } { - 1 }$ So again we can split off an orthogonal summand and proceed by induction. Since,by (2.1), there always exists a vector x∈ X with either x $x = \pm 1$ or $\mathbf { \boldsymbol { x } } \cdot \mathbf { \boldsymbol { x } } = \mathbf { 0 }$ ,this completes the proof.□

(2.3) Remark. The statement of (2.2) is actually true for ranks 5,6, and 7 also.It is false for ranks $\geq 8 ,$ as we will see in $\ S 6 .$

# S 3.The Hasse-Minkowski Theorem and Meyer’s Theorem

Next we will invoke a basic theorem of algebraic number theory, which we will not prove. Given an inner product space $X$ over the rational numbers $\mathbf { Q } ,$ ，we want to find a vector $x \neq 0$ with $\boldsymbol { x } \cdot \boldsymbol { x } = 0$ .Choosing an orthogonal basis, so that

$$
X \cong \langle a _ { 1 } \rangle \oplus \cdots \oplus \langle a _ { n } \rangle
$$

we see that this is equivalent to finding a non-trivial solution to the equation

$$
a _ { 1 } \xi _ { 1 } ^ { 2 } + \cdots + a _ { n } \xi _ { n } ^ { 2 } = 0 .
$$

(3.1) Theorem (Hasse-Minkowski). The equation $a _ { 1 } \zeta _ { 1 } ^ { 2 } + \cdots + a _ { n } \zeta _ { n } ^ { 2 } = 0 ,$ with non-zero rational coefficients, has a non-trivial rational solution if and only if(1) it has a non-trivial real solution and(2)for every prime number $p$ it has a non-trivial solution in the field $\mathbf { Q } _ { p }$ of $p$ -adic numbers.

Proofs are given for example in [Borevich-Shafarevich], [O'Meara] and [Serre]. An outline of a proof is given in Appendix 3.

(3.2) Corollary (Meyer's theorem). An indefinite inner product space of rank n≥5 over Q always possesses a vector $x \neq 0$ with x - x equal to 0.

(The word “indefinite” means that the norm $x \cdot x$ takes on both positive and negative values. The restriction $n \geq 5$ is essential. For example the equation $\xi _ { 1 } ^ { 2 } + \xi _ { 2 } ^ { 2 } + \xi _ { 3 } ^ { 2 } - 7 \xi _ { 4 } ^ { 2 }$ has no non-trivial rational solution as can easily be verified by clearing denominators and then reducing modulo 8.)

To prove the corollary from the theorem, we need only show that the

![](images/105a925f16e1c205d3d1c71b386ccd6d36c616b2d928032c31b2456aaac1d7d7.jpg)

Proof of (3.2). Given $a _ { 1 } , . . . , a _ { 5 } { \in } \mathbf { Q } _ { p }$ , we may assume that each $a _ { i }$ is either a $p$ -adic unit or $p$ times a unit. If at least three of the $a _ { i }$ are units, we are finished by (3.4). But otherwise at least three of the $a _ { i }$ are equal to $p$ times a unit,and again it follows from (3.4) that there is a $p$ -adic solution.

The proof for $p { = } 2$ is similar, but one must work modulo 8, since a number must be congruent to 1 modulo 8 in order to guarantee that it is a 2-adic square. We may assume, after permuting the coeficients and multiplying by a constant, that $a _ { 1 } = 1$ that $a _ { 2 }$ and $a _ { 3 }$ are 2-adic units, and that $a _ { 4 }$ and $a _ { 5 }$ are divisible by at most 2. It is then not dificult to check that the congruence

$$
a _ { 2 } \xi _ { 2 } ^ { 2 } + a _ { 3 } \xi _ { 3 } ^ { 2 } + a _ { 4 } \xi _ { 4 } ^ { 2 } + a _ { 5 } \xi _ { 5 } ^ { 2 } \equiv - 1 ( \mathrm { m o d } 
$$

has a solution, and the argument proceeds as above.

# \$ 4. Indefinite Spaces over Z

(4.1) Lemma. Every indefinite inner product space over Z possesses a vector $x \neq 0$ with $\boldsymbol { x } \cdot \boldsymbol { x } = 0$

Proof. If the rank is $\geq 5 ,$ ，this follows from Meyer's_theorem (3.2), while if the rank is $\leq 4$ it follows from (2.2).

Remark. This argument depends of course on the Hasse-Minkowski theorem, which we have not proved.A different and self-contained proof of (4.1) will be given in Chapter IV.

(4.2) Definition. An inner product space over $\mathbf { Z }$ is of type I if it contains a vector $x$ with $x \cdot x$ odd,and of type II if there is no such vector.

Evidently $X$ is of type II if and only if the quadratic function $q ( x ) =$ $\textstyle { \frac { 1 } { 2 } } x \cdot x$ takes values in $\mathbf { Z } .$ Thus the inner product spaces of type I are pre-cisely those which arise from quadratic inner product spaces over $\mathbf { Z }$ (Compare Appendix 1.)

(4.3) Theorem. Every indefinite inner product space of type I over Z possesses an orthogonal basis,and hence is isomorphic to an orthogonal sum of copies of <1> and $\langle - 1 \rangle$

(It follows that such a space is uniquely determined by its rank and signature. Compare the discussion below.)

Proof by induction. The statement is already known for small values of the rank. Choose a vector $x _ { 1 } \neq 0$ with $x _ { 1 } \cdot x _ { 1 } { = } 0 .$ Without loss of generality we may assume that $x _ { \mathrm { { 1 } } }$ is indivisible,and hence forms part of a-basis $x _ { 1 } , \ldots , x _ { n }$ for X. Let $y _ { 1 } , \ldots , y _ { n }$ be the dual basis. Then $x _ { 1 } \cdot y _ { 1 } = 1 .$

By hypothesis, there exists a vector $y$ whose norm $y \cdot y$ is odd. Hence one of the basis vectors $y _ { k }$ must have odd norm. Choose a subspace $X _ { 0 } { \subset } X$ as follows. If $y _ { 1 } \cdot y _ { 1 }$ is odd, let $X _ { 0 }$ be spanned by $x _ { 1 }$ and $y _ { 1 }$ .If $y _ { 1 } \cdot y _ { 1 }$ is even, let $X _ { 0 }$ be spanned by $x _ { 1 }$ and $y _ { 1 } + y _ { k }$ where $k$ is chosen so that

![](images/f7feba893547a6ce420ac8a61f13159ee058d167f8b50d590776a87f82168b5a.jpg)

This homomorphism is surjective since $\sigma \langle 1 \rangle = 1$ . It has kernel zero, since if $\sigma ( X ) { = } 0$ then the sum $X \oplus \langle 1 \rangle \oplus \langle - 1 \rangle$ is isomorphic to a sum of copies of $\left. 1 \right. \oplus \left. - 1 \right.$ by (4.3),and therefore

$$
X { \sim } X \oplus \langle 1 \rangle \oplus \langle - 1 \rangle { \sim } 0 .
$$

Thus two inner product spaces over Z have the same signature if and only if they belong to the same Witt class. Since the identity $\sigma \langle 1 \rangle =$ 1 implies that the bijection $W ( \mathbf { Z } ) \to \mathbf { Z }$ is a ring isomorphism, this completes the proof.□

# \$ 5. Spaces of Type II

We will first prove the following.

(5.1) Theorem. The signature of an inner product space of type I is necessarily divisible by 8.

An example in which the signature is precisely 8 will be described in $\ S 6$

To prove (5.1), we first consider an arbitrary inner product space $X$ over Z. An element $u \in X$ will be called characteristic if

$$
u \cdot x \equiv x \cdot x { \pmod { 2 } }
$$

(5.2) Lemma (van der Blij). Every inner product space X over Z possesses a characteristic element.Furthermore,if $u \in X$ is characteristic, then

$$
u \cdot u \equiv \sigma ( X ) { \pmod { 8 } } .
$$

Proof.Form the induced inner product space $X \otimes \mathbf { F } _ { 2 } = X / 2 X$ over the field with 2 elements. If $\bar { x }$ denotes the image of $x$ in $X / 2 X$ ,then the -inner product $_ x$ .yon $X$ clearly gives rise to an $\mathbf { F } _ { 2 }$ -valued inner product

x · y=(residue class of x · y mod 2) on X/2 x.

The function $\bar { x } \mapsto \bar { x } \cdot \bar { x }$ from X/2 X to $\mathbf { F } _ { 2 }$ is $\mathbf { F } _ { 2 }$ -linear. Hence there is one and only one element ${ \overline { { u } } } \in X / 2 X$ which satisfies the equation

$$
{ \bar { u } } \cdot { \bar { x } } = { \bar { x } } \cdot { \bar { x } }
$$

for all x. Choosing any preimage $u \in X$ ，we obtain the required characteristic element.

Next note that the residue class of u ·u modulo 8 is an invariant of X. For if $\pmb { u } ^ { \prime }$ is another characteristic element, then $u ^ { \prime } { = } u { + } 2 x$ hence

$$
u ^ { \prime } \cdot u ^ { \prime } = u \cdot u + 4 ( u \cdot x + x \cdot x ) \equiv u \cdot u ( { \bf m o d } \ : 8 ) .
$$

Clearly this invariant $u \cdot u$ is additive with respect to direct sums. For the inner product space $\langle 1 \rangle$ note that $u \cdot u \equiv 1$ mod 8, while for $\langle - 1 \rangle$ note that $u \cdot u \equiv - 1$ mod 8. So for the orthogonal sum of $p$ copies of $\langle 1 \rangle$ and $q$ copies of $\langle - 1 \rangle$ we see that $u \cdot u$ is congruent to the signature $\sigma { = } p { - } q { \bmod { 8 } } .$

For any inner product space $X$ ,the orthogonal sum $X \oplus \langle 1 \rangle \oplus \langle - 1 \rangle$ is indefinite of type I, and hence is isomorphic to a sum of copies of $\langle 1 \rangle$ and <-1>.Since theinvariant $u \cdot u$ mod 8 associated with $X \oplus \langle 1 \rangle \oplus \langle - 1 \rangle$ is the residue class of $\sigma ( x \oplus \langle 1 \rangle \oplus \langle - 1 \rangle ) { = } \sigma ( X )$ mod 8,and since the invariant associated with $\langle 1 \rangle \oplus \langle - 1 \rangle$ is zero, this proves the lemma.

Proof of(5.1). If $X$ is of type II, then we can choose $u = 0$ .Hence

$$
\sigma ( X ) { \equiv } 0 \cdot 0 ( \mathrm { m o d } 8 ) ,
$$

which completes the proof.□

Remark 1.The invariant $u \cdot u$ modulo 8is also defined for an inner product space over the ring $\mathbf { Z } _ { 2 }$ of 2-adic integers.It gives rise to a homomorphism from the Witt ring $W ( \mathbf { Z } _ { 2 } )$ to $\mathbf { Z } / 8 \mathbf { Z } .$ Evidently the diagram

W(Z)- →W(Z2) uu $\mathbf { Z } { \longrightarrow } \mathbf { Z } / 8 \mathbf { Z }$

is a commutative diagram of ring homomorphisms.

Remark 2.A different and quite intriguing formula for the signature mod 8 has recently been given by J.Milgram, in connection with a problem in topology. Let $V$ be any inner product space of signature $\sigma$ over the rational numbers,and let $L \subset V$ be any lattice which is small enough so that $l \cdot l { \in } 2 \mathbf { Z }$ for every $l \in L$ If $L ^ { \# } \subset V$ denotes the“dual lattice", consisting of all $\boldsymbol { v } \in V$ with ${ \vec { v } } \cdot L \subset \mathbf { Z } .$ and if $\overline { { v _ { 1 } , \ldots , v _ { d } } }$ is a complete set of coset representatives for $L ^ { \# } ~ \mathrm { m o d u l o } ~ L$ ，then Milgram proves that

$$
\exp ( 2 \pi i \sigma / 8 ) { = } \sum _ { j = 1 } ^ { d } \exp ( \pi i v _ { j } \cdot v _ { j } ) / \sqrt { d } .
$$

See Appendix 4 for further details.As an example,if $L$ is unimodular then $L = L ^ { \# }$ and $d = 1$ ,so the right hand side of this equation is equal to 1,and it follows once more that $\sigma { \equiv } 0 { \bmod { 8 } }$ .This is very close to the original proof of this congruence in [van der Blij].

![](images/c5d0aae6b257328e15bae29618a600911c980344440ed0bd7c056fc92c64b9c6.jpg)

For type I this was proved in $\ S 4 _ { ; }$ , so we need only consider type II.

Proof (following [Serre]). First consider the following construction. Given an inner product space $X$ of type I, we can form the subset $X _ { 0 }$ consisting of all $x$ with $x \cdot x { \equiv } 0 { \pmod { 2 } }$ . Evidently this is a sublattice of index 2 in X.We would like to construct an inner product space of type II which also contains $X _ { 0 }$ as a sublattice of index 2.If such a space exists, then evidently it must be contained in the“dual lattice”

$$
X _ { 0 } ^ { \# } \subset \mathbf { Q } \otimes X ,
$$

consisting of all vectors $x ^ { \# }$ in the vector space $\mathbf { Q } \otimes X$ which satisfy the condition ${ \boldsymbol { x } } ^ { * } { \boldsymbol { \cdot } } { \boldsymbol { x } } \in { \boldsymbol { Z } }$

for all ${ \boldsymbol { x } } \in X _ { 0 }$ . (Compare Chapter IV, $\ S 3 . )$ Since $X _ { 0 } ^ { \# }$ contains $X _ { 0 }$ as a sublattice of index 4, there are at most three different lattices which properly contain $X _ { 0 }$ and are properly contained in $X _ { 0 } ^ { \# }$ .One of these is $X$ itself.We will be interested in the other two.

As an example, let us apply this construction to the inner product space $W { = } \langle 1 \rangle \oplus \langle { - } 1 \rangle$ ，with orthogonal basis $e _ { 1 } , e _ { 2 }$ . Inspection shows that $W _ { 0 }$ has basis $e _ { 1 } + e _ { 2 } , e _ { 1 } - e _ { 2 }$ ,and that $W _ { 0 } ^ { \# }$ has a dual basis $\begin{array} { r } { \frac { 1 } { 2 } ( e _ { 1 } - e _ { 2 } ) , } \end{array}$ $\begin{array} { r } { \frac { 1 } { 2 } \left( e _ { 1 } + e _ { 2 } \right) } \end{array}$ Inthis case there are thre lattices lying between $W _ { 0 }$ and $W _ { 0 } ^ { \# }$ ，： One of these is W, and the other two are evidently both isomorphic to the hyperbolic plane $\overline { H }$

Now consider the sum $Y \oplus W { = } Y \oplus \langle 1 \rangle \oplus \langle - 1 \rangle$ where Y is an arbitrary inner product space of type II. Then the subspace $( Y \oplus W ) _ { 0 }$ of vectors of even norm is equal to $Y \oplus W _ { 0 }$ , hence $( Y \oplus W ) _ { 0 } ^ { \# } = Y \oplus W _ { 0 } ^ { \# }$ . Clearly there are three lattices lying between $( Y \oplus W ) _ { 0 }$ and $( Y \oplus W ) _ { 0 } ^ { \# }$ . One is $Y \oplus$ W, and the other two are both isomorphic to $Y \oplus H$

Let $Y ^ { \prime }$ be another inner product space of type II having the same rank and signature as Y. Then

by Theorem(4.3). Applying the construction above to both sides, it follows that $Y \oplus H \cong Y ^ { \prime } \oplus H .$

But a straightforward argument shows that any indefinite inner product space of type II is isomorphic to the orthogonal sum $Y \oplus H$ for some Y.(Compare Sections 2 and 4.) Evidently this completes the proof. $\bigtriangledown$

# $\ S 6 .$ The Classification Problem for Positive Definite Spaces

First let us describe some examples of positive definite inner product spaces over $\mathbf { Z } .$ Let $\mathbf { R } ^ { 4 m }$ denote the euclidean space with orthonormal basis e.,...,e4m

(6.1) Lemma. The vectors $e _ { i } + e _ { j }$ and $\scriptstyle { \frac { 1 } { 2 } } ( e _ { 1 } + \cdots + e _ { 4 m } )$ span $a$ lattice $ { T _ { 4 m } } \subset  { \mathbb { R } } ^ { 4 m }$ which is an inner product space over $\mathbf { Z }$

Proof. Let $L _ { 0 }$ be the sublatice of index 2 spanned by the $e _ { i } + e _ { j }$ Evidently $\scriptstyle L _ { 0 }$ can also be considered as a sublattice of index 2 in the lattice spanned by $e _ { 1 } , \ldots , e _ { 4 m }$ . Therefore a fundamental domain for $\scriptstyle L _ { 0 }$ has volume $^ 2$ ; hence a fundamental domain for $T _ { 4 m }$ has volume 1. Since inspection shows that the inner product of any two elements of $T _ { 4 m }$ is an integer, this completes the proof.

[More explicitly, $\Gamma _ { 4 m }$ can be described as the set of all linear combinations $\xi _ { 1 } e _ { 1 } + \dots + \xi _ { 4 m } e _ { 4 m }$ with $2 \xi _ { i } \in \mathbf { Z }$ $\xi _ { 1 } \equiv \xi _ { 2 } \equiv \cdots \equiv \xi _ { 4 m }$ mod $\mathbf { Z }$ and $\xi _ { 1 } + \cdots + \xi _ { 4 m } { \equiv } 0$ mod 2 Z.]

(6.2) Lemma. This inner product space $\Gamma _ { 4 m } ^ { \cdot }$ has type $I$ if m is odd, and （2014号 $t y p e I I$ if m is even.

Proof. Since each vector $\boldsymbol { \mathbf { \mathit { e } } } _ { i } + \boldsymbol { \mathbf { \mathit { e } } } _ { j }$ has norm 2，and the vector $\scriptstyle { \frac { 1 } { 2 } } ( e _ { 1 } + \cdots + e _ { 4 m } )$ has norm m, the conclusion follows easily.

Thus the lattices $\Gamma _ { 8 } , \Gamma _ { 1 6 } , \Gamma _ { 2 4 } , \ldots$ provide examples of positive definite inner product spaces of type II with signatures 8,16,2.4,...

We can get some insight into the collection of all positive definite inner product spaces over $\mathbf { z }$ as follows.

(6.3) Definition. An inner product space X is indecomposable provided it cannot be expressed as the orthogonal sum of two non-trivial subspaces.

(6.4) Theorem (Eichler). Every positive definite inner product space over Z splits uniquely as an orthogonal sum of indecomposable spaces.

Proof. (Compare [Kneser, 1954].) Call a vector $x \neq 0$ of $X$ minimal provided $_ { x }$ cannot be expressed as a sum y+z of two strictly shorter vectors of X (vectors with $y \cdot y < x \cdot x$ and $\scriptstyle z \cdot z < x \cdot x )$ Evidently the procedure of expressing a vector as a sum of shorter vectors must stop after a finite number of steps, hence $X$ is spanned (or generated) by its collection of minimal vectors. If $X$ splits as an orthogonal sum $X _ { 1 } \oplus X _ { 2 }$ ， note that every minimal vector of $X$ must belong either to $X _ { 1 }$ or to $X _ { 2 }$ ：

We say that two minimal vectors $x$ and $\boldsymbol { x ^ { \prime } }$ are equivalent provided there exists a finite sequence $x { = } x _ { 0 } , x _ { 1 } , \ldots , x _ { k } { = } x ^ { \prime }$ of minimal vectors with $x _ { i - 1 } \cdot x _ { i } { \neq } 0$ for $1 \leq i \leq k$ .Then each equivalence class spans a subspace of $X$ ,and clearly $X$ is the orthogonal direct sum of these subspaces.

Since this spliting is uniquely defined, the proof is complete.

Note that the above construction is easy to carry out in practice. Here is an example, where details are left to the reader.

(6.5) Proposition. The inner product space $\Gamma _ { 4 m }$ is indecomposable for $m \geq 2$ The minimal vectors of $\Gamma _ { 4 m }$ are precisely those vectors of the form $\pm e _ { i } \pm e _ { j } o r { \textstyle { \frac { 1 } { 2 } } } ( \pm e _ { 1 } \pm \dots \pm e _ { 4 m } )$ in $\Gamma _ { 4 m }$

Of course $T _ { 4 }$ is not indecomposable， since by (2.2) every positive definite space ofrank 4over Z must be isomorphic to $\langle 1 \rangle \oplus \langle 1 \rangle \oplus \langle 1 \rangle \oplus \langle 1 \rangle .$

![](images/dea52db8cc877246e639ff0db591cfff8f27eeb67f2706fe818e2ef4190b5c66.jpg)

It is not known whether any such symmetrical lattices exist in higher dimensions. It would be natural to look next in dimension 48, since the theory of modular forms [Serre,pp.171-178] indicates that an inner product space of type I with $x \cdot x { \geq } 6$ for $x \neq 0$ must have dimension at least 48. (It is intriguing to note that $8 = 3 ^ { 2 } - 1 , 2 4 = 5 ^ { 2 } - 1 , 4 8 = 7 ^ { 2 } - 1 . )$

# \$7. The Packing of Equal Balls in $\mathbf { R } ^ { n }$

The unimodular lattice $\Gamma _ { 8 }$ has the property that $x \cdot x { \geq } 2$ for every $x \neq 0$ in $\Gamma _ { 8 }$ ，while the Leech lattice has the property that $x \cdot x { \geq } 4$ for every $x \neq 0$ The $n$ -fold tensor product $I _ { 8 } \otimes \cdots \otimes I _ { 8 }$ provides an example of a unimodular lattice with $x \cdot x { \geq } 2 ^ { n }$ for every $x \ne 0$ (Compare $\ S 9 . 6 . )$ These -examples suggest the following question. Fixing $\scriptstyle n _ { 5 }$ what is the largest -possible value for the minimum non-zero norm

for a unimodular lattice $L$ in $\mathbf { R } ^ { n }$ ？

An alternative and completely equivalent formulation is the following. What is the largest possible value for the ratio

where now $L$ is allowed to vary over all lattices in $\mathbf { R } ^ { n } ?$ This version is equivalent, since any lattice of maximal rank in $\mathbf { R } ^ { n }$ can be transformed into a unimodular lattice by a similarity transformation $x \mapsto x / \sqrt [ 2 \eta ] { \operatorname* { d e t } { \cal L } }$ which does not affect the ratio $\mu ( L )$

Thefollowing observation is classical.(Compare [Watson,pp.29-31].)

(7.1) Lemma. For each dimension n there exists a lattice $L _ { n }$ which maximizes the ratio $\scriptstyle \mu ( L ) = ( \operatorname* { m i n } _ { x \in L - 0 } x \cdot x ) / \sqrt [ n ] { \operatorname* { d e t } L }$ .Furthermore,chooing $a$ basis for $L _ { n }$ , the associated inner product matrix (multiplied by a real constant if necessary）is $a$ matrix of rational numbers.

Hence the maximal ratio $\mu ( L _ { n } )$ is the $n$ -th root of a rational number. The proof of (7.1) will be given at the end of this section.

For $n { \le } 5$ the maximum value of $\mu ( L )$ was determined by Korkine and Zolotareff, and for $n { \le } 8$ by Blichfeldt. These maximum values, for $1 \leq n \leq 8 .$ are equal to $1 , { \sqrt { 4 / 3 } } , { \sqrt [ 3 ] { 2 } } , { \sqrt [ 4 ] { 4 } } , { \sqrt [ 3 ] { 8 } } , { \sqrt [ 6 4 / 3 ] { 6 4 } } , { \sqrt [ 7 ] { 6 4 } } ,$ and 2 respectively.Rounded to three decimal places, the values are as follows. (Compare p.36, Fig.3.)

![](images/00ac45b4d0e994add6d28c3481d332bde38d13350107bb26b95e47dcc1df8823.jpg)

In the case $n = 2$ the maximal value $\mu ( L _ { 2 } ) = \sqrt { 4 / 3 }$ is attained by the lattice of Fig.1, with inner product matrix $\binom { 2 } { 1 } \binom { 1 } { 2 }$ . We willrefer to this as the regular hexagonal lattice, since the associated “Voronoi polyhedron", consisting of all points in $ { \mathbf { R } } ^ { 2 }$ which are at least as close to the origin as to any other lattice point, is a regular hexagon.

![](images/7eea47268bdf09e9ec642ac16bf8c21f220249130377ab12e187e485c528e4f7.jpg)  
Fig.1. The regular hexagonal latice,and the associated packing of $\mathbf { R } ^ { 2 }$

For $n = 3$ ,4,5 the maximal value $\mu ( L _ { n } )$ is attained by a lattice $L _ { n }$ constructed as follows. Let $\mathbf { Z } ^ { n }$ be the lattice spanned by an orthonormal basis $e _ { 1 } , \ldots , e _ { n }$ for $\overline { { \mathbf { R } ^ { n } } }$ ,and let $\overline { { { L } _ { n } } }$ be the sublattice of index 2 spanned by the elements $\boldsymbol e _ { i } + \boldsymbol e _ { j }$ . In the case $n = 3$ ,this is known as the face centered cubic lattice, since it can be obtained from the“cubic” latice with basis $2 \boldsymbol { e } _ { 1 }$ ， $2 \boldsymbol { e } _ { 2 }$ ， $2 \boldsymbol { e } _ { 3 }$ by adjoining the center points of the faces of all of the cubes.(Compare Fig.2,as well as [Hilbert and Cohn-Vossen].） The inner product matrix, with respect to the basis $e _ { 1 } + e _ { 2 } , e _ { 1 } + e _ { 3 } , e _ { 2 } + e _ { 3 }$ is

$$
\left( { \begin{array} { c c c } { 2 } & { 1 } & { 1 } \\ { 1 } & { 2 } & { 1 } \\ { 1 } & { 1 } & { 2 } \end{array} } \right) .
$$

This lattice occurs in the real world as the configuration of atoms in a crystal of (for example) gold, silver, or aluminum. The Voronoi polyhedron associated with $L _ { 3 }$ is a rhombic dodecahedron; that is, it is a solid bounded by twelve rhombuses.

![](images/8237e76bd4e15f183be069e0455b9bcf5954dbe005c41d2a3b0e51684db7ec5e.jpg)  
Fig.2.The face centered cubic lattice in $\mathbb { R } ^ { 3 }$

For $n = 6 ,$ ，7,8 the function $\mu ( L )$ is maximized by a lattice $L _ { n }$ constructed as follows. Let $L _ { 8 }$ be the lattice $T _ { 8 }$ of $\ S 6$ let $\scriptstyle { L _ { 7 } }$ be the orthogonal complement of a minimal vector in $T _ { 8 }$ , and let $\scriptstyle L _ { 6 }$ be the orthogonal complement of a regular hexagonal lattice in $T _ { 8 }$ . These three lattices can be identified with the lattices generated by the root systems of the exceptional Lie groups $E _ { 6 } , \ E _ { 7 }$ ，and $E _ { 8 }$ . (Similarly the lattices $L _ { 2 } , L _ { 3 } , L _ { 4 } , L _ { 5 }$ are generated by the root systems $A _ { 2 } , A _ { 3 } , D _ { 4 } , D _ { 5 }$ . Compare pp.138-139.) For $n { > } 8$ ,the precise value of $\mu ( L _ { n } ) { = } \operatorname { M a x } _ { L \subset \mathbb { R } ^ { n } } \mu ( L )$ is not known. However it can be computed up to a factor of 4 as follows. Recall that $\omega _ { n } =$ $\pi ^ { n / 2 } / { \cal T } ( 1 + n / 2 )$ denotes the volume of the unit disk in $\mathbf { R } ^ { n }$

# (7.2) Theorem of Minkowski. The inequality

$$
\omega _ { n } ^ { - 2 / n } < \mu ( L _ { n } ) \le 4 \omega _ { n } ^ { - 2 / n }
$$

is valid for every n.

In fact, the upper bound $\mu ( L ) { \leq } 4 \omega _ { n } ^ { - 2 / n }$ is just a restatement of Corollary 1.5.Using Stirling's formula

![](images/0f3063df453bf8ab5be1169e4e1d5428a32a92ccdab912ede3de06dfaef296f2.jpg)

A much sharper upper bound of the form

$$
\mu ( L ) { \le } 4 ( \sigma _ { n } / \omega _ { n } ) ^ { 2 / n } { \sim } n / \pi e
$$

has been obtained by C.A.Rogers,and will be discussed later in this section. (Compare Fig.3.)

![](images/982564060ffe1666fdcb18c979f93806e6397c7fe2229a66f1cde0b6a04d9b9a.jpg)

(or rather the slightly sharper lower bound $\mu ( L _ { n } ) \geq ( 2 \zeta ( n ) / \omega _ { n } ) ^ { 2 / n } )$ was proved by Minkowski in 1905.The name of E.Hlawka is often attached to this inequality since a generalization, stated by Minkowski, was first proved by Hlawka. Sharper inequalities of this form have been given by W. Schmidt, Rogers and others, but these all have the same asymptotic behavior as $n \to \infty$ . Compare [Rogers, 1964]. A version involving self-dual lattices will be proved in \$ 9.5.

Proof of the inequality $\mu ( L _ { n } ) \geq ( 2 / \omega _ { n } ) ^ { 2 / n } > \omega _ { n } ^ { - 2 / n }$ .The notation ${ \boldsymbol { x } } =$ $( \xi _ { 1 } , \ldots , \xi _ { n } )$ will be used for a point in $\mathbf { R } ^ { n }$ Let $f ( x ) { = } f ( \xi _ { 1 } , \ldots , \xi _ { n } ) { \\\ \geq } 0$ be a continuous real valued function with compact support. The integral $\int _ { - \infty } ^ { \infty } \cdots \int _ { - \infty } ^ { \infty } f ( \xi _ { 1 } , \ldots , \xi _ { n } ) d \xi _ { 1 } \ldots d \xi _ { n }$ will be written briefly as $\int f ( x ) d x .$ We 1 will first prove the following. Assume that $n \geq 2$

(7.3) Lemma. Given any real number $\beta { \ > } \int f ( x ) d x ,$ there exists $^ { a }$ unimodular lattice $\mathbf { \mathcal { L } } \mathbf { \mathbf { \Lambda } } = \mathbf { \mathbf { R } } ^ { n }$ so that the sum ∑ f(x)is less than $\beta$ xeL-0

Proof. Let $e _ { 1 } , \ldots , e _ { n }$ be the standard orthonormal basis for $\mathbf { R } ^ { n }$ Let $\varepsilon > 0$ be a fixed small number, to be chosen later,and define $\lambda { > } 0$ by the equation $\varepsilon \lambda ^ { n - 1 } = 1$ Given real parameters $\tau _ { 1 } , \dots , \tau _ { n - 1 }$ we consider the unimodular lattice $L = L ( \tau _ { 1 } , \dots , \tau _ { n - 1 } )$ which is spanned by the basis

$$
\lambda e _ { 1 } , \ldots , \lambda e _ { n - 1 } , \quad \tau _ { 1 } \lambda e _ { 1 } + \cdots + \tau _ { n - 1 } \lambda e _ { n - 1 } + \varepsilon e _ { n } .
$$

Thus a typical element of this lattice $L ( \tau _ { 1 } , \dots , \tau _ { n - 1 } )$ is the n-tuple

$$
\left( \lambda ( i _ { 1 } + j \tau _ { 1 } ) , \ldots , \lambda ( i _ { n - 1 } + j \tau _ { n - 1 } ) , j \varepsilon \right)
$$

where $i _ { 1 } , \ldots , i _ { n - 1 }$ and $j$ range independently over $\mathbf { Z }$ Clearly the lattice $L ( \tau _ { 1 } , \dots , \tau _ { n - 1 } )$ remains unchanged if we add an integer to any one of the parameters $\tau _ { y }$

Fixing ε, for each value of the parameters $\tau _ { 1 } , \dots , \tau _ { n - 1 }$ modulo 1 consider the sum

$$
\frac { \displaystyle \sum _ { x \in L ( \tau _ { 1 } , \ldots , \tau _ { n - 1 } ) - 0 } f ( x ) { = } \sum ^ { } f ( \lambda ( i _ { 1 } { + } j \tau _ { 1 } ) , \ldots , \lambda ( i _ { n - 1 } { + } j \tau _ { n - 1 } ) , j \varepsilon ) , } { x \in L ( \tau _ { 1 } , \ldots , \tau _ { n - 1 } ) - 0 }
$$

where the latter sum extends over al $n$ -tuples $i _ { 1 } , \ldots , i _ { n - 1 } , j$ of integers, not all zero. Since $f$ has compact support, we may choose ε so small that

$$
f ( \lambda i _ { 1 } , \ldots , \lambda i _ { n - 1 } , 0 ) { = } 0
$$

for $( i _ { 1 } , \ldots , i _ { n - 1 } ) { \neq } ( 0 , \ldots , 0 )$ ，If ε is so chosen, then the terms with $\scriptstyle j = 0$ make no contribution, so we can rewrite the sum(1) as

where

$$
S _ { j } ( \tau _ { 1 } , \dots , \tau _ { n - 1 } ) = \sum _ { i _ { 1 } , \dots , i _ { n - 1 } } f \bigl ( \lambda ( i _ { 1 } + j \tau _ { 1 } ) , \dots , \lambda ( i _ { n - 1 } + j \tau _ { n - 1 } ) , j \varepsilon \bigr )
$$

is zero for $| j |$ large. Next consider the average

$$
\begin{array} { r l r } {  { \frac { 1 } { \int \cdots \int \sum _ { 0 } ^ { 1 } { S _ { j } ( \tau _ { 1 } , \dots , \tau _ { n - 1 } ) d \tau _ { 1 } \dots d \tau _ { n - 1 } } } } } \\ & { } & { \frac { 1 } { \int \cdots \int \sum _ { 0 } ^ { 1 } { S _ { j } ( \tau _ { 1 } , \dots , \tau _ { n - 1 } ) d \tau _ { 1 } \dots d \tau _ { n - 1 } } } } \end{array}
$$

as $\tau _ { 1 } , \dots , \tau _ { n - 1 }$ vary from $^ { \circ }$ to 1. If $j > 0$ ，then the substitution $\eta _ { \mathrm { v } } = j \tau _ { \mathrm { v } }$ transforms the latter integral into

$$
j ^ { 1 - n } \int _ { 0 } ^ { j } \dots \int _ { 0 - i _ { 1 } , \dots i _ { n - 1 } } ^ { j } f \bigl ( \lambda ( i _ { 1 } + \eta _ { 1 } ) , \dots , \lambda ( i _ { n - 1 } + \eta _ { n - 1 } ) , j \varepsilon \bigr ) d \eta _ { 1 } \dots d \eta _ { n - 1 } .
$$

But inspection shows that we are integrating precisely $j ^ { n - 1 }$ times over each unit cube in $\mathbf { R } ^ { n - 1 }$ ,so that this expresonis preciselyequal to

$$
\begin{array} { l } { { \displaystyle \int \cdots \int ^ { \infty } f ( \lambda \eta _ { 1 } , \ldots , \lambda \eta _ { n - 1 } , j \varepsilon ) d \eta _ { 1 } \ldots d \eta _ { n - 1 } . } } \\ { { \displaystyle - \infty \qquad - \infty } } \end{array}
$$

A similar argument proves this formula when $j { < } 0$ .Seting

$$
g ( \eta ) = \int \displaylimits _ { - \infty } ^ { \infty } \dots \int f ( \xi _ { 1 } , \dots , \xi _ { n - 1 } , \eta ) d \xi _ { 1 } \dots d \xi _ { n - 1 } ,
$$

$$
\lambda ^ { 1 - n } g ( j \varepsilon ) = \varepsilon g ( j \varepsilon ) .
$$

Therefore the average (2) is equal to

$$
\sum _ { j \not = 0 } \varepsilon g ( j \varepsilon ) .
$$

But the function $g ( \eta )$ is continuous with compact support, so the sum (3) clearly converges, as $\varepsilon \to 0 ,$ to the Riemann integral

$$
\intop _ { - \infty } ^ { \infty } g ( \eta ) d \eta = \int f ( x ) d x < \beta .
$$

Choosing ε so small that the Riemann sum (3) is less than $\beta _ { : }$ ,it follows that the average (2) is also less than $\beta$ .Therefore there must exist actual parameter values $\tau _ { 1 } , \dots , \tau _ { n - 1 }$ so that the sum $( 1 ) { = } ( 1 ^ { \prime } )$ is less than $\beta$ This completes the proof of (7.3).□

To prove Theorem 7.2, we make a particular choice of the function $f .$ Let $r < s$ be positive real numbers which are less than $( 2 / \omega _ { n } ) ^ { 1 / n } .$ Choose $f$ so that T7-. 1 12

with $0 \leq f ( x ) \leq 1$ everywhere. Then evidently

$$
\int f ( x ) d x < \omega _ { n } s ^ { n } < 2 .
$$

Therefore, by (7.3), there exists a unimodular lattice $L \subset \mathbf { \mathbf { R } } ^ { n }$ with

$$
\sum _ { \mathbf { x } \in L - 0 } f ( x ) < 2 .
$$

This lattice Lcannot contain any vector $\mathbf { \boldsymbol { x } } _ { 0 }$ with

$$
0 < x _ { 0 } \cdot x _ { 0 } \le r ^ { 2 } .
$$

For if such a vector $x _ { 0 }$ existed, then the summation (4) would include the terms $f ( x _ { 0 } ) + f ( - x _ { 0 } ) { \geq } 2$ ,which is impossible.Therefore

$$
\mu ( L ) { = } \operatorname { M i n } _ { x \in L - 0 } x \cdot x > r ^ { 2 } .
$$

Since $r ^ { 2 }$ can be any number less than $( 2 / \omega _ { n } ) ^ { 2 / n }$ ,this proves that

$$
\scriptstyle \mu ( L _ { n } ) = \operatorname* { s u p } _ { L \subset \mathbb { R } ^ { n } } \mu ( L ) \geq ( 2 / \omega _ { n } ) ^ { 2 / n } ,
$$

which completes the proof of 7.2.□

These remarks leave many questions unanswered. Does the ratio $\mu ( L _ { n } ) / n$ tend to a limit as $n \to \infty ?$ If so,what is the limit? Does the sequence $\mu ( L _ { 1 } ) , \mu ( L _ { 2 } )$ ,.. increase monotonically? What are the actual values of $\mu ( L _ { 9 } ) , \mu ( L _ { 1 0 } ) , \ldots ?$

Closely related to the problem of computing $\overline { { \mu ( L _ { n } ) } }$ is the following classical problem. What is the maximum possible density for a union of non-overlapping balls of fixed radius in the euclidean space $\mathbf { R } ^ { n }$ ?

Such a union $P$ of non-overlapping balls, all of the same radius, will be called briefly a packing of $\mathbf { R } ^ { n } .$ A packing $P$ is said to have density $\rho$ if the ratio

$$
\mathsf { v o l } ( P \cap C ) / \mathsf { v o l } ( C ) ,
$$

where C denotes a large cube, tends uniformly to the limit p as the edge of the cube tends to infinity.

Any lattice $\mathbf { Z } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } \mathbf { R } ^ { n }$ gives rise to a packing of $\overline { { \mathbf { R } ^ { n } } }$ as follows. Define the radius r by the equation

$$
( 2 r ) ^ { 2 } { = } \operatorname* { M i n } _ { x \in L - 0 } x \cdot x .
$$

Centering a ball of radius $r$ at each lattice point, the interiors of the different balls will evidently be disjoint. The density of this packing is given by the formula

$$
\rho { = } \omega _ { n } r ^ { n } / \sqrt { \operatorname* { d e t } L } { = } \omega _ { n } ( \mu ( L ) / 4 ) ^ { n / 2 } .
$$

Therefore

$$
\scriptstyle \mu ( L ) = 4 ( \rho / \omega _ { n } ) ^ { 2 / n } .
$$

Note that Minkowski's estimate (1.5) is just the inequality $\rho { \stackrel { < } { = } } 1 .$

It was proved by A. Thue that the maximum possible density of a packing of $\mathbf { R } ^ { 2 }$ is equal to the density $\rho { = } \pi / \sqrt { 1 2 }$ associated with the regular hexagonal lattice of Fig.1. For $n = 3$ ，the face centered cubic lattice gives rise to a packing with density $\pi / { \sqrt { 1 8 } }$ ，For an arbitrary packing of $\overline { { \mathbf { R } ^ { 3 } } }$ ,according to Rogers, “many mathematicians believe and all physicists know that the density cannot exceed $\pi / \nu ^ { \sqrt { 1 8 } ^ { \ast } } .$ However this has never been proved. Indeed the problem remains unsolved for all $n \geq 3$ .It is noteworthy that Leech and Sloane have recently described examples of non-lattice packings in dimensions 10, 11,13 which are denser than the packings associated with any known lattices in these dimensions.

An excellent upper bound for the density for any packing of $\mathbf { R } ^ { n }$ ,has been given by Rogers,based on earlier work by Blichfeldt.Let $\varDelta _ { n }$ be an equilateral $\underline { n }$ -simplex in euclidean space, with edge length 2. Let $B$ be the subset consisting of all points in $\varDelta _ { n }$ with distance ≤1 from some vertex of $A _ { n } ,$ and let

Then for any packing of $R ^ { n }$ which possesses a density $\rho$ ,Rogers proves the inequality

(Here is a table listing some examples, with decimals rounded to the nearest ten-thousandth.)

![](images/e4cf952d4b17ff4e37068d3b34ef68eee60faeb196143686c5c780e68bda9dfd.jpg)

For any lattice $L ,$ it follows that

$$
\mu ( L ) { = } 4 ( \rho / \omega _ { n } ) ^ { 2 / n } { \leq } 4 ( \sigma _ { n } / \omega _ { n } ) ^ { 2 / n } .
$$

This represents a: substantial improvement over the upper bound $4 ( 1 / \omega _ { n } ) ^ { 2 / n }$ of $\ S 1$ ，as becomes apparent if one uses Rogers asymptotic formula

Numerical values, for $n { \leq } 2 4 ,$ are plotted in Fig.3. All of the data used in this graph are taken from [Leech] and [Leech, Sloane].For $\scriptstyle n = 8$ 。

note that the Rogers upper bound $4 ( \sigma _ { 8 } / \omega _ { 8 } ) ^ { \frac { 1 } { 4 } } \approx 2 . 0 0 6$ is so close to $\mu ( L _ { 8 } ) { = } 2$ that the two points appear to coincide in the graph.

![](images/6b56d921bb957f3795bc74dfd1d7443ac7e0b1cccd96b84a1fe305b18d616060.jpg)  
Fig.3. The middle row of dots gives the largest possible value of $\overline { { \mu ( L ) { = } \mathbf { M } { \mathrm { i n } } ( \mathbf { x } \cdot \mathbf { x } ) / \sqrt [ n ] { \operatorname* { d e t } L } } }$ for a lattice $\overline { { L } }$ in each dimension $n \leq 8$ ,and the largest known value for each dimension $n$ 2 between 9 and 24. The top row of dots gives the Rogers upper bound 4 $( \sigma _ { n } / \omega _ { n } ) ^ { 2 / n } ;$ and the bottom row gives the crude Minkowski lower bound $( 2 / \omega _ { n } ) ^ { 2 / n }$ ：

To conclude this section we must prove Lemma 7.1. The proof wil be based on the following.

(7.4) Lemma. There exists $^ { a }$ constant $c _ { n } > 0$ so that every lattice in $\mathbf { R } ^ { n }$ possesses a basis $\boldsymbol { b } _ { 1 } , \ldots , \boldsymbol { b } _ { n }$ with

for all i,j.

$$
| b _ { i } \cdot b _ { j } | \{ \neq { c _ { n } } \operatorname* { d e t } ( L ) / ( \operatorname* { M i n } _ { L - 0 } x \cdot x ) ^ { n - 1 }
$$

In fact we will show that a suitable constant $c _ { n }$ can be defined inductively by the formula

$$
c _ { n } = ( \frac { 4 } { 3 } ) ^ { n - 2 } c _ { n - 1 } + 4 ^ { n } \omega _ { n } ^ { - 2 } ,
$$

with ${ { c } _ { 1 } } \mathrm { { = } } 1 .$

To begin the proof of (7.4), choose a vector bn=O in L with

$$
b _ { n } \cdot b _ { n } { = } \operatorname* { M i n } _ { x \in L - 0 } x \cdot x .
$$

Then

$$
b _ { n } \cdot b _ { n } \leq 4 \omega _ { n } ^ { - 2 / n } ( \operatorname* { d e t } L ) ^ { 1 / n }
$$

by 1.5 or 7.2. Dividing the $n$ -th power of (7) by the $( n - 1 )$ -st power of (6), we obtain the inequality

$$
b _ { n } \cdot b _ { n } { \leq } ( 4 ^ { n } \omega _ { n } ^ { - 2 } ) \operatorname * { d e t } L / ( \operatorname * { M i n } _ { L - 0 } x \cdot x ) ^ { n - 1 } ,
$$

This completes the proof when $n = 1$ . Suppose then that $n \geq 2 .$ Let $L ^ { \prime }$ denote the image of $L$ under orthogonal projection from $\mathbf { R } ^ { n }$ to the hyperplane $( b _ { n } ) ^ { \perp }$ . Then every vector $x ^ { \prime } \in L ^ { \prime }$ can be expressed as a difference

$$
\scriptstyle { \mathbf { x } } ^ { \prime } = { \mathbf { x } } - \lambda b _ { n }
$$

$$
b _ { n } \cdot b _ { n } \leq x \cdot x = x ^ { \prime } \cdot x ^ { \prime } + \lambda ^ { 2 } b _ { n } \cdot b _ { n } \leq x ^ { \prime } \cdot x ^ { \prime } + \textstyle { \frac { 1 } { 4 } } b _ { n } \cdot b _ { n } ,
$$

hence

$$
x ^ { \prime } \cdot x ^ { \prime } \geq \frac { 3 } { 4 } b _ { n } \cdot b _ { n } = \frac { 3 } { 4 } \operatorname* { M i n } _ { L - 0 } x \cdot x .
$$

Now, using the formulas

$$
\operatorname* { M i n } _ { L ^ { \prime } - 0 } x ^ { \prime } \cdot x ^ { \prime } { \\\geq } \frac { 3 } { 4 } \operatorname { M i n } _ { L - 0 } x \cdot x
$$

and

$$
\operatorname * { d e t } ( L ^ { \prime } ) { = } \operatorname * { d e t } ( L ) / b _ { n } \cdot b _ { n } ,
$$

it follows inductively that $L ^ { \prime }$ possesses a basis $b _ { 1 } ^ { \prime } , \ldots , b _ { n - 1 } ^ { \prime }$ with

$$
\begin{array} { r } { \jmath _ { i } ^ { \prime } \cdot b _ { i } ^ { \prime } \leq c _ { n - 1 } \operatorname* { d e t } { ( L ^ { \prime } ) } / \big ( \underset { L ^ { \prime } - 0 } { \operatorname { M i n } } x ^ { \prime } \cdot x ^ { \prime } ) ^ { n - 2 } \leq ( \frac { 4 } { 3 } ) ^ { n - 2 } c _ { n - 1 } \operatorname* { d e t } { ( L ) } / \big ( \underset { L - 0 } { \operatorname { M i n } } x \cdot x \big ) ^ { n - 1 } . } \end{array}
$$

Setting $b _ { i } ^ { \prime } { = } b _ { i } { - } \lambda _ { i } b _ { n }$ with $| \lambda _ { i } | < 1$ ，we obtain the required elements $b _ { 1 } , \ldots , b _ { n - 1 } ,$ satisfying

$$
\frac { \ d b _ { i } \cdot b _ { i } < b _ { i } ^ { \prime } \cdot b _ { i } ^ { \prime } + b _ { n } \cdot b _ { n } \leq c _ { n } \operatorname* { d e t } L / ( \operatorname* { M i n } _ { L - 0 } x \cdot x ) ^ { n - 1 } } { \ d t }
$$

by (5), (8), (9). Evidently $b _ { 1 } , \ldots , b _ { n }$ form a basis for $L$ . Since the required upper bound for $| \boldsymbol { b } _ { i } \cdot \boldsymbol { b } _ { j } |$ ，with $i \neq j ,$ ，now follows from the Schwarz inequality,this completes the proof of(7.4).□

Proof of Lemma (7.1). Let $K$ be the set consisting of all symmetric $n \times n$ matrices $A = ( a _ { i j } )$ of real numbers which satisfy the inequality

$$
\sum a _ { i j } \zeta _ { i } \zeta _ { j } \exists ^ { } 1
$$

for every n-tuple $( \zeta _ { 1 } , \ldots , \zeta _ { n } )$ of integers, not all zero.Evidently K can be thought of as a closed and convex subset of real $n ( n + 1 ) / 2$ -space.

Note that every matrix in $\kappa$ is positive definite. In fact it follows from 1.5 or 7.2 that every positive definite matrix $\overline { { A } }$ in $\kappa$ satisfies the inequality

$$
\operatorname* { d e t } { ( A ) } \geq \omega _ { n } ^ { 2 } / 4 ^ { n } > 0 .
$$

It follows easily that the subset of $K$ consisting of positive definite matrices is not only open, but also closed.Hence this subset equals $K$

We will prove that the determinant function $A \mapsto \operatorname* { d e t } ( A )$ from $K$ to R actually attains a minimum value at some point $\scriptstyle A _ { 0 } \in K$ .Let $K _ { 0 } { \subset } K$ be the compact subset consisting of all matrices $\scriptstyle { \overline { { A = ( a _ { i j } ) } } }$ in $\kappa$ whose entries $\overline { { a _ { i j } } }$ satisfy lai/≤en

It follows from 7.4 that for every matrix $A \in K$ with det $( A ) \leq 1$ there exists an invertible integer matrix $P { \in } \mathrm { G L } ( n , \mathbf { Z } )$ so that $P A P ^ { t } { \in } K _ { 0 }$ ： Evidently

$$
\operatorname* { d e t } { ( P A P ^ { t } ) } = \operatorname* { d e t } { ( A ) } .
$$

But the determinant function restricted to the compact set $K _ { 0 }$ certainly attains a minimum value. Therefore we can choose $\mathbf { \delta } _ { A _ { 0 } \in K _ { 0 } }$ with det $\operatorname { \Pi } ( A _ { 0 } ) { \leq } \operatorname* { d e t } ( A )$ for all $\scriptstyle A \in K _ { 0 }$ ,and therefore for all $\mathbf { \nabla } \overline { { A \in K } }$

$L _ { n }$ is a lattice with inner product matrix $A _ { 0 }$ ， then evidently it follows that

$$
\mu ( L _ { n } ) { = } 1 / \sqrt [ n ] { \operatorname* { d e t } A _ { 0 } }
$$

is equal to $\operatorname* { M a x } _ { L \subset \mathbb { R } ^ { n } } \mu ( L )$

Now we must prove that $A _ { 0 }$ is a matrix of rational numbers.More generally, following Korkine and Zolotareff, a matrix $\underline { { A _ { 0 } } } \in K$ is called extreme if the function det: $\mathbf { \nabla } K \to \mathbf { R }$ has a local minimum at $\scriptstyle A _ { 0 }$ .Note that an extreme matrix $A _ { 0 }$ cannot lie in the interior of $^ { a }$ line segment of matrices

$$
\begin{array} { r } { A _ { \xi } = A _ { 0 } + \xi B , ~ - \varepsilon < \xi < \varepsilon , } \end{array}
$$

all belonging to $K$ with $B \neq 0 .$ (In the language of convex set theory, an extreme matrix is necessarily an“extreme point”of the convex set $K .$ For choosing a real matrix $P$ with $P A _ { 0 } P ^ { t } = I ,$ and setting $P B P ^ { t } = C = ( c _ { i j } ) ,$ a short computation shows that

$$
\operatorname * { d e t } ( \varLambda _ { \xi } ) / \operatorname * { d e t } ( \varLambda _ { 0 } ) = \operatorname * { d e t } ( I + \xi C ) = \frac { 1 } { 2 } + \frac { 1 } { 2 } \bigl ( 1 + \xi \sum _ { i } c _ { i i } \bigr ) ^ { 2 } - \frac { 1 } { 2 } \xi _ { * } ^ { 2 } \sum _ { i } \sum _ { j } c _ { i j } ^ { 2 } + \cdots
$$

omitting terms in $\xi ^ { 3 }$ and higher powers. Since $C \neq 0 ,$ ,it follows easily that there exist arbitrarily small values of $\xi$ with det $\begin{array} { r } { ( A _ { \xi } ) { < } \mathrm { d e t } ( A _ { 0 } ) . } \end{array}$

If $A _ { 0 }$ is an extreme matrix, let $\pm z _ { ( 1 ) } , . . . , \pm z _ { ( N ) }$ be a complete list of all $n$ -tuples of integers (thought of as $1 \times n$ matrices) which satisfy the matrix equation

$$
z _ { ( i ) } A _ { 0 } z _ { ( i ) } ^ { t } = 1 .
$$

We will consider $\mathrm { ( 1 1 ) }$ as a collection of N linear equations for ther $\ n ( n + 1 ) / 2$ entries of the matrix $A _ { 0 }$ . We claim that these equations can be solved uniquely for $A _ { 0 }$ . For otherwise,if the solution were not unique, there would exist a one-parameter family of symmetric matrices $\begin{array} { r } { A _ { \xi } = A _ { 0 } + \xi B _ { \xi } } \end{array}$ all satisfying the equations (11). We will prove that $A _ { \xi } { \in } K$ for $\xi$ sufficiently small. If $z$ is a non-zero $n$ -tuple of integers, then either $z A _ { 0 } z ^ { t } = 1$ and hence $z A _ { \xi } z ^ { t } { = } 1$ also,or $z A _ { 0 } z ^ { t } \ge c$ for some constant $c > 1$ In the latter case, choosing a constant $\pmb { \varepsilon } > \mathbf { 0 }$ so that

for all $\boldsymbol { x } \in \mathbb { R } ^ { n } ,$ , it follows that

$$
z A _ { \xi } z ^ { t } \ge z A _ { 0 } z ^ { t } - \varepsilon ^ { - 1 } | \xi | z A _ { 0 } z ^ { t } > 1
$$

whenever $| \xi | < ( 1 - c ^ { - 1 } ) \varepsilon$ Thus $\underline { { A _ { \xi } \in K } }$ for $| \xi | < ( 1 - c ^ { - 1 } ) \varepsilon ,$ which contradicts the hypothesis that $\scriptstyle A _ { 0 }$ is extreme.

Since the unique solution of rational linear equations is necessarily rational, this shows that $A _ { 0 }$ is a matrix of rational numbers,and completes the proof of (7.1).□

# \$ 8. Sums of Two and Four Squares

This section will use Minkowski's convex body theorem to prove two venerable theorems. The first was stated by Fermat in the seventeenth century,and proved by Euler in the eighteenth century.

(8.1) Theorem. If $\overline { { p } }$ is a prime number of the form 4k+1, then the equation $a ^ { 2 } + b ^ { 2 } = p$ has a solution with $a , b \in \mathbf { Z }$

In terms of the ring $\mathbf { Z } [ i ]$ of Gaussian integers,this theorem states that every such prime splits as a product $\left( a + b i \right) ( a - b i ) .$

Proof. Let $p$ be any odd prime. First note that the congruence $u ^ { 2 } { \equiv } \mathrm { - } 1 ( \mathrm { m o d } p )$ has a solution u∈Z if and only if p=1 (mod 4). For the group $( \mathbf { Z } / p \mathbf { Z } ) ^ { \bullet }$ of relatively prime residue classes modulo $p$ is cyclic of order $p { - } 1$ The image of $- 1 \mathrm { i n } ( \mathbf { Z } / p \mathbf { Z } ) ^ { \bullet }$ is the unique element of order 2. Evidently there exists an element of order 4 in this group if and only if 4 divides $p { - } 1$ ,that is,if and only if $p { \equiv } 1 \ ( \mathbf { m o d } \ 4 )$

Suppose now that $p$ is congruent to 1 mod 4,and choose some integer $u$ satisfying the congruence $u ^ { 2 } \equiv - 1$ (mod $p \mathrm { ~ , ~ }$ Fixing $u _ { { \scriptscriptstyle \mathrm { i } } }$ ，let $\mathbf { \Delta } L = \mathbf { Z } \oplus \mathbf { Z }$ be the lattice in $\mathbf { R } ^ { 2 }$ consisting of all pairs $( a , b )$ of integers satisfving

$$
b \equiv u a { \pmod { p } } .
$$

Then $\pmb { L }$ is a subgroup of index ${ \dot { p \ln { \bf Z } ^ { 2 } } }$ ,hence the volume of a fundamental domain for $\boldsymbol { L }$ is $p$ .Therefore by (1.5) there exists a lattice point $\overline { { x \ne 0 } }$ with

$$
x \cdot x \leq 4 p / \pi .
$$

Setting $\scriptstyle x = ( a , b )$ , it follows that

$$
0 < a ^ { 2 } + b ^ { 2 } \leq 4 p / \pi < 2 p .
$$

But modulo $p$ we have

$$
a ^ { 2 } + b ^ { 2 } \equiv a ^ { 2 } + ( u a ) ^ { 2 } \equiv ( 1 + u ^ { 2 } ) a ^ { 2 } \equiv 0 .
$$

Therefore $a ^ { 2 } + b ^ { 2 }$ must be precisely equal to $p .$ ，This completes the proof.□

(8.2) Corollary. The subset of $\mathbf { Q } ^ { \bullet }$ consisting of all non-zero rationals which can be expressed as the sum of two squares is $a$ free abelian multiplicative group, with basis 2, $3 ^ { 2 }$ ,5, $7 ^ { 2 }$ $1 1 ^ { 2 }$ ,13,17,...

(Compare Chapter III, $\ S 4 . 4 . )$

Proof. First consider any equation of the form $\alpha ^ { 2 } + \beta ^ { 2 } = \gamma \neq 0$ in Q. After multiplying by a large square, we may assume that $\alpha , \beta , \gamma \in \mathbf { Z }$ We must show that any odd prime $\overline { { p } }$ which divides y to an odd power must be of the form $4 k + 1$ Let $p ^ { 2 i }$ be the highest power of $p$ dividing both $\alpha ^ { 2 }$ and $\beta ^ { 2 }$ . Then evidently

$$
( \alpha / p ^ { i } ) ^ { 2 } \equiv - ( \beta / p ^ { i } ) ^ { 2 } \not \equiv 0 ( \mathrm { m o d } p ) .
$$

Hence $- 1$ is a quadratic residue modulo $p$ ，and by the first remark in the proof of (8.1) it follows that $p \equiv 1$ (mod 4). Thus if $\gamma = { \alpha } ^ { 2 } + { \beta } ^ { 2 }$ then $\gamma$ must belong to the multiplicative group generated by 2, 3², 5, 7², Conversely,using the identity

$$
( a ^ { 2 } + b ^ { 2 } ) ( c ^ { 2 } + d ^ { 2 } ) = ( a c - b d ) ^ { 2 } + ( a d + b c ) ^ { 2 }
$$

it follows easily that every element of this multiplicative group is a sum of squares.

Here is an exercise for the reader. Prove that an integer is a sum of two rational squares if and only if it is a sum of two integer squares.

Our second theorem was stated by Bachet de Méziriac in the seventeenth century,and proved by Lagrange in the eighteenth.

(8.3) Theorem. Every positive integer is a sum of four squares.

It follows easily that every positive rational is a sum of four rational squares. (This can be interpreted as a special case of Meyer's theorem, corresponding to inner product spaces of the form $\langle 1 \rangle \oplus \langle 1 \rangle \oplus \langle 1 \rangle \oplus$ $\langle 1 \rangle \oplus \langle - r \rangle . \rangle$

Proof. Let $\overline { { p } }$ be any odd prime. By Lemma 3.3, we see that the con

$$
u ^ { 2 } + v ^ { 2 } + 1 \equiv 0 { \bmod { p } }
$$

has a solution u, $v \in \mathbf { Z }$ .(The“shoe box principal” shows that one of the $( p + 1 ) / 2$ distinct values of $u ^ { 2 }$ modulo $p$ must coincide with one of the $( p + 1 ) / 2$ distinct values of $- 1 - v ^ { 2 } .$ ）Fixing $u$ and $v _ { \mathrm { { s } } }$ let $\pmb { L } { \in } \pmb { Z } \oplus \pmb { Z } \oplus \pmb { Z } \oplus \pmb { Z }$ be the lattice consisting of all 4-tuples $( a , b , c , d )$ with

$$
c \equiv u a + v b , \quad d \equiv u b - v a ( \mathrm { m o d } p ) .
$$

Then L is a subgroup of index $p ^ { 2 } \dot { \mathrm { ~ i n ~ } } \mathbf { Z } ^ { 4 }$ , so it follows that the volume of a fundamental domain for $\scriptstyle { \dot { L } } { \mathrm { i s } } p ^ { 2 }$ .Therefore,by (1.5), there existsa lattice point $\overline { { x } }$ +0with

$$
x \cdot x { \leq } 4 \sqrt { p ^ { 2 } / \omega _ { 4 } } { = } 4 p \sqrt { 2 } / \pi .
$$

Setting $\scriptstyle x = ( a , b , c , d ) .$ ,it follows that

$$
0 < a ^ { 2 } + b ^ { 2 } + c ^ { 2 } + d ^ { 2 } \leq 4 p \sqrt { 2 } / \pi < 2 p .
$$

But, working modulo $p$ ,we have

$$
\frac { a ^ { 2 } + b ^ { 2 } + c ^ { 2 } + d ^ { 2 } \equiv a ^ { 2 } + b ^ { 2 } + ( u a + v b ) ^ { 2 } + ( u b - v a ) ^ { 2 } } { = ( 1 + u ^ { 2 } + v ^ { 2 } ) a ^ { 2 } + ( 1 + u ^ { 2 } + v ^ { 2 } ) b ^ { 2 } }
$$

Therefore $a ^ { 2 } + b ^ { 2 } + c ^ { 2 } + d ^ { 2 }$ must be precisely equal to $p$

To extend this result to an arbitrary product of primes, we note that $a ^ { 2 } + b ^ { 2 } + c ^ { 2 } + d ^ { 2 }$ is the norm of the quaternion $a + b i + c j + d k .$ Since the norm function from the quaternions to the reals is multiplicative, it follows that any product $( a ^ { 2 } + b ^ { 2 } + c ^ { 2 } + d ^ { 2 } )$ $( A ^ { 2 } + B ^ { 2 } + C ^ { 2 } + D ^ { 2 } )$ of sums of four squares can itself be expressed as a sum

$$
( a A - b B - c C - d D ) ^ { 2 } + ( a B + b A + c D - d C ) ^ { 2 }
$$

$$
+ ( a C - b D + c A + d B ) ^ { 2 } + ( a D + b C - c B + d A ) ^ { 2 } +
$$

of four squares. Evidently this completes the proof.口

For a characterization of sums of three squares, see for example [Serre, p. 79].

# § 9. A Theorem of Siegel

This section will describe a basic formula due to C.L. Siegel, concerning positive definite bilinear forms over Z. No proof will be given, but some interesting applications will be described in detail. For proofs the reader is referred to [Siegel],[Weil],[Mars].

One of the classical problems of number theory is that of giving a satisfactory formula for the number of solutions to a quadratic equation in several integer variables. For example, given a positive integer $k ,$ how many n-tuples $x _ { 1 } , . . . , x _ { n } { \in } { \mathbf { Z } }$ satisfy the equation $x _ { 1 } ^ { 2 } + \cdots + x _ { n } ^ { 2 } = k ?$ In 1881 the Paris Academy announced that its Grand Prize would be awarded to the author of the best paper on the topic“Théorie de la dé- composition des nombres entiers en une somme de cinq carrés.”The French press was outraged, two years later, when half3a of the prize was awarded to a teen-aged German student who, because of time pressure, had not even followed the rules and submitted his manuscript in the French language. However the French Academy stood firm. In his prize winning paper, Hermann Minkowski laid the groundwork for our 3aTheother prizewinnerwas H.J..SmithofOxford,whohadactuall publishedasolu present theory of quadratic forms over the integers and over the rational numbers.

This section will be concerned with Siegel's formula for the“average ” number of solutions to a quadratic equation. In order to state the formula,a number of definitions will be needed.

Let $X$ and Y be topological spaces, each provided with a measure on the $\overline { { \pmb { \sigma } } }$ -ring generated by open sets. The measure ofa set $\boldsymbol { \mathit { t } }$ will be denoted by $\operatorname { v o l } ( U ) .$ Given any continuous map $f \colon X \to Y ,$ the density of solutions to the equation $f ( x ) = y _ { 0 }$ can be measured as follows. Consider small neighborhoods $U$ of $y _ { 0 }$ ,and form the limit

$$
\operatorname* { l i m } _ { U \to y _ { 0 } } \operatorname { v o l } f ^ { - 1 } ( U ) / \operatorname { v o l } ( U ) .
$$

If this limit exists, then it will be caled the density of f-1 at yo,and denoted by $D f ^ { - 1 } ( y _ { 0 } ) .$ If this density is continuous as a function of $y _ { 0 } ,$ （24号 then evidently

$$
\intop _ { U } ^ { } D f ^ { - 1 } ( y ) d y { = } \mathrm { v o l } f ^ { - 1 } ( U )
$$

for any measurable set $U \subset Y .$ (This is a topological version of the RadonNikodym theorem.)

Example 1. Let $f$ $\mathbf { R } ^ { n } { \xrightarrow { } } \mathbf { R }$ be the quadratic function $f ( x _ { 1 } , \ldots , x _ { n } ) =$ $\textstyle { \frac { 2 } { x _ { 1 } ^ { 2 } + \cdots + x _ { n } ^ { 2 } } }$ Using the usual Lebesgue measure on $\mathbf { R } ^ { n }$ and on $\mathbf { R }$ we see that

$$
\intop _ { 0 } ^ { y } D f ^ { - 1 } ( \eta ) d \eta = \mathrm { v o l } f ^ { - 1 } [ 0 , y ]
$$

is equal to the volume of aballof radius $\sqrt { y }$ for $y > 0$ Therefore $D f ^ { - 1 } ( y )$ is equal to the derivative

$$
\frac { d } { d y } \left( \omega _ { n } \sqrt { y } ^ { n } \right) { = } \frac { 1 } { 2 } n \omega _ { n } y ^ { n / 2 - 1 } .
$$

For example

and so on, provided that $y > 0$ Evidently $D f ^ { - 1 } ( y ) = 0$ for $y < 0$ The function $D f ^ { - 1 }$ is continuous at O for $n \geq 3$ ，but is discontinuous for $n { = } 1 , 2$ ，

Example2. Let $\mathbf { Z } _ { p }$ denote the ring of $p$ -adic integers.This ring has a canonical Haar measure, in which the volume of each of the $p ^ { k }$ distinct residue classes modulo $p ^ { k }$ is equal to $p ^ { - k }$ The $n$ -fold cartesian product $\mathbf { Z } _ { p } \times \cdots \times \mathbf { Z } _ { p }$ has a corresponding product Haar measure. Defining $f _ { p } \colon { \mathbf { Z } } _ { p } \times \cdots \times { \mathbf { Z } } _ { p } \to { \mathbf { Z } } _ { p }$ by $f _ { p } ( x _ { 1 } , \ldots , x _ { n } ) = x _ { 1 } ^ { 2 } + \cdots + x _ { n } ^ { 2 }$ ，we can again form the density $D f _ { p } ^ { - 1 } \colon \mathbf { Z } _ { p }  \mathbf { R }$ .

Let $u$ be any $p$ -adic unit. Then the transformation $( x _ { 1 } , \ldots , x _ { n } ) \mapsto$ （2014号 $( u x _ { 1 } , \ldots , u x _ { n } )$ is continuous and volume preserving. Since

$$
\begin{array} { r } { f _ { p } ( u x _ { 1 } , \ldots , u x _ { n } ) = u ^ { 2 } f _ { p } ( x _ { 1 } , \ldots , x _ { n } ) , } \end{array}
$$

it follows that $D f _ { p } ^ { - 1 } ( u ^ { 2 } y )$ is equal to $D f _ { p } ^ { - 1 } ( y )$ In particular, for every $y \ne 0$ in $\mathbf { Z } _ { p }$ the function $D f _ { p } ^ { - 1 }$ is constant throughout $^ { a }$ neighborhood of y.

Here is an explicit formula for $D f _ { p } ^ { - 1 }$ .To simplify the discussion we consider only the case n even, say $n { = } 2 m$ .Recall that every element $y \ne 0$ in $\mathbf { Z } _ { p }$ can be written uniquely as a product $p ^ { v } u$ where $v$ is a non-negative integer and $\pmb { u }$ is a p-adic unit.

(9.1) Lemma. $\underline { { L e t \ f _ { p } { : } \mathbf Z _ { p } { \times } \dots { \times } \mathbf Z _ { p } } } \to \mathbf Z _ { p } \ b e \ t h e \ f u n c t i o n \ f _ { p } ( x _ { 1 } , \dots , x _ { 2 m } )$   
$= x _ { 1 } ^ { 2 } + \cdots + x _ { 2 m } ^ { 2 }$ of 2m $p$ -adic variables. Let $\overline { { r = p ^ { 1 - m } } }$ and for $p$ odd let   
$\varepsilon { = } \left( \frac { - 1 } { p } \right) ^ { n }$ 1 so that ε equals $+ 1$ or $- 1$ according as $p ^ { m } \equiv 1$ or $p ^ { m } \equiv - 1$   
(mod 4). If $p$ is odd then the associated density function $D f _ { p } ^ { - 1 } ( p ^ { v } u ) \ i$ s   
equal to $( 1 - \varepsilon r / p ) ( 1 + \varepsilon r + \varepsilon ^ { 2 } r ^ { 2 } + \dots + \varepsilon ^ { v } r ^ { v } ) .$

For $\scriptstyle p = 2$ and m even it is equal to

$$
1 + ( - 1 ) ^ { m / 2 } ( r + r ^ { 2 } + \cdots + r ^ { v - 1 } - r ^ { v } ) ,
$$

while for $p { = } 2$ and m odd it is equal to either $1 + r ^ { v + 1 }$ or $1 - r ^ { v + 1 }$ according as $m \equiv u$ or $m \equiv - u ( { \bf m o d } 4 )$

The proof will be given at the end of this section. The formulas for n odd are slightly more complicated.

Note that $D f _ { p } ^ { - 1 } ( y )$ tends to 1 as $m \to \infty$ .Furthermore, if m≥2, note that $D f _ { p } ^ { - 1 } ( y )$ tends to 1uniformly as $p  \infty$

It will be convenient to unify our notations by declaring that the symbol $\mathbf { Z } _ { \infty }$ shall stand for the real numbers R.Thus we have a canonical embedding $\mathbf { Z } \to \mathbf { Z } _ { p }$ for $\displaystyle p = 2 , 3 , 5 , 7 , \ldots , \infty .$

Definition (Gauss, Minkowski). Two bilinear form spaces $X$ and $Y$ over the integers belong to the same genus if the induced bilinear form space $X \otimes \mathbf { Z } _ { p }$ over $\mathbf { Z } _ { p }$ is isomorphic to $Y \otimes \mathbf { Z } _ { p }$ for every $\displaystyle p = 2 , 3 , \ldots , \infty .$ ， If X andYhave the same genus,then it is not difficult to verify that they also have the same determinant.Hence, using (1.6), we see that each genus contains only finitely many distinct spaces, up to isomorphism.

Example 3.The two bilinear form spaces $\langle 5 \rangle \oplus \langle 1 1 \rangle$ and $\langle 1 \rangle \oplus \langle 5 5 \rangle$ are both positive definite,and it is not difficult to show that the injection $\mathbf { Z } \to \mathbf { Z } _ { p }$ carries them into isomorphic spaces for every finite prime $p$ Hence these two spaces belong to the same genus. They are not isomorphic, since the equation $5 x ^ { 2 } + 1 1 y ^ { 2 } = 1$ has no integer solution.

Similarly the two inner product spaces $\langle 1 \rangle \oplus T _ { 8 }$ and $\langle 1 \rangle \oplus \cdots \oplus \langle 1 \rangle$ of rank 9 belong to the same genus, but are not isomorphic.

We are now ready to state one form of Siegel's theorem. Let $X$ be a positive definite bilinear form space of rank $n \geq 2$ over $\mathbf { Z }$

Definition. For each integer $k ,$ let $r _ { X } ( k )$ denote the number of distinct elements $\boldsymbol { x } \in \boldsymbol { X }$ satisfying the equation $x \cdot x { } = k$

For each $p$ we can form the induced space $X \otimes \mathbf { Z } _ { p }$ over $\mathbf { Z } _ { p }$ .Let

$$
f _ { p } \colon X \otimes \mathbf { Z } _ { p } \to \mathbf { Z } _ { p }
$$

denote the quadratic function $f _ { p } ( \xi ) = \xi \cdot \xi .$ ，

(9.2) Siegel's theorem (preliminary version). If the genus of $X$ contains only one isomorphism class,then

$$
r _ { X } ( k ) { = } \varepsilon \prod _ { p = 2 , 3 , \ldots , \infty } D f _ { p } ^ { - 1 } ( k )
$$

for every integer k≠O,where the coefficientεis defined to be or1according $\scriptstyle a s n = 2 o r n > 2 .$

For the proof, which is not easy,we refer to [Siegel, pp.326-366]. This theorem remains true in the indefinite case, but is not interesting since both sides of the equation are usually infinite.

The product on the right is absolutely convergent if $n \geq 4$ .In the cases $n { = } 2 , 3$ , care must be taken to multiply the factors in the usual order.

Example 4. The inner product space $\langle 1 \rangle \oplus \langle 1 \rangle \oplus \dots \oplus \langle 1 \rangle$ of rank 8 satisfies the hypothesis of (9.2). Let $v _ { p } = v _ { p } ( k )$ denote the exponent of the highest power of $p$ dividing $k .$ Then, by (9.1),

$$
D f _ { p } ^ { - 1 } ( k ) { = } ( 1 { - } p ^ { - 4 } ) ( 1 { + } p ^ { - 3 } + p ^ { - 6 } + \cdots + p ^ { - 3 } v _ { p } )
$$

for $p$ odd, and

$$
D f _ { 2 } ^ { - 1 } ( k ) = 1 + 2 ^ { - 3 } + 2 ^ { - 6 } + \cdots + 2 ^ { - 3 ( v _ { 2 } - 1 ) } - 2 ^ { - 3 v _ { 2 } }
$$

for $p { = } 2 .$ (1f $v _ { 2 } = 0$ ,this formula reads $D f _ { 2 } ^ { - 1 } ( k ) = 1 .$ )Furthermore

$$
D f _ { \infty } ^ { - 1 } ( k ) { = } 4 \omega _ { 8 } k ^ { 3 } { = } { \pi } ^ { 4 } k ^ { 3 } / 6
$$

by Example 1. Taking the product over $\scriptstyle p = 2 , 3 , \ldots , \infty .$ we obfain an infinite product

$$
C = { \frac { 1 } { 6 } } \pi ^ { 4 } ( 1 - 3 ^ { - 4 } ) ( 1 - 5 ^ { - 4 } ) ( 1 - 7 ^ { - 4 } ) . . .
$$

which does not depend on $k _ { \mathrm { { ; } } }$ ,multiplied by a finite product

$$
k ^ { 3 } \prod _ { p \mid k } ( 1 + p ^ { - 3 } + p ^ { - 6 } + \cdots \pm p ^ { - 3 v _ { p } } )
$$

which depends explicitly on $k$ ， Multiplying out this last expression, we obtain

$$
k ^ { 3 } \sum _ { d \mid k } \pm d ^ { - 3 } = \sum _ { d \mid k } \pm d ^ { 3 } ,
$$

where the sign of the summand $d ^ { 3 }$ turns out to be $( - 1 ) ^ { d + k }$

As for the constant $C$ ,evaluating $r _ { X } ( k )$ at $k = 1$ we see that $C = 1 6$ Or alternatively, in terms of the Riemann zeta function we can write

$$
C = { \textstyle \frac { 1 } { 6 } } \pi ^ { 4 } ( 1 - 2 ^ { - 4 } ) ^ { - 1 } \prod _ { p \mathrm { f i n i t e } } ( 1 - p ^ { - 4 } ) = { \textstyle \frac { 1 } { 6 } } \pi ^ { 4 } { \textstyle \frac { 1 6 } { 1 5 } } \zeta ( 4 ) ^ { - 1 } .
$$

Substituting the known identity

$$
\zeta ( 4 ) = \pi ^ { 4 } / 9 0
$$

(see for example [Serre, p.148]), we again obtain $C = 1 6 .$ Thus we have derived the following.

Formula of Jacobi. For any positive integer $k$ ,the number ofrepresentations ofk as a sum of eight squares is equal tc $\frac { \mid 6 \sum _ { d \mid k } ( - 1 ) ^ { d + k } d ^ { 3 } } { d \mid k }$

We leave the corresponding formulas for sums of two, four, or six squares as exercises for the reader.

Now consider an arbitrary genus $G$ of positive definite bilinear form spaces. Then $G$ contains say $g$ distinct isomorphism classes,where $g$ is a positive integer. Let $X _ { 1 } , \ldots , X _ { g }$ be representatives for these various isomorphism classes.Following Eisenstein,we weight the various isomorphism classes according to their lack of symmetry.More precisely, let $\displaystyle | \theta ( X _ { i } ) |$ denote the order of the orthogonal group consisting of all automorphisms of $X _ { i }$ . Defining

$$
w _ { i } { = } | O ( X _ { i } ) | ^ { - 1 } \Biggl / \sum _ { j { = } 1 } ^ { g } | O ( X _ { j } ) | ^ { - 1 } ,
$$

we obtain positive rational numbers $w _ { 1 } , \ldots , w _ { g }$ with $w _ { 1 } + \cdots + w _ { g } = 1$

Let $f _ { p } \colon X _ { 1 } \otimes \mathbf { Z } _ { p } \to \mathbf { Z } _ { p }$ be the quadratic functions $f _ { p } ( x ) = x \cdot x$ ,as above.

(9.3) Siegel's theorem (second version). For any $k \neq 0 ,$ the weighted average $w _ { 1 } r _ { X _ { 1 } } ( k ) + \cdots + w _ { g } r _ { X _ { g } } ( k )$ is equal to ε $D f _ { p } ^ { - 1 } ( k )$ whereε p=2,3,.,8 equals $\textstyle { \frac { 1 } { 2 } }$ or 1 according as the rank is 2 or greater than 2.

Suppose for example that $X _ { 1 }$ is the inner product space $\langle 1 \rangle \oplus \cdots \oplus \langle 1 \rangle$ of rank n. Then the genus $G$ consists of all positive definite inner product spaces of type I and rank $\pmb { n }$ .We denote this genus by the symbol $I _ { n }$ ：

f $n$ is large,then the finite primes contribute very little to the product $\Pi { \cal D } f _ { p } ^ { - 1 } ( k )$ The factor

$$
\overline { { { D f _ { \infty } ^ { - 1 } ( k ) = \frac { 1 } { 2 } n \omega _ { n } k ^ { n / 2 - 1 } } } }
$$

is dominant. Here is a very crude estimate.

(9.4) Lemma. If $f _ { p } ( x _ { 1 } , \ldots , x _ { n } ) { = } \sum x _ { i } ^ { 2 }$ with $n \geq 8 ,$ ,then the product over all finite primes of $D f _ { p } ^ { - 1 } ( k )$ lies between $\frac { 5 } { 6 }$ and $\frac { 6 } { 5 }$

The proof will be given later.

Hence the average $w _ { 1 } r _ { X _ { 1 } } ( k ) + \cdots + w _ { g } r _ { X _ { g } } ( k )$ lies between $\scriptscriptstyle { \frac { 5 } { 1 2 } n \omega _ { n } k ^ { n / 2 - 1 } }$ and n n kn/2-1.

J.H.Conway and J.Thompson have pointed out (unpublished) that Siegel’s theorem can be used to prove an analogue of the MinkowskiHlawka Theorem (7.2) for inner product spaces (i.e., self-dual lattices) over $\mathbf { Z }$ ：

For each $n > 0$ let $k ( n )$ denote the closest integer to ${ \bigl ( } { \frac { 5 } { 3 } } \omega _ { n } ^ { - 1 } { \bigr ) } ^ { 2 / n }$ .Clearly this integer $k ( n )$ is asymptotic to $\omega _ { n } ^ { - 2 / n } \sim n / 2 \pi e$ as $n \to \infty$

(9.5) Theorem (Conway, Thompson). For any dimension n there exists a positive definite inner product space $X$ oftypeI and rank nwith

Proof.Let $k = k ( n )$ .We may assume that $n \geq 8$ ,since $k \leq 1$ for smaller values of n. Hence Lemma (9.4) applies. If $X _ { 1 } , \ldots , X _ { g }$ are the distinct inner product spaces in the genus $I _ { n }$ ,then $\begin{array} { r } { w _ { 1 } r _ { X _ { 1 } } ( j ) + \cdots + \overset { \circ } { w _ { g } } r _ { X _ { g } } ( j ) < \frac { 6 } { 1 0 } n \omega _ { n } j ^ { n / 2 - 1 } . } \end{array}$ Summing over $j = 1 , 2 , \ldots , k - 1 .$ ,and using the inequality

which is valid for $m \geq 1 ,$ ， we see that the weighted average

$$
\sum _ { i = 1 } ^ { g } w _ { i } \big ( r _ { X _ { i } } ( 1 ) + r _ { X _ { i } } ( 2 ) + \cdots + r _ { X _ { i } } ( k - 1 ) \big )
$$

is less than

$$
\begin{array} { c } { { \frac { 6 } { 1 0 } n \omega _ { n } \displaystyle \int _ { 0 } ^ { k - \frac { 1 } { 2 } } t ^ { n / 2 - 1 } d t = \frac { 6 } { 5 } \omega _ { n } ( k - \frac { 1 } { 2 } ) ^ { n / 2 } . } } \end{array}
$$

$$
\begin{array} { r } { k - \frac { 1 } { 2 } \leq ( \frac { 5 } { 3 } \omega _ { n } ^ { - 1 } ) ^ { 2 / n } . } \end{array}
$$

Therefore this upper bound is less than or equal to $\begin{array} { r } { \frac { 6 } { 5 } \omega _ { n } \frac { 5 } { 3 } \omega _ { n } ^ { - 1 } = 2 . } \end{array}$ Since the weighted average is less than 2,there must exist some particular inner product space $X = X _ { i }$ so that

$$
r _ { X } ( 1 ) + r _ { X } ( 2 ) + \cdots + r _ { X } ( k - 1 ) < 2 .
$$

![](images/735d82189daa8a5b2ab65d6debc278641db9116e835895ceb12cc0feaf5ddf63.jpg)

To prove the first statement, we note that $L \otimes L _ { 8 }$ can be described as the set of all elements $u _ { 1 } \otimes e _ { 1 } + \cdots + u _ { 8 } \otimes e _ { 8 }$ in $\mathbf { R } ^ { n } \otimes \mathbf { R } ^ { 8 }$ for which

$$
u _ { i } \in \frac { 1 } { 2 } \cal { L } , ~ u _ { 1 } \equiv u _ { 2 } \equiv \cdots \equiv u _ { 8 } \bmod { L } , ~ \mathrm { a n d } ~ u _ { 1 } + \cdots + u _ { 8 } \in 2 \cal { L } .
$$

Suppose that $\overline { { \boldsymbol { x } = \sum { u _ { i } \otimes \boldsymbol { e } _ { i } } } }$ is a non-zero element of $L \otimes L _ { 8 }$ . If $\overline { { u _ { 1 } , \ldots , u _ { 8 } \in 2 L , } }$ then

$$
\begin{array} { r } { x \cdot x = \sum u _ { i } \cdot u _ { i } \geq m ( 2 L ) = 4 m ( L ) . } \end{array}
$$

If one of the $u _ { i }$ belongs to $L$ but not to $2 L$ ,then some other, say $u _ { j }$ ,must also belong to $L$ but not to $2 L$ ; hence $u _ { i } \ne 0 , u _ { j } \ne 0 ,$ and

$$
x \cdot x \geq u _ { i } u _ { i } + u _ { j } \cdot u _ { j } { \geq } 2 m ( L ) .
$$

Finally, if some $u _ { i }$ does not belong to $L$ ,then $u _ { j } \ne 0$ for all $j ,$ and therefore

$$
x \cdot x \geq 8 m ( { \textstyle { \frac { 1 } { 2 } } } L ) = 2 m ( L ) .
$$

Thus $m ( L \otimes T _ { 8 } ) \mathop { \geq } 2 m ( L ) .$ and it clearly follows that equality holds.

As an example, consider the tensor product of $k$ copies of ${ \cal { F } } _ { 8 }$ . It evidently follows inductively that $m ( { \cal I } _ { 8 } \otimes \cdots \otimes { \cal I } _ { 8 } ) { = } 2 ^ { k }$

To prove the second statement, let $L$ be any lattice in $\mathbf { R } ^ { n }$ and let $L ^ { \# }$ denote the dual lattice consisting of all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ with ${ \boldsymbol { x } } \cdot { \boldsymbol { L } } { \subset } \mathbf { Z }$ .The tensor product $L \otimes L ^ { \# }$ is canonically isomorphic to $\mathrm { H o m } ( L , L )$ so $L \otimes L ^ { \# }$ contains a distinguished element $e$ corresponding to the identity map of $L$ In terms of a basis $b _ { 1 } , \ldots , b _ { n }$ and dual basis $b _ { 1 } ^ { \# } , \ldots , b _ { n } ^ { \# }$ one has

$$
\begin{array} { r } { e = b _ { 1 } \otimes b _ { 1 } ^ { \# } + \cdots + b _ { n } \otimes b _ { n } ^ { \# } . } \end{array}
$$

A short computation shows that $e \cdot e { = } n$ .Therefore

$$
m ( L \otimes L ^ { \# } ) { \leq } n .
$$

Now let us apply (9.5). For any $n$ there exists an inner product space (that is a self-dual lattice) $L = L ^ { \# }$ with

$$
m ( L ) \geq k ( n ) \sim n / 2 \pi e .
$$

For large n this is evidently greater than √n. In fact,if n>(2πe)²= 291.708.. then computation shows that $k ( n ) { \dot { > } } { \sqrt { n } }$ Thus, choosing L with

$$
m ( L ) { = } m ( L ^ { \# } ) { > } \sqrt { n } ,
$$

it follows that

$$
m ( L ) m ( L ^ { \# } ) { > } n { \geq } m ( L \otimes L ^ { \# } ) ,
$$

which completes the proof.□

Now let us describe a still more general version of Siegel's formula. Instead of solving a single equation ${ \boldsymbol { x } } \cdot { \boldsymbol { x } } = k$ , suppose that we try to solve a collection of $t ( t + 1 ) / 2$ simultaneous equations of the form

$$
\boldsymbol { x } _ { i } \cdot \boldsymbol { x } _ { j } = K _ { i j }
$$

where $K = ( K _ { i j } )$ is a fixed symmetric $t \times t$ matrix of integers and $x _ { 1 } , \ldots , x _ { t }$ are unknown elements of $X$ . We assume that $1 \leq t \leq n$ Let $r _ { X } ( K )$ denote the number of solutions.In other words $r _ { X } ( K )$ is the number of elements in $f ^ { - 1 } ( K ) ;$ where

is the quadratic function $f ( x _ { 1 } , \ldots , x _ { t } ) = ( x _ { i } \cdot x _ { j } )$ Just as above, we can tensor everything with $\mathbf { Z } _ { p }$ ,and form a corresponding $p$ -adic function $f _ { p }$ (9.7) Siegel's theorem (final version).The weighted average

$$
w _ { 1 } r _ { X _ { 1 } } ( K ) + \cdots + w _ { g } r _ { X _ { g } } ( K ) ,
$$

where $X _ { 1 } , \ldots , X _ { g }$ represent the distinct isomorphism classes in the genus of $X = X _ { 1 }$ ,is equal to

$$
\frac { - ( \varepsilon _ { n - t - 1 } / \varepsilon _ { n - 1 } ) \prod _ { p = 2 , 3 , \ldots , \infty } \varepsilon _ { n - t } { \cal D } f _ { p } ^ { - 1 } ( K ) , } { p = 2 , 3 , \ldots , \infty }
$$

where the coeffcient ε is equal to ifi=O,and to 1 ifi≠0.

Evidently this reduces to the previous theorem in the case $n > t = 1$

By way of contrast, let us look at the case $n { = } t { > } 1 .$ Choosing a basis $b _ { 1 } , \ldots , b _ { n }$ for $X _ { 1 }$ ，suppose that $K _ { 1 }$ is the matrix $( \boldsymbol { b } _ { i } \cdot \boldsymbol { b } _ { j } )$ Then $r _ { X _ { 1 } } ( K _ { 1 } )$ is evidently equal to the number $| O ( X _ { 1 } ) |$ of automorphisms of $X _ { 1 }$ ，while $r _ { X _ { i } } ( \dot { K _ { 1 } } ) { = } 0$ for $i > 1$ Thus the weighted average $\sum w _ { i } r _ { X _ { i } } ( K _ { 1 } )$ reduces to $w _ { 1 } | \boldsymbol { O } ( X _ { 1 } ) |$ But by definition

$$
w _ { 1 } { = } | O ( X _ { 1 } ) | ^ { - 1 } / \sum _ { j } | O ( X _ { j } ) | ^ { - 1 } .
$$

Therefore the weighted average is equal to the expression

$$
\left( \sum _ { j = 1 } ^ { g } | O ( X _ { j } ) | ^ { - 1 } \right) ^ { - 1 }
$$

which depends only on the genus $\textbf { \textit { G } }$ Classically the reciprocal is called the mass associated with the genus $G$ .Thus we have a more or less effective formula $M ( G ) = \prod _ { p = 2 , . . . , \infty } \bar { ( \frac { 1 } { 2 } D f _ { p } ^ { - 1 } ( K _ { 1 } ) ) ^ { - 1 } }$ for computing the mass associated with any genus of positive definite spaces over $\mathbf { Z }$

Note the basic inequality $g \geq 2 M ( G ) ,$ where $g$ is the number of distinct   
isomorphism classes in $G .$ ，This is evident since each automorphism   
group $O ( X )$ contains at least two distinct elements (namely 1 and -1). As an example, consider the genus $I _ { n }$ consisting of all positive definite   
inner product spaces of type I and rank n. Then the function $M ( I _ { n } )$ is   
plotted in Fig.4, on a highly condensed logarithmic scale. For small

![](images/fc624a4b29abcf32869e3a552e6d114b006e5cf7605df531946f600b11cec887.jpg)  
Fig. 4. The mass $M ( I _ { n } )$ of the genus ${ \cal I } _ { n }$ plotted on a logarithmic scale as a function of $\pmb { n }$

values of $n$ the mass $M ( I _ { n } )$ is very close to zero. For example if $n { \le } 8$ then $M ( I _ { n } )$ is just the reciprocal of the number $n ! 2 ^ { n }$ of automorphisms of the $n$ -fold sum $\langle 1 \rangle \oplus \cdots \oplus \langle 1 \rangle$ .But for larger values of $n$ the mass $M ( I _ { n } )$ is a very large number. Thus computation shows that

![](images/60cec0235648fe88c388ed1f28c9165922e0f2eb1cacb750f3076715bbc6dbb9.jpg)

Hence there are at least 2O9 distinct isomorphism classes in $I _ { 2 8 }$ , at least 297185in $I _ { 2 9 }$ , and so on. The number $M ( I _ { n } )$ is asymptotic to

$$
C ( n / 2 \pi e \sqrt { e } ) ^ { n ^ { 2 } / 4 } ( 8 \pi e / n ) ^ { n / 4 } / \sqrt [ 2 ] { n }
$$

as ${ \underline { { n \to \infty } } }$ ， where the constant $C$ is approximately 0.705, and $2 \pi e \sqrt { e } =$ 28.159...

The actual details of the computation of $M ( I _ { n } )$ are rather tedious. We mention merely that the factors $\scriptstyle { \frac { 1 } { 2 } } D f _ { p } ^ { - 1 } ( I )$ coming from finite primes are reasonable close to 1,and contribute very little to the final result. The manic behavior of the function $n \mapsto M ( I _ { n } )$ is entirely due to the single factor ${ \scriptstyle { \frac { 1 } { 2 } } } D f _ { \infty } ^ { - 1 } ( I )$ .This factor can be computed by the formula

Further details will be omitted.

Similar computations can be carried out for spaces of type II. Compare [Serre, p. 94].

To conclude this section we must prove Lemmas (9.1) and (9.4). Let $N _ { n } ( a )$ denote the number of solutions to the congruence

$$
x _ { 1 } ^ { 2 } + \ldots + x _ { n } ^ { 2 } \equiv a { \pmod { p } } ,
$$

where $p$ is a fixed odd prime. In [Siegel, p.344] such numbers are computed by an ingeneous Gauss sum argument. We will use an alternative method.

Let $( a / p )$ be the Legendre symbol, equal to $+ 1$ or $- 1$ according as $a$ is or is not a quadratic residue modulo $p$ .It will be convenient to extend the usual definition by agreeing that $( a / p ) { = } 0$ whenever $a \equiv 0$ $( \mathbf { m o d } p )$ ，With this convention, the number $N _ { 1 } ( a )$ of solutions to the congruence

is evidently equal to $1 + ( a / p )$

To compute $N _ { 2 } ( a )$ we use the identity

Substituting $1 + ( x / p ) \mathrm { f o r } N _ { 1 } ( x )$ this yields

$$
N _ { 2 } ( a ) { = } \displaystyle \sum _ { x + y \equiv a } \left( 1 + \left( { \frac { x } { p } } \right) + \left( { \frac { y } { p } } \right) + \left( { \frac { x y } { p } } \right) \right) .
$$

But clearly the sum of $( x / p )$ over all residue classes $x$ modulo $p$ is equal to zero.Hence:

$$
N _ { 2 } ( a ) { = } p { + } 0 { + } 0 { + } \sum _ { x + y \equiv a } \left( { \frac { x y } { p } } \right) .
$$

First suppose that $\overline { { a = 0 } }$ . Then each summand $\scriptstyle \left( { \frac { x y } { p } } \right) = \left( { \frac { - x ^ { 2 } } { p } } \right)$ is equal t0 $\Big ( \frac { - 1 } { p } \Big )$ 证 $x \not \equiv 0 ( { \mathrm { m o d } } p ) .$ ,and is zero if ${ x } \equiv \mathbf { 0 }$ Therefore

$$
N _ { 2 } ( 0 ) { = } p + ( p - 1 ) \left( { \frac { - 1 } { p } } \right) .
$$

On the other hand if $^ { a }$ is relatively prime to $p$ then the sum

is independent of $^ { a }$ For if $x + y \equiv a$ then $u x + u y \equiv u a$ and

$$
\left( { \frac { u x u y } { p } } \right) = \left( { \frac { x y } { p } } \right)
$$

for any u relatively prime to $p$ Thus

But the sum

$$
{ \cal N } _ { 2 } ( 1 ) { = } { \cal N } _ { 2 } ( 2 ) { = } { \cdots } { = } { \cal N } _ { 2 } ( p - 1 ) .
$$

$$
N _ { 2 } ( 0 ) + N _ { 2 } \left( 1 \right) + \cdots + N _ { 2 } \left( p - 1 \right)
$$

is clearly equal to $p ^ { 2 }$ , the total number of pairs $( x _ { 1 } , x _ { 2 } )$ mod $p$ .Therefore

$$
N _ { 2 } \left( u \right) = N _ { 2 } \left( 1 \right) = \left( p ^ { 2 } - N _ { 2 } \left( 0 \right) \right) / ( p - 1 )
$$

for any relatively prime residue class $u$ modulo $p$ Substituting (1), we obtain the formula

$$
\cdot \frac { N _ { 2 } \left( u \right) = p - \left( \frac { - 1 } { p } \right) . } { p }
$$

$s { = } \left( \frac { - 1 } { p } \right) p ^ { - 1 } ,$

and

$$
N _ { 2 } ( u ) { = } p ( 1 { - } s )
$$

$$
\ N _ { 2 } ( 0 ) { = } N _ { 2 } ( u ) { + } p ^ { 2 } s .
$$

$$
{ N _ { 2 m + 2 } } ( a ) \mathrm { { = } } \sum _ { x + y \equiv a } { N _ { 2 m } ( x ) N _ { 2 } ( y ) }
$$

a straightforward induction on m shows that

$$
N _ { 2 m } ( u ) { = } p ^ { 2 m - 1 } ( 1 - s ^ { m } )
$$

$$
\scriptstyle N _ { 2 m } ( 0 ) = N _ { 2 m } ( u ) + p ^ { 2 m } s ^ { m }
$$

for every positive integer m.

More generally， let $N _ { n } ( a { \bmod { p ^ { k } } } )$ denote the number of n-tuples $x _ { 1 } , \ldots , x _ { n }$ modulo $p ^ { k }$ satisfying the congruence

$$
x _ { 1 } ^ { 2 } + \cdots + x _ { n } ^ { 2 } \equiv a { \pmod { p ^ { k } } } .
$$

These numbers can be computed as follows. We will assume that $a = p ^ { v } u$ with $v < k ,$ where $u$ is relatively prime to $p$

$$
p ^ { ( n - 1 ) ( k - 1 ) } N _ { n } ( u ) .
$$

For each solution to the congruence

$$
\xi _ { 1 } ^ { 2 } + \dots + \xi _ { n } ^ { 2 } \equiv u { \pmod { p } }
$$

gives rise to precisely $p ^ { ( n - 1 ) ( k - 1 ) }$ solutions modulo $p ^ { k }$ . To see this, note that the $\xi _ { i }$ cannot all be divisible by $p$ If say $\xi _ { 1 }$ 丰0(mod p), then choosing any residue classes $\mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { n }$ modulo $p ^ { k }$ with

$$
x _ { 2 } \equiv \xi _ { 2 } , \ldots , x _ { n } \equiv \xi _ { n } { \pmod { p } } ,
$$

it follows easily that the residue class of $x _ { 1 }$ modulo $p ^ { k }$ is uniquely determined.

Case 2. Even if $v \geq 1$ there may still be solutions to the congruence

$$
\xi _ { 1 } ^ { 2 } + \dots + \xi _ { n } ^ { 2 } \equiv p ^ { v } u \equiv 0 ( { \bmod { p } } )
$$

in which the $\xi _ { i }$ are not all divisible by $p$ .The total number of such solutions is equal to Nn(O)-1. Proceeding as in Case 1, the number of solutions to (5) in which the $x _ { i }$ are not all divisible by $p$ is equal to $p ^ { ( n - 1 ) ( k - 1 ) } \bigl ( N _ { n } ( 0 ) - 1 \bigr ) .$

$C a s e 3 . \mathrm { ~ H ~ } v \geq 2 ,$ then the Eq.(5) may have solutions in which all of the $\boldsymbol { \mathbf { \check { x } } } _ { i }$ are divisible by $p$ .The total number of such solutions is equal to

$$
p ^ { n } N _ { n } ( p ^ { v - 2 } u \mod p ^ { k - 2 } ) ,
$$

since every solution to the congruence

$$
\xi _ { 1 } ^ { 2 } + \dots + \xi _ { n } ^ { 2 } \equiv p ^ { v - 2 } u { \pmod { p ^ { k - 2 } } }
$$

gives rise to precisely $p ^ { n }$ solutions to (5) satisfying the conditions

$$
x _ { 1 } \equiv p \xi _ { 1 } , \ldots , x _ { n } \equiv p \xi _ { n } { \pmod { p ^ { k - 1 } } } .
$$

Combining Cases 1, 2, 3 with the explicit formulas (3) and (4) for $\mathrm { N } _ { 2 m } ( u )$ and ${ \cal N } _ { 2 m } ( 0 ) ;$ ,a straightforward induction on $v$ now produces the following conclusion.

(9.8) Lemma. If $0 \leq v < k ,$ ，then the number $N _ { 2 m } ( p ^ { v } u$ mod $p ^ { k } .$ of solutions to the congruence

$$
x _ { 1 } ^ { 2 } + \cdots + x _ { 2 m } ^ { 2 } { \equiv } p ^ { v } u { \pmod { p ^ { k } } }
$$

is equal to

$$
p ^ { ( 2 m - 1 ) k } ( 1 - s ^ { m } ) ( 1 + p s ^ { m } + p ^ { 2 } s ^ { 2 m } + \cdots + p ^ { v } s ^ { v m } ) ,
$$

Proof of Lemma (9.1) for $p$ odd. Let $D f _ { p } ^ { - 1 } \colon \mathbf { Z } _ { p } {  } \mathbf { R }$ be the density function associated with $f _ { p } ( x _ { 1 } , . . . , x _ { 2 m } ) { = } x _ { 1 } ^ { 2 } + \dots + x _ { 2 m } ^ { 2 }$ . Comparing the definition of $D f _ { p } ^ { - 1 }$ with (9.8), it follows easily that

$$
D f _ { p } ^ { - 1 } ( p ^ { v } u ) { = } ( 1 { - } s ^ { m } ) ( 1 { + } p s ^ { m } + p ^ { 2 } s ^ { 2 m } + \cdots + p ^ { v } s ^ { v m } ) .
$$

![](images/3118c551b3607b80b6250efc946b03752d49114331bb0b29a2ae341b7355052c.jpg)

as $v \to \infty$ (or as $p ^ { v } u  0 \AA$ . Similarly, for $p { = } 2$ the function

$$
\delta _ { 8 , 2 } ( 2 ^ { v } u ) = 1 + 8 ^ { - 1 } + 8 ^ { - 2 } + \cdots + 8 ^ { 1 - v } - 8 ^ { - v }
$$

attains its minimum $\frac { 7 } { 8 }$ when $v = 1 ,$ , and tends to its maximum $\frac { 8 } { 7 }$ as $v \to \infty$

where $k$ varies over $\mathbf { z }$ ,attains its minimum

$$
{ \frac { 7 } { 8 } } \prod _ { p { \ o d } { \bf d } } ( 1 - p ^ { - 4 } ) = { \frac { 1 4 } { 1 5 } } \zeta ( 4 ) ^ { - 1 } = 0 . 8 6 2 . . .
$$

at $k = 2 ,$ ,and its maximum

$$
{ \frac { 8 } { 7 } } \prod _ { p \ o d 8 } ( 1 - p ^ { - 4 } ) / ( 1 - p ^ { - 3 } ) = { \frac { 1 6 } { 1 5 } } \zeta ( 3 ) / \zeta ( 4 ) = 1 . 1 8 4 . . .
$$

at $k { = } 0$ . Since these bounds lie between $\frac { 5 } { 6 }$ and $\frac { 6 } { 5 }$ ， this completes the proof of (9.4) for the case $n = 8$

But any upper or lower bound for $\delta _ { 8 , p }$ is automatically an upper or lower bound for $\delta _ { n , p }$ for any $n \geq 8 .$ 、In fact, dividing both sides of the identity

$$
\frac { N _ { m + n } ( a \bmod p ^ { k } ) = \sum _ { x + y \equiv a ( \bmod p ^ { k } ) } N _ { m } ( x \bmod p ^ { k } ) N _ { n } ( y \bmod p ^ { k } ) } { x + y \equiv a ( \bmod p ^ { k } ) }
$$

by $p ^ { ( m + n - 1 ) k }$ and passing to the limit as $k \to \infty$ we obtain the con  
volution formula $\delta _ { m + n } ( a ) = \int \delta _ { m } ( x ) \delta _ { n } ( a - x ) d x .$

Thus, if $\delta _ { 8 } ( x ) { \leq } c$ for all $x _ { i }$ , it follows immediately that

$$
\delta _ { m + 8 } ( a ) { \leq } \int \delta _ { m } ( x ) c d x { = } c
$$

for all $^ { a }$ .This completes the proof.□

# Chapter III. Inner Product Spaces over a Field

This chapter will describe some of the highlights of the theory of the Witt ring $W ( { \boldsymbol { F } } ) _ { : }$ where $F$ is an arbitrary field. We are particularly careful to give proofs which are valid also in characteristic 2. The classical theory for number fields,as described for example in [O'Meara], is largely ignored.

All inner product spaces are to be symmetric.

# S1. Anisotropic Inner Product Spaces

An inner product space $X$ is anisotropic if $x \cdot x { = } 0$ implies $\scriptstyle x = 0$ In this section we will show that every element in the Witt ring $W ( { \boldsymbol { F } } )$ is represented by an anisotropic inner product space which is unique up to isomorphism. First note the following.

(1.1) Lemma. Every inner product space X over F is isomorphic to an orthogonal sum $\pmb { S } \oplus \pmb { A }$ with $s$ split and A anisotropic.

Proof. If the space $X$ itself is anisotropic, then we can simply choose $\pmb { S } = \mathbf { 0 }$ 、If not, then there exists a vector $x \neq 0$ with $\mathbf { \boldsymbol { x } } \cdot \mathbf { \boldsymbol { x } } = 0$ ,and we can choose a vector $y$ with $x \cdot y = 1$ Then $x$ and $y$ span a subspace $s _ { 1 } \subset X$ with inner product matrix $\binom { 0 } { 1 } \frac { 1 } { * }$ . Evidently $\underline { { S } } _ { 1 }$ is split, and

Applying the same construction to $S _ { 1 } ^ { \perp }$ ，and continuing inductively,one can easily complete the proof.

Choosing such a decomposition $X \cong S \oplus A$ ，we want to show that the anisotropic summand $\pmb { A }$ is unique up to isomorphism. If the characteristic of $F$ is $\neq 2 ,$ ，then this is quite easy to prove,using Chapter I, Theorem (4.4) and Lemma (6.3). We will give a different argument which works also in characteristic 2.

Define the index of isotropy $i ( X )$ of an inner product space $X$ to be the maximal dimension of a subspace $N \subset X$ which is self-orthogonal, that is, $N \cdot N { = } 0$

(1.2) Lemma. The index of isotropy, for any inner product space $X ,$ satisfies

where the first equality holds if and only if $X$ is anisotropic,and the second holds if and only if $X$ is split.

Proof. If $N \cdot N { = } 0 $ ,then $N { \subset } N ^ { \perp }$ ,and therefore

$$
\mathbf { r k } \left( N \right) { \le } \mathbf { r k } \left( N ^ { \perp } \right) { = } \mathbf { r k } \left( X \right) { - } \mathbf { r k } \left( N \right) ,
$$

where equality holds if and only if $N { = } N ^ { \perp }$ .The argument is now straightforward.

We will need the following upper bound.

(1.3) Main lemma. If $\pmb { A }$ is anisotropic, and $X$ is an arbitrary inner product space, then

$$
i ( X \oplus A ) + i ( X ) \mathop { \leq } \operatorname { r } \mathbf { k } ( X ) .
$$

The proof will be based on the following interpretation of $i ( X \oplus A )$ We will call a linear mapping

$$
\scriptstyle f \colon X \to Y
$$

an anti-isometry if $f ( x ) \cdot f ( x ^ { \prime } ) = - x \cdot x ^ { \prime }$ for all $x$ and $\mathbf { \boldsymbol { x } } ^ { \prime }$ in $X$

(1.4) Lemma. With $X$ and $A$ as above, there exists $^ { a }$ self-orthogonal subspace $N { \Leftarrow } X \oplus A$ of rank n if and only if there exists $a$ subspace $M \subset X$ of rank $n$ and an anti-isometry $f$ $M  A$

Proof. Given such an anti-isometry $f _ { : }$ let Nc XA denote the graph of $f _ { : }$ consisting of all pairs $( x , a )$ with $\mathbf { \boldsymbol { x } } \in M$ and $f ( x ) = a$ .Given any two pairs $( x , f ( x ) )$ and $( x ^ { \prime } , f ( x ^ { \prime } ) )$ in the graph, we have

$$
( x , f ( x ) ) \cdot ( x ^ { \prime } , f ( x ^ { \prime } ) ) { = } x \cdot x ^ { \prime } + f ( x ) \cdot f ( x ^ { \prime } ) { = } 0 .
$$

Thus $N$ is self-orthogonal of rank $n _ { \mathrm { { \ell } } }$ , as required.

Conversely， given $N { \Leftarrow } X \oplus A$ with $N \cdot N { = } 0 $ ，note that $N$ intersects the anisotropic subspace $\mathbf { 0 } \oplus \mathbf { A }$ in the zero vector only. If the pairs $( x , a )$ and $( x , a ^ { \prime } )$ both belong to $\mathbf { \delta } _ { N } ,$ it follows that $\boldsymbol { a } = \boldsymbol { a } ^ { \prime }$ Thus $N$ can be identified with the graph of a linear mapping $f \colon M \to A$ for some submodule $M \in X ;$ and since N is self-orthogonal it follows that $f$ is an anti-isometry.0

Proof of (1.3); by induction on the rank of $X \oplus A$ . We may assume that $A \ne 0$ since if $A = 0$ the inequality follows from (1.2).

Given an anti-isometry $f$ ： $M  A$ with $M \subset X$ ，we must find an upper bound for the rank of $M$ Let $M _ { 0 }$ denote the kernel of $f ,$ and let $\overline { { M _ { 1 } } }$ denote a complementary direct summand, so that

$$
M = M _ { 0 } + M _ { 1 } , \theta = M _ { 0 } \cap M _ { 1 } .
$$

Then $M _ { 1 }$ maps injectively into $A$ $M _ { 1 }$ is anisotropic. Therefore the inner product, restricted to $M _ { 1 }$ , is again an inner product; and

$$
X \cong M _ { 1 } ^ { \bot } \oplus M _ { 1 } .
$$

Applying the induction hypothesis,we conclude that

$$
i ( X ) + i ( M _ { 1 } ^ { \bot } ) { \leqq } \mathrm { r } \mathrm { k } ( M _ { 1 } ^ { \bot } ) .
$$

But $M _ { 0 } \cdot M { = } 0 , { \textnormal { s o } } M _ { 0 }$ is a self-orthogonal subspace of $M _ { 1  } ^ { \bot }$ and

$$
\mathbf { r k } ( M _ { 0 } ) { \underline { { \leq } } } i ( M _ { 1 } ^ { \pm } ) .
$$

Adding these two inequalities, and adding $\mathbf { r k } ( M _ { 1 } ) - i ( M _ { 1 } ^ { \bot } )$ to both sides, we obtain

$$
i ( X ) + \operatorname { r k } ( M ) { \leq } \operatorname { r k } ( X ) .
$$

which completes the proof.□

As an example, suppose that $\mathbf { { \boldsymbol { X } } } { = } \mathbf { { \boldsymbol { S } } }$ is split. Then the inequality $i ( S \oplus A ) { \underline { { \leq } } } \mathbf { r } \mathbf { k } ( S ) - i ( S ) = i ( S )$ implies that $i ( S \oplus \mathbf { A } ) = i ( S ) .$

(1.5) Corollary. Suppose that an orthogonal sum $\pmb { S } \oplus \pmb { A }$ ，with $s$ split and $A$ anisotropic,is itself split.Then $A = 0$

For substituting $i ( S \oplus A ) { = } { \textstyle { \frac { 1 } { 2 } } } \mathbf { r } \mathbf { k } \left( S \oplus A \right)$ into the inequality $i ( S \oplus A ) +$ $i ( S ) { \leqq } \mathbf { r k } ( S ) ,$ weobtain ${ \scriptstyle { \frac { 1 } { 2 } } } \operatorname { r k } ( S \oplus A ) \equiv \operatorname { r k } ( S ) - i ( S ) = { \scriptstyle { \frac { 1 } { 2 } } } \operatorname { r k } ( S ) ,$ hence $\mathbf { r k } ( A )$ ≤0.□

(1.6) Corollary. An inner product space X represents the zero element ofthe Witt ring if and onlyif Xis split.

For if $X$ belongs to the Witt class of O, then there exist split spaces $s ^ { \prime }$ and $S ^ { \prime \prime }$ so that

$$
X \oplus S ^ { \prime } \cong 0 \oplus S ^ { \prime \prime } .
$$

Setting

$$
X \cong A \oplus S
$$

by (1.1), it follows that ${ \big . } A \oplus S \oplus S ^ { \prime }$ is split. Therefore $\scriptstyle { \big . } { \big | } = 0$ ,and $\pmb { X }$ is split.

(1.7) Theorem. Every element of the Witt ring W(F) is represented by one, and up to isomorphism only one, anisotropic inner product space.

Proof. If two anisotropic inner product spaces $A$ and $A ^ { \prime }$ belong to the same Witt class, $A \sim A ^ { \prime }$ ， then we must prove that $A \cong A ^ { \prime }$ . Consider the inner product space $B ^ { \prime } { = } \zeta - 1 \rangle { \otimes } A ^ { \prime } .$ Then $A ^ { \prime } { \oplus B ^ { \prime } }$ is split, so it follows from (1.6) that the space $A \oplus B ^ { \prime } \sim A ^ { \prime } \oplus B ^ { \prime }$ is split. Therefore, according to (1.4), there exists a subspace $M \subset A$ and an anti-isometry

$$
f \colon M \to B ^ { \prime } ,
$$

$$
\operatorname { r k } ( M ) { = } i ( A \oplus B ^ { \prime } ) { = } { \frac { 1 } { 2 } } \operatorname { r k } ( A \oplus B ^ { \prime } ) .
$$

But $M$ is anisotropic, so $f$ has trivial kernel, and

$$
\operatorname { r k } ( M ) { \leq } \operatorname { r k } ( A ) , \quad \operatorname { r k } ( M ) { \leq } \operatorname { r k } ( B ^ { \prime } ) .
$$

It follows that $\mathbf { r k } \left( M \right) = \mathbf { r k } \left( A \right) = \mathbf { r k } \left( B ^ { \prime } \right) ,$ hence $M = A$ ，and $f$ is an antiisometry from $A$ onto $B ^ { \prime }$ . Thus $A$ is anti-isometric to $B ^ { \prime }$ ,and therefore $\pmb { A }$ is isomorphic to $\pmb { A } ^ { \prime }$ ,which completes the proof.0

Thus the Witt ring W(F) can be identified with the collection of isomorphism classes of anisotropic inner product spaces over $E .$ To complete the picture, one more element of structure is needed.

(1.8) Definition. For each element w in the Witt ring $W ( F ) ,$ let $\| w \|$ denote the rank of the unique anisotropic representative for w.

Alternatively, choosing an arbitrary representative $X$ for the Witt class w. we can set

$$
\left\| w \right\| = \operatorname { r k } \left( X \right) - 2 i ( X ) .
$$

$$
\lVert \boldsymbol { w } \rVert \geq 0
$$

where equality holds only if $w = 0$ .Note also the inequalities

$$
\begin{array} { l } { \left\| w \pm w ^ { \prime } \right\| \leq \left\| w \right\| + \left\| w ^ { \prime } \right\| , } \\ { \left\| w w ^ { \prime } \right\| \leq \left\| w \right\| \left\| w ^ { \prime } \right\| } \end{array}
$$

and

# \$2. Ordered Fields

This section is mainly a review of classical results concerning ordered fields. It studies the“total signature” $\sigma ( X )$ of an inner product space over a field $F$ .Thisisacertain $\pmb { \Omega }$ -tuple of integers, $\pmb { \Omega }$ being the collection of all orderings of $F$

(2.1) Definition. An ordering of a field F is a subset Pc F\* which is closed under addition and multiplication, and satisfies

$$
P \cup ( - P ) { = } F ^ { \bullet } .
$$

The elements of $P$ are called positive (or strictly positive),and one writes $\xi > \eta$ if $\xi - \eta \in P .$

Note that the two subsets $P$ and $- \boldsymbol { P }$ are necessarily disjoint. For if both $\xi$ and $- \xi$ belonged to $P ,$ then the sum $\xi + ( - \xi )$ would have to belong to ${ \overline { { P , } } }$ contradicting the hypothesis that $P { \subset } F ^ { \bullet }$ ：

In an ordered field, every non-zero square is positive. For if $\xi \neq 0$ then either $\xi \in { \cal P } \ \mathrm { o r } - \xi \in { \cal P } ,$ and in either case it follows that $\zeta ^ { 2 } = ( - \zeta ) ^ { 2 } \in P .$

An ordered field necessarily has characteristic zero.For $1 = 1 ^ { 2 } \in { \cal P } ,$ hence every sum $1 + 1 + \cdots + 1$ belongs to $P .$ ，Therefore no such sum can equal O in $F .$

(2.2) Artin-Schreier theorem. $\pmb { A }$ field $F$ possesses an ordering if and only if-1is not $^ { a }$ sum of squares in $F .$

Proof. If $\pmb { F }$ possesses an ordering $P ,$ then 1∈P,hence -1‡P,and -1 cannot be a sum of squares.

Conversely let $F$ be a field in which $- 1$ is not a sum of squares. Byapartial ordering of $F$ we will mean any subset of $F ^ { \bullet }$ which is closed under addition and multiplication. One partial ordering $P _ { 0 }$ can be constructed as follows. Let $P _ { 0 }$ be the collection of all sums of non-zero squares in $\boldsymbol { \mathsf { { F } } }$ Then $P _ { 0 }$ is clearly closed under addition and multiplication, and if O belonged to $P _ { 0 }$ then the equation

$$
\overline { { 0 = \xi _ { 1 } ^ { 2 } + \cdots + \zeta _ { n } ^ { 2 } } }
$$

with $\boldsymbol { \xi } _ { i } \mathrm { \neq 0 }$ would imply that

$$
- 1 = ( \xi _ { 2 } / \xi _ { 1 } ) ^ { 2 } + \dots + ( \xi _ { n } / \xi _ { 1 } ) ^ { 2 } ,
$$

contradicting our hypothesis.

By Zorn's lemma, the partial ordering $\underline { { P } } _ { 0 }$ is contained in some partial ordering $P$ of $F$ which is maximal with respect to inclusion. Given $\xi \neq 0 ,$ we will prove that either $\xi \in P \ o r \ - \xi \in P .$ This will show that P is an ordering of F.Consider the subset

$$
Q { = } P \cup \xi P \cup ( P { + } \xi P )
$$

of $F$ which is additively generated by $P$ and $\xi P .$ If $Q$ contains O, then setting $0 = \pi ^ { \prime } + \xi \pi$ with $\pi ^ { \prime }$ and $\pi$ in $P$ we obtain

$$
- \xi = \pi ^ { \prime } / \pi = \pi ^ { \prime } \pi ( \pi ^ { - 1 } ) ^ { 2 } \in { \cal P } .
$$

(Every non-zero square belongs to $P$ since $P = P _ { 0 }$ .) On the other hand, if Q does not contain O then evidently $\boldsymbol { Q }$ is a partial ordering of F.But Q contains the maximal partial ordering $P ,$ s0 $Q = P ,$ and it follows that ∈P.This shows that $P$ is an ordering of $\pmb { F }$ ; which completes the proof.□

Here is an excursion for the reader.

(2.3) Exercise. Let $F$ be a field of characteristic $\neq 2 .$ Using similar methods, prove that a field element $\xi \neq 0$ can be expressed as a sum of squares if and only if $\xi \in P$ for every ordering $P$ of $F .$ (Such element $\xi$ are called“totally positive".) In particular, if $\pmb { F }$ has no orderings at all, then every element of $\pmb { F }$ is a sum of squares.

The classical case can be described as follows.

![](images/0ab6902ee298c1835362345111a82fd70ebf264d1cfe57bc6b40ef87f82947d4.jpg)

positive definite and $X ^ { - }$ negative definite. The ranks of $X ^ { + }$ and $X ^ { - }$ are isomorphism invariants of $X$

That is,these ranks do not depend on the particular choice of $X ^ { + }$ and $X ^ { - }$

Proof. Choosing an orthogonal basis $\underline { { e _ { 1 } , \ldots , e _ { r } } }$ for $X$ ,let $X ^ { + }$ be the subspace spanned by those $\boldsymbol { e } _ { i }$ for which $e _ { i } \cdot e _ { i } > 0 .$ and let $X ^ { - }$ be spanned by those $e _ { i }$ with $e _ { i } \cdot e _ { i } { < 0 }$ .Then evidently $X \cong X ^ { + } \oplus X ^ { - }$ with $X ^ { + }$ positive definite and $X ^ { - }$ negative definite.

Now let $Y$ be an arbitrary positive definite subspace of $X$ Then $Y \cap X ^ { - } = 0$ ,hence

$$
\operatorname { r k } { ( Y ) } { \leq } \operatorname { r k } { ( X ) } - \operatorname { r k } { ( X ^ { - } ) } { = } \operatorname { r k } { ( X ^ { + } ) } .
$$

Therefore rk $( X ^ { + } )$ can be characterized as the maximum possible dimension of a positive definite subspace of X. This shows that it is an isomorphism invariant of $X ,$ and completes the proof.□

Definition. The difference $\operatorname { r k } ( X ^ { + } ) - \operatorname { r k } ( X ^ { - } )$ is called the signature of the inner product space $X$ at the ordering $P .$ We will use the notation

$$
\sigma _ { P } ( X ) { \in } \mathbf { Z }
$$

for this signature. Evidently $\sigma _ { P } ( X )$ is also an isomorphism invariant of x.

In the case of an inner product space $\langle x \rangle$ of rank 1, note that the signature $\sigma _ { P } \langle \alpha \rangle$ is just what is usually called the sign of the field element $\alpha$ at the ordering $P .$ That is $\sigma _ { P } \langle \alpha \rangle$ is equal to $+ 1$ or $- 1$ according as $\pmb { \alpha }$ is positive or negative.

(2.6) Lemma. The signature $\sigma _ { P } ( X )$ depends only on the Witt class of $X$ Furthermore

$$
\sigma _ { P } ( X \circledast Y ) = \sigma _ { P } ( X ) + \sigma _ { P } ( Y ) ,
$$

Thus the signature $\sigma _ { P }$ gives rise to a well defined homomorphism from the Witt ring $W ( { \boldsymbol { F } } )$ to the ring of integers $\mathbf { Z }$

Proof. If $s$ is a split inner product space, then it follows from Chapter I, $\ S 6 . 3$ that $s$ is isomorphic to an orthogonal sum of copies of $\langle 1 \rangle \oplus \langle - 1 \rangle$ . Hence the signature $\sigma _ { P } ( S )$ is zero. [Or more directly， if （214号 $N { \subset } S$ is self-orthogonal then the argument used to prove (2.5) shows also that ${ \bf r k } ( N ) { \bf \leq } { \bf r k } ( S ^ { + } )$ and $\operatorname { r k } ( N ) { \overset { } { \leq } } \operatorname { r k } ( S ^ { - } ) . { \mathrm { ~ S o ~ } } { \mathrm { i f ~ } } \operatorname { r k } ( N ) { \overset { } { = } } { \frac { 1 } { 2 } } \operatorname { r k } ( S ) ,$ it follows that r $\operatorname { k } ( N ) { = } \operatorname { r k } ( S ^ { + } ) { = } \operatorname { r k } ( S ^ { - } ) .$ and the signature is zero.]

Now expressing $X$ and $Y$ as sums of spaces of rank 1, and using the evident identity

$$
\sigma _ { P } ( \langle \alpha _ { 1 } \rangle \oplus \dots \oplus \langle \alpha _ { r } \rangle ) { = } \sigma _ { P } \langle \alpha _ { 1 } \rangle + \dots + \sigma _ { P } \langle \alpha _ { r } \rangle ,
$$

the rest of the proof is straightforward. 0

(2.7) Corollary. Suppose that $F$ is an ordered feld in which every positive element is a square. Then $\sigma _ { P } \colon W ( F ) \to \mathbf { Z }$ is an isomorphism.

For example the Witt ring of the real numbers $\mathbf { R }$ is isomorphic to Z. The proof is straightforward from (2.5) and (2.6).□

Remark. It is shown in standard algebra texts (Lang or van der Waerden) that there is a one-to-one correspondence between orderings of a field $F$ and isomorphism classes of “real closures ” of $F .$ The real closure $F _ { P }$ associated with any ordering $P$ can be characterized as the maximal compatibly ordered algebraic extension field of $\boldsymbol { \mathsf { \Pi } }$ Every positive element of $F _ { P }$ is a square, hence the Witt ring $W ( F _ { P } )$ is isomorphic to $\mathbf { z }$ It follows easily that the signature homomorphism ${ \pmb { \sigma _ { P } } }$ ： $W ( F ) \to \mathbf { Z }$ can be identified with the natural ring homomorphism $W ( { \boldsymbol { F } } ) \to W ( { \boldsymbol { F } } _ { P } ) .$

Now consider the collection $\scriptstyle { \mathcal { Q } } = { \mathcal { Q } } ( F )$ consisting of all possible orderings of a given field $\pmb { F }$ We topologize $\pmb { \Omega }$ as follows.

Definition. For each $\xi \in F ^ { \bullet } \operatorname { l e t } U _ { \xi } \subset \Omega$ be the set of all orderings $P$ for which $\boldsymbol { \xi } \in \mathrm { P }$ Then these sets $U _ { \xi }$ generate the required topology. (In other words a subset of $\pmb { \Omega }$ is defined to be open if and only if it is a union of finite intersections of the $U _ { \xi }$ ）

(2.8) Lemma. This topological space $\pmb { \Omega }$ is compact and totally disconnected. For each inner product space $X$ over $F _ { \mathrm { { } } }$ ,the function

$$
P \mapsto \sigma _ { P } ( X )
$$

from Ω to Z is continuous.

Definition. This function $P \mapsto \sigma _ { P } ( X )$ will be called the total signature $\sigma ( X )$ of the inner product space $X .$

Proof of (2.8). First consider an inner product space $\langle \xi \rangle$ of rank 1. Then the inverse image of 1 under the total signature function

$$
P \mapsto \sigma _ { P } \langle \xi \rangle
$$

is the open set $U _ { \xi } { \subset } \Omega ,$ ,and the inverse image of -1 is the complementary open set $U _ { - \xi }$ .Thus the total signature function of $\langle \xi \rangle$ is continuous, and it follows easily that the total signature function associated with any iner produet space $X \cong ( \xi _ { 1 } ) \oplus \dots \oplus \langle \xi _ { r } \rangle$ is continuous.

Since $\pmb { \Omega }$ is the union of disjoint open sets $U _ { \xi }$ and $U _ { - \xi }$ for any $\xi \in F ^ { \bullet }$ it is easy to check that $\pmb { \Omega }$ is Hausdorff and totally disconnected. To prove compactness, we introduce the space $2 ^ { F }$ consisting of all subsets of $F$ · This is to be topologized as a cartesian product.That is we identify each subset of $\overline { F }$ with its characteristic function $F \to \{ 0 , 1 \}$ ,and hence identify $2 ^ { F }$ with a cartesian product of copies of $\{ 0 , 1 \}$ , one copy for each element of F.This product is compact by Tychonoffs theorem.

Each ordering of $F$ can be considered as an element of $2 ^ { F }$ so $\pmb { \Omega }$ is embedded as a subset of $2 ^ { F }$ . Evidently the topology which we constructed for $\pmb { \Omega }$ is precisely the relative topology which $\pmb { \Omega }$ acquires as a subset of $2 ^ { F }$ In fact $\pmb { \Omega }$ is a closed subset of $2 ^ { \bar { F } }$ .For if a subset $Q { \subset } F$ is not an ordering, then it is easy to construct a neighborhood of $Q$ in $2 ^ { F }$ which does not contain any orderings.This proves that $\pmb { \Omega }$ is compact, and completes the proof of (2.8).□

(2.9) Definition. The ring consisting of all continuous functions from $\pmb { \Omega }$ to $\mathbf { z }$ will be denoted by ${ \bf Z } ^ { \Omega }$ . Evidently, for any inner product space $\boldsymbol { X }$ over $\overline { F }$ ,the total signature function $\sigma ( X )$ is an element of this ring ${ \bf Z } ^ { \Omega }$ Since $\sigma$ is additive, multiplicative,and since $\sigma ( X )$ depends only on the Witt class of $X _ { i }$ ,we obtain a well defined ring homomorphism

$$
\overline { { { \boldsymbol { \sigma } } \colon W ( { \boldsymbol { F } } ) \to \mathbf { Z } ^ { \Omega } } } .
$$

[Of course if the set Ω is vacuous, then $\mathbf { Z } ^ { \mathcal { \Omega } }$ is the zero ring,and this construction is not particularly interesting.]

Remark. If $\pmb { \Omega }$ has more than one element, then this homomorphism $\sigma$ is not surjective. In fact the congruence

$$
\sigma _ { P } ( X ) { \equiv } \mathbf { r } \mathbf { k } ( X ) { \pmod { 2 } }
$$

clearly holds for any inner product space $X$ and any ordering $P _ { - }$ Therefore the total signature

$$
\sigma ^ { ( \boldsymbol { X } ) \in \mathbf { Z } ^ { 2 } }
$$

must be congruent to either O or 1 modulo the ideal $2 \mathbf { Z } ^ { \Omega } .$ according as the rank of $X$ is even or odd.

In order to determine the precise image of $\sigma$ ： $W ( F ) \to \mathbf { Z } ^ { \mathcal { \Omega } }$ ,one needs to know to what extent it is possible to prescribe the signs of a field element at the various orderings of $F$

(2.10) Example. If $F$ is an algebraic extension of the rationals, then given a completely arbitrary open and closed subset $U { \bf { C } } \Omega ,$ there exists $^ { a }$ field element $\alpha$ which satisfies the condition

$$
\alpha \in P \Leftrightarrow P \in U .
$$

Now the signature $\sigma ( \langle 1 \rangle + \langle \alpha \rangle ) \in { \bf Z } ^ { \Omega }$ is twice the characteristic function of $U$ ,and by adding such characteristic functions, one sees that every element ofthe ideal $2 \mathbf { Z } ^ { \Omega }$ belongs to the image of $\overleftarrow { \boldsymbol { \sigma } } .$ (The corresponding statement for a completely arbitrary field would be false.)

Proof of (2.10). First suppose that $\boldsymbol { F }$ has finite degree over $\mathbf { Q }$ Then there exist only finitely many embeddings

$$
\varphi _ { 1 } , \ldots , \varphi _ { m } \colon F \longrightarrow \mathbf { R } ,
$$

and it clearly suffices to construct field elements $\alpha _ { 1 } , \ldots , \alpha _ { m }$ so that $\varphi _ { i } ( \alpha _ { j } )$ is positive if $i \neq j$ and negative if $i { = } j$ .Suitable products of the $\alpha _ { i }$ will then have arbitrarily prescribed signs.

Choose a field element $\xi$ so that $\begin{array} { r } { F { = } \mathbf { Q } \left( \xi \right) . } \end{array}$ ，Now choose a rational numher $\varepsilon > 0$ so that

$$
2 \varepsilon < | \varphi _ { i } ( \xi ) - \varphi _ { j } ( \xi ) |
$$

for i+j,and choose rational numbers $q _ { 1 } , \ldots , q _ { m } :$ so that

$$
\displaystyle | \varphi _ { i } ( \xi ) - q _ { i } | < \varepsilon .
$$

The differences

$$
\alpha _ { i } = ( \xi - q _ { i } ) ^ { 2 } - \varepsilon ^ { 2 }
$$

will then have the required property.

Now suppose that $\pmb { F }$ has infinite degree over $\mathbf { Q }$ .The given open and closed set $U { \bf \subset } { \pmb { \Omega } }$ can be covered by finitely many basic open sets $U _ { \xi _ { 1 } } \cap \cdots \cap U _ { \xi _ { k } }$ which do not intersect the complement of U. Taking all of these field elements $\xi _ { 1 } , \ldots , \xi _ { k }$ for all of the basic open sets which are needed, we generate a certain subfield $F _ { 0 } { \subset } F$ which is finite over Q. Clearly the given set $U { \subset } \Omega ( F )$ is equal to the inverse image of a suitable subset $U _ { 0 } { \subset } \Omega ( F _ { 0 } )$ under the restriction morphism

$$
\Omega ( F ) \to \Omega ( F _ { 0 } ) .
$$

Choosing $\alpha \in F _ { 0 }$ so as to be positive at the orderings in $U _ { 0 }$ and negative at the orderings in the complement of $U _ { 0 }$ ,this completes the proof.□

For further information see [Knebusch, Rosenberg, and Ware].

# § 3. Prime Ideals in the Witt Ring

In this section we study the structure of the Wittring $W ( { \boldsymbol { F } } )$ for an arbitrary field F.The results are due to Pfister, but the simplified proofs are due to Lorenz and Leicht.

(3.1) Lemma. The Witt ring W $( F )$ is additively generated by the elements (α>, where α varies over F.

Proof. This follows immediately from Chapter I, δ 3.

(3.2) Lemma. If $\mathfrak { p }$ is an arbitrary prime ideal in $W ( { \boldsymbol { F } } ) ,$ then for every $\alpha \in F ^ { \bullet }$ either

$$
\begin{array} { r } { { \langle \alpha \rangle } \equiv { \langle 1 \rangle } \qquad { \mathrm { m o d } } { \mathfrak { p } } } \end{array}
$$

Hence the quotient ring $W ( F ) / { \mathfrak { p } }$ is isomorphic either to $\mathbf { Z } ,$ or to the field $\mathbf { F } _ { p } = \mathbf { Z } / p \mathbf { Z }$ for some prime number $\pmb { p }$

Proof. Since the element $\langle x ^ { 2 } \rangle$ of $W ( { \boldsymbol { F } } )$ is equal to $\langle 1 \rangle$ , we have

$$
\scriptstyle ( \langle \alpha \rangle - \langle 1 \rangle ) ( \langle \alpha \rangle + \langle 1 \rangle ) = 0
$$

in $W ( { \boldsymbol { F } } ) .$ . Therefore, modulo any prime ideal $\mathfrak { p }$ , the element $\langle { \alpha } \rangle$ is congruent to either <1> or $- \left. 1 \right.$ . It follows that the unique ring homomorphism

$$
\mathbf { Z } \to W ( F ) \to W ( F ) / { \mathfrak { p } }
$$

is surjective. Since the kernel must be a prime ideal of Z, this completes the proof.□

First consider the case $p { = } 2$

(3.3) Lemma. For any field $\pmb { F }$ ,there is one and only one ideal I in $W ( { \boldsymbol { F } } )$ such that $W ( F ) / I { \cong } \mathbf { F } _ { 2 }$ ：

Thus $\scriptstyle I = I ( F )$ is the kernel of the unique ring homomorphism $W ( F ) \to \mathbf { F } _ { 2 }$ . We will call I the fundamental ideal of the Witt ring.

Proof of(3.3). If $W ( F ) / I { \cong } \mathbf { F } _ { 2 }$ ,then

$$
\langle 1 \rangle \equiv \langle - 1 \rangle \mod I ,
$$

and therefore

$$
\begin{array} { r } { { \langle \alpha \rangle } \equiv { \langle 1 \rangle } \qquad { \mathrm { m o d } } I } \end{array}
$$

for every $\alpha$ It follows that I consists precisely of all sums $\langle \alpha _ { 1 } \rangle + \cdots + \langle \alpha _ { r } \rangle$ for which the rank r is even.

correspondence

$$
X \mapsto \operatorname { r k } ( X ) \mod \operatorname { u l o } 2
$$

gives rise to a ring homomorphism $W ( F ) \to \mathbf { F } _ { 2 }$ whose kernel is the required fundamental ideal $I$ □

(3.4) Remark. The Wit ring $W ( { \boldsymbol { F } } )$ is isomorphic to $\mathbf { F } _ { 2 }$ if and only if every element of ${ \pmb F } ^ { \bullet }$ is a square.

Examples are provided by algebraically closed fields, and perfect fields of characteristic 2.

Proof.If $W ( F ) { \cong } \mathbf { F } _ { 2 }$ , then for every $\alpha \in F ^ { \bullet }$ the anisotropic inner product space $\langle { \alpha } \rangle$ belongs to the same Witt class as $\langle 1 \rangle$ ,and therefore is isomorphic to <1>.Hence $\pmb { \alpha }$ is a square. Since the converse is straightforward, this completes the proof.□

Now let us look at the remaining prime ideals.

(3.5) Main lemma. 1 $f { \mathfrak { p } } \subset W ( F )$ is any prime ideal with

$$
W ( F ) / { \mathfrak { p } } \not \equiv \mathbf { F } _ { 2 } ,
$$

then the set $P { \subset } F ^ { \bullet }$ consisting of all feld elements $\alpha \neq 0$ with

$$
\langle \alpha \rangle \equiv \langle 1 \rangle { \pmod { \mathfrak { p } } }
$$

constitutes an ordering of $F$ .The associated signature homomorphism

$$
\sigma _ { P } \colon W ( F ) \to \mathbf { Z }
$$

satisfies the congruence

$$
\begin{array} { r } { \overline { { \ b { w } } } \equiv \sigma _ { P } ( w ) \left. 1 \right. \qquad ( \mathrm { m o d } \ \mathfrak { p } ) } \end{array}
$$

for every element w in the Witt ring.

Hence the given prime ideal $\mathfrak { p }$ is either the kernel of $\sigma _ { P }$ or the kernel nf the camnasitinn

$$
\overline { { W ( F ) \xrightarrow { \sigma _ { P } } \mathbf { Z } \xrightarrow { } \mathbf { F } _ { p } } }
$$

according as the quotient $W ( F ) / { \mathfrak { p } }$ is isomorphic to $\mathbf { Z _ { \theta } } \mathrm { o r } \mathbf { F _ { p } } .$ ，

Proof.It is clear that P is closed under multiplication, and that

$$
P \cup ( - P ) { = } F ^ { \bullet } .
$$

So we need only prove that $P$ is closed under addition. If $\alpha , \beta { \in } P$ and $\alpha + \beta = \gamma \neq 0$ ,then evidently

$$
\langle \alpha \rangle \oplus \langle \beta \rangle \cong \langle \gamma \rangle \oplus \langle \delta \rangle
$$

for some δ.Reducing modulo p in the Witt ring,this yields

$$
\langle 1 \rangle + \langle 1 \rangle \equiv \langle \gamma \rangle + \langle \delta \rangle { \pmod { \mathfrak { p } } }
$$

with $\langle \gamma \rangle \equiv \langle \pm 1 \rangle$ and $\langle \delta \rangle \equiv \langle \pm 1 \rangle$ . But the hypothesis that $W ( F ) / { \mathfrak { p } } \not \equiv { \mathbf { F } } _ { 2 }$ implies that $\langle 1 \rangle + \langle 1 \rangle$ is not congruent to either $\langle - 1 \rangle + \langle 1 \rangle$ or $\langle - 1 \rangle +$ $\langle - 1 \rangle$ modulo $\mathfrak { p }$ .Therefore

$$
\langle \gamma \rangle \equiv \langle 1 \rangle { \pmod { \mathfrak { p } } } ,
$$

hence $\gamma = { \mathfrak { X } } + \beta \in P$ .The case $\pmb { \alpha }$ $\beta \in P$ and $\alpha + \beta = 0$ cannot occur, since the inner product space $\langle \alpha \rangle \oplus \langle \beta \rangle$ would then be split, implying that

$$
\langle 1 \rangle + \langle 1 \rangle \equiv \langle \alpha \rangle + \langle \beta \rangle = 0
$$

which contradicts our hypothesis. Thus $P$ is an ordering of $\pmb { F }$ ：

Now for any $\pmb { \alpha }$ in $F ^ { \bullet }$ the congruence

$$
\langle \alpha \rangle \equiv \sigma _ { P } ( \langle \alpha \rangle ) \langle 1 \rangle { \pmod { \mathfrak { p } } }
$$

![](images/33c2f4fd26b5b0b7affca17ae5eedf3b76c0aa8b6265e050204cbe125549048d.jpg)

In particular,since $\langle 1 \rangle + \langle 1 \rangle \in { \cal I } ,$ it follows that some power $( \langle 1 \rangle + \langle 1 \rangle ) ^ { n } = 2 ^ { n } \langle 1 \rangle$ is zero in $W ( { \boldsymbol { F } } )$ (Here $2 ^ { n } \langle 1 \rangle$ denotes the sum of $2 ^ { n }$ copies of <1>.) Therefore $2 ^ { n } w = 0$ for every w in the Witt ring. This completes the proof.□

Remark. This proof makes rather blatant use of Zorn's lemma. We will give a more constructive argument in $\ S 4 . 6 .$

Now consider a field in which -1 is not a sum of squares. Let M denote the ideal consisting of all nilpotent elements in the Witt ring.

(3.8) Theorem. $I f - 1$ is not $a$ sum of squares in $F$ ,thenthenilradical $\mathfrak { N } \subset W ( F )$ is precisely equal to the kernel of the total signature homomorphism $\boldsymbol { \sigma } \colon W ( F ) \to \mathbf { Z } ^ { \Omega }$

of $\ S 2 . 8$ . An element w in the Witt ring is a unit if and only if its image $\sigma ( w )$ is a unit in the ring $\mathbf { Z } ^ { \mathcal { \Omega } }$

Proof. If $\sigma ( w ) { = } 0$ , then certainly w belongs to the fundamental ideal 1, consisting of Witt classes of even rank. But it follows from (3.5) that w belongs to every other prime ideal also.Therefore $w \in \mathfrak { N }$ .Conversely, if $w \in \mathfrak { N }$ then $\sigma ( w )$ is nilpotent hence $\sigma ( w ) = 0$

Now suppose that $\sigma ( w )$ is a unit. Then $\sigma ( w ) ^ { 2 } = 1 , { \mathrm { h e n c e ~ } } w ^ { 2 } \equiv 1 { \mathrm { m o d } } \mathfrak { N } ,$ and it follows that w is a unit. This completes the proof.

(3.9) Corollary. The Witt ring W(F) is isomorphic to Z if and only if F is an ordered field in which every positive element is a square.

For if $W ( F ) { \cong } \mathbf { Z } $ ,then $F$ can be ordered,and for every $\alpha > 0$ the anisotropic inner product space $\langle \alpha \rangle$ belongs to the same Witt class as $\langle 1 \rangle$ and hence is isomorphic to $\langle 1 \rangle$ .Therefore $\pmb { \alpha }$ is a square. Together with (2.7), this completes the proof.□

(3.10) Theorem. For any field $F$ ，the torsion subgroup of $W ( { \boldsymbol { F } } )$ is precisely the kernel of the total signature homomorphism

The order of every torsion element is a power of 2.

Remark. If $F$ has only one ordering, then this can be proved quite simply as follows. Clearly the kernel of $\sigma { : W ( F ) \to \mathbf { Z } }$ is additively generated by elements of the form $\langle 1 \rangle - \langle \alpha \rangle$ with $\alpha > 0$ .But

$$
( \langle 1 \rangle - \langle \alpha \rangle ) ^ { 2 } = 2 ( \langle 1 \rangle - \langle \alpha \rangle )
$$

and therefore

$$
( \langle 1 \rangle - \langle \alpha \rangle ) ^ { n } { = } 2 ^ { n - 1 } ( \langle 1 \rangle - \langle \alpha \rangle ) .
$$

Since <1>-<α> is known to be nilpotent, it follows that its order is a power of 2.

The proof in the general case will be based on the following. Let $K$ be any extension field of $F$ .Recall from Chapter I, $\ S 5 . 4$ that any inner product space $X$ of rank $r$ over $F$ gives rise to an inner product space $K \otimes _ { F } X$ of rank $r$ over $K$ . Clearly this correspondence induces a ring

homomorphism

For a quadratic extension, the kernel of this homomorphism is computed as follows. We assume that $F$ has characteristic $\neq 2$

(3.11) Lemma. For any $\alpha \in F ^ { \bullet }$ ,the kernel of the natural homomorphism $W ( { \dot { F } } ) \to { \overline { { W } } } \big ( F ( \sqrt { \alpha } ) \big )$ is equal to the principal ideal $( \langle 1 \rangle - \langle \alpha \rangle ) W ( F )$ Every element w in the kernel satisfies $w = - \langle { \boldsymbol { \alpha } } \rangle w$

Proof. Certainly $\pmb { \alpha }$ maps to a square in $F ( { \sqrt { \alpha } } ) ,$ hence the ideal $( \langle 1 \rangle - \langle \alpha \rangle ) W ( F )$ maps to zero. But if an anisotropic inner product space $X { \neq } 0$ over $F$ represents a Witt class in the kernel, then there certainly exists a vector $\operatorname { \dot { z } } \pm \theta \operatorname { i n } F ( { \sqrt { \alpha } } ) \otimes _ { F } X$ with $z \cdot z = 0$ Setting $z = x + \sqrt { \alpha } y$ with $\overline { { x } }$ and $\overline { { y } }$ in $X$ , the equation ${ \overline { { z \cdot z } } } = 0$ implies that

$$
x \cdot x + \alpha y \cdot y = 0 , ~ x \cdot y = 0 .
$$

Since $X$ is anisotropic, at least one of the field elements $x \cdot x$ and $y \cdot y$ is non-zero, hence both are non-zero. Seting $y \cdot y = \eta _ { 1 }$ and $x \cdot x { = } - \alpha \eta _ { 1 } ;$ we see that X decomposes as an orthogonal sum

$$
\overline { { \langle \eta _ { 1 } \rangle \oplus \langle - \alpha \eta _ { 1 } \rangle \oplus X ^ { \prime } } } ,
$$

where $X ^ { \prime }$ is also anisotropic and also represents an element of the kernel. An easy induction now shows that

$$
X \cong ( \langle 1 \rangle \oplus \langle - \alpha \rangle ) \otimes ( \langle \eta _ { 1 } \rangle \oplus \dots \oplus \langle \eta _ { k } \rangle )
$$

for suitable $\boldsymbol { \eta } _ { 1 } , \dots , \boldsymbol { \eta } _ { k }$ . Clearly it follows that

$$
{ \cal X } \cong \langle - \alpha \rangle \otimes { \cal X } ,
$$

which completes the proof.□

Proof of Theorem (3.10). Suppose that some nilpotent element w of $W ( { \boldsymbol { F } } )$ satisfies $2 ^ { n } w \neq 0$ for all $\pmb { n }$ .Consider algebraic extension fields $K \supset F$ such that the image $w ^ { \prime } = i _ { * } ( w )$ in $W ( K )$ satisfies $2 ^ { n } w ^ { \prime } \ne 0$ for all n. Note that any monotone union of fields having this property will again have this property.Hence, by Zorn's lemma, there exists a maximal extension field $K$ with this property. If $\alpha \in K$ is any non-square, then the field $\kappa ( \sqrt { \alpha } )$ is strictly larger than $K .$ .Therefore the image of $2 ^ { n } w ^ { \prime }$ in $W \big ( K ( \sqrt { \alpha } ) \big )$ is zero for large n, and it follows from (3.11) that

Since $W ( K )$ is not a 2-torsion group, it follows from (3.6) that $K$ can be ordered. Since $W ( K )$ possesses nilpotent elements, it follows from (3.9) that not every positive element of $K$ is a square. Therefore the quotient $K ^ { \bullet } / K ^ { \bullet 2 }$ contains at least four distinct elements. Let $1 , \alpha , \beta ,$ and $\alpha \beta$ in Kbe distinct modulo $K ^ { \bullet 2 }$ .Then

$$
\begin{array} { c } { { 2 ^ { n } w ^ { \prime } = \langle - \alpha \rangle 2 ^ { n } w ^ { \prime } = \langle - \alpha \rangle \langle - \beta \rangle 2 ^ { n } w ^ { \prime } } } \\ { { = \langle - \alpha \rangle \langle - \beta \rangle \langle - \alpha \beta \rangle 2 ^ { n } w ^ { \prime } } } \end{array}
$$

for large n. This proves that $2 ^ { n } w ^ { \prime } = - 2 ^ { n } w ^ { \prime }$ or $2 ^ { n + 1 } \ w ^ { \prime } { = } 0 .$ ， which contradicts our hypothesis and completes the proof.□

(3.12) Corollary.For each ordering $P$ let $F _ { P }$ denote the associated real closure of $F$ .Then the kernel of the natural homomorphism

is equal to the torsion subgroup of W(F).

The proof is immediate.

To conclude this section, we will outline a different description of the torsion in $W ( { \boldsymbol { F } } ) _ { : }$ due to Scharlau [1969],[1970].Let $\pmb { F }$ be a field of charactersistic 丰2.

Definition. The field $\boldsymbol { \mathsf { \Pi } }$ is pythagorean if the subset $F ^ { 2 }$ is closed under addition; or in other words if every sum of squares is a square in $F$

Given any field $F$ of characteristic $\neq 2 ,$ ，with algebraic closure ${ \overline { { F } } } _ { z }$ there is a unique smallest extension field $F _ { p y } \subset \overline { { F } }$ which is pythagorean. In fact $F _ { p y }$ is the union of all iterated quadratic extensions of the form

$$
F { \subset } \cdots { \subset } K { \subset } K \left( \sqrt { \alpha ^ { 2 } + \beta ^ { 2 } } \right)
$$

within $\overline { { F } }$ We will call this unique field $F _ { p y }$ the pythagorean closure of $F$ The Witt ring $W ( F _ { p y } )$ of a pythagorean field can be described as follows. If -1 is a sum of squares in $F _ { p y }$ ,then every element of $F _ { p y }$ is a square,and it follows that $W ( F _ { p y } ) { \cong } \bar { \mathbf { Z } } / 2 \mathbf { Z } .$ (Compare (2.3) and (3.4).) On the other hand if-1 is not $a$ sum of squares, then $W ( F _ { p y } )$ is torsion free. In fact,given $w \ne 0$ in $W ( F _ { p y } )$ choose an anisotropic representative $A \cong \langle \alpha _ { 1 } \rangle \oplus \dots \oplus \langle \alpha _ { n } \rangle$ for $w$ .Then for any $k > 0$ the $k$ -fold sum $A \oplus \cdots \oplus A$ is also anisotropic. For if the equation $\sum _ { j \mathop { = } 1 } ^ { k } \sum _ { i \mathop { = } 1 } ^ { n } \alpha _ { i } \zeta _ { i j } ^ { 2 } { = } 0$ had a non-trivial solution then, setting $\sum _ { j } \xi _ { i j } ^ { 2 } = \eta _ { i } ^ { 2 }$ ， it would follow that the equation $\sum \alpha _ { i } \eta _ { i } ^ { 2 } = 0$ also had a non-trivial solution, which is impossible.

(3.13) Assertion. If $F _ { p y }$ is the pythagorean closure of $F$ ，then the

$$
0 \to { \mathrm { T o r s ~ } } I W ( F ) \to W ( F ) \to W ( F _ { p y } )
$$

Here Tors $I W ( F )$ denotes the torsion subgroup of the fundamental ideal $I { \subset W ( F ) }$ ,considered as additive group.

Proof. First consider a quadratic extension of the form

$$
K \subset K ( \sqrt { \alpha ^ { 2 } + \beta ^ { 2 } } ) .
$$

By (3.11) the kernel of the associated homomorphism

$$
W ( K ) \to W \bigl ( K ( \sqrt { \alpha ^ { 2 } + \beta ^ { 2 } } ) \bigr )
$$

is equal to the ideal $( \langle 1 \rangle - \langle \alpha ^ { 2 } + \beta ^ { 2 } \rangle ) W ( K ) .$ Using the isomorphism

$$
( 1 ) \oplus ( 1 ) \cong ( \alpha ^ { 2 } + \beta ^ { 2 } ) \oplus ( \alpha ^ { 2 } + \beta ^ { 2 } )
$$

we see that every element in this ideal has order 2. For an iterated extension $F { \mathsf { C } } \cdots { \mathsf { C } } K { \mathsf { C } } K ( { \sqrt { \alpha ^ { 2 } + \beta ^ { 2 } } } )$ of degree $2 ^ { n }$ over $F$ it follows inductively that the kernel of the associated homomorphism of Witt rings has exponent $2 ^ { n }$ .Passing to the direct limit $\stackrel { \cdot } { = }$ inductive limit) of all such iterated extensions, it follows that the kernel of the homomorphism

$$
W ( \boldsymbol { F } ) \to W ( F _ { p y } )
$$

is a 2-primary torsion group. But $W ( F _ { p \bf { y } } )$ is torsion free,so this kernel must be precisely equal to the torsion subgroup of W(F).□

This argument, incidentally, gives a simpler proof that the Witt ring of a field contains no odd torsion.

Note that for any field (even in characteristic 2) the subgroup Tors $I W ( F )$ is precisely equal to the nilradical of $W ( { \boldsymbol { F } } )$

# $\ S$ 4. Multiplicative Inner Product Spaces

The results in this section are due to Pfister. (Compare [Scharlau, 1969] and [Lorenz].) However for convenience we will modify Pfister's definitions.

If $_ x$ belongs to an inner product space $X$ , it will be convenient to call $x \cdot x$ the norm of $x .$ Thus a field element $\pmb { \alpha }$ is a norm from $X$ if ${ \mathfrak { x } } = { \mathfrak { x } } \cdot { \mathfrak { x } }$ for some $_ x$

(4.1) Definition. An inner product space $X$ is multiplicative if

$$
X \cong \langle \alpha \rangle \otimes X
$$

for every field element $\pmb { \alpha }$ ±0 which is a norm from X.

One important property of multiplicative spaces is the following.

(4.2) Lemma. If $X$ is multiplicative, then the set of all field elements $\alpha \neq 0$ which are norms from $X$ forms $^ { a }$ subgroup of $F ^ { \bullet }$

$$
f \colon X \to \langle \beta \rangle \otimes X .
$$

Seting $f ( x ) = e \otimes z$ ,where $e \cdot e = \beta$ ，we obtain

$$
x \cdot x { = } f ( x ) \cdot f ( x ) { = } \beta z \cdot z .
$$

Therefore the quotient $\alpha / \beta = z \cdot z$ is also a norm from $X$ ,which completes the proof.□

As an example, the inner product space $\langle 1 \rangle$ is certainly multiplicative, with group of non-zero norms equal to F· 2.

(4.3) Theorem. Any tensor product of the form

$$
( ( 1 ) \oplus ( \alpha _ { 1 } ) ) \otimes \cdots \otimes ( ( 1 ) \oplus ( \alpha _ { n } ) )
$$

is multiplicative.Furthermore any such tensor product is either anisotropic or split.

Proof. First consider the case $\overline { { n = 1 } }$ .If $\beta { \neq } 0$ is a norm from $\langle 1 \rangle \oplus \langle { \alpha } \rangle$ ， then clearly $\langle 1 \rangle \oplus \langle \alpha \rangle \cong \langle \beta \rangle \oplus \langle \gamma \rangle$

for some $\gamma$ .Comparing determinants, we see that $\langle \gamma \rangle \cong \langle \beta \alpha \rangle , \ s \scriptscriptstyle 0$

$$
\langle 1 \rangle \oplus \langle \alpha \rangle \cong \langle \beta \rangle \otimes ( \langle 1 \rangle \oplus \langle \alpha \rangle )
$$

as required. Since very inner product space of rank 2 is either anisotropic or split, this takes care of the case $n = 1$

The proof now proceeds by induction. Assuming that $X$ is multiplicative, we will show that the space

$$
\left( \left. 1 \right. \oplus \left. \alpha \right. \right) X \cong X \oplus \left. \alpha \right. X
$$

is multiplicative. Here we are leaving out the tensor product signs, to simplify the notation. Let $\beta { \neq } 0$ be a norm from $X \oplus \langle a \rangle X$ .Then clearly $\beta$ has the form

$$
\beta = x \cdot x + \alpha y \cdot y = \xi + \alpha \eta
$$

where $\xi$ and $\eta$ are norms from $X$ .If $\xi = 0$ ,then $\eta \neq 0$ so $\langle \eta \rangle X { \cong } X$ and $\left. \alpha \eta \right. ( X \oplus \left. \alpha \right. X ) \cong \left. \alpha \right. X \oplus \left. \alpha \right. ^ { 2 } X \cong X \oplus \left. \alpha \right. X ,$ ，as required. The case $\scriptstyle \eta = 0$ is handled similarly. Suppose then that both $\xi$ and $\eta$ are non-zero. Then $X \cong \langle \xi \rangle X \cong \langle \eta / \xi \rangle X$ so it follows that

$$
\begin{array} { r } { \underbrace { \left. \xi + \alpha \eta \right. \left( X \oplus \left. \alpha \right. X \right) \cong \left. 1 + \alpha \eta / \xi \right. \left( X \oplus \left. \alpha \eta / \xi \right. X \right) } _ { \cong \left. 1 + \alpha \eta / \xi \right. \left( \left. 1 \right. \oplus \left. \alpha \eta / \xi \right. \right) X } } \end{array}
$$

But we have already established that the inner product space

$$
\langle 1 \rangle \oplus \langle \alpha \eta / \xi \rangle
$$

is multiplicative. Since 1+αn/§ is a non-zero norm from this space, we see that the factor $\langle 1 + \alpha \eta / \xi \rangle$ can be cancelled, and we are left with

$( ( 1 ) \oplus \langle \alpha \eta / \xi \rangle ) X \cong X \oplus \langle \alpha \rangle X ,$ as required.

We must prove also that $X \oplus \langle { \alpha } \rangle X$ is either anistropic or split, assuming inductively that $X$ itself is either anisotropic or split. If $X \oplus \alpha X$ is not anisotropic,then there exist vectors $x$ and $y$ in $X$ ,not both zero, so that

$$
\scriptstyle x \cdot x + \alpha y \cdot y = \xi + \alpha \eta = 0 .
$$

$\mathrm { H } \ \xi = \eta = 0 ;$ then $X$ must be split, and it certainly follows that $X \oplus \langle a \rangle X$ is split. But otherwise $\xi / \eta = - \alpha$ is a non-zero norm from $X$ ; therefore $X \cong \langle - \alpha \rangle X$ and it follows again that $X \oplus \langle a \rangle X$ is split. This completes the proof.□

A special case of (4.3) which is particularly interesting is the case $\alpha _ { 1 } = \cdots = \alpha _ { n } = 1 \quad$ .The tensor product

is then a $2 ^ { n }$ fold orthogonal sum of copies of $\left. 1 \right.$ .We write this briefly as $2 ^ { n } \langle 1 \rangle$

(4.4) Corollary. For any field $F$ and any $n { \geq } 0$ the subset consisting of field element $\xi \neq 0$ which can be expressed as the sum of $2 ^ { n }$ squares forms a multiplicative group.

This follows from (4.2) and (4.3) since a field element is a norm from $2 ^ { n } \langle 1 \rangle$ if and only if it is a sum of $2 ^ { n }$ squares.

As an example, for the field Q of rational numbers, since both $5 = 1 ^ { 2 } + 2 ^ { 2 }$ and $1 3 = 2 ^ { 2 } + 3 ^ { 2 }$ can be expressed as the sum of 2 squares, it follows that $6 5 ( = 4 ^ { 2 } + 7 ^ { 2 } )$ can also.(Compare Chapter II, \$8.) By way of contrast, both $3 = 1 ^ { 2 } + 1 ^ { 2 } + 1 ^ { 2 }$ and $5 = 0 ^ { 2 } + 1 ^ { 2 } + 2 ^ { 2 }$ can be expressed as the sum of 3 squares, yet their product cannot. For if 15 were equal to $\alpha ^ { 2 } + \beta ^ { 2 } + \gamma ^ { 2 }$ ， then clearing denominators and reducing modulo 8 one would obtain

$$
- d ^ { 2 } \equiv a ^ { 2 } + b ^ { 2 } + c ^ { 2 } \mod 8
$$

with at least one of the integers $a , b , c , d$ odd, which is easily seen to be impossible.

Here is an important application of (4.3).

Definition. If -1 is a sum of squares in $F ,$ then the level (Stufe) of $F$ is the smallest integer $s$ such that $- 1$ is a sum of $s$ squares. If $^ { - 1 }$ is not a sum of squares, we set $s { = } \infty$

(4.5) Theorem. For any field F, the order of the element $\langle 1 \rangle$ in the additive group of $W ( { \boldsymbol { F } } )$ is precisely equal to 2s. The level s is always either infinity or a power of 2.

Remark. In the classical case of a number field, the level $s$ is always equal to $\infty , 1 , 2$ ,or 4. Examples are provided by Q, $\mathbf { Q } ( { \sqrt { - 1 } } )$ $\mathbf { Q } ( { \sqrt { - 2 } } )$ and $\mathbf { Q } ( \gamma ^ { - 7 } )$ respectively. Since the order of $\langle 1 \rangle$ is comparitively easy to compute, this theorem provides an excellent method for computing s.

Proof of (4.5). If $s { = } \infty$ the assertion is clear, so we may assume that $s < \infty$ .Note first that the $S ^ { \prime }$ -fold orthogonal sum $\langle 1 \rangle \oplus \dots \oplus \big \langle 1 \big \rangle = s \big \langle 1 \big \rangle$ is anisotropic. For if the equation

$$
\xi _ { 1 } ^ { 2 } + \cdots + \xi _ { s } ^ { 2 } = 0
$$

had a solution with say $\xi _ { 1 } \neq 0$ ,then it would follow that

$$
- 1 = ( \xi _ { 2 } / \xi _ { 1 } ) ^ { 2 } + \dots + ( \xi _ { s } / \xi _ { 1 } ) ^ { 2 } ,
$$

contradicting the definition of s.A similar argument shows that the $( s + 1 )$ fold orthogonal sum $( s + 1 ) \langle 1 \rangle$ is not anisotropic.

Now define an integer $n { \stackrel { \textstyle > 0 } { = } }$ by the inequality $2 ^ { n } \leq s < 2 ^ { n + 1 }$ . It follows   
a fortiori that the orthogonal sum $2 ^ { n } \langle 1 \rangle$ is anisotropic, but that $2 ^ { n + 1 } \langle 1 \rangle$   
is not.Let us apply Theorem (4.3). Since $2 ^ { n + 1 } \langle 1 \rangle$ can be expressed as a   
tensor product $( \langle 1 \rangle \oplus \langle 1 \rangle ) \otimes \cdots \otimes ( \langle 1 \rangle \oplus \langle 1 \rangle ) ,$

and is not anisotropic, it follows that $2 ^ { n + 1 } \langle 1 \rangle$ is split. The relations

$$
2 ^ { n } \langle 1 \rangle \nsim 0 , 2 ^ { n + 1 } \langle 1 \rangle \sim 0
$$

now clearly imply that the order of the element $\left. 1 \right.$ in the Witt ring is precisely equal to 2n+1.

We must prove that ${ \mathfrak { s } } = 2 ^ { n }$ .Adding $2 ^ { n }$ copies of $\langle - 1 \rangle$ to both sides of the relation $2 ^ { n + 1 } \langle 1 \rangle \sim 0$ ,we conclude that

$$
2 ^ { n } \langle 1 \rangle \sim 2 ^ { n } \langle - 1 \rangle .
$$

But these spaces are anisotropic, so it follows from (1.7) that

$$
2 ^ { n } \langle 1 \rangle \cong 2 ^ { n } \langle - 1 \rangle .
$$

Therefore -1 is a sum of 2" squares, hence $s { \leq } 2 ^ { n } ,$ and therefore $s { = } 2 ^ { n }$ This completes the proof.0

(4.6) Remark. We can now give a more constructive proof that every element of the fundamental ideal $I { \subset W ( F ) }$ is nilpotent, whenever $s { = } 2 ^ { n } { < } \infty$ . (Compare $\ S 3 . 6 . )$ In fact for any $w$ in the Witt ring, setting

$$
w = \langle \alpha _ { 1 } \rangle + \cdots + \langle \alpha _ { r } \rangle
$$

$$
w ^ { 2 } \equiv \langle \alpha _ { 1 } \rangle ^ { 2 } + \dots + \langle \alpha _ { r } \rangle ^ { 2 } = r \langle 1 \rangle \mod 2 W ( F ) .
$$

If the rank $r$ is even, it follows that

$$
w ^ { 2 } { \equiv } 0 \mod 2 W ( F )
$$

and therefore

$$
w ^ { 2 ( n + 1 ) } \equiv 0 { \pmod { 2 ^ { n + 1 } W ( F ) } } .
$$

Since multiplication by $2 ^ { n + 1 } = 2 s$ annihilates every element of the Witt ring, this proves that $\overline { { w ^ { 2 \left( n + 1 \right) } = 0 } }$

Here is a concluding problem for the reader. An $\pmb { F }$ -linear bijection $f$ ： $X \to X$ is called a similarity transformation if there exists a field element $\lambda \neq 0$ so that

$$
f ( x ) \cdot f ( y ) = \lambda x \cdot y
$$

for all $_ x$ and $y$

Exercise. Assume that 1 is a norm from X. Prove that the group of similarity transformations of X operates transitively on $X { - } 0$ if and only if $\pmb { X }$ is multiplicative and anisotropic.

# § 5.The Powers of the Fundamental Ideal

This section will discuss the chain of ideals $I { \supset } I ^ { 2 } { \supset } I ^ { 3 } { \supset } \cdots$ in the Witt ring $W ( { \boldsymbol { F } } ) _ { : }$ where $I$ is the fundamental ideal consisting of all Witt classes with even rank. A basic theorem concerning these ideals has recently been proved by Arason and Pfister. We state it here without proof.

(5.1) Theorem. If w∈I" and w≠0, then |lw≥2n.

(Here $\| w \|$ denotes the rank of the anisotropic representative for the Witt class w.） It follows immediately that the intersection of the ideals $I ^ { n }$ is zero.

Each quotient $I ^ { n } / I ^ { n + 1 }$ is clearly a vector space over the field

$$
W ( F ) / I { \cong } \mathbf { F } _ { 2 } .
$$

The following observation is due to Pfister.

The proof is based on the determinant operation of Chapter I, $\ S 2$ For any inner product space $X$ ，recall that det $( X )$ is a well defined element of $F ^ { \bullet } / F ^ { \bullet 2 }$ . However we have to be careful since the determinant of a split inner product space is not necessarily trivial. To correct this, we make the following modification.

Definition. For any inner product space $X$ of rank $_ r$ the discriminant

$$
d ( X ) { \in } F ^ { \bullet } / F ^ { \bullet 2 }
$$

is defined to be the element $( - 1 ) ^ { r ( r - 1 ) / 2 } \operatorname* { d e t } ( X )$

Let us compute the discriminant of an orthogonal sum $X \oplus Y .$ Setting $r = \mathbf { r k } ( X )$ and $s = \mathbf { r } \mathbf { k } ( Y ) .$ ,and setting $f ( r ) { = } r ( r - 1 ) / 2$ ,the identity

$$
f ( r + s ) = f ( r ) + f ( s ) + r s
$$

is easily verified. It follows that

$$
d ( X \oplus Y ) { = } ( - 1 ) ^ { r s } d ( X ) d ( Y ) .
$$

In particular, if either $X$ or $Y$ has even rank, then $d ( X \oplus Y ) { = } d ( X ) d ( Y ) .$

(5.3) Lemma. The discriminant $d ( X )$ depends only on the Witt class ofx.

For if S is split, of rank $2 n$ , then by Chapter $\operatorname { I , \ S 6 . 3 }$ , the inner product matrixof Swithrespecttoasuitablebasis hasthefor $\left( \begin{array} { l l } { 0 } & { I } \\ { I } & { * } \end{array} \right)$ $\operatorname* { d e t } ( S ) = ( - 1 ) ^ { n } F ^ { \bullet 2 } ,$

and it follows that $d ( S )$ is the identity element of $F ^ { \bullet } / F ^ { \bullet 2 }$ . The proof of (5.3) is now straightforward.□

Proof of (5.2). Evidently the correspondence $w \mapsto d ( w )$ maps the additive group of I homomorphically to the group $F ^ { \bullet } / F ^ { \bullet 2 } .$ This homomorphism is surjective since

$$
d ( \langle \xi \rangle + \langle - 1 \rangle ) { = } \xi F ^ { \bullet 2 } ;
$$

and it annihilates the ideal $I ^ { 2 }$ since $I ^ { 2 }$ is additively generated by products of the form

$$
( \langle \alpha \rangle + \langle 1 \rangle ) ( \langle \beta \rangle + \langle 1 \rangle ) { = } \langle \alpha \beta \rangle + \langle \alpha \rangle + \langle \beta \rangle + \langle 1 \rangle ,
$$

each of which has trivial discriminant. Now let $w = \langle \alpha _ { 1 } \rangle + \cdots + \langle \alpha _ { 2 r } \rangle$ be an arbitrary element of $I _ { \ l }$ .Using the congruences

$$
\begin{array} { r } { \langle \alpha \rangle + \langle \beta \rangle \equiv \langle - \alpha \beta \rangle + \langle - 1 \rangle \pmod { I ^ { 2 } } } \end{array}
$$

we see by induction on $r$ that w is congruent to an expression of the form $\langle \xi \rangle + \langle - 1 \rangle$ modulo $I ^ { 2 }$ .Now if

$$
d ( w ) = d ( \langle \xi \rangle + \langle - 1 \rangle ) = \xi F ^ { \bullet 2 }
$$

is the identity element of $F ^ { \bullet } / F ^ { \bullet 2 }$ then $\langle \xi \rangle + \langle - 1 \rangle = 0 ,$ and it follows that $w \in { \cal I } ^ { 2 } .$ Thus the sequence $0 \to I ^ { 2 } { \to } I { \to } F ^ { \bullet } / F ^ { \bullet 2 } { \to } 1$ is exact; which completes the proof.□

The next step is naturally to look at the quotient $I ^ { 2 } / I ^ { 3 }$

(5.4) Definition. A symbol on $F$ with values in the group ${ \bf Z ^ { \bullet } } = \{ \pm 1 \}$ is a bimultiplicative function

$$
\varphi \colon F ^ { \bullet } \times F ^ { \bullet } \to \mathbf { Z } ^ { \bullet }
$$

which satisfies the identity $\varphi ( \alpha , 1 - \alpha ) = 1$ for all $\alpha \neq 0$ 1.

The word “bimultiplicative” means that $\overline { { \varphi ( \alpha , \beta ) } }$ is multiplicative as a function of $\pmb { \alpha }$ for fixed $\beta$ and multiplicative as a function of $\boldsymbol { \beta }$ for fixed $\pmb { \alpha }$ .In particular $\varphi ( \alpha , 1 ) = 1$ ：

Remarks. The prototype for such an object is the“Hilbert symbol”. If $F$ is a local field of characteristic $\neq 2 ,$ ，Hilbert showed that there is one and only one non-trivial symbol on $\overline { F }$ with values in $\mathbf { Z } ^ { \bullet }$ More recently, symbols with values in an arbitrary commutative group have arisen in R. Steinberg's analysis of central extensions of classical groups. Compare [Milnor,Introduction to Algebraic $\kappa$ Theory].

(5.5) Lemma. Given some fixed symbol $\varphi$ on $F$ with values in $\mathbf { Z } ^ { \bullet }$ ,the image $\varphi ( \alpha , \beta )$ depends only on the Witt class of the inner product space $\langle \alpha \rangle \oplus \langle \beta \rangle$

Proof. Since the target group $\mathbf { Z ^ { \bullet } }$ has exponent 2, the image $\varphi ( \alpha , \beta )$ is not changed if we multiply $\pmb { \alpha }$ or $\beta$ by a square. Using the identity

$$
- \alpha = ( 1 - \alpha ) / ( 1 - \alpha ^ { - 1 } ) ,
$$

we see easily that

$$
\varphi ( \alpha , - \alpha ) = 1 ,
$$

so that $\varphi ( \alpha , \beta )$ is trivial whenever the inner product space $\langle \alpha \rangle \oplus \langle \beta \rangle$ is split.

Suppose then that the inner product spaces $\langle \alpha \rangle \oplus \langle \beta \rangle \sim \langle \gamma \rangle \oplus \langle \delta \rangle$ are not split. Then these spaces are isomorphic,so the equation

$$
\gamma = \alpha \xi ^ { 2 } + \beta \eta ^ { 2 }
$$

has a solution. Note the relation

If $\scriptstyle \eta = 0$ ,then $\alpha \equiv \gamma , \beta \equiv \delta ( \mathrm { m o d } F ^ { \bullet 2 } )$ so certainly $\varphi ( \alpha , \beta ) { = } \varphi ( \gamma , \delta )$ If $\xi = 0$ a similar argument shows that

$$
\varphi \left( \gamma , \delta \right) = \varphi \left( \beta , \alpha \right) .
$$

But the symmetry relation

$$
\varphi ( \beta , \alpha ) { = } \varphi ( \alpha , \beta ) ^ { - 1 } { = } \varphi ( \alpha , \beta )
$$

can easily be established by expanding the identity $\varphi ( \alpha \beta , - \alpha \beta ) = 1$ Finally, suppose that $\xi \neq 0$ and $\eta \neq 0$ Then

hence

$$
\alpha \xi ^ { 2 } / \gamma + \beta \eta ^ { 2 } / \gamma = 1
$$

$$
\varphi ( \alpha \gamma , \beta \gamma ) = \varphi ( \alpha \xi ^ { 2 } / \gamma , \beta \eta ^ { 2 } / \gamma ) = 1 .
$$

Expanding, it follows that

$$
\varphi ( \alpha , \beta ) = \overset { \cdot } { \phi } ( \gamma , \alpha \beta \gamma )
$$

which completes the proof, since $\alpha \beta \gamma \equiv \delta$ modulo $F ^ { \bullet 2 }$ ：□

(5.6) Lemma. Suppose that the two inner product spaces

$$
\begin{array} { r l } { \langle \alpha _ { 1 } \rangle \oplus \cdots \oplus \langle \alpha _ { n } \rangle } & { { } a n d \quad \langle \beta _ { 1 } \rangle \oplus \cdots \oplus \langle \beta _ { n } \rangle } \end{array}
$$

have the same rank and Witt class. Then it is possible to pass from the sequence α1,.., αn to the sequence β1,..., βn by changing just two entries at a time, preserving the Witt class at every stage.

The proof of this classical lemma wil be deferred until the end of $\ S 5$ ， Now for any inner product space $X$ which possesses an orthogonal basis,

$$
X \cong \langle \alpha _ { 1 } \rangle \oplus \cdots \oplus \langle \alpha _ { n } \rangle ,
$$

we defined the Hasse invariant $H _ { \varphi } ( X ) \in \mathbf { Z } ^ { \bullet } ~$ o be the product $\prod _ { i < j } \varphi ( \alpha _ { i } , \alpha _ { j } ) .$ If X does not possess an orthogonal basis, then it must be symplectic, with $\boldsymbol { \mathsf { \Sigma } }$ of characteristic 2,and we set $H _ { \varphi } ( X ) = 1$

(5.7) Theorem. The Hasse invariant $H _ { \varphi } ( X )$ does not depend on the choice of orthogonal decomposition. In fact if two spaces $X$ and $X ^ { \prime }$ have the same rank and Witt class,then $H _ { \varphi } ( X ) = H _ { \varphi } ( X ^ { \prime } ) .$ The identity

$$
\begin{array} { r } { { \cal H } _ { \varphi } ( X \oplus Y ) { = } { \cal H } _ { \varphi } ( X ) { \cal H } _ { \varphi } ( Y ) \varphi ( \operatorname* { d e t } X , \operatorname* { d e t } Y ) } \end{array}
$$

is satisfied for all X and Y.

The proof, making use of (5.5) and (5.6), is straightforward and will be left to the reader.□

Let $s$ be a split inner product space of rank $n { = } 2 m$ Then $s$ has the same rank and Witt class as the m-fold sum $m ( \langle 1 \rangle \oplus \langle - 1 \rangle )$ .It follows easily that

$$
H _ { \varphi } ( S ) = \varphi ( - 1 , 1 ) ^ { m ( m - 1 ) / 2 } .
$$

This invariant is not always equal to 1； but if $n { = } 2 m { \equiv } 0 \mathrm { m o d } 8$ then certainly $H _ { \varphi } ( S ) = 1$ ，

Definition. For any Witt class w in the fundamental ideal I, the Hasse-Witt invariant $h _ { \varphi } ( w )$ is defined as follows. Choose a representative inner product space $X$ for the Witt class w so that

$$
\operatorname { r a n k } ( X ) { \equiv } 0 { \pmod { 8 } } ,
$$

and set $h _ { \varphi } ( w )$ equal to the Hasse invariant $H _ { \varphi } ( X )$

This function is well defined, since if $X \sim X ^ { \prime }$ with rank $( X ) \equiv \mathbf { r a n k } \left( X ^ { \prime } \right)$   
$\equiv 0 ( { \ m o d } 8 )$ then $X \oplus S \cong X ^ { \prime } \oplus S ^ { \prime }$ with rank $( S ) \equiv$ rank $( S ^ { \prime } ) { \equiv } 0$ (mod 8), and   
therefore $H _ { \varphi } ( X ) = H _ { \varphi } ( X \oplus S ) = H _ { \varphi } ( X ^ { \prime } \oplus S ^ { \prime } ) = H _ { \varphi } ( X ^ { \prime } ) .$

(5.8) Theorem. For each symbol $\overline { { \varphi } }$ the restriction of the Hasse-Witt function $h _ { \varphi }$ to the ideal $I ^ { 2 }$ yields $a$ well defined homomorphism

$$
h _ { \varphi } \colon I ^ { 2 } \to \mathbf { Z ^ { \bullet } } .
$$

An element w of $I ^ { 2 }$ is annihilated by every one of these homomorphisms $h _ { \varphi }$ if and only if w∈I.

(Compare [Milnor, 1970].) In fact, the proof will show that the group of all symbols $\varphi$ on $F$ with values in $\mathbf { Z ^ { \bullet } }$ is canonically isomorphic to the group $\mathrm { H o m } ( I ^ { 2 } / I ^ { 3 } , { \bf Z ^ { \bullet } } )$

Proof of (5.8). The identity

$$
h _ { \varphi } ( w + w ^ { \prime } ) = h _ { \varphi } ( w ) h _ { \varphi } ( w ^ { \prime } ) \varphi \left( d ( w ) , d ( w ^ { \prime } ) \right)
$$

is evidently satisfied for any w and $w ^ { \prime }$ in the fundamental ideal I.If $w \in I ^ { 2 } ,$ so that $d ( w ) = 1 ,$ it follows that

$$
h _ { \varphi } ( w + w ^ { \prime } ) = h _ { \varphi } ( w ) h _ { \varphi } ( w ^ { \prime } ) .
$$

Next let us compute the Hasse-Witt invariant of a product $w \langle \beta \rangle$ ： Setting $w = \langle _ { \mathcal { I } } { \alpha } _ { 1 } \rangle + \dots + \langle { \alpha } _ { m } \rangle$ with $m \equiv 0$ (mod 8), we have

$$
\begin{array} { c } { { h _ { \varphi } ( w \left. \beta \right. ) = \displaystyle \prod _ { i < j } \varphi ( \alpha _ { i } \beta , \alpha _ { j } \beta ) = h _ { \varphi } ( w ) \varphi ( \alpha _ { 1 } . . . \alpha _ { m } , \beta ) ^ { m - 1 } \varphi ( \beta , \beta ) ^ { m ( m - 1 ) / 2 } } } \\ { { { } } } \\ { { = h _ { \varphi } ( w ) \varphi \left( d ( w ) , \beta \right) . } } \end{array}
$$

For any w' ∈ I,setting $w ^ { \prime } { = } \langle \beta _ { 1 } \rangle { + } \cdots { + } \langle \beta _ { n } \rangle$ with $\scriptstyle n \equiv 0$ (mod 4), we have

In particular, if $w \in I$ and $w ^ { \prime } \in I ^ { 2 }$ then $h _ { \varphi } ( w w ^ { \prime } ) = 1$ .Therefore each $h _ { \varphi }$ annihilates $I ^ { 3 }$ ,and gives rise to a homomorphism

$$
h _ { \varphi } \colon I ^ { 2 } / I ^ { 3 } \to \mathbf { Z } ^ { \bullet } .
$$

Conversely， given any homomorphism $g \colon I ^ { 2 } / I ^ { 3 } \to \mathbf { Z ^ { \bullet } }$ let $\varphi$ denote the symbol $\varphi ( \alpha , \beta ) = g \bigl ( ( \langle \alpha \rangle - \langle 1 \rangle ) ( \langle \beta \rangle - \langle 1 \rangle ) \bigr ) .$

Using the congruence

$$
\scriptstyle \langle \alpha \alpha ^ { \prime } \rangle - \langle 1 \rangle \equiv \langle \alpha \rangle - \langle 1 \rangle + \langle \alpha ^ { \prime } \rangle - \langle 1 \rangle \mod I ^ { 2 }
$$

we see that $\varphi$ is bimultiplicative;and if $\alpha + \beta = 1$ then the isomorphism

$$
\langle \alpha \rangle \oplus \langle \beta \rangle \cong \langle 1 \rangle \oplus \langle \alpha \beta \rangle
$$

implies that $\varphi ( \alpha , \beta ) = 1$ . Since the associated homomorphism

$$
\not h _ { \varphi } \colon I ^ { 2 } / I ^ { 3 } \to \mathbf { Z } ^ { \bullet }
$$

coincides with $g$ on every generator $( \langle { \alpha } \rangle - \langle { 1 } \rangle )$ $( \langle \beta \rangle - \langle 1 \rangle )$ of $I ^ { 2 }$ ,it follows that $h _ { \varphi } = g$ Now if an element $w \in { \cal I } ^ { 2 }$ is annihilated by every $h _ { \varphi }$ ， then it is annihilated by every homomorphism from $I ^ { 2 } / I ^ { 3 }$ to $\mathbf { Z ^ { \bullet } }$ and it follows that $\overline { { w \in I ^ { 3 } } }$ □

(5.9) The classical examples. If $F$ is a finite field, then an elementary argument due to Steinberg shows that every symbol on $\boldsymbol { F }$ is trivial, hence the ideal $I ^ { 2 } { \subset } W ( F )$ is zero. Compare Chapter IV, $\ S 1 . 5$

If $F$ is a finite extension of the field of $p$ -adic numbers,then there is precisely one non-trivial symbol on $F$ with values in $\mathbf { Z ^ { \bullet } }$ ，hence $I ^ { 2 } / I ^ { 3 }$ is cyclic of order 2.In fact, the rank,determinant, and Hasse invariant form a complete system of invariants for an inner product space over $F .$ (See [O'Meara,p.170].) It follows easily that the ideal $I ^ { 2 }$ is cyclic of order 2,and that $\scriptstyle { \mathbf { } } { \mathbf { } } { \mathbf { } } ^ { 3 } = 0$ ，

Now suppose that $\pmb { F }$ isa finite extension of the field of rational numbers. In this case, a complete invariant for an inner product space over $F$ is provided by the rank, determinant, and total signature, together with the Hasse invariants associated with all of the various local completions of $F$ ([O'Meara,p.189]). For an element w in the ideal $I ^ { 3 } { \subset } W ( F ) .$ it follows easily that the signature $\sigma ( w )$ provides a complete invariant. In fact the homomorphism $\sigma$ maps $I ^ { 3 }$ bijectively to the ideal $8 \mathbf { Z } ^ { \Omega }$ In particular in the totally imaginary case $\Omega = \emptyset$ it follows that $I ^ { 3 } { = } 0$

Note that the“length”of the chain of ideals $I { \supseteq } I ^ { 2 } { \supseteq } I ^ { 3 } { \supseteq } \cdots$ in the case of a number field is either 2 or o according as-1 is a sum of squares or not. Here is a computation of this “length” in a quite different case.

Let $F$ be a field of characteristic 2. Then the homomorphism $\xi \mapsto \xi ^ { 2 }$ maps $F$ isomorphically onto a subfield $F ^ { 2 }$ . The degree of $F$ over $F ^ { 2 }$ isa number of the form $2 ^ { \imath } { : }$ ,where i can take the values O,1, 2.,..., $\infty$ .Note that $F$ is perfect if and only if $\imath = 0$ If $E$ is a finite extension of degree $n$ over $F ,$ then $E ^ { 2 }$ has degree n over $F ^ { 2 }$ ,hence $E$ has degree $2 ^ { \iota }$ over $E ^ { 2 }$ In other words this measure t of imperfection is invariant under finite extensions of F.It is also invariant under arbitrary separable algebraic extensions. However $\imath$ increases by 1 under a simple transcendental extension. (For another characterization of $\imath$ see [Zariski and Samuel, p. 130].)

(5.10) Theorem. If the field $F$ of characteristic 2 has degree $2 ^ { \iota }$ over $F ^ { 2 }$ then the ideal $I ^ { n } { \subset } W ( F )$ is zero for $n > \iota$ and non-zero for $n { \stackrel { < } { = } } \iota$

For example if $F$ is finite then $\imath = 0$ ，so the fundamental ideal $I { = } I ^ { 1 }$ itself is zero.

Proof. The ideal ${ \cal { I } } ^ { n }$ is additively generated by products of the form

$$
X = ( \langle 1 \rangle \oplus \langle \alpha _ { 1 } \rangle , \overleftrightarrow { \alpha \cdots \otimes ( \langle 1 \rangle \oplus \langle \alpha _ { n } \rangle ) } .
$$

By Pfister's theorem (4.3), every such product is either anisotropic or split.But if $n > \iota$ ，then the $2 ^ { n }$ products $\mathfrak { X } _ { j _ { 1 } } \mathfrak { X } _ { j _ { 2 } } . . . \mathfrak { X } _ { j _ { k } }$ ，where $\{ j _ { 1 } , \ldots , j _ { k } \}$ ranges over all subsets of $\{ 1 , \ldots , n \}$ ， cannot be linearly independent over $F ^ { 2 }$ Hence $X$ ,being the orthogonal sum of the $\langle \alpha _ { j _ { 1 } } . . . \alpha _ { j _ { k } } \rangle$ ,cannot be anisotropic. Therefore $X { \sim } 0 .$ ,and it follows that ${ \overline { { I ^ { n } } } } { = } 0$

To conclude $\ S 5$ ,we prove the Lemma (5.6). Suppose that

$$
\langle \alpha _ { 1 } \rangle \oplus \cdots \oplus \langle \alpha _ { n } \rangle \sim \langle \beta _ { 1 } \rangle \oplus \cdots \oplus \langle \beta _ { n } \rangle .
$$

We must prove by induction on $\pmb { n }$ that we can change the $\alpha _ { i }$ two at a time, preserving the Witt class, so as to transform one sequence to the other. Certainly any permutation of the $\alpha _ { i }$ can be obtained as a composition of permutation involving only two elements. To start the induction, the statement is certainly true for $n = 2$

First suppose that the two spaces are anisotropic,and hence isomorphic. Then the equation

$$
\beta _ { 1 } = \alpha _ { 1 } \xi _ { 1 } ^ { 2 } + \cdots + \alpha _ { n } \xi _ { n } ^ { 2 }
$$

has a solution. Let $k$ be the number of indices i for which $\boldsymbol { \xi } _ { i } \neq \boldsymbol { \theta } _ { \mathrm { \ell } }$ The proof will be based on a subsidiary induction on k.

f $k = 1$ say $\beta _ { 1 } = \mathfrak { a } _ { 1 } \xi _ { 1 } ^ { 2 }$ ，then $\langle { \alpha _ { 1 } } \rangle { \cong } \langle { \beta _ { 1 } } \rangle$ ，hence $\langle \alpha _ { 2 } \rangle \oplus \cdots \oplus \langle \alpha _ { n } \rangle \sim$ $\langle \beta _ { 2 } \rangle \oplus \cdots \oplus \langle \beta _ { n } \rangle$ ,and the conclusion follows by induction on n. If $k \geq 2 .$ then say $\xi _ { 1 } \neq 0$ and $\xi _ { 2 } \neq 0$ ,and we may assume that the field element

$$
\gamma = \alpha _ { 1 } \zeta _ { 1 } ^ { 2 } + \alpha _ { 2 } \zeta _ { 2 } ^ { 2 }
$$

is non-zero. Hence $\langle \alpha _ { 1 } \rangle \oplus \langle \alpha _ { 2 } \rangle \cong \langle \gamma \rangle \oplus \langle \delta \rangle$ for some $\delta$ Substituting 2 and $\delta$ for ${ \pmb { \alpha } } _ { 1 }$ and $a _ { 2 }$ , the conclusion follows by induction on k.

Suppose then that the two spaces are not anisotropic. Then the

![](images/66d7d33d3e04d065c38c043910732570ad41dd8e8abd1859d006a5cef221c983.jpg)

# Chapter IV. Discrete Valuations and Dedekind Domains

The first section of this chapter defines the two residue class form homomorphisms associated with a discrete valuation of a field. Section 2 uses the second residue class form homomorphisms to compute the Witt ring $W ( \mathbf { Q } )$ of the rational numbers,and to give a new proof that $W ( \mathbf { Z } ) { \cong } \mathbf { Z }$ Section 3 applies a similar construction to an arbitrary Dedekind domain $D$ with quotient field $F ,$ constructing an exact sequence

$$
0 \to W ( D ) \to W ( F ) \to \bigoplus W ( D / \mathfrak { p } ) ,
$$

where the direct sum extends over all maximal ideals $\mathfrak { p }$ of $D$ .The final section applies this sequence to the special case of the integers in a number field.

# \$1. The Homomorphism 0,: W(F)→ W(F)

Recall that a discrete valuation $v$ on a field $F$ is a homomorphism from $F ^ { \bullet }$ onto the additive group $\mathbf { Z }$ satisfying

$$
v ( \alpha + \beta ) \mathop { \geq } \mathrm { M i n } \left( v ( \alpha ) , v ( \beta ) \right)
$$

for $\pmb { \alpha }$ $\beta _ { : }$ $\alpha + \beta \neq 0$ It is convenient to set $v ( 0 ) = + \infty$ . The associated valuation ring $\mathfrak { D }$ consists of all $\mathbf { \boldsymbol { \alpha } } \in F$ with $v ( x ) { \geq } 0$ .This ring has a unique maximal ideal $\mathfrak { P }$ consisting of all $\pmb { \alpha }$ with $v ( { \boldsymbol { \alpha } } ) > 0$ The quotient $\scriptstyle { \overline { { F } } } = { \overline { { \mathfrak { D } } } } / { \mathfrak { P } }$ is called the residue class field. The image of any $u \in \mathfrak { D } ^ { \bullet }$ will be denoted by $\overrightharpoon { u } \in \overrightharpoon { F } ^ { \bullet }$

We will construct an additive homomorphism $\partial _ { v }$ $W ( { \boldsymbol { F } } ) \to W ( { \boldsymbol { \overline { { F } } } } ) .$ well defined up to multiplication by units of the form $\langle \overline { { u } } \rangle$ in $W ( { \overline { { F } } } )$ In order to define $\partial _ { v }$ , it is convenient to give a presentation of $W ( { \boldsymbol { F } } )$ by generators and relations.

(1.1) Lemma (Wit). The additive group $W ( { \boldsymbol { F } } )$ is generated'by the -elements $\langle x \rangle$ with $\alpha \in F ^ { \bullet } ,$ subject only to the following relations and their consequences

(i $\langle { \alpha } \rangle { = } \langle { \alpha } \xi ^ { 2 } \rangle$ for $\xi \neq 0$ (ii) $\langle { \alpha } \rangle + \langle - { \alpha } \rangle = 0 ;$ (ii) $\langle \alpha \rangle + \langle \beta \rangle = \langle \alpha + \beta \rangle + \langle \alpha \beta ( \alpha + \beta ) \rangle$ for $\alpha + \beta \neq 0 .$

Proof. These three relations are clearly satisfied in $W ( F ) .$ and the fact that every relation follows from these is an easy consequence of Chapter III, $\ S 5 . 6$ □

Now choose a prime element $\pi \in \mathfrak { S }$ ,that is an element $\pi$ with $v ( \pi ) = 1$ ， so that $\pi { \mathfrak { D } } = { \mathfrak { P } }$ .Then every element of $F ^ { \bullet }$ can be written uniquely as a product $\pi ^ { i } u$ with $u \in \mathfrak { D } ^ { \bullet }$ ：

(1.2) Lemma (Springer, Knebusch). Fixing $\pi$ ， and fixing an integer $k { = } 0 o r 1$ ,there is one and only one additive homomorphism

which maps each generator (πiu> to either <u> or O according as i=k (mod 2) or i±k (mod 2).

Proof. By (1.1) we need only verify that each of the defining relations for $W ( { \boldsymbol { F } } )$ maps to a valid relation in $W ( { \overline { { F } } } ) .$ ，Only the third relation presents any problem. It will be convenient to let the symbol ε, stand for either 1 or O according as $i \equiv k$ ori $k$ (mod 2). If

$$
\pi ^ { h } u _ { 1 } + \pi ^ { i } u _ { 2 } = \pi ^ { j } u _ { 3 } ,
$$

then we must prove that

$$
\varepsilon _ { h } \left. \overline { { u } } _ { 1 } \right. + \varepsilon _ { i } \left. \overline { { u } } _ { 2 } \right. = \varepsilon _ { j } \left. \overline { { u } } _ { 3 } \right. + \varepsilon _ { h + i + j } \big \langle \overline { { u } } _ { 1 } \overline { { u } } _ { 2 } \overline { { u } } _ { 3 } \big \rangle
$$

in $W ( { \overline { { F } } } ) .$ . After dividing by a suitable power of $\pi$ (and interchanging the roles of $\psi ^ { 0 }$ and $\psi ^ { 1 }$ if necessary) we may assume that two of the three numbers $h , i , j$ are O,and that the third is $\geq 0$

Case 1. If $h = i = j = 0 ,$ then ${ \overline { { u } } } _ { 1 } + { \overline { { u } } } _ { 2 } = { \overline { { u } } } _ { 3 } ,$ and the required equation certainly follows.

Case 2. If $h > i = j = 0 .$ then $\bar { u } _ { 2 } = \bar { u } _ { 3 }$ hence $\langle \bar { u } _ { 1 } \rangle = \langle \bar { u } _ { 1 } \bar { u } _ { 2 } \bar { u } _ { 3 } \rangle$ and the equation follows. The case $i > 0$ is completely analogous.

Case 3. If $\ 0 = h = i < j$ ,then ${ \bar { u } } _ { 1 } + { \bar { u } } _ { 2 } = 0$ hence

$$
\langle \bar { u } _ { 1 } \rangle + \langle \bar { u } _ { 2 } \rangle = 0 , ~ \langle \bar { u } _ { 3 } \rangle + \langle \bar { u } _ { 1 } \bar { u } _ { 2 } \bar { u } _ { 3 } \rangle = 0 ,
$$

and again the required equation follows. This completes the proof.Q

Definition. These homomorphisms $\psi ^ { 0 }$ and 1 from W(F) to W(F) are called the two residue class form homomorphisms associated with the valuation $\boldsymbol { v }$ We will be particularly interested in $\psi ^ { 1 }$ ,and will use the

alternative notation

$$
\partial _ { v } \colon W ( F ) \to W ( { \overline { { F } } } )
$$

for $\psi ^ { 1 }$ . Note that $\psi ^ { 0 }$ is well defined,but that $\psi ^ { 1 } = \partial _ { v } $ depends on the particular choice of $\pi$ ：

Let $\mathfrak { D } \subset F$ be the valuation ring associated with $v ,$ and let $W ( { \mathfrak { S } } ) \to$ W(F) be the natural ring homomorphism.

(1.3) Lemma. The composition $W ( { \mathfrak { D } } ) { \to } W ( F ) \xrightarrow { \psi ^ { 1 } } W ( { \overline { { F } } } )$ is zero.

In fact we will see in $\ S 3$ that the sequence $0 \to W ( { \mathfrak { O } } ) \to W ( F ) \to$ $W ( { \overline { { F } } } ) \to 0$ is exact.

Proof of (1.3). Since $\mathfrak { D }$ is a local ring,any inner product space over $\mathfrak { D }$ can easily be expressed as an orthogonal sum of inner product spaces of rank 1, with inner product matrix $\mathit { \Pi } \left( u \right)$ ,and inner product spaces of rank 2 with inner product matrix of the form

$$
{ \binom { \alpha } { 1 } } \quad { \binom { 1 } { \beta } }
$$

with $\alpha { \equiv } 0 \mathrm { m o d } \ \mathfrak { P }$ . In the first case, the corresponding element $\langle u \rangle$ in $W ( { \boldsymbol { F } } )$ certainly satisfies $\psi ^ { 1 } \langle u \rangle { = } 0$ In the second case, if $\alpha \neq 0$ the corresponding element in $W ( { \boldsymbol { F } } )$ can be written as a sum $( \alpha ) + \langle \alpha ( \alpha \beta - 1 ) \rangle$ with $\alpha \beta - 1 \equiv - 1 \bmod \mathfrak { P }$ Evidently $\psi ^ { 1 }$ annihilates any such sum. Finally, if $\scriptstyle { \alpha = 0 , }$ then the given summand is split and hence corresponds to the zero element_ in the Witt ring. Thus each orthogonal summand maps to zero in $W ( { \overline { { F } } } ) _ { : }$ ,and the conclusion follows.□

(1.4) Lemma. Each homomorphism $\psi ^ { k }$ ： $W ( { \boldsymbol { F } } ) \to W ( { \overline { { \boldsymbol { F } } } } )$ carries theideal $I ^ { n } ( F )$ onto $I ^ { n - 1 } ( \overline { { F } } )$ for $n { \stackrel { } { = } } 1$ ：

Proof. Inspection shows that the sum ${ \psi } ^ { 0 } + { \psi } ^ { 1 }$ is a ring homomorphism which carries the ideal $I ( F )$ to $I ( \overline { { F } } ) .$ ，and hence carries $I ^ { n } ( F )$ to ${ \cal I } ^ { n } ( \overline { { { \cal F } } } )$ Thus for any $w _ { n } \in I ^ { n } ( F )$ we have

$$
\begin{array} { r } { \overline { { \psi ^ { 1 } ( w _ { n } ) \equiv - \psi ^ { 0 } ( w _ { n } ) \pmod { I ^ { n } ( \overline { { F } } ) } } } . } \end{array}
$$

Suppose inductively that $\psi ^ { 0 } ( w _ { n } ) { \equiv } 0 \left( \mathrm { m o d } I ^ { n - 1 } ( \overline { { F } } ) \right)$ . Then for any $w \in I ( F )$ we have

$$
\begin{array} { r } { \psi ^ { 0 } \left( w w _ { n } \right) = \psi ^ { 0 } \left( w \right) \psi ^ { 0 } \left( w _ { n } \right) + \psi ^ { 1 } ( w ) \psi ^ { 1 } \left( w _ { n } \right) } \\ { \equiv \psi ^ { 0 } \left( w \right) \psi ^ { 0 } \left( w _ { n } \right) - \psi ^ { 1 } \left( w \right) \psi ^ { 0 } \left( w _ { n } \right) } \end{array}
$$

since °(w)-1(w) clearly belongs to $I ( { \overline { { F } } } ) .$ This completes the induction. Since every generator $( < \overline { { 1 } } ) + < \overline { { u } } _ { 1 } > ) . . . ( < \overline { { 1 } } > + < \overline { { u } } _ { n - 1 } > )$ of $I ^ { n - 1 } ( \overline { { F } } )$ isthe

image, under either $\psi ^ { 0 }$ or $\psi ^ { 1 }$ ,of the generator

$$
\left( \langle 1 \rangle + \langle \pi \rangle \right) \left( \langle 1 \rangle + \langle u _ { 1 } \rangle \right) \ldots \left( \langle 1 \rangle + \langle u _ { n - 1 } \rangle \right)
$$

of $I ^ { n } ( F ) _ { : }$ ,this proves the lemma.□

We will be particularly interested in residue class fields $\scriptstyle { \overline { { F } } }$ which are finite. Let $\mathbf { F } _ { q }$ denote the field with $\mathbf { \Delta } \mathbf { q }$ elements.

(1.5) Lemma. For any finite field $\mathbf { F } _ { q }$ the ideal $I ( \mathbf { F } _ { q } )$ is either zero or cyclic oforder 2 according as q is even or odd. The additive group of $W ( { \mathbf { F } _ { q } } )$ is either cyclic of order 2,cyclic of order 4,or non-cyclic of order 4 according as $q$ is even, $q \equiv 3$ (mod 4), or $q \equiv 1$ (mod 4).

Proof. Given $\pmb { \alpha }$ ${ \boldsymbol { \beta } } { \in } \mathbf { F } _ { q } ^ { \bullet }$ , the equation

$$
\alpha \xi ^ { 2 } + \beta \eta ^ { 2 } = 1
$$

has a solution by Chapter II, $\ S 3 . 3$ .Therefore

$$
( \alpha ) \oplus \langle \beta \rangle \cong \langle 1 \rangle \oplus \langle \alpha \beta \rangle ,
$$

and it follows that the ideal $I ^ { 2 } ( \mathbf { F } _ { q } )$ is zero.Using Chapter II, $\ S 5 . 2 ,$ it follows that

$$
I ( \mathbf { F } _ { q } ) { \cong } \mathbf { F } _ { q } ^ { { \bullet } } / \mathbf { F } _ { q } ^ { { \bullet } 2 } ,
$$

where the group $\underline { { \mathbf { F } _ { q } ^ { \bullet } } }$ is cyclic of order $\overline { { q - 1 } }$ .Hence this ideal $I ( \mathbf { F } _ { q } )$ has order 1 or 2 according as $\boldsymbol { \mathscr { q } }$ -1 is odd or even.

If $q \equiv 3 ( { \bf m o d } 4 )$ ,then-1is not a square in $\mathbf { F } _ { q }$ (compare Chapter II, $\ S 8 . 1 )$ ，hence $\langle - 1 \rangle \ I \yen 1 \rangle$ ，so $\langle 1 \rangle \oplus \langle 1 \rangle \nsim 0$ and it follows easily that $W ( \mathbf { F } _ { q } ) { \cong } \mathbf { Z } / 4 \mathbf { Z }$ .On the other hand if $q$ 丰3 (mod 4), then $\langle - 1 \rangle \cong \langle 1 \rangle$ ， and it follows that $W ( \mathbf { F } _ { q } )$ is an algebra over $\mathbf { Z } / 2 \mathbf { Z }$ ，This completes the proof.□

# § 2. Computation of W(Q)

This section will completely describe the additive structure of the Witt ring W(Q). Also it will give another proof that $W ( \mathbf { Z } ) { \cong } \mathbf { Z } ,$ not making use of the Hasse-Minkowski theorem.

For each prime number $p$ the $p$ -adic valuation of $\mathbf { Q }$ gives rise to an additive homomorphism

$$
\psi ^ { 1 } = \partial _ { p } \colon W ( \mathbf { Q } ) \to W ( \mathbf { F } _ { p } ) .
$$

For any fixed w in W(Q),it is clear that $\partial _ { p } ( w ) = 0$ for almost all $p$ Therefore -we can aggregate these homomorphisms $\partial _ { { p } }$ into one homomorphism 0: $W ( \mathbf { Q } ) \to \bigoplus W ( \mathbf { F } _ { p } ) .$ Let i denote the unique ring homomorphism from Z to W(Q).

(2.1) Theorem. The sequence

$$
0 \to \mathbf { Z } \xrightarrow { \textit { i } } W ( \mathbf { Q } ) \xrightarrow { \textit { 0 } } \oplus W ( \mathbf { F } _ { p } ) \to 0
$$

is split exact.

Here the direct sum extends over all prime numbers $p$ .(Thus in order to describe the most classical of Witt rings $W ( \mathbf { Q } )$ we are led to consider inner product spaces over finite fields, including the field $\mathbf { F } _ { 2 }$ which is excluded in the classical theory.) For the structure of $W ( \mathbf { F } _ { p } )$ ,see (1.5).

Proof of (2.1). For each integer $k \geq 1$ ,let $L _ { k }$ denote the subring of $W ( \mathbf { Q } )$ generated by the elements $\langle 1 \rangle , \langle 2 \rangle , . . . , \langle k \rangle$ . Then clearly

$$
L _ { 1 } { \subset } L _ { 2 } { \subset } L _ { 3 } { \subset } \cdots
$$

with union equal to $W ( \mathbf { Q } )$ Thering $L _ { 1 }$ is evidently isomorphic to $\mathbf { Z }$ Note that $L _ { k } = L _ { k - 1 }$ unless $k$ is prime.

Henceforth we will ignore the ring structure and think of $L _ { k }$ as an additive group.

(2.2) Lemma. For each prime number $p$ ，the additive homomorphism $\partial _ { p } \colon W ( \mathbf { Q } ) \to W ( \mathbf { F } _ { p } )$ induces an isomorphism

$$
L _ { p } / L _ { p - 1 } \to W ( \mathbf { F } _ { p } ) .
$$

Proof. The homomorphism $\partial _ { { p } }$ clearly annihilates $\scriptstyle L _ { p - 1 }$ and maps $L _ { p }$ onto $W ( \mathbf { F } _ { p } )$ .We will need the following subsidiary lemma.

(2.3) Lemma. If the numbers $n _ { i }$ and n satisfy $0 < | n _ { i } | < p , 0 < | n | < p , a n d$

$$
n _ { 1 } \ldots n _ { r } \equiv n { \pmod { p } } ,
$$

then

$$
\langle p n _ { 1 } \ldots n _ { r } \rangle \equiv \langle p n \rangle { \pmod { L _ { p - 1 } } } .
$$

Proof. First consider the case $r = 2$ Then

$$
n _ { 1 } n _ { 2 } = n + k p
$$

$$
| k | \leq ( ( p - 1 ) ^ { 2 } + ( p - 1 ) ) / p < p .
$$

If $k = 0$ , there is nothing to prove. Otherwise, tensoring the isomorphism

$$
\langle n \rangle \oplus \langle k p \rangle \cong \langle n _ { 1 } n _ { 2 } \rangle \oplus \langle n _ { 1 } n _ { 2 } n k p \rangle
$$

with $\langle p \rangle$ ,we obtain

$$
\langle p n \rangle \oplus \langle k \rangle \cong \langle p n _ { 1 } n _ { 2 } \rangle \oplus \langle n _ { 1 } n _ { 2 } n k \rangle
$$

and hence $\langle p n \rangle \equiv \langle p n _ { 1 } n _ { 2 } \rangle ( { \mathrm { m o d } } L _ { p - 1 } )$ .For any $n _ { 3 } , \ldots , n _ { r }$ which are less than $p$ in absolute value, it follows that

$$
\langle p n n _ { 3 } \ldots n _ { r } \rangle \equiv \langle p n _ { 1 } n _ { 2 } n _ { 3 } \ldots n _ { r } \rangle { \pmod { L _ { p - 1 } } } .
$$

A straightforward induction now completes the proof of (2.3). 0

Proof of (2.2). For each generator <n> of W(Fp), we can choose a representative n with |n|<p,and lift <n> to the generator <pn> ofLp/Lp-1· We will check that these lifted elements satisfy all of the defining relations for $W ( \mathbf { F } _ { p } )$ .(Compare (1.1).) Thus if

$$
n ^ { \prime } { \equiv } n m ^ { 2 } { \pmod { p } }
$$

where n',n,m are less than p in absolute value, then it follows from (2.3) that

$$
\langle p n ^ { \prime } \rangle \equiv \langle p n m ^ { 2 } \rangle = \langle p n \rangle { \pmod { L _ { p - 1 } } } .
$$

Clearly <p n>+<p(-n)>=O; and if n1 +n2=n,where we may assume that $n _ { 1 }$ and $n _ { 2 }$ satisfy $- p < n _ { 1 } < 0 < n _ { 2 } < p$ ,then

$$
\langle p n _ { 1 } \rangle \oplus \langle p n _ { 2 } \rangle \cong \langle p n \rangle \oplus \langle p n n _ { 1 } n _ { 2 } \rangle .
$$

Thus these elements <pn> modulo Lp-1 satisfy all of the defining relations for W(Fp), and therefore generate a subgroup of Lp/Lp-1 which maps isomorphically to $W ( \mathbf { F } _ { p } )$ Since it follows from (2.3) that these elements <pn> generate Lp modulo Lp-1, this completes the proof.□

Proof of Theorem (2.1). We will show by induction on $k$ that the homomorphism

-is surjective,with kernel equal to L_=Z.Certainly this statement is true for k=1. Suppose then that it is true for k-1. We may assume that k is prime. Given an element in the direct sum, by (2.2) there exists an element w in Lk whose image has the correct k-th coordinate. Subtracting the image of w, surjectivity follows by induction.

Similarly, if $w \in L _ { k }$ maps to zero, then (2.2) implies that $w \in L _ { k - 1 }$ and it follows by induction that $w \in L _ { 1 } \cong \mathbf { Z }$

Now passing to the direct limit as $k \to \infty .$ ， we see that the required sequence

$$
\begin{array} { r } { \left. \begin{array} { r l r } { \Theta \longrightarrow \mathbf { Z } \longrightarrow W ( \mathbf { Q } ) \longrightarrow \bigoplus W ( \mathbf { F } _ { p } ) \longrightarrow 0 } \end{array} \right. } \end{array}
$$

is exact. Using the signature homomorphism $W ( \mathbf { Q } ) \to \mathbf { Z }$ , it follows that it is split exact. In fact the spliting is unique, since all of the groups $W ( \mathbf { F } _ { p } )$ are torsion. This completes the proof of (2.1).

As one corollary of (2.1), we obtain a weak form of the Hasse-Minkowski theorem.

(2.4) Corollary. If an element w in the Witt ring W(Q) maps to zero in the Witt ring W(Qp) of the p-adic numbers for every prime p, and also maps to zero in W(R), then w ${ \bf \Lambda } = { \bf 0 }$

Proof. This follows since the homomorphism $\partial _ { p } \colon W ( \mathbf { Q } ) \to W ( \mathbf { F } _ { p } )$ can be factored through $W ( \mathbf { Q } _ { p } )$ □

(2.5) Corollary. If $I$ denotes the fundamental ideal in $W ( \mathbf { Q } ) ,$ then $I ^ { 3 }$ is the free additive group generated by $8 \langle 1 \rangle$

P $r o o f . \mathrm { I f } \ w \in I ^ { 3 } ( \mathbf { Q } ) , \mathrm { t h e n } \ \partial _ { p } ( w ) \in I ^ { 2 } ( \mathbf { F } _ { p } ) = 0 ,$ by (1.4) and (1.5). Hence w is a multiple of $\left. 1 \right.$ . In fact w must be a multiple of 8<1> since the signature homomorphism carries $I ^ { n } ( \mathbf { Q } )$ to $2 ^ { n } \mathbf { Z }$ □

Now let us give an alternative proof of Lemma (4.1) of Chapter II.

(2.6) Corollary. Let $X$ be any inner product space over Z. Then the induced inner product space $\mathbf { Q } \otimes X$ over $\mathbf { Q }$ is isomorphic to an orthogonal sum of copies of <1> and $\langle - 1 \rangle$ ：

Proof. Let $\mathbf { Z } _ { ( p ) } { \subset } \mathbf { Q }$ denote the valuation ring associated with the $p$ -adic valuation of Q. Since the natural homomorphism $\overline { { W ( \mathbf { Z } ) \to W ( \mathbf { Q } ) } }$ factors through $W ( \mathbf { Z } _ { ( p ) } ) .$ it follows from (1.3) that the composition

$$
W ( \mathbf { Z } ) {  } W ( \mathbf { Q } ) {  } \oplus W ( \mathbf { F } _ { p } )
$$

is zero. Hence the image of $W ( \mathbf { Z } ) \mathrm { i n } W ( \mathbf { Q } )$ consists precisely of all positive or negative multiples of $\langle 1 \rangle$ .Together with Chapter I $\ S 7 . 4 ,$ this completes the proof.

In particular, if $X$ is indefinite, it follows that there exists a non-zero vector $y$ in $\mathbf { Q } \otimes X$ with $y \cdot y = 0$ 、Multiplying by a suitable positive integer m, this yields a non-zero vector $x = m y$ in the lattice $X$ with $x \cdot x { = } 0$ Thus we have reproved Lemma (4.1) of Chapter II.

(2.7) Corollary. The Wit ring $W ( \mathbf { Z } )$ is isomorphic to $\mathbf { Z }$

Proof. If $X$ represents an element in the kernel of the natural homomorphism $W ( { \bf Z } ) \to W ( { \bf Q } ) ;$ ，then certainly X contains a vector $x \neq 0$ with ${ \boldsymbol { x } } \cdot { \boldsymbol { x } } = 0$ Proceeding as in Chapter II, $\ S 2 . 2$ ，we can decompose $X$ as an orthogonal sum $X _ { 0 } \oplus X _ { 0 } ^ { \perp }$ where $X _ { 0 }$ has inner product matrix $\binom { 0 \quad 1 } { 1 \quad * } .$

It follows inductively that $X$ is split. (Compare $\ S 3 . 3$ below.) Hence $W ( \mathbf { Z } )$ maps isomorphically to the ring $\mathbf { Z } \subset W ( \mathbf { Q } )$ □

Combining (2.1) and (2.7), we see that the sequence

$$
0 \to W ( \mathbf { Z } ) \to W ( \mathbf { Q } ) \to \oplus W ( \mathbf { Z } / p \mathbf { Z } ) \to 0
$$

is exact. In this form, the sequence admits a significant generalization, which is discussed in the next section.

# \$ 3.Dedekind Domains

Let $D$ be a Dedekind domain: that is a commutative ring without zero divisors in which any non-zero ideal can be expressed uniquely as a product of maximal ideals. The quotient field of $\overline { { D } }$ will be denoted by $F \supset D$ Every maximal ideal ${ \mathfrak { p } } \subset D$ gives rise to a p-adic valuation on $F$ with residue class field ${ \underline { { D / { \mathfrak { p } } } } }$ , and hence to an associated homomorphism

$$
\partial _ { \mathfrak { p } } \colon W ( F ) \to W ( D / { \mathfrak { p } } ) .
$$

We will refer to such maximal ideals briefly as primes.Let $X$ be an inner product space over $F$ . Given finitely many elements $x _ { 1 } , \ldots , x _ { k }$ , including a basis for $X$ over $F$ ,we can form the $D$ -submodule

$$
k = { \cal { D } } x _ { 1 } + \cdots + { \cal { D } } x _ { k } \in X
$$

Definition. Any such finitely generated $\mathbfcal { D }$ -submodule, containing a basis for $X$ over $F$ ,is called a lattice (or a $D /$ -lattice) in $X$

Given a lattice $L \subset X$ , the dual lattice $L ^ { \# } \subset X$ is defined to be the set of all $x \in X$ such that $x \cdot l \in D$ for all $l \in L$

Note that $L ^ { \# }$ is in fact a $D$ -module, canonically isomorphic to ${ \mathrm { H o m } } _ { D } ( L , D )$ Forevery $D$ -linearmap $L {  } D$ extends uniquely to an $\boldsymbol { F }$ -linear map $X \to F$ which must have the form $x \mapsto x \cdot x _ { 0 }$ for some unique $x _ { 0 } \in L ^ { \# }$ . Using the theorem that every finitely generated torsion free module over $D$ is projective4, we see that $L$ and thus also $L ^ { \# }$ are finitely generated and projective. Clearly $L ^ { \# }$ contains a basis for $X$ over $F$

(3.1) Theorem. An inner product space $X$ over $F$ contains a lattice $L$ which is self-dual, $L = L ^ { \# }$ ,if and only if the Witt class of $X$ belongs to the kernel of the homomorphism

for every maximal ideal p of D.

Evidently $L$ is self-dual if and only if the given inner product on $X$ when restricted to $L$ makes $L$ into an inner product space over $D$

Proof of (3.1). First suppose that there is only one maximal ideal $\mathfrak { p }$ in $D$ ,so that $D$ is the valuation ring associated with the $\mathfrak { p }$ -adic valuation of $F$ Let $X$ be an inner product space over $F _ { \ast }$ , and suppose that

$$
X \cong \left. \pi u _ { 1 } \right. \oplus \cdots \oplus \left. \pi u _ { m } \right. \oplus \left. u _ { m + 1 } \right. \oplus \cdots \oplus \left. u _ { n } \right. .
$$

4 Seeforexample[Cartan-Eilenberg]or[Milnor,ItroductiontoAlgebraicK-Theory]

class group of the Dedekind domain $D \subset F$ .Then there is a unique homomorphism

$$
W ( D / { \mathfrak { p } } ) { \to } \mathscr { C } / \mathscr { C } ^ { 2 }
$$

which carries each generator $\langle \overline { { u } } \rangle$ f $W ( D / { \mathfrak { p } } )$ to the ideal class of $\mathfrak { p }$ modulo $\mathcal { C } ^ { 2 }$ . It is now not difficult to verify that the sequence

$$
W ( F ) \xrightarrow { \circ } \mathbb { O } W ( D / { \mathfrak { p } } ) {  } \mathcal { C } / \mathcal { C } ^ { 2 } {  } 0
$$

is exact. (One uses Lemma (4.4) below, together with the discussion preceding (4.4), to show that every element of $\bigoplus I ( D / { \mathfrak { p } } )$ lifts back to $I ^ { 2 } ( F )$ . It is then only necessary to verify that the cokernel of the homomorphism from $I \left( F \right) / I ^ { 2 } \left( F \right) { \cong } F ^ { \bullet } / F ^ { \bullet 2 }$ to $\oplus W ( D / { \mathfrak { p } } ) / I ( D / { \mathfrak { p } } ) { \cong } \oplus { \bf Z } / 2$ induced by $\partial$ is isomorphic to ${ \mathcal { C } } / { \mathcal { C } } ^ { 2 }$ ）

(3.5) Example. Let $D$ be the ring $\mathbb { R } [ x , y ] / ( x ^ { 2 } + y ^ { 2 } - 1 )$ consisting of all polynomial functions on the circle. Then each point (cos $\theta _ { \pm }$ sin $\theta$ on the unit circle gives rise to an ideal ${ \mathfrak { p } } _ { \theta }$ consisting of polynomials $f ( x , y )$ which vanish at $( \cos \theta , \sin \theta )$ . Clearly the quotient ${ \cal D } / { \mathfrak { p } } _ { \theta }$ is the field of real numbers, hence $W ( D / { \mathfrak { p } } _ { \theta } ) { \cong } { \mathbf Z }$ . The associated homomorphism

$$
{ \hat { \partial } } _ { \theta } \colon W ( F ) \to W ( D / { \mathfrak { p } } _ { \theta } ) { \cong } \mathbf { Z }
$$

is well defined up to sign. Clearly $\hat { \partial } _ { \theta _ { 9 } }$ carries each generator $\langle f \rangle$ of $W ( { \boldsymbol { F } } )$ to either ±1 or O according as the function $f ( \cos \theta , \sin \theta )$ changes sign or not as the variable $\theta$ passes through $\theta _ { 0 }$ A choice of sign for $\partial _ { \pmb { \theta } }$ is equivalent to a choice of local orientation for the circle. Choosing orientations coherently, we obtain the relation

$$
\sum _ { \theta } \partial _ { \theta } \langle f \rangle = 0
$$

for every $f { \in } F ^ { \bullet }$ . It is now not difficult to verify that the cokernel of

$$
\partial \colon { \cal W } ( { \cal F } ) \to \oplus { \cal W } ( D / \mathfrak { p } )
$$

is infinite cyclic.

# S.4.Number Fields

Let $F$ be a finite extension of the rational numbers,and let $D$ be the ring of all algebraic integers in $F$ .(See for example [Lang,p.20].) Since the structure of $W ( { \boldsymbol { F } } )$ is well understood (compare Chapter III, $\ S 5 . 9 )$ ，we can use the exact sequence (3.3) to describe the ring $W ( D )$

First some notation. Let $d$ be the number of dyadic primes in $D$ (that is the number of prime ideals p such that $\underline { { \boldsymbol { D } / \mathfrak { p } } }$ has characteristic 2). Let r be the number of embeddings of $\cal { F }$ in the real numbers and'c the number of pairs of conjugate embeddings of $\boldsymbol { \mathsf { \Pi } }$ as a dense subset of the complex numbers. Thus $r + 2 c$ is the degree of $F$ over $\mathbf { Q }$

Two non-zero ideals $\mathfrak { a }$ and $\mathfrak { b }$ in $D$ are called strictly equivalent if ${ \mathfrak { a } } = \tau { \mathfrak { b } }$ for some field element $\tau$ which is totally positive (i.e., positive with respect to every embedding of $F$ in $\mathbf { R }$ .Let $\boldsymbol { \hat { \mathcal { C } } }$ be the group of all strict equivalence classes of non-zero ideals.This is a finite extension of the usual ideal class group, which we denote by $\mathscr { C }$ ，

(4.1) Theorem’. The radical $\Re _ { D }$ , consisting of all nilpotent elements in the Witt ring $W ( D )$ is a finite group with order equal to $2 ^ { c + d - 1 }$ multiplied by the number of elements of order $\leq 2 \mathrm { ~ } i n \mathcal { \hat { C } }$

Clearly an element of $W ( D )$ is nilpotent if and only if its image in $W ( { \boldsymbol { F } } )$ is nilpotent. Comparing Chapter III, $\ S 3 . 6$ and $\ S 3 . 8$ , it follows that there is an exact sequence which takes the form

$$
0 \to \mathfrak { N } _ { D } \to W ( D ) \to \mathbf { F } _ { 2 } \to 0
$$

if $F$ is totally imaginary $( r = 0 )$ ; and an exact sequence

$$
\overline { { 0 \to \mathfrak { N } _ { D } \to W ( D ) } } \overset { \sigma } { \to } { \mathbf Z } ^ { \Omega }
$$

otherwise.We will see in (4.5) that the image $\sigma \big ( W ( D ) \big )$ is always a subgroup of finite index in Z².

(4.2) Corollary. If F is totally imaginary, then $W ( D )$ is a finite ring with order equal to $2 ^ { c + d }$ multiplied by the number of elements of order 2 in the ideal class group.

Here are some examples.For the imaginary quadratic field $\mathbf { Q } ( { \sqrt { - 2 } } )$ or $\mathbf { Q } ( { \sqrt { - 3 } } ) ;$ we have $W ( D ) \cong \mathbf { Z } / 4 \mathbf { Z }$ ；while for $\overset { \scriptscriptstyle - } { \mathbf { Q } } ( \sqrt { \mathbf { - } 7 } ) .$ the ring $W ( D )$ is isomorphic to $\mathbf { Z } / 8 \mathbf { Z }$ .For $\mathbf { Q } ( { \sqrt { - 1 } } )$ it is non-cyclic of order 4 with basis $\langle 1 \rangle$ and $\langle i \rangle$ .Finally, for $\dot { \bf Q } ( \sqrt { - 5 } )$ ， $W ( D )$ is the sum of the ring $\mathbf { Z } / 4 \mathbf { Z }$ and an element of order 2 corresponding to an inner product space which is not free over $\mathcal { D }$ (Compare the table below.)

(4.3) Corollary. The radical $\mathfrak { N } _ { D }$ is zero if and only ifDis totally real, has only one dyadic prime, has odd class number, and contains units with arbitrarily prescribed sign. If these conditions are satisfied, then $W ( D )$ is $a$ free additive group with basis $\langle 1 \rangle$ ， $\langle u _ { 1 } \rangle , \ldots , \langle u _ { r - 1 } \rangle$ ,where $u _ { j }$ is negative at the $j .$ -th ordering of $F$ and positive at the remaining $r - 1$ orderings.

For example these conditions are satisfied for the fields Q, $\mathbf { Q } ( { \sqrt { 2 } } ) .$ $\mathbb { Q } ( \sqrt { 5 } )$ and $\hat { \mathbf { Q } } ( \sqrt { 1 3 } )$ .Compare the table below,as well as the tables in [Borevich-Shafarevich].

The proofs of (4.2) and (4.3) are easily supplied.

5 Wearegrateful toKnebusch forpointing out anerrorinanarlierforulationofthis result.

If the Witt class of $X$ belongs to the kernel of $\partial _ { \mathfrak { p } }$ ,then the inner product space

$$
\langle \bar { u } _ { 1 } \rangle \oplus \cdots \oplus \langle \bar { u } _ { m } \rangle
$$

over ${ \cal D } / { \mathfrak { p } }$ is split. Hence this inner product space has inner produet matrix of the form $\binom { 0 \quad I } { I \quad * } ,$ with respect to a suitable basis.Lifting to the local ring $D$ , it follows easily that the inner product space $\langle u _ { 1 } \rangle \oplus \cdots \oplus \langle u _ { m } \rangle$ over $D$ has inner product matrix of the form $\binom { A \quad I } { I \quad B }$ with respect to a suitable basis,where each entry of $A$ belongs to the ideal $\mathfrak { p }$ .Hence the same statement applies to the inner product space $\langle u _ { 1 } \rangle \oplus \cdots \oplus \langle u _ { m } \rangle$ over $F$ .Tensoring with $\langle \pi \rangle$ ，it follows that the inner product space $\left. \pi u _ { 1 } \right. \oplus \cdots \oplus \left. \pi u _ { m } \right.$ has inner product matrix

Dividing each of the first $m / 2$ basis vectors by $\pi$ ，this inner product matrix is replaced by

Evidently this is a matrix with entries in $\overline { { D } }$ whose determinant is a unit of $D$ . Hence this modified basis spans the required self-dual lattice in $\left. \pi u _ { 1 } \right. \oplus \cdots \oplus \left. \pi u _ { m } \right.$ .Forming the direct sum with the obvious self-dual lattice in $\langle u _ { m + 1 } \rangle \oplus \cdots \oplus \langle u _ { n } \rangle$ ,we have the required self-dual lattice in $X$

There is one special case not covered by this argument. If $F$ has characteristic 2 and $X$ is symplectic, then we cannot find an orthogonal basis for $X$ . But in that case $X$ is an orthogonal sum of hyperbolic planes,and clearly possesses a self-dual lattice.

Now suppose that the Dedekind domain $\overline { { D } }$ possesses more than one maximal ideal p. For each p, let $\smash { \frac { D _ { p } \subset F } { p } }$ be the associated valuation ring. Choosing a basis $e _ { 1 } , \ldots , e _ { n }$ for $X$ ，note that each inner product $e _ { i } \cdot e _ { j }$ belongs to $D _ { \mathfrak { p } }$ for all but a finite number of primes $\mathfrak { p }$ .Similarly the determinant det $( e _ { i } \cdot e _ { j } )$ is a unit of $D _ { \mathfrak { p } }$ for all but a finite number of primes. Thus there exists a finite set $s$ of primes so that the $D _ { \mathfrak { p } }$ -lattice

$$
D _ { \mathfrak { p } } e _ { 1 } + \cdots + D _ { \mathfrak { p } } e _ { n }
$$

is self-dual for all ${ \mathfrak { p } } \notin S .$

Now suppose that $\partial _ { \mathfrak { p } } ( X ) { \sim } 0$ for all p.Then for each p∈ S we can choose a $\boldsymbol { D _ { \mathfrak { p } } }$ -lattice which is self-dual by the argument above. We will need the following.

(3.2) Lemma. Let $X$ be a vector space over $F$ with basis $e _ { 1 } , \ldots , e _ { n }$ Given a $D _ { \mathfrak { p } }$ -lattice $L _ { \mathfrak { p } }$ in $X$ for each prime $\mathfrak { p }$ ,subject to the restriction that

$$
L _ { \mathfrak { p } } = D _ { \mathfrak { p } } e _ { 1 } + \cdots + D _ { \mathfrak { p } } e _ { n }
$$

for all but a finite number of p, there exists one and only one D-lattice

$$
L { = } \bigcap E _ { \mathfrak { p } }
$$

such that the $D _ { \mathfrak { p } }$ -lattice spanned $b y L$ is equal to $L _ { \mathfrak { p } }$ for every p.

This is proved,for example, in [O'Meara, $\ S 8 1 { : } 1 4 ]$

Combining (3.2) with the discussion above, we construct a $D$ -lattice $L$ with the property that the induced $D _ { \mathfrak { p } }$ -lattice $D _ { \mathfrak { p } } L$ is self-dual for every maximal ideal $\mathfrak { p }$ .Thus if $x$ $y \in L$ then $\boldsymbol { x } \cdot \boldsymbol { y } \in D _ { \mathfrak { p } }$ for every $\mathfrak { p }$ ,hence $x \cdot y \in D$ This proves that $L { \subset } L ^ { \# }$ .Conversely, if $x \in L ^ { \# }$ ,then $x \cdot D _ { \mathfrak { p } } L \subset D _ { \mathfrak { p } }$ for every prime $\mathfrak { p }$ .hence

$$
\begin{array} { r } { \overline { { x \in \bigcap ( D _ { \mathfrak { p } } L ) ^ { \# } } } = \bigcap D _ { \mathfrak { p } } L { = } L . } \end{array}
$$

Therefore the lattice $_ { L }$ is self-dual.

Conversely, if $X$ contains a self-dual lattice, then it follows easily from (1.3) that the image of $X$ in $W ( D / { \mathfrak { p } } )$ is zero for every p.This completes the proof of (3.1).□

(3.3) Corollary.For any Dedekind domain $D$ ,the sequence

$$
0 \to W ( D ) \to W ( F ) \to \oplus W ( D / { \mathfrak { p } } )
$$

is exact, where the direct sum extends over all non-zero prime ideals.

Proof. If an inner product space $L$ over $D$ corresponds to a split inner product space over $F$ ,we must prove that $L$ itself is split.We will think of $L$ as a self-dual lattice in the inner product space $X { = } F \otimes L$ .Let $N \subset X$ $\pmb { D }$ be a subspace of half the dimension with $N \cdot N { = } 0$ so that $N = N ^ { \perp }$ . Then the intersection $N \cap L$ is clearly a self-orthogonal subspace of $L$ This intersection is a direct summand of $L$ since the quotient

$$
L / ( N \cap L ) \subset X / N
$$

is finitely generated and torsion-free, hence projective. It is equal to $( N \cap L ) ^ { \perp }$ ，since ifan element $x \in L$ is orthogonal to $\mathbf N \cap L$ then it is orthogonal to all of $N$ ,and hence belongs to $N ^ { \bot } \cap L = N \cap L$

Thus $L$ is split, and the sequence $0 \to W ( D ) \to W ( F )$ is exact. The rest of the proof is straightforward, using (3.1).

Remark.In contrast to the situation in $\ S 2 ,$ ,we do not assert that the homomorphism $\hat { \boldsymbol { o } }$ $W ( { \boldsymbol { F } } ) \to \oplus W ( { \boldsymbol { D } } / { \mathfrak { p } } )$ is necessarily surjective.

(3.4) Example. If F is a finite extension of the rational numbers, then the cokernel of $\hat { \boldsymbol { \sigma } }$ can be computed as follows. Let $\mathcal { C }$ denote the ideal

Table describing the additive structure of $W ( D )$ for the quadratic field $\mathbf { Q } ( { \sqrt { n } } )$ .The cyclic group of order $m$ is denoted briefly by m.

![](images/ff1e01b28dcec853aa279581e0eb8abeaee3a3a4879a5b8a527d24f503516e5c.jpg)

Proof of (4.1). We will think of $W ( D )$ as a subring of $W ( { \boldsymbol { F } } )$ Hence we can intersect the radical $\mathfrak { N } _ { D }$ with the ideal $I ^ { 2 } ( F ) .$ 、As a first step in the proof, we will show that this intersection $\mathfrak { N } _ { D } \cap I ^ { 2 } ( F )$ is an elementary 2-group of order $2 ^ { d - 1 }$

Let $F _ { \mathfrak { p } }$ denote the p-adic completion of F. The classical theory,as described for example in [O'Meara], shows that an inner product space over $F _ { \mathfrak { p } }$ isuniquely determined by its rank,determinant, and Hasse invariant.If the rank is $\geq 3$ ，then the determinant in $F _ { \mathfrak { p } } ^ { \bullet } / F _ { \mathfrak { p } } ^ { \bullet 2 }$ and the Hasse invariant in $\mathbf { Z ^ { \bullet } }$ can be prescribed arbitrarily. It follows easily that the ideal $I ^ { 2 } ( F _ { \mathfrak { p } } )$ is cyclic of order 2,and that the Hasse-Witt homomorphism

$$
h _ { \mathfrak { p } } \colon I ^ { 2 } ( F _ { \mathfrak { p } } ) \to \mathbf { Z } ^ { \bullet }
$$

is bijective. (Compare Chapter II, \$\$ 5.4-5.9.)

Now recall that the homomorphism $\partial _ { \mathfrak { p } } \colon I ^ { 2 } ( F _ { \mathfrak { p } } ) {  } I ( D / \mathfrak { p } ) \circ \mathfrak { f } \ \ S 1$ is surjective. If the prime p is not dyadic then the target group $I ( D / { \mathfrak { p } } )$ has two elements by (1.5), so it follows that the homomorphism

$$
\partial _ { \mathfrak { p } } \colon I ^ { 2 } ( F _ { \mathfrak { p } } ) \to I ( D / \mathfrak { p } )
$$

is also bijective. Identifying $I ( D / { \mathfrak { p } } )$ with $\mathbf { Z } ^ { \bullet }$ ,this proves that the homomorphism

$$
\partial _ { \mathfrak { p } } \colon I ^ { 2 } ( F ) \to I ( D / \mathfrak { p } ) \cong \mathbf { Z ^ { \bullet } }
$$

can be identified with the p-th Hasse-Witt invariant, for every prime p whichis not dyadic.

The classical theory yields the following deseription of $I ^ { 2 } ( F )$

(4.4) Lemma. An element w in $I ^ { 2 } ( F )$ is uniquely determined by its   
Hasse-Witt invariants $h _ { \mathfrak { p } } ( w ) \in \mathbf { Z ^ { \bullet } }$ for the various primes $\mathfrak { p }$ ，and by its   
signature $\sigma _ { P } ( w ) { \in } 4 \mathbf { Z }$ for the various orderings of $F .$ These are subject only   
to the restriction that $h _ { \mathfrak { p } } ( w ) = 1$ for almost all $\mathfrak { p }$ ,and that $\prod _ { \mathfrak { p } } h _ { \mathfrak { p } } ( w )$ must be   
equal to [1(-1)op(w)/4. P

Proof.This follows easily from the classical description of inner product spaces over $F$ (compare [O'Meara, $\ S 7 2 ]$ )，together with the discussion in Chapter III, $\ S 5$ □

Now let us ask which elements w of $I ^ { 2 } ( F )$ belong to the subring $W ( D )$ .A necessary and sufficient condition is that $\partial _ { \mathfrak { p } } ( \boldsymbol { w } )$ must be zero for all p. We have seen that $\partial _ { \mathfrak { p } } ( \boldsymbol { w } )$ can be identified with the $\mathfrak { p }$ -th Hasse-Witt invariant whenever $\mathfrak { p }$ is non-dyadic；but that $\partial _ { \mathfrak { p } } I ^ { 2 } ( F ) = 0$ when $\mathfrak { p }$ is dyadic. Evidently this proves the following.

(4.5) Corollary. An element w in the intersection $W ( D ) \cap I ^ { 2 } ( F )$ is uniquely specified by its Hasse-Witt invariants at the d dyadic primes, together with its signatures $\sigma _ { P } ( w ) { \in } 4 \mathbf { Z }$ at the $r$ orderings of $F .$ These are subject only to the relation $\prod _ { p } \dot { h } _ {  p } ( w ) = \prod _ { P } ( - 1 ) ^ { \sigma _ { P } ( w ) / 4 }$

In particular the image $\sigma ( W ( D ) \cap I ^ { 2 } ( F ) )$ is precisely equal to $\mathbf { \vec { 4 } } \mathbf { Z } ^ { \Omega }$ 」， since there always exists at least one dyadic prime. Therefore ${ \underline { { \sigma } } } \left( W ( D ) \right) i s$ a subring of finite index in $\mathbf { Z } ^ { \Omega }$

It follows that $W ( D ) \cap I ^ { 2 } ( F )$ is the direct sum of a free abelian group of rank $r _ { \ast }$ ,and an elementary 2-group of order $2 ^ { d - 1 }$ . Restricting to the kernel of $\sigma _ { \mathrm { { : } } }$ ,it follows that $\Re _ { D } \cap I ^ { 2 } ( F )$ is an elementary 2-group of order $2 ^ { d - 1 }$ ：

Next we must study the quotient $\Re _ { D } / \Re _ { D } \cap I ^ { 2 } ( F )$ Clearly this embeds in the quotient

$$
I ( F ) / I ^ { 2 } ( F ) { \cong } F ^ { \bullet } / F ^ { \bullet 2 } ,
$$

and hence is an elementary 2-group. The precise image in ${ F ^ { \bullet } } / { F ^ { \bullet } } ^ { 2 }$ can be identified as follows. Let $F _ { + } ^ { \bullet } \subset F ^ { \bullet }$ denote the subgroup of index $2 ^ { r }$ consisting of totally positive elements;and let $F _ { \mathbf { e v } } ^ { \bullet }$ denote the subgroup consisting of elements $\pmb { \alpha }$ such that the $\mathfrak { p }$ -adic value of $\pmb { \alpha }$ is even for all $\mathfrak { p }$ In other words $F _ { \mathrm { e v } } ^ { \bullet }$ consists of all $\pmb { \alpha }$ such that the fractional ideal $D \alpha$ is equal to ${ \mathfrak { a } } ^ { 2 }$ for some fractional ideal $\mathfrak { a }$

(4.6) Lemma. The quotient $\mathfrak { N } _ { D } / \mathfrak { N } _ { D } \cap I ^ { 2 } ( F )$ is canonically isomorphic to the quotient $( F _ { + } ^ { \bullet } \cap F _ { \mathrm { e v } } ^ { \bullet } ) / F ^ { \bullet 2 }$ ：

Proof. We must decide which elements $\pmb { \alpha }$ of $F ^ { \bullet }$ modulo $F ^ { \bullet 2 }$ can appear as the discriminants of inner product spaces over $D$ with signature zero.If $\pmb { \alpha }$ is totally positive, and

$$
\mathbf { \nabla } D \mathfrak { x } = \mathfrak { a } ^ { 2 }
$$

for some fractional ideal $\mathfrak { a }$ ，then we can make $\mathfrak { a }$ into an inner product space over $D$ by introducing the inner product

$$
x \cdot y { } = x y / \alpha
$$

for $x , y \in \mathfrak { a }$ .Evidently a is positive definite at $\mathcal { \textbf { P } }$ for every ordering $\overline { { P } }$ of F. Hence the inner product space

over $D$ represents an element of $W ( D ) \subset W ( F )$ with signature zero and discriminant $\alpha F ^ { \bullet 2 }$

Conversely, given an inner product space $X$ of even rank and zero signature over $D$ ,we may assume (adding a hyperbolic plane if necessary) that the rank n is divisible by 4.The exterior power $\wedge ^ { n } X$ has rank 1 and is positive definite at every ordering. It is then easy to verify that $\wedge ^ { n } X$ is isomorphic to an ideal $\mathfrak { a }$ with inner product

$$
x \cdot y { } = x y / \alpha
$$

where $\pmb { \alpha }$ is totally positive, spans ${ \mathfrak { a } } ^ { 2 }$ ,and where $d ( X ) { = } \alpha F ^ { \bullet 2 }$

Now consider the inclusions

![](images/8a0320e8a9a8a9fed39511f97361779313321a1cfb5b63d69993e195a82ade1f.jpg)

Let us assume first, to fix our ideas, that $r \geq 1$ .Going around the top of this diagram, since $F _ { + } ^ { \bullet }$ has index $2 ^ { r }$ in $F ^ { \bullet } ,$ it follows easily that $F _ { + } ^ { \bullet 2 }$ has index $2 ^ { r - 1 } \mathrm { i n } F ^ { \bullet 2 } .$ .We have seen that the index of $F ^ { \bullet 2 }$ in $F _ { + } ^ { \bullet } \cap F _ { \mathrm { e v } } ^ { \bullet }$ is equal to the order of $\Re _ { D } / \Re _ { D } \cap I ^ { 2 } ( F )$

Going around the bottom of the diagram, the Dirichlet unit theorem implies that the quotient

$$
D _ { + } ^ { \bullet } F _ { + } ^ { \bullet 2 } / F _ { + } ^ { \bullet 2 } { \cong } D _ { + } ^ { \bullet } / D _ { + } ^ { \bullet 2 }
$$

has order $2 ^ { r + c - 1 }$ (still assuming that $r \geq 1 { \underline { { \underline { { \mathbf { \Pi } } } } } }$ 0. We claim that the quotient

$$
( F _ { + } ^ { \bullet } \cap F _ { \mathrm { e v } } ^ { \bullet } ) / D _ { + } ^ { \bullet } F _ { + } ^ { \bullet 2 }
$$

is canonically isomorphic to the group of elements of order 2 in $\hat { \mathcal { C } }$ .For each $\pmb { \alpha }$ in $F _ { + } ^ { \bullet } \cap F _ { \mathrm { e v } } ^ { \bullet }$ determines a unique fractional ideal $\mathfrak { a }$ ，

$$
a ^ { 2 } = D \alpha
$$

representing an element of order 2 in $\boldsymbol { \hat { \mathcal { C } } }$ ; and this ideal $\mathfrak { a }$ represents the identity element of $\boldsymbol { \hat { \mathcal { C } } }$ if and only if $\alpha$ is the product of a unit and the square of a totally positive field element.

![](images/47128db9c78451b3f0cfcb27a5b16c30041e09a058a1f4b370f43b62f8858ea0.jpg)

class number of an imaginary quadratic field $\mathbf { Q } ( { \sqrt { - n } } )$ is given for example in [Borevich-Shafarevich, Ch.V, $\ S 4 . 1 ]$ . Inspecting this formula, we see that the class number is odd if and only if the square-free integer n is equal to $1 , 2 ,$ or a prime of the form $4 k + 3 .$ The cases $n { = } 1 , 2 ,$ are easily handled, so we may assume that $n { \geq } 3$

If n is a prime of the form $8 k + 3$ ,there is only one dyadic prime in $\pmb { D }$ (namely ${ \mathfrak { p } } = 2 D _ { \circ }$ , so it follows from (4.2) that $W ( D )$ has order 4.But -1 is not a square in $F _ { \mathrm { { ; } } }$ ，so the element $\langle 1 \rangle \in W ( D )$ has order at least 4.This proves that $W ( D )$ is cyclic of order 4.

On the other hand if $n$ is a prime of the form $8 k + 7$ ,then the prime 2 splits in $D _ { i }$ ，hence $W ( D )$ has order 8.Using the Hasse-Witt invariant associated with one of the two dyadic primes,we see that

$$
\langle 1 \rangle \oplus \langle 1 \rangle \oplus \langle 1 \rangle \oplus \langle 1 \rangle \nsim 0 ,
$$

so that $\left. 1 \right.$ has order at least 8. This shows that $W ( D )$ is cyclic of order 8; and completes the proof.0

![](images/2089f9ecb951db8b5634eff9bec6acaa17a5d678fb6965fbf84cd2cf393b4c60.jpg)

In this concluding chapter we briefly describe some examples of bilinear forms which arise naturally in topology, in differential geometry,and in number theory. The three sections of this chapter are completely independent.

# S1.Homology Theory of Manifolds

It will be convenient to use the old fashioned terminology, and say that a manifold is closed if it is compact without boundary.

Let $M = M ^ { 2 n }$ be a closed manifold of dimension $2 n ,$ and let $\mathbf { F } _ { 2 }$ be   
the field with two elements. If $_ x$ and $y$ are homology classes in $H _ { n } ( M ; \mathbb { F } _ { 2 } ) ;$   
the intersection number $x \cdot y { = } y \cdot x \in \mathbf { F } _ { 2 }$

is defined. The Poincaré duality theorem, see for example [Spanier], implies that $H _ { n } ( M ; \mathbf { F } _ { 2 } )$ is an inner product space over ${ \bf E } _ { 2 }$ ，using the intersection number as inner product.

Let us look at the special case of a surface; that is let $n = 1$ If $M$ is connected then every homology class $x \in H _ { 1 } ( M ; \mathbf { F } _ { 2 } )$ can be represented by a simple closed curve $\gamma \subset M$ Note that the self intersection number $x \cdot x$ is zero if and only if $^ { a }$ small neighborhood $N$ of $\gamma$ is orientable. For if $N$ is orientable, then a small homotopy will deform $\gamma$ to a curve $\gamma ^ { \prime } { \subset } N$ which is disjoint from y. (Compare Fig. 5.) But if γ does not possess an orientable neighborhood, then it must possess a neighborhood $N$ which is a Moebius band. In this case, deforming γ to a curve $\gamma ^ { \prime }$ which cuts $\gamma$ transversally, the number of intersection points will be odd. This proves the following.

![](images/028068a08f914c41bae4202c545e1f104c0c0543590fc02b61b0c1835818c136.jpg)  
Fig.5

(1.1) Lemma. The surface M is orientable if and only if $x \cdot x { = } 0$ for every $x \in H _ { 1 } ( M ; \mathbf { F } _ { 2 } )$

Since a closed connected surface is completely determined by its orientability or non-orientability, together with its middle Betti number, see for example [Massey], this implies:

(1.2) Corollary. Two closed connected surfaces $M$ and $M ^ { \prime }$ are homeomorphic if and only if the inner product spaces $H _ { 1 } ( M ; \mathbf { F } _ { 2 } )$ and $H _ { 1 } ( M ^ { \prime } , \mathbf { F } _ { 2 } )$ are isomorphic.

Here are some examples. For the torus T, the space $H _ { 1 } ( T ; \mathbf { F } _ { 2 } )$ isa 01 hyperbolic plane, with basis $\boldsymbol { e } _ { 1 } , \boldsymbol { e } _ { 2 }$ and inner product matrix 1 A (Compare Fig.6.） For the projective plane $P ,$ there is just one basis vector $e .$ with $e \cdot e = 1$ ,so that

$$
H _ { 1 } ( P ; \mathbf { F } _ { 2 } ) \cong \langle 1 \rangle .
$$

![](images/9b62c2e5851d0e6b5b1f4f05d2e65e0a90331bf9b72be1e6cf0f93c28fce94bf.jpg)  
Fig. 6.The torus and Klein bottle

As a final example, for the Klein bottle K there is a basis e,e2 with inner product matrix $\binom { 0 } { 1 }$ Or alternatively， using the orthogonal basis $e _ { 1 } + e _ { 2 } , e _ { 2 }$ , we see that

$$
\begin{array} { r } { H _ { 1 } ( K ; { \bf F } _ { 2 } ) \cong \langle 1 \rangle \oplus \langle 1 \rangle . } \end{array}
$$

This decomposition corresponds of course to the geometric relation

$$
K \cong P \# P ,
$$

where # denotes the “connected sum”operation:removing a small hole from each summand and then gluing boundaries together. Similarly the relation $\langle 1 \rangle \oplus \langle 1 \rangle \oplus \langle 1 \rangle \cong \langle 1 \rangle \oplus$ (hyperbolic plane) of Chapter I, $\ S 4 ,$

corresponds to the geometric relation.

$$
P \# K \cong P \# T .
$$

(1.3) Lemma. Every inner product space over $\mathbf { F } _ { 2 }$ is isomorphic to $H _ { 1 } ( M ; \mathbf { F } _ { 2 } )$ for some closed connected surface $\pmb { M }$

For by Chapter I,S 3.3 the given inner product space is isomorphic to

![](images/cabe4f597f08bfe2beaa7146cdb298b34c279ac56bf4ee9b499179bcd577903c.jpg)

Now let $M ^ { 2 n }$ be a closed oriented manifold,and let $F$ be an arbitrary coefficient field. Then $H _ { n } ( M ^ { 2 n } ; F )$ is an inner product space over $F _ { \ast }$ using the intersection number as inner product. This inner product space is either symmetric or skew-symmetric according as $n$ is even or odd. If $M ^ { 2 n }$ bounds an oriented $( 2 n + 1 )$ -manifold, then $H _ { n } ( M ^ { 2 n } ; F )$ is a split inner product space.

Similarly one can work with integer coefficients. The Z-module $H _ { n } ( M ^ { 2 n } ; \mathbf { Z } ) /$ (torsion subgroup) is an inner product space over $\mathbf { Z }$ The case of a simply-connected 4-manifold is particularly interesting.

(1.5) Theorem. Let $M$ and $M ^ { \prime }$ be closed oriented simply-connected 4-dimensional manifolds. There exists an orientation preserving homotopy equivalence $M \to M ^ { \prime }$ if and only if the symmetric inner product space $H _ { 2 } ( M ; \mathbf { Z } )$ is isomorphic to $H _ { 2 } ( M ^ { \prime } ; \mathbf { Z } )$

Remark. It is not known whether every inner product space over Z can be realized as $H _ { 2 } ( M ; \mathbf { Z } )$ for a suitable closed simply-connected 4-manifold $M .$ In Chapter I we described a positive definite inner product space $I _ { 8 }$ of rank 8 over $\mathbf { Z }$ satisfying

$$
x \cdot x { \equiv } 0 \mod 2
$$

for every $x \in \Gamma _ { 8 }$ . It would be extremely interesting to know whether $\Gamma _ { 8 } \cong H _ { 2 } ( M ; \mathbf { Z } )$ for some $\overline { { M } }$ .If such a manifold M exists, then by a theorem of Rohlin it cannot be given any piecewise-linear structure. (Compare [Milnor,1958].)

Our special examples of surfaces have rather precise analogues   
among 4-manifolds. For example if $P$ denotes the complex projective   
plane, then $H _ { 2 } ( P ; { \bf Z } ) \cong \langle 1 \rangle .$

If $\bar { P }$ denotes the same manifold with reversed orientation, then

$$
H _ { 2 } ( \stackrel {  } { P } ; \mathbf { Z } ) \cong \langle - 1 \rangle .
$$

The analogue of the torus is the product $T { = } S ^ { 2 } \times S ^ { 2 } ,$ having inner (01) product matrix (10 with respect to a suitable basis $\boldsymbol { e } _ { 1 } , \boldsymbol { e } _ { 2 }$ . Note that the diagonal homology class $e _ { 1 } { + } e _ { 2 }$ has self intersection number $( e _ { 1 } + e _ { 2 } )$ (e1+e2) equal to 2. The analogue of a Klein bottle is the twisted S²- bundle $K$ over $S ^ { 2 }$ . One can show by geometric arguments that

$$
K \cong P \# { \overline { { P } } } ,
$$

and that

even though the inner product space $H _ { 2 } ( K ; \mathbf { Z } )$ is clearly not isomorphic to $H _ { 2 } ( T ; \mathbf { Z } )$ (Compare Chapter I, $\ S 4 . )$ （4号

Proof of Theorem (1.5). Let $E$ denote the interior of an embedded 4-disk in $M$ . Using the homology exact sequence of the pair $( M , M - E )$ with coeficients in $\mathbf { Z }$ ,together with Poincaré duality, we see easily that

$$
H _ { i } ( M - E ) { = } H _ { i } ( \mathrm { p o i n t } ) \quad \mathrm { ~ f o r ~ } i { \neq } 2 .
$$

The group

$$
H _ { 2 } ( M - E ) \cong H _ { 2 } ( M )
$$

is free abelian,say of rank $r$ ; and the Poincaré duality isomorphism

$$
H _ { 2 } ( M ) { \cong } H ^ { 2 } ( M ) { \cong } \mathrm { H o m } \ ( H _ { 2 } ( M ) , { \bf Z } )
$$

shows that the intersection number is an inner product on $H _ { 2 } ( M )$

Since $\pi _ { 1 } ( M - E ) = 0 .$ we have

$$
\pi _ { 2 } ( M - E ) \cong H _ { 2 } ( M - E ) \cong H _ { 2 } ( M )
$$

by the Hurewicz theorem. Hence there exists a map

$$
f \colon S ^ { 2 } \vee \cdots \vee S ^ { 2 }  M - E
$$

from the $r$ -fold bouquet of 2-spheres which induces a homology isomorphism

$$
H _ { * } ( S ^ { 2 } \lor \cdots \lor S ^ { 2 } )  H _ { * } ( M - E ) .
$$

Since $M - E$ is an absolute neighborhood retract, it has the homotopy type of a CW-complex.Therefore, by a theorem of J.H.C.Whitehead, f is a homotopy equivalence. (Compare [Spanier, pp. 393-405].)

But M is obtained from $M - E$ by attaching a 4-cell. ([Spanier, p.145].) Therefore $M$ has the homotopy type of a space obtained from the $r$ fold bouquet $S ^ { 2 } \vee \cdots \vee S ^ { 2 }$ by attaching a 4-cell, using some attaching map

$$
g \colon S ^ { 3 } \longrightarrow S ^ { 2 } \vee \cdots \vee S ^ { 2 } .
$$

We denote this resulting space by $\underline { { ( S ^ { 2 } \vee \cdots \vee S ^ { 2 } ) \cup E ^ { 4 } } }$ .The homotopy type of $M$ is completely determined by the homotopy class of g in $\pi _ { 3 } ( S ^ { 2 } \vee \cdots \vee S ^ { 2 } ) .$

To calculate the group $\pi _ { 3 } ( S ^ { 2 } \vee \cdots \vee S ^ { 2 } )$ we_embed $S ^ { 2 } { = } P _ { 1 } ( \mathbf { C } )$ in_the infinite complex projective space $\begin{array} { r } { P _ { \infty } ( \mathbf { C } ) , } \end{array}$ and use the inclusion

$$
S ^ { 2 } \vee \cdots \vee S ^ { 2 } = S ^ { 2 } \times \cdots \times S ^ { 2 } = P _ { \infty } ( \mathbf { C } ) \times \cdots \times P _ { \infty } ( \mathbf { C } ) .
$$

Denoting the $r .$ fold bouquet by $B .$ ,and the $r .$ -fold product of projective spaces by $K$ ,this inclusion $B \subset K$ gives rise to isomorphisms

$$
H _ { 4 } ( K ) { \cong } H _ { 4 } ( K , B ) { \cong } { \pi } _ { 4 } ( K , B ) { \cong } { \pi } _ { 3 } ( B ) .
$$

In fact the first of these isomorphisms comes from the homology exact -sequence of the pair $( K , B ) ,$ the second comes from the relative Hurewicz -theorem, and the third from the homotopy exact sequence of the pair.

Clearly $H _ { 4 } ( K )$ is a free $\mathbf { Z }$ -module.The dual module

$$
H ^ { 4 } ( K ) { \cong } \mathrm { H o m } \ ( H _ { 4 } ( K ) , { \bf Z } )
$$

has a basis consisting of products $u _ { i } u _ { j }$ with $i \leq j ,$ where $u _ { 1 } , \ldots , u _ { r }$ form a basis for the cohomology group

$$
H ^ { 2 } ( K ) { \cong } H ^ { 2 } ( B ) { \cong } H ^ { 2 } ( M - E ) { \cong } H ^ { 2 } ( M ) .
$$

([Spanier,p.264].)Now extend the inclusion $B \to K$ to a mapping

$$
B \cup E ^ { 4 }  K .
$$

Lifting the products $u _ { i } u _ { j } { \in } H ^ { 4 } ( K )$ back to $H ^ { 4 } \big ( B \cup E ^ { 4 } \big ) \cong H ^ { 4 } ( M ) .$ and then evaluating on the orientation class $[ M ] \in H _ { 4 } ( M ) { \cong } { \mathbf Z } ,$ we obtain a symmetric matrix of integers $u _ { i } u _ { j } [ M ]$ which completes describes the inner product space $H ^ { 2 } ( M ) { \cong } H _ { 2 } ( \dot { M } )$ But evidently these integers also describe the homotopy class of the attaching map in $\pi _ { 3 } ( B ) { \cong } \pi _ { 4 } ( K , B ) { \cong } H _ { 4 } ( K ) .$ This completes the proof.□

# S 2. Rings of Smooth Real Valued Functions

The word smooth will mean $\bar { k }$ times continuously differentiable where $\bar { k }$ is fixed, $0 \leq k \leq \infty$

Given a smooth paracompact manifold $M _ { ☉ }$ let $R ( M )$ be the ring of all smooth real valued functions on $M .$ Then a finitely generated projective module over $R ( M )$ can be identified with the module $\varGamma ( \xi )$ consisting of all smooth cross-sections of some real vector bundle $\xi$ over $M$ (Compare [Swan, 1962].) The projective module $\varGamma ( \xi )$ is free if and only if $\xi$ is a trivial vector bundle.

An inner product on $\varGamma ( \xi )$ (taking values in $R ( M ) )$ is just a smooth function which assigns to each point $_ x$ of $M$ a real valued inner product on the fiber of $\xi$ over $x$

First consider the symplectic case. Vector bundles with symplectic inner product occur naturally in the theory of Hamiltonian differential equations. (See for example [MacLane].) Such bundles are classified by mappings of the base space $M$ into a certain universal base space $B S p ( 2 n , \mathbf { R } )$ which has the same homotopy type as $B U ( n )$ . (Compare [Steenrod, $\ S 1 9 . 8$ ,41.15].Here $S p ( 2 n , \mathbf { R } )$ denotes the group of isometries ofa $2 n \cdot$ -dimensional real symplectic inner product space.) Thus there is $^ { a }$ one-to-one correspondence between symplectic inner product spaces of rank 2n over $R ( M )$ and complex n-dimensional vector bundles over $M$ ([Steenrod, \$41j.) A symplectic inner product space possesses a symplectic basis if and only if the corresponding complex vector bundle is trivial.

One example which is particularly easy to understand is that of an oriented 2-dimensional vector bundle.Then $\wedge ^ { 2 } \xi$ is a trivial line bundle, so the module $\varGamma ( \xi )$ possesses a more or less unique symplectic inner product. If $\xi$ is non-trivial (e.g., if $\xi$ is the tangent bundle of the 2-sphere), then $T ( \xi )$ certainly cannot possess a symplectic basis.

Now consider the symmetric case. Vector bundles with symmetric inner product occur naturally in Riemannian geometry, and in general relativity. The following statement is due to G.Lusztig. (Compare [Steenrod, $\ S 4 0 ]$ as well as [Gelfand,Mishchenko].)

Theorem. The Witt ring $W \big ( R ( M ) \big ) .$ ，consisting of Witt classes of symmetric inner product spaces over $R ( M ) $ ，is canonically isomorphic to the ring $K O ( M )$ of virtual real vector bundles over $M$

The proof can be sketched as follows. Let ζ be a real vector bundle over $\pmb { M }$ with symmetric inner product. We will show first that $\xi$ isisomorphic to an orthogonal sum ζ+④ §- where each fiber of $\xi ^ { + }$ is positive definite and each fiber of - is negative definite. For each fiber $\xi _ { x }$ of $\xi$ let $P ( \xi _ { x } )$ be the set consisting of all positive definite subspaces of maximal rank in $\xi _ { x }$ . Then $P ( \xi _ { x } )$ has a natural topology,and in fact is a topological cell. To prove this, choose a base point $\eta _ { x } ^ { 0 } \in P ( \xi _ { x } )$ It is clear that the real inner product space $\xi _ { x }$ decomposes as

$$
\overline { { \xi _ { x } = \eta _ { x } ^ { 0 } \oplus \eta _ { x } ^ { 0 \perp } } } .
$$

Now an arbitrary element $\eta _ { x } \in P ( \xi _ { x } )$ can be described as the graph of a linear mapping $f { \in } \mathrm { H o m } ( \eta _ { x } ^ { 0 } , \eta _ { x } ^ { 0 \perp } )$ belonging to the convex open set described by the inequality

$$
| f ( v ) \cdot f ( v ) | < v \cdot v
$$

for all $\pmb { v } \in \eta _ { \pmb { x } } ^ { 0 }$ $v \neq 0$

Evidently these cells $P ( \xi _ { x } )$ form the fibers of a new fiber bundle over $\mathcal { M }$ .This new bundle possesses a cross-section

$$
x \mapsto \xi _ { x } ^ { + } \in P ( \xi _ { x } )
$$

(compare [Hirzebruch,p.51]),and the resulting spaces $\xi _ { x } ^ { + }$ form the fibers of the required sub-bundle $\xi ^ { + } \subset \xi$ with $\xi = \xi ^ { + } \oplus \xi ^ { + \bot } = \xi ^ { + } \oplus \xi ^ { - }$ as required.

The two vector bundles $\xi ^ { + }$ and $\xi ^ { - }$ are uniquely determined, up to isomorphism.For if $\xi$ also decomposes as $\eta ^ { + } \oplus \eta ^ { - }$ then $\eta ^ { + } \cap \xi ^ { - } = 0 .$ hence the composition

is an isomorphism of vector bundles.

It is not difficult to show that the inner product space $\varGamma ( \xi ^ { + } \oplus \xi ^ { - } )$ splits if and only if the vector bundle $\xi ^ { + }$ is isomorphic to $\xi ^ { - }$ . Further details will be left to the reader.

# S 3. The Discriminant of a Field Extension

Let $F { \subset } F ^ { \prime }$ be finite extensions of the field of rational numbers.Then the ring $R$ consisting of all algebraic integers in $F$ is a Dedekind domain [Lang,p.20],as is the ring $R ^ { \prime }$ consisting of all algebraic integers in $F ^ { \prime }$ Forgetting its ring structure,we will think of the larger ring $R ^ { \prime }$ as a module over $R$ This $R$ -module is torsion free and finitely generated [Lang,p.6]. Therefore,by a classical theorem of Steinitz, $R ^ { \prime }$ is projective,being $R$ -linearly isomorphic to a direct sum of the form $R \oplus \cdots \oplus R \oplus \mathfrak { a }$ where α is a non-zero ideal in $R$ (See for example [Milnor, Introduction to Algebraic K-Theory, p.11].) Evidently the number n of summands (including a) is equal to the degree of $F ^ { \prime }$ over $\mathcal { F } .$

This module $R ^ { \prime }$ possesses a canonical $R$ -valued symmetric bilinear form

$$
\beta ( x , y ) { = } \mathrm { t r a c e } _ { F ^ { \prime } / F } ( x y ) .
$$

Thus the pair $( R ^ { \prime } , \beta )$ is a bilinear form space over $R$

As in Chapter I, $\ S 5 . 7 _ { : }$ ，we will consider the $\pmb { n }$ -th exterior power $\textstyle \bigwedge _ { R } ^ { n } R ^ { \prime }$ ， This exterior power is a projective module of rank 1, being $\pmb R$ -linearly isomorphic to the ideal $\mathfrak { a }$ .It is provided with a canonical symmetric bilinear form $\widehat { \beta }$ ,defined by

$$
{ \widehat { \beta } } ( x _ { 1 } \wedge \cdots \wedge x _ { n } , y _ { 1 } \wedge \cdots \wedge y _ { n } ) { \mathop { = } } \mathrm { d e t } \big ( \beta ( x _ { i } , y _ { j } ) \big ) .
$$

The“discriminant”of the extension $R ^ { \prime } { \supset } R$ is usually defined to be a certain ideal D in $R$ :([Lang, p. 65].) For example $\mathfrak { d }$ can be described as the ideal generated by the image of the function

$$
\widehat { \beta } \colon \Lambda _ { R } ^ { n } R ^ { \prime } \times \Lambda _ { R } ^ { n } R ^ { \prime } {  } R .
$$

We obtain a slightly sharper invariant by defining the discriminant of $\scriptstyle { R ^ { \prime } }$ over $R$ to be the isomorphism class of the bilinear form space $( \Lambda _ { R } ^ { n } R ^ { \prime } , \widehat { \beta } )$ over $R$ .(Compare [Frohlich,1960].)

As an example, suppose that $R ^ { \prime }$ happens to be free over $R$ with basis $e _ { 1 } , \ldots , e _ { n }$ . Then $\textstyle { \bigwedge } _ { R } ^ { n } R ^ { \prime }$ is free over $R$ with a single basis element $e =$ $e _ { 1 } \wedge \cdots \wedge e _ { n }$ . Setting

$$
{ d _ { 0 } } = \widehat { \beta } ( e , e ) = \mathrm { d e t } \big ( \mathrm { t r a c e } ( e _ { i } e _ { j } ) \big ) \in R ,
$$

it follows that $( \triangle _ { R } ^ { n } R ^ { \prime } , \widehat { \beta } )$ is isomorphic to the free bilinear form space $\langle d _ { 0 } \rangle = \langle d _ { 0 } \rangle _ { R }$ .This ring element $d _ { 0 }$ is well defined up to multiplication

by squares of units. Evidently the discriminant ideal D, generated by the image of ${ \widehat { \beta } } _ { : }$ , is equal to the principal ideal $d _ { 0 } R$

Even if $R ^ { \prime }$ is not free over $R$ ，the field $F ^ { \prime }$ is certainly free over $F .$ Working over $F ,$ the corresponding exterior power $\textstyle \bigwedge _ { F } ^ { n } F ^ { \prime }$ is provided with a corresponding symmetric bilinear form $\widehat { \beta }$ Evidently

$$
( \bigwedge _ { F } ^ { n } F ^ { \prime } , \widehat { \beta } ) \cong \langle d \rangle _ { F }
$$

for some field element $d \neq 0$ ,where $d$ is well defined up to multiplication by $F ^ { \bullet 2 }$ . The following result is due to [Artin,1950] and [Frohlich,1960].

(3.1) Lemma. With d and D as above,there is one and only one fractional ideal $\mathfrak { a }$ in $F$ satisfying the equation

$$
\mathfrak { d } = d \mathfrak { a } ^ { 2 } .
$$

The exterior power $\hat { \mathcal { A } } _ { R } ^ { n } R ^ { \prime }$ is R-linearly isomorphic to this ideal ${ \mathfrak { a } } .$ Hence the ring $\scriptstyle { R ^ { \prime } }$ is free over $R$ if and only if $\pmb { \alpha }$ is $^ { a }$ principal ideal.

In fact the proof will show that the bilinear form space $( { \textstyle \bigwedge } _ { R } ^ { n } R ^ { \prime } , { \widehat { \beta } } )$ is isomorphic to $( \mathfrak { a } , \beta _ { d } )$ where

$$
\beta _ { d } ( a _ { 1 } , a _ { 2 } ) = d a _ { 1 } a _ { 2 }
$$

for all $a _ { 1 }$ ， $\alpha _ { 2 } \in \mathfrak { a }$ We have already noted that $\scriptstyle { \mathcal { R } } ^ { \prime }$ is $R$ -linearly isomorphic to $\pmb { R } \oplus \cdots \oplus \pmb { R } \oplus \pmb { \alpha } _ { 1 }$ ,and therefore $\Lambda _ { R } ^ { n } R ^ { \prime } \cong \mathfrak { a } _ { 1 }$ ,for some ideal $\mathfrak { a } _ { 1 }$ .Evidently any $\mathbf { \vec { \nabla } } R$ -valued bilinear form on $\overline { { \pmb { \mathfrak { a } } _ { 1 } } }$ is equal to the form $\mathcal { \beta } _ { d _ { 1 } }$ defined by Eq.(2), for some $d _ { 1 } \in \mathfrak { a } _ { 1 } ^ { - 2 }$ .Thus

$$
( \land _ { R } ^ { n } R ^ { \prime } , \widehat { \beta } ) \cong ( { \mathfrak { a } } _ { 1 } , \beta _ { d _ { 1 } } ) ,
$$

and it follows that $\mathfrak { d } = d _ { 1 } \mathfrak { a } _ { 1 } ^ { 2 }$ .Tensoring the isomorphism (3) with $F _ { \mathrm { { ; } } }$ we see that $d _ { 1 } = d f ^ { 2 }$ for some $f \in F ^ { \bullet }$ . Now defining $\mathfrak { a } = f \mathfrak { a } _ { 1 }$ ,it follows that $\mathfrak { d } = d \mathfrak { a } ^ { 2 }$ and that

$$
( \mathfrak { a } _ { 1 } , \beta _ { d _ { 1 } } ) \cong ( \mathfrak { a } , \beta _ { d } ) ,
$$

which completes the proof.□

(3.2) Example. Suppose that $R = \mathbf { Z } [ \sqrt { \mathbf { - 5 } } ]$ is the ring of integers in the field $\textcircled { 2 ( \sqrt { - 5 } ) }$ and that $R ^ { \prime }$ is the ring of integers in the quadratic extension field $\mathbf { Q } ( { \sqrt { - 5 } } , { \sqrt { 2 } } )$ 、Then the discriminant $( \Lambda _ { R } ^ { 2 } R ^ { \prime } , \widehat { \beta } )$ of this extension is isomorphic to $( { \mathfrak { p } } , \beta _ { 2 } )$ where $\mathfrak { p }$ denotes the prime ideal $2 R +$ $( 1 + { \sqrt { - 5 } } ) R$ with ${ \mathfrak { p } } ^ { 2 } = 2 R$ and where $\beta _ { 2 } ( a _ { 1 } , a _ { 2 } ) { = } 2 a _ { 1 } a _ { 2 }$ for $a _ { 1 }$ ， $a _ { 2 } \in \mathfrak { p }$ The ideal $\mathfrak { p }$ is not principal, so the ring $R ^ { \prime }$ is not free over $R$

Proof. $R ^ { \prime }$ can be described more explicitly by noting that the elements $1 , \sqrt { - 5 } , \sqrt { 2 } , \frac { 1 } { 2 } ( \sqrt { 2 } + \sqrt { - 1 0 } )$ forma basis for $R ^ { \prime }$ over Z.This can be established,for example, by embedding $F ^ { \prime } { = } \mathbf { Q } ( \sqrt { - 5 } , \sqrt { 2 } )$ in the cyclotomic field $\mathbf { Q } ( e ^ { 2 \pi i / 4 0 } )$ and using the fact that $\mathcal { R } ^ { \prime }$ is the intersection of $F ^ { \prime }$ with the ring Z[e2πi/4o] of cyclotomic integers. ([Lang, p.75].) Details of the computation will be left to the reader. The ideal $\mathfrak { d } = \mathfrak { d } _ { R ^ { \prime } / R }$ can now be computed directly. Alternatively, one can first compute the two discriminants

$$
\begin{array} { r } { ( { \small \bigwedge } _ { \bf Z } ^ { 2 } R , \hat { \beta } ) \cong { \big \langle } - 2 0 { \big \rangle } _ { \bf Z } , \qquad ( { \small \bigwedge } _ { \bf Z } ^ { 4 } R ^ { \prime } , \hat { \beta } ) \cong { \big \langle } 6 4 0 0 { \big \rangle } _ { \bf Z } } \end{array}
$$

and then make use of the identity (where n is the degree of F' over F)

$$
\mathfrak { d } _ { R ^ { \prime } / \mathbf { Z } } = \mathfrak { d } _ { R / \mathbf { Z } } ^ { n } \mathrm { n o r m } _ { R / \mathbf { Z } } \big ( \mathfrak { d } _ { R ^ { \prime } / R } \big ) ,
$$

![](images/d74b6b77ec0a5bc59737bc6fa3050a5caa90685da9be6fd27acb6bf2787cf209.jpg)

# Appendix 1. Quadratic Forms

The theory of symmetric bilinear forms is intimately related to the theory of quadratic forms.In fact, over a ring in which 2 is a unit, the two theories are indistinguishable. For this reason,it seems advisable

![](images/667507a276a8d3464a4174bd88552eacbe309c9994395e44746a2a4addfde715.jpg)

Definition. Let $( X _ { 1 } , q _ { 1 } ) , \dots , ( X _ { n } , q _ { n } )$ be modules with quadratic forms over any commutative ring $R$ . The orthogonal sum $X _ { 1 } \oplus \cdots \oplus X _ { n }$ is defined to be the direct sum of the modules $X _ { i }$ with quadratic form $q$ defined by the eauation

$$
\begin{array} { r } { q ( x _ { 1 } \oplus \cdots \oplus x _ { n } ) = \sum q _ { i } ( x _ { i } ) } \end{array}
$$

summed over $1 \leq i \leq n$

The associated bilinear form $( x | y )$ on $X = X _ { 1 } \oplus \cdots \oplus X _ { n }$ is the orthogonal sum of the associated bilinear forms $( x | y ) _ { i }$ on the $\overline { { { X } _ { i } } }$ . Hence $( x | \mathbf { y } )$ （201 is an inner product if and only if each $( x | y ) _ { i }$ is an inner product.

Definition. We will call the pair $( X , q )$ a quadratic inner product space, if $X$ is finitely generated projective, and if the bilinear form $( x | y )$ associated with the quadratic form $q$ is an inner product on $X$ (Chapter I, $\ S 1 . 1 )$

We observed in Chapter I, \$4 that the Witt Cancellation Theorem(4.4) is not true for inner product spaces in characteristic 2.It is interesting to note that the analogue of (4.4) for quadratic inner product spaces is true in any characteristic.That is, if

$$
( X _ { 1 } , q _ { 1 } ) \oplus ( X , q ) \cong ( X _ { 2 } , q _ { 2 } ) \oplus ( X , q ) ,
$$

where $( X _ { 1 } , q _ { 1 } ) _ { : }$ $( X _ { 2 } , q _ { 2 } )$ ,and $( X , q )$ are quadratic inner product spaces over a field, then $( X _ { 1 } , q _ { 1 } ) { \cong } ( X _ { 2 } , q _ { 2 } )$ This is proved in [Chevalley, p.16] or [Bourbaki, p. 71].

The following basic remark is due to [Frohlich, 1969] and independently to [Sah]. If $X _ { 1 }$ is a symmetric bilinear form module and $X _ { 2 }$ is a quadratic form module,then the tensor product $X _ { 1 } \otimes X _ { 2 }$ is a quadratic form module. In fact, given a symmetric bilinear form $\beta _ { 1 }$ on $X _ { 1 }$ and a quadratic form $q _ { 2 }$ on $X _ { 2 }$ , there is a unique quadratic form $q$ on $X _ { 1 } \otimes X _ { 2 }$ satisfying the equations,both being necessary for the definition,

$$
q \left( x _ { 1 } \otimes x _ { 2 } \right) = \beta _ { 1 } \left( x _ { 1 } , x _ { 1 } \right) q _ { 2 } \left( x _ { 2 } \right)
$$

and

$$
\left( x _ { 1 } \otimes x _ { 2 } | y _ { 1 } \otimes y _ { 2 } \right) = \beta _ { 1 } ( x _ { 1 } , y _ { 1 } ) ( x _ { 2 } | y _ { 2 } ) .
$$

Note the isomorphism

$$
\langle 1 \rangle \otimes X _ { 2 } \cong X _ { 2 } .
$$

If both $X _ { 1 }$ and $X _ { 2 }$ are quadratic form modules, then using the associated bilinear form $( x _ { 1 } | y _ { 1 } )$ as $\beta _ { 1 }$ it follows that $X _ { 1 } \otimes X _ { 2 }$ is also a quadratic form module.The quadratic form $q$ on $X _ { 1 } \otimes X _ { 2 }$ is determined by the equations

$$
q ( x _ { 1 } \otimes x _ { 2 } ) { = } 2 q _ { 1 } ( x _ { 1 } ) q _ { 2 } ( x _ { 2 } )
$$

and

$$
( x _ { 1 } \otimes x _ { 2 } | y _ { 1 } \otimes y _ { 2 } ) = ( x _ { 1 } | y _ { 1 } ) ( x _ { 2 } | y _ { 2 } ) .
$$

The factor of 2 is surprising but necessary. This factor was incorrectly left out in [Bourbaki, v. 24, p. 137].

The Witt algebra $W Q ( R )$ of quadratic inner product spaces over $R$ can now be defined as follows. (Compare [Bass], [Sah].) A quadratic inner product space $( X , q )$ is said to be split if the module $X$ contains a direct summand $N$ with $N = N ^ { \perp }$ and $q ( N ) { = } 0$ 、Two quadratic inner product spaces $( X _ { 1 } , q _ { 1 } )$ and $( X _ { 2 } , q _ { 2 } )$ belong to the same Witt class if

$$
( X _ { 1 } , q _ { 1 } ) \oplus ( S _ { 1 } , q _ { 1 } ^ { \prime } ) \cong ( X _ { 2 } , q _ { 2 } ) \oplus ( S _ { 2 } , q _ { 2 } ^ { \prime } )
$$

![](images/a2e53008643f72abf6dfdddb285f26f191448946d8a71a1fc4b8b4f8930f3eb5.jpg)

modulo $\wp ( F )$ is an invariant of $( X , q )$ .This Arf invariant depends only on the Witt class of $( X , q )$ ,and hence gives rise to an additive surjection

$$
\varDelta \colon W Q ( F ) \to F / \wp F .
$$

The kernel of 4 has been computed by H.Sah as follows. Let $\scriptstyle { \cal I } \subset W ( F )$ be the fundamental ideal. Then

$$
\mathrm { \overline { { \ k e r n e l { ( } } } } \varDelta ) = I \cdot W Q ( F ) .
$$

The resulting additive isomorphism

$$
W Q ( F ) / I \cdot W Q ( F ) { \cong } F / { \wp } F
$$

should perhaps be regarded as an analogue of Pfister's isomorphism

$$
I / I ^ { 2 } \cong F ^ { \bullet } / F ^ { \bullet 2 } .
$$

(Compare Chapter II, $\ S 5 . 2 . )$

Here is a simple example to illustrate the Arf invariant. Let $( X , q )$ be a quadratic inner product space of rank 2. We continue to assume that the field $\overline { F }$ has characteristic 2. To any basis $x , \ y$ with $( x | y ) = 1$ we associate the residue class

$$
q ( x ) q ( y ) { \pmod { g ( F ) } } .
$$

This is an invariant of $( X , q )$ . For under an elementary change of basis $\bar { x } = x + \alpha y$ we have $q ( \bar { x } ) = q ( x ) + \alpha + \alpha ^ { 2 } q ( y )$ ,and therefore

$$
q ( \bar { x } ) q ( y ) { = } q ( x ) q ( y ) { + } \wp ( \alpha q ( y ) ) .
$$

From this formula we see that the quadratic form q represents O if and only if $q ( x ) q ( y ) { \equiv } 0$ mod $\wp ( F )$ Forif $q ( x ) q ( y ) { \equiv } 0$ and $q ( y ) \neq 0$ ,then we can choose $\pmb { \alpha }$ so that $q ( { \bar { x } } ) q ( y ) = 0 .$ .In fact we can actually choose a symplectic basis $\bar { x } , \ \bar { y }$ with $q ( { \bar { x } } ) = q ( { \bar { y } } ) = 0 .$ ，simply by setting $\overline { { y } } = \beta \overline { { x } } + y$ and choosing $\beta$ appropriately.

If the field $F$ is perfect, then the residue class $q ( x ) q ( y )$ mod $\wp ( F )$ is always $^ { a }$ complete invariant for the quadratic inner product space.

Proof. We may assume that $q ( x ) \pm 0$ Choosing an arbitrary representative $\varDelta _ { 0 } = q ( x ) q ( y ) + \wp ( \alpha )$ for the Arf invariant, the symplectic basis

$$
\begin{array} { r l r } { \overline { { x } } = x / \sqrt { q ( x ) } } & { { } } & { \overline { { y } } = \alpha \overline { { x } } + y \sqrt { q ( x ) } } \end{array}
$$

will satisfy

$$
q ( \bar { x } ) = 1 , q ( \bar { y } ) = { \varDelta } _ { 0 } .
$$

Thus $\varDelta _ { 0 }$ determines the isomorphism class of $( X , q )$ □

In particular,if $F$ is $^ { a }$ finite field of characteristic 2 it follows that there are precisely two isomorphism classes of quadratic inner product spaces of rank two over F. For by inspecting the additive exact sequence $ { \boldsymbol { 0 } } \to  { \mathbf { F } } _ { 2 } \to F \longrightarrow  { \boldsymbol { \wp } } \to F$ we see that the cokernel $F / \wp ( F )$ has order two.

# Appendix 2. Hermitian Forms

Let $R$ be an associative ring with 1, not necessarily commutative. By an involution of $R$ (or more precisely an “involutory anti-automorphism") is meant an additive homomorphism $\alpha \mapsto \alpha ^ { J }$ from $R$ to itself satisfying

$$
( \alpha \beta ) ^ { J } = \beta ^ { J } \alpha ^ { J }
$$

and

$$
( x ^ { J } ) ^ { J } = \alpha
$$

for all α and β. Note that $\overline { { 1 ^ { J } = 1 } }$

Examples. If R is commutative, then the identity map of $\mathbf { \nabla } \mathcal { R }$ is an involution. For any multiplicative group $\pi$ ,the integral group ring $\mathbf { Z } \pi$ possesses a canonical involution which maps each group element $\sigma$ to $\pmb { \sigma } ^ { - 1 }$ .(Compare [Wall, δ5] as well as [Gel'fand-Mishchenko].） The ring of n $\times n$ matrices over a commutative ring has a canonical involution which maps each matrix to its transpose.

Let R be any fixed ring with involution,and let $X$ be a left $\pmb R$ module.

Definition. A hermitian form on $X$ is a function

$$
\varphi \colon X \times X \to R ,
$$

which is $R$ -linear in the first variable and satisfies

$$
\varphi ( y , x ) { = } \varphi ( x , y ) ^ { J } .
$$

It follows that $\varphi ( x , y )$ is bilinear over $\mathbf { Z } ,$ and that

$$
\overline { { { \varphi \left( \alpha x , \beta y \right) = \alpha \varphi \left( x , y \right) \beta ^ { J } . } } }
$$

If the correspondence

$$
y \mapsto \varphi ( \_ y )
$$

from $X$ to ${ \mathrm { H o m } } _ { R } ( X , R )$ is bijective, then $\varphi$ is called a hermitian inner product, and the pair $( X , \varphi )$ is called a hermitian inner product module.

Just as for symmetric inner product spaces and quadratic inner product spaces, one can define the concept of a split hermitian inner product space. Working modulo these split spaces,we obtain a Witt group of hermitian inner product spaces over $R .$ The notation $W ( R , J )$ will be used. In the commutative case, $W ( R , J )$ has a natural ring structure. If $J$ is the identity involution, then this coincides with the ordinary Witt ring $W ( R )$

If $X$ is a free $R$ -module with basis $e _ { 1 } , \ldots , e _ { n }$ ， then evidently any hermitian form $\varphi$ on $X$ is completely characterized by the matrix $[ \varphi ( e _ { i } , e _ { k } ) ]$ , which is subject only to the requirement that

$$
\varphi ( e _ { k } , e _ { i } ) = \varphi ( e _ { i } , e _ { k } ) \sp J .
$$

The form $\varphi$ is actually a hermitian inner product if and only if this matrix $[ \varphi ( e _ { i } , e _ { k } ) ]$ is invertible.

Now suppose that the ring $R$ is commutative. Then the set

$$
R _ { 0 } = \{ \alpha \in \mathbf { R } | \alpha ^ { J } = \alpha \}
$$

of fixed points forms a subring of $R$ .The determinant of the matrix $[ \varphi ( e _ { i } , e _ { k } ) ]$ is evidently an element of $\underline { { R } } _ { 0 }$ . If we choose some new basis $e _ { 1 } ^ { \prime } , \ldots , e _ { n } ^ { \prime }$ for $X$ ， the determinant will be multiplied by some arbitrary element in the image of the homomorphism

$$
\overline { { \mathrm { n o r m } } } \colon R ^ { \bullet } \to R _ { 0 } ^ { \bullet }
$$

defined by $\mathrm { n o r m } ( \alpha ) = \alpha \alpha ^ { J }$ .Definition. The (multiplicative) residue class of det $[ \varphi ( e _ { i } , e _ { j } ) ]$ modulo $\operatorname { n o r m } ( R ^ { \bullet } )$ is called the determinant of the hermitian space $X$ . This determinant is a surprisingly powerful invariant. Compare Examples 2 and 4 below.

In the commutative case, every hermitian form over $\mathcal { R }$ gives rise to a

$$
Q ( x ) = \varphi ( x , x )
$$

over $R _ { 0 }$ . In particular, this function $Q$ takes values in $R _ { 0 }$ and the associated form

$$
\begin{array} { c } { { ( x \vert y ) { = } Q ( x + y ) { - } Q ( x ) { - } Q ( y ) } } \\ { { { } } } \\ { { { = } \varphi ( x , y ) { + } \varphi ( y , x ) } } \end{array}
$$

is bilinear over $R _ { 0 }$

Suppose now that $F$ is a field with non-trivial involution. It follows from Galois theory that $E$ is a quadratic Galois extension of the fixed field $F _ { 0 }$ ：

Jacobson theorem. Two hermitian inner product spaces over $F$ are isomorphic if and only if their underlying quadratic spaces are isomorphic over $F _ { 0 }$ ：

In other words $X$ is isomorphic to $Y$ as hermitian space over $F$ whenever there is an $F _ { 0 }$ -linear mapping from $X$ onto Y preserving the -quadratic function $Q ( x ) { = } \varphi ( x , x )$ ，Thus the classification of hermitian -inner product spaces over $\boldsymbol { \mathsf { \Pi } }$ is reduced to the classification of quadratic -inner product spaces over $F _ { 0 }$

Proof $b y$ induction on the rank. First note that the field $F$ contains an element $\alpha _ { 0 }$ with $\alpha _ { 0 } + \alpha _ { 0 } ^ { J } \neq 0$ In the characteristic 2 case, $\alpha _ { 0 }$ can be any element in the complement of $F _ { 0 }$ ; while in the characteristic $\neq 2$ case we can take $\alpha _ { 0 } = 1$ ：

![](images/71e0c3f10d711f7f14feb8f1b791e8faacf14f9c188662a101745730d6ae2f17.jpg)

$$
( x | y ) { = } \varphi ( x , y ) { + } \varphi ( y , x )
$$

is an inner product over $F _ { 0 }$ . In fact, given $x \neq 0$ we can certainly choose $x ^ { \prime }$ so that $\varphi \left( x , x ^ { \prime } \right) { \neq } 0 .$ After multiplying $x ^ { \prime }$ by an appropriate field element, we may assume that $\varphi \left( x , x ^ { \prime } \right) = \alpha _ { 0 }$ ,and it follows that

$$
( x | x ^ { \prime } ) = \alpha _ { 0 } + \alpha _ { 0 } ^ { J } \neq 0 .
$$

Suppose now that the hermitian inner product spaces $X$ and $Y$ are isomorphic as $F _ { 0 }$ -quadratic spaces. Since the associated bilinear form $( x | x ^ { \prime } )$ is not identically zero,we can certainly choose a vector $x \in X$ and a corresponding vector y∈ Y with $Q ( x ) = Q ( y ) \neq 0 .$

Since $\varphi ( x , x ) \neq 0$ it follows, just as in Chapter $\mathbf { I } , \ S 3 .$ ,that the hermitian space $X$ is isomorphic to an orthogonal sum $( F x ) \oplus ( F x ) ^ { \perp }$ . Similarly $Y$ is isomorphic to $( F y ) \oplus ( F y ) ^ { \perp }$ . But evidently $( F x ) \cong ( F y )$

Now let us pass to the underlying quadratic spaces over $\overline { { F _ { 0 } } }$ ，and apply the Witt cancellation theorem. (Compare Chapter I, $\ S 4$ and Appendix 1.) It follows that $( F x ) ^ { \perp }$ is isomorphic as quadratic space to $( F y ) ^ { \perp }$ .Using the induction hypothesis,it follows that $( F x ) ^ { \perp } \cong ( \bar { F } y ) ^ { \perp }$ as hermitian space, and therefore $X \cong Y .$ □

Corollary. With $F { \supset } F _ { 0 }$ as above,there is an exact sequence

$$
0 \to W ( F , J ) \to W Q ( F _ { 0 } ) \to W Q ( F )
$$

of $W ( F _ { 0 } )$ -modules.

Proof. Given a non-zero element of $W ( F , J )$ ,we can clearly choose a representative hermitian inner product space $X$ which is anisotropic:

$$
\varphi ( x , x ) \mp 0 \mathrm { f o r } x \neq 0 .
$$

It follows that the underlying quadratic space is also anisotropic, and hence represents a non-zero element of $W Q ( F _ { 0 } )$ . Thus the natural homomorphism $W ( F , J ) \to W Q ( F _ { 0 } )$ is injective.

Next let us look at the composition $W ( F , J ) \to W Q ( F _ { 0 } ) \to W Q ( F ) .$ （ Choose a basis $\{ 1 , \alpha \}$ for $F$ over $F _ { 0 }$ . First consider a hermitian space $X$ of dimension 1 over $F .$ Then $X$ has a basis vector $e _ { 1 }$ with $\varphi ( e _ { 1 } , e _ { 1 } ) \in F _ { 0 } ^ { \bullet }$ It follows that X is 2-dimensional over $F _ { 0 }$ with basis $\{ e _ { 1 } , e _ { 2 } \}$ where 2 $e _ { 2 } = \alpha e _ { 1 }$ ,and

$$
\scriptstyle Q ( e _ { 2 } ) = \alpha \alpha ^ { J } Q ( e _ { 1 } ) , \quad ( e _ { 1 } + e _ { 2 } ) = ( \alpha + \alpha ^ { J } ) Q ( e _ { 1 } ) .
$$

(It may be convenient to choose $\pmb { \alpha }$ so that $\alpha + \alpha ^ { J } = 1$ in the characteristic 2 case,or $\boldsymbol { \alpha } + \boldsymbol { \alpha } ^ { J } = 0$ in the characteristic $\neq 2$ case; but this is not necessary.)

Now let us pass to the induced quadratic space $F _ { \ @ } X$ of dimension $\pmb { F _ { 0 } }$ 2 over_F.Consider the non-zero vector $\alpha \otimes e _ { 1 } - 1 \otimes e _ { 2 }$ in this_induced space.Evidently

$$
\begin{array} { c } { { \mathcal { Q } \left( \alpha \otimes e _ { 1 } - 1 \otimes e _ { 2 } \right) = \alpha ^ { 2 } \mathcal { Q } \left( e _ { 1 } \right) + \mathcal { Q } \left( e _ { 2 } \right) - \alpha \left( e _ { 1 } | e _ { 2 } \right) } } \\ { { { } } } \\ { { = \left( \alpha ^ { 2 } + \alpha \ : \alpha ^ { J } - \alpha \left( \alpha + \alpha ^ { J } \right) \right) \mathcal { Q } \left( e _ { 1 } \right) = 0 . } } \end{array}
$$

Therefore this induced quadratic space is split. Since any hermitian inner product space over $F$ is clearly an orthogonal sum of 1-dimensional spaces,this proves that the composition $W ( F , J ) \to W Q ( F _ { 0 } ) \to W Q ( F )$ is zero.

Conversely let $Y$ be a quadratic space over $F _ { 0 }$ which maps to zero in $W Q ( F )$ . After eliminating any split orthogonal summand, we may assume that Y is anisotropic. Since $\frac { F \otimes Y } { F _ { 0 } }$ is split, it certainly contains a vector $y$ 丰 $\mathbf { 0 }$ with $Q \left( y \right) = 0$ Setting

$$
y = \alpha \otimes y _ { 1 } - 1 \otimes y _ { 2 }
$$

with $y _ { 1 } , y _ { 2 } \in Y ,$ we have

$$
Q ( y ) { = } \alpha ^ { 2 } Q ( y _ { 1 } ) + Q ( y _ { 2 } ) { - } \alpha ( y _ { 1 } | y _ { 2 } ) { = } 0 .
$$

Substituting

$$
a ^ { 2 } = a ( x + a ^ { J } ) - a a ^ { J }
$$

and recalling that 1 and $\pmb { \alpha }$ are linearly independent over $F _ { 0 }$ , it follows that

$$
\begin{array} { c } { { ( y _ { 1 } | y _ { 2 } ) = ( \alpha + \alpha ^ { J } ) ~ Q ( y _ { 1 } ) } } \\ { { { } } } \\ { { Q ( y _ { 2 } ) = \alpha \alpha ^ { J } ~ Q ( y _ { 1 } ) , } } \end{array}
$$

where $Q ( y _ { 1 } ) \pm 0$ since $Y$ is anisotropic. This proves that the subspace of $Y$ spanned by $\mathcal { V } _ { 1 }$ and $y _ { 2 }$ is isomorphic to the underlying quadratic space of a hermitian space over $F$ spanned by a vector $\mathcal { Y } _ { 1 }$ with $\varphi ( y _ { 1 } , y _ { 1 } ) =$ $\mathbb { Q } ( y _ { 1 } ) .$ where $\pmb { \alpha } y _ { 1 }$ corresponds to the vector $\overline { { y _ { 2 } } }$ ：

Now express Y as an orthogonal sum $( F _ { 0 } y _ { 1 } @ F _ { 0 } y _ { 2 } ) \oplus ( F _ { 0 } y _ { 1 } @ F _ { 0 } y _ { 2 } ) ^ { \pm }$ The second summand has smaller rank, is also anisotropic,and also represents an element of the kernel. A straightforward induction now completes the proof.□

Here are some examples worked out in more detail. (Compare [Milnor, 1969].) In each case we assume that the involution $J$ is not the identity.

Example 1.If F is a finite field, then a hermitian inner product space splits if and only if it has even rank.The rank is a complete invariant; and $W ( F , J ) \cong \mathbf { Z } / 2$

Note that the description is exactly the same whether the characteristic is 2 or $\neq 2$ .The proof will be left to the reader.

Example 2. If $F$ is a local field,or a function field in one variable over a finite field, then the rank and determinant of a hermitian inner product space form a complete system of invariants. The kernel of the rank homomorphism $W ( F , J ) \to \mathbf { Z } / 2$ is an ideal, additively isomorphic to $F _ { 0 } ^ { \bullet } / \mathbf { n o r m } F ^ { \bullet }$ , and with square equal to 0.

Again the characteristic 2 case is not distinguished in any way. The proof can be sketched as follows. It suffices to note that any space $X$ of rank $\geq 2$ over $F$ has rank $\geq 4$ over $F _ { 0 }$ ， hence the quadratic equation $Q ( e _ { 1 } ) = 1$ has a solution. (Using the Hasse-Minkowski theorem in the global case; compare Chapter II, $\ S 3$ .For the characteristic 2 case, see [Arf,pp.164-167].） Hence $X$ is isomorphic to an orthogonal sum $( F e _ { 1 } ) \oplus ( F e _ { 1 } ) ^ { \perp }$ . Continuing inductively, we find an orthogonal basis $e _ { 1 } , \ldots , e _ { n }$ with $\varphi ( e _ { i } , e _ { i } ) { = } Q ( e _ { i } ) { = } 1$ for $i < n$ ，Hence the determinant' $\varphi ( e _ { n } , e _ { n } )$ determines the structure of $\pmb { X }$ completely.

Example 3. If $F$ is the field $\mathbf { C }$ of complex numbers, with complex conjugation as involution, then clearly the rank and signature of the underlying quadratic space form a complete system of invariants.Hence $W ( { \bf C } , { \mathrm { c o n j u g a t i o n } } ) { \cong } { \bf Z } .$

Example 4. If F is an algebraic extension of the rationals, then every conjugation preserving embedding $\omega$ ： $\mathbf { \nabla } F \to \mathbf { C }$ gives rise to a signature homomorphism

$$
\omega _ { * } \colon W ( F , J ) \to W ( \mathbf { C } , \mathrm { c o n j u g a t i o n } ) { \cong } \mathbf { Z } .
$$

The rank, determinant,and these various signatures form a complete system of invariants for a hermitian inner product space over $F .$ For details, the reader is referred to [Landherr].

To conclude this section, we remark that Jacobson's theorem applies also in certain non-commutative situations. For the statement to make sense however, we must assume that the fixed point set $R _ { 0 }$ of the involution $J$ is a subring, contained in the center of R.This is notably the case if $R$ is a quaternion algebra with basis $1 , i , j ,$ and $i j = - j i$ over $R _ { 0 }$ ， where $i ^ { 2 }$ and $j ^ { 2 }$ belong to $R _ { 0 } ^ { \bullet }$ .Here $R _ { 0 }$ should be a field of characteristic $\neq 2$ .The involution is defined by $i ^ { J } = - i$ $j ^ { J } = - j$ 、Note that the norm $\xi \xi ^ { J }$ of an element $\xi = \alpha + \beta i + \gamma j + \delta i j$ is equal to

$$
\alpha ^ { 2 } - \beta ^ { 2 } i ^ { 2 } - \gamma ^ { 2 } j ^ { 2 } + \delta ^ { 2 } i ^ { 2 } j ^ { 2 } .
$$

If 55+0 for $\xi \neq 0$ ，or in other words if the associated inner product

$$
\langle 1 \rangle \oplus \langle - i ^ { 2 } \rangle \oplus \langle - j ^ { 2 } \rangle \oplus \langle i ^ { 2 } j ^ { 2 } \rangle
$$

over Ro is anisotropic, then clearly R is a division algebra(=skew field). In this case，Jacobson's argument applies just as before.There is a canonical embedding

$$
0 \to W ( R , J ) \to W Q ( R _ { 0 } ) ,
$$

and two hermitian inner product spaces are isomorphic if and only if their underlying quadratic spaces are isomorphic over $\scriptstyle { \mathcal { R } } _ { 0 }$ ：

Jacobson remarks also that the“determinant” of a hermitian space can still be defined， in this non-abelian context, as an element of $R _ { 0 } ^ { \bullet } / \mathrm { n o r m } ( R ^ { \bullet } )$ .The definition is based on work of E.H.Moore.(Compare [Dyson].)

# Appendix 3. The Hasse-Minkowski Theorem

The Hasse-Minkowski theorem is one of the most beautiful results in algebraic number theory. The proof which follows assumes some knowledge of Class Field Theory,as described in [Lang] or [CasselsFrohlich].In the case of the rational field, it is possible to give a more elementary proof. (See [Serre] or [Borevich-Shafarevich].） For a complete and self-contained proof in the general case, see [O'Meara]. First some definitions.Let X be an inner product space over a field F. Then X is said to represent a field element $\pmb { \alpha }$ if there exists a non-zero vector $\mathbf { \boldsymbol { x } } \in X$ with $x \cdot x { } = \alpha$

Henceforth we assume that $F$ has characteristic $\neq 2$

Lemma 1. If a space $X$ over $F$ represents O, then it represents every element of F.

Forif X represents O then X admits a hyperbolic plane as direct summand (Chapter I, S 6), and a hyperbolic plane clearly represents all field elements.□

Corollary. $A$ space $X$ represents the element $\alpha \neq 0$ if and only if the orthogonal sum $X \oplus \langle - \alpha \rangle$ represents 0.

(In other words an inhomogeneous equation in n variables can be expressed as a homogeneous equation in $n + 1$ variables.） The proof is immediate.□

Now suppose that $E$ isaglobal field.Thatis,Fis either finite over the rational numbers, or finitely generated of transcendence degre 1 over a finite field. We continue to assume that $\boldsymbol { F }$ has characteristic =2.

For every (non-trivial) valuation $\boldsymbol { v }$ of $F _ { i }$ let $F _ { v }$ denote the completion, and let $X _ { v }$ denote the induced inner product space $F _ { v } \otimes X$ over $F _ { v }$ . Let $\pmb { \alpha }$ be some fixed element of $F .$

Hasse-Minkowski theorem. The inner product space $X$ represents $\pmb { \alpha }$ if and only if $X _ { v }$ represents $\pmb { \alpha }$ for every (non-trivial） valuation v of $F .$ ：

Both archimedian and non-archimedian valuations $\pmb { v }$ must be ineluded.

In order to prove this theorem, it will be convenient to break it up into two parts,according as the field element $\pmb { \alpha }$ is zero or non-zero:

Assertion $A _ { n }$ . Let $\alpha \in F ^ { \bullet }$ $A$ space $X$ of rank n over $F$ represents α if and only if $X _ { v }$ represents $\pmb { \alpha }$ for every $v$

Using the corollary to Lemma 1 above, this is completely equivalent to the following statement.

Assertion ${ \pmb A } _ { \pmb { n } } ^ { \prime }$ ： $A$ space $Y$ of rank $n { + 1 }$ over $F$ represents O if and only if the completion $Y _ { v }$ represents O for every valuation $v$

Note the shift from dimension $n$ to $n + 1$ in Assertion $A _ { n } ^ { \prime }$

In order to prove these two statements, we will pass back and forth between the two forms, first proving $A _ { 2 }$ ,and then showing that

$$
\overline { { A _ { 2 } ^ { \prime } \Rightarrow A _ { 3 } \Rightarrow A _ { n } ^ { \prime } } }
$$

for $\overline { { n \mathop { = } 4 } }$ The proof of $\overline { { A _ { 1 } } }$ will be given last, since it is completely irrelevant to the rest of the argument.

Proof of $A _ { 2 }$ . Suppose that $X \cong \langle u _ { 1 } \rangle \oplus \langle u _ { 2 } \rangle$ . We must try to solve the equation

$$
u _ { 1 } \xi ^ { 2 } + u _ { 2 } \eta ^ { 2 } = \alpha ,
$$

where $\pmb { \alpha }$ 0.Alternatively, seting $u = - u _ { 2 } / u _ { 1 }$ and $\beta = \alpha / u _ { 1 }$ ,this can be written as

$$
\zeta ^ { 2 } - u \eta ^ { 2 } = \beta .
$$

Let $K$ denote the extension field $F ( \sqrt { u } ) { = } F ( \sqrt { - u _ { 2 } / u _ { 1 } } )$ Then the Eq.(1) possesses a solution $\xi , \eta \in F$ if and only if $\beta$ belongs to the image of the norm homomorphism

$$
\underline { { { \mathrm { n o r m } } _ { K / F } } } \colon K ^ { \bullet } \to F ^ { \bullet } .
$$

If $K \neq F$ this is clear, since $\mathfrak { n o r m } ( \xi + \eta \sqrt { u } ) = \xi ^ { 2 } - \eta ^ { 2 } u$ If $K = F$ it is clear since $u _ { 2 } \in - u _ { 1 } F ^ { \bullet 2 }$ ，so the inner product space $X$ splits and the Eq.(1) always has a solution.

Now recall the following:

Hasse norm theorem. Let $K$ be a cyclic Galois extension of the global field $F$ .Then an element $\pmb { \alpha }$ of $F ^ { \bullet }$ belongs to the image of the homomorphism $\scriptstyle { \mathrm { n o r m } } = { \mathrm { n o r m } } _ { K / F } ;$ $K ^ { \bullet }  F ^ { \bullet }$ if and only if $\pmb { \alpha }$ belongs to the image of

for every valuation w of K.

This is proved in [Lang, p. 195] or [Cassels-Frohlich, p. 185].

If the Eq.(1) has a solution in $F _ { v }$ for every $v$ ，then $\beta$ is a norm from $K _ { w } ^ { \bullet }$ for every $w _ { \mathrm { { ; } } }$ hence $\beta$ is a norm from $K$ by the Hasse norm theorem. This completes the proof of Assertion $A _ { 2 }$

![](images/b747f078c9b703b17c311e5ed2c37caa58ae411c52f1a92b77864b9f3df697d2.jpg)

Let $T = T ( u _ { 1 } , u _ { 2 } , u _ { 3 } )$ denote the finite set consisting of all(equivalence classes of) valuations $v$ such that either

(1) $v$ is archimedian or dyadic, or

$$
\mid u _ { 1 } \mid _ { v } \pm 1 ~ \mathrm { o r } ~ \vert u _ { 2 } \vert _ { v } \pm 1 ~ \mathrm { o r } ~ \vert u _ { 3 } \vert _ { v } \pm 1 .
$$

For vdT we see as in Chapter II, $\ S 3 . 4$ that the completed space $\scriptstyle { Z _ { v } }$ necessarily represents 0.

Suppose now that $X _ { v }$ represents 0. Then we can certainly choose vectors $y _ { v } \in Y _ { v }$ and $\boldsymbol { z } _ { v } \in \boldsymbol { Z } _ { v }$ ，not both zero,so that $y _ { v } \cdot y _ { v } + z _ { v } \cdot z _ { v } = 0$ In fact these vectors can be chosen so that

$$
y _ { v } \cdot y _ { v } = - z _ { v } \cdot z _ { v } \mp 0 .
$$

For if our first choice of $y _ { v }$ and $z _ { v }$ yields $y _ { v } \cdot y _ { v } = z _ { v } \cdot z _ { v } = 0$ ,then either $Y$ represents O, in which case we can choose an arbitrary $z _ { v } ^ { \prime }$ with $z _ { v } ^ { \prime } \cdot z _ { v } ^ { \prime } \ne 0$ and apply Lemma 1,or Z represents O in which case any $y _ { v } ^ { \prime } \cdot y _ { v } ^ { \prime } \neq 0$ will do.

We will also make use of the following.

Weak approximation theorem. Given finitely many inequivalent valuations $v _ { 1 } , \ldots , v _ { t }$ on $^ { a }$ field $F ,$ the image of the diagonal embedding

is everywhere dense.

This is proved for example in Lang, Algebra, Addison-Wesley 1965, p.285.

Now consider the $( n - 2 )$ -dimensional vector space $Y$ over $F ,$ and the set $T = \{ v _ { 1 } , \ldots , v _ { t } \}$ . Applying this approximation theorem to each of the $n - 2$ coordinates,we see that the image of the diagonal embedding $Y {  Y _ { v _ { 1 } } \times \cdots \times Y _ { v _ { t } } }$ is dense. In particular, we can choose an element $y \in Y$ which is so close to $y _ { v }$ for each $v \in T$ that the ratio $( y \cdot y ) / ( y _ { v } \cdot y _ { v } )$ is a square in $F _ { v } ^ { \bullet }$ ：

Let us apply Assertion $\overline { { A _ { 3 } } }$ to the space Z. For each $\boldsymbol { v } \in T$ the completion $\overline { { Z _ { v } } }$ represents $- y _ { v } \cdot y _ { v }$ and therefore represents $\underline { { - y \cdot y } }$ But for each v $T$ the completion represents 0,and therefore represents -y · y. Applying $A _ { 3 }$ , it follows that $Z$ itself represents $- y \cdot y$ ，and therefore $X = Y \oplus Z$ represents 0. This completes the proof of $A _ { n }$ and $A _ { n } ^ { \prime }$ for $n \geq 2$

To conclude the proof of the Hasse-Minkowski theorem,we must prove Assertion $A _ { 1 }$ . Given $X \cong \langle u \rangle$ , and given $\alpha \neq 0$ in $F _ { \ast }$ ，we must solve the equation

$$
u \xi ^ { 2 } = a .
$$

Setting $\alpha / u = \beta ,$ this can be written as $\begin{array} { r } { \xi ^ { 2 } = \beta . } \end{array}$ Thus we must prove the following.

Square theorem. $I f$ the field element $\beta \in F ^ { \bullet }$ is a square in the completion $F _ { v }$ for every $v$ then $\beta$ is $^ { a }$ square in $F .$

This theorem follows easily from the basic inequalities of global class field theory.Recall that the idele group $A _ { F } ^ { \bullet }$ is the group of units in the ring $A _ { F } { \LARGE \subset } \prod F _ { v }$ consisting of all elements $( a _ { v } )$ in the cartesian product which satisfy the condition $\textstyle | a _ { v } | _ { v } \leq 1$ for almost all $v$ (In forming this cartesian product, one of course chooses just one valuation $v$ in each non-trivial equivalence class of valuations.) The quotient $\ A _ { F } ^ { \bullet } / F ^ { \bullet }$ is called the idele class group $C _ { F }$ . For any finite extension $K { \supset } F ,$ the local norm homomorphisms $K _ { w } ^ { \bullet } \to F _ { w | F } ^ { \bullet }$ combine to yield the global norm homorphisms $A _ { K } ^ { \bullet } \substack { \longrightarrow } A _ { F } ^ { \bullet }$ ，and $\dot { C } _ { K } \to C _ { F }$ . If $K$ is cyclic of degree m over $F ,$ then the inequalities of class field theory state that the index of the subgroup norm $_ { \mathbf { \tilde { \mathbf { \mathbf { K } } } } / \mathbf { F } } C _ { \kappa } { \subset } C _ { F }$ is equal to m. See [Lang, p.192] or [CasselsFrohlich, p.179].

Proof of the square theorem. Given $\beta \in F ^ { \bullet }$ ,let $\scriptstyle K = F ( { \sqrt { \beta } } )$ If $\overline { { \beta } }$ isa square in $F _ { v }$ for every $v$ ,then $K _ { w } = F _ { w | F }$ for every valuation w of $K$ ,so the norm homomorphism $A _ { K } ^ { \bullet } \substack { \longrightarrow } A _ { F } ^ { \bullet }$ is surjective. Therefore the norm homomorphism $C _ { \kappa } {  } C _ { { \scriptscriptstyle F } }$ is surjective, and the degree m must be 1. Thus ${ \sqrt { \beta } } \in F ,$ which completes the proof of the square theorem and the HasseMinkowski theorem.0

Now consider a more general situation. Let X and Y be two inner product spaces over a field F with rank(X)≥rank(Y).

Definition. The space $X$ is said to represent $Y$ if $X \cong Y \oplus Z$ for some $Z$

If Y has rank 1, say $Y \cong \langle u \rangle$ , then clearly $X$ represents $Y$ if and only if $X$ represents u.

Corollary 1. Suppose again that $F$ is a global field.If the completion $\textstyle \sum _ { v }$ represents $\underline { { Y } } _ { v }$ for every valuation $v$ ,then $X$ represents Y.

Proof. This is certainly true if Y has rank 1. If the rank of Y is greater than 1, then, setting $Y = Y ^ { \prime } \oplus \langle u \rangle$ ， we may assume inductively that $X$ represents $Y ^ { \prime }$ say

$$
X \cong Y ^ { \prime } \oplus Z ^ { \prime } .
$$

By hypothesis,for each $v$ there exists a space $Z ( v )$ over $F _ { v }$ so that

$$
\begin{array} { c } { { X _ { v } \cong Y _ { v } \oplus Z ( v ) } } \\ { { \cong Y _ { v } ^ { \prime } \oplus \langle u \rangle _ { v } \oplus Z ( v ) . } } \end{array}
$$

Comparing this isomorphism with the completion of (2), and applying the Witt cancellation theorem, we obtain

$$
\begin{array} { r } { Z _ { v } ^ { \prime } \cong \langle u \rangle _ { v } \oplus Z ( v ) . } \end{array}
$$

Thus $Z _ { v } ^ { \prime }$ represents $u$ for every $v$ 、By the Hasse-Minkowski theorem,it follows that $\mathbf { Z ^ { \prime } }$ represents $u$ ,say

$$
Z ^ { \prime } \cong \langle { u } \rangle \oplus Z ^ { \prime \prime } .
$$

Together with (2),this completes the proof.

Corollary 2. Two spaces X and Y over $\overline { F }$ are isomorphic if and only if $X _ { v }$ is isomorphic to $Y _ { v }$ for every v. In particular $X$ splits if and only if $X _ { v }$ splits for every $v$

Proof. This is just the special case rank $( X ) { = } \operatorname { r a n k } ( Y )$ of Corollary 1, using Chapter I. $\ S 6 . 3$

Here is still another formulation of the Hasse-Minkowski theorem.

Corollary 3. Consider a quadratic equation $\begin{array} { r } { \sum \alpha _ { i j } \xi _ { i } \xi _ { j } + \sum \beta _ { k } \xi _ { k } + \gamma = 0 , } \end{array}$ in nvariables,with coefcientsinthe global fieldF.If this equation has $^ { a }$ solution in $F _ { v }$ for every $\pmb { \vartheta }$ then it has $^ { a }$ solution in F.

Note that the corresponding statement for equations of higher degree, or for systems of quadratic equations,would be false.Here is a trivial example. The 6-th degree equation

$$
( \zeta ^ { 2 } + 1 ) ( \zeta ^ { 2 } + 1 7 ) ( \zeta ^ { 2 } - 1 7 ) = 0
$$

has a solution in $\mathbf { Q } _ { v }$ for every $v$ ,but has no rational solution. Similarly, consider the simultaneous quadratic equations

$$
\begin{array} { c } { { \xi ^ { 2 } + \eta = 0 , } } \\ { { \qquad \quad } } \\ { { ( \eta - \zeta ) ( \eta - \zeta + 1 6 ) = 0 , } } \\ { { \qquad \quad } } \\ { { \zeta ^ { 2 } = 1 7 ^ { 2 } . } } \end{array}
$$

For any solution $( 5 , 1 , 5 )$ we must have $\zeta = \pm 1 7$ hence $\eta { = } 1$ ,17,-17 or-33,and $\zeta ^ { 2 } + \eta = 0$ Again there is a solution in $\mathbf { Q } _ { v }$ for every $v$ but no solution in $\mathbf { Q }$ ，

Proof of Corollary 3.Write the given equation as

$$
\alpha ( x , x ) + \beta ( x ) + \gamma = 0 ,
$$

where $\pmb { \alpha }$ is a symmetric bilinear form on the vector space $X = F ^ { n }$ and where $\beta$ is an element of the dual vector space ${ \mathrm { H o m } } ( X , F )$ Let $N$ be the null space of the linear mapping $x \mapsto \alpha ( x , \ )$ from $X$ to ${ \mathrm { H o m } } ( X , F )$ Counting dimensions, we see that the sequence

$$
\cdot 0 \to N { \to } X { \to } \mathrm { H o m } ( X , F ) { \to } \mathrm { H o m } ( N , F ) { \to } 0 .
$$

is exact.

If the element $\beta \in { \mathrm { H o m } } ( X , F )$ restricts to a non-zero element of ${ \mathrm { H o m } } ( N , F ) .$ ，then it is easy to choose $x \in N$ so as to satisfy the required equation

$$
0 + \beta ( x ) + \gamma = 0 .
$$

Suppose then that $\beta$ maps to zero in ${ \mathrm { H o m } } ( N , F )$ Then $\beta$ lifts to an   
element of $X$ ,say $\beta ( x ) = 2 \alpha ( x _ { 0 } , x )$

for every $x \in X$ . The substitution $\scriptstyle x = y - x _ { 0 }$ now reduces Eq.(3) to the form

$$
\alpha ( y , y ) = \gamma ^ { \prime } ,
$$

![](images/3e221c2c4cc2c1ea77b700ff79e91f496115f2790e57594d09c4a2ce19fd3689.jpg)

# Appendix 4. Gauss Sums, the Signature mod 8, and Quadratic Reciprocity

Let $L$ be a free $\mathbf { z }$ -module of rank $n _ { : }$ ，provided with a $\mathbf { z }$ -valued symmetric bilinear form $x \cdot y$ with non-zero determinant. We denote the signature of this form by $\sigma$ ，and the absolute value of the determinant by $d .$ 、An expression for $\exp ( 2 \pi i \sigma / 8 )$ as a finite exponential sum was given by H.Braun in 1940.(Explicitly,she showed that

$$
\frac { ( 2 a ) ^ { n / 2 } { \sqrt { d } } \exp ( 2 \pi i \sigma / 8 ) { = } \sum _ { x \in L / a L } \exp ( 2 \pi i x \cdot x / a ) } { x \in L / a L }
$$

where $a = 8 d ^ { 3 }$ It follows that σ mod8 is determined by the $a ^ { n }$ numbers $x \cdot x$ modulo $^ { a }$ ） We will describe a closely related formula which has recently been obtained by J.Milgram. (Compare the discussion in Chapter I1, $\ S 5 .$ ）

As in Chapter I,we will say that $L$ is of type IIif the congruence is satisfied for every $\overline { { x } } \in E$ Let $L ^ { \# }$ denote the dual lattice, consisting of all $u \in \mathbf { Q } \otimes L$ satisfying the condition $u \cdot L \subset \mathbf { Z }$ ：Then the quotient $L ^ { \# } / L$ is a finite abelian group of order $d .$ If $L$ is of type II, then setting

$$
\varphi ( u ) { = } \frac { 1 } { 2 } u \cdot u \qquad \mathrm { m o d u l o } { \bf Z } ,
$$

we obtain a well defined quadratic function $\varphi$ ： $L ^ { \# } / L \to \mathbf { Q } / \mathbf { Z }$

Theorem (Milgram). If Lis of type II, then the Gauss sum is defined and is equal to ${ \overline { { \sqrt { d } } } } \exp ( 2 \pi i \sigma / 8 ) .$

The original proof of this formula was a rather delicate argument involving the Poisson summation formula. The following proof,suggested by Knebusch, is quite a bit easier.

Consider lattices $L$ of type II in a fixed rational inner product space. We will denote the $d$ foldsum ∑exp(2πiφ(u))=∑exp(πiu·u) briefly by the symbol $G ( L )$ LL LL

Lemma 1. If $L _ { 1 } { \subset } L$ is $^ { a }$ sub-lattice of index $k _ { \ast }$ then $G ( L _ { 1 } ) = k G ( L ) .$

Proof.Evidently $L _ { 1 } { \subset } L { \subset } L ^ { \# } { \subset } L _ { 1 } ^ { \# }$ where the index of each lattice in the next is equal to $k _ { : }$ or $d ( L ) ,$ or $k$ respectively. Let $x _ { 1 } , \dots , x _ { k d ( L ) }$ be a complete set of coset representatives for $L _ { 1 } ^ { \# }$ modulo $L _ { ☉ }$ Then the Gauss -sum $G ( L _ { 1 } )$ can be written as

$$
G ( L _ { 1 } ) = \sum _ { { \bf \Phi } _ { ^ { \lambda } , J } } \sum _ { u \in L / L _ { 1 } } \exp \bigl ( 2 \pi i \varphi ( x _ { j } + u ) \bigr ) .
$$

If we substitute

$$
\varphi ( x _ { j } + u ) { \equiv } \varphi ( x _ { j } ) + x _ { j } \cdot u { \pmod { \mathbf { Z } } } ,
$$

this becomes

$$
G ( L _ { 1 } ) { = } \underset { x _ { j } } { \sum } \exp \bigl ( 2 \pi i \varphi ( x _ { j } ) \bigr ) \sum _ { u \in L / L _ { 1 } } \exp \bigl ( 2 \pi i ( x _ { j } \cdot u ) \bigr ) .
$$

But for each fixed $\underline { { x } } _ { j }$ the $k$ -fold sum

can be evaluated as follows. If $x _ { j }$ happens to belong to $L ^ { \# }$ , this sum is evidently equal to $1 + \cdots + 1 = k .$ f $x _ { j } \notin { L } ^ { \# }$ then the correspondence

$$
\begin{array} { r } { u \mapsto \exp \bigl ( 2 \pi i ( x _ { j } \cdot u ) \bigr ) } \end{array}
$$

defines a non-trivial homomorphism from $L / L _ { 1 }$ to C, so a standard argument [Lang, p.82] shows that the sum (2) is zero. Therefore $G ( L _ { 1 } )$ is equal to

$$
\sum _ { x _ { j } \in L ^ { \# } / L } \exp \bigl ( 2 \pi i \varphi ( x _ { k } ) \bigr ) k { = } k G ( L )
$$

as asserted.□

Evidently $d ( L _ { 1 } ) = k ^ { 2 } d ( L )$ ; so it follows from Lemma 1 that

$$
G ( L ) / \sqrt { d ( L ) } { = } G ( L _ { 1 } ) / \sqrt { d ( L _ { 1 } ) } .
$$

In fact the complex number $G ( L ) / \sqrt { d ( L ) }$ is completely independent of the lattice $L ,$ and depends only on the ambient rational inner product space. This is clear, since any two lattices $\scriptstyle { \pmb { L } }$ and $\scriptstyle { \mathcal { L } }$ spanning the same rational space must contain a common sub-lattice $L \cap E$ which has finite index in each of them.

To evaluate this invariant $G ( L ) / \sqrt { d ( L ) }$ of the inner product space $\mathbf { Q } \otimes L$ ，we recall that every rational inner product space is isomorphic to an orthogonal sum of 1-dimensional spaces, and hence contains a lattice of type I which splits as an orthogonal sum of 1-dimensional lattices.Note that the invariant $G ( L ) / \sqrt { d ( L ) }$ is multiplicative with respect -to orthogonal sums. For the identity

is easily verified,and the identity

$$
d ( L _ { 1 } \oplus L _ { 2 } ) = d ( L _ { 1 } ) d ( L _ { 2 } )
$$

is familiar. Thus to compute this invariant $G ( L ) / \sqrt { d ( L ) }$ for any rational inner product space, it suffices to compute it for a 1-dimensional inner product space.

The following elementary observation will be needed for the computation in the 1-dimensional case.

Lemma 2. For any constant $c > 0$ ，the integral $\int \limits _ { 0 } ^ { A } \exp ( c \pi i s ^ { 2 } ) d s$ tendsto a well defined finite limit as $A \to \infty$ ：

To prove that the imaginary part of this integral converges, substitute $\stackrel { - } { u } = c s ^ { 2 }$ and integrate between successive integer values of $u ,$ noting that the terms of the resulting series alternate in sign, with absolute values tending monotonely to zero. Convergence of the real part is proved similarly, using half-integer values. 0

Consider now a 1-dimensional lattice of type H, say $L \cong \langle 2 m \rangle$ ： Suppose, to fix our ideas, that $m > 0$ Evidently $L ^ { \# } / L$ is cyclic of order 2m, and $G ( L )$ is equal to the $2 m \cdot$ -fold sum

To evaluate this sum, following Dirichlet and Landau, we introduce an associated periodic function $f \colon \mathbf { R }  \mathbf { C }$ of period 1, where

$$
f ( t ) { = } \sum _ { k = 0 } ^ { 2 m - 1 } \exp ( \pi i ( k { + } t ) ^ { 2 } / 2 m )
$$

for $0 \leq t \leq 1$ Thus $f ( 0 ) { = } f ( 1 )$ is equal to the Gauss sum $G ( L ) .$ (Compare [Lang, p. 88].)

Since f is continuous and piecewise smooth, its Fourier series expansion converges to $f$ everywhere. (See, for example, Titchmarsh, Theory of Functions; or Courant and Hilbert, Volume 1.) We will write this Fourier series in the form

where

$$
f ( t ) { = } \sum _ { - \infty } ^ { \infty } a _ { n } \exp ( - 2 \pi i n t ) ,
$$

$$
a _ { n } { = } \intop _ { 0 } ^ { 1 } f ( t ) \exp ( 2 \pi i n t ) d t .
$$

To evaluate the coefficient $a _ { n }$ ,first substitute the definition of $f ( t ) ,$ obtaining

$$
a _ { n } = \sum _ { k = 0 } ^ { 2 m - 1 } \int \exp \left( 2 \pi i \left( \frac { ( k + t ) ^ { 2 } } { 4 m } + n t \right) \right) d t .
$$

Next complete the square, so as to obtain the congruence

$$
{ \frac { ( k + t ) ^ { 2 } } { 4 m } } + n t \equiv ( k + t + 2 m n ) ^ { 2 } / 4 m { \pmod { \mathbf { Z } } } ,
$$

and then substitute $s = k + t + 2 m n$ . This yields

$$
a _ { n } { = } \sum _ { k = 0 } ^ { 2 m - 1 } \int _ { k + 2 m n } ^ { k + 1 + 2 m n } \exp ( 2 \pi i s ^ { 2 } / 4 m ) d s
$$

Now sum over n, so as to obtain the formula

$$
\begin{array} { r } { G ( L ) { = } \displaystyle \sum a _ { n } { = } \intop _ { - \infty } ^ { \infty } \exp ( \pi i s ^ { 2 } / 2 m ) d s , } \end{array}
$$

where the improper integral is well defined by Lemma 2. In fact, substituting $\scriptstyle { u = s / \sqrt { 2 m } } .$ ,it follows that $G ( L ) = G ( \langle 2 m \rangle )$ is equal to

Thus the ratio

$$
G ( \langle 2 m \rangle ) / \sqrt { 2 m } = \intop _ { - \infty } ^ { \infty } \exp ( \pi i u ^ { 2 } ) d u
$$

is independent of m. To evaluate this integral, we simply evaluate the Gauss sum for the case $m = 1$ ,obtaining the identity

$$
G ( \langle 2 m \rangle ) / \sqrt { 2 m } = ( 1 + i ) / \sqrt { 2 } = \exp ( 2 \pi i / 8 ) .
$$

Similarly $G ( \langle - 2 m \rangle ) / \sqrt { 2 m }$ is equal to the complex conjugate $\exp ( - 2 \pi i / 8 )$ .Thus we have shown that the invariant $G ( L ) / \sqrt { d ( L ) }$ is equal to $\exp ( 2 \pi i \sigma / 8 )$ for every 1-dimensional lattice $L$ The corresponding formula for an orthogonal sum of 1-dimensional lattices, and hence for an arbitrary lattice, now follows immediately. This completes the proof of Milgram's theorem.0

The formula of Braun can be recovered from that of Milgram as follows. Let $L$ be any lattice in a rational inner product space, subject only to the hypothesis that $x \cdot y \in \mathbf { Z }$ for $x , y \in L .$ As before we set $d =$ |determinant $\dagger { > } 0$ and $\scriptstyle n = r k ( L )$

Corollary. If $q$ is $^ { a }$ multiple of $2 d ,$ then

$$
\sum _ { x \in L / q L } \exp ( \pi i x \cdot x / q ) { = } q ^ { n / 2 } { \sqrt { d } } \exp ( 2 \pi i \sigma / 8 ) .
$$

Evidently the formula quoted at the beginning of this Appendix is an immediate consequence, taking $q = a / 2$

Proof of the corollary. Consider the new inner product qx · y on the lattice $L ^ { \# }$ . Note that $L ^ { \# }$ , with this new inner product, is of type II,and has dual lattice equal to $q ^ { - 1 } L$ .Applying Milgram's theorem we obtain

$$
\sum _ { \boldsymbol { u } \in \boldsymbol { q } ^ { - 1 } L / L ^ { \sharp } } \exp ( \pi i \boldsymbol { q } \boldsymbol { u } \cdot \boldsymbol { u } ) = \sqrt { \boldsymbol { q } ^ { n } / d } \exp ( 2 \pi i \sigma / 8 ) .
$$

Now substitute $u = q ^ { - 1 } x$ and multiply both sides of this equation by $d .$ The left hand side becomes

$$
- \underset { x \in L / q L ^ { * } } { \sum } \exp ( \pi i x \cdot x \cdot x / q ) { = \underset { x \in L / q L } { \sum } } \exp ( \pi i x \cdot x \cdot x / q ) ,
$$

since qL contains $q L$ as a subgroup of index d. This completes the proof.□

Knebusch points out that Milgram's formula is closely related to a version of the quadratic reciprocity law due to [Weil, 1964]. Given Las above, let $( L ^ { \# } / L ) _ { p }$ denote the $p$ -primary component of the finite abelian group $L ^ { \# } / L$ Then $L ^ { \# } / L$ decomposes as the orthogonal sum of the various $( L ^ { \# } / L ) _ { p }$ ，hence the Gauss sum $G ( L )$ can be expressed correspondingly as a product $\prod G \big ( ( L ^ { \# } / L ) _ { p } \big ) .$ ，where all but finitely many of the factors are equal to 1. Similarly the order $d$ of $L ^ { \# } / L$ splits as the product of its $p$ primary components $d _ { p }$

Lemma 3. The ratio $\gamma _ { p } ( L ) { = } G \left( ( L ^ { \# } / L ) _ { p } \right) / \sqrt { d _ { p } }$ depends only on the $p$ -adic completion $\mathbf { Q } _ { p } \otimes L$ of the inner product space $\mathbf { Q } \otimes L$ ，The correspondence $\mathbf { Q } _ { p } \otimes L \mapsto \boldsymbol { \gamma } _ { p } ( L )$ gives rise to $^ { a }$ homomorphism from the finite additive group $W ( \mathbf { Q } _ { p } )$ to the multiplicative group of roots of unity in C.

Briefly we say that $\gamma _ { p }$ is a character of the Witt group $W ( \mathbf { Q } _ { p } )$ The proof of the first statement is completely analogous to the proof of Lemma 1. One simply uses the $p$ -adic integers $\mathbf { Z } _ { p }$ and the $p$ -adic field $\mathbf { Q } _ { p }$ in place of $\mathbf { Z }$ and Q. To prove the second statement, suppose that the completion $\mathbf { Q } _ { p } \otimes L$ is a split inner product space. Then this completion has innerproduct matrix $\binom { 0 } { I } \binom { I } { 0 }$ with respect to a suitable basis, and this basis spans a $\underline { { \boldsymbol { Z } } } _ { p }$ -lattice which is self-dual. But the existence of such a self-duai lattice implies that $\gamma _ { p } ( L ) = 1$ Since the function $\gamma _ { p }$ is clearly multiplicative with respect to orthogonal sums, this proves the lemma.0

Let us define $\gamma _ { \infty } ( L )$ to be the root of unity exp $( - 2 \pi i \sigma / 8 )$ . Evidently this depends only on the real completion $\mathbf { R } \otimes L$ of the inner product space $\mathbf { Q } \otimes L$

Weil reciprocity theorem. For any lattice $L$ ,the product $\prod _ { p \leq \infty } \gamma _ { p } ( \mathbf { Q } \otimes L )$ is equal to 1. 1

Proof.This follows immediately from Milgram's theorem.0

Let us see what this reciprocity formula means in the rank 1 case. Suppose then that the lattice $L$ is spanned by a single vector $l _ { 1 }$ . Suppose also, to fix our ideas, that $l _ { 1 } \cdot l _ { 1 } = 4 m$ with m odd. We will write briefly $L = \left. 4 m \right.$ ：

Lemma 4. The character $\gamma _ { 2 } \left. 4 m \right.$ is equal to exp(2π i m/8).

In fact $L ^ { \# } / L$ is cyclic of order |4ml, generated by $l _ { 1 } / 4 m$ Hence the 2-primary component $\left( L ^ { \# } / L \right) _ { 2 }$ is cyclic of order 4, generated by $l _ { 1 } / 4 ,$ with $\varphi ( l _ { 1 } / 4 ) \equiv m / 8 ( \mathrm { m o d } \mathrm { \bf Z } )$ . It follows easily that

$$
\gamma _ { 2 } \langle 4 m \rangle { = } \sum _ { j = 1 } ^ { 4 } \exp ( 2 \pi i j ^ { 2 } m / 8 ) / \sqrt { 4 }
$$

Next suppose that m is an odd prime p.

Lemma 5. The character vp<4p>is equal to exp(2π i(1-p)/8).

Proof. This follows from Lemma 4， by solving the reciprocity equation

$$
\gamma _ { 2 } \langle 4 p \rangle \gamma _ { p } \langle 4 p \rangle \gamma _ { \infty } \langle 4 p \rangle = 1 . \quad \mathbb { I }
$$

More generally suppose that $m = p u _ { \mathrm { { } } }$ where $u$ is relatively prime to $p$

$$
\overline { { { \bf { L e m m a 6 . 7 } h e ~ c h a r a c t e r } \gamma _ { p } \langle 4 p u \rangle \ i s \ e q u a l \ t o \left( \frac { u } { p } \right) \gamma _ { p } \langle 4 p \rangle . } }
$$

Here the Legendre symbol (u/p) is defined to be either +1 or -1 according as u is or is not a quadratic residue modulo $p$

Proof. Proceeding as above, the $p$ -primary component $( L ^ { \# } / L ) _ { p }$ is spanned by a vector l/p with φ(l/p)=2u/p(mod Z). Hence

$$
\gamma _ { p } \langle 4 p u \rangle { = } \sum _ { j = 1 } ^ { p } \exp \bigl ( 2 \pi i ( 2 u j ^ { 2 } / p ) \bigr ) .
$$

If (u/p)= +1,then evidently the expression uj² varies over all quadratic residues modulo p, taking each non-zero value twice, and taking the value zero modulo $p$ just once. On the other hand if $( u / p ) = - 1$ then $u j ^ { 2 }$ takes each non-residue value twice, again taking the zero value once. Since the sum of $\exp \bigl ( 2 \pi i ( 2 k / p ) \bigr )$ over all residue classes $k$ modulo $p$ is zero, the conclusion follows easily.(Compare [Lang, p.85].）□

Now let p and $q$ be distinct odd primes.Applying the reciprocity formula $\gamma _ { 2 } ( L ) \gamma _ { p } ( L ) \gamma _ { q } ( L ) \gamma _ { \infty } ( L )$

to the lattice $L = \langle 4 p q \rangle$ we obtain the identity

$$
\left( \frac { p } { q } \right) \left( \frac { q } { p } \right) \exp \left( 2 \pi i ( p - 1 ) ( q - 1 ) / 8 \right) = 1 .
$$

This is just the classical quadratic reciprocity law.

Concluding remark. There is an analogous Weil reciprocity formula over an arbitrary number field, which can be derived from the rational reciprocity formula. (Compare [Scharlau, 1972] and [KnebuschScharlau,1971].) It takes the form

$$
\prod _ { v } \gamma _ { v } ( X ) = 1 ,
$$

where X is an inner product space over the number field $F _ { : }$ and $\boldsymbol { v }$ ranges over all valuations of $F .$ Here $\gamma _ { v }$ is defined as follows.

Case 1. If $\boldsymbol { v }$ is a complex archimedian valuation, then $\gamma _ { v } ( X ) = 1 .$

Case 2. If $v$ is a real archimedian valuation, then

$$
\gamma _ { v } ( X ) { = } \exp \bigl ( { - } 2 \pi i \sigma _ { v } ( X ) / 8 \bigr )
$$

where $\sigma _ { v } ( X )$ is the associated signature.

Case 3. If $\boldsymbol { v }$ is the p-adic valuation, where p is a prime ideal in the ring of integers $\pmb { D }$ ,then $\mathcal { Y } _ { v } ( X )$ is defined as the ratio

$$
\cal G ( ( L ^ { \pm } / L ) _ { p } ) / \sqrt { | ( L ^ { \pm } / L ) _ { p } | } .
$$

Here $L$ can be any $D$ -lattice in $X$ satisfying $\scriptstyle { \frac { 1 } { 2 } } l \cdot l \in D$ for $l \in L ,$ and $L ^ { \# }$ is the dual lattice with respect to the $\mathbf { Q }$ -valued inner product

$$
x , y \mapsto \mathrm { t r a c e } _ { F / \mathbf { Q } } x \cdot y .
$$

The Gauss sum $G \left( ( L ^ { \# } / L ) _ { \mathfrak { p } } \right)$ is defined as the sum of $\mathrm { e x p } \big ( \pi i \mathrm { t r a c e } ( u \cdot u ) \big )$ over all $_ { \pmb { u } }$ in $( L ^ { \# } / L ) _ { \mathfrak { p } }$ ：

Now the reciprocity law Iv,(X)=1 follows easily from Milgram's formula,applied to the inner product trace(x·y) on L.

One special case of this reciprocity law is of particular interest.

$$
\begin{array} { r } { X = ( \langle \alpha \rangle \oplus \langle - 1 \rangle ) \otimes ( \langle \beta \rangle \oplus \langle - 1 \rangle ) , } \end{array}
$$

representing an element in the ideal $I ^ { 2 } ( F )$ in the Witt ring. Then it is easily verified that $\overline { { \gamma _ { v } ( X ) = \pm 1 } }$ If $F _ { v } \notin \mathbf { C } ,$ then both Weil and Scharlau show that $\gamma _ { v } ( X ) = - 1$ for suitably chosen $\pmb { \alpha }$ and $\beta$ The correspondence

![](images/b3306b9a6a7cb78aba570ebbbfc48a684d5683576f44c8e46fdacad743251a2e.jpg)

# Appendix 5. The Leech Lattice, and Other Lattices in Dimension 24

We will construct a self-dual unimodular lattice $L { \bf { \subset } } { \bf { R } } ^ { 2 4 }$ with the property that $x \cdot x \geq 4$ for every $x \neq 0$ in $L$ (Compare Chapter II, \$\$ 6, 7.)

The construction begins with the following combinatorial statement. Let $\mathbf { F } _ { 2 } ^ { 2 4 }$ denote the vector space over $\mathbf { F } _ { 2 }$ consisting of all 24-tuples of integers modulo 2.

Lemma. There exists a 12-dimensional subspace $\overline { { S } } { \subset } { \bf { F } } _ { 2 } ^ { 2 4 }$ with the following property. For every non-zero vector $\boldsymbol { s } = ( s _ { 1 } , \ldots , s _ { 2 4 } )$ in S,the number of components s: which are equal to one is at least 8,and is divisible by 4.Furthermore S contains the vector $( 1 , \ldots , 1 )$ consisting of 24 ones.

Proof.Following Leech,we will display $s$ as the row space of an explicit $1 2 \times 2 4$ matrix.Let A denote the symmetric 11×11 matrix over $\mathbf { F } _ { 2 }$ whose first row is

and whose remaining rows are obtained by permuting these entries cyclically to the left. Thus each row of $A$ contains 6 ones. Patient inspection shows that

(i) each pair of distinct rows of $A$ has precisely 3 ones in common (i.e., in the same column).

Let $B$ denote the symmetric $1 2 \times 1 2$ matrix which is formed from $A$ byadjoining the first row011111111111 and a corresponding first column. Using (i) we easily verify the following.

![](images/dc7dd4f2e3ce038a86cdadf255121d2000a5d45df52f97ce0ae8534ee68dec15.jpg)

(ii) The matrix $B$ satisfies the identity $B ^ { 2 } = B B ^ { t } = I .$ Hence $B$ is nonsingular, and any two rows of $B$ are orthogonal with respect to the inner product $\boldsymbol { r } \cdot \boldsymbol { r ^ { \prime } } = \sum \boldsymbol { r } _ { i } \boldsymbol { r } _ { i } ^ { \prime }$

![](images/0fa5bfe46ba81539e71bdee1aee8bd016cf10730afebffc98e9ecf158fa9cb6d.jpg)

is now the required $1 2 \times 2 4$ matrix of rank 12. Evidently the sum of all of the rows of $C$ is equal to the 24-tuple $( 1 , 1 , \ldots , 1 )$ .Note that

(iii) The number of ones in any row of $C$ is either 8or 12.Furthermore any two distinct rows of $C$ are orthogonal.

It will be convenient to use the notation $\| s \|$ for the number of ones in a 24-tuple $s = ( s _ { 1 } , \ldots , s _ { 2 4 } )$ . As a corollary of (ii) we obtain the following statement.

(iv) If s is a linear combination of the rows of C,then |/sll=0 (mod 4).

This is proved by induction on the number of rows involved. If $\overline { s } ^ { \prime }$ is obtained from $\overline { s }$ by adding a row $r _ { \mathrm { { ; } } }$ ,then evidently

$$
\left\| s ^ { \prime } \right\| = \left\| s \right\| + \left\| r \right\| - 2 n
$$

where n denotes the number of ones which $\pmb { S }$ and $r$ have in common. But s and r are orthogonal by (ii), so n is even. Assuming inductively that |/sl is divisible by 4, it follows that $\| s ^ { \prime } \|$ is divisible by 4 also. (v) If s is a non-zero linear combination of the rows of C,then |/sll ≥8.

Proof. By (iv), it suffices to prove that $\| s \| \geq 5$ .Suppose that $s$ is the sum of $k$ distinct rows of $C$ The case $k = 1$ is covered by (ii). If $k = 2$ then it follows easily from (i) that $\| s \| = 8$ .If $k = 3$ and if $s$ is the sum of the first row of $C$ and two other rows, then again it follows from (i) that $\| s \| = 8$ If $s$ is the sum of three rows of $C$ not including the first row, then evidently the first thirteen entries of s include precisely 4 ones.If the remaining eleven entries were all zero, this would mean that the sum of the three corresponding rows of A was zero. Hence the sum of the remaining eight rows of A would also be zero; and the sum of the corresponding eight rows of $\overline { B }$ would be zero, contradicting (ii). Therefore $\left\| s \right\| \geq 5$ ，

Finally, if $k \geq 4$ ，then the first twelve entries of s contain at least 4 ones,and the remaining entries contain at least 1 one by (i), so again it follows that $\| s \| \geq 5$ .This proves (v),and completes the proof of the Lemma.□

Remark 1. The matrix C was constructed in a rather ad hoc manner. The following description of its row space S may seem a little more motivated.Consider the field $\mathbf { F } _ { 2 0 4 8 }$ with $2 ^ { 1 1 }$ elements. We claim that S can be identified with the collection of all “relations”between the $2 3 ^ { \mathrm { r d } }$ roots of unity in $\mathbf { F } _ { 2 0 4 8 }$ .Let $\omega$ denote a $2 3 ^ { \mathrm { r d } }$ root of unity satisfying the irreducible equation

$$
1 + \omega + \omega ^ { 5 } + \omega ^ { 6 } + \omega ^ { 7 } + \omega ^ { 9 } + \omega ^ { 1 1 } = 0
$$

over $\mathbf { F } _ { 2 }$ , and let $\overline { { \varphi } }$ denote the Frobenius automorphism $| \alpha | \to \alpha ^ { 2 }$ .Then

![](images/c118034be69f7dfaef43fc91389012419a9c270cc888af933c924d52f25c5065.jpg)

the number of $t _ { i }$ congruent to 2 modulo 4 is divisible by 4.If the $t _ { i }$ are odd, then $t _ { i } ^ { 2 }$ is congruent to 1 or 9 modulo 16 according as $t _ { i }$ is congruent to $\pm 1$ or $\pm 3$ modulo 8.Thus

$$
\sum t _ { i } ^ { 2 } \equiv \alpha _ { 1 } + 9 \alpha _ { 3 } + 9 \alpha _ { 5 } + \alpha _ { 7 } ( \mathrm { m o d } 1 6 ) ,
$$

where $\alpha _ { j }$ denotes the number of $t _ { i }$ which are congruent to $j$ modulo 8. Note the congruences

$$
\begin{array} { r l } { \alpha _ { 1 } + \alpha _ { 3 } + \alpha _ { 5 } + \alpha _ { 7 } = 2 4 \equiv 0 } & { { } { \pmod { 8 } } , } \\ { \alpha _ { 1 } + 3 \alpha _ { 3 } + 5 \alpha _ { 5 } + 7 \alpha _ { 7 } \equiv 4 } & { { } { \pmod { 8 } } , } \\ { \alpha _ { 1 } } & { { } { \pmod { 4 } } , } \end{array}
$$

where the last two follow from (vii) and the lemma. Adding the first two congruences and subtracting twice the third, we obtain

$$
4 \alpha _ { 3 } + 4 \alpha _ { 5 } \equiv 4 { \pmod { 8 } } .
$$

Thus $a _ { 3 } + a _ { 5 }$ is odd,and itfollows that $\sum t _ { i } ^ { 2 } \equiv 2 4 + 8 ( \alpha _ { 3 } + \alpha _ { 5 } ) \equiv 0 ( \mathrm { m o d } 1 6 ) .$

For any $_ x$ and $y$ in $\overline { { L } }$ ,it follows that

$$
x \cdot y = { \frac { 1 } { 2 } } { \big ( } ( x + y ) \cdot ( x + y ) - x \cdot x - y \cdot y { \big ) } \in \mathbf { Z } .
$$

Thus the lattice $L$ is self-dual.

Note that no element $\overline { { x \in L } }$ can satisfy ${ \overline { { x \cdot x } } } = 2$ For if $t _ { 1 } ^ { 2 } + \cdots + t _ { 2 4 } ^ { 2 } = 1 6$ then the $\overline { { t _ { i } } }$ certainly cannot all be odd. But the only expressions for 16 as a sum of even squares are

$$
1 6 { = } 4 ^ { 2 } { = } 2 ^ { 2 } + 2 ^ { 2 } + 2 ^ { 2 } + 2 ^ { 2 } ,
$$

and both possibilities are excluded by (vi) and the lemma. Therefore $x \cdot x \geq 4$ for every $x \neq 0$

For further information about the Leech lattice,the reader is referred to [Conway].

Concluding remark. A complete classification of unimodular lattices of type II in $\mathbf { R } ^ { 2 4 }$ has been given by [Niemeier].He shows that there are precisely 24 such lattices L up to isomorphism; and that a complete invariant for Lis provided by the finite subset ${ \cal R } ( L )$ consisting of all vectors $x \in L$ with norm $x \cdot x$ equal to 2.Evidently,for any $x _ { 0 } { \in } R ( L )$ the reflection

$$
y \mapsto y - ( x _ { 0 } \cdot y ) x _ { 0 }
$$

in the hyperplane perpendicular to $x _ { 0 }$ maps $L$ to itself, and hence maps $R ( L )$ to itself.Therefore $R ( L )$ is a“root system”,as described in [Bourbaki, v.34, pp.142-197], in some euclidean space. Note that the angle between any two vectors in $R ( L )$ is either 0°,60°,90°,120°,0r 180° Using the classification theorem for root systems,we see that $R ( L )$ is a disjoint union of mutually perpendicular root systems, each of which can be described by a“Dynkin diagram”of one of the following three types.In each case, each vertex of the Dynkin diagram represents a basis vector of norm $x \cdot x { } = 2$ in an m-dimensional lattice, and two such basis vectors have inner product either -1 or O according as they are joined by a line segment or not. The associated root system consists of all vectors of norm 2 in the lattice $\bar { L }$ spanned by these basis vectors.

Type $A _ { m } ( m \geq 1 )$ . In this case the Dynkin diagram consists of m vertices joined by $m - 1$ line segments as follows.

![](images/06057b1b6a9afe470d8923b32f62bb5574dea6cff4ba83550586427dd77a3fe6.jpg)

In terms of auxilliary orthonormal vectors $e _ { 1 } , \ldots , e _ { m + 1 }$ ,the $i$ -th vertex in this diagram can be identified with the diference vector $e _ { i } - e _ { i + 1 }$ ： Thus the lattice $\bar { L }$ can be identified with the lattice consisting of all $( m + 1 )$ -tuples of integers with sum zero. The determinant of $\bar { L }$ is equal $_ { \textrm t o m + 1 }$

（2014号 $\overline { { { T y p e } ~ { D _ { m } ( m \geq 4 ) } } }$ . In this case the m vertices are connected as follows.

![](images/4b2836326ec357e7f3adb6c3cec128332cce22428024d2aab94862cefaba9685.jpg)

In terms of orthonormal vectors $e _ { 1 } , \ldots , e _ { m }$ ， the m vertices can be identified with the vectors $e _ { i } - e _ { i + 1 }$ and $e _ { m - 1 } + e _ { m }$ The lattice $\bar { L }$ can be identified with the lattice consisting of all m-tuples of integers with even sum. Its determinant is equal to 4.

Type $E _ { m } ( m = 6 , 7 , 8 )$ . In these three exceptional cases the m vertices are connected as follows; and the determinant of $\bar { L }$ is equal to $9 - m$

![](images/f37fbd466ef019b0fc24db3c93f1e94963488840005651981f5a20b39c1752a2.jpg)

Compare the discussion in Chapter I1, \$ 7.

Niemeier gives an explicit list of the 24 distinct root systems which arise from unimodular lattices of type $\mathrm { I I }$ in $\mathbf { R } ^ { 2 4 }$ . In general the root system $R ( L )$ spansa sub-lattice $\bar { L }$ which has finite index in $L$ .The Leech lattice, with $\bar { L } { = } 0$ ,is the only exception to this. In general the lattice $\bar { L }$ has determinant greater than 1,and hence is a proper sub-lattice of $L .$ Again there is just one exception, namely the lattice $\scriptstyle { \bar { L } } = L = { \Gamma _ { 8 } } \oplus { \Gamma _ { 8 } } \oplus { \Gamma _ { 8 } }$ with root system $R ( L )$ equal to $E _ { 8 } \cup E _ { 8 } \cup E _ { 8 }$ .Note that $\bar { L }$ may be (and usually is) decomposable, even when the unimodular lattice $L$ isindecomposable.

# Chronological Table

![](images/198c1219d755004ad25b851339d080583c0090bae30d035a958236a69bb6eabe.jpg)

![](images/a60321cc597f9c3f76a39c625a498c42245f1227e1778b964162653c4e1a1859.jpg)

Arason,J.K., Pfister,A.:Beweis_desKrullschen Durchschnitsatzes fur den Witring. Invent.Math.12,173-176 (1971). Arf,C.:Untersuchungen über quadratische Formen in Korpern der Characteristic 2. J.ReineAngew.Math.183,148-167(1941).(Compareibid.193,121-125 (1954).) Artin,E.: Geometric algebra. Interscience 1957. Bass,H.:Lectures on topics in algebraic $\pmb { K }$ -theory.Bombay:Tata Institute 1967. Birkhoff, G.,MacLane,S.:A survey of modern algebra.MacMillan 1941.   
Blichfeldt, H.F.: The minimum values of quadratic forms in six,seven, and eight variables. Math. Z.39,1-15 (1935).   
VBlij,F.van der: An invariant of quadratic forms mod 8.Indag. Math.21,291-293 (1959). Borevich,Z.I.,Shafarevich,I.R.: Number theory.Academic Press 1966. Bourbaki, N.:Eléments 24 (Algebre 9), Formes sesquilineaires et formes quadratiques. Hermann 1959. Bourbaki, N.: Eléments 34, Groupes et algebres de Lie 4-6.Hermann 1968. Braun,H.: Geschlechter quadratischer Formen. J. Reine Angew. Math. 182, 32-49 (1940). Cartan,H., Eilenberg, S.: Homological algebra. Princeton University Press 1956. Chevally, C.: The algebraic theory of Spinors. Columbia University Press 1954. Conway,J.H.:A group of order 8,315,553,613,086,720,000. Bull.Lond.Math.Soc.1, 79-88 (1969). Conway, J.H.: A characterization of Leech's lattice. Invent. Math.7,137-142 (1969). Conway,J.H.:Groups, lattces,and quadratic forms, pp.135-139 of “Computers in Algebra and Number Theory", SIAM-AMS Proceedings 4,AMS 1971. Dickson,L.E.: History of the Theory of Numbers,2and 3,New York: G.E.Stechart & Co 1934. Dyson,F.J.: Quaternion determinants. Helv.Phys.Acta 45,289-302 (1972). Frohlich,A.: Discriminants of algebraic number fields.Math. Z. 74, 18-28 (1960). (See also: Ideals in an extension field .., p. 29-38.) Frohlich,A.: Hermitian and quadratic forms over rings with involution. Quart. J. Math. Oxford 20,297-317 (1969). Frohlich,A.: On the K-theory of unimodular forms over rings of algebraic integers. Quart. J. Math. Oxford, to appear. Frohlich, A., McEvett: Forms over rings with involution. J. Algebra 12, $7 9 { \scriptstyle - 1 0 4 }$ (1969). Gelfand, 1.M., Mischchenko,A.S.: Quadratic forms over commutative group rings and the $\kappa$ -theory.Functional Analysis and its Applications 3,277-281 (1969). Geyer,W.-D.,Harder, G., Knebusch, M., Scharlau, W.: Ein Residuensatz fur symmetrische Bilinearformen.Invent.Math.11,319-328 (1970). Hilbert,D., Cohn-Vossen,S.: Geometry and the imagination. Chelsea 1952. Hirzebruch,F.: Topological methods in algebraic geometry. Springer 1966. Jacobson,N.: A note on hermitian forms. Bull Amer. Math. Soc.46,264-268 (1940). Knebusch, M.: Grothendieck und Wittringe von nichtausgearteten symmetrischen Bilinearformen,Sitzungsber. Heidelb. Akad. Wiss. Math.-naturw.Kl. 1969/70,3.Abh.

![](images/bf00febbf131dacb63b9e704bb5231d3b12ab98352ae726d324c3ba5b7386c4a.jpg)

# References

![](images/5b53e245e7b76d64915d89a91612821bc7f96fd6b07a96e9e1ce59cba337b225.jpg)

![](images/39450f8e6467a9398d59ac9c5a3e57f2e9968a80a2235f1e9634ee1db6f85ac3.jpg)

# Index

![](images/c31e8c1046589535c81c80a2a83f283cc25ec8ad8dd3b4f9c41c612ed578afba.jpg)

![](images/5b27207eb9cd025396cc2b8f1c86f304993856913be5973c2e9dddd79e5f0eac.jpg)

# Special Notations

![](images/aec710d6c419bdc0f6b7ab51bb051d0f9fa00b9bc8e2dc32c30408a1f2170ea6.jpg)

![](images/c5820a08bfa9e21868cc3783eb61ca735e14ad094b33e3911d624bfe72285da2.jpg)

# Ergebnisse der Mathematik und ihrer Grenzgebiete

1. Bachmann: Transfinite Zahlen. DM 48,-; US \$15.30   
2. Miranda: Partial Differential Equations of Eliptic Type. DM 58,-; US \$18.40   
4.Samuel: Methodes d'Algebre Abstraiteen Geometrie Algebrique.DM 34,-;US \$10.80   
5.Dieudonne:La Geometrie des Groupes Classiques.DM42 ;US \$13.40   
7. Ostmann: Additive Zahlentheorie. i.Teil: Allgemeine Untersuchungen. DM 42,一; US \$13.40   
8. Wittich: Neuere Untersuchungen über eindeutige analytische Funktionen. DM 36,一; US \$13.40   
11. Ostmann: Additive Zahlentheorie. 2.Teil: Spezielle Zahlenmengen. DM 34,一; US \$10.80   
13.Segre: Some Properties of Diffrentiable Varieties and Transformations. DM 46,-; US \$14.60   
14. Coxeter/Moser: Generators and Relations for Discrete Groups. DM 42,-; US \$13.40   
15.Zeller/Beckmann: Theorie der Limitierungsverfahren. DM 64,-; US \$20.30   
16. Cesari: Asymptotic Behavior and Stability Problems in Ordinary Differential Equations.DM $s 4 , -$ ;US \$17.20   
17. Severi:Iltheoremadi Riemann-Roch percurve - superficieevarieta questionicollegate. DM 30,-;US \$9.60   
18. Jenkins: Univalent Functions and Conformal Mapping. DM 37,-; US \$11.80   
19.Boas/Buck: Polynomial Expansions of Analytic Functions. DM 24,-;US \$7.70   
20.Bruck: A Survey of Binary Systems.DM 46,-; US \$14.60   
21. Day: Normed Linear Spaces. In preparation   
23.Bergmann: Integral Operators in the Theory of Linear Partial Differential Equations. DM 40 $\bar { \bullet }$ ;US \$12.70   
25. Sikorski: Boolean Algebras. DM 42. ; US \$13.40   
26. Kinzi: Quasikonforme Abbildungen.DM 43,-;US \$13.70   
27. Schatten: Norm Ideals of Completely Continuous Operators.DM 30,-;US \$9.60   
28.Noshiro:Cluster Sets.DM40 ;US \$12.70   
30.Beckenbach/Bellman: Inequalities.DM38,-; US \$12.10   
31. Wolfowitz: Coding Theorems of Information Theory.DM 30,-; US \$9.60   
32. Constantinescu/Cornea: Ideale Ränder Riemannscher Flachen.DM 75,-; US \$23.80   
33. Conner/Floyd: Diffrentiable Periodic Maps. DM34,-; US \$10.80   
34.Mumford: Geometric Invariant Theory.DM 24,-; US \$7.70   
35.Gabriel/Zisman: Calculus of Fractions and Homotopy Theory.DM42,-; US \$13.40   
36.Putnam: Commutation Properties of Hilbert Space Operators and Related Topics. DM 31,-; US \$9.90   
37. Neumann: Varieties of Groups. DM 51,-; US \$16.20   
38.Boas: Integrability Theorems for Trigonometric Transforms. DM 20,-;US \$6.20   
39.Sz.-Nagy: Spektraldarstellung linearer Transformationen des Hilbertschen Raumes. DM 24,-;US \$7.70   
40.Seligman: Modular Lie Algebras.DM43,-; US \$13.70   
41.Deuring: Algebren.DM30,-;US \$9.60   
42.Schute:Volstandige Systeme modaler und intuitionistischer Logik.DM30-; US \$9.60   
43.Smullyan: First-Order Logic. DM36,-; US \$11.50   
44.Dembowski: Finite Geometries.DM 68,-; US \$21.60   
45.Linnik: Ergodic Properties of Algebraic Fields.DM 44,-; US \$14.00   
46. Krull: Idealtheorie. DM34,-; US \$10.80   
47. Nachbin: Topology on Spaces of Holomorphic Mappings. DM 18,-; US \$5.80   
48.A.Ionescu Tulcea/C.Ionescu Tulcea: Topics in the Theory of Lifting. DM 36,一; US \$11.50   
49.Hayes/Pauc: Derivation and Martingales.DM 48,-;US \$15.30   
50.Kahane: Series de Fourier absolument convergentes. DM 44,-; US \$14.00   
51.Behnke/Thullen: Theorie der Funktionen mehrerer komplexer Veränderlichen. DM 48,-; US \$15.30   
52.Wilf: Finite Sections of Some Classical Inequalities.DM 28,-;US \$8.90

![](images/5ca937bb359c457998c43302f89efb24ea4846afefb741b21976d757395354d0.jpg)