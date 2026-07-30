from fractions import Fraction as F
# Construct explicit regime-C1 config and check the inequality chain.
# Regime C1: a_1 >= 2a_2, a_1 < 4/7, a_2 >= 2a_3, sum=1.
# Try a_1 = 0.55 = 11/20, a_2 = 0.25 = 1/4, a_3 = 0.2 = 1/5. Check: 0.55>=0.5 yes, 0.55<4/7≈0.571 yes, 0.25>=0.4? NO (0.25<0.4). Not C1.
# Try a_1=0.5, a_2=0.2, a_3=0.3? a_3>a_2 no. 
# Need a_1<4/7≈0.571, a_1>=2a_2 so a_2<=0.2855, a_2>=2a_3 so a_3<=0.1427, sum a_1+a_2+a_3=1.
# a_1+a_2+a_3 >= a_1 (min a_2,a_3 small). Try a_1=0.56=14/25, a_2=0.22=11/50, a_3=0.22? no a_3<=a_2/2=0.11. a_1=0.56,a_2=0.34>a_1/2=0.28 no.
# Let me parametrize: a_2 = t, a_3 = t/2 (max), a_1 = 1 - 3t/2. Need a_1>=2a_2=2t: 1-3t/2>=2t => 1>=7t/2 => t<=2/7≈0.2857. And a_1<4/7: 1-3t/2<4/7 => 3t/2>3/7 => t>2/7. CONTRADICTION (t<=2/7 and t>2/7).
# So at the boundary t=2/7: a_1=1-3/7=4/7 (not <4/7). So regime C1 with a_2>=2a_3 (a_3=a_2/2 max) is EMPTY near the boundary?? Let me check: if a_3 <= a_2/2, then a_1+a_2+a_3 <= a_1 + a_2 + a_2/2 = a_1+3a_2/2. For sum=1: 1<=a_1+3a_2/2. With a_2<=a_1/2: 1<=a_1+3a_1/4=7a_1/4 => a_1>=4/7. So regime C1 (a_1<4/7 AND a_2>=2a_3) is EMPTY!
# That means C1 never occurs in regime C. Let me verify.
print("Checking if regime C1 (a_1>=2a_2, a_1<4/7, a_2>=2a_3) is empty:")
# a_1<4/7, a_2<=a_1/2<2/7, a_3<=a_2/2<a_1/4. sum=a_1+a_2+a_3 < a_1 + a_1/2 + a_1/4 = 7a_1/4. sum=1 => 1<7a_1/4 => a_1>4/7. Contradicts a_1<4/7.
print("a_1<4/7, a_2<=a_1/2, a_3<=a_2/2 => a_1+a_2+a_3 <= 7a_1/4 < 7*(4/7)/4 = 1. So sum<1, contradiction. C1 EMPTY in regime C.")
print("So C1 is vacuous; the buggy inequality never applies. C2 (a_2<2a_3) is the only sub-case of regime C.")
# Confirm: in regime C, must have a_2<2a_3 (C2), else sum<1.
# C2 bound: D(rest) <= a_3/2, a_3 <= a_2 <= a_1/2 < 2/7 => a_3/2<1/7. Fine.
