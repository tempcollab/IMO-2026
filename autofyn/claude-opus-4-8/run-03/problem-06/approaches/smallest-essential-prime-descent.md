## Status
solved

## Approaches tried
- (round 10) **aimo-0030 game-framing transplant — SOLVED.** The decisive move: transplant aimo-0030
  ("Ana–Banana") Claims 1–3 + the final minimal-pair descent **in the game/greedy framing** (recursive
  good/bad + strictly-decreasing "moves"), NOT in the static covering framing that walled every prior
  round. In the game framing the descent target `x < n` is *automatic* (it is the definition of a move),
  which is exactly the "GAP B" (`x<n` not automatic for an arbitrary avoiding witness) the covering
  translation could never supply. Establishing the three recursive facts (F1 recursive characterization,
  F2 terms pairwise non-coprime, F3 a_1 good) from the greedy definition + certified ENUM lets Claims 1–3
  and the descent run verbatim over integer values with concrete elementary inequalities
  (y^α < a_1·y ≤ p·y = x/p^{r-1} < n/p^{r-1}). Conclusion: any two similar numbers (same prime factors
  ≤ a_1) have the same good/bad status, so E_∞∩[a_1,∞) is periodic mod M=∏_{p≤a_1}p, and the certified
  periodic-set-enumeration gives the theorem. **Complete, no gaps.** GAP A/B/C of the outline are
  dissolved (not "closed in the covering domain") by switching framing.
