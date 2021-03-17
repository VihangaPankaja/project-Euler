# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the
# sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from my_math import divisors

max_non_abn = 28123

## check for abundant numbers in range
abn_lst = []
for i in range(max_non_abn):
    if sum(divisors(i + 1)) > (i + 1):
        abn_lst.append((i + 1))
####################################

## get sum of abundant numbers under range
sum_of_adn = []
for i in range(len(abn_lst)):
    for j in range(i, len(abn_lst)):
        if abn_lst[i] + abn_lst[j] > max_non_abn:
            break

        else:
            sum_of_adn.append(abn_lst[i] + abn_lst[j])
####################################


print(sum(i for i in range(1, max_non_abn + 1) if i not in sum_of_adn))   # sum of numbers not in list