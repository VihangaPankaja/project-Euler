"""
  A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
* a² + b² = c²

  For example, 
* 3² + 4² = 9 + 16 = 25 = 5²

  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
? Find the product abc
"""

from typing import Union


def prod_of_py_trplle(trpple_sum: int) -> Union[int,str]:
    loop: bool = True
    for b in range(1, (int(trpple_sum//2) + 1)):   # a    ## possible a,b 's
        for a in range(1, b+1):                                             ##
            if a**2 + b**2 == (trpple_sum - a - b)**2:   # c = sum -a-b then a² + b² = (sum -a-b)²
                lst = [a, b, (trpple_sum - a - b)]

                loop = False
                break

        if not loop:
            break

    try:
        return (lst[0] * lst[1] * lst[2])
    except:
        return 'no values maching'



if __name__ == '__main__':
    print(prod_of_py_trplle(1_000))