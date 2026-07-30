import itertools, random
from fractions import Fraction as F

# Verify identity 1/c(n) = 2 - 2^{-n}
for n in range(1,8):
    cn = F(2**n, 2**(n+1)-1)
    e = 1/cn
    g = 2 - e
    print(n, cn, e, g, g == F(1,2**n))
