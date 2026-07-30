# proof-builder role memory

ALWAYS: for cut-and-claim / alternating-selection games, the value = odd-rank sum (Lemma G, pairing strategy) and the discrepancy D = O−E has a clean level-set form D = meas{t: #(pieces>t) odd} = alternating sum; a single split toggles N-parity exactly on (0,x)∪(L−x,L), giving |ΔD|≤2·min(x,L−x). This is the order-aware certificate when separable weights fail (imo-2026-03).

## imo-2026-03 (IMO 2026 P3, stick-cutting claim game), round 1
ALWAYS: reduce this game to discrepancy D via Level-Measure Formula D=λ{t:#(pieces>t) odd}
  and the Cut-Flip Lemma (a cut of ℓ at x flips parity of N(t) on [0,x)∪(ℓ−x,ℓ)); these
  turn the whole problem into parity-covering and are clean+provable (round 1).
NEVER: try to cap Liu with a bisection-only Xiang strategy — Lemma SD (min over subsets
  D(T) ≤ u) is FALSE for n≥2 (max≈0.165>1/7 at n=2). Xiang needs unequal cuts; upper bound
  is the true open crux (round 1).
  n≤4); Case A (top piece uncut ⇒ Liu total ≥ g=(1+u)/2) is clean; Case B needs a
  cut-budget-refined induction to beat parity cancellation — still open (round 1).

## imo-2026-03 round 2 (GAP U upper bound)
ALWAYS: Lemma F — after Xiang's cuts, final odd-level set = O_0 △ F_1 △...△ F_k (symmetric
  difference of Liu's odd-set with the flip-sets F_j=[0,x_j)∪(L_j−x_j,L_j)); parities add mod 2
  regardless of cut order/nesting. Turns Xiang's problem into exact parity-covering. Bisecting a
  piece (F=[0,ℓ)) makes it parity-INVISIBLE even under later cuts ⇒ D=D(remaining pieces). This
  unconditional bisection-invisibility is the engine (round 2).
  which is ≤u_n IFF ℓ1≥c(n)=(1+u_n)/2=1−u_n/u_{n−1}. So DOMINANT case (ℓ1≥c(n)) is a clean
  conditional inductive step; only the NON-DOMINANT case ℓ1<c(n) is open for n≥3 (round 2).
  bisect-recurse; balanced-top pin-a-copy-of-ℓ2 then two-piece one-cut on {ℓ1−ℓ2,ℓ3} with the
  pigeonhole "p+P=1−2ℓ2, P≤ℓ2 ⇒ min(p,P−p)≤1/7"; sub-threshold bisect ℓ1 (ℓ2<2/7). Verified 0
  violations / max 0.14266<1/7. Two-piece one-cut bound min(p,P−p) is the workhorse (round 2).

## imo-2026-03 GAP L, round 2
ALWAYS: rescale the dyadic lower-bound to INTEGER UNITS (×1/u_n): Liu={1,2,...,2^n}, bottom block
  becomes the LITERAL (n-1)-dyadic {1,...,2^{n-1}} with NO scaling factor, target D>=u becomes D~>=1.
  This exposed the clean exact recursion f(n,k)=f(n-1,k-1)=f_{n-k}, f_m=(2^{m+1}+(-1)^m)/3 — the
  equality-robust replacement for the refuted strict W(n-1,b)>u_{n-1} (round 2).
  random Case-B violations). The top can cancel bottom's odd-set below D_bot; the theorem D~>=1 still
  holds via the threshold decomposition, not via D>=D_bot (round 2).
ALWAYS: for top/bottom cancellation, split O_Y at threshold θ=2^{n-1}: bottom lives in (0,θ) so on
  [θ,∞) there is NO cancellation. Get D = D_top^> + D_top^< + D_bot - 2λ(O_Y^<∩O_Z), bound
  D >= D_top^> + |D_top^< - D_bot| (λ(cap)<=min). Closes ~85% (region |D_top^<-D_bot|>=1); residual
  balanced region needs a JOINT location bound on where O_Z sits inside O_Y^< (round 2).

## imo-2026-03 GAP L, round 3
ALWAYS: half-total single-crosser trick — when a sub-block Y sums to exactly 2θ (top piece =2·2^{n-1}),
  AT MOST ONE Y-part exceeds θ, so on (θ,∞) the level fn N∈{0,1} and λ(O∩(θ,∞))=(y₁−θ)⁺ EXACTLY
  (no cancellation). Gives D~≥(y₁−θ)⁺, closing y₁≥θ+1 cleanly — far weaker demand than C3's y₁≥2^n
  (round 3). This is the sharp cancellation-free reduction; the residual is only the doubly-balanced
  region y₁<θ+1 & |D_top^<−D_bot|<1−D_top^>.
  cutting the 2 into x,2−x gives odd-set (1,2−x)∪(0,x) reaching near 0; only λ(O) is controlled, never
  its location. The residual is intrinsically JOINT (interleaving of O_Y^< and O_Z), not one-sided (r3).

