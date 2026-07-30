# Approach: periodic-set-iteration

## Status
partial

## Approaches tried
- (round 1) Factor the problem into (I) an abstract periodic-set-iteration theorem + (II) convergence of the admissible sets `A_n`. — **Theorem I proved in full** (clean, promotable, certified-pending in `lemmas/periodic-set-iteration.md`); **Part II (set stabilization) NOT closed**: the profinite-compactness gamble is shown, honestly, to be insufficient on its own (it yields a profinite point, not a finite-period set containing the orbit), and the conditional reduction to the shared B1 conjecture is carried as far as it rigorously goes (stabilization of the `S`-support family) but the free-rider "large-prime shortcuts stop" sub-gap and B1 itself remain open. From-`n=1` conditional on stabilization is also left as a gap.

## Current best
**Theorem 1 (iteration on a periodic set is a single cycle, periodic from the start)** — fully proved in `lemmas/periodic-set-iteration.md`; this is the route's clean, reusable, cross-route contribution (it is the lift = L / from-n=1 mechanism needed by `bounded-diff-finite-state`, `hitting-set-monovariant`, and `bijection-from-n1`).

**Reductive frame (clean):** the greedy rule is `a_{n+1} = min(A_n ∩ (a_n, ∞))` where `A_n = {m ≥ 1 : gcd(m, a_i) > 1 ∀ i ≤ n}`; `(A_n)` is a decreasing chain of periodic sets, each a finite union of arithmetic progressions; `A_n ≠ ∅` for every `n` (bounded-diff lemma). The whole problem reduces to exhibiting a *fixed* periodic set `A` such that, from some index onward, the greedy decision `min(A_n ∩ (a_n,∞))` coincides with `min(A ∩ (a_n,∞))`, then applying Theorem 1.

**Open gaps:** (B1) finiteness of the kernel prime set `S`; (free-rider sub-gap) stabilization of the *local* admissible set near `a_n` to a fixed periodic set even granted B1; (from-n=1) showing the stabilization index is `1`.

## Full proof

Target: ∃ positive integers `T, L` with `a_{n+T} = a_n + L` for every `n ≥ 1`.

We factor the argument into Part I (a pure combinatorial theorem on periodic-set iteration — **proved in full**) and Part II (the number-theoretic reduction — **carried as far as it goes, with explicit gaps**).

---

### Part I — Abstract theorem (PROVED)

**Theorem 1 (least-greater-than iteration on a periodic set).** Let `A ⊆ ℤ` be nonempty and periodic with positive period `L` (`A + L = A`). Let `R = A ∩ [0, L) = {r_1 < r_2 < … < r_T}`, `T = |R| ≥ 1`, and `f_A(x) = min{ y ∈ A : y > x }`. Then for every `x_0 ∈ A`, the orbit `x_{k+1} = f_A(x_k)` satisfies
`x_{k+T} = x_k + L` for all `k ≥ 0`.

**Proof.** (Full proof at `results/imo-2026-06/lemmas/periodic-set-iteration.md`; summarized here for self-containment.) A nonempty `L`-periodic set is unbounded above, so `f_A` is well-defined. An integer `m` lies in `A` iff `m mod L ∈ R`. For `x_k ≡ r_i (mod L)` with `i < T`, the candidate `y = x_k + (r_{i+1} − r_i)` lies in `A` (`y ≡ r_{i+1}`) and every `z` with `x_k < z < y` has `z mod L ∈ (r_i, r_{i+1})`, disjoint from `R`; hence `f_A(x_k) = y`. The wrap case `i = T` uses `y = x_k + (L − r_T) + r_1`. So the residue map is the *cyclic successor* `τ(r_i) = r_{i+1}` (cyclically), a single `T`-cycle by construction. Hence `ρ_{k+T} = ρ_k`, and the displacement over one cycle telescopes to `(r_2−r_1) + … + (r_T−r_{T-1}) + (L − r_T + r_1) = L`. ∎

(Cross-checked numerically on the `a_1 = 15` data: residues `R = {0,6,10,12,15,18,20,24} mod 30`, `T = 8`, orbit `15, 18, 20, 24, 30, 36, 40, 42, 45, …` matches the empirical greedy exactly and satisfies `x_{k+8} = x_k + 30` from `k = 0`.)

