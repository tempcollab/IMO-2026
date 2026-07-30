from fractions import Fraction as F
import itertools, math

# Claim game value (greedy = odd-index sum of sorted-desc pieces)
def claim_value(pieces):
    s=sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def D_value(pieces):  # = 2*value - total  (parity integral)
    return 2*claim_value(pieces)-sum(pieces)

# Liu tower T_n normalized: pieces {1,2,...,2^n}/D_n  (unnormalized integers, total D_n=2^{n+1}-1)
def tower(n):
    return [2**k for k in range(0,n+1)]

# Xiang refinement: given Liu's pieces (as sizes), Xiang places <=n marks splitting pieces.
# A refinement = for each Liu piece, a partition of it into positive parts. total marks = sum(len(part)-1) <= n.
# Brute force over a discrete grid of cut positions.

def xiang_best_discrete(liu_pieces, n, grid=64):
    """Xiang minimizes Liu's claim value; returns min value (as Fraction) over grid refinements."""
    # represent cuts as fractions of each piece from a grid
    # For tractability, limit: try all ways to distribute k marks (0..n) across pieces, grid cuts.
    # Enumerate by: choose a multiset of cut fractions on the size axis per piece.
    # Simpler: generate all refinements by recursively splitting pieces, using grid points, total marks<=n.
    best=[None]  # min claim value
    # We'll do: for each piece, list of possible sub-partitions using grid points, with a count of marks.
    # then combine with total marks <= n.  Too expensive for many pieces; do recursive DP with remaining marks.
    gridpts=[F(i,grid) for i in range(1,grid)]
    # precompute per-piece partition options (list of (parts, marks_used)) for each piece size
    def piece_options(size, maxmarks):
        # all ways to split 'size' into >=1 positive parts using <=maxmarks cuts on grid
        # generate partitions by cut positions subset
        opts=[([size],0)]
        # choose k cuts 1..maxmarks
        for k in range(1,maxmarks+1):
            for cuts in itertools.combinations(gridpts,k):
                pts=sorted(cuts)
                parts=[]
                prev=0
                ok=True
                for c in pts:
                    parts.append(size*(c-prev)); prev=c
                parts.append(size*(1-prev))
                if all(p>0 for p in parts):
                    opts.append((parts,k))
        return opts
    # recursive combine
    pieces=liu_pieces
    npieces=len(pieces)
    # we want min claim_value over combined parts with sum marks<=n
    # DFS
    import sys
    sys.setrecursionlimit(10000)
    def dfs(idx, marks_left, acc_parts):
        if idx==npieces:
            val=claim_value(acc_parts)
            if best[0] is None or val<best[0]:
                best[0]=val
            return
        for parts,m in piece_options(pieces[idx], min(marks_left, n)):
            if m<=marks_left:
                dfs(idx+1, marks_left-m, acc_parts+parts)
    dfs(0,n,[])
    return best[0]

# Test n=1: Liu tower T_1 = {1,2} (total 3). Xiang 1 mark.
print("n=1 tower unnormalized", tower(1), "value=", claim_value(tower(1)), "target v_1=", F(2,3), "unnormalized 2")
v=xiang_best_discrete(tower(1),1,grid=64)
print("  xiang best (grid64):", v, "fraction of total:", v/F(3))

# n=2 tower {1,2,4} total 7
print("\nn=2 tower", tower(2), "value=", claim_value(tower(2)), "target unnormalized 4")
v=xiang_best_discrete(tower(2),2,grid=50)
print("  xiang best (grid50):", v, "fraction:", v/F(7))
