""" 
    It is possible to show that the square root of two can be expressed as an infinite continued fraction.
            √̅₂ = 1 + 1/(2 + 1/(2 + 1/(2 + ...)))

    By expanding this for the first four iterations, we get:
        1 + 1/2                         = 3/2   = 1.5
        1 + 1/(2 + 1/2)                 = 7/5   = 1.4
        1 + 1/(2 + 1/(2 + 1/2))         = 17/12 = 1.41666...
        1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
        
    The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, 
    is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

?   In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

from typing import Generator
from fractions import Fraction

def fraction_expantion_of_root2(iterations: int) -> Generator[Fraction, None, None]:
    """ generates continuous fraction expansion of root 2 for given iterations """
    
    T_n = Fraction(1)
    for _ in range(iterations):
        T_n = 1 + 1/(1 + T_n)
        yield T_n
        

if __name__ == "__main__":
    print(sum([len(str(i.numerator)) > len(str(i.denominator)) 
               for i in fraction_expantion_of_root2(1000)]))