## imo-2026-06

Scope note (applies to every approach below): even $a_1$ is fully solved
(`approaches/absorption-recurrence-even-case.md`, certified `lemmas/even-persistence.md`) — not
touched again. **Every approach below targets the whole theorem but its only remaining content is
$a_1$ odd.** The field has been stuck for 5+ rounds on one equivalent combinatorial target reached
three independent ways (Antichain Stabilization / P-Confinement / "Step 6" / Type B finiteness) —
per the plateau-breaking rule this round opens a **genuinely different top-level framing** (not a
same-wall bypass) as the primary bet, plus one targeted revision of the strongest existing
antichain-family narrowing with genuinely new technique, plus one more diversity opening. Do **not**
re-open `monovariant-telescoping`'s $|Q|<\infty$, `dense-signature-vanishing`'s `aimo-0680` transplant,
the refuted $O(\log a_n)$ per-step charging shape, "finite total prime pool $\Pi$," "star realizability,"
or "complete-graph realizability as a general shape" (all confirmed dead, see `current.md`).

---

### 1. `global-signature-purification` — **new**

**Target:** the whole theorem for odd $a_1$: $\exists T,L\in\mathbb Z_{>0}$ with $a_{n+T}=a_n+L$ for
*every* $n\ge1$.

**Technique.** Direct transplant (re-derived from scratch, not cited) of crux `aimo-0030`'s (IMO 2022
P3) "good numbers" purification + strong-downward-induction technique, applied **globally** with fixed
threshold $k:=a_1$ (not locally per step against the moving floor $a_{i-1}$ — that specific local
transplant was already tried and killed in round 5, concrete counterexample $a_1=15$, $a_{i-1}=1009$
vs. $q=17$; this is a materially different, global claim, unattempted). This **entirely bypasses**
the antichain-of-prime-sets object, PC, and "Step 6" — a genuinely different top-level target, not a
same-framing patch.

**Key observation (definitional, not a gap).** $(a_n)$ *is*, by its own recursive definition, the
increasing enumeration of "good" integers $\ge k=a_1$ in the sense of `aimo-0030`'s game with
$b_0=k$: $x$ is good iff $x=a_n$ for some $n$. This identification is immediate from the problem
statement (no translation needed — the two recursions are termwise identical), so Step 1 below is
bookkeeping, not the hard part.

