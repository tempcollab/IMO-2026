# Approach: bijection-from-n1

## Status
partial

## Approaches tried
- (round 1 seed) Attempted a direct injectivity argument (T on reachable residues injective ⟹ bijection ⟹ single cycle ⟹ from-n=1) WITHOUT first proving the admissible set stabilizes (the "B1 river"). **Outcome: collapsed.** The "transition on residues mod L" is not even well-defined until the admissible set is periodic mod L, and periodicity mod L requires precisely the kernel-stabilization (B1) this route hoped to bypass. The outline-reviewer's warning ("if injectivity secretly requires 'admissible set periodic' = B1, the route is NOT genuinely distinct") is confirmed: the injectivity crux reduces to periodic-set-iteration's Theorem 1 (iteration on a FIXED periodic set is a single cycle). Recorded below: the two genuinely clean, unconditional sub-results (even a_1; prime-power a_1), plus two promotable lemmas (bounded-diff; Theorem 1 = the injectivity/bijection/single-cycle/lift=L mechanism), plus the explicit gaps.

## Current best
Two unconditional solved sub-cases (even a_1; prime-power a_1), each T=1, L=p from n=1, fully rigorous. Plus a clean promotable **Theorem 1** (iteration of least-greater-than on a fixed periodic set is a single cycle from the start, with lift exactly the period) — this is the route's intended injectivity mechanism, but it only applies AFTER the admissible set stabilizes, so it gives from-n=N (eventual), not from-n=1.

**Open gaps (blocking the general case):**
- **[GAP: B1 — kernel stabilization]** The admissible set `A_n = {m : gcd(m,a_i)>1 ∀ i≤n}` stabilizes to a fixed `L`-periodic set `A` (equivalently, a finite kernel prime set `S ⊇ primes(a_1)`, `L=∏S`). Unproven; shared with every other route.
- **[GAP: from-n=1 consistency]** Even given B1 (so `A_n = A` for `n ≥ N`), the greedy's choices for `n < N` coincide with the eventual cycle (no "premature valid candidate" lies in the gap `(a_n, cyclic_successor_A(a_n))` for `n < N`). This is the route's intended "free" payoff; it is NOT free — it is an additional gap. The outline-reviewer's flag is sustained.

## Full proof

Not `solved` (the general case has the two gaps above). What is proved in full below: (A) the bounded-difference lemma; (B) Theorem 1 — the injectivity/bijection/single-cycle/lift=L mechanism for a fixed periodic set; (C) two unconditional trivial sub-cases (even, prime-power). The general case is reduced to the two gaps.

---

### A. Bounded-difference lemma (clean; promotable)

**Lemma (bounded differences).** Let `R := rad(a_1) = ∏_{p | a_1} p` (squarefree radical of `a_1`, a fixed constant depending only on `a_1`). Then for every `n ≥ 1`,
```
a_{n+1} − a_n ≤ R .
```

*Proof.* Let `P_1 = {primes dividing a_1}` (so `R = ∏_{p ∈ P_1} p`). Every past term `a_i` (`i ≤ n`) satisfies `gcd(a_i, a_1) > 1` (the greedy chose `a_i` to hit `a_1` among others), hence `a_i` is divisible by some `p ∈ P_1`. Consider
```
m := ⌈(a_n + 1)/R⌉ · R ,
```
the smallest multiple of `R` strictly larger than `a_n`. Then `m ≤ a_n + R` (multiples of `R` are spaced `R` apart) and `R | m`, so `p | m` for **every** `p ∈ P_1`. Since each `a_i` (`i ≤ n`) is divisible by some `p ∈ P_1` and `m` is divisible by all of them, `gcd(m, a_i) ≥ p > 1` for every `i ≤ n`. Thus `m` is a valid candidate for `a_{n+1}`, and by minimality of the greedy,
```
a_{n+1} ≤ m ≤ a_n + R .  ∎
```
This is **non-circular**: `R = rad(a_1)` is a fixed constant, independent of the dynamics. (KB: *Divisor analysis* — rad/gcd structure; *Order of an element / Fermat-Euler* — periodicity mod `m`.)

Numerical check (a_1 ∈ {15,35,77,135,175,187,221}): `maxdiff ≤ rad(a_1)` in every case. ∎

---

### B. Theorem 1 — iteration on a fixed periodic set is a single cycle from the start (clean; promotable)

