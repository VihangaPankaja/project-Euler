# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
# by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

file = open('files\p022_names.txt', 'r').read().split('"')
file = file[1:-1]    # remove "" from list

for i in range(file.count(',')):  # remove , from list
    file.remove(',')

file.sort()    # sort alphabaticaly

values = []
for i in file:
    charact = list(i)
    values.append(sum((ord(i) - 64) for i in charact))   # get value for each charactor and add them to list

print(sum(((i + 1) * (values[i])) for i in range(len(values))))  # calculate scores for names and add them