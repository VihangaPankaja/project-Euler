""" 
    The series, 
*        1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.

?   Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.
"""


def main(terms: int, last_digit: int) -> str:
    return str(sum([n**n for n in range(1, terms+1)]))[-last_digit:]


if __name__ == '__main__':
    print(main(1_000, 10))
