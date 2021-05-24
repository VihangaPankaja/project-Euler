# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

from my_math import num_to_word


def wrd_count(number: int)-> int:
    word_count: int = 0

    for i in range(1,number + 1):
        word_count += len(num_to_word(i))
        
    return word_count


if __name__ == '__main__':
    print(wrd_count(1_000))