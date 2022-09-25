# https://projecteuler.net/problem=179
# Consecutive positive divisors

'''
Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same number of positive divisors. For example, 
14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
'''

# ANSWER: 986262

from functools import reduce

# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python

def find_factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number

def divisorGen(n):
    factors = list(find_factors(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def main():
    count = 0
    old_num_factors = 0
    num_factors = 0

    for i in range(1, 10_000_000):
        num_factors = len(list(find_factors(i)))
        if i > 1:
            if num_factors == old_num_factors:
                count += 1
        old_num_factors = num_factors
    print(count)
                

if __name__ == "__main__":
    main()