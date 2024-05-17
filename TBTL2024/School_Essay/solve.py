from Crypto.Util.number import *
from tonellishanks import *

def invpow3(x):
    lo, hi = 1, x
    while lo < hi:
        mid = (lo + hi) // 2 + 1
        if (mid**3) <= x:
            lo = mid
        else:
            hi = mid - 1
    return lo


value_1 = 34994952631013563439857468985559745199379391295940238707110695903159545061311344766055629477728657
value_2 = 7906488397402721714607879953738472269409876715324979164781592447
N = 59557942237937483757629838075432240015613811860811898821186897952866236010569299041278104165604573

root1 = tonelli_shanks(value_1, N)
root2 = N-root1

if invpow3(root1**2)==value_2:
    root = root1
else:
    root = root2

print(long_to_bytes(root))
