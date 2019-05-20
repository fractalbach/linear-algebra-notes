
Matrices
=====================================================================

Specific Things involving Matrices

TODO see chapter 8 and 9.



Algebraic Properties of Matrices
---------------------------------------------------------------------
TODO


Algebraic Properties of Matrix Transpose
---------------------------------------------------------------------

* $(A^T)^T = A$
* $(A+B)^T = A^T + B^T$
* $(cA)^T = cA^T$
* $(AB)^T = B^T A^T$


Leading Entry
---------------------------------------------------------------------

The Leading Entry of a row in a matrix the is first non-zero element in that row (from left-to-right).


Special Notations
---------------------------------------------------------------------

The $1- \star - \times - 0$ notation.

* $1$ : must be a 1
* $\star$ : Non-zero values
* $\times$ : any number
* $0$ : must be a 0



Main Diagonal
---------------------------------------------------------------------

For a matrix $a_{i,k}$, the main diagonal would be defined as the set of entries:
$$
    \left\{
        a_{i,k} : i = k
    \right\}
$$
In the following example, the Main Diagonal would be the 1s:
$$
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{bmatrix}
$$

*Non-Diagonal* entries are all values that are *not* in the main diagonal:
$$
    \left\{ a_{i,k} : i \neq k \right\}
$$


Diagonal Matrix
---------------------------------------------------------------------

Diagonal Matrix is a matrix where all non-diagonal entries are 0.

For example, the following is a Diagonal Matrix:
$$
    \begin{bmatrix}
    \star & 0 & 0 \\
    0 & \star & 0 \\
    0 & 0 & \star
    \end{bmatrix}    
$$


Identity Matrix
---------------------------------------------------------------------

An Identity Matrix is a matrix where all diagonal entries are 1, and all non-diagonal entries are 0.  For example,
$$
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{bmatrix}    
$$
The Identity matrix is a function $I : \mathbb{R}^n \to \mathbb{R}^n$ that maps to the same vector space it started from. It satisfies the existence of an identity for linear maps.  For all $v \in \mathbb{R}^n$,
$$
    Iv = v
$$
Thus, the Identity Matrix needs to be a Square Matrix in $\mathbb{R}^{n\times n}$.




Lower-Triangular Entries
---------------------------------------------------------------------

*Lower-Triangular Entries* of a matrix are either on the diagonal are below the diagonal.  Defined as:
$$
    \left\{
        L_{i,k} : i \geq k
    \right\}
$$

*Strictly Lower-Triangular Entries* of a matrix are only the values below the diagonal:
$$
    \left\{
        L_{i,k} : i > k
    \right\}
$$





Lower-Triangular Matrix
---------------------------------------------------------------------

A Lower-Triangular Matrix, $L \in \mathbb{R}^{n \times n}$, is a square matrix such that
$$
    L_{i,k} = 0 \quad \text{for all } i < k
$$
For example, in this Lower-Triangular Matrix, $L \in \mathbb{R}^{3 \times 3}$,
$$
    \begin{bmatrix}
        \star & 0 & 0 \\
        \star & \star & 0 \\
        \star & \star & \star
    \end{bmatrix}
$$
the lower-triangular entries can be anything, and the rest must be 0.



Unit Lower-Triangular Matrix
---------------------------------------------------------------------

The Unit Lower-Triangular Matrix, $L \in \mathbb{R}^{n \times n}$ is both:
$$
    \begin{aligned}
        L_{i,k} = 1  && \quad \text{for all } i=k \\
        L_{i,k} = 0  && \quad \text{for all } i < k
    \end{aligned}
$$
An example of a Unit Lower-Triangular Matrix, $L \in \mathbb{R}^{3 \times 3}$,
$$
    \begin{bmatrix}
        1 & 0 & 0 \\
        \star & 1 & 0 \\
        \star & \star & 1
    \end{bmatrix}
$$



Upper-Triangular Matrix
---------------------------------------------------------------------

Upper-Triangular Entries are defined as:
$$
    \left\{ U_{i,k} : i \leq k \right\}
$$
Strictly-Upper-Triangular Entries are defined as:
$$
    \left\{ U_{i,k} : i < k \right\}
$$
Upper-Triangular Matrix example:
$$
    \begin{bmatrix}
        \star & \star & \star \\
        0 & \star & \star \\
        0 & 0 & \star
    \end{bmatrix}
$$
Unit Upper-Triangular Matrix example:
$$
    \begin{bmatrix}
        1 & \star & \star \\
        0 & 1 & \star \\
        0 & 0 & 1
    \end{bmatrix}
$$
Quite similar to the Lower-Triangular Matrix definitions and examples.

Bands of a Matrix
---------------------------------------------------------------------
TODO


Row Partition
---------------------------------------------------------------------
TODO


Column Partition
---------------------------------------------------------------------
TODO



Outer Product of Vectors
---------------------------------------------------------------------
TODO


Rank-one Updates
---------------------------------------------------------------------
TODO


Shear
---------------------------------------------------------------------
TODO


Dilation
---------------------------------------------------------------------
TODO


Transposition
---------------------------------------------------------------------
TODO


Givens Rotation
---------------------------------------------------------------------
TODO


Gauss Transform
---------------------------------------------------------------------
TODO
