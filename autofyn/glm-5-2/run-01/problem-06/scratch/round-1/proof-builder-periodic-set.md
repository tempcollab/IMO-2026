# proof-builder report — periodic-set-iteration (imo-2026-06, round 1)

## What proved (rigorous, self-contained)

**Theorem 1 (periodic-set-iteration) — FULLY PROVED.** Let A ⊆ ℤ be nonempty, L-periodic; R = A∩[0,L) = {r_1<…<r_T}. Then f_A(x)=min{y∈A:y>x} iterated from any x_0∈A gives x_{k+T}=x_k+L for all k≥0 (periodic from k=0, no pre-period). Mechanism: residue map is the cyclic successor τ(r_i)=r_{i+1} (wrap r_T→r_1 in next period), a single T-cycle by construction; displacement over one cycle telescopes to L. Written to `results/imo-2026-06/lemmas/periodic-set-iteration.md` for reviewer certification. Cross-checked numerically on a_1=15 (R={0,6,10,12,15,18,20,24} mod 30, T=8, orbit 15,18,20,24,30,36,40,42,45,… matches empirical greedy exactly, x_{k+8}=x_k+30 from k=0).

**Reductive frame (clean).** Greedy = a_{n+1}=min(A_n∩(a_n,∞)), A_n={m: gcd(m,a_i)>1 ∀i≤n}. (A_n) decreasing chain of periodic sets, each a finite union of APs with period M_n=rad(∏a_i). A_n nonempty (bounded-diff lemma, re-proved inline): next multiple of R=rad(a_1) after a_n is admissible, so a_{n+1}−a_n≤R.

**Profinite compactness point (clean topological statement).** Viewing A_n as clopen Â_n in Ẑ, decreasing nonempty closed sets in compact Ẑ ⇒ Â_∞=∩Â_n≠∅.

**Conditional reduction (B1 ⇒ candidate periodic set exists).** Assuming B1 (finite kernel S⊇P_1, every a_n divisible by some p∈S): the S-support family F_n⊆2^S\{∅} is monotone in a finite set ⇒ stabilizes to F_∞ at N_1. A^{(S)}={m: supp(m)∩S hits every s∈F_∞} is a well-defined L-periodic set, L=∏S, to which Theorem 1 applies. A^{(S)}⊆A_n for n≥N_1.

## Exact gaps (honest)

- **[GAP-A — distinctive gamble shown insufficient]** The profinite-compactness escape does NOT close the problem on its own. Compactness gives a profinite point ẑ∈Â_∞ (a consistent residue mod each M_n), NOT a finite-period set containing the orbit. Â_∞ need not contain any genuine integer (no fixed m has gcd(m,a_n)>1 for all n in T>1 cases), and the orbit (a_n) is NOT contained in Â_∞ (a_n drops out of Â_m for m>n). Made explicit and honestly abandoned as a standalone route; falls back to B1.

- **[GAP-B — shared B1]** Finiteness of kernel S. Not proved here (shared with all routes).

- **[GAP-C — free-rider sub-gap]** Even granting B1, must show no m∈(a_n,a_n+R] lying in A_n\A^{(S)} is admissible for large n (free-rider primes in past terms could let a candidate hit a_i via a non-S prime, stealing the greedy from the S-admissible candidate). Candidate mechanism (growth of past-term multiplicities vs O(log a_n) large primes of m) sketched, not proved. Shared with bounded-diff-finite-state step 3.

- **[GAP-D — from-n=1]** Theorem 1 gives periodicity from k=0 *relative to entry index N*, i.e. a_{n+T}=a_n+L for n≥N. Elevating to n≥1 needs N=1. Two routes sketched (injectivity of τ = bijection-from-n1's wall; direct induction from a_1), neither closed.

## Conditional conclusion proved

(B1) + (free-rider sub-gap) ⇒ ∃ N,T with a_{n+T}=a_n+L for all n≥N (eventual periodicity), via stabilization of F_n + Theorem 1. From-n=1 (GAP-D) and B1/C themselves remain open.

## Certified / shared lemmas

- **Proposed for certification: Theorem 1 (periodic-set-iteration)** at `results/imo-2026-06/lemmas/periodic-set-iteration.md`. This is the route's clean reusable contribution — the lift=L / from-n=1 mechanism needed by bounded-diff-finite-state, hitting-set-monovariant, bijection-from-n1. Reviewer to certify.
- Bounded-diff lemma (a_{n+1}−a_n≤rad(a_1)) re-proved inline; owned by bounded-diff-finite-state builder, not re-certified.

## Self-assessed status

**partial.** Theorem 1 is a complete, rigorous, promotable contribution. The number-theoretic Part II is carried as far as it honestly goes: the distinctive profinite-compactness gamble is made explicit and shown insufficient on its own (the orbit is not in Â_∞); the conditional reduction to B1 is rigorous up to the free-rider sub-gap; B1, the free-rider sub-gap, and from-n=1 remain open. No overclaiming.

Main approach file: `/home/agentuser/repo/results/imo-2026-06/approaches/periodic-set-iteration.md`
Lemma file: `/home/agentuser/repo/results/imo-2026-06/lemmas/periodic-set-iteration.md`
