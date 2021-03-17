def prime_list_till(prime):
    '''returns list of primes till a given number
    param:prime = last number to check as prime'''
    marked = [0] * prime
    value = 3

    prime_lst = []
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


def prime_list_for(prime_for):
    '''returns list of first n prime numbers
    param:prime_for = number of prime numbers return in list'''
    n = 0
    while True:
        lst = prime_list_till(100000 + n)
        if len(lst) >= prime_for:
            return lst[:prime_for]
        else:
            n += 100000


def n_C_r(n, r):
    '''returns value of combinations formula'''
    from math import factorial
    return int(factorial(n) / (factorial(n - r) * factorial(r)))


def num_to_word(n):
    '''return word for given number without spaces'''
    if n > 1000 or n < 0:
        print('out of range')
        return ''
    elif n == 0:
        return 'zero'
    elif n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelwe'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'
    elif n == 20:
        return 'twenty'
    elif 20 < n < 30:
        return 'twenty' + num_to_word(n - 20)
    elif n == 30:
        return 'thirty'
    elif 30 < n < 40:
        return 'thirty' + num_to_word(n - 30)
    elif n == 40:
        return 'forty'
    elif 40 < n < 50:
        return 'forty' + num_to_word(n - 40)
    elif n == 50:
        return 'fifty'
    elif 50 < n < 60:
        return 'fifty' + num_to_word(n - 50)
    elif n == 60:
        return 'sixty'
    elif 60 < n < 70:
        return 'sixty' + num_to_word(n - 60)
    elif n == 70:
        return 'seventy'
    elif 70 < n < 80:
        return 'seventy' + num_to_word(n - 70)
    elif n == 80:
        return 'eighty'
    elif 80 < n < 90:
        return 'eighty' + num_to_word(n - 80)
    elif n == 90:
        return 'ninety'
    elif 90 < n < 100:
        return 'ninety' + num_to_word(n - 90)
    elif n == 100 or n == 200 or n == 300 or n == 400 or n == 500 or n == 600 or n == 700 or n == 800 or n == 900:
        return num_to_word(int(n / 100)) + 'hundred'
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
