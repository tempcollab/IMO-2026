## imo-2026-06

Scope for every approach below: the even-$a_1$ case is **fully solved and closed**
(`approaches/absorption-recurrence-even-case.md`, certified `lemmas/even-persistence.md`); do not
reopen it. All approaches below target **odd $a_1$ only** (equivalently $2\notin S=\mathrm{primes}(a_1)$),
which is the entire remaining content of the theorem. Notation throughout (imported, not re-derived):
$D_i=\mathrm{primes}(a_i)$, $S=D_1$, $L_0=\mathrm{rad}(a_1)$, $P=\{\text{primes}\le L_0\}$,
$L_P=\prod_{p\in P}p$, $\pi(x)=P\cap\mathrm{primes}(x)$, $\mathcal A_n$ = antichain of inclusion-minimal
$D_i$ among $\{D_1,\dots,D_n\}$ ("generators", `lemmas/constraint-domination.md`).

---

leftover-witness-confinement: revise of `dilworth-antichain-bound`
Target: the full theorem for every odd $a_1$ (via the already-certified
`lemmas/pc-implies-theorem.md`: PC $\Rightarrow$ theorem with zero secondary gap).
Technique: strong induction on the generator index / minimal-counterexample descent on **P-Confinement
(PC)**, using the certified Local Congruence Reduction (LCR, `lemmas/local-congruence-reduction.md`)
plus this round's new **Leftover-Witness Lemma** (from `/tmp/round-5/math-explorer-minimal-counterexample.md`,
1233/1233 computationally verified, zero exceptions) to reduce PC's remaining content to a single bounded
combinatorial question.
Skeleton:
  1. Suppose PC fails; let $n$ be **minimal** such that the generator $D_n\not\subseteq P$, i.e. some
     prime $q\mid a_n$ has $q>L_0$; let $e=v_q(a_n)\ge1$, $m:=a_n/q^e$. By minimality, PC holds for
     every generator index $<n$, so LCR applies with $i=n$ — by the LCR proof.
  2. **Leftover-Witness Lemma** (certify formally as `lemmas/leftover-witness.md` before building on
     it): either $m<a_1$ ("Case A") or $m=a_j$ exactly for some $j<n$ ("Case B") — by LCR's
     $(\Leftarrow)$ direction (which needs only $D_j\subseteq P$ for $j<n$, not $x>a_{n-1}$, giving
     $m$ globally valid against all of $a_1,\dots,a_{n-1}$) combined with strict monotonicity of the
     sequence and minimality of each $a_k$ as the smallest valid candidate $>a_{k-1}$.
  3. **Case B is impossible**: $a_n=q^e\cdot a_j$ so $D_j\subseteq D_n$ trivially, with $j<n$ — this
     dominates $D_n$, contradicting that $D_n$ is a genuine new generator (inclusion-minimal) — by
     `lemmas/constraint-domination.md`'s domination relation.
  4. So Case A holds: $m<a_1$ is a **bounded** auxiliary integer (bound independent of $n$), and by the
     same validity/domination logic, $\pi(m)$ must (i) hit every block $F\in\mathcal A_{n-1}$
     (validity, from LCR) and (ii) contain no block $F\in\mathcal A_{n-1}$ in full — else $F\subseteq
     \pi(m)\subseteq D_n$ would dominate $D_n$ exactly as in step 3.
  5. **New Singleton-Block sub-lemma (this round, to prove in the build):** if $\mathcal A_{n-1}$
     contains any singleton block $\{p\}$, Case A is **immediately impossible** — hitting $\{p\}$
     forces $p\in\pi(m)$, i.e. $\{p\}\subseteq\pi(m)$, i.e. $m$ *contains* that block, contradicting
     (ii). Moreover, once a singleton generator has ever appeared, the whole theorem already follows
     directly from `lemmas/absorption-lemma.md` without needing PC at all in that branch. So the
     **only residual case** is: $\mathcal A_{n-1}$ has **no singleton block** (every block has size
     $\ge2$).
  6. **Core open target, narrowed and precisely restated:** for an antichain $\mathcal A$ all of whose
     blocks have size $\ge2$, does there exist a subset $H\subseteq P$ with $|H|\le\omega(m)\le
     \log_2(a_1)$ (bounded, independent of $n$) that hits every block of $\mathcal A$ but contains no
     block of $\mathcal A$ in full? Show no such $H$ can arise from the specific antichains produced
     by this recursion (not an arbitrary antichain — use that every block is itself realized by an
     actual, previously-valid term $a_j$, which may supply extra structure beyond raw combinatorics).
  7. If step 6 closes (no such $H$ exists / cannot arise), Case A is impossible too, contradicting the
     minimal-counterexample assumption — PC holds for all $n$, theorem follows via
     `lemmas/pc-implies-theorem.md`.
