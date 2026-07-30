# Recursive good/bad characterization + similarity-closure of E_∞ (TERMINAL — solves P6)

Source: `approaches/smallest-essential-prime-descent.md` (round 10). Reviewer-certified round 10;
every step independently re-derived and numerically confirmed (0 counterexamples for
a_1 ∈ {15,16,17,30,35,45,99,100,210,231}).

Setup: greedy sequence a_1<a_2<…; E_∞ = {m>1 : gcd(m,a_i)>1 ∀i}. By (ENUM) the terms are exactly
E_∞∩[a_1,∞). For m≥a_1: **good** := m∈E_∞ (= a term), **bad** := m∉E_∞. A **move** m→x means
gcd(m,x)=1 and a_1≤x<m. Small prime := ≤a_1; two numbers ≥a_1 are **similar** if they share the same
set of prime divisors ≤ a_1. M := ∏_{p≤a_1} p ≥ 2.

## F2 (goods pairwise non-coprime)
g=a_i, g'=a_j, i<j: the rule gave gcd(a_j,a_i)>1. ∎

## F3
a_1 is a term, so a_1∈E_∞, good. ∎

## F1 (recursive characterization) — the load-bearing bridge
For m≥a_1: **m good ⟺ no good x with a_1≤x<m is coprime to m**; equivalently m bad ⟺ ∃ move m→x to a
good x.
*Proof.* (⟹) m=a_i good; any good x<m is a_l (l<i), gcd(a_l,a_i)>1 by F2. (⟸) If m=a_1, F3. If m>a_1,
the goods <m are {a_1,…,a_j}, a_j the largest; the hypothesis gives gcd(m,a_l)>1 for all l≤j; but a_{j+1}
is the smallest integer >a_j with gcd(·,a_l)>1 ∀l≤j, and m>a_j qualifies, so a_{j+1}≤m; a_{j+1}<m would
be a good strictly between a_j and m (contra maximality), so a_{j+1}=m, good. ∎

## Claim 1 (multiple of a good is good)
n good, n∣n', n'≥a_1 ⟹ n' good. *If n' bad, move n'→x good, gcd(x,n')=1; n∣n' ⟹ gcd(x,n)=1; x,n coprime
goods contra F2.* ∎

## Claim 2 (rs bad ⟹ r²s bad)
rs≥a_1 bad ⟹ move rs→x good; primes(r²s)=primes(rs) ⟹ gcd(x,r²s)=1; x<rs≤r²s, x≥a_1, r²s≥a_1 ⟹ move
r²s→x, so r²s bad. Contrapositive: rs≥a_1 & r²s good ⟹ rs good. ∎

## Claim 3 (n bad, p>a_1 prime ⟹ np bad)
Minimal counterexample (p,n): n bad, np good. Move n→x good, gcd(x,n)=1, a_1≤x<n. If gcd(x,p)=1 then
np→x is a move ⟹ np bad, contra; so p∣x, x=p^r y, r≥1, p∤y. If y=1: x=p^r>a_1, gcd(x,a_1)=1, so x→a_1 is a
move to the good a_1 ⟹ x bad, contra x good; so y≥2. Let α least with y^α≥a_1 (so y^{α-1}<a_1). y^α is bad
(gcd(y^α,np)=1, coprime-goods contra F2 if good). Descent: y^α=y·y^{α-1}<y·a_1≤y·p, times p^{r-1}:
p^{r-1}y^α<p^r y=x<n. By minimality Claim 3 holds for all bad integers <n; induction j=0..r (each
p^j y^α≥a_1, and <n for j≤r-1) gives p^r y^α bad. But x=p^r y ∣ p^r y^α (y∣y^α) with p^r y^α≥a_1, so by
Claim 1 p^r y^α good — contradiction. ∎

## Main claim (similarity closure) — TERMINAL CRUX, PROVED
If a,b≥a_1 are similar then a,b have the same status. Reduce to **(★):** for c≥a_1 and any multiple d of
c similar to c, c and d have the same status (apply to (a,ab),(b,ab); ab similar to both).
*Proof of (★).* Minimal counterexample (c_0,d_0), d_0 minimal. Claim 1 ⟹ c_0 bad, d_0 good; d_0≥2c_0. Pick
prime p∣(d_0/c_0), so d_0/p=c_0u (u≥1) is an integer multiple of c_0, similar to c_0 (small sets squeezed
c_0∣d_0/p∣d_0), d_0/p<d_0. **p≤a_1:** similar ⟹ p∣c_0, and p∣d_0/c_0 ⟹ p²∣d_0; contrapositive of Claim 2
(r=p, s=d_0/p²) gives d_0/p good. **p>a_1:** n=d_0/p≥a_1, np=d_0 good ⟹ (Claim 3) n good. Either way
(c_0,d_0/p) is a smaller counterexample — contradiction. ∎

## Consequence (periodicity + theorem)
For n≥a_1, n and n+M share the same primes ≤a_1 (as p∣M for every small p), so are similar; Main claim ⟹
n∈E_∞ ⟺ n+M∈E_∞. Thus E_∞ is tail-periodic from a_1 with period L=M, and (ENUM)+(PER) give
a_{n+T}=a_n+L for all n with T=#(E_∞∩[a_1,a_1+M))≥1. **This proves IMO 2026 P6.**

Imports: (ENUM) `enumeration-of-E-infinity.md`, (PER) `periodic-set-enumeration.md`.
