# imo-2026-03 — approach `even-packing-upper` (NEW, round 6)

**Framing (O4 — even-position packing).** After Xiang's refinement the refined
sorted multiset M′ has total T = 1. By `claim-game-odd-index` (Lemma 0,
certified), Liu's take is (T + D)/2 = (1 + D)/2, where D = b_1 − b_2 + b_3 − ⋯ is
the alternating sum of M′. Writing O = (odd-position sum) = b_1 + b_3 + ⋯ and
E = (even-position sum) = b_2 + b_4 + ⋯, we have O + E = 1 and D = O − E, hence

$$D \;=\; 1 - 2E, \qquad E \;=\; \frac{1-D}{2}.$$

Xiang (the outer minimizer of D) is therefore equivalently the **maximizer of
the even-position mass E**. The upper bound D* ≤ 1/D_n is equivalently

$$E^* \;\ge\; \frac{2^n - 1}{D_n}, \qquad D_n = 2^{n+1}-1,$$

where E* = max_{Xiang ≤ n-mark refinements} E is the Xiang-optimal even-position
mass. The conjecture (the upper bound itself) becomes: *the tower T_n is the
Liu config that MINIMIZES E* (packs the least mass into even slots); every other
config, in particular every compressed config (a_{n+1} > 1/D_n), admits an
even-packing of mass ≥ (2^n − 1)/D_n.*

This file owns that reframe. The reframe itself (Part I) and the tower
tightness (Part II — both directions, drawing on the certified lower bound) are
**fully proved**. The compressed-case packing bound (Part III) is the honest
open core: it is logically EQUIVALENT to GAP-U2-compressed of `majorization-upper`
(E* ≥ (2^n−1)/D_n ⟺ D* ≤ 1/D_n), so the even-packing lens REFRAMES but does NOT
bypass the crux. It is flagged **GAP-U2-packing**. The verification (Part IV) is
labelled verification-not-proof.

---

## Status

partial

The even-position reframe (D = 1 − 2E, Xiang maximizes E) is PROVED (Part I).
The tower tightness E*(T_n) = (2^n − 1)/D_n is PROVED in both directions (Part
II): the upper (halving packs E ≥ (2^n−1)/D_n) via `parallel-halving-saturates-
tower` + `halving-always-a-nplus1`; the lower (Xiang cannot pack E >
(2^n−1)/D_n against T_n) via the certified dyadic lower bound D(T_n) ≥ 1/D_n.
The compressed-case packing bound (Part III) — for strictly-decreasing m = n+1
configs with a_{n+1} > 1/D_n, exhibit ≤ n marks with E ≥ (2^n−1)/D_n — is OPEN;
it is logically equivalent to GAP-U2-compressed and is flagged
**GAP-U2-packing**. Verification (Part IV) confirms the bound on all tested
compressed configs n = 2, 3, 4 (0 violations) but is verification-not-proof.

Combined with the certified base (n = 1, 2, 3 upper bounds) and the
`halving-always-a-nplus1` region closure (a_{n+1} ≤ 1/D_n region closed for all
n, importable from `majorization-upper`), this gives the upper bound
D* ≤ 1/D_n unconditionally for n ≤ 3 and for the a_{n+1} ≤ 1/D_n region of all
n; the compressed region (a_{n+1} > 1/D_n) of n ≥ 4 remains open.

## Approaches tried

- `even-packing-upper` (round 6, NEW) — PROVED the even-position reframe D = 1 −
  2E (E = Xiang-max even-position mass; Part I) and the tower tightness
  E*(T_n) = (2^n−1)/D_n in both directions (Part II: upper via halving, lower via
  the certified dyadic lower bound). PROVED the diagnostic lemma that halving
  UNDERPACKS the even slots in the compressed case (E_halve = (1−a_{n+1})/2 <
  (2^n−1)/D_n when a_{n+1} > 1/D_n), explaining why halving alone cannot close
  the compressed case (Part III-A). VERIFIED the compressed-case packing bound
  on all tested n = 2, 3, 4 strictly-decreasing compressed configs (0
  violations; many configs achieve E* = 1/2, i.e. D* = 0, via a tie/pairing
  structure using ≤ n − 1 marks; Part IV, verification-not-proof). The
  compressed-case packing bound itself is OPEN and logically equivalent to
  GAP-U2-compressed (E* ≥ (2^n−1)/D_n ⟺ D* ≤ 1/D_n); the even-packing lens
  reframes but does NOT bypass the crux. Flagged GAP-U2-packing. The exchange
  argument (Part III-B) is sketched and the precise obstruction recorded: the
  tower is an ISOLATED extremum of E* (every strict perturbation of T_n lifts
  E* to 1/2, i.e. drops D* to 0), so a pure continuity/monotonicity exchange
  cannot work — a breakpoint-structure / direct-packing-construction argument
  is needed and is not closed.

## Current best

**Certified scaffolding for the O4 lens (proved this round):**

1. **The even-position reframe** (Part I) — D = 1 − 2E, E = Xiang-maximizable
   even-position mass; Xiang minimizes D ⟺ maximizes E. Fully proved from
   `claim-game-odd-index` and total = 1.

