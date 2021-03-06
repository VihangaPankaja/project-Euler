"""
    Starting in the top left corner of a 2×2 grid, 
    and only being able to move to the right and down,
    there are exactly 6 routes to the
    bottom right corner.
  
*   ┍━┯━┓  ┍━┱─┐  ┍━┱─┐
*   ├─┼─┨  ├─╄━┪  ├─╂─┤
*   └─┴─┚  └─┴─┚  └─┺━┙
*   ┎─┬─┐  ┎─┬─┐  ┎─┬─┐          
*   ┠─┼─┤  ┡━╅─┤  ┡━┿━┪
*   ┗━┷━┙  └─┺━┙  └─┴─┚

?   How many such routes are there through a 20×20 grid
"""


def grid_paths(grid: int) -> list[int]:
    """ find how many grid paths for given grid size

    Args:
    ----
        grid (int): grid size of one side

    Returns:
    ----
        list[int]:
    """
    
    lst1 = list(range(1, grid+2))

    for _ in range(grid - 2):
        lst2 = []

        for j in range(1, grid+2):
            lst2.append(sum(lst1[:j]))

        lst1 = lst2
        
    return lst1


#### or just use 2nCn function ####
def easy_grid_path(grid: int) -> int:
    from my_math import n_C_r
    
    return n_C_r(2*grid, grid)
###################################


if __name__ == '__main__':
    print(sum(grid_paths(20)))
    # print(easy_grid_path(20))