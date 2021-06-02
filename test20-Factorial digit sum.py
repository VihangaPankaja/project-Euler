"""
  𝑛! means,
*   𝑛 × (𝑛 − 1) × ... × 3 × 2 × 1

  For example, 
* 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
  and the sum of the digits in the number 10! is,
* 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

? Find the sum of the digits in the number 100!
"""

from math import factorial

def factorial_sum(num: int)-> int:
    return sum(int(i) for i in str(factorial(num)))


if __name__ == '__main__':
    print(factorial_sum(100))