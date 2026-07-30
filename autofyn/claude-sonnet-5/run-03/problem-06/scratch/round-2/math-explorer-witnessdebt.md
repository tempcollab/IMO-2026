## imo-2026-06

### Headline finding (new opening, strongly recommended)

The "No-Escape" gap (core-signature-pigeonhole) is an artifact of using an *a-priori-truncated*
prime set `P = {primes ≤ L0}` (L0 = rad(a_1)) to approximate the antichain of live constraints.
If instead one works with the **true, untruncated antichain** from `constraint-domination.md`
(inclusion-minimal elements of {primes(a_1),...,primes(a_n)}, using each a_i's *real* full
factorization, not its intersection with a fixed small set), the No-Escape problem **disappears
by construction**: once the antichain of live indices stabilizes to a fixed finite list
I* = {i_1,...,i_k} (n > N*), the true validity condition C_true(x,n) is *exactly*
"gcd(x, a_{i_j}) > 1 for j=1..k" (no approximation, by Constraint Domination, which is already
certified and exact). Define P* := primes(a_{i_1}) ∪ ... ∪ primes(a_{i_k}) — finite because k is
finite and each a_{i_j} is a fixed integer. Then hitting-G-mod-lcm(P*) is *simultaneously* necessary
and sufficient for C_true (no "escape via a prime outside P*" is even meaningful, because P*
literally contains every prime that could ever matter for these k fixed generators). The existing
certified lemma `lemmas/periodicity-given-no-escape.md` is already stated generically for *any*
finite P ⊇ primes(a_1) satisfying signature stabilization + sufficiency — it plugs in directly once
antichain stabilization is granted, with **no residual gap** (unlike the P=primes≤L0 route, which
needed a separate unproven "no escape" step even after signature stabilization).

**Conclusion: the entire remaining difficulty of the theorem reduces to ONE clean, purely
combinatorial claim — Antichain Stabilization** — with no secondary gap once it is granted. This is
a strictly better target than "No-Escape relative to P=primes≤L0" and should replace it as the
primary open lemma for next round.

**Antichain Stabilization (the new target).** There exists N* such that for all n ≥ N*, the family
of inclusion-minimal elements of {primes(a_1),...,primes(a_n)} (under ⊆) is unchanged from its value
at n = N* — i.e., no index n > N* ever produces a_n whose prime set is incomparable to every current
minimal element (a "new incomparable/growth event").

### Computational evidence (strong, this round's main contribution)

I instrumented the exact antichain dynamics (not an approximation) and tracked (a) antichain size
over n, (b) the index of every "new incomparable growth event", for many a_1:

- a_1 ∈ {15,35,105,77,30,1001,210,6}: stabilizes essentially immediately (last growth event at
  n ≤ 52 in every case), then **zero** further growth events over the remaining ~4000 steps.
- a_1 = 30, 6: stabilizes at antichain size 1 from the very first step (never grows).
- a_1 = 2310 = 2·3·5·7·11 (5 distinct primes): antichain size grows to a **max of 268** before
  collapsing to final size 1; last growth event at n=887; verified **zero** further growth events
  out to n=20000 (re-ran with a longer horizon specifically to stress-test this).
- a_1 = 30030 = 2·3·5·7·11·13 (6 distinct primes): max antichain size 588, last growth at n=1367,
  stable for the remaining ~4600 steps tested.
- a_1 ∈ {1155,385,1309}: last growth events at n ≤ 62, stable for thousands of steps after.

Key qualitative pattern: **antichain size is NOT monotone** (it can balloon into the hundreds, e.g.
268 or 588, then collapse sharply via a single dominating element removing many at once) — so a
naive "antichain size is non-decreasing hence bounded" monovariant is FALSE; any invariant must
tolerate large intermediate excursions. But in every test, growth events themselves eventually and
permanently cease. This is conjectural (finite-horizon simulation), but the horizon (up to 20000
steps, well past the last observed event by more than an order of magnitude in the worst case) makes
it strong evidence, not just a guess.

### Candidate mechanism for Antichain Stabilization (scouted, NOT developed into a proof)

- **Efficiency/minimality charging argument.** a_{n+1} is the *smallest* valid candidate, and
  Lemma 2 (`gap-bound.md`) guarantees a "boring" always-valid candidate within a_n + L0 using only
  primes of S = primes(a_1). A genuinely new incomparable a_{n+1} must beat this bound, and — more
  restrictively — must simultaneously intersect every one of the k current antichain sets Q_1..Q_k
  without containing any of them wholly. As k grows, this requires a_{n+1} to pack enough distinct
  "hitting primes" into a number that is also smaller than the reliably-available boring candidate;
  since a number ≤ X has at most O(log X) distinct prime factors, there is tension between k growing
  and the number of available factorization "slots" in the bounded window — this is the flavor of a
  counting/pigeonhole argument bounding the total number of growth events, but I did NOT complete it
  (needs a precise charging scheme: e.g. charge each growth event to a "new prime pulled in", and
  bound how many distinct primes can ever be pulled in using that primes small enough to be reused
  are always cheaper). This is the "witness debt" mechanism requested — a real candidate, not yet a
  proof.
- **Dilworth/covering-style antichain bound** (seen in crux aimo-0716, combinatorics/double-counting:
  "bound an antichain by covering the ground set with chains/cones"): the poset here is finite
  subsets of primes under ⊆, restricted to sets that (a) contain some prime of the fixed finite
  S = primes(a_1) (Lemma 1, already certified) and (b) arise as primes(a_n) for a term in a window
  of length ≤ L0 above the previous term. A chain-covering argument bounding the antichain by the
  number of "types" of numbers achievable in that window might work but the window's arithmetic
  content changes with n (not literally periodic yet), so this needs real adaptation, not a direct
  transplant.
