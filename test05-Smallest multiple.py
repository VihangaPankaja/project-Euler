# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

getnum = int(input('Enter ther number to find number that divisabe by all numbers till: '))
cur_num = getnum

for i in range(1, (getnum + 1)):
    if cur_num % i == 0:         # check the number divicable by the number curruntly checking
        continue
    
    for j in range(2, (i + 1)):   # check number multily by 2 to currunt check if that divicable
        if (cur_num * j) % i == 0:
            cur_num *= j
            
            break


print(cur_num)