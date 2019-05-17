---
geometry: "left=1.5cm,right=1.5cm,top=2cm,bottom=2cm"
classoption: twocolumn
pagetitle: Linear Algebra Notes
header-includes: |
    \usepackage{euler}
    \pagestyle{headings}
---


Definitions
=====================================================================

Vector Space
---------------------------------------------------------------------

Assume that $u,v,w$ are vectors in $V$, and $a,b,c$ are scalars in $\mathbb{R}$.  A **vector space** is a set $V$ with the following properties:

**Commutativity**:  

* $u+v=v+u$

**Associativity**:  

* $(u+v)+w = u+(v+w)$
* $(ab)v=a(bv)$

**Additive Identity**:

* there exists $0 \in V$ such that $v+0=v$ for all $v\in V$

**Multiplicative Identity**:  

* for all $v\in V$, there exists $w\in V$ such that $v+w=0$

**Distributive Properties**:

* $a(u+v)=au+av$
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

The set of all linear combinations of a list of vectors $v_1, \ldots, v_n$ is called the **span** of $v_1, \ldots, v_n$, or Span$(v_1, \ldots, v_n)$.  Defined as:
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

The **Standard Basis** of the vector space $\mathbb{R^n}$ is
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
    \text{dim } \mathbb{R^n} = n
$$



Linear Map
---------------------------------------------------------------------

A linear map from vector space $V$ to vector space $W$ is a function $T:V\to W$ with the following properties:

**Additivity**

* $T(u+v) = Tu + Tv$ for all vectors $u,w \in V$

**Homogeneity**

* $T(av) = a(Tv)$ for all $a\in \mathbb{R}$ and all $v\in V$


## Inner Product

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


## Norm

The norm of a vector $v$ is defined:
$$
    \| x \| = \sqrt{{x_1}^2 + \ldots + {x_n}^2}
$$




## Linear Maps and Matrices

Suppose $M$ is a linear map $f: \mathbb{R}^a \to \mathbb{R}^b$, then $M$ can be written as $b$-by-$a$ matrix:
$$
    \begin{bmatrix}
        x_{1,1} & \cdots & x_{1, a} \\
        \vdots & \vdots & \vdots \\
        x_{b, 1} & \cdots & x_{b, a}
    \end{bmatrix}
$$