Key lemmas (claim + mechanism):
  - Leftover-Witness Lemma — because LCR's sufficiency direction never used $x>a_{i-1}$, so removing
    $q^e$ from $a_n$ yields a globally-valid integer, forcing it to equal the true minimal candidate at
    some earlier step or be smaller than the very first term.
  - Case-B-impossible Corollary — because $a_j\mid a_n$ makes $D_j\subseteq D_n$ trivially, violating
    minimality of the "new" generator $D_n$.
  - Singleton-Block sub-lemma — because a singleton block's hitting condition and its non-containment
    condition are the *same* condition, so they are jointly unsatisfiable unless $p\notin\pi(m)$, which
    would violate hitting.
Open gaps: step 6, the bounded hitting-but-non-covering transversal exclusion for antichains with all
  blocks $\ge2$ — this is the true residual target, strictly narrower than raw PC (it never needs to
  reason about $n$ directly, only about the abstract antichain shape at the moment of failure, plus
  the fact that each block traces back to an actually-realized earlier term).
Cases to cover: (a) $\mathcal A_{n-1}$ has a singleton block — closed immediately via Absorption; (b)
  $\mathcal A_{n-1}$ has no singleton block — open, the residual target of step 6.
Watch out for: don't conflate "hits every block" with "contains some block" — they are logically
  independent for blocks of size $\ge2$; verify the bound $\omega(m)\le\log_2 a_1$ carefully ($m<a_1$
  a positive integer, product of $\omega(m)$ distinct primes each $\ge2$); double-check Case A/B are
  exhaustive and mutually exclusive as stated (the explorer's data shows a boundary case $m=a_1$ itself,
  i.e. $j=1$, should be classified consistently — pick one convention and state it explicitly).

---