**Skeleton.**
1. Fix $a_1=k$ odd. For $x\ge k$ define the **small-prime signature** $\pi(x):=\{p\le k : p\mid x\}$
   (note: threshold is $k=a_1$ itself, **not** $L_0=\mathrm{rad}(a_1)$ — see discrepancy note below;
   this is a self-contained new object, decoupled from the population's $P=\{p\le L_0\}$).
2. **Fact ($\pi(x)\ne\emptyset$ for every good $x\ge k$, $x\ne k$).** By definition, a good $x>k$
   must satisfy $\gcd(x,a_1)>1$; since every prime factor of $a_1=k$ is $\le k$ trivially, this forces
   $\pi(x)\supseteq(\text{some prime of }a_1)\ne\emptyset$. Immediate, one line.
3. **Purification Lemma (transplant of `aimo-0030` Claim 4).** For every $x\ge k$ with
   $\pi(x)\ne\emptyset$, there exists $x^*$ with $\pi(x^*)=\pi(x)$, $k\le x^*\le x$, and $x^*$ is
   $k$-smooth (no prime factor $>k$). *Construction:* let $a:=\prod_{p\in\pi(x)}p$ (squarefree), fix
   any $p_0\in\pi(x)$, let $m\ge0$ be least with $a\cdot p_0^m\ge k$, set $x^*:=a\cdot p_0^m$. Then
   $\pi(x^*)=\pi(x)$ automatically (multiplying $a$ by more copies of $p_0\in\pi(x)$ introduces no new
   prime). **Gap: the size bound $x^*\le x$** — needs the same case analysis as `aimo-0030`'s Claim 4
   (using that any prime factor $q>k$ of $x$ contributes a factor $\ge k+1$ that $x^*$ dispenses with,
   vs. minimality of $m$) — this is real work, re-derive fully, do not just cite.
4. **Signature Determinacy (transplant of `aimo-0030` Claim 5).** If $x,x'\ge k$ and $\pi(x)=\pi(x')$,
   then $x$ is good iff $x'$ is good. *Mechanism:* strong downward induction on $\max(x,x')$ over a
   minimal counterexample pair; use the Purification Lemma to replace the larger of $x,x'$ by a
   strictly smaller (or equal) same-signature representative $x^{**}\le\max(x,x')$, apply the
   induction hypothesis to the new, smaller-max pair, and derive the contradiction (a good/bad
   mismatch cannot survive purification, because goodness of $x^{**}$ is determined recursively only
   by which *earlier* good numbers it shares a prime with, and $\pi$ alone governs every such
   sharing test). **Gap: the full induction** — this is the technical heart, genuinely nontrivial (it
   is the load-bearing step of the source IMO problem's own solution), must be redone in full for our
   recursion's actual selection rule (not just asserted by analogy).
5. **Periodicity of $\pi$ (elementary, no gap).** $\pi(x)$ depends on $x$ only through $x\bmod
   L:=\prod_{p\le k}p$ (CRT: divisibility by each fixed $p\le k$ depends only on $x\bmod p$). So by
   Step 4, the indicator "$x$ is good" restricted to $x\ge k$ is periodic mod $L$.
6. **Conclusion.** A periodic (period $L$) subset of $[k,\infty)$, enumerated in increasing order as
   $a_1<a_2<\cdots$, satisfies $a_{n+T}=a_n+L$ for *every* $n\ge1$, where
   $T:=\#\{x\in[k,k+L):x\text{ good}\}\ge1$ (since $a_1=k$ itself is good and lies in this window) —
   a standard, easy re-indexing fact (small lemma, not a real gap). This is exactly the theorem's
   conclusion, for every $n\ge1$, not merely eventually — matching the problem statement precisely.

**Key lemmas (claim + mechanism):**
- Purification Lemma — because any large-prime ($>k$) factor of $x$ is "wasted weight" that can be
  replaced by extra copies of a *small* prime already in $x$'s signature without changing which small
  primes divide the result, and the minimal such replacement is provably $\le x$.
- Signature Determinacy — because goodness is a recursively-defined property that only ever tests
  gcd-sharing with earlier good numbers, and sharing a prime is entirely determined by $\pi$; a
  minimal-counterexample-by-value induction combined with Purification eliminates any value-dependence
  beyond signature.
- Periodic-enumeration Corollary — because a periodic subset of $\mathbb Z$, listed in increasing
  order, is forced to repeat its own increasing-order gap pattern every $T$ elements.

**Open gaps:** the two starred items above (Purification's size bound; Signature Determinacy's full
induction) are unproved — this is the entire content the builder must supply. Both are substantial but
have a known correct template (the source IMO 2022 P3 solution) to adapt, not a wall the population has
hit before.

**Cases to cover:** none beyond odd/even (even already closed elsewhere); Signature Determinacy's
induction itself will likely need an internal case split (which of $x,x'$ purifies below the other,
and whether $x^{**}$ collides with $k$ itself) — flag this for the builder, do not skip.

**Watch out for:**
- The threshold discrepancy: this approach uses $P':=\{p\le a_1\}$, **not** the rest of the
  population's $P=\{p\le L_0=\mathrm{rad}(a_1)\}$. Do **not** try to reuse `lemmas/gap-bound.md`,
  `lemmas/constraint-domination.md`, or any $P$-indexed lemma from the antichain family without
  re-deriving them for $P'$ — this approach should be **self-contained**, importing only the bare
  problem statement and (if convenient, as a sanity re-check, not a dependency) the fact that even
  $a_1$ is already closed.
- Step 4's induction genuinely needs $x^{**}\ge k$ preserved at every step (Purification already
  guarantees this) and must not silently assume the very goodness-determinacy it is proving when
  handling the recursive "earlier good numbers" structure — this is the single easiest place to
  smuggle in circularity, exactly as CLAUDE.md's rigor rules warn against.
- If this closes, it **fully proves the theorem** with zero remaining dependence on Antichain
  Stabilization / PC / Step 6 — a strictly different, complete alternate proof, not merely a lemma
  contribution to the existing chain.

---

### 2. `leftover-witness-confinement` — **revise** (inject purification into Step 6)

**Target:** unchanged — the whole theorem for odd $a_1$, via PC $\Rightarrow$ theorem
(`lemmas/pc-implies-theorem.md`, already certified, zero secondary gap).

**Technique.** Keep the file's fully-certified Steps 1–5 (minimal-counterexample descent on PC,
Leftover-Witness Dichotomy, singleton case closed two ways) exactly as is — these are correct and
reviewer-verified, re-proving them would be wasted effort. **Re-plan only "Step 6"** using the
Step-6-realizability explorer's secondary opening: apply a **purification-style downgrade** directly
to the witness $H=\pi(m)$ (population's own $\pi$, w.r.t. $P=\{p\le L_0\}$) constructed in Step 3,
instead of trying to rule out abstract hitting-but-not-containing sets combinatorially (which the
reviewer's counterexample $\{1,2\},\{1,3\},\{1,4\}$ shows cannot work without more structure).

**Skeleton (only the new Step 6 content; Steps 1–5 imported verbatim from the current file).**
1. Recall (Step 3 of the existing file): if PC fails at minimal generator index $n$, then
   $m:=a_n/q^e<a_1$ (Case A forced) and $H:=\pi(m)\subseteq P$ hits every block of $\mathcal A_{n-1}$
   without containing any.
2. **New Coincidence Lemma (target).** Show $H$ (or a purification of $H$, same idea as Approach 1's
   Purification Lemma but instantiated with $P$'s threshold $L_0$ instead of $a_1$) is forced to equal
   $D_j$ for some earlier generator $j<n-1$ — i.e., $H$ is not just an abstract set but is *realized*
   by an actual earlier term of the sequence. If this holds, $H=D_j\subseteq H$ trivially contains
   the block $D_j\in\mathcal A_{n-1}$, contradicting condition (ii) (no block contained) — **directly
   closing Step 6** by converting Case A back into a Case-B-style contradiction, the exact route the
   round-6 explorer flagged as promising and not yet tried.
3. *Mechanism to attempt:* $m<a_1$ means $m$ was already a "candidate" considered at some earlier step
   of the recursion (every positive integer $<a_1$ is $<a_2<\cdots$, so $m$ was tested for validity at
   step $2$ and rejected only because it failed some earlier gcd constraint, **or** $m$ itself never
   got tested because a smaller *valid* candidate won at that step). Use this to try to exhibit $m$ (or
   its small-prime part) as literally equal to some $a_j$, $j<n$, or show a contradiction if it is not.
   This is genuinely new content (not attempted in any round yet) — flag honestly as **speculative**,
   with a concrete fallback: if the Coincidence Lemma turns out false in general (test computationally
   first, on the same $a_1=15,105,385$ data already in the file), report the negative finding precisely
   (which specific step of the mechanism breaks) rather than silently abandoning it.

**Key lemmas:** Coincidence Lemma (claim above) — because $m<a_1$ constrains $m$ to have already been
a real, tested candidate in the recursion's own history (not an arbitrary abstract integer), which is
structural information Step 6's purely combinatorial framing (abstract antichains) has never used.

**Open gaps:** the Coincidence Lemma itself (entirely new; may be false — test on existing data first,
this round, before committing to a full proof attempt).

**Cases to cover:** whichever cases the Coincidence Lemma's proof needs (likely: $m$ was tested and
lost to a smaller valid candidate at its own step, vs. $m$ was never reached because the floor had
already passed it — both need separate handling).

**Watch out for:** don't re-derive Steps 1–5 (already certified, `lemmas/leftover-witness.md`,
`lemmas/singleton-generator-permanence.md`) — only Step 6 changes. Also fix the file's own flagged
cosmetic error (complete-graph special case holds for $k\ge3$, **not** $k\ge2$; $k=2$ has explicit
counterexample $H=\{p_1\}$) while touching the file.

---

### 3. `gcd-pigeonhole-omega-induction` — **new**

**Target:** the whole theorem for odd $a_1$, via a completely different top-level architecture: strong
induction on $\omega(a_1)$ (number of distinct prime factors of $a_1$) rather than a fixed-point
stabilization claim about one sequence's evolving antichain state. Avoids the antichain-of-prime-sets
object entirely — third genuinely different framing this round.

**Technique.** Combine two openings from the fresh-framing explorer: (a) `aimo-0421`'s
finite-divisor-values pigeonhole on $\gcd(a_1,a_n)$, and (b) descent on the scalar invariant
$\omega(a_1)$, with $\omega(a_1)=1$ (prime power) as the fully-solved base case
(`lemmas/absorption-lemma.md` + `lemmas/singleton-generator-permanence.md`: a prime-power $a_1$ forces
immediate singleton collapse, theorem holds with $T=1,L=p$).

**Skeleton.**
1. **Base case ($\omega(a_1)=1$).** Already unconditionally proved: $a_1=p^e$ forces singleton
   antichain collapse at $n=1$ trivially, giving $a_n=a_1+p(n-1)$. Cite
   `lemmas/singleton-generator-permanence.md` directly, no new work.
2. **Pigeonhole fact (cheap, always true, no gap).** For $n\ge2$, $\gcd(a_1,a_n)>1$ (forced by the
   defining constraint against $i=1$) and $\gcd(a_1,a_n)\mid a_1$, so it takes one of the $\le d(a_1)-1$
   nontrivial divisor values of $a_1$; by pigeonhole on an infinite sequence into a finite set, some
   fixed divisor $g_0>1$ satisfies $\gcd(a_1,a_n)=g_0$ for infinitely many $n$. Let $R:=\mathrm{primes}
   (g_0)\subseteq S:=\mathrm{primes}(a_1)$, nonempty.
3. **Reduction Lemma (target, genuinely new, currently unestablished — the load-bearing gap).**
   Attempt to show: the tail behavior of $(a_n)$ is governed by (reduces to, in the sense of producing
   the same eventual period structure as) the sequence generated by the smaller seed
   $a_1':=g_0$ (or $\mathrm{rad}(g_0)$), which has $\omega(a_1')\le\omega(a_1)-1$ (since $g_0\mid a_1$,
   $g_0\ne a_1$ is not guaranteed in general — **this needs to be checked/forced**: if $g_0=a_1$ i.e.
   $R=S$, the reduction is vacuous and this route needs a different argument for that case,
   flagged explicitly below). If a genuine reduction can be built (e.g., by showing infinitely many
   terms $a_n$ restricted to their $R$-primes already behave exactly like a fresh instance of the
   recursion seeded at $g_0$), induction on $\omega(a_1)$ closes the theorem.
