#!/bin/python3
# https://www.hackerrank.com/challenges/find-maximum-index-product/problem

import os
import sys


# Complete the solve function below.
def solve(arr):
    result = 0

    for idx in range(0, len(arr)):
        r = index_product(idx, arr)
        if r > result:
            result = r

    return result


def index_product(idx, arr):
    return left(idx, arr) * right(idx, arr)


def left(idx, arr):
    resp = 0

    for ii in range(idx - 1, 0, -1):
        if arr[ii] > arr[idx]:
            resp = ii + 1
            break

    return resp


def right(idx, arr):
    resp = 0

    for ii in range(idx + 1, len(arr)):
        if arr[ii] > arr[idx]:
            resp = ii + 1
            break

    return resp


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # arr_count = int(input())
    # arr = list(map(int, input().rstrip().split()))

    for arr in [[5, 4, 3, 4, 5]]:
        result = solve(arr)
        print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
