"""
    A unit fraction contains 1 in the numerator. 
  
    The decimal representation of the unit fractions with denominators 2 to 10 are given:
*       ⅟₂	= 	0.5
*       ⅟₃	= 	0.(3)
*       ⅟₄	= 	0.25
*       ⅟₅	= 	0.2
*       ⅟₆	= 	0.1(6)
*       ⅟₇	= 	0.(142857)
*       ⅟₈	= 	0.125
*       ⅟₉	= 	0.(1)
*       ⅟₁₀	= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
  
    It can be seen that ⅟₇ has a 6-digit recurring cycle.

?   Find the value of 𝑑 < 1000 for which 1/𝑑 contains the longest recurring cycle in its decimal fraction part.
"""


def cycle_lenth(d: int) -> int:
    """ returns number of rucurring digits for 1/𝑑 for given 𝑑

    Args:
    ----
        d (int): 𝑑

    Returns:
    ----
        int:
    """
    
    remainig: list[int] = [1]   # because 1/
    
    while True:
        remainig.append((remainig[-1]*10) % d)    ## remaing from dividing

        if remainig[-1] == 0:                       # check if 1/𝑑 has no recurring digits
            return 0

        elif remainig[-1] in remainig[:-1]:        ## check for recurring cycle completed
            return (len(remainig) 
                    - remainig.index(remainig[-1]) 
                    - 1)


def longest_repeating_decimal(max_d: int) -> int:
    """ returns longest repeating decimal for ⅟₂ to 1/𝑑 when 𝑑 is given

    Args:
    ----
        max_d (int): maximum 𝑑

    Returns:
    ----
        int:
    """
    
    cyc_lenths: list[int] = []      # list of number of recurring digits for given number

    for d in range(1, max_d):
        cyc_lenths.append(cycle_lenth(d))

    return cyc_lenths.index(max(cyc_lenths)) + 1        # find dthat has max recurring digit cycle


if __name__ == '__main__':
    print(longest_repeating_decimal(1_000))
