def reverse_column(matrix, idx):
    original_column = list()
    for line in matrix:
        original_column.append(line[idx])
    original_column.reverse()

    result = list()
    for ii, line in enumerate(matrix):
        result.append(line.copy())
        result[ii][idx] = original_column[ii]

    return result


def reverse_row(matrix, idx):
    result = list()
    for ii, line in enumerate(matrix):
        result.append(line.copy())
        if ii == idx:
            result[ii].reverse()

    return result


def flippingMatrix(matrix, n):
    max_sub_sum = 0
    for ii in range(len(matrix)):
        for jj in range(len(matrix[ii])):
            reversed_matrix = reverse_row(reverse_column(matrix, ii), jj)

            print(ii, jj)
            print(reversed_matrix)
            sub_matrix = list()
            for line in reversed_matrix[:n]:
                sub_matrix.append(line[:n].copy())

            print(sub_matrix)
            sub_sum = sum([sum(line) for line in sub_matrix])
            print(sub_sum)
            max_sub_sum = max(max_sub_sum, sub_sum)

    return max_sub_sum


if __name__ == '__main__':
    # matrix = list()
    # matrix.append([1, 2, 3,     4])
    # matrix.append([7, 8, 9,    10])
    # matrix.append([13, 14, 15, 16])
    # matrix.append([19, 20, 21, 22])
    matrix = [
        [107, 54, 128, 15],
        [12, 75, 110, 138],
        [100, 96, 34, 85],
        [75, 15, 28, 112],
    ]
    print(flippingMatrix(matrix, 2))
