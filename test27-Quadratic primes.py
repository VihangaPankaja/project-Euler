""" 
Euler discovered the remarkable quadratic formula:
*    𝑛² + 𝑛 + 41
  It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= 𝑛 <= 39. However,
  when 𝑛 = 40, 
    40² + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
    and certainly when 𝑛 = 41, 
        41² + 41 + 41 is clearly divisible by 41.

  The incredible formula 𝑛² - 79𝑛 + 1601 was discovered, 
  which produces 80 primes for the consecutive values 0 <= 𝑛 <= 79.
  The product of the coefficients, −79 and 1601, is −126479.

  Considering quadratics of the form:
*       𝑛² + 𝑎𝑛 + 𝑏, where |𝑎| < 1000 and |𝑏| <= 1000
        where |𝑛| is the modulus/absolute value of 𝑛
            e.g. |11| = 11 and |-4| = 4

? Find the product of the coefficients, 𝑎 and 𝑏, 
?   for the quadratic expression that produces the maximum number
?   of primes for consecutive values of 𝑛, starting with 𝑛 = 0
"""



###### ! less optimised code. run time about an hour 😢 ############

from my_math import prime_list_till


def q_formula_prime_count(a, b):
    """ count primes possible for given 𝑎,𝑏 """ 

    n: int = 0
    prime_coun: int = 0

    while True:
        if isPrime((n ** 2) + (a * n) + b):
            prime_coun += 1
            
        else:
            break
        
        n += 1
        
        
    return prime_coun


def isPrime(n: int)-> bool:
    """ check if prime """

    if n in primes:
        return True

    else:
        return False


def main()-> tuple[int]:
    global primes

    a: range = range(-999, 1000)        # 𝑎 value range
    b: range = range(-1000, 1001)       # 𝑏 value range
    dictionary: dict = {0: 0}        # key = prime numbers count , values = 𝑎,𝑏 values used
    primes: list[int] = prime_list_till(1000000)  # get prime list till 1 000 000

    
    """ get primes possible for all 𝑎,𝑏 values """ 

    for i in a:
        for j in b:
            prime_coun: int = q_formula_prime_count(i, j)
            dictionary[prime_coun] = (i, j)

    return dictionary[max(dictionary.keys())]  # get 𝑎,𝑏 for maximus primes found



if __name__ == '__main__':
    a, b = main()
    print(a * b)
