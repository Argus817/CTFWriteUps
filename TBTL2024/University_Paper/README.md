# University Paper - Crypto
## Hint
I had to write a scientific paper for one of my university courses describing my scientific role model. I wonder if my professors will be able to figure out who I'm describing...
#### Attachments: `description.txt` `chall.py`

## Solution
We are given a text file `description.txt` with the following contents
```
On the Estemeed Scientifc Role Model of Mine
============================================

Within the confines of this academic setting, the individual whom
I hold in highest regard not only boasts an engaging smile but also
possesses a remarkable sense of humor, complemented by an array of
vibrant notebooks.

Yet, it is their distinct quantifiable attribute that stands out
most prominently: their name, when converted into an integer value
and squared modulo 13113180816763040887576781992067364636289723584543479342139964290889855987378109190372819034517913477911738026253141916115785049387269347257060732629562571,
astonishingly results in 11295696938311339473824077083449119515455766620804723271417795055153345707595152245303924808555919718654126902417279389829240793581636850443514989727075129.

Furthermore, the greatest integer that does not surpass the cube root
of the aforementioned squared name equals 25255532621039290870985214051278041571596463385115156541846401100873975663406085683775323107488.
This computational detail adds another layer of distinction.

It is likely that by this point, many of you have discerned the identity
of this distinguished role model.
```

We are also given a file `chall.py` which was used to generate `description.txt`

`chall.py` has the following contents
```python3
from Crypto.Util.number import *
from redacted import FLAG

ESSAY_TEMPLATE = """
On the Estemeed Scientifc Role Model of Mine
============================================

Within the confines of this academic setting, the individual whom
I hold in highest regard not only boasts an engaging smile but also
possesses a remarkable sense of humor, complemented by an array of
vibrant notebooks.

Yet, it is their distinct quantifiable attribute that stands out
most prominently: their name, when converted into an integer value
and squared modulo %d,
astonishingly results in %d.

Furthermore, the greatest integer that does not surpass the cube root
of the aforementioned squared name equals %d.
This computational detail adds another layer of distinction.

It is likely that by this point, many of you have discerned the identity
of this distinguished role model.
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


N = 13113180816763040887576781992067364636289723584543479342139964290889855987378109190372819034517913477911738026253141916115785049387269347257060732629562571

name_int = bytes_to_long(FLAG)

assert 1 < name_int < N

value_1 = (name_int**2) % N
value_2 = invpow3(name_int**2)

assert (value_2**3) <= (name_int**2)
assert ((value_2 + 2) ** 3) > (name_int**2)

print(ESSAY_TEMPLATE % (N, value_1, value_2))
```
We have 
`N`, `value_1` and `value_2` from the above code.<br>
Let $v_1$ = `value_1`, ${v_2}$ = `value_2`, n = `N` and the integer representing flag to be $f$. Here `N` is composite so we cannot directly use Tonelli-Shanks algorithm to compute $f$ such that $f^2 \equiv {v_1} \mod n$.<br>

We know that $v_1 \equiv f^2\mod n$ and ${v_2} = \lfloor  (f^2)^{\frac{1}{3}} \rfloor$. 
We also know that<br>
${v_2} < f^{\frac{2}{3}} < y+1$ and hence <br>
${v_2}^{\frac{3}{2}} < f < ({v_2}+1)^{\frac{3}{2}}$<br>

Let $l = \lceil {v_2}^{\frac{3}{2}}\rceil$, we can be sure that $f = l+x$ where $ x < ({v_2}+1)^{\frac{3}{2}} - {v_2}^{\frac{3}{2}} \approx {\frac{3}{2}}{v_2}^{\frac{1}{2}} < {\frac{3}{2}}{n}^{\frac{1}{3}}$. 
Since we know that in mod $n$,
${v_1} \equiv f^2 \equiv (l+x)^2$, we can use Coppersmith's method on the polynomial $g(x) = (x+l)^2 - {v_1}$ to find the value of $x_0$ such that $g(x_0) \equiv 0 \mod n, \ {x_0} < {\frac{3}{2}}{n}^{\frac{1}{3}}$, and hence the value of $f$. <br>

Complete solution is given in [`solve.py`](./solve.py). Coppersmith's method is implemented using SageMath's `small_roots` ([link](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_modn_dense_ntl.html#sage.rings.polynomial.polynomial_modn_dense_ntl.small_roots)) function.
