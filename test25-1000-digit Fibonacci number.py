# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fib_digits(digits_in_num: int)-> int:
    """ get term number for given digits for fibonacci number """
    
    fib_num = [1, 1]  # fibanachi series with first 2 numbers

    while True:
        fib_num.append(fib_num[-1] + fib_num[-2])   # find next nuber in series
        if len(str(fib_num[-1])) == digits_in_num:  # check dgits in number satisfies
            break
        
    return len(fib_num)


if __name__ == '__main__':
    print(fib_digits(1000))      # print n of Fn which satisfies 