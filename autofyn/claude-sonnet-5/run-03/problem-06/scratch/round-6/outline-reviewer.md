# Outline review — round 6

Scope reminder: even $a_1$ is fully closed and not touched. Every approach below targets the whole
theorem, with the only remaining content being $a_1$ odd. Five-plus rounds have bottomed out on one
shared target reached three equivalent ways (Antichain Stabilization / P-Confinement / "Step 6" /
Type B finiteness). This round's field: one genuinely new top-level framing (mandatory per the
plateau-breaking rule), one revision of the strongest existing narrowing, and one speculative third
framing.

---

## 1. `global-signature-purification` — new — **APPROVE**

**Verdict rationale.** This is a sound, well-specified outline, and — critically — a *genuinely
different top-level target*: it never forms the antichain-of-prime-sets object $\mathcal A_n$ at all.
Checked:

- The identification of $(a_n)$ with crux `aimo-0030`'s (IMO 2022 P3) "good numbers" game (fixed floor
  $b_0=k=a_1$, "coprime to none of $b_0,\dots,b_n$") is termwise exact — I re-read the problem
  statement and confirm the recursions match with zero translation needed. This is legitimate reuse
  under CLAUDE.md's rule ("a hint to adapt, never a citation") since the outline explicitly requires
  every borrowed step (Purification, Signature Determinacy) to be re-derived from scratch for our
  recursion's actual selection rule, not imported.
- Step 2 (nonempty small-prime signature for $x\ne k$) is a correct one-line consequence of $\gcd(x,a_1)>1$
  being forced (since $a_1$ is always among the "prior good numbers" the candidate must share a factor
  with) — no gap.
- The two flagged gaps (Purification's size bound $x^*\le x$; Signature Determinacy's induction) are
  each given a genuine mechanism, not a bare label: Purification's mechanism (large-prime factor is
  "wasted weight," replaceable by extra copies of a small prime already present, with the least such
  replacement provably $\le x$) is the actual content of the source proof's Claim 4, correctly
  restated; Signature Determinacy's mechanism (strong downward induction on $\max(x,x')$ over a minimal
  counterexample pair, using Purification to shrink the larger element) is the actual content of Claim
  5. Both are real, checkable proof shapes with a known-correct template, not hand-waves.
- Step 5 (periodicity of $\pi$ mod $L=\prod_{p\le k}p$, CRT) and Step 6 (periodic indicator on
  $[k,\infty)$ $\Rightarrow$ $a_{n+T}=a_n+L$ for every $n$, with $T$ = count of good numbers in one
  window) are both correct, standard, low-risk closing steps — I re-derived Step 6 independently: a
  periodic-mod-$L$ subset of $\mathbb Z_{\ge k}$, enumerated increasingly, is forced to repeat its own
  gap pattern every $T$ elements where $T$ is the window count; this holds unconditionally once
  periodicity of membership is established, no additional gap hidden here.
- The outline correctly distinguishes this from round 5's already-refuted *local* per-step transplant
  (moving floor $a_{i-1}$ vs. fixed threshold $a_1$) — this is a materially different, global claim,
  correctly flagged as unattempted, not a repeat of a dead end.
- The outline explicitly and correctly warns against smuggling circularity into Step 4's induction
  (assuming the very goodness-determinacy being proved) — good adversarial self-awareness, matches
  CLAUDE.md's rigor rules.

**One risk to flag for the builder (not fatal, watch closely):** the threshold discrepancy $P'=\{p\le
a_1\}$ vs. the population's $P=\{p\le L_0=\mathrm{rad}(a_1)\}$ is real — the source proof's size
inequality for Purification specifically needs $k<q$ (i.e. threshold $=a_1$) to make $x^*\le x$ work.
The explorer's own computational check (zero violations of pairwise-sharing at primes $\le L_0$,
several odd $a_1$) is suggestive but not dispositive that the smaller threshold suffices; the builder
should not assume $P'$ can be silently shrunk to $L_0$ without re-deriving the size bound for the
smaller set.

**This approach must be in the build set** per the run's plateau-breaking rule — it is the first
approach in 5+ rounds that does not touch $\mathcal A_n$/PC/Step 6 at all, and if it closes it is a
complete independent proof, not a lemma contribution.

---

## 2. `leftover-witness-confinement` — revise — **APPROVE (with one required fix)**

