## imo-2026-06 — route: finite-prime-cover / support-stabilization

### TL;DR — the route as literally tasked does NOT work; here is the reformulation that does

The task's sub-claims 1 (only finitely many primes divide any `a_n`) and 2 (the support pattern `supp(a_n)` is eventually periodic) are **FALSE as stated**. They must be replaced by stabilization of the *minimal-hitting-set family*. The correct crux is: the family of minimal hitting sets of `{supp(a_i): i≤n}` eventually stabilizes, after which the greedy is deterministic on a fixed finite union of arithmetic progressions and is periodic mod `L`.

### Evidence (numerical, conjecture-grade)

- `a1=15=3·5`: terms stabilize to residues `{0,6,10,12,15,18,20,24} mod 30`. `T=8, L=30=2·3·5`. The 8 residues are exactly the `m mod 30` divisible by one of `6,10,15` (= products of the 2-subsets of `{2,3,5}`). Minimal-hitting-set family `M = {{2,3},{2,5},{3,5}}` (all 2-subsets), pairwise intersecting. ✓
- `a1=77=7·11`: `T=18, L=154=2·7·11`. Residues mod 154 are exactly the multiples of `14`, `22`, or `77` (products of 2-subsets of `{2,7,11}`). Same shape: `M = all 2-subsets of a 3-prime set`.
- `a1=35=5·7`: `T=34, L=210=2·3·5·7`. `M = all 3-subsets of {2,3,5,7}` (products `30,42,70,105`, lcm 210). ✓
- `a1=21=3·7`: **collapses** to `a_n = 3(n+6)`, `T=1, L=3`. Here `M` collapses to the singleton `{{3}}` once the greedy hits `a_3 = 27 = 3^3` (a pure prime power of an `a_1`-prime).
- `a1=p` prime / `p^k`: `a_n = n·p`, arithmetic, `M={{p}}`.

So the value of `L` (the eventual translation) is always the **product of the primes in the stabilized active set `P = ∪M`**, and `T = |{r ∈ [0,L) : m_h | r for some h ∈ M}|`.

### Why sub-claims 1 & 2 are false (must be reformulated)