**Corollary 1 (from the start).** Because `τ` is a single cycle (a bijection), periodicity begins at `k = 0` once the orbit lives in a fixed periodic set `A`.

---

### Part II — Number-theoretic reduction: the greedy is the iteration of `f_A` for a fixed periodic `A`

Define, for `n ≥ 1`,
  `A_n = { m ≥ 1 : gcd(m, a_i) > 1 for every i = 1, …, n }`
(the *admissible set* at step `n`). The greedy rule is exactly
  `a_{n+1} = min( A_n ∩ (a_n, ∞) ) = f_{A_n}(a_n)`.

We must show that, eventually, `f_{A_n}` agrees near `a_n` with `f_A` for a single periodic set `A`.

#### Step 1 — `A_n` is a decreasing chain of periodic sets (CLEAN)

**Monotonicity.** `A_{n+1} ⊆ A_n`: adding the constraint "`gcd(·, a_{n+1}) > 1`" only removes elements.

**Each `A_n` is periodic.** Put `M_n = rad( ∏_{i=1}^n a_i )` (the squarefree kernel of the product of all past terms; equivalently the radical of their lcm). For any `m`, the truth of "`p | m`" for `p | M_n` is invariant under `m ↦ m + M_n` (since `p | M_n`). Whether `m ∈ A_n` depends only on the pattern of which primes `p ∈ supp(a_1) ∪ … ∪ supp(a_n)` divide `m`; all such primes divide `M_n`. Hence `m ∈ A_n ⇔ m + M_n ∈ A_n`. So `A_n` is periodic with period `M_n`. (It is a finite union of residue classes mod `M_n`.) [No gap.]

Concretely, `A_n = ∪_h { m : ∀ p ∈ h, p | m } = ∪_h { multiples of ∏_{p∈h} p }`, the union ranging over the minimal *hitting sets* `h` (minimal sets of primes meeting every `supp(a_i), i ≤ n`); each summand is an AP.

#### Step 2 — `A_n` is nonempty (CLEAN; uses the bounded-diff lemma)

**Bounded-difference lemma** (shared; cf. `bounded-diff-finite-state`). Let `R = rad(a_1) = ∏_{p | a_1} p`. Every past term `a_i` (`i ≤ n`) satisfies `gcd(a_i, a_1) > 1`, hence is divisible by some prime `p | a_1`. The next multiple of `R` strictly after `a_n`, call it `m = ⌈(a_n+1)/R⌉ · R ≤ a_n + R`, is divisible by every prime of `a_1`, hence by some prime dividing each `a_i`; thus `gcd(m, a_i) > 1` for every `i ≤ n`, i.e. `m ∈ A_n`. So `A_n ≠ ∅` (and is unbounded above). In particular `a_{n+1} − a_n ≤ R` for all `n`. [No gap.]

#### Step 3 — The profinite-compactness gamble (DISTINCTIVE; honestly shown INSUFFICIENT alone)

We attempt the route's distinctive move: extract a fixed finite-period set the orbit lies on, *without* first bounding the kernel prime set `S`, by compactness in the profinite completion `Ẑ`.

**Setup.** Identify `A_n`, a union of residue classes mod `M_n`, with the clopen set `Â_n = { z ∈ Ẑ : z mod M_n ∈ A_n mod M_n }` under the reduction map `ℤ → Ẑ`. Each `Â_n` is clopen (hence closed) in the compact space `Ẑ`, and `Â_1 ⊇ Â_2 ⊇ …` (decreasing) by Step 1. Each `Â_n` is nonempty (Step 2). By the finite-intersection property of compact spaces (KB: Extreme value theorem / compactness — a decreasing chain of nonempty closed subsets of a compact space has nonempty intersection),

  `Â_∞ := ∩_{n≥1} Â_n ≠ ∅`  in `Ẑ`.

So there exists a *profinite integer* `ẑ ∈ Ẑ` that is "admissible for all time": for every `n`, the residue `ẑ mod M_n` lies in `A_n mod M_n`.

