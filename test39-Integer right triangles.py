""" 
  If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
  there are exactly three solutions for p = 120.
*   {20,48,52}, {24,45,51}, {30,40,50}
  
? For which value of p ≤ 1000, is the number of solutions maximised
"""


def max_solutions(p_max: int)-> int:
    solutions: dict[int : list[set[int]]] = {x:[] for x in range(1, p_max+1)}  # p as key and solutions list


    """ 
    𝑎,𝑏,𝑐 ∈ ℤ , 𝑚 > 𝑛 > 0 ∈ ℤ ,  𝑘 ∈ ℤ
        𝑎² + 𝑏² = 𝑐²
        𝑎 = 𝑘(𝑚² - 𝑛²)
        𝑏 = 𝑘(2𝑚𝑛)
        𝑐 = 𝑘(𝑚² + 𝑛²)
    """
    for n in range(1, (p_max+1)):
        for m in range(n+1, (p_max+1)):

            a0: int = m**2 - n**2
            b0: int = 2 * m * n
            c0: int = m**2 + n**2
            k: int = 1
            
            
            while True:

                a: int = k * a0
                b: int = k * b0
                c: int = k * c0
                p: int = a + b + c
                
                
                if p <= p_max:
                    tripple: set[int] = {a, b, c}     # sets not permutate
                    
                    if tripple not in solutions[p]:
                        solutions[p].append(tripple)
                        
                else:
                    break
                k += 1

    return max(solutions, key=lambda x: len(solutions.get(x)))    # return what key have maximum solutions



if __name__ == '__main__':
    print(max_solutions(1000))