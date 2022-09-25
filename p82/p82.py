# https://projecteuler.info/problem=82
# Path sum: three ways

'''
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in
the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

131 673 234 103  18
201  96 342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524  37 331
 
201 -> 96 -> 342 -> 234 -> 103 -> 18 

Find the minimal path sum from the left column to the right column in matrix.txt 
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
'''

# Based on https://codereview.stackexchange.com/questions/38404/project-euler-82-path-sum-three-ways
def minimum_path_sum(matrix):
    nrows, ncols = len(matrix), len(matrix[0])
    best = [matrix[row][0] for row in range(nrows)]

    for col in range(1, ncols):
        column = [matrix[row][col] for row in range(nrows)]

        best = [
            # The cost of each cell, plus...
            column[row] +

            # the cost of the cheapest approach to it
            min([
                best[prev_row] + sum(column[prev_row:row:(1 if prev_row <= row else -1)])
                for prev_row in range(nrows)
            ])
            for row in range(nrows)
        ]

    return min(best)

def main():

    matrix = []
    with open("./p82/p082_matrix.txt", 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            split_line = line.strip().split(',')
            matrix.append([ int(n) for n in split_line ])

    sum = minimum_path_sum(matrix)
    print(sum)

    return()

if __name__ == "__main__":

    main()