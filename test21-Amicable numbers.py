""" 
  Let d(𝑛) be defined as the sum of proper divisors of 𝑛 (numbers less than 𝑛 which divide evenly into 𝑛)
  .
* If d(𝑎) = 𝑏 and d(𝑏) = 𝑎, where 𝑎 ≠ 𝑏, 
  then 𝑎 and 𝑏 are an amicable pair and each of 𝑎 and 𝑏 are called amicable numbers.
  
  For example, the proper divisors of 220 are 
  1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
  therefore d(220) = 284. 
  
  The proper divisors of 284 are,
  1, 2, 4, 71 and 142; 
  so d(284) = 220.

? Evaluate the sum of all the amicable numbers under 10000. 
"""

import my_math


def uncheck_prime() -> None:
    prime_lst = my_math.prime_list_till(amicable_num - 1)       # get primes under target

    num_check[0] = -1   # uncheck number 1

    for i in prime_lst:
        num_check[i - 1] = -1
        
    return None


def d(n: int) -> int:
    '''return sum divisors'''
    divisors = []

    for i in range(1, int(n/2 + 1)):
        if n % i == 0:
            divisors.append(i)

    return sum(divisors)


def amicable_cheack() -> list[int]:
    for i in range(1, amicable_num):
        if num_check[i - 1] == 0:           # check if not unchecked

            if i == d(d(i)) and i != d(i):   # ckeck for amicable number
                num_check[i - 1] = d(i)         # mark amikable
                num_check[d(i) - 1] = i         # mark amicable

            else:
                num_check[i - 1] = -1           # uncheck
                
    return num_check


if __name__ == "__main__":
    amicable_num: int = 10000
    num_check: list[int] = [0] * (amicable_num - 1)     # as a checkbox for every number
    
    print(sum(i for i in amicable_cheack() if i != -1))