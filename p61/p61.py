def main():

    # P_3,n = n*(n+1)/2
    n_min = 45
    n_max = 140

    P_3 = []
    for n in range(n_min, n_max+1):
        P_3.append(n*(n+1)/2)

    # P_4,n = n^2
    n_min = 32
    n_max = 99

    P_4 = []
    for n in range(n_min, n_max+1):
        P_4.append(n*n)

    # P_5,n = n(3n-1)/2
    n_min = 26
    n_max = 81

    P_5 = []
    for n in range(n_min, n_max+1):
        P_5.append(n*(3*n-1)/2)

    # P_6,n = n(2n-1)
    n_min = 23
    n_max = 70

    P_6 = []
    for n in range(n_min, n_max+1):
        P_6.append(n*(2*n-1))

    # P_7,n = n(5n-3)/2
    n_min = 21
    n_max = 63

    P_7 = []
    for n in range(n_min, n_max+1):
        P_7.append(n*(5*n-3)/2)
        # print(f'P_7,{n} = {P_7}')

    # P_8,n = n(3n-2)
    n_min = 19
    n_max = 58

    P_8 = []
    for n in range(n_min, n_max+1):
        P_8.append(n*(3*n-2))
        # print(f'P_8,{n} = {P_8}')

    P_3_end_slice = []
    for value in P_3:
        P_3_end_slice.append(str(int(value))[-2:])

    P_4_start_slice = []
    for value in P_4:
        P_4_start_slice.append(str(int(value))[0:2])

    
    return()

if __name__ == "__main__":
    main()