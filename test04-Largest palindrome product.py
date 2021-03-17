#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers


num = int(input('number in two factors of palidrome numbers: '))
num_list = []   # list for posiible palindrome numbers for given digits in factors


for i in range((10 ** (num - 1)), (10 ** num)):   ### possible factors for given digits 
    for j in range((10 ** (num - 1)), (10 ** num)):                                      ###
        mul_asc = i * j
        
        mul_dec = int(str(mul_asc)[-1::-1])     ##### check product equal to itself when reversed
        if mul_dec == mul_asc:                                                                   #####
            num_list.append(mul_asc)


print(max(num_list))