# https://projecteuler.info/problem=104
# Pandigital Fibonacci ends

'''
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_(n−1) + F_(n−2), where F1 = 1 and F2 = 1.
It turns out that F_541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 
pandigital (contain all the digits 1 to 9, but not necessarily in order). And F_2749, which contains 575 digits, is the 
first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, 
find k.
'''

import math

def generate_fibonacci(n_minus_1, n_minus_2, f_end):
    for i in range(f_end):
        fn = n_minus_1 + n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = fn
        if check_for_last_pangidital(fn):
            if check_for_start_pangidital(fn):
                print('last: ' + str(i+3))
    return(fn)

def check_for_start_pangidital(fn):
    num_digits = int(math.log10(fn))+1
    first_nine_int = fn // 10**(num_digits - 9)
    # first_nine = str(fn)[0:9]]
    first_nine = str(first_nine_int)
    first_pandigital = set(first_nine)
    if len(first_pandigital) == 9 and not '0' in first_pandigital:
        # print(fn)
        # print(num_digits)
        return(True)
    return(False)

def check_for_last_pangidital(fn):
    last_nine_int = fn % 10_000_000_000
    # last_nine = str(fn)[-9:]
    last_nine = str(last_nine_int)
    last_pandigital = set(last_nine)
    if len(last_pandigital) == 9 and not '0' in last_pandigital:
        # print(fn)
        return(True)
    return(False)


def main():
        
    f1 = 1
    f2 = 1
    f_end = 2747
    f_end = 2_000_000
    fn = generate_fibonacci(f1, f2, f_end)
    # print(fn)



    return()


if __name__ == "__main__":
    main()