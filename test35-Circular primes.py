# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

from my_math import prime_list_till

prime_range = 1_000_000
prime_lst = prime_list_till(prime_range)      # get primesinthat range
circular_primes = []                          # circukar primes pound


def number_rotations(n):
    digits = list(str(n))
    rotate = []

    for i in range(len(digits)):
        digits.append(digits.pop(0))            # rotate digits
        rotate.append(int(''.join(digits)))

    return rotate                               # return rotated digits


while True:
    elem = number_rotations(prime_lst[0])       # checck first in primes
    for i in elem:
        if i not in prime_lst:                  # if all of rotated numebrs aren't prime break
            break

    else:
        for j in elem:
            circular_primes.append(j)           # if all primes add to list
    

    for j in elem:
        try:
            prime_lst.remove(j)                 # remove all checked primes

        except:
            pass
    
    if prime_lst == []:                         # if primes are empty
        break

circular_primes = list(set(circular_primes))
print(circular_primes, len(circular_primes))

