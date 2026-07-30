# Outline review — imo-2026-03 (IMO 2026 P3), Round 2

Shared context is solid and CERTIFIED (Lemma G, level-measure identity `D=λ{t:#pieces>t odd}`,
cut-flip; reduction `D*=max_Liu min_Xiang D = u`; n=1 both bounds; lower-bound Case A). Two walls
remain: GAP L (lower, top piece cut) and GAP U (upper, general non-myopic ≤n-cut Xiang rule).

I ran one decisive cheap-kill this round: is `f(p):=min_Xiang D` concave over the Liu simplex?
That question decides the entire concavity-lp approach. Answer below.

---

## concavity-lp — RETHINK (fatal: the concavity engine is numerically FALSE)

The approach's whole selling point is: `f` is **concave** on the simplex, so a single first-order
(KKT/subgradient) certificate at the dyadic partition proves it is the *global* max — "one local
check replaces GAP U's per-partition case analysis." This rests entirely on the claim
`f = min of finitely many GLOBAL affine functionals ⇒ f concave` (skeleton step 3 / GAP C2).

**I tested concavity directly (n=2, 3-piece Liu partitions, a well-converged allocation-enumeration
+ many-restart Nelder–Mead inner optimizer, validated to reproduce `min D = 1/7` at dyadic).**
Midpoint test `f((p+q)/2) ≥ (f(p)+f(q))/2`: **12 / 60 random pairs violate concavity**, gaps up to
0.058. Re-run of the worst cases with 120 restarts on all three points confirms it, e.g.
`f(p)=0.0462, f(q)=0.0510, f(mid)=0.0048` (avg 0.0486). `f(mid)` sits far BELOW the average — a
clean concavity violation.

This is not an optimizer artifact. Under-convergence inflates `min D` (the upper-bound explorer's
warning is about fake *high* values); a *low* `f(mid)` surviving heavy restarts is the true value.
The mechanism of the failure is exactly the gap the outliner flagged as C2 but assumed away: the
functionals `ĝ_S` are affine only **per order-type**, and the set of Xiang responses (and their
affine extensions) is **p-dependent**. At the midpoint Liu's partition has near-equal top pieces
that Xiang cancels with a cheap response unavailable — and not affine-extendable with `ĝ_S ≥ f` —
at the endpoints. So `min-of-affine-per-order-type ≠ min-of-global-affine`; the envelope inequality
`ĝ_S ≥ f` fails off-region and `f` is not concave.

Consequence: KKT-stationarity at dyadic certifies nothing (a stationary point of a non-concave
function need not be a global max). The freshframing explorer's evidence only showed dyadic is a
*local* max in 5 directions — true but insufficient without concavity, and my test shows global
concavity is false. The "one mechanism, both bounds" claim collapses. The salvageable pieces
(affine-per-order-type, single-cut optimum at a boundary) are already the certified cut-flip lemma
and add nothing new on their own.

Verdict RETHINK. **Not registered** — a rejected line stays out of the pool. Back to the outliner:
concavity/LP-global-optimality is the wrong engine here. The genuinely-different framing the field
still needs must not rely on global concavity of `f`. (The answer `D*=u` itself is unaffected —
dyadic is still the numerically-confirmed global max; only this proof route is dead.)

## induction-recursion — CHANGES REQUESTED (sound; owns GAP L)

The REVISE is correct and well-posed. The round-1 mechanism (strict `W(n−1,b)>u_{n−1}` for `b<n−1`)
was genuinely refuted by the lower-bound explorer (equality `D=u` attained at `b=1<n−1=2`, n=3), and
the replacement — an **exact-value minimax recursion** `V(n,k):=min_{≤k cuts}D`, prove `V(n,n)=u_n`
by strong induction with budget split `k=a+b`, bottom `= σ·V(n−1,b)` — is equality-robust and
matches the explorer's recommendation. `V(n,k)` is well-defined; the recursion is not circular; the
`O_top△O_bot` identity and `λ(O_bot)≥u` (scaled IH) are already in hand. The recommended
rank-interleaving sub-mechanism (merged sorted T/B label string, bypassing the opaque
`2λ(O_top∩O_bot)` cancellation) is the right invariant.

Build issues to close (GAP-LB): (1) prove the exact recurrence for `V` actually CLOSES at `u_n` —
i.e. that combining `a` top-cuts with `σ·V(n−1,b)` cannot dip below `u_n` for any `a+b≤n`, using the
merged-order signed sum (GAP-LB.1) or the canonical-form exchange (GAP-LB.2); (2) keep the argument
non-strict/equality-robust throughout (do NOT reintroduce any strict domination — refuted). This is
real work but a legitimate mechanism, not a relabel of a dead end.

## dyadic-discrepancy — CHANGES REQUESTED (leader; owns GAP U)

ADVANCE is right. The close-the-largest-PAIRING-GAP strategy is genuinely distinct from the three
refuted rules: it is greedy on the pairing-form gaps `b_{2i−1}−b_{2i}` (and pairing-off the odd
leftover), NOT on literal equal tiers (why bisection-only fails), NOT on per-cut D-reduction (the
refuted myopic rule), NOT top-only (refuted on near-balanced Liu). The upper-bound explorer's
Opening 2 independently isolates this same regime-adaptive "greedy on gaps" rule and shows it
reproduces all three observed regimes (dyadic ⇒ split top; near-balanced ⇒ subdivide small
leftover; n=1 ⇒ certified threshold rule). So it is not a relabel of the refuted greedy.

Build issues to close (GAP U): the strategy is now concrete but the `D≤u` bound is unproven — the
two sub-claims (U.a) gap-greedy optimality by exchange, and (U.b) residual `≤u` by the
budget-vs-pieces pigeonhole in **pairing-gap form** — are the crux and remain open. Honest caveat:
GAP U is the hardest wall and no approach has fully closed it; this is the best available line for
the upper bound and worth the build, but the builder should not overclaim if (U.b) resists.

## potential-certificate — RETIRE (near-duplicate; distinct result already banked)

I concur with the outliner. After its round-1 pivot it uses the SAME order-aware level-set
certificate as the other two and shares BOTH walls, so as a live whole-problem attempt it adds no
diversity. Its one distinct deliverable (no separable per-piece potential can certify the odd-rank
functional — clean witness + LP infeasibility) is a COMPLETED certified dead-end, already recorded;
nothing is lost. Handled via the ranking: I ranked it last head-to-head (Elo dropped 1468→1442), so
it is naturally down-sampled. **Not in the build set.** Do not repoint it to rank-interleaving — that
overlaps induction-recursion's GAP-LB.1 and would not restore diversity.

---

## Ranking (updated this round; stale flags cleared)

Anchored to evidence: dyadic-discrepancy is the leader (certified spine + Case A + n=1 + a concrete,
not-refuted GAP U strategy), so it beats both. induction-recursion (live, revised to an
equality-robust mechanism) beats the retired near-duplicate potential-certificate.

- dyadic-discrepancy **1558** (leader, GAP U)
- induction-recursion **1500** (revised, GAP L)
- potential-certificate **1442** (retired duplicate — sinking)
- concavity-lp — not registered (RETHINK)

## Diversity flag for the orchestrator

The intended round-2 diversity injection (concavity-lp) is numerically dead, and
potential-certificate is retired. The live field is now just **two D-language approaches sharing the
certified reduction**: dyadic-discrepancy (GAP U) and induction-recursion (GAP L). They attack the
two different walls with genuinely different mechanisms (explicit adaptive strategy vs self-similar
exact recursion), so they are not the single-gap trap — but the field is thin and both live in the
discrepancy language. If both walls resist next round, the orchestrator should ask the outliner for a
framing that does NOT rely on (a) global concavity of `f` [refuted] or (b) a separable potential
[refuted] or (c) the same `D`-level-measure reduction — a genuinely orthogonal route (e.g. a direct
strategy-stealing/scale-invariance argument on the game tree, or an amortized halving monovariant on
`W_n=2^{-n}`) is what would actually broaden the terrain.

build set: dyadic-discrepancy, induction-recursion
