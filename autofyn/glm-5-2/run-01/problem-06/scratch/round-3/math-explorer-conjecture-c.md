# imo-2026-06 — math-explorer (conjecture-C / structural lens)

## Distinct openings (each a different attack the outliner could build into a rival approach)

1. **[W ⟹ (C) — the clean reduction, NEW this round]** Conjecture (C) (`A_n ∩ (a_n, a_n+R] ⊆ B_n`) follows from a single, purely structural fact **W**:
   > **(W)** *For every small-support class `σ* ∈ F'_n`, the class `{a_i : i≤n, σ_i=σ*}` contains at least one **R-smooth** term `a_j` (i.e. `supp(a_j) ⊆ P_R`, all prime factors `≤ R`).*

   **Proof that W ⟹ (C)** (rigorous, short): take `m ∈ A_n ∩ (a_n, a_n+R]` and suppose `m ∉ B_n`. Then `σ(m)` misses some `σ* ∈ F'_n`. By (W), pick `a_j` (`j≤n`) with `σ_j = σ*` and `supp(a_j) ⊆ P_R`. Since `m ∈ A_n`, `gcd(m, a_j) > 1`; any prime `p | gcd(m,a_j)` lies in `supp(a_j) ⊆ P_R` (so `p ≤ R`) and in `supp(a_j)` hence in `σ*`; also `p | m` so `p ∈ σ(m)`. Thus `p ∈ σ(m) ∩ σ* ≠ ∅` — contradicting "`σ(m)` misses `σ*`". Hence `m ∈ B_n`. ∎

   Since (C) ⟹ B1' trivially (B1' is just the minima-coinciding consequence), **W is a single clean sufficient target for the whole crux.** This reframes B1' from a "greedy-minimum coincidence" (hard to handle) to a "structural property of the σ*-classes" (has inductive flavor).

2. **The "uncompensatable `σ(a_1)`-class" — a one-sided partial proof of (C) that needs NO new idea.** `a_1`'s prime support is *entirely* small (`supp(a_1) = primes(a_1) ⊆ P_R`, since every prime of `a_1` is `≤ R=rad(a_1)`). So if `σ(m)` misses `σ(a_1)`, then `m` cannot hit `a_1` through any large prime (`a_1` has none), so `m ∉ A_n`. This handles the **70–80% of `m ∉ B_n` cases where `σ(a_1)` is among the missed classes** — for free. The residual (σ(m) hits `σ(a_1)` but misses another class) is the genuinely hard ~20–30%, and it is where large-prime compensation must be ruled out. *Cheap-kill candidate:* **prove (C) for the subcase "σ(m) misses σ(a_1)" unconditionally** (immediate from the above), shrinking the open residual.

3. **The s-substitution descent (aimo-0030 analog) — works for admissibility, fails on size.** For a term `a_j` carrying a large prime, let `s = `R-smooth part of `a_j` (divide out all prime-power factors `> R`). Then `σ(s) = σ(a_j)`, and **`s` is admissible for `{a_1,…,a_{j-1}}` in 100% of tested cases** (`20/20` for `a_1=15`, `12/12` for `a_1=135`, `1/1` for `a_1=35`). *Why:* in the common subcase where `σ(a_j)` is a hitting set of `F'_{j-1}`, every past `a_i` is hit by a small prime of `a_j`, hence of `s`. The gap: **`s ≤ a_{j-1}` in every tested case** (never `s > a_{j-1}`), so `s` does not lie in the window `(a_{j-1}, a_j)` and gives no greedy contradiction at step `j`. The greedy "passed `s` over" earlier for a smaller admissible of a *different* class. The aimo-0030 lever ("bound the small-prime-only rewrite *below the original*") needs a size argument that does not yet exist here.

4. **Induction on class birth order.** Order the classes by first appearance. Suppose `σ*` is the first class (by birth order) with no R-smooth term; all earlier classes have one. Try to derive a contradiction by rewriting the first `σ*`-term `a_j` via the s-substitution. The a_1=135 case (class `{2,3}` born at `a_2=138=2·3·23` with NO all-small term until `a_4=144`) shows the all-small representative can arrive *2 steps late*, so the induction step must span a short delay, not be instantaneous. The mechanism forcing the late all-small term is the open sub-question.

