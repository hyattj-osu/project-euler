# https://projecteuler.net/problem=125
# Palindromic sums

'''
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 
92 + 102 + 112 + 122.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of 
these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of 
positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive 
squares
'''

from math import sqrt, floor

def find_consequtive_squares(max_n):
    cons_squares = []
    max_n = 595
    for i in range(1, max_n+1):
        max_square = floor(sqrt(i))
        sum = 0
        while sum < i:
            for j in range(max_square, 0, -1):
                sum += j
                if sum == i: # found consecutive squares
                    print(f"{i}: found consecutive squares")
                    # cons_squares.append(i)
                if sum > i: # need to start lower
                    sum = 0
                    max_square -= 1
                
            # Reaching this point means you are already too far
  

    # print(cons_squares)

def main():

    



    return()

if __name__ == "__main__":
    main()