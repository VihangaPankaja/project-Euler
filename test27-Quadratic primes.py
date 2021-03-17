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



######less optimised code. run time about an hour############

from my_math import prime_list_till

a = range(-999, 1000)  # a value range
b = range(-1000, 1001) # b value range
dictionary = {0: 0}  # key = prime numbers count , values = a,b values used


## count primes possible for given a,b ##
def q_formula_prime_count(a, b):
    n = 0
    prime_coun = 0
    while True:
        if isPrime((n ** 2) + (a * n) + b):
            prime_coun += 1
        else:
            break
        n += 1
    return prime_coun
##########################################


primes = prime_list_till(1000000)  # get prime list till 1 000 000


## check if prime ##
def isPrime(n):
    if n in primes:
        return True
    else:
        return False
####################


## get primes possible for all a,b values ##
for i in a:
    for j in b:
        prime_coun = q_formula_prime_count(i, j)
        dictionary[prime_coun] = (i, j)
#############################################


a, b = dictionary[max(dictionary.keys())]  # get a,b for maximus primes found
print(a * b)
