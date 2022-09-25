# https://projecteuler.info/problem=81
# Path sum: two ways

'''
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and 
down, is indicated in bold red and is equal to 2427.

131 673 234 103  18
201  96 342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524  37 331
 
131 -> 201 -> 96 -> 342 -> 746 -> 422 -> 121 -> 37 -> 331

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt 
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
'''

# Based on https://github.com/kyle8998/LeetCode/blob/master/Python/minimum-path-sum.py
def minimum_path_sum(grid):
    sum = list(grid[0])
    for j in range(1, len(grid[0])):
        sum[j] = sum[j - 1] + grid[0][j]

    for i in range(1, len(grid)):
        sum[0] += grid[i][0]
        for j in range(1, len(grid[0])):
            sum[j] = min(sum[j - 1], sum[j]) + grid[i][j]

    return sum[-1]

def main():

    matrix = []
    with open("./p81/p081_matrix.txt", 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            split_line = line.strip().split(',')
            matrix.append([ int(n) for n in split_line ])

    sum = minimum_path_sum(matrix)
    print(sum)

    return()

if __name__ == "__main__":

    main()