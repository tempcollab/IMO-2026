"""
Final probes on the XOR framing:
 1. When R = T_{n-1} (unsplit), is C bounded by a clean dyadic expression in F?
 2. Recursive telescoping: D = 1 + sum_k (D_{F_k} - 2 C_k); is each partial sum >= 0?
 3. Is C always <= D_R (trivial) and is there a sharper decoupled bound C <= f(D_R) only?
 4. Check: for R a tower refinement, is the R-odd region always a union of dyadic intervals?
"""
from fractions import Fraction as F
import random
random.seed(11)

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**k)*v for k,v in enumerate(s))
def D_integral(pieces):
    s = sorted(set([F(0)]+[p for p in pieces]), reverse=False)
    t=F(0)
    for i in range(len(s)-1):
        lo,hi=s[i],s[i+1]; mid=(lo+hi)/2
        N=sum(1 for p in pieces if p>=mid)
        if N%2==1: t+=(hi-lo)
    return t
def odd_region(pieces):
    """Return list of (lo,hi) intervals where N(t) is odd."""
    s=sorted(set([F(0)]+[p for p in pieces]),reverse=False)
    regs=[]
    for i in range(len(s)-1):
        lo,hi=s[i],s[i+1]; mid=(lo+hi)/2
        N=sum(1 for p in pieces if p>=mid)
        if N%2==1: regs.append((lo,hi))
    return regs
def overlap_C(Fp,Rp):
    return sum((hi-lo) for lo,hi in odd_region(Fp+Rp) if False) or _ovl(Fp,Rp)
def _ovl(Fp,Rp):
    allvals=sorted(set([F(0)]+list(Fp)+list(Rp)),reverse=False)
    t=F(0)
    for i in range(len(allvals)-1):
        lo,hi=allvals[i],allvals[i+1]; mid=(lo+hi)/2
        NF=sum(1 for p in Fp if p>=mid); NR=sum(1 for p in Rp if p>=mid)
        if NF%2==1 and NR%2==1: t+=(hi-lo)
    return t
def tower(n): return [F(2**k) for k in range(n,-1,-1)]

# 4. Is the R-odd region (R = tower refinement) always dyadic intervals?
print("R-odd region for R = T_{n-1} unsplit (should be dyadic intervals):")
for n in [3,4]:
    Rp = tower(n-1)
    regs = odd_region(Rp)
    print(f"  T_{n-1} odd region: {[(str(lo),str(hi)) for lo,hi in regs]}")

# 1. R = T_{n-1} unsplit: characterize C as function of F.
#    F-odd region intervals; overlap with R-odd dyadic intervals.
print("\nR=T_{n-1} unsplit: C vs D_F, and the bound D_F + D_R - 2C >= 1 (= D>=1):")
for n in [3,4,5]:
    top=F(2**n); Rp=tower(n-1); DR=D_integral(Rp)
    # enumerate breakpoint splits of top
    # quick: random + dyadic
    worst_slack=None
    for trial in range(3000):
        nf=random.randint(1,n)
        Fp=[top]
        for _ in range(nf):
            V=max(Fp); idx=Fp.index(V)
            f=V*F(random.randint(1,7),8)
            if f<=0 or f>=V: continue
            Fp=Fp[:idx]+[f,V-f]+Fp[idx+1:]
        DF=D_integral(Fp); C=_ovl(Fp,Rp); Dg=D_of(Fp+Rp)
        slack = (DF+DR-2*C) - 1  # = D - 1
        if worst_slack is None or slack < worst_slack:
            worst_slack = slack
    print(f"  T_{n}: min(D-1) = {worst_slack} (D_R={DR})")

# 3. Decoupled bound: is C <= g(D_R) for some function g independent of F?
#    Trivially C <= D_R. Is C <= D_R - 1/2? or C <= (D_R)/2 + something?
print("\nDecoupled bound C <= f(D_R): max C for fixed D_R (R=tower ref, F arbitrary split):")
for n in [3,4]:
    top=F(2**n)
    data={}
    for trial in range(8000):
        ntop=random.randint(1,n); nbelow=random.randint(0,n-ntop)
        Fp=list(tower(0)); Fp=[top]
        for _ in range(ntop):
            V=max(Fp); idx=Fp.index(V); f=V*F(random.randint(1,7),8)
            if f<=0 or f>=V: continue
            Fp=Fp[:idx]+[f,V-f]+Fp[idx+1:]
        # R as tower refinement
        Rp=list(tower(n-1))
        for _ in range(nbelow):
            V=max(Rp); idx=Rp.index(V); f=V*F(random.randint(1,7),8)
            if f<=0 or f>=V: continue
            Rp=Rp[:idx]+[f,V-f]+Rp[idx+1:]
        DR=D_integral(Rp); C=_ovl(Fp,Rp); DF=D_integral(Fp)
        key=str(DR)
        if key not in data or C>data[key][0]: data[key]=(C,DF)
    print(f"  T_{n}: max C per D_R value (sample): ", end="")
    for k in sorted(data, key=lambda x: F(x))[:6]:
        print(f"D_R={k}->maxC={data[k][0]},DF={data[k][1]}; ", end="")
    print()

# 2. Recursive telescoping sanity: D = 1 + sum of (D_Fk - 2 C_k)?
#    For the unsplit tower (no marks): D = D(T_n). Recursion D(T_n) = 2^n - D(T_{n-1}).
#    XOR with F={2^n} (unsplit top): D_F=2^n, C = D_R (full overlap). D = 2^n + D_R - 2 D_R = 2^n - D_R. ✓
print("\nSanity: F={2^n} unsplit: D_F=2^n, C should = D_R, D = 2^n - D_R = D(T_n)?")
for n in [3,4,5]:
    top=F(2**n); Rp=tower(n-1); DR=D_integral(Rp)
    Fp=[top]; DF=D_integral(Fp); C=_ovl(Fp,Rp)
    Dg=D_of(Fp+Rp)
    print(f"  T_{n}: D_F={DF}, C={C}, D_R={DR}, D={Dg}, D(T_n)={D_of(tower(n))}, C==D_R? {C==DR}")
