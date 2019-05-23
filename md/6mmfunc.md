Matrix Multiplication as the Composition of Linear Functions
=====================================================================

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

You could write these as a **composition of functions**,
$$
    g \circ f : R^2 \to R^3 \to R^2
$$
which just simplifies to:
$$
    g \circ f : R^2 \to R^2
$$
So let's create some example input so we can see what's going on here.  When composing functions, we don't actually care what the input is, but it helps for understanding.

Let our example input be a vector $a \in R^2$.  Let's rewrite our composition of functions in a way that looks more familiar,
$$
    (g \circ f)(a) = g(f(a))
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
    g \circ f =
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
And finally, let's say that $G$ represents the first matrix, and $F$ represents the second matrix,
$$
    g \circ f =
    GF
$$
