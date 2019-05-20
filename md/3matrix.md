
Matrices
=====================================================================

Algebraic Properties of Matrices
---------------------------------------------------------------------

Compare these with the properties of Vector Space.

*Protip:* Matrices are in Vector Space.

Commutativity:

* $A+B=B+A$

Associativity:

* $A+(B+C)=(A+B)+C$

Additive Identity:

* $A+0=A$

Additive Inverse:

* $A+(-A)=0$

Distributivity of matrix addition:

* $a(A+B) = aA+aB$

Distributivity of scalar addition:

* $(a+b)A=aA+bA$

Associativity of scalar multiplication

* $a(bA)=(ab)A$

Multiplicative Identity of scalar multiplication

* $1A=A$



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

Entries

* $A_{ij}$ of matrix $A$ is the entry in the $i^{\text{th}}$ row and $j^{\text{th}}$ column.
* I like to use $A_{i,j}$ or $A_{[i,j]}$ depending on the situation.


The $1- \star - \times - 0$ notation:

* $1$ : must be a 1
* $\star$ : Non-zero numbers, $= \{c \in \mathbb{R} : c \neq 0\}$
* $\times$ : any number $= \{c\in \mathbb{R}\}$
* $0$ : must be a 0

MATLAB Syntax and Commands:

* $\texttt{A(i,k)}$ returns the entry $A_{i,k}$
* $\texttt{A(i,:)}$ returns the $i^{\text{th}}$ row
* $\texttt{A(:,k)}$ returns the $k^{\text{th}}$ column
* $\texttt{numel(A)}$ returns the number of elements in matrix $A$
* $\texttt{nnz(A)}$ returns the number of non-zero elements in $A$



Main Diagonal
---------------------------------------------------------------------

For a matrix entry $a_{i,k}$, the main diagonal entries would be defined as the set:
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

An Identity Matrix, denoted $I_n$ or just $I$,  is a square matrix in $\mathbb{R}^{n\times n}$ where all diagonal entries are 1, and all non-diagonal entries are 0.  For example,
$$
    I_3 =
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{bmatrix}    
$$
When used in Matrix Multiplication, for some matrix $A \in \mathbb{R}^{m \times n}$, the Identity Matrix has the property:
$$
    I_m A = A I_n = A
$$


Lower-Triangular Entries
---------------------------------------------------------------------

*Lower-Triangular Entries* of a matrix are either: on the diagonal, or below the diagonal.
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
        \times & 0 & 0 \\
        \times & \times & 0 \\
        \times & \times & \times
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
        \times & 1 & 0 \\
        \times & \times & 1
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
        \times & \times & \times \\
        0 & \times & \times \\
        0 & 0 & \times
    \end{bmatrix}
$$
Unit Upper-Triangular Matrix example:
$$
    \begin{bmatrix}
        1 & \times & \times \\
        0 & 1 & \times \\
        0 & 0 & 1
    \end{bmatrix}
$$
Quite similar to the Lower-Triangular Matrix definitions and examples.



Bands of a Matrix
---------------------------------------------------------------------

*Diagonal Band*

The $d^{\text{th}}$-diagonal-band of a matrix $A$ is the set of entries:
$$
    \text{d}^\text{th}\text{ diagonal band} = \{ A_{i,k} : i - k = d \}
$$
For example, the 0-diagonal-band is the main diagonal, and the 2-band of $A \in \mathbb{R}^3$ would be:
$$
    \left\{ A_{[0,2]}, A_{[1,1]}, A_{[2,0]} \right\}
$$

Upper-Triangular Bands :

* Set of entries
* $\left\{ A_{i,k} : i-k\leq 0 \right\}$

Lower-Triangular Bands :

* Set of entries
* $\left\{ A_{i,k} : k \geq 0 \right\}$

Lower Bandwidth :

* Number
* $d$ such that $A_{i,k}=0$ for $(i-k>d)$.
* The lowest band before everything becomes 0s.

Upper Bandwidth:

* Number
* $d$ such that $A_{i,k}=0$ for $(i-k<d)$.
* The highest band before everything becomes 0s.


Outer Product of Vectors
---------------------------------------------------------------------

For $x \in \mathbb{R}^m, y \in \mathbb{R}^n$ the outer product is defined,
$$
\begin{aligned}
    x \otimes y
    & =
    xy^T =
    \begin{bmatrix} x_1 \\ \vdots \\ x_m \end{bmatrix}
    \begin{bmatrix} y_1 & \cdots & y_n \end{bmatrix}
    =
    \begin{bmatrix}
        x_1y_1 & \cdots & x_1y_n \\
        \vdots & \vdots & \vdots \\
        x_my_1 & \cdots & x_my_n
    \end{bmatrix}
\end{aligned}
$$
you could also say that the outer product is a function:
$$
    (\mathbb{R}^m,  \mathbb{R}^n) \to \mathbb{R}^{m \times n}
$$


Rank-one Updates
---------------------------------------------------------------------
For $A\in\mathbb{R}^{m\times n}, x \in \mathbb{R}^m, y \in \mathbb{R}^n$, the rank-one update is defined,
$$
    A+xy^T
$$


Shear
---------------------------------------------------------------------
Shear matrices are Rank-One Updates to the Identity matrix. An $n\times n$ shear matrix is:
$$
    S_{[i,k]}(c) = I_n + c \ \textbf{e}_i ({\textbf{e}_k}^T)
$$
where $\textbf{e}$ is the standard basis, and $i\neq k$.

Example: where $i=3, k=1, c=-5, n=3$,
$$
\begin{aligned}
     S_{[3,1]}(-5)
    & =
        I_3 + -5 \textbf{e}_3 ({\textbf{e}_1}^T)  \\ \\
    & =
        \begin{bmatrix}
            1 & 0 & 0 \\
            0 & 1 & 0 \\
            0 & 0 & 1
        \end{bmatrix}
        + -5
        \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
        \begin{bmatrix} 1 & 0 & 0 \end{bmatrix}
        \\ \\
    & =
        \begin{bmatrix}
            1 & 0 & 0 \\
            0 & 1 & 0 \\
            -5 & 0 & 1
        \end{bmatrix}
\end{aligned}
$$


Dilation
---------------------------------------------------------------------
For $n\in \mathbb{N}, \enspace j \in \mathbb{N}, \enspace j \leq n$, define an $n\times n$ dilation matrix to be:
$$
    D_j(c)=I_n+(c-1)e_j({e_j}^T)
$$

Transposition
---------------------------------------------------------------------
For $n \in \mathbb{N}, \enspace i\neq k$, define the $n \times n$ transposition matrix to be:
$$
    P_{[i,k]} = e_i({e_k}^T) + e_k({e_i}^T)+\sum_{\substack{j=1 \\ j\neq k}}^n e_j ({e_j}^T)
$$
Example:
$$
    P_{[2,4]} =
    \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 0 & 0 & 1 \\
        0 & 0 & 1 & 0 \\
        0 & 1 & 0 & 0 \\
    \end{bmatrix}
$$


Gauss Transform
---------------------------------------------------------------------
Let $n,k \in \mathbb{N}, \enspace k<n, \enspace T\in\mathbb{R}^n$, where T is a vector whose first $k$ components are zero.
$$
    T^T =
    \begin{bmatrix}
        0 & \cdots &
        T_{k+1} & \cdots & T_n
    \end{bmatrix}
$$
The Gauss Transformation is a matrix
$$
    L_k = I_n - T({e_k}^T)
$$
