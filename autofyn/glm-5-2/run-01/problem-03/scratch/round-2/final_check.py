from fractions import Fraction

def D_exact(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i) * s[i] for i in range(len(s)))

# Final verification: the direct bound for n=2 cases C and B2.
# Case C (L >= 2*a_2, L < 4/7): halve L. rest = (a_2, a_3). D(rest) = a_2 - a_3.
#   a_2 - a_3 = a_2 - (1-L-a_2) = 2*a_2 + L - 1. With a_2 <= L/2: D <= 2L-1 < 1/7.
# Case B2 (L < 2*a_2, a_2 < 2/7): pair. rest' = (L-a_2, a_3). D(rest') = |L-a_2 - a_3| = |2L-1|.
#   Need |2L-1| < 1/7. For B2: L < 2*a_2 < 4/7, and L > 3/7 (from a_2 >= (1-L)/2, a_2 < 2/7).
#   So L in (3/7, 4/7): |2L-1| = 2L-1 (L>1/2) or 1-2L (L<1/2). Both < 1/7 when L in (3/7,4/7).
#   2L-1 < 1/7 iff L < 4/7 ✓. 1-2L < 1/7 iff L > 3/7 ✓.

# The KEY LEMMA candidate: "If L < 2^n/D_n, then after one well-chosen mark,
# D(total) <= D(rest) where rest is a config with total R and max piece <= L/2,
# AND D(rest) <= 2L-1 < 1/D_n (when rest has 2 pieces)."
# For n=2, rest always has 2 pieces. For n>=3, need generalization.

# Verify the "rest max <= L/2" claim:
# Case C: rest = {a_2, ...}, max = a_2 <= L/2 (from L >= 2*a_2). ✓
# Case B: rest' = {L-a_2, a_3, ...}, max = max(L-a_2, a_3). L-a_2 < a_2 (from L < 2*a_2).
#   a_3 <= a_2. So max(rest') <= a_2 <= L (trivially). But a_2 could be > L/2 in case B!
#   In B, L < 2*a_2 means a_2 > L/2. So rest' max = a_2 > L/2. NOT <= L/2.
#   But rest' max = a_2 < L (since a_2 <= L). And we need rest' to be "below threshold" in (n-1)-game.
#   (n-1)-game threshold = 2^{n-1}/D_{n-1}. rest' max = a_2. In B2: a_2 < 2^{n-1}/D_n < 2^{n-1}/D_{n-1}. ✓
#   In B1: a_2 >= 2^{n-1}/D_n, but B1 closes by induction. So B2 has rest' max < 2^{n-1}/D_{n-1}.

# Summary: the "below threshold" property propagates:
# n-game threshold = 2^n/D_n. If L < 2^n/D_n, after one mark, rest's max < 2^{n-1}/D_{n-1} = (n-1)-threshold.
# This is because:
#   Case C: rest max = a_2 <= L/2 < 2^{n-1}/D_n <= 2^{n-1}/D_{n-1} (since D_n > D_{n-1}).
#   Case B2: rest' max = a_2 < 2^{n-1}/D_n < 2^{n-1}/D_{n-1}.

# So "below threshold" is PRESERVED under one mark. After k marks, the rest is below the
# (n-k)-threshold. This means the config is ALWAYS in the "below threshold" regime at each level,
# never reaching the dominant case A — so the induction (which needs case A) never fires!

# This means the recursive strategy ALWAYS stays in cases B/C — it never hits the "easy" case A.
# That's why it fails: it never uses the induction, and the direct 2-piece bound only works at the bottom.

# The RESOLUTION: the induction should work DIFFERENTLY. Instead of "halve + induct on rest",
# it should be: "if above threshold (case A), halve + induct; if below threshold, the config
# is far from the tower and a SEPARATE argument (pairing/balancing) applies."

# The key open question: for n >= 3, what is the "separate argument" for below-threshold configs?
# The numerics show it's always possible (0 optimal fails), but the mechanism is unclear.

# Let me check: for below-threshold configs (L < 2^n/D_n), is the optimal D bounded by 1/D_n
# using a DIFFERENT kind of induction — e.g., on the NUMBER of pieces, not on n?

# Actually: below threshold means L < 2^n/D_n ≈ 1/2. So the config has no piece > ~1/2.
# This means the config has at least 3 pieces (for n >= 2). With m >= 3 pieces and n marks,
# Xiang can create pairs. The claim: with m pieces and n >= m-1 marks, Xiang can force D = 0
# (by pairing all pieces). When n < m-1, can't pair everything.

# For the tower (m = n+1 pieces, n marks): can't pair everything (n marks, n+1 pieces).
# But tower is ABOVE threshold (case A), handled by factorization.

# For below-threshold: the config has m pieces with m >= 2 (since L < 1/2 means m >= 3 for n >= 2).
# Actually for n=3: L < 8/15 ≈ 0.533. Could have 2 pieces (L=0.5, 1-L=0.5): L=0.5 < 0.533, 
# 2 pieces, 3 marks. Xiang can pair: split 0.5 into 0.25+0.25, then split other 0.5 into 0.25+0.25.
# Config: (0.25,0.25,0.25,0.25), D=0. Or split each into equal halves: 2 marks, D=0.
# So 2-piece below-threshold is trivially easy (pair both into equal halves, D=0).

print("=== Below-threshold analysis ===")
print("For n>=2, below-threshold (L < 2^n/D_n ~ 1/2) means:")
print("  - Config has >= 2 pieces, likely >= 3 for n>=3")
print("  - The tower (hardest config) is ABOVE threshold (case A)")
print("  - Below-threshold configs are 'far from tower' and easier")
print()
print("The complete upper-bound strategy:")
print("  Case A (L >= 2*a_2 AND L >= 2^n/D_n): HALVE L, induct on rest. [FACTORING - clean]")
print("  Case C (L >= 2*a_2, L < 2^n/D_n): below-threshold, parity-clean. [NEEDS ARGUMENT]")
print("  Case B (L < 2*a_2): below-threshold, non-dominant. PAIR L with a_2. [NEEDS ARGUMENT]")
print("  Sub-cases B1 (a_2 >= 2^{n-1}/D_n): induct. [clean]")
print("  Sub-cases B2 (a_2 < 2^{n-1}/D_n): below (n-1)-threshold. [NEEDS ARGUMENT]")
print()
print("Cases A and B1 close by induction. Cases C and B2 are 'below threshold' —")
print("the induction doesn't fire, but the config is far from the tower and easier.")
print("The mechanism for C/B2 at general n is the OPEN GAP of this route.")
print("DONE")
