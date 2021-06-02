""" 
  The sum of the squares of the first ten natural numbers is,
* 1² + 2² + ... + 10² = 385

  The square of the sum of the first ten natural numbers is,
* (1 + 2 + ... + 10)² = 55^2 = 3025

  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
* 3025 - 385 = 2640.

? Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
"""



def diff(num: int)-> int:
       ###########{         sum of squares            }######{    square of sum              }########
       return (sum(n for n in range(1, num + 1)) ** 2) - sum(n ** 2 for n in range(1, num + 1))


if __name__ == "__main__":
       print(diff(100))