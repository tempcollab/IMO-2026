# Lemma VERT-LOW (LP-vertex reduction of MID-core) — CERTIFIED (round 12)

**Certification (round 12).** Reviewer-verified independently. The reduction is sound:
(i) within a fixed combinatorial type `T` the word `σ` is a *valid* descending order enforced by
the (O) constraints, so the alternating functional `L_T` equals `D` on all of `P_T` (equal values
sit at consecutive positions in a descending sort and cancel `+v−v=0`, so `D=μ{N odd}` agrees with
`L_T` including at ties and at zero-length degenerate boundary points, which sit at the bottom and
contribute `0` without shifting parities); (ii) the admissible refinements are exactly the
positive-coordinate points of `⋃_T P_T` and `D=L_T` there; (iii) a linear functional on a nonempty
compact polytope attains its minimum at a vertex (Fundamental Theorem of LP). Enlarging the feasible
set to the closed polytope only lowers the minimum, so `min over vertices ≥ 1 ⇒ every genuine
refinement has D ≥ 1`; conversely by continuity of `D` (Lemma M) a degenerate vertex is a limit of
genuine refinements, so the two are equivalent. Cheap-kill (exact LP, scipy HiGHS) reproduced:
global `min L_T = 1` for `n=3` (5 F-types) and `n=4` (21 F-types), NO vertex with `L_T < 1`; also
confirmed on independent finer rational grids (n=2 den 6, n=3 den 3): min `D = 1`, no sub-1 vertex.
Admitted.

**Statement.** Fix `n`. A MID-core refinement is `S = F ⊔ B` with `F` the fragments of the top piece
`2^n` (each in `(0,2^{n-1}]`, `ΣF=2^n`, `|F|≥3`) and `B` a refinement of the tail ladder
`C_{n-1}={2^0,…,2^{n-1}}` (`ΣB=2^n−1`), under the cut budget `(|F|−1)+c_B ≤ n`. A **combinatorial
type** `T=(|F|,(k_0,…,k_{n-1}),σ)` fixes the fragment counts and a word `σ` (a descending-consistent
linear order on the labelled pieces). For each `T` let `P_T` be the compact polytope in the
piece-value variables cut out by (E) group sums, (O) descending order per `σ`, (C) box
`0≤v_i≤2^{n-1}`; let `L_T(v)=Σ_{odd pos}v − Σ_{even pos}v` be the alternating functional along `σ`.
Then MID-core (`D(S)≥1` for the residual band `|F|≥3`) is **equivalent** to:

```
        for every type T and every vertex v of P_T,   L_T(v) ≥ 1.        (GAP-EXTR)
```

**Note (ONE-REC is not a facet).** Two fragments of tail group `j` each `>2^{j-1}` would sum
`>2^j = Σ group j`, so "≤1 fragment of group j exceeds `2^{j-1}`" is IMPLIED by (E)+positivity; it
restricts which words `σ` are realisable but adds no binding inequality inside a fixed `P_T`.

**Scope.** Loss-free reduction of MID-core to a finite explicit vertex bound (GAP-EXTR); it
*reframes and sharpens* MID-core but does NOT close it — GAP-EXTR is itself the open crux. The
integrality shortcut (`D∈ℤ_{>0}`) is refuted (non-integer vertices exist at n=3, all with `D>1`) and
the constant-value shortcut is refuted (`D` varies across words; Case (a) gives `D=2^{n-1}`).
