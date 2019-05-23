# Linear Maps

Linear Maps Definitions
---------------------------------------------------------------------

A Linear Map from vector spaces $V$ to $W$ is a function $T:V \to W$ with the following properties:

Additivity

* $T(u+v) = Tu + Tv$ for all $u,v\in V$

Homogeneity

* $T(cv) = c(Tv)$ for all $c \in F$ and all $v\in V$

Scalar Addition

* $(S+T)(v) = Sv+Tv$

Scalar Multiplication

* $(cT)(v) = c(Tv)$

Product of Linear Map

* $(ST)(u) = ST(u)$





Algebraic Properties
---------------------------------------------------------------------

These properties can be derived from the Linear Map Definitions.

Associativity

* $(T_1 T_2) T_3 = T_1 (T_2 T_3)$

Identity

* $TI = IT = T$

Distributive Properties

* $(S_1 + S_2)T = S_1T + S_2T$
* $S(T_1 + T_2) = ST_1 + ST_2$





Linear Maps and Basis of domain
---------------------------------------------------------------------

Suppose some list of vectors $v_1, \ldots v_n$ is a basis $V$.

Therefore, there exists a unique linear map $T:V\to W$ such that
$$
    Tv_i = w_i
$$
for $i = 1,\ldots,n$ and $w$ is a list of vectors $w_i,\ldots,w_n$ in a different vector space $W$.


Matrix Multiplication as the Composition of Linear Functions
---------------------------------------------------------------------

Suppose there are two functions, $f$ and $g$.  

Let function $f$ be defined as $f: R^2 \to R^3$ such that,
$$
    f
    \left(
        \begin{bmatrix} x \\ y \end{bmatrix}
    \right)
    =
    \begin{bmatrix}
        0x + 1y \\
        2x + 3y \\
        4x + 5y
    \end{bmatrix}
    =
    \begin{bmatrix}
        0 & 1 \\
        2 & 3 \\
        4 & 5
    \end{bmatrix}
    \begin{bmatrix}
        x \\ y
    \end{bmatrix}
$$
for some values $x,y \in R$.

Let function $g$ be defined as $g: R^3 \to R^2$ such that,
$$
    g
    \left(
        \begin{bmatrix} x \\ y \\ z \end{bmatrix}
    \right)
    =
    \begin{bmatrix}
        1x + 2y + 3z \\
        4x + 5y + 6z
    \end{bmatrix}
    =
    \begin{bmatrix}
        1 & 2 & 3 \\
        4 & 5 & 6
    \end{bmatrix}
    \begin{bmatrix} x \\ y \\ z \end{bmatrix}
$$
for some different values of $x,y,z \in R$.

You could write these as a composition of functions,
$$
    f \circ g : R^2 \to R^3 \to R^2
$$
which just simplifies to:
$$
    f \circ g : R^2 \to R^2
$$
So let's create some example input so we can see what's going on here.  When composing functions, we don't actually care what the input is, but it helps for understanding.

Let our example input be a vector $a \in R^2$.  Let's rewrite our composition of functions in a way that looks more familiar,
$$
    (f \circ g )(a) = g(f(a))
$$

Take a look at what happens as the input is mapped to different sets through each function,
$$
\begin{aligned}
    a & \in R^2 \\
    f(a) & \in R^3 \\
    g(f(a)) & \in R^2
\end{aligned}
$$
Looking back at the definition of $f$, let's plug in the input $a$,
$$
    f(a)=
    \begin{bmatrix}
        0 & 1 \\
        2 & 3 \\
        4 & 5
    \end{bmatrix}
    \begin{bmatrix}
        a_1 \\ a_2
    \end{bmatrix}
$$
Looking back at the definition of $g$, let's put in $f(a)$,
$$
    g(f(a)) =
    \begin{bmatrix}
        1 & 2 & 3 \\
        4 & 5 & 6
    \end{bmatrix}
    \begin{bmatrix}
        0 & 1 \\
        2 & 3 \\
        4 & 5
    \end{bmatrix}
    \begin{bmatrix}
        a_1 \\ a_2
    \end{bmatrix}
$$
We have now created a new function!

To understand why multiplying matrices is still the composition of functions, consider how it looks when we remove $a$, and just focus on the matrices,
$$
    f \circ g =
    \begin{bmatrix}
        1 & 2 & 3 \\
        4 & 5 & 6
    \end{bmatrix}
    \begin{bmatrix}
        0 & 1 \\
        2 & 3 \\
        4 & 5
    \end{bmatrix}
$$
And finally, let's say that $A$ represents the first matrix, and $B$ represents the second matrix,
$$
    f \circ g =
    A B
$$


------

*Hardcore Way:*

Look back up at the definitions for $f$ and $g$.  Let's try evaluating the input $a$.
$$
\begin{aligned}
    f\left( \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} \right)
    =
    \begin{bmatrix}
        0a_1 + 1a_2 \\
        2a_1 + 3a_2 \\
        4a_1 + 5a_2
    \end{bmatrix}
\end{aligned}
$$
We can use this as input to the function $g$,
$$
    g
    \left(
        \begin{bmatrix}
            0a_1 + 1a_2 \\
            2a_1 + 3a_2 \\
            4a_1 + 5a_2
        \end{bmatrix}
    \right)
    =
    \begin{bmatrix}
        1(0a_1 + 1a_2) + 2(2a_1 + 3a_2) + 3(4a_1 + 5a_2) \\
        4(0a_1 + 1a_2) + 5(2a_1 + 3a_2) + 6(4a_1 + 5a_2)
    \end{bmatrix}    
$$
Applying the distributive property of real numbers, we can expand:
$$
    g(f(a)) =
    \begin{bmatrix}
        (1\cdot0)a_1 + (1\cdot1)a_2 + (2\cdot2)a_1 + (2\cdot3)a_2 + (3\cdot4)a_1 + (3\cdot5)a_2 \\
        (4\cdot0)a_1 + (4\cdot1)a_2 + (5\cdot2)a_1 + (5\cdot3)a_2) + (6\cdot4)a_1 + (6\cdot5)a_2
    \end{bmatrix}
$$
And now simplify by combining similar terms together,
$$
    g(f(a)) =
    \begin{bmatrix}
        (1\cdot0 + 2\cdot2 + 3\cdot4)a_1
        + (1\cdot1 + 2\cdot3 + 3\cdot5)a_2
        \\
        (4\cdot0 + 5\cdot2 + 6\cdot4)a_1
        + (4\cdot1 + 5\cdot3 + 6\cdot5)a_2
    \end{bmatrix}
$$
Now, separate out the $a_1$ and $a_2$ terms,
$$
    g(f(a)) =
    \begin{bmatrix}
        (1\cdot0 + 2\cdot2 + 3\cdot4)
        &  (1\cdot1 + 2\cdot3 + 3\cdot5)
        \\
        (4\cdot0 + 5\cdot2 + 6\cdot4) &
        (4\cdot1 + 5\cdot3 + 6\cdot5)
    \end{bmatrix}    
    \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}
$$
Now, let's remove the input entirely.  After all, we don't actually care what it is right now.  Instead, let's call our functions something like $A$ and $B$.  Each of $A$ and $B$ is a matrix.
$$
    f \circ g = A \cdot B
$$


TITLE
---------------------------------------------------------------------
TODO



TITLE
---------------------------------------------------------------------
TODO
