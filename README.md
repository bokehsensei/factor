# Description
Factor is an integer factorization algorithm I wrote for the fun of it.
This may very well be a re-invention of a well-known algorithm,
but I could not find something quite so similar.

In a way, the closest algorithm is the [Fermat's factorization method](http://en.wikipedia.org/wiki/Fermat%27s_factorization_method).

Factor splits a number N into 2 factors, if it is a composite, or (1, N) if it is prime.
Time: its worst case is O(2^n) for a prime number with n bits.
Space: O(1)

all_factors returns the distribution of prime factors in N, by apply factor 'recursively' with a stack.

# Usage:

```python
from factor import factor, all_factors

from random import getrandbits

N = getrandbits(60)

factor(N) => (894764513, 983607138)

all_factors( 3*17*17*257*257*257*13)   => { 3:1, 17:2, 257:3, 13:1 }
```



