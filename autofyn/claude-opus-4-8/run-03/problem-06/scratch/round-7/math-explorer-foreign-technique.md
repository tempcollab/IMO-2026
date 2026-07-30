## imo-2026-06 — foreign-technique hunt for the single wall

Context recap (from current.md / run_state.md): the ONE remaining wall, 3 certified-equivalent
faces — (6b) contradiction from an unbounded family of bad terms [covering-small-part-descent];
(FIN-W) infinite branch = a "star": a hub term B small-disjoint (shares no prime ≤ P_max) from an
infinite family of terms all divisible by ONE fixed large prime q>P_max, in one residue class mod
L_0 [bad-residue-witness-index]; (DESC): a bad window has no minimum [minimal-linking-prime-extremal].
Global Σ1/p² capacity and pure covering/Helly (Prop D) are PROVEN dead for it. aimo-0016's
infinitely-often⇒always template does NOT transplant (no per-index local recurrence). I searched the
crux corpus (domain=number_theory, combinatorics; subtopics size-bounding-and-descent,
invariants-and-monovariants, extremal-principle, sequences-and-recurrences, processes-and-algorithms,
zsigmondy-and-primitive-divisors, pigeonhole, double-counting) plus knowledge_base.md for a load-bearing
move that could crack this wall by a mechanism genuinely different from static covering/density.

### Distinct openings (foreign-technique candidates)

