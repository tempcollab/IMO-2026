from fractions import Fraction as F
from itertools import product

# Tower units: T_n = (2^n, 2^{n-1}, ..., 2, 1), total D_n = 2^{n+1}-1
def tower(n):
    return [F(2**(n-k)) for k in range(n+1)]

def alt_sum(m):
    # m sorted descending
    s = F(0)
    for i,x in enumerate(m):
        s += (x if i%2==0 else -x)
    return s

def Dn(n): return 2**(n+1)-1

# 1. Frontier recursion & closed form
print("== Frontier recursion / closed form ==")
Dvals={}
for n in range(0,9):
    T=tower(n)
    D=alt_sum(T)
    Dvals[n]=D
    cf=(2**(n+1)+((-1)**n))//3
    print(f"n={n}: T={T} D={D} closed_form={(2**(n+1)+(-1)**n)}/{3}={F(2**(n+1)+(-1)**n,3)} >=1: {D>=1}")
# frontier
for n in range(1,9):
    print(f"n={n}: D(T_n)+D(T_{n-1})={Dvals[n]+Dvals[n-1]} == 2^n={2**n}: {Dvals[n]+Dvals[n-1]==2**n}")

# parity: (2^{n+1}+(-1)^n)/3 integer?
for n in range(0,9):
    v = 2**(n+1)+((-1)**n)
    print(f"n={n} parity: 2^(n+1)+(-1)^n = {v}, /3 = {F(v,3)} int={v%3==0}")
