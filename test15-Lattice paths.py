# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the
# bottom right corner.

# How many such routes are there through a 20×20 grid?

grid  = int(input('Enter grid size to find paths: '))
lst1 = list(range(1, grid + 2))

for i in range(grid - 2):
    lst2 = []

    for j in range(1, grid + 2):
        lst2.append(sum(lst1[:j]))

    lst1 = lst2


print(sum(lst1))

#### or just use 2nCn function ####
# from my_math import n_C_r
# print(n_C_r(2 * grid,grid))