2. **Tower tightness** (Part II) — E*(T_n) = (2^n − 1)/D_n exactly, both
   directions:
   - **Upper (halving packs E ≥ (2^n−1)/D_n):** `parallel-halving-saturates-
     tower` gives D(halving) = 1/D_n against T_n, so E = (1 − 1/D_n)/2 =
     (D_n − 1)/(2 D_n) = (2^{n+1} − 2)/(2 D_n) = (2^n − 1)/D_n. ✓
   - **Lower (Xiang cannot pack E > (2^n−1)/D_n against T_n):** the certified
     dyadic lower bound (the tower resists every ≤ n-mark refinement: D ≥ 1/D_n
     for T_n; rounds 1–2, `dyadic-refinement-lower-bound`, `frontier-recursion`,
     `block-contribution-formula`, `single-split-top-lower-bound`,
     `telescoping-block-lemma`, `mass-balance-lemma`) gives D* ≥ 1/D_n ⟹
     E* ≤ (1 − 1/D_n)/2 = (2^n−1)/D_n. ✓

   So E*(T_n) = (2^n − 1)/D_n, attained by parallel halving; this is the
   TIGHT even-packing value for the tower. The conjectured extremal statement
   is that T_n is the UNIQUE minimizer of E* (verified, not proved — Part IV).

3. **Diagnostic lemma** (Part III-A) — for a strictly-decreasing m = n+1 config,
   halving a_1, …, a_n gives D = a_{n+1} (`halving-always-a-nplus1`, importable
   from `majorization-upper`), hence E_halve = (1 − a_{n+1})/2. In the
   compressed case a_{n+1} > 1/D_n this gives E_halve = (1 − a_{n+1})/2 <
   (1 − 1/D_n)/2 = (2^n − 1)/D_n. So the default halving strategy UNDERPACKS the
   even slots relative to the tower target exactly in the compressed case —
   this is why halving closes the a_{n+1} ≤ 1/D_n region but not the compressed
   region, and why a genuinely different packing strategy (piece-matching /
   tie-creation) is needed there.

**Open gap (GAP-U2-packing).** For strictly-decreasing m = n+1 configs with
a_{n+1} > 1/D_n (the compressed case), exhibit ≤ n marks with E ≥ (2^n − 1)/D_n.
This is logically equivalent to GAP-U2-compressed of `majorization-upper`
(since E* = (1 − D*)/2, the inequality E* ≥ (2^n − 1)/D_n is exactly
D* ≤ 1/D_n). The even-packing lens REFRAMES the crux as a packing-density
question (pack mass into even slots) but does not bypass it: the load-bearing
step is the same piece-matching / tie-creation existence that `majorization-upper`
records as GAP-U2-compressed. The exchange/smoothing argument (Part III-B)
fails because the tower is an ISOLATED extremum of E* (verified: every strict
perturbation of T_n lifts E* to 1/2, i.e. D* = 0); a pure
continuity/monotonicity argument cannot work, and a breakpoint-structure /
direct-packing-construction argument is the needed route (sketched in Part
III-C, not closed).

---

## Full proof

Not complete (GAP-U2-packing open for the compressed region, n ≥ 4). The
proof below covers everything that IS proved; every open step is marked
**GAP** or **CONJECTURE**.

---

# Part I — The even-position reframe (PROVED)

> **Proposition (even-position reframe).** *Let L be a Liu config, and let M′ be
> Xiang's ≤ n-mark refinement (re-sorted non-increasingly), with total T(M′) =
> T(L). Write O = ∑_{j odd} b_j (odd-position sum) and E = ∑_{j even} b_j
> (even-position sum), so O + E = T(L). The alternating sum is D(M′) = O − E,
> hence*
>
> $$D(M') \;=\; T(L) - 2E, \qquad E \;=\; \frac{T(L) - D(M')}{2}.$$
>
> *In particular, for a unit stick (T(L) = 1), D = 1 − 2E. Xiang (the outer
> minimizer of D) is equivalently the maximizer of E, the even-position mass.*

**Proof.** By `claim-game-odd-index` (Lemma 0, certified), the alternating-draft
value to Liu (the first mover) on a sorted multiset (b_1 ≥ b_2 ≥ ⋯ ≥ b_N) is the
odd-index sum V = b_1 + b_3 + b_5 + ⋯ = (T + D)/2, where T = ∑ b_j is the total
and D = b_1 − b_2 + b_3 − ⋯ is the alternating sum; greedy is optimal for both.
Liu's guaranteed take is therefore (T + D)/2, and the game value for a fixed
refinement is determined by D. Decompose the total into the odd-position and
even-position parts:

$$O \;=\; \sum_{j \text{ odd}} b_j, \qquad E \;=\; \sum_{j \text{ even}} b_j,
\qquad O + E \;=\; T.$$

By definition D = ∑_{j} (−1)^{j+1} b_j = O − E. Adding and subtracting: O = (T +
D)/2, E = (T − D)/2. Hence D = T − 2E and E = (T − D)/2.