## imo-2026-03 GAP U, round 3
ALWAYS: Invisible-Pair Lemma — for any multiset R and v>0, D(R∪{v,v})=D(R) (two equal pieces add
  2·1[t<v], even, to N(t) everywhere). Generalizes bisection-invisibility. Gives two 1-cut removal
  ops: bisect ℓ_i (delete ℓ_i, total −ℓ_i); generalized pin ℓ_j into ℓ_i for any ℓ_i>ℓ_j (cut ℓ_i→
  {ℓ_j,ℓ_i−ℓ_j}, delete the ℓ_j-pair, total −2ℓ_j). D≤total ⇒ Residual-Total Theorem: force
  effective total ≤u_n ⇒ D≤u_n. Cases (i) ℓ1≥c(n)Σ and (ii) 2ℓ2≥c(n)Σ close for ALL n by one op+IH,
  c(n)=1−u_n/u_{n−1}=2^n/(2^{n+1}−1). Only balanced case max(ℓ1,2ℓ2)<c(n)Σ remains (round 3).
NEVER: try to close GAP U's balanced case with greedy "remove-max-total" or any black-box
  single-move+IH — PROVEN insufficient: its guarantee telescopes to r_k≤2/((k+1)(k+2))>u_k for k≥3,
  and deterministic max-greedy numerically violates u_k from n=3 (worst 0.074>1/15). Optimal (min
  over all B/P/free-pair sequences) DOES reach ≤u_n (verified n≤5, dyadic tight) but is non-greedy;
  needs a strengthened potential ψ(k,β), β=ℓ1/Σ, ψ(k,c(k))=u_k crediting post-move balance (round 3).

ALWAYS: for GAP U Case (iii), split on ℓ₁ vs Σ/2. Sub-region A {Σ/2≤ℓ₁<c(k)Σ} is CLOSED
  constructively (round 4) by the ACCUMULATOR schedule: pin the 2nd-largest into the largest
  repeatedly (free-delete equal pairs). Final residual = exactly 2ℓ₁−Σ, uses ≤k cuts, NO induction.
  Since c(k)=(1+u_k)/2, 2ℓ₁−Σ≤u_kΣ ⟺ ℓ₁≤c(k)Σ; tight at dyadic (ℓ₁=c(k)Σ→exactly u_k). The
  feasibility invariant "Σ(rest)≤accumulator" is self-restoring when ℓ₁≥Σ/2 (because new acc a−b ≥
  Σ(rest)−b ≥ every survivor, so acc stays the max) (round 4).
NEVER: use "pin largest against SMALLEST" for Case (iii) — REFUTED by the ground-truth solver
  (removes only 2ℓ_min/step; residual 4–14× u_k). The single Finding-1 trace's real pattern was the
  ACCUMULATOR (final=2ℓ₁−Σ), not smallest-first (round 4).
ALWAYS: run the empirical gate /tmp/round-N/rt_search.py (eval_f = optimal reachable residual) BEFORE
  writing any Case-(iii) schedule; extract the OPTIMAL op-sequence and read off the final-value
  formula. Region B {ℓ₁<Σ/2} defeats EVERY fixed simple schedule (accumulator, pair-tournament,
  half-bisect) for k≥3 while opt stays ≤0.72u_k — it is the genuine non-greedy core (round 4).

## imo-2026-03 GAP L, round 4 (telescope slug)
ALWAYS: for the Case-B lower bound, use M:=N_Y−N_Z. Since N_Y+N_Z≡N_Y−N_Z (mod2), D̃=∫1[M odd];
  since sum(Y)−sum(Z)=2^n−(2^n−1)=1 identically, ∫M=1, so target D̃≥1 ⟺ ∫1[M odd]≥∫M (clean, not
  pointwise). Merged descending order with prefix imbalance c_i gives EXACT identity
  D̃−1=Σψ(c_i)Δw_i, ψ(c)=1[c odd]−c, verified 7e−15 (round 4). This is the clean signed-sum form.
ALWAYS: Termwise Lattice Lemma — if the merged descending order of Y⊎Z has #T−#B≤1 in every prefix
  (maxc≤1) then D̃≥sum(Y)−sum(Z), termwise since ψ(c)≥0⇔c≤1. This is RIGOROUS and closes ALL tight
  (D̃=1) GAP-LB′ configs (they all have maxc≤1; verified 4e5 samples). The residual maxc≥2 has slack
  (min≈1.017) but infimum→1, so no crude estimate closes it — needs Z's dyadic anchors (round 4).
NEVER: expect the general merged-order Lemma T to close maxc≥2 — it does not invoke Z's cut-tree.
  The maxc≥2 residual (T-run deficit ≤ anchor surplus) genuinely needs the Structure Lemma: Z's
  uncut dyadic anchors z>y₁ open the merge with c=−1 excursions of definite width (round 4).

## imo-2026-03 dyadic-discrepancy notes (round 4)
ALWAYS: use exact Fraction arithmetic in the RT solver (float memoization gave phantom
  free-delete matches); /tmp/round-4/exp*.py have the clean exact versions (because float
  eval_f in rt_search.py mis-detects equal pairs, round 4).
NEVER: propose a one-parameter potential ψ(k,β) for RT Case (iii) — the pin recursion depends
  on ℓ_2,ℓ_3 individually, not β; it provably does not close (verified round 4).
