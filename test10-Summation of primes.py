"""
  The sum of the primes below 10 is 
* 2 + 3 + 5 + 7 = 17.

? Find the sum of all the primes below two million.
"""


def prime_lst_till(number_range: int)-> list[int]:
    """ generates prime list till given number """
    
    from math import sqrt

    prime_list = [2]

    for i in range(3, number_range):

        temp_list = []
        for j in prime_list:
            temp_list.append(j)

            if j > sqrt(i):  # don't need to check numbers more then sqrt
                break

        for j in temp_list:
            if i % j == 0: # not prime
                break
        else:
            prime_list.append(i) # prime
            
    return prime_list



######fastest method found#######
def sum_of_primes_till(number_range: int)-> int:
    marked = [0] * number_range       # create check box for each number
    value = 3                    # currunt checking value
    s = 2                        # total of primes

    while value < number_range:
        if marked[value] == 0:     # 0 means prime
            s += value             # add prime value to total
            i = value              # currunt prime

            while i < number_range:     # mark multiplications of currunt prime as not prime
                marked[i] = 1
                i += value

        value += 2                 # check only for odd numbers

    return s
##################################
    
    
    
if __name__ == '__main__':
    # print(sum(prime_lst_till(2_000_000)))
    print(sum_of_primes_till(2_000_000))