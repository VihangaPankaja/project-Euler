""" 
  Let d(𝑛) be defined as the sum of proper divisors of 𝑛 (numbers less than 𝑛 which divide evenly into 𝑛)
  .
* If d(𝑎) = 𝑏 and d(𝑏) = 𝑎, where 𝑎 ≠ 𝑏, 
  then 𝑎 and 𝑏 are an amicable pair and each of 𝑎 and 𝑏 are called amicable numbers.
  
  For example, the proper divisors of 220 are 
  1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
  therefore d(220) = 284. 
  
  The proper divisors of 284 are,
  1, 2, 4, 71 and 142; 
  so d(284) = 220.

? Evaluate the sum of all the amicable numbers under 10000. 
"""

import numpy as np
from math import sqrt, ceil


def d(n: int) -> int:
    '''return sum divisors'''

    divisors: np.ndarray = np.zeros(ceil(n/2) + 2, dtype=bool)  # array of false
    divisors[1] = True

    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            divisors[i] = True          # factor
            divisors[n//i] = True       # factor

    return sum(np.nonzero(divisors)[0])


def amicable_list_under(num_check: np.ndarray, amicable_num: int) -> np.ndarray:
    """ returns amicable numbers under the given number """

    for i in range(1, amicable_num):
        if not num_check[i]:           # check if not unchecked
            
            if i == d(D:= d(i)) and i != D:          # ckeck for amicable number
                num_check[i] = True             # mark amikable
                num_check[D] = True          # mark amicable
        
    return np.nonzero(num_check)[0]


if __name__ == "__main__":
    amicable_num: int = 10_000
    # as a checkbox for every number
    num_check: np.ndarray = np.zeros(amicable_num, dtype=bool)

    print(sum(amicable_list_under(num_check, amicable_num)))