This is the route's distinctive injectivity/bijection/single-cycle mechanism, isolated as a standalone theorem. It is the rigorous content behind the skeleton's "T injective ⟹ bijection ⟹ single cycle ⟹ from-n=1" — but it applies to a **fixed** periodic admissible set, which is why the route cannot bypass B1.

**Theorem 1.** Let `A ⊆ ℤ` be nonempty and periodic with period `L > 0` (`A + L = A`). Let
```
R = { r ∈ {0,1,…,L−1} : r ≡ a (mod L) for some a ∈ A } = A (mod L) ⊆ ℤ/Lℤ
```
be the (nonempty) residue set, written in increasing order `0 ≤ r_1 < r_2 < … < r_t < L` where `t = |R|`. Define `f : A → A` by `f(x) = min(A ∩ (x, +∞))` (the least element of `A` strictly greater than `x`). Then:

1. **Well-definedness.** `f(x) mod L` depends only on `x mod L`; the induced map `σ : R → R` is the **cyclic successor**:
   `σ(r_i) = r_{i+1}` for `i < t`, and `σ(r_t) = r_1`.
2. **Injectivity / bijectivity.** `σ` is a bijection of `R`; indeed it is a **single cycle of length `t = |R|`**.
3. **Lift = L, from the start.** For every starting point `x_0 ∈ A`, the orbit `x_{k+1} = f(x_k)` satisfies
   `x_{k+t} = x_k + L` for all `k ≥ 0` (in particular from `k = 0`: no transient).

*Proof.*
*(1) Well-definedness.* Because `A` is `L`-periodic, `A = ⋃_{j=1}^{t} (r_j + L·ℤ)`. Fix `x ∈ A` and write `x = r_i + kL` with `r_i ∈ R`, `k ∈ ℤ`. The set `A ∩ (x, +∞)` consists of all `r_j + m·L` (`1 ≤ j ≤ t`, `m ∈ ℤ`) strictly greater than `r_i + k·L`. The smallest such is obtained by taking the smallest residue strictly larger than `r_i` (cyclically) at the smallest admissible level:
- if `i < t`: the next residue is `r_{i+1} > r_i`, and `r_{i+1} + k·L > r_i + k·L = x`, so `f(x) = r_{i+1} + k·L`;
- if `i = t` (so `r_i = r_t` is the largest residue): no residue in `R` exceeds `r_t` within `[0,L)`, so the next element of `A` above `x = r_t + k·L` is `r_1 + (k+1)·L`, i.e. `f(x) = r_1 + (k+1)·L`.

In both cases `f(x) mod L` is the cyclic successor of `r_i`, independent of `k`. Hence `σ(r_i) = r_{i+1}` (`i<t`) and `σ(r_t) = r_1` is well-defined. (Existence of `f(x)`: `A` is `L`-periodic and nonempty, hence infinite, so `A ∩ (x,+∞) ≠ ∅` and the minimum exists by well-ordering of `ℤ`.)

*(2) Bijectivity / single cycle.* `σ` is, by (1), the map "advance one step in the cyclic order `r_1 → r_2 → … → r_t → r_1`". Its inverse is the cyclic predecessor, so `σ` is a bijection. Moreover the orbit of any `r_i` is `r_i → r_{i+1} → … → r_t → r_1 → … → r_i`, which traverses **all** of `R` before returning; hence `σ` is a single `t`-cycle. (In particular `σ` is injective — this is the "injectivity ⟹ bijection on a finite set" step of the skeleton, here proven directly: `σ` is literally a cyclic shift.)

*(3) Lift = L, from k = 0.* Track the orbit `x_k = f^k(x_0)`. Write `x_k = r_{i_k} + m_k·L` with `i_k ∈ {1,…,t}` and `m_k ∈ ℤ`. By (1), each application of `f` either advances the residue index without wrapping (`i → i+1 ≤ t`, `m` unchanged) or wraps (`i = t → 1`, `m → m+1`). After exactly `t` applications the index returns to its starting value (`i_{k+t} = i_k`, since `σ` is a `t`-cycle) and the wrap counter has increased by exactly `1` (one full traversal of the cyclic order wraps precisely once). Hence `m_{k+t} = m_k + 1` and
```
x_{k+t} = r_{i_k} + (m_k + 1)·L = x_k + L .
```
This holds for **every** `k ≥ 0`, including `k = 0` — the period is exact from the first term, with no transient, and the translation per period is exactly `L` (one full wrap), not a multiple `c·L` with `c ≥ 2`. ∎

