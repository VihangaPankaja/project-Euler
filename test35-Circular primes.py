"""
  The number, 197, is called a circular prime because all rotations of the digits: 
*   197, 971, and 719, are themselves prime.
  
  There are thirteen such primes below 100: 
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

? How many circular primes are there below one million
"""

from my_math import prime_list_till


def number_rotations(n):
    digits: list[str] = list(str(n))
    rotate: list[int] = []

    for _ in range(len(digits)):
        digits.append(digits.pop(0))            # rotate digits
        rotate.append(int(''.join(digits)))

    return rotate                               # return rotated digits


def circular_prime_count(prime_lst: list[int])-> list[int]:
    circular_primes: list[int] = []                          # circukar primes pound
    
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

    return len(set(circular_primes))
    
    
if __name__ == "__main__":
    print(circular_prime_count(prime_list_till(1_000_000)))

