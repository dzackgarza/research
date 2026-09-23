## Appendix: Root Systems

#### Examples of Specific Root Systems {#sec:root-lattice-conventions}

##### $A_4$

The relevant Euclidean space is $\EE_{A_4} = \{ x \in \RR^5 : x_1+x_2+x_3+x_4+x_5=0 \}$ with
$$
\Phi(A_4)\colon
\begin{cases}
\alpha_1= e_1 - e_2 \\
\alpha_2= e_2 - e_3 \\
\alpha_3= e_3 - e_4 \\
\alpha_4= e_4 - e_5
\end{cases}
\qquad 
G_{A_4(-1)} =
\begin{pmatrix}
-2 & 1 & 0 & 0 \\
1 & -2 & 1 & 0 \\
0 & 1 & -2 & 1 \\
0 & 0 & 1 & -2
\end{pmatrix}
$$
By convention, we take $A_n$ to mean $A_n(-1)$.
This has Coxeter diagram

\begin{align*}
A_4:\quad \dynkin[mark=o,scale=3]{A}{4}
.\end{align*}


##### $B_4$

Roots live in $\EE_{B_4} = \RR^4$, and
$$
\Phi(B_4)\colon
\begin{cases}
\alpha_1 = e_1 - e_2 \\
\alpha_2 = e_2 - e_3 \\
\alpha_3 = e_3 - e_4 \\
\alpha_4 = e_4
\end{cases}
\qquad
G_{B_4(-1)} =
\begin{pmatrix}
-2 & 1 & 0 & 0 \\
1 & -2 & 1 & 0 \\
0 & 1 & -2 & 1 \\
0 & 0 & 1 & -1
\end{pmatrix}
$$
Because we typically work with roots with $v^2 = -2$ or $-4$, we often replace $B_n$ with $B_n(2)$, where for example
$$
G_{B_4(-2)} =
\begin{pmatrix}
-4 & 2 & 0 & 0 \\
2 & -4 & 2 & 0 \\
0 & 2 & -4 & 2 \\
0 & 0 & 2 & -2
\end{pmatrix}
$$
By convention, we thus take $B_n$ to mean $B_n(-2)$, and identify the following Coxeter diagram:

\begin{align*}
B_4: \quad 
\dynkin[arrows=false,scale=3]{B}{***o}
.\end{align*}


##### $C_4$

Set $\EE_{C_4} = \RR^4$, then
$$
\Phi(C_4)\colon
\begin{cases}
\alpha_1 = e_1 - e_2 \\
\alpha_2 = e_2 - e_3 \\
\alpha_3 = e_3 - e_4 \\
\alpha_4 = 2e_4
\end{cases}
\qquad
G_{C_4(-1)} =
\begin{pmatrix}
-2 & 1 & 0 & 0 \\
1 & -2 & 1 & 0 \\
0 & 1 & -2 & 2 \\
0 & 0 & 2 & -4
\end{pmatrix}
$$
We again take $C_n$ to mean $C_n(-1)$ by convention, with Coxeter diagram

\begin{align*}
C_4:\quad \dynkin[arrows=false,scale=3]{C}{ooo*}
.\end{align*}


##### $D_4$

Roots live in $\EE_{D_4} = \RR^4$ and
$$
\Phi(D_4)\colon
\begin{cases}
\alpha_1 = e_1 - e_2 \\
\alpha_2 = e_2 - e_3 \\
\alpha_3 = e_3 - e_4 \\
\alpha_4 = e_3 + e_4
\end{cases}
\qquad
G_{D_4(-1)} =
\begin{pmatrix}
-2 & 1 & 0 & 0 \\
1 & -2 & 1 & 1 \\
0 & 1 & -2 & 0 \\
0 & 1 & 0 & -2
\end{pmatrix}
$$
We take $D_n$ to mean $D_n(-1)$, and identify the Coxeter diagram as:
 
\begin{align*}
D_4:\quad \dynkin[mark=o,scale=3]{D}{4}
.\end{align*}

##### $E_6$

