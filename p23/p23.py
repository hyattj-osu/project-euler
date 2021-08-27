# https://projecteuler.net/problem=23
# Non-abundant sums
# Answer: 4179871

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper 
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers 
is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed 
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

LOWER_ABUNDANT_LIMIT = 12
UPPER_ABUNDANT_LIMIT = 28_123

# find divisors
# sum them
# abdundant if greather than the number

def find_divisors(num):
    divisors = []

    for i in range(1, num):
        if (num % i == 0):
            if i not in divisors:
                divisors.append(i)

    return(divisors)


def find_abundant_numbers(lower, upper):

    abundant_numbers = []
    for i in range(lower, upper+1):
        divisors = find_divisors(i)
        # print(divisors)

        divisor_sum = sum(divisors)

        if divisor_sum > i: # abundant
            abundant_numbers.append(i)

    return(abundant_numbers)


def find_deficient_numbers(lower, upper):

    deficient_numbers = []
    for i in range(lower, upper+1):
        divisors = find_divisors(i)
        # print(divisors)

        divisor_sum = sum(divisors)

        if divisor_sum < i: # deficient
            deficient_numbers.append(i)

    return(deficient_numbers)    


def write_abundants():
    print("Starting abundant...")
    with open("./p23/abundant_list.txt" ,'w') as abundant_file:
        abundant_numbers = find_abundant_numbers(LOWER_ABUNDANT_LIMIT, UPPER_ABUNDANT_LIMIT) 
        for number in abundant_numbers:
            abundant_file.write("%s\n" % number)
    print("Abundant done!")
    return()

def read_abundants():

    with open("./p23/abundant_list.txt" ,'r') as abundant_file:
        lines = abundant_file.readlines()
        abundants_list = []
        [ abundants_list.append(int(n)) for n in lines ]
        # abundants = set(abundants_list)
    return(abundants_list)



def write_deficients():
    print("Starting deficient...")
    with open("./p23/deficient_list.txt" ,'w') as deficient_file:
        deficient_numbers = find_deficient_numbers(LOWER_ABUNDANT_LIMIT, UPPER_ABUNDANT_LIMIT) 
        for number in deficient_numbers:
            deficient_file.write("%s\n" % number) 
    print("Deficient done!")
    return()

def read_deficients():

    with open("./p23/deficient_list.txt" ,'r') as deficient_file:
        lines = deficient_file.readlines()
        deficient_list = []
        [ deficient_list.append(int(n)) for n in lines ]
        # deficients = set(deficient_list)
    return(deficient_list)




def write_abundant_sums(abundants):
    sums = []

    # abundant + abundant
    length = len(abundants)
    for i in range(0, length):
        for j in range(i, length):
            sums.append(abundants[i] + abundants[j])

    sum_set = set(sums)

    with open("./p23/abundant_sums_list.txt" ,'w') as abundant_sums_file:
        for number in list(sum_set):
            abundant_sums_file.write("%s\n" % number) 
    return()    

def read_abundant_sums():

    with open("./p23/abundant_sums_list.txt" ,'r') as abundant_sums_file:
        lines = abundant_sums_file.readlines()
        abundant_sums_list = []
        [ abundant_sums_list.append(int(n)) for n in lines ]
        # deficients = set(deficient_list)
    return(abundant_sums_list)    




def main():

    write_abundants()
    # write_deficients()
    abundants = read_abundants()
    # deficients = read_deficients()

    write_abundant_sums(abundants)
    abundant_sums = read_abundant_sums()

    base_numbers = set([*range(1, UPPER_ABUNDANT_LIMIT+1, 1)])
    abundant_sums_set = set(abundant_sums)

    good_values = base_numbers - abundant_sums_set

    end_sum = sum(good_values)
    print(f'Sum: {end_sum}')
    

    return()

if __name__ == "__main__":
    main()