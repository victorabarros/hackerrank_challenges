#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    results = []
    for ii in range(0, 4):
        line = arr[ii]
        line_plus_one = arr[ii + 1]
        line_plus_two = arr[ii + 2]
        for jj in range(0, 4):
            result = line[jj] + line[jj + 1] + line[jj + 2]
            result += line_plus_one[jj + 1]
            result += line_plus_two[jj] + line_plus_two[jj + 1] + line_plus_two[jj + 2]
            results.append(result)
    import pdb; pdb.set_trace()
    return max(results)

if __name__ == '__main__':
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(result)