Roots live in $\EE_{E_6} = \{ x \in \RR^8 : x_1+\cdots+x_8=0 \}$ with 
$$
\Phi(E_6)\colon\,\,
\begin{cases}
\alpha_1 = e_1 - e_2 \\[6pt]
\alpha_2 = e_2 - e_3 \\[6pt]
\alpha_3 = e_3 - e_4 \\[6pt]
\alpha_4 = e_4 - e_5 \\[6pt]
\alpha_5 = e_5 - e_6 \\[6pt]
\alpha_6 = \tfrac{1}{2}(e_1 + e_2 + e_3 + e_4 - e_5 - e_6 - e_7 - e_8)
\end{cases},
G_{E_6(-1)} =
\begin{pmatrix}
-2 & 1  & 0  & 0  & 0  & 0 \\
1  & -2 & 1  & 0  & 0  & 0 \\
0  & 1  & -2 & 1  & 0  & 0 \\
0  & 0  & 1  & -2 & 1  & -1 \\
0  & 0  & 0  & 1  & -2 & 0 \\
0  & 0  & 0  & -1 & 0  & -2
\end{pmatrix}
$$
We take $E_n$ to mean $E_n(-1)$, and identify the Coxeter diagram as:
\begin{align*}
E_6: \dynkin[mark=o,scale=2.5]{E}{6}
.\end{align*}


##### $F_4$

We take the simple roots

\begin{align*}
\begin{cases}
\alpha_1 = e_2 - e_3 \\
\alpha_2 = e_3 - e_4 \\
\alpha_3 = e_4 \\
\alpha_4 = {1\over 2}(e_1 - e_2 - e_3 - e_4)
\end{cases}
.\end{align*}

with the standard Gram matrix
$$
G_{F_4} = 
\begin{pmatrix}
2 & -1 & 0 & 0 \\
-1 & 2 & -1 & 0 \\
0 & -1 & 1 & -{1\over 2} \\
0 & 0 & -{1\over 2} & 1
\end{pmatrix}
$$
To work integrally, we rescale by $-2$:

\begin{align*}
G_{F_4(-2)} =
\begin{pmatrix}
-4 & 2 & 0 & 0 \\
2 & -4 & 2 & 0 \\
0 & 2 & -2 & 1 \\
0 & 0 & 1 & -2
\end{pmatrix}
.\end{align*}

and thus take $F_4$ to mean $F_4(-2)$, with Coxeter diagram

\begin{align*}
F_4: \quad 
\dynkin[arrows=false,scale=3]{F}{ooo*}
.\end{align*}


##### $G_2$

Roots live in $\EE_{G_2} = \{ x \in \RR^3 \st x_1 + x_2 + x_3 = 0 \}$ with simple roots and Gram matrix
$$
\Phi(G_2)\colon
\begin{cases}
\alpha_1 = e_1 - e_2 \\
\alpha_2 = -e_1 + 2e_2 - e_3
\end{cases}
\qquad
G_{G_2(-1)} =
\begin{pmatrix}
-2 & 3 \\
3 & -6
\end{pmatrix}
.$$
We thus take $G_2$ to mean $G_2(-1)$, and identify the Coxeter diagram as

\begin{align*}
G_2:\quad 
\dynkin[arrows=false,label,labels={,-6},scale=4,text style/.style={scale=1.2}]{G}{o*}
.\end{align*}



#### Root Lattice Conventions {#section-root-lattice-conventions}

To fix conventions, we record here Bourbaki's conventions for these Dynkin diagrams and the corresponding simple roots.
The Euclidean embeddings can be used to compute the following invariants in all types, which we show below.
Note that for $D_n$, $A_L = \ZZ_{2^2}$ when $n$ is odd, and $A_L = (\ZZ_2)^2$ when $n$ is even.

