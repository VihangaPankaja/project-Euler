"""
  Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
*   1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
*   8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
*   9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴

  As 1 = 1⁴ is not a sum it is not included. 
  The sum of these numbers is 1634 + 8208 + 9474 = 19316.
  
? Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def num_range(power_for_sum: int)-> int:
    """ find the number which digtis used exceeds the digits in sum """

    n: int = 0
    while True:
        n += 1
        val: int = n * (9 ** power_for_sum)
        if len(str(val)) < n:
            break
        
    return n


def aft_sum(nums: list[str], power_for_sum: int)-> int:
    """ sum of digits that raised to the given power """
    
    nums = list(map(int, nums))

    return sum(i ** power_for_sum for i in nums)


def digits(nums: list[str])-> int:
    """ return decimal from string digits """
    
    return int(''.join(nums))


def mathing_nums(power_for_sum: int)-> list[int]:
    """ find matchong numbers """

    mach: list[int]= []

    for i in [list(str(x)) for x in range(10 ** (num_range(power_for_sum) - 1))]:  #check numbers in possible range found from (𝑛-1)
        a: int = aft_sum(i, power_for_sum)
        
        if a == digits(i) and not (a ==0 or a == 1):   # check for digits in sum are equal to the digits used
            mach.append(a)
            
    return mach


if __name__ == '__main__':
    print(sum(mathing_nums(5)))