4. **Conclude by strong induction** once Step 3 is established: base case $\omega=1$ (done), inductive
   step reduces $\omega(a_1)$ to a strictly smaller value's already-proved case.

**Key lemmas:**
- Pigeonhole divisor-recurrence fact — because $\gcd(a_1,\cdot)$ is a divisor of the fixed integer
  $a_1$, hence has finitely many possible values, forcing some value to recur infinitely often in any
  infinite sequence.
- Reduction Lemma — **mechanism not yet found**; this is honestly the speculative core of the whole
  approach, explicitly flagged as such per the explorer's own caution (no reduction lemma was
  constructed or verified in exploration).

**Open gaps:** the entire Reduction Lemma (Step 3) — including the boundary case $R=S$ where the
pigeonhole value is $a_1$ itself and no size decrease is available (may need a wholly different
sub-argument there, e.g. falling back to the antichain machinery only for that residual case, or
finding that $R=S$ recurring forces a structural fact — e.g. that $S$ itself is eventually always
achievable via one common divisor pattern — worth checking computationally first).

**Cases to cover:** $R\subsetneq S$ (genuine size decrease, main inductive case) vs. $R=S$ (degenerate,
needs separate handling or may turn out to be the generic/hard case — check this computationally
before investing further proof effort).

**Watch out for:** this is the most speculative approach of the four — explicitly the "third opening,
lower-confidence" diversity slot per the dispatch note. Builder should spend an early, bounded effort
checking computationally (on the existing 24-case dataset already built by
`self-closing-pair-density-odd-case`) whether $R=S$ recurring is common or rare, and whether any clean
reduction to a smaller seed is even visible in the data, **before** committing to a full proof attempt
— if the reduction doesn't show up in data, report a precise negative finding (per CLAUDE.md's
"record everything") rather than force a proof.

