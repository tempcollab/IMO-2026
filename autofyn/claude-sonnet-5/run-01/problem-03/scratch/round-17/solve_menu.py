import itertools, random
from fractions import Fraction as F

def L2(u,v):
    M,m = (u,v) if u>=v else (v,u)
    if M <= 2*m:
        return M
    else:
        return M/2+m

def V3(x,y,z):
    # sorted descending x>=y>=z
    s = x+y+z
    if x >= F(4,7)*s:
        return x/2 + L2(y,z)
    elif x >= s/2:
        return x
    else:
        return min(x+z/2, y+L2(x-y,z))

def c(k):
    # c(k) = 2^k/(2^{k+1}-1)
    return F(2**k, 2**(k+1)-1)

# full menu-based V4 (already known, from current.md)
def V4(A):
    p1,t1,t2,t3 = A
    stratA = t1 + V3(t2,t3,p1-t1) if p1>=t1 else None
    stratB = p1/2 + V3(t1,t2,t3)
    # StratC_ij: tie p1 to t_j via r=t_i-t_j, recurse on (p1,t_k,r) where k is remaining index
    def stratC(i,j,k):
        ti,tj,tk = A[i],A[j],A[k]
        r = ti - tj
        if r<0: return None
        trip = sorted([p1,tk,r], reverse=True)
        return tj + V3(*trip)
    sC12 = stratC(1,2,3)  # tie t1,t2 -> wait indices: A=[p1,t1,t2,t3], idx1=t1(idx1),idx2=t2(idx2)... let's just use direct formula from doc
    # Actually per doc:
    # StratC_12 = t2 + V3(p1,t3,r), r = t1-t2
    # StratC_13 = t3 + V3(p1,t2,r), r = t1-t3
    # StratC_23 = t3 + V3(p1,t1,r), r = t2-t3
    def sc(a,b,rest_idx):
        pass
    r12 = t1-t2
    C12 = t2 + V3(*sorted([p1,t3,r12],reverse=True)) if r12>=0 else None
    r13 = t1-t3
    C13 = t3 + V3(*sorted([p1,t2,r13],reverse=True)) if r13>=0 else None
    r23 = t2-t3
    C23 = t3 + V3(*sorted([p1,t1,r23],reverse=True)) if r23>=0 else None
    vals = [v for v in [stratA,stratB,C12,C13,C23] if v is not None]
    return min(vals)

if __name__=="__main__":
    import random
    random.seed(0)
    worst = None
    for _ in range(20000):
        vals = sorted([random.randint(1,1000) for _ in range(4)], reverse=True)
        A = [F(v) for v in vals]
        S = sum(A)
        if A[0] >= S/2:  # not Case C
            continue
        val = V4(A)
        target = c(3)*S
        margin = target - val
        ratio = margin/S
        if worst is None or ratio < worst[0]:
            worst = (ratio, A, val, target)
    print(worst)