phi-weighted-antichain-monovariant: revise of `self-closing-pair-density-odd-case`
Target: Antichain Stabilization (equivalently self-closing reachability, via
`lemmas/self-closing-antichain-sufficiency.md`) for every odd $a_1$ — a genuinely different mechanism
from PC/LCR, attacking the sibling target directly via a joint (not per-prime) weighted potential.
Technique: Sperner/LYM/Bollobás set-pair inequality for (automatically pairwise-intersecting)
antichains, exploiting joint co-occurrence structure — directly responds to round 4's own diagnosis
(`per-prime-divisor-chain-decomposition.md`) that per-prime state discards the joint information that
actually drives antichain evolution.
Skeleton:
  1. Observe (trivial restatement of the problem's hypothesis, not yet exploited quantitatively in the
     population): $\gcd(a_j,a_i)>1$ for all $i<j$ forces $D_i\cap D_j\ne\emptyset$ for all $i,j$, so
     $\{D_1,\dots,D_n\}$, hence $\mathcal A_n$, is always a pairwise-intersecting family.
  2. **Before building anything else**, computationally test candidate potentials on the existing rich
     data set (esp. $a_1=15,105,385,429,3003$, whose antichains are already fully traced in
     `self-closing-pair-density-odd-case.md` and the round-5 explorer reports) — per memory rule
     "ALWAYS test... premise computationally before a builder builds on it." Test:
     $\Phi_n:=\sum_{F\in\mathcal A_n}L_0^{-|F|}$, and if that fails, the true LYM weight
     $\Phi_n':=\sum_{F\in\mathcal A_n}\binom{|P|}{|F|}^{-1}$ (ground set $P$, size $|P|=\pi(L_0)$).
  3. **Key question to resolve before claiming progress:** is $\Phi_n$ (or $\Phi_n'$) provably
     non-increasing (or eventually so) at every "growth event" (new generator added), by an argument
     that does **not** presuppose already knowing which generators are eventually permanent (avoid the
     exact trap that refuted $\tau_p$ in round 4 — a monovariant claim is worthless if it can only be
     checked in hindsight)? If a domination event only ever removes blocks (never adds), $\Phi_n$
     trivially decreases there — the real content is bounding the *increase* from growth events.
  4. If a strict-decrease-or-bounded-increase property is established with a fixed per-event budget
     that sums to a finite total (this is the crux — must not reduce to the previously-refuted
     $O(\log a_n)$ charging shape), conclude $\mathcal A_n$'s growth events are finite in number, hence
     $\mathcal A_n$ stabilizes, giving self-closing via `lemmas/self-closing-antichain-sufficiency.md`.
Key lemmas (claim + mechanism):
  - Pairwise-intersecting antichain fact — because the problem's own hypothesis gives $\gcd>1$ for
    every pair of indices, immediate.
  - Candidate potential $\Phi_n$/$\Phi_n'$ non-increasing-or-bounded-total-increase — **unverified,
    the entire content of this approach**; must be tested computationally first, using the $a_1=3003$
    "risk ratio climbs to 0.70 before a rescuing Absorption" data point from
    `/tmp/round-5/math-explorer-fresh-framing2.md` as the hardest available stress test (247 live
    generators at the peak).
Open gaps: everything past step 2 — this is the most exploratory approach in the field; the builder's
  first task is the computational test, not a proof attempt, and should report honestly if $\Phi_n$
  fails to behave (a clean negative result, in the shape of round 4's $\sigma_p$/$\tau_p$ diagnoses, is
  an acceptable and valuable outcome here, not a failure to hide).
Cases to cover: none (single unified potential-function argument, if it works).
Watch out for: the $\tau_p$ circularity trap (monotonicity only visible in hindsight); confirm the
  chosen weight genuinely uses the *joint* size $|F|$ of each block (not a per-prime quantity in
  disguise) — the whole point is to capture co-occurrence, which per-prime candidates already failed to
  capture.

---

antichain-signature-closure: advance
Target: the full theorem for every odd $a_1$, via Antichain Stabilization
(`lemmas/self-closing-antichain-sufficiency.md`).
Technique: unchanged (exact untruncated antichain closure, Lemmas 0–5 as certified); this round's task
is (a) a concrete, cheap fix to the one outstanding rigor gap the reviewer flagged (round 2: citation
of `lemmas/periodicity-given-no-escape.md` with $P^*$ built from the eventual generator set, whose
literal hypothesis $\mathrm{primes}(a_1)\subseteq P^*$ is not obviously guaranteed), and (b) checking
whether the Singleton-Block observation from `leftover-witness-confinement` (step 5 above) gives an
independent, PC-free route to self-closing in the singleton-generator branch, tightening this file's
own Lemma 4 (Absorption)'s role.
Skeleton:
  1. Resolve the citation gap directly: either (i) prove $P^*\supseteq\mathrm{primes}(a_1)$ always
     holds (check whether $D_1=S$ can itself ever be fully dominated by a later, strictly smaller
     generator — by `lemmas/constraint-domination.md`, this would require some $D_j\subsetneq S$ with
     $j>1$, i.e. an early term whose prime set is a proper subset of $a_1$'s own; check this directly
     against the computational record, e.g. $a_1=15,105,385$), or (ii) re-derive
     `periodicity-given-no-escape.md`'s conclusion generic in $P$ (i.e. confirm and state explicitly
     that its proof body never actually uses $\mathrm{primes}(a_1)\subseteq P$, only $P$ finite and the
     No-Escape hypothesis, dropping the unused hypothesis from the citation).
  2. Re-derive Lemma 3 (periodicity) with the fixed citation, closing the previously-flagged "zero
     residual gap" claim honestly.
  3. Import the Singleton-Block observation: state explicitly that whenever $\mathcal A_n$ ever
     contains a singleton, this file's own Lemma 4 (Absorption) already finishes the theorem with no
     further antichain-closure machinery needed — sharpening the scope of the *remaining* open case to
     antichains with all blocks of size $\ge2$, matching `leftover-witness-confinement`'s scoping
     exactly (useful cross-check between the two independent routes).
Key lemmas (claim + mechanism): none new required beyond the citation-hygiene fix (step 1) — a concrete,
  bounded, closeable task this round, distinct from the open Antichain Stabilization target itself.
Open gaps: Antichain Stabilization itself remains open (unchanged); this round's build only closes the
  citation-hygiene gap and cross-checks scope with the sibling approach.
Cases to cover: the two sub-cases of step 1 (i)/(ii) — pick whichever resolves cleanest; both are
  legitimate fixes.
Watch out for: don't let this advance quietly re-claim "zero residual gap" without actually completing
  step 1 — the reviewer flagged this precisely because it was asserted without proof before.

---

