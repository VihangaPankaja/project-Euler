# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


def is_pendigital(n: int)-> bool:
    '''check if a number use all 1 to 9 digits once'''

    digits = list(range(1, 10))
    try:
        for i in str(n):           # check for pandigital
            digits.remove(int(i))

    except:
        pass
    
    else:
        if len(digits) == 0:    # if pandigital
            return True
    
    return False


def concatenate(n):
    '''generate concatenated product of n and (1, 2, 3, ....) till 9 digits'''

    num_gented = ''
    for i in range(1, 10):
        num_gented += str(n * i)     # concatenate products

        if len(num_gented) == 9:     # can generate 9 digits
            return int(num_gented)
        
        elif len(num_gented) > 9:    # cannot generate 9 digits
            return False

            
if __name__ == '__main__':
    numerbs = []
    for i in range(10_000):                              # last number can get 9 digits like this is 9999 (4 and 5 digits)
        if is_pendigital(concatenate(i)):
            numerbs.append((i, concatenate(i)))

    print(max(list(y for x, y in numerbs)))               # find biggest pandigital number
