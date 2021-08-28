# https://projecteuler.net/problem=51
# Prime digit replacements

'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''

import math
from collections import Counter

# A prime number is a number greater than 1 with only two factors – themselves and 1
def is_prime(num):

    if (num > 1):
        for i in range(2, num):
            if (num % i == 0):
                return(False)

    return(True)


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



def main():
        
    primes = sieve_of_eratosthenes(100_000)

    primes_that_repeat = []
    # cull the primes that don't have a certain number of repeated digits
    for prime in primes:
        if len(str(prime)) < 5:
            continue
        repeated_values = [ i for i,j in Counter(str(prime)).items() if j > 1 ]
        if repeated_values:
            primes_that_repeat.append(prime)

    with open("./p51/primes_that_repeat.txt", 'w') as primes_that_repeat_outfile:
        for prime in primes_that_repeat:
            primes_that_repeat_outfile.write("%s\n" % prime)

    return()


if __name__ == "__main__":
    main()