**Why this does NOT close the problem (honest diagnosis).** `Â_∞` is a closed subset of `Ẑ`, generally not open / not determined by any single finite modulus, and it is *not* a finite union of residue classes mod some fixed `L` in general. Moreover, and crucially:

  - `Â_∞` need not contain any *genuine* integer. A genuine integer `m ∈ A_∞ = ∩ A_n` would satisfy `gcd(m, a_n) > 1` for *every* `n`. If no single prime divides all `a_n` (the generic `T > 1` case, e.g. `a_1 = 15`), no fixed integer `m` has this property in general — `m` would need to carry, simultaneously, a prime factor hitting each of the (unboundedly many distinct) `a_n`. The compactness point `ẑ` exists *profinite-wise* (it chooses a consistent residue mod each `M_n`) but is not a genuine integer.
  - **The orbit `(a_n)` is not contained in `Â_∞`.** Indeed `a_n ∈ A_{n-1}` but `a_n ∈ A_n` requires `gcd(a_n, a_n) > 1` (trivially yes), while `a_n ∈ A_m` for `m > n` requires `gcd(a_n, a_j) > 1` for `j ∈ (n, m]`, i.e. that `a_n` hit future terms — generally false. So each `a_n` lies in `Â_1, …, Â_{n}` but drops out of `Â_m` for large `m`; no single `Â_N` contains the whole orbit, and the orbit is not contained in `Â_∞`.

Hence compactness furnishes a *point* of the inverse limit but not a finite-period set `A` on which the orbit evolves as `f_A`. The distinctive gamble, as stated, does not short-circuit the kernel bound. **[GAP: the profinite-compactness escape does not, by itself, produce the required fixed periodic set. It reframes `A_∞` as a profinite object but leaves the orbit outside any single `Â_n`. This gap is the honest reason the route falls back to B1 below.]**

#### Step 4 — Conditional reduction assuming B1 (the honest fallback)

Let us now *assume* the shared conjecture **B1** (the "kernel river"; see `bounded-diff-finite-state`):

  **(B1)** There is a finite set of primes `S`, with `P_1 := supp(a_1) ⊆ S`, such that every `a_n` is divisible by some `p ∈ S`.

(Computationally `S = primes(L)`; `S ⊇ P_1`; conjecturally `S ⊆ { primes p ≤ R = rad(a_1) }`, but we only need finiteness.)

**Step 4a — the `S`-support family stabilizes (CLEAN under B1).** For each `n`, put `s_n = supp(a_n) ∩ S` (a nonempty subset of `S` by B1). The family `F_n = { s_i : i ≤ n }` is monotone non-decreasing in `2^S \ {∅}`, a finite set. Hence `F_n` stabilizes: ∃ `N_1` with `F_n =: F_∞` for all `n ≥ N_1`. [No gap, given B1.]

**Step 4b — define the candidate periodic set.** Let `L = ∏_{p ∈ S} p` (squarefree). Define the *S-admissible* set
  `A^{(S)} = { m ≥ 1 : ∀ s ∈ F_∞, supp(m) ∩ s ≠ ∅ }`
  = `{ m : supp(m) ∩ S hits every member of F_∞ }`.
Because membership depends only on which primes of `S` divide `m`, `A^{(S)}` is a union of residue classes mod `L` (CRT, KB: Modular arithmetic / CRT), hence `L`-periodic, and nonempty (it contains, for instance, `L` itself, which is divisible by every `p ∈ S`). So `A^{(S)}` is a periodic set to which Theorem 1 applies.

**Step 4c — the orbit is eventually `f_{A^{(S)}}`-iterative (SUB-GAP).** We would like: for all `n ≥ N_1`, the greedy `a_{n+1} = min(A_n ∩ (a_n, ∞))` equals `f_{A^{(S)}}(a_n) = min(A^{(S)} ∩ (a_n, ∞))`. The inclusion `A_n ⊆ A^{(S)}` holds for `n ≥ N_1`? Not as sets: `A_n` requires hitting the *full* support `supp(a_i)` (including free-rider primes outside `S`), so `A_n` may contain elements not in `A^{(S)}` (elements hitting some `a_i` only via a free-rider prime) and may omit elements of `A^{(S)}` (no — `A^{(S)}` requires hitting only the `S`-part of each `a_i`; any `m` hitting each `s ∈ F_∞` via `S`-primes hits each `a_i` via that same `S`-prime, so `A^{(S)} ⊆ A_n` for `n ≥ N_1`).

