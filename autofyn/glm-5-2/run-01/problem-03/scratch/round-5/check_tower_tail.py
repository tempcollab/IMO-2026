from fractions import Fraction as F
from itertools import combinations_with_replacement, product

def D_of(pieces):
    s = F(0)
    for i,p in enumerate(pieces):
        if i % 2 == 0: s += p
        else: s -= p
    return s

# Liu config (14,8,4,2,1) in tower units, sum=29. Actual pieces = val/29.
# n=4, Xiang has 4 marks. Target D <= 1/31 (actual units) = 1/31.
# In tower units, D_tower = D_actual * 29. Target D_tower <= 29/31.
# D_tower = 1 (halving) -> D_actual = 1/29 > 1/31. VIOLATION if D*=1.

# Breakpoint-restricted search: at optimum, each Xiang split piece ties with another piece.
# So the final multiset (sorted desc) has every value with multiplicity >= 2, except
# possibly leftover Liu pieces.
# Equivalently: Xiang's 4 marks create 4 splits, each producing a tie.
# The final multiset is a REFINEMENT of (14,8,4,2,1) where every distinct value
# (except possibly the unsplit ones) appears >= 2 times... actually breakpoint means
# every piece in the final sort has a TIE (adjacent equal). So the final multiset
# has NO unique values (every value appears >= 2), OR the unique values are at the
# "end" (the odd-position leftovers).

# More precisely: at a breakpoint (tie) config, every piece is tied with its neighbor.
# So the multiset has even multiplicities for all values, except possibly the LAST one
# (if odd count). For 9 pieces (4 marks on 5): 9 is odd, so one value has odd mult.
# The 8 others pair up. D = (sum of + pairs) - (sum of - pairs) + [last piece if odd pos].

# Breakpoint = final multiset is a partition of 29 (tower units) into pieces where
# every value except possibly the smallest appears an even number of times.
# (The smallest can be alone at the end.)

# Enumerate: all multisets of pieces summing to 29, where each value has mult >= 2
# except possibly the minimum value (mult can be odd).
# And the multiset must be a REFINEMENT of (14,8,4,2,1): i.e., the pieces can be
# obtained by splitting the 5 original pieces.

# Actually, any partition of 29 into parts where we use <= 4 splits (5 -> up to 9 parts)
# and it's a refinement of (14,8,4,2,1). A refinement means we can group the parts
# back into {14, 8, 4, 2, 1}.

# Let me just enumerate all refinements of (14,8,4,2,1) using exactly 0..4 splits,
# restricted to breakpoint (tie) configs.

# A split of piece v into (q, v-q). Breakpoint: q equals some OTHER piece's value,
# or v-q equals some piece value, or q = v-q (balanced), or q/v is a ratio that
# creates a tie with adjacent in sorted order.

# Simpler: enumerate all partitions of 29 into <= 9 parts that refine (14,8,4,2,1)
# and are breakpoint configs (every part has a tie).

# Even simpler: just brute-force all 4-split refinements with rational breakpoints,
# using the piece values {14,8,4,2,1, and halves/sums thereof}.

# Let me use the approach: at a breakpoint, all pieces take values from the SET of
# all possible piece values obtainable. The possible "tie values" are:
# all subset-sums and fractions of {14,8,4,2,1}. At a breakpoint, each piece equals
# some other piece. So the distinct values in the final multiset each appear >= 2.

# Enumerate multisets: choose values from possible set, each with even multiplicity
# (except one), summing to 29, and check if it's a valid refinement.

# Possible piece values (must be achievable by splitting 14,8,4,2,1):
# Any value v such that v is a piece in some refinement. At breakpoints, v can be
# any rational that ties. The key constraint: the multiset refines (14,8,4,2,1).

# Let me just do full brute force but smart: split each of 14,8,4,2,1 at breakpoints
# (values that create ties). The tie values are: any existing piece value, any half,
# any sum/difference of piece values.

# Actually, the simplest correct approach: enumerate all ways to split the 5 pieces
# using 0-4 splits where each split point creates a tie. A split of v at q creates
# a tie if q equals some piece in the current multiset, or q = v/2 (self-tie), or
# v-q equals some piece.

# Let me just do unrestricted breakpoint search by trying all tie-creating splits.
from functools import lru_cache

def search(pieces_tuple, marks_left, best_so_far):
    pieces = sorted(pieces_tuple, reverse=True)
    d = D_of(pieces)
    if d < best_so_far[0]:
        best_so_far[0] = d
    if marks_left == 0 or best_so_far[0] == 0:
        return
    vals = set(pieces)
    n = len(pieces)
    for i in range(n):
        v = pieces[i]
        # tie-creating split points: q = v/2, or q = some other piece value,
        # or v - q = some piece value => q = v - w for w in vals
        candidates = set()
        candidates.add(F(1,2) * v)  # balanced
        for w in vals:
            if w < v:
                candidates.add(w)  # q = w, piece = w, v-w
                candidates.add(v - w)  # q = v-w, piece = v-w, w
        for q in candidates:
            if q <= 0 or q >= v:
                continue
            new = [q, v - q]
            rest = [pieces[j] for j in range(n) if j != i]
            merged = tuple(sorted(new + rest, reverse=True))
            search(merged, marks_left - 1, best_so_far)

# Test configs
target = F(1, 31)
for a1 in [16, 14, 13, 12, 10, 8]:
    cfg = (F(a1), F(8), F(4), F(2), F(1))
    S = sum(cfg)
    best = [F(10**9)]
    search(cfg, 4, best)
    d_star = best[0] / S  # actual units
    halving = F(1) / S
    print(f'a1={a1} S={S} D*={best[0]}/{S}={d_star} D(halv)={halving} target=1/31 D*<=target:{d_star<=target} D*=target:{d_star==target} VIOLATION:{d_star>target}')