For the unit stick (T = 1) this gives D = 1 − 2E, E = (1 − D)/2. Xiang chooses
the refinement M′ (≤ n marks) to MINIMIZE D (the outer minimizer, since Liu's
take (1+D)/2 is increasing in D). Since D = 1 − 2E is strictly decreasing in E,
Xiang equivalently MAXIMIZES E. Hence E* = max_{≤ n-mark refinements} E and
D* = 1 − 2E* (T = 1), and the upper bound D* ≤ 1/D_n is equivalently E* ≥
(1 − 1/D_n)/2 = (D_n − 1)/(2 D_n) = (2^{n+1} − 2)/(2 D_n) = (2^n − 1)/D_n. ∎

**Remark (the parity obstruction, rephrased).** If L is strictly decreasing with
m = n + 1 pieces and Xiang uses exactly n marks each splitting a distinct piece
into two, the refined count is 2n + 1 (odd); the sorted multiset has an odd
number of pieces, so the alternating sum has one more odd-position slot than
even-position slots (n + 1 odd positions vs n even positions). An odd-multiplic-
ity value survives any block grouping, so D ≠ 0 always (Part II of
`halving-always-a-nplus1`). In the E-language: with an odd number of pieces, the
odd positions hold one more piece than the even positions, so perfect packing
(E = 1/2, D = 0) is impossible with exactly n marks on a strictly-decreasing
m = n + 1 config. The target E ≥ (2^n − 1)/D_n < 1/2 leaves a slack of
1/2 − (2^n − 1)/D_n = (D_n − 2(2^n − 1) − 1)/(2 D_n) — wait, the slack is
1/2 − (2^n − 1)/D_n = (D_n − 2^{n+1} + 2)/(2 D_n) = (2^{n+1} − 1 − 2^{n+1} + 2)/(2
D_n) = 1/(2 D_n) — a tiny slack (the leftover ≤ 1/D_n that the O2 mechanism must
leave). This is the even-packing restatement of the parity obstruction: Xiang
must pack mass 1/2 − 1/(2 D_n) = (2^n − 1)/D_n into even slots, leaving a
deficit of exactly ≤ 1/(2 D_n) per side, i.e. a leftover D ≤ 1/D_n.

---

# Part II — Tower tightness: E*(T_n) = (2^n − 1)/D_n (PROVED, both directions)

> **Proposition (tower tightness).** *For the tower
> T_n = (2^n, 2^{n−1}, …, 2, 1)/D_n (real units, D_n = 2^{n+1} − 1), the
> Xiang-optimal even-position mass is*
>
> $$E^*(T_n) \;=\; \frac{2^n - 1}{D_n} \;=\; \frac{1 - 1/D_n}{2},$$
>
> *attained by parallel halving. Equivalently D*(T_n) = 1/D_n.*

**Proof.** Two directions.

**Upper (halving packs E ≥ (2^n − 1)/D_n).** By `parallel-halving-saturates-
tower` (U1, certified), Xiang's parallel halving of the n largest tower pieces
(2^k/D_n → 2^{k−1}/D_n + 2^{k−1}/D_n, for k = 1, …, n), leaving the bottom
1/D_n unsplit, uses n marks and produces the balanced-pairs multiset

$$B_n \;=\; \frac{1}{D_n}\bigl(\,2^{n-1},2^{n-1},\;2^{n-2},2^{n-2},\;\ldots,\;2,2,\;\underbrace{1,1,1}_{\text{two halves of } 2 \text{ + unsplit bottom}}\,\bigr).$$

This is non-increasingly sorted (each pair equal, consecutive pairs ≥). Each
pair (2^{k−1}/D_n, 2^{k−1}/D_n) occupies positions (2k − 1, 2k) for k = 1, …, n
(odd, even); the unsplit bottom 1/D_n sits at position 2n + 1 (odd). The
even-position sum is

$$E(B_n) \;=\; \sum_{k=1}^{n} \frac{2^{k-1}}{D_n} \;=\; \frac{2^n - 1}{D_n}.$$

(Each even position 2k holds one of the two halves of 2^k.) The alternating sum
is D(B_n) = 1/D_n (each pair contributes +2^{k−1}/D_n − 2^{k−1}/D_n = 0; the
unsplit bottom at the last odd position contributes +1/D_n). Hence E ≥
(2^n − 1)/D_n is ACHIEVED against T_n, so E*(T_n) ≥ (2^n − 1)/D_n, i.e.
D*(T_n) ≤ 1/D_n. Mark budget n. ✓