(KB: *Pigeonhole / extremal* — cyclic structure of a finite ordered set; *Invariants* — the wrap counter is the invariant. The "injectivity" is part (2); "single cycle ⟹ from-the-start" is (2)+(3); "lift = L" is (3).)

**Remark (consistency with the empirical data).** For `a_1 = 15`, the stabilized admissible set is `A = {m : m divisible by ≥2 of {2,3,5}}`, period `L = 30`, residues `R = {0,6,10,12,15,18,20,24}` (so `t = 8 = T`). The cyclic successor of `15` is `18`, of `18` is `20`, …, of `24` is `0` (wrapping to `30`); after `t = 8` steps the value is `15 + 30 = 45 = a_9`. Theorem 1 recovers `T = |R| = 8`, `L = 30`, from `n = 1`. ∎

**Scope of Theorem 1.** It governs the greedy **once the admissible set is the fixed periodic set `A`**. It does **not** by itself establish that the actual greedy (whose admissible set `A_n` varies with `n`) coincides with iteration on `A`. That coincidence is precisely the two gaps below.

---

### C. Trivial sub-cases (clean, unconditional, from n=1)

These two sub-cases are solved in full. They are the degenerate limits of the general theory where the kernel is a singleton `S = {p}`; we prove them directly, without B1.

#### C.1. A common-prime lock lemma

**Lemma (common-prime lock).** Suppose a prime `p` divides **every** term `a_1, a_2, a_3, …`. Then
```
a_{n+1} = a_n + p   for every n ≥ 1 ,
```
i.e. the conclusion holds with `T = 1`, `L = p`, from `n = 1`.

*Proof.* Fix `n`. Since `p | a_{n+1}` (every term) and `a_{n+1} > a_n` with `p | a_n`, the integer `a_{n+1}` is a multiple of `p` strictly larger than the multiple `a_n` of `p`; the next multiple of `p` after `a_n` is `a_n + p`, so `a_{n+1} ≥ a_n + p`. Conversely, `a_n + p` is a multiple of `p`, and since every past term `a_i` (`i ≤ n`) is divisible by `p`, `gcd(a_n + p, a_i) ≥ p > 1`; thus `a_n + p` is a valid candidate, and by minimality `a_{n+1} ≤ a_n + p`. Hence `a_{n+1} = a_n + p`. ∎ (KB: *Divisor analysis* — multiples of `p`.)

#### C.2. `a_1` even ⟹ `T = 1`, `L = 2` (from `n = 1`)

*Proof.* It suffices (by the common-prime lock with `p = 2`) to show `2 | a_n` for every `n`. We prove this by induction.

Base: `2 | a_1` by hypothesis. Step: assume `2 | a_1, …, a_n`. We show `a_{n+1} = a_n + 2` (hence `2 | a_{n+1}`).
- Upper bound: `a_n + 2` is even, and every past term `a_i` (`i ≤ n`) is even, so `gcd(a_n + 2, a_i) ≥ 2 > 1`; thus `a_n + 2` is a valid candidate, giving `a_{n+1} ≤ a_n + 2`.
- Lower bound: `a_{n+1} > a_n`, so `a_{n+1} ≥ a_n + 1`. But `a_{n+1} = a_n + 1` is impossible, because consecutive integers are coprime — `gcd(a_n + 1, a_n) = 1` — so `a_n + 1` does **not** hit `a_n` (a required past term). Hence `a_{n+1} ≥ a_n + 2`.

Together, `a_{n+1} = a_n + 2`, completing the induction. The common-prime lock (or directly the induction) gives `a_{n+1} = a_n + 2` for every `n ≥ 1`, i.e. `T = 1`, `L = 2`, from `n = 1`. ∎ (KB: *Divisor analysis* — consecutive-integer coprimeness `gcd(k, k+1) = 1`.)

Numerical check: `a_1 = 10` gives `10, 12, 14, 16, 18, …`, diffs all `2`. ∎

#### C.3. `a_1 = p^k` (a prime power) ⟹ `T = 1`, `L = p` (from `n = 1`)

*Proof.* Every term `a_n` must hit `a_1 = p^k`; the only prime dividing `p^k` is `p`, so `gcd(a_n, p^k) > 1` forces `p | a_n`. Thus `p` divides every term, and the common-prime lock gives `a_{n+1} = a_n + p` for every `n ≥ 1`: `T = 1`, `L = p`, from `n = 1`. ∎

Numerical checks: `a_1 = 9 = 3^2` gives `9, 12, 15, 18, …` (step `3`); `a_1 = 25 = 5^2` gives `25, 30, 35, …` (step `5`). ∎

