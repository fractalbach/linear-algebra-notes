
Applications
=====================================================================

Examples of applying Linear Algebra to other things.
Includes models made with Vectors and Matrices.

Incidence Matrix of a Graph
---------------------------------------------------------------------

* Rows = Edges
* Columns = Nodes

Undirected Incidence Matrix:

* 1 if an edge connects a node
* 0 otherwise

Directed Incident Matrix

* 1 if edge pointing away from node. (leaves)
* -1 if edge is pointing inward to node. (enters)
* 0 otherwise.


3D Wireframe
---------------------------------------------------------------------

The Wireframe model has a list of vectors in $\mathbb{R}^3$, where each corresponds to a position in the space.  They are put together into a vertex table in $\mathbb{R}^{3 \times n}$ like so:
$$
    \begin{bmatrix}
    v_{1_x} & \cdots & v_{n_x} \\
    v_{1_y} & \cdots & v_{n_y} \\
    v_{1_z} & \cdots & v_{n_z}
    \end{bmatrix}
$$
They can be connected using an Wireframe Edgetable, where the vertex number corresponds to the column number from the table above.
$$
    \begin{bmatrix}
    \texttt{edge}_1 & \texttt{StartVertex}_1 & \texttt{EndVertex}_1 \\
    \vdots & \vdots & \vdots \\
    \texttt{edge}_m & \texttt{StartVertex}_m & \texttt{EndVertex}_m
    \end{bmatrix}
$$
This is enough information to create wireframes.

3D Polygons
---------------------------------------------------------------------
To create polygons, you also need to include a polygon face table
$$
    \begin{bmatrix}
    \texttt{face} & \texttt{vertex1} & \texttt{vertex2} & \texttt{vertex3} \\
    \vdots & \vdots & \vdots & \vdots
    \end{bmatrix}
$$
with a matrix of faces and the vertices that generate them.

Spring-Mass Problem
---------------------------------------------------------------------

* $x_1(t)$ : position of mass 1 at time $t$
* $x_0$ : vector of positions at time 0
* $x(t)$ : vector of positions at time $t$.
* $u(t) = x(t) - x_0$ : vector of $\Delta x$ between time 0 and $t$.
* Let $e(t)$ be the "elongation" of the spring, the change in length of the spring between time 0 and $t$.
* $e(0)$ would be set to 0 by default, since that is our point of reference for checking the change in length of the spring.
* To find the length of the spring, measure the distance between the two masses that hold the spring together (one of those might just be the ceiling). For your own sanity, try finding the initial length: $l_0$ and the final length: $l_f$, then set $e(t) = l_f - l_0$.
* Try to set $e(t)$ in terms of $u(t)$.

*Finding $e(t)$*:

However, it will be useful for this problem to define each $e_i(t)$ in terms of $u_i(t)$, where $i$ represents one of the masses.
$$
\begin{aligned}
    e_1(t) &= a_1u_1(t) + \ldots + a_nu_n(t) \\
    e_2(t) &= a_1u_1(t) + \ldots + a_nu_n(t) \\
\end{aligned}
$$
and so on, one equation for each of the springs. (With different values of $a$ in each equation).  There are $n$ masses total, and each of them is an argument to the function.  Thus, we are looking at a linear map here:

* $a_1,\ldots,a_n \in \mathbb{R}$
* Let $m$ be the number of masses
* Let $n$ is the number of springs
* Notice that $n=m+1$ in this problem.
* Our linear map is from $\mathbb{R}^m \to \mathbb{R}^n$

Which means we can write it as matrix:
$$
    e(t) =
    \begin{bmatrix} e_1(t) \\ \vdots \\ e_n(t) \end{bmatrix}
    =
    A_1 u_m(t) + \ldots A_m u_m(t)
    = Au(t)
$$
where $A_1, \ldots, A_m \in \mathbb{R^n}$ and $A\in\mathbb{R^{m\times n} }$

*Finding Forces*:

* Each mass has 3 forces acting upon it
* $f_s$ is restoring force (going up) given by Hooke's law.

Find the restoring force
$$
    f_s(t) =
    \begin{bmatrix}
        f_{s_1}(t) \\ \vdots \\ f_{s_n}(t)
    \end{bmatrix}
    =
    \begin{bmatrix}
        k_1e_1(t) \\ \vdots \\ k_ne_n(t)
    \end{bmatrix}
    =
    e_1(t)\begin{bmatrix}k_1 \\ \vdots \\ 0 \end{bmatrix}
    +
    \cdots
    +
    e_n(t) \begin{bmatrix}0 \\ \vdots \\ k_n \end{bmatrix}
$$
Find net internal forces
$$
\begin{aligned}
    y_1(t) & = f_{s_2}(t) - f_{s_1}(t) \\
    & \vdots \\
    y_m(t) & = f_{s_{n} }(t) - f_{s_{(n-1)} }(t)
\end{aligned}
$$
Notice again that $n=m+1$ in this problem.
Write each $y_i(t)$ for $i\in[1,m]$ as a combination of all forces $f_s(t)$:
$$
\begin{aligned}
    y_{1(t)} &= (-1)f_{s_1(t)} + (1)f_{s_2(t)} + \ldots + (0)f_{s_n(t)} \\
    & \vdots \\
    y_{m(t)} &=(0)f_{s_1(t)} + \ldots + (-1)f_{s_{(n-1)}(t)} + (1)f_{s_{n}(t)}
\end{aligned}
$$
Write the matrix version of $y(t)$, (see the Trick: Matrix as a Function):
$$
    y(t) =
    \begin{bmatrix}
        -1 & 1 & \cdots & 0 \\
        \vdots & \vdots & \vdots & \vdots \\
        0 & \cdots & -1 & 1
    \end{bmatrix}
    \begin{bmatrix}
        f_{s_1(t)} \\
        \vdots \\
        f_{s_{(n-1)}(t)} \\
        f_{s_n(t)}
    \end{bmatrix}
    =
    -A^T f_{s}(t)
$$
And,
$$
\begin{aligned}
    y(t) &= -A^T f_s(t) \\
    &= -A^T Ce(t) \\
    &= -A^T CAu(t) \\
    &= -Ku(t)
\end{aligned}
$$
where
$$
    K = A^T C A
$$
and where
$$
    C = \begin{bmatrix}
    k_1 & 0 & \cdots & 0 \\
    0 & k_2 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \vdots \\
    0 & 0 & \cdots & k_n
    \end{bmatrix}
$$

And eventually we get the net external forces,
$$
    Ku(t) = F_e(t)
$$
which is a function we can use to calculate the force $F_e(t)$ given the displacement vector $u(t)$.
