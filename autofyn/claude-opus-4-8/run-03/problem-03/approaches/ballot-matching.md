## Status
partial (mechanism REFUTED this round — see Current best; the distinct ballot-matching vehicle
collapses. Certified reduction + two sub-cases stand; MID-core itself remains open.)

## Approach: ballot-matching (framing J — GAP MID-core via an explicit weighted debit→credit
transport / Hall certificate, NOT a scalar potential)

Target (the whole claim): minimax D = u_n = 1/(2^{n+1}−1), c(n)=2^n/(2^{n+1}−1), both bounds.
Distinct intended contribution: a **non-inductive, certificate-style** proof of the lower exchange
GAP MID-core by an explicit measure-preserving map from the walk's overshoot ("debit") mass to its
deficit ("credit") mass, with a Hall/transportation feasibility condition supplied by the ladder —
rather than a scalar monovariant/potential (parity-measure, whose entire family was refuted R10).

### Reduction (imported, exact — all certified)
By Lemmas R, M/T, TB, MID, ONE-REC, CLIP the lower bound residual is the a=0 (top-shredded) case,
`|F|≥3`, all pieces `≤2^{n−1}`, where `S=F⊔B`, `F` = fragments of `2^n` (each `≤2^{n−1}`,
`ΣF=2^n`), `B` = a `≤(n−1)`-cut refinement of `C_{n−1}` (each piece `≤2^{n−1}`, `ΣB=2^n−1`). Read the
descending merge `v_1>…>v_m` with steps `e_i=±1` (+1 iff `v_i∈F`), partial sums `S_i=Σ_{j≤i}e_j`,
gap lengths `w_i=v_i−v_{i+1}` (`v_{m+1}=0`). Then (certified):
- `D(S) = Σ_{i odd} w_i`,
- `∫g = Σ_i S_i w_i = ΣF−ΣB = 1`,
- **GAP MID-core ⟺ `Σ_i c_i w_i ≥ 0`, `c_i := 1[i odd] − S_i`** (every `c_i` an even integer, since
  `S_i≡i (mod 2)`), equivalently the CLIP τ=0 order-statistic transport face
  **`Σ_{F even rank} v ≤ Σ_{B odd rank} v`**.
Credit set `𝒫={c_i>0}`, debit set `𝒩={c_i<0}`; the target is `Σ_{𝒫}c_iw_i ≥ Σ_{𝒩}|c_i|w_i`.

---

## Round 11 — the mandated FIRST ACTION and its DECISIVE (negative) outcome

Per the dispatch and outline-reviewer guardrails I first constructed the explicit transport BY HAND /
by numeric min-cut on the sharpest known adversarial witness and on n=3..6 random a=0 instances,
BEFORE attempting a general proof. This de-risking step **falsified the ballot-matching mechanism**.

### The worked n=7 CLIP witness (the field's first explicit instance)
`F = {63.0119, 62.8559, 2.1322}` (`ΣF=128`, `|F|=3`), `B` a valid 12-piece refinement of
`C_6={1,2,4,8,16,32,64}` (`ΣB=127`), e.g. `B={1,2,2.5,1.5,5,3,10,6,20,12,40,24}` (cuts of
`4,8,16,32,64`). Descending merge and the walk:

```
rank  v        col  S_i  c_i
 1    63.012   F     1    0
 2    62.856   F     2   -2    <- the ONLY debit  (F at even rank)
 3    40.000   B     1    0
 4    24.000   B     0    0
 5    20.000   B    -1   +2 } 
 6    12.000   B    -2   +2 }
 7    10.000   B    -3   +4 }  all credits (B at odd rank),
 8     6.000   B    -4   +4 }  spread over EVERY scale from 20 down to 1
 9     5.000   B    -5   +6 }
10     3.000   B    -6   +6 }
11     2.500   B    -7   +8 }
13     2.000   B    -7   +8 }
14     1.500   B    -8   +8 }
15     1.000   B    -9  +10 }
```
`D(S)=32.02≥1`, `cw=Σc_iw_i=31.02≥0`. The **entire debit** is the single term at rank 2 (value ≈62.9,
`|c|w = 2·(62.856−40)=45.7`); the credit that must absorb it is distributed across values `20,12,10,…,1`
— i.e. from the top scale down to the bottom scale. There is NO local scale-neighbourhood of the debit
containing enough credit: the debit at scale ~5 must reach credit at scales 4,3,2,1,0. This instance
alone shows the transport is irreducibly GLOBAL.

