"""
  Consider all integer combinations of 𝑎ᵇ for 2 ≤ 𝑎 ≤ 5 and 2 ≤ 𝑏 ≤ 5:
*    2²=4,   2³=8,   2⁴=16,  2⁵=32
*    3²=9,   3³=27,  3⁴=81,  3⁵=243
*    4²=16,  4³=64,  4⁴=256, 4⁵=1024
*    5²=25,  5³=125, 5⁴=625, 5⁵=3125

  If they are then placed in numerical order, with any repeats removed, 
  we get the following sequence of 15 distinct terms:  
*    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
  
? How many distinct terms are in the sequence generated by 𝑎ᵇ for 2 ≤ 𝑎 ≤ 100 and 2 ≤ 𝑏 ≤ 100?
"""


def terms_in_power_seq(a: range, b: range) -> int:
    number_lst: list[int] = []

    for i in a: 
        for j in b: 
            number_lst.append(i**j)  # all posibilities

    return len(set(number_lst))  # clean duplicate and  find lenth

    
if __name__ == "__main__":
    print(terms_in_power_seq(range(2, 101), range(2, 101)))