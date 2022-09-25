# https://projecteuler.info/problem=169
# Exploring the number of different ways a number can be expressed as a sum of powers of 2 

'''
Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2 using each 
power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(10^25)?
'''


from time import time
from math import log, pow

exponent = 25
N = pow(10, exponent)

def recursion_mess(n, po2=None):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    po2_secondary = int(log(n, 2)) # find the largest power of 2 that fits in the remaining number
    if po2 is None:
        po2 = po2_secondary
    elif po2 < po2_secondary - 1:
        return 0
    else:
        po2 = min(po2, po2_secondary)
    if po2 == 0:
        if n < 3:
            return 1
        else:
            return 0
    po2_max = pow(2, po2)
    # tests all three possible branches at once; n being left alone, using one of the po2, or both
    return recursion_mess(n, po2-1)+recursion_mess(n-po2_max, po2-1)+recursion_mess(n-po2_max*2, po2-1)

start = time()
answer = recursion_mess(N)
finish = time()
print(f'10^{exponent}: {answer} in {finish - start} seconds')


# from itertools import chain, combinations

# def powerset(iterable):
#     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# import math
# from numpy import empty

# from sympy import sequence


# def get_powers_of_two(max_num):

#     powers_of_two = []
#     current_num = 0
#     current_exponent = 0
#     while current_num < max_num:
#         current_num = math.pow(2, current_exponent)
#         if current_num <= max_num:
#             powers_of_two.append(current_num)
#             current_exponent += 1
#     powers_of_two.sort(reverse=True)
#     return(powers_of_two)

# def find_sequence(powers_of_two, max_num, sequences):
#     sum = 0
#     sequence = []
#     for power_of_two in powers_of_two:
#         for i in range(2):
#             if sum + power_of_two <= max_num:
#                 sum += power_of_two
#                 sequence.append(power_of_two)
#     if sequence in sequences:
#         used_sequence = True
#     else:
#         return(sequence)

# def main():

#     # This empirical information is interesting
#     # Power of two      Value       Good Subsets
#     #          2^0          1                  1
#     #          2^1          2                  2
#     #          2^2          4                  3
#     #          2^3          8                  4
#     #          2^4         16                  5
#     #          2^5         32                  6
#     #          2^6         64                  7
#     #          2^7        128                  8
#     #          2^8        256                  9
#     #          2^9        512                 10
#     #          2^10      1024                 11

#     # It looks like there are exactly n+1 good subsets for 2^n
#     # Max power of 2 value under 1x10^25 is 2^83
#     # 2^83 would give 84 good subsets 

#     # max_num = 1e4
#     # powers_of_two = get_powers_of_two(max_num)
#     # sequences = []

#     # import itertools
#     # good_subsets = []
#     # stuff = []
#     # for power_of_two in powers_of_two:
#     #     stuff.append(power_of_two)
#     #     stuff.append(power_of_two)
#     # for L in range(len(stuff) + 1):
#     #     for subset in itertools.combinations(stuff, L):
#     #         if sum(subset) == max_num:
#     #             good_subsets.append(subset)
#     #             print(subset)
#     # print(len(set(good_subsets)))

#     max_num = 1e4
#     powers_of_two = get_powers_of_two(max_num)
#     sequences = []

#     stuff = []
#     for power_of_two in powers_of_two:
#         stuff.append(power_of_two)
#         stuff.append(power_of_two)

#     results = list(powerset(stuff))
#     print(results)
    
    

#     return
#     max_num = 1E25
#     max_num = 10
#     powers_of_two = get_powers_of_two(max_num)
#     sequences = []

#     sequences_remain = True
#     while sequences_remain:
#         new_sequence = find_sequence(powers_of_two, max_num, sequences)
#         if new_sequence is not empty:
#             sequences.append(new_sequence)
#         else:
#             sequences_remain = False
    
#     for sequence in sequences:
#         print(sequence)

#     return()


# if __name__ == "__main__":
#     main()