- (prior rounds' covering-framed descent) — stalled at GAP B in the covering domain; superseded by the
  game-framing transplant above, which is where `x<n` becomes free.

## Current best
Full solution below (Status: solved). The problem is IMO-2026-P6, whose greedy sequence is exactly the
"good-number" enumeration of the 2015 IMO Shortlist / aimo-0030 game of numbers with k=a_1; its solution
Claims 1–3 + minimal-pair descent transplant to our object with the recursive good/bad characterization
supplied by the certified enumeration lemma. Every step is elementary once F1/F2/F3 are in hand.

## Full proof

Throughout, `a_1 < a_2 < a_3 < …` is the given sequence: each `a_{n+1}` is the smallest integer `> a_n`
with `gcd(a_{n+1}, a_i) > 1` for all `i ≤ n`, and all `a_i > 1`. Write
`E_∞ := { m ∈ ℤ_{>1} : gcd(m, a_i) > 1 for every i ≥ 1 }`.

### 0. Imported certified facts

We use two certified lemmas from the shared cache, verbatim (imported, not re-proved):

- **(ENUM)** [`lemmas/enumeration-of-E-infinity.md`]: `{a_n : n ≥ 1} = E_∞ ∩ [a_1, ∞)`, and `a_n` is the
  `n`-th smallest element of `E_∞` that is `≥ a_1`. In particular the greedy sequence is the increasing
  enumeration of `E_∞ ∩ [a_1,∞)`.
- **(PER)** [`lemmas/periodic-set-enumeration.md`]: if `E ⊆ ℤ` is nonempty and tail-periodic from `a`
  with period `L > 0` (i.e. for all integers `x ≥ a`, `x ∈ E ⟺ x + L ∈ E`), and `E ∩ [a,∞)` is enumerated
  increasingly as `b_1 < b_2 < …`, then with `T := #(E ∩ [a, a+L)) ≥ 1` we have `b_{n+T} = b_n + L` for
  every `n ≥ 1`.

By (ENUM) and (PER), **it suffices to prove that `E_∞` is tail-periodic from `a_1` with some period
`L > 0`**: then `a_{n+T} = a_n + L` for all `n` with `T = #(E_∞ ∩ [a_1, a_1+L)) ≥ 1` and `L > 0`, which
is the desired conclusion.

### 1. Definitions

For an integer `m ≥ a_1`, call `m` **good** if `m ∈ E_∞`, and **bad** if `m ∉ E_∞`. By (ENUM), the good
numbers are exactly the terms `a_1, a_2, a_3, …`.

A **move** `m → x` means: `x` and `m` are integers with `gcd(m, x) = 1` and `a_1 ≤ x < m`.

Call a prime `p` **small** if `p ≤ a_1`, and **big** if `p > a_1`. For `a, b ≥ a_1`, call `a` and `b`
**similar** if they have the same set of small prime divisors. Set `M := ∏_{p ≤ a_1, p prime} p` (a
positive integer, empty product `= 1` only if `a_1 < 2`, impossible since `a_1 ≥ 2`; so `M ≥ 2`).

### 2. Three recursive facts

**Fact F2 (goods are pairwise non-coprime).** *If `g, g'` are good with `g ≠ g'`, then `gcd(g, g') > 1`.*

*Proof.* Say `g = a_i`, `g' = a_j` with `i < j` (goods are the terms, strictly increasing). By the
defining rule, `a_j` was chosen with `gcd(a_j, a_l) > 1` for every `l < j`; taking `l = i` gives
`gcd(a_i, a_j) > 1`. ∎

**Fact F3 (`a_1` is good).** `a_1 = a_1 ∈ {a_n} ⊆ E_∞`, so `a_1` is good. ∎

**Fact F1 (recursive characterization).** *For `m ≥ a_1`:*
`m` *is good* `⟺` *no good `x` with `a_1 ≤ x < m` is coprime to `m`.*
*Equivalently, `m` is bad `⟺` there is a move `m → x` to some good `x`.*

*Proof.* Let `a_1 = a_1 < a_2 < …` be the greedy sequence (= the good numbers, by (ENUM)).

(⟹) Suppose `m` is good, `m = a_i`. Any good `x < m` equals `a_l` for some `l < i`; by F2,
`gcd(x, m) = gcd(a_l, a_i) > 1`. So no good `x < m` is coprime to `m`.

(⟸) Suppose no good `x` with `a_1 ≤ x < m` is coprime to `m`. If `m = a_1`, then `m` is good by F3 (and
the hypothesis is vacuous). If `m > a_1`, then `a_1 < m` is a good number `< m`, so the set of good
numbers `< m` is `{a_1, …, a_j}` for some `j ≥ 1` (finitely many integers in `[a_1, m)`), with `a_j` the
largest good number `< m`. By hypothesis, `m` shares a common factor with each `a_l` (`l ≤ j`), i.e.
`gcd(m, a_l) > 1` for all `l ≤ j`. Now the rule defines `a_{j+1}` as the smallest integer `> a_j` with
`gcd(·, a_l) > 1` for all `l ≤ j`; since `m > a_j` satisfies these conditions, `a_{j+1} ≤ m`. If
`a_{j+1} < m`, then `a_{j+1}` is a good number strictly between `a_j` and `m`, contradicting that `a_j` is
the largest good number `< m`. Hence `a_{j+1} = m`, so `m` is good.

The equivalent phrasing is the contrapositive: `m` bad `⟺` some good `x`, `a_1 ≤ x < m`, has
`gcd(x, m) = 1`, i.e. a move `m → x` to a good `x`. ∎

These three facts are all we use; the actual game of aimo-0030 is never invoked — F1/F2/F3 make the
recursive good/bad calculus available directly on `E_∞`.

### 3. Claim 1 (multiples of goods are good)

*If `n` is good and `n'` is a multiple of `n` with `n' ≥ a_1`, then `n'` is good.*

*Proof.* Suppose `n'` is bad. By F1 there is a move `n' → x` to some good `x`: `gcd(x, n') = 1` and
`a_1 ≤ x < n'`. Since `n ∣ n'`, every prime dividing `n` divides `n'`, so `gcd(x, n') = 1` forces
`gcd(x, n) = 1`. Then `x` and `n` are two good numbers that are coprime, contradicting F2. Hence `n'` is
good. ∎

(We will only need this for `n' = n·t`, `t ≥ 1`, where indeed `n' ≥ n ≥ a_1`.)

### 4. Claim 2 (squaring a factor of a bad number keeps it bad)

*If `r, s` are positive integers with `rs ≥ a_1` bad, then `r²s` is bad.*

*Proof.* `rs` bad, so by F1 there is a move `rs → x` to some good `x`: `gcd(x, rs) = 1` and
`a_1 ≤ x < rs`. Now `r²s` has the same set of prime divisors as `rs` (namely `primes(r) ∪ primes(s)`), so
`gcd(x, r²s) = gcd(x, rs) = 1`; and `x < rs ≤ r²s` (as `r ≥ 1`), while `x ≥ a_1`. Also `r²s = r·(rs) ≥ rs
≥ a_1`. Thus `r²s → x` is a move to a good `x`, so by F1, `r²s` is bad. ∎

**Contrapositive of Claim 2:** *if `rs ≥ a_1` and `r²s` is good, then `rs` is good.*

### 5. Claim 3 (multiplying a bad number by a big prime keeps it bad)

*If `p > a_1` is prime and `n ≥ a_1` is bad, then `np` is bad.*

*Proof.* Suppose the claim fails. Among all counterexamples `(p, n)` (with `p > a_1` prime, `n ≥ a_1` bad,
`np` good) choose one with `n` minimal; this is possible since the values `n` form a nonempty set of
positive integers. So `n` is bad, and `np` is good (note `np ≥ n ≥ a_1`).

Since `n` is bad, by F1 there is a move `n → x` to some good `x`:
```
gcd(x, n) = 1,     a_1 ≤ x < n,     x good.               (5.1)
```
Consider whether `np → x` is a move. We have `a_1 ≤ x < n < np` and `gcd(x, n) = 1`; if also
`gcd(x, p) = 1`, then `gcd(x, np) = 1`, so `np → x` would be a move to a good `x`, forcing `np` bad by F1
— contradicting `np` good. Therefore `p ∣ x`. Write
```
x = p^r · y,     r ≥ 1,     p ∤ y,     y ≥ 1.             (5.2)
```

**Sub-case `y = 1`.** Then `x = p^r`. Since `p > a_1`, `p ∤ a_1`, and `p` is the only prime of `x`, so
`gcd(a_1, x) = 1`. Also `x = p^r ≥ p > a_1 ≥ a_1`, so `a_1 ≤ a_1 < x`. Thus `x → a_1` is a move, and
`a_1` is good (F3), so by F1 `x` is bad — contradicting that `x` is good. Hence `y ≥ 2`.

**Sub-case `y ≥ 2`.** Let `α ≥ 1` be the least positive integer with `y^α ≥ a_1` (it exists since
`y ≥ 2` makes `y^α → ∞`). By minimality of `α`,
```
y^{α-1} < a_1        (5.3)
```
(true also for `α = 1`, where `y^0 = 1 < a_1` because `a_1 ≥ 2`).

*`y^α` is bad.* From (5.2), `primes(y) = primes(x) ∖ {p}` and, since `y ∣ x` with `gcd(x, n) = 1`, also
`gcd(y, n) = 1`. Hence
```
primes(y^α) ∩ primes(np) = primes(y) ∩ (primes(n) ∪ {p}) = ∅,
```
so `gcd(y^α, np) = 1`. Now `y^α ≥ a_1`, and `np` is good; if `y^α` were good, then `np` and `y^α` would
be two coprime goods, contradicting F2. Therefore `y^α` is bad.

*Descent inequality.* Using (5.3), `a_1 < p` (as `p > a_1`), and `x < n` from (5.1):
```
y^α = y · y^{α-1} < y · a_1 ≤ y · p ,
```
and multiplying by `p^{r-1} ≥ 1`,
```
p^{r-1} · y^α < p^{r-1} · (y · p) = p^r · y = x < n .           (5.4)
```
In particular `p^{j} · y^α ≤ p^{r-1} · y^α < n` for every `0 ≤ j ≤ r-1`.

*Iterated Claim 3 below `n`.* Because `n` was chosen minimal among counterexamples, Claim 3 **holds** for
every bad integer `< n` (with the same big prime `p`). We show by induction on `j = 0, 1, …, r` that
`p^{j} · y^α` is bad:
- `j = 0`: `y^α` is bad (shown above).
- Induction step `j → j+1` (`0 ≤ j ≤ r-1`): `p^{j} y^α` is bad and, by (5.4), `p^{j} y^α < n`; since
  Claim 3 holds for all bad integers `< n`, applying it to the bad number `p^{j} y^α` and the big prime
  `p` gives `p^{j} y^α · p = p^{j+1} y^α` bad.

Hence `p^{r} · y^α` is bad.

*Contradiction.* From (5.2), `x = p^r y` and `y ∣ y^α` (as `α ≥ 1`), so `x = p^r y ∣ p^r y^α`. Thus
`p^r y^α` is a multiple of the good number `x`, and `p^r y^α ≥ y^α ≥ a_1`; by Claim 1, `p^r y^α` is good.
This contradicts `p^r y^α` being bad. The contradiction proves Claim 3. ∎

### 6. Main claim: similar numbers have the same status

*If `a, b ≥ a_1` are similar, then `a` and `b` are both good or both bad.*

**Reduction.** It suffices to prove:
> **(★)** For every `c ≥ a_1` and every multiple `d` of `c` with `d` similar to `c`, the numbers `c` and
> `d` have the same status.

Indeed, given similar `a, b ≥ a_1`, put `d := ab ≥ a_1`. The set of small prime divisors of `ab` is
`(small primes of a) ∪ (small primes of b)`, which equals the small primes of `a` (and of `b`) since `a`,
`b` are similar; so `ab` is similar to `a` and to `b`. Also `ab` is a multiple of `a` and of `b`. By (★)
with `(c,d) = (a, ab)`, `a` and `ab` have the same status; by (★) with `(c,d) = (b, ab)`, `b` and `ab`
have the same status. Hence `a` and `b` have the same status.

**Proof of (★).** Suppose (★) fails. Among all counterexamples `(c, d)` — `d` a multiple of `c ≥ a_1`,
`d` similar to `c`, `c` and `d` of opposite status — choose one, `(c_0, d_0)`, with `d_0` minimal.

By Claim 1, if `c_0` were good then `d_0` (a multiple of `c_0`, `≥ a_1`) would be good too — same status,
no counterexample. Hence
```
c_0 is bad and d_0 is good.
```
If `d_0 = c_0` they would have equal status; so `d_0 ≠ c_0`, and being a multiple of `c_0`, `d_0 ≥ 2c_0 >
c_0`. Thus `d_0 / c_0 ≥ 2` has a prime factor `p`, and `p ∣ d_0`. Because `d_0/c_0 ≥ 2` is divisible by
`p`, we may write
```
d_0 / c_0 = p · u   for some integer u ≥ 1,   whence   d_0 / p = c_0 · u,     (6.1)
```
so `d_0/p` is an integer and `c_0 ∣ (d_0/p)`.

We claim `(c_0, d_0/p)` is again a valid counterexample, contradicting minimality of `d_0`. First,
`d_0/p < d_0`. Second, `c_0 ∣ (d_0/p)` by (6.1), so `d_0/p` is a multiple of `c_0`. Third, `d_0/p` is
similar to `c_0`: since `c_0 ∣ d_0/p ∣ d_0`, the small-prime-divisor sets satisfy
`small(c_0) ⊆ small(d_0/p) ⊆ small(d_0) = small(c_0)` (the last equality because `c_0, d_0` are similar),
so all three are equal; in particular `small(d_0/p) = small(c_0)`. It remains to show `c_0` and `d_0/p`
have opposite status, i.e. (as `c_0` is bad) that `d_0/p` is good. We split on the size of `p`.

*Case `p ≤ a_1` (small).* Since `c_0` and `d_0` are similar and `p ∣ d_0` is small, `p ∣ c_0`. Together
with `p ∣ d_0/c_0` (our choice of `p`), this gives `p^2 ∣ d_0`. Apply the **contrapositive of Claim 2**
with `r := p`, `s := d_0 / p^2` (a positive integer since `p^2 ∣ d_0`): then `r^2 s = d_0` and
`r s = p · (d_0/p^2) = d_0 / p`, with `rs = d_0/p = c_0 u ≥ c_0 ≥ a_1`. Since `d_0 = r^2 s` is good, the
contrapositive of Claim 2 gives `rs = d_0/p` good.

*Case `p > a_1` (big).* Set `n := d_0/p ≥ a_1` (indeed `d_0/p = c_0 u ≥ c_0 ≥ a_1` by (6.1)). Then
`np = d_0` is good. If `n` were bad, Claim 3 (with the big prime `p`) would make `np = d_0` bad — false.
Hence `n = d_0/p` is good.

In both cases `d_0/p` is good while `c_0` is bad, so `(c_0, d_0/p)` is a counterexample with
`d_0/p < d_0`, contradicting the minimality of `d_0`. Therefore (★) holds, and with it the Main claim. ∎

### 7. Periodicity of `E_∞` and conclusion

Recall `M = ∏_{p ≤ a_1} p ≥ 2`. Take any integer `n ≥ a_1`; then `n + M ≥ a_1`. For every small prime
`p` (so `p ∣ M`), `n ≡ n + M (mod p)`, hence `p ∣ n ⟺ p ∣ (n+M)`. Thus `n` and `n + M` have the same set
of small prime divisors, i.e. they are **similar**. By the Main claim, `n` and `n+M` have the same
good/bad status:
```
n ∈ E_∞  ⟺  n is good  ⟺  n+M is good  ⟺  n+M ∈ E_∞     (for all n ≥ a_1).
```
This is exactly tail-periodicity of `E_∞` from `a_1` with period `L := M > 0`. `E_∞` is nonempty
(`a_1 ∈ E_∞`). By (PER), setting `T := #(E_∞ ∩ [a_1, a_1 + M)) ≥ 1` (nonempty, as `a_1` lies in it) and
`L := M`, the increasing enumeration `a_1 < a_2 < …` of `E_∞ ∩ [a_1,∞)` satisfies
```
a_{n+T} = a_n + L      for every positive integer n,
```
with `T` and `L = M` positive integers. This is the required statement. ∎

### 8. Verification

The result is a proof of an existence statement (`∃ T, L`), so "verification" means a consistency check
of the produced `(T, L)`. Taking `L = M = ∏_{p ≤ a_1} p`: for `a_1 = 15`, `M = 2·3·5·7·11·13 = 30030`,
and the true minimal period of `E_∞` for `a_1 = 15` is `30` (certified in
`lemmas/periodic-set-enumeration.md`; also matches aimo-0030 Comment 3), which divides `M`, so `M` is
indeed a valid (non-minimal) period — consistent. Direct computation of the greedy sequence for
`a_1 ∈ {15, 35, 99, 231}` confirms that any two similar numbers `≥ a_1` in the computed range have the
same good/bad status (the content of the Main claim), hence `n ∈ E_∞ ⟺ n+M ∈ E_∞` for `n ≥ a_1`. The
conclusion `a_{n+T} = a_n + L` for all `n` then follows from (ENUM)+(PER) as above. (These computations
only corroborate; the proof in §§1–7 is self-contained.)

∎

## Promotable lemmas

- **(F1) Recursive good/bad characterization** (§2). For `m ≥ a_1`: `m ∈ E_∞ ⟺` no term `x` with
  `a_1 ≤ x < m` is coprime to `m`; equivalently `m ∉ E_∞ ⟺` there is a term `x`, `a_1 ≤ x < m`,
  `gcd(x,m)=1`. Proved from the greedy definition + (ENUM). *This is the load-bearing bridge* that makes
  the aimo-0030 game calculus available on `E_∞` without invoking any game. Reusable by every approach.
- **(Similarity-closure of `E_∞`) Main claim** (§6). If `a, b ≥ a_1` have the same set of prime divisors
  `≤ a_1`, then `a ∈ E_∞ ⟺ b ∈ E_∞`. Consequently `E_∞` is periodic from `a_1` with period
  `∏_{p ≤ a_1} p`. This is the crux of P6, proved in full; it immediately implies (and is stronger than)
  the standing (CSP)/(SL) target. Worth certifying as the terminal lemma.
- **(Claims 1–3)** the three monotonicity lemmas (multiple-of-good is good; `rs` bad ⟹ `r²s` bad; `n`
  bad, `p>a_1` prime ⟹ `np` bad), each proved via F1/F2/F3. Reusable building blocks.
