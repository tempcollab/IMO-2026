## Lemma (Constraint Domination)

For indices $i<j$ in the greedy sequence, if $\mathrm{primes}(a_j)\subseteq\mathrm{primes}(a_i)$,
then for every integer $y$: $\gcd(y,a_j)>1 \implies \gcd(y,a_i)>1$.

Consequently, when testing whether a candidate $y$ satisfies all of the constraints
$\{\gcd(y,a_i)>1 : i=1,\dots,n\}$, any constraint whose index's prime set is a strict superset of
another appearing prime set is logically redundant and may be dropped: the system of $n$
constraints is equivalent (for the purpose of deciding valid $y$) to the sub-system indexed by the
inclusion-minimal elements of $\{\mathrm{primes}(a_1),\dots,\mathrm{primes}(a_n)\}$ under set
inclusion.

## Proof

If $\gcd(y,a_j)>1$, some prime $q$ divides both $y$ and $a_j$, so $q\in\mathrm{primes}(a_j)$. By
hypothesis $\mathrm{primes}(a_j)\subseteq\mathrm{primes}(a_i)$, so $q\in\mathrm{primes}(a_i)$ too,
i.e. $q\mid a_i$. Since also $q\mid y$, $\gcd(y,a_i)\ge q>1$.

For the consequence: if $D_j:=\mathrm{primes}(a_j)$ is a strict superset of some other $D_i$
appearing among $D_1,\dots,D_n$, the argument above (applied with the roles matching the inclusion)
shows the constraint from $j$ is implied by the constraint from $i$, so $j$'s constraint can be
dropped without changing the set of valid $y$; the converse (a non-dominated / inclusion-minimal
constraint cannot be dropped) is immediate since it is literally one of the original constraints.
$\blacksquare$

## Status
Certified. Proved in full in `growth-bound-density.md` (Lemma 3); reviewed and correct (one-line
argument from prime divisibility, no gaps). Reusable by any approach that wants to reduce "$n$
raw constraints" to a bounded live set. Note: this lemma alone does **not** establish that the
resulting antichain of inclusion-minimal prime-sets is itself finite-state / eventually stable —
that remains open (see the "antichain stabilization" gap recorded in `growth-bound-density.md` and
the essentially equivalent "No-Escape" gap in `core-signature-pigeonhole.md`).
