# Outline review — round 5 — imo-2026-06

Scope confirmed: even-$a_1$ is closed and out of scope. All four candidates below correctly target
odd $a_1$, the entire remaining content of the theorem. No approach repeats a confirmed dead end
(checked against `current.md` Rules: aimo-0680 transplant, $|Q|<\infty$, $O(\log a_n)$ charging in
any dressing, $\sigma_p/\tau_p$, aimo-0030 transplant, universal-Dirichlet-forces-Absorption — none
of the four reappear).

## 1. `leftover-witness-confinement` (revise of `dilworth-antichain-bound`) — APPROVE, highest priority

This is real, verified new content, not a repackaging. I independently re-derived and computationally
re-checked the central claim from scratch (fresh Python simulation, not reusing the explorer's code),
for $a_1\in\{15,21,105\}$ up to 400 terms: **zero violations** of the Leftover-Witness dichotomy across
all large-prime-factor instances, and (separately) **zero** generator terms ever carry a prime $>L_0$
in the tested range, consistent with PC holding throughout. This matches the explorer's 1233/1233 claim
with an independent implementation, so I trust the mechanism, not just the report.

Checked the logic chain step by step:
- **LCR's ($\Leftarrow$) direction genuinely doesn't need $x>a_{i-1}$.** I re-read the certified
  `lemmas/local-congruence-reduction.md` proof body directly: the ($\Leftarrow$) proof only uses
  Constraint Domination and $D_j\subseteq P$ for $j<i$; the hypothesis $x>a_{i-1}$ never appears in
  the proof body (it's part of the lemma's stated scope, not used). The outline's claim that this
  lets $m=a_n/q^e$ (any size) be shown "globally valid" is therefore correct, not a leap.
- **Case A/B is exhaustive.** Given $m$ globally valid against $a_1,\dots,a_{n-1}$: if $m\ge a_1$,
  the standard "smallest valid candidate" argument (find $k$ with $a_{k-1}<m\le a_k$, use minimality
  of $a_k$) forces $m=a_k$ exactly. One subtlety not spelled out in the outline: this requires $k\le
  n-1$, i.e. $m<a_n$ — but $m=a_n/q^e<a_n$ trivially since $q^e>1$, so this is automatic, not a gap.
  I checked this myself since the outline's sketch doesn't explicitly rule out $k=n$; it turns out
  $k=n$ would itself force $m<a_n$ to be a smaller valid candidate than $a_n$ at the same step,
  contradicting $a_n$'s own minimality even faster — so the case split is sound either way. Confirmed
  exhaustive and (modulo the $m=a_1$ boundary convention flagged by the outline itself) mutually
  exclusive.
- **Case B domination is real, not circular.** $a_n=q^e\cdot a_j$ with $j<n$ gives $D_j\subseteq D_n$
  trivially (every prime of $a_j$ divides $a_n$); combined with $j<n$ this directly contradicts $D_n$
  being assumed inclusion-minimal (a genuine new generator) at the top of the minimal-counterexample
  setup. This is a clean, non-circular application of `constraint-domination.md`, not an assumption of
  the conclusion.
- **Singleton-Block sub-lemma is correct**: hitting and non-containment of a size-1 block are
  literally the same condition, so they're jointly unsatisfiable — trivial once stated, correctly
  flagged as immediate.
- **Step 6 (core open target) is honestly scoped as open**, not glossed over — the outline explicitly
  states it as unresolved and describes the residual case precisely (antichains with no singleton
  block). This is the correct, narrower open target; it is a genuine narrowing of PC, not a
  restatement of the whole wall (verified by hand on the $a_1=15$ triangle $\{2,3\},\{2,5\},\{3,5\}$:
  any 2-element hitting set of this specific triangle already *equals* one of the blocks, so
  hit-but-not-contain is impossible there — consistent with this configuration being known to
  self-close).

One thing to tell the builder explicitly: the "no size restriction needed" corollary of LCR's
($\Leftarrow$) direction should be certified as its own lemma file before other approaches lean on it
(the outline already says this — keep it).

No fatal flaw found. Real narrowing of the gap, verified mechanism. **APPROVE, build.**

## 2. `antichain-signature-closure` (advance) — APPROVE, cheap and useful

Pure rigor-hygiene fix (the reviewer-flagged citation gap: $P^*\supseteq\mathrm{primes}(a_1)$ not
verified for `periodicity-given-no-escape.md`). Both sub-options in step 1 are legitimate and cheap.
Also cross-checks scope with `leftover-witness-confinement`'s Singleton-Block finding (both converge on
the same "no singleton block" residual case independently — a useful consistency check between two
independently-built routes, worth having in the population this round). No new gap introduced, no
overclaiming. **APPROVE, build** — low cost, closes an outstanding flagged issue.

## 3. `global-smooth-density-contradiction` (new) — APPROVE as this round's required diversity opening