5. **The "large primes never appear" regime.** For `a_1 ∈ {35,77,91,105,175,187,221,385}` (8 of 11 tested), **no `a_n` ever has a prime factor `> R`** (verified to `n=25–60`). For these, W is *trivial* (every term is R-smooth, so every class is all-small) and (C)/B1' is immediate. The hard cases are exactly those with **small `R`** (`a_1=15,45,135` all have `R=15`), where large primes do appear. *Conjectural cleaner statement to test next: "if `R` is large enough relative to `a_1`'s prime factors, the sequence is purely R-smooth."* This would isolate the hard regime.

## Candidate technique(s)
- **Minimal-counterexample descent on the support** (aimo-0030 shape): strip large primes, produce an R-smooth witness of the same small-support signature, bound below the original. *The admissibility of the rewrite is verified; the size bound is the gap.*
- **Induction on `n` maintaining "every `σ*`-class has an R-smooth term" (the invariant = W)** — the natural home for (W).
- **Pigeonhole/extremal + divisibility-graph** (KB "Pigeonhole/extremal principle", "Comparability/divisibility graphs") for the class-birth structure.
- **Spacing fact + value-bound lemma** (CERTIFIED, `lemmas/spacing-fact.md`, `lemmas/value-bound-unkillable-window.md`) — already proved, necessary-condition input; *do not re-prove*.

