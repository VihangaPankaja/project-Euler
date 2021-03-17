# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from math import sqrt

number_range = int(input('Enter number range to find sum of primes: '))
prime_list = [2]

for i in range(3, number_range):

    temp_list = []
    for j in prime_list:
        temp_list.append(j)

        if j > sqrt(i):  # don't need to check numbers more then sqrt
            break

    for j in temp_list:
        if i % j == 0: # not prime
            break
    else:
        prime_list.append(i) # prime

print(sum(prime_list))

######fastest method found#######
# marked = [0] * 2000000       # create check box for each number
# value = 3                    # currunt checking value
# s = 2                        # total of primes

# while value < 2000000:
#     if marked[value] == 0:     # 0 means prime
#         s += value             # add prime value to total
#         i = value              # currunt prime

#         while i < 2000000:     # mark multiplications of currunt prime as not prime
#             marked[i] = 1
#             i += value

#     value += 2                 # check only for odd numbers

# print(s)
