## Lemma (Growth-Event Update)

**Statement.** Let $D_i:=\mathrm{primes}(a_i)$, $\mathcal A_n$ the antichain of inclusion-minimal
elements of $\{D_1,\dots,D_n\}$. Call $n\ge2$ a **growth event** if no $i<n$ has $D_i\subseteq D_n$
(equivalently $D_n$ is inclusion-minimal in $\{D_1,\dots,D_n\}$). Then:

(a) If $n$ is not a growth event, $\mathcal A_n=\mathcal A_{n-1}$.

(b) If $n$ is a growth event, $D_n\notin\mathcal A_{n-1}$ and
$$\mathcal A_n=\big(\mathcal A_{n-1}\setminus\{B\in\mathcal A_{n-1}:D_n\subsetneq B\}\big)\cup\{D_n\}
\ne\mathcal A_{n-1}.$$

**Proof.** Standard finite-poset argument: write $E=\{D_1,\dots,D_{n-1}\}$, $E'=E\cup\{D_n\}$; (a)
adjoining a dominated or repeated element does not change the set of inclusion-minimal elements of a
finite poset; (b) adjoining a genuinely new inclusion-minimal element $D_n$ removes exactly those
previously-minimal elements it is a proper subset of, and adds itself. Full step-by-step derivation:
`approaches/global-smooth-density-contradiction.md` (round 5), Lemma 1.

## Corollary (Antichain Stabilization $\Leftrightarrow$ finitely many growth events)

**Statement.** Antichain Stabilization ($\exists N^*:\mathcal A_n=\mathcal A_{N^*}\ \forall n\ge N^*$)
holds iff only finitely many $n\ge2$ are growth events.

**Proof.** Immediate telescoping of the Growth-Event Update Lemma in both directions (full proof:
same source file, Corollary 1).

## Definitions and Propositions (Type A / Type B growth-event decomposition)

Fix $P=\{p\text{ prime}: p\le L_0\}$ ($L_0=\mathrm{rad}(a_1)$), $D_n^P:=P\cap D_n$,
$R_n:=\{D_1^P,\dots,D_n^P\}$. A growth event $n$ is **Type A** if $D_n^P\notin R_{n-1}$, **Type B**
otherwise.

**Proposition (Type A events are finite, unconditionally, $\le 2^{|P|}-2$).** *Proof:* $(R_n)$ is a
non-decreasing chain of subsets of $2^P\setminus\{\emptyset\}$ (size $2^{|P|}-1$), $R_1$ nonempty, so
at most $2^{|P|}-2$ strict increases.

**Proposition (Type B growth events are exactly the PC-violating ones: $n$ Type B $\Rightarrow$
$D_n\not\subseteq P$).** *Proof:* if $D_n\subseteq P$ then $D_n=D_n^P\in R_{n-1}=D_j^P$ for some
$j<n$; case-split on whether $D_j\subseteq P$ shows $D_j\subseteq D_n$ either way, contradicting $n$
being a growth event.

Both propositions proved in full in `approaches/global-smooth-density-contradiction.md` (round 5), §3
(Propositions 2–3).

## Status
Certified. All statements above reviewed and re-derived independently by the proof-reviewer (round 5)
from the cited source file; no gap found — elementary finite-poset / pigeonhole reasoning throughout,
using only the problem's definitions and `lemmas/constraint-domination.md`.

## Reuse note
Gives a clean, self-closing-antichain-free restatement of the sole remaining open target for odd
$a_1$: **only finitely many Type B growth events occur** (Type A is already unconditionally finite).
This is the same event set as `leftover-witness-confinement.md`'s "Step 6" residual case (antichains
with no singleton block) and `antichain-signature-closure.md`'s "self-closing reachability" — three
independently-built approaches converge on an equivalent open target, cross-checked, not yet proved
for general $a_1$.
