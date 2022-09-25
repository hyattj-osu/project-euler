# https://projecteuler.net/problem=145
# How many reversible numbers are there below one-billion?

'''
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. 
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are 
reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
'''

# ANSWER: 608720

def is_reversible(n):
    n_str = str(n)
    # no leading / trailing zeroes
    if n_str[-1] == '0':
        return(False)
    reversed_n = int(''.join(reversed(str(n))))    
    sum = n + reversed_n
    for digit in str(sum):
        is_odd = int(digit) % 2
        if not is_odd:
            return(False)
    return(True)


def main():
    # tests = [ 36, 63, 409, 904 ]
    # for test in tests:
    #     print(f'{test}: {is_reversible(test)}')

    num_reversible = 0
    for i in range(1, 1_000_000_000):
        if is_reversible(i):
            num_reversible += 1
    print(num_reversible)
    return()

if __name__ == "__main__":
    main()