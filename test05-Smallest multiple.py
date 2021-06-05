""" 
  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

? What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
"""


def smallest_divisible(num: int)-> int:
    """ returns smallest positive number that is evenly divisible by all of the numbers from 1 to num """
    
    cur_num: int= num

    for i in range(1, (num + 1)):
        if cur_num % i == 0:         # check the number divicable by the number curruntly checking
            continue

        for j in range(2, (i + 1)):   # check number multily by 2 to currunt check if that divicable
            if (cur_num * j) % i == 0:
                cur_num *= j
                break
            
    return cur_num


if __name__ == '__main__':
    print(smallest_divisible(20))