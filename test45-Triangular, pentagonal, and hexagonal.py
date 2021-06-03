""" 
  Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
*   Triangle	 	    𝑇ₙ = 𝑛(𝑛+1)/2	 	        1, 3, 6, 10, 15, ...
*   Pentagonal	 	    𝑃ₙ = 𝑛(3𝑛−1)/2	 	        1, 5, 12, 22, 35, ...
*   Hexagonal	 	    𝐻ₙ = 𝑛(2𝑛−1)	 	            1, 6, 15, 28, 45, ...

  It can be verified that 𝑇₂₈₅ = 𝑃₁₆₅ = 𝐻₁₄₃ = 40755.

? Find the next triangle number that is also pentagonal and hexagonal.
"""

from typing import Generator


def triangle(n: int=286)-> Generator[int, None, None]:
    """ 
    generates triangle numbers
        Parameters:
            n (int): (optional) starts with given number
            
    ! infine generator
    """
    
    while True:
        yield int(n * (n + 1) / 2)
        n += 1
        

def is_pentagonal(n: int)-> bool:
    if (1 + (1 + 24*n)**0.5) % 6 == 0:
        return True
    
    return False


def is_hexagonal(n: int)-> bool:
    if (1 + (1 + 8*n)**0.5) % 4 == 0:
        return True
    
    return False


def next_3_5_6_num()-> int:
    for i in triangle():
        if is_pentagonal(i) and is_hexagonal(i):
            return i


if __name__ == '__main__':
    print(next_3_5_6_num())