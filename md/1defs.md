---
geometry: "left=1.5cm,right=1.5cm,top=2cm,bottom=2cm"
classoption: twocolumn
pagetitle: Linear Algebra Notes
author: Achenbach
numbersections: true
header-includes: |
    \usepackage{euler}
    \pagestyle{headings}
    \usepackage{cancel}
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \fancyfoot[C]{}
    \fancyfoot[L]{\scshape{a\ccPublicDomain henbach}}
    \fancyfoot[R]{\footnotesize{\ttfamily{github.com/fractalbach/linear-algebra-notes}}}
    \renewcommand{\footrulewidth}{0.4pt}
    \usepackage{ccicons}
---


Definitions
=====================================================================

Vector Space
---------------------------------------------------------------------

Assume that $v,x,y,z$ are vectors in $V$, and $a,b,c$ are scalars in $\mathbb{R}$.  A **vector space** is a set $V$ with the following properties:

Commutativity:  

* $x+y=y+x$

Associativity:  

* $(x+y)+z = x+(y+z)$
* $(ab)v=a(bv)$

Additive Identity:

* there exists $0 \in V$ such that $v+0=v$ for all $v\in V$

Additive Inverse:

* for all $v\in V$, there exists $x\in V$ such that $v+x=0$

Multiplicative Identity:  

* $1v = v$

Distributive Properties:

* $a(x+y)=ax+ay$
* $(a+b)v=av+bv$


Linear Combination
---------------------------------------------------------------------

A linear combination of a list of vectors $v_1, \ldots, v_n$ is itself a vector, taking the form:
$$
    a_1v_1 + \ldots + a_mv_m
$$
where each $a_1, \ldots a_n \in \mathbb{R}$


Span
---------------------------------------------------------------------

The set of all linear combinations of a list of vectors $v_1, \ldots, v_n$ is called the **span** of $v_1, \ldots, v_n$, and is defined:
$$
    \text{span}(v_1,\ldots,v_n) =
    \left\{
        a_1v_1 + \cdots + a_nv_n
        \ : \
        a_1,\ldots,a_m \in \mathbb{R}
    \right\}
$$
If the span is equal to some space $\text{span}(v_1,\ldots,v_n)=V$, then you could say that $v_1,\ldots,v_n$ **spans** $V$.


Linearly Independent
---------------------------------------------------------------------

For $v_1,\ldots,v_n \in V$ and $a_1,\ldots,a_n \in \mathbb{R}$ such that:
$$
    a_1v_1 + \cdots + a_nv_n = 0
$$
The list of vectors $v_1,\ldots,v_n$ is called **linearly independent** when
$$
    a_1=\cdots=a_n=0
$$
for all possible values of $v_1,\ldots,v_n$.


Basis
---------------------------------------------------------------------

A **basis** of V is a list of vectors in $V$ that is both linearly independent and spans $V$.

The **Standard Basis** of the vector space $\mathbb{R}^n$ is
$$
    (1,0,\ldots,0) \space , \space
    (0,1,\ldots,0) \space , \space
    \ldots \space , \space  
    (0,0,\ldots,1)
$$
which could also be written, using matrix bracket notation, as:
$$
    \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix},
    \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix},
    \ldots,
    \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}
$$

Dimension
---------------------------------------------------------------------

The dimension of a vector space is the length of any basis of the vector space.  For example,
$$
    \text{dim } \mathbb{R}^n = n
$$


Inner Product
---------------------------------------------------------------------

For a pair of vectors $u,v \in V$ in the same vector space (they are both in $\mathbb{R}^n$ for example), the Inner Product is defined as:
$$
    u \cdot v = u_1v_1 + ... + u_nv_n
$$
which is also sometimes written using angular brackets:
$$
    \langle u, v \rangle
$$
Keep in mind that the dimension of $u$ and $v$ must be the same.  Using matrix dimension notation:
$$
    u_{\{n \times 1\}} \cdot v_{\{n \times 1\}}
$$

The **Inner Product** is also a function $f: (\mathbb{R}^n, \mathbb{R}^n) \to \mathbb{R}$.  The input is an ordered pair of vectors, and the output is a number.  Inner products have the following properties:

Positivity:

* $\langle v, v \rangle \geq 0$ for all $v \in V$

Definiteness:

* $\langle v, v \rangle = 0$ if and only if $v=0$

Additivity in First Slot:

* $\langle u+v, w \rangle = \langle u,w \rangle + \langle v,w \rangle$ for all $u,v,w \in V$

Homogeneity in First Slot:

* $\langle au, v \rangle = a \langle u,v \rangle$ for all $a \in \mathbb{R}$ and all $u,v \in V$


In another definition of the Inner Product, the concepts of "additivity" and "homogeneity" are combined into a concept called "linearity".  **Bilinearity** is when there is linearity in both the First and Second slots.  Additionally, there is a concept called **Symmetry** for all real numbers.

For $x,y,z \in V$ and $a,b \in \mathbb{R}$:

Bilinearity:

* Additivity and Homogeneity in First and Second Slot:
* $\langle ax+by,\space z \rangle = a \langle x,z \rangle + b \langle y,z \rangle$
* $\langle x ,\space ay+bz \rangle = a \langle x,y \rangle + b \langle x,z \rangle$

Symmetry:

* $\langle x,y \rangle = \langle y,x \rangle$



Norm
---------------------------------------------------------------------
The Norm of a vector $x$ is defined as the square root inner product of $x$ with itself:
$$
    \|x\| = \sqrt{ \langle x,x \rangle }
$$
The Euclidean Norm, also called 2-norm, is defined:
$$
    {\| x \|}_2 = \sqrt{ {x_1}^2 + \ldots + {x_n}^2 }
$$
which has the following properties:

Positivity:

* $\|x\| \geq 0$
* $\|x\|=0$ if and only if $x = 0$

Homogeneity:

* $\|ax\| = |a| \space \|x\|$ for all $a \in \mathbb{R}$

Triangle Inequality:

* $\|x+y\| \leq \|x\| + \|y\|$


Orthogonal
---------------------------------------------------------------------

Two vectors $u,v \in V$ are called **orthogonal** if the inner product between them is 0,
$$
    \langle u, v \rangle = 0
$$
you could also say "$u$ is orthogonal to $v$".  Orthogonal is another way of saying "at right angles to each other", or "perpendicular".

Linear Map
---------------------------------------------------------------------

A linear map from vector space $V$ to vector space $W$ is a function $T:V\to W$ with the following properties:

Additivity:

* $T(u+v) = Tu + Tv$ for all vectors $u,w \in V$

Homogeneity:

* $T(av) = a(Tv)$ for all $a\in \mathbb{R}$ and all $v\in V$



Linear Maps and Matrices
---------------------------------------------------------------------

Suppose $M$ is a linear map $f: \mathbb{R}^a \to \mathbb{R}^b$, then $M$ can be written as $b$-by-$a$ matrix:
$$
    \begin{bmatrix}
        x_{1,1} & \cdots & x_{1, a} \\
        \vdots & \vdots & \vdots \\
        x_{b, 1} & \cdots & x_{b, a}
    \end{bmatrix}
$$
