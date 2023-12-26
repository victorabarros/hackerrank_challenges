from collections import deque


def maxCost(costs, labels, dailyCount):
    deque_costs = deque(costs)
    deque_labels = deque(labels)
    max_sum_daily_cost = 0

    while len(deque_costs) > dailyCount:
        daily_costs, daily_labels = list(), list()

        for _ in range(dailyCount):
            daily_costs.append(deque_costs.popleft())
            daily_labels.append(deque_labels.popleft())

        gap = dailyCount - daily_labels.count("legal")
        while gap > 0:
            if gap > len(deque_costs):
                return max_sum_daily_cost
                # break

            for _ in range(gap):
                daily_costs.append(deque_costs.popleft())
                daily_labels.append(deque_labels.popleft())

            gap = dailyCount - daily_labels.count("legal")

        max_sum_daily_cost = max(max_sum_daily_cost, sum(daily_costs))

    return max_sum_daily_cost


if __name__ == '__main__':
    for costs, labels, dailyCount, ans in [
        ([2, 5, 3, 11, 1], ["legal", "illegal", "legal", "illegal", "legal"], 2, 10),
        ([2], ["illegal"], 1, 0),
        ([0, 3, 2, 3, 4], ["legal", "legal", "illegal", "legal", "legal"], 1, 5),
        ([3, 2, 0, 2, 4, 0, 1, 4], ["legal", "illegal", "legal", "legal", "illegal", "legal", "legal", "legal"], 4, 11),
    ]:
        result = maxCost(costs, labels, dailyCount)
        print(result, result == ans)
