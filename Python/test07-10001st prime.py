""" 
  By listing the first six prime numbers: 
*   2, 3, 5, 7, 11, and 13, 
    we can see that the 6th prime is 13.

? What is the 10 001st prime number 
"""



def nth_prime(prime_no: int) -> int:
    from math import sqrt

    prime_count: int = 0
    cur_num: int = 1

    while prime_count < prime_no:
        cur_num += 1
        
        for i in range(2, (int(sqrt(cur_num))+ 1)):   # only check for factors till sqrt
            if cur_num % i == 0 : break               # if not prime
        
        else:                       # if prime
            prime_count += 1
            last_prime = cur_num

    return last_prime


## alternative #####################
def alternative(prime_no: int) -> int:
    from my_math import prime_list_for

    return (prime_list_for(prime_no)[-1])
####################################


if __name__ == '__main__':
    print(nth_prime(10_001))
    # print(alternative(10_001))