# https://www.hackerrank.com/contests/desafio-algoritmos-hurb-3010/challenges/fraudulent-activity-notifications
#!/bin/python3

import os
from statistics import median


def activityNotifications(expenditure, d):
    result = 0
    for idx in range(d, len(expenditure)):
        med = median(expenditure[idx-d:idx])
        if expenditure[idx] >= 2 * med:
            result += 1
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n, d = map(int, input().split())
    # expenditure = [int(ii) for ii in input().rstrip().split()]
    # result = activityNotifications(expenditure, d)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    for e, d in [([1, 2, 3, 4, 4], 4),
                 ([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)]:
        print(activityNotifications(e, d))
