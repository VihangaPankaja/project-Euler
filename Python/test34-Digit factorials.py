"""
    145 is a curious number, 
*       as 1! + 4! + 5! = 1 + 24 + 120 = 145.
  
?   Find the sum of all numbers which are equal to the sum of the factorial of their digits.
  
    NOTE: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from  math import factorial


def factorial_digits() -> list[int]:
    factorials_for_digits: dict[int, int] = {x:factorial(x) for x in range(10)}   # dictionary of factorils for respective digits for reduse processing needed
    numbers: list[int] = []

    for n in range(10, 7*factorial(9)):    # all possible number range at 7 digits it reaches maximum like this
        digits: list[int] = list(map(int, str(n)))      # n as a digit list

        if factorials_for_digits[max(digits)] > n:    # check factorial of maximum digit exceeds n
            continue

        if n == sum(map(lambda x: factorials_for_digits[x], digits)):     # what was asked
            numbers.append(n)
            
    return numbers


if __name__ == "__main__":
    print(sum(factorial_digits()))