---

### Cross-cutting notes for the outline-reviewer

- Approaches 1 and 3 are **new top-level framings**, deliberately avoiding the antichain-of-prime-sets
  object that approaches 2 (and the population's other live antichain-family files) all still use —
  satisfies the plateau-breaking rule (round 5/6 shared-wall diagnosis in `current.md`).
- Approach 2 is the only one still inside the antichain framing; it earns its slot by injecting a
  genuinely new mechanism (purification-derived Coincidence Lemma) into the single most-narrowed open
  target in the population, not by re-patching the same combinatorial hitting-set search that has
  already failed twice (star realizability, complete-graph realizability).
- Do **not** additionally advance `antichain-signature-closure` or `global-smooth-density-contradiction`
  this round — both converge on the exact same "Step 6" target that approach 2 already owns with the
  fullest machinery (`lemmas/leftover-witness.md`, `lemmas/singleton-generator-permanence.md`); building
  them in parallel would be the single-shared-gap trap flagged in memory rule 5. Leave them live,
  unbuilt, for a future round if approach 2's new mechanism stalls.
- Do **not** advance `self-closing-pair-density-odd-case` or `per-prime-divisor-chain-decomposition`
  this round — both are checked, documented dead ends for their specific mechanisms (finite-prime-pool
  reduction; all three per-prime monovariant candidates) with no new content to add; they remain useful
  as recorded negative results only.
- If approach 1 (`global-signature-purification`) succeeds, it fully subsumes and moots approaches 2
  and 3 (a complete, independent proof). If it stalls, approaches 2 and 3 remain live, genuinely
  different fallbacks — this is intentional portfolio diversity, not redundant effort.
