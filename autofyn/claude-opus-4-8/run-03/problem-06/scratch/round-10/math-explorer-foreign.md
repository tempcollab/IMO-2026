## imo-2026-06 — FOREIGN-TECHNIQUE / CRUX-CORPUS scout (round 10)

### Mandate reminder (what I did NOT re-scout)
Per dispatch, I did not re-open (CSP)=ℰ-small-only=(EC)=¬(FIN-Q) as a target, and did not re-propose
aimo-0016 static covering, global Σ1/p² capacity, symmetric ascent, distinctness-by-difference
confinement, or lex-rewrite. This report is pure terrain: a crux-corpus mechanism search for the
missing "value/dynamics lower-pressure inequality via the greedy successor choice."

### Method
Read `crux_moves_documentation.md` for the exact schema (`technique`, `how_used`, `domain`,
`subtopic` — NOT `crux_move`/`statement`). Filtered `past_crux_moves_database.json` by
`domain ∈ {number_theory, combinatorics}` and `subtopic ∈ {size-bounding-and-descent,
processes-and-algorithms, extremal-principle, invariants-and-monovariants}`, then grepped for
greedy/minimal/smallest/potential/weight/cost/window/recruit/successor in `technique`+`how_used`.
Read full `problem`+`solutions` from `past_problems_database.json` for the strongest hits.

### Best find: aimo-0030 (IMO — "Ana and Banana" coprime-descent game), domain=number_theory,
subtopic=size-bounding-and-descent

**Problem shape (genuinely structurally cousin to imo-2026-06, not superficial):** a number
n≥k is "good"/"bad" via a move relation n→x defined by gcd(n,x)=1, x<n, x≥k (opponent-game
recursion). Goal: prove n,n' with the SAME set of primes ≤k dividing them have the same good/bad
status — i.e. **only primes ≤ k are ever load-bearing for the status**, EXACTLY our crux's shape
(only primes ≤ P_max are ever load-bearing for E_∞-membership / covering).

**Structural parallel already validated, not just superficial:**
- Their **Claim 1** (n good, n' multiple of n ⟹ n' good) is the direct analogue of our already-
  certified fact that E_∞-membership (and "coveredness") is a pure function of the prime SUPPORT
  of m, monotone under multiplication.
- Their **Claim 2** (rs bad ⟹ r²s bad, same argument, same witness) is the EXACT analogue of our
  own certified **Lemma 6 / `lemmas/bad-signature-geometric-family.md`** (m bad ⟹ m·r^k bad, same
  signature, same witness) — round 5 independently re-derived the same fact this crux uses. This
  cross-check is strong evidence the two problems share real DNA, not just a coincidental label.
- Their **Claim 3** (p>k prime, n≥k bad ⟹ np bad) is the piece we are missing: a genuine
  MINIMAL-COUNTEREXAMPLE argument that forces a large prime p to be non-load-bearing, using a real
  VALUE INEQUALITY (not a static covering/set argument).

**The mechanism of Claim 3 (the candidate transplant):** take n minimal among {bad n : np good}
(the smallest violator, for a fixed p>k). n bad gives a good witness x with gcd(n,x)=1. np good
forces gcd(np,x)>1, and since gcd(n,x)=1 this forces p | x. Write x = p^r·y, p∤y. Take α minimal
with y^α ≥ k. A chain of floor/size inequalities (y^α < ky < py = x/p^{r-1} < n/p^{r-1}) shows
p^{r-1}·y^α < n — i.e. y^α is STRICTLY SMALLER than the minimal counterexample n. Coprimality
forces y^α to be bad (since np good ⟹ every number coprime to np, smaller than np, is bad — and
gcd(np,y^α)=1 as gcd(n,y)=1, gcd(p,y)=1); minimality of n (as smallest violator of Claim 3 for this
p) then applies Claim 3 itself to the SMALLER bad number y^α, iterating to get p^r·y^α bad; finally
Claim 1's contrapositive (x | p^r·y^α, the bigger number is bad ⟹ x cannot be good) contradicts x
being good. QED by induction on the size of the counterexample.

