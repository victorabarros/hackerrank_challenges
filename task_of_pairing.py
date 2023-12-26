from collections import deque


# def taskOfPairing(freq):
#     weights = deque(freq)
#     resp = 0

#     while len(weights) > 0:
#         nof_weight_n = weights.popleft()
#         resp += nof_weight_n // 2

#         if nof_weight_n % 2 != 0 and len(weights) > 0:
#             nof_weight_n_plus = weights.popleft()
#             resp += nof_weight_n_plus // 2

#             if nof_weight_n_plus % 2 != 0:
#                 resp += 1

#     return resp

def taskOfPairing(freq):
    weights = deque(freq)
    resp = list()
    weight = 2

    while len(weights) > 0:
        nof_weight_n_minus = weights.popleft()

        if len(weights) > 0:
            nof_weight_n = weights.popleft()

            if len(weights) > 0:
                nof_weight_n_plus = weights.popleft()

                if nof_weight_n_minus < nof_weight_n:
                    resp.extend(
                        [(weight - 1, weight) for ii in range(nof_weight_n_minus)])
                    nof_weight_n -= nof_weight_n_minu
                if nof_weight_n < nof_weight_n_plus:
                    resp.extend(
                        [(weight, weight + 1) for ii in range(nof_weight_n_plus)])
                    nof_weight_n -= nof_weight_n_plus
        else:
            resp.extend([(weight-1, weight-1) for ii in range(nof_weight_n_minus // 2)])

        resp.extend([(weight, weight) for ii in range(nof_weight_n // 2)])
        weight += 1
    return len(resp)


if __name__ == '__main__':
    for weights, ans in [
        ([2, 4, 3, 1], 5),
        ([3, 5, 4, 3], 7),
        ([5, 6, 2], 6),
        ([2, 4, 6], 6),
        ([2, 4, 5], 5),
        ([2, 3, 4], 4),
        ([2, 3, 5], 5),
        ([1, 4, 5], 4),
        ([1, 3, 4], 4),
        ([1, 3, 5], 4),
        ([3, 20, 9], 16)
        # 1-2 1-2 1-2                         -> 3
        # 2-2 2-2 2-2 2-2 (2)                 -> 4
        # 2-3 2-3 2-3 2-3 2-3 2-3 2-3 2-3 2-3 -> 9
    ]:
        resp = taskOfPairing(weights)
        print(resp, resp == ans)
