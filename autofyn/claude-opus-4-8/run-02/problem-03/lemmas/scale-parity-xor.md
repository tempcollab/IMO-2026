# Lemma (Scale-parity XOR identity `(⊞)`) — CERTIFIED round 8

**Source:** approaches/even-rank-doublecount.md §2 (Lemmas 2.1–2.2).
**Reviewer status:** verified (algebra re-derived independently; numerics 0/20000 mismatch, n≤5).

## Statement
Let `F = ⊎_{j=0}^n π_j` be any finite multiset of positive reals partitioned into groups
`π_j` (scale-`j` fragments). Sort `F` descending `w_1≥w_2≥…`. Let `N(t)=#{w_i>t}`,
`N_j(t)=#{p∈π_j: p>t}`, so `N=Σ_j N_j`. Then

- **Even/odd-rank level form:** `E(F):=Σ_{i even} w_i = ∫_0^∞ ⌊N(t)/2⌋ dt`, and
  `O(F):=Σ_{i odd} w_i = ∫_0^∞ ⌈N(t)/2⌉ dt`.
- **Scale-parity XOR:** `D̃(F):=O(F)−E(F) = ∫_0^∞ 1[N(t) odd] dt = ∫_0^∞ (⊕_{j=0}^n 1[N_j(t) odd]) dt`.
- **Roots-of-unity form:** with `σ_j:=(−1)^{N_j}`, `D̃(F)=½∫_{(0,W)}(1−∏_j σ_j)dt`, `W=w_1`.

## Proof
`w_{2k}=λ{t: N(t)≥2k}` (since `N(t)≥2k ⇔ t<w_{2k}` for descending sort). Summing and using
`Σ_{k≥1}1[N≥2k]=⌊N/2⌋`, Tonelli gives `E=∫⌊N/2⌋`; likewise `O=∫⌈N/2⌉`. Subtract:
`⌈N/2⌉−⌊N/2⌋=1[N odd]` ⇒ `D̃=∫1[N odd]` (matches certified level-measure form). Since
`N=Σ_j N_j`, parity of `N` is the XOR of the parities `1[N_j odd]`, giving the XOR form;
`1[N odd]=½(1−(−1)^N)=½(1−∏_j σ_j)`. ∎

## Reuse
Game-free, measure-language-free restatement of the lower-bound discrepancy that keeps every
scale's parts separate (NOT a scalar summary of Z). Recasts GAP L as a parity-covering problem
over `n+1` interval-parity functions with shared budget `Σ a_j ≤ n`. The trivial half-bound
`⌊N/2⌋≤N/2` gives only `E≤ΣF/2` (`D̃≥0`); the residual is `2^n−E = D̃/2`, so the constant `1`
(`D̃≥1`) is the entire open content.
