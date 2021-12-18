""" 
    Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
            37 36 35 34 33 32 31
            38 17 16 15 14 13 30
            39 18  5  4  3 12 29
            40 19  6  1  2 11 28
            41 20  7  8  9 10 27
            42 21 22 23 24 25 26
            43 44 45 46 47 48 49

    It is interesting to note that the odd squares lie along the bottom right diagonal, 
    but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
    that is, a ratio of 8/13 ≈ 62%.

    If one complete new layer is wrapped around the spiral above, 
    a square spiral with side length 9 will be formed. If this process is continued, 
?   what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%
"""

from typing import Generator
from my_math import is_prime


def diagonals_of_square_spiral() -> Generator[tuple[int], None, None]:
    """ yields 4 corner point values of each new layer(n) as a tuple """

    n = 2
    
    while True:
        yield (2*n - 1)**2, (2*n - 1)**2 - 2*(n-1), (2*n - 1)**2 - 4*(n-1), (2*n - 1)**2 - 6*(n-1)
        n += 1
    
    
def main() -> int:
    all_nums = 1
    primes = 0
    
    for n, diagonals in enumerate(diagonals_of_square_spiral(), 2):
        all_nums += 4
        
        for i in diagonals:     # count number of primes
            if is_prime(i):
                primes += 1
        
        if 10 * primes < all_nums:  # < 10%
            print(2*n - 1)          # side length
            break

if __name__ == "__main__":
    main()