# https://www.hackerrank.com/contests/desafio-algoritmos-0611/challenges/queens-attack-2
#!/bin/python3

import math
import os
import random
import re
import sys


def checkElementInObstacle(element, obstacles):
    try:
        idx = obstacles.index(element)
        obstacles.pop(idx)  # Anti pattern
        return True
    except ValueError:
        return False


# Complete the queensAttack function below.
def queensAttack(n, k, rq, cq, obstacles):
    rst = 0

    # L
    L_ii, L_jj = rq, cq + 1
    while L_jj <= n:
        if checkElementInObstacle((L_ii, L_jj), obstacles):
            break
        rst, L_jj = rst + 1, L_jj + 1

    # NL
    NL_ii, NL_jj = rq + 1, cq + 1
    while NL_ii <= n and NL_jj <= n:
        if checkElementInObstacle((NL_ii, NL_jj), obstacles):
            break
        rst, NL_ii, NL_jj = rst + 1, NL_ii + 1, NL_jj + 1

    # N
    N_ii, N_jj = rq + 1, cq
    while N_ii <= n:
        if checkElementInObstacle((N_ii, N_jj), obstacles):
            break
        rst, N_ii = rst + 1, N_ii + 1

    # NO
    NO_ii, NO_jj = rq + 1, cq - 1
    while NO_ii <= n and NO_jj > 0:
        if checkElementInObstacle((NO_ii, NO_jj), obstacles):
            break
        rst, NO_ii, NO_jj = rst + 1, NO_ii + 1, NO_jj - 1

    # O
    O_ii, O_jj = rq, cq - 1
    while O_jj > 0:
        if checkElementInObstacle((O_ii, O_jj), obstacles):
            break
        rst, O_jj = rst + 1, O_jj - 1

    # SO
    SO_ii, SO_jj = rq - 1, cq - 1
    while SO_ii > 0 and SO_jj > 0:
        if checkElementInObstacle((SO_ii, SO_jj), obstacles):
            break
        rst, SO_ii, SO_jj = rst + 1, SO_ii - 1, SO_jj - 1

    # S
    S_ii, S_jj = rq - 1, cq
    while S_ii > 0:
        if checkElementInObstacle((S_ii, S_jj), obstacles):
            break
        rst, S_ii = rst + 1, S_ii - 1

    # SL
    SL_ii, SL_jj = rq - 1, cq + 1
    while SL_ii > 0 and SL_jj <= n:
        if checkElementInObstacle((SL_ii, SL_jj), obstacles):
            break
        rst, SL_ii, SL_jj = rst + 1, SL_ii - 1, SL_jj + 1

    return rst


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # nk = input().split()
    # n = int(nk[0])
    # k = int(nk[1])
    # r_qC_q = input().split()
    # r_q = int(r_qC_q[0])
    # c_q = int(r_qC_q[1])
    # obstacles = []

    # for _ in range(k):
    #     obstacles.append(tuple(map(int, input().rstrip().split())))
    for (n, k), (r_q, c_q), obstacles, answer in [
        ((4, 0), (4, 4), [], 9),
        ((5, 3), (4, 3), [(5, 5), (4, 2), (2, 3)], 10),
        ((5, 3), (4, 3), [(5, 5), (4, 2), (2, 3)], 10)
    ]:
        result = queensAttack(n, k, r_q, c_q, obstacles)
        print(result, result == answer)
    # fptr.write(str(result) + '\n')
    # fptr.close()
