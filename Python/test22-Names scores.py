"""
  Using names.txt, a 46K text file containing over five-thousand first names,
  
  begin by sorting it into alphabetical order. 
  Then working out the alphabetical value for each name, 
  multiply this value by its alphabetical position in the list to obtain a name score.

  For example, when the list is sorted into alphabetical order, 
*     COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
*     is the 938th name in the list. So, 
*     COLIN would obtain a score of 938 × 53 = 49714.

? What is the total of all the name scores in the file
"""


def sum_score_for_names() -> list[int]:
    with open('files\p022_names.txt', 'r', encoding='utf-8') as file:
        file = [x for x in file.read().split('"') if x not in ['"', ',']]  # get names from file
        file.sort()    # sort alphabaticaly


        values: list[int] = []
        for i in file:
            charact: str = list(i)
            values.append(sum((ord(i) - 64) for i in charact))   # get value for each charactor and add them to list

    return sum(((i+1) * (values[i])) 
                    for i in range(len(values)))  # calculate scores for names and add them


if __name__ == '__main__':
    print(sum_score_for_names())