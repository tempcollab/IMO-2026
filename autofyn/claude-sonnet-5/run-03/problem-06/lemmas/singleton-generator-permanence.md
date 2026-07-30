## Lemma (Singleton-generator permanence)

**Statement.** Adopt the Convention of `lemmas/leftover-witness.md` ("index $i$ is a generator" means
$D_i$ is not a superset of, and not equal to, any $D_j$ for $j<i$). Suppose some generator index $j$
has $D_j=\{p\}$ for a prime $p$ (i.e. $a_j=p^{e_j}$ is a pure prime power). Then **no index $n>j$ can
be a generator**: the antichain of live generators is permanently $\{\{p\}\}$ from index $j$ onward.
In particular, if $\omega(a_1)=1$ (so $D_1=\{p\}$ itself), P-Confinement holds for that $a_1$
unconditionally, with no further argument needed.

**Proof.** By `lemmas/absorption-lemma.md` part (a) (applied with $m=j$, $q=p$, $e=e_j$): $p\mid a_k$
for every $k\ge1$. Fix any $n>j$. Then $p\mid a_n$, so $\{p\}\subseteq D_n$. Either $D_n=\{p\}$, which
equals the earlier $D_j$ ($j<n$), contradicting the Convention (a generator cannot equal an earlier
$D_j$); or $D_n\supsetneq\{p\}=D_j$ properly, again contradicting the Convention (a generator cannot
be a proper superset of an earlier $D_j$). Either way $n$ is not a generator. Since $n>j$ was
arbitrary, no index past $j$ is ever a generator, so the antichain (as a set of distinct realized
minimal prime-sets) is exactly $\{\{p\}\}$ for all indices $\ge j$ — consistent with, and strengthening,
`lemmas/absorption-lemma.md` part (b) (which shows $\{p\}$ is the antichain's sole element, without the
additional "no fresh generator" statement proved here).

For the "in particular": if $\omega(a_1)=1$, then $j=1$ works directly ($D_1=\{p\}=S$ is trivially a
singleton generator), so by the above no index $n>1$ is ever a generator, and $D_1=\{p\}\subseteq P$
trivially. Hence every generator index (just $i=1$) satisfies $D_i\subseteq P$: P-Confinement holds.
$\blacksquare$

**Status.** Certified. Proved in full by `approaches/leftover-witness-confinement.md` (round 5), Step
4 Proof 1, as a direct consequence of `lemmas/absorption-lemma.md`. Sharper than Absorption's own
stated consequence: shows not just that the antichain stabilizes as a *set*, but that *no index can
ever again be classified as a generator* once a singleton generator has appeared — useful to any
approach attacking P-Confinement or Antichain Stabilization by induction/minimal-counterexample on the
generator index, since it lets that approach assume, in every remaining case, that no singleton
generator has appeared yet (all live blocks have size $\ge2$).