**1. Minimal-counterexample + forced-residue-exclusion bootstrap (aimo-0009, IMO-SL, "eventually
periodic sequence with a_{a_i}≤n+i−1 bound").** Borrowed idea: assume a minimal index i violating
the target bound; use the sequence's OWN periodicity plugged into the hypothesis at *shifted* indices
to show a_i cannot lie in a whole BLOCK of residues mod n (not just one value) — this over-shoots the
naive violation into a much stronger one (a_i ≥ 2n+1), which then forces the SAME violation down at
i=1 via monotonicity, closing by minimality. Mechanically this is: minimal counterexample + periodicity
+ "rule out an entire residue block" (not a single residue), i.e. a STRONGER exclusion than plain
pigeonhole gives, obtained by using several shifted instances of the hypothesis at once.
  Adaptation attempt: take the *lexicographically minimal* bad configuration (q*, hub-window-index)
  per `minimal-linking-prime-and-window-cap.md` (q* already gives a non-symmetric floor). Try to run
  several SHIFTED instances of F1/GPC (every pair of terms shares a small-or-≥q* prime) against the
  known mod-L_0 periodicity of S(·) to exclude a whole block of residues mod L_0 for the hub's witness
  index, forcing the witness into a residue class that is already known to be good (covering) —
  contradiction. HONEST STATUS: I could not complete this reduction in exploration time; the
  aimo-0009 proof leans on a *linear inequality chain* (a_i ≤ n+i-1, a_{i+1}-a_i bounds) that has no
  literal analogue here (our object is a divisibility/covering condition, not a numeric inequality on
  indices) — the "shift-and-combine several hypothesis instances to over-exclude" MECHANISM is
  transplantable in spirit, but the specific overshoot computation (a_i≥2n+1) does not carry over
  mechanically; someone would need to find the actual over-exclusion inequality for our covering
  condition. Flag as PROMISING BUT UNVERIFIED, not a known dead end.

**2. Lexicographic-minimal + explicit local rewrite / exchange argument (aimo-0960 "minimal-length
representation, lex-least exponents, local rewrite lowers the multiset"; also aimo-0666/aimo-0854
leximinimal + local reachability/exchange).** Borrowed idea: rather than *finding* a smaller bad
partner passively (which is what `bad-partner-and-ascent.md` already does, and which the round-4/5
reviewers found is SYMMETRIC — the partner relation gives no strict descent), actively CONSTRUCT an
explicit rewrite of the presumed-minimal bad configuration that is provably smaller in a chosen order,
by design asymmetric (an exchange operator, not an existence claim). Concretely: take the
lexicographically-minimal (q*, window-index k) bad pair (q* from Lemma A, well-ordered; k the smaller
window index among the pair). Instead of asking "does a smaller partner exist" (symmetric), actively
construct a candidate integer via a determined operation (e.g. replace the hub's large-prime factor q
by a smaller admissible large prime, or peel q out and substitute the cofactor's own witness) and show
it is BOTH a term (via REAL clause (c)) AND strictly (q*,k)-smaller AND still bad — this is a genuine
descent by an explicit rewrite, not a passive "exists a partner," so it could break the symmetry trap
that killed the value-ascent route in rounds 4–5. HONEST STATUS: I did not verify such a rewrite exists;
this is a candidate MECHANISM (active construction vs. passive partner-finding) worth trying, distinct
from anything in the population — flag as an opening, not a result.

**3. Discharging / injective-charging bound on how many times ONE large prime can be load-bearing
(aimo-0558, aimo-0718, aimo-0099 "injective mapping bounds a closure-linked set's size").** Borrowed
idea: bound the SIZE of a suspicious set by injecting each of its elements into a DIFFERENT finite
resource (a distinct earlier term, a distinct window, a distinct small prime). I tested whether this
kills the star / Lemma-6 geometric family directly: the family m, m·r, m·r², … all have primes(m·r^k)
= primes(m) EXACTLY (fixed finite set, independent of k) — so the "bridge prime" linking the hub B to
each family member is the SAME single fixed prime for every k. There is no growing resource to charge
against (no injection is forced — reusing one q infinitely often across k is completely consistent with
any finite-charging scheme). CONCLUSION: charging/injection does NOT touch the Lemma-6 orbit; it can at
best bound the number of DISTINCT residue classes / DISTINCT hubs, not rule out one hub, one bridge
prime, infinitely many family members. This matches the round-5 finding that the orbit's capacity
contribution is density→0 anyway — charging is REDUNDANT with the already-dead capacity route here.
DEAD END for this specific configuration (verified by direct inspection, not just cited).

**4. Zsigmondy / primitive-divisor bound (aimo-0157, aimo-0611).** Checked: both source problems rely
on values of the form a^n − b^n or "term grows past the product of all earlier terms, forcing a new
prime to appear to higher exponent." Neither transplants: our terms are not powers of a fixed base, and
"the sequence is defined by smallest-integer-satisfying-a-property," not a fast-growing product, so
there's no exponent-growth mechanism to force a genuinely NEW primitive prime. DEAD END on inspection,
do not pursue.

**5. Vieta jumping / infinite descent on a symmetric Diophantine relation (aimo-0276, aimo-0313,
aimo-0783).** Checked: these require a genuine ALGEBRAIC (quadratic, symmetric) relation between two
variables to jump on. Our object is a set-covering/divisibility condition with no polynomial relation
between hub and witness values. No natural quadratic to jump on. DEAD END, do not pursue.

**6. aimo-0648 (USA TSTST 2011, floor-average recurrence, eventually periodic via max-value
propagation + Bezout shift by 1 mod T).** Mechanism: once periodic, the term at the GLOBAL MAXIMUM
forces every one of its d_i-predecessors to also be the max; a Bezout combination of the gaps ≡1 (mod
T) then propagates "is-max" backward one full residue at a time, so eventually every residue is max,
i.e. the sequence is constant. Interesting "propagate an extremal VALUE property backward through a
linear combination of a periodic structure" mechanism — but it needs an averaging/floor recurrence
(a genuine functional relation on values) that our greedy gcd-covering process does not have (there is
no formula for a_{n+1} in terms of earlier a_i's, only a search condition). Does not obviously
transplant; flag as a LOW-CONFIDENCE opening only if someone can recast "covering-ness of a residue
class" as a value propagated by a linear/Bezout combination of the *known* mod-L_0 period structure —
speculative, not verified.

### Cheap-kill candidates
None obvious beyond what's already certified (F1, GPC, q* floor, per-window cap). The Lemma-6 orbit
inspection above (#3) is itself a small cheap-kill: it PROVES that no charging/injection scheme can see
that particular family, saving a round of building that route.

### Candidate technique(s) to hand the outliner
Priority order: (1) the aimo-0009 shift-and-overshoot mechanism recast for a covering condition
(most novel, most aligned with "genuinely foreign," unverified but not contradicted); (2) the
aimo-0960-style active/explicit rewrite operator on the lexicographically-minimal (q*, window-index)
configuration, replacing the passive bad-partner-and-ascent symmetric relation with a designed
asymmetric construction. Both are UNTESTED — an approach slug attempting either should say so plainly
and expect to spend the round finding the concrete overshoot inequality / rewrite operator, not
assume it exists.

### Knowledge-base entries relevant
- "Pigeonhole / extremal principle: take the maximal or minimal element" (Combinatorics section) —
  underlies both openings #1 and #2, but note plain minimality already tried (symmetric trap); the
  NEW ingredient must be the shift-and-overshoot or the explicit-rewrite mechanism, not bare minimality.
- No LTE/Zsigmondy/Vieta/Dirichlet entries apply (checked and ruled out, see #4, #5).
- CRT / modular-arithmetic entry underlies the existing certified mod-L_0 periodicity (already used).

### Analogous past problems (cruxes)
- **aimo-0009** (IMO-SL, algebra/size-bounding-and-descent) — closest genuine mechanism-analog found:
  minimal-counterexample bootstrapped through periodicity to over-exclude a whole residue block. Not a
  literal template (different object: numeric inequality vs. covering condition) but the MECHANISM
  (combine several shifted hypothesis-instances to force a stronger exclusion than plain pigeonhole)
  is worth transplanting in spirit. UNVERIFIED for our problem.
- **aimo-0960** (algebra, symmetric-functions-and-substitution / sequences-and-recurrences) — closest
  analog for breaking a symmetric-descent trap: lexicographically-minimal representation + an explicit
  LOCAL REWRITE (not a passive partner-existence claim) that strictly lowers the order, contradicting
  minimality. Directly relevant to the round-4/5 finding that bad-partner-and-ascent is symmetric and
  gives no descent — this crux shows the standard fix (replace "find a partner" with "construct a
  rewrite"). UNVERIFIED for our problem but structurally the best-matched fix for the known trap.
- **aimo-0648** (USA TSTST, algebra/sequences-and-recurrences) — weaker analog; propagate an extremal
  VALUE property backward via a Bezout/periodic-gap combination. Needs a value recurrence we don't
  have; low confidence, listed for completeness only.
- Ruled out as NOT analogous after inspection: aimo-0157, aimo-0611 (Zsigmondy — no exponent-growth
  mechanism here); aimo-0276/aimo-0313/aimo-0783 (Vieta jumping — no polynomial relation between hub
  and witness); aimo-0678 (already checked in round 5, doesn't transplant — deterministic-state
  periodicity needs a FIXED finite state space, which our infinite-witness star denies).

### Prior progress
Current best (unchanged from round 5/6, see current.md): full scaffold certified (ENUM, PER); crux
reduced to (CSP)/(FIN-W)/(DESC), all equivalent; sub-gap (6a) unboundedness CLOSED via Lemma 6
(bad-signature-geometric-family.md: bad m ⇒ m·r^k bad, same signature/witness, unbounded family for
free). The SOLE remaining wall is the single value-level contradiction, none of whose 3 phrasings have
been cracked in 2 prior collapse cycles.

### Dead ends (do not retry)
- Global Σ1/p² capacity counting (certified dead, round 2).
- Pure covering-set/Helly/sunflower argument (Prop D barrier, round 2).
- aimo-0016 infinitely-often⇒always template (checked round 5, does not transplant — no per-index
  local recurrence in our bad family).
- Charging/injection on the Lemma-6 geometric orbit specifically (checked THIS round, #3 above): the
  orbit m·r^k has a CONSTANT prime set independent of k, so there is no growing resource to charge
  against — any injective/discharging scheme sees nothing new here and reduces to the already-dead
  capacity route.
- Zsigmondy/primitive-divisor mechanisms (checked this round, #4): no exponent-growth structure exists
  in this problem to force a genuinely new primitive prime.
- Vieta jumping (checked this round, #5): no polynomial/symmetric-quadratic relation between hub and
  witness values to jump on.

### Small-case / intuition notes
Not re-run numerically this round (prior rounds already verified CSP holds with 0 counterexamples on
20+ seeds up to thousands of terms — still just evidence, not proof). The Lemma-6 orbit inspection (#3)
is a NEW small structural fact worth recording precisely: for the specific family m·r^k arising from
Lemma 6, the *set* of primes dividing the family member never changes with k — only the VALUE grows.
This means any attempted contradiction from "this orbit is infinite" must come from a value-level fact
(e.g. F1 forcing a shared prime with growing k, but the shared prime set is also fixed, so F1 gives
nothing new per k) — reinforcing the reviewers' conclusion that (6a)'s family is not itself a
contradiction source; the crux genuinely needs a fresh mechanism at the (CSP)/existence level, i.e.
before any bad term exists at all, which is why openings #1 and #2 (attacking the MINIMAL bad
configuration's existence, not an already-produced infinite family) are more promising than trying to
re-analyze the Lemma-6 orbit itself.
