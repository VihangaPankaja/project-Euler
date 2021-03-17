# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

power_for_sum = 5

## find the number which digtis used exceeds the digits in sum ##
n = 0
while True:
    n += 1
    val = n * (9 ** power_for_sum)
    if len(str(val)) < n:
        break
##################################

## sum of digits that raised to the given power ##
def aft_sum(nums):
    global power_for_sum
    nums = list(map(int, nums))
    return sum(i ** power_for_sum for i in nums)

## return digits in string
def digits(nums):
    return int(''.join(nums))


mach = []
for i in (list(str(x)) for x in range(10 ** (n-1))):  #check numbers in possible range found from (n-1)
    a = aft_sum(i)
    if a == digits(i) and not (a ==0 or a == 1):   # check for digits in sum are equal to the digits used
        mach.append(a)

print(sum(mach))