ALWAYS: Case (iii) split ℓ_1≥Σ/2 vs <Σ/2 — the ≥ half closes cleanly via Pivot Lemma
  (subtract all others into ℓ_1, residual 2ℓ_1−Σ<u_kΣ, exactly k ops); only ℓ_1<Σ/2 open
  and it needs adaptive-pivot/pin-created coins, not a single pivot (round 4).


ALWAYS: for imo-2026-03 GAP-L, the merged-order signed sum (♦) reduces EXACTLY to the super-level
count D̃−1=2(Σ_j|B_{2j-1}|−Σ_j|A_{2j}|), A_k={M≥k},B_k={M≤−k} (proved via ψ(c)=−2⌊c⁺/2⌋+2⌈c⁻/2⌉);
deficit E_A≤Σy_{2j} and lives on (0,θ). Clean but the anchor lower bound on O_B (surplus) is the SAME
wall as telescope's Step 5 — the two GAP-L mechanisms genuinely share it (round 6, reviewer predicted).
NEVER bound the surplus O_B by a Y-only or scalar-of-Z quantity — deficit budget Σy_{2j} is provably
too loose (tie config n=4 Y=(8,3,3,2) Z=(8,2,2,2,1): E_A=1 but Σy_{2j}=5, O_B=1); needs Z's cut-tree
anchor placement (round 6).

ALWAYS: for imo-2026-03 GAP-L residual, the compensation is a GLOBAL sum across dyadic scales, NOT a local per-anchor/per-run match — the survival-function (measure) domination {Z odd-pos} over {Y even-pos} fails on 21% of Case-B configs (round 6). Any "match each run to an anchor" outline step is refuted; target the global inequality (♠≥0) ⇔ even-rank sum E(F) ≤ 2^n−1.
NEVER: assert a strict slack >1 on maxc≥2 for imo-2026-03 — D is tie-invariant and the infimum is exactly 1, attained at exact-tie configs (n=4, Y=(8,3,3,2), Z=(8,2,2,2,1)); prove non-strict (round 6).

ALWAYS: for imo-2026-03 GAP-U (upper bound), Xiang's MIN reachable effective total = min over ε∈{-1,0,1}^m of |Σ ε_i ℓ_i| (verified exact vs op-DP, 4000 instances, 0 diff). Then subset-sum PIGEONHOLE: 2^{n+1} subset sums in [0,Σ], min consecutive gap ≤ Σ/(2^{n+1}-1)=u_nΣ; symmetric-diff pattern realized by a Realizability Lemma (bisect zeros; repeatedly pin an opposite-signed pair) in ≤n ops. This closes the ENTIRE upper bound for all n in ~1 page, superseding the whole RT/pin-top-2/potential-ψ casework the outline demanded. Lesson: when a residual sub-case resists fixed schedules, look for a GLOBAL reachability characterization (all signed sums) + pigeonhole, not a smarter fixed first move (round 6).
NEVER: chase a "smarter fixed first move / two-parameter potential" for an op-reachability problem when the true optimum is a global choice — the k=4 near-miss (pin-top-2 ratio 1.039) killed every fixed-first-move rule but vanishes once you optimize the sign pattern globally (round 6).

