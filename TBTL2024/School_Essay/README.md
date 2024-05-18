# School Essay - Crypto
## Hint
I had to write an essay for school describing my favorite classmate. I wonder if my classmates will be able to figure out who I'm describing... 
#### Attachments: `description.txt` `chall.py`
## Solution
We are given a text file `description.txt` with the following contents
```
My Favorite Classmate
=====================

My favorite person in this class has a beautiful smile,
great sense of humour, and lots of colorful notebooks.

However, their most distinctive feature is the fact that
you can represent their name as an integer value, square
it modulo 59557942237937483757629838075432240015613811860811898821186897952866236010569299041278104165604573,
and you'll get 34994952631013563439857468985559745199379391295940238707110695903159545061311344766055629477728657.

Additionally, When you compute the greatest integer not exceeding
the cube root of their squared name, you get 7906488397402721714607879953738472269409876715324979164781592447.

By now, all of you have probably guessed who I'm talking about.
```

We are also given a file `chall.py` which was used to generate `description.txt`

`chall.py` has the following contents
```python3
from Crypto.Util.number import *
from redacted import FLAG

ESSAY_TEMPLATE = """
My Favorite Classmate
=====================

My favorite person in this class has a beautiful smile,
great sense of humour, and lots of colorful notebooks.

However, their most distinctive feature is the fact that
you can represent their name as an integer value, square
it modulo %d,
and you'll get %d.

Additionally, When you compute the greatest integer not exceeding
the cube root of their squared name, you get %d.

By now, all of you have probably guessed who I'm talking about.
"""


def invpow3(x):
    lo, hi = 1, x
    while lo < hi:
        mid = (lo + hi) // 2 + 1
        if (mid**3) <= x:
            lo = mid
        else:
            hi = mid - 1
    return lo


N = 59557942237937483757629838075432240015613811860811898821186897952866236010569299041278104165604573

name_int = bytes_to_long(FLAG)

assert 1 < name_int < N

value_1 = (name_int**2) % N
value_2 = invpow3(name_int**2)

print(ESSAY_TEMPLATE % (N, value_1, value_2))
```
We have 
`N`, `value_1` and `value_2` from the above code.<br>
Let $v_1$ = `value_1`, ${v_2}$ = `value_2`, n = `N` and the integer representing flag to be $f$. Here `N` is prime so we can use Tonelli-Shank's algorithm to compute $f$ such that $f^2 \equiv {v_1} \mod n$

Complete solution is given in [`solve.py`](./solve.py). Tonelli-Shank's algorithm is given in [`tonellishanks.py`](./tonellishanks.py) (credits to [ZeroBone](https://zerobone.net/blog/math/tonelli-shanks/)).