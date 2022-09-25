# https://projecteuler.net/problem=112
# Bouncy numbers

'''
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for 
example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525)
are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers
is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

# ANSWER: 1587000


def is_decreasing(n):
    n_str = str(n)
    for i, char in enumerate(n_str):
        if i == 0:
            continue
        if int(n_str[i]) > int(n_str[i-1]):
            return False
    return(True)

def is_increasing(n):
    n_str = str(n)
    for i, char in enumerate(n_str):
        if i == 0:
            continue
        if int(n_str[i]) < int(n_str[i-1]):
            return False
    return(True)

def what_are_you(n):
    if is_decreasing(n):
        return("Decreasing")
    elif is_increasing(n):
        return("Increasing")
    else:
        return("Bouncy")

def main():

    # tests = [ 134468, 66420, 155349, 21780 ]
    # for test in tests:
    #     print(f'{test} is {what_are_you(test)}')

    # total_bouncy = 0
    # total_increasing = 0
    # total_decreasing = 0
    # total_tests = 21780

    # for i in range(1, total_tests+1):
    #     result = what_are_you(i)
    #     if result == "Bouncy":
    #         total_bouncy += 1
    #     elif result == "Increasing":
    #         total_increasing += 1
    #     elif result == "Decreasing":
    #         total_decreasing += 1

    # bouncy_proportion = total_bouncy / total_tests 
    # print(bouncy_proportion)

    total_bouncy = 0
    total_increasing = 0
    total_decreasing = 0
    proportion_desired = 0.99
    proportion_hit = False
    index = 1

    while not proportion_hit:
        result = what_are_you(index)
        if result == "Bouncy":
            total_bouncy += 1
        elif result == "Increasing":
            total_increasing += 1
        elif result == "Decreasing":
            total_decreasing += 1

        bouncy_proportion = total_bouncy / index 
        if bouncy_proportion == proportion_desired:
            proportion_hit = True
            print(index)
        index += 1

    return()


if __name__ == "__main__":
    main()