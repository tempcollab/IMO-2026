# Explorer report: fresh top-level framing for imo-2026-06 (round 3)

## Summary verdict
I did **not** find a genuinely different framing that avoids the shared wall. Every
promising lead I traced — analytic/sieve counting, compactness on "primes dividing
a_n eventually," finite-automaton/pigeonhole on a bounded state space, and a
backward "guess T, L" approach — either (a) is provably equivalent to
P-Confinement / Antichain Stabilization once made precise, or (b) is a repackaging
of the already-reviewer-confirmed-dead "witness-debt charging" argument. I *did*
find two crux transplants that are genuinely different in **technique** (not just
dressing) from the antichain/signature machinery the rest of the field uses; they
don't bypass the wall but could give a cleaner attack surface on it. Full detail
below, organized by the five directions in my brief.

## 1. Direct analytic/sieve counting on gap + growth rate — DEAD END, already refuted
The natural version of this is exactly the "witness-debt charging" argument:
charge each new prime that must enter a live generator against the O(log a_n)
budget of "room" the bounded gap (`lemmas/gap-bound.md`, a_{n+1}-a_n ≤ L_0) leaves
per step. `current.md` records this was independently reviewer-confirmed dead
**twice**, in two different dressings (`antichain-signature-closure`'s and
`dilworth-antichain-bound`'s versions): the per-step budget is not n-independent,
it grows with n, so no finite total bound follows. A genuine sieve/PNT-style
argument (count primes ≤ x via π(x) ~ x/log x, argue "new primes are sparse
so must run out") is the same idea in different clothing — it still needs a
budget argument bounding *how many* new primes can enter *ever*, and the reviewer
has already shown the natural budget isn't finite. I did not find a repair. This
avenue is closed unless someone finds a genuinely different charging quantity
(not O(log a_n) per event) — I looked for one and didn't find a candidate.

## 2. "Eventually finitely many primes divide a_n" via compactness — equivalent to the wall, not new
This is just P-Confinement stated differently: "the set of primes ever appearing
in a *live minimal generator*'s factorization is eventually confined to a fixed
finite set" is literally the PC hypothesis in `lemmas/pc-implies-theorem.md`.
Note carefully: it is **not** true that only finitely many primes divide the a_n
overall (a_n grows without bound and can pick up new large prime factors freely
as *non-minimal*, dominated terms) — the real claim only needs to control primes
appearing in inclusion-minimal generator sets, which is exactly the antichain
machinery. So this framing collapses into the sibling's territory immediately;
no independent route found.

## 3. Finite-state automaton on residues mod M — equivalent to the wall, confirmed by a crux parallel
This is also what `signature-stabilization-and-crt-sufficiency.md` already builds
(residues mod L_P = ∏_{p≤L_0} p). A crux from **USA TSTST 2011** (`aimo-0648`,
domain number_theory) is a clean instance of the *general principle* this
framing relies on: a linear recurrence x_n = ⌊(sum of k earlier bounded
terms)/k⌋ is shown eventually periodic by (i) observing the terms stay in a
fixed interval [A,B] forever (so the state space is finite, hence eventual
periodicity is automatic by pigeonhole), then (ii) pinning the exact eventual
behavior with an extremal (max-term) + Bézout argument. Applied to our problem:
step (i) is exactly "the state (a_n mod L_P, or equivalently which generator-set
signatures are live) lives in a finite space" — which is precisely P-Confinement
again. So the automaton framing is real but it does not supply a *new* argument
for why the state space is finite; it just restates the target. Not independently
useful beyond confirming the target's shape is the standard one for this class of
problem.

## 4. Crux corpus search — closest genuinely different technique found
Searched `past_crux_moves_database.json` across number_theory / combinatorics /
algebra for keywords: greedy, eventually periodic, coprime, gcd, antichain,
covering system, residue class, density, minimal element, stabiliz*, finite
automaton, compactness, numerical semigroup. Two hits stand out as **technique-
different** from the antichain/signature apparatus (they decompose the problem
prime-by-prime or via a monotone divisor-chain, rather than via inclusion-minimal
prime-SETS):

- **`aimo-0477` (IMO SL 2018 N-something, "eventually a_n = a_{n+1}").**
  Crux techniques: (i) track d_n := gcd(a_1, a_n) and show, for *every* prime p
  separately, v_p(d_n) = min(v_p(a_1), v_p(a_n)) is nondecreasing, so d_n | d_{n+1}
  — an ascending chain of divisors of the *fixed* a_1, which must stabilize
  (finitely many divisors of a_1); (ii) once stabilized, write a_1 = dα, a_n = dβ_n
  with gcd(α,β_n)=1 and get β_{n+1} | β_n from integrality, a *descending* divisor
  chain that must also stabilize. Two nested finite divisor-chain pigeonholes,
  each on a single fixed number's divisor lattice — no antichain-of-sets language
  at all.
  **Relevance check**: our problem's per-prime valuations v_p(a_n) are not
  obviously monotone in the same way (there's no integrality-of-a-sum constraint
  forcing it), so the transplant is not literal. But the *shape* — decompose into
  finitely many single-prime divisor-chain arguments over p ∈ P = primes ≤ L_0,
  each with its own simple monovariant, then recombine via CRT — is a genuinely
  different decomposition axis than "antichain of minimal prime-SETS." I did not
  find the right monovariant per prime for our recursion (unlike aimo-0477, our
  defining condition is a covering condition — "shares a prime with every earlier
  term" — not a sum-integrality condition, so there's no obvious analogue of "the
  term of strictly minimal valuation breaks integrality"). Flagging as worth a
  dedicated look next round: **does v_p(a_n) or "is p ever again the unique shared
  prime with some specific earlier a_i" have a forced eventual monotonicity for
  each fixed p ∈ P, proved independently of the other primes?** This would let a
  future approach avoid the antichain's combinatorial-explosion-over-subsets
  entirely and instead run |P| ≤ π(L_0) independent, much simpler one-prime
  arguments — a real reduction in complexity even if it turns out to face its own
  version of the wall.

- **`aimo-0421` (Germany TST 2022, infinite-set gcd-pigeonhole).** Technique:
  for a fixed a in an infinite set S, {gcd(a,s): s∈S} is a finite set of divisors
  of a, so pigeonhole over infinitely many s gives infinitely many s with the same
  gcd(a,s). This is the general-purpose fact "gcd against a fixed number takes
  finitely many values" — already implicitly used throughout the existing field
  (e.g. `gap-bound.md` Step 1 uses gcd(a_i,a_1)>1 forcing a shared prime in the
  *finite* set S=primes(a_1)). Not independently new content, but confirms that
  pigeonholing gcd(a_1, a_n) (rather than the antichain of ALL minimal generators)
  is a recognized, load-bearing move elsewhere — reinforcing the aimo-0477 lead
  above as the more promising one to actually chase.

- **`aimo-0813` (IMO SL 2007, functional equation via numerical-semigroup-style
  argument).** "Take the minimal element d of an addition-closed subset of N,
  show the subset is exactly the multiples of d." Checked for transfer: our
  problem's "valid next values" set is not addition-closed in any useful sense
  (it's a covering/gcd condition, not a sum condition), so I could not construct
  an analogous minimal-generator-of-a-numerical-semigroup argument. Dead end,
  reported so it isn't retried.

- **`aimo-0648`** — see §3 above, the bounded-interval + extremal-pigeonhole
  eventual-periodicity template; real but not independent of the wall.

No hit in the corpus attacks a "smallest integer satisfying a coprimality-to-all-
previous-terms condition" recursion directly — this exact recursion shape (as
opposed to sum-integrality or divisibility-of-partial-sums shapes) does not appear
to have a close pre-2026 analogue in the corpus. This is itself useful negative
information: don't spend more budget searching the corpus for a closer structural
match; the closest matches are the ones above.

## 5. Backward "guess T, L, construct" — low value, doesn't shortcut the gap
If eventual periodicity a_{n+T}=a_n+L holds, then necessarily (once in the
periodic regime) the multiset of gaps {a_{n+1}-a_n : n=N,...,N+T-1} sums to L, and
by `gap-bound.md` each gap is ≤ L_0=rad(a_1), so L ≤ T·L_0. Also T must be a period
of the eventual valid-residue set G mod L_P (from
`signature-stabilization-and-crt-sufficiency.md`), so T | (a divisor structure of)
L_P = ∏_{p≤L_0} p, or more precisely T is the order of the periodic pattern that
G induces — i.e. T can be taken to divide L_P (residues mod L_P repeat with
period exactly L_P, though the *true* minimal period could be a proper divisor).
This pins down **candidate shapes** for T and L (T | L_P, L = T · (density of G in
Z/L_PZ)) but doing this "backward" presupposes G is already known to be the
eventual valid set, which is exactly what No-Escape / PC establishes forward.
Working backward from a guessed (T,L) and trying to *verify* it directly for
general a_1 requires already knowing the eventual generator antichain to compute
G — so this does not give an independent existence proof; it's a restatement of
the forward machinery's output, useful at most as a sanity-check / description of
what the final theorem's constants look like, not as a new proof route. Not
recommended as a round focus.

## Recommendation for next round
1. **Best lead**: dedicate an approach to the single-prime decomposition inspired
   by `aimo-0477` — for each fixed p ∈ P = {primes ≤ L_0} independently, study
   whether "p ∈ primes(a_n)" or a refined per-prime state has a forced eventual
   monotonicity/stabilization, proved by a direct argument specific to that one
   prime (not via the antichain-of-sets object). Even if it re-derives PC in the
   end, decomposing into |P| independent one-prime arguments may be tractable
   where the joint combinatorial-subset argument isn't — this is genuinely a
   different proof *shape*, not just different words for the same object.
2. Do **not** re-attempt: witness-debt/charging-budget arguments (dead twice,
   confirmed by reviewer with an actual re-derivation both times), sieve/PNT
   density counting (same budget problem), numerical-semigroup/addition-closure
   framing (no transfer found — the condition isn't additive), or literal
   transplants of aimo-0680-style difference-quotient identities (already refuted
   by explicit counterexample in `dense-signature-vanishing`).
3. If pursuing (1) stalls too, it's worth explicitly recording in `current.md`
   that **all five prescribed alternative-framing directions were checked this
   round and found equivalent-to-or-weaker-than the existing PC/Antichain-
   Stabilization wall**, which is itself useful signal: the wall is very likely
   the problem's actual mathematical content (IMO P6/hard difficulty problems
   often do have one genuine hard combinatorial core), so future rounds may get
   more value from a fourth *independent proof attempt at PC itself* (e.g. via
   the per-prime monovariant above) than from further top-level reframing.