**Verdict rationale.** Steps 1–5 stay untouched (already reviewer-certified, correctly not re-derived).
The revision's new content — replacing Step 6's abstract hitting-set search with a "Coincidence Lemma"
($H:=\pi(m)$ forced to equal an earlier block $D_j$) — is honestly and correctly labeled speculative,
with a sound fallback instruction (test on existing data first, report a precise negative finding if
false, per CLAUDE.md's "record everything").

**Real flaw found in the stated mechanism, must be fixed before the builder invests full effort.** The
"mechanism to attempt" (Skeleton point 3) argues $m<a_1$ means "$m$ was already tested as a candidate
at step 2 of the recursion, rejected... or never reached." This premise is **false as stated**: the
recursion's candidates for $a_2$ are integers strictly greater than $a_1$ (the sequence is increasing
and every $a_n\ge a_1$), so no integer $m<a_1$ is ever, at any step, in the recursion's candidate range
— $m$ was literally never tested. Since the actual target is about the *signature* $\pi(m)$ coinciding
with an earlier block $D_j$ (not $m$ itself equaling an earlier term $a_j$), this flaw does not
necessarily kill the Coincidence Lemma's truth, but the specific justification offered is invalid and
must not be relied on as written. **Required fix:** the builder must either (a) find a different,
correct justification for why $\pi(m)$ should coincide with an earlier $D_j$ (not resting on "m was a
tested candidate"), or (b) test the lemma computationally first (as the outline itself instructs) and,
if the mechanism doesn't pan out, report the precise negative finding rather than force a flawed proof.

**Also carry forward** the already-flagged cosmetic fix: the complete-graph special case holds for
$k\ge3$, not $k\ge2$ ($k=2$ counterexample $H=\{p_1\}$ verified by the round-6 proof-reviewer).

---

## 3. `gcd-pigeonhole-omega-induction` — new — **APPROVE, low priority, bounded effort**

**Verdict rationale.** The base case ($\omega(a_1)=1$) is already unconditionally solved by citation
(`lemmas/singleton-generator-permanence.md`) — no gap. The pigeonhole fact (some fixed divisor $g_0>1$
of $a_1$ satisfies $\gcd(a_1,a_n)=g_0$ for infinitely many $n$) is a correct, cheap, always-true
consequence of finite divisor count — no gap, verified by inspection.

**The core inductive step (Reduction Lemma) has no mechanism at all** — the outline itself says so
plainly ("mechanism not yet found... explicitly flagged as such per the explorer's own caution").
This is exactly the "lemma named without its mechanism" pattern the review criteria warn against, and
it is worse than approach 2's flawed-but-present mechanism: there is no proposed argument here, only a
hoped-for shape. Compounding this, the outline admits the boundary case $R=S$ (where the pigeonhole
value is $a_1$ itself, giving no size decrease) "may turn out to be the generic/hard case" — i.e. the
easy case may not even be the common one.

**Why APPROVE rather than RETHINK.** The outline does not ask the builder to blindly write a proof of
an unfounded claim; it explicitly directs a *bounded computational check first* (does $R=S$ recur
often? is any reduction pattern visible in the existing 24-case dataset?) with instructions to report a
precise negative finding and stop if nothing is found — the same disciplined pattern that produced a
useful, reviewer-certified negative result for `dense-signature-vanishing` in round 2. This is a
legitimate low-cost use of a build slot, not a doomed full-proof commitment. Build it, but the builder
must not proceed to a "full induction" write-up unless the bounded check actually turns up a concrete
reduction mechanism — otherwise stop and report the negative finding, per CLAUDE.md's "record
everything."

---

## Diversity assessment

- Approach 1 (`global-signature-purification`) and approach 3 (`gcd-pigeonhole-omega-induction`) are
  genuinely new top-level framings, both avoiding $\mathcal A_n$/PC/Step 6 entirely — real diversity,
  not variations of one idea.
- Approach 2 (`leftover-witness-confinement`) is the only one still inside the antichain framing; it
  earns its slot on the strength of its already-certified Steps 1–5 (the field's most-narrowed target)
  plus a new (if currently flawed) mechanism attempt, not by re-patching a previously-failed
  combinatorial search.
- Per the outliner's own note and confirmed here: do not additionally advance
  `antichain-signature-closure` or `global-smooth-density-contradiction` this round (same Step 6 target,
  already owned by approach 2 with the fullest machinery); do not advance
  `self-closing-pair-density-odd-case` or `per-prime-divisor-chain-decomposition` (documented dead
  ends for their specific mechanisms, no new content this round).

## Ranking

Registered new approaches `global-signature-purification` and `gcd-pigeonhole-omega-induction`
(cold-start 1500), then ran `update_ranking` anchoring both against the established field: newcomers
beat the two dead-ends (`monovariant-telescoping`, `dense-signature-vanishing`) and, for
`global-signature-purification`, beat the plateaued antichain siblings (`antichain-signature-closure`,
`dilworth-antichain-bound`) reflecting the plateau-breaking priority; `global-signature-purification`
vs. `leftover-witness-confinement` recorded as a draw (both are the round's strongest bets, genuine
uncertainty, let build outcomes decide); `gcd-pigeonhole-omega-induction` loses to both live
established approaches it was compared against (`antichain-signature-closure`,
`leftover-witness-confinement`) reflecting its unfounded core step. Post-update Elo (best-first):
`leftover-witness-confinement` 1601.9, `global-signature-purification` 1574.9,
`antichain-signature-closure` 1561.6, `dilworth-antichain-bound` 1550.1,
`global-smooth-density-contradiction` 1502.0, `gcd-pigeonhole-omega-induction` 1483.4,
`dense-signature-vanishing` 1439.0, `monovariant-telescoping` 1361.8.

## Build set

All three approaches are approved for building this round: `global-signature-purification` is
mandatory per the plateau-breaking rule (first genuinely wall-independent framing in 5+ rounds, sound
skeleton, real gaps with real mechanisms); `leftover-witness-confinement` is the field's
most-narrowed, highest-Elo target and gets a required mechanism fix before its new Coincidence Lemma
attempt; `gcd-pigeonhole-omega-induction` is approved for a bounded, disciplined computational-check
effort only — the builder must stop and report a negative finding rather than force a proof if the
Reduction Lemma doesn't materialize.

build set: global-signature-purification, leftover-witness-confinement, gcd-pigeonhole-omega-induction
