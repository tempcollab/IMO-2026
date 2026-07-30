# imo-2026-06 — route: hitting-set monovariant (scouting the B1 crux)

Lens: the **hitting-set monovariant** route to crux **B1** (kernel stabilization). I probed the skeleton in `/home/agentuser/repo/results/imo-2026-06/approaches/hitting-set-monovariant.md` against computation and against the certified lemmas in `results/imo-2026-06/lemmas/`. All numerics below are real (python/sympy), labeled conjecture where they stop short of proof.

## Terrain

### Q1. Does the cross-intersecting closure lemma (step 3) actually hold?

**YES — rigorously valid, both in proof and in 2000 randomized off-greedy stress tests (0 violations) and in all 7 on-greedy sequences (the first cross-intersecting M_n stays fixed forever after).**

Proof (cleaner than the skeleton's): Assume `M_n` is pairwise cross-intersecting and `a_{n+1}` is admissible, so `supp(a_{n+1})` is a hitting set of `F_n` and hence contains some `h_0 ∈ M_n` (well-founded reduction). Then:
- *Old sets persist:* every `h' ∈ M_n` meets `h_0` (cross-intersecting), and `h_0 ⊆ supp(a_{n+1})`, so `h' ∩ supp(a_{n+1}) ⊇ h' ∩ h_0 ≠ ∅`. Thus `h'` still hits the new row; `h'` is still a hitting set of `F_{n+1}`. Minimality is preserved because `F_{n+1} ⊇ F_n` (a proper subset failing some old row still fails it).
- *No new minimal hitting set appears:* let `g` be a new minimal hitting set of `F_{n+1}` not in `M_n`. Since `g` is a hitting set of `F_n`, it properly contains some `h_g ∈ M_n` (minimality in `M_n`). Cross-intersecting gives `h_g ∩ h_0 ≠ ∅`, and `h_0 ⊆ supp(a_{n+1})`, so `h_g ∩ supp(a_{n+1}) ≠ ∅` — i.e. `h_g` ALSO hits the new row, so `h_g` is a hitting set of `F_{n+1}` strictly inside `g`, contradicting minimality of `g`.

Hence `M_{n+1} = M_n`. ∎ (The "introduces no new minimal hitting set" weak point flagged in the skeleton is closed by this argument; it is the load-bearing step and it is correct.)

Verified: off-greedy, 2000 random families on a 7-element universe — 0 closure-lemma violations. On-greedy, for `a_1 ∈ {15,35,77,91,105,135,385}` the first cross-intersecting `M_n` stays byte-identical through 60 terms in every case.

### Q2. What is the right well-founded monovariant?

**None of the three candidate measures is a monovariant — they are all NON-MONOTONE under the greedy.** The skeleton's step 4 ("strictly decreases at every non-closed step") is FALSE as stated.

Concrete trajectory, `a_1 = 385` (R = 385), the worst case I found:

| n | |M| | Σ\|h\| | #disjoint-pairs | \|∪M\| |
|---|---|---|---|---|
| 1 | 3 | 3 | 3 | 3 |
| 2 | 7 | 13 | 12 | 6 |
| 5 | 8 | 22 | 4 | 7 |
| 7 | 9 | 26 | 3 | 7 |
| 11 | 8 | 23 | 1 | 6 |
| 38 | 7 | 20 | 0 | 6 |

- `|M_n|` rises `3→7→6→8→9` then falls to `7`. It INCREASES through the early phase.
- `Σ|h|` rises `3→13→22→26` then falls. Increases.
- `#disjoint-pairs` rises `3→12` (!) before trending down to `0` at n=38. The very first step INCREASES the disjoint-pair count from 3 to 12. Not a monovariant.
- `|∪M_n|` rises `3→6→7→6` — also non-monotone (drops from 7 to 6 between n=10 and n=11).

`#disjoint-pairs` DOES reach 0 (cross-intersecting) in every tested case, and the *eventual* trend is downward, but it is not a strict monovariant, so it cannot carry a well-foundedness argument by itself. **I could not find any simple strictly-decreasing measure on `M_n` that survives the greedy's actual dynamics.** The skeleton's step 4 needs to be abandoned or completely reworked.

### Q3. Does `M_n` reach cross-intersecting (or singleton) empirically? Stabilized `S = ∪M`, `L`?

**YES — universally, in every one of the 7 required inputs AND in a full scan of odd `a_1 ∈ [3,130]`. Cross-intersecting is always the attractor (no non-cross-intersecting stable state was ever observed); `S = ∪M ⊆ {primes ≤ R = rad(a_1)}` always; stabilization happens within ≤ 50 terms for `a_1 ≤ 130` (within 38 for `a_1 = 385`).**

Required inputs:

| a_1 | R=rad | stabilize at n= | stable M (minimal hitting sets) | S=∪M | S⊆{p≤R}? | cross-int? | L=∏S |
|---|---|---|---|---|---|---|---|
| 15 | 15 | 3 | {2,3},{2,5},{3,5} | {2,3,5} | YES | YES | 30 |
| 35 | 35 | 4 | {2,3,7},{2,5},{3,5},{5,7} | {2,3,5,7} | YES | YES | 210 |
| 77 | 77 | 4 | {2,7},{2,11},{7,11} | {2,7,11} | YES | YES | 154 |
| 91 | 91 | 3 | {2,7},{2,13},{7,13} | {2,7,13} | YES | YES | 182 |
| 105 | 105 | 16 | {2,3},{2,5},{2,7},{3,5,7} | {2,3,5,7} | YES | YES | 210 |
| 135 | 15 | 5 | {2,3},{2,5,7},{3,5},{3,7} | {2,3,5,7} | YES | YES | 210 |
| 385 | 385 | 38 | {2,3,5},{2,3,11},{2,7},{2,11,19},{3,7,11},{3,7,19},{5,7,11} | {2,3,5,7,11,19} | YES | YES | 43890 |

Scan of odd `a_1 ∈ [3,130]`: **0 violations** of `S ⊆ {primes ≤ R}`; every case stabilized by term 50. The "extra" primes that enter `S` beyond `primes(a_1)` (e.g. 7 in `a_1=135`, 19 in `a_1=385`) are themselves always `≤ R`. The conjecture `S ⊆ {primes ≤ R}` (round-1 prime-cover explorer) is strongly supported and is the load-bearing empirical fact.

`M_n = M'_n` (the small-prime-reduced family, where `M'_n` = minimal hitting sets of `{σ(a_i): i≤n}`, `σ(m) = supp(m) ∩ P_R`, `P_R = {primes ≤ R}`) was verified to hold at EVERY step, not just eventually, for `a_1 = 385`. (Since `S ⊆ P_R` always, `M_n` only ever uses small primes, so `M_n = M'_n` trivially.)

### Q4. Does this route genuinely differ from bounded-diff-finite-state, or does it re-import B1?

**It re-imports B1. Honest answer: the route's true crux is EQUIVALENT to B1(a) (the "no free-rider large-prime shortcut" sub-gap). It does NOT bypass B1; it gives a cleaner equivalent reformulation and a cleaner terminal condition, but the wall is the same wall.**

Here is the precise equivalence I verified:

**Claim:** `M_n = M'_n` for all `n` (i.e. no minimal hitting set ever uses a prime `> R`) **iff** the greedy's small-prime-reduced support `σ(a_{n+1})` hits every past `σ(a_i)` (i.e. `a_{n+1}` hits every past term via a small prime `≤ R` — equivalently, no free-rider prime `> R` is ever essential).

- `M'_n ⊆ M_n` is always true (any small-prime hitting set of `{σ(a_i)}` is a hitting set of `{supp(a_i)}`, and minimality transfers because the rows only grew).
- `M_n ⊆ M'_n` is the crux: it says every `g ∈ M_n` lies inside `P_R`. Suppose `g ∈ M_n` contains a large prime `q > R`. By minimality, some past row `a_j` is hit by `g` ONLY through `q` (i.e. `supp(a_j) ∩ (g\{q}) = ∅`, `q ∈ supp(a_j)`). That is exactly a past term hit by `a_{n+1}`'s "ancestor admissible set" via a large prime only — the free-rider shortcut condition B1(a) forbids. So ruling out large primes in `M_n` IS ruling out free-rider shortcuts.

The skeleton's own step 4 admits this ("bound the measure's range — needs `|h|` bounded, which needs the active primes bounded"), but under-emphasizes that "active primes bounded" IS B1(a), not a side condition.

**The silver lining — and it is real — the route collapses to a much cleaner skeleton than the one written:**

The skeleton's step 3 (closure lemma) AND step 4 (monovariant) are both **unnecessary** for the theorem, because stabilization becomes FREE once `M_n = M'_n` is granted:

1. **Reduction** (definitional, clean): `A_n = ∪_{h∈M_n}{mult of m_h}`. [as written]
2. **Bounded diff** (import `lemmas/bounded-difference.md`): `a_{n+1} - a_n ≤ R`. [certified]
3. **`M_n = M'_n`** [THE crux = B1(a); unproven, see below].
4. **Finite-universe stabilization** (CLEAN, replaces steps 3 AND 4 of the skeleton): Once `M_n = M'_n`, the family `F'_n = {σ(a_i): i ≤ n}` is a GROWING family of subsets of the FIXED finite set `P_R = {primes ≤ R}`. Hence `F'_n` stabilizes as a set at some index `N` (`|F'_n| ≤ 2^{|P_R|}`). Since `M'_n` is a function of `F'_n` alone, `M_n = M'_n` stabilizes at `N`. Then `A_n = A := ∪_{h∈M}{mult of m_h}` is fixed.
5. **Seed is automatic** (closes B1(b) for free): `a_N ∈ A_N = A` because `a_N` is admissible for `F_{N-1}` (hits all earlier, and trivially hits itself), so `a_N ∈ A_N`. No separate seed sub-gap.
6. **Cyclic successor** (import `lemmas/periodic-set-iteration.md` Theorem 1): the greedy = `min(A ∩ (a_n,∞))` on the fixed `L`-periodic `A` (`L = ∏_{p ∈ ∪M} p`, squarefree, built from small primes) from index `N`. Theorem 1 gives `a_{n+T} = a_n + L` for all `n ≥ N`, `T = |A ∩ [0,L)|`, single cycle, no pre-period inside `A`.
7. **From-n=1** (B2, still open): extend from `n ≥ N` to `n ≥ 1`. Unchanged, separate gap.

So the hitting-set route, properly recast, reduces the whole problem to **B1(a) alone + B2** — eliminating the skeleton's monovariant, eliminating B1(b) (the seed sub-gap the bounded-diff route had to carry), and eliminating the closure lemma as a *load-bearing* piece (it becomes a clean *early*-stabilization shortcut, see below, but is not needed for the theorem).

The closure lemma (step 3) is still VALUABLE as a *sharper* stabilization mechanism: empirically `M_n` freezes as soon as it is cross-intersecting (n=38 for `a_1=385`), which is MUCH earlier than `F'_n` stabilizing as a set (which for `a_1=385` had not even happened by term 42 — `|F'_n|` was still growing: 27 at n=38, 28 at n=41). The closure lemma explains why `M` can freeze before `F'` does: once cross-intersecting, every future `σ(a_{n+1})` (which contains some `h ∈ M`) leaves `M` unchanged. So the closure lemma is the mechanism of EARLY stabilization, and the finite-universe argument is the EXISTENCE backstop. Either suffices for the theorem; the closure lemma gives a cleaner story and an explicit terminal condition.

## Promising openings

1. **Drop the monovariant; recast the skeleton as the 7-step chain above.** The crux becomes the single statement `M_n = M'_n` (= B1(a) in hitting-set language). This is the cleanest equivalent form of B1 found in either round — it is purely combinatorial ("every minimal transversal of the support family uses only small primes") and avoids any mention of the greedy's window mechanics.

2. **Attempt a direct combinatorial proof of "large primes are never essential."** I tried and could NOT close it, but the cleanest framing I found is: suppose `q > R` lies in some `g ∈ M_n`; by minimality ∃ past `a_j` with `supp(a_j) ∩ (g\{q}) = ∅` and `q | a_j`. Since `g` is a hitting set it meets `supp(a_1) ⊆ P_R`, so `g` has a small prime `p`; then `p ∤ a_j` but `a_j` shares SOME small prime `p' ≠ p` with `a_1` (admissibility). This forces `a_1` to have ≥ 2 distinct small prime factors — consistent with the hard case, so no contradiction. The argument genuinely needs more than bounded-diff; the refuted Bertrand/competing-candidate attack of round 1 tried exactly this direction and failed. **A genuinely new idea is needed here; do not re-try Bertrand.**

3. **Use the closure lemma as the induction engine (partial alternative to direct B1(a) attack).** Induct on `n`: if `M'_n` is cross-intersecting, the closure lemma gives `M'_{n+1} = M'_n` AND (because no new minimal hitting sets appear at all) `M_{n+1} = M_n = M'_n` for free — so the induction step is free past the cross-intersecting threshold. The hard work is the PRE-cross-intersecting phase: prove `M_n = M'_n` while `M'_n` is still non-cross-intersecting. Empirically this phase is short (≤ 38 terms) and `|M_n|` is small, but I do not see a uniform argument. Worth one builder attempt.

4. **Prove stable-⟹-cross-intersecting** (would let the closure lemma reach the attractor from any stable state): if `M'_N` is stable but has disjoint `h, h'`, then every future `σ(a_m) ⊇ h_m ∈ M'_N` must be hit by `h'` (else `h'` is removed). Infinitely many future terms, finitely many `h_m`, so some `h* ∈ M'_N` sits inside infinitely many `σ(a_m)`. If `h* = h` (disjoint from `h'`), those `σ(a_m)` all contain `h` and must each carry a `h'`-prime. I could not turn this into a contradiction; it is plausible but not established. If provable, it converts the finite-universe backstop into "M stabilizes AND is cross-intersecting," sharpening step 4 without a monovariant.

## Dead-ends confirmed

- **The skeleton's step-4 monovariant `(|M_n|, Σ|h|)` or `#disjoint-pairs`**: DEAD. All three measures are non-monotone under the greedy (data: `a_1=385`, `|M|` rises `3→9` before falling; `#disjoint-pairs` rises `3→12` on the very first step). Do NOT have the builder try to prove "strictly decreases at every non-closed step" for any of these — it is false.
- **Bertrand / competing-candidate attack on B1(a)**: already refuted in round 1 (`bounded-diff-finite-state`), and the hitting-set route offers no new tool for it. Do not retry.
- **Proving "the set of all primes dividing some `a_n` is finite"**: FALSE (round 1). The stabilizing object is `M_n` / `∪M`, never `∪ supp(a_i)`.

## Recommended next step for the builder (concrete)

**First priority: rewrite the skeleton into the 7-step chain above (drop the monovariant; drop the closure lemma as load-bearing; keep it as the early-stabilization shortcut).** This recasts the route as "B1(a) ⟺ `M_n = M'_n`, then finite-universe gives the rest for free, with B1(b) and the monovariant both eliminated." That is a real simplification over `bounded-diff-finite-state` (which still carries B1(b) and the free-rider-shortcuts sub-gap as separate items).

**Second priority — pick ONE of these to attempt first (in order of promise):**

(a) **Direct proof that no prime `> R` ever enters `M_n`.** Frame: "a large prime `q > R` dividing some `a_j` is never essential, because `σ(a_j)` alone already hits every past `σ(a_i)`." This is B1(a) head-on; the honest expectation is that it is NOT easier than the bounded-diff route's attempt — but the hitting-set language may suggest a transversal-minimality move the window-based framing missed (e.g. a rank/matching argument: if `q` were essential, the small-prime part of the support family would have a matching deficiency contradicting the bounded-diff candidate `R·⌈(a_n+1)/R⌉` being admissible).

(b) **Closure-lemma induction.** Prove `M_n = M'_n` for the pre-cross-intersecting phase by a separate argument (e.g. brute structural case analysis on the small `|M_n|` regimes — risky to make uniform, but the phase is empirically tiny). If this holds, the closure lemma carries the rest. Concretely: try to show that whenever `M'_n` is NOT cross-intersecting, the next greedy step strictly *reduces* `|∪M'_n|` or merges two disjoint minimal transversals — note this is a DIFFERENT measure than the three I falsified, and I have NOT checked it; the builder should test it on the `a_1=385` trajectory before trusting it.

If neither (a) nor (b) yields in one round, the route is stuck on the same B1(a) wall as the other routes and should be flagged back to the outliner for a genuinely different framing — the hitting-set lens has then exhausted its distinctive contribution (the clean reduction + closure lemma) without cracking the shared crux.

## Knowledge-base entries to use

- **Invariants & monovariants** (KB) — for the closure-lemma induction framing (b), the "family over a finite universe stabilizes" is the relevant monovariant pattern, NOT a measure on `M_n`.
- **Pigeonhole / extremal principle** (KB) — the finite-universe stabilization `|F'_n| ≤ 2^{|P_R|}` is the pigeonhole/finite-poset move.
- **Divisibility and gcd / consecutive-integer coprimeness** (KB) — for any direct attack on "large primes never essential" (the bounded-diff candidate `R·⌈(a_n+1)/R⌉` is the admissibility witness).
- **Modular arithmetic and CRT** (KB) — step 6, `A` is a union of residue classes mod `L`.
- Reuse certified: `lemmas/bounded-difference.md`, `lemmas/universal-small-prime.md`, `lemmas/periodic-set-iteration.md` (Theorem 1).

## Analogous past problems (cruxes)

Querying the corpus for transversal / hitting-set / monovariant-descent moves:

- The subtopic `invariants-and-monovariants` (number_theory and combinatorics) is the closest match by spirit, but no crux in the corpus uses *minimal-transversal families* as the stabilizing object. The closest is the pattern "a growing family over a finite universe stabilizes" — a standard pigeonhole move — but it is too generic to cite as a single crux.
- **No direct crux match found.** The "greedy smallest-with-gcd-condition → eventually periodic-up-to-translation" structure, and the reduction of its crux to "minimal transversals of the support family use only bounded primes," appear to be novel relative to the pre-2026 NT/combinatorics corpus. Do not force a wrong match.

## Small-case / intuition notes (all CONJECTURE, labeled)

- **Conjecture (S ⊆ primes ≤ R):** universal in every tested case (`a_1 ≤ 130` odd scan + the 7 required inputs). This is the empirical ground for the whole route. If it ever fails for some `a_1`, the route dies — but I found no failure in a broad scan.
- **Conjecture (cross-intersecting is the unique attractor):** every stabilized `M` is pairwise cross-intersecting; no non-cross-intersecting stable state was observed. If provable, it sharpens step 4 to "stable ⟹ cross-intersecting" without a monovariant (opening 4 above), but I could not prove it.
- **Conjecture (M_n = M'_n from n=1):** the equality holds at EVERY step, not just eventually — verified step-by-step for `a_1=385`. So the pre-cross-intersecting phase does NOT rely on large primes either. This makes the induction framing (opening 3) clean but leaves the pre-cross-intersecting phase as the unproved link.
- **Intuition for why large primes never enter M:** when `a_{n+1}` is chosen, it is ≤ the next multiple of `R` (bounded-diff witness), which is divisible by every prime of `a_1`. So `a_{n+1}` and the multiple-of-`R` candidate both sit in a window of length `R`, and `a_{n+1}` is divisible by some small prime `≤ R`. For a large prime `q > R` to be essential, some past `a_j` would have to be hit by `a_{n+1}` *only* through `q` — but `a_j` itself carries a small prime of `a_1`, and the greedy's structure seems to keep small-prime coverage "saturated." I could not formalize this; it is exactly where a new idea is needed.
