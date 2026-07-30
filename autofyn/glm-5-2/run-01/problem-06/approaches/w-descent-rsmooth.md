# Approach: w-descent-rsmooth

## Status
solved

## Approaches tried
- (round 3, this build) Discovered that the retrieved crux `aimo-0030` (IMO 2013 SL N5, "game of numbers") IS this problem: its good-number set (official solution, Comment 2) is exactly our greedy set, and its similarity theorem (proved from scratch via the **s-substitution** = Claim 4 + a **minimal-counterexample descent**) directly yields periodicity. Built the complete self-contained proof by transcribing the crux shape into the P6 language (no game theory; the "good/bad" dichotomy is replaced by membership in the greedy set G, characterized combinatorially). The s-substitution IS the (W)-mechanism the outline sought, the minimal-counterexample descent IS the "late-arrival" mechanism (GAP F), and the delay-window issue (GAP C / (W)-at-step-n) **dissolves**: with the natural aimo threshold "small = primes ≤ a_1" (rather than the spine's rad(a_1)), the a_1=135 delay-2 artifact vanishes (a_2=138=2·3·23 is 135-smooth, since 23≤135). Periodicity follows without the certified B1'-spine (a direct corollary of similarity + Theorem 1), so B1' AND B2 are both closed. Outcome: SOLVED.
- (round 3, patch v2) Reviewer DOWNGRADED v1 to CHANGES REQUESTED with a precise, correct gap: Lemma 2's Case 2 implicitly assumed `b` has a big prime (anchor `a·q ≤ b`), but the construction was invoked unconditionally — when `b` is `k`-smooth there is no `q`, and Case 2's inflation overshoots (`a_1=15, b=18=2·3²` gives `x=24>18`). This is exercised in the purely-smooth regime (`a_1 ∈ {175,221,385}` where NO greedy term has a big prime). Applied the reviewer-specified **one-case-split patch**: Case 1 (`b` k-smooth ⟹ `x = b`) handles the base/purely-smooth case; Case 2 (`b` has big prime) keeps the strip+inflate construction unchanged. Re-verified the **descent survives equality**: the minimal-counterexample argument needs `r' ≤ r` (NOT `r' < r`); the strict decrease is `max(r,r') = r < a = (move)`, independent of whether `r'=r` or `r'<r`. In the purely-smooth regime Case 1 always fires (`r' = r`), and the descent reduces to the common-small-prime contradiction without any stripping. Verified computationally across `a_1 ∈ {15,35,77,91,105,135,175,187,221,385}`: Lemma 2 (patched) 0 failures; similarity 0 violations. Outcome: SOLVED (gap closed).

## Current best
A complete, rigorous, self-contained proof of the theorem (periodicity a_{n+T}=a_n+L for all n≥1). The crux is the **similarity theorem** (two integers ≥a_1 with the same set of prime factors ≤a_1 have the same membership in the greedy set G), proved by minimal counterexample using the **s-substitution lemma** (strip every prime factor >a_1 of a greedy element b, replace by a bounded power of one small prime to land back in [a_1,b]; the result is a_1-smooth, "similar" to b, and ≤ b). Similarity ⟹ the greedy set is periodic modulo P=∏(primes≤a_1) ⟹ Theorem 1 (cited, `lemmas/periodic-set-iteration.md`) gives a_{n+T}=a_n+P from n=1 (no pre-period, so B2 is free). No open gaps.

## Full proof

We prove the theorem for **every** initial value `a_1 > 1`. Fix `a_1` and let the greedy sequence be
```
a_1 > 1,   a_{n+1} = min{ m > a_n : gcd(m, a_i) > 1  for every i = 1, …, n }.   (★)
```
Set
```
k := a_1,    P := ∏_{p ≤ k, p prime} p   (product of all primes not exceeding k).
```
We call a prime **small** if `p ≤ k` and **big** if `p > k`. Two integers `b, b' ≥ k` are **similar** if they are divisible by exactly the same small primes, i.e. `{p ≤ k : p | b} = {p ≤ k : p | b'}`. The proof has four parts: (I) a combinatorial characterization of the greedy set `G = {a_1, a_2, …}`; (II) the **s-substitution lemma**; (III) the **similarity theorem** (every two similar integers ≥ k are either both in `G` or both outside `G`); (IV) periodicity via `lemmas/periodic-set-iteration.md`. Parts (I)–(III) are proved from scratch (they adapt the crux `aimo-0030`, retrieved from `past_crux_moves_database.json`, problem_id `aimo-0030`, subtopic `size-bounding-and-descent`); each borrowed step is re-proved here in the language of the greedy sequence, with no game theory and no citation of `aimo-0030` as authority.

---

### Part I. The greedy set, and its self-referential characterization

Let `G = {a_1, a_2, a_3, …}` (viewed as a set). The first term `a_1 = k` belongs to `G` by definition. We use throughout the **bounded-difference lemma** (`lemmas/bounded-difference.md`, CERTIFIED): `a_{n+1} − a_n ≤ R := rad(a_1) ≤ k`, so the greedy is well-defined (a fresh term always exists) and `G` is an infinite unbounded subset of `[k, ∞)`.

**Lemma 1 (characterization).** *For an integer `n ≥ k`,*
```
n ∈ G  ⟺  for every g ∈ G with g < n, one has gcd(n, g) > 1.        (†)
```
*Proof.* Write `H := {n ≥ k : gcd(n,g) > 1 for every g ∈ G with g < n}`. We prove `G = H`.

`G ⊆ H`. Let `n ∈ G`. If `n = k = a_1`, there is no element of `G` below `n`, so the condition in `H` holds vacuously. If `n = a_j ∈ G` with `j ≥ 2`, then `n` was selected by (★) at step `j−1` precisely because it is coprime to none of `a_1, …, a_{j−1}`; the set `{a_1, …, a_{j−1}}` is exactly `G ∩ [k, n)`, so `gcd(n, g) > 1` for every `g ∈ G` with `g < n`. Hence `n ∈ H`.

`H ⊆ G`. Let `n ∈ H` with `n > k` (the case `n = k` is `a_1 ∈ G` tautologically). Suppose, for contradiction, that `n ∉ G`. Let `g_r` be the largest element of `G ∩ [k, n)` (it exists, since `a_1 = k < n` is in this set; it is finite since `G ∩ [k,n) ⊆ [k,n)`). The greedy selects `a_{r+1} = min{ m > g_r : gcd(m, a_i) > 1 for every i ≤ r }`. Because `n ∈ H`, `n` is coprime to none of `g_1, …, g_r` (the elements of `G` below `n`, all of which are ≤ g_r and hence among `a_1, …, a_r`); and `n > g_r`. Thus `n` is an admissible candidate for step `r`, so `a_{r+1} ≤ n`. If `a_{r+1} = n` then `n ∈ G`, contradiction. Hence `a_{r+1} < n`. But `a_{r+1} ∈ G` and `g_r < a_{r+1} < n`, contradicting the choice of `g_r` as the largest element of `G ∩ [k, n)`. So `n ∈ G`. ∎

The equivalence (†) is the exact combinatorial avatar of the "good/bad" dichotomy of the source crux (`n` is "good" ⟺ `n ∈ G`): `n ∈ G` iff no smaller element of `G` is coprime to `n`.

**Corollary 1.1 (two good numbers share a prime).** *If `g_1 < g_2` are distinct elements of `G`, then `gcd(g_1, g_2) > 1`.* **Proof.** `g_2 ∈ G` and `g_2 > k`; by Lemma 1, `g_2` is coprime to none of the elements of `G` below it, in particular `g_1`. ∎

**Corollary 1.2 (a bad number has a move to a smaller good number).** *If `n ≥ k` and `n ∉ G`, then there exists `r ∈ G` with `r < n` and `gcd(n, r) = 1`.* **Proof.** `n > k` (since `k = a_1 ∈ G`), and `n ∉ H` (Lemma 1, contrapositive of `H ⊆ G`), so `n` fails the condition in `H`: some `g ∈ G` with `g < n` has `gcd(n, g) = 1`. Take `r = g`. ∎

---

### Part II. The s-substitution lemma

**Lemma 2 (s-substitution, with case-split).** *Let `b ≥ k` be an integer that is divisible by at least one small prime. Then there exists an integer `x` with*
```
k ≤ x ≤ b,    x has no big prime factor (x is k-smooth),    x is similar to b.
```
*Proof.* Let `a` be the product of all *distinct* small prime divisors of `b` (so `a` is squarefree, every prime of `a` is small, and `a | b`). Pick any small prime `p` dividing `b` (which exists by hypothesis; then `p | a`, so `p ≤ a`). We split on whether `b` is already `k`-smooth.

**Case 1 — `b` is `k`-smooth (no prime of `b` exceeds `k`).** Take `x = b`. Then `x = b` satisfies `k ≤ x ≤ b` (with equality on both sides), `x` is `k`-smooth by hypothesis, and `x` is similar to `b` trivially. Done. (This is the **base case** of the s-substitution: nothing needs to be stripped. It carries the whole argument in the "purely-smooth regime" where no greedy term ever has a big prime — e.g. `a_1 ∈ {175, 221, 385}`, verified empirically: among the first 300 greedy terms, 0 carry a prime `> a_1`.)

**Case 2 — `b` has a big prime `q > k`.** Let `n ≥ 0` be the least integer with `x := p^n · a ≥ k` (well-defined since `p ≥ 2`). Then `x` is a product of small primes only, hence `k`-smooth, and its set of small prime divisors is exactly the set of primes of `a`, i.e. the small-prime set of `b`; so `x` is similar to `b`. It remains to show `x ≤ b`.

If `n = 0` then `x = a`; as `a` is a product of distinct prime divisors of `b` and `b` has at least one small prime, `a | b`, so `a ≤ b`. Done.

If `n ≥ 1`, the minimality of `n` gives `p^{n−1}·a < k`, hence
```
x = p^n · a = p · (p^{n−1}·a) < p · k.
```
Now `p ≤ a` (because `p | a`) and `k < q` (big prime). Because `a` is coprime to `q` (the primes of `a` are small, `q` is big) and both `a | b` and `q | b`, the product `a·q` divides `b`, so `a·q ≤ b`. Stringing the inequalities,
```
x < p·k ≤ a·k < a·q ≤ b,
```
where `p·k ≤ a·k` uses `p ≤ a`, and `a·k < a·q` uses `k < q`. Hence `x < b`. Done. ∎

**Remark (why the case-split, and why `x ≤ b` rather than `x < b`).** The bound in Case 2 is anchored by a big prime `q` of `b` via `a·q ≤ b`; when `b` is `k`-smooth there is no such `q` and the construction of Case 2 would not produce a witness ≤ `b` (e.g. `a_1 = 15, b = 18 = 2·3²` is `15`-smooth, and the Case-2 inflation would give `x = 24 > 18 = b`). Case 1 (`x = b`) closes exactly those inputs. The conclusion is `x ≤ b` (not `x < b`): in Case 1 equality holds, in Case 2 the inequality is strict. This is deliberate and sufficient — the **minimal-counterexample descent in Theorem (similarity) only requires `r' ≤ r`**, not `r' < r` (the descent's strict decrease comes from `r < a`, the *move* of Corollary 1.2, which is independent of whether `r' = r` or `r' < r`). See the remark following Theorem (similarity).

(This is the s-substitution / R-smooth-stripping move the outline sought: write `s` = `k`-smooth part of `b` and inflate by a minimal power of one small prime to clear `k`. The bound `x ≤ b` is the load-bearing comparison of products of distinct prime factors of `b`.)

**Corollary 2.1.** *If `b ∈ G` and `b` is not `k`-smooth, the integer `x` supplied by Lemma 2 (Case 2) satisfies `x < b`. If `b` is `k`-smooth, Lemma 2 (Case 1) gives `x = b`. In both cases `x ≤ b`, `x` is `k`-smooth, `x` is similar to `b`. Once the similarity theorem of Part III is available, `x ∈ G` (a similar number to a `G`-element is itself a `G`-element). In particular every "class" of `G`-elements (a similarity class) contains a `k`-smooth element of `G` (its smallest member is `k`-smooth by an iterated application of Lemma 2: if the smallest member `m` of a class were not `k`-smooth, Lemma 2 Case 2 would produce a strictly smaller `k`-smooth similar `x < m` with `x ∈ G`, contradicting minimality of `m`).* This is the precise content of the outline's invariant **(W)**, with the threshold `k = a_1` in place of the spine's `rad(a_1)`.

---

### Part III. The similarity theorem

**Theorem (similarity).** *If `a, b ≥ k` are similar, then either `a, b ∈ G` or `a, b ∉ G`.*

*Proof.* Suppose not, and choose a counterexample pair `(a, b)` with `a ∉ G`, `b ∈ G`, `a, b` similar, and `max(a, b)` as small as possible among all such pairs (well-defined, since `max(a,b)` is a positive integer ≥ k). Both `a` and `b` are ≥ k; `a ≠ b` (one is in `G`, the other not).

Because `a ∉ G`, Corollary 1.2 furnishes a **move** `a ⟶ r`: an element `r ∈ G` with `r < a` and `gcd(a, r) = 1`.

Both `k = a_1` and `r` lie in `G`. By Corollary 1.1 (if `r ≠ k`) or trivially (if `r = k`, take any prime of `k`), there is a prime `p` with `p | k` and `p | r`. Since `p | k`, `p` is small. In particular `r` has a small prime divisor, so Lemma 2 (s-substitution) applies to `r`: there is an integer `r'` with `k ≤ r' ≤ r`, `r'` `k`-smooth, and `r'` similar to `r`.

Now `max(r, r') = r < a ≤ max(a, b)`. The pair `(r, r')` is similar (both similar to one another by construction). By the minimality of `max(a,b)` in the choice of counterexample, a similar pair with strictly smaller maximum cannot have opposite `G`-status; since `r ∈ G`, we conclude `r' ∈ G`.

Both `r'` and `b` lie in `G`. By Corollary 1.1 (if `r' ≠ b`) or trivially (if `r' = b`, take any prime factor of the `k`-smooth number `r' = b`), there is a prime `p'` with `p' | r'` and `p' | b`. Because `r'` is `k`-smooth, every prime divisor of `r'` is small, so `p'` is small.

We now chain three similarity observations:
- `r'` is similar to `r`, and `p'` is a small prime dividing `r'`; similarity means "same small-prime set", so `p' | r`.
- `b` is similar to `a`, and `p'` is a small prime dividing `b`; similarity gives `p' | a`.
- (Already: `p' | r'` and `p' | b`.)

Thus `p' | a` and `p' | r`, which forces `gcd(a, r) ≥ p' ≥ 2`. But `a ⟶ r` is a move, meaning `gcd(a, r) = 1`. Contradiction. ∎

**Remark on the outline's "late-arrival" gap (GAP F).** The minimal-counterexample argument above *is* the late-arrival descent the outline sought. The s-substitution (Lemma 2) produces the `k`-smooth witness `r' ≤ r` "similar to" the greedy element `r`; minimality of the counterexample forces `r' ∈ G` (the `k`-smooth similar number must already be a greedy element, arriving no later than `r`). **The descent only requires `r' ≤ r`, not `r' < r`**: the strict decrease that powers the contradiction is `max(r, r') = r < a ≤ max(a, b)` (the move `a ⟶ r` from Corollary 1.2 gives `r < a` regardless of how `r'` relates to `r`), so the equality `r' = r` allowed by Lemma 2 Case 1 (when `r` is `k`-smooth) does not stall the descent — `max(r, r') = r` strictly decreases `max(a, b)` to `r` whether `r' = r` or `r' < r`. There is no unbounded delay: the `k`-smooth representative of each similarity class lies at or below the first greedy element of that class that carries a big prime, and if a class's smallest member is already `k`-smooth there is nothing to produce (Case 1). The `a_1 = 135` "delay-2" phenomenon recorded in the outline is an artifact of the *spine's* tighter threshold `rad(135) = 15` (under which `23` is "big"); with the natural threshold `k = a_1 = 135`, the term `a_2 = 138 = 2·3·23` is already `135`-smooth (since `23 ≤ 135`), so there is no delay at all. In the **purely-smooth regime** (`a_1 ∈ {175, 221, 385}`, where no greedy term ever carries a prime `> a_1`), every greedy element is `k`-smooth, Lemma 2 always takes Case 1 (`r' = r`), and the descent reduces to: pick the minimal counterexample `(a, b)`; move `a ⟶ r`; with `r' = r`, find a common small prime `p'` of `r` and `b`; similarity forces `p' | a`, contradicting `gcd(a, r) = 1`. The argument is uniform across both regimes.

**Remark on the outline's "(W)-at-step-n" gap (GAP C).** Because similarity holds for *all* `n ≥ k` simultaneously (not inductively step-by-step), the s-substitution + similarity give, for every `n` and every similarity class `σ*` that appears among `a_1, …, a_n`, a `k`-smooth element `x ∈ G` of class `σ*` with `x ≤ a_j ≤ a_n` (where `a_j` is any `σ*`-term, `j ≤ n`); since `x ∈ G ∩ [k, a_n] = {a_1, …, a_n}`, the witness `x = a_i` is among the first `n` terms. So **(W) holds at step `n` for every `n`**, with no pre-arrival window to handle separately.

**Remark on the "s-substitution admissibility" gap (GAP E).** The outline worried that the `k`-smooth part `s` of `a_j` might fail to be admissible for the prior terms. In the present proof this concern does not arise: we never need `s` (or `r'`) to be admissible for the past *directly*; we need `r' ∈ G`, which is supplied by the *similarity theorem* (not by an admissibility check). And the similarity theorem is proved once and for all in Part III. So GAP E is dissolved, not bypassed: the admissibility of `r'` is a consequence of `r' ∈ G` (= being a greedy element), which is exactly what similarity delivers.

---

### Part IV. Periodicity

Let `R ⊆ {0, 1, …, P−1}` be the set of residues `r` such that (any / every) integer `n ≥ k` with `n ≡ r (mod P)` lies in `G`; this is well-defined by the next paragraph.

**Claim.** `G`-membership of `n ≥ k` depends only on `n mod P`.

*Proof of Claim.* By the Chinese remainder theorem, `n mod P` determines `n mod p` for every prime `p ≤ k` (the primes `p ≤ k` are pairwise coprime and their product is `P`). In turn `n mod p` determines whether `p | n`. Hence `n mod P` determines the full small-prime set `{p ≤ k : p | n}`, i.e. the similarity class of `n`. By the similarity theorem, two similar integers ≥ k have the same `G`-membership. ∎

Consequently `G` (as a subset of `[k, ∞)`) is `P`-periodic: for `n ≥ k`, `n ∈ G ⇔ n + P ∈ G` (since `n + P ≡ n (mod P)` and `n + P ≥ k`). Extend `G` to a `P`-periodic subset of all of `ℤ` by `G^* := {m ∈ ℤ : m mod P ∈ R}`; then `G^* + P = G^*`, `G^* ∩ [k, ∞) = G`, and `a_1 = k ∈ G^*` (because `k ∈ G`).

The greedy orbit is the cyclic successor on `G^*`. Indeed, by definition of `G` as the greedy set, `a_{n+1}` is the least element of `G` greater than `a_n`; since `a_n ≥ k`, this equals `min{m ∈ G^* : m > a_n}`. That is, with `f_{G^*}(x) := min{m ∈ G^* : m > x}`, we have `a_{n+1} = f_{G^*}(a_n)` for every `n ≥ 1`.

Apply **Theorem 1** (`lemmas/periodic-set-iteration.md`, CERTIFIED): `G^*` is nonempty and `P`-periodic, and `a_1 ∈ G^*`; therefore the orbit `a_1, a_2, … = f_{G^*}`-orbit from `a_1` satisfies
```
a_{n+T} = a_n + P   for every n ≥ 1,
```
where `T = |G^* ∩ [0, P)| = |R|`. (Theorem 1 gives periodicity *from the start* `k = 0`, i.e. from `n = 1` in our indexing — no pre-period.)

Setting `L := P` and `T := |R|` (both positive integers) yields `a_{n+T} = a_n + L` for every positive integer `n`. ∎

---

### Remarks: scope, B1'/spine, B2, and the "R-large regime"

- **B1' and the certified spine are subsumed, not used.** The outline's plan was to prove B1' (`M_n = M'_n`, equivalently `a_{n+1} = min(B_n ∩ (a_n,∞))`) via the reduction `(W) ⟹ (C) ⟹ B1'` and then cite the certified spine `B1' ⟹` periodicity from `N`. The similarity theorem is *stronger* and *more direct*: it gives periodicity from `n = 1` (not merely from some `N`), with no B1' intermediary. For completeness, the outline's reduction does go through as a corollary: with the threshold `k = a_1`, define `P_k = {primes ≤ k}`, `σ(n) = supp(n) ∩ P_k`, `M'_n` the minimal hitting sets of `{σ(a_i) : i ≤ n}`, `B_n = ∪_{h ∈ M'_n}{multiples of ∏h}`, `b_n = min(B_n ∩ (a_n,∞))`. Invariant **(W)** ("every σ*-class of `F'_n` has a `k`-smooth term among `a_1,…,a_n`") holds by Part II + Part III (Cor. 2.1 and the (W)-at-step-n remark). The reduction **(W) ⟹ (C)** is then exactly the clean argument of the outline: if `m ∈ A_n ∩ (a_n, a_n+R]` missed some `σ* ∈ F'_n`, take the `k`-smooth `a_j` (`j ≤ n`) with `σ(a_j) = σ*` supplied by (W); `m ∈ A_n` forces `gcd(m, a_j) > 1`, and any prime `p | gcd(m, a_j)` lies in `supp(a_j) ⊆ P_k` (k-smoothness) and in `σ*`, while `p | m` puts `p ∈ σ(m)`, contradicting `σ(m) ∩ σ* = ∅`. Hence (C): `A_n ∩ (a_n, a_n+R] ⊆ B_n`. Then **(C) ⟹ B1'** via `a_{n+1} ∈ (a_n, a_n+R]` (`lemmas/bounded-difference.md`) and `b_n ∈ (a_n, a_n+R]` (`lemmas/small-prime-minimum-in-window.md`, with `R` there taken as `rad(a_1) ≤ k`, so the window `(a_n, a_n+R] ⊆ (a_n, a_n+k]`). So B1' is a corollary; but the proof does not need it, since similarity already gives periodicity.

- **B2 (from `n = 1`) is free.** Theorem 1 supplies periodicity from `n = 1` (no pre-period inside the periodic set, because the orbit starts at `a_1 ∈ G^*`). The empirical observation of `current.md` (every tested `a_1` satisfies `a_{1+T} = a_1 + L` from `n = 1`, e.g. `a_1 = 15` gives `(T,L) = (8,30)`) is explained: the true period `L` divides `P`, and `a_1` already lies in the `L`-periodic good set, so no transient occurs. The deferral of B2 to the sibling slug `b2-induction-step` is therefore unnecessary for this approach — B2 is closed here.

- **The "R-large regime" (outline point 4) is subsumed.** The outline conjectured a threshold `R ≥ (?)` above which no `a_n` carries a big prime, making (W) trivial. No such threshold is needed: for *every* `a_1`, Lemma 2 + similarity handle the terms that *do* carry big primes (producing a `k`-smooth similar member of `G` at or below them), and terms carrying no big prime are already `k`-smooth. Empirically, for `a_1 ∈ {175, 385}` *no* term among the first 300 carries a prime `> a_1` (so every term is `a_1`-smooth and (W) is immediate), while for `a_1 ∈ {15, 35, 77, 91, 105, 135}` some terms do carry big primes and are handled by the s-substitution + similarity. Both regimes are covered by the single argument.

- **Trivial cases.** The certified trivial cases (`a_1` even ⟹ `T = 1, L = 2`; `a_1 = p^α` ⟹ `T = 1, L = p`) are subsumed: the theorem gives `L = P = ∏(primes ≤ a_1)` (a possibly non-minimal period), which is a valid choice of `L` for those inputs too (`a_{n+T} = a_n + P` holds with `T = |R|`).

- **Sigma-periodicity consistency.** The round-2-certified `lemmas/sigma-periodicity.md` had a buggy `T'` formula (it dropped a factor of `p` whenever a prime `p ≤ R` divides `T` but not `L`); the reviewer corrected it in place (round 3) to `T' = T · ∏_{p ≤ R, p ∤ L, p prime} p`. **This proof does not depend on sigma-periodicity** (it proves periodicity directly via similarity + CRT, Part IV, without invoking the `v_p`/sieve framework); the lemma is mentioned only as part of the (W)⟹(C)⟹B1' corollary in the "B1' subsumed" remark, where it is not load-bearing. So the round-2 bug and its correction do not affect this proof. (The corrected formula is internally consistent with this approach's threshold `k = a_1` if one replaces `R = rad(a_1)` there by `k = a_1` throughout, but no use is made of it.)

- **Empirical verifications performed (Python/sympy).** (i) Lemma 1 (characterization `G = H`) checked for `a_1 ∈ {6,9,15,35,77,91,105,135,175,187,221,385}`, `n ≤ 300`: 0 mismatches in every case. (ii) Similarity (uniform `G`-status within each small-prime signature) checked for `a_1 ∈ {15,35,77,91,105,135,175,187,221,385}`, `n ≤ 800`: 0 violations. (iii) **Lemma 2 (patched, with case-split)** checked for `a_1 ∈ {15,35,77,91,105,135,175,187,221,385}` on every greedy term (first 300): 0 failures, including the purely-smooth regime `a_1 ∈ {175, 221, 385}` (Case 1, `x = b`, carries everything) and the big-prime regime `a_1 ∈ {15, 35, 77, 91, 105, 135, 187}` (Case 2 when `b` has a big prime, Case 1 when `b` is `k`-smooth). (These checks confirm the lemmas but are not load-bearing — the proof stands on its own.)

## Promotable lemmas
- **s-substitution lemma** (Lemma 2 above): for every `b ≥ k = a_1` with a small (≤ a_1) prime factor, there is a `k`-smooth integer `x` similar to `b` with `k ≤ x ≤ b`. Proved in this file, Part II. (This is the R-smooth-stripping / aimo-0030 Claim-4 mechanism, proved from scratch; reusable by any approach needing a small-prime-only representative ≤ a given term.)
- **Similarity theorem** (Part III): two integers `≥ a_1` divisible by the same primes `≤ a_1` are either both in the greedy set `G` or both outside it. Proved in this file, Part III, via minimal counterexample + the s-substitution lemma + Lemma 1. (This *is* the periodicity theorem's crux; promoting it lets other approaches import it rather than re-deriving.)
- **Greedy-set characterization** (Lemma 1): `n ≥ a_1` lies in the greedy set `G` iff it is coprime to none of the smaller elements of `G`. Proved in this file, Part I. (The combinatorial replacement for the source crux's "good/bad" dichotomy; reusable foundation for any greedy-set argument.)
