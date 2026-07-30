# Build report — minimal-linking-prime-extremal (round 5)

**Status: partial.** Wrote `results/imo-2026-06/approaches/minimal-linking-prime-extremal.md`.

## What was built (rigorous, imported certified lemmas by reference — none re-proved)
- **Step 1** (CSP)⇒theorem: imported `csp-implies-theorem.md`. Assume a bad term exists, toward contradiction.
- **Step 2** Windows W_k=(k·a_1,(k+1)·a_1), length a_1, good endpoints. (2a) every bad term is off-lattice inside some W_k (imported GPC + BPA). (2b) every term small-hits every a_1-multiple (clean GPC corollary).
- **Step 3** Extremal prime q\*=min large prime dividing both members of some small-disjoint term pair; well-defined by well-ordering once a bad term is assumed (BPA gives such a pair). **(3a)** every large link of every small-disjoint term pair is ≥ q\* — the non-symmetric, value-independent handle.
- **Step 4** Local per-window spacing: ≤ a_1/q\*+1 multiples of any p≥q\* per window; same-window links are <a_1 apart, big links (≥a_1) straddle two windows. Strictly local — does NOT touch the dead global Σ1/p² count.
- Crux reformulated as **(DESC)**: the bad-window index set has no minimum (a bad window forces a smaller-index bad window). (DESC)⇒ contradiction with k\*=min ⇒ (CSP) ⇒ theorem.

## Reviewer correction heeded
DROPPED the false "finitely many bad windows collide with the single ascent" closure. Recorded in-file why it fails (BPA ascent only lifts the *smallest* bad term, never produces a bad term above every bad term). Pursued ONLY the self-contained descent-on-k line, as instructed.

## Honest open gap
**(DESC)** — the window-index descent step — is unproved and is difficulty-equivalent to the whole crux (CSP). Documented in-file that all three natural descents fail: (i) descend along the symmetric bad partner gives no smaller-index control (partner window can be larger); (ii) endpoint links are *small*, cannot seed a small-disjoint (bad) neighbour; (iii) descend on the prime (produce a link in (P_max,q\*)) would contradict q\* minimality and finish, but no construction of such a pair exists from the witness pair. Each attempt either re-assembles an infinite chain the structure does not supply (the relocated 6a trap) or needs an input equivalent to (CSP). Not claimed.

## Promotable sub-lemmas (offered to reviewer)
1. **Minimal linking prime q\* floors every large link** (Step 3) — non-symmetric handle, rests only on certified F1 + well-ordering.
2. **Per-window spacing cap** (Step 4) — local count, avoids the dead global capacity route.

## Assessment for orchestrator
This new far framing did not close the crux. It confirms the reviewer's diversity-assessment prediction: like the other two new framings it bottoms out on converting a single non-symmetric handle (here q\*) into a descent/unboundedness — the 6a wall relocated to the window index. The extremal prime buys a genuine floor (3a) and a genuine local count (4a/4b) but not the downward step. If bad-residue-witness-index also stalled on "one recurring object is not yet a contradiction," treat the shared wall as persisting and, per the reviewer's note, seed a framing attacking the greedy DYNAMICS of the actual successor a_{n+1} directly.
