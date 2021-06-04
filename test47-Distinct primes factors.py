""" 
  The first two consecutive numbers to have two distinct prime factors are:
*        14 = 2 × 7
*        15 = 3 × 5

  The first three consecutive numbers to have three distinct prime factors are:
*        644 = 2² × 7  × 23
*        645 = 3  × 5  × 43
*        646 = 2  × 17 × 19.

? Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers
"""

from my_math import is_prime


def distinct_prime_factors(n: int) -> int:
    """ reurns how many distinct prime factors to given number """

    prime_factors: set = set()

    while True:
        if is_prime(n):
            prime_factors.add(n)        # include prime to factors found
            return len(prime_factors)   # how many prime factors found

        elif n <= 1:
            return len(prime_factors)

        else:       # composite
            for i in range(2, int(n**0.5)+1):       # only check divicibility for √̅𝑛
                if n % i == 0:                  # if divisible
                    prime_factors.add(i)
                    n //= i                 # divide by prime factor
                    break


def consecutive_prime_factors(distinct_factors: int) -> int:
    """ returns first number for first n consecutive integers to have distinct n prime factors """

    cur_num = 10    # starts checking numbers from 9
    
    while True:
        found = []      # reset found numbers
        
        if distinct_prime_factors(cur_num) != distinct_factors:     # distinct prime factors of current number is not given number
            cur_num += distinct_factors                             # increment current number by given number
            
        else:                                                       # matching distinct prime factors
            found.append(cur_num)                                   # add matching number
            
            for i in range(distinct_factors - 1):                   # check for numbers below current number
                if distinct_prime_factors(cur_num - i - 1) == distinct_factors: # consecutive matching number found
                    found.append(cur_num - i - 1)
                
                else:       # no consecutive matching number found
                    break
                
            else:       # didn't break the loop (required consecutive matching numbers found)
                return min(found)
            
            for i in range(distinct_factors - len(found)):          # check for numbers above current number (only check for required amount)
                if distinct_prime_factors(cur_num + i + 1) == distinct_factors: # consecutive matching number found
                    found.append(cur_num + i + 1)
                    
                else:   # # no consecutive matching number found (no match in current range)
                    break
            
            else:       # didn't break the loop (required consecutive matching numbers found)
                return min(found)
            
            cur_num += distinct_factors     # optimize by adding given number
                

if __name__ == "__main__":
    print(consecutive_prime_factors(4))