|  | $A_n$ | $D_n$ | $E_6$ | $E_7$ | $E_8$ |
|---|---|---|---|---|---|
| $\rank(L) = |\Phi(L)|$ | $n$ | $n$ | $2 \cdot 3$ | $7$ | $2^3$ |
| $|R(L)|$ | $n(n+1)$ | $2n(n-1)$ | $2^3 \cdot 3^2$ | $2 \cdot 3^2 \cdot 7$ | $2^4 \cdot 3 \cdot 5$ |
| $W(L)$ | $S_{n+1}$ | $(\ZZ_2)^{n-1} \rtimes S_n$ | $W(E_6)$ | $W(E_7)$ | $W(E_8)$ |
| $|W(L)|$ | $(n+1)!$ | $2^{n-1}\cdot n!$ | $2^7 \cdot 3^4 \cdot 5$ | $2^{10} \cdot 3^4 \cdot 5 \cdot 7$ | $2^{14} \cdot 3^5 \cdot 5^2 \cdot 7$ |
| $A_L$ | $\ZZ_{n+1}$ | $\ZZ_{2^2}$ or $\ZZ_2^2$ | $\ZZ_3$ | $\ZZ_2$ | $\{0\}$ |
| $\disc(L)$ | $n+1$ | $2^2$ | $3$ | $2$ | $1$ |

: Simply Laced Root Lattices (A, D, E types)

|  | $B_n$ | $C_n$ | $F_4$ | $G_2$ |
|---|---|---|---|---|
| $\rank(L) = |\Phi(L)|$ | $n$ | $n$ | $2^2$ | $2$ |
| $|R(L)|$ | $2n^2$ | $2n^2$ | $2^4 \cdot 3$ | $2^2 \cdot 3$ |
| $W(L)$ | $\ZZ_2^n \rtimes S_n$ | $\ZZ_2^n \rtimes S_n$ | $W(F_4)$ | $W(G_2)$ |
| $|W(L)|$ | $2^n \cdot n!$ | $2^n n!$ | $2^7 \cdot 3^2$ | $2^2 \cdot 3$ |
| $A_L$ | $\ZZ_2$ | $\ZZ_2$ | $\{0\}$ | $\ZZ_3$ |
| $\disc(L)$ | $2$ | $2$ | $1$ | $3$ |

: Non-Simply Laced Root Lattices (B, C, F, G types)

We now record explicit representatives for the simple roots of each lattice, their Gram matrix, and the associated Coxeter diagrams:

#### Types A,B,C, D


\begin{align*}
A_n:\,\,
\begin{cases}
\alpha_1 &= e_1 - e_2 \\
\alpha_2 &= e_2-e_3 \\
\vdots & \vdots \\
\alpha_n &= e_n - e_{n+1},
\end{cases}
\quad
G_{A_n} &=
\begin{pmatrix}
2 & -1 & \cdot & \cdots & \cdot \\
-1 & 2 & \ddots & \cdots & \cdot \\
\cdot & \ddots & \ddots & \ddots & \vdots \\
\vdots & \cdots & \ddots & 2 & -1 \\
\cdot & \cdots & \cdot & -1 & 2
\end{pmatrix} \\
& \hspace{-8em}
\raisebox{0.75em}{$A_n$:\,\,} \dynkin[mark=o, labels={\alpha_1,\alpha_2,,\alpha_n}, label directions={above,above,,above}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] A{} \\[1em]
B_n:\,\,
\begin{cases}
\alpha_1 &= e_1 - e_2 \\
\alpha_2 &= e_2 - e_3 \\
\vdots & \vdots \\
\alpha_{n-1} &= e_{n-1} - e_n \\
\alpha_n &= e_n
\end{cases},
\quad
G_{B_n} &=
\begin{pmatrix}
2 & -1 & \cdot & \cdot & \cdots & \cdot & \cdot \\
-1 & 2 & \ddots & \cdot & \cdots & \cdot & \cdot \\
\cdot & \ddots & \ddots & \ddots & \cdots & \cdot & \cdot \\
\vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\
\cdot & \cdot & \cdots & \ddots & 2 & -1 \\
\cdot & \cdot & \cdots & \cdot & -1 & 1
\end{pmatrix} \\
& \hspace{-8em} 
\raisebox{0.75em}{$B_n(2)$:\,\,}\dynkin[arrows=false, labels={\alpha_1,\alpha_2,\alpha_{n-1}, \alpha_n}, label directions={above,above,above, above}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] B{**.*o} \\[1em]
C_n:\,\,
\begin{cases}
\alpha_1 &= e_1 - e_2 \\
\alpha_2 &= e_2 - e_3 \\
\vdots & \vdots \\
\alpha_{n-1} &= e_{n-1} - e_n \\
\alpha_n &= 2e_n,
\end{cases}
\quad
G_{C_n} &=
\begin{pmatrix}
2 & -1 & \cdot & \cdot & \cdots & \cdot \\
-1 & 2 & \ddots & \cdot & \cdots & \cdot  \\
\cdot & \ddots & \ddots & \ddots & \cdots & \cdot \\
\vdots & \vdots & \ddots & 2 & -1 & \vdots  \\
\cdot & \cdot & \cdots & -1 & 2 & -2 \\
\cdot & \cdot & \cdots & \cdot & -2 & 4
\end{pmatrix} \\
& \hspace{-8em} 
\raisebox{0.75em}{$C_n$:\,\,}\dynkin[arrows=false, labels={\alpha_1,\alpha_2,\alpha_{n-1}, \alpha_n}, label directions={above,above,above, above}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] C{oo.o*} \\[1em]
\end{align*}

