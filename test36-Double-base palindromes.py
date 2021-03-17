# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

palindromic = []

n = 0
while n < 1_000_000:
    n += 1
    binary = format(n, 'b')  # convert to binary

    if str(n)[-1] == 0 or str(binary)[-1] == 0:   # if last digit 0
        continue

    elif n == int(str(n)[::-1]) and int(binary) == int(str(binary)[::-1]):  # if decimal and binary are palindromic
        palindromic.append(n)

print(palindromic)
print(sum(palindromic))