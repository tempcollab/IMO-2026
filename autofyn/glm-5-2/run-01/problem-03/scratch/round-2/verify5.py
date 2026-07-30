from fractions import Fraction as F

def alt_sum(m):
    s=F(0)
    for i,x in enumerate(sorted(m,reverse=True)):
        s += (x if i%2==0 else -x)
    return s

def Dn(n): return 2**(n+1)-1

# U1: balanced-pairs config {2^{n-1},2^{n-1}, ..., 2,2,1,1,1} (tower units) -> D=1
print("== U1 parallel-halving -> D=1 (tower units) ==")
for n in range(1,7):
    cfg=[]
    for k in range(1,n+1):
        cfg += [F(2)**(k-1), F(2)**(k-1)]  # 2^{n-1},2^{n-1}, ..., 2,2 wait order
    cfg += [F(1), F(1), F(1)]
    # sorted descending
    D=alt_sum(cfg)
    total=sum(cfg)
    print(f"n={n}: cfg total={total}, D_n={Dn(n)}, D={D}, matches 1: {D==1}, total matches: {total==Dn(n)}")

# U2 arithmetic identity (2^n - 1)/D_{n-1} = 1
print("\n== U2 identity (2^n-1)/D_{n-1}=1 ==")
for n in range(2,8):
    Dn1=Dn(n-1)
    num=2**n - 1
    print(f"n={n}: 2^n-1={num}, D_{{n-1}}={Dn1}, ratio={F(num,Dn1)} ==1: {num==Dn1}")
