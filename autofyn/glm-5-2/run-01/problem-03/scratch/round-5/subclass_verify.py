"""Verify the CORRECTED narrow interleaved sub-class (single adjacent 2-piece
interleaving at EVEN k, rest clean) under the corrected LP-2 convention.
The cert: y_eq[t*]=0, y_eq=s_t on clean bins, mountain = single bump m_k=1.
Check feasibility (inequality star) + objective >= 1 + scipy strong duality.
"""
import numpy as np
from scipy.optimize import linprog

def solve(n, b, tower_vals):
    m=len(b); c=np.array([(-1.)**k for k in range(m)])
    bins=sorted(set(b)); A_eq=np.zeros((len(bins),m)); b_eq=np.zeros(len(bins))
    for i,t in enumerate(bins):
        for k in range(m):
            if b[k]==t: A_eq[i,k]=1.0
        b_eq[i]=float(tower_vals[t])
    A_ub=np.zeros((m-1,m))
    for k in range(m-1): A_ub[k,k]=-1.0; A_ub[k,k+1]=1.0
    res=linprog(c,A_ub=A_ub,b_ub=np.zeros(m-1),A_eq=A_eq,b_eq=b_eq,
                bounds=[(0,None)]*m,method='highs')
    return res,c,A_eq,b_eq

def check_cert_ineq(b, y_eq_cert, tower_vals):
    """Check corrected inequality (star): exists nonneg m (m_{-1}=m_{m-1}=0) with
    m_j - m_{j-1} <= d_j = (-1)^j - y_eq[b(j)].  Feasibility LP."""
    m=len(b); d=np.array([(-1.)**k - y_eq_cert[b[k]] for k in range(m)])
    nvar=m-1  # m_0..m_{m-2}
    A=np.zeros((m,nvar)); rhs=np.zeros(m)
    for j in range(m):
        if j==0: A[j,0]=1.0; rhs[j]=d[0]
        elif j<m-1: A[j,j]=1.0; A[j,j-1]=-1.0; rhs[j]=d[j]
        else: A[j,m-2]=-1.0; rhs[j]=d[m-1]
    feas=linprog(np.zeros(nvar),A_ub=A,b_ub=rhs,bounds=[(0,None)]*nvar,method='highs')
    obj=float(sum(y_eq_cert[t]*tower_vals[t] for t in y_eq_cert))
    return feas.success, obj, d, feas.x

# --- Even-k single adjacent interleaving (the CORRECTED sub-class) ---
# T_2: bin0(pos0,+,clean val4), bin1(pos1,-,clean val2), bin2(pos2,3 interleaved val1)
n=2; TV={0:4,1:2,2:1}
b=(0,1,2,2)  # k=2 EVEN interleaving for bin2
res,c,A_eq,b_eq=solve(n,b,TV)
print(f"Even-k (k=2) b={b}: primal min D = {res.fun}, p={np.round(res.x,4)}")
cert={0:1.0,1:-1.0,2:0.0}  # y_eq[t*]=0
ok,obj,d,mm=check_cert_ineq(b,cert,TV)
print(f"  cert y_eq=(1,-1,0): feasible={ok}, obj={obj}, d={d}, m={mm}")

# Another even-k: T_3, bin at positions 2,3 (k=2 even)
n=3; TV3={0:8,1:4,2:2,3:1}
# bin0(pos0,+),bin1(pos1,-),bin2(pos2,3 interl val2),bin3(pos4,+,clean val1)
b=(0,1,2,2,3)
res,c,A_eq,b_eq=solve(n,b,TV3)
print(f"\nEven-k (k=2) T_3 b={b}: primal min D = {res.fun}, p={np.round(res.x,4)}")
cert={0:1.0,1:-1.0,2:0.0,3:1.0}  # bin3 clean at + (pos4 even +)
# wait pos4 = +1 sign, so s_3 = +1
ok,obj,d,mm=check_cert_ineq(b,cert,TV3)
print(f"  cert y_eq=(1,-1,0,+1): feasible={ok}, obj={obj}, d={d}, m={mm}")

# Odd-k interleaving (should be INFEASIBLE with the bump=1 cert; needs different mountain)
# T_2: bin0(pos0,+),bin1(pos1,2 interleaved?? no. Let's do bin2 at positions 1,2 (k=1 odd)
# Actually adjacent (k,k+1) with k=1: positions 1,2. (-1)^1=-1, (-1)^2=+1.
# bin0(pos0,+),bin2(pos1,2 interl val1),bin1(pos3,-,val2). b=(0,2,2,1), m=4
b=(0,2,2,1); res,c,A_eq,b_eq=solve(n,TV and 2,TV) if False else solve(2,b,TV)
print(f"\nOdd-k (k=1) b={b}: primal min D = {res.fun}, p={np.round(res.x,4)}")
cert={0:1.0,1:-1.0,2:0.0}
ok,obj,d,mm=check_cert_ineq(b,cert,TV)
print(f"  cert y_eq=(1,-1,0): feasible={ok}, obj={obj}, d={d}")
# the bump should fail; check if ANY cert with obj>=1 is feasible (scipy dual)
print(f"  scipy dual y_eq={np.round(res.eqlin.marginals,4)} y_ub={np.round(res.ineqlin.marginals,4)} obj={float(b_eq@res.eqlin.marginals)}")

# --- The original round-4 infeasible T_2 demo, re-verified under CORRECTED convention ---
print("\n=== Round-4 demo (bin2 at positions 3,4) under corrected convention ===")
n=2; b=(0,1,0,2,2)  # bin0 at {0,2} clean +, bin1 at {1} clean -, bin2 at {3,4} interleaved
res,c,A_eq,b_eq=solve(n,b,TV)
print(f"b={b}: primal min D = {res.fun}, p={np.round(res.x,4)}")
# uniform cert
cert={0:1.0,1:-1.0,2:-1.0}
ok,obj,d,mm=check_cert_ineq(b,cert,TV)
print(f"  uniform y_eq=(1,-1,-1): feasible={ok}, obj={obj}, d={d}, m={mm}")
print(f"  scipy dual y_eq={np.round(res.eqlin.marginals,4)} obj={float(b_eq@res.eqlin.marginals)}")
