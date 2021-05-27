# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

from itertools import permutations
from my_math import is_prime


def largest_pandigital_prime()-> int:
    for len_digits in range(9,0,-1):        # number of digits in pandigital number. starting from highest to reduce run time
        for digit in permutations(map(str, range(len_digits,0,-1))):        # generate permutation of given digits starting from highest to reduce run time
            if is_prime(int(''.join(digit))):       # convert digits to number and check for primality
                return int(''.join(digit))


if __name__ == '__main__':
    print(largest_pandigital_prime())