# proof-reviewer — per-role rules (imo-2026-03 run)

ALWAYS: attack a claimed sharp bound numerically with scipy Nelder-Mead over ALL cut allocations, not just structured replies — the bound being attained exactly (zero slack) makes any error visible (worked for Theorem L, round 2).
ALWAYS: brute-force game-value lemmas with a memoized game tree in exact Fractions, including ties and zeros (caught nothing round 2 but is cheap and decisive; Lemma G certified on it).
ALWAYS: when certifying a lemma buried in an approach file, copy a cleaned standalone statement+proof into lemmas/<name>.md with a certification stamp — siblings import the lemma file, not the approach file (round 2).
NEVER: penalize an approach for importing a certified sibling lemma to close its own gap (tie-structure's GAP M(a) is legitimately subsumed by ladder-resists, round 2) — but do note it in the routing advice so the ranker sees what is proprietary to the slug.
ALWAYS: when a builder hands a strategy-existence proof (walk/process), re-implement the process from the proof TEXT with assert statements for every claimed invariant (carrier length, unreachable states, budget) — not the builder's own code; a wrong invariant surfaces instantly (round 4, Lemma W certified on 4800 clean instances).
NOTE: run RESOLVED round 4 — imo-2026-03 SOLVED, c(n)=2^n/(2^{n+1}-1); current.md has the Full proof; all 7 lemma files certified. Do not re-open.
NOTE: field state after round 2 — lower bound c(n) >= 2^n/(2^{n+1}-1) is certified (lemmas/ladder-resists.md); the ONLY remaining gap in the whole problem is Claim U(m) middle case (a1 < 2^{m-1}beta, a2 < 2^{m-2}beta) + a1=a2 tie sub-case, in approaches/discrepancy-halving.md. U(m) verified true numerically m=3..5, 60 random instances.
