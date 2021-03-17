# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

numbers = list(range(1,10))   # digits using
nums_found = []


tem_numbers = numbers.copy()
for i in tem_numbers:                               ## strat of number selector from digits ##
    tem_num1 = tem_numbers.copy()
    tem_num1.remove(i)
    for j in tem_num1:
        tem_num2 = tem_num1.copy()
        tem_num2.remove(j)
        for k in tem_num2:
            tem_num3 = tem_num2.copy()
            tem_num3.remove(k)
            for l in tem_num3:
                tem_num4 = tem_num3.copy()
                tem_num4.remove(l)
                for m in tem_num4:
                    tem_num5 = tem_num4.copy()
                    tem_num5.remove(m)              ## end of number selector form digits ##
                    
                    ## 1 digit by 4 digit posibilities ##
                    pro = i * int(str(j) + str(k) + str(l) + str(m))  # multiply
                    
                    if 1000 < pro < 9999 and (len(list(str(pro))) == len(set(str(pro)))):    # check for digits in multipy is in list
                        try:
                            tem_num6 = tem_num5.copy()
                            for n in map(int, list(str(pro))):
                                tem_num6.remove(n)
                        
                        except:
                            pass
                        
                        else:
                            nums_found.append(pro)         # posible numerbs
                    ###########################
                    
                    ## 2 digit by 3 digit posibilities ##
                    pro = int(str(i) + str(j)) * int(str(k) + str(l) + str(m))  # multiply

                    if 1000 < pro < 9999 and (len(list(str(pro))) == len(set(str(pro)))):    # check for digits in multipy is in list
                        try:
                            tem_num6 = tem_num5.copy()
                            for n in map(int, list(str(pro))):
                                tem_num6.remove(n)
                        
                        except:
                            pass
                        
                        else:
                            nums_found.append(pro)       #posible numbers
                    ###########################

print(sum(set(nums_found)))