So `A^{(S)} ⊆ A_n` for `n ≥ N_1`, giving `f_{A_n}(a_n) ≤ f_{A^{(S)}}(a_n)`. The danger is the reverse inequality failing: a free-rider-based candidate `m ∈ A_n \ A^{(S)}` could be smaller than `f_{A^{(S)}}(a_n)` and steal the greedy. By the bounded-diff lemma, `a_{n+1} ≤ a_n + R`, so only candidates in the window `(a_n, a_n + R]` matter.

  **[GAP (free-rider shortcuts): prove that for all sufficiently large `n`, no `m ∈ (a_n, a_n + R]` lying in `A_n \ A^{(S)}` is admissible — equivalently, every admissible candidate in the window already lies in `A^{(S)}`. Candidate mechanism (not proved here): the number of past terms with a given `S`-support grows unboundedly while a candidate `m ≤ a_n + R` carries only `O(log a_n)` large primes; a free-rider prime `q ∉ S` of `m` can hit only the past terms divisible by `q`, a set that (unless `q ∈ S`) is not cofinal in the support family. This sub-gap is shared with `bounded-diff-finite-state` (its step 3) and is not closed here.]**

*Conditional on the sub-gap:* once `f_{A_n}(a_n) = f_{A^{(S)}}(a_n)` for all `n ≥ N`, Theorem 1 (applied with `A = A^{(S)}`, period `L`, `x_0 = a_N`) yields, with `T = |A^{(S)} ∩ [0, L)|`,
  `a_{n+T} = a_n + L`   for every `n ≥ N`.   (eventual periodicity)

This is the rigorous reduction: **(B1) + (free-rider sub-gap) ⇒ eventual periodicity with `L = ∏S`**. The proof of *eventual* periodicity is complete conditional on those two gaps; the gaps themselves are not closed by this route.

#### Step 5 — From eventual to "for every `n ≥ 1`" (GAP)