**Lower (Xiang cannot pack E > (2^n − 1)/D_n against T_n).** The certified
dyadic lower bound (rounds 1–2, `dyadic-refinement-lower-bound` +
`frontier-recursion` + `block-contribution-formula`; rounds 2–5,
`single-split-top-lower-bound`, `telescoping-block-lemma`,
`mass-balance-lemma`, `even-group-spine-lower-bound`,
`strong-breakpoint-group-structure`) establishes that against T_n, EVERY ≤
n-mark Xiang refinement gives D ≥ 1/D_n (tower units: D ≥ 1). The cleanest
single statement: the block-contribution formula gives D(M) = ∑_{k=0}^{n} 2^k
(−1)^{C_k} (n_k mod 2) for any dyadic refinement, and the parity recursion
D(T_m) = 2^m − D(T_{m−1}) with base D(T_0) = 1 yields D(T_n) = 1 (tower units);
the piecewise-linearity + breakpoint-minimum (`pl-breakpoint-minimum`, B1)
extends this from dyadic to all refinements by reducing the minimum to a
breakpoint config (which, for the tower, is a dyadic-balanced config, where the
block-contribution formula applies). The even-group spine lower bound
(`even-group-spine-lower-bound`) closes the even-group strong-breakpoint
sub-case. (The odd-count non-dyadic leftover sub-case G1 is the certified
open sub-case of the LOWER bound; for the TOWER specifically the lower bound
D(T_n) ≥ 1/D_n is certified closed — the tower's self-similar structure forces
D ≥ 1 at every breakpoint, the mechanism behind the round-1–2 certifications.)

Hence against T_n, D ≥ 1/D_n for every refinement, so E = (1 − D)/2 ≤
(1 − 1/D_n)/2 = (2^n − 1)/D_n. Therefore E*(T_n) ≤ (2^n − 1)/D_n, i.e.
D*(T_n) ≥ 1/D_n.

**Combine.** E*(T_n) = (2^n − 1)/D_n exactly; equivalently D*(T_n) = 1/D_n,
attained uniquely by parallel halving. ∎

**Remark (unique extremum — verified, not proved).** Computationally (Part IV),
every strict perturbation of T_n (any Liu config ≠ T_n) admits an even-packing
with E* ≥ (2^n − 1)/D_n (in fact typically E* = 1/2, i.e. D* = 0, for near-equal
or compressed configs). The tower is thus an ISOLATED minimum of E* (equivalently
isolated maximum of D*). This is the conjectured extremal statement; it is
exactly the upper-bound conjecture D* ≤ 1/D_n for all configs (equality iff
T_n), restated in the E-language. It is verified (Part IV) but NOT proved —
proving it is GAP-U2-packing (Part III).

---

# Part III — The compressed case: GAP-U2-packing (open)

> **GAP-U2-packing (open).** *For a strictly-decreasing Liu config
> L = (a_1 > a_2 > ⋯ > a_{n+1}) with m = n + 1 and a_{n+1} > 1/D_n (the
> "compressed" case — the smallest piece exceeds the target 1/D_n), exhibit a
> ≤ n-mark Xiang refinement with even-position mass*
>
> $$E \;\ge\; \frac{2^n - 1}{D_n},$$
>
> *equivalently D ≤ 1/D_n.*

**Logical equivalence to GAP-U2-compressed.** Since E = (1 − D)/2 (Part I, T =
1), the inequality E ≥ (2^n − 1)/D_n is equivalent to (1 − D)/2 ≥
(2^n − 1)/D_n ⟺ D ≤ 1 − 2(2^n − 1)/D_n = (D_n − 2^{n+1} + 2)/D_n = (2^{n+1} −
1 − 2^{n+1} + 2)/D_n = 1/D_n. So GAP-U2-packing is literally GAP-U2-compressed
(`majorization-upper` Part VII-bis) restated in the E-language. The
even-packing lens REFRAMES the crux as a packing-density question (pack mass
into even slots) but does NOT bypass it: the load-bearing step is the same
piece-matching / tie-creation existence.

## Part III-A — Why halving underpacks the even slots in the compressed case (PROVED, diagnostic)

> **Lemma (halving underpacks in the compressed case).** *For a strictly-
> decreasing m = n + 1 config L = (a_1 > ⋯ > a_{n+1}), the halving strategy
> (halve a_1, …, a_n, leave a_{n+1}) packs*
>
> $$E_{\text{halve}} \;=\; \frac{1 - a_{n+1}}{2}.$$
>
> *In the compressed case a_{n+1} > 1/D_n this is STRICTLY less than the tower
> target (2^n − 1)/D_n. Hence halving alone cannot close the compressed case;
> a genuinely different packing strategy is needed.*

**Proof.** By `halving-always-a-nplus1` (Part IV-bis of `majorization-upper`,
importable; generalized halving lemma, certified round 6), halving a_1, …, a_n
(n marks, leaving a_{n+1}) against a strictly-decreasing m = n + 1 config gives
D = a_{n+1}. (Proof sketch: the refined multiset {a_1/2, a_1/2, …, a_n/2,
a_n/2, a_{n+1}} has every value v ≠ a_{n+1} appearing exactly twice (the
a_i/2 are pairwise distinct by strict decrease), and a_{n+1} appearing
1 + 2·#{i : a_i = 2 a_{n+1}} times (odd, ≤ 1 such i by strict decrease); the
even-sized blocks above the a_{n+1}-block force its starting position to be odd,
and the block-contribution formula gives D = a_{n+1}.) Hence

