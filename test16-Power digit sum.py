""" 
* 2¹⁵ = 32768 
  and the sum of its digits is,
* 3 + 2 + 7 + 6 + 8 = 26.

? What is the sum of the digits of the number 2¹⁰⁰⁰
 """
 
 
def pow(num: int)-> int:
    return sum(map(int, str(2 ** num)))


if __name__ == "__main__":
    print(pow(1_000))