## Cheap-kill candidates
- **Prove (C) for the subcase "`σ(m)` misses `σ(a_1)`" unconditionally** (immediate: `a_1` has no large prime, so `m` can't compensate). Shrinks the open residual to ~20–30% of `m ∉ B_n`. *This is a genuinely free partial result a builder can record immediately.*
- **The "large primes never appear" fact for `R ≥ min-prime-of-a_1 × something`** — verify the threshold computationally and prove the sequence is purely R-smooth in that regime (would settle 8/11 hard-case `a_1` inputs at once).

## Knowledge-base entries to use
- **Pigeonhole / extremal principle** (KB Combinatorics) — class-birth ordering, minimal counterexample.
- **Comparability / divisibility graphs** (KB Combinatorics) — `σ*`-classes as divisibility signatures.
- **Invariants & monovariants** (KB Combinatorics) — the W-invariant across `n`.
- **Divisor analysis, consecutive-integer coprimeness** (KB Number Theory) — `gcd` structure of `a_1` vs window.
- **Modular arithmetic / CRT** (KB Number Theory) — for the late-arrival / σ-periodicity interaction.
- *(Spacing fact, value-bound, σ-periodicity, v_p-union-bound, cross-intersecting-closure, small-prime-minimum-in-window, small-prime-inclusion — all CERTIFIED in `lemmas/`, import directly.)*

## Analogous past problems (cruxes)
- **`aimo-0030`** (number_theory / divisibility-and-gcd; subtopic `size-bounding-and-descent`): crux = *"To produce a number with the same allowed-prime signature but no forbidden (large) prime factors, take the product of all allowed primes times the least power of one allowed prime reaching the threshold, and bound it below the original"*; plus *"Strengthen 'two special objects share a forbidden-class prime' to 'they share an allowed-class prime' by minimal-counterexample descent."* **Directly analogous to the s-substitution + W**: produce an R-smooth witness of the same `σ*`, descend. The aimo-0030 descent closes via a product-of-distinct-primes size comparison; our `s ≤ a_{j-1}` gap is the analogous size bound that we have NOT yet derived. The hitting-set-monovariant route already tried this descent and found the one-prime swap fails — but that was in *hitting-set* language; in **W-language** the substitution preserves admissibility (verified), so the descent may still close with the right size argument.
- No other corpus crux resembles the "greedy next-multiple-of-rad + periodicity" shape closely; the σ*-class structure is distinctive to this problem.

## Prior progress (consolidated)
- Bounded-diff, universal-small-prime, Theorem 1 (cyclic successor), trivial cases — CERTIFIED.
- Conditional spine (B1' ⟹ periodicity from `N_0`) — CERTIFIED. Seed automatic (Lemma 7). Stabilization over `P_R` free.
- Spacing fact + value-bound/unkillable-window (necessary condition only) — CERTIFIED.
- σ-periodicity (conditional on B1') + v_p union-bound (PARTIAL: B1' for `n ≤ n_0(a_1)∼10^{2000}`) — CERTIFIED as far as they go.
- Crux pinpointed to **B1'** (single window-admissibility claim) + secondary **B2** (empty pre-period).
- **This round's addition: (C) holds universally (0 violations, 11 `a_1`, all `n≤80`); and (C) reduces cleanly to the structural fact (W).**

## Dead ends (do not retry)
- **Clean value-window (Cov) sufficiency** — empirically REFUTED (9927 violations at `a_1=15`); the `σ*`-terms are too sparse in the short value window. *The obstruction is number-theoretic, not pure spacing.*
- **v_p/density sieve beyond `n_0`** — sieve error `~a_n` outpaces signal `~n·δ` (since `δ<1<L`); same wall as spacing. Coupled, not independent.
- **Transversal-minimality / Hall-König duality for `M_n=M'_n`** — one-prime swap fails (other `q`-essential rows needn't share `p_j`); Hall/König doesn't apply to hypergraph transversals; universal-small-prime necessary but NOT sufficient (1515/5000 counterexamples). Bare hypergraph theory cannot prove B1'.
- **Frozen-invariant (aimo-0678 shape) monovariant** — RETIRED (`w_n` is non-decreasing, not non-increasing; no frozen invariant / gcd-lcm recurrence exists in our single-sequence greedy).
- **Bertrand/competing-candidate** (round 1) — refuted.
- **Profinite compactness / residue-mod-M finite-state** — residue does not determine next residue (`a_1=15`, residue `0 mod 15` → next `10` vs `3`).
- **Injectivity-on-residues bypass** — transition not well-defined until B1.
- **Shift-invariance induction on prime supports** — supports of `a_{n+T}` and `a_n` are NOT equal; dead.
- **"First term of each `σ*`-class is R-smooth"** — FALSE (counterexample `a_1=135`: class `{2,3}` born at `a_2=138=2·3·23`). Do NOT build on the "first term all-small" claim; use the weaker (W) "every class has SOME all-small term" instead.

## Small-case / intuition notes (all CONJECTURE, labeled)
- **(C) holds with 0 violations** over 11 `a_1` (`{15,35,45,77,91,105,135,175,187,221,385}`), `n≤40–80` each, every `m` in every window `(a_n, a_n+R]`.
- **(W) holds universally** (same 11 `a_1`, every `n`): every `σ*`-class has an R-smooth term. For `a_1∈{35,77,91,105,175,187,221,385}` this is trivial (sequence is purely R-smooth). For `a_1∈{15,45,135}` (`R=15`), large primes do appear in some `a_n` but every class still has an R-smooth representative (e.g. `a_1=135` class `{2,3}`: first term `138=2·3·23` has large `23`, but `a_4=144=2^4·3^2` is the all-small representative).
- **Large-prime inventory (`a_1=15`, `n≤120`)**: only **9 distinct large primes** ever divide any `a_n`: `{17,19,23,29,31,37,41,43,47}`. Each is sparse: max frequency `5` (for `17`), inter-arrival gaps `9–33`. A single large prime `q` can divide at most one window-`W_n` integer (spacing fact) and recurs with gap `≥ q > R`.
- **Escape pattern**: among `4139` "interesting" `m ∉ B_n` (with large primes, missing a class) for `a_1=15`, the **escape size is `1` in `1624` cases (the mode)**, and the escaper is **`a_1` (index 1) in the vast majority** — because `a_1` is uncompensatable. This confirms the `σ(a_1)`-class is structurally special.
- **s-substitution**: for every term-with-large-prime, the R-smooth part `s` is admissible for the prior terms (`20/20`, `12/12`, `1/1`) but `s ≤ a_{j-1}` always (`s > a_{j-1}` in `0` cases) — so the s-rewrite never lands in the greedy window. The size gap is the sole obstruction to closing the aimo-0030-style descent.

## SINGLE most promising concrete next step for a builder
**Attempt an inductive proof of (W) — "every `σ*`-class in `F'_n` contains an R-smooth term" — by induction on `n` (or on class birth order), using the s-substitution as the descent step and the `σ(a_1)`-class as the base case (free).** The induction step: when a new class `σ*` is born at `a_j`, if `a_j` is R-smooth we are done; otherwise form `s = `R-smooth part of `a_j` (admissible for the past, verified) and either (i) land `s ∈ (a_{j-1}, a_j)` — contradiction, done — or (ii) `s ≤ a_{j-1}` — then `s` was a prior admissible candidate that the greedy passed over; *use the induction hypothesis on the smaller class structure at that earlier step to force an all-small `σ*`-term within a bounded delay* (the `a_1=135` case shows delay `2`). The clean reduction (W ⟹ (C) ⟹ B1') means a successful proof of (W) **collapses the entire crux B1'**; combined with the certified conditional spine, only B2 would remain. Concretely: start by writing down (W) as a lemma, prove the `σ(a_1)`-base case and the (W ⟹ (C)) implication (both short), then attack the inductive step with the s-substitution + a size bound closing the `s ≤ a_{j-1}` gap.
