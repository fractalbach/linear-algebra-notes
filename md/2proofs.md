
Proofs
=====================================================================


Cosine Formula for Inner Product
---------------------------------------------------------------------

For two non-zero vectors $x,y\in V$,
$$
    \langle x,y \rangle = \|x\|\|y\| \cos{ \theta }
$$
where the angle $\angle x y = \theta$.

*Proof*:

There are two cases we need to write a proof for.

* Case 1: when $x$ and $y$ are not scalar multiples of each other.
* Case 2: when $x$ and $y$ are scalar multiples.

*Case 1*:

For any triangle with sides $a,b,c$, The Law of Cosines states,
$$
    c^2 = a^2 + b^2 - 2ab \cos{ \theta }
$$
where the angle $\angle a b = \theta$.   For vectors $x,y \in V$, we can treat them as sides of the triangle.  Let:
$$
    \begin{aligned}
        a &= \|x\| \\
        b &= \|y\| \\
        c &= \|x-y\| \\
    \end{aligned}
$$
Which allows us to rewrite the Law of Cosines:
$$
    {\|x-y\|}^2 \space = \space
    {\|x\|}^2 + {\|y\|}^2 - 2\|x\|\|y\| \cos{ \theta }
$$

Start with the definition of Inner Product, and apply its algebraic properties (notably the Bilinearity property), to show that Law of Cosines for Inner Products is correct.
$$
    \begin{aligned}
        &  {\|x-y\|}^2 \\
        &=
            \langle x-y , x-y \rangle
            \\
        &=
            \langle x, x-y \rangle - \langle y, x-y \rangle
             \\
        &=
            \left(\vphantom{\sum}
                \langle x, x \rangle - \langle x, y\rangle
            \right)
            -
            \left(\vphantom{\sum}
                \langle y, x \rangle - \langle y, y\rangle\right)
            \\
        &=
            \langle x, x \rangle - \langle x, y\rangle
            - \langle y, x \rangle + \langle y, y\rangle \\
        &=
            {\|x\|}^2 - 2\langle x,y \rangle + \|y\|^2 \\
    \end{aligned}
$$
Returning to the Law of Cosines,
$$
    \begin{aligned}
            {\|x-y\|}^2 \space
        &= \space
            {\|x\|}^2
            + {\|y\|}^2
            - 2\|x\|\|y\| \cos{ \theta }
        \\
            \cancel{ {\|x\|}^2}
            - 2 \langle x,y \rangle
            + \cancel{\|y\|^2}
        &=
            \cancel{ {\|x\|}^2 }
            +  \cancel{ {\|y\|}^2 }
            - 2 \|x\|\|y\| \cos{ \theta }
        \\
            \cancel{-2} \langle x,y \rangle
        &=
            \cancel{- 2} \|x\|\|y\| \cos{ \theta }
        \\
            \langle x,y \rangle
        &=
            \|x\|\|y\| \cos{ \theta }
    \end{aligned}
$$
$\Box$

*Case 2*:

Since $x$ and $y$ are scalar multiples of each other, we can write,
$$
    y = cx
$$
for some scalar $c\in \mathbb{R}$ where $c\neq 0$ (since the theorem statement says that $x$ and $y$ are "nonzero vectors").  Now, to find the value of $\theta$, we look at the value of $c$:

* If $c > 0$, then $\theta = 0$, and $\cos{\theta}=1$
* If $c < 0$, then $\theta = \pi$, and $\cos{\theta}=-1$

Define the sign of $c$, so that we can use it in our proof:
$$
    \text{sign}(c) =  \cos{\theta}
$$
And here's the proof:
$$
\begin{aligned}
    \langle x,y \rangle
    &= \langle cx, x \rangle \\
    &= c\langle x , x \rangle \\
    &= c {\| x \|}^2 \\
    &= c \|x\| \|x\| \\
    &= c \sqrt{({x_1}^2 + \ldots + {x_n}^2)} \ \|x\| \\
    &= \text{sign}(c) \sqrt{c^2 ({x_1}^2 + \ldots + {x_n}^2)} \ \|x\| \\
    &= \text{sign}(c) \sqrt{(c^2{x_1}^2 + \ldots + c^2{x_n}^2)} \ \|x\| \\
    &= \text{sign}(c) \sqrt{({y_1}^2 + \ldots + {y_n}^2)} \ \|x\| \\
    &= \text{sign}(c) \|y\| \|x\| \\
    &= \|x\| \|y\| \cos{\theta} \\
\end{aligned}
$$
$\Box$


Triangle Inequality
---------------------------------------------------------------------

TODO


Cauchy-Schwartz Inequality
---------------------------------------------------------------------

TODO
