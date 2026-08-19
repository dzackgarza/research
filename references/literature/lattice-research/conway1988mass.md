Low-dimensional lattices. IV. The mass formula

BY J.H.CoNWA $\mathbf { Y } ^ { 1 }$ ,F.R.S., AND N.J.A. SLOANE²

$\mathbf { 1 }$ Mathematics Department, Princeton University, Princeton, New Jersey 08540, U.S.A. ${ \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi } } _ { \bf { \psi \psi } } _ { \bf { \psi \psi } } _ { \bf { \psi \psi } } _ { \bf { \psi \psi } } _ { \bf { \psi \psi } } _ { \bf { \psi \psi } } _ { \bf { \psi \psi } } _ { \bf { \psi \psi } } _ { \bf { \psi \psi } } _ { \bf { \psi \psi } } _ { \bf { \psi \psi } } _  \bf { \psi \psi \psi } _ { \bf \psi } _ { \bf { \psi \psi \psi } } _ { \bf { \psi \psi \psi } } _ _ { \bf { \psi \psi \psi } } _ _ { \bf { \psi \psi \psi } } _ _  \bf { \psi \psi \psi } _ { \bf \psi } _ { \bf \psi \psi } _ { \psi \psi } _ { \bf \psi } _ { \bf \psi } _ { \psi \psi \psi } _ { \bf \psi \psi } _ { \psi \psi \psi } _ _ { \psi \psi \psi \psi } _ { \psi \psi \psi } _  \psi \psi \psi \psi \psi _ { \psi \psi \psi } _ { \psi \psi \psi } _ { \psi \psi \psi \psi } _ { \psi \psi \psi \psi \psi } _  \psi \psi \psi \psi \psi { \psi \psi \psi } _ { \psi \psi \psi \psi \psi } _  \psi \psi \psi \psi \psi \psi { \psi \psi \psi \psi \psi } \psi _ { \psi \psi \psi \psi \psi \psi }  \psi \psi \psi \psi $ Mathematical Sciences Research Center，AT&T Bell Laboratories, Murray Hill, New Jersey O7974, U.S.A.

(Received 6 April 1988)

The mass formula expresses the sum of the reciprocals of the group orders of the lattices in a genus in terms of the properties of any of them. We restate the formula so as to make it easier to compute.In particular we give a simple and reliable way to evaluate the 2-adic contribution. Our version,unlike earlier ones,is visibly invariant under scale changes and dualizing.We use the formula to check the enumeration of lattices of determinant $d \leqslant 2 5$ given in the first paper in this series.We also give tables of the‘standard mass', the $L$ -series $\Sigma \left( n / m \right) m ^ { - s }$ (m odd), and genera of lattices of determinant $d \leqslant 2 5$ ：

# 1.INTRODUCTION

The‘mass formula’gives the sum of the reciprocals of the group orders of all inequivalent quadratic forms in a genus.More precisely, $\operatorname { l e t } f$ be an $\mathbfcal { n }$ -dimensional positive definite integral quadratic form (or lattice),and le $\mathfrak { d } ^ { ( 1 ) } = f , \ldots , f ^ { ( h ) }$ be the integrally inequivalent forms in the genus of $f$ .The mass of this genus is defined to be

$$
m ( f ) = \sum _ { i = 1 } ^ { h } { \frac { 1 } { \left| \mathrm { A u t } \left( f ^ { ( i ) } \right) \right| } } ,
$$

where Aut $( f ^ { ( i ) } )$ is the automorphism group of $\cdot f ^ { ( i ) }$ $\boldsymbol { h }$ is called the class number).The mass formula expresses $m ( f )$ in terms of properties of $f$ alone.

In this paper, the fourth of a series dealing with low-dimensional lattices (see Conway $\&$ Sloane $\mathbf { r } 9 8 8 b  – d )$ we give a version of the mass formula (see (2)) which we believe is easier to evaluate than previous versions.

A brief description of the history of the mass formula appears in $\ S 2$ H. J. S. Smith's important 1867 contribution is usually overlooked.Published versions of the formula have often been incorrect (see $\ S 3 \ r ,$ .We pay particular attention to the 2-adic contribution to the mass,which is notoriously prone to error.

The formula is described in $\ S \ S 4 \mathbf { - 6 }$ .It is expressed in terms of what we call the $p$ -masses $m _ { p } ( f )$ of the lattice or form (see (3)),where $p$ is any prime,rather than in terms of the usual $p$ -adic densities $\alpha _ { p } ( f )$ . The $p$ -mass $m _ { p } ( f )$ appears as the product of the diagonal factors $M _ { p } ( f _ { q } )$ , the cross terms and the type factor.

The calculation of the diagonal factors,made routine by the use of tables 1 and 2, is described in $\ S 5$ .The mass is found as a simple rational multiple of the standard mass, defined in $\ S 7$ (see table 3).For a form of determinant $d$ and even dimension ${ \boldsymbol { n } } = 2 s$ the standard mass involves the $L$ -series

$$
\zeta _ { D } ( s ) = \sum _ { m = 1 , 3 , 5 , . . . } \biggl ( \frac { D } { m } \biggr ) \frac { 1 } { m ^ { s } } ,
$$

where $D = ( - 1 ) ^ { s } d$ and $( D / m )$ is a Jacobi symbol. Table 6 gives $\zeta _ { D } ( s )$ for $d \leqslant 2 5$ ， $s \leqslant 1 2$ .This table provides an extensive generalization of such familiar identities as

$$
\mathbf { 1 } - { \frac { 1 } { 5 } } + { \frac { 1 } { 7 } } - { \frac { 1 } { 1 1 } } + { \frac { 1 } { 1 3 } } - \ldots = { \frac { \pi } { 2 \sqrt { 3 } } }
$$

(the case $d = 3 , s = 1 , D = - 3 )$ ，and

$$
{ \bf 1 } + \frac { 1 } { 3 ^ { 4 } } + \frac { 1 } { 5 ^ { 4 } } + \frac { 1 } { 7 ^ { 4 } } + \ldots = \frac { \pi ^ { 4 } } { 9 6 }
$$

(the case $d = D = 1$ ， $s = 4$ ,cf.Abramowitz $\&$ Stegun (1966,p.808) and (15) and (16)below).For example when $d = D = 2$ ， $s = 6$ ,we find

$$
1 - { \frac { 1 } { 3 ^ { 6 } } } - { \frac { 1 } { 5 ^ { 6 } } } + { \frac { 1 } { 7 ^ { 6 } } } + { \frac { 1 } { 9 ^ { 6 } } } - { \frac { 1 } { 1 1 ^ { 6 } } } - { \frac { 1 } { 1 3 ^ { 6 } } } + { \frac { 1 } { 1 5 ^ { 6 } } } + \ldots = { \frac { 3 6 1 \pi ^ { 6 } } { 2 4 5 7 6 0 \sqrt { 2 } } } .
$$

Examples of mass formula calculations are given in $\ S \ S 9$ and 10.One of the main aims of this paper was to check the enumeration of lattices of determinant $d \leqslant 2 5$ (up to various dimensions) given in the first paper in this series (Conway $\&$ Sloane $\mathbf { I 9 } 8 8 6$ ; hereafter part I).These calculations,which also provided a stringent check on our formula,are described in $\ S 1 0$ . The lattices (or more precisely their genera) may be conveniently arranged into‘vines', formed by joining any two genera containing lattices $L$ and $L \oplus \mathbf { I _ { 1 \rho } }$ (see,for example,figure 1).Table 7shows how the mass formula was used to check the results of part I.Table 8 then displays the vines containing the lattices enumerated in part I. The glue group orders $g _ { 1 }$ and $g _ { 2 }$ for most of these lattices were given in part I.Table 9 supplies this information for the remaining lattices.

The theoretical justification for the division of genera into vines is provided by lemma 3 of $\ S 1 1$ .Lemmas 1, 2 and 4 of $\ S 1 1$ give other properties of the genus which can.often be used to simplify calculations.In particular,lemmas 2 and 4 can serve as.operational definitions of the genus.

The relation between our $p$ -masses and the more usual $p$ -adic densities is described in $\ S 1 2$ ,and the final section $( \ S _ { 1 3 } )$ gives a heuristic justification for the structure of the mass formula.

# 2.HISTORY

The mass formula has a long history. The two-dimensional version gives the celebrated class number formula of Gauss and Dirichlet (see Cresse I9I9; Landau 1927,vol. I, pp. 127-180; Cassels 1978, pp. 370-374).

