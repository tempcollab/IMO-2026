from fractions import Fraction as F
def alt_sum(m):
    s=F(0)
    for i,x in enumerate(sorted(m,reverse=True)):
        s += (x if i%2==0 else -x)
    return s
def Dn(n): return 2**(n+1)-1
print("== U1 balanced-pairs (corrected) ==")
for n in range(1,7):
    cfg=[]
    # pairs of 2^{k-1} for k=1..n means pairs of 1, 2, ..., 2^{n-1}
    for k in range(1,n+1):
        v=F(2)**(k-1)
        cfg += [v,v]
    cfg += [F(1)]  # unsplit bottom
    D=alt_sum(cfg); total=sum(cfg)
    print(f"n={n}: total={total}==D_n={Dn(n)}: {total==Dn(n)}, D={D}==1: {D==1}")
