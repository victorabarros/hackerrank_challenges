# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    resp = 0
    index = 0

    while True:
        if index >= len(arr):
            break

        elem = arr[index]

        if elem - 1 != index:
            arr[index], arr[elem-1] = arr[elem-1], elem
            resp += 1
        else:
            index += 1

    return resp


if __name__ == '__main__':
    for arr in [[7, 1, 3, 2, 4, 5, 6],
                [4, 3, 1, 2],
                [2, 3, 4, 1, 5],
                [1, 3, 5, 2, 4, 6, 7]]:
        res = minimumSwaps(arr)
        print(res)
