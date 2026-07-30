## imo-2026-06

### Assigned lens
Extremal/minimality attack on the shared crux ("Lemma A" / "Structural Lemma" / "R finite"), NOT via
the abstract E_∞-covering machinery. Below: what a smallest-counterexample argument buys you, where it
gets stuck, a genuinely new equivalent reformulation discovered by direct experiment, and why the most
tempting "shortcut" (peel off the large prime) turns out to be circular.

### Distinct openings

1. **Minimal-index counterexample to the Structural Lemma (the natural extremal setup).**
   Structural Lemma (from density-bounded-recruitment, restated tightly with P_max instead of a_1):
   *every two terms a_i, a_j share a prime ≤ P_max.* Take **j minimal** such that a_j fails to share a
   small prime with SOME earlier a_i (equivalently: j minimal witnessing Lemma A somewhere in the
   prefix). Minimality of j is genuinely useful: it forces **all pairs among a_1,...,a_{j-1} to
   pairwise share a small prime with each other** (not just with a_1) — a clean, usable induction
   hypothesis, stronger than what "Lemma A holds for all earlier pairs" alone would give. This is real
   progress over the un-anchored statement of Lemma A. The unresolved sub-problem it leaves: using this
   pairwise-small-intersecting prefix, construct (or prove existence of) a candidate M with
   a_{j-1} < M < a_j that is compatible (via any prime, small or large) with all of a_1,...,a_{j-1},
   contradicting minimality of a_j. This is a genuine covering/hitting-set-in-a-short-window problem —
   see "collapses" below for why it isn't just a counting triviality.

