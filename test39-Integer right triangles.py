# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?


def max_solutions(p_max: int):
    solutions = {x:[] for x in range(1, p_max+1)}  # p as key and solutions list


    # a,b,c    a**2+b**2 = c**2    
    # m>n>0 in Z   k in Z
    # a = k(m**2 - n**2)
    # b = k(2mn)
    # c = k(m**2 + n**2)
    for n in range(1, (p_max+1)):
        for m in range(n+1, (p_max+1)):

            a0 = m**2 - n**2
            b0 = 2 * m * n
            c0 = m**2 + n**2
            k = 1
            
            
            while True:

                a = k * a0
                b = k * b0
                c = k * c0
                p = a + b + c
                
                
                if p <= p_max:
                    tripple = {a, b, c}     # sets not permutate
                    
                    if tripple not in solutions[p]:
                        solutions[p].append(tripple)
                        
                else:
                    break
                k += 1

    return (max(solutions, key=lambda x: len(solutions.get(x))))    # return what key have maximum solutions



if __name__ == '__main__':
    print(max_solutions(1000))