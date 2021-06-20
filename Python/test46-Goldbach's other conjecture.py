""" 
  It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

*       9  = 7  + 2 × 1²
*       15 = 7  + 2 × 2²
*       21 = 3  + 2 × 3²
*       25 = 7  + 2 × 3²
*       27 = 19 + 2 × 2²
*       33 = 31 + 2 × 1²

  It turns out that the conjecture was false.

? What is the smallest odd composite that cannot be written as the sum of a prime and twice a square
"""

from typing import Generator
from my_math import is_prime


def twice_square() -> Generator[int, None, None]:
    """
    Generates twice of square numbers
        ! infinite generator

    Yields:
    ----
        Generator[int, None, None]:
    """
    
    n: int = 1
    
    while True:
        yield 2*(n ** 2)
        n += 1
        

def odd_composite() -> Generator[int, None, None]:
    """
    Generates odd composite numbers
        ! infinite generator

    Yields:
    ----
        Generator[int, None, None]: composite numbers
    """

    n: int = 9  # first odd composite
    
    while True:
        if not is_prime(n):
            yield n
            
        n += 2
        

def smallest_odd_composite() -> int:
    """ returns smallest odd composite that cannot be written as the sum of a prime and twice a square

    Returns:
    ----
        int:
    """
        
    for com in odd_composite():
        for sub in twice_square():
            if sub >= com - 1:          # no matching primes found
                return com
            
            if is_prime(com - sub):     # matching prime found by reducing by twice square
                break
    

if __name__ == '__main__':
    print(smallest_odd_composite())