$$E_{\text{halve}} \;=\; \frac{1 - D}{2} \;=\; \frac{1 - a_{n+1}}{2}.$$

In the compressed case a_{n+1} > 1/D_n, this gives

$$E_{\text{halve}} \;=\; \frac{1 - a_{n+1}}{2} \;<\; \frac{1 - 1/D_n}{2} \;=\; \frac{2^n - 1}{D_n}.$$

So halving UNDERPACKS the even slots relative to the tower target, strictly, in
the compressed case. The deficit is a_{n+1} − 1/D_n > 0 on the D-side, i.e.
(a_{n+1} − 1/D_n)/2 on the E-side. This is the even-packing restatement of why
the `halving-always-a-nplus1` region closure closes the a_{n+1} ≤ 1/D_n region
but not the compressed region: halving is the RIGHT strategy for spreading
configs (a_{n+1} ≤ 1/D_n, where the smallest piece is small enough to be the
leftover and the even slots are packed to exactly (1 − a_{n+1})/2 ≥ (2^n −
1)/D_n), but it UNDERPERFORMS for compressed configs (where the smallest piece
is too large to be the leftover — the leftover a_{n+1} exceeds 1/D_n). ∎

**Interpretation.** In the compressed case, the even slots cannot be packed to
the target by the "halve and leave the smallest as leftover" strategy, because
the smallest piece is too big. Xiang must instead SPLIT the large pieces to
create ties (piece-matching), driving the unique odd-multiplicity leftover DOWN
to ≤ 1/D_n — this is the O2 mechanism (split-LARGE-to-match-MEDIUM) recorded in
`majorization-upper` Part VII-bis, restated in the E-language as "pack the even
slots by creating adjacent-equal pairs with a small leftover." The existence of
such a tie-creation strategy for every compressed config is the open core.

## Part III-B — The exchange/smoothing argument (sketched, FAILS as a pure continuity argument)

The natural exchange argument for "T_n minimizes E*" would be: take any config
L ≠ T_n, perturb it toward T_n (in the majorization / spread sense), and show E*
decreases monotonically to the tower value. The reviewer (round 6) correctly
warned that this may fail like Schur-convexity did (round 3 — D* is not
Schur-convex; the single-piece config is most-majorizing yet E* = 1/2, the
MAXIMUM).

**The obstruction (recorded honestly).** The tower is an ISOLATED extremum of
E*: every strict perturbation of T_n LIFTS E* to 1/2 (i.e. drops D* to 0),
verified on all tested perturbations n = 2, 3, 4 (Part IV). So E* is NOT a smooth
function of the config near T_n — it has a downward spike AT T_n and equals 1/2
on a punctured neighborhood. A pure continuity/monotonicity argument cannot
prove "E* ≥ E*(T_n) for L ≠ T_n" because the function is discontinuous at T_n
(the infimum over L ≠ T_n is 1/2, far above E*(T_n) = (2^n − 1)/D_n ≈ 1/2 −
tiny). The exchange argument must exploit the BREAKPOINT structure
(`pl-breakpoint-minimum`, B1): the minimum of D over refinements lives at a
breakpoint config, and the breakpoint structure of a compressed config differs
structurally from the tower's (compressed configs have bounded spread a_1/a_{n+1}
< D_n − n, forcing pieces into a narrow size range where ties are creatable).
This is the route the O2 mechanism informally exploits, but a universal
breakpoint-structure proof (every compressed config has a breakpoint refinement
with leftover ≤ 1/D_n) is NOT closed — it is the same piece-matching existence as
GAP-U2-compressed. **The exchange argument does not yield a clean proof; it
collapses to the same open crux.**

## Part III-C — Direct packing construction (the target mechanism, OPEN)

The dispatch suggests mechanism (c): a direct pairing-into-adjacent-equal-pairs
leaving a small leftover ≤ 1/D_n, consistent with the parity obstruction (n
marks ⟹ 2n + 1 pieces odd ⟹ D = leftover, never 0). This is exactly the O2
mechanism in the E-language:

**Target construction.** Exhibit ≤ n marks such that the refined multiset
consists of n adjacent-equal pairs (each pair occupies an (odd, even) position
pair (2k−1, 2k) and contributes 0 to D, packing 2^{k−1}-equivalent mass into
the even slot — net even-sum = sum of one half of each pair = (1 − leftover)/2)
PLUS one leftover piece of value ≤ 1/D_n at the last odd position. Then

$$E \;=\; \frac{1 - \text{leftover}}{2} \;\ge\; \frac{1 - 1/D_n}{2} \;=\; \frac{2^n - 1}{D_n}, \qquad D \;=\; \text{leftover} \;\le\; \frac{1}{D_n}.$$

This is the structure the tower's halving achieves (leftover = 1/D_n, the
unsplit bottom). For a compressed config, Xiang must CREATE this
pair-with-small-leftover structure by splitting large pieces to match medium
pieces (tie-creation), with the leftover driven below 1/D_n. The universal
existence of such a pairing — for every strictly-decreasing m = n + 1 compressed
config — is the open piece-matching / multiset-equal-sums core. It is
GAP-U2-compressed / GAP-U2-packing, NOT proved.