global-smooth-density-contradiction: new
Target: the full theorem for every odd $a_1$, via a proof-by-contradiction architecture that never
constructs PC or Antichain Stabilization positively — genuinely orthogonal to the LCR/PC and
antichain-closure family (per the plateau-breaking rule: this is the round's required far-from-the-field
opening).
Technique: global density/counting contradiction (not per-step local charging, which is confirmed dead
three times — see `current.md` Rules), reusing two already-proved facts: the linear growth bound
$a_n\le a_1+(n-1)L_0$ (`lemmas/gap-bound.md`) and the smooth-number counting bound (elementary,
$M$-smooth integers up to $x$ number $O_M((\log x)^{\pi(M)})$, already proved from scratch in
`self-closing-pair-density-odd-case.md` Attempt 3) — deployed here in the *opposite* direction from
that file's negative use.
Skeleton:
  1. Suppose for contradiction the antichain $\mathcal A_n$ **never stabilizes**: infinitely many $n$
     are growth events (a genuinely new inclusion-minimal generator $D_n$ enters, not implied by any
     earlier generator).
  2. Each growth event's witnessing term satisfies $a_n\le a_1+(n-1)L_0=O(n)$ (gap-bound), so among the
     first $N$ growth events, the corresponding terms all lie in $[1,\,a_1+(n_N-1)L_0]$ for $n_N=O(N)$
     (the index of the $N$-th growth event, itself unbounded but the point range is controlled by it).
  3. **Central open task (the crux of this approach, honestly flagged as unresolved):** identify a
     "scarce resource" consumed by each growth event that is globally bounded across a range of size
     $X$ — candidates to test: (a) each growth event's term $a_n$, restricted to primes $\le L_0$
     (i.e. $D_n^P$), must be a genuinely new element of the *finite* lattice $2^P$ not yet seen as a
     truncated signature (by `lemmas/signature-stabilization-and-crt-sufficiency.md` Lemma A, this
     already happens only finitely often — so growth events with a new $D_n^P$ are automatically
     finite; the open sub-case is growth events whose $D_n^P$ *repeats* an old truncated signature but
     whose *untruncated* $D_n$ is still a new inclusion-minimal set, i.e. exactly PC-violating events);
     (b) count, via the smooth-number bound, how many integers up to $X$ can be $L_0$-smooth
     ($O((\log X)^{\pi(L_0)})$, polylogarithmic) versus how many growth events with a large prime factor
     the recursion could in principle need — if growth events forced to carry a large prime factor were
     shown to require a term from a set of density $\to0$, while gap-bound forces growth-event terms to
     appear with gaps $\le L_0$ (i.e. relatively densely, not sparsely) among all terms up to $X$, this
     tension may be sharpenable into a genuine counting contradiction — **this step is not yet completed
     and is the approach's real content**; the builder's job is to attempt to close it or report the
     precise obstruction if it does not close.
  4. If step 3 succeeds for a suitable scarce resource, conclude only finitely many growth events occur,
     i.e. Antichain Stabilization, hence the theorem via `lemmas/self-closing-antichain-sufficiency.md`.
Key lemmas (claim + mechanism):
  - Finite-truncated-signature sub-case is already closed — because
    `lemmas/signature-stabilization-and-crt-sufficiency.md` Lemma A gives $R_n$ (the set of $P$-truncated
    signatures) stabilizes by pigeonhole on the finite lattice $2^P$; so the only residual growth
    events are exactly those where $D_n^P$ repeats but $D_n\not\subseteq P$ (a PC violation) — this
    reduces global-smooth-density-contradiction's residual scope to precisely the same PC-violating
    events that `leftover-witness-confinement` targets directly, but via a counting argument on the
    *whole range* rather than a single minimal-counterexample step. **This is a valuable structural
    observation this round even without completing step 3**: it shows this "new" architecture, when
    made precise, converges onto the same set of events the other approaches attack, but from a global
    density angle instead of a single-index minimal-counterexample angle — worth recording either way.
Open gaps: step 3 in full; this is the field's most speculative/exploratory approach, explicitly
  acknowledged as such (per the explorer's own honest "medium-low, architecturally novel" rating). A
  clean negative result (showing this counting approach cannot close, with the precise reason) is a
  legitimate and valuable outcome, not a failure.
Cases to cover: the two growth-event sub-cases in step 3(a) (new truncated signature — closed; repeated
  truncated signature / PC violation — open, the residual target).
Watch out for: do not let this collapse back into the refuted per-step $O(\log a_n)$ charging shape —
  the scarce resource must be counted *globally* over a range $[1,X]$, not accounted per individual step
  $n$; if the builder finds the argument reducing to a per-step budget, that is itself the negative
  result to report (matching the three prior refutations), not a reason to force it through.
