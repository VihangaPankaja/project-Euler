###########################################################################
def prime_list_till(prime: int) -> list[int]:
    '''
    returns list of primes till a given number
        Parameters:
            prime (int) last number to check as prime
    '''

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


def primes(n: int) -> list[int]:
    """ Returns  a list of primes < n 
    excec time about 78.9  ms for 1mil"""
    
    sieve = [True] * n
    
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i :: 2*i] = [False] * ((n - i*i - 1)//(2*i) + 1)
            
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def primes1(n) -> list[int]:
    """ Returns  a list of primes < n 
    excec time about 76.1  ms for 1mil"""
    
    sieve = [True] * (n//2)
    
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i // 2 :: i] = [False] * ((n - i*i - 1)//(2*i) + 1)
            
    return [2] + [2*i + 1 for i in range(1, n//2) if sieve[i]]


def primes2(n) -> list[int]:
    """ Input n>=6, Returns a list of primes, 2 <= p < n 
    excec time about 57.9  ms for 1mil"""
    n, correction = n - n%6 + 6, 2 - (n%6 > 1)
    sieve = [True] * (n//3)
    
    for i in range(1,int(n**0.5)//3 + 1):
      if sieve[i]:
        k = 3*i + 1 | 1
        sieve[(k*k//3) :: 2*k] = [False] * ((n//6 - k*k//6 - 1)//k + 1)
        sieve[(k*(k - 2*(i & 1) + 4) // 3) :: 2*k] = [False] * ((n//6 - k*(k -2*(i & 1) + 4)//6 -1)//k + 1)
        
    return ([2, 3] + [(3*i + 1 | 1) for i in range(1, n//3 - correction) if sieve[i]])


import numpy
def primesfrom2to(n) -> numpy.ndarray:
    """ Input n>=6, Returns a array of primes, 2 <= p < n 
    excec time about 3.71  ms for 1mil"""
    
    sieve = numpy.ones(n//3 + (n%6 == 2), dtype=numpy.bool_)
    
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k = (3*i + 1) | 1
            sieve[(k*k // 3) :: 2*k] = False
            sieve[(k*(k - 2*(i & 1) + 4) // 3) :: 2*k] = False
            
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


def primesfrom3to(n) -> numpy.ndarray:
    """ Returns a array of primes, 3 <= p < n 
    excec time about 3.95 ms for 1mil"""
    
    sieve = numpy.ones(n//2, dtype=numpy.bool_)
    
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[(i*i // 2) :: i] = False
            
    return 2 * numpy.nonzero(sieve)[0][1::] + 1


def get_primes_erat(n) -> list[int]:
    """ excec time about 596 ms for 1mil """
    import itertools
    
    def erat2( ):
        D = {  }
        yield 2
        for q in itertools.islice(itertools.count(3), 0, None, 2):
            p = D.pop(q, None)
            if p is None:
                D[q*q] = q
                yield q
            else:
                x = p + q
                while x in D or not (x&1):
                    x += p
                D[x] = p
                
    return list(itertools.takewhile(lambda p: p<n, erat2()))


def prime_list_for(prime_for: int) -> list[int]:
    '''
    returns list of first n prime numbers
        parameters:
            prime_for (int) number of prime numbers return in list
    '''

    n: int = 0
    while True:
        lst = prime_list_till(100000 + n)
        if len(lst) >= prime_for:
            return lst[:prime_for]
        else:
            n += 100000
            

##############################################################################

from typing import Generator
def prime_gen(recursionLimit: int = 1_000_000)-> Generator[int, None, None]:
    """
    generates primes numbers on demand 
     set recursion limit to higher number if recursion depth exceeds exception occured
        default limit is 1_000_000
    ! not working very well because of lot of recursions and generators
    """

    import sys
    sys.setrecursionlimit(recursionLimit)
    def nats(n):
        """ generates integers from given point """
        while True:
            yield n
            n += 1
        
    def sieve(s):
        n = next(s)
        yield n
        yield from sieve(i for i in s if i%n!=0)
    
    return sieve(nats(2))


def is_prime(n: int) -> bool:
    """Primality test using 6𝑘 ± 1 optimization.
    https://en.wikipedia.org/wiki/Primality_test#Python_code"""
    
    if n <= 3:          # only defines for above 3
        return n > 1
    
    if n % 2 == 0 or n % 3 == 0:    # multiples of 2 and 3
        return False
    
    i: int = 5      # for 5
    # coprimes below 25 is divisible by 2 or 3
    while i ** 2 <= n:      # only check till √̅𝑖  6𝑘 ± 1 <= √̅𝑛 (i as 6𝑘-1)
        if n % i == 0 or n % (i + 2) == 0:      # divicable by 6𝑘-1 or 6𝑘 + 1 as 𝑖 is 6𝑘-1 type
            return False

        i += 6
        
    return True


def n_C_r(n: int, r: int) -> int:
    '''
    returns value of combinations formula
    '''

    from math import factorial
    return int(factorial(n) / (factorial(n - r) * factorial(r)))


from typing import Union
def num_to_word(n: Union[int, float, str], spaces:bool=True) -> str:
    '''
    return word for given number
    for long floating point numbers use string format(after about 17 digits)
    '''
    
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
        'e+3':'thousand',
        'e+6':'million',
        'e+9':'billion',
        'e+12':'trillion',
        'e+15':'quardillion',
        'e+18':'quintillion',
        'e+21':'sextillion',
        'e+24':'septillion',
        'e+27':'octillion',
        'e+30':'nonillion',
        'e+33':'decillion',
        'e+63':'vigintillion',
        'e+93':'trigintillion',
        'e+123':'quadragintillion',
        'e+153':'quinquagintillion',
        'e+183':'sexagintillion',
        'e+213':'septuagintillion',
        'e+243':'octogintillion',
        'e+273':'nonagintillion',
        'e+303':'centillion',
        'e+(x+3)':'un',
        'e+(x+6)':'duo',
        'e+(x+9)':'tre',
        'e+(x+12)':'quattour',
        'e+(x+15)':'quin',
        'e+(x+18)':'sex',
        'e+(x+21)':'septen',
        'e+(x+24)':'octo',
        'e+(x+27)':'novem',
    }

    def dec_to_wrd(dec: str, spaces:bool=True) -> str:
        """ return words for digits after decimal place """
        return (' ' if spaces else '').join([wrd[int(digit)] for digit in dec])
            
    def digit_grp_to_str(key: str, val: str, spaces:bool=True) -> str:
        """ returns name for 3 digit group with suffix appended """
        
        if val == '0':  # zero point number
            return wrd[0]
        
        elif val == '000':  # no value in given digit group
            return ''
        
        else:
            def hundrads(digit: int, spaces:bool=True)-> str: return (' ' if spaces else '').join([wrd[digit], 'hundrad'])  # str for 100 multiplications
            def tenths(digit: int)-> str: return wrd[digit*10]      # str for 10 multiplications after 20
            def ones_and_till_nineteen(digit: int)-> str: return wrd[digit]     # str for 1 to 19
            
            val = val.rjust(3, '0')             # if not have 3 digits
            suffix = suffix_for_digit_grp(key)  # suffix for digit group
            gap = ' ' if spaces else ''         # spaces
            
            if val[0]!='0' and val[1:]=='00':       # multiplications of 100
                return ''.join([
                        hundrads(int(val[0]), spaces),
                        (' 'if suffix!='' and spaces else ''),
                        suffix
                    ])
            
            elif val[0]!='0':   # values above 100
                
                if val[1] in ['0', '1']:    # values above 100 and last 2 digits between 1 and 19
                    return ''.join([
                            hundrads(int(val[0]), spaces),
                            gap,
                            'and',
                            gap,
                            ones_and_till_nineteen(int(val[1:])),
                            (' 'if suffix!='' and spaces else ''),
                            suffix
                        ])
                
                else:                       # values above 100 and last 2 digits between 20 and 99
                    return ''.join([
                            hundrads(int(val[0]), spaces),
                            gap,
                            'and', 
                            gap,
                            tenths(int(val[1])),
                            ((('-' if spaces else '') + ones_and_till_nineteen(int(val[-1]))) if val[-1]!='0' else ''),
                            (' 'if suffix!='' and spaces else ''),
                            suffix
                        ])
                
            else:       # value under 100
                if val[1] in ['0', '1']:    # value between 1 and 19
                    return ''.join([
                            ones_and_till_nineteen(int(val[1:])),
                            (' 'if suffix!='' and spaces else ''),
                            suffix
                        ])
                
                else:       # value between 20 and 99
                    return ''.join([
                            tenths(int(val[1])),
                            ((('-' if spaces else '') + ones_and_till_nineteen(int(val[-1]))) if val[-1]!='0' else ''),
                            (' 'if suffix!='' and spaces else ''),
                            suffix
                        ])
            
    def suffix_for_digit_grp(key: str) -> str:
        """ suffix for thousand digit groups """

        pow = int(key[2:])
        
        if pow == 0:    # under 1000
            return ''
        
        elif 3 <= pow <= 33 or (pow <= 303 and (pow-33)%30==0):     # thousand to dectillion
            return wrd[key] + ','
        
        elif 33 < pow < 303:        # dectillion to centillion
            return wrd[f'e+(x+{(pow-33)%30})'] + wrd[f'e+{((pow-33)//30)*30 + 33}'] + ','
        
        elif pow > 303:             # above centillion
            return f'{100 + int((pow - 303)/3)}-illon,'
        
          
    if type(n) == int:  # integer n
        n = str(n)
        ### group to 3 digit classes ###
        quo, rem = len(n)//3, len(n)%3
        
        digit_grps = {f'e+{quo*3}':n[:-quo*3]} if rem != 0 else {}
        digit_grps.update({f'e+{(i - 1) * 3}' : n[(-i * 3) : (-i * 3 + 3) if (-i * 3 + 3) != 0 else None] for i in range(quo, 0, -1)})
        
        if len(n) < 3:
            digit_grps = {'e+0':n}
        ###################################
        
        num_name = (' ' if spaces else '').join([digit_grp_to_str(key, val, spaces) for key, val in digit_grps.items()])    # name for given integer
        
        return num_name[:-1] if num_name[-1] == ',' else num_name   # if last character is ',' then remove it
    
    elif type(n) == float:  # float n
        whole_part, decimal_part = str(n).split('.')    # separate from decimal point

        return num_to_word(int(whole_part), spaces) + (' ' if spaces else '') + 'point' + (' ' if spaces else '') + dec_to_wrd(decimal_part, spaces)
    
    elif type(n) == str:    # string n
        if '.' in n:    # if has a decimal point
            whole_part, decimal_part = n.split('.') # separate from decimal point
            
            return num_to_word(int(whole_part), spaces) + (' ' if spaces else '') + 'point' + (' ' if spaces else '') + dec_to_wrd(decimal_part, spaces)
        
        else:   # no decimal point
            return num_to_word(int(n), spaces)
            
    else:
        return 'wrong data type'


def triangle(n) -> int:
    '''retunrs triange value of the given number'''
    return int(n * (n+1) / 2)


def reverse_triangle(x) -> int:
    '''retuns n value for trangle n'''
    return int((((8*x + 1)**0.5) - 1) / 2)


def divisors(n) -> list[int]:
    '''returnd a list of divisors'''
    divisors = []
    for i in range(1, int(n / 2 + 1)):
        if n % i == 0:
            divisors.append(i)
    return divisors


if __name__ == '__main__':
    pass