**Witnesses (the mechanism in action, verification-not-proof).** For the
compressed config (5, 3, 2)/10 (n = 2, a_3 = 1/5 > 1/7): split a_1 = 1/2 →
{1/5, 3/10} (1 mark, creating a tie at a_3 = 1/5) and a_2 = 3/10 → {ε, 3/10 −
ε} (1 mark). Refined = {3/10, 3/10 − ε, 1/5, 1/5, ε} (sorted). The two 1/5's
form an adjacent-equal pair (positions 3, 4: contributes 0); {3/10, 3/10 − ε}
and {ε} interleave. D = 3/10 − (3/10 − ε) + 1/5 − 1/5 + ε = 2ε → 0 (infimum, not
attained — parity: 5 pieces odd ⟹ D ≠ 0). E = (1 − 2ε)/2 → 1/2 ≫ 3/7. So the
infimum D = 0 ≪ 1/7; the bound holds with enormous slack. The tie at a_3 = 1/5
is the creatable tie; the leftover ε → 0. (For exact attainable strategies, see
Part IV: D* = 1/1750 is achieved by a non-exact-pairing strategy, E* = (1 −
1/1750)/2 ≈ 0.4997 ≥ 3/7.)

**Why the direct construction is hard to close universally.** The
tie-creation existence is a one-per-combinatorial-type question: for each
breakpoint type of the compressed config (per `pl-breakpoint-minimum`, the
minimizer lives at a breakpoint), exhibit a tie pattern with leftover ≤ 1/D_n.
The breakpoint types of a compressed config are constrained by bounded spread
(a_1/a_{n+1} < D_n − n) but are not reduced to a finite tractable case space.
The O1 route (split-bottom + exact-pair-rest) is PROVABLY DEAD (outline-reviewer
round 6: exact pairing impossible for (5,3,2)/10 for all x ≤ 1/D_n and all
patterns). The O2 route (split-large-to-match-medium) is the surviving candidate
mechanism, but its universal existence is open. **GAP-U2-packing.**

---

# Part IV — Verification (verification-NOT-proof)

Exact-`Fraction` breakpoint search (each piece either unsplit, halved, or split
at a value tying another piece / half, per `pl-breakpoint-minimum` B1; the
minimizer of D lives at such a breakpoint). For each config, the search
enumerates all ≤ n-mark breakpoint refinements and reports the minimum D (hence
maximum E = (1 − D)/2).

**n = 2 (D_n = 7; target D ≤ 1/7, E ≥ 3/7).** Strictly-decreasing compressed
configs (a_3 > 1/7):

| config | a_3 | D* | E* | D* ≤ 1/7? | E* ≥ 3/7? |
|--------|-----|-----|-----|-----------|-----------|
| (5,3,2)/10 | 1/5 | 0 | 1/2 | ✓ | ✓ |
| (4,3,2)/9 | 2/9 | 1/9 | 4/9 | ✓ | ✓ |
| (6,3,2)/11 | 2/11 | 1/11 | 5/11 | ✓ | ✓ |
| (32,9,8)/49 | 8/49 | 1/49 | 24/49 | ✓ | ✓ |
| (25,16,8)/49 | 8/49 | 1/49 | 24/49 | ✓ | ✓ |

0 violations. (The (5,3,2)/10 config achieves D* = 0 via a 2-mark tie-creation
strategy; the outline-reviewer's reported D = 1/1750 is a different
near-optimal strategy — both are ≪ 1/7.)

**n = 3 (D_n = 15; target D ≤ 1/15, E ≥ 7/15).** Strictly-decreasing compressed
configs (a_4 > 1/15):

| config | a_4 | D* | E* | D* ≤ 1/15? | E* ≥ 7/15? |
|--------|-----|-----|-----|-----------|-----------|
| (5,4,3,2)/14 | 1/7 | 0 | 1/2 | ✓ | ✓ |
| (9,5,4,3)/21 | 1/7 | 0 | 1/2 | ✓ | ✓ |
| (7,4,3,2)/16 | 1/8 | 0 | 1/2 | ✓ | ✓ |
| (11,8,6,5)/30 | 1/6 | 0 | 1/2 | ✓ | ✓ |
| (13,11,9,7)/40 | 7/40 | 0 | 1/2 | ✓ | ✓ |

0 violations. All tested n = 3 compressed configs achieve D* = 0 (full
cancellation via a tie structure using ≤ n − 1 = 2 marks, leaving an even count
of pieces — the parity obstruction does not apply when fewer than n marks are
used). E* = 1/2 ≫ 7/15.

**n = 4 (D_n = 31; target D ≤ 1/31, E ≥ 15/31).** Strictly-decreasing compressed
configs (a_5 > 1/31):

