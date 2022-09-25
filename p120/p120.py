import math

# ANSWER: 333082500

def main():

    total = 0
    for a in range(3, 1001):
        r_max = 0
        for n in range(1, 2001):
            # calc = math.pow(a-1, n) + math.pow(a+1, n)
            calc = ((a-1)**n) + ((a+1)**n)
            calc2 = a * a
            remainder = calc % calc2

            if remainder > r_max:
                r_max = remainder

        total = total + r_max
    print(total)

    return()

if __name__ == "__main__":
    main()