These two sub-cases cover all even `a_1`, all prime powers, and their overlaps (e.g. `a_1 = 2^k`, both apply, `L = 2 = p`).

---

### D. The general case — reduction to the two gaps

Now suppose `a_1` is neither even nor a prime power (equivalently, `a_1` is odd with at least two distinct prime factors). The route attempts to prove `∃ T, L > 0 : a_{n+T} = a_n + L` for every `n ≥ 1` via the injectivity mechanism of Theorem 1. We reduce to two gaps and state them precisely.

Define the **admissible set at time `n`**
```
A_n := { m ∈ ℤ : gcd(m, a_i) > 1 for every i ≤ n } = ⋂_{i=1}^{n} { m : gcd(m, a_i) > 1 } .
```
The greedy is `a_{n+1} = min(A_n ∩ (a_n, +∞))`. Note `A_{n+1} = A_n ∩ { m : gcd(m, a_{n+1}) > 1 } ⊆ A_n`, so `(A_n)` is a decreasing chain.

#### D.1. [GAP: B1 — kernel stabilization]

**Conjecture (B1).** There exist a finite prime set `S` with `primes(a_1) ⊆ S ⊆ {primes p : p ≤ R = rad(a_1)}`, a modulus `L = ∏_{p ∈ S} p`, and an index `N ≥ 1`, such that for all `n ≥ N` the admissible set equals a fixed `L`-periodic set:
```
A_n = A  (for all n ≥ N),   where  A = ⋃_{r ∈ R} (r + L·ℤ) ,   R ⊆ {0,…,L−1},  and  a_n ∈ A  for all n ≥ N .
```

*Why this is needed.* Theorem 1 requires a **fixed** periodic set; the actual greedy uses the varying chain `A_n`. Until `A_n` stabilizes to `A`, the "transition on residues mod `L`" is not even well-defined (two times `n, m` with `a_n ≡ a_m (mod L)` need not have `a_{n+1} ≡ a_{m+1} (mod L)`, because `A_n ≠ A_m`). Indeed, periodicity **mod `R = rad(a_1)` is false** (verified: `a_1 = 15` has `a_1 ≡ a_5 ≡ 0 (mod 15)` but `a_2 ≡ 3`, `a_6 ≡ 6 (mod 15)` — different successors); the modulus must be the kernel product `L = ∏S`, which is what B1 supplies.

*Why this is the crux.* B1 asserts the "kernel" prime set `S` is finite and the hitting pattern stabilizes. This is the shared "B1 river" identified by the outline-reviewer: the set of all primes dividing some `a_n` is **infinite** (free-rider primes accumulate: e.g. `a_1 = 15` has every prime `q` dividing `30q`), so the wrong object is `∪_n supp(a_n)`; the right object is the *essential/kernel* set `S = primes(L)`. Bounding `S` absolutely (conjecturally `S ⊆ {p ≤ R}`) is the genuine difficulty — the competing-candidate/Bertrand mechanism proposed by `bounded-diff-finite-state` is the most concrete attack, but it is unproven here.

*Status.* **Unproven (gap).** The route cannot bypass it: well-definedness of the residue transition presupposes it. This is the collapse the outline-reviewer warned of — the route is not genuinely distinct from `bounded-diff-finite-state` for this step.

#### D.2. Conditional consequence (given B1): eventual periodicity

**Proposition (eventual periodicity, conditional on B1).** Assuming B1, there exist `T, L > 0` with `a_{n+T} = a_n + L` for all `n ≥ N` (where `N` is the stabilization index of B1). In particular the sequence is eventually periodic up to translation.

*Proof (conditional).* For `n ≥ N`, `A_n = A` and `a_n ∈ A`, so the greedy `a_{n+1} = min(A ∩ (a_n, +∞)) = f(a_n)` is exactly the iteration of Theorem 1 on the fixed periodic set `A`. By Theorem 1.(3), `a_{n+T} = a_n + L` for every `n ≥ N`, with `T = |R|` and `L` the period of `A`. ∎

So **conditional on B1**, the route delivers eventual (`n ≥ N`) periodicity, with `T = |R|`, `L = ∏_{p∈S} p`, and lift exactly `L` (not a multiple — Theorem 1.(3)).

#### D.3. [GAP: from-n=1 consistency] — the route's intended "free" payoff is NOT free

