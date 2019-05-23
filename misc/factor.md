---
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
classoption: twoside
fontsize: 12pt
header-includes: |
    \usepackage{euler}
    \pagestyle{headings}
    \usepackage{cancel}
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \fancyhead{}
    \fancyhead[OR, EL]{\thepage}
    \fancyhead[C]{\scshape{Prime Factor Vector Space}}
    \fancyfoot[C]{}
    \fancyfoot[L]{\scshape{achenbach}}
    <!-- \fancyfoot[R]{\footnotesize{\ttfamily{github.com/fractalbach/linear-algebra-notes}}} -->
    \renewcommand{\footrulewidth}{0.4pt}
---



# Prime Factor Space

$$
    \begin{bmatrix} 0 \\ 1 \\ 2 \\ 3 \\ 4 \\ \end{bmatrix}
    = 2^0 \cdot 3^1 \cdot 5^2 \cdot 7^3 \cdot 11^4
$$

# Definitions

Let $A$ represent an ordered set $(a_1, \ldots, a_n)$, and let:
$$
    P_A = 2^{a_1} \cdot 3^{a_2} \cdot 5 ^{a_3} \cdots {(p_n)}^{a_n}
$$
Where each of the factors is in the order set of Prime Numbers, and $p_n$ denotes the $n^{th}$ prime number.

To define the sets that these things are in:
$$
    A \in \mathbb{R}^n \text{ and } P_A \in \mathbb{R}
$$
For all $A \in \mathbb{R}^n$ and $c \in \mathbb{R}$:

Let Addition be defined:
$$
    P_A + P_B = P_{A+B}
$$
Let Multiplicative be defined:
$$
    P_A \cdot P_B = P_{AB}
$$
Let scalar addition be defined:
$$
    c + A =  P_{c+A} = 2^{c + a_1} \cdots {p_n}^{c + a_n}
$$

Let scalar multiplication be defined:
$$
    c \cdot A =  P_{cA} = 2^{c\cdot a_1} \cdots {p_n}^{c \cdot a_n}
$$

Let there exist a $\vec{0}$ such that:
$$
    \vec{0} = P_0 = 2^{0} \cdots {p_n}^{0} = 1
$$



# Proof of Vector Space

The goal is to show that our special $P$ is a vector space $V$

Commutative
---------------------------------------------------------------------

$A + B = B + A$ for all $A,B\in V$

*Proof*:

Let $A = (a_1, \ldots a_n)$, and $B = (b_1, \ldots b_n)$.
Then by MYDEF,
$$
\begin{aligned}
    A & = 2^{a_1} \cdots {p_n}^{a_n} \\
    B & = 2^{b_1} \cdots {p_n}^{b_n}
\end{aligned}
$$
Since addition of A and B is written like:
$$
    A+B =
    \left(\vphantom{\sum} 2^{a_1} \cdots {(P_n)}^{a_n} \right)
    \cdot
    \left(\vphantom{\sum} 2^{b_1} \cdots {(P_n)}^{b_n} \right)
$$
Since both sides are esssentially real numbers. Then you can rewrite the expression like this:
$$
    \left(\vphantom{\sum} 2^{b_1} \cdots {(P_n)}^{b_n} \right)
    \cdot
    \left(\vphantom{\sum} 2^{a_1} \cdots {(P_n)}^{a_n} \right)
    = B+A
$$
Thus,
$$
    A + B = B+A
$$

$\Box$

It might be easier to show that they become real numbers.
$$
\begin{aligned}
    A+B &= P_A \cdot P_B \\
    &= P_B \cdot P_A \\
    &= B+A
\end{aligned}
$$


Associative
---------------------------------------------------------------------

For all $A,B,C \in V$ and $a,b \in F$:

* $(A+B)+C = A + (B+C)$
* $(ab)A = a(bA)$

*Proof*

$$
\begin{aligned}
    (A + B) + C &=  (P_A \cdot P_B) \cdot P_C \\
    &= P_A \cdot (P_B \cdot P_C) \\
    &= A + (B + C)
\end{aligned}
$$
$\Box$


Additive Identity
---------------------------------------------------------------------

There exists an element $0 \in V$ such that $A+0 = A$ for all $A \in V$

*Proof*

