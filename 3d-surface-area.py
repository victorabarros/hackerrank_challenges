# https://www.hackerrank.com/challenges/3d-surface-area/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the surfaceArea function below.
def surfaceArea(A):
    # Calculate bottom
    bottom = 0
    for ii, line in enumerate(A):
        for jj, ee in enumerate(line):
            if ee != 0:
                bottom += 1

    # Calculate top
    top = 0
    top = bottom

    # Calculate front
    front = 0


    print("ii\tjj\tee")
    for ii, line in enumerate(A):
        for jj, ee in enumerate(line):
            print(f"{ii}\t{jj}\t{ee}")
    pass


if __name__ == '__main__':
    A = [[1, 3, 4],                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
         [2, 2, 3],
         [1, 2, 4]]
    print(surfaceArea(A))
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # HW = input().split()
    # H = int(HW[0])
    # W = int(HW[1])

    # A = []
    # for _ in range(H):
    #     A.append(list(map(int, input().rstrip().split())))

    # result = surfaceArea(A)
    # fptr.write(str(result) + '\n')
    # fptr.close()
