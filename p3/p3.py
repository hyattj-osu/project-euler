# https://projecteuler.net/problem=3
# Largest prime factor

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math


# TARGET_INT = 13_195
TARGET_INT = 600_851_475_143


# Doesn't work super well for large numbers
# A prime number is a number greater than 1 with only two factors – themselves and 1
def is_prime(num):

    if (num > 1):
        for i in range(2, num):
            if (num % i == 0):
                return(False)

    return(True)


def main():
    
    largest_prime_factor = 0

    prime_found = False
    current_divisor = 1

    # divide the target integer by natural numbers starting with 1, then check if they are prime
    while not prime_found:
        if (TARGET_INT % current_divisor == 0): # factor found
            factor = int(TARGET_INT / current_divisor)
            if (is_prime(factor)): # check if the factor is a prime number
                largest_prime_factor = factor
                prime_found = True
                print(f'Divisor: {current_divisor}')
        current_divisor += 1

    print(f'Largest Prime Factor: {largest_prime_factor}')

    return()


if __name__ == "__main__":
    main()