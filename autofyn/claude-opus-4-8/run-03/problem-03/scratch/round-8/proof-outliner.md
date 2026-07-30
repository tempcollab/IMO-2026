## imo-2026-03

Field of 4. Two sharpened walls, each getting its single best vehicle PLUS one genuinely
different-mechanism framing (per the collapse: lower = one ballot inequality shared by
parity-measure ≡ merge-interleave; upper = one tree-realizable subset-sum object shared by
breakpoint-vertex ≡ subset-sum-pigeonhole). I do NOT advance merge-interleave-pattern or
subset-sum-pigeonhole as parallel levers — the explorers proved each is the SAME inequality/object
as the best vehicle on its wall (single-gap trap). Instead each wall gets a genuinely different
attack: LOWER matching-certificate vs induction; UPPER construction vs existence.

Answer CONFIRMED (do not re-derive): c(n)=2^n/(2^{n+1}−1), minimax D=u_n=1/(2^{n+1}−1).
Import the 13 certified lemmas; do not re-prove.

---

parity-measure-potential: advance
Target: minimax D=u_n, hence c(n)=2^n/(2^{n+1}−1) (both bounds); this round closes the LOWER wall.
Technique: the ballot / signed-walk aggregate-compensation inequality (owns Lemma MID); best lower
vehicle.
Skeleton:
  1. Import certified reduction R/M/TB → lower bound reduces to GAP MID-core (a=0, |F|≥3). — done
  2. Round-8 walk encoding (math-explorer-lower-midcore): merge S=F⊔B descending v_1>…>v_m, steps
     e_i=±1, partial sums S_i, gaps w_i. Then D(S)=Σ_{i odd}w_i and ∫g=Σ_i S_i w_i=1 (Abel). —
     by Lemma MID(a,b) + the mod-2 walk fact S_i≡i.
  3. GAP MID-core ⇔ Σ_i c_i w_i ≥ 0, c_i:=1[i odd]−S_i (each c_i even). — algebra from step 2.
  4. Prove step 3 by aggregate compensation using Lemma ONE recursed: peel the top dyadic scale of
     B; each scale hosts ≤1 F-fragment, so the running deficit Δ(i)=Σ_{j≤i}c_j w_j cannot dip below
     a bound that the NEXT ladder-forced B-crossing repays; induct down the scales. — the open gap.
Key lemmas (claim + mechanism):
  - D(S)=Σ_{i odd}w_i = alternating sum of the merged order statistics — because S_i≡i (mod 2)
    always (every step ±1), so {g odd}=⋃_{i odd}(v_{i+1},v_i) is exactly the odd-rank gaps.
  - ∫g=1 — because Σ_i S_i w_i = Σ_j e_j v_j = ΣF−ΣB = 2^n−(2^n−1)=1 (superincreasing signature;
    certified MID(b)).
  - Σ c_i w_i ≥ 0 — because F can run ahead of the ladder baseline by ≤1 fragment per dyadic gap
    (Lemma ONE recursed), so every overshoot is repaid by the next forced B-crossing; the walk MUST
    end at S_m=|F|−|B|<0, guaranteeing terminal compensation.
Open gaps: step 4 (the aggregate-compensation induction on Δ(i) via Lemma ONE recursed). Steps 1–3
are certified/algebraic.
Cases to cover: |F|≥3 only (|F|=2 and 0≤g≤1 closed inside MID). Base of the scale-induction = the
top scale where Lemma ONE (not recursed) already applies.
Watch out for: the pure-integral version is FALSE (g≡2 on measure ½) — the ladder MUST enter. The
naive termwise condition "S_i≤1[i odd] for all i" is FALSE (explorer counterexample S_4=2 at n=3) —
the correct claim is the AGGREGATE Σc_iw_i≥0, never termwise. Do NOT resurrect the "O_B meets each
gap in ≤1 interval" invariant (refuted). Do NOT use the aimo-0298 split-and-average monovariant
(refuted R7).

---

ballot-matching: new
Target: minimax D=u_n, c(n)=2^n/(2^{n+1}−1) (both bounds); distinct contribution = the LOWER
exchange GAP MID-core by a matching certificate.
Technique: weighted transportation / Hall marriage on the signed walk — genuinely different
MECHANISM from parity-measure's induction (certificate vs recursion), same target inequality.
Skeleton:
  1. Same reduction + walk encoding as parity-measure (steps 1–3 above). — imported.
  2. Split indices: debit set 𝒩={c_i<0} (walk overshoots baseline), credit set 𝒫={c_i>0} (walk at
     or below baseline). Goal Σ_𝒫 c_iw_i ≥ Σ_𝒩 |c_i|w_i. — definition.
  3. Build an explicit transport T routing each debit at index i to strictly-later credit created by
     the next B-crossing at the same/coarser dyadic scale. — by Lemma ONE recursed.
  4. Verify the Hall/feasibility inequality scale-by-scale: debit accumulated above threshold τ ≤
     credit reachable ≤τ, plus the forced terminal descent (S_m<0, |B| large) absorbs any residue.
     — the open gap.
Key lemmas (claim + mechanism):
  - Debit is dominated by later credit — because ≤1 F-fragment per dyadic gap (Lemma ONE recursed)
    caps how far the walk can run ahead before the next −1 B-step forces repayment.
  - Transport is total — because the walk ends at S_m=|F|−|B|<0 with |B| large (ladder length), so
    terminal credit exists to absorb residual debit.