\begin{align*}
\hspace{-8em}
D_n:\,\,
\begin{cases}
\alpha_1 &= e_1 - e_2 \\
\alpha_2 &= e_2 - e_3 \\
\vdots & \vdots \\
\alpha_{n-2} &= e_{n-2} - e_{n-1} \\
\alpha_{n-1} &= e_{n-1} - e_n \\
\alpha_n &= e_{n-1} + e_n,
\end{cases}
\,\,\qquad\qquad
G_{D_n} =
\begin{pmatrix}
2 & -1 & \cdot & \cdot & \cdots & \cdot & \cdot & \cdot \\
-1 & 2 & \ddots & \cdot & \cdots & \cdot & \cdot & \cdot \\
\cdot & \ddots & \ddots & \ddots & \cdots & \cdot & \cdot & \cdot \\
\vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots & \vdots \\
\cdot & \cdot & \cdots & \ddots & 2 & -1 & -1 \\
\cdot & \cdot & \cdots & \cdot & -1 & 2 & \cdot \\
\cdot & \cdot & \cdots & \cdot & -1 & \cdot & 2
\end{pmatrix}
  \qquad\qquad\qquad\qquad\\
\hspace{-26em}
\raisebox{0.75em}{$D_n$:\,\,}
  \dynkin[labels={\alpha_1,\alpha_2,\alpha_{n-2},\alpha_{n-1}, \alpha_{n}}, label directions={above,above,above left,above right,below right}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] D{oo.ooo} \hspace{10em} \\[1em]
%
\hline \\
  \hspace{-8em}
E_6:\,\,
\begin{cases}
\alpha_1 &= \tfrac{1}{2}(e_1 - e_2 - e_3 - e_4 - e_5 - e_6 - e_7 + e_8) \\
\alpha_2 &= e_1 + e_2 \\
\alpha_3 &= -e_1 + e_2 \\
\alpha_4 &= -e_2 + e_3 \\
\alpha_5 &= -e_3 + e_4 \\
\alpha_6 &= -e_4 + e_5,
\end{cases}
\,\,
G_{E_6} =
\begin{pmatrix}
2 & \cdot & -1 & \cdot & \cdot & \cdot \\
\cdot & 2 & \cdot & -1 & \cdot & \cdot \\
-1 & \cdot & 2 & -1 & \cdot & \cdot \\
\cdot & -1 & -1 & 2 & \ddots & \cdot \\
\cdot & \cdot & \cdot & \ddots & \ddots & -1 \\
\cdot & \cdot & \cdot & \cdot & -1 & 2
\end{pmatrix}
 \\
 \hspace{-26em}
\raisebox{0.75em}{$E_6$:\,\,}
  \dynkin[mark=o, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4,\alpha_5,\alpha_6}, label directions={below,above,below,below,below,below}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] E6  \hspace{12em} \\[1em]
\end{align*}

#### Type E

