

def main():

    tri_string = []
    tri_string.append('75')
    tri_string.append('95 64')
    tri_string.append('17 47 82')
    tri_string.append('18 35 87 10')
    tri_string.append('20 04 82 47 65')
    tri_string.append('19 01 23 75 03 34')
    tri_string.append('88 02 77 73 07 63 67')
    tri_string.append('99 65 04 28 06 16 70 92')
    tri_string.append('41 41 26 56 83 40 80 70 33')
    tri_string.append('41 48 72 33 47 32 37 16 94 29')
    tri_string.append('53 71 44 65 25 43 91 52 97 51 14')
    tri_string.append('70 11 33 28 77 73 17 78 39 68 17 57')
    tri_string.append('91 71 52 38 17 14 91 43 58 50 27 29 48')
    tri_string.append('63 66 04 68 89 53 67 30 73 16 69 87 40 31')
    tri_string.append('04 62 98 27 23 09 70 98 73 93 38 53 60 04 23')

    triangle = []
    for line in tri_string:
        triangle.append([ int(num) for num in line.split(' ') ])

    current_y = 0
    current_x = 0
    path = []

    while(current_y < len(triangle)):
        sum_y = 0
        sum_x = 0
        for y in range(current_y+1, len(triangle)):
            sum_y += triangle[y][current_x]
            sum_x += triangle[y][current_x+y-1]

        if sum_y > sum_x:
            current_y += 1
        else:
            current_y += 1
            current_x += 1
        if current_y < len(triangle):
            path.append(triangle[current_y][current_x])

    sum(path)
    return()

if __name__ == '__main__':
    main()