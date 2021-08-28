# https://projecteuler.net/problem=26
# Reciprocal cycles

'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

from decimal import Decimal, getcontext
import math

def main():

    # for i in range(1, 1000):
    #     # fraction = "{:.16f}".format(1/i)
    #     getcontext().prec = 50
    #     fraction = Decimal(1)/Decimal(i)
    #     print(f'1/{i}: {fraction}')

    repeat_length = []
    for i in range(1, 1000):
        targets = [] 
        target = int(math.pow(10,len(str(i))))
        # targets.append(1)
        while(True):
            targets.append(target)
            target = target % i
            if (target == 0):
                repeat_length.append(0)
                break
            target *= 10
            if (target in targets):
                # check index width
                repeat_length.append( len(targets)-targets.index(target) )
                break
            
    max_repeat_length = max(repeat_length)
    max_index = repeat_length.index(max_repeat_length)+1
    print(f'1/{max_index} has a repeat length of {max_repeat_length}')

    return()



if __name__ == "__main__":
    main()