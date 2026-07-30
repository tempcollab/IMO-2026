from fractions import Fraction as Fr
from probe_star import ladder, partitions_of, Dtilde_from_merge

for n in range(1,7):
    L=ladder(n); tot=2**n
    tie_configs=[]
    for pi in partitions_of(tot, n+1):
        D,bo,re=Dtilde_from_merge(pi,L)
        if D==1: tie_configs.append(pi)
    print(f"n={n}: {len(tie_configs)} ties:")
    for pi in tie_configs: print("   ", pi)
