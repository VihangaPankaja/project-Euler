"""
    The number, 197, is called a circular prime because all rotations of the digits: 
*       197, 971, and 719, are themselves prime.
  
    There are thirteen such primes below 100: 
        2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

?   How many circular primes are there below one million
"""

from my_math import primesfrom2to
from typing import Generator


def rotations(num: int) -> Generator[int, None, None]:
    """ yields rotated numbers for given number

    Args:
    ----
        num (int): number

    Yields:
    ----
        Generator[int, None, None]: 
    """

    num: str = str(num)

    for i in range(len(num) - 1):
        yield int(num[-1-i:] + num[: -1-i])


def circular_primes_count(primes_under: int) -> int:
    """ returns how many circular primes under the given number ,
     made for only 10ⁿ (𝑛 ∈ ℤ) numbers as it only check for primes under given range

    Args:
    ----
        primes_under (int): numbers to check under

    Returns:
    ----
        int:
    """

    # 0 -> unchecked, 1 -> circular prime, -1 -> not a circular prime
    circular_primes: dict[int, int] = {
        x: 0 for x in primesfrom2to(primes_under)}
    original = circular_primes.copy()
    found: set[int] = set()

    def is_prime(n):
        try:    # try to find in dictionary
            if not circular_primes[n]:
                return True
            return False
        except KeyError:    # not in dictionary
            return False

    for prime in original:
        if circular_primes[prime]:  # previously checked
            continue

        rot = (prime, *rotations(prime))    # all rotations
        if all(map(is_prime, rot)):     # all rotations are prime
            for i in rot:
                circular_primes[i] = 1
                found.add(i)

        else:
            for i in rot:
                circular_primes[i] = -1

    return len(found)


if __name__ == "__main__":
    print(circular_primes_count(1_000_000))