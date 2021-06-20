""" 
  By replacing the 1st digit of the 2-digit number *3, 
  it turns out that six of the nine possible values: 
*        13, 23, 43, 53, 73, and 83, are all prime.

  By replacing the 3rd and 4th digits of 56**3 with the same digit, 
  this 5-digit number is the first example having seven primes among the ten generated numbers, 
  yielding the family: 
*        56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
        Consequently 56003, being the first member of this family, 
        is the smallest prime with this property.

? Find the smallest prime which, 
?    by replacing part of the number (not necessarily adjacent digits) with the same digit, 
?    is part of an eight prime value family.
"""
# ! run time about 40s

from my_math import primesfrom2to
from array import array
from itertools import combinations, chain
from typing import Generator


def primality_for_given_digt_numbers(digits: int) -> dict[int, bool]:
    """dictionary of primality for given digit numbers

    Args:
    ----
        digits (int): what digit numbers are checking

    Returns:
    ----
        dict[int:bool]: True if prime in dictionary

    eg:-
    >>> primality_for_given_digt_numbers(1)
    ... {0:False, 1:False, 2:True,...
    """

    is_prime: dict[int, bool] = {i: False for i in range(
        10**(digits - 1), 10**digits)}   # initialize dictionary in number range

    for i in primesfrom2to(10**digits):
        if i < 10**(digits - 1):    # not on considering digit range
            continue

        is_prime[i] = True  # mark primes

    return is_prime


def is_prime_family(members_in_family: int, template: array, 
                    is_prime: dict[int, bool]) -> bool:
    """return true if given number of primes for given template.
    update min prime if found

    Args:
    ----
        members_in_family (int): how many primes
        template (array[str]): number with replacable possitions

    Returns:
    ----
        bool:
    """
    global min_prime
    primes = 0
    smll_in = None

    for i in '0123456789':
        if template[0] == '*' and i == '0':     # 0 is not applied in first digit
            continue

        if is_prime[int(k := template.tounicode().replace('*', i))]:    # check for replaced values
            primes += 1

            if smll_in is None:     # for first prime found
                smll_in = int(k)
            
    if primes == members_in_family:     # if all primes found equals to members cound requires
        if min_prime is None or min_prime > smll_in:
            min_prime = smll_in
        return True
    return False


def template(replacement: tuple[int], digits: int) -> Generator[array, None, None]:
    """generates number template that witha replacable possitions for given replacement  possitions

    Args:
    ----
        replacement (tuple[int]): number possitions that are fixed
        digits (int): length of number

    Yields:
    ----
        array[str]: number templte with replacable possitions
    """
    
    l: int = len(replacement)
    for num in range(10**(l) if not replacement[0] else 0, 
                     10**(l + 1)):    # if first value replcing start with 10ˡ
        tem: array[str] = array('u', "*" * digits)
        num: str = str(num).rjust(l, '0')

        for index, i in enumerate(replacement):     # replce parts with numbers to generate template
            tem[i] = num[index]

        yield tem
    return


def smallest_prime_family(members_in_family: int) -> int:
    """Find the smallest prime which, 
    by replacing part of the number (not necessarily adjacent digits) with the same digit, 
    is part of an eight prime value family.

    Args:
    ----
        members_in_family (int): members in family

    Returns:
    ----
        int: smallest prime that has given number of family members
    """
    cur_digits: int = 2
    check: bool = True

    while check:    # untill find check only for n digit numbers 
        is_prime: dict[int, bool] = primality_for_given_digt_numbers(
            cur_digits)

        for replcement in chain(*(combinations(range(cur_digits), i) 
                                  for i in range(1, cur_digits))):   
            # all possibilities of getting 𝑖 items from 𝑛 items where 𝑖 is 1 to 𝑛-1

            for tem in template(replcement, cur_digits):
                if (is_prime_family(members_in_family, tem, is_prime)):
                    check = False

        cur_digits += 1

    return min_prime


if __name__ == "__main__":
    min_prime = None
    print(smallest_prime_family(8))
