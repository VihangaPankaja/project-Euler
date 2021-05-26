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


from typing import Union
def num_to_word(n: Union[int, float, str], spaces:bool=True)-> str:
    '''return word for given number
    for long floating point numbers use string format(after about 17 digits)'''
    
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

    def dec_to_wrd(dec: str, spaces:bool=True)-> str:
        return (' ' if spaces else '').join([wrd[int(digit)] for digit in dec])
            
    def digit_grp_to_str(key: str, val: str, spaces:bool=True)-> str:
        if val == '0':
            return wrd[0]
        
        elif val == '000':
            return ''
        
        else:
            def hundrads(digit: int, spaces:bool=True)-> str: return (' ' if spaces else '').join([wrd[digit], 'hundrad'])
            def tenths(digit: int)-> str: return wrd[digit*10]
            def ones_and_till_nineteen(digit: int)-> str: return wrd[digit]
            
            val = val.rjust(3, '0')
            suffix = suffix_for_digit_grp(key)
            gap = ' ' if spaces else ''
            
            if val[0]!='0' and val[1:]=='00':
                return hundrads(int(val[0]), spaces) + (' 'if suffix!='' and spaces else '') + suffix
            
            elif val[0]!='0':
                if val[1] in ['0', '1']:
                    return hundrads(int(val[0]), spaces) + gap + 'and' + gap + ones_and_till_nineteen(int(val[1:])) + (' 'if suffix!='' and spaces else '') + suffix
                
                else:
                    return hundrads(int(val[0]), spaces) + gap + 'and' + gap + tenths(int(val[1])) + ((('-' if spaces else '') + ones_and_till_nineteen(int(val[-1]))) if val[-1]!='0' else '') + (' 'if suffix!='' and spaces else '') + suffix
                
            else:
                if val[1] in ['0', '1']:
                    return ones_and_till_nineteen(int(val[1:])) + (' 'if suffix!='' and spaces else '') + suffix
                
                else:
                    return tenths(int(val[1])) + ((('-' if spaces else '') + ones_and_till_nineteen(int(val[-1]))) if val[-1]!='0' else '') + (' 'if suffix!='' and spaces else '') + suffix
            
    
    def suffix_for_digit_grp(key: str)-> str:
        pow = int(key[2:])
        
        if pow == 0:
            return ''
        
        elif 3 <= pow <= 33 or (pow <= 303 and (pow-33)%30==0):
            return wrd[key] + ','
        
        elif 33 < pow < 303:
            return wrd[f'e+(x+{(pow-33)%30})'] + wrd[f'e+{((pow-33)//30)*30 + 33}'] + ','
        
        elif pow > 303:
            return f'{100 + int((pow - 303)/3)}-illon,'
        
          
    if type(n) == int:
        n = str(n)
        ### group to 3 digit classes ###
        quo, rem = len(n)//3, len(n)%3
        
        digit_grps = {f'e+{quo*3}':n[:-quo*3]} if rem != 0 else {}
        digit_grps.update({f'e+{(i - 1) * 3}' : n[(-i * 3) : (-i * 3 + 3) if (-i * 3 + 3) != 0 else None] for i in range(quo, 0, -1)})
        
        if len(n) < 3:
            digit_grps = {'e+0':n}
        ###################################
        
        num_name = (' ' if spaces else '').join([digit_grp_to_str(key, val, spaces) for key, val in digit_grps.items()])
        
        return num_name[:-1] if num_name[-1] == ',' else num_name
    
    elif type(n) == float:
        whole_part, decimal_part = str(n).split('.')

        return num_to_word(int(whole_part), spaces) + (' ' if spaces else '') + 'point' + (' ' if spaces else '') + dec_to_wrd(decimal_part, spaces)
    
    elif type(n) == str:
        if '.' in n:
            whole_part, decimal_part = n.split('.')
            
            return num_to_word(int(whole_part), spaces) + (' ' if spaces else '') + 'point' + (' ' if spaces else '') + dec_to_wrd(decimal_part, spaces)
        
        else:
            return num_to_word(int(n), spaces)
            
    else:
        return 'wrong data type'


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