# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from  math import factorial, log10

fatorials_for_digts = {0:factorial(0), 1:factorial(1), 2: factorial(2), 3: factorial(3), 4: factorial(4), 
                                5: factorial(5), 6: factorial(6), 7: factorial(7), 8: factorial(8), 9: factorial(9)}   # dictionary of factorils for respective digits for reduse proccesing needed


numbers = []
for n in range(10, 7 * factorial(9)):    # all possible number range at 7 digits it reaches maximum like this
    digits = list(map(int, str(n)))      # n as a digit list
    
    if fatorials_for_digts[max(digits)] > n:    # check factorial of maximum digit exceeds n
        continue

    if n == sum(map(lambda x: fatorials_for_digts[x], digits)):     # what was asked
        numbers.append(n)

print(sum(numbers))