**Why this could supply the missing ingredient:** it is a genuine VALUE inequality (an explicit
strictly-smaller integer y^α manufactured from a witness's cofactor decomposition x=p^r·y via a
floor/power bound, not a set-theoretic/covering argument) driving a well-founded descent that
directly forces "primes above the threshold are never load-bearing" — precisely the shape of
statement our crux needs, attacked via minimality on VALUE (not on prime-count, not on set
inclusion). It is far from all four exhausted framings: it does not go through CSP/ℰ/EC/FIN-Q at
all; it is a direct minimal-counterexample induction on an ordinary integer variable analogous to
"the smallest bad term for which some fixed large prime q is ever essential."

**Candidate transplant sketch (terrain only, not a proof):** Fix a large prime q suspected
essential (the smallest such q, or the smallest bad/essential-connector configuration using q).
Take the minimal bad term / minimal (A,q) essential-connector pair using q. From the certified
`essential-connector-equivalence.md` (Lemma 13/14), an A-avoiding witness term B is forced to be
divisible by q. Decompose B = q^r·y (y coprime to q, y = the part of B built from OTHER primes).
Try to manufacture, via a floor/power inequality analogous to y^α<ky<py=x/p^{r-1}<n/p^{r-1}
(needs a problem-specific analogue — likely tying y's smallest valid "companion" or the smallest
multiple of y that lands back in the term set, to a_1 or P_max as the threshold "k"), a STRICTLY
SMALLER essential-connector witness for q, contradicting minimality of the chosen configuration.

**Honest risk — why this may NOT transplant (be upfront, as instructed):**
1. Their game's "move" relation is a SINGLE pairwise gcd comparison (n vs one x); our E_∞
   membership is an INFINITE conjunction (gcd>1 against every predecessor a_i simultaneously). The
   clean single-step "np good ⟹ gcd(np,x)>1 forces p|x" step relies on x being EXACTLY the single
   comparison target; our analogue would need "B is A-avoiding" to force p|B via essentiality
   (this part DOES exist, certified as Lemma 13), but the subsequent floor/power inequality in their
   proof crucially uses the SPECIFIC recursive game bound x<n (game move constraint) — we have no
   literal "x < n" bound of that shape; our nearest analogue is the certified window-length /
   floor-tightness facts (Lemma 9/X: m_0 < a_1·p for a redundant prime), which is a similar SHAPE
   of inequality but was already tried by covering-small-part-descent/lex-rewrite and stalled
   exactly at the a_1 threshold (per round 7/9 findings) — so a literal reuse of Lemma 9/X as the
   "floor inequality" ingredient is NOT new; what would be new is COMBINING it with a genuine
   MINIMAL-COUNTEREXAMPLE-ON-q induction (as in Claim 3) rather than minimal-counterexample-on-term
   (already tried, e.g. minimal-bad-term-floor-tightness), i.e. induct on the PRIME, using the term
   inequality only as an internal lemma, not as the outer induction variable. This inversion of the
   induction variable (prime-indexed minimality, not term-indexed) is the genuinely untried piece.
2. Their multiplicative closure (Claims 1/2) is exact and unconditional because "good/bad" is
   PURELY a function of the radical of n; ours has the analogous fact ALREADY certified (Lemma 6),
   so this part is not new — but it means the remaining novelty is narrowly Claim 3's induction
   shape, not the whole apparatus.
3. This is a DIFFERENT problem's actual claim (finite threshold on move-status), not P6; every
   borrowed step must be reproven from scratch per CLAUDE.md — I have NOT verified the floor/power
   inequality has a working analogue in our value-domain; that verification is exactly the gap the
   outliner/builder would need to close, and it may fail (in which case this transplant dies like
   the others, but from a genuinely different angle than the four already-exhausted reformulations).

### Secondary candidates (weaker, reported for completeness)

