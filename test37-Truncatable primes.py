# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage:
# 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


def is_prime(n: int)-> int:
    '''return if prime or not'''

    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            break
    else:
        return True
    
    return False



def main():
    trunctable: list[int] = []
    lst_digits: list[int] = [2, 3, 5, 7]

    n = 10
    while True:
        if len(trunctable) == 11:  # there is only 11 trunctables
            break

        elif (int(str(n)[0]) not in lst_digits) or (int(str(n)[-1]) not in lst_digits):   #firs an last digit should be a prime. to save proccesing
            pass

        elif n < 100:
            if is_prime(n):
                trunctable.append(n)

        else:
            if is_prime(n):
                for i in range(len(str(n)) - 2):
                    if not (is_prime(int(str(n)[:i + 2])) and is_prime(int(str(n)[i + 1:]))):      # going right to left and left to right and check if not prime
                        break
                else:
                    trunctable.append(n)        # add to list if all not prime checks failed

        n += 1
        
    return trunctable

if __name__ == '__main__':
    print(sum(main()))