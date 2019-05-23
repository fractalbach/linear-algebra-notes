
Tips and Tricks
=====================================================================

Extra things that are useful as a reference.


Dimensions of Nine Different Products
---------------------------------------------------------------------

$$
\begin{aligned}
    \text{Scalar , Scalar}:
    && \mathbb{R}
    & \times \mathbb{R}
    && \to \mathbb{R}
\\
    \text{Scalar , Column Vector}:
    && \mathbb{R}
    & \times \mathbb{R}^n
    && \to \mathbb{R}^n
\\
    \text{Scalar , Row Vector}:
    && \mathbb{R}
    & \times \mathbb{R}^{1\times n}
    && \to \mathbb{R}^{1 \times n}
\\
    \text{Inner Product on }\mathbb{R}^n:
    && \mathbb{R}^n
    & \times \mathbb{R}^n
    && \to \mathbb{R}
\\
    \text{Inner Product on }\mathbb{R}^{1 \times n}:
    && \mathbb{R}^{1\times n}
    & \times \mathbb{R}^{1 \times n}
    && \to \mathbb{R}
\\
    \text{Outer Product}:
    && \mathbb{R}^{m\times 1}
    & \times \mathbb{R}^{n \times 1}
    && \to \mathbb{R}^{m \times n}
\\
    \text{Scalar, Matrix}:
    && \mathbb{R}
    & \times \mathbb{R}^{m \times n}
    && \to \mathbb{R}^{m \times n}
\\
    \text{Matrix, Column Vector}:
    && \mathbb{R}^{m \times n}
    & \times \mathbb{R}^{n \times 1}
    && \to \mathbb{R}^{m \times 1}
\\
    \text{Row Vector, Matrix}:
    && \mathbb{R}^{1 \times m}
    & \times \mathbb{R}^{m \times n}
    && \to \mathbb{R}^{1 \times n}
\end{aligned}
$$




The Matrix as a Function
---------------------------------------------------------------------

Let $f$ be a function:
$$
    f(x,y) = \left( \vphantom{\sum}
        x+2y, \enspace
        3x+4y, \enspace
        5x+6y
    \right)
$$
The function takes 2 elements as input and gives 3 elements as output,
$$
    f:\mathbb{R}^2 \to \mathbb{R}^3
$$
Suppose $x=1$ and $y=2$,
$$
\begin{aligned}
    & f(1,2) \\
    & =
        \left( \vphantom{\sum}
            1 (1) + 2 (2), \enspace
            3 (1) + 4 (2), \enspace
            5 (1) + 6 (2)
        \right)
    \\
    & =
        \left( 5, 11, 17 \right)
\end{aligned}
$$
We could rewrite the input list $(1,2)$ and output list $(5,11,17)$ as vectors, which reveals:
$$
    f
    \left(
        \begin{bmatrix} 1 \\ 2 \end{bmatrix}
    \right)
    =
    \begin{bmatrix} 5 \\ 11 \\ 17 \end{bmatrix}
$$
Now, let's say that function $f$ is a Linear Map, $A$, from $\mathbb{R}^2$ to $\mathbb{R}^3$, and rewrite this in an algebraic form.
$$
    A
    \begin{bmatrix} 1 \\ 2 \end{bmatrix}
    =
    \begin{bmatrix} 5 \\ 11 \\ 17 \end{bmatrix}
$$
Looking back above to the function $f$, we can use this to rewrite $A$ in a matrix notation.
$$
    \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
    \begin{bmatrix} 1 \\ 2 \end{bmatrix}
    =
    \begin{bmatrix} 5 \\ 11 \\ 17 \end{bmatrix}
$$
At this point, compare and contrast the dimensions of the matrix  with the function definition,
$$
    \begin{aligned}
        f : \; & \mathbb{R}^2 \to \mathbb{R}^3 \\
        A \in \; & \mathbb{R}^{3 \times 2}
    \end{aligned}
$$
and compare and contrast the input and output:
$$
\begin{aligned}
    x \in \mathbb{R}^2 \\
    Ax \in \mathbb{R}^{3}
\end{aligned}
$$
We can rewrite the function again.  This time, let's use our matrices to gain a new perspective of the nature of Linear Algebra:
$$
    f(x,y) =
    \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
    \begin{bmatrix} x \\ y \end{bmatrix}
    =
    \begin{bmatrix} 1x + 2y \\ 3x + 4y \\ 5x + 6y \end{bmatrix}
$$
