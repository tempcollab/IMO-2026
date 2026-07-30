# Proof-builder report — breakpoint-vertex (imo-2026-03), round 18

## Outcome: C2 GATE FAILED → Status partial (no new prose; mechanism refuted and recorded dead)

Per the binding dispatch preconditions I ran precondition (1), the C2 post-crossing-contraction gate,
FIRST, in exact `Fraction` (never float). It FAILED decisively. Per the refute-and-stop instruction I
STOPPED, did NOT attempt precondition (2) C1 (caterpillar-min completeness — gated strictly behind a
passing C2), and shipped NO deep-interior proof. No fake proof.

## What was gated (exact Fraction; /tmp/gate_c2.py, gate_c2b.py, gate_c2c.py)

Object: `Φ(A)=min_{∅≠T} descKK(T)` (certified residual). Deep region `a₁<(L−u_nL)/2`. The proposed
closing mechanism: after the certified band-landing crossing index `k*`, the anchored reflected residual
`w_k=|w_{k-1}−a_k|` telescopes/contracts to `≤ u_nL` under ONE-REC dyadic caps. Most generous
operationalisation tested: `minpost = min_{k≥k*} w_k` (min over ALL post-crossing stopping points).

Adversarial families (as mandated): random sliver profiles, tight family `A^{(n)}={2^n,…,4,3,2}/(2^{n+1}+1)`,
and `A^{(n)}`-perturbations into the sliver, at n=3,4,5,6, ~14000 samples each.

## Result (worst-case ratios, exact Fraction)

```
 n | worst true Φ/u_n | worst minpost/u_n (contraction object)
 3 |     0.8824       |            4.5434
 4 |     0.9394       |            9.0932
 5 |     0.9692       |           13.8705
 6 |     0.9845       |           24.2583
```

- True `Φ/u_n ≤ 1` always (theorem TRUE, asymptotically tight — VALLEY-TIGHT).
- Contraction object `minpost/u_n` SATURATES far above `u_n`, GROWS with n (4.5→9.1→13.9→24.3, ~2× per
  unit n = the `~2^{n-1}` covering-radius signature). This IS the dead covering-radius family (GAP
  TWO-CAP: 3.2/6.1/8.9/15.8/24.6 at n=3..7) — exactly the collapse the reviewer warned of.

Clean exact witness (n=4, deep, reproducible): `A={1/3, 13/40, 13/40, 1/120, 1/120}`, `a₁=1/3 < L/2−u₄=29/62`,
`u₄=1/31`. Post-crossing reflected residual `minpost = 3/10 = 9.3·u₄`; true `Φ=0` via the tail subset
`{13/40,13/40}` (even cancellation) which EXCLUDES the anchor `a₁`.

## Root cause (structural, so no reflected-walk variant survives)

The reflected/caterpillar walk is anchored at `a₁` — every prefix contains `a₁`. The true minimiser is a
tail subset that EXCLUDES `a₁` (size up to `n`; cf. R17 `{30,25,20,15,10}/100`, R18 explorer's size-`n`
minimisers). No single anchored pass — of any stopping rule, since `minpost` already minimises over all
post-crossing stops — can see these. The ONE-REC caps bound the decrements, not the reflected residual;
the residual re-inflates on the next tail piece exactly as the covering radius does.

## Verdict / routing

- **9th dead upper mechanism:** sharpened-WTC / post-crossing reflected-walk / anchored-caterpillar
  contraction = covering-radius family in disguise. Recorded in the approach file so no round re-tries it.
- Slug stays **live, partial** — the certified reduction and the WTC boundary-layer closure (leader's
  rigorous core) are untouched. Deep-interior / sliver residual `Φ ≤ u_nL` for `a₁<L/2−u_n/2` stays OPEN.
- **Suggested route (route this slug: CHANGES REQUESTED / or RETHINK the C2 sub-mechanism).** The next
  upper lever must be a genuinely different object: an EXISTENCE bound on the restricted signed-subset-sum
  set — `∃ ∅≠T: |Σ_{i∈T} ε_i a_i| ≤ u_nL` with tree-realizable signs (Lemma RL) — via Steinitz /
  vector-balancing / prefix-discrepancy over ALL tree-realizable signings, NOT any anchored contraction.
  This matches the reviewer's plateau-break call.

## Spec concern

The outline's C2 mechanism was unsound as flagged by the reviewer (single-gap trap + covering-radius
collapse risk). The gate confirmed the collapse. reflected-walk-contraction (HELD) shares this dead gap,
so it too is dead as configured; do not build it. The field needs the Steinitz/signed-subset-sum
existence object next.

Files: approach `/home/agentuser/repo/results/imo-2026-03/approaches/breakpoint-vertex.md`;
gate scripts `/tmp/gate_c2.py`, `/tmp/gate_c2b.py`, `/tmp/gate_c2c.py`.
