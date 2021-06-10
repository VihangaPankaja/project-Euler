""" 
  The arithmetic sequence, 
*    1487, 4817, 8147, 
  in which each of the terms increases by 3330, is unusual in two ways: 
*    𝑖.  each of the three terms are prime
*    𝑖𝑖. each of the 4-digit numbers are permutations of one another.

  There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
  but there is one other 4-digit increasing sequence.

? What 12-digit number do you form by concatenating the three terms in this sequence
"""

from my_math import is_prime
from itertools import permutations

def arithmetic_seq() -> str:
    """ returns concatenated three terms in above arithmetic sequence """
    
    for i in range(1_000, 10_000 - 3330):
        if all([
            is_prime(i),
            tuple(str(i + 3330)) in permutations(str(i)),
            tuple(str(i + 2*3330)) in permutations(str(i)),
            is_prime(i + 3330),
            is_prime(i + 2*3330),
            i != 1487
        ]): return ''.join([str(i), str(i + 3330), str(i + 2*3330)])
        

if __name__ == '__main__':
    print(arithmetic_seq())
            