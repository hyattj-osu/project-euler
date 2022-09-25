# https://projecteuler.info/problem=233
# Lattice points on a circle

'''
Let f(N) be the number of points with integer coordinates that are on a circle passing through (0,0), (N,0),(0,N), 
and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?
'''


# f(160225) MIGHT be one that has 420

from time import time
from math import pow, ceil, floor, sqrt

# https://www.khanacademy.org/math/geometry/xff63fac4:hs-geo-conic-sections/hs-geo-circle-expanded-equation/a/circle-equation-review
# equation of a circle: (x-h)^2 + (y-k)^2 = r^2
# circle centered at h,k with radius r

# https://mathworld.wolfram.com/SchinzelCircle.html
# Maybe?
# https://en.m.wikipedia.org/wiki/Pythagorean_triple


# https://stackoverflow.com/questions/575117/generating-unique-ordered-pythagorean-triplets
# import numpy as np

# def gen_prim_pyth_trips(limit=None):
#     u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
#     a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
#     d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
#     uad = np.array([u, a, d])
#     m = np.array([3, 4, 5])
#     while m.size:
#         m = m.reshape(-1, 3)
#         if limit:
#             m = m[m[:, 2] <= limit]
#         yield from m
#         m = np.dot(m, uad)
#     return

# def gen_all_pyth_trips(limit):
#     for prim in gen_prim_pyth_trips(limit):
#         i = prim
#         for _ in range(limit//prim[2]):
#             yield i
#             i = i + prim
#     return

# def pythagorean_triples(limit):
#     result = []
#     for x in range(1, limit):
#         xx = x * x
#         y = x + 1
#         z = y + 1
#         while z <= limit:
#             zz = xx + y * y
#             while z * z < zz:
#                 z += 1
#             if z * z == zz and z <= limit:
#                 result.append([x, y, z])
#             y += 1
#     return result

# def main():
#     limit = 100_000
#     N = 10_000

#     # pythagorean_triples(limit)

#     # for n in gen_prim_pyth_trips(limit):
#     #     print(n)

#     pyths = list(gen_all_pyth_trips(limit))

#     # distance formula from 0,0 to N,N to get diameter
#     # d = sqrt(pow(N,2)+pow(N,2))
#     r = N / sqrt(2)
#     # r = d / 2

    # return()

from cmath import atan
import math

def main():
    # angles = []

    # we know h and k are both N/2
    min_n = 1
    max_n = 10**11
    for n in range(min_n, max_n+1):
        num_ints = 0
        num_ints_quad = 0
        h = n / 2
        k = n / 2

        # distance formula from 0,0 to N,N to get diameter
        d = math.sqrt(pow(n,2)+pow(n,2))
        r = d / 2

        # we only need to check a quarter of the circle
        # the largest x and y coordinate would be (N/2 + r)

        x_max = math.floor((n/2) + r)
        y_max = x_max

        # minimum numbers are just over n/2 as an integer
        x_min = math.ceil(n/2)
        y_min = x_min
        for x in range(x_min, x_max+1):
            # circle: (x-h)^2 + (y-k)^2 = r^2
            y = math.sqrt(pow(r,2) - pow(x-h,2))+k
            if round(y,10) == int(y):
                # print(x, y)
                # try:
                #     angle = math.degrees(math.atan(y/x))
                #     if not angle in angles:
                #         angles.append(angle)
                # except:
                #     pass

                # if n == 9860:
                #     print(x, y)

                num_ints_quad += 1
                num_ints = num_ints_quad * 4
                # if num_ints >= 100:
                #     print(f'f({n}): {num_ints}')
                if num_ints >= 420:
                    break # already over the number we want
        
        if num_ints > 400:
            print(f'f({n}): {num_ints}')

    # with open("./p233/angles.txt", 'w') as angles_file:
    #     angles.sort()
    #     for angle in angles:
    #         angles_file.write("%s\n" % angle)
    
    return()

if __name__ == "__main__":
    main()