Although the general formula is usually referred to as the Minkowski-Siegel mass formula,the version given by H.J.S.Smith $\left( \tt { I } 8 6 7 \right)$ in this journal over 120 years (and 40o volumes) ago is already very close to the modern version. Partial results (mostly for $\mathbf { \nabla } n = 3$ ） had previously been given by Eisenstein. Smith gave certain invariants for quadratic forms,and asserted that he could prove that two forms with the same invariants are equivalent under a rational transformation with inessential denominator.In particular this implies that these invariants are a complete system of invariants for the genus. We have not checked (but have no reason to doubt） that Smith's solution to this problem is equivalent to the solutions given almost 80 years later by Jones (1944) and Pall (1945). Smith also gives a complete statement of the mass formula in the case when the determinant is odd,and asserts that the same methods work in the general case,which ‘presents no theoretical difficulty but [requires a] multiplicity of cases to be considered'.

Minkowski (1885) in his inaugural dissertation gives a formula that sums the mass over any genus.Siegel (1935) found and corrected an error in Minkowski's formula. He also gave a formula for the weighted average of the theta series over the genus,and even more generally a formula for the weighted number of times any given form is represented by the forms of a genus.

Siegel later gave further generalizations-see the papers reprinted in Siegel (1966). From among other works dealing with the mass formula we mention van der Blij (1949), Braun (1941), Cassels (1978), Conway $\&$ Sloane $\left( \mathbf { I } 9 8 2 a , b \right)$ ,Ko (1938，1939)，Magnus (1937),Milnor & Husemoller (1973)，O'Meara (1976), Pfeuffer $( \mathbf { I 9 6 9 } , \mathbf { I 9 7 1 } a , b )$ , and Conway $\&$ Sloane ( $\operatorname { I } 9 8 8 a$ (hereafter SLG), chap.16). The later reference also cites coding-theoretic analogues of the mass formula. The papers by Carlitz (1954), Carlitz & Hodges (1955),Hodges (1955), Pall (1965), Reiner(1956) and Watson (1976) are concerned with the calculation of the $p$ -adic density $\alpha _ { p }$ .For the interpretation of the mass formula in terms of Tamagawa numbers’ see Cassels (1978)，Kneser (1967)，O'Meara (1976)， Serre (1983), Tamagawa (1966) and Weil (1962).

Henry John Steven Smith's 1867 paper was neglected even in his lifetime. Although Smith gives an explicit formula for the number of representations of a number as the sum of five squares,this problem was proposed in 1882 by the French Academy for the Grand Prix des Sciences Mathématiques.Smith stated his formula without proof, but as he wrote to Glaisher,he gives in Smith $\left( \tt { I } 8 6 7 \right)$ ‘the general theory from which this theorem is a corollary with some fullness of detail’(Glaisher 1894,p. lxvi).He submitted a solution (Smith $\mathbf { I 8 8 4 } )$ to the French Academy and, shortly after his death at the age of 56,was awarded the prize jointly with the 19 year old Hermann Minkowski (see Minkowski $\mathbf { r } 8 8 4 \mathbf { \dot { \Omega } }$ ） When awarding the prizes the French Academy made no mention of the fact that Smith had solved the problem more than fifteen years before,nor that ‘any competitor might have availed himself of the indications contained in his published writings’(Glaisher 1894,p. lxx), a circumstance which gave rise to a good deal of comment at the time.

Two further quotations are pertinent.‘The name of Minkowski is familiar today to many,even at Oxford,who have certainly never read a line of Smith.It is curious to contemplate at a distance the storm of indignation which convulsed the mathematical circles of England when Smith,bracketed after his death with the then unknown German mathematician, received a greater honour than any that had been paid to him in life’(Hardy 1920).

From Jowett's memoir (Jowett 1894):‘I have endeavoured...to give a sketch of...one of the most remarkable persons of his time.Yet he lived and died almost unknown to the world at large...His mathematical writings...await the judgment of time.'

Like most other authors,we have hitherto referred to the‘Minkowski-Siegel‘ formula. We now feel that it is more appropriately called the SmithMinkowski-Siegel mass formula.

# 3.ERRORS

There is also a long tradition of errors in the mass formula.Minkowski's version (Minkowski $\mathbf { r } 8 8 5$ ） contained an incorrect power of 2,apparently first noticed by Siegel in 1935. As Smith already remarked in 1867,‘It is easy to apply the general formulae to particular examples; but our imperfect knowledge of quadratic forms containing many indeterminates renders it practically impossible to test the results by any independent process. The demonstrations are simple in principle, but require attention to a great number of details with respect to which it is very easy to fall into error.'

The details are complicated, so that minor errors and misprints are almost inevitable. There are also two other main sources of error. First, the formula as normally stated only applies to dimensions $n \geqslant 2$ ,and the answers produced for $\mathbf { \nabla } \pmb { n } = \mathbf { 0 }$ and1 are often incorrect (not just undefined).We comment further on this in $\ S 6$ .Second, the 2-adic densities are extremely diffcult to evaluate correctly.

Watson (1976) points out some small errors and a missing case in Pall's (1965) formula for the 2-adic density.The formula for the 2-mass in this paper is ultimately derived by translation and simplification of Watson's formula,which seems to us to be essentially correct.+

The errors extend also to the published values for particular cases.For example Magnus (1937) gives incorrect values for the masses of the genera $\mathbf { I _ { 9 } }$ ， $\mathbf { I _ { 1 0 } }$ and $\mathbf { I _ { 1 1 } }$ of odd unimodular forms. (Two of these are quoted by Cassels (1978).) Ko (1939) gave the correct values for $\mathbf { I _ { 9 } } , . . . , \mathbf { I _ { 1 2 } }$ but an incorrect value for $\mathbf { I _ { 1 3 } }$ . When we were preparing chapter 16 of SLG we were unable to locate complete and correct formulae for the mass of the genus ${ \mathbf { I } } _ { n }$ anywhere in the literature. The version in Sloane (1979） contains misprints,and even the version in Conway & Sloane $\left( \mathbf { I } \mathbf { 9 } ^ { 8 2 , b { b } } \right)$ is incorrect for $\pmb { n = 1 }$ .It seems that the entire set of formulae for the mass of the genus ${ \mathbf { I } } _ { n }$ are first correctly stated in SLG (chap.16,theorem 1). Serre (1970) gives the correct formula for the genus $\mathbf { { I I } } _ { n }$ of even unimodular forms (see SLG, chap.16,theorem 2). See also $\ S 9 \mathrm { i v }$ below.

The reader may be confident that our version of the general mass formula (given in the next section) is correct.The enumeration of forms of small determinant given in Part I of this paper has increased our ‘knowledge of quadratic forms containing many indeterminates' and has enabled us to test the formula very stringently.

$^ \dagger$ In fact we could not quite reconcile Watson's version with ours; they appear to differ by a factor of $2 ^ { n }$ for $\pmb { n }$ -dimensional forms.This is almost certainly due to our misunderstanding of Watson's conventions,which differ considerably from ours.

# 4.THE MASS FORMULA

Our version differs from the classical one in that we use the $p$ -masses $m _ { p } ( f )$ of the form rather than the usual $p$ -adic densities $\alpha _ { p } ( f )$ (see $\ S 1 2$ below). The mass formula expresses the mass $m ( f )$ (see (1)) of a genus of positive definite quadratic forms of dimension $n \geqslant 2$ in terms of the $p$ -masses of any form in that genus :

$$
m ( f ) = 2 \pi ^ { - \frac { 1 } { 4 } n ( n + 1 ) } \cdot \prod _ { j = 1 } ^ { n } \Gamma ( \textstyle { \frac { 1 } { 2 } } j ) \cdot \prod _ { p } { ( 2 m _ { p } ( f ) ) } , \quad ( n \geqslant 2 ) ,
$$

where $p$ runs through all primes ${ \bf 2 , 3 , . . . }$ (For $n = 0$ and 1 see $\ S 6 . )$

The $p$ -mass is the reciprocal of the number of automorphisms of $f$ modulo a sufficiently large power $p ^ { r }$ of $p$ , multiplied by a normalizing power of $p$ (for the precise definition see $\ S 1 2 \}$ .If $f$ has a $p$ -adic Jordan decomposition

$$
\begin{array} { r } { f = \sum q f _ { q } , } \end{array}
$$

where $\operatorname* { d e t } f _ { q }$ is prime to $q$ (see $\ S 5 _ { , }$ ， then its $p$ mass $m _ { p } ( f )$ is given by

$$
m _ { p } ( f ) = \prod _ { q } M _ { p } ( f _ { q } ) \cdot \prod _ { \scriptstyle q , q ^ { \prime } \atop { \scriptstyle ( q < q ^ { \prime } ) } } ( q ^ { \prime } / q ) ^ { { \scriptstyle \frac { 1 } { 2 } } n ( q ) n ( q ^ { \prime } ) } \cdot 2 ^ { n ( { \mathbf { I } } , { \mathbf { I } } ) - n ( { \mathbf { I I } } ) } .
$$

Here $q$ ranges over all powers $p ^ { t }$ of $p$ (including those with negative exponent $t$ ）

The factor $M _ { p } ( f _ { q } )$ is called a diagonal factor,and its value can be read from tables 1 and 2 (see) $\ S 5 )$ . The product $\Pi _ { q } \dot { M } _ { p } ( f _ { q } )$ is called the diagonal product.

The factor $( q ^ { \prime } / q ) ^ { \frac { 1 } { 2 } n ( q ) n ( q ^ { \prime } ) }$ , in which $n ( q ) = \dim f _ { q } , n ( q ^ { \prime } ) = \dim f _ { q ^ { \prime } }$ , is called a cro88- term,and the product of all such terms over pairs of distinct powers $q < q ^ { \prime }$ of $p$ is called the cross-product.

The last factor in (3) is called the type factor,and is present only for $p = 2$ ,in which case $n ( \mathrm { I I } )$ is the sum of the dimensions of all Jordan constituents $f _ { q }$ that have type II, and $n ( \mathbf { I } , \mathbf { I } )$ is the total number of pairs of adjacent constituents $f _ { q } , f _ { 2 q }$ that are both of type I.

In this section we show how to compute the diagonal factors $M _ { p } ( f _ { q } )$ . Over the $p$ -adic integers a rational quadratic form $f$ has a Jordan decomposition as a direct sum

$$
f = \ldots \oplus \frac { 1 } { p } f _ { 1 / p } \oplus 1 f _ { 1 } \oplus p f _ { p } \oplus p ^ { 2 } f _ { p ^ { 2 } } \oplus \ldots = \sum _ { q } q f _ { q } ,
$$

where $q$ ranges over all powers of $p$ (including those with negative exponent),and each $f _ { q }$ is a $p$ -adic unit form, that is,a $p$ -adically integral form whose determinant is prime to $p$ . Of course the sum in (4) is really finite, because allbut finitely many of the $f _ { q }$ are love forms (i.e. have dimension zero, see $\ S 6$ ）

Apart from a normalizing power of $p$ , the diagonal factor $M _ { p } ( f _ { q } )$ is the reciprocal of the order of a certain orthogonal group over $\mathbb { F } _ { p }$ associated with the constituent $f _ { q }$ ，The classification of orthogonal groups over $\mathbb { F } _ { p }$ is well known:when the dimension $N$ is odd there is just one such group $O _ { N } ( p )$ ,and when $N$ is even there are two, $O _ { N + } ( p )$ and $O _ { N - } ( p )$ .We call the subscript $( N , N +$ or $N - )$ the species of the group.

The species of the orthogonal group associated with $f _ { q }$ is given by table 1. Then $M _ { p } ( f _ { q } ) = M _ { p } ( N )$ $M _ { p } ( N + )$ or $M _ { p } ( N - )$ depends just on this species,and is given by table 2.

TABLE 1. DETERMINING THE SPECIES OF $f _ { q }$   
![](images/9ea458ff431c4bcc9b5166dae2ba6108213e272eaab080f7bb7669ec1ce2cab8.jpg)

![](images/79909b550de111c35782679e52c6d86795de699b04c943c2e6acd6c8b2fe8722.jpg)

# TABLE 2. DIAGONAL FACTOR $M _ { p }$ AS A FUNCTION OF THE SPECIES

(This is also std $_ p ( f )$ for a form $f$ of one of the dimensions given in the last column.)

![](images/827d250ca158a596f2dcabecf8decee58115ac1e2f2f37c5cb1f9121d765e7fa.jpg)

# The species table (table 1)

We see in the bottom half of table 1 that when $p$ is odd all that matters about $f _ { q }$ is its dimension $n ( q )$ and whether its determinant $d _ { q }$ is or is not a quadratic residue modulo $p$ ，

For $p = 2$ other invariants of $f _ { q }$ must also be considered. If $f _ { q }$ represents an odd 2-adic integer it is called odd or of type I,otherwise it is even or of type II. There is also an invariant of $f _ { q }$ taking values modulo 8,which we call (for want of a better name) its octane value.This may be computed as follows.If $f _ { q }$ has type II its octane value is O or 4 according as its determinant is $\pm 1$ or $\pm 3$ (mod 8). If $f _ { q }$ has type I it may be diagonalized, to say diag $\{ a _ { 1 } , a _ { 2 } , \ldots \}$ ，where the $a _ { i }$ are odd 2-adic integers: Then the octane value of $f _ { q }$ is. the number of $\mathbf { \delta } _ { a _ { i } }$ that are congruent to 1 (mod·4) minus the number of $\mathbf { \delta } _ { a _ { i } }$ that are congruent to -1 (mod 4). (In the notation of (SLG,chap.15), the octane value of $f _ { q }$ is equal to the oddity of $f _ { q }$ if the sign of $f _ { q }$ is $^ +$ ，or the oddity $^ { + 4 }$ if the sign is -.)

Unfortunately the form $f$ can have several essentially different 2-adic Jordan decompositions (see SLG,chap.15).As a result the different Jordan constituents $f _ { q }$ interact, and the species associated with any particular $f _ { q }$ may depend on other constituents.In our analysis we express this dependence by saying that $f _ { q }$ is bound if either (or both) of the adjacent constituents $f _ { { \frac { 1 } { 2 } } q }$ or $f _ { 2 q }$ is of type I,and otherwise that $f _ { q }$ is free.

The top half of table 1 then gives the species of $f _ { q }$ in terms of its type, dimension, octane value,and its free or bound status.

# The diagonal factors (table 2)

The diagonal factor $M _ { p } ( f _ { q } )$ is determined by the species of $f _ { q }$ as follows :

$$
\left. \begin{array} { l } { { M _ { p } ( 2 s - 1 ) = \displaystyle \frac { 1 } { 2 ( 1 - p ^ { - 2 } ) ( 1 - p ^ { - 4 } ) \ldots ( 1 - p ^ { 2 - 2 s } ) } , } } \\ { { { } } } \\ { { M _ { p } ( 2 s \pm ) = \displaystyle \frac { 1 } { 2 ( 1 - p ^ { - 2 } ) ( 1 - p ^ { - 4 } ) \ldots ( 1 - p ^ { 2 - 2 s } ) \cdot ( 1 \mp p ^ { - s } ) } . } } \end{array} \right\}
$$

The first few values are given in table 2. When $p$ is odd,or when $p = 2$ and $f _ { q }$ is free, $M _ { p } ( f _ { q } )$ is just the $p$ -mass of $f _ { q }$ considered as a form in its own right.

6.A NOTE ON LOVE FORMS:THE MASS FORMULA IN DIMENSIONS O AND 1

The sum in (4） extends over all powers $q$ of $p$ ，including those of negative exponent.For almost all $q , f _ { q }$ will be what we call a love form,i.e.have dimension zero.We gain considerable clarity by explicitly including these love forms in the discussion.Although the value of a love form is O,its determinant is 1.

In the Jordan decomposition for an odd prime $p$ ,a love form can be ignored, because it contributes a factor 1 to the mass.However, for $p = 2$ there are two types of love forms : free love forms,which can still be ignored (free love really is free !),and bound love forms which must be taken into account because they each contribute a factor of $\scriptstyle { \frac { 1 } { 2 } }$ to the mass.

The initial 2 in the mass formula (2) is the‘Tamagawa number'of the special orthogonal group $S O _ { n }$ (see Cassels 1978;O'Meara 1976; Serre 1983). It may be regarded as expressing the fact that if we specify $p$ -adic forms of determinant $^ d$ for each $p$ ,then the chance is precisely 1in 2 that there is a global form of which they are the localizations.This 2 should therefore be replaced by 1 in dimensions O and 1,because then both the local and global forms of determinant $\ b { d }$ are unique (it being understood.as above that $d = 1$ in dimension O).

Our $^ { \mathfrak { \prime } } p$ -mass' $m _ { p } ( f )$ was defined in terms of the general orthogonal group $O _ { n }$ ： The factor $2 m _ { p } ( f )$ in (2) is really the ‘proper $p$ -mass', corresponding to the special orthogonal group.The factor 2 in $2 m _ { p } ( f )$ is the index of $S O _ { n }$ in $O _ { n }$ . It should therefore be replaced by 1 in dimension O,where the two groups coincide and all forms are love forms.

7.THE STANDARD $p$ -MASSES AND THE STANDARD MASS

Let $f$ be a form of given determinant $\pmb { d }$ and dimension ${ \boldsymbol { n } } = 2 s$ or ${ \bf 2 } s - 1$ . Then for all but finitely many primes $p$ the $p$ -mass $m _ { p } ( f )$ takes what we shall call its standard value

$$
\operatorname { s t d } _ { p } ( f ) = { \frac { 1 } { 2 ( 1 - p ^ { - 2 } ) ( 1 - p ^ { - 4 } ) \dots ( 1 - p ^ { 2 - 2 s } ) \cdot ( 1 - \epsilon p ^ { - s } ) } } ,
$$

where $\epsilon$ is O for $\pmb { n }$ odd and is otherwise the Legendre symbol

$$
( D / p ) , { \mathrm { w h e r e ~ } } D = ( - 1 ) ^ { s } d ,
$$

which we interpret as O if $p | 2 d$

If all the $p$ -masses took their standard values, the mass $m ( f )$ of $f$ would take its own standard value

$$
\mathrm { s t d } ( f ) = 2 \pi ^ { - n ( n + 1 ) / 4 } \cdot \prod _ { j = 1 } ^ { n } \varGamma ( \frac { 1 } { 2 } j ) \cdot \zeta ( 2 ) \zeta ( 4 ) \ldots \zeta ( 2 s - 2 ) \cdot \zeta _ { D } ( s ) ,
$$

where the last factor $\zeta _ { D } ( s )$ is omitted when $\pmb { n }$ is odd,and otherwise has the value

$$
\begin{array} { r } { \zeta _ { D } ( s ) = \underset { p } { \prod } \left. 1 - \left( \frac { D } { p } \right) \frac { 1 } { p ^ { s } } \right. ^ { - 1 } } \\ { = \underset { m = 1 , 3 , 5 , \ldots } { \sum } \left( \frac { D } { m } \right) \frac { 1 } { m ^ { s } } , } \end{array}
$$

where $( D / m )$ is a Jacobi symbol. $( \zeta ( s )$ is the Riemann zeta function.） We call std $( f )$ the standard mass; the actual mass $m ( f )$ will be a simple rational multiple of this.

Table 3 gives the standard mass (as a multiple of $\zeta _ { D } ( s )$ when $\mathscr { n }$ is even） for dimensions $n \leqslant 2 5$ ，

TABLE 3. STANDARD MASS $\operatorname { s t d } ( f )$ OF AN $\pmb { n }$ -DIMENSIONAL FORM OF   
![](images/a8d23cf482c5aedd407dc4d57d8c557ad7ed52e1270d61b9e28384d12c50ede3.jpg)

# 8. CALCULATION OF $\zeta _ { D } ( s )$

Smith $\left( \mathbf { r } 8 6 7 \right)$ uses results of Dirichlet and Cauchy to evaluate $\zeta _ { D } ( s )$ (see (8)) in terms of Bernoulli polynomials.We use a similar method,following Apostol (1976).We assume $s \geqslant 1$ is an integer.

The sum (9) is the $L$ -series $L ( s , \chi )$ ，where $\chi$ is the Dirichlet character

$$
\chi ( m ) = 0 { \mathrm { ~ i f ~ } } m { \mathrm { ~ e v e n , ~ } } = ( D / m ) { \mathrm { ~ i f ~ } } \ r
$$

We find the modulus $k$ and conductor $k _ { 1 }$ of this character,and write

$$
\chi = \chi _ { 1 } \cdot \psi ,
$$

where $\chi _ { 1 }$ is the principal character modulo $k$ and $\psi$ is a primitive character modulo $k _ { 1 }$ (cf.Apostol 1976,theorem 8.18). Then

$$
\zeta _ { D } ( s ) = { \cal L } ( s , \chi ) = { \cal L } ( s , \psi ) \prod _ { p \mid k } ( 1 - \psi ( p ) / p ^ { s } )
$$

(Apostol 1976,theorem 12.9).From the functional equation for Dirichlet $L$ series,

$$
\begin{array} { c } { { \displaystyle { \cal L } ( 1 - s , \psi ) = \frac { k _ { 1 } ^ { s - 1 } T ( s ) } { ( 2 \pi ) ^ { s } } ( i ^ { - s } + \psi ( - 1 ) i ^ { s } ) { \cal G } ( \psi ) { \cal L } ( s , \psi ) , } } \\ { { { \cal G } ( \psi ) = \displaystyle \sum _ { r = 1 } ^ { k _ { 1 } } \psi ( r ) \mathrm { e } ^ { 2 \pi i r / k _ { 1 } } } } \end{array}
$$

where

(Apostol 1976, the0rem 12.11). Now ${ \bf 1 } - s$ is a non-positive integer, so

$$
L ( 1 - s , \psi ) = - \frac { k _ { 1 } ^ { s - 1 } } { s } \sum _ { r = 1 } ^ { k _ { 1 } } \psi ( r ) B _ { s } \left( \frac { r } { k _ { 1 } } \right) ,
$$

where $B _ { s } ( \boldsymbol { x } )$ is a Bernoull polynomial (Apostol 1976,p. 249 and theorem 12.13). By combining (10)-(12) we obtain

$$
\zeta _ { D } ( s ) = \prod _ { p \mid k } \left( 1 - { \frac { \psi ( p ) } { p ^ { s } } } \right) \cdot { \frac { - ( 2 \pi ) ^ { s } } { s ! ( i ^ { - s } + \psi ( - 1 ) i ^ { s } ) } } \cdot { \frac { \stackrel { k _ { 1 } } { \sum } \psi ( r ) B _ { s } ( r / k _ { 1 } ) } { \stackrel { r = 1 } { \sum } \psi ( r ) \mathrm { e } ^ { 2 \pi i r / k _ { 1 } } } } .
$$

If $k = k _ { 1 }$ ,the initial product in (13) is 1 and can be omitted.Note that (from the definition)

$$
\zeta _ { 4 D } ( s ) = \zeta _ { D } ( s ) , \quad \zeta _ { p ^ { 3 } D } ( s ) = \zeta _ { p D } ( s ) ,
$$

where $p$ is an odd prime and $D$ is arbitrary.

For $d = 1$ we have

$$
\begin{array} { r l } { \zeta _ { 1 } ( s ) = ( 1 - 2 ^ { - s } ) \zeta ( s ) } & { { } ( s \mathrm { e v e n } ) } \\ { \displaystyle } & { { } } \\ { = ( 1 - 2 ^ { - s } ) \frac { ( 2 \pi ) ^ { s } } { 2 \cdot s ! } | B _ { s } | } & { { } ( s \mathrm { e v e n } ) , } \end{array}
$$

$$
\zeta _ { - 1 } ( s ) = { \frac { ( { \frac { 1 } { 2 } } \pi ) ^ { s } } { 2 \cdot ( s - 1 ) ! } } | E _ { s - 1 } | \qquad ( s \operatorname { o d d } ) ,
$$

where $B _ { s }$ and $E _ { s - 1 }$ are Bernoulli and Euler numbers respectively (Abramowitz $\&$ Stegun 1966,chap.23).

Table 4 gives some initial values of $k$ and $k _ { 1 }$ ,and table 5 the values of $\psi ( m )$ for $1 \leqslant m \leqslant k _ { 1 }$ and $| D | \leqslant 9$ .Table 6 gives the values of

$$
\frac { d ^ { s - 1 } \sqrt { d } } { \pi ^ { s } } \zeta _ { D } ( s ) = \frac { d ^ { s - 1 } \sqrt { d } } { \pi ^ { s } } \sum _ { m = 1 , 3 , 5 , . . . } \left( \frac { ( - 1 ) ^ { s } d } { m } \right) \frac { 1 } { m ^ { s } } ,
$$

for $d \leqslant 2 5 , s \leqslant 1 2$

TABLE 4. MODULUS $k$ AND CONDUCTOR $k _ { 1 }$ OF THE DIRICHLET CHARACTER $\chi$ FOR $| D | \leqslant 1 1$   
![](images/85aafd2e9b592a1def06c3a2d5e43e04944c66bc12cf4a7161fc02febbe3585a.jpg)

TABLE 5.VALUES OF THE PRIMITIVE CHARACTER $\psi ( m )$ FOR $1 \leqslant m \leqslant k _ { 1 }$ AND $| D | \leqslant 9$   
![](images/9a143050de40495602e5da7d26ac8d720b7fd4f7dc3d2a94d8bd2a95ca3631f8.jpg)

$$
{ \begin{array} { r l r l r l r l r l r l r l r l r l r l r l } { { 5 } } & { 0 } & { 0 } & { - } & { 0 } & { - } & { 0 } & { 0 } & { 0 } & { 0 } & { - } & { 0 } & { 0 } & { 0 } & { - } & { 0 } \\ { 6 } & { 0 } & { 0 } & { - } & { 0 } & { + } & { 0 } & { 0 } & { 0 } & { 0 } & { + } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 6 } & { 0 } & { 0 } & { - } & { 0 } & { - } & { 0 } & { 0 } & { 0 } & { 0 } & { - } & { 0 } & { 0 } & { - } & { 0 } & { 0 } & { 0 } \\ { 7 } & { - } & { 0 } & { - } & { 0 } & { + } & { 0 } & { 0 } & { 0 } & { 0 } & { - } & { 0 } & { 0 } & { + } & { 0 } & { + } & { 0 } & { 0 } \end{array} }
$$

# 9.EXAMPLES OF MASS CALCULATIONS

(i) As a first example we exhibit the calculations for the mass of the genus containing the form $f = \mathrm { d i a g } \left\{ 7 , 1 , 1 \right\}$ .For $p = 2$ the Jordan constituents $f _ { q }$ are love forms except for $q = 1$ ，when $f _ { 1 } = f ;$ ，of type I,dimension 3 and octane value $- 1 + 1 + 1 = 1$ .All $f _ { q }$ are free except $f _ { \frac { 1 } { 2 } }$ and $f _ { 2 }$ ，which are bound. For $p = 7$ the constituents are love forms except for $q = 1$ (when $f _ { 1 } = \mathrm { d i a g } \{ 1 , 1 \} )$ and $q = 7$ (when $f _ { 7 } = \mathrm { d i a g } \left\{ { \bf 1 } \right\} )$ . The calculations are shown in the following tableau (page 272, explained in more detail below).

TABLE 6.VALUES OF $\zeta _ { D } ( s ) d ^ { s - 1 } \sqrt { d / \pi ^ { s } }$   
![](images/a67613fbb7748366e45620866bb819ade6c8c86d91306ac319dcef0b33cebad8.jpg)
This content downloaded from 75.138.140.178 on Wed,02 Apr 2025 23:51:27 UTC All use subject to https://about.jstor.org/terms

$$
( D = ( - 1 ) ^ { d } s ) , \mathtt { F O R } d \leqslant 2 5 , s \leqslant 1 2
$$

![](images/6f180f83bea381b88a6a0529910772b7c9681cefe1462993f74ad7d2db6b9335.jpg)

![](images/48a34c999055e5d25c43af986caf1cd4bfa124baeeb39f8c85ded1e8745ba314.jpg)

For all other $p$ the $p$ -mass is $\operatorname { s t d } _ { p } ( f )$ ,and so for this form we have

$$
\begin{array} { r } { m ( f ) = \frac { 3 } { 8 } \times 3 \times \mathrm { s t d } ( f ) = \frac { 9 } { 8 } \mathrm { s t d } ( f ) = \frac { 9 } { 8 } { \cdot } \frac { 1 } { 6 } = \frac { 3 } { 1 6 } . } \end{array}
$$

Here std $( f )$ can either be read from table 3,or evaluated directly as

$$
\mathrm { s t d } \left( f \right) = 2 \pi ^ { - 3 } T ( 1 / 2 ) T ( 2 / 2 ) T ( 3 / 2 ) \zeta ( 2 ) = 1 / 6 .
$$

In the tableau,for $p = 2 , \mathbf { I } _ { n } { : } v$ or $\operatorname { I I } _ { n } { : v }$ indicates an $\pmb { n }$ -dimensional Jordan constituent $f _ { q }$ of type I or II and octane value $v$ ，with asterisks for bound forms. For odd $p$ $\scriptstyle { R _ { n } }$ or $N _ { n }$ indicates an $f _ { q }$ of dimension $\pmb { n }$ whose determinant is a quadratic residue or non-residue (mod p) respectively. The species are read from table 1,the diagonal factors from table 2,and their product is the diagonal product.

The $p$ -mass $m _ { p } ( f )$ is then found by multiplying the diagonal product by the cross-terms (written in the form $\mathcal { V } ( q ^ { \prime } / q ) ^ { n ( q ) \times n ( q ^ { \prime } ) } )$ ， and the type factor if any (written in the form $2 ^ { j - k }$ ，where $j = n ( \mathbf { I } , \mathbf { I } )$ ， $k = n ( \mathbf { I I } )$ ). We finally express it as a fraction of the standard $p$ -mass $\operatorname { s t d } _ { p } ( f )$ (see (6)), whose values can also be read from table 2,using the fact that,when $p$ divides $\mathbf { 2 } d$ ，

$$
\mathrm { s t d } _ { p } ( f ) = \left. { \cal M } _ { p } ( n ) \mathrm { i f } n \mathrm { o d d } , \right. \left. \right.
$$

In this example we verify that the mass of $\mathbf { 3 / 1 6 }$ is correct,by observing (from part I, or from the $7 ^ { + }$ vine of table 7 below) that there are two forms in the genus of $f _ { i }$ namely $\mathbf { 7 _ { 1 } } \oplus \mathbf { I _ { 2 } } = f$ itself and $\mathbf { \nabla } \mathsf { I } _ { 2 } \oplus \mathbf { I _ { 1 } } = { \mathfrak { g } }$ .These forms have automorphism groups of orders 16 and 8 respectively,and indeed

$$
{ \frac { 1 } { 1 6 } } + { \frac { 1 } { 8 } } = { \frac { 3 } { 1 6 } } .
$$

(ii) As a second example we calculate the mass of the genus containing the fourdimensional form $f = a _ { 3 } \oplus \mathrm { { I } } _ { 1 }$ ，of determinant 24,where $a _ { 3 } = A _ { 1 } ^ { 2 } 2 4 _ { 1 } [ 1 1 \frac { 1 } { 2 } ]$ ，with Gram matrix

$$
{ \left( \begin{array} { l l l } { 7 } & { 1 } & { 1 } \\ { 1 } & { 2 } & { 0 } \\ { 1 } & { 0 } & { 2 } \end{array} \right) } ,
$$

is the first three-dimensional form in the tableat the end of $\ S 5$ of part I. This form can be diagonalized to

$$
\mathrm { d i a g } \{ 7 , 1 3 / 7 , 2 4 / 1 3 \}
$$

by a transformation not involving divisions by 2 or 7,so its 2-adic decomposition is diag{7, 13/7}8 diag $\{ \mathbf { 3 } / 1 3 \}$ and its 3-adic decomposition is ( $\operatorname* { l i a g } \left\{ 7 , 1 3 / 7 \right\} \oplus$ 3 diag $\{ { \bf 8 } / { \bf 1 3 } \}$ . The tableau for the mass of $f$ is then :

![](images/e0e40cf328cbf57ed59cc29001f5bf050f028479bbe4ce40960f11037fd440d5.jpg)

Thus the mass $m ( f )$ is

$$
{ \cfrac { 3 } { \sqrt { 2 } } } \times { \cfrac { 3 \sqrt { 3 } } { 2 } } \cdot \operatorname { s t d } \left( f \right) = { \cfrac { 9 \sqrt { 3 } } { 2 \sqrt { 2 } } } \cdot { \cfrac { \zeta _ { 2 4 } ( 2 ) } { 6 \pi ^ { 2 } } } = { \cfrac { 3 } { 3 2 } } ,
$$

(by using table 3 for.std $( f )$ and table 6 for $\zeta _ { 2 4 } ( 2 ) = \zeta _ { 6 } ( 2 ) = \textstyle { \frac { 3 } { 2 } } \cdot \pi ^ { 2 } / 6 \sqrt { 6 } )$ ：

In fact,from part I(or the $2 4 _ { - } ^ { - + }$ vine of table 7 below) there are two forms in the genus of $f$ ，namely

$$
\begin{array} { r } { f = a _ { 3 } \oplus \operatorname { I } _ { 1 } = A _ { 1 } ^ { 2 } 2 4 _ { 1 } [ 1 1 { \frac { 1 } { 2 } } ] \oplus \operatorname { I } _ { 1 } \mathrm { ~ a n d ~ } g = c _ { 4 } = A _ { 1 } 6 _ { 1 } ( 3 ^ { 1 } 3 ) _ { 2 } [ 1 { \frac { 1 } { 2 } } { \frac { 1 } { 2 } } { \frac { 1 } { 2 } } ] . } \end{array}
$$

Their total mass is indeed

$$
{ \frac { 1 } { 2 ^ { 2 } \cdot 2 \cdot 2 \cdot 2 } } + { \frac { 1 } { 2 \cdot 8 \cdot 1 } } = { \frac { 3 } { 3 2 } } .
$$

(iii) An abbreviated tableau.Because each bound love form contributes a factor of $\scriptstyle { \frac { 1 } { 2 } }$ (see $\ S 6 )$ ，the tableaux may be simplified by omitting the love forms and replacing the type factor $2 ^ { i - j }$ by $2 ^ { i - j - l }$ ，where $ { \boldsymbol { l } }$ is the number of bound love forms.

The abbreviated tableaux for our examples are

![](images/18e32f04ae5a483ddf91bd592534b2657ca80599178db074c9507120b9bf5e5c.jpg)

and

![](images/3de6c74c8120a91cb5e9b8d6d205fcf77b9552004078b1ac2ac38b5663a2a362.jpg)

(iv) Unimodular lattices.For $d = 1$ (2)easily yields the expressions for the mass of unimodular lattices given in theorems 1 and 2 of SLG (chap.16). (For the odd genera, $\pmb { \zeta } _ { \pm 1 } ( s )$ is given by (15) and (16).)

# 10.VERIFICATION OF THE RESULTS OF PART I

In this section we describe how the mass formula was used to check the enumeration of lattices of small determinant given in part I. Tables 8 and 9 supply additional information about these lattices.

The lattices may be arranged into‘vines’(such as that shown in figure 1) as follows.We form a graph, in which each node represents a genus,and nodes for genera containing lattices $L$ and $L \oplus \mathbf { I _ { 1 \rho } }$ are joined by an edge.

In view of lemma 3 of $\ S 1 3$ ，this graph has the following structure.Each connected component of the graph is a tree consisting of a single path (the ‘stem'), the nodes of which represent odd genera, together with other nodes representing even genera that are joined to the stem by single edges (the‘twigs'). There is at most one twig at any stem node.We call such a tree a‘vine'.

Figure 1 shows the beginning of the vine containing the determinant 11 lattices of genera $\mathrm { I } _ { n } ( 1 1 ^ { + } )$ (the stem)and $\Pi _ { n } ( 1 1 ^ { + } )$ (the twigs). Only lattices containing no vectors of norm 1 are shown.The complete set of $\pmb { n }$ -dimensional lattices in agiven vine then consists of all direct sums $L _ { r } \oplus \operatorname { I } _ { n - r }$ ，where $L _ { r }$ is any $r$ -dimensional lattice $( r \leqslant n )$ that is marked on the vine.

![](images/bbb37fcf348e5ece05414105a88da0232e3ff6b69dc00cb63ff4db0ddc1bf394.jpg)  
FIGURE 1.Vine showing lattices of determinant 11 and genera $\mathrm { I } _ { n } ( 1 1 ^ { + } )$ (the stem) and $\Pi _ { n } ( 1 1 ^ { + } )$ (the twigs).Only lattices with no vectors of norm 1 are shown.

We illustrate by displaying (in table 7) the calculations for the determinant $1 1 ^ { + }$ vine shown in figure 1. The 2-adic decomposition of any form $f$ in $\mathbf { I } _ { n } ( 1 1 ^ { + } )$ (for example $f = \mathrm { d i a g } \left\{ { \bf 1 1 } \right\} \oplus { \bf I } _ { n - 1 } )$ has $f _ { 1 } = f _ { : }$ ，of type I,dimension $\mathscr { n }$ and octane value ${ \it \Delta } n - 2$ ,while the other $f _ { q }$ are love forms,of which $f _ { \frac { 1 } { 2 } }$ and $f _ { 2 }$ are bound.In the 11-adic decomposition, ${ \mathrm { d i m } } f _ { 1 } = n - 1$ ， $\dim f _ { 1 1 } = 1$ ，and both determinants are residues.

The total mass of $\mathbf { I } _ { n } ( 1 1 ^ { + } )$ as given by (2) is shown in the second column of table 7.

The remaining columns of table 7 give the contributions to the mass from each family $L _ { \kappa } \oplus \mathbf { I } _ { n - k }$ ，where $L _ { k }$ contains no vectors of norm 1.The mass of $L _ { k } \oplus \mathbf { I } _ { r }$ is obtained by dividing the mass of $L _ { k } \oplus \mathbf { I } _ { r - 1 }$ by $2 r$ as indicated. Because $L _ { 6 } = 1 1 _ { 6 }$ is even,its mass {enclosed in curly brackets} only contributes to the odd genera in dimensions 7 onwards.As can be seen, the masses do sum to the predicted values.

Similar calculations were performed for all the vines in table 8 below. Once the lattices were placed in the appropriate vines，we verified that the total mass $\sum \vert \mathbf { A u t } ( f ^ { ( i ) } ) \vert ^ { - 1 }$ of the lattices $f ^ { ( 1 ) } , \ldots , f ^ { ( h ) }$ at each node was equal to the value $m ( f ^ { ( 1 ) } )$ given by (2). This was now essentially a simple and routine arithmetical calculation,because the group orders are fully specified by table 1 of part I and table 9 below.

The calculations were automated to a certain extent.Inevitably we found a few errors in the manuscript of part I,which of course we corrected.But most of the time it was quite astonishing to watch the miraculous agreement of the two calculations!

# Description of tables 8 and 9

In part I we enumerated lattices of determinant $d \leqslant 2 5$ up to various dimensions (ranging from dimension 18 for $\pmb { d } = 1$ to $\pmb { n = 7 }$ for $d = 2 5$ ). The vines containing these lattices are given in table 8.

Each line of table 8 represents one vine.The genera (i.e. the nodes) are separated by semicolons, while the lattices in a genus are separated by commas.Even genera (or twig nodes) are enclosed in curly brackets $\{ \}$ ,the other genera being odd (or stem nodes).

Only lattices containing no vectors of norm 1 are shown.In the majority of cases the names of the lattices are taken from table 1 of part I.That table also gives the Witt components, glue vectors, genus symbol and group orders $g _ { 1 }$ and ${ \pmb g } _ { 2 }$ for those lattices.

# TABLE 8.VINES SHOWING THE CLASSIFICATION OF THE LATTICES OF PART I

(Semicolons separate genera,commas separate individual lattices,and type $\mathbf { I I }$ lattices are

INTO GENERA   
![](images/03d5970d3c61d58664ff12e8d65e63ad415acbffb610b2b2b9cf0da06b69d5f8.jpg)

# TABLE 8 (cont.)

# determinant

lattices

$4 ^ { 2 - }$ （42）；（42-）；{Cg}$4 _ { + } \cdot 4 _ { + }$ {4)；（44）,{44}；mg44 {44}；（44）；Jg,{44,44}44 (4:4)4； (4）；eg,54.22 {44； （4-2）42 （4+22）s；（4${ \bf 4 } \cdot { \bf 2 } \cdot { \bf 2 }$ 42；{42； (42.2), {42, 44)24 (24)6； {432.2·2·2 {21）；{423）；kg,{42}$1 7 ^ { + }$ 1717；17t17g;67$1 7 ^ { - }$ 17; 17;(173; 17；; a,,${ \bf 1 8 ^ { + } }$ 92;18;92; 18; {c)18- {18}；92；18;92;d,{a,b}32+·2 32, {63)； 322)；63;32-.2 63；332；18；92,{63,63)$1 9 ^ { + }$ 19；19；19；19;C6,{,6}；19+$1 9 ^ { - }$ {19}；19；194;d；;19,20 {203;54；(20）,54, （20+）3； 54；h20 54；20；{（20-）3；54，f20 {20）；54；（20）954,c)20 20；{20}；54；(5.4）；e,{a,b)5+:22 {（5+ 22）); 544； (522)6$\begin{array} { r l } { \sum _ { j = 1 } ^ { n } } &  \frac { \partial } { \partial x _ { j } } \sum _ { j = 1 } ^ { n } \sum _ { k = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^ { n } \sum _ { l = 1 } ^  \end{array}$

TABLE 9. THE WITT COMPONENTS AND ${ \pmb g _ { 1 } , \pmb g _ { 2 } }$ FOR THE LATTICES IN TABLE 8 THAT ARE NOT GIVEN IN PART I,TABLE 1   
![](images/fbb7e6f851f499066bcca629446e85fbcd5a2d1044968d0ab3f6e07630b1b4a6.jpg)

TABLE 9 (cont.)   
![](images/fafb51127f759637bc94a8ecc5c84c0e30019af4c8f95d341fff9264eecaed33.jpg)

Lattices that appear in the supplementary table (table 2) of part I have been named in table 8 as follows.The lattices of determinant $\ b { d }$ and dimension $\pmb { n }$ in the supplementary table have been labelled $a _ { n } , b _ { n } , c _ { n } , \ldots$ reading from left to right.A similar notation has been used for the lattices of determinants 19, 23,24 and 25 that are described in the text of part I.

The group orders $g _ { 1 }$ and ${ \pmb g } _ { \mathbf 2 }$ (defined in part I) for the lattices described in the preceding paragraph were omitted from part I,and this information is now given in table 9.For each $\pmb { n }$ -dimensional lattice of determinant $^ d$ ,table 9 gives $d _ { n }$ ,，the name of the lattice,its Witt components, and the values of ${ \pmb g } _ { \bf 1 }$ and ${ \pmb g } _ { 2 }$

# 11.PROPERTIES OF THE GENUS

In this section we state without proof some properties of the genus,which can sometimes be used to simplify the calculations. (These results also follow from Kneser & Puppe (1953).) Lemmas 2 and 4 also serve as operational definitions of the genus.

LEMMA 1. Two forms $f$ and $g$ are in the same genus if and only if the indefnite .forms

$$
f \oplus { \left( \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right) } \quad { \mathrm { a n d } } \quad g \oplus { \left( \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right) }
$$

are integrally equivalent.

This follows from properties of the spinor genus (see SLG, chap.15).

The other lemmas are best stated in terms of lattices rather than quadratic forms. Let $L$ be an integral lattice, and $L ^ { * } / L$ the dual quotient group. The norms of all vectors in any given coset $u + L$ of $L ^ { * } / L$ are congruent modulo 1 (or modulo 2if $L$ is even),and so the norm defines a quadratic form on $L ^ { * } / L$ which takes values in $\mathbb { Q } / \mathbb { Z }$ (or $\mathbb { Q } / 2 \mathbb { Z }$ if $L$ is even).

LEMMA 2. Two lattices $L$ and $M$ are in the same genus if and only if they have the same dimension n and type $\pmb { T }$ (where $\mathbf { \nabla } T = 1$ for type I, ${ \pmb T } = { \pmb 2 }$ for type II) and there is an isomorphism between the dual quotients $L ^ { * } / L$ and $M ^ { * } / M$ which preserves norms modulo $\pmb { T }$

LEMMA 3.If two lattices $L \oplus \mathbf { I _ { 1 \rho } }$ and $M \oplus \mathbf { I _ { 1 \oplus \mathbf { \phi } } }$ are in the same genus,then so are L and M provided they have the same type ${ \boldsymbol { T } } \left( = 1 o r \ 2 \right)$

Lemmas 2 and 3 are proved by verifying that the given information is enough to determine the invariants of their Jordan decompositions.This is trivial except when $p = 2$ ：

By combining lemmas 2 and 3 we can strengthen lemma 2.

LEMMA 4. Two lattices $L$ and $M$ are in the same genus if and only if they have the same dimension and type and there is an isomorphism between $L ^ { * } / L$ and $M ^ { * } / M$ which preserves norms modulo 1.

For the proof we apply lemma 2 to $L \oplus  \bf I _  1 \it$ and $M \oplus \mathbf { I _ { 1 \oplus \mathbf { \oplus \mathbf { \oplus \mathbf { \oplus \mathbf { \oplus \mathbf { \oplus \mathbf { \oplus \mathbf { \oplus \mathbf { \oplus \mathbf { \oplus \mathbf { \oplus \ddots } } } } } } } } } } } }$ ,and then use lemma 3. However, lemma 2 has a categorical character not shared by lemma 4. In lemma

4 there need not be a 2-adically integral equivalence between $L$ and $M$ that induces the given isomorphism between their dual quotients $L ^ { * } / L$ and $M ^ { * } / M$ ：

We demonstrate one possible application of these lemmas by finding the possible genera of lattices of various small determinants.If $L$ has determinant $d = 2$ ,and $v _ { 2 }$ is a vector that generates $L ^ { * }$ modulo $L$ ,then $v _ { 2 } \cdot v _ { 2 }$ must be congruent to $\scriptstyle { \frac { 1 } { 2 } }$ (mod 1) (for if $v _ { 2 } \cdot v _ { 2 }$ were an integer then $\langle L , v _ { \mathbf { 2 } } \rangle$ would be an integral lattice of determinant $\scriptstyle { \frac { 1 } { 2 } } ,$ ).Lemma 4 now implies that $L$ has one of two possible genera, namely $\mathbf { I } _ { n } ( 2 )$ if $L$ is odd or $\mathrm { { I I } } _ { n } ( 2 )$ if $L$ is even. These genera form a single vine (cf. $\ S 1 0 )$ ：

Similarly,if $d = p$ is an odd prime,and $v _ { p }$ generates $L ^ { * }$ modulo $L$ ，then $v _ { p } \cdot v _ { p } = a / p$ where $a \neq 0$ is an integer. Because $N ( k v _ { p } ) = k ^ { 2 } N ( v _ { p } )$ ，only the quadratic residuacity of $^ { a }$ modulo $p$ is important,and (by lemma 4) there are four possible genera in two vines,belonging to

$$
\begin{array} { r l } { \mathrm { I } _ { n } ( p ^ { + } ) \ \mathrm { a n d } \ \mathrm { I I } _ { n } ( p ^ { + } ) , } & { { } \mathrm { I } _ { n } ( p ^ { - } ) \ \mathrm { a n d } \ \mathrm { I I } _ { n } ( p ^ { - } ) } \end{array}
$$

(the $^ +$ sign if $^ { a }$ is a residue, the - sign for a non-residue).

Distinct primes can be treated independently. Thus in the case of determinant $d = 2 p$ ， $L ^ { * }$ is generated modulo $L$ by vectors $v _ { 2 }$ and $v _ { p }$ ，of orders 2 and $p$ respectively. The preceding argument shows that there is only one choice for the norm of $v _ { 2 }$ (mod 1),and two choices for the norm of $v _ { p }$ (mod 1),so that again there are four genera in two vines :

$$
\mathrm { I } _ { n } ( d ^ { + } ) ~ \mathrm { a n d ~ I I } _ { n } ( d ^ { + } ) , \ : \ : \ : \mathrm { I } _ { n } ( d ^ { - } ) ~ \mathrm { a n d ~ I I } _ { n } ( d ^ { - } ) ,
$$

where $\mathbf { I } _ { n } ( d ^ { + } )$ abbreviates $ { \mathbf { I } } _ { n } ( p ^ { + } \cdot 2 )$ , etc. as in part I.

# 12.THE $p$ -ADIC DENSITY AND THE $p$ -MASS

The mass is traditionally expressed in terms of certain constants $\alpha _ { p } ( f )$ called the $p$ -adic densities (cf. Siegel 1935). Our idea of giving the same information in terms of the $p$ -masses $m _ { p } ( f )$ was prompted by Watson's suggestion (1976, p. 106) of a ‘more modern form’for the mass.However,our formula improves on Watson in that it is visibly invariant under duality as well as scale changes.

Let $N ( p ^ { r } )$ be the number of $\pmb { n } \times \pmb { n }$ matrices $X$ , with entries which are integers modulo $p ^ { r }$ , that satisfy

$$
X ^ { t r } A X \equiv A { \pmod { p ^ { r } } } ,
$$

where $\pmb { A }$ is the Gram matrix of the form $f .$ ：Then for all sufficiently large $r$ ，the $p$ -adic density

$$
\alpha _ { p } ( f ) = \frac { N ( p ^ { r } ) } { p ^ { \frac { 1 } { 2 } r n ( n - 1 ) } }
$$

is independent of $r$ .If $p ^ { s }$ is the highest power of $p$ dividing the determinant $\operatorname* { d e t } f = \operatorname* { d e t } A$ ,then the $\pmb { p }$ -mass is given by

$$
m _ { p } ( f ) = \frac { p ^ { \frac { 1 } { 2 } s ( n + 1 ) } } { \alpha _ { p } ( f ) } = \frac { p ^ { \frac { 1 } { 2 } \{ r n ( n - 1 ) + s ( n + 1 ) \} } } { N ( p ^ { r } ) } .
$$

Thus the $p$ -mass is the reciprocal of the order of the automorphism group of the form modulo $p ^ { r }$ , multiplied by a normalizing power of $p$

The $p$ -adic density $\alpha _ { p } ( f )$ seems inappropriate for several reasons. First, it is embarrassing that the mass of a form varies inversely with the density!Also the $p$ -mass,unlike the $p$ -adic density,is invariant under changing the scale of the form:

# 13.THE STRUCTURE OF THE MASS FORMULA

We shall neither prove the mass formula ((2) and (3)) nor justify our evaluation of the $p$ -masses $( \ S 5 )$ .However the following remarks may make the formulae plausible.

The approximation theorem (cf. Cassels $\yen 978$ ，chap.3） tells us that a determinant 1 automorphism of $f$ is adequately specified by the corresponding determinant 1 automorphisms of the $p$ -adic localizations of $f .$ This explains why we should expect $m ( f )$ to be proportional to the product $\Pi _ { p } ( \bar { 2 } m _ { p } ( f ) )$ (see (2)). The precise factor of proportionality is determined by an integration over $S O ( n )$ (cf. Siegel 1935).

We next discuss the form of(3),supposing first that $p$ is odd. The typical matrix $X$ in (18) has the form shown in figure 2.The typical diagonal block $X _ { q }$ ,when read modulo $p$ ,is an automorphism of $f _ { q }$ $( { \bf m o d } p )$ .If $f _ { q }$ has dimension $\boldsymbol { n } ( \boldsymbol { q } ) = \boldsymbol { N }$ ，such automorphisms form the orthogonal group over $\mathbb { F } _ { p }$ of species $N$ ， $N +$ ，or $N -$ (see $\ S 5$ ).

![](images/00209965b09522337e5c240d12fc932742b82a6870a7eeae3f0e3774d0a061d7.jpg)  
FIGURE 2. Structure of matrix $X$ satisfying (18).

Again, if $q < q ^ { \prime }$ (but not if $q > q ^ { \prime }$ ）we can add multiples of the basis vectors for $f _ { q ^ { \prime } }$ to those for $f _ { q }$ without changing their norms and inner products modulo $p$ When the normalizing powers of $p$ are taken into account these transformations explain the cross-terms in (3).

When $p = 2$ the situation is more complicated:the quadratic form corresponding to $f _ { q }$ may not have the same dimension as $f _ { q }$ .For instance when $f _ { q }$ is $x _ { 1 } ^ { 2 } + \ldots + x _ { 4 } ^ { 2 }$ ,the appropriate quadratic form is defined only on the 2-space of binary vectors $( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } )$ with an even number of 1's,taken modulo (1,1,1,1),and its value is half the number of1's in such a vector.This is a quadratic form of species $\mathbf { 2 } -$ .This explains the entry $\mathbf { 2 } -$ corresponding to $\mathbf { I } _ { 4 } { : } 4$ in table 1.

The dimension $N$ of the orthogonal group in table 1 may even be greater than the dimension of $f _ { q }$ ! We explain this,and also the relevance of the free or bound status of $f _ { q }$ ，by considering the forms $f$ and $g$ with Gram matrices

$$
\begin{array}{c} \begin{array} { c c } { { e _ { 1 } \bigg ( 2 } } & { { 1 \bigg ) , } } & { { e _ { 1 } \bigg ( 2 } } \\ { { e _ { 2 } \bigg ( 1 } } & { { 2 \bigg ) , } } & { { e _ { 2 } \bigg ( 1 } } \\ { { } } & { { e _ { 3 } \big ) 0 } } & { { 0 } } \end{array} \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } \\ { { 0 } } & { { 2 } } \end{array} \begin{array} { c c } { { 0 } } \\ { { 0 } } \\ { { 2 } } \end{array} \bigg )  \end{array}
$$

respectively. Both $f$ and $g$ have the same Jordan constituents for $q = 1$ , namely $f _ { 1 } = g _ { 1 } = 2 \ ( x ^ { 2 } + x y + y ^ { 2 } )$ ， of dimension 2 and octane value 4 (corresponding to $\mathbf { I I _ { 2 } } { : } 4$ in table 1),but this is free for $f$ and bound for $g$ ，

The matrix $X$ of (18) for $f ,$ when read modulo 2,must be an automorphism of $x ^ { 2 } + x y + y ^ { 2 }$ .Such automorphisms form the orthogonal group of species $\mathbf { 2 } -$ over $\mathbb { F } _ { 2 }$ .This explains the entry $\mathbf { 2 - }$ for free forms $\Pi _ { 2 } { : } 4$ in table 1.

However,in the typical matrix

$$
X = { \left( \begin{array} { l l l } { a } & { b } & { * } \\ { c } & { d } & { * } \\ { * } & { * } & { X _ { 2 } } \end{array} \right) }
$$

for the form $g$ the leading $\mathbf { \delta 2 } \times \mathbf { 2 }$ block $X _ { 1 } = { \binom { a \ b } { c \ d } }$ need not orespod to an automorphism of the constituent $g _ { 1 }$ .This is because $g$ has other Jordan decompositions.For example $g$ is 2-adically equivalent to the form $\boldsymbol { h }$ with Gram matrix

$$
\begin{array} { l } { { e _ { 1 } ^ { \prime } = e _ { 1 } } } \\ { { e _ { 2 } ^ { \prime } = e _ { 2 } + e _ { 3 } \left( \begin{array} { l l l } { { 2 } } & { { 1 } } & { { 0 } } \\ { { 1 } } & { { 4 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { { \frac { 6 } { 7 } } } } \end{array} \right) , } } \end{array}
$$

for which $h _ { 1 }$ is the form $2 ( x ^ { 2 } + x y + 2 y ^ { 2 } )$ with octane value O (so $\mathbf { I I _ { 2 } } { : } \mathbf { 0 }$ ). Note that the transformation

$$
\scriptstyle { \left( { \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \\ { { \frac { 4 } { 7 } } } & { { \frac { - 2 } { 7 } } } & { { \frac { 3 } { 7 } } } \end{array} } \right) } = { \left( { \begin{array} { l l l } { 1 } & { 0 } & { * } \\ { 0 } & { 1 } & { * } \\ { * } & { * } & { { \frac { 3 } { 7 } } } \end{array} } \right) }
$$

between $g$ and $\pmb { h }$ has the identity matrix for $X _ { 1 }$ . Consider now the general $X$ of (18) and (19) for $g$ .The $X _ { 1 }$ block need not correspond to an automorphism of ${ \pmb g } _ { \bf 1 }$ .It could for example transform $g _ { 1 }$ to $h _ { 1 }$ with matrix

$$
{ \binom { 2 } { 1 } } ,
$$

because this can be cured by dividing by (20).

However, for any $X$ ,the matrix $X _ { 1 }$ (modulo 2) must preserve the symplectic form with matrix

$$
\binom { 0 } { 1 } \binom { 1 } { 0 }
$$

obtained by reading $g _ { 1 }$ or $h _ { 1 }$ modulo 2,and the group of such matrices is the twodimensional symplectic group over $\mathbb { F } _ { \mathbf { 2 } }$ .It is well-known that the $\mathbf { 2 } m$ -dimensional symplectic group over $\mathbb { F } _ { 2 }$ is isomorphic to the $( 2 m + 1 )$ -dimensional orthogonal group. This explains the entry 3 for bound forms $\mathbf { I I _ { 2 } }$ : in table 1. The equivalence between $\pmb { g }$ and $\mathbf { \Omega } _ { h }$ in this example is a case of ‘sign-walking’(see SLG, chap.15).

In a similar way, every multiplicity of‘canonical forms‘ for $f$ (see SLG, chap. 15, $\ S 7 )$ has its effect on the mass formula. If $f _ { q }$ and $f _ { 2 q }$ are both of type I we can increase the octane value of $f _ { q }$ by any even number $v$ while decreasing that of $f _ { 2 q }$ by $v$ .However, if $v$ is a multiple of four, this can also be done by sign-walking, so we have just one extra factor of two for each adjacent pair $f _ { q } , f _ { 2 q }$ of type I forms. This explains the portion $\textstyle { \mathfrak { Z } } ^ { n ( \mathbf { I } , \mathbf { I } ) }$ of the type factor (see (3)).

The invariants for a type $\mathbf { I }$ summand $f _ { q }$ are its sign

$$
\epsilon _ { q } = \left( \frac { 2 } { \mathrm { d e t } f _ { q } } \right)
$$

and its octane value, whereas for a type II summand the octane value is already determined by $\epsilon _ { q }$ .What amount of information about the canonical form for a type I summand $\boldsymbol { f _ { q } } = \operatorname { d i a g } \left\{ a _ { 1 } , \dots , a _ { n ( q ) } \right\}$ is required to compute the octane value ? Answer : $n ( q )$ bits, specifying the $2 ^ { n ( q ) }$ signs in $a _ { i } \equiv \pm 1$ (mod 4).Each type II summand $f _ { q }$ loses this much information.This explains the portion $2 ^ { - n ( \mathbf { I I } ) }$ of the type factor.

It should now be apparent that a real understanding of the 2-adic contribution requires knowledge of the possible 2-adic structures of the form and of a suitable parametrization of orthogonal groups in characteristic 2.It is therefore not surprising that the 2-adic part of the mass caused so much diffculty，because (after Smith) the 2-adic structure was first completely described by Jones (1944) and Pall (1945),and the correct parametrization of the orthogonal groups only emerged after the work of Chevalley (1955） and Dieudonné (1955).

We caution the reader that our brief‘explanations’ conceal as much as they reveal.We have explained the mass in terms of matrices that take one‘canonical form'of $f$ to a distinct one.When expressed instead in terms of the matrices $X$ that preserve $f ,$ ，the explanation to some extent depends on the fact that the Hensel lifting process for $p = 2$ sometimes demands initial terms of greater accuracy than it does for odd $p$

It is a remarkable instance of the principle of permanence of form that the diagonal product for $p = 2$ looks so similar to that for odd $p$ ，because the explanations differ in so many details.

# REFERENCES

Abramowitz，M. & Stegun， I.A. 1965 Handbook of mathematical functions. New York: Dover.   
Apostol, T.M. 1976 Introduction to analytic number theory. New York: Springer-Verlag.   
van der Blij,F. 1949 On the theory of quadratic forms.Ann.Math.50,875-883.   
Braun,Hel. 1941 Zur theorie der hermitschen Formen.Abh.Math.Sem.Hansischen Univ.14, 61-150.   
Carlitz,L._1954 Representations by quadratic forms in a finite field. Duke math.J. 21, 123-137.   
Carlitz,L.& Hodges,J.H. I955 Representations by Hermitian forms in a finite feld.Duke math.J.22,393-405.   
Cassels, J. W. S. 1978 Rational quadratic forms. New York: Academic Press.   
Chevalley, C. 1955 Sur certains groupes simples. Tohoku Math. J. 7,14-66.   
Conway,J.H.& Sloane,N.J.A. 1982a On the enumeration of lattices of determinant one. J.Number Theory 15,83-94.   
Conway,J. H. & Sloane,N. J. A. 1982b The unimodular lattces of dimension up to 23 and the Minkowski-Siegel mass constants.Eur.J.Combinatorics 3,219-231   
Conway， J.H.& Sloane, N.J.A. 1988a Sphere packings, lattices and groups. New York: Springer: Verlag. (SLG.)   
Conway,J.H.& Sloane,N.J. A. 1988b Low-dimensional latices. I. Quadratic forms of small determinant.Proc.R. Soc.Lond. A 418,17-41.   
Conway, J. H.& Sloane,N. J.A.1988c Low-dimensional latices. II. Subgroups of $\mathcal { G L } ( \boldsymbol { n } , \mathbb { Z } )$ Proc.R. Soc.Lond.A 419,29-68   
Conway,J.H.& Sloane,N.J.A. $\mathbf { I 9 8 8 } d$ Low-dimensional lattices.III.Perfect forms.Proc.R. Soc.Lond.A. 418,43-80.   
Cresse,G.H. 1919 Number of classes of binary quadratic forms with integral coeffcients. Vol.3,ch.5 of Dickson (1919).   
Dickson,L.E. 1919 History of the theory of numbers. (3 volumes.) Washington, D.C.: Carnegie Institute.   
Dieudonne, J.A. 1955 La geometrie des groupes classiques. New York: Springer-Verlag.   
Glaisher,J.W.L.1894 Introduction to the collected mathematical papers of Henry J.S. Smith.In Smith (1894),vol. 1,pp.lxi-xcv.   
Hardy,G.H. 19zo Some famous problems of the theory of numbers and in particular Waring's problem. Oxford: Clarendon Press. (Coll. Papers I, 645-679 (1966).).   
Hodges,J.H.1955Representations by bilinear forms in a finite field. Duke math. J.22, 497-509.   
Jones,B.W. 1944 A canonical rational form for the ring of 2-adic integers. Duke math. J.11, 715-727.   
Jowett,B. 1894 Recollections of Professor Smith. In Smith (1894), vol. 1, pp. xxxvii-xlv.   
Kneser, M. 1967 Semi-simple algebraic groups.In Algebraic number theory (ed. J.W. S. Cassels & A.Frohlich), pp.250-265. New York: Academic Press.   
Kneser,M.& Puppe, D. 1953 Quadratische Formen und Verschlingungsinvarianten von Knoten. Math. Z. 58,376-384.   
Ko, C.1938 Determination of the class number of positive quadratic forms in nine variables with determinant unity.J.Lond.math. Soc.13,102-110.   
Ko,C. I939 On the positive definite quadratic forms with determinant unity. Acta Arith. 3, 79-85.   
Landau, E. 1927 Vorlesungen über Zahlentheorie. Leipzig: Hirzel. (New York: Chelsea (1950).)   
Magnus, W. 1937 Uber die Anzahl der in einem Geschlecht enthaltenen Klassen von positivdefiniten quadratischen Formen.Math.Annln 114,465-475；115 (1938),643-644. (Coll. Papers,1984,pp.163-175.)   
Milnor,J. & Husemoller,D. 1973 Symmetric bilinear forms. New York: Springer-Verlag.   
Minkowski, H. 1884 Memoire sur la theorie des formes quadratiques. Mem. divers'savants Institut de France,vol.29,no.2. (Ges. Abh. 1,3-144 (1911).)   
Minkowski, H. 1885 Untersuchungen iber quadratischer Formen. Bestimmung der Anzahl verschiedener Formen, welche ein gegebenes Genus enthalt. Konigsberg: Inauguraldissertation. (Acta Math.(1885),7,201-258;Ges.Abhand.1,157-202 (1911).)   
O'Meara, O.T. 1976 Hilbert's eleventh problem: the arithmetic theory of quadratic forms. Proc. Symp. pure Math. 28,379-400.   
Pall, G.1945 The arithmetical invariants of quadratic forms. Bull.Am. math. Soc. 51, 185-197.   
Pall,G. 1965 The weight of a genus of positive $\mathscr { n }$ -ary quadratic forms. Proc. Symp. pure Math. 8, 95-105.   
Pfeuffer, H. 1969 Bemerkung zur Berechnung dyadischer Darstellungsdichten einer quadratischen Form über algebraischen Zahlkorpern. $J$ reine angew.Math.236,219-220.   
Pfeufer, H. 197Ia Quadratsummen in totalreelln algebraischen Zahlkorpern.J. reine angew. Math.249,208-216.   
Pfeuffer,H.1971b Einklassige Geschlechter totalpositiver quadratischer Formen in totalreellen algebraischen Zahlkorpern.J.Number Theory 3,371-411.   
Reiner,Irma I956 On the two-adic density of representations by quadratic forms.Pacific J. Math.6,753-762.   
Serre,J.-P. 197o Cours d'arithmetique. Paris: Presses Universitaires de France. (English translation 1973.New York:Springer-Verlag.)   
Serre,J.-P. 1983 Resumé des cours de 1982-1983.Annuaire du College de France,pp.81-86. (Oeuvres,III (1986),669-674.)   
Siegel, C.L. 1935 Uber die analytische Theorie der quadratischen Formen. Ann. Math.36, 527-606 (Siegel, I (1966),326-405).   
Siegel, C.L. i966 Gesammelte abhandlungen. (Four volumes.) New York: Springer-Verlag.   
Sloane, N.J.A. 1979 Self-dual codes and lattices. Proc. Symp. pure Math. 34, 273-308.   
Smith,H.J.S. 1867 On the orders and genera of quadratic forms containing more than three indeterminates.Proc.R.Soc.Lond.16,197-208.(Also in Smith (1894)，vol.1, pp.510-523.)   
Smith, H.J. S. $\tt { I 8 8 4 }$ Mémoire sur la représentation des nombres par des sommes de cinq carreés.Mem.divers savants Institut de France,vol.29,no.1. (Also in Smith (1894),vol.2, pp.623-680.)   
Smith,H.J.S.1894 Collected mathematical papers.Reprinted 1979.New York:Chelsea Publ. Co., 2 vols.   
Tamagawa,T. 1966 Adeles.Proc. Symp.pure Math.9,113-121.   
Watson,G.L. 1976 The 2-adic density of a quadratic form.Mathematika 23,94-106.   
Weil,A. 1962 Sur la theorie des formes quadratiques. Colloque sur la Theorie des Groupes Algebriques,pp. 9-22.Brussels: C.B.R.M.(Oeuvres Sci.II (1979),471-484.)