# Lemma (finite-witness periodicity) — (FIN-W) ⟹ theorem

**Certified** (proof-reviewer, round 5). Source: bad-residue-witness-index Reduction Lemma.

Notation: greedy sequence a_1<a_2<…; E_∞={m>1:gcd(m,a_i)>1 ∀i}; P:=primes(a_1); P_max:=max P;
L_0:=∏_{p≤P_max}p; S(m):=primes(m)∩[2,P_max]. For a term a_i, Q_i:=primes(a_i)∩(P_max,∞). A term m is
**bad** iff some term B has primes(B)∩S(m)=∅. For a residue r∈ℤ/L_0ℤ, S(r):=S(m) for any m≡r
(well-defined, certified `csp-implies-theorem.md` Step 1a); r is **non-covering** iff S(r) misses some
color; R_bad:={r : S(r) non-covering}; W(r):={i : primes(a_i)∩S(r)=∅}. Imports: ENUM, PER, F1, GPC,
and "S(m) depends only on m mod L_0" (all certified).

**(FIN-W):** for every term m, W(m mod L_0) is finite — equivalently, every term is small-disjoint from
only finitely many terms.

## Statement
(FIN-W) implies E_∞ is tail-periodic from a_1 with period M := L_0·∏_{q∈Q_rel} q, where
Q_rel := ⋃_{r∈R'_bad} ⋃_{i∈W(r)} Q_i and R'_bad := {r∈R_bad : E_∞ meets class r}; hence by ENUM+PER
there exist T,L with a_{n+T}=a_n+L for every n (L=M, T=#(E_∞∩[a_1,a_1+M))≥1). (CSP — no bad term — is
the special case R'_bad=∅, M=L_0; so (CSP)⟹(FIN-W)⟹theorem and (FIN-W) is strictly weaker.)

## Proof
Under (FIN-W) each W(r) (r∈R'_bad) is finite and each Q_i finite; R'_bad⊆R_bad is finite (≤L_0), so
Q_rel is a finite union of finite sets, hence **finite**. Set M=L_0·∏_{q∈Q_rel}q (squarefree; L_0's
primes ≤P_max, Q_rel's >P_max, all distinct). Fix m>1, r=m mod L_0.

- **r covering:** for every i, primes(a_i)∩S(r)≠∅, and S(r)=S(m)⊆primes(m), so gcd(m,a_i)>1 for all i,
  i.e. m∈E_∞. Determined by r, a fortiori by m mod M.
- **r∈R'_bad:** for i∉W(r), primes(a_i)∩S(r)≠∅ gives gcd(m,a_i)>1 automatically; for i∈W(r), a_i and
  m share no small prime, so gcd(m,a_i)>1 ⟺ some q∈Q_i divides m. Hence (★) m∈E_∞ ⟺ ∀i∈W(r) ∃q∈Q_i:
  q∣m. Every such q∈Q_i⊆Q_rel divides M, so "q∣m" depends only on m mod M; W(r),Q_i depend only on
  r=m mod L_0∣M. So m∈E_∞ is determined by m mod M.
- **r∈R_bad, E_∞ misses class r:** then every m≡r (mod L_0) has m∉E_∞ (else the class is met); a
  constant "false", determined by m mod L_0∣M. ("E_∞ meets class r" is a fixed truth value of r; when
  false, no m≡r lies in E_∞. If some m≡r satisfied (★), the class would be met — so this case is
  exactly the complement of the previous within R_bad.)

In all cases m∈E_∞ is a function of m mod M, so for x≥a_1: x∈E_∞ ⟺ x+M∈E_∞ — E_∞ tail-periodic from
a_1 with period M. E_∞∩[a_1,∞) is infinite (contains every k·a_1). Apply PER (E=E_∞, a=a_1, L=M): its
increasing enumeration b_1<b_2<… has b_{n+T}=b_n+M, T=#(E_∞∩[a_1,a_1+M))≥1; by ENUM that enumeration
is a_1,a_2,…, so a_{n+T}=a_n+M for all n. ∎

## Scope / caveats
- The reduction is gap-free and generalizes `csp-implies-theorem.md`. The residual crux is **(FIN-W)
  itself** (its infinite-witness branch: a term small-disjoint from infinitely many terms), which the
  source approach reduces by pigeonhole to a "star configuration" that is NOT yet contradicted — the
  field's standing wall, not closed here.
- Uses no dead route (not covering/Helly, not global Σ1/p² capacity).