For `a1=15`, the stabilized subsequence at residue `0 mod 30` is `30, 60, 90, …, 30k, …` with `k=1,2,3,…` — so `a_n = 30k` for infinitely many `n`, and `supp(30k)` ranges over every prime as `k` varies. Thus:
- the set of primes dividing *some* `a_n` is **infinite** (every prime `q` divides `30q`);
- `supp(a_n)` is **not** eventually periodic (`supp(30k)` depends on `k`'s factorization).

The right object is *not* `supp(a_n)` but **`supp(a_n) ∩ P`** (the support restricted to the active prime set `P`), or equivalently the family of minimal hitting sets `M_n`. Primes outside `P` (like `7` in `42=2·3·7`, or `61` in `732=4·3·61`) enter values of `a_n` but never enter `M` — they are "incidental" and do not constrain the future.

### The chain of lemmas (reformulated route)

**Lemma A — `A_n` is always a finite union of APs.** Let `M_n` = minimal hitting sets of `F_n = {supp(a_i): i≤n}`. Each `h ∈ M_n` is a subset of primes; let `m_h = ∏_{p∈h} p`. Then the allowed set `A_n = {m : supp(m) hits every supp(a_i), i≤n} = ∪_{h∈M_n} {multiples of m_h}`. *Why plausible*: definition of hitting set + every hitting set contains a minimal one (well-founded reduction). *Gap*: none — this is a definition. *Tools*: none.

**Lemma B (THE CRUX) — `M_n` stabilizes.** There exist `N`, a finite active prime set `P`, and a fixed family `M` such that for all `n ≥ N`, `M_n = M` and every prime of `supp(a_n)` that lies in `M` is from `P` (equivalently: no new prime enters `M` after `N`). *Why plausible*: numerics; plus the self-sustaining observation below. *Gap (the hard step)*: see "Crux" below. *Tools*: Bertrand / size-bounding (to bound the size of a prime that can newly enter `M`), pigeonhole on the finite state `M_n`, minimality of the greedy.

**Lemma C — self-sustaining closure.** If at some step `M_n` is **pairwise cross-intersecting** (every `h, h' ∈ M_n` satisfy `h ∩ h' ≠ ∅`) then `M` is stable forever after: every future term `a_{n+1}` is a hitting set, so its support contains some `h ∈ M`; because `h` meets every `h' ∈ M`, the new support intersects every `h'`, so adding it removes no `h'` and (by the reduction argument) introduces no new minimal hitting set. *Why plausible*: clean combinatorial argument; matches the data (`a1=15,77,35` all land in a pairwise-cross-intersecting `M` and stay). *Gap*: showing `M_n` always *reaches* a pairwise-cross-intersecting (or otherwise self-sustaining) state in finite time. *Tools*: minimality, a well-founded measure on `M_n`.

**Lemma D — from stable `M` to `a_{n+T}=a_n+L`.** Once `M_n = M` for `n ≥ N`, `A_n = A` is fixed. Let `L = lcm{m_h : h ∈ M} = ∏_{p ∈ P} p`. The allowed residues `R = {r ∈ [0,L) : m_h | r for some h ∈ M}` are finite. The greedy picks `a_{n+1} =` smallest `> a_n` with residue in `R mod L`; this cycles through `R` in increasing cyclic order, so `a_{n+T} = a_n + L` with `T = |R|`. *Why plausible*: deterministic greedy on a periodic target set; numerics confirm `T=|R|`, `L=∏P`. *Gap*: proving the greedy strictly cycles (no "skips" — follows from `a_n ∈ A` and `A` periodic, plus monotone growth `a_{n+1} > a_n`, the next element of `A` after `a_n` is `a_n` plus the gap to the next residue in `R`). *Tools*: CRT (to see `A` is a union of residue classes mod `L`), order-of-element / periodicity.

### The crux — Lemma B (stabilization of `M_n`)

This is the single hardest step. The mechanism that *could* destabilize: a term `a_{n+1}` whose support **misses** some current `h ∈ M_n`. Then `h` stops hitting the new family, is removed, and replacements `h ∪ {s}` (`s ∈ supp(a_{n+1})`) become new minimal hitting sets — potentially introducing a **new prime** into `M`.

Two sub-gaps the outliner must close:

- **(B1) Size bound on entering primes.** If a new prime `q ∉ P` enters `M` at step `n+1`, then the greedy *preferred* a number using `q` over the next multiple of an old `m_h`. The next multiple of `m_h` after `a_n` is at most `a_n + m_h ≤ a_n + ∏P`. So `q ≤ a_{n+1} ≤ a_n + ∏P`. *This alone does not bound `q` absolutely* (it grows with `a_n`), so a naive size argument is insufficient — the outliner needs a sharper measure (e.g. argue `q` entering forces `q ≤ ∏P` via a Bertrand-style comparison, or via the fact that `a_{n+1}` must also be a multiple of `m_h` for some `h`, pinning `q | m_h · k` for small `k`). **This is the technical heart.**
- **(B2) Termination of the `M_n`-evolution.** Each destabilizing event strictly *enlarges* some minimal hitting set (`h → h ∪ {s}`), so `|h|` increases. Need a well-founded monotone quantity that can only increase finitely often — candidate: `∑_{h∈M_n} |h|`, or the tuple `(min |h|, # of size-minimal h's, …)` lexicographically. But `|h| ≤ |P_n|` and `P_n` can grow, so the measure must also bound `|P_n|` — which loops back to (B1).

### Three distinct ways to complete the chain

1. **Pairwise-cross-intersecting closure (cleanest).** Prove `M_n` reaches a pairwise-cross-intersecting family in finite time (via a measure that increases at each non-closed step and is bounded once (B1) caps `|P|`), then invoke Lemma C. This is the path most supported by data (`a1=15,35,77` all land here).
2. **Singleton collapse (the other observed attractor).** Show that *either* `M` reaches pairwise-cross-intersecting closure, *or* it collapses to a singleton `{{p}}` (a prime `p | a_1` survives as the unique minimal hitting set forever, giving arithmetic diff `p`). Prove no third behavior is possible (e.g. every non-closed, non-collapsed `M_n` admits a strictly-decreasing measure). `a1=21,6,prime,prime-power` exercise this branch.
3. **Compactness / eventual-periodicity-mod-`M` (avoid bounding `|P|` directly).** Instead of proving `|P|` finite, prove directly that the *residue class of `a_n` mod `L_n`* (for a cleverly chosen increasing sequence of moduli `L_n = ∏(primes seen so far)`) is eventually stable, using a König's-lemma / compactness argument on the tree of residue histories. This sidesteps (B1) but needs careful construction of `L_n` and is closer to a different route (the modular-state route) — flagged here for the outliner.

### Candidate knowledge-base entries to cite

- **Modular arithmetic, CRT** (KB §Number Theory) — Lemma D: `A` is a union of residue classes mod `L`; combine via CRT.
- **Order of an element, Fermat/Euler** (KB) — supports the periodicity claim of Lemma D (greedy on a periodic set).
- **Bertrand's postulate** (KB) — Lemma B1: bound a newly-entering prime by comparing `q` against the next multiple of `∏P`; force a prime factor into a dyadic interval.
- **Divisor analysis / consecutive-integer coprimality** (KB) — `gcd(k,k+1)=1` style arguments appear when comparing two consecutive candidate terms.
- **Pigeonhole** (KB §combinatorics-flavored) — Lemma B: `M_n` ranges over a finite poset once `|P|` is bounded; pigeonhole forces repetition ⇒ stabilization.
- **Invariants and monovariants** (KB) — Lemma B2: a well-founded measure on `M_n` (e.g. `∑|h|`).
- **Size-bounding and descent** (KB §number_theory) — Lemma B1.

### Analogous past problems (cruxes)

- **aimo-0727** (`divisibility-and-gcd`): *"bounded multiplier would confine all prime factors of the sequence to a finite set, contradicting infinitely many prime divisors"* — the **reverse** direction (it forces *unboundedness* by contradicting a finite-prime-set conclusion). Useful as the test for what a finiteness argument must avoid. Adapt with caution.
- **aimo-0212** (`divisibility-and-gcd`): *"every prime dividing a polynomial's values lies in a fixed finite set, then a polynomial with finitely many prime divisors must be constant"* — closest in spirit to the *finite-prime-set stabilization* move, though for a different conclusion (constancy). The technique of "trap every prime divisor into a fixed finite set via a divisibility relation" is the analogy for Lemma B.
- **aimo-0628** (`modular-arithmetic-and-CRT`): *"partition by residue mod `p`, flag sparse classes, swap a member for another in the same residue class preserving the structure"* — the residue-class-swap idea echoes Lemma D's "cycle through `R` mod `L`" and is the closest crux to the periodic-value step.
- No crux in the corpus is a direct match (this problem's "greedy smallest-with-gcd-condition → eventually periodic-up-to-translation" structure is not in the pre-2026 NT corpus that I could find). Do not force a wrong match.

### Prior progress

- None. Workspace `results/imo-2026-06/` is empty (no approaches, no lemmas, no `current.md`). This is round 1.

### Dead ends (do not retry)

- None yet (round 1). But flag for the outliner: **do NOT pursue "the set of primes dividing the terms is finite" or "the support pattern `supp(a_n)` is eventually periodic"** — both are refuted by the `a1=15` data (the `30k` subsequence accumulates every prime). The unit of analysis is `supp(a_n) ∩ P` / the minimal-hitting-set family `M_n`, never the full support.

### Small-case / intuition notes (all conjecture, labeled)

- **Conjecture (stabilized shape):** `M` always lands as either a singleton `{{p}}` (giving arithmetic diff `p`, `T=1`) or the family of all `(k-1)`-subsets of a `k`-prime set `P` (pairwise cross-intersecting when `k≥3`), giving `L = ∏P`, `T = |R|`. The two attractors are observed (`a1=21,6,p` → singleton; `a1=15,35,77` → `(k−1)`-subsets). Whether these are the *only* possible stabilized shapes is open — the outliner need not prove this classification; Lemma B + C + D suffice.
- **Conjecture (active primes come from early terms):** every prime in the stabilized `P` divides one of the first few `a_i` (in all examples, `P ⊆ supp(a_1) ∪ supp(a_2) ∪ supp(a_3)`). If true, this trivializes (B1) (gives an absolute `|P|` bound up front). Worth the outliner attempting, but unproved.
- **Conjecture (L = ∏P):** confirmed in all computed examples; the translation is the product of active primes, and `T = |R|` where `R = {r mod L : m_h | r for some h}`. Verify by construction once `M` is known.

### Distinct openings surfaced (for the outliner's rival approaches)

1. Hit the crux Lemma B head-on via a **well-founded monovariant on `M_n`** (`∑|h|` or lex tuple), pairing with a **Bertrand size-bound** (B1) to cap `|P|`.
2. Reduce Lemma B to **pairwise-cross-intersecting closure** (Lemma C) and prove *only* that `M_n` reaches such a state — a cleaner combinatorial target than bounding `|P|` directly.
3. **Sidestep (B1)** with a **compactness / König's-lemma** argument on residue histories mod a growing modulus — avoids ever proving `|P|` finite explicitly (closest to a modular-state route, but reachable from the prime-cover framing).
4. **Two-attractor case split**: prove `M_n` ends in either singleton-collapse or `(k−1)`-subset closure, handling each branch separately (the singleton branch is nearly trivial; the closure branch is Lemma C).
