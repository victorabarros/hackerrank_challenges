#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the formingMagicSquare function below.
def formingMagicSquare(matrix):
    magic_ctes = _magic_ctes(matrix)
    # print(magic_ctes)
    for magic_cte in magic_ctes.keys():
        


def _magic_ctes(matrix: list) -> dict:
    magic_ctes = defaultdict(int)
    lenght = len(matrix)

    # iter lines
    for line in matrix:
        magic_cte = sum(line)
        magic_ctes[magic_cte] += 1

    # iter columns
    for ii in range(0, lenght):
        magic_cte = 0
        for jj in range(0, lenght):
            magic_cte += matrix[jj][ii]
        magic_ctes[magic_cte] += 1

    # iter primary diagonal
    magic_cte = 0
    for ii in range(0, lenght):
        magic_cte += matrix[ii][ii]
    magic_ctes[magic_cte] += 1

    # iter secondary diagonal
    magic_cte = 0
    for ii in range(0, lenght):
        magic_cte += matrix[ii][lenght - 1 - ii]
    magic_ctes[magic_cte] += 1

    return magic_ctes


if __name__ == '__main__':
    # # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = []
    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare([[4, 8, 2],  # 14
                                 [4, 5, 7],  # 16
                                 [6, 1, 6]]) # 13
                            # 13 14 14 15 15
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
