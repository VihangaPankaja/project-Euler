""" 
    A googol (10¹⁰⁰) is a massive number: one followed by one-hundred zeros; 
    10¹⁰⁰ is almost unimaginably large: one followed by two-hundred zeros. Despite their size, 
    the sum of the digits in each number is only 1.

?   Considering natural numbers of the form, aᵇ, where a, b < 100, what is the maximum digital sum?
"""

def digit_sum(n: int) -> int:
    """ calculates the sum of the values of the digits in the given number """
    return sum(map(int, str(n)))


if __name__ == "__main__":
    print(max([digit_sum(n**m) 
                    for n in range(100) 
                    for m in range(100)]))