Open gaps: GAP-HALL (per-scale Hall feasibility) + GAP-TERMINAL (totality of the transport).
Cases to cover: |F|≥3, a=0. none else.
Watch out for: HONESTY FLAG — this shares the target inequality with parity-measure-potential and
merge-interleave-pattern; it is offered as the genuinely-different-mechanism second lower lever
(matching, no induction on n) so the wall has two independent attacks. If the reviewer judges it too
close to parity-measure, prune it and keep parity-measure as the single lower vehicle. Do NOT
develop it as if it were a new inequality — it is the SAME Σc_iw_i≥0 attacked by a certificate.

---

breakpoint-vertex: advance
Target: minimax D=u_n, c(n)=2^n/(2^{n+1}−1) (both bounds); this round closes the UPPER valley wall.
Technique: LP-vertex finiteness (Theorem VERT) + certified RL/VS → finite tie-pattern search for
Prop UV; best upper vehicle (owns VERT, RL, VS, R-UV).
Skeleton:
  1. Import R/M/U0/whole-tail-peel/R-UV → upper valley ⇔ min 𝓡(A) ≤ u_nL. — certified.
  2. By Lemma RL, 𝓡(A) = tree-realizable signed subset sums; by Theorem VERT the optimal Xiang
     response is a polytope vertex with ≤n+1 distinct values, so min 𝓡(A) is attained over a FINITE
     tie-pattern family. — certified VERT + RL.
  3. Prove Prop UV: over that finite family, min 𝓡(A) ≤ u_nL, profile-independently, using the two
     valley hypotheses a₁<L/2, a₂<β_nL to bound the best tie-pattern's leftover. — the open gap.
Key lemmas (claim + mechanism):
  - 𝓡(A) is a strict subset of {0,±1} signed sums (differences only, no sum of two positives) —
    because MATCH produces only x−y; certified RL. (So a naive 2^{n+1} pigeonhole is INVALID.)
  - ≥2 coordinated cuts are forced (adaptivity) — because single DELETE needs a_i≥c(n)L>L/2 and
    single MATCH needs y≥β_nL, both failing in the valley; certified VS.
  - Prop UV — because the dyadic cascade 2^n−2^{n−1}−…−1=1 telescopes to exactly u_nL and any valley
    profile admits a tie-pattern that does no worse (to be proved via VERT's finite vertex set).
Open gaps: Prop UV (the restricted signed-subset-sum discrepancy bound over the VERT vertex family).
Cases to cover: balanced valley {m=n+1, a₁<L/2, a₂<β_nL} only; all else closed.
Watch out for: DELETE / subset-selection is ESSENTIAL — full-support (no-DELETE) trees overshoot on
214/516 valley profiles (≤7.5×); any construction MUST use DELETE. Do NOT pigeonhole all {0,±1}
patterns (RL forbids it). Prove profile-independently over the vertex family — a 387-profile
spot-check is NOT a proof (reviewer rule R3/R4).

---

valley-differencing-construction: new
Target: minimax D=u_n, c(n)=2^n/(2^{n+1}−1) (both bounds); distinct contribution = UPPER valley by
EXPLICIT construction.
Technique: constructive sorted-differencing chain + DELETE-repair prefix (Karmarkar–Karp analogue,
aimo-0796 sequential-append) — genuinely different from existential VERT/pigeonhole.
Skeleton:
  1. Same reduction to min 𝓡(A) ≤ u_nL (R-UV). — imported.
  2. Xiang plays: DELETE a specified small-piece subset, then run the left-deep descending-difference
     chain r₁=a₁, r_k=|r_{k−1}−a_k| on survivors (each step a legal MATCH; tree-realizable by RL). —
     construction.
  3. Prove the chain leftover ρ ≤ u_nL profile-independently. — the open gap.
Key lemmas (claim + mechanism):
  - The chain drives r→0 — because a₁<L/2 ⇒ a₁<Σ(rest), so the descending differences cannot stall
    positive (aimo-0796 gives the crude ρ<a₂).
  - Sharp bound ρ≤u_nL — because a₂<β_nL and the dyadic cascade telescopes to exactly u_nL; the
    overshoot is bounded by induction on the number of survivors (this is the real content).
Open gaps: GAP-CHAIN (sharp telescoping overshoot bound ρ≤u_nL) + GAP-DELETE-RULE (make the DELETE
set deterministic & budget-legal: |T|−1 MATCH + (n+1−|T|) DELETE = n cuts).
Cases to cover: balanced valley only.
Watch out for: aimo-0796's bound is only ρ<a₂, and a₂ can be ≈2^{n−1}·u_nL — so the sequential-append
lemma ALONE is off by up to 2^{n−1}; a genuine telescoping bound (not aimo-0796 as-is) is mandatory.
No-DELETE full-support chains are machine-refuted — DELETE must be used non-trivially. Do NOT present
a numeric check as the proof.

---

Build-set recommendation to the outline-reviewer: parity-measure-potential (advance),
breakpoint-vertex (advance), valley-differencing-construction (new), ballot-matching (new).
Priority order if capacity-limited: parity-measure-potential and breakpoint-vertex are the two best
vehicles (advance both); valley-differencing-construction is the higher-value new framing (a fully
explicit construction can close Prop UV outright if GAP-CHAIN yields); ballot-matching is the
insurance second lower lever — keep it only if the reviewer agrees the matching mechanism is far
enough from parity-measure's induction, else drop to keep the field from collapsing to one lower
wall with two names.
