# https://www.hackerrank.com/contests/desafio-algoritmos-hurb-1610/challenges/sherlock-and-squares
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the squares function below.
def squares(a, b):
    sqrt_a = math.sqrt(a)
    sqrt_b = math.sqrt(b)
    return int(sqrt_b) - math.ceil(sqrt_a) + 1


if __name__ == '__main__':
    for a, b in [(3, 9), (17, 24)]:
        print(squares(a, b))
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # q = int(input())

    # for q_itr in range(q):
    #     ab = input().split()
    #     a = int(ab[0])
    #     b = int(ab[1])
    #     result = squares(a, b)
    #     fptr.write(str(result) + '\n')

    # fptr.close()
