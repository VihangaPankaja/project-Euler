# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the
# digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # digits used for create numbers
stop = False
number = 0
how_number = int(input('Enter the lexicographic permutations number: '))   # which number to find ascending order


count = 0
def lex_permu(sel_nums = []):
    global count, digits, stop, number
    
    rem_dig = list(i for i in digits if i not in sel_nums)  # list of digits remaing after previous selections

    if len(rem_dig) == 2:           ## selecting last 2 digits
        for i in range(2):          # last 2 digis can store in 2 posible ways
            count += 1              # indexing in number series
            
            if how_number == count:         # check if requested number reached
                stop = True                 # stop looping
                
                if i == 0:                                     # check for what number use for as there are 2 posible numbers in last 2 digits
                    number = (''.join([str(i) for i in (sel_nums + [rem_dig[0], rem_dig[1]])]))   # join digits as a number 
                
                else:
                    number = (''.join([str(i) for i in (sel_nums + [rem_dig[1], rem_dig[0]])]))   # join digits as a number 
                
                break
    
    else:
        for i in rem_dig:  # loop through remaining digits
            if stop:      # check if need to stop
                break
            
            lex_permu(sel_nums + [i])  # choose next set of numbers
lex_permu()


print(number)