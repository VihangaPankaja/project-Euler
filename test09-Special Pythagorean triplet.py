# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

sum_of_all = int(input('Enter a+b+c value: '))  # a+b+c

loop = True
for b in range(1, (int(sum_of_all // 2) + 1)):   # a    ## possible a,b 's
    for a in range(1, b + 1):                                             ##
        if a ** 2 + b ** 2 == (sum_of_all - a - b) ** 2:   # c = sum -a-b then a^2 + b^2 = (sum -a-b)^2
            lst = [a, b, (sum_of_all - a - b)]
            
            loop = False
            break
    
    if not loop:
        break

try:
    print(lst[0] * lst[1] * lst[2])
except:
    print('no values maching')