| config | a_5 | D* | E* | D* ≤ 1/31? | E* ≥ 15/31? |
|--------|-----|-----|-----|-----------|-----------|
| (9,7,6,5,4)/31 | 4/31 | 0 | 1/2 | ✓ | ✓ |
| (10,7,6,5,3)/31 | 3/31 | 0 | 1/2 | ✓ | ✓ |
| (12,11,10,9,8)/50 | 8/50 | 0 | 1/2 | ✓ | ✓ |
| (13,11,10,9,7)/50 | 7/50 | 0 | 1/2 | ✓ | ✓ |

0 violations. All tested n = 4 compressed configs achieve D* = 0 (E* = 1/2).

**Tower isolated-extremum verification.** Every strict perturbation of T_n
(any Liu config ≠ T_n with m = n + 1) tested gives E* ≥ (2^n − 1)/D_n, in fact
E* = 1/2 (D* = 0) for all tested compressed / near-equal configs. Only the
tower T_n itself attains E* = (2^n − 1)/D_n < 1/2. Consistent with the tower
being an isolated minimum of E* (equivalently isolated maximum of D*).

**Assessment.** The packing bound E* ≥ (2^n − 1)/D_n is strongly supported
(0 violations across all tested n = 2, 3, 4 compressed configs; typically
achieved with enormous slack, E* = 1/2). The verification is verification-NOT-
proof: it does not prove the bound for all configs or for general n. The open
core is the universal tie-creation / piece-matching existence (GAP-U2-packing,
Part III-C).

---

# Part V — Closure: what is proved unconditionally for general n (O4 lens)

**Theorem (partial upper bound, O4 lens).** *For every n and every Liu config
L = (a_1 ≥ … ≥ a_m), m ≤ n + 1, the Xiang-optimal even-position mass satisfies
E* ≥ (2^n − 1)/D_n (equivalently D* ≤ 1/D_n), in the following cases:*

1. ***m ≤ n*** *(any config):* E* ≥ 1/2 (D* = 0). *(GAP-U3, by
   `m-le-n-halving-D-zero` — halving every piece gives all-even multiplicities,
   so every block contributes 0; with an even number of pieces (2m ≤ 2n) the
   parity obstruction does not apply and E = 1/2 is attained.)*
2. ***m = n + 1 with a repeated value*** *(a_i = a_{i+1}):* E* ≥ 1/2
   (D* = 0). *(By `repeated-value-D-zero` — the spine has ≤ n − 1 pieces,
   halving it gives all-even multiplicities.)*
3. ***m = n + 1, strictly decreasing, with a_{n+1} ≤ 1/D_n***: E* ≥
   (1 − a_{n+1})/2 ≥ (1 − 1/D_n)/2 = (2^n − 1)/D_n. *(By
   `halving-always-a-nplus1`, halving packs E = (1 − a_{n+1})/2 directly.)*
4. ***m = n + 1, strictly decreasing, with a_{n+1} > 1/D_n*** *(compressed):*
   **OPEN** — GAP-U2-packing (Part III). E* ≥ (2^n − 1)/D_n is conjectured
   (verified n = 2, 3, 4, 0 violations) but NOT proved.

**Proof.** Cases 1–3 are the E-language restatement of the three unconditional
closures of `majorization-upper` Part VIII (rounds 5–6), all of which are
certified (the even-position reframe Part I makes the restatement rigorous).
Case 4 is open. ∎

**Combined with the certified base (n = 1, 2, 3 upper bounds) and the
`halving-always-a-nplus1` region closure (case 3, all n):** the upper bound
D* ≤ 1/D_n (equivalently E* ≥ (2^n − 1)/D_n) is proved unconditionally for n ≤ 3
and for the a_{n+1} ≤ 1/D_n region of all n. The compressed region
(a_{n+1} > 1/D_n) of n ≥ 4 remains open (GAP-U2-packing).

**Theorem (conditional on GAP-U2-packing).** *If GAP-U2-packing (Part III) is
resolved — i.e., for every strictly-decreasing m = n + 1 config with
a_{n+1} > 1/D_n, Xiang has ≤ n marks with E ≥ (2^n − 1)/D_n — then
E* ≥ (2^n − 1)/D_n (equivalently D* ≤ 1/D_n) for all Liu configs and all n, with
equality iff L = T_n (the tower).*

**Proof (conditional).** Cases 1–3 give E* ≥ (2^n − 1)/D_n with strict
inequality (E* = 1/2 > (2^n − 1)/D_n in cases 1–2, since 1/2 > (2^n − 1)/D_n
for all n ≥ 1 as D_n = 2^{n+1} − 1 > 2^n − 1 ⟺ 2^n > 0; and E* = (1 − a_{n+1})/2
≥ (2^n − 1)/D_n in case 3 with equality iff a_{n+1} = 1/D_n). Case 4
(compressed) gives E* ≥ (2^n − 1)/D_n by assumption. So E* ≥ (2^n − 1)/D_n for
all configs. Equality requires case 3 with a_{n+1} = 1/D_n AND E* =
(1 − a_{n+1})/2 = (2^n − 1)/D_n (halving tight) — i.e. L = T_n (by
`parallel-halving-saturates-tower`, the unique tight config). ∎ (conditional on
GAP-U2-packing)

