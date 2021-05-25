def prime_list_till(prime: int)-> list[int]:
    '''returns list of primes till a given number
    param:prime = last number to check as prime'''
    marked: list[bool] = [0] * (prime + 1)
    value: int = 3

    prime_lst: list[int] = []
    if prime >= 2:
        prime_lst.append(2)

    while value <= prime:
        if marked[value] == 0:
            prime_lst.append(value)
            i = value
            while i < prime:
                marked[i] = 1
                i += value
        value += 2

    return prime_lst


def prime_list_for(prime_for: int)-> list[int]:
    '''returns list of first n prime numbers
    param:prime_for = number of prime numbers return in list'''

    n: int = 0
    while True:
        lst = prime_list_till(100000 + n)
        if len(lst) >= prime_for:
            return lst[:prime_for]
        else:
            n += 100000
            

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization.
    https://en.wikipedia.org/wiki/Primality_test#Python_code"""
    
    if n <= 3:          # only defines for above 3
        return n > 1
    
    if n % 2 == 0 or n % 3 == 0:    # multiples of 2 and 3
        return False
    
    i: int = 5      # for 5
    # coprimes below 25 is divisible by 2 or 3
    while i ** 2 <= n:      # only check till sqrt(i)  6k +-1 <= sqrt(n) (i as 6k-1)
        if n % i == 0 or n % (i + 2) == 0:      # divicable by 6k-1 or 6k + 1 as i is 6k-1 type
            return False

        i += 6
        
    return True


def n_C_r(n: int, r: int)-> int:
    '''returns value of combinations formula'''
    from math import factorial
    return int(factorial(n) / (factorial(n - r) * factorial(r)))


def num_to_word(n: __import__('typing').Union(int, float), spaces:bool=True)-> str:
    '''return word for given number'''
    
    wrd = {
        0:'zero',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelwe',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        20:'twenty',
        30:'thirty',
        40:'forty',
        50:'fifty',
        60:'sixty',
        70:'seventy',
        80:'eighty',
        90:'ninety',

    }
    
    if n > 1000 or n < 0:
        print('not implemented')
        return ''
    elif 20 < n < 30:
        return 'twenty' + num_to_word(n - 20)
    elif 30 < n < 40:
        return 'thirty' + num_to_word(n - 30)
    elif 40 < n < 50:
        return 'forty' + num_to_word(n - 40)
    elif 50 < n < 60:
        return 'fifty' + num_to_word(n - 50)
    elif 60 < n < 70:
        return 'sixty' + num_to_word(n - 60)
    elif 70 < n < 80:
        return 'seventy' + num_to_word(n - 70)
    elif 80 < n < 90:
        return 'eighty' + num_to_word(n - 80)
    elif 90 < n < 100:
        return 'ninety' + num_to_word(n - 90)
    # 100 or n == 200 or n == 300 or n == 400 or n == 500 or n == 600 or n == 700 or n == 800 or n == 900:num_to_word(int(n / 100)) + 'hundred',
    elif n < 1000:
        return num_to_word(int(str(n)[0])) + 'hundred' + 'and' + num_to_word(int(str(n)[1:]))
    else:
        return 'one' + 'thousand'


def triangle(n):
    '''retunrs triange value of the given number'''
    return int(n * (n + 1) / 2)


def reverse_triangle(x):
    '''retuns n value for trangle n'''
    return int((((8 * x + 1) ** 0.5) - 1) / 2)


def divisors(n):
    '''returnd a list of divisors'''
    divisors = []
    for i in range(1, int(n / 2 + 1)):
        if n % i == 0:
            divisors.append(i)
    return divisors


if __name__ == '__main__':
    pass