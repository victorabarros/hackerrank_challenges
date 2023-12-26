def arrayValue(arr):
    even = 0
    odd = 0
    for idx, ii in enumerate(arr):
        if idx % 2 == 0:
            even += ii
        else:
            odd += ii
    return (even - odd) ** 2


def get_sub_arrays(arr):
    resp = list()
    for idx_i, _ in enumerate(arr):
        for idx_j, _ in enumerate(arr):
            if idx_j < idx_i:
                continue
            resp.append(arr[idx_i:idx_j + 1])
    return resp


def maxSubarrayValue(arr):
    resp = 0
    # sub_arrays = get_sub_arrays(arr)
    # for sub_arr in sub_arrays:
    #     sub_arr_value = arrayValue(sub_arr)
    #     if sub_arr_value > resp:
    #         # print(sub_arr, sub_arr_value)
    #         resp = sub_arr_value

    for idx_i, _ in enumerate(arr):
        for idx_j, _ in enumerate(arr):
            if idx_j < idx_i:
                continue
            sub_arr_value = arrayValue(arr[idx_i:idx_j + 1])
            resp = max(sub_arr_value, resp)

    return resp


if __name__ == '__main__':
    for arr, ans in [
        ([2, -1, -4, 5], 36),
        ([1, -1, 1, -1, 1], 25),
        ([-1, 2, 3, 4, -5], 81)
    ]:
        result = maxSubarrayValue(arr)
        print(result, result == ans)
