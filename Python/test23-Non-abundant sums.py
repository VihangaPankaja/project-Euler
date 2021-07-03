"""
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
    For example,
        the sum of the proper divisors of 28 would be 
*       1 + 2 + 4 + 7 + 14 = 28, 
        which means that 28 is a perfect number.
  
    A number 𝑛 is called deficient 
        if the sum of its proper divisors is less than 𝑛 and
    
    it is called abundant if this sum exceeds 𝑛.
  
    As 12 is the smallest abundant number, 
*       1 + 2 + 3 + 4 + 6 = 16, 
    the smallest number that can be written as the sum of two abundant numbers is 24. 
  
    By mathematical analysis, 
*       it can be shown that all integers greater than 28123 
        can be written as the sum of two abundant numbers. 
    However, this upper limit cannot be reduced any further by analysis 
    even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
  
?   Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import numpy as np
import math as m


def abundant_nums_under(num: int) -> np.ndarray:
    """ get abundant numbers under given number

    Args:
    ----
        num (int): check for numbers under

    Returns:
    ----
        np.ndarray:
    """

    # fille array with false
    nums: np.ndarray = np.zeros(num+1, dtype=bool)

    for i in range(12, num+1, 6):   # multiples of 6 are abundant (6 is a perfect number)
        nums[i] = True

    for i in range(12, num+1):      # 12 is the first abundant number

        if not nums[i]:

            div_sum: int = 1        # include 1
            for j in range(2, m.floor(m.sqrt(i)) + 1):
                if i % j == 0:

                    if i//j == j:   # i/j also same
                        div_sum += j

                    else:
                        div_sum += j
                        div_sum += i/j

            if div_sum == i:            # is abundant and multiples of abundant also abundant
                for j in range(2*i, num+1, i):
                    nums[j] = True

            elif div_sum > i:           # is perfect number but multiples of perfect number is abundant
                for j in range(i, num+1, i):
                    nums[j] = True

    return np.nonzero(nums)[0]


def sum_of_non_abn_sums(abundants: np.ndarray, num: int) -> int:
    """ returns sum of positive inegers which cannot be represented as the sum of 2 abundant numbers

    Args:
    ----
        abundants (np.ndarray): abundant number array
        num (int): numbers under

    Returns:
    ----
        int:
    """

    non_abn_sums: np.ndarray = np.ones(num+1, dtype=bool)

    for i in abundants:
        for j in abundants:
            if (k := i+j) <= num:        # sum of abundants
                non_abn_sums[k] = False

            else:
                break

    # numbers doesn't get from sum of abundants
    return sum(np.nonzero(non_abn_sums)[0])


if __name__ == '__main__':
    print(sum_of_non_abn_sums(abundant_nums_under(28_123), 28_123))
