
Proofs
=====================================================================

Law of Cosines
---------------------------------------------------------------------

For any triangle with sides $a,b,c$, The Law of Cosines states,
$$
    c^2 = a^2 + b^2 - 2ab \cos{ \theta }
$$
where the angle $\angle a b = \theta$.

To generalize to vectors, we take the Law of Cosines and make **Cosine Formula for Inner Product**. For vectors $x,y \in V$, we can treat them as sides of the triangle:

* $a = \|x\|$
* $b = \|y\|$
* $c = \|x-y\|$

You can rewrite the Law of Cosines to say:
$$
    {\|x-y\|}^2 \space = \space
    {\|x\|}^2 + {\|y\|}^2 - 2\|x\|\|y\| \cos{ \theta }
$$
*Proof*:

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
The Bilinearity property is used multiple times to break down the original 1 inner product into the 4 different ones.  In the last step, the Symmetry property was used to get the term $2\langle x,y \rangle$.


Triangle Inequality
---------------------------------------------------------------------

TODO


Cauchy-Schwartz Inequality
---------------------------------------------------------------------

TODO


## Other

For vectors $u,v \in V$ such that:
$$
    \langle u, v \rangle = \|u\| \|v\| \cos{\theta}
$$
Show that $u,v$ are orthogonal when $\theta = 0$.
