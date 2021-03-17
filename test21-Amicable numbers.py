# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
# are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import my_math

amicable_num = 10000
num_check = [0] * (amicable_num - 1)     # as a checkbox for every number
prime_lst = my_math.prime_list_till(amicable_num - 1)       # get primes under target

num_check[0] = -1   # uncheck number 1

## uncheck all primes
for i in prime_lst:
    num_check[i - 1] = -1
###################


def d(n):
    '''return sum divisors'''
    divisors = []

    for i in range(1, int(n / 2 + 1)):
        if n % i == 0:
            divisors.append(i)

    return sum(divisors)


for i in range(1, amicable_num):
    if num_check[i - 1] == 0:           # check if not unchecked

        if i == d(d(i)) and i != d(i):   # ckeck for amicable number
            num_check[i - 1] = d(i)         # mark amikable
            num_check[d(i) - 1] = i         # mark amicable

        else:
            num_check[i - 1] = -1           # uncheck

print(sum(i for i in num_check if i != -1))