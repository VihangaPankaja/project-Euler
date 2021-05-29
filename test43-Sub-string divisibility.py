# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting 
# sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

from typing import Generator, Iterator
from itertools import permutations


def divicible_pandigital(divicible: dict[str, Iterator[str]])-> Generator[int, None, None]:
    """ 
        generates 0 to 9 digits pandigital numbers that are follows
            d2d3d4 is divisible by 2
            d3d4d5 is divisible by 3
            d4d5d6 is divisible by 5
            d5d6d7 is divisible by 7
            d6d7d8 is divisible by 11
            d7d8d9 is divisible by 13
            d8d9d10 is divisible by 17
        rules where dn is nth digit
    """
    
    for digits in permutations(map(str, range(10))):
        num: str = ''.join(digits)   # digits to number
        
        if all((
                num[0]!='0', 
                num[1:4] in divicible['d2'], 
                num[2:5] in divicible['d3'], 
                num[3:6] in divicible['d5'], 
                num[4:7] in divicible['d7'], 
                num[5:8] in divicible['d11'], 
                num[6:9] in divicible['d13'], 
                num[7:10] in divicible['d17']
            )):     # check if follow digits divicible rules follows and not starts with 0 
            yield int(num)


if __name__ == "__main__":
    #################################################################################################################################################
    divicible: dict[str, list[str]] = {
        ###############    filter only has different digits     ############ fill 0 till 3 digits ## numbers divicible by 2 have max 3 digits ###
        'd2':list(filter(lambda x: all([x.count(i)==1 for i in x]), map( lambda x:str(x).rjust(3,'0') , [ i for i in range(1000) if i%2 == 0 ] ))),
        'd3':list(filter(lambda x: all([x.count(i)==1 for i in x]), map( lambda x:str(x).rjust(3,'0') , [ i for i in range(1000) if i%3 == 0 ] ))),
        'd5':list(filter(lambda x: all([x.count(i)==1 for i in x]), map( lambda x:str(x).rjust(3,'0') , [ i for i in range(1000) if i%5 == 0 ] ))),
        'd7':list(filter(lambda x: all([x.count(i)==1 for i in x]), map( lambda x:str(x).rjust(3,'0') , [ i for i in range(1000) if i%7 == 0 ] ))),
        'd11':list(filter(lambda x: all([x.count(i)==1 for i in x]), map( lambda x:str(x).rjust(3,'0') , [ i for i in range(1000) if i%11 == 0 ] ))),
        'd13':list(filter(lambda x: all([x.count(i)==1 for i in x]), map( lambda x:str(x).rjust(3,'0') , [ i for i in range(1000) if i%13 == 0 ] ))),
        'd17':list(filter(lambda x: all([x.count(i)==1 for i in x]), map( lambda x:str(x).rjust(3,'0') , [ i for i in range(1000) if i%17 == 0 ] )))
    }
    ##################################################################################################################################################
    
    print(sum(divicible_pandigital(divicible)))