- **aimo-0184** (IMO — "every prime occurs in a_n", `a_n` = smallest x>a_{n-1} satisfying a
  floor-sum identity; proof shows a_n = the k-th-power-free integers exactly, by strong induction
  matching the greedy identity against the natural enumeration). This is the CLOSEST literal
  structural cousin in "form" (a smallest-valid-successor greedy sequence, proved to equal a clean
  enumeration by induction on n matching identities) — already flagged in `/tmp/memory/math-explorer.md`
  round 1 as a technique donor, and our own ENUM reduction (`enumeration-of-E-infinity.md`) already
  IS this style of argument, fully certified. It does not supply anything new for the OPEN crux
  (finiteness of load-bearing primes) — its induction proves an enumeration coincidence, not a
  finiteness-of-support fact. Not recommending as fresh; flagging only that it is exhausted (already
  used for the certified scaffold).
- **aimo-0680** (number_theory, size-bounding-and-descent): "if finitely many rows are known
  arithmetic progressions, subtract their predictable per-window element counts... the remaining
  rows jointly have constant positive count" — a periodicity/window-counting move for a DIFFERENT
  goal (showing some non-AP row must be infinite). Superficial resemblance to our periodic-set
  endgame (already fully certified, not the open part) — not a new lever for the crux; the
  window-counting shape has already been explored and killed in round 2/9 (global capacity, local
  window pigeonhole with L_0 vs a_1 mismatch — see `/tmp/memory/math-explorer.md` rounds 1/5 notes).
  Do not re-pursue.
- **aimo-1015** (Vieta-conjugate size bound + minimal-(x+y) monovariant jump): same GENERIC shape
  (extremal/minimal representative + jump across a fixed threshold) as aimo-0030's Claim 3 but for
  a Pell/Vieta-jumping context with no gcd/prime-support structure — the mechanism (bound a
  conjugate object, show it crosses a threshold, descend to the minimal representative) is a useful
  generic template for "how to search for the missing inequality" but has no closer surface match
  than aimo-0030. Listed only as a secondary confirmation that "extremal + explicit crossing
  inequality" is a recurring, transplantable olympiad pattern — not a specific lemma to import.

### Recommendation for the outliner
Open ONE new approach that inverts the induction variable relative to every prior lane: induct on
the SMALLEST large prime q that is EVER an essential connector (minimality on the PRIME, not on the
term or window index, and not via CSP/ℰ/EC/FIN-Q framing directly), and inside that induction use
the certified Lemma 13 (EC, forced divisibility) plus a to-be-derived floor/power inequality (in the
style of aimo-0030 Claim 3's y^α<ky<py=x/p^{r-1}<n/p^{r-1} chain) to manufacture a genuinely SMALLER
essential-connector configuration using a SMALLER prime, contradicting minimality of q. This is
untried in the run's history (all "minimality" lanes so far minimize a TERM value or a WINDOW
index, never a PRIME itself as the well-founded induction variable) and is far enough from the four
exhausted faces to satisfy the shared-gap-break mandate. Flag clearly to the builder that the
floor/power inequality step is UNVERIFIED here and is precisely the crux-equivalent gap to attack —
if it fails, this route dies like the others, but it opens fresh terrain (prime-indexed minimality)
rather than a 5th CSP/ℰ/EC/FIN-Q repackaging.

### Prior progress (for context, not re-derived here)
Current wall unchanged: (CSP) = ℰ-small-only = (EC) = ¬(FIN-Q), certified equivalent, 4th+ round
collapse (see `current.md`, round 9 entries). Live carrier: `covering-small-part-descent` (EC form).
19 lemmas cached in `results/imo-2026-06/lemmas/`. No dead end here that I re-scouted; this report
adds a fifth face candidate (prime-indexed minimal-counterexample via aimo-0030's Claim-3 mechanism)
that has not yet been tried.

### Small-case / intuition notes
No new numerics run this round (terrain/literature scouting only, per assigned lens). Prior rounds'
numeric confirmation of CSP (0 counterexamples across 29+ seeds) stands unchanged and unre-verified
by me this round.
