""" 
    By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
    the maximum total from top to bottom is 23.
*      3
*     7 4
*    2 4 6
*   8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

?   Find the maximum total from top to bottom of the triangle below:
*                 75
*                95 64
*               17 47 82
*              18 35 87 10
*             20 04 82 47 65
*            19 01 23 75 03 34
*           88 02 77 73 07 63 67
*          99 65 04 28 06 16 70 92
*         41 41 26 56 83 40 80 70 33
*        41 48 72 33 47 32 37 16 94 29
*       53 71 44 65 25 43 91 52 97 51 14
*      70 11 33 28 77 73 17 78 39 68 17 57
*     91 71 52 38 17 14 91 43 58 50 27 29 48
*    63 66 04 68 89 53 67 30 73 16 69 87 40 31
*   04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE:   As there are only 16384 routes, it is possible to solve this problem by trying every route.
            However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
            it cannot be solved by brute force, and requires a clever method! ;o) 
"""

from typing import NoReturn
import my_math

numbers = '''  75
              95 64
             17 47 82
            18 35 87 10
           20 04 82 47 65
          19 01 23 75 03 34
         88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
       41 41 26 56 83 40 80 70 33
      41 48 72 33 47 32 37 16 94 29
     53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''



def value_for_cordinate(line, position) -> int:
    """ get value for given coordinates at grid

    Args:
    ----
        line ([type]): line NO:
        position ([type]): Possition in line

    Returns:
    ----
        int: [description]
    """
    
    global num_lst
    
    return int(num_lst[my_math.triangle(line-1) + (position-1)])


def maxmum_sum(cur_line: int = 1, currunt_position: int = 1, currunt_sum: int = 0) -> NoReturn:
    """ find sums in every path

    Args:
    ----
        cur_line (int, optional): current line working. Defaults to 1.
        currunt_position (int, optional): current possition in working line. Defaults to 1.
        currunt_sum (int, optional): current sum along path followed. Defaults to 0.
    """
    
    global total_lines, sum_list

    if cur_line == total_lines - 1:                                                                                     # at 2nd last line complete path and calculate sum
        sum_list.append(currunt_sum 
                        + value_for_cordinate(cur_line, currunt_position) 
                        + value_for_cordinate(cur_line+1, currunt_position))
        
        sum_list.append(currunt_sum 
                        + value_for_cordinate(cur_line, currunt_position) 
                        + value_for_cordinate(cur_line+1, currunt_position+1))
        
    else:                                                                                                               # go along possible 2 paths

        maxmum_sum(cur_line + 1, 
                   currunt_position, 
                   currunt_sum + value_for_cordinate(cur_line, currunt_position))
        
        maxmum_sum(cur_line + 1,
                    currunt_position + 1,
                    currunt_sum + value_for_cordinate(cur_line, currunt_position))



if __name__ == '__main__':
    # get numbers as a list
    num_lst: str = numbers.split(' ')
    for i in range(num_lst.count('')):
        num_lst.remove('')
    #############

    for i in range(my_math.reverse_triangle(len(num_lst)) - 1):                                 # itterate for lines - 1 times
        num_lst[my_math.triangle(i+1) - 1] = num_lst[my_math.triangle(i+1) - 1][:-1]            # remove line break(\n) from last vale for every line

    total_lines: int = my_math.reverse_triangle(len(num_lst))
    sum_list: list[int] = []
    
    maxmum_sum()
    
    print(max(sum_list))