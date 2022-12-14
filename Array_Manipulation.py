# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

def arrayManipulation(n, queries):
    row = [0] * n
    for low, high, incr in queries:
        row[low-1] += incr
        if high != n:
            row[high] -= incr

    resp = 0
    acc = 0

    for elem in row:
        acc += elem
        if acc > resp:
            resp = acc

    return resp


if __name__ == '__main__':
    for n, queries in [
                       (10, [[1, 5, 3],   [4, 8, 7],   [6, 9, 1]]),
                       (5,  [[1, 2, 100], [2, 5, 100], [3, 4, 100]]),
                       (10, [[2, 6, 8],   [3, 5, 7],   [1, 8, 1], [5, 9, 15]]),
                       (4,  [[2, 3, 603], [1, 1, 286], [4, 4, 882]])
                      ]:
        res = arrayManipulation(n, queries)
        print(res)
