""" 
  The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
  but it also has a rather interesting sub-string divisibility property.
  
  Let 𝑑₁ be the 1ˢᵗ digit, 𝑑₂ be the 2ⁿᵈ digit, and so on. 
  In this way, we note the following:
*       𝑑₂𝑑₃𝑑₄  = 406   is divisible by 2
*       𝑑₃𝑑₄𝑑₅  = 063   is divisible by 3
*       𝑑₄𝑑₅𝑑₆  = 635   is divisible by 5
*       𝑑₅𝑑₆𝑑₇  = 357   is divisible by 7
*       𝑑₆𝑑₇𝑑₈  = 572   is divisible by 11
*       𝑑₇𝑑₈𝑑₉  = 728   is divisible by 13
*       𝑑₈𝑑₉𝑑₁₀ = 289   is divisible by 17

? Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from typing import Generator
from itertools import permutations


def divicible_pandigital(divicible: dict[str, dict[str, bool]]) -> Generator[int, None, None]:
    """ 
        generates 0 to 9 digits pandigital numbers that are follows
            * 𝑑₂𝑑₃𝑑₄  is divisible by 2
            * 𝑑₃𝑑₄𝑑₅  is divisible by 3
            * 𝑑₄𝑑₅𝑑₆  is divisible by 5
            * 𝑑₅𝑑₆𝑑₇  is divisible by 7
            * 𝑑₆𝑑₇𝑑₈  is divisible by 11
            * 𝑑₇𝑑₈𝑑₉  is divisible by 13
            * 𝑑₈𝑑₉𝑑₁₀ is divisible by 17
        rules where 𝑑ₙ is 𝑛ᵗʰ digit
    """

    for digits in permutations(map(str, range(10))):
        num: str = ''.join(digits)   # digits to number

        if all((
            num[0] != '0',
            divicible['d2'][num[1:4]],
            divicible['d3'][num[2:5]],
            divicible['d5'][num[3:6]],
            divicible['d7'][num[4:7]],
            divicible['d11'][num[5:8]],
            divicible['d13'][num[6:9]],
            divicible['d17'][num[7:10]]
        )):     # check if follow digits divicible rules follows and not starts with 0
            yield int(num)


def make_divisible_dic():
    nums = [k for i in range(1000) if len(set((k:= str(i).rjust(3, '0')))) == 3]

    divicible: dict[str, dict[str, bool]] = {
        'd2': {i: False for i in nums},
        'd3': {i: False for i in nums},
        'd5': {i: False for i in nums},
        'd7': {i: False for i in nums},
        'd11': {i: False for i in nums},
        'd13': {i: False for i in nums},
        'd17': {i: False for i in nums}
    }

    for i in divicible['d2'].keys():
        if int(i) % 2 == 0:
            divicible['d2'][i] = True
        if int(i) % 3 == 0:
            divicible['d3'][i] = True
        if int(i) % 5 == 0:
            divicible['d5'][i] = True
        if int(i) % 7 == 0:
            divicible['d7'][i] = True
        if int(i) % 11 == 0:
            divicible['d11'][i] = True
        if int(i) % 13 == 0:
            divicible['d13'][i] = True
        if int(i) % 17 == 0:
            divicible['d17'][i] = True
            
    return divicible


if __name__ == "__main__":
    print(sum(divicible_pandigital(make_divisible_dic())))