This is the field's honest attempt at the CLAUDE.md plateau-breaking requirement (odd-case wall has
now stood 4 rounds). Architecture is genuinely different in kind from the other three: global
counting/density over a range $[1,X]$ in a proof-by-contradiction shape, vs. local minimal-counterexample
induction on the generator index (used by `leftover-witness-confinement`,`antichain-signature-closure`,
`dilworth-antichain-bound`). It correctly avoids resurrecting the refuted per-step $O(\log a_n)$
charging shape (explicitly flagged as a trap to avoid in "Watch out for"), and it reuses only
already-certified facts (gap-bound, the smooth-number counting bound proved from scratch in round 4).
**Caveat, worth flagging to the orchestrator**: the outline itself admits (in "Key lemmas") that once
made precise, this approach's residual scope collapses onto *exactly* the same PC-violating events
`leftover-witness-confinement` targets — so while the *mechanism* is new, the *target* is not
independent; if step 3 fails to close, this is evidence (not proof) that the wall is mechanism-agnostic,
which is itself valuable information for the orchestrator's plateau diagnosis. Step 3 (the "central open
task") is honestly unresolved, and the outline correctly treats a clean negative result as an acceptable
outcome, not a failure to hide. **APPROVE, build** — satisfies the diversity requirement in good faith.

## 4. `phi-weighted-antichain-monovariant` (revise of `self-closing-pair-density-odd-case`) — APPROVE but flagged as NOT the diversity-breaker; defer this round

Judged against the dispatch's specific question: this is **not** a genuinely different framing from
the antichain family — it operates on the exact same object $\mathcal A_n$ (the antichain of minimal
prime-sets) that `antichain-signature-closure`/`leftover-witness-confinement`/`dilworth-antichain-bound`
all already use, seeking a monovariant/potential-function proof of the same Antichain Stabilization
target. The one genuine novelty is that the candidate potential $\Phi_n=\sum_F L_0^{-|F|}$ is a *joint*
statistic over blocks rather than a per-prime one (correctly distinguishing it from the refuted
$\sigma_p/\tau_p$ per-prime monovariants), which is a real, not-yet-tried angle and worth keeping in the
population — but it is a **technique variant within the antichain-machinery family**, not an
independent top-level framing, and should not be counted toward the "genuinely different mechanism"
quota (that's `global-smooth-density-contradiction`'s job this round). The outline is also honest that
step 2 (computational test) must happen *before* any proof claim, and correctly treats a negative
result as legitimate. Soundness of the outline itself is fine (no circular step, no unjustified leap —
it hasn't gotten far enough yet to have one), but it is the most exploratory and least mechanistically
distinct of the four, and its very first deliverable (the computational test) is cheap enough that a
future round's explorer could resolve it before committing a full builder slot. **APPROVE for the
population (register, keep live), but not in this round's build set** given "few strongest, normally
1-3" — the other three are stronger uses of this round's build budget. Recommend revisiting next round
once $\Phi_n$'s behavior is tested (either by this round's builders' spare capacity, if any, or a
future explorer).

## Field diversity verdict (for the orchestrator)

The odd-case wall (PC / Antichain Stabilization) has now stood 4 rounds. This round's field: 3 of 4
candidates (`leftover-witness-confinement`, `antichain-signature-closure`, `phi-weighted-antichain-monovariant`)
still operate on the antichain object, using local induction, local induction, and a joint monovariant
respectively — real technique diversity within one framing, not framing diversity. Only
`global-smooth-density-contradiction` is a genuinely different top-level architecture (global
contradiction vs. local construction), and even it admits converging onto the same event set. This
satisfies CLAUDE.md's "at least one live approach attacks from a genuinely different framing" bar for
this round, but only barely — if `global-smooth-density-contradiction`'s step 3 fails to close this
round, the orchestrator should treat that as strong evidence the underlying obstruction (which
PC-violating/growth events are permitted) is genuinely mechanism-agnostic, and push next round's
explorers toward frameings that avoid the antichain-of-prime-sets object *entirely* (e.g. a direct
argument about the integer sequence's residues/gaps without ever forming $D_i$), rather than another
counting/potential dressing of the same object.

## Ranking

Registered new slugs `leftover-witness-confinement`, `phi-weighted-antichain-monovariant`,
`global-smooth-density-contradiction` (cold-start Elo 1500). `antichain-signature-closure` keeps its
existing slug (advance). Ran `update_ranking` with comparisons anchoring each newcomer against
established siblings: `leftover-witness-confinement` beat `dilworth-antichain-bound` (its parent) and
`antichain-signature-closure` (sharper, verified narrowing); `antichain-signature-closure` beat
`growth-bound-density`/`core-signature-pigeonhole` and drew with sibling `self-closing-pair-density-odd-case`;
`global-smooth-density-contradiction` beat the dead `dense-signature-vanishing` and beat
`phi-weighted-antichain-monovariant` (more clearly novel architecture); `phi-weighted-antichain-monovariant`
beat the dead `monovariant-telescoping` but lost to `dilworth-antichain-bound` (established, more
concrete). Post-update Elo order (top): `dilworth-antichain-bound` (1568) ≈
`antichain-signature-closure` (1567) ≈ `leftover-witness-confinement` (1566) >
`self-closing-pair-density-odd-case` (1560) > `growth-bound-density` (1522) >
`global-smooth-density-contradiction` (1516) > `dense-signature-vanishing`/`phi-weighted-antichain-monovariant`/
`core-signature-pigeonhole` (1464-1476) > `monovariant-telescoping` (1381, dead-end floor).

build set: leftover-witness-confinement, antichain-signature-closure, global-smooth-density-contradiction