The skeleton's distinctive claim was that "from-n=1 is FREE once injectivity holds." This is **not** automatic. Theorem 1 gives from-the-start periodicity **for iteration on the fixed set `A`** — i.e. from `n = N`. The actual greedy uses `A_n ⊋ A` for `n < N` (a *larger* set, fewer constraints), so its choices for `n < N` need not coincide with `f`.

**Conjecture (from-n=1 consistency).** For every `n < N` and every `m ∈ (a_n, f(a_n))` (the open gap between `a_n` and its cyclic successor in the stabilized set `A`), `m ∉ A_n` — equivalently, no "prematurely valid" candidate (one that hits `a_1,…,a_n` but fails some future constraint) lies in the gap. Then the greedy's choice equals `f(a_n)` even for `n < N`, and the conclusion `a_{n+T} = a_n + L` holds for every `n ≥ 1`.

*Why this is a real gap, not a formality.* An element `m ∈ (a_n, f(a_n))` is, by definition of `f(a_n) = min(A ∩ (a_n,+∞))`, **not** in `A` (it fails to hit some `a_j`, `j > n`). But it may still lie in `A_n` (it hits `a_1,…,a_n`), making it a valid candidate at time `n` — in which case the greedy would pick `m < f(a_n)`, breaking the cycle for that `n`. Empirically this never happens (the pre-period is empty in every tested case, including stubborn ones like `a_1 = 187, 209`), but a proof requires showing the gap `(a_n, f(a_n))` — of length at most `R ≤ L` (by the bounded-diff lemma and `L ≥ R = ∏_{p∈P_1} ⊆ S`) — contains no such "temporarily valid" `m`. No argument is known here; the bounded-diff lemma bounds the gap size but does not exclude its contents.

*Status.* **Unproven (gap).** The route's intended payoff (from-n=1 "for free") reduces to this conjecture; it is not delivered by injectivity alone. This is the second, sharper reason the route collapses short of its goal: even granting B1, Theorem 1 only yields from-n=N.

---

### E. Summary and honest self-assessment

- **Proved in full (unconditional):** the bounded-difference lemma `a_{n+1} − a_n ≤ rad(a_1)`; Theorem 1 (iteration on a fixed periodic set is a single cycle, from the start, lift = period); the even-`a_1` sub-case (`T=1, L=2`, from `n=1`); the prime-power sub-case (`T=1, L=p`, from `n=1`).
- **Reduced to gaps:** the general (odd, ≥2-prime-factor) case is reduced to (B1) kernel stabilization and (from-n=1 consistency) no-premature-candidate-in-the-gap.
- **Distinctiveness verdict (sustaining the outline-reviewer's warning):** the route's injectivity crux **does** reduce to Theorem 1 — which is the same "lift = L / from-the-start" mechanism `periodic-set-iteration` isolates as its Theorem 1 and `bounded-diff-finite-state` uses for its final steps. The route is therefore **not genuinely distinct** in mechanism: it repackages the shared final-step theorem plus the shared B1 wall. Its one residual structural observation — that the from-n=1 surprise is a *separate* gap (D.3), not a free corollary of injectivity — is a useful diagnostic but not a proof.

Status: **partial** (two unconditional solved sub-cases; two clean promotable lemmas; the general case blocked by B1 and the from-n=1 consistency gap).

## Promotable lemmas
- **bounded-difference** (Lemma A): `a_{n+1} − a_n ≤ rad(a_1)` for all `n`; proof via the next multiple of `rad(a_1)` after `a_n` hitting every past term through the primes of `a_1`. Proved in full in section A above. (Not yet in `lemmas/`; the builder of `bounded-diff-finite-state` was assigned to certify it — if certified there, import it instead.)
- **periodic-set-single-cycle** (Theorem 1): iterating `f(x)=min(A∩(x,+∞))` on a nonempty `L`-periodic set `A` from any `x_0 ∈ A` gives `x_{k+t}=x_k+L` for every `k ≥ 0` (so from the start, with lift exactly the period `L`, not a multiple), where `t = |A mod L|`; the induced residue map is the cyclic successor, a single `t`-cycle (hence injective/bijective). Proved in full in section B above. This is the shared "injectivity ⟹ bijection ⟹ single cycle ⟹ from-the-start ⟹ lift=L" mechanism that `bounded-diff-finite-state`, `hitting-set-monovariant`, and `periodic-set-iteration` all need for their final steps.
- **common-prime-lock**: if a prime `p` divides every term, then `a_{n+1}=a_n+p` for all `n ≥ 1` (`T=1, L=p`, from `n=1`). Proved in full in section C.1.
