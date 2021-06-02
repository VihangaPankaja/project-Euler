"""
  The Fibonacci sequence is defined by the recurrence relation:
  
  Fₙ = Fₙ₋₁ + Fₙ₋₂, where F₁ = 1 and F₂ = 1.
  
  Hence the first 12 terms will be:
*   F₁  = 1
*   F₂  = 1
*   F₃  = 2
*   F₄  = 3
*   F₅  = 5
*   F₆  = 8
*   F₇  = 13
*   F₈  = 21
*   F₉  = 34
*   F₁₀ = 55
*   F₁₁ = 89
*   F₁₂ = 144
  The 12ᵗʰ term, F₁₂, is the first term to contain three digits.
  
? What is the index of the first term in the Fibonacci sequence to contain 1000 digits
"""

def fib_digits(digits_in_num: int)-> int:
    """ get term number for given digits for fibonacci number """
    
    fib_num = [1, 1]  # fibanachi series with first 2 numbers

    while True:
        fib_num.append(fib_num[-1] + fib_num[-2])   # find next nuber in series
        if len(str(fib_num[-1])) == digits_in_num:  # check dgits in number satisfies
            break
        
    return len(fib_num)


if __name__ == '__main__':
    print(fib_digits(1000))      # print 𝑛 of Fₙ which satisfies 