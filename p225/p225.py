# https://projecteuler.info/problem=225
# Tribonacci non-divisors

'''
The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ...
is defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.

It can be shown that 27 does not divide any terms of this sequence.
In fact, 27 is the first odd number with this property.

Find the 124th odd number that does not divide any terms of the above sequence.
'''


def main():

    term_count = 0
    trib = []
    trib_max = 50_000
    for i in range(trib_max):
        if i < 3:
            trib.append(1)
        else:
            trib.append(trib[i-3] + trib[i-2] + trib[i-1])

    top_end = 10_000
    for i in range(3,top_end,2):
        even_division = False
        for trib_num in trib:
            mod = trib_num % i
            if mod == 0:
                even_division = True
        if not even_division:
            term_count += 1
            print(term_count, i)
            if term_count == 124:
                break


    return()

if __name__ == "__main__":
    main()