2. **NEW sharp reformulation, discovered by direct experiment: the two greedy processes coincide
   exactly.** Define the "reduced" process: b_1 = a_1, and b_{n+1} = the smallest integer > b_n such
   that for every i ≤ n, primes(b_{n+1}) ∩ primes(b_i) ∩ [2, P_max] ≠ ∅ (i.e., compatibility checked
   using ONLY primes ≤ P_max, ignoring any large-prime connections). This is a manifestly finite-state
   process (finite universe of candidate primes ≤ P_max), so periodicity for (b_n) is comparatively
   easy. **Numerically verified EXACT termwise equality b_n = a_n for every n (not just eventually),
   across every seed tested** (see Small-case notes). If this equality can be proved, the whole problem
   is immediate: b is manifestly periodic (finite covering system mod L = ∏(primes ≤ P_max)), so a is
   too. This reformulates the crux as a clean **induction target**: strong induction on n, IH "b_k=a_k
   for k ≤ n," want "a_{n+1} is automatically reduced-compatible" (i.e., shares a small prime with
   EVERY a_i, i≤n, not just some prime). One direction of the inequality (a_{n+1} ≤ b_{n+1}) is trivial
   (reduced-compatible ⟹ really-compatible, so the reduced-min is an upper bound on the real-min); the
   whole difficulty is the reverse inequality, and it is exactly as hard as Lemma A restated — but the
   induction packaging (assume the two SEQUENCES have matched up to n, not just "R has been finite so
   far") may be a cleaner scaffold for the outliner to hang a genuine inductive argument on.

3. **The "peel off the large prime" idea — looks promising, is actually circular (report as a dead
   end for THIS round, save the outliner the wasted cycle).** For every observed term a_n divisible by
   some prime q > P_max, writing a_n = q^e·v (v coprime to q), it was found (100% of ~60 sampled
   instances across 9 seeds) that **v ≤ a_{n-1}** and **v is compatible with every earlier term**. This
   looks like a mechanism ("the large prime is just decoration on an already-compatible small base, and
   that base was already too small to be a fresh candidate"). But tracing WHY v is always compatible
   with every earlier term shows it is a direct COROLLARY of the Structural Lemma itself (if a_n shares
   a small prime with every earlier a_k, that small-prime part survives when q is divided out) — so this
   observation cannot be used to prove the Structural Lemma without assuming it first. Do not let the
   outliner mistake this for an independent route; flag it explicitly as circular.

4. **Window/hitting-set counting angle (why opening 1's endgame is NOT a free counting argument).**
   Naively one might hope: since a_1,...,a_{j-1} pairwise share small primes (a finite universe of
   size π(P_max)), and gaps are bounded (a_{n+1}-a_n ≤ a_1, certified fact), pigeonhole/CRT should give
   a small-prime-only candidate in every window of length a_1. This is FALSE in general as a generic
   counting fact: CRT only guarantees a representative of a chosen hitting pattern within a window of
   length equal to the *product* of the primes involved, which can vastly exceed a_1 (e.g. if a_1 is a
   large prime, P_max = a_1 itself, and the "universe" of small primes has up to π(a_1) elements — the
   product of even a handful of mid-sized primes ≤ a_1 can dwarf a_1). So the endgame of opening 1
   needs a real structural argument (using that the a_i's ALREADY realize a common small-prime hitting
   pattern, not an arbitrary one) — this is where the genuine difficulty of the whole problem lives, and
   it is not solved by generic counting/pigeonhole.

### Candidate technique(s)
- Minimal-counterexample / smallest-witness extremal argument (**KB: Pigeonhole/extremal principle**;
  **KB: minimal-counterexample / no minimal counterexample can exist** entries).
- Strong induction packaged as "two greedy sequences agree termwise" (opening 2) — a cleaner
  formalization target than the abstract "R is finite" framing; still needs the same hard step.
- CRT / finite covering systems (**KB: Modular arithmetic, CRT**) — for the EASY direction (periodicity
  of the b-process once matched), not for closing the hard direction.

### Cheap-kill candidates
- None of the extremal ideas above close the gap outright; all reduce to the same hard step (large
  prime is never uniquely load-bearing). No new cheap kill found this round beyond what's already
  certified (gap bound a_{n+1}-a_n ≤ a_1; every term shares a prime with primes(a_1)).
- The "peel the large prime" mechanism (opening 3) is NOT a cheap kill — flagged explicitly as
  circular, do not spend a build cycle on it as an independent lemma.

### Knowledge-base entries to use
- Pigeonhole / extremal principle (General Proof Methods / Combinatorics section).
- "No minimal counterexample can exist" (induction's dual) — for organizing opening 1/2 as a genuine
  minimal-counterexample proof by contradiction.
- Modular arithmetic, CRT — for the covering-system periodicity of the b-process once/if matched to a.
- Divisor analysis (gcd structure, bounding search by size) — background for any hitting-set argument.

### Analogous past problems (cruxes)
No new analog beyond what round-1 already surfaced (aimo-0680's divisibility-squeeze, aimo-0447's
witness-prime grid encoding). Neither directly supplies the missing mechanism for "why can't a large
prime ever be the sole connector" — that combinatorial fact about greedy minimality with an unbounded
history appears to be genuinely novel to this problem, confirming round-1's note that no crux offers a
ready template for the actual hard step.

### Prior progress
Unchanged from `current.md`: full rigorous reduction to Lemma A / R finite / Structural Lemma (three
equivalent phrasings), certified lemmas (enumeration-of-E-infinity, periodic-set-enumeration), gap bound
a_{n+1}-a_n ≤ a_1, and now (this round) a fourth equivalent phrasing — **exact termwise coincidence of
the real process with the small-primes-only reduced process** — which is a genuinely different-looking
target (a process-identity, not a set-finiteness claim) worth handing to the outliner as an alternative
formalization to build the induction around.

### Dead ends (do not retry)
- Opening 3 (peel off the large prime / cofactor-≤-predecessor mechanism) as an INDEPENDENT proof route:
  verified circular — it is a corollary of the crux, not a path to it. (New finding this round.)
- Generic pigeonhole/CRT counting to fill the gap in opening 1/4: shown to fail in general because
  window length a_1 can be far smaller than the product of primes needed to guarantee a hitting-set
  representative by CRT alone (new structural observation this round — the argument must use that the
  a_i's realize a SPECIFIC already-achieved hitting pattern, not a generic one).
- (Carried from round 1 / density-bounded-recruitment) pure density/asymptotic arguments cannot isolate
  load-bearing primes, since E_∞ periodic ⇒ every recruited prime meets it in positive density; still
  valid, still a dead end for that specific technique.

### Small-case / intuition notes (all conjectural — numerical evidence only)
- **Structural Lemma (every pair of terms shares a prime ≤ P_max)**: verified with 0 violations across
  13 seeds (a_1 ∈ {6,15,30,35,63,77,99,105,143,182,255,1001,2310}), pairs checked among the first
  200–500 terms each — including a_1 = 2310 = 2·3·5·7·11 (five distinct small primes) with no failures.
- **NEW: exact process coincidence (opening 2)**: for every seed tested (a_1 ∈ {15,35,77,105,143,1155,
  182,97,2431}, including a_1 = 97 a bare prime and a1=2431=11·13·17), the "small-primes-only" greedy
  sequence b_n matches the true sequence a_n **exactly, term for term**, for all n up to 150–200 terms
  checked — not merely eventually. This is stronger evidence than the earlier Lemma-A pair-checking and
  suggests the true theorem might be provable as an exact (not just eventual) statement, potentially
  simplifying case analysis (no "transient" phase needs separate handling if the two processes never
  diverge even once).
- The "cofactor ≤ predecessor" fact (opening 3) held in 100% of ~60 sampled large-prime-bearing terms
  across 9 seeds, but — as explained above — is a downstream consequence, not new leverage.
- All of the above remain CONJECTURES verified only by finite computation (≤ ~500 terms, ≤ ~15 seeds);
  none constitute a proof of Lemma A / the Structural Lemma / process-coincidence.
