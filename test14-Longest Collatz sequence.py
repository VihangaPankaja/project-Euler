# he following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

max_number = 1_000_000

def T_n(n):
    global term_lst

    if n == 2:
        term_lst.append(1)

    elif n == 1:
        return term_lst

    elif n % 2 == 0:                    # if n even
        term_lst.append(int(n /2))
        T_n(int(n / 2))

    else:                              # if n odd
        term_lst.append(3 * n + 1)
        T_n(3 * n + 1)

    return term_lst

max_start = 0
max_terms = 0

for i in range(1, max_number):
    term_lst = [i]                      # new term list with currunt number for function
    seq_lenth = len(T_n(i))             # lenth for that number

    if seq_lenth > max_terms:           # lenth higher than currunt max
        max_terms = seq_lenth
        max_start = i


print(max_start,max_terms)
