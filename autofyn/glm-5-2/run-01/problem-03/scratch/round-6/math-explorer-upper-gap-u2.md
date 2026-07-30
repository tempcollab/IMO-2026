## imo-2026-03 (GAP-U2 upper-bound wall, NON-cascade scout)

### HEADLINE FINDING (clean, provable, drops a hypothesis)

**Halving a_1,…,a_n (n marks) ALWAYS gives D = a_{n+1} for ANY strictly-decreasing m=n+1 Liu config — the bottom-dominant hypothesis of `bottom-dominant-halving` is UNNECESSARY.** Verified exact-`Fraction` 0 violations / 1500 random strictly-decreasing configs (n=2..6). The proof is a clean parity/grouping argument:

*Proof.* Refine by halving a_1,…,a_n (n marks), leave a_{n+1}. Refined multiset = {a_1/2,a_1/2,…,a_n/2,a_n/2,a_{n+1}} (2n+1 pieces). Because L is strictly decreasing, the values a_1/2,…,a_n/2 are pairwise distinct. Group consecutive equal values in the sorted order. Every value a_i/2 with a_i/2 ≠ a_{n+1} appears exactly twice → an even-size (size-2) block → contributes 0 to D (two consecutive positions, signs +/−). The value a_{n+1} appears 1 + 2·#{i : a_i = 2a_{n+1}} = 1+2k times (odd) — and strictly-decreasing ⇒ at most one i has a_i = 2a_{n+1}, so k ∈ {0,1}. All other blocks being size-2 (even) and sitting in pairs, the a_{n+1}-block starts at position 1 + 2·(#blocks above it) = odd. A block of 2k+1 consecutive signs starting at + has sign-sum +1. So the a_{n+1}-block contributes +a_{n+1}, everything else 0. ∴ D = a_{n+1}. ∎

**Consequence — GAP-U2 SIMPLIFIES to a single open sub-case.** Since halving is a valid n-mark Xiang strategy, **D* ≤ a_{n+1} for EVERY strictly-decreasing m=n+1 config, unconditionally (all n, no induction).** Therefore:
- **a_{n+1} ≤ 1/D_n ⟹ D* ≤ 1/D_n — CLOSED for all n** (regardless of bottom-dominance). This subsumes the entire non-bottom-dominant regime (Part VII sub-case (a)) WHEN a_{n+1} ≤ 1/D_n, and the bottom-dominant sub-case (b) with a_{n+1} ≤ 1/D_n. The non-bottom-dominant vs bottom-dominant distinction is IRRELEVANT to the bound.
- **The ONLY remaining open case is a_{n+1} > 1/D_n** (the "compressed" case: the smallest piece exceeds 1/D_n). This is strictly narrower than GAP-U2-as-stated.

This is a real, certifiable lemma the outliner can promote immediately (`halving-always-a-nplus1`), generalizing `bottom-dominant-halving` and dropping its hypothesis. It is the single most useful structural fact this round.

### Distinct openings (the compressed case a_{n+1} > 1/D_n)

