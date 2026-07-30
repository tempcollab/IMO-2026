import random, sys
sys.path.insert(0,'/tmp/round-6')
from rt_search import eval_f, u, c

random.seed(11)
print("Restrict to TRUE residual: ell1<Sigma/2 AND 2*ell2<c(k)*Sigma (case ii doesn't apply)")
for k in [2,3,4]:
    uk=u(k); ck=c(k); ukm1=u(k-1)
    m=k+1
    n_seen=0
    worst_ratio_true=0; worst_ratio_bound=0
    n_fail_true=0; n_fail_bound=0
    worst_true_ex=None; worst_bound_ex=None
    trials=3000
    for t in range(trials):
        xs = sorted([random.random() for _ in range(m-1)])
        parts=[]; prev=0
        for x in xs:
            parts.append(x-prev); prev=x
        parts.append(1-prev)
        parts.sort(reverse=True)
        ell1,ell2=parts[0],parts[1]
        if ell1>=0.5-1e-9: continue
        if 2*ell2 >= ck-1e-9: continue  # skip case ii
        n_seen+=1
        merged = abs(ell1-ell2)
        rest = [merged]+parts[2:]
        Sp = sum(rest)
        g_true = eval_f(rest, k-1)
        g_bound = ukm1*Sp
        rt = g_true/uk; rb = g_bound/uk
        if rt>worst_ratio_true: worst_ratio_true=rt; worst_true_ex=parts
        if rb>worst_ratio_bound: worst_ratio_bound=rb; worst_bound_ex=parts
        if g_true>uk+1e-9: n_fail_true+=1
        if g_bound>uk+1e-9: n_fail_bound+=1
    print(f"k={k}: residual instances seen={n_seen}/{trials}")
    print(f"   TRUE-optimal-recurse: fails={n_fail_true} worst ratio={worst_ratio_true:.4f} ex={worst_true_ex}")
    print(f"   IH-BOUND-recurse:     fails={n_fail_bound} worst ratio={worst_ratio_bound:.4f} ex={worst_bound_ex}")
