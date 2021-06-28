""" 
    The prime 41, can be written as the sum of six consecutive primes:
*       41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

?   Which prime, below one-million, can be written as the sum of the most consecutive primes
"""

from my_math import is_prime, primesfrom2to
import numpy as np


def prime_sum_of_consecutive_primes(limit: int) -> int:
    """returns prime that can be written as the lonest sum of consecutive 
    primes below given limit

    Args:
    ----
        limit (int): upper limit of numbers

    Returns:
    ----
        int:
    """

    primes: np.ndarray[int] = primesfrom2to(limit)      # all primes under given limit
    prime_sum: tuple[int, int] = (0, 0)                 # holds max chain sum found and chain length

    for i in range(primes.size):    # chain starting possition
        prime_sums: np.ndarray[int] = np.add.accumulate(primes[i:])     # sum of previous primes ``similar to itertools.accumulate```
        prime_sums = prime_sums[prime_sums < limit]                     # filter primes smaller than limit

        if prime_sums.size < prime_sum[1]:  # current chain smaller than maximum prime chain found
            break
        
        for j in prime_sums[::-1]:  # check for prime from last to beginnig
            if j < prime_sum[0]:    # current sum smaller than maximum prime sum found
                break
            
            #                  chain length                           is larger than previous max
            if (is_prime(j) and 
                (l := np.nonzero(prime_sums == j)[0] + 1) > prime_sum[1]):
                
                prime_sum = (j, l)      # update new max
                break

    return prime_sum[0]     # max consecutive prime sum found


if __name__ == '__main__':
    print(prime_sum_of_consecutive_primes(1_000_000))