This makes use of the definition of exponents.  All real numbers taken to the $0^{th}$ power equal to 1.
$$
\begin{aligned}
    A + 0 &= P_A \cdot P_0 \\
    &= P_A \cdot (2^0 \cdots {p_n}^0) \\
    &= P_A \cdot (1 \cdots 1) \\
    &= P_A  \cdot 1 \\
    &= P_A \\
    &= A
\end{aligned}
$$
$\Box$

Additive Inverse
---------------------------------------------------------------------
For every $A \in V$ there exists a $B \in V$ such that $A+B=\vec{0}$

*Proof*

Suppose $A = P_A$ and $B=P_{-A}$, Then:
$$
\begin{aligned}
    A + B &= P_A \cdot P_{-A} \\
    &=
        \left( \vphantom{\sum} 2^{a_1} \cdots {p_n}^{a_n} \right)
        \cdot
        \left( \vphantom{\sum} 2^{-a_1} \cdots {p_n}^{-a_n} \right)
    \\
    &=
        \left( \vphantom{\sum}
            2^{a_1} \cdot 2^{-a_1}
            \cdots
            {(p_n)}^{a_n} \cdot {(p_n)}^{-a_n}
        \right)
    \\
    &=
        \left( \vphantom{\sum}
            2^{a_1 - a_1} \cdots {p_n}^{a_n-a_n}
        \right)
    \\
    &=
        \left( \vphantom{\sum}
            2^{0} \cdots {p_n}^{0}
        \right)
    \\
    &=
    P_0 \\
    &= \vec{0}
\end{aligned}
$$
$\Box$

It's important to note at this point that $\vec{0}$, which is an ordered list of $0$s, becomes $P_0$, which is equal to $1$.

Just because it's always fun to write things like this:
$$
    \vec{0} = 1
$$
which is true only in our special Factor Space.




Multiplicative Identity
---------------------------------------------------------------------

$1A = A$ for all $A \in V$.

*Proof*

$$
\begin{aligned}
    1A &= P_{1A} \\
    &=
        \left( \vphantom{\sum}
            2^{1a_1} \cdots {p_n}^{1a_n}
        \right)
    \\
    &=
        \left( \vphantom{\sum}
            2^{a_1} \cdots {p_n}^{a_n}
        \right)
    \\
    &=
        P_A
    \\
    &=
        A
\end{aligned}
$$
$\Box$





Distributive
---------------------------------------------------------------------

For all $c,d\in F$ and $A,B \in V$,

* $c(A+B) = cA + cB$
* $(c+d)A = cA + dA$

*Proof Part 1*
$$
\begin{aligned}
    cA+cB &= P_{cA} + P_{cB} \\
    &= (2^{ca} \cdots {p_n}^{ca_n}) \cdot (2^{cb} \cdots {p_n}^{cb_n}) \\
    &= 2^{ca + cb} \cdots {p_n}^{ca + cb} \\
    &= 2^{c(a+b)} \cdots {p_n}^{c(a+b)} \\
    &= P_{c(A+B)} \\
    &= c(A+B)
\end{aligned}
$$
$\Box$

*Proof Part 2*
$$
\begin{aligned}
    (c+d)A &= P_{(c+d)A} \\
    &= 2^{(c+d)A} \cdots {p_n}^{(c+d)A} \\
    &= 2^{cA+dA} \cdots {p_n}^{cA+dA} \\
    &= 2^{cA} \cdot 2^{dA}  \cdots {p_n}^{cA}\cdot {p_n}^{dA} \\
    &= (2^{cA} \cdots {p_n}^{cA}) \cdot (2^{dA} \cdots {p_n}^{dA}) \\
    &= P_{cA} \cdot P_{dA} \\
    &= cA + dA
\end{aligned}
$$
$\Box$

# Extras

If $A$ is a list of positive integers, $A\in \mathbb{N}^n$, then
$$
    P_A \in \mathbb{Z}
$$
because of the Fundamental Theorem of Arithmetic.


$$
\begin{aligned}
\end{aligned}
$$


~~~python
def primes(x):
    print(2)
    primes = [2]
    n = 3
    while len(primes) < x:
        notPrime = False
        for p in primes:
            if n % p == 0:
                notPrime = True
                break
        if not notPrime:
            primes += [n]
            print(n)
        n += 1
    return primes
~~~
