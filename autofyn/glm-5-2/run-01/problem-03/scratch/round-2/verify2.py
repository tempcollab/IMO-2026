from fractions import Fraction as F

def alt_sum(m):
    s=F(0)
    for i,x in enumerate(sorted(m,reverse=True)):
        s += (x if i%2==0 else -x)
    return s

def tower(n):
    return [F(2**(n-k)) for k in range(n+1)]

# Single-split case (b-i): split top of T_n into p+q, p>=q. Check D>=D(T_{n-1})>=1
# and that min is at q=2^{n-1} (balanced), value D(T_{n-1})
print("== Single-split (b-i) brute force ==")
for n in [2,3,4]:
    T=tower(n)
    top=T[0]
    rest=T[1:]
    # scan q in (0, top/2] on fine dyadic-ish grid of fractions
    # use grid step 1/128 in tower units, q from small to top/2
    N=512
    mind=None; minq=None
    vals={}
    for i in range(1,N+1):
        q = F(i,N)*top  # q in (0, top]
        if q > top/2: 
            continue  # enforce p>=q i.e. q <= top/2
        p = top - q
        M=[p,q]+list(rest)
        D=alt_sum(M)
        vals[q]=D
        if mind is None or D<mind:
            mind=D; minq=q
    Dn1=alt_sum(tower(n-1))
    print(f"n={n}: top={top}, D(T_{{n-1}})={Dn1}, min D={mind} at q={minq} (float {float(minq)}), top/2={top/2}; min>=1: {mind>=1}, min==D(Tn-1): {mind==Dn1}")
    # check monotone non-increasing in q (samples)
    qs=sorted(vals.keys())
    noninc=True
    violations=0
    for i in range(1,len(qs)):
        if vals[qs[i]]>vals[qs[i-1]]:
            noninc=False; violations+=1
    print(f"   non-increasing in q on grid: {noninc} (violations: {violations})")
    # check slope is 0 or -2: sample consecutive
    print(f"   plateau top segment (q in (2^(n-2), 2^(n-1)]): val at q=2^(n-1)={vals.get(F(2**(n-1)))}, val near top of plateau q just below 2^(n-1): sample")
    if F(2**(n-1)) in vals:
        print(f"      D at balanced q=2^(n-1)={vals[F(2**(n-1))]}")