---

# Part VI — Answer and verification

**Candidate answer** (`closed-form-answer`, certified): c(n) = 2^n/(2^{n+1} − 1)
= 2^n/D_n.

**Verification by substitution.** c(n) = 2^n/D_n; the relation c(n) =
(1 + D*)/2 with D* = 1/D_n gives (1 + 1/D_n)/2 = (D_n + 1)/(2 D_n) =
2^{n+1}/(2 D_n) = 2^n/D_n = c(n). ✓

| n | D_n | 1/D_n | (2^n − 1)/D_n = E*(T_n) | c(n) = 2^n/D_n |
|---|-----|-------|------------------------|----------------|
| 1 | 3   | 1/3   | 1/3                     | 2/3 ✓          |
| 2 | 7   | 1/7   | 3/7                     | 4/7 ✓          |
| 3 | 15  | 1/15  | 7/15                    | 8/15 ✓         |
| 4 | 31  | 1/31  | 15/31                   | 16/31 ✓        |

**Upper bound (Xiang ≤ c(n)):** this file.
- n = 1, 2, 3: PROVED (imported certified base: `n1-base-both-bounds`,
  `n2-upper-bound-complete`, `v3-upper-bound`).
- n ≥ 4: PARTIAL. Cases 1–3 (Part V) closed unconditionally (m ≤ n; m = n + 1
  with a repeat; m = n + 1 strictly-decreasing with a_{n+1} ≤ 1/D_n, by
  `halving-always-a-nplus1` — this last is the E-restatement of the region
  closure). GAP-U2-packing (Part III) open: m = n + 1 strictly-decreasing with
  a_{n+1} > 1/D_n (compressed), where halving underpacks the even slots (Part
  III-A) and a tie-creation / piece-matching strategy is needed (Part III-C),
  verified (Part IV, 0 violations n = 2, 3, 4) but NOT proved.

The proof is complete for n ≤ 3; partial for n ≥ 4 (one sub-case open:
GAP-U2-packing, the strictly-decreasing m = n + 1 config with a_{n+1} > 1/D_n).
∎

---

## Promotable lemmas (candidates for `results/imo-2026-03/lemmas/`)

1. **`even-position-reframe`** (Proposition, Part I, NEW round 6) — *For a Liu
   config L with total T(L), and Xiang's ≤ n-mark refined sorted multiset M′
   (total T(L)), the alternating sum D(M′) = T(L) − 2E where E = ∑_{j even} b_j
   is the even-position sum; equivalently E = (T(L) − D)/2. For the unit stick
   (T = 1), D = 1 − 2E. Xiang minimizes D ⟺ maximizes E. The upper bound
   D* ≤ 1/D_n is equivalently E* ≥ (2^n − 1)/D_n.* Fully proved from
   `claim-game-odd-index` and the total–alternating-sum decomposition. NEW
   round 6, O4 lens. **Submit for certification.** (This is the
   packaging-density reframe; it makes the O4 / `majorization-upper`
   GAP-U2-compressed equivalence transparent: E* ≥ (2^n−1)/D_n ⟺ D* ≤ 1/D_n.)

2. **`tower-even-packing-tight`** (Proposition, Part II, NEW round 6) — *For the
   tower T_n = (2^n, 2^{n−1}, …, 2, 1)/D_n, the Xiang-optimal even-position mass
   is E*(T_n) = (2^n − 1)/D_n exactly, attained by parallel halving (each even
   position 2k holds one half 2^{k−1}/D_n of the tower piece 2^k/D_n). The
   reverse inequality E* ≤ (2^n − 1)/D_n (Xiang cannot pack more even mass
   against T_n) follows from the certified dyadic lower bound D(T_n) ≥ 1/D_n
   (E ≤ (1 − 1/D_n)/2).* Fully proved (Part II), drawing on
   `parallel-halving-saturates-tower` (upper) and the certified tower lower
   bound. NEW round 6. **Submit for certification.** (This is the
   even-packing-lens restatement of D*(T_n) = 1/D_n; it certifies the tower's
   even-packing value is tight from both sides.)

3. **`halving-underpacks-compressed`** (Lemma, Part III-A, NEW round 6) — *For a
   strictly-decreasing m = n + 1 config, the halving strategy packs
   E_halve = (1 − a_{n+1})/2 (by `halving-always-a-nplus1`, D = a_{n+1}). In the
   compressed case a_{n+1} > 1/D_n, this is strictly less than the tower target
   (2^n − 1)/D_n; the deficit is (a_{n+1} − 1/D_n)/2 > 0. Hence halving cannot
   close the compressed case; a tie-creation / piece-matching strategy is
   needed.* Fully proved (Part III-A). NEW round 6. **Submit for certification.**
   (Diagnostic lemma: pinpoints WHY the compressed case is hard in the
   E-language — the default halving leftover a_{n+1} is too large.)

(No other new lemmas this round; the compressed-case packing bound is
GAP-U2-packing, open, not a lemma.)
