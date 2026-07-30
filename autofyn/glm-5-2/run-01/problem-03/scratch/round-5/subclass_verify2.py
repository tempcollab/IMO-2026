"""Check odd-k interleaving and the round-4 demo under corrected convention."""
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
    return res,A_eq,b_eq

def check_cert_ineq(b, y_eq_cert, tower_vals):
    m=len(b); d=np.array([(-1.)**k - y_eq_cert[b[k]] for k in range(m)])
    nvar=m-1
    A=np.zeros((m,nvar)); rhs=np.zeros(m)
    for j in range(m):
        if j==0: A[j,0]=1.0; rhs[j]=d[0]
        elif j<m-1: A[j,j]=1.0; A[j,j-1]=-1.0; rhs[j]=d[j]
        else: A[j,m-2]=-1.0; rhs[j]=d[m-1]
    feas=linprog(np.zeros(nvar),A_ub=A,b_ub=rhs,bounds=[(0,None)]*nvar,method='highs')
    obj=float(sum(y_eq_cert[t]*tower_vals[t] for t in y_eq_cert))
    return feas.success, obj, d, feas.x

TV={0:4,1:2,2:1}

# Odd-k interleaving: bin2 at positions 1,2 (k=1 odd). b=(0,2,2,1) m=4.
# bin0(pos0,+), bin2(pos1,2 interl), bin1(pos3,-)
b=(0,2,2,1)
res,A_eq,b_eq=solve(2,b,TV)
print(f"Odd-k (k=1) b={b}: primal min D = {res.fun}, p={np.round(res.x,4)}")
cert={0:1.0,1:-1.0,2:0.0}
ok,obj,d,mm=check_cert_ineq(b,cert,TV)
print(f"  cert y_eq=(1,-1,0): feasible={ok}, obj={obj}, d={d}")
print(f"  scipy dual y_eq={np.round(res.eqlin.marginals,4)} obj={float(b_eq@res.eqlin.marginals)}")

# Round-4 demo
print("\n=== Round-4 demo b=(0,1,0,2,2) ===")
b=(0,1,0,2,2)
res,A_eq,b_eq=solve(2,b,TV)
print(f"primal min D = {res.fun}, p={np.round(res.x,4)}")
cert={0:1.0,1:-1.0,2:-1.0}
ok,obj,d,mm=check_cert_ineq(b,cert,TV)
print(f"  uniform y_eq=(1,-1,-1): feasible={ok}, obj={obj}, d={d}, m={mm}")
print(f"  scipy dual y_eq={np.round(res.eqlin.marginals,4)} obj={float(b_eq@res.eqlin.marginals)}")

# Round-4's CLAIMED cert (y_eq=(1,-1,0)) -- should be infeasible under corrected conv
cert={0:1.0,1:-1.0,2:0.0}
ok,obj,d,mm=check_cert_ineq(b,cert,TV)
print(f"  round-4 claimed y_eq=(1,-1,0): feasible={ok}, obj={obj}, d={d}")