Theorem 1 actually gives periodicity *from `k = 0`* relative to the entry index `N` (i.e. for `n ≥ N`). To obtain the theorem as stated (`for every n ≥ 1`), we need `N = 1`: the orbit must lie on the periodic set `A^{(S)}` from the very first term. Computationally this is always the case (the pre-period is empty in every tested instance — `a_1 = 15`: `a_9 = 45 = a_1 + 30`, etc.). Two honest routes to it:

  (i) **Injectivity / bijection route** (cf. `bijection-from-n1`): show the transition `τ` on the reachable residue set is injective, hence a permutation, hence a single cycle, forcing `a_1 mod L` onto the cycle. [GAP — the injectivity crux, not proved here; this is `bijection-from-n1`'s distinctive wall.]

  (ii) **Direct induction from `a_1`**: construct `L, T, R` from `a_1` and prove `a_{n+T} = a_n + L` by induction with the greedy rule closing the inductive step via `L`-shift-invariance of `R`. [GAP — not carried out here.]

  **[GAP (from-`n=1`): neither route is closed in this approach. Conditional on (B1) + (free-rider sub-gap) we obtain `a_{n+T} = a_n + L` for all `n ≥ N`; elevating to `n ≥ 1` requires the additional from-`n=1` argument above.]**

---

### Summary of what is proved vs. conjectured

**Proved (rigorous, self-contained):**
- Theorem 1 (iteration of least-greater-than on a fixed periodic set is a single cycle, periodic from `k = 0`); certified-pending in `lemmas/periodic-set-iteration.md`.
- `A_n` is a decreasing chain of periodic sets, each a finite union of APs (Step 1).
- `A_n ≠ ∅` and `a_{n+1} − a_n ≤ rad(a_1)` (Step 2; shared bounded-diff lemma, re-proved inline).
- The profinite intersection `Â_∞ = ∩ Â_n` is nonempty in `Ẑ` (Step 3, the compactness point).
- Conditional on **(B1)**: the `S`-support family `F_n` stabilizes to a finite `F_∞`, and the candidate set `A^{(S)}` is a well-defined `L`-periodic set with `L = ∏S`, to which Theorem 1 applies (Steps 4a, 4b).
- Conditional on **(B1) + (free-rider sub-gap)**: `a_{n+T} = a_n + L` for all `n ≥ N` (eventual periodicity, Step 4c + Theorem 1).

**Gaps (honest):**
- **[GAP-A]** The profinite-compactness escape (Step 3) does not, by itself, produce a fixed finite-period set containing the orbit; it yields a profinite point `ẑ ∈ Ẑ` and the orbit is not contained in `Â_∞`. The distinctive gamble does not short-circuit B1.
- **[GAP-B]** **(B1)**: finiteness of the kernel prime set `S` (shared with all routes).
- **[GAP-C]** (free-rider shortcuts sub-gap, Step 4c): even granting B1, free-rider primes in past terms can in principle let candidates `m ∈ (a_n, a_n+R]` be admissible without being `S`-admissible; must show this stops for large `n`. Shared with `bounded-diff-finite-state` step 3.
- **[GAP-D]** (from-`n=1`, Step 5): elevating eventual periodicity to "for every `n ≥ 1`" requires the stabilization index `N = 1`; not closed here.

**Conjectured (numerical evidence, NOT proved):**
- `S = primes(L)` is finite and `S ⊇ P_1` (computationally always true).
- The free-rider sub-gap resolves affirmatively (computationally, passive primes never create new coverage).
- The from-`n=1` lift: in every tested case (`a_1 = 2..59` and odd composites to 391) the pre-period is empty (`a_{1+T} = a_1 + L`).

---

### Cases covered
- **Trivial sub-cases** (`a_1` even; `a_1 = p^k` a prime power): here a single prime `p` divides every term (for even `a_1`, `p = 2` via `gcd(a_1, a_1+1) = 1` forcing `a_2 = a_1 + 2` and inductively all even; KB: divisor analysis, consecutive-integer coprimeness). Then `A_n =` (multiples of `p`) from the start, `L = p`, `T = 1`, and Theorem 1 with `R = {0}` gives `a_{n+1} = a_n + p` for all `n ≥ 1`. [Fully proved sub-case.]
- **Hard case** (`a_1` odd with ≥ 2 distinct prime factors, `T > 1`): the full route above applies, with gaps B/C/D as flagged.

### Watch out for
- `A_n` does NOT have a common period from the start: `M_n = rad(∏_{i≤n} a_i)` grows (free-rider primes appear forever). The common period must be *extracted* (Step 4b), not assumed.
- The orbit `(a_n)` is NOT contained in `A_∞ = ∩ A_n` (Step 3 honest diagnosis); do not assert it.
- `L = ∏S` (kernel product), NOT `R = rad(a_1)` and NOT `∏_{p ≤ R} p`. Periodicity mod `∏_{p≤R}p` is FALSE (verified: `a_1 = 15` has `L = 30`, not a divisor of `∏_{p≤15} p = 30030` with the right period).
- The set of primes dividing *some* `a_n` is NOT finite (free riders unbounded). Do not claim it. The stabilizing object is the kernel `S`, not `∪_n supp(a_n)`.

## Promotable lemmas
- **Theorem 1 (periodic-set-iteration).** Statement and full proof at `results/imo-2026-06/lemmas/periodic-set-iteration.md`. *Iterating `f_A(x) = min(A ∩ (x,∞))` on a nonempty `L`-periodic set `A` from any `x_0 ∈ A` yields `x_{k+T} = x_k + L` for all `k ≥ 0`, with `T = |A ∩ [0,L)|`.* Mechanism: the residue map is the cyclic successor on the sorted residue set, a single cycle; displacement telescopes to `L`. This is the reusable lift = L / from-n=1 mechanism for `bounded-diff-finite-state`, `hitting-set-monovariant`, `bijection-from-n1`. (Awaiting reviewer certification.)
- **Bounded-difference lemma (`a_{n+1} − a_n ≤ rad(a_1)`).** Stated and proved inline in Step 2 (also proposed by `bounded-diff-finite-state`); the next multiple of `rad(a_1)` after `a_n` is a valid admissible candidate. Cross-route value; not re-certified here (owned by the bounded-diff builder).
