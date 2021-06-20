"""
  he following iterative sequence is defined for the set of positive integers:

*   𝑛 → 𝑛/2       (n is even)
*   𝑛 → 3𝑛 + 1    (𝑛 is odd)

  Using the rule above and starting with 13, we generate the following sequence:
*   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

  It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
  Although it has not been proved yet (Collatz Problem), 
  it is thought that all starting numbers finish at 1.

? Which starting number, under one million, produces the longest chain?

  NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import numpy as np


def T_next(n: int) -> int:
    return 3*n + 1 if n % 2 else n//2


def longest_chain(max_number: int) -> int:
    """ find the longest chain giving number under given number """

    nums: np.ndarray = np.ones(max_number, dtype=bool)
    chain_size: dict[int, int] = {}

    for i in range(1, max_number):

        if nums[i]:     # if wasn't check before
            def chain(n):
                """ return chain size of next number, update chain_size and update nums """
                
                try:                    # if in chain_size
                    return chain_size[n]

                except KeyError:
                    if n == 1:
                        chain_size[1] = 1
                        return 1
                    chain_size[n] = (k := 1 + chain(T_next(n)))     # add to chain_size
                    if n < max_number:
                        nums[n] = False     # set in nums
                    return k
            
            chain(i)

    return max(chain_size, key=lambda x: chain_size[x])     # return that has biggest chain


if __name__ == '__main__':
    global nums, chain_size
    print(longest_chain(1_000_000))
