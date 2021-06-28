""" 
    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
 *      ┏━━━━┱────┬────┬────┲━━━━┓
 *      ┃ 21 ┃ 22 │ 23 │ 24 ┃ 25 ┃
 *      ┡━━━━╋━━━━╅────╆━━━━╋━━━━┩
 *      │ 20 ┃  7 ┃  8 ┃  9 ┃ 10 │
 *      ├────╄━━━━╋━━━━╋━━━━╃────┤
 *      │ 19 │  6 ┃  1 ┃  2 │ 11 │
 *      ├────╆━━━━╋━━━━╋━━━━╅────┤
 *      │ 18 ┃  5 ┃  4 ┃  3 ┃ 12 │
 *      ┢━━━━╋━━━━╃────╄━━━━╋━━━━┪
 *      ┃ 17 ┃ 16 │ 15 │ 14 ┃ 13 ┃
 *      ┗━━━━┹────┴────┴────┺━━━━┛
  
    It can be verified that the sum of the numbers on the diagonals is 101.
  
?   What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way
"""

# yeah i could've used annonymous functions 😁
def f_lef_up(n: int) -> int: return (2*n + 1)**2 - (2*n)       # values for left up direction from middle


def f_lef_down(n: int) -> int: return (2*n + 1)**2 - (4*n)     # values for left down direction from middle


def f_right_up(n: int) -> int: return (2*n + 1)**2             # values for right up direction from middle


def f_right_down(n: int) -> int: return (2*n + 1)**2 - (6*n)   # values for right down direction from middle


def sum_of_diagonal_numbers(grid: int) -> int:
    return sum([1, 
                sum(f_lef_up(n) for n in range(1, int(grid/2) + 1)),
                sum(f_lef_down(n) for n in range(1, int(grid/2) + 1)),
                sum(f_right_up(n) for n in range(1, int(grid/2) + 1)),
                sum(f_right_down(n) for n in range(1, int(grid/2) + 1))
            ])
    
    
if __name__ == '__main__':
    print(sum_of_diagonal_numbers(1_001))