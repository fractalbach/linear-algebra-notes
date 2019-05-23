
# Matrix Vector Multiplication


Givens Rotations
---------------------------------------------------------------------


construct 2 by 2 matrix that can be used to Rotate a vector by angle $\theta$ in the counter-clockwise direction.

Let $Q \in R^{2 \times 2}$, called the Givens Rotation matrix.
$$
Q = \begin{bmatrix}
\cos{\theta} &&  -\sin{\theta}\\
\sin{\theta} && \cos{\theta}
\end{bmatrix}
$$
You can rotate a vector $v$ to become another vector $b$ by doing:
$$
Qv = b
$$

Examples:

* Rotate vector $\vec{e}_1 = (1, 0)$ and it becomes $\vec{b}_1 = (\cos{\theta}, \sin{\theta})$

* Rotate vector $\vec{e}_1 = (0,1)$ to become $\vec{b}_1 = (-\sin{\theta}, \cos{\theta})$




Moving Toward Invertible Matrices (Introducing Zeroes into Specific Matrices)
---------------------------------------------------------------------

Suppose
$$
    x = \begin{bmatrix} 2 \\ 1 \\ 3\\ -4 \end{bmatrix}
$$
Then find a matrix $A$ so that
$$
    Ax = \begin{bmatrix} \times \\ \times \\ 0 \\ 0 \end{bmatrix}
$$
We can do this by creating a linear map $f: R^4 \to R^4$
$$
    f(x) = \begin{bmatrix}
        1x_1 + 0x_2 + 0x_3 + 0x_4 \\
        0x_1 + 1x_2 + 0x_3 + 0x_4 \\
        0x_1 + 0x_2 + 0x_3 + 0x_4 \\
        0x_1 + 0x_2 + 0x_3 + 0x_4 \\
    \end{bmatrix}
$$
Which would simplify to:
$$
    f(x) = \begin{bmatrix}
    x_1 \\
    x_2 \\
    0 \\
    0 \\
    \end{bmatrix}
$$
And Let $A$ be the matrix that represents this function.  We will need a 4 by 4 matrix.
$$
A = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0
\end{bmatrix}
$$


However, there is another way, that will let us write an **Invertible** Matrix, Suppose
$$
    A = \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & -3 & 1 & 0 \\
        0 & 4 & 0 & 1
    \end{bmatrix}
$$
This also satisfies our goal:
$$
    \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & -3 & 1 & 0 \\
        0 & 4 & 0 & 1
    \end{bmatrix}
    \begin{bmatrix} 2 \\ 1 \\ 3 \\ -4 \end{bmatrix}
    =
    \begin{bmatrix} 2 \\ 1 \\ 0 \\ 0 \end{bmatrix}
$$
But What's cool about Invertible Matrices is that:
$$
    A A x = x
$$
notice how they can cancel each other out! So you can see that:
$$
    A A \begin{bmatrix} 2 \\ 1 \\ 3 \\ -4 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \\ 3 \\ -4 \end{bmatrix}
$$
Which is quite crazy, If you apply the transformation an infinite number of times, it will still be only 1 of the two different possible values.





Invertible Linear Maps
---------------------------------------------------------------------
TODO



Matrix-Matrix Mult Stuff
---------------------------------------------------------------------

$$
    B_{m \times p} = M_{m \times n } \cdot X_{n \times p}
$$

* The number of columns of the left argument matches the number of rows of right argument

* The number of rows of left arg A = number of rows of output product B

* Number of columns of right arg X = number of columns of output product

$$

$$






TITLE
---------------------------------------------------------------------
TODO



Extras
---------------------------------------------------------------------

Orthogonal Matrices (Unitary Matrices)
$$
    I_n = Q^T Q = Q Q^T
$$


Invertibility
---------------------------------------------------------------------









Challenge Problem
================================

Let $A \in R^{4 \times 4}$. Find an $X$ that swaps (permutes) columns 2 and 3 of $A$ via multiplication.

*Restated*:

We want to find $A$ such that:
$$
    A
    \begin{bmatrix}
        \times & a_2 & a_3 & \times \\
        \times & b_2 & b_3 & \times \\
        \times & c_2 & c_3 & \times \\
        \times & d_2 & d_3 & \times \\
    \end{bmatrix}
    =
    \begin{bmatrix}
        \times & a_3 & a_2 & \times \\
        \times & b_3 & b_2 & \times \\
        \times & c_3 & c_2 & \times \\
        \times & d_3 & d_2 & \times \\
    \end{bmatrix}
$$
We find, through magical intuition, that:
$$
    A =
    \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 0 & 1
    \end{bmatrix}
$$
which is often called a transposition matrix.


$$
    \begin{bmatrix}
    1 & 2 & 3  \\    \hdashline
    4 & 5 & 6
    \end{bmatrix}
$$


# Matrix Exponentiation

Look this up
