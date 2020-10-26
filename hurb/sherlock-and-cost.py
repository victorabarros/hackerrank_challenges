# https://www.hackerrank.com/contests/desafio-algoritmos-hurb-1610/challenges/sherlock-and-cost
#!/bin/python3

import math
import os
import random
import re
import sys
from copy import copy


# Complete the cost function below.
def cost(B):
    possibilities = []
    initial_list = [1 for ii in B]
    possibilities.append(initial_list)
    print("idx\tii\tjj\tcurr")
    for idx, ii in enumerate(B):
        for jj in range(2, ii + 1):
            curr = copy(initial_list)
            curr[idx] = jj
            print(f"{idx}\t{ii}\t{jj}\t{curr}")
            possibilities.append(curr)
    return possibilities


if __name__ == '__main__':
    for B in [
        [1, 2, 3]
        # [10, 1, 10, 1, 10]
    ]:
        print(B)
        print(cost(B))
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # t = int(input())
    # for t_itr in range(t):
    #     n = int(input())
    #     B = list(map(int, input().rstrip().split()))
    #     result = cost(B)
    #     fptr.write(str(result) + '\n')
    # fptr.close()
