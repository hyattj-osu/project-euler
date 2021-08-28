# https://projecteuler.net/problem=69
# Totient maximum

'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	                   1	2
3	1,2	                   2	1.5
4	1,3	                   2	2
5	1,2,3,4	               4	1.25
6	1,5	                   2	3
7	1,2,3,4,5,6	           6	1.1666...
8	1,3,5,7	               4	2
9	1,2,4,5,7,8	           6	1.5
10	1,3,7,9	               4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''

import math

LOWER_LIMIT = 2
UPPER_LIMIT = 1_000_000
# UPPER_LIMIT = 100_000

# returns all of the prime numbers from 2 to upper_limit
def sieve_of_eratosthenes(upper_limit):
    # input: an integer n > 1.
    # output: all prime numbers from 2 through n.
    primes = []

    # let A be an array of Boolean values, indexed by integers 2 to n,
    # initially all set to true.
    A = []
    for i in range(0, upper_limit+1):
        A.append(True)
    
    stopping_point = math.floor( int( math.sqrt( upper_limit ) ) )
    for i in range(2, stopping_point):
        if A[i] is True:
            counter = 0
            j = int(math.pow(i,2) + counter*i)
            while(j <= upper_limit):
                A[j] = False
                counter += 1
                j = int(math.pow(i,2) + counter*i)

    for i in range(2, upper_limit):
        if A[i] is True:
            primes.append(i)

    return(primes)



def find_prime_factors(n, primes):
    prime_factors = []
    for p in primes:
        # if p > int(math.sqrt(n)):
        if p > n:
            break
        if (n % p == 0): # prime factor
            prime_factors.append(p)
    if not prime_factors:
        prime_factors.append(n)
    return(prime_factors)      



def main():
    primes = sieve_of_eratosthenes(1_000)
    totients = []
    max_n_over_totient = 0
    max_n = 0
    for n in range(LOWER_LIMIT, UPPER_LIMIT+1):
        prime_factors = find_prime_factors(n, primes)
        totient = n
        for p in prime_factors:
            totient *= (1 - (1/p))
        totient = int(totient)
        totients.append(totient)
        n_over_totient = n / totient
        if (n_over_totient > max_n_over_totient):
            max_n_over_totient = n_over_totient
            max_n = n

    print(f'Max n: {max_n}')

    return()



if __name__ == "__main__":
    main()