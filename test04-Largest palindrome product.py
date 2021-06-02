""" 
  A palindromic number reads the same both ways. 
  The largest palindrome made from the product of two 2-digit numbers is
* 9009 = 91 × 99.

? Find the largest palindrome made from the product of two 3-digit numbers
"""



def prod_digit_palindrome(num: int)-> list[int]:
    """ return list of palindroms for given digit factors """
    
    num_list: list[int] = []   # list for posiible palindrome numbers for given digits in factors


    for i in range((10 ** (num - 1)), (10 ** num)):   ### possible factors for given digits 
        for j in range((10 ** (num - 1)), (10 ** num)):                                      ###

            mul_asc = i * j
            mul_dec = int(str(mul_asc)[-1::-1])     ##### check product equal to itself when reversed
            if mul_dec == mul_asc:                                                                   #####
                num_list.append(mul_asc)
    return num_list


if __name__ == '__main__':
    print(max(prod_digit_palindrome(3)))