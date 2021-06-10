""" 
  Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,

  the first 10 terms will be:
* 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

  By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
? find the sum of the even-valued terms
 """

def sum_fib(max_num: int) -> int:
    fib: list[int] = [1,2] # fibanachi values s a list

    while fib[-1] <= max_num:
        fib.append(fib[-1] + fib[-2]) # find next in series

    return (sum(n for n in fib if n%2 == 0)) # sum of even in series


if __name__ == '__main__':
    print(sum_fib(4_000_000))
