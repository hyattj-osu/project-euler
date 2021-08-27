# https://projecteuler.net/problem=13
# Large sum

'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

*saved as data.txt*
'''


def main():

    numbers = []
    with open("./p13/data.txt", 'r') as infile:
        lines = infile.readlines()
        [ numbers.append(int(n)) for n in lines ]

    # python can just add these no problem
    full_sum = sum(numbers)
    print(f'Full Sum: {full_sum}')
    sum_string = str(full_sum)
    print(sum_string[0 : 10])
    return()


if __name__ == "__main__":
    main()