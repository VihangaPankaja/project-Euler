"""
    In the United Kingdom the currency is made up of pound (£) and pence (p). 
  
    There are eight coins in general circulation:
*       1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

    It is possible to make £2 in the following way:  
        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    
?   How many different ways can £2 be made using any number of coins?
"""


def pos_count(cur_index: int = 0, cur_tot: int = 0,chs: list[int] = []) -> int:
    """ find all possibilities of coins combinations for a given value

    Args:
    ----
        cur_index (int, optional): selected coin. Defaults to 0.
        cur_tot (int, optional): current total. Defaults to 0.
        chs (list[int], optional): previously found possibilities. Defaults to [].

    Returns:
    ----
        int:
    """
    
    global coins, tar_val, possibilities

    coin_count: int = 0
    while True:
        cur_val = coin_count * coins[cur_index]  #value from currunt type of coin
        
        if cur_val + cur_tot > tar_val:   #check if the currunt combination cannot reach the tearget
            return
        
        elif cur_val + cur_tot == tar_val:  #check if the currunt combination can reach the target
            possibilities +=1
            
            return possibilities
        
        else:
            if cur_index != 7:  #check if not the last item
                pos_count(cur_index + 1, 
                          cur_tot + cur_val, 
                          chs + [coin_count])  #calling function again to choose next type of coin
        
        
        coin_count +=1 #coins selected from current type of coins increase by 1


if __name__ == '__main__':
    tar_val: int = 200
    coins: tuple[int] = (1, 2, 5, 10, 20, 50, 100, 200)
    possibilities: int = 0
    
    print(pos_count())