""" 
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
    but it also has a rather interesting sub-string divisibility property.
    
    Let ๐โ be the 1หขแต digit, ๐โ be the 2โฟแต digit, and so on. 
    In this way, we note the following:
*       ๐โ๐โ๐โ  = 406   is divisible by 2
*       ๐โ๐โ๐โ  = 063   is divisible by 3
*       ๐โ๐โ๐โ  = 635   is divisible by 5
*       ๐โ๐โ๐โ  = 357   is divisible by 7
*       ๐โ๐โ๐โ  = 572   is divisible by 11
*       ๐โ๐โ๐โ  = 728   is divisible by 13
*       ๐โ๐โ๐โโ = 289   is divisible by 17

?   Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from typing import Generator
from itertools import permutations


def divisible_pandigital(divisible: dict[str, dict[str, bool]]) -> Generator[int, None, None]:
    """ 
    generates 0 to 9 digits pandigital numbers that are follows
        * ๐โ๐โ๐โ  is divisible by 2
        * ๐โ๐โ๐โ  is divisible by 3
        * ๐โ๐โ๐โ  is divisible by 5
        * ๐โ๐โ๐โ  is divisible by 7
        * ๐โ๐โ๐โ  is divisible by 11
        * ๐โ๐โ๐โ  is divisible by 13
        * ๐โ๐โ๐โโ is divisible by 17
        
        rules where ๐โ is ๐แตสฐ digit
    
    Args:
    ----
        divisible (dict[str, dict[str, bool]]): dictionary of divisibility

    Yields:
    ----
        Generator[int, None, None]: 
    """

    for digits in permutations(map(str, range(10))):
        num: str = ''.join(digits)   # digits to number

        if all((
            num[0] != '0',
            divisible['d2'][num[1:4]],
            divisible['d3'][num[2:5]],
            divisible['d5'][num[3:6]],
            divisible['d7'][num[4:7]],
            divisible['d11'][num[5:8]],
            divisible['d13'][num[6:9]],
            divisible['d17'][num[7:10]]
        )):     # check if follow digits divisible rules follows and not starts with 0
            yield int(num)


def make_divisible_dic() -> dict[str, dict[str, bool]]:
    """ make dictionary of divisible number divisibility under 1000

    Returns:
    ----
        dict[str, dict[str, bool]]: divisible by 2,3,5,7,11,13,17
        
    >>> make_divisible_dic()
    ... {'d2':{'000':True, '001':False, '002':True, ..., '999':False},'d3':{...}, ..., 'd17':{...}}
    """
    
    nums = [k for i in range(1000) if len(set((k:= str(i).rjust(3, '0')))) == 3]

    divisible: dict[str, dict[str, bool]] = {
        'd2': {i: False for i in nums},
        'd3': {i: False for i in nums},
        'd5': {i: False for i in nums},
        'd7': {i: False for i in nums},
        'd11': {i: False for i in nums},
        'd13': {i: False for i in nums},
        'd17': {i: False for i in nums}
    }

    for i in divisible['d2'].keys():
        if int(i) % 2 == 0:
            divisible['d2'][i] = True
        if int(i) % 3 == 0:
            divisible['d3'][i] = True
        if int(i) % 5 == 0:
            divisible['d5'][i] = True
        if int(i) % 7 == 0:
            divisible['d7'][i] = True
        if int(i) % 11 == 0:
            divisible['d11'][i] = True
        if int(i) % 13 == 0:
            divisible['d13'][i] = True
        if int(i) % 17 == 0:
            divisible['d17'][i] = True
            
    return divisible


if __name__ == "__main__":
    print(sum(divisible_pandigital(make_divisible_dic())))
