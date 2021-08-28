import math


count = 0
for n in range(23, 101):
    for r in range(n):
        if (math.factorial(n) / ((math.factorial(r)*math.factorial(n - r)))) > 1_000_000:
            count += 1


print(count)
