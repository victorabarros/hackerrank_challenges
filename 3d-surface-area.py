# https://www.hackerrank.com/challenges/3d-surface-area/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the surfaceArea function below.
def surfaceArea(A):
    H, W = len(A), len(A[0])

    # Calculate bottom
    bottom = 0
    for line in A:
        for ee in line:
            if ee != 0:
                bottom += 1

    # Calculate top
    top = bottom

    # Calculate front
    fronts = [0 for ii in range(W)]
    for ii, line in enumerate(A):
        for jj, ee in enumerate(line):
            if ii == 0:
                fronts[jj] += ee
                continue

            ee_behind = A[ii - 1][jj]  # same element from line behind
            if ee > ee_behind:
                fronts[jj] += ee - ee_behind
    front = sum(fronts)

    # Calculate back
    back = front

    # Calculate left
    lefts = [0 for ii in range(H)]
    for jj in range(W):
        for ii in range(H):
            ee = A[ii][jj]
            if jj == 0:
                lefts[ii] += ee
                continue

            ee_behind = A[ii][jj - 1]  # same element from line behind
            if ee > ee_behind:
                lefts[ii] += ee - ee_behind
    left = sum(lefts)

    # Calculate right
    right = left

    return bottom, top, front, back, left, right


if __name__ == '__main__':
    sur = surfaceArea([[1, 2, 4],
                       [2, 2, 3],
                       [1, 3, 4]])
    print(sum(sur))
    # bottom  9
    # top     9
    # front  10
    # back   10
    # left   11
    # right  11
    # sum    60

    sur = surfaceArea([[91, 80, 7, 41, 36, 11, 48, 57, 40, 43]])
    print(sum(sur))
    # bottom 10
    # top    10
    # front  91+80+7+41+36+11+48+57+40+43=454
    # back   91+80+7+41+36+11+48+57+40+43=454
    # left   91+(41-7)+(48-11)+(57-48)+(43-40)=174
    # right  43+(57-40)+(36-11)+(41-36)+(80-7)+(91-80)=174
    # sum    1276

    sur = surfaceArea([[1, 3, 4],
                       [2, 2, 3],
                       [1, 2, 4]])
    print(sum(sur))
    # bottom  9
    # top     9
    # front  10
    # back   10
    # left   11
    # right  11
    # sum    60

    sur = surfaceArea([
        [51],
        [32],
        [28],
        [49],
        [28],
        [21],
        [98],
        [56],
        [99],
        [77]
    ])
    print(sum(sur))
    # bottom 10
    # top    10
    # front  51+49-28+98-21+99-56=192
    # back   77+(99-77)+(98-56)+(28-21)+(49-28)+(32-28)+(51-32)=192
    # left   51+32+28+49+28+21+98+56+99+77=539
    # right  51+32+28+49+28+21+98+56+99+77=539
    # sum    1482

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
