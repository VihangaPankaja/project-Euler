"""
    The fraction 49/98 is a curious fraction, 
    as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, 
    is obtained by cancelling the 9s.
    
    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    
    There are exactly four non-trivial examples of this type of fraction, 
    less than one in value, and containing two digits in the numerator and denominator.

?   If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from math import prod


def non_trivial_product() -> tuple[int, int]:
    """ find the product of 4 non-trivial fractions

    Returns:
    ----
        tuple[int, int]: (numerator, denominator)
    """
    
    pos_prod: list[tuple[int]] = []
    
    for i, j in ((n, m) for n in range(11,100) 
                        for m in range(n + 1, 100) 
                        if n % 10 != 0 and m % 10 != 0):    # all possible numerators and denominators
        
        if (list(str(i))[0] not in list(str(j)) and 
            list(str(i))[1] not in list(str(j))):                      # clearing numbers that don't have similar digit
            
            continue

        lst_i = list(map(int, str(i)))   ## digits in chosen numbers
        lst_j = list(map(int, str(j)))   ###########################

        if lst_i[0] in lst_j:  # check for similar digits
            lst_j.remove(lst_i[0])   # remove similar digits
            lst_i.remove(lst_i[0])

            if (i/j) == (lst_i[0] / lst_j[0]):       # check same after removing similar digits
                pos_prod.append((lst_i[0], lst_j[0]))
        
        elif lst_i[1] in lst_j:   # check for similar digits
            lst_j.remove(lst_i[1])   # remove similar digits
            lst_i.remove(lst_i[1])

            if (i/j) == (lst_i[0] / lst_j[0]):     # check same after removing similar digits
                pos_prod.append((lst_i[0], lst_j[0]))

    return (prod(i[0] for i in pos_prod), 
            prod(i[1] for i in pos_prod))   # products of numerators and denominators


def simplify_frac(nuratr: int, denmtr: int) -> int:
    """ returns denominator of the simplified fraction

    Args:
    ----
        nuratr (int): numeratror
        denmtr (int): denominator

    Returns:
    ----
        int:
    """
    
    for i in range(nuratr, 0, -1):            # simplify the fraction
        if (nuratr % i == 0 and 
            denmtr % i == 0):
            
            nuratr /= i
            denmtr /= i
        
        if nuratr == 1:
            break
    
    return denmtr


if __name__ == '__main__':
    print(int(simplify_frac(*non_trivial_product())))