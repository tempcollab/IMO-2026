# Lemma (finite connector-pool periodicity) — (FIN-Q) ⟹ theorem

**Certified** (proof-reviewer, round 7). Source: window-purity-class-cycle Lemma 2. Strict
strengthening of the certified `finite-witness-periodicity.md` (weaker hypothesis).

Notation as in `finite-witness-periodicity.md`: E_∞={m>1:gcd(m,a_i)>1 ∀i}; P:=primes(a_1); P_max:=max P;
L_0:=∏_{p≤P_max}p; S(m):=primes(m)∩[2,P_max]; for a term a_i, Q_i:=primes(a_i)∩(P_max,∞). For a residue
r∈ℤ/L_0ℤ, S(r) is well-defined; R_bad:={r:S(r) non-covering}; W(r):={i:primes(a_i)∩S(r)=∅};
R'_bad:={r∈R_bad : E_∞ meets class r}. Imports: ENUM, PER, the membership dichotomy (★) below (all from
the certified Reduction Lemma `finite-witness-periodicity.md`), and residue-locality of S.

For r∈R'_bad define the **large connector pool** Q(r) := ⋃_{i∈W(r)} Q_i.

**(FIN-Q):** for every E_∞-inhabited bad class r∈R'_bad, the pool Q(r) is finite.

Recall the certified membership dichotomy: for r∈R'_bad and m≡r (mod L_0),
> (★)  m∈E_∞ ⟺ for every i∈W(r), some q∈Q_i divides m;

with companions: if r covering then every m≡r (m>1) lies in E_∞; if E_∞ misses class r then no m≡r lies
in E_∞.

## Statement
(FIN-Q) implies E_∞ is tail-periodic from a_1 with period M := L_0·∏_{q∈Q_rel} q, where
Q_rel := ⋃_{r∈R'_bad} Q(r); hence by ENUM+PER there exist T,L with a_{n+T}=a_n+L for every n
(L=M, T=#(E_∞∩[a_1,a_1+M))≥1). (FIN-Q) is **strictly weaker** than (FIN-W): (FIN-W)⟹(FIN-Q) [W(r) finite
⟹ Q(r) a finite union of finite sets, finite], but Q(r) may be finite with W(r) infinite (infinitely many
witness colors drawing on one fixed finite set of large primes). So (CSP)⟹(FIN-W)⟹(FIN-Q)⟹theorem.

## Proof
Assume (FIN-Q). R'_bad⊆R_bad is finite (≤L_0, residue-locality) and each Q(r) finite, so Q_rel is a
finite union of finite sets, hence finite. Set M=L_0·∏_{q∈Q_rel}q (squarefree: L_0's primes ≤P_max,
Q_rel's >P_max, disjoint). Fix m>1, r=m mod L_0; we show m∈E_∞ is a function of m mod M.

- **r covering:** by the covering companion of (★), m∈E_∞ unconditionally — a function of r=m mod L_0 | M.
- **r∈R'_bad:** by (★), m∈E_∞ ⟺ ∀i∈W(r) ∃q∈Q_i: q|m. Take m'≡m (mod M). For every q∈Q_rel, q|M so
  q|m ⟺ q|m'. Each i∈W(r) has Q_i⊆Q(r)⊆Q_rel, so "∃q∈Q_i: q|m" ⟺ "∃q∈Q_i: q|m'" separately for each i;
  the (possibly infinite) conjunction over the fixed index set W(r) therefore holds for m iff for m'.
  W(r) and each Q_i depend only on r=m mod L_0 | M = m' mod L_0. Hence m∈E_∞ ⟺ m'∈E_∞.
  **Key point:** the argument never needs W(r) finite — an infinite conjunction of conditions each
  determined by m mod M is itself determined by m mod M.
- **r∈R_bad, E_∞ misses class r:** every m≡r has m∉E_∞ (class-miss companion of (★)); constant, a
  function of m mod L_0 | M.

In all cases m∈E_∞ is a function of m mod M, so for x≥a_1: x∈E_∞ ⟺ x+M∈E_∞ — E_∞ tail-periodic from a_1
with period M. E_∞∩[a_1,∞) is infinite (contains every k·a_1). Apply PER (E=E_∞, a=a_1, L=M): its
increasing enumeration b_1<b_2<… has b_{n+T}=b_n+M, T=#(E_∞∩[a_1,a_1+M))≥1; by ENUM this enumeration is
a_1,a_2,…, so a_{n+T}=a_n+M for all n. ∎

## Scope / caveats
- Gap-free; supersedes `finite-witness-periodicity.md` (any use of (FIN-W)⟹theorem is a special case).
  Rigorises "single-sided infinite witnessing is harmless": an inhabited bad class obstructed by infinitely
  many witness colors that draw on only finitely many distinct large primes contributes exactly the finite
  factor ∏Q(r) to the period and yields NO obstruction to periodicity.
- Residual crux = **¬(FIN-Q)**: an inhabited bad class r_0 with Q(r_0) INFINITE (infinitely many distinct
  large connector primes across its witness colors). Strictly harder to arrange than ¬(FIN-W). NOT closed.
- Uses no dead route (not covering/Helly, not global Σ1/p² capacity).
