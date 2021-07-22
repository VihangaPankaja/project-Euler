"""
    The prime factors of 13195 are 5, 7, 13 and 29.

?   What is the largest prime factor of the number 600851475143
"""


def largest_prime_factor(num: int) -> int:
    """ find the largest prime factor

    Args:
    ----
        num (int): number

    Returns:
    ----
        int: 
    """
    tempnum: int = num
    lastnum: int = 2
    lrgfact: int = 1

    while tempnum > lastnum:
        for i in range(lastnum, int(tempnum+1)) :  # check for divisible numbers, start from last divisible number
            
            if tempnum % i == 0:  # if dividable
                if i > lrgfact:   # if currunt factor larger than previous one
                    lrgfact = i

                tempnum /= i  # other factor
                lastnum = i

                break   # run until there are no facrots

    if tempnum > lrgfact:
        lrgfact = tempnum
    return lrgfact


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
