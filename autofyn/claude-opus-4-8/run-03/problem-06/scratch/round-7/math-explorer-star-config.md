## imo-2026-06 — lens: directly contradict the star configuration

### Setup recap (verified against the certified lemma chain)
Star config (from `lemmas/finite-witness-periodicity.md` Step 5 / `bad-residue-witness-index.md`):
hub term h (bad, S(h)=s_0≠∅ non-covering), infinite family t_1<t_2<... (all terms of the
sequence), all small-disjoint from h (S(t_j)∩s_0=∅), all ≡ one class mod L_0 (so all with the
SAME small part s_1≠∅, itself non-covering — witnessed by h), all divisible by ONE fixed large
prime q>P_max, in fact all ≡ one fixed residue mod q·L_0 (a single AP). By GPC, a_1∤h, a_1∤t_j
(off-lattice). By Lemma 6, mutual: h witnesses every t_j bad, and vice versa.

### Distinct openings tried this lens

**(1) Greedy-minimality-between-consecutive-m_i.** Since each t_j is *squeezed off the
a_1-lattice* by GPC, it lies in the open window (k_j·a_1,(k_j+1)·a_1) — but this containment is
TRIVIAL for any non-multiple of a_1, not extra leverage by itself (checked: GPC only forbids
a_1|t_j, it does not bound t_j's position beyond that). The genuine content would have to come
from t_j being the SPECIFIC greedy value in its window: every integer strictly between t_j's
predecessor a_{i_j-1} and t_j is *blocked* (fails gcd>1 with some earlier term). I could not turn
this into a contradiction: q|t_j and q|h means compatibility with h is trivially satisfied via q
itself — badness (S(t_j) non-covering) does NOT threaten t_j's validity as a term at all, since
term-validity only needs gcd>1 with every predecessor via ANY prime, small or large. So the
"blocked-integers" structure constrains what ISN'T chosen, not what forces a contradiction on what
IS chosen. This is exactly the unexploited "greedy dynamics" surface the run-state flags as
missing — it looks live in principle but I found no concrete lever; flag as the genuinely open
angle for the outliner, not a dead end but not yet cracked either.

**(2) Pigeonhole from h's finite factorization forcing a shared large prime.** Checked carefully:
this is NOT a fresh handle — it is *already exactly how the star itself is constructed*
(Step 5 of `finite-witness-periodicity.md`/`bad-residue-witness-index.md`: h has finitely many
prime factors, F1 forces each t_j to share one with h, pigeonhole over the infinite family
forces one fixed q). Re-deriving it produces nothing new: q dividing infinitely many terms is
NOT by itself a contradiction — it is exactly what genuine eventual periodicity mod some period M
containing q would look like (an AP of period-M terms). Verdict: **not live as an independent
lever; already saturated inside the star's own derivation.**

**(3) h's own compatible-partner structure.** Since h is a term, `realizability-and-self-dual-
clutter.md` (𝒯⊆𝒞) gives primes(h) covering (meets every color, i.e. every a_i's prime set).
Since S(h) (small part) alone is non-covering (h bad, by definition), the missing colors MUST be
covered by h's LARGE primes Q(h) = primes(h)∩(P_max,∞) — i.e., for every color/index i with
primes(a_i)∩S(h)=∅ (i.e. i∈W(h mod L_0)), some prime of Q(h) divides a_i. This is a real,
previously-unstated LOCAL fact: **h's finitely many large primes must jointly cover the (possibly
infinite) index set W(h mod L_0)**, i.e. W(r) = ⋃_{q∈Q(h)} {i : q|a_i}. Since |Q(h)| is finite (h
is one fixed integer), if W(r) is infinite (the star hypothesis), pigeonhole forces some SINGLE
q∈Q(h) to have {i∈W(r): q|a_i} infinite — this is *identical* to the round-5 derivation (opening
2), so again not new leverage on its own; but it does make explicit that the star's "q" is exactly
one of h's own large prime factors covering one specific missing color of S(h), a fact that could
be sharpened (bound: #colors missed by S(h) ≤ #primes in Q(h), a finite local capacity count —
distinct from the dead GLOBAL Σ1/p² route since it never sums over all h, only fixes one h). This
local capacity fact is UNUSED elsewhere in the population and worth flagging to the outliner as a
possible new local-pigeonhole angle (bound missed-colors-of-h by |Q(h)|, then try to force |Q(h)|
too small vs. the number of colors any bad term must miss) — but I did NOT find how to close it;
report as an opening, not a result.

### Crux-corpus check (subtopic divisibility-and-gcd / pigeonhole)
**aimo-0421** (Bundeswettbewarb-style): infinite set S with 4 distinct elements of differing
pairwise gcds ⇒ ∃ a "balanced triple" a,b,c∈S with gcd(a,b)=gcd(a,c)≠gcd(b,c). Its crux moves are
the CLOSEST genuine analog found:
- *"gcd of a fixed element with a varying one is always a divisor of that fixed element, hence
  finite-valued; pigeonhole over an infinite family forces infinitely many partners to share one
  gcd value."* — this is EXACTLY the move already embedded in the star's construction (opening 2
  above), confirming it is a real, correct, but already-exhausted move for our problem.
- *"When every prime divides only finitely many elements of an infinite set, only finitely many
  elements fail to be coprime to a fixed pair b,c — choose a 3rd element a coprime to both."* —
  I checked whether this TRANSPLANTS to give the contradiction. **It does not, structurally**: in
  aimo-0421's ambient set S, coprime pairs of elements are permitted to exist (S is a generic
  infinite integer set). In our problem, **F1 (every two terms share a prime) certifies that NO
  two terms are EVER coprime** — the term-family is a genuinely *intersecting* family of prime-sets.
  So the "find a 3rd element coprime to both b,c" step is IMPOSSIBLE to execute here by
  construction; the finite-fiber branch of aimo-0421's argument is a dead transplant for this
  problem. This is a useful NEGATIVE finding: it re-confirms (independently of the already-known
  Prop D barrier) that pairwise-intersecting structure is precisely what makes this problem harder
  than generic gcd/pigeonhole set problems, and rules out one more "obvious" borrowed move.
- No other corpus entry in divisibility-and-gcd/pigeonhole/processes-and-algorithms/extremal-
  principle was a genuine match (checked ~130 candidates by keyword; aimo-0421 is the standout).

### Cheap-kill candidates
- None found that close the star directly. The one modest new fact (opening 3: h's finitely many
  large primes must jointly cover W(h mod L_0), a LOCAL finite-capacity constraint on ONE hub) is
  cheap to state but I could not push it into a numeric contradiction (e.g. bounding "missed
  colors of h" vs "|Q(h)|" doesn't obviously exceed available capacity — a bad term could in
  principle miss just ONE color and have Q(h) of size 1, i.e. q alone suffices, no overflow).
- Checked (numerically, see below): whether bad terms occur at all. **0 bad terms found** for
  a_1 ∈ {15,21,33,35,51,55,65,77,85,91,95,99,105,119,143,161,165,187,195,203,209,221,231,255,
  299,323,341,377,391} over 601 greedy terms each (Python/sympy simulation). This is STRONG
  (but unproven, conjectural) evidence that (CSP) — no bad term ever — holds unconditionally, not
  just that the star can't occur. Suggests: proving CSP/(RED_n) directly (reduced-process-identity
  approach, still Elo-top and parked) may be a more tractable target than refuting the star, since
  in every tested instance the phenomenon that would seed a star (a single bad term) never even
  arises. Worth telling the outliner to keep pushing reduced-process-identity's RED_n in parallel
  to any star-refutation approach, not deprioritize it.

### Candidate technique(s)
- Greedy-window minimality (opening 1) — genuinely unexploited, but no concrete lever found this
  round; flagged live for a future dedicated dynamics-focused pass (e.g. explicitly tracking WHICH
  integers between a_{i_j-1} and t_j are blocked and by which earlier term/prime).
- Local finite-capacity pigeonhole on h's own large primes (opening 3) — modest, correct, not yet
  closed; distinct from the dead global Σ1/p² capacity route since it never sums over all hubs.
- Direct proof of CSP (no bad term ever) via reduced-process-identity's RED_n — reinforced by fresh
  0-counterexample evidence; not this lens's focus but worth re-emphasizing to the outliner.

### Knowledge-base entries in play
`Pigeonhole / extremal principle`, `Modular arithmetic, CRT` (knowledge_base.md Combinatorics /
Number Theory sections) — both already in use via GPC/CRT-periodicity machinery; no new KB entry
identified as applicable that isn't already cited by the certified lemmas.

### Analogous past problems (cruxes)
- `aimo-0421` (divisibility-and-gcd/pigeonhole) — closest analog. Crux move "fixed element's
  finite divisor set forces infinite pigeonhole partner" is ALREADY embedded in our star's
  derivation (not new); its complementary "coprime 3rd element" move is PROVABLY INAPPLICABLE here
  because our term family is F1-pairwise-intersecting (no two terms are ever coprime), unlike
  generic S in aimo-0421. Useful negative result, not a route.
- No other corpus entry judged genuinely analogous after filtering ~130 gcd/pigeonhole/processes
  candidates by keyword.

### Prior progress
Unchanged from round 5/6 state (see current.md / run_state.md): (6a) closed (Lemma 6); sole
remaining wall = star non-existence, certified-equivalent to (6b)/(DESC). No new certified result
this round from this lens.

### Dead ends (do not retry)
- Handle 2 (pigeonhole on h's finite factorization) as an INDEPENDENT lever — it is already fully
  baked into the star's own construction; re-deriving it produces nothing new.
- aimo-0421's "finite-fiber branch ⇒ find coprime 3rd element" move — structurally blocked by F1
  (pairwise-intersecting term family); do not have a builder attempt this transplant.
- (Reconfirmed from run history, not re-tested in depth) global Σ1/p² capacity counting and pure
  covering/Helly (Prop D barrier) remain dead for closing the star.

### Small-case / intuition notes (conjectural)
Fresh simulation (this round): 0 bad terms across 29 values of a_1 (15..391, composite with 2-3
prime factors), 601 terms each. Together with round-1/4's earlier 20+-seed checks, this is now
~50 seeds with zero bad terms ever observed — strengthens the conjecture that CSP (not just
FIN-W) holds unconditionally, i.e. the star configuration (and even weaker, ANY bad term) may
simply never be realizable. No proof found this round for why.
