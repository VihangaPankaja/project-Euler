""" 
  The prime 41, can be written as the sum of six consecutive primes:
*       41 = 2 + 3 + 5 + 7 + 11 + 13

  This is the longest sum of consecutive primes that adds to a prime below one-hundred.

  The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

? Which prime, below one-million, can be written as the sum of the most consecutive primes
"""

from my_math import prime_gen, is_prime


def prime_sum_of_consecutive_primes(limit: int) -> int:
    """ returns prime that can be written as the lonest sum of consecutive primes below given limit """

    prime_lst = []
    prime_sum = 0

    for prime in prime_gen():
        if prime_sum >= limit:
            break
        print(prime)
        prime_sum += prime
        prime_lst.append(prime)

    print(prime_lst)
    for prime in prime_lst[::-1]:
        if is_prime(prime_sum):
            return prime_sum

        prime_sum -= prime


if __name__ == '__main__':
    print(prime_sum_of_consecutive_primes(1_000_000))
