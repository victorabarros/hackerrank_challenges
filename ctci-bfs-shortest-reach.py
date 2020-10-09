# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
# from collections import defaultdict
import sys


class Graph:
    def __init__(self, nodes: int):
        self._distances = dict()
        self._gender = nodes
        self.passe = 6
        for ii in range(nodes):
            self._distances[ii] = dict()

    def connect(self, x: int, y: int):
        self._distances[x][y] = self.passe
        self._distances[y][x] = self.passe

    def print_distances_from_start(self, start: int):
        # https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
        results = {ii: sys.maxsize for ii in range(self._gender)}
        results[start] = 0

        for ii in range(self._gender):
            ii += start
            if ii >= self._gender:
                ii -= self._gender
            for jj in range(self._gender):
                if self._distances[ii].get(jj):
                    passe = self._distances[ii][jj]
                    if results[ii] + passe < results[jj]:
                        results[jj] = results[ii] + passe
        for ii in range(self._gender):
            ii += start
            if ii >= self._gender:
                ii -= self._gender
            for jj in range(self._gender):
                if self._distances[ii].get(jj):
                    passe = self._distances[ii][jj]
                    if results[ii] + passe < results[jj]:
                        results[jj] = results[ii] + passe
        # for ii in range(start):
        #     for jj in range(self._gender):
        #         if self._distances[ii].get(jj):
        #             passe = self._distances[ii][jj]
        #             if results[ii] + passe < results[jj]:
        #                 results[jj] = results[ii] + passe
        # for ii in range(self._gender):
        #     for jj in range(self._gender):
        #         if self._distances[ii].get(jj):
        #             passe = self._distances[ii][jj]
        #             if results[ii] + passe < results[jj]:
        #                 results[jj] = results[ii] + passe

        del results[start]

        response = list()
        for v in results.values():
            if v == sys.maxsize:
                response.append(str(-1))
                continue
            response.append(str(v))
        print(" ".join(response))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x-1, y-1)

    s = int(input())
    graph.print_distances_from_start(s-1)
