# Build report — dyadic-discrepancy-euclid (GAP U, Case iii, constructive route), Round 4

**Problem:** imo-2026-03 (IMO 2026 P3). **Slug:** dyadic-discrepancy-euclid. **Status: partial.**
File: `results/imo-2026-03/approaches/dyadic-discrepancy-euclid.md` (created; the copy_approach seed
did not exist, so I authored a self-contained file importing the certified spine).

## EMPIRICAL GATE RESULT (led, as mandated — blocking gate honored)

Ran candidate deterministic pivot rules against the ground-truth solver `/tmp/round-4/rt_search.py`
on thousands of random Case (iii) instances per `k∈{2,3,4,5}`:

- **Naive "pin largest against SMALLEST" (literal Finding-1 reading): REFUTED.** Removes only
  `2ℓ_min`/step; residual `4×–14× u_k`, fails on 68–95% of k≥3 instances. Recorded as a dead end.
- **Correct rule = the ACCUMULATOR** (pin the *second*-largest into the largest; equivalently pin
  every other piece into a fixed top). Its final residual is exactly `2ℓ₁−Σ`. It **PASSES the gate on
  sub-region A `{ℓ₁ ≥ Σ/2}` for every k, 0 failures, worst ratio → 1 exactly at the boundary
  `ℓ₁=c(k)Σ`.** Verified `r=2ℓ₁−Σ` to machine precision and `≤u_k` with 0 violations over 2·10⁵
  region-A samples, k=2..6.
- On **sub-region B `{ℓ₁ < Σ/2}`** (super-balanced) the accumulator FAILS (2–10× u_k, k≥3); so do the
  pairwise-difference tournament and half-bisect-else-accumulate rules. The optimal solver stays
  ≤ 0.72 u_k there, so a winning play exists but is **not** any fixed simple schedule (consistent with
  the round-3 non-greedy obstruction). B is the same hard core the twin faces.

Gate verdict: a genuine deterministic schedule survives on region A, so the route is real and worth the
write-up; it is refuted on region B, left as an explicit gap (no fabrication).

## What I closed (fully rigorous, no induction)

**Case (iii) sub-region A `{Σ/2 ≤ ℓ₁ < c(k)Σ}` — closed for all n.** The accumulator schedule is a
legal Xiang play (Invisible-Pair pins) using `≤ k` cuts that reaches effective total exactly `2ℓ₁−Σ`.

Key proven pieces (all in the file):
- **Lemma 5.1:** `c(k)=(1+u_k)/2`, hence `2ℓ₁−Σ ≤ u_kΣ ⟺ ℓ₁ ≤ c(k)Σ` (5.1).
- **Lemma 5.2 (feasibility invariant):** under `ℓ₁≥Σ/2`, the invariant `Σ(rest) ≤ accumulator` is
  self-restoring; each step is a legal pin keeping the accumulator the unique maximum; the `b=a` edge
  forces `rest={b}` → a free-delete finishing at total 0. Termination in `≤ m−1 ≤ k` ops.
- **Theorem 5.3 / Corollary 5.4:** final total `= 2ℓ₁−Σ < u_kΣ`; RT then forces `D ≤ u_kΣ`.
- **Tightness:** at `ℓ₁=c(k)Σ` (dyadic extremal) the schedule returns exactly `u_k` — it is the
  optimal Xiang play at the extremum. This is a strong sanity anchor: the constructive strategy
  reproduces the sharp bound with equality on the exact tight configuration.

This is a genuinely distinct, directly-citable object from the twin (an explicit deterministic strategy
vs a strengthened existence-IH), and it needs **no** RT(k−1) call.

## Precise remaining gap

**GAP U-B (open):** RT(k) for `m=k+1` pieces with `ℓ₁ < Σ/2` (super-balanced Case iii). No fixed
simple schedule reaches `u_kΣ`; the optimal play mixes bisecting the largest with pinning near-equal
survivors, instance-dependently. Candidate routes noted in the file: stopping-time accumulator;
one-op reduction B→A; or the twin's balanced-regime invariant. Sub-region B grows with k
(`c(k)→1/2⁺`), so asymptotically it is most of Case (iii) — it is the real remaining wall.

## Spec concerns

- The two GAP-U twins (this slug + dyadic-discrepancy) now share the *same* residual, sub-region B
  `{ℓ₁<Σ/2}` of Case (iii): my constructive route peels off region A cleanly but bottoms out on B,
  and the twin's strengthened-IH targets exactly B. Per the outline-reviewer's own flag, if the twin
  also stalls on B next round, wall GAP U has collapsed to one obstruction and the orchestrator should
  escalate a genuinely different framing (the 2-adic recast) rather than a third same-wall mechanism.
  For next round I recommend routing this slug's builder specifically at GAP U-B via the
  **stopping-time accumulator** (pin into the top only until the "rest" total ≤ u_kΣ, then bisect
  survivors) — a concrete, checkable continuation of the constructive route.
- No other concerns; the region-A proof is complete and self-contained (imports only certified IP + RT).
