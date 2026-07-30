# Approach: cut-sequence-potential (amortized monovariant over Xiang's ordered cuts)

## Status
partial

Framework and the exact per‑cut toggle geometry are rigorous (rest on certified lemmas).
The one hard step — an **explicit** amortized reserve `r_k` making `Φ_k = D̃_k − 1 − r_k`
a genuine monovariant — is NOT closed. This round proves a **structural Equivalence Theorem**
that pins down exactly why: the existence of *any* admissible reserve (magnitude‑based or
geometric) is **logically equivalent to the target inequality itself**, so the sequential
framing provides no independent leverage unless one can *guess an explicit geometric reserve*
(a root‑tight, one‑cut‑verifiable upper bound on the maximal remaining drop). No such explicit
formula was found; the natural candidates are ruled out (numerically and structurally). This is
the early RETHINK signal the outline‑reviewer asked for, with the precise reason.

## Approaches tried
- **cut-sequence-potential (this round, R8)** — Set up the amortized framework over Xiang's
  ordered cut sequence using the *exact* Cut‑Flip toggle set (not just its measure). Proved the
  base value `D̃(F_0) = (2^{n+1}+(−1)^n)/3 ≥ 1`, and the exact per‑cut law
  `ΔD̃ = λ(S) − 2λ(S∩O)`, `S = [0,x)∪[L−x,L)`. Then proved an **Equivalence Theorem**: an
  admissible reserve exists **iff** `D̃(F)≥1` holds — the monovariant is not easier than the
  problem. Numerically ruled out coarse reserves (depend only on `(D̃,b)`) and linear/summed‑
  magnitude reserves (the refuted budget‑count). **Outcome: partial; RETHINK‑leaning** — the
  reserve does NOT collapse to summed‑magnitude (the guardrail's failure mode was avoided), but a
  provable *geometric* reserve is provably no weaker than the theorem, so no leverage was gained.

## Current best

### 0. Setup (all certified; imported, not re‑proved)

Work in **integer units** (rescale Liu's dyadic partition by `1/u_n`, `u_n=1/(2^{n+1}−1)`):
Liu plays `F_0 = {1,2,4,…,2^n}` (sum `2^{n+1}−1`). For a finite multiset of positive parts `P`,
let `N_P(t) = #{parts > t}` and `O(P) = {t>0 : N_P(t)\text{ odd}}`. By the **Level‑Measure
identity** (`lemmas/greedy-claim.md`) the discrepancy is
`D̃(P) = b_1−b_2+b_3−⋯ = λ(O(P))` (sorted descending). The target (GAP L, Case B) is:

> **(T)** For every response of Xiang using `≤ n` cuts applied to `F_0`, the final multiset `F`
> satisfies `D̃(F) ≥ 1`. (Equality is attained, e.g. `n=4`, `Y=(8,3,3,2)`, `Z=(8,2,2,2,1)`, so
> (T) is **non‑strict**.)

**Base value (direct computation).** `D̃(F_0) = 2^n − 2^{n-1} + ⋯ ± 1 = (2^{n+1}+(−1)^n)/3`.
Verified `n=1..5`: `1, 3, 5, 11, 21` (script `/tmp/exp1.py`, matches `λ(O)`). For `n≥1`,
`(2^{n+1}+(−1)^n)/3 ≥ 1` (equality only at `n=1`). So the process starts at or above `1`.

**Exact per‑cut law (Cut‑Flip geometry, certified `lemmas/cut-flip.md`).** Replacing a part of
length `L` by `(x, L−x)` with `0<x≤L−x` toggles the parity of `N(t)` **exactly** on the toggle
set `S = [0,x) ∪ [L−x, L)` (`λ(S)=2x=2·min(x,L−x)`), and nowhere else. Hence the new odd
indicator is the old one XOR `1_S`, so

> **(∗) ΔD̃ = λ(S) − 2·λ(S ∩ O)** ,  giving  `−2·min(x,L−x) ≤ ΔD̃ ≤ 2·min(x,L−x)`.

The **drop** produced by a cut is `−ΔD̃ = 2λ(S∩O) − λ(S)`. This is the *exact* geometry: a cut
can only lower `D̃` by twice the odd‑measure it overlaps, minus its own width — it is not a bare
magnitude. (This is the toggle‑set geometry the hard‑gate demanded we use, not `Σ|ΔD̃|`.)

### 1. The amortized program (as set up by the outline)

Process Xiang's `k≤n` cuts one at a time, `F_0→F_1→⋯→F_k=F`. Track the remaining budget
`b = n − (\text{cuts so far})`, so cut `j` takes `(F_{j-1}, b) → (F_j, b−1)`. Seek a **reserve**
`r_k = R(F_k, n−k)` and set `Φ_k = D̃(F_k) − 1 − R(F_k, n−k)`, aiming for `ΔΦ ≥ 0` at every cut
plus boundary pins, so that `D̃(F)−1 = Φ_k ≥ Φ_0 ≥ 0`.

Unwinding, the required properties of `R : (\text{config},\,\text{budget}) → ℝ_{≥0}` are:

- **(R0)** `R(P,0) = 0` (no cuts left ⇒ no further drop to reserve);
- **(R1)** for every config `P`, budget `b≥1`, and legal single cut `P→P'`:
  `R(P,b) − R(P',b−1) ≥ D̃(P) − D̃(P')` (= the drop; i.e. the cut's drop is charged against
  reserve released by that same cut);
- **(R2)** `R(F_0,n) ≤ D̃(F_0) − 1` (so `Φ_0 = D̃(F_0)−1−R(F_0,n) ≥ 0`);
- **(R3)** `R ≥ 0`.

Call such an `R` **admissible**. If an admissible `R` exists, then along any `≤n`‑cut sequence,
telescoping (R1) gives `R(F_0,n) ≥ (D̃(F_0) − D̃(F_k)) + R(F_k,n−k)`; with (R2),(R3),
`D̃(F_k) ≥ D̃(F_0) − R(F_0,n) ≥ 1`. So **admissible `R` ⇒ (T)**. This is the whole content of
the approach: *produce an admissible `R`.*

### 2. Equivalence Theorem (proved this round — the honest core result)

> **Theorem (Reserve⇔Target).** Fix `n`. An admissible reserve `R` (satisfying (R0)–(R3) over
> all configs reachable from `F_0` by `≤n` cuts) **exists if and only if the target (T) holds.**

**Proof.**

*(⇐) (T) ⇒ admissible `R` exists.* Define the **value‑function reserve**
`R^*(P,b) := D̃(P) − \mathrm{minreach}(P,b)`, where
`\mathrm{minreach}(P,b) := \min\{\,D̃(Q) : Q \text{ reachable from } P \text{ by } ≤b \text{ cuts}\}`.
- (R0): with `b=0` the only `Q` is `P`, so `R^*(P,0)=0`.
- (R3): `\mathrm{minreach}(P,b) ≤ D̃(P)` (take `0` cuts), so `R^* ≥ 0`.
- (R1): `\mathrm{minreach}(P,b) = \min\big(D̃(P),\ \min_{P→P'}\mathrm{minreach}(P',b−1)\big)`,
  so for any specific cut `P→P'`, `\mathrm{minreach}(P,b) ≤ \mathrm{minreach}(P',b−1)`. Then
  `R^*(P,b)−R^*(P',b−1) = [D̃(P)−D̃(P')] + [\mathrm{minreach}(P',b−1)−\mathrm{minreach}(P,b)]
  ≥ D̃(P)−D̃(P')`.
- (R2): `\mathrm{minreach}(F_0,n) ≥ 1` is exactly (T); hence `R^*(F_0,n)=D̃(F_0)−\mathrm{minreach}(F_0,n) ≤ D̃(F_0)−1`.

So `R^*` is admissible. (One‑cut inequality (R1) verified numerically with 0 violations over 200
random cut/budget instances at `n=4`, `/tmp/exp5.py`.)

*(⇒) admissible `R` exists ⇒ (T).* Immediate from §1's telescoping argument. ∎

**Consequence.** The amortized monovariant is *logically equivalent* to the theorem it is meant
to prove. It carries **no independent deductive leverage**: the only admissible reserves are
exactly the functions dominating the maximal‑remaining‑drop and tight at the root
(`R(F_0,n) = D̃(F_0)−1 = R^*(F_0,n)` forced by (R2) plus (R1)‑telescoping). The value‑function
reserve `R^*` is admissible but **vacuous** (it *is* `minreach`, so writing "Φ non‑decreasing"
just restates `\mathrm{minreach}(F_0,n)≥1`). The *only* way the program yields a genuine proof is
to exhibit a **different, explicit closed‑form geometric `R`** whose one‑cut inequality (R1) is
provable *locally* (config‑to‑single‑cut‑child) — a strictly stronger deliverable than merely
"having a monovariant."

### 3. Why the explicit reserve resists (the open gap, with evidence)

An admissible explicit `R` must be a **root‑tight upper bound on the maximal remaining drop**
`R^*(P,b)`. The geometry of `R^*` was probed to see if any tractable formula fits:

1. **Coarse reserves fail.** `R^*(P,b)` is *not* a function of `(D̃(P),b)` alone: at `n=4`,
   configs with the same `(D̃,b)=(11,1)` have `R^* ∈ {6,7,8}`; `(9,1)` gives `{2,4,6}`;
   `(11,2)` gives `{8,9,10}` (`/tmp/exp3.py`, 9 of 48 `(D̃,b)`‑classes are split). So an
   admissible `R` **must read the full toggle‑set geometry** of `P`, not just its discrepancy.

2. **Summed‑magnitude / linear‑in‑budget reserves fail (the refuted budget‑count).** From `F_0`
   the maximal remaining drop `R^*(F_0,b)` is **strictly concave/saturating**, not `b·(const)`
   (`/tmp/exp4.py`):
   - `n=2`: `R^*(F_0,b) = 0,2,2` (increments `2,0`);
   - `n=3`: `0,2,4,4` (increments `2,2,0`);
   - `n=4`: `0,6,8,10,10` (increments `6,2,2,0`).
   A cut can drop `D̃` by a large amount early (`6` at `n=4`, from bisecting the top part) but
   only `2` per cut thereafter — so no `Σ 2·\min(x,L−x)`‑type bound is tight at the root, and any
   magnitude bound over‑counts wildly. This is *exactly* the collapse the hard‑gate warned about,
   and it is confirmed dead. (Optimal descent `n=4`: `11→5→3→1`, i.e. `D̃(F_0^{(n)})→
   D̃(F_0^{(n-1)})→⋯→1`.)

3. **No closed form for the max single‑cut drop.** The max single‑cut drop from `P` is
   `\max_{L,\,x}\big(2λ(S(x)∩O(P)) − 2x\big)` over the exact toggle set `S(x)=[0,x)∪[L−x,L)`. For
   `F_0` (`n=4`, `O=(0,1)∪(2,4)∪(8,16)`) the optimum is bisecting the top part
   (`drop = 2λ(O∩[0,16)) − 16 = 22−16 = 6`); but which part/where is optimal changes with the
   full interval structure of `O`, and the *iterated* optimum `R^*(P,b)` inherits this. No
   telescoping closed form was found, consistent with §2: any such form would be a root‑tight
   bound on `R^*`, i.e. as strong as (T).

**Net.** The reserve does **not** collapse to a summed magnitude (we used the exact geometry, and
magnitude bounds are provably too loose here). But the geometry‑based reserve is, by the
Equivalence Theorem, **no weaker than the theorem**; and every tractable explicit candidate
(coarse, linear, single‑cut‑closed‑form) is ruled out. So the sequential‑cut framing, as an
*independent* engine, does not reduce the difficulty of GAP L.

### 4. Honest verdict / RETHINK signal

Per the outline‑reviewer's early‑RETHINK gate: this slug's reserve did **not** collapse into the
refuted summed‑magnitude budget‑count (that failure mode is explicitly excluded — see §3.2). It
failed for a **deeper, structural** reason: the Equivalence Theorem shows the amortized
monovariant is logically equivalent to (T), so unless one *guesses* an explicit geometric reserve
(a root‑tight, locally verifiable upper bound on `minreach`‑drop), the framing yields no proof.
No such explicit reserve was found this round, and the three natural families are dead.

Recommendation to the orchestrator: treat **cut-sequence-potential as RETHINK / low‑priority**.
The Equivalence Theorem (§2) also retroactively explains why the retired `induction-recursion`
(a sequential budget‑count) died: *the entire sequential‑count family is logically equivalent to
(T)* and cannot be easier. Concentrate the field on the two framings that route through a
*different object* than the cut sequence — `induction-recursion-telescope` (merged‑order
block‑tiling of `Σψ(c_i)Δw_i ≥ 0`) and `even-rank-doublecount` (static `E(F)≤2^n−1`). If both of
those also stall, the Equivalence Theorem is the signal to open a genuinely new framing (e.g. an
LP/entropy relaxation of `E(F)≤2^n−1`), not another sequential monovariant.

## Full proof
Not present — Status is `partial`. The framework (§0), the amortized reduction (§1), and the
Equivalence Theorem (§2) are rigorous; the load‑bearing explicit reserve (§3) is the open gap,
and §2 shows it is exactly as hard as GAP L itself.

## Promotable lemmas

**Reserve⇔Target Equivalence Theorem** (proved in full, §2 above; numerically corroborated
`/tmp/exp5.py`, 0/200 one‑cut violations of the value‑function reserve).
*Statement.* For the dyadic root `F_0={1,…,2^n}` and cuts as above, an admissible reserve
`R` — i.e. `R≥0`, `R(·,0)=0`, `R(F_0,n)≤D̃(F_0)−1`, and the one‑cut charging inequality
`R(P,b)−R(P',b−1) ≥ D̃(P)−D̃(P')` for every legal cut `P→P'` — **exists if and only if** the
GAP‑L target `D̃(F)≥1` holds for every `≤n`‑cut response. In particular the value‑function reserve
`R^*(P,b)=D̃(P)−\mathrm{minreach}(P,b)` is the (vacuous) canonical admissible reserve, and any
admissible reserve is forced to be root‑tight, `R(F_0,n)=D̃(F_0)−1`.
*Why reusable / worth certifying.* It rigorously establishes that **no amortized monovariant over
Xiang's cut sequence (magnitude‑ or geometry‑based) can be strictly easier than GAP L**, which
prunes an entire family of future attempts (the sequential‑count/potential family, incl. the
already‑retired `induction-recursion`). This is a general obstruction, not specific to a
candidate reserve.
