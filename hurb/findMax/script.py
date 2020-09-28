#!/bin/python3
# https://www.hackerrank.com/challenges/find-maximum-index-product/problem

import os
import sys


# Complete the solve function below.
def solve(arr):
    result = list()
    idx = 0

    for n in arr:
        result.append(index_product(idx, arr))
        idx += 1

    return max(result)


def index_product(idx, arr):
    le = left(idx, arr)
    ri = right(idx, arr)
    resp = le * ri
    # print(f"{idx}\t{arr[idx]}\t{le}\t{ri}\t{resp}")
    return resp


def left(idx, arr):
    resp, ii = 0, 0

    for n in arr:
        if ii >= idx:
            break
        if n > arr[idx]:
            resp = ii + 1
        ii += 1

    return resp


def right(idx, arr):
    resp, ii = 0, len(arr) - 1

    for n in arr:
        if ii <= idx:
            break
        if arr[ii] > arr[idx]:
            resp = ii + 1
        ii -= 1

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
