# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?


solutions = [0] * 1001


# a,b,c    a**2+b**2 = c**2    
# m>n>0 in Z   k in Z
# a = k(m**2 - n**2)
# b = k(2mn)
# c = k(m**2 + n**2)
for n in range(1, 1001):
    for m in range(n+1, 1001):
        a0 = m**2 - n**2
        b0 = 2 * m * n
        c0 = m**2 + n**2
        k = 1
        while True:
            a = k * a0
            b = k * b0
            c = k * c0
            p = a + b + c
            if p <= 1000:
                pass
            k += 1