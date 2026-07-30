# Approach: hitting-set-monovariant

## Status
unsolved (RETIRED, round 3 outline-reviewer). Reason: the distinctive mechanism — transversal-minimality / matching-duality / one-prime-swap descent — is a recorded dead end (one-prime swap fails; Hall/König inapplicable to hypergraph transversals; universal-small-prime necessary-not-sufficient, 1515/5000 counterexamples). All salvageable content (cross-intersecting closure lemma, definitional reduction, certified conditional spine) is ALREADY certified in `lemmas/` and imported by the live slugs `cross-intersecting-anchor`/`w-descent-rsmooth`. The slug name ("monovariant") is misleading — the monovariant was dropped in round 2. Frozen in the ranker; not in the build set. The certified lemmas remain importable.

## Approaches tried
- (round 1 seed) Skeleton with well-founded monovariant `(|M_n|, Σ|h|, #disjoint-pairs)` on the minimal-hitting-set family — unbuilt.
- (round 2, REVISED) Dropped the FALSE round-1 monovariant (verified non-monotone: `a_1=385` gives `|M|` rising 3→9 before falling, `#disjoint-pairs` rising 3→12 on step 1). Recast as the clean 7-step chain whose only crux is `M_n = M'_n` (= B1', "no large-prime shortcut"), stabilization then FREE by pigeonhole over the definitional finite universe `P_R={primes≤R}`. Proved in full: the definitional reduction, the cross-intersecting closure lemma (stress-tested, 0/1581 violations), finite-universe stabilization, seed-automaticity, and Theorem 1 import. Attempted the crux via **transversal-minimality / matching duality** (the `aimo-0030` IMO-SL 2013 "small-prime replacement + minimal-counterexample descent" analog); the descent does NOT close — the obstruction is exhibited by a counterexample scan (1515/5000 arbitrary small-prime-bearing hypergraphs have a minimal hitting set using ONLY large primes), confirming that "every row carries a small prime" is necessary but NOT sufficient. The crux `M_n=M'_n` and the secondary `B2` (from-`n=1`) remain as explicit [GAP]s. Outcome: partial — the whole theorem is reduced to the single clean claim B1' + B2, with all surrounding machinery rigorous.

## Current best
The furthest rigorous progress, all verified (Python/sympy) and stress-tested:

1. **Definitional reduction (proved).** `A_n = {m≥1 : gcd(m,a_i)>1 ∀i≤n} = ∪_{h∈M_n}{multiples of m_h}`, where `M_n` = minimal hitting sets of `F_n={supp(a_i):i≤n}` and `m_h=∏_{p∈h}p`. The greedy is `a_{n+1}=min(A_n∩(a_n,∞))`. This is an identity (every hitting set contains a minimal one by well-founded reduction).

2. **Small-prime reduction (proved).** Let `R=rad(a_1)`, `P_R={primes≤R}`, `σ_i=supp(a_i)∩P_R`, `F'_n={σ_i:i≤n}`, `M'_n` = minimal hitting sets of `F'_n` (⊆`2^{P_R}`, an automatically finite universe), `B_n=∪_{h∈M'_n}{mult of m_h}`, `L_n=∏_{p∈∪M'_n}p`. Always `M'_n⊆M_n` (hence `B_n⊆A_n`): a small-prime minimal hitting set `h` of `F'_n` hits every `σ_i⊆supp(a_i)`, hence every `supp(a_i)`, and is minimal for `{supp(a_i)}` because `supp(a_i)∩h = σ_i∩h` (h is small-only). The crux is the reverse inclusion.

3. **Cross-intersecting closure lemma (proved, stress-tested 0/1581).** If `M_n` is pairwise cross-intersecting then `M_{n+1}=M_n` (and inductively `M` is fixed forever), for ANY new support that is a hitting set of `F_n`. Unconditional (no B1' needed). Under B1' the same closure applies to `M'_n`.

4. **Finite-universe stabilization (proved, conditional on B1').** If `M_n=M'_n` for all `n`, then `F'_n` is a monotone-growing family over the fixed finite set `P_R`, so it stabilizes as a set at some `N` (pigeonhole: `|F'_n|≤2^{|P_R|}`); then `M'_n=:M'_∞` is fixed for `n≥N`, `B_n=:B` is fixed and `L`-periodic with `L=∏_{p∈∪M'_∞}p` (the KERNEL product — e.g. `30`, not `∏_{p≤15}p=30030`; verified `a_1=15,35,77,91,135,385`).

5. **Seed automaticity (proved, conditional on B1').** `a_N∈B`: `a_N` is admissible for `F'_{N-1}` (hits every earlier small support, trivially its own), and B1' makes admissible = small-prime-admissible, so `a_N` is a multiple of some `m_h`, `h∈M'_∞`. (This dissolves the old B1(b) seed sub-gap for free.)

6. **Theorem 1 (import, certified).** Once the greedy = cyclic successor `f_B` on the fixed `L`-periodic `B` from index `N`, `lemmas/periodic-set-iteration.md` gives `a_{n+T}=a_n+L` for all `n≥N`, `T=|B∩[0,L)|`, single cycle, no internal pre-period.

7. **Trivial cases (import, certified).** `a_1` even ⟹ `T=1,L=2`; `a_1=p^k` ⟹ `T=1,L=p`. Fully proved from `n=1` (round 1).

**The precisely-located open gaps:**

- **[GAP B1' — THE crux]** `M_n=M'_n` for all `n`, i.e. no minimal hitting set of the full supports ever uses a prime `q>R`. Attempted via transversal-minimality / matching duality (the `aimo-0030` descent analog); the descent breaks at a precise point (see Proof §4). This is the SAME wall as the round-1 B1 in cleaner combinatorial language (an equivalent reformulation, not a bypass — honestly flagged by the round-2 explorer and confirmed here).

- **[GAP B2 — secondary]** Extend periodicity from `n≥N` to `n≥1` (empty pre-period on the small lattice). Empirically empty for all tested `a_1`; mechanism not found.

Empirics (conjecture, not proof): `M_n=M'_n` holds at EVERY step (verified step-by-step `a_1=385`, and at `n=60` for `a_1∈{15,35,77,91,135,385}`); `S=∪M'_∞⊆{primes≤R}` universally; `M'_∞={{2,3},{2,5},{3,5}}` for `a_1=15` (`L=30,T=8`), `{{2,7},{2,11},{7,11}}` for `a_1=77` (`L=154,T=18`), `{{2,7},{2,13},{7,13}}` for `a_1=91` (`L=182,T=20`); the round-1 monovariant `(|M_n|,Σ|h|,#disjoint-pairs)` is NON-monotone (DROP it — `a_1=385`: `|M|` rises `3→9` before falling).

---

## Proof (partial — rigorous modulo [GAP B1'] and [GAP B2])

Throughout, `a_1>1` is fixed and the sequence is defined by
`a_{n+1}=min{m>a_n : gcd(m,a_i)>1 ∀ i=1,…,n}`.   (★)

Set `R:=rad(a_1)=∏_{p|a_1}p` and `P_R:={primes p : p≤R}`. For an integer `m` write `supp(m)={p prime : p|m}` and `σ(m):=supp(m)∩P_R` (the *small-prime support*).

### §1. Definitional reduction to minimal hitting sets

For `n≥1` let `F_n:={supp(a_i) : 1≤i≤n}` (a family of finite sets of primes). A *hitting set* of `F_n` is a set `H` of primes with `H∩supp(a_i)≠∅` for every `i≤n`. Let `M_n` be the family of **minimal** (by inclusion) hitting sets of `F_n`, and for `h∈M_n` put `m_h:=∏_{p∈h}p` (squarefree).

**Lemma 1 (admissible-set identity).** `A_n:={m≥1 : gcd(m,a_i)>1 ∀i≤n}=∪_{h∈M_n}{k·m_h : k≥1}`.

*Proof.* `m∈A_n` ⇔ `supp(m)∩supp(a_i)≠∅` for every `i≤n` ⇔ `supp(m)` is a hitting set of `F_n`. Every hitting set contains a minimal one (well-foundedness: the collection of hitting sets is nonempty — e.g. `∪_{i}supp(a_i)` — and inclusion-decreasing chains terminate since supports are finite), so `supp(m)⊇h` for some `h∈M_n`. Then `m_h | m` (as `h⊆supp(m)`), i.e. `m` is a multiple of `m_h`. Conversely every multiple of `m_h` (`h∈M_n`) hits every `a_i`. ∎

Hence (★) is `a_{n+1}=min(A_n∩(a_n,∞))=:f_{A_n}(a_n)`.

### §2. Certified imports

**Lemma 2 (bounded difference, `lemmas/bounded-difference.md`).** `a_{n+1}-a_n≤R` for all `n`. The witness `W_n:=R·⌈(a_n+1)/R⌉` (next multiple of `R` after `a_n`) lies in `(a_n,a_n+R]` and is admissible (it is divisible by every prime of `a_1`, and every past `a_i` shares a prime of `a_1` with it). Note `W_n` is *small-prime-only*: `supp(W_n)=supp(a_1)⊆P_R`.

**Lemma 3 (universal small prime, `lemmas/universal-small-prime.md`).** Every `a_n` (`n≥1`) is divisible by some prime of `a_1`, hence by a prime `≤R`. (For `n≥2`, `gcd(a_n,a_1)>1` since `a_1` is a past term.)

**Theorem 1 (cyclic successor on a periodic set, `lemmas/periodic-set-iteration.md`).** Let `B⊆ℤ` be nonempty and `L`-periodic (`B+L=B`), `R_B=B∩[0,L)={r_1<…<r_T}`. Then `f_B(x)=min(B∩(x,∞))` satisfies `x_{k+T}=x_k+L` for every `k≥0`, for any `x_0∈B` (single cycle, no pre-period).

**Trivial cases (round 1, certified).** `a_1` even ⟹ `T=1,L=2`; `a_1=p^k` ⟹ `T=1,L=p`. These are complete proofs from `n=1` and are not revisited below.

### §3. The small-prime lattice and the crux B1'

Let `F'_n:={σ(a_i):1≤i≤n}` (small-prime supports), let `M'_n` be the minimal hitting sets of `F'_n`, `B_n:=∪_{h∈M'_n}{k·m_h}`, and `L_n:=∏_{p∈∪M'_n}p`. Because `σ(a_i)⊆supp(a_i)` and every `h∈M'_n` is small-only:

**Lemma 4 (one-sided inclusion).** `M'_n⊆M_n` and `B_n⊆A_n` for every `n`.

*Proof.* Let `h∈M'_n`. Then `h` meets every `σ(a_i)`, hence every `supp(a_i)`: a hitting set of `F_n`. Minimality for `F_n`: for `p∈h`, minimality for `F'_n` gives `i` with `σ(a_i)∩(h\{p})=∅`; since `h⊆P_R`, `supp(a_i)∩(h\{p})=σ(a_i)∩(h\{p})=∅`, so `h\{p}` misses `supp(a_i)`. Hence `h` is minimal for `F_n`. So `M'_n⊆M_n`, giving `B_n⊆A_n`. ∎

The crux is the reverse inclusion. We isolate it as a single clean claim.

> **(B1')** For every `n≥1`, `M_n=M'_n` (equivalently: no minimal hitting set of the full supports `F_n` uses a prime `q>R`).

**Equivalence with the round-1 "no-free-rider-shortcut" wall.** `M_n=M'_n` ⇒ `A_n=B_n` (Lemma 1) ⇒ the greedy `a_{n+1}=min(B_n∩(a_n,∞))` equals the *small-prime greedy* ⇒ no candidate in `A_n\B_n` (a number that hits some past term only through a large prime) lies below `min(B_n∩(a_n,∞))` in the window `(a_n,a_n+R]`. Conversely, a free-rider shortcut in the window is exactly a minimal hitting set using a large prime (a minimal hitting set `g` with large `q` has a witness row `a_j` hit by `g` only through `q`, by minimality — the free-rider condition). So B1' is the round-1 crux B1(a) in transversal language. *(This is an equivalent reformulation, not a bypass — per the round-2 explorer's honest admission, confirmed here.)*

### §4. ATTEMPT: B1' via transversal-minimality / matching duality  [GAP]

The distinctive mechanism of this approach. We attempt to prove B1' by adapting the **`aimo-0030` (IMO-SL 2013) descent**: there, two "good" numbers sharing the same small-prime signature are shown to share a *small* prime by a minimal-counterexample descent that replaces big primes by a small-prime-only "representative" (Claim 4) and uses the game's coprimality to descend (Claim 5). We mirror this: the bounded-diff witness `W_n` is a small-prime-only admissible candidate (Lemma 2), so we attempt to show a large prime is never *essential* for minimality.

**Setup of the descent.** Suppose, for contradiction, that some `g∈M_n` contains a large prime `q>R`. By minimality of `g`, the prime `q` is *essential*: there exists a witness row `a_j` (`j≤n`) with
`supp(a_j)∩g={q}`  and  `q∈supp(a_j)`.
(Indeed, if every row met by `g` through `q` were also met through `g\{q}`, then `g\{q}` would still be a hitting set, contradicting minimality.) By Lemma 3, `a_j` carries a small prime `p_j|a_1`, `p_j≤R`. Since `supp(a_j)∩g={q}` and `p_j≤R<q`, we have `p_j∉g`. So:

> (*) the witness row `a_j` for the large prime `q∈g` carries a small prime `p_j|a_1` that is **not** in `g`.

**The natural repair and where it breaks.** To descend, one wants to replace `q` by `p_j` in `g`, forming `g^*=(g\{q})∪{p_j}`, and argue `g^*` is a smaller (smaller-product) hitting set — contradicting either minimality of `g` or the minimal-product choice. The obstruction: `g^*` need **not** be a hitting set. The rows that `g` hit *only* through `q` (the set `J_q:={i : supp(a_i)∩g={q}}`, which contains `j`) are hit by `g^*` only if `p_j` divides them — and there is no guarantee of that. A single large prime `q` may be the sole `g`-contact for several rows carrying *different* small primes; replacing `q` by any one `p_j` recovers only the row `a_j` and loses the others. So the one-prime swap fails, and unlike `aimo-0038` (where Claim 4 replaces **all** big primes at once by `p^n·(∏ small primes)`, landing a similar small-only number below the original), the hitting-set analogue of "replace all large primes simultaneously" has no canonical small-only target: the minimal small-prime hitting sets `M'_n` exist (Lemma 4: `M'_n≠∅` since `supp(a_1)⊆P_R` is a small hitting set), but they are not comparable to `g` by inclusion in general.

**Why matching/Hall–König duality does not close it either.** A minimal hitting set of a hypergraph is a *minimal transversal*, not a bipartite vertex cover; the clean Hall/König min-vertex-cover = max-matching identity applies to *graphs* (pairwise edges), not to arbitrary hypergraph transversals. Restricting to the bipartite rows×primes incidence graph, a hitting set is a set of prime-vertices dominating all row-vertices — a *set cover* / *transversal* of the hypergraph of supports, for which no min=max matching duality exists in general. So the duality bridge named in the outline does not supply B1'.

**The obstruction is real, not a failure of effort.** A counterexample scan confirms that the implication "every row carries a small prime ⟹ every minimal hitting set is small-only" is **false** for arbitrary hypergraphs: over 5000 random hypergraphs on `small={1,2,3,4}`, `large={5,6,7,8}` in which every row contains a small element, in 1515 cases some minimal hitting set used *only* large primes. Thus Lemma 3 (universal-small-prime) is *necessary* but **not sufficient** for B1'; the greedy's specific dynamics (the bounded-diff window, the admissibility structure) must enter, and we cannot extract a proof from transversal-minimality alone.

**What would close it.** A genuine new ingredient is required — e.g. the spacing+covering-bound attack of `small-prime-window-lemma` (which uses that a large prime `q>R` divides ≤1 integer of the window `(a_n,a_n+R]`, a *greedy-specific* fact absent from the bare hypergraph), or a `v_p`-cofinality count. The transversal-duality framing has reduced B1 to its cleanest equivalent form but does not itself prove it.

> **[GAP B1'].** `M_n=M'_n` for all `n` remains unproved. The transversal-minimality / matching-duality descent breaks at the one-prime-swap step (*); no small-only comparable target exists, and hypergraph transversal admits no Hall/König min=max duality. The claim is equivalent to the round-1 free-rider-shortcut wall. HONEST STATUS: open.

### §5. Stabilization, seed, periodicity — ALL conditional on B1'

Henceforth **assume B1'**. Then `M_n=M'_n` for all `n`, so `A_n=B_n` and the greedy is `a_{n+1}=min(B_n∩(a_n,∞))`.

**Lemma 5 (finite-universe stabilization).** `F'_n` stabilizes: ∃`N` with `F'_n=F'_N` for all `n≥N`. Consequently `M'_n=:M'_∞`, `B_n=:B`, and `L_n=:L=∏_{p∈∪M'_∞}p` are fixed for `n≥N`; `B` is `L`-periodic.

*Proof.* `F'_n` is a monotone-nondecreasing family of subsets of the fixed finite set `P_R` (Lemma 3: every `σ(a_i)⊆P_R`). Since `2^{P_R}` is finite (pigeonhole / extremal principle, KB "Pigeonhole"), the chain `F'_1⊆F'_2⊆…` stabilizes at some `N`. `M'_n` is a function of `F'_n` alone (it is the set of inclusion-minimal transversals of `F'_n`), so it is fixed for `n≥N`; hence `B` and `L` are fixed. `B` is `L`-periodic because membership `m∈B` depends only on divisibility by the primes in `∪M'_∞`, all of which divide `L`: `m∈B ⇔ m+L∈B`. `B≠∅` because `M'_∞≠∅` (Lemma 4; `supp(a_1)⊆P_R` is a small hitting set). ∎

*(The cross-intersecting closure lemma below gives a sharper EARLY freeze — `M` stabilizes as soon as it is cross-intersecting, often far before `F'` does — but it is not load-bearing; Lemma 5 is the backstop.)*

**Lemma 6 (cross-intersecting closure — proved, unconditional).** If `M_n` is pairwise cross-intersecting (`h∩h'≠∅` for all `h,h'∈M_n`) and `S_{n+1}:=supp(a_{n+1})` is a hitting set of `F_n`, then `M_{n+1}=M_n`. In particular (under B1') if `M'_n` is cross-intersecting then `M'_{n+1}=M'_n`, and `M` is fixed forever from `n`.

*Proof.* Since `S_{n+1}` is a hitting set of `F_n`, by well-foundedness `S_{n+1}⊇h_0` for some `h_0∈M_n`.

*Old sets persist.* Let `h'∈M_n`. `h'` is a hitting set of `F_n`; we check it hits the new row: `h'∩S_{n+1}⊇h'∩h_0≠∅` (cross-intersecting, `h_0⊆S_{n+1}`). So `h'` is a hitting set of `F_{n+1}=F_n∪{S_{n+1}}`. Minimality is preserved: any `h''⊂h'` fails some row of `F_n` (minimality of `h'` for `F_n`), hence fails it in `F_{n+1}`. So `h'∈M_{n+1}`; thus `M_n⊆M_{n+1}`.

*No new minimal hitting set.* Let `g∈M_{n+1}`. Then `g` is a hitting set of `F_{n+1}⊇F_n`, hence of `F_n`; by well-foundedness `g⊇h_g` for some `h_g∈M_n`. Cross-intersecting gives `h_g∩h_0≠∅`, and `h_0⊆S_{n+1}`, so `h_g∩S_{n+1}≠∅`: `h_g` hits the new row. Since `h_g` hits all of `F_n`, it hits all of `F_{n+1}`; so `h_g` is a hitting set of `F_{n+1}` with `h_g⊆g`. Minimality of `g` for `F_{n+1}` forces `h_g=g`, i.e. `g=h_g∈M_n`. So `M_{n+1}⊆M_n`.

Hence `M_{n+1}=M_n`. ∎ (Stress-tested: 0 violations in 1581 random cross-intersecting families with an added hitting-set row.)

Under B1', `M_n=M'_n`; the new row's small support `σ(a_{n+1})⊇h_0∈M'_n` (since `a_{n+1}∈B_n` by the greedy), so the lemma applies to `M'_n` verbatim. Empirically `M` freezes at the first cross-intersecting stage (`n=3` for `a_1=15`, `n=38` for `a_1=385`), far earlier than `F'_n` stabilizes as a set — but either mechanism suffices.

**Lemma 7 (seed automaticity).** Under B1', `a_N∈B`.

*Proof.* `a_N` is admissible for `{a_1,…,a_{N-1}}` (it hits every earlier term by (★)); by B1' admissibility equals small-prime-admissibility, so `σ(a_N)` hits `F'_{N-1}=F'_∞` (stabilized). Hence `σ(a_N)⊇h` for some `h∈M'_∞` (well-foundedness), so `m_h|a_N`, i.e. `a_N∈B`. (This dissolves the round-1 B1(b) seed sub-gap.) ∎

**Theorem (periodicity from `N`).** Under B1', `a_{n+T}=a_n+L` for all `n≥N`, where `T=|B∩[0,L)|`, `L=∏_{p∈∪M'_∞}p`.

*Proof.* By Lemmas 5,7 the greedy is `a_{n+1}=f_B(a_n)=min(B∩(a_n,∞))` on the fixed `L`-periodic nonempty set `B`, with `a_N∈B`. Theorem 1 (import, §2) gives `a_{N+k+T}=a_{N+k}+L` for all `k≥0`, i.e. `a_{n+T}=a_n+L` for `n≥N`. ∎

### §6. B2 — from `n=1`  [GAP]

Theorem 1 gives periodicity from `n=N`. The problem requires `n≥1`. The pre-period is empty in every tested case (`a_1∈{15,35,77,91,105,135,175,187,221,385}` all satisfy `a_{1+T}=a_1+L`), but:

> **[GAP B2].** For `n<N`, no "prematurely valid" candidate `m∈(a_n,f_B(a_n))` (admissible for the still-growing `B_n`, hence valid for the greedy, but failing some future constraint that `B` encodes) steals the greedy. The single-cycle structure of Theorem 1 removes any *internal* pre-period once the orbit lies in `B`, but does not by itself force the early terms `a_1,…,a_{N-1}` to lie on the same cycle: one would need `a_n∈B` and `a_{n+1}=f_B(a_n)` for `n<N` too, i.e. that `M'_n` already equals `M'_∞` "enough" for the greedy's choice — which is stronger than the finite-universe stabilization Lemma 5 supplies. No proof found. (Free in the trivial cases `a_1` even / `a_1=p^k`, where `N=1`.)

### §7. Summary of the reduction

Granting B1' and B2, the proof is complete: B1' + Lemma 5 ⇒ fixed `L`-periodic `B` + seed `a_N∈B` (Lemma 7) ⇒ Theorem 1 ⇒ `a_{n+T}=a_n+L` from `n=N`; B2 ⇒ from `n=1`. The whole problem is reduced to the **single** combinatorial claim B1' (`M_n=M'_n`, "no large prime is ever essential for a minimal transversal") plus the secondary B2. The transversal-minimality / matching-duality mechanism formulates B1' cleanly and exhibits precisely where it breaks (§4), but does not close it; the genuine lever must come from a greedy-specific ingredient (spacing or `v_p`-cofinality), not from bare hypergraph transversal theory.

## Promotable lemmas
- **Cross-intersecting closure lemma** — statement: *if `M_n` (minimal hitting sets of `F_n`) is pairwise cross-intersecting and the new row's support is a hitting set of `F_n`, then `M_{n+1}=M_n`*; proved in §5/Lemma 6 above, stress-tested (0/1581). Reusable by any hitting-set-based approach to `imo-2026-06` (and by the small-prime version under B1'). Candidate file: `results/imo-2026-06/lemmas/cross-intersecting-closure.md`.
- **Small-prime one-sided inclusion** — statement: *`M'_n⊆M_n` and `B_n⊆A_n` always*; proved in §3/Lemma 4. Reusable; candidate file `results/imo-2026-06/lemmas/small-prime-inclusion.md`. (Smaller; the closure lemma is the principal promotable result.)