\begin{align*}
E_7:\,\,
\begin{cases}
\alpha_1 &= \tfrac{1}{2}(e_1 - e_2 - e_3 - e_4 - e_5 - e_6 - e_7 + e_8) \\
\alpha_2 &= e_1 + e_2 \\
\alpha_3 &= -e_1 + e_2 \\
\alpha_4 &= -e_2 + e_3 \\
\alpha_5 &= -e_3 + e_4 \\
\alpha_6 &= -e_4 + e_5 \\
\alpha_7 &= -e_5 + e_6
\end{cases},
\quad
G_{E_7} &=
\begin{pmatrix}
2 & \cdot & -1 & \cdot & \cdot & \cdots & \cdot \\
\cdot & 2 & \cdot & -1 & \cdot & \cdots & \cdot \\
-1 & \cdot & 2 & -1 & \cdot & \cdots & \cdot \\
\cdot & -1 & -1 & 2 & -1 & \cdots & \cdot \\
\cdot & \cdot & \cdot & -1 & 2 & \ddots & \vdots \\
\vdots & \vdots & \vdots & \vdots & \ddots & \ddots & -1 \\
\cdot & \cdot & \cdot & \cdot & \cdots & -1 & 2
\end{pmatrix} \\
& \hspace{-16em}
\raisebox{0.75em}{$E_7$:\,\,}
\dynkin[mark=o, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4,\alpha_5,\alpha_6,\alpha_7}, label directions={below,above,below,below,below,below,below}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] E7 &\\[1em]
%
\hline \\
E_8:\,\,
\begin{cases}
\alpha_1 &= \tfrac{1}{2}(e_1 - e_2 - e_3 - e_4 - e_5 - e_6 - e_7 + e_8) \\
\alpha_2 &= e_1 + e_2 \\
\alpha_3 &= -e_1 + e_2 \\
\alpha_4 &= -e_2 + e_3 \\
\alpha_5 &= -e_3 + e_4 \\
\alpha_6 &= -e_4 + e_5 \\
\alpha_7 &= -e_5 + e_6 \\
\alpha_8 &= -e_6 + e_7
\end{cases},
\quad
G_{E_8} &=
\begin{pmatrix}
2 & \cdot & -1 & \cdot & \cdot & \cdots & \cdot \\
\cdot & 2 & \cdot & -1 & \cdot & \cdots & \cdot \\
-1 & \cdot & 2 & -1 & \cdot & \cdots & \cdot \\
\cdot & -1 & -1 & 2 & -1 & \cdots & \cdot \\
\cdot & \cdot & \cdot & -1 & 2 & \ddots & \vdots \\
\vdots & \vdots & \vdots & \vdots & \ddots & \ddots & -1 \\
\cdot & \cdot & \cdot & \cdot & \cdots & -1 & 2
\end{pmatrix} \\
& \hspace{-16em}
\raisebox{0.75em}{$E_8$:\,\,}
\dynkin[mark=o, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4,\alpha_5,\alpha_6,\alpha_7,\alpha_8}, label directions={below,above,below,below,below,below,below,below}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] E8 
\end{align*}

#### Types $F_4$ and $G_2$

\begin{align*}
F_4:\,\,
\begin{cases}
\alpha_1 &= e_2 - e_3 \\
\alpha_2 &= e_3 - e_4 \\
\alpha_3 &= e_4 \\
\alpha_4 &= \frac{1}{2}(e_1 - e_2 - e_3 - e_4),
\end{cases}
\quad
G_{F_4} &=\begin{pmatrix}
2 & -1 & \cdot & \cdot \\
-1 & 2 & -1 & \cdot \\
\cdot & -1 & 1 & -\frac{1}{2} \\
\cdot & \cdot & -\frac{1}{2} & 1
\end{pmatrix} \\
& \hspace{-12em}
\raisebox{0.75em}{$F_4(2)$:\,\,}
\dynkin[arrows=false, labels={\alpha_1,\alpha_2,\alpha_3,\alpha_4}, label directions={above,above,above,above}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] F{**oo} \\[1em]
%
\hline \\
G_2:\,\,
\begin{cases}
\alpha_1 &= e_2 - e_3 \\
\alpha_2 &= e_1 - 2e_2 + e_3,
\end{cases}
\quad
G_{G_2} &=\begin{pmatrix}
2 & -3 \\
-3 & 6
\end{pmatrix} \\
& \hspace{-8em}
\raisebox{0.75em}{$G_2$:\,\,}\dynkin[arrows=false, labels={\alpha_1,\alpha_2}, label directions={above,above}, scale=4, text style/.style={scale=1.2}, label distance=0.3em] G{*o}
\end{align*}
