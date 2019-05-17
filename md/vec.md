---
geometry: "left=1.5cm,right=1.5cm,top=2cm,bottom=2cm"
classoption: twocolumn
pagetitle: Linear Algebra Notes
header-includes: |
    \usepackage{euler}
    \pagestyle{headings}
---

# Definitions

## Vector Space

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

## Linear Combination

A linear combination of a list of vectors $v_1, \ldots, v_n$ is itself a vector, taking the form:
$$
    a_1v_1 + \ldots + a_mv_m
$$
where each $a_1, \ldots a_n \in \mathbb{R}$


## Span

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


## Linearly Independent

For $v_1,\ldots,v_n \in V$ and $a_1,\ldots,a_n \in \mathbb{R}$ such that:
$$
    a_1v_1 + \cdots + a_nv_n = 0
$$
The list of vectors $v_1,\ldots,v_n$ is called **linearly independent** when
$$
    a_1=\cdots=a_n=0
$$
for all possible values of $v_1,\ldots,v_n$.



## Inner Product

TODO




# Proofs

## Law of Cosines

TODO

## Triangle Inequality

TODO

### Cauchy-Schwartz Inequality

TODO
