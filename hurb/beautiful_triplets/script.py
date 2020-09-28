#!/bin/python3


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    resp = 0
    n = len(arr)

    def iterFinal(jj):
        inc = 0
        for kk in range(jj + 1, n):
            if arr[kk] - arr[jj] > d:
                break
            if arr[kk] - arr[jj] == d:
                inc += 1

        return inc

    def iterMid(ii):
        inc = 0
        for jj in range(ii + 1, n):
            if arr[jj] - arr[ii] < d:
                continue
            if arr[jj] - arr[ii] > d:
                break

            inc += iterFinal(jj)

        return inc

    for ii in range(0, n):
        resp += iterMid(ii)

    return resp


if __name__ == '__main__':
    for d, arr in [(1, [2, 2, 3, 4, 5]),
                   (3, [1, 2, 4, 5, 7, 8, 10])]:
        print(beautifulTriplets(d, arr))