- **(O1) Split-bottom + exact-pair-rest, with tunable split (continuity/IVT).** Split a_{n+1} → {x, a_{n+1}−x} with x ≤ 1/D_n (1 mark), then exact-pair {a_1,…,a_n, a_{n+1}−x} into n equal pairs using n−1 marks (gaps 0). Then D = x ≤ 1/D_n. The piece a_{n+1}−x is a CONTINUOUS tunable parameter; the exact-pairing feasibility changes only at finitely many breakpoints of x (where a fragment ties an existing piece). At x = a_{n+1} (no split) D = a_{n+1} > 1/D_n; at x → 0 the rest ≈ the original n+1 pieces and (conjecturally) becomes pairable (compressed ⇒ pairable). An IVT/parity-on-breakpoints argument may certify ∃ x ≤ 1/D_n with a valid exact pairing. **Most promising — see verdict below.**
- **(O2) "Split the large piece to match the medium pieces" (the empirically winning move).** The actual D=0 witness for the spread config (0.6,0.2,0.1,0.055,0.045)/1 is: split a_1=0.6 → {0.2,0.2,0.2} (2 marks, matching the existing a_2=0.2 → four 0.2's, even) AND split a_3=0.1 → {0.055,0.045} (1 mark, matching a_4,a_5). Result all-even-multiplicity ⇒ D=0. So the winning strategy pairs LARGE pieces against MEDIUM pieces (not the bottom-up cascade, which pairs second-smallest against smallest). This is a subset-sum/matching existence: "can each a_i be written as a sum of fragments taken from a multiset of equal pairs?" The freedom (Xiang chooses the pair values v_j) is large, but a universal existence proof is the hard subset-sum core.
- **(O3) Unique-max-at-tower / exchange (route 1, relocalized).** D* ≤ a_{n+1} (proved) and a_{n+1} ≤ 1/D_n ⟺ "the config is at least as spread as the tower." The tower T_n is the unique minimally-compressed spread config (a_{n+1}=1/D_n, ratios exactly 2). Any config with a_{n+1} > 1/D_n is STRICTLY more compressed than T_n ⇒ should be pairable (D* small). The exchange step needed: show that compressing the tower (reducing spread while keeping sum 1) strictly decreases D* below 1/D_n. The discontinuity (D*=1/D_n AT the tower, D*=0 for perturbations) makes a pure continuity argument fail, but an exchange/smoothing at the breakpoint structure may work.
- **(O4) Even-position packing reframe (route 5).** D = 1 − 2·(even-position sum); Xiang wants even-position sum ≥ (2^n−1)/D_n. Halving the tower packs exactly (2^n−1)/D_n into even slots (tight). For compressed configs, the "even slots can absorb more mass" because pieces are near-equal. A direct packing/greedy argument (fill even slots greedily from largest pieces) may certify the bound. Distinct from the lower-bound LP-dual (this is Xiang's min, the primal).
- **(O5) Generalize the n=2 pairing/averaging bound (route 4).** The n=2 proof (regime B1/B2) uses: pair a_1 → {a_2, a_1−a_2}, then averaging bound D(rest) ≤ b_2/2 ≤ a_3/2 < 1/7. The natural n-generalization: pair a_1 → {a_2, a_1−a_2} (cancel two a_2's), reduce to an (n−1)-mark game on {a_1−a_2, a_3,…,a_{n+1}}. But this REQUIRES the n−1 bound on the rest — CIRCULAR (the V(n)←V(n−1) IH, already refuted as phantom-crux). So route 4 via IH is a DEAD END; only a DIRECT (non-inductive) averaging bound on the rest would work, and no such bound is visible (the rest's optimum is not a clean function of its total).

### Candidate technique(s)
- **Parity/grouping for the alternating sum** (the halving lemma's engine — size-2 blocks contribute 0, the unique odd-block sits at an odd position). This is the technique behind the headline finding.
- **Piecewise-linear / breakpoint analysis** (pl-breakpoint-minimum, already certified): the min of D over refinements is at a breakpoint (tie) config; the tunable-split route O1 lives on this PL landscape.
- **IVT / intermediate value on a one-parameter split** (O1): a continuous parameter x with finitely many PL breakpoints.
- **Prouhet–Tarry–Escott / multiset power-sum matching** (knowledge_base "Multiset partitions & power-sum matching"): the exact-pairing existence is a multiset-equal-sums problem; this KB entry is the closest match for O2.

### Cheap-kill candidates
- **The halving lemma itself is the cheap kill** for the entire a_{n+1} ≤ 1/D_n region (no computation needed, pure parity). Promote it as a lemma; it collapses ~half of GAP-U2.
- **Parity obstruction for the compressed case:** with exactly n marks the refined count is 2n+1 (odd) ⇒ D ≠ 0 always (an odd-multiplicity value survives). So D=0 (full pairing) needs ≤ n−1 marks (even count). This means the compressed case CANNOT be closed by "D=0 always"; the best one can hope is D = small leftover ≤ 1/D_n. (A useful negative: don't try to prove D=0 in the compressed case via n marks — parity forbids it. The split-bottom route O1 uses 1 mark on the bottom + n−1 on the rest = n marks, leaving the split piece x as the unique odd leftover — consistent.)
- **a_{n+1} > 1/D_n forces compression:** a_i ≥ a_{n+1} > 1/D_n for all i ⇒ a_1 ≤ 1 − n/D_n = (D_n − n)/D_n, so the spread a_1/a_{n+1} < D_n − n. Bounded spread ⇒ pieces are within a factor < 2^{n+1} of each other. A pigeonhole/size-bucket argument on this bounded range may force a matchable structure.

### Knowledge-base entries to use
- **Multiset partitions & power-sum matching** (Prouhet–Tarry–Escott flavor) — for the exact-pairing existence in O2/O1.
- **Piecewise-concavity smoothing / breakpoint minimum** — the min of D is at a breakpoint; O1's tunable split lives on this PL landscape (pl-breakpoint-minimum already certified).
- **Pigeonhole / extremal principle** — bounded-spread forcing a matchable structure (cheap-kill).
- **Invariants & monovariants** — the parity-of-position invariant underlies the halving lemma.

### Analogous past problems (cruxes)
- **`aimo-0117`** (combinatorics, games-and-strategy) — "Assign the played values as a two-sided geometric progression" + "Defer committing the extreme value." A two-box game with n stones where the crux is a geometric-progression (2:1) assignment — directly analogous to the tower's 2:1 structure being the extremal assignment. Crux move: the geometric-progression assignment is the unique tight config (mirrors T_n being the unique maximizer).
- **`aimo-0115`** (combinatorics, games-and-strategy) — "Pair the cells of a region into dominoes and have each move flip a domino" / "Saturate a full separating line." A pairing-strategy crux where the second player pairs cells — analogous to Xiang's exact-pairing strategy (O2). Crux move: the pairing strategy certifies the bound; the obstruction is when no perfect pairing exists (the tower).
- No crux in the corpus is a direct stick-cut/alternating-claim game (the 2026 problem is novel in framing); the above are the closest by STRATEGY (pairing/extremal-assignment), not by surface. Do not treat them as citations.

### Prior progress
- **Best proven (importable):** `bottom-dominant-halving` (D = a_{n+1} when a_n ≥ 2a_{n+1}); `m-le-n-halving-D-zero`; `repeated-value-D-zero`; `parallel-halving-saturates-tower` (D(T_n)=1/D_n witness); `pl-breakpoint-minimum`; `spine-pair-cancellation`; n=1,2,3 upper bounds certified.
- **This round's new best (provable, promote):** `halving-always-a-nplus1` — halving a_1..a_n gives D = a_{n+1} for ALL strictly-decreasing m=n+1 configs (drops bottom-dominant). ⇒ D* ≤ a_{n+1} unconditionally ⇒ closes a_{n+1} ≤ 1/D_n for ALL n. The remaining open case is a_{n+1} > 1/D_n (compressed), strictly narrower than GAP-U2.

### Dead ends (do not retry)
- **Bottom-up pair-matching cascade as a Diophantine-termination proof (the original GAP-U2 conjecture):** DEAD. The cascade's residual recurrence r_0=a_{n+1}, r_k = a_{n-k+1} − r_{k-1} gives, IF it completes without a match, r_n = D(L) (the alternating sum of the ORIGINAL config) — and D(L) can be ≫ 1/D_n (witness (0.6,0.2,0.1,0.055,0.045): D(L)=0.49 vs 1/31≈0.032). The cascade only helps when it HITS a match (D=0), which is a subset-sum condition with no general guarantee. Do NOT frame GAP-U2 as "the cascade terminates in n steps."
- **V(n) ← V(n−1) IH (route 4 via induction):** DEAD (round 5, phantom-crux). The IH is a worst-case bound blind to slack; the pairing rest-optimum is not a clean function of the rest total. Any induction on n is circular (the n−1 bound IS what we're proving).
- **Max-bound D* ≤ M/2^n:** REFUTED (round 4, (7,6,5,3)/21). Do not revisit.
- **Schur-convexity / majorization / Karamata on the Liu config:** DEAD (round 3, D* not Schur-convex; single-piece config most-majorizing yet D*=0).
- **3-mark cascade (route B from round 4):** DEAD (targets the phantom crux regime, which gives D*=0 anyway).

### Small-case / intuition notes (all CONJECTURES from computation, labeled)
- **Halving-always-D=a_{n+1}:** 0 violations / 1500 exact-Fraction trials n=2..6. CONJECTURE numerically, but the PROOF above is rigorous (parity) — this is a THEOREM, not a conjecture.
- **Compressed case (a_{n+1} > 1/D_n):** n=3, 0 search-violations / 40 compressed configs (all D* ≤ 1/15 found, mostly D=0); n=4 search finds D=0 or small (search too slow for exhaustive, but 0 violations in completed trials). CONJECTURE: D* ≤ 1/D_n (likely D*=0 or tiny) whenever a_{n+1} > 1/D_n strictly.
- **Discontinuity at the tower:** D*(T_n)=1/D_n, but every strict perturbation of T_n gives D*=0 (verified round 5). The tower is an ISOLATED maximizer. CONJECTURE (supports route O3).
- **The winning compressed strategy is "split large to match medium" (O2), NOT bottom-up cascade.** Witness: (0.6,0.2,0.1,0.055,0.045) → split 0.6→{0.2,0.2,0.2} (match a_2) + 0.1→{0.055,0.045} (match a_4,a_5), all-even, D=0. CONJECTURE: this generalizes (large pieces are "reservoirs" to match the medium/small pieces).
- **a_{n+1} > 1/D_n forces bounded spread** (a_1/a_{n+1} < D_n − n): CONJECTURE that bounded spread forces pairability, but the matching existence is the unproved subset-sum core.

### most promising route = O1 (split-bottom + exact-pair-rest with tunable split)

**One-sentence proof skeleton:** Split the bottom piece a_{n+1} → {x, a_{n+1}−x} with x ∈ (0, 1/D_n] (1 mark), and prove (via the PL/breakpoint structure of the exact-pairing feasibility of {a_1,…,a_n, a_{n+1}−x} as a function of the continuous parameter x) that for SOME x ≤ 1/D_n the n pieces {a_1,…,a_n, a_{n+1}−x} admit an exact pairing into n equal pairs using n−1 marks — yielding D = x ≤ 1/D_n.

**Single hardest sub-step:** proving the exact-pairing of {a_1,…,a_n, a_{n+1}−x} into n equal pairs is achievable for some x ≤ 1/D_n. This is a one-parameter subset-sum/multiset-equal-sums existence; the tunability of x is the lever, and the PL-breakpoint machinery (`pl-breakpoint-minimum`) is the natural tool, but the existence step is the genuine open core. Fallback if O1 stalls: the bounded-spread pigeonhole cheap-kill (a_{n+1} > 1/D_n ⇒ spread < D_n − n) may force a matchable structure directly, bypassing the continuous parameter.

### Honest assessment of the other routes
- **Route 1 (unique max / exchange):** supported by the halving lemma (D* ≤ a_{n+1} ≤ 1/D_n ⟺ spread ≥ tower) and the isolated-maximum numerics, but the DISCONTINUITY at the tower (D* drops to 0 under perturbation) blocks a naive continuity/exchange proof. Needs the PL-breakpoint machinery — converges to O1.
- **Route 2 (cascade residual bound):** DEAD as framed (residual = D(L) ≫ 1/D_n). The only salvageable version is "cascade hits a match ⟹ D=0," which is exactly the subset-sum core of O2, not a separate route.
- **Route 3 (universal potential Φ):** Φ = a_{n+1} works for the a_{n+1} ≤ 1/D_n region (this IS the halving lemma); it FAILS for the compressed region (a_{n+1} > 1/D_n, where Φ = a_{n+1} > 1/D_n). No config-dependent potential for the compressed region found. The halving lemma is the best potential and it caps at a_{n+1}.
- **Route 4 (n=2 pairing generalization via IH):** DEAD (circular). The non-inductive n=2 averaging bound (D(rest) ≤ b_2/2) does not lift to n≥3 without an n−1 bound on the rest.
- **Route 5 (LP/optimization):** the even-position packing reframe (D = 1 − 2·even-sum) is clean but the dual is not obviously simpler than the primal; it is a genuinely-different CERTIFICATE form (like the lower-bound LP-dual) but no clean dual bound on the max even-sum is visible. Keep as a fallback if O1/O2 stall.
