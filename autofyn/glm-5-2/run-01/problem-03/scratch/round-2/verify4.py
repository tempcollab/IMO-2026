from fractions import Fraction as F
import math
from itertools import product

# Verify F-min: 1 <= D_n(e) <= 2^n - 1 for ALL parity vectors e in {0,1}^n
# Compute D_n(e) via F-block formula directly (which we verified matches direct)
# But e -> n_k mapping: n_k = 1 + 2*c_{k+1} - c_k where c_k = #splits at level k
# e_k = c_k mod 2. The block formula needs actual counts not just parities...
# Actually F-block: D = sum_k 2^k (-1)^{C_k} (n_k mod 2), n_k mod 2 = (1 + c_k) mod 2 = 1 - e_k (mod 2)
# Wait: n_k = 1 + 2 c_{k+1} - c_k, so n_k mod 2 = (1 - c_k) mod 2 = 1 - e_k (since c_k mod 2 = e_k)
# So n_k odd iff e_k = 0.
# C_k mod 2 = sum_{j>k} n_j mod 2 = sum_{j>k} (1 - e_j) mod 2 = (n-k - sum_{j>k} e_j) mod 2
# Let me compute D_n(e) from e directly.

def Dn_from_e(e):
    # e[0..n-1] correspond to e_1..e_n (e_0 fixed = 0, not in input)
    n=len(e)
    # levels 0..n. e_k for k=1..n is e[k-1]; e_0=0.
    ek=lambda k: 0 if k==0 else e[k-1]
    # n_k mod 2 = 1 - e_k (for k>=0, with e_0=0 -> n_0 odd iff e_0=0 -> odd). 
    nk_mod2 = [ (1 - ek(k)) % 2 for k in range(n+1) ]
    # C_k = sum_{j>k} n_j; we need C_k mod 2 = sum_{j>k} (1-e_j) mod 2
    Ck_mod2=[]
    for k in range(n+1):
        s = sum( (1-ek(j))%2 for j in range(k+1,n+1) )
        Ck_mod2.append(s%2)
    D=F(0)
    for k in range(n+1):
        if nk_mod2[k]==1:
            D += F(2)**k * ((-1)**Ck_mod2[k])
    return D

print("== F-min over all parity vectors ==")
for n in range(1,8):
    vals=[]
    for e in product([0,1],repeat=n):
        vals.append(Dn_from_e(e))
    print(f"n={n}: #parity vecs={2**n}, min={min(vals)}, max={max(vals)}, all in [1,2^n-1={2**n-1}]: {all(1<=v<=2**n-1 for v in vals)}, cascade e=all1 D={Dn_from_e([1]*n)}")
