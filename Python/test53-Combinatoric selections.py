"""
    There are exactly ten ways of selecting three from five, 12345:
*       123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation,
  
        ⎛ 5 ⎞  = 10
        ⎜ 3 ⎟   
        ⎝   ⎠

    In general,
*                     𝑛!
*        ⎛ 𝑛 ⎞  = ⎯⎯⎯⎯⎯⎯⎯⎯⎯   where, 𝑟 ≤ 𝑛, 𝑛! = 𝑛 × (𝑛 - 1) × ... × 3 × 2 × 1  and 0! = 1
*        ⎜ 𝑟      𝑟!(𝑛 - 𝑟)!
*        ⎝   ⎠

    It is not until 𝑛 = 23, that a value exceeds one-million: 
          
        ⎛ 23 ⎞  = 1144066
        ⎜ 10 ⎟   
        ⎝    ⎠

?   How many, not necessarily distinct, values of 
?
?    ⎛ 𝑛 ⎞   for 1 ≤ 𝑛 ≤ 100, are greater than one-million?
?    ⎜ 𝑟     
?    ⎝   ⎠
"""

from math import factorial
from typing import Generator


def nCr_above_million(n: int) -> Generator[int, None, None]:
    """ calculates ⁿ𝐶ᵣ values above 1_000_000

    Args:
    ----
        n (int): number for ⁿ𝐶ᵣ

    Yields:
    ----
        Generator[int, None, None]:
        
    >>> [nCr_above_millon(23)]
    ... [1144066, 1352078, 1352078, 1144066]
    """
    
    for r in range(n):
        if (nCr:= factorial(n) // (factorial(r)*factorial(n-r))) > 1_000_000:
            yield nCr
            
    
if __name__ == "__main__":
    print(sum(len([*nCr_above_million(i)]) for i in range(1, 101)))