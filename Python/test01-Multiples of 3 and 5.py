"""
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
    The sum of these multiples is 23.
  
?   Find the sum of all the multiples of 3 or 5 below 1000.
"""


def total(num: int) -> int:
    return sum(n for n in range(num) if (n%3 == 0 or n%5 == 0))


if __name__ == '__main__':
    print(total(1000)) 
