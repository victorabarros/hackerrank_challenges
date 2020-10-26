# https://www.hackerrank.com/contests/desafio-algoritmos-hurb-0910/challenges/bomber-man
import math
import os
import random
import re
import sys


# RULES:
# Initially, Bomberman arbitrarily plants bombs in some of the cells.
# After one second, Bomberman does nothing.
# After one, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs.
# After one, any bombs planted exactly three seconds ago will detonate.
# Bomberman then repeats steps 3 and 4 indefinitely.
class Grid:
    def __init__(self, grid):
        self.grid = grid

# Complete the bomberMan function below.
def bomberMan(n, grid):
    bombs = findBombs(grid)
    # second 1:
    # do nothing

    # second 2
    grid = fillAllGridWithBombs(grid)
    # second 3
    # initial bomb detonates and blow up neighboring
    grid = detonateBombs(grid, bombs)

    print(bombs)
    return grid


def findBombs(grid):
    bombs = []
    for ii, line in enumerate(grid):
        for jj, v in enumerate(line):
            if v == "O":
                bombs.append((ii, jj))
    return bombs


def fillAllGridWithBombs(grid):
    for ii, line in enumerate(grid):
        for jj, _ in enumerate(line):
            grid[ii][jj] = "O"
    return grid


def detonateBombs(grid, bombs):
    for ii, jj in bombs:
        grid[ii][jj] = "."
        if ii > 0:
            grid[ii - 1][jj] = "."
        if jj > 0:
            grid[ii][jj - 1] = "."
        if ii < len(grid):
            grid[ii + 1][jj] = "."
        if jj < len(grid[0]):
            grid[ii][jj + 1] = "."
    return grid


if __name__ == '__main__':
    # rct = input().split()
    # r, c, t = map(int, rct)
    r, c, t = 6, 7, 3
    # grid = []

    # for _ in range(r):
    #     grid_item = input()
    #     grid.append(grid_item)
    grid = [
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "O", ".", ".", "."],
        [".", ".", ".", ".", "O", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        ["O", "O", ".", ".", ".", ".", "."],
        ["O", "O", ".", ".", ".", ".", "."]
    ]

    result = bomberMan(t, grid)

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    # fptr.close()
