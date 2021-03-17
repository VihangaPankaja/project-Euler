# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

tar_val = 200
coins = (1, 2, 5, 10, 20, 50, 100, 200)

posibilities = 0
def pos_count(cur_index=0, cur_tot=0,chs = []):
    global coins, tar_val, posibilities

    coin_count = 0
    while True:
        cur_val = coin_count * coins[cur_index]  #value from currunt type of coin
        
        if cur_val + cur_tot > tar_val:   #check if the currunt combination cannot rech the tearget
            break
        
        elif cur_val + cur_tot == tar_val:  #check if the currunt combination can rech the target
            posibilities +=1
            break
        
        else:
            if cur_index != 7:  #check if not the last item
                pos_count(cur_index + 1, cur_tot + cur_val, chs + [coin_count])  #calling functioon again to choose next type of coin
        
        
        coin_count +=1 #coins selected from currn type of coins increase by 1

pos_count()
print(posibilities)

