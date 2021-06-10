"""
 We shall say that an n-digit number is pandigital 
    if it makes use of all the digits 1 to n exactly once; 
    for example, 
        the 5-digit number, 15234, is 1 through 5 pandigital.
 
 The product 7254 is unusual, as the identity, 
    39 × 186 = 7254, 
    containing multiplicand, multiplier, and product is 1 through 9 pandigital.
 
 ? Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
 
 NOTE: Some products can be obtained in more than one way so be sure to only include it once in your sum.
 """
                    
from itertools import permutations


def pandigital_nums() -> set[int]:
    nums_found: set[int] = set()   
    
    def is_pandigital(product: int, digits: tuple[int]) -> bool:
        """ check if pandigital """
        
        for i in map(int, str(product)):
            if i in digits or i == 0:    # also no 0 in digits
                return False
        return True
    
    
    for digits in permutations([*range(1, 10)], 5):      # factors only using digits once
        
        ## 1 digit by 4 digit posibilities ##
        product: int = (digits[0] 
                        * int(''.join(map(str, digits[1:]))))  # product in $ * $$$$
        
        if 1(000 <= product <= 9999 and         # check if contains 4 digits
             len(set(str(product))) == 4 and    # check product has different digits
             is_pandigital(product, digits)):   # chech product and identity is pandigital  
              
            nums_found.add(product)
        
        
        ## 2 digit by 3 digit posibilities ##
        product: int= (int(''.join(map(str, digits[:2]))) 
                       * int(''.join(map(str, digits[2:]))))  # product in $$ * $$$
        
        if (1000 <= product <= 9999 and         # check if contains 4 digits
            len(set(str(product))) == 4 and     # check product has different digits 
            is_pandigital(product, digits)):    # chech product and identity is pandigital
            
            nums_found.add(product)
            
            
    return nums_found


if __name__ == '__main__':
    print(sum(pandigital_nums()))