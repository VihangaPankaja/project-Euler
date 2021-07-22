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


def cycle_length(d: int) -> int:
    """ returns number of recurring digits for 1/𝑑 for given 𝑑

    Args:
    ----
        d (int): 𝑑

    Returns:
    ----
        int:
    """
    
    remaining: list[int] = [1]   # because 1/
    
    while True:
        remaining.append((remaining[-1]*10) % d)    ## remaining from dividing

        if remaining[-1] == 0:                       # check if 1/𝑑 has no recurring digits
            return 0

        elif remaining[-1] in remaining[:-1]:        ## check for recurring cycle completed
            return (len(remaining) 
                    - remaining.index(remaining[-1]) 
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
    
    cyc_lengths: list[int] = []      # list of number of recurring digits for given number

    for d in range(1, max_d):
        cyc_lengths.append(cycle_length(d))

    return cyc_lengths.index(max(cyc_lengths)) + 1        # find that has max recurring digit cycle


if __name__ == '__main__':
    print(longest_repeating_decimal(1_000))