### The four structured/inspectable certificate families ALL FAIL (adversarial scan, n=3..6)
For a Hall/transport proof to have content, the debit→credit adjacency must be a *structured,
inspectable* object (else "complete-bipartite adjacency is feasible" is just a restatement of `cw≥0`).
Every natural structured adjacency was tested and refuted:

| candidate certificate | meaning | failure rate |
|---|---|---|
| prefix sums `Σ_{i≤k}c_iw_i≥0` | charge each debit to EARLIER credit | 8.5% (worst −29.6) |
| suffix sums `Σ_{i≥k}c_iw_i≥0` | charge each debit to LATER credit | 30.4% (worst −21.8) |
| interval-Hall on dyadic VALUE-scale bands | HALL-ENDPOINT: debit→credit at same/nearby scale | **49.1%** (worst −26.1) |
| value-dominating injection `F_even→B_odd` | greedy nested matching, `k`-th largest `F_e ≤ k`-th `B_o` | 49.6% (worst −13.0) |

(20000–40000 admissible a=0 refinements each; `cw≥0` itself never violated, min `cw=5·10^{−4}`.)

- **Prefix and suffix both fail** ⇒ the transport is neither forward nor backward directional; a debit
  must be chargeable both up and down the order. (Reconfirms the R8 "prefix fails 27%" fact.)
- **Interval-Hall on dyadic scale bands fails 49%** ⇒ the outline's `HALL-ENDPOINT` mechanism
  ("Lemma ONE-REC caps each scale-group to ≤1 F-fragment, so the debit accruing before the next
  ladder-forced B-crossing is bounded by that fragment's mass, which the crossing repays") is FALSE:
  the credit that repays a debit is NOT located at the same or a coarser scale — it sits at arbitrarily
  finer scales, typically near the bottom of the ladder (exactly the `n=7` witness picture).
- **No value-dominating injection** ⇒ the aggregate `Σ_{F even}≤Σ_{B odd}` holds with NO pointwise
  domination; it is a genuine aggregate (ballot-type) inequality, not a matching of individual masses.

### GAP-TERMINAL premise is FALSE
The skeleton's `GAP-TERMINAL` rests on `S_m=|F|−|B|<0` ("B refines the full ladder so `|B|≥|F|`, the
walk must end net-negative, supplying guaranteed terminal credit = the def(G) budget"). This is
**false**: over 2000 random a=0 refinements the terminal value `S_m` takes values
`{+1:655, −1:455, 0:316, −3:209, −2:180, …}` — it is `+1` most often. Indeed the *tight* minimiser
(`B` = uncut ladder `|B|=n`, `F` = `n+1` fragments interleaving the tail, `D=1` exactly) has
`|F|=|B|+1`, so `S_m=+1>0`: the walk ends ABOVE baseline precisely in the extremal case. There is no
"forced terminal descent," so the defect-Hall deficiency budget the skeleton invokes does not exist.

### Induction-on-|F| by merging F-fragments also fails
An alternative non-transport route — reduce `|F|` toward the certified `|F|=2` base by merging two
F-fragments while keeping `D` non-increasing — was tested: in 7.3% of instances **no** valid pair
merge (sum `≤2^{n−1}`) is `D`-non-increasing (merging the two smallest fails 22%). So there is no clean
`|F|`-monotone reduction to the base case either.

### Conclusion: the ballot-matching vehicle COLLAPSES
The only transport that is feasible for this inequality is the complete-bipartite one, whose
feasibility (total credit ≥ total debit, i.e. `cw≥0`) is *logically identical to the target itself*.
Every structured, inspectable adjacency — directional, dyadic-scale-local, or value-dominating — is
refuted, and the terminal-descent budget does not exist. Per the outline-reviewer's explicit
instruction ("if the min-cut does not sit on a structured non-prefix set the framing is vacuous… if
ballot-matching collapses this round, declare it collapsed, do not ship it"), I declare the
distinct-mechanism matching certificate **refuted**, and do NOT dress the aggregate inequality up in
Hall language as a fake proof. This is the honest analogue, one wall down, of R10's refutation of the
whole scalar-reserve family: after R10 (scalar family dead) and R11 (structured-matching family dead),
GAP MID-core has NO surviving structured lower lever.

---

## Open gaps
- **GAP MID-core (unchanged, still open).** `Σ_i c_i w_i ≥ 0`, equivalently `Σ_{F even}v ≤ Σ_{B odd}v`,
  for every a=0 refinement with `|F|≥3`. Confirmed true (min `cw≈0`, tight) but **irreducibly
  aggregate**: no scalar potential (R10), no structured transport/Hall certificate (R11, this round),
  no `|F|`-monotone induction closes it. The next attack must be a genuinely new GLOBAL mechanism — a
  direct aggregate ballot / cycle-lemma argument on the reachable word, or a majorization/exchange on
  the F-partition against the fixed ladder B — NOT a scalar and NOT a structured matching.
- **GAP-HALL / HALL-ENDPOINT — REFUTED this round** (dyadic-scale interval-Hall fails 49%). Do not
  retry local scale-adjacency.
- **GAP-TERMINAL — REFUTED this round** (`S_m=|F|−|B|` is `+1` in the tight case). Do not retry the
  defect-Hall terminal-descent budget.

## Upper bound
Deferred to the field's upper slug (breakpoint-vertex); this approach's intended contribution was the
lower exchange only.

## Approaches tried
- (round 8, new) skeleton: GAP MID-core recast as weighted debit→credit transport with a Hall
  feasibility condition from the ladder. Registered.
- (round 10) re-planned GAP-HALL via aimo-0129 endpoint-splitting (verify feasibility scale-by-scale
  using ONE-REC's ≤1-fragment-per-scale cap). Skeleton only.
- (round 11) **executed the mandated FIRST ACTION (explicit transport construction) and REFUTED the
  vehicle.** Worked the n=7 CLIP witness explicitly (field's first worked matching instance) + n=3..6
  adversarial scans. DECISIVE negatives: (i) HALL-ENDPOINT local dyadic-scale interval-Hall fails 49%
  — the credit repaying a debit is globally spread to arbitrarily finer scales, not same/coarser;
  (ii) GAP-TERMINAL false — `S_m=+1` in the tight case, no forced terminal descent; (iii) prefix (8.5%)
  and suffix (30.4%) directional transports both fail — non-directional; (iv) no value-dominating
  injection (49.6%) — the inequality is aggregate, not a pointwise matching; (v) no `D`-non-increasing
  `|F|`-merge in 7.3% — no clean induction on `|F|`. The distinct matching MECHANISM collapses (only
  complete-bipartite adjacency is feasible ⟺ the target itself). Recommend **RETHINK/prune**: the
  lower wall now has no surviving structured lever and needs a genuinely new global framing.

## Current best
The certified reduction stands: GAP MID-core `⟺ Σ_ic_iw_i≥0 ⟺ Σ_{F even}v≤Σ_{B odd}v` (via certified
Lemmas R, M, MID, OSR, CLIP), plus the two closed sub-cases — `g≤1` everywhere (certified Lemma
OSR-cap, Abel summation) and `D(F)=0` even-multiplicity F (Lemma SPLIT, `D(S)≥|D(F)−D(B)|=D(B)≥1`).
The residual (`|F|≥3`, `g` reaches `2`) is the same aggregate inequality as before.

**Net round-11 result: the ballot-matching vehicle is refuted at the mechanism level** — this is a
negative structural result, not a step toward the proof. Both natural non-scalar candidate families
for MID-core (scalar reserves R10; structured matchings R11) are now exhausted. Orchestrator note:
the lower wall requires a seed of a genuinely new global mechanism next round (aggregate ballot /
cycle-lemma on the reachable word, or F-partition majorization vs the fixed ladder), not another
variant of transport or potential.

## Promotable lemmas
None new proved this round (the round's content is a mechanism refutation, not a lemma). The refutation
facts (HALL-ENDPOINT local-scale interval-Hall fails 49%; GAP-TERMINAL `S_m=+1` in the tight case;
prefix/suffix/dominating certificates all fail) are recorded here and in run_state Rules for future
rounds; they are negative results, not certifiable lemmas.
