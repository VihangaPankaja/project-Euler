""" 
  It can be seen that the number, 
    125874, and its double, 251748, 
    contain exactly the same digits, but in a different order.

? Find the smallest positive integer, x, such that 
?   2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

import array


def is_multiple_same_digit(number: int, multiple: int) -> bool:
    """ Check if a multiple of a given number has the same digits

    Args:
    ----
        number (int): number check for multiples
        multiple (int): multiplier

    Returns:
    ----
        bool:
    """
    
    if len(i:= str(number)) != len(j:= str(number*multiple)):   # length mismatch
        return False
    
    product: array = array.array('u', j)
    for digit in i:
        try:    # check if all digits similar
            product.remove(digit)
        except ValueError:
            return False
    
    return True


def main() -> int:
    """ find the smallest number that 2,3,4,5,6 multipliers contains same digits

    Returns:
    ----
        int:
    """
    
    i: int = 11
    
    while True:
        if all([is_multiple_same_digit(i, 2),
                is_multiple_same_digit(i, 3),
                is_multiple_same_digit(i, 4),
                is_multiple_same_digit(i, 5),
                is_multiple_same_digit(i, 6)]):     # check all multiles have same digits
            return i
        
        i += 1


if __name__ == "__main__":
    print(main())