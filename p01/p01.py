# https://projecteuler.net/problem=1

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''



def main():

    multiples = []
    for num in range(3, 1000): # [3, 1000)
        if (num % 3 == 0) or (num % 5 == 0):
            multiples.append(num)
            # print(num)

    mult_sum = sum(multiples)
    print(f'Sum: {mult_sum}')

    return()



if __name__ == "__main__":
    main()