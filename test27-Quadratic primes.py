# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However,
# when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79.
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| <= 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
# of primes for consecutive values of n, starting with n = 0



###### less optimised code. run time about an hour 😢 ############

from my_math import prime_list_till


def q_formula_prime_count(a, b):
    """ count primes possible for given a,b """ 

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

    a: range = range(-999, 1000)  # a value range
    b: range = range(-1000, 1001) # b value range
    dictionary: dict = {0: 0}  # key = prime numbers count , values = a,b values used
    primes: list[int] = prime_list_till(1000000)  # get prime list till 1 000 000

    
    """ get primes possible for all a,b values """ 

    for i in a:
        for j in b:
            prime_coun: int = q_formula_prime_count(i, j)
            dictionary[prime_coun] = (i, j)

    return dictionary[max(dictionary.keys())]  # get a,b for maximus primes found



if __name__ == '__main__':
    a, b = main()
    print(a * b)
