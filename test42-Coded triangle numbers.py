# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we 
# form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number 
# then we shall call the word a triangle word.


from functools import cache    # only hashable objects can be cached
# implementing frozendict for cache dict
# using cache because using function multiple times with same variable

class frozendict(dict):
    """ hashable dictionary """
    def __hash__(self):
        return hash(frozenset(self.items()))


@cache
def wrd_scor(wrd: str)-> int:
    scores = frozendict({chr(x+64):x for x in range(1, 27)})
    
    return sum([scores[i] for i in wrd])


def triangle_lst(num: int)-> list[int]:
    triangles: list[int] = [1]
    n = 1
    
    while triangles[-1] <= num:
        n+=1
        triangles.append(int(n*(n+1)/ 2))
    
    return triangles


if __name__ == '__main__':
    ################## load file #####################
    with open('files\p042_words.txt', 'r') as f:
        wrds = [i[1:-1] for i in f.read().split(',')]
    ##################################################

    score_lst = [wrd_scor(wrd) for wrd in wrds]  # word scores
    triangles = triangle_lst(max(score_lst))
    is_triangle_wrd_lst = [(lambda x:x in triangles)(i) for i in score_lst]   # check for word score is triangle
    
    print(is_triangle_wrd_lst.count(True))