## imo-2026-03 GAP U (round 6, dyadic-discrepancy-euclid)
ALWAYS: check whether a claimed "op-budget" gap is even binding before chasing it — for RT(k) any single-coin signed-subset play uses EXACTLY k ops (k+1-s deletes + s-1 pins), so budget is never the constraint; the real crux was reachability (because round 6, the reviewer's Euclidean-chain-overrun fear was a non-issue).
ALWAYS: verify reduction equalities with the exact ground-truth DP before building on them — solver-min == min-signed-subset == min-caterpillar EXACTLY (0/12000, exact Fraction) reframed the whole upper bound as a subset-sum discrepancy (because round 6 this pigeonhole on 2^{k+1} subset sums gives <=u_kSigma universally, closing the discrepancy half for ALL cases, not just region B).
NEVER: conflate "pigeonhole on reachable values" (refuted mesh) with "pigeonhole on the 2^{k+1} subset sums" (correct, elementary) — they are different objects (round 6).
NEVER: assume "value <= min piece => reachable by iterated abs-diff" inducts by peeling smallest with the same IH — the subproblem needs reachable values ABOVE its own min (e.g. 24 in Reach({44,20})), so a naive IH breaks; needs the full recursive Reach characterization (round 6 open gap).

## imo-2026-03 GAP U (round 7, dyadic-discrepancy)
ALWAYS: the load-bearing link "D(actual final multiset) = D(effective multiset)" in the subset-sum
upper bound is the physical decomposition P = E ⊎ ⋃_s{v_s,v_s}: EACH op leaves exactly one equal
pair physically (bisect→two halves; pin b into a→ original b + new b; free-delete→the pair), IP
strips them all without changing the odd-set. Verified end-to-end: physical mass conserved =Σ, true
D≤u_n, 0 violations, exactly n ops (round 7). Make this explicit or a reviewer will flag "effective
total ≠ real position."

ALWAYS: for imo-2026-03 GAP L, target the aggregate `O_B≥E_A` — the termwise super-level pairing `|A_{2j}|≤|B_{2j-1}|` is PROVEN FALSE (explicit witness n=4,a=2,b=2), so no level-matched/monotone-pairing proof can work (because natural sub-route killed, round 7).
NEVER: propose a "super-level pairing" or any scalar/count summary of Z as a GAP-L closer — both refuted; the tight maxc>=2 slice is b>=1 near-tie only (b=0 has slack >=1.029), so any real proof needs Z's cut-fragment interleaving or a genuinely different framing (LP-duality / amortized cut-sequence potential), not a 4th attack on O_B>=E_A (round 7).

## imo-2026-03 GAP L, round 7 (telescope slug)
ALWAYS: use the EXACT threshold-split identity D(F)=(y1-θ)⁺+λ_{(0,θ)}(O_Y△O_Z), θ=2^{n-1} (parity=XOR
  + ≤1 Y-fragment exceeds θ since sumY=2θ); it reduces Case B to the BOUNDED-mass localized inequality
  λ_{(0,θ)}{M odd}≥∫_{(0,θ)}M=1−β (M=N_Y−N_Z, β=(y1−θ)⁺∈[0,1]). Cleaner/stronger than (★★) (round 7).
NEVER: use a TOP-DOWN reserve of Z for the GAP-L residual — "Z's odd measure leads its even measure
  from the top" is FALSE (7306/4e5, worst −22.5); in the tie config n=4 Y=(8,3,3,2) Z=(8,2,2,2,1) the
  whole surplus is the NEAR-0 count-parity band (0,1) (|Z|=5 odd vs |Y|=4 even) and the top anchor 8
  CANCELS in O_Y△O_Z. Surplus is bottom-inclusive/global, not a top-anchor reserve (round 7).

## imo-2026-03 GAP U (round 7, dyadic-discrepancy-euclid) — UPPER BOUND CLOSED
ALWAYS: to realize the min signed sum as a single reachable coin (the round-6 open §D), use the
SIGN-PAIRING induction, NOT peel-the-smallest: pick a +/- pair from any minimizer, contract to coin
|x_p-x_q| (one pin), and the contracted problem's min signed sum EQUALS the original's (contracted
patterns = original patterns with ε_p=-ε_q; minimizer feasible). Gives Theorem R: min abs-diff tree
= min ±1 signed sum, exactly (0/2000 exact Fraction). This closed the whole GAP U in one page,
replacing the failed peel-smallest IH (round 7).
ALWAYS: the "Liu uses fewer than n marks" (a<n, a+1<=n pieces) upper-bound case is TRIVIAL — Xiang
bisects ALL a+1<=n pieces -> all invisible pairs -> D=0. Only a=n (n+1 pieces, budget n) needs the
subset-sum+Theorem-R construction, which uses EXACTLY n ops (n+1-s bisects + s-1 pins). Don't try to
reach the deep u_n pigeonhole from few pieces (creation+realization overruns budget ~2x) — bisecting
to D=0 is the clean route (round 7).

## imo-2026-03 GAP L, round 8 (even-rank-doublecount slug)
ALWAYS: the even-rank sum has level form E(F)=∫⌊N/2⌋dt, and the discrepancy has the SCALE-PARITY XOR
  identity D̃(F)=∫⊕_j 1[N_j(t) odd] dt (N_j = level fn of scale j = fragments of 2^{n-j}); verified
  0/20000 exact. This is a clean game-free/measure-free restatement that keeps each scale separate
  (NOT a scalar summary). Trivial ⌊N/2⌋≤N/2 gives only E≤2^n-1/2 (D̃≥0); the missing 1/2 = D̃/2 is
  the WHOLE content (round 8).
NEVER: expect a bivariate/scale-graded generating function (RUF at x=-1 with a q-scale variable) to
  close E(F)≤2^n-1. Cheap-kill REFUTES it: ∫⊕s_j is non-additive across scales, and the prefix-budget
  region {Σ_{j≤k}a_j≤k ∀k} has HUGE margin (min D̃=4/8/9 for n=3/4/5) while ALL tight configs are
  FRONT-LOADED (budget on top scales, prefix over-budget so IH unavailable). The (♣)-not-pointwise
  wall reappears verbatim in the scale grading; the genfn mechanism is a RETHINK (round 8).

## imo-2026-03 GAP L, round 8 (cut-sequence-potential slug)
ALWAYS: before building an amortized/potential monovariant to prove a min-over-adversary bound,
  check the Reserve⇔Target equivalence: an admissible reserve R (R>=0, R(.,0)=0, root-tight
  R(root,n)<=value-1, one-cut charging R(P,b)-R(P',b-1)>=drop) EXISTS iff the target inequality
  itself holds (value-function R*=val-minreach is the canonical vacuous witness). So a sequential
  monovariant over the move sequence gives NO leverage unless you can GUESS an explicit closed-form
  R with a locally provable one-cut inequality. This killed cut-sequence-potential (and explains
  why the sequential budget-count induction-recursion died) for imo-2026-03 (round 8).
NEVER: for imo-2026-03 GAP L, propose a reserve that is a function of (D̃, budget) only (refuted:
  same (11,1) gives R*∈{6,7,8}) or linear-in-budget/summed-magnitude (refuted: R*(F0,b) concave
  0,6,8,10,10 not b·const) — both dead; any admissible reserve needs full toggle-set geometry AND
  is provably no easier than the theorem (round 8).

## imo-2026-03 GAP L, round 8
NEVER: try to close Σψ(c_i)Δw_i≥0 by a greedy/bounded-window nonneg-BLOCK TILING (crux aimo-0626).
  A consecutive-nonneg-block tiling exists IFF the total≥0 (single block [1,m]) — so it is CIRCULAR;
  and there is NO local certificate: a single depth-2 deficit can exceed each adjacent surplus
  separately (witness n=3 Y=(3.382,2.553,2.065) Z=(4,1.042,1,0.958), s_4=−2.046 vs ±1.237/1.916),
  needing a full-list window. Both-directional greedy fails 222/2e5 (round 8).
ALWAYS: identity (△△): ∫(⌊M+/2⌋−⌈M−/2⌉)=½∫M−½D̃ ⇒ ALL layer/summed/(♠)/(△⋆) forms are pure
  measure-algebra restatements of D̃≥1; trivial layer bound gives only D̃≥0 (off by ½ = the O≥S/2
  gap). The missing ½ MUST come from the dyadic budget Σa_j≤n entering NON-locally — no reshuffle of
  the profile M closes it (round 8). Merged-order block/window/matching family is exhausted.

ALWAYS test "does plain IH suffice" for an induction step by feeding an ARBITRARY object satisfying only the IH conclusion (not the full structure) into the step — if it breaks, the loaded invariant is genuinely necessary (imo-2026-03 GAP L peel: arbitrary altsum>=1 F' gave D=0.146<1, real dyadic refinement gave min=1). Round 9.
NEVER claim a peel/measure decomposition escapes the R8 "equivalent-to-target" meta without checking: D̃(F)=D̃(π0)+D̃(F')-2·overlap re-derives the certified (△⋆) exactly; only the INDUCTION on n (coupling π0's partition with recursive F') is new, not the measure identity. Round 9.

## imo-2026-03 GAP L, round 9 (vertex-integrality-parity)
ALWAYS: the Parity Lemma is the clean +1 injector for GAP L: any INTEGER feasible config has odd
  total 2^{n+1}-1, so D~ = ΣF - 2E ≡ ΣF ≡ 1 (mod 2), and with D~>=0 gives D~>=1. Hypothesis is odd
  TOTAL not odd part-count. This is the finishing device for ANY approach reaching an integer optimum.
NEVER: claim cell-polytope vertices are integral (B2/TU) — REFUTED R9: minimizing vertices are often
  fractional (4,2,1/2,1/2), per-cell min VALUES can be non-integer (1.667), and rounding-in-cell
  OVERSHOOTS (LP min 2 but integer min 3). TU of partition-rows+order-rows is FALSE.
ALWAYS: the real GAP-L crux for the extremal route is GLOBAL not cell-local: min over the whole
  feasible union = min over integer configs (=1), even though it FAILS cell-by-cell (fractional
  vertices live only in cells whose min >1). For n<=3 every OPTIMAL(value-1) cell has an integer
  vertex minimizer (exact LP). The obstruction to per-block rounding: an odd fractional tie-block of
  value v needs group-block-sums n_g*v to stay fixed & integer — impossible if n_g*v fractional, so
  integralization needs CROSS-BLOCK global mass transfer. Reduction "integer minimizer exists" is
  NON-circular (about WHERE min lives, not its value) but genuinely global — still open.

## imo-2026-03 GAP-L, round 10 (peel-integral-exchange)
ALWAYS: D̃ = descending alternating sum of the distinct ODD-multiplicity values (even tie-blocks
  contribute 0): D̃=Σ(-1)^{p-1}u_{(p)}, u_{(1)}>u_{(2)}>... over values of odd mult. Proof: per-block
  Σ_{t=0}^{r-1}(-1)^t=1[r odd]. Verified 0/5e4. Clean new form (Lemma OB), natural monovariant potential.
ALWAYS: at a minimizing cell-vertex, #distinct part-values K<=n+1 (LP active-constraint count
  m<=(n+1)+(m-K)); reduces GAP-IMR to the FINITE "some optimal vertex is integer" (GAP-IMR'). Does NOT
  give integrality (fractional even-block vertices exist: (4,2,1/2,1/2), K=3).
NEVER: expect "cross-scale mass transfer" to integralize — mass CANNOT cross a scale (each Σπ_j=2^{n-j}
  is a HARD equality). Only cross-scale lever is BUDGET reallocation (merge small-scale parts), and a
  merge of an even fractional block can INCREASE D̃ (({1/2,1/2}->{1}) sends 2->3 at (4,2,1/2,1/2)). So a
  non-increasing integralization of an optimal vertex is NOT constructed — GAP-IMR' still open (round 10).
NEVER: think "optimal-face evenness" (all fractional blocks even) closes it — evenness => D̃ integer but
  NOT >=1 (continuum even blocks carry fractional values summing to odd total); integrality (Parity Lemma)
  is irreducible, not evenness (round 10).

ALWAYS use the exact identity D̃(F)=1−2∫_{(0,θ)}⌊M/2⌋ (M=N_{π_0}−N_{F'}) to state GAP L Case B: it
reduces the whole lower bound to the single scalar inequality ∫_{(0,θ)}⌊M/2⌋≤0, tie-attained (found
& proven round 10, imo-2026-03; supersedes the (△⋆) measure form). Layer form
∫⌊M/2⌋=Σ_k(λ{M≥2k}−λ{M≤−(2k−1)}); even/odd threshold asymmetry = the missing ½.
NEVER test GAP-L configs without enforcing the JOINT budget Σa_j≤n across ALL scales (round 10: an
F'-with-full-budget-n−1 probe gave many false I_n>0 — the budget is non-local; it enters ONLY via
M(0⁺)≤1). Use exact Fraction, never limit_denominator.

ALWAYS: for imo-2026-03, remember GAP-IMR ("min D̃ attained at integer config") is LOGICALLY
EQUIVALENT to the target D̃≥1, not a reduction — because integer-min=1 is already proved and integer
configs are feasible (min≤1). Any "reduce to integer minimizer" plan is the whole lower bound in
disguise (proven round 10, exact).
NEVER: try to close GAP-IMR by a local D̃-non-increasing "smoothing/descent" from a fractional
minimizer — at isolated fractional vertices (e.g. n=2 {4,2,1/3,1/3,1/3}, D̃=7/3, the odd block IS a
whole group) every feasible move strictly increases D̃, so no descent exists; and for n≤3 no
fractional minimizer exists at all (0/90, 0/1134 min vertices fractional) so the scheme is vacuous
and ungroundable (round 10). The real-valued content belongs to the peel induction, not rounding.

## imo-2026-03 GAP L, round 11 (allocation-vertex-corner)
NEVER: prune the GAP-L allocation space by the scalar b=Σ_{j≥1}a_j — the tie I_n=0 is reached at
  b=0 AND b=2 (a=(1,2,0,0,0), π0={8,8}, F'={5,4,2,2,1,1}) AND b=3 (a=(1,2,1,0,0),
  F={8,8,3,3,2,2,2,2,1}), all EXACT (D̃=1). So any "φ(b)<0 for b≥1 / prune to small-b corner"
  engine is REFUTED; b carries no separating power for the tie set (verified exact Fraction, r11).
ALWAYS: the positive layers of I_n are controlled by π0's even-ranked parts alone:
  P:=Σ_k λ{M≥2k} ≤ Σ_{k=1}^{⌊(a0+1)/2⌋} y_{2k} (since {M≥2k}⊆{N_{π0}≥2k}=(0,y_{2k}), y_{2k}≤y_2≤θ).
  Rigorous, tight, 0/20000 exact. Positive contribution needs a0≥2k−1; re-proves Case A on the +side.
  This is the FLOOR-language form of the banked r6 deficit bound E_A≤Σy_{2j} — still too loose alone,
  the matching lower bound on Q=Σλ{M≤−(2k−1)} needs F''s cut-tree (the shared wall) (round 11).

## imo-2026-03 GAP L base case, round 11
ALWAYS: for the b=0 extremal base case D̃(π_0⊎L)≥1 (L=uncut ladder), use the interleaving
  identity D̃(π_0⊎L)=1+2(Σ_blue_odd−Σ_red_even) [subtract colour-sign sum Στ_j w_j=Σπ_0−ΣL=1
  from D̃=Σ(−1)^{j−1}w_j]. It makes the base case EXACTLY (★) Σblue_odd≥Σred_even, tie=equality.
  Clean, fully proven, promotable (round 11).
ALWAYS: region {M=N_{π_0}−N_L≤1 on (0,θ)} closes ~88% of base configs unconditionally
  (⌊M/2⌋≤0 pointwise ⇒ I_n≤0). D̃(L)=(2^n−(−1)^n)/3 exact; DIFF shell |D̃(π_0)−D̃(L)|≥1 closes more.
NEVER: charge each even-rank red to a same-block blue via Σ_red_even≤Σⱼ⌈m_j/2⌉b_j — TOO LOSSY,
  sufficient cond Σblue_odd≥charge fails ~51% (round 11). The ladder-dominance closer needs
  cross-block/cross-k tail cancellation (a high odd-blue dominates a whole tail of lower even-reds).
NEVER: hold π_0 FIXED in a per-cut monovariant for the reduction-to-base (b→b+1) — FALSE ~30%
  (banked R11); it must be a slice-max statement with π_0 co-varying, and add cuts (never merge:
  merging even tie-blocks can RAISE D̃, {4,2,½,½}:2→3).
ALWAYS: for a "prove weak-majorization / uniform-in-t tail-charge" gap, reduce the continuum to a
  FINITE check via Φ(t)=Σ(v-t)^+ over the two multisets: Φ is piecewise-linear with convex kinks only
  at values of the majorizing multiset, so its min is at t=0 or such a value — turns "for all t" into
  ≤n rung inequalities (worked round 13, imo-2026-03 §11.6; cite HLP ramp form, prove ⟸ by t=y↓_k).
NEVER: expect a single-rung DOM charge to close Φ(b_i)≥0 for i≥2 (round 13): the shift term
  b_i(|BO(P_i)|-|RE(P_i)|) is a self-similar deficient (★) on scaled ladder 2b_i·L_{i-1} — the SAME
  wall as ladder-length-deficient-induction's generalised lemma; only i=1 (top rung, Φ(θ)=0) is local.

## imo-2026-03 GAP-L base slice (★), round 13 — CLOSED via ladder-length-deficient-induction
ALWAYS: for the base slice (★) Σblue_odd≥Σred_even (=Δ_n(π0)≥0, Δ_m(R):=½(D̃(R⊎L_m)−ΣR+2^m−1)=BO−RE),
  the mutual induction on ladder length m CLOSES: (P_m) #R≤m+1,ΣR≤2^m⇒Δ≥0 [Branch1 one red>θ: exact
  pair-removal Δ_m(R)=Δ_{m−1}(R∖y)→(P_{m−1}); Branch2 no red>θ: rung-peel Δ_m=2^m−1−ΣR−Δ_{m−1}→(Q_{m−1})];
  (Q_m) #R≤m+2,parts≤2^m,ΣR≤2^{m+1}⇒Δ≤2^{m+1}−1−ΣR [k=0 via D̃≥0 trivial; k≥1 red-peel
  Δ_m(R)=2^m−1−Σ(R∖y)−Δ_m(R∖y), need Δ_m(R0)≥y−2^m from (LB_m)]. The KEY that unlocked it (round 13):
  the DEFICIENT lower bound (LB_m) Δ_m≥min(0,2^m−ΣR) collapses to the TIGHT case (P_m) via D̃'s
  1-LIPSCHITZ continuity — shrink red total by ε=ΣR−2^m to hit Σ=2^m, apply (P_m)[Δ(R̂)≥0], then
  Δ(R)≥Δ(R̂)−ε=−ε. This is what defeats the eternal "off-by-½ at the tight config" that killed every
  crude-bound route for 10 rounds. All identities via LEVEL-MEASURE D̃=∫1[N odd] (tie-free).
NEVER: try to close (LB_m)/(Q_m) hard sub-cases with D̃≤max or D̃≥0 crude bounds directly — they miss
  by exactly ½/1 in a razor strip ΣR∈(2^m,2^m+1) (the problem's missing-½ localized). The Lipschitz
  shrink to the tight case is the ONLY thing that injects it. (round 13)
ALWAYS: D̃ is 1-Lipschitz — decreasing element values by total ε changes D̃ by ≤ε (each single move by δ
  flips parity on an interval of length δ). Turns any deficient-total discrepancy bound into its tight
  case. Reusable general tool. (round 13)

## imo-2026-03 b-lift, round 14 (absorb-rescale-induction)
NEVER: use ABSORB (Δ(R,Z)=θ+Δ(R⊎π_1,Z')) as a b-lift CLOSER — it is a bookkeeping TAUTOLOGY:
  R̄⊎F''=π_0⊎F' same multiset, so Δ_m(R̄,F'')≥−θ is LITERALLY D̃(π_0⊎F')≥1 (the original target).
  Proven exact R14. The "rescaled deficient bound" gives Δ≥−2θ, STRICTLY WEAKER than trivial D̃≥0
  (which gives −θ−½); target is −θ. So the outline's GAP-A1/A2 count-cap accounting is moot — even
  closed it yields −2θ. Whole content = the missing ½ at tripled mass 3·2^m against a refinement.
ALWAYS: refinement-blue max-peel D̃(P)=max(P)−D̃(P∖max) ⇒ Δ(R,Z)=y−ΣR+ΣZ−Δ(R∖y,Z) for global-max y
  works against ANY blue (generalizes certified (I3) off the full ladder). Peels big reds into the
  certified window ΣR≤2^{m+1} WITHOUT changing scale — but scale reduction m→m−1 still needs peeling
  F''s SPLIT top rung = split-rung (I1′). absorb-rescale is NOT independent of split-rung (round 14).

## imo-2026-03 b-lift, round 14 (split-rung-mutual-induction)
NEVER: propose a "split-rung-peel (I1′)" with a CLOSED alternating-sum correction and a sign-flipped
  Δ_{m−1} recursion — the clean form is FALSE (fails 3931/4000; witness m=2 R={1} Z={3/2,1/2,1}: true
  Δ=3/2 vs clean=3). The honest split-rung identity is just certified SD/PEEL:
  D̃(R⊎ρ_1⊎Z')=D̃(R⊎Z')+D̃(ρ_1)−2λ(O_{ρ_1}∩O_{R⊎Z'}); the residual is the odd-set OVERLAP term =
  GAP-P1 itself. Peeling one blue scale while fixing R doubles relative red mass (illusory "bounded
  mass"); dropping the overlap ≥0 telescopes to vacuous Δ≥½(D̃(R)−ΣR)≤0 (round 14).
ALWAYS: certified (I3) red-peel GENERALIZES to arbitrary blue Z with parts ≤θ, y=maxR>θ:
  D̃(R⊎Z)=y−D̃((R∖y)⊎Z) (parity flip on (0,y), N_{P'}=0 above y). Verified 0/4000. Reduces any
  blue=F' bound to the all-red-≤θ regime. Reusable — call it (I3′) (round 14).

ALWAYS: for imo-2026-03 GAP L, run the mandated exact-Fraction cheap-kill BEFORE proving — the bottom-band split's overlap is EXACTLY D̃(F_{≤τ})·1[|F_{>τ}| odd] (clean, real-valued), but its odd branch IS the certified DIFF/overlap wall; split-agnostic, dead (round 15).
NEVER: route the +1 through the Parity Lemma for imo-2026-03 unless the config is integer — z_min→0 kills the near-0 concentration on reals, and integer reduction (GAP-IMR) is proven equivalent-difficulty (R10, round 15).

## imo-2026-03 b-lift, round 15 (ladder-length-deficient-induction)
ALWAYS: the b-lift target D̃(π₀⊎F')≥1 is FALSE for "arbitrary refinement F'" — it NEEDS the global
  cut-budget Σa_i≤n (Xiang's n marks), non-local across rungs. Counterexamples (exact Fraction):
  π₀={2,2},F'={3/2,3/2} n=2 gives D̃=0 (unstructured); rung-sums + 7 cuts n=2 gives D̃=0 (no budget).
  Any b-lift statement MUST carry the budget explicitly. The outline/reviewer under-specified F' (r15).
ALWAYS: the budget-aware engine (P̂_m)/(Q̂_m) (a₀+b≤m, blue=budgeted refinement Σρ_i=2^{m-i}) CLOSES
  every case whose TOP blue rung is UNCUT: (A1) MAXPEEL Δ(R,F')=(2^m-1-ΣR)-Δ(R,F'')→(Q̂_{m-1}) [reds≤θ];
  (A2) (I2)-general Δ(R,F')=Δ(R∖y,F'') [one red>θ, top rung uncut]→(P̂_{m-1}); (A3) (I3′) red-peel.
  Verified 0 fails. Base slice (b=0) = special case all-rungs-uncut. Sole gap: CUT top rung (r15).
NEVER: peel a CUT top blue rung for the LOWER bound — (i) the cut-peel correction (C)
  Δ(R,F')=Δ(R,F'')+½θ+½D̃(ρ₁)-I_S does NOT flip Δ's sign (unlike MAXPEEL on an uncut rung), so it
  needs a LOWER bound on Δ(R,F'') while reds are oversized (ΣR up to 2·new-θ) — only (Q̂) upper bound
  available; (ii) I_S=λ(O_{ρ₁}∩O_W)=GAP-P1, scalar 0≤I_S≤D̃(ρ₁) telescopes vacuous (R14). The exact
  correction (C) carries the global below-p_r tail via E={N_{ρ₁} even}∩(0,θ), λ(E)=θ-D̃(ρ₁) (r15).

ALWAYS: on imo-2026-03 b-lift cut-top-rung leaf, verify any claimed I_S-bound is not just the target restated — the (†) I_S≤Δ(R,F'')+½θ+½D̃(ρ₁) rearranges (via mass identity D̃(W)=2Δ(R,F'')+ΣR−(θ−1) and even-complement λ(E∩O_W)=D̃(W)−I_S) to exactly D̃(R⊎F')≥1. The ΣR≤θ half closes cheaply (L̂B-inherit≥0 + I_S≤D̃(ρ₁)≤p₁<θ); only ΣR>θ is open and razor-tight (min Δ→0.062), so scalar ceilings are vacuous (round 16).

## imo-2026-03 b-lift, round 17 (ladder-length-deficient-induction)
ALWAYS: for the b-lift endpoint SigmaR=2^m, the CLEAN split is by the TOP RUNG of F' (uncut->A1/A2->
  (Q̂_{m-1})/(P̂_{m-1}) endpoints; cut-> (C) overlap wall), NOT by "has a red=θ vs not". S1 (SigmaR<=2^m-1
  trivial via D̃>=0) + S2 (Lipschitz (I4) fill to endpoint) SOLIDLY reduce the whole (P̂_m) to the single
  endpoint slice; these are stand-alone certifiable (round 17).
NEVER: use the "no red=θ => slack D̃>=13/12 (or ~1.12)" endpoint-forcing claim — REFUTED even on the
  cut-top-rung endpoint. Exact witness m=3: R={3,3,2}(ΣR=8=2^m,no red=θ=4), F'={2,2,2,1}(top rung {2,2}
  cut) gives D̃=1 exactly. Both the reviewer's 1.12 and the draft's 13/12 were false; the "no-θ-red"
  sub-case is razor-tight, so θ-red-peel+slack cannot close the endpoint (round 17).
ALWAYS: the anchor D̃(F')>=1 (<=m-1 cuts) is genuinely a (P̂_{m-1})-at-endpoint instance in its cut-top-rung
  branch (view ρ₁ as red R̄, ΣR̄=2^{m-1}); legitimate induction descent, NOT circular, but NOT an
  independent endpoint closer once θ-forcing is refuted. Its uncut branch (θ-D̃(F''), D̃(F'')<=ΣF''=θ-1)
  is unconditional (round 17).
