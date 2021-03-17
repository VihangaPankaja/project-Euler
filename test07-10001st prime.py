#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?


from math import sqrt

prime_no = int(input('Enter the prime number you want to fimd: '))
prime_count = 0
cur_num = 1
last_prime = 0


while prime_count < prime_no:
    cur_num += 1
    
    for i in range(2, (int(sqrt(cur_num))+ 1)):
        if cur_num % i == 0 : break
    
    else:
        prime_count += 1
        last_prime = cur_num


print(last_prime)

## alternative #####################
from my_math import prime_list_for

print(prime_list_for(prime_no)[-1])
####################################