- **Minimal-counterexample / greedy-minimality contradiction** (matches
  `covering-construction-induction.md`'s sub-strategy 3b): assume infinitely many growth events;
  derive a contradiction from the fact that each such event's value must be *minimal* among valid
  candidates, forcing a specific numeric relationship between the new prime and the gap bound L0
  that cannot recur infinitely often. Not completed but structurally compatible with the antichain
  reframing above (and now has a cleaner, gap-free payoff if it succeeds — no more secondary
  No-Escape check needed).

### Cheap-kill / pruning ideas
- Parity/size check already ruled out: antichain size is not monotone (see above) — do not let a
  builder assume it is.
- A quick necessary condition worth checking before deep investment: verify computationally whether
  the total number of growth events for a_1 with ω(a_1) = m distinct primes grows combinatorially in
  m (data hints at this: m=2 → ~2-3 events, m=3 → ~4-36, m=4 → ~7-12, m=5 → 333, m=6 → 810) — if a
  clean formula/bound in terms of ω(a_1) emerges, that is a strong hint toward the right charging
  argument (e.g. bound by 2^{2^{ω(a1)}} or similar tower-type bound from iterating the antichain
  poset structure). I did not chase this further; flagging as a promising quick numerical follow-up
  for next round's explorer/outliner.

### Knowledge-base entries to use
- Pigeonhole/extremal principle for monotone chains in a finite poset (already used in Lemma 3 of
  `core-signature-pigeonhole.md`) — directly reusable once antichain stabilization at a *fixed* index
  set is granted, exactly as in `periodicity-given-no-escape.md`.
- No new knowledge_base.md entry found that directly attacks "antichain of finite sets under
  inclusion generated by a greedy minimality process eventually stabilizes" — this really is the
  crux and likely needs a bespoke counting argument, not an off-the-shelf theorem.

### Analogous past problems (crux corpus)
- `aimo-0678` (IMO-SL 2015, gcd/lcm coupled recurrence) — already found round 1, still the best
  structural analog for the "bound one coordinate, reduce the other mod a fixed lcm, get a finite
  deterministic map, pigeonhole for periodicity" back-half of the argument (matches
  `periodicity-given-no-escape.md` almost exactly). Its front-half (a bounded monovariant `w_n` =
  min of a forbidden set, shown non-increasing) does NOT transplant directly (imo-2026-06's a_n is
  unbounded, not bounded), but is worth showing a builder as an example of the *shape* of argument
  ("min of a set that fails some property is non-increasing") that COULD inspire a genuinely
  different monovariant for antichain growth events specifically (e.g. "smallest prime not yet used
  by any live antichain element" or similar) — speculative, not verified.
- `aimo-0716` (combinatorics, antichain bound via chain/cone covering) — same-shape technique
  (bound an antichain via a covering), different domain (geometric poset vs. prime-divisor poset);
  worth a look if a builder wants to try the covering-bound mechanism above, but is not a ready-made
  transplant.
- No crux found that is a close analog of "greedy sequence's antichain of coprimality constraints
  stabilizes" specifically — searched subtopics divisibility-and-gcd, pigeonhole,
  invariants-and-monovariants, sequences-and-recurrences, zsigmondy-and-primitive-divisors in
  number_theory and double-counting/invariants-and-monovariants in combinatorics; nothing else
  closely matches beyond the two above.

### Dead ends (do not retry)
- Do NOT resurrect `monovariant-telescoping`'s |Q|<∞ target (Q = primes dividing infinitely many
  terms) — proven false by the reviewer, reconfirmed structurally here (once periodic, every prime
  coprime to L divides infinitely many terms).
- Do NOT assume antichain size is monotone non-decreasing or non-increasing — refuted numerically
  (a_1=2310: max 268 → final 1; a_1=210: max 13 → final 1). Any invariant/monovariant proposal must
  survive this.
- The `core-signature-pigeonhole` P=primes≤L0 formulation of No-Escape is NOT wrong, but it is now a
  strictly weaker/less clean target than Antichain Stabilization — a builder should not keep trying
  to directly prove No-Escape-relative-to-P without first considering whether to switch to the
  antichain framing, which removes the need for a secondary sufficiency-vs-necessity gap entirely.

### Prior progress
See `results/imo-2026-06/current.md`: furthest rigorous chain is core-signature-pigeonhole's Lemmas
1–5 + 7, reducing everything to the (P=primes≤L0)-relative No-Escape lemma. This round's finding
shows how to eliminate that specific formulation's residual gap entirely by re-targeting the exact
antichain instead — Lemma 7's proof (periodicity-given-no-escape) is already written generically
enough (for *any* finite P ⊇ primes(a_1) with signature stabilization) that it can be reused
verbatim once Antichain Stabilization is granted, by taking P := P* (the union of the finitely many
stabilized antichain generators' full prime sets) instead of P := {primes ≤ L0}.

### Small-case / intuition notes (conjecture, not proof)
- Antichain Stabilization appears true in every tested case (12 values of a_1, ω(a_1) from 1 to 6,
  horizons from 300 to 20000 steps), with last-growth-event index apparently growing quickly (roughly
  super-linearly, possibly worse) in ω(a_1) — a_1 with 5–6 distinct prime factors needed ~900–1400
  steps before freezing, vs. ≤ 60 for ≤ 4 factors. This suggests any proof of Antichain Stabilization
  will likely need to handle a genuinely unbounded (in terms of a_1) transient phase, not just a
  small-case check, and any "explicit formula" style approach (as attempted in
  `covering-construction-induction.md`'s step 1 coarse-guess) should expect the transient length to
  scale badly with ω(a_1), reinforcing that a counting/existence argument (not an explicit
  closed-form construction) is the more promising proof shape.
