""" 
    An irrational decimal fraction is created by concatenating the positive integers:
*       0.123456789101112131415161718192021...

    It can be seen that the 12ᵗʰ digit of the fractional part is 1.
  
    If 𝑑ₙ represents the 𝑛ᵗʰ digit of the fractional part, find the value of the following expression.
?   𝑑₁ × 𝑑₁₀ × 𝑑₁₀₀ × 𝑑₁₀₀₀ × 𝑑₁₀₀₀₀ × 𝑑₁₀₀₀₀₀ × 𝑑₁₀₀₀₀₀₀
"""



def d_n(n: int) -> int:
    """ find 𝑛ᵗʰ digit of concatenated number

    Args:
    ----
        n (int): 𝑛ᵗʰ digit

    Returns:
    ----
        int: 
    """
    
    if n <= 0:
        return None
    
    elif 1 <= n <= 9:
        return n
    
    else:
        last_digit: int = 9
        power: int = 1       # 10ᵗʰ power (digits in decimal number)

        while True:
            if ((last_digit+1) <= n <= (last_digit + (power+1) 
                                            * (10 ** (power+1) - 10**power))):    # digits in decimal number
                
                n -= last_digit    # remove nth digits till previous digit

                num = ((10**power -1) + ( (n // (power+1) + 1) 
                                         if n % (power+1) != 0 
                                         else (n // (power+1)) ))   # select number in 𝑛ᵗʰ digit
                ######{last num of   ###{ quotient + 1}#########{remainder is 0 }#######{   quotient   }####
                ######previous digit}#######################################################################
                ## eg: 10 -> 10-9=1 -> quo=0 rem=1
                ##     11 -> 11-9=2 -> quo=1 rem=0
                
                return int(str(num)[n%(power + 1) - 1])   # return required digit from selected number 
            
            else:
                last_digit += (power + 1) * (10**(power + 1) - 10**power)   # concatinated digits for current number of digits
                power += 1      # next 10th power
    

if __name__ == '__main__':
    print(d_n(1) 
          * d_n(10) 
          * d_n(100) 
          * d_n(1_000) 
          * d_n(10_000) 
          * d_n(100_000) 
          * d_n(1_000_000))