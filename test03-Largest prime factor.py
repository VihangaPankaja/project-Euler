#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

num = 600851475143

tempnum = num
lastnum = 2
lrgfact = 1

while tempnum > lastnum:
    for i in range(lastnum, int(tempnum + 1)) :  # check for divicable numbers, strat from last divicable number
        if tempnum % i == 0:  # if ivicable
            if i > lrgfact:   # if currunt factor larger than previous one
                lrgfact = i
            
            tempnum /= i  # other factor
            lastnum = i
            
            break   # run untill there are no facr0ts

if tempnum > lrgfact:
    lrgfact = tempnum


print(lrgfact)
