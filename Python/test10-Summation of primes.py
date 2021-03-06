"""
    The sum of the primes below 10 is 
*       2 + 3 + 5 + 7 = 17.

?   Find the sum of all the primes below two million.
"""

def sum_of_primes_till(number_range: int) -> int:
    """ return sum of primes under given number

    Args:
    ----
        number_range (int): number

    Returns:
    ----
        int:
    """
    
    marked = [0] * number_range       # create check box for each number
    value = 3                    # currunt checking value
    s = 2                        # total of primes

    while value < number_range:
        if marked[value] == 0:     # 0 means prime
            s += value             # add prime value to total
            i = value              # currunt prime

            while i < number_range:     # mark multiplications of currunt prime as not prime
                marked[i] = 1
                i += value

        value += 2                 # check only for odd numbers

    return s
    
    
if __name__ == '__main__':
    print(sum_of_primes_till(2_000_000))