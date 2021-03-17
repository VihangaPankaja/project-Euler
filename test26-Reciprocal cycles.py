# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

max_d = 1000  # max d checking for 1/d
cyc_lenths = [] # list of number of recurring digits for given number


## returns number of rucurring digits for 1/d for given d ##
def cycle_lenth(d):
    remainig = [1]   # because 1/
    while True:
        remainig.append((remainig[-1] * 10) % d)    ## remaing from dividing

        if remainig[-1] == 0:                       # check if 1/d has no recurring digits
            return 0

        elif remainig[-1] in remainig[:-1]:        ## check for recurring cycle completed
            return len(remainig) - remainig.index(remainig[-1]) - 1
#####################################


for d in range(1, max_d):
    cyc_lenths.append(cycle_lenth(d))


print(cyc_lenths.index(max(cyc_lenths)) + 1)  # find dthat has max recurring digit cycle
