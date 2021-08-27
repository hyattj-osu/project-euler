# https://projecteuler.net/problem=25
# 1000-digit Fibonacci number

'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''



def main():

    n_minus_2 = 0
    n_minus_1 = 1
    curr_num = n_minus_1 + n_minus_2

    index = 2
    while ( len(str(curr_num)) < 1_000):
        # print(curr_num)
        n_minus_2 = n_minus_1
        n_minus_1 = curr_num
        curr_num = n_minus_1 + n_minus_2
        index += 1

    print(f'First Fibonacci with 1,000 digits: {curr_num}')
    print(f'Index of Fibonacci with 1,000 digits: {index}')

    return()



if __name__ == "__main__":
    main()