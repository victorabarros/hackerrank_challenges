# https://www.hackerrank.com/challenges/count-triplets-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def countTriplets(arr, r):
    resp = 0
    occurance = {n: arr.count(n) for n in set(arr)}
    for n in set(arr):
        resp += occurance.get(n, 0) * occurance.get(n * r, 0) * \
            occurance.get(n * r**2, 0)
    return resp


if __name__ == '__main__':
    for r, arr, ans in [
                    (2, [1, 2, 2, 4], 2),
                    (3, [1, 3, 9, 9, 27, 81], 6),
                    (5, [1, 5, 5, 25, 125], 4),
                    (1, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 161700),
                    # (, []),
                  ]:
        res = countTriplets